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
<img src="https://cdn4.telesco.pe/file/s73OxbUgeHhi1hI_EkwWq0sheupmSsFPzMJFr_VHlblDHjfbXrUnOUkjYV2F84nlJ7VFlBe36B4vTAYqGy4QpgGQYyXB7vPIj-xYUe6VnBy36gd_-QcNl3urG-Sb1u-SRESqNQ-wC8K47YrQVpLkFmtr1mc8RGf9Koz-LH0MRAdgH3r4nemyS0FJeC6491y4Yy8N5yjJbftemyxJaSfb87fERfAKJhKtBUtaHzWmMJcJPSgCyKJU_kp1V6km_9FLe4MJ_tFwE3GAX5IB67a368NeDXBTp1e10Zq1g4yaxtI-AM7nBQcue5856jPjuK5f72o_4sfA-blKZdtahM_3aA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMoTuyRKyBcD6uqJHj4buXqvV1pgVMZgYi6E1Qrptgpw6o9gc37cp8LApYgx75akWQafNZysjsFskUoDAZ2P2G-k-MT9fU9MEJSqpMsSC3b1acKj2cdZa7KN4IlFbaWDR4tSoNQiRCGfjMK6Ji2TRiVqV9to5nzf5zfA5zB6Jzvdjeon7wzZwYmaZ8TEdM4zYxkMOxxu19dcy6w_k0LiVJlajKVgiEjWLQurxfz4tIIG5Q7EiVzZEGSwLpW8uO8gaiq69GmShVnokUfWmUz0PoTqnZsS2AtDB-4c3ha4OzSmK8eCAsxDzjdAqruOuN7QAfRLEYKNS56CzqOawxSj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYYwozUOeLOMy2N-HUzHnUK_e5gFDWj-LxB1qbR6YkZk_ONJEu1d25K-78mE53VazS6lxpbDxPNyCkbdgpmKZPtKxGWNg3B1YZbYpk3gqCOZSffPNKTyyaSmOHR-_ggvCM6-zN0I3ZCyY1FwftTMCekU5Ek-FBeFiGYqphYQePEKsSjwjBDOqFZj4M2-IGXTcommlU6-9zTKPWeegekjvqTSAQWwkZCYKLgM-sKyaO2ev6uT4XwCuYDUTIpUxnpz79zgMjFBRbmX49sIu_65E2x2I0yc0fEcqpS1BldamOTy_bxrYSx841c_6dkSyeYKtsjM7axEvpSSlCJ71Fz5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnzoBQJjggwwzC54ao9K9eKFp0WEzVgAUEO2CuvHO2Gw8IUjH_38CJ7CK3CDrxHRnuWOYx0A4KIMHIbDdlbwS1aeEVXN3WUE9wiFf32n7Ss1Tb_H1JEqaj6VxWXLl8rGHSY0Ejnw8LH_tUatkjzIedTFgmaHhBCrIWxI2Dycv5PWz12e-OMSjNDMnIbggPwY_OK3O2kOFn73Ib6WAVZeyIyOuaccwcvNIGr6Oiaej9lVvK6HyIWUo06I5N0g8A_MuZSyWeKunH8zogcrnjendEMZWaAfjs2XGujr-Ttg27hSGZqHOPaZ4jejXVPjPYjd-NIXv27uSSxJNtAiwog8gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGpZTNHoFG2CNhnDocSOvzZN_sMoL_WXwjmPChQ7aN2aMwoQyyWv1Wj_aLH90bp0_nmuqPbzH6kpJvwVSOjOX0mL3NTr2klHSOM1-jsFV0fMVQhoulrmxqZnfF7d01qvIxaxEkKFt35GoqbzGSjHSM3gnjsAUXa62I40lEXX4AX2JoXit7Q4-Kr0S-TZXTKZlFQdP5nbmjzXHk29iof_b3Jep92rFdyJwzuBkePn_U0EAHPabp_Lf2sm4V9gZBqQK4EB3p7CvQlMfL_pn8Q6wGBt7zPDPx7zmjNqNBkj7ARuxPvcfJYwu_SPS4qRjPE2EcWW9A0gvgE3retMUn24yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو دشمن اصلی ایران
این‌نقشه، راهنما و توضیحاتش امروز یکم‌ تیرماه(۲۲ ژوئن)‌ از یک کانال تلگرامی نظامی اخذ شده است. بر نقشه و راهنما متمرکز شوید:
"کوریدور خیانت؛ تمام حملات هوایی به تهران و حومه، از این مسیر و به طور روزانه انجام میشه... آذربایجان، ترکیه"
کاملا درست ترسیم کرده و نوشته است. باور کنید در جنگ‌های ۱۲ روزه و ۳۹ روزه، تقریبا هر شب و روز‌جنگنده ها از بالای سر من میان البرز می گذشتند.
ولی این کمترین سزای حکومتی است که حاضر به گوش دل دادن به پژوهش های بیطرفانه نیست.
بیش از ۲۵ سال پیش، پژوهش های طولانی مدت و استراتژیکم طی دو جلد کتاب با عناوین: مقدمه ای بر ایران و همسایگان (منابع تنش و تهدید) و کتاب: مقدمه ای بر تقسیمات کشوری(ج یکم)‌ منتش شد . کتاب هایی که نه تنها سرداران آن را خواندند، بلکه مقدمه ای شدند برای اجرای پروژه اطلس استراتژیک ایران. پروژه ای که بارها برای سرداران فیروزابادی‌، شمخانی، باقری، سلامی و ...سرلشگران زنده گزارش شد.
میدانید چکیده کتاب ایران و همسایگان چیست:
دو دشمن پابرجا و اصلی ایران ترکیه و جمهوری آدربایجان هستند.
ولی کو گوش،شنوا.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/17913" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jthiFr4yO3qwEZrcjxDoF4e8CDRvCEvBt9vxYKSVMDmiyY_FzmGqdvRII4i6l2ajYurdEGuWJJP7I676stfoII1d5DE4dPVnxrQPgzSV8gHve-lx2nFt-Sg_JMGnPsIZLnwPRiFp_ij7bInzxVMmGj7LBMfDjkYZOaERT83_fvh0rcCCePUL-F-CfeFO5GoKeh7MoFzxiYdxJwzGYjzI16io65hKJu7KvR6GyK-qQrmyEuqoz6T81grMPCCiP0wGgBAwW4-4Lmk6clIm0quXMureJI0H8A4rbQ_U9GddkHyBkLmbG7SQb8FiR52nRpD0P-EjKwZ4EOhrQXPG8aZCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLwYFovPu2PJjOrljKvHDy8urQ-WJ1xJGMhe5J51wHYzsCzf8Uo9Enq4vRyv5F0GAx2i3Qkqqho4qWaQkydN_UFzfui0RDjNCLt0AoORgjn_Jc6pVaSDGvigjT0dHm6kVLHm5AhebQIXsTvCfYWrzwRRik5tZfEJtJUVNErMQoI3-1CBKufhWnpyA5nncOpVLU7CU3njl-gGxSQVCDffJ8DZ9KCLUBkmlfDAKNHAqwyVI1vBiy2oIm038bIzWT83QC2cDqTRabeEH9Bn2Pv5mcORqdexPjQQx02fEUcyXyOfO3UbgMmcvXkdljUQMBqslXbxGaUm2f1g-DbAfscfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
یادداشت تحلیلی: آینده بازار نفت در شرایط جدید ژئوپلیتیکی
بازگشایی تنگه هرمز و توافق آمریکا و ایران می‌تواند فشار عرضه نفت را کاهش دهد، اما بازگشت تولید به سطح عادی زمان‌بر خواهد بود و رقابت تولیدکنندگان دیگر را تشدید می‌کند.
در سمت تقاضا، رشد اقتصادی جهانی در برابر ریسک‌هایی مثل دلار قوی، نرخ بهره بالا و تنش‌های ژئوپلیتیکی قرار دارد و همین باعث می‌شود بازار نفت وارد یک دوره نوسانی و چندعاملی شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/17908" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pT6JZXdbNS-aQXEfnainQ4zTkxd-cI1lV8UAzqw4sIMYK33OjEKVQZ9zxR74g9wPpKdfHCe4VHyvE1rFiu-uZIjFPbuiiYTZ4k-p95wLLbsGnj5kaQvk8aK6JFuu8vtgZX0MKg3FgilXiIr8O5nrJ1Umrka8N5sJihaKBq5X8ytG8L85b8yiguMnthouejVM1ZJG1oWovy5b2xb9WSf9dzUn3cgk6Ht5fNSZ5FUKwr_8wtSNnB-Q6Bo4wcMR3pntHYBuBixBCa4rP7bNCE9OY_5Pb5FhEo5DegEpqwyMkiLOhf3sauF2uGAqByZmljXOqarXjSte-8Ru8IoQvw9BOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17893">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">استارمر نخست وزیر چپگرای انگلیس استعفای خود را اعلام کرد.
دو ضربه بزرگ به چپ جهانی در کلمبیا و بریتانیا در یک روز!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17893" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
بیانیه مشترک قطر و پاکستان:
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17889" target="_blank">📅 06:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17888">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=A23pD_nBBHednAjzwkak7N1csYpHGowg5HublH1ZTXGaAzldHk2V_yyaKr7IywgsBWngKxIoJ8yUh69hdKm2pV35K04ujFPOnrsuFQF2tvYvN7z7x5WkNvQV0gTUdoi3xqYg-wuKAk6VXNSC84Qxjwz4GJSjGC7EUMkSYu4noZnln4jaNPJ2ASbja1IGSrpK52KHbq2uMSKmTFrOdd9Oyx_7C28OnyxaGrPsVX1vAYCtY9u68ocqvlioHvGvZ5c6L_AcUnuaOI28DnYV4ZP2GybCxEqUWmQDJhQ8CpcBQunIJiejXftACxFdSi9xMt2R8pyZz177mIm8jDg86soKzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=A23pD_nBBHednAjzwkak7N1csYpHGowg5HublH1ZTXGaAzldHk2V_yyaKr7IywgsBWngKxIoJ8yUh69hdKm2pV35K04ujFPOnrsuFQF2tvYvN7z7x5WkNvQV0gTUdoi3xqYg-wuKAk6VXNSC84Qxjwz4GJSjGC7EUMkSYu4noZnln4jaNPJ2ASbja1IGSrpK52KHbq2uMSKmTFrOdd9Oyx_7C28OnyxaGrPsVX1vAYCtY9u68ocqvlioHvGvZ5c6L_AcUnuaOI28DnYV4ZP2GybCxEqUWmQDJhQ8CpcBQunIJiejXftACxFdSi9xMt2R8pyZz177mIm8jDg86soKzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lV_jiFCpsjOfYi2JwJ-Dx-RRVa67p-HCFNY7mmNPdrz_814XmQsL0qG-kFzSJmP1IsYEeKXSJ5A-jQls9D1wC7wdePbgWfyJBDli2o_RnTj7C72pqeEFlFVS43av0kT4_i3N1Ml689ASorIM77bni6bqSZNKYFkMgjb6grgBUWkYiB6jgHQ8MFRKFUtujUtfu7itBBXyXEu7k0KaQ2jE7IDTcYCw9yLmYv_sBKDbtT7Lyka7IbHwkj-cnidHr4ZXc681XjgqX7wDspge1HjT7lnEbrmEf3lMleJVe52qybR65urWaJHXRYCpw0I6fXg_rIA5uib4hebkQbfAw_tKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17880">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbBXnFWi_JONDmgqHTZhzoQEkpF_PoD451VGDAkFcD-pxZabJrPNbVcXnUWEPFt4epApiIynxDKxzevJudBAFTZe_QAjnVktfKbYA5gVcV-2WZh2HBbHmpFk7XVHlg-F_H3CPYqSo0mgfa59jemEsIbe7ziOAy0L4utYXCCc7XpebD_ieAgKoOYc1WT6TzMTDhrTL-miUi0V-Rp6ueqZpNdA9r9CGRRqlq5CxugCe_KPRsMuccUGu90eGpnIis7h5mhqaJM2n_XsVsH_9NuSrm7OXMOH3uO9JM9r3IzZigMgHmNe6ku2S-LZbKW6GH6M5CY6M9_j5Z5TcWwwCos1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!
انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17880" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17879">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=bHUVTPhufRiplNK9ZLtc-5QU07jY2JbbkVHJZvp5xNkhoRUNfJmz5x19-SgFmf7_ANfo_-0k_NjXmrbxMhBiEqiZmkbL2iMYV4O8yjdGhKhgOnY9D8wuG0FQJrb5HVQP2W2IKcHE8UrLyJgdlp4fH0IStzNR2EB5BqX5LRzaOs9uLFzec_ShHPXvJiw73sau5K4BSmp_4YD-qLAb9D1cRe4_6cCD-2SkzyNgOdutM5OkO97YDCJjysFn2we3QVJWXWypnHFTPbdUIga94g6DUEF-C87QPcVdObe-M20w9sVdORnZzELDDaeXtmYXByRjBpSoV5dm5-90kYcjfZOL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=bHUVTPhufRiplNK9ZLtc-5QU07jY2JbbkVHJZvp5xNkhoRUNfJmz5x19-SgFmf7_ANfo_-0k_NjXmrbxMhBiEqiZmkbL2iMYV4O8yjdGhKhgOnY9D8wuG0FQJrb5HVQP2W2IKcHE8UrLyJgdlp4fH0IStzNR2EB5BqX5LRzaOs9uLFzec_ShHPXvJiw73sau5K4BSmp_4YD-qLAb9D1cRe4_6cCD-2SkzyNgOdutM5OkO97YDCJjysFn2we3QVJWXWypnHFTPbdUIga94g6DUEF-C87QPcVdObe-M20w9sVdORnZzELDDaeXtmYXByRjBpSoV5dm5-90kYcjfZOL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دلال های محبت فاکستانی را ببینید!
شهباز شریف از عراقچی التماس می‌کند تا با ونس ترنس دست بدهد اما عراقچی پشت کرده و می‌رود و بعد شهباز شریف و عاصم منیر شروع به ماله کشی برای آمریکایی‌ها می‌کنند!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17879" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17878">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">راس الفان همان منطقه ای است که ایران تاسیسات گازی قطری ها را در مارس به آتش کشیده بود</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17878" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17877">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرنگار صداوسیما:
هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17877" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17876">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وزارت کشور قطر:   انفجار داخلی در یکی از کارخانه‌ های منطقه صنعتی راس لفان رخ داد و تیم‌های دفاع مدنی به محل حادثه اعزام شدند و هیچ گونه آسیب جانی یا نشتی ثبت نشده است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17876" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17875">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17875" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17874">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇶🇦
🇧🇭
— گزارش‌هایی از انفجار در قطر و بحرین.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17874" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17873">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdKUdeLDLqMa-v3yJZGtreM7fxLupKvHfDKwguF2Yax1BxlqBiZ65lj65f5TtPQ8gobe27UKc1B0BO_oI4xJGEuD6TXNzscSePF6cW13USTUTixfuWGlocPeUrUXoSwmdcyNlCk_dW8RXTbwH-JgDokuhyM-Rk21MzPFkDp58e2ijnU2ogjWlW0VCQ3u-MzDSH9q-3GFlu9-Q-6KbpHIo99Njm_R7dYYTAXJL2xLrz8FCE3XwUgxNZPls21_piNqsrnMEJ1kXsAxvLM3fMcfEQe9noGLL3FyDEd8jmemkWhvROLHP_AaDhEeYoUtaQ18BSawQrT7qlc5bOQYqHFiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به جای طارمی، سهراب سپهری رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم  》Keyvan《  @OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17873" target="_blank">📅 23:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17872">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">اگه به جای طارمی،
سهراب سپهری
رو میذاشتن نوک خط حمله ایران، الان ۱-۰ از بلژیک جلو بودیم
》Keyvan《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17872" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17871">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">به اندازه قهرمانی پرسپولیس در آسیا از بلژیک جلو بودیم…
لعنت بر پرچم کمک داور !</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17871" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17870">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تیکی تاکای عالی از بچه ها !
منتهی در محوطه جریمه خودمان</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17870" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17869">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتوییتر فارسی</strong></div>
<div class="tg-text">از نادر محمدخانی به اینور هر چی مدافع تیم ملی داشته امشب فیکسه.
》Footfun《
@OfficialPersiaTwiter</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17869" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17868">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">با نتایج درخشانی که همسایگان بیابانگردمان در عراق و عربستان و قطر گرفتند، فشار روحی از روی بچه ها اندکی برداشته شده و امشب با خیالی آسوده تر می توانند برینند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17868" target="_blank">📅 22:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17867">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17867" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17866">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خواننده Secret Box مدتهاست که از این طرح آگاه است.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17866" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17865">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اسرائیل در حال بررسی عقب‌نشینی محدود نیروها در جنوب لبنان است.
— کانال ۱۲ اسراییل</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17865" target="_blank">📅 21:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17864">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17864" target="_blank">📅 21:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17863">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مذاکرات آمریکا و ایران در سوئیس به دلیل پست ها و تهدید های امروز ترامپ، زودتر از موعد با خروج ایران پایان یافت</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17863" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17862">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.   @StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17862" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17861">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار استراتژیک</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=bRzzFwe3BJDwJU0MwQ1FmaescbuJcrVErEUARAELmBwXyyOCfjRaCwCcaNXCaJ23vu1jrZN4U15gtS6rz4opHJlb_fHqwRzT96HV5aCYw3zcwkBbVVQYtfIgBAKDm-rp2SxFhVH_CcW-uHyTjQnqdhlpjG10o-76X564F9Vtd8L26d24KT38K7WJEMEv9hpcso-0QeNAE6MJ6VM-M-8LGk3upf4Kvs8W_qX4y1wHqcjmjfFt1J_ksgcS1u8Z5Slo8U0sLJf8DOxlL33ozBkmxMwsrd73YEcpfe7mJdyPIgyDL0iF2dR-cIBOYJ4YA9Kka4fO4bnsE9cpt0pVvRSnxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bcc2190.mp4?token=bRzzFwe3BJDwJU0MwQ1FmaescbuJcrVErEUARAELmBwXyyOCfjRaCwCcaNXCaJ23vu1jrZN4U15gtS6rz4opHJlb_fHqwRzT96HV5aCYw3zcwkBbVVQYtfIgBAKDm-rp2SxFhVH_CcW-uHyTjQnqdhlpjG10o-76X564F9Vtd8L26d24KT38K7WJEMEv9hpcso-0QeNAE6MJ6VM-M-8LGk3upf4Kvs8W_qX4y1wHqcjmjfFt1J_ksgcS1u8Z5Slo8U0sLJf8DOxlL33ozBkmxMwsrd73YEcpfe7mJdyPIgyDL0iF2dR-cIBOYJ4YA9Kka4fO4bnsE9cpt0pVvRSnxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
لیندسی گراهام: به مسئولین ایران می گویم؛ اگر گوش می‌دهید: وقتی از حزب‌ الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@StrategicNews_ir</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17861" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17859">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ درباره لبنان:  من ناامیدم که اسرائیل نمی‌تواند حزب‌الله را از بین ببرد. آنها بدون خراب کردن ساختمان‌ها نمی‌توانند کاری انجام دهند.  من نزدیکم که این کار را به سوریه بسپارم چون او کار دقیق‌تری انجام می‌دهد</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17859" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17858">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گزارش الاخبار، جولانی در جلسه‌ای محرمانه وعده داده که از حزب الله انتقام خواهد گرفت. وی گفته :  «حالا نوبت حزب‌الله است و ما انتقام خود را فراموش نخواهیم کرد»  به نظر می‌رسد  که در صورت حملات آمریکا به ایران، جولانی از وضعیت برای باز کردن جبهه‌ای علیه لبنان…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17858" target="_blank">📅 18:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17857">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من دقیقا نمیفهمم روی چه چیزی به جز پایان موقت ۶۰ روزه جنگ توافق شده؟!  لبنان؟! تنگه هرمز؟! موشکی؟! نیابتی؟!</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17857" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17856" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17855">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قراردادهای میان کشورها تحت فشار (Under Duress)  در حقوق بین‌الملل، قراردادها و معاهدات میان کشورها باید بر پایه رضایت آزادانه (free consent) منعقد شوند. مفهوم Under Duress یا تحت اکراه زمانی اعمال میشود که یک طرف با تهدید غیرقانونی، نیروی نظامی، فشار اقتصادی…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17855" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مدیر Secret Box از اعضای تیم دیپلماتیک کشورمان ممنون است و به شرافتشان درود میفرستد!</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17854" target="_blank">📅 17:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4HbmlZfQWzWeVXPdzNcRKsl4zAUU8pIeOwIFlA5YUaKrU2xZFWAzv5SpevOBKUOjeHf2LcLOMlt9tIRGf2TnLLhaxR10CTR5HekBPFpO2VwXRT-doDEeBBfcHZIKf2FpRb2tewJlxh9Voo7wgYBkX6bIaE1dc9i1B2j17NjKS7keo7ihV1hFV3ePHwEp4Dx951Av-UR9uk0FxW7ismEFNHY9aGYzSTxcyY4_CgIPz34KtgG63KqEpFZaY05gQ3c8s3F7rB7-7iuybqLAD4WymlTnEwlwvU7WO-TfmXlTiBkNe-X9JsGwhhZAWvsOKhS-zZw5dDTPakFT9CegA6Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه یمنی ها در باب المندب فعال شده اند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17853" target="_blank">📅 17:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:  اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17852" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ:
اگر ایران تنگه هرمز را ببندد، مذاکره‌کنندگان ایرانی به کشورشان باز نخواهند گشت.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17851" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">— وزیر دفاع اسرائیل، کاتز:
"هیچ محدودیتی برای سربازان ارتش اسرائیل در لبنان برای اقدام به حذف تهدیدها وجود نداشته و وجود ندارد.
آتش‌بس دیروز اعلام شده، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که جوامع شمال اسرائیل را محافظت می‌کند، باقی می‌گذارد.
همانطور که نتانیاهو و من روشن کرده‌ایم: اسرائیل از منطقه امنیتی در لبنان عقب‌نشینی نخواهد کرد".</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17850" target="_blank">📅 14:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeexInpODvK_BwAsga9UXZq9SQ61PmbHJhRcc9E40_CE1McL94Y9RLDfKBIbono8JuPtmLMJwfGKji-p_mV9wAJ44GjZxfPUAUkeUg7SidxyNrSArUFyN5L41_2o6J7V2xhc5R0bfl9XMQKAyEqFlmSX7kstpWKne1XUNZxCkLRqHX9XIFaIEb3pPwGlO427eiPa8_HClOiCca59Hq3ReyH13O2qSQ6YjNKHUxjcJPyS0b5UaUYNT7L8NDCIyLlLP7MTCs3E0QeFM-iIVpuNSW9SHH9VIIQb84Krn9p4RDedhvUPDz9WXx-t1zNl6XEJA_LWOPNRMCUyR-ZgGvDO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو و پیام Hawkish به بازارها
در نشست فدرال رزرو آمریکا در ۱۸ ژوئن ۲۰۲۶، نرخ بهره بدون تغییر باقی ماند، اما لحن سیاست‌گذاران به‌وضوح
Hawkish
بود.
✔️
اعضای کمیته
FOMC
تأکید کردند که ریسک تداوم و حتی تشدید تورم همچنان بالاست. همچنین داده‌های
Dot Plot
نشان داد که بسیاری از اعضا احتمال یک مرحله افزایش نرخ بهره در ماه‌های آینده را منتفی نمی‌دانند.
اگرچه در داخل
FOMC
اختلاف‌نظرهایی وجود داشت، اما دیدگاه غالب این بود که
Rate Cut
در شرایط فعلی چندان مناسب نیست و در صورت لزوم حتی گزینه
Rate Hike
نیز می‌تواند مطرح شود.
🔽
واکنش بازار سریع و قابل‌توجه بود؛ پس از انتشار بیانیه،
USD
تقویت شد و انتظارات معامله‌گران نسبت به سیاست‌های انبساطی کاهش یافت.
نکته مهم اینجاست که بازار انتظار یک
Full Hold
(ثبات نرخ بهره بدون هیچ‌گونه سوگیری مشخص) را داشت، اما فدرال رزرو با اتخاذ یک
Hawkish Hold
نشان داد که همچنان نسبت به تورم نگران است و برای حفظ سیاست‌های پولی انقباضی آمادگی دارد.
🕯
جمع‌بندی:
فدرال رزرو برخلاف انتظارات بخش قابل‌توجهی از بازار، سیگنالی انقباضی ارسال کرد. این موضوع باعث افزایش تقاضا برای
USD
شد و تا زمانی که فشارهای تورمی به‌طور محسوسی کاهش پیدا نکنند، می‌تواند از دلار حمایت کند.
💬
برای کسب اطلاعات بیشتر، با آیدی آموزش (
@CWedu
) و یا شماره تماس 09908006002 در ارتباط باشید.
@CyclicalWaves</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17849" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور
:
سرویس اینترنت پرو متوقف شد و مبالغ کاربران باید عودت داده شود</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17848" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🗯
دونالد ترامپ ؛ رئیس دولت آمریکا
:
آنتروپیک دیگر تهدیدی برای امنیت ملی آمریکا نیست
وی در مصاحبه جدیدی اعلام کرد که پس از اقدامات اخیر شرکت آنتروپیک، دیگر این مجموعه و مدیرعامل آن را تهدیدی برای امنیت ملی آمریکا نمی‌داند. این موضوع پس از آن مطرح شد که آنتروپیک در پاسخ به دستور دولت، دسترسی کاربران خارجی به مدل‌های پیشرفته Fable 5 و Mythos 5 را مسدود کرد
اگرچه ترامپ از سرعت عمل و رفتار مسئولانه مدیرعامل آنتروپیک تمجید کرد اما همچنان احتمال استفاده از اختیارات اضطراری قانون تولید دفاعی را برای خود پابرجا نگه داشت. در‌همین‌حال، شرکت آنتروپیک نیز بر تعهد خود برای همکاری با دولت آمریکا جهت حفظ امنیت زیرساخت‌ها و پیشتازی در این فناوری تأکید کرده است</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17847" target="_blank">📅 12:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQvWUcxtWAFVs_wC8yAdyAAXW-z-b5PA5veWc8o1wrJuXC0NWZLBZUqnR4LWJAve6eOaaMVTIlxYZICpOxa2VYmALjuponkLsdFOY1tGsn7BaHUBPi9mhtyEBhJCkVliYPZzyMWze3_eahFpdleo_7488-EcsUwZ5zsnBSzbZZGrayDI4hdHceeynlzv1hnbmZ5IONe7hDht-d661u4TBTZ0dxfiNDMsF3TPrZ1YTsQjgTzeYmDSnym4p-P9uRL1wCrHhc13DEs8Yan-Qlx2YHHS72EEbRK0JoIBRW292oV5iA52i5B6CHKANHO0N9cJmlljqTJvTsx5t9plSBoiJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدانم ولی اگر بیعت کرده قطعاً مصعب سرش کلاه گذاشته بعداً</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17846" target="_blank">📅 11:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پزشکیان:  تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17845" target="_blank">📅 11:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17844">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پزشکیان:
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم؛ این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17844" target="_blank">📅 11:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17843">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حسین شریعتمداری: مسئولان نظام برای بازگرداندن  بحرین به سرزمین اصلی ایران اقدام کنند  حسین شریعتمداری نوشت: «هموطنان بحرینی‌مان بارها اعلام کرده‌اند که خواستار پیوستن به ایران یعنی وطن اصلی خود هستند و انتظار آن است که مسئولان دست‌اندر‌کار نظام این خواسته…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17843" target="_blank">📅 11:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17842">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17842" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شریعتمداری:   مسیر دفع محاصره دریایی آمریکا؛ شلیک موشک‌های ۲۵۰۰ کیلومتری با کلاهک سنگین به سمت باب المندب است</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17841" target="_blank">📅 10:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17840" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17839" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17838">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آقایان عراقچی و تیم همراه علیرغم ادامه و تشدید حملات اسرائیل به جنوب لبنان عازم ژنو شدند!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17838" target="_blank">📅 09:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:   «در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17837" target="_blank">📅 08:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
«در طول دوره آتش‌بس، به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز دریافت نخواهد شد و پس از انقضای این دوره ۶۰ روزه نیز هیچ عوارضی دریافت نخواهد شد، مگر اینکه توسط و برای ایالات متحده آمریکا وضع شود، در صورتی که توافق به پایان نرسد، به عنوان جبران هزینه‌های گذشته، حال و آینده برای خدماتی که به عنوان فرشته نگهبان برای کشورهای خاورمیانه ارائه شده است».</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17836" target="_blank">📅 08:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هشدار فوری مجدد نیروی دریایی سپاه روی سیگنال رادیویی برای گشودن آتش روی هر شناوری که به تنگه هرمز نزدیک شود.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17835" target="_blank">📅 01:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کمرنگ شدن اهرم هرمز؛ چگونه امارات در حال خنثی‌سازی یکی از مهم‌ترین ابزارهای فشار ایران است؟  برای بیش از چهار دهه، تنگه هرمز یکی از مهم‌ترین اهرم‌های ژئوپلیتیکی ایران محسوب می‌شد. حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه تهدید…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17834" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr3pduXPjuvT4WUW43C3iQ9KDJwcTx4unVFUuFrWJ_icO2lwav0pM9m9YLjoQPjYOr0wICwYbBw33oypH68nmI1-l-ywuR6VdvYV3dR6DTrq3Z6nTkRZydKYqZuR9VlXFjzzikLm-DWAno-aqxc19kzY9_o4NSVnXdxwIogJ3FxvwnAc8uDrRV85ODYG9RtMGddHjbTolEO2KyubAy2t2-ABlaoF8F8BJd8CYg-sCe3PmBZSdzMBPpcnpz075hlykGqofH4E03Or4DeY1CjYtXVOXI4Z1oT8V-dqqpCnNxxBi9KstRO0tJe_sRd5-LMh5RaRMUrCaeErqFVHKyFoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت ترجمه شده: جنگ آینده، جنگ سیستم‌عامل‌ها  دانیلو تسوک، رئیس مرکز هوش مصنوعی وزارت دفاع اوکراین، پیش‌بینی می‌کند که جنگ در سال‌های آینده با یک پارادایم جدید مواجه خواهد شد: جنگ سیستم‌عامل‌ها. او معتقد است که هوش مصنوعی در حال تغییر بنیادی شیوه جنگ است…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17833" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=haxYK-WeMcSyH4czjA783v7vn68Y5aMVaVLHrFjCCNDFocAj-pcOZ_0KIH_ESkSI9WZYG8wudZIJ1APYN-F2PTm1fxWthmHpse_qEfd0qesKW90m9vnbOChQ0NHYMfyCOsZQh7tZB_VMXIqQJlhhzwRppGSqU2ACvWK9xBk5ORDaUJlZTdkUJRqrBg3J__Z2SRNnitPqUOWIP5SVjJ5IJNqK517gTBblHkE7MdEYy5kN4_TWbPlfKJjwyfQQsMfHvlsQ_JhGOGlZyM7xQn3T2u0aMhPlVTB4zShvpUMX8rrBFsSeAj85elWjuk4e0AZJZ_pf_pDIcaD-MG7HwRdzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e185e8d16.mp4?token=haxYK-WeMcSyH4czjA783v7vn68Y5aMVaVLHrFjCCNDFocAj-pcOZ_0KIH_ESkSI9WZYG8wudZIJ1APYN-F2PTm1fxWthmHpse_qEfd0qesKW90m9vnbOChQ0NHYMfyCOsZQh7tZB_VMXIqQJlhhzwRppGSqU2ACvWK9xBk5ORDaUJlZTdkUJRqrBg3J__Z2SRNnitPqUOWIP5SVjJ5IJNqK517gTBblHkE7MdEYy5kN4_TWbPlfKJjwyfQQsMfHvlsQ_JhGOGlZyM7xQn3T2u0aMhPlVTB4zShvpUMX8rrBFsSeAj85elWjuk4e0AZJZ_pf_pDIcaD-MG7HwRdzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که سنتکام میگوید تنگه هرمز باز است، اژدهای بندر نظر دیگری دارد!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17832" target="_blank">📅 23:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17831" target="_blank">📅 20:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!  در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17830" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCoFD1JbJLXRLyx1lyXSxr2d1Im0DmHcjWOW9bw271Kl9NwYZyzAesY4xBXsVI_jPqM8QWZGNjQ2YzkwFynwtEwcLsLfVG89Bq7lQ1Pa0jxxOjQRhvM4LJosJRSghh2Vnq5q7TzGCbBpCg_w8042v8YgfL7aL5tNSHU5W9chuhTIxrGCtILb5sQ_XRFIdE64ucYxuESqvtJJmitfDkL3xVOhnCYO83TENett7BUG1zeyIvM_D5gJPZLx525wRpAJ3prWTAswBFXxHVnUr8_iS0ebvjdqXfWZ5sv5TMe2ss6SjpVIfMm1f7x6GFx-7j0AFxhXxhMlvcUC5Pj8vbvaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین در حال جایگزینی مردان از دست رفته با وارد کردن  مردهای بیگانه است!
در هند، بنرهای دولتی اوکراین نصب شده‌اند که هندی‌ها را تشویق می‌کنند به اوکراین مهاجرت کنند تا «خانواده‌ای تشکیل دهند» و «شغلی پیدا کنند». این بنرها زنان اوکراینی جذاب و مجرد را نشان می‌دهند. در هند به دلیل فرهنگ پسرپرستی، کمبود زنان وجود دارد و زنان اغلب در صورت اطلاع از دختر بودن جنین، سقط جنین می‌کنند.
در مرحله اول، برنامه‌ریزی شده است که ۳۰۰٬۰۰۰ مهاجر وارد شود.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/17829" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رسانه های اسرائیل:   عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17828" target="_blank">📅 19:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzoSbSu28VhQJrSoEN3hO8ZFqiV7TjmtNQKgLLfKhNjs6MzNbQcUdIVFQulle1l6o8jQ7_n4aV3XuBwPAZ9uRuPaQAlLWCpIZZr3zM8i0DMSo1w8jTCSbEWhsLFsQlYSF7MqGQ6GjvaIoMHcy3pFsaYgwILCNLG7IGRkTKJr_AFTnNbxj8wMaHNXiexcYtm2pOUbHimTZM9aykizltYs9mQ7LfGiqmiIhCp5m8sdORJpZRr0f8UqwumV3Edt1GptzC49M0bi3oqhYIJ0kWmS9ixNnmzu6tL_0g0tGdFDtIZaRKiD91YDm4jDAEkgV-HA5o4TAkPtKBGfd2sVpi19uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عثمانی ها جوری مهمتچیکلر فوتبالی شان را بدرقه کردند که انگار دیگر نیمه نهایی در جیب شان است!  اکنون با 2 باخت 0 امتیاز دارند و بازی بعدیشان هم با آمریکای جنایتکار بی رحم است!  ُسبحان الله!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17827" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17826">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه های اسرائیل:
عملیات ها در لبنان متوقف شد اما نیروهای ارتش اسرائیل هیچ عقب نشینی در لبنان نخواهند داشت.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17826" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17825" target="_blank">📅 17:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17824" target="_blank">📅 17:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا اعلام کرد نظر به بدعهدی و پیمان‌شکنی آشکار آمریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس از سوی اسرائیل در جنوب لبنان و همچنین با توجه به‌عدم عقب‌نشینی ارتش این کشور از لبنان، تنگه هرمز مجددا بسته خواهد شد.
قرارگاه مرکزی خاتم‌الانبیا اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17823" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یارانۀ 2 دلاری خرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17822" target="_blank">📅 16:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWLduV0cL-1lxz6MKY1833HZym9ucUTZYIEztK3W8efabgVLpgBfF0xaJJCqeqTPUIYi1tZ8YChgwd6fWMKv9X5ZaKW7h8ci-jEDRh4e5r0ECaZCvFPa07EzMMTs0eESJQvTbTOnFQZR0z9dq--im_2QTjeithkvmT4XPtvpXcZKloq3SYrNL2VZCeIVA7LqGAi8PWvlvRfXtA0FvsM4ErX7ucxijMMauGdWd_yAb1hL-msqhiX_h3x8tYCjIt5gnIOreC8Gtlq2vnfAHeQ1sU0wtmbgpmXSUBddNnYcBT2UxbA6YjLFnNOgERj7c0Mq5Pc0vjmzWbRLjKR8KXoSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لابد چون نظامیان می دانند درگیر شدن با ارتش اول دنیا و یک قدرت هسته ای با فنآوری بالا با توییت ریدن زیر کولر متفاوت است؟!
یک بار از بچه های پدافند و لانچر و ... بپرسید شرایط چطور بود؟!</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17821" target="_blank">📅 16:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17820" target="_blank">📅 16:03 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
