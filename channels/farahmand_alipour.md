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
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 03:30:22</div>
<hr>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsZTJBX_xt5fjVfaMmgI6e-PCbwU7BMBGzhqBWIfRKUg5Pe6O4hRq0o14MLWxccvDcbxAsbX34CSiElzTCO4IaLB1SEPqVIl_EB8V_UNbhkLGlq0AVlrweb5cZ_hACt_00tZHFcUxA82Z6xRngPGVsy2W7_ZLW97xpGgeS8nAnHRpdfLDxDT3CrXKEb9kv9eg33hj_ZTDf-LTzxYslMNK8q_1xM1MYl_ZB0vPlIpejJafllRsaYwLu1kTs_G2j8yyn63ATGbgyhr_0Hgc1Yo7DvQQpmqbbQDqxKme0JbQL2vD_rrVqY-fqI8rfsdDYXDsSMPJCxXckoxQbpAvpw5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=nHxBgFsmRKxCTJ07FOt793gY3m0IO7d668-iRxILB6UMHmtgHD-_GQJZnDM-QIe8LxIcxmNldjcUp8LU0EkCO1yGOSbZj-IdUUaiB3758zyHrtVhoZTSCyC7TqXXiF44r3JCg63jOHjdUpw8IK4-94M3Y9djqpj9HyhdFt2mOv5Ies0ixiAqI3aatLbJuT-6p7AsQBFjrGG3tfRQheae0YBZDLPGNt7FSu160Y014CH_aVxh_-Mxrcec7AdU9pMqFRdE0fnHiS-xduRyeYQGeNwWc4bF1O8Is4JwtrZgNR-S_Gxm53sW81wS8gOq6gfsk3WiKip4NqoNcSAEwG3Nyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPyLKqC2Ab8FwvxcoFYjY2oFfSKAUwkj9D8tyFgarLb6TIsKRE4WMVddSDEp15xwSLMZJNViL-StMs1EO-s2RqN9jYc1L00suXz_KWtIGNsLZcfe03kSP8qQwUdHoYeiapXvPImTB2ownfO3gidRSHxDS5TnQPvpj9v1KWTNRra7deoGLGjfGTWwMSBwUybvPCO7u9AjX40-1uDBxJW1VpxdWisznZZXGvT3jTg2dfH7YQTLilMvasvSeSEj-mtTBt-RaMM1h7FrAaJnmULfj0BG7g2-nETFkGxOLcPvNvJXmaA6tXvWnKC9vH4Z1m5cqp9weB62CJAp-Ru1nLt8QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3U90zV_bA9BbOnca6Qm9r9tfpK8CuQ9E6ZfjBvFNbdzGYtF559tvYZIvgODN5UeM0lwK4RfPQg3eKz4zjasuAYQ0m6CmGqtWDjyAZATYYBhuYPMs5Am5w4EjKyu9O6uzGoyWJO6Riv0kQd7aPEyWoFgREsg9WGoeM-mWJ4mcp2h90Z_0MhDCEzHMLUsqYn9nOruQ2t2QCgWbPqIyNY1VCWjvqQqSbuY3jNM7yOHskubRkFS-ZLlbRTrFmXgyNci_bhN39pWeIJ8j2BxjbexIyckXvpCJnwfYHqx-FvE8yvgqUK-1KmRfpRkX7hW75nzla8ecncrMwBQUswV0jJ2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L64VijQjG8pYE3raY3iuxVkV6-1zq3bglPgHVQP50WAkVunbPJyyR3AQqxvSVX1LlDGfUboe_vfpVxZ7c5pBEUd7jdi5yum3Kdy-47EFH4Nl7PRvucPA2i6zqx16agoTcxVdukSRwIjTtGmrnUvu4HZMoX72HfU0UI_4QWy2pxWP6WrBN2cciZ3toBwnzdN5ywegKHQ_FRnNgXMnARo7mfw1m2JqfhkGBEyWOHFzk5nG6QJSsgyJJg7_fDvJkVGZLGukObfNeIkce5oFW3yKakqW-cD7wy43RC3cIJZpYRNT5tFP3zyE9-GS9oBzzQQBUvdpUX9SMzkeipqMJ-Dy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfOG8r9Le797iCT_r1O-6F2tl1IKrJXs0hhcDjwGlX56-Y1VSZjX9DosHSHHmxdD-7WTb2uN5qBfL5GHqSI6RY62CuJAxxTW3WOtrHiOF69Ni6RfArcbx5TD3O9uEWXwsxB2qnvw5lCEJZnqje-nZXdG4YdkYzcaJ3GxibPUFM4LKxQb_b7TZP8xzIR8zeCuL5oY3GhlH6R41k8QBJm3NTYGV2RzgNtpeDmVdzNFO5ODUZ_XdDwc5sxN4ma5TjG4M6Nr9rXx596qMmqnNNdc2RGXTN4HnxHvJQA5_Lun6ez4FZyYfadpFbg5jkH4gyaZkTDqSlLeU0-DreGOFmjkeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=B3PU1zzpczZsk363Fov5HlKKokzebos_Xz5Osf3cUUEl1kc11FBisMJbURl-P-Ax8xSxiSKrA5qSHlhMnloBtjeQcw8wgN4BNC6QnDeEA0H90xB9kIjMbB5cFx1UzZ0JcEhfG5w2020_oNlHpB39DswB8nEDPg_HZx0XTAICRylRfWNP-uySmvZclfdwaoLQEj-yQfe1RCNLl_w4vCkjS5t5KeS7myxESntJw1bLCt1GibkjEEf3FWIVW7MSGYxWC_rbNP2L9UZCVt4ZwSet5bu82ccVFOMEORWnWueb600ZqVQzX2YMZxqMT5qTLAOcoz_2OPv8cxSs7cqUz3q1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=vkGRFmtIynouFjsYt6t0Y17Y06QWnajSu4fVtgCAxsANqdYUAlHYlgV-8yopZ5kPskIdzvkBevFWdsyGkUSPkUzSK9g8cEHVRPkbLAdAXKorE0Mi6ztfxozG_e7TvXIzuJhpL4oOibypLjhvi1395MwXcl2T3WfeHzf3SGm7oTXKCWoyzCOoLrLu5PQsueT4DG-EOFGQaF559hUtEljkYhZgnv09DJpr435odlM2sPz9zSc3ZGC22Za_LEvBdbFRl3fLrJiYtjdtTtJExbeqMh2VGivtqRoxX1Zl-Qx-t9yotCaw8fUIkQceGI4Qt-8vg5uS5kJn-5CRikJ68-CNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMAkGBrR1Wrrs-8F7EOCnSK_eDHa6IPFemHwWozUNCnPROiCVN-F8kBITQ7eLiAPkAAfll-kqLgM28jHZwsQgngLvKKZG09AZ1kDljgbZomBYyJ3mfBLYbyIC4i_HjjfddbYOpjBEpdPU1BeVm6L2EBr5rYE9XJZ4vCiF6TBFm66zyRGaADSGmvQxR5xKhgS1E09Mbn1JT8CTFqYWxwfL_k_lSuj7CTpMFQ6IWzb3KF3SiYj0mzy4dE54EyFqY4eQT3K2j3eywYWAil30i22CjyyFd9EXoaYjsgi_R3OSWg5wmDdfi3GIfaIyxvcrt3K1ocMCHQEn8rmOOFUfRTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UklD1j-uZQHKDIdS0id56I2T8zqERHYg4t5ZpYVq7u4JxghEje35Zxjcsnig1XFa52tDsV7YRuLfb93sKh2b45xevyUiVcDPZgR9cyF0gp4SyooVejogPSzgLRgkdx547mQkak3aVGYIagQZMMkMMMYJ2b4ZZgI2u_-luSXrIW3oGZJwecXZXnh4Ud9rpV_DlWUL_HP6dtVIQrdhQydtdzndv2Kbq1dOaj2SkTu1AnYJJe1N9zm--xjlPx8WAAfOZftRGg8NMmv-Sqv_5RP0DkpK0GvtzBJmQcFCTj1QivaLEdWrbGt7xfMLFidKfkN7lyPFsRRnsk7e-Bssaf8cTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=FO_QRCdD7rwq54Jjvshtd3QpnWGsa5vboA61a9RP1tH293qcchvVvzbI5WASn_DICT65EH7sgt0duw_S3eLqQhxbXzFsN4TokiANsvlAdytnH-VkufgosQuDeuoQqTc2rMkrNKpNXv9IJ5FxOBisSgmgSgrQ2dWgYvR2khU6It9Dw4NI98hKKNuFy9WGQBm4e3x2raBmPGFBmsgotWIDg63_k1HKDtWYCteXJvqMUh1Qy7qKV5y4oHXjGSgmjiHDQqkb5c1cy8hsF9uwYq4q79kX6F9G9e2J0fhZrX0xPPW36riVznCsHjsdoZBNEUDOG-MKJgSOqM_hzVuV8GGy6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=FO_QRCdD7rwq54Jjvshtd3QpnWGsa5vboA61a9RP1tH293qcchvVvzbI5WASn_DICT65EH7sgt0duw_S3eLqQhxbXzFsN4TokiANsvlAdytnH-VkufgosQuDeuoQqTc2rMkrNKpNXv9IJ5FxOBisSgmgSgrQ2dWgYvR2khU6It9Dw4NI98hKKNuFy9WGQBm4e3x2raBmPGFBmsgotWIDg63_k1HKDtWYCteXJvqMUh1Qy7qKV5y4oHXjGSgmjiHDQqkb5c1cy8hsF9uwYq4q79kX6F9G9e2J0fhZrX0xPPW36riVznCsHjsdoZBNEUDOG-MKJgSOqM_hzVuV8GGy6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u25nrom1IJz0Bz5uuAkuPeoPx5hGmOMR1uB5-66yoIJa4RCSqLTboPh0Z5-B1ai-u1cQiZQmAdGeUycTOmmn-9X6cw_iK1WRRYcS0kB9IQv-u1eWQqO0X0GtpcCGdsQzN37ZPDXv-U58vobAj4_S7Al-C7btCf-DA5lf9Sxo-Xf-CMjX2XAM7sKjuUxr4tWh2yBokykLoLGOlgkCr2AiFg7o7sXE2fx9H3JIASXQhpUESwt_H9xzq3AUZUkZu2bNxuEyj9M12sVu-FxZ24trnuslXt9n15MXDIYELIwUBG6aXgutFS_BxBg7CriQIQv7tuOnLpGGysJ7K3fw8ZOiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA1zh-4MFVhrKxtq5bPjUbpAEjyOmK3YgWY2heWQ_t5HW7kilIxyKhQyyUsKOJj3k0DcNbqEnw8CXcVlgmPGTi8ntvr97BHgOfi5Q6kQ2Y1ATvrbEIG-TEu1iTExJ6-yeCSmOGUbyTTHPWvHJge2EU4CuHw8WBftyrTak4zALh3e6Y7h4nhWamXH9qAQHrubatkGvw1PVmhK2QOCk8GO8PY-7k0jorNEjSOQqclii1VRH64CoS9B-L-N1H0GYNLM88j6JKeZ8hXIrbd05LCyizysmlTucFA7VxJtiUAucyouXJmCc2huKjQ9Zq6pD5oEnoe74AFao6L4aZVhyyBSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9rocoO2BelX_hO6EzE9XiKY3j4obinly_J98vRguSkKDcyirUEbgjtbgLPDVcZyWvjxY4IDJZydvgGaqD7YFaWkjnK28YtYq1p3ic0uYCSZ7tcDCTr97n09vcrrPhEfHfP2i_q1K2zi_8_D5DKeA0zlo0imAQOJ0Pb15evIPp67eGEW1PKZ7afeMfVFt-dWsxU3cPZlRroel21OnHOhlB8O2Ab3P1UXesAVgmSiRcIpRIqeseRnkPPuVkWGIhX9nvvGRYUcw1QtdBvCVCkB-Yg10gj4Jna73esPNSvuv4RpwemzDiIHot9UtvmXhQMtQeiMrROxnks5S4hP6AmsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=byPjxfiQAGBUuyciShxrYTmQy8j2rjNnuPzR8CCwzR5QJ8Bf2XhuSBztmEvzX2dZ0ziLNEljGrA2YcFARSFiQ1-n35YYJe-hBKl2_-WPgXOePYZW9NU_QO2ommqhmQyUvFC-gyyiUvGXYJseCbtTuZTrjqApQPtaAPh4MvOaCdy38_e9CxANzICFZWKdTcZqlpZVio1E-qGExPPyiuJQBUVwc0d5KpLrmMcUznkffWoPqK7U7KiU3JrIxJXNBJ-au7H3re8Mbk5m7sOLgIVMzj9UR_LjM3Irno5xJAaGAdZR1K5itTezXjX2yTQryxmXYkhswWM1_4Nzi0MbjAw2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dba9d6faf.mp4?token=byPjxfiQAGBUuyciShxrYTmQy8j2rjNnuPzR8CCwzR5QJ8Bf2XhuSBztmEvzX2dZ0ziLNEljGrA2YcFARSFiQ1-n35YYJe-hBKl2_-WPgXOePYZW9NU_QO2ommqhmQyUvFC-gyyiUvGXYJseCbtTuZTrjqApQPtaAPh4MvOaCdy38_e9CxANzICFZWKdTcZqlpZVio1E-qGExPPyiuJQBUVwc0d5KpLrmMcUznkffWoPqK7U7KiU3JrIxJXNBJ-au7H3re8Mbk5m7sOLgIVMzj9UR_LjM3Irno5xJAaGAdZR1K5itTezXjX2yTQryxmXYkhswWM1_4Nzi0MbjAw2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون [شاخه افغانستانی‌های سپاه] : هر کس گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=GzSfeMzqUA2jcbdd5443tHWpeG_1T-MhSJ-4N30qGNsnYFe8b4bJFcFIciI3LmEFSkOtOq2QVPO1H7ppWL5aOlvXi44fuicdtWUoJkiz1jli3PDxd2n6hT-QFcf77V69G5BY-X8dbKb2IG9yxjlpHsIDxSE6ZNSZENQpKKkWE9d6GOpj1nP2oQZj2GqqqMx_BN_nDcNafaSgU8QP9uNLmGUgQC_6kUSx0wW1yj3JbPsx9WhSbQMajH0968mP2W58M79W7us9YIcM2YPVpqknFzWxOp1jiBW--0Op1PF5dR87u0FfDfW-YnFHvFsIFggR6higdIE31GotJXawvpuQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d975cfefc.mp4?token=GzSfeMzqUA2jcbdd5443tHWpeG_1T-MhSJ-4N30qGNsnYFe8b4bJFcFIciI3LmEFSkOtOq2QVPO1H7ppWL5aOlvXi44fuicdtWUoJkiz1jli3PDxd2n6hT-QFcf77V69G5BY-X8dbKb2IG9yxjlpHsIDxSE6ZNSZENQpKKkWE9d6GOpj1nP2oQZj2GqqqMx_BN_nDcNafaSgU8QP9uNLmGUgQC_6kUSx0wW1yj3JbPsx9WhSbQMajH0968mP2W58M79W7us9YIcM2YPVpqknFzWxOp1jiBW--0Op1PF5dR87u0FfDfW-YnFHvFsIFggR6higdIE31GotJXawvpuQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله رو دارن نابود میکنن و جمهوری اسلامی برای حمایت کاری نمیکنه.
«عدم ترستون رو نشون بدید»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=Zt5cwJ_kRn-innay7V7T-qnY6ThwjvRWCY3cFaCMrdRtiReQhgEfvfZkclmIbtbMjJZjWRthEuNKWDUIXuT0KoxsMX2DMTzs8cvjEfZBD9XsCJqd4l0C4a42IQ1dEaGyKzVCtsklc6rvR7bQ54v0KOE0kpiOgub48s7S1UJPH3K5k6Vp5aCVBjH48eqch-bxKu2S7THQyUg0vEEHv1GDYPYn2ktL2y6yjKI5A96gHPhfsAmQMjEBLgSWvFRBE1zTbF_9XU_kJJI-_auomfFImAum7yQIXY7XkogSs2d8pJ6AYpzrxnka1uI7vffs3Xt02OfoeyT_j8E1eSw_m3wAhiuGQAb3aGNlH-Og9ifU9kPot2zyDtXKmJfrvIXTAc8u2YFW_pU8mMQZDxeSHvJn3OpO8K7ZWML08tOcah_ny4cfLy9qfz4b8S6QCpmXc-I161C4jTfeGSP8RjBZvrduOe9wqU3yP_koKSImPNYKURWksuvwGajHDjlMMGo51UpPXHr_FNVKUyCbRQcCLvD-_qT0L3nWt_8Okw0NRG7h1k2iaac6qz_EOzYfnskrGiecbBpUVkluIocTmu4xCQPzXWUkU9Uq0xFV0zm_ZS3rjqWl9lFfn1IPjdm0kD1r6HxMoo4kQlniJeVmTTt8bl4Fnq9y2JKsv3yBOjaZfqhBOo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3f82fa44.mp4?token=Zt5cwJ_kRn-innay7V7T-qnY6ThwjvRWCY3cFaCMrdRtiReQhgEfvfZkclmIbtbMjJZjWRthEuNKWDUIXuT0KoxsMX2DMTzs8cvjEfZBD9XsCJqd4l0C4a42IQ1dEaGyKzVCtsklc6rvR7bQ54v0KOE0kpiOgub48s7S1UJPH3K5k6Vp5aCVBjH48eqch-bxKu2S7THQyUg0vEEHv1GDYPYn2ktL2y6yjKI5A96gHPhfsAmQMjEBLgSWvFRBE1zTbF_9XU_kJJI-_auomfFImAum7yQIXY7XkogSs2d8pJ6AYpzrxnka1uI7vffs3Xt02OfoeyT_j8E1eSw_m3wAhiuGQAb3aGNlH-Og9ifU9kPot2zyDtXKmJfrvIXTAc8u2YFW_pU8mMQZDxeSHvJn3OpO8K7ZWML08tOcah_ny4cfLy9qfz4b8S6QCpmXc-I161C4jTfeGSP8RjBZvrduOe9wqU3yP_koKSImPNYKURWksuvwGajHDjlMMGo51UpPXHr_FNVKUyCbRQcCLvD-_qT0L3nWt_8Okw0NRG7h1k2iaac6qz_EOzYfnskrGiecbBpUVkluIocTmu4xCQPzXWUkU9Uq0xFV0zm_ZS3rjqWl9lFfn1IPjdm0kD1r6HxMoo4kQlniJeVmTTt8bl4Fnq9y2JKsv3yBOjaZfqhBOo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏محسن رضایی امروز به CNN:
‏اگر ترامپ مذاکرات را جدی بگیرد غرامت ۲۴ میلیارد دلار برای آمریکا رقم بزرگی نیست. اگر او واقعاً بخواهد با ایران به توافق برسد، این ۲۴ میلیارد دلار آزمونی برای اعتماد است اعتمادی که ایران می‌خواهد نسبت به ترامپ داشته باشد.
‏این آزمونی است که آمریکا باید از آن عبور کند؛ در آن صورت مسیر توافق باز خواهد شد. این پول، پولِ ماست، نه پولِ آمریکا!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPyO5MTobZgFw1hx5NAEQmqftwy9Y8uxgvZPo9fqXxLvX3b0vtsPzgdRucXqSrfEfZfivGbtwG7NlMiO22B3xUHwvE2u91NoItI2V0Qsawie4BieYtQQfZepnd3qZXNJRltH-ocddQsHGxeFwdYHIbEBMF4DWvWbch8ZNB5UnvOkcWoes5Lo26TAzChxLQVt8o37f_cyEHt6eW5fKZq0PMiJnAmPzuwmwLpHrQVK05KpceTVKYUcUoWFQU_nGcPnkVyJqUMUIZjuN-m5AlMgw_N2smLqX4ODzhuSonEAx8h3kxb50-ZBBPz87EyTOdRiI5yw3kcI7DBl_w9aKwWn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای انجیلی مشهد
که سال ۱۳۸۴ به عنوان یک اثر ملی
به ثبت رسیده بود، سحرگاه امروز
توسط بولدوزرهای جمهوری اسلامی نابود شد.
مسیحیان انجیلی، اولین بیمارستان در مشهد رو هم احداث کرده بودند.
کلیسای آشوری تبریز هم چند سال پیش ابتدا مصادره و تعطیل شد.
کلیسای جماعت ربانی مرکز تهران هم
توسط وزارت اطلاعات تعطیل شد.
کلیسای کرج و املاک اون نیز مصادره شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=vnkj7BfGFNzcZjekGMVqdYazNS2kXfIaAg8Gh6Ik0JuDm3Aahb222x45Q4nxfdwxceosSJT_TdYwLtBqzVf4Smx5I9AkZbQwDRHXQzoydlZTvRYX-7gEwLeW1vhhHYPp0Ywymkn8fMDOAkU3AewdfEB-Q4s0Y0sEdGdjfAXAsw53fbx5_uSjtWTL5OsBN2N0cfqXpsdHe-eZFFfv1TFFBBolDPWxLL-QjFfHs2juSSmlpApi5YNoKdYolDwnZA7VfgV66RrWZkxgm1wDylSPbRO9qON2i-QkGGpKNmKgxBNqTPTX13ZNlGN3Rfg8C-8O7si8gW5Ms0v5f7YDgpGVp3UHIpAzSPGe9-JkHrAvjEAGxZ0FKbysMRd4RlH4h3fNmjvUoMhuwR1tBXcRnBfnNIfmmMewZLbWv8LjSGy4v75Wxt5N2f3PcC1DY0FgHoDPJ-n68scEFoq5xG3reasVSOsQoZnLpY9-FYq8KN30iktmfuAJo6t__oeFfaUQLPoVkbWMPtPeUuaMMHHhbf5nrit_73wDiWlFX4pj_sfzuzrFW0YJUv21AB82ChP0tBkJP4cdX7Oyh1jGFy2AUIHo_QcXaFHqA8SAcMMv24o7yTROI-golDf3e-y_4xu98x5WNtA5RaQ9f1_u3zElhuoeKI8M3LsvSd5Z3aNHZbvgiVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d5c99a5.mp4?token=vnkj7BfGFNzcZjekGMVqdYazNS2kXfIaAg8Gh6Ik0JuDm3Aahb222x45Q4nxfdwxceosSJT_TdYwLtBqzVf4Smx5I9AkZbQwDRHXQzoydlZTvRYX-7gEwLeW1vhhHYPp0Ywymkn8fMDOAkU3AewdfEB-Q4s0Y0sEdGdjfAXAsw53fbx5_uSjtWTL5OsBN2N0cfqXpsdHe-eZFFfv1TFFBBolDPWxLL-QjFfHs2juSSmlpApi5YNoKdYolDwnZA7VfgV66RrWZkxgm1wDylSPbRO9qON2i-QkGGpKNmKgxBNqTPTX13ZNlGN3Rfg8C-8O7si8gW5Ms0v5f7YDgpGVp3UHIpAzSPGe9-JkHrAvjEAGxZ0FKbysMRd4RlH4h3fNmjvUoMhuwR1tBXcRnBfnNIfmmMewZLbWv8LjSGy4v75Wxt5N2f3PcC1DY0FgHoDPJ-n68scEFoq5xG3reasVSOsQoZnLpY9-FYq8KN30iktmfuAJo6t__oeFfaUQLPoVkbWMPtPeUuaMMHHhbf5nrit_73wDiWlFX4pj_sfzuzrFW0YJUv21AB82ChP0tBkJP4cdX7Oyh1jGFy2AUIHo_QcXaFHqA8SAcMMv24o7yTROI-golDf3e-y_4xu98x5WNtA5RaQ9f1_u3zElhuoeKI8M3LsvSd5Z3aNHZbvgiVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور لبنان : این کشور ما است!
کشور شما (جمهوری اسلامی) نیست!
به شما ربطی نداره که دخالت می‌کنید!
این خونه‌های کشور ماست که داره ویران میشه!
[ ج‌ا ] کشور ما رو به گروگان گرفته برای
مذاکره و چانه زنی  با آمریکا!
این غیر قابل قبوله! حزب‌الله هم باید بفهمه که هیچ راهی جز گفتگو و مذاکره و دیپلماسی نیست.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رئیس جمهور لبنان خطاب به جمهوری اسلامی :
شما در تلاش نیستید که به ما کمک کنی،
مردم لبنان دارند هزینه‌ سیاست‌ و منافع جمهوری اسلامی را پرداخت می‌کنند، منافع ما مردم لبنان با منافع شما (ج‌ا) یکی نیست.
رئیس جمهور لبنان خطاب به سپاه پاسداران: این کشور شما نیست؛ این کشور ماست.
سپاه پاسداران از لبنان به‌عنوان یک برگ چانه‌زنی در مذاکرات خود با آمریکا استفاده می‌کند. این قابل قبول نیست.
مذاکرات با اسرائیلی‌ها سخت بود، تا زمانی که به یک پیشرفت بزرگ  (آتش‌بس) رسیدیم.
این توافق می‌تواند راهی رو به جلو برای رسیدن به یک «صلح عادلانه و پایدار» باشد.
یادآوری : دیروز حزب‌الله لبنان توافق آتش‌بس میان دولت لبنان و اسرائیل را  رد کرد.
جمهوری اسلامی عملا لبنان رو به گروگان گرفته.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQxDl9jv7Rx6C7FM5e1ZDn4ZQEoU5cVchIt_gmYXgXrVLl0Z6RFxLpE7DIT7jKdon6yXz-r8R_o3mhmRbibbbNTGFHd35ZqJaAD1g2h6FlJphWYOm4HJz_jt4hJ-qnEKyRIw8htIKv9n9cEXnIX5HuH4q-YZTu8EvBRmPYMBnmZrjnhEVotb1b328Kyhwc6B4uuF5MYfRv8tYio2ZN9jAj9vTlraiN7cwX26eZrb16FERRGiIEXNWS8yRhCx80Ak6Qb6SLWDOGfHseVuiqu33DG2mtbHQ6SVQvhbZnPyva9RZOhleNiWFOYZaMtJIB03jrnX2JCt6J_s8w6HAwIVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امروز، چهارم ژوئن، سالروز آزادی شهر رم
در سال ۱۹۴۴
۳۳۰ روز پس از ورود نیروهای آمریکایی
به خاک ایتالیا، رم آزاد شد.
موسولینی در یک سخنرانی رادیویی از مردم رم خواست علیه سربازان آمریکایی قیام کنند؛ اما مردم رم از آنان استقبال کردند و آن‌ها را «آزادکنندگان» خود می‌دانستند.
رم در عرض یک روز آزاد شد.
شهرهای شمالی ایتالیا، از جمله میلان، تورین و جنوا، چند ماه بعد آزاد شدند؛ اما در بسیاری از این شهرها، آزادی پیش از ورود کامل نیروهای متفقین و به‌دست پارتیزان‌ها و مردم ایتالیا رقم خورد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0o9tlIOcIEyotoTenkMUIqb9PXIw7qow8o1UZiZ1Zfy_f1lI4LkDO2E394jqsaRCnGySJnZHDN88M0EAJmA8TqSbrfYwxMGr48UVsbFxmnxLfNKdwiiJCqIWYtYb_Fwmp5OBXoQ_zXWIksJvF_Hc7SnlR0_Aqy9bqhx7PT9ccfPv3ilFMSQB-qMx__onslm-_0zvJbG_78LApfztsDWsFl8qGn47wXj0vulR6rxjEe1OyBEIXomDfGBezhzO8bORqTnlGhpgXZOIGNPWfVkVR1fVxC7iTWlAKcBqPUYaUV3IcskfKWh5Qt3G77mS8Pogg20DM7L9ARjPsdqxKexQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGgaJWAvF-e6_d8pW9zuwCgJGzRGdMjU0uQ7oyu2JMhlxlDRWEN_RBozKaDO_vSRz2--ku30TNp_a-1XfjEYV3LLqt75yX9Htz8cxiEh7omU0wI29sadC3nTthxsp0SOMzZRJIOBRYUM2LzjSVNwkrKFnqciyuED__E6I_GXuG28g8qaWmiCS-0-slqgLgryY34i1gZEHeONRCZpaZKDPEf2WbtQGedmf-TQX_rX2D96BQ-5LmvCorZyHiIB1pPRIc0W64HuLLcHArShsNR0UGHokZPMP5yN76hOGT9xsr64CLeI-Z2gJrwhUzruGbhxAwp3IJ5s8RHcUxJCsvZDuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5302" target="_blank">📅 13:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhHn1KImsyj8lwE6yUuZGS7GUaiqUmfCp3NZGEwYVP4F_IxvTPvGvpG69tz1qO3vHV0k_njxYCwM8O6o-aWxLwJcdtEu7VjKSDz0OGrpzjgaa07_wq1Msg8S9dnZ2d_4BVPBX4DOLPfYMlhxDZH-FZDbtga9p0Z48gjNhn1Ak57RHD0rAK21oIyXmqheRGuciflWuS8Hk2RsJ6BWCcnEOmxNNoRwHwaBVSrK902gJ7d_UTmXbYahaEgk48Ord0Bdt3tV0eFvqLCPsniN3Kh_8sEMrhdI2rp7QKXY1uMwkC_kbodMrbaFnNyUo9HuVU95AmmnlArMxaqB6GPoSLc2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooSsDHsiathbNFRTZ2lhxOJsvsbtTOojkxJuqLz8C4TZ2kw34Tnv9z2QE9xSqVUKgK-ebj7koIKtcxxb9P1XNC_ud_JFcwuTkPN-MnQ4zh-PFUAuuYZsNTVxpXXV70XxaH8BMqOhYxFND6p8ruVaWJPMXfcwICzf8_muQ5hXO17h2Xx06gwvTPgFlxu9RZ8oioBtaNUs5ybtzrFvggn-F-Cu_QhVDGOxTevf0flNXTTpnuVQ9yZ6MMXliZf61jp-rOdCfSIr5gvHI1oj_rmX36d9mMadRHa9WxdlREpW-pvSShXHkrSEeIJNsvILB7P2DqyfSEnUeIjttfShQA-Tdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNoVuClvSuG5FdV2XujqX3G6oTcmOWoHcbYKNyoX5K3kshhXPSppoJo0y5RgnN0W-0UjpnuuRQ9n6wGPNWHs5vjJBxsz8qELyQZ9L0SNAp3LxDlSAVfRSSlNeOTrHp5Hk0Geaz-tf-Iima-UyfVWsmOl-i3fZtXiiS7sYBF00-gvBMTu6KjZuo__Tcxzl2zn5CbLK9fuSEKkk0mzhAHm-dZy_zcAKA3PazvVnkFC7b9nfxWLwr5Jl_wkuGXjEToIqfSVwN-HXwH0ClnjdMjvdUCmCvK0TS9u9-in2K1IZMy5gjqOwGTPUDO3Tm330ck1bV0QZh1I4z5hisJXc7Kjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=g26tETNcCgfyiDFwQdbPC_4pV6WN6eJU7uaEtpHm_OzMoe8wpV4YHHwf_Er4_d9it-gYzrCXHZAseP2PnXuSyBZrH5D7Bouj4WXqMoQq1Dm9OMFWp-6DdFj24eyU9vr3ZSrSMbaUALeFepu5xXkwTHLTb7l54tyCILC8TWvWkDaKFaoAz_ZsnoDKBSU9gdhV3oG5syqVYiac0ZLyVavxhV0eF2Vx_Y8Tx2JPUm6jA2ZdtQnOWbZvFll9Oaax6NQRuljTjXi0mrRn-HIPwc5ZQmgMaZKROhcY3htdTSPne4Z0vfsTiCNx09joiIhR41qCQdaeWz3m4QVU99iKmfg8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=g26tETNcCgfyiDFwQdbPC_4pV6WN6eJU7uaEtpHm_OzMoe8wpV4YHHwf_Er4_d9it-gYzrCXHZAseP2PnXuSyBZrH5D7Bouj4WXqMoQq1Dm9OMFWp-6DdFj24eyU9vr3ZSrSMbaUALeFepu5xXkwTHLTb7l54tyCILC8TWvWkDaKFaoAz_ZsnoDKBSU9gdhV3oG5syqVYiac0ZLyVavxhV0eF2Vx_Y8Tx2JPUm6jA2ZdtQnOWbZvFll9Oaax6NQRuljTjXi0mrRn-HIPwc5ZQmgMaZKROhcY3htdTSPne4Z0vfsTiCNx09joiIhR41qCQdaeWz3m4QVU99iKmfg8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfRsVFsgLMEAd-1d--mrgHgKkTnSihxJWk0AvfL8se5Dh3KL47lIdkvVvQYw9SW_vsnVi35ZywWhzD1krwva714TODj-dGsLiS_P9y68IMV-ZurHFMnYRmSfZlVfqBAvheq1zdQ4ntRoLIageQVKGqXcmUmQH8oyHU8ioJTzh7eogu79RtFzDE4QsJXskl3a-_jT_XHOFpigrg15tLPNui-SA6qgIUHm3BUMn1t1-b9EOa-_lFkKuJbP-CElPdNdmdP2nVXraewjvGA5bDDMxBbiGipzkg76V_5SwZ-2oQmvQFQXCX1O8wTwYpqKyySTaEyjqDDs97BwtoTrWHPohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYmzNSXou5gDYoUbLdo0lSeLw3JhQIIYoTj45364fVHyGprZglkIBEo7lPb3WaPqSw_RwpzLEOPlkuXeeg0SoAcsLsfBoKF0O01GizDu_NkryfRYoD2iBtEZlgWuUsslUv5bkVzWV5JCF_Uu2dzRBb7Q79sULPkgwf5s8qPc5NmIzQLC-b7YKloSOi2sORaGBO99R4WUJCojLO7HfLMnOSLnhAg9W4JmmhZJ-TH4JnMLViZVAY7TJroEVIDnXsfgyCUfEJLs2LdWTYEyGEgNze2H6v1Oad7OVrAzK97px5-dRupDFb317b_PaLscg8ChIKNlOV79pUy3xrWfdFrXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G80F1ybX28x3fr18n0Y865x0cOoMJZqUcNpIxdgsKyhSlB-bXcc9uEqg7RHifIojwj2xAZVt6OwgQAxGY8jBn9gvSJ8ZWnW19Gsq6O1OrQdGUeUbixKfdxRnbHiRYt8A-VzXa8gYYLn_qsVteEBhsaC0CRpRgjGDdpTKxJHsFERObGHS2rNrDtSzx6Y5K4N922ncT5ARjoY6DsUD6m_zn6evqHaTsSN6N9KODMpOS4agFuKJY19llelE95juli-wh3kXx2vFRFXRg-Zeq8lAamEZBsyF8yUvsj-R_iESaUDFP6vfMZCnazer0GZCrca4D6OeXI8NNtbbnmRoERImQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=ORg8nRZWN9lZtKHe18VULiNS679AduVndYMfZ61253H-Qpomu8gBP7IhVoLmqtG-AXQLuy-c0sYoegu6aw2vUjCRxUBOjaIL1xpSl9oNijmV7SR-yRLRWG-0HHK-qUPaEtsQMFmtAgaBId8m-3zaFvKGzyFKPB5IVROUeUUGNXu9Lzu8jrDM31FT3H4VSZY7JPHG3Jvs3xS6E6lY3MxpPp_0MH4LmnxnrBF7-DmLI-0KCUgwvoAoSpvsLeDhbR2NiuUBEHeKkM-sfU7dbYBBOQiP2zFg6N3Ec1YEL0C4cTIrSMQjYXw5ZKLHk1FqBQJlKxrSGF61hxIhkj_WlmNmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=ORg8nRZWN9lZtKHe18VULiNS679AduVndYMfZ61253H-Qpomu8gBP7IhVoLmqtG-AXQLuy-c0sYoegu6aw2vUjCRxUBOjaIL1xpSl9oNijmV7SR-yRLRWG-0HHK-qUPaEtsQMFmtAgaBId8m-3zaFvKGzyFKPB5IVROUeUUGNXu9Lzu8jrDM31FT3H4VSZY7JPHG3Jvs3xS6E6lY3MxpPp_0MH4LmnxnrBF7-DmLI-0KCUgwvoAoSpvsLeDhbR2NiuUBEHeKkM-sfU7dbYBBOQiP2zFg6N3Ec1YEL0C4cTIrSMQjYXw5ZKLHk1FqBQJlKxrSGF61hxIhkj_WlmNmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=PAgZwoA5TFZQnTiz1sKRs3PpQ53_Ph-U-YeqI4xJVIniOUTW0VRVd41Pg5Qt31P28KjWz8Qpl8xwK7hCiEIvOduGsg9aQHbiz6yFDkEMFs85MYNUXPEkWYb08uhMEfaCY_vqzLZ2K3vcjyAp97ldt9q2Ql-ZeEpmun6gxFvVDXgfwZSE6-wfFuwZMH8PvTzmkykIAbaNTYTVL8qe6GKu0vZ51FnPcHsCyXoKQad0lBQgKqhV9x1J70Xl9uzho57K5jhh1KVOBJmkdwrKj3ifTs18VYsRCCogvOygkukkFSuwqKvKvHbSH_LJUfdXJ4OzvBfCJEEPbLFIfmNG250U1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=PAgZwoA5TFZQnTiz1sKRs3PpQ53_Ph-U-YeqI4xJVIniOUTW0VRVd41Pg5Qt31P28KjWz8Qpl8xwK7hCiEIvOduGsg9aQHbiz6yFDkEMFs85MYNUXPEkWYb08uhMEfaCY_vqzLZ2K3vcjyAp97ldt9q2Ql-ZeEpmun6gxFvVDXgfwZSE6-wfFuwZMH8PvTzmkykIAbaNTYTVL8qe6GKu0vZ51FnPcHsCyXoKQad0lBQgKqhV9x1J70Xl9uzho57K5jhh1KVOBJmkdwrKj3ifTs18VYsRCCogvOygkukkFSuwqKvKvHbSH_LJUfdXJ4OzvBfCJEEPbLFIfmNG250U1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxIg85SBAq8tPTHbs1QufHkuLQfNjFR4zS2aj2tWfvCb7_RnDBIgn6O2qrWYWF-0EQlqqqZhAJlX1nuTqL-5iqsXGNh8XNh1NL9WqO5oOogwWcFpnjFTYbMwNK-ib6bawn5D0oq2dZBoOTeeDJJrtGP9lW_oFTM4BHT5uczKLhTkD5yLPDdJ3WcHdMqpSRuwmlfS0qHkuD_iulDOcy7lQT6KKPVKoznNj444aXAt2ZEFuJaWDR64Vb_tWlaKrbmaz8-xa1D-1L3FSQ40LIqEQBSGF_PBT1ZiJj0TrVERhGzg6FUEAcfg2wF6cq5v3U8_shIJmbhYcCMYWngsYoTPyIkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=D0KTsGT8zvJ1IlNUsMEcAmpyOzblecWqAO24rfYd476VNLPIZWeqtbXmon_lATmhYhSvF0gZiaX_7N3ImmlBaIGGnGcuLGZY-c0DdvNGNYsjsSO0tWPAqd6WQi2VKFji68fYxUN-IbLkKrBo4VpAsJ-E8zvspg_gfqDIs7ejeeKWW27zzURSxkrwAQ9U8WqNTQ3CGY9aJcyRHjHjLJINA8JqyhX7lrQlQW_LUPxbm6ip6Vni-Cds-6c2eVd0nlGX4DPLKCjUpJZD0z8htNh_5Poe735cusPOniHjCfw13BO9Mi9acvJAR3h6H_IucJRYjbq9OZoooN66qRatvSxcxIg85SBAq8tPTHbs1QufHkuLQfNjFR4zS2aj2tWfvCb7_RnDBIgn6O2qrWYWF-0EQlqqqZhAJlX1nuTqL-5iqsXGNh8XNh1NL9WqO5oOogwWcFpnjFTYbMwNK-ib6bawn5D0oq2dZBoOTeeDJJrtGP9lW_oFTM4BHT5uczKLhTkD5yLPDdJ3WcHdMqpSRuwmlfS0qHkuD_iulDOcy7lQT6KKPVKoznNj444aXAt2ZEFuJaWDR64Vb_tWlaKrbmaz8-xa1D-1L3FSQ40LIqEQBSGF_PBT1ZiJj0TrVERhGzg6FUEAcfg2wF6cq5v3U8_shIJmbhYcCMYWngsYoTPyIkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5289" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M28X7EFAdT416a2rZqHmdsdmopvu2WPFhD7Shs-eirImslbMiGWtjbmYFaskkB32B17eOd3DnoAEc1bdaRDx5KZ0JlkKcuua8UmxopsgBMnb0G1Xl7m9n0mg0UN-oeUm4Q7Psc1ZuqxTEuKCmSURt6EohzmEWGFx_uGZKlyOwmvLpOe5rJX8U7acuYinms-JJofEhg0qbDxghdQYHAxD7tkuk2MQWpeeX835fSskYMvZ1SwKgaLnzagp790rNw24nQ3GatxrFIjOUc5en70XmlqHlhuYZ-4lxopHpn6pTrnOc2g8bY9to-VNVKmNQGU99x5Gji4joWe-_gZ86YdDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت ۸ صبح حمله صورت گرفت
(توی روضه‌هاشون هم‌ میگن رهبرمون گشنه و تشنه بود! ساعت ۸ صبح!)
اینها همون بگیم ساعت ۱۰ صبح فهمیدن! اما دائم تکذیب میکردن!
نیمه شب به وقت ایران تایید کردن،
اونهم زمانی که ترامپ و نتانیاهو با قاطعیت و رسما نوشتن که حذف شده!
اگه این دو نمی‌نوشتن هنوز میگفتن خامنه‌ای زنده است و «کمین» کرده
و داره رهبری میکنه و…..!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5288" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5286">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPWX6JFB6Fuh9AFRt6XohYDo6om5o-44ZZkSuGvyLaE4-GxsiqtxilVydtpxoPDDDXs_jby3IQY_lZf_Jf-Vo3jnuk2qg050eBrt6ZjMnkLDo9ODpgsF5oJU9iLc1WxU3elHkcDbuWwaGYHQA0qGBrVggxhzrRbfzL8Al4G18jUwrMiyi2erWyb92w1_E5l0NfP7OWDEbKwoVBNbMhj9UxXgB5e-z3f4lsmnEqs2rUudWARyRijlHJ3yEsMYrw-R0Fg_3yIksSCpPfmm7PLxb5vwgHWU6AOq5Pz5fKcY2Rn-WDJ6sQGNF2iKKhm2Pk_JY951a3MlEVt7gGedfR9Hsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=s3IWUMOUOI9-R2Cuxk_TdflgkJLKlyhbAMVSZLrX2X-p96lAOPfdgc5c9qWxuU-JqUijSs6JEInt90poaSaLSDzhxcfCA2xHoZKXUA2U6r-LdD0oGh_UoGVhiCJKwb4y8cfLXIUr8ms68Cg5pHpOw_mAJkYDGAk62JOemN6zdPbS7iSdbxVhMqjF-9fTkEQ09BnQ1-0UMItBst4ywnUlJr35MjBVNLYu137dbtaLQSivNXmGnoLc7lG9k3_vtq-DoXNhfJv0IFbGH1GjUmpCmQZt0M_Z4A7wT1zzJWj_M6y52ETQvNJaknehjtWVdWdh1uji-G2A3EtVTUr59zaICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=s3IWUMOUOI9-R2Cuxk_TdflgkJLKlyhbAMVSZLrX2X-p96lAOPfdgc5c9qWxuU-JqUijSs6JEInt90poaSaLSDzhxcfCA2xHoZKXUA2U6r-LdD0oGh_UoGVhiCJKwb4y8cfLXIUr8ms68Cg5pHpOw_mAJkYDGAk62JOemN6zdPbS7iSdbxVhMqjF-9fTkEQ09BnQ1-0UMItBst4ywnUlJr35MjBVNLYu137dbtaLQSivNXmGnoLc7lG9k3_vtq-DoXNhfJv0IFbGH1GjUmpCmQZt0M_Z4A7wT1zzJWj_M6y52ETQvNJaknehjtWVdWdh1uji-G2A3EtVTUr59zaICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5284">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏روایت سی‌ان‌ان از درگیری شب گذشته ج‌ا و آمریکا در خلیج فارس
‏ایالات متحده و ج‌ا در یکی از سنگین‌ترین شب‌های حملات از زمان آغاز آتش‌بس در آوریل، دست به تبادل حمله زده‌اند
‏به نظر می‌رسد درگیری‌های شب سه‌شنبه زمانی آغاز شد که ارتش آمریکا با استفاده از موشک هلفایر، یک نفت‌کش با پرچم بوتسوانا را که به سمت بندری ایرانی در جزیره خارک در حرکت بود، هدف قرار داد. به گفته فرماندهی مرکزی ایالات متحده (سنتکام)، این کشتی با محاصره دریایی بنادر ایران توسط آمریکا همکاری نکرده بود.
‏در پاسخ، ج‌ا اعلام کرد به یک کشتی با پرچم لیبریا موشک شلیک کرده است.
‏اما تشدید خطرناک‌تر پس از آن رخ داد که آمریکا یک ایستگاه کنترل زمینی نظامی ج‌ا را در جزیره قشم، نزدیک تنگه هرمز، هدف قرار داد و این موضوع باعث شد ج‌ا به کشورهای کویت و بحرین در منطقه خلیج فارس موشک و پهپاد شلیک کند.
‏ج‌ا اعلام کرد که «یک پایگاه هوایی و بالگردی آمریکایی» در منطقه و همچنین مقر ناوگان پنجم ایالات متحده در بحرین را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5284" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5283">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبری که ایتالیا رو شوکه کرده:
یک پاکستانی در جنوب ایتالیا،  با ریختن بنزین ۴ نفر (۳ افغانستانی و یک پاکستانی) را در یک خودرو به آتش کشید و کشت!
https://www.instagram.com/reel/DZF42fzqtho/?igsh=aTJocnQzcWw5dWVj</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5283" target="_blank">📅 08:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5282">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سنتکام : حملات موشکی جمهوری اسلامی به بحرین و کویت ناکام ماند. موشک‌ها رهگیری و منهدم شدند.
به اهدافی در قشم حمله کردیم.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5282" target="_blank">📅 08:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5W9ut9fN04KD12ltoog7Gu6Qc8gx87zcoVvZT9Wy_MfyMFqby1svSx1Ayeb2JyDdYo_duKYSEWPTK1hmUk0DWC9x37KtF1XJ_AwZjnfC-VeaqCz_U5c2ovUDcOCLs-H87i7y6mNbamjYlnKtRPicPOuKkfR3EFwDMD2E7-mhvIvDAWKKBJjEnwDmpbEOBceF8AlLCp9o5KYq6X3Mi7GY2mMu3VhTaPwQ4gNTeMY87F-WK3t41sM-tL_ulSsbJwWwXKC7t6CqtZnhRiaTNHZAEC8fBsIKbkFjuJfKyHncf5i1PEsUXhPB9Py8_FD-Vf74MXq3tJrD9Pvtulyc4JMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم اعدام برای دو برادر دو قلوی یتیم فقط به اتهام داشتن تصاویر ساختمان‌های تخریب شده در تلفن همراه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5281" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5280">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
شنیده شدن صدای انفجارهای تازه در قشم
🚨
فعال شدن ضد هوایی در عربستان</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5280" target="_blank">📅 02:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله ج‌ا به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
حمله موشکی جمهوری اسلامی به اربیل در عراق و به بحرین!
حمله مجدد موشکی ج‌ا به کویت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5278" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=fZe9jhqvcnDz9BZQjl3DGPzzaqekMXldH_fO_G_cBBSi_Hci_J0Js0UFpJM4ZIb0poWw5nFHkGLDFMlP6x-dVxzw7DdXZRr2Ynv6PWHGsBmzejNCCnl4k1_QiU-5ldX5ITn4ZQNPUBfRTJyzSyOBnPo7eaYSTEabKfejvBbH9YewOSCmJWRnhiJjWYtiW8xy0z5_YZSaeMqSeA8D7DgjgB55W8vC2lPnxT7ASHR1xiSm_xBfedFDIRmxTmJJB1Yim8iD_SBF7vCJOh6Z702szbyocWm7GhkyxRLwsmPPqsA_IkAGyw5NL1Q2XSVqO1l3d6-DHpGoVsV21pcBySuyWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=fZe9jhqvcnDz9BZQjl3DGPzzaqekMXldH_fO_G_cBBSi_Hci_J0Js0UFpJM4ZIb0poWw5nFHkGLDFMlP6x-dVxzw7DdXZRr2Ynv6PWHGsBmzejNCCnl4k1_QiU-5ldX5ITn4ZQNPUBfRTJyzSyOBnPo7eaYSTEabKfejvBbH9YewOSCmJWRnhiJjWYtiW8xy0z5_YZSaeMqSeA8D7DgjgB55W8vC2lPnxT7ASHR1xiSm_xBfedFDIRmxTmJJB1Yim8iD_SBF7vCJOh6Z702szbyocWm7GhkyxRLwsmPPqsA_IkAGyw5NL1Q2XSVqO1l3d6-DHpGoVsV21pcBySuyWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امشب جمهوری اسلامی به کویت
و انهدام موشک‌ها در آسمان کویت</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5277" target="_blank">📅 02:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سنتکام:
نیروهای ما یک نفتکش خالی را در خلیج فارس که به سمت یکی از بنادر ایران در حرکت بود، متوقف کردند.
نفتکش توقیف‌شده توسط نیروهای ما، پرچم بوتسوانا را برافراشته بود و خدمه آن به دستورات داده‌شده تمکین نکردند.
یک هواپیمای آمریکایی با شلیک موشک به موتورخانه نفتکش، آن را از کار انداخت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش کویت : حملات موشکی و پهپادی به کویت.
برخی از رسانه‌ها از شلیک سه موشک از منطقه‌ای نزدیک شیراز خبر داده‌اند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5275" target="_blank">📅 01:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
شنیده شدن صدای آژیر خطر در کویت</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5274" target="_blank">📅 01:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=HB_KfJI58VoOXxLBOvzjkhKwLK9oehc3l48KyuD9bfxd3sEvRyUTQ1LcI8mqwx-_vp-y3jM-Sx2V9NPPJ8pMgbYDi4H1Pp4swaM-cvdQPyw1xrOzn50Z5MjHzjfWCgVx-6sZLe_NBZD3lZt4UIYQHZO1IpYUovUkN57QCBJFA6rFvzwg4CKLyRq_XAUNrww8UoY_1sW-3h8tQBcJxFeTlWcegzvfSIeVXvAoD2-ZvDoozbRlEZq0DNB5Z9F0THeCj1DlCXVVoI9zS9nrJp0xIJ-ftjZPOkW1IQvk32f660Ibp8plJ_JoeLNIwQslL8QEovNREjVfd9PECX8aRZgOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=HB_KfJI58VoOXxLBOvzjkhKwLK9oehc3l48KyuD9bfxd3sEvRyUTQ1LcI8mqwx-_vp-y3jM-Sx2V9NPPJ8pMgbYDi4H1Pp4swaM-cvdQPyw1xrOzn50Z5MjHzjfWCgVx-6sZLe_NBZD3lZt4UIYQHZO1IpYUovUkN57QCBJFA6rFvzwg4CKLyRq_XAUNrww8UoY_1sW-3h8tQBcJxFeTlWcegzvfSIeVXvAoD2-ZvDoozbRlEZq0DNB5Z9F0THeCj1DlCXVVoI9zS9nrJp0xIJ-ftjZPOkW1IQvk32f660Ibp8plJ_JoeLNIwQslL8QEovNREjVfd9PECX8aRZgOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=bYGe20GnSjXfi3uIYFcU3Ce_siBzulCi3tFllu2ACsfQeQjjf81b7IFH5EJ1osVpKaMY_-OX4msugnM8KfeJ4MVKiXf23bUAzAfdWNEAEzjeQvB0EPi6GjInSxszYYUJxb3W2lDPmVcHLnp1mSHBPXJQ6Dd9dGgTVC8Kkvx60McJ5BZ-Nk-o96qRnJVZ0WWH_rGbJL3eUwyzMGfCfzWBefSk9FDGuHO6d-lfyFfOE_DhQNf_hn-32HUSoqbDlo68yi2I-RYJp3ZtoeswO4ezXB-FTMQZwb6tfPTAWiGXO5mIVo_U76cAlo7dbtacTLSOKbGXv_J3jvWA1Zr2w0xcYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=bYGe20GnSjXfi3uIYFcU3Ce_siBzulCi3tFllu2ACsfQeQjjf81b7IFH5EJ1osVpKaMY_-OX4msugnM8KfeJ4MVKiXf23bUAzAfdWNEAEzjeQvB0EPi6GjInSxszYYUJxb3W2lDPmVcHLnp1mSHBPXJQ6Dd9dGgTVC8Kkvx60McJ5BZ-Nk-o96qRnJVZ0WWH_rGbJL3eUwyzMGfCfzWBefSk9FDGuHO6d-lfyFfOE_DhQNf_hn-32HUSoqbDlo68yi2I-RYJp3ZtoeswO4ezXB-FTMQZwb6tfPTAWiGXO5mIVo_U76cAlo7dbtacTLSOKbGXv_J3jvWA1Zr2w0xcYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=hEpGd7VarcTqvGUiHe53yCuh1mQMQydDmbpm3qvs87gjkMwInggmhY3MSE6fr9QlTTmm3GWVxgVYacbaKZHEklcxTUip3klBsuARxITiLGuPj4XRysxu6YksrBIqiGHav0PT7PTIkJkdASNrtmdrf5lsbsU5-paAtCjETdOS0DRziFurXLeXWe0RZ8V0fOVWaoeobaRiKJgY_m8MDybPEkhGYDnPesdhe9W9VUeu3Z1ulLdgEV3p01Anmq-jpm6unkmOtxYI6fR-l2wbgK_Rdw8kRMTBCdVj03vzfSt562qSTgez8SORL-3mSiSI59FQAztJJCsZsn2iuiB0q3LgUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=hEpGd7VarcTqvGUiHe53yCuh1mQMQydDmbpm3qvs87gjkMwInggmhY3MSE6fr9QlTTmm3GWVxgVYacbaKZHEklcxTUip3klBsuARxITiLGuPj4XRysxu6YksrBIqiGHav0PT7PTIkJkdASNrtmdrf5lsbsU5-paAtCjETdOS0DRziFurXLeXWe0RZ8V0fOVWaoeobaRiKJgY_m8MDybPEkhGYDnPesdhe9W9VUeu3Z1ulLdgEV3p01Anmq-jpm6unkmOtxYI6fR-l2wbgK_Rdw8kRMTBCdVj03vzfSt562qSTgez8SORL-3mSiSI59FQAztJJCsZsn2iuiB0q3LgUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب در میدان انقلاب تهران چه شعاری میدادن؟
نحن جنود الدین و العقیده / لبنان لن نترکها وحیده
ما سربازان دین و عقیده هستیم،
لبنان را تنها نمیگذاریم
(همون لبنانی که سفیر جمهوری اسلامی رو اخراج کرده و میگه این جنگ رو جمهوری اسلامی سر لبنان آوار کرده)
فردا که جنگ بشه میان میگن :
موضوع ایرانه! تجزیه ایرانه! برای خاکه!
رستم تهمتن و آرش و شاپور و…..!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5269" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حالا اینها با همین سوابقشون!  بزرگترین حامیان غزه و … هستن!  دوستانه بهتون میگم، روایت فلسطین و مدلی که جمهوری اسلامی  به خورد همه ما داد، و اینهمه براش هزینه کرد و پاش پول میریزه تا همیشه جنگ باشه و خصومت باشه و…..  نه تنها از بزرگ‌ترین دروغ‌های یک طرفه …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5268" target="_blank">📅 16:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgEZ5ZszqMXUTKhcLNVFFXsLQogk9zRlkiGP40hDlxqT2WJttU6WocAPGrQbRCz7EaYyOEjcto_C5aCTInGjJcDv27GnvwboLxK24JVZ2Z02pjrXaxgWwNEV1534oJZBqKbqe4_3cGe9D5Yh1k4HwkuWGcypbSir9_caFnAUmOPIVvEhCreSnTa3Q7eN6XpZ5F9fNy6MSEbYicouSmTbyI76dI6RJha2WPeioZH5P9aLXx0LdF0vo78kkMwaITB_Dx_mEu9wBaamaZl-erK9p1vu8y4n0awJRRW5KJAKrBqlBBe-Ynz3fx6509UySzj_SVKQbBQxA7PpRaHVyF82Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyjY6GjAY70nqUatpvO25UnYgFv08VG1bsuHk9moCc5_VqPx4tfZg9Ny3oeJVAI61o-M6AwJbEGGasU-_IqIV4yDZutik7EWe2f3NsXlAWJRoaiSF3Msb2O3gQJJPRUmW_LLbsryCyJRQbTdC9ZcRQRbq7awzJJt1u38WCJasfI7BCde4ipSGDnkBaYOkdYsq_tru5X0JB_FEzJbh2aHri67u8v8O2X6Z5keUa_LjoDbWMBTqfiLNRDNzeXiyTMfHUquwQmFrtkV2PlostDUC5OUF3Duo7dk2Jk0QXu7jqTdZC9ARXehUko1FJPqRZsmkh3U7834uFKuO4A3e5xYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dqt9BZ5lqPjuDGS0CokUHNhtzfXotl449yiSUgpvSSFJfPVQ0WuRjB8BcrKe9ucdZd9q8JUQfFw7gGHMo91DDW-IX8ZvwzlgtVIGFWf-7aqpBgwyvY_C0OMNVSlyZSyOhWG_EdGn0jY4cV9fQnqL8zHC-o8W5nw4WWMSrmzEGrRhRyIBBp8-IsLHPapsIpw8QOgusjm28tgz0w-zBiiv-hi_StpuG_Twuda86gKdN0Bpt2VX9Wi4W99CDU9-y55sjkM3Em9rHSk2q22N4X7SigmocTOiqF9XvEeH4KZDFH3Q4JWNMI7v0JDvqCBnqPr9v4MuwSuwJyZ4RPUMHGKvNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5265" target="_blank">📅 15:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZqAqc7lD52QD1YkGWHzUBtcNM7zVmkM0INHiyqEV3EUuAZ_bleWWaDBx9xws-eFqiL__Tp8seWdYjQfVZ4W8jYnfDcJcqswokXQTaisORcFC8OTKD3eHjOYJtwxQi46vGA-5onUQJ8AOIH02WhGc8qZYJRnjIak4pSNNzqqIcocQ-uDtw9FPEgQbHE-H7Ok24eiRDE2t1jx_WmHbJ_eCl3N3KIri-geEHri-5A2ICo6wMoef-fHfIkOOArSgSgdZkva0ruu3uaMAXZk_9pB_aORWBa8ioC6wH6Ef5x-pV3Jw3UA4CeFK-sDnUTu4L_vsoKws8o3KmzLlaFiU1B93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9NCYzulKCq1AFw8Byrue2lLJzZHzM3p8fOktRwbVAuvoG_DyIYrAkQjCwuBoGoNGQScxT2Q_5kWLFFzxuc58sWZVsw3I33BGkYWt0jpvIBWVg4A4aqskspuuqjkrqtecDteTvc_1Vqgaxl8mHr2xXnK5OHueJBtpZGg1Que1-4BFXa0z4dyBExodBdah5e3LwbKjeug_SIgjHFp6BAPI9GlPahNuLD7pdXcpPFXN8ivo_8GWhPE0EH8OV_nK5wUjK8_bsrL-RqSpTCDtQ3-bzsLJJPuCwKUBQxCR3yCBVNh1X3daga1UIYsR2Uz7iTH5Bp4z5R3omr9i7AowjlT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRf-3l3TFOc4DD2xMHLvv6Z1BCsrWDxmtyNG1XykEixM5xcl0M99HpUVkjlPGUfe5kign4uGyLW09PA3fvNut3R3e7c7Y0TV5HtBuBsVtpbKUNBr0usaZMnbm4rKnpnGJb5bGQjBuEYw6Gjfc-j723raKC8yUyYdx-FktOj-szkVuT2uEZ_2-_X9Y_KtNE-N-MuZoGLIOJ7bfJX-2Cosp1Hu1Q7nIDmhic44zdS4ZYOpEZOuv-bo1Z1zP6NKnWR18b7wgO5ninpWeWOyDpLH7B18cqN0oBnV6b3M94zm_0swXPZtbVxPhsNLL595N8GuUv-XVR0Lk1EEPuH4nD1tIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK5IRXCy2fxSDWd4-a8B2K9kGKcvSg1bKDz2UuDDArBTM9x_ueCNE8tQD0LvK7qy0SkHGw4p-84RhlFT71zN64ImFIHY4Qc48-sjydOdlXK56j-3NpMDalG7kMWWLUtq-_N0-jX4ad3gGY3zXHJqZoX0UOxbgIQYUdCdgexVzaeYsccu8tFYdRtha3dS1eVrRKZFklisLcCWaJAKtF56wB13Oc1oO_9O7ZAEp4ou4z_YLKmh1EFuXvic9f2wEmiRcST2OR95l1w17cnThWKo6BbpGCJC-Gx-tsdy7Vh_u9W9TcJepm52DnkoUG38ZPiouCuytcbWH-XBhRDKtBTT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=m5uyw-cQbCitF6BUgqrVTau_7yOoWKVarUrbZlqSbQkUI5QK8Xa7UL2Nv_ZA2q5pZQqYcBUfhnZXoo59dCHgQXfwJIeNIVQpK_LTfJzBjbRh4YSg_RdiclhilynOjybNzC0-BxaJUAgegufit5g6YCUDhn4tAPLSVgY3tu8EJYKlBPmJC_7nF9-JdsyvVm3oKL-iYeFR3guuZSU8iEfQYW_4ch-vGCDPI4B9wY2aTdsfsARDbP96Sv6GnIckVuqliRZFLGIf2rnWTq-G5Kt4GxnHO5htRyBwRpmDXUO5yYrYKYOi0fYvupY6FQ9jaZ4t6xrNgw1YAQJl9IbWbx_hnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=m5uyw-cQbCitF6BUgqrVTau_7yOoWKVarUrbZlqSbQkUI5QK8Xa7UL2Nv_ZA2q5pZQqYcBUfhnZXoo59dCHgQXfwJIeNIVQpK_LTfJzBjbRh4YSg_RdiclhilynOjybNzC0-BxaJUAgegufit5g6YCUDhn4tAPLSVgY3tu8EJYKlBPmJC_7nF9-JdsyvVm3oKL-iYeFR3guuZSU8iEfQYW_4ch-vGCDPI4B9wY2aTdsfsARDbP96Sv6GnIckVuqliRZFLGIf2rnWTq-G5Kt4GxnHO5htRyBwRpmDXUO5yYrYKYOi0fYvupY6FQ9jaZ4t6xrNgw1YAQJl9IbWbx_hnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM-Dm-QcLFcL90BM9a_H1svEqgPVXM9sPwj61dbKD5FqG7yuAXT6kO8c0kc1UcY1sBii2F-Pi4JCls9xY5PmSON0lyY5Dxydb-vMZz2PKVnFjegS2YINqiLpUfCz42J7q0wyRd9lLTlN3yGcRx8QUY076C7HuobWeqHqdiLyxEPbY0OhxDf2af4sCvQ0ifKHRpdEH5F2zWKx_IY5yNmuGz3IQr8NLssGJBND0MnFarzgaCJWFFCOUr_aKJAgHqdh9ZEfuO1kWUvy7ckKSQGf_EkUT_bA28vx4gdjAN1Dp0MxA2_7YAq5XleWmYb3Uw0lShOBcxPNmH1R58FVl6c1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vocNG_9mtr-mVCwAyBtj27jobjxd1g6PYin34ZAHcV6KAc-S98Iui6WB1GGzeDOCL0KsjIATmWK7f45f7Fu2wJEkFxLdHKKQ8TXZ_Te7rhTkQgfLfzh2LpgXy4rlR4G6pGOEhpM01mTYYGLgP7FWEeRnWmLtAPY2-3slcz1ctu1KuU_IT0F1_2ew4KFWiPZ2jAj97_qfpafdGptMDIww8bTW3BXD2yioH5c4V3ZAeSOxJIjrud5TzgGHXjrwzSayj5oMCMH2I1n8VyWrK5leb1-hx43OEfHIi2qSE6clIJujm7HBCiI1rKpRL5JAC_ZV9K8jS5hYqCJnpRmv2bdRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjE6hfrpz19pKPJiDodmhmF8ODGVGxHxv8iyf2l0Xh__W9I1Ly_lDbvKf7mzyYhHcUto6OzA2bYEwUo8dhIU2ddX8Lz_LUQv3RQLXJWhEco61nc0TFquwbadWobkKXf_OzrQyokhvCR9pHeHx4kHiZfz9ozFRJAp7_H35k6XTNSOYEbMttuIO_pfPZ93U5o_HEmFtLvvAK-TcdGXWIoO3NWhrF7B1MYp0osGgqI98A4dCYh5qMtvzl5QqV19KfAVANsP_C01wGZlTQV5Fw4siqL-Ln04nVS41XnoTJXPdQVKI926kI_wVhcazMXTyQ3taqJTT_SMvoOccXDnGMxfpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHV_Zub5CLZ5BHU5kn4_mwIPjusBuz4weQp6EEnWVBKbhifn9D7dmJs4XPLow6uCyyfkSaPqesgW_7cBgBvB_qQQTie-N384bXW2gBbtUX1CmCYG0-sbdvIJ5Sw_ggcI6I60_6gye96Bc93Omi3WXUmK2Sd3hnxolteHDTIiDICmJvr8zsd4N6fnIUL4h4wnKmNVj2HnHMZhyeB3-L3bSu3OThCtVOOwysJdQiw3icb2w-GhPZWXY0aM2PAvE8j64uY3Schis0io80lTMPN8pcaBO5JnGOWuPs6xoa4t6W5MTVug8tV5UHVL2Z-15ElKYIwBA3ngM8jlDp_8nZ4u_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T93Q2VVdpDaI2mZ_w0zNnL__DzbDFzHutfo7rh-b59HMXwQCffnuDuL7ZiZotpBcYLYg7PGDb_vhJeFf9c5tGJUUIgfceLca0MgMu-zaqJxbdpCsXKC9cn-ALx0WrI7AJ74rRKhE3GjBxC6DdAx6oyA_EhTSI5qJ9yoYGrLfCC04-LTN5MS8uTpuoUmvhNYv1pCv2waHxgVOumXF7UiOwo43zPIdcD_Wbxu29nLh4DmdbkSxwtvXW8LE7KXvTfWrZQjmTS3yjwkM588Zb_C4NCYnVfgXRN5NICIrHQmg-FTvndaaFeXUNenAKQXyF7cJYd0J25vIetPHVUobujIM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ff1ElWFqFTKnzXf_Bfo9ccafgExsqSgydhO1pedWUyK4Q4ti_V5_bSzKdF6lx4qjYG5vwWfNEAhy587QE5Vp4LY2rx_5I386WmAa6ci9MFh2VBe2TvPl7YOeg5pJVkYdXd-SSEysgnesj6EcnTZd94j2gqowyLZuUaOwKCMpD3dsZ9hUDmhASvYU-cGxVUSvXbZLk0Vj3mKY_imgvPqpWxvngn_9tK01shGTT8r6cVTfR970ej-ogdZDMA28qNKN1Dvr6RWKzgF8DM2EA5YNeo2jbe9WdGXjccFLBfYhYi10eaf60_ez26ezTiY8UEC5hl4Ssp8OIVGuSDXaVTXh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GfsBsEaOGcseUY2s9dJFJpl95NlDqxGRu2Z1to25Rz_tKpTYUNdA5Y6tvLDAn5kDPzQONZkm3o1jCglVnt9YYdQniZVc47JB3sNmlw6H6I9YUHrCU1KxlZ2-2LC-DKsX7lOQmpJs46UF6j-dMS6SzFhGPfJt3XxVdnmXgBcw5CE1YR5vdtGWssXVqrvsHbB8uy9O08Yx08JP9uf5OZzG6I6Ab6SJvJUi824wOn19LdteRUDDeeyuW1yFEEl2KsUHx58piI5RQeYBwZBW2j0V_ZnLhe4_wLL5EdsFC1XS17JMG71PdwZnu3XdcRbDJEnDk1s_WbMskm2cAHl3mXM7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bh1hStawqDxteJiitfZKSnE5EYWo8eTHTSxMoMcqfLmj0FZ6-Epxw9oGqQmjsVvNlix2oulFBE5bLql2k5D3PaKrIANerzdVsYqk4qTtt3yvH1NE9MJ_qraAyDaSo9yz8bcdenMTlfr4a4frBkbM6ycK0Aj4vX-UM_-HPZHTDi1LGLIeoNbHtZGRxH5dw-vhOUSyaCn0N_X-CrcAKF2sYyLm9XtSGJoMQPCYy10M1uTkMK_v6nsKbCbn00expJbbce_kNe1I19WLlqpw77j_6Dxkec9CgOw7MRuubmu-UM8EGkL9n1-uKuD9lkW8WTgpP_Vpl6RDCH11M31D3H4t6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=fOyqF926vtMUdsw_fZ0kI4U3r050HTW8MyHv7jUhIAr70qc5XdPcuJpWZ-nrkTjuia6n29fgnmqZsZ20V0NejBJGvTEK4guTLMzUpWl456tjyq9_IHZTOoXoLdVB4BkczjJI2EUtumfsV7qGPatmBvR9_OeD6xniN1l80QIXXpKAZ7hs2ireQowCsGbINek_2M5cbIRAvYH3KR-iK-wH0TCab_UYS3OYSaRCd5vZHeTgdP3buIGglNZhjUAaZZqk3RFQhngzjST_9HpAlkuwDifNON_AismqP5OSniP4tJxBsYwCu-HU2AuOtIYKCde-K-ZzAYeiwhQiVZfnx2bnRi9K5leEtyqW6z6xGfkxUn5sBP1Unz7oJSbMpZ9Mvw0LYuucD2aXnNwU03LIHGEpTJmV4btAe7DHTiQuVi-l7gLqvrbFio6Yfu-MSljrZCeNjacBe0qUl8FbCwRhFuaRmtX8iW70Ur_9e-BNb435B4pux8xDu8OUuQlBLDofJDPJFB3ZSuu-XMlYvvkgzWVhqxWOac4FM0oobyz8foZuKz45DeJwmeVGFa7IJUyQgWwVAtFjxo3M5sUf9sMcS4ePFZ4EjkslJu182iF_M0MEAmbjpPpgrhKGnD622QwyF9qbHq2aX86Vh4f5LHqG_4QXUIEOYBqo9WC0woiq2JEohxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=fOyqF926vtMUdsw_fZ0kI4U3r050HTW8MyHv7jUhIAr70qc5XdPcuJpWZ-nrkTjuia6n29fgnmqZsZ20V0NejBJGvTEK4guTLMzUpWl456tjyq9_IHZTOoXoLdVB4BkczjJI2EUtumfsV7qGPatmBvR9_OeD6xniN1l80QIXXpKAZ7hs2ireQowCsGbINek_2M5cbIRAvYH3KR-iK-wH0TCab_UYS3OYSaRCd5vZHeTgdP3buIGglNZhjUAaZZqk3RFQhngzjST_9HpAlkuwDifNON_AismqP5OSniP4tJxBsYwCu-HU2AuOtIYKCde-K-ZzAYeiwhQiVZfnx2bnRi9K5leEtyqW6z6xGfkxUn5sBP1Unz7oJSbMpZ9Mvw0LYuucD2aXnNwU03LIHGEpTJmV4btAe7DHTiQuVi-l7gLqvrbFio6Yfu-MSljrZCeNjacBe0qUl8FbCwRhFuaRmtX8iW70Ur_9e-BNb435B4pux8xDu8OUuQlBLDofJDPJFB3ZSuu-XMlYvvkgzWVhqxWOac4FM0oobyz8foZuKz45DeJwmeVGFa7IJUyQgWwVAtFjxo3M5sUf9sMcS4ePFZ4EjkslJu182iF_M0MEAmbjpPpgrhKGnD622QwyF9qbHq2aX86Vh4f5LHqG_4QXUIEOYBqo9WC0woiq2JEohxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=H0wKiO2OIw5-uk3xCNY9r4BjunM3EEI6IeJzAlzDkD9rucM97QXn9PeqAkfD5oqSzvso9FrNB4rZpeC6BQoeUyhVKOc1zNsAh61yZfokPyESbYELwL5qE5pdrsgRlVwcheaAis7tiG-UHGprs7fmMzztnw0dCi_Msjco0WO9SMhCdo2jSlktuPV8DOsLsRFXJo8ve3i-qRUoJ0oToQMY501DrdXVpsXSSCB3XaHiwffVHQJxvK-xFoDS8Ge0o6q_IxPVSNcO0GkCylL4i4Ah2a4oc3wEpNzGuWXjmCcAAZY65DhCj_oESRRD2nle19IlFOBFz4yiGwFc2q0lQXUAhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=H0wKiO2OIw5-uk3xCNY9r4BjunM3EEI6IeJzAlzDkD9rucM97QXn9PeqAkfD5oqSzvso9FrNB4rZpeC6BQoeUyhVKOc1zNsAh61yZfokPyESbYELwL5qE5pdrsgRlVwcheaAis7tiG-UHGprs7fmMzztnw0dCi_Msjco0WO9SMhCdo2jSlktuPV8DOsLsRFXJo8ve3i-qRUoJ0oToQMY501DrdXVpsXSSCB3XaHiwffVHQJxvK-xFoDS8Ge0o6q_IxPVSNcO0GkCylL4i4Ah2a4oc3wEpNzGuWXjmCcAAZY65DhCj_oESRRD2nle19IlFOBFz4yiGwFc2q0lQXUAhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی
از فعل گذشته برای مجتبی خامنه‌ای
استفاده میکنه.
مجری : رهبر جدیدمون آیت الله آقا سید فلان!
حداد عادل :
ایشون از آقا سختگیرتر «
بود
» !</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5250" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5pHzrs6JhBGJU3UQXCzDpp9tEbmFWH3NlYPmDxT5NNaYoW-_5aWDUY1e_dAwEu9gBlNS0okQ7_KAnlW3YjSoGxJLPYoicgPY3fMb8lgOqw1_gv6GmAO7RW_47ESiZZx_YlurHnCV1pjeoHKjGx2YbkzNSd93m5_-vVx5LgHnoSBzh0YZsJc2z1l-Rk38KAUDV_TrtBwFs8HWgnFITg9ovHHocsHUzQLZ0F4H6yicSdA1QSrZIa5OyEy09noBIRwoQl7gd0KrHeAvksqEuPghQdievA72DJVrxULNIZbfO9bbE_kXw1TW7bi3mKhUp6L3w4S89EqsGdKwG37s8J4IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5249" target="_blank">📅 01:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قالیباف در گفتگو با نبیه بری (چهره شاخص شیعه لبنان و رئیس پارلمان):
«جان ما و شما یکی است و پیوند ج.ا و لبنان ناگسستنی است.
در دو روز گذشته، ما به طور جدی توقف حملات اسرائیل را دنبال کرده‌ایم. اگر جنایات ادامه یابد، نه تنها روند مذاکرات را متوقف خواهیم کرد، بلکه در مقابل اسرائیل نیز خواهیم ایستاد.
ما مصمم به برقراری آتش‌بس در سراسر لبنان، به ویژه در جنوب این کشور هستیم.
اگر توافقی برای پایان جنگ بین ج.ا و آمریکا حاصل شود، شامل توقف حملات در همه جبهه‌ها، به ویژه لبنان، خواهد بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5248" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
به رغم گزارش و خبر ترامپ : حزب‌الله لبنان چند راکت به شمال اسرائیل شلیک کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5247" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5246" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Phz0uSSDzv4eL_L3modzjRMau57Sni458UtTGmZlEIW2RuS2Dz3_y3yafP8ZROENq6RKUBqtH_qOBUASRB8koEil9qYU80YW59HQrNjZ_UJ0XNKXpI_noF5AXV7bJAxWNV7ofVte89FEJeZt2ReFILvOUOLJN_gSEP2gxzzcHovFmqn85D4d2-PE_TpP0jKHaxZk1GrU9-Dn6iuppTRLnOUYb7AWVX7-21MHYlQo6lA1Amqo7jMS98gbnQL8qPpNelFn3uZ_XE3OhwyatGPjUw5bLHni09jM1OYzS7JQ9HyLLS10kO7h-tyVpuEGdEKChpttnV3-6Hkkgaxr5DSMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه جمهوری اسلامی اسرائیل رو متهم میکنه به «نقض حاکمیت ملی لبنان»
یادآوری :
دولت لبنان سفیر جمهوری اسلامی
رو اخراج کرده و گفته مسبب این جنگ جمهوری اسلامی است اما سفیر ج‌ا
لبنان رو ترک نکرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5244" target="_blank">📅 21:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5243" target="_blank">📅 21:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ5dxWMbuSh7SRGT7rJcdVbmzKTecrIY8xWi3kktUIGwS7VYTrJm5EYxgimLMORu7m_k_yCYN7KfVRf4BB39Py40SpIYT2c1O3IlxUiCNHgW-pq3kgZkt28VlGSHvgKnV0jltY80aUZRKZlyo0HMaY_o0fqI5X098nT7BjdSZQavdDGqjAqr794eIz34i6KJzENTvwSBBgp0QITiuEfoHriuzFZmwa6hsDJSCpTgx6b0bwoego3NMpXBYll34ZryncfQb1o5y3x76n-gcfu2p3baLkjdSoWH3S0drxMpnuL75BMT9hs_f-FSuj_WUKgIKeD-QSVltQVzVlHOq0iPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt45CsUE1QtwHKatTMDPLA8_pSU9Agczc-xbG_JzVH3089-DE3Ha2zzHi9KnZ0KYPGc6fBL2PNpt5Tg-RChXYNRBDeA_mDtnnUYACrhVumBmkoZB7NQ87R-Qjs_gh62kMTVkByewjG7tWnTdRnDk-3QoUhI3ChmFXD3Ty2gHam2gymjhk0NE6HG5Y26-iUpAWETEeP4HwJI_dBVx1Un3-Y7TGiWTYSznBQ7kb1uh4LU3C7QOE0v9LI5XywHecH95gv7UEEEWgKrBiAQ1p4rTpOBRwnZavn0Bo7YRy1KKxSYHy7cD0sldtuhpK_FOcTb4PtZS3tynswCsxuFWvuEoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHR3C3XZynD9ZDhnQ7LFNSS69wnL92P4MDdaUNbF9OM37daPwlTq_54ToARiTxh7YRDy6U5LHPlqfQWK-iW7CokhZptIr4QjdhowQav7TglCwfkgmT7CywutHZaEz9E5-FWQr5dbdeKC2uShp4AqKs-Fs5t1RLeQCqF1arbTde7dOO6tiIvaRbarZLwWsyC-8FyCsd4rXSEqe5GP7vveLHSsG1B9_qwRr5KtjMdauMDtlVSoGUBDas4-h_uSamfKbZ2k8OjdBSkerPrnFfLd8Ia4hweM8L6jPtn-w7qerduWwDAZSGCjXb6lDI8qirqH2nhFXrG-zBci1bFWnTJxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
به خاطر گروه تروریستی حزب الله لبنان: جمهوری اسلامی روند مذاکرات با آمریکا را متوقف کرد! سپاه ساکنان شمال اسرائیل را تهدید کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5239" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3SVXl49wxMNOgrIkZ-fV5miVvHntioRscNbI1OFIhJKzmrtQizrSFdV7DHUo07SKxfwCw3xkRz6XT43lun_x3olrjz1MrC6-WkuZmAM1N4eKH6_fjBK1lJ1CYfMBVl_wHaUCbREXk6VpFKNuOE3FTOfYwinvYIQPf_fOS7sVPxhi4agzaXOLzFniwNsttQVicUXG5hs01dXsUDQzlmN68tNzSWUlmnfEqxXOJtQvy88XwpwBaW-UINM4UmUaAqrQkAjqarA1ykVKD-NpdylHTO5tnYJebQGazajjcUvr10JZHseYtVHza7YAIYnktRCYxUWPIRuxoBTJniHIqs2jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتابهای اسلامی برای کودکان
(در مصر و تونس و….)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5238" target="_blank">📅 17:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این دو سال رو یک مدلی با ترامپ راه بیاییم و بعدش بزنیم زیر قرارداد!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5237" target="_blank">📅 15:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK6Wt6CZ96XQSDdJTsQqPwVv24IUtG1jpN3Te_X45gRSmtEXbQRiLju_w67S9BGQoNHVJTzqm3Zb64bQDan8Z8slizCS23gn0TZeX1f59WlGt2gWqHdDabAUHlO90hrMkr4nmmk-mZ2qjMATxBElR5ls3ksDaUUONSrlcd0Vznntgz3_1NOEoO96z0G6fDIc-ybkWmXFXs5CqzhdKOogvmAdZOEAoknZNKKx4rMeYf48A_7s20T49b_NOqcPy5GR-oz8JgX-wRZzcdpLx-ncoRc8avvycMiSTq7mOYLNjDU9WzFPDyKv0-1ZrU9gEYHWql0y2gDjsbVfgcEIzK0_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نتانیاهو دستور حمله به ضاحیه (بخش شیعه‌نشینِ بیروت) را صادر کرد.
🚨
بلافاصله پس از انتشار بیانیه نتانیاهو، پهپادهای اسرائیلی در ارتفاع پایین بر فراز ضاحیه به پرواز درآمدند و خیابان‌های خروجی این منطقه بند آمد؛ هزاران تن از ساکنان ضاحیه که پس از آتش‌بس نسبی به خانه‌های خود بازگشته بودند، دوباره در حال فرار از منطقه هستند.
🔺
نتانیاهو دیشب نیز در دستوری به ارتش اسرائیل خواستار  عمیق‌تر شدن و گسترده‌تر شدن عملیات زمینی ارتش اسرائیل شده بود.
باید دید واکنش جمهوری اسلامی چه خواهد بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5236" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tei48hfUJjFsfgOhQiIq5-2UiYJw242VIV2cqSQYQHLyGMlVxnEA_u0ES6gkiyEh9jl-7t1OtUA2arqJYn3_ogkszQw6UQl2xy-eJGAGEfuV2fldQF7ZllWb7Q-x8VuSWswFBVgD37uGXjwCGNpyey0obfT9w4RndAjIgt-zQ2DyzhcdoZakynQZZLVvkPJLv8W9mbGmtWTgFCTOI8ozgT6XHegp4M-_jm3wE69iy-vMELEWPBAr6oSBB1-sVydCAy9PNTbx7jU89skE2WPLAfvjLRZYBgPr4Na4DqqPpkAfZi8pwoiUpJktOWRegtxUCS4wB1UH4cc6rGHEW8k00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIlqUcWA13oDwfBuEmT6l5XFXIylpDWixbFYThWKC9_k7Nrt-XSYF2tk3j9AtyyfJoN_RWsNA3Hx6XJU1ltlhdlfzishw5BpTcseqnVGokV3DZllyu2It0r3P2i6XehYvjXKH3mPEfOdNCys74XIaiYhGXZXbC8MZMB69R9HW7bzDOos397ajj7bHduKXfgLvXW1bVS2WTUU4FPH0aHTgDHjI3x_sTJy7ofoedxuAvFksxJlEc4dc1oPEp8BiB_vDzW4vJ6MSZnwBSnG7UiSqyt6QI-7tuUi9D3ZwXpekcf4IOdg3pMvP6vdE4MT-oRSpeidpz1vmgNd4fYANI2pRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=SEg5ma9YVDnDC1coKQwAOtluERhY6ZOFuI5cGAsbM9RUGgM65CGUjShH0WHRNNkKsdCe_JTTfxB0o3-kjYgeSyi9CupYr3SWCJY8Ayr7BBq0TVkhmhKvy_zT9UZllFjQY73Y7izb9T6GrKjzobEhmm_HOXodvqTc8SQ3adtGENO_uy1kmANNGSPAQZHlcHCWCDhK6Bl9iId35iaafzQT1sAj1hrj4KywB7nlR1OaRpBS4OIa3JVMNtz245SDaSIN8VswGcGKdewXmoSAIZTtfXel4z4-JMlZDMHZuoswz2M82XWBuxeoCgP-ai_oUzobj2JzXTU_mO6MBW89DEXocw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=SEg5ma9YVDnDC1coKQwAOtluERhY6ZOFuI5cGAsbM9RUGgM65CGUjShH0WHRNNkKsdCe_JTTfxB0o3-kjYgeSyi9CupYr3SWCJY8Ayr7BBq0TVkhmhKvy_zT9UZllFjQY73Y7izb9T6GrKjzobEhmm_HOXodvqTc8SQ3adtGENO_uy1kmANNGSPAQZHlcHCWCDhK6Bl9iId35iaafzQT1sAj1hrj4KywB7nlR1OaRpBS4OIa3JVMNtz245SDaSIN8VswGcGKdewXmoSAIZTtfXel4z4-JMlZDMHZuoswz2M82XWBuxeoCgP-ai_oUzobj2JzXTU_mO6MBW89DEXocw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال «پاریسن ژرمن» قهرمان شد و پاریس و فرانسه رو به آتش کشیدن
قیافه‌هاشون که تابلوئه!
توی یکی از ویدئوها شعار الله اکبر هم‌ میدن!!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5232" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.
پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5231" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFurynCo2ecfKudPJocxd5qkeZWGNz_mQrPi1DKtvO5jgFTB_XiwVAJiFYnupjnMuxdhK27ccIDvApUp2mxUxjFI8zp0n-rxYVkPjD_hTV-R9k9wDbk2cvaksQEomhNmql7s-R30H00d8xgrc9wQAZ6r7mPayd1RPzgwKKS3UADBBHrE3YCoQSIl3uOIN9fDByh4UR7SIt3sy58VsAXUU5sNgPLid3yom3aewuQvXkc1MFhVh5AeGBRdJxV_obJFJkb4mq9RTFiFklgvEri3_GQzvN3BbXBNN6MsMpqpQ703XFLXsGEUU8gA2fdTNGY3-fpe1tR5zwZek1ydynfFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش آمریکا رسما اعلام کرده
که چند حمله در دو روز اخیر به قشم
و گورک در نزدیکی تنگه هرمز انجام داده!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5230" target="_blank">📅 11:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=n65OFM7FvQEOeGXaGvTPqylZR4s3kwDUUoMse3bsGPAicKSqDj6lRebixAJiUeJzQcB-nC3gQdbBp8BYAOejE9qYNO37ZjXS8F6TtV43jfHx4xJaKDBGvCsSAdZA1oo3uNRTRhSCB8hNaFiLmlahW-Vd1WLA7hj0CyVgWIabytwrjRbF8Gz-LBqbZxvAJbOzPEBJA2tljfTyM6VhLqm4fXuNampmvI06hh_5wrddUfvx2DlZ7r-DlwfR6MITbIudGdHVELAv4v8GcgIa_7MlXRKwFjb-TqSJwEKoh5pKOuGspFMDieI0_GW9aJbnvmBDX_edT5-fRf6_o5WHXKfZqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=n65OFM7FvQEOeGXaGvTPqylZR4s3kwDUUoMse3bsGPAicKSqDj6lRebixAJiUeJzQcB-nC3gQdbBp8BYAOejE9qYNO37ZjXS8F6TtV43jfHx4xJaKDBGvCsSAdZA1oo3uNRTRhSCB8hNaFiLmlahW-Vd1WLA7hj0CyVgWIabytwrjRbF8Gz-LBqbZxvAJbOzPEBJA2tljfTyM6VhLqm4fXuNampmvI06hh_5wrddUfvx2DlZ7r-DlwfR6MITbIudGdHVELAv4v8GcgIa_7MlXRKwFjb-TqSJwEKoh5pKOuGspFMDieI0_GW9aJbnvmBDX_edT5-fRf6_o5WHXKfZqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
