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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 23:34:57</div>
<hr>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsZTJBX_xt5fjVfaMmgI6e-PCbwU7BMBGzhqBWIfRKUg5Pe6O4hRq0o14MLWxccvDcbxAsbX34CSiElzTCO4IaLB1SEPqVIl_EB8V_UNbhkLGlq0AVlrweb5cZ_hACt_00tZHFcUxA82Z6xRngPGVsy2W7_ZLW97xpGgeS8nAnHRpdfLDxDT3CrXKEb9kv9eg33hj_ZTDf-LTzxYslMNK8q_1xM1MYl_ZB0vPlIpejJafllRsaYwLu1kTs_G2j8yyn63ATGbgyhr_0Hgc1Yo7DvQQpmqbbQDqxKme0JbQL2vD_rrVqY-fqI8rfsdDYXDsSMPJCxXckoxQbpAvpw5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPyLKqC2Ab8FwvxcoFYjY2oFfSKAUwkj9D8tyFgarLb6TIsKRE4WMVddSDEp15xwSLMZJNViL-StMs1EO-s2RqN9jYc1L00suXz_KWtIGNsLZcfe03kSP8qQwUdHoYeiapXvPImTB2ownfO3gidRSHxDS5TnQPvpj9v1KWTNRra7deoGLGjfGTWwMSBwUybvPCO7u9AjX40-1uDBxJW1VpxdWisznZZXGvT3jTg2dfH7YQTLilMvasvSeSEj-mtTBt-RaMM1h7FrAaJnmULfj0BG7g2-nETFkGxOLcPvNvJXmaA6tXvWnKC9vH4Z1m5cqp9weB62CJAp-Ru1nLt8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3U90zV_bA9BbOnca6Qm9r9tfpK8CuQ9E6ZfjBvFNbdzGYtF559tvYZIvgODN5UeM0lwK4RfPQg3eKz4zjasuAYQ0m6CmGqtWDjyAZATYYBhuYPMs5Am5w4EjKyu9O6uzGoyWJO6Riv0kQd7aPEyWoFgREsg9WGoeM-mWJ4mcp2h90Z_0MhDCEzHMLUsqYn9nOruQ2t2QCgWbPqIyNY1VCWjvqQqSbuY3jNM7yOHskubRkFS-ZLlbRTrFmXgyNci_bhN39pWeIJ8j2BxjbexIyckXvpCJnwfYHqx-FvE8yvgqUK-1KmRfpRkX7hW75nzla8ecncrMwBQUswV0jJ2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L64VijQjG8pYE3raY3iuxVkV6-1zq3bglPgHVQP50WAkVunbPJyyR3AQqxvSVX1LlDGfUboe_vfpVxZ7c5pBEUd7jdi5yum3Kdy-47EFH4Nl7PRvucPA2i6zqx16agoTcxVdukSRwIjTtGmrnUvu4HZMoX72HfU0UI_4QWy2pxWP6WrBN2cciZ3toBwnzdN5ywegKHQ_FRnNgXMnARo7mfw1m2JqfhkGBEyWOHFzk5nG6QJSsgyJJg7_fDvJkVGZLGukObfNeIkce5oFW3yKakqW-cD7wy43RC3cIJZpYRNT5tFP3zyE9-GS9oBzzQQBUvdpUX9SMzkeipqMJ-Dy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfOG8r9Le797iCT_r1O-6F2tl1IKrJXs0hhcDjwGlX56-Y1VSZjX9DosHSHHmxdD-7WTb2uN5qBfL5GHqSI6RY62CuJAxxTW3WOtrHiOF69Ni6RfArcbx5TD3O9uEWXwsxB2qnvw5lCEJZnqje-nZXdG4YdkYzcaJ3GxibPUFM4LKxQb_b7TZP8xzIR8zeCuL5oY3GhlH6R41k8QBJm3NTYGV2RzgNtpeDmVdzNFO5ODUZ_XdDwc5sxN4ma5TjG4M6Nr9rXx596qMmqnNNdc2RGXTN4HnxHvJQA5_Lun6ez4FZyYfadpFbg5jkH4gyaZkTDqSlLeU0-DreGOFmjkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAkGBrR1Wrrs-8F7EOCnSK_eDHa6IPFemHwWozUNCnPROiCVN-F8kBITQ7eLiAPkAAfll-kqLgM28jHZwsQgngLvKKZG09AZ1kDljgbZomBYyJ3mfBLYbyIC4i_HjjfddbYOpjBEpdPU1BeVm6L2EBr5rYE9XJZ4vCiF6TBFm66zyRGaADSGmvQxR5xKhgS1E09Mbn1JT8CTFqYWxwfL_k_lSuj7CTpMFQ6IWzb3KF3SiYj0mzy4dE54EyFqY4eQT3K2j3eywYWAil30i22CjyyFd9EXoaYjsgi_R3OSWg5wmDdfi3GIfaIyxvcrt3K1ocMCHQEn8rmOOFUfRTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=aPPL4ZW_lQ89MoyT1O62wgElKUiqzh6wv4C_vY5pW_pV46mN8yaZxCweiiDNu7AEWtDF6kCDHs8WdP3xYGg_016Hv2YQSYW3F1RDxkhYMmOSAv7MPPreXftGQfQvb6v8oELx4N8WEtbeeFFCORUFv9sDiRr3G2BDpk4tzju7FmcUuydK0M3BSQ7m3JLxt4SzEPp5LjpvIX1gy61mglLlwJHqwhWmq5esu7yjZeC_UurlVktOvRhZLIadEg3oluwQLugH6yahBphGzUHGwCyawuC8dGsYLuo6DGgYzuxU2c4QT1uosw3V8pRYmMP3s8N7RNxpxB1LabysWrF_Mogaag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=aPPL4ZW_lQ89MoyT1O62wgElKUiqzh6wv4C_vY5pW_pV46mN8yaZxCweiiDNu7AEWtDF6kCDHs8WdP3xYGg_016Hv2YQSYW3F1RDxkhYMmOSAv7MPPreXftGQfQvb6v8oELx4N8WEtbeeFFCORUFv9sDiRr3G2BDpk4tzju7FmcUuydK0M3BSQ7m3JLxt4SzEPp5LjpvIX1gy61mglLlwJHqwhWmq5esu7yjZeC_UurlVktOvRhZLIadEg3oluwQLugH6yahBphGzUHGwCyawuC8dGsYLuo6DGgYzuxU2c4QT1uosw3V8pRYmMP3s8N7RNxpxB1LabysWrF_Mogaag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u25nrom1IJz0Bz5uuAkuPeoPx5hGmOMR1uB5-66yoIJa4RCSqLTboPh0Z5-B1ai-u1cQiZQmAdGeUycTOmmn-9X6cw_iK1WRRYcS0kB9IQv-u1eWQqO0X0GtpcCGdsQzN37ZPDXv-U58vobAj4_S7Al-C7btCf-DA5lf9Sxo-Xf-CMjX2XAM7sKjuUxr4tWh2yBokykLoLGOlgkCr2AiFg7o7sXE2fx9H3JIASXQhpUESwt_H9xzq3AUZUkZu2bNxuEyj9M12sVu-FxZ24trnuslXt9n15MXDIYELIwUBG6aXgutFS_BxBg7CriQIQv7tuOnLpGGysJ7K3fw8ZOiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn5epKsWwTmfPFTLZD8tLHcR4o_AdQWsDybjOmsfzlBmoQoQEgZlS7eN2XgnVD2eGAAP1COd8Pr757mFAXwHnsx4mIsKvNKbl_UiFNKEyXtHMNcbHVbrEgRT3s2iAaL3tLQ6xxDRIXYMWNWtWJ1BMPRTU08xKxb3jJH1khcSo1yxfXuA1KZ8-M6JhmTkbnf2fgKFWFFb-KjMApj1K6472Mchn24x4DOIVsJlQFdvCvoosh-01AdMIfx1wWYxCBova58T-ujPxuP69QeyJeD3EVx8RcUXdO9L0KdCZRcJ5CUHUDuVUUsu46AdYRbtvJE3YmS2vnD2TxCOhQS68TySDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSDi-vRDhvRanCw_WraHhdVSz2X4wbj8WDZpvTT5VpPFz8kmErO345-IgDWbvdKMt2uevRPN_EdmeCWcWqdc4AMaP5eVBlBSOIE6Uk4K9RQB7XqPaNX4PxKKnWD4zNCSUWwDbSyPM6haDyEAZtKAF5VEOB8fMcKn441J1jBD-o0PVXw3y80fqf3sbkn9WK6__zggcDEauXUoca_ZznuWOxU2-GTTCQKL8-XJvsmlHO1VImvld_DH1pZE4AE-m6k3eWss_7b8CjGX_gXLZOFvqcg1tI2eZjFFqhtas2_8515-_9J41rr1aDdIN_xDWiDRJVSOPG2v2_TLystWJGGH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=enT1IdZc9bEK5son82kgSfblFxaMB22fdGaB4oyf57ZjHJjrthdfkX0avwD5qX7GRYhwIH0hCW87l2pvTZqzFaje-1wMg9s0JOYDWYG8ynvI-qP9KRfS6c_b3VuCwzxLRFLng0HkRD090BCX42h6Ckw2gntFAWNK5F1fwIY9uV3odq7eLcc22nzpyF-Im8n1ZwDhIIAsLtZ6Zz0xpQlH68TejjK6O0V2rtN3e-X3XVFFZHyNnRcbw-Jmhi-RAaIwMLrWDFQLTYMxJd-c_vYSEJoxzztooQH8eoVwvJswKxgv-Gh-61O9QxvzDZrQs0zKLFwp_1NUtELnyfeJiPwEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=enT1IdZc9bEK5son82kgSfblFxaMB22fdGaB4oyf57ZjHJjrthdfkX0avwD5qX7GRYhwIH0hCW87l2pvTZqzFaje-1wMg9s0JOYDWYG8ynvI-qP9KRfS6c_b3VuCwzxLRFLng0HkRD090BCX42h6Ckw2gntFAWNK5F1fwIY9uV3odq7eLcc22nzpyF-Im8n1ZwDhIIAsLtZ6Zz0xpQlH68TejjK6O0V2rtN3e-X3XVFFZHyNnRcbw-Jmhi-RAaIwMLrWDFQLTYMxJd-c_vYSEJoxzztooQH8eoVwvJswKxgv-Gh-61O9QxvzDZrQs0zKLFwp_1NUtELnyfeJiPwEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=VFstiSnr6ez48wD565qxEq_mDw1d_v_108lOCYcSp7MjpJlzl4VGEl7GRykNBUJC___UydtBpFm2UEqmQbm08xPQiGihYPSS0NUTxRy04-FqRuRLBbYYr-lHk-ZrMqvgjcO13nnqqMqsp9mGZyABbABhaAJ0E-iJjIQ23G67tS8iOBld3o8Ty1f0S7D2wXuza5fteIqHRv9WmTi0x8S_u1kWv_QC-_nn7IA8fAD5A0VbvRIOGhdkk7QXWc9sROo40lNxXQ_oDC7vp1Etgn6lg5Jgp-FI-GcPGGsKrcWFNV3-7p-gxbhAkJsToZx0sK2uSaUKOgICp32fa4Ak_Bj_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=VFstiSnr6ez48wD565qxEq_mDw1d_v_108lOCYcSp7MjpJlzl4VGEl7GRykNBUJC___UydtBpFm2UEqmQbm08xPQiGihYPSS0NUTxRy04-FqRuRLBbYYr-lHk-ZrMqvgjcO13nnqqMqsp9mGZyABbABhaAJ0E-iJjIQ23G67tS8iOBld3o8Ty1f0S7D2wXuza5fteIqHRv9WmTi0x8S_u1kWv_QC-_nn7IA8fAD5A0VbvRIOGhdkk7QXWc9sROo40lNxXQ_oDC7vp1Etgn6lg5Jgp-FI-GcPGGsKrcWFNV3-7p-gxbhAkJsToZx0sK2uSaUKOgICp32fa4Ak_Bj_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=pFKIGxg58xYsnwbOJtuV0WuPh3mkBaXV7qMJSfj7UIMyEjrWNv_wmAmc5l5FPVUF_hpz1oY9AsA-hGmxSYIARdanpKgX1zq3I9Fh-UcEZNkywoFhOjNbXuRVj1MoBAT6oyHPNrY1KXV6b5l_A6rV-7qcTh2WaHT2Sl8cvL8QeirfuWTC2vmhuhZQPc8FS0mJp9dzSPAzvbyJQNe3yU0anNXYV93UPaIH_B28hQO8L2EuSin4g495w8ZH9egwjP_c3DSya_IHO7_Nds3SGVHYqfb0OFu-3uxWHMysG7WF2eKXyDYT7uGzlOT9sk34xrOiuUDNzKdcCX78Z-zsheUfppv35q667DSIbNUYILZ7zJuGqIi8ajjf8CjvrY-BZoAoxcnyCWhhzcG3xVBzeC8oEnCznBV7ovYYs4QHuH3Uaq9T61Y8XLcFrntxY8ZjmVQM6lGLF_NlVMrj1wIRpApPVB7DSPtdoY-_RmQSH79yvg2SiSqkR58p8lmRWY7KwUMd1KEdJh4lLuQze2vC1wczLOgN7x91W2RVq7WlRps3inRO_Hxc4YwA5A_9Rf2rrUUklM7WqfGWIsy6bomQiJkj-tCdPfxRLsT2UEC1fOU4edoaLmkOhF-QnIljhaihEAaFJZWxOkZBZL1A0nhwOKR9VhXGZP3iJ6dQKXfjWAvzQ_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=pFKIGxg58xYsnwbOJtuV0WuPh3mkBaXV7qMJSfj7UIMyEjrWNv_wmAmc5l5FPVUF_hpz1oY9AsA-hGmxSYIARdanpKgX1zq3I9Fh-UcEZNkywoFhOjNbXuRVj1MoBAT6oyHPNrY1KXV6b5l_A6rV-7qcTh2WaHT2Sl8cvL8QeirfuWTC2vmhuhZQPc8FS0mJp9dzSPAzvbyJQNe3yU0anNXYV93UPaIH_B28hQO8L2EuSin4g495w8ZH9egwjP_c3DSya_IHO7_Nds3SGVHYqfb0OFu-3uxWHMysG7WF2eKXyDYT7uGzlOT9sk34xrOiuUDNzKdcCX78Z-zsheUfppv35q667DSIbNUYILZ7zJuGqIi8ajjf8CjvrY-BZoAoxcnyCWhhzcG3xVBzeC8oEnCznBV7ovYYs4QHuH3Uaq9T61Y8XLcFrntxY8ZjmVQM6lGLF_NlVMrj1wIRpApPVB7DSPtdoY-_RmQSH79yvg2SiSqkR58p8lmRWY7KwUMd1KEdJh4lLuQze2vC1wczLOgN7x91W2RVq7WlRps3inRO_Hxc4YwA5A_9Rf2rrUUklM7WqfGWIsy6bomQiJkj-tCdPfxRLsT2UEC1fOU4edoaLmkOhF-QnIljhaihEAaFJZWxOkZBZL1A0nhwOKR9VhXGZP3iJ6dQKXfjWAvzQ_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbUFCs0j0pgsyN4svjRDrHlMLYu0YzTvvE-JRIa5aR4vHihBEvY5peLpKUA5A59--B2vkbr0FhBBb2H1-knjTVl7DJ6JzFyIskD7E-kx75ArKndotajW1SYvdtyXzBMK--iyPeITvXAiKf5MWuhKh_IuU8q6c0VF51wlKcXKkJsAZVqoHbaVW-XqAfK1zUQapPqomTXhpoGP-lEtm8AN9wn7xn0f5RAWqdk4ofDDOr5SWtjA2RvMzB944-rrqle8iO-INDptG29tFG7_nvkmvQVPgTSZJceKQqrowru7RskdNEqP1XdnWsGWH28fwrz-FeAAqvgSXPI1JshNvKr6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-QhlJA3DAIC8B_HxMLN6SYk8bkWMBFc2l8_iItGu3eaDpOCf3BzVBeRYBFg_-yEWNuYkLZU1cV7NKcimtqPaQllbNNObTWJJB5gejKxsg0GcpOss7bZpmFm-aD47fbPhPcef5UEnt4MHGTtXeVxsgX_fHTcViMQFmnPMbcxhJeRKEHZYShxu9_qtKyNNVTq4-2AIDoOi2lt5rr9e3JyXM0RgtILzwScBI8Mv-Z4K_YCKeT5mxBSZnzHP4QNrjdp4cJXXFv-16PQ7XEJmTm9QkbaFCbp4JvlrcB_2mGV81xHTkXefm6xX8ek6dFl-O3aKO0-AGPOdojwvUJ-DITnxF4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-QhlJA3DAIC8B_HxMLN6SYk8bkWMBFc2l8_iItGu3eaDpOCf3BzVBeRYBFg_-yEWNuYkLZU1cV7NKcimtqPaQllbNNObTWJJB5gejKxsg0GcpOss7bZpmFm-aD47fbPhPcef5UEnt4MHGTtXeVxsgX_fHTcViMQFmnPMbcxhJeRKEHZYShxu9_qtKyNNVTq4-2AIDoOi2lt5rr9e3JyXM0RgtILzwScBI8Mv-Z4K_YCKeT5mxBSZnzHP4QNrjdp4cJXXFv-16PQ7XEJmTm9QkbaFCbp4JvlrcB_2mGV81xHTkXefm6xX8ek6dFl-O3aKO0-AGPOdojwvUJ-DITnxF4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb3rNDbrxBlU7uzhd02-XrloK15e-UBL7x1BNhMUhBxI8jf2O1Wx7t1gpVC2KpVwJAbHGAzgldL85VpglvekMmtOoQUs3_VgFwGo5tNZxdZjKzKGBYTokW_ywCvqiS57n9-yAvwK0Ll3CI_ur16OKNYIw7fHiOEpFrk6ZBPQAOqrYGD_SVqBYSF8CPOOzSWWIZrdRdB9_Frg1o6BzayxxqneSPxSIVl1XF0dUDt_Xe1cHwixW2s8TfphQZXtGwsVpjLdkZe-dsvpRseYnVEtpQTok6NjExMf-JChqVz-clz8_8bf1B2_d1Otoxy7Qy9HhYx5TXl7EsxcrKYXu29Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKObD2KT_XDwaWWAFrDYfAtVR5CcePe97ke2MDf9YJhuTEHl2vhQ22JG7z8cHP25aaY5T_HMd0CRdFee62kso7Em0wlbEy56NxmmeLVZGQA3DE_tlMgfgLj800r9fiQXBy7ResCRJ5T7QGAMn3t0Qw9NIqATEmgAQNqu86jP9Ra3n371zSWOEmU5-hf284oEkF_74XZk4NEnb_o257SYvUPltS6ZwO4dGLxS3j6Dj3QgFMbwOBvIOL2kQn7PQ0FS8CjZKzLVD6t1GznNjpsWh7kBvA5BEX2gg6B2eG9YO3cg35w9bQXwCTevLJ2WSiJeTXPa29Si-gVTrzdQPx5kGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mptO0f9dQgnLycw71FsEuPJXwAV4Mje2A4Xy8acIcGyPnvfY5wvYJevXVCvWl4MEnA4OrLIydOAI868mSUTYMcZC1Oo-il8j_YpAnjrzDoV8v4vOpNLYZPwZCuy6MlSIjYr-gbKRgPoQPCPchYALBjThmuhPF6UXlIKiAzjCo48z6526sLFr6TYkjTnDZqS9xwDdPLKjKg_YPmvm--HG3FV2EoXCvjqXDtJv43aYd330TS4etrqh9uvuVu1H4h984uXRxGM7sjiQhlr01PN9xiFHXGORCK2A7AObWtij5Nc1h1rE2ik0npmL99peqFWwryTK0qo8wL5StNrLNZYOIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_auA3nEbZf3BF_cKKfX-tj6gr6heBpVDDOTt8PuSgKFWGfU5atPovPxItb7tXSmB40w1FSyT2PWBW-gOQKhilWF4LCFe2zCMBXdwmwPNdQpiD7fati9lf-LrXG5nLWma1VVmexBtERj6pCsPGs5-ryIQ1ZGujcA1FUJIAgiTCy9bk6P9iLW4zai1LfoMcQ8vPfGGCir-Z9BKr2kMjN43C8EES53qZjsDIqBj72M-fmqLr8-F1Veop77Sz9INd0_OAcyRvfavqEl5XdHSE568h1KC-oS-GVOpexd3OX363yc039jm28vNVbOV7JV78Lv6VX5FUwVb4cEksAmB2l1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM59GiTzE2LKFVTL0JeThp67PAfFiFZQsA_lvmYpCYUyIlh7v_kUbU_eHFbbFyJUdgLlvDqiDWwjbMSSfcmlmKZCGOnaAAOlASxefFKp661nfef6dWMicGcqDUnmP1Vzcj2nVO_jl4OMmtYROrlNlPM5PvBRODMHMpE4fayhYF7x5cwaxY6G9S_02Ppf0IA_3ljpcNHNqcJW7SHIdXQb7rOAItEBzwR9l1oA2YMOfU1l_q0E9tWBlJaTY7nPrT1R0-R4iBDeMoLrbcfBqolaKAj5oL967ucr2Q629_fFT02QZwUPk6a7xKygSbd7dyQlRYiH0G3bhdu6NFZhwWZwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olhynLHfUB27ijN0dTf_P28n3S5ejjp6LUqi9UaaYjiz0fyELndYzQww7SVKzQAxr7Ijhf_ponSsS_rRb-yMvI5pw5XWFBXbomjCoBAEUcU-77hcFb1pGlAsGiM2xSuJqNAbpHTYSjn0Z7irEhX7XvPmpvqq2Ui3cg_bJv3Q9F74PEVSv8kCL281dYSzYAfKfkIs7Wrm3TbqG6dIe4iPuhl5XmMqg6fwgBYTFdnj8xdHi67us6GcVfREHU6ktjwNy_gJKoyw8tb63FPJY63FOtHDLtZxaDVR_LC9vs1xF5sX5Mjp1ZaIGlSvfnp_qffOeO2s3mCLby3s3iOB9UsG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=XGxSaXI7xLRRwMxWtlSu-x7LItME_8R3rFE6f6BPyrdngSoqrrCElTLaghujiwulsbG_v4Sufjlxg2WNfBvFJvEKDBhyQgQL371w_zJCvhFem2GPwRsMXTIV4ZjCzBo0XLnF0khy-7CyObaDzGakKwfHF7VYcfGrP0K0JAp4n9skfnaA_UBtIptWpFUIlAN_1mMqdpI9CWeJlXkOCmJ0TUlzu2Xv2ZRspFoequMkPOn5B7UWd0xZZEKTFPYtcS3SOVEi18hquDcqdzFCNSMlt3Q8vaQeEleF2RXvgsCn_C06uYNbwjtMjx9e3ix2bMxyNwqBPX47wV098OnKscjnow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=XGxSaXI7xLRRwMxWtlSu-x7LItME_8R3rFE6f6BPyrdngSoqrrCElTLaghujiwulsbG_v4Sufjlxg2WNfBvFJvEKDBhyQgQL371w_zJCvhFem2GPwRsMXTIV4ZjCzBo0XLnF0khy-7CyObaDzGakKwfHF7VYcfGrP0K0JAp4n9skfnaA_UBtIptWpFUIlAN_1mMqdpI9CWeJlXkOCmJ0TUlzu2Xv2ZRspFoequMkPOn5B7UWd0xZZEKTFPYtcS3SOVEi18hquDcqdzFCNSMlt3Q8vaQeEleF2RXvgsCn_C06uYNbwjtMjx9e3ix2bMxyNwqBPX47wV098OnKscjnow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sruAwGZfS98d-G6n_R22OIuh1S3KLXakicSftTs7bOQK84boVE6RHA30tv96YgFo5H2u_R2QkUHO4Ku8cR6wHxHftrOddBA8ys0OAJzQYqWWvGGyzC39pNrUccVQnUT49eUwaNkms-7yky8u1Xc4nDK8WSp133DQe7BUNrOkKld5iOxthYgp8h7JN5D83vANp3rN3JLJqkhFRx8NEE6NEDoKlfaQVSUZq9_y6dZKWbUZFRMFOqkaYFGRKFl3sVf8p6ColdU31pwZ3D445bB1lJxvLaGY18eAKvyWrFnTZMSDsMVocP320uKODgnibMrzQyWP78u8ziGNJasJgwP6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftqkjGOjdqDoGrEBnC-dQ_MWrBNE01skpd5j1oX-rTAsUKCyVJY_xoQIskYxnvZhJqUj854vhCJe1xjhwR_HTVroiKLmmVXSxjeMvwL-Yz7eBrrNS2kLiyzCg4l6jdHC0oCPTZqTHGK0yeKhs9fSHoPCUhblInFTLzjZCTcfgQkbGP_DZDWIopesnHtTxOIl2x96yMsRTuCH29vY8HtjmjqnzuYRaH57J1MOgHcyI43vh0Yg4xywHauDyHd8hPW2ybHTcMdrn7SSFpMQfGjSvLOLXFJKIry1xc5lMi0kfiZhOZ-D9TP87vxJIDtwXA5RZCK2B94agHAvoz9oNAPmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSs-HXG2VQnAWxegHMhZj0iX0Vcr84pBynDRWJN5GtTXLJOz3sXHlcgjcm883Hx-v5MybTuAQ2bkWf-YM2GGTzJ33LUwLZWlLB3XwJWGORn9WLz1_jr_5DXsx00e4hJZJ9UNPNduvy76e7ZwBWTsssJGq3Qma8EIakiiKvm18tVJQLcPIXWOdVZLy6B_-bbYovLgrc7M2WIR59OVPvDamBomf_zyL0dxG5BrPYfebaaMGpCHx-vZ99s6OWoHUfNgxnj5K1HXz-WVVUqegIrUIgLbfWro2eYpyxoNVuDEuPyRfxaKCdJOmC5Vr7cSEMlmbWuA_uCUeM4CtSe28xTr1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=mQNDbsbl0q0_Des3Tt8zNGTv1wAnBpXDxlTXEaYtlsnywhtvFQp5xRzAMgtB1gH-XR9sHKQ8pacEHecHtrISFW6jdKQqu-bn7JwgVwKVFLiytBermzhwIczPGrIYpmM5-8YgSPf3EyMlz3g7NMp6FNhdkbrw9lOGjvb8-OOE0SE-WbU9k-3CyNjJzlygC9BeKqNxkh7wKQobFuGs5Msg4q5gai118m-pBJitiEJXpr7iksEh1Yekmum1ZSqLdh_2-wKWJTn42eS98js8axh7PFpwNAcXRUW3kE6u-S3w0EoxwZ9VFDDQiTQxd7oIr6AkKi8NRRAuH2NFWWpxv5I4Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=mQNDbsbl0q0_Des3Tt8zNGTv1wAnBpXDxlTXEaYtlsnywhtvFQp5xRzAMgtB1gH-XR9sHKQ8pacEHecHtrISFW6jdKQqu-bn7JwgVwKVFLiytBermzhwIczPGrIYpmM5-8YgSPf3EyMlz3g7NMp6FNhdkbrw9lOGjvb8-OOE0SE-WbU9k-3CyNjJzlygC9BeKqNxkh7wKQobFuGs5Msg4q5gai118m-pBJitiEJXpr7iksEh1Yekmum1ZSqLdh_2-wKWJTn42eS98js8axh7PFpwNAcXRUW3kE6u-S3w0EoxwZ9VFDDQiTQxd7oIr6AkKi8NRRAuH2NFWWpxv5I4Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=QsNqQpiORNb6brhAJnZ9LOUox8nqI1f2rqMlAOfo_Yu6Nf7CZc623pmM2As6Z5NetXqCxHjBD-XI-g4zohnzIujnr_X_U0cAgu8cZkfBP6RmNWzI-YOXHlsmkwTxoHAR-qx285mIHT9QEIIwXSrC6IsKFbPSOuTYnWzXYl7cME4oPQ52ELPJwFbVfiIjmSsT3ESraBOKDsLCFRXN2KaU6RWnjScMhmASDrqqmJT9HnbyRZ-k3-5Lo561jvKgXHWh4AyIbQtoYBFQoNFXePpvcSg1wT2k8yiYKrFD2kop6lF8z8Yoovy-SGjoTBbphuJV7vcXRPdLEMy6PFbkv7JZBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=QsNqQpiORNb6brhAJnZ9LOUox8nqI1f2rqMlAOfo_Yu6Nf7CZc623pmM2As6Z5NetXqCxHjBD-XI-g4zohnzIujnr_X_U0cAgu8cZkfBP6RmNWzI-YOXHlsmkwTxoHAR-qx285mIHT9QEIIwXSrC6IsKFbPSOuTYnWzXYl7cME4oPQ52ELPJwFbVfiIjmSsT3ESraBOKDsLCFRXN2KaU6RWnjScMhmASDrqqmJT9HnbyRZ-k3-5Lo561jvKgXHWh4AyIbQtoYBFQoNFXePpvcSg1wT2k8yiYKrFD2kop6lF8z8Yoovy-SGjoTBbphuJV7vcXRPdLEMy6PFbkv7JZBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxL3nBrRKH4AW9AOUqWQw-xxZwFUeEl90K84oIyY4CGE28nr9hcP9ymNU5IMMfZh392A2_7LfpF7ou5wrluJC0f2geofLOpCSQNfPXk4ohxD9Wgyq2tqJKjTKh3AHtjZGd-3EpDKvh0hygsR99oZC4ysTcLvZa7NT6dePkCYmIAunRmG_mc6AVWKFL4_ip35rd-8CSu8_BJeXxLl8XgI39-_Ma_GsTSwv58r-pQ69LEX9kvBm610OywVSJuzkoccFnKFTM_lT1-IC0iPH46RCXQYvLqA2ilS8pxLHBsNuGYSsK0YhPoOuzsQwl6g-B56QsFfgGCqB4O7nwUMY9AvBd3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxL3nBrRKH4AW9AOUqWQw-xxZwFUeEl90K84oIyY4CGE28nr9hcP9ymNU5IMMfZh392A2_7LfpF7ou5wrluJC0f2geofLOpCSQNfPXk4ohxD9Wgyq2tqJKjTKh3AHtjZGd-3EpDKvh0hygsR99oZC4ysTcLvZa7NT6dePkCYmIAunRmG_mc6AVWKFL4_ip35rd-8CSu8_BJeXxLl8XgI39-_Ma_GsTSwv58r-pQ69LEX9kvBm610OywVSJuzkoccFnKFTM_lT1-IC0iPH46RCXQYvLqA2ilS8pxLHBsNuGYSsK0YhPoOuzsQwl6g-B56QsFfgGCqB4O7nwUMY9AvBd3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0RXO6Ac_dCisPaKgINn_bML1xIRCouCSGojDOeo5uVV26iiHFgVRQPSzvEBwB_e42l7VxP0kYOGEnLt4g-kezLAk1BzpCMde28lAgw_CXRpMwvs2Nvj8f48PYpIylHGciarjHZNBcnLURCIgg6zOcn0zEQNzmyJDi8IJDEQjNTV3yy2d4YW95jnP-pJH4hOjnUvACwyq4dQmdjxI5BDcSbgLJGK7q-ZMH6G5bN6CZes2qbfex9dYyCfyW9PGTxqI8lNvPKw3bhiZAlBMwCP1lPHfX-Kt2Iiq4uoy1IuAjlPzWSpmlG9jpKngibKmR23thijbTs1sgjQ2qFULaG0cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5JaKVuQvcF9XXW867hZV3JoiVJ2RoGELN60I7Fdp1sAr-FzMOuM4BmrakTQlTA7Y2eCN1pfi3EXeWKgnCiKzbbhgfgiFXtzdmO5fMsf-8jQuXOdK6dRAyXyP7a8n0BYMakvNHd0gWFpcpZMr3vzjcu3FHSZUBNHi8sCV1tMJK0LnLp0F7uByR2qE8K00CH03R9xtOHhnowU5F01gfHnw0_zM6fXiA48YrZ-Y9IzYhQjflvuwAGWVUb29vRJTAhptMHtTIqnLSm0Dr_nv9R38TVD0NnqHVNVImiLfzvJxycDg8lIb-W8pNdPv9LM2UYgkJ9aflRr5djALEfZujg2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=qlU-aVCele0HGHEgr1jX8baZqs9YP6wcot8B2QnUe0XNruSAPv3va4OZVG4QTDNLBJwkOZ0y63c5_3Ne23KB25sVn0DJLTncfd9CkCko2Fn9L4iV75QAiwXdjZJr6WWk0SGoViUMLJvdgy9bYXfbycOTZOoeBHNjsjVCuZSD5ihmiHz4viBzDmwBMF6VNVm2CHN8HB66S0FvFlu6utNM30qG0hru_N8v9bwnJHEHTV37M5B6dUZCLB807sdc_Jaj4xfPMzj1p9FUx5N9aemXNQSKV2WIeOEC_sSgItwvRMkqXy6XOqvUJP07p1mQ4t2LakzIR6gHLCef1yK3Htz4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=qlU-aVCele0HGHEgr1jX8baZqs9YP6wcot8B2QnUe0XNruSAPv3va4OZVG4QTDNLBJwkOZ0y63c5_3Ne23KB25sVn0DJLTncfd9CkCko2Fn9L4iV75QAiwXdjZJr6WWk0SGoViUMLJvdgy9bYXfbycOTZOoeBHNjsjVCuZSD5ihmiHz4viBzDmwBMF6VNVm2CHN8HB66S0FvFlu6utNM30qG0hru_N8v9bwnJHEHTV37M5B6dUZCLB807sdc_Jaj4xfPMzj1p9FUx5N9aemXNQSKV2WIeOEC_sSgItwvRMkqXy6XOqvUJP07p1mQ4t2LakzIR6gHLCef1yK3Htz4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdOGJXuogdbNH3JU8LIKDyqa4XIIXoxnBtEfpiXpgcuLrgRQzaRIk52up32Zc0NK_5kpPDI1oySQiZslLrayeyT8I5oQn1vZKvNBq64rlpxclMyq8q3ac6_dqXPndCBAeIvba0F4Mb2ceR1FIBWEnEIOpFnyHcUErpQMQHPxHLk-elrMIpPn-6ySsdP2My365Tb5alOe4N9vydZlIj-aL3f9rDuwQS5ATdWnd-1pWDlPx3XGywp9hIayJX-4TxTVZ2f_Y1-gA5nde9tPX7T3-pmrTRR30yTVNOJLrty9RcFj_swNCustqMlE_bGn7XR7OxGf2I2ZhYMdLxNtdaI6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=ENLI83A5w8rSNrBjLF8RFO9ajCyg-vzi6174PTZ8NHwIfuHXjLfcXwgAc3-lGEVb35ajkarwgax_PVI1SqxARhTLUL_RaRBrUhsLtyvGiCL7nnGlOF0llESclIiT6hulHVLpxubhQ1oVDa_dswdHOy3-CWdUaofkKH-woOZV7zEDkgEvYViZH3yP3O4zeW09kpdVQgJpfzTH5HHebUaXq7RWwwTYpijjax7k2CpYmidSvx6fo4v5cO8NJh0IBhU5_rXIAu1oI_ztKVZ5egFEYNE_2pS65Q9ToVQ96doTS0dkzmy3C4FasiyBPDpYawu67so_7KxH123D6ZspNNsFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=ENLI83A5w8rSNrBjLF8RFO9ajCyg-vzi6174PTZ8NHwIfuHXjLfcXwgAc3-lGEVb35ajkarwgax_PVI1SqxARhTLUL_RaRBrUhsLtyvGiCL7nnGlOF0llESclIiT6hulHVLpxubhQ1oVDa_dswdHOy3-CWdUaofkKH-woOZV7zEDkgEvYViZH3yP3O4zeW09kpdVQgJpfzTH5HHebUaXq7RWwwTYpijjax7k2CpYmidSvx6fo4v5cO8NJh0IBhU5_rXIAu1oI_ztKVZ5egFEYNE_2pS65Q9ToVQ96doTS0dkzmy3C4FasiyBPDpYawu67so_7KxH123D6ZspNNsFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
شنیده شدن صدای انفجار در محدوده جزیره قشم
‏بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است.
‏
‏بر اساس این گزارش، هنوز ماهیت این صداها به طور دقیق مشخص نیست و هیچ‌ یک از نهادهای رسمی  نظامی و انتظامی تا این لحظه درباره علت وقوع این صداها اظهارنظری نکرده‌اند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=PFwNCMNHZ_uk4eg6UQ9H-gU9lARb_zM_fLSaU4_RDzJbCvXJZN0i_JHjsgTA0l0iH26MQ8akxuWytjsV68lylKeuTDhBN0KUQlMcq2XDPLvUrWRrlFTJzvXc3Kj8SAG8LTWYmtNzEMaSYg_LHgF23hojQe7wA0ibA1BE59F5pxdYU8nOyhQPfRZVTi6Mzcoyzraju3K9qmOkU2lSUr1O5xJTI5hUt_7J4a0_TynWuKtLGI3FU5Bx7uiLzAB_Ne00Az00XA3qwcktuuM-_JJmW_C39cf0pR5SrRNS2XgkQPum6RDzvh57_L14NndNE0e_PK2hMCr9msD0aqImMeSYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=PFwNCMNHZ_uk4eg6UQ9H-gU9lARb_zM_fLSaU4_RDzJbCvXJZN0i_JHjsgTA0l0iH26MQ8akxuWytjsV68lylKeuTDhBN0KUQlMcq2XDPLvUrWRrlFTJzvXc3Kj8SAG8LTWYmtNzEMaSYg_LHgF23hojQe7wA0ibA1BE59F5pxdYU8nOyhQPfRZVTi6Mzcoyzraju3K9qmOkU2lSUr1O5xJTI5hUt_7J4a0_TynWuKtLGI3FU5Bx7uiLzAB_Ne00Az00XA3qwcktuuM-_JJmW_C39cf0pR5SrRNS2XgkQPum6RDzvh57_L14NndNE0e_PK2hMCr9msD0aqImMeSYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=v8l-7vdg3PkNklaDA7gYnql_PXZKZ3U-z8tSabGXHy5qkb2-VuJwQi9EMPBRPqMGQ-__tU0Xs2LAe0I87bFPbqQ2K1dJREKupsvYzQgfKjGD5XObFs_kR-1w7DzNsXfEPBk7uVm8wqdNx0JYwpQrt546d3Eww3w4AUTNY7QtEYj1mCTAJiCBuFUna8Q7T5sxILihLWg2JmTfs94v5FIDJLQYkh8BjZ4K624B52mru_p-QkgeA9S9pPsDkTXSYwqef2JiZHI0kL8XNXM6QsNP0LuALXk5NwE7jm17pOST3r_H-clkfjk5utaeCMfua3kl9wg0O_GPJ8EW4sjc3lLxwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=v8l-7vdg3PkNklaDA7gYnql_PXZKZ3U-z8tSabGXHy5qkb2-VuJwQi9EMPBRPqMGQ-__tU0Xs2LAe0I87bFPbqQ2K1dJREKupsvYzQgfKjGD5XObFs_kR-1w7DzNsXfEPBk7uVm8wqdNx0JYwpQrt546d3Eww3w4AUTNY7QtEYj1mCTAJiCBuFUna8Q7T5sxILihLWg2JmTfs94v5FIDJLQYkh8BjZ4K624B52mru_p-QkgeA9S9pPsDkTXSYwqef2JiZHI0kL8XNXM6QsNP0LuALXk5NwE7jm17pOST3r_H-clkfjk5utaeCMfua3kl9wg0O_GPJ8EW4sjc3lLxwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=piCqfbbqQWcPasw74yGRuKz2LYY90y41EWPa_rN7rCuR6J9v4PfmIt-KzDi1RMCV9fI_GKcTEfR6WLJ9IVw_N8m7Jukv9G0CsLGCigDBfT0ShLZa_c5PsbW2yR86ky_auvfwFcTWQbhAGs2pC7F79joWJ3eYmrr-jonuR6blx0oujNQ5e6TfDO0_hozr1t4SzOR1HHeS7LhwgTVhPjcj26dtInjj89YLq2Iul0xQSrsWMBIFexDmC9qFf4GO4Lk8cxUIBJlNI_DMNIJg_PzJkH1fukYJoRl66jNqX1qfN3xmlM_YUn3WOknbWOljLlWchIGiJ48OtcLkxvVbXpwb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=piCqfbbqQWcPasw74yGRuKz2LYY90y41EWPa_rN7rCuR6J9v4PfmIt-KzDi1RMCV9fI_GKcTEfR6WLJ9IVw_N8m7Jukv9G0CsLGCigDBfT0ShLZa_c5PsbW2yR86ky_auvfwFcTWQbhAGs2pC7F79joWJ3eYmrr-jonuR6blx0oujNQ5e6TfDO0_hozr1t4SzOR1HHeS7LhwgTVhPjcj26dtInjj89YLq2Iul0xQSrsWMBIFexDmC9qFf4GO4Lk8cxUIBJlNI_DMNIJg_PzJkH1fukYJoRl66jNqX1qfN3xmlM_YUn3WOknbWOljLlWchIGiJ48OtcLkxvVbXpwb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjcEsn_aHo6uO5IjSbdumH9OTSULTH6xvt__1OwqS-19vmhC7poLQl7qNLPMaJcT_2RPsle1hpcnBepzNCzhPHY6j4UrQluS0lxD0YkFQznwxJlvO-seKeQiFRTspVQXIDjPTEYZdpWQtQRWfVSMNMx6X4Maaa1d_LCRrSVPMO6rtFIcE386J2eOxmYebVKwnvyplqB4Hyfxf3Sjz7_apLvyxR7dpqL_NixCZsXib0N5FjFG8MUxsKkq16RrOhFb7EafDAQbEt_Yz4EIuEe8SyrT1R0RA9yiA6N2hhOfaNBvC3aiFFFeyvhDBnIntj6tBiCxCAGDFGJO-q8My2NzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKGxxuZLWztJQ4Id_859aik20pCvmL7QirGusnsDrWQN4gpAJ750YctjfDlJMH-sPi6HEtVyArXD9memEBYUmpOTTrvbKvxXFAZOvTiIKaYRDQ3mlNTuow8IaBP0B_-KyWzdLGwrkYF3raDNHFl7mv7RTmjJVyDIPXb3SBGpF00kg67s19ZJeAmQ1nQ7U8DU_MumVgzhI2XUDWiI7P9_baFNgi_idi33wg46BEOL76lnkg8O8EBEGXrlw2gtfW4UoNC4XyaPqzD1vp4os__t4ob2r80llzzm0glVB9RfS-SGy4GsBGCjWfvv0UzB4YbERxJ8lhslEzQw0_y2NbIZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJIOOKQ72oHMDRIzHRj6ol9v9TIppDkU-Rq3240rBWM0mlSQlWSpSzH2yvM58qTxq0Hnc09nhPg1H5Q2scGBSsrCreyeH4NKBBy-cfiTszGlXfn90L9EqVHeAk885laUJ3Pxu1UsltJwv3825guloy05MSMXPgIApcLO60gs72lcLIK6nl4x6Y6dpw_l6OZ4PbVVmN3JEH91XZieP7Yic0-O7ZUBHoLgEipCypecATg_asKZ9HGqaLSqrOvHvCOAwlqJK92vc7jowt_J0I9mjmYpq65d3iDs7jGvnF8smpHPVLF2VcwVV1bi-QQn_OHnEYQkaCX-_YboBGzY333Wqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQzqWOFJX4D-8_ew64fow0jzUiasodku2DY4l6iS5rcwwZtYWSpN7xK4FdrrpwfX4pbMAylLCDQ0fjUpE1xBjoM16GckinmhuFIt0u8QfTkNTLP9zs-2kTmmaNS4yOBl1w5pN_Q4d2pmZ_uqoGf8Gq97eOwDI3zkeHYKIM6hx12LrN-_GD6iYxIMmiGv8Hn3pmqUhDCSoOdyPc1mdstvZOZWYYuieJAStY4gz71HK4KMPnJABlfYeG69sbczf-OGVbS3fC7b7egdfX_iaiNhLT-OSCpfNdd-fa-qKo31rQnSVe2bn_4H4YKrXdv-P4bZ-DsdL03FGgQkOPai4cjc_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBmejKZsQEwhMs1Rvu91f9xT4_EOCP1Vi-jhttXfngYWekyXh1VjfJycKBGF7Vu5VThzM0Ctu74NJencq66ueOVWrms7bSmY9Gx0qi-ys-0VAiLk5dOC-Czwsa0LD4n3-At7bWb593TVBkA17iPhHj3ff754wqA4Xywx1qgu6q88ouee1r-SK-ENAaGDgWMmNFpwYVb6cNbuqD70N2hZtvd306G2_zPOC5cAsc-wze1IcxWXw5cDyA-TwD4ogqk1BGvUWC5o6iGNekZMlb7UAQGEZnhuL-LVD562XYrVxP7CnVQk43LPkUd4H5yHRdJaj5Ov0m5GoxS2_JQi_2ZSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3jkgg4TveFDZq0btJZrMn0XPwwHGsVhUrBOA0lFqhBKICJB_dCnRlpPuuie0lGTPe8IB8HDLD_7R7wbSEiRR5f1pI4ll5b2bp9yvhQ9fvV2deClilAh-_aaG1iUEAc_YGqyHf4dYO5DRuTFoiwWbx5_yz4a9aLM6RJLUVYzOlS9On1eMeCJ_Xrzg5mNmo4ZlW4IZtC_LvDk1emn9VtMVVO2wh62yCsInWIHphrgnGpUEaH8QpZpoajjBVhjBXYPRVtnPmJyJbMZ05UMfzfOn2wbeqwyX4d41nPE1ATDLo9ELS410L3w4kBXWPGVBg9q_34-BqsrdEMhMAXevuVsNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPESUsvuv0hGV-JeYqEUUqOQmdsLeByZXsAEhGVPp7uedPzpibWoRSQGREpyJ1kKjDhIp2JTSsLADUdmn0K4FExHsCNt2BTQCMpC33F_-YBvh_r0S09lIDSqz7IMXdxAEGv9Yoj5vU2wcPFtoPaXtuPTHDl_cflqINjK6VeKjFlFn3yPfb473rx5xBOODDMKBUq8HN2XiX4647VGWGzWIK9ATeM_A8EryI7XWKsi-wIkrfT1IOaxFGYAYX9uonlx4uOolukZGOT6a38Js8hpjMPO8GqwCbe8sWIbwNM3ShSGZMCoQ1MlNTmc7knbtaiCaa0YOzTevhbDIf7XtM0UiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=pETBDzVOzkw8yzcRK2oXed39zjEmUTkr811ULbKhvKYHIrJr-mS-nOMuxRSkr1zo7wgDaXPdrNSY5FO_iiNEretNDEzQwHdR7ZCCgSlDPesXFmn33ojgnkzKp4BA_4r1_dom-eLygooJxrDV9_LDmUZNHvhk82Yt1fZB7n5aklqCnsIOzOthyv5SfpPuj7mvpg1OJRewBdlcL8sxti0_6EXzru0scCSv_AzDBCUeBvwyqjMA2p4rPtbbJYII-Ga_whRpQXhvB_x5LmOi3sjeppnPyFE0OtmTfU8QYQzjdu_m-GJqR5CLtUPZIzIF3UJgwr6xsEQ-RcHoCN6JaVqj0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=pETBDzVOzkw8yzcRK2oXed39zjEmUTkr811ULbKhvKYHIrJr-mS-nOMuxRSkr1zo7wgDaXPdrNSY5FO_iiNEretNDEzQwHdR7ZCCgSlDPesXFmn33ojgnkzKp4BA_4r1_dom-eLygooJxrDV9_LDmUZNHvhk82Yt1fZB7n5aklqCnsIOzOthyv5SfpPuj7mvpg1OJRewBdlcL8sxti0_6EXzru0scCSv_AzDBCUeBvwyqjMA2p4rPtbbJYII-Ga_whRpQXhvB_x5LmOi3sjeppnPyFE0OtmTfU8QYQzjdu_m-GJqR5CLtUPZIzIF3UJgwr6xsEQ-RcHoCN6JaVqj0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq1jM7b5j32Y7GaS63GttG8nnz9aVkIb1eRSUxwDIR3H0Iye-RwqKU_uf9seNbAhUS4vKx-ldkUwApStPs7W5uEsx_n79dp4Ev87MxbXnSTnoEBLC98z6qIdWWZpss3HA67WqBeMy7KV4iEKEoTOJ-3dRNKzKPRVNJ_D_ionr-YEdDmrG1u-b1psPwHOYlL808Wb7Fc6EXSPzjRCBIv_NeAMfj-h6YFCzFmrJXLeVhI5FKXeQJvk-_jqpcf5YL0TgJVX_3zT9XTpcqB4pVS2YtGZdB92v4dlNj6GJnQkYAfuFhU9M3l_DzB0vGe1wWVKrQLhGEfrjhi1zOnE_AJlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkuJXMjCOxSVRJ-yewcxP6J1vyOo8MsawA-V6datM816oZN9RC2r6SuCU4-2lX5lHvdfAR8AtBzjM7s1LDMmVPEblUvpchM3hqXGL7jNgyDccs-oeklXtB3hProB2tyPP4X87I-y2aXSRV6X4G0WpDdEDg3Wh9n1U6jPGB6PQanTC2a2Lc5iMgOjxMrEiYzAOXCzBvPTODVLwA8Tpw03ZeemEObkbZCtMIJNKzUR07y_Jo_7dL65XKprhemk9pSY6YGfSRRDIIbQ_3EhFW2t5mljG2Q3OPVP7vkn7kH83YfhkYQHXmbIFdTr1_00MMjpzM8TRtZFkJVxWeWCmyHZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPqHonA5zgh_fA9WNRzzKbR3ZjuUMgjHq6h1GZKr-ZRRYcK2eAYndzFeT3sBiDfGK4npQndMuk5NkRgkWl_e6XGOqIxuXRooZpkFbDcus2HeHK6E4ZrEb5tLwPV7TCcrYufPOghWyK97TSntfqP1uwLset_nez4FPFTYphAh3ZFDnq5as_1shTrIIJDHJ7t_8R-Hw50P1cqQgZCgOtHwgMuzDoviWK4y1z9ouKXw7rRd5-2pqYyd7ZAOcGzpxXULqFbmGNAXYVSGtlec86prZC5skDdi7ssYaq6J-d6O99CekI7d1xJG0b6VCvZKnaYLOg_X1WRkagE6ye0pWWQuSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgK6-MUj6V3usvZFU26bs3-wm0qgVtE45n9Qy4LH5ts8hZaI7Ml1CZIXRSi5aZd08l4sF6P1MmnhoV-2fph1_t1GKm923fZR7GylXkCMXRk1U3CTBtkvwAKteQqvtmTNbsrPZwXNp0ZV5jA59pDoxehck9MeSlQLw3ksPMS7d0ZM97ogjJF0ZO0NHVSqEIhAgJaAustPgrwLM5zqMWxlF_SRG29mD4UyTLJETmYHNehW5hc1vOgSAOXoFvqK0ZeOFVk68tKu5vBkicsdwe99G9D-Xiy5ttAgpaKSr-sS6Jljs8xgRVd4CXmm0Y9ehMRNYI8PvAsaCWz6ZUfD3OBG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJX9t_BIA3pkR7f1eFfBH1otXY4WO0qaYK5nOqzUfwWbG1XtyIh9Pw-aclWveLnRb01BK6uLsHqxOeV9dK9piOouMRR72ZOBIcqEclonS2sTmeY2D22WpE4uxS0_39CJ3QbfGIEwqhJdGtWsduVMNB9moS4jXuWri-6YxKlP3ALTr_zcZk30c2-fbfORnHPqvJ6M3aAW8fCnUQ8UjBz13dlqxJyIYDxyLx2NFaKmlLlHq2GP-YRJXvXJAbu28RskGHfY9Igyg8WTwSSMccZ1-IsuKGegelB4bXnZRTCHO51q0IfsvMRUBHN1IcoDchZpInNWXd6NvQelAkWIBCZN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCnyq7EpgZMQKZikFzWPJs1R6UsoklFEcGM9XUduKX2fYfDmmcoqqkfR_8uYAPWYiJhpaVTwbOJRayGKxfScB6LNSOzpX3-IpX6iEi0QyGb6--WH5L712DYuaX95aKpAk16cXVU7C0hvhMpi0xxk-In6MXID3pVXqal3Z5udHhwTG-UsXQ_1tcx0x2lscImRAdcKNqWs6DNK-n1fQzoWOgh-QoEw07oGBCwsvIfc-4wb0HkbTmb4qghYENTkuBQT9mUBPwGurX07KxiEAzq0FIM1ZXMABry30QTbCUjpQ2WUuBHxwfiB-xtmuVGgdK0xQwD-2CZfxJRS6jaIMuS-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNpJkmMIkbBUw9-zbjLzgPekdcfPsYTBJ_QP2gi4tsQFVBvnYzPZKPwfrhfd5_fC1UtI4RAN6bOsyWjHbAviNwknnJKuk8uidZfsTq8iCxBGrxXZ_BdSosiKMAM13nhqG4rXLreKx9G_WbAQdvYajtZ_MtdIBD2kQgcvL5F0NhTCdJ4jbvHw0U-TvMLC-AD6jVppBucBLOvtDH8ZPzEfHMe7_PZ0wHyc3Nl-wohHi2nynH6tXD9hjx5hSvbQ8U0ORXj83o7ukxnTopXjBWvhiLPetSCi_8qD7aim1BAV9cy6INjkJpUslua4vkF9YA9T1WURmAhqVaZh8RO1aDMzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjgLQSuOtdjA_vRAyQX1gwYlKsy99tphbRgzAKoGN9U6ohglqaugFXPT2QWHFzyv1YtffqHYK4Wycvf74R2nLea6Pak-Fo27SrFWiwXdo58J2lGQIGS63IYSM3zC3lgOVU9DTepvoWVSOhtjlOMUEmsQd4eaNmZijT6WbAYBsRnHPxp9JX7c3F9INllC1o2dco_oJgyja4IMYyB80pTcA2Cax6WcmnEmvqI6FrvfCv-mlqt_KSuKu5kJcDBL3nE2Dh7JMA8fx3zjf4dDNEwS_uMDVmY6R9mbq-XewqBAyE28ioUYXhjiA25k0egbxvwYkMzzSs1-phABingBxHpawQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5252" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=JzcQRnLMRG_Ava4fPfhQih9RjMFDiG0KeUKWDDPJLEzkSTP4gTVl-jggU4HQSz1kGeArP2yHOlzws3iqg4Q1M9BkqcmPkInhbsiGMxlso6qf1S7OB7kl02gD9wkqloGv7fBtfO5S1OAb33GO_fiwjWdjyHBTyimyo0UxWhlxLppK4oke4swvy1Q5vGbfmH2ZY3mbze9weNN8btPwCyjkLCvvS7eJO5S_sM-EKKYIs2dt2GxeaVmgJbNz0QvzZX2FG7YzWm0IXHKHhdhwbsMtNT92PjJbuJVCj7Kf2CK7pH7X3R6-gcMHtnhBZjYNVgrHkDeOXoNsYZP3Dac2uvPyoHtxoYP5i9oOCZ4-Cs_xat2dtTOb5hN3MyhJII9zrkn_4W63JdtY8R03yDv-TiyytKeKIe6-TRtvo20RyKKJQ7q0MOuJCkK84hrq45BNGRfzcjk3_2uBUkT3RUCkeenmud5Al-W1t7ct9-I5EMsGtFYwk1beZhvYLBoMzdgFQdVaUC2551tyYiJWxfGAq-TSxGE6E_OlySThxR0VdZXOEaP2h2xNL6vdUQeJg5WBXw7HGLgnAUTlZqXaKTt_JpJ8GQ6rDG12_sSAckKabY2KaL_4-Q9sXj22TU7HnYxtJ10gU5rBaIODAmFzOfSZ_AF0bdaM9UWEe1YMeKzjGFBa9uo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=JzcQRnLMRG_Ava4fPfhQih9RjMFDiG0KeUKWDDPJLEzkSTP4gTVl-jggU4HQSz1kGeArP2yHOlzws3iqg4Q1M9BkqcmPkInhbsiGMxlso6qf1S7OB7kl02gD9wkqloGv7fBtfO5S1OAb33GO_fiwjWdjyHBTyimyo0UxWhlxLppK4oke4swvy1Q5vGbfmH2ZY3mbze9weNN8btPwCyjkLCvvS7eJO5S_sM-EKKYIs2dt2GxeaVmgJbNz0QvzZX2FG7YzWm0IXHKHhdhwbsMtNT92PjJbuJVCj7Kf2CK7pH7X3R6-gcMHtnhBZjYNVgrHkDeOXoNsYZP3Dac2uvPyoHtxoYP5i9oOCZ4-Cs_xat2dtTOb5hN3MyhJII9zrkn_4W63JdtY8R03yDv-TiyytKeKIe6-TRtvo20RyKKJQ7q0MOuJCkK84hrq45BNGRfzcjk3_2uBUkT3RUCkeenmud5Al-W1t7ct9-I5EMsGtFYwk1beZhvYLBoMzdgFQdVaUC2551tyYiJWxfGAq-TSxGE6E_OlySThxR0VdZXOEaP2h2xNL6vdUQeJg5WBXw7HGLgnAUTlZqXaKTt_JpJ8GQ6rDG12_sSAckKabY2KaL_4-Q9sXj22TU7HnYxtJ10gU5rBaIODAmFzOfSZ_AF0bdaM9UWEe1YMeKzjGFBa9uo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=JGWAv58K0_gWdhVirvJcIPJsek1TTZ75LfuqJtsxlmY6JwdZRa0f1OKu4f6Mp29Otnos2rSemT16zmsIXqtEQUwyv21CF-ucRQdMIZuMNnEfWS_eE9Rm-3zFGTQbmtCtyhV1y87OsGPKtsOg5OzDf7kUIIWEHU9wfb2TSUddTsZxrEluYzcev2yevkwwdxMq84si3mEMbvwdKn2Wu4vn5t6AhmbFu8SHG3B2gQyAcwEZdBB6ClwDwc7faSPLf38qtnlMGzI9EOydx7xsef-a6HmpRBuhdDYOxdK83g9JrjlRiUfnK4awDk5CtvoWXhdNxvoyczs3Cr69aVTIqdrIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=JGWAv58K0_gWdhVirvJcIPJsek1TTZ75LfuqJtsxlmY6JwdZRa0f1OKu4f6Mp29Otnos2rSemT16zmsIXqtEQUwyv21CF-ucRQdMIZuMNnEfWS_eE9Rm-3zFGTQbmtCtyhV1y87OsGPKtsOg5OzDf7kUIIWEHU9wfb2TSUddTsZxrEluYzcev2yevkwwdxMq84si3mEMbvwdKn2Wu4vn5t6AhmbFu8SHG3B2gQyAcwEZdBB6ClwDwc7faSPLf38qtnlMGzI9EOydx7xsef-a6HmpRBuhdDYOxdK83g9JrjlRiUfnK4awDk5CtvoWXhdNxvoyczs3Cr69aVTIqdrIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2CvDotmzEnTrqc-_hPCYKaLlDO5pg2sUc6dI71R-1-L7QdqbOFY3jAdM5nhD3_CrfNTsXJGj-zz1jUfjC9Fu2PGfsob1y8DKCn70JJjh77Zo10LaI957zF-9rFmykMicAgtNIabn8HMz00IShkCOesMjOlOkI078rtmPWcZ1cUnnZrmNeT73kGU3BqMOKPGH7-LpcjVsmQSZudn8Xl4AJZ9Q2TI8I_YbKFtMJ3stjIr7WMw30kYBKc6D0TGMaKUmJOEmPer925aGWM9ZwcS2LpRo6FfikV40yZPHqCG05ZWkfFn5JsM7Rf0TxqCmkoCn7920DyzufUUOU_BDQO6Ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DufyB3j9bUipSkGWkXw7SdWXNC9IvMDZmUztWGqMGSx4vi1KO0Z72QQ1dqczzVjS2goniuqtQ2lce2Un6z3v6H7X2cbWj5DilF36lpuo4T378creIxmY14qash3GQoLcic2ykdAlFKm04krmHNuIlPguWKZuTSclSJI43uuuivlyCFOFlD6rgfDOoO-VZmQJDCUpSSA8t_zJC2az6k8dIwZSmtuB3Uc6nuRi7stUTn617omI1n3py-Qolo4j6Q1r-5ZHmpLb-RFz-AxlwFylNkdOZKwh1UBrcs1syUJbkmqOcpAOkXBS5WRXxx_Gt5DT-cLjHoeGX88OT7EILS5z6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6f5n87qE1o2RhXphr8N0qse7FcAFIVdTn6_VvFlpne_T64GcbI34yCO8eSgTNp5u-_prR9tIkn1fXLV62_mxpE4LUMGwlS1A7ywXbKv-kvTxhiVLU7Rf8-pSwGQj_REIo2tPI205nnk1A0nfxJ8BsmKnTQTAeGMgo0wdsmzvupQrzeEaHduvCLOU1caKxnG7cWVYW4DI9A6-uOU8bmrF2M7euzSipYC_xyoh_x0x8WEB0p77V-mekmGxJsC0QNQKDTFTUENyRH6p8mauIkgvfSjnI_3VcrUHuTm77XGfXF6snNLdkMb8oRv05nA1tdBrGgvs_9jlo-bPKNQTDTDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sbu1ALFEDmo8B7BiMztFSZQ6P7xjYeTt8IjmYbJ6juyMNgszSrmq65Vo_q3ad9yt6CpaYMuDlH186XPfX540_KJj-_6i4sKd68PHIFrWmwI-TH4Wtb5kq1uqZaz5zfZZzs8HNUU3rPNQh3NJYpRp_7umHoOIaNOO1WRPfW23pQAZOIIRgb80-o9gb0qoNngVPRSz_CYM_TWAWR4TBu289ZwAo3ejyKDV5MpjeKe2MNph2XRjNmCn_3JEikxzV2me041LQG2suFBMYFXv4ePnnSjnpVFHb8noIQH2rwdm496z2Qy5q1_L0v0TN_yENaqS1lolr2qVUKHiOden1UAKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY7xYAE0wFH9LmIdWhPtL-SgUbMNFjSRC6521Hp6JgS5lY_sonm99DPwqqWjnw__KQFf9T5E2q-3XSWkHE0IOtTqXKptkOZq9nstgrL--UU3YTpVFflUsq6hrfaqn-VT_vYNiCGZDVwQme--1fFpS12mbQ723Mh0fuBlNzpfUdLi2_0vKDGFrDPLMBd4BC0hjb8cIfk8MGzqGYZbPF4YCltqncgrPDxIrwDsoSIsWsI5W0JoKkfq1j_FNGzeRbcmYF9Mz4WafFxXvtl4P3__Ed9EAI-qt49v3RCTwuZVRof2eo-K0Ab1UZU1EhvZBH1GQHz1zKgBRszSa9g2gkXtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNg1w5yGsl6TcOIgZvTTAImx9qYHNQsi8Fz_Gy384YvXChzYI8pMY5PvSR8jOMGDpVDer_JJWJVP1USFXidd0qyXUhNvVRoXr87ghdLnVloxxh6BQ6A_-cpLfmYaVRAdBl_g9fZ71ztgB-Z4fr4PoWjKQBk1wsdqbIlUENueOue8o0YlbOf3Ib9s4IRhsM5bAhzSLZXlKjaMkqascCpqpm44qiGpNj6-RMKdob_OtrBMZr4VDQcTi9If0IDBFZzuRFt1MOMm3CJLczeVF1UHW7xkpk3ZG0WLpui55IEMn7UZGydfprsJDcEuolB_zNyXwdrhf_sPKSnl0KZqt87KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez0zIcnHUIiTZ2WY1z10FbSaKJxPTkTz2n5fJ9MSIuXio6x8jcKoL_iGQeQAf5fF2oxZ1XUlsinCGQCeFuukZ-DhHJCTHMsIdWggpUsEs6oHE_0yt6M6EVEqMNTw_N7B6coy_PIHr2UZaIFvQ4THN3pBiaV3gQN6G4bGR6_2UdKt6bzjbVH_ypcnnW_cgGc0TZni4ZkSwaP-Hob_Zer0nI4m8ysSxGv8eRiNGNbSrPstSXYDcxtmXQKI8KnX2uWvkHypdz43osHl6Z_FiFyT6F4odFhE1jtqah_XNyvVEgI4-m_Eyv-mtdJU3FEOCmZW5Yckf3wM6hfWxiVpIndgPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ps1TRcjDMFg1lXc15HOWoFbIJs1Hr0PDb7t-koHibRWOYN37sxCMjncZ7YlvplIoIt6ShqWz9Y_5XFltRaATtKxYAcIg8gdZIQ0N2G70IX8deqBzQyoQCMWlIaPzX0kVROM5HOvcQzaIWIVopV-uFLmvRbRiSrNfMoQ0Xb3d0eDyVqJ3DyBnv3Nf3zgV_5qnrR-L2I_JwFYVBRugxu6RDIrKyIvN9AASWcPsGI17lscQz1rD2NLHYK_vaBR9qWAx-bquIetHzJVfSHlN6AVeqWQzBC7IEnaDEqljOFIf3mhrL1I9OL6MOfxHMxg8Sz7HkJ5iGM6SVlEJgUWe5o3G9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSKM1QOJq6ceyj0FU9bznlcWJeMlikm26Ew1ioV7DwtlO02lNAR3YJBofriNp8EgTXE-dTyU8_zph-IGNfEbliePww1On42TNXZRxLK-vPf6Tl-KvNkJFjm7XNNoITp_sITQRHXFZZjhDIDSo2K_0AuZJXBORfpYI9MEm50HPetMZBm7Jx0F-KQP1LuVTw9Wm5FgkhSDP1npt8s0knlJSbyqXqTfQzsyBD3QQlBi00tN8812g3001ffsMbLMPZuTOyy0xgGg5aPFIFiGjGFtna75d-VvKtd04e94FBxXByOlPf060Pqo5GjlnGbDFzAWDCfh4MDLHZWeWckVPRMJ3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=pXtn1dTJq6CoN0MwGiZBzjLhsQOdUSlNz0Nb29dGo9JeL1YoJ_pYI9jEvhhpuPJoZRS9q6P7r41oH5sJWWlFnJubw7lOCwbSjh9by6QREL1w6Ih15XWeE9bHkkyz8kbXUg3LXAQIm8nieqBXepD3yJmFB0WepK4SwB4h6pYQk4mvRDfQlhZkswiTccg2z7HWMfWwxY_itKPClFT4Ywti7HTn4kh4wgARnRoqzMQYTo56wencr7BJqHAUKEXyEIGiLJE7OYf2zfCXl7zgBtbP2L2lc9yGCztiItbVkIx0jcgPqm06BzbYjJybz3_bn1_3exq6DQaw-LUKTJMAdrUvXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=pXtn1dTJq6CoN0MwGiZBzjLhsQOdUSlNz0Nb29dGo9JeL1YoJ_pYI9jEvhhpuPJoZRS9q6P7r41oH5sJWWlFnJubw7lOCwbSjh9by6QREL1w6Ih15XWeE9bHkkyz8kbXUg3LXAQIm8nieqBXepD3yJmFB0WepK4SwB4h6pYQk4mvRDfQlhZkswiTccg2z7HWMfWwxY_itKPClFT4Ywti7HTn4kh4wgARnRoqzMQYTo56wencr7BJqHAUKEXyEIGiLJE7OYf2zfCXl7zgBtbP2L2lc9yGCztiItbVkIx0jcgPqm06BzbYjJybz3_bn1_3exq6DQaw-LUKTJMAdrUvXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr6fkpxnH-9cqnDww0mE3ZwoM5XvltRm1SHM0q4d_C6_MPzuCzbeenmLYO1om9Ov7QpDRXFpW_15oWvel4YiF7xOE7C01ZDwSOeVSBUgTU0G9AHQLNzho5mw0yNHhQ6iD_nkdhRgLEncNtvNBqG_zmRd8e7bUozx9Vo8gPe1E8D1Pkj3ZKiTuIEybwYSoqKJ0-wVy8nwCi1GGsYpzLo45FjDsInYNYQ9jijioMcN_IE5QEFihcWOERygFkN0sOk_Sa9BlDJPv0OFAwPKrkgWxMm8nXsKoe4OezuZZUppwseRyYJZ4I9SD6rb6JTHirCTJymsOBFttoAdP2e5FBAdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=DYUgoQUFD4rMpA0vLSiSbZajjJXsiqyYJg47rRVBlcs74-LrR78RLJKciXESdR-Kj9W739X1weidvof0kfuBS2A4UTuVxrj1oobxdci5-tsz9IppcnLi8Xnx8vW2EcypZprlitPtX_bvriyrK8wcMA-328QttJmL5gWYQ-rGpwonb_zdxX3DSXH3MjN_Yvll44_3-yhsaDdV_3Kt8eX2Qsp3awMAPwz0FlauTCYHKUwclHK9hnidUuIksUrichvAvTEl-CJz-3fWNI1DowHeJERDmeLVk2wzbx_uY2hH-1Y2eIf2aXSsTdl5zTCiRDe-fwDQetQyQ8bgf8KPtSU87Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=DYUgoQUFD4rMpA0vLSiSbZajjJXsiqyYJg47rRVBlcs74-LrR78RLJKciXESdR-Kj9W739X1weidvof0kfuBS2A4UTuVxrj1oobxdci5-tsz9IppcnLi8Xnx8vW2EcypZprlitPtX_bvriyrK8wcMA-328QttJmL5gWYQ-rGpwonb_zdxX3DSXH3MjN_Yvll44_3-yhsaDdV_3Kt8eX2Qsp3awMAPwz0FlauTCYHKUwclHK9hnidUuIksUrichvAvTEl-CJz-3fWNI1DowHeJERDmeLVk2wzbx_uY2hH-1Y2eIf2aXSsTdl5zTCiRDe-fwDQetQyQ8bgf8KPtSU87Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=YT4wICIDZ3oTIXtWLQ039qzdj4-kX69NUoKhHeoVlavssKlDlnkHBkajCb9iqwVVzLphPR0qqYmDj800i0bYQKRAxMBwPQgy0pKvuRlvwyQeMPl_PNMzmZF9zXTF33EPu54CEz-4_FpjEL_rn1judfZ3Zs4uPo4irdP_lV4SUHmegl56g2AtGE2-y8CDhvjHngXf1NQOo8UJ2rt3z9toNwLD_wZJQIokpdMMpnn6TwQ9yP27l7Y7vJFEvYTMyhHtWEkczrWMnT4skQG_wvK9FNXeBoqJT2ZWaq88uQp6bmZtZ7h__czbgqYuMlAt-QTdDjihYPkeeqe_zfeOecWugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=YT4wICIDZ3oTIXtWLQ039qzdj4-kX69NUoKhHeoVlavssKlDlnkHBkajCb9iqwVVzLphPR0qqYmDj800i0bYQKRAxMBwPQgy0pKvuRlvwyQeMPl_PNMzmZF9zXTF33EPu54CEz-4_FpjEL_rn1judfZ3Zs4uPo4irdP_lV4SUHmegl56g2AtGE2-y8CDhvjHngXf1NQOo8UJ2rt3z9toNwLD_wZJQIokpdMMpnn6TwQ9yP27l7Y7vJFEvYTMyhHtWEkczrWMnT4skQG_wvK9FNXeBoqJT2ZWaq88uQp6bmZtZ7h__czbgqYuMlAt-QTdDjihYPkeeqe_zfeOecWugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فراکسیون پارلمانی گروه تروریستی حزب‌الله لبنان، چند‌ وقت پیش رسما  از دولت لبنان خواسته بودن  که برای آتش‌بس، مذاکره نکنه و…..! به دولت لبنان گفتن که بگذارید جمهوری اسلامی با اهرم‌هایی که داره از طریق مذاکره با آمریکا برای ما آتش بس بیاره (که بعد بگن دیدید،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5228" target="_blank">📅 11:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvzhj9wy6xo38fwZ-lyuyVMiqJV-CiM3hwlCBoMGJiU_gJzn43yZjyJgwgX3uMItiHTvtdSykKSPoL45yUKqDfUSaoRIxfJEqpNMerpWgCStL3rZ4igbsrwD26qcDuxjPiQginQU-VNoT7gzQtydpDGbI0q6G5GohCSKOXkx-Fw-bxhomgtm_vEzqM78pU8cTWWElpmnOjjoXq1jAMkPmRbvcXqPClsQtX1xZzt1idQrMWXydUkoqIF30CjJpr2kjk3YMBlYmmXhAVV1y7wTw4TFmfNhecOwFW5CQpZrzzhU6zd0MzDzyO3MTtKI9UybChbiz5jtnmDinkf-vpo9tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وقتی ایران ساسانی به دست عربهای مسلمان سقوط کرد، حکومتی‌های عربی دست به مهاجرت و اسکان جمعیت بزرگی از عربها در مناطق ایران زدند.  به طوری که مناطق بزرگی از ایران برای همیشه عرب زبان شدند.، مثلا تیسفون و بغداد که قلب تپنده حکومت ساسانی بود!  یا شهر‌ نجف!  برخی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5226" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
