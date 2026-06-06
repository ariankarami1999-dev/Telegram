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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
<hr>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPyLKqC2Ab8FwvxcoFYjY2oFfSKAUwkj9D8tyFgarLb6TIsKRE4WMVddSDEp15xwSLMZJNViL-StMs1EO-s2RqN9jYc1L00suXz_KWtIGNsLZcfe03kSP8qQwUdHoYeiapXvPImTB2ownfO3gidRSHxDS5TnQPvpj9v1KWTNRra7deoGLGjfGTWwMSBwUybvPCO7u9AjX40-1uDBxJW1VpxdWisznZZXGvT3jTg2dfH7YQTLilMvasvSeSEj-mtTBt-RaMM1h7FrAaJnmULfj0BG7g2-nETFkGxOLcPvNvJXmaA6tXvWnKC9vH4Z1m5cqp9weB62CJAp-Ru1nLt8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3U90zV_bA9BbOnca6Qm9r9tfpK8CuQ9E6ZfjBvFNbdzGYtF559tvYZIvgODN5UeM0lwK4RfPQg3eKz4zjasuAYQ0m6CmGqtWDjyAZATYYBhuYPMs5Am5w4EjKyu9O6uzGoyWJO6Riv0kQd7aPEyWoFgREsg9WGoeM-mWJ4mcp2h90Z_0MhDCEzHMLUsqYn9nOruQ2t2QCgWbPqIyNY1VCWjvqQqSbuY3jNM7yOHskubRkFS-ZLlbRTrFmXgyNci_bhN39pWeIJ8j2BxjbexIyckXvpCJnwfYHqx-FvE8yvgqUK-1KmRfpRkX7hW75nzla8ecncrMwBQUswV0jJ2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L64VijQjG8pYE3raY3iuxVkV6-1zq3bglPgHVQP50WAkVunbPJyyR3AQqxvSVX1LlDGfUboe_vfpVxZ7c5pBEUd7jdi5yum3Kdy-47EFH4Nl7PRvucPA2i6zqx16agoTcxVdukSRwIjTtGmrnUvu4HZMoX72HfU0UI_4QWy2pxWP6WrBN2cciZ3toBwnzdN5ywegKHQ_FRnNgXMnARo7mfw1m2JqfhkGBEyWOHFzk5nG6QJSsgyJJg7_fDvJkVGZLGukObfNeIkce5oFW3yKakqW-cD7wy43RC3cIJZpYRNT5tFP3zyE9-GS9oBzzQQBUvdpUX9SMzkeipqMJ-Dy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfOG8r9Le797iCT_r1O-6F2tl1IKrJXs0hhcDjwGlX56-Y1VSZjX9DosHSHHmxdD-7WTb2uN5qBfL5GHqSI6RY62CuJAxxTW3WOtrHiOF69Ni6RfArcbx5TD3O9uEWXwsxB2qnvw5lCEJZnqje-nZXdG4YdkYzcaJ3GxibPUFM4LKxQb_b7TZP8xzIR8zeCuL5oY3GhlH6R41k8QBJm3NTYGV2RzgNtpeDmVdzNFO5ODUZ_XdDwc5sxN4ma5TjG4M6Nr9rXx596qMmqnNNdc2RGXTN4HnxHvJQA5_Lun6ez4FZyYfadpFbg5jkH4gyaZkTDqSlLeU0-DreGOFmjkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAkGBrR1Wrrs-8F7EOCnSK_eDHa6IPFemHwWozUNCnPROiCVN-F8kBITQ7eLiAPkAAfll-kqLgM28jHZwsQgngLvKKZG09AZ1kDljgbZomBYyJ3mfBLYbyIC4i_HjjfddbYOpjBEpdPU1BeVm6L2EBr5rYE9XJZ4vCiF6TBFm66zyRGaADSGmvQxR5xKhgS1E09Mbn1JT8CTFqYWxwfL_k_lSuj7CTpMFQ6IWzb3KF3SiYj0mzy4dE54EyFqY4eQT3K2j3eywYWAil30i22CjyyFd9EXoaYjsgi_R3OSWg5wmDdfi3GIfaIyxvcrt3K1ocMCHQEn8rmOOFUfRTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmwMFkzu-ZSmk4eQ_q-FTjcm_glsTaNlNPRSYlPCaUUtLBoF-IJNKGp-sf9FSOOLsouKFU2vPEaVYvIHAib3LtzaB6oLQ-xflSapqtdiZHKsTXbq3t16E3w1E5HvYVht0HNiqo60uzyaU0DoIENCWeBCgkrrHPYFEfveTAA_R40XOt9soH3y5p6l51eA4F0NGm8CGY0_hkyovYL8kWT4Q3dn7-NH6zhCpeQoJi19eReZ3FeFFjaDmgcgFzHR5KxMxV4fBwXJVgKtBJjxC7spXNbI-rA65CRFyUztQjP1gGPNETDswlbtsAiQcvhzqWGN85zRZAhg7xAefurpXCIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhU5XtQ_pW7Z6NcRCgmAzfn4lYcV7Y_t69KoYpjSs-njPKvPInfx1yeY_pl94FE_f14KnHWcYJxK9bxOPrJ7HnJawtmSE_KvEzixaJrlvwN7vJZ35aeWE3VUROG47UgwaINKjb10xX5cA9YEFkdZWRXxfcPbS3YXjK3vMDAb0JeCaAAsuXyxIsCtl3W-NeCf9l1aFFXHH1EoTNP6PI5vWfq4iiPqyTyDCNbrnaMy1JD6EhzpjocxQvJRgjtoJczTE7t932Oyfh-mXlL7X24faLOR1oUkDk-jLpObZ-NElcZAywb-i_Ii-V8S5N9QNtv_wh3IPgSt8sRlY8iTF64goA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=qF1yBQumuAORZNRNWgE2zn_0ozJLzhwRYGlRBnxthSVr44BoQfoAsgMS9Rvc84LlW1t7PvCZGxebE-_YumnE5tf9sonp-wUDT4Ri6aJsyvWhnks1PG91w1XDoa9ojMyFBAyuIJ5M5oAVPxwKkTbdq9vYpIvWsXo7OIIgphxkge9v88dFmNTOwYKBXOuTp-0rOhxA9ZEYU5MYl7rCZXx3RUBX28Wl5YqtCJMkraEb4f1G7YtBbOyK4o5gP0zPXgcLZ8WPPb7WccRHBH3EkR5_spsNlPuojgtIl0RmBQbNahgfRM4qaZBqwrzWqJGifEvF5hzTzIw1X-nc6upY8KCp7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=qF1yBQumuAORZNRNWgE2zn_0ozJLzhwRYGlRBnxthSVr44BoQfoAsgMS9Rvc84LlW1t7PvCZGxebE-_YumnE5tf9sonp-wUDT4Ri6aJsyvWhnks1PG91w1XDoa9ojMyFBAyuIJ5M5oAVPxwKkTbdq9vYpIvWsXo7OIIgphxkge9v88dFmNTOwYKBXOuTp-0rOhxA9ZEYU5MYl7rCZXx3RUBX28Wl5YqtCJMkraEb4f1G7YtBbOyK4o5gP0zPXgcLZ8WPPb7WccRHBH3EkR5_spsNlPuojgtIl0RmBQbNahgfRM4qaZBqwrzWqJGifEvF5hzTzIw1X-nc6upY8KCp7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=vnkj7BfGFNzcZjekGMVqdYazNS2kXfIaAg8Gh6Ik0JuDm3Aahb222x45Q4nxfdwxceosSJT_TdYwLtBqzVf4Smx5I9AkZbQwDRHXQzoydlZTvRYX-7gEwLeW1vhhHYPp0Ywymkn8fMDOAkU3AewdfEB-Q4s0Y0sEdGdjfAXAsw53fbx5_uSjtWTL5OsBN2N0cfqXpsdHe-eZFFfv1TFFBBolDPWxLL-QjFfHs2juSSmlpApi5YNoKdYolDwnZA7VfgV66RrWZkxgm1wDylSPbRO9qON2i-QkGGpKNmKgxBNqTPTX13ZNlGN3Rfg8C-8O7si8gW5Ms0v5f7YDgpGVpzZDN_6RPY1bNUpkmMqFT3zJr0kFC0Cmakfs0Rs393Phhzp9BFOls_FXGu0ydr6jvovO8Kn1NMCAIxjye_JuNLFmmYlK95VC2M8bTtZaH-iwFvtkHQ_0brFdUDsPjRxwEiR5GmZ2UVQljYtHMWSFbkUhjlOMSmj_3qls02HWlvOd6ELCzHMW6at10z2lJmi6q00u7UHNd2n8KixErTQ0LAhmNCrfEYRvY1kDeCElEIKl8botxNonftyEBoM-piaXOF3n-skJOF-m0coyU-7Jl2eNzpIof_7uUB99CBOR1nI-KTKSV98bV48sINGU1Mow137YxNsid3cI3elG70W4Pwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=vnkj7BfGFNzcZjekGMVqdYazNS2kXfIaAg8Gh6Ik0JuDm3Aahb222x45Q4nxfdwxceosSJT_TdYwLtBqzVf4Smx5I9AkZbQwDRHXQzoydlZTvRYX-7gEwLeW1vhhHYPp0Ywymkn8fMDOAkU3AewdfEB-Q4s0Y0sEdGdjfAXAsw53fbx5_uSjtWTL5OsBN2N0cfqXpsdHe-eZFFfv1TFFBBolDPWxLL-QjFfHs2juSSmlpApi5YNoKdYolDwnZA7VfgV66RrWZkxgm1wDylSPbRO9qON2i-QkGGpKNmKgxBNqTPTX13ZNlGN3Rfg8C-8O7si8gW5Ms0v5f7YDgpGVpzZDN_6RPY1bNUpkmMqFT3zJr0kFC0Cmakfs0Rs393Phhzp9BFOls_FXGu0ydr6jvovO8Kn1NMCAIxjye_JuNLFmmYlK95VC2M8bTtZaH-iwFvtkHQ_0brFdUDsPjRxwEiR5GmZ2UVQljYtHMWSFbkUhjlOMSmj_3qls02HWlvOd6ELCzHMW6at10z2lJmi6q00u7UHNd2n8KixErTQ0LAhmNCrfEYRvY1kDeCElEIKl8botxNonftyEBoM-piaXOF3n-skJOF-m0coyU-7Jl2eNzpIof_7uUB99CBOR1nI-KTKSV98bV48sINGU1Mow137YxNsid3cI3elG70W4Pwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI34hXCaz8kDSH-_0EvgPx0F0sbsrZhM_Sosi5e2vYJ4ZDkZ29akEjhnwt2T1DAWDR962Qz2GjtzcHhoiA_EpG1AG_Xn4xrpfygZGXrzBFTmDgNDQCEbZ5wXC4_Mj8ahHUA90IjtM9ZhCp2D3duuJoknSNzWSdRG-fSkP27QVNOYgcPDo0MJgvFfGrbERIQET7YTBv6rPZM_utSoUO1duL7YZNIZU4WoG7r8sqWa0BydWJDR_CHGpCjyA9KDoUYpSkkXYWk7bUr9y9oauynHv2nLedKu_A9gVXEW2aBpOxUl4Kv6luQy5cu0lKVtEbj8bxF5GENQMKiMbdbo_DpyIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQDMNl8J2FmZ0i5D2zzVS8yfJ7nf1lAGU5MqGNgFr6tVrWtqZl5a1f3hp_A9O-kLk6K9TaeKQvSvts_NxHa0LNkocK8CFrdMRdzICbireHrOh082WHbXwN8pqAUBsrI5-fS_Qkehc1wQlcUIeXwyLQKi_zdI_cEYNTTG7I1K3AGkWqz7Z13y5xNvT5Ps_BpqaA6eYtL8IhIwXeXG9HCKG8kdgylJd9A236EiFfBOnNMbyfp4VwNGJHRd6TDribMLu0Ur2Vtga7hOCce9gjQrrxzyk6diYnWd1mymHj3KtHoXLCyNLXn6H3yKIO167f66p7iuq0jikENztFvPMEn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5fIwGIzWEazAp95LcnwDRFK-wjtmj4l3k55r7uQQbaDjbn1tMTB0h4Bb53JWIJEEkS-CDuualiYxOoLEayAQvGHVF_R56ZgGJWDWkRgZtBTMUt2vh5DxMAXhyYHEFvXtYXglQYMattI0J74-Jv-Kk9-mt2SXvSS1ZrEkVzDuotWoS3pp26cM5QHBVvycwhMfhDlD6BueE1EN3OmfMBLhSvrCq7-IeSffb_X28ZXSe2KEpvWw5El6Ojts6gnpXNR7_QzurTDwlsG_QYIv_3qeYIA-QcjBiGkT11RKBWYKI1Ku9suoY3K65wEN6_biW_YyWBVbsK2s11iPF-mPNwJvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_U9xkLeiHppY4y6Wus4HAVQcbmdy-D-5vZ8dKiLE4n5aLfcplqIFiDbA-Me5EdyGxxs7lLYU34LBC394Nyg25sLMmoGPOMWFxShId9kkv_fh-B7h-YOYaRcjQF2aMZpgUIwQKECmalayGwuiBzkUNEXWYg9DATty4dxyVFz4Ua-u7dB3cR7DJuGwKkk9PS4aeA7GQHkbTFZAGqiq9iaqQT1Z04s56evgWihFLiBa21BPtUCGT71B_R3KxUIzuk5t2DCZ52HMN39rR2bTJKhA8pkA1ooLA6lqC6oSrVpzv40L5ul7jThPrnkDElmihStGYRkekgqNIGf_lRED2_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO02MrPPdB0jtUZGDvdZFcSEHrTkF5fi-d-lCVh2_xAU-DPjyo-f6_-FRzFWa_V2rDN_7StotphG1RSCzYH3oxNdfNK48V58kf3sHNbYl5wEbJjEEMNkQnGuQW2uUhBlsUsrCxY4v3YATosPTOOi0iYzsvovM97eq5WFNlojNPzpCOz0i-qstmr3kcvOWi1BEQPCdfsKjREi9JUSyag5Urcc5Pd_Oq6HIEfubjnJYVZeFdzg4RlKe0EQW98dMCjLt4ax2s4A0m3CYEIfe73yCj5eMlcaQO70BLMjfTcNpC5zKgwWKXJ27fV5nKgUL0a3_nLLVOeVnGi9kFtx9861jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1xC2V_tu8V6H-z0fz5Eu12Aez2ZJKHao9B1UEXxduTXdQstccsnn2vJYJ7nply8XE0Az3IByRf5f5-tUE4gdUgnT_5uLQ_H-WnNbyPYMBxT0tL1zXOasoIrn3lVbKd94eAd3Ewqaf_-ERP7no-EBauC6zqp_MFgPkGSLIg8WbUqxlDzaU9mMEt8zfDF1CPKeL3NZVuQPSRlexKbxVtXdH3vawur-dSXbGoTARoup-roKjWV6-cHr7rBDY7w58V3JedQ2A6xm-tMKUXYY89SaDFCmB1PJ2B1EPi9dhPyKmy5wmL6YxBkx_K59oxRfacO2PIVZZwK5xz38_nwbbCkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=N3tJhcgyBwv_Jd-6IYKo82PlLcQVI2u05lids--bl9l8ZsmnMV50dg0lWhXI4g2aJmSpKxUlOBOzR3E0J8IflHAl2nOZBIgSaymGVFfc3yhSD9EbyLvQEFqtw_jvFU8Tj3Bd_sNseASJUeBOW4o70cSwRb7b1wuthEjycH4UBmCpVTckzJhUkgGe7RHMArQMa-XPgT_rY3tgclvTboiU3F_kmBAM3m0cfsQm19oJors1zZxAV71xCVC1JeCGkj3v9jtLiSgVfhhY9U0TBdV4NCg1T3iiWdPaahTzpp2DNfrkGw7TlXOmuMaJXd9Ni9c99-0Pmqhzl_c6yK_Nw7NhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=N3tJhcgyBwv_Jd-6IYKo82PlLcQVI2u05lids--bl9l8ZsmnMV50dg0lWhXI4g2aJmSpKxUlOBOzR3E0J8IflHAl2nOZBIgSaymGVFfc3yhSD9EbyLvQEFqtw_jvFU8Tj3Bd_sNseASJUeBOW4o70cSwRb7b1wuthEjycH4UBmCpVTckzJhUkgGe7RHMArQMa-XPgT_rY3tgclvTboiU3F_kmBAM3m0cfsQm19oJors1zZxAV71xCVC1JeCGkj3v9jtLiSgVfhhY9U0TBdV4NCg1T3iiWdPaahTzpp2DNfrkGw7TlXOmuMaJXd9Ni9c99-0Pmqhzl_c6yK_Nw7NhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwQ0v6OztapK07cdwRSpW6qPcXI1JaTrL3Y82I5mQVPznmBWDNEKvdUvp-puk-9AQuRKC2UeopnbABk-RoJkiZ5FJq4SI-wEzVytQBWq8g_dWDAB-lV4p2eOTqY3enazlUAG-e-411e2w0wN_KVnxxhluO4kBy8ICfDSLFawr1_8mC4tmGjI2MN22l_ImAx9pjA1u_qCjEBcpQmQ4S-2S3NRx8gpZGYQ1PFrJNDxT1MxvsPdWwc_1h7yIbxgxsvLt1JzXd_PT1VOZzqk2c5ySYUlBF4YKTvyBf16BiK3DLld2BlHNlMVXDJjIobFfn2ORGKCqgsekNeF6-fimCxYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d03eEUrnnXwWUgAzIicD9gEsPutBXBimWR4ICpH2vwri7sHUukB4ShZ0kNdPMPaGPdpkEIIuFoKYiVKEliv6ZZZPPC5m32SSE5T6aenROQBMtA5Eidr3QB7Gmg09S59UYJcQq6VrVxxLuoxdyQB7SvdQKhKteZVBbNEs_bIgXpuHN-IANRaIU_7v95sFIFoczIJW9DOhEY7L_CaW9edoI7XfWqW73dtHI0a4YEQQsUFxmGXEhXVeCjMKlOSWC3npUAxlS-rWVPmBuyDv5ovv9A8hVpNezEOT9lMeyimUXjpHabpdtAr-wuN-IC0Bfa_MBmObo-RFxU7JIr50d-xdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKhFfFcsttxQb5M_Tqi_S4uGTN-wZeEXeNW19cWmuWT2r9sRx9L-50B3dH9KWXoluTG3uitHNHKXYV2J_oAy0IlfdnPO5xFGTEV1mRAKlVSngc4X4l2n2GjwmBknMDnpsjUBMpLmKUjanyOgRQrYMLqBE2nOyZP2bwLT8ttF0ouoPsc08Fv4kDELCRDe4dKfXHjh7T3IC17GBJtA4HUoIqJ5OcJbW0iA8o9r-uXydl2bceGYz_NkLgfZ15uUFV6RkFAPy9F7N8QJ_Pz6mcKLzvo01Xy1tJgvSNUx59KGqXG3eFjMGdwmwRG-TBZea1DKnRkakDe_c9mHj6tD9bZUgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=kcve8XCp4pGI12G_8clh_UKJpfsdmjaOLd2YzAeTnLjtg9meENFZerRFXlc39nom4OEoIWlli4eL-ECREYrV18wcFYJFB-Ns0UC6bfRVxeOgBeA3jJLIZHJS_qVzKhZe9JOQN6Z_uVqO65PUenEATbGjortKR_8QelpgzNt8uBHBgjVbCpM25N41YXYz3Ys6qRIvdAW7mIOx4fEXL3VfFIPWaNsKkzohcbe1am21g3b60fivnQcNtYrRLUAm7CDdONAjiZQvu-Q12glA4M2MbIMBFBQ9z5YGWIU1J2hQt8eQFVBAr2yIMzTO6XlMZ9qwwSR6ftt0-MNfR-OqeCq0HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=kcve8XCp4pGI12G_8clh_UKJpfsdmjaOLd2YzAeTnLjtg9meENFZerRFXlc39nom4OEoIWlli4eL-ECREYrV18wcFYJFB-Ns0UC6bfRVxeOgBeA3jJLIZHJS_qVzKhZe9JOQN6Z_uVqO65PUenEATbGjortKR_8QelpgzNt8uBHBgjVbCpM25N41YXYz3Ys6qRIvdAW7mIOx4fEXL3VfFIPWaNsKkzohcbe1am21g3b60fivnQcNtYrRLUAm7CDdONAjiZQvu-Q12glA4M2MbIMBFBQ9z5YGWIU1J2hQt8eQFVBAr2yIMzTO6XlMZ9qwwSR6ftt0-MNfR-OqeCq0HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=bw62C8iXZ6ZLgp6mN4YR7L8-pEOgjfjsaIlgI4egjN7VGWGim7Zps7UzihcrBHUnqFdWm1q43ez4VpwpMG41qPz4plLxs2XjzHR33L1oGcRn1PIlv-drV_9MZFACYWX4YwXCpdhn3iTf8bBMDh5QO8JoS1aFnJylF1j5_IZsYUA-F2lL81-M93OHy0rNz-NdUk0NnOUmliNztnGksCt_TqZgU6RrMvQfn48GItruDdVVhHUWjKRrAMREri5WRruHwryTrneXyBGFtkiH9XPTBShEugk9rpbucoIbShQXXq0G56gwbGFT7rl1xoQTc7Y9MZUPS7vTxIg5ja218CkE-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=bw62C8iXZ6ZLgp6mN4YR7L8-pEOgjfjsaIlgI4egjN7VGWGim7Zps7UzihcrBHUnqFdWm1q43ez4VpwpMG41qPz4plLxs2XjzHR33L1oGcRn1PIlv-drV_9MZFACYWX4YwXCpdhn3iTf8bBMDh5QO8JoS1aFnJylF1j5_IZsYUA-F2lL81-M93OHy0rNz-NdUk0NnOUmliNztnGksCt_TqZgU6RrMvQfn48GItruDdVVhHUWjKRrAMREri5WRruHwryTrneXyBGFtkiH9XPTBShEugk9rpbucoIbShQXXq0G56gwbGFT7rl1xoQTc7Y9MZUPS7vTxIg5ja218CkE-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxEl2Fvc8cmK9bm9xHuz3H9zMFgELcp9OHhq4qCijbopwfHgmaKn_p8juFxCkWAc1kdnRN2b0j44JIxD1VI37s1AGmBlJjM0rCteKApAqseZRwFkXCNMsV8ITTfHVACCqRhdMkFqIzl2qthsOvvVY0A-KSmCAdypUM8TZzfRrynpJHWAlf1s5tp-Dk69tIiuRo0pHrHV1TMdsiCzD7ERSpO12V1pjFH497cC_e_XtEvczceEA0D2zhnx7F17hvNO_tG5Ca7Y9AIu0529Opcy5dwSex2k9xiOo7bawFVh3RXcwGyFIIg5f0B2sOpyELplLldgLQbmFUKALO4q6gHjSz38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxEl2Fvc8cmK9bm9xHuz3H9zMFgELcp9OHhq4qCijbopwfHgmaKn_p8juFxCkWAc1kdnRN2b0j44JIxD1VI37s1AGmBlJjM0rCteKApAqseZRwFkXCNMsV8ITTfHVACCqRhdMkFqIzl2qthsOvvVY0A-KSmCAdypUM8TZzfRrynpJHWAlf1s5tp-Dk69tIiuRo0pHrHV1TMdsiCzD7ERSpO12V1pjFH497cC_e_XtEvczceEA0D2zhnx7F17hvNO_tG5Ca7Y9AIu0529Opcy5dwSex2k9xiOo7bawFVh3RXcwGyFIIg5f0B2sOpyELplLldgLQbmFUKALO4q6gHjSz38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdfLHi_glT0vqcJN5fLQcCS9KsRF2WprOisNqkiil4-EbV_gbL-rTjjxFHWDgfdxMwd39vl-zsTryJMOOqWRztuRBvB8cp1wL9ChwcdFk7ziJAvB9SPlYG7QaHc0oGLErca2z-8RnXSIfDwGOatSEEj1mDZv0LqISyXaDUaK3p5CbHPbE57AZudc9udwBtUZj7tcDJPgYGEsYLrqz_TTAJmmESSrpkPKkXXLc68OQdPwpEOjp41Jb8LoTsvNRPzg4C7vwRSB2iMJb8wbhItsbZDsD8sw7hJRBP22njzyNkB5fwUFOBDsUvQn_-Ih3SzszYfrY5x0sODFJiKCK2J4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-sm1kE85BK5y_PCfM7CwczzOi-DGQEAhc-9gfFu3S3NmoAyUM07eJMsR4HL5spoSXye2Qna2YkkFWJV_S5bu8XNo_wBJoCLpbAF5NhxbOd5K8EcYT1Kw832kwUCzpVwQKb4rVhW-7ZNkug7O1_dZGjfaEUUpsrljmApYQJyMfUci_z7QSGKJREHoaGMF9cCShGG5i6AC0sruRR8ZNlDnj6pAL09uAjOmjeSXzPPahHjFFnzrJM0Wk3WteF0hAwW8h55ST-Hm40apFrfWz3qV79r8ZxLl7ZG0TwHi1AoIYPx6xvtQF4QgBc-dLcYnLnhXoXTZu2JWf1tM4Mnza-O6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=cn2nO3ck5N0o7r0ispaOu6wfH8lYO-2ReLk9KFMDKGstRWDgfk08MzqGKkXwZ7QZf9ES7MzMh1du-i4nccfQl7yYHhtil6hwTB01IxIZlHK47e6qj4PmPsQ7ygixIw3-vdKpvzyranEBmsNQYCV9mn_G7AhEXt6S6wmWvBi_mwCjJjiLSXbjJ2aAOr_Hx837WnIsLhSz6y_5nFIf6GKFmYRqLNOTPaP9zKdxNum6PIggMAZ1TiHS4fuObIlMa2igXzLlFIEbtsiSrCENzTq6oQ043qqclbr-3jnwoxMcnLF8hC_TFKVD4HWWRrA_sewsGOE-JdFfPMcfhfr_NA3W6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=cn2nO3ck5N0o7r0ispaOu6wfH8lYO-2ReLk9KFMDKGstRWDgfk08MzqGKkXwZ7QZf9ES7MzMh1du-i4nccfQl7yYHhtil6hwTB01IxIZlHK47e6qj4PmPsQ7ygixIw3-vdKpvzyranEBmsNQYCV9mn_G7AhEXt6S6wmWvBi_mwCjJjiLSXbjJ2aAOr_Hx837WnIsLhSz6y_5nFIf6GKFmYRqLNOTPaP9zKdxNum6PIggMAZ1TiHS4fuObIlMa2igXzLlFIEbtsiSrCENzTq6oQ043qqclbr-3jnwoxMcnLF8hC_TFKVD4HWWRrA_sewsGOE-JdFfPMcfhfr_NA3W6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7hgSwppad51emZFJAv3cEKMS8v68VNOhQmzJ8M5KtcL4TPfnBk9ngOeqwhXZvLFBU8QaGxa7c29BqgJkzelQV_-CpnMVoyJtAeCO1Qxr2L4szkaXR0xet17EPhFS0JinD2RK83foya3WvKJemSzbZdye8NwrMEJ7tRpMgpU36NDL91kqJcuK2QrYROE2ADD-oQWqbHPu_pSuZZ9yp4-gbTc7S4EL3i0L8YkIhAelnPL0JI4j7vw_XW5RVXHaCvrNCIKob9zodJwtgByvmRYrB8QQ0B3mwVwoTjRaVQk0VIw9_9-Pi0P7mmVcFWwj2iG9PAL9UcikR13bbiCu6MmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=d_N-z9noeZ7B0xXdeTdleRJrOZ7kMiaViL_PgHK4ogkNOPr1gLet8shYYNYb92gamtvlaQkKXjQlQmcYORxMEevNO0vyz9xCFFZkhKTm87VLZBSbumaNRpInTqTPRUIfYJZW3U7oFlyrMybUyPIbOXi2AMcz8_JjGwR1_QoQ5lTGQ63SH4zIhDfOnzDGJkkEwV7ZlnZQEymB-Eufofj8JYjb9b7BH1nzqDZ5Dy4-JWWV1k_ukoif3XMa3FugHzdGJIEB56QveWzOez7zUGpmMEcYUgaPpRcQb_MW-vs6BUMS-dg4Xi_EMEWX57zL8WrbbFK0OitSLHEZ4-Vzx8X6Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=d_N-z9noeZ7B0xXdeTdleRJrOZ7kMiaViL_PgHK4ogkNOPr1gLet8shYYNYb92gamtvlaQkKXjQlQmcYORxMEevNO0vyz9xCFFZkhKTm87VLZBSbumaNRpInTqTPRUIfYJZW3U7oFlyrMybUyPIbOXi2AMcz8_JjGwR1_QoQ5lTGQ63SH4zIhDfOnzDGJkkEwV7ZlnZQEymB-Eufofj8JYjb9b7BH1nzqDZ5Dy4-JWWV1k_ukoif3XMa3FugHzdGJIEB56QveWzOez7zUGpmMEcYUgaPpRcQb_MW-vs6BUMS-dg4Xi_EMEWX57zL8WrbbFK0OitSLHEZ4-Vzx8X6Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=kOUghT888hDUzJFVA97xIBcQ73-k-hliChCjBhtYQDgXWn_GXjtV7Jo8H0wY7wF6YbVc_gpl8dSmiIm17jVyQK1W5CqbIYY_T0ss7Kc-PX3YSV_wzUVS96y8-8pLt0K0yyAFOBjD3u6vI_0aP4NgkvOba79OJbQAnU5PnFLTMWHxzPF6iVbx6FGh1qIsMQ5vsFtbeAc1yXBV2e1xmBJQ3Sjhl3WLZJQOm5baNu89qH0m-zVRUgctHoFkq_jWEWJsQ2yk43w-7T2zmUzyb_2pPvEDWSEeBVgC_D1fQf1M-o74ObC1XCZfu8W72NReANVA3yPP5iLmlOGL17IobJ0pjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=kOUghT888hDUzJFVA97xIBcQ73-k-hliChCjBhtYQDgXWn_GXjtV7Jo8H0wY7wF6YbVc_gpl8dSmiIm17jVyQK1W5CqbIYY_T0ss7Kc-PX3YSV_wzUVS96y8-8pLt0K0yyAFOBjD3u6vI_0aP4NgkvOba79OJbQAnU5PnFLTMWHxzPF6iVbx6FGh1qIsMQ5vsFtbeAc1yXBV2e1xmBJQ3Sjhl3WLZJQOm5baNu89qH0m-zVRUgctHoFkq_jWEWJsQ2yk43w-7T2zmUzyb_2pPvEDWSEeBVgC_D1fQf1M-o74ObC1XCZfu8W72NReANVA3yPP5iLmlOGL17IobJ0pjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=b7jI83zUHGaizaFCgG0FYLJzdYdoUs5b0NoriD5urNha27tStwHXWL-HHTo-FifpFB5kPdoNLgoi_f-AN3Ap0NUM_46oD1vKLUaUUMCZtpXiZfZ9_gISlaQGH3jv3DfFGzbkPzN5GntXs_Jmilawt0jQHmwcWhuU4TVMennjzaQ1AP_P7DQb5mERxl8sAoZTUVzNZ6_0RL5XPrecxZXCVZSAWY06jPVDI3MYIkDDCwJ0uZT-KEw0oHXEL7d2djhaEqn216VWgo59ewK_10saEHSTJbSJVB0G7XtLcx3ZW7TC9BpZ2GVFuR4asJsuOe09yqb_GFkbomo8Fd2SVzN79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=b7jI83zUHGaizaFCgG0FYLJzdYdoUs5b0NoriD5urNha27tStwHXWL-HHTo-FifpFB5kPdoNLgoi_f-AN3Ap0NUM_46oD1vKLUaUUMCZtpXiZfZ9_gISlaQGH3jv3DfFGzbkPzN5GntXs_Jmilawt0jQHmwcWhuU4TVMennjzaQ1AP_P7DQb5mERxl8sAoZTUVzNZ6_0RL5XPrecxZXCVZSAWY06jPVDI3MYIkDDCwJ0uZT-KEw0oHXEL7d2djhaEqn216VWgo59ewK_10saEHSTJbSJVB0G7XtLcx3ZW7TC9BpZ2GVFuR4asJsuOe09yqb_GFkbomo8Fd2SVzN79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=kPP1H4HVyOuxZAeNpKkL8-hM_I3iE20FSog00sB9wu9Y-xz6zhGlith1WejerIN4NZO02zBegnzmdrbe3HJap4oQFe5wzymhlvFB6LdVurfN3SM41zblL6NMX454DIpenluHfKh8eJ3JgBMl0LbDfMeTU6M72mptshQIe9SUcMpwaUrFLrDtAC7myrDEgTt9UV3WWDW0xtNJtBmt9gXs7v49EktRZiU9QUOEq2YcRfgUs8V_5ss4MiYUZb2Bxqo2lRMEqHFZh2sshnwaPiDFKKQTBYEwWcez-cMaztYF3YZTLpWLa2z8YMMiZ8lzC5Wxez_8-jdAI18gr-rysgTLAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=kPP1H4HVyOuxZAeNpKkL8-hM_I3iE20FSog00sB9wu9Y-xz6zhGlith1WejerIN4NZO02zBegnzmdrbe3HJap4oQFe5wzymhlvFB6LdVurfN3SM41zblL6NMX454DIpenluHfKh8eJ3JgBMl0LbDfMeTU6M72mptshQIe9SUcMpwaUrFLrDtAC7myrDEgTt9UV3WWDW0xtNJtBmt9gXs7v49EktRZiU9QUOEq2YcRfgUs8V_5ss4MiYUZb2Bxqo2lRMEqHFZh2sshnwaPiDFKKQTBYEwWcez-cMaztYF3YZTLpWLa2z8YMMiZ8lzC5Wxez_8-jdAI18gr-rysgTLAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWf1-fo5FdeSRe2GI-FsKKdJsyJNynNshbJHsfBXrbT46iOrVmiL03yvIfngCSOkt9kjqvMRrgqomZb8Kmrii3MJMRsm4dDSxM75I3a7idvZyMGOBpJPCziMDPD3iPZCgiCLdPx6IKqXy5iouYU_RA6rHfnEp5iiA8Db0uJ8YbsxqxbrzZO6vjMUH1rj8vuLiYo-KQSb6t5uhjfxaZKCAeMFDYvf1LyV0e-IfG3vVfBHmyc6ZkVlavHyBmFQaMmGeoCY4_UuepctqaIBhFchXrzWpNRBzUbympMQ1jbKDZvXHDhssexIxS8sISRc42DVaOrsKEFM2a15mBsdVbUZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvR3U7YAKlPuzO5WtESWTUNoex9S7FbSHj7Dnf_Zoc7ZUeDbHbKLkIaHq_jqiawT9E9OU3m3PbXhF9EbDldWj846bU8yO_YMDbEhJTPNUVhYZq1RUEWGyOPKPbgtBBB8ktQY8kR2L5wt_H6UmbE1FgEgJLt6P8Jq09OjgZ3UOp-QbaLU5cCw4StPyFcY9J-0GoynmHLkbpg152b3y8HwwJI0aW7psi9w7j2QqYvRAg-fF5JZN1KZGC-MYxB2cPXv2Hbl8LhKcV3Hig7XGzDhxCTeViG_QBdS_YSZxMJQPisseMTlgphmdyOCvXkS5zypZzWjVpkKuz_gIci_w26qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk6gbCvzHpw0UBOZyyzCGwpQGiwIHKlOBhm2aPMbWnYQwxRSDtQ_r8GIunQNn-xScPCU8DDdQFJUCR1gTuInk5Rfbc-iRFqjxUHlAi6BeQnUOQxgy6NG2L0Z9SKXLayz-4-ZnbUS2rp9iaW3ZFMSh9tGPnopGRa1NMSDm4xTT49ZP0ZIp5wXk3LLX448w8U5KCIbIzTw3A4T0s6bPC9pm5KO3YUcif3BRBGezdhfKgeZZFvP2idrQ_1F4JWnlcr2mTIoG5Isl03Te-f2ujsX73vp3dQ-MMFsNKt7mfP9GHAJV8lKJoIL_VO3ojkwHBuOp6n7VeSEScswqM6WMdioFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c95JT6OPd2ZWNd6ffUbGHtcDFdK-l7iO1f00x0SkjJ56V2t8fbhJqA8VwWjP9gh5uz_wbLaUV--qm0pWGqQLCWNNQadTgiJD8OcFn32SAS07dDL_ybvB-AgjaMlLIhZCiVIknbcY7GAS_KkGi-KaaoPqacSjRpd-UAtakVJsaUqNzRkiYwV5XNUDcmw7T1WRFKgjcO0uSKzQ985pPPIuSjYtSAypiR_Drshmx0xShIIF6EJ1e8Idx6OEW7mjY0i_RskdyH0qRfpyqkc3SAnNzbiTYwaaS8s6z1COYztSO6YE0wXFBeXgJt4K26H6oB38pfpoNFrsg1KD5W9Df_l8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlA5TXjsfuplbzeCUAM0vOHJYbn0-Gm92h5Umnua80qtbrE1SKMokPP2BAsEhSyLfLEwuumFiqtUZM0AOWrI1tJ5DyklOkzOAIoPIE7PTxwo6Xh8W4rs9yyj39upnwkFriDRskWVI1vPvwelHT4pDboKSs--Okjnx9N4asCs9cQuwCe-PDORVq6u3_UkHpMkvoWevQV_rbq57ZFyp12ISuD3bm3Tbdnu6yHE1kstmaqytN5p7odfTaF8lblOH55QmML5E5kVgfQKCwzW7gmi7JIY_C_ls5PkJXtvZGNFda2SyyfpXINhT96O850PJa8YHzFeeagNAeWmB3d88v5_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrRRAr-ijH9iklk49y4C-_N1OnIh5LUpxvS7sBYKMGNRxROmeGL4p5E0FtXyMHjhoU5kw4HJgE6yx4QzLV4JLO3ZvPnu6UTJMHMxEz2KHcttoo4zehJVNP4QlWDv58cAcYJ1OLAXp480F80QR91QXmj-GUT6Hk65yigJT_rsTNokJt25AWuHYZwGPH3GHobmytTRSGD6qpwO2-9taBz7-WiHupHUwzZfY3ePc4drQ5TV-wH2Th9wj1_DqalHFx_EY_AXXSIbJ3z9U7hzrnu6SUZpDP28Jd-tS_uB3Sb23VAFP6sVGFioGRap4Y6JoZyBqViKbiECrNVOrrBqEEG35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfmcO8v2ZdIRre3tDZXYp--C1SyCDw_kubZQG0dK3beE6xwHZBl3NpI5WI6Jm9uMQpbS8yaT-worTcpL_GwKjnfSnfxMD5d6DcyvwRlFZOKX-uOYbYKcoJsln8R3zba5IKsMcFCvbpyhtKlslNCs5ZlLLNF8xKhY226EYIy8nXqSRAgd3fFh1Wg3sH-QR4lec4t0pTffz-yV-DMuEoAbUCtDIkuqhogucTXk25YPWvkOKIpRVM71u6jqY8BsF_47nXIHDC56zv9JmWTfZGtIVWTYh83n0eHTaedfmiDYJzZuNf97XI22Trqjr304Zvv-u4s-NNDJvHCqW8Whslllwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=H20JFIzeJiJOodzM52hE8bHeMyNoTD-GkXCWMVCjhCA3ayCs_tFUtmBPnBoIl2WCLfyzHN_TKM07AgAod9SrLaaEenqG4S9D1puZD-N4Y1J-JPCkCXgXhQ72RBU_nKiAl_h3g7OMj2Kv_NR1b3tUjG9xoql5tRDx-Jf7qTQxQ4f9dl0FewTtMDPVDJirHhimEM8uoL5T0HYbmxfUi_oorSVh86H2TiGLJSA5LoyF1F15cTLn2DYtdUfx1KCvWz42z8OdCrg7ShMkWE0z2PTjMxROuv8emL6VC0T4Nff4lxXBAWS0SFD3Ky_C6XTwl8719xPHqHlen84fAz9C7QgwlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=H20JFIzeJiJOodzM52hE8bHeMyNoTD-GkXCWMVCjhCA3ayCs_tFUtmBPnBoIl2WCLfyzHN_TKM07AgAod9SrLaaEenqG4S9D1puZD-N4Y1J-JPCkCXgXhQ72RBU_nKiAl_h3g7OMj2Kv_NR1b3tUjG9xoql5tRDx-Jf7qTQxQ4f9dl0FewTtMDPVDJirHhimEM8uoL5T0HYbmxfUi_oorSVh86H2TiGLJSA5LoyF1F15cTLn2DYtdUfx1KCvWz42z8OdCrg7ShMkWE0z2PTjMxROuv8emL6VC0T4Nff4lxXBAWS0SFD3Ky_C6XTwl8719xPHqHlen84fAz9C7QgwlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpBuVekTBj5Ev0GtsW017sqvQz7MSH4fuWdAiR3yVQYL9DhPdcrBbYPeAjksBE-i0lMFbCoUbRQqq_gNjLncTeER-DcdnfdW8_LA-vLShtib3bFs48ki-2fFr0hwhWsrgnBWoACed_ls7LPwt8dpFAsDr2G0JOLtqqclWQXAow87e_zbdOTTjta5BrLzP3qyKuDaxYfuDUiJHrxln0zIoEv2z10sMEH0uC4wh3xQeok7BtyeLCAELPkHDS2nm9Qk4axD-fgp0F5YYmjgnkMMIv73cugaYeyu8senNo5zDXagL9b2Br1jBO6FitBatsbo3INxLCkGT1sRUdXJ9B1ovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDYTkbfAkewV7pYJhzP0sEZrN3z-sobD6566Sx5qvBVD2TAOX5v4pvZh5ycwoA7R8GE_qPsiyF15-hqy0KIqxCAUUVU3wREgVS-qPOC7JksMm29JkmjhuXEXT4rJKYdU7n-GrBn4vHacSMzO2O02YwdmWVOf_bxAW44rtHVySRhixZ4puYwh4wcqmbJG8gYPsPqoV0pZypuZ1v1WXE50fru9UkxlNs6rHKYWN_Ab3fAeU6RSlvfrxqYHcvCZWX0nUpIfl7X7R_qGxmLtYCuf-dDB_2_b-bCQ5mD7jfmhdBDc9NL1GlAM90eaRymrH_qteeFX6fjJ9jxgSHOlGFXeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPQ5miYYSXZ3NB5YQX2YcE74t-3_RkGE4GhjtBquivmHj2MVzz_CVZFUwG9U1gVwdw4T2iWPc1jzEYhM57jundoAUq1kdmE09UtUk5P7Eg7rwRS9UCeUH2JBYKrNKGGtQNwoMcZ3RNUvafsmpMwUACvB3LdzFiDHZ-_j-7VzWvWT_KfVl5qsgovaET-PPpzXwGgKiAE9ZbiJvk3wUFiw0pCe4iV3rRJgwQBy8xTntFIAiLEw-FmE9vwUwQPG9qSUah2TtEiKQ7Fy2bI1u5f1dKHoPQ18DZ6pvREa94ZDFu5NQEvoYntyMp7Ab3AFVINTy_DINEzwyzRHgdKMmzDq8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0SuWXTowxf6KSIA0uKakP0z-bdbW4h9mys_9JonbMhnhBXrgiQdvMIrlgg7R4Uku4XOJ2vg01pOQD1iA7tkgZUzYeuqwKITQRO7sypFfTdJ8DEaBsiwZ2bTrcPwywahzfYb34luo0BlesOvy27eElyXfAPLnrSzlrASTQbQyfNjIE6plhU64Ge72WVps27KQ_yszmqx4nYwjoJ_9vMOQVVlgY-bKUS-d3pZLtDF8QMjBDwOEGRAfwKiFg9M9Pp6-oqe1z1FcVJ5DIVBV5GMTRx2k8A-NkOuGhZ0HZw4OZ24wWn09cFhu0-hubsP1naODrRXc0TOQ4sl1349w1JG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFVPX_sqiY-Ku7HIA9ATu4zVH7ASnZ07repDINKsvelz9dQuXmUcnQQS5QmP7sv8MgsocGVEoAUf3xa9rMnTlUWSIkguQJRDycILK5xIZ1owI9TYYPc8ah4H_T_DjyC_d_zVr-ENTF94yKxdriixu2rtbt70zLYF8vFdP70Z9jrrovSRheQ0ctMYK8IYtFiyYdx6tclcKVOZ4yfuO_cBpYrL5ibwCX6ydzp5UrvVJVTT4d-ar321G7JCLDV-4NbjZo7U4BZty7KU4Cawqnrs2wjUmQzhWXeJWcu7ETEpPYH0720udehXj_gvNq5EddOvhncocvcaIaUelP5-ZqhoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxIpwV32oK6gLAjaUnazL3-U0gHBtqel3hCC6-RqWw4Xl8c-AWZxXoGr7ocK-UVqDVQm6Q3b4mxRKwwogkhhKh0H9USJYy8Do3wkR77mHFuLnhrcian04G1SRoQXaWbzO5Tb6DWApwBUH66var3GJStJRoYCJq6lcxAWf5O9MXCy8pexo6Qt0pglG60MTJRebefaRRIz-esJEKWW0h7FOaPMNQbtSqIN_HkU_sXzqjjxLypxrj_VTsIr3p948SFtt6Zr9BBUJBusfbHM1hUGsET7U3gZry1opBbNIF8QOKFN9LhUE-bWglZLIkGt5oXEax0rnUZbjjJeNqZSbJwF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXOdNRQmhmvnxtNroNQnnzLRispmqSYSa20JYzG9cAPCRY6w3HC2XJAAyGcCwtIkgqz6rutEhBnAPZ1xcGZG_nUnFzVQfCOn6XrZ5RRLaP1NNkr9njtO_A7iyxuETQYmU98BsHtiA_zkGxZ8P4RCC5oMwRad8HtFKCBWeIcB_3-KRXdC7vFvrIeaCssNgEYy8JIpSTr_mfaWk-RYLmwzdLZYWzyz4UhWz6smRpI-Qt1xmVUyZoUGcGko2nvjE5GJVCzt_VPHcQO6G9P7SBPFRzqMII1hGeGmJDG0hSD_4W1MiFHOMTWHra11lC-Kd4bFSYWSIxnCnRgTSnMTS9LPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5nrZaJP-o-dIy2Z4SSLuxKPbNfmY6Zy3Ol3abfRHgqQPM95ixiw42PXJ33WUsa93Gt4eQSWOJUrjSRJ_rFKK2X7o23IxcNfE-DfR5UIIdgRBZVX8xvlg0QWZ30kSKFlBf67N8ACsbzJbazGazND3bvHtAWzwHDO1Vo4eda_lNAQ_dCM7l8VFfYDA53FEFu7gvV1lQNhLtqo53Skt4zfm-cHhsaoItc-I7xIon2reDF876JuzXnHN3HAM_3HWw4QGSzRwt3F5fSKxk4ex_f8wiPGdUFhSKsYTi62bz02yYmDHoyDRwDwh-mMIGpD74iT_0Oc8Kg8GhPEU702QGYQqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=pf8jGDSgeRX41mANO7pqY3uH7PSCaOgmpBZxM4P_lcazKoaOw6jJXVrm9bPaVx5AbzO0lic-IK5nagWNFM8jTcaxH4UXcpT3OKGtgQYYVX1822S0YdrcBgbyYJSHSgQzJH4-FORNOu6KdqQd4jRpwAp9rL77fT58pcu9jKbaYpyimsKaB3Z1AhLe-m6pFhX4kVxmEM-aq6Z_99QASIGDsV3XOxgNZiRYvAGDS2y6oyxVKGx8zY8GudyBi69hHWcSLBn01qGGwjEHGsoWWO6Vfz27q3GOx_WaRzUNaEY9qRP_O79VR6H0GM8Irqv8aPmBmo0uWU16i_-z6vNtzOoL4TI-cTNN4eq3gk6uCszFrl0cIi3j3YPQfCjDFCh7fjR6ssyBQPp8T_Cj7j_b0DDB1U4p8ZJpDyznitBOKNNXSPtghypdgaauv2-YUvn-aJKB6kQ4qm-q6DmvWcwhB26BFH2dWS7a2-vXk9Cey-RAp4CTTDamUlwClqRByZJB87vfk783zXdVYu2VhuYtOOG-8w2sNY-dPjaskcmIq5nR6MnxnjbRMf6_8lc3lPoPALgBbOd9vEXUbJU6KYsEPyRAA6epMrKUnTjSxDB5sC55gdxvN3aSxtcldRTRQFugTRqgTFaatc8OAjRRIyrUUDvDAOKZxVferq83leDKvxPB-7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=pf8jGDSgeRX41mANO7pqY3uH7PSCaOgmpBZxM4P_lcazKoaOw6jJXVrm9bPaVx5AbzO0lic-IK5nagWNFM8jTcaxH4UXcpT3OKGtgQYYVX1822S0YdrcBgbyYJSHSgQzJH4-FORNOu6KdqQd4jRpwAp9rL77fT58pcu9jKbaYpyimsKaB3Z1AhLe-m6pFhX4kVxmEM-aq6Z_99QASIGDsV3XOxgNZiRYvAGDS2y6oyxVKGx8zY8GudyBi69hHWcSLBn01qGGwjEHGsoWWO6Vfz27q3GOx_WaRzUNaEY9qRP_O79VR6H0GM8Irqv8aPmBmo0uWU16i_-z6vNtzOoL4TI-cTNN4eq3gk6uCszFrl0cIi3j3YPQfCjDFCh7fjR6ssyBQPp8T_Cj7j_b0DDB1U4p8ZJpDyznitBOKNNXSPtghypdgaauv2-YUvn-aJKB6kQ4qm-q6DmvWcwhB26BFH2dWS7a2-vXk9Cey-RAp4CTTDamUlwClqRByZJB87vfk783zXdVYu2VhuYtOOG-8w2sNY-dPjaskcmIq5nR6MnxnjbRMf6_8lc3lPoPALgBbOd9vEXUbJU6KYsEPyRAA6epMrKUnTjSxDB5sC55gdxvN3aSxtcldRTRQFugTRqgTFaatc8OAjRRIyrUUDvDAOKZxVferq83leDKvxPB-7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Gs1omloC0vcnEJDShsAga8neuVJxBnhGCO_dcDfvLQSxBwl6BvWRkeln-_VSs49OEWVHdwybFXCEW2_aXgZ3Epr4OL-HfdcyFjVXqLr0-mFJBuc57Do1HMiwBlW9XvxPZYzb6iP83x5TeLKS1tFTM68qlL7lb4jfYiLYwFPOALaUioIGh6rwGdvd-0Um2DD07EHpRZDWpn26o_2JCrSOhOmMcvDm7JBqIUSO7X-asXKRJ1-uoMOxxmX0l4oc0vyEfbx3gOsI3WG5oluYUej5mv5r_hswnlrcZFGh6sxtIHnksmENluiXzYUzciNwdEjd0UcyHdezPe6TMNUa8GpV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=Gs1omloC0vcnEJDShsAga8neuVJxBnhGCO_dcDfvLQSxBwl6BvWRkeln-_VSs49OEWVHdwybFXCEW2_aXgZ3Epr4OL-HfdcyFjVXqLr0-mFJBuc57Do1HMiwBlW9XvxPZYzb6iP83x5TeLKS1tFTM68qlL7lb4jfYiLYwFPOALaUioIGh6rwGdvd-0Um2DD07EHpRZDWpn26o_2JCrSOhOmMcvDm7JBqIUSO7X-asXKRJ1-uoMOxxmX0l4oc0vyEfbx3gOsI3WG5oluYUej5mv5r_hswnlrcZFGh6sxtIHnksmENluiXzYUzciNwdEjd0UcyHdezPe6TMNUa8GpV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3OyYB_2Tvzv8mN9En7-Sc87urrJdkwu4PO6GU5cQ20j4WQ_M1fPhHqfvHq05mz4tYAVoEYtAbP-VfF96yzSG21Lz_UlZo5AOxU6lPxABip9_lmQzN9Wtv9IMgpMKYVZ1a8zaQkEqTA8EMibRNyEjbF_QGixhIENtdJst1_2Cf3tKE1j3AuG6e5PV7d-mcAYbJO95nA573phGs2igSgdGjSpxtdDlrXEQ-gaHD0vK3UbKGfBucFfh0u_YevjdPYg6LrBiVg6R_64Q08WxUf45kobsVFrA-W1IzWg3dAxZ5VzXXynN4Qqst-FD-zm459fNps0R_uvkGPXdgJ6tcPqsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK3GVq95CQoQGvegpklhIikFbJOtI-oUXWgx24-55UEr-AGOxEXeMnkzAYcUsT_Ny5DklnDM7rR67e8TbxxXrFhp6araRDGcr5K1T387l2ywOdEgG8iIkzdwES3J3CUPjxO-_D16C91LDFBbYpsetZIbd3Y87U3GYh1o4tRN9_LXSOAZ3JhXfAUpeam1ffBLqJ5vYRnoW3Bj7HJuo0Gmvs6RYToicqlShiQoNrwOZ7xOzj7xB7p_hA-15u1dTR5vjGZRcXseUCjndSgLyeMJHH2G5_U3A7w3Bv9fOT9OjEuBBb9LZLds540Yhg5EDIJYuQd3dqPKh3s5pG22i9SkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcf-oDaVUPkW7fDKpsnrmciUcYnQ_9k0zhk0vqFwDWQnuWCJfsSOWkjCGCEgbZYnRNmm_G5zSv1_zkIE8pRzT-Au-95xX9Sck4fCHbVCyn4YN7kneDSxGnpOyPIhygruYLea7E1KrMtMjSFRSwzKAlw_IlCKHuqHFrhXc29Q8muqmi19puj5ja6p65X-n3M-IxbUW0J39KU41reoa9N_A2ax6TsKpX-SZAnMFIKevQdqRLBjPGrKKyyQZav6xenN5tl-qQfJ-NMKDoUm9dMSW4TCTZN22yKu5cUyKnYpaMmhoz3veiHI-g1-RO2zDTqkDbVxVrLBp3zKaTdBwgoTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5tC2oDnXYbULWphlLts7A3EbS6OVP7jmE8fZOqS_2Jg3s2xmBQh1X5pk0Vq34uxgLJnCdrq9jiReg6DKURdDcRspzOKjwbn0g-zQQumZt9JJPmj46Amb0OHXnXksJt2LVqyYYaT6uWph0BVXNuiFeXL0oSFpiKWqa3IbtsQZEgGtTtT6AD50NIDm2IlWUNxTeyp6KccRliitOL2URcpETGhYsyRrei60Gm5QYoiKzAVbjfuW4SwOrILDAQtZd99Nd0WdE1i_g_mQbhuD9rjL62ssRUkZnKx8W6UReSq30sGoi_RgeHbfCmGZuEuoLBh9wZxo9fUFYaOEElq8c_LUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trIw7C28_UKI-EkgK4GHpYGkwd1ezrTMbqUQcXJKMskKLlngjysfsWjV4qW3IiSaN1Z4e63-3fnGsdyTcgPWe3Y_doqnx8Mgb5MXEjv9-H7lGU7XOQTjEWNEo7x7hcZOxgNeVH8HyDHycFQkDbCt10ryXKd9diq3tYubpOiy7Q1mlaufijbBkCJWYjIhfbQ-eO_ymRPEBk25LY8zora6QqvbWuKjvWvJJPEeYMTYdye19iJbikEabwQJJK2nXJxhi7h0N_c8UfTgORhLDuYsdQWNGWHK4zRsGaQXip1otRiKUxt-tu4R_ml4DJteLupjrq9H-it76I_9jI_e-lqC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCHE9OczUwVoYVT0yvj4cHAn37qOMeL5c4o9CbwqODEob-GMdYZ3vd1chZNNEBmwdg0aJ1uooR1Fuyu7XyWomZjrnVyol2JyIYx7M4u_9Qlx15EhaP2rNGMCIg55IZ_lpVv_EA-KgOJqIbiO8y40QYXS1a9MbMfOHB_VETWiusJt9AdueSEd9L_-zLDE_glieCSpkkBRG-CfvtY28NEli-i437iwyh69jQ4P9pGXP48DXCK9Y6a2gj4N2SWCKMJI9g0R7s-9TWl7A61kIRLhn21MoGvuNoFNGLrSGnQUHBTOplOvNx3nUFnWjBKLsMS2VXjnjvxDpST5lWGSGnKdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcylKSuVBVLJ8RVoN09SD4F-cZRgS3Ilb71OJkdCZjQYB8hdo5PeVsWpbnJ_nDJ7tXhufAgdpQsKh9ATiMTp2KdIku1f4DFCNvOPoBuNzkhb8wZGPWCdmbG5ePu9-_ZsnYf4HSwZ6TNSBu6it-t80SvVwOTNDHmDQ8sdwsaPw0kDKfE8EXQFGV0oeil1JgbNZxHqxS116iHP6R7LFT5h2FuLruCloJSPWxfDZuUOeJEne7RMYNPo7GkxmMCZisl0YzTe76x-hHzwLiwgXXEteUt7imk3Queijc9m1_CFhljkX1G7c29IbiAioD7jUso9JJ2H36WoI-aOztiC18LXRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzOg4HFteeLikH9NQvH9Bqj9_LQYEoL8yHiX4x-fvjOx3rCANz-GfZjcaMkFM9FvArF7GTaFCLIRYA88DAYg_7shImklJfHWCxlPSC6csAQE4ZdCrNJonH2CCmk1jXozkSxU9uU-Brx5ch26TTx36PWAY-URbqvZIjhABJc40NCTt6GpUlrMnG4QqK_I7LrbKevnZY4uG1k6HVmDFOx5wL7C2SJaKE-Ch24uR9tE7H36B2kitFD2rdTk1-fyBRzeYZojVPpwe51HqYOHh-S_aC0Hw4tq9yb77_a_F3lJV3EArDJzEkqXRFzKh_5esOVULC_8wayQe7LzjB_1IKA3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-eQoN67wRFlrCSVj7cWjxg-yfiBBRUdQb2hKcnjzAjgWGf9tHFq_N2r-lahRQ2O6pd-GLrrn3gTOFuJxq7a_iYTS6XdVDSpae24yQg_QK5KdlcMk4YDdZRTtOXQy_pgo8BOAPYHweglVIA4OtXanTRsgrrkF_STxeMwLpPt9zrW9LGRWzRpGrNbf5gfyMF1uGaaFUi-1dxx7nDM7MQOEziJygE7EhQFqYiv0PXdexvgM17aNTm5fZgGfCXyklB4jneZ82WAz9N8IS-lNtAQgLi2i_yzdVZCp1HUqXfGihIwXaAdEz-Gf8UcpHpecUoPd3yFStVnlRuWEiJpGFNkVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ScCmPkygKaBB8UhLOw3RgPVHR57cTlXaECfu4R2sy-c0rqRq7EJOwRNX0CNYE3YoUYSpMzw4gqiryzT2KPesmuFuyeJ3u5bfKI-D4krDjOLDCRnyo2JOfzse3xGrJ2jmhoRlznpvpg2NN16Wka1-P2Mb3OgOEpOzLYyr2vWf_0f0LY54ofc5hDhI05NIVz31FfUZ5mbJ3DyiIPKWfD0biQTVXwfoDcKxaB290mIc8-s8VGE-SDNDAThRJpOrJap6YWaFO_ZqSxa9rMaWFZMGT8oTERImoz0NNf7Kb226LA7D8CvMHQkIT-WBUnkbAbU5_47ngtSbiw_t1t7o3lpTsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ScCmPkygKaBB8UhLOw3RgPVHR57cTlXaECfu4R2sy-c0rqRq7EJOwRNX0CNYE3YoUYSpMzw4gqiryzT2KPesmuFuyeJ3u5bfKI-D4krDjOLDCRnyo2JOfzse3xGrJ2jmhoRlznpvpg2NN16Wka1-P2Mb3OgOEpOzLYyr2vWf_0f0LY54ofc5hDhI05NIVz31FfUZ5mbJ3DyiIPKWfD0biQTVXwfoDcKxaB290mIc8-s8VGE-SDNDAThRJpOrJap6YWaFO_ZqSxa9rMaWFZMGT8oTERImoz0NNf7Kb226LA7D8CvMHQkIT-WBUnkbAbU5_47ngtSbiw_t1t7o3lpTsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdQHYsuZcIbLAcoLt-lNwjsl1iwtH1MgFvQ9z8yuGuHdgHI34bOkFfC1J9J-rR3HinV_4cwaOrgvwH6CLSbTBs9sxcpt7Z-onpOdL1pSh8ABv-HH1HdqY0BngGa8Ub4ySb9GQaOlUl9IitLtApMAtmVB1hLkMpfFLOh6N6bqA7UAEzl_PJZDro0UHpGRyV6eh389WPh8I3RLpbzp4Sdr3n8NUyM8mOKMDq14rgQ0jCQwtss6B1Kj1crx2v9aSaIO2nKa3zNddpGB51e9-umjeuOjPGJk4dXMPjLIjkeYmdzolM7sl6OR5TLkFK95I2cIlSEbarAcF5Pgv8v8mpg6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=eQpUoBV2UbX4gwbmiI5GqtsOoQFJJ-gieyC-oX8d2VZD3xyz_St2hip6zEo4a-rKKDWNR_NoJixvZD1fRxjDBAFYK5zp7BFHwH67mdJrNhVLUWo-Jlfkkf-b-m5xMYpTzrsuQNBHK9362ONR4FD5HXjZ4wLAgPDHMF5_Y010VmPkp9PUqWuVelwwINwjAHmuZFdL_yo-4WhGM2WmRk7IDKwc9UlNZQysD-T5soonO-W70sA_77f3qs8IVr64pnk4gZ7h5fWTn08mMP33A4jEgv45G-tq8JoyVRawq772lZqOjORLc3VJgv_9UdlCK_D6Fh0nX9axgJTsaFDi7TPjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=eQpUoBV2UbX4gwbmiI5GqtsOoQFJJ-gieyC-oX8d2VZD3xyz_St2hip6zEo4a-rKKDWNR_NoJixvZD1fRxjDBAFYK5zp7BFHwH67mdJrNhVLUWo-Jlfkkf-b-m5xMYpTzrsuQNBHK9362ONR4FD5HXjZ4wLAgPDHMF5_Y010VmPkp9PUqWuVelwwINwjAHmuZFdL_yo-4WhGM2WmRk7IDKwc9UlNZQysD-T5soonO-W70sA_77f3qs8IVr64pnk4gZ7h5fWTn08mMP33A4jEgv45G-tq8JoyVRawq772lZqOjORLc3VJgv_9UdlCK_D6Fh0nX9axgJTsaFDi7TPjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=l8_jZNa_rEQl3n3ygUrf4Nk8C2A8JPW_HZ-1bhVMjLpFQGqyXPBfVkDHLcbQv533y7aqheVNGF79SeFha7yrcomPml79nEGzU5X_nwcLaHE8XZwq9NCWPBk1mBTCN4KK1uCYtBLTK4gHckEyzTUDeQmdFiUoGDHKdQ2EqBlTIIcRzk3Lu-2_aEf8_DwRV6Quj2kgq-wd8ia40CcMMlZhMER1BxK8hQwktmlRYpDprRPfU5LtmLkfYZIh44MPshF01NUDsGA4V1TErK3IEW7Q9a8qsW5jVgXXbA1yHG4nnReJMwXfsTui8bmZ6Za09zol5L-Fci5QkN2WYfTvp_CxwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=l8_jZNa_rEQl3n3ygUrf4Nk8C2A8JPW_HZ-1bhVMjLpFQGqyXPBfVkDHLcbQv533y7aqheVNGF79SeFha7yrcomPml79nEGzU5X_nwcLaHE8XZwq9NCWPBk1mBTCN4KK1uCYtBLTK4gHckEyzTUDeQmdFiUoGDHKdQ2EqBlTIIcRzk3Lu-2_aEf8_DwRV6Quj2kgq-wd8ia40CcMMlZhMER1BxK8hQwktmlRYpDprRPfU5LtmLkfYZIh44MPshF01NUDsGA4V1TErK3IEW7Q9a8qsW5jVgXXbA1yHG4nnReJMwXfsTui8bmZ6Za09zol5L-Fci5QkN2WYfTvp_CxwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzNFZKFCDDwDdVDJDS7VVhnNWGvxj6MgqVKrIyo9Y6OFWeiRv1L442-qDHHw53gj6u_JeE-nOFOryK6UvNQ7Vod4v1szyB0bB1EaSwlRMTU5Gs4ssApcpccBJ1X9_RxLTvFYz_AD51J4rSqDUxvWhR680NFDTM26Gtc3i4mDg0dijvDqISd_s4AZq6aPLVNh3wEEgZoZJH22g7IUsZ26ChlINVAr501i3KvhGi-wp8EJ0XFD2y28_VlOlkCN_gTkj-PT1CGp8thOPLdE9vY9Sht9vU9WndNxerOOW9Ew7oIlOQDnZjCmSdhBdawjKIfJJjei6dG7w7PMLYXqjzCfbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=GFVQGiE0cWX13IQsTJcVhsM2JGOcauyCrB161ONcNOZNHdy9Nh36TC7F3pS6l_LoxQEpWJAsRWhZT32f4R79msNCV6EMNxpwSzZdOXjPNe6r2WyuwuIxzwD_JVJgxt3POC6uU7ixMt-Ep469Jly3-XrHHirXJ_Aocs18sVDy4oTKJMBLmPhrMd63righEv9hS6Ovwa9q7JMUymOR95aUUj6CcSCd05tUEq7HdTkyvRj2L8vZY_4on1H_txZo6mS_msTwXqe6jJM8zRBjv8bYE_1UrGm82_HJMo9S30fIMjYnWpbd38gaNKVvonuZbuZyshM8llxIaMZEonvqt5quqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=GFVQGiE0cWX13IQsTJcVhsM2JGOcauyCrB161ONcNOZNHdy9Nh36TC7F3pS6l_LoxQEpWJAsRWhZT32f4R79msNCV6EMNxpwSzZdOXjPNe6r2WyuwuIxzwD_JVJgxt3POC6uU7ixMt-Ep469Jly3-XrHHirXJ_Aocs18sVDy4oTKJMBLmPhrMd63righEv9hS6Ovwa9q7JMUymOR95aUUj6CcSCd05tUEq7HdTkyvRj2L8vZY_4on1H_txZo6mS_msTwXqe6jJM8zRBjv8bYE_1UrGm82_HJMo9S30fIMjYnWpbd38gaNKVvonuZbuZyshM8llxIaMZEonvqt5quqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeWENSomaAUWZzuCsfY1cBTO6w1ynQ-tv53bhj8cEzN2SD2jzZcjYdBKIW-XA1izei4Wm3vhlfabK51YcgjaVn0rjmlE46Bo-L7f3WMLvLmjclu5Lf9YXvDZxISeg5lVkfrAZAvkJrpFdQU6KeVhGSgQjWlMif8zAHAv4N46WR7qdGhsd9B-EZxm2p8m3GlT8L4k3HD7fb_yFHfQ-Yl-O-jM1wuobgyeiEzLHVs3fN2bEWLml7aEGZZQ-nMQ9ny2hxE8OvVqR0x0VhoVFgkwGQfCbhczMxBO0HluoUWBqvjkZXXGnFLiW6_loD8WwjyF7qNGYlI6YPvz2yzfhCvj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور تریتا پارسی در آمریکا
متوجه یک «طرح پنهانی» برخی نهادهای امنیتی در تهران شده؟!
معلومه یا این طرح رو خودش داده
یا با این نهادهای امنیتی رابطه داره!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5224" target="_blank">📅 02:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
مایک والتز سفیر آمریکا در سازمان ملل : جمهوری اسلامی با حمله به کشورهای عرب همسایه‌اش اشتباه بزرگی مرتکب شد و تاوان آن را خواهد پرداخت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5223" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
