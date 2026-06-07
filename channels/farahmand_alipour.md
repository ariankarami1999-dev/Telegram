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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 08:32:57</div>
<hr>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Rb7vOKXYANEkdTdXUwNbKtOg-yTW5f-WxScQdtnNehTCQts1OMRXGiJHXuN-NvzLsoAbMuXaSRGF2nBuc93ChBu9zXRTZNqoy9ZTksUAp7KyDRfB5kjDi92z5gNuHB-5h2tBtgdb-8q2hY1A69K2-ted5wmOLhZR4FTjAn_Apr9ozSJgTRLFO4DCAeHIZuf-kpTCp20N5L36G6wCxcgJbJ5dPD_as9diM04QqAyF-4_kET89Au41qQdY5JLTuu8O8Y4Of5rUkaAMBm3J1fgTxJXIUHQTBPYVoLOwQYpZTJzsvYV1E7jkuKx4VW3oGDfVlPx9bbXLAOkv9_s6AgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ1H0l0U63-k3oVaFUXprFif1I3hz7MLvyLASRAKYVzXwq-YPOuaKaldefYN2HQtfKmPkFSQByphYfBBrHReqUTr6e-UbMTzqk4XexdCWR7nMGpftuH9FKK-9Ku6OKw-tpVepXAaYV5Y9-Ld_wuCiQ_YSRgOZME-vVZQgDF79kV83Wim5N_5ADJUCOcdGZJuZuwpIEeKAOuNYgG1LhEAYu5mRr-MMzbQEmGna9-88hqszGhBjP7lpkiFzycaVBNZeQ6OI6gXHErGhEgcHLj4SzyrU_HeMiI-YN58d0wOaXAUfm_LqDNEM_yZ9avXs2VeAV7RnBFJPHypQ6g9vdV2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ndz8D0Yg9Oidr9Rhk9icN6mNFcDL_v0xfLFtOymm6lbQbS6a93goYsighEi4XPyxYpGFnC6oabestYnTW9PLsR7uZ9arktJxpCqhTBnCe19mf19jEZ0SPWAvyp3iIRNnF5J9IMpH0Afec5auV_JNzZEvqtdA7nIheuD98qnGaox6RB6lrl4sjTPm5EsRmYLYnrb5oTjwN9x6gq0e44zavxEzVTzzGs-sBLtTIHhtwA8TYEMSvPZ3pbt5fODXKx36LqGrK-DyTumzJeAcG7FNFKUWF-_SCy2DFSsfft9ckni7XaHl0qpzM7_cRhaKpr_cLMz9297xeD3bsm3Vsq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llyRh8x-y_tU88pcPE92AivwyvMYfH9WYQmbaopIJLzeBh5vX8XJRQ9ZqnOhmEXQzVSKQotZ1bMUgHuXV1fj-HXvjBeO6CWv-MzDaGlvqTHT8r6yTzJTYELbpEVNPCEqWakrXlNHYhvunXZD2ZasHVcOCwbd9b8XtlonOtZBRtIJkSipUdXROYesuYr16WJmthmyaPqNxM9XAGDWVYUAlcn2ocYzxQpkmlRAXxbujIfVuU7BupSyvFktRzRooixKxA4dM3JuqMuLcYq53rsXAptCJyw4l2IAaEWhy8oKM-zUNw_GSIrR9DoKiactF9Ur6Sr007_m0-cS0W6EYz3fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiIZYTURhwybJSbVPdI0kCYcFu71qeoSF_giNmbBnB2U5cVPQMqmWZPTr1D36Ri0ARrAra2X3rjwA3HJRENL8v6f3cBKu7Ox2JSDdUmYNn-X18BPVZJDlMTJCso_p-viqwfr_HCRo6vTh0hromg0SRU3l9RVWAR3oWM0kpgtR2j5Or8cav-cBz4vc6__mykgjeAK36TzYw9FshetEOUtC4s13ECS2nCQS3bo3qyuW09pnUJfEekkxSMkIp6O4WJcFZycRnF3OrbqRTNv-wKA2VFcX0ItpVgWVG2VoXDFHmC7SNsAmnSOgbTJeBvSSeS09j1XI6jwvtuqz0p7bYK7fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkjMW9Ripsw_aZUHJ-A-jWeQsQYE8kJP4cxoEDi6jT6uFSus9QmyCwoZxEUs-spIvd6UKIf2vAfCr5jgpLayQ5G-jHlra1wXj6hstdcI_kd8OSDJYZHymty8ogPrjjgqSVp2Bs2HX1pPEUytEpEUGsW7nZuraOVCgRlWozSgvoBFYpll8LVFpFAAYazuvrEjjGf3QJoNcd4pmAETTdisJsd51yfCuwloWS7NTU_CRmh1q6O22-HMj1KJpR_oYFqNk6_hX7b6myJoDqrPY_JTsZIrAZyMgP32FZEKtnNWXZpYTtjNcLhBQkkHZKcLx06-vKYUnAd_jQna9wPNHKNoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbGlsor8b9DpX3qbPIM_nRfRy7TKxbwgL2oiosM2PBrt1cod-MpzJhoQ_jPX0-SjpoO4evpyqaNT4GlNMWP_Y3aO61nKVMwikzNlRwHDTlmHZpC81CnPC1gxY0E-tiSsFIlBYW_H8Dz8aE-3YKnrbzUL7vI65hfvrhN0hC9i_pid88Q89HFDdvyNnb0FD36GaUa5VR-FaAB1dazciXWZzQKhWDoQTLfr6oFnL0rWOupdVXc7Wt-Q0xCteBH6QMjS-ARyZdHbj0T3-3eDHqjkLSvmMS3XNf1Fb95lnXl2kI2ctsuAbv9M6SCCgMvxsYRoFM6YHQTUrg4knxaBN1Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Unoq4j_LluTHnwUyK8unLKbMm2SAs8bD8jL2lfU667u-KfYwr6Ubdcq2I2F7glCcIwcpnhmFz9nYK639HYK_Fg0gCp8QicuncdoGtvDMLYkkHnAPmy8of83AyPg6VSMgNwPyVqN8mWfJXiAUz6j5H-Tb1VqU55whl0k7pvuNY4fipVEBM5YDHrxdkYTvXj0ajkwTrsXfZsmFOigRxzEWDP-UaLfYMAiW_DfviS7LXjqonH4AL6TY4Jm3CZKs_w3y3jKgTqU967ANq-QswQOET64U9yEW_bYirmCx3uJsxIr9f5moq3Ley2s-VCE6UKp2mYz9eLTkcs36UEGx4BrZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=ZNhQ9qbJfm-6zMVXPGPNA2qpWJ6qg9LU-1npg0qEg2dD7cN6hejPALRMCbZTcNvp8bIqig0pF6BoEceqYnK6SU79XIIACe8ilQTNLXHkcwx_tyCDkhH6fTIXWgujLt4dJFS1kYkwmWLBWfJNlVIB88VrDji4sMsa9U-zihkSRp7lqo6MOG8dUXyWjQACtukoDIWwOuXLz-rj0MlKWFJg83SOuvx26eGWM8sL1CFaUubW5lbUD7T49h4gaqyhXp0NEQyys2WlVFIiey6RnPzhovmtup2brKLMbzvud-Qucmp4_AkR-pe0-k5MONgeOeRar_06zpyBTGswFWpMAu0BHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=ZNhQ9qbJfm-6zMVXPGPNA2qpWJ6qg9LU-1npg0qEg2dD7cN6hejPALRMCbZTcNvp8bIqig0pF6BoEceqYnK6SU79XIIACe8ilQTNLXHkcwx_tyCDkhH6fTIXWgujLt4dJFS1kYkwmWLBWfJNlVIB88VrDji4sMsa9U-zihkSRp7lqo6MOG8dUXyWjQACtukoDIWwOuXLz-rj0MlKWFJg83SOuvx26eGWM8sL1CFaUubW5lbUD7T49h4gaqyhXp0NEQyys2WlVFIiey6RnPzhovmtup2brKLMbzvud-Qucmp4_AkR-pe0-k5MONgeOeRar_06zpyBTGswFWpMAu0BHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u25nrom1IJz0Bz5uuAkuPeoPx5hGmOMR1uB5-66yoIJa4RCSqLTboPh0Z5-B1ai-u1cQiZQmAdGeUycTOmmn-9X6cw_iK1WRRYcS0kB9IQv-u1eWQqO0X0GtpcCGdsQzN37ZPDXv-U58vobAj4_S7Al-C7btCf-DA5lf9Sxo-Xf-CMjX2XAM7sKjuUxr4tWh2yBokykLoLGOlgkCr2AiFg7o7sXE2fx9H3JIASXQhpUESwt_H9xzq3AUZUkZu2bNxuEyj9M12sVu-FxZ24trnuslXt9n15MXDIYELIwUBG6aXgutFS_BxBg7CriQIQv7tuOnLpGGysJ7K3fw8ZOiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG0up5ORAjLSYzO5QFn-hgGKcUY4PORYk4EL3dyRbVMVGbpxxhPCmMsZJAxDraHqu7ZWTsNpSpHu02xw10892ZZAROM2MIDs_YdavUfRz3OuLQNsQMnfPdINIYceuK-XaeL8tviFXmmS24X4EoJaOohyeOMG1zTcod72Sy5bnam_N7cRnUYgwaFA05rzQMX6i7DCi0eyzXULnOBF5-hDoE3cdHzOcNy955LWi1qDoO3uzlZMk2OBSCbNM-d8J-bEgefop_MbvdAbIpnGqlGNjEwznQGcPsz1ceKbUyvoroxrW6uE_V9QWzOptKgR6d8OD-TyUBgRBJSnlTpX3fW21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5312" target="_blank">📅 23:05 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5311" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5310" target="_blank">📅 22:22 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5309" target="_blank">📅 18:16 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5308" target="_blank">📅 17:16 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5307" target="_blank">📅 17:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQxDl9jv7Rx6C7FM5e1ZDn4ZQEoU5cVchIt_gmYXgXrVLl0Z6RFxLpE7DIT7jKdon6yXz-r8R_o3mhmRbibbbNTGFHd35ZqJaAD1g2h6FlJphWYOm4HJz_jt4hJ-qnEKyRIw8htIKv9n9cEXnIX5HuH4q-YZTu8EvBRmPYMBnmZrjnhEVotb1b328Kyhwc6B4uuF5MYfRv8tYio2ZN9jAj9vTlraiN7cwX26eZrb16FERRGiIEXNWS8yRhCx80Ak6Qb6SLWDOGfHseVuiqu33DG2mtbHQ6SVQvhbZnPyva9RZOhleNiWFOYZaMtJIB03jrnX2JCt6J_s8w6HAwIVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان دیروز توافق دولت لبنان و اسرائیل برای آتش‌بس رو رد کرد.
اسرائیل امروز دستور تخلیه ۹ شهرک و روستا در جنوب لبنان را صادر کرد و ساکنان آن در حال فرار هستند.
چرا اسرائیل با سایر مناطق لبنان کاری نداره؟ چرا با سنی‌ها و مسیحی‌ها کاری نداره؟
چون این گروه تروریستی فرقه‌ای‌ پول و سلاح از جمهوری اسلامی میگیره برای جنگ‌های بی‌پایان با اسرائیل.
عملا برای حزب‌الله و حامیانش، این یک نوع شغل و زندگی و هویت شده! تبدیل شده به هویت و شغل روزمزه‌شون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5306" target="_blank">📅 14:15 · 15 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5305" target="_blank">📅 13:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">« سد طالقان را یک شرکت چینی صفر تا صد ساخت، بعد به دروغ
به مردم گفتن که به دست مهندسان ایرانی ساخته شده .»</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5304" target="_blank">📅 09:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVDYaZf6T8ol7Dg14b2G9QexXqNYPSJZsoKm_rM9Mr7ahx9jqnbXnHKzecAugQAjjcxYwzu6juCOqFTA_hBpeo1MXYRzOkn9H5EDomYSGsv9ZtRp9Rz1s9RKrAMtCi1ntoeFj_aBaEOZSoyxaHj5L4t0XvE1Sav4PHMfCEs7J5f6FBNrWvC8RwfnnebJb7VUBagV095PMMQcOxyoYFKSLHzTD56DGHA8OxF21Zbp9Xtn7jHzR1qy2VT_iWTUpscC7-psIxXIDrV6AwIdRqXCactGkzjBrFTDr3i0jSAG_JpmPd6MYbgdKcW0CCp0qEfvQiznM2_uqxHXnOt_aG7gIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5303" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbW-Ifa4Q3V8IeBbFN5S7w8gxQPCITmnO0H3ZfqKpxUpjuExxNrjqrwP56dWv0qKaRCjxILWaa2MlW7SrzPbFBmr3YMCsRUohP5gtlwnGNL-GHFb5280wZSTq36Mf38t2xxvzpyMTFkfCygYw17f_0hmlCRQLMigHVNlPOPEpgyIWzaD2W_YCf_-oikIuUrSXFNREeo6bJxxdTpDBuRvAFRUMOgW9DdCKnuenSKYNhmzoSUAyvTzT1jMLuXwy-tOL0oAjLsg_MbnYLXO4KyZIheNpbSENjB89ILcbDeNgURdv0q32nVsUaouRpvTxh1EaJRapxr42LKPPsz_B7OdyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoSff1BLCpVfblTfbWsB12jjRpKA4l5iBFmBVGMg2YKZqT606ZeEFET1U3nHcq3hts6vbYyQM1L08ILDg7tYFWEgCmAy92XApDaCsbbIufjXQk_s2Jhs33B9UV11Wtv7R7J0rrWdovpObWyGf9K9SW-eDa__v_BrmbMpuA7je1UvicU7yoP1O4j6lvJLEaKpXLVdEEL7hzfjlv9Y0GIjeyKfIx3A6S0NS8v4tAivR8B8SvAixWgfApEsD_FsWDWkCck0vpvVjv5yh_AsyAxfY-iOTJ5D_fIz2nqIyXGMxc0JseFoICs90UEsFGxXCBqymcRH-n4qB7v9BjK0eiBVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی در ۵۶ سالگی درگذشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5301" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تصاویری از فرودگاه کویت
پس از حمله جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5300" target="_blank">📅 22:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdMDRXm7qZBMfjyJ0CzvWQkGhf-cIKRXnFAOhv1UWyc0D19kZnDc6XvZH_HCz6nelUpgooMAsEb6I_1JHthlbSgK0Ee7A-v8xxRk6JbOR2ymdxoJYiW4O3s0oaedXBt0SKrQnCO-JyWdvu9wWwqupWd0fe8PfggabtmCwygjuMYTn7pXDzy9vSgDWrCCQS7wl8N_7DC48dzm5YlMPnOVtzWJaeEQFet1nu6Kv6I5eVlHAZ8tJKJ-1vDOVGsn6pARkzy9gSjsCww-3rKzPu7yim-INE55k2sG0f7nxkuHQoYdojf4V3JKTm3ZmK5v6SPPklszG4I5hgX-y39aNI8izw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5299" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpVPR8_b7ygkXJC7NNzG8NX6aaO5kLrBcCHnEsfRo08Ie5eRK6kB-Vc3ElbvxwrPp9ZmmLwqjPymAO7xpM0cvt6qrXKb_J7qgG5pmmBPXYWOJP_clhpxJH3L1sN4PMBzLXiX0GMQHr_Piz4p1A3V5kkThzbIS5UmltdiADE3AfBhr7X9gtDnN31T_4uzq3OOlLBMrvGjbDKdolwsa0dWQMaNwm6cPfAeTq_JIl3AQR2PEe6dh7tBg4EPPYuwkLQrY9RI6WMcfYmYLRpI9fOK_sLZIOzeDltHw_RbJZEUTKsnGv0crOi203Lv9ftX1BrG6wAOYqpzercSWi4PG7-Dhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
کویت ضمن احضار کاردار جمهوری اسلامی، دو دیپلمات جمهوری اسلامی را به عنوان «عنصر نامطلوب» اعلام کرد و از آنها خواست تا ظرف ۲۴ ساعت خاک کویت را ترک کنند.
وزارت دفاع کویت: جمهوری اسلامی امروز ۱۷ پهپاد و ۱۳ موشک بالستیک به سمت کویت شلیک کرد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5298" target="_blank">📅 16:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=FB5g9AbkUyaPtTc9WESGY5EN1DzDeQiGkNR1y5U_K6XY0O2ezofqAyKVO6YmOG0zyMuFcr_-X2BHMMD6CCE6Tt98DU2rLEaM0Z1ls6tHv2K3NP63b-95nf5wJ9MSIbBlr-1J_Kj0_xy3sNWor5nuP4obhCiTTSUgOgPolEJOdNadJNOtX3UT-kUMXEMXe0hVw8oNMTqzL3Gt2Ss1OomW3xlTpERhjrxfYmxcFruXjghnPCwWm90-y8McjLr3DNGHl4UeCt-XVVliEqMfTy5vQLNUhH0OW-gbUBlb8ht7tkxkAzL1dVczVKDuRwKubz7KtDfsrRE5dR5j1t_caLpY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0b8905a2.mp4?token=FB5g9AbkUyaPtTc9WESGY5EN1DzDeQiGkNR1y5U_K6XY0O2ezofqAyKVO6YmOG0zyMuFcr_-X2BHMMD6CCE6Tt98DU2rLEaM0Z1ls6tHv2K3NP63b-95nf5wJ9MSIbBlr-1J_Kj0_xy3sNWor5nuP4obhCiTTSUgOgPolEJOdNadJNOtX3UT-kUMXEMXe0hVw8oNMTqzL3Gt2Ss1OomW3xlTpERhjrxfYmxcFruXjghnPCwWm90-y8McjLr3DNGHl4UeCt-XVVliEqMfTy5vQLNUhH0OW-gbUBlb8ht7tkxkAzL1dVczVKDuRwKubz7KtDfsrRE5dR5j1t_caLpY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«وطن کجاست؟  عقلا منطقا نجف»!
وطن‌ پرست‌هایی که وطن‌شون لبنان و غزه و عراقه
و میگن برای غزه و لبنان حاضرن ایران بمباران بشه!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5297" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کویت : در اثر حمله جمهوری اسلامی به فرودگاه بین‌المللی کویت ۶۳ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5296" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بخش بزرگی از انگیزه جمهوری اسلامی  در حملات پی‌ در پی به دوبی را باید در عقده حقارت جمهوری اسلامی جستجو کرد.  شهری که برای ده‌ها میلیون ایرانی  نماد پیشرفت و توسعه بود، که ظرف ۴۰ سال از هیچ به گوهری درخشان تبدیل شد،  و مردم ایران دائما دوبی  را با ایران  و…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5295" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5YuNKpNRu9qqtu7k65LG11lVVcuURRnMCml_dMtGKFGRBLDJ829uVqUWDERo0w906fsR7NoIkwlyI55AhatDSWjFrwzUCk0lSHA8aFMo_e9OCLg6PGqcvZW7vXZBGeamiXKmyNQCoaAmWOZqyYDrXnlED7njXUf2XtFbEKpszGQf7CMw2GlMkQ5l7G_CwUmP0GvwHYexfOoUEQptdcq_Q-tsaLKX4ppuMa5_z4WdDOJQuQmSTd7t0BRBV7o8FWYDhs9TxhwiOP19_2B4CqtZckejbIYS9Q0VADFwxsgRqi1nqt7Ov71Z8is1VBugXsNCAHkZdLR45RDcZABrrDj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAh2WdycMgb83QdyaSe-5xdQWq8B_ATNP-73A_YMxO3ohl6_YBW_XLW3avcECxrt4onCaWanOD-AEjvcOwiCDdm3ZEkM8TcvDLWgskFz2YdkmcE9ZmrcAD4qLDfDoZ1KblccjaY2p6RPMb_wwEWvCU47GmIL0Hxrj5EISB2jV6YvPoYYs_63lRPM8Kpzx9jUVujTKeusrEzl9SS8Cze7jA9NVYJZn734pFscjPgSVuUMn68hefqL-OYVz3mrwcw66Pp_DFmHl4lfxoQP2PkMYf-oh7EECBivRoyZoS8AVF8ejWHKIeBmL2YGi33FdJIIGlK4gq6ElwUGAhVxUSrixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n94XM_txSlNnFFqP6u66V-K6p5uKDOoUYFO6agGkpATtchtvjKi8WrcfVs7Z6bmA0dkCRnRdUvsLvHlRlU5umGalbq6Q4BO5f5ojvhPwmhhD5w4yQdHL3XJLfudDPdEkQCy2yhoNuodutOcD6YGIjutQSc0wVoE8ZA6WdqsYlyrMt0faRO8fQkF9KiLWcMvZZk24-BcX2c6HmGpNZofqfUTMXiPVDKMkeRhR_tMUfbW6K_9kDgV309uBsl_Ll8mAjIc5HYjYdEidhUQLKxImWxICjSVn9MXilcsmJi6TNn-w0WI0-10y1A3z2PPRNqoHc-8586nJb2BewSGGLjJfDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درست ۲ روز پیش کویت ترمینال شماره یک اش رو دوباره بازسازی و افتتاح کرده بود،
که جمهوری اسلامی دقیقا همین ترمینال رو دیشب با موشک زد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5292" target="_blank">📅 14:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=tm2jA_uoQgBwPiKfwE6D6IhMUXznclt8c5yDHn16ms2_jO0_HEZYiblQwY0z2JZFHe7FoVHiCw2o69JPN3cfvlJHEm0rlEKfkvm4y3g490PozM69-YAVRvwkSQe5bis6j3dP74XRlt2DP4zuGQ-5XbDgFv0A2UgQ9_MIfqfGQABK6zJchpwOoNXNkVQ6tP3_k37VVK1AiFe4MbYUyZHCSXSrds617JL3O9G2OCpzaJ2mawU7xjfsx78fmwFVPKRuub5vFXwqtZvOmAu0nM5jSDGtRIP5r68oZv-QljgdfQUVXDUCWOkqHDmwp2MUlQZwL0Mj-DpCKUta4u248g7l1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d4bd44367.mp4?token=tm2jA_uoQgBwPiKfwE6D6IhMUXznclt8c5yDHn16ms2_jO0_HEZYiblQwY0z2JZFHe7FoVHiCw2o69JPN3cfvlJHEm0rlEKfkvm4y3g490PozM69-YAVRvwkSQe5bis6j3dP74XRlt2DP4zuGQ-5XbDgFv0A2UgQ9_MIfqfGQABK6zJchpwOoNXNkVQ6tP3_k37VVK1AiFe4MbYUyZHCSXSrds617JL3O9G2OCpzaJ2mawU7xjfsx78fmwFVPKRuub5vFXwqtZvOmAu0nM5jSDGtRIP5r68oZv-QljgdfQUVXDUCWOkqHDmwp2MUlQZwL0Mj-DpCKUta4u248g7l1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5291" target="_blank">📅 12:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c026494834.mp4?token=mlRWZv5x9_xAG6I3LsSPIE1lxxdwk7rv_5Ce4XoDgV-54HXi_J-47ZvsYFuIZVOUoK6WEEUV6qKYGsgVpyF8LHg4NUQ0HcaRVcUD5BBLgbEyUQqhNO1nxjoLRhoU7umILK-B45VptSZn4BazZp8T7owKVZ8ZAjXgEO-ccspt7ob8HWIPOof4QaDGHjh2DYIxoil7ZlVvU8olIJYF82QXzrBeRRGXhgL7CFllbmrTMx5OAXuI9BijfocgHQObtvAblBOuzeKg_qnqyfBHg30vv8xRT6X_Ynw6l_HZYuLPyjdCGqinFKfaM4wOC9UT3HbIylVFPY5jbg57P-nWCxnHYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c026494834.mp4?token=mlRWZv5x9_xAG6I3LsSPIE1lxxdwk7rv_5Ce4XoDgV-54HXi_J-47ZvsYFuIZVOUoK6WEEUV6qKYGsgVpyF8LHg4NUQ0HcaRVcUD5BBLgbEyUQqhNO1nxjoLRhoU7umILK-B45VptSZn4BazZp8T7owKVZ8ZAjXgEO-ccspt7ob8HWIPOof4QaDGHjh2DYIxoil7ZlVvU8olIJYF82QXzrBeRRGXhgL7CFllbmrTMx5OAXuI9BijfocgHQObtvAblBOuzeKg_qnqyfBHg30vv8xRT6X_Ynw6l_HZYuLPyjdCGqinFKfaM4wOC9UT3HbIylVFPY5jbg57P-nWCxnHYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرودگاه کویت - شب گذشته - بعد از حمله جمهوری اسلامی
حالا اینها برگردن فرودگاهی در ایران رو بزنن میگن : «دیدید اینها مشکل‌شون با خود ایرانه و زیرساخت‌هامونه و نه حکومت؟ »</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5290" target="_blank">📅 12:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFRPuM8rriot8PVSh_sXKlJ7Wanb0pq-8zskqTu_mIoWnZJhSfpQKzCRezSx6Ha2Ru3976t6dZefCeQjOl5ZWbbmNUIIXSUKznKe01rMH_8wibmM72Z2ZCMyABO78lEOUXpfeTGquE5lsgoGOZwMA68W6yYU1vgCwirt6OaMmxd7mwcZ5J7ukG5VAS5C83h2w6G-1gs6br0o47p1O3HEBdkXqjZuoD3ZMXuRD5aN9PmKkGzc2iPHZzbp95iWPq6LGe-bCfmGY2Q63mfp8TUG0_FoKlpNYRkoxCXkL6I0xm4o5YsyHtHtfeOjgooMr2eqZ6634cnGTJ-2uWctuR1BpIHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e6c7c91.mp4?token=evZ7gwP2lYVX_oMXJzNlzEOGJe7__UV0L-8NRooEtz8yVT0sKDLc16Yd80sDw-fAv5B0dtrmHaykj1W5MYJp0uS-EFu123DJOa4OFOVQzYCsOv0ECnz2LSwPkI4I9KjwI9Nh36tePS0X89woKLZ2wOFAOLTcBKkEluXYrCsdHtWeBNGnKIGMfxyhurqGCv9xQEJK3Y8WhroPtQ2l7ogjJDd0LL8gHKFcZ8aVwq2Vn6wa_VwREHJXtjB8wiU-zz6Tb9E2y5DbvyaEJD_NLA538Osp5H-HF1_FQdb3BBT7uSlTEGDKEQ1xLk1bMyy3_5ubnzrOwvf73mgTj9NoEaZzFRPuM8rriot8PVSh_sXKlJ7Wanb0pq-8zskqTu_mIoWnZJhSfpQKzCRezSx6Ha2Ru3976t6dZefCeQjOl5ZWbbmNUIIXSUKznKe01rMH_8wibmM72Z2ZCMyABO78lEOUXpfeTGquE5lsgoGOZwMA68W6yYU1vgCwirt6OaMmxd7mwcZ5J7ukG5VAS5C83h2w6G-1gs6br0o47p1O3HEBdkXqjZuoD3ZMXuRD5aN9PmKkGzc2iPHZzbp95iWPq6LGe-bCfmGY2Q63mfp8TUG0_FoKlpNYRkoxCXkL6I0xm4o5YsyHtHtfeOjgooMr2eqZ6634cnGTJ-2uWctuR1BpIHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AadjavsfRyv-LBhoQCr6Y-7A1_eTRBdpJqCjs6LlmgGKtd6vaKsK9fguzdU-eEgiuBjedtLliv_edv1xsX3oVat4oWlh11NPaZQxUWHjbvCitLHoAbyuacZcVTPzk4tB0Sy13n2ECIDkaP-gpOsvQut5k5ricTT2ckvLbYeJjMFYYF0xi3bvnBUxRLB2TooM0v0d6kE_MAxvttmlNLm_FyXYFvB3J62c1pVDBh_F44ZC-USb76HI7QeVCzUb0Jtu8fdXrwfd5O4Mcrhj0u-_0u-yape7Y2g5PDFHLp-l6FOJ6smBaPsKrvFTOO_hBNvG7ClbXwlU6V67-IjVpSxzEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFUDdUU1g0TRaVEyihdih6AJyrxE8QHVXFDLSEMhVBkoy5ZiSx8ow4wkIq9SH6LBZki6gPTC8vciXKNaD1VmVbp5oIpoNavgrzgLypyunA-1eFVKXG0qyIU7Gte3SeqP79hO-LmC56SRDU1zbKaAKfvHNsxyS1SanZhLfI5PLDWRriqs-P-2PYCcKlHHfgfsOxUjv8PdY8qnrHHwu4fO7wcyiDR5R36Y9ApUudS1bkFRigHpWJ-v9wXJFH0oqWOVjpT1CB-qU-PlDhaw0N8GazzQJD_19Ahtq9lhybW31s1uUws4ay1tUhloMy63OPdRY5Zqak-18cQ05DKxKtDKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015500535c.mp4?token=hAF2lfheAhcIg9j1vxVYBL7dk9x3tBzYJyUMhZsMDto1sBZMeVTI0vaIlCfISJ7lsjpyDl1-58lqucLnhkNDJkgcIFUZeWtTGBNt3n28j_KEoWnaAuAtMIAy-jlYWcJ_y1E-yTZvKuDB4uGcUdOW_PtWXfKadgyJcueT8KNcvAhqiEQhvoyOOZBUwazteOyr1q5TFpvG8Vf5QS6q0d2cuFzAWxJoOu0Js8u6QUgo22DWuRiCRCSMsN5uyu9lT-jn8tqjaeIsHO7cOe1h9y-no5vs1t60AhvALSwP6hO5TUoJvZfWuiL3fBKuMCEXse3yX05Sd5KLAM-XLWhZ8_dJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015500535c.mp4?token=hAF2lfheAhcIg9j1vxVYBL7dk9x3tBzYJyUMhZsMDto1sBZMeVTI0vaIlCfISJ7lsjpyDl1-58lqucLnhkNDJkgcIFUZeWtTGBNt3n28j_KEoWnaAuAtMIAy-jlYWcJ_y1E-yTZvKuDB4uGcUdOW_PtWXfKadgyJcueT8KNcvAhqiEQhvoyOOZBUwazteOyr1q5TFpvG8Vf5QS6q0d2cuFzAWxJoOu0Js8u6QUgo22DWuRiCRCSMsN5uyu9lT-jn8tqjaeIsHO7cOe1h9y-no5vs1t60AhvALSwP6hO5TUoJvZfWuiL3fBKuMCEXse3yX05Sd5KLAM-XLWhZ8_dJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5286" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5285">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وارونه گویی!
به خاطر دشمنی با اسرائیل رفتن دور تا دور اسرائیل گروه‌های مسلح ایجاد کردن، پول و سلاح دادن، حماس، جنبش جهاد اسلامی، حزب‌الله و… تا دائم با اسرائیل در جنگ باشن، خود خامنه‌ای بارها تهدید کرد و گفت «کرانه باختری» رو هم مسلح میکنیم علیه اسرائیل!
حالا که اونها برگشتن حمله کردن، میگن ما اونها رو برای دفاع ساخته بودیم که بهمون حمله نکنن!!
نه خیر! ساخته بودید که حمله کنید! نه دفاع! که هم اونها رو زدن، هم اومدن سراغ خودتون!
و الا اسرائیل زمان حکومت شاه، با ایران دشمنی نداشت! جنگی با ایران نداشت!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5285" target="_blank">📅 10:25 · 13 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7IHtvvEIPVVJaYZD45Kyl_-Lc6nerpYahjoPSjkK6zlb70QIudYHxeMFNdnU2wPB4X9fRufsqz0Gk8kUTzhEjoudVPC7bQvqyH2B-jEkO8C8si0S9EWOKenyjkkWrglMl2h5M372fXQ59RAHVRTdQ4uj7wQ1r7gP4QhoenA8vV4zd1uZ4KFYiGjq-MgXTg0NUGokbcTNprCuJQe0dTeKUXCKH64hjraghVamU4RMNW1HkCuaj0incwLbjxmmDhsuyod4ArnnmFqA0Bu3qog2exLcsF3FLuHDwnIP198rxaXpphS9MZbFzh21nGIaCuBzCigqqpE_EnhvePVYzqixg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5279" target="_blank">📅 02:47 · 13 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=N629AvhIcd5mIZGXuDTKCHAR98YjudDlvtZ6RUtbGkfxSRWtbmlqE5txGNoAZiTJf8nCAlJzhRUVlRLQ4Awnbc3WECQAPqkLTbLlO_IB3YWDtMjCTHEBk8Xtc8XY1UOH8VvHogqT9EamV4z9koU3wBks7T0xMLF9HHqJX3Zrxjee4FdC1-Qo4RHCYuLr3HHnbI59se4SfH8ISEBb63VdaOlvHx9WZXen1WrbSkU_Rl7LhKOIP6YapHTBMioiqTCKwD9Cpe1tRUfom7FkM0J0lfq2qoZbykPIlR_f99jX8B9ve8tdgTgrRjGDXE0MVasmURWGscdDXwSU1LxrwgJxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767a4036f8.mp4?token=N629AvhIcd5mIZGXuDTKCHAR98YjudDlvtZ6RUtbGkfxSRWtbmlqE5txGNoAZiTJf8nCAlJzhRUVlRLQ4Awnbc3WECQAPqkLTbLlO_IB3YWDtMjCTHEBk8Xtc8XY1UOH8VvHogqT9EamV4z9koU3wBks7T0xMLF9HHqJX3Zrxjee4FdC1-Qo4RHCYuLr3HHnbI59se4SfH8ISEBb63VdaOlvHx9WZXen1WrbSkU_Rl7LhKOIP6YapHTBMioiqTCKwD9Cpe1tRUfom7FkM0J0lfq2qoZbykPIlR_f99jX8B9ve8tdgTgrRjGDXE0MVasmURWGscdDXwSU1LxrwgJxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5276" target="_blank">📅 01:42 · 13 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5273" target="_blank">📅 01:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=iPukVqeeCT522nj69icAerSQR9tXwspojAq2-xs9r4gbRqet3gm6symwVj3LrqC_0OIzGMDgjvx5A9UVaMMGcHk_NBJQbQRpvEFBILT5E1hn-B_HqXKGeA6exqS67m_tEghn-w_HhZz2B-RBdGIJNnTScLvVUPqwhfJXHlRogOzCM9D3sgYE3fjk17OxTlNPES_Tz-GPVVrAYYi5QS0MdsN2DbrTproM7X5LXg9VRVkwH8rJV8MHBWuSLhKJRnDNx6wakz0-J6KbzFtzMCy3JVePMom5vDnBqppyM8lkQht5cQHaMyQ2oxr4sTkCGQcTy_p1KhocmqPk5ioQrVrxLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42bee8bd9.mp4?token=iPukVqeeCT522nj69icAerSQR9tXwspojAq2-xs9r4gbRqet3gm6symwVj3LrqC_0OIzGMDgjvx5A9UVaMMGcHk_NBJQbQRpvEFBILT5E1hn-B_HqXKGeA6exqS67m_tEghn-w_HhZz2B-RBdGIJNnTScLvVUPqwhfJXHlRogOzCM9D3sgYE3fjk17OxTlNPES_Tz-GPVVrAYYi5QS0MdsN2DbrTproM7X5LXg9VRVkwH8rJV8MHBWuSLhKJRnDNx6wakz0-J6KbzFtzMCy3JVePMom5vDnBqppyM8lkQht5cQHaMyQ2oxr4sTkCGQcTy_p1KhocmqPk5ioQrVrxLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد عمرانی</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5272" target="_blank">📅 23:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به درخواست فرانسه، امروز شورای امنیت سازمان ملل نشستی اضطراری در خصوص وضعیت لبنان برگزار خواهد کرد.  پایان این نشست قطعا چیزی در حد صدور یک بیانیه خواهد بود و یک محکومیت، هیچی نخواهد شد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5271" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=HvIpFBkinCnSCcmxAhOueb4oRYBKL1Pb7weY9Avx3EJQwnsqp7QjJGM7yyngMxKfD1Sdipvx3-LDyYwSIkNtoYWLYrfJbGYDt2Rcv1qnJgTPipSDMiLEQ1XQCRFMtMhSrS0wWmm9fNjL-84ZTKa6y9HWgUOP1iU2TLpeD7KfDVXxaADOG7LSFiQup-LysvHom7aMuHfHpuPQvay_EU_mdjjF_zlLrJpyfe6I7bWXMMMKp5ZvdKrDD4xXxPhi12YJCl8o8jwo6CU6_QlMQ47f64fxnZiiJ6RUbB_jEmHODYXjG1ed2sQR3QDeKNGxsNS2rVdHIk6cLwUZZf1Z3CwA7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52501c2e8.mp4?token=HvIpFBkinCnSCcmxAhOueb4oRYBKL1Pb7weY9Avx3EJQwnsqp7QjJGM7yyngMxKfD1Sdipvx3-LDyYwSIkNtoYWLYrfJbGYDt2Rcv1qnJgTPipSDMiLEQ1XQCRFMtMhSrS0wWmm9fNjL-84ZTKa6y9HWgUOP1iU2TLpeD7KfDVXxaADOG7LSFiQup-LysvHom7aMuHfHpuPQvay_EU_mdjjF_zlLrJpyfe6I7bWXMMMKp5ZvdKrDD4xXxPhi12YJCl8o8jwo6CU6_QlMQ47f64fxnZiiJ6RUbB_jEmHODYXjG1ed2sQR3QDeKNGxsNS2rVdHIk6cLwUZZf1Z3CwA7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی تازه منتشر شده از ۱۹ دیماه - کرمانشاه
و تیراندازی به سمت مردم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5270" target="_blank">📅 18:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=inDOzpPyyVRvmtND692zKEyKnmhiz2NQwtCsSV-B7Jp2cd4vVr6pVnFENGqV7AzfPKogRoeqjdRWTbGW1RZdLTYV4WFfNx3V-S5VhnMmxe5bx6_meU40BXke3sG-jBIxe-s5dyMdnUXvSXWF4A4t4we0QEDKrO2QTdKMpePF-ytdrGv7HmqSZXBoqBvtrXtaA2R2TX1QiZvdycp8QXsgU3YjAAjr6EZUKzlCwrzB7eeR9tfqmTZrqwB2p6U6OpyZ3bK7O_itrPXo4mRiyL6f3jTD6DrtGbsoZMRXQ4N2tEML3pd_lt80KLUTf3X-SjefdL3X7rNLlKVhTScvHjvtAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1239a4e0f4.mp4?token=inDOzpPyyVRvmtND692zKEyKnmhiz2NQwtCsSV-B7Jp2cd4vVr6pVnFENGqV7AzfPKogRoeqjdRWTbGW1RZdLTYV4WFfNx3V-S5VhnMmxe5bx6_meU40BXke3sG-jBIxe-s5dyMdnUXvSXWF4A4t4we0QEDKrO2QTdKMpePF-ytdrGv7HmqSZXBoqBvtrXtaA2R2TX1QiZvdycp8QXsgU3YjAAjr6EZUKzlCwrzB7eeR9tfqmTZrqwB2p6U6OpyZ3bK7O_itrPXo4mRiyL6f3jTD6DrtGbsoZMRXQ4N2tEML3pd_lt80KLUTf3X-SjefdL3X7rNLlKVhTScvHjvtAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVj2_PaM3yT2I1Pxd_j8C6vTdVeZxXRE5glCXAgH7W_EEHXJyYDW8zVE7uH8TkDOEcw9DkXsWJKr9UTvRMoRo1_QCHkPnYHi18ghOi8Auvra5zABKNuRbgZ-unAMx6drI7zbfhzRk-86qVp8C1kVZVl6kGlvnzN6EoJjCnjObOcFeM9f9k909Vdl7tfkf0yIp-wtizEmtJaVgq6O5vycw7mNx7ax1PG_Y6lOVGbVycoc9QL6UujawmMdvCMelExujm2SEVRse61cR5nu5CMxu6aVACgMkZELJKNZ1ksg8CJzVqo0gMoYqVF7N1Qr6A0YMQPAz6BLu8Jishy2nYu9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سال بعد، در جریان جنگ ۶ روزه شرق بیت‌المقدس این بار افتاد دست اسرائیل!  ۳۰ تا مسجد اونجا بود!  حتی یکی از اونها هم خراب نشد!  همین امروز ۳۶۵ هزار مسلمان در بخش شرقی بیت المقدس زندگی میکنن!  در حالی که بخش شرقی بیت المقدس تا افتاد به دست مسلمین اجازه زندگی…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5267" target="_blank">📅 16:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6rolnWt__EcuDWBgMZDbjbhltsgPl-x-fc5vEKDPynS1JRCPq8uvQtsg-IaZWfCdoi2fdIUCaXoU-rgCFbSyGbj2cNGJ0EOi6W-Bp3XMCeaUV-_ydlxL36CP-IB1VevOfmTw6bA0cFG4sIcgVoYYrKmBX7J4X3p-zkvEpFek9hv8AHCVOYDxf4kVDC9eLfy7HBAQVHjgL1rgg0_GlaQnM8zBLrf1OaE4PRWWj0-9rP1eUxxV5JLQZAgT9VZbBDxhAkCaskhM1yLWnTNZeky9Kmo1zpJ2Tj1zQZCpvHJwQzvU8jtA_28lC0KQW4Fbo3cAirvFtZCd5VfHmZFuKLFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال ۱۹۴۷ در جریان جنگ اعراب و اسرائیل،  وقتی اردن کنترل بخش شرقی بیت‌المقدس رو به دست گرفت، دست به اخراج «همه یهودیان» ساکن در این منطقه زد.  منطقه‌ای که حداقل ۳ هزار سال یهودی نشین بود!  یعنی از زمان هخامنشینیان این بخش  یهودی نشین بود! و ربطی به اسرائیل…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5266" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reLI0fDSIWCn3vWHu7e3Ilx_toNJcxWxDA8F-ad3eWrMIhsz6RfeksYtpwbh5Pq2j2CoJxNWLUBt82Lr6e6XRTA1BdUHHcmVEoTMsBOzY2gvRFn3elX6LTb_OItux3go58CReTsiMPJJNkDhYZKZaUw7YWNovGi5IqyxP8A9YUaQ-iCKCk6KE9MmQo342ybgP6Tlvxr65TE04F1hH9IAxLAFtO8cD_WUmHzryEr8CrgyWaigHCESzS036K91I5yDKCfQbCGA2JFWt9llMaXmUWYGElakdF5GJbHrBXET8zKhgK1xRk7RI9offRI8pW6s4gIpj1EMUwxJNTHGwBXFdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVjoPOnXCYyU68f8Yh5UY9qrnWNp4eKinrLdQfDBnm5yfrNbsy9DXQF2RW3qy3QsJVG30qeevNPIN4DOrWTZV9T1r70X2gEna2_U0CkM4mqlsyNH0lEcHQvj79Qk2CKmw9EYXJBGRZF9R7dn_Md7UzC0qvgXYyHLFTtji7YkqH_Wj-xdbgbYi06bpUsxcgkCCaQhhQUdA3WPilwu3q_tsm3znXn9TnCI3-LrO12PG8kd85N-jPkG5gWlztHWCAPZv-LKSAF4uBnpb2RGBZnGg9iWqMC3-Ri4q267RMgvMPurzgIqNZjD-_R9cL7qSWd_TT_QJOS_2FhB-wij4-mnOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرهایی چون «ازمیر» و «طرابوزان» و…..  کلا مسیحی بودن. طوری که ترکهای مسلمان بهش میگفتن  «ازمیر کافر»! جمعیت ازمیر، که یونانی بودن از جمعیت آتن! پایتخت یونان بیشتر بود!  مردم همه این شهرها رو بیرون ریختن و یا اخراج کردن از خونه‌هاشون و فرار کردن  یا اینکه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5264" target="_blank">📅 15:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h35lVYJi-qpr15b4XeHAaF66Jh9lHxArbyf-vb6rQNxHdSQEnyJsGtxTWH_aII9LoIjUVT5PrmMJ5Ci8xOtFaMyv00bwwg0XyITPZSHFP7ItcBpW0vPp80KysWuvWXTFLav64f2UCB1HH78md_uKcInxCkqW0Ls7uZ6v-uyd_8i063Gw42h0GQxD0xukx3bdsMG0HlzY5UIbLvPDcnO0a2tf_BhJUkA70uRBGMzmE0OdU7A3hDjisBzLe3X99ifVjc2jVRNate0iuXNDcl4VEZ7lvZ4N3IWSjDQ-AusZN3cm_8MteqkUSJkPQ0DCAlKpll1d1X-MjuFrZIXQQP2xPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر این بنای باشکوه و عظیم،  کلیسای «ایا صوفیا» (صوفیای مقدس)  از عمر پیدایش اسلام بیشتره! ۱۵۰۰ ساله است!  همچنان باشکوه سرپا!   با وجود اسکان گسترده مسلمانان در این شهر، این شهر تا همین حوالی ۱۰۰ سال پیش (تا ۱۹۲۰) نیمی از جمعیت آن مسیحی بود،  ارمنی و یونانی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5263" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3JjiITi8iZg1fs92QDsSMSVw9yz-hCMVbyBnD88eMEDzWtEpa2aqb1PWUE83lt9vOmjqZD_vAOuL9BTdBE-FJKZGXycNdDjzH-5W71ot3aKj8GJJooJ_Wq65dludcJSuY4bz7vrtz---Khap1dGdFyHDIS8973cYac-zeFr7aKU6YKxx4Ctvhv2LYZFBSk8yGr5SGHjWem3EI5RcvyC5o5xLBZRumq2wW6ir1_IwdJw5azZ38dTSvhxC9IQClKJphFcYBO6mtFG9nKiqJiY_jXE098dHdSZN9xoQwnWP8Mxubg_em4PZpylfVCeNMw1w3jN2EPPlh43gkjlU-c20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول برای ۱۲۰۰ سال یک شهر مسیحی بود،  برای حدود ۹۰۰ سال در برابر حملات مسلمانان مقاومت کرد و تمدن رومی - مسیحی - یونانی‌اش رو ادامه داد.  تا اینکه «سلطان محمد فاتح» استانبول رو تصرف کرد از اولین دستورهایی که سلطان محمد فاتح (لقب فاتح، که اسم یک محله در…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5262" target="_blank">📅 15:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7TRx2iT5SmSy0X6aWyycpERuYpMXD0VsSoEF3dBK2Aks_8czEj9H7YlUBDkr-wCjhvn76U7sYaGs6Gxmj0XvDfOdsC8XNUof8Mpuq1ALMibaGaqU7wskrv-C--1NT4tgxn687TNwycT_cG0ZoqB_Hiu473J98Z8x3AY_pl9Q_lqm6-2GznizZBYrn-QSDZJozNIYETozX-A12dZDzZvB2VUwGGBhMW3SoF5Hpbp253YKJtalzS6ln9Nn2vnAzkO52KZj5q8wnozvmTRNWZC86mCH8FLt_VocMxoC8j8EGTmQTpR0HGnahAsU2m10uBu8_h1KphVhTLS9DrzhekMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان میگه :  «استانبول  تا قیامت یک شهر ترک  و مسلمان باقی خواهد ماند ! » به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5261" target="_blank">📅 15:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=E5de9vrY7kH8zbng8hAmm6-LBSJPju_2o_izb2rJxEfbLQXyO4no1RYCZAk3zHk4dF8TsDfh1uqib9_zI4iFH1RgPTs3KgqqCgQzdHefDqEnSE2Vu8f7GQUZRBsLNdSr5_DvHngP8RaAFJffMTN_VQpJUE_08aU-0DFnlmmQoF7fy_MKmw4p-pgDA1aPyNuciyp1echl3ubGJGw_UU6AyEMQH-NlIHUbbn9K0oRCGRii4JKWNz_t_9Fetm8IyaQE3wa2YZprwJwF_A0gz3sCBBdzBYMSa8jpffjFXOknRVzClQ5-VInqAkvbEp4Bao8kpM6X-N4ANhPKSDwSynDBJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64175a1cdd.mp4?token=E5de9vrY7kH8zbng8hAmm6-LBSJPju_2o_izb2rJxEfbLQXyO4no1RYCZAk3zHk4dF8TsDfh1uqib9_zI4iFH1RgPTs3KgqqCgQzdHefDqEnSE2Vu8f7GQUZRBsLNdSr5_DvHngP8RaAFJffMTN_VQpJUE_08aU-0DFnlmmQoF7fy_MKmw4p-pgDA1aPyNuciyp1echl3ubGJGw_UU6AyEMQH-NlIHUbbn9K0oRCGRii4JKWNz_t_9Fetm8IyaQE3wa2YZprwJwF_A0gz3sCBBdzBYMSa8jpffjFXOknRVzClQ5-VInqAkvbEp4Bao8kpM6X-N4ANhPKSDwSynDBJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان میگه :
«استانبول  تا قیامت یک شهر ترک
و مسلمان باقی خواهد ماند ! »
به نظرتون چرا اردوغان باید چنین حرفی رو بزنه؟ در خصوص یک شهری که ۱۷ میلیون نفر جمعیت داره؟ ۹۹٪  مسلمان!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5260" target="_blank">📅 15:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GChyj6E1pkZy8OKPNfRvMtNS0VL3thIDWsniVNRkDLGvOLIzP88tv3NGgnxFR5_bHrkxpbSVrhMoJwgzVbhY-hJv6aWTuK9rYZIHDb9gootARz1XdmYrGh2uAj2SZRhCEYOTEufoNPo8Coo8xik8QtX24p79yDke-NdpUXxCB3x5gYcQcc1tp8ptYxV73kIQV66IKH7jeTp0BT97mbV8WGdbTwaL8VOoPVGLuryPYfOxFSIZeL2Iq8IXzXnGpATegK6ePHratthCVf-0oQ2Qt-BZfsTkbng5oxkPmZORngMn-FfL5rAz3nhWJIFKAlUkAGZBrHyBz-HwTKy6Js644A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،  خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!  در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان  رو پذیرفتن،  اما «خسرو پناه»! مخالفت کرده…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5259" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/reGTE2Tnga_T_3slt34HWQu1uPInkZ1e8dhzFbyPACJOXBr_Rb9Mgrur54stZC-TzmPbsVqBySZ20-zZSv_5SWHn6qx3K7vvS1KncJjlK9kJhLVfWJQyfjNcMHsEO2r5Yo6GQVL6tlJ7fl1CyubzPzGju7Zoxr-3CIzZ1QpfoMstC8kisvibC1HX5PlSP8PBdyi8MS5ucLFYQbVIpsZr2flDdnS35kqJ-ovJw83FBpBC8bvuQjotzFMYSt3II1WwWV-JEb82iptEU9ftBve1TLUd40T1NdpgNNwZrfzjBhvNksvUjMhqeAB1i9AzdyUqk1LVEFC2w3CUPq24aJQjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGWBE5JgTiDiRa6KJ7GtHbgrYlmMkIvYXQEMSSLWr0J7qxiZ0fugSFVztGIcXCcENkmtJHvAfw37OsDJSjEyd85uYRvB_HFkmFFDzkUOJdFpcAsIbGTMd1dLeumtEfskQINj6qE043JEcN6YrQgt78-M0g9BDJF4K7dRASU3mBlCpZZykumYkOUrpjUGj8mefHH_ItYqZM3CY-I6Z3bp064kyPRvBNxsfcLr58sQvcinbd_2eHRQFP8svOFfG7OZLPM5X3LbtJQpWxR-Mx8WnIxUsPgkr67y66p7WBMgSHI1FKFQhzrdtZe4M7X3BTtMPndskpmb_JvkMaMum5Ed9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احتمالا شنیدید امروز در تهران و چند شهر دانش‌آموزان تجمع داشتن،
خیلی خلاصه میخوام یک نکته رو خدمتتون بگم بیاد دستتون جمهوری اسلامی چه موجودیه!
در حالی که رئیس جمهور و وزیر آموزش و‌ پرورش به نوعی درخواست دانش آموزان
رو پذیرفتن،
اما «خسرو پناه»! مخالفت کرده و همه چی قفل شده!
خسرو پناه کیه؟ دبیر شورای عالی انقلاب فرهنگی
که توسط خامنه‌ای انتخاب شده و نهاد به قول خودشون انقلابی است! و قدرت و نفوذش در مدارس و دانشگاه و….. از رئیس جمهور و وزرای آموزش و پرورش و آموزش عالی بالاتره!!!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5257" target="_blank">📅 13:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX_8yaZJMVScBc9J4wnhgTi8fH4yp8uBdsGKgKTGdYmriPSHxFQmec36q_YIRADEj9TKlx4E3ulsrtGCjUKp3DaF6YPBqUd9Rf6GQTeeI4Jj8eOLkkUZiCyncotTvjeViUa2qivYaftAyvZ_vhJN9m0LQue9AEZgqUkyOW-hd2JWycJFANnmchPaYKLOyW29tRQvD--PJwyHNqydpwtIdpoeXRdLDfRDipw7miMdsrYPKLNgkXoJQeXJArO4umzeB6A2idSKfpvqpN0M8u6COR4hs_wzGy-FqFtx_071t704z5NDhuVQdQ2UXwH6i6ldcbYjnWzXsAkORb09s7NGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئوی این گزارش به تاریخ  یکشنبه۲۱ دیماه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5256" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FskPYOLqUxGYHO35p7vELLeC8kPXfmZrUBkNbXyEOJ7Q65b2ysk9axxeNQEtns1XsuVR_SNS3sbYZsQezGKQL1oqUNudZlsarl-6ejzkDr6R6OqcdAPri05P2zthHltxnQOte5hZ2YnLrMP8vVQObNbfkSdsey4eV_lpw7hMOQLMZHYiQJaVB-LSTLljo3LPBglmeiDhaeJWEir18aAGC68UlCqAJuDXKh98Rhqj3hd5DmZYATl9RzZKZ1E5gbPNMR8CCslJCyw-hVERieQk5hB48E1A-cqrvXzGnoby6l6xsWbq3pH32kwnH95Hjmo0BnLSuJNb_jp3joJrD2ABWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiusjyrSCmQwBPVQvWr8prtJJpFtJKVVBlFTi4px-nLaqF2NbY-TwTZkm6AsFxFBpzzehsCAz7pd8gj832qpYRg--8O1g68z8hMt1MrodE6yvkJrgOoePdMTpxGcOx6U-wrLGnkg4-c5t-fmlVcEBMJ2PrNxGP8nIamSeyiVM5WZq-EtdmkPv9GJX_lefJPl_GqwstAfWw0KRQ9A_zGv0PEWXnE0MExKwwY6AxoRyritnBCRrM7oTrZn_Wls9nVz7-fIEde-OP4oOOKSUt2BbUT1v_TLsgtKCOh6u-sGIP7N47uyKaEh4YYb_r5hTE3_i-EAS7wrf8ThoVGrxpWQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHATdRPk1v0d2bOCQK5znSrRJex8biLg_70PO-Cv7q9MnCv-riXZ7ijNBMJ-0kFgPMKTzTIj0E6qaqv1r_xnzgzGpTWEMcGy4G0cYlu3q4Fxgz7mantKak71BOJTkXX3aketDAsG4CWyk2LI0QmeCNrLhcuZ8IOXpod89A02RRYm7dBpoF3d9xvIkoSOWl-B6n3i-r6Sp3LduMDZdluAGEzQF9sVvuh3ABA7EQ_GH9BtwOBWf47OPO8hj9nZHQcj3ueV_nFYaQQuok45ZE3HsgryzJetGUxCGHITbjo9J7rUp5teXBHwxDBHTcNrjsz0GvtBQxtwOQL84azpS-qwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sESHKSjD8Twr0IHLVTlRT2gysVQTWO5hMSSEbOcrGhx8keeOcqNyhTqBWSQfmeEM8I8pk_NMkpN5jb9SodXYdhf-GB-cAI7UyFvkEHY9i7E2-wuNVZq8gnIE_Zf1wVVdJDb3a8q5hIAd2LmxDzoFWLQh8KO2vTbiMQ2SAvQzLAWNa5Kx0qpIA9CoNc0br00ZzM2MwpvAkoqAmOQPA90mXb0UTqrVeL5tLrKx-P2HhVghgnd0cMI669oHc0Edtg8hIeZpQZNFxm-pz-LDYCWryKZ-oKi6nQeDZw-9w6G0NyPOh3ob-xag2Axod67NWNh1kNGn8pKUlE4B8xCqKqKQsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/25938e5740.mp4?token=aC4JecH0wMBTfjgPtcLZ3R2sAguR31VZZplBsmyphQW25POLpTBDJMjM53n3900FbTYGknigzfifuJHhIIy2lCy-cRlLeMjkO8bdAHr1IcNBl68Cb18Wx7sUUhUpFlgsJ54AXM-z0DFtsmIrStA01vCsIjRMHZO62vdnVBlYymgDTNJfZ8m1OnXHsTOqVDsJjk_6szbSeSOvdysHpSsBznBDvIl11Ll5E44U4TbUZalVu4lTu2WUV6Magu26UuePgc4r45riyrUB8tkIfeGJc-XkYI3AFjoBv6N1uhx99t5qvq34MAcarPLZEKO9qy-zzieBs_jBQAWh_W7l5bMlcAsoQvZ339TD3W_Ok_a8azBMkIB1yitJy7bgp0SlUMWXlQK-Xypz8FABsP1a_Rag0roky4yPkfuy6ileoOaF5lYuDGPdnRgoXv0yhbxOJTRY_HyAzWmP2SESxakMuQyMzTS7Eb3MhtjtwoxV8V7cIc_Qq72vB1A4Z6t6S1Am2nklrxp42cSrW2MrsS8OnOZd6rGDLdfW5fkj8_IwOG7TPQnf8e22wIfmjvmFqrZolTaVlUkWovZyaw6g3s4hGbNyW5CeN93lGkVG77YRJBCO2zxZAnKG1Ujm3O0nOhLMeALnEzCtCS15GbV8GBoD0yZDQdh-NeQ8IJqBoKcTS_yipQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25938e5740.mp4?token=aC4JecH0wMBTfjgPtcLZ3R2sAguR31VZZplBsmyphQW25POLpTBDJMjM53n3900FbTYGknigzfifuJHhIIy2lCy-cRlLeMjkO8bdAHr1IcNBl68Cb18Wx7sUUhUpFlgsJ54AXM-z0DFtsmIrStA01vCsIjRMHZO62vdnVBlYymgDTNJfZ8m1OnXHsTOqVDsJjk_6szbSeSOvdysHpSsBznBDvIl11Ll5E44U4TbUZalVu4lTu2WUV6Magu26UuePgc4r45riyrUB8tkIfeGJc-XkYI3AFjoBv6N1uhx99t5qvq34MAcarPLZEKO9qy-zzieBs_jBQAWh_W7l5bMlcAsoQvZ339TD3W_Ok_a8azBMkIB1yitJy7bgp0SlUMWXlQK-Xypz8FABsP1a_Rag0roky4yPkfuy6ileoOaF5lYuDGPdnRgoXv0yhbxOJTRY_HyAzWmP2SESxakMuQyMzTS7Eb3MhtjtwoxV8V7cIc_Qq72vB1A4Z6t6S1Am2nklrxp42cSrW2MrsS8OnOZd6rGDLdfW5fkj8_IwOG7TPQnf8e22wIfmjvmFqrZolTaVlUkWovZyaw6g3s4hGbNyW5CeN93lGkVG77YRJBCO2zxZAnKG1Ujm3O0nOhLMeALnEzCtCS15GbV8GBoD0yZDQdh-NeQ8IJqBoKcTS_yipQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداد عادل پدر زن مجتبی از فعل گذشته برای مجتبی خامنه‌ای  استفاده میکنه.  مجری : رهبر جدیدمون آیت الله آقا سید فلان!  حداد عادل :  ایشون از آقا سختگیرتر «بود» !</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5251" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1710c62683.mp4?token=J-UeTR43wubCg5yZqxee9MyupMlOsC_ybVUZ9K1Af_tdvb4fhM9-efBUDNE0umOjEvByqjc_bAyp5vn8kgtQTforw2O63Q-CgDcG7Zzozfre1gu5EvLPpbI01GZmgObhNCm89X5rq9bhFJTx2v6Z8hpGl6hFMigZiXKUHFZTHeVc19uvCfqBOZbytJc-p22YrAQr2qEm2IO4y84w5SNsGdz5mbUUjgECj8PpNdiRbtTKrcyiQ_Be2oKKab6QlupEIWwvcmXhYD4ShtjYzRp5oodjLhm2JVk86sL5xEzN6Pgsw8CLGK8aa0oSxWEpIk52Tpf3iQFIdkpMi_K8gEn3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1710c62683.mp4?token=J-UeTR43wubCg5yZqxee9MyupMlOsC_ybVUZ9K1Af_tdvb4fhM9-efBUDNE0umOjEvByqjc_bAyp5vn8kgtQTforw2O63Q-CgDcG7Zzozfre1gu5EvLPpbI01GZmgObhNCm89X5rq9bhFJTx2v6Z8hpGl6hFMigZiXKUHFZTHeVc19uvCfqBOZbytJc-p22YrAQr2qEm2IO4y84w5SNsGdz5mbUUjgECj8PpNdiRbtTKrcyiQ_Be2oKKab6QlupEIWwvcmXhYD4ShtjYzRp5oodjLhm2JVk86sL5xEzN6Pgsw8CLGK8aa0oSxWEpIk52Tpf3iQFIdkpMi_K8gEn3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZoPFpLBqssXwSzG8EIz6bLPjwmwhp9KNo-XZ5mXWNiq80xNw_LaKTm6ed64VTpM5dSunZd69BDoUMhy_tUaQsLBCxBVRarccA2q4DwFVaofeUPmYxN5LuMMa_ff8gIpucTF0ms2qtGwuhi6dsiIU8d5FBGoYH4hXy_2uHscO1sBvGsbyw7rGUSlfAro-T3NqIHTUnjUqTaS-i4Jjrggo5NgEwRITo_BT5aGOEFvpnvM9_2Oyu3MBDVJdW6xT1ckSp6GEaKxr0cQrYy3DdOeJQxdqdFgLeW5B_i_JObLMrzV7N1WejSQ0CkI6uPn0c1DRUNKspxnTHUyWXxcdTU_8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR5buuGBwm2TNWAmA2AEB7UPOr-uEmN6ZM0teVEei6UGMbFqU31X5VYjdl4Amy4hqW9hQzSX4M6l3PKWRtafhqVeTAQzb9MJIfwKM3aTVcSE2FiFERRA91f_I0vbJ0njtuk721EyppYEdK6-lFS99eozZPYHH8hk8zRLydeAdBU9ELM0T7TiBWHWqY9jNM785NPNrQ__eggPlco_9YvYcwYWZZxoQTJOadh9SqktYzDL3STf3X024KEUm-9IUzyzYirpbUHBCuWkSmt3ZC4ZJzm2Qzjs86N51SMtYBJD89eABJvDAP7-V2sgAx1c6-YAY8o9w9IviuWmQg7PQnMhYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1H41_-uA7gXE2PJjK9GRialVd9UltQaeSYJZE0YKDsGP0KVm6P2RohKHPI993sFZFiBJUxfu3uy7DOVQi2U5zIx7XBTfxRuPUSVnZDWKIgf8tZtViT8ID7msxqzLty9q09C08C_ROw6dBMzCx10qwKPpYQ1zmA3IvWXIeHeGeh6c-1EWgpgvkcMYZrTD-mK0n-EpPPkwdDNz6cfhYlROpcZYcsO-1CKZCum5jdP5xkS0eBnOiieej4pOv60lY9IZsTi2pZiopluw4p1unC9vuDcQY9CdtH9VpryHqA55gsqk3deFqcfR8MSvLXhu1nA0eaZImr3Fyj3CjaGqUIL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5242" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMpCHAS026WHhHXsuMoQ6PhwaIvmUNzdLMVne1w-s1_w8yFi64p6Dy_0eNFsC7a1AmkyDS5VWV8ha2PS1VlU9Hs7QofQNg6G3o-nvUYvYGbZ1L98qG41H2Hde-jHVns8RIuxsc022JK5qMBkFMxUv8fEKzFIoylPlni8TmjQlgZVu67TDrRUrOKcHe9Fq0k39ibJiKUJjCFrBPJ8Cmf9vg_dCtPPaQ9aViOEAqR86sOCrSUmVWPQZUHI5dhMi9Fgk4XECrgNros8Gyee8OsiRZ_7uRbwb_H5iBEbCjBY8Dmae4BYF9qgT9frftHE4YPHDktT66NXUpDodiUKHDUJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5241" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhqNk6RDn7O3Jv-gNKkiyxjhAY3DpKc07H4HKqqWXjKe-5_uJwuFPTi-5Mb4ya-ZoAQw-7nHdHHjDw0WiKWXVreQowm8ODq_ceSbRaPu5A_8KyxUnBXdJfKzObA20DAWqAWFbI4ty-KLeio8gjU8FoWkJtBZXa7nCKOkqzw9YdiBzpxtoB_waEM1w_76kal4bAeWTwg5aHphoRhp1qo5SsZPktBTmR-UosKm_9T_pPGKvXvYMfGM78bnIkZsXICvctSAHLfk0iNSvIA6X-4MM1kIhVC82wwGLZsXILTf9Pejnd3WWfeLxluQ9yuZxy1bpXR-aH_CAakK2Z9m3pYS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه خب ! اینها «وطن پرست» هستند
دغدغه‌شون «جمهوری اسلامی» نیست!
حفظ «ایرانه» و بحث «وطنه»!
فقط اولویت نخستشون
گروه تروریستی حزب‌الله لبنانه!
و توی مصاحبه‌هاشون هم میگن حاضریم ایران به خاطر حزب‌الله موشک بخوره!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5240" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqWDTrbgyAuWOJ18_55fONKX5P2CDUiVcT0lbLaSjlOu2koZcyBzVJz9JA4AqjNZCnmg6QZFqXAo9eayDojWdkOw1_bRgiTKux-ZBtWMzae5dkE-awrd64QPkIkCFfWHMZpD6i44NjETg6CCv1gjTc7v00hVYTR4DzaDSKRsJ4kJCQYT3vElcrFaPh5-VHjssYcliMBBG50R-JEKiLujSba0Ozi8UDNH25LsGs1mgs8UnieMYEYnpSSkmeqHcI-WqotLYgiHB1tlCO_fLPg8ncKlhMIDTINKXbZaV0Wq4Ut-jzCl67RVcspJEIMFsfvJ0WSMuZ-gEPCBkhO1OTKecw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbvZIWwjJN7UdFWwIljs_TOK-7oit14SUeInBmx_tkIfTEhRm_VnIfFzmi63kQ5VheOfO1uJ0wOGFCRa32YAjQXzUcD6LOu34jrz0xW62yW2wLDs0CmnrNAhWZ99lof4d2KD1oLbI9AGDALeOostJ5hwOwHxOlsOhWNU8XrbRw8PTno3E-YuJuFzmTkkn9qKrbErZSDOBjjRAOBfIgbEOafPUGfVdGJFxNhEDdx2QtgEG9vkfhMMzCCoiaF8KtU6Pc6rmG7zOCI4BxbSjBCjaMZBzF1zzMgLuZQGLGkUTH3FZntmzKWC2_FwuUewsQRNCgiYqyWsrCQTgwrvspqCnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDixbY6fE81z99C99JVTiW60-9_ygYBzxIK8zNv-AEc9-Rd4kBdljgw5Drrog5iwRPr9ZGoPtI0blZDKdays2ZgUXkN01MgM1wJb1ZkjvDpVCZlvmHeMBjzdm6VrQd_OPSix9Y3pPHtmEii8he_Zv4aSdH6Chl5bDH_6F3PsDw3duHIsQgGQ_YtbKyeP-KHXbYJRbFrKfKlQAS7y55bi5By-w0Ej-vlEti3BEbC9eEMiZKKCOiX-mmZRvyRTRi1zOrSpybomGOLQVogkoPoF4oaGgETET0vY7aEQZCr5fKz-LtQnbOC_PrYbAgwv5x3_ypWNQ--TYencdSm2phK5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLaQGdV8iU_vqNjbCfgBS2NfLcGZf5hXPN3Ibhb5B60Nd188-a7NHl5DppHfRc-OX2pEwRcILoTAzHfSexvlT4Y3cGSfM3IG4-8X9USqbBt65mFbZlOW3ei_bWxM62FIPYacsMZM2-cCRyPk3x3L4_kCJ9QBhqW8TUVCxqQksAX9jCVgXROWPwP61A9J-MMa3VTgs9Lteu0CwiITzWmJdygG8IPQQVHNLxLJoAnyrMWJvZJlTAOPPY5VI2zNr5jWL82wFev_T502q4kMGXYAxdOk4tOkqnF9IuIIQkAVVXSrlY1dAuoPaPZgVU7a-Ttu3nVb2pPw8PpTBL0wW_44_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسحاق قالیباف
فرزند سردار رشید اسلام محمد باقر قالیباف</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5234" target="_blank">📅 14:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=Wi-NyBx8cXcv4Hi4URGUGhiYJ27ik0db9pkTFmfEXl6Uj1hRjBPjyf_9MamFhcJ3xgndZJc47En0vrHYVuFgDI6UwqhvxLgB4t5QqrqI44yBJxyRmmilGjqTijf4fBZ5EyMEoOFZGFTaNM7Zfv4KOzNXLPdDIDHONAWHmOIRKygrE2yvd8EqgmtMkH0k0jS-YGd-tgtxjn_M83HbwGGbbqT-hwKXyHh2rEG94p8ZeeMTIkExoMK3UdASUtaF4plxERZNXGIxT_vZksZRCA5HV09wiit-PAB0i_PAqBuw0U0LABWqVSH_pegKP_MEW17GN2I1vwn9QGXCfh4rHRd0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6befcc9146.mp4?token=Wi-NyBx8cXcv4Hi4URGUGhiYJ27ik0db9pkTFmfEXl6Uj1hRjBPjyf_9MamFhcJ3xgndZJc47En0vrHYVuFgDI6UwqhvxLgB4t5QqrqI44yBJxyRmmilGjqTijf4fBZ5EyMEoOFZGFTaNM7Zfv4KOzNXLPdDIDHONAWHmOIRKygrE2yvd8EqgmtMkH0k0jS-YGd-tgtxjn_M83HbwGGbbqT-hwKXyHh2rEG94p8ZeeMTIkExoMK3UdASUtaF4plxERZNXGIxT_vZksZRCA5HV09wiit-PAB0i_PAqBuw0U0LABWqVSH_pegKP_MEW17GN2I1vwn9QGXCfh4rHRd0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obvNsQZzfpNKUAX5sbRgUUfigwxTHL2x7euMPO1JvAZqku0MOLOStWwmyooxchU1to-Scepe6qqWuP_NVapH9jDgGdiYXwIWrm1WyFxoi9P4jANpxohi6K15ssmBqJD_NcHPt0kf8-CkvcVpGLKjezNzhH9nDZLAnqXAYcUfwCeulugtkPfr54h1R2apiX2xzwTQQElpCWY5BaFznJFDL1S2_p49Eswe3Fkn2RilSofIYZt-c3iSLOhsbz9N_MBYF3MKxEt9sJjLvg0frKZ3UMcsJ--WtTY1ZaAWhLgmBVbMLOJ7-NQVxo6eulyriWkZztn58dW4ggBKJkIQTdiH4A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Bo99k2lPHOjSfpIHAhw6iS7hBQVIXntpzWHijcTZUhy7vm88hj3M2x0Y52Q22_RrIXvQPQlTCNccziaODGyGjEUoVQ2VOkbhZ7mPevjX4gLUboC6-bAD2tapH20mPnuyW4qkUujsJ_arysR8D_dDh4tPM4H9jjzFVetUxU2XRS15C7ifZZCcWQJxmJ13H_BPj8hXJxp2W4Vfs7rYpFbGQp6jOFCXr6n2k786XorZIoxHfW99MPdwEne2T8j22za6BSpxZu3Hg17PfAdJ9znlqMMv6hOzmFj06T0K6CQ30LgLBKV9hMckpEiGxlpIBYRoW8Ubnw5-XBwuyY3I7NQvEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58623f2eb.mp4?token=Bo99k2lPHOjSfpIHAhw6iS7hBQVIXntpzWHijcTZUhy7vm88hj3M2x0Y52Q22_RrIXvQPQlTCNccziaODGyGjEUoVQ2VOkbhZ7mPevjX4gLUboC6-bAD2tapH20mPnuyW4qkUujsJ_arysR8D_dDh4tPM4H9jjzFVetUxU2XRS15C7ifZZCcWQJxmJ13H_BPj8hXJxp2W4Vfs7rYpFbGQp6jOFCXr6n2k786XorZIoxHfW99MPdwEne2T8j22za6BSpxZu3Hg17PfAdJ9znlqMMv6hOzmFj06T0K6CQ30LgLBKV9hMckpEiGxlpIBYRoW8Ubnw5-XBwuyY3I7NQvEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا این خانم از فرقه گروه تروریستی حزب‌الله لبنان، میگه در برابر اعتراضات حامیان حزب‌الله در لبنان که چرا جمهوری اسلامی ما رو رها کرده و کاری برامون نمیکنه «لال» شدم !  داره میگه حامیان حزب الله لبنان از جمهوری اسلامی ناامید و خشمگین شدن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5229" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
