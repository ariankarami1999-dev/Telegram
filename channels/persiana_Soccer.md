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
<img src="https://cdn4.telesco.pe/file/GxKT-zoumib3Wr2CavFRaVYZP5qZ4OSY3m1ul5MDLjkxXiQy47raeffE4r-ndc0Lzs6Ha5mf2xxNgo_imNyhuy0gVjoO39Vlb-QldyFxGw0RsvCYb794JDOlWddKmPrpkIXx2w18YIv4uhIN2AJ5ugCxbOLPnIKaBVfNT7Nb-Jz6u0ldLz0MLdXP5sJdZhii5XJ7pO5NtNR_O3slYUngReiFOwLR3CWp8JsRgXEkPEQKajdlUBruCRxM2U4ZTOk2C0T-3yGdRDJAvHKDBgIiMXBs5jcYGUCNlYqnmyX503mo_ozQR07v10cIA8zU1KN7i1q5PungZ0tAw5bnv-sPLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 211K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 11:50:17</div>
<hr>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7rOnYaNqSM3-x-3e4Mi-FHsiG0ewKdbh7iHfgsbP7nDYtG2RhiSWXk1qi2QOj95ItR1aog1403wlag_eMNJoNeXdoYyEbl7yw2_qP_PNiWtp1GnGQFcLMA_xDybJ0GYs81t2a4LUrwDgpVbRvXZQJymnQFDzxdaRVKdUU01BHqtu5QXg3nziR9sET82hb1ikAkMJiPNcQJ5wv6trZZIsfV_D8obE5qVVwodvzKCW9nXCy9qqPt6CugdCUn-OG6C6n_p4apj6MawAxit7QmX4Xx6qsRFsAsY25lIi0qfnYmP7SpBP0jqrwEsdepn4StGSpw7jkTzTK3MH7chi6NuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2OFps6B_wLFSCKY_EuviK-9fzFwjRXwTAkVY7xG8XA841s33zJDj6dfUuu13CRQ8WtS4ZfDWzYcpAbcZdbe3G9ONxJlkt5Uqq0dQiXKvC2dd-W8DTrXEgqyKTmeJEE8vLvguSCZPCtljyXW9yiz4a_q7CzHZWJaqW5IkFVHHCtYiiSETGo8z1cQVk2k643fKMeT6oV9G8E6OpWaRxWq9iBTh1NBXbIjW9H8ivuS53EZxtlvkb1EayiY4MtfOJgCV8V2962helMatPHUkmsLSe5DQgAr4YQqHD_wbHu7Qp0W3IxsQk00dzhG7eAbt90Rkbut0jefhhh2zv70EdC93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMKLV5drrJ7CbxX41gc-SYdLjGiY-UQlaPghJA8QtVTTYBkywbPVT2dn0HQMP7hyLK5IqTRpn9CtDoIICa4kDZB3awe_pkFzSYSLyb8_3G_u2gNHEOhg21FZrrt7QuK_UP_2vpDOPq2UlC7tV7GO4nxXPmxuGO2j8-tDbxAV0X8EvDu6Y-IftNaXqKodxukeQdha3Sw1sTSiloOTLmtDtljEQdiUtn5uxtnCd1wb7w1jGrYhW_JmgkMKDOBzG_NnG3q_Hn0XjjQuWfAlZq-SgxHRuc8qfypinxw6wa5BLhSCGQS2bYUN8gLQrahyDrqqcsa_RNSSCSpiu_B4JNUmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzjIFUHcTm7S4qWa9hLQF5QSqLmNCTCkfXQ_8jvs2dOTyZAkPg5J2FIH2I57IQOpgPQspD2mID-_HdD-lP3E79m-8wvJfwkMPWaUieAor-86YfGMR6uxjlFF2PEh7D165efizbeEW0eus9kgs0xxWbAadmADXGp2EhzzOGKO61bJLdNWREMwjr0VqWpUCZIQBezXk2ZqX6RUGd-IOl48WDNcK8lkAwI_cvUZyb-FlhqX43P3rfipWLProsLB06lJ6z9pUhJB-YQCFgQPq0vhSzr0seL95SH3r20fdbIlwgaG11qqWNP7xMOZoXPhe-teFc9hzSK-2prKOsTxZ8DsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22134">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu9kKRmdyVXXLkD6gR8qSiLZDB7VI6H3UbAR0r1DMQnna_MXh3hx0Db1FijcVxaY-y7PJ8Zd-JdpkZZgun1gbzU5z3sfaiUzrpSAnP3nv6CVlaj9rbrEKWtdzTyJxaQIJsAOYfvpeXS--yZFWgyqp7rwVLql3SQC64gfUmqqeKuNaIPhLYf4Z6NOXsSxoXnpFYm2Z9C__F7y-QoECNjrLwVK0elPC-f_Tvx6nzHF2wBOoOCDVKGrv6xJg9NZfu67q9aSz5UHxNo54-geqcjrMoC-2G_wZKzXFT0xlAo_EoRG5wYo1YGCCITAwSGuXT17ik0Xn-vRCS7PGo_v1xC3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/persiana_Soccer/22134" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7RDxvC66dKTQ1Wt0sAqwCXiWg2IFf7ZfjtbX6nKBWY1BeXjF_XiILB_nTK6_6zEIaWeTyiktX2r_e6YXd3uraB2tVIqFjnn_wb9zxMJs9Fd3vPDmArdMwIksTsYeKD_h2RssTC8KngsoIR9KmyNIfiO00blpMR4tpSvIgiUSS1SnD9TByiOWC6amZWz8X56INa_S54uEwKSywwxkzMc2K8Ppzq8JM5Apj9x4QC29lhATffFQj-uOICFsOxBq5Qi5T0ZrrlOoUy0czBpF2gndjMDbvJw-mArufTfCdNZvHU44JK9GjkQZPEyJbsHBdbMBvmbPu0HFzvLm4xRy4MgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=j9JF5OJ9OioaMfk2PT2sYWcFuS-gdW1aaoBB5xA_DJmnkx3PGkV2C4uk5Udo0XULrpgJAFiuj5UAQQXb36XV8k5nbJdsIrCt2QbcUsSHA5UPvfmpiP7f1cERXfzAVenb_DFD5XE_tSjDHhKMzQdBVXkbWTm9K7ibhU2CfzI7S-EynqKLJI7QVB-rTvYwy2sYooOjif-gp1uU-nTDfK1JRbYYwzx3LpJjrwkE2j-KbnRvAsylWWUKPq1PnqIl2nqPj3u3I30-jkWR2O3fIgWiAq8J0iXMUZ88-LmOvZaNQPFcBk4VLgv6y3n0FoFtOStmPGveXbA07EuDl98uVl-laQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=j9JF5OJ9OioaMfk2PT2sYWcFuS-gdW1aaoBB5xA_DJmnkx3PGkV2C4uk5Udo0XULrpgJAFiuj5UAQQXb36XV8k5nbJdsIrCt2QbcUsSHA5UPvfmpiP7f1cERXfzAVenb_DFD5XE_tSjDHhKMzQdBVXkbWTm9K7ibhU2CfzI7S-EynqKLJI7QVB-rTvYwy2sYooOjif-gp1uU-nTDfK1JRbYYwzx3LpJjrwkE2j-KbnRvAsylWWUKPq1PnqIl2nqPj3u3I30-jkWR2O3fIgWiAq8J0iXMUZ88-LmOvZaNQPFcBk4VLgv6y3n0FoFtOStmPGveXbA07EuDl98uVl-laQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22131">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
رفقا با علیرضا صحبت کردم هر گیگ کافینگ رو ۲۱۰ میده
با لینک ساب بدون ضریب
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk70_6mFQl9Ox_2mb6XWNNY5xHA_MIyyBKqh321oIBID4uEjyOIEA2OcPXj943ami30L7j7cehiTUsIgvlLobU6gdIzCljRYPXu7nlcV4SWTyj9s7okliXkM0y95t1ltNMBckuLmOFHhN1KQbiZWv-AA-x85BFpeyXt90ftBhk-qycfGzoyt3v803MtsUWUagIXEurlgIrNEroQQGsZPgii_0TdNHJLr5EOPlL1CsAdS7UKkU7FB6Csz3Bgbq8s9U45-j8ESrd5AzwRPnbX3yHm1r0H2t2sJCjurHPW8xEihxQX0-53Lqb8Ul8wFhxDlf_h3lvqjZn8iXaT5PMQ2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFpvvFy0UB_WwzA4rQNEWdhh8gtmWStcjgzxhHqksXtWZSv_5SQxiaTwXbKChaLPqvR_NBWyzqJOb7_qrQMWsrn1Y2Gx_7hC7eAdbtDrgiu9lETLGUapz_fFkVfkNUI8wAhx_FI8uLRGHUwYvMk2pkpyzrZrzDlkbQY03eA8XJvFQNoP2XZly9c2UgZQRw73bZIaMpIcJVwT1JXa7MVOVokfo56nkKUYnwSk778nE2zMEt6v7wcUxRj8GUmjVFIzE0FCdzNHQtO6QYaXv8XYUsRbIpCmkYHFyMGGczpqRAU2hYXWYheAcX9ZRC6sUy0W1_h8m8dKl6Z0_FqSt5yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA_tYi-DEabbG93JhXAK4E8gft69M4Oc7yF64hvRPZxRi4BQrH5rYLwcfr1ZrBEPNEe-cVYTX11ffoYWp4ItGTyUGNW_utUPxkc1-R4ztzsUqcKHkFPwwo6jUOfpHu2BITDNrMfgNFbzbqDqi0SFZOOUrPf4LQkckTO-zZBWviQtRK1hLOs2Y-Cnz7SUEjhNNqFQZQuxum7JRNtZN8djJU2aAeInjV1ZbTT5R5tZifORjypqAkhc2qvfoL-cFPCXp7JuycIAwwc6m-b0ueRlSASaRQffk5nTYcp_93qwCWxIVP0_R_7SnHVdSe1_GLXlVFiWGZOoh5XF764Qq2XvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvMwPm-QRXgeiA44VhXcmxu4vQJCatpqA4HTVNlW72uFHDbp6J6DWT2VmeEIJ1PT7-2pmf4VWnQUfqKRMgKYDzrmZjaQ04FIvNy7Af7D-eS3spur06vgKp_hKzGfj8JV5W-HlBH6dX6YMnkHoBDLeToYZPKHToxXKWLCc6Uk94PrsEyT8pofYQisQOhAyUQ_cJlC65QLxAQV7jepUkK_YaAX6MO14dIA5id534sBJ7fI8Gfn7SMQl6YzNWHVmXgxccLuRy-ACKR6qiheYhgI7Cny2h0A0_0LxTqXg3gxEW1992qQp2OUASVReB1HnaGQdlR6zbykGqPAWG9XnCbOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8XcOtst7VVpY8r0O9dtEIHmkL0qzEwnhiBxtvpJYbMcPC42Uo-4j5h43fledWMl7UunckA5nLJpxdgnamBLs7zymmgeUISupfevebD0gtld6AaC6nTyLpaE_M6uvul-O2eYDhtb4Z8ppLrzs4qEUUWxo8Up1ijWuMTFLIqqs4DkvVtG-4U9AmXitTLAk8U7g5ez0Kf67OOknk1Y3IedK7KVBeSWD5wzJRIu1CO9Lgs1VFeXUVTK7e_-dz9de78M516mqMTL32VAhO9wMw50dWIaKocNAZzevShds4ZlrxoxQeqB_gERAfedOUzCx97bOOp3gLKngBNjAUofJgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORGSskuYyOPVS0-TgRAEc2s-AGWcefXloFZgUf_2RPpm-5KIlW-65yZ1dqjfg7z2kkH17QaVNN9o3Dhg5RaAy7OJ10yNm4tvpp1C_2U3-HIcuycbj_mHuQZ1bIKT5cd_clD9X8PEYpunQVHfTH2BagB26V7FkqtWi9jFP6yCWDyjGGmsplsZ0nTNGElPIn4xlv_PbS_ymdwyXaBMiEhFg3kvNORDYFUneTFU7Nk844GIXecqXWcrMdVEquOp2rgBrinyEot4l4HlgsVMyaocj3zV0xEo_YisZLeLSpEb94G4t7IMZVd78YYYw8bpdmKF3JLV7CwOUueQKnfu4QlQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfzjtqSTUcwSwvrFD1VIyVc3DhYSc2BnEKrgKRKv9klvpm08xHMO4kiKoedTe-y5eRoX8e0jyMnmvYO9zQFbSVV4srveDSTJqdu8XyScFgJk5VoVYZ8UY_sNC-lJ5pH_Pi3-2TTFnN4FNRhcZGNdV5eEhM2Uip0Wfzp6iN6QbTpx-CyzXiH5GRjMAnprbdXsvTrOWEGJrH2ICSyS4PwwyKMU7Jbr3S5tCkTmpxILLpTBDkTclZThIrWe2FOJufWx0CWRV2BUo8EkHO_DDJkB-4WxyPcoXEIb8bqDwA-QNCPxsmz-Jjfo-Uze4X9siYOARuU62JAQrwmvC9eFLlRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfSzq-2Q6YKC9WkECyfY5KMufuScUopC9Y9CjMac-XiNRrHoOdSbilgMkJ44fKtfnM37j0boSi0oUCxeyaEeGl2XqMa1lGSxyg3MGp-swxMzcjz2XlSC6XsIb1rFTqJSeRXa7nz7s2zHc7e4X8qPdMAjkwZarezCpNaI5XvrbaTI1ka6MW0FrEVAIg3X99t5bpKaTxPxb0Z90fPvainnsJ2d8SBk7kDsf4l2952APF-pXbujQmeUSNoLdCabAzIVclcGKjOBX_B3_ShYr03U9oU1VV3jBnYLWT3fMtlaqb767cqIbRbQ4GvtAxmS7xX_wEwdG0BETzk13YMH-7HcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CNkb_5l7HO-OAT5-VANksfCDFtmnfB-tF-qcqmn64Qbm7AzXCPXBT42wwVaNqCkoBhPxYAMOLOOiZuW1RNppTautlkUlbRJiJ7nNCuXp2RO4G5sCKfo9KQQK3l8K-rIdjS2-VdZ7LvWnj6XiYt4qC3slV4dLMIKEpNplSLSha6kFLSHSGMob4iSsnaI-fBkZOs8ov59yzUtQ3rhn9lnPRbq7OhDI5wlWGyPFEHcj4DgJnJ0HK7nX4L4h9H-iRqtIaj4hOkpPVzeaUQuIQivEML3tu_Ev6V9VR8ofokXw98SY5AIh1aWpFc-lzPwEc5vWkO_NCQB_aMaTB9Pz6aM7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CNkb_5l7HO-OAT5-VANksfCDFtmnfB-tF-qcqmn64Qbm7AzXCPXBT42wwVaNqCkoBhPxYAMOLOOiZuW1RNppTautlkUlbRJiJ7nNCuXp2RO4G5sCKfo9KQQK3l8K-rIdjS2-VdZ7LvWnj6XiYt4qC3slV4dLMIKEpNplSLSha6kFLSHSGMob4iSsnaI-fBkZOs8ov59yzUtQ3rhn9lnPRbq7OhDI5wlWGyPFEHcj4DgJnJ0HK7nX4L4h9H-iRqtIaj4hOkpPVzeaUQuIQivEML3tu_Ev6V9VR8ofokXw98SY5AIh1aWpFc-lzPwEc5vWkO_NCQB_aMaTB9Pz6aM7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goBBhfRMjsf5EStnP189oy0pHtTEh2ZCqVETT6DNnW9k_YP2-d0j0F1DzGdxkmBp1KyIPa6wGR0__uNHOp0Crt7dnauiyLFrMZBNM9o19MXzi9OtV_VKcrIe_2KnoEOrxcrz7uyF9RXTynq_6S0Kk9Kjr3D9vMzLAp3eaNj9bF17m9HZQwIbJolHG3ty7HvAQA8nXVBkkkEOKyyr5i2dxFT4g4lLgLASd0VONJyMcWhzejVWusCgzSy71TXcpJyHnCsTbetecUA9r5DQ51y2bJRkMhTsieCcPNnyPk8z_Zfj0mHmSVAzh_LGt9lJZ7KUuqhioDjYr0TJ2u5IBMw_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-aS9QoLWdmidC7uZgc1VribhUPHJfDQXmmRsCd_dan7hr-m8t8lE5jpW13z-d7e9dzgngZGCZl_8qOllGYwnXyNxDQDDQGAltbeFl5Ru-oVIijW-wOl2-K7oTUB0CU_jdWkOo_yrm6ThtGBahpfDyOQlUL0qnPMopBJYk3ZIILDJ63qZnDfnC4Jk9D2203sHJG5dNkBBDRu-C_PJoIEpcbZvfzJHjHaKj00mVk09qwUYr0qh3lsZnFXgQy_wZcSDfye9bwR2om16pgozizRrNEO6pfgwXK5nQIU-H7Xyj2liIYTcz9X-UoP3BJdv_OuDkhGRlgkwM6HrvmweoqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=C8nkZo2G4pHzayy6zUBYVCIl6WWVhqfntn1ZyUrriXw6M0UrS9WCb4wR9rNTvFdabR19-67XrkuArQYreNu-oPO0FIRHbqM8BuM5IOYWOHgGfno0CekZVZ0aJ-02a2PbdIMafn90tGnl9WuMnRdvNpExspxhtK0vpIt9_hmlG4rB_4AHK_ocbF63mq4LeEfXYxkP-tVq42uUfNqrcmnHJ0x5LUVqfhLZ2TG_K1En8-dZNyw39E4EJq1-b5qQJLhH8jCYrl66brkA_7tmPvgREud338sOa5HQ0lpSjZ4FvERnAMW8aFzIFowdTAeRCfKFjwQJtUba8XPXQiYW1pdepQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=C8nkZo2G4pHzayy6zUBYVCIl6WWVhqfntn1ZyUrriXw6M0UrS9WCb4wR9rNTvFdabR19-67XrkuArQYreNu-oPO0FIRHbqM8BuM5IOYWOHgGfno0CekZVZ0aJ-02a2PbdIMafn90tGnl9WuMnRdvNpExspxhtK0vpIt9_hmlG4rB_4AHK_ocbF63mq4LeEfXYxkP-tVq42uUfNqrcmnHJ0x5LUVqfhLZ2TG_K1En8-dZNyw39E4EJq1-b5qQJLhH8jCYrl66brkA_7tmPvgREud338sOa5HQ0lpSjZ4FvERnAMW8aFzIFowdTAeRCfKFjwQJtUba8XPXQiYW1pdepQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsU2G71yzcVDl3VKjFrlwBrKCqTvviDLmERN4A7oFFmQbkxxiS207POFwqUK50OPtv7TnZth6vgB4RYpTVNcC5Mk9DaQPNh_Iuf0Mxuk0o5ldiRivGSOSphldVvvuUbTJ1hlRA8P3wY233CH4CgaZIRSsysSHgRAktr1dDXqMHIrL4cp5mz1FT1OGMxCaRrmDBYiyoLl4w2-sQRJ-pjgHLfdBLeYVd8PZisuTFjPef0vS634eryFjqZOpp1TeDtVZ9L0Ru9hW1vp5tmYVxPq2fGNXDT-mqo3Ti6kWxc7STahPD-7RFqQGuBTf96dU4siWJBG7hsHGuNyWUPPxUWe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qhtPZAKTMtnX0WTCgAnM55PZiZMpXdX-4JoGzwcrjvG9IFsLPzUbNprRJuRxtvxlL-4oa1AClXGO-qJRo0pSZlLLc8VHQnKxa9fIag-XIQ0cacYmeM9LIsXqBA7CJFeluz58IWkoAtPnGDGfPkw3iERuUB03Dx9JIg25Kne0Kc5nedpf0_CCYmQk8BQfX9T6gbu84gXG6yVwukjrsC3qvx6P5cjSSQfzxp6IpxStej3thPpVWs3cjza10CxRBECKA-lTN2Vv1U0Hh9zi_cuFNnM5OkDqAQ-HrNGFM4QNAsYWNZoA2HWpuY9Ltgk63BabJV_78BSzl_4AQKSSz42TpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV6qu0lhqrAkELgWA68O78KyeTZIT785RSjxOasGKcCy54KkPPI_33zBrxxUjjn2t-1DngOEa9oOIVHf0-IIVV2zw3rDYDtwr5mhGI4VeNvNeM4xr8Yb9uxYK5Aj-ge9eqlEW0or21SIk35w-NqypZ-J_yIgc4nsUhQMzG849D8GZfb4hBlzpOjKetc93OSJ66-KgjurA2yk6kry9wSOSqxGwohoXs5cLRDPq3ykbPQi9DgSJhWmvsxeoxPq36mj6Z5wBVWsSiABG7dQGjCnKN8uwbCJUs2KOLpT3gaySe_DgrGv42wmORFHLXQb1lrWgyNnsogKJYfFMXQK0jCQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeJ8zW7jvwXyXoxW8pMc8nvV6NDFyuyL3HB4Y_MUhcr2HsKAfwfUh280wZVcJzgOTBMyliGU0tkxL2fkuL1FKqIt2EmdmYWc0ydYDbe3DuH44YdiaSgGd2Bf2tLS1yAEDE6sIs073ZJ-epAjcGcj9NR0iiKmm_30odRuhTpdfHss1bbIBCgQG4FNGFaHhacgQqtZSsq6ocI9xfVxtj_U3__npDqTGjCnaqnttc2qakkV7kFeZPuJM9uxCjuDsLeA8LJbmehGZGwvQwMkH52XeRpnnpOuiGHUjj8l96zbcPRTpMwJ1CuMwsfc4qNADKEf-GnYSAWn0fzQQLGQ9DNqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5mdkP8irR39nfNBlobbZKAWfkLEo5x8MRdngaKUntExvwiH48dc3qxALCiJdoV_S4bnnForgyaVxfFuNE3htiVFh4MJQ5MqRA_u3hZivula3EdW7c3LLm8O3APSkBxYR_rAsnruU_T3kRZC4iB6DguCEKc8RujcBrQLEckI-2tUQVGUeaj9rgFS1cXN1Js7dIp1oeIeN5t21c1qjp9IYDhloXHS9Uwjc8e2rqQdVFYlwERvuPJ2K1g25hdGLMKuvjZ3O6Yd0o7CNT-9pnQtIO7PoIOmki48eMTk0z6_lAGzH0pMm-nBV-HPn4Yed7FOxR5TsXTRUXOJtEhdrzl89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAbqqFzH_ls1L6XScHZ3v-f48h-2Rdl8EErzwzWA_nV1QOfmruqOuh2K3BHBoxFR5rYcewMNcQKI3HdS1Wha1YjoLA8giGeVNilVaf30Eoih1lvCsQlbKoQ14mompGoHKwlYiTidq4Ski7bIFhzVbV-g0O-lsnmuKyrYxXr7SpSc9d8FS9H9FI6gC9_EToMegI5Fkqx4Xr83PKYWPbp2Lv0Q-wIKP-gHXkC11GbjaGET2gqSjd_lle1_sqDmK5lNTDbNANftdQYkUrmV7TL2blhxBATx6_iCLN6I6OpeGR_isfu4j9hhxdq90AwlzXIX0JRLUGuscGB0L-ycM7p7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLDq38gGF2voqzSkRGp7kCbkm1RdWoVwqzogiovy_wmdVOIzVSgO0mSrHY3Oy1cuFEWYBhL48lY1h9rxza0IJayKTpd7YaLJzJefMJFGsw4Klm38Sb-aP3I_XY6p5tCXzjeah4ClvcZrtRfCshuABbyDx5Ari-ohBxEg-VWD5DQv6ZBtQsCYm3h4iQF_WR2FpiPwMprCdFx0Unkvr9U5Rm8zOSYQyrHoBATGWeIwzifcmYSaZVWCV2kENoUu6imFPYBEiMuKLAZiQIfH38Q53McBi5UO3LrSEMmtJOFTgEeGQR_tMQVKphR2LenmrsVJpFjd28NH4GZRhM08jsdsNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_DRNj8F2pioMW8jRAs2poI7KDeDdzPz8ab5PvuFYPAl6ZsmcTcjJIsM3vdQWMq-Hjv65yZ63VdCn0M4HWoq6QsiNW03IKgYgwMIGQdCvHxh-uYMTap9DdJPJcdfjBViR4FhkDo1AjdKblg5tPPYdA_8aVOEwfESEGN2KPfFKD1BXIUfnDto6SWnMqNDb6BV8bk_yELapXHIFDj7DH_TPUaUiS_-Fc-YMkKStvBLJuYjPeiyH2kHQzW6RPXIq6sih9QEtx_b_mp9ZxD6-3DIFx23aoT14I9uTbq75VPh5ullOU2_DOWX-2HUwzsSNjeINDO6FFy6OTHOs8yoMHgL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7Mda5pTOEG_Hqu8X_Fb5dxoGUpKLN7vmv3A9ka9Y1I7eXStzeQbWwoMwG_hzZFvmEGFfBYnk0zaOmhAwaFw9E8LSthwRLLZmA7E0IW_vwkbPuPYRfSw_1yfh_J8JxboRtdPcMY-NESWsD4VAbFP3KhwNKES-Y0AjfLoeAwOC-_1twckRiyX13pfKDbAguY0DhaHgShnKR19qMWl1rzDDj2QNvHXiGAG2Em_18_dB3m2DzT_f9b5Gel6gC6FJBFvcs8Pgx4F8JP1XB5LeVuEDhCexokG2eUAoG2jbp7Tr_29RLdXnLvZPImAcuLOgTY4st6tbZV1tbTfE3GUY2oLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ayw9VBPy0z8etGOEoKlDrpBdYGtqvIQ61Avs3ALRdLxPDTXzecny7CrF4JIVs1mxraew9BiXCQCOGcp79ye55tzwQPKjOsS2nTyRRrrmSYxoKQaGoSocdF_hoMcHRDbG3ikwZd973tAF-SBaTUbOUe5g8hHy97Dc0R1COv0unB9D-whH0Rm1tveACVbHtyrZ15rNCoQ2JgQUFRUG5_4b5kQtdQjFex1vxgDnD975Ua_Cv2E3lt1daAVZJr9BK6CNkqUycf7p2LFk1cB7k8cKXQ3FJ6qzfffpLdyWyoczellCeHPtKoe4nK8hIOG7GYikPMQpGGYpDN6Yz1s99q1zhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYPoX2ON4iGjCftMgTCCi_cG6LVXAGNauddoXwPYvpm3rZN53NuzgfgExgzo1nn-6Lhjv22xr4grlNzG5lx2wEGcnV6nQmk757kJrm2WfKaE-R0f_HV5lNPYPFVDJZ0g_0V4DCVrPQ0JQE9aZdfxIGVjBRs7NpYPVlnDSizAx5xUNyyRo7N30OI22kQFHS4i_mqbhdkUjGN74hqp8XQUubUWSFQK3S9GqJ265hY3qqeNIhMybEZzDZw-Z1FPeN-c6c_KpVqnMqyzc88I2jvJdluWg-hgo3Njo1K6a_wtGGSramz85P2cWX7PlbI30TYvIIJsa6ObOwnur4TTfWSt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpwK1ieqbm3bk2HHuoFixebSo9ofIhCpTepnLv5G0PLj-_GS0ZenS0Tc7_0IXzSdSpPI4rnwfLPin5k4qjcRmIP9DcKc4VPEaV07fA9UNvIRjVynFCDz18vQx1hvV78hb3nHtwjFmo67HJsPIyjZjL6onN68kqhXBRV6-o40kv54gosd3-kjNO0oW097TFiMD1lp62JJjmkmtB09YrMCcJ-f6eY2jGDUEbiELlkmZ-g01gZ4-rPmisixRcEV_1d00VuwTsvTqB7Jm3e4OJc65OvKwmL1ulCVEQQtMjB7w-kowVZdHooOu2OwZdogMKD5Teqz9tn_qelNw1xQhqsYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1OIwErHKp-6SOk7Q-8DFmt984MqRCYmqPDt_yOFnNEnjzj8r7TyT1pIOsbJl3a6e54Ir3Pz2SZLPUFvBRnMD9RiCCHZ3ABdQnsSgUZyPrGZ-Y0wS9n2PU93cWl4dA3mLgq-0oiI6ElVHrJPoJxRSW4Q9pCGRtZSqGKhQXGPT9Xi4kpiMguK6fM4K9UZ4IJgcPpb4pLPXDOVZtiJ0AVuLrXhBpgvmvVZ7DmPEPHRyPfc4VDbUGSCBBzlOnbW5PgZel-fbsCrPcqKsCN0pfQU6pmb0uqnBYZmHMyeGSz9pVAuVH6bdmrurr6SveAbLM_mSkgz8kjcUWoqxIZ3GiepXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxiY-mTHgkQzIN3FDBQy_mjWSr8ghrZ3ZwDQuw6uJAWbxnOarwVJ_UlslAcrW3WM2LBNuFKZZE854rFsUpCnUUwunqH2iuI8zdjHuQagW1KAoEfzoKoDLVJgZ4BjwQfrxpFKx7Ra0ojQ8rpQG2Omhb6Et9P6H12HN6p1u2IrIIyykL2TLFqPz8vJ5sHy3r5KocCscJ4hxyahUSZd-UlsJJ5fm5-G_8NF94OQuBI5Ce83CFnlz3AiJxVJHdEXbxb2Lk3OTO6fTrSdzHPg1Bs8sVatU8valx26g8v_5WpWB8MAdWOYj_6nhUop_U42ANmqcVnrPRQusus_otaeqM6tMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qAeROQ_PuOd8ax_8uC0zkWdzsgmDGveQwj-mbpr2-RBoVxH-uo949FK_aghKN_n_bBZ0weW8ZDrw2W__PmB-JPtoRodJrqIP4BLrnVkW0RbYj31JS0VEhp37v6tnFJI0QrXrjjlhguBt8c4PQkVlq7-KK9ELb8zm90swR0tM1dGqK2AaxOdKkw-obq7ssrhYajxrKk-M7Gi8UOwNwH4Wc2NzHtQ2144FU807DNguTh09tPZz_FpIfhAxOf4-RwkArYGcB2co9kL8P7cmUQNFTAmJ8NpctIGf0uYE-01kImECEtyv-ZMBT-7pk342az4nUAiRs7ZQ2cOppocSAZBWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qAeROQ_PuOd8ax_8uC0zkWdzsgmDGveQwj-mbpr2-RBoVxH-uo949FK_aghKN_n_bBZ0weW8ZDrw2W__PmB-JPtoRodJrqIP4BLrnVkW0RbYj31JS0VEhp37v6tnFJI0QrXrjjlhguBt8c4PQkVlq7-KK9ELb8zm90swR0tM1dGqK2AaxOdKkw-obq7ssrhYajxrKk-M7Gi8UOwNwH4Wc2NzHtQ2144FU807DNguTh09tPZz_FpIfhAxOf4-RwkArYGcB2co9kL8P7cmUQNFTAmJ8NpctIGf0uYE-01kImECEtyv-ZMBT-7pk342az4nUAiRs7ZQ2cOppocSAZBWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJn5EsSxVEp735CYA0Xucqq153ZJEQfmN05ht3BaVg3X1lmaZOyv_VFR98sg2frVzhM317ag5uV_v79JQjmIHE4hQJcZKCF_daQbljsJE9Xuu6y3Ko7Ytk3PGJvkhNJWooyiC2zCPT6HAeuWRT2bqCe1ATHccK722eMCmCF_APy6siqjliDybJlSbMlAGhBFeAJy7NtzZL7A4TAMJImUN1uL2bAeZXTiDhbYnptARaxqluVDn308XNPsFDLp8_h5f4Qt8bFHK_QJ1h-2KbWBrgbtmPoizq40DTSSdLyp7BL4oeE3Q79qTy0uPh5XsCdfs784P9MoTQoRJQ9z5PrR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy23rmdwbDOQBpkYhJsKiRdgrd28lhr-z4Qp55Vej5w72nlNiCKitANbsk68oG-pwjLyM-2nrMvtjGlZh0fqeFHanLBBjwgdIevZIBJkcNMMVYSyVXjWchk8HyvnUocVvUGzsQ2SFL9-GekgHNWTj5iLQdjivICx_eJHUu0x6Rl3-PH4FpujZrD0fGMKwZFcEnrb6lY-PBUNq7K5x_fPN2hZ1OLlUUbbDFi-KwmJFCasmELCPPnLRc15a8iq8o2SM-6t3gjFzXr16fpXjHs0SvrHrjjRa9u_sIusqtmE_zYI5r9SsoXF8g1IuLVt4PdVlzkhMwutJOxT6So8hvVnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy25MVvqHuaRgGMGh3F7ZnbplrR8UBep4u99-io-AaqrmQh6U_-5aIU8167buJZw2Pe3kDfcFxNmmcV8e7dgqFcM0yiQq_sREkTwqpFxvfnixD2k_W_JLY5DP8T-XY3CKCtxVQ8cd4-Rz2lhtTK_m9zmWvt-19CPYzg7ImhCg2_1Ltud0jN7GkTbk6inkmeTGSkT8ADCQFAO4MglD1xfPdkIMvni56WKE2jbdKiJx8aEhtqay8cMfxLLJILJk07pxU6iDBxaU-aZ9uKNEVqAgUnVa5kNBhX8md8r6PO-scXD0dwezqugqrTVrf0vb5YHXc3XNz-nsf20eSN0aZhvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbO5nIyJ91R-0B8HuLFvsPAd3mA-EnR_fAYLKgXtQhWHAD3Iw-WymKrrmZ_MMiJfxDvksXr3SOzJQt5ooqNdmP1UvBOxjMk_-m8MfB3FqkNMcznMnVY6OJJBQ9KoyS3pcrnfJl2gVc7dzFfnXS06HRBZCxqUxRhXLmffVXU-viiKFpjetSmsD_rviznI_5JQD_AwqXafz9X2Vy6yKE2kxZ34vz9pfi6ZCzOqg0wxqNDiNwuqEzBF5l1j_a9TuRY0sF-3dr-isEMhsSf0ivHh-0QLl-6yAWit9YWKcY_XE683evusaFi377Gca5MubnPvZ5_bsHe2ATY22qFLTU3mZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyKlmZu4hQPpGYLuADlSFwEGuOGsV4LeSVL7EEtqG5oUfguv7VEHjVxPG9ubk-qY1PoG-0Pjpw3WIGVdYgJnlE6-kXKB9_GQOy3S8R22lJSxHZEdoVzVwqx7DLEm6_0FQmEWXGO6REhiCdg9eDOkDUtle8l5A9jKns3ALsoSeDzowZalXTF1rSDBv5A_1UfukhhNrzzPRnPSwJgrP9bXMiFLjPTdUcHdkFSrf5Y8AARcJWZN5LzuuEi-rTWXEiBPPCADXYSKLYphbV1vaOQn4k88Ut3REKiIJMb2KNxl3gU8J3xzhkEXvdaQE-x_BOsv_7yQN7V-VB6RNZG3S7ekEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCsUNCHOSoA0oNFz0iKqgmT5WMPU4yH-fJjFpCljwUFl4OwmtroKxGSp3EQ6zBL7u7jfGqJEs4OcJGUDT8C7KhHKObOGw0L3CqfhhKpCT3cstmiO8Nj17CQ-KlNRDU1N0nQx5yqugSwz6jgeroOYQcBgub6Jqb_yXKm1xeBUvOEowrq52nK41CyVmjCy_8G3NQ7FUmzcXJsWw0v60hT3-bv9B7w0UvZ1Wp1ynSYtMxo0tmC5rN6iRgoAFnRSUvI2xKjKZhG4nEj7ys_eAEJs5Ovr1my-fZb4xB0mIHZVjrnq2rwLnn9eMo8cYOS79aUVjKKdmjyW11JyaT3ISRlNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxjvGpQqnp71Ji2YviKY-hhdKCNXAlCas2TIKQ22C2eNveBlEaibraqPQ1rqoxDiGeFimWJgn3RHMOxTX3F-SAHYGtQFKQxXhqMPP8uJxjtXL-v8hZiABIUQE03Plj8QGWaKMpqCJJH8MPRV3b8qMQWNa9LzIh2VkA63uxZxTXS6tix27AEWTpPiiA9Lu_IrxZpI5r1nhhWZO79mBsKfjSXCI49JlthiuBriPqx1C0xQDCeRjmlYqAtBOHZgH6v682_fYQqfZZnPgsLDeyFh51JICFhGVXBt9pP1zl2Ws1Yh_-eGS-GWMR2Pxv9dWj3t_FwLh477iTKR3xn_89cibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX-0HHbdj5LdqrDXQxKZ4_xujvpL4TcyKi22VGeW8MNrTUeDJu_Z_e3NKr0-BYu4-1qU9XIBENPRR754GB59KyMq1tLVLQqLXBAQm9AqHX410LYCphZiKryLM8KV2wlnXm4axOQSYMyphZXbRFE0JsJDHKDIaFBOhYMc841bFgKUG1M90fo_obPmGn1HTw0objJ2MdsSsNUklMkGI6oyPdJcZFNo6R5aBwRfUViH1_GAYZJP4ruGik5JXDaNhwfSLozpYn7UYIS5_uJj0J2D-M1tjCCnVg7jgRhn4--e15iJtgP6VoGlkLAxytG2moxWT6AlqQqsi48t4WsTehDEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vcx4588j2EYTmBIV1WgkCVjKgGzfvQjpokCvOGaKFPLoirX33PhiNQXmNrxkjrUY5nTsKjg2xaFLNYUAtvD9rOAq8JtnaJ1A_450Uqlr2e3Y7MSH7uVuFjJKU_VzPUiQ-IrTnaJEMGmbsswr0tbVUshbozGq-LsuyPPPhY7QlIp2A5DUcutCaprzUoUpE_d0Pafzyy_J5f8AoZsMusACb0GeQkgMcVIssBPoIoshOthrJAg6R0wRiMZ2Gi5fP0HXhMnALTRbhf1CZI1UIrQCFuZ2hZk4NdsCgnApq3OwPk_sFmsT55czxH5NW0D_0DFQdouX5BKBk_lrKmRCeYoP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHY6Gdj0fpj4kGiUFokKAgcxmPPnR-gYoJJLsMXs8S1qHpxFRSPoyQ6t7dp_s0WkUJLibFxtPjZuxXXhhRpvrMLr0PS53P7J1ob5FijNjN1e26QsY-ayqdcCum6yKJTqBAakpTQmEnTWOGggO-Dx01EUW-nmIr2uDqhpxVlAnBw4vi4d2SLyIQRJHlvsCQnTHT6lt-UifNzq7q5Q_9m_pU0L7TKqG2W-VqR4IQq3_Yb9zq0Tkir9uQfHKPNGYxqb4Wli22PnX5yZcOr9aIiTI3FDjLpE3OPwawVH7aP5LZo0AlHg3CINxpVkyyRd4NI_oTJkKtoznr9QtvPVQ2V65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMLo5vB-Iok1-WgKWarQrX4mu4EP4zzmAR4ZNOdBUNi-I1kQ3CjCuWCYIMED2UF0jauSQ7HK4ROLojvdb0I4BU7hzfV2qR_7tIW1e4tRd5795nPN9aiBfrtzjmvIuk0_PFOX6Sz6NsxNrxNXUK4G4-ucouT3KRUTI-wkweGi_SWDP75nk6jcu_RTc2IFyk7TnFLo_VtFLDE6h8qeoMfUpusCoQ8H_GDWPvhdxTv7Mxhd2KZOOjiJg4osal-4e7TNJQWbH1kXIfMrNwLkNKLptgaG1RsAIweGh-ZAws7EHhunTZpwfdQq7BR799G_uzmnEVRRT0ScvE78WBWWiIO8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEKUbIdzhnvs1RrBBn3sBEbSRWsSv0ajLsD-IEmC92pF2sV0HM3x7wCXLoQOhoBt-oPjEd6fvmYVP-G763kUqeasbU7KvQAkjmRuQDD9-d1t5iMmmY6HY3g9X7nr8_2-4zS-YRIN7q2M7QjF1YuFzPrxqbvTRd7NJfE2f_5wVa1n3KTatGPkKLy4ZgcfUDJnm52CFp49eTMRpzmtySg9kOhJ09YOpO158_wWACswVgTLGxYUa8qi1aeyb6KCimT9NWsB7nWvM-enP96MkB7-z12URyS8rIF9gdOCztSWxMQGbMFUJbDpSJ5zq6_Tm5PhsLfC24pJSGZTNhnFAG8VDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nS7y6OGb20W95Wq2du6KJWVJHUqzHDRK88xBfMxg003mQGKhlQoR89kmpAo5ZsiUTnXPO75Z24C9AbXvZ5atsl01qZhQ4xGFY1H-011dBoBN_ow4q3jGs013MxDwIi2VeqQiZmnZipjX40U2IVklFuFb0aHOU12YaKYU6-2XQ9RsAhxoIPaQF8fiVEDiaFGPL6uiZ2EaLsrDoN0Lk1xpkC-8hHhr0EfI05yeMQ4nY8vMVAjg4CjrEH66D9qTfk2DMM1f_sbyryNPCSDj65hrUWrGCy13xx7Rg4hKfud46oJnSDg5mRjMUkue9c2AjPhngfy0V0ybddHlrPX7h8FtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUg9uGntCCxd-VYAdpPxW6WzynnXkXPpPRpD1s9EnLZ7RCZVNKqc8-Hfsse132XmOtY1JHV0ha3IP7TgVtH3ZW9hLk6P8Ww38zJ0bUXNQXFza17u5oivz3OGlJi0ygYUmoGWF0bcVqdcNtUeoNBuBAArThDq1AnJcV906_RFvr2xKNPUS4gCdfyULwX6yoxF1rTw6Dg8_UubI96jwKqzEHHzv9MBT8wm0G-ISfsRKWxPgawzoz5hzCEJNkz-sq8G2dUbcrG_sTzyH0Rcqa5l5V46ngWqmToXmG9BXaj6e3C-JjWNfkt5RfoHmP7G2o1Lno3jqX4204BESId8lcSxkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8Af6Y8U3wlhNGe6KbixM9jX_gffoeT_h2vcBnWzgrEPWkBx1uPT1gVQ4V_QHFawlM9-9I95iay_zPrtcvR3OFwPo-V-N93Wrt-8VOPvawOrtRZaQmtU14feIqT73dt1uo0XH4AK3RHXcDcKdfP3OLstvyinVmhmhR-Y93MkexKUrMXPIqoCb9gPn97Tx087g51TxT_6oCY8gfnaHTn_absHmRNuG7azWEp_MMtKRVRnKMvVfxbyJo9Myimbp1IOkyg8RFmOjo-ZMAGwbDhIBeTIgjPb_Fj7F6rlr9tMn4ot05HDj_dAlM0xAgBidxzI9KFvTWln-HbqQVwkOmLuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtXt5CeLQrTndDcUV3mnmhoWRnorpYQp4yIQQer2lwO9DYZ4dY8dfXl2xNo6EZtiKCtNF2HCA6vlpMd65-nqWIkA9KjVYX3MORyWrKLZSs_jCqlc3pSxFFwdFZdpz-Z5Bz3Q5jna1Z_5lPLVaGC_K2ZiKGvmcpgdMOdrJmSm618WYB7KtIzntJFdu5WMf4Dw3shdhhjvAmRjlaSEmeSUG8hvj7PNpX5JyREMr2sblp4sLw5v7Y59k67RX5iFl81YbpmLC7gxQ8N3tmd34vF34K7BOrSwO6kwvCSYyCGN0W_JlNon_7Wi9A6D76jckJD3xvNQh6u1cSng2KOwOmW3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn_TQvvPvSjgCQQnsRdhVmFdcsq3DqISdDRngYU0BSfVLf6egvDDwOAsE9qcLrVYk8xXjom29fJKtX8G2pYJmaseuLlLY2Lg6d1ACgBBTosfidbm8WPmKhSLf1uvxGvkkUjUGX0YJjpfylEqzfj78lwAFpB2N8BGTgFRBur0Ib0M0VeBjvPsuBNtb78N9vxa-Uxbaikj540tBkA1yT8ZKD2KGeP2bFDOeU3Q424CJ2aEWV7oYXMd9KIClemempfXFoqoiEeoUYERHZHRgq8nCF-gtRVL2f1yuzoDe5JDcTGJ-1MEWOTuHGV81qjDN2VDEOWBdRTQbq00tZd4eNXSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIqFuFYRWjpnqJjUEhKEgmbbjpQBMA27QZLTH7NO-AT60YX6Ji9NDrH4gQZuywaW25Ms19szq8wzVJub1-oaOOpar8LXZJ7LLzWkdG19s6kapQZJ5pBJdKJXwJ5qSKh-Fq2ATVV9Hx9BP-pYCbCvgPS5jqveqfT1rY_XStnzFV7sNQuafKj4OZ-6tXHrX8yC7X1yxas3oSYxhmIdDaHlFXHh9_0zZI6ZEkRlrW6fQuf8wMp-ElvWvnyfx-TK4IlCaF2tlAyg0zM_G3dygADZLJJBg4GFRQy0YsoIJ7KdAS-UODBcpSxU1OMFv2cCcqTOoR5A52LAy17D5YT3ncfcAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY2ZeLpguvhmAjTMQox89A5N9n0OYUrDPR6DWSLRpwB0poUQZhfNY7_H_P2Rv1SCUbTu_fogGYIvsNZxb6issHl3mbHTWWweUFf2kbmqAdpRzo900Z6bxqIWONUUeUuDWD4WmpCzOnBwFFd53aFm69eTAu9ArcZli4gYTR4VMP85jp_40va_k4kWROz45gm2C1u1pHgotc5PHFzgZl2DGaqo7wlQvMC1B8QCLDfttC68CgjDhvAoYnlClHKY4uZrRrsQLdh4uT34VFT0rhDxlP3Ki3RVLhz7R8EVedNBg8clwHbfv65IoV1nF6_vxtipiDcyWRx-D0qBijst0pFkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vudiBVHw4shxtX0myrkMQEBhgV1I4CcgM6Ojx4oHZdbCsBmiquLRpem20uaUgOSvWIcQZe2qa3PIkCrV_3WyzDlGTTWJ509meY6fF_NS3w7tRqCxtSfgLFYVeFdbv7b2fzUzaeSNp_hSbXbcru-evX2ztCjQscO-aJDU0jYm6cCG2QYcr1T4n97Xj5yFtyg6IDQbPyooH_IR7xGGiKt2fmL5aCBSzsPPdSiJ0fvwsO_KBa8urrNjjnz3ZNBGm4EqZWvvJByu-dzjzbHq9o2OlS8X3Izj6oSNui1f7I3CJPBNIX2z_xz3go8N8a6oUFVBwDZwpRWmDDnSNLFv8qqARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5SA7aaJyweDnz-o6fG6JlZtf0FcDHxkckmQap2JD2G_UuxlERT9JZOu6axXti5upaAsYU6dECZQqxIL6S5JaEkHRNMsEob7oWST07hDNG3e6pAXA-x0QNNX1YjHKjfxSyjrrkwINeoXHcKOcMAr7C45KBq7YVOdP7zfVnHOsF5mT-PGJRzUOCKRCMacjxjQ2owT5OtB3-RGKygrQ6bFWQcrm_XeMLMZFL-czSRIn-F3msvcH2OlKwyuCGBpyfZLvochpO2oThqX4IG3WZXgBAvRun_jubTqzyOT7fTpdl6W-pI2mWPJV_qzg4iFGO44RwT2gwQBx9F3Lun6KlraZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtc4DSEnQhP5_C0XhY6Y-1OhzXArqSUQzkY_9X9eWd3vQHKjc_YZf2Qu2XmPOrni2L4hkRhclm435z-iu5VKTtLFpdhYlmpI27DGNH-tGTflrWC7hUfkxydBMiidohTu4UIAjai-AkDz_RXTDGEIMzkgK1jhjyAosy-x_VC_meyE1dAW_YYs5vHlqy35ZNr_KQl92svDE-ch0Twdi7bs_rGDFTBJzPOuBtsH_ms-BOwjdEVFa7bAIIMZVSEOJ9vae4-nSM11mDVUE6h_DOmVW05l_hU9kwNnWp0B9sgKt76k-Rqausas1k9pw9_B4IqZXUrtt-LpTF-Aes2tppmHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDtOb7FJoQDnHH0_nO7uokMilaVaWvSrUsD8303CmfmOZY_lQa3yoF4M1Leso6zklwsR5sQAADIHI0cskFLd4736CtIg8vudEMhu70NfDahM2sYMo5pi1BUvBgxy6_JZ8ABa6eO4iRrQEPdfgCBwvqKn6wYD0NXYwrl4jAIL6p5oHvcUdHz9PlYz0KFicw_kF9idORSjWBVaSxEXnfKoUBW-2AuIwvxJj_GZUwCq1JJymp6R7ARKw4bjXn1ttYPvEiZo300l95IssuJMf8pEJac1w66_VzoA0_rYlUC8mXUZfV4fUx_EhB8q3HT-c7UwPdzvhxIMRbEUiAvOPHjxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=vFv-ffZEpMY-ST6TEJlBZ-SBpg5dP6HcyIitEv8M4QapdeP95WssS83iRyvi1G08YX_K8ynqucCHYeWmJU8kLn0LtEHa19V4O7lg1j_mH-KQxOS6z3Kq1FJWULlGBvtuuZa2zBOqpbVFn1ZeKonoU1MwRK0jzWmVQUE2Ux2Rr9rK6ck8gJVYbt0KXCasYldM2yhrpG3pb9bcWFjJd40bkgX4YUa2PfcvlbtP2R2zMB03uPhQViYh08hhDc32JQFg5mSSKq0q6VIa3gGSee1QRoSppkDeD6AACdYs82CSBNsgKwJHyC0Rrk3rgGu2H4pSQ5LOexQq08J1iRIT4yq-QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=vFv-ffZEpMY-ST6TEJlBZ-SBpg5dP6HcyIitEv8M4QapdeP95WssS83iRyvi1G08YX_K8ynqucCHYeWmJU8kLn0LtEHa19V4O7lg1j_mH-KQxOS6z3Kq1FJWULlGBvtuuZa2zBOqpbVFn1ZeKonoU1MwRK0jzWmVQUE2Ux2Rr9rK6ck8gJVYbt0KXCasYldM2yhrpG3pb9bcWFjJd40bkgX4YUa2PfcvlbtP2R2zMB03uPhQViYh08hhDc32JQFg5mSSKq0q6VIa3gGSee1QRoSppkDeD6AACdYs82CSBNsgKwJHyC0Rrk3rgGu2H4pSQ5LOexQq08J1iRIT4yq-QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLbsyqOia0-i6XgEFKFK_kqtQZL7st-3XEslXA3MGhi7UJt66U0edKo3mUPqfW6Swh9uq22HESt09Mrt48XpOYiWfcJeXQdtDfPFj_zki-iIIqJ0oKQfv22lN-cfKHEkCEGD4wPVqiOPUW1SZ6Axw0qMYhhn6qOFK1GtuemV4dCoG_iY1YlFNJcuKqej3WwZ99v209xvC1n9PpyvwzSTnAWCryz4Iqt7Y65vohplhMClW8YAerWChRtpFXEi1ZA3DUu9XxYGEwIOSTVpfvuB2CTzals7ZEJpO0BHizMDXkYVnDCMwTJG2nKF3p9v4hVROGLFTtGDcx7CF4aTzcu6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorzkPbVQXCsv-4fBozEGYzSkYMedOKTi9rWzJtnU5v31htDk9BqMm0lhGhOUXe_RHwauFW1e5Q7LbnX1dUQ567my3-xLcjvXLCj3j-kMaXSxFFZ539J7XFdWJpkKIINUA6vHM5xcibssaOwGeGCKgCH8UcvScUL8G2I1DpYiKmWotlArKOldFixd2jjWfwe5lZpBNGfP__cUYIPO85JlCn_U6hrF9yDlFa0F2ffP620FV-kvlAZdM80VDKerpmSIyTsPL1IwOkjXmtjJNyhg_z0Bt6PcPOsfeQaD4Fxt9HRNHbjlzTKtr1sglaUaebiTBdgEjnMGbJ7v9eMFdgr8IyDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorzkPbVQXCsv-4fBozEGYzSkYMedOKTi9rWzJtnU5v31htDk9BqMm0lhGhOUXe_RHwauFW1e5Q7LbnX1dUQ567my3-xLcjvXLCj3j-kMaXSxFFZ539J7XFdWJpkKIINUA6vHM5xcibssaOwGeGCKgCH8UcvScUL8G2I1DpYiKmWotlArKOldFixd2jjWfwe5lZpBNGfP__cUYIPO85JlCn_U6hrF9yDlFa0F2ffP620FV-kvlAZdM80VDKerpmSIyTsPL1IwOkjXmtjJNyhg_z0Bt6PcPOsfeQaD4Fxt9HRNHbjlzTKtr1sglaUaebiTBdgEjnMGbJ7v9eMFdgr8IyDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvU68VoREKjHDnRMAVkcIxDz2OC_DU_T63Nnj3oy1NU_gesEmCpR0jwUfwZh8RzgaByFSia9uSAWehUqAlWSWeDhOsNBZzZZ0BOlw8usKeMShZyqTzF0olykfRzCa8fvxl-rNczonxR5CGd5Zp6vUzYlk61jWzIQbr3rGOJ4d7jgYJjfutK4bpPexyqgNSeX2HXVqSIA3ZFJVQZcB-zsdU-l0ok8g7JuQlP-wxAU7x3avpE430s5DuH30p1MJI_b80n2h5phr2ZUq884dPsittRrB-WSpuSm9H5qqtZmM6SNiB5acreDUKUywHDEorimQuUWUOnpfe4VKLHVN584ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP2XeSJxfuqwGEc_w5fCRdQVyGmgUliVHtTnmCTbcmcB0IQTldUrQb_fe0HACnO9uuEps9SuzHfHpxx-XbXbjvvf5fstZsMPFKbIXoLynNdLrC86L7VPYvKR2jFC81h3ZAcryuJ296XgTceFXh8pfhwqCs2NG1kU5HpWzEudgEG5vE3GcqyIA-o2BpEq0sN0r2MMhNUkoSkWU8_dnFtj-gt88pTgefQCd5784iqTFsRZUd_RlR2q8D388vVq0cGUpblePUK8qEuOE9YkYfwo-DPIjTyR6OQ6SaW8YOeXCNoob4vNVEfUPSAQ0zCn6RaEKNRHo-o9P2y9ZIxyHTVEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd0V0Jy3cVaCm-OZ6V1vgdGIp5wJgQiyFYp_lAmqvx6Yn7WbGBENBPZdzLxtLGj-jfsGYxNlsa3bQckuo126KwNenlefsjK4WWE14VHZfCvIrw-SrsahPCcr2Z-tUJQ5FncD8vOV2YdXuUhUZxGfiECSs7oi0hZZmgUKjzaqadt7O8W9KI4tHY9IO9FnVMAWcAtUy_3bg68ubk7UqPE1aNU7FuaHT1NLnVtMyJesAa0wNs5oOBF952oRi7wfAddIG48C3NkOpJoH2Uv4iBZguN-QHPmoFEbomNZSHZSWcN5yt0myw1ZQuZUSYWAlKvSJXnTek_-Bh1t63w1yrlLDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjcdHU8X7IMjkvRBonBzhNixoEcB1M2Gr2KHGNj4rakSneEtJgdA_oi1sVOmQSUf39rBbQUpCgYiemrqhlom0pIGXjSbH5fkMnnBKyecASNlkur_NHngsCafUdXKjaMyBih7luoup9L_ViUIlFgXile-lEgSnH9kP6nqMafrpum0i1StdZeunLaddw7jt1Fuj9TrXZmOgEtqoPvR-vulOOPjtVKAzc2jF34YKyEFCc1LgDTpy62Ek8N32W3xzEdPg63sBT3BDYDHhmwuuNCeWH8q7V9gdQcJJ3C3GDetsSyd4ALNOE1RYVwoxOBDV3QwZ1LZfvbb5AUYqtGzCMFCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-8AadejT5AlFMz6EHUDv2sSdogcvMllbeAcmiqnkULBEQH8G-XcVh3HhxIY3Sf87xy5S6PkZyYzhEQvsWn61o86ygJvQiMkIbukcdgE7obqecdeSvhoZaXffF30rNGMidxlBfMhTuaTV6unDcGyjXwCoVUgm0HoHy7gQxa9cvf1URN371ewSpvFzpS_9Pvx-xDqdIKwqq1eCyY4FpuRvQDoFLWub_CCHY42hghg2kucYPdBb3tGkg9cSH6jraRP35goTPw2l7bSljYuImOBVE5T8VTwFabTCXFLcyyIF40Y1Q9tTHXtUk4YXCjjm3ysND5hy9cknNVx3ha7Uk8WdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7DETAatuiNOY9byzPTM7_FtMYf4iD9QDCoN8nDxnnBNaljol89NsJBw5khSAIANTpRC2JYA6W53A8zrtNEsEL_OrO5oiXacJjPCYPGLgnmk0hYvbtdHLev8eEYHwAmfjaZNPd_sB5aQw05cx6G0V66nzgv2l4R_hS2tfhmQU-AmAjNPRPQRwap2Pqg864RXr49an1sctjl2d5aXmtZkopf8pefNcYmYKXWv-QyCpaeK4FnsImg61zxmp_stdmQ6LTgaJ2uwWpV98-_Q7E8Ii_S5xoiAGr8j9l1EtJaJVFW5L8ardU-q5tyOevXLpBomchAgTwCYVEDYxi3z_AJmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4y8Reu1yi_6Qdtaw3tF23LDBlSe7IVAADcU32Qqu6cbIclDiRAdM_df8FcHnwUFL6ZFrGPHBrVWVZvuZVhEcjPCiwi7vavPwnVDJoPeDIU2E7Ubo953YQ_SQ9KoZajjINseN81gTdWQVCYDXtFQM_Fm5TvQdIotsHDyRmq31arG-_3XrbjeM5xzKFA8bqDvg5c-DZFQ_ADcKW8j8TjKPyjska4UeQmcsN6xiLtkBzushEcZ2VA6XATElMcltDfEnjI0WTYH7Dtc32FqiZp6QzArlF--4xZ-y3oEHXtuX-bqpC7vvPbgmO8-wmKPn4-YDEvlh1r2YqZsp_luoOWmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YasPiikppnWYQxRLeEWEfddl14h2XADCWn7BlHppBJR4S4sIVNhze240dmvLpeWaQltZldsNnRLlIq_t4qzBtnG77JL25mapUFc2usdKztuJVFaVqv1aLAfGXFpjj1NQRdHTPZDVSJs5K682BCpwdwiFSWJCS3Pj997X6l4k1JurtO8uTStp8mhW59Dfz5u975Doqj-iGmCNA-7Vc8_qVUZvk9zmHm7E29aJ4GGOG9ZBrW5IaY1QsHbD4fc7q3SdYz0YTlcOizUbu2t7QGkBgp9BeVVQCzNDQ4Ff-fYONjTxh2GjfsONbYuAgPWwuQ9wszRO6iU0p0Nxn-3gOy3k5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJSQIjETiXr6IwvDTJIpXYd7QOjXOyqLsiiH5BW0L4yeInMDf9dLVRq9LAfr48kAPc0ssl85PfQNn0Nr84XRzMIT_m-D_wc6KeobCksrS8E52P-HD6Y5sc2jBly0cwtblP_1MZmmmUkgbecJEPNU6fPDRYOyw0KfsuXkixLWGZk8v0rDYkI8-Gn5Nc-n_oKd_iM3hl68s_NUJMi2lZ7DXI2iG4ejrBWax8kcVbSWGzX6FVAafTtcnXmgjkXde2Rq4ZVwUvFOiA577E3SfByWVVRxlWHoDEny-s3YED-X-sQXgq02uunAI3OGrkeeXZbd7AE4juneC_Wymy3CjJCk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y961VtI5HgyGOXct2lbKpU1yOYQOzuyzGWsBiz-rRXD7Tl7zq_RKA6sjyDH2nCXx_XksjUfAS46p7_Iyo3Xn1qRfq77R5vW4TQvPy4UIFGVo7CdMt7HK9nQqLlpv2VS9LhCmVA3R05d6qVE-wAypGEfU786rBxaQLOlaneo6mz2El5pnODJUeS9x0RD6yTS1LIpjj7-VWv2jRQa79t4ujoabRahHwFuTx7B6a27aFr-nTMcsw4RZ4CKBPaJrgF0DVs0fI-SMSkhhTn_sf4bMWBA2Xbw-3OLN-MpkyXaMf35Fk0I2bO7KIKeACmZ4f62CtzJF3l8Zs-Y9iAAef23iYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax1frp4FzxaLlpouAtxubC1njt9pWMzwVzvrw0NrbtbgwIZqr8JfBCKkCUC2xymwPaorTjTUfvO_Rq5CLzaMZ5bSMkzVEa6ObIndL3NVPThORUWhkUgclw68bccGGe63o17sFt0NbxrtSu460jn-nIUQ3l29T1tMzUmipnoCA1lqL6dmn_QcN2xthsLzrVG7bzUdP_qN2qOP0_qCpOynnMjHLYgjVhUvtdcl3YuU_2h9mqJeazH5h7T1sHZ8mvmwLjrRXiX7hOnzUaM5_24tSpYAMQs3Vw3szfjcUVzyslIV47LZrtWfjC6iCPZ87Qny2ZyGLvhc2YYo6bZBYH9MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=Fr6RvCZbpfD_TOfl7x5abYTLvcxCL4hARNSod5CO5Bz9aZGh1Krr0ADclV3IXU7OFMAz16ew-Uwj4aw1P2OwhA_b3SblNUu6Xhi6zdrs6MNIevxfE3Dc8YDGLyjx_u44qQceHOYW1D42O8DyxkiuHL6A3aRefpnzqhp5fw-dmLjcBtVfmtBod6_8A-XNy6MZ0giRPyjwFME_oFDURhcVXqJC78vKfcRBLM4ogbnzNBqvcUYMyEwgLGG4Yve7f-KfDMVA35yPMCIscaq7HO-oXjaDNA0m5rQyQJpowqkYdTYJzs-M0_jLcBa60vu68HslYzb3fsLlSti51QLw62rKFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=Fr6RvCZbpfD_TOfl7x5abYTLvcxCL4hARNSod5CO5Bz9aZGh1Krr0ADclV3IXU7OFMAz16ew-Uwj4aw1P2OwhA_b3SblNUu6Xhi6zdrs6MNIevxfE3Dc8YDGLyjx_u44qQceHOYW1D42O8DyxkiuHL6A3aRefpnzqhp5fw-dmLjcBtVfmtBod6_8A-XNy6MZ0giRPyjwFME_oFDURhcVXqJC78vKfcRBLM4ogbnzNBqvcUYMyEwgLGG4Yve7f-KfDMVA35yPMCIscaq7HO-oXjaDNA0m5rQyQJpowqkYdTYJzs-M0_jLcBa60vu68HslYzb3fsLlSti51QLw62rKFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxcP2CFEnb2k91J8okb3tf2w32V15HOHxZODUw0oNs55Jn-jSWxq8kGumRyrKivngHxzGuNGD-vGYMLZz4DgM8IXjguuUXitPFtbEHEK4mkXym-L7iD8qcpXOWQ_fJ-ng8-HmIs_J5ku_9sPjSqC6wTevfOKB2eF3nu2y2xuomCQ3fZlZ_3j831RqUoBDQhvqFFlvPCLo84q5slfVGXtpBq8KH1X79fZJqL_AvZBuPwbSu5f8qT6lvA0ZtJaPbxq2Btfcgvkza9_op1a4ZD4HbT4YJbiSw9yefQVRGEm59pHVL2xG2FlXaDdJd4hCQG56xO7ibp8Z_3WKAwoKr7JCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL9k2pQeBKDp8-F8lKMhMV-boHaXmaJpjZf0YzHzsWu6mgeVUCVpEQzEVN_xp3KXhrV8Wy2qRx1mtL_DKTnVV_nu0-L3wsZRZ3E8al-2ANBLE1qIvFuTdtqHhH4R1_ivzqWjB7yMxsmaIOlA-GqJeadDSktQuMe93enJKJHA3HVwx7dFi58gkRzZibBT9jNeTC_MnCBhn612FltHca7-FfoJPQFGP8eWj8l1_T4sAa-7q_urIdydpI_Q6uHVqNIjlaiVgo4nX_XM04y8jD7aPZirr8eyFb8SqmMef2XJ-FReN4MO6udP9uWUL-1sKLX2UL7lCAaqVia_JsZWAleQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HloCbTJtFTmQTDEOLergZYN0y-NSajaCuUnuHaWQfZTMOEG3QaEAqMvNXGZA2SXC1U7Xlb356f99zk-4zyHR9MoproX2OxGJihPrjtTR334Eqoe_YfxTakKa5v_2oZv0yaEYbC_fVhYqf7GCXay1gnrNLAmoeIz45oLkyMiUQd6_RR1BRB6f6TEhV6R6r46KvLA9IsFD_QS0wAD1avCNZ4Jp7TBmYi1tM4RZgtqPFVsnVgLiVpXt8ec8HQwICxhat7D857wluTyyV4qxZ0aHTleHHIVlvB5mJ2YqQ9FDH_0lIBjIWGeFCZgqq0V9DTg0HDsahZwvJsEADiP6V1Hc-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8NR-Q8Ktsr7_CIFOpSjojMXQiW182dChDWjm2Ex6F_aKUmciWYcKy-uTDNAIIEuvJoY_LqgzhrKiAZhOHHdnZIIhoQ6V9MNvh8k1KOLOJUtuhSeJ7-ou__bc7PquyKda5lnBufkW-6cE9tgZ8C2KlenL1zdlZcww_MvHm2aPwtfjH4ap9XqBhLqbeERPWcihwwL0c-tRMJd6BjkUgkmEcvo0W5sj0bJswljpyub4ADqQ09wtVu25w0cLNKEzZSTqII8Gt8_fM-dqIH73u5tAEWfIE9E4lkopzYpXYr6aC0oggvTo8FGNtbTcAoUY3PAMcfrq1Z1WKAbxrHX5f4ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8sPsIvVrNEu0bvUQVg5OPgrmXTCFBDYb9SMycA6dq_STYtxRU2hEhbsPN-Qs4t7mloYAUATPransQrhr2K4e97BFCIe3eEMQeST9S1GJ9vLTITZYwEx5DyrAADi1O0SA5nT5BqZnXDBfj9kEjJ4XtCaal8W5YZmjUe_Ai7kgpaQmtZFbTiD9RJ4-I4FgqVJXMWbohBYe5-v6GkYd7QV9GkEsUfpU9E8gFln0XRZlNPWnGJzJzzhRbpeZ69G-j6O0b8y6WqDPgxFfDagsWFl3C1UK5jwoLC4rovzHmuEN0JyK52147lEwoBf6krLK2ib_o9Vi2DZAm7ncpX99-xJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INFDqS-Qu0F7QkDfAU7moPcqL-6YB5VDTl2N2znuDqY0B4ATKSRpt_Kpo6anJV5QSvUyKlb5ceM4be2sDgG91QYu4lPotcA0rBfkpAdP1QVnkTBSbTFnbAo5ikEY_T4HKHZxfi3Wc-jUI-sIL5WWsGsLP6CfJpAFhqU8MYOgCosDKfk7P790S4DzJXzkpZqCQ-BB7PsmCfC8q2t7EgyuIyd2kCN-k-_AJeo_fXHInd1aF_fEjbYQZNgD5BcG299HhgPo_7UTchY2Ja4f4HISiVvVQsRf6UDFQzJ3_F6VFkv07-tan7RdZNOrYrdeXyYE4JWI3KKV2YEjFExcXcdIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc0Z5VYmINYeJUk6ktgWsNa_cxqML4Ayib6FHvZ3cX2fe2I4nSvnfjxzjNOyOiqxiXjrH_zV_La5zCx4h_cLBBfORz8Z8Noe1nHjNBeDnu3_0k7qpx_vgYLLzvI8Re3m_nAKENDCOQQERMXa1SohYJaQB_etzCrOyvhJPdLZ00TPafJ3JJnGufBBkeUiPilFTe9AZkJ1lGAP40AR80Id0QQWtesTqkykSjVGRYzFyYMmk3XfvL2QsVUbvYIAubyKSbER8qpuYBHCMCUM2bvuGfuV4NeAUUg0JXAvRz1SzCOrqWIpEw7dXqAjm_xrs9oSt2pjaGfeYocljeU6IBHJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=ge9SAXyDKkRXBRK_o1rEaVH5cNZhsJlNHhZj4OailYcB8t3lsvlnKx8FJSmkSa9OHb4woWF_Rzgpblv1m24KVOBdK_anpiX2tjLu5DhMkjei1vYXYGQvkTmfYs6z4v1BciI4VyasIni0AzDSgzCNzZcoJOyGySYUAmOBqAgHEIbyAZN1f4Aqa3GtufQ3Z4uP3tzHgLf-0rsSMgcpvRkEm5u5h-KcB8PLa-DMjTLNszpyLAVwTgHz49CKdt-zHyKo49xqiNwaejqs3Z4D-EuDH_uqzV_Ddr4bxBWvKTKG-KuwUzp7OpVM7Fxg-qPmroNilpVUAk5kJo2uJfLDAl0CWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=ge9SAXyDKkRXBRK_o1rEaVH5cNZhsJlNHhZj4OailYcB8t3lsvlnKx8FJSmkSa9OHb4woWF_Rzgpblv1m24KVOBdK_anpiX2tjLu5DhMkjei1vYXYGQvkTmfYs6z4v1BciI4VyasIni0AzDSgzCNzZcoJOyGySYUAmOBqAgHEIbyAZN1f4Aqa3GtufQ3Z4uP3tzHgLf-0rsSMgcpvRkEm5u5h-KcB8PLa-DMjTLNszpyLAVwTgHz49CKdt-zHyKo49xqiNwaejqs3Z4D-EuDH_uqzV_Ddr4bxBWvKTKG-KuwUzp7OpVM7Fxg-qPmroNilpVUAk5kJo2uJfLDAl0CWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=uXjsytlfndukIzIErYLiuwRgJ21Z88Mc7Z8DU7WQC8E49vBjqwVf5S-yJfHnq6_cBIaKCCEbPzV0T-kent1huN0maP6D7a_vX8MSf3-01HNDGYiCVu9WZ5Vsm5lvBCvgIaMtfACEDt6PBOvUPe6CJLYk-anmryasWGepL0XlmyDE00tvwvV1qKu0nPIieawSK2J91ET-bvErTSHGWUemYYMBamsv_oWpqYxbzvEJbVd03y5LF-RG0xZaGW6gVTXhx8Q7ndX6lY-VoBfEaUnOFJNHLgCOogUDH18b6zcOvyTGLlDPM-cqSDMvxOmpwGEWxq1kw-dVCAUS8c1QH8uG_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=uXjsytlfndukIzIErYLiuwRgJ21Z88Mc7Z8DU7WQC8E49vBjqwVf5S-yJfHnq6_cBIaKCCEbPzV0T-kent1huN0maP6D7a_vX8MSf3-01HNDGYiCVu9WZ5Vsm5lvBCvgIaMtfACEDt6PBOvUPe6CJLYk-anmryasWGepL0XlmyDE00tvwvV1qKu0nPIieawSK2J91ET-bvErTSHGWUemYYMBamsv_oWpqYxbzvEJbVd03y5LF-RG0xZaGW6gVTXhx8Q7ndX6lY-VoBfEaUnOFJNHLgCOogUDH18b6zcOvyTGLlDPM-cqSDMvxOmpwGEWxq1kw-dVCAUS8c1QH8uG_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSo6RNKBX-NSZ6tJNA2GqurkwsfphBf2MFrWbbo_nS0OO1NER7G7DYx1Hn1q8Jt5pUpwf6EaSNrsBPaXY0ofMmfOBaeatRbbTk4-fn1Uxs4Az-r_eA4KeaoVy8xAIIzJmHmnwlayvvpki-vqz72v2-_SrKcVRtkg2re6RyFuXJZKugz92TlGXim5xGwcdZf0MbSePN0ZOAqguqDMiJ9Q-f0DmyK68vHIQ4FnCwTb_K3haFiXRjghan_W1S-fhhY0rM4_6Ddq-uwwLwNbuPBYT9ZxB9pLAcnAEfwttlWksa_Df168RZDGGnH6WFO4Rff7AOCQ3VJTft1DYXjPI0sByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcCV6S6RNfPwZuUVqijNqB9seFHRPhETPo-kvKoHEbPwO1cpEQP193iJfp8WnimfhGTzbIgRKtFuDLjKeTYELyFz38a5j9rXbKhjusIjM2eenqf8nPhCCSkjMiNlMbeq-xTpDgXCmpt-2CvNp2vGJVK7UnowdX3Q2UUjsEmgNuT0WtFXs5PnBuZjbb7PQ5OMj5pSi98aJ66mFdeSWP5FRsgcRFyyIqVDBhQDjWS824bOQEXkF9E2GuL0J-DH4YoYS-bg86QSAF9RW6bcmutVGJ8P59hAZcpP0jvqufEnE9SyK2HFsKnmBb5wOmrLw3VyDyBidT8vXn-EjJ0aiDjbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o92autxHe3v1uYvUKpiAEikOqylWCPYhtbRGiSBgEl8mIXksceIIVKS5xh9yzIiRi36WKTJAH-Ai0k0p-lTO8-efSGgcQiYbdbGI9UUaua0_lfoh2aPXkj2Sntnssjv3Y0MZrUBY1Czr04Av5isep_TMPdxKaWsJg23x4e6nl0JIiyCXGxmzUGvfGPCfEAKB7V6Kh64YErjzOv4wejWN21vgGrsGfraoduX0mcTp3B0vE4Puey-p09SrcEQF6KZpvxeLc2IZPO5AV9MZTbTstu3MUghNmYTUgodJogPpvVHDJyahzCAHc9iJDRyxcDkr2BtGCKrCkMxzzTL6Z6k1hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huCM9CHx96KA5NfktbDUm6NK4pQygpnSU3D3aCvdEt4GAth2HMPhhaoNO7_PFDnVzysAPc9RyeNdFktgLNbWDXuzBcByCRDJUeQ4zphg0f31wRkJ9fETw1wp3zJMAaPUD-znCngzgXm3_Kw4O8KAuTdPG9aa-r_b4BJb8pJteIckLHoemQ_ZYtw3s40VliLC88YSfUhCekeTHXXOrVrhvEC_WSDRmwhDv9noFguoV0rJvIvyGyQ5P7QZxemMTmfFOLdBuJJdZ2NU2grCfk7eIN88iFG8LzTDjzThoDpZC8fO70jS9g9pBmEIfPgomOF4P8XHr7ScoRqmwhVlpnsrzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myNzlXhdeOEawHZ9Hk2wEVAohOWuK5lLMIqCexI47yboNmDpwi8eWAzEtMy9dYXRUzwyOywNWdx8bu_a_kmZURdyoG1GUCaDLPblh_cwg1rIOtFNC0X0MQlwQZSUpyttln86lCDwk7fnzOh2kjjnjcFlVDjsePkbnAwQ4A_E59_2QmP3IZB_oaPsmHnXuFuTumiyX1Q0aKpjEbe9_ZXtQiaATOWLEIkSn-L8MBU89Dk6dmsmF_EFaPApEqhcewMB9bnhzbWsdKZd9YFXvlRI2MvCBv2ABFaHvjiDmerwjBdFivIJm33oIA4Fgv7VCxwWhRDmiWsBqIigboJtZtsPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV_P1oz8hS4HI6xag0_EjkRc5FCplKrr8DuCxmi_u4z7bPvvCGYSu_bnrNkPn5-moX_7SJaeHWevqPIW-mt6HIHRhYRWQCcFdL6p73TGY8DZ4C_77ZiIeDyQAMlgfYq42he9mRvT5Trli7kUzzrqpXmaPEEKKpRNG-WtdC3XaVF8qSzrCAJNfg9fXcX_4K08CNH1jzKvTTnTbhBYOIlfC9_cMpDhv35x9hVOQEA04eyTVAAPMX6HKxSIR_Gzo7iedTVDR8REJTR3AX2xEONhA6WZYlEd12ahLxhcGD69B7KO8FDCdTZODf1FJ_V-1F1K-biwlx__tsqoGMNdDYbUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=LmBbzub4L0JUHGPw7NwDzku9UN_d74tuSHPrSEUE9Bf737LswWB3jSZG4V18rjhZtq5GjW3drR1jg11vvewm-dfPDaKFnllrvjXqjgYfxwDFw_8TuJDm_30kJPfCZHKepLInL8JZOednMCuOctlEEtdu_Zq2AIR49rt-DbNFIYgK_GPcca-uim1Qr2vVgK3s7Xzw0udwcn7OAMJMehrt29Th6vdVAGcOHohC-oenwX6CqEy1MznxK3oS--R6fJTE-hU1K30DaBQ_ka4d7SBoea-QWD9cBXnvmCeGUx2Rk3ZGfWLsdUmu99kCaQX4ofmbwTT_sOCSHbUGehxb_Ardqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=LmBbzub4L0JUHGPw7NwDzku9UN_d74tuSHPrSEUE9Bf737LswWB3jSZG4V18rjhZtq5GjW3drR1jg11vvewm-dfPDaKFnllrvjXqjgYfxwDFw_8TuJDm_30kJPfCZHKepLInL8JZOednMCuOctlEEtdu_Zq2AIR49rt-DbNFIYgK_GPcca-uim1Qr2vVgK3s7Xzw0udwcn7OAMJMehrt29Th6vdVAGcOHohC-oenwX6CqEy1MznxK3oS--R6fJTE-hU1K30DaBQ_ka4d7SBoea-QWD9cBXnvmCeGUx2Rk3ZGfWLsdUmu99kCaQX4ofmbwTT_sOCSHbUGehxb_Ardqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PctRIgQjueSXdApknt8SnIrTetJF9D1Pqmq5BuvhBGwgpbPaTx2GSzkBAaiYH6yxVwCOhwfqa372pw8xczgg9agSddFpT2L56YJ_7kmTvTi2pJlXTOHbCP4kBSG3dE6Gnou0Z99loE_Y8WS7gUDce-ZtCQmCER1UYFnTLvWbtAEQioR-Ic5891tdA_nxuHflZEcEJMY5Go_vqdEY0N_pOzS7hwXGNVVHe7sv_n_PuhcyHC3o4svbDk7UYfK1BHCscRRRkvo9q1TowgazGN7aLF_ewf_krP1QjtzvU-rfkDWhtLQud0Xo5lGG09Ex48oRl_yKRXfPtPtat882nIbyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzdUyqtza0N8qSPzy3nxIhEadiqdympPur6U0UFXCmJo_Aq8yy8DwvANd5hz_IcD1_pKwfK3K8tMixZmk6c6SNJBYsPX8nETziUIA5uFsrqPmJpEWLXTqDjiZhMW0eE6epfdRv2cJ6eDNDK52UfEjYY8EU_PsRBrMuJiRciL_GCTQVPu9rWXvEJwkZUZjgg3B2-iMDOR-dfKKWjjjl4yul8Rwik43Wh-RrBAK6yueWditSmFkL0DKuyYpKsAq688BZfoHM_8gNQ1tIInAZcbvl5MFjDFdjv73G_yZSQAiGRlMtWB-x7_a9pWjGoOh-YKzXft6hxMgEGlwwWf9uO80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRouR7BtKBis-C_yOuhLw06WwjGYfPbKHCHSOf5_eEV_15hSwUhKSkBhtadhCJFLidkAaasMr9dbir0o8t8w7sFx4MjD6-ECzEP-sBKipb44bSGsJvYrlvOEqJzCbXJhYZpc80hdtkRVvM5ky75cwB9rSwL4JdKMPKy0anx0ULXncuuuvf2J9Ks6gKkAbx_ALa89Y2Mty283-PW6o26gh8t0ITdNOmUw2Ec-BbK4xuBpnhsbgCLfOBMZUuq20u0dF6M_0K0BIZfFi4ixSNjVG8ccNdEXTZL1w93vK1XrEc1T6E_Evxd-QXTCn4-zqGoxoyhbSQ0HQWlSu2W5YBAn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtWF6RrWtnRoUEbiIO1m5uYZtIaInMWKtVAd20v1R8tlnXoGYvDP6wMOcc9YJv31kiv1-mjCJS5Nb5MXI0rlSSD0LzNI_6CJN81fco09PaPCNVKszAbY7FSmWSrXWtPOpDkjaCWxzSQzgpZs4Fc2dCaalHX417XavTCuxtAYmn-x0WYy600_3W4ONN7nHkofjrvfHs2WWs6_2o0Unip_pzn0pH8lvnvc9UoHpYCFz1kb29a4e5dPrlYnmvCjqipb93EO0E9gRK83Pjlp8Q8wXKRlDlga_87W0h2JYeo5HV-YAUzp03z9uENKp9VeGS6iwFolCobTCy-mQLdWDdZUDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDyd-90jXOeuE5b0elGeKw28L_Q0Xs8f4ISKCdfVdumwPM9rC3Goh40Og5wmnfTUWSHtt7wXS60iojoUW7mKN9kFY7S8Lz7F_w7BW2xwVCkWG1kVaIztWqnJmJAAuz7QgmSA-WUxYpxs9tL_6a1rcj7EcQKgRIIi89SoIML6p5SlhGiLjXlTEsf4N5vWdFk-rs-s91YkiZXwskQ5mKi9vfTcOkS_EatTkVFlQm5BED3HTExOQIaF0mFdmxDyxX6Mptol1gIYbcp55ggTmAMoUurjbWvyjvLvagb235hVGAc3If7471dhQZWTDK0MEq_5W8dhcyupjnBHilg21I6Vuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK-Qydbm7MqbibJNs32sFPH21iybO-s3xEg5usC8QkvedwN6YM6AONVbmGKvqW7OjurG5ZHALnsdHNXkMaS_wjR7QodWAk427DnBfIawiPmARktT2HhNMnFjRGP9F99t4fu73kDUGN8_0Nu2zMg5uOYUxasz7FgNTYrSVFXffGCaptK5huRvS-L_SAZKFSo-6ikqbXYY2-r6L1YD3t5XYmqx-TzPFtMtC721p6T2QsxPv5tctdP8wT-3E48zDfHrz3fPZkCzyPKkCAtkfKAk_MbhW5DTDm_CBB_9GfgFGWnx1bLU22-X-WHbpJaEh5u8BxY-FETZDMQMPkT15ZVEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw88-J_k2MUaEeVoXFd0HbaXgHeQefbmFo6rbYz35hy2XW2HMns1Lt6xJV_BWrOHK7WQFw7AsdRU-iBfIGOREYW7cImjyhWaarxt2XrUBgKBM9v28ER1iDJZ1nlm1iC6DVANHSRzQj6DzWh_AX46_cfa03PR4HWFnxprrtZsVOR7GrELXLbcItXnLYwXaN7YhG-B6qU4pl9n4H808bP4D-Wat6_wgAdLj8aMSEighy9C75iXQumGiCcs9glgouv8GBwKdYujTl0wRAxnN6U54SpBT2f_9rp9EIM6oIIzrZQL9mXOKghj7u6BTvetj7wSlOl-o5WE0ufuzEyBhFSK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjtYxC55EYmJa7lhq44DLD5ckulA0rKy7Zh8LPG4btM5D4etEk1-MZNyuivRwB8UOg0GLv48LvpVvHv9LTZ9hg56-FtGU5XIDIP0xOJpRY20O2PWFDiBzHlo_IjxJmTckLU6Ek3P9zxK0al3p1V42pXZXK9d1aoCfYJh3Nqsz8c8JQKO1hgim8334wcrpCn_oLSHdpaT0IpKc6g0K8LnqSHoNDUPRE8_79kiQYfySqNFjkxdhMFwzZF7oiw-b6sWcbblu2j3VGQw6mTE8k6fwxmZPu21D6jJHBBhKGqQvbxXvoJcXs6Fce6v8vGF2icvI5etbvTkz05MylH5Ygh9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0yY3rs3yxFsMfzFvwr5lzxT3_1uKHerXa_yYfjq0iPEpEyHEQQ30QNzLM6u0738A81KaPDBQTC-XHB2hIp6Pv7MYpjrzTki8lH79qMf0h9V7dB5tg5Trb6frFeclj-BFuTHRi2PFtkcTz4x77UJiYj5lxJAkdVKG8CYBaKSzKx9YZ12mticZutM-oq-5BUUOpEBq3lPqJZQbaD7AnbV3UaH-K9LdeHI1XWZm4bA6-jJUtb7nDIBoyLzL57DvfrFJrRhltJ6EQYnqgZRQYEISGmT2IXTwR3r0Nu0md2jFUkdghu3R2hH68KZEpL2JyfnztrDf-rcSziQb2YxWDQr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Mbj9YHO3FB29NHN9eKO2ZiFH5ohs8WOoi6BPPLpE0B73aemCFQIVYwoX23t_zvBYRUfAUG_QVzYPSai-KvlsrARiqX5iPIuO3onax6IIYG7hBs0K1v4P_Bc7HxcE2QbzGxClKRFgwcKk_xn8CXnMQ_ab3IyMd-2RPTEdGVvMlFw7OdRlK-D8aC4tCcTBsB8MhDRHZCjK3rmyXXwGgxB7ZhzXW17DMWAZB_T6JkF96VfDs7ElCdjDACxDmMTT5_hiVVrQ4IAgrxN2iofdgJkxbHf9N5C7csbJ2qKwPj1xpfHBZhyFwY7uIRuzc7pZkSk2e8gEpHPiDF2zzNN0D6qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=mnBne-aMW3aGYnlVIMPzX2iZnBArRtNctEIDvqqhmPPOHjNOndno0-aNFNSklfZUyJXm2LdY9vtLnXZVG8seO858YyXRzL4RCDjaBQfmAwZlJKsHYUdX1vFl0jb3M4twqEHpXaRsntFzV0Mtl0l6smPElJZ6C94zzCGKvQW1MtedZG0pIt6gVoX1ZJqgK7dMWkSiINJcK7DshY2YfASUCUTI3D_dIxwNPXhy0IdcqHWB0VAWYVL2S08LaSkGxKnnMtkFyA1fcDcTSPeSwvV_-8_s0tNTa_E-PLjT_CDFNuEkJ5TksnkILAkrBoDYNoKtItGKV-Z85L9wKc2ZbPSPjxTSvYxdvZU4FavdnazaFG1ephTR6DKB-F3N9RUo6gkzuOsMY4iA4HfDguhdwTabSbo1PnQWsrahOGKCjUTpLrgV2cVMw2CkAaqTa5It2PGO0QYQiFG7H1WFNfUue1zew39fMB0E8da_Ygb0sMcHCv4raMQ96JgrVhi3rjlj5NiTdg7xael8yRjvw-hgB8MbDCJq-KE-9P94li7-BPaZknW2APCQmWYMBP3qGstLOvHJ6MFkbdzv4uCTqIpl5n3ReU8qA82VsN61kTeNEJbYMQXW5kr080gazfO7YbIHSUEdgj0deE4aBalYK1Z0kJ6I-qXb0AG163LU5KlrF8B6PYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=mnBne-aMW3aGYnlVIMPzX2iZnBArRtNctEIDvqqhmPPOHjNOndno0-aNFNSklfZUyJXm2LdY9vtLnXZVG8seO858YyXRzL4RCDjaBQfmAwZlJKsHYUdX1vFl0jb3M4twqEHpXaRsntFzV0Mtl0l6smPElJZ6C94zzCGKvQW1MtedZG0pIt6gVoX1ZJqgK7dMWkSiINJcK7DshY2YfASUCUTI3D_dIxwNPXhy0IdcqHWB0VAWYVL2S08LaSkGxKnnMtkFyA1fcDcTSPeSwvV_-8_s0tNTa_E-PLjT_CDFNuEkJ5TksnkILAkrBoDYNoKtItGKV-Z85L9wKc2ZbPSPjxTSvYxdvZU4FavdnazaFG1ephTR6DKB-F3N9RUo6gkzuOsMY4iA4HfDguhdwTabSbo1PnQWsrahOGKCjUTpLrgV2cVMw2CkAaqTa5It2PGO0QYQiFG7H1WFNfUue1zew39fMB0E8da_Ygb0sMcHCv4raMQ96JgrVhi3rjlj5NiTdg7xael8yRjvw-hgB8MbDCJq-KE-9P94li7-BPaZknW2APCQmWYMBP3qGstLOvHJ6MFkbdzv4uCTqIpl5n3ReU8qA82VsN61kTeNEJbYMQXW5kr080gazfO7YbIHSUEdgj0deE4aBalYK1Z0kJ6I-qXb0AG163LU5KlrF8B6PYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
