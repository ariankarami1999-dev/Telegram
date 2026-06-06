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
<img src="https://cdn4.telesco.pe/file/vW5qaF4FzAEC_Fw2rxqskDyfH-buzcl70EUuCnBuT31Y5g4wPr46P2kRUMfiIqEvJGukFbkLjxrsLUygZFMgAhHKZvm84_LHg5dlHhWFdcfOcIDInkx_DYaHyCo2aFRnnfasowyps7HWjUt-IqroB2N8an1ugv9x7DDgs18O-L6jEOVrbsnJjbOyhkv0BGKwdkLMl_oVFS-xPj8-uPWoWt7ZntDSwttrz8JfTyDnqyABfUyDEnT43cxQnY9KxRi9y2wXZPdfoT3oskot3Ls1Lx8LF8L9qYgDiDBX182zLUwp7XXJSgFOkoVVXZXSk1F-7EQtKH4sPS_vf23a6thl1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 291K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
<hr>

<div class="tg-post" id="msg-13626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=LhJerVz967QOzlYqgHYrRJAS0ol73U8vkmC3EfYcKOglskixqP1bQla27znj4t6yLgzOJ--dWQtmz9C-WTrcvQT-2iD8knw9cp5fa6hVVk2hVzrSIvyJ7F6YxW8xk4Jp4Olk-WrSMEv08MJQq_tUi3f0LE7uBBB1zppYsfoLrn6mNkIgwjgrOIdqAIOMbqSzB_HBGaBC3juvt0DtRu5TSgGuH8RjuzLAAOJGnBEb5nC70M2HUWHyA_lhmbIuZD4-r5NY-R63oFdyqa9XumBdH1DxnumSKxx6czni6qhHoKBKb02FYe4PnFRa_yr2kBtzuMz6bBM-YF8iq-XAPFneRmzDIHT5OlkV_vxu2V41zyfWMpg_BfouJyKR1SEKUsZ3ZGDBT8d-cETFGPtBFZPZx1-Ju_2bEXbi1jPng-WMw-U5pqBBejJHLv48njoqRxYz2YCSifvX2BXOduTAo7w-g1k-qqgkCyZV2RluCPQTc2dZsNTzYqxM0xfk7xL6ZaSyfngexWoLtchoh9_-_sJNrrSLwESXdEymT5y-lllje_YGcFXCX0zogX6nxqoVWL6trcGHRaKeRnZfQLczL462CTYOgNxb5QMtodIqlQO2ta6i11ZqEPPinqg4oFy9gH2IsVUyfyUwNCxeWa5FDwqe26ZaHKTAV6j0IDgYx4TnIZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=LhJerVz967QOzlYqgHYrRJAS0ol73U8vkmC3EfYcKOglskixqP1bQla27znj4t6yLgzOJ--dWQtmz9C-WTrcvQT-2iD8knw9cp5fa6hVVk2hVzrSIvyJ7F6YxW8xk4Jp4Olk-WrSMEv08MJQq_tUi3f0LE7uBBB1zppYsfoLrn6mNkIgwjgrOIdqAIOMbqSzB_HBGaBC3juvt0DtRu5TSgGuH8RjuzLAAOJGnBEb5nC70M2HUWHyA_lhmbIuZD4-r5NY-R63oFdyqa9XumBdH1DxnumSKxx6czni6qhHoKBKb02FYe4PnFRa_yr2kBtzuMz6bBM-YF8iq-XAPFneRmzDIHT5OlkV_vxu2V41zyfWMpg_BfouJyKR1SEKUsZ3ZGDBT8d-cETFGPtBFZPZx1-Ju_2bEXbi1jPng-WMw-U5pqBBejJHLv48njoqRxYz2YCSifvX2BXOduTAo7w-g1k-qqgkCyZV2RluCPQTc2dZsNTzYqxM0xfk7xL6ZaSyfngexWoLtchoh9_-_sJNrrSLwESXdEymT5y-lllje_YGcFXCX0zogX6nxqoVWL6trcGHRaKeRnZfQLczL462CTYOgNxb5QMtodIqlQO2ta6i11ZqEPPinqg4oFy9gH2IsVUyfyUwNCxeWa5FDwqe26ZaHKTAV6j0IDgYx4TnIZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/13626" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkV0rVsLRey94qqvoZrx2xTcFQarjoXeZ85sU8paLlvlnjoIz2hikpCct4hrOQl8Nppk2Q4Bl1VA5EyLpgNQ8NT76bpxLyn0D3nzXsvQpyG_jQTS44zzgCYZfzY-XN4r_kKyrghPS0bg5TgntCSdOtaqn06-hqZwT5hL4iUcgaAg0dGq8JxXnP-D4OjvghhBFGtCr861xrK6j-kncBDixoM69BT1qAgmlxtJUHiZY-gVGAkQmn29krebZn7uyX5RfDY9Vnr4RH4N7ticN41NYIlvfUZwRCbStIn7Wh9Y7XOhnP2uX4m0yhi9HsgKFEjDL7yREarbTu061HH_yaamzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی پایگاه شهید راهبر نیرو دریایی سپاه در بندر سیریک که شب گذشته، هدف پرتابه‌های آمریکایی قرار گرفت
پیش‌تر اسکله این پایگاه در طول جنگ هدف بمباران آمریکایی ها قرار گرفته بود.
@withyashar</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/withyashar/13625" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/withyashar/13624" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مدیرعامل آسیاتک: اینترنت دیتاسنترها همچنان قطع است
مدیرعامل شرکت آسیاتک، با اشاره به تداوم مشکلات دسترسی به شبکه در بخش‌های تخصصی، اعلام کرد که برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت اینترنت بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/13623" target="_blank">📅 15:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/13622" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/13621" target="_blank">📅 13:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صدای انفجار قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/13620" target="_blank">📅 13:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13619" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/13619" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13617">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزیر کشور پاکستان(
سناتور سید محسن رضا نقوی
)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13617" target="_blank">📅 12:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13616">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=HyF3VRf3gzB3XciSVQpEql8v3KXQX2CUpbsE2-hzEW17L7MkYtFLU_r94nRQ8ejdjxscVrAsSmRwtmrJzn9OVUU_AR2ONYOSAtTXmJ3Px6ql40th55VtVIWudYYtLt-mLrLWlzlfexCNdkoUKNFpudikim5lOe_XFlI2qSIQSK3NZmv5cYsYjL2D2PRH4WF3Z9L6J5QjJ8WqE90rpuV_equhz4HjCwrq2c3JBemLPupqZgd3Yn3g54_5ETqfRqgqEvNQPa0FFJwAiNfd_qzZRXZ4vr_UBuykuatEE__s5IEpX2ecHLRYpJMsuyfi2d--LVtZx3rTW1lR_Kmlo7uJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=HyF3VRf3gzB3XciSVQpEql8v3KXQX2CUpbsE2-hzEW17L7MkYtFLU_r94nRQ8ejdjxscVrAsSmRwtmrJzn9OVUU_AR2ONYOSAtTXmJ3Px6ql40th55VtVIWudYYtLt-mLrLWlzlfexCNdkoUKNFpudikim5lOe_XFlI2qSIQSK3NZmv5cYsYjL2D2PRH4WF3Z9L6J5QjJ8WqE90rpuV_equhz4HjCwrq2c3JBemLPupqZgd3Yn3g54_5ETqfRqgqEvNQPa0FFJwAiNfd_qzZRXZ4vr_UBuykuatEE__s5IEpX2ecHLRYpJMsuyfi2d--LVtZx3rTW1lR_Kmlo7uJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون پرواز هواپیمای اف-۵ ئی
تایگر ۲( تک نفره )متعلق به هوانیروز جمهوری اسلامی برفراز مشهد
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/13616" target="_blank">📅 12:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13615">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA_sLc83uWf4ZByTzNIobycm-WSJxcfo5hNL6AXkR3vuqJCKUPl5SsgSr3uwU3YDtxDzBroYigt25R2UrQQmvzoVHAOS6URJegOVB6VDNBoytND8WbilBP1OJX8uxMvHXSoHcDIT_6vvzEIAyNqYVmQ6ZJdrbljJq57y4WE2nA3JDX2mB67yGpbuXaZ_QBaYVMFrE5NR9YnsslrpIR_MHjI68DUsS-KN8-o6JwoT9JbYzw519XmTEXC4KbZIHbf1jDM5TKAKK38Jtk6UkyXVpRyNWMV-f-UE8x19fBVXfeN8Ka060rEfk_7Rh1dxFkrVhlxOLx6uQfKLcHoPF3PPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس های جدید پایگاه هفتم شکاری شیراز بعد از جنگ
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13615" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13614">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ورزش سه :  آمریکا به 15 نفر‌ از اعضای تیم‌ ملی ویزا نداده و رفتن ایران به جام جهانی در هاله ای از ابهام‌ قرار‌گرفته.
رویترز : کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13614" target="_blank">📅 10:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13613">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13613" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13612">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=sCX-m_dbTdj0ApT7cYk3Gb4ov0jr1OOAndzK163_0w1U2-xhsWlfJfgghj2OnCpbpAbBy5qEeTtPlfCvSChXwIHDEMFkwAhYXD5upJwZ1oIthhnizvJxKUNBFBFkW0v9i5zQOyQJW1o6NCNuAioaGVEUKhkmUrwiAzz3XHO7Cmx1IhouBiF1n5xeluJWqS_aefymnPZSCT7pV5C2MQb9LW1v6YMymrJCTI8IGgQxXq9kt2gO-_L5pIY8mp2n7u1WcnJLiJOvfPoP2jv8KTUB_zYfpx1lCmKDrYFhY7Ez-sqjWVRTPET1tmQd3ewKANgueDh_sP5cs6GJPNRfraqxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=sCX-m_dbTdj0ApT7cYk3Gb4ov0jr1OOAndzK163_0w1U2-xhsWlfJfgghj2OnCpbpAbBy5qEeTtPlfCvSChXwIHDEMFkwAhYXD5upJwZ1oIthhnizvJxKUNBFBFkW0v9i5zQOyQJW1o6NCNuAioaGVEUKhkmUrwiAzz3XHO7Cmx1IhouBiF1n5xeluJWqS_aefymnPZSCT7pV5C2MQb9LW1v6YMymrJCTI8IGgQxXq9kt2gO-_L5pIY8mp2n7u1WcnJLiJOvfPoP2jv8KTUB_zYfpx1lCmKDrYFhY7Ez-sqjWVRTPET1tmQd3ewKANgueDh_sP5cs6GJPNRfraqxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر کرد و
کفت
حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/13612" target="_blank">📅 10:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13611">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارسالی : من بابامم تعریف میکرد که زمان جنگ عراق و کویت صدا های بمب هارو میشنیدن خرمشهر
@withyashar
گزارش های زیاد از شنیده شدن انفجار کویت از خرمشهر !</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13611" target="_blank">📅 04:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13610">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBX6F8AVpCtxeGqbr2axo2ebcrLpDNiy81BjOvjeGu4H5dxRdTJkemha-JWfNyP6Sy7suk3m4sFOHUu6ECPeJTFNbgoOVw2hg3o_hA1TFV-9-exN1PNZ4myLq89z9WSphVfqCejaYJ834g0fRyVEQ0Pyzv0BcxJNDQ26R_QDcrrcyASATYlw7CfLQnwz_QFxZfYDIZZ_0ZlG87mewft-TL6Efv6uIiASf_QCRbNdzG3GBS97vF0eTD-nRJWqA4LTtTNcJuKOP9MZ9j9Y7O_QJ2l73EShIgTCNtQ-R2ZMwO-u3mq1Mdu4M7AYjHdAJxXNcXAutucpQQaEN31lHNBOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : کویت آلارم اومد الان ، ۳پا موشک زده سمتش !
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/13610" target="_blank">📅 04:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13609">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622170a597.mp4?token=armPFxFBawHIK7P3PPDeP00k69dagBQucZPrT1gJ-D3uNWnbgc6nuPcl6pysWGrqZepF3HnaCZU3J6XwuBMmFEyUonKAKN5wDlHPBqKe0CSxGV50eKeqxgrBQVe27Dmz_JM6kgAYu4x_w58XTyNzi_utR9jZDpTm0A0TNSdcRYUQ6aImTpLW_KUtLlWSBt6o7fczRxck4fr-HBZbAFh1wZbKjoT-HVcLDaRZ_j69CG7THOsYGkCqEQpH_dyGakKTx3IuzRGPm8chl3H5bAxC7t5qLouAHkXZpFadMOJcS8NQyYd4NIWQmUyOUukuXm4s44NdoT8q5eFYlKB_TLUpMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622170a597.mp4?token=armPFxFBawHIK7P3PPDeP00k69dagBQucZPrT1gJ-D3uNWnbgc6nuPcl6pysWGrqZepF3HnaCZU3J6XwuBMmFEyUonKAKN5wDlHPBqKe0CSxGV50eKeqxgrBQVe27Dmz_JM6kgAYu4x_w58XTyNzi_utR9jZDpTm0A0TNSdcRYUQ6aImTpLW_KUtLlWSBt6o7fczRxck4fr-HBZbAFh1wZbKjoT-HVcLDaRZ_j69CG7THOsYGkCqEQpH_dyGakKTx3IuzRGPm8chl3H5bAxC7t5qLouAHkXZpFadMOJcS8NQyYd4NIWQmUyOUukuXm4s44NdoT8q5eFYlKB_TLUpMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در‌تروث : نیروی دریایی ایران
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13609" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13608">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=i0RzWZ8UNgednUqtdaQ4lPrOlobLMuc3cUkpkdrK5GPq11J0YsvPHwW9YVOz6vxafevrAqj5XvIBYRuMqjIvuKR6GZkxUPmev_Af71GRDGK480HPxlZSGKJ6-_L2X7NXXM-l6YSm2i3bpdCNEmsQhVWyk4Q9Za8hoRSdRle4TIUyWZKeKr_P70P7ms-iVLtc7ZuxEZmQ4OBkSYex9-Ava7laIEe9UhRMCoSPKCGk06kz3D4EvII1xzNflW0HGiwaYoGNBGKWqzww_UCdzJE6FaGz8JPsoxCkPszGq6kfqQahjJmxgDn2pfCSUeJyLr9i4zkbmQ7gAtoPdYSGP1RkhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=i0RzWZ8UNgednUqtdaQ4lPrOlobLMuc3cUkpkdrK5GPq11J0YsvPHwW9YVOz6vxafevrAqj5XvIBYRuMqjIvuKR6GZkxUPmev_Af71GRDGK480HPxlZSGKJ6-_L2X7NXXM-l6YSm2i3bpdCNEmsQhVWyk4Q9Za8hoRSdRle4TIUyWZKeKr_P70P7ms-iVLtc7ZuxEZmQ4OBkSYex9-Ava7laIEe9UhRMCoSPKCGk06kz3D4EvII1xzNflW0HGiwaYoGNBGKWqzww_UCdzJE6FaGz8JPsoxCkPszGq6kfqQahjJmxgDn2pfCSUeJyLr9i4zkbmQ7gAtoPdYSGP1RkhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون
جت‌های جنگنده آمریکایی در حال پرواز بر فراز استان بصره عراق نزدیک مرز ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/13608" target="_blank">📅 03:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13607">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=ufy_3o-l-pbCBb3Muw76lzNVZRa7618-dj5kYQGw-zLcVpHU7r9xdofh6mN2_THh55Z5VkolMRNl4XoTmLhkVtpE1j2p80N8wOBSah-YzPxTfidTKylFN5X_75zgTcxAIs_QMdMfMS4iULRgEU0_qyOhAt0FfgFArAO2SBgYfob8Lct6ieB7xi-A41Joa7jbyQ6pO-nMtjZL_0BXkA2a33uk7bq5-aHTlKETHVYPDefclCkjbN8Mk6UMsoXpNe7qyxgDRpTrAqv5kMkSL_k9J27SoRgDiUUDThzMp_sfMynnMezVgW8Ykgy75t9T5sIewSt0xhvVjqw6gUr8_JxBSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=ufy_3o-l-pbCBb3Muw76lzNVZRa7618-dj5kYQGw-zLcVpHU7r9xdofh6mN2_THh55Z5VkolMRNl4XoTmLhkVtpE1j2p80N8wOBSah-YzPxTfidTKylFN5X_75zgTcxAIs_QMdMfMS4iULRgEU0_qyOhAt0FfgFArAO2SBgYfob8Lct6ieB7xi-A41Joa7jbyQ6pO-nMtjZL_0BXkA2a33uk7bq5-aHTlKETHVYPDefclCkjbN8Mk6UMsoXpNe7qyxgDRpTrAqv5kMkSL_k9J27SoRgDiUUDThzMp_sfMynnMezVgW8Ykgy75t9T5sIewSt0xhvVjqw6gUr8_JxBSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتک نیم وارو پهپاد های شناسایی اسمون بندر عباس همین الان
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13607" target="_blank">📅 03:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13606">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13606" target="_blank">📅 03:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13605">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13605" target="_blank">📅 03:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=IZbAnW0gJ4QYmr25bjuu7_i_G8lRaIUZ1-fGrwgKKctMWP5sbmeCNw0C5IXUK5CLhWYe99Fi0V26iU--xV3S5Z6S8EfmLsaT4q4OITn5F2HVbt53Oa6W6_r9PDE-NlTcR-Ul9jKyQIEp8aQUtORnbPAAF3E-d23FxqEcdwyrTRLWfkK7wh1Qe_BJ0uEkF8XbQaO_zPmPqD_F_-Tdvd2b6UiE4_5YfwMHt5dnb29Vh1FqtBCoLOQyiyQxuLoujbB4xWGh1eeTx2UMbJJx6fe63rA96Qcs4YLXlaf_mjZ6s12OeD7f0siZpe4dD3c95_T4R5p_Jf8E5c8isTyXplXrGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=IZbAnW0gJ4QYmr25bjuu7_i_G8lRaIUZ1-fGrwgKKctMWP5sbmeCNw0C5IXUK5CLhWYe99Fi0V26iU--xV3S5Z6S8EfmLsaT4q4OITn5F2HVbt53Oa6W6_r9PDE-NlTcR-Ul9jKyQIEp8aQUtORnbPAAF3E-d23FxqEcdwyrTRLWfkK7wh1Qe_BJ0uEkF8XbQaO_zPmPqD_F_-Tdvd2b6UiE4_5YfwMHt5dnb29Vh1FqtBCoLOQyiyQxuLoujbB4xWGh1eeTx2UMbJJx6fe63rA96Qcs4YLXlaf_mjZ6s12OeD7f0siZpe4dD3c95_T4R5p_Jf8E5c8isTyXplXrGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر زارتان زورتان</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13604" target="_blank">📅 03:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۳پا باید یه جوابی بده چیزی‌ دیدن یا شنیدین بگین</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13603" target="_blank">📅 02:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13602" target="_blank">📅 02:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۴: همه امیدوار بودند که آتش بس برقرار شود، اما بازی به طور کامل در حال تغییر است. برای یک آخر هفته فوق العاده گرم در خاورمیانه آماده می شوند، زیرا ایران و آمریکا از اعتصابات تصادفی شبانه به رویارویی های روز روشن تغییر می کنند!
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/13601" target="_blank">📅 02:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام : چند لحظه پیش، نیروهای سنتکام چهار پهپاد تهاجمی یک‌طرفهٔ ایرانی را که به سمت تنگهٔ هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه ایجاد کرده بودند. در ادامه، نیروهای آمریکا برای دفاع در برابر حملات بیشتر، سایت‌های رادار مراقبت ساحلی ایران در گورک و جزیرهٔ قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ‌دادن به تجاوز بی‌دلیل ایران در چارچوب دفاع از خود، در حالت آماده‌باش قرار دارند.
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13600" target="_blank">📅 02:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
سنتکام از حمله به سایت های راداری قشم خبر داد!
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13599" target="_blank">📅 02:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13598" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سی‌بی‌اس نیوز به نقل از یک مقام آمریکایی: نیروهای آمریکایی حداقل ۴ پهپاد را که توسط ایران به سمت تنگه هرمز پرتاب شده بود، سرنگون کرده‌اند.
🚨
@withyashar
بچه جنگ شده باز</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13597" target="_blank">📅 02:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚠️
@withyashar
گول نخوری !</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13596" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فقط در ۴ ماه ! بسوزید عرزشی ها</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13595" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💥
290k عرزشی سوز ترین کانال تلگرام</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/13594" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش هایی از قطع شدن اینترنت
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13593" target="_blank">📅 01:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سی ان ان : منابع می گوید ایران چندین پهپاد را به سمت تنگه هرمز پرتاب کرده است. نیروهای ایالات متحده حداقل 3 تا از آنها را رهگیری کردند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13592" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوتا صدای انفجار الان ومد همین الان قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13591" target="_blank">📅 01:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجری ان‌بی‌سی: رهبران جمهوری اسلامی معتقد نیستن که به‌طور کامل شکست خوردن.
ترامپ: ایران به دلیل تصور برخورداری از قدرت کافی، از امضای توافق خودداری کرده. ایران در نهایت گزینه‌ای جز توافق نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13590" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ به ان بی سی:
خیلی از مقاماتشون مغرورن، یه سری کارها هست که هیچوقت فکر نمی‌کردن مجبور بشن انجام بدن ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره.
داریم درباره 47 سال حرف میزنیم که هر کاری خواستن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13589" target="_blank">📅 01:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ به NBC : وضعیت برای اونا واقعاً سخته
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13588" target="_blank">📅 01:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/13587" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13586">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌ @withyashar</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13586" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13585">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13585" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13584">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به نظر می‌رسد جنگنده‌های اسرائیلی از عراق به سمت ایران می‌آیند
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/13584" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13583">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد @withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13583" target="_blank">📅 01:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13582">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/13582" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13581">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به خبرای هست ولی نمیتونم ثابت کنم</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13581" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13580">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13580" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13579">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارشهایی از صدای جنگنده و پدافند در شمال کشور
🚨
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/13579" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13578">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/13578" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش های تایید نشده : چندین جت جنگنده آمریکایی حمله‌ای را به بندرعباس و مناطق اطراف جزیره خارک آغاز کردند و چندین بندر از جمله فرودگاه بندرعباس را هدف قرار دادند. پدافند هوایی فعال شد و درگیر نبرد شدیدی با جت‌های جنگنده شد.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13577" target="_blank">📅 00:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش هایی از شلیک نیروهای ایرانی به سمت ناو های آمریکایی
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13576" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره خارک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13575" target="_blank">📅 00:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">@withyashar
only for pro members</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13574" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">@withyashar
operation economic fury</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/13573" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13572">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13572" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13571">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13571" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13570">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_w0IImAtGH2crIm0M7we1enwCdkyaX5Tl7TAjUgZ2qeMQSk5RrGsKPAE-SL-GjcWH14FRa4HAqMK-67pe1kcPm1wH-866NJIVdKk8cdswv4IEWpsOsa-WGx5dUY-Ye3ZHcSKi2pjJapKWQMxkteW_R-BlJQSqF4akw3GrimoJlGjcbu5O6mwy9awE5RdJ82YR6CyYWgeuy7UeJSVzDR_kJWGt0cprDqKsUrX0wEwPzqOkbE1IfwTniqMNZ_TrmXAz2vMBQAwMm9CN1dHUx5kCqrfynVDtkGo-5gYw0wrGZX42oZOYjhxZ2cqko88nAtALm7oqS2OMNsDgqJLM_JFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواستگاری جنجالی قیصر از الهام چرخنده در تجمعات حکومتی
قیصر در یکی از تجمعات حکومتی، به‌صورت علنی از الهام چرخنده، بازیگر سابق تلویزیون ایران، درخواست ازدواج کرد. این اتفاق غیرمنتظره خیلی زود در فضای مجازی و رسانه‌ای مورد توجه قرار گرفت و واکنش‌های زیادی را به دنبال داشت
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/13570" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شبکه ۱۲ اسرائیل به نقل از رئیس ستاد ارتش این رژیم: قصد نداریم از سرزمین‌هایی که در لبنان پیشروی کرده‌ایم، خارج شویم
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/13569" target="_blank">📅 22:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است. @withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13568" target="_blank">📅 22:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13567" target="_blank">📅 22:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارشگر: بازی که شما می‌روید  ببینید ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند بلیت این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13566" target="_blank">📅 21:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ درباره پوتین و زلنسکی:
بگذارید خودشان حل کنند. من کسی هستم که آن‌ها را به این موقعیت رساندم.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13565" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ درباره جان بولتون:
فکر می‌کردم او در زمینه جنگ رادیکال است، نه در زمینه چیزهای دیگر.
او می‌خواست با هر کسی که دهانش را باز می‌کرد وارد جنگ شود.
او همیشه می‌خواست مردم را بکشد. من هرگز به او گوش ندادم.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13564" target="_blank">📅 21:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ درباره ایران دم مسترا:
ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم.
آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
ترامپ:
پیت هگستث معلوم شد که یک گوهر است.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/13563" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=D_NbiucOeRrTa5UmQMLp3W7ySXil6qUyjtTt0C0w-1fnKp9iib2n9-0U5sjSrGRNPslswnC4sKrqoGZjJ6DoK6BH9SD9D4XPNH_Iab2XqFaM9U6tyTUcsJ-U6ifrYtstfySVYp5hIlcU9EA34GbTydGV4bCGF8IT110enHTyAgsooNKwkYSYjx32tCNYvHWWmHz8BlE55UOXU0qj_7n4GpCJBK9MKUB0_T4S27uIBqD3oPMNYC--hNEXTlM1R6E9h9heE4eH7BuLyy4Yyl4BNvz5VfDkVQf8XO72CdLqWJv7hOs4sSnYPe9vaBU5SJJnbLUCT-vq5ajosZttv_pJWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=D_NbiucOeRrTa5UmQMLp3W7ySXil6qUyjtTt0C0w-1fnKp9iib2n9-0U5sjSrGRNPslswnC4sKrqoGZjJ6DoK6BH9SD9D4XPNH_Iab2XqFaM9U6tyTUcsJ-U6ifrYtstfySVYp5hIlcU9EA34GbTydGV4bCGF8IT110enHTyAgsooNKwkYSYjx32tCNYvHWWmHz8BlE55UOXU0qj_7n4GpCJBK9MKUB0_T4S27uIBqD3oPMNYC--hNEXTlM1R6E9h9heE4eH7BuLyy4Yyl4BNvz5VfDkVQf8XO72CdLqWJv7hOs4sSnYPe9vaBU5SJJnbLUCT-vq5ajosZttv_pJWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیرون کاخ سفید با خبرنگارا حرف نزد، و قبل از سوار شدن به ایر فورس وان هم هیچ مصاحبه‌ای نکرد، ببینیم دم توالت چیزی میگه یا نه
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13562" target="_blank">📅 21:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند. خط قرمز اردوغان: هیچ نیروی نظامی کردی…</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/13561" target="_blank">📅 20:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند.
خط قرمز اردوغان: هیچ نیروی نظامی کردی در نزدیکی مرزهای ترکیه نباشد.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/13560" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13559" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">️حمام خون در بازار کریپتو!  بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است. @withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13558" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آلمان با صدور هشدار امنیتی برای شهروندانش، نسبت به سفر به خاورمیانه هشدار داد و دلیل اون رو احتمال تشدید دوباره تنش‌ها و اختلال در پروازها عنوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13557" target="_blank">📅 18:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام:
ادعای نادرست: ایران ادعا میکنه که به سمت کشتی‌های جنگی ایالات متحده در خلیج عمان تیر هشدار شلیک کرده و کشتی‌های آمریکایی رو مجبور به «عقب‌نشینی» به سمت اقیانوس هند کرده.
حقیقت: نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی ایالات متحده حمله نکرده یا به سمت آنها شلیک نکردن. انجام این کار نقض فاحش آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره مداوم علیه ایران رو به طور کامل اجرا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/13556" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gloria2018Remaster(IG @yashar)</div>
  <div class="tg-doc-extra">Umberto Tozzi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13555" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/13555" target="_blank">📅 17:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=oOBedIFGD3dMpxgAIGMoWXBxCO1l77-xEQFQB5MmAxEJZ1T9J4RzY9QgO-rbKw-RM4dszbAjJGE7t55qpb2H4D2eOUmaccrmKDH6zsYVXoBQOsigA4CVIy7cit-YA29ndzOd7iaCutnnHLE9Sd-0QpPYZd82onVgbJHgnWQnps_GiXVruFFhmyXzEDNcrvNcu647L3d1pg156R7QUOI0QhcY0WxZ9h9-8ozGp2YNByo-2p0qBG65R6vwVASBIqo6aUnVU5Cse0l5ZRDFE6bhI4dSUkQT1qSuRt536dVVC25AiLk4PCspTusQ5zGW2A6e0ZQJv2Z5MvNfvPnFoYrklg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=oOBedIFGD3dMpxgAIGMoWXBxCO1l77-xEQFQB5MmAxEJZ1T9J4RzY9QgO-rbKw-RM4dszbAjJGE7t55qpb2H4D2eOUmaccrmKDH6zsYVXoBQOsigA4CVIy7cit-YA29ndzOd7iaCutnnHLE9Sd-0QpPYZd82onVgbJHgnWQnps_GiXVruFFhmyXzEDNcrvNcu647L3d1pg156R7QUOI0QhcY0WxZ9h9-8ozGp2YNByo-2p0qBG65R6vwVASBIqo6aUnVU5Cse0l5ZRDFE6bhI4dSUkQT1qSuRt536dVVC25AiLk4PCspTusQ5zGW2A6e0ZQJv2Z5MvNfvPnFoYrklg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ویدئویی جدیدی در شبکه تروث منتشر کرد که در حال بازی گلف است و یک ضربه فوق‌العاده میزند. همچنین از آهنگ معروف گلوريا لذت میبرد.
