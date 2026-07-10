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
<img src="https://cdn5.telesco.pe/file/huH1SWU_PLgyH5k2JruYd6cOsT8i45jhkbxv7sNCIZIr8nuOTWLcpE9L-qNO2UpXxibztjQ7b1Z-GE0YO_qrcmHNYtMzh_qmvgswTbLJhuI3mgIcBLWAbPIC0QW_zm5WnPFwAtBC0LGA7O-oic16q1WyA0IpJS75Na9PKqO-dAjC0AmsthLfutcq2nJOZ0OMr8K79jRwxaUYGU3zYIUGUJaKBlWV_ntGFeeyBy9Xjxm6iyoVwrE4Z8Q_vpcxKdwbFck7m4hIxWs1ai6hpPfBhlPVrscwK7_KmcSbxstWXfAplWOm68xEzNVlTpaT4HusDPqD4olQTQAh21hoaHVp-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 598K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 01:02:14</div>
<hr>

<div class="tg-post" id="msg-99501">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961be455f.mp4?token=dEu72Oa7R5uEig2mw7uQelQPnnWEyHJ3fvuoqw8x7ooAG3UpYkJphtkuCgQfiCupdjYQ-J_NrI69nl3Pe_MVKvWU0s5ftaIRnk7eq1XVDjYlwEeW_GuTInSvtvbeq98GWs_JLN4sWzAaeCbOJL5C6Q2RvAnPqRCSHrsOYnCTiuMLLa6_UT_6N1QqgIhjDLqPmagupv0DesUQpjbD76WIDEPvFchrsTuS9wFGWiTh-FLuhhsOs7RKRC6lP-P2LGsHFtaqi6gySQSdjD2XHCzwoC6Z7lX3yrb3RvHdUu6IIywY244WSYPTudoRvNO95P6UnrhKuWqYZj1Mpd9RIxuT4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا اینجوری میکنه
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/99501" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99500">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=S14J4m3IIfErTXe6_6TN9BBHLuJGa0nM29QuLhhl7hJHeg1LhUvd2VtpM-LogPgR0wHBkVLYbSm3mi5HhXA1o1DZuadq1WZlu8SGqbDHexXYpnxnnwrgXsSsC2tn99DM7wRIdN2tvd6a39OMz0iL1INKYoQyMS2z3xHCkKV1uLNkHIh8P2_15StNeKYHmA3125_I3DoM4P1BTQ6fBnv_7cMGhhxzbUQXWJyy1LZ4QM5NqOu0F479GkY-I_rS0XCo3obTEd76ELNN6YsS3Sqsrx27hUWSJa8w43RLPfqG8cH-JhNYszLX0_UcjucAvsgjHPk1j_nzEFdSXOz-q9p-JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
MOTM
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/99500" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99499">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG3hGOt6vt2ATwBWqHA6PwyQcmQrPit-5CfjDvEvs-GM_K5N50vmtpb1JCX0LRCx0jeigtP1QsgRMSn6JIBXGrvlCLPKhyaK7WIUyGtbt3VZt1s-Q3SwWBtQ_yyfX7uijB3F8tu2h-wCy8a_OjGU5RQ4k7PL7FTyI8HNXv6lFZ6YCaLqQ-DoGTjj49_dETF5FhC1VSM5ljEo6CRtL6xWlnrIo_w51sjHv5JIp8VHhsITGzq_eEvinTp7x1We0cl3PiKWi9uZXa1LiDy3AOdxvJlxGZFjW3tVYESdhIy19WYjNqW7DM0jFTBzbAnT-mnyIuk_rZKjDbGYHxHx4bntyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🤯
🇪🇸
فابیان رویز تا به امروز هیچ مسابقه‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
📊
48 مسابقه؛ 33 پیروزی؛  15 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/99499" target="_blank">📅 00:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99498">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/99498" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99497">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQw9-x08b7-dzCEsaYxfWP3vV8-lj_xKmH3Q3_oq77AHVfSYtGUWWq88xq8fW5AWtUS9PGLwvmvGy0TytnnaWHHfs03r9nQ0nCxF6Symn9vRRF2M4Lr3Q17ewAWiq4WWa2uNiriDdqmhCgQ11QaqVhb6sTkaZS2nBbNqDmRhhxhvOU-cUMmrS7kao36EBQnPaaACqIog9V78A4y0N_mrNhHSXdbnoNb6np7rNXk31lZ5j8rArKbTBG4XriIolEj-s7gd1_gkE_rg-O3sLO5rv3LGya8qUtZYxe-VNgR3i7PfoXx3jkSQywMMiILpF0C87yCd0NsvewLLS9VldOGQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
اسپانیا با پیروزی در این مسابقه، برای 36 بازی متوالی، بدون شکست باقی ماند و یک رکورد جدید در تاریخ این تیم را به ثبت رساند.
✔️
‏آمار این روند: ‏27 برد؛ ‏9 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/Futball180TV/99497" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99496">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99496" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/99496" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99495">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZWOSisUuQFXXlIyBXUs34SLKCDjnN0ewF1L4EeGxp9f-gRf_sw10GqVj1_7BRt_Fiujqje9QgZDylzPHe_F1MjenYMufJZPVCdcrf8u-76MP2cWMDb3g-9Oru5GITRN4jPkMLOxq8qXHq-mA84Qf9XxdttZjgMbTuJX1goHmqLadendVWNlPCH_x6cdenk1XM-xAMvboJuSpv5tEVOc7qtLAbl1vvNRbSSbiR_MPoOSFfQ9zkQU-rnMc4Q75ZohmtD_z8653qrOZL303XtPWxoOjcn6Xs66Nk65bPmn-OeSXbeimKjiFbMrit0UvT7D-Bx_2qZt-uPDQdtJkNFeEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/99495" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99494">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOjMWq2tf_H4_Lv3fDjBLZ5VKkfZNJMtos6vfHxyPgNFv3i8qgKhmj-O4wJ4HXN7KaGc01kMrXbelCN3buuvbDJnLnMlZGv-GmA-WI2r5uuC_pyi68V69SIiTkCBbsFru4mai-Z-JfB-G-pWcRkA6G_1t-YSQITteN-DUL1BqJ4PhkvwuZtWXpiNq-DVjgkVUSXRPYevG3Dfp1lzzXIF8SUofhrhWUHfQavuUPuy-054vK12_twlj0sVqAVYCTY3Rne0_MciQhAVqcTW1vq4W3eqOFlq-eORRSsH_Eri7PNZbrZOVsDAUTdUulyCJ_hULszm9BbsIuJ3APjM_nvfog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
در 11 بازی اخیر که لامین یامال از ابتدا در ترکیب اصلی تیم ملی اسپانیا حضور داشته، اسپانیا در مسابقات بزرگ (یورو + جام جهانی) پیروز شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/Futball180TV/99494" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99493">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ دکلان‌رایس، مارک‌گهی و ریس جیمز در آستانه بازی با نروژ به تمرینات انگلیس بازگشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/99493" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99492">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA5ESzgKnIztBhRqr-P2qRtk37LwWeYN89CqHhDUe918HrE-nE2BIMOePnNMruf5mjeFPZK7gX6GjxQ0ZWI2UW7-mIxfLobhw91_MhDfwDcGXsRL6Ozx83zvEyteHhUofJvlYNwO_7yAUFxpbgqfDG2byOYCVQlu49QJfjb4EI4qOTc-DnPZ6D3XFSaKnNZWGY-esue6XPqiuQRKxPDi_K1-bQKzff_Ev9X-7xO11IO0_Dj0kw7Wxce0vz8Mz2NTHuMNJpiXoaSsTZSYWD6876uItGGNzY52Q_wcjDllVIEmw2kH4uXx5K4tvqPvBkVR3KxGR8RWy7fyiPJkfy2cdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/99492" target="_blank">📅 00:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99491">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_zTBU8yaR-g0_kRIetrvAKwGRl4O1JLIxHoiPfS9pDiCCCr6K9krbjw7WfXR3SlVynnfViSW0mar3rJeHMugikxeBF5jI92tdjKqv73Jhica_OQ1xO9rCe4tUgzXMQV-_J8_SU5PUPxRtJ4QOK6nKMchpA-cnVv-cMfDruI64xqN4oPHa21i1otIwYM6cQikLozaAhsjvwZAw1IpvlwktAj85A4Ds5oLwkxn0wTCcIuCcDaPr9baOjk01inFqQ-TnifiZ5-zw8f7rG64tMGBd_K2FWJ4GOkhIOdqB2vIzk3JVqVWF1c6jE6OH8oZ45-7TijuuXif1zY34ihk4DzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا پس از سال 2010 برای دومین بار در تاریخ به نیمه نهایی جام جهانی رسید
‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/99491" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99489">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEKuBEDmLpITb2pWEQ2xVwAwyVKGeP3Gk-UEAMyq5pxTCor_znyBP4Kob61J_IvleUE1prGi0Aqukv5ohNxBeqd6dzbx8mj1OqxZbwuMaM5WVqJ2XXjUE0xfzzPNBt1qA17C3SQu52YK2l8hDwhMFXfPIsqgmXilfKhilo1tlCQifuRHF25YP0g4xgEM8zTP87CRGIN0RKjHGSxdAX2VdpWIXe3jZwqbK9Ivo2tSXC_UrgBU4dw4BovIVggjbwoj5qwS7jZnFlLPlFZjCjFo13Atpq2h29xi9o50bfF6lZAudxB2agoRDWL8q3WhnkiDWE6bPtWFI2McODzNyU-9gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PT4oPHZOB-3mQTEQp5flg3xWq9C_uv0iKmzMw1evXkeTZk0gAW-3C0ysQ-MS7gCfvrsWifVKS5wZ4qQMuZEGuhroS-E-bnOwv0GS5kJ2473f4ihQazHk5Lfhu41ab9w01RQrLVz6hWxLb7j6Fi6p6Fzjati2LkOpLiEpTnowLroagbzpMdthcu4n1P2OLV_Loxcq5BB6Q5krjxp5LhQZ0nhtjahSZoB_yinLGmB0jrDHdktIYXZOoS_B-80ik3JBMvXl1E0vuy4d16tWIB0OhEX3nfx5KatszxCkEs3vop6Kq7cXSZvi9K62Eb6EptB7ZbbpS7YkTIP81EMfv0ZyGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داش یامال تو استادیوم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99489" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99487">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1PySIOxGD9yMdHPu32e37v68Mpapoo6XaqR8s8Ck5SIUcBNL2mpZtZs9s5tq47d6BUTw4rPbE4alafF84yVOduY4VbcT9z6mcjJZPN3-aQtZClngzkPob1lIVG4ZbyHhtyf4l6dCL2RR7D_ic_W_KCKymGe_xN-4MnrfNpLLoC26wLnv4LE69M8D1oFWvY-2Ft_rXs6pSHT-YobPSTJtDZHzw1Drq68TKO1p6dKe3nrcf9MhRskoYZTZ7U32l4MfOiCjBy5-7rKIXAwbdpquyRb7_KViPSTIl-6qmYbl4KzmDPn-0rEe3aDrHdHP1b3I-A1SiejJBwvCxBQ0nvsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
🏆
🇪🇸
آمار بازی امشب بلژیک و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99487" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99486">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnyQ_dIq1Vpf1hM6K8RYA7iiHlzyxuImXHu0CxHSq3o-04m6WBdQyRgIwSdz7coihDD6Xzd0Uf_rIhA-vNj2gfy2KLWmnZWuYgxSSyOAaprWotwZUWqdnhOx80JQRsERVP-2bqdE1jdC3F6L6q-SyE_MujJ8g61bypnRvyhc1IteaA2XXn1nH-v6jwa8CCBf0v2DtIcvQvlYW48fY9rL3vNP6mL9y_AOSYDkxlTA9xfa-mvthwgm6bZ7ReXzae8tMsGEtjw98fuAj-rmOhwpKoPEhk_PPWMToesxlTwgo_2PHsiFPcXvcSVcoMcv0JlBYqux12zMRt4EbSVZMklYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار جام جهانی؛ این سمت که واقعا جذاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99486" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99485">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiU_9nnOt43V0idmBkeHKF18SuGl5I5XPhdy6I945IAskE14n9pFhggfYvJc_-l81bNzBuBWQT_seafUu5ki4d6195uWadnxZuRAsjPI15Ayw_NW9t00kpnoMwG-FjK9twP6guNAQr64xbFpYCQoCZKD5o7xi2aUShT4tEeYXkNpw7fzRw5hB7KXdTSv4DU3cFtW962Fh9K64Udpsrqf2eY6GK55g0etyV7EwPdpwIEqrtkC0EJKcdWx2-ZvIIx1u5lFIEBU73FiddMENS-qtdu5GE_v1jqXa9xT-CS9gaoHNIU2qfGouEw84LWXYJbarNRbCkiaI8gkJQ8IfBFedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99485" target="_blank">📅 00:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99484">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVyoqfNZ6-L5FZhszf0YiC2KdFH8tps5DWv3yU1oP9WP4SqVRjhk6U5ret9TC5vHlhkIcSmKp57WE2SorZMiqOB3VH31n0XBSCzg0LgMxhZ-EEwhMJOrPA1bPZCBuFgzSthKXBaODWZdLEYFUeXJJw75a64So_vyXE8Lv3ZApwfpHGS0ivBPLv-HbaYsZUqxRSaq9I2PhKWh8X43t5ZvLDgjGL5akYOB9wmB64JCkA057wNBeuVJ23uL8Ztqewub8GmWz7VoqeXU7f3UTSf_RuYWLW-CTXPuAYmUIjMAFYt4uZl2tMb4ePHE2l-yObZOvQyz8JoG_ywZDc0EEdlteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99484" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99483">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCLgKddncrHOZbaWfu_R98jcXaIsi6qemro2egKuVw5YSRvZ5zkQvI0o5Y_zilyQ794O7sHvZl9EQ31elMeV0yOE-YefyGQW5l_UtP1fYv_vgNwOSjeBn7O0XuqAGGIoCBmoidsmZGnsAL6drLHOXW5w_LZKfWaaWR6UJ_5W4saGIAVkldTM9ENETFryC0oL7mul96ZSA2tM2ANn50XN1V8QY3jypDA2pHYtZNNy4S1JqZqXxWDbbZV9MoOnZIQXRFWvbpGc2BMaMm4TgRNWW0sXgcr7QrhWvx5BJQUbgd1lMSSmI7A875qTR0VkvGYCIPenlAbp3OgcVNz_lmrVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|داستان اسپانیا در جام‌جهانی همچنان ادامه دارد؛ راوی قصه ستاره آرسنال است! بلژیک در کمال شایستگی حذف شد
🇧🇪
بلژیک
😃
😀
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99483" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99482">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پدری ریدددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/99482" target="_blank">📅 00:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99481">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چه توپییییی در آورد لاپورتتتتتتتت</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99481" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99480">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99480" target="_blank">📅 00:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هفتتتتت دقیقه فقط تا پایان</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99479" target="_blank">📅 00:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بلژیک اونجایی که کورتوا مصدوم شد بازیو باخت</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99478" target="_blank">📅 00:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XGxNgGyWrgFA2kDrnO8KV8iR1ysqttE4ghLSG5yRuVGiQ9dHBFEm3KYIwk46myIE9DD2OnrKFEgSpDf51agLAJTEc5AvnGsFzJYtlqv3HjpnxSEhJxg4FG27O7jh8TOievHm8xWj2e6MYUiE6tLU0VHYX_4ddvFgFNbV7dv6nsK2j9aJEs2jPfEhhhfe18Lp32KP8huA2XbLyA1rWENczHZSooAN9eu7IAGJflcLOpqikeF0zuO69v7J9X8mgnhw4e1QKbyE1BxKA7rVH3gZPswvax07-o66PF-K23OeP_bN9XqX8Q3oVdESxFsy2iB_3BYaGuodkNZLNo4yC909DU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4b3fe7a64.mp4?token=PtjeS38ETg7GFwUek9gDST3nlTl9nHfyFfhFdGnPrQgFhAUq-EzP1KeyVR_HbQY3SS2hY-wWjQyK6sUON-MmOKrDX2Rh3qQFAVfuhUXolB6NiESQIwF5PwdIboEV7palqwSlLXA8Vy40bMPkWP89BZGwBxCTxDF1kV8KvNhqOcZMsujN9rFYnZOZEHMSrHf2EXDy2khA_lwstc5Q0gm_YpVHOVqRqgkZO8M55-Y83MRAkv1kfR70-edW-g3P3KfBt-Fek-2OWLrOGLCGuGIqlh2y-TeDFQdcegGOudUGQk7T9Ru9-tIe54oNR0tC8gJzYr1Nldx5GTY9LXOEyq9b1XGxNgGyWrgFA2kDrnO8KV8iR1ysqttE4ghLSG5yRuVGiQ9dHBFEm3KYIwk46myIE9DD2OnrKFEgSpDf51agLAJTEc5AvnGsFzJYtlqv3HjpnxSEhJxg4FG27O7jh8TOievHm8xWj2e6MYUiE6tLU0VHYX_4ddvFgFNbV7dv6nsK2j9aJEs2jPfEhhhfe18Lp32KP8huA2XbLyA1rWENczHZSooAN9eu7IAGJflcLOpqikeF0zuO69v7J9X8mgnhw4e1QKbyE1BxKA7rVH3gZPswvax07-o66PF-K23OeP_bN9XqX8Q3oVdESxFsy2iB_3BYaGuodkNZLNo4yC909DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌دوم اسپانیا به بلژیک توسط مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99477" target="_blank">📅 00:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مرینو عشققققققق</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99476" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چه شاهکاریه این مرینوووووو</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99475" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگلگللللللللللللللللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99474" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گلگلگگلگلگلگلگلگلگلگلگللللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99473" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گل دومممممممممم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99472" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اسپانیااااااااا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99471" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مرینوووووووو</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99470" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گللللللللللللل دوممم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99469" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99468" target="_blank">📅 00:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مرینو عشق پرتغالیا اومد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99467" target="_blank">📅 00:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=pjbjVISQejHRto4x8zm9UteYGcuQfqLTgH99IMPEv2pdWzyS_7brYjee8FiJg-_ZhgnpOgdi83TR2fdqY0qyWB5seU2WXHNYj9668yh4wB_-GAJSw2nCswUMseUSCe7e3og0buqGfr4KlTbfVOD0qfub-zdkgyRMwovLDDCpnqPqxx9owShE_lvIQFAj3Ao954uN05G6io92PLJ_8WlfRsBEkSRtZaUbBb5hW_7IHZYKLRAnyx3AvzYdGpbohqyolC9iTqRDD1h4QWfCbcMGLfW8qqDUKJF2XOrmM6oWoeMZXUZeDb5iedbys9_vsFMq7DSfhuGrnuWPyrEmIGbfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6497dfae.mp4?token=pjbjVISQejHRto4x8zm9UteYGcuQfqLTgH99IMPEv2pdWzyS_7brYjee8FiJg-_ZhgnpOgdi83TR2fdqY0qyWB5seU2WXHNYj9668yh4wB_-GAJSw2nCswUMseUSCe7e3og0buqGfr4KlTbfVOD0qfub-zdkgyRMwovLDDCpnqPqxx9owShE_lvIQFAj3Ao954uN05G6io92PLJ_8WlfRsBEkSRtZaUbBb5hW_7IHZYKLRAnyx3AvzYdGpbohqyolC9iTqRDD1h4QWfCbcMGLfW8qqDUKJF2XOrmM6oWoeMZXUZeDb5iedbys9_vsFMq7DSfhuGrnuWPyrEmIGbfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/99466" target="_blank">📅 00:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uN8MJod6E1NEcBGBpSDxW_5HoMYL5d8fbKwEmXqBEZ41c_AohbkpJtG-1sGXHPKwsm_o45bxHLeRntGcfSykNjs3RbVih3DOuHMqrGGJ3hgqhHOhEYzsNhOcZA9z5PFU-CpQBq-c0EgD47ip6U_qQ_hfl24KmBV6GxmfXEIRbtP1wElNYG5hZHaVYCqifuFGchRmqj1dexsEl-XuFK4Ycu5zA6_7rcVOX19YW_5qG9MuaU_2LFMebIM9EPgD7BhY-WvrOg1t5f6GPh0CJ4Hdvgy_WbZDa8OHzNOS1xNMX3Mr2NYfUaGMxvBVPwQtWp9lwriYBv_M4Jitbp42L5NdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گریه‌های شدید تیبو کورتوا
🚨
🚨
🚨
🚨
😐</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99465" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کورتوا تعویض شدددددد
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99464" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دو تیم خوب بازی میکنن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99463" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بلژیک چه ضدحمله هایی میزنه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/99462" target="_blank">📅 23:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آغاز نیمه‌دوم بازی اسپانیا و بلژیک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99461" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99460" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇪🇸
🏆
• 10 گلی که اسپانیا در جام جهانی 2026 به ثمر رساند:
6 گل در نیمه اول.
4 گل در نیمه دوم.
🇧🇪
🏆
گل‌های تیم بلژیک در جام جهانی 2026:
‏4 گل در نیمه اول.
‏9 گل در نیمه دوم.
‏1 گل در وقت‌های اضافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99459" target="_blank">📅 23:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh-JF8mJqgrp2_yqLMYg-zEE1hJb2T6jKQR_qIukYiluTHoUUDJbvq9ok_iqRbU3Qvm1YVCVzmuykUKj3JiDZgdPYJYAy53AGAo0Y40OgkGuf9ITvlXB72qMEaNnEvrNgWFsjo5DfQsARkBVVglB-4bAqagmxBhx1Ns1XVswQD37pTXPNPMPLUmSkm1sop9wZzpDis0gI8Ur1HTqWary9rbsKmGVFtDnMeMRPQVxJn-pGPWw2GOGbOoGrC6AC0RRANzijT9DBvGPj9D5xKFOetzzfdAT3TO9t0WUTSNDWzXVy2hm5uSV2wvUlsDaRErBvhHW7A05XhOtZte3fx9HIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇧🇪
دکتلاره (با ۳ گل) به عنوان بهترین گلزن تاریخ بلژیک در مسابقات حذفی جام جهانی، با روملو لوکاكو هم‌رتبه شد.
🇧🇪
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/99458" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 بلژیک 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99456" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99455">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🔥
گل‌تساوی بلژیک توسط دکتلاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99455" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99454">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گل تاییده و موردی نداره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99454" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99453">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">چه ضربه سر خوشگلیییی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99453" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99452">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مساووییییی بلژییییک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99452" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99451">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99451" target="_blank">📅 23:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99450">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7LHZ82iB5-UUn1bAuT_v9RlQrkfGw41O7DaSeaJdw41y1_9DnNkq_ox0o9kbT_fMqjB5S8nS_yaddeAGLXU32NXihTuTvDv9vqxOltkzDft1MGtU6ul-R1bs0Z0d0D_3Y0anZxboJ7tyF91vTvsBZ0_lG__Tx-wBkLnlqtRkxjNvscIZqNvb35n11abDw8jGfMiNTuKsEVJ7_RNRpyaK23WlpPSp8388e8HKkz4s29KxJQYKeKebeiuFSeLc6Dq5uaC4zZd_b-vAbWf9fnsoWsHs88Tgl7E-OeuQxFBuEnn7p4EpFyaST2ngwngTJ0IwDUaLqm-pVm7T0cj4ymaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور برد پیت تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99450" target="_blank">📅 23:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99449">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خوشگل سیو‌ کرد کورتوا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99449" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99448">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چه خووووب زد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99448" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99447">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99447" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99446">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چه بازی ای میکنه یامااااال</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99446" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99445">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یامال دفاع چپ بلژیکو کرده قشنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99445" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99444">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خطاااااای خوش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99444" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99443">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔥
گل‌اول اسپانیا به بلژیک توسط فابیان رویز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/99443" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99442">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اسپانیاااااا فرانسسسسه داریم نیمه نهاییییییییییی</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99442" target="_blank">📅 23:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99441">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ببببببه بببببببههههههه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99441" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99440">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بالاخرهههههه شددددددد</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99440" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99439">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فابیاننننننن رویزززژزززز</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99439" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99438">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اسپانیاااااا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99438" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99437">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99437" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99436">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/99436" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99435">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEYvYQH4a18trmPAM3INIl1uSH2sgFjUMIwVo9sPsgJjcKnDgha5N4rZUY9qHqQFbI1b0EB7KxBdexCcbGlBlUliikPiyXjMbGgJ5XC4OWpWPKSlSD0fH6HJ-iD5J5bwYjuHkGm3sAIOExFl497AsJBRrJfnal2J3j21g8K5h4ZppQhz8PGYAbL18Q1i4KXkQJrNI-nUewR5n3nPwYdezk6eVpgvdula1o6MNMcZdwYkWbHUAxJcECHJyz2tJoVFAiE51dxzXqe8dRwp8UzE3l--pU00r-yfhdA25-3ABk3VI3QqqL4yaan12ZoxgSsxNlCIXO3HN7JjvgHuXXu67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
#فوووووری
از آرشیو وار: پنالتی اسپانیا مقابل بلژیک گرفته نشدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99435" target="_blank">📅 22:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99434">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mlqe9J0iuUaKbDIY3OuwwHAwx7ADpEC0rJVVqBNIZDrNhizsHuMhM3l5t18aD_AaImZ-s0pE9xkuMvcHQyt3D8IvT7bYKqrfYhympatOI_kMNvtYWkNANOsRYr4j1eUgpHfSJALN3R8NiUCGpNqWyYqKlYPZS6b-VrDyhu5xSdS82UF6VBLCykfhBn_rUQ8QRUQV1DG240SVMxUNH_ExLgeZ6psmEknNWX8Nxmb-RqUFuUQNn_ZCAGEvejegwbjJLec_GwybOrXmOrUNO74uRmnrP3NM8v6kZXl2S1bPyrkDtBD1lItzHTpW2mp4VMsOFyihDdwUklTwDqlSRZGgkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
پست جدید رونالدو: یه پیروزی میلیون ها میارزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99434" target="_blank">📅 22:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99433">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKtKfmwHxZjid_ywrdEZ8ttzWOpEl3xMQuURFxEnL_LXtWTbK0CX6jZ_4zR82mClRR2-QOd16FMT4HQesZCOwu9ErhuoALezH31YkFUnJGrs30aWKu9AsFePKGo-CA0V_7CdyA0hNpMB_t25A-jEdNBGrBZBmTFjfKl1Sv2dDm7nvn-ixHbq4RRbVY4kn4LMj1Wp7QpsBAdqycylZHYsyFMuKYMq3jf9bIVuv74KDvjmpSfuENoyo3RqHO9EojzRtrt6S9YIwRdArHtffxIsAj5ZhBy-omyAz7FIF9HTG95W8uI8NOMOKPQPz3QrxAkNeZ_rNoiRdTEU4N1fsnNuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر یامال تو ورزشگاهه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/99433" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99432">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bet_maxxx</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/99432" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99431">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAZK3Jqfv63Z6CpcRKjogyU4MYOzpSMI7ptsidAYgCgVcRL307cSzF9RuQb6TLx2hdg8y0Fa14JHkIIGhx1DLtOmHR3rgR2FHWkI4a98Zl4kqvF_VZyJc360KJvy-5zfd5sKEDyxQQs42AW1iCsudZz0PEdUFSso_QrE2nkg717a5fbodAzN9Cl29JJuMhNr8K19zwth8rFfmUTBAmr9A3KBmWwX0-8899WO_NPu3itE8SOF4z1ZMzqX3KtPcBzr3MuuTuYAl2wYewAtO9K6MyeiEmF1eqTsS1tdPNCIzC1NLeQjDNemXR8qzTuWkNPTHvFhvKpdtCb5_ezMZPbipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bet_maxxx</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99431" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99430">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بریییم سراغ بازی جذاب اسپانیا و بلژیک
🔥</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99430" target="_blank">📅 22:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99429">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇧🇪
ترکیب بلژیک مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99429" target="_blank">📅 22:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDqUO7jevOOMQ3JKtqpCEerlsZdVLn6T5L6iqZ4SIzHPsBfCHRP98exfS-r2gDD3BHYg6yJiANEnZnXAS7foJLOy-WxUadPFo6TL49sKUckcTF3MCiYO-iSyZTKXSdz9d5B0r4Ss7Fl7k-knK9jjia6gAPd6OfY8nftFY0MGqGn6djE2NFTyGfQ3l86T0ZSguO-LgPVWzF6itb7Xj61tqj6WMekMa-2VcbG8HxsPntsnbJUHfrZ__0QCOqS8-6ABd6YZRSmAgsq0w01hrkqLgqTC_Zf4V6wNFTVD__Tke2t0NRY5xuaK8VEn2NAn9janagUcTwBnQifxMbdZ2Q3JSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
📰
فابریزیو رومانو: انتقال ادرسون ستاره برزیلی آتالانتا به منچستریونایتد منتفی شد. این بازیکن به این تیم نخواهد پیوست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دلیل لغو قرارداد، بروز نگرانی‌های پزشکی پس از انجام بخش اول معاینات پزشکی بود. (این نگرانی‌ها به ویژه مربوط به آسیب قبلی زانو، به خصوص آسیب غضروف مفصلی که در فصل گذشته (2025/26) رخ داده بود، و همچنین تردیدها در مورد سرعت بهبودی او بود).
تیم منچستریونایتد از نتایج معاینات راضی نبود و تصمیم گرفت این قرارداد را تکمیل نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99428" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR0XTYFVQU-b76nxR1RNqOzz1k3ULiN1lPnzrmRDBIppUIxloS4GwSaJwt-IVabPwULOb9DOOsRmijNjXk6hY6PUf7mA4boswdGsjFR9kN5m3PpR9L5UESn3loCQkAQhBED34uurhFJtL5rpGsrKDU1f9FnBb703L46wB0M1FEfP34A6aFKok2JxN2JWy-Veg5YqM40E1F7C_ymZ3BiPcmuMoh4MC0stlvLIwcyd2htYQgzX4t1Me3QT4XoGKH6cfzj24m3MfZextlki8tlhIR72Hd1bPKTCu_1Uk_CPD3ehNRd8akKRi9fn-Wl7fGxbZp9FW6rngnRe_guNHh4wGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
علی‌تاجرنیا مدیرعامل استقلال در آخرین صحبت ساعاتی‌پیش خود با سهراب بختیاری‌زاده اعلام کرده که پنجره نقل‌وانتقالات آبی‌پوشان تا ده روز آینده باز می‌شود! هرچند به صحبت‌های تاجرنیا نمی‌شود استناد کرد اما باید تا اواخر تیر برای اتفاقات…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99427" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99426">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=dXHpQiIAlZLYfhGOI32Vu3h5r9q3x4mOSzHOF0YUfXK768dq20jK3Uia2n3p4gNHqxLcVFsjhVmVivF6odzyjh-Cc6U8H9SAZUUEX3PYebLdDOBeSIs0Plf5lEeNjz9x-yy-pjF_pY5jarFHOFPZcqJk0tDtK_4-NZYU-oe0wWgUVPYCenExmdN4Um7a28VaWF95XrpaDDK2QTD70ofx08PLSDw6EwT7UbuTuy-I8oOWKs5e-UkRPQ2fClQ2Ubss3IlAZQwAggj4D1qUHQCO8AWoxOmuPgRiLE1BddlWKT8uAQW43-OCi3UZzpwVRWt45GMudfd8ryiY9Wsjkhzs-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a87c3f99.mp4?token=dXHpQiIAlZLYfhGOI32Vu3h5r9q3x4mOSzHOF0YUfXK768dq20jK3Uia2n3p4gNHqxLcVFsjhVmVivF6odzyjh-Cc6U8H9SAZUUEX3PYebLdDOBeSIs0Plf5lEeNjz9x-yy-pjF_pY5jarFHOFPZcqJk0tDtK_4-NZYU-oe0wWgUVPYCenExmdN4Um7a28VaWF95XrpaDDK2QTD70ofx08PLSDw6EwT7UbuTuy-I8oOWKs5e-UkRPQ2fClQ2Ubss3IlAZQwAggj4D1qUHQCO8AWoxOmuPgRiLE1BddlWKT8uAQW43-OCi3UZzpwVRWt45GMudfd8ryiY9Wsjkhzs-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید سیتی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99426" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99425">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فکر کنم کیش انقلاب شده خبر نداریم
😐
@sammfoott | پروکسی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99425" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99424">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siWeY2AQv-qqTWNs8gR1DztvIWKXSPinw7l9NNQJ1ejkAof602-FhRO6IJXaQlxj1D_7ehSesHf0MjB2f2hpAM5QTb8wrG-S7QDIRzcioeOW18nGvv-4eVBhYC97CcNWHJUW2O72kbAKrwprunzCPSzynnowqAa8EboKEO3HExEMD0ipDDor1T0lAJeiTM2ev0r7k6H5eqFhDe9aq3sExeYFF7e4XUCHtbRwSlPqMllQ4cBW6vDPjZRqHyLzJlUFCFvYeQdc-hn6_GsPmmv5z4MLmw9bV02RVzmV9QUPwBL6DoaGHi1PqjHA7hGrmsJBnXVimaQlF3VxzYBQcGa0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
هدف مورد نظر بارسلونا همچنان خولیان آلوارز است. قرارداد آدیمی، تاثیری بر تمایل باشگاه برای جذب یک مهاجم جدید نخواهد داشت، چه خولیان جذب شود و چه نشود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99424" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99423">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3OvdcZ0NimiYivwElrW5XKe42e6NWbKdMKnXLWe7aNnupnLg6_5Usf-x3Wq3cYxuwaAzk8b1FmQN3Lag-u9f4UZ-wAIo_494xEdvQj2y2eqpmoQERq374TF6o8itrEe1U0VuQDIq0dKZjZrbRMMiU45D4T5oiMZ25a7JEDzTY_7Je32QWytAbaODaYNpdmCLdswy1GeoONnsCmv7kRFXcAgsC1GNaSpbVf2CfaHGtVDQG0wX9dg_jgHGkcItV1XC7Sivl7CrHkr5i5TqhFweL1d1af2LaDZjYMg5qdvRgWdsAXN9tfi__UGybeeDLY32WhgYv2Wq-xD93LFneqc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99423" target="_blank">📅 21:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99422">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQqe8rP1WOYYHfBgz278DIFuT3MJxqbxyJzzrQ-1bBFWZyarJLy-Q8q4fbenVDGW5Jgnh6Q8Ugky1cr4Xvn4-U2Tby0znsQd0JVCtkJ4ZJsaL3Uw4jPbwfCZIhfKKJgpy0tV0Gu-HTiceHWyqrXUZ3mt3hSYtwpeG-4b5o98adA5F4s8xO-o2p4fTpJbot74e-M0S1BrTim9pm-49rOWb9-yKpScGOwpELyLz3-e1hwsfPAUnpv4ZwD_gr3rkDq2-NWEfw6W7ldvPU-1BJRfTDEnmY3O7NLAUmfSuxNsAt1TJc-1Zjhvs3mOEQ9lpUJmuBkCwtuZvbtPhb6yejam3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب اسپانیا مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99422" target="_blank">📅 20:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99421">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=NRaSH4dal0imc5mvSSCY2-ZiZyGpVjbC0bE5V15_0fQM9ZYKKZVm1enr7WzbJijn81Kv41-w1b7M5OqbMdI91BeTF5UXF-M9F2Z9p_ITc6NaNB3vaeP3seJ6Rd1AyDW_RfLN-wIbfkXZOr5vgWm4JAXxMz-3RaYIzqBBqjInd4fA6c-UnwENU6ON8oWYWbvVctnawYH-R8WZUUilPBrJgLzaBHhIsNFKij6FFLcDabaWIh2lKU6jas8zHq14-pRz_OWSMm2FKMslf8LY41_G00UtaTc4nwKlMbGwKl_dp08t8UVCzdhFYxkTAy-IlBDUjyMkJ-0yAIg-ZersjqVg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd631f7d8.mp4?token=NRaSH4dal0imc5mvSSCY2-ZiZyGpVjbC0bE5V15_0fQM9ZYKKZVm1enr7WzbJijn81Kv41-w1b7M5OqbMdI91BeTF5UXF-M9F2Z9p_ITc6NaNB3vaeP3seJ6Rd1AyDW_RfLN-wIbfkXZOr5vgWm4JAXxMz-3RaYIzqBBqjInd4fA6c-UnwENU6ON8oWYWbvVctnawYH-R8WZUUilPBrJgLzaBHhIsNFKij6FFLcDabaWIh2lKU6jas8zHq14-pRz_OWSMm2FKMslf8LY41_G00UtaTc4nwKlMbGwKl_dp08t8UVCzdhFYxkTAy-IlBDUjyMkJ-0yAIg-ZersjqVg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
سرقت‌ گوشی سینا سعیدی‌فر گلر سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99421" target="_blank">📅 20:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99420">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7B3gR9BorVqmDqtq7-0qXwIvBI6qEpMMlrvl-oJZZrBQviU8BQfLkok8jk1QraP-g9mFUO1DiooX9TPlYo-WNdx9dquLk-Rok1HDP6v9l29nMMC_VLoPtPwBVFYNvS9RHyP3AlI-Dwh1b_3_R1blYo_bspsc41kJSBLSL7j9ipf63xrCAUAuh_iUpKGdRe69AtdTTt0AzZEZ2_jwOaLXu4HajlHKnUn0C8L8e9dLzq6-9wpgMQO0QX-lKq9s0aUOqA4M6eWx1NDgacu0kYd1FaGuDkdqmnqg-gBSSgVqH1Iu_R4iXwAOE7bStFzHgIZReS66BxJQnxCqx7V_3mmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99420" target="_blank">📅 20:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99419">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1gN0NqXimey_7LxJIZ9bHszNjKDJmVCyhQRE2gwlu068JSBHWnXYVksXisb5EX4WQi0CO7mrXdKlqYWbkeBQJWmKyXxrP-i136XVU0yHZuGz6FZmrwdByrt2F_VyjxlHC11PElrB4ts9u-MhcWRNFqdNYFlEyJt8VBtBzzqRFoP4O9tZElWdWRiPhIIbKHwhI_s_3EAyOUBBturAKAV7Lb1y-k47Wk_E0XVtAEpiWGwEfxRkewd1uL8lGCSsCO3ikKgxLZJk6MU1E_SMeFNpNr0olhpNxOZzrPfplEnBVfZEYFgbQb5VqRqkmNTifcj5OnyG_nS5x7XHXGdkPQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
👤
استوری رامین‌رضاییان که تمریناتش رو بجای حضور در کمپ استقلال در کشور اسپانیا پیگیری میکنه و اعلام کرده که بزودی اخبار خوب در راهه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99419" target="_blank">📅 20:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99418">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBc9Z1aEE_Neb1AyCiFNIdCE8VJzKiK-EHsj8PZJojr268ZJyMOtZqJt1zNGoa0TqD4KKovXvhMkx0dkmd75bqTCVOTn3LZ14YvXlsbgh6wo9CCpV3j-pJSC-WRQUF46eWnUAnoViqY9WaTD1thzfDI1UYiq4ZJpQEctQmLeSHSMDzp6W4CXTizMgiV0GPOYTmIe1IuNz3a6hsLiSNjT8TBYiuoNbFv8HO-hDCvjrPrIOTvffoiMx-FTW-HFttcpybHGXlzpwS8UjuuiuHLLiQaTPaiZSD41f0igwb-n6ZLrkzAjL1K9w6gvglE9T_W4k2g4bT8OriFjuQvIInRH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مورات یاکین سرمربی سوئیس غیبت یوهان مانزامبی در بازی با آرژانتین را تایید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99418" target="_blank">📅 20:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99417">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/99417" target="_blank">📅 20:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99416">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔥
🏆
🇪🇸
🇧🇪
تیزر فوق‌العاده از تقابل امشب اسپانیا و بلژیک در ¼نهایی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99416" target="_blank">📅 20:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99415">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=UoQPpbGZ4sjzBdG61pApJPGJzQfJl9B8GJfslfQEkt6lTN6yctIntBbRqhoEdWXSVnujIsZ3UcD9kx4qn8marRk-5EkzZK-DNKPJV_ulN_1erA6Jk3GZ1WpWXWEUVksOkiK_sRorLcHqkoDLmnxVF0Oaga_zSLn44VdOBqc6AabGNgJZyKUDNnVYCnhtqmjhEK2YI5MjaunteD_RDAlRnHrD_Ui7WCpjHmydF2K4y3NkVdr3EptbQ_NkxXC5rCj19YjX3bzL8ZbMmKfO9Z42k8ddXgjPKUbRbSX1UHjC9S-MAHN2w2-zwvQgVxhJcBRF8Epl0thf78FO9uQjUkhXfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bbfbe87.mp4?token=UoQPpbGZ4sjzBdG61pApJPGJzQfJl9B8GJfslfQEkt6lTN6yctIntBbRqhoEdWXSVnujIsZ3UcD9kx4qn8marRk-5EkzZK-DNKPJV_ulN_1erA6Jk3GZ1WpWXWEUVksOkiK_sRorLcHqkoDLmnxVF0Oaga_zSLn44VdOBqc6AabGNgJZyKUDNnVYCnhtqmjhEK2YI5MjaunteD_RDAlRnHrD_Ui7WCpjHmydF2K4y3NkVdr3EptbQ_NkxXC5rCj19YjX3bzL8ZbMmKfO9Z42k8ddXgjPKUbRbSX1UHjC9S-MAHN2w2-zwvQgVxhJcBRF8Epl0thf78FO9uQjUkhXfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هدیه‌یک هوادار برزیلی برای کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99415" target="_blank">📅 20:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99414">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=MykhkX3mE5yY4HVCLzXt8TnJ8PzOSTqTSEs_JQK6KUz2MytIfz9p8gKIwD39VR6BYEHYLCkZ0ts1VLlbPO-cd_sxi2mYTgJ1-_cFW1d7WtJnCqmaLa2CC78K_W2_w3fQ31FBEbURZv_9bEuGzB47r0wOlUZwOqUurI0QW5EsJcfGwZ6vEUeBIs3pwq86uj5qOedVu12Ns1YYnQs3Ncc8n1dXW-JA0rWzcba7IiaaqzBBSL8LmE6P-zZ_XS1Gx9eIFLwuzjs6ywvdPcHZZY-sR92zhdK7hWUPzdMofq0inY39Gk61J21-CIbh3bm03kYL-xI6ymInori63Pj7553KBRq_D4EkH77MC3u7ioDEq8bC4wn94ThwkLW1ypXAd8jePdUrgplZjF0qXAZnXM5rar2yDbo52PNtsS69vGmxjJt4bI_pAhaFwWjkDl7znpFXYCP58o1dPzOnkJEl0Rww8Vaa6P1uohEIDHXhQpyWRDDqcVIukgGFBULYl1sxQpAibKYRe1pJzoKmcw7SmMpSIYikXghMpBM0oQ_fZC1g35z72R_8A8y0gOcf8eNNPufP5PIRx_uKc09YadKHcLiRKS4xB4X216BJeMsQ7t2zy7j3-6fRgv8dkC7UOoucxxT3aXldJKb2A2pVj_8gic9w_G36T1eDb57ROtGK3qLJp7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd28a0670.mp4?token=MykhkX3mE5yY4HVCLzXt8TnJ8PzOSTqTSEs_JQK6KUz2MytIfz9p8gKIwD39VR6BYEHYLCkZ0ts1VLlbPO-cd_sxi2mYTgJ1-_cFW1d7WtJnCqmaLa2CC78K_W2_w3fQ31FBEbURZv_9bEuGzB47r0wOlUZwOqUurI0QW5EsJcfGwZ6vEUeBIs3pwq86uj5qOedVu12Ns1YYnQs3Ncc8n1dXW-JA0rWzcba7IiaaqzBBSL8LmE6P-zZ_XS1Gx9eIFLwuzjs6ywvdPcHZZY-sR92zhdK7hWUPzdMofq0inY39Gk61J21-CIbh3bm03kYL-xI6ymInori63Pj7553KBRq_D4EkH77MC3u7ioDEq8bC4wn94ThwkLW1ypXAd8jePdUrgplZjF0qXAZnXM5rar2yDbo52PNtsS69vGmxjJt4bI_pAhaFwWjkDl7znpFXYCP58o1dPzOnkJEl0Rww8Vaa6P1uohEIDHXhQpyWRDDqcVIukgGFBULYl1sxQpAibKYRe1pJzoKmcw7SmMpSIYikXghMpBM0oQ_fZC1g35z72R_8A8y0gOcf8eNNPufP5PIRx_uKc09YadKHcLiRKS4xB4X216BJeMsQ7t2zy7j3-6fRgv8dkC7UOoucxxT3aXldJKb2A2pVj_8gic9w_G36T1eDb57ROtGK3qLJp7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
استقبال پشم‌ریزون مصری‌ها از کاروان تیم‌ملی فوتبال کشورشون بعد بازگشت به این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99414" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99413">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/99413" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99413" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99412">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHkaqOwmRCl9SiHWV5-CM94OPN8QpXxc1jbMk9DS3tok0z4CgJAaO8TCP9n27qqxlap7Mykpg3grCMUp8QYGMfXWumSV-TM8cpNJCeq5wNKZgWvYTSh03QmD_X4va3a8NoAc9oWRZi-OZWZbtzKnf2yG5Trww-i_EoTyNnzeGf5S6ewWcnXpvF4J-v8oo8Dk4nK6T3RjwbCGIxi6gKHiRx-Kzj2k2wUvarCxLV4H9bZymG6ISAEoT49OXL1WAdI6qZYd7JRkCDVrMCwKAX44JTTIq3fm0FCKKQw5hCUOR0wKCp7YWwWW33tHFTs8_Rr0x5005KiwNCP4vI1d-W1fsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《
لینک سایت برای کاربران ایرانی
》
👍
《
دانلود اپلیکیشن اندروید
》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
19
🔤
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99412" target="_blank">📅 20:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99411">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0G6j8TuJFN9Fkva4u_7QOa97wymoLPRkVBPyDjTnLgjbWlRGi1BGz5cCs85SBK57i1q_zDKhSFIDg36EEhaqljFygRlhPZR7nMmcSUPBpMNt2ckUdEO6uLBigUWmcHf8hM7IBgoDPcqS7jhovLG8R7Ju27O5c0X-EC_kvNC7S-G7-wR7YzvTur2zeKWusB3_FrfV0_wplYzsmxTlxAd2yAQdSB0KdguELsKVWKeC0-XHnRF1f18ylcGkD5HBpE2xz7NoYQvzZW6TGQeZgUtmbbfJjwbvimxoQjip3VOfNL7oSoYX0IQo8TBVrH8hni6qtB51w-npPpfl__tJE-Fjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‏
🎙
🇧🇪
رودی گارسیا سرمربی بلژیک: رویارویی اسپانیا و بلژیک اتفاق خوبی است، اما زیباترین اتفاق، حذف آن‌ها و صعود به نیمه‌نهایی خواهد بود
🤩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/99411" target="_blank">📅 20:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99410">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو: آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99410" target="_blank">📅 19:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99409">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfRHVW1phdqLX25BElwyS3Fko2UHaB6_WajR3pI0rmrZ4fVoyxD_F7lQYEmSccEOqdRWgx_fJ0WtCkbKGkMHPW3_9nkrD8ojunHzg66WpumRew-vRxOGuo8Bn5H9mxW0m7nonYWMLCvxEYHNbCgqPwYzP382yrBOjIU9-jJ3faWfD-uHPRGtNJOO7cVguZJ37ufcFzL5tDrmUQneAbf2HvrMGMx7HVpmS5Ryw4Wt8sDGjfe_vfmmgaTqiL8hgiSWKD_dgOrk6hWPYWKuG8_GmRUzGq8wGkeG_O_gZJts9HvjEfq2UJZb4fCFUUQj0QxRXukgdR414cSYbEtU7k-Zsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🔥
فابریزیو رومانو:
آدیمی به بارسلونا
🔥
🔥
🔥
🔥
Here We Gooo
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99409" target="_blank">📅 19:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99408">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFu6muvZKfrLN4Ol1YM44N2zX77_1Vut-f_utrLPP3pqg6H6dfsMOWnSmfa2k6G_altzxsepIevWcgvu2xw1rbIQtZBwWsugj-IaIdmamE-wVaJ0LBKRGZsjmxXQ541_I_lcaB64fIjlComBOCvS6lyLS-xZ581ZpkzRlTMqYtZEWM9J8rnGWNGuL4ZwQVIC-mCiJG6mf9f-t-1jRCvNIfHj0mZDZTXWNs73_d6msG0IKULYBej3tRI249AHxpm0y8HW7lBMqSuCgBRdrX_t2_IUPTAgVAS_fZR5Ss4qrgSOK0yyGwMSn1ThUjQZY7nCVtgZGYbWA01gNOeBXIZL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
ایکر کاسیاس:
- رابطه‌ام با خوزه مورینیو بیشتر شبیه یک ازدواج بود که به پایان ناخوشایندی رسید.
در سال اول، ما بسیار نزدیک بودیم و رابطه‌مان پر از شور و اشتیاق بود.
اما با گذشت زمان، رابطه‌مان رو به وخامت رفت و به دلایل مختلف، از بین رفت.
امروزه، اگر با هم ملاقات کنیم، احوالپرسی می‌کنیم و حتی می‌توانیم کنار هم بنشینیم و بدون هیچ مشکلی صحبت کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/99408" target="_blank">📅 19:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC3i39q2Kxf-78y7dxUNiBGyOvwKZgqjqBHi-GWHYpns7XEUxpwA652aUCsV86mYd7kvjYec0nvtiTAppGDNj-pBUvoZ6lwaY4TDQHHMQ2PsXk1n6MXY8oxGqm_Yp9oVRpbjyRgq1gEA8-5EC58-Upr3Osr-6GD75lED-YtoV3O9wGg0q4ZwEJmJmnLovLlr8ISwm9QjIVUVEt1ra_5-dOfhXJL-ujx2-n4hVsgd9AkD8TQmxFtkzDUDT2nUJzLFj5MIqe_QieSpVhoTgyNoPD8RvHyQwo33QN_HzcdGW8oi1XDh_HOz8LlbyUoE6rvw3WTot7DPhxh3p904aWVAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد سادیو مانه در طول بازی برای سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99407" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99406">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnWS_BOj8GwhmxlLSByQNoem3AWbBNsheCzijQbsEBHuhEOhbEyu_8hl37rXysPRJ9mISsDzPECf_Yh56D3or0WaxgPPSiWjnwHdpdA0zKblF2Tl0rS7yzAqZszHLkpgM06X4Mxyqu3_N4RYZ8v8rlsM__rKk5P7v1z9cCjtKEQQMdhzV4KlHHSELWFwdlQxPIlNEGTMsbVqGIR_kP08rttHmg2bOJnGIp9M2DtMx1KIwmILsypk8bU5yR0Y4vR1YuMWtL5CEW_iiJl02gC4KK4COz-nL0dMPy_JpsCQFlteq-FAFKxAxRjLqjWx6tdd5NlOhnRB2Sli0fJFFdKRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت را ثبت کن!
🇧🇪
بلژیک
🆚
🇪🇸
اسپانیا
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇧🇪
بلژیک یا
🇪🇸
اسپانیا؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p5_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99406" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99405">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izjxZyIkI7B7lPBL8AeZ1nxgmhTvivfp5GSEM1d4R5w2HpGbY6RSY8vAqr1zW6qPRAbuLasc5K3iVPZtIJ1hYi4-s470cnE9C62pR15j0vosHoLaOoFBYY0lUkbw_t2wdEpDY3qxFCQwKaXKXJd6n-JmXurT3JmGlFmHOv57LsNsBK5bfhTBYCafkmCMpfV21mD8wL1oVj-13fHUlLhpnqeYw7KdaiVhqzO8zgo5rK7fzbgBpFJtPmdNFJjQoKwWmf7I0TzhJtlTpzlpzM0qRFw8TKC69CdsrSxiP2GNU5Y1j21Zf8W_Izk-EI9C9PtmaE0DIOHDqwKY6puesEp3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
اسکای اسپورت:
بارسلونا پیشنهادی به مبلغ 20 میلیون یورو به همراه 10 میلیون یورو آپشن برای کریم آدیمی ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99405" target="_blank">📅 19:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99404">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-n8icQPerAJesZm65X92u3ARrkPhA1et0z0nBszkCLrAi0dR425uq7jCh4lB8LAtUhdewlotAaYRyakxhLTzfZVEiJ9xeZ2JJsOdBL-ELek1fL1VvkE1vhUUz6hKnL8aFhL-c4jn61-oXTIUmLlGXYCY0r8q2gOtDpqlqN0kPKe2PKU5uSUVYSY77BA103j2b3CS4o3Wp5C56Sx7qgXIQXcIRjntNJ5CuunuwSJtSsWBb6NHwN4uSSoU-QdsczZ_grYYMxI0HZdriBQ-6KR4sNvfhRDZYwT32gUaMdIJ6BsIm_p14CPGJCvyQtdpBXk83qft1ocmIXdG4IX99OX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇵🇹
خورخه ژسوس:
کریستیانو هرگز مشکل تیم ملی نخواهد بود، نه برای من و نه برای تیم. کریستیانو نماد فوتبال پرتغالی است. او می‌خواهد به پیروزی ادامه دهد و دوران حرفه‌ای خود را در النصر به پایان برساند. کار کردن با کریستیانو آسان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99404" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99403">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrJiKGPnyMdupTRBfyHkvZbqEO96aPfwm3AY-khQovhL3rQTyxJKSfr2b2T-yL9I3S1JDX7taG6cabqV1jpiA93ga4Z2rSEMu1fZrYebrubstQCqRJiMbPSQDJfcEvfq-K9nbf-1eJXHaY7FxGvHGEnPd3RR9HgBKwHGL4F6dV2WWcA_7Q56kTQJkh8NWQuKLiO98upnKu7fvXf85E2K6ozzZmYAdrzcnnFyvU1lBOS2eUF7wCN8VlXINNWGTH3dBsoCgeNxMHxdBhWSUCoBGmqwtkLvDOAdGgSSGgJma08dXNpajbNjrNVflwcm1egoVUEf8fQYBDX-C9zYBBx3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی اینترمیامی برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/99403" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99402">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99402" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99401">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvo0csH5v6PY7ej2MEycemcmYX96-dcuNJbDo6gXjazD-lCo8H1-XHKrY_AcKRLmYY07Y2A6ugKWjl4nwe1IJRLc9WlBExt744jsLLfm_cO_lC8n-MjPA8u6WmgqJeHHFFjSapCGdg8c1MmeNb28mdTGKbOmrF3n1SHr-CXyIlMR37qOhAiC9Uv_rbB_XbTMU3ODe7hp6hEVak0v2gr6R_Xv3o3aJQyuCY-xdbe38lbBVhQkE_7XGvT25eetataF7zShBTgn7PFhQhu5RUNUbKnNw56B6vi-8LGhRd5Zv1VvVAf52xHBuNalqZRYZqxeyh2wJQcqZn5TlIFWAcIPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین ربات  بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو ربات و ببین
🔥
@TNT_Winner_Bot
@TNT_Winner_Bot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/99401" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99400">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fj9TBy6XHrbvAUl4WRqUXwSjNvGy5ZHblbxwLSipwsaoeWkIz9kgUlN_iq5aiJYl0T9ORsNQAM2I0sQxbPbEwbfc6REJhMXBgF53dXBID6gqd1TtGXBLQA5PlzkkG3oMTGJoa47vCiYBqwneFq7B1PoNuzIl0Gw0FPpUNyPscoPs6LizzW-VeOO9Z-nHH_sqG-rZiY7OZum3YZv4bEISaMnr-U_cBLhdw8d00G9GJwjwr-Kcsyk0a6qMH9pw2NB_AVuoZ1rwEdG7bhy71R-G5pBv2Gu7XfgIeN3EYaC9d4141HY06GynsvEpW7KaZ1005f0FeJAklFLr3LEqowAzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر گارسیا، دوس دختر پدری، دوس دختر و خواهر گاوی، دوس دختر و خواهر کوبارسی تو امریکا؛ همه خوشگلا تو یه عکس جمع شدن
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99400" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99399">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMZPbXufZSA5k-Lz6ypwQdTU8jbE6jFqGRPS-ocBxSE8sgV2qVDbMH-a7bIBoAlYcA_q7qpdUQK6oE0RDS9uG_OZHGvsLN8ZevzRwIqE-jk8Z97AKWLgksw2DwRjAw7T4OcmS_6hGeUb4aADocWfF7d7_UxLSMi9yNFTl8rddEmFSdg18jwHytOYvnPf5fYiewt7gL5xIZv54ZRb_1tEemSkYFE9pZ8VqfwHFyIlH0SwLtOpHJL3ykODNKERIT7dN4vNUCKKRJBF3_jeSg1t6ViVuAzVbrSfV9xQqw2sH9CHWYSFS9m9WQj1IoO5X9s4pfJNNkvjT3KkpLNjbQMpQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری
؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99399" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
