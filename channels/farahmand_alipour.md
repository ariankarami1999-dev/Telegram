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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 19:18:04</div>
<hr>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPyLKqC2Ab8FwvxcoFYjY2oFfSKAUwkj9D8tyFgarLb6TIsKRE4WMVddSDEp15xwSLMZJNViL-StMs1EO-s2RqN9jYc1L00suXz_KWtIGNsLZcfe03kSP8qQwUdHoYeiapXvPImTB2ownfO3gidRSHxDS5TnQPvpj9v1KWTNRra7deoGLGjfGTWwMSBwUybvPCO7u9AjX40-1uDBxJW1VpxdWisznZZXGvT3jTg2dfH7YQTLilMvasvSeSEj-mtTBt-RaMM1h7FrAaJnmULfj0BG7g2-nETFkGxOLcPvNvJXmaA6tXvWnKC9vH4Z1m5cqp9weB62CJAp-Ru1nLt8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3U90zV_bA9BbOnca6Qm9r9tfpK8CuQ9E6ZfjBvFNbdzGYtF559tvYZIvgODN5UeM0lwK4RfPQg3eKz4zjasuAYQ0m6CmGqtWDjyAZATYYBhuYPMs5Am5w4EjKyu9O6uzGoyWJO6Riv0kQd7aPEyWoFgREsg9WGoeM-mWJ4mcp2h90Z_0MhDCEzHMLUsqYn9nOruQ2t2QCgWbPqIyNY1VCWjvqQqSbuY3jNM7yOHskubRkFS-ZLlbRTrFmXgyNci_bhN39pWeIJ8j2BxjbexIyckXvpCJnwfYHqx-FvE8yvgqUK-1KmRfpRkX7hW75nzla8ecncrMwBQUswV0jJ2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L64VijQjG8pYE3raY3iuxVkV6-1zq3bglPgHVQP50WAkVunbPJyyR3AQqxvSVX1LlDGfUboe_vfpVxZ7c5pBEUd7jdi5yum3Kdy-47EFH4Nl7PRvucPA2i6zqx16agoTcxVdukSRwIjTtGmrnUvu4HZMoX72HfU0UI_4QWy2pxWP6WrBN2cciZ3toBwnzdN5ywegKHQ_FRnNgXMnARo7mfw1m2JqfhkGBEyWOHFzk5nG6QJSsgyJJg7_fDvJkVGZLGukObfNeIkce5oFW3yKakqW-cD7wy43RC3cIJZpYRNT5tFP3zyE9-GS9oBzzQQBUvdpUX9SMzkeipqMJ-Dy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfOG8r9Le797iCT_r1O-6F2tl1IKrJXs0hhcDjwGlX56-Y1VSZjX9DosHSHHmxdD-7WTb2uN5qBfL5GHqSI6RY62CuJAxxTW3WOtrHiOF69Ni6RfArcbx5TD3O9uEWXwsxB2qnvw5lCEJZnqje-nZXdG4YdkYzcaJ3GxibPUFM4LKxQb_b7TZP8xzIR8zeCuL5oY3GhlH6R41k8QBJm3NTYGV2RzgNtpeDmVdzNFO5ODUZ_XdDwc5sxN4ma5TjG4M6Nr9rXx596qMmqnNNdc2RGXTN4HnxHvJQA5_Lun6ez4FZyYfadpFbg5jkH4gyaZkTDqSlLeU0-DreGOFmjkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAkGBrR1Wrrs-8F7EOCnSK_eDHa6IPFemHwWozUNCnPROiCVN-F8kBITQ7eLiAPkAAfll-kqLgM28jHZwsQgngLvKKZG09AZ1kDljgbZomBYyJ3mfBLYbyIC4i_HjjfddbYOpjBEpdPU1BeVm6L2EBr5rYE9XJZ4vCiF6TBFm66zyRGaADSGmvQxR5xKhgS1E09Mbn1JT8CTFqYWxwfL_k_lSuj7CTpMFQ6IWzb3KF3SiYj0mzy4dE54EyFqY4eQT3K2j3eywYWAil30i22CjyyFd9EXoaYjsgi_R3OSWg5wmDdfi3GIfaIyxvcrt3K1ocMCHQEn8rmOOFUfRTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=klsaEJ_DHiRko86h6BCVtWMc61l7r-4gXLjnF9Q1IlUZvlrFAPR29yaGdR6tXuPQ75PsjYSDSbbc58_EKFYYxYqua4FFV2uipAERHi4pPHQxPobImxtFIDKtJqjtcSpq7sJ_8cxmzpeoL-UvvwZJ6Ax3CxVHAUpLuobLkLBIUyJdL5OVi7RuSuEIUbMh4JD_NEGTGqX5dHlTBgQ3gv9QqSmfjcCqV7YRsL9Dd8yDJ2pB_RjD2TOGt90-2zhfSaKdyywkxUEpCzIRNR6pvP9MibQenvR7wLV1L_qQZrxZvNJWxiT8JNXZfnPqcAtdRiv6Qr5DTL03RI0WQUFaH2PS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmwMFkzu-ZSmk4eQ_q-FTjcm_glsTaNlNPRSYlPCaUUtLBoF-IJNKGp-sf9FSOOLsouKFU2vPEaVYvIHAib3LtzaB6oLQ-xflSapqtdiZHKsTXbq3t16E3w1E5HvYVht0HNiqo60uzyaU0DoIENCWeBCgkrrHPYFEfveTAA_R40XOt9soH3y5p6l51eA4F0NGm8CGY0_hkyovYL8kWT4Q3dn7-NH6zhCpeQoJi19eReZ3FeFFjaDmgcgFzHR5KxMxV4fBwXJVgKtBJjxC7spXNbI-rA65CRFyUztQjP1gGPNETDswlbtsAiQcvhzqWGN85zRZAhg7xAefurpXCIWyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDbsDC7mREbf09ut3qDDXR5ypIHjEPw8a10OdcPY4xnnzHNUYl1Jxv_aH6w5ocosznZaFI7WPNvNa0ZaJiRgVQr_7zSxjcD3rVzAKxpysdT2Xj90I-1VQDiS4-izDzOMh01KARNqS_i0kfd3mZUDawJ5hijeeA-SY3pljNeQLTfyeKF7wQpy5nebLRVCI96ejtCuzj33pZbVWcjxri6fSJaqJkyPBplTXw3Bts2hh0cMIhY6J7xObE9A_I_6UpCxfTIREjTALGThERzVSAkkf5uwcyxveXPEw4C5DkMo5okuvJLNIiVjc8FPgnUL0hsg78hEwedoMdSgwJv8KTWvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPehyDy6fHS51yZgOKse5t41VPUAbP5L6i-USgAJHBvoGAm_MFRAfI4Ru8vf_Mc3Kh937Z61QzQwYmVx4FkhrSQJAA-rHYtQGxOHeGHCybD9mBV7MaTYsXyQG-AUVRX_EBHyq8gV-uy6u564ytAKdozja38_aLZY8Z9swmD_hKooQxqz1MId_idXisWbP_u6HdMkYa5szRP9vIIhU4lt4i1YTRTbwVntLFykDzyuJe-HwandDbY7SZzVY8awa5KgHSTaKK3IyQ0o8SKF7wPPAlh_vPWezCWVhsTgMUxSf-kyddgkUcxNUamNqN-gIpuKB7C7a_GQQm4v3rMn-fbvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=iNg4wnBeJqiZmmwkEehyVPUMpMRqOErXbCv6YhxZ5tIOQVO7gTmdAqgE63YKr8QICWoWr5Q2J7thDLCA5zR6mscf8JJ6tUFr9u9aiWJUwWGJCtc6xmJBT-Qv8EpfBuUBFddJW5SFQoGnIwO6Ax5Kc1a6luXYvnLR9uvTYSpRpvK9QudNPX-Bp7ts6nmgJLmvFOQDTNIKUTozbN279N2sEKKByTsw7aRiHRAo755a2sd_7BwSMHhRTPDPTJ31xyJXUSuVzwGySr2iRfYDxT08gOuz7MQdXbb7S7g7WQRQbFl3aGvZbCqjS4M5FG-HxVeK313x5fBYd2Y7IzWASRL75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=iNg4wnBeJqiZmmwkEehyVPUMpMRqOErXbCv6YhxZ5tIOQVO7gTmdAqgE63YKr8QICWoWr5Q2J7thDLCA5zR6mscf8JJ6tUFr9u9aiWJUwWGJCtc6xmJBT-Qv8EpfBuUBFddJW5SFQoGnIwO6Ax5Kc1a6luXYvnLR9uvTYSpRpvK9QudNPX-Bp7ts6nmgJLmvFOQDTNIKUTozbN279N2sEKKByTsw7aRiHRAo755a2sd_7BwSMHhRTPDPTJ31xyJXUSuVzwGySr2iRfYDxT08gOuz7MQdXbb7S7g7WQRQbFl3aGvZbCqjS4M5FG-HxVeK313x5fBYd2Y7IzWASRL75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=jPCSO7h02T81HGwzy6XIeIRfmW98AoRVcXVGVS4_YK1CBmpeyjxZrTPmQY4Uq8kLx5N0tZh_kH-VIMd11jQu3F_6WPavuIaXSXtwarxcVdjtRP7FlkrmSQw9OOwts-WWXXteLi7-CgozsNfAvkwah9oBEVN0TFuhXRgIzyxVi0OL2PNR-Fl7XxYtL7_1EVmIi646lCN8kzRkKxiZouHjAmeBMgvSpH1D5mzTJLT4wdX-bZmpPSuaZ7uegHlJTRzPex_3sLg_LIufpp03l-vsnNMhwZO5oYY74Mavk-6fDhv8WTdIgAhM2zWrmGoiI6belotv5TU5RO9yx8Rl6ILWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=XX_9gGwkFWhivt6xWT5jJ7_kMrEj2RTzs4Dwm5ilkAry9zYhU-65xZ9Yj7OpZuTs5nK8xyouKdDO5j8OpzprThp4I2HRFQokTyG0BAyD6TF1apCSaMGhYaJ8uReUQg1dN37aWQPDsWE_GYInmtyBesyDDUMpcxd8fsPZRTl7qDgmpybei-KIRkxYJxqYK9eqF-vcQFFViNsrN7Tfd70xGTjVB1e52BSABjsMkwvjh9wMSzs8r7GzB0_Da0KRjShF6kN953yEITq2zJT72ibXmCb8-Ur6jhHzIpSYnBx5On6dntTiceyVYDvc4Oit6qVnLjkXnAhspnfM-0nDJSgOlwktHaktfZf0dH9a9zzZm7Ph2HTNxmBilJhGpXfJ07tY_2zq4LESYyvd7xIYNXOfxFOvuJQT8KBo-_wo97PKmdHd7M1YeIMn9EX3xwwCE6O3wvoKscmOMWY3dv8NqyOOD0XBuoIoC0XOh9hembJM3K2CnIkqyR6h8sGy6_qo01WfzK8sPsvW9yZw3BIW1_K_qBH-2l50RJaWuBf0bL9SFxcqpsUnqMeNvtIX1Ph-X24b8CsVvilRQ2WhEuyg4czP939udqgRFHGGbb1QsrWzZtomzLrW3olhi8caa75oB8DAQ5JcnCA-GFoaR-wVHxlTpJjdDDw2CaAdGPVUDzxWsOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=XX_9gGwkFWhivt6xWT5jJ7_kMrEj2RTzs4Dwm5ilkAry9zYhU-65xZ9Yj7OpZuTs5nK8xyouKdDO5j8OpzprThp4I2HRFQokTyG0BAyD6TF1apCSaMGhYaJ8uReUQg1dN37aWQPDsWE_GYInmtyBesyDDUMpcxd8fsPZRTl7qDgmpybei-KIRkxYJxqYK9eqF-vcQFFViNsrN7Tfd70xGTjVB1e52BSABjsMkwvjh9wMSzs8r7GzB0_Da0KRjShF6kN953yEITq2zJT72ibXmCb8-Ur6jhHzIpSYnBx5On6dntTiceyVYDvc4Oit6qVnLjkXnAhspnfM-0nDJSgOlwktHaktfZf0dH9a9zzZm7Ph2HTNxmBilJhGpXfJ07tY_2zq4LESYyvd7xIYNXOfxFOvuJQT8KBo-_wo97PKmdHd7M1YeIMn9EX3xwwCE6O3wvoKscmOMWY3dv8NqyOOD0XBuoIoC0XOh9hembJM3K2CnIkqyR6h8sGy6_qo01WfzK8sPsvW9yZw3BIW1_K_qBH-2l50RJaWuBf0bL9SFxcqpsUnqMeNvtIX1Ph-X24b8CsVvilRQ2WhEuyg4czP939udqgRFHGGbb1QsrWzZtomzLrW3olhi8caa75oB8DAQ5JcnCA-GFoaR-wVHxlTpJjdDDw2CaAdGPVUDzxWsOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEOGY3ezuOk-rPtMhJN2WJGQtdQ91M1R38M28tkbrHFaXD9Sv3xxqSR9rFBslSFsnVjp9rk8zTY2BJfYUw7cb8eUT5zv_J8wPFJ-PHLiiWFYCFd1Ms906atxp-myrjfbLs-Ao4L6jCPuq3A2WnkK_dLKNbSrOLG9QAKfFRVQIUOymezcbHDaM7JB4aWv6C8Ubj9wa9_rrrl-tvJgnUMSibymUrkJ3xR06NEB49k-1E_RpZ440cswCJ4FJmmfodIAZ-NYuw7CGLXW58gYOqkai9qmp4ebkqYm_ULImxsQa2doulfMy_BahbPuuAza2ivRw_4vOK1qjlWEMopJVIngDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=vnkj7BfGFNzcZjekGMVqdYazNS2kXfIaAg8Gh6Ik0JuDm3Aahb222x45Q4nxfdwxceosSJT_TdYwLtBqzVf4Smx5I9AkZbQwDRHXQzoydlZTvRYX-7gEwLeW1vhhHYPp0Ywymkn8fMDOAkU3AewdfEB-Q4s0Y0sEdGdjfAXAsw53fbx5_uSjtWTL5OsBN2N0cfqXpsdHe-eZFFfv1TFFBBolDPWxLL-QjFfHs2juSSmlpApi5YNoKdYolDwnZA7VfgV66RrWZkxgm1wDylSPbRO9qON2i-QkGGpKNmKgxBNqTPTX13ZNlGN3Rfg8C-8O7si8gW5Ms0v5f7YDgpGVp53AZ9lkEVecVJbvSctynepwNHQJnzXptNETtZF1_1QQl7xxTYjf3r92CCrjFil6qRTQtSZ9Xnk5tO3H05NMh42brV1rj---rJPO9aHT9p8vsVCfxnPkqbxOC2W4cxHhGVNYYYqyO1nE9-6VOCmdXzxFe0IAoVTnVlYY-2LS7rjuS5odNDrXPZw7udG2oyF7qHKRMsY0Mg8f0C1IwjO56x2r1d4_2jXzDrUuBJoQrSwiQlI-BNiawkUBgd9xGsTa3B3qUwfjJ9OMPlY_XYfL9bFavPcymbrgy8GNEDKIGqntxSte4ojhunYsJ66G0A-Yv9Uoj9N6qgQ7UgWn41_qAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=vnkj7BfGFNzcZjekGMVqdYazNS2kXfIaAg8Gh6Ik0JuDm3Aahb222x45Q4nxfdwxceosSJT_TdYwLtBqzVf4Smx5I9AkZbQwDRHXQzoydlZTvRYX-7gEwLeW1vhhHYPp0Ywymkn8fMDOAkU3AewdfEB-Q4s0Y0sEdGdjfAXAsw53fbx5_uSjtWTL5OsBN2N0cfqXpsdHe-eZFFfv1TFFBBolDPWxLL-QjFfHs2juSSmlpApi5YNoKdYolDwnZA7VfgV66RrWZkxgm1wDylSPbRO9qON2i-QkGGpKNmKgxBNqTPTX13ZNlGN3Rfg8C-8O7si8gW5Ms0v5f7YDgpGVp53AZ9lkEVecVJbvSctynepwNHQJnzXptNETtZF1_1QQl7xxTYjf3r92CCrjFil6qRTQtSZ9Xnk5tO3H05NMh42brV1rj---rJPO9aHT9p8vsVCfxnPkqbxOC2W4cxHhGVNYYYqyO1nE9-6VOCmdXzxFe0IAoVTnVlYY-2LS7rjuS5odNDrXPZw7udG2oyF7qHKRMsY0Mg8f0C1IwjO56x2r1d4_2jXzDrUuBJoQrSwiQlI-BNiawkUBgd9xGsTa3B3qUwfjJ9OMPlY_XYfL9bFavPcymbrgy8GNEDKIGqntxSte4ojhunYsJ66G0A-Yv9Uoj9N6qgQ7UgWn41_qAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfItVPgawYI1DprYkhMjr0P0Vu9ezlJoBBIJGqXXg2I7ppdiuiNOBA9E5nG7Ld583blJoCW0wYrwF_GFKtrzdpZdSpZSs0rKUTHNUtBnOgVlh0-jAtKRF65DqXl4KYvrRgWJwtW322ndWyp2Z_NMLkE9fDlK5xbbcoxm6CsioN9pFVo-EDjT2vKWQg34SX1X65OKyHoP_Lglo3RPtS7cy_fYBmw3GDvW_JBAURgU9FsL63TjPySa6nZ2NLKPhXXNE9HF35qXUeDjgEOOGNq6CVYFWeS5w5xipLbIO3TN2OlfSsTPvIzZUIiNo8049oFlBoaiyxrpCYp9qPk9XgUdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvhnA2G2-DB5Vr8tJO7RH2OfQa6l-Kf3wUll_WJ4HRq_mpztKfMrFz4eDPZKsO4qZj29vsyl7Nt4xpU38afRFpdFE8Aa_RCPOvvePg3tEJFqycRu2Zguro3ofONSdgsiDazE17chXHKB7WbxxAX4sG1SrxNXMyoXMdiPVrov8XSLAEo6IqYn1DvYEP5lKazkb9pEGCRwytUaqxAxP_KPlvOt0l8gRTQwchB-K59LwKi5LCYwMdXtcA5HqwGbKPURg1QEOOnt5kE4HgrjEd1CBJmou6MINx3Z-rJa04wHV3JdlE6_xNwzYKguug0RoXo4wSQabENjqh7gZ_naXljMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6njPL4TZF7Os8VC8l8a1dMOT6xfgw6LbSpjpOWd3f4aIsgTdpK4ec4LAAu4AP4EtyNVzuVIfDSTY8FHZCFaxkeumfOhu2CAXtvQ537KNNQHiUGqF4P7cV7U9q1sIr_8kd71v1FB_I9QllwyjZgev6SzTfxKcLA4hYsGweoGIVxuNWAzV78njkKWEHfgDglHRDzZJW8q3DJaWavH7aA43EDKT9I-xkwtk7UNmswJaQxaUQRHusgc2zdQSug0UNexBogVVzkrRJlDUyii-svyUyfkg7AzCdQDdP8zmdKFieJRlneO9YcrnUpQ5G3XggoN3gKpkgsrubltNVNu62rqgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_U9xkLeiHppY4y6Wus4HAVQcbmdy-D-5vZ8dKiLE4n5aLfcplqIFiDbA-Me5EdyGxxs7lLYU34LBC394Nyg25sLMmoGPOMWFxShId9kkv_fh-B7h-YOYaRcjQF2aMZpgUIwQKECmalayGwuiBzkUNEXWYg9DATty4dxyVFz4Ua-u7dB3cR7DJuGwKkk9PS4aeA7GQHkbTFZAGqiq9iaqQT1Z04s56evgWihFLiBa21BPtUCGT71B_R3KxUIzuk5t2DCZ52HMN39rR2bTJKhA8pkA1ooLA6lqC6oSrVpzv40L5ul7jThPrnkDElmihStGYRkekgqNIGf_lRED2_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwVUda5yh5nmnYwqTQ-YNVMLzQt532XgxTQtlZK9UngmBOO0NkKzVoWo3qTrDjReCsD9FNQjd_O_J6CEBR-FgnX2q5C7wOAAAJWCPRjJDpOE_BGOL1Pz8GCVYRcfslWMFHbBDZThyDyj_Bm39vd5Qu1sVsvvUnm284Ak2Oanc7cK8uDqTMLoGZb2UrHSoDGUvEdp0AKcZtI_Rj6L33reH8NJ7-RBpymVGNN9AdWvsWyiBYsLbjXgjd07-CVyelVIaVUBTOdOM9ZqkE07NIeqyvGTG7ybgteNH22H9Nsb9TW1o7UGNV6Wk-z7RBZoP155-JxvtxdW56hTB_YulB1DHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvMJZ9PmJvWOVG_ScBAAP54GaODpX0ycYwvGIV11Yhxg5TRocEtZ5yktRWHGoF6GQY3-dqyqVnGTD2dZ1ZL-d__9GgTxmg8ltj2H3fOLCveZn4ulYRUo-Omj60vyLBErWknXsQVN_LMeg2Qm5jy1VBN7sSP33cn78JrJr-uopjxFkc5Wmk7pU4jB_Y0yDKjTtePv6fm2UzzHADTDdd_lGpC5rC16-tYfBCqM9Wu5ePrqDTlbXqDo8Nlota0sWe2H3juOWEj1KAKXiw_sB2rylV4xxyjwpXjVrdYwJGKyxxwTSIANtBah-WD7VqtSZl2j9N2KqzJpoc-VZJUs74FGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=oyaK5Q3jWoH4qpdqmNO50vqL3FHIdMq9zqDsaJ4_ou9774JYEf4OwC5z1FyMW1aLKFOBUgMFgnTJhF6rVC-Davo2Syc5ry1RNBXr0YC7nfcJz0B8s2mhghrmnFe_bCXUR0CDXU60uNWr6iZQDNZnt0atOSVFnr5YXipzY30cluFnmtsg-28tn9tJtFeuOAFfi11zGSgBN3z4VXiJSXieH9t5ygJ3RnktuhEUFkyx30BIBFc4lwH-FwWFZRoLh_2TaHSh9Fij8OOdc9CiJLO2avgg74x5At4zb61Zpdd31pyBTe0f4R0dM7RQZ7c22DYmozj4vHEBJDGFglBMtkUnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=oyaK5Q3jWoH4qpdqmNO50vqL3FHIdMq9zqDsaJ4_ou9774JYEf4OwC5z1FyMW1aLKFOBUgMFgnTJhF6rVC-Davo2Syc5ry1RNBXr0YC7nfcJz0B8s2mhghrmnFe_bCXUR0CDXU60uNWr6iZQDNZnt0atOSVFnr5YXipzY30cluFnmtsg-28tn9tJtFeuOAFfi11zGSgBN3z4VXiJSXieH9t5ygJ3RnktuhEUFkyx30BIBFc4lwH-FwWFZRoLh_2TaHSh9Fij8OOdc9CiJLO2avgg74x5At4zb61Zpdd31pyBTe0f4R0dM7RQZ7c22DYmozj4vHEBJDGFglBMtkUnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0eMogIzFstCPqWQfToTBcTdA9AgRLxt5uIL7oX3Xi5y1v2uRzpb7n08OKpBcoipp6lJxcgbMPGXWh-fRAUveErpmd286xodaxgomfHgTUQjV2BAv98Yx0LvgNEezA5gZnLsBNWUEAz0NdrOlhrMkRlzpCzGxpVLbU9AKMANsCU4hUyO_zdi84jSWh39E-knsJKeUhwOxqm5wrEs3J_AyrL71DiXhzJo_YteQdh1Fe5SdfhG_eBq8q7NYCgUPVbZI_K0cDkYkPmkc7EXsroFEUhM5Vo0vGYhPAK7x3UY5zxSYmhZA_KYP713lzH0il6o1Shr-M8u340LIqvW0-hXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MyA2NLtlyg7qKZMLV3vzTKpq26LFgJOvIqHW3CosKdNkVitjuVezgFBGcBWrP20vYspEob82rjRaud-KhrogpWDC8VnTgSCZ01CNR8SotqPPKli_IkmWsVlcuf_0Wi5ymAx-zgY2wHqkm5h1cU5xVv5SVphCd8UA8-PxoJlQBaxw1-m0Jpm9V5jB-okJ5rHOX7yRxoSK-k0YV9bsDp5kbIZRQ5VrwFSVwK4fGRC7OFrEImfewbwQPRG6UfgSvJbqevZv3bvidkhpM-WMooMv14redOdQFmmfkdL_LPcHoUjVlOZ-uTaxXFbOvu6bfIUAfPuUIX6MakLlNR7jqMo0gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leL1M4CBcCPZP4jsghyAmZEyEa_IKlsnmvm8EhUJ783ZRRGCpos_zf222brIyYU1jt1ZoGAEa99KoronpYymK1JFmIYWNVKO0VCwxiTipmIHay7HYRmzAZAowD-_7TJZ7AXYJDQArdNAEtL5yFlyb0VZXQc_3FO8Mr_6XAFomAmEy91XZYJk38IKWnYsgnoMhdzSgJZUxJj6ggzo1uQRmGA2-QBDyqukRrax-KknOFwxAamOrjpkbOfB7PIWgIb6bNWEDGCEySUYLptmH-1gC69hGVs00a9rBolWnt2lAycxpeJ0DOMWpsKYWqj4hzfC7i4CtJTJIs8OErQdkMFyhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qieKSNx7lG_PmNXr_mprrgs44bLVexE0BZAkkeEtcOp1C407jYn1NJt-lgHC-5vcTx3GKaGQQ3bbNbAvibQaMmO3ZbeyBYzL7ESa7OtN0sbCjeb7NpZUs1w1SMdb_7TdbYq-QeRWydSWIfUfZF2CU1wEB-X63jLzT8eJk6RX0g0RuqVCYhFvEfOGf46Ro7lRbVZoPWiHB-AJnQ4wboWYMvZVGkikDTbk8nSlatPPx3LNKSX3llqJTKemojzyWahL8meQYhEANzoDspDLqY1MKh-4T4VzxiAytaqzNvfC8iQE4KPlIFsEZMxUzcWY4AdS86IE4cro57vmFZSuRaL7UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=qieKSNx7lG_PmNXr_mprrgs44bLVexE0BZAkkeEtcOp1C407jYn1NJt-lgHC-5vcTx3GKaGQQ3bbNbAvibQaMmO3ZbeyBYzL7ESa7OtN0sbCjeb7NpZUs1w1SMdb_7TdbYq-QeRWydSWIfUfZF2CU1wEB-X63jLzT8eJk6RX0g0RuqVCYhFvEfOGf46Ro7lRbVZoPWiHB-AJnQ4wboWYMvZVGkikDTbk8nSlatPPx3LNKSX3llqJTKemojzyWahL8meQYhEANzoDspDLqY1MKh-4T4VzxiAytaqzNvfC8iQE4KPlIFsEZMxUzcWY4AdS86IE4cro57vmFZSuRaL7UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=IvRoiVP-j_j8gvo3UXLBiq-VVpFrA_ViBHebiGJ18V-j9hmD-thfvV0-dzt00c6dRq0A04R-kvMLG4woiHQAk1NofCDfgcMCqtPdv61Twm3QqD2kpeeGAJEyGx0OazBY7xAoygOGqIHYi8yxr_VXj2wgrxCeXMkXbdV9RGR_Yh6xZpbmp5u82tRmAV38ssvJpyPut10hMNZoXQTOD3CpBzmaS4qQ8UKU9DeJ286oNauGZfvbbZuMK9b-bdpzRq9JkurwUok5zTb5OaMr9jUVyxBdy5si0g_mfbUW6o9iEFlJgg3Von6BMwiSweVKyxienZ1dtoBZyKLsk0915XPVfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=IvRoiVP-j_j8gvo3UXLBiq-VVpFrA_ViBHebiGJ18V-j9hmD-thfvV0-dzt00c6dRq0A04R-kvMLG4woiHQAk1NofCDfgcMCqtPdv61Twm3QqD2kpeeGAJEyGx0OazBY7xAoygOGqIHYi8yxr_VXj2wgrxCeXMkXbdV9RGR_Yh6xZpbmp5u82tRmAV38ssvJpyPut10hMNZoXQTOD3CpBzmaS4qQ8UKU9DeJ286oNauGZfvbbZuMK9b-bdpzRq9JkurwUok5zTb5OaMr9jUVyxBdy5si0g_mfbUW6o9iEFlJgg3Von6BMwiSweVKyxienZ1dtoBZyKLsk0915XPVfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxFseUgf5j7GwatBFPNy3zcEGG2zuZPHk7OwKuhthe2xDHswPC_aLu6Jz9DFuqHV5vulb7XppGMuV_VryahxfJpC6AqcGE9sxrLRTC1FaAAKmyKJq8lsHGGCjSnzOrcjbjcIhVV1uEOUnFgSFimJhegSfymSxTCO2EjPMVkuOmpISbfI6Q_PLCHLe5WaHErWHOD9hxTTyyJNmuw2TxGHBQ_fEQoc0-I6TUUqiy3zd_VjpZ2nMdZyy5n6Sf18eBcI4ex45RuFtTbzTpTy-dxrm4uzTAs4ISBJpBQAkNUAlKjcjSDON7MHKhyXdhHItfuZiPI4Dmd64EQST1tCeazeEzSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxFseUgf5j7GwatBFPNy3zcEGG2zuZPHk7OwKuhthe2xDHswPC_aLu6Jz9DFuqHV5vulb7XppGMuV_VryahxfJpC6AqcGE9sxrLRTC1FaAAKmyKJq8lsHGGCjSnzOrcjbjcIhVV1uEOUnFgSFimJhegSfymSxTCO2EjPMVkuOmpISbfI6Q_PLCHLe5WaHErWHOD9hxTTyyJNmuw2TxGHBQ_fEQoc0-I6TUUqiy3zd_VjpZ2nMdZyy5n6Sf18eBcI4ex45RuFtTbzTpTy-dxrm4uzTAs4ISBJpBQAkNUAlKjcjSDON7MHKhyXdhHItfuZiPI4Dmd64EQST1tCeazeEzSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBiUpIkzQa0JxLOVK5Auc5dRVcpDxJXqPnHDcnIfFHrYgQtlhX0E2qtgX2ylSocwB1ByaMqJHRoPW5sZQaO0QzUUb2T28heZRGE_5R3Ixy0sL-IAL7XxtbYrhNDxchg46o0kZhlO0RtHEhxi-puDZHH_hOlebFIMnHKxvsHd6KfjX3kxU2bvl0PeXqF4mF169B_kNqS6GAS_aUed0yVcpmBWAPlKdkHQ8dQvbRLzCEIIOhWtibSpDYnqoFr4xTUftIAgppwKFeXd9zQT1mCj0atPE2YF0zD5kM_OKBC2bZtLuEzvxOzEwgTZR3xiCuy_pzjsmV3LgRVJS1wveK_5pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI-guUTBa9ZWhV5BH2UaaWA5V045F-2ixS6gUYh-0fagH5MicTyAYKO5Gg3nWFkCio5gbO1hfKHtfq3prdLFIIfcjNEVBAKNv7TgQQgr-KpCH3RBurnqLXEawvfz3RW6P2XTsxNsiGv7YKfiyZ-p6FZucnpy5yywk1iZWSkxkMtwUiUa54tYSEfl3D6UjQaowHuBsWukZpSEL4aTCGc_cDQBzfCvgyQvVgiCYgn34si82c9h6h_qgZ2IM2F3rZkBwemNTIRlG8qLbO3XmOHh2EDtJXoNW9-pOKcrDU21FRwod1shvY1-axkfyKPxwjhWu7f7fKvspHYeo0JnEQpqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=bnwoJWD258bRDWUrszASTOpDZpbz6RGtqgHCYFgVxdBKdDy8Y4DeS7mWe_M_fahq9A6b9C__v55kjIRiTY9ZbNhc5yPgpREvlOjtBwkdPjEEiLJn-fvj-zQHC9d6dJ6dDve_8D3beigySf_xTw0qzUBSN5g5y8ykLk5_nQkZKYjFJOUk2VxjFATS4o0rVQb38QUTHMNdN4ovTbNRsaw10FBycWeNUv6ZSufy6oOwOwQcZOQB7fCFY3dLJDs0TW1g2DqfnFXuERpxToIE9LFbKGIN-lEHzTjRWoUKi_GLvmmRFdVM5M-uELInZDk4S6lQPI255FjpxjYi3rjNbtUMFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=bnwoJWD258bRDWUrszASTOpDZpbz6RGtqgHCYFgVxdBKdDy8Y4DeS7mWe_M_fahq9A6b9C__v55kjIRiTY9ZbNhc5yPgpREvlOjtBwkdPjEEiLJn-fvj-zQHC9d6dJ6dDve_8D3beigySf_xTw0qzUBSN5g5y8ykLk5_nQkZKYjFJOUk2VxjFATS4o0rVQb38QUTHMNdN4ovTbNRsaw10FBycWeNUv6ZSufy6oOwOwQcZOQB7fCFY3dLJDs0TW1g2DqfnFXuERpxToIE9LFbKGIN-lEHzTjRWoUKi_GLvmmRFdVM5M-uELInZDk4S6lQPI255FjpxjYi3rjNbtUMFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgP6302iAt1KgGCK5VYFQs0vg8MdNiHEgLeVRxCXYnGZRVmY1s55vWEjWMki3xgvG9Ttmlwa4Hzy3WbpzI5ZYyBnmBEWBzq2Kpk_5oqYa_eS5LJuGQcMIBEbZP4bYY0mujWWIGkOTFtOlso-2DVNIJsOZ4Web8T2tJ82HEig8rsCwd7iNKiTglpxBmZeuKM6Kfaco0BZ44B1A77mJRZeQ2dGAIZy8qaIYsgXPgk9tawNcgY9rlVi1ZnzQE8Gu2zME6jsWeaCUJuHJh4QC5w0DLtG-ULWp4L2EuXhItDb_FRjPVMp5ItNuGfZUDCQQluH2QYXBF_gq8kBVIl3YbHf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=dNdwFCMA9Jcp8zGHXw769hzkYRAQEY31LL-DKx_MP2oww3-3VQBp075-Gv9BqH7kUken0RjpLEP4RHefAUbNk17yObzKrCVYpR1BKgsfuO9znM99QqXjhNVzjXkW0HJgnP7po9kzcOw2_3OS4hWi3iT85nQQXE27LAbQrz56pIQo6F-bttBRFK3Mr93Gt_tGtAwOtDEYOCkioN2Cu82a14mlOgaeJHb2jdp7iKX2upRoSAHM9uD16tjbspx2scGdPlO2PZNJxmY4NoIJEUWNmL5mrBam-Br1Cg3UCf5DAWZsLj3_O3EHZmjrdGda6UIDJgi29HS6uNCNwefUA8l-UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=dNdwFCMA9Jcp8zGHXw769hzkYRAQEY31LL-DKx_MP2oww3-3VQBp075-Gv9BqH7kUken0RjpLEP4RHefAUbNk17yObzKrCVYpR1BKgsfuO9znM99QqXjhNVzjXkW0HJgnP7po9kzcOw2_3OS4hWi3iT85nQQXE27LAbQrz56pIQo6F-bttBRFK3Mr93Gt_tGtAwOtDEYOCkioN2Cu82a14mlOgaeJHb2jdp7iKX2upRoSAHM9uD16tjbspx2scGdPlO2PZNJxmY4NoIJEUWNmL5mrBam-Br1Cg3UCf5DAWZsLj3_O3EHZmjrdGda6UIDJgi29HS6uNCNwefUA8l-UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=XnNISMLlRIRIKMA2ZYRN2Dxs4IkV1nNKFP0GeV4eXDOp01d-6Xj3a9tejFaOHg6Gzq_Q3Sax2ohGCnRqYimnCcDUs0VoSlY_u3MJZuwDD79hsGIBzeKJ-rLKGYSZ0o8fmkiJL9v12eELZzpzRvq75yGxRU1dT9kH0TrSp4dtXVEAnGY78yg__B91mBhf6liFHn5vL0Wi7-gxkCXC3WJtAoFJjkJtLvPZMHP1dP0ksfSVamdDIstcCzT2dxenHqZhErb1aPdwj98K6_QlcNiVyLTnE0jt4nP7FsYHTdAoVazcHp35I7fNQwXV_ghvOqrs74GcRBMEZXJVH-tel7woXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=XnNISMLlRIRIKMA2ZYRN2Dxs4IkV1nNKFP0GeV4eXDOp01d-6Xj3a9tejFaOHg6Gzq_Q3Sax2ohGCnRqYimnCcDUs0VoSlY_u3MJZuwDD79hsGIBzeKJ-rLKGYSZ0o8fmkiJL9v12eELZzpzRvq75yGxRU1dT9kH0TrSp4dtXVEAnGY78yg__B91mBhf6liFHn5vL0Wi7-gxkCXC3WJtAoFJjkJtLvPZMHP1dP0ksfSVamdDIstcCzT2dxenHqZhErb1aPdwj98K6_QlcNiVyLTnE0jt4nP7FsYHTdAoVazcHp35I7fNQwXV_ghvOqrs74GcRBMEZXJVH-tel7woXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=ihljIsUf6aBO2jUaqpCjI3ceUvPO-TtE1YgEXiWRuC0hi52zDKLkVxEO3hBwKMtx1qAPK91lkvataC9hzrGwCVwC_70uFXGyi9SIFoVUiAAVuaAoKgJFz1xwAYbbbDhjPLVbfmZqj8Gq7mczMaKL16MQ8DzEvQ2o57aZ0JNbCzhQssY_5zbLeppehB4M_nAXuxY1eT38plbkLXdW7DQsBxQ0Jewr4vE8WLN1fztGRFUHIsz8uG3wJkTdwYGZ2A0Xht2J8xOCDFIUPr2n8mpRmy5TsXEo79Tq8HljeY-nPc-Hc7tRHQyctItEU1wBdOC0DbTUw80vwhKW-DoTZ-2xQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=ihljIsUf6aBO2jUaqpCjI3ceUvPO-TtE1YgEXiWRuC0hi52zDKLkVxEO3hBwKMtx1qAPK91lkvataC9hzrGwCVwC_70uFXGyi9SIFoVUiAAVuaAoKgJFz1xwAYbbbDhjPLVbfmZqj8Gq7mczMaKL16MQ8DzEvQ2o57aZ0JNbCzhQssY_5zbLeppehB4M_nAXuxY1eT38plbkLXdW7DQsBxQ0Jewr4vE8WLN1fztGRFUHIsz8uG3wJkTdwYGZ2A0Xht2J8xOCDFIUPr2n8mpRmy5TsXEo79Tq8HljeY-nPc-Hc7tRHQyctItEU1wBdOC0DbTUw80vwhKW-DoTZ-2xQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=nT0gyO7-pIXEXTDYJpJ9C69Ptwa6nhJjB0w2BTcgbihDiRdpeLsekm71okYK3C0wrn22uiK2HgCC5lrQb1d3lQl2x82Pj453mIICRVzMuBaRf2U3NiP99-vEugrWWUv6RrLnKRvd3zVIMmx56n3tcCj6v4yVtFG2_qM9QJM9Syl5xOiIoo14ivqlU2mKEOBUZGTfCtiHPJQhZ7JVkbcnnVNCbJAYNhIHFhVNHC0YDigEuvonG6-3cwb1GjoJNce-mWFW5nPXS2caanMudOgnS2gbm5VjrmnWvwuO_th2rDaqz0EQE0UYNyKFc5c3nojfhnhmyI6OFJ_iY6uPkuly6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=nT0gyO7-pIXEXTDYJpJ9C69Ptwa6nhJjB0w2BTcgbihDiRdpeLsekm71okYK3C0wrn22uiK2HgCC5lrQb1d3lQl2x82Pj453mIICRVzMuBaRf2U3NiP99-vEugrWWUv6RrLnKRvd3zVIMmx56n3tcCj6v4yVtFG2_qM9QJM9Syl5xOiIoo14ivqlU2mKEOBUZGTfCtiHPJQhZ7JVkbcnnVNCbJAYNhIHFhVNHC0YDigEuvonG6-3cwb1GjoJNce-mWFW5nPXS2caanMudOgnS2gbm5VjrmnWvwuO_th2rDaqz0EQE0UYNyKFc5c3nojfhnhmyI6OFJ_iY6uPkuly6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOiWi_EDW7EMzuXzWYEEHn9SeIE10N7E30W2xyUwFq25wmwmojgtIDTe8a-e_FI1JrHFL0VsGCAuY37g99ZUCkzbSyGeMJA5V4_XP9My7RDMAvzEzAVyACQfLdcM3RAAB1YwFJ8vlrmjbnYpLyZap0aWrC6UbB96CP1NcJGElilbY3lmIspZaJgXQp3u0jfJNVJ9WaCn-2e8tQBvkoM-9IafAdOtSHN87r8nzHNjsTvdS4CR9_sriYI8K78ejqRqOu2NdEPWXEqTqIkqaFz56Q2MjiNKwPsH3JXjsDV2PUj1NB3SdbG7GDx3I3oJkJCtOgMZvZJMxG1DhrLBf-cNtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZnp91NlpOvVdVymIF6WZbaKxN4z25kX7ueoxCO8a292aH0gGOlLLb8gEDAzBTFQa39m1nmQGoDJWDhS3hSQDlp24LLsLr3wqRqoLjy15aJzaRhblRHqz3kSfkAQ90MQPwYtTwkj8dEs7h_WMmXhZZVRCRh4q_YsBz6N1jTooeNkftvdTx_ukT4TfSx88pJGcyWzBnOpQP_QAY2duVAKDPyVLNFw4PrN1kRkPrkcFysyMzH7SyX41Hm7hlbq9PkVio4kGObkQ7JOGxE1pdKu5NNMo1Xw0SE-Eda0qYRSUgLF3KSr06fugHKFefobFTNeNKRKvYuYRHyw_Mm_3UgtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2AkHy_FSL-UUPZCFbnmTQqce5hXiGrtiCnOUt3yMRmKbRd9upRQbR4vRbBMTPs6h6MGblVIU6ZNhUdkPJiWu84zn1C1vZZ1xbLw5yt1BMqNst8rN1MTQbgGyAfP5RHGTE91J_Vhd_pU6mhK7cX8erU7_5B2g0nLR5ba24GmI-SRXOGu0GVJm3poF5EY-56jcs9RAgnM_iAe1LiTyin-iSF9i_gnlNUqiJGVbQd7KyYDrOptJHM-AIlBjWnYQkufpW6UE8vTo_ozeI7--vP3Mv7HoI6bEXnh1K_65QXBrgprp6xUxgFchQiGAn6QauE24pMaxRcdCwIxXxKC4MlZtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkT5OvmGUy4_KQhMnyFdlmxaqQ8ROJBoLca3O94B8VzHbuNhdVAL60j1WSi1xTNisvPQhMZDdJ2MccsOj5FtAO9s8rz99Rc3_f7zthJZZAUXi47yqdXVWPQ43u88YjJsy8Taepgwpmth2RkDmN0NHSr9qNW29arHN85j3XKXWu1-yuF-_mo5L7SMVZVK4WDhR2mGo8a08XKqR7-LHp1gN75sfWTqLaH9HOoPTEltXjJ6AZeWsmsDKZJC0tiPillgdReAzLDohQG3eQCSyiu2OC1h0paSELaX63mWS2eqphlwf29b6xlPOB258aM8eCvEhwb6O0kz9Nrx4UsO5hvrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9SiGYLVGZ_u9IAtK5UVf991OdPIj6d5V_5q4J9J7W62ESNBMGJcwrsLNDXPydZMii1BaZwnLZfP-DgztgCCnvQQIKzxtUmrpPfAK6tcl8t6jrkAFRYpOD2Kgjn9r0c3YBT3o2dqZJZL3YjMMWDzayikePfsFgQlVxHJWZvCWpQe2XOkDcDwq3cziuO-R9HBQEExwBUu2TZKkP5DqRNDiaeL39K5BgA1_e9BI-xRc-Uxi8_XmFs8q4yrbVDArAuFqRebIFKAh78Ksi90bxal-NFAOoxlMqmrCFeG5RRJrIpP-yyIBPS31TzlSMnLBVg9yLMSDWFNOmUDa2OANHmukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_zOUc1jrPfuXfvz6CrIPRMabLovltkZhleV6m2DvQJ4aa58bK-yxrJvQM4H1wX3gyZDeLmj6xToQ9Pg0gzOCVwKccZ-lSo-Jm4WMnpQay9buHkfRHHcNNAwW7q7pI3P_4BvPxUa1WagN36BlvkjQXs-rY6MxVBi13CGvOz09G-8ZSmhdfRXcsUFWv0fuUoMN4IureM5-hlizknaLoEYQQY1T26DrODCeTcDsg5hdxdCcTicuNDX06aQuwQARgfzZlyASqZFg7O-uAjFirBh3p2CwRlkNJiKLNot6SIzSRAGRlkdSRACiQl8p0K9C_FDiKl4Lpd9PjMGUn8bMEZ2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx9-xTmixthNlIVsafwgDv5DJcz8m-SRwuEZvkaTU239xGAxm-JejQ3e65J6E04bAdR89HmGJMhjnQXyPpU4PQOnl3V49nqCYcBY2Aon5ZdohUgC8yjzbtFbzWiDpBJKfEAEnMV1WOfjJwBc1jIvHEQp1GP4T3WsTA83-Uf8zlcZo_PKY8HVQsDgE3fPWZy1bGWaDOJECB6egdDXh4EjtAO511z3tAmiDA5XXBz0IF1eUDgDLHepJNi9Ry3qkwl0FVqpL3Kbx7u8Lbd7YRT-IVISR5tgph02nTtljRTg3f2GFVZtTxygqp-D8zvqw5hHrgma9s-Cg_t1oJaWojouZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=DPn9HI2dm3UJBb17Ex0kLS3AnFLHeN9X7cTiQLnLn7Bp-CeV7fU8gb6E0XiZHqaSCWlEGa71SkvIFqayNNxPM3ON5XhlNaKtki5ASlLTEnaSM2zxlt4gVOuCkfYEIjQZCFkxd_BHXv6tkSQBSYIbNRK6wQR-HZDpNAASJXfIJowu298CTKOkCAiRxVWAsNbZv0fAaLxKnC6FMqA5UwEaBhvL3alx2K_JfrD7pPqOZfO2gRWExAi15n9DJzshzrGXYmDlir127JbF66wFomEEe4UJAx199FloGGhos33RttIvgtuQm7BkCz_nOrN_85I76mE2ITbcuyCPR_6jIYtWOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=DPn9HI2dm3UJBb17Ex0kLS3AnFLHeN9X7cTiQLnLn7Bp-CeV7fU8gb6E0XiZHqaSCWlEGa71SkvIFqayNNxPM3ON5XhlNaKtki5ASlLTEnaSM2zxlt4gVOuCkfYEIjQZCFkxd_BHXv6tkSQBSYIbNRK6wQR-HZDpNAASJXfIJowu298CTKOkCAiRxVWAsNbZv0fAaLxKnC6FMqA5UwEaBhvL3alx2K_JfrD7pPqOZfO2gRWExAi15n9DJzshzrGXYmDlir127JbF66wFomEEe4UJAx199FloGGhos33RttIvgtuQm7BkCz_nOrN_85I76mE2ITbcuyCPR_6jIYtWOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koCRYaQy8dAM8w-kD5YFI_QCcf63fpxz-JZUJXXhkwZ7dKZnZNdeO3Q5UzzqD6a_GUajMxYzzkNJRm8oR_kSDyKQz8Lq2MGTXyuoeJTSfLzVAd5MCV318ho0XXs5jfbEs1Nz_uSOkw7XFrlZHPhwlxVR-ZWWv7wSDhv5aS7cBo5c6DdRuK5sMQD1shDpaFyELvnQh_lxtWuYpaHwhyLkuVeCvdh3UrxjXD3rsJ7TMKsOFXCRXM1sKMDrloXrWPrJEfDTK50r0hyVpaZX3X_-kRZkFgm_MfyLJBM-48eOzhAU0sEFvA8E0YGCcqASSQ-ugVmcueLCemD9KSEJJd_eAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGpjDLjW_5CA4s1znpliT0_PwX-3drO9ZwiWbGvIZT2Fjjfpgi5YcyK-Fyg4N1SEqJDRHliC7wAv2MD3PdkMS77Tn0Hh4aw90jk3ugo8G9JrRXwSCsW8zqu0OVOcmKhNjz8IEi1EEUBsNiV0Dc1FKgilr8s4oQJWrcAxV1J2xK2iCoJqd1az-9tDZN2sIdjP0Y9jAFdDUrFJwveoskvGqIENVVtN6CjjHjeBTlWHqlCOkAUuyBUHBbY_e4ipRTnEyytdEDwRyoUehBxIqPCM373SJesPklEaf9Rcw7r69AG7zQJd_Ha11K9HMkmao4RwDxg11WMUfyvpHf0FI4Ex5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3Eu4q_n4qPHVVXaJve6Gtb4a04Ue0HmGAia-xFTyrSPa5ms1kX477NFguOD2uAuH36tS8WzsAjM5hLCjJmBLYZKRmY-hf3RdP29OxFF_CPsyfGeIInr9zXR1dP0dKzBHXeshTRES9RbQkV0VGoJY-XxPmBE7aTBq16ztpu8ukdhIBRKpy2VPZwiIc3Q4PaGfhfF_0pZ0DqHaGGF-G5C4KkiBGhMeeFZpDE9zZGDq47D7CBlmIacL0XsnRczJ0rhPYk4KFLNxh3ojd--S3rrc3a8qOKNxWaLxBH7UDyolT5RxRxlWhohgftHaJdjMbv6Et00yNDqpbOTK6iChGwg1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op5PAHYxOuc_PeB0xVjSOjxEZr7X5gz1c991DWe1jxNk0P9Oe7oODdtY00Hc0aZiqOCiof0dj2ZNT7Y5mxjnGxpmTazcLlILPyU429OTgN6ZrXiOzlk4pwpX5KvHUVPGaU8S3SGiD8TcTq6DFAEly0z2IDVApJwKFUObYCZLCUcQyNKRjLKOxPoE91-omqxRIHbh0HQbRkw0mTrldn-zDW7zMj-zbqsi0zSVbdquKIVd_QW29OcH6SKKafeMrtxtQFfrtC476P8dufMSDWji3CvmWUxypc0TdegQ4K9tCXnVeMzRfA_5ArkwzvLxN5T0bob97ViKxw_6Hk-5-nTgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_97AiXSGuADggbkDzDun388KtRh5IX05tcRLIKjPzhhdfNksdCMmFjuTgzQDJi4uM2NIpXeNc6S_y30RBd4w5WeOZRGXqNcHjg9PWubvpDsvqGzAWelosxDtM3SYKlrUVfzg2nwjg4xq0U6qZTiv7M7AfsbzGDoW3iSqeg9DIQaRU2fLZErwrR4sjNPUbQg6yXehIcwduvh5lB0hpkwbdluyoYCzkhKw0qP8W_y7EmUyiv0zSQ3Wpp_FO5TT8IVETLLCvAeUFcOYpmp8lHNs2s29pFGBqoC9vC3C-_AK41hjkEnBvISAJE2b9-EkyE7bxXgHKnQynQWR-r9vY4clA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGeQ_96ephFuGml3VIxI8xpH2OOmW_ni-xQKW8SZLY5jtC3fd0BWRUEHdQjr3SO6S9NCbnOYhLramc8WENGbOUhGEIt34wvcoNo0xu75o8J6J5Xqf5gWOzZ13YuSnTKIDemCHGTeS4R6zm4u7Gz5TaJh5XyopaxSWJhDKysgM8Yf3l5dUMfSBtLEGAQH3z1tzh8A1silsU-w0HnggDni2yJk9zxhnfstNtJFjahxEqUwLC6Nh7HnSPebCbJa0AZiy5_H65NGf7B5Fptqie2zc69aF-KATXCvZdQkni0EAtS5kqr4efk8B1WDYXsInZkAA0qPxID4WxHZW16JwkRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PxZ9HLrCa1WSbZI2l-VrgIRksxK23izpJLKAlJCzvYTP5xUGX_Y6oOfH2zGS7dA4XlpwPhQ2F6nuGUaKcHTrkpmkfW2FBXHZxdUXnBKDzmlpPO-wQWBIdfykMuBPctW2k7uomkldqDiZzOiveucty-6xryCNFstGsun3Mm6xMMv8JPReA_jBxxvGWIqoPHfjJMbNkwYW6Mzabso4JZUvQNS2o3Sawf0_wPL6B-jbXjz66G0vsUH_8OO0uX4ojyEjG5SkQQFAnNjSkjqRJYL_-gzhoXVXOUPLP83HoqAxZt-q-8WlnqmfmzUbz8LdYMoMWCd25BEVvCL2J6yLOFm0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVjYHBS-97-VcDcT8PqlsRLSld-tsBAHlGc442FlycQ-8lsF_NCeREJ-rrmiRB6JhwWCCPoDF2eKyCuj_zrTGGuFGNHHiAdQstUD_ySG_aOiMWULpcbShIGFdUCT2ED0KT5y8CL8hZ9pDW4sJ3kRVbUS8W-0yVcvaowcRat7nsrfCNIXzZlfVchz6fdI2PPjAaXlJp_QPcloZR5uUskFMGrhk5QBpuAVE9Y6N0v3XY3GUZey28IeM5EEizHOv25zzOWPbhXok665-MJmwtsv1oGMImp5hglwAQmvtFxlCaj1OR5QNflLpL6irDqk6C__3fSzygTsYqpuZB0EcB-lDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=TjUTZfaK7huNY_tmO_eubDtPQxAatbw2naguhsS9nc1qcbyg-rD1g8SjRMiM6naT15C_W4TA2VHAbR1AI55_1bdgeJZGIk29fCddEew9x4SKDThD200e6DIYTo-MQQdSkKz4Tlj6XHWAKYGsCTquPuLh8gsS80MDxVuxWiLCYJuz7YlA-2fd5CjicOpfBUsJwyiQiBOYr_-u-gXGp2Px8SXN7-WHZpmnynxg8Q4frdcEjLXoOks3UPF1a4tap0sMOH4ncNkIVwYcoiQAzOYKUsDR8FMVU-9R38tIBmuxVu1ApY42QBO-LnwEzqalQFdep85lf7sKVIVyZOXKPKyn00SaTs7x2BM8qR9Cw0sKsFEBZpGgBx-C4jj7F4ETI12Nd7USk4C5JHZZ39_Yp9tU2kIMwdbbyT6iGjfaWsCE2lnBGqGzMb7mfsJvmEHBWeza4WvaBaR9Fn3VJUf7eeYI-lkQ4OZ_k16o9PLOCMt10xaOi1x0WMGS-WJFiTI4vd4N3IQcyg_mR0ypUXc7w_T4CKH3GAuuQd_MtbsH71Ee-DZs6zMZXpTdThkoYyJyHqD910g9K-dmPfVVC_M08gle9oCQs5eFrQua8XvvUkUthkf3Am5r5WyQUTZEp9sigFPai9WyRJ-KsvnEH1_UB-8geFnGpUNXPt8E74gjSfsjpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=TjUTZfaK7huNY_tmO_eubDtPQxAatbw2naguhsS9nc1qcbyg-rD1g8SjRMiM6naT15C_W4TA2VHAbR1AI55_1bdgeJZGIk29fCddEew9x4SKDThD200e6DIYTo-MQQdSkKz4Tlj6XHWAKYGsCTquPuLh8gsS80MDxVuxWiLCYJuz7YlA-2fd5CjicOpfBUsJwyiQiBOYr_-u-gXGp2Px8SXN7-WHZpmnynxg8Q4frdcEjLXoOks3UPF1a4tap0sMOH4ncNkIVwYcoiQAzOYKUsDR8FMVU-9R38tIBmuxVu1ApY42QBO-LnwEzqalQFdep85lf7sKVIVyZOXKPKyn00SaTs7x2BM8qR9Cw0sKsFEBZpGgBx-C4jj7F4ETI12Nd7USk4C5JHZZ39_Yp9tU2kIMwdbbyT6iGjfaWsCE2lnBGqGzMb7mfsJvmEHBWeza4WvaBaR9Fn3VJUf7eeYI-lkQ4OZ_k16o9PLOCMt10xaOi1x0WMGS-WJFiTI4vd4N3IQcyg_mR0ypUXc7w_T4CKH3GAuuQd_MtbsH71Ee-DZs6zMZXpTdThkoYyJyHqD910g9K-dmPfVVC_M08gle9oCQs5eFrQua8XvvUkUthkf3Am5r5WyQUTZEp9sigFPai9WyRJ-KsvnEH1_UB-8geFnGpUNXPt8E74gjSfsjpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=sRENaS6f_g6e-eX1U-H0nOCA6ViECQH4rI2LZWmEKyktsEWyfzeSWtJXqc0bjEQkhmzyYZYSjxvPsdefhcMIdcdbJ8ovgawtZf1O-hWOXpOGUoEqCudO8pswzZx6UfOfFlz8mtZqyNYsZ8eeghHjK_lZHf3GvIQKSGGNcU0nsXElH93ssSk-AJYfk98-kZ6yuM0Q1Bi9nHkwitMD7_VkUq94aluJyVQE22HwAWeoFJX3k62-kG5ziK430SP2KEytbWpbxFW2P8jlLl7XnEt_hbVMa1tE3A0-xgo3kdO1EMXnWxPhYZAe4yNeGy8yi7wemNvpstK5HUvYWXOoN_sXBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=sRENaS6f_g6e-eX1U-H0nOCA6ViECQH4rI2LZWmEKyktsEWyfzeSWtJXqc0bjEQkhmzyYZYSjxvPsdefhcMIdcdbJ8ovgawtZf1O-hWOXpOGUoEqCudO8pswzZx6UfOfFlz8mtZqyNYsZ8eeghHjK_lZHf3GvIQKSGGNcU0nsXElH93ssSk-AJYfk98-kZ6yuM0Q1Bi9nHkwitMD7_VkUq94aluJyVQE22HwAWeoFJX3k62-kG5ziK430SP2KEytbWpbxFW2P8jlLl7XnEt_hbVMa1tE3A0-xgo3kdO1EMXnWxPhYZAe4yNeGy8yi7wemNvpstK5HUvYWXOoN_sXBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuzuENPcs5uAJ8TTBJpMvulSSaZdVPqalGbjheOI9xbcTliFPGQsGFtDdJfyZz-z3r3isR5kRoDAeMGfVCN1kWKEe-T1NrvcSneLlXrRU_mfUbWtJwCzXaP60QKWMsq8Xc1bgZ8BcXIx7zGaOfVmmBmUaDHBEIwu9xpg858OiV-aWCSYfoZ9ife95o-h-vRScHummGIl9gdpfXA2LLKMIKbygtNM7q9HQORYf_V-xqgrHddnb4T0auVXKWyZD2evI6bbBUD1MxktaxMn1F2KPeKoaepfFXhDoVe0YyGfBhyB8DgE83bgAILxpus-Uq8AFU8AcTrMt4-IliKslf-K7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otfy7iDmeJJfk8d3xlOM3oTc62VNsMiRQJ19f0y15MAjggYDCkWRGh1EAHCyC5udvwN2py7QX-v5lVdLe68mNNnZhE8uXK-VSYhpCuFBs5UrA-bLI_OsDN6RtEN3ZZhD6Xci1S_cVKyI2uUC3-yCjjI9jYcjGO1azYqJ3aSPhmTDNNZDls9qBIwc5l1IBrnosdnruQVBpiTpTx7E8gGmNFIYEgWmwkMsRiiDqEWDggGI2bxWxUyuOcw0mMdxCiwpWaFaXmWiUtPEMgguMdpGkc8cyM3G658NKFPbEs8EIjIPZo_4w0CoVXs8w3f-DPE2X4_PAllKK91ONdCMjjdnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyTk1vMt6E87WRZhAopNoUBXeCXDXzKx5iPe61jIMTEkbdCaOEd9xpeHaAjd-NkEu5CWC7jCP-0gR7A1BLeTYYkAt_df0uYwTJ2qi49jeSYYfOMWJugaikOO2BIGnXuaCq38Lg2lB-53P85iERlioEIv9DO0N9IsYDTC6BAP3kGxEY2wKDXEUejMPWvdQGm9rQrHYj27XOnV9nZH0Vj28MSQtIP2Cvgr4QbIu9AdYco4NeOaK7JNj0HSZ1wk4IAt9_m_5NOfEW6JjQiUlBKBwec4U768uB2GMbjN0TLUYRvtyEPU4nbXd0vRTqXc8KckSnaJalklv5emtl_9tc5clg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Xdb6bKcFRfGZCKPWjJMMZ7DdVn5nBx-GBvwsU60kfRBhJrHg9UR6jQjrk4ALfJfWmS3QXYYGbWIckLsrKGu2PvrtY9-FPBITn_IGx-cLlzhCL1Ycyb-Hw9_jqlbl_qudQ7-cvVz-d0nkaUbPzkoWpoS3nDFkeeCyMogeNcc37nH3Z5sVOx_5-njtZ0JWsQKjUoVFcgeQoUra-SKiiAu8NgCXgTyfQNpFYeXEZImFoixPJ5CYZYDOtckiQPvv5MzF_Z12EkpysQHRXdgnTAdJySpOFwPe4zDyRPMHPgY5QvB8odyUTI3N4ixWHeG-xQHY45y4Ip51xyWBVYKZ5JwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDUf-qDoTK4C4Rn4sqrbmuxf9brkipm--IlBzrWy4h4l3rbSdd02pzMVieoNg4e2wt6iNrl4uQxoT6EUWcAdFqVUxRxHUZT5YTcass_BuMXLU5angJhqSOh_pK3t3bPbvYl-8T9wP-bT94H5p1lDFRVGIJntH6Bq81rCRAE-1Y1hBoKvuJJe4sdnoFLqAJYTKu2sKg3sE6IN1XgV88sh-jUMS-Syo0JggW43E5TsWWZ1cTmV5JYzHaBhbX75WXH0nc2sv9FdD87iDP_YoSlKOUNTeFW8-O60YNN7aqLGmLg2Su_W1Ir5Scd0ByPw3bwR0vncoWbvUsgEPXsVBK2fhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcpVyU34jvpQivx09vBlCyThUHOEYBSX6t-pvFiWezCLfPWkGUHBtVtnT1mt-ITLrKzPs6aBVJmo64I63gl94LIesMPOlA3e2L91gqidHLDdMuVcy2AptDuBsQtzuLk7kUfxeRxYja53I8fFurGWL_qr3F5VDB5GdM9V-HQfPfpYT6T_jFlQPUej0Wo7N0Jr46dydntmfAckkhjHxtf0KB-oITwKIBUm7e1o_YXQrDSEx0sW_Qe90fchi3aNkLkpgv37WnpbB5D1IRu2kRCQGBgtXJ5QS6EVi_Hv9pcu1JzTDkm6Cy8vJRRUgkutdp388c57z23z_-CyiYMDdc__8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9BRq2680o8jc5LNOPKpa5XYqegBX5Iz78K1SR_Jgt2Gt3_kYLsIV9Zw-eXNJ8fuk5zp9xRjgiiF9Rle-IiJeFmPfGXz-YQW9QMcs8coXZ3GTHjYSG98ozrp3eyUrfXt3giQITo3UmI4qYq9EjzOhO4fVZj1wzh15mR4KLgr4REkqdGIYDDHBb59-z6rxyio03xOs1Qf-C9_1rgni-VyIG_WDXLfJl_n6zt8SsXD_XUwv3zoQsXbQ1a3T8NV8IvmSFiSNZ_YS9m217RTFpBkClPtdI1ZYLjvkIB1HhzSpqai6nIo0oFUZ41ulUEyq0-GWYfqhAqWfrYxAp-vRzY_0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjsTlw4nnjI7eYklwWQl1pTf7P88una2x2nGGN7iVnOWeG_95ndYXs_anpejjAJ4Bn8gN4qjMICXRPevDmGLViYFNNWjFhKkFKLgz45-R7o3CY_aQ8SOH1G9KGyOw4b0Q51TTYZieSWjqgrRtCCzIB5GvMK5lgIdI7KMApjuBr3--CpthKyEHGGsd0088L7zrTBBBCKCmRIybGy0QoUVx5X9SHQ39alMtl6fCFHs44B7Gn8P2RiJJoexA12pWHnU2so9FIzHN3XRVNLjX6mx-wPCog8o_97QM1KAryYNo5ZbFIKpbF7cCefO5T0RhG6J5AZsEphKcmQ35oG8oc541Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mH0V1IF4M6923soJ68vRpEGK-7rHHJQ6oDQv9wupq3rxzmg84XxBvYPg2_qMOUEUx736j6TvDP3Ii-pYeDmVW4FbhW01i-aoVhA-Zr9_sOLLstdTsIa_o0lmQrvjjKB27kSlbuFVOTnG9x9TseomXs8V5OnThXF5IDEZKeeR0AaqykssR1-Oaoj1WJB7g50nt0hgk9PFaQlJ5WlCZLaiVwNsATjB7tDrTBR-An9pIyRi0LYGeQeN8V1nyyeVD39sJ6cVvPMcYausvsDqHMvqFUDjXW9NCa5QO0_TYxFJkVFd3A8i_uCFbvey9uNpM1UHQTSdq1PJtbwD5ZWW3ZQAeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=KKVGTE9Sa8NdwshKfr9bkmUf4B9FFKhUpqrXKKRaljCtmWwjpeM2sqO0LUoAxRHWnynDG4IjSHDZoFXcX1XdyQcdkvfFs0biYlqVez2qFS0EXEaZ5afMVkKJY7_gOmOaazDRTI4W9XakEuNWOyq7ddkM6kxZPxiGJf6tElx2YIU-Itp-RxvVeZyN8KynaPRIC8V1t5cWjOaGmJu7tvHrZ8pS5-Z4ry2Xtyys5qjcBX19x2HJ_M6GuikQcv8Ofw43py4X7Q0v44rWeDm0r0rtL6yUJA39zLttJIQije6PN8EbvTCu9pJI_ugTbcTixbKGvcxUCYsDDfpWM_TeDsjD1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=KKVGTE9Sa8NdwshKfr9bkmUf4B9FFKhUpqrXKKRaljCtmWwjpeM2sqO0LUoAxRHWnynDG4IjSHDZoFXcX1XdyQcdkvfFs0biYlqVez2qFS0EXEaZ5afMVkKJY7_gOmOaazDRTI4W9XakEuNWOyq7ddkM6kxZPxiGJf6tElx2YIU-Itp-RxvVeZyN8KynaPRIC8V1t5cWjOaGmJu7tvHrZ8pS5-Z4ry2Xtyys5qjcBX19x2HJ_M6GuikQcv8Ofw43py4X7Q0v44rWeDm0r0rtL6yUJA39zLttJIQije6PN8EbvTCu9pJI_ugTbcTixbKGvcxUCYsDDfpWM_TeDsjD1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_9ROufdHEqbeMv5Wmh_-JwQlHpdWihFl7oH1DX1yiEWT8aibBOZLmoxjsEYeCMndsIGBVQDfbU4eBgDNBajssdUf180xwvPm-u7RlQMJr7LNMoeLkDYExUa_r3ymlx3bkrT-VJZ4mhkpa0VOllzyL_-aBgdM5m13Gfv5RYKS-8ayM4v6YgnfDnpNCE52P7lAVTez9oLLggNpl0nCam5VqrKca_MRpon6XSY9vk9eZGWrJlvvmkTLZVhQ2TVd3EsU1-hRQNMxW0fFBUZ-4L8Ia7SNlh04OodkYYqZ4QzLgR263e3mmVDci4VXizt8Ce8XxOedqKM61yGl2L2Pw60cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=lhxZYrEilDB9K766HXEaBFkIcXOrwAhAa93AR4G9jIPx7-5bOEiBdYZRrbTa5UKyS4_rvDpFmQa7HErdZAjTzh6gqhJwnOaclR2OCzEVy6kBAcBrJjPljpL1JSNWt51EKY4eyfv6balUzvQmizsxWF4lwJ-kHle2R4MEa_gN73tvd6yU8mwQMJQQyvLJydmC1FC0domuXWMuLO6h5ksyEY_xvai-s8N5v6Hu88V9uSJ7-fOYCHcLkUik2k4dPaGKghk9YxcYeEmem7RtmyvhYdLwb3aBW4P8VSMCfHMm-Mniz-5rWs4jdRRcLyh8Hxfl6IwsTk1K2rIcwya4fY-2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=lhxZYrEilDB9K766HXEaBFkIcXOrwAhAa93AR4G9jIPx7-5bOEiBdYZRrbTa5UKyS4_rvDpFmQa7HErdZAjTzh6gqhJwnOaclR2OCzEVy6kBAcBrJjPljpL1JSNWt51EKY4eyfv6balUzvQmizsxWF4lwJ-kHle2R4MEa_gN73tvd6yU8mwQMJQQyvLJydmC1FC0domuXWMuLO6h5ksyEY_xvai-s8N5v6Hu88V9uSJ7-fOYCHcLkUik2k4dPaGKghk9YxcYeEmem7RtmyvhYdLwb3aBW4P8VSMCfHMm-Mniz-5rWs4jdRRcLyh8Hxfl6IwsTk1K2rIcwya4fY-2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=n2dlfvEUjo_ZX-g3yrXW9FtDqI0JOmxINoZbdF7zQ5WfKy33Cx638YBhIRTwxvtyNf_gzAQgsyVEVNWP09z5zHmZsj3jDEZktOuAr4PBMYRuIFllvCT0iFK8JVxLMrHolly8AxVxDmoWamIxbE7Jzq2g5q19sL2oP1MKQAW5u9HeEnmHBaYLc-igLZg7q19kJ-tr0P3mcgm0h3jRuV-fcqilPFmq9KWtQslZDW95l_bjnwkOWSGBvQXh1j2x788OhgZmQ3nipCyW-Bq3ktqDJlWP3S6lMXoL-z-V47S-QAPidhamX0rrJV9Qh4JAEgiKH3rIUN9S0NoUCxCgPOf8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=n2dlfvEUjo_ZX-g3yrXW9FtDqI0JOmxINoZbdF7zQ5WfKy33Cx638YBhIRTwxvtyNf_gzAQgsyVEVNWP09z5zHmZsj3jDEZktOuAr4PBMYRuIFllvCT0iFK8JVxLMrHolly8AxVxDmoWamIxbE7Jzq2g5q19sL2oP1MKQAW5u9HeEnmHBaYLc-igLZg7q19kJ-tr0P3mcgm0h3jRuV-fcqilPFmq9KWtQslZDW95l_bjnwkOWSGBvQXh1j2x788OhgZmQ3nipCyW-Bq3ktqDJlWP3S6lMXoL-z-V47S-QAPidhamX0rrJV9Qh4JAEgiKH3rIUN9S0NoUCxCgPOf8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7zgzdnjr-CDfyVrOn08hKTCCBVi1mn0HgKJ0L46y77kkTYDIkTIeOwbGoZXXVISeeFoh2HcnVzgmu6ftvT6FX_pUztfMN1kAx1wPtEJo8d1iBaEAO7SnYnt236crVcu4CuDvyK2gpm3tdDAmGbrJQZI5SMn7KGuea2ygCatEh2TZczNyNg-H9j_JyQgsadtQjwtLOHywJGVQu8nN2iPT0GWLZP-S5VRrM4JoDpDUxptd-71FtS0raE6I9ZU2Aj5L8l-rvoQUZ72mSwHpMj0v4-1I3fr9yJLQnE2HPrfENM5Oi_qmMA5-3aRu-z6fqE8L29RaqOj79DTtus8NJPjNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=eG-WKfAy4jKt0GCcfsAAEtZFB2J96ywspkSHb7xs_mkbBUvZY-rwMSd4o1oO_mZeCLI6EWydovMxnHkgSsk9fs6FDdfuaRIBNipsjlBv5YeTSPz-QC2SKsbCmurXZ6GM65pS5_pYF9ArSO9kTDJJXZTBr7aVLN7i_GUtCZvx3TF_mVA6y_HB4zOBoyI8v5vm5Db2vkPMVy_xr0l07UFxPnfWtIIdJ0Rj3qg9P_2KZMEHgs_yQB2GbIKFjwWZxvDGe__YrNnAN0gk47EMZLfn7o1rcmuQvvurQrYk1WmMJmr_zF0H-OMqlMepx28i8DHT6E9O6UAFdawIsCocIgI-uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e458969a1.mp4?token=eG-WKfAy4jKt0GCcfsAAEtZFB2J96ywspkSHb7xs_mkbBUvZY-rwMSd4o1oO_mZeCLI6EWydovMxnHkgSsk9fs6FDdfuaRIBNipsjlBv5YeTSPz-QC2SKsbCmurXZ6GM65pS5_pYF9ArSO9kTDJJXZTBr7aVLN7i_GUtCZvx3TF_mVA6y_HB4zOBoyI8v5vm5Db2vkPMVy_xr0l07UFxPnfWtIIdJ0Rj3qg9P_2KZMEHgs_yQB2GbIKFjwWZxvDGe__YrNnAN0gk47EMZLfn7o1rcmuQvvurQrYk1WmMJmr_zF0H-OMqlMepx28i8DHT6E9O6UAFdawIsCocIgI-uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