یاشار: آخرین باری که این آهنگ ویرال شد در فیلم گرگ وال استریت بود. مضمون این آهنگ این است که
کنترل نکردن زندگی احساسی می‌تواند خطرناک باشد
توجه زیاد دیگران همیشه خوشبختی نمی‌آورد
باید قبل از اینکه دیر شود، آرام‌تر شد و به خود رسید
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/13554" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس‌جمهور لبنان، ژوزف عون، در مصاحبه‌ای با سی‌ان‌ان ایران را متهم کرد که در رویارویی با آمریکا و اسرائیل از کشور او به‌عنوان یک برگ چانه‌زنی استفاده می‌کند و گفت: «این کشور، کشور شما نیست.»
عون همچنین افزود که مردم لبنان از جنگ میان اسرائیل و حزب‌الله خسته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13553" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است و جای نگرانی برای شهروندان وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13552" target="_blank">📅 16:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130435eef7.mp4?token=TbBBr2er2OmZZ8QBwp7svR-05S9xtKSf3EgL2W5JK9niIn1lQ9WIKIuMtpw_5De7F2paVuL7MnBZHenUFLuSXRA9LzZ6FPVUZTcwRRZKALNZ1tu0dXmmBu3ahqfooCcBL4PeEze2XhnTFKTEwputzZ0bOnaylTjTf_dz6hYWMcASetBMEeQ4_u1GyRa63-aN-GwckMUyN9i_LPz_lq7lRCjc33IOhCApGPfBqmpLUOhSxRvLR3iBhXY8F4qE6pL7Q4uwhGmd4vn2dLiZtWXHB39fc4EbPU32SidGiHc3XlnkEMGp_XqSlpm2Or947cMfwhHMqyFwt1x6VETfSbfQt4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130435eef7.mp4?token=TbBBr2er2OmZZ8QBwp7svR-05S9xtKSf3EgL2W5JK9niIn1lQ9WIKIuMtpw_5De7F2paVuL7MnBZHenUFLuSXRA9LzZ6FPVUZTcwRRZKALNZ1tu0dXmmBu3ahqfooCcBL4PeEze2XhnTFKTEwputzZ0bOnaylTjTf_dz6hYWMcASetBMEeQ4_u1GyRa63-aN-GwckMUyN9i_LPz_lq7lRCjc33IOhCApGPfBqmpLUOhSxRvLR3iBhXY8F4qE6pL7Q4uwhGmd4vn2dLiZtWXHB39fc4EbPU32SidGiHc3XlnkEMGp_XqSlpm2Or947cMfwhHMqyFwt1x6VETfSbfQt4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/13551" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c96db917.mp4?token=aZrgLMwhCiBkZrAMOwetUSuugMveoi_dBfPC6sKxNQnHJe3aiVqtERcozcb4b9NFevMYgTK2Utij1BHkkiHoQpmoMQMKlGJE_UjVK2cV7NiUdEOQ14kG5607lJWw3sENSsycBkznUC6dPA_NaX9mBteZLgO380WFjymXzq3pB5WBWGjj2TY7YZnK96TdURu3GbQen0upe4uptJAB71cgbY4ds3vNIsZbgO_UvqheHmkxqcPxVlwhWNoKoOzFEfCTqburKQT4MiVlWws6lpPY5w6eGktwPWirblXTto5B_HVm-Hs5K-6jqn_uVQ7bnRUEcmNfrMDtzld8Glym57ilZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c96db917.mp4?token=aZrgLMwhCiBkZrAMOwetUSuugMveoi_dBfPC6sKxNQnHJe3aiVqtERcozcb4b9NFevMYgTK2Utij1BHkkiHoQpmoMQMKlGJE_UjVK2cV7NiUdEOQ14kG5607lJWw3sENSsycBkznUC6dPA_NaX9mBteZLgO380WFjymXzq3pB5WBWGjj2TY7YZnK96TdURu3GbQen0upe4uptJAB71cgbY4ds3vNIsZbgO_UvqheHmkxqcPxVlwhWNoKoOzFEfCTqburKQT4MiVlWws6lpPY5w6eGktwPWirblXTto5B_HVm-Hs5K-6jqn_uVQ7bnRUEcmNfrMDtzld8Glym57ilZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ایران اعلام کرد که به دو ناوشکن آمریکایی (DDG-103 و DDG-87) در دریای عمان شلیک هشدار انجام داده است  موشک‌های قادر و پهپادهای شهید دانایی.
هر دو ناوشکن به سمت اقیانوس هند عقب‌نشینی کردند.
ایران همچنین ادعا می‌کند که ناو حمله آبی-خاکی یو‌اس‌اس تریپولی مجبور به ترک منطقه شده است.
هشدار نیروی دریایی ایران: اگر کشتی‌های آمریکایی بازگردند، از موشک‌های برد بلندتری استفاده خواهد شد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/13550" target="_blank">📅 15:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEtVR8qAE21DMMSHfrnlCHXhDdMO-9d1pLRspEAr40W0V_nqleg2aWxRlnR3YwRqP2-n6LxIVbehs15tkMHHMkQ3EqYap_NYLdXsQ1IgktVZqHpZ85lx0BDmfB54SkC8--N46fgONZGe7tQkFhaulomdieYl4w4HuoZXz612AGkbF6v6Fpq3wYKeAecdy4uWVOjspcU9RHyAsRxZFb0zFZVyHNpp0ziJd5wfQMApY1fM8_vO34lk3NCcvBA6eqnOF_cmDdVo3e-U3MqO8u7QdVdug1sO7l9nCbC7GM6EHr1GoYMTbQBjoViWdKs5WF5SwJ7XX5kDbPBEKvpghdNbQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️حمام خون در بازار کریپتو!
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است.
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13549" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=mFto6QGUqRJLxPGZj57FVLlTP2wxuT6iw2najplfK3--Vey48VBlAKGlHqoA5u5pKOeaaM7C0g7wpyjY_4-bOfOElKWEn-ql5Ok-VNFXIsMwjb3VSi8hUvGvHtQ4WKEsIFHo9glhBdPxTw8P6L_6ClIkDszZzlPkGGTTJbn65fJvEaO9s_ZVcMoOBglEDj7zqVDOIhhicdhdlIFwLzD3h4HgDLDLcDBfQm2TPAyUkVK4LJofWscjUcOnzTMy8UtM7-i8W4jt9jvoNCOH7Aa9gOTox0yp0ULSAu5v_ypTOQ2wmMWFnn1yDFR2TWBELamBCYorffxMKcKxK7-A2p9s5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=mFto6QGUqRJLxPGZj57FVLlTP2wxuT6iw2najplfK3--Vey48VBlAKGlHqoA5u5pKOeaaM7C0g7wpyjY_4-bOfOElKWEn-ql5Ok-VNFXIsMwjb3VSi8hUvGvHtQ4WKEsIFHo9glhBdPxTw8P6L_6ClIkDszZzlPkGGTTJbn65fJvEaO9s_ZVcMoOBglEDj7zqVDOIhhicdhdlIFwLzD3h4HgDLDLcDBfQm2TPAyUkVK4LJofWscjUcOnzTMy8UtM7-i8W4jt9jvoNCOH7Aa9gOTox0yp0ULSAu5v_ypTOQ2wmMWFnn1yDFR2TWBELamBCYorffxMKcKxK7-A2p9s5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود حجیم جنوب مركزي تهرانه  همين الان
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13548" target="_blank">📅 15:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13547" target="_blank">📅 15:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه. @withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13546" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فیفا: نقص سایت باعث صدور بلیت‌های رایگان شد
‏فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/13545" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13544">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/13544" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13543" target="_blank">📅 12:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13542">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد و از اسرائیل نیز متقابلاً خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت این کشور احترام بگذارد.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/13542" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13541">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=rz2OHFBahxtUWkkrI2IeBwurX_IqMPz_Bw6OiMZXr9DnNMioIEv4R_SqVzrhzH4k7lcT9kCh9bukXqUkk6r9_N3C4XHqpL-H4L72_pC7e9UZRrjNFHCqDxBLgsqtNAkVmSLT2_DFOO5KR3OgGzQjmrImwudiQHirT9kEVyBscAAf-KX-6V7A3YUkjrA6L4RLInATLQ6GfwgxFJN2FQ3yA3qkJTgZ9OHTbNMc6KehpYr7VmsXai_nX1HZkiAmKW7Le6VMzjM1xu0HeIQ5jeeHedKctdr1suuZEthGFG84L7DbExOU75KjizTk6skn6fP57umG2fO5m7pQ3g_SQtSL3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=rz2OHFBahxtUWkkrI2IeBwurX_IqMPz_Bw6OiMZXr9DnNMioIEv4R_SqVzrhzH4k7lcT9kCh9bukXqUkk6r9_N3C4XHqpL-H4L72_pC7e9UZRrjNFHCqDxBLgsqtNAkVmSLT2_DFOO5KR3OgGzQjmrImwudiQHirT9kEVyBscAAf-KX-6V7A3YUkjrA6L4RLInATLQ6GfwgxFJN2FQ3yA3qkJTgZ9OHTbNMc6KehpYr7VmsXai_nX1HZkiAmKW7Le6VMzjM1xu0HeIQ5jeeHedKctdr1suuZEthGFG84L7DbExOU75KjizTk6skn6fP57umG2fO5m7pQ3g_SQtSL3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اصابت یک پهپاد به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/13541" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13540">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل شب گذشته به قطعنامه آتش بس در لبنان رای نداد
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/13540" target="_blank">📅 09:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق روال هر روز صبح حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/13539" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6y__Y0uw5-vGlt04v0cld_UIKXqje1j-CK5WSGeJlA6l8DrJBthMmZ2K3e1mF7TBcZUqhUkIUHIsdy27j6OSeF07ILN_UB3QhPe1VeoWHD0qYhHYHPKbXhyGjve7rvLC8sYlTrDpc2iqccYwYOgB7hi9nmhosBndG65EDCUCRBkzr48_O-3p7q1MpGxsj4wuKNP8m2Kq1O4e9GQXqDavTV3nJQkZnNVg-z60h01Z2XHobv7KapkCVId5g85vLSD4ZQQeqDCEEmrjmQeI1suzbEvYDPKQ5VAEtiOdqD6XmXew--qnQwDRiYOVQ2h4LKPhW6Z81fyZdFXLdd6UvlYeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای زیادی برایم فرستادید که از پدافند سنگین ۳-۴ صبح و چندین انفجار در تهران ولی مدرکی نیست… فقط چندین عکس از اینجا برایم آمده.
آزاد راه پردیس به تهران
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/13538" target="_blank">📅 09:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امشب بیداریم ، ردبولم میزنیم
🤣
💥</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/13537" target="_blank">📅 09:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رویترز: بامداد جمعه انفجاری پهپادی در بندر الفحل عمان رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/13536" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران:یادداشت تفاهم در مرحله نهایی خود قرار دارد
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/13535" target="_blank">📅 08:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=I4h9JBVaihtCsmAlflKiJ4zIci0dCdrs9NoEI2KkJQC-9xKOUkbJrn8Mh6AU99xXPnZbj_8EzptG-D2RsiTRaMoGnJg3AZpMBg_gax6PZ6KxhAWKFkEzDKrYZMMvmNNsWK4AtckJD_NX4vqh9LruCnyLoThQDvPQSs6NdWggb8hTtyoWsXO-ndA-xLXk7fIVAya7sO6TsDK8UKKF2weC8h6_F89-O2SGVhwyb0BMIAH61M8RvjRBx2FPGKVOrtJ8fxWcDlJnkw0o6uvyhh7DE4BnhLwocUK_WuCcTtziQ0ughqdpu--T-V-Jb-AhclLAyMEDPUIzlEIm81O50BDHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=I4h9JBVaihtCsmAlflKiJ4zIci0dCdrs9NoEI2KkJQC-9xKOUkbJrn8Mh6AU99xXPnZbj_8EzptG-D2RsiTRaMoGnJg3AZpMBg_gax6PZ6KxhAWKFkEzDKrYZMMvmNNsWK4AtckJD_NX4vqh9LruCnyLoThQDvPQSs6NdWggb8hTtyoWsXO-ndA-xLXk7fIVAya7sO6TsDK8UKKF2weC8h6_F89-O2SGVhwyb0BMIAH61M8RvjRBx2FPGKVOrtJ8fxWcDlJnkw0o6uvyhh7DE4BnhLwocUK_WuCcTtziQ0ughqdpu--T-V-Jb-AhclLAyMEDPUIzlEIm81O50BDHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر اختصاصی جدید CNN خسارت ناشی از آتش‌سوزی در ناو هواپیمابر USS Gerald R. Ford (CVN-78) را نشان می‌دهد؛ آتش‌سوزی‌ای که در بخش لباسشویی کشتی رخ داده و در زمان استقرار آن در دریای سرخ و در چارچوب عملیات آمریکا علیه ایران گزارش شده است.
این حادثه در ماه مارس حین جنگ با ایران  رخ داد و نیروی دریایی آمریکا فوری اعلام کردن آتش «مهار شده»، دو ملوان با جراحات غیرمرگبار درمان شده‌اند و ناو همچنان «کاملاً عملیاتی» است.
اما ویدیوی جدید CNN نشان می‌دهد خسارت بسیار شدیدتر از گزارش اولیه بوده است و منابع به CNN گفته‌اند سامانه اطفای حریق ناو از کار افتاده بود.
یکی از ملوانان گفته است خدمه حدود ۳۰ ساعت به‌صورت دستی با آتش مقابله کرده‌اند و حتی نگرانی درباره احتمال از دست رفتن ناو وجود داشته است.
مقامات تأیید کرده‌اند این آتش‌سوزی به‌طور موقت عملیات را مختل کرده، پرواز جنگنده‌ها را دو روز به تأخیر انداخته و باعث شده ناو برای تعمیرات اضطراری در یونان پهلو بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13534" target="_blank">📅 01:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ می‌گوید دولتش بررسی کرده بود که نیروهایی را برای تصرف اورانیوم ایران بفرستد، اما در نهایت این ایده را رد کرد چون خیلی پرخطر بود و می‌توانست به تلفات آمریکایی‌ها منجر شود، و این موضوع را با مأموریت ناموفق نجات گروگان‌های کارتر مقایسه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/13533" target="_blank">📅 01:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ ۲۵ بهمن ۱۴۰۴: میخوام با آیت الله علی خامنه ای دیدار کنم.
۹ اسفند بخارش‌ کرد.
ترامپ ۱۴ خرداد ۱۴۰۵: میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
چه تاریخی بخار میشه؟!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13532" target="_blank">📅 00:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: ما به ایران رسیدگی خواهیم کرد، و به‌محض اینکه کارمان با آن تمام شد، در مسیر بازگشت، برای مدت کوتاهی توقف می‌کنیم و به کوبا رسیدگی خواهیم کرد… باید از شر این نظام خلاص شویم
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/13531" target="_blank">📅 00:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ: برنده این جنگ ما هستیم حالا چه روی کاغذ چه با قدرت نظامی
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/13530" target="_blank">📅 00:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/13529" target="_blank">📅 00:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ : من دنبال عملیات مخفی برای گرفتن اورانیوم ایران نیستم اون اورانیوم عملاً دفن شده و از بین رفته
اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران؟ نه من نمی‌خوام جیمی کارتر باشم
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/13528" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ:
راستش نمی‌خوام با آیت‌الله دیدار کنم، ولی اگه ببینمش، برام افتخاره. با احترام هم باهاش رفتار می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/13527" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13526">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak</strong></div>
<div class="tg-text">عمو یاشار اتاق جنگ نمیری امشب؟</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/13526" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
