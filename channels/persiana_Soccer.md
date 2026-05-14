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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 19:09:59</div>
<hr>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7RDxvC66dKTQ1Wt0sAqwCXiWg2IFf7ZfjtbX6nKBWY1BeXjF_XiILB_nTK6_6zEIaWeTyiktX2r_e6YXd3uraB2tVIqFjnn_wb9zxMJs9Fd3vPDmArdMwIksTsYeKD_h2RssTC8KngsoIR9KmyNIfiO00blpMR4tpSvIgiUSS1SnD9TByiOWC6amZWz8X56INa_S54uEwKSywwxkzMc2K8Ppzq8JM5Apj9x4QC29lhATffFQj-uOICFsOxBq5Qi5T0ZrrlOoUy0czBpF2gndjMDbvJw-mArufTfCdNZvHU44JK9GjkQZPEyJbsHBdbMBvmbPu0HFzvLm4xRy4MgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 567 · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 754 · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 752 · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCdyUQ1YBOFLA4N6dfEO7SW_fZuWFcConm1oTJ46BUMO__yHA_Sf1oqLUDQtcW8EiAWnwIGdcZqy70R4-GbWMQLCbi8Yp03Ykwu0hMCqRLr1HfpbsVWdOwrpb4aqF488FpAnDnzJx9FHxgbVjlF8p4h9t9aBKVYW1kBowW0HCwFp1RVHhiCPKb2-mMC9uNHhy7EHEU9M3Wnboijaua3_bBj-ZMMzbmDerxt0fMOP3LZLcyR6mqsohIBexhtODx7X_lKbicoAnUvOaHzcAsa-4hj1S9Y-emSkcuc9yCgSnVMs9F10t-F1cGldykqfvZ5rMt2OACsWE0_weIzSc1OzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj-veqmFkxbU7tgEThin7mBozcSogSB3LQXkTJ5icqIiQaMQINDwSOdm-tyEkAmGSPBct-bgcDS_41aWy4Z1gFyjMAe9w3JtIZfEpiaOafYeA79Goibog1MYKJUOoZrVLGgo2ivjzoFaFN08q8-l0c508p4HRfqovj9KX1BlG8HfzJo2t84zQt01qatm6H203C-5RXPcmKLHYNT5Ileo6bKnqbrNqwPw8OSuzxOURv3FPYKMu6dQ-M3D7tsv8i__t9roAhIEVQ-zNdQgnxA-xEWiMpX2f-o6IgKXPIWb-g0hPsE1xUjHXIdfC3S39KgVZu_HsDy69Oq-vURNY4uHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvMwPm-QRXgeiA44VhXcmxu4vQJCatpqA4HTVNlW72uFHDbp6J6DWT2VmeEIJ1PT7-2pmf4VWnQUfqKRMgKYDzrmZjaQ04FIvNy7Af7D-eS3spur06vgKp_hKzGfj8JV5W-HlBH6dX6YMnkHoBDLeToYZPKHToxXKWLCc6Uk94PrsEyT8pofYQisQOhAyUQ_cJlC65QLxAQV7jepUkK_YaAX6MO14dIA5id534sBJ7fI8Gfn7SMQl6YzNWHVmXgxccLuRy-ACKR6qiheYhgI7Cny2h0A0_0LxTqXg3gxEW1992qQp2OUASVReB1HnaGQdlR6zbykGqPAWG9XnCbOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFSjT3XneP1bPb5dmETDnWqc63IixHhFLC9juaNCU-LmovqXwr5DtuZqav6dW0v0jIYDNcCKRwehe2n2Wp6_-h4qS5ttYquc9_JGI1h1VmMtdDbFH84vvqPsfgvpw1xrai0WVwH_h843-cemfbyEZDrIOgIajPikDBul_YYel7pS5DRqWiTZyxDXgyTSHmKq723LixhHbpzPKeD2IqtqOfbVGads1kqXsEE7BLcFW0VcVhstdSRqReOVZ3FTFRRIN9KkNZddqWjS2PjXgGdmMsG6TRDfbJtKnEt_KHN8eZI-UFs5T8zj21tG8VlhXxAFPq5_1j4eTJUdcAwadyL-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr0PnkYnw6ozYfDw-hax7ZMyYTpCWAmjudQoCTZZ234poz_rZfIU0cetvhm0ayxbtRWAcqYlokn9id-5jBRkYz4Kvbs5duEWSAw2l2gxlacP0Zk2VA2RU6x85-ZxoveAl3QNsZDLR_YKTFaRKvMqkM51i65opFxOMbe9GN2qF2qpPhJntB-RALhybappT94P4EjcIForNvaX8L_2k_hkbmdYozgZZeRceruC3-ONhTvfiwTQRAjzApE7Ycz6DFllZL82Dbs_L49JLPcRbtSzXPVJo9DHmZVQlk8H-zrpHqp1EjT6t0MPvBQk6ORb6LZ_aZZjbyCsPyYEsANxrmtFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUYJYCeg01_GrUdQ2c5nCK9HvC-pDiORrpwvhatRkzu4zwz3u6JZxXkQtHYwKOSlKcKPKXuXDWbZVBa8TLdu7AYOj_L0rxCapOY7aOHQjcVw8HlI1ro44Os2fVJ86ony9-6KFeUn_QNOXxI_a2SFjxZeS2MEvcFdbpj26M9UYz2yxREerAR-82HLhVN5QcGt1vPDe95HWS5Xe0v8SYk_kHH1oufabHXP0wqR60v3yjC124X8SIZkVlxsQlvtii3APihfJWP2mKPVu1Q6IyGa9y_O1NdCRWph4oUOfnrBqzqtj8Yzwo1j-84xt196Wr85QLzP4wWQ6_mg93UwwoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKlcARNib46iBTfCqticAV5QV_CBxZjumzVuQ2t1KjZAn8bgcAx98Tf_oFBU7-88rVoabYBeKqShj-mjlSnwdFajGq6ud0G5MXOa-ds9X6LibCrTYJyvI9rToIoWbi0Wt4Y6fugB2ckk1m6pFCYP7JQUCDHmZE80iXRditjW6s0n3-wvCqG3U5wzy_z_kl4vgNZJLquOoHOEXs2y33hGz-VILTuSP104a9ZfUNuSRz3xo8HjZEAgYlhvYE0rtu9cSVejESjGi9-ayRVP6pwGscLqPj3Tj9BIVemrxUYbOvgdhZWaDapA0yGxfS99NEuzQShu6437n0c6iwdpq8rzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvP8q5LYLh3yqr6UqXHauWPrQ5dWvoX2yL7VGc17TecPjC3yQBq5ue6uDAGbZgG8N2phG2OnKJb3RfHevkNlWokeELtoozFo_1dLe9NTts5RpwUEwDF8y326-j9okYI8Q1B-4Qnmyp7kF77tP2HK8EjmIy5gw2vsK_KwYmWQtgDCbAQ4JBR2whyAd3PZHxsWse3rPUsEVsDSwyFINu463uPdPT3zNRVDDD1OoWfxFwMblOLbAlX0dhh7T6GLSE2dyahk3jBdUlI0m5OfftpJub-Bly2MNNHOoV3NlwM1S_RHA1JDlpMlovEorLXh4epxHzRYIv4nWhV5-_hKcGvXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv4MxdOj2Zj2CCoIwW0UayljEpy1l_FIzkgvF1m8NMP9o2vWdoUfNMzqy3LW1LmK4CuvVBRh7vhJIQLM2tCfrXi4adUSEp_Mxcu6XmHkB5iojTn84tL--oxZHvrKUQ_8bo6ktiSAFYCDQsioPVGkqzUG-BfTqCaBmyUB0XFsW9xPSQw7oxLx3OJ3jHUzoWtovT8WC1BFlvfAItZOBblW20gGuY2j6nc0M8hU3BCtKTLrmEFSppntYUAYwrSpnkHTum8v7Jg3ufn1UZdn8GJi5UGhmHJkh5t9jcEFw53wa20JBs_G-bJYs2yylSW6RmZjXlNuZR55pCMJuO0g_DZPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsU2G71yzcVDl3VKjFrlwBrKCqTvviDLmERN4A7oFFmQbkxxiS207POFwqUK50OPtv7TnZth6vgB4RYpTVNcC5Mk9DaQPNh_Iuf0Mxuk0o5ldiRivGSOSphldVvvuUbTJ1hlRA8P3wY233CH4CgaZIRSsysSHgRAktr1dDXqMHIrL4cp5mz1FT1OGMxCaRrmDBYiyoLl4w2-sQRJ-pjgHLfdBLeYVd8PZisuTFjPef0vS634eryFjqZOpp1TeDtVZ9L0Ru9hW1vp5tmYVxPq2fGNXDT-mqo3Ti6kWxc7STahPD-7RFqQGuBTf96dU4siWJBG7hsHGuNyWUPPxUWe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1r1QXNWfwJBDQygPHRkaQKBpoXgbgRt_yLlQ1TOvNzj7Jcw8AND7Ni_-ZUCA3UDUkQC6a6XNEyi4qcQMx5R5XpjY0F0dyipOABfp4WHoaKe47weQdGY6JzbIR9XrGZWP_FBCHyna7m6s_Z_cuM5T_qjR4y2h271sRO_nWOhSjKysxFWNTyT2JGAPRcUfgDWYA0mRnHwmaR3e361yufRPDKJJ7t7zMRpmM7s_UxfjCrm-wp1-ZIZMKnsaeCcTqJN-midhCm6gn3N8G4VKa61WK8ssd-wSKsLG37YADfBuPiJF0T2Nl1iY6MF5zt152lmjFELValnhvBG-UVw6QvV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXAWllHg8Aw9QizZY_SYEWfX-YNr9WwFbgri1TyMIVoO6_dcUdjeobofzeFMSc3LNnF8WcMQjp-on01r3aVZNbr1uJN8KwS96d9SjC_Wrgeoe8DGqlxfwTXJIqyF799aPzjTuCLu2xOBHvF9f_ieBONlAsicjujmJRn9JQXwV_KmpieeLTkXvyi_iFHAVx-ran_0BogfCNgxOZ_dwwmZLBWATejxjJxKCRJ3stkeoQVXd1UaTJH1-GyS8vJnZNpu8OrScWqe76LAwmzNSIMq2O5Vze0EFDcAJLRv5bob3VxImL_tsZUSnQtiyWa1n4eZczw_clyzFOfTlZEgwlBirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcybI1UjZOxT9fi4hAMImFbnd94GKUW4kl-kjsXTHhv5xFV7D0VlxqtRbTF2Le3mBOK_-seNLfGh8AOCAqFtx3XRqwxVhIVtdtjQozYPw5ugVx8eMa0vjq3YAx2KuM9mMVl6_gmHAzBCHn-IeIXHO_4NoBaj3moVF1DE0ugPdRRoNLzPBUTcUOR0XafxCKuLsYmKeam4ki1IThfKiWc_R9cZQdxkpvMuSsyzZOO8YXfgppx0bnNJri-TEwB-9M68AKpF3fAgDSyfTAo1vOI99C0aHs5Mlpfik98RNzy2iDM29edwpLArVXnBPw7pBOUmAyi69vsSlfb0NGmjstk-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1yPR7gfoV02Gl3ElwrbngB5RXXOgh3LXSiM0BYxisHs-0HrouBZhNLIOMCbPQmxrluOR5SYxj2DxvE2lXSpKLKTsR11y6qXnG_iA5_QdKKDLMeDaGbJ28MHI6ZFValSR-A_JCMt-qRmHA4QLP0Z1yBJwwTTVdqNlt2RL6EyehtgFt690U40Pb_gnkRqfey4O7A3nXhnrXHDmM2uZdyp9NsPR3KWJdmbUkgGybJFO0HdAfc58JbeM3MFnbCQUhWRyTUuyWOKmi1w6IIcjW_u8E_SWjA6rvMxaCijjsbAEfC9KRroZixkEmt1abHEbgMt-cEufqBib4DLe6eySD8bFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEBARRPXiLxma2PxxqVrDuELDXK8SbynWdzMDHEyimFT5YYJHtZvXRi2cwaBxIu-XcvwJmke2wUwFBpa85vZGV_1cyoArBehC27m80zfqSp58pzCd-q-4yaoVqvqKQYItZqNrZ6ieHCuxuJK7TwJsrkvwaUB59euyMRDouOkiUDeC6aDR4ixeRtyfzL24MCc9XB6GIjiSw3OXXF_4StbK5tDbiXprINWRFSZFxIeHAUDofkTfmtMrfwfueiHd67sBVqUge-9ZTOfRbHFHvdI1EryN_-Pcdbfyo0OpkZh4ZivvMK2qrbY8s0kA-0jW5BPbxvOaiUYyFUsiF857gDoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-uNRCHZF0zujDdtDbvLsvr8nuGNXuetVI4FWnnL9XQcZFvnXw9R2mE8rIvuxyLy2vMXWjHebOdHc6fEoUKgIgB5DdSq8C20rCng0GvDg9UOXLqKUZv8M2rAWZygO6sgXeCKFycR9r3UWLG8An7aY6k33qxfm_yst57SUs80XcyySff_ic_RRfCHBq5KCxnJ-JIZa_eSQ7gsYqI58Mva8gwxyUf8AWQhforQq2eZxxqTgH5lprqU6nHKh4yiapQgb7loCR1V2IvGELdWeVvMmISi0OzzW26FbDedy4U8D1bDdWW0vHviJY9drVupJMHz_JwygFAGMsa8omFGA7VRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7O4-ojRDVVaxEE0z09-7ilcu_OQPlkINjVL824Xn5xCce7EkNAJqcjxZBkB_TMPAHaS8nyAYABketbiAGqV8lszeDeTnd_IulZboKZ9k5AyYJ-OhYr0n8OtUaSpvoN54LWk9qeHU9fqBugUzsfj9cu5HRUCmTAaZVyWMqRRXHhXYY3bXzlNfm3aFzRXLgTlJVkDY62W4C8Ts01isNC653AKNl3vSzZVgBzWMuITJCvtZ-8mWHXlLsUZwoXDjuvgZORQdAjtaUK9zzqevHNTNn8ASKAeGDUwR0xxursByLDXqcjOjF_oMkv5iKpPkh3t1Ncc8hFgHVjIwQLFLxX32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdNEhyJlRD9HMrguB0CBeN9qI63t6zMBdWM-m61JLCe1cECe1-4mIuUalwgVor9NY-40ntmYUjaD88Pijzm-VyKdRDINjMSLd11LGZZs6bhINfjlQO1QxrKso2aoIrGnqKFXssUmkMOGMsL2p_X7uXDhmypvZQVSdFP9qvAILgSw2FiqJ0qc6KlGl-GlnB2o5KnF4sez9r9q27U0tLX0Tl555J53CA2IUW0tiCvq2nY_d-U06eYwXgHnA-9zwmmm7Hl5gAsfxswAIRdjBcOvV9y6RUBdEa7fLUN6_1BpmokyVNdw6GQfsW5KsK8TK4NGBjFpA4jj8yJMWy4tgm2Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giVteRlGCScEh4cHVl8QPveqvcTw9OO7e0Bku75HsZdlQA3tS7h2W_FppQGZerib6R1YIkaaARe_x2_42cDzp3_M6FTN5Vnju6EJb9lsK75cW_T2zISUj2laU9o4I6SfiWBliJwt_amLqSZcEkRkgOkDmOOBgC_4d01yhNQdZizD8YRyoVSlFVikx6NYmmSf8a2tZPnyneaA5ao9joTHCFKHO42jBAUXuzo7c2_wx2dqJXW-XrRWRdSf_j0ZyyXc2d2zFlSfxr7l9Rqedv81R1xKPBfiNNwv8JYwJFuCoCOn6XGXe-91qcLfkj4Am-eQXybnAlKu7JSu5EoT4wjESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=OwgKfDjpHuSzeVS8fftnzaQ4mQT1oAlG6lNlFPdsTz6JrlCbs8RwIgiWE7vxWol5aJrN9tJknVJvnh-AniPyuiIS50nztokVZb6YaHmDh3DXW7-0_pFdyRMLyEHlJLG7x5oSoF6N1QHPNEId5HOJULSCsKYF_sFFteW5UKk-FFgGoYmUSojC6DIZ1wmTfkR4Nr_tvmvZiaSxr3HfdIThM6eV5LHu_cBVdn2ULqFj3rG5GfVcK3jeW2KWgRYzJxFN6qzJ6tQ3ptWyaOjzVpW0gqO9PNzM8zYYyTInUjHk01uFBpnWoq2fxeLnOhp6Z8KRUVds4mdKvR1LflHXya_cKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=OwgKfDjpHuSzeVS8fftnzaQ4mQT1oAlG6lNlFPdsTz6JrlCbs8RwIgiWE7vxWol5aJrN9tJknVJvnh-AniPyuiIS50nztokVZb6YaHmDh3DXW7-0_pFdyRMLyEHlJLG7x5oSoF6N1QHPNEId5HOJULSCsKYF_sFFteW5UKk-FFgGoYmUSojC6DIZ1wmTfkR4Nr_tvmvZiaSxr3HfdIThM6eV5LHu_cBVdn2ULqFj3rG5GfVcK3jeW2KWgRYzJxFN6qzJ6tQ3ptWyaOjzVpW0gqO9PNzM8zYYyTInUjHk01uFBpnWoq2fxeLnOhp6Z8KRUVds4mdKvR1LflHXya_cKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCQvA0aKMO6DiiiZiRE1KLLzzm73yI0BlednLsnKWn8xp_n8w-NI9RvnkKYPpnzqPaHcOx47h1v-TyqdU0W5Wuq6vC7EVCISDIa5wUyoifmXJEeixBtPoEakHJeNtGL4bpBIFN37x9XgO5mfOx0ghXQWjxKmPpBcNqBIHumw_Isg6K1s45vuLIyAI5Eqh_G5oPmykBiioF6w5lLrtIXWo__L5M9FuqYoChk2DZcWpnx_BIuS2kYUf8ouF0wbStviOH0gDCjuSnw47r9uUW9rMrYXnhRK1qVZ6IZWg-t7CBuq5EkbDKsaTurvkwAh0a2aCfsqPBGnfC0VfHtVM6pagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMgcYOZoFCQIqDN5GYpImdf-v3HGYPWKyO1BAVo3Oh-DMO-7zHP1EHk7AICRXuwGvXPtxAw12CFNVDb8wUUFPC4N6YHv6tou5qIgHeBZtHqB7eqXEGSIgfKWdmvNRJb88Ljc-2zZK00NjPOu0GicDf9hd6RxMyTo7M_SBmwkHpi0-kn5TZeVJRpl6Q6eqMUzrXrD6GWOZqcZ7dI3629fSWOqTYuRT3ZJ4a7fxMTGnGFSa7R9Bp9T0mbVzMea3dCwHyA4Ty8EwUfuYXk_OB50WzTJlwzJaPj6O0jKLQ38isksnLoDGqF2ncr0DgZymJwMb5xr0AmbQdLmp9jdKgmOuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuIEue7_O9HgnmgBoSx2G0VnAxesZx8-lSUU_1lTL0aIABkgGt-VbzUShFFuYJDWY9qLRKURzGxVnaQ7Bx20KpybbzJ98gdkvPjoPplTWiU5e1f1fz3FICx3_kfrt6rr51nbzYoj7tCsNm58ChbSndMFiNmRa2aj4NxEIR4x6Awnq7TvH0Sml-Tmcb3_waPoWmgu2muLXYOPHcSleh_cHk6Z6I89qCi6-DpI4e40GOrkhUZPT81MaAantPle19uHXpSVvM3lqzw48zcqULzDhJ-31VCLff7gMpZnby_MAdRyhalsEYnZdg5GFNqqLpDW6KJrH8_PGa6qWGHYTD0h8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpW7T6ke5f6_V0SSOIwPWVLjSwT6TlVzDuK4zYWng5IFTby3r4ja4MP7vXwm92sTGQEkQeKml8LmJU7Aa0K6Abq1NmSxdKxPWHsfgdDNkkpEi0b7uPtx7WbVsmh7Lj0BOuyqgoHmVyzwrKG5XaGLSwL5fS6BFPYbMK39UlGPO9KqdhVR-rwggu_BTp38Fzq_fLJpqKwalCSKfqkZsEHJHON8fplzrakpjVWbzwooZH_ByHPi_9NfCpl5Ww4Z-CtpZxJ8YSmWZBd9RF0bokXWZ_8t2bVx6qq52kF_K1odIsdfta7_Hzn-qRr0B8nTC-05C-tZiWexwGIMVZ2aDwsP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUjbgHQZRAcr3IL6txoZZqrwltiHYo26hGrxQEZiBHKaKFrg9m5-B8B7NVeVSE2R5IXAzWBk6ELzGtxmNdTOF2oMyDrK-oo_Ohpo2by9eyupIoCZ2gjXukPMjVoRZuPLB3gKvA5glCL3WuNBWk2vayKfn7xz2r64192X6cOU3cLmK6gG1SxVyiOEj10YJM55YsyGACKzGDbAy34N93uVQGpS1CGp8ygSWNewsR5Dc7kF1zJcYTFazF0d5emfIsEP4xMrbXnZaqwcKA9p4vMS4zPwX1Tfp0PmZm7qXS11x79Vz2v-0HeMt7sSlLQk7TEH_o02b46SZHYbKxXLkETLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcAJeyttot8cqzQKoWD6DTW-8boptD8YYhmGBe99T0IJuBfz25eUNqQYrU-DMa9QI0k1TnIdmhItNPb30JbJKabJLRNs-hbayOQC6z6HpUm3a_CpwYFJFukiO5MyXXpUjrxmdCeevP3N84I1ul12Y9Lh4ISvGXwZHP1vyALVyW-cdM_C6tsZTozQUWifsDxjj0x0EyZl-oWTNjtgQb7L2MoUPRxCrDhXKTN4ZF_smUg4fCLZ6paa7obQ8oFYtrRtlpIDTCGB3hlZBPlv-2P27j397na6l15J7IN5MCgui9pHCEksgECB7A0NZJ5fQ5DPAM7jAglN_4KifjSxPIrPUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COdqtLisCqDCcKR-zabEAXaQfAE2cZ2On0Ji0wulBQEgOpLsfyFfxRwIdb81Cgf7dVYWKoezjQLoDpAyQHWRwMrRQ9FihwYVVnJTGaINMnCeWSGBNck5tgT-IF4vmShKcs62ySIxeyL4QMwQ1EbeuboT9xq0I6TS7txeNplpELrQlOo4-cXsz0RVpoxcU-9KkDtS_0k7N5Bgm_KzCfvJvgsBHz_wePVNq9AlioR1yu9WbYGHf6TEHZZ9cvGViLZ_G5RV50FNyj8ybqbwNcRroc6kyyPXTTyAZrJHvSzQT6KOzgLP1E8o_mIyCCVOwmOx0fMYoBEGG7s1IP-uPGbvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbMXxkCXrMMIL6kUOqdLCtnRkj0Lkhi9bFlU2iELHAxqimtEGyX9cm8hVQkKoBODwGy6TTAej90-pjlLQgUbBSXCe0i5Y9H15NjQyesbGC3-a0cQcFaci53kj9BhVFfjJ2FKTTcFbgVaGD5ZLPPa_vfvZitWUQfkITlqF5Bxt99QXsTLfRyQKAwcKQ93Al-vEhbz1ds6S9iSjz1et8wFqnXFxSjazZy0n5lg2YzvaipluaDDPX2rQs3kPqFA6hG4_9ck1yWYDrbiDbkXe_xrNCzF8NmR4VUh9xnOrk8DJkETW9ra78AbeCYievDUuLYpS6_4jUpWyQo5HfHG18o0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttzGsgruI06D-kz11lDxzYO4TD7lKv-MRdsax7D3mHnD4v3c2C1D7uVeT79mCphG3iPQ5md-RqfiM70ZnwoykfJkPRttB9RMNFzyF-f8z6pFwRouYM-V6YYB86LRxTCBHxX7B2vulJtX0uH6IELER8bQHLHKiQ3nRBvSUlY8xricYFWY3-4HSqpMs8JbqcSMnEwjlLRs0Djid7opvC3y5RvlqPh6mG03WjwN82h7Ye_lrQU7FGJBVcnNvIRqmVqx4ybwzJoKaqhNnMr62jyCCx_AyPimHcASExL-E6Mnh2b9Lv4-qVtd3_GozJgEA7ZBbvszLGZ92v6kpz0yRfF2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYA7Y7L-00WQmPlpEzx_lbSkRYNr0-G_nv9svoTeqObSjIFd5LgfQ1dRvjtmB1GkCVzwj-nvIO4aG1n6kx7MpzT2cfl7KFVgD7wgbC5fnBg1fB2oW2R4OeHaMdch8FPFfd3JiLaw_wvioWsBIKliQoObEInmvXQ41VF5MmlLTBkG2TMdw67rbtGDmThQmVxYpCdIXKhLvJQxnAGTeJUbba45WnfJQbSoxEI-M_Z3_8QSL9Y8OuGJ4TwhkU6vVLhwoIUF4YTNayqzbwqQjF_t8TDJOyLwnAqflO5vRxoC_FS9yE-zC0jU7kmKcafPDM5QWr1hTBMbvAnCAR4Xb9ZK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un6IzSnD47UQ-_6pdRkRLBOi2zyvEQGiJFkRbwHL8t10In86w7-pOMm9AmjmdqcLFE612ls-CXXMO_eg9P2Cdouv4Xs1q9sZA4_O-gmpExkcQSGPER9vUSQCD2oIgY9HfoqLI9wze6fZJg87V5Wj247F9wy50Kkm006lyDgiiC9qvFPyFNJseIHy8jwyLSaukxEv9fCIfFsyWU6YxexgM9e9lGBZ0JMGe-L7QldF--iPfWx8wYzOV1jAXJGXUJAw5njUpfY21PNj1LlLXijMk3t3TcMvAxgf6qTqNLfSgeWhVd_2AMA3QSShZ6eV5pdwbkIOA3APIiTF9gsV5eAkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjXPNgeON7uzE93SSydL9Diwj-1YaW2Ab--xSt9U3s3oQC19Zsl4YXLK0wZOjW1b6O64T6ziPn3WyH_80iH2HI8L3PQrfW7V-87TW0y3888XkhcEi_InFDL6ToQGhw982hfPO1synAWUAneD9xsO0cLN82vDoN_WWyfpIJ6CPyhOryW3L-YaZ4JkCQxDnjIffz4mHQo087aEf3qziUbYhFEgvNmtNjhhWDTBOC8-reiifHwBEC3UpXS2VYSkUSIhs9WTcNpk6z_T4VsO5KOOmQBkVrNWGmWky7mNxjqm_U3L2Co_FgtfEst7NdlbRn5snl-GVj_KGvGefrgtvUj7vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC9Djo3NuM_4N1dDR6cvNZAfu_imaLbr6zmsLW84OrPPd3mOH_ihT7TkhQZIgSZe_XNtWYsVBbadoWR65dMHNihRw-hI3bsY0sxIak5hPNQ8_maMEc518-SDaCfbzF98QBYmuat4oc86_IqsgwKc8x7lxT5qjlfMZT5mJZ-nVRdXkJD3sudInVVQBIvhpaXNcHJQqKYulRb4WrBVD4X0lvZ0tTsYKRE5mrV4B78sn60DtW9i1yL0VsVfPfl1oyB4bD3y1Cr1UDcjLsJ78zWSh85sqdfkJfYfYIuITOpfK4woSVKCJ5VGFzX-F6IBrb918vs485grSw3-V0x7m5Sq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13MF7lV6IoxLgxQG_0lqO-hSR_TUwna8uXOTqpxeedxTDxiNPHlzj3J9jiYiaGXaN_y43j4uy8hNKtn62mB10aukwY78l8sh9AIq5aJ0K6r_S1glDuDELHjBcbVCJ7-Ab4vesMi-fzXIud6swfMJaZt2RFXWmfMxj5VWNQx2sbJVQxiVU9c-SsIi1Y_BwZDczuA-bDJhAxLsMFJ2wHRrXg6lD2G-WdSv3DLnOEyO7nHStgjd22fbMdvu4atQ8t85PKN-QwLyJdfWo7DR5ad7ncekLRpYnENMxQDzkQWCVc0hsZTASmY8K2_kl47Ta4OXsQGvln7j_fDIOQqGPwX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiAc1vSVE849jy6-FKM-RGqw9X2kS_inJZm8yEVUelGJtGdLBLrYKFU6sLAbUI4bTTU2cU7XrSk7QqTCNggS8PCBTEnZy5VIsulKwHDSp3sKQ9TegY1lkPscMlEQQc_d9CzrODqLzRLLF-bFkwPlslpER2Dgy1Ocz7BHZoV8VzfZrbdxTarUZi1BXetE_LJhzOASxMhtFQ_bq1W-4YEuK6FvOrxjARe3eyqhT94nWx7KxbxLijK7fiqyEQi2AsRzjR47lm6kcLG4qTt-Mvo3PXuY5AEc-hrPDF_cCa11b8VER_etft4wkOwto-FspYULV4uG1_lwggS_iT5sgSuOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFsqKIIcIrvzG-Wu00Mpz0uuK16snfXhmcrXiv0Ex5Mk7gRCG4D6i77Texj9U8h4rXccbq769vrieASogZEWE-GYwyWpAi7tfQ5PK6FV_RaBbphE4c8YvaCra0-GZ47tVu-J_kIPkSQkYvoI8y0l4DSsRnT2b98mJ5Mv3-QxigxjBtXUkyBDFTMtObDhrkn6Ez-RF7FeyUgSi8UCB3SfgEfojS4PsI9kfzgpFRGaBtvM_fTKDXFywPQ22c-dEWcLrDN_fu_oOFf_GmKDoATo9EFixH4of4eoL1kV1vfd9e3aZpriBMazp4lppSDZbE2X3FXhf-h-nzOQgy2QPCpAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOEiU0coRBywWPmuDtCH1ieekQbOsShL6L9Q1gPXWI0I0ZuQ3zXmAUrHo6O942gOQvjIRvNaXNGH_lXbUdpSsgDVw4I5mOnfBdALociZornZ7VafisK2IO6C15MD4x7NIKoAmlg_VffIa7TQxa2BKmzhaQ8q26Seu2fk3C8Dg36xldkiCzXyeUl51hj7Hqgz3T6grSM1XA9cA61Svt6y97usMG04dyk10CONbwp5yZHyLkaANvQe6dLwNxdt86hD_aHEcBAoW4wJjcf5ZjF7OvFVd8l1rawBjX6acfn9gUffGJ4Z0TIcX9XkH-_PZ2KrP1GEY1EkhFgLRl7qtm2NZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOqp6HhdHfSCLgeNdBQ7eUzgN8M5OLlqFJ1lBpf97PEbjQAxu3t5CFGnMFujpnmKwybQBCbnPfG47O5p7rtTJ6qhe_2grIXUE_Bchb5ZbU0LvVcGtD48ivPicqBulu2JhA1O_uiUuJtHyB0RfwQgNZsqUgyMOgNYybwc2jn8lHowJJLIxMhInKzW9ndBEH4yXfiqdpuobm1rSuZaGM0pM3VPFUgoyV0ZN-O3uFdSEJ7yB0CBPpiNGMAPQI1LtHoxBEg5eDfGFn8BmnDMz0rT6uBX3qSWuUmuYS5rSKE8XXBrLvwmsYa2imDGlvxr-VU86cseFs-6ncmLO1eR8vS4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBviHWe-ai63M5VM5bwUeUbJD0IYLbKjc8vSUtSzdxggJfoueMYrqhKsY23OYPDSDoKpRbjKpwR3_ruaOsw7P-FT3Z_Z8VIJZbydbiYB90oW5S9IdP8bOIlM5PvPFXc075YmaBMQ8OdPt1aUdtbBqEjPlKtTypaO1PE8bAWzgLAKpdxkkq10ptHlxOEmh87VKjNP2EN1b-81AKSLRS_Uuy3aJfifdoW6BOKMB-eb3OqieS-kcIS-eBzQhMtUzqlZ1fl_Ch3Hz8_yhm0j5mw4QLdAARtahXlZZavx9Acn6Y_5C1pT1ine1aFPUeg55SBAsqIts-loVmIZzclIBr8llQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=v-vgpPZnJ1SQ38yGy1-UtVaDHO1tUb2ng7KU5qhArJO2-59Tz_KuivuV2bNC84fQSnCl4NBOC7pKfKxYKWnavfW22feK1SjaJnQNkASOI4gcmkPWN3LLJyNU3lqTMthyjWKdfXB00xg18yWwMxRNwrQ1gUEURsi9ywCwyvPqkXG1F1CoYHQ8rwG0q8YULn5EyawycERltEBMnhmaQGkAbCAVN9-jbhOheHTYEBFOhRRu-jcn8S_N8g00NZC31lxpg2a5ixTTzpf2XfYkRtzh01S5qPZTx5-37LpXQ_iWMj26gkK-VOJGo3myEryDgzRE1HCaWoDpYUYJBkkXFbq0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=v-vgpPZnJ1SQ38yGy1-UtVaDHO1tUb2ng7KU5qhArJO2-59Tz_KuivuV2bNC84fQSnCl4NBOC7pKfKxYKWnavfW22feK1SjaJnQNkASOI4gcmkPWN3LLJyNU3lqTMthyjWKdfXB00xg18yWwMxRNwrQ1gUEURsi9ywCwyvPqkXG1F1CoYHQ8rwG0q8YULn5EyawycERltEBMnhmaQGkAbCAVN9-jbhOheHTYEBFOhRRu-jcn8S_N8g00NZC31lxpg2a5ixTTzpf2XfYkRtzh01S5qPZTx5-37LpXQ_iWMj26gkK-VOJGo3myEryDgzRE1HCaWoDpYUYJBkkXFbq0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYnzDzfmna7izp-7YrC0dz5buvUtJtop--vmQ9I8sKO_h8URlpFhULLj7UrU-TZyDhqmIAGSN_A0krmzghWXEam0z0PfLGgPoRf4_wXvXCrnAYpPuMto01mzwZMpNBIIsjXMF6hPU1MsoXcltgBomDSeCPmcl_Tu7i2Tcyy-CCYTZI0rctvgZeHSt5LT6Y9VRlrFEUuHs2zj3XiX-zLkPtVVwdxjqyfl88QlzhE6hqk96-2p4QqvybrXMn_eLKVykVaZSxb9Q1R3b-sDeP5CsUy63wqS7E-VH97jVrq4Npz5oM30WMAZMrSCN89lSmg0XEDmlA3SYFCvxpFZX7Z5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFWjCEFQn_gkmfmTs0qQrPM32GDscenJth_Ro0Ndu3SKBgx7-WH3cTNAf2_PGV65qmq0jY92EljnP1Q6jxAxJurPKUdjBXFTvFiYYPSUKGRxbuX5xtYc1LeYLrUOIXfaVjM_a_sI7uzetc6AjlbGWqi3SzJ_MlivAgbsOBtlVhRZupYSzwCCwhYW5yfzhkeIpFYjEtgdA8tmPPAXfyWD1dC9Kgrl3kvQQpyt8COhp1uMi0LmbYtoif6n3AxnPmFTlaWMJzhStGpTEoJJp7DcPthHkf61HQOpoPjThmU6loYFYCEhetaUQg4ehJVZ_yfp8wO-ivN71xWwE_XLvVu17Cbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFWjCEFQn_gkmfmTs0qQrPM32GDscenJth_Ro0Ndu3SKBgx7-WH3cTNAf2_PGV65qmq0jY92EljnP1Q6jxAxJurPKUdjBXFTvFiYYPSUKGRxbuX5xtYc1LeYLrUOIXfaVjM_a_sI7uzetc6AjlbGWqi3SzJ_MlivAgbsOBtlVhRZupYSzwCCwhYW5yfzhkeIpFYjEtgdA8tmPPAXfyWD1dC9Kgrl3kvQQpyt8COhp1uMi0LmbYtoif6n3AxnPmFTlaWMJzhStGpTEoJJp7DcPthHkf61HQOpoPjThmU6loYFYCEhetaUQg4ehJVZ_yfp8wO-ivN71xWwE_XLvVu17Cbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R41sV0qUASjiKzyqtSAZ16ErRG--RUDr8AnLpfRXceMhLD81GFZVnKy3aSDWqnohAw-9CLj4nEGInElbXbqBGpemxE37FjTssCKuhOOPHQWG__Gam_U2myCnLx2WUMFUnj2nELsqfmwKuGbGUbD10jHcYTpxGSDTQaKppOAXyY9lzoBdB90IYrXkP-xLxDYwvNl9xmLVSQTCuMgA3XtwB-0Owx9u1pFSXZyd1MkhMqBNdHj1hOzzhpEcgGfevgDAINx3wwbpJz1NNhhLeeYKs9pqK5m2v6LHUfFsDRDxbbh4F-GRgC-FuboOlkKFjCyJPWE_dOrWjFnToGGndr8lhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBfwyJ5TkXqLVEbw2Eh-zphrNLmofudRHulteh_ykYOlix2RmSwa-ugMKTULml7A7hf1spXPeaSkoo2eT1gRzeBMu_Uj80sExzPfk_8B1Ms0UlPvvU3-BzemtY0pEIlRLXWZqQ85-NFsoMc2HXU5sVZi3ZoA0tSm0RqvOZ1nO2RQgUhuLbf8dF1hr7l-z8QIbSryBWUMk5aCJUjy8_FlpM6dSyEXZ5mGjPCv_HsHWZg2ztuabN6VhySGwd9js_znLCiSsXnUlI7O4_5STTt9BD79YLFEw8wYuEqiCcZLZLrzBu6_wdDdnYxqnQFk4OmvyVXbSR6atX7k8-39bY_WsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqhrbIcqQ1RUbXEj8pToj63qacb_eSMAkaVpia0rQb6c-fyS9dGmNx3Wa4mCZ-LpQTA_CTcrFUn6kim-_IEWA1PL8AhUmk9TaCV28Lz1mvzvCDcZxBQQAmLcbp0DDaF59fbWe4P3yfcdvwmVTsN5PEbs-VE6T0belw81YzYCncpEMyXQoS5n7UeAG0ccmkdUKRn1W0KL6_R3jhpmWzee_vZ7K9zzwUKb9_zE7y94rPdKQf4CWPwQMk_kXxMBCcQMaRgr-qO3ut1UG1ZAvXj5o9AQw_E1-dAadlDjCXb75Lywsq15F-P4Wq2VyMLbWKuOkZEBJ6mQA9WL0KqZziHCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqewzCn6Vevmqhq8kPLn7d0EubSbKWvkWdWURMphenjfIQJcmTENByx2g1M75Z-x7yJCsKJOS7uF7OxyrRp7EIwWTXEpPYaQdeJ4K3Z42ilt7Zm0mCmGhSWkJ99ryyFGJLd53UbHCdtMD6APSDDlcl9jrKLoPfrZuuXZrmMK50-4qWYCjDEx3hSWh734vFGqd8V64ndnNZgXEuHqzt1LETblCx7OTLQH2Df-fZBitQufsonxXPLj8qFWbdxMX7v29GQ42BEXCu-oUMXzCkUtV1qbL1gtqU_EzsnPYUEUJH8uOcxThAaDc5GLxvVqQkbPYxsmyBizz8tW-GrTqO4T9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeRSDsGU_R0upP66vKShwn-IE9KwdHTuzUeIibRlIVmK3yzv92yHIVKOC-JMqx5uEFFYdD8Fb0ztrPj0hsyLVmEp05cf-VQOzkuYiLlkbyTfrPzugyCgxe_FsLC0MM_PaI2I7xjMtP3HcmNBK7sg5Lmvgd_J6LhZPJnjbWUl9yz9_rrAQ__-XU99ZWvwECTVf68ZvE05tflYGSlibyLDcl_2ZK2m3_nOQFl7XUIlq-G2Ec3wr_XeDZuSH29RY1juA7u1hJBl06xmdshMSehaY3amcQ3Q4FIvTf0EPtuUzXQh4MXPO7KmT4qSTBy3gJm0nX9gnaDy9KmjgPaQMo8aDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_7_TtVFQ4Z9XzBPnwJMcqxCCpuk1g2L5ezJ4Lvof1k0I3wYiHFggZnpdISNuOEJQKl2l1iSqRB2tQnsm4Ui1PD-LFt9ik61vvnY4qXydS-PJC0lQsIbXr905R6yDN386ahWgcAC_5yepq2WQ6IahyIxW_TDWSXK2qMdFZv8RPPaICgKg9g2GdpPJroBpMJ9ChilZzDpJ2sTcBaGvgVkmeLCiRkuIr3UHN3nc73eFiIoCdzuJpPFqMj84Y74LFa1SbRgk3eKZwQBJQjCDcsYPdUiNFIO3Na8_2k4lUz7m335WwL3SLZc1cxIOSviuCKw_PbEN84JtWkcvGVYyHUgeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0rvHkjj10QSkYJODJAZl-80z7tE0qRU-1bOIK8Uty9MVJQ_FG-s5Z4kLmhpCgSmoWjxmsY8AKASZVmLbtDkkSs8uYZzrlpzOIdUBiFnOQTt9YVnc2hRps_VPCUIMBqyh2pBuTgj_ZPB-S6t_3jBe6iZDWoQiYGtt2jbqkR0a3vGXuvHuDucVzQUNfJpIpD-e3fseo-uPgH26psCYxgDcnwXP3Fdx26eWjLZIQMeoN31_2Vl5LpJw1ZUH2RM5OXPMsquIV1iKhCgaKTpTiWelhV0NudvRWCA58EAesepK-RNBdMC1_YO_yUi6G0xvtoNAhPLVYMwek8_cOBAOhrFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pC2P-qjpS1hJmj_msdlWKmR-LB_5lkWZ-T3t3UB6L9IYO2hZYhHZQ5z_CmDWryP_ff8oGh1M6-h7RxTLwQnsJ_oH4LxSzJreLLtzTFKcnr8761wycKVFrO90U9ZkobyYf_gczkWlrcwwWld7Cvz1DUBO3x23VSDA5dwWkSNP8Zrmfw_IweeT0rGApeHgLrxwdWwGiFMw0eZ22yogOZFxHzOH_41sDvAjwawM-ECkUFxxs3auY2UtBcHLyz5-l27IdN1DdAUnOK6fTJnTUIRD4FV5kHgAI_VuwHjHqDs7PgvwBZGT2P-pdzNmAqtZ_h-ThV-IQunYiwNuG4cIUPaGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxkgNcfYEO8WwRtjA9a0sb1gff_FgBk_uPaqsUHGtSHbFFxdwoOs8n8jjtxDGuZpof9f0-Na9qzSZrBDiOdLUHTLSrghXZDQlidWVTP71MBgC_POxJ7Lu4CutUiq0yMpzZ0At-F4BhgFqWuEVIAyO8edD_pq-_W5cUg7_PbR9cYwmzFahBE46aD7C86sJJ2jFcoIjhGOHKIpUnc3iTY-aAzEBZbRxBkIRZax-fpiTgxbxwq911Ze8R5ZoOGIpVrbjgvTkTLBmjQlNPjtdvDZpD1xc59T7SfsIRERpA6lY_o8CjNwiULMWm7ePK_qAGPBYYAchx_M8FC3Z86juzecJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQUHQrJNnV7TYHPLE8ORPRzSXUcNB8NXO6gxo8PjsIArU7h93Ef1jPGjp--X6h-CvmoWgTdSqrlkdi19ugsAZVflCC1D3fZdESfWDZ0eRFrCbUoqESK0GF2inQlsB_54C2zY6odo6tVNVPwHSJLc0_xNxIg0w1ZwWWA4nMsMmp7ZUTjZALlJxrqd3CAeLa-uiI-Aw-9dQoKIKTgnYz0iNX-_P1g-6JPS4h-5hi_LGVRQ0n6aAXqhkK0UOSkARVm3m_BL1oX84TgyZgfzT6Vk63anRsYYeFLgf-bG5ygTTKvAWA7gJG_zw-qpwG4kOWu89zOEyNWDc94dZp75In5rDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=f6HD_6rcVbu3ryXsoD8_9r7nZcxGIXfiQjwCa32EBTmqYlsUR92zvt08LHcQHQtyjkFbjARPMdDtZ7ehxBPnLUL__Bxk6n2-cJXqZskkSeuEmJDIUWZfOEowaPcbZGYgE_mKO7yjyLa3V4_PGVhmMOyi1UXdVAqKyEYyf1IjkVOQCh7hSsCdNAakgoryvXoGnfzvbpRn_dxNjxoPR86rMdV6DKUx0kZZsWSarl_d3IAkDfAO07C1KF-UZp-wm-79On9Vh-l41JxkF02HNlsbugPJehpAxUaTLfYa6MiGeJ_6s2h6xHC83-0S9qSMm4DksTh9kwX9llD-dw-7pl0onA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=f6HD_6rcVbu3ryXsoD8_9r7nZcxGIXfiQjwCa32EBTmqYlsUR92zvt08LHcQHQtyjkFbjARPMdDtZ7ehxBPnLUL__Bxk6n2-cJXqZskkSeuEmJDIUWZfOEowaPcbZGYgE_mKO7yjyLa3V4_PGVhmMOyi1UXdVAqKyEYyf1IjkVOQCh7hSsCdNAakgoryvXoGnfzvbpRn_dxNjxoPR86rMdV6DKUx0kZZsWSarl_d3IAkDfAO07C1KF-UZp-wm-79On9Vh-l41JxkF02HNlsbugPJehpAxUaTLfYa6MiGeJ_6s2h6xHC83-0S9qSMm4DksTh9kwX9llD-dw-7pl0onA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOeA_ISChz4XX1BknAGPCLMaK16tR8USnonEXbDT4rwtUY20xbdvE8Xng7wZF4xc-2TDJmYBBRqjOQX_94VQjiJwajOe52uRzyq5mKMFwRoQ3losH-6pnJ0b2PRWDCip8p0rieZkOsM9X55EP6fpCOvf91wgdTyKT7r3UlxyZ5QAAh68vPKbTTT0cAfoLNKWA39_TyWM3ofte4X3jqiV997trkJ1zM7bfVuffTvee4I3Fk-q6qNB1bA1dYMJuUkeo0koS5r0YqyTSeSmxBaejjKACl5xeL7ppIC4NW8Er81_SESo70HSSmc1-gjQpmqcO7gNCz4JQoPLrQKgjukHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAz8nQoUQi7fC9cMuY4OHGJQDLukhHJU6gGZdgpTeFt6S13Xf39PZp7FTSQKKQ709TyCT7pvx-WAHtp2DonCrQ6RX2oW3u3KhARGMbQc3_aPn0d8NxQRjw8p5qmnLrD1SESCGQ_kKjag_vdqqEcOkfMgSGoQL0zq-AhfKo5MdTb722O5Rl7-3-RFRLKD2NI9uT8NwbSAU_lBU4DATTFF778xcw3P4zgAuOc2pRhHvK4h81HxItCucOYeugnQHUBwVmX6b3OdRUepc_xXDWYbVVtMJIfCR0NeK8dF5lREhhLnPpnHiFn2iaXaCjEZ2epuDUAVqP3m9AIXYGoUOZPmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi--8JAEIsJRh1ndFrPA_RUcWLoANXcKMjER-HjkBUNtcG_pxC60jWtXzYkFyat8Cn5LhP3uV0_DyJPaPsxmmrE_kcJBwXvQ1o7s3QYG18zpfOzqWUgmfTIuTWKrtnDBPjWBuVJ0Fll2C7ZVI-ePRM6gZqgJSIlRvIQFOxG9tmLxqA2fp9AZEg6bTeVmh2OFsagZkqviMeEwhVlAHW1W0CrBz8PtINL4i-_2d1JcAKMgXtxCXq5vCVRLNojD4ElxucKhFHRNgyyTq_bQcqnA97EX3RZ8lqGT5gkDPSI64QtVWKEcggVUku7yn7bCj9TqRdssk9gcUbbhfQM1uUwcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrS3h3KT_FLllR5x5B9BcV8-shJxGk0rZ1MmZp4BlSi6XfqssdJX4OyOS963r-gSB_z75LFcfDAfS0VtqQJXDn-5xFSMqxmRLzkz2EtGT84GnOlBSLo4PYRNMM9UNTDvpOvqMqOpPGMxD7Na7kSI3VxqLXIrfz41Sfi0Fzxx31_ARw1mDmZLc_eXjyPW9JqqphlIEJRTIzAvBt2KzeB9ZvneqU90EdITUjDIED_7dWgYlV0JDXdAxj1G5n-nh7Vpoj0rWg6LY5jSJfHX6Tpt2FuF1FaEg8PpI5XIvZeSVDoKsu5pH7baziYh04fmwgqelB2jWyb9J3cNnUbqwqFQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siAz9P_zTxcy2OKzafC5Otu5Lpu009HD5FI5tNEe8zaRMoJTtkXIALitf--KTumyzdyay-fg7NcDCNY9u2oXdlTR1t3cuuPfgrEb0JBlS1Xoy4tAJH6ZamS3JjADoZQOFpZmJH-Srsyk960NZjkdSQVSvD0RbhWHY8AgFucsR-LolK8otPXnTfzGsyWg__SjJM0KRGjt4pskjzgD97LitbheIrGm_syjCB785SzgSxVFLvR2jGmhMk26hoNmIubTnh3hkBGmOlzQPoOgJSPndQoehWsqw2Vh1wKb-H8YPG1cJ9g7b4TPGiiejzZQmqG_fA7I5d_u_dHzOBnaNGTTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgSOGCTqtc5AXv3esxHZQSzEo7ZkKJ9vqpwBFaISolDI_1HIOXHokxuYRWTZ8OcJc2iK25_ISmyUEyqhaMtty-g6LkEg3CAoe6utENNJVwJlmjzxxisE6e56ABcu0wMQcXCMDpGoA4ZnEjKemOeTfcEDgyB6I_s19MhhYDXZQCyWBYG7NoNfiIDbcTsvJ6btyo84xTeqbnKUMI4wqAmIcN9zh-1N0H9uLvhGbF0uxSgWvpJDnOXZKvvRJv-fzEwL2qzj3pB82m_qYHqsHpfsGU6fdb5oWAuP8AjA07QeTaXf_toKe-OQBMywLGpAG8sCooJjj5uJbLsbXdqRUMxOmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7DeVEJV5gkkOSHDfg5IAT82i1WSnYinjdgBe39vr9REjem6LWDTJrCdXiyHwarfZDW6ZkYypnrTmsLKG4eJpWVN_pL66fx3IYY__0XzWcBQgucd6vzoXIYWvg4W8OmxJmOL7MC0EoTtF_JLXe8iu2rMwtNLU64kzRU5VFxyv0xUCWmvGHb7RHMRvyRZQdlJZAdzBMkNCX5pWU_cMqtKmH5xLy1bFO_HuNfW47HBw1y5YpQUd1gPe8JSuHdTDfET6rflAgH53LdNj_Io8CKF58gzen3YJHfiTBRR6qJaJ_lTpsdvB-gFEU51qn3mjGJIh03KAmKU01MDBxEHko8Efw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=M7ygNrkZZuT2kxpdL0wgg8m5-VTUBmEL62e9QluaPqeCjwI-Kprn3gFXgG78NaGNHgIaKUXBqOLR5L-yK8XiAQQ2UslIPgZUT-ulr3wH40p7KrnXk68lBX7y2BTJ8okZ74NYFcDzTSGE9vZxHdQ0_fKSbzgDoG1v8eSSBRaHMNoj2Nx28cD23WsdbN2xVQMqj17pEXCd9slERl_Q9Jy5qJAPyiB_znq-A_9xdkw0X7NcD9IxnnA2R8sbnjzvePrlzCaABvvfIbopeA8xuCtemSXrOTptjh4Gu6dU92UOXQLuOYYT3ZtAomIIUQ4jLJQ_e8NLsLHnmFUEpc2NYowsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=M7ygNrkZZuT2kxpdL0wgg8m5-VTUBmEL62e9QluaPqeCjwI-Kprn3gFXgG78NaGNHgIaKUXBqOLR5L-yK8XiAQQ2UslIPgZUT-ulr3wH40p7KrnXk68lBX7y2BTJ8okZ74NYFcDzTSGE9vZxHdQ0_fKSbzgDoG1v8eSSBRaHMNoj2Nx28cD23WsdbN2xVQMqj17pEXCd9slERl_Q9Jy5qJAPyiB_znq-A_9xdkw0X7NcD9IxnnA2R8sbnjzvePrlzCaABvvfIbopeA8xuCtemSXrOTptjh4Gu6dU92UOXQLuOYYT3ZtAomIIUQ4jLJQ_e8NLsLHnmFUEpc2NYowsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=B8w5vMcvsR7Qz-sdS9PoauVgMq6BFOKK1V2OwzlwJ9z1dCo6B_aP0_S9f17fI_pTu3kdLs6C4Yrl6CrPG6MMlciWwbQzPwBonvlGy5P-1NUCRtXO5RgSnF-waAp95IR-iWLqFJCLCZmOxCA869re9b3vf_O7X69goHa3AYNBXY1-7g1evvLUmaKgW5flxJgEsdntOSB8kEPNJcUkq_p3P14rFYgHx3LM6L1iWzWO2OvnspOszATrGxDa5pfs7fHEkrjcDpOE4m0Y4-w5dlpC2FgzGRXQeoIUI_OZ1hFEZflH8goDCySeHFQVM-rz9m5m7wBeBF2KV8GZMQ4ljq7CHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=B8w5vMcvsR7Qz-sdS9PoauVgMq6BFOKK1V2OwzlwJ9z1dCo6B_aP0_S9f17fI_pTu3kdLs6C4Yrl6CrPG6MMlciWwbQzPwBonvlGy5P-1NUCRtXO5RgSnF-waAp95IR-iWLqFJCLCZmOxCA869re9b3vf_O7X69goHa3AYNBXY1-7g1evvLUmaKgW5flxJgEsdntOSB8kEPNJcUkq_p3P14rFYgHx3LM6L1iWzWO2OvnspOszATrGxDa5pfs7fHEkrjcDpOE4m0Y4-w5dlpC2FgzGRXQeoIUI_OZ1hFEZflH8goDCySeHFQVM-rz9m5m7wBeBF2KV8GZMQ4ljq7CHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKny_vRAmki7VrfITVRpddcVVhdF_PNWRfCFR5N-_UQOIJJK6wVxWp5DaJBQJ2SA4NS9waZFiXig7O49iK5PTRJYNlo0IsmF7iH1NvMYbZK37MG4y1a50PqxTAfMuoFdh4C9X3OH7FJU7_ArVywHFyGDnocUeN2FyAKxZufv31Y--aDiat_j4fj_LwaoA3T7Lw4rANeUpvs0Tyb7gN8VEj7cDckSpbiORLgb7tcgsbA89mlKc2XU3KV-8CP1LloDBIPMsbGRCtPEDEmfa9uPkZIh295QJEKwdTC6xNX-F1-1oyeMneCtNFYfo_Dpe7IKwxIy1myzundgJCU8dq2LCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOpoloTjuuNa7wwBuscF0wgherQTMjoUDDtsu4yLYIVlH6_H7r9DjggjjJxfsmQ03YFKI9ymIY7mRveINDe7zKtFreZ3mT_fezkUVP_A-uSyNQ_vufwgqQknCk04bMo27SoqPl28KEMA6ZhuUebly7qIPw1WOy2QL1KflwjnlZwwW9I2V_y5ezXe1BLAiZeDBG6FIq_8iXvb8Fm5APDXNYQB301fxUWimk8WAEeYygWCHbRlMnhuk6KWEdfxNryrl4nsThiGm18tpIUP3MKKr305XHwJFQScFeYo_cvRyOifAvqyGvtiUPhV9YklZVpHWbd02NWZJBdP6VCjuiVgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuJDL_WWdYJhH-GerN1_E9cSEq0g1zU01iaivb_uuBDW8jz2s6vsnx6uCAUqJ37rW7kmIflAvYMs5c_8Pi1IiGPmqxLifssuC6cwMpnK-H7oRBpT8spV6OMKtDaY117XPlY87gUYopRxSrMbOWKx-Lwk7NKfxzYFqWqsQZJqXu8ufYazG_3keAlNLe6K3oCRpK-ocESsM1ezk1hlIq6nWZqaMQhHkLtkEKLD6b6ul8Pq8nVAZBxWnJoPArmpxV3zAUNUFfSbtQN88PjHjV211R3TGtqJVKe8ZteMOy7LupNL145snIinQGRiZocmPHYtCK3fM19lQkLDF8Y7UIZVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnIw0ecigWBx3Uogfw7cupGrAVEtHhbruH_Em4NO2v4Wcdms4zoZWADkUFFZnIIA9UtOI7vo5LP50JEHXKD5AI9DI7T5uP7gzW4BkbAHbPs_EFpFak4TfOyOyZrHKrUSTXNrszTo8ub6OAEV3_dVONZ3vHMIn-mWydSptVBnEZPe3ADZYAepMTWFIZHT6kUCId84EACcOWLm8PhK3lO_MjAUFNXy_NQJ34SqGmFjvIwyv4qhz1fflfgxD8U5vNbweF8X3YQfFEG2zHZwDxq_frXIVM3BPIHUS6h1Oo34UbkKZ3qXXAJnUFcjCmrauT4mz4yuh2YWVUOvigK2x-XDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxt9H2KlXGyvvXAC0TnCn3VQ3B-Wt7BZzdgZYS7NEF4N93oaTnqThjeWUYPaqhkJeDhsYFafoHWM6Pcz_h4KUTlzWAQE5uzEujFdapugkIVLw6o2goe0-sXCORfJhvyAIfixYDXdKOUI7-aa4JjJNtRyfGO5zAIY021TgZf4dtL0g9y1i2eHn1JdY7WzyNFBTTvpna-FZKKI7DxV93aCHCM_syWjyPmxSfm5f_-WIxZKYJghcGJP5b6wlKe4jLGsW-dd0feHK1LETAkomi3GleFPtRTHf4zk2tavVfsXofox4fcW3X8z5PvkR5UX8DYlXVpPaBTpZTz1DJr75vw63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjcKjOluwJ_V1rmqKVuGLKWH8P7lNGFaFVhu0uUuRYDKV8p7ZKRW3qcLzH2M1KHcNQg1xcAzlM_K4nie5kejauAkOKbDrOYLz4lmBlxiX8G0QpS-uAE8Zuju9g_iWOA94hg9Av0rT25G6PA1YaZ1KbmMVnLtaMWsK0DIeTDqTDRSzMQg__JTBVznitY8sSaev9V9PO1AHfacxF75o-V6zihaINqUMatm3OfiKEUjWkJVzTG2qrhIfbBHCLb_LDvbRga0lzlRWR23TpTtXG3Isd8rtIGRu0AIm-jrQKyALgaRuYe95t7IYUXXAiDUFgCv51CwFEPLE7qhd9Z1eZFIoA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=NckTc61X9zIVF-E1AJg0dpPqAC2N8_wzKzJTXuxBNoDv_AMmov4CnGE2DXLxk3KlgRHDVxMO_cpN7EeqYNAsFNXyD0CFA972TeZWi3MQ261ETgb3VSjxR7bOJJp6GQl_5KegOXMdAEH83aynYMQiStGRUQTNo3BARrL330XGEC8rBIihONg2PYfybEIUXyrjefQr7He8GxEZBe99p23rHWqRRp0XZdFOQzivFDAjAqwJV4fZB0344Eix8QlG0kXUSR5-vD7VV8TenYrS5whJAvvDrhjjPdcjxnB7Q6gokVuQAMd60CAD3GxZSoOsVJS4riJI6DTMt3l_n_plBWmGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=NckTc61X9zIVF-E1AJg0dpPqAC2N8_wzKzJTXuxBNoDv_AMmov4CnGE2DXLxk3KlgRHDVxMO_cpN7EeqYNAsFNXyD0CFA972TeZWi3MQ261ETgb3VSjxR7bOJJp6GQl_5KegOXMdAEH83aynYMQiStGRUQTNo3BARrL330XGEC8rBIihONg2PYfybEIUXyrjefQr7He8GxEZBe99p23rHWqRRp0XZdFOQzivFDAjAqwJV4fZB0344Eix8QlG0kXUSR5-vD7VV8TenYrS5whJAvvDrhjjPdcjxnB7Q6gokVuQAMd60CAD3GxZSoOsVJS4riJI6DTMt3l_n_plBWmGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5o-VBDFpzZGBTL5kudBLkZhL6RZtr_TCG5Kguu309lhiHoBtKcxFIKFgsN-FvGhuqUn_QfXwEchZE7BsXaSTe9LRBaWxTlE8CaqEHqWIF6QQt17P8bqdL8O0_sS6cVhk0r0RpLyiTxrEAK85UceS3VPjxG4jlgvd80l5XF6idj1_DBBxqafD4gWCMSK1yW8nOMmYpIiVivPZkk_y0RwWw3aY-VNZG8FvQ_qZyd7mcZH7RSqtkvVPdw0GPpyJD1c8BCYDhgVbps3fMtESOG4T8ifXceeGSm4O_J3H4v7ZTsGD14nJjowna-s5OSMDXK3m0UKJvun-3CAFOyyFnV_YA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iun3fawtp6X1qgxg6E8u-Eye0TqxCHuMqmDi7jDsVEXF3OpLLysuCOv58O2AcaSbyVZZnfAW5ePkjyc9_1eDLY2aJypJH8XeeMzQp_dcc95WThmqDds14f6tb4E9P9TAIc2o2rqD1cQksQJEutQj4_Doalyf0c3Uz_hCsZrXAN2dD78FZ4jFYMrSNJH6H6_wRwKjIX_-QhaICYNUu62Qy7n9j2Zk06bJLhP3U2jF8xMxCNTTcdpNGkDtJwz7xrvPdNALZBIq6cA4a0Ph4ad5yQPRV1AHxHvHgiskJI9Bg-mXLZRJX7RzyxejNGG_ZZCqbvIK1c71pAhkAWanUCQksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca865Tmj9ITrTw4IiJCwDB6YHi99JRgRF3-LrTDSNWz3AqrxiCAVyxVqGPDtq422CeuyS71SoE4Oeno1rWcUGZfF9GKLBeu-im9wBPG3E8_BbKmwmS34M5u9ir-N1KwG2_Vl1ifSLK8UFNNg8NSVJsk2NemhR3lKzSZmNlJUqTDzLU5ThcMspZ-ZdBHRWpfIdu_BFMRDf4PaQ4b6qblbGzlmXMUnHEvMf9umc6uB-8EmBgP7JYvxliHDuhpPZFxV3yoC7js5MCnk3eGFA1GRA0CfBhgyD--LvnGMEXIvl_XCjURYPOWokchrH3tXiBI4gajGbCzPeR-GuE6oE1y4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4a5yZ5LusxxTYbzhrgVCg-Uoc6WNkX_nsSMD0sgx6_LRIkafgVTtoo5lUtuGpqIQOUSpbEPHYkOVxS0o6MF2TWuyqN8xn1oGYw2Yc-E-_q-PJV6WYx7brBqAVehpKEROeMEs0rZGGqqRSPMOXcmMjqWGU_m_Q3vT9r3hk2mJobmJ_yIYj6COu6G0mFyzzgFsa4hABXZ4S87cKzol_9O3Dat0BoPjfru1P4k88eKf-YXCDkcJff9is5k4Xzdx86gD29ygWdciqQ7xXMs21DOOhBM0fGOae2tdb5qUSm0CTjUfFzzJy1PKn2GCPubwK8kqB1rw3o4JBWrbIQcbcGVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5ww-SC3b_ClOVqaqe1Z-VbiR929iIXA1fnp3ReEl7_IRyT-dpQRjSYz9XbcOKqGyG6cqO6j-N-A3E6o08ZPBs_PPNvbk2qDlIZ8aKcIa-wSnOSFWuoUeQ4bUncUb_67lcFEOV7N9dmeoCi5Ud8CssNIuHAd3_IOybwICLkpsLxonF6okZ6VvmFKkFLIcobzUwKV2G9qBM4fhIroOKkWrLDOR-wbEBgV8pdjqA1acXoJWHSvSL36aaKrpriwRWFB_hZLFXmeSBuus3r2HJRNqc6siUa_nybprATxukN4m9ljEb-eT8xB6wN0iAqyof3ataOdm3-gyjoAUPv1pQttEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzniFXsi0kLg0ZsxCRZPN6VyOdMVkX_snxuAkGLmeGUCHrgAEphWG33nYqoFI-tPgfjPtt8bpXe4NWsNKlrzKsLl4NaNPro9-tlomwtspppHdx8S11aU2Q8A9HZXDKRLGZkv1XxRR3h3F3e_K1Ksc9_qeNxiMntc9IIbQoa9NDV0DOCTHPhKujIEhRsmBGFvUDLJEB79xqdZ4K1CkXOHoYMDlxOnja9cYB3QirM2yVzgZHfxkNPrgXN_99e5aU84AagNnQ60lJoRnML_ZT6kwCRnwVLHqYWnKS0maITcRpaltGBMtOiUgqrMxHB4RyC4m7u34aqXyKa490erQIYvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6m2BrRWOCTF6DSysQSY-sjf-cqqjlY3nY8o0dCeVjuZrWP0iDNDZptK0QzpS6O8nOAAPKhFNxGdBe8hyPVQ4z5MspBG0R5eXYuk7QpHwgfave3xztq3KcF2-SJOJW2_6V8w4QRAMRTI12jrtUGwLha_eoJP19S-Oi78hTF_WOhEmg8tQRWeSIhNCs-J837Ul3P1h6kMak26uAuBnsbBntnBd288Hi7vD9_Lcc5NX273fhEv7CgHnUympChkfwTL_riasZ-Cj5_2qmFXk2kPyDKvz_klDDuGQnNsxE_VSCMjSDmvJdc9mRLX70NQQsArkPqYBskIOvVMmOcM1-uiDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6UPaH_iGCv9gok6-q0eEOwde_X_lky2-TqwJHGbN-Sv_-BvW5FmSgW5LLmCARWc9LEZxBcI27c51MEMCukgb6K0estt0EAA1GK0qL44j4qYymssDq-sWQ2NZdBpIEP-BE-aUroAJCpjuIW3pujkAB42jJn_dEYO8ks_RBIbFfHOhfYyakVSZJR4Mkhp9F0YUc9uCfcbSvCnPsk2orDer1LdIKt4xjqIH-Mv62AOeBWGzIaeonFRI-ZnKGu-9zlO6k6pXzxmds9T89nvokr3rGx96rUYbrTv9He2fFopbbZVAATyqOJ70xi9XppxY7iwhOLI1_VmO9c1Oe99TDHggQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgUkVYEOJCbaUD2IsbT4V9dZMFMq6I9MhHgNHTJaDVX3NHBQ5MYmUjM_25TgvJM6WRfk02ZaVGtFEIwalQLzkW4q37jHoZdYIxOrVdcwuDMNjgASveolEF8YtC3Kp17L4U-KOrP6B-obD_vGoXhGU4Ky-AifuQoCfmK7lsQJARq3DFW4LEMlqint41Ca2ckDamHA7JvQH01qKPWb4LbjBsZMQQ_D39OfKNvY9vcD_jtUzOqVYH3y0CNdBaT15blRrygK_lm51kya7xUiRvYgTJRdvpr9ow9z3A9Vao0-7JvOjFR4khOBBu3cnlizZcS2RQCAuE74P8A72vkBErQPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHR9D3567CTBUaybZvpICiKa8gD0wcOcN2QQAdsvEZ3zZzYT0W3cwtHj8z9hbLzqDBovSP0PpD4QmxYxNiVy4nrPFdvHedvzSHPbbDqgI9KaBavqLVhfGlhkEdS-oI3tbD26vT3YSxq2zwfCy0QivaUebvhZQTvytkJX5wICh_g5z5V_am1JP_wTpEAUtTNZMv1Oxary31axzQyLgW1z9JOjofkxzeg6e2kUEJXldMDz_LJmQ4UWbnt21Dt2jz9Qr6nTZRGkMzeQYkfMaEeks_Zp0f1T9fNM1nOBr4Gc9CnbSRHLNeYPgM6Q4IqzngtTd9aB4h3hLq1tUOShg_wwzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=A2hnFU1cXNDbDULXu361LkaRXJDPBXFaHwG7SPuJGEKMGbIAXC5VM_X-aV8SUTBip-KfACXA2irIfMrNX7YIreIvYPuxOYCF0PEwOwrDHLnwByEIOgsBkDV7XLeH8oF8m4Hgjh3MZQwSZtWGbZMuoR5b6i821zC16M2FdPnUIv5-BZRYtgW0iRK5lFt-piXgUxa7BSqD1xDLPkE1nxA-tc4wWYMMvCls5VlnSULV-DoyYicI8hM1VUkej4jP_SvdsDGjnWBYRWaq2Ke_ebB3CPm_eGHi4nXISIP9fhnprt132n_fcaI8hnwqgBgF6uAUAqyDY4JEukf4uuNM9-RLoXNLTpA6Nx2hzQU5LtwmDwGigvh3NvJ-cFefqisKcmZ_Va87qL8P3t44ZkXSL9d2Sl_1dmz0fxJdbE_jF_NrEezJ1CZDpxtIbZTN6RKhYHWVpPCxbpO68KVWVvjhiAGIgx-UDITkwbG6FekvX7c9JcSKjZHp7rDFd1VLnItVYW_WeHpkUFXyGlnebGtkzPGp32wMlz3KONGYCXalsEonBtjPTDE8ral6ktcRpNFCKARx1m_cnEmlhYOyymPimYmdXMF2HzxC99uM591ciMq1XteduLx6-z-d3KKUHYJcs8mjHLyLiFqbL-uMqYP_RpVu0lKRqPhIS8xPqEK4PqP-t8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=A2hnFU1cXNDbDULXu361LkaRXJDPBXFaHwG7SPuJGEKMGbIAXC5VM_X-aV8SUTBip-KfACXA2irIfMrNX7YIreIvYPuxOYCF0PEwOwrDHLnwByEIOgsBkDV7XLeH8oF8m4Hgjh3MZQwSZtWGbZMuoR5b6i821zC16M2FdPnUIv5-BZRYtgW0iRK5lFt-piXgUxa7BSqD1xDLPkE1nxA-tc4wWYMMvCls5VlnSULV-DoyYicI8hM1VUkej4jP_SvdsDGjnWBYRWaq2Ke_ebB3CPm_eGHi4nXISIP9fhnprt132n_fcaI8hnwqgBgF6uAUAqyDY4JEukf4uuNM9-RLoXNLTpA6Nx2hzQU5LtwmDwGigvh3NvJ-cFefqisKcmZ_Va87qL8P3t44ZkXSL9d2Sl_1dmz0fxJdbE_jF_NrEezJ1CZDpxtIbZTN6RKhYHWVpPCxbpO68KVWVvjhiAGIgx-UDITkwbG6FekvX7c9JcSKjZHp7rDFd1VLnItVYW_WeHpkUFXyGlnebGtkzPGp32wMlz3KONGYCXalsEonBtjPTDE8ral6ktcRpNFCKARx1m_cnEmlhYOyymPimYmdXMF2HzxC99uM591ciMq1XteduLx6-z-d3KKUHYJcs8mjHLyLiFqbL-uMqYP_RpVu0lKRqPhIS8xPqEK4PqP-t8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3yhGlUZtAzSsZJOQOUvcl6Tbo4gEQQK8STjVRXvYCHMk0LNnztRy9Jprli6oPvqW7NX7WTi41UFQmvFao_mDS5JMg2ut1-xGReIJKc8k5wDlODG17Cy_LX61ibtoFlx1pc2lomAb3F3RgwAkTPXbT6SpCtfXrknH65mHzaltEhp_hecSPEfmd-yz92ZpsCxSpxaJFBHbTKmjbkKJy965nRwn0XR9K2ZwKYzMeRDQ2N9neNDC_0yUAsWkzM5iVfZm_QpKx9qx5TVNfPnCS-Y6j0TlFFh4SvNfgLq0KBY38TTJpjJV34HaduicnIP2bZXeZlrDSJ2QbD0RQN0J78Lug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du-CuGt72iJZIm4q0y3FCDDu1bru41TsKQ2cak4ftANljp7aoQB3lR7hSbfyFlhd95rff-Lku7n8B__B0jOuVM8ORJgf7bHGHQU6fPxmoBZzgORBtjwOnEWpP5t-OzzMrcHauXFgSKSFnnc8867Pe9PVbZMuQB2B1qeEMpl1eVJkQrG3ZUrTGTI6tlxG19kN3bKEzuLTPu6fgmCly6SHUj3uUBFH-1LEl0bJahdRjvXQ0jTIm8-UgDneJJTOgqzCZNwqzIns8b9OeiPiD-e5Q1qGmrxu4zYzPF6tAM8rIMnHYLOk2H30-u0oJ9LL_4f5F8ILTMP5A0DtbPdgVb2tnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRmAUyoggZeVl7dsOs6OnPACTI9NcN8JiimGWnlOBvpCO8iXVIV0pneRVkBgtZu-x9hGN2qTA-4FLyX8_K9GaXfcQlta_amB4dQpPP0_dGF4VkIep5wq7G9DhB20K_as4Ho11PjH00hTjI3JIYX9K35tZcye0Armk2h_y5bHdHbBCyYfDmG2F0Xm-jbd9USwW8D64YY_J5De6JfIRyBTvC9ZKXbhU0PvDmgPjOTAMEANU-uxSlklh8wW0vX6ImNrUjcoWcypHdi7xiwllw3mOQcs0FeJ_VX-21dJmW0diJPBlr39nHzQbzjNkXjvhk-HEKPMZQlGSJck8p91R0L6nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVZz8gZCk030ECarizSJwn2ZKkvmJ9z8bh8xTMvsP1adEexrc-j21O39v97bdG-Emdlbk-N_qy0aKlRG2F1s_4vlOJHAOXMh9ZZkuxQ6EZFYPoxrD1WXd-eOdhV34LKYnn5jPCzC4D4kmldZaB-ejV3z0ellUGjAG9FeqoqCVtzsYWgV-Tm9j362vIQkk1K1j8-1ZSLY8YTbwewKaI9VcDwk11gKSx6wcLbzdhwZ7nJXVgfb_CifKXItdnwBpJhZrOtW7dDXgA_LeLBZSAQuDX4bzGVxW5NLIVJr6gshdhXjxIRr0_hO5Isha4pr6fJUHcd_6lKnF_r2NBCzVqA7mA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTtnbim6HhwnA7sIp--CnWFI5bpsEHwjS2A3y7WBpRDHK5Ni2yRQVdYNzpw7s1rKEQLJXmHOW8HY_19a9zS31K0d4YnwYJC6oT74rPc2gCSm8BBA2uKrvj2XIr4qhNkuZI-Y4KE9kb7a7pTKDtM9COB9-mFRM-o5vWJ1Mj9z30YTTYLuozgHEmn8p_BlodjqbcTGPMmGJ3ZdQW0q9JpXA-N9bCZAOPByM3mMT3IKG_AjloRbdRo1VsoooomAB1rtuVzX__4OpTRaNviQTvby559ZB5j7uPGmYUABf8lYpAUl-abgTrreTMGqsNsK4OqXHJRHYuCYXyMvdvAdxsFyNw.jpg" alt="photo" loading="lazy"/></div>
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
