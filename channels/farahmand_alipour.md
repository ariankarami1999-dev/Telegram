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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 22:15:48</div>
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
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=YQ7DlElj5VMjoolIJ_caKwpCXELztGX-_we-26fZ59MPKs3trAWFzzDJHBZk2WUEqGUeVCWPxZvQJlZ7GZmi4zU7vsx5SAKJCh592bOmngoxEEIwQUmv9_tlVXPJqo-4ngnRLB6cD2Ni7BPSnbx3iV_uO3BjdfzLNg4guLI6j2Ra4Cn8mc1q1KJArqjKbjHwYCu7aKKlOtVagurqQdv-zNQj5aBodpUisA3hri1UP6fxXaI1eecFo_I1soMbkCZusulxHZW6eckTTgNC90lOQa6ovzpr81c2PjKy0MBW3yW2fAFak9WvsRLhkk1Qwchpy9BzNlzDozdoKrcgk7EGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=YQ7DlElj5VMjoolIJ_caKwpCXELztGX-_we-26fZ59MPKs3trAWFzzDJHBZk2WUEqGUeVCWPxZvQJlZ7GZmi4zU7vsx5SAKJCh592bOmngoxEEIwQUmv9_tlVXPJqo-4ngnRLB6cD2Ni7BPSnbx3iV_uO3BjdfzLNg4guLI6j2Ra4Cn8mc1q1KJArqjKbjHwYCu7aKKlOtVagurqQdv-zNQj5aBodpUisA3hri1UP6fxXaI1eecFo_I1soMbkCZusulxHZW6eckTTgNC90lOQa6ovzpr81c2PjKy0MBW3yW2fAFak9WvsRLhkk1Qwchpy9BzNlzDozdoKrcgk7EGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u25nrom1IJz0Bz5uuAkuPeoPx5hGmOMR1uB5-66yoIJa4RCSqLTboPh0Z5-B1ai-u1cQiZQmAdGeUycTOmmn-9X6cw_iK1WRRYcS0kB9IQv-u1eWQqO0X0GtpcCGdsQzN37ZPDXv-U58vobAj4_S7Al-C7btCf-DA5lf9Sxo-Xf-CMjX2XAM7sKjuUxr4tWh2yBokykLoLGOlgkCr2AiFg7o7sXE2fx9H3JIASXQhpUESwt_H9xzq3AUZUkZu2bNxuEyj9M12sVu-FxZ24trnuslXt9n15MXDIYELIwUBG6aXgutFS_BxBg7CriQIQv7tuOnLpGGysJ7K3fw8ZOiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyi9Qt-vohnhx-h__yymhlHIX4y5GfCWs95dLHks6GLdHJdZEcr2cqSOAJYxbg8XAWiWMYvL1jp2AfLV2ot0a1PC6tLJLWWtHShvKxEYT3WZrHr5sRUq20oAhP3d9HlG5vTWtezEnucHMUO4rgXDdNUoIUlwwmwhQyUMM8BPHUDDby33px7pp82Yn-RFaL_hAZpud_-QbiVHStYljZJ7_Iuige2viGYQ8LCfH6kQ4pLm49tk5eSnpe3k0mGXOmM3yWrKJ0e-35IvTbSbIEcu7hF8uTk7Fod3v0BAW30UX2pSK8pDYqCBsX5eMfykU4z_ry2WCT5vobXFianaSi9jfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBq-RVYissa76tdSX0331IvG-u6D4idCYnIJpUmW777tZVL8n-b8O2KKMqUwh_LwwyDlwVHnPJ8z-KQz94lourEXDoaTCe1PYgjQcfmu4bky_kAIO17kfgD5qN0WdpOfwQGagtbgQNbv784nllsVOSkFmciK-aTpv-twbsUCoGqEfrgzLPn4u2ap4IecnpQN9emA_Tc42KPm84O9sC8N5zCiaaWNWSo4s99w3akJ-t2A_axjQOxhBYPnCEA23FSy1Okl8hRoYKmHbVaAJzDYEZnDKJmq2lawTBMU_cTu1u_3n-KsbZeICXqqXT-8MP72h7kyE--4qcMRHfYQ0Z9gUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=gMkMnVmlV2bw7u_EczTWHlH-ZqFM_REgc09WEiLBWs8I5vTnmlEvpH2sUe1Fdw_zPUgnJXQIvXbZAWRXiQm-ipxTpbSQzzgMglKigVGvjT4VYWN9j8ht0gmcnFDTMWV7uSMEgnLt38gJUmhkbrigSriJliws_X8IjkVI9pHY6WssL4hiFySC9fPbFCcNGZ3h8dV_YlPpUOKCaEmYgDBVrbyU947uD83vssRQokKe9rXkMTkBJOCKpr1cGMKY-lgkkzUmvWAV6c2OAhZh_zrE4bHxeCsvaBo2R0FJD53hY6lMDTjtpBTLT0OTctIHsosADepNBG_-vbr06mS5quyKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=gMkMnVmlV2bw7u_EczTWHlH-ZqFM_REgc09WEiLBWs8I5vTnmlEvpH2sUe1Fdw_zPUgnJXQIvXbZAWRXiQm-ipxTpbSQzzgMglKigVGvjT4VYWN9j8ht0gmcnFDTMWV7uSMEgnLt38gJUmhkbrigSriJliws_X8IjkVI9pHY6WssL4hiFySC9fPbFCcNGZ3h8dV_YlPpUOKCaEmYgDBVrbyU947uD83vssRQokKe9rXkMTkBJOCKpr1cGMKY-lgkkzUmvWAV6c2OAhZh_zrE4bHxeCsvaBo2R0FJD53hY6lMDTjtpBTLT0OTctIHsosADepNBG_-vbr06mS5quyKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=Q-IsH1XVIDAv0hxsNbPu-7CO_m887DA74GN0TJ-Fvhtsq8mn9KmM5xLhu3_w3C0wGg7Qrju7epXB9yCeAxQINCzVQHFrGsV6sOD9n9xgkszaqM-hSmIDl5O7l-I9W8GuQ1MqPFbHRz1evOzwacp4gJGrVvFFWEjZuyg8JCJnevVQ55adMGGQotqqWZ0BxLgFIxoxsavpbn0SNqFmGWazONvvxdOgPqBp7uSeLzeCC1zrqSWNxdQRpeXj0VGSMObg5KBjh0nmId_XxfWcjleobFAbx1xz870yUyddjwj-a6wqdADMzm2BRUN1CVfMhYyEhxsIxgpsflFrwG45AfRDpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=Q-IsH1XVIDAv0hxsNbPu-7CO_m887DA74GN0TJ-Fvhtsq8mn9KmM5xLhu3_w3C0wGg7Qrju7epXB9yCeAxQINCzVQHFrGsV6sOD9n9xgkszaqM-hSmIDl5O7l-I9W8GuQ1MqPFbHRz1evOzwacp4gJGrVvFFWEjZuyg8JCJnevVQ55adMGGQotqqWZ0BxLgFIxoxsavpbn0SNqFmGWazONvvxdOgPqBp7uSeLzeCC1zrqSWNxdQRpeXj0VGSMObg5KBjh0nmId_XxfWcjleobFAbx1xz870yUyddjwj-a6wqdADMzm2BRUN1CVfMhYyEhxsIxgpsflFrwG45AfRDpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=va7_5_QdsU0-tKD7b71E1KtuETT0AV1mzBe7SjctbQgsdhVw7KYAanmO4yafBB1A3aBvaSK1ARUuVZIvDRxtEkQyngos3m-G5L7NRpzpLDqioJKepcGbiU6hEVPmuhav0OJw2CnVsG-oodKt9GDSfbmZHOXALN8rZVmv0tx55PbqRRXhi3JHLHj6CT_1AWhyIlpiSsp3Kp9PHpT9ThgDgkDh66_A05TfsCOcdQEa2pV0dNO124anYtzwCklKnu6XIAQqnt8wT0PkCSGNJttHNTbhVU43se19JnI_W6H5qgsycSg-Hmf0sCC-5g28NNMrdjFEwgW_HPyDgQWLMzOWMLqxNd6pmBhJWZPTkmS5pDxSxGn6OQpIjJdxhhEtPtY_PViyLsr5xR-8NzBRSHLTvxALAlO2mEm3Kw27Aw8Vk-oeC0ARdd02-WEjEfxK1mgfFh2fJkO8yy5duW84YCtq7W6JxfKfmKsFoRw7YAzRLTKwrsgdHe2gBuZltdAG3JIGXEAjlZ81xz_r7scnbwsyGYLvtMPsMC5czfohcWkcjkSNLZ4LqYWi3grP-GHsrD9UXqy9oJR9QBMrssNNqqCjd38gJNuor3PF7XWJPUeqYtQYINsIooYU8pmMxGT0G8O1T9w0R1ssEbYNWtQMQbDMHcLvgH9QmIiP9IJkRPlkZR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=va7_5_QdsU0-tKD7b71E1KtuETT0AV1mzBe7SjctbQgsdhVw7KYAanmO4yafBB1A3aBvaSK1ARUuVZIvDRxtEkQyngos3m-G5L7NRpzpLDqioJKepcGbiU6hEVPmuhav0OJw2CnVsG-oodKt9GDSfbmZHOXALN8rZVmv0tx55PbqRRXhi3JHLHj6CT_1AWhyIlpiSsp3Kp9PHpT9ThgDgkDh66_A05TfsCOcdQEa2pV0dNO124anYtzwCklKnu6XIAQqnt8wT0PkCSGNJttHNTbhVU43se19JnI_W6H5qgsycSg-Hmf0sCC-5g28NNMrdjFEwgW_HPyDgQWLMzOWMLqxNd6pmBhJWZPTkmS5pDxSxGn6OQpIjJdxhhEtPtY_PViyLsr5xR-8NzBRSHLTvxALAlO2mEm3Kw27Aw8Vk-oeC0ARdd02-WEjEfxK1mgfFh2fJkO8yy5duW84YCtq7W6JxfKfmKsFoRw7YAzRLTKwrsgdHe2gBuZltdAG3JIGXEAjlZ81xz_r7scnbwsyGYLvtMPsMC5czfohcWkcjkSNLZ4LqYWi3grP-GHsrD9UXqy9oJR9QBMrssNNqqCjd38gJNuor3PF7XWJPUeqYtQYINsIooYU8pmMxGT0G8O1T9w0R1ssEbYNWtQMQbDMHcLvgH9QmIiP9IJkRPlkZR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qflTQagKLyOrOb4Q1j5-Ovb3_t5IVNqCN8GaM1BIuGCXCiZfTu5DvvGUzCSYFYKty4wnJfInrZ_-QtbJ9PKDkgXBGZ7X_73YCzyQU3JBm1alRGUno6kdNKwYIqx778n4t5y5xqvtyiKz6k3Iwfh9vlmPUIA8N2u9qCp5ULDzleHu4DozxyGQ4qb-SigxaXvbIGHaTNnUOMev21uyypi39QBA3t14e1yItX2xFgxoVq-1oAqUlXWtP57bWMp4a9fXVxDUokSpS_TZxfWs1zxPj4fKD_-GI3_eCXyHouxHrFYRqDQKqiCaoC802reSMj2nN1ZZirPzqLhtFlp0Zb0_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TNbZDAVRD7K-QVYiO1kO1O3VmriOTiWzk4fgkov_9FnwWoGtnB5XStYG5-1m4nBxMFZoyv0L8WlLJ7_8LYqGTkZinTure74hcY5FQs2UqG228RE-5GBbC5R4tp-Pf63oRXmT27zVvhEOafbT2ve3jwf75vBgM3Q4o9WD88eV0xxQ4pv02WglL0olUd8aCQNQbtzHCV6P-Dpq1bIj48Juv0W3JI3I7esXVgfT7c1wJ4-hDVXakhfvGs39ch1D2aqKz0J8lL-vqhn57XXl-l5V2cbidEJO-AT39zqFi7QzF_PQGmlNVebSaw76SlMSm7A0Q6LEh1MrLfZ5qcfCNNl-9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=YK7oNkjBBHmEWS9Z-t0pN5qLAjl_YhU03RQ0USe6YrZAhYUn5Ut196_IKfeKYGBg7LddrUGPjhXdlNsJOXSKaCIU8vgv9OIvBc3g9vX9_IbzT-BqbqhZOQ0nUTIKrNM6tjdlGgjoOtaRPh6851gxY3fufhtbhrS9t7fn6ssLGvL3L-bE4Hrwy63ELR6IOS3JU3EVFntk7J8fT183hwFBpbz0TtJv0CemP26LQpNbsqewqlMzNXhrJWjaX04J3iylJ1gbYaH0q94j46opcaa8VMwr6yv1wSb3LGqb4545SOBjpLr7bXGWN13uyQgjKgcAtyiPnMnwCfD4qfb1jzlL-TNbZDAVRD7K-QVYiO1kO1O3VmriOTiWzk4fgkov_9FnwWoGtnB5XStYG5-1m4nBxMFZoyv0L8WlLJ7_8LYqGTkZinTure74hcY5FQs2UqG228RE-5GBbC5R4tp-Pf63oRXmT27zVvhEOafbT2ve3jwf75vBgM3Q4o9WD88eV0xxQ4pv02WglL0olUd8aCQNQbtzHCV6P-Dpq1bIj48Juv0W3JI3I7esXVgfT7c1wJ4-hDVXakhfvGs39ch1D2aqKz0J8lL-vqhn57XXl-l5V2cbidEJO-AT39zqFi7QzF_PQGmlNVebSaw76SlMSm7A0Q6LEh1MrLfZ5qcfCNNl-9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5TCr0DliTihBEFUiEgKO5BLikfcLMZ9uxYsSaQdp2robMlO797bCGDx_s2u_JktDRATqCkIwPQZOnQvZr5vWE0JwEWDYn4xRfU72PyNyJIcM0-BftqL8G3ZZinovoB56QMP7rXz-mcMc0PSThrU2GWZ6a0ppAWP-kuEcMkEtgxBnkzlFB5UFMnQI2BAZnQsNDNJdQuz4IphZo5u-AbjAilbXhdnmwH-3pT_skpugJouYp1vK4Uw6fLXOMSOMVIrkyabKbNDUZvPLjWfwqu7XWF40YKROUiLy3bzw0o4ne0zOtgJ3zFl9X-DWa5aD-zpK3vKkObr1gsw6jytkPuKhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4XofurQQea4us2sEgZG2dIDvAzO3whkjpiQ3cCZHCxh2GSjF_7ADFJcDIWrj2b207vKJ3hgNIoOg1zNEW7aw6qoBb_wYkHVgdtuFExbDB7dZ0Nb0RqGIASCE-_nHzjMIWv9QoRUkioBTrrLDE8qBaSGlrk2mhmN35Umnx_1SP2IFF9Fj25BIge95xbr26TM41lbT4yloS_mVyo4dcvSYNfyy4FlUqY5QBM6qmiv0AviEYaTdz3KgAkI8z8S6G79u-vnXZg99LQsIP5FRYnIz1G-oCKjf0VEzTKWttISLqBrnMGnTweSPNqlwzLy6S4HqapBsN6VLOEKTJBHeu7Feg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXXp5NRca-VpgtsK2gKf8rN7uV5ECOh0BkZseS1p2dAnF--s3TGkymq-Umkoe2w8fzgewHOKTC-fShSQuKxrDHdQEFX0tsLm72gkrPM_E1e0s8C_ukvMDh9wqiohfADNyjRBC0OJgcNKhQMBEGsy9zURthx4iM2mmas1heqoKM47mKBUaoqnQHBjmk2qKAoye5NgttolpzzuKTSXfETiIcQWua5RlLksuIS-2wxsFi3DGzQ8Mv7r3btdpVSEhgApA6ZWR4bdv418wI8F4r6jM9kLl-ybBtmdGR7cnbA4OaL4S9PhbabKE96ocZo0OHW59pOvJ1Hy69dnPSZeoT9ViA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrpJdpc6fy1Ug8cCLQXAk_n3xR1g0MExj3zQNyV977egAF4Ys7opbOOzrIZVgVzYQc1gec4L7WyYN10hdluZpjJSfs6Odm2hYFD1Hu4DUCdUdEeqv_vkBOuobVOz2a7LnwggRAGRHrsSCc_fIjsnG-JfRP8A8ztDYGZo6l-rERkdFeA_8XbM2nVPeSFxiXGrMLnzFr6fjaigRinYPB53uPBRyEku-M9t3GxphA2R6I8-AaP26355K9dKNGkwKD6ELHmp-XPXKti_rscQHYW0I8vzgSHbS27f7K4u1wpbHayximws7rjASE85PtXaHwgICo4kjiQwLJawXND0DWqtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA_Jw1QO7HWETYIt3gvm2YdG7soGKbFGCxOzEQ6TDsnv7brnLHR_KWne1EP7QIWv1OeJb3vjbikUbXhqeLL30mbTP-QhVX9wVfg1_TyvpwkPwhgmVtItQtOqEMzQZynw3rKXNT05KRbr3ICFSjvAImqL3JZJE21ax1daMRB6R6cPrUM5LKLUx4vzG2BJXnV0_z04gQx6qwz-WBwyRxnesBSGc9IHZvKCOjraoXMvFSzw5key3rpp8pCygERFxS2xMLZmdW-xZKbJZIvn-in2v9a4SdJlJvsMj-HauxTp_zcWCLmyRelrtJrZYdHWk2kkaOMmGgJ7BlAOJu0tW30T2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB8d14XYzxQKc5O8BlooAfHA165rB1bCyeLG75MaIrjV-IYChkr205mPxOpkfYzW7Z5bGFo-2E12f_HXkrJnIUBL0gYBu_0DUmn6sQqay6xIvRmW_xxLiVw33YmlFSdpdUAAazzxBC0lHcbkDLTSg84YPLignrXkGIqSVEV9W7C5WGnHkvUsHJQB6hUSPOSiZJm2u4Ku-HQV7ht_DjajnPuXi8b3AlgOAqQmWieu0s0YRRwVTPaPb6uSmuPaDVGreNXAmlZmihHHeHRJdRCCKJ_TQhdoI5ZxX-oa18dKWQ-pWd-smS87brEVxQUtL-nYxcgziws_mAbRfBPvSX1mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=DgoCkrGs6-O8FTncKpNIUO4eWiT1ckYEFmTzrqlPiynNOa_XNM-T-qq9Yaw6ft-2JPRmeYOc0ftyXezf36nMbtGyta5mJvitwzp8aWnOtY_RNC-WoGMc7FSU8A_TFV2b_xU1IqFSLLxIG9zNjFNvSEupc00cEzJfAttqUjEMskzxPGtpx9GOFIMbbM46UhBD82y5hEYUb4GOt0mrRAYTQB3OfNEAEg46ESR-2tpBsbWmb7uzkGvZU7dnoHz1x2MzoW8u0irte8soTyh-3sp-cKkkXSdZOcpdkxr934yKKlD01F6Lxly5Nu9cMvLOduo0JJ04_yC3icLXiNp9omSn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=DgoCkrGs6-O8FTncKpNIUO4eWiT1ckYEFmTzrqlPiynNOa_XNM-T-qq9Yaw6ft-2JPRmeYOc0ftyXezf36nMbtGyta5mJvitwzp8aWnOtY_RNC-WoGMc7FSU8A_TFV2b_xU1IqFSLLxIG9zNjFNvSEupc00cEzJfAttqUjEMskzxPGtpx9GOFIMbbM46UhBD82y5hEYUb4GOt0mrRAYTQB3OfNEAEg46ESR-2tpBsbWmb7uzkGvZU7dnoHz1x2MzoW8u0irte8soTyh-3sp-cKkkXSdZOcpdkxr934yKKlD01F6Lxly5Nu9cMvLOduo0JJ04_yC3icLXiNp9omSn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imUluBtvmdnLAWXPhe0pZbG4kLb2cE7Q13qVXTOe8HSON7XHYiJeMFpZB2F6qUuhvEViktU37zMKdxF2jlEJyQjLQ50V2ugVxINjAUH-LuVscrY2RTZ2myvkXNsWAimhb9dEYQ5k3vhHbwei83ro3g1-U1wnZ-swG_ItIT5ru7LG7vF_tb3bGyqk5WNKMXs8WPRUFtgWZdRNUMltCiPJj1B9hfpIF0dlsswe8Od8itt_58l6c2ofjIo6_YtshPIKQ-_r-YkXrC0stZTHAoYoWgbEFUVQ2BdLrlk1gRE9TFfdz7sh6nVObC0-wC_pKncUqxALctjlftDnFGw1Mk8PFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DG4AJ_CVgYdIzs49a12GuAOfw2eF4Mi19OXb1eXWNOKaDtC2TSEd1_C7WcPMotZq2kDU0QCdLdO-7kKPM5DE3m57hpJPaDG9XbiNgqOF5s3oANdf44uABuVB-z0sfka6T5JCJi4gXcxWcRV52TiiekMu85HTry03iuMGKSBeGFEbwernutXNPvHVaIntwNXGk3_30P2mfeKJI2bRdU_97yBElU80G2Yzk_6ww3INONHJuxAleBaS4GGKB5pGZu7TMvaJFXtHz361Att7aR_VogsnrklJwvvIo3trTPUxQe_L-B87ECvRKwulfBDp__0a6GKQtQJFpNMqlgn-ru5zlg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=hPkajO9kBxLRtURpxXxRwfP0ddBhyxT8jppmDruO9dUdukUNylesKpOGB9CJ6lUgSNtKAslIlg0ffBnXss3_PxoBSVU-Bnsv-OKNJsIpiJHPYULVHcKe9o4jmwH36ykOLIhETUguO2KAp8rPI26NIDRGEUtDulhJGfe0c9g8tCsej6CAgWYnO-xRVV_AvpTshv8sn1obJL4Zad7SZ1Sqet5ljtA946DQ-9UCJCPhRPjij-JvxpjcUYF45cgv4gHypJZiOb2gpLMqFoJWjbc8wimvcsfOHgmtkYw47q-zzWTQv3Gl5Dae1E4JpeHXF6B3x4uhtc9lhjfFR2CRY26k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=hPkajO9kBxLRtURpxXxRwfP0ddBhyxT8jppmDruO9dUdukUNylesKpOGB9CJ6lUgSNtKAslIlg0ffBnXss3_PxoBSVU-Bnsv-OKNJsIpiJHPYULVHcKe9o4jmwH36ykOLIhETUguO2KAp8rPI26NIDRGEUtDulhJGfe0c9g8tCsej6CAgWYnO-xRVV_AvpTshv8sn1obJL4Zad7SZ1Sqet5ljtA946DQ-9UCJCPhRPjij-JvxpjcUYF45cgv4gHypJZiOb2gpLMqFoJWjbc8wimvcsfOHgmtkYw47q-zzWTQv3Gl5Dae1E4JpeHXF6B3x4uhtc9lhjfFR2CRY26k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=KWMlKu1aRt8o3JKfEc2GBEOWGCOo2nUrelL79J7oMadt_KdthnsoYwsjEEUhNWvAbE9E-30Kke_gkw5lFQeuRr83VoaAjbsgu-cap9aLG8JQTozyM8j50bS0E_1KEUg_uUJKmDlfgnyNJazMiAgRzgxgqq87m2bp5vpAqtSskVAZnhHxOHAuZ_PkvsVUKoTe6_vaj_YN5cG4VE2ESiYM1s-AixZupwlfR_e_M-3v4bHvQvlHL-d3TDft5dPBvmZnPGTsDdFBS3702mQMnBYjPPz9rg8IU6LKjKugbMfJ7p_koHYF1EuzdotU18dbu7MiCb4LDxDSsCrbyCaYdCYaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=KWMlKu1aRt8o3JKfEc2GBEOWGCOo2nUrelL79J7oMadt_KdthnsoYwsjEEUhNWvAbE9E-30Kke_gkw5lFQeuRr83VoaAjbsgu-cap9aLG8JQTozyM8j50bS0E_1KEUg_uUJKmDlfgnyNJazMiAgRzgxgqq87m2bp5vpAqtSskVAZnhHxOHAuZ_PkvsVUKoTe6_vaj_YN5cG4VE2ESiYM1s-AixZupwlfR_e_M-3v4bHvQvlHL-d3TDft5dPBvmZnPGTsDdFBS3702mQMnBYjPPz9rg8IU6LKjKugbMfJ7p_koHYF1EuzdotU18dbu7MiCb4LDxDSsCrbyCaYdCYaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJwkqr7ovTNZvhTSIWbompBHqK1L1eeMjjhoL2Q6Jgr8yol-LUBZgGspBJn1FanhsZxIqfXw5R-J-HzbyA9inePatqSDqliw6gC99mE7Glz1uwE10TWPP_QyMf1inJ2uwDdehni-YybentOZu6UUjL8WO6DURtYjzsArvkSuSXhTqNGL1nTW0Uy4b9EvLKz5zR8C-EOosKqaHeRMhPuJD5zh8aFJLYaM0-J9o3IW57VXtTJWNKQ7ka1Xc4MrGlMIABAFiiv4DrpZqOZsQku7uIg4bXMkkQ5iw86SeYGbsgEuio8ywpCcA1WB1r3y7_nSBD1zzpgSGwsdUDlAQdh8_XE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxJwkqr7ovTNZvhTSIWbompBHqK1L1eeMjjhoL2Q6Jgr8yol-LUBZgGspBJn1FanhsZxIqfXw5R-J-HzbyA9inePatqSDqliw6gC99mE7Glz1uwE10TWPP_QyMf1inJ2uwDdehni-YybentOZu6UUjL8WO6DURtYjzsArvkSuSXhTqNGL1nTW0Uy4b9EvLKz5zR8C-EOosKqaHeRMhPuJD5zh8aFJLYaM0-J9o3IW57VXtTJWNKQ7ka1Xc4MrGlMIABAFiiv4DrpZqOZsQku7uIg4bXMkkQ5iw86SeYGbsgEuio8ywpCcA1WB1r3y7_nSBD1zzpgSGwsdUDlAQdh8_XE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS-zWvh1R4dne7eI89AwNyQtL8A2-5fb947rSSPhRci_m4kpdqtP6Q7ztiOu3WZSBq1abtAelN_Wv1UwF_VuOrlBtIZAKzdfTwEYcdCadYJyc2-tpYtHypvcxc91_g9ZXsdwkwJwz4KwbO6u1ZAi69dY65D8hgnzDPXKqPknAuKr9bY3EzLpdgEwtq0GbKB5W-3geTBvL0LEaE79B-v7luXfosSehYhyKLHR_XSzcCkpAZHmKn61FhhL1hfUHWYMGWyXnYiIjl-Z67nyKx0Z_9zSz4cZyU2M3Cwe9hlO3JsrU5oRY9f17ACpTFjoUaZzdpwEfC5BqSr9KDH4BfoRlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM6wWNUJ9mPk35IjEjv94HWYwaOCmFIAyUzmZRkk6TV5zJeN0FLQleXYpWnaCW61dimUFxbKHyWNHiRyGsXSifGdGGo_s3GHjQVnmYbx89DmY5zmMjGy1Ds4AVZp9pf5HzK1iQc-BbkB6NsYpdbg5wIP0CrEpd0C7gNVQCmnK-5pM1cnVSUKvCYf03Gp5t5T900kDb-LleIaObUYa8pOpG2CjJUxLH5UAM9sod358teOQ6KnxmqVdt0fAKSbG15QrClw8uxeH0tgecXJmtwlFg7Xo-QXbavgDbJnJEPiVomRQP8JkEAglfHyWyGeXydjcWzS0yGU2FVcaRf8v4PObw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEipt1yI_6DSU1C3T-WMVfnyOzk3M-sLlxpIdVnGdLuqMbxvw4aAW1JUK7eGXimHTO6fAJdKH8r1BsjQ--JEB8iKI5DL93XrTmt2aqXdapVvHAiXo6cRMP0CSPQ656HAClU7CXJDEzt10Z3HnllZrHCXTz6wgl3pFiXMUu1CkPfNJBoKR0ziJyxnrJUiR7wBHYeyowWu2niAA9humcDSQLuFXjmyyqfeQ_p1Vnk0dWa4jNT0VkekU7XKgjsVQSwvdg9xbrPTXrWIivUjVNu9fOEQ_RgBkPmZbzCa_m5V5ewSx0jhc3zRcLxb4W1Tm2by4qNGPdwqezCKsW3DVNtWnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=q3_qusd3yX_GJiSut0GhGDAUxavRH7fJU7pAbKU8a0X_Mkzdzogz0FJ-jvja3--iVtV4h9DZxhQFAehlT-53NOzRRK_hx1NSvpDGVMh0bDi5-zN9MJuja1X8Ejo8k5hY-bLiKjgC5Ok5GoM5vrmAJQlzneECvB6lPUDs6zJDPJGtw2Fg1VrGRA3dW-jnDSIbx2kjlZHXwrD0CAa2tI-JZ_elNkR3cMKAq0ldYzeqalVjW7iYVW1thWdxBxLgQBX6cmfZJW9RbwrzB8w6ixgUz1L74omUhCyzBh2Pd93UQEB9rtE_WCERmQXu5rVxZrXV1VljkIK3l7Ay9JW-9q0FYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=q3_qusd3yX_GJiSut0GhGDAUxavRH7fJU7pAbKU8a0X_Mkzdzogz0FJ-jvja3--iVtV4h9DZxhQFAehlT-53NOzRRK_hx1NSvpDGVMh0bDi5-zN9MJuja1X8Ejo8k5hY-bLiKjgC5Ok5GoM5vrmAJQlzneECvB6lPUDs6zJDPJGtw2Fg1VrGRA3dW-jnDSIbx2kjlZHXwrD0CAa2tI-JZ_elNkR3cMKAq0ldYzeqalVjW7iYVW1thWdxBxLgQBX6cmfZJW9RbwrzB8w6ixgUz1L74omUhCyzBh2Pd93UQEB9rtE_WCERmQXu5rVxZrXV1VljkIK3l7Ay9JW-9q0FYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=YS7h-0Y8p8y-hTRaXPhsErHXIp_AFLB2EAWRnZtptOlz_xf-WgXIzS0cWW-c0uRNvXr3ORGiiPBixSqqgg-nnspYvC6qE_xnNOlLloh9Ew7-cTMlsG3kwU3anlk68J9cTBuvthfnxwOY0q_jRUtCs9aOxJ7OCF2MdjEMBoRMHg5XnbNAbiufKxflPfyx5VPFxL6y_5UaPbDDZ3K5OmoMraG9tqdrasMLcwv_a8NB7mIxg9buSW0QddMFr3vmic95NnQjUJrSjDp_DLGbousjSqRjSBtI6Q6qGx8aXX2vMaCnEWItrWl9HJcbZCLtfKZq82WnySdmPJ_Hn9vPDxJecQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=YS7h-0Y8p8y-hTRaXPhsErHXIp_AFLB2EAWRnZtptOlz_xf-WgXIzS0cWW-c0uRNvXr3ORGiiPBixSqqgg-nnspYvC6qE_xnNOlLloh9Ew7-cTMlsG3kwU3anlk68J9cTBuvthfnxwOY0q_jRUtCs9aOxJ7OCF2MdjEMBoRMHg5XnbNAbiufKxflPfyx5VPFxL6y_5UaPbDDZ3K5OmoMraG9tqdrasMLcwv_a8NB7mIxg9buSW0QddMFr3vmic95NnQjUJrSjDp_DLGbousjSqRjSBtI6Q6qGx8aXX2vMaCnEWItrWl9HJcbZCLtfKZq82WnySdmPJ_Hn9vPDxJecQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=f3DVZulogyqT9w9_ZfjeHLIOwixw7ijfl3RnM3G1i8cp2rS5Y1CdrMsSu6fJwPZKndl0KJhVppLY-S7n6v1A70BtpFe8iUvoRoOiVHbpenj5KzRDvAU4NtJISEeG9QQew8a3XHYqqxceDOCDwm-a2JAYoHMlWU7AlJY5aGgANgQ-cABnFgR9zNZRPrYTEHjKIoM0AVYeBb9Jsy6v3VzYVP78yUwY0AhlXcyoErG5XrHfktdyHPuvokx95CTmYVwUMAPzb27hoKNDs867KQFuC0nbl6iH8uI7Qh4Z4GdTAvTTMi7xnRJtx9wvL2SLzlmLWqt3U7cTQalTYi9PvW4iNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=f3DVZulogyqT9w9_ZfjeHLIOwixw7ijfl3RnM3G1i8cp2rS5Y1CdrMsSu6fJwPZKndl0KJhVppLY-S7n6v1A70BtpFe8iUvoRoOiVHbpenj5KzRDvAU4NtJISEeG9QQew8a3XHYqqxceDOCDwm-a2JAYoHMlWU7AlJY5aGgANgQ-cABnFgR9zNZRPrYTEHjKIoM0AVYeBb9Jsy6v3VzYVP78yUwY0AhlXcyoErG5XrHfktdyHPuvokx95CTmYVwUMAPzb27hoKNDs867KQFuC0nbl6iH8uI7Qh4Z4GdTAvTTMi7xnRJtx9wvL2SLzlmLWqt3U7cTQalTYi9PvW4iNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=XzpgXyU50uDTCMAwhMlsiVBc1Ssq5tlQRKr74CDkV6laYcPeiP0ztU4GAUXnu6qwfNIEtxty3Zm-53cTLNvkA0ElSyxNBIHaRL9Shdl1b3EEe9r36fG0t9xmFaRFiQjCXukz3AwiSrOHqv5msGNmDHFlbYnPbCihRYfbekGFVRLvxd44EXDReT9X5PkY4hOrdJx57Nzc--OvebAZNYOc3m7CO0LhYSfc5UNXxMYMNNWHhlTe1muuoHPjA6WAcwNVrXeMmhN_tGuac0LXF-PbnxPU6SHczkGdbN6P3UoVE7d7NmdhFZPWC1dAC1G1YF0awNdOK8XiW_0OjAYkYY1kNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=XzpgXyU50uDTCMAwhMlsiVBc1Ssq5tlQRKr74CDkV6laYcPeiP0ztU4GAUXnu6qwfNIEtxty3Zm-53cTLNvkA0ElSyxNBIHaRL9Shdl1b3EEe9r36fG0t9xmFaRFiQjCXukz3AwiSrOHqv5msGNmDHFlbYnPbCihRYfbekGFVRLvxd44EXDReT9X5PkY4hOrdJx57Nzc--OvebAZNYOc3m7CO0LhYSfc5UNXxMYMNNWHhlTe1muuoHPjA6WAcwNVrXeMmhN_tGuac0LXF-PbnxPU6SHczkGdbN6P3UoVE7d7NmdhFZPWC1dAC1G1YF0awNdOK8XiW_0OjAYkYY1kNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFpQq7OngzUnxRxhdi4etQHNWZTefsPQzNbr3dqdH8HFqpC6MrsdpwZV8WW88D-zHt6V-potE_2NJ7uCX9YurntXHzBic6IoVOchDf9idgqwi5FXqNAXuVG-89gZT3Rlf1aI378T03vSN9ACcjhpD9CiL1jaD4NEmVQUmUY4PM3EevCcmN3HuATkxrozRwGKO1v0Ska9f3O1O34WDlYaIFnMIdbsvAYeI8gBPMZw9lN_GvDwDjBsMneJ3RABCmJffhvKYMW1UD-HUs5IM81gjkuc6Xut5FWWMnfdJzyIHkr926UMlgpyXXjZom42tSH0MGyIrBVr8Ib21NwSPxa0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvVo9lYoKK9VOAPgvNTKYDnn5lxUMi4nM6boqUDWRXCFGMPJmgn2xzYplsRT8NXgLjZxaWMPB3uGG2dEmssm1TC4AhV6aFxPnpXW6sPnUPr0zGkM3BiB0uSYSWBrsLKV0bKkEOxqZRlGFTjmNVxwe7CYJOTN3KLbSPfIoCg9exVnPheVXtr7GU0wntgwThX3nLtO3MjVNCnXgDA2Plas55f4e6oek_GeY9nIXvmJW80ZxOBa3vmd_P8lXRxOzbs4Lg4MVcB6kir9k6Ic6gGMnhvPxUjAC1K2V7rga6fnxJSXtq6nb3mhswo8NgQxByX3aZFBc6-UfxkHfRDy6BG90w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaMqWIyywUYz_TbOOB-M0NoWnd9gAzvPtFL-FwbUWET9CQk5upcJzEpKquDsJBM_abHXSdL-CGS7sqVXFpWyCBIz_ITaqih9DVJNRx3a22pMMNInmCepsFnqj1SGDMI3cM90I77qGWcq8-AdwFXrTGBxNwBaCzoJEtW2nqMuxtFcaLcxRl2TsE5eFGrS4uq0iqNcZLLhB5cDsh7nAT47C_Scwh4JLqqxFnon-GRuinewjfKzDdqSEQTBSkY5MM406g2pw5pdUzw72xI9a46xvXpMgzy-wOFeJDD4yvD1HjWJP224SSULqJvL1DvDrQKjiqIrlWWWUXmnvHKfux8ZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTfwFoS7SK6EptRV8T_B8LLPwWk6T603tRsO9GaR3Lu_WCqha3uv4lZYMv2CYk3KAeM6vh4rJrtdMVnExaUtHZi-GmN4omu86aFT461s_brRo_BPFD2GnQDyjzhL60fKfPSb5L_WpxgH2NztvdRRcK3JfuI_i-fKkrcynRGqf_WJw5LH3lb5tN_hYVwqp8kblTzY0nRj0-OiD8rWW-inm8Q3sRsEzOgZpaVZawP2JmIYkV998tA4W6UBsVulPfOU6a_qvQY19_bPi1tWfMz5PoIlrs2dpTTcKp72Ow6wb0MkOU3zuCnstMRzb4RTBDJfU70MZbpuf7C0mzHcCTgAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wozpbw9QxsgF4SrBqy_bAo44NP5CRmcDH2yP0eZLLm-MrQFuz4rhipTIFS3ddYHKARjevD5v3fZ6NLIIL5SNcLr6v7GH-XgxpLp7malYaE59QG_JMFDJvpqYQ02zGP2Ti44fODShOk-TYMZJLVCEZDPZpabnNy68ajUhTdB_gaBntWY_6ma55EEotVQjbkCrQWUz4fnFU8f1rsn4zrp2hpfHmhPLS34YFFNMqoe3ypNnYQFpaL2d0xfUHVkVzvtYOkNB84GX1donLmAMueSbdAQCS-9jG5E9_8IfXC2tOWM_awpqMLz42iBaCtiTCvJb7g3RBpRGiZyEKnALBQkM4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2u_YCRFDScybeAA2cnBM431YX5ewSDyKZrkHEDQ7e2Fzng2ST2OJS0ww7HQkEJZjbUdihXEQaDZzY5Ib5cgBjFLOkzzxSrHxmFP233RskMLwS4Kje79G3bWKbPMKlo-m7qgUDR0yTHDp0dp0QoJrNHaOZ3zO3sNzWeMC7_F0WLHfrUULOxAt4IIo2YVNqZnLdMagPFn8nZkyVE23rPXuMrdbpMkrkK52JmrIQ4Agmm-CnKorYrhrsqi4WpvDvFr2DIXRNOdtoIQsBv4Lh8up7AQyP_bNdpMTGvQDbBuETDvKh9L8yoiPGL6v1c3PF1xR7rcbmHL4sXfZ8I5MIgJAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=tpuKLpIiJ5oi2XGG2FuTlxcU0QV4IPRMZ6ozT1Z7NFj9y69JzyIV9IJhs_yAeD4nYQU_-GBZNWamiHUbGZBgP2vy3NZSCcaeylq_era_rv3lCiT31AsNlAFb-jQ2nmLhPE8eJjnpr2fSTcIUsgGtgrQg2o0_yLNJbbW4hvub-7qkb8-4Mtz_33fpTtCGN8gnmuiBfGK3VdCbQDZJl50Vo3CcEazMhXHfYYL_Ly6-_mG3LCTTMTzLkwaahD-y8qnREfVWjKcEnDdflmQ5iqi6NPmmRsC-Jy6YemzhdW2_JzlJjohgsk8zqwm5Te8uR7e1kTwdj8xvoz_qmoqGRdiqcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=tpuKLpIiJ5oi2XGG2FuTlxcU0QV4IPRMZ6ozT1Z7NFj9y69JzyIV9IJhs_yAeD4nYQU_-GBZNWamiHUbGZBgP2vy3NZSCcaeylq_era_rv3lCiT31AsNlAFb-jQ2nmLhPE8eJjnpr2fSTcIUsgGtgrQg2o0_yLNJbbW4hvub-7qkb8-4Mtz_33fpTtCGN8gnmuiBfGK3VdCbQDZJl50Vo3CcEazMhXHfYYL_Ly6-_mG3LCTTMTzLkwaahD-y8qnREfVWjKcEnDdflmQ5iqi6NPmmRsC-Jy6YemzhdW2_JzlJjohgsk8zqwm5Te8uR7e1kTwdj8xvoz_qmoqGRdiqcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJm6urei-RkCXLKfog4b_PQSSGc8xNjpLBx_jRLrbHyUY4Oi-eipohmrpnUaFdX_IrZ2FYN3JBXh94OIRPxAEkCiHlRk21wpwpmL1xuyW9uZf52YTTvMfY_XIlIuEBn7TSZ4xyDVtwUKuwvjzuyV7M5qHGlKNXQC9_XwZksVhPRFAERPEaN9BEOA4rNHZqhAz-m682tQgHksiEy6rOODH73o9d_OIyZAdqpDkBpzZbN2JGghTT7LB33QUa2oeslO2JjEdt2Pofv-PpHxUY1IAUrRSPqA0GCiVXsSgni3kTRDPAVcdtFmUeNtstME_FTxvgvsg9ojEIgbT_odGZvj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHvvxmDw1upG2tqUnBV_3TUOw2c3At7b1tWtY7yOgHcBivIttopOHF1VY4CG5kmf5lX502zz7cqNRK4INvNGPjxHytB9sS7e0tIh0EKloJJUM31DuR0mPbDm3C-G51jac2LeUOkhykg3CAGPMdwq2T3ob-30_gfJT1d7zmLj5IO9e3pYexPd-fLBN7mTNdwc81bCZYgsjeqMwSQGR291QzNgOXmTFANZyl5KVywx5gW2WMT5PruMIpJIlga40MnzFH1ecgALsubA73sTBF26CGVnRshSNIwIVnOMR9Fnhjc6zeNisTL7RbUSfiNae-v2oFrS6eNcBAnZCaiHuK18Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWl9fQBRS5P28m6U_GGnA8YEaguAu0pv5JH7olDm9jnN589tMRlMa4S0oU_1jyjgWtTxm3x56ntXTTvOftcOIYtBmPhrKgs6adUJaFP92efgZGkUxBQ-FsnYu9sR73eyPEUcN344t20aUIQLTIf_6yBbjjoukyks0lontRj3rBxelAa36aBhRhPud-Kevdg8G2FrmBA_ZfHOuGQgs8XuVZORf3WTNoI2M5kxhg8epVxOF7OYPeQq6Yik0y5h-48ppsKmbDWovT4eh3NiNfngfGBEodfE_LPyVMDBzc0cDaXmhS2ev64qXBnIq28JN73i8xAJ2RxYtWrY0asEQycrCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkaABcIVXgjwfphrsT7gOMtthJCkXNokRN1lfg2E0ZDQ_Z88etwFcepeZaUz_mSYLhfd0Bw868RB8jmumU5gyaY-5tH_NvB3AjpDIBSXlBqHgdArzlRHuOIwOReEVQ46bNWyx3HDpTZLsfBvw9hIi0-fKIN6xPDMON_Ru3d0MZma8oOdw1RRLIn7NCVbBWWy5GEK7o6NndzZ6FnbNlseRN_0ipOMZKHrfhBVDP8jlk1oJZZWxuwq6UKxFQANAmCkIbqd_LzfHdVTmlwycuCE8YnjXxuW6jo-lbmuyiT_TD2zgK1xgf3a0QeHAWkevFFmIzGsfb0aCUkO52ITmvKvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWGv7AreicUxP-yUugGwECnb6E5AVaXP8kXlY4AqfnasvawwBIyNGAyV6fl3IoKinf11_pJ5YPCEOLGGYNM83AEtnASqARK8yTjKoz2GwlE6HbOl86DqOz-1XD9Ks1q6jhts5Hk3oMQKQNjAbbKZN--TY5QMYsXnw8t63sLVGqNkJxXCNwK12vqCb6GY9z3_lUIaJgtV26SA2R-7pBqBrErjXlb7lTzTLPIXbr-zjkzMnl_6f8ae7ZCQKdefXMZ-MYbqdMJ0mVsQnzpW2epIVcoGEZYju_6DPrNaI2UQNQ73m4ON4TaqAdfdfh-a_W4H5eLacCTtZxN5pdPGsRqO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvU93vSqr1ABLOds81fOHpym7HlUYUliB4uk8waO73qtM1u6D6dRL7VEmIcm7tMnZ_OhijVx-rjDXt8WqQVv08gj_vjfA9T5rxFEKh91NUsQzDpPFFzw1UD0oyjSgpVj7tu1E1oY5M2o3kLnJWIXGk5qJRuR3uazwzC7ZLI9N69wHR78GJWsTZf7XxWarmc5jOltpxUBcWAHgC2bhcf_pfTnn1UoswuhjvQWSV-zEnmD6Oq7KCRO-pI9usRw3YSs5Q2WhYy-s3nXR-A0OZaFptkz-1WfewPriaoPaATHLwkNF8-c7OMj4M2C6xU6VSF1PPn2tWe2tB9HgYOnDG9cjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5YbdoCvAETgw9lTjRdm1lK9NToyL58kJJKT2Pyf2g3g7sNu0uxWOxi8HvQYxvmPztVLV5SzlLUzsvMReg_vVXc8IkHR5vIDqJhaVa5P6Si7Yq9MR0XsklNhH1NVtkdXpH2kt6VR1vbn_vuURCTnr2xO7p5FwFHvqwVwDoMP22SXT4LkvylKhbGTLoXCRYbN0tnxCS85Y1rqtIidpu1ITx54D3tKrRF68NGbpMMGKiwL7qkUNzQKNgojAG_Fa_ztZfx0nC58wwxxbfCOmnWb46VJUlKq1GpBm3xkxx_v3gmxK6OtWE8LeUr0yInd7h6XXb1b1yqGFZFlMRboMUXl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsH2hDSAOs1vUEeGMSlYjNvdEnuRmm1mpVCcaie2SfJvFuCunGqKaU7W7VPGpL6xuLCkXsp7hHh3qbyGD80w9aMh-eeK1_fe9RQT4jKl8N8EobO79c0t-C5bCq3M21fopDZ9znZAdB9H8vKR9Tb1MRTVaYC88M09GxzbJTncZk2GdblfNXMyuYyCvafvAaG9Ok1QsR_v7upjcAXXhKQYM8wWvi9g3uloGEk3B-xSRbh_K1EdI_y3Cznm3i4BdDWsghD-Qa4ZjfSRZJAzWe20s4-J1lUJv-6JP1QFz1Y461zZEkgop69kF-R5ho_XQHyFk08AZ9vYavpsYbvNwfba2w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=qQ214-J0J2NzTdjDP9I5nzexlkB61ejnaqorAfMXFNUaTlinNSDWPQVHG6ycWIQ_WE7i30CcDz3N9Iv3pqRYh_8e--sJ3Y88rlN4TZml4eEt75LwLiMne165pDrvCD8nOWdi-ywdV0ZMaFLhCHHW1wE10DJz20aAyLQ9GaK6HTyENILxuIgEZWIFB-vIp_O7TE56STTQXPzoK5PFNLpZExWOcwoNgxbFs2A4Jzlc5OS6uk6BYzAGIBj-76R1m-9EU9fX-bGzFsGUQL5vESRBBqc35jN6H2MG7PKLoT5zKjJz5TTXrphWVWoNNHg_UCu4s-uEnIPgTVYR3jkr8-iyvq6F2e6Zw_bNZNOrabY9SaagrQwOHDSdTERyAJQn6psAGOnkNGg8Zze0RUne2BmfarIqdh3fGwYbruGwnBrxsyMCA0c0V19pDlDC_yEknIYr_47oBfZ_K7la4-9eHdNzVnx13tVA7vDBYMrW5VQHMBU3eHEICnLBlZHfyZKnZ0o_uFvyICg1ryjNDNvKDO6pFAr_ipfc1MouA4_ZHCOntkIz5vU8hhL-vepqqoJ5wE4o8eNdCBxMz9xbOZ_RRnY6jbvo40UVW5oA_XbksgfE07rOlK_bz0V8PkIjAPoLj07WQZ9uKW29uM8qUAjGDIiT7jpUgzvdmCmyVXbd_x5qo2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=qQ214-J0J2NzTdjDP9I5nzexlkB61ejnaqorAfMXFNUaTlinNSDWPQVHG6ycWIQ_WE7i30CcDz3N9Iv3pqRYh_8e--sJ3Y88rlN4TZml4eEt75LwLiMne165pDrvCD8nOWdi-ywdV0ZMaFLhCHHW1wE10DJz20aAyLQ9GaK6HTyENILxuIgEZWIFB-vIp_O7TE56STTQXPzoK5PFNLpZExWOcwoNgxbFs2A4Jzlc5OS6uk6BYzAGIBj-76R1m-9EU9fX-bGzFsGUQL5vESRBBqc35jN6H2MG7PKLoT5zKjJz5TTXrphWVWoNNHg_UCu4s-uEnIPgTVYR3jkr8-iyvq6F2e6Zw_bNZNOrabY9SaagrQwOHDSdTERyAJQn6psAGOnkNGg8Zze0RUne2BmfarIqdh3fGwYbruGwnBrxsyMCA0c0V19pDlDC_yEknIYr_47oBfZ_K7la4-9eHdNzVnx13tVA7vDBYMrW5VQHMBU3eHEICnLBlZHfyZKnZ0o_uFvyICg1ryjNDNvKDO6pFAr_ipfc1MouA4_ZHCOntkIz5vU8hhL-vepqqoJ5wE4o8eNdCBxMz9xbOZ_RRnY6jbvo40UVW5oA_XbksgfE07rOlK_bz0V8PkIjAPoLj07WQZ9uKW29uM8qUAjGDIiT7jpUgzvdmCmyVXbd_x5qo2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=MTIi4O9B1UOFgGbRem4ir2MGUwymar8buinUDOB_TUdRC1htH3Ri-6gG4pcSiM2A_WzooSzR4SknhC_ebQe4ru_GNsrsFgkTvbbBy3rGalG2hhjYdy9w9h05vgO6jFUGbXmegNkPMSxjOjLCC5u40sioGlGROuv6KH6CfCAoZ8sOM4ir92ZJrSNVYmk3ConpTnygyic1KxQ1FyB79mqjfW5Hv8kdf0tzp93JscT9p13ms5qp1z6zpRUZ3eVfu3Sl1c591L_fxByJj-Xnj7-o62AxdMf3Q-2ftuZMGLOvEViL_TMBY_lWFFwS77wf-UyfZEycZs0XYkr-1656Wl6_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=MTIi4O9B1UOFgGbRem4ir2MGUwymar8buinUDOB_TUdRC1htH3Ri-6gG4pcSiM2A_WzooSzR4SknhC_ebQe4ru_GNsrsFgkTvbbBy3rGalG2hhjYdy9w9h05vgO6jFUGbXmegNkPMSxjOjLCC5u40sioGlGROuv6KH6CfCAoZ8sOM4ir92ZJrSNVYmk3ConpTnygyic1KxQ1FyB79mqjfW5Hv8kdf0tzp93JscT9p13ms5qp1z6zpRUZ3eVfu3Sl1c591L_fxByJj-Xnj7-o62AxdMf3Q-2ftuZMGLOvEViL_TMBY_lWFFwS77wf-UyfZEycZs0XYkr-1656Wl6_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1d4H-9yPJGaBSZFhL8NmmO5qPJasRTPI9KmzjH1QF2ZMDBqRBRe535BQfLmhzL-HavsRf7lwChvbqF92ouVdC9GqurfRUpJOjVrVCowKvfUbKkIsgZVw6tXVo5vzPcdL89w5pcLxKJCbQg53oUMpHTwtf8nf5WSVnDVFIdwLZrh6yBRbWMXXXD8ELdEl-KmDLNwACYb5yrp74-dAeG_kzOv2B4tdIbIoxfemrFSv0YE5OGTsa_aPGdXBsOl1ix1BbyXzW2Gy3cYpq7bFunJZSkcU_tA9pVNJ3dcYa7VsRygqQEg2AA5dkzj9E-s4ZxblHascw68dIhCN0pQCOsxfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdPs4sV3Xji2QDf-WcvhCFhX7OXxGSArqyySfaZmo-VnwVDITEOma5ZxpBB3IOMWHt54vu07K2sLXTU-k0KkV1p2HUTd0e8LNkrNO8bwseLAPm2fbKgA0QbvY-BZ71YM4KHQrMwkx3UJK20wiLKwqbKUMCHaHcqN7_-IAoYBGwuF9_9DmSpPFMU4D5RN0iuNgGpgMEv9k1B6DbwaeLCJu78BRpyl5VqL9WbrdpzWjXyL9w9FazStRGgpuBNiOhfXFkIn4U2dHanlciKNBS9fTw5GWTK9oxZR-uDb8JLPWE4fPMklN4Hr-aLnFdsl0eY6pfRiV73Ds8nnXDZhQAOJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsLJBgpcvoj7P7BC9_xPvDsCQM1dM1_X7TWwD4k_6FvOjzj5evoH6k6VnX5SN84LxDyg_yJjymhT0Cvt9d0VuhwCyEj3s7JKQFcs4DNNkucJrRSa8Mz6v-f-ilPbXmiiPISHJXShi-kt8xKHiUb4urCkhPb2cl3zz0O59SKBPrYUENbmcee9tVujZpbIb8WpDOGgh5fDQqLK5A6W2vZSOaIdVKcXv_iweuD88czeyppuOy-__ssL4z0xUIDWvbdeWQvjKSWn0uxS75PhvxsMHdcSLmdpE3zYiZK20odxlCOeYnTOUg-3oV1cO7myCmP77zmOU-faUhBOGA_GPMq0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtLv6X6oI_IoaAWoqlb1dyno0O3KPr2w2SqXzERJgJJMJlzZrtLtHlTwnP2QgPujfIfnXssJ69Gv4tOXu1ajSPzX894fvt8dIvbXCKS2THuyXeIezuHqTJ0nB7EF2ay5J15gDD6pxGPlVYwIc9-ABUuBb-Vz8fTyG4xJsT2pNPlXEySK0eTDdgUoXK2W7vFMXZtGFTj0FdLGZgAFgvKT-tQL6ckPSBqiJy2OWxurCpd_O8QyPmWveDgczBKJsQUh0xIJxoP3e3s5SwFGKAriZCME9Xq3xmKx3nCHSLm_VyMAZyLHAXBr9t1ji1sFHgwzanz_3oJUhRZyQPBxIMymug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hra1Dk4CKTwjsMec34ySM0WL250TcWM3v6xSYEmCCdYx9udV_-fs4B7xTpJPe00C29dpqz9QRe9SyxKRDL5z4rJJUyOI_fLTGhjf5qSFxidc1ifRhs8HJ78ac9TdBnQiYt0uPLx2DtXxZV50wisGB03daEnRMDNUY3dSAUIdV5QLZrc9t9CH_2KMsiA_NZs4Am1l6w6SgGGc8KQYZmkR1kIGtAtJDYG95JgMvTuMCHGtCLO22cIHqZjKsVtfRjiVgYBIjXmDpcQCYfENuaV0J8vrmeVeSLUO4CVOUBvo0qA6-1HzAASFukpUpgXQTN7bMpYI7eTnaCI7t_pjn8ohTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE6wsgFk4TqQsWbzfNNMzvJEOdPg16RVUl6UaLoCoO2Pb8_Hj1DxiQqvC2T8NvkbTuwhmBDRjy_NDuNS_YeAxymfe7_n3WyzKJkzAMGjGp8KTGS8bZp9wtvK_dGYv-wyCNW7hsfjDzfx2YQq3FbH5eFKqCP6XazVZBvOq_y79bHsBKgCMDtfyIKRA1g7ymiACS0XIeirCEqQDErzBDukjz3jcySm61P5-Tda6P1zo9K2Un2lUlJCQzWzyBmh3UeuVd7V4v0sv25HXkVv9OUlrxZCHJ6qCRCZiEyfBukAgXYWi_MpvkurZVEZX-7Rge0qJYS3kTKJR8Qnt0UAu1uWzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEICGksOWEh6c7XXgBsBdXfuGvqjcQvg1ATCKznu8dlBSzZHcSMVSC6u9dNOxuSiti2stth5Ja4eg32FQiYa_XykIeaYsIbcFEWtAtOPwkk3VIeUjsj4FQB0uKybbLHoeiH9mmtzd0mw-7MIfe7pJ7p23s4SCD8dFOyU4RAWqpgbcjQYrXK4_STb1Bd4AVLMwtXYn1pQYFhwZOyC6RQoyBKOj1fXw8QvVhHa0bXxxX4v4LnsDJZLHbSKyNU3TD93fMdQY_mjmnupqYxqEXK-TG2l_FeVg54cgzPAFwIhPbbH1AlSVPUSaaMO0l5qL3tJCJFDYH6srNQasqS7ROwIqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvhKsBGJHd6zq7DvWJyq3m33_87NfLG2YfABLV4AdDbS-mGJPXP3_B1eeZNFt6ePGJKnEm8QR9XIVux4uKF5D-A-5y3-Avm2J7htFB_PjErDr10cntMChshjihP479VNdeMmKfbFkKWp2iS_Dcjfwp7kgz1uxySKVcwR54oVfUGdfJxj9kATjZOh27T0pdI2b2BuzxMfzdWGDgUjjPPGjVsDedmTVL1sfmOrKBgqt38uMT1dxi6hrUQTQzIAdUhF-ZpktFzefo4D2Rk0zvY7_vpHUp6L_ISGxN7HHbNMenxZVu8lGHok04BlG3i1e5205P5wHd50ZUYvFTBG3hyGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9mknYC3OznxCV2CK_TvsJtNyzVCpyniyqvtCYVHJD6FYoJq3fBSRMQOY63T7Uznf7XTA3roR64Q4Txpu3GMFonPf46D3Kpm8zJOW0LPQVFxON77mF6TVXlEb5OXH3OzLTeLtpfuQ_r83xx0HS0HFfQNbJ543NZ5Vhf1SXEqvNEH6WGO3RI_XKp4oEruBpG8Jvk9ugwmPYVXJPlKHmgN1DxsUpCQyCR55ga3YuH7vLArV4VBlT7_-p1rZEwGmrHcSUum_X6IdL1NFyXrp2063M3FFYD4pYs8hgUuM9vfOgQNoug4Omne7nJNCaoO3s9_Fa0jTW3OuBzKx9e_bsD1Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ZCBuxRO8R8_g3YM7qZkSV6WFzgWs8a8hgiRu0g6vS_vCLrMLDPSn1xSS96qh6vgZdKsGLI1bLhJZ3gOKkJII8nftnJHU21ey2gJzYKbrl2I1OxOP2yQO2Z7tuZNrVLBdvBRTDmYWBSGM2CORubkhmG-xIi3XiuFDFvzxMZVEsaaB0TfmELuIl2fvazuAzdeB6-acGpLqsrZbtzOYuOCMFoVQdLYxZ0TkvqIUFiFmpH6_S0lrDpuORseB9f9LtMnhiAvbFQNdAl2nMyEqhN31VggZjf7ADPGS7-uB0ybcmsjomQWXj8nr-js12fCqaQRjXwTvB9UTpjC_YgKIK9NRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=ZCBuxRO8R8_g3YM7qZkSV6WFzgWs8a8hgiRu0g6vS_vCLrMLDPSn1xSS96qh6vgZdKsGLI1bLhJZ3gOKkJII8nftnJHU21ey2gJzYKbrl2I1OxOP2yQO2Z7tuZNrVLBdvBRTDmYWBSGM2CORubkhmG-xIi3XiuFDFvzxMZVEsaaB0TfmELuIl2fvazuAzdeB6-acGpLqsrZbtzOYuOCMFoVQdLYxZ0TkvqIUFiFmpH6_S0lrDpuORseB9f9LtMnhiAvbFQNdAl2nMyEqhN31VggZjf7ADPGS7-uB0ybcmsjomQWXj8nr-js12fCqaQRjXwTvB9UTpjC_YgKIK9NRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuWhFkwe6xyT-6rEqSUWFMt6cetkr2969j4PGgF76i3gfXqTM9Ssuxddyci1ofgKrqtUWqaQYA761DiwDl7gRuGh3oGTuZKHoZ2S69xPw7WsJe9etVyxvI5OtEXNFzdiP_uv0NDHAyF8nqT50ZaapryoyWjW6f8N9vnPqmqKI-pcddkEiDD4IV8ccVPue8CnI93Y_oX1lKHq2SOwA5XY8KrWLHmpWRRx2jbhHZPxtxzztyd4d1lnMltOOtxopoGrv4fsnt0_AcWzFHDMsQVWrW-OriYQaS6HPctDz_BrjG_-fP87DVsETL34HtrSSH1rRHfvVu-LLWzU-an38_XT7g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=k2Ik86luMHEdWYXG3NYPbcz1lnNZW1V4NtNHrpqRee4nxSgmTzoc9AFlQAj-rDSXT1nF4pC94XDPWTc38UUdVJGH4Fg3pkv5DcUQG9W91ABYuf2sOJDOKvMEzdAOCWY0K4yhXNvRgXGv7D1EeC9yq845Q2hP4QZCghVNXUKGcDyza7GLEfNggMB7Ij7JwhwwqXeeNqBaTM5enYFlPqGyuzRGD7Mw3SC3ANLNPGJbooXCNBmBznAqDmPJi2qXrQREWIpBvthOStJfod9zfKtLVpWTX0p6wApF_xp9EZA1fFkN-jCHIfKjP1EtZF1DsLxD0m1WP49g4GpftDXWAw5wMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=k2Ik86luMHEdWYXG3NYPbcz1lnNZW1V4NtNHrpqRee4nxSgmTzoc9AFlQAj-rDSXT1nF4pC94XDPWTc38UUdVJGH4Fg3pkv5DcUQG9W91ABYuf2sOJDOKvMEzdAOCWY0K4yhXNvRgXGv7D1EeC9yq845Q2hP4QZCghVNXUKGcDyza7GLEfNggMB7Ij7JwhwwqXeeNqBaTM5enYFlPqGyuzRGD7Mw3SC3ANLNPGJbooXCNBmBznAqDmPJi2qXrQREWIpBvthOStJfod9zfKtLVpWTX0p6wApF_xp9EZA1fFkN-jCHIfKjP1EtZF1DsLxD0m1WP49g4GpftDXWAw5wMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=jIt2Xmx5lt03XUfKw0VNylH5J0_JoLRbcWOE8tRIJKS2ZOAkW3zs8its8rQ_i1luWkQFNJ5XPZFlYKK6BT-LGUIs4ZpTt2F2l9qSP-zRR3q34ABQoZb6GWgFm3fu5oclQ27Cf-scmKk9AdC5nLo-7ru6FX2oAOJHDIyY-tI1-x-B9CtM4nTvBtMpfb2cVDcH-MFIwK_0nMY_DNVMvaxYnjRsyoRESR-tz1o-zUzX9EDYXrJxhEcPQ0DpLwQrARSoF57zxjMkrS8TQQ6syEREYvcHVQXXFKPYlKoYdO26gPkI_k_aXq5LRVFI6ifpiuME3EMr3AJOwDHN0Tk6ZQdzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6921e12e46.mp4?token=jIt2Xmx5lt03XUfKw0VNylH5J0_JoLRbcWOE8tRIJKS2ZOAkW3zs8its8rQ_i1luWkQFNJ5XPZFlYKK6BT-LGUIs4ZpTt2F2l9qSP-zRR3q34ABQoZb6GWgFm3fu5oclQ27Cf-scmKk9AdC5nLo-7ru6FX2oAOJHDIyY-tI1-x-B9CtM4nTvBtMpfb2cVDcH-MFIwK_0nMY_DNVMvaxYnjRsyoRESR-tz1o-zUzX9EDYXrJxhEcPQ0DpLwQrARSoF57zxjMkrS8TQQ6syEREYvcHVQXXFKPYlKoYdO26gPkI_k_aXq5LRVFI6ifpiuME3EMr3AJOwDHN0Tk6ZQdzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
