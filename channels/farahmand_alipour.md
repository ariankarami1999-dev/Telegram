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
<img src="https://cdn4.telesco.pe/file/aGYe1VXalSvP8XA_AjnJqQwS23WipVc2fl4G2-8PslkMVKFE1sBfjmn38drIWp9tq5XiH-JHrEU_HwSrJ1ft0gRn8MkcBqiiunUiEcsLbgbk9p9oZkyIYJ9WJBMu-TWULiCCea9GOeWygZhhMMdEuet39bRQ2FDuxw6SArRl75f4AgIIKvBQipIuqKdk63Xwfm7jKyyAF86W5BpT5xIxszpvzr0AIy8daF9XpJWp4pP44D6rdXhA74GfOVRHRKH1nRc-8OsN-yIaSZ3_UheqSgMruuIpoMYX_kYjEpoRpL4mEZ4kwo1dgEHFSbqFvQBrCjI212v8dvcCQyhM2KWqdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISShzcooHJKo9U33ZDXDq_AZ2KJcugA2tOmTTiO3yIcJNhL0K9blPMXeMoSFtCyilTXr_FQJiKOVdCxDjCijfuREznkLlBl8MK9KEF6kmcIm1X6XgoPSHh0Gl9wLuhTN8Z8LfGJEwjRMyU_ZEOshCwKJalP_uQlHcxaNjPSzrbZUCFZL0LnYnkUB61aZ3MW_6H4djUwIG3Wev5aoqbjHx_j_6ZwkRM8S4NUhyET43dTuWRY-LuYhDKy0zmgZYnZBpVxGUhC7X76iytilkP0Y8zDOhLptjA06xJFO4HONcztMPfdIyZXKZp58qo-1Qk41v0cORmtYQQBCnciWHsSZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPyLKqC2Ab8FwvxcoFYjY2oFfSKAUwkj9D8tyFgarLb6TIsKRE4WMVddSDEp15xwSLMZJNViL-StMs1EO-s2RqN9jYc1L00suXz_KWtIGNsLZcfe03kSP8qQwUdHoYeiapXvPImTB2ownfO3gidRSHxDS5TnQPvpj9v1KWTNRra7deoGLGjfGTWwMSBwUybvPCO7u9AjX40-1uDBxJW1VpxdWisznZZXGvT3jTg2dfH7YQTLilMvasvSeSEj-mtTBt-RaMM1h7FrAaJnmULfj0BG7g2-nETFkGxOLcPvNvJXmaA6tXvWnKC9vH4Z1m5cqp9weB62CJAp-Ru1nLt8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3U90zV_bA9BbOnca6Qm9r9tfpK8CuQ9E6ZfjBvFNbdzGYtF559tvYZIvgODN5UeM0lwK4RfPQg3eKz4zjasuAYQ0m6CmGqtWDjyAZATYYBhuYPMs5Am5w4EjKyu9O6uzGoyWJO6Riv0kQd7aPEyWoFgREsg9WGoeM-mWJ4mcp2h90Z_0MhDCEzHMLUsqYn9nOruQ2t2QCgWbPqIyNY1VCWjvqQqSbuY3jNM7yOHskubRkFS-ZLlbRTrFmXgyNci_bhN39pWeIJ8j2BxjbexIyckXvpCJnwfYHqx-FvE8yvgqUK-1KmRfpRkX7hW75nzla8ecncrMwBQUswV0jJ2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L64VijQjG8pYE3raY3iuxVkV6-1zq3bglPgHVQP50WAkVunbPJyyR3AQqxvSVX1LlDGfUboe_vfpVxZ7c5pBEUd7jdi5yum3Kdy-47EFH4Nl7PRvucPA2i6zqx16agoTcxVdukSRwIjTtGmrnUvu4HZMoX72HfU0UI_4QWy2pxWP6WrBN2cciZ3toBwnzdN5ywegKHQ_FRnNgXMnARo7mfw1m2JqfhkGBEyWOHFzk5nG6QJSsgyJJg7_fDvJkVGZLGukObfNeIkce5oFW3yKakqW-cD7wy43RC3cIJZpYRNT5tFP3zyE9-GS9oBzzQQBUvdpUX9SMzkeipqMJ-Dy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfOG8r9Le797iCT_r1O-6F2tl1IKrJXs0hhcDjwGlX56-Y1VSZjX9DosHSHHmxdD-7WTb2uN5qBfL5GHqSI6RY62CuJAxxTW3WOtrHiOF69Ni6RfArcbx5TD3O9uEWXwsxB2qnvw5lCEJZnqje-nZXdG4YdkYzcaJ3GxibPUFM4LKxQb_b7TZP8xzIR8zeCuL5oY3GhlH6R41k8QBJm3NTYGV2RzgNtpeDmVdzNFO5ODUZ_XdDwc5sxN4ma5TjG4M6Nr9rXx596qMmqnNNdc2RGXTN4HnxHvJQA5_Lun6ez4FZyYfadpFbg5jkH4gyaZkTDqSlLeU0-DreGOFmjkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAkGBrR1Wrrs-8F7EOCnSK_eDHa6IPFemHwWozUNCnPROiCVN-F8kBITQ7eLiAPkAAfll-kqLgM28jHZwsQgngLvKKZG09AZ1kDljgbZomBYyJ3mfBLYbyIC4i_HjjfddbYOpjBEpdPU1BeVm6L2EBr5rYE9XJZ4vCiF6TBFm66zyRGaADSGmvQxR5xKhgS1E09Mbn1JT8CTFqYWxwfL_k_lSuj7CTpMFQ6IWzb3KF3SiYj0mzy4dE54EyFqY4eQT3K2j3eywYWAil30i22CjyyFd9EXoaYjsgi_R3OSWg5wmDdfi3GIfaIyxvcrt3K1ocMCHQEn8rmOOFUfRTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=S0KomKl7r-hYoLkSwmpE9w5-ziSe5jn7MDQ74oB64I9TwCCWS1xmmixv77y_E8DWeOrWy0GFqs6akuL-7yzvpmcaKlpAYPyhr2ZuSVJLqpiLGaXT5dNrJchimNWLd_8KLBq9dcicKvlS2XtQsRxpG6RV9pKXbGcGElD6hQaJq9Fr4cqEuPEJFZX3vszX2hS3w404T5EHl7BOXcswj4-pNTV0zkiaVTOcVWLe-WgpKqUWc7fj61EcypGUgUJy0sPTYplWo4-f0CFS8usOsurrqxzMFryUS7ke-_xfGLlgrETIYxErFQOGyDSxN4AmBv-wjUlQ-6sq-pBBJB3T8VP13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=S0KomKl7r-hYoLkSwmpE9w5-ziSe5jn7MDQ74oB64I9TwCCWS1xmmixv77y_E8DWeOrWy0GFqs6akuL-7yzvpmcaKlpAYPyhr2ZuSVJLqpiLGaXT5dNrJchimNWLd_8KLBq9dcicKvlS2XtQsRxpG6RV9pKXbGcGElD6hQaJq9Fr4cqEuPEJFZX3vszX2hS3w404T5EHl7BOXcswj4-pNTV0zkiaVTOcVWLe-WgpKqUWc7fj61EcypGUgUJy0sPTYplWo4-f0CFS8usOsurrqxzMFryUS7ke-_xfGLlgrETIYxErFQOGyDSxN4AmBv-wjUlQ-6sq-pBBJB3T8VP13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmwMFkzu-ZSmk4eQ_q-FTjcm_glsTaNlNPRSYlPCaUUtLBoF-IJNKGp-sf9FSOOLsouKFU2vPEaVYvIHAib3LtzaB6oLQ-xflSapqtdiZHKsTXbq3t16E3w1E5HvYVht0HNiqo60uzyaU0DoIENCWeBCgkrrHPYFEfveTAA_R40XOt9soH3y5p6l51eA4F0NGm8CGY0_hkyovYL8kWT4Q3dn7-NH6zhCpeQoJi19eReZ3FeFFjaDmgcgFzHR5KxMxV4fBwXJVgKtBJjxC7spXNbI-rA65CRFyUztQjP1gGPNETDswlbtsAiQcvhzqWGN85zRZAhg7xAefurpXCIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhVTfv_EKv5h5qoTkD0KRuzNC8V3Zb3D_XV2eO8BDaTuov6lzLmugqkQyxmiI3AOUTgV5_AJswWVBTQl1ggV9WO2BI27T4KbGNbfRmOYbxru92ZXfBSEC03-X62VuPeuN8iehidg6OfdUbpJOGikRUgF2073Yho0xRfj-2xk5rhGnLtD7E30864oOlwIkFmLucVuJSLyKuqIPZmmNzLt6deSAUZwTIumoJvExRg-QL8e5z48LmarQSuozBzJDNwxc4N7XqctqHjyGYSt8CoOEWXDAWYsK3mwxlnI08sMhudWjKHJyzlaP6qEJlM-SiqM3vt2mCpH49U429u5uXZNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnIbP8ejH5EkEjLaZbDouVOn5nxl2_FuX92tuIF9reaQvmv1YMg1xfE-RHaqyX_NRlOtjFPkCf7bMaOcLwMrb-a01cK4qkocgKADBrEWorHIZ9eIQu5yQte06lH1nPWM5607Wc0YRGnHVpvBI3cnN8PfaIML8bbEaIc_oYq1yM6Y7yNpfyLglPIZLPshw71K3hRe0aQrLHsiGpQ-eLvzftv_m8qt8QDBf7aFnRnddq7BN8i7TcRSxhOF7AZ_bTAYdW2esIjXcyugYTNFXERNyNovuTwnusGm5nquff3lg63blHgULwlG_8B3II98wBQnyUspQiA39qLrEsml8ib2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=qF1yBQumuAORZNRNWgE2zn_0ozJLzhwRYGlRBnxthSVr44BoQfoAsgMS9Rvc84LlW1t7PvCZGxebE-_YumnE5tf9sonp-wUDT4Ri6aJsyvWhnks1PG91w1XDoa9ojMyFBAyuIJ5M5oAVPxwKkTbdq9vYpIvWsXo7OIIgphxkge9v88dFmNTOwYKBXOuTp-0rOhxA9ZEYU5MYl7rCZXx3RUBX28Wl5YqtCJMkraEb4f1G7YtBbOyK4o5gP0zPXgcLZ8WPPb7WccRHBH3EkR5_spsNlPuojgtIl0RmBQbNahgfRM4qaZBqwrzWqJGifEvF5hzTzIw1X-nc6upY8KCp7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=qF1yBQumuAORZNRNWgE2zn_0ozJLzhwRYGlRBnxthSVr44BoQfoAsgMS9Rvc84LlW1t7PvCZGxebE-_YumnE5tf9sonp-wUDT4Ri6aJsyvWhnks1PG91w1XDoa9ojMyFBAyuIJ5M5oAVPxwKkTbdq9vYpIvWsXo7OIIgphxkge9v88dFmNTOwYKBXOuTp-0rOhxA9ZEYU5MYl7rCZXx3RUBX28Wl5YqtCJMkraEb4f1G7YtBbOyK4o5gP0zPXgcLZ8WPPb7WccRHBH3EkR5_spsNlPuojgtIl0RmBQbNahgfRM4qaZBqwrzWqJGifEvF5hzTzIw1X-nc6upY8KCp7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=nP_La9j_erUbbnS6bsVHHe_yVZb4OAOrQQZ00hg8Pe_kwXk2YCsoHvXgm3fyYjz-ELK5I9B48CLxmO0noOwKcafetiDQXwuFk7Y1qtT7eF9Q7oZNS4cjM95wTU494VdW4xccdSSjFKqab_lVTqzqfWnzYiTVlKkliTO8ZlxC3SFT0UEdFI8zDFTm6hoXnMlwR5HBtmqIZeJhURAo36Te15_xatQ2HoeSzJyoB6T2qbNTeFOusZ8Fpjr5PAz1yb5Jm_mzKN951VnxvqfD804tmX_l_KoZc7ij_LIYAEOzU53Ut60oHT2kmAB_9YjjGYFOzRDnbctMJmx7nK61aSnE2EbpBzoZ5dr2eHPg0Q5jWR67gSL1-Au5SmBHs5C2h8C17uUud1C0ePWpE36rBrCkljsIxHA9LfALWEQsLvXfyqPUEuLik1scJ4rPYPATewr1sqZywBB6cnQ5VSf-jrRheRb0FyT6-IykhUehRUf_eGHge9OuqJLGOGgJ3Oa63yCc1pXaBNA2gPREK7EruNqnDzzww1jCiZpHm4GZR0g-kf1N21D3rPGJwD9rr7QmDEyVkVH2D2EGk-S-sJbWXk1js59-MSGV-YrJk_GpANjTMjZnYqz6GFVv7SXEim6l-S7WcTAhgQcPO1druBIJUM3YqdDXwspPFqmBXluqBiWEEWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=nP_La9j_erUbbnS6bsVHHe_yVZb4OAOrQQZ00hg8Pe_kwXk2YCsoHvXgm3fyYjz-ELK5I9B48CLxmO0noOwKcafetiDQXwuFk7Y1qtT7eF9Q7oZNS4cjM95wTU494VdW4xccdSSjFKqab_lVTqzqfWnzYiTVlKkliTO8ZlxC3SFT0UEdFI8zDFTm6hoXnMlwR5HBtmqIZeJhURAo36Te15_xatQ2HoeSzJyoB6T2qbNTeFOusZ8Fpjr5PAz1yb5Jm_mzKN951VnxvqfD804tmX_l_KoZc7ij_LIYAEOzU53Ut60oHT2kmAB_9YjjGYFOzRDnbctMJmx7nK61aSnE2EbpBzoZ5dr2eHPg0Q5jWR67gSL1-Au5SmBHs5C2h8C17uUud1C0ePWpE36rBrCkljsIxHA9LfALWEQsLvXfyqPUEuLik1scJ4rPYPATewr1sqZywBB6cnQ5VSf-jrRheRb0FyT6-IykhUehRUf_eGHge9OuqJLGOGgJ3Oa63yCc1pXaBNA2gPREK7EruNqnDzzww1jCiZpHm4GZR0g-kf1N21D3rPGJwD9rr7QmDEyVkVH2D2EGk-S-sJbWXk1js59-MSGV-YrJk_GpANjTMjZnYqz6GFVv7SXEim6l-S7WcTAhgQcPO1druBIJUM3YqdDXwspPFqmBXluqBiWEEWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY99gAqmpfiE2H5fH1NbbcJdbCNKU1rLFCr6H-ZPrh-jxzqYliRgE_9fKPG3oPjiT1tUqu-sZ4yegwnJrr2FQCS2xG75FeV04OPOXvb0i0nP932ie1QqKYbDKygi_JNHPkVqncZoIp1Pp2yunnGYmjnSotn78rLxXn03YY4G3JJtYF_Yl1pG2vfr6KkuWpsfMc5SV6yRxXGFd-ZErHFnGPyTO4TxIxFJ_iPgJPq4MX6gwxgHr1Re6YmWMjEFswPjZW06wXgIdnItb_BpRVBz7EU-yxhs37xMI9jOcgzHm_TV4ucJbeALFQrhKE9SrLAlpi25jB_RByDQwjrfyV7V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-StYa_HezuggOPExjcWAXnppAVK4X81lBUKtruqLDsS7bCKD4yeslA4IEARLXmPtP8e878evr3L4Q2thyBjUSc6v9-LCHoUeoa4Qx0eEnjLHdzTiKUSv_mu_eXarqR3xvgZYeiTGANNZiaHoaKbf8-TewLIeDqBRFLBgwTYmQ6ubQWqgX40Xv-3t21wxzkA4yxZOJpzN2NMIdFI88tNuTekczpNZxH7XpSv0ykeVXTiuc_qd-x20vGiO1UEVaDXew7mn1kByNYvMi1C446WX-szolHJ3Zi4T5q6U5N0BM-46jreVIgM8N4x0wgvfrdbnAMEP6cEksz2Aeqis5h3nzcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-StYa_HezuggOPExjcWAXnppAVK4X81lBUKtruqLDsS7bCKD4yeslA4IEARLXmPtP8e878evr3L4Q2thyBjUSc6v9-LCHoUeoa4Qx0eEnjLHdzTiKUSv_mu_eXarqR3xvgZYeiTGANNZiaHoaKbf8-TewLIeDqBRFLBgwTYmQ6ubQWqgX40Xv-3t21wxzkA4yxZOJpzN2NMIdFI88tNuTekczpNZxH7XpSv0ykeVXTiuc_qd-x20vGiO1UEVaDXew7mn1kByNYvMi1C446WX-szolHJ3Zi4T5q6U5N0BM-46jreVIgM8N4x0wgvfrdbnAMEP6cEksz2Aeqis5h3nzcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkgxXrrnvq-Int9yVMnArh6mtvdaox3lK9FFl153mKV4gKbMiAoyLreSLqIS34rXRGgvpxg7WmMFQ5Zv3biCMHTjrchzYIQJDxqKzw4aq124-J2Xh9jIA6EMzdnMRskeStY4nMw_iFaSNZLQoFPlaRZ957m7H1v9GcW8-yNMFGPlmwVevSDhSwBe18kGrcB10oo1_ZJ1V2_vamtNa0L9J6R31VzlSC8-iZpkjFo6XRZ4GsubAvVrbHiXoT1HLe1nXMHY3AdAuv9OGH--cWcPQBu3eT3BK3OzK8lCwUsvhIzhdP5stVp9O8S0tu_hOE7TZriQU0QAg7kdG7isa-2uYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALo1KoIzAzbDkoge5wlN6Mh0_89wIyvBnr7TDlKhVaeGbAj0YnB1e4Yy14KGp04ebbT5KXO2SFMONH4OWx2zIcBzvuXhvUtbpxZkafl7aA-FT9zs3bvf2xptpW5SzGSWMrcbuUfb2MzNkqzsoSoJZt7_ziLxbfIGigf6_RB2uAIIwunVG4AZloOoqsauVZL20CDcbWHj7Xga6CvmVt1pGdgH4hlptlGoJNgs-oucnn7tVeYoRDTSG8Bb4_GCTRpmvdjcwNoar8iBHCKO_4KxENLY6Y6sAvpIA0YCDZkwIxBGQljhrV6kLkHJ3whUkgOh93VZ6w-HUcQTpw5qMoaGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeGZNIlBQJD7qCSLMHfIqpQ0kF6eGjHKwkJVHJB5a0N48banT21f8WEIglc6uEPUHjk8V_KqDhx0JM67PKEV9iBiPfFmY2OwwASefzWdyzUGemKfhIWM2phaLCoyguf-40ae0V1YnHyUqOFCF20IBPR_7lOUImOMX8j6Nis7kJCXgqLQvwCnWeeIl9VczsjZ3I1k3xbpm3dL9ahALIrLQqwhEOBzSkjIbyNKDfS_ZNc7Oy6nLFeQgKp0reI146nyooNP9G6Vk2x12ImdScZzAOA-uro_8BnZ67TmPgY-1lzKKS4jfLoSYtgEYQEvtxrVCnacfXWG8ZZ0NonwI8NeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به این بخش از نوشته نادر سلطان پور که نوشته بود : «فقط ایرانی می‌خواهند آن‌قدر ضعیف که هیچ‌گاه تهدیدی برای اسراییل نباشد.»
پاکستان یک قدرت اتمیه! ترکیه ارتش بسیار قدرتمندی داره، مصر هم همینطور،
چرا دنبال تضعیف اونها نیستن؟؟
زمان شاه هم ارتش ایران بسیار قدرتمند بود
ولی مشکلی با قدرت  ایران نداشتن!
بهترین سلاح‌ها رو هم بهش میدادن!
پس موضوع «ایران» نیست! رژیم حاکم بر ایرانه!
چرا با جمهوری اسلامی مشکل دارن؟
چون اونها سیاست شون رو جنگ و نابودی اسرائیل نگذاشتن! افتخار نمی‌کنن
که به گروه‌های تروریستی سلاح و پول میدن!
این چه ناراحتیه که ما میخوایم تهدید باشیم برای اسرائیل و اسرائیل و حامیانش مخالف این هستن؟
بیان کمکتون هم کنن؟؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_U9xkLeiHppY4y6Wus4HAVQcbmdy-D-5vZ8dKiLE4n5aLfcplqIFiDbA-Me5EdyGxxs7lLYU34LBC394Nyg25sLMmoGPOMWFxShId9kkv_fh-B7h-YOYaRcjQF2aMZpgUIwQKECmalayGwuiBzkUNEXWYg9DATty4dxyVFz4Ua-u7dB3cR7DJuGwKkk9PS4aeA7GQHkbTFZAGqiq9iaqQT1Z04s56evgWihFLiBa21BPtUCGT71B_R3KxUIzuk5t2DCZ52HMN39rR2bTJKhA8pkA1ooLA6lqC6oSrVpzv40L5ul7jThPrnkDElmihStGYRkekgqNIGf_lRED2_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO02MrPPdB0jtUZGDvdZFcSEHrTkF5fi-d-lCVh2_xAU-DPjyo-f6_-FRzFWa_V2rDN_7StotphG1RSCzYH3oxNdfNK48V58kf3sHNbYl5wEbJjEEMNkQnGuQW2uUhBlsUsrCxY4v3YATosPTOOi0iYzsvovM97eq5WFNlojNPzpCOz0i-qstmr3kcvOWi1BEQPCdfsKjREi9JUSyag5Urcc5Pd_Oq6HIEfubjnJYVZeFdzg4RlKe0EQW98dMCjLt4ax2s4A0m3CYEIfe73yCj5eMlcaQO70BLMjfTcNpC5zKgwWKXJ27fV5nKgUL0a3_nLLVOeVnGi9kFtx9861jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaPTPGewu5JJP40SfWJ8gsDSm1j7YHI8QsP4a6UiSAmwJ8lOaiNOo7xeD7ZL1L5eqpQe0Nb9BdN6W5iXZrASQJHEiy025Wc_Y-JEDCkE03NHHQtlPX3qETZgYdxJbDFnbmFcxeSxXWVLBYdp4DoawbcuOKn2uTcxClcbp-1AwKXna6jtJjveCfca-LnlucZ84MRZwS9dTxJotcRPWDAklZ07p1tN6sXowPI_E3ohUleENkbdNWsqEgWbaeO0DMKCXPay4ptNMW9thWNgKiS0zxGdMRNxHgOqVdssv3v_LJwFFNbRwwKmo6ldNkT54WE9Qi50vTmfh4VAaOKt4u1h6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=nes1P3-xNiNM0TezK04tlrSjzBooX939QsLCC1QBdU3Ahb_JOI2DEo90sSd3WtJ1MYO_JeOehthO0rUkjRJHwF4KMa65DkTdinWoKx7xFdv-QdKLCfiIS2G4nWFiY3mQBVHvtEIGfHKsouurZRjwYh0f4s4ljl9KK3o7ch6Qf3LVm6aMzwm49NjJ9BetIS6m16e3OGXyaPxN7ny19LEy5Ex5pGJuMsOtXV4_yZLoIq8W2DWDe_n5EyjaZY60uRhwgilO5Y3uulmjcHMPrYPJYO_wlVrPy-CgFxkrQvZKJdjJbygANZD12v14-I6IWdI-GeCzsQ3kP_ucWJU7XUBm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=nes1P3-xNiNM0TezK04tlrSjzBooX939QsLCC1QBdU3Ahb_JOI2DEo90sSd3WtJ1MYO_JeOehthO0rUkjRJHwF4KMa65DkTdinWoKx7xFdv-QdKLCfiIS2G4nWFiY3mQBVHvtEIGfHKsouurZRjwYh0f4s4ljl9KK3o7ch6Qf3LVm6aMzwm49NjJ9BetIS6m16e3OGXyaPxN7ny19LEy5Ex5pGJuMsOtXV4_yZLoIq8W2DWDe_n5EyjaZY60uRhwgilO5Y3uulmjcHMPrYPJYO_wlVrPy-CgFxkrQvZKJdjJbygANZD12v14-I6IWdI-GeCzsQ3kP_ucWJU7XUBm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/noyies7Lpo1Oj7HWOaKI8qrhDynPM3teYto3hB92rPN5kyYTqRD2Fp5_IwpRIoZ7sX2BBev0qInjaVkcazTk1QgbKAUgWY05Ved_tYVwahP4gQyWSrNrur73UPDyWH_4wye2lKQME68mRiy0MmR4m72kehE7Z1wWDOXCm49rVqv_XOh92bVMVqA01oYezCIhLEbV0bbYwUYc8uqxpgchnw8MZoOsEUnQLmBZvB_SXmdUpMO3tJL_pu46UXyTdXaPuMsivp_6P37gvRbKVbLi0IRSadVXb6GJ-c7H9nQCjauFHg22DONFEZmTbITVVFSJzCc957fsY2zeO6lzFr3M_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAd60eEWWrLKp2TAM_hODk0N3QFkxP88uO-EAZ5-mwPOk2c1xYQ7cV9kv8ACxbmaFlfBXms6rgxLmKtRY3ntfz2j33yS1B46HxjVmwPypcqZLZOiMdMZ91t96Lnqpt_GyqAZHz8B-AaiizlB9-EEnRC2NSowiv1AwltCakvLI-eMQx--29txUDo3HYIwrZg9BOLAwKFMTpGVLTCzQjcT4yhkP0yLS2jbj9EyJWYfvLC3iSGdPDZx7XYngBG7SPc523EQPrm3FszwOf8F7xiscE96uc04DRC_b6LvHF6f-KwDenP4pyKyy4Gwdbg5pTLJICDprUURRP2lfkuTTQU_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBZzkYfTmeZFAuZVvTs6Nd3Hta3urW7QPJ9V8q34Z6Or6AqKF8o_vlTiGOTKe57GelNoolsShwEmf6Te_v75xS-gqdv-7LkepTFIwOM3V3X3tExQU-Klpj82YszwKe_XLHNLCummZqFVsi-igb0FQzr9soUz6YTDP-MpEMv_V6E-xB3fqJMvVSMJdB0qS0DY2wLTiev7cV-YAW-XbgqPQ2aAbBUMpOxA0ru0VWTQgg194YgZxKxqG49XP5qDFd1r4VaIQRUrY2W_6AOCvoKsVnxtTfP_6-fAmbzs9PNEpqsY8M2R6GweYJ2Q6_-f6ltjHhuT4CEj958kfipKcTV6ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=Tiygwka_7Hujb35d0jYKSwmTOPvuT12YW9K5KlxGNpVnaBgd5ysFMDLqRHsf8lvXxatTtRzsTZ_fH5D3_stHGET7lvBH-rdco2foOkSGwXGWkZpzqu11aIRxm17KLJoczOqLwafk8hTj6Ir4t401VvHm1qRvHPdqTJXInqRBKGxs5HMZzVWn_GviqQxdrSWIfPaXiKXWXT__DRQTE-q2wY5D8RVlsDSD3dvcQPgQY7bUgQ6jwdYLACIEevycsIcSMR-HpDQlXUY7eUwwhm7o7HFEGCCcUj6FmoM_VLQ_XG1N-PrCUieZOjgLNvAl6Z1Y88qwUXJgdwZnGoJv9so4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=Tiygwka_7Hujb35d0jYKSwmTOPvuT12YW9K5KlxGNpVnaBgd5ysFMDLqRHsf8lvXxatTtRzsTZ_fH5D3_stHGET7lvBH-rdco2foOkSGwXGWkZpzqu11aIRxm17KLJoczOqLwafk8hTj6Ir4t401VvHm1qRvHPdqTJXInqRBKGxs5HMZzVWn_GviqQxdrSWIfPaXiKXWXT__DRQTE-q2wY5D8RVlsDSD3dvcQPgQY7bUgQ6jwdYLACIEevycsIcSMR-HpDQlXUY7eUwwhm7o7HFEGCCcUj6FmoM_VLQ_XG1N-PrCUieZOjgLNvAl6Z1Y88qwUXJgdwZnGoJv9so4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=lRFSeR4o4VlkttqMLPTTqh76WtKXv5vCaAoPKA1TOcW1HfmAU1uV7K4KzV2Fz4Dqt6evRCXh15quIFyHhqMuAR7EgiNrNRVGivilIZFGt_sK7pFKeO25gs9qmwchIint6T81_AuPZg4fdbKbGi7zHD-J8qt9q0Dim3jhjjds6G8exTNn4TU0A_N2VElWgUcmRJF8rdL5VZN8VOI_V2yyMltZShDhiawkhZNQF9300ap64Iakwbo3yFCaH7_TmszOr1cgBAQ3UbEJuGzCEVR4AH3Za9fF_ONBHxKVgLtDiizJp5II3204oefDSyBFfBJYQSPmqjCnFqpockWJm7wTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=lRFSeR4o4VlkttqMLPTTqh76WtKXv5vCaAoPKA1TOcW1HfmAU1uV7K4KzV2Fz4Dqt6evRCXh15quIFyHhqMuAR7EgiNrNRVGivilIZFGt_sK7pFKeO25gs9qmwchIint6T81_AuPZg4fdbKbGi7zHD-J8qt9q0Dim3jhjjds6G8exTNn4TU0A_N2VElWgUcmRJF8rdL5VZN8VOI_V2yyMltZShDhiawkhZNQF9300ap64Iakwbo3yFCaH7_TmszOr1cgBAQ3UbEJuGzCEVR4AH3Za9fF_ONBHxKVgLtDiizJp5II3204oefDSyBFfBJYQSPmqjCnFqpockWJm7wTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFSc9VpHFHQkUlLnkUZtwJwKcIRS0AzNqCt1V3-oXs7oCRHmvCfvgR4jzB8oYjugGYJCGQO_cxiEvPHej4tluxVKHfrRQN-Pnt7fiBbrTmsW6l2MVKB2fufvBI6s7F9uVwclen7j235zMsPFeFfDzsHM2miXd2igkpMTNHEriT59S-68ZUPiPAdedwSDyN_NkuhJGqfAb6WmB93cs5RI11fQFzkfqxDB0CXHxXNJCYE5mf9B5OnPNc-lZzWMRmN1M48C2OJajii1vIwqt2ZTTp7sLYxP9mpxDZSJyBkM820QtkPED4O2sABaGIpaodUV9kh26mGHy2KfUvyymnToC1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFSc9VpHFHQkUlLnkUZtwJwKcIRS0AzNqCt1V3-oXs7oCRHmvCfvgR4jzB8oYjugGYJCGQO_cxiEvPHej4tluxVKHfrRQN-Pnt7fiBbrTmsW6l2MVKB2fufvBI6s7F9uVwclen7j235zMsPFeFfDzsHM2miXd2igkpMTNHEriT59S-68ZUPiPAdedwSDyN_NkuhJGqfAb6WmB93cs5RI11fQFzkfqxDB0CXHxXNJCYE5mf9B5OnPNc-lZzWMRmN1M48C2OJajii1vIwqt2ZTTp7sLYxP9mpxDZSJyBkM820QtkPED4O2sABaGIpaodUV9kh26mGHy2KfUvyymnToC1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسام الدین آشنا، که قبلا معاون ویژه وزارت اطلاعات بوده، طوری وضعیت رو ترسیم میکنه انگار ترکیه فقط یک فرودگاه خوب در استانبول زده،
بقیه کشور رو رها کرده! اما جمهوری اسلامی
در همه کشور فرودگاه زده!!!
ایران ۹ فرودگاه بین‌المللی داره!
ترکیه ۳۷ تا! چرت و پرت!
یه جوری میگه ما همه جا ریل و قطار داریم
خب پس بیا بگو چرا مردم قم، اصفهان، شیراز  و…..
برای سفر به تهران باید یا اتوبوس بگیرن
یا خودرو؟ چند درصد با قطار میرن؟
۵ درصد مسافران با قطار میرن؟؟</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmU9B7Q-0EU663L2CEn2MQ0iyTJc4g5-Wtpvcj0HGMrJyleykjK629x47HRiZ8hO2Bvwb28y3q5AsYdxb5I1ueBsWMHwA4EpXNxqg5iHBOAKkjMn4FF5o8j79lRmqYLUJNOofgMPIpfZmKL-yACFZ0CXpZUnMWvS6UbLaEE-Vn4S_BcbwWKJ_7zTx0HYRED4RoceCuDyDYUVt4F7wF05j5GfsK3o3IeUGY-oj7xqofEUN12SBU2R5PTKeS276IQA-SN2K0cxf8wVFZEH5NY-siSVa44i5RsJPUnTf8RCethA6C_zIwRNZYPYXI_OUnq3SiigrD1J98FheH2mNpDZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnnmM0zc6Jh7NloseZzlv9kRE9h4uFMoU3gomlfb4-_KitNsgRwfZfMfR87t3WKbV7uiwDIqg_i78JLu79qZvJ_htla038buj4CRgwQgnWqculVKkjU1bhHP3C_0EpKP3DOiLGB96jfPO7AtooOPlG3DrI7Z864K_nkQaeSECaKGNhPUMzL3cu1sAF-K8TzP6C1GKay-JsLCM-jpcTOKyIhzWsrM_wb8r-PIs9vbxZVfCN7wh90FXFT8TdA5otW1Ta9vv8Jbgjf5e-SJhGledhNYFN5oIUBed3XUqLl7-QVsFH1Slk_KsxDlxW4MwioWWmOWRPh_JD6v8E5ZcYFsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=VpyLdbsxmmPJrht29Hd70qJkXMjsN7wgra4gk8jn-DdRb4jSyCNoF-VeoF4BNREaMd_BmKfY4K1kxGjJlTmM_IydVEf5Buppdtw-4-NbzuGFhM4OoJP1wFvNfNU0hyE-aY9fBmXjOSnJkHUDPcAYC474gh5FrdW1wEUxhrRrAixqZl_tjGiVypAcV-zBcWIc_V5tkWDpGEP-wzd-IIt2eO1zee7CP_0JTdxLnyJ7nel_SaeqjLh9WWFdfp4fojWzar8Fc_KP28iK9moUBCclrvuUjGCneQHYu7KvQtfBkvRafjiB1Z6NQofuVQqbIDqQejL6OgY6DXbQ-VI5mG6bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=VpyLdbsxmmPJrht29Hd70qJkXMjsN7wgra4gk8jn-DdRb4jSyCNoF-VeoF4BNREaMd_BmKfY4K1kxGjJlTmM_IydVEf5Buppdtw-4-NbzuGFhM4OoJP1wFvNfNU0hyE-aY9fBmXjOSnJkHUDPcAYC474gh5FrdW1wEUxhrRrAixqZl_tjGiVypAcV-zBcWIc_V5tkWDpGEP-wzd-IIt2eO1zee7CP_0JTdxLnyJ7nel_SaeqjLh9WWFdfp4fojWzar8Fc_KP28iK9moUBCclrvuUjGCneQHYu7KvQtfBkvRafjiB1Z6NQofuVQqbIDqQejL6OgY6DXbQ-VI5mG6bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ایران از عراق بهتره؟
این روزنامه جوان متعلق به سپاه !
در خصوص زنان ایرانی بدون سرپرسته،
که مجبورن برای سیر کردن شکم خودشون و بچه‌هاشون روی خط مرزی بین ایران و عراق «کولبری»!! کنن! در کوه و دره!
چون به این پول نیاز دارن، بیا بگو چرا شهروندان عراق، که روی همین خط مرزی هستن،
نیازی پیدا نمیکنن که دست به چنین کاری بزنن؟
اما زن ایرانی بدون سرپرست نیاز پیدا میکنه
که دست به این کار بزنه؟
تازه میگه بهمون گفته بودن به روستاها برق نبرید!
دستتون درد نکنه چه منتی!!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY2ZDIQhZCSvMABPh_sdoGHXkK_ld6ORLtPShuEfID-7yHeo3rN_FNw1JqbdjVFZ-M-d97FUGKW96QwMSSp0ujBNE3aLUkyxSLyX6SkVVZijiI022AZxI6o_ZlRLUgmHt1inlU6R4ffN2oFERy7ynkZwULHI3XEqk993eNs_zmkuA1tExmtkptBtFCzJTZ0po9udx8JjTQXPbSiB9AC0wKF9yKUekE-bqfefhFXfabJL-GaHyrX6pYW9lDATjV19gv-Hg2m1u8bqejtcYQ4vfsp5wp7TBQmU0bUqshnOMnLkIie5S8-BC_1VVWdxnlyxssyHrO_3OfxxG4MvfNiWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=dwUKI8YScc4J0piJQDyuZQ5gKefQ_Vlq2mbnMlpNMQ0UUnjlgT2PskgFLBUZZGasQyGVOfE0BIVCv5emTlpIQzQKIXCAgL_pZ2KtOK9mcZ_R7QrcFRpoydRczpFyrqVhtxRYafkuO5lWUjRFD6Y1rKUsySNl1AWeaLSZqUKtZ--ONoIHtnzxekJa1FEoJJEcH0MSuODiOl03nYxEglveHrfzY4Lsul6A66E-2GvpUkkEQwLfX9TfrG0HJyIZkI9WPSyGsJ3-U35b_LOcenv7mUAu5vppPjVr17wSqK7HqwkvMNmIhjDwkneersGCVCdCHjlNWtwhNZv_tFTwi3TUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=dwUKI8YScc4J0piJQDyuZQ5gKefQ_Vlq2mbnMlpNMQ0UUnjlgT2PskgFLBUZZGasQyGVOfE0BIVCv5emTlpIQzQKIXCAgL_pZ2KtOK9mcZ_R7QrcFRpoydRczpFyrqVhtxRYafkuO5lWUjRFD6Y1rKUsySNl1AWeaLSZqUKtZ--ONoIHtnzxekJa1FEoJJEcH0MSuODiOl03nYxEglveHrfzY4Lsul6A66E-2GvpUkkEQwLfX9TfrG0HJyIZkI9WPSyGsJ3-U35b_LOcenv7mUAu5vppPjVr17wSqK7HqwkvMNmIhjDwkneersGCVCdCHjlNWtwhNZv_tFTwi3TUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Rk8HavDEjNACWAmRrz-22JxmevvHMCKOxojVAlACbASQR9ancxScTAXrJaMwpDoKoAnCpZir5KAK1_tyNyO0dfjc3e_hcdlQVccomcJL_OZS6ncapXyWSJGe7y504y2bsaxaszqlhEodU1vOA9DdaI01iRNpZBLxTVNnvpZrrPXm73PcHYDh_4IHYQkpzRjQRxt18pKiHugXRaH5yr1-G7EOiStsc3-EE1DjhhamrCF_nXCxQ_thgv2EJOnuEM3-5XA9mGHqdivS-SAdf-fZbB5BbtFYDetY7veLwvvWPA3zi2zueb0s9Q2p5WlHVPJpUVGMtPIhFqMEyUypT4ivpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=Rk8HavDEjNACWAmRrz-22JxmevvHMCKOxojVAlACbASQR9ancxScTAXrJaMwpDoKoAnCpZir5KAK1_tyNyO0dfjc3e_hcdlQVccomcJL_OZS6ncapXyWSJGe7y504y2bsaxaszqlhEodU1vOA9DdaI01iRNpZBLxTVNnvpZrrPXm73PcHYDh_4IHYQkpzRjQRxt18pKiHugXRaH5yr1-G7EOiStsc3-EE1DjhhamrCF_nXCxQ_thgv2EJOnuEM3-5XA9mGHqdivS-SAdf-fZbB5BbtFYDetY7veLwvvWPA3zi2zueb0s9Q2p5WlHVPJpUVGMtPIhFqMEyUypT4ivpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=IbkBJgg5xTyhKB2kTLWPe2J19NhD8FFd24GlATi4Zmk02-5Dimuqtdwe_fPVOVP6BVPI3_oDaRAgEGdi8K7sjJEsd9dbHVERVnpUU9TwZkjAEDFpsIF-nzM-HndX2bzX4ur4hivf37cEn6iDCC2e7zHAUsnDeu0RRx1OkNmMP6Gte0-p7aZE1Gpz0R5m3zY6y13PNJy7cYhqgBxvxdo0P-7ayy3KNOE1u-Obnl0zU4M4NMAoOy8o69B5AXJUL0c5FlOlN0SiCsQrD6g-B_bW1ShXl92dx_Z0fhcl3m74GETn1qREAv479gysBj299V4JGOpT8XnntaT_dGXdqWwyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=IbkBJgg5xTyhKB2kTLWPe2J19NhD8FFd24GlATi4Zmk02-5Dimuqtdwe_fPVOVP6BVPI3_oDaRAgEGdi8K7sjJEsd9dbHVERVnpUU9TwZkjAEDFpsIF-nzM-HndX2bzX4ur4hivf37cEn6iDCC2e7zHAUsnDeu0RRx1OkNmMP6Gte0-p7aZE1Gpz0R5m3zY6y13PNJy7cYhqgBxvxdo0P-7ayy3KNOE1u-Obnl0zU4M4NMAoOy8o69B5AXJUL0c5FlOlN0SiCsQrD6g-B_bW1ShXl92dx_Z0fhcl3m74GETn1qREAv479gysBj299V4JGOpT8XnntaT_dGXdqWwyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=u65jSdiMKKwHZvun1yCmoL5_GALaB6v1oYuKE_waZXdNFoSmvHxxeQMaufEJoNH-1O5gBtOAdtrHgf3wWeHdJZRRwj-9J7SjEoPDJlJCyDYdkmSHxyo2youKdhnb_VP43chHAUoi8dz8j2gdpNeTeeQoHyzMiSGszdv1odgCvqHDVx7I27ddGjSVg54SUZF1tGRFoE4ZgB_peGHiQwz5up-ju7Kjv-2K7tPQ24eK-i6QoGLyoM2y7BmXNrScFFfOD_w0Kyhqjz4c9q2FddHLjSpwTh4HxfWctAJkwC5gqL0VLOKBH3jXSo3Yb8FIeW7z-XcU8P8Fm8pDJLjMUzo-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=u65jSdiMKKwHZvun1yCmoL5_GALaB6v1oYuKE_waZXdNFoSmvHxxeQMaufEJoNH-1O5gBtOAdtrHgf3wWeHdJZRRwj-9J7SjEoPDJlJCyDYdkmSHxyo2youKdhnb_VP43chHAUoi8dz8j2gdpNeTeeQoHyzMiSGszdv1odgCvqHDVx7I27ddGjSVg54SUZF1tGRFoE4ZgB_peGHiQwz5up-ju7Kjv-2K7tPQ24eK-i6QoGLyoM2y7BmXNrScFFfOD_w0Kyhqjz4c9q2FddHLjSpwTh4HxfWctAJkwC5gqL0VLOKBH3jXSo3Yb8FIeW7z-XcU8P8Fm8pDJLjMUzo-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9vH4CMv-oEiQp8XTR8W3K94JFx_FL6O2EGd9uhS7v7PCPtT9KPeJZcc4f_JzYwim8HsEHhYXDRSXVeN97nkUtobtfkk0-u5AiDGtrR3VBn6CI8nDyriO1f-Qv7YytKWFVppjSWsjpkJzH9Vs9D-CWfPlutjcVYcRCBodulblvCgsH8nGnUo3Ao0vDiERuRrGIa5LYfLDVpM94rrUgCuUJTm29mR418HAFUCCZ5dsAnYM665jI-gJ6ud0ise7t7behGyCYRFnyBhPOs1G8PKStp6qZoDLt0U_LaVqRm1AfRnoAIaQ1Q-GM-t0Jp-5uZxr9UWixs0yF4mkXpL51i04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9ag0THhwKZgr3NHiGv5UmF1hoKEuAWATqhi_MUFwO-tTHJLk1C1bi89_Xu08udL7eWBIpR1VB2YNQ6ufpRth7w6i2_rG4qwRXstZn9_ua6l3aUlbbx-sRzb8X7S-xx5MAExaH83FNgiGamzDXWh9xRUYSQHrYf84UmPcP1blueATr2XCbK9KrZupLBKZrOVsaxByMQ56sIdsSAnfIcbaWcLZFJXutRvmo5gncqx7znhizfFueAvP6t_6gi-tKLQC2zo35WDYA9wThj2eWaixF5AX_0US3u2vuMGqGv4Xm7rEsnhDCYBx_L05cItfzNW8KB7yfA4Qd5PBC3XBqle_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R96bdvy_BTeTpUXDSgeT-nn9MAAw3a0Sywof2VOLv5tEUoaUSdz4QbbafeZyn6zZVZpm2Np0tNPN5uo6_wtbxRfdDQyk__LatYh1HMzjx-kA3U6V5FT6DlesXXMcpalc3c-nIrnJ90Oh76q1cEUrQo3xTyNS5c5ll3p-4vz2Jm--KnAnxs1khlxcbgSha2OjZLCfQO9agq_LPGgGv23Wb_D9bGIxJ84OOzcjEvBKbB8VuvdoUntBM71JfZfPlkkrLIB4F6ycF4tXhHDsYwn1BM2jv_BNjWrLkPxxzTvCn6pLg-opq5ObVo3iDSc8yLqrIuQXAsRU7NNH6jYAQ-uCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،
وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.
منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!
یعنی از زمان هخامنشینیان این بخش
یهودی نشین بود! و ربطی به اسرائیل به عنوان یک کشور جدید نداشت!
دولت اردن نه تنها همه یهودیان رو اخراج کرد
بلکه ۵۸ کنیسه یهودیان رو هم با گذاشتن مین
منفجر کرد! فقط و فقط «یک کنیسه» رو نابود نکرد
که البته غارتش کردن و فضای داخلی اش رو نابود کردن ولی دیوارهای ساختمان سالم ماند!
۲۰ سال بعدش چه اتفاقی افتاد؟؟</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUqLK-IDvAoJmzNuBW4Q6QrI0kZMoiSWkzRKNHJARYu7XfvY72jYZvrED417LISxkxp-IcdxZlb6NeaYOEqPM-wEvOkz9ypYY-e33fdBUOwSUjEG0KnWxMK4nzBsELLhGfiRFKe1k6nQ9KTyuBdtSkKi7MwoXH-4t1KkuIIccYXRY59cQdgpWL8IOOx7LieCgp3gtkYkUAomua6lb_0B26Wone1zUMEI4s6eVjt3D4ahdJOqSuFVX8FQCMpEm2WVH1UlI2Z7R5cPZr446QTgCXLoO9zM9clJdmWZWwFHEGReUry90jjenRuwr3rh7eouj3IzRI27YfCvvPZm8HU6-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx_gApqX3JDoa-l97vxKM-j0To7P9fSekeJvw_p0cqDKlTGI5Yb_CV9BerpOkOxfmOjYKzhW562-1h88fpgxHiptEt5aERcw9lmLc91pJicXl2Xy3KcPcdUtWhtm5T5qHkLYdhDr4FjDRRCeGex0blbON9Kn9NKIQULCBL19qXzhw712LDVMHU19aDAgJLnmc1ML4UgO45c4RI70fQK-kxsAyCkH5FgKTSAQuLdcQxTVNicbdPEFvIczThbTgicr1w5_UniSGiii9eoVtvGpGAITTI_LnrfdE_Twi4dDk3Nxjgpl5tFYdgEJEZNO9IoPvJd_VrNXHmvvxnkGUcrxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siit7ZKIh-Z6OXe6VqacKwqsnYRhscRNMDDh8RVY1G6zN9-i5RCKj_OEWtcJONdhrSjdkB1bPulLbLU_YEsnpkMWd1oE_uRjSKfw0xp8sol3PJMGynoh0NCSpQbz22RnQyCTGxs-rvm0QhiVC0dQkvTUBr-LX9-TO3YcfgpxLXrk7g8UhjoeaQqO5S2FUpzqsAene1g7oq2vkSvGM9or90yZGP-eCx_J5w_SBVpzI_OgNxb-BCDFm0aSDYqQVLyKShZbei9gM6Pv9aAagoiL-kNymDy8xIW_4UxdSiML1n8pk06ttJSE2MajlfAAtGDrxJpGdXOcxp1RKygdfAU_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHMleGEoQbpYkhe4hTARhNxt1fI3b__DGwNEQ5xiErNxtYHzDwHpwFmtC0PE3kBvotZ1dvFs3oObZhjk_wT-RNgZJpRaMiuduMLGlxPS1XLCrfXejWW1vJ79LdBrIRweLu0RdwJaNtredkyLJGybqjOaZzUJv99Fd1mJDLZ_2Yt9v8Hpt259R6I0JOCmD-MKN6S5tNS6vKOg-UvhqKR3O4HqImzvL73KXUCWpDzDnP11KPmJ8LrlOzmqOp4vcmY18G4U9uXgJJ6DFXt1EXYJ2NZdJDIdOXMsEMeKXrJxUKjdHv4m-4GkiCY3BWnSlNT0uvA_pBlA80aa-VK8votwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=dmkslnyoGXgSEVZwDilhmqJ-_LHc_ih8ZtIw_pTvlCiOsSZfowePXJfA3QZ7wqqVgInwL388WD9jlNXlrhWDBbotEbN-J4lgVefa8WqbcCRlZzFX2dH0C3chPUtmdeAbWv9-zDZbY5CbCAUU3zLayNesG6ihP68PYeHg5H3uTQ8R4Ct0ehvM_85uOdv1kboqrJHPaTb5KPf20Xf1rD2WBpQzAT4hzkg4tI0dv7X3NMPasOtO7ExBiWk6Ez30CsGwj8qM1O3i55Oopli_EhXXAB1_8ErJ4fGc4OT4UwO6GghwZNsGwKsjFRncjSEpyoso4DYbQxTk2O2Hqe5MZ8eroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=dmkslnyoGXgSEVZwDilhmqJ-_LHc_ih8ZtIw_pTvlCiOsSZfowePXJfA3QZ7wqqVgInwL388WD9jlNXlrhWDBbotEbN-J4lgVefa8WqbcCRlZzFX2dH0C3chPUtmdeAbWv9-zDZbY5CbCAUU3zLayNesG6ihP68PYeHg5H3uTQ8R4Ct0ehvM_85uOdv1kboqrJHPaTb5KPf20Xf1rD2WBpQzAT4hzkg4tI0dv7X3NMPasOtO7ExBiWk6Ez30CsGwj8qM1O3i55Oopli_EhXXAB1_8ErJ4fGc4OT4UwO6GghwZNsGwKsjFRncjSEpyoso4DYbQxTk2O2Hqe5MZ8eroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEKw_jifmL0Kft1DxCg89iheGRHVO5opGNaDbympYvNzZaozsv8fAbtMJ6UQ4126whpBKow7aCokwg_88aWrvl5dlAxM_YJMJdctcuI1pck2uqZcvxa9xhFjoVZrjSt1ZH3Q8zhepzxtGk_qKQ5BDHscTSZq56a9kbBZlcLh1yMzfWVB1a6ZXm6YhjdOuFMBrTccZ_43mDPjXKC3tWYduRHFapuz6OS2VbtYPPd0TqVO2XfpwUpgH55MW5-TDJv8rbR8JNindFNXpid1U4ULMsCpttJwhlHsNnjWH9IZobwUdy-nIUohKc0inoNSuirtLUkLRKeiu0dqFu1XhpqdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/co4x5_ow28c9rjAiwmkzwa6DbtqFN7GE8R9CfVWUmJm1FtUpmmtPCPOSM4yBTZtvaqSygZ_k0hVeUqeXM0LY-mEsR-aDEAdRkHi2AOCV7EDuF2DcVkHuGfFdn01xpElYZLIWNmIE6GBwufx_FB_Cb2tcf0_roxCAYPNEedS1eh1AXEuL4GHMsbdPbbGO_W4hDF-UdD0WPgWPs2T-5SAgYfF57wlt2qjRKS4MpaDVRaXyIvZyc9CBg06vPsixKHQhjQ6facOmBCxiPy3hO4zzb7vtnDoYINeIvux6q90SlJLGs2G1Vzvhu9Jf7L5ok2EMLleq_Rs1aPWOqKNJ_Dv59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rpF1lvm2Fz79cNhxGAAL_b939K1L7EiuZuDR4gso-S-4wo6h5gm-TzfIKSKcuiZSM6Kk510KxxMT4DNoYx3EnFDXgsx1pLsrn9NXBhL5WqcJK62Jl9t5W-g0yXrBJp3zYBI6nz1sV-Lu7jFsX6Ej8yoQqnE63F-VtyWB7YDaHmM3WbyFhSI8luTuN0a6_dF9G3QN2MmVrR1CuxKQNmydrfvAPItHE-oCLlr9ZNTG3l1Jbl6a-KfgGWFPFUh3nkLywUXHgVGBX3FcHjVek7NiSH0u87XxjqOOJXO6yxD45fIHLqNchizV2w0DzBRXH23z1P1_k0X03miZnCTLlLk7Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZODZuHdnpKJa4TULlGu5Z9jpIbntNPX2_t3eRfibWWec5ELJ50MNb3jshO86fE9TGQGcW76nJtrg4VTLl9t2dWdPTdpPvpkwcbeZttlV39F6XLpq57g69GMI7452rZ4LQdi3jXCcIe8RTaEt--RNZxtzc8KZTUlzSk6BoD4fYaoZI0G-m2uDeuo8bITyX8VfEqeNhwwOGu7NbUxAKxt18GLG9NdVUBvaRshAhcAbXOlHbKNb8k9APO3qTLfwFaHZoTv3VYOmMALGw5X2OyiZsKpMx9xh10xeGeAdvGZxCxoVEsMEqLS2rQi--bryY9NTFDyKIEE4DDSu32MmH0vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdqZjKu7s8_GQUI4nCWSydh2YPrmltbgPKR6YgiWYl7dA7pMmmQJ9B3ZSFBNTILC_NwJYJknUfLWm3pbxtzvps-gNzTfAoJ0ehT0ncV-_86b1vkEY7q_fNFkEvafKzjK0_cmRFT96gQmbdH6QDJ5ay8m_TjX4A51fXknozsKUvE1vlk7ag0kkSmWsQ3XL5oaBtZbByzxFHD0ZsjCuwx1IrWAj2cxKLTQvs39dp5AOcGJo9QubMia3n2YQt5_zL47qJFEPVlT-WsSgANpDC-y1ijuBDVsewLkAPh00WRPCpHIhNtys4LGx7NKgfvEmS9TtzghV1NoxzP3kybKAOubQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxG7lM80JrGKnyIRGyQUp6GhH6wXdFzlsPQN8TD1ixJsw8vVcwQABH-xTiXzhrhd7EpZHdojRDtRgNLyzp3T_9P_3zI8WIW7hPBh4ScMdjp1BXtPr1VuCgfN7V8ISCagts2o8ErBu7f6FdPl0qFi5KHUVOxxJvKP6WQ5fR5KCk7kohMfzlJHVXGTRmRJIEssaImU8OVZAJMANiN_vq6fbX5roxBULfR2oTb0g9iTmxx5nO5CRk3hvenA-A9QG-Pl8mZD2O7qTBj1rUpw8xKpo5_mI327COGahqVOw8sBZUR1HpkQPkyrhaC6EKgBu-HbOwjglFh6agvLU-8vr2SUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro3_kkFKVb0lKwxAbmCUrDiRmN9SmKZrU7XWP1upe0gwQXZRJ0g7bE09FOhChWRhiaH42fARNaLh7NJI0jE8l9EqMzacw-GhlFDCxhX08g-tOM3NQX2W1u9JHsqzPjp8qePHArszsh8SaTkqlECE4yosnsQaFi8FrvO_3C0Nlo7YJg-9wN2mcKcaKYW9t1jKm8uzyImJHsuJUZGOT6-BzYiDMMUfEdYudWa5uO_qwsiKvdfI_MjhhzxoeW-hVgVMFpE1soAsudr2YTnH9wluvH7z0NuTPCvas6avAc-x0X7eXRAtOlJoWgskMz0lLEzoR9Gr2hF7QQZqoAmQ43eDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9jaR7i4nNSIXw_aHKFoVZ0jO6JJbDOeDJ1a4LwBOOicCSlM027M79B--iXcDA-mxph1ahLaxmg3R1eRJWWITQSN7urZWyTzt3r1uQ_TvOAXmDw2_y15f0PKNgTnmarKa0V1yXqvYUHhWBR4y3gtfoczPzh3p4fgGSk9EDCCGitgZzl7kZ06lglQzKp9dGUs7QEMiczUBXdTX9dteR514MHZIVPLkZu00Agq19wVu6crzHVZ6ogRwvHgXRNfLr_jiCaswceRFe4LLDh57PZdfDZsS2qB98DfhVBSJD_AKkXTzIj6fGajELzWGahdT1zAACuSHh0T6yTSt_BJzBuKPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">و بعله! خامنه‌ای و پسرهاش
خیلی ساده زیست «بودن»!
فقط در زمان رهبری خامنه‌ای، برای خمینی مقبره‌ای ساخته شد که هیچ کدام
از اهرام فرعون‌های مصر،
حتی فرعون‌های مصر!
به این  هزینه و گرانبهایی ساخته نبودن و نیستن!
این فقط و فقط «یک قلم»! از ولخرجی
اینها از اموال ملت ایران بود!
در کشوری که هزاران مدرسه‌اش توالت نداره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=LMjk_s-mmI_DxiaQop9JVnmEtB2UqETtW4OWHnOsZLJn8yI5vKfWabwgrkE5H-clKVDsyrHTcWkwLES-wXqSt915m3X3VRITJdFEiPLrs6L_1G71UwM2EcuhUOgyiAOzpS0YApTeb2RdoquTnyr_frKmABy_FD3kjkWzRVoIiD8gv6lUximpVNajKH5YjiIW8iIDEI0EQMRtj0K99sZWcCLbjGuyXEK2iQuDZ-jvwJC3fK7jvcyqnZ0Qtl41xhT02Rx4IgzWxYbQrmfXXuZcmlgf0NebPTlDVeUz5mNnVg9KnGHp37uJsA_M_ucCoszyDJgO5dEakea7y1x6olDG4En5eF1eszYxenpcILwItuPjW3bIiVm6DDE3AJSdpfWAfEWcEApVnCEiIUqrve6zhFyZlc9V0KrXmXsVfRWt8sV3h21eidISQK__sthNQUPg-Z4FY-oBIvMroWIj0mT35Biqw4jV9EpnmdJiCEIofQXqUz-X7ugO-3cP8rtA8AFyDFovYRfKMy_KHweyuaahnIPBT6t8bFWs7BId--wG2mbF_nlw7J_coetXJM9d72fRsKdm26FLPgPI-wa7QDSKLFOSEwjBH9Px2M0HkQ1bDvByBnw1AYLt_jalhj3Pypn0v_Qrhd8pYTCMGLi9h_Uola_SZKKrXcWMJh0MsbSOo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=LMjk_s-mmI_DxiaQop9JVnmEtB2UqETtW4OWHnOsZLJn8yI5vKfWabwgrkE5H-clKVDsyrHTcWkwLES-wXqSt915m3X3VRITJdFEiPLrs6L_1G71UwM2EcuhUOgyiAOzpS0YApTeb2RdoquTnyr_frKmABy_FD3kjkWzRVoIiD8gv6lUximpVNajKH5YjiIW8iIDEI0EQMRtj0K99sZWcCLbjGuyXEK2iQuDZ-jvwJC3fK7jvcyqnZ0Qtl41xhT02Rx4IgzWxYbQrmfXXuZcmlgf0NebPTlDVeUz5mNnVg9KnGHp37uJsA_M_ucCoszyDJgO5dEakea7y1x6olDG4En5eF1eszYxenpcILwItuPjW3bIiVm6DDE3AJSdpfWAfEWcEApVnCEiIUqrve6zhFyZlc9V0KrXmXsVfRWt8sV3h21eidISQK__sthNQUPg-Z4FY-oBIvMroWIj0mT35Biqw4jV9EpnmdJiCEIofQXqUz-X7ugO-3cP8rtA8AFyDFovYRfKMy_KHweyuaahnIPBT6t8bFWs7BId--wG2mbF_nlw7J_coetXJM9d72fRsKdm26FLPgPI-wa7QDSKLFOSEwjBH9Px2M0HkQ1bDvByBnw1AYLt_jalhj3Pypn0v_Qrhd8pYTCMGLi9h_Uola_SZKKrXcWMJh0MsbSOo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=k0JMzTbOvtwZ2XP6NUIwfQ0R6w7FhtYzmDIb-XhlrTvhP7Uv4lxZt92U84WnqHiahBWwdidCB4GRXAxzzoIlm_t0ZcpPdT_xLqwR5JGDzuccWGBHiKSUfAqvFDULLLCQ7uMqFhFumLBuugNER_9pF7JBx_VvjYYCASONvXPzWvXN1mE2dGH9ZZh-wt9xxTNsxbwXXJDoK4lIhREqo5Fm38uqfiqvtQeqcP5eJZSivzjp56_JQOKWUyIpfw2G3WOvGoRPZ-PtNIMPN0G7P-Rsh8_O1oWkFZkqrbF-y2e4WjwhYn5H32_WtJaVp1xc5T1uvjL4WQVoLpcm740eE_vEfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=k0JMzTbOvtwZ2XP6NUIwfQ0R6w7FhtYzmDIb-XhlrTvhP7Uv4lxZt92U84WnqHiahBWwdidCB4GRXAxzzoIlm_t0ZcpPdT_xLqwR5JGDzuccWGBHiKSUfAqvFDULLLCQ7uMqFhFumLBuugNER_9pF7JBx_VvjYYCASONvXPzWvXN1mE2dGH9ZZh-wt9xxTNsxbwXXJDoK4lIhREqo5Fm38uqfiqvtQeqcP5eJZSivzjp56_JQOKWUyIpfw2G3WOvGoRPZ-PtNIMPN0G7P-Rsh8_O1oWkFZkqrbF-y2e4WjwhYn5H32_WtJaVp1xc5T1uvjL4WQVoLpcm740eE_vEfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMfiClMMOZKCn0pjWsmWqDrvkUhJulJl__Lk1Fx-cqDZQnaIKNav3k28XtN0_REyq5nohvd9hNU0qEvXQSolHeFLDmFfypS17lsYvlxSuzBfhIaBQNoJNMIOM9jfDnmRVAswc8-qls1MGqt-11ueCn_9wh_Y4Gym-InVblnRtu8mJkf113QMDMHliGdPfbwWXn0_4z0iHMYT8YRtsiL1NjzrMl-jB3jFdtsAklxobtz27KAlT8Bv3KfZFeTl6ghTmu05II9Tc8sf7G6EaXM3gXsp94KzaZ4S24RAZnmJcBJhyg2zin5I_-ksEqRYBiBHaL2eRZTAP788-qM3HXlpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف گفته که اگر حملات اسرائیل
به لبنان ادامه پیدا کنه، در مقابل
اسرائیل خواهند ایستاد
‌ و «زنده باد دفاع از سرزمین مادری»!!
میخوان وارد جنگ بشن
برای دفاع از سرزمین مادری!
حزب‌الله برای چی وارد جنگ با اسرائیل شد؟
برای خونخواهی خامنه‌ای! که
هیچ ربطی به لبنان و سرزمین لبنان نداشت!
اینها فقط برای فرقه خودشون میجنگن!
نه ایران و نه لبنان!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیانیه سفارت لبنان در واشنگتن در خصوص توافق
بر
سر
آتش‌بس
متقابل
:
حزب‌الله با پیشنهاد آمریکا برای توقف متقابل حملات موافقت کرده است؛ به این صورت که حملات اسرائیل به ضاحیه بیروت متوقف شود و در مقابل، حزب‌الله نیز حمله‌ای علیه اسرائیل انجام ندهد.
اسرائیل به ضاحیه در بیروت حمله نکنه
حزب‌الله به اسرائیل!
یعنی : اسرائیل می‌تونه به حملاتش در جنوب لبنان ادامه بده، اما حزب‌الله نمی‌تونه به اسرائیل حمله کنه !</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ :
«من تماس بسیار سازنده‌ای با نتانیاهو داشتم.  هیچ نیروی نظامی به بیروت اعزام نخواهد شد و تمام نیروهایی که در راه بودند، همین حالا بازگردانده شده‌اند. همچنین، از طریق نمایندگان عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمام تیراندازی‌ها متوقف شود؛ یعنی نه اسرائیل به آن‌ها حمله خواهد کرد و نه آن‌ها به اسرائیل حمله می‌کنند.»
🔺
ادعاهای ترامپ شبیه برخی ادعاهاش در خصوص ایرانه.
اساسا اسرائیل قصدی برای ارسال نیرو به بیروت نداشت! بلکه نیروهاش در جنوب لبنان هستن!
🔺
دوم : بر اساس قرارداد آتش‌بس اسرائیل قرار بود که به بیروت حمله نکنه! ولی داره حمله میکنه
و در نوشته ترامپ هم اشاره نشده
به حملات هوایی اسرائیل به بیروت!
گفته : نیروی زمینی به سمت بیروت نره و برگشت کرده و…!
گویی ترامپ دست اسرائیل رو باز کرده که به‌ حملات هوایی‌اش به بیروت ادامه بده و به پیشروی‌اش در جنوب لبنان ادامه بده.
همزمان گفته بله من مانع شدن‌ نیروی زمینی ارتش اسرائیل به بیروت بره!
🔺
سوم:  ترامپ گفته با نماینده های حزب‌الله در تماس بوده و… عجیبه! بعیده!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5245" target="_blank">📅 21:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3zsSy9VZzoji2-eNxMetsD2jONnJlDxY2EfEFzQjgy3lVKqQzdcCE1hbl3WSk4qYkKjC6t9EJxCdKlP4fjlRsE1udFMedttGTZ7PCe5Q9la2__4EcO8THWKidQquREYiWtWBvBV0eOUbygpKbk-JdHcgA02qWAt7dBHgpXz4eveSy5AumnTiHFfnxNYlc2dGiVqw1JGyR2ndtfpJCudWj6O7UNVxIUkK_X7Je-zjT3Ub0HVn0Vfkrl5T-A-rqwsZsGhe96nIdKUvAsqlDHFoWrBWh5SfWTaLhd-PTJASOSxLaB0NbGBRVmwiBCdsDnJpp6qqV8r7SQ44yl5Km8rYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWTl8ofKx6IR8mMuEzRGdAP92OfsB-qwVedLLJTX1Cpygk2vEDgg5gSYVshkyWTu54DcGZu18dP36VN1M3x4YOH5OZuqK6uIWaeGMKO6gF9aM6NtPLUqZwAzexat1TowifxRx2iEyE6y90mEweHEZUQaFPMn_CrG_6gwVgqqk0rE1Lb8oCoFhIyvd5rBvw7BIodTQizhdnsh5V7ZWx6u-UmT2oSPDj_S300c3UmePXoLbh1Wxm3ylHNt8kPDyuynx0f4ZP8W0K7mAfAT5i4TH_BYATphk97xAly20CEd4qLykG0NuVZcWotsWwn4UuyjQOHgxYF3O8lrX-wV4P3PkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnWZzRXMDD8kds_kJh937vOhXuYJcXrgJyzxYZ5m6CN42N1FNoSQFKewI-0gFHBHKQlm1DXP9MRyeTGNSfvwrPt7ILpyV7yH-GDoSPHB9hMaU_gJbkZt6lSefMIn3dbWv96q2Y40RV-2GxUh99AUR981FHIoA3lhU-YvWc8TcIW-H5EMv_6QsJztsph9NVAsfrznL8FRgk69Mr4wmXMXhO6s6W2orkcbNjKvX6c0KSq6oZ7NdshKGx_6hkH6fMaVsDr75ZSF4R8HLlAoR-50Tnyt68jGsAZskK_Ple7Xjb6Jn9_R5Yfk8I4frhs6vOvcjRBRtkaxHFU_beUhcote9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC7H9LpehZYFCIQnpCb-IfD-PO0w0CD8el2sBDV87KFlnkp7-sC-rU58lwHHpE6Sh-qRDLU8-WqHenqBlWQomOTkG03KzLOWNOBFmAIWDCGV35Grp38c43Y9fxi2fGzzyzF5KP54_kbdQzQAB7iPrnfRmHQrfzWjRH0L61SgIRAqfEdDj4yyB14dApNtXxN81kijW9ILSG0l5OQwchg9Z2RXjNEe2pmqxYRrv3DTAO5VMTA_hSduFwKb8aLMy29Nv1s1cUuhA5eh7CRD4Yr0lsuUsjoHEct4Pufvc-05wnVAYS_8ZlRSaLwBgG9QClWrZrebbnhCQtAAHuetjqxP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPrjvGnGrdU0ryiJZTzs6yP-q6ml2OhwzIFpb4zzN7kA8wWX50zvDY9zwna9ysJAfOk7Xk21HX5V-In8ZT9RBc6RAJaW8R02f4AJtbGvYacQ9XY-PABIFsLxudqm4PqG-IqrwMToKuz7nVEMNutycximEhL-aiIg5absNWDwDhgDvhBiGJF60yDrmfxHEWLx-6humOeWcaMVcYbNrZMnkMBJijvW7exxWZ8qBgTJt1aom7kAbWeCYskhUHWAE2TcpI_iz-7eiK3kVSpGm62ShHkR2ZLu9S9QZXn-xFGT9YwYX5pToJwcM20FLKug1Mk2Ln3RLcuryya4CyOf_hr_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J65OmKJaPQDVLyiPdClVO0MEtvtdouMSQMrF_7SftkF8jaOeaz67Qxx-ivziqJ5zCQgWkk7goT-jZRdK5aTIf1uWz-UeC4xbc5KILErwAHe1-NnJaeozqqqHvbGjn8LukeKa5pYQIEtD25DZpOUnjv7PJ5rSAF95giz02VWK_p_DEXAN1GDSI_es8E3Buw_PAQZ-5b31HxDyRDHacXbSMJ233M_IqwDoQKSApe5mwbaPgYtaloEbmB-eNkaKW3PBcGMEhiYEftu2MDdU6vEiX16fD23lf5I-efIzfX-6hYhF34QBffpsVrva71D0UJPt-h6VbYfr78dkLRjJ88SCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgXIr6A_iB2mhq8OXEdQvtn31aE4EiJ6ONoVTBZKEr6m6951qsq82eLAKAEKsXZF-2TyrVOPTVrQL1vzZEN3l6vCEr65trpHnwT8GC6cvEeF6kau8ldL39F0myBPofdzz_AdeoDi1Z-7o9yg4HogiEIbSqKejEpzOO94BGQBmKH2beq9bh7b7g7KJhJNScbGhtLHdanY5KLoXu_OybVK2D2Wp9xhCeNHDxhPZwhvxDPEq7_VT4rdZrhyjrf65WFB8ImOCnQcBpHp8dd0K3RmupU6x9ZIBw0eyP1sigzz1tj4kPVoNtHrozQoZKew06E6ru6XBGuQAInKmO1r40za7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H761O9npRF0bxE3educArUwFkc-JZGWvKABYN-kvnEBZ9rQC69YRCiSH9oz7liX-iyKaOlx3-dDUkGJM6TNJyOej3jSOmgEhVNFDWz0HrEHvoC1VuOL9sizkytvMkMxwUukf1q_jGshykEHuJA6vJxUiRIOrfpdvaIMAi21CDlHgY_CDWRJL71AJwtQNf2dk0PL3DmyFxAVwktH0GxHKf6sLR-hsPKqYapJzl4pXlyS0zdBeE0CK9Ti_CTqN5wiCngIQlDq6R0dueWD2NNrqsGROaiWmcLU6z_nj_4RmI4HQBqh6svGL_88uzpw9f2cEOG8w6vPuXQmLXS1num17Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=VRPu5Gty2FQBGRb9pG6xkSpvlEMltQ7pQexiLxunOFbWuQO8zjM35XtJVnJTYoxIGF2FWsD7OTc4Y9EV7M2qByYzW0KE6q7-f6YqSCMi-eZpr2LHqX4EYbNDDY-c_bHL9RA3ktW1cTPy8Ht_LpiMZLQIQs3KXkNfvmIHJDsPN9NNfNBbzfssD508wWwiORggk1YiuOXUXMG2x9fRGfK-jWzyFynF2VtBMyEx3Gm6ZZVfFFcfqi4y8VNBCXNTBU9rMuA7tBRL8xJL7UNHoVyXtF1-VBPh5p6CSrXXQs9WCPaBsj-n3VHzbOVdUw7J-P_ROIfG9zNv3dEnRLhFHXd5Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=VRPu5Gty2FQBGRb9pG6xkSpvlEMltQ7pQexiLxunOFbWuQO8zjM35XtJVnJTYoxIGF2FWsD7OTc4Y9EV7M2qByYzW0KE6q7-f6YqSCMi-eZpr2LHqX4EYbNDDY-c_bHL9RA3ktW1cTPy8Ht_LpiMZLQIQs3KXkNfvmIHJDsPN9NNfNBbzfssD508wWwiORggk1YiuOXUXMG2x9fRGfK-jWzyFynF2VtBMyEx3Gm6ZZVfFFcfqi4y8VNBCXNTBU9rMuA7tBRL8xJL7UNHoVyXtF1-VBPh5p6CSrXXQs9WCPaBsj-n3VHzbOVdUw7J-P_ROIfG9zNv3dEnRLhFHXd5Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHDCtrYGlcfKtg8jmLGXTCvhuqXy6hYwKImucHaMjOWyZ6LDhsvqbLYWY25Gu4Ys1nKGYdonS-oTRNFWsmXDkz-KNkKXZu511Cce8E75MUtRZneBWewVKfwFPrXDODnOSYh893Oo9-wTr8mtU4fbrh66lk-mHFqOs-mGRRvHEijdqZ7J_kODvuJksv6Rd9CnB9ZEXvl-OJBYlyK6WK0n1KazfX4X6KlKfFnp6d4P6hz7p8E2YEJRxZZoAQ2ShO1gshd5sKcsHH6XCsnzFVh4C6jGuLqmRZllCyDRYQFKynUkFyrg89gN29KdHJWfie-ki3Vf9o5kx1Xt8coGk8EBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=hmbbIx5qCNo257zV-ps-BFhHcsMIN2UmdTsCjhddmnNf3zDXfaXHt-2irEUszriGwhW5PY-eo8vhdiSxkSoQrcqyiAW3V_a37xdjBkWAbD_z_JcWIZxtVwsDUmzia0YvjiUbDGMPVVFaojYpzIAKSndAQ8BKx8_Qe_d9bK-PhAyQcWwQ82tFpId9s5oENrLzJPICffJmMg2uacn4E8XyxAJVNcnkOvXDM8XdROtiWpPrPVBfjL76wMWvZc_xTKEX9y71JH08ActVpaCFsVRcnII_DMq8zjHPQve0wkgZkk3XCONF0vOwYPssyStg7oMFHWxAVNOpNdMvTtTWtVNYzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=hmbbIx5qCNo257zV-ps-BFhHcsMIN2UmdTsCjhddmnNf3zDXfaXHt-2irEUszriGwhW5PY-eo8vhdiSxkSoQrcqyiAW3V_a37xdjBkWAbD_z_JcWIZxtVwsDUmzia0YvjiUbDGMPVVFaojYpzIAKSndAQ8BKx8_Qe_d9bK-PhAyQcWwQ82tFpId9s5oENrLzJPICffJmMg2uacn4E8XyxAJVNcnkOvXDM8XdROtiWpPrPVBfjL76wMWvZc_xTKEX9y71JH08ActVpaCFsVRcnII_DMq8zjHPQve0wkgZkk3XCONF0vOwYPssyStg7oMFHWxAVNOpNdMvTtTWtVNYzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=fEqjMMUBNciAi5CUnbwg4CkSGreF3-zG-hCukY0fqtHKj_GL_m1gkTANfdzzS0OPatgtsYlt0p6UKKcnLpkFpgfPCWE3jDTerfIx_5Tn9WxpoQ_5xttzRbm2s7uPI_Yj2NaTKEtbrro9KD27AcVvV2Pf3Jr73auM9WJtZQZZER5iGWMqiFZ09Dm9da6XrcH1lQPyloGf-Erb8XNe5ztHfBqNZ51dvQLIB450uZ0xlLDOA5mH1Li9eGvObHlmz3aYZzy2NfcIh6DGKGZRC2sYEvOfMz5avER5KJEshxS1Wi99Fd9tfyFQtlDOPdKBcoqLkupMFMQCxWgh8jUGLp7smQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=fEqjMMUBNciAi5CUnbwg4CkSGreF3-zG-hCukY0fqtHKj_GL_m1gkTANfdzzS0OPatgtsYlt0p6UKKcnLpkFpgfPCWE3jDTerfIx_5Tn9WxpoQ_5xttzRbm2s7uPI_Yj2NaTKEtbrro9KD27AcVvV2Pf3Jr73auM9WJtZQZZER5iGWMqiFZ09Dm9da6XrcH1lQPyloGf-Erb8XNe5ztHfBqNZ51dvQLIB450uZ0xlLDOA5mH1Li9eGvObHlmz3aYZzy2NfcIh6DGKGZRC2sYEvOfMz5avER5KJEshxS1Wi99Fd9tfyFQtlDOPdKBcoqLkupMFMQCxWgh8jUGLp7smQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E65qL1Pj1lXxGQrvI_Pcyj4mBvpRhoQ2X-rT-Hb46nV0YVu3v1iJoTTBDPbxv_WimQnoRaIoyRW3OF7Gfm1q9c5htjm8PZJLhK-YwbP2Zvz4AZpC_k84v4pKjxAfkd4R6dho17twYiBD1ak533BZtyAyEdL8fVctnlWHJmh1K5DrGor-eadUrQ_fOWOfOzrP6muoPY0GMkND4Lr0T-EV7EF3M3GOcu1GzkVM41-JGaUn03sgcX95GSXBgc9VjJjBzE8AGxIh0tYmRgtcZu4qiVQ1YLBVDeZJ2aOxnWxxuUDFOfZgagZyJw193u0Dzui__z5v2AQEOgLE2gyjVfuClw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما
از دولت لبنان خواسته بودن
که برای آتش‌بس، مذاکره نکنه و…..!
به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره
(که بعد بگن دیدید، همون کشوری که به ما پول و اسلحه و….. میده، آتش‌بس رو هم آورد؟)
ولی الان می‌بینن جمهوری اسلامی توان چنین کاری رو نداره!
ترامپ اساسا داره لفتش میده و سرزمین‌های تحت کنترل حزب‌الله هم داره می‌افته دست اسرائیل پ یک میلیون نفرشون هم آواره شدن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5227" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=vC0nbHtdAg4SitU95Drb5sKdVOlMPv7FjntFRXWaOLKA0adyItg8o3Nubi7FFWNg8e2aothBRuDvylW9sJnSakpLUxjpXOIH_YOXjitXCmANHQorS40c9ykpG98nPxC3KbsfUw3CfFOPzdZyyTpckK__rzE3TUUMtc82gLhGgbVujxggohxXSb0TQA-3EgZoWnbuXrnBy1lzxlxoBbVExwyg_ahWQhbBCStuoBo3lk_8j2ugyQdEMnt-ITdU6d0mm5Poes0jPdcmYUmeTv2OTy5iULw8pbBVCfq_0kr6c4aANDkkt8vCnDjmZpoLXuHtkbb6vz93SzVWOug1n2A22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=vC0nbHtdAg4SitU95Drb5sKdVOlMPv7FjntFRXWaOLKA0adyItg8o3Nubi7FFWNg8e2aothBRuDvylW9sJnSakpLUxjpXOIH_YOXjitXCmANHQorS40c9ykpG98nPxC3KbsfUw3CfFOPzdZyyTpckK__rzE3TUUMtc82gLhGgbVujxggohxXSb0TQA-3EgZoWnbuXrnBy1lzxlxoBbVExwyg_ahWQhbBCStuoBo3lk_8j2ugyQdEMnt-ITdU6d0mm5Poes0jPdcmYUmeTv2OTy5iULw8pbBVCfq_0kr6c4aANDkkt8vCnDjmZpoLXuHtkbb6vz93SzVWOug1n2A22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.
به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.،
مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!
یا شهر‌ نجف!
برخی از شهرها را اساسا به صورت شهرهای پادگانی عربی در وسط مناطق فارسی زبان و ایرانی ساختند،
پادگان شهرهایی چون : بصره و کوفه!
در قم اینقدر عرب ساکن کردند (از قبایل یمنی اشعری و از کوفه)  که برای چند قرن یک شهر با هویت عربی بود!
اصفهان اغلب یهودی بودند، یک شهر تجاری، عربها حتی بهش میگفتن دارالیهود
عربها شهر «جی» رو کنارش ساختند و اعراب رو ساکن اون کردن. تا نیمی از منطقه شهری اصفهان عرب باشه.
نیمی از قزوین، محلات عربی بود.
این حجم از استقرار قبایل عرب در قم، مرو، قزوین، اصفهان و… اغلب به خاطر قیام مردم در این شهرها علیه حکومت عربها و مسلمین بود. قیام های قم بسیار معروفه، اما اینقدر عرب ساکن قم کردند. که شهر برای قرن‌ها هویت عربی گرفت!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5225" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9sTscANY3poNsun0uSRmipKgg3HxUGpEPRfvz5VMe6FCCZFw_jnJ1bypJjyvLuwRZFMB1PSBGTrxowFM1sbNOzS2vjndBsK3lnCztJoSk6Dv52Wdf7Jszm9RXaZx_qleSfbPnk3ey9N8R4u4NNl6ljXpUNSxBz8J71W_feT45_pKs4lQJNvctPR1SEhWBMxIOoFt2RV7x2jtqw17VbgEB0yQ953ZFQnYbac8iQQXo7B4gra_Kvh1hywXPE4LtvR7-373XUx_-JeyWLllPPOySG7iFzR7ItAzLi5TEPS7kn_81c8riJfGyPjlSVg2lJpXfcGKkGoQocc8847xBovOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
