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
<img src="https://cdn4.telesco.pe/file/kDu9ufzvlI3rt3dje5IZJax-ydP6l6mp0esL0ePGkDNzkoFK4zmFaR31mEXu9qKFRbj4_3Sr9_QJgPumWmqv4VSfZRnwGz3ITnyieun4fo0ftnl7AtBs2OcjmhbuBIngYwzD4wAIOS13sG84XWQtp6ADwqY3N1PTPXEoytnjxJHRnXUWHButlkg1kM62vibdP6rg58B1mKc_83soObx8TttZYzW18PY1y62NcC4WHVKON3YA13fJKWcLQlwbxU0mtbbLOkoXABco-vB3EWj1NtWD67kxnUjm9lIq2usaxDulcMCY127On5AxWmnDkqYa46JVu0febvG6yauABw4ohQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 211K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 21:13:13</div>
<hr>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7RDxvC66dKTQ1Wt0sAqwCXiWg2IFf7ZfjtbX6nKBWY1BeXjF_XiILB_nTK6_6zEIaWeTyiktX2r_e6YXd3uraB2tVIqFjnn_wb9zxMJs9Fd3vPDmArdMwIksTsYeKD_h2RssTC8KngsoIR9KmyNIfiO00blpMR4tpSvIgiUSS1SnD9TByiOWC6amZWz8X56INa_S54uEwKSywwxkzMc2K8Ppzq8JM5Apj9x4QC29lhATffFQj-uOICFsOxBq5Qi5T0ZrrlOoUy0czBpF2gndjMDbvJw-mArufTfCdNZvHU44JK9GjkQZPEyJbsHBdbMBvmbPu0HFzvLm4xRy4MgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22131">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
⭕️
رفقا با علیرضا صحبت کردم هر گیگ کافینگ رو ۲۱۰ میده
با لینک ساب بدون ضریب
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCdyUQ1YBOFLA4N6dfEO7SW_fZuWFcConm1oTJ46BUMO__yHA_Sf1oqLUDQtcW8EiAWnwIGdcZqy70R4-GbWMQLCbi8Yp03Ykwu0hMCqRLr1HfpbsVWdOwrpb4aqF488FpAnDnzJx9FHxgbVjlF8p4h9t9aBKVYW1kBowW0HCwFp1RVHhiCPKb2-mMC9uNHhy7EHEU9M3Wnboijaua3_bBj-ZMMzbmDerxt0fMOP3LZLcyR6mqsohIBexhtODx7X_lKbicoAnUvOaHzcAsa-4hj1S9Y-emSkcuc9yCgSnVMs9F10t-F1cGldykqfvZ5rMt2OACsWE0_weIzSc1OzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj-veqmFkxbU7tgEThin7mBozcSogSB3LQXkTJ5icqIiQaMQINDwSOdm-tyEkAmGSPBct-bgcDS_41aWy4Z1gFyjMAe9w3JtIZfEpiaOafYeA79Goibog1MYKJUOoZrVLGgo2ivjzoFaFN08q8-l0c508p4HRfqovj9KX1BlG8HfzJo2t84zQt01qatm6H203C-5RXPcmKLHYNT5Ileo6bKnqbrNqwPw8OSuzxOURv3FPYKMu6dQ-M3D7tsv8i__t9roAhIEVQ-zNdQgnxA-xEWiMpX2f-o6IgKXPIWb-g0hPsE1xUjHXIdfC3S39KgVZu_HsDy69Oq-vURNY4uHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFIapQtA5GAP-KNKA4Evm1J4iZD8mtpog9zGNtdQ1NPNnsT-800yHk3S9Ez4cx5u_jaflbRXz5OS9nYbbaW1A3DZAtkZwvWaiM8cPV0ncrfx235rg9P872fWzZsXqaYiqYzb30lrO_6r9U1WtGzVqKG3NBLAG1aeS-TspTYH9TqZmQZ-x2I0D0nuZTQZYNQ-k6uUGfnpGuoxmq2WbeGyGU6s7PMhBn8KqQGpn6jZSAQQ30ENyc6v0W3l9YhIjOdDIiFuhobFjjTa5RANvXBjQRifRoU08v035XNek5GVJweuGRQqO4oAUj0k1g5MoF5BiulfDIeDmPiMWIZyJghoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvMwPm-QRXgeiA44VhXcmxu4vQJCatpqA4HTVNlW72uFHDbp6J6DWT2VmeEIJ1PT7-2pmf4VWnQUfqKRMgKYDzrmZjaQ04FIvNy7Af7D-eS3spur06vgKp_hKzGfj8JV5W-HlBH6dX6YMnkHoBDLeToYZPKHToxXKWLCc6Uk94PrsEyT8pofYQisQOhAyUQ_cJlC65QLxAQV7jepUkK_YaAX6MO14dIA5id534sBJ7fI8Gfn7SMQl6YzNWHVmXgxccLuRy-ACKR6qiheYhgI7Cny2h0A0_0LxTqXg3gxEW1992qQp2OUASVReB1HnaGQdlR6zbykGqPAWG9XnCbOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFSjT3XneP1bPb5dmETDnWqc63IixHhFLC9juaNCU-LmovqXwr5DtuZqav6dW0v0jIYDNcCKRwehe2n2Wp6_-h4qS5ttYquc9_JGI1h1VmMtdDbFH84vvqPsfgvpw1xrai0WVwH_h843-cemfbyEZDrIOgIajPikDBul_YYel7pS5DRqWiTZyxDXgyTSHmKq723LixhHbpzPKeD2IqtqOfbVGads1kqXsEE7BLcFW0VcVhstdSRqReOVZ3FTFRRIN9KkNZddqWjS2PjXgGdmMsG6TRDfbJtKnEt_KHN8eZI-UFs5T8zj21tG8VlhXxAFPq5_1j4eTJUdcAwadyL-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr0PnkYnw6ozYfDw-hax7ZMyYTpCWAmjudQoCTZZ234poz_rZfIU0cetvhm0ayxbtRWAcqYlokn9id-5jBRkYz4Kvbs5duEWSAw2l2gxlacP0Zk2VA2RU6x85-ZxoveAl3QNsZDLR_YKTFaRKvMqkM51i65opFxOMbe9GN2qF2qpPhJntB-RALhybappT94P4EjcIForNvaX8L_2k_hkbmdYozgZZeRceruC3-ONhTvfiwTQRAjzApE7Ycz6DFllZL82Dbs_L49JLPcRbtSzXPVJo9DHmZVQlk8H-zrpHqp1EjT6t0MPvBQk6ORb6LZ_aZZjbyCsPyYEsANxrmtFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUYJYCeg01_GrUdQ2c5nCK9HvC-pDiORrpwvhatRkzu4zwz3u6JZxXkQtHYwKOSlKcKPKXuXDWbZVBa8TLdu7AYOj_L0rxCapOY7aOHQjcVw8HlI1ro44Os2fVJ86ony9-6KFeUn_QNOXxI_a2SFjxZeS2MEvcFdbpj26M9UYz2yxREerAR-82HLhVN5QcGt1vPDe95HWS5Xe0v8SYk_kHH1oufabHXP0wqR60v3yjC124X8SIZkVlxsQlvtii3APihfJWP2mKPVu1Q6IyGa9y_O1NdCRWph4oUOfnrBqzqtj8Yzwo1j-84xt196Wr85QLzP4wWQ6_mg93UwwoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKlcARNib46iBTfCqticAV5QV_CBxZjumzVuQ2t1KjZAn8bgcAx98Tf_oFBU7-88rVoabYBeKqShj-mjlSnwdFajGq6ud0G5MXOa-ds9X6LibCrTYJyvI9rToIoWbi0Wt4Y6fugB2ckk1m6pFCYP7JQUCDHmZE80iXRditjW6s0n3-wvCqG3U5wzy_z_kl4vgNZJLquOoHOEXs2y33hGz-VILTuSP104a9ZfUNuSRz3xo8HjZEAgYlhvYE0rtu9cSVejESjGi9-ayRVP6pwGscLqPj3Tj9BIVemrxUYbOvgdhZWaDapA0yGxfS99NEuzQShu6437n0c6iwdpq8rzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goBBhfRMjsf5EStnP189oy0pHtTEh2ZCqVETT6DNnW9k_YP2-d0j0F1DzGdxkmBp1KyIPa6wGR0__uNHOp0Crt7dnauiyLFrMZBNM9o19MXzi9OtV_VKcrIe_2KnoEOrxcrz7uyF9RXTynq_6S0Kk9Kjr3D9vMzLAp3eaNj9bF17m9HZQwIbJolHG3ty7HvAQA8nXVBkkkEOKyyr5i2dxFT4g4lLgLASd0VONJyMcWhzejVWusCgzSy71TXcpJyHnCsTbetecUA9r5DQ51y2bJRkMhTsieCcPNnyPk8z_Zfj0mHmSVAzh_LGt9lJZ7KUuqhioDjYr0TJ2u5IBMw_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-aS9QoLWdmidC7uZgc1VribhUPHJfDQXmmRsCd_dan7hr-m8t8lE5jpW13z-d7e9dzgngZGCZl_8qOllGYwnXyNxDQDDQGAltbeFl5Ru-oVIijW-wOl2-K7oTUB0CU_jdWkOo_yrm6ThtGBahpfDyOQlUL0qnPMopBJYk3ZIILDJ63qZnDfnC4Jk9D2203sHJG5dNkBBDRu-C_PJoIEpcbZvfzJHjHaKj00mVk09qwUYr0qh3lsZnFXgQy_wZcSDfye9bwR2om16pgozizRrNEO6pfgwXK5nQIU-H7Xyj2liIYTcz9X-UoP3BJdv_OuDkhGRlgkwM6HrvmweoqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsU2G71yzcVDl3VKjFrlwBrKCqTvviDLmERN4A7oFFmQbkxxiS207POFwqUK50OPtv7TnZth6vgB4RYpTVNcC5Mk9DaQPNh_Iuf0Mxuk0o5ldiRivGSOSphldVvvuUbTJ1hlRA8P3wY233CH4CgaZIRSsysSHgRAktr1dDXqMHIrL4cp5mz1FT1OGMxCaRrmDBYiyoLl4w2-sQRJ-pjgHLfdBLeYVd8PZisuTFjPef0vS634eryFjqZOpp1TeDtVZ9L0Ru9hW1vp5tmYVxPq2fGNXDT-mqo3Ti6kWxc7STahPD-7RFqQGuBTf96dU4siWJBG7hsHGuNyWUPPxUWe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OggEIESIGZcrbGqiEhFdCecYspuFIfg2DLzN3xOeHEyaRz-LtmXNNzxHBFZquIFGvQuq7u1yf7s1Q6h4fWITm1iXDTT5mA-vZam8RS8U1Ui4v8rE8kJq-AQB0KW7YklvRUPdUVLOzVUL_UmyEuu7X6-n0IvRiFcpzccBf_rvVcyumEW1viGfXuTlO4Wy2tNdPznlaUJHwT_xSC0K7gKqiDQiLo3Ff78ezTuGnn6URSf5EE44VQLUj24ktLacKRwcFyeTqZokRZ2Nj8BuIOPRO5Pw14aBDjPJFkgZWTogq2ZholoOnMkB6GtE5l69w19VTWxbZaPhaVF4fTKJ8W7oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQhr-0sJjaTSxCmfVRgH1vIFcN3IPE45MC_a0W0cdt9Bd-SUmB_H-5UgraGhlMXLGsselm-xWZ3-kbUlG6Yb03CxrUM-8bzzUQs3yH0otcIriCBfEtokdUZE17zvOERiPw58EvSLxkM8w4Ejhi9AP4EnHXSLomy-8dCIFwgthKT_2aeGAus2H6aoTOLnndS0kiSgrQCRturFd0S-npIXUO9jdearsiJYQmZD_aKtmf2PApaAjJlT_h5U1hlp5JIaNAiQQSOx8E3Sm-lbPYyYg5PuxTwKU5xTvCT09Ae_4lqbBVnmbu1kPwMEm2OoOEWis-8QEBX62Fg_yU1ijv7cAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1r1QXNWfwJBDQygPHRkaQKBpoXgbgRt_yLlQ1TOvNzj7Jcw8AND7Ni_-ZUCA3UDUkQC6a6XNEyi4qcQMx5R5XpjY0F0dyipOABfp4WHoaKe47weQdGY6JzbIR9XrGZWP_FBCHyna7m6s_Z_cuM5T_qjR4y2h271sRO_nWOhSjKysxFWNTyT2JGAPRcUfgDWYA0mRnHwmaR3e361yufRPDKJJ7t7zMRpmM7s_UxfjCrm-wp1-ZIZMKnsaeCcTqJN-midhCm6gn3N8G4VKa61WK8ssd-wSKsLG37YADfBuPiJF0T2Nl1iY6MF5zt152lmjFELValnhvBG-UVw6QvV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXAWllHg8Aw9QizZY_SYEWfX-YNr9WwFbgri1TyMIVoO6_dcUdjeobofzeFMSc3LNnF8WcMQjp-on01r3aVZNbr1uJN8KwS96d9SjC_Wrgeoe8DGqlxfwTXJIqyF799aPzjTuCLu2xOBHvF9f_ieBONlAsicjujmJRn9JQXwV_KmpieeLTkXvyi_iFHAVx-ran_0BogfCNgxOZ_dwwmZLBWATejxjJxKCRJ3stkeoQVXd1UaTJH1-GyS8vJnZNpu8OrScWqe76LAwmzNSIMq2O5Vze0EFDcAJLRv5bob3VxImL_tsZUSnQtiyWa1n4eZczw_clyzFOfTlZEgwlBirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sawB5vThNyrVkfRRc2ojHYz9u2FaREGkMFwF6bllf0cjkeZYxRq6kY5EsEe1d1e8msfRtuaZQlfhTVevsoHLt5AzEc0kTphOVqwrzndGtEHgA5a0npqzvuNse6s3cNKgUxoNoWlAbmIvJ3iw3nxZofaH0cDpF2Kbh8WBlZhoWLmFmaq_GjVklKDmifzTeFEkGnVXPkFKIljuX80jzZtyyWxV6XRwn9KMlLGGybUEhYp2L_1otcgnkdMeX08WW_0sElNe3sAPKMjm5Wibn78dvpP0qTL9-V_6WyTmmzFWOMJ-NUXepj1ZcvDCiv_Fsc-lIITHokhsGQWH3617r9jrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaTy24xa8fBDvDA53jyhcaLkqD7VdLbLlP9uEybVVXwNLYyeCf6M1HUnyQVxQJp12pWBcWIqlEvjT5PIgQV-HfAIgwUqHeBu1LghGESl34TZV4S-CNg827e_Ra5ENgBxOCPaRBTSLysSJOleWxo7l_tb4hH-EcVMXX8QWN_4MIXkkZNF7nu7cJXlnJsCjuNKfcb8P6ROhI3J9XBixnzENAMXAf4jR2xY6Cis8hGQyYQEhj6vbSQuHaA1XV5RDk0WGe-0G-Ji_R07bGgUK9W8Fhl5li0EpQGPb_77JwxsoyoPDdjUP5vhPfsM0tjqbicdP5mxC80WwI4fGJzU84M88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM4hV8dTpywf8jD9QG5CEpJHJF0-lzPvRW_6KvrAsdlTjONCGxri-yLzFZa9ZUh6vNX7BgSEtZVi1K7PYhjn8cgPR8VGXKO3mguPas3XRexOcepV6qy1sExav9C62eXA6sYhc0orphYTLKbgyYAsPvchbTeUWOJya5VekQw-KMSYK90UJTM68tOz-s68I5vO5xU9-7N6F2JxlKqzxz91lLwE0qT0zjK3_bbMc0hFmwQgfPyh3LWm2jFlk07vuEdZQ4u1-thoEtWIjPjtp6u6MmovZiLMMdOL2iqaWVVGWtF6ks4jlYSmFoHa9a3eLIh0gWLfLXPV43bhN0tDLBcr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ-_UQ3YnK6I0OcAiJxZYd9tehDUxG1EY4e-zI5dODZHshmh9Qvx5lOHbbYk7VnTpQ-1ZVgVxUfEjGlrbgsT8vhs3GJlqvU5dSuGi7eOJw3Gl96zBNV2NxAoUVzj21k_b3leh0X6-yWlzxc3AaFj0I4h7IjLLrog6DFRt8O9r7HqfofSDNupf7p0PWgf86KNUeGZZwrlSx6DFyB8-0WHGYLw94vSLAE_h9Rl4-BZtjkh4tBYBp2224nWD_BkK_q5eKcr_NBSqsQoONMx1q4A7yZ_HBJN7RSyCPJZD_APPsmAd6uhF_tQia010qzIqL6O3F9EQVtilK7QH20MABJQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVz-PYdP0kdA-D7y10dCuOxIIAThfhgOnxYEZ9nambRj6UImd7xr2KHEbyqfcmqApPbJihp-vLNaPinCXY6MwjkAjFlDrdTHwj5qTYWZCjB0KYfaAQ8bYXy0m73hR0Ie0ABsRYjMciNdmKBV6YoHklSUXyFSl-gr_W7tkIL2j5_BM7II7-r9KNxdAwdEd6QjNOcyNnxxsokz6qQQkGMKIqFRl7ng_huEaZP_yxY5vOvAqNK3Ae_3P-sBkgbrPD7vOjtSE7LzKQXAbnymYBgvNybabwy6RqiDjEIrW4KpL0RzGUuVc_bNL8vqLB8qw2QUSU4T07DbSpWRpfuIfYWH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5nBkLBNg51HGd0wyU9jsbrH73JqoZmI1KwjO4Kp6W5PwT5uEWRZgVK92m_ib693hs2o9aHr9O-nY30egZ74X9vAIS2iAMl9mWF3fj-sZr8jnQeQ0kztm9K26N6UNJ8JOHR8W9NifJeX7GNzMp7m0AqGwn0bZyKPgx2Zjvpk96SWbTS8gnOC-3vKGYJxByYThE8iluNQ1hqpatNYSML8CnmthUSndqTUrJq5ekRIqlbQ7Eimg-gN6TqHs4VF_wXpGuVqr9R5zNccYnm8lwY07WQo6yOU44ZG8YJkEqqipYo5bO2ekGPqP0ygJ3aL5dkZnafq8UwKFulYPVkkLeT-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go-ejkU_XOINkoVeMzvFR0_D7uL4fW-gUFQZbzXPVSQ5pb43evGRANX8K8cYonn12IEcTtep5szfFL7TjSqveb6DkXJR-Hyjmsi919cTh6LF6c00hAJKJvjw-8QPftBTPD0jo8TVQUY1Vk8JSY-G6Qssv0rRkfde6P2hsdOYlERqzI1ox8tQ7cPemkRc4EHrwApok0oQ0FDXMgX3mowwUnWMIoyyCueXumEOyN-7ousszrONrtvW1p2PYRBvALgXGLx_ZFuDj-H15TIhUucl74FCg5ouVAzKeE0qIbHMXsTujBpaO-1pxDijuBvCGhHqaJf5BXd6rjZsTkTqIS77Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw741ISadO0gz1rlq1Ur8x7wJhf9ii5CzaLtR8CDySoHqPUL6tWjwMAGlVraKKTPq1QcjvBvQK1pMGajFrEgkq3ScK34oScstea2jW6MurTLcR30TVLs13f_RF69NycrccjTfM4TOy1DvejNyi41lxxjvvGm3sqiDpDjLk5GFP1xfaFijn1SEEqJdMtGVL36Xr-mtm4pbAip9oaaDVUvWuF6VP592UDFRphLDeJ7U-YWanQ1HxWrXUwR3nipggm3U5YEnmdLla8XXG_LUqBfkEggZFjdMq_8a6b-mtnTF0FrbEGmzrsDu7rovJrGGU88N7FXulCVugAK6XfhZdF-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFRZ6NEQv0SvSHrLqavlQiCGIrjSZgmIlVHy-S3jWYDhNDeIDcz35ogR3o3620lGpHQZAsY3ZJ6gx6s09GCmQ5BBnBRtL7c2oB4__XjH_FrxBOUth9p9VXXZQR2GY8LL57wTKA-yyXh8tM9Psg8gD7zo0h-CyUf4cFnlgngEcA3JlMoFQQRJ15s79JS9mnshzrrEAZK-LPbH2f0XvHhrbKPIvvd6wizMt5aKML9avW3BdmnhQEbDHSoVMvsDza_sRfO0Xhi4kQeMTzd2xeQ4CzIjodmuE0Gpk-24RLwOwZPbCdz81nqQnS17xexan4OeTVaZ7QYkWfucGYZxUgS0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=Snw17P834dmYyE7ej2KgzhwMkjimXj4XfyH6Ce4-xzvX-gZLtTmJjEG0EnOrcu5Pt27mPLuoIzNZF25kfHievUFKwQFRQCsXgWfG_xvR_qfY0LSyigtGh0yfd2_pSAwzspgBFrr0jdjFqnt6jTtyBtx6YsaI3WugATLy4nx1s_3RBuCs2ASCaKfAihjK7MoJ58uzVdVU-f1qdXcB57tQj3nAzYX6Ph4vwoDmbwDq9UrfodffHfWDYj4nSt371gyBepzgWDDFvnQjq6xZzKHm77LwMw40jyTHejRXCHkWXKBIZN5YmlBW8ZeREWBM0X3aAm3Oz8_UcDfg___n44-ZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=Snw17P834dmYyE7ej2KgzhwMkjimXj4XfyH6Ce4-xzvX-gZLtTmJjEG0EnOrcu5Pt27mPLuoIzNZF25kfHievUFKwQFRQCsXgWfG_xvR_qfY0LSyigtGh0yfd2_pSAwzspgBFrr0jdjFqnt6jTtyBtx6YsaI3WugATLy4nx1s_3RBuCs2ASCaKfAihjK7MoJ58uzVdVU-f1qdXcB57tQj3nAzYX6Ph4vwoDmbwDq9UrfodffHfWDYj4nSt371gyBepzgWDDFvnQjq6xZzKHm77LwMw40jyTHejRXCHkWXKBIZN5YmlBW8ZeREWBM0X3aAm3Oz8_UcDfg___n44-ZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vou5A5WG8uec76t798sExuzZYL100RRGyDr9tam8oTw8bvKGNn79Q4djytHWWMj9CniGtVgluvJJbiHIQSrnd85JweqxYzPGfjMGqAnPE72uoJg7rOmtSWFdm8mprGoyrUrohA3pVGDLx40biJO2NH5AH5tF1AR-ArBqtNBW_28W6vbmKK4UNNzlcQaFt4EQu2qw8yP_kjYccF7Ry4HEelu2lcn58y2Fmio_v3DaPTaU74nbcfiTPlP4HITJZ2cSOwZmoaPwX2iltQgGI9A9wW_d6A_ZkuK1QD2B9uSkuV-wN4GLET2LW-Se_nFJcX5t_QacRc-UCHfABGMYyylkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AubNufsl2YcS8pNRxDmoClNEjJt3b6zlX_u0VGl-g6OoLDNBVVan4297r-Bq4B3Y_e9gsrQDwYza8ysCqtrzDuIqdYFrY-gRnsEXO4yacBK8M6BzdfIv1KFuwhfR-kB7wFBB_5GrAUa6ZjyzAOLrG7ZUKy5E1RXNddS1wxOWVgZn75NHz2BzWxHlNA2QtX50tmixb-1tQGgBqOuG5zIxIYqLRuIi8YfacrJ_zjhggV09hjKtoMpvNe80fjqC4owAYv_zhbAyxyxd0bNLM26wJkjiK-auYTUU8KgrtWersrQMhuiF5Df9qsQfEnngZ1PKQuekdEDdZtp8G1gdlhi_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBLHe29LdMqKo9gvhIn933uBY1E726zt6u2qMUdZF_KKyIPTBqtEyueJj8B6_NJc1-HSUSylat52t1Pcbpd83HEye4ABK_UTgC-cYf99xDuq-9lN2tAzQOnLdv2ZNEFO0I-wrMJIV1x6NPyIvqae8VHshrWoAEzXbCcTqV3dKzLJidU_N1kfS_8Af3jnyAyqxoKdmwyB-mzPH60SYduAgGjZ9MlIU5Hf7Z1JtBowcajFhDEYKDW7exwr818IRLKvGD6Cdgs1wpBbKBCnNACIh6RrhU9FBSbb9BdWp9U7aqMdDFuOTqGLKB57n4YQtqszmC3dZp476PXHWULHEiR-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaNfS2e_8rqfbylRwku_oxTkAn_CYLHnyge2gIjdUq3DkwbLNrc0jlxC3x6flZDGBK6-wQtlu2Dyr9I5gd1MNJSHkL-CMquJ88_hw_PzTpO4m2Z5qqX45jhOgW2BE_cLjzf9vx1Jh4gmWUPJ-attIi7502FfdAXKcdYSvkHcz5eOcC36WlM8oppjnAjzY4GeJ_6bGoyxbIgEFPJPEQUDwJDFqPJPAteGdiHQWyTb9gLQrRpnt1oHAnhRrI-MlrfdI3xvtfl6Tj2ww7Xyv05WRN1AHX3G-LNiJEGnhdvCeTOCuqd0fDtFKblqztiM4WrfNxYeCzuEtd_fb2nnMx9_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abERRcUCyZtjLKY9edl8cci-MLmhzVef0mN8ZLaXIjfWxprpRyODq4EjL_ABaMTslR6tSpNMeX3cP3yUjpNLrrmxHtHdXnrEdDuoZ7o2TARtO4F-6tH68jBlf9K1eUSzR47qQfibhIybq3ZLRFeRFSJbBK7SriSLb5RLxHZsSrrZzaxtsXmQxPk-dwktbciCIvubN_JYwv9tCUEkPNww9nLjo6kM0yfXOEhlYWrY4PP9lyvEXbMB0ljhj2iNKzuxwjJzd4r2cC6JqCP57pZMiqoRK2fhOjktgeFfiRDiVrwnSzLeR6K1u_kGn1g_nCNC5ItN2HYhzvUmzZ5_gdra6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYYC_ttINKqjkRgrvIrOl4DcrIArFs69dhCc0AsReC2TNGd1nQb7y4daYMveCzBc6eGD1D3Ntg1VLHv3054UkDFJGFDpvOtGsWb6OeWE-RO9hydO9VNEsMN19TCF33Ywwtiaj8oqWhuzNhVZAt6mhsbPtWDSgW02N8pFurksJ3ameT2X-tS5cgfxKSEOq5jUhl_zNe1SfWQiDHr65EK6WRlzHhAt6F5KC8QbQ4KEXgVE52zMxcdKGYXIK2r-eK5cWkRL9ryKARvPMggF-OYjHf2GQYRc8rb-Am4OtOC612cNF0db3L6iRFxUwMDkPX1YVCcJsztjkz1bu72QUVQ02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUAJjQ4Wsf9PtY2M-9rS_KgpQGq2UcmOGHane7oiKaBtm0H1x6ThK-yMQRq8A3k71qa-lv9aEYPXqM5Oyh6irHOJ7Fgi50pHMxSa4m8PEY5Lg8vRUawPp9out86MJsIYwQTTlMfkDRyzw8HSPAq5ePocVYSBiOEVVm4ZBMiKjxPTcPaxgSmas5EYh2Li3cqPY3UgjVG1tml_soHKi-zCNrQYx0iIfgpMojkb74BPfZwKa2-QegCK9LCvFnMn_QZJv_kECZoZ641OzlIY5Pni1omfmlqDEkG1wkxx3JDdsfDpsxQ5Kz5_O24pnWanPNMmdONgr_Lx_8-QtNKAlD_Wbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJyciIeaQmNZ9sAlXKpDcCjvh3qy-jfKBcCyH8c6ctC3T5LfsW_doN21gjGs9cxchGLxBntAJxiokGS5I2jdHBF7akpaFn4N66r2syq0n4su8AyEsDTYd4n8Czbqr-z4NVdaad-cskf4QVzrD42VO_wNd3u2MHvZWuoRlQQ6qvfBECpJjmFVrZR72saAbP758Bfb29-Ogc0pTnBeD9GgfqQB4pbGT0BnZUuk5bs3R29HE5Z9W3m6RzkP34NeXGrd5nqObHoZMdSicp9F32u7Zn1WZw4OYj6aNAOAgS3sn3wg53I3GdO0LJBUnOfiOSGt_RcanUN7WUpaKivzuLekkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqaLPPA3s6u6sOuXf9VwzpimG3enlUmg3SZd931uCf-4l9jyiJ73jfmHbWUkgoW-f9UnPCN2lUBGd0NzpKOwAkqVNy-al2NdKibg7855RfRIfCQ9KS2X0RhgfhnDm0DE7OL4qxnqf7ZamghC9QCX22yB4PQj9RWi6RB0qmo7yrkOaad0ASMKUb5Krminm_epQXN8OMNvVB17W5YESFH8If5K8mm3QzGDh6xpmZFa6m5381Sp-WNntqKHErgsKe3iPnNuU17uHXiQDSYEom6f0oXqVo3r1jbO627vDu1rpj6mkcNNYevDK6npfh6TGmm83B0EJVwMdwjgtrkMAo044w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcoj5l5x6VrUgjVlvdNbxIEftZ2lcd5PJZYY8LeBSqECZhDIxyv7ONqscSuPnkXfr9mO1UYVqKeEtGs__ERzCvAf-GZPv0_G5v9MVXOs2sl8YENOmii50NBcPRP2B5ixychOo-ziKaS8Q9nk_dhv3pPXgbxrB2sYWmxATY_02Um9Kqtf5mGSvP11kO6P0BP1uJY9eg5x6386PpZtbCQ3Yrq8klTNcC3yQDgRHrOTVsGqdRJR75aoCL5InBb8-HHI7MXRfH4z94emaj1EqxsIgwQTo4nYEXDR7T5DNmWyCI5N5iaZ8W72oMl1i3ZOjwxmcRzXcQbLb3x-OuerfVqCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTaCbFIbM2vHE9k0S2klSV2yDrZrurQe8TNqzqhBL5UwwLvLzKB6DGqs0Riq1ju7WFD8klgCjN4OZNn2fAbXatf-Fyi9FXbuxcU890itMJEvi6lRsIDlAwUz8X2U8bolKFKFy7fr9S63YGikN0FAfaHxyz6NCpVRHBjRGoAQhQSQg4gFGwj7bLGB3JFa_ZEetJ_mG5-3BIO8PMkgrCgywEvxnHYk4zVFSR8FXBORb37LBetA1BuGy-kERL4vg2m6EPFMOtgyXxRFQsf_N07-G1DZTvNaktLjCL-96UFYM1b5S0wjV-HDGJbQxFl6fsbnfYY47z7jyLR28nGiitpxMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNBrgqQ6_bXyy4GNiKqbnVCPhWkV18Yfpbj5bUWvZoDAMnGa1hgvzKATZ6Q0jj7A3k_MlyX7ZFggWEuF5BaaZ-NigI-eS2UGHAVxChv3UYjvhA1q-sYvLJqAKPU-rKvGWuxBiMfmrQTzpKllBLPFkGDRzQnlPDVPcxGo8htuBDvQ5SJ_MUSZN2Tnj--G-LoEtsmFE94xoG6w_1XbQnl7qR1rDtGSBpOCBjPSAO-6m6wYOtnB9MofE2LADEGPhjO4EN88fAnKnp699Fkl8uZJXCJV1FFw2awRzG3v9SW_Aedr5gdpKlx333EtZr-H4Jb1Ps52BNnKqkU80azBUorpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onf_c1Wr5HYng35Mgx8ZInh8VnNb_8BYDhJAOadfR7-ATAi8t--YEqDSY1GSUTKV284XxQQKjXRrqI1JZiSq_QJRB7YvPSu9ODlzhwMA8wnSWK_-PI6rqnmAnkKjuzkIH7CZoJQY06Tq7FbxIaytLWgvh__l0RdE0UpHYvaM1q5TYmXleR2cH6f58dTf0nqKNRU0pgJ2a0p_ua_-6C_vAjqbc3bJFsIVXsPK3bKvXqQJxpEY8t2ETGvxJww6I0PxNyCGK_O4l2j_zrlcw0TA6yNXR0Hw1Kgk52mesN5RsgGhKob9rxD4b6XvHRD9XYFtZrrNlRkpmtz7W3kubN5kUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-7rfm0wHPnJ3Y9ai9tbSCwjTFrkPaiELfiEYLVhW0kvHURCH_AnZMdvIlfD6Hx4IbUF_sE0NaP8h8FrpaWwsJnr-Y8MzRRnpYRxPYQhLE_X6KC8nlziyLG5c7WBAiTs0jj5NzHohvuYNVSNSpid8_uBbakp6pXUwSdRQAaGedF1a_vzhfh2vBzVlMcQqAhU1FWV2njmCNBICV_G0r0G7szjv7Nr0JHciOtHorhyGTFCdKen1gONjGONBmc26gF3drLooJ8_QqBljq3B2mIwtbX00LSH8iRVhL2Vj6cXwug45gtMkDi4xVdexRKFfNaRskpiPbAO_42YulIUei5UPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnjxtMfg_-E4Iii2VlmIvMHqRzuVxRH-pTFAIfHKAtCXAjx06qTOdMsvEOGfaiSCrzRD3OKKCKWcs2IxEaB2krv427fPy2W6ccaLwJhLL3be3VDfKoj_Vt1fIzSNnp_pqxtX8FVCZLOXS-WcQ5LSqutDGkWl_zVOGXyFBP-df3RUn8x4sYQHA44vcR2e7RdRsbOYdXBfefEKXMLFuUo-COV9V7aUzCjjzg_CX-ZPsIClxRwkLqokCe5X50jxZiVeZKG6-Kxq0a_P-NBHWCoXVJ4-fMm7d8gf7JpnlCCwH9rOtII_T3wlaWWSL9_iwXWnNisti9QHDsT5aLAG1L5WkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjwYR5NUK_6D9BgodviTaD3SDKMoW2eOvso_uAiS9KG0pXvmYtQw3p_BKadoc6s3LI_79BCW-vAcvkKTNiGSJvb2rwLu7HtOsDi5XKYDhjrLMb_g4a2-vRNRxn5LB8tho3m9yOfFHEdM2gIPcC7d910PkztYJz4sahxXSoQ1UGlhEtRhEJNetgCKeq-nxV1jr0hUBbLWTLir5hbEYPXYg_66dxAVGzwDcjxUX0Z-1hWtxTpEps5Nk8m2dVks3MEURhEQnG2RiLT_yp26cl29SK0Thc2CDPyfEoCKmBEhcwJRD_9cuRCZY6asT5i70ohXkgtZoIKh-lM4D7w2Fd6MEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5JtXucS7Xetxm-GAL-1Oz4D8MRocFfERShrSfVtPSkqcGIA8LTju3V20Sn3_zH-8CB280Nr1YzIOGN4lYwuo78wN_rD3zHIjkgO8kC4R3MRbwAXn7I2WW7UPA7iY71lLcjw7MByIdJF8Kp7JtAEOaMtL_iQH5_46vH-aZV1QsMCi_m83hKX86xsbEshxTv609ubhXmlGQa_KzaCjlOqs9q6M8ASbKzzH-iiX4OQPcM6KfjLO8C4vvxY_1IgxLndkKeR7Rz5e7XqOVpkkextrP5egcuL92jf061j5qPza6sBERoMGCAxWyuJJcCuY8gMdb9KGaleavhLiCLUiP8Lyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTaur2oZBGEq5zgkxKNU7bJw-C_Cfi0A60N1kaprr5Rlso4pn2wBdbcRa_4UzP3uBcKwB918gApFopDtsC7kdfYdIU9VNLjysAx_kWD6Wt_Q0TokWMNgZkaqYpS-SbqCHe0Ua0Urw94nZyA6fxDCmt4EcePz1TkS-HwXf-67Ilhc99udPPSdE7MYg-ICl3R0CNSXDCprXPTzNC5aekEzR41581r4GGmguZFOLc_QW-LV9XIq7o-GXVACVPgOIh9URml-iz2l7f1kAjY6T790fPm0KtzayMMePZhWqcmDKPbMYxARmaZKAL2Oa1qXzNtjF2fTwPaIzwIMzrSSgqt8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZOiYw7QwXUGzjL-Dfzito5yUyaw2fr2RwVPDu7CnoAma8swctvn5-t1cUFwLY56Q4IhHk61aZ3cl0bujfYSn3Zrw6ZSs3bkPJXCcMYb9xxf6AtkL_2UsYj_5lyJ4evFq6zpZ5z0kRefmS7UHH0B91PzEayMnyx_nPLsSH3J5MMczdoHv7HbgDbT5ZH80AwTPxnWn1XsYCXWVZPxLQ_DWr_WIr3tnQhezUXhus8LYy7fNkQT8Odn3fXUH-d-gDx1CcqrjOe4mbVEhcK_DxECp5IRuYZ0y8NePTCeyHxuHP_xFKlD7115pRMSvMT7Lb4iLrGE1hGo0z4IKC9mK4SoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqal9j3Df9FjyGz7frql_chD0oMbqLJg1taxKZ9fwWRlEfo8sStR9kd02jPdPBgfWH0giFg-eveV0KEXITAmZEnku3OURH57b4lSl38efx2Yd1x3h5xWlrGppukgtmvoAMY0h1hzbUGulQxMyll31-aDWVfzkcqn-EvlyvCV4PQKTFga4wKe1FpAGECOxnpZcjJ4P9aGqG-FiJBgf3Bz91Gy-oJtqN5WA9_rpQosbRwr7P05KS-gnOMy2AkQqPQNxrWSXIshbJmtirCzUZL77R2q_FY885frZXEkv422ofs2C5s0HmMSMor-oA4qd9lvkAkXzlbeFK-4qNCxGE4rIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0o7w-uhpENG3jDAJuY6-7j9PzS6cZ1IRG7soqzG0d7o6BRVMKfkbNgBLye1FsACfXFtMKK6oeyLVrLcCW2phDUYJYNr_STwQ7AFqhmPoKvGKUkfjDcLBFCTaw6bjfW-nEQH77KXXOFFdzLQRCCAr31Q7C2xuO_Uq3td5fW3DWrXzG_9bZBsAxNJ5lrVGW0zbYs-w0mmNN2lwddez6yeZpKXrwTlzeXN5OuHWI5ztMk5lJhzj6sQMhWTXOEo2IAcl6HSi8oYqwr-lOlmRA72IcOboubUyS7B61-TF1PKfFyadVJuR50acxlIAxd9BBL0o1gokR3VW0AE8aNWCFJnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C15InrrEg6zMfhYgPc_BRw2gULrAwiMCC_t6jMx6S-SHX4-zQUkXq9W5Zzi2-FSjMd0lx4D7qQs-b8nG0w_Pm7uwPgiBUYQd_F93hoPPRra9hKdgHhjPyPEmIW6pPaAWbkNBaNhseUDbr_rUYVhfOiTny30LmulPY8Tk0IYePe_xf44RHrNnyryITgdfKV_Oy5VWLspbXSXuwstZfAd9D1dLxZc-E1ktbpk5QCRT9XNytRitKtvHV3RkFJk3cMmYCOi95ktgTQIBMkIgC5sd-JC-9uxWcM6fYIAYBGWuhKmS_FAhcLRgSJF1Mp2NTjhS0c52n6LSBA0uIO2nt7QLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1yXzquVMLt8MeRADKgEsmJnWuuqT17Dm0t3XjBYB-aURE2S4BoBg_ScIQG9hULDydzO5OXCrvvkCRwnctdVGwNNF7Yz-RcbP7uWVbqcABghq_vTl27VXt46PeaHNHEwJl_T2Nyzh8KYY2RIsz0HDYgu-cvKVGZ714wDvx1pMfQ2ZXbdfeWo0R9Lst67oDrPluiJZTs4J1L3Ziw8t-eJujQygNG1Q7i4mOQkCP6AWV-FE5g954pSvnqgDb5B-UmAS4xda8DwEfAFtuK3YyrEorx03k_WHGN-COHLDuf7sYBaZfEHE2vxUtM2ACJjHtXymV8p5XL_Dd-Z3yel9gKb2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=tpluHhpLNVQ9iuNXMDFACwYgOrVGUum7SYys7J8MGobF9xZMAdY4PTjL-0rm-BGj48zJrDJ1zStofYymo1vFadUgU3Ef9Qw0SHl6tpCXUNSYcOOjTI7VOxKFyvc8-mJvNPdJVb7uuz4FNusYYyY0sM470lwhTVvivk9uDQ9hxxz3SvGeyTI7WKUnf_xRzCQaAS69tELDQkGfqIQe7u85m_Kia5gMFUYgfuuPmWo0y9-b29gph_xt5gknqWpLBmoj4YTkKjhYjd7JJJfpNalX-HTmyp5oLrFC_HRNAworv0pyfRS859BM5JRWcfcpvL8k7h8-S5X9VMWQ9M75xR4gmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=tpluHhpLNVQ9iuNXMDFACwYgOrVGUum7SYys7J8MGobF9xZMAdY4PTjL-0rm-BGj48zJrDJ1zStofYymo1vFadUgU3Ef9Qw0SHl6tpCXUNSYcOOjTI7VOxKFyvc8-mJvNPdJVb7uuz4FNusYYyY0sM470lwhTVvivk9uDQ9hxxz3SvGeyTI7WKUnf_xRzCQaAS69tELDQkGfqIQe7u85m_Kia5gMFUYgfuuPmWo0y9-b29gph_xt5gknqWpLBmoj4YTkKjhYjd7JJJfpNalX-HTmyp5oLrFC_HRNAworv0pyfRS859BM5JRWcfcpvL8k7h8-S5X9VMWQ9M75xR4gmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUClkzWGLYMu04RoCf7O-fXYHeHA306hsudeZ1wK7z2DX-6JTV_g1XxcIKaIS9QuRH56sXl9HziYDLQxiugJ_kJFqjdVTu039IQYBUUyLtLmEmcFraL9qtRnvpR9h7B2e00jIKGa1VVZmQvLymAbLpHo-aJQleGlQUb44gEMrAfOpgwPVmbgWsOgPSvPE-p9dtF18_TPa_Op-XT0VT3CRSe8TQQnYABnohEMlNp98jzVrD7OCxeYMD2ka9BJnRvEO-6pOsr1ftai8JUL3KFRyeR1iqDxkC-oEhmZg7fZJBimCkGq4EvwQLckXepl5_LG2cneeQ49vhbq10CGQTLXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor38fRZ0X2B7J26MOQaLqQaGPLHvR56QRuFapHuu2hEA8H3Aa8A0XVypK7gdHIYStdYITnoS4mASL6vm6B2gHHGsBGDVEFxh2HLKUTebbQaJ4mosx5zHjkiTr9_jzba9EY4ufO9Ly3g3omQ-fvXuKMRLQ9DKsGCDV-UgdpaAxNTpaOcIFd-bbMsbU11MX4oMFE331YudxsSZGZpUqRObtkmh_qaSdMQGlMSZxlbPRLoxjy1A0pVMsuEbvJOSC6gU8C7dBR4MWo3Pa_lcCV54R3vTsiZ7PIBz3CiY33tBv40rKVvPSnxTzldX0LyNRdl3L-elIZoYsWhDXb6ZZUJKy2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor38fRZ0X2B7J26MOQaLqQaGPLHvR56QRuFapHuu2hEA8H3Aa8A0XVypK7gdHIYStdYITnoS4mASL6vm6B2gHHGsBGDVEFxh2HLKUTebbQaJ4mosx5zHjkiTr9_jzba9EY4ufO9Ly3g3omQ-fvXuKMRLQ9DKsGCDV-UgdpaAxNTpaOcIFd-bbMsbU11MX4oMFE331YudxsSZGZpUqRObtkmh_qaSdMQGlMSZxlbPRLoxjy1A0pVMsuEbvJOSC6gU8C7dBR4MWo3Pa_lcCV54R3vTsiZ7PIBz3CiY33tBv40rKVvPSnxTzldX0LyNRdl3L-elIZoYsWhDXb6ZZUJKy2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6CXvr8V1pobHLyqI5g42zFHyNy7adeNjCqG5rKUmmNQCqPdwQ6h1Nm6GAx07TKRkINUEJE9eKQPUSDl7fy_MD4E4Yo3l_ilguVftS8VO6crOsr2YIWgYH1lncUYHo_63vExzzl0g36VPwXPqeLOi6-Ymks2RPLEktuAzSpUAqn33v5iXfwCjSr_JjcHz4CumSaMf9vdIlFvbgAeRvsUtO1vxaJNIQJjk3HXl_U0vk8AvLLJTITiTe2F1EA50gotDkFMe0NBq-rCZzOTC1j4D3sBmjixIcnDN9bgmz08OGEDeb7GLOGaIGc25Zqf20zoFcF8Qy-pJko-DorIKdaLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxI4bUDkNKtICKgXNSw4vQMN4Op2OfIpa9Or4YkmdXv3vy_x95U6F8ebjzYHvKwBHLVcVdauIyM_mfOYRc4ZYB_2zNGSsl462O3VZ2vGc-2b7Vc6rpbkfioS5s1Z6XkPNwCXSVH5tM8KZVlcYLEpjpnDwO8ncyEZjc_tEV1bXGvcWQ89Xb7G_9y7fblogK8Tw1cPgRdi8bRyLfkmszkRfm9cr3UJsG2uTdqMt9JX1cYKaMdhgFQZZm8xxrOuBvv07wGfuTwlaymb9t5esOZUJgdHnryR53zBbJ2ZbwGAO1ymHf000dnSxmvFylh0ryYYp1H58_lGkcbGI9OjC6yByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VssSaIYVpEhTJAbn12Cjp6QtepqEL735ZPJxt9MG9wJQ4UXO__dcGadj83kNaeckdQYXCUnzV9tSGqfivB2_HEBCOzXsztPKZdI1LMlrLUqbTMpImx9DjCfQPWoNZMUd4nl8gf-PJz21jxO1vdveuYXjMhRDZsK7SglM6dNL3aIXOjcJO_LnecCR_vTQq_HoVJHF8je1kpn4kantMfsIWTe8MJvq363zYdzLmxOP8K--SqDWZttWmeVmhD83NT3ZQGh5CJ3Yb0CSi_Pild9aAqcjKZsmrdV0BQekSUN_k5S_B0YVrj3ihEL6qnhpimRlI_v4JhGiZ5vXPolp-r5SFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD_RrD-Df6FNJPSXbIG69ldAa36NlIT3Kn2DXHkjunwLrEI19hDs8iS3zY23e096lQU0D21vi8KaHwPqaqNg9YBedi4BIcFam_1aDFIyfF3IpTSwMxtJoufUtIJGr79gFYyKNzxiitYWpcrCVNu7_2zIWA0rZG0emx6bfQQneG8590XmMUEtSXgh4267QFjC68qzvDDDEsHPfvuT5dDLHSwndcO34333Ejlo8zmuOO3GDD06H8HtQKWd05icklClRg4ZJF4EWE_UEoH8WqPYBCG1eWLVfik5Tip6ymhpQRomxNUmneCsCumUmSfeBWEP-eYWX32BRzw_lhpBC6ml0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsr0KJcXa27dBEizNDbIlpGd5J2Fos6q1WrY3q69bWZX9WMmK57J8dMRE5txkpGvFG3i46TWCkbAKVyHCaHAaFZeDfJBmK2AFOFSCAneYm2HgkQhLLfX1wLYeEVJ68lEVhtIo2iO-ACSCGeGx7YUyw22QAvT2fiy1_5B-eVKZV87Z4mHJcBb7WiSnCXol0_J3UmmxptKeCNfGGNck6pGN7Gj93izj10q2CFBY6itvf2gNsNJBVpH2qNpGVQQPjkRQvd0_zgJeajLXVX623XTtCFcoT_4tZ-uXayHU1LMNkq2Lg-pJMIatxal11SUD3S9zXwdeXf9TZUgNymVgeS_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E403q0paUarFXow4cCQyvL98nArzp8t0wEHECHTqb7u2XbQMq-FjcdqD1-c1j_TMpitmuML62LD3H6GYgQ_rlPQIiZS4dCY2ZNKhdnHoiUW8fgs7EkT-1SXzLeIcdcrSpKC-OcauVwrHdY1lbalNBjagNnmhcQ-p5qFzJBnp4IqniCmg8jV2djCdveYasSGD54opJixdP41yGTKtoDjLjlHOLM1LOcjfwGgj4loEYfVKPsQi8l0gpdISMvfdveQHOp9w2FgbVybLn1OgYXvitIoKjVGOHC9kO47mXLWXw-ffBSlftQKv1mFjhdzQTn8NI_fxMyw9QdXsG3EwYOnZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgW_mkbN3RzcZLU06eH7GqhFqvXvUDjQvdK3z1-ZeyhuzPmTiH1tXenM41zhc7P3DcTFJ_UZ311svvJtACIQeVOgsXpDeaPppFe0o73dRQc2w91gDpRmEDkmQ_brsrJSkNa9RjNNITl3nt3cCOmLGVmNn6tyFEZ47K5gXzHDPJy5pZ0_T5Mp8aXUNcoo1055X_uS7BhYvsXpmi04jDfSo-K7ajQQMvO3EXcNzGXpjiqnOdgvA0Ca1voYR1XFc4AIc0nbOCEJeY2UhLg73UDeOXL11kMso50r_YI7ZCHQsRUQj4pHEfK-nYM7zeM_qTPJarYrCbkDZEUjk6Ru3sj3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmfDiC2L11HhDuV3JU4hMiSXkY3a-XzfVxbU9DnbyU9rwAs02LjZDE19MCH-8RJPgt6z9EMTbWnP5b6FJktjkl-F-yw7A0WflttluBgyRCB6bRB6sg1xkggzx-EtLPj7wvqh8lLXghYxbLj-geo2jT8n4McWvV3_6ZXXTXiiidCpDmpx_IzuY43l2MuvzSg8iVUtJInXYbiCEFSkIB2Lr_zBy5AmPJ2ycU1dK5WGeVAnP9mUZpqemPEkdlYMYrH3XyEe9nnEEhdasIjpQdGgfgnvvCUL-U7vuklYpFnzvB-5zH3MVj9KssDAcecpz0FA734iLJF4POnxBb2WiY5-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QODEPcE3jOPhfZx538hakOFvN-3B-WSjzaYz8GUxn5VuW_jOvjhzZ7KoMmWJXZl7zxBLEBJvgbsf2zhWertGFt-mCRO7j_kENsLzo7CgaT1CRpLmkwTjXWXhuJqZy2GB9Hfj0BE7sARA9mQDvoChT4fPMhrCOzbmItBcTiSGn2_vN5segIYXAC32XUJcuDiNohjXTCkKQkjGaFvVuKMLAmQypGw8owaBX1RcUbXUQgVawb1XSgH06f4AuvB0ZNOlEnan3Zh8-uOD0RDW3mtI0w_u7HaJ8R8GC1-7wqdiVp6ARqAOy3ayyglcaAjzFDFDR1xVic_v67huFHxknaP1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAbUzwTzDOboJnbwssa1C8ONokQr-7fiRGUBzZGNQ0oN1ua4gZkIWncS6SjlDfKN124boAn3iHtDyvLcfs6-a1b2Wh1xH-6tlvoLbmMaurVemxDZbnIVjSoHyfLpn2MnAh-U_8oDJNTLXS3OcwZUQVniEy-ZL9_KycPwMSJcuspcn70WE9GlCBsTMo-Fq7zWH2BsRzEMjseOyGPF3JTN02pzPMIsBtV3Gup8xZrXXFdmK-N-ZP1ndcvwtbDdEXQq2vpQXz5HqU3wt_dRmSc8guiOmooRMjjZg8-PY0iAVxiDJrvrW-TRfzlyjMbeaOaERSqOWbpO4Fi4zdU6RYa_5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbLPJpVx9SmWxFjrUIrSEA4OMlj_5r-MG6APHDkNfJKd80BhJvKionBOk0tCe9RWmepCDhuagDl0pykfe3oojAuRydnQfDkyxL0fwmdTocYZkD6Bjs9JXi31w60gc5utZ-jagrgidhqUoJNyO9Z-YH14J81mD8ex5sB26Th5IUrmQ_lWfs0EZ_MN8X0wjh3njJ91CJ3ASwWew0K8CxX7ekeozGLC10el9fc4I26vZmLnFFMKjjQX3RcPVq2piegj0LDs6gczx-1phRGb3V8QnWRZsd50zKs2Sum0uxtzrCaFmqK9Y28LZIiBhvslmSJjzBvvkJQKIB9MZQIdlcrf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=cEkllPSM-rlFWIXjQ1TvyzzmolCTtkGZ_ZZ4QVoFTl_3IiuS3V0VMT6b3i14gj8eQ6B_VIYlkdZI9NfWgiWhuCHx-GNUfhTscmqsXw2PmnEHl45aAvh2KGMY31HYbsXyUHiPWTxUZmjy3Dc1B9_VaQ9FoqQo287tA6SqkTR-sxtateqPkuHvbe0d7Wt1o_ZLSaaAFDndZY5EkrzHIppZpV0jdN2ZmRNI58ZJFe9-4ZUdMAyw0LYWt5F97Xl-G1kLcx4SEklF3279pUGQyvggjzLvmrNJnlK5BVkhtpjUG3PGIfQvRHVCQbXOYJLzEBDymWxD91oBfxi6hKyiuOi6mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=cEkllPSM-rlFWIXjQ1TvyzzmolCTtkGZ_ZZ4QVoFTl_3IiuS3V0VMT6b3i14gj8eQ6B_VIYlkdZI9NfWgiWhuCHx-GNUfhTscmqsXw2PmnEHl45aAvh2KGMY31HYbsXyUHiPWTxUZmjy3Dc1B9_VaQ9FoqQo287tA6SqkTR-sxtateqPkuHvbe0d7Wt1o_ZLSaaAFDndZY5EkrzHIppZpV0jdN2ZmRNI58ZJFe9-4ZUdMAyw0LYWt5F97Xl-G1kLcx4SEklF3279pUGQyvggjzLvmrNJnlK5BVkhtpjUG3PGIfQvRHVCQbXOYJLzEBDymWxD91oBfxi6hKyiuOi6mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrNWM1W_Xtg77T-h-k6_bFeI5egcl4UnL_qv1N8lWHDM1szPIv39jJH86Mg_ebUFtDQch8BfUJRHdcJ0N0KgKSrYThJMNzMVa1HAVZHrsYZ1hHZ4AH4_UyhkJH93w3G_PdOV3jB8QmoZCmbccYHwCUknu9fCxfpqeYD3jVQ6b3My3-TElPesTXh4T-sCCfHHFhMBRS6wwW25n3pctPhUz7Z1rdUjY9ohiQcegrq67sT2wwteT6b0_zkAkj76UvnBC4Z_f1dlvvMhdEXLdyz3Vjgm7HQ4s4r-pFS4rEsbjqwGqqTHQ1Wz8zn3vp79kiSweEwWlZVmpEC3ZPJL4RamQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2BCH6yC9AZCJCuWV7tRG2EZ15RBqlQRFY3wNseAnpG1esRrTwnFe_e-YNW-86M2-u7FPDw36iTCa8UBH5DMkZCe5DE4KKlTuzvKwpjxQoTJMj7Rw0fFfJ3S9kLX9ixwlou5pVPb-44SpQ7Dh6HQzyUVKt8nOpJlOePjcucsCDXwmVfQdzFaEOAZXFurB4CwJxPcYIG575fyPBenZAjx8Vo8fre0UFK5JzyBy9-0iDVZ_2hPQbH11mk0HwGbr6_kWqesWXgpwkP7rY71XUURZL2QjNTK03GsGnGXzZ6_gpyfOa-Ar3rj-bL-M2f2wPAfaGd6GLxpGNtDkvpCl18akw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnv3idnY8MK9zXgWyrH-E_onW5eSiIh1hsfJdVFubKiEtNPOK3gRvAvvvlNtamdKNr1AlpTYz-wjHfkyPbksHqrSWJ_V1QEYMYZIzK5Kgga4SpatjeMzystaCpWC6QW0YemVcs7bfY14FBn4q6ftFrpty-dkjG6ZexuGARBFJ0kCacbwN-QeakIdo013ILcDmD1afIcwD0i1oTa1AHNDrtaTvc0O2Cr8-7B2dbhLo_N6hEqh9SzWRweqCJBnCKUJmqBXq6sJDM4Ekz6a_eOvd4Zp9tXyVVi1orjr8b9stOsPiZsC6PwjQS9LtnABqPvYhKWiYTz4BCXrdiLJKGTH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzuMoz6B69H0A6nzuRPQiaf2QWzflyOE8p1gUorO8BEtj9E3dAWfFTo4LurF7Sb7bYm0Gpz8GN9C5iHVu407U3tg8ZGgKaYI-QHiFKCOClzGVPMMHSDzE62f8Rb-OiGA8JQnSoDT7vkDfokMcvG__gg6tKQPrYSiJVJTF6HwpS6P_3ryd50B32irtnf8TgAqYcPUgVfN7PuyJWYIMnOu1eFhvuKrUa0--Ch-Dh2SSrbWyLZT_IvxDmPvwv9HetU3yHwH-kUY_0tAVr91bpPZeX7kkEmiQCxy6Jl0c41bthXPlcNmPN4rJY88ahBLslHrS8ILfzODzdlMUkH2Pp4Kww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtBbovUPvglq14JXCJSD3cEzNYa9JkWKw0Q-i2TnQgjX5yF2U3bXgvc3OTfkUm3NmPjCrP-ogZBOZwE0TtEwSCXV6wtQKCP7EmJUMoiRaUlsaNmUqXXCuimWWiO2gOX5aJLG54_yuRCIeqNi-15Qw_C0d5JNPru5A7fKUSQrJIbUBWrRbt8i1WDHNx8_R6GPvAYmLxgu7-ZaOgQgszzKVBk08iVa1uvtHbHB6ompIRZaSl-w-_P16ZqvetcSMF4QZYhJXRHLeJ6SzClRUTsMoNSQlDF9tvoqwr9gCVUdTbHBOE8WqF2_6jzJjlTzWVf4sYmGPxta3sjFU4S98VTMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlcWu6TuaYkc-G2ZFsRAQh0ZwDgvza5VIMJ5SIVfXTZ0rWF15rhgxAK0CwbPRE7Gus7Lv6xCA_jYDHPs3b7DFy9JKHpe7kBHJ4NioKQCjxP8AhLpi2eGrqRhR0a9cX7qlTBM6rjcmdQ5tgZb57P7Vf-2g3VzZxadWCEzRIXrOlrMN0jI0vNb9v89ezEkNcu3vo7HOwRfo2Yn1VWpXyB-GCiX85oNvqDAT7QyP_ilF1b6gv3ocGeM0jub78puGeX6eDTX6JNR4Y_nLbeZI01-Gq8MadW7oNejIj8yzHDwwxZ3O7Jh5ftUNzmq8Snu6aGiPmumvetGGyjy1HxJJXUEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9U2MIMnUCNHYCifZdXu0biB8YzUyk9WkSF_jXYBlD36d4HxkH2M_fXMHs406LSGGqUX1iJyUo0t3GTE7LdbR5VFQrRZ24zeF2BGshqSPzh6ECBpVBmnLguoFEeDuhSK1pbTd_G8AlSdE6WiXA8pr1VRHzyFPnNFp10WVzXTByR7yyvPgc-NZRSSA9MUoHoxAowh2uIajkO_IZ7nh5szuCwB9nJvxXzu2AQVNIm401AJY9vdl-tqhGWCo6hqjGzh1YpwruCZmq03vdr-v1FMWywotf87pw24hiIX-QFd2ocgcEZsW5sPqkORygEl0wnKLWJgBJp0naiQiXHKaBhnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=YH0RlSnhCrbqVJjKVVNaBtv3gNBQ9cBaqr5W2hpXbHlpZKcavLGEa9YL-sCMBb54vk2uuRNEb9Jh1NVy24ctJCtGl4TKwUFOxgVZHoGDN-UmrnwqSR9mzjcP7VL6buYzdfp-jgPMJ7u9D1V4XolMKXDvILRfwkz52WnC0dBbAWg96QTwHFD64E-0phlHC8LwpKv7dtonUe9bmhV6piywWaPH8QqFioPBqNBfabow0xl5gb1v_swc0UL09gIog0SPgJ2zf6-Nw3LrMKOZOuI6WM5LhKDre4jqMdWvO1dRAXjEJ0xyv5ohRmyq-DuOus5uTwm3_PdoopByU7c5TT4yaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=YH0RlSnhCrbqVJjKVVNaBtv3gNBQ9cBaqr5W2hpXbHlpZKcavLGEa9YL-sCMBb54vk2uuRNEb9Jh1NVy24ctJCtGl4TKwUFOxgVZHoGDN-UmrnwqSR9mzjcP7VL6buYzdfp-jgPMJ7u9D1V4XolMKXDvILRfwkz52WnC0dBbAWg96QTwHFD64E-0phlHC8LwpKv7dtonUe9bmhV6piywWaPH8QqFioPBqNBfabow0xl5gb1v_swc0UL09gIog0SPgJ2zf6-Nw3LrMKOZOuI6WM5LhKDre4jqMdWvO1dRAXjEJ0xyv5ohRmyq-DuOus5uTwm3_PdoopByU7c5TT4yaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=TCh1LuMhBISUk-rXcZAZ_dS_ZpizP3hamVPgm__2s5PvCC-fW5SU00ELajtfY57F8yylMqYoX1tLX3bK-HEAtJdi1snoNmCGKkYJHPobwSC9494w52dNiK3vRljpjejR-RJNVzffqW3ISnLkwswzlxxJgO4BnfWQavEIiffWcJhoyytt07T2X0Cr2aF1XfW8BDhelQPb0jup5LvLE_tBwXR4CZKUxCmJxUXuCI0U5JJv54-jdCH7m67fXg5n1zkGGPiKSXIcY4koD66qx48DXbkIhLJ8UUf2xub36qjdbVBt466ll-4ZauT_DJtXFk1rDrnk9kVcwWe2PhueIPC4GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=TCh1LuMhBISUk-rXcZAZ_dS_ZpizP3hamVPgm__2s5PvCC-fW5SU00ELajtfY57F8yylMqYoX1tLX3bK-HEAtJdi1snoNmCGKkYJHPobwSC9494w52dNiK3vRljpjejR-RJNVzffqW3ISnLkwswzlxxJgO4BnfWQavEIiffWcJhoyytt07T2X0Cr2aF1XfW8BDhelQPb0jup5LvLE_tBwXR4CZKUxCmJxUXuCI0U5JJv54-jdCH7m67fXg5n1zkGGPiKSXIcY4koD66qx48DXbkIhLJ8UUf2xub36qjdbVBt466ll-4ZauT_DJtXFk1rDrnk9kVcwWe2PhueIPC4GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaLL-jtYN6p1OIoxL89Ie9Ufc9cvsdzycIy_VP2E_Qggn_SCF12QremiBN81Rxvek7rYRXtVNYud4nPHCznNa1nDoEOGaZz83IDjRzEpUbehQGlci9rmvSMUgEc4-OqNUQ-wQ-qIPG2uO7JdJFZFyrDl1B_9_LICngo02jm0l4M2P2IXbnJIcL4WG7jr2nIO3xGPD1uxSRoVCoxHqC2912VZ0yyobDwfj0PkdGSmEUwLlPbA3WI5Cj1ErmTVCQThCXOpgo-WEJoAQNo8R3e8YB6kKBA7GY45X6vieWBzxQS8LLmHrjsNAAn15fnOvqE4-lWqhLOlpkL4i9CpblP81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcCV6S6RNfPwZuUVqijNqB9seFHRPhETPo-kvKoHEbPwO1cpEQP193iJfp8WnimfhGTzbIgRKtFuDLjKeTYELyFz38a5j9rXbKhjusIjM2eenqf8nPhCCSkjMiNlMbeq-xTpDgXCmpt-2CvNp2vGJVK7UnowdX3Q2UUjsEmgNuT0WtFXs5PnBuZjbb7PQ5OMj5pSi98aJ66mFdeSWP5FRsgcRFyyIqVDBhQDjWS824bOQEXkF9E2GuL0J-DH4YoYS-bg86QSAF9RW6bcmutVGJ8P59hAZcpP0jvqufEnE9SyK2HFsKnmBb5wOmrLw3VyDyBidT8vXn-EjJ0aiDjbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hH1bKSkFaihDR4VRsJ5Bc3ucA5yYP4LsN9Ao54cryC7Q-ursby57ENQ1qUZOYJ7mKWcnrMrPX4ZdInYvXFoNsXWM1H20DSNvIDhFyXuDyF-rvJaKTVcSkIIlL6o0DKuRyQu6me_MnM4UzbYw7xw6onS1unXdY2fWLNegGvaL-14dePHX5Y-Paj6xt3B6u_vZ81HKuoQT4xS2Lvu27H_XE-AK3f53OcukQegtgF0TvbbkYWegC5E92jZiJ4YmNErugCU-ieHC92PwrIXJLVwr4ScuaDe2is3vr3YOKVdJ6EJAq9XMG7lHqHZm2xKmX-1D696JMLRfG5ubctYgn0u9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCuKi8vmkFdLC3waQecFcpjqvdofqQdFMC1cNZZAlWLx-TWzvMUB6D96K8wjnMInr0CdtiJ69hVAkEj8IH_1XQtoDROlhHp02NOrG6IzZuhdAHO1jlUa7MFOIOi08X_D8VXTL7Gt-C-ZAhX06ptVid1VUWf9fGH9lro_FjvWb19fmg9NT9yPDk40hOufWdGmjvBDpdT90Lt_L7alIjBgJaVJOuP8VJJNmK22uZpnTnkcmudU4zAk_HYBCeltpQDkX1UI_ZZOT1qbFGzaY-TMojuvoMYDk2D7S6LYIUhJPa04Clujg1dlYIvSP12hiLKI0mlE1wVtSHmlNZZxuYx2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYrp_dRj6HnTljTLiCU1EtfZq4oQeGFypFcUQBbXCxJyo1vfmvcycg72kydDZ3oJQzfouW-MBmQy1rHb8y9gnx63sUAD8RkmJJlcv24qbrMX1t27EMPU3VnvzN2_JH1WiY0BM9qlDUaqlxdMQ2Jt_dRKNljLv0pLc3MHBMoFPZdcXzss8rkb88jfBumANIfa9jp6MCHVuRoZrUy_xJUl0YcpQKH6bYXChN-dkb-iYmfJgl7WNlokLhpO30xtdipY1t3C0z9eXm8DirY2ZnjK3qbWNH7DvX3mtFZp0CqTLOfcYtuCRxZXjnerwaZBHTkPW4spIQudTDHzDZ3C7iHXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z00QtFrnTYau1MjdnVhQTnAqMgEjXImUZagN5-2IcLWNtNAzqZHICCUIqmaQCSSx7mAFrEWbiOUCNh5yNjf9RCNmHJvxphS8Va4SemNWZ0slzUhC9paRt6cZ1wXCOwB7dQ3N3_GVY41l36nc4u7VZruOjSZ89VsBUH2gmrdWQvshsK3kFKnxiYrdDqVD5Ocm74qDqsuvCyeLwa79R3DMu4rpbVj5QBfo1eCCJX96RSwC2kXx5bQJMWlTUu3lwgUv8XRsfyCnzCOmW90gianp2pn-NqrvxJPGreNFDKopKokGSHk5vFm-W71wQL_R8XZD2OI5tNG4Hcdlf94mH2J1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=HkIy0UJ2BgkWdGm2EqjKAiCeqOeFyB5rcyA6aAFDdlrR4e7TnQsULxJz71xI4BGWjYmttGMfiMFbXv_9xEPyM7ksfYODCMgEf_FP19ipAQH12qtIk4HFxoVK-I9M3Gg27yld9rc60XvIQAo8bw1fUoYmVe7X6M6LDG1rCYabn3QEMB2d1S9BqvwlcYgw39-xQSSIIjHQ729NNGo4t04e2aSSAtMwWWDyImqDHtD3Or5b0gOdsxsZD1EP90csvlnKrmCewCG0Y1roOBg70UjBQXZLGb2pGZ5g-9n4mV3mie5WccHwvkPlXHS6iq-A9Ffb09Ld4_RsvZ_jDDTImBUy1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=HkIy0UJ2BgkWdGm2EqjKAiCeqOeFyB5rcyA6aAFDdlrR4e7TnQsULxJz71xI4BGWjYmttGMfiMFbXv_9xEPyM7ksfYODCMgEf_FP19ipAQH12qtIk4HFxoVK-I9M3Gg27yld9rc60XvIQAo8bw1fUoYmVe7X6M6LDG1rCYabn3QEMB2d1S9BqvwlcYgw39-xQSSIIjHQ729NNGo4t04e2aSSAtMwWWDyImqDHtD3Or5b0gOdsxsZD1EP90csvlnKrmCewCG0Y1roOBg70UjBQXZLGb2pGZ5g-9n4mV3mie5WccHwvkPlXHS6iq-A9Ffb09Ld4_RsvZ_jDDTImBUy1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUnqx0Y57_MAbJm22R_dbEZns_Y5cqecMZPFVv43WSg9-qSndK4yS30SJ-xdIddCJ1lP6ot3QeW3-lqpdS7K7Nz3R-QaLF2qo76Wt31vOrIyPjzqOkJIFc_JIsNhNU_TfPUxpuELSBbi0-r91O69DpUt6yTf4KDlasQSeklsKa6HHSk4JGra67f4HZOqDW2HOExKZuEsN4FVtbpbDYO0zyBsQh_U8EwLTfISbMlnuLKARTe8mRBey6E_qDTl_dOJ63BdwmTO4P3djxxblgu70b0rKdNzOrB3Mh3xv0bKq9Xo5rbILo93DyA9tjYWMDksNRs9YtpzqAaQirPdVJwOJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSy-Rjzni_cJRJruJe8PSBA1Al-2WOZL87tD_MMgcBliQIFonin2VEZautH-iFRKyZtp0T9EKqE3j8oUzeR6xtuFXdwoTWzg5dgYf25M5Ejp25RaxN_EZRx_n7irSStibvDTkNBO4eDPy6Otd-Q0VQoPuSVZ30YNdUIxGljlEZfnv_-Ql2I15g5miPNOd0L_3LI0UaR6e-4hIOLGU0CyKK0GgBCeAepQW2WLerV0tYa-Szyn-Jt3caARi3DNYqqxWpSYiiiz-K_u6raAjXhjVucut-CX0kSs-I5zmWtJRiA6Krgk9f6ung2KM5krxCtShUwgukwynlTDrYokYGl6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5ijbnQV6sOlkVYauW95AhGONaVgXushxVJ5xL_MJH1lRB2Koqi50BNP4DHc1iGoFky2ewkCweq73UbZX4OUmif07Iyfh7IzLmxNIPmfJbvmxq5zXLM8s-vLf8ySIjcdQdPxWaSr1KncfZoiNq09vn7K9EcAKlkKPwy3X2FnX_wec-bWcBH9ymfdQ7-8AaieF8yDsUC83aYCgtKCQsfVqo2XqO0JW7My5MolMyUH2PtVE6zCgDGfQvKpOY0PUjZXGqu4BqCV8axZVARfUOGUwt-U1lkeeGKnUMG9PY5fFaALLI2YJSdk1lUPO0N1N2pOMgJqg4cJVMEB4iSn0kcAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVTyH8J6l-dWOzNFs6d6fQADkCSjBvA-GmR8sbKNrzn1XAb196CWmp_lNLT18HFSMc-ZuuvHwBIx7RrJK9u1jTVJ9IeLkp03R1gVbEuA98nc3Pl4UJnTtVJ9tKly1w7HwxphEdVmoTLwP2-02cwEZRstvcmhQWprWFveVSZncfDdPgO2DoJCU5A7BIY3MasR1BBomV4JkPtRsKzFVfRyfTt8H6rbxxh6eJS5IRewLJzcoxP2Zsah0j2IBB0PRycoTt_s_-YleC-RomnT4QbH0AlcLEBf_uXZ-qWeVA0AfXlUT6rKPQ_y58R65avWYchgsEPHthMHdXYN8tV4sp8w6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFFWN4EgquEFLpyVSogu229pGbFjKOjQ8UIhQ8CCF2tzJi40_wlJSqC0FIgxs8rwRlcL-buckVfBR41AdvRrKxK462nVEhsYkBNLFKvX7l6_drkMjX9nISXyQeeSsy1JlHIR-PhKGV2lqSPisTCKCGOnkfbEm7EP_6RbuKLtRBbLtZD7kcWr1a7Wp_T9FCwWmxhpNHsRa4DfIsIW2dCVXSybPPY-uZVZJGs49kqShlb-HfOmuf_PrgQMrNyqpc9rQLj0xJuoy1rgud4ak5fbiSWu6ulvXLpafX_ACeUvOTpv-xeqVYGyvy4Dhc5hkV8Y24USZsnTls5xMiFvjOmWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXwA9WlslMRRFBfpZPZ1ZXJHVGs1pvzw9_HOwD7idRAiXoRsOLGJqdW6D3LCtTKpCvOTH0JihmQRXcNJUvl96du7c6De8h0xVBeL_uEm1dmNX32OkAMfuS2hTWtKUi7QFaZrv_5836M_yRmlSVJzjy46N7ZX_fAm6TRvaDv9lInaWJEB3iHquIGw0WW2NURkRO2eohPgvlcuVC1hOSE7JLkWniHcTsuP0Eaofcv_yc_tE3AedmG5xfNlLINSlTy7HvV9cSOgl1DPdds5nGbhDQGCQYMuJx8f0mNahxouHJfcXFYdtydwFc5iLLU-hF_ozflNsEVUfzELR2GZ_SSs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXM-y7pO6z5__uPlJW8PJC4fFBH1PE27Sot_AZ3s5V_LI2U3Aw23OUU4Zbwqb-CQ1-EYkPLnRaxTiEtSeoEbAI4tJUsq043MIZILCdikkNG5j-ZiSUSH3kM5kXmslM5NsmZRzaMAe6G8TJKIlhTDGDA9s1RQsGR8VXt0SxzeN5TVThhBRB_p_OlY5PUScpCiACId8aRFbuIQRo3tmoxBYwQ4sVoACcmPPhYdihgeJe6PwPe1S3TP5rXe5PNv-f-VU1PHrWgtdZZkKFhzqypIetqcUG9LV27mKkiopHXMeiJCqa0V2Tv1LjiSaEJUjBlIm7K64KNIx9eR5KOuR2D-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOYjBq8I4uvMmx8fpm-K8i1cAnk5AgRaqFsZm_-HW3ww9gCyXGLM94Mj15O40Cn0X_DqYCMpb6MCk_tKyhPY_LGNwGAvv8s3Vw2jv9M4lGow2foLz8BV0PnRIb4OqZZt9pVmS8zL0IkSTAr5Esepffwgka-akKoizjYDgcsA3oEEq6WQZkrsQ6jyk8lb77yiyxhUX6ru6yzxW6p_vINeYjbmHaAYq6Ag-z_m_izhbtEl_QW2FEinO91KQx2LIHLfkll-5P0hids6g9uOCSUPNY7GmaehjKtRiFXcmCDglADDfhDT-5kGm1_0H3C6pWPL_JXHpPFrk5nOxEAbLih5RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQpe-W_77QqSdvmU5aaALOCh6q0Yv4TyDJFT5qQzaWGHxfucuLzKJfpFKNLx6tCVHi6-74vY0q-rP7eGfwZ_JFbv8EhKebhqAKRAX5SZyNNdwpd7FyXs0ikeMXLJRGyYxDhV3H6wxZ3AO60FC9QPAkJeEaCYAcFozoksYdeCfnu-ijXLaOVcDXLnh8poU2Xtewu5IGdINBVElAGmvxV5_RsNjEfBRsdqzpc5lVdH_vNUrlDuzuH3yWvKXkfL-4RUcd7xsHEXWRUjq6MxDPGn0sIoWAN9vi9qa9-Pz6uWedE56PL1VzFQCRb5j4v8wt194L3NLXAebkfxYcYuhSb0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtSoS7aI85wBlak05fTOo9qAS6pd-LdhULAZwT5_VXiCZpX0vXxsF40Lxx3ILUpdRDYfkC5ssBy1GVpQCCRFq4zClpWUk5yhx-XPViV35zwJC5Hz3RwGlVEbKq40Whg0fWpDn71IlLvOQ7ijQRH5Z1n9vt7FpMCle33XeQBGONf99S7R-_I00nF0hOFHG1uykDNeUUSVIq6Q80NbMUNR2VpYjuXk6e3Vc3bF_JnuqL3oAA4Bpk5ReJrr1DkebCz3_fBz_SUddSzAoVmSZMhyFxgZSJF8SNMPcTne79j9XL1Z1dqeX8tNnsKdsKQRVuSCoSlLClBp550YXc-Kx_9BYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=gBJwPCX90SyNrWjOrp5-nQkrF_FSA0ktKn1q6lkNlyCV7nzi8abn1jKPwrsJ37CvXoD17rGNYfkJ2mBg0WmP_jEmDgg8Y71D_rDt8zI3ooCMz8pUEbjU14dHviO8H5oqvxCWdiopYLwIoTE7_wvc4NlBKm0wcGzhd9_FE4vcMoVRonLI6D2rCFqJ3azoxoQhRVpBFRnF2s9TmxfAT_hsULadAaXq2ZPh97NDOC5fIBe5Wb6lGL-9Es-GLzNpTH1BgKLqaAZ_i_dVGKDOSFh3EpJhXngMk2XFFmTgJO1QQhLM7cMDtsUH--KFpzqT04_R1cfC00Y3dx68oOwH5xJaX6283Zjy2BiL_0YNuO27bLqe-XkdNDli7cc-Nx4ise_c6fe_qAru1X4om0zJQZY5ybqbm8DgiwjOmI1sW7XliuY_xhNbnuWeuhr4znCly9IRAe47-7n5MAl_6oHVjkJQWPbTd5un2cokzHPNk4hgw8_WQHwTfsA29_jpJrKs4l0Ft24AtIiXIL0jzrYaFV8S1zdW-jjQJejUJJnfmYXwBL4VwB1bQQOEUCskhOgurdtORcNZjCZBMWa9l5w6tJFIQ2XCISbf3zhXBYFUB1ICFhSaoIO8xSCkQCqHwjdctV4NvXCtLE1FwxRcoV1KPSFJvdLzlHbIYBYju9Yc3J9F-Q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=gBJwPCX90SyNrWjOrp5-nQkrF_FSA0ktKn1q6lkNlyCV7nzi8abn1jKPwrsJ37CvXoD17rGNYfkJ2mBg0WmP_jEmDgg8Y71D_rDt8zI3ooCMz8pUEbjU14dHviO8H5oqvxCWdiopYLwIoTE7_wvc4NlBKm0wcGzhd9_FE4vcMoVRonLI6D2rCFqJ3azoxoQhRVpBFRnF2s9TmxfAT_hsULadAaXq2ZPh97NDOC5fIBe5Wb6lGL-9Es-GLzNpTH1BgKLqaAZ_i_dVGKDOSFh3EpJhXngMk2XFFmTgJO1QQhLM7cMDtsUH--KFpzqT04_R1cfC00Y3dx68oOwH5xJaX6283Zjy2BiL_0YNuO27bLqe-XkdNDli7cc-Nx4ise_c6fe_qAru1X4om0zJQZY5ybqbm8DgiwjOmI1sW7XliuY_xhNbnuWeuhr4znCly9IRAe47-7n5MAl_6oHVjkJQWPbTd5un2cokzHPNk4hgw8_WQHwTfsA29_jpJrKs4l0Ft24AtIiXIL0jzrYaFV8S1zdW-jjQJejUJJnfmYXwBL4VwB1bQQOEUCskhOgurdtORcNZjCZBMWa9l5w6tJFIQ2XCISbf3zhXBYFUB1ICFhSaoIO8xSCkQCqHwjdctV4NvXCtLE1FwxRcoV1KPSFJvdLzlHbIYBYju9Yc3J9F-Q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6zIRnQWTkIZ42ibBM071oLK2U6Q_86_VAoMhw21iZwVI84_Hv2nJHto_Rf_YH9Sjy7ZXUK8RTDXrAjJ7ND_qV1inN0ftcyWa2yiUjZGPa5b64QbE3pm824Ngb8aygstFN3IdGTluCgLga6Z1nJdJBSI0crbwNUeCUIucdoOWPYbVcpSU69k_3XsueO4KP9VnyIKd0zeGVLt0YSjvSxXl6ApXd_hSZbNhl3UUKb2jnqQqDX3DJItFxcUd8GmLHsTDN4bD7YYW8YmttM3W7MMHivtFFq5Indt5_vBDofcYb631W3CPKSEqhcN5amkig_OwLddt7hnYTtktscuDT9ANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYTAVwbq1fUm9W--sXJbqynbXVycNhH9qQZs8ibX8UD0_tvtZliPz1hTD6M6kIcPv2aU4a4ILqTc-yEJdqv6Y43ObwGuDoY9hGhA1szfY5IprIa6u9FZfBBSDAGgMSbJS4t3eui0jqh4SJX5cPCtaVAQEpFKBsBiOjnLDOk01oe4_mo6bewJJFdukfFOiSaPyUHgxwlCavujBowzV-1Uox5oLzJO9QR_dQ1YHKjXDcVPZnBpVVEG_dtGKQJt4G1BZbG8spM_Cyt9hF1DY0Kj9LlxvFvaxmFQ75KKaM3UHo77g0T1K62mgufuiDAlh77mr8ztavEqHw9LnzhoLILlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTMjcqPouO4p7CjA4_zmuStVAeoUvuuT9-DeDJPGmyovG-JquvN4t-jL7MFOV_ZjKEjonEwN5m-Chb2CKQbxXQMOlM-Td8-v3J6Lrvugx8cILFduxTk1efzZKhfgVguLvrePdkRQqp5E-KVOH2dgEJW7A5tu--elomHmmvrJGUbDjuO7nf44J4twaNTC8FAJipqs5E3TDeOoHrEO3UUZglU_RNKg0Cp8uOVzEwKJR52dIRyV1-BdAU0_BYhWLjDqZpun_UUbaELz0Eyhn7lntS5JYU0-3IS_nfHQpMJ9Z2i4ASKh9XDhoyDRNaU7nhqv5e6vlpkCNN6cdqYsC5Gg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmWroDUm5WbzI_2s4EjrBhWYlnneu9S4BOuL6eEQdWXxNppXPEaWPt3_K0WK7h2YFubu36WHIpUClsSnXYPfMAcho3G88vAhXLRac9f8m0hpfGrgQUcefOm1lRTzBFYpPVXc_C4a7ZvwSWhbTU-4hV45jGRe12VET7PkKdOQxd28YfhGEz8SbPu3oQqf_jmtQW54vu7mRVUQ_tANjLo18Zf2IUZkTyyu_qioyPa6pYCTS9nhQolkm0Nh6ueDRV_BDJw-e0eBY9JjmDxQfT3iroZbWRyQuWKFhN19azfEWKLfnA64D1rsQptXLt0GWHQpdqnEA7DCppwgc1esu6Cy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw_qUvS_Q5LnI-EvfAhCi-toEE4HGWN6zuRpYKdUe4FebFT864c-uCQUm_dAtFOE5IIRyLjj6hVm7XvzkS3O1gFRGVDsTCWibbiieEXFDDrz82y7-O13x_KTkjpAbq79ijVZmT4SQXoZNpvh9GD1fZxHY5h_yIH1fzKoQ9ruI4hiHFyKZj77A0BxAYPzguwA338AjtAQabT7IboGqjK-9A1h0CNasAAqW8LuMtRUUdtaYFDaVs-OeSdcVGj5nsvpHXttluoHUJ6cSN2XAhRIRChj5faa1DfeKsniHEDB2SLRUp4NdmIUwRR6vxoSykvavlCS1KHwLZ6IldiZTzb39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
