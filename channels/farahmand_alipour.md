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
<img src="https://cdn4.telesco.pe/file/NQvxoefCyNHsxAdMFoSUUiQn7dEeOULtu6x-5LPzHeJdXXyQZOgefg67Ms2O7RIY8CAwShz_XwFsHCKkJrAnComUeu6E4hGArWatRH6gkx-peJm1iCfldMTsfQ1xONhjhfj0XSe0OuTCwRlE4XuMblB_XxQBLJ0EQb_HcVCqJ0pzhbxe0gFtQg8F2ktWG1vPJdmRm71z_fCqY7bS-zRxQcJy4FDBjINU88YQhvyloydKF1ndIUN6SphBt0rSEkxIlRF-609khjJ00THT-X9eC-H4pUIH6k5K0_KBc9OPTtP5oIlDK2Rovcycf7IpvZF-VEng0oMzpfQYAf1_j6mZpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 14:32:04</div>
<hr>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmwMFkzu-ZSmk4eQ_q-FTjcm_glsTaNlNPRSYlPCaUUtLBoF-IJNKGp-sf9FSOOLsouKFU2vPEaVYvIHAib3LtzaB6oLQ-xflSapqtdiZHKsTXbq3t16E3w1E5HvYVht0HNiqo60uzyaU0DoIENCWeBCgkrrHPYFEfveTAA_R40XOt9soH3y5p6l51eA4F0NGm8CGY0_hkyovYL8kWT4Q3dn7-NH6zhCpeQoJi19eReZ3FeFFjaDmgcgFzHR5KxMxV4fBwXJVgKtBJjxC7spXNbI-rA65CRFyUztQjP1gGPNETDswlbtsAiQcvhzqWGN85zRZAhg7xAefurpXCIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm9QMm5wHRuy6EKHD-kdwjppZbtpx4S2POhcJyiT8bUvPZ34IUHAv_Zj-hp-I_5JMWFPTGdo4NsTqxmdc4YDdX1E2h73mwMu5Li9HahAjfUIJu_XWUKg2GzNaWooUIHAAQTAzFPuPoYKKpITSbMuzepE3vWludCRpj6JBOi1nJE5utAuLDBnjJiDzOqj_tGnxoSwWDqLroogjy1xH-3PvwQueGTBZ05C4CHpXBz_VmJWJr0nOZ522pRuFTILguWY9FywEUfScUk2JtiJotQ1R9Z6bq4w0FAkjGCqYH8homfR-GW4yBw7SCfoIKMMiLTHMbeLcH3pVm-g4QHumdQjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=KKYd_1Lbh3rBpeoSE0h-Ohrdfff5wkILOdWmdsUim2tKBGy1h2EWOpgA9Ib2as5QargejSnO9rMdgQqango-_w-VLNXZsV0eOzM_cTT72pgPCoXr7iVcfFFfaK9mSYbRRi6G4lp-QksQy7TQisEQz2rnmm6sopfmnPjPrdhbPCkFh-zRSFeWBqAS2YnXX-Bnf7bhz5t6A0l46e-dO8VrnNaUclKGB7od6DfJkBKtJYFut-vfITueHfOJNERcOjWsBRnvf2RrUmT_MP34FrZpbzB22wkWl3MdiRgche04S4z5gXkD-ZA7helgfCnm6W2GcFd20xYa4uZbKJ8eqSKIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TmaYvA0vaMIHGmdW3_JhFhcnVZ_G09WRy5NQelnzEFkgXi8y7eU8ttmlRd42UPwIcM6-1VgDaySv4rXCtS8Z_iAIJ5tQ0aPEmeW-D7gIcaSrvPB74P2m8f0CKE7Sre4YlREw_B6HcHW1m8S5HncVcxQBctyCqothvpdt6ntP8HRLLffd4p_mOrk0FyMRBSrsJdpyCXyE6mCXPtM9tgGiFoJbXaPLFXqodEbYliUqqRnzmKZARIfwC4jmzrg1ksN6ZjA66LEPK4Y9BepiPS3CY3FZVCf1x3g4uZKMHUngxlGIwBaL_dVcgnrknA_YcvyH9XdiRtVAmD19zZZqKDZevk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMq48--FZW0zdOT_7Xr6Tm5krYjUk2z_ydSHiCwXiNRVZmHrhhIs77JLd05NoOIpvBnHxij5t9zg144gdzwZHn9V9CKOJKBFp4_72mI4mG_V0s4pI6rCf6WNPNZVdZ0I61aseaPauzuY5fyn9UTRg45g9OEClnhEzC2aslSXLrukWhTjjZKw_ZOwO8iIuQZV-lJUgFy7E2eeN4JItGvffmkBMUHgjcKa1yq6CUYRluDLeLvkhcnw3FrjgW58m7_KF3b-oB7lDW0vzSCsHuIfCFAy-SirPQOj418ECx7ve7s1fvNyN6wAc3NdrynABRtZqcVOiQ22LK_a3Wn00pF-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgYg2JU3I67lEinmLYqG_cX3AN7VE5l3tU2pnnlNcRjIwowkzmb5FFfznfEGqGZYkhuzGPpAd86syFzSLBJvb0ipaHIiRCNQvfjQxqJ9uueJeoI0iBgjsgw9Y60JWqHnk2cHHAf_iAl7btbrf0KwRpLEl7-djFaD_b0bSkRQ1lts6rinQtgRxMSw6cCdymEXm9w_i0tsz8jxBUCxFcS0Zxj6EgolJioBp06U_lEVdPzXCaszxL3Hf9V5lZCCZCxJ2fe9f3itliJpegfNpSPJE5zwEbP5derwX2VHInD-Rh2-qExtuSPUNlXK-zvPOqRHWUBwMunKNVtJuURBuVq_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biDF4_5s4aqTwN9HlrQL_m0Q-bepBO-aI73Eghxz4RSPv1VITdu4LoUMunn0Vtz1BH9EiX1Byb9ZFC2r-6cB5gutrgIeA4ovEuf3kU0CmxLdpmFyiEF1U63T0cp0VOgimTMs9Dupb9ftwKlbiD1bH-jCPqwGx7twFXjGfO5oWrvrYM04IhPMWEtRgOO-vNrKjh92t8YDeZYs0oxFnbM3OmhC8PSJxqJ_8sisjy06sq7NhYgIQS4cc__yRFfzwKYBj60IUmb2liGBDldF7vLK9FfQWMp_FAQKalFQbg49SKQo-Vfsz7IIsyqkMtUapJGMvOQ4V9qpMa-OcoSGEk3yrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrcgGwo9_8E_UMtXGwqIP_hRftqShG3LLWiJSb7cNuOMq2cggWVBd-iy42hQMFBdQxbOIf_U_ZK_nesd-cv9U67Psw7kk0QaMYb-0uKGhRKY0r3g34DNtDi8NfFora03Q-KG8etE0t5QrSXLmEQpMl3zhTnzixAjVvbdPrNZM3rzZjbVK2jKImyHI237uVnNA5bKET6ibjVHX1tphmK0koFwAeYRD3txLog0soaqSA3exwAw04wNAg3TSNUUrD-cYl496ZoQJXwfejAhCYUwz4x5_UxcGzcy1k3c62KQO3EUdQ3gzQE4EDBIYpXMAAglAWKPeevm0QmTiMpD9_CJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=dW6WSfv0NQn8TPe9u8KlYHhS0EKW4AjeXvQzO3wv_KG3Wn0ZhrRmhXdc9ZpwbZftmqtioOC5-UHXn-5o7h_xYHK_izlhKIXuv5QHDphNHQz8K91h9Mo50Z1iqFsqyRzRI4wBoAtTX5vRmkHgw9jsRsKkOhHYnF1rCniZye1SKgQM4u0jpc8qYBxPPag30Fq9fRngVBJVA8A_2cjEF7kjsUBO8Th2_VoYbOgD4VSiRrKFMLFAjry0wnD0Ps-G4aSeW32Cpw0WpXBriglnVqExdxUOu-5ghVMC5RniwbzSw7BYxakoIp582mSqD3ZM7mIdJoc944_5_RkdyH4fm-5m8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=dW6WSfv0NQn8TPe9u8KlYHhS0EKW4AjeXvQzO3wv_KG3Wn0ZhrRmhXdc9ZpwbZftmqtioOC5-UHXn-5o7h_xYHK_izlhKIXuv5QHDphNHQz8K91h9Mo50Z1iqFsqyRzRI4wBoAtTX5vRmkHgw9jsRsKkOhHYnF1rCniZye1SKgQM4u0jpc8qYBxPPag30Fq9fRngVBJVA8A_2cjEF7kjsUBO8Th2_VoYbOgD4VSiRrKFMLFAjry0wnD0Ps-G4aSeW32Cpw0WpXBriglnVqExdxUOu-5ghVMC5RniwbzSw7BYxakoIp582mSqD3ZM7mIdJoc944_5_RkdyH4fm-5m8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=TfKdly03l6gPoSfZNbupiU61GcGmIxVwHpRcUdL8S1MIEAExh4l0-fKKOZeymWq9N5xig2c96jCi1gl2FbvbQV050uIUXUkwI38yCty0oVojrmDndX-7VUXgdsPXOT12gGiE4Tto98jW4mrfX45QaSH713CFZXRlR4ASc31FjwIEprOwyvZ-5DxKG-8lp4gjUVTa9L2uzAlDuMvHn0dbxVw4fykpa-4S4KZHnhYqRdlwBJYuldvNSaj9PEYVpfmf5j-4P3K8xUf9LWWHY16Ce7gfEAgmZYJQcssZo_ez49fGaVIxRcDR3tMDjFtT7GWtXDIberTjDh8AOfBY16TztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=TfKdly03l6gPoSfZNbupiU61GcGmIxVwHpRcUdL8S1MIEAExh4l0-fKKOZeymWq9N5xig2c96jCi1gl2FbvbQV050uIUXUkwI38yCty0oVojrmDndX-7VUXgdsPXOT12gGiE4Tto98jW4mrfX45QaSH713CFZXRlR4ASc31FjwIEprOwyvZ-5DxKG-8lp4gjUVTa9L2uzAlDuMvHn0dbxVw4fykpa-4S4KZHnhYqRdlwBJYuldvNSaj9PEYVpfmf5j-4P3K8xUf9LWWHY16Ce7gfEAgmZYJQcssZo_ez49fGaVIxRcDR3tMDjFtT7GWtXDIberTjDh8AOfBY16TztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJOD1P6G10tzlu3PkYekeQXto8PCFVweX5dDkL9pD7PvV0fqlbKouXssMBFpO3-lSm7vZfpU7Gzli_v6HiIsf2Wve6B6W9ql8CsDFc2Ejo5lE0k63JVD5Tpxk4iBM141GTDYh5r_HzhkfKGizTCE6pNC3WHubouW108FSxGE8u9MGoz8bQJt0sH3G4mANSl2GbKJJWbMKUK2w0i7YTGJlGbs2NTehhcZiK8QSaZoOEyVlGQF8rOOcJ7l-S552nXCkyOkB576B_yisL48Z78HTaDCHSAdKTd5WOHTxhSAZl7TEvY9t-vp5cLyOKR7G0I9GvqP3G-DzOk-djh5T7A3dok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJOD1P6G10tzlu3PkYekeQXto8PCFVweX5dDkL9pD7PvV0fqlbKouXssMBFpO3-lSm7vZfpU7Gzli_v6HiIsf2Wve6B6W9ql8CsDFc2Ejo5lE0k63JVD5Tpxk4iBM141GTDYh5r_HzhkfKGizTCE6pNC3WHubouW108FSxGE8u9MGoz8bQJt0sH3G4mANSl2GbKJJWbMKUK2w0i7YTGJlGbs2NTehhcZiK8QSaZoOEyVlGQF8rOOcJ7l-S552nXCkyOkB576B_yisL48Z78HTaDCHSAdKTd5WOHTxhSAZl7TEvY9t-vp5cLyOKR7G0I9GvqP3G-DzOk-djh5T7A3dok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKBU5y3Z3afWprkNxpraMDOcME0IX7yE13w56IkpQGnlGB5-uIww5ahSHO7CfIufOhZOKW5VKHYQEwLSoG0RziarHR50Pn3P7UkimGB1FtxcUOqIyqOD4R9J3UMnvKfwo-6F66v2viTHAwbHQSr3qsd7dIEsOIeUAh-VnOM9X4rG9TI0KojiYiDgo940-mP9yuVDYQw8QrgWkNUw8PzZ0IJF8GxDxi0mQVvHnOF5ee_w2fiwCdOLlk0LI1iA4jRr-q1bBHm5mKQK0toa-eGD2zdw_sZztYNTuZ-nL59Mw3mXYK0SyyxC3ZVkXhcMNIiZp279fgyYbd3V7vbTb8IsSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No99YXS9mt5HT919aJlRrz0DN7in49Sx8w1Rhwnq1ygdrhMSbqHExWIjiUNTn3q6-MGrXTKRtd_yGpaBZzfus21DysTkxRpLxOpNNVClim2UZRLLqJk8E90nTP_YHTzGy1R6J_q7MxZmTuznWucAq0GP9Cwa18soQjXd3OE9IIqflGNY8vPJ8dhiQMgc0JLLEMdtaaci9X8BYumCtFwdgUvKP8HsdHwrcx1xuTrD_bs1Mo7yn_b6AxnANqC7zyrCFlrkFtOY7-oCbUbF1kQNjoF7oihiEUwNHGnnH_WJabBcuy2l5jnZc_542_Hg7aDGLrW4LZtF-6XFsPuUvQYReA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=ZKLeY0e8rTopTQUQAfIeNlvC3aYzTHzYsKZfc9iflUqGbuTHs3NKXG7cCNLSpJqx6aEePK5WYztWUtH4hxhMD69ORjTlPgMXYPRZWS_e7pBvq9ESUBG4nwaZn1pIqcD3QDyZuygrnvJLmtGrKNHklYNjHqAjnmFbj7zf1Qa5Ul6IiErXhOtvPgkEKh8_6-FH_Vgq0fSnEujqprjHoh7U_U60N6nKPfZHqmoxWPsj2piZKNTpHfQVXQmWL-P9bbe4ueHpl_Uw359033DWXzYuwPrvf9D4bOhJFuUWjLFUD2poNilpdvsigK9uMO60PEkNNZZfPzRUAHg6XOsdXuXDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=ZKLeY0e8rTopTQUQAfIeNlvC3aYzTHzYsKZfc9iflUqGbuTHs3NKXG7cCNLSpJqx6aEePK5WYztWUtH4hxhMD69ORjTlPgMXYPRZWS_e7pBvq9ESUBG4nwaZn1pIqcD3QDyZuygrnvJLmtGrKNHklYNjHqAjnmFbj7zf1Qa5Ul6IiErXhOtvPgkEKh8_6-FH_Vgq0fSnEujqprjHoh7U_U60N6nKPfZHqmoxWPsj2piZKNTpHfQVXQmWL-P9bbe4ueHpl_Uw359033DWXzYuwPrvf9D4bOhJFuUWjLFUD2poNilpdvsigK9uMO60PEkNNZZfPzRUAHg6XOsdXuXDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=tzG9rqE3NZRqNFL7I58zqYNVmh34E1LL0jAaMew1ym2NIKJYHX9Cx1d5RtV_xmwSApIDCTUOKW35dgpuYZol5zJH_UgY1_d0IlGos1DQnBV7maw_ZQ60HU9zFG8k1tLwYf0zj67Tg-GeUQTHPLcr9jtayWKufT4lzT1XFtbxkz4tMj-5j0SkWhwvHLfHl8QCWkm4Ggh9M-3fA_g1Adow7jfKB4wlJ6NT9CfJNDuVJCVjJZX78Ve2GLEXDcNF5OL1Rc4HF9oLd2LN-Fzuxm4y_nf0kRTYXUVnZ8rp4QTrClrb9FchDCmX0CVa0t5LqbW_-yq0EO6KubZZD_EIcmWeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=tzG9rqE3NZRqNFL7I58zqYNVmh34E1LL0jAaMew1ym2NIKJYHX9Cx1d5RtV_xmwSApIDCTUOKW35dgpuYZol5zJH_UgY1_d0IlGos1DQnBV7maw_ZQ60HU9zFG8k1tLwYf0zj67Tg-GeUQTHPLcr9jtayWKufT4lzT1XFtbxkz4tMj-5j0SkWhwvHLfHl8QCWkm4Ggh9M-3fA_g1Adow7jfKB4wlJ6NT9CfJNDuVJCVjJZX78Ve2GLEXDcNF5OL1Rc4HF9oLd2LN-Fzuxm4y_nf0kRTYXUVnZ8rp4QTrClrb9FchDCmX0CVa0t5LqbW_-yq0EO6KubZZD_EIcmWeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=FrlXG54wGfXnog885zYu9FOWkUbKAX-TY4Uiv04WWAO3ecj90sc7kSPWPGXhg1Iu8-uSvY_sTlAKa6pwUSZnf_KWaOEPE_BUFrZYnnOthHvc1DxiZebv3AY_gi7M1jd7eAzA2lsidVV4bzjkTztJtWHcp3SdEOCyr8lctgCzu4gvz52dezfRhB5orCnyAIsNuKnpRpfmBhgMCDNs0LZsXKvbab3LC2cNS74hPtZFtvnpo2CtE0wz6-lvH2PIFAcElnrLl6MDAv16cfRd4BYyBB5azw5QJn2Tj5ePlFqePwSUCh6iGtDCjW6-yH2K6YwdFr61y6BFmKEy-cBH27DCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=FrlXG54wGfXnog885zYu9FOWkUbKAX-TY4Uiv04WWAO3ecj90sc7kSPWPGXhg1Iu8-uSvY_sTlAKa6pwUSZnf_KWaOEPE_BUFrZYnnOthHvc1DxiZebv3AY_gi7M1jd7eAzA2lsidVV4bzjkTztJtWHcp3SdEOCyr8lctgCzu4gvz52dezfRhB5orCnyAIsNuKnpRpfmBhgMCDNs0LZsXKvbab3LC2cNS74hPtZFtvnpo2CtE0wz6-lvH2PIFAcElnrLl6MDAv16cfRd4BYyBB5azw5QJn2Tj5ePlFqePwSUCh6iGtDCjW6-yH2K6YwdFr61y6BFmKEy-cBH27DCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm2XzQQ7vsd9JkCXcrbS7SL5N7OxStFBFwnVYTY0EemPSd8Rb6AJBPGAbvggXnvBpnRFkyo3CmJ90durfWgZsqPv3zeMK2TApRbO2liJO9GF5LG0gxocPkuuzuOrL9YbE_8mLxSgLo57ykPo-1ARb_QcHEasZAoJX34moxMT1PvGX8DpBMN3-wAEG6YnmavI65--OZG94EIQagcpxyIxLXFUHXnq1TV0GutBDSIl29aa7wDgvoaBkbKzBMIZ0I445-ld3ajhPugYKF_UAhQwX8W6DHVAMAyd4E4cAung5Rb3i13gLG3LHng0mp2WygVnf4GbF26X9v5BEeqLc_rgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNxPlaKj6YwN7tDXHq3Zk65B2fxpKmoT9Q-N6FdI-mQSU2YuLLfT4XEQoylPzVpO5kqVU4IqlQj0fijTLa2ir53kKV6djOomiNdxOxlX-g-ypVsrgv2Adr3flvuomol8OocPSTkjnmEkH4fTl0Lxu0-pRE_N5dNK2vf45qkg4CgcI0m5Ufdji-hHJ8YB2p2NwgjtocR3XR-6RtgSQp7hsz6NQYyQFbS5k1hcGG5434XwmsDPCazB_VbY66n7TrTc-m343AHQXX9M4XtJTO9g9hHsHq_VoCU3_87cMRibgTgd94zutM7ogIZxhbJJb37R8Rm-PYKwTg0UIycDqJUtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe9tc0PAfTRPE4ks1Hb1CveHtMa-fONLCXSzg7JNxgRK8mC9eBpYiJefRToY9Mtmsrx6eXCIeTePZdLAu17j-YMxyLo-3Lfz2U9CloMJg-ekMko9gt_jmzjRweQb1smcUJWtL-Fv2UqLX_svcdp_jLUFYCius_ILMFKflm6-MEWTJsHc0x_sAigZI_94o7rsVwhZ7kt8or-QJY_hvbvzw9OTUz2zjAUm17PtloK5WvWGAT0Mdzxz0vCAU1_LYtH2xjBFPSEKXU81mX98qfzigDfJTYz_jl0UvwrObqciShM0rJFzLuDKQEEinQp_zwN6IeYp43vh1stBv0y9RHsADA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mrl1tl2z0vJYCPqd4ZwEpI9GbjXx8VdqtuhlCRuZArpAS-W2OhgQCiaGHA9vyFck2gl9cJdgI9DFGSg0eZxeNKKuXUMLDKkjxyhx92sk3PkhR1S2BVWE-npr9LTWnJhBxXcG6U3vJyFe8sgcYRbV54nnuYzUv9MiaMn_Rw8NQYRPTCN3nYKx6qEijclT1rwmLIV-39D4ZEYOThSf_rOZqrXYzSN1-iXk1GbQfv_j0WS5TPahdvIT4-53_GkMJ1Cii1vJdAZ3--iFNn6DhpR32o8-J7yqjpu_C3Mn4JRFmzwUVdXXs-UgNI7qauP_GFutty6nOjbGjX15BCtLezag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSJ2QJEbwEoJGyaoMV5ZatdOxYqPU0Ampv674Hl6IPJlgz-NnuGfGyLQq5gcA5i4Dhn9x1dCbVXlmiwqkB714_deXyO0N8_AN-bxxH2cSh4HWux3MZJNE-9RKpLXzjFlL12uP8ztcmB7hk6ZDuD4FN0Ib0J4fiY2SRyprQ4HzL2qeYUW2eUXcTFr6LDv_siUpyKx65Qc0BAOJjsGde2kOAe0bhAOyD9eAWplJ-2jOMz6XLOJRDUOB8C3_7Nyx421rzwoVnEUlD188HT59VrfY0kG3oae0oouq5Yhc5pEL1jOEOooKGE2Elml9iBbjbrlgv1AMKjdkADtlUtarALalw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDzhM8E7tZNK1ll3yGKNMzDLcntSqLiprpWcj1bNlnByzCmwbEWywKwjYbdZUzSTt_ZmtR251oCXeShSMN-UJLk_uvmHj99ftXJWMKQP02QM3UOf_EW1eZSLnTR5qxHjlRR2V2RxUFjDri0-smIwlVsjqA6IgHf1-QYMLlJoNh7jsLawuotvnjEFav-sxy9517dVLZ9uT7ZJLfslJOp5tAGyaRN7SM1a5rjjkVsT4S-DOtPgTQ5byf6q-7wxxUPIYMi_kJlYIUygQJwZd2dYh1sizGnpCLxCb2ajYA1Tk5suBvRzac-3guP_AFH_GxFRRrXoahSjrcYCPpmM7mLypg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvw284Y3FqrXEOCf9Hrf_vn-OZViY8LIk7tlbfHvxgz9xjarEHoiX2hB00IYeqdM-oDDOQFJyBDaAK2ZqHFBi7aPBhI99XuDIDijf04AfD9wNzZDnUjig3OP0UAFUlf758KTrIoycs4O8dVolDK9ChJmdQdhLtGKcIE3W3LjZ8e0BHR7R9mTFlRJzFMeE2iYvUdHOsNGnc9iaBvSzRWuBV3wPq_CySI9DXZFNHu2lj0cpfXBXQ46RU8LvWDfCNAJAODXyHwIAJBFzBk4BwlR-FLdD-CV8T4wu5g9bYVLizRczfDmzu4AlhOk0TEgQZ_BNMMNMFL86H7L3enKbNw-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=OSVqpoFMssw-KH_bnS0-IF0tx_ySqYl85PtHC4mnJNJjeTSXkBsbouSbXGr5wIkdGeAEebSjNRlDKCrqP3zcY92LOP4zTeB5A1YRwPojYJpc5JLsZcOQIkZ1mAHOIai1-2myT3lLiRNxBXiNe1pAlwG98VIQFqjarimI1RzCoxj45AHYK97XRgG1QDFt2npcfUIkaN2cRzvcFzLeYgs1DIZHYdOsoqyQxki_GD1ZnfvKFL2Cbc8EzJVfkNbXKRqsmDvHUdJrqZzuHsxoPCc6hHboN4Y4eTYwwxtsKl_gr2_xFNVDSwitJ_PQCzhmrWmaDhx8sdZu6GCI4PZ5mO36cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=OSVqpoFMssw-KH_bnS0-IF0tx_ySqYl85PtHC4mnJNJjeTSXkBsbouSbXGr5wIkdGeAEebSjNRlDKCrqP3zcY92LOP4zTeB5A1YRwPojYJpc5JLsZcOQIkZ1mAHOIai1-2myT3lLiRNxBXiNe1pAlwG98VIQFqjarimI1RzCoxj45AHYK97XRgG1QDFt2npcfUIkaN2cRzvcFzLeYgs1DIZHYdOsoqyQxki_GD1ZnfvKFL2Cbc8EzJVfkNbXKRqsmDvHUdJrqZzuHsxoPCc6hHboN4Y4eTYwwxtsKl_gr2_xFNVDSwitJ_PQCzhmrWmaDhx8sdZu6GCI4PZ5mO36cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOkQu-XMqL9NRunFdVAJpYIBOA0ODahtNE79exWmF5tWplrDFSVtO5mGyEXqiiM1r7m_DK6Nvh4GfeGvOFkb8P01MMDRWES_P91vhAmd-HNUjxWB9QxecydBpB9bCi8iWEcshHoJ1XuUXjVMjzgEKMEr1rPz0jqFyMvsrzEydaoRVGcYp_bdXGP26QVs4YvSdr5xA11ugAxGPSl3qA22iykLf6GmDEfgzH7VDPn0FF7hAjqnjvoVN8vRE7xkKQZtszN814814qaa1j3cDyQT_vt06romH8jGZb7jyBA5nwqMUdKS2byAiNyvGQiPreH1NcRVNSSNxQzJoeTd3Upetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuFbL9qWFC2BiaUKj1VZMhRNh7rhRRFjA3n2QVXQb-0u2ig_vz-dNi6droCnd0DOXuNlD9LL_M-nqJrLujkUrMc_l_knnk1SO8HEbAxIa6CfGAO7MhJNlbruiYgPJM8pVl1H6ktCOdmXM7GFNjFuhQSfXbEGFmb4NrVEMzLhqvk2iEhOmcG83mdnf7NC22XBwgFk_KEnaGqkMVEgS1TcyAzfn5o7HFi6_GLL_y6jP8qipoZVXQnldVjIrQmjOV7zskujoHrNjMvbFf8SjlKzN5xLinL0O0KBzcMWFZsrIUHJdr5WfTpLmkMyY9mQ71NleAAu7DPVqRAroITvta5bTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNN-8LC56tSjok8GedR3QyrTOUD8h5yDp8DPyOKGPJJH31lWBiwUmPTS8IEa-RvHpiuFyXoqrNbUMe7bud13T5dZ3tIsfsHUFuZLXaqSGzran6jUs2o4fVi_n_MeyZPABAY0219ltWAbObW9Wu8eQ8PmLnDAuaAVr6wFlfj7WjxIXM30PKn7cAEiNHopmWhTbJgisShp9oy1PI95dT6-MxaHjiceLHRLIrG0aQIPL56aNvtgdbOSZ6b23WFZAaEZLnYYYf6oassBFJQCzd7Qwhfi5DuzKYs0EcR6YeryXRcIi22f9x_slqsv4ilWMXCJRmQq3rnAGJd_7Fx4V6D99w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-oA12N1gbgzQr-7aNO_45ok5o83XZM6E1zB8vs5AW7fMXYtdmJVnWu_6LzFho0Rjbn9V6wRfdoohh32ura2fW65i-lSRQTC5mUYXulbcCNdBy9k46bsjPckqNLzhFHRXVptRU1FTCY1WC1quXT7QwXsocXoCCM2CVVpx3q9NewbJpAicIcmzgf3RFewkDIkT6zIE_WzKXJvHHH_64rGWe0MhY_btDiIL87VIbR-gaA5Y6QgkR4kv0VKM5l-9RwFfVH0iICuAZMvTHYJ_KaN3B8rOCLbsDz5TvG4XNW4LHO-RsPUkZHeTobEgOYPu-Abw1npPA0XnsfZrzxKb7xhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUZaEyQ8FTxLD43wES5g30VSIocloJoRYkTofG8F8t5S6YAyxEqRrSzZAB45FVoZj4WPN5Nrq1EARiWPfUUATaUSVVgvryGc0pviCvpukHSsahkU-GpWMldUDasa3Jlj9QjbFr9wITQ2h2TZGfgZ4vijt87cJY2UrQGrM2Bn7BaIf4P-2cNbwa_I45JIfgrgyp0v_Z3MpuZmg8OA3eL182I7g7RfZs3avlrsRqXbMrQzKOpN4NA0xlBPwGeXamoeWfJM7QoJvJKXePKqf-puC7NvfWVUknWx_-6ldlRVglXQEdlBZGw6VNDe9kCdLHVaAM18cQNxrMQHH7cuWenYBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8zIieOSPHGSjGWK80ZfTRmXuNWJFUCBR50ezJUTklE4qVZlUs-_DsgLuU-ZHYEKqsTrzNKiUJKUUESGwb0mPZeZLNIbeRoK71nbOe5jWY1zKv46DWSUW5LOU7nLzX_R3VOJUUtq6hnnQLxr9eKHH247nwuyFibJK2D6Si3h9Er3P1UGTif1Ce8eCjbeu-aE_NAFvJG15tkcIe5q4rtHbJ5y5RRyz6WnxTb7gAkMbJ9a0bRU_yM134660Eg01o1Vt8zPX-BXJQSXu8M-gyWuY9yHsxeMc06XYlS_BCHL2v8Rm2lFuFTtYyFm40bz_i2qBx2oJfuafobKTFMycMhC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ciWdDynlkap_akgvgMSjD4412EdzlLeIf4u7jypfkCQXkaEeZrYt5YLyu0N1px9x-lOojFM1IoFQCWH__QtC2FFUdI3Cts1QgFyWd2vRATWYYef4pCfgSR43Rz2GtJS8LN0HSPDxxulTUDooQIV-tkL4kZvoAJsgsV--1WslrogIA77ITNM0hFYbbBcUDBhz4r989XC-0RUDVe8yQl-xp_9M7aX0UHYXxeDTb6LExcRlzGpozyO4QV_Mzaj7K-NRKdT_B-vdDIcRRLJ5vQCYzkq7cCY9vKxtp30NkUIkdk0w1-UBRrVyn1R1Q8iZtsvSv41CGLOe9yLNDnLSyBJTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nweHwQnEel4L4iwiXfA7XyAseq9gEqMeVqSTg3AxlbM5x4UVIKuhtDZZS-AvDPfevM7NlmO5t2IU5JDHTV7X7Z0CPh55di4zqefiKV6bC__GK20kE0rHvtkEkb8hsC_UWdK2dPgjMPLZgjvvnWem6nzwPySj1ebbJvnx8TNk2VLz8qgn-xNMocMsTFmoJkP_TMcncGE5GmN8pNBDac75WRupYwFlNVIhTlXgVyUDBCNUzM9TsCubQ9EvgCvv1g936wBI31--Ss1zbY-cYA_xV9xbOzF_X5ViI6UfdD-RlmhFSf6TokkWlH7nUnQ2ZcR0d1pSueMc3zzbd8MnAGKwKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=FQf6nzyP1H4sNvEE3uipx56ce-mwSkqTyZ1Cyep5WD2JS8uscHi9rzX6i8-VlHgppK49yZ2SRCXPafgeqvTAgwHcx9B2e5j_wuhkaHNEHIDXxl7K1wYHHD2TLT26rj7GqZ3djeon9UoLHN9j6R7jX_lzg-C_nzYzQ8Yp9-MIW-6P57SzVql2gn3qatBgR54INqm8zr6tnnvApQbzJ252oPFxuZV2ROQziulu2j8GoVDUF3w-V-K8CFCYT4unVd6Qjy0eimz50DP9NzePj7lR6FNuS8712RQZgjBu9v3BN81a2rvwj8o-jd_DVxeBF3ku01-dB7iXgX8BI_NZsF3TeBy308wVDoMUVyTUmYpJyRt3C104O4OeDxUPm0_80KTlEIIjaqcMwZY95WHAWpoMyL_pSHa7Frah3-k0aGhMr9LXhToMX4O7ZuN_wvLWF8QLSm9FcjouqE_DAJa9gL-jTqbmIrJlotozC0XgaSJVuR3JjYRZibyYoRkxNuFg6baW4flxGmqJdKn_cTFG8SlkYmBDv03bZJctSsKhBEQ3pl6Ow1dAMADDY5B4dwyJn59QEZEAENvQ9gZZsj7ZAudQfa9H7SOMV7yrbO9BtveKSxsf6SVP8EojJhfelx_JtS3Tc3iOU9nrYeE7mtHDsIEYTVD-IwUNs9joqnldxFxODBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=FQf6nzyP1H4sNvEE3uipx56ce-mwSkqTyZ1Cyep5WD2JS8uscHi9rzX6i8-VlHgppK49yZ2SRCXPafgeqvTAgwHcx9B2e5j_wuhkaHNEHIDXxl7K1wYHHD2TLT26rj7GqZ3djeon9UoLHN9j6R7jX_lzg-C_nzYzQ8Yp9-MIW-6P57SzVql2gn3qatBgR54INqm8zr6tnnvApQbzJ252oPFxuZV2ROQziulu2j8GoVDUF3w-V-K8CFCYT4unVd6Qjy0eimz50DP9NzePj7lR6FNuS8712RQZgjBu9v3BN81a2rvwj8o-jd_DVxeBF3ku01-dB7iXgX8BI_NZsF3TeBy308wVDoMUVyTUmYpJyRt3C104O4OeDxUPm0_80KTlEIIjaqcMwZY95WHAWpoMyL_pSHa7Frah3-k0aGhMr9LXhToMX4O7ZuN_wvLWF8QLSm9FcjouqE_DAJa9gL-jTqbmIrJlotozC0XgaSJVuR3JjYRZibyYoRkxNuFg6baW4flxGmqJdKn_cTFG8SlkYmBDv03bZJctSsKhBEQ3pl6Ow1dAMADDY5B4dwyJn59QEZEAENvQ9gZZsj7ZAudQfa9H7SOMV7yrbO9BtveKSxsf6SVP8EojJhfelx_JtS3Tc3iOU9nrYeE7mtHDsIEYTVD-IwUNs9joqnldxFxODBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=YbBdcvjNhkHJkbxyq0zw8fkRhDhEpbyBCxI_9kMR5SFd7S8BsQwAVlrAnPbX2wZnh4k8kCz4D_D6TP1dpjSCudB_pZgVzkB201MOooorNWIezGTnzhVYw9bZiMePztomFS745cn1m7uNT_Z_RaYZ43n6agVcY-5dYTAfH3F00lzgldZMorSBy2ArLuHhJzrqh6XpfsHFq2KMKYOwYIjKMXA7dJdWmYhRnYA6lLcf_RobrkSCyQ50vzG5NIDsottL8UBJHDR5Sq4OvCU3fBz4Sv-lxMlGh10MgVmt0xiNVEwcqeRXY_kxlFHzxFe1yTJoD6etJSJp6dUQXbXTKtrndQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=YbBdcvjNhkHJkbxyq0zw8fkRhDhEpbyBCxI_9kMR5SFd7S8BsQwAVlrAnPbX2wZnh4k8kCz4D_D6TP1dpjSCudB_pZgVzkB201MOooorNWIezGTnzhVYw9bZiMePztomFS745cn1m7uNT_Z_RaYZ43n6agVcY-5dYTAfH3F00lzgldZMorSBy2ArLuHhJzrqh6XpfsHFq2KMKYOwYIjKMXA7dJdWmYhRnYA6lLcf_RobrkSCyQ50vzG5NIDsottL8UBJHDR5Sq4OvCU3fBz4Sv-lxMlGh10MgVmt0xiNVEwcqeRXY_kxlFHzxFe1yTJoD6etJSJp6dUQXbXTKtrndQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY2tKVT0VgAZMBYgkKjvhIDYTznaC-kHaXJPaqcqL7CHBAubUB7CGTBmYRooFuLZeZ5OIqpzepWtQkIVt7A49HOJrZEkFFET5zyeMCyne5YKYU-asDgCyrYr76xx7J7ymn8LgxnO8Klz-6ti7bLgfjiFmmR4WCPf19Sg6GVH0AoE9TmPymPwXUncVNWBx-MDKoBl5mia-OeAoxUmBdokZv3lDT40azliTUjQ_hJYotJumf6SiMWopJn_PB-J_aLfZfSt2LlQ1XvO3qvtUpWqdwsfhEQ7Dz6aTGgrMZ_debd-BdSaUmoUT8HPE0cnAqO9GCuKeX8Xx8yjPrNKvwntBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jey6m1ZLpV_JoI_EZXYPxq-ljID5KDqwp6IrveGN6AquBNPGKcC4l_lk9XIHCzeUHqeHfZiu5SyRQMio8Hw4ppzQEiXWCcL3FkSXh_sT6zMuoqqSCWWQpHg4HW4ugRrqiSJWSgaLvavFlXIJEe9-p2nHAw62suW8b_enUJJhAWzSZNomRIt254Gg2BIQgWqSiXH_bmLgC2l4kwSdR6ml3ep8ZdIPTKU8NHqhVYP-3IBhfmY271h3LFSagGyRlp2Bu1LBMXe6tIq22JgdC4R0T4WmWUxiuxis7npcYO4o6u2zs7d9bCiU0ssb4CZz_Zs5eewsAuQDEIufLmS-y5wIEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s68qUUXE0g4ZS-fbu2HUKve53Vw9G0q2090Cc9ane93OKpMxgAFNjowLll-C-bIErxRLl9WRuaR1IGvK3Efc5wUTknwxu70gSruDcfIbhRvC82hBzcmxUjyZfjGslyrYzsRy4IB9fcdCFpStUeGiC6RqpOqsD8-rdIAXYXpVIyhUItmUZWGlPYSVSj1LvWZEB421XUiXJ4vOcJpTGcZ97_JQVrGG_zsKgWmreLmbVGVqlCDf8SdgoFNODpM3RpJBdNUthPp6fjU95PKFlMe2hfXpOZqOAJ3TnSkMklot1dNf83dp8GV3tFpu7Nl5LMSnMcfGO0NXHRmJiUOKPFJh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw4DCS4a7Dmt02zUj4NfeuiMBNxbxpIDkXzdP45rdCLqTNOK7VNcptW6Bd5Wr_Ie0w9e0uoS8HqGKTgGhrg76vf4mNYCmRHcHeXIUNFx010yRiYKz54qbF4rO7lkdkR2cCmrcxTWwCUEI56tUk3xIwPaiYg-E5Vi0bVsegeYrGGqbcuyJbREAdVlh77NdeWVKqo-czy04lx2QsGt4TScN7zc508Y2KUbKSF_ZZ8dIFT1f_aVJiJcUfLGJ0aKI4nHhO7-WnsRbcsi1XOb__0dZdNU_gfwM_1Dahfs6ubA8GVXtht3jkZ-n1MlW_DgVPEkK1txEzI7Yfgj1m7S0e5ENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLMgmX7M4a7ekixG4sId9pk6A0oF11qweF88YoS8qQeMrNbZBCZGOOdBfvVCmioI-s8hV-CKKqn5j5MMoykha1CoL1u3T9IkcKyLAtdJfRMAJQjyr-eXCoMqdrK14l95i8FhlNy1J1cQgNCvi60ONuxUXjXG7hdtesHJ8cJJV4v3URxpsCEAVxE_k0-Tn69uIWZY42Jrekb8hF5lccw2PPx7Pgq6NZ_FcugcZt3K5_rKLos5Jeh73_fsNL4A7y7J2VrvWHJjjIN7MIZo9KphlaUJoECbZiLRzeiSHhzCEegxgoIasXqr_AifkSkeNwkACMxqz02zTFcATPAn6WP_kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwF_ynjmUu2HwWHrF1tJSQ76_xSX_TBLyhdeC-O7Xz_0lM0JHeBhY-_HmNnEXfIq2tDImfyYksZFivz93cvLhdHxAm4dt0iIIwd3EIK0d2K8IpErRau51DLf8dcbOeMU38U1-qGqHpaJ-xhKDyn_hhQRTZduXSU6nb-hdoFhSO4eRNdcxQow0g_5cdIHo8HuZEF6geASaTUnU1c4X4Rruk3h4v4QPsL7IGn4gykLoZEr8NzDdRbFrOnJKKOLqNbK4Ig0QQtAq_JX1naLUYNh4_Bies90hrqdilyHm33ePBpBzC7dsl59hdx_b2smmFOAY3IQAo9YYXIjOhhqAUv8oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU3sRhOnGwwEbt92BEAJHj-IH3MisJZQOnCAP0ClM5kfmsMt-Y4QjRzMhea-RGcTSKfPcUuXlzZeeF27RBkT0tIIKVjkue0u2c9A6J51QYxMGMQM3Cu-0vtXYihod5x1QxF9oGveMDlF5IBemPfwc3AzjkK9Kh63NeijxGR7bkJQjZiF5b8Qz3NE9wtrpYfXhtTJp8X29Eza7SFgorJHh_I4zSeBqWNZB6KyXQINzsjLcrW8QndX7I_VqoTYnSn1YR6ehsaL1spIz66rGZ7-IGE-DRFJUiixgs62pn3mSutetd6AgieYyHKcsySAL3YcWjQYH5lNSDX-Z4QQ2Qk9uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQQtbT4mXh16iNJZb_fzJSADO26eZGV8Va5DauZD-DuGq3wXhqtVVL6GKlDimN1zLo2V9J1ISY6mGuE1SrKVjCX4KL-YvVXT_wyoL2IgkVxn_y3C4NyPvIpJsXXc-e-qKodG6NJYki6Jf7TBcODfd5URx2hrd4GtFykMRKGXpcS0Jz-s9I2hnB8p9jD0k1CyON2fS5rfGApdOV1-LLHgtB3RxhQKMeWwVDTUGz01h-Occp-CggPb3IqPkb9ZPDjGRSU0i8mGNbs2TZM9Qv2qdBG5RTkkxFF-xM4lYf6gAe5gcFasu6gBK2x5dTgPeERmgs-ZDxO9W9f3PEHrx4odAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-GQL38mCNoHJTktdppf6Sbgi81lGYdSDIejBnk4Qngzej9gNad5EYcyCStqIzvp4WIbwq9T2tNkR4vFO7IAxcrH-x6ZGpSAFqzbhy30zBbp82Yg4MG0pFBcAoRSdc559Ca03mDyDtgHxDeQc4xwZpL4YhR3zGWDR-M6u4fCjKjkx_xeD35LW3fNRswv3ijwYpVjRlHZ6i7r01I1oW-AcTPIV8AHuqoOdqZYVjNSVDcKVP4wJluYlbRFl5-Fqrvg6llbTpbI_m58pLpsm75CHPewz8lBiBHdCGx3_fczYix1nlXq24Cdu6_R6Kn5okxNquKUR4r0QgKbW5wgFwQxjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=mzZQw_L-Dg-bbomXF7uauRbOfYYiBxDmqE9f8FCZ6X5QXv0QN3JsXliwia6x0qLuGSJIHbqSzKfdq7NTvd7laxNuWpMp2-OaEeKWeP3byC0b9MJub8YpfBljm3TUdIFnFdpqojPiX19HIFDQHRBQ5bFF5Xk_gKnhudCmzIJ0Z_aXud20X4AycNhWSovoN7LEa8aREWBHFCQ-DLKaOeGQOAfvV56zhGH8V-gMshXxVJpMZmamg8YjDE0JaBt8VxYqLX6WAIlxgcOHzPqsirjwAHOMd407dr9uxxYkxXPPa0QYelW4ssddX2WY5Y3ZCuuBE_snsbVJXESUl7Rne8gNVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=mzZQw_L-Dg-bbomXF7uauRbOfYYiBxDmqE9f8FCZ6X5QXv0QN3JsXliwia6x0qLuGSJIHbqSzKfdq7NTvd7laxNuWpMp2-OaEeKWeP3byC0b9MJub8YpfBljm3TUdIFnFdpqojPiX19HIFDQHRBQ5bFF5Xk_gKnhudCmzIJ0Z_aXud20X4AycNhWSovoN7LEa8aREWBHFCQ-DLKaOeGQOAfvV56zhGH8V-gMshXxVJpMZmamg8YjDE0JaBt8VxYqLX6WAIlxgcOHzPqsirjwAHOMd407dr9uxxYkxXPPa0QYelW4ssddX2WY5Y3ZCuuBE_snsbVJXESUl7Rne8gNVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwK6axFiFAQCM1snOEi68kVD5w3xE2Rs-66Tk7CABH73c58PHx3LDCW0VHXfoPchk9fKyp1Y83v4SOG8_vl6TpSeTNjtkboBei7wSDgXcVTaW7CQDPgTlJ88QtAfxgQAzevyJJrcgxjBpNYc_qhlQUsDHxy5tHlxaPGOp_bKnVDwHP5x14ZVVwEcXbzmNzNDVdMoTUO6mIFdiKJyXiIWnSPAvt74v7R09z6_FRuZMochLGL-Kgx_u-fl2puv_yhTorI3eDXjfwoaBBAwSiChZU1guwi3sedMrU0n8JvFguKqPFE81a4YujlqeUW14MjiFZ9b4j27cfHJYJd4O0k6qg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=h6pqH_mN7iiGGY7xkhYf1qPdoEfBjMEosZbsuxdbxUfSdpo-nF-IUFPzgLo37ntvwsCD1j5s4IJyhfoGUgTuw1nnwlbjuWCi0blBghvuhVnFLTCJvNdgHNddsk3SjMp1EHjXlblh9iirtuzB_wif2yiU37nAGAqwR9jvPMXVXTlUKsRs5inBUpr0bJ0-v7DX9SLINOHVWnkKdX2bojI8P7mOCLD7wUpcj8oPvGhW0rRIC7rR9eJRk-WJmrg-y4OwhsSi-Zl_W8b7bSvPASZMwQZCqhzSr-KvWdw56MUVCumiRJEIM9msQLkaPoHySt4njtoI_ezL9RsZGcgl25G4Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=h6pqH_mN7iiGGY7xkhYf1qPdoEfBjMEosZbsuxdbxUfSdpo-nF-IUFPzgLo37ntvwsCD1j5s4IJyhfoGUgTuw1nnwlbjuWCi0blBghvuhVnFLTCJvNdgHNddsk3SjMp1EHjXlblh9iirtuzB_wif2yiU37nAGAqwR9jvPMXVXTlUKsRs5inBUpr0bJ0-v7DX9SLINOHVWnkKdX2bojI8P7mOCLD7wUpcj8oPvGhW0rRIC7rR9eJRk-WJmrg-y4OwhsSi-Zl_W8b7bSvPASZMwQZCqhzSr-KvWdw56MUVCumiRJEIM9msQLkaPoHySt4njtoI_ezL9RsZGcgl25G4Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=o3EGci9GkhxcLpDQMuNMyVcOfVf0mTIidx_i9mayvbd4qZKITBMvekjqpGMS0DXokCBMkT1ZNssLYVfJ8pZiUpmR4nnDLr4zMb3Y46lCiV87_EPFieP9ngGSDdEF_Cy9AfJ0kPYk1BJHXBhjfTHUHI9iGRrN_3ecb91G6rzg1zNR3YVxWhpJ5_cEgXR7u1nAMqts3_8H5QXT0OUFKGuWrPsUOsx-1DK-eAd28pKY0dtraPt7ty4Z6sksq54XWZzkLpOvnWTMiTfylZZ7m8R5EAenthQi9UO4SFHspGkc73sBnClJ8q8xx_aes_cK_TQZ9wyHIW2-Fg2kcYK6_Ke7xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=o3EGci9GkhxcLpDQMuNMyVcOfVf0mTIidx_i9mayvbd4qZKITBMvekjqpGMS0DXokCBMkT1ZNssLYVfJ8pZiUpmR4nnDLr4zMb3Y46lCiV87_EPFieP9ngGSDdEF_Cy9AfJ0kPYk1BJHXBhjfTHUHI9iGRrN_3ecb91G6rzg1zNR3YVxWhpJ5_cEgXR7u1nAMqts3_8H5QXT0OUFKGuWrPsUOsx-1DK-eAd28pKY0dtraPt7ty4Z6sksq54XWZzkLpOvnWTMiTfylZZ7m8R5EAenthQi9UO4SFHspGkc73sBnClJ8q8xx_aes_cK_TQZ9wyHIW2-Fg2kcYK6_Ke7xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV7zSO2Q6vbAVdiKd6MNcPziFG6eFjWSrOkGfOhZ9eZUXp10ii-rUShhOzXocP6ELE-ITlN9IFTOhKb6AJ2PfZM5Gv4Zd9PmJjVyxF4Lcsshoyo8jg4rph88B4IENAzNjqfn7Sjmw5KQPwQVGPg_BdTDMNKwWUkOqoio8kAtcNVWJEagbFsbihWxFFHfY-LUwcwSLJojuV-D92OWqWutSw-Ki0ud9JSZ3cJv6jhwLfxO7WE6Ax464S52qwWaTr8Opi9N3CRqqRT-_sNFKLihZWBjuG58TmJaPv9EP7mzQQ2wvYV9PXfpv9-3Ixtm1TGazDAJDgb6LlLcrYPRVrOBew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=Wny-ikzz4WlOw77QCnYTXNRrYuOkOLCPMKZIcOx45e_pvsErpPqI77NglB49vg7v2Eaqh4TCpLRG9uqpKX9LfHCR4tHAdMfBcJWnkT7hP8oWunWIMxuqBypmGQOPnEcJ_bUEPGGNrT7iyMgey9ivQLyxMSzD4P7pIkkesNGuH-DSKYllnuEZATyxdor-OKHs7lad8WzyI5jZePE-nrgJg-tMBUG8sRWIQS5DiWEgfVZ0Xz7pKXVjmfMvAsSc8Osg89Ahd2xy-3gh59nap5sI4oqtG8_XKCb00grMdBt2F6ue9C1L1RweHU3BYuQ0-QZEO-8c4QvvRrovPJnp-Cu4pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=Wny-ikzz4WlOw77QCnYTXNRrYuOkOLCPMKZIcOx45e_pvsErpPqI77NglB49vg7v2Eaqh4TCpLRG9uqpKX9LfHCR4tHAdMfBcJWnkT7hP8oWunWIMxuqBypmGQOPnEcJ_bUEPGGNrT7iyMgey9ivQLyxMSzD4P7pIkkesNGuH-DSKYllnuEZATyxdor-OKHs7lad8WzyI5jZePE-nrgJg-tMBUG8sRWIQS5DiWEgfVZ0Xz7pKXVjmfMvAsSc8Osg89Ahd2xy-3gh59nap5sI4oqtG8_XKCb00grMdBt2F6ue9C1L1RweHU3BYuQ0-QZEO-8c4QvvRrovPJnp-Cu4pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Er0KKrv8I0EGwugCVKNvAVFTjAHhqymhzuft8GauTBk0DA-iz15OJzqXru3sKGyFhPgB6GbY7yO9sdTo4_OqcqCWVkSe2sjdYpTKMvafWGFpBp78u4fsHR3em1S8XzD2LkU8j16QWCJw2HK1DnS5tXlifYNvMBQmaaioMxxfnlZIvJQVmytfQmrCBoXITlF_Ro6yBXXd87z7-t-Zw8XC0G5ikyy-F3yXhhuylTK0nOT_aI5l5SxKDHKKPKVmYdTRtMMy4E30xEhbeYMONcHlDLz03gDqwq8QFTGaAfx_HUZQ0_2bMsLUUFcYZmNlHikU34Qsh1S-Zc3g6tX7Z9nw.jpg" alt="photo" loading="lazy"/></div>
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
