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
<img src="https://cdn4.telesco.pe/file/t9QXv6BYYmt70VnVtIEQ32Bnz_lxVUiQmJZfUjEj26KTCNhCiJ-6UTUS3r7FLrS8C5blGXkETOPgBlc3GavOQaBwC2hsVbOPjQqyxEjRXPVET1P5PX5zRkb6BsVhrq91DMH05zDQQSZ9at4ffa6NhW36ZgZnLqwFVRWc4tsPE_i-DV8OSQ4yW-0rUdVkhYfBluo-OpTXX2AbfOnSZh7Kf6pkaE8eB9tTXFXlshoUfbbibGK4GisGAgT1tjXQ5c8Mo3G86WkbR3e6E_iftWO9SQsy6X-GRBTCJzA1dhhAlTZy4RHdlsHH_Qz9ZyExbWapaE8iJOkAA3rzCPxAhELNXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 545K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grPzqcVyce5MbcL6MKBQ736WntDNNSBCCHlGV4yXv-f6hY9aL9KUptZhGMzt8G1Pfc1clCX_i-89Hsc7T6fyZsvF1hINQT9AH_W0MOE4VI9vlSqndsQCAH0uN1eouRxmaGc5vHleMy7eNpSwdJh5AClTqbRTGEai1NgKnIGzaf3bJDS5V-zwaxbYwJzVVTs-wXq6ks3kXsstP23-W-vDJJdMXGXViybJWMkOT6dkhCWRTBgjCfOn6Fvcf-yRl2ApkEOZNMJL4ohDWF02auUlvzvFKKsD8MC9qU0XATooNq4ikSY7rY3U-fy7FDUWXeglXY-YhDVgkvAeQabvm2E2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FueuJqDAvtTTLVmIuUP2sqMzu9BsTxqfH9b3vV0p2UFwih48yP6fdly-jBfFDRE5zUpO8BcBm5m7A_XtAfbXJPe2D2I9bAaAn7kF3BETpxqxBKxmKmr3lfgTeBtGQk01qEW6pCttXT9q1tDJZOOmb4S0gUEfM1KFFhuomVTax5JlgkPDOPSY2N3UdbS5SHrdL0_YIqArda-7nOE6VPMb-oeLXvn3MupFX8XwdFhCjFAk98AL00gQCl-EVq0XPzmYaHlViHaFkpgrk3-AaKYIBPIE-Za0GfNMN4QDyP2WO20IfOKlKuANLFI8SGKTzT5zQc0ZwRk_fSOr-vAAT1p9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxAjgqSl2SB1YeWhbuLTig2G-bw7zrV_xlUArawlnZ6fRv0SdEEHxp0A9z9q28hck0olb0ty8F4SyEHlh2t30blDhCu9uIZHWbC2qWugYc1zpuMlDLMKwVZZrs4ZwHuxrExRmYMhQ68PV-S164IVg-HrQyYxxUSP5IHVKA0BpI0nKdpMuIQfsHg4sTk6hp4xtkxJjH2lOm_RlTyMhITMXWrMfNeMya9nNToe04o1rnvOdSq81fF7EsZoevY920xS1RyS4Scuk5MT2D_RduxWbpPZ4V2cgh4ibuylMgES-D6N3a6ug1zAHR86NO-vNoPVf2dzjpg6nWtxhq7kjRIuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r31
📩
@winro_io</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/26280" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct_sCUJoYKCSkrv7FheNNZqS-RNvF_O_ORHUpCZ9J1TkFd9KMbFXRsSJVfplWs6IIi0Qpl6ARsCITny2-CfJYSQdWYszNX5XdAFkfpE96sy81oyaKX4rxXexB5wuWYPeWnfV7F8rE3L_zuSW6gQZjBFUqWOt5uE785dHXlnWJoAB7uip1Hm0qNChrPM-RSvsm1-FShQNw3syvvpQeT7zTODI3GBY2XI9YaT5gMKGmToLejEz2yI6ogvzPItpupOHtZ77yi-I5UjWnOSTMN1pFOVvs_OWeBbvdtL378j8cr1DBNpkZiGgMdRwM8KDBGrdphF9RsOwHZOEHDVOrvC8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-96ktIoxM9JGuoKECL_hoGqK_q95f3DJgVzGu0fwZnRzImfyu7IAYLYTW7atqFdtz3orRoCa3Nr3aSZrgjM9JU_ElVqRxAMhrwqnOuo-aSBYK2BngShbtpmH9QtiW2HxzT8Jw3oWFjrkka_f-vC5TCmKJh39Nc5Vy6Dr5uAh6Z_qEQFLlvCVwS9mW1pzG8H_bePJKrK6IarMIo4yUgkjvbS2k7DKo3K5Ud0jRyFmCW3kQ7x269FcMqePqbS61VHWMWzsGJm1EcRXFcJGJhuNc_zZ_-tentXYTRrxzWm2ZufrmUmjPZ_JInZ0sig-QBX5p5aNi1322s3iu09zN9ghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGgMpjT1WlmePFKXhHUWCNDabILWNpPYo9W9uXRzLdkc9qZt3LuQNHfiJt1mH_txhUg7m78K5sGEUupg8XVS1ZPJlzJTVsx61cxh1-EWQwgGUsDt_q6hy22UF7URl-t6whxcotGFATEae0ejteVgnegn7o2Hvem5Oy4fkJvzctPWUVwCsMfnU8XujpkSvZtScC-8NW_FBAk1CLLLeHnhD576hYTQCCyM2gk7cY_0hJXIItv1Ki_w2NYNceJutoSJZZI0FbMpoUPg-Qi_sndf2ogvKLg4-C5On0dHk4YZSTNMlYDp9XlsH0JpJh7vIuRrSaOd7fIbtFNMYVxmiX_GfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpKImnDXEbYxcK8fR4QFYhY3M1XScePpCNmwZ6cdHbGhC1MPgDPjQ_s0udGbeTncuHl85hmRGwtaVg5Vzw1Oefpze2N4cdOQE9djkkm74bh82dOgmOZaTsLPLosf02TI-kbT9Y0q6zwk3WbOnoBTBTe4cY9oSFFWOZQHN5ZHToxgUqgEboTadi-03-zzdELDr_v0yOPGKym5EySGrup7Y_jrSUlPYmvlujqRkfsuQvzbm9PUtIEBN1rXXkH60AA5ZN04tHBgU5_NctAQhOpR_7Z37CNqMlTxWIGrc_wtDvnWxA_SHp9XTL5c7i1AcFLiPEQNJ3tYuO_b0aVTVYhMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQCmA1ZIljxhPY9k_dJojGRjQw4EH3csPf4WD5PbiEdeEnpveCRbIU58TsYqAjDjTUSCFZwjAoFLTj2aDIX61GL6_IL-MQixoj4ZDA4qKSLAK5090kVT9KKdUfbLoBAfnCsF9D8xZKb8kZ-sBgAx_uam_Q7kO2sMeYQPWtIlBOOpMEeNV2uGh3SmPt7mNZLFHuQn4TJSBfhh9PnwGQojz6qHJPZH0N_fOAVWY8oAutJl17x6OLumj3sNalvQ8M1ejsdT6AHQUmP0eApyrrZNLnfAvJSuKV0KlGUjjK6eJMU5UZgAY-TNXuSsv-5wrzE5nEb7ayoNeQexcOKg7Cn7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=MyxbedJN33ADN--xr88G4aE-npGXv-iNE5upGTEy29Qfgsr1bmOE7S7E9rDouDj24HOQ8-BLZwuZR9I15pNsQ6Y5Xzqw2XyNewR9AtlNwsTfNqLE4zeN-Vxm6H9-3BDfaIszGeE-EzYchY7tFbJRwj2v_ewMCcFc-0tX8sK-BI3TIasYY8V4mo9BZV4PRY6TBAOvJq0DNfMD9bCObvKkPWsDh5_WD9llJoca1SKB3GecCrrCzMaCefGm4W-Esv4v64aDqYsur_MIT444-X1izVDJ5OM891MwcU4QajucL_AeHziSuAgoQ29z0PwAjaAq7Oef56Ry8BceOkjf-b1LUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=MyxbedJN33ADN--xr88G4aE-npGXv-iNE5upGTEy29Qfgsr1bmOE7S7E9rDouDj24HOQ8-BLZwuZR9I15pNsQ6Y5Xzqw2XyNewR9AtlNwsTfNqLE4zeN-Vxm6H9-3BDfaIszGeE-EzYchY7tFbJRwj2v_ewMCcFc-0tX8sK-BI3TIasYY8V4mo9BZV4PRY6TBAOvJq0DNfMD9bCObvKkPWsDh5_WD9llJoca1SKB3GecCrrCzMaCefGm4W-Esv4v64aDqYsur_MIT444-X1izVDJ5OM891MwcU4QajucL_AeHziSuAgoQ29z0PwAjaAq7Oef56Ry8BceOkjf-b1LUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLyb5v1dcs2zs6JILMMQOGt3D85e0BlyCGhLkxM8KQZo3aX3iH1Zcv0ppm-VTtyTo8zPNDf1YzhrdQpXlZRyvt_Ml-oEo8qfBsNH8qphTsB3vblKYAc-2IUp-_stnXFjjGlHVmh7T-TDK0SLzE7ywT7UGT2xJsPZqWbtXest39owBylQwsiAPjmlLuyVxo5lbYxHwfcD3uCCM97ONLBXwLX2i1nAJL2OUiFV1UGH74PsbRNkmtjPgj1bHnmcPUH_j1_WHN3Fpm8zZNgk4p80L41fmY8Q2FYP-1u6g5ThMjp4yiykWkHKKzWqLJhgFxRf-lgZskqZ4Meu0-xLJdhF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=ZRhm3WKXwJTwPFgy_1IAaTNh6n6zvbs-nlNES96pspIHjJo3QdjzkfMAiUjVF0Ae7Qq6HFliHFaqoSogCcYqB2MAhA3IWUs4yIFsgD0ZEd5uwNoZNo-vJy6cTTjDRWTegEZIcLHAz9cWAF9SW_8m7hFfsPtNDG9v7l0CUIw3r5610h3xjPj2soFVEIzdfTaNgY5lezCqTiHjjVyYZUTWY_NGWBUSwasyKJfVkAZcxNH_7pgtsJzvPSRA-VPF6EG03IJEBIsJOaKNQGkUFTDpy5XvrQ3O5-VciAgbRv6lME4iGH7EwyhC68uH_17UccdtmsV0PSOe50uVeHp-YnzvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=ZRhm3WKXwJTwPFgy_1IAaTNh6n6zvbs-nlNES96pspIHjJo3QdjzkfMAiUjVF0Ae7Qq6HFliHFaqoSogCcYqB2MAhA3IWUs4yIFsgD0ZEd5uwNoZNo-vJy6cTTjDRWTegEZIcLHAz9cWAF9SW_8m7hFfsPtNDG9v7l0CUIw3r5610h3xjPj2soFVEIzdfTaNgY5lezCqTiHjjVyYZUTWY_NGWBUSwasyKJfVkAZcxNH_7pgtsJzvPSRA-VPF6EG03IJEBIsJOaKNQGkUFTDpy5XvrQ3O5-VciAgbRv6lME4iGH7EwyhC68uH_17UccdtmsV0PSOe50uVeHp-YnzvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFf_q6_Xz0KWW8pQucChXGGEDqRkZRo8INcxKiCNKexZKFvay-v3VPGyvd8kb4KTbV1WY5Rz2jdxwsDC0dPuvuJcORBKXkf_r3SjO0JxOC4ATdRow69LsaMxcNGSXx_qvrZBrkcNcVtYQFMbIBfPXYjpzDa2M27-tIrKXWhLZctLG6cjzQTz7h-QIEDbOX6XHp0VWojl1zSkoHbuvMb4zfKVK58_98Fw52E9m8goBHZxq9fxeCYVaxaXPAUGI6mSbtG8mtmj2XKKZnDs7GOoE1mSt0S7d-pNfc6WXVn8dCoVkPXrtyC255QIAzWCepwW5vmPOv9a-znvl_l5mdmuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs5K6FBVOz_p8kMRhsqhhcjsGlCrPelI12y3FotDVD2PPKiTHGqF2cBRDVL9MtcnnQjQBvhI1-nHHR8oNv6nLrfOXMidtvajiJl5Vr6eo1BMxk10DRjgqa5AVby6_L2nqTH4Kl-L4txlzwH0494sm8Nmt3XgaOxgN-AuD20xdMUc663TiiNQcjdKMmHIk7E5QdB2y10eJimH_R_bupifNllkTSBC8Kv5bA1rc5ndcij3UaDkC3y91kakIzUdUw15xt2Hztvz47TgF8CXBqkGsHaFbz6Hedz5vSI0B7LhRkdPQ8s13SdrJOpgr4Zg6RsYMhh0w3etfQFS4xBa_-5sTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ZlVfcYCG8sY55qqxVgbiV4izAz-GtWaKCwH03FrGA8jjANBBnJhvWcGLOAzCaii25KKNJqK8bNJZAGD0XcTaG-dhg-iAlyeDS_p4SBYfOA_gZjUdq-z_rR2XK5CmyAAL4O4Gc2UdSwE7vEQGlclR5TExlTK76Y9Ay3YSZzdzgIk6AABK4171RHTWqzpXK6SUVCwt_NXKVeMh7W4lZEVotJ5_QGauj831PXh3KVr7n8bcMuxZsy2EhtQtFRRqPZ_KbMIJeTbYxNhABZzXeuH1Hnslj1IcvAMeGqxDkJImgbCrQVxFdUwq-P16xt28yBzkghjqRJVpHdjzIzzowUAb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=ZlVfcYCG8sY55qqxVgbiV4izAz-GtWaKCwH03FrGA8jjANBBnJhvWcGLOAzCaii25KKNJqK8bNJZAGD0XcTaG-dhg-iAlyeDS_p4SBYfOA_gZjUdq-z_rR2XK5CmyAAL4O4Gc2UdSwE7vEQGlclR5TExlTK76Y9Ay3YSZzdzgIk6AABK4171RHTWqzpXK6SUVCwt_NXKVeMh7W4lZEVotJ5_QGauj831PXh3KVr7n8bcMuxZsy2EhtQtFRRqPZ_KbMIJeTbYxNhABZzXeuH1Hnslj1IcvAMeGqxDkJImgbCrQVxFdUwq-P16xt28yBzkghjqRJVpHdjzIzzowUAb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuSVMnzg5V_MCgdRLhno_LdN3F1nTZMnTHbT1G2I6p1WzboKEuhwBsUyUJ63T-Lss5446o5zNq1mBL8b5JJOla9AKjETSxoF80o5SMN197cio2sEkwAa890O-seQ-E2-1S3vBXKxmO7SwsSqVpNiTZSAERwsoESFATqafeU7nZPpM9D8zj-HzSvyNPMXpxmkiA1LVrgJUM5uOT8xjA2keXuwMWDXVwbvmRKnqnj329wI-AbeOZjSvJnSUGDyvpaQyaKmZdFA6r0ZfGsFUO6u30sV5QtfHCZ4hW_kNorFjTOFlJHc5R-wQgjmfO_HJVNB90eTDKRrUjkjYONWkz1Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIrgJDezyXVDd6ps9UghDn2U8rEwOCzXZdsEcyVofccc_f583zVtLxM-AlATVbJFD1jRZ1ZL21EQHbF2fWOsIafShISiwK4jRId2RjAhh1-E_gJBCe6rRHXKKzvTj2BkdTNNK2Rs-yxKscjjmC2GhSBeG2Q_-C_INFZLqjWVsxdlgUazN9WAxtgHbUd5suUdEI0u_Iq8it9S1C0_DPiZ4EB9nEF8uno8At7HlOVfiOKVNJQKDvcG8Bs6mGxiwuVQIEzBOfYdyVeARkQZmjzaK8QiK_QIKSohlTMUghB0AOhjQHZoOz6WOB6zP-8nDo6FTHDv4RkEH-lgiapcACJ57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBCEUwBpelyJiO7UjmALKc-_-v522PeUCWqPtqIOiHJbNXbOPVbH5mGI2GSsZpWaa_4gZMeqUC7K-8stgqfDW6-UtCumBapvJnsGMit2Nnfeah66oox_PTSUmGs5n3tPKnRPYvk1X63IGK3l_GQI2gZU2gB1ocYe40h_Md0xLLfHChf1eJFr7oHhrnPJEhrwoeknwiIKF5lsOH6D3Oo-TqFSOPyKhFGfD3OyP59ZF7lpdkMa2t3GoQOPoB_P-AkfwJ7sKONfaWPadp6PLalrPeJvCkAGt81s_2K__h-aw30lbx7_3Xc0e1R6SQ_UlnRMzkFdxFu0Izn-DOe6_4EzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=O8zMfgOwgjtqf_VeTnKlJhTswLRXBja8QmsUdfwwy20FUfaYYv_e6bMPSZeLSlMxBBiaVJ_jK-t59zGkSQkaC7g_v3NvuiPXpHPicTInrK3J-MMVhDJk4jvpsQ_PoqDrgAS1g5yiUVLIOfqWf28SNVOGvQqBWfO5Uzb55E4Lta13cNob6ZNcW23IKCPrV0qGymjwuxU7xqpLFuHSSdXhfdCrD_-xhNmlxLNQ1aTWWl1-vWUVkHtNkSFxqnU2aRtRMLmVwAHXokiFnmyO76Tu3PYejjLicipXLP8am4swn5iT3OnCsJeCZY7hf2D3Tfa2wv3jFBoGYYxUPWSk9w0wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=lQuKf8ZV-Z-gNb67V5RC44vQo_YYXRlS3f1DPhE8U87QXOmepJ-e2txDTS6ZeSeJlXKVtrQuvL698Lm6ZVqJk6vsiY3SJ_B0jG_ZLyP0HumgwvDfMlaQFQwbffKMYrzRf7L6PUnlxHKYIGrEk1CoUB_g39VVB2m_SC4TwHrfXh3GWTbGWoXXp-_9NzF5_ehDai5XUs0_NnFGnoLlkludImKS_oBldxuJ9XzfJ2AkCebR_iOB3AFCn8kxJsgWqZEUH-CPZdSRMYumXD6eLhPiq-lQcm8Dq5uB-GnBt3nAymsdOH9It4YNkVpYvK9FraHuj9cWhZPlioy_96vomuTIQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bulvij45AcTGXTZ1FnkEMOuMIF7ma_P8m55cLBBxqRKU2mnMiO8qQ5CXJLuqKrXRQxUpa8djzCFmJbPwcOUEjLHn-7FX1Guout6fzxCHaK_ylCYtqVFXdE07LyFRy5WXThv87Z1X0G3tqlPbIt8oyLE0T2IqjxXD6nQB1Fu-ekQJDLuxjlGt1w0fOWiCev48fwDyvYUqt3KvS-XtcocXN_Vp1QMHhDWQ3f2x-Z_C2vWaFybtC8okrzpi3VlaZ7ZBBUXRuJTq1SesswQmLvToYpkEnFY--sUk80SW7nxajL32G_A4iQ5kuB6pGrRH78XmdpAzAmUdphk5wnPyEOtybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb9HFdSAm0Lyc244Jy-34BFoqExiqzJMRYefV8zCAxH5O49SjXapdp2FUnzivuql1XfIM73C2_6mWsr1RFc7i1L6sOjVEUbqep3e47WTFzzkxaL9BYQgEHwf0RJW23-IQGJfOv5DyXr8db9GNe-9WXJemHLaNHYnxW5DLQK_g36hKiPMnz8N7Dg9Rfug1k21iWCcGxJwD6FQ7tcBoOhZ99m0wjdHLjwJFUt7DEhqWfEirbGiMcglVyWEUuZkV2xz-aTWiRPbUyGSNFgxpea88Yl_4jHiwD9283T1IgvuxT7Kw_QguVVSQJAkj01EVGvTR5x9FWsWYMITZP2Vkq9ZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey56noqRzdOHPf0rGC-n3KPaCuuCJ0ju6VWu52kjDvtW4w3fjxYLJTukvF-mxxNZf7abWh2sDnFWnMDBLopxGBwNXIWiupUAdE7R_3Oy0OjQmVu9PIeP7ONVJqd65rd1EgDl9zWNe82CtZcRGu0NsPpOjVEGchAUz1CbR7vE5PaKYkXEwKysszqjRQd9Ab6t2r_G4TLaxMDa1lsmrt9OMgiUKNrfsShf_5rhc6Pfb8Q6y8fYTLaFEVhuKiH7nQgPW2B4iQmfiKzMJARbrqwRXTEXx_Tu-TGRrjWnSXZY52XUZvVsePlnUPHWiDY4m2Xf_qwF1qKqs3ADioky2pr20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCaCdgzPrPTckBLiGH4ogIocAO4xKzddaNiwWTpTT46VyZmOkgLrLg5DbyVswGH4W0J8Od_vy8eXHNZNZLbiBHb-RryVSnPiDODoXiC_x-X4HsFonVBvVGsZpfFm6-HX_EvRplDlWYgCwVOf-ylR-yW9DXCx7MqogsVF6pEUCbIl_iyzdlIi_y8aBhIBpvZlX8g8z6reZDsY1ppbhBKuUzRxhs44oCW9S7vbA0IDB_92b7Rm5BOQSeTP55WDAEiq4BUpWytiRMgMAM0bpj0lipxRxGkRz3m2iMgxVL1GFyN63VynltZ2NCzFmiSEJEHsON6wO2tmkX_Au-5VBUEeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewi-UxTLZ-rI0IOPHEENlRRqCG7bUmHi7gQvRdM2lEEdrNLkevJ5BvaY7aCWrvqbKX2_pXhmTdFzK8PO8-X82BEztrVIV5XpyRAFxHbAdDp-xuq_786uyhJ7Frr3cls0fGE_HadtNn-cSTzxaWxJHc3KqctLAoftIO1jAPdo9SqSc1P-eoGDBTGh7qaLaexiISR41is1uwohn6XBL4TwDp4a9sDDLRF3JkMB_83fl9aMvabebVZV2FpSvdLOprgp1M_HFVcQBe8poqfQKsTO6O5Apddat4MvW9ZSgkYvl-2Vo8XfZLJ25VmZTvU1NNL-ipyku_JmN-Eu0aaavVnRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5RYf0SkAqdghInfnCo6ZxiiMTn0kE-GfsWS3nbTKuNCQTIc83cTn8_NfqF9so727gRZZm9hQ61Ljr5_G8tt6V5p-MiVPikl1Oj93REYahZF5LwXZUsHb9J_7Fk629vMzBIfMfIkbKRnx_bY5CqVmbtCB18HeB2JrJWY-svOkB2hKOSipEslfYXhu3lycdtND5aEcOTvj84P9iSw7L-jXIXHY4sMT3tuR4AGrZaJ-11Quf5fMt_AeXyi-4D483dA6bcgl5GH4ix8YcHHSHzJg9gcwehl2jIP5hHXNxTGbrdsdhza8nJG4H0m6mQMp9f_uMhDlEHdzc_clq3uIbs3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=lvtLBCY0ojrko-_KUSZXZ_dwjZ_YR_UMedZk408bGX0v0E3kOM3pltQi6YOZd6gS3dVvxwHL3aOmsKzxyO8FP8WHlZNRyJz-oalJulKdTxNs1oKPwruTJDr8NEORcHLDbN13Peix8TcI3Todx8TeCemTtRLHPmtgr84A01ff_bf_hThAqTNVS9cfB_cqcgCSedVWjl1YuSdnCULcGAwQ3gXODvYpXHkiNHZZoj9VnXXiAenjwuyVPLyAvawG58NNqc7DqcLzrl5bVnZNF5yDj7IDjQMAVjSYZRmKScRF3LY36FRBEx-TuyPMlqkmCxmA03n5FRgQ3aZiCiwZriVgog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=u58PvyyW-aXc3CahdneMcU53reC8ajsb1hB9Ktr8SDHCOHlGLwvYpZ-70ozWmcmlldQ0sDO0kqxQIYO6eHhjs4zBKETrq7Y4HRc8NzJe3WvFxxRZBtAB6d2klvSAcOVemyv5j42q5wUt6bbYM0GGGScbLVSa6lyDyjry_xpnh-8R8zUwO4hwsj_f65mCIIGOGiFYLR0QG5J3ZVmkDIQJwQzqPiZKeopQvnNfd0ZWzOjCyelYUq3SWR4Uw7IkeQJBbK0_hP7VgR513Ht_e0jHcqli88CpJw_czhkGAb2X0GjkNeZbDpyiyqJxYATi7ziakDGFc7L1pNicJ8-GND9pfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=u58PvyyW-aXc3CahdneMcU53reC8ajsb1hB9Ktr8SDHCOHlGLwvYpZ-70ozWmcmlldQ0sDO0kqxQIYO6eHhjs4zBKETrq7Y4HRc8NzJe3WvFxxRZBtAB6d2klvSAcOVemyv5j42q5wUt6bbYM0GGGScbLVSa6lyDyjry_xpnh-8R8zUwO4hwsj_f65mCIIGOGiFYLR0QG5J3ZVmkDIQJwQzqPiZKeopQvnNfd0ZWzOjCyelYUq3SWR4Uw7IkeQJBbK0_hP7VgR513Ht_e0jHcqli88CpJw_czhkGAb2X0GjkNeZbDpyiyqJxYATi7ziakDGFc7L1pNicJ8-GND9pfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnpWzRn20eP4rNOZw2XlOkA9evRYa2jrtLrnfvcBXP8-GauLXX-ZgLuHxAUzczcE1W1VijQDsaOTgQkXYyEp1mQ0tg-aOMThKa1CkVsUjgegZExjXxFIfL5GpYRWVBmjMwio848ZYecUc2T59GFRrSRg8yruXcBS5qYIPPkjEVZYEK7irhnvta_cZq_k2VJI9LWM-OFc2ewgI3XhKTRPGwbyVPDUGUgENoTh8de7qOGNZmFbEeBwkzu0DNxKm4e8OKbv5cvp31p35POAI2VaPT3Fq82eG5HtdBe_llivTUaJKR4CGE9V8buIBVn4Q8RwMOAqDnGR_B0qMXz-j2_zMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=MbbCrzbSzgUvhyhG7YEwKdw_zPPp6PPNZN2BWU-shJ6buAOIrIWIp5L2veeO635QpQYiT2iLLjjKb9QcUyjb6ZKDdzTsSirywuon80BYCI2cbmckukRYSUrDOKyOryUOSo81mA_bCaw9IRw7rrEKM9WtUwXNW4n1FV3hdaS2KnxxHTevDm0ZE9KHukfPHhqOyionqDtZgPhHfX2dMGEfm2YapUeG_0gJe21ULXkeacRFAytRolLJ7MxOsDoYwYKLuxHuVRpwwBO4_GkWdsV_szOpLnduypmUGf3XNLcmJo06Hgs386gtS7lIuMsNbeRgKnPkA6GXwvOcbs1fNArKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=MbbCrzbSzgUvhyhG7YEwKdw_zPPp6PPNZN2BWU-shJ6buAOIrIWIp5L2veeO635QpQYiT2iLLjjKb9QcUyjb6ZKDdzTsSirywuon80BYCI2cbmckukRYSUrDOKyOryUOSo81mA_bCaw9IRw7rrEKM9WtUwXNW4n1FV3hdaS2KnxxHTevDm0ZE9KHukfPHhqOyionqDtZgPhHfX2dMGEfm2YapUeG_0gJe21ULXkeacRFAytRolLJ7MxOsDoYwYKLuxHuVRpwwBO4_GkWdsV_szOpLnduypmUGf3XNLcmJo06Hgs386gtS7lIuMsNbeRgKnPkA6GXwvOcbs1fNArKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=VZuXcmKu84T8fKUAZNMaYIILchmEl3eap-eLnMKo23ytbqSlDTSFwbhT4m6OGTScXtjYbXVO_CSttxSGi4frtFJjR357GkuqSepjzGViKbpAGKp9xMMB_QGzZRghwsixpjnDvI94MOD8Gj0Rz6GcXUScReb5JqfD0HjTf20gKpt8D2IsFIDNvh2eq4si7JUO2LJQOYgPg8ey4zslGjqFEgvx9lrhvkQFxko-3__iDnVKjvdDiolLe71Cz7zSXOmlp3gEeKizOU3tMasjkaV-QKA0-64vu05jNbil3t07NbHXgkk6W8fedf0lagg7X8inETau4fSD2HQJ0FDc2xAf3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=VZuXcmKu84T8fKUAZNMaYIILchmEl3eap-eLnMKo23ytbqSlDTSFwbhT4m6OGTScXtjYbXVO_CSttxSGi4frtFJjR357GkuqSepjzGViKbpAGKp9xMMB_QGzZRghwsixpjnDvI94MOD8Gj0Rz6GcXUScReb5JqfD0HjTf20gKpt8D2IsFIDNvh2eq4si7JUO2LJQOYgPg8ey4zslGjqFEgvx9lrhvkQFxko-3__iDnVKjvdDiolLe71Cz7zSXOmlp3gEeKizOU3tMasjkaV-QKA0-64vu05jNbil3t07NbHXgkk6W8fedf0lagg7X8inETau4fSD2HQJ0FDc2xAf3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9Y-AiGHcXwFnHHH-Z10navIHhzhMCSbx_xvLmeC9upGmVkT56LQZ22vW5cyUvq6YIuCO5jUexmF_iW39JXedlgvj9UpXvzEkgAmXpMQxdqgTIMlRlDBF0tUCY8qkfnqwyBr1mRWOkadVaUydlj0GiXFuooKT3Wdcrnk23vNEd-qL4LhSm40j0fC82LR8kT1r4iAIfeG7TUdLCfCFz7oA804eh-DlR2Bo5FnvM426foUC6YAx5h-FQhoW_owHKHJj8z-VMefTd2bST2vRP2eFwW8hqeZKjyJUis_nJ3ArkoyBDAHeSRgWfsWLWVN7jkqO4NP7N_wk1_DYglc-PNFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6CKRAET_vMMOPC4JwyTIEA15YUevjD1XFiCJcpH6XnI5ZmTLmUjjw5tfqF8_2knAJAX6wMKFK8Mn42F9YQIZIVVuG0RRNAzRVAMLR4GLRrgWVnSkaFMWSr26hVAszJ441Ptpq4xedaQdyhuyZ7YFp80B-zOKtaOgwdJRHVAODBA9trVJrtOSnSco1-HWAbv9cCffXXMdbbRJ1FzukvwZLS2G6zJEFM_SJcNaIE4-i7hc6gSGVpE1tTjSWmgC2KfvUwp3VV6XZHLiPjfUJl4jRdz55C9PWql7j7a-cwW4WvYDZRx1l_OY12Cx-tGSRHUN22vt869wpkEzbooNo7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7mKsBkuQWcXH8h1mGbDhiknWPOGUoILKFdldNBNWWebfHho7tnG6RJIZZ7k3tO4TNOM_ouhK2nE-a3m4kfpsppO7-zmk9Im788JBdQGgJNgZJofI25AOgulrGwhtEWraHrxzXQ3bquCm-iPWae47Pjf_7GvGulWPq6KP49WElcNLYYk1A0OFAyNw8dco1LIMeISffuvVvncfP2ohHs75mrl_3Ygin5xUitiuvSAkxrfXOBBFRiXx0Hgn-z6XubMsnG7OsFG-uT7qaDvoXNydP2UUplAGBOZPSGmynKKJ2y1Tf5TSdZL4iyRjj9kSC-Bn1Jkh0rE0-L8nXZFGjnjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=oImEN_PO7JlHi2drVPeIoGcSQjNuH_aIEHpVwANQAIu9O8JMBoeY5ug6-nZIf6J-Rh45mKD7ZUUXCI8tF__gJnMbrRfuolrnaKEDg8qalnpuZ1O-jLaxJpq9A9cE6PgFsyTtod8upw_C7H5p8B9tIPvKTpSlGtjOfRkPJi0Dq9q9cxun1bqXCx4VPjNad4FtiyH-8hpodTrqEpQ56MebDGCjwvtJqsWnJVHgIp5cr865dIMCZDT7wHibHH9jo1for1kr00vBOxfNYEe59Fk5pXx7yO-BxKUCCuk-Zqooh_2c9EJ7nwv7024uQ1v32XopnRNpO_4ZGGiAGTQfTO7sszsXqxBCGbrWDH7vT0xSlifYyY4Ls4Brj24qJViS-bgsQpgF8v5yFbWPksLoVgFCUSYzDMkYg0s6u8IkoyWX53F80p_NKcQMWxgP_206VhlclFmTF_fcusp79tT08EpCz2Kk94Ua_L2Okd_S7FRUsu0KeDgSmAdcpyMJjHdvpK8u9R9OYFGkpXIyvs0t__j2_d8tO4GgOAQTrZu67O5jerh0cvcjO9EM88fuk4H61n70KE-7TBxejxZ8QyzYGL1B3Qqtm1UXL8dLYy9swcUxeEq6avvGBvRCABGyqWJxjFU6c52SKVpgrUB2hfVYTVTFUCgUxf12WsdlxoSpUFGE6-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-8xRJclFWl-wKv_7MUchXEDpik8TOkcL2zlbzGibPyDrS-JbldX_9u7S_SLMdtefLcPjQG48ItihYcUB1ravfAlQjWIFIYRCO397KQh6Tc0qn2bGAOuPC-gHYTOL8UvRXpDH2jzTZ8Y89s8J2CJJmTP8giUWiYGCBybnmJTYae9UCKU8KG-UdFFdXi3yOv2sEzXnHtKQ7EWUC2T6NPtHZeD3Gsa2PpeXW6FPcS5nDZR7MXiqeknJuiB3IT7ioX7x4IUvsk7gaoxhAbftuflwGMpf3HVbCuCep4CRjJxYi7VjkgXOosOE_-UhPGqlH-ETYZhypXN1vxiu1ALqD6ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBaNRoi_aSkdk4kGTcX926Di2RRhftfU-u7nqXxhnHiaiomMAE4JMwPxUhWJz79l_-A7eFRBwFZrXSeiFhHTiqqff_C0rnQEk9dVHZfCYt-f29FtZkHBNTOl2yigl1fuwhdUB5xGvoa-ZLWGe4D-CfSaNkON_fPz7Dmo4KwULAvVgAbTqD96Pnx2QCShcWkt4s7EPvXJ8GHr8i723KYoAA19FZ7w7UNSn5UliTB_gZ4Ay75Efwrq-bvY0fGt4sRce9vqWcIcGs1m4BJazP1d4o62ra4nQpzOfM_S401cZ4hNVFkfF4OJi4V1SKx-nbrfWG7-QnzfRiRzYwz6KTbQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYGDCrG6AljhxbCh_HMfoOeoaBouU7lhGIv8fAYk0u2dSyAHTdg3mr4guK45vnceEwKNBoI6p5i80muubGb_JnMRx2hRxk1yQaQA51sbSZZ3F9DCyX-lIHg3oUpjOlW1KpEEh0KUsj7OJCj5P_FBpUuzgILFGgyV416nCKrOIPlnQJiwE2Psi42vSRgWikh6EAYJSN6gINgwHKESoo6saIkVgf0F179lmF7vDlVF9lLzWu2o4hSiLFSYfV_5d3xKHKBa-R8PfNzEJzV-aHHxn25LcR8tqrdIkUN3fBWtDuh6dTeVkaspc4x7Wwhx-REpMEmstjZXyVcjUIpP4wFi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRAmecfDKlXPuYVlDIoU8MbdFLenMJyOr5AK1FQtCDHFtD9JxhSFOCUV71rsCbmQhQv25xv0z_X3odP7qmrG6LAa-bUEQe4-SBNlmI3ZxCbl7F29trIhyPNb5QHzYx-Cg0rKFseBJGh5W_pd13EQ0Olyboarj2tU5GB2Qkd_I4TCrb64ydmK8pJiStfgB8bbt-aLeOcJ3fKoXmSZZqME77lBx8b1urqv-SJwFCFxjwckIYj0Bf0rkeAzr4gmIvcqr3ebRYS1TUqfcNXDTD9wd0R51TGAH4oUgBDz3fzaEkx6K6evGnBi5J9bT8MXBPETibLCsMQA0XRbyp16i5zuYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfa8C4ekVwGpgRLbqoE2z9XuNwn9hai3QNwSlzugT5E7lLb6BTWBHdlvDLq2iU7t-xoWmUg7trV2sNs5P239Q4b5l98aEPi1wq9hTGK2ADOpGa1KaKhcu5zF2ahvQgy7-uPu8Mfzva_see99eBQ48OvnoHYdaqIEber9gJRezP93Ag-lH9z8wJd04UqAA9bZXdBOJdCl6Dam_WS4rl0bNrkLjBAQQUCA2EtVrj5GMrlCKWjH1_-R13Y0E9fIhCtTC0EnfyoFXM-ZsUeQLvZAKs_xNnC0DU8YlNv2LHaSeSK7Yoo5UVv148XZF1ClzFb0uMmLna1cOjRsUE4ANuMaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=l5PumpUKU0DylDMWNFIiisj6iWCZfl1Nj3skaBkAncLVMj4RzYp2F71Gg2Dhn40XGK5JICir7nIb6NRzH94bQSwE1ZfYYdEbwgrcy17MHCvyrmJ4RGtQzNYQ8GB5QGSNdBZ1xiIpYrpNorbEoxR3oxmbksE-sNCY9J5Elo1NainGLCqdqGcYYHNyl3FBy2UwIZl9gcSZdeupiSiLUQN9TaUwrUgy_3W2lb2R-kv1LRbIwvcc3i8yUnqUBdQr_uWC0q1QpBfTmW2NnOorAKl5G59O1kjEIsyNFal5qGyCYIHNMCCky_PIoy_Ymqg_UHk_a3ownrXWccF2CpNNPPAM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip6eQHWHApF68Roh7AkoHgplyBJYIWaqGSonTjik--AjJD9wigrs_cvRqZsiRbUc7VS4jlx_iDaPikkZ_GSfxEWia9V5OXmK6S1qRGOBV03-K-jYVRCUfDNh_JlujjZ0m2Tg5NVHDTOu3KpG-_ZACwyFFb2DCrOaN1qIk9CZmaYD67_UoXk2ewfA1TCzYZI_6jd15BIyBpDc6q-wlGLnUSPSmkhk6-oEWGH5Tw67tU2xlYrOrpL5qgVaJCpQ1p5p2w1pZ0QgunzPADjBOnxdC8tqRAESN2dwuEOASzYxAg3C_Gwvo069pqwTFbUeklNkDJH7j1dN_6JOO9_nS-_J-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfPLzcoTbVk2O5Lvep4sRpeLRKmFh2mf_ie-CiPq25W-CmwLtv_aBw0WiXQXIpYMTHglTXalUGg4v-U4lxNXXWRtETo6_lOEa8WSkfJIKZExm43p96MfVMrKY4t-G_yrvy3gmcxbbDWEtLyRVKN72QlADLyAxn8L8RoW1JVWuQdOJF88cyvo2-HEiR5BW0A-o2Z1-qYjsEMGDDScr-ivIXbwqUWf8A7L227-o_4KgHQxVLiVl5AhxljWhMTblxI_Baj99V58gQf_Nu5lWYYdpn50cnuytE1wPl7K8aklvBBUBUvWjcZdkY20uzQ-0j0GoZwESJkW_gjwBwkmR8BBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIJnh1lGly2nQMFfaOoZkqCOG5OSLVmK5pgp8hvUr72ji4jO8RVS7wnnnHaAt5LQZ_FgcPja1FIlj24a8TW3u38hD6j6DarR9TFXOGypoGKFI1rWFuc4sDrG9HZKwmRhmAN_S2P5CsnnPVjA1mfyy1mo55084LY1uv4G3gDuswXTdzJTOs4kdhyz1kMakGSLi4RpayGHxcuBnSQdEJ0KTV7hra3ASZxcVK1jl378GNfgK_fJejOjFm16z_Jc5mAcARv9Bj8E67eTrK80bMNNLWMKAAiXp-Pu_1T4F6wlLUIACiJyXX6Xu4CTBuY8TNtwNT7izz0KHrsqidnRj6xYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=kijEBuHNudk34zpjHafUFJ21aJI9n5M2DSEBvfgyrmOF1pMd2BZYrAxXbNFNuLAJ2XqOhgyXdF9p1WDqWoe26yi91Jb7T1UsFtpIAZSjSzLUvm_i9fDXwzbp8xYNxHrN9CIdGyDe-8Y0JL4e-71NZYIbcMP8DBtnO_kr8EffUsKhNwKv5KUcI7_R3gfZFnmJRYjAjHgRE2af2GCUiG7Us-70dDkYm3XNiabIDNpLnv5DOhHI0YlM3RVuxZ_TQK9kiyGPnsY_4aEezwh_UgjnNogpuvy8pMRHoD8gu77C7dDNjh1fHu5vntYb9iNhjhDuCh-laDs17eokWD5tqFPEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haYJuQGzFUGCjn-7v8tSzDv4ah6EOn_xGs7iCaot8Kgm8oXyn27s3vYKmCC_WICDgJko_dt0KY9Rb8wl1J3gLCUpbHR-X_UJUYS7GcR3TTKQwMhMbSIeGDxiumm0Qp-kEFB5_bJSg8hhJsH_frQ3zwwC_HnEDWAinqYt0kYZVc9RMiptrR8RHHMfLxCahhDU8UcYRz-DGHZCgKW-5DR2D4cG2fddLDa-9Io_45L1V6K3Mv8yedS60Qlqi7AV20cWfTCe2C-J0W0jAdg4GJ0MzxNpTL2KW1LT9AFvlGsU96Bgukvs_QH_KumynI13SisHTBYaU4b_nVcXyTxpBj3QJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mcx-SrEfdcONkub2sZRI0vhuH57_oiHI4wV6JXi8qxKU66HjYjU2wKx2JLZCEh-9CWbyASUxWlPFcX7uj5RZucObs6BAQfd1Vd0BUicj0bZmAzt_HM_ETdiBzKCcdD7LM1jlJjc2lI1NSgW1bw3g1bmIPg7zOILf0IeubxQL6k_eKq1syf8w18a_RbesD-927aZrIY8glQs7N4ONki3kcDh-1M6QrLv7Vl1GLruh7NzXYxolZjSKQ6XFK0Pzmcaostr5qu1gU9HrPIsfejmrIwc7mTfiMIFoAH7PHXV5Miuhu1XvPMw2erBokH68zihwE3OAp5QbeAvFbAS-xfcsxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxFdImJ6BHSvbMqfEMuhtepnbHYRR9aYsA-sx1sWYOTOwuP0o8jWk9RMfk8zMaPnRm3KgCVy97oXZ2QJXcl30NVcSYClHCoLg_nAmTS7R-iPPMbhsmZtFqA-jpPzprmI94-Z2dbI9LTB1kDTTBCBzOaR8KAo8ZsqUTvXFNUbnV08t3qzL5ZZSYJ8O2aV5REkIYMD4-urnnKeDFJ7D8pVm3BEFHrts6Y_6CcERTa7_nwkHkLPkXM4X6NY0VGdXgaPchBWFywzYamQlX9ma9m68BvSurh2n19dgL89jnJFAqWuePyO0YV90agpm5fmsA582qsB86fD-4dkYEsBeiKK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keaqzuBCRk3rm51hC_ZkvZpYbrZvbQtSrCiI5K7phSvpKOKzgiBOPNdr2vnkP1BVeVo2ZhlLEg5jq877HRMVM6DVQO5IPzZMx9N9AoclI6pj5OlQlkMNTN8a3-x5cxkRF9iAn8yGUEWv0kIJFBDj7vTFjsZc6w4do_2u9Xj8S1Xk1_ArQd-vxe2FA0pay6FUIzB5OWkFagAPc8d8MmuABgfcHvmK-XKZjWwx_3E2gFf_qixenuRhqN7UgsAP3xyGDh8p5O16mt-9cVtQyKsjSt5-0gASqKWGvy1WLIGKT11Q5fW1UEhsFJ4niCOvJS0RNQcQ6aOYDnR-3StaoBPo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT6wqaMqEDN0ueTnK0oJdshJMFSOg0kANuehqnsltCd-91Wz7glWCN9Kf2LIWFFtDaPj3en-bXIRkMLelMvAT032ifN5xX3gMAOsx574DySBOqbtlIvQHQZv_NqKddwtSXhEacRdCIuLQvEJqmXPeXmTgbQ6T6zvuzKquZx2fD8co05A8lYQgoxMoJXrzWfbjV8RhtpJMztHVjUBZtEEg9oeX5GLtpsStNMUpSl-a829wuVqjYJW77DJFJeX_nbaL-TxBzLSAQGyeUOFOrIosfdblBceCQsM9xpkJaXJSz0d5FO_PA1uDrj5z_qWYI6V_ce0oXTnNlsKe3VqtT8rmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPn8QApGdOh8c6IIMOP3_wXnmKDCWH6-NXNSq5zgd5DEVjUdXG-Hta6zjiEl-cCWzWQhRRJk8FCf___X6wccvXpvhVeg-is-IyBYGOkUv-wmajmaWitGwQdnL0wDuxgkcnALWoS10yYr6Hq9sFbh984SkRp9sclv5HRzxtLCRYfwNEMoKE5UlCdlRHDlsiuyD81Bbvl6klwco0xvnbxIE-7p8agS8-UA2wEugTl-_f_mOG07ooV0cX1m1Ytgo9NE5mruQymPVvTCOgEqyFcjzwd8h93ljHRq07U4o4G_EcVJZYM8S9ThodMA-YZzQSOfA8yvy3oPx4MVOp9nzFw3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6Eerm4-BOZlhrUvDhEMXBp5De-FHtxjzsASfgxFb9t2Q42vZyES46yB71M2mnk6a6KEsdbiNs_yONekXTBFensFY3K-mPsRtUIqtkN236Pwh-uS5XEaNguGwhfD6IW-_lMaT_owUjbvhLFeWndZ5S97yAOM7j_1Fy7l34ltpPoZXl62ajfOI1EY9X2UZYmqM_3EJu8j4AEUsZLL2KIWo4yPWBajF1N_PRsxiNERM7T_oZNGTXxY8bQWQR27zPX-AVaKad8XLmuQTUQ5Bh8gWbofDbjw8jOGd7WGL9qZEB44Dg_44UJ8FuqzJl-_CTsR51JnnXPHIX1Up7fUakLEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ub50nK9MATCktzFahni7g8xB5mkbUdSSzyXYjWKbgdAPQGrY4qhCIj2RqwS_dQwxjm1yr0_EEJwa5yhXBnQhfh3Ec2i9uQ-7YQAygd1EqOwW1aKJhKTtNuD_wm5sE9Z8SyzOGfpnJ0U0qbGGkdTp6tTBmBwsSAmGW0HaObuL1BZ5ibjcTfvC6VOP5XdnvyRSuKI-MIWziWUSBGlQ-G0On7Pq5p41btnAt4gkVQs1UUL1Rva7B_TWQ-6KLpSEgxZm1oBrnV7e_tCN83Qk2GhFAAux3x97xHwoJY4auNbf87khPBTJT4Wm2T7DcHdY9Ozdn0Vjkn6E_Sgt5xrcQ7lwuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHGfs50PoTAMHKssowGNqmF4cPpm1F53IQLjjZf-7sTwpR2Rskc1NqyjF-5JFYMyNKzJiQK88z-twT2OATK5Y4GCRSYwu2fjdaKzSKXS5w0-ebLZ4EdYM2rRiF6KysDJP_LTWhmmx4f2c7q22mThtgkikbrAnlhQwL-zyhfnoY_TXMQsYuMuFlwztCnCd_hrL5x7fcgX1SwXu_mQwPckB4TyjZvec04HriQfXu6Sp_EeSx4g-4hbf8yldliXtna9wB_p4ggKgGEQAZx4-lqbSQsOEKwdUjH5XnXQ1WOAJjDEGjARUehB9XyThlvk4u3to0UJm_z6HklBTvNZ7CqPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYSInUwwj7vNKeooxfIpwSvzt9OiubmtuYr6dFLnsY4281hfAr3EoFO-56ZXV-iINcasCRTKtsZ9DCfQBacFDjKWM1D0YgkPISQJfXH19XNCOdTa4qmw-v6hq7NbC7nrpiOvZtenEnsP2T6r1RZzg8i5mlCK44t_WzIWT_72B_QFCUUZ_Alk0KYAWowMzhcwanbgMYgXRZ1uX8rvXD8uwUaa-W2NBDS6SplbLpxEIsR7Db-pe0gSm5dY-HQ-67dF_27yKTdCyNkZoXbVdEGJ8fvjzdJr9snHJupZE-c9ddnN8aGFEdKcItLvf2cou6t6F1evBWa-Xcx1c-hptagXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmzKP1VSk459TpbyY5wbnE-ji2nuZQkEo6yGUUa6LLPyaUZwuoA6KAoIjdvYk4oNRCR5yJNgk7nBC5ykUqkttoEsgwT-0HuUFRT5odZjBNpzvwhqZkjUnXTUGBOILvBt1xdfJcKSigGQhTkaHu2opxwk0wGCcnOxLdTHuUnpOwSbnAmGH_be4lo_Yn2xHuSGxRkIpzi-d8jJJpaBgmELV4YKWkE6jQSlIr4t8V0iihA2IhuWEywqZ5rCdQM1gJsZLu8GU8cEKKFTibiUyjrQGYq2uRMoBR4X_nRQxDOYbBWYlSzn334OZEPpqG79sYKDPNNFChNSNsKspxKxgWJeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5QFnP-FgTDl_77Lz-6Sr_GHRVl9i0rVrKierC-nVsjYpOoBinW_f1FdxGTC4FTMh035q-P3iRHhrOJ9ERe3HKjZOmn43A1CWRqi5dDYwqEO5WlcK_TnvDtHMPmMSQBVxSGXENFtEEzmc9KpL5P4NuzSlM4dx9mzvOEqPI3GHVYW53ueG_aJJVaxuBPVtj2kuZzpxt1ONIPf_PfZnx5Cpl5wpINc-jJ1O7qjNKHMO8qQ8YXpdKYP4KOo_-C6IqzSgCYAb6-ofgel_JpUh2O4YfFRgNQomGl0KFKTTa4WZlLI3hBpn9FVwGBTQV_jBSIV0uhugAImq0oNTVO1r2r3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9bzjr44J0ROMfeo3tRokHi8HAqAIb2DbggaLrdQcdBo-tQTCXPvG9xsRhBZV-tSOOPOsoWMD3u9SZdwpWABeL7wtKGLYEnrvhurTIkvsu-rNwzeNceBxYHyY8g6dRAfCNFxO6ro6cnxfy-OLKOgvhfb2D_LDAGnwbKCyp9N53dS1XAhNAQKcZQL7ZAgH3XiswCJbKKQMAsNx-zDR0ZTr8QAo7Rg-54h57IVyQe4wcbOphLTgrVvlwMKgK3JlUHP_9LBGMCUfPLKX6h_PhQNyvdgP2i-3gOzJpFRNZ2sOicEdgUI16VjWMnrNYnfQY_0ThlLXi1hn25D5Rn8XGU6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYVWEwfxbp7QdED6i3AkAbfkz1EbtwNS_LtCOdDuyWj0ATdPp5qYtQKJse2VygXNg1gAbvoBVniN1RmvYmPAm0O7qVSUCVFEaXCT1S0eOjrl6MkrVJIfzD-jc4oJK200a-mn2Q8qC7G8ayOcFawIeI-pxUL98ILhCi-U93JcdVPlZ8yGA2aRS-4EnNmmxsfGaQFvNT301YV-3kYDrOJ8J_h8o37FN8TY8RVPT8KyPMmXVAUpBZVBmfxghxc9XUDNRWptnOgGV3Cw5IyoF4kOmDCSVK4OmE_bQKVWcs0BnhT8esO21db32Q1g8YsIgnCClU4vWRP-RNX1ikN0yOgf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpwIe1e5yt1jWd0duyidZl9WrcUBPEuPXRC2-YUp9gL0bpuG1UzVyiRocg23E3dWjAYDnnQ9iXeLecifT5oYD4HKCKp6bYEOnOp-u4iipc9YsMLr2HrsT6GuonkqTqrr-udNayl7hmqtCe5mVJJ3LGZN0nR9sGw-9-KcFc1j830Vi3xU5KHlcAvF6cuyCtBmf5qm9PqPv4wZo5kK6bZpuD533-BBIv-1awgEeYRwxJRoXkznVdh3p83jeYgL1mF5stCF36T2B6TB9QhUlGyhhrcBhWS2wSxgG73JtUUCm8R3tD8UrFYIiifbhEdJZFcVcO1V90PfuvyvDVnSluQQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUnTELzUcW3CeKP9eQn5uBoGombcYsrX5_Ixru4k7hBv7EnsJqAcqMKyqZOKCyWK2EsOMKBvIvaC-NWAiAQr2rcyVh96BpCK9FcrPckE3E2d-WvVKM_I0VN1_78iRzH0Lgq5yiRzG1z-CuCZwl4l-UW2_BfanULcDOeYi7mJMB7gKDKQlLzMAe6nb3SM33xbZojCmFWUc9JA-Y75OPhuBxmQWjO82I4UfBcgKMqThLzhEwHPljvoniE1zp4wkI3PuNjuL6WEvVkMjF4ueSXl0nHnXBvGN49if1i0t8oF8S9dRhki7Zw8mMALn9_NluEXdfpZ_btyGemmn5LshCZGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hykWMzxFOOSUi3oNvZW1-GpntG59264-iZ9VaAml4ZiCid9U98pSkflNdPNcI5i_NbfFZKxMa0tzzV__MrSiNnW9VGKSw87Fwqsb_6G1s0dfOvh1XTTEJ0I6KmVVAzIAHt8_nLANjufpPFHT6NvtWHtftwEs290Zxvn8zStTRmgkllrW594Narsx2-eW1cLhJaanRi_6LPBqJAWV7QOp-WxsiKeCjSVzgjHxqMvMarH81-KD9PbdrteD0yTlN3YAtsoo0lXaS41T8QZ8_Fjo0IbvR9TzM6TQvMHJ-Y8P-_UH_HAkhl9UCYNoyWUzXghk5IaWwYFirUqo419fsx0s2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdok9yhPlwFlPlb49DqySmrVeHi6UCOHbqflPUbM6hjKt113jdtrojDTKmqMa15sIsr2g1TWUSNUQX7e8cRV7Q5tnnyT1b5_TgRKlf6niJrSGlSVnjCRr8LrNs5nicc3xC4CU29klyG3zzaEqTyGflnr5yTJTvVdJvYw4V-aKgEy-th1dd7_ypOvnbR6Z5F2B8cHtMg5OG68q-kdwsPvTGat9Oaz0TwQOqxr4PNl-W9gqNkoZHklYrHTw1YuOg6b2svTPwLnh2WQAVbo1ZSDA4Rk-79F8URO1o9rzSz-QtAGp7-QmPef2KL5eGBudf44-XTpREyZ0LppVBeuGmdNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWFbmYqqtogtj10KJBE1woKNERYB6RwmMuVowoUWhQrU3hPlcA9ir3aONn7RMTkgijbpC8-6Qn0kOq9moyLh3rRq0kOr3KF5NGnRLjjTVejeBRVUj7pddpmSW5xCPDwNw_z2R1IpOp9i6Sd0TIN4cArRBsRTqMtBolxdAcXcdZQ-6IA-DMwn0WEkrxGBIYCrACNh5TG_Tcfou50S1VG3k7Z2xbT7TeP1gATEItIfwZgnY_Y4iKT97I0yp04p3DM_e7XDgOx9-AhVmMNCvj-X75zm7NYJGLArs5ure9rS-TVnM--SJeTdp7Io7pIe1zSIQCTVpuoyFUcLo_a0-mca4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIiuFBiQ_p7RmNjjvW-AYmVnJX5kN8j-rBX1LOg-kSG0nw52U0JDiEqQ1XwjCdvQfDjEjylM5MXsglvkSJJ0o6o9MOnIBTpOhgB1T-fhp-ahUw6NIJniwZ0Su8JYiQ7ArJBi9wCTvSzsKBw6Kk3SCdH2x18ZgXV6W2smQYJm7KawQ-RGJFMp-AsjUVYqXqE_2qIt4xUL9ZMrMnF2jGdBiafZQfB9MI-6eSSf2V1F9q0K355UEswjQqW2vV4MSlxpp9sW8bDSx3HvY80CCQ8869UAWBVLctXqCUsBDsLEt6SSJV4yzBzuQmFuCeXznayx682-3_jSuc34tCXhGuZHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjtBnTlsMWZYe-CpEXMZ_oxD1n2icmZwq4MgMSlpTDIsBCFLXYbgpLmGQQksVByRPpONG5uHhfq2MMgLy3KovdI3BVHTzhMjqz-zW7_gcVK1e9WsypecQJb7Sv7ppntJ23gGyd5BFZ_VHw2oVMYPSHQa3rcaXQ4xXDYWMend6o7_urE3ZnTztb2jQVCmF3bAh-kO9Fx0CKTpA0wNqfV67_jcoCvd0Djx300aOErt6qWX4X0c1QlJc65IIIfVu33ijHE5eOcWQtfochNCcab_J3fZvjgf0wwpWFnYR5QKAn40ZDnjIgmUhi1lRwcBbLhXmhP5SPWBHAzlMPqzqnxUhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAG4tk1wWj1xKFVzBiTJwGhi9gNA922QlwWRTwc_N0ZoK81G-8b38pbsK_XVBVLD7sTwjHiySCXBsWblLNOZHGUNy9JpEl4GRKn6ZAOfjBnN89HzNwQlLcTSMFtd67qEo-Pi138WJCX_lCq4n612IjWwl1Gmcqiz4PXL3RKhWDYK6-kWZKpozvRV8zDVTCvpByedAMDjf1zm6qi3YYuCBD-fBa2-KyrD12MxuveoGtyVo--p3z8QA_ufTbjMhvBJ-NiSX2dkdB9rWaTnm3pCC0eWbTLS2NE8zLkkRXtBzIifZ8cJn4hFIZ2JLxT1IPWAPnPtd7-aXQLmeSqD8e5j4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG_lFhs3qDutSGLOv9wCMpfenBvcYpqcMIRPv29Leu8d5qER4AXRmlzfpmq-jhaEwEEohnRfohM67yyhB9WZZjInsotvqJO9g8uPoRz-LtpHA2OvOBSC-RvFIUnNE7kxAziG6DBTb89AX12WA4qQA9YTbOgf0kCnwilkUIKuYwM5HztPWRsENpu99f8SI70HTrogOgVzU68i0ll3yg7yvKpkd4OcEsk3eT1mUCMpWTwywDKt2Ip9sU1enqLgTiqwWp0C2hji6I6iusWVHqb_lGxdkGINrGwf4zfH_4o5AFrq23C67UtWZGApZh9sXkCOFREm_u_c_B9xte_FOAyGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=UBUaM6kJnV85wanULcLMKXjDiJP2twXVcannzNaEnQX6Spp39KGu5AlWCQltmoJDL0cXObH6aqwXB64ADxou4zY5P_6l-gIa0OwFw9w1Y7iH8oFf1k_s4Jnz-O2R2y5ezlfBPgNCOVDbuQMR75oX7JYhIYxDp0djtfSIPVFROvsaHPnoocPbBX3CHELwDBmh7x1bBT6NexKDhNvMu7wAT4gqGTKDgPU38INZ7jq2TE28o0ibwCPKbN55jYcmm2_f6Gy5eCR9lJ6bpWy4h0cvH0kDV5LkuG92BZfLMLw_l2IZMk7ZfijstoaPEnU3DwPB7Z_S-bXLlrhOe-E7cu3f0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=UBUaM6kJnV85wanULcLMKXjDiJP2twXVcannzNaEnQX6Spp39KGu5AlWCQltmoJDL0cXObH6aqwXB64ADxou4zY5P_6l-gIa0OwFw9w1Y7iH8oFf1k_s4Jnz-O2R2y5ezlfBPgNCOVDbuQMR75oX7JYhIYxDp0djtfSIPVFROvsaHPnoocPbBX3CHELwDBmh7x1bBT6NexKDhNvMu7wAT4gqGTKDgPU38INZ7jq2TE28o0ibwCPKbN55jYcmm2_f6Gy5eCR9lJ6bpWy4h0cvH0kDV5LkuG92BZfLMLw_l2IZMk7ZfijstoaPEnU3DwPB7Z_S-bXLlrhOe-E7cu3f0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8k-xblmDeLe-kS7Gz-MLTfUCvkq1xjtreNYd00_2AjdOvKf4DazPm_hFzfcFZ7Te1XLs4vFqhnLuwnLmZvpqTllMuaY0PtKT-K2ps6ix5yA7kFzibnV7vM6HoVytXTIVcdQls1A7vKGYlIuK-juoAqy6KK-1hlXDbP3ej1sV8q94GhawgZ3_G5okuGzqcB7OtE9Wq_YJPdEQlA_tJQKyGD-PU0ccJV1PsfXd56dz9aysEwDUF5v8DwFm6XAC8yughK2us-PoCViuiJHWKAktl4Dj9yKo0GvXvlY2LnFLT2dNPV_h8MCBzWviriAlNHaKtCnWGJUCcYDosiIqAFflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah8Q6o8F1WsqSMhUt_ZBTQaHH0y1qxNaD7qDTxib4T793Upns5V3CX71pDCiuHp0SEc3ZylbeD8oJaD0Fnb9zokTNZ2DBvJKaB_vlwIBE287oNcMZyb72FPKeI1Zujq6wD36eD7EbtvK2T3Jj0ebo1ZKTb9UFUYkCOm-_gCrEnQdW_5oTzF0cmFpevd1J2z-eFjC89q2-qcJI-9WN_ZXHl2ZLCErET4xrl1ly1ZEao6EM_T7Y0Tg6XoGuqCfro_WFYrxK7NQmL9mCqAUbCaApr8VddDPlZb4GG4YR9ZWizvQwTXELfa2GnwDnIobjZgaqsoPhWls18Pq1FPSrSBPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXROD3n8gQLjKVsSFz0phMKbGTXutlmeVhXIcRw7fnfPGyWHXdHHWgESF3f8Z8SilLFsjIQ_O4U3UDDiYdqOLm_p5KHlNMzcbjy2mAEl9qx-JZNt22FSQRSdUc-N4a9Vrtfne2hpoqU9yRbLD33sHdi-WNNOTdfGFxvsbp3CpJJRx7KGUOT3iZUvMUvtIlJrN9mXgJGSEHr-s-DqVQh0CGJO0VuDErrgrSZ4d-yTzxfqhFiR6YNUiu9wBQ-6FG0xnOG69X9WHHwDNuLlPlhehtkf9kmScrKoffqoFs_w2W8kFHwiscroaxUC5x9ic76MRwm14MLe3WpnS-q_yCBfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8hWGQLocveW8gJh0VNUJKQAJKcmdGT1OCBHfcSpTxGabe8POOyCQbQF3dH1AczssA1WIG6gsz9p0a2ZE_M7ybCHV3QWD7V9mkfAvKSrAXoKgR7SxRhckvYbF0mBElqZfr06R36HgYpHtqAu9jiFHO_0r-eIumnUU4qB3k0prFXK4YnGs4PpA45F8C2USEoG64Un3QMfLViKSj7yuNmFxeWf3SZPQIze0x9GydYYCeYHQof7z32mHspkR_arvqEYlC2R0shyDLuaViVRBCKs6IjjFD3shy4jvNwYX9dFtXYu-NUOKdSdvhhdTmos9BdaUSRs1lveYdtB114e8wfxqufA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=BoalYiH23FmEYTjTTLMuPltd74RSaKwo1G2C2JZvZdti7nx1wjkuLUooFb-YKWVH5HoL00Hzbo9RwY81jUfMDFFi_jA0aoxVrv27ulqEC6-X_2qxwe65mjUq7Sql0CnoB0KQFvAb5e0KtjCfKX4wUsM8dU_wBn9F1ygEPFVcUzyfDuYEnbfmixmP5VlcsW8W0ibCpgtC8bD1961znKpfEbxpk8SgJilgADQjsfekBAyZ7SsA0DSBqCJ_k1aZ6XjQV-GIUWKB6MFNbAe26oFqu4FApeTr9_-OAiJcLaYuUiNEvxPcV4cLJLuYy9Tb9cZTlzNqez7Kl_VNkfW7Zv0c8hWGQLocveW8gJh0VNUJKQAJKcmdGT1OCBHfcSpTxGabe8POOyCQbQF3dH1AczssA1WIG6gsz9p0a2ZE_M7ybCHV3QWD7V9mkfAvKSrAXoKgR7SxRhckvYbF0mBElqZfr06R36HgYpHtqAu9jiFHO_0r-eIumnUU4qB3k0prFXK4YnGs4PpA45F8C2USEoG64Un3QMfLViKSj7yuNmFxeWf3SZPQIze0x9GydYYCeYHQof7z32mHspkR_arvqEYlC2R0shyDLuaViVRBCKs6IjjFD3shy4jvNwYX9dFtXYu-NUOKdSdvhhdTmos9BdaUSRs1lveYdtB114e8wfxqufA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svCCBZ-hAoRnOS-R-gve2-Ofeb7g4zsaG09j2cQO5KXy3ZsR0UW1ClpR33paBl0kDsvTECE0-5aHXtOCdP16VDPA2RS2HP2R1vWCUDsch4JSPqk8sxiZdN37MvrJthExIIBdB4mA6MrU7s-JdhXKTfQgfVovk_rsZHYbwjV5SQAvsgEdU2Tz7MP77VhcOvvTBoTKCJnKOeIt6jBsJyi2EGp5qSb-urqjkf3AVTvnbLNOKNPlrK3NOsa78BNnnT7_BQdxhQ_R7WGcZ9qfUBjdLi5OtHqcbyZIS3kGL-IFgXz6OkwVMMMZaOkDhIYmbbvQ9IycXSxggxxBjjaeyCJQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbZVk_8W3eLtdTmwG2HeJFhFd9qvM__x86kacUDSFwGe7HeqpP5C8eKXwWwUd9ygjQdnh7f-OexkcGz86Mw5Eyrr7zH48-vcwf2Oh-Y7HkZP18qoacD-h2kIpwaCIL-Rj_7QRsq2A2qqP16jOdSThLSWnbp5lLLcxw_mRs3i4mEfrgf9tiiQbP5uPq5dzgzQM5ZmLlFJM5QAJOwRYSzyqPRweTM3wI3x7sijqZqNid3rFEXoAj2MEh5pliibSwFIN4gEnEeKm7V7k5h85fcKGUotOfr8DBUgPIsDiW7HVWaOmYMxjyTaIuA-gLJAOntQl2LV8aifcv8_pADN_QocTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=mzqiqEKo4YkU6h6oQGisMHhCt-vSBqlrNCgcQrwSbFu6DbUeqyMStO4w-tas7qss20ize7bndcDhotZgIlJUU9i9rByrNtNnImNeGb10E2KZbnxc1x5FFVZ6pirH4s1E5osnR1Ca5H3RFqDrFrIHhBD1QG8cc6PE56sjeOhHtxQl5Pg2UfeYqhCZ8-dbc2cO3h6b6-fjDMcdCWojVHpVcbdDvYddcnN3QfktZIAILQ0Hw1-fAGm9Aykm01-bO5cXJzGVHdH34pYsFuTnalibTa2ksPg7kNu-Ku1WHTM9ubvak7D4lOCyInPeVL_E_LlHz1LTOAagSxMpe7fyuiIUqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=mzqiqEKo4YkU6h6oQGisMHhCt-vSBqlrNCgcQrwSbFu6DbUeqyMStO4w-tas7qss20ize7bndcDhotZgIlJUU9i9rByrNtNnImNeGb10E2KZbnxc1x5FFVZ6pirH4s1E5osnR1Ca5H3RFqDrFrIHhBD1QG8cc6PE56sjeOhHtxQl5Pg2UfeYqhCZ8-dbc2cO3h6b6-fjDMcdCWojVHpVcbdDvYddcnN3QfktZIAILQ0Hw1-fAGm9Aykm01-bO5cXJzGVHdH34pYsFuTnalibTa2ksPg7kNu-Ku1WHTM9ubvak7D4lOCyInPeVL_E_LlHz1LTOAagSxMpe7fyuiIUqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=nzB0N4V8ScgsuSGQo67kP-ExKgJjEJHvB6ML2V3R2BOGIcu4k0Aog7PG6LXoozJBrT5SFyHlrr4L8YEd54S4SDSoKMoAA-6cN1BBZAXjWnqo9buyPqIDFqM3o07XsbQmmAIw1Kfh0WIW2CibtgaTTvjSGfqYBprWbxv5_meGyv1hGDiOgvcS7tD11gqXJwTxv1fj4N1D9Sxc1vzJeu_qKyiB4dg4Yy6w0KDutJF8MbBv_rE3xzhCOmUcTxVap1BLytKBd7o4ks9IoYOdE0Dmw82oqM3t8lo1g-LNCjSXEWCWqvIle3M5ulCz1NZtv3ON-TdFMn6SeDZQRfpTX8PTiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=nzB0N4V8ScgsuSGQo67kP-ExKgJjEJHvB6ML2V3R2BOGIcu4k0Aog7PG6LXoozJBrT5SFyHlrr4L8YEd54S4SDSoKMoAA-6cN1BBZAXjWnqo9buyPqIDFqM3o07XsbQmmAIw1Kfh0WIW2CibtgaTTvjSGfqYBprWbxv5_meGyv1hGDiOgvcS7tD11gqXJwTxv1fj4N1D9Sxc1vzJeu_qKyiB4dg4Yy6w0KDutJF8MbBv_rE3xzhCOmUcTxVap1BLytKBd7o4ks9IoYOdE0Dmw82oqM3t8lo1g-LNCjSXEWCWqvIle3M5ulCz1NZtv3ON-TdFMn6SeDZQRfpTX8PTiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=rPoZASA8W4OqSH8YeV8_0SYAd_RMFbpPd-azqzpog8I7L1AgbI6I8_zyp5TNxRtSL6-gC_WHxAIzGXti1MQFIzpEKNj09odoUm-TazHm5SaqJ5po_9AXe0dOuLrLQHZQsoaCd2tgl3Cnoc4ZSwv2TgWVzjyp0E5uKp4oA8eveyJquaJmqupgPtKUB_P9GK0ZKPKMiwV-aP3HrsJEZjtL_vl9EuGXYqf8JRjMgA7D131LYBIi7AkXdekUXcaWATR9-xli2HiOb88ts6Oy2MSa_x5HdCyDNBtHAfIemh_1psudXTPY3gBw0H2AsSZraBOer5bFd1Pe_586R_UX2Ti2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=rPoZASA8W4OqSH8YeV8_0SYAd_RMFbpPd-azqzpog8I7L1AgbI6I8_zyp5TNxRtSL6-gC_WHxAIzGXti1MQFIzpEKNj09odoUm-TazHm5SaqJ5po_9AXe0dOuLrLQHZQsoaCd2tgl3Cnoc4ZSwv2TgWVzjyp0E5uKp4oA8eveyJquaJmqupgPtKUB_P9GK0ZKPKMiwV-aP3HrsJEZjtL_vl9EuGXYqf8JRjMgA7D131LYBIi7AkXdekUXcaWATR9-xli2HiOb88ts6Oy2MSa_x5HdCyDNBtHAfIemh_1psudXTPY3gBw0H2AsSZraBOer5bFd1Pe_586R_UX2Ti2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml5ghYoVuc8iwEiow-CJsXGOFOp6b2ITKwKvSUzb-OQaLB_NjZsUuh4ClAC3OKelBOTAiMqECljQws23ceI1HN1aUl4_faOmNwSStU_P1TOkYW_AV_dTj7dFyqGjgyFXvfw_8_M9vjDUQ4Ykn-XGP7OJgO-xItNxwb75fOiC1N6GZr-aST3SseMKcWCwEUCIJP6Gx0zR1yC_AzdMsqztqyRMqpThfgC5dK_O2tZ4t5oaVcFP-fgxBnWW4W6fd17BOBtrKbc5TP8LhuL3yzigTh3fZy0UqfDXJD-7DUUV0kBLmlVm7k5pcWV5_SrlAYOFvkKTsWtRE1cR3zwkXpCe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0fgQIPuYf6dY04s5U3WoCKATSsytVdxsjJMxgspc6M2dmzDNuuGp6TuTAgxUowXFTKyzZ1_EAoJD7V4Iu9cBtIGg8xgG3gHYQKTrpvTpfdvpIr0RbYoMkEWuBVQ0DbYn46UHkERJfAzyfEta9B_B4lW7Gknrn22UCBslKtf6FniXawBaRYnSyUhlKGsAzahy7sJCdOsIDqrNklhOjXWocAYcrzUSeVnau0HOSdhOps3_8zYH__FsyfQfG07hHX2nxC1izYt2y0TKTxv3KDN580iVxuLuPsqG1qeJVKc-3fCXmMxM6zffUeUO7eEvvjrh4JQVHeyYgJX9TBXBix9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=sacngiEUvtgJB7L1NE00Nd9F6JASfTcLrx-DkpXhjWSini1C4SbLbKPxqy6YjVHzJD6VS3aeZpe6gPrOexOPhFkhRwVcnIOrtYAg8NC4Q-nOBU71HZuj6B_ZhUgswqwp3nNBSl8VyBUrzxpkrt0ZNq31-CVQPWR9PPsfjp--0CSnuEqP-wHPbGSa_pMkCJ5z3huQ7jj5qcc1szrn6J05GyFp-hNO3ulgnh1J77eN80L9_ScXQIraqxxT2-k0st89fNzx2ULAmJw4IDBrqVIk4e1lkimxbxQwcuddpNf7gNqxruIEgmkqtpGpS4vld_KetlWwOQdIVr1MlBbum98whg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=sacngiEUvtgJB7L1NE00Nd9F6JASfTcLrx-DkpXhjWSini1C4SbLbKPxqy6YjVHzJD6VS3aeZpe6gPrOexOPhFkhRwVcnIOrtYAg8NC4Q-nOBU71HZuj6B_ZhUgswqwp3nNBSl8VyBUrzxpkrt0ZNq31-CVQPWR9PPsfjp--0CSnuEqP-wHPbGSa_pMkCJ5z3huQ7jj5qcc1szrn6J05GyFp-hNO3ulgnh1J77eN80L9_ScXQIraqxxT2-k0st89fNzx2ULAmJw4IDBrqVIk4e1lkimxbxQwcuddpNf7gNqxruIEgmkqtpGpS4vld_KetlWwOQdIVr1MlBbum98whg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=i051p5k82EBsZ6BNMF7GIo5o1oIi4t7c-71tky7dYlshHhHdFjJ-3oSelFrWPDyiD-7gyLyN8u4lk2OtMuiqztrBnYC1gZQgJDQza3k-W6ugd5C9poRu2h6HBoONe_BYbovZVBrNaoweI5oljMwvBmf9-G8nofe0rsIYcWhOpQBaWJOfcqGy_uSi9HhaZlGMrc0Gwf8kowt30axk99QGPr1PImd7ej5MspkAzC6TY96PrEcozOuX4GqQq6Vvkp8D-BBhwizoVitLKPYQsi17W2IFgSrwzvlgp_ichlg66yZ1vIVAck0h9aRTkEbKVNuP0f50H0dO22QAq4kobC1x_hJzmVEsZsde7mtXEmZjMzv6BG874wmoRfqnGFF-sRmAicl7ezddwBWMC0Sp_uLpm3h0ER2CevXt4zLdtTOPCHpNkMt6RqM8kFJ721Phh7iSjU1OcB_804HOFNpcrlbdMv823RfgAtAXpdsLxU_ztkeF_-qm-z0vNKPtNu2Bb80K05h0tPwJA_VmPXgomBTt_rdNf2t622vJ29aVv64BHeiuW7SD3yggxbAALgaMIvspmFGnJhluWuafS2K8abYhhrDZVEKiyLfNm5aN6rl4-reRc3ni_-J4IGS-JsmK4fHlfU8Ui8S6OwN5Uyf8_WNEMw-RPZtT4rWXjmeu9RI1i1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=i051p5k82EBsZ6BNMF7GIo5o1oIi4t7c-71tky7dYlshHhHdFjJ-3oSelFrWPDyiD-7gyLyN8u4lk2OtMuiqztrBnYC1gZQgJDQza3k-W6ugd5C9poRu2h6HBoONe_BYbovZVBrNaoweI5oljMwvBmf9-G8nofe0rsIYcWhOpQBaWJOfcqGy_uSi9HhaZlGMrc0Gwf8kowt30axk99QGPr1PImd7ej5MspkAzC6TY96PrEcozOuX4GqQq6Vvkp8D-BBhwizoVitLKPYQsi17W2IFgSrwzvlgp_ichlg66yZ1vIVAck0h9aRTkEbKVNuP0f50H0dO22QAq4kobC1x_hJzmVEsZsde7mtXEmZjMzv6BG874wmoRfqnGFF-sRmAicl7ezddwBWMC0Sp_uLpm3h0ER2CevXt4zLdtTOPCHpNkMt6RqM8kFJ721Phh7iSjU1OcB_804HOFNpcrlbdMv823RfgAtAXpdsLxU_ztkeF_-qm-z0vNKPtNu2Bb80K05h0tPwJA_VmPXgomBTt_rdNf2t622vJ29aVv64BHeiuW7SD3yggxbAALgaMIvspmFGnJhluWuafS2K8abYhhrDZVEKiyLfNm5aN6rl4-reRc3ni_-J4IGS-JsmK4fHlfU8Ui8S6OwN5Uyf8_WNEMw-RPZtT4rWXjmeu9RI1i1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhtPSXJ9VdkFK6T4UjRchWcdusUKwRZNtpSFwYGuMlJiyhAkuKdf1EFvihDgn5RBcukhjuCuIKtusknkCn77EgluBNCybC3DJ755QCXS0pLuOL99g6rUlr6rX41dpUTKYR1Mqu8maNytK1t7jdX4CR_1zTr6Rb-JoJoGxLJ3i28nbsG9qULx9mYRlzOzFoUPSjaJJtCxnrSgnbRoI-RB9GthgBA74EVbyKhD_a8fynfnk7q46n7QDt3vCThpBg_t8qVDnl2JyxKHhzQZTnpGtGRJgfB550ZHS4JEG3w1daBI5nA9CCsfeRhjBw1iuI4oPlP7h-yXBlp-96n8wK2gXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=hvE7zcqC7Uc4PuL-ogKzUTuUGiTeHv9GI2sqgKLUkGGkhITcDTgBRdFcF90cbJgAF8X5wehwWidH6oCHJ4k1idy1O2jBirJwj8qP1DK1qG6j0GsoFElhHHSeAyA1ubEgegJIIsNBrJg9Y3YvG_-vyvAAm4J2O3-XDm0Zz025_jpRZ6cK27cx1cYNNmIA4UF6xLQ4DXzTy_PU1jlNou_ehQ0zih-DwEndnlGU1kZ_cNpRkUdfjWKBBdOhTPtVT4dSz-l2W_54mLQN0gpxaVCyMGeBeVMXC4w36u0f7GLG6ncv9obXYCTeNkOWqUEcKEMtjHEFqjH0hMHO5pXda0d70g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=hvE7zcqC7Uc4PuL-ogKzUTuUGiTeHv9GI2sqgKLUkGGkhITcDTgBRdFcF90cbJgAF8X5wehwWidH6oCHJ4k1idy1O2jBirJwj8qP1DK1qG6j0GsoFElhHHSeAyA1ubEgegJIIsNBrJg9Y3YvG_-vyvAAm4J2O3-XDm0Zz025_jpRZ6cK27cx1cYNNmIA4UF6xLQ4DXzTy_PU1jlNou_ehQ0zih-DwEndnlGU1kZ_cNpRkUdfjWKBBdOhTPtVT4dSz-l2W_54mLQN0gpxaVCyMGeBeVMXC4w36u0f7GLG6ncv9obXYCTeNkOWqUEcKEMtjHEFqjH0hMHO5pXda0d70g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=qAUP_cikxjUFWovHx8E5xaVnuKKtUfuclSURpCTj22vCaZYkthFg4xNtIl_qXzRuf-jri_KS4F9dkb_PhV3QSk2rAJhfQiirSN-TbjOXfe8ckKeaE0Jiv_uN2COs4u8C0wE0bQIEhSagXR2-3-P-ArUm3OdMHYdlM_EInZy38Knnopg1DDaOauSIWH33WZNwcG6h7Xa8-TXMhl5qMUAjD8NdoxmLxjXjg6wErNU4tBL6lUVVp_Iua18UXc4BMZTt5HLpmCm3DJma4FkC3O874zlAd8ihYycA8QTNZg86x6ZOeyC_0i0eVgYjYMIvVA_L_suAGcY3Ir9Tv18t2Xc3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=qAUP_cikxjUFWovHx8E5xaVnuKKtUfuclSURpCTj22vCaZYkthFg4xNtIl_qXzRuf-jri_KS4F9dkb_PhV3QSk2rAJhfQiirSN-TbjOXfe8ckKeaE0Jiv_uN2COs4u8C0wE0bQIEhSagXR2-3-P-ArUm3OdMHYdlM_EInZy38Knnopg1DDaOauSIWH33WZNwcG6h7Xa8-TXMhl5qMUAjD8NdoxmLxjXjg6wErNU4tBL6lUVVp_Iua18UXc4BMZTt5HLpmCm3DJma4FkC3O874zlAd8ihYycA8QTNZg86x6ZOeyC_0i0eVgYjYMIvVA_L_suAGcY3Ir9Tv18t2Xc3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnVznNz8aiBbOsNhmCU7UM7S2M18348DngZ7CY37Zw_WkYnvGBUoz_lkoAvv-K5uGslLbbZAuZvM_9Wmqth3zjOe21sD6GPkiIFI4LjxeJzkwZX89wGyoBDQs0muH15Mm0hJ9goAcSGUoLIvt0QYY5Z_AOL_Hesv-QJ89bw1X0SNHL4m1aSeFEYsUjfDe5HlUBE9bRLpJ5hz_1OxPxuNVVzJOpmEw9qeQgo3NQyDwG6wtl17BlAahHKzGdJ9eVApbEtlhN0yhb3MAZ5pxLGJWa22Nc017il9b6wJGEGDm3cAh25pHUkg-EFWs-Xyy_37bFv7uB8PLNTH1i3momClXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7yYOpR_xoWpGSAXvHrc8O6PauO_lIb-KonMRkBO5KeUpjWFceGOKfQkSvgdicA-reG3qSsGPTfUthEafcQWtAmH5C5vdVs2ptupIPXWGCuzPktHUdMKYdwPdBiwMmhdkbTjvLk4rS6nY93SShqsa1b6UH4XbmCs2kJ3noHkycyCaCUJeMWlyJYEGGTeOxBXwRa7nODOAzEiDXQoDJtTPbZ0MD0uiGovP4VdT6rLQR2OIU_W39i-Jpt-nFHYE_AW93794DQEVSobqFBcUm_1weUOogQI1t7-UEAa6Z3GMmj9y-82jVMKV7u5kz3Pklded41gd4KZwFW7KhmsOp-AyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=aDU2gFg9zZlkPkzLdsSzUvPlKJZPdRuGsJ6ILzjNWUaffTrhkY2Sdh4jv-dkMKjMl9-iyCkM1j6ZjfZkAVcYMJGzsrEZh60A0vF-MG_0SJZ8fZrRwL4ibq1z3AUcOmQZ00kBHNfZjB-YN5Gl-EwWbOhCBoPUzkRlYR1AxQHD_kBdraIDdxn1Djbv55I8LV2Zr7GSwzfKL5yOdzl1p4YN3xvpuh3qyfjpt3N2Lo9crXvuuG7QKBExi1YqkWp2623FA0777Esuotxu46ZeKvkjAn0S32MrL5is6r4YHwNxStlRpK7T_cOa-QDmZKXzeLqPLVgogoUL-0j8j0oCGpJh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=aDU2gFg9zZlkPkzLdsSzUvPlKJZPdRuGsJ6ILzjNWUaffTrhkY2Sdh4jv-dkMKjMl9-iyCkM1j6ZjfZkAVcYMJGzsrEZh60A0vF-MG_0SJZ8fZrRwL4ibq1z3AUcOmQZ00kBHNfZjB-YN5Gl-EwWbOhCBoPUzkRlYR1AxQHD_kBdraIDdxn1Djbv55I8LV2Zr7GSwzfKL5yOdzl1p4YN3xvpuh3qyfjpt3N2Lo9crXvuuG7QKBExi1YqkWp2623FA0777Esuotxu46ZeKvkjAn0S32MrL5is6r4YHwNxStlRpK7T_cOa-QDmZKXzeLqPLVgogoUL-0j8j0oCGpJh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=LTaao7R2z4C1WNL3ASJhPfXtZlTozvpSJsfag4_f6IzstUlpMeTsYcbe6e04k6JELwzhGGUSqBv1AuVt4XA4rblMCT4W-6_adR0mfM6k0OXrnCKe3RiHmHwh13zLHoZ4Z2VHKrwI5fBbLT66jjtFWiE__e2Dp3fHWeUWAiDE0tUbTV4Q1JKmfXoVOtOgar1RJ88x2-9apeXD5lGFWL-J9akTLmzVoUQ_42IpWjvpY_yEu_05GiPc8y0Rk4QkODmgEPphmc6m7xagToaxDpqfhhDjWs9lyE3OH5hbZYCR29y4AWAHM3_x5SPTAUD6cHZKD2DOlpprSiE-whNzwRg3Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=LTaao7R2z4C1WNL3ASJhPfXtZlTozvpSJsfag4_f6IzstUlpMeTsYcbe6e04k6JELwzhGGUSqBv1AuVt4XA4rblMCT4W-6_adR0mfM6k0OXrnCKe3RiHmHwh13zLHoZ4Z2VHKrwI5fBbLT66jjtFWiE__e2Dp3fHWeUWAiDE0tUbTV4Q1JKmfXoVOtOgar1RJ88x2-9apeXD5lGFWL-J9akTLmzVoUQ_42IpWjvpY_yEu_05GiPc8y0Rk4QkODmgEPphmc6m7xagToaxDpqfhhDjWs9lyE3OH5hbZYCR29y4AWAHM3_x5SPTAUD6cHZKD2DOlpprSiE-whNzwRg3Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTEP_pCa15XHmMB2nVcVDNZR4abIbvL_4BM9sVrHe3gc6rleEiQuwnb24eYg0hmRbWMkm6gv0bZvy75nkEJXjDHHpn9GpAxoYZ9Y0ehtaQjEH-ln_WX0scFfMA8IdG87t_k3nwjepzF7s5NbyntfifCUCT7wUZykjU3rBkCobLK6ib2LiqzoD28j_FNGgDXtQynf3hN_RhwgAnyavzZe__F0s62fdSxtPMV_ZAwZo1rHpa-sfB92e0EK944KaPO-wMsfkJXoNTeoFajcIB5mOsBo_UEQBoWHVRQBO-v8dXY-wyxVzkfrif0FDlzt1ph-kI-ecS4yWqByVyFrM3_Nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED9kYgzS13ya3u5wtGgWO9moc7lZ90Mht7aBxGoC32MaODKaimwSU28Mky1IO-o43GHKRplLI0Sc-5UVRodk_XqzVzRTq0a4LHVczIbOxFAiZmcYWQGrndRAgsdcC0h0KOS4Ajb-4f5JJA13vhRdcxuz1BdZ_t10iM8Fp--n9I3Qa2BB-NiZ1aAOk64pHvsr8AVd1UZ2sa1k3veD6iD5RXf39EoD6CMTVg3Efxw3LPewme-50ogzHPyNj5J1lI4CnTV6Odwlfgoql0jq9eeabZTpXaMD81jwnOKDshGrXnR6oYfBfpEaGWQgmQTC9drtejJUy7EqEHkqPzl3IhVbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMl2fNCa08tGIAajYtniH3ZhQzfRW_G6heOj3UpLbz7opRR9XnrzJAhoKbzEBd5Z5y6uL_s6Y-7lBULpiaSgiMZr_DSrowu_d-LEuaWRN7DL-3nKuhAb6o4-nlqD5TKqVq7ZGO2fHA1AIsjlGU4aqFECIp97DbAli1WjzyAXEj2WOyUNnO48NI5e2sYSz-Wlha6JXlcRZP6Avu7_SislUaAx9LBasu1ZCre-cxFe__X7QfAZz6530soMeHUlxgTsYO6s3K3FnzoeN1FovO998JKsK8DIAWNGXeSOD6do3RdCEVTdLqSpJYGqW9tr0pGlzZRvBo14tMLZsBuqcCwc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTgYzzIYCkQ8qy28DEleg8JwPF1ZLFGa5YdwUvRfp0x5MeHhImXGalaIdsXgTjmLb87T_Tp23IPMkn7i8ZOLub0ZgvlfaKXjsjf5HXLPO_FlEiHxCDq4YsjF0vZ-uKId8KIN3MFrpN67agc2Ss7pEbNfB0qn9iqFAlS1sIu53LyJiNZdlWmIo3cwsdvAEkd9d7Ls1quaWK1tMLEUQ3-LrIGWT-9C5iuzfWai4NoWZqxJ7u-Xk2454QAoKLvCrD6NGW_eKvPJelVtqyDhZsdyiolu2ZKSt9nly7wDK8vzaS9B9sQChLXUxXKmADs1EQ-IvBNnCWCPJN9NbIhDepx7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=Uil2s3VH6JIo6xlsQAdcafS0yoakDmJU03fRV2ID-OsaCn6LrMYjDjRzQAhE4x7l6IRL4dgsc4Iv9D7_iHHMOmYFDf2pdQknFnxadNiNejUdqe19wkblS52SW5D9cRztfpe_f_06vv4I8WXMMgmIZj4rT9uzy4n0MAq6dCyQRsCHHtrWkwYMzH23w3VaxhQetZCz0D-8GQHM3vYqRUin0CvfWyO_NvYJpTFKS2wqRDrT3U0bC4x0L-jiG0odzXP8SYY6Zb0y9TsK9CK2-8Yr3QaroumFy26O4jrcLLPS3FdFDYRtfTmSmwjMm7sHV3Re1Aq00X0l26YEodYbQq05eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=Uil2s3VH6JIo6xlsQAdcafS0yoakDmJU03fRV2ID-OsaCn6LrMYjDjRzQAhE4x7l6IRL4dgsc4Iv9D7_iHHMOmYFDf2pdQknFnxadNiNejUdqe19wkblS52SW5D9cRztfpe_f_06vv4I8WXMMgmIZj4rT9uzy4n0MAq6dCyQRsCHHtrWkwYMzH23w3VaxhQetZCz0D-8GQHM3vYqRUin0CvfWyO_NvYJpTFKS2wqRDrT3U0bC4x0L-jiG0odzXP8SYY6Zb0y9TsK9CK2-8Yr3QaroumFy26O4jrcLLPS3FdFDYRtfTmSmwjMm7sHV3Re1Aq00X0l26YEodYbQq05eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=OxlzgqTDUf-jJEJ2VcdKPsl7B-nC9YsbsjTemLN7kJfy2v56LrdGaIBpr_lXWK5dkKo34tswrvCHVfNous6280dy1FuR4tuLLKbX0CayL0vXKWMf376WvY6ikfPCFgEfB5YnmYIalLMrpqabvZ33SxXz3FIhcqB-ak1dPoWMSXTX1G4DsgOrFHxnoFhoIc1x7CuH2SW6qxifCz7iKchSvxFJx54OGKZX0mLMOG_UCZ3U3D8sVjH9yGgqmhAVmbzfOuAAdYtMGHlRfmQqYHfyqlt0jkIZDb-GH2FxuBoQ7RJvYOI-yDzKfs0UQTtJTD8XIt-OPGx0wxChY9W3uHG3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=OxlzgqTDUf-jJEJ2VcdKPsl7B-nC9YsbsjTemLN7kJfy2v56LrdGaIBpr_lXWK5dkKo34tswrvCHVfNous6280dy1FuR4tuLLKbX0CayL0vXKWMf376WvY6ikfPCFgEfB5YnmYIalLMrpqabvZ33SxXz3FIhcqB-ak1dPoWMSXTX1G4DsgOrFHxnoFhoIc1x7CuH2SW6qxifCz7iKchSvxFJx54OGKZX0mLMOG_UCZ3U3D8sVjH9yGgqmhAVmbzfOuAAdYtMGHlRfmQqYHfyqlt0jkIZDb-GH2FxuBoQ7RJvYOI-yDzKfs0UQTtJTD8XIt-OPGx0wxChY9W3uHG3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=dcNOg4I9Q6R-VZKMM0PBvNz50ynk5iIMw9QSIFW-meYq2ESdEG8txv0-_RCrtA6fTfm26Mr5iYUe0QI6aUQTtexONb1ZBq-3gvtmUc8FkGTEtFQtqHRgHo-xjYDaHjPRytU_6NNquA9zH7fS9sHmF7j1umJ4qxITzkiLDzX34970Kz5wgDjs26HCpKmCCRTlwHH0EuVqcYqOKVcLj7ftt6WQMM3IXDKtgzem-lwwReXDokS6k8P8eHtjsRHjg-25xuDpfXbGmZ9e1opDjR8Zqvkcg4yssbp_oIWqLaTvsElwRvozlMSJXoMi_zXj9dI_RaMXAidwPfzWqXY-QiFC-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=dcNOg4I9Q6R-VZKMM0PBvNz50ynk5iIMw9QSIFW-meYq2ESdEG8txv0-_RCrtA6fTfm26Mr5iYUe0QI6aUQTtexONb1ZBq-3gvtmUc8FkGTEtFQtqHRgHo-xjYDaHjPRytU_6NNquA9zH7fS9sHmF7j1umJ4qxITzkiLDzX34970Kz5wgDjs26HCpKmCCRTlwHH0EuVqcYqOKVcLj7ftt6WQMM3IXDKtgzem-lwwReXDokS6k8P8eHtjsRHjg-25xuDpfXbGmZ9e1opDjR8Zqvkcg4yssbp_oIWqLaTvsElwRvozlMSJXoMi_zXj9dI_RaMXAidwPfzWqXY-QiFC-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=tFfgB_OE2B0HcGC8NpffJty6FzpRFBXZqy0iI1eTc7H99ZbhPjaYkMbad1mt7GmUqXNsGJunmc8PlyCbzk7E1wyB-4pxOIQTEwixhlsTEm-Smdvl-xYo4lksGqZpRwgJbG5uQX8GG3rfbgQIBIioyLqAPny-1Bs9341g_THLH70BUDmu5DA5aUu8EvU8VZfWu1SLLsTJad2po6371ob8Ogy7zJrTvecqv-4NESmkO1GTenQeK4TY_ZCVqRqh-QlsJZ3vAdzoZwtgnlZO2_yRbL8yopyhkF1JfunfF3e-meyn8CShmIyY6mBhTuFkm8JCpaZfl1fiAY1Q52jBJatwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=tFfgB_OE2B0HcGC8NpffJty6FzpRFBXZqy0iI1eTc7H99ZbhPjaYkMbad1mt7GmUqXNsGJunmc8PlyCbzk7E1wyB-4pxOIQTEwixhlsTEm-Smdvl-xYo4lksGqZpRwgJbG5uQX8GG3rfbgQIBIioyLqAPny-1Bs9341g_THLH70BUDmu5DA5aUu8EvU8VZfWu1SLLsTJad2po6371ob8Ogy7zJrTvecqv-4NESmkO1GTenQeK4TY_ZCVqRqh-QlsJZ3vAdzoZwtgnlZO2_yRbL8yopyhkF1JfunfF3e-meyn8CShmIyY6mBhTuFkm8JCpaZfl1fiAY1Q52jBJatwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2D94PmwfVTlXmIic33PJqF6rxBlTSmPTX8kSp3XNC53ejnSmAuQ9Joul3fC6PielAVu7nDHDtcMO-ISYv8eME7kdnafx5QSFkeRxaCzjyXWmFgGbdO5y_Mp7sMZZJfWxUUpnA79ToOSuwekelIVvy7sOqLhsoZEetb2gYUV_ImtHzgnff8HrMcEHtkWJwtZ4hWqHX1hDGG0A8Nd7__y0gIAxnczXf-w-ZuATLqBuLm_n9iiuwJOPQLQWPSJI7r3VVUIZViCBTHLWepefDyPCd_WiosKbxCXxSaAhvKkN-_17ykgRKm3fAAtcXlhW1UUvZe_vBo4JCVusGRpxPNmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
