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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 22:58:53</div>
<hr>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7RDxvC66dKTQ1Wt0sAqwCXiWg2IFf7ZfjtbX6nKBWY1BeXjF_XiILB_nTK6_6zEIaWeTyiktX2r_e6YXd3uraB2tVIqFjnn_wb9zxMJs9Fd3vPDmArdMwIksTsYeKD_h2RssTC8KngsoIR9KmyNIfiO00blpMR4tpSvIgiUSS1SnD9TByiOWC6amZWz8X56INa_S54uEwKSywwxkzMc2K8Ppzq8JM5Apj9x4QC29lhATffFQj-uOICFsOxBq5Qi5T0ZrrlOoUy0czBpF2gndjMDbvJw-mArufTfCdNZvHU44JK9GjkQZPEyJbsHBdbMBvmbPu0HFzvLm4xRy4MgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCdyUQ1YBOFLA4N6dfEO7SW_fZuWFcConm1oTJ46BUMO__yHA_Sf1oqLUDQtcW8EiAWnwIGdcZqy70R4-GbWMQLCbi8Yp03Ykwu0hMCqRLr1HfpbsVWdOwrpb4aqF488FpAnDnzJx9FHxgbVjlF8p4h9t9aBKVYW1kBowW0HCwFp1RVHhiCPKb2-mMC9uNHhy7EHEU9M3Wnboijaua3_bBj-ZMMzbmDerxt0fMOP3LZLcyR6mqsohIBexhtODx7X_lKbicoAnUvOaHzcAsa-4hj1S9Y-emSkcuc9yCgSnVMs9F10t-F1cGldykqfvZ5rMt2OACsWE0_weIzSc1OzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj-veqmFkxbU7tgEThin7mBozcSogSB3LQXkTJ5icqIiQaMQINDwSOdm-tyEkAmGSPBct-bgcDS_41aWy4Z1gFyjMAe9w3JtIZfEpiaOafYeA79Goibog1MYKJUOoZrVLGgo2ivjzoFaFN08q8-l0c508p4HRfqovj9KX1BlG8HfzJo2t84zQt01qatm6H203C-5RXPcmKLHYNT5Ileo6bKnqbrNqwPw8OSuzxOURv3FPYKMu6dQ-M3D7tsv8i__t9roAhIEVQ-zNdQgnxA-xEWiMpX2f-o6IgKXPIWb-g0hPsE1xUjHXIdfC3S39KgVZu_HsDy69Oq-vURNY4uHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvMwPm-QRXgeiA44VhXcmxu4vQJCatpqA4HTVNlW72uFHDbp6J6DWT2VmeEIJ1PT7-2pmf4VWnQUfqKRMgKYDzrmZjaQ04FIvNy7Af7D-eS3spur06vgKp_hKzGfj8JV5W-HlBH6dX6YMnkHoBDLeToYZPKHToxXKWLCc6Uk94PrsEyT8pofYQisQOhAyUQ_cJlC65QLxAQV7jepUkK_YaAX6MO14dIA5id534sBJ7fI8Gfn7SMQl6YzNWHVmXgxccLuRy-ACKR6qiheYhgI7Cny2h0A0_0LxTqXg3gxEW1992qQp2OUASVReB1HnaGQdlR6zbykGqPAWG9XnCbOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFSjT3XneP1bPb5dmETDnWqc63IixHhFLC9juaNCU-LmovqXwr5DtuZqav6dW0v0jIYDNcCKRwehe2n2Wp6_-h4qS5ttYquc9_JGI1h1VmMtdDbFH84vvqPsfgvpw1xrai0WVwH_h843-cemfbyEZDrIOgIajPikDBul_YYel7pS5DRqWiTZyxDXgyTSHmKq723LixhHbpzPKeD2IqtqOfbVGads1kqXsEE7BLcFW0VcVhstdSRqReOVZ3FTFRRIN9KkNZddqWjS2PjXgGdmMsG6TRDfbJtKnEt_KHN8eZI-UFs5T8zj21tG8VlhXxAFPq5_1j4eTJUdcAwadyL-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr0PnkYnw6ozYfDw-hax7ZMyYTpCWAmjudQoCTZZ234poz_rZfIU0cetvhm0ayxbtRWAcqYlokn9id-5jBRkYz4Kvbs5duEWSAw2l2gxlacP0Zk2VA2RU6x85-ZxoveAl3QNsZDLR_YKTFaRKvMqkM51i65opFxOMbe9GN2qF2qpPhJntB-RALhybappT94P4EjcIForNvaX8L_2k_hkbmdYozgZZeRceruC3-ONhTvfiwTQRAjzApE7Ycz6DFllZL82Dbs_L49JLPcRbtSzXPVJo9DHmZVQlk8H-zrpHqp1EjT6t0MPvBQk6ORb6LZ_aZZjbyCsPyYEsANxrmtFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfzjtqSTUcwSwvrFD1VIyVc3DhYSc2BnEKrgKRKv9klvpm08xHMO4kiKoedTe-y5eRoX8e0jyMnmvYO9zQFbSVV4srveDSTJqdu8XyScFgJk5VoVYZ8UY_sNC-lJ5pH_Pi3-2TTFnN4FNRhcZGNdV5eEhM2Uip0Wfzp6iN6QbTpx-CyzXiH5GRjMAnprbdXsvTrOWEGJrH2ICSyS4PwwyKMU7Jbr3S5tCkTmpxILLpTBDkTclZThIrWe2FOJufWx0CWRV2BUo8EkHO_DDJkB-4WxyPcoXEIb8bqDwA-QNCPxsmz-Jjfo-Uze4X9siYOARuU62JAQrwmvC9eFLlRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfSzq-2Q6YKC9WkECyfY5KMufuScUopC9Y9CjMac-XiNRrHoOdSbilgMkJ44fKtfnM37j0boSi0oUCxeyaEeGl2XqMa1lGSxyg3MGp-swxMzcjz2XlSC6XsIb1rFTqJSeRXa7nz7s2zHc7e4X8qPdMAjkwZarezCpNaI5XvrbaTI1ka6MW0FrEVAIg3X99t5bpKaTxPxb0Z90fPvainnsJ2d8SBk7kDsf4l2952APF-pXbujQmeUSNoLdCabAzIVclcGKjOBX_B3_ShYr03U9oU1VV3jBnYLWT3fMtlaqb767cqIbRbQ4GvtAxmS7xX_wEwdG0BETzk13YMH-7HcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-aS9QoLWdmidC7uZgc1VribhUPHJfDQXmmRsCd_dan7hr-m8t8lE5jpW13z-d7e9dzgngZGCZl_8qOllGYwnXyNxDQDDQGAltbeFl5Ru-oVIijW-wOl2-K7oTUB0CU_jdWkOo_yrm6ThtGBahpfDyOQlUL0qnPMopBJYk3ZIILDJ63qZnDfnC4Jk9D2203sHJG5dNkBBDRu-C_PJoIEpcbZvfzJHjHaKj00mVk09qwUYr0qh3lsZnFXgQy_wZcSDfye9bwR2om16pgozizRrNEO6pfgwXK5nQIU-H7Xyj2liIYTcz9X-UoP3BJdv_OuDkhGRlgkwM6HrvmweoqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsU2G71yzcVDl3VKjFrlwBrKCqTvviDLmERN4A7oFFmQbkxxiS207POFwqUK50OPtv7TnZth6vgB4RYpTVNcC5Mk9DaQPNh_Iuf0Mxuk0o5ldiRivGSOSphldVvvuUbTJ1hlRA8P3wY233CH4CgaZIRSsysSHgRAktr1dDXqMHIrL4cp5mz1FT1OGMxCaRrmDBYiyoLl4w2-sQRJ-pjgHLfdBLeYVd8PZisuTFjPef0vS634eryFjqZOpp1TeDtVZ9L0Ru9hW1vp5tmYVxPq2fGNXDT-mqo3Ti6kWxc7STahPD-7RFqQGuBTf96dU4siWJBG7hsHGuNyWUPPxUWe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEWTeaIbcJhQITPFtuwtnPLY7yah5kakV4Br8aK2ZLa__L6NlP0HvxqQoMMypKTQNe8BzPXdSmugzNw3nwZTa23lcmYYnR0tzjaMNcxaC1yWMNiWL6pqlNm_O83DsJKeT8R3HqN0ahc1ZbCk_VoaiiLn7N1nXFkCqRPtfjBvBcKNGPXHVmemMButULvxIUrWVjD14S3nW9MwRu8gNBcYJJ2tcc8-1K8aPTnh1iXa_7qdogQeo3kYm0Ga2UmeakRt0ql4Ghr1hb6IJmnmJJMN3kew1njSBx6BlYxvNGItz-NOcYxOIUIng2isuxjxNAOW8Z8vDGfGoqd4d97Uo_elng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaTy24xa8fBDvDA53jyhcaLkqD7VdLbLlP9uEybVVXwNLYyeCf6M1HUnyQVxQJp12pWBcWIqlEvjT5PIgQV-HfAIgwUqHeBu1LghGESl34TZV4S-CNg827e_Ra5ENgBxOCPaRBTSLysSJOleWxo7l_tb4hH-EcVMXX8QWN_4MIXkkZNF7nu7cJXlnJsCjuNKfcb8P6ROhI3J9XBixnzENAMXAf4jR2xY6Cis8hGQyYQEhj6vbSQuHaA1XV5RDk0WGe-0G-Ji_R07bGgUK9W8Fhl5li0EpQGPb_77JwxsoyoPDdjUP5vhPfsM0tjqbicdP5mxC80WwI4fGJzU84M88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcmQkUBbZvWxO6g7hWp9Sb5LuTS2tZSCilNfeqazDCRuqyF3Ag33sPdgiRoQEQWywZLu_VuCVGw6Xo9yMJxLqgUMdZjAvjZ1KMeoScpzHD3R-c9bQ-5krdk4yFrDPc_HTI5uYpBjMpj0FiNV6NZaygFTvBCroy-adogxkqABVZ6n19aUf5ItKnQHaVkp8FpWtEuxTsUbAG5qg-TMPAWt-HUYrYoxLMrGWqLwrxb6qm13FxW0I9EMleB4SALpR8s0274hIci6LSu0ATT7LW7SbL0oY56oivOD_jnV4HMdf20k11lrghtQq4GxCknOQZJfRxMTzqQMyIzZhZgGWkJ27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfth4dUI0te7qXgA9guT4YxpE4flyoOm8XAP1MJmeFd6SC5Ilq5zyfdZLp0wSzbnHEcjijfan2KuAiTGcUX6ZDuX-ucx3h21lqrWmSrqgxA18pheWxcLu5wtt2WUgqGkFtC8uHFj3FKMWCUUteoczemBKu0XaX1pBS-MAExP71ZYGcze5PGNkBZTOFYvlbBQ05D_4KyfWAHupxWnX1cPRQwuK2UcikeMVN-7qgVe7y2aBJXZXF12ZSlRa_VXFfaYGRJeeqgXw0pIzaUgkr5Bv6dF9k2BS5-zkWnO7r8COmAxyui9bH6jgNBjDJTkGAfCHPYaQEPo7LBJ6aUGGHvVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkEsi2StfGMjI8Beu1sIyQ7SnuID3lmeDGXBh3eZAmxclHewUEF04pa7h6qHDIFYaRRRFcwViHciXdizYnwb2vcRRVpbSR-5q9f3IL1dtpUio9K6WD1Id03MSPIwuKQCVewKE7euNzYeC5v9_vaxauxcipN-1gX_sEJsvk0yO_e02wwi9gD_1RibC9iuVDFU7F0Ep3xizVWAAvzDuzCRak_rQmJ-M_L3hqxJb8jUVQzGI7AQ-OmcF2JEfjB7AfdChfAbwUciODoD6Fs2LO_WefBDyjhv_pRWCeFJmBGqLPbRFUToBg6S2l9zrZ0ZAvTkI-uRNbI_XsSoRIE8t0xMvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frJr0ha1KtRjgqPpqZdNKw06-0lxo9DP52WpDKr534eWd5kiw1d4e6SCp4V_38fDmb4E1fWIN6nLTckmz-qlXeCG_csXfIPMD3gqgXhi0Beo7pp3Y8Sp1W9QPJBZy4y0owbNPE0HWw_z77e8fHT4QU7e7syYRObFehQjO4VZQf5Er05b6jWjbeID3_UXsapJec6shHOJ7g0Ff1FRkxijyM223uxOaSHNBY6ZnZMYM6_4HVrUxGRRjjUuCKphik9eROVnfiPDvmmdrrOhyejnM2iW3ZMn-3QcByi3YY2Sy_Ki08PXAQc1IDSo8__IkpZLH9DxPe5usDjcG6csNaVreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_EbNc7_7h3jIJQByHBnBBQszqw-zH5nL0FgxG6R6COq1N0Wt439XwmE9Oql68OoqlEnH9MzBQuoXiHBEWXpAIrVjlbhj980pOEg5iRR1Tb-uDxFED2SPnP-uuQTH7Sp4kXBGxrSpEmYSfddjR6McWKp24ONIy-EcVyqEQv5-8MFCUm2l2w1txKmvQDn2B2JVG1_tCkjKi-dogrROHXQNr_VHgckC6uFHUaRJJZDHiMId3CZUH6dUMs_LvqqM3_7k5YXwPdzjt5zZKS8FhUw9PGJbYmnuwFjB90n2sz-jcV1m3RfXQsQzZh3ImGMTNnOmyvphEnVQGdC4kVqZHpnQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtOlyfj6zvbv8YWb9sB_N824dRaOeIbRnfj5kmky25CgvEymzr2KYGoiGy26xxdGrgTovA5sb7viyXA6g3fDpnz5yGUxgtjgl9ZvPo_KmzrbJGo5W_1ub6_j1VA3t3xUdt9_a97X-ecfv7OmXHc6ro5lElOnEeXlGEN8ZkrILvd_eLZI_QNQjOUS0WEkhv0Rca04wOPG7IuNeIkCgp5-GPasV8D_434lCgLsqUUmLEJzl7rJDjoUoGl1XbdgtubRMeNMMv5Jub1WVjoThT3PwzIu5qg-cCkAA3QPggPDcIqBPy13vRrkFYF6i0U42dZrD9Q8ElyE6XQ-kD6eflnz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wATIn8FQQ40ptHAsaiuyAXJKO4_J_mgme3K6_TkiRgYYXafE3T0CwR0HN_u8H3nOI7bOOYp_XfwH_v2LiowDmMNS3ETG-0grxeRiIaQLYqd282htt4K5XAWqb6QorOYICVt7KjB6U-dvFXIxsDHN1v7_TEh7KXDvwOx9DmbzcRaZGUEZ7aaD4msirEYt32oRqdMcHwaKaph1GZ4Nx36xyq2xQLtEmtA7vqZrFoK6ObQ0qoCQ-rvuQ6-3Cg41Dw3Hq0vquPw0khQO_0mEfb42Vry153LAIDWRBBtkXWJ90FhacLyrD1U9tEECTiL2hJ5IMrOXG6dycIiYN9dStrMogw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=Sg66GiSGqUTQrLTT4BKzCBqujGKZsDk6Hq98pT4Dk14hxiRdbv8YGV8HjdQqFmudO5Q4TKHmplWkq_DK2IOQ-VE8Pfk6vMVgHtenfSZSi6rN6PMEWy7uVYApBAYzm0-3Qel2LEEEpdlsQWXHNK62KSqFkO_m_V8t_XLxtRCNtonxbxbqefskmYIMYNuCYbs8UqteKs7zMmxMObp4cf_NPIKZcF2yO1qKShoBMmaGaCh4Gln3EMR2YaEBhNBvtJg1-DdyDhkGbR10eIz79sT5xwI0IfbzfFSjLqD_O3dBQLPQ3GL66IuwDqUuvDg_qGaFzG6Ri4k6HNPPzVm7bjNrxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=Sg66GiSGqUTQrLTT4BKzCBqujGKZsDk6Hq98pT4Dk14hxiRdbv8YGV8HjdQqFmudO5Q4TKHmplWkq_DK2IOQ-VE8Pfk6vMVgHtenfSZSi6rN6PMEWy7uVYApBAYzm0-3Qel2LEEEpdlsQWXHNK62KSqFkO_m_V8t_XLxtRCNtonxbxbqefskmYIMYNuCYbs8UqteKs7zMmxMObp4cf_NPIKZcF2yO1qKShoBMmaGaCh4Gln3EMR2YaEBhNBvtJg1-DdyDhkGbR10eIz79sT5xwI0IfbzfFSjLqD_O3dBQLPQ3GL66IuwDqUuvDg_qGaFzG6Ri4k6HNPPzVm7bjNrxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlOfC_g1KdW7UiQXUqAjjcXpVRZFGDMOAb_9Ogjz4KOahpcH5l9AnNUdyUOE6OGfDnrQp8m3IS2KLJB1jBorDAP2NJMfqoGN6O-xlT1RldQwH_ludMgk6G3KnSJGOIOKsW8GTIGnPf4SkCc5sa4KH4pwtBLB6GxAG7QPcokBr3Z1w4tZRILhti0bhOz2ktsWcVfI4-vC8Pw4CPnEDqqXjvumivZ7mo-T3wgiFt-0tuiS8GdLNgQgsAz13JkDys9BytYbqHHXlH_vw0RGO4KlzKtEF-ZypSuKtxc3Hk27XD7zOaCeoZCAJufaGKDRl0dT2YpaP-ZRdhxpHXPoTnrF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdU-gM9XU0Z7fEdfZM30sFtt_iAp4JVYG0TMvn8MdGm9p45mrVO7J_cGGOAkODVhRFg3CvT6Zz0WeRZMEq4iwDfdpYHIC3oivRQlFPcdRCJgFftErLaMPfGnAPCEUK_Z-lNcWEw2XJhuX46XGMYo55zm46bVRGDsKjxAsXvVGA0lzW0_YkQAM7z-zqPkHB--RVwtUzAqqXCZW8cHlmKWzTjtE7ROHheFUe5YT-nCeP9dQyNsU5KYaYX-MzP7ePnTVBKfCCIGGPCGUOYVHo-OCB4cTECw-SW622Xr7KNk1nMvyZNc5XUoa9L2Tal4PBlkvFa4a7lF_ano30PPHWlXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1b_vpVYbDIoYQ5rHJFIDoIUaiKfQwdjCb9bane54sgj8JSey6REJWn23SJ4yYQiIvZScXq58EMB5lDMsDJ3FP2687gamt7_ZezL5dv0a2wmM41QQf2Ns8-qe0ZjseJ8hLz1mWt-fneWzqgkg_4xFfW7yCwEM1qzrhEk780VYivXBVNJTS884gZN2SerlboOhIhwkM3_qw-M_MgzlOQVbxaUqfZwq7kQxHcq3lnltmubykKc0_1Q5TQ6cmX1fJLPYj4Ku9wROuHuV47L93AVlsoK2vjlutlMZRRsnMLBRxLwDMt9_--5J3u2vNddK3KLxFKfH-s21HGmBJG7QyeLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUwkasY5RPPCm-bLsPlXbibMK6uWPx-XmZgqZMWaQkOjmO9pEv7d1Hbg9ep5OyC_MSwnZn6ZH4Flq09y9cY5UOw2XYPnP5yfaRORaXjV2aDIdp69XuEaLtGsJdQa6znKoryTx72mkH71z9U7dS_GDk3-oywMBREPX6RgcCzsIL9FOKC-HZau-_H9ls1nk_8sATeGh6farkBQqIhSj34HmvILmvJlIEik7OgnyQCkaAkWGfW_89r0_lCYDlH2mzw70JIKoV5JSDu88swUQrUjAeybo1-3xMwHAXNDtuhc3F6IumPcrLV4HUnelm4n-IU-R2wfYOH4EwlVSABhb34kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpq1xH1_zkLfXfzUduhLAiDGlVTxV7cDo060eJakOvJ4yvQ72gdDilZe0IE8ZOStDNwrcO8BzHV2Du6wJQNoHoIifBtVpbWEy5U8T9EL57l99xAYqoWRRkq9Qrbb5r0_85jpro_tU-oyUdnGBuQjHuG8P6SFzCojMN4udxN5ZErDE9ymlCcYnycnlylMkYNFpZheK-jS4uAXN6uu4cbvbjrCU58AEoNFmaznpMvvtDNaoMH4J9QEQrw-VTkFUU9sz4Wg4LRtS2_E5Z8z_G3w-HDk4YeccM0yvEPeDpn-r-dFme5PmVsOcPtngKvkibPXxENgt1m-wndKi0lTUGpfww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0h8zPc6PeRp2O3LdSTxCdSIMDA0WZoMeGaI9Nmg71ZoAQ_hA-IXi5P9PyzvM8N4i2QV_qzRxAKtYvg4cTr6eP6AD6cTqYOjKe049CrlqooaFu3q7GbYYKLQe9ITb2JZ8Cb5FdDB1Di15W-zZwpHLJ2_K-hTdX2pH3nDGJBw4dVlBkvn-u8WwVu68E_u4ZnXf-5HZGc32Gh34SkXyIbwhCtDuf2jAP3EZidmYhN0f14HbewvM0EZmtCZlLwRLpoVErlOfwkRhGk1Hnv1JCqSL1oYG8Oo8hK7iOo9360xlYKmU_PXJaFGUq1jIv4jr5yRX7P4LS5AqlOxBZGkt2T__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjFUhPXyckOk7nPx2KFrNDxgxsw41gMvfwGsKnKoUXFodMSv5mRNrWenwHnqNJbQ6IDYlXWG1wUgPbUgrU6SlLSspvVAg-HCF3pHqOnCJjvMuXC1g_77Q3dFuA9X1W3n0_ZJ7TB9sSv20lnI_5V9s8TiHQEJfqtoXdIiV70n0PWpG96rQh8ynZUZhJ53BD1VSJ-eqLwVy_wurI67qEjtjHYts16jsKULP1oJpig_2WvCk_wKbr1cyYi4EU63Z2Gg-vScrVy3Qg6csE7k_9i8IYUUW1bWjs4jHiafM4zPublbjWc5aUl44bG7pIe00rdm35Oxv2ZHdpwWGZhobQdn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQLtwPVhhV9LgdfYlfpa_Ep5HxljZUQ_cPK9IjfH1-XdNpmih_6UeQIPIX_ndlr_siseOpyfTYLbe5Rbl-N1waeYJHfbXL0a3d6FZlOYppqleT65Q-5kLTt2N3msDC3KwDg1XToidX7cSt9yRIIW230axgt0a-V62JZ1kRc0KOKJpAgXD2gMJLMGuVZADdUaWg5fAwmA3xRYrWSCEGqhBs4pXoygsCYRM14uYKyXc4xzp4a9oBgRW2EJs_zGVTFXmUad8Uo3tBssSs2xDYyTnevxRlm2RacTuSQL9if_wuScWZZ5l8nFp2UPkcTZtqQQn1MrooQdWa6F8fc8vS9arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F88QRJ1QMqOAVS95-cxRr6wclXiFKP7S_gXfdTxzuG2ycLwjPhy2wEIDEEqqQpe1_RmVVDxTXyvTt0cZeoQSsyrL9NYJKhEqNDx8saVunzRuj54zk8gnSA1J9893njtykedcPp6iibY9N02ZHMVYw0zKUjOY4kidTx_BLT-2lc2-D0tGaS9YUU2vPXEBE2fVJt8cLMJi1Nvaty_RsWObUystqUcnOew-YaoUC4rLoPgWsqaMXbL7Ja3vM87db5fwHQ-NJc3iqFpR99yuFR34V2TfpHDePT8aFhev1mW5fwZmLZUQGyTUR1zE-MBqo1XMre3bclcRkJ4Z2F0dnscJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHY6Gdj0fpj4kGiUFokKAgcxmPPnR-gYoJJLsMXs8S1qHpxFRSPoyQ6t7dp_s0WkUJLibFxtPjZuxXXhhRpvrMLr0PS53P7J1ob5FijNjN1e26QsY-ayqdcCum6yKJTqBAakpTQmEnTWOGggO-Dx01EUW-nmIr2uDqhpxVlAnBw4vi4d2SLyIQRJHlvsCQnTHT6lt-UifNzq7q5Q_9m_pU0L7TKqG2W-VqR4IQq3_Yb9zq0Tkir9uQfHKPNGYxqb4Wli22PnX5yZcOr9aIiTI3FDjLpE3OPwawVH7aP5LZo0AlHg3CINxpVkyyRd4NI_oTJkKtoznr9QtvPVQ2V65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7Qyn1lIY7rwP5SrpOQbB3VBaMwL5G8JJ6hcW8tFEhSR80UAchRJpZZ6DYq0ORzmVOg7uWXeEAZKnROjHEkVR9KUotmQEmmndQGpzq_hygU5HoH3PYgHAbAbzoDvl9l96vRJWqIfc-T8vKY-vFQ8zqIzIiAWbqsvS4fDbHeDT1OcpAdaMBQpnm0Fx5H0HfUHQ_GznulDHzJM2yjCqRWBerPUtxtLkzvRqrSpG37OhY6m1dKBAT2mspF5_Sk-elfXkqWOWQs46y3DqvTk6z3oiIG4ULCwRy_02umcmq2PnhofKiy0hVn6umoqRNEuU7fEMahZTwsw5ad3viCYCP6dfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVzipsfHHRt_hn2t0yEGiVGU6ed6L9hr5Nj0Olh4Ia624rTktBrYuYFNAauXbbwV_KTiqFnNuCTRhFTJCwS0tyrvb1QGkuPZzEWoHaSOfLnCj8XRwg9N8xCmkg6B_83YEd-rAGOBHUwoOjb3h3Sg9rLwwts-V_knyDY34Os1KQ1gkKGLMKT0cIrXQ3z4ptqRNGrra6p6oTIPlgJVJNj4nrXI0mUDAnz9bFncIrVGebflWKNCHssnTIb6722nwV19hzKAUY7PuP1RqJZbZHtXuygqhfTv3Sbn94n8yOLCmGgn9gAjDl6T16AZRxKTIwWwvVOTXrNaRoQfdHpg7WPFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrh2QgDFKJwBtyKWRRcQscVS5h1p6g9lxgddKGY6JdodoxEwW2qrqMxmMjB86JtcSLEri1lhsxxaJ2cWN0xiZfMAmWFNMpsTCbzpUOGJkXtePBEsxJlLHkDxgwE5h3NvpD2yPQ-t2OYLfP2iRP8iFzfeFNKYKBUTYpD1h5twskaaA7cZI8Pcxgl698fGKaNNqn7OKeXiVBeafnlHzMDD9LCBgZzMccdbjTb8kR-7SWkfWmqCbUyrdyLPIL6qBt8R9AKsFgT3l_IL6xJds2Ymc8FB4h9B-TzJd1MeU_sTUElzqUsAN74bEwJcGdno_8rceeipYmGyhhkuo3KhE9uBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDDUzRF8u7TjzQAdwRdEsnbSWtxCCrFIdI94xvM4JTtc3ywmsmiqG6cpKGCOZow6nNkM3mRcgCvkmla6hz0GkRmE59tuxt4ORvoM6myNE9a4MyeDbtWMgzCUDZAU3mum3glDvfFFLKzNCs8Q_NO5u6FE-YL_n0F4JQnUoigKc54Z03TnQQPvvH9pTgZAocRDr4sg-E_LRUDCvncFC0maQkgacsjpZfmVn4LXj6vAXYE7grZ0gwYru49dS7AFu2IP-tUfclJhMrwuI6_lLmYi2ObOx7kQfblC4hkiwVvTSMswqHfCNjGoRKhpvsTUQCfeVUATt9D9lxuslka4iaJF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCkrHUMBGe7A5yoGOA4_i93k_iuFabL1pgRCzEUe9ZwrAIoFZwx070h8A79_5-cUYUOMzGw3oBH0lIMAATCb7JXTUIFe-AnF7lgzRqWCrKLeDyFEXkbG3wjXRTwEsg1oaYI2ON0263j-ufaCuoKYIWNNPtF2geKhsuqSmDUCdNxuNsCqekNBurdXVD7_WRyhttHyRgN7l2bUNUUsN7DRbJzd4d5rGwwgY4SJ-uKcQHIpyk_Uu8P__EV-o7azt8cZ9DPBq5FvaFMe3kUmdMc0sh7zhr6G8hK28jwyIi3Yc6wLmmKYm1YrS3iI66_2vo7i8K-fqWp__kv5mywOax9Y3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGhxBcZpVtDp5V0QToe4vSANgsH3Dn1t1XUEQjGR-tltyx14BtFiXIqKzDD8HFG-VH3MdB-27dJjj_yh7nOffxtoOdbJ-DogF76T2OsKjqaA91xreTywTfSIIb2dm6OpHgdkU_amY0ukHQVnJ1mWkZRdutyfpzmnSY-tqiidXbazDyEA3B61kOkJWzzf81NUP69XTeeAMZumBFKCG5-uhpeP7cplEJJXH8wU49To8DkwrhtjdB9ED2nt5VMeHTzRz1g5A1YvbYOXuyWNUgdzGDQUT7NeAgErNUh5H9Gz_YD-TmAKmP6ayAZB0XOTcCtY97OH9PXLiVI3K6Na9si6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO2tfO_PuXr3FpFxPCrUR8bw3uQ5ny0uFTRf0JDhtzxALkhybq-pYRwvAavtgLyTWBnA1O2HBcFsEkYy1Zm7zVXwy8etSJvPCZ7i3XCcyWDeol3YUmKOrVCYVAkQpanUAQvYsZ6d1H20-6EjYzl9_RcUjbbKJ9liSDcDf8G3Z7wkmC5FyMzMH7v71n79EDZc3SytBWfC-GWN3INNkou_qucTR1RWTa9FqICqdE1mjefr1ku9fi0p6j6q5CG52EpQe-UjpFKjIESnrE0U-tAZfBU3MNtiHUloeOP1NN68LKYrDQDCnnsuxv8PadEWL6JItX4hO1E1tp1vGFxpHozyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qdyn3cOW1I6Iuyc-7qMCc-uc6N066lGmV22D2_eLRJuzrnKseb8K8WGlk-D-x_cwZcM7FS-X3V6xtoGEhvvnMMzxjwQRGAsukq-aeuUoBBSTCh3KiVEZQdfgvR-SSJGHqFZ-_CUbOVuojkxolGHZuco6LVcahTGoQAnQus7tEk55Al9e3eSmtcQ9FFEHT2V-2HbQbgymGeUzw9SDY0GwueTPZDO2Ph7fFaJufJtS-wAixxA6BaTTBp7ZQs7haHp96Squ8LKdncHdy06-ERVr1LRIKPWUUAzsoc0frKm2fGI6x0UUYn1Xnv3kO0I13_-cS9SZr11TxAD933KzECK_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBK770-dKT2NTBj1i0fimCxV3D5B5cj9V-DfujzB0tbpaGI7BwsLJpru0w-qhlWDMJFWZHThtbrY03nbVFbO6LgSzQirO0JRnXex6eq3A4fw5ro5Np748kIbBlcuejr2xZOYGbx7KPfR0Isd1jeiBRk_YxiZZhRozICcw7G7sJrlp-XVRr3M74biaZLA2RjXGKsco97lXhgMkWxrvColBIjnnXpb-mMk1MbqI7-7S5kFLn234S94bESMI2XrkP6HfNQlz-Ab5F8hqNlmWTWFwtC2O2vMQCWEsVGJxG7HqFoq3WWnE3wFbEv1h4lEV6oNMuSTtx2jhN9WSggvDb4eSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCC8NpXNGWznVPgWIu6CXb1NlG8tRRSc0T1OHNUQDWD_vRFqFWqCR8TYNhSnlub_SwtZUuTBcdHmrLnkowsNUmdGsz6fAcfuqAcwOMhqAlr5bf-uLtmQrgpCbnTgh9_TYDBoLHAObSAcRT7EgdBa1y5EIs3nYxMlZjEczba70hAGSJMJ1_iSKz_L3L5t8EFWJecz1nmJCZjpIstgk8HgmOY5DIvVW3eMJgPSS55qwbK2_SSpGzpVIwY59nBTwpBTqMyr-6dqBDJmNt5yQkAc26AEC-iDKruxcsUqZVi_XRJVEiAKD2whwecEC2TzEwyEAQeHa8dJv3y1zHYYCgAT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXk0Y-CGzc7nGRGW7AlwjKYJa9I4kNGcgzGMRiEiK7Zxc2cQYislOHAbru7mURI_xX0iFNaCsQO5HqLYQKeXIozNQum4zMr0o9A1F1XbtY6JNooRJMf_CUrY-MsU3GGjULoKeD47wQvwn95tiLCeTzZjVoQshtKeaqXImMZUe_1hm7Th-vLMUxAkV-BeuCnYiNlYotrsgWU_6rxQwOW8xMI6lIed4RrDDvxgr12uSdv6-VQ1H00MQi__dOGJJMv7CvLHeunyQlgOespTL6p0jzx6GvOz3zHKbMdB93iUVnJMyQcpoBnC7s2CSOdKidFN5WwkJ_1I6J6xelE-8uxBRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmWhtmw7YU8WDMQ1YgTVFxYuQi6BDtn8_CZJchQs6KzRKPCbh6AUIXB33X-oe3SQSA4CyvK1c5ykK_hjUwGeomziQkwGeEqTaDawrb5NPTAIysfQCxCO3SSMjb5JGLDhasO_lGepTlP5ApqpoIU0mwjcghpWu4fbQHTTsaFpwE0QC9Cy-ddDV-WfhRKmmQn1jC6nRFz8E6JspmNF5dM7urNmre6A5IdSbEh9NtrXH_h6qxR07qpqYC8mF3RWHXXlps9g1iOYYW_il0XkRqG7w6Vz881QTcy3Z_DFhs8LtPt9fEbgKwd_Tl_NcbH_HURByD18NmtAOl4ZBjylzOUlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2NVrqKWFd0FH7BubrFS4H8ji1aHny7KQSlRO3Uzicm98M58EbbpBVxIlRKExMemGY9bEucrNmvL4q1W2q5PvIC-hLIXIwq5AT_kyxHbulA2hstVQY87QidRUre1VyKoJ_Z25mdyJkpBmpsLZEj03fpJqWE2HbinKS9SPLgoeHGfGaphERtkd1tltTv9TahVgbJiTb9PTU0JCHxsWfbExaAIP8YwaaqwLhoC_WNsobXlPp0fneHCRlqWq4B_81V4TYznfvM3zlJIsA1cdMNQcwGdKxpM5ZpcRETETR9jmsu4ohiw2S6ht1aRfoO3jXpx-PyLtn0a7iEh_YJXmIWU3A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=Ryifz-VCeNc9TcQ2ZoaZTxsFZF9guwbi8csda0fOyXvtaTMSEUr2YAVVueS4ZUWtsqtLAbF01H4Ki_pXasAK9Fpi4Y9y9AFasUkCejyHLsXb0ou6wUvNaYbVKGWeXqwkbZwUW4PTI9krBdLO7hLO71qI43KN4kZ89NiUI44kt9qfTh9D5wf5xN5cgDuiEpjGugTi9bPHZQZNHbSCPRx9jLjj27CKtUiPalp_Boqhv0UsXePrqUPu0nQtVq7GN-oZEPIp-MTqXgxXwf4T_h2_Itl52DP-9NHuNl2eqN8pAJa3BZrdqBa6q8W06kDmlNoSSJPRZA7qHFZGZV50mD6SRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=Ryifz-VCeNc9TcQ2ZoaZTxsFZF9guwbi8csda0fOyXvtaTMSEUr2YAVVueS4ZUWtsqtLAbF01H4Ki_pXasAK9Fpi4Y9y9AFasUkCejyHLsXb0ou6wUvNaYbVKGWeXqwkbZwUW4PTI9krBdLO7hLO71qI43KN4kZ89NiUI44kt9qfTh9D5wf5xN5cgDuiEpjGugTi9bPHZQZNHbSCPRx9jLjj27CKtUiPalp_Boqhv0UsXePrqUPu0nQtVq7GN-oZEPIp-MTqXgxXwf4T_h2_Itl52DP-9NHuNl2eqN8pAJa3BZrdqBa6q8W06kDmlNoSSJPRZA7qHFZGZV50mD6SRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCxhcbxTTL1K8j67257WPFOMyWVBcrVBnzxb8Bz4ZnF7neCN16KF6NEx9VWtv4Mxn1uwYP8W5M_j_7x4eQJMdeuSARksh9qWiLaSXOrpAxTn9x3lpLpd-JOFOseLzE0bNazphP-5Lq8VpOUP8BGecyWv-e6bQTaiuq1ZV5OQpHQNOOosWKHuKmm-JPXf9K5jauNMNlskRVWAugppguj6FHM4FjXAiKsrU5XW035StJuhHfRaXIT6N0-1eN3rG6IoBURVU2TzrbDZzM8MClqEuXGHnXaBU15wBABg7Y1302B966kxQtEYCpNWTt7mWkTWL3vLjGrrX813MubPVatX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFUn9Rqz9nYDT4JO-u7kxxDZsiu7CW1Cw3cdkYtubFxG-jdveNOqZC9c9AFZH1uXVrShOno2GgS4r_cBVRoJRO4LDfJrz2BS8lLgTClH9uNMwOvKA6G0_Hr2X_t46mTPd-tLUehSlnQFinT8A3UfgxAmgER6fZYPF_jaE5Mfz6fqP5_eGappuebrtYHzJFGGekaVFwo6xIYyFGBDOW1ECmwZR1x0Mi0K2a7C9j6AlMVgeh1Gi-kpn1hKwp2Tyzd8CkomxNeQsCVngQ0OVJ5J50j7KH_Vskc7yMbe-jYKmP8UuJAKVif6fFMtah3jZXrSs9WzzMPtFsksn05sVTq9V4As" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFUn9Rqz9nYDT4JO-u7kxxDZsiu7CW1Cw3cdkYtubFxG-jdveNOqZC9c9AFZH1uXVrShOno2GgS4r_cBVRoJRO4LDfJrz2BS8lLgTClH9uNMwOvKA6G0_Hr2X_t46mTPd-tLUehSlnQFinT8A3UfgxAmgER6fZYPF_jaE5Mfz6fqP5_eGappuebrtYHzJFGGekaVFwo6xIYyFGBDOW1ECmwZR1x0Mi0K2a7C9j6AlMVgeh1Gi-kpn1hKwp2Tyzd8CkomxNeQsCVngQ0OVJ5J50j7KH_Vskc7yMbe-jYKmP8UuJAKVif6fFMtah3jZXrSs9WzzMPtFsksn05sVTq9V4As" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvU68VoREKjHDnRMAVkcIxDz2OC_DU_T63Nnj3oy1NU_gesEmCpR0jwUfwZh8RzgaByFSia9uSAWehUqAlWSWeDhOsNBZzZZ0BOlw8usKeMShZyqTzF0olykfRzCa8fvxl-rNczonxR5CGd5Zp6vUzYlk61jWzIQbr3rGOJ4d7jgYJjfutK4bpPexyqgNSeX2HXVqSIA3ZFJVQZcB-zsdU-l0ok8g7JuQlP-wxAU7x3avpE430s5DuH30p1MJI_b80n2h5phr2ZUq884dPsittRrB-WSpuSm9H5qqtZmM6SNiB5acreDUKUywHDEorimQuUWUOnpfe4VKLHVN584ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rkk_MeJYUldzfKpV3pTT2K9KqDTcz3En7IYAKpHnTpakCSBtc2VE4Y2w0owEEdtwz9q1MQH0EKTmezxUQ7Z8tb6fqU0DqZtbIh0uNH0EYqpT0cw1EhTfh85rBW92f3zM7SkEv8pFlidmSdWveibnAXOvzeNdjqyNHL6qN4vCWZEsFajRRamdCSkP2aCL-BEWaI4K8saqINub0BPjdi6xiAUVL9re0Xxw9DXQ1Ebx12Cvn1XMc79Ah2G0SxKPpTEhpxf6yspWRigFPo9GosXd79CaRExzB0PUugeYxQWEVhCpqx0zB7wxSHo7n8u7m-KhNFnFNzgXALoWeNYjXXZakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba5FymOdgc8mfR6LOUNGgRx4tH6gg-wSwlSARxhBuk0nZT_TTU7AZ_LlH0Zey1QAXtl1Ak7sq-mvSi4mNM7gKJ6LdeSu0OwzXoF20ZoP5VF4cjw6tjIO-FJxI6txmhLLwxU9ZbO4Ng2wpn1UICrjcXsm9nv6Za3VUw2rAX2WL0M8j-hmad_6fX5nbC0ZcfYn7si9hQ1SXMvQ4nIFqfxTlIFygSUtFp45jR0fLwlUAVKIiffAvnpOHA-LgEX3UlAonIcprLm8NnAxd5v5ZvIC72vlNJFSzZ_4fmE-SdZJwA7XUfN4wj8HuvJgm7d8Zm5-WN0bpu2CiA1S_buOsYqUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLxmjI8a4lDJ1Pty1ffye7cfXPPQ_OtXI0PJc38yCxHl2Ul07gQwrW6BngDjfENc-wEzkNBcQk-RooZiNKIJ5SbXrFSkxNVYsv_m2aPEJ5G3-0UV5VXXMvZIKjpRhVXi2IjL_rsh1IhWBG1lccDyCXYv5xrYVUlf8q9E-DAn0jV2EtSw8QQHuwEM6nzqnfDYE9yRffpCRCAVtvgjX5b3DByVLZGU3Ov14K9gTxPEHANmkCC0j7RCpUCC7Z0V2Wik26B8i4yB01DgGQOYRfTE6qy1tVItS4g8p8bdRNOqR7K0WZ3Kwc601eZconAVHZZjBgP6QdEo9hKaz1UJlKyaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiaXiuYFtO2z5yuOvV56x6yykFBJfbfI20rdDEV2B27OWtUB1eE5d8ayQAdeLoWMXZCSTb3CeCIwGYVKxx4gZX3b791ZqDPVMuDKqT79eEPzfKzXF5b8Fie7OKIj3ER6N8Q8NkpMq_3_IwCQ_ZrGeMu-NwpVqhq_4yBZQVrlLFJ8Ze36ue_oAtXXTG3A7I3We1AqksOFagFGLObUkqphoL_PwwNMDe4zbHCZS6zlrkftNP4avRfpkUrW2EAN3F-h1uq45RqVxJvVjXaMjBHv-AYZRLAtzLSP73YW4Gd4jfN8WEHJmZpLk89yKEsTdLNLFQhIJ50fctY5ufrDY1Y3_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVWHEo8tyIbu_YzcRdCJRGZn7bjwy0DOjHMDw1mBulSZwXt5EKKbKWdOK5KklT-f4M69tcHbjh86vIA7zrxBt9yt9xVSWFtOOx06oNW9sHC54oCVtx6iVHTnXqTQYrhnCQRakYaKqdZXSI9QuKmKFvcTlPUfC8tDD-Lq4qajKZh-aby2-n0s9OtZLNlSQnFn_r97UQFpuWvTTqkcYNyCah8fZJyfcEG3Mcx9_NOXma6ujy37oTffb2wz03LXEk_3G1H0Q7CDyLKDtbZzV1hAKgcKnGpCXfhij5aK4PokPpe3l91rKAGxcLZJ1SgsVOpSu8xC_HhnnGzuSf1OpMz64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXovsv5MDDF4f1oKvNltXyKTlaSAlHrpsb9Eq7lImX8LnWxzAcdT5tzjfZAzKGl9dn1MEhUH-r98AHSCdMWUtLPtIsNLxdbYU4nztsk2erzKggcY9BI0_cl-vru9Z4Xk95S44bIco4UxCXmW-r0EhvZ67Iz4o7-KAgDhW2bkHE7SJ8lmWRet1-S9L6K_KWJDGxZai3GKoOIb5XLuU8mvWhQPE98TQjq1fDuUg_4qtp1N1eNdwR5wbiE3vqgdGlb2PhC6XbxifgLZL9gnC53f1q5n7FPmrHm9pOrdJJIp_vUK0rpGaWI4gj5H5-XPpFDPXH8t2RNHLe-OvEY-zeoIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l4e0a3yInGexFzL6gXZ5AgLq3QIl7mycZf2WrI3E4-gVQ6vfAai5Q35yWxyXjDJxUfjerLFAV_OAJP8tlANubfLaA6v1tgvK65bYYr5ry4hhXYcqw5Qybu9GI_KACmuap8iWC6Ecbp4V_2bm39YoE7r7Bn-NZwwzLczA4yc7aUlt-uLITwhTu5GKfspNndS_k9h7FAffQOE9IZINRD5lOgvhXXwhI-Xf4TWFxlB5wuUJpSzuYyVpZkppCEkuURD1A0FCNUZTrhyq7N5PihTxluykjDH7p6E9RXX-H25igbZ9UDdLoK055CEJgDmlNa3o60iSUa0IkpgEvINVKvWZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApzYmwGK2MEmJ5SkjaXfo4lpvzuSgT5X-wx8V2jhxoWhvg5w52Hs2YLvk1Gy9DNGsAFa7qWpNuqQNboRh5XOXbTkPp7k6EHwo6BQYyE1WO3am_NzcsrHBvnOaCBoNf-yBZR86i0l4tYxfyjGu4LJQj4PRIgc6ONbIapztzLXj6_8Ds-vGQaIslEyruHYnBa83Pq65v1iSKljt2HSRZTZO4VpJO6I7VBblyEbiOLbLR0tiehEErZ3g4bHHgsRZp8oeQf6elkw0Vf3Jp4s3T-IFhdQFaXfzFI9jrLKSrITdPuxTHe_-a39xdUgplTRUJxZEt8oTuhm336VpENtLgQ-9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ws7x8PWuzz1GVEF3F5DKg31vJqAA30-G4fcHEHLjekFMA7oj_7WdIrn4xA0wdZ97zaViACZRtwi1yAYcULnPSzBeKUdGmAoWF_rtiW2jz62EpauwR0tOVVT2g679BiL2V-JQsax7pKGvnCp6EpyzFCSqT1F4Ggb6Rfn-X-fegd0gqxgHeH-513C-aRMChpHVQ6GEAloXo2-JHHuh_N47NuhR1bbq16KEKreV6jGZmO9vWXYjszzrJG1q3aZZpmF-hY25bVEsFZR2sOWc2iHQ6EpzvItk5FJpdsg9YdoXa3RUybXb9jYpp3lh_tzwf1_jZD19KW39Zi5-PfwA746O-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=KEUPnwOVmAS5BJ17pum3bAs5lc7kPzb-pBP3G3VXbvFAr_v51QaIcXUwG1M8IlRPVRNpZUHsu3MFnjgT5sNK1AXrBP1-avvl5LG0OOpyArjozAZUJrpNEW5noWnyR_F7J2rBgroJQKm53hmrArXKYyt4Mm4DAfo826I_04IuGLr2ht3afByX5dIAl7Qa0cN0Xuk-T4dilMc6k578PcsXrIpOfM-rtRdgT6sYNU63SQU3X_A0Ol5JwmwFuEj8248B-06NpYP4NZo6neoPm056XNsdFAhBcgPYzctwqaW9KIfwvLkZ5cf0wIjjf8BjSeJ-U8TKStlNElPFrTdFCbJuyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=KEUPnwOVmAS5BJ17pum3bAs5lc7kPzb-pBP3G3VXbvFAr_v51QaIcXUwG1M8IlRPVRNpZUHsu3MFnjgT5sNK1AXrBP1-avvl5LG0OOpyArjozAZUJrpNEW5noWnyR_F7J2rBgroJQKm53hmrArXKYyt4Mm4DAfo826I_04IuGLr2ht3afByX5dIAl7Qa0cN0Xuk-T4dilMc6k578PcsXrIpOfM-rtRdgT6sYNU63SQU3X_A0Ol5JwmwFuEj8248B-06NpYP4NZo6neoPm056XNsdFAhBcgPYzctwqaW9KIfwvLkZ5cf0wIjjf8BjSeJ-U8TKStlNElPFrTdFCbJuyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0CkRb09hKlOunc-zRN83VPkeujoffNUbhy-Cq_2VCsJUJhstjuKwTOs-VO5gECAEMbaxDTYCmxuw9zzQKl8QxFhUiFxbNudsOVS-sSiHWgLh8RmZJP4qzGk8-DaLUEvTEF6InaDx1CNN3vNFSRcDKEOZ5Z9_PAcEknhzfePSK4aA0xvxZi86FmySalVCVqTpXFpIU2_9Bivn5_Q7D2Fn3lpHQ29GG7WKPqGnYyY02jS1qouQdhvOn1ieZ8-72Ri9Oun-UFmEvaXvWKWqDZvDR5PKN0E3BvPy5zeq15M5NAeJet6h4kCVAZP-GoqwKU_UKqhH91B9TfJ-nEB7QxySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ-BzjBWYsNM0J7Ox9O3LbVeD-1zWspW3xbGWaWYIu-0HAqoc_G-t3guavcjgrf_bhSj-y7v673hVR_kUJlJG5HCMUDC7NCZjIxHa9hzRXrYekfM9l47t_4MaMD8hdBJtMylGOALDqDdYBCWYDq0bqSOk5qv2wbKeLXAaa80atmnj79NBkC9DAEByuqraKGxRq-gZZZMBByFk_oIV2iQO399vRWoQxWndLuR0btQrmPM_VgNgiigjQXvs0Y3cLbPqskAIzDaTVqi7rlRm7k1PYBYEwcuJINTmeV3SJYC0ZgxGiN2mzkiiJA8MZ3VAXWn5SjHrb40SWyodr4j7fmZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzGOVt2WCAhYD9JGwOm6lAZ5jdTfIGYjqNwwRhTN6QVvC-1fZJOpnPZYf6iHMb-zAbKjl1jFBjyUzP5TXOY78V6vDWyOKCQn2LYVnAAJVy5GbLgIle9eKGNbRVuDqKtMpDFZHOJN0cb30XMYGCzTayWfTmHLgVBGwUEpXpsvxLqdujjSUl848JcVd4kb9EbygupRyH5upgy93oc3rTFQZhCOO1BQZwBfSagbZXkJcWfRX1Sje1kBA3xZlFaTE1X-MXeAwnl5rA2MkSkc5KTiN_uuAWS2XFkJWGtua2VpXgGbeY1PHsp3LFWTS6oB5HmQcbNxda32q9FGeHkPLT_-4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tksg9OANS5clm83Wl0gN1xyy56tx7aZ5bFVjClyJXFJF_ar8miVVSCSuQ9jRE-ZG3hRGvA5buPkrJS2tYyl3iD3SFHN5k_2VEK71aYK7AtIJ1wUK_2x5u9M2FvLoLRneqcEEx_yN3qzt9w6QHAydeQTuUHyndLSmIk5K6vYhh_iGE3J-7XfwfsY9RKUhYeV0KzP_2Wsa8CkNd7ldxgglqaXWcLnpv4SxDS5FXbGUQ60ltMVTkBO066vzneqDq35JaGrHaUovCSMIuMmGEq59n8OG7q6m5aeTFP_fkCvDHFNkvh6-PrY0RV9ZhAWGUs7s8Kdp7YCLzoEla-XcqPqd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4MZS9wx58Gmgseu1knNl84ZIZXCwjLU-23TTBGc6nfDkLp5gecwBmuCUrU03nQE9L_Qb1PzT8lfQHNoVCFzueNZNhGFMAnnrtGKIJCLOXHnzKZjI5iNEBQs0KS_l7CueI-f2hbdRvPtpHfMhkx0bj9BXAP1TcTn52AlnlW3gbpX9VrREwQXRtFcO6jWezfZaHVKNKO8fZmz2xE-u152IRENMGf6ACLcwW2aSux-PN5dH019OefyHlXpLiN8vZw8nvnyFZYsxdznNNk6iLz5iTz0xRxTepuRPXFBP69_LlwjAndmsl3RsAM1UYuNh9S3tNOQvH_2bZjh6qCHAMM0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdEdReZHEbUSgVWuzni9o8Id8C7yfguYJcj46LQZK_Wz1vGSAT9yRPzQjHrdKN1Z0ivSWBHRU9bj7ETQ5m6zjYyDWjLyto1JuOTtG1Eh3WLKwa4lg73GlJtnNv3BshAn-tgvdE8iiWqfdUN2vGv4Fb8wg0FMiXHeGlUrwdVwbB6U2dhm3gMVZPjn9NaVpoEG3sko0vzPAOUDTdwRRCDvFWnaW3ZTuu_wHnMJRk3BnN8NSzkRzAI_y7XMeSwoknCD2Ey_V5QUpOZLP-cWl1J_eVrFeqd3HDBZ2Qmk1HMicS5IAgIXTdZdLgMlEvgk-IkpyaK_FGzGXCSBFD1XM9DTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2rEu0bBlGPbdHaGcxwmEl4dh697f6UBgTzZYnmu-6qQIH59UjDe3F85tNvlnAEwb0-CnMtX4R3yYjQY6d7GRcQC2Q-fiH3NyybQNaDBQZOhYHX7gss_dhYB9RZQKf3na5G72x1OQMz_m9uuoSrOrSJ4gK3EVAHXFM9gxqUvzaVHAP73Lft04HpdKiFFAv0zqh3nbgH_xNIr8RIzcjJlMDfgjTQYBSGvrbNnsqj_jjhx_6rGRi4oRj25Ieb_SMdyx3v9Sv69fbS7O37zSrVGaFDOEiVZFDENbK8TPTSSQnD7vJc0o6t-OxOfhan870pYzZTUwb52vtX5CqVE8MyrsQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=pCLZy5yyNFYgmoKvj9jPQlc1trYk_53oPL9OIQgDvwt4kY76nfe2wLw9ODZxzvg-I-o5KIfWKxCfSE8csdnC4VhTwkQA3aXJpW6LfD-XWqNCVP7E79JpWuyreZ8ATznQg8zXnHRrRaFCgIHv6wXdsW7FGRxqWY9Oqfw9mvhr0_MTfn0qC8MK37KrvefNSxCqx06rqwV4QiByXopjrFzMw9Ad5eD8h95tEkbPlczs6B7FcaOqw1JZ9bJ3ZPglzYKOntvftEzWSyjSL5Js-4I1FMWGLaxaFai2IqGv3xi39-Tw_aKlK7TgDbfbU_YzDzQV-6dKSeqYpRAVkuLHW2TkNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=pCLZy5yyNFYgmoKvj9jPQlc1trYk_53oPL9OIQgDvwt4kY76nfe2wLw9ODZxzvg-I-o5KIfWKxCfSE8csdnC4VhTwkQA3aXJpW6LfD-XWqNCVP7E79JpWuyreZ8ATznQg8zXnHRrRaFCgIHv6wXdsW7FGRxqWY9Oqfw9mvhr0_MTfn0qC8MK37KrvefNSxCqx06rqwV4QiByXopjrFzMw9Ad5eD8h95tEkbPlczs6B7FcaOqw1JZ9bJ3ZPglzYKOntvftEzWSyjSL5Js-4I1FMWGLaxaFai2IqGv3xi39-Tw_aKlK7TgDbfbU_YzDzQV-6dKSeqYpRAVkuLHW2TkNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=trXKdW3TVQ6QRuHjo6DFj_akSHbAUFEJNdr6INvnKzLGlIS6owFzLM3N14P-4bzf9TFvWyElvZIivIkFseAMibCF-YAf74qYgpOKPSrtDeRFMezt_7YNxAVtax6RMntxp6AA-51y_SlCGf4L3V5Ws8MwTPzrByItvPnWIsSO7zfySB5BcRNPNsSOqWkpmc1HULtsKq0faRM5KNH_eHsYPaSB44EVvxWH-qvpHjGt0gyyxsy0pv3w_4btapJzqgc-YIAyxmCV3Yc-PpM-sFsGF_k4XyzHI7N_m8D3zUQ7HwlE1vy1PTwF8vryb1Ls-71bK7SgslDDCMgmAbZ1-9ZcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=trXKdW3TVQ6QRuHjo6DFj_akSHbAUFEJNdr6INvnKzLGlIS6owFzLM3N14P-4bzf9TFvWyElvZIivIkFseAMibCF-YAf74qYgpOKPSrtDeRFMezt_7YNxAVtax6RMntxp6AA-51y_SlCGf4L3V5Ws8MwTPzrByItvPnWIsSO7zfySB5BcRNPNsSOqWkpmc1HULtsKq0faRM5KNH_eHsYPaSB44EVvxWH-qvpHjGt0gyyxsy0pv3w_4btapJzqgc-YIAyxmCV3Yc-PpM-sFsGF_k4XyzHI7N_m8D3zUQ7HwlE1vy1PTwF8vryb1Ls-71bK7SgslDDCMgmAbZ1-9ZcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEYB4sAvLVuaN31AaC72CblFVd9THRETZsZbqoPrjvi-96qD58x1kJgkejtCBR4oyQ4vtTpFVPrEypgyIIdk7EawSO-zy9gbeEhH0uoOliMh3v8oPujC_8sFB_CUoCrzjoVsuNll-1GJv2D3lKHFEJIi6-GQxdw4am6fJCrortwYECkt75K5Fgk-fZ7FcXREGTFE594kYPKzBYTaXUOBgxlVvu94ihOfmWBb2Cv9RFeUTaXZnjqrn9qN30H3NZvAxDyaNEABoMT17OtSjxa7Z8UrqzGwDl_eiG4oTKtPT7sHfMaedvEJfaH5t5cuI8ORh-2kYxt28re7mmCTtfSWig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWxb3OOlgro1GRAuqih0y-rfTq8dZr9UIdr1RN5Mn3ExwxMsU_XOX9OW5NHHjGO3RMva1t3ZwloA80WT7lPpOUV3Mu3LC4p2vjMHgm-qG0gQd9gzTXuo8SogEGz2YBhPDYHuRC6QGAMHRQm502pYETb-4gcy6VpUiMJjU0VoYf789J0WpmJ68CH6qeistZKlfD9Rr2-2H53d2GaC_3Do1ejuXoeGra9Am2BAYITHJYstmvfJTE1_C6uc4uSlvN4r8I5tYlKlJC7Kk91e6_PtuI39U0pG4ni4VzHOJosUkfEzhVkleA_y4eAoryA1qkeOsfXt1o6RhhiSXYgp4xAI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7xCjy5yMOsshyWkCw3xg7dRQaRRq985cfGfv12YUK5ULPxCmU5-_CIpvnyLJEgnUgDvVdGyZxYSUuUnJZeZG1JqoGI0ydCEfr0PABwVpMzchzZ9GHQxVeYEMwM36Sw5YKg6QgoZjR72q-mn67tYxNXRFANdaFUAswiuoYywtYXOTYszHzCx0e2znuBf5uLZ-WHkqsOePoWeCepXVaDPTVwRgs3s4YG3ilKYPBJFFlUGUrT-lnCyNpJQYwWCuQ8XG68RQS0PkodwnG-6Hu9VO_eFDtMoeRVO0MQkaBQpNPZl9S9lSYffC-ZVoJ82objkJYvdJwLjNjQ_KygsM9-tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOZXv1yn3Ef2_8zbqmh_-TUFXKIpBgAvg0HRiJqWlUja4OzC-9raFwWcT5PoLbi48txonfIeb-kujun2oC7hNobH6dnRB3sHPL2HEwSnlfMBrjIo7HFzaQbY2LYKrEe6SAS6uyQo4IJa8O-vhYi8gt8u4qtYCqdjRdU5K7TROk-ythItyLJgiUhAJT46GYm6xTzxh7sb2UaVrlV7k7aDGyimlx2bYqN6-LMVXL3w7wvuk5RVEN5UZNSfACfIkMXjqk3XF4_eoNw8K7A6D-IRksXNsY7S6IhYlRf75GUuKNX4bQkb0QO-hsvoy9fV9surTR2KnhVt3c1_xMfk2cFk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8tuWJCNGZsC9Veg-5XHnErigIowV808V5JmTTz0yCqlLYzUZKZqKnwrgLOXQ2_Lk0HsYxb6XKl6EjrB8YQpUPdlJMAktJDl4Bcxpx4fs7vtnTuLFa4eL-JSZvuEJ3MNzXiq9V8EdmKkcFrJg3_VpPYc5mjK4vxvbxQuTSI7b3MY-pr_rhpUFIrCKj0LiGeZ1MBwZuEQ9mZUMHIs5U3ZxzNfT7tCgHAlK1pZ-OHnUSE65coE_Ix8GBhQ4mKl6T44pPpQYTy0CmFK7UHF8RPB64kWpG7czIlnW09ij6MeIZn5A5yhGfV9g0SrBffu2xhtBgBTjzfBJLderkQAmEE0Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=gNJHilzmV12i-90iaUtdCAdbeuXrcc0rhgMx6CzDWfI_Y4XjCE6WBQ9_Nn9FOogEb_dPKBsdg3kVbFLoQG4Cff6YwI079wEkc7VW5wvzUwvwcvBtCIWladnDKxD7IRpzJFprP722eZi4Y-n7-oD8-4Qrn0X9L6KIh-5IkTvfiABRW8RXAunbZ5TNqs5g7kIA6ddec6Z1sDffmDuTdMdg1go3koUxaLuIVvVA-7w9pxTAe4IehB-eNeq8I5yJyARXNQYATBqRqC91Qqh99GUSx9cAwgHZftfwfRY02n6PpWkJz0bbHU99QGQo9VsKYkoog6nYob9_JxiYjnUYByKNkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=gNJHilzmV12i-90iaUtdCAdbeuXrcc0rhgMx6CzDWfI_Y4XjCE6WBQ9_Nn9FOogEb_dPKBsdg3kVbFLoQG4Cff6YwI079wEkc7VW5wvzUwvwcvBtCIWladnDKxD7IRpzJFprP722eZi4Y-n7-oD8-4Qrn0X9L6KIh-5IkTvfiABRW8RXAunbZ5TNqs5g7kIA6ddec6Z1sDffmDuTdMdg1go3koUxaLuIVvVA-7w9pxTAe4IehB-eNeq8I5yJyARXNQYATBqRqC91Qqh99GUSx9cAwgHZftfwfRY02n6PpWkJz0bbHU99QGQo9VsKYkoog6nYob9_JxiYjnUYByKNkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLTXYBxOR-uuVgd72OLI-2FE2SsmabKrAQSw02vpi-z6v2yKPgi0KwI4OTCD_QM4-vGZC8epcKeeHbYD_3Nj-jmku5Ahy8H7CwJA3zYbxF7r9yMAwWbDe9vqLv9cG1EXbVeCoJHOvj386HpemT5tDylcF1OJqjWWFUrw5z5AhVzZYdV4K_VS7Aw9PGVBLy7T4j3L-HrBoHQhej2yhHFgVebtxsmO3c1v50YVMR-bKYk_tEiJE5udMwLYr19AO2-4tgbxefsuMt8hFg4Gg0LtPVEeOCwefWvWBUwh7zt5ru-N4Q6iBX1F5YzC0IFuJM5T2vxS5b5vOHjcaWQHkKW-ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4a3HLEEFFrSsIEESch3SYXfvmFz36JW8G26eMmAON93eorVfBL15XSYZMl1JMRPwFuuANL2jakrYouXO0es-pfwsJDJ84olIWNNPO406lcNTGP1kVB4ffJzQEmy69nnIidUqd6X3QQOu0MIx4t3OtWBNGJ-RzYB4cgP7qhKkKIRJR_4ykBP7r2BgNeLE2KO1j0e350sckqgQcMlknAscuAdimNMGhF7ZLuJd13rsGxcC-pejZPs0UXZb6J26MVy3xfDzSJPS0ZE9I3JYBtmb-0cONeiZiGKgMnbw27Fv8RmZpaViirCXzfUJG2Az9FiBO-ISHjgsaWqHg_A5hIR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rscr3vkvknOxFRxsGC6TcbSRBst5gjsjCdbMNWl_LtFTGwo46r_Bxr02Z0UUErXbqKobpbSYagiWi17Q6OyIc2Zx0vGW0GxgwzjVArY7XD_i9o3CEGM9os2gOd67V06vLmxsKryH_xeROz_XvXFlYqprFrTPGUvmYWi2uOgnUbA55SFO1mB_rI-4WlEycxLLHUWS2VfUhkhZ4gNP-IgYha2ZfOPOjyGU8fPK6qMp510X89_SokQxbo577KzPYQG027SLROKEdhoIcLFuKTrek461a9ZCycNtybPh9EOBsINBRxdp7pbPIheTjiqcFF1jymIZh3K6cJZsY7-sXNzTzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgRmrpDR-jyVFlCKpbmWUuSeJ_vdFsYJrkXPXc4zYaMk2rdjI__L3EcFWaxJ5QtBEJcYMgJVqRHwCk48TbzXQTZWhbA6Nd8jgV0FWJKY8p56YUwhnSE_k648JCrjXKIWkTWt3QfemPtEG0lmt12fH845WIIppboEtwdzoHFQRPgnis8XPHZRor5CU6FTrxnklz3NzYncA34KGI4YetzDj7oooDcn9gcBlQvPtBBTxNOb-9CROIZn80uYiwka_wKdA_Zk-uStbAOM8f_X2xCcVJYJEXMrnOxVFTyr_A53SWRo3cd1s7voA8veh-__ki_YxoMikpMKj7hj7OtMo9wZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiXPvlruyzN-VbmQRTsQSBZesvepbKEyOwo0cul5v7WmhR9RRvKoVPa3HQwDZazWuh1-bZF_UDnNZTGbimQIOMqBOr6zyO3B7nlv7Pg5qEXQlLraLUcPrbUJZsfqxsQsMeSg5UxsX23M7sNI8kNfsgyPwpVSm9UD5zkgzh2-W7UjTgWOfq8j6XdZPGLIi5S133vIfMMDpYlE7pvjNj4HpEZCXvkl81MoCJ940C_buFOH0BhyR6DewNBcYiwhS4xtGVEwsGm8ZaRebYndzEKKISwVlkNalNMpyX8LteZcWtEC7aIPTGd3KRNVDODSvdA2O0Kcr6c4-jYxAUelOACaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-uZwXViqh_loL8TCbwwSst_WDze3sVRbRo_yY9U4y1LPUJj0IJIvLazwAMbfA48yncjix8jCUu1a6Ouk_ilEjBc1ptpoN2ZS9TR9Oo4can2_brz0I2cHPSqjkxpb8EQpzbR5n8r_y9ehPyV57km7AKfMNXbl3Dk5BYVmZIEyEzpQddEP_X26uFny6YxsThhMVrjv49ELJLFmuN3tS786GApg-3a9Ubcpq72z1BoM27w2l4uqimt2NrciA7_JBrRWs7auj0bFoSqRbvoTS4afl3IWhnnsLyUAt95eKUHC2cPE-hQlTEgkmJW8OhemW_6HZcDicjG0LIaHwHv4927EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2D1DhVKl5OqIZcGj70PKyFAhgVyP6hb1ZQPuEGIMaDMa73C5kma-0-ijPEyxaaN8MtDzGQKZDXa86dJGoqdfwelhYyUlJUU-Xvl42iTbRAlXY6t3HxJdIlM4SwdGN8drgSMlF6u3XmLvcB40svHMpwQtbP3L5PaxioJI_rEDo6tkNaJjzUwG4jbpAMa9brHibMPQGDeVEr6YrGw8GK-6TrNQmayQDD0ZLCjjkSbtG1DWyZx569v3AafZ8B3SMQ-zWcbTSyZk8_Sx-TVAvqz-K1LZaGzyWwGdUohIhOemy3YEGYev-kYIJWgYirwmwHqJ7Yu3cGnkBbAW1l9uJBaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9DFPlzpXQ2DmEE5D_sKw-dtnBfNY9scDZWX6fj8zbG1pPOAOGA9d_SQ2eTUNTTozjpZLGlBzRQ8l4oUSNXFE9dAhNuRgDnwY1bHFPXCfJ5hfOlA408ImzXvfOCKMEkCWkydAUy2eO0-0jNI1Dl3_El8arpxeS-QLrO3PITqbDVsltFb9W1nGWWYKjgymDgEWhvd9ngLCqWzsGZagL2UMIqnIAxluQum3-YcEHxw8UmBdl1sTswb4OP7N1a7krJAYMWMyVJOZhsDiRwkoSehSZnRIP-SJt8HwrgVSh74k8lA7k8r35G57mkiXnShOTiJCP4-kV-4PstO_-SeRLkSog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCCeUVEZslWFVCwoBzb5W-RLsbC-snHf9MspAG7NJggeM69nb44DGVXkZ_-HCz7hZaRAAng57ZGqzrNv9a7xjOsgcV6rn57v9afEZ9siNb4peM98xOtQM3Cpi16olN0GtIackE6tiADQBcfj6BVbsS7jmYCSTwlHEHRVCqE7fe-Pf-WPZCggwAt0xuqoh1EqJfH_EUslcVSKXWZRmQUKZDoiaG8EoB4UzQhkOM1eW8uQceI6e8tcF_dMhdOVjD8bKM2Ur2S0yQ7WfI_2VKasPIclkO9yWp6nGprN3VD3yFK88T1hP-2kcLI_fvLLC8Nv6muEMsg0kfH4IkpaSW32WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmGjMdJMwAZTkAnzAwo6BMp9H7WGjpLcoNuD7niA_Kjks3rxDrnakCPa_yoh2aFJ60St6FvGcYFwdSkvxh4r7j_NAekgc4M1JcmJoNGj0i86wp67QAn6TBi3QXimaoI1zydvsktf_lV8_IxEgmLgeA5vZFmtlGrOFf5MEya_sVMKv7KyB_ungolZnW1gcvTPDfLfVspx6fTjB8wpioYwGCezF-3f04YWCeANg65Qie-x9b20-E3NzZS9GKngTiYVU24METv6BOfZk4qQHUnRiJO21BwJHHm8kFt-MtfAON6rgxok_CtKlm2WF6NsSQhLOeJEDm8hpQfPguTNqp_Djw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=U7qq_KZgj1zUGvgjvEHS2Bu4tLbbIoV2Xcj_WgqxyuY5STpUgu2w7SVhz4piDUrxZEMcZ4u_rtdeLQnS7tGtpZv-5W8NP62S76Tt30jHMo1ZkHg8dijOjI8KABM93r6NpcXLEE4iGO06HeuZ69g-FajIb9lzmhWW3SyqHzIb8_So_sVikCDZ7KjFptNeXtSkVXS0mvj-DvGhrH6JY6StFlOG2dA8vFr8H_8NW5e-ZaR5aYTEYUxOmjyuPwynxHwNUNXXOGbsg6529a8l3vlmCDJlfbQGsjc9JEOxX9t2TgopkEBejHNxUJt6QwJ2K-gkbOFiXQX02goOro-3Y2EH6KnG1sGg7PggX2vXdAex0HWo-mkwq2o_MvCIcyi8S9iiiYWEixJ6aT6SV7tGnHjfzWu_S_jzkLMqG2ulc45cnYwsRsca7e7hdVRHXbMCunXX04bp3YORD1xTjpuBwYuHm-wDpEGtFeCjug7q4vv252vXbqrvsZYm_HGR-8PcHRy8eWLuotknQZT1l8qH5iyLPQY_EMzCFBXT3F7tG9VvfFA8859eUsQbI8SDlfKoPtXakhipUcCmBaWJ_SOsW3WHAKNccjF5XGB7xqML1-Wmf4lZUch7jL18SMWeSLPU_HYYzQlpZjUGtnQdby76mdeg_C01G2Lt8_pA0Xl-8hFvI10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=U7qq_KZgj1zUGvgjvEHS2Bu4tLbbIoV2Xcj_WgqxyuY5STpUgu2w7SVhz4piDUrxZEMcZ4u_rtdeLQnS7tGtpZv-5W8NP62S76Tt30jHMo1ZkHg8dijOjI8KABM93r6NpcXLEE4iGO06HeuZ69g-FajIb9lzmhWW3SyqHzIb8_So_sVikCDZ7KjFptNeXtSkVXS0mvj-DvGhrH6JY6StFlOG2dA8vFr8H_8NW5e-ZaR5aYTEYUxOmjyuPwynxHwNUNXXOGbsg6529a8l3vlmCDJlfbQGsjc9JEOxX9t2TgopkEBejHNxUJt6QwJ2K-gkbOFiXQX02goOro-3Y2EH6KnG1sGg7PggX2vXdAex0HWo-mkwq2o_MvCIcyi8S9iiiYWEixJ6aT6SV7tGnHjfzWu_S_jzkLMqG2ulc45cnYwsRsca7e7hdVRHXbMCunXX04bp3YORD1xTjpuBwYuHm-wDpEGtFeCjug7q4vv252vXbqrvsZYm_HGR-8PcHRy8eWLuotknQZT1l8qH5iyLPQY_EMzCFBXT3F7tG9VvfFA8859eUsQbI8SDlfKoPtXakhipUcCmBaWJ_SOsW3WHAKNccjF5XGB7xqML1-Wmf4lZUch7jL18SMWeSLPU_HYYzQlpZjUGtnQdby76mdeg_C01G2Lt8_pA0Xl-8hFvI10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJjDPWSqvkljU0DG7RcQXIoqLI6bwwcemZMy68Z3oHBIL3l0BQ3JTBfpLD7jSSaOMHcpOArDL_7UknWj9C2Vb-Y9pTBjFv78UavFa1Wp8rYyJBGW9Z6MUExfoxan9iFWjLKngIR_sMXLx2NHjj84QNEol-v54-SChQWKUKcwWuxN8PvI3Fq3Y7yIIWfIIf-M5qL9VBCZZ21v2DiMAd0utt88rLBHcSoL_qBS1HsCcyEya6m1DdEBjqmB8GhyNPsUyYK_W_xfcWqPA6eTORfHRTomLekqwkyG_yeeIm9nv6WXhEq4lIjWisbt6uKaQgFZ32qUZO58SqzqQrPlBQAn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpWhnOmc7H1i8L7qIbXDA37VB2vFHXLpZqStfAw_yr9l7DFieP3CUB5cBBBtsmkE-ELNsajbJmBk2UZWzPKh6gQ85KkwBnUiM54VaPcZIZfvYLfZOGOzTxSfbepgnqK1iCeQhtYNd4MGZc6Lv5mduzOolXFi-9O3XU4rY_2QYvbt4pl0qOSGLGbddCwZrQSmWsM0W_l95NjzNp1LY5jh9XHjcHt72ju16AfeUbDy6hqUfropPQ5hHKMEXc9nO2PIfyuNHfbzgm1Xt_voFGVNA9bytxrfHg2HpECXxWvXI3ed54KHo0Jlur6W1W_BO5BxgGqxE0jhobuBO9wQLqgJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQbaTwn2mRhDMiynH3rqty0XOFVEzyzXgKQrtLpNt98qUvPu2YinZR5pkqCFTwe9eXGlFqcj6pfBEAZF4MtzF9LrSX7DcL4KO6RDIFmSXH3GMiSclMOeBKOiis2FQy1t-FtDmoGFN04MCcceNDBcNJBbNJPCwyUIQoMEWD00r0cnhvdXJdZfBQqqeDyV51fZd5_qm4H7v5eEhVpLzBIOf4qKAbkLMDSYeHe-xV39wjRRmQB3AkrcL2BgeuVbhSJhh21JAtyydlNp5sJvK0pCsRW2LOcqTlSC6dFa44KrLU4td131JCCgfVDtUxPU-R1MXvPAXYZeoNIq89y-pHkWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKTfEDmvtrRlfqib5GD48CYKlGxrCfHt0Mx0ktjvq9_IoGxfXdgGdhrQn4FQkgcDOntjNPtvH0eYewtS9dBWO4H41Scl5dHyWUqAGNbndB9e5EYfhoZ0o2BAydkmvj6WyzyDoUgNTU3QPY1k__lCgpD6onurMWSxGJTon3-PJ7r0DHeMT1d2ED4OaTeGrlKRaivDGsDFTxslN6AdRjI-uocauqxxkjMFCaEc7Cs1vUURfON6AURyUFlQaumoUfDcF7xODgP-dd4DKe2PkiQJPemmq2pHmNsPRSkRD6eDEZuf1e__m58nNwNtsv6SiAsyZDvdr-8FbXHpX44RHPHivA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZby4PF_Z1QcEmFHDvsxY-Nv0Rqgm_tZLQpQDk-sNgLZiUMPitPsLOJgJopUKB3Rsu4yA-EBMuaOxVIPutKJJER5MLJmUjy7pCC6XY115B-vWQ78KEsySOL3NrnRzZTigZ_l0QEhxrtwomDMoCqsUuZ5L2Xic7gNwEfLQrKYgCj2BAV8RF30ZY4OPtAXa26ZLhNg9u-RsDPZJybosxSZeQHDDXmRNNWDJ54zYYcm966coLF-O4POvGCj9_KHDvt6RbdoxUFkXm_84g6jvmIdix7ESvhZa0hY64A-iCONuDAq5_WYulOyaMb3UmUKFibGIlIjyUPUsqRQ52QnUS-ChA.jpg" alt="photo" loading="lazy"/></div>
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
