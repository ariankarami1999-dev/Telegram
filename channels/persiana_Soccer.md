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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 14:12:51</div>
<hr>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7rOnYaNqSM3-x-3e4Mi-FHsiG0ewKdbh7iHfgsbP7nDYtG2RhiSWXk1qi2QOj95ItR1aog1403wlag_eMNJoNeXdoYyEbl7yw2_qP_PNiWtp1GnGQFcLMA_xDybJ0GYs81t2a4LUrwDgpVbRvXZQJymnQFDzxdaRVKdUU01BHqtu5QXg3nziR9sET82hb1ikAkMJiPNcQJ5wv6trZZIsfV_D8obE5qVVwodvzKCW9nXCy9qqPt6CugdCUn-OG6C6n_p4apj6MawAxit7QmX4Xx6qsRFsAsY25lIi0qfnYmP7SpBP0jqrwEsdepn4StGSpw7jkTzTK3MH7chi6NuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMKLV5drrJ7CbxX41gc-SYdLjGiY-UQlaPghJA8QtVTTYBkywbPVT2dn0HQMP7hyLK5IqTRpn9CtDoIICa4kDZB3awe_pkFzSYSLyb8_3G_u2gNHEOhg21FZrrt7QuK_UP_2vpDOPq2UlC7tV7GO4nxXPmxuGO2j8-tDbxAV0X8EvDu6Y-IftNaXqKodxukeQdha3Sw1sTSiloOTLmtDtljEQdiUtn5uxtnCd1wb7w1jGrYhW_JmgkMKDOBzG_NnG3q_Hn0XjjQuWfAlZq-SgxHRuc8qfypinxw6wa5BLhSCGQS2bYUN8gLQrahyDrqqcsa_RNSSCSpiu_B4JNUmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzjIFUHcTm7S4qWa9hLQF5QSqLmNCTCkfXQ_8jvs2dOTyZAkPg5J2FIH2I57IQOpgPQspD2mID-_HdD-lP3E79m-8wvJfwkMPWaUieAor-86YfGMR6uxjlFF2PEh7D165efizbeEW0eus9kgs0xxWbAadmADXGp2EhzzOGKO61bJLdNWREMwjr0VqWpUCZIQBezXk2ZqX6RUGd-IOl48WDNcK8lkAwI_cvUZyb-FlhqX43P3rfipWLProsLB06lJ6z9pUhJB-YQCFgQPq0vhSzr0seL95SH3r20fdbIlwgaG11qqWNP7xMOZoXPhe-teFc9hzSK-2prKOsTxZ8DsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/persiana_Soccer/22134" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7RDxvC66dKTQ1Wt0sAqwCXiWg2IFf7ZfjtbX6nKBWY1BeXjF_XiILB_nTK6_6zEIaWeTyiktX2r_e6YXd3uraB2tVIqFjnn_wb9zxMJs9Fd3vPDmArdMwIksTsYeKD_h2RssTC8KngsoIR9KmyNIfiO00blpMR4tpSvIgiUSS1SnD9TByiOWC6amZWz8X56INa_S54uEwKSywwxkzMc2K8Ppzq8JM5Apj9x4QC29lhATffFQj-uOICFsOxBq5Qi5T0ZrrlOoUy0czBpF2gndjMDbvJw-mArufTfCdNZvHU44JK9GjkQZPEyJbsHBdbMBvmbPu0HFzvLm4xRy4MgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk70_6mFQl9Ox_2mb6XWNNY5xHA_MIyyBKqh321oIBID4uEjyOIEA2OcPXj943ami30L7j7cehiTUsIgvlLobU6gdIzCljRYPXu7nlcV4SWTyj9s7okliXkM0y95t1ltNMBckuLmOFHhN1KQbiZWv-AA-x85BFpeyXt90ftBhk-qycfGzoyt3v803MtsUWUagIXEurlgIrNEroQQGsZPgii_0TdNHJLr5EOPlL1CsAdS7UKkU7FB6Csz3Bgbq8s9U45-j8ESrd5AzwRPnbX3yHm1r0H2t2sJCjurHPW8xEihxQX0-53Lqb8Ul8wFhxDlf_h3lvqjZn8iXaT5PMQ2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFpvvFy0UB_WwzA4rQNEWdhh8gtmWStcjgzxhHqksXtWZSv_5SQxiaTwXbKChaLPqvR_NBWyzqJOb7_qrQMWsrn1Y2Gx_7hC7eAdbtDrgiu9lETLGUapz_fFkVfkNUI8wAhx_FI8uLRGHUwYvMk2pkpyzrZrzDlkbQY03eA8XJvFQNoP2XZly9c2UgZQRw73bZIaMpIcJVwT1JXa7MVOVokfo56nkKUYnwSk778nE2zMEt6v7wcUxRj8GUmjVFIzE0FCdzNHQtO6QYaXv8XYUsRbIpCmkYHFyMGGczpqRAU2hYXWYheAcX9ZRC6sUy0W1_h8m8dKl6Z0_FqSt5yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvMwPm-QRXgeiA44VhXcmxu4vQJCatpqA4HTVNlW72uFHDbp6J6DWT2VmeEIJ1PT7-2pmf4VWnQUfqKRMgKYDzrmZjaQ04FIvNy7Af7D-eS3spur06vgKp_hKzGfj8JV5W-HlBH6dX6YMnkHoBDLeToYZPKHToxXKWLCc6Uk94PrsEyT8pofYQisQOhAyUQ_cJlC65QLxAQV7jepUkK_YaAX6MO14dIA5id534sBJ7fI8Gfn7SMQl6YzNWHVmXgxccLuRy-ACKR6qiheYhgI7Cny2h0A0_0LxTqXg3gxEW1992qQp2OUASVReB1HnaGQdlR6zbykGqPAWG9XnCbOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8XcOtst7VVpY8r0O9dtEIHmkL0qzEwnhiBxtvpJYbMcPC42Uo-4j5h43fledWMl7UunckA5nLJpxdgnamBLs7zymmgeUISupfevebD0gtld6AaC6nTyLpaE_M6uvul-O2eYDhtb4Z8ppLrzs4qEUUWxo8Up1ijWuMTFLIqqs4DkvVtG-4U9AmXitTLAk8U7g5ez0Kf67OOknk1Y3IedK7KVBeSWD5wzJRIu1CO9Lgs1VFeXUVTK7e_-dz9de78M516mqMTL32VAhO9wMw50dWIaKocNAZzevShds4ZlrxoxQeqB_gERAfedOUzCx97bOOp3gLKngBNjAUofJgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORGSskuYyOPVS0-TgRAEc2s-AGWcefXloFZgUf_2RPpm-5KIlW-65yZ1dqjfg7z2kkH17QaVNN9o3Dhg5RaAy7OJ10yNm4tvpp1C_2U3-HIcuycbj_mHuQZ1bIKT5cd_clD9X8PEYpunQVHfTH2BagB26V7FkqtWi9jFP6yCWDyjGGmsplsZ0nTNGElPIn4xlv_PbS_ymdwyXaBMiEhFg3kvNORDYFUneTFU7Nk844GIXecqXWcrMdVEquOp2rgBrinyEot4l4HlgsVMyaocj3zV0xEo_YisZLeLSpEb94G4t7IMZVd78YYYw8bpdmKF3JLV7CwOUueQKnfu4QlQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfzjtqSTUcwSwvrFD1VIyVc3DhYSc2BnEKrgKRKv9klvpm08xHMO4kiKoedTe-y5eRoX8e0jyMnmvYO9zQFbSVV4srveDSTJqdu8XyScFgJk5VoVYZ8UY_sNC-lJ5pH_Pi3-2TTFnN4FNRhcZGNdV5eEhM2Uip0Wfzp6iN6QbTpx-CyzXiH5GRjMAnprbdXsvTrOWEGJrH2ICSyS4PwwyKMU7Jbr3S5tCkTmpxILLpTBDkTclZThIrWe2FOJufWx0CWRV2BUo8EkHO_DDJkB-4WxyPcoXEIb8bqDwA-QNCPxsmz-Jjfo-Uze4X9siYOARuU62JAQrwmvC9eFLlRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfSzq-2Q6YKC9WkECyfY5KMufuScUopC9Y9CjMac-XiNRrHoOdSbilgMkJ44fKtfnM37j0boSi0oUCxeyaEeGl2XqMa1lGSxyg3MGp-swxMzcjz2XlSC6XsIb1rFTqJSeRXa7nz7s2zHc7e4X8qPdMAjkwZarezCpNaI5XvrbaTI1ka6MW0FrEVAIg3X99t5bpKaTxPxb0Z90fPvainnsJ2d8SBk7kDsf4l2952APF-pXbujQmeUSNoLdCabAzIVclcGKjOBX_B3_ShYr03U9oU1VV3jBnYLWT3fMtlaqb767cqIbRbQ4GvtAxmS7xX_wEwdG0BETzk13YMH-7HcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-aS9QoLWdmidC7uZgc1VribhUPHJfDQXmmRsCd_dan7hr-m8t8lE5jpW13z-d7e9dzgngZGCZl_8qOllGYwnXyNxDQDDQGAltbeFl5Ru-oVIijW-wOl2-K7oTUB0CU_jdWkOo_yrm6ThtGBahpfDyOQlUL0qnPMopBJYk3ZIILDJ63qZnDfnC4Jk9D2203sHJG5dNkBBDRu-C_PJoIEpcbZvfzJHjHaKj00mVk09qwUYr0qh3lsZnFXgQy_wZcSDfye9bwR2om16pgozizRrNEO6pfgwXK5nQIU-H7Xyj2liIYTcz9X-UoP3BJdv_OuDkhGRlgkwM6HrvmweoqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upI8cSriONBh34NdwZnyZSvqSgB7dvLEPYe7CSGhH1AjpfbgRu-zQIEEdluaPxFdGzxAbLUxq6hIk9CB6V6GoxMHOkHS0aU8GOlC8rPUZ1OvFwimnS0DyXklqlTUu2CBzAS5OlWnU-zKrqY_WEVw-p_acfnO8A-Kk-A3ONG6H8WK4klcIFxZMnLFnhlwYcBfMwYpMGQ4kpwEgMnjQaJsDZ07Hc1HpLozn00hFXCgGjbDLiHEHnRhiVnMaBrFzT8m2VOkKac6vk26l1MfrjMTndXXOpGellzXE0Z9w19qFdpv3rviQSdTdW1CMisPUN-bg0WUg0TFMrizNkXwpjslMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aSBqJTSKC43bXdXgdWVFucMgedfxFBTtRoXJkopKI_obBdXPtcjkObhyF9_V4CIh5A6FKYS_pJveLdPruMD798zingKd1lIS_bNVb9iuHE3fGclA_sVBF4Xq--K9Te_tjP2eOAglwSjOfFPc7q1B56gqniv4pxhmoq2rb5fkYYiOKODCKGZAhtNdMeSI6cprx71zHz86ejzHYa2FJ3PWb-yjOzD9h_Vdd8wR5Kv6U73ghj3ma8ynF6e4LIO0fF3uwjwPS80gKJC5TOL9pxtcyuc9D5HM1YZw8wYR9h6p1K-lcdpvMVVWC3vclUF_hkBIo24NDVLJzjnV7xma6DuKkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjY_iB1N95n5FnTOI-dbNxBnan1MoHllayXWQ4CagFsN-Z-XoK2OKqRStQRNnkZP8u1OElfVfjd1e7au3k8QMPSWiVw4_USCbf26pW35PbiJXkruRuO36fJ2NGsvvc2ps8650xD79fukpQjo-nrWNHRvMVnoYvSZXxfALxKGkWRYWyZyi0U7GXJ2VvfOr9FCnIxBAzRWZ86My5iXUDCxq-1ODHrtLFZwg6hDtBmzOUgfB-SBWqmhNwbB-b9W3grppJefMXOi3ZeYOj2hj388GnZxx5WD3t__f80zGC3LwPLAu4TQMhOho2h1V8T4k7E9PtZw4nGzYWiToLECVMGEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rusbEwlwyV5fAoCQNV00Of3qiAMUJ5L1GKwedPDLPFucaq2aFcwpks1RaHf2u9DyA17c_tyFqgFBAmnPQ1kFpVsSD45U9hBGjWNGtSA09_HilE5luPTjlbjDfWbhua2EGeuRN2_3g_qy8IlBVcGvXduAQovQ1ckYyOi8RnUDzEvHrbqtYYRboCZAu4S9xKlw5hUK0NqCa7PFIj5wDT9vxkqQrq49gZPz6-qW5MYgiL-ycXQ3R_iXJc_KYz964NIyvi4o9rgpfdz3QiVMWqog-heDAObxMgVKTtDAh0Qqd-nQRQFeVM9Wg3UE_yRwhNWlnzZjg7q8lpbXjKyV80Pl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHdJCGKTXXOTx2icsstEETZp6zE7BDl_dVfXelEFeC-w00X_FC8DQBaizZrnn3WtRxPsDAKu9u-SuFIoZxohQGY0UHFTHL6FMDLfJIrRlgUgqxodvW66Ti4yMKaZNY-xwZUDFCmiU_PhGXIwP_b4vN0qBjjlo-h6W1rL4uXi4qFsPvmz1npc--5_sqT2XN8U-nr8uURo8KyufiHvNawgJ35MR5hLBgFlN_fERtoQ50XrigsM_9imgnGcK3V6OQN5SEbhfrrhL3r7AHykHCEWZqwZWGrAvFnsBdmnOka1AgLlqg6uhMFVjVXz120Yw6Jre9t-XL1qhxMO_bIJprkABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG4LcWFR9KSOyp32dxiQXzSEnaHH9UpNUAckbLKigP4w5TqyX73BfYTGfQVn2KZDQAMhLiq7NPVZg8DEpZtWLfLdpRcxiHT09krvTzPspwWN4PA6YR1tlzFyn8eIZHOOOKbeq91mDvvXrjzcz_LQQjki0CGIQTFajCWl2sfaWp0RT2Qkldj4HkMhLg-hmkwlN4M4Rnj4aQbBZGL6Xgms2FOEA2fEZa3JcMGLQpnIwG--YLgQgkBogYzHfJM_TmyUHNmG59dowvYYXauHa-Kwwenz5tv6qsqLk_8qJaCKaCmvjFihu4NF2iowakHtbNBU3yA2QoGCHeURqwo-YT1c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw6JnK7AruH_WftKSVqNrLQJC3tSMaeSSrDAkoZSbcKTGNQVyFzQSdP2SANkchwC83fEgR_fqRxwBuxI4SbjH7bUpHWrDeddjlaggy9sSFxmLX1eqw-iDbImJ1DLWV1azWwugHpkldwxsgsOFFHPlkEI0h0udG9xHpbtC0GkPhQj8eVaILiRGb27XCOwC7HXpLbRnDGC4rLA6PiA3KZnZae6sustzJzdakFwDLo_hL3HyHCZDSqYenGN6Z1rNQy5IT08hiPoW0vYjocFPhP_OINhK5596nHDP9bseRvQ3Lpq0xJDCI3uFMxC7cT2WCbM-_4D_8pwUBp_m2m6to0uYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjTSBJFrkpe04OO6b5wM_HVmB8z0WYK-A1_J8Nt-WUFoao8f9ECyFYb4T8tAOvpyHmmrqMoz1rcStG6eWKjE3dLDXC22vp0qWDReUdpIzi5u3aGrnvfRuLZYY7EdXTcvB7a6LSlE5ZrZxtr7Z7PVJrmYGYpnyKVeMqi7ghjBvV9J0C1Aoh4k9ZYUk23kqHSJPvxQi2n7lXbzsJ9P4heXtc3dFDx737xEZcP20_S9hS1UyPJ204VvjvGLGOmUTdhg1zLrSJ5-WzxxJt-kOrZnxeodr2QIDiJXVf5KisiHND08yEgG_RdqD3aZ-78WFViXouS9WsXx9JycoCpgeHD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRgYMYlqTtl6Nl-_6mXr7E9zdt0k9QAb1e5miOSZqMg97lVfaW9Nhzhe1YHv3S9aQzJgPL_MQxv5b2hXXWnm6tlcoLKoSjPAgGMkymW_ZRYC2YCMCBPvEi3CWKLvgBnMORj4VdUZNnBrcqc3C9_Adda4vEHcNvn1eePst6Nx6W0Rc1hhzIcn51OSktxltCwvfz-UluNz4HyYhkLTQLLm7F4_OYwkFC7gCmZgw_cp9GvRqhjwCn42WlkI5FPpc0ks_wM8q-NOnNhs6eFulcY14Mnmpdv1h-El4mmzm4PU4WPvgH4n_jJFb08xOWgMvDBhJe10pkNtayz3Mhvj52JM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntKwZsdVr3jzdi8L0JRtbAT7HNYrLkWQPCKT5oHiuBhxROtOR2Bv8oCKdOoe7PLEmWM-RAoH84KxAQhyqlEmw9EXL7JT3Hndvc4lS2p8negj9VdtUoTCCPMuKXxAxFSZp_4KAyBcPqgPrUV4Z84adbjFuN6xrWBFGwcZhcr-la65Igfppd-u39aL3IdM-M2PAmfQ-ptg5FFGQqj7N2LI9KEDXqOlfsNmJR3rteQSScEAW8suxmOVSKnnML2BFia2dr3l0ish8dhDYQ-7CtuifZ6glDKZ9D79ZXP24XSCBQE7MUj_d4P8Z_AVQv5taRzAUb4bcIRyqj0OIY_raUWIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_KvE9YVYi8rGdjkR7lCivXwW57-c96Ad9w94OQ4yGp41UpTdefQuKxqrcrNu2FYuVjw0YBqo6f1iO1qCmv4mZxyxfOg1PR2uLgQ0KyExpUhNbgIg89Q2lFdHsVzY6xmwY2qPzHA-CYpm2yWV0LVV1ypgd183393V1zchu6CL6mA1Xuap-QdK_Gl9hqrvFe32gpoTZ8uCB_pVC9SxZcr-8QXyqL6yW5XN6AYX2UHxRYEvz-7HJj4TqyLjHr9SdOvzqfs4BDjkspYVmdU97841yWAZhO7SJNNU7kf2g2h_WKu_ksE-22w_95-_JekVBHan0V2Kqbld-O9kQld0qTIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bILLggcXoew80jb6ZsXl98DS6r5IZp-DluaTZ8ACKykl7wLFotQB3KZjeJUewDVSI1VDTXwe-GlXLJ8HELDi7O4nCq-sBpl5mFHbr3BbXwqCBSQxqIrW1A1ycavrQuiMKOoFfoOOR5bFG1xFOUc8IceLryEcAQEx525BXE8bzWxVF2Z3E5h29yiRQ41bmhKiyNt7QBphzmzhhes7K6ziqX2HVflCh0McPYHMOIdwYgFXwk-WxgVy0y_7jzj3kKGMZsHzM9lGmHYmOvwK_bvPed5k8V3yYUVQON8o_UcVqFQMD6lLIjmn2nBj-Tn18dBkjj0pu6E4x5YGVIqA4_8okw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpsPEfm9SlcqXiyxE1s_pVYrE8g2j1ESrbGjZ0gvJ5UT_hCKM4uTVCkTVgRbeTYvpwjRsVesyAZhdyhoi7a7-djqO_giACIkTsPQmrAmEDLaOLmsDayiIuY3EY1AhyYZOIVd0wH9hlNaD4gBCP7WJneLWHKddL60q3K94OyROQCfOAuIOfF1qcCzbgPmxA-fHAXiLIzZZGit3adqWLYWjPfLiCutTXOuk9efFPewjIq3Mxuvpl1dFfCeqKDfdtDp-EIXykQPPuC03h_kUNXim2JH-dZM_bFSAypROzIfiMK5LGMMYh-4DT6fCkFdXqt_fQrFhdST9Aqa8rQ_A2-lJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov3MwGUTW_APdxwrvwf-9gRwKnDK0UgZGdT2Mf6J5c36TQ6R8DkJ0Zmn-8VCjWK6gS8LW7_7xMSJdROKveX52TIYzL2OUfEPM-sXzSXXDMD1wGG8gDMnkxFWdpHYQ4FFnnoC8eR9Ku3uCsf7UHi90nd3GLxlpi8pcX9G2WIyu5zt8LLDwwXyLc6piPstHw4_uK2Webv5y9rIDmtEMRgk8zWiselBH9LpzW-B4I8zKZ7dhmBtNU49HOjmt_o05G1L-LlybXaPG-8V3-Si8YpL6B_iA5Swj3SqCXFmNX0Gj-tTMjvsgXiuTsIHtpXy9OL8jXVtb36qFtWYX83OOF_m5g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=oDQX5HQmwldJipyTJml7_5WIJeLT58XWaOGtzD3E-TH-m7eoD6SaZCEUoBvFvLGTlKIo3v1vcKj5eLigqnV-H1DeIvErjAOTqbmZpq3TxizaYdO_U2SjZiAoOieITzOqJXb_qlpmH2KLF_rMRxRQYICKhmE6KRCqHsOe8J_g8Ih1q3U_6fTP0KZuyv-jTWHFEqKKoc7AAxCSfKNesNYIgAYL7-Pr5xgRsLI3xton5HP1qOPVVryec8V8g-tptBpfUaoE80HPXp8vNS8Zn4inx13GF7BW9uIroOYP9Ag-F5_JXDm-B_UxepY03zEbCpp1SlEKeR2ux0r-TSrbJYgVog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=oDQX5HQmwldJipyTJml7_5WIJeLT58XWaOGtzD3E-TH-m7eoD6SaZCEUoBvFvLGTlKIo3v1vcKj5eLigqnV-H1DeIvErjAOTqbmZpq3TxizaYdO_U2SjZiAoOieITzOqJXb_qlpmH2KLF_rMRxRQYICKhmE6KRCqHsOe8J_g8Ih1q3U_6fTP0KZuyv-jTWHFEqKKoc7AAxCSfKNesNYIgAYL7-Pr5xgRsLI3xton5HP1qOPVVryec8V8g-tptBpfUaoE80HPXp8vNS8Zn4inx13GF7BW9uIroOYP9Ag-F5_JXDm-B_UxepY03zEbCpp1SlEKeR2ux0r-TSrbJYgVog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjSM7-J97kFHfId0B5grS6HEKDxkkdgbOn5XMP7Rlbo6Ky6M3ul2gcAIUkECSDpCpj3sFkFpV1XOewvXmby3-rDeH486-0uXeJnAOOiMTd9AEtLlT7Mq6m9BPGnNY2JV2ZJCItA7ESGvusyhngFOyZedvyF-1IOP-x5ZZwcuIXqlCWt13xaK_OvLR6satttA9xzT2qg4nqRQP0TSHnazzrt6hBFOQDTztRg31zYD833BOZOGxI_6N2CxTJtt3-8fjJyddIsq4vaX3JXJD1XNm8n-YO3fk-1QwqwNGQFw8u3WZwnAXmsr2KwKps_pcmGU6wiH0qsW6XT9wS0m3t6x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMYFgkd9EOnsBgAXyCZZn4B7QG0LXOeQfTWgN9EyX8ZGAgVnGSY-5HFS5-ZJsxOdb1TIXINxU6wjd8uUKK7B94acWg5QJONDCUcJyjCC3VK7HMpbuiFG-6GRtNUKtWha7R8I57nWh7dTBzWjti3lBiDmE0TJ2JHTBr4uyGeaqXAQQeFfpXLYYjhq3-9qO5u2x0XmRCGIwRfRBYrsjX42a60ABEDla-Q5lWj7e-gxFjRPe4BMOk9-wLFHovrrFmqyDr-L9-RWwlPVgGHlFv5mL4NSlV89dywTcEa2j6I4Ipu1YlARW7az7XAUJ5pw4XOy_7EBxLIuV7rmDUGpzhZ8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSRbbT5AgKb9mWIEklyx-vo3TSxI8WaVGqMpp3IiX52vXs1LUfVmUvC-38STdB3RGGX-ClIynr--zUrjRWXuWwAInkNu_m9JV-EKIuFaYCa19W9j1FTlUEuNP4NCFpTacBP7GV9eaHyeFmUEH6QdPXNfgrDF78e8w7i64MbHQfuFi8V3H6oIRLfzskxW5-WC-Cxkl2hRCJ6rUqaNH4-hWIQJ4pAbS7BtrggksltDrBYyILQaUYwa6AG3nefhytl-XMlOzb-33Q57CBo-Hn7e0yYnZqcbotNDQhH2KJMTzDkckkadPQCDNIOeFBKm95x0EIcsxrNBtsKoROVe6P8dJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGgG2tPc-JLlUV8jLFX06mCvBrs5351grYVGb86cXj21Yx5CytOG3x_VCjUqBOx9ZtMW2ofcCCQe0Svzxh53kV1urcVHmXdnPmrChjAqkyiAkafkGMAxF7qc6FNJqQQZG6R3TJLYJhOLBKLInTJwsXepJ-ZC6Ny9GWajxTQPXDggy-KQo0XkQXXv59OEQV11aaQHeSeBUBN_71OkVK-0dr2pLms7HEmNdip1fGrlYdYQkVpstp-Fmll9yziXtgNAKrMKhCckcY3CeQQzgpQwBhPOfrktQs3kWZ5-_afrdy8GqK2X_ZhsZ7WaOS6Y7MNWD2AJp9yiCMxqvbIXXQmvkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqYuWMdlzxkeqHzLwPzg3NGJr7W6WcEyt7syRW_LsnGhCJ3g76hJ0J8VLbpoFEdGAXT7a85-csa2Gru9vocJBRu3JDyO5MUhRuPV3JGkjpY_FyFyiy2gyVFCP8ya3KYzAFQ9HIDDblmqnBEv7A6U77s1UCxSqCDH6xSQGjjwXkoa2HBERtzvDme8D3v2LejhIhOV90ulS9afa1hgJ3NF6MHY19uiSQehAA2ZqPRAOPrU4xxMh4UovvQblsXOy61oX8YKxdWsXswA_I7YojwOU2n7wiRJgXwQIu3MzOP5uQLepfsAfWEslTsyzkX_TUZ1pPYxuoad95KPbu03IaoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF0gg34CfziGzbV5ScwaZIAtkMeY_K_MSwo3fbWWmV5rMs6PG4ENykiHDX08UasuMGxHLdPHnpCyVTkyz2Sjv4c36vu1gh5KvEXvNHEYo3whBOvAsaT0jMZs7q-ElqerH2cWnoHA_glqEkzlJcZe40FGo-7Vww2ru0DwBceloXNw7xX6SuB5giYe4ZcsHHvGK4BoOZTu9a_vG-NNtCSkxBBZU73xfmW1rqfm0DvIcoAzgi69iUFEhMshdWfVtInMzrKJ0qxElZLW39IpbySGmBdKvpDhzFrGy8SHpn11zfbcP3pHNa1AQA-uvU1k7sT4pvlkyzs__AgGi5NXqRs0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbqRkEfoooFqbisB4QQP2B-ESxNfZIKJleL6M-5wH3bE-kry3dkSfPUu8bvDh6bc_2BarpZaFUtu34LEInMz9N7s4IeZRlmSKCmXStHHLeMa3xL1CxSrUu6Bcvbel-oKfwj4mHsheMf_9QTQ0ko1hm5Eu0dXLyIljobs9ycxyLyxXu6w1lyR-z-7oE3MSWoPS28jsPs6tRfWub1L2bMRaRA32SfhGvriqzW8EAbM-PqMmC8uvLqNpkT423FqwDIjxvmzo436Nb9FhTy-m5jGhBxeDI7ssfflXNbl__4hWg_cydJ8nZM9qIFppEDYzerC70omYEu5VNdy2DOky_sVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QA4rJFTLU_AXta3EELlBN6Wv2Qr-TzFg_3l8X5zBH7BOY0jnfIA4def7_Axqxk6k01Vkz1Xnzz2O-8-4mGHmpcUCDkG0w8iRns7OlzvUATp8Cg05qX1Os2kkypZLFd4QCnmdHgE2gBMIgtjkcyFywMRJmZMT-IaEEvEPaqlUXZrXRTJ3kkCc7uKwRCHA2Ru7OT6-p4GgvWBNK5WaVoTk1oYypXSwfF9EiETWbUVE6XHHJmoxZtEGdr2QtLpAGq8MwVWNk4XxXAHVXn7xQP2UnDbVnEiCPHooHjabxu9wdNUmilpSjOOkAhAlGHm2CLMEW0Em2pRKGdu7VcV3sPlCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhHXTFUr5x88bImYQjSjY95jU3ZB0AsWzCjBmXd_SCvdtmm9hdp5LVsCNDr737gaix9FwSq88w4kW3odlVCZMsgEj5nI-zieZFM268YrSQZiFeY-t8OeFCP4R7MSvcZamM0USpqnekArivQmSrjZeiOJMFyZtOh0l3x-j6_cuu_NfAIuYLs8V1bhdzc-jvUXWTfm9m2z56qLgnZgUsFMydeCYlCN3Po9UvtJAD0MY_a-NPmYd-1y3jID4coF5wIjbNRGBCSMURtkO0RrC28M0v26hhPvjbAnCj7RVUBzrU8ds2U_qR5fywoNAx4chE6lPbSg1AVEl1_e-w7hLVgyhw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRD2qRjYRhU7DlHDlx6uLAtOSOQ_i1uMoC-MDTlTq0nm48l7s08C3Ryjf6s4kchTgGDDkfQZvlm5Imo-w9hZchKEssey6UPW27GgzpGMMoLHWuzdX1CNcrvXNWpQsUNMOMVsDlmrKEZDo0wCaGH9Fn-L2o37b02ccz79yHJ3Mivbg4YcdR44OdbYzoQNFhHJKh5ZZfv6IX0C12qCjWLa-RrpJrw9I83PzUkMR81P0CbVg7EA4Pt55R9JkZWojWsEEvieQHZs1muAnwDRxBPbRjQ1J98XKINWk9wmpNTdKuJBP-Cu1whrfX11Ty5ijypgvFcXzILxgar9sjc-csINWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T60hmYGMVVSLbKrAHLUdwaEpkZapxa5DuxTe4kuRtrzoV025KBnqBCCKj-hd9lb13gfEK6HKADAPN2IFzBRM9ggQCiF49GQHQ1YAe9YC38tvlqtDMwoRdrKEdDuf6T64RZ8FS2vKkoJo6V5X2xaPDwxqo_i6i7qmkOD8XVI4d8H44u8l9Jb9fe7BNFjvyLRkuCTOMofnrpZ0pyKQchAtBzOCNKBIXSTiP78HgIWNnZrLva1Dvjx69L_W7BOXErZTPdW0OVR6uT1b_MwePW_YmtqPmunWVNnA6vuna9W5LlmDZBoMWIZdht3L3bvbQxmovvUn0xP4qcYsoUNahGPCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjYkbztLYl6qKv75KrDLNHfzfKuRti_UmoDaJPTwPTYmk5Q2pnR5kFkvsmk0uep7RPjV_0x30qol3HN8inPvB-FrUFLf5npLv1DbozqnhF9-h0ZjLV9LH87zcZPYNRdn3sOEEM26fTfCyBSFih-UrAhx8IJs3XgUlWL9afj_fcEUg_7TuogEo9lriRvejguCbvleRttgHqgE0kwfjx-ItpnIWoUN1XtgRgVzJ09YZCbPzXm0NaWo9UXLSZS1SRAfIUEMTXekooHKMfOdboiehvwZmee166g5aMwZQ-M1XnstlZRDt6jJ4S5TJQQI-cYOquWsSH9NKumdfUqGhZbwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XihbL5PamthWQUAP3K90emCdp5me3hBwkqbQ11TBkZ91vppEZF0N-Ps9OUMQAOpHnsGWQFqDMXawM6QvOvxyf6bI-aE7VXwg1I98foqDW-kLqwavkLc01KP_NzHYO6MtnzA2eRroBP7Z5MEFEodRxOy0NZyC_R57XYJ067cX_qC9pi170-uZDEVYelW_vWMiIOl1DJTqH5ejvtmGWkSVWZDsxIa8tb8KJqMsAWTJEziCPq1gbr9YyyzAnpNQ78q5olZYSaJvLLaRucjhSclOAvvZkVKb56vxS1K5ZKj_YsgN3EO7ww73ga8CGkL00GFO73FWMc2gwWjxTUahkbqnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZQtRdwiUna2jX0EEEPYFv1wEOS9SN2srON-Qd89pnqk8HI1GvbEwB3p467M8zZLxblRY6TLdUHPtklnBAvGIbNR8-zkcpGvh2HywBMe2NCrA4wm8GmEpt_Ud2wcKBeohINQkVFxS2WvPYj8VLFWHpWbfyEVB-3mtpyZ64cnk9EQOuHUcRwTfCxxCtBY-yIeFaOWuLgOqw2FvZfwH2M_vpXXaafTSlgOFZ468CIDILLdfhwm7Wq6jaqrg6MAzBleqLnlm4J-JMCv_Pm21UZB1fMGaAg-x7j-LmEY0NP85J38bRZKn78q0-bN4oINo5oKBTZAwRtQfZ-A5El8t5oL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSlibVmW6jirMwH2xnK7OYbkzL0sK7XUPlUGsQVk582W_9062hr4SfiHzl3681_8UPtTLX9SOXUHG7JW-t9wWZysUU31ZfvBZivgVcpe1rgCYAe0M2lZVEEAPKNJMKUToKl-aMv_4JsiNMCu_OiuEOQwBUAajIX9RmJ_fyKLfVwLdVLSzkfcB7vBfzTXT_y-1C8uUMq-euRNvb-z8sxM3cQAmlOgXwDjbm1S5Kv_tuHk0s_dJCoKoX1XOzKVcifMdG5rUTZX46FM94ZhPqU_-IeXBJUR4NWCy9-5onzZHrN0TgYSsXtGlKAY87vMbKAnNQV1ZFDNbbsZ_SZs0HCLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7sDKZvj-v7wVwplVkcowyi7mBrW-BEO0aW1ms9cvGKCRazjLF2QdGxnk_jH8Tbje3yqiYB1X5g4iRMMbclnDU0MPc78K99pCrYsT-NijZO_yE4bZCfiKK8vHly7beeeGSfiqvDG6_If39NNIIaQ8DEduqbze4kv6pp7Z4oV9nQ2OSjqZiCiBOTEdDGZNwtYX9iZyvTWuVHb0o-CDECB8FydQMd5ftj6HQIzw1tDo_fvc8gPQNAM96WmnmYXcmpP7wn-K6OpARymSoAVNY8SAjpJyadlWCDieeekbCJbmWEdQTBh8bMFCY8gj7NmSohYZ4P4d3UGRMJcLFHrgX8y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rf-auMpXBGvDjUzoIEfJCf87ElWjxX8hvqX-1vkFYW_IYLcRNtR_bG59p5L0Qj41QvHisXATjJrmzESfK6NHWAtRBjl8pzzoqoDec5uPdpzmKo1TNc1jjMFm91w6oL0JKMT7BUnZZ7hp-AS09Ye_C_gdCcAEzPJTQQpBl7VwdVAs6SjJaY8Zulahb17kFvRVR6iOwuINYR1xnL3Kpei7IEwruhbWv3UTym9RpmFjwa205-or8Q49GoUCuVu1jxydrfS-s7UXiRjCUsY8209uLZZPvWm2K4XilEROdvMGWOQZVWjmczpQOPnlMtq-aPgb_ec3hBiu4JvMdwCrGkq8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzs2ftzrROABj9yj_Pg3EWXnnq4ccNSzso9D9bSeRQ-U_O45FJkX2WGy422sMHOeB5SziSX_L42gh9IKeqaARgiwAjrbRWI0AszDS4wfFvhUUlpkefC3I3E9WqdsHdzE154kso2k5A0UMYbQs5_kbJ6Wmcmr90wkB62NMMf1DNl1mL2-SyuVDqF-2znaC1HVR9zyy4pmhnSKv1QulsOVgIPR0274CwDPttDkGGcrou4qSPvbmeITcsUaVjx7qeitsMBVoF5HnET3E3D5Rf7MSd88x3jlMYGKzvJhxTcZt0PN8evwyWn6x-PDYVKzVJaiR_f7PM7INAXe56LajzX06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5hULBcFp_RLUwBOLwR1k5IY_4V-YxbhIBsP5HIT85_lgE5Fh5DdqBrl8jsWphhK4Hg9InYA4jf8utXivkxLnVycevbMKkf1zvySvsHKfJjHOZnn9T3uAjUsJ4F45XmJaRKhVkLOYJhjYX585WAgGhpZAWagarh1wr4J3ug41jHLXNDZFdsWxAwm4J45FxrkdRrrRD2KlgGaFKVCDXbNqm-W9MLuIB7o9zl45ocqJk-ULwT4xiozQ0N6h1yP6Z7VKYlKQOOn0KwNZE4svAncuFT9qIC3s_l-ngPtscT4y7tScKP04weKgs1EcI-RItV8nu7WGDIkmcfQUyS1DP8KmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG3l0eBr8WWALReIu1U7zumK-DQZmTEhnL3zK1badils7B4y2Q7pI_iGc0aoTxqr_cUHxyxbmP3VwJmZzg66Yv7dTU4p08Oep6X_X41PmNkjXDdEQ4DbFzNbgA2eQ63ujnloZ21A8EOK8_kCqWx-cOEUhFN_8jq7abujg29BHFEnPZ3GnGqfoMlF_T7n1IVrvGNGxdtJdNigM2T2vjnWjhz1WLEt3S5W-dBOCbNs2U6nMQ2bWPgE2V4Qa45bIhXyXcpTmhupM1w16bQr_GUSY4aR2EJiBCR6GRbEOV622Jtj6zlocIGCc57SxbyBBVa1EqclnEOwRD4TJnuS52aGPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzAHvHmqY9AHU00wbS7dH4Z4AeRcJaoilHzg1xNMc_hhCLV9PsI4ENS0OTg_S2_Yxs4Koz34pHVwAmmZurtlN7L5LthhiPxe_7JWCo0nhhlGb3inW0nkkeXFuz0mckuiR4JZLFJYoX4X3Pg2kbKYTx86goW3ELDIuCdOJAn07CXZb8OnXity6e6_oJW4sGIQiQaidUxN8uUhpf3M-KimAdPCzSssKps9O2Tk7MOvSzRZ9NgrAYb41-myUHq3cgSun0JIc5ff4fXJA4EFllIarhRSIxW-7rp4nIt1jYVdosqgzISg6SVGiBYOVmjfDk88jyu0zakrPzSJ7kCqvenG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg_A89M8NaM3DM7scBxbCSnQouxgGi_k9j-9Q81uOJmb1FZ2Qg7eakZB_qOcY-2NdoW8XS3jqw4xYj5GjFGLcaCFwbIFf_gKaV_isLr8cmGdgLT6kHfCdRQbZkii-wRkci4Eb9NjFUGFiT5-1NDtZyijL-nYMdmtrSqCSw19lKVIxA6LjRFHXxaiJF_2BC4RIJHwjoMO82cgoPZAqDLF1Ye6-Xpf7NhlxfuUsbt_hc6SfMpaMh6WXmo4qFRRd2e4iLXdm_MhitCmO9oXKswmqOgOCXEa8DpTEsxEOgQzBbCuMlKjrhTeF9pOOltRediKTi1xuJ4q_reWxnPqTZi7sQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=jztCD1ZOrTrQt5yl7Go5UfxaGwQt155MqPInhTYEhMMlhoDqr58fl45MUnxhGO6yPUJ_QNDLpkKsm03eWFe4fMsBhk8I-Ver8IaQN0bxHGdSRpN4lbLxyMer5tpjTfuAMI4hFPpwqJyWvvRNr3xT4M-ws7_IBA3VAqOIJ8p1MqLivqnqZW6ZYGLnnhU_E3NnqtEZMZ7JqzXAjUHSaeH0hikTIy54_gZfH_V00KrpPSoL6QI9xtZnWWuhvDMsgzg3QisWV7t_Wv3sJ8ct5Q5b6SLy-IUzctbRZsYD0_KG3ebpZ8xYNS6jL-zyW6gETs0VZxsHDZOIHpCco8EJ3zh1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=jztCD1ZOrTrQt5yl7Go5UfxaGwQt155MqPInhTYEhMMlhoDqr58fl45MUnxhGO6yPUJ_QNDLpkKsm03eWFe4fMsBhk8I-Ver8IaQN0bxHGdSRpN4lbLxyMer5tpjTfuAMI4hFPpwqJyWvvRNr3xT4M-ws7_IBA3VAqOIJ8p1MqLivqnqZW6ZYGLnnhU_E3NnqtEZMZ7JqzXAjUHSaeH0hikTIy54_gZfH_V00KrpPSoL6QI9xtZnWWuhvDMsgzg3QisWV7t_Wv3sJ8ct5Q5b6SLy-IUzctbRZsYD0_KG3ebpZ8xYNS6jL-zyW6gETs0VZxsHDZOIHpCco8EJ3zh1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHe6Hye_0GnkUlO3bLPQoGunWW_0ZjgiSkZtvXON6BC5rfpDXcvF6gVgbvakvrucfDvhokhYKhGanAJLiBfOn2MEDDqyRB5YTm0Ujo3XMSBnI3e1N7LZ5vLvgplxWYWmyIYm97GbCdHYjC2wrZH5xT7VF0voYaz0SdmBSfcSYp_w428xQVPB1H0LB_AmlEdyMVpSZnpaN78cNuYoAWbWs9yrdW2fytHio3zdQDMY6s3XZ0BQSq_RqGibnsdbt01DH9Uj9tWvHfXsKpFSIfqaPQiiSlYO4XLUquPA2djSSAdJVbXb45GZwTnuzwHhnFYk3tjLcojDGbGOyEcuxpTgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorzJ9S86OkIlscjsx5V_gjsefOgr80ogw6DI3falng0Ggunfbmrzd1WxZs-TMLnxn1bbXhWMgUnDlv_5-WWVkBkGREgwonjKyBd56tJ2pTWJbDbAe-mHa1QwihMXv8-VW4v623Z5Vep11jVsE0aON3WPRRdaDPUIXRo-keUYFjbvdsJMHoTG99B8usGFS4tXDEjKeJ3A3Bb4WkXjP86XPRCZuJXIruTMbzI27E9bk5-XyClcaw-LRrvysO7JbzFCGadFJ_ZDpbQt4ZALfXjZDE0DijrK4siT1CnXzxTAw0l5exebzESWOf7rmaaeg9tyOO4JOv5YDkOlfCJPlYo7h-pM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorzJ9S86OkIlscjsx5V_gjsefOgr80ogw6DI3falng0Ggunfbmrzd1WxZs-TMLnxn1bbXhWMgUnDlv_5-WWVkBkGREgwonjKyBd56tJ2pTWJbDbAe-mHa1QwihMXv8-VW4v623Z5Vep11jVsE0aON3WPRRdaDPUIXRo-keUYFjbvdsJMHoTG99B8usGFS4tXDEjKeJ3A3Bb4WkXjP86XPRCZuJXIruTMbzI27E9bk5-XyClcaw-LRrvysO7JbzFCGadFJ_ZDpbQt4ZALfXjZDE0DijrK4siT1CnXzxTAw0l5exebzESWOf7rmaaeg9tyOO4JOv5YDkOlfCJPlYo7h-pM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhRI58X1BA7wBMF6vuMfw5GKb3GGe5agOnTlmSeL2l9Elg1RLJtb_3X5ZWZo6jquKEtGBaE_sV3W37YWJxOnxz3-tyYZPZW9lh7Kj3Zlh5EJ_8NpPWrZyCVOx1KiUmteBqxg0L0gXT3D-nAZShN0P4-g9poj05agGxtrzXFDuRRVaxwdmGY1H2BzE5_cKRdBZ5Zfe3keLbBoMzhkQZ3QYz2wNrvCKKK2qSZ4sSTRwes7HcBcFVDsILOPhXZ0Xe1dP5TZzYW4EFHF0vKrXnmmK_dTxf1mgQ1mVn8Vf1wWE85P2KB46Sz7QPtepFDRreqI0ej6HAwcSZD65VPSxF6GRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDhB6kIeLjNk-QC_YFT3-CKgfO22Gqg985EHbpJwxbF1DHgN_hIEufZ8APRoS_fsevJEK7krCYZClzZyXuLrd72PSZ2SvCzlGaTsM9bB6GvEf12js-ASmGbVFgI4L3hURp4V360Dbk8sEcdFsPEE-6f4Zotzf7ELTiANZOpXSwn6GHW11zaAk7Kkehq0LhqGq3AMTdAxYPIZgfVXJgJ6CPxFyWgSZ4ypeypJS7Bq6sDY7aH7oSflyo6suiisPcjFXHPfPoHc4MYicuWnDoBg2AUtwOeIWWwWyjDJmi7xzFkOrmIqb-reX7v-bRexfnFKWtLCJ_LiZL4pFuKfbhrjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuTJhmXLxHOB1qpxDDW7SXKDm26eXKV8DUosoKjyr8xmlXya6mo5zEPeX8VVRuHaRQQpfQLU1OpW1PF5dwUtartdRxvVOJ3jjwcobLkP7H_S-7Hd7Hb1q1HZOyCEbbOy4y227pDKEMwuuE5guCk9tirkZBzdQ_c-q2Fbg_0vfbKo6hfpdM_JjVq6Sujv_d7mhrkOpQLVAb65-ZHW-FT8W7g0Ld-Bvqi8XeZDjmE8efz5nkWmw4kdUiRKaySGYqKV9PmNUaJM0fblKE3tz1jURzhT3pyOE9noSShbQ32Lxu1caYDKZyWM7YZxxk84FIEIgI13rC-Y3ApdyxtD1VtTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDfwENMIBpIfVR-cvZGCkMIQNnHaZVX93eD3khmUjpq-Zs5JnQcqz0D53xesWym1kqXl_KlEbOxnph5EjnkiSp69Ip3435puHHAGkVGGgwpJB_or_8h56o33sjvMYjRR58TGx3K5fb5wFYbTewI7DvMHUdLT3liwZHtOJeHmjiMU95PaUa8KtVztAYm91iOkNBmdq6moIrM-Ui9-lnc15qqLEjqHWU97v_SIuUXIi8BlboJ77sSN62Hiu4BXJWjB7_-me2vWDAogfqUaApEFFXLEV2sUyMR6BBaSKYp1O5c3dXg9UkdH5J7fZTIoOKzE2ci4y2pCEylKEbrQfac-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWvbUUd3C2lL0xX7VwHzHwGimHRtWw6WSQyvvIAiRKWh6LMUPk7jkY73XVCnxq0q83GoTv_ek6ytqeHAOTvxiwIVWiwtNoVgqMSWYll-iwdFjnhTag4SFZV0Ep-on1VOsKsb89BUwAIxaf9KCIhwFZDCV0h_0fg4VePConq6Ny_btHtyuaYnxGuvhVYOYmYSmNjdFBtJge108javwvV-zm4D2QyyCc9z8I8wuRKKnuhU6c9mJ2DHVkZoXnMqTeD7QwPyRkFsebeE-FN5fGgtGdGDiGNvu79S3J3UZYjfZ6-1g6j9WF2_u98EYdI1LlOGlt-AP-kqLcnllUYaX_4IqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWevyx5cO7OsBYClHuS-31NS5Dm3A_lqMrAJygft2TbAMTg3-tyCX734CysC73PHHzHaMzCREj1Z5__tXiioeiDM__-A2Wpd4lF2zUQm8oZXYV9RAaqmle9aBKAGwnSerAUA9vJSPgbKpehoh-UkxRVP9dEDtz9HrfMHFpK8JrOXgVkxWI8zqqjXCpEYR37xJ3p3W24iE9FujKDGLoiUYnoemm5SCzeYLb7J1IMYmsERjTe8MeqtHYR5F5budkL9HF7PwLibe-st7yZlFhuBnxhbquGm4ZGmBNr2F2PHrMxPkwHnl7V8ub_8zkrtodxe8CDEvnTiba9z3r-8qmeqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIwjZVam5_HWipL1zU2ujzOJN8Hik2whWbHOTgJx-IFWvVQE5vu_YrACNsW-kraDHOfwA0ihSuFTv55_WAC-_CBKVWPSYpGb27m7aMpFnNVvZZFqpxUpbZbK-YF8x3LjsHl2apiMLDkOCPzJJJNgQwvMjwgVfvWMJitI5kcxxI1ksD4bSx9wcLU_s5owxNxS7-eTTBxHnB1udx5i6JbJ7ev61Ri7DxPY2qwY369WPACWkbHuzMFmLwaE7CkFAyHYQZH51NjQQCtKkOea_2JxhkI3QPLQvUwrKQfAPPF7fLzAZK2PQ0CsuGsxtvjrHKIYaY9v_nvUEVfcfYxGffHyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1bQc23r_F2WnTOclQlERs5ryMtmvmcvBKKaOCBo7z-DtDCEV2tHWd9QCN6T21hpl1ckLYTUigj6c8XpjBMlhZTqHdu1zfYyHs-h1pkaERdmMMEglPJvNaudzD9o-W2oY_gMbvSNagPwzEgv6CugVQ_nJpVVam3l_7IW2nYdyArRm5fQsS2-YeHebpneY6qGqD0ixiiX9URe7bBYFXOS-ViQavQ6Q48TQTA_S0NxTNo_xAMQLQO75fptkf-JBEtYeiRoYSk_bePsLDuqeyb_kfgDyESjEw6khl0CS0Zkp-afXXOwi-ZeYna-fdM450WlBKjqFlyiWfUez0yLO3EmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvX_EQLUAVk8v0vfOjqgcSa16LHAFZA9PclvfJqTs1Yy5Qi6MZOmGBFRmFO9Ao4mNJnTyfSUgQ_PuBw7-yY672WhCRS699cFpqCow_t889JkcyBzq-eyApSsKE5zIJqq2vxelRiRr4vNp6tiq97VkPRd7WJ6qNVMEIFOIfMnak9LWsouoZIXrDtdpWcTJrpe6glEcGvYj1bZoylbUv_nbw2ZO94rKDAi6oZmUZJxtr1QVf2slCD9iGwnmQHx0cG4bD_I0HJyqn60Wn60Knm-i4FL38OPveBAU28ajGFjaezcwJWSYS3YxYHr2uHgvIHxS6HllaHFuxpbgah24tZ-ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GetJ0ZbcQ_DJu8CqtJxQ1h4DuCE4F8Xmcve6xi35fn7QyOt47q58lRyA7ROGLpMEfkOl86avQR6S7UKcWdqA2WoEOvrVVuXgV23St5pjIuH73EevLwx2Qfoxj0hJQGJiz-03Q54-rAD5_3dlhyz1PfAk_17rAzzPCvRfl3abeHdXPiHruxdImTAPLL9Ba49WnYAquFOvi_cMZfxxe5TEu11VJ6V-751Sz1xhbWndPEsjI2Hj-71jXwJ9Pjs5_hAMKubvekAy8Xo1wq_b9qCEyPmzS58Ui8AuNEYzdgv6G22uHNTEBhg7nR5fPrPgWl1lHhYiaVK0q1S0tSkE-o_FCg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=tnxuw6J1osz0WJMS83df_HWgR_aBCAg7UrV3RgMzznCC32ix0SmjG48bURHwdrIWi4pwEvS_0aHxn6Kyr7-WL4z-rEbktgvrr2m-KezulDa4JR6hu2rhyzJ0JOVQGtY1Uy1U1IVizZ6H5emdu24Drd2J2MCNNJq9ThmeFS0sU-TBfBc9kzwDKMgkHC4qa9GIjovNLble-0XkQ0TpUVwCDXNLzyC1udnTDVfQ3I5oF_vEYnZdb1M6yK6jz1UuEhzKNr7CbkDEciixx9PxiUOkLa5cUwX4bbbq2FBp5EBmR7lp2mZwSJ64UgoskcVC0G8fLi4ZvbIybmHPncFkJ5sFuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=tnxuw6J1osz0WJMS83df_HWgR_aBCAg7UrV3RgMzznCC32ix0SmjG48bURHwdrIWi4pwEvS_0aHxn6Kyr7-WL4z-rEbktgvrr2m-KezulDa4JR6hu2rhyzJ0JOVQGtY1Uy1U1IVizZ6H5emdu24Drd2J2MCNNJq9ThmeFS0sU-TBfBc9kzwDKMgkHC4qa9GIjovNLble-0XkQ0TpUVwCDXNLzyC1udnTDVfQ3I5oF_vEYnZdb1M6yK6jz1UuEhzKNr7CbkDEciixx9PxiUOkLa5cUwX4bbbq2FBp5EBmR7lp2mZwSJ64UgoskcVC0G8fLi4ZvbIybmHPncFkJ5sFuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok4XDBXpSUUym2g9NXLrJREIgUCHjIBZVxpxg1cvT-JjIok2GLy-UYZPhEODdtSYUbqOTIpSUdZo2oX50fws7e5slGlZbWKM8FIOJquodbWQzrZ3Pv9fsr8Oxp4II1RrrLSXmGJb6wLNM3TOoD-z3NfIGxA4B3OomSUbGJQ5dg-R3dCKIIookAP_35mpJf43omKmwZp0GY7QnRGt1WEB2Q3IaGiS2KsZbULhDm9I-HPpixcV0PXa4wB_Gs-j1s_SDriZ9OnsTt7VukiiWtlLr2PdXddFB5oFezbaiInX_-lq56iyEwxptKh-5_n6JMI4bDRYb47rnyugsEOMSiIRMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky4LFSXxC2vLyPsq3wCTygkWE9nNFiTsX9LWXmYoDcCoXSTcFlVR6j5WmDcjUjVIhrjc51rs1UXXpvxTKl3-WgTnmOEaYV0aV2PAJXZ2kXpckBHMYFb-VMQ5DInHcdS34AuTxESloqNKW0UdQ3gdxqGQeINutDv6s0AvPO4jmcB_YMRxqennIvjy6-EgGUtt_ErRdVj07_4mf-bVDpairWlGjlhB0fkAt8g7-sHMSA5XrIzlEbE_LK72hBjmOT1DvHTpkwVupLKsH1vRPAorhYJr_jmTMwps9vDe_Q9PoW7LXDVZNV7t3ftyxgHBXZmH2Z5DJC4orJnTbkWa8EK7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgPPaGL3rbH8Zn8wrR-9cY5vRPeqeObZwCH7k8J1TR70bPnn7CiplkpbmrE_qtVZSObXh-QuKJKKEjmDc6p-s5ltcL5RxviZbRlPn6p6A0XiEq8F3rin8DLGI8Xi3l3haH5EX33GAAWzFIAd9D1e32hYd86DsWO7cZo8If_Py3WDw0vb0M2nmbELyAGQEH0jFMNt68JQsj0vMt70DjRVk3z6YmQjD1MQNreM4JMeS-v9G4eOa9KuadgcCRferd1vlVqkLWHh2Pepsre5gBvlv4qqHCjzex3BRFAZGFMmCVx7ZGVZlTqUofjx7dLuQ964ZLIo11r3t_HvoANAjpbhmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewBJa1W1i4CQh7rQufBZqyVZUBGGfpybJk-RvVqqRFngz7fg9kmRMjTqOEK2EXMUeIXxU9aY4J8Lw-qBCPssfaeZLZ65vOwqlitepuxO8eQ5WAICf73FEXNa7Ru_a31C_p3IR-gBAESWrMGWjHAYjy8hMozoNWITzD6Z59OWhKPQCh0YYphZ9JvLYyl34CLlLsF88DmotMe_tQ-Mpojtu6xDe5G-HI98eULTMQU_zyAzdKxPmFcju3loACtFd5vRxiu9-ue2yviq8W2MRFEZK-rw48T0RugfAuEi6melQBW5AX2rBxOIQe60LsWQnYatUvjS92Gb_EdVMzptIynWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehkguIOTI6y-zUJQdlAc2ZE2vvNcq8r0tjc6zylw_vOe196yC3LjMkm8TR-5Xf6qxEGmo9FBLUjxdaPmxIMQexj1_nmz4zCD8VZigai7VtvzYCg3CYnEFQaH4h8ufuXXB5-9DxeRPYfnpa22K1lvuTFWDSHiGuz9RJluY8m23ih1gur_2CQYrLPC04S2fglF1ui1mGnnf2GoVdKQN_8BmTFeSQSX0FkIXYeHfXrmELd1D8tpgyVMHuh4d4NZQqA7J2xKH_eeEiSGXuSwsGhkg7trbS-Z5_aNLR2WYgklvqaipUJW5t8ddLPZtcm2fQB14vrMdfucUqmlkU3AoGZnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-FZNxroEKfkStXl7av1G-qt054Nwwtvgv94hotRzyYHicMVOaehtGYfJ3cFUoUe4kc-_yVkI_ytNvVxSe6-J4nB2uaaCF7NbLci1YkAGRvnabAURM0Lww62_RRCiiY9_9kelEFPttJCsav54mBs-z7JkhbQ_ldUF1pyqoV42iQMfNUqhRrysEBZLfucUN_--LKt2dBWx0Ps1Z66MDlP_sm_ZtyRakDoNrpoaaFBsf1MEn5qYdwcG-SUIAhKjjivk4gqykoNORFkVdRwMwHb9Vf2HNrmV2i7twFr69M5_iAPuBJJWnbk7iaV_FIYHmPnNAS7KwgTZFPMYDBtZWKOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3qtZYdMSsOHGMIZVGUq1Y_efI85rb2zteGFLixBxKXNRXhjJzffo5SyimK0taIHZ6uSCWFwF_m0bP4jyH0eE0yOezrB72UyHZ8inYkzTZRfnP8c1nD9zwKF9WJ9W-b5irfbOxQKlGXzpYETyTOM8QC42-sRWh01bzPc2QVPrG8wCPd0HhxC-q7n711As0IpwlwNeius6Q4m3xmD6k2xnpbRCd26akN8-37RxtgrYCQppyaaxkdA_MKK6BqMwrgG1yqgUSOiH3vBr57deSESLXOUAICIIPXW40Xr1umFkKGv3YpZpTyshKd2UqNOkSiOIt8ALMw8YvadMgK7hgBrvA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=uSLAdrrU7r-3xlkvAGg-rwmLO7FSpNEgWzXPb1O2v4utoxJUjWed8kENhSPF3yntYt-bPFMnf3GCooM1rSwv0zag1x092DBf4ThomtWFOBG-jkshPue7RYdog3qw54bmObQ75fWrlttBlLq1HoNZw-X1Wbqni7WvJ7o1o5uiTAsXkRNTePjHLlY8BypEn4pXxJLIbce80PPasxYUAscQdXXlUto7_53xZ9AzsR0oerl5Q-m6cCxkujUnzBOr3-iYbFWSav_HFABrPvg_pI0O_5BCoc-0m-93QhrmyNnSCPHYlIgQqqvLZrmNIhgz_BnAfvX09jf4JGhkOQJKE1FnGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=uSLAdrrU7r-3xlkvAGg-rwmLO7FSpNEgWzXPb1O2v4utoxJUjWed8kENhSPF3yntYt-bPFMnf3GCooM1rSwv0zag1x092DBf4ThomtWFOBG-jkshPue7RYdog3qw54bmObQ75fWrlttBlLq1HoNZw-X1Wbqni7WvJ7o1o5uiTAsXkRNTePjHLlY8BypEn4pXxJLIbce80PPasxYUAscQdXXlUto7_53xZ9AzsR0oerl5Q-m6cCxkujUnzBOr3-iYbFWSav_HFABrPvg_pI0O_5BCoc-0m-93QhrmyNnSCPHYlIgQqqvLZrmNIhgz_BnAfvX09jf4JGhkOQJKE1FnGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biTo7dOc5kCfag2VaEW252oUaI1QImnyjKc_OxKHMf7wwOVO4_zJyTROrgOOpOLzEg7wv9ItmdpuYW3Cbjx9-69soLhmpCTc6DPgcmh5X1LvnpmF9Q90uH7hHgCYM44j4YwsO1rqYNEZcy2HGUloiFSN2Y1sy67PfRBq3hCKk8tbRwdrPCMKu8COYNXU98zL-h0jC9wHdeY78w_OmdL5IgbXpQ4Pp8C96pP5HtcKhuK9eHXheFzphPFfkP7N_i0tVYD48zbFBImBqAkIyfRaKl6sWdjPm8ZzxymIvKDsSPTXdac6z0rWYrgyb603EHgJxPdXn98MC6rHDaEP82AVvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPcaSwM05Au6-H3yaXq7NTsbUk4tC62L6fBgghgxlnmoZA9Kc26dystXug4rkR4qVxu1fmTJxk-GwhX1KnfO3n1aaDziYYJVG4u8u-BKj8TNBUIXAvqSHLqNG0WGr-xvbITuGgbSsgC9BxG1Iy7AHXITMaq6bqUtk7eNF2ls0q9p87TtRkuymgsQem2XBlKQp8hOq5QgY7gCS0kZoQ0SXTsgn46tVmDMHHXWsPjSDHzb711u29S2SD7w_V8JVTCH2qoUSBIei-M1xF_84MzZ_7XfJug54tlHLpch0a2Rwcv8Iz3CsisZ4GAUIZ9k-3odJQzMf8PyGn4_PMk90GDOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usYS4h5Ra3iB8AZ3cVJWG69PaABjbiWL9JDCN0HJbDkEaraRHVG5L4MsFM-Fe-n_xH-DADDJBrdHTjtFHViITTbIctsdcNwTo6cjpNEGKqF_HZ7L-swnMIZmBQJ0kQgxptDBBlDGoj-Q03SOMGtbZ4zL8YgJ96AVoLbzYCu9CrzGdhvEDupFfi2M7dpLfsgF6DwNtX1o4ltWtSkbutsAgR07MyuB3VkFSzL5Zp5Uc7FJQleJFPsFPOSxj92DNtXJja6Z6ed5Xak4eJQSg8Rgo1UzJhSewqyDnf3UDJy8lt0E5Jr4TSVVUJDt52SppGzKlO9zMkrO6f0Dfr38XAYpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9qN98a1VvvYJmtrQgRK40p0U_h_4pR8n3LJS_ct01b8A_yTtGdkzbMPyWx2LnCOafaqSX4W-ee0IhmsWH8k8ak_QUQe0IKv5QSNRBFKZyBVKaU2ZYRYzC-fHkJGSK7NhyxfE_mSj8k0RjkpAc19hFH6tjQafj-0HbrZX08Za-oyNtXmv704_cPyebV6m-WWiMrM-C3IW_VAf-RwqNDBHh4QfBzF-KahJ6s4a8Ia5jqi2HBaZZt6Ooiygxkn_2FljNyIpT74i5kzTi9_UtKbGvXb3axI2MFTlzEzPIWyoIEzZwLjbMktB-SNfLfvjRomd5Cd1X8x_mUcs_RqAWUrKQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=lP7JqXIwps2VB0HQRRQVw9hbgLeTV1F5LzoqWJQ98ajmnn2YFtpODbfVaqAD1CoWeHxTTEbyfX7t7qBhq-MmRpO8f6pMqn2t4ckm4mwVIp0crBdWFGVENV8kKzc0OthfKNrRLxSdNeliD0wduMYDYmx3Y4S7BAXy4DAhV5XehTjG9sDl4DkMxONJgFNvlgXyomGmkpxgN9w6Wc8yRLuwya7JVOYJ9BJz43A_NBdU2TI5IXpNZ6waHByzNtQMKeXveZ1BAQDfKFY22MAjNp6MYZFuRCJnDLT7Irj9zxwQk5rcHZUZIW7jC8W00zKtvGXk9aqmKj2Fh0f1xQWhKeTBfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=lP7JqXIwps2VB0HQRRQVw9hbgLeTV1F5LzoqWJQ98ajmnn2YFtpODbfVaqAD1CoWeHxTTEbyfX7t7qBhq-MmRpO8f6pMqn2t4ckm4mwVIp0crBdWFGVENV8kKzc0OthfKNrRLxSdNeliD0wduMYDYmx3Y4S7BAXy4DAhV5XehTjG9sDl4DkMxONJgFNvlgXyomGmkpxgN9w6Wc8yRLuwya7JVOYJ9BJz43A_NBdU2TI5IXpNZ6waHByzNtQMKeXveZ1BAQDfKFY22MAjNp6MYZFuRCJnDLT7Irj9zxwQk5rcHZUZIW7jC8W00zKtvGXk9aqmKj2Fh0f1xQWhKeTBfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuPfiTwE645Z28TinTTUcmXoOw2Pym_68_ZYM-5thuOUp4_T-oqddl8dIrOGG-ZT3jUhwkD0hAIFG69YFz9Sj39X84jF1pCgiZJy-2SzLihWh8p-T7d9Yl7IqyDHa_IYvWRNR40B7SzkpYlzDr2Jjj0TUG-PzeCu1WO35lCLTLySVyyTyjSb5tmGzSNwUnUSjh1mQZWiHuTZsvCB7oWJSo2lHO7Sdw8nCCNZpmB8Yl4sSNA9LX8kd9fvuE_EoZN_Q17OTsT9j4N2m--eYgJl4W_WumEsQk9v7B_3hcFwHaNJ_iye08EPieHmRRJC9Nkk9pAFr1q-xi2uhQwIgZxbPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7rqT9JJ4aTcQzgAxYPtJvGL5QCMKN53AecD8oWt5NfGV9UY8Mpmq1Cce28pY_5XEA0ruYtJBY-pVd0W5wafnQUDgCZDZ_KkChFgsbapVOwK0kMPNdsvbn57nJWg4uvCsWLflRm3DaAttRvLkLVTzd_c1KomHdsy9kMsYFvUH-BoBzH6gdUfSnALL_rzLCIPpEycy_Cd61QpIAFT1JteSfjlILStnoFC250yErNs8UTxJlY8CYAkjaMGoDRt3lxczXZAUgCJn2ca7Om3ItyR0prXOOPB9RhMDIfGHd_98nYlKib5Rm5CwLTO-I0RNN1mM5eWwoTPvhGZMuPGSRExog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgahNfytV4x8WCmGEfquwg8om364l3G50gQ4tVlBqElOIxhX6Db53QpXjMwQIMB221Z80p1ZewpT4HsmrghgacHmOUo38QEOZl5IHWOBmZpjdO-Wm6yvEhh_v0_gd3cuZGBZAa8OMUgq8DrpOv5ljfrmxqmXe36oChOKJedG6OW0nGYnnntXSxk8T__lX-MtPIIKile9sr7-x8ZRF9iR5U-K1oFZ5s_uGImtFG3cVPM-hHbb-xwEki6yzR0EOkXacMv-E2BEB131SERY63xxh3IxgzrkNyklQwav-KI0SI_I4WqfJpABe9-y5zYGbOzrv9TrYMDlys24PC5PiLCOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1B7caKEJL2q8Ctdfzo9V0upMP9qt79M4T1fs-f68JwshdGi6trtd-tYSYQhumkQj9JW9lQgNvUkv1hmBu70OpxJ3CsBD3ZYXfo8A2UrKM8Kw53Ms61EfVVFv7vQelxLbpFZSHs76YnmVM3wplvyBFLuI8qMoA_8FO85nEftuHCqihkPbobTk-jTdWh7JN94WgHMKyN22SjseGeeBPX-fYKt0GgP5UZDQ1fBzqNG9G2oLhHlvBSkUcZ5yuDQbEiHS5dwHd6jKMUUPU2hyhqX2g8jJuvf3zyhUNPGK5uTeK9lgPJ1kvT2jYDRM57tkSpmq67wT5lY8Suqc1__-pduWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp3vN8Z1gZ7aVaStnmlXS_aISMmrVf2frWdgZjXMRExFM1QG3fM-pWQ0u4lU-W7f3PkJX7JOjmezAsjUJSTNSU7hfvuHrKSSzvmMjBCARJIMuTiKtdi_k7NhhtiZ7QLc3hBF9veB_Sy9OF2Sad1ZHcfoCFvSSDwNXv7MkUCyZ7Ry7XzHsR_eD1NRb1ozwTNnN48PmK55SxxSqSOgiFHhGGlb-JPY68u-hMOh4uchUgwaA2Z2tJhYNU6c29B38oU_bPR83ZyVCsR_kFiMiFvXz3I-jHUQlKvKY90o6Axx5JDEnBEaquWzKiZFhIXm70930Odq4Tyd1kGRPt3wS4RhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnT58c26_RXQqF9j4-V3HNbD2Ye8HVCN2ficbuVRit3pll3KHs8X7GlP4rejNo9ym3TfX2ED79pTnV8aWZk6jvrJjHgQjNsyznbqkRglX9tj-MNGooyuqeumohJKPxeOulnTIsAoOSGsi5au2unNDp_rNvcpo96onvtKIKM0T2hv_IyLw9xaJFKbSFukkzBs-fchtKdSgOtxW1ON5CWIjO48nck_5MNRPYTxXewuYDa4gxiBt9yLMq8M7IssOl0rPIabmvPt8KPQkWr7-HTUm8ctY1bprIJUgVofXczo0gOYs-alrrAzEcex0tOQK3f4RkBEJs1uskbIcEzxinO33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKrPp-t90rkraWZ0bNj0urlXXK_MjZFz8r4jA48FAN6YqlrFHSnoMspdsnrRvIDmGP6nq2bIfjduNfgIAnBWoJ7B7Cla8Cv-XJ5dTYt9Wem-wAkhvysN--Zc02RiwvGO62OWa1Eaw-j5wTCVn-nv9zM7WyaPSsPP1guCoctEKB1YDKaW-4xMvJi4G9gHxmGLqE1IUmuGAXReKX-fbqyMPXxBbMWTcQ61OezjBxI4fNfp8z1EfkCe1oIYi7wxkyhazRj9PnUkll2qAfO7k-S56DgcxWP-pr5KaiKHMFT2-RHEpmNR9h0DYRphtpu1sKx7XCWYdO0oSG0_eWD63gm2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP1wGMF7wOY_LvIx_ld2PREyHynjqqQvn_H4Usn3p-pNfTbhaa-8A3zjLrZN6PQV_KSyz_Vm4_GnT6oCj1TQlL6Bfm7UL8wtMWd2iPV06bjMmqJyZnRmkOftwYCaxCZYnbfNapQHCWbEwb4POt1lnxselzBXve_Mb8XzUoDm1SLgz7p7L94P3UZt-r-oU0QglwmZGEqu2QOiv8ecUqOgLV6rrKlzCgBSpstOjKSww_MgEqTn3uCPf7_07DxrZVhOZOFecvwsWeL1Y4U2eNxATvLfMWQ2OuRnTOL066qUOEar-g9VCfHgyUCOjRMKUPIB9ZjkpgU0XgcXAG7LZvxjZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf9NBIE0aGS_o47Fsq3VVbTGE-uogVNpMVHWVUQQ9_FM7CeSkvaABdtllmHBRasbX_hs1vgV8GXClDWRYhtSifxYS1R0RyMxbeF1B5s8FOw17Q1L0ZtQk_iWEUw8R4BrKsfW0rQYpnt8SffbNaJKsOUEuX-54VtG5yYV2urxcEDM5JkdDN0iYvywZlxVKok1VdKMmMQncoeVBu5Mx7dStx6KmwgEQMfsGXT-1Ik2gJqrfoX4r9xcng3yEw99ZW0D8zBh6R-2Oiw0FkSjG1gouXcJwhMJ3Wg276fuUqgz8ZIaLUu7tSoTU07Zvzeq8EWO_nHtyvx16aWLYlkGFedYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfqXvYBXsFAAtTO2HXPK95oaIry3wfj_CDBMsk3G6C4_Dc6n4CCEVHlvNhzeqjDArn_NvI4wMKOke9-uokiX02x6dtd-vLuEPZsalAB2TkiSFuFqbAA5DfWPX1oJ0PzBHm5g1sf7CWGHZmvsKsbok40vIxerAxN0zV2kvQ9RjJrAgszyrswAzGPgNdNPvCPndEC_3O7D5WEl5NZxLQ4jRyTGl84qeGObMUmKUvAeTwEQFszEs4xLgOWGdyAt9dMe-4LMfjzH2b3STOTioMNsU3-QeEM50ez6thzYE6QQveIVfRssFfjV2wJxInF023S0lRVwjpwZvWdIUg03mHm3ug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=sV2I79YInI09xFn-HAr4lfmr1JMlBZFTahrwJRuS9no9VwApvLhTbp1Q0jkJ2ltUrw6UyVEwROvgQNMNKw71PNQdEHqMsRQMaPBHDnGCSHa2eFnuycqt0WerHd2C3qd57w9WV4aVIqCGIy7SBfr2E34Z70Jk1B-lWaD9OSbLFLTcmTBINAJpNpnn1v-sjg07gFj9tEwi7b3dzyrnn-Ca79o8fLtTUDInXo6fcMMYk8-hTeYudPj2ltcEGjUV2HR_PIFYxUvR6aZLdVUOQ0Lt9FwogZiyUBs19c7sKhy4JoO2D9dh6CqGV_4ncVnKeHIltV0D6fzYVfZLxEiuSzdLDT3k21hOTzXn2d1nIya1Cfee36V01OBtUKf7xqnkpOH2rVLhYaXuABCs1eCI2_GOayhf7tOOXoUPvaHuvp63C7wsfKzXqed-NXMAVTXGQ9TDCdMEPv0bonDkio2Y8ofOsowB9KqcMqPrIbLgOtiaM7tQbptgR8zhzrSC3b2SC2RJ6FegwlP-UhofWfAaz3PSySnXm7ZzEuBEI5dGflXr4ljSXrldhslmmHDO6bKYM5U67dHPALKwSpQPTJXMqb4zW4TUoQHyhU1TByZbELBFwvhcHjXcjwd9EaabgekTbPwu8Us2wksA2BwlZpeO6YI7WeOBueqrHrQhZdGW6Vjhn5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=sV2I79YInI09xFn-HAr4lfmr1JMlBZFTahrwJRuS9no9VwApvLhTbp1Q0jkJ2ltUrw6UyVEwROvgQNMNKw71PNQdEHqMsRQMaPBHDnGCSHa2eFnuycqt0WerHd2C3qd57w9WV4aVIqCGIy7SBfr2E34Z70Jk1B-lWaD9OSbLFLTcmTBINAJpNpnn1v-sjg07gFj9tEwi7b3dzyrnn-Ca79o8fLtTUDInXo6fcMMYk8-hTeYudPj2ltcEGjUV2HR_PIFYxUvR6aZLdVUOQ0Lt9FwogZiyUBs19c7sKhy4JoO2D9dh6CqGV_4ncVnKeHIltV0D6fzYVfZLxEiuSzdLDT3k21hOTzXn2d1nIya1Cfee36V01OBtUKf7xqnkpOH2rVLhYaXuABCs1eCI2_GOayhf7tOOXoUPvaHuvp63C7wsfKzXqed-NXMAVTXGQ9TDCdMEPv0bonDkio2Y8ofOsowB9KqcMqPrIbLgOtiaM7tQbptgR8zhzrSC3b2SC2RJ6FegwlP-UhofWfAaz3PSySnXm7ZzEuBEI5dGflXr4ljSXrldhslmmHDO6bKYM5U67dHPALKwSpQPTJXMqb4zW4TUoQHyhU1TByZbELBFwvhcHjXcjwd9EaabgekTbPwu8Us2wksA2BwlZpeO6YI7WeOBueqrHrQhZdGW6Vjhn5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
