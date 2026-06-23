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
<img src="https://cdn4.telesco.pe/file/jEVfE9TVkbI1P9uPkkDDb1LS0R0JVmcuABZnqPSmMbGaGrPZDYWye6DlkKmSAvTTonTPUTiHyjd2QnyR6y7ilTC_OZt8TFRPTKzOk6f0a3Kpk6hn4R5YYkaLA2z10YUq34Fdht9M01ByMduqwVtWacInfYt0h3OK7oCCZ24yc3X8Iaaik1K5oho41tN9Mxaoe32JAP6jjsiVYbVFmt-pZfHdpEwQ5eXbgJRmUYuP8j7pV899kHn4QBDvj1o7qqeOYvk_QuZxQAZ9opAvCfcclKoW5Yq5U9mrbmsKmrMeAfCzo6T7nyvLCpvdjYd0-K8Lp5hiZR0ED1RTUrgL7gEwxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 15:06:33</div>
<hr>

<div class="tg-post" id="msg-662628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNm5gLDgWcsMyeYTtNSCaQSv9AH6IDeJeSYzW6N9vCY-_JF_4CS0o3oKWFX_CGLx3I2GMYLT3fpdST-6ISQQgsnCbovpNW1XtMJNPWBYzN1DOgbzjKwVLgDQNw7y0msTqacI4qtBUDkjvw1w7D30TwmBHF7I19Xkq_d3bq9dBjdqVXx44w_5pLCM5zJ6Nv9S-Kb89KiVR2pcq1LvAnvedTa8Tx9-Fs7EPvYjC5hV-swo8mCjVNzUMHtmFGmShLMe3CHW-XKhFIGFuDP1uJF6_LmwbpU3QrXMAq7CXZ4Ic688h7gl9cS3Js10g7X0DKbaiWoAwsyVBqvAytjgGM2tsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: ایران با بازرسی‌های گسترده هسته‌ای موافقت کرده است
ترامپ:
🔹
این بازرسی‌ها صداقت هسته‌ای ایران را تضمین خواهد کرد. اگر ایران با این موضوع موافقت نمی‌کرد، هیچ مذاکره دیگری در کار نبود. ایران به دنبال امتیازهای ارائه‌ شده از سوی ایران، با باز ماندن تنگه هرمز و پایان محاصره دریایی موافقت کرده است.
🔹
تمام کشتی‌ها و تجهیزات نظامی در موقعیت خود باقی خواهند ماند تا در صورت نیاز، محاصره دوباره برقرار شود؛ هرچند در حال حاضر چنین احتمالی بسیار بعید به نظر می‌رسد.
🔹
منابع مالی و کاهش تحریم‌هایی که در اختیار ایران قرار می‌گیرد، در حساب‌های امانی تحت کنترل آمریکا نگهداری خواهد شد و صرفاً برای خرید مواد غذایی و تجهیزات پزشکی از ایالات متحده استفاده می‌شود. این یک بحران انسانی است و احساس می‌کنم باید همین حالا کمک کنیم، قبل از آنکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/662628" target="_blank">📅 15:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIiPcok1vP6vMI5oYlgD_yl5l2G3FXWdM6H3AQx_vjzJd0fXQRyOpxlsirDIrc8aSd1Ak69lmEtnWunPYCBzG9-743CMvcWQvb-BWHHMYKSHsLFOri_lAZS0QJzIDyoqXPWyHSzluwmqml1wtp96NN3DwJ2ZDk0dI5Fa2c_gP7WWopsDEn9nKIms_Rv82AO4FI-_qalrSeQj1kwCjg_fHd8Z_pCmW6tQ9u-J9hjdPt2McmxJs5KPJ3H3EjEzIJIg3aSAUnbbbELrBp5i_oY-CqXZFZPuASCgASCtOpXUL_RW5c78iAaoLtJrJKpMq8rT2XRwFL-ZBgEOKiVYSBv4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد، یک رکورد بی‌سابقه. قیمت‌های نفت در حال سقوط هستند و جهان جای بسیار امن‌تری است!!!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/akhbarefori/662627" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmXoxlpFDdHefGl8xmIe-Hqx1-w0g8AzdvO3-8HLTiEwHRCSZFcYrq1mcMxHaBP3T-WrdrmcMPZ6mM_H3CRTvOnob-DZ-17tk2D3fM7lrPx62H0zsAYjtLn3gI2cREjCU4xz3N4_aLiG5YIh56hX77fzSBLKyXp8f83MdfRH4SSSBaucylp3rSvTpmUfD8rTPBmfBr2VgNh6UqF544tWrGi8-pBGApk_RNJMaff64DJIeVb-UuE6UAKkxOjYA-1bi2VY2q0Dv7fHX3r51iJhBB6a4ZtcefZpHmGTu0RMcLIpUk7k7nDSIWdeD2-mAWTez4_qqd_vwzuvY4Dexj859w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجله اشپیگل در آلمان: ۹۲ درصد مردم اسرائیل، ایران را پیروز جنگ می‌دانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/662626" target="_blank">📅 14:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منبع نظامی: فقط تعداد معینی از شناورها اجازۀ عبور از تنگه هرمز را دارند
یک منبع نظامی:
🔹
براساس هماهنگی‌های انجام‌ شده با نیروی دریایی سپاه، روزانه تنها تعداد معینی از شناورها مجاز به عبور از تنگه هرمز هستند. این تعداد از شناورها به‌صورت روزانه و متناسب با شرایط، متغیر خواهد بود.
🔹
گفتنی است، در پی اقدامات خصمانۀ رژیم صهیونیستی و همچنین نقض تعهدات آمریکا در اجرای آتش‌بس، تنگه هرمز طی روزهای گذشته بسته شده بود و در این مدت هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/662625" target="_blank">📅 14:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662624">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
عراقچی به بغداد می‌رود
🔹
عراقچی یکشنبه آینده در چارچوب تعاملات دو جانبه و هماهنگی‌های برگزاری مراسم تشییع پیکر رهبر شهید ایران به عراق سفر می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/662624" target="_blank">📅 14:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
خبرگزاری عمان نوشت سلطنت عمان و جمهوری‌اسلامی ایران بر سر گفتگو از طریق یک کارگروه مشترک درباره مدیریت آینده هرمز توافق کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662623" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جوادی‌حصار: موضع ما در خصوص شعار مرگ بر آمریکا باید عوض شود!
محمدصادق جوادی‌حصار، سیاستمدار اصلاح‌طلب در
#گفتگو
با خبرفوری:
🔹
شعارهای مرگ بر آمریکا که چندین سال است سر می‌دهیم به دلیل دشمنی آمریکا با ملت ما بود و حالا که قرار است تفاهم و دوستی صورت بگیرد، باید جهت ما هم عوض شود و در گذشته ما مرگ بر شوروی هم می‌گفتیم ولی الان روسیه از دشمنان ما نیست.
🔹
نگاه مردم به دشمنان تا حد زیادی تابع رویکرد حاکمیت است و در صورت حرکت به سمت دوستی با آمریکا، اکثریت جامعه نیز همراه خواهند شد. پایبندی دو طرف به تعهدات می‌تواند زمینه‌ساز دوستی و همکاری‌های بین‌المللی باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662622" target="_blank">📅 14:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86931711b.mp4?token=GW9GFhdrV22vWpGE7PZ1eJXxk0lLYcAP8BtYz1LwhKTQuvw0kFXZaOlzNT5-ZLwCoozLDix64CYtlti9-ntHc7BIph_3l1nQySWeTWlyO-DijniSFbYNszrNoa95jdbZGNKWJ9Nfum581NN77bGH3JelB1fm5rkVeNTPM-ITTHSn-70HVsiiFO2XY0YoGkC4QslMlVifUS_xG2vQvVlnGvsi_n4deI3KZObEbnE2n_isZEOJNCq338XIRZlymEZ1jCqExiRg9498ygUssomb1pqwARUTKvxwqa9KfQs4MNlRKEDVKmrfWuTaIa2CYSMiKk4hBDbJxKsE2p68wY7YXjccwtVIJkSABhUY2fIXmI2B6oS0IUUBcrQ3UR5APCFqK2_QVReUXgkv8XY792MIXb_zxCvWH1LKlHP_fMYDsGMi_gBzSm6q--LSTsODzctDHd1DsAjciMNB36PsRmuTNMABek1BU6qied77a03JYeyGAd687YBfMI2Z0ob4-kSRh3mTnueta8RshCdyXfOdgPqNdMdfDMl4XrXxfzU4dzkYS8tO30ATtqkejSzypbbZC7Pm8nVkcnBQMJfcA61a23af_FhzbP95_cyiTOABAuNepPlsM-W0fcBkf4zrvhuSo2iCc9m2N7AGu1UMao_mhsZPJEXGDPqb6pHhFaxtu1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86931711b.mp4?token=GW9GFhdrV22vWpGE7PZ1eJXxk0lLYcAP8BtYz1LwhKTQuvw0kFXZaOlzNT5-ZLwCoozLDix64CYtlti9-ntHc7BIph_3l1nQySWeTWlyO-DijniSFbYNszrNoa95jdbZGNKWJ9Nfum581NN77bGH3JelB1fm5rkVeNTPM-ITTHSn-70HVsiiFO2XY0YoGkC4QslMlVifUS_xG2vQvVlnGvsi_n4deI3KZObEbnE2n_isZEOJNCq338XIRZlymEZ1jCqExiRg9498ygUssomb1pqwARUTKvxwqa9KfQs4MNlRKEDVKmrfWuTaIa2CYSMiKk4hBDbJxKsE2p68wY7YXjccwtVIJkSABhUY2fIXmI2B6oS0IUUBcrQ3UR5APCFqK2_QVReUXgkv8XY792MIXb_zxCvWH1LKlHP_fMYDsGMi_gBzSm6q--LSTsODzctDHd1DsAjciMNB36PsRmuTNMABek1BU6qied77a03JYeyGAd687YBfMI2Z0ob4-kSRh3mTnueta8RshCdyXfOdgPqNdMdfDMl4XrXxfzU4dzkYS8tO30ATtqkejSzypbbZC7Pm8nVkcnBQMJfcA61a23af_FhzbP95_cyiTOABAuNepPlsM-W0fcBkf4zrvhuSo2iCc9m2N7AGu1UMao_mhsZPJEXGDPqb6pHhFaxtu1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی خراتیان: با این روند، بیروت را از دست خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662621" target="_blank">📅 14:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cdafe617c.mp4?token=j5FQJ4JClrvLlU30HMsESvbFq2RdJDdsvOrzseAiQDwl1Ym3RP6aVN-8ZLBVB3hKZPalf_tRXPk6G6C22ugV7sMvg63GNwqm2hOb1RZgJJEcgm7XEt5IAquPaMVDYQrf83Nfz9PO-HmBBLNaI8VVbzw5mVqlmRwN4mIMyrv4VRKZQYnc-AiWUMUwaaoTq57sQXIBuhkbySkucB69w5leCo2LMJRJLDhs3tJ6z4wfLaVtBjBEpqCkBsPuOQeI0kuX9sizc44FC1mmC4h6NHM-FVHJT_InH3bXcaarzoAy8x0p12w5xUwDJpVoXNaObOUgUE1RRLpMY2_l8Ye2wj8jHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cdafe617c.mp4?token=j5FQJ4JClrvLlU30HMsESvbFq2RdJDdsvOrzseAiQDwl1Ym3RP6aVN-8ZLBVB3hKZPalf_tRXPk6G6C22ugV7sMvg63GNwqm2hOb1RZgJJEcgm7XEt5IAquPaMVDYQrf83Nfz9PO-HmBBLNaI8VVbzw5mVqlmRwN4mIMyrv4VRKZQYnc-AiWUMUwaaoTq57sQXIBuhkbySkucB69w5leCo2LMJRJLDhs3tJ6z4wfLaVtBjBEpqCkBsPuOQeI0kuX9sizc44FC1mmC4h6NHM-FVHJT_InH3bXcaarzoAy8x0p12w5xUwDJpVoXNaObOUgUE1RRLpMY2_l8Ye2wj8jHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر خارجۀ روسیه: باید شرمنده باشیم که نتوانسته‌ایم مسئله فلسطین را حل کنیم
🔹
زیرنویس اختصاصی خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/662620" target="_blank">📅 14:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wq4_RAcU3cL7WX8FKQImC84ZnKlMgxrECrlMs_QRjx8Q3fVfDcIu6-z8ahKQnMVY6cS2_Bkn09nze3IbWWOLRVd2DViSF0sqYXJYJVl4UKAHV9wmCGWYzgHzFd5k4XrcA81eRRSPsPm-NxDjcnLEPaWfVJuAtvMrOS9hTRsEznETqoaxN9N7mu48NVv8czT8cRFc11qYwT98I-Rh8Xecq1PC1ETOrE87IAIqLmfkB3ecCqcLmUSa6XYyVcD1ovUq0P64yJmnXODbJmsSkq5Tp3R_dJlI6eP813cPnSxRug-Pd9gEAEop3yUJR6AEUZGclsAjPkzgZFC2VB5L77rOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر جالب از هجوم مدافعان اسکاتلند به بازیکن مراکش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662619" target="_blank">📅 14:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEvphGIyY54EfX70dUl0qm2AT3pzSqAJH1bsIGNoxTfECum0EYHUnnKRXqGtb61dNV7jVDvDU1teKUrVLlnQ7cSKhEXlCRYi5WqnUYVvlVvc2WXbCaU-UxnuwwtFQ3sdy1Ie_RGcnhV8t0p8BcDCloHMwyUSHEb1161soUhyCC0H6m_8QEcphJ2bcBExlQxw2wWTzpDYPnKY90C8H_Gq3hTliD1rxxo1zDb4zLOFk3usf6YUgXbncHaYW4oh8EWXG1OTQ7mARDHD1mXVCIf6XSb4VQnZYcluUTIq6oqxFKdxhglVtCwHbb_J47qMJ9bKD9zbtQwrAY1MHo7sDrs0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرار نیست همه چیز را حفظ باشید؛ فقط هر روز یک واژه یاد بگیرید
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662618" target="_blank">📅 14:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
یک مقام وزارت امور خارجه: شرایط تنگه هرمز به وضعیت قبل از جنگ برنمی‌گردد
🔹
سفر آقای قالیباف به عنوان رئیس هیات مذاکره کننده ایران با آمریکا به کشور عمان، بلافاصله پس از بازگشت از مذاکرات سوئیس، این پیام مهم را در بردارد که شرایط تنگه هرمز به وضعیت قبل از جنگ برنمی‌گردد.
🔹
تصمیم‌گیری در خصوص مدیریت تنگه هرمز در حیطه اختیارات دو کشور دوست، همسایه و برادر ایران و عمان است و چگونگی اعمال حاکمیت در تنظیم ترتیبات عبور و مرور به عهده این دو کشور ساحلی تنگه هرمز است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/662617" target="_blank">📅 14:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 در ایام ماه محرم معمولاً کدام فضا را برای شرکت در مراسم عزاداری ترجیح می‌دهید؟</h4>
<ul>
<li>✓ هیئت‌های محلی</li>
<li>✓ هیئت‌های بزرگ و معروف</li>
<li>✓ به صورت آنلاین (شبکه‌های اجتماعی/پخش زنده)</li>
<li>✓ در خانه و از تلویزیون</li>
<li>✓ معمولا در عزاداری محرم شرکت نمی‌کنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/662616" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس/حمله وحشیانه صهیونیست‌ها به غیرنظامیان در جنوب لبنان  خبرنگار الجزیره:
🔹
نیروهای اسرائیلی در محله دیر در نبطیه الفوقا، جنوب لبنان، به روی غیرنظامیان آتش گشودند.
🔹
پس از تیراندازی نیروهای اسرائیلی به شهروندان در نبطیه الفوقه یک نفر شهید و دو…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662614" target="_blank">📅 14:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
عراقچی وارد اسلام‌آباد شد
🔹
وزیر امور خارجه جمهوری اسلامی ایران همزمان با برنامه سفر رسمی امروز پزشکیان به پاکستان، وارد اسلام‌آباد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/662613" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10071cd098.mp4?token=ZE640EZZdd6lw_83vwHrC2LpdeqiKmHbYV5emwNYUdbUYU8a9RHqs3aRVu3M5gwIqJYOwLLevH9wNolU7ctA2nABMEz5Fwr9Uogl5LXlp-QpYFTzzRR3mxBaymXiky2zZ4yqA1nX6vISPbQ8a5XAP4UtH4iS9lywkXgUIHZPKoJOj82vqK8y1u2n2ZOBWC2sCbtSfImm2BZ5Q71tU5jFblgDv1NiA7XgiOQhTGv4rfUpkfSWLN3R1djEklm8Cumc9r_DVPcwqaEHDr0YZg0Dk6G1STI1mvQeYSbYvprqg8_Yd3-vgYaEQq2yZXFptzelS1g6oRF_k-0n_hBqtgcZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10071cd098.mp4?token=ZE640EZZdd6lw_83vwHrC2LpdeqiKmHbYV5emwNYUdbUYU8a9RHqs3aRVu3M5gwIqJYOwLLevH9wNolU7ctA2nABMEz5Fwr9Uogl5LXlp-QpYFTzzRR3mxBaymXiky2zZ4yqA1nX6vISPbQ8a5XAP4UtH4iS9lywkXgUIHZPKoJOj82vqK8y1u2n2ZOBWC2sCbtSfImm2BZ5Q71tU5jFblgDv1NiA7XgiOQhTGv4rfUpkfSWLN3R1djEklm8Cumc9r_DVPcwqaEHDr0YZg0Dk6G1STI1mvQeYSbYvprqg8_Yd3-vgYaEQq2yZXFptzelS1g6oRF_k-0n_hBqtgcZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توافق جدید با ایران صلح نیست، یک آتش‌بس موقت برای فشار بیشتر است
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
یک تحلیلگر سوئیسی توافق اخیر با ایران را نه صلح پایدار، بلکه وقفه‌ای موقت برای مدیریت تنش‌ها دانست و هشدار داد که به دلیل فقدان اعتماد و تضمین‌های امنیتی، این مسیر می‌تواند دوباره به تشدید فشارها و درگیری‌ها منجر شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662612" target="_blank">📅 14:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
عراقچی وارد اسلام‌آباد شد
🔹
وزیر امور خارجه جمهوری اسلامی ایران همزمان با برنامه سفر رسمی امروز پزشکیان به پاکستان، وارد اسلام‌آباد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662611" target="_blank">📅 14:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d59a3bd4.mp4?token=gaSY0kzKxbxGVhdlLA3-ubv9DDqCZh3PHKU7MDRFbARYM7W_NBk6qpvWCGIp1lL1fh4pCTnLnRrO6FFjSW8BcCsenARVx2Fo--7HNN7_9SnURZykwSxUoIUq9RVPplkBfZfeJv98_SCgVE0D4i0TwSOnMYLM_SHYOppzfthdbRPsymseHGGqGWAXvraMoXmR-S04LGnlOY5nX_SbWk1u9CHi928eYZSu5Lz6SPGk8rY7hhNIHFTQ9dRv1ihYDrhU5Y4QMC5bJsELexEAVSRL5eO1QQLE1rSpDRaWel96YeGVnSQ8EPrI0E-UoXL3nzGxlsdEPA_CmUkoVmYoB-pNKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d59a3bd4.mp4?token=gaSY0kzKxbxGVhdlLA3-ubv9DDqCZh3PHKU7MDRFbARYM7W_NBk6qpvWCGIp1lL1fh4pCTnLnRrO6FFjSW8BcCsenARVx2Fo--7HNN7_9SnURZykwSxUoIUq9RVPplkBfZfeJv98_SCgVE0D4i0TwSOnMYLM_SHYOppzfthdbRPsymseHGGqGWAXvraMoXmR-S04LGnlOY5nX_SbWk1u9CHi928eYZSu5Lz6SPGk8rY7hhNIHFTQ9dRv1ihYDrhU5Y4QMC5bJsELexEAVSRL5eO1QQLE1rSpDRaWel96YeGVnSQ8EPrI0E-UoXL3nzGxlsdEPA_CmUkoVmYoB-pNKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشمندان چینی پرینت سه‌بعدی‌ای اختراع کردند که فقط با نور، اشیا را در ۰.۶ ثانیه می‌سازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662610" target="_blank">📅 13:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWd0XNdi5F7VwfD1YW5-7MokYJmmq4p9YXjSjQJIcoSiOxnjVoIkrKm5cGfQDRVwP9mIRO7Flew6ZU-l5kh6FhVyTf-y6HyfCQwn0AgkutyV6IwVz9_2kJL96aBKW7jx-0wbi4sn3H8FsuyAD-Px_jsta6vcnFwggIaJcgHJ4l9XyzeY2LQWHDU2HmMv5Y0brXt-hpTOBwAMi1rTWQ1RMU2Ab3VwMhhT1zpxosmwzF5aQmwwz1Cih80BgkcGwI20p60jnkosGoJ6EYVk986oJVNJMD1m4Bv-Brlhfeo_LkLXKKLWvtK1q2_lN0Va6kof4S54FcT6pWeG4nzhG9AQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆔
@talasea_mag
امسال کجا سرمایه‌گذاری کنیم و از چه تصمیم‌هایی دوری کنیم؟
وبینار «استراتژی سرمایه‌گذاری در شرایط عدم قطعیت» برای کسانی است که می‌خواهند در سال ۱۴۰۵، سرمایه‌گذاری را با چارچوب، مدیریت ریسک و نگاه بلندمدت جلو ببرند؛ نه با حدس و هیجان.
👤
مدرس: سهند غلامحسینی
🗓️
دوشنبه ۸ تیر | ساعت ۲۰ تا ۲۲
همین حالا برای این وبینار آنلاین در ای‌سمینار ثبت‌نام کنید:
👇
👇
🔗
لینک ثبت‌نام وبینار
🔗
لینک ثبت‌نام وبینار
🔗
لینک ثبت‌نام وبینار</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662609" target="_blank">📅 13:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
بر اساس تصویب دولت روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر استان تهران و دوشنبه ۱۵ تیر کل کشور تعطیل است
🔹
همچنین روز سه شنبه ۱۶ تیرماه استان قم و پنجشنبه ۱۸ تیرماه استان خراسان رضوی تعطیل است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/662608" target="_blank">📅 13:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
اختلال گسترده در شبکه بانکی کشور
🔹
بر اساس بررسی‌ گزارش‌های کاربران، تعدادی از بانک‌های کشور دچار اختلال شده‌اند. بر این اساس برخی از پایانه‌های فروشگاهی و اپلیکیشن‌های برخی از بانک‌ها با اختلال مواجه شده‌اند.
🔹
به نظر می‌رسد این اختلال به صورت گسترده در…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/662607" target="_blank">📅 13:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اعتراض ایران به تداخل ورزش و سیاست در آمریکا
بحرینی، نماینده دائم ایران در سازمان ملل:
🔹
ایالات متحده خیلی دیر برای تیم ایران ویزا صادر کرد و به آنها اجازه اقامت در این کشور را نداد.
🔹
ما از رویکرد ایالات متحده که فوتبال را به یک ابزار سیاسی تبدیل کرده است، بسیار ناراضی و معترض هستیم.
🔹
باید شرایط یکسانی برای همه ورزشکاران فراهم شود./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/662606" target="_blank">📅 13:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دیدار و رایزنی قالیباف با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662605" target="_blank">📅 13:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار جدی یک اقتصاددان: حتی با رفع کامل تحریم‌ها، سیستم بانکی ایران آماده مراوده با خارج از کشور نیست!
مرتضی افقه، کارشناس اقتصادی در
#گفتگو
با خبرفوری:
🔹
اگر توافق با آمریکا به سمت و سوی خوبی پیش برود، قطعاً تجارت ما رشد قابل‌توجهی خواهد کرد، اما موانعی مانند بوروکراسی، مشکلات گمرکی، ضعف نظام بانکی و قوانین متناقض اقتصادی همچنان پابرجاست.
🔹
ایران پس از رفع تحریم‌ها می‌تواند مقصد جذابی برای سرمایه‌گذاری و تجارت و صادرات باشد اما قوانین بسیار ضد و نقیضی که مجلس‌های گذشته تاکنون برای تجارت و اقتصاد تصویب کرده‌اند موانع جدی هستند و بانک‌های ما سال‌هاست که مراودات خارجی نداشتند و الان هم آمادگی مراوده را ندارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662604" target="_blank">📅 13:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e648ddb2dc.mp4?token=YnLwOyd8MUvbvUV9BxVH057WVCkvYcC_Fb5Lm2b9dxKoxgSCkEY_DA5iQi4jyUPggm8P4okxAocdORF7QV1AX_crDjFhxYCzgnBVBw_3dfWSvmhfehDzG-nM01kzMLNk2NUTHy_rzU6nNJ7lsayyBgl-nssqncnmsYJrVi02K13x0vsqzg_coyLqJlK1fvbqRcpAEylHyuVHzQZCz7S54GOWk00VUxCS3wUBY2Duk-hwa8j_cqY0_I8VJtmcabAbqtA6i3B-vriyqRH9uUZOynYOxj8gNOJy6SmV1rddru3GKy0ZtfQvRhHS1qW73o7mkk_QcUmM7Dz5zA40FH8Qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e648ddb2dc.mp4?token=YnLwOyd8MUvbvUV9BxVH057WVCkvYcC_Fb5Lm2b9dxKoxgSCkEY_DA5iQi4jyUPggm8P4okxAocdORF7QV1AX_crDjFhxYCzgnBVBw_3dfWSvmhfehDzG-nM01kzMLNk2NUTHy_rzU6nNJ7lsayyBgl-nssqncnmsYJrVi02K13x0vsqzg_coyLqJlK1fvbqRcpAEylHyuVHzQZCz7S54GOWk00VUxCS3wUBY2Duk-hwa8j_cqY0_I8VJtmcabAbqtA6i3B-vriyqRH9uUZOynYOxj8gNOJy6SmV1rddru3GKy0ZtfQvRhHS1qW73o7mkk_QcUmM7Dz5zA40FH8Qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس مورفی: جنگ را باختیم و برای بازگشایی تنگه هرمز باید پول هنگفتی به ایران بپردازیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662603" target="_blank">📅 13:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068939d7a.mp4?token=dSGSsJFQb_BrZtCZt3VDzRifeLOX24EhS5OqX5OaPshuv_sQ0LpS7m-7nfMYTlQW2XbfDro4R1S8ZhEP7MGzzs_x4pRMX1p3qP3_2bC29xmINHuxzSNNuQjdO6ATpj5OIpSKSjJ-ViiBdxy2FXs6-F8dSYdHTXke4zr0OGCYcJObybf6K3ONiLIZILXZT36m0TFtqoImdQScLpxXuLWpEF6-eO5TWzhZjVpVpDKfzjkFT17YSHvraU68x-ITOqx9OiHcqcC1XQnXQCBWjvyY5RBDGYdcQVY_FviJKySvZ482tVD03ZgjjH_tEl-TN9wkINEaZ-rV9nlPE7WW2q-c0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068939d7a.mp4?token=dSGSsJFQb_BrZtCZt3VDzRifeLOX24EhS5OqX5OaPshuv_sQ0LpS7m-7nfMYTlQW2XbfDro4R1S8ZhEP7MGzzs_x4pRMX1p3qP3_2bC29xmINHuxzSNNuQjdO6ATpj5OIpSKSjJ-ViiBdxy2FXs6-F8dSYdHTXke4zr0OGCYcJObybf6K3ONiLIZILXZT36m0TFtqoImdQScLpxXuLWpEF6-eO5TWzhZjVpVpDKfzjkFT17YSHvraU68x-ITOqx9OiHcqcC1XQnXQCBWjvyY5RBDGYdcQVY_FviJKySvZ482tVD03ZgjjH_tEl-TN9wkINEaZ-rV9nlPE7WW2q-c0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر انرژی‌ آمریکا: آلبرت انیشتن ۱۲۰ سال پیش مقاله‌ای منتشر کرد که...
🔹
ترامپ: برای هیچ کس اهمیت نداره..
🔹
وزیر انرژی: به نکته خوبی اشاره کردین قربان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662602" target="_blank">📅 13:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098a65f379.mp4?token=vDVe8yOMcTJAa20Rwl_PyS14l8Lsi8QQKjkcDH2fbLy5FkTzSt_XMiN1T2RiqxpLWv-th7xO5IrjChOECPknjXai3Jy3APzrEirEKYYwQTxBTwLEieWUsUiJOeK_020CncCO7miaJzhGkyGNuSgHJyLWi3q1kl49I30jnwoMSIGYVg7r-V8LpfCy8Ie74A4f-lGyvTxodRUvpayxYGnK38YBymhsz7UK4-O0RQ7sbLJ8SYwZep85pgNbf5fPEXLorQlPbOjOGQufA86JLBXKH3fQGtLMwQqVBAJiqpULbVvfGw292tIHrNRb0TP2gYTHf170wJ6WDl0nyCbcgsriCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098a65f379.mp4?token=vDVe8yOMcTJAa20Rwl_PyS14l8Lsi8QQKjkcDH2fbLy5FkTzSt_XMiN1T2RiqxpLWv-th7xO5IrjChOECPknjXai3Jy3APzrEirEKYYwQTxBTwLEieWUsUiJOeK_020CncCO7miaJzhGkyGNuSgHJyLWi3q1kl49I30jnwoMSIGYVg7r-V8LpfCy8Ie74A4f-lGyvTxodRUvpayxYGnK38YBymhsz7UK4-O0RQ7sbLJ8SYwZep85pgNbf5fPEXLorQlPbOjOGQufA86JLBXKH3fQGtLMwQqVBAJiqpULbVvfGw292tIHrNRb0TP2gYTHf170wJ6WDl0nyCbcgsriCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از دره زیبای هلد، شهرستان پلدختر
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662601" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رفع اختلالات بانکی زودتر از برآوردهای اولیه به پایان می‌رسد
🔹
یک منبع آگاه در حوزه بانکی با رد برآورد دو هفته‌ای برای رفع کامل اختلالات چهار بانک کشور، اعلام کرد که روند بازگشت سامانه‌ها به شرایط عادی احتمالاً در مدتی کوتاه‌تر از این بازه زمانی انجام خواهد…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662599" target="_blank">📅 13:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fouutVmfm9R71Ps04dBRCTPJnoODPKOh_20zli-rV5RqXSA7AG061q2nTxXqSyKMDpeF0XA0XtuXsVIf0CLrRf313BjMrSnK4Dk7MHUXO6g-b5I3YUr2UWHIOMy-atH9xcIR72FHslRzGQiHyuZc1hpF5R2VgT9SEI86eP75jQjFjZ9-deqnG7uVWpxokjE9KMI-HuzVpoXqOYSsQXTXT2pCIhnmMxqcCxNZdZCsN_O1lK3k7B9LWlWNYg4COHFHjghespTAJN9kt22Qwn2zK3YVL-rvHiuqilO7BcYRay6XADohw8gdfB4tDYOOnSHworxNFAymRw5rYpsyCN1M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هواداران ژاپن بار دیگر با پاکسازی ورزشگاه تحسین جهان را برانگیختند
🔹
هواداران ژاپنی پس از پیروزی پرگل تیم ملی کشورشان مقابل تونس در جام جهانی، مانند همیشه پس از پایان مسابقه در ورزشگاه ماندند و زباله‌های اطراف خود را جمع‌آوری کردند. این اقدام که بخشی از فرهنگ…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662598" target="_blank">📅 13:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxU8htVZeZ_PoI1aBmLatL4xHN5lG7Jz1m_2Wnzr0mjX1gGM4eed8k0Mnk6FjOqrdjC-jHH1i3Y6eoF6C8CSYMcPhf0NuVUbHN5mPDLwXdls_oSTTUWzSz6itke8wK8Z_qfw78_Ddagvfb9MT0uPZnOtCS9M_2LWum4hSlzs5g1aGxq0ixSLKUUk3-MOXKw1l6j9Imji_Ah9-_vavxRa6dWN5wIIKLfws38y8_4JPVB7lptOTt2oqr2LPMQyTZt9cGVmh7mtiQ4_782OlVQiuzvWzKQPIIZvhjmXjkBBEhF4pQCzYmVZxk55yM3ELqw3csp5ZOMpoU0Q8lcBt4knIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس دوباره صعودی شد
🔹
بورس تهران بعد از دور روز روند نزولی، بار دیگر به مسیر صعودی بازگشت و شاخص کل ۸۸ هزار واحد صعود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/662597" target="_blank">📅 13:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8d45705f.mp4?token=WCrroBEZvgj3xV-SLMF50S7T14Ry__kz_wKdvpT6PyuVUDtiCIHuTmbjSTcl6oVp4N3WNd2-SJa6hAJuJXcnWGtmk3V-ib95GvZFQXAO5r4KKd4VkaD3puBViw0Ee17Lpe_6XHCS4FJGnwuG1VoJcZYih9lfUKybU2Q4Ye-zH-l782fstJ11_I1nPcZ0vzMjGKq58PoADM2ilyN7W-Qb3TmmCiZsGQ8ga8ewr4glJGDcNLjm7wyNa5VrcgWfOelpTYnmBeAB37ZaAiwi6Aq-ijl4qlygsAEtrFD3frxvy8uN7K8DzoVN9wOjXwVmtVo92fVro-sccWhX59DzEG7Fcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8d45705f.mp4?token=WCrroBEZvgj3xV-SLMF50S7T14Ry__kz_wKdvpT6PyuVUDtiCIHuTmbjSTcl6oVp4N3WNd2-SJa6hAJuJXcnWGtmk3V-ib95GvZFQXAO5r4KKd4VkaD3puBViw0Ee17Lpe_6XHCS4FJGnwuG1VoJcZYih9lfUKybU2Q4Ye-zH-l782fstJ11_I1nPcZ0vzMjGKq58PoADM2ilyN7W-Qb3TmmCiZsGQ8ga8ewr4glJGDcNLjm7wyNa5VrcgWfOelpTYnmBeAB37ZaAiwi6Aq-ijl4qlygsAEtrFD3frxvy8uN7K8DzoVN9wOjXwVmtVo92fVro-sccWhX59DzEG7Fcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از هوای شرجی جزیره کیش| امروز
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662596" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ترامپ بار دیگر ملونی، نخست وزیر ایتالیا را تحقیر کرد   ترامپ با انتقاد از موضع ایتالیا در قبال جنگ آمریکا علیه ایران نوشته:
🔹
او زمانی که بحث جلوگیری از دستیابی ایران به سلاح هسته‌ای مطرح بود، از آمریکا حمایت نکرد. حتی اجازه استفاده از باندها و فرودگاه‌های…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/662595" target="_blank">📅 13:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662591">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6SqVLDiy4mGBeEbiyEDomsDp6BWUd9XzllYoOoO3MwpbK6OCfeyv_5W-k_gLDrUvMOnd1iCtTsqNTnw80FM41piqwla2CzI5uINPCNNsCgKck2TVzTFSETDMlQ50ftdrimVh_ZCu-ttMTMfwRSA7p4u6xdgmXy72p6j4V5tQqobQ1tdByD3-eiEwHb33yTqmF136VJoC-CSxhmHw7BrmqinO20O2DoMikgdY2uOxVk5DV9gATtHDzOSRUkN_PXj_kkF1qD3ARcuUMHyGOQ4SrVTN_3TGIP7fZfvvZQs9_3fR76NK7Nl9JE5qPT-y9Q_z3DXMLqCxJFqNujIohGCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dm_wiZYyHGqoa5tKV65vZsJ1dsmFhqTImU2kF9eGDBNE_UURWJ7F0jiLi-ecgVU4grchW5D8bzI-LILI2SXh2aqeSSPDoV2Sc_ssBNZwFsu7TdMm1QGXpnvAgtpBm7anMCuvFYp73MAQHxyKi37wSciZDVBzaAOv4fiAXusMMuFYqThqAIIbqCtFu46Qiz1AFO5w6lPIcNHDLck5m-DOrX2yDaID6FxDZKhZFyW0Yj5ZtuhRNar2E-7Supmwew6DksJT79FsBfzitABsXcVh_V-3Z5fsoRaTGALgDt93hqP7qF2WGbA5yZfxC3Vsfima8FjeySz2aQ6Z5MgH8vQXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYhidueZOc2nKtd6ZAWzLUXw1rkvIC9DRPAfQ5_OfJFjTKf_8ZvX4OzTe-kxrK0zz0cokBs2SUXWBXpgNnFwwJr3wJM8rcTY6sMJaFYVxN6qW2RVSVhYi5zbfQaGxPqxnHYqXhgSnwZylvPKxMHaixm3HnQOMmxOHdEeTr86asWcOk-a7o16KPdAj4zZ6GCFCi5rb1vTOhC5i_TMhGXMUUtabJ1NNdmYgMCy6a2bWPvhDhJNhsXv2jZWjzGtQygn3NeRZZSlvO4_J-CdrfUXXwNJAnUQqa06pnsHLrCTYOVzZMrIu0I5g4myUAbcDnjPW_6OtokyjwM4fZVc-pG2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtpahNoi8jq0TzAfIrQI4_l8-C_l9eeXPokrRov49r5YUvGLfB7mo9gfCje5AaiV-gZmCmm6GxpF140BVb9Ohbpd76m0LRMPSghrJh8VKdm3DueRbLL8NKyZr0zvMofMYTq2I2toCu8hdUlmuJwxGforh3qd1SvKBaqTWrSlMipyhteXvWvZVQamB5xM4v4tAJ_ZqIJ4_zSryz4IyItE_lkjz_vW253Gy9lVQ90sblczKL45PmqcNVI376OaA618zU4VaJ9Cnxte9h9ZteKEPedYZOb9lnBnwI7GVuU2k1zBR52ph-YsefbQjmq3p6-9siB1CiylUzMk_vF9BeAwOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازار داغ پروازهای نجف؛ قیمت بلیت تا ۳۲ میلیون رسید!
🔹
ایام تاسوعا و عاشورای حسینی قیمت بلیت پروازهای تهران - نجف افزایش یافته و بسته به نوع ایرلاین، ساعت و نوع پرواز از ۲۱ تا ۳۲ میلیون تومان فروخته می‌شود.
🔹
البته نرخ بلیت در این مسیر روزهای بعد از تاسوعا و عاشورا کاهشی و شش میلیون تومان قیمت‌گذاری شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662591" target="_blank">📅 13:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662590">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: تدریس هوش‌ مصنوعی از سال آینده وارد مدارس کشور می‌شود
محمدرضا احمدی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
هنوز جلسه‌ای مبنی بر اینکه امسال کمبود معلم داریم یا خیر برگزار نشده، ولی بنا بود از طریق ماده ۲۸، جذب صورت بگیرد و حتما مانند سنوات گذشته امسال هم کمبود معلم داریم.
🔹
هوش مصنوعی یکی از علوم جدید است و قرار است به عنوان یکی از سرفصل‌های آموزشی، احتمالا از سال آینده و از مقطع ابتدایی به مدارس اضافه شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662590" target="_blank">📅 13:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662589">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb19a5702.mp4?token=IKTZwWqGwSNuFQQ1-iK0FcPTsgTbu8zzgSuRkFu9AvVDSLGRQcXdvr-S16z8lmd6Tj1ZmEVWQ6NZk-KERWwrReInHEEo7UXOUaOG-eOEgGgOiDp7nOQX1gYW089gSaUVUL110cvoWAHa1wAO9exYoq7YPmZmUlImR4OFFpopWLCozGjekjAxRI1Z6OdLmy2au9BrVJuEPbWJ3r9YXTi0Vkf8GcvSFHf82jqstaJI7ufGFZ0OCKsHK0Ien2ubI3aJEI5hhKutG_25YBO3xvS5t9HcTAkEbNfZVPNN3ahfhOJ8ETRIIhfmaSPSywcqzIg2F5lw4yYJM0ePMDsAEAzNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb19a5702.mp4?token=IKTZwWqGwSNuFQQ1-iK0FcPTsgTbu8zzgSuRkFu9AvVDSLGRQcXdvr-S16z8lmd6Tj1ZmEVWQ6NZk-KERWwrReInHEEo7UXOUaOG-eOEgGgOiDp7nOQX1gYW089gSaUVUL110cvoWAHa1wAO9exYoq7YPmZmUlImR4OFFpopWLCozGjekjAxRI1Z6OdLmy2au9BrVJuEPbWJ3r9YXTi0Vkf8GcvSFHf82jqstaJI7ufGFZ0OCKsHK0Ien2ubI3aJEI5hhKutG_25YBO3xvS5t9HcTAkEbNfZVPNN3ahfhOJ8ETRIIhfmaSPSywcqzIg2F5lw4yYJM0ePMDsAEAzNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسکن مهربانی
🔹
مخاطبان خبرفوری از تجربه‌های خود در بازار مسکن می‌گویند؛ از صاحبخانه هایی که در میان موج افزایش قیمت‌ها، انسانیت و مروت را فراموش نکرده‌اند.
🔸
الوفوری را دنبال کنید
👇
#مسکن_مهربانی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662589" target="_blank">📅 12:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662588">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgSNM7q8PdfMg5Wpi05Ir8WblKkPQcLcaZM4lskWfUj7vLn0yv7CxIvQTyc_JCRi_L9St3grDI6iccN1o0aOe6ZINZo--kG0Os55J_ELZyAatsJiwJY-YvgHfXV8ieHV3SnNF9e0OrNhSnbzqkyjCB6McEk-vwDHIuZZZ3a_8HwAa9dhqueydM5HExrioAp2eYIJZZDBBEpNUI8qYibZAgcWmNS4NhkHjosMwx6IuvNszMhkvasJX0Y0ykGdOkzPhYE0GX8S-93rnO-efbsFBRcZ_jkk8GyULntS1bMaBEEHqQN1A3Y-KabugEgjwIBRaOmHA9VIsd4IJgbf3_Jc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گسترش «مسیسم» در آرژانتین؛ برخی هواداران لیونل مسی را «فرستاده خدا» می‌دانند
🔹
پس از درخشش Lionel Messi در جام جهانی ۲۰۲۲ و گلزنی‌های اخیر او، جریان نمادین «مسیسم» که ابتدا در روستای لا‌اسکوندیدا با ۳.۹٠٠ نفر جمعیت شکل گرفته بود، در بخش‌هایی از آرژانتین گسترش یافته و برخی هواداران مسی را «فرستاده خدا» می‌دانند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662588" target="_blank">📅 12:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662587">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نتانیاهو
:
حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/662587" target="_blank">📅 12:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662586">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
المیادین: عراقچی یکشنبه به بغداد سفر می‌کند.
🔹
معاون سازمان بازرسی: تخلفات دستگاه‌ها در حوزه تولید بدون نیاز به شکایت پیگیری می‌شود.
🔹
پاکستان: پیشرفت مثبت بین ایران و آمریکا نه تنها برای خاورمیانه، بلکه در سطح بین‌المللی یک تحول خوشایند است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662586" target="_blank">📅 12:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رفع اختلالات بانکی زودتر از برآوردهای اولیه به پایان می‌رسد
🔹
یک منبع آگاه در حوزه بانکی با رد برآورد دو هفته‌ای برای رفع کامل اختلالات چهار بانک کشور، اعلام کرد که روند بازگشت سامانه‌ها به شرایط عادی احتمالاً در مدتی کوتاه‌تر از این بازه زمانی انجام خواهد شد، هرچند زمان دقیق رفع کامل مشکلات هنوز مشخص نیست/سیتنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662585" target="_blank">📅 12:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662584">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d218c70bda.mp4?token=YTfnEJnY_JdYZAqh1GkyX7E8N8QL63pqUuifmkWYaRgXEh5YkeQTmCxhG1urs60GIDrP_PRYcihevQi8s69ImtdyZtkhcrA3_dH126gzIXuyC0HBIOszaLtWFp7ZXDUN9iuZ8UiSOKzQSABkEOaLe3Fw68irnesYGUGVnW-I_EqZw7UO6ghJsse_NxcDbjxV2myripcfmrabJBUOkF1e4fqDjT9WyGs-Gr4xqDGOxCY_ZbWJ5zRWYmXGr22lMZGdZRwp1SAWnYrdNWM2b-xOKhaVEVaf4zLNigT4x75jOnXfzVghB19LOYsUWTjVfqJ2NI850QijqBm1OoKIhT_xBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d218c70bda.mp4?token=YTfnEJnY_JdYZAqh1GkyX7E8N8QL63pqUuifmkWYaRgXEh5YkeQTmCxhG1urs60GIDrP_PRYcihevQi8s69ImtdyZtkhcrA3_dH126gzIXuyC0HBIOszaLtWFp7ZXDUN9iuZ8UiSOKzQSABkEOaLe3Fw68irnesYGUGVnW-I_EqZw7UO6ghJsse_NxcDbjxV2myripcfmrabJBUOkF1e4fqDjT9WyGs-Gr4xqDGOxCY_ZbWJ5zRWYmXGr22lMZGdZRwp1SAWnYrdNWM2b-xOKhaVEVaf4zLNigT4x75jOnXfzVghB19LOYsUWTjVfqJ2NI850QijqBm1OoKIhT_xBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهرام همایون: هر دادگاهی لازم باشد می‌آیم؛ اینترنشنال در راستای تجزیه ملت ایران، تیم ملی را از مردم جدا کرد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662584" target="_blank">📅 12:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662583">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baeebf9730.mp4?token=THDMrReG6DLEn9FddbmiZYKYDDL0DHeZaqPhnJGdYVNld3dDEY4ptmqBUlT3YMM8CpZEmzvt0LadXDdCpYvAKOJ5I54mKVbck9khtm1xIuLVXrCX_-bQ4JqbIwP5hHI_adDqLBcOUghm2VoXsN6y1jHFCZSk6oF3cmhzltz9Rrt5iWRwJ8iz7r2BUkWpBZZxI9ZrFaw5-GRit-eSW-jp8Dge8HTE7IYUTNYW55DeoA3De4I_-TfEGV5doMjrpwf1QDrV5T_r_qC5ENP_Fyw1LPhqujHCBjAUWKhB3dvzFiP11xQ2IXn2FgbIbpLEbLUq7ivYBexPzPObKN5CsV73aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baeebf9730.mp4?token=THDMrReG6DLEn9FddbmiZYKYDDL0DHeZaqPhnJGdYVNld3dDEY4ptmqBUlT3YMM8CpZEmzvt0LadXDdCpYvAKOJ5I54mKVbck9khtm1xIuLVXrCX_-bQ4JqbIwP5hHI_adDqLBcOUghm2VoXsN6y1jHFCZSk6oF3cmhzltz9Rrt5iWRwJ8iz7r2BUkWpBZZxI9ZrFaw5-GRit-eSW-jp8Dge8HTE7IYUTNYW55DeoA3De4I_-TfEGV5doMjrpwf1QDrV5T_r_qC5ENP_Fyw1LPhqujHCBjAUWKhB3dvzFiP11xQ2IXn2FgbIbpLEbLUq7ivYBexPzPObKN5CsV73aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفسیر سریع آزمایش خون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/662583" target="_blank">📅 12:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662582">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پیروزی پرگل فرانسه با بریس امباپه؛ در مقابل عراق
⬛️
🇫🇷
3️⃣
🏆
0️⃣
🇮🇶
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662582" target="_blank">📅 12:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662581">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس/حمله وحشیانه صهیونیست‌ها به غیرنظامیان در جنوب لبنان
خبرنگار الجزیره:
🔹
نیروهای اسرائیلی در محله دیر در نبطیه الفوقا، جنوب لبنان، به روی غیرنظامیان آتش گشودند.
🔹
پس از تیراندازی نیروهای اسرائیلی به شهروندان در نبطیه الفوقه یک نفر شهید و دو نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662581" target="_blank">📅 12:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662580">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وضعیت خوب سد کرج ۲۸ خرداد ۱۴۰۵  #اخبار_البرز در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/662580" target="_blank">📅 12:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662579">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
دیدار و رایزنی قالیباف با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/662579" target="_blank">📅 12:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662578">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d90aca8726.mp4?token=kY9JmjWWliu-tx31DSefSlRCYPZAtzi4jsqJbMWjrz4OBgAwBVEs-N7jOSIMS_RIvJWQqHgUBeugMIm2ToYGDCVg9Y_oxsnt5xSiQB41jBFzJeSpw3QBD6IewzkzYclhg2AE8y2-WG-w8GQl4wp5CU2T8YpgSW1Y6UG_mDPLirjYTHQ3Roey7uumyrezhQDGmfXJIotTl4fiMlYefePDPxWsFCXjJ752UjzyXliVBW43NMVL_m8hoyQFobudZfhvT3uZRh56PIsr-sOQaYtM_WWLOUzPzUCYLI2cx10RWrVRcTZHwM74yBdCIAU742gGh2p64J6y3cOvp0Hz5xnCLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d90aca8726.mp4?token=kY9JmjWWliu-tx31DSefSlRCYPZAtzi4jsqJbMWjrz4OBgAwBVEs-N7jOSIMS_RIvJWQqHgUBeugMIm2ToYGDCVg9Y_oxsnt5xSiQB41jBFzJeSpw3QBD6IewzkzYclhg2AE8y2-WG-w8GQl4wp5CU2T8YpgSW1Y6UG_mDPLirjYTHQ3Roey7uumyrezhQDGmfXJIotTl4fiMlYefePDPxWsFCXjJ752UjzyXliVBW43NMVL_m8hoyQFobudZfhvT3uZRh56PIsr-sOQaYtM_WWLOUzPzUCYLI2cx10RWrVRcTZHwM74yBdCIAU742gGh2p64J6y3cOvp0Hz5xnCLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از درخشش دیشب مسی، امباپه و هالند، امشب نگاه‌ها فقط یک مقصد دارد: رونالدو
▪️
قسمت هشتم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662578" target="_blank">📅 12:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtqXlSMLgrhVlE5UagaOFRHNXsZuH7NZKBtYYknlDqp4XivfFN3NwE_NzwcxEee5ZvxH3k2DiINrvX-O6Zrs-PM0hkPKvdfYXmLsKzct1iENUX9dEQXvlE5Exe6wUxYL6aIx2yEBJWz9-vcWX5BD7vlhFv8aCVWljNxF-KpTeGOR7sUmufiJRm6_3tzt_wLYV2eGAgxj0VUw9UiubvApLWz-m1miBPR4rNmz4PTBxnjtdJWE86jbuQ0-2kAVY9jhgzZtAji2y3hI5jOHB2rtf47vay5d-AD5JoRt_YmAcA1GZzeT1-lyODvlgnbuVkCtY8kjPDLPPhh3wivJ2JFlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LFncNrfjg0Cg8V_c5x2N371xhrqx563lKkpqlBJhPfh22RqEuItBDwtxbdPiQNHyXd59S703VVEylYGieAJIB_hYu6LR_UuID2521h2tTC0r0Tu1S6X2FTP8M_ILpYUT06hjuyVPNYUvGtfsubMoq3hGJPx9S-9qNnp4P2Y5-c3wBWXcsKDx_8yT090zsVJLDBJKrsCOxOIYVlb4lNfk_Om9YLQpJRWOv3sEBXjoaXDKg9Mv1B-_RrjwOGmV6Bg4koWp-NS0yoMXIGmczVNBgvFlOza8s7rTtGdHpkcpeoxIIb3b_GSl0mqGi6W9CwVvRkUg0i-YOKwQNVFFYvj9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PW6JvN9gCyKh8UkLUR6KU7g68EEAME1urQ93nh8zH8CIYLqCpo_Kup7NiXq2BLTwQ2waRCfHcmaEUsGsIsJRtmDvxVVLfI7mnYgZ3jB-6BzJz_0eOsZpUs-lIjDP0kJ76uTAS1155c_d1dSM7GhAq-Ok-84cP4FPaiCuBB82eQP1BLURM1Sq5529mFj3zV_mq_R23dSUu1Zchgq0_qjmeuPLZlVDBEXZ_pcNp45WFpjltV6UBG3RNxxJndSbtmTLQft4cTcJGbg4BxIA2GVFQNYUVYNprGOjAdKU801IorqMWqYbQjO-6GRByBeOHuD74QoZnjAojs1hH8myYHP78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntF36T3UhpfnW3bZXtqQx87pe4Ftp6WJe6ejNO3su21KKCViT-YX7whR2Ae6BTNQ3yo_qzSaH4Udu6lIaKB_0Eq_RzH1-tPTQG50mGzggj36rBLM3KpZkSODexbw6MFkSv6vlx4IJV7cXBVy-SAO3iTnMFIZ1dgeRjlf9C8GPUBiUIQ_ZVyx-wGdnpg0TsvT9vDS_aDiPrsBtob8EQWZhj2spu1oGqJJ5X2cm6C80E9mD-KGoxBOcItfGHxCJ1SUWJC9_TJ6tAfU0bVjw1zySRvkjTt3aljpzERz0PKqtxnBFelK6zByhSPI2KldbauBD-aGwMhubtf8YPKJ8vkvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SW0FkEO0argCSpFS8m3Wn0iXJJvj9GCLeETRSZJE1lWVQ3TABcc4W7WPKdN1IBFTPZWpG0W0B7IhEQXAqUO1oJOGLe5cdCcNt37oKr0BGav8t3zUAY7BFN6b_opZm7VXbgAyQBTuBsvOsH9aKUSRkd3cnDdTdbPMmae2xGmcwhP5s5waOtRbDY4D7ZOnANsXHQQMgbu2QpyffFMgUd0c_jE4Qky-2vkhj3fCidAbCj8dcyK_TkjmnKvCZ4pUBR1heW8ILjbcwu99azuVTeHKbR_X2B8uNk46nvQisWYG5GlRO0yElupjJT7MHdmodZhyOG6XXK-xoHFL1rYJRd9G-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtA2VT8wAuYsewImCN9xpBM0Wke3V9kE_UP3wOIGrACFGAIGt82Bk9q-cWomZR1tQC6BQfzdOKi8qmsUn4Qtcd59-M7iexiVy227c88O6OFBy41b9guFA8-_7YqzpY2CdsOKu4tUy107NjUDiYQ9joRifzUHmJshaKwPJBdSdZ4BifyEa8CPv9qeNiftmXQDfs9Gy4fOODPLTtoY9t10Opbsv4ddozFpFi7imFEF7L9imCq6C3N6yQiOek_WdkoGVEIQfol8ZQ3iLhEm2Gys3-o9JS_K-vmOdgvrwjxqRpgEf-THxKD1AHVg4WmcQZuVbB6P4UJ81m0wytM78SuNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/df3EU-GWxpaccfwmM1zaU5lTSOdGUDJyRoRHAqEbXH9-zgQyCO9a2Uily3D9Wynm9LmxKuBvZ5Hq8A7XEecdGYuGyLrYIPfCeub3wEyolo1lmqov-DVWFtIXRkmbkbb9gd-hlODckju3s8w50ECQISyyygReVZyTTXhvEv9-QuOCLdrj7xWmAq6IR0Bg9M9GbQyS1QVK6s06mRmKLUK_e5Kj5FCYAWJkLJAwlplvRDGCkBEXlNob_1h7vA6msEr4M6sgRAZKQC_Pryba9SS-DVTBtjqVO4MD13n7pqMgdxn7VXozX1O3E4G76yuL_79mLnjL7Ty660N957pdikwlEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نروژ با حفر نخستین تونل دریایی دنیا، کشتی‌های عظیم را از دل کوه عبور خواهد داد
🔹
نروژ در حال اجرای پروژه نخستین تونل دریایی جهان برای عبور کشتی‌هاست. این تونل ۱.۷ کیلومتری از زیر شبه‌جزیره استادلانتت می‌گذرد و جایگزین مسیر خطرناک و طوفانی استدهاوت می‌شود. ساخت آن از ۲۰۲۷ آغاز خواهد شد و علاوه بر افزایش ایمنی، مصرف سوخت و آلاینده‌ها را نیز کاهش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/662571" target="_blank">📅 12:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
خلاصه بازی اتریش- آرژانتین/ مسی آرژانتین را با درخشش کاملش به مرحله بعد رساند
⬛️
🇦🇹
0️⃣
🏆
2️⃣
🇦🇷
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/662570" target="_blank">📅 12:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq8qr1i-NYCKnv1p70lh-iSWE3p167fRn4pL5rM5RGh_Ycus50rTXhziByQQe-sSANjztXMfEpl4KYCf_raq5_3OPR7jFtYZPPVuTiTzffF4Cph_rMfm5tr3WLobFdOOVDVya0RMDz-960L-kiYWfQZDwO16J5_u_zdD7YaHf8keXO5fT2HOw7Uc67K9B167TEIoYQT1MrOudY_6uxLRpYsOLMxHM4k3_c909_ngAxDkqH80Wy7JHTg4WX59XYVqQJsk50iWeUZSrxpKOUn8GwkqzNjoQr7qYV4EAh_-a88JoJB0NN_2iDVGvYW_01yzd6P6I6h8UYndw6duyJwVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش ۵۰ درصدی فروش گوشی هوشمند
🔸
فروش گوشی‌های هوشمند حدود ۵۰ درصد کاهش یافته و تمایل خریداران به بازار گوشی‌های دست‌دوم افزایش پیدا کرده است.
🔸
با وجود کاهش عرضه برخی کالاها در بازار، به دلیل افت قدرت خرید، احساس کمبود کالا در میان مصرف‌کنندگان چندان مشهود نیست.
@amarfact</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/662569" target="_blank">📅 12:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هشدار وزارت بهداشت درباره غذاهای نذری
رئیس مرکز سلامت محیط و کار:
🔹
در فصل گرما، نگهداری نامناسب غذا به‌ویژه غذاهای پروتئینی مانند گوشت و مرغ می‌تواند خطر مسمومیت غذایی را افزایش دهد؛ در دمای بالای ۳۵ درجه توصیه می‌شود زمان توزیع غذا حداکثر یک ساعت باشد و طولانی‌تر شدن آن باعث فساد مواد غذایی و افزایش احتمال مسمومیت می‌شود./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662568" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxG0RaY40po20SOWzIGZRxW72bot093P2HYkjs28AQTOdmv08db_JAZdk5zrVHdoe1_XrW5KKqX14kA1_OTTXRfV4YL1OqTIVRIdlzLV-Ert0orvVEjKQ2RB6M_QiCvlqKXx_2tYSW_GWLNsez0mdiz24-cspsLtChYSwUfU-_ew6XfInf1iDQQDHdqNHqZA8an6LX6C0jT8ha6Ax9Ra_hzgs_tMX0Cpfmj1VXhlAX2udIYvjsF2nUZFt4MwsmB5HtQu-ARP9ZOXQmsma7lgdseVRfAtR-wKE4g6IAxeOgLNSo8faMOyiuW0qtyc4e1XV329KRSopibYKiu-pPX4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
هوادار ۱٠٠ ساله معروف مسی هم در ورزشگاه
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662567" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4om6AyeTRqIlb4ub5L2kKx_RQiGYaENLotN-flyXRIBoqSPAoVOEDzlnbkYgSPaQP0XTC1Yyy4R9Z_qqKXj35ORE_xAE54y49_Jf7D7H0TiPayGnYl0quiv0WgrgunBpGMhq_dHgFBNRr26jSQfbF1nMlAJyuhm7v_I4Od2ciqmI3meLUTCEUEmEVEwKia4eCw4FsghQbtfS6sH0mSGgtSp0_pPYPlmWloDwlAS7sL35Jg2DELTNYFt91dB-fa5zbYO-0Y5UBYQcV2hnYbww5t3QFdj5GlNWykDcnma_K_bfsk8zc4kmMYrjpo_C2BpmJ6h13Cb16hcEeg53OOSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایتی کوتاه از وقایع روز هفتم کربلا #به_وقت_حسین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662566" target="_blank">📅 12:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e3805d07.mp4?token=kBEWfd7-nlqIDacgyk0w0HpudSqMSK8-gkjtmsjNWxkBQqhh8ObHn8uaVUUWZssLXPLiHjGqrpGZY0lkWmtxnORI_8t6ro-oGLkXZeE_LCMXQZioZH23bPK60ucdAQ6wd4V90uCpxGTKp8BzA6dKTo6nR4ykw10Uk6b30WSY59d9vfRYmeH-TrB2OQ2WR4t0wcpQQrvnHGdHJjCPfw7eAkNimK9UJz02VDZZos82VklxRkQr1Dwsrd-3T2JDWxwSYLLq13xX-WSt7VJgKoobKcfiVYMhl8keJjqk3INH-i8ScPxvxchvsDl13lIE5L18m-EGlQiTfYKplFFzzg27NyjuNDHj4Po0D9zwhF5KU1-srORyX8hGkn5-2hDrYTKVy_KYiWUDM2_X4Ioh5320JRia_DqVFMMfwH-Wzgu3hQ0lBWmkLL7zGm7q8tU_DbkAhUe6wamTraX37Whmwqvu4-q4zjJOP5xpfB99yfd6nAvI8VC7p_b-egNbzh-DyzTajMzUYXssyx_AL0cHg73j10OsbKKsKL4deAwAvrwjNpxznTrONdmMoki66sXZFVFcxBBzMlEX4-p73TFyjvi1HTKcEHI7cjtsXkOuwIrbIfl_24GBMpTF1w48S5nJ6A6RN0EBl5ksnOogQdtNoGJlMF-B7yOM7y852R7qEu6ad80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e3805d07.mp4?token=kBEWfd7-nlqIDacgyk0w0HpudSqMSK8-gkjtmsjNWxkBQqhh8ObHn8uaVUUWZssLXPLiHjGqrpGZY0lkWmtxnORI_8t6ro-oGLkXZeE_LCMXQZioZH23bPK60ucdAQ6wd4V90uCpxGTKp8BzA6dKTo6nR4ykw10Uk6b30WSY59d9vfRYmeH-TrB2OQ2WR4t0wcpQQrvnHGdHJjCPfw7eAkNimK9UJz02VDZZos82VklxRkQr1Dwsrd-3T2JDWxwSYLLq13xX-WSt7VJgKoobKcfiVYMhl8keJjqk3INH-i8ScPxvxchvsDl13lIE5L18m-EGlQiTfYKplFFzzg27NyjuNDHj4Po0D9zwhF5KU1-srORyX8hGkn5-2hDrYTKVy_KYiWUDM2_X4Ioh5320JRia_DqVFMMfwH-Wzgu3hQ0lBWmkLL7zGm7q8tU_DbkAhUe6wamTraX37Whmwqvu4-q4zjJOP5xpfB99yfd6nAvI8VC7p_b-egNbzh-DyzTajMzUYXssyx_AL0cHg73j10OsbKKsKL4deAwAvrwjNpxznTrONdmMoki66sXZFVFcxBBzMlEX4-p73TFyjvi1HTKcEHI7cjtsXkOuwIrbIfl_24GBMpTF1w48S5nJ6A6RN0EBl5ksnOogQdtNoGJlMF-B7yOM7y852R7qEu6ad80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: عمان و ایران هر دو دولت ساحلی تنگه هرمز هستند و برای اطمینان از تردد ایمن کشتی‌ها از این مسیر، باید هماهنگی‌های لازم بین هر دو طرف صورت بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662565" target="_blank">📅 12:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFbdeYRYBcC6iFclWXFRqaeP_vAxPnJWsWh_7MsJzG30a40edLUfFrTZCiISm1AfgOasBabe07DPpTE844fou5xDhWe3NUeKXg5q1TyDb0FBg5inUghSgNd3wrLZ6Nef42KznMEyPqBle5FyTqsfVXxQL_T9IEC7ys_bBz0rw-uanypqDHNp_WwsmkjwMRs5diV7Te0izGEaC0-ZnRytS3Fef40dkURIKVDgulLv0JcmuZJFw9brMB6stTy0OdwmI1aEHl77kMbD6mTQRipRTqtqhvM6WHzdc_D8nQmNqiBbRn2fRJoOvLJoUPXsSlUGwCLNNgaX1aV-E6fB6RC9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حفظ امنیت منطقه و ایمنی کشتیرانی در تنگه هرمز، محور رایزنی‌های هیات ایران در مسقط
🔹
خبرگزاری رسمی عمان گزارش داد مقام‌های عمان و جمهوری اسلامی ایران در دیداری در مسقط بر استفاده از فرصت دیپلماتیک کنونی برای حمایت از تلاش‌های صلح و تقویت ثبات منطقه تأکید…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662564" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662563">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بقایی: ظرف ۳٠ روز از توافق نهایی نیروهای آمریکایی باید از منطقه پیرامونی ایران خارج شوند
🔹
جزئیات این گزاره باید در حین مذاکرات مورد بحث قرار گیرد.
🔹
یک تعهد دیگر این است که آمریکا در حین مذاکرات به نیروهای خود در منطقه اضافه نکند
🔹
ما این موضوع را به طور…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662563" target="_blank">📅 11:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662562">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
بقایی: مطلقا موضوع توانمندی دفاعی و موشکی ایران به هیچ عنوان نه بخشی از گفتگوهای ما بوده و نه هیچگاه موضوع مذاکره با هیچ طرفی خواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662562" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662561">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: پس‌از تهدیدهای ترامپ مذاکرات را ادامه ندادیم
🔹
در وقفهٔ بین مذاکره با تهدیدهای موهن مقامات آمریکایی مواجه شدیم و پس‌از آن نشست چهارجانبه تشکیل نشد. ادامهٔ بحث‌ها فقط تبادل پیام از طریق میانجی‌ها بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662561" target="_blank">📅 11:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662560">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقایی: توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662560" target="_blank">📅 11:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662559">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=PHZ9wtiylzCxUAFxlhKQIde09J9IYn6dIVIM4Ek2h1F-5J53ae1z1kyH7VkMfcsTs2UIFNmET83kz6eQL9ZqSPXU3VrAaA0Ns3seTSnwA9EB0lifla0CDGpThKlSzXhlhfyl5nT-Sv_vSkNyS3XRVIlrcTBhexKjNWd8kNl6dyfL6w0Mu7iW0NNRqpCaCUzBpp1Mog_XkWLDdqdZwkiOjb41VU4QmjQqB9lxz12AH1MuinLSTdo3j6yVGC04V1XWQFAJt4kUyG7YV6IvQH79X3Lt8KYPydrBHPgmyrkXkKdL_8URItJHRh3XESACxsGlHMm51pGrWcKon1oW2bqb-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=PHZ9wtiylzCxUAFxlhKQIde09J9IYn6dIVIM4Ek2h1F-5J53ae1z1kyH7VkMfcsTs2UIFNmET83kz6eQL9ZqSPXU3VrAaA0Ns3seTSnwA9EB0lifla0CDGpThKlSzXhlhfyl5nT-Sv_vSkNyS3XRVIlrcTBhexKjNWd8kNl6dyfL6w0Mu7iW0NNRqpCaCUzBpp1Mog_XkWLDdqdZwkiOjb41VU4QmjQqB9lxz12AH1MuinLSTdo3j6yVGC04V1XWQFAJt4kUyG7YV6IvQH79X3Lt8KYPydrBHPgmyrkXkKdL_8URItJHRh3XESACxsGlHMm51pGrWcKon1oW2bqb-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/662559" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662558">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e39941421.mp4?token=bfLdBJ4hRuw8YhY-8qWZYbBp-aW9hmyAPEAo3Id3YhEpK4dHLx3SD3PvShwlEaWbztozZsuyrO6Q90xE60Xfvs92WWyxRGm5sMNagdI4U4mJDrwhpjnPxuMK3sOXRfOy4PznEaeSl1I0A4TaIAxTtvDI9mDEEho79glGAxDF8L5f6qCVFLOckW-c4SVp8McRxovKeSCx87jud8QewqWcoiYwsrQJJ0VXJA_SMvKCzjrbJ8Ciw2dKAA_FyDB2eeA_LnobxsoDTHO3AldI5miEGirOYFx9cWidnw-UWKb1Mgsc2ngSed-j0tKt3V3blAMmBt5WVQnYdKzFosxMWn5tkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e39941421.mp4?token=bfLdBJ4hRuw8YhY-8qWZYbBp-aW9hmyAPEAo3Id3YhEpK4dHLx3SD3PvShwlEaWbztozZsuyrO6Q90xE60Xfvs92WWyxRGm5sMNagdI4U4mJDrwhpjnPxuMK3sOXRfOy4PznEaeSl1I0A4TaIAxTtvDI9mDEEho79glGAxDF8L5f6qCVFLOckW-c4SVp8McRxovKeSCx87jud8QewqWcoiYwsrQJJ0VXJA_SMvKCzjrbJ8Ciw2dKAA_FyDB2eeA_LnobxsoDTHO3AldI5miEGirOYFx9cWidnw-UWKb1Mgsc2ngSed-j0tKt3V3blAMmBt5WVQnYdKzFosxMWn5tkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلفظ درست ماه‌های میلادی و مصادف تاریخ شمسی آن‌ها را یاد بگیریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/662558" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662557">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800218067c.mp4?token=RZ3V7TwRa4IZKrFo60f8rJiiciec7QNBr6kVbp7jEPeb7duompxW6Th1JNKEcOmQZQNwWt0qABeaYpPGzBIOo-bm9RCx4K7D9exJFaSYpQryQ9QRtp1HftUbJHlTQTl7aoZ-8tX5r5oczW3oOASYm6JwIA9RhidPrcs4q8GnMJfIb9QbHQbmxClQVM9rHV9D3vw4wMYTu_PO36fIWeEhr66H-ey6X5msCxjOkZFueQixZ5cD1jpDi4-RBm6oRNzsr1l3Z7WQ-WjSNJoEXlZrreZTEEqrgrVNI-2bxM95pWeCBVH8W0YudL_RYafuvSniMtrkyTl6RTCy2A_PUXOZxyt-mdG7YL0n93REpeTd8YRgS2dE6XPZUzmpLT3HjUHlU1YAcFCroht0XNP6s87uYXj_ixfme5v-OEyFaa58WQs_mBuvz7LzCQiADu9I1FBTDbR_fi0T0cPrNDi-n5ElyfuahGMqj3aciGojYuXxBrs_zqn0LDrrIW4n7kGME1n1H_gmKPL-hUa7sKDN-XvtiIhnfrnkG5_dRXCoc910-wgLJqiLzrmM68ooxrbgwissdv0eniW0F1A7jWghZa0P0Bd4Pw4Vuy5BNapPSSLMSqN-8CLubDKLgjGCIfUBuWIa21dXjcPk8QNcmaRiEhOEo78LOZ6hdDXzO1YFqktGYCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800218067c.mp4?token=RZ3V7TwRa4IZKrFo60f8rJiiciec7QNBr6kVbp7jEPeb7duompxW6Th1JNKEcOmQZQNwWt0qABeaYpPGzBIOo-bm9RCx4K7D9exJFaSYpQryQ9QRtp1HftUbJHlTQTl7aoZ-8tX5r5oczW3oOASYm6JwIA9RhidPrcs4q8GnMJfIb9QbHQbmxClQVM9rHV9D3vw4wMYTu_PO36fIWeEhr66H-ey6X5msCxjOkZFueQixZ5cD1jpDi4-RBm6oRNzsr1l3Z7WQ-WjSNJoEXlZrreZTEEqrgrVNI-2bxM95pWeCBVH8W0YudL_RYafuvSniMtrkyTl6RTCy2A_PUXOZxyt-mdG7YL0n93REpeTd8YRgS2dE6XPZUzmpLT3HjUHlU1YAcFCroht0XNP6s87uYXj_ixfme5v-OEyFaa58WQs_mBuvz7LzCQiADu9I1FBTDbR_fi0T0cPrNDi-n5ElyfuahGMqj3aciGojYuXxBrs_zqn0LDrrIW4n7kGME1n1H_gmKPL-hUa7sKDN-XvtiIhnfrnkG5_dRXCoc910-wgLJqiLzrmM68ooxrbgwissdv0eniW0F1A7jWghZa0P0Bd4Pw4Vuy5BNapPSSLMSqN-8CLubDKLgjGCIfUBuWIa21dXjcPk8QNcmaRiEhOEo78LOZ6hdDXzO1YFqktGYCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/662557" target="_blank">📅 11:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662556">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/662556" target="_blank">📅 11:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662555">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207303375.mp4?token=NkmWgukWo6eKuaiIQiUtOM_m9gIQio0onNy37lpOewB5nHOUJXDJJkicfXf4vqLGMnG5XYDsa5OvJKy_QvLJLodT-ox5VI4UMhYrwgdqs5W-y-HnGkInSfKYawu--ukpHx6Yg-ZET0F0rXrxSXoeAWpXNbW7W0PP7lpFSFTo0OffoZ7KDzdeJqxdcfaLKypk5QJC6Age9W354ldWd_pra05W8Kp5OFYEe5M1KQ0hCa_kzFgPXHgQzdj6a1We2k4e7ufskvBRWon4WtLclYHW9nf2QKQokLtxx0uhqYXxPoe00hn8NDVC079BFBgFPTpLGpxrF15cNPhEu6GfOzjWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207303375.mp4?token=NkmWgukWo6eKuaiIQiUtOM_m9gIQio0onNy37lpOewB5nHOUJXDJJkicfXf4vqLGMnG5XYDsa5OvJKy_QvLJLodT-ox5VI4UMhYrwgdqs5W-y-HnGkInSfKYawu--ukpHx6Yg-ZET0F0rXrxSXoeAWpXNbW7W0PP7lpFSFTo0OffoZ7KDzdeJqxdcfaLKypk5QJC6Age9W354ldWd_pra05W8Kp5OFYEe5M1KQ0hCa_kzFgPXHgQzdj6a1We2k4e7ufskvBRWon4WtLclYHW9nf2QKQokLtxx0uhqYXxPoe00hn8NDVC079BFBgFPTpLGpxrF15cNPhEu6GfOzjWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید درباره ایران: این فرض که ترامپ هرگز قراردادی را امضا کند که به هر نحوی با توافق فاجعه‌بار برجام که باراک حسین اوباما امضا کرد، قابل مقایسه باشد، مضحک است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/662555" target="_blank">📅 11:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662554">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b824858.mp4?token=tcrEtVzCJvkdCPtQQGZpZu0Nw7D_89e8GI1wyZHJB9C39mOq1Tw36inSXXRW9SYQmkCbi_bwv_09lO7aH21eF6S5W1EQnmp_n_jpIeCqu1avheHhO_e5H2fdQWVT9piPBaTFjeGp3Qo43F4CKhtiZp0Fy_8XCurJvSoYuDCgTSgWL8ZCIE4bvBxYIk2mafUSj4EJJVNQ0ZxtbXdfhcvJy0vIw92HiRZ1HSYNYVB-DC7I3X7TAJlG8bUc_r80dgWrYozyNm045n_5QKXpGqI3j68rXNYe2ECzXuPgQt8o4IBGh84iujt2gnNJ24OCC5KsIWVw7lgHKQx98LbXyJrdoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b824858.mp4?token=tcrEtVzCJvkdCPtQQGZpZu0Nw7D_89e8GI1wyZHJB9C39mOq1Tw36inSXXRW9SYQmkCbi_bwv_09lO7aH21eF6S5W1EQnmp_n_jpIeCqu1avheHhO_e5H2fdQWVT9piPBaTFjeGp3Qo43F4CKhtiZp0Fy_8XCurJvSoYuDCgTSgWL8ZCIE4bvBxYIk2mafUSj4EJJVNQ0ZxtbXdfhcvJy0vIw92HiRZ1HSYNYVB-DC7I3X7TAJlG8bUc_r80dgWrYozyNm045n_5QKXpGqI3j68rXNYe2ECzXuPgQt8o4IBGh84iujt2gnNJ24OCC5KsIWVw7lgHKQx98LbXyJrdoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/662554" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662553">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcZnFRdbJs77H_ThyX9aWewehxcD2mXC1YSxyk7DFZyWsoS9tN0qoNu1_9OT1HdlzElcOOVw1aH-5GGMie6OSWe2TeQrN9HPnPkY6C27o0q38eCXilscmzURJDnG2FTF_knN_95RGWNp7Tk7LSqzQuy4osmEl_7mEGaemXmUB7J0I2oThcDDy2wekUCcp4ovvZclbkY7DDVeKIfIuSE6L9r2xaFcxaR6FNUoTSou95xyzLPyS-46Ny8KbmIi3v0VYmTpZI0FC92Uk4BYrjhRmY8-rMXU6YH7P8XaHNjW_9Mr6XGqbBBnVLjLShxFCyQODg0Y52UsaC4MjnTvIclh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدافع مصر ضربه مغزی شد/ غایب بزرگ مقابل ایران
🔹
حسام عبدالمجید، مدافع میانی تیم ملی مصر که در دیدار مقابل نیوزیلند دچار آسیب‌دیدگی از ناحیه سر شد و طبق پروتکل پزشکی فیفا از زمین خارج شد، به‌دلیل ضربه مغزی حدود یک هفته دوران نقاهت دارد و به‌طور قطعی در دیدار برابر ایران غایب خواهد بود.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/662553" target="_blank">📅 11:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662550">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bqe7ET5xnn-XFH9m6yi5xQX7_6imni4jcGoh7zmPNoKflTGVi9tKl_HOSR3rBCWX9nYRNzE5P08T-h1Sr4oe5UotWn5CxtYWp38VpGByqaxujsTCqbw-XvPl-_H95qO1ThYWS5s0OHi59G80gMIlfrzetE6uAAlvvInkxyBheHY-TAn20CAjcNJYb_1gH5vw_HuF_-Kt-ujKxT-3Q2umTnE6j145QYR_CjI1eybJsajRUlsMxxnAsCPMzF5DgvfWFTsuHHgpYoFMpcpYICuTmcI5pQIw6BXM9MWIt0kghVKk5PRlKgRCj_1lRjw87gx_2poG9UeXXQzusI4ASaoRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob-RcHQoOWMtn1E2hMBec9MKiLrzYoHHWur2RwRIs31Vxe9xoAIJMw-LdFVs6YXx8WiAFTBfUOzbJGjuhmFjJ0eEzvGhJyQHoFdHp8BAYtE_IpM4wrJWVhtAEDchmnbefDBuGK5nOR_5aPUt5v06E39SsJ5uRFoiWTdE_VtPpXaV8jyDeSzF4VkRnr6fsd1fzDCYx0IWVMMO_l3V051IVlOfcrL_Nib8-aXjNpOcaM7cYDYWw22GFV4uxVj08oRDLuHkKCNlwSo3kZ30FnlOfa1y_Qswpy-895GrTH84sP7abta-rQcQ-RMz6ksyPNC8ogsO3wdv8lDypLIpRiC_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXBznDzr70clRnMRARUw_FpA8jqDln9vF0PfbsDaAwnuGTyOZAGsoR-vu-1_uqdRdiZM-IFhZG_ynD5x579X2fPYViZKNdv_wj-OoJ2C8VrtKCLrJ60td9kG-VsJ1gh4tGm0lrtkAh4DabzjF7Aet8VgphA4Z_Xkzgp8jo6MwuxMtBqhSQuGOffTzp8vqlWYtVCW1ZVrnAahNxbk9h8w0xhQsPsPqCRdhnTmn5XuN4k-VonpH_9vOAJcnShfomgtKz06_ypEDXx906z8k5sugIbrBx7AP-Wrs-0a96XP9uIs60NtLldjOBGEqJBTLfUhGXys72xSXD1lk_V6VWptNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بازی دیشب فرانسه - عراق؛ زیر بارش شدید باران
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662550" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662549">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مسیرهای مراسم تشییع رهبر انقلاب مشابه مسیر راهپیمایی ۲۲ بهمن است
معاون فرهنگی شهرداری تهران:
🔹
مسیرهای مراسم نیز مشابه مسیر راهپیمایی ۲۲ بهمن خواهد بود.
🔹
بیشترین حجم تردد ورودی تهران از محورهای غربی و جنوبی است.
🔹
تهران دارای ۱۴ ورودی اصلی است که بیشترین حجم ورود از محورهای تهران ـ قم و تهران ـ کرج است.
🔹
در روز مراسم، برخی ایستگاه‌های اتوبوس فعال و برخی دیگر غیرفعال خواهند شد.
🔹
فاصله حرکت قطارهای مترو حدود ۱۰ دقیقه در نظر گرفته شده و خدمات‌رسانی ۲۴ ساعته انجام میشود.
🔹
از پنجشنبه هفته آینده تجهیزات اطلاع‌رسانی در بزرگراه‌های شهر تهران فعال می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/662549" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662548">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0158a349e0.mp4?token=iE6kHPCGZU6XmTWDEP7S-WfjWRl6UDzb7_IBxoQ1BPPedvfQQ6Au5mxpdQnoMkjwZu974uZoRx9R9aRVYpi3HzbOk3eQ-N3qItWH1zxqu8xiziWKLUPN3VVe61TEfSwNP8F_NFazPN2yff_Z2k0koZYCSU51lDTXacIjJo9c7cOvnpQgXDPK9iT_6AWhRZJzL6te9Fdbr7De-mJSSncEO9vRAh_iOtIF4ZRgpFlPO8ONErLsoOJNricsminFR4JIRO_bO4cAuRdzlUh2C4ukSBRB4q7LHwqUKnCEZay6JhQFnH4iGrCWVHVVY0_YomVOc2gGvClK7kwGE9NvMb2HDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0158a349e0.mp4?token=iE6kHPCGZU6XmTWDEP7S-WfjWRl6UDzb7_IBxoQ1BPPedvfQQ6Au5mxpdQnoMkjwZu974uZoRx9R9aRVYpi3HzbOk3eQ-N3qItWH1zxqu8xiziWKLUPN3VVe61TEfSwNP8F_NFazPN2yff_Z2k0koZYCSU51lDTXacIjJo9c7cOvnpQgXDPK9iT_6AWhRZJzL6te9Fdbr7De-mJSSncEO9vRAh_iOtIF4ZRgpFlPO8ONErLsoOJNricsminFR4JIRO_bO4cAuRdzlUh2C4ukSBRB4q7LHwqUKnCEZay6JhQFnH4iGrCWVHVVY0_YomVOc2gGvClK7kwGE9NvMb2HDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشگل‌ترین انرژی بار دنیا رو اینجوری میتونی درست کنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662548" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd57389c4d.mp4?token=SWTITfuiWNvz1jkRmBvbp4r1wAvGBJO0ehV7zDXzf9cx1MUVNluU5ISsymyYRSPMNbtobvve3xHsBKyPE9liyNY4K9livFOGC2-8MKmUzAhmibw4TA8RP8vn0tqLaix6akNMvi8u4KwRfUb8iGcrJNhP1dxtIKhqqXWOrpULnfxJ-tYSBmwy9bX_3HjRxqGEVicYFMF19sKuhnuztQOBxqu-WjSgnW6WwFvrwjXMzqM8pzMU-dJhFCc815sEMG3xzQl4VBwFu2OE0eMFfPGdv_fmlgsMdQSzpzC6pfa-OxCxt-MWCnGwRRjbOmX9WeKQDlUIJ3aCKGXuRK-Mi1AbPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd57389c4d.mp4?token=SWTITfuiWNvz1jkRmBvbp4r1wAvGBJO0ehV7zDXzf9cx1MUVNluU5ISsymyYRSPMNbtobvve3xHsBKyPE9liyNY4K9livFOGC2-8MKmUzAhmibw4TA8RP8vn0tqLaix6akNMvi8u4KwRfUb8iGcrJNhP1dxtIKhqqXWOrpULnfxJ-tYSBmwy9bX_3HjRxqGEVicYFMF19sKuhnuztQOBxqu-WjSgnW6WwFvrwjXMzqM8pzMU-dJhFCc815sEMG3xzQl4VBwFu2OE0eMFfPGdv_fmlgsMdQSzpzC6pfa-OxCxt-MWCnGwRRjbOmX9WeKQDlUIJ3aCKGXuRK-Mi1AbPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار رییس اتحادیه نمایشگاه‌داران و فروشندگان خودرو: مراقب کلاهبرداران باشید و پول را فقط به حساب شرکت‌ها واریز کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662547" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رؤیابافی رادیو ارتش اسرائیل: تا نابودی کامل حزب‌الله در لبنان می‌مانیم
🔹
در حالیکه طبق تعهد آمریکا در تفاهمنامه، جنگ در تمامی جبهه‌ها می‌بایست پایان یابد، رادیو ارتش اشغالگر بار دیگر بر ادامه حضور در جنوب لبنان تأکید کرد.
🔹
به ادعای این رسانه، ارتش صهیونیستی تا منطقه الشقیف، در خاک لبنان باقی خواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/662546" target="_blank">📅 11:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNUH8yboXBmP5ZSAzAc0kqrDcmII6M99L4jO5rLKOsApJpxP7f6Edu0dnnPEkg0ZC10Q3fa7F6ZoKDJR0CLCEFRhD931UI2bIDFajI_1LUZTtNrnJYnRm9-ZIfLXI3VwVBon3XfYE_w_nasZ1qVvVfaGf59o9Ogo19m4b4TdRf79pTtIFAb3-tocnGSP54KzoE_fdypmwiml5RZd9p4J__ncX44Rl3xIzPuiwys2kq_p4Nhyr2EJiXbJQmO-E5ycbFhz6I9b-ti8MnDTBwUd803d__s-bslWicOArTBiDWMFDaSujyGM-RhPUZxDt1k5u0MHyZBYGXpV-YGYZe4rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امن‌ترین کشورهای جهان در سال ۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/662545" target="_blank">📅 10:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662544">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروایت فتح</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b93cb9ff5.mp4?token=jvqL9IdapR3Al7P7POn6PgpHmVOl3GvziSDqIKrsbWznWCFxSZtcqTQSUFm1-KR43MAyz892uGbrkBdi-OSI-uKicyXnGG8sEWxjUiP5aG8Rh667f1AXGWkxh_LoQhc7ue5Y3WThy_z3tX3lQcni1sXmBfW33jbSOd8ccRluIkKRXp1l7L5Oe9J-pCbcxPNChMXINoRr6vus8ADBZvfXf-47EajHeX6R3VHD47F7_wsi8MbsDGN4la7jQdkqNxnwSHvIrYOwW1IvH8SH5izZ8N2GeQ49TYhKPe7bE_9OoUHUJhbDsNdQLQbE3LhAh3qpPqAxZXQNfFmb6zhlA_xouYepZ92dB46JhJ0UkE0j9bUAlssLjXTu0J3APx66OIp9mPRTH89QlSo01AFgqxMaXr6vhyYIod50nwnIHRYY31h7schNrAhSk-1tNIhUcNh_6R5B9fFd4-SAn9Cyh9e1bkeLi1FtfezalIQ1Cgbstnn_HqZzXSNpb-LtQekfGf6vhXzFxl1R2rKROlFvP4T192dHKrMgbPHb8OGKf2JPFlU8HsdwT_JNtYEvMyqs1Kaj8F460Hy2xqGdJUd-KP4L-yJnYG3bqBT9WwT600Vr0crJms9ywsUXWmw6vyJQp2dGlwYauv8Xllys1_uCnOkKGZfbhuOM0ZZe3hnonDHQ7do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b93cb9ff5.mp4?token=jvqL9IdapR3Al7P7POn6PgpHmVOl3GvziSDqIKrsbWznWCFxSZtcqTQSUFm1-KR43MAyz892uGbrkBdi-OSI-uKicyXnGG8sEWxjUiP5aG8Rh667f1AXGWkxh_LoQhc7ue5Y3WThy_z3tX3lQcni1sXmBfW33jbSOd8ccRluIkKRXp1l7L5Oe9J-pCbcxPNChMXINoRr6vus8ADBZvfXf-47EajHeX6R3VHD47F7_wsi8MbsDGN4la7jQdkqNxnwSHvIrYOwW1IvH8SH5izZ8N2GeQ49TYhKPe7bE_9OoUHUJhbDsNdQLQbE3LhAh3qpPqAxZXQNfFmb6zhlA_xouYepZ92dB46JhJ0UkE0j9bUAlssLjXTu0J3APx66OIp9mPRTH89QlSo01AFgqxMaXr6vhyYIod50nwnIHRYY31h7schNrAhSk-1tNIhUcNh_6R5B9fFd4-SAn9Cyh9e1bkeLi1FtfezalIQ1Cgbstnn_HqZzXSNpb-LtQekfGf6vhXzFxl1R2rKROlFvP4T192dHKrMgbPHb8OGKf2JPFlU8HsdwT_JNtYEvMyqs1Kaj8F460Hy2xqGdJUd-KP4L-yJnYG3bqBT9WwT600Vr0crJms9ywsUXWmw6vyJQp2dGlwYauv8Xllys1_uCnOkKGZfbhuOM0ZZe3hnonDHQ7do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آب ندارند، اما دست از کمک به دیگران نکشیده‌اند
روستای کنارجوی سیریک؛ جایی که مردمش با وجود محرومیت‌ها و کمبودها، از روزهای اول جنگ پای کار بودند.
#روایت_فتح
@revayatefath3</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/662544" target="_blank">📅 10:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662543">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889d4f5a02.mp4?token=ihH4miD11UCPQiN9ymUga9edm2a3bii9h_BcTEvcTHkjHDmv9Tr11f9QrEDxj9wQU7nUyWBg8Wrhk8tzLYGwEGF10F2lqoMb3jos64P0k3wEy3RVCFbla5IzDtGhkMdGp8FPNPqkpk238x5oHYMaVwBGLbcPdMzsm5e0vwWY0VuO6U3tD1ikxbkJ-NwcoBknPCOCXaSr6CjwyHXyYGwubanUkO3_AvBh0R-Lt1ZdF6poMa6ujAg5NUTFVoXkzvVvh4reOFmqTxCmF_eo4uvzGsY5qpbrb6J3qgjhUCi1UhkGNeF0y_bI8PUWsQ1TiX2WsT_HbmJrD3Qzm6j606QAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889d4f5a02.mp4?token=ihH4miD11UCPQiN9ymUga9edm2a3bii9h_BcTEvcTHkjHDmv9Tr11f9QrEDxj9wQU7nUyWBg8Wrhk8tzLYGwEGF10F2lqoMb3jos64P0k3wEy3RVCFbla5IzDtGhkMdGp8FPNPqkpk238x5oHYMaVwBGLbcPdMzsm5e0vwWY0VuO6U3tD1ikxbkJ-NwcoBknPCOCXaSr6CjwyHXyYGwubanUkO3_AvBh0R-Lt1ZdF6poMa6ujAg5NUTFVoXkzvVvh4reOFmqTxCmF_eo4uvzGsY5qpbrb6J3qgjhUCi1UhkGNeF0y_bI8PUWsQ1TiX2WsT_HbmJrD3Qzm6j606QAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو خودروی لکوس ‌ال‌ایکس ۵٧٠ با یک پلاک!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662543" target="_blank">📅 10:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662542">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
بنای دولت پیگیری حقوق ملت ایران و تقویت صلح و امنیت منطقه‌ای است
پزشکیان:
🔹
سفر به پاکستان با هدف قدردانی از تلاش‌هایی انجام می‌شود که دولت این کشور برای نهایی شدن تفاهم‌نامه انجام داده است.
🔹
ما به دنبال اجرای کامل بندهایی هستیم که در چارچوب قوانین بین‌المللی و حقوق ملت ایران به امضا رسیده و در صورت تحقق این مهم، بسیاری از مشکلات منطقه کاهش یافته و دست متجاوزان و تجاوزکاران کوتاه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662542" target="_blank">📅 10:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662541">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان راهی پاکستان شد.
🔹
دانیال نوریان از پرسنل مرزبانی شهرستان مریوان در حین ماموریت به درجه رفیع شهادت نائل آمد.
🔹
سازمان ملل: برای نخستین بار از مارس هیچ حمله هوایی در لبنان ثبت نشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662541" target="_blank">📅 10:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662540">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfFIRcuB3qmVZ1u8wHNBaCZ2wLCvyWMgtU3qAXlIUAsTF_EMOoorWPfPKbVafUJhVv2grL6Dx3prseb4dI3Vy-hqumzaXXZj5KtEe3-2Du5zGnLyfvVnENkc7wDKN5j2JGn-CPhuFUU2vCu2pSFNdBHtEelXit40tQsyExhRRL7im89mFALw1eLt2KDprwwmaZyb4JGBHVcZXxwuWAl1hyiab8C3rPEPkm1AjfidQrZfbkrGnB1IBzfHdxQSwhIgHRkPfVzpoz86Xwt00Ze1n1hdwYifL-Inlrn6goPfb6dzMNo22GqlgSs_bMugMtyGZG_HkT7odGyDxGYP05W9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ نکته عجیب درباره ارث که همه باید بدانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/662540" target="_blank">📅 10:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662535">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rW9LnK5YTcZQhIM67gWbMufNRqBlFyu7PB0P3ymUG6uswoUo3X6jD46xncTt9yaq6078a4WwWcab709NxvrjI69QSmqNz7raY95XyRPuGdZq42357eWlnpHyNz5rHEov6CL0a6QzdbnoOyF_6N2eUPdouCXeCkoXXhnzZJ5KfZHnSrPXhyhvm_zbP72yzRU4QpqAanUb7R0o5WgRQMBFqmSAZuFa_z8kP568ZoemnIBRC0t1_hj_BLUaVlBR5OEmfWrqli881zdsT9EM5J_-p810c4us0Giedy9pda-4V8A8suLl2mfpGy7MwYnyl-yHlj-jxJQIerQEGnm7nWKPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJGPj7pkczBBanFx9xU5BcndyFf8OufQ_058cOnE2MMvHWzxUBFAN788cBPAHRfBKdisBGaIH3GiJvLNZNfyDbV7wJYDpH22EqQSi9tJtvG75S_Vh2bc1FoB0ATqytOpoKzYL2HZFhJLs9uxwQq6pcQ5fSZgzRcJhqPa1Z0DUMaE_25WZwcIrQwDMnCBM6tHST64KxbbkpZ9XmVOoxpWRsue5QhIvkNylnf7fqO3xHDh8FqAyS4IP1jmlbXaTFm9bAGYOojmCwG9lnY-7LnbKZhtX-qc_oghoD_h8z1d4aTVUeuJGHUR25KxWqXYYjLm6NJ6OvxvUnqEGe62pryGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pp8FG3tlhE251Ds9KPKbwEIwGMKngbbR4_jiq_49B38SB4MpMk8N7aroGNuoHQem4Gqf3HOiwhKA9YNhW176T_9Pe5dQvEQ6MBTpXpyzn1Lw_PncMjOEnrBTcq0bhLIxfak9vQg1X3fpNKXeIePgVHl8sLLyFDgxna3bDc-fMioxA3QszeaVHGeGZjVkWolwS-z1N7QCtpDBFfscbcAfXpyfKQc3sLVpGcHlg9BrjWuK96_RxDNbddpmQFfgSNWo4RmVUdKRwB1gd9m-SKr6WnnF1AHGNXJqxowWSC8YU20To4ktRJ1VKbGajCPt3JF21xHg-4clzRzKCbOsXqt23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VT6ydpfFx9sirotNS4tuGBiaTxgU-sYJbbZtaT3eEUQEyQnqD3JxBy41d0TOc8Cli-y20MURKQ14BrDWtotqnhgTLL-gWBjE8yMxbWAks09qqCPAkWjWPEdc_u-6uS-0mZMYV3FYsUKoYwwaBNecHX84YfcxdtAqcqFb3sKNhKRRafOzAzms83F_5ijGLvCl4OHR6fqRBv8hAsY9rQSHz3eZBps4CTnfCcxhazhDzgw6eLSZlpvJSKIUfO7Wz1dw2Uv4WWOvA9DcurB3yJdQQwzkq_FdmHjjFHLPXVZmnsCED2U7xsPH0YL7Ll-fR0T8jFNQydJpgo3_dsvyR1eJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lX-A4JYi_lU7CdJdRfNswMZixbHz6QvxVKxqB8D2nYoAVFIv4a4HlTBQgJvOVSt2kHhrABQm5pEufE30V8qh3fGLJ4h_w-763KbdSftY1t7tPzCt9LWDlgfnEdd2jy98aieJw6mQ5m0mrTheHcI3VEgVP26QYSwgox3IoHJBVQTzskrmPHPDzSppl6mrpBPan_Fz8X5TiAmGF1fAAcQr7M68QIbuTVdnn7eTzrP1rcbNcCdW7ANeEG4Ym-lUGApsMzykdLVpPM-mNNUsKPhgraqR53dzkKc80jyXB9Kczw7J5TKq_GPAtw2NqT8GLj2Qr0aei6MPYUvzXJ-ZrlDwFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ازسرگیری واردات خودرو از عمان - جزیره قشم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662535" target="_blank">📅 10:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY17U3i53UQBXLnnCO2GD7xmSW7CE8K-CnM3qCTAkRdKZV4yXoUdg5TUgQmYMiFId7kgZE2-_cByrqMCW_zgEWMpnMRYoq9K0gc5JUvhufJg6YwrsdtHfrx3CwTOFgO07tKl1mNA8GXnSCc4HKBU_qjF7GGYNNqMRysorWCNbPoMpQWZvVxiSTJgWod6Iuo18EJCgxV8kWxarTUf6YNe4tUdgeEHM91T_AD07nGzdLhVvX9hc3vmss4ELe6ELiH5_VCEm76ACm52XhS_GJboUgDrYYQ-hh1XMuSSGe5pfZvqTNwl-cnkp5hV31NE5jpEFpv4dqUTZ94SgjqeYQRNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbgIOooX1o7QK1vb_GFY9p5iZmUdmCdpFNIo2IhXh99Kfob_EwKHs1Zrm-DK_d5s2SPW4OEhSSg8rK-UcQ_ytYe4EQ0bn0i-QNfXpq43YDfo2MO7gxXM9LVdS_hYaI30Pz-ikTFlyn2goG3LQ2ZKo2n_r8bw3L2WcNcVO4JM0VyxSCEg13bb1YgfgLgvVBea6LwRxEusgKYYu3fw4iifh48nkZPD3UaQ13qrwcWlfeQ23DeL_QTeH08BSbDKTUQ9sFm_bZLVvWbaBm4cePJi6UcxLYSnARRHhY7RnGetfMLV5PV7Ersu3Ii7E4VSh9urtDdNFOAmypOEn-XFnpqq2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اطلاعیهٔ جدید آموزش‌وپرورش: برنامهٔ برگزاری امتحانات نهایی بدون هیچ‌گونه تغییر اجرا می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/662532" target="_blank">📅 10:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
الجزیره: بند مربوط به لبنان در تفاهمات جدید ایران و آمریکا باعث نگرانی اسرائیل شده و گفته می‌شود نتانیاهو را سردرگم کرده است
🔹
مقامات رژیم صهیونیستی با وجود این نگرانی‌ها تأکید کردند که حضور نظامی خود را در جنوب لبنان حفظ خواهند کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662531" target="_blank">📅 10:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662529">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQnVFfRJpaAYmlDRqx6nEeuSUbOAjzc19fzJ2hdAa4jR54jwcW-EjJBgp2n6WYovWrLEaXRwB8WCRkWzXOaebiXuJ_lVIPEd0PNsns2G_6M0nFj_-lkhQHWhTb57pHOS_Xgxeq4CJhDO63GLKMhSvq-OfGLPi0hoBXUPBGrcI6gXz2ndml0lMxbxpIH3TQ17ICAPkbJFvF9S4ty5MwiiTXq131-6mbkcbZJrhzPO4lq3McL0HPOLtQgI3-aEQpQV816MMKqlNFtJ48vbz5h2XLC9Ipr52wrJ7fE0IJhuyZORkXB4EF-njfIPCx3smvixk9dbUTRpv__P8jgu7PHVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
دکتر فتحعلی در مراسم روز ملی اصناف مطرح کرد:
🔰
بانک مهر ایران در مسیر تبدیل شدن به بانک عامل اصناف کشور
🔸
با حضور دکتر «مسعود پزشکیان» رئیس‌جمهور، دکتر «سید محمد اتابک» وزیر صنعت، معدن و تجارت، دکتر «امین‌حسین رحیمی» وزیر دادگستری، رئیس اتاق اصناف ایران، رئیس اتاق بازرگانی، جمعی از نمایندگان مجلس و مدیران دولتی و دکتر «غلامرضا فتحعلی» مدیرعامل بانک قرض‌الحسنه مهر ایران، آیین گرامیداشت روز ملی اصناف در سالن اجلاس سران برگزار شد.
🔸
مدیرعامل بانک قرض‌الحسنه مهر ایران در این مراسم، گفت: این بانک با خدمات خود در تلاش است به بانک عامل اصناف کشور تبدیل شود.
🔸
فتحعلی با بیان اینکه پایین بودن نرخ تمام شده پول مهم‌ترین مزیت بانک است، گفت: در حال حاضر بیش از یک میلیون و ۳۰۰ هزار صنف، مشتری بانک هستند؛ همچنین یک میلیون دستگاه کارتخوان بانک در این حوزه فعال است.
🔸
وی افزود: بانک مهر ایران علاوه بر خدمات بانکی، در حوزه پرداخت‌های ارزی، صدور ضمانت‌نامه، صدور کارت رفاهی متصل به اوراق گام و همچنین فروش کالا و خدمت در بازارگاه کیومارت می‌تواند در کنار اصناف سراسر کشور باشد.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662529" target="_blank">📅 10:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb45e6f68.mp4?token=a72RS8Muao4XBkt8VWVY18nuuivErGmPJEa5ujrtmH5bEXg8UsKdyWMm3ONe36OWSVwkd8mt23yTxZ7OfX6ZL3q3PI8QCB77xHlT2zPzAKWB_VwQpXAwk-9Alxc1-IJR_uEc4KpQaT0NynzMhGruvRuX7jUzgyJ_doI-Tq0JaWqwEzojsnXewHl1-jOWAQsDCTxSypkxw2sEcJtnaNxNuxVyGxnx9g0Zx-kyZaQ7-lxragb8JR-jDG_0cL8-vQ0emyHvwbm2uFcbQrCkXGmFS5YQYL4VkD-9IN7UOEY-peR9ubn3r5vmlBz_Etpwpy7R59npYmh5nOXFAVH2oztegw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb45e6f68.mp4?token=a72RS8Muao4XBkt8VWVY18nuuivErGmPJEa5ujrtmH5bEXg8UsKdyWMm3ONe36OWSVwkd8mt23yTxZ7OfX6ZL3q3PI8QCB77xHlT2zPzAKWB_VwQpXAwk-9Alxc1-IJR_uEc4KpQaT0NynzMhGruvRuX7jUzgyJ_doI-Tq0JaWqwEzojsnXewHl1-jOWAQsDCTxSypkxw2sEcJtnaNxNuxVyGxnx9g0Zx-kyZaQ7-lxragb8JR-jDG_0cL8-vQ0emyHvwbm2uFcbQrCkXGmFS5YQYL4VkD-9IN7UOEY-peR9ubn3r5vmlBz_Etpwpy7R59npYmh5nOXFAVH2oztegw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض کمدین آمریکایی به ویزای یک روزه بازیکنان ایران: این چه وضع برگزاری جام جهانی در آمریکا است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/662528" target="_blank">📅 10:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662526">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7795093980.mp4?token=A2iBmGZQDFpiU1TzF_vsw6TLfQTCj9iPAGnTY4Xjh5ANNqiKgVQPtgiiAbDEDPZUGtqK9Ud6pnX5bGMlsGWmPbH-rhc13tkBm7-0e8aPpYRuW4rHYY6BC-IKWgOZAcS-K3rkHxv-EdkyK5rJrx23rFN27l_N4lk76-51qXoQ6mTj9OzvKDxZ93AeivDpJ9_7hCbQKXkoLucpQIDcmN1kpuiX7uXELMpm6X70DTGCxGT9VzvcViJhW7EGMA3PRAUcY7War-BNMzkUsTySl5F_6HsULOFWOT_oQFhh3kSDeUr0Ycz8uRKDk-KOcz2JK_CRNp8XbhhaRpWiyho_efeKjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7795093980.mp4?token=A2iBmGZQDFpiU1TzF_vsw6TLfQTCj9iPAGnTY4Xjh5ANNqiKgVQPtgiiAbDEDPZUGtqK9Ud6pnX5bGMlsGWmPbH-rhc13tkBm7-0e8aPpYRuW4rHYY6BC-IKWgOZAcS-K3rkHxv-EdkyK5rJrx23rFN27l_N4lk76-51qXoQ6mTj9OzvKDxZ93AeivDpJ9_7hCbQKXkoLucpQIDcmN1kpuiX7uXELMpm6X70DTGCxGT9VzvcViJhW7EGMA3PRAUcY7War-BNMzkUsTySl5F_6HsULOFWOT_oQFhh3kSDeUr0Ycz8uRKDk-KOcz2JK_CRNp8XbhhaRpWiyho_efeKjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام عجیب راننده پراید برای فروش ماشین که باعث چپ شدن ماشین شد !
🔹
راننده قصد داشت برای معرفی ماشین، یه دستی بکشه و از خودرو پیاده بشه تا فیلم جذاب‌تری برای آگهی فروش بگیره؛ اما این حرکت نمایشی آن‌طور که انتظار داشت پیش نرفت و در نهایت خودرو چپ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/662526" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662523">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4p6UIkhcqfohnwo65NPK_QcXGfoU_XStoWCudRRWbxGfTbp2ZqaTg-KDGFHSPs2RtkPac5sGecYsLpxsOpShho_A4ktozJ5KZxwoeh-8nJpEZ4cIZIC_b5QZdbJmV8bQxITwTLHRo-Ui5KGd3I3hsEyOr5hQhe_KhsOHuOS7IHy9R4JOBplCQ7RysKLAIwWApTdCpZFuAubvOZGE2jmy4AoPEM27t2_ErFWTS8YKhNArDXAuy9llsGyLEFfTQt1F4maxuvBSRp-RUUzx2wsDVUHz2GutU5QaDwTVtdICbiHNvOZJveRN5XALVr6Uc51y5uvQlPmjkVbxxba7BHA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت یک کاربر بلژیکی: ما نتوانستیم ایران را شکست دهیم اما حداقل ۳٠٠ میلیارد دلار هزینه نکردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/662523" target="_blank">📅 10:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662512">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0R6WAMKUV-a1Hkd6He_5P6lf4quEF8Rzccxc20iTCWPZFeXr6B3qpjqj_diyLNgdDt6z4P3eVUh7fTjCbCcZJ4E_bcrmhjprQK_emO5LV45QpqEBMv5puOgPpLr_3xQ2RUeO1d-D8Pmg0KTdpuKjRcVs_9xEOKA5YpNftPtKk86872u_zC5HZ4XYCEg2cM7yeebG6U_VY1xgcNcMgyw-XfElhvYAlLmhYbYF8w43q_ZCWhUFcJvJA_MIfXarWiMr_N54KNrztEEoql4myW3TaOTJOHA_6J_ba5daHCRgtWbYgD77wwMw_JGyq65W5jv-wuwjd1qpvpQtwuCGIBvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lyZKvsN_9REeEodfWNwltz9nFz3C6PW76kXm0JeDAAewZ7eosXDKRG3j1IJlk972gK9jCBJhoOw5m36wn2AlPcI2ELUfeYXXH-di43MyTzQZ3ZnxvuJ1QRyesOgNCVtQP_bosKFW2Olag_MjZ1vl8HHmI_JvzW9EajrWW8GaKnXQuJuij45xRe-GWYETiWAjb8-X-PIlUSLucxQQrHXj_dah_AwE7EPg3FwNnsK4gyQUOmkZ3QWB5kabPN2qzsKrFWfQxixWbmYffLMLnddQauGd2M0JCnIC0byX8QzGX9YY1cuF6EBQ7M7rwo-0Ro_Ow7ZLuft91dt_kRCv-svdoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj2r3crgQx8tL6HldWcEthR13RGSps62WOYF31F88OanrMGI-SVWVj1StamuLInAKtYl-RYThruEpreLfi5x-WrGJT4Tz-OiX7rtw9iJ2Yr2gfdVRwcFZqcqGUwO0m7nHXgSLAlrNyM2pafDsbwSqhxdAbmafvH8Pws4fuUpTYjFjHlCNQEiLIlmosGsmxSmId9vowDrussKiBdrCXOMXv1kv3ADisomU1smg7cGJEMm4acze4p_fSIC1w63ppwY_mxssOzSL11AaJOQPBJ_lSGVzq5jkK6kxrFgcN44qAzfX4olcRQc_J6Ew9r8r45BDnXPCRFrFQtSUCp8ekJ1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK4uRJsMUc6SgECySv8QBBi7UaUhjhqFBuuI6H-a3EobVM8NPlTdqwohwu8-lbJJJHdACaAlnjpCf8UD0rLAW4esFWdS-bN6DE1AbUZ8f-A7MeuQ9jzlVNPl0tEXEWTbydWVjOxYqvHGkt4y5CKHLvfBCGMcDyALAMJ9jflztJRpIYVJxv38P-YGLrGMmkLCiYhau2A4UtPUIceA8G8H9n2wPZa_BdmZaFMn4aTQPvr6kROc9faE_bFwCCPh-tg7UNEmQi-Zd0yTWOqVFW9LAepKyzrtNzcwzDuIAyocZb8D8w0aUqu_FB1TjAhWycRNc8mL38GpE79XwgC9W2ORrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4tj-JuGjgQ_3VmIXourwfAspncqdo31_knMkdtc9p9nGhLqqymUvQA8fx4B77Szh6pI9xl_RB9P2iarmSMiy3AJ5fyhuJnHBsoBb8RZ3CYLGpLgiBIiu31OEjuicwWNaugHePpXIhQrFccjVeZPm7YWFwHpm-Pf7wRRbDd4DAScr5qewm-_pGlYQM-pY3-U2ezVlO3jQJ4wsvtRO8VhjjwRKGFwWGWnEPlSSePWGrQto0l5qNWjFx1_fMOxmAyNbXK9MLap3Fc_xSnKID1QGJQ7XV9gnNF8CCScR9IvGUui1lgArsHi02BSFF-4MOf9VGYWAXgYGf-EStp9QILQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKhUqyobHpnRKPuNFYXv1sn9ElcT2e-xAlsRNIwmAQ-aPsVB1e4kiSz2lSdE5l3fJ24r5iq_eJ-HjSUEKu1WhgDbHWyJVpBajlSg-7WDqzxhjMfw8TS52bkPMR9UjGiHZ-ZMZA-D-11h7jdIR4PNvZCHfa--8yQXxkwh6EtkYkJo08tGbTqlcJh8ULo-L6F3pb0rJSiQFieERtlvPXON0xK-vbRRrtTLF_bc7pU34Mta9oUBMW5l1E4dbiUcz5MGjSvxjBQAYA83ABHzxQUHcGVqRl7--xHrFIw5vKQ766RasPIEk8_Vubn9wEQiV7LsikLTUIqlWome3MSyA5huAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvjB4jJkdEZX8Mzi7fuBsGT91n-BlOZMUgSvRdV15qe0YPrBZYoWrPCcUIuLDYy84hKwRF_iLhRQVF9cICPQ9HUsCHLNZaLRV0X9tIZcs0fCPAE3_dwR6w9OlkmSZdqaBG9jGfXpeQZ4k6PEfjSNnpYANdAmTTeIg-3di1x2Aieoc6rLTGzs5s3oikitk1w8UvdUdw3GB5mXLfEZ2kvuE2IZgI3uuPgXqLuNf828CnS0zEm5ww_aCAVofS-TmtKq1wBCWLHIIvO31rDP_gyXLaEYt_hzRo4ZkzH0bv4LLji-PMGzBr_uswmMQPH229bi2plzPq-kUheLTamUqF1M4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRxlY6nbaY79HIx-FGGWM1HapFwIveCzaJzb1LCeS8svI9xrwdGRfPSVd7QnOBST0WFtZw4DBWM89ERloFt3kBOBCsUbAZkyVrZOCTsEyPJxfFcF-8WoxCOmd7_JPhPDZegRdQnrKliTupz3X24xSIYIv5oBaMMsPps748Nn7kuYRhUiRLeV28gMXuayesTsqbam1ngaumwCiA-v2fhIMACFm82XXopoUKGmhrlAfUXPAwItr78OkJxpqx2dZ4At1zQaXdwgut5DDS5YFtott6Y1vdp-MBrUImCAOix2mgNA1zb8gZsF3AUizOxbLQjmm37C7sI1hdICt-7ZaY9Uuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8LKiSgA5Qm9emS_n4BsyBnTvOC6AQsHpzRZcktcmcw1RKxnLpfOYaJqcL03TuBI7i7XhPKKZx4sKVTsWhTa_XLvrGt4Z683fin9dFaXVe0G9YIlNyuYLNrcvfxAjDuinuHZDcm2WREB7wkQBNmB7_hs1wnsg0qTz1riVnUOOSMCJzr378KTZes1DjffXET9N-OM1FmLEKQG5E8d2dFJR0qUzBkvVlD1zJtNaHMTn1S7DlpibmF_BN944A7HOIwx81-NbjjYlrM2aK0A8HTQtv_6LXyeAIBfKwQs0bZ9VsaRNIZhltAROn5d9_GP2htoFH5bRZ3XpxAwLnztdhrsBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ نشانه که میگه سلامت‌ روان شما در حال فرسوده شدنه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/662512" target="_blank">📅 10:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش: امتحانات نهایی پایه یازدهم از ۲۰ تیر ۱۴۰۵ و پایه دوازدهم از ۲۱ تیر ۱۴۰۵ طبق برنامه اعلام‌شده برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/662511" target="_blank">📅 09:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662510">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3727fe8.mp4?token=idLJ1JNn1h8eJQkKj25o22weD5oOKZIah5HFrVCrbOPCesYbZHkXR6LdtM2KH725-oBoEx1d4T-sRBGdVX6usknyeDVfpuLYqciu1MQ98pH0PU2Du28lVDoCoSodciqhqxxJkiTRsdNlG9_uMTYy0G-gc1s37fQe2aJi9iyMBLkpXL-VFuVXSFBnzm6LwIOPTUVWMnu4rzz586ptNH29weV0E3JqF0Z52y2nZOtKje82Mbwq-j5BeUWY7RN2LXwhavyF8du6W5e8XnaqDkaMhvE32YdODROAEIgRi-Tp0vNCGXdqnvD5TxzquYoLJUsAUOt-OMoAJ50BcZhgZ45Csg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3727fe8.mp4?token=idLJ1JNn1h8eJQkKj25o22weD5oOKZIah5HFrVCrbOPCesYbZHkXR6LdtM2KH725-oBoEx1d4T-sRBGdVX6usknyeDVfpuLYqciu1MQ98pH0PU2Du28lVDoCoSodciqhqxxJkiTRsdNlG9_uMTYy0G-gc1s37fQe2aJi9iyMBLkpXL-VFuVXSFBnzm6LwIOPTUVWMnu4rzz586ptNH29weV0E3JqF0Z52y2nZOtKje82Mbwq-j5BeUWY7RN2LXwhavyF8du6W5e8XnaqDkaMhvE32YdODROAEIgRi-Tp0vNCGXdqnvD5TxzquYoLJUsAUOt-OMoAJ50BcZhgZ45Csg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی منتشرشده توسط ناسا پرواز کاوشگر این آژانس فضایی را در کنار قمر سیاره نپتون به نمایش می‌گذارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662510" target="_blank">📅 09:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662506">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjQs48vkfRMjieU115NVwE_VrC7TOam8bHQ4j96aZEa0Viq9IATn0B9F__I9mXtH8VxaDJzPd4FoRqTCFObBtBsL6rR5VOhXeixIHGO5b7e0yoWTYz9MGfn-_skituT-ASRyzQTzLxdCvHgOvADkEZ9kT_Gh2UnwmGFpG0MtZgfBZRsKXerWctGPJwJ15zAn63nX9hcs7I29MVWBFonc8_H8tKFHNkQVz-VXn3XDnWPtVa2MKvwQHortnvZzTTKct4Az_4kzkAm8wXyUAI5qLVFt2JXOKqz-sU05Nca3xPDu74ZyLToDOkOWIPN7dya92uRY_HlzNH3aof_W_VjDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ اعلام کرد خودروسازان آمریکایی کارخانه‌های خود را برای تولید سلاح‌هایی مثل پاتریوت و تاماهاک تغییر کاربری می‌دهند
🔹
این تصمیم در پی گزارش‌هایی گرفته شده که می‌گوید درگیری با ایران، حدود نیمی از ذخایر پاتریوت و ۳۰٪ تاماهاک آمریکا را تمام کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662506" target="_blank">📅 09:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662505">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دوم،قسمت چهارم</div>
  <div class="tg-doc-extra">بزرگمهر بختگان</div>
</div>
<a href="https://t.me/akhbarefori/662505" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
♦️
کریم‌خان زند (وکیلِ مردم)
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «برندینگ معکوس»، «مدیریتِ ریسکِ آینده» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/662505" target="_blank">📅 09:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662504">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194817b2c6.mp4?token=ErrVCnxLGvUlo62Huk1bDZdzZW0RVIGUNXFsKptr_UpJoqimHRYZwqhTrT15I_pWIXie1Fy3ksds4aFIwopU-DCGx-x0sWzLjgHXICvgRGrm3Wp19OdZ1XN7QUbEKkvcxrYdK6e7tSL5w6NugbofMFDru3cfpmsjkWuDVXtFCeC6_cSXNPduTaLuIDAQQeBD03Am5DEnGFYOGbiLqbW4pTcfj9tTKm4HwTBU4Fgnnf75Jj42JNSNlnYojQWXs2ggwJmQjy-5DRXnOf73H-JsU2CY9udT0fe5hGvqftPO6gL0Mn9u-v2nCXLeZ1SAYmwINe9fBZYkNVFOPBJjbQPR3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194817b2c6.mp4?token=ErrVCnxLGvUlo62Huk1bDZdzZW0RVIGUNXFsKptr_UpJoqimHRYZwqhTrT15I_pWIXie1Fy3ksds4aFIwopU-DCGx-x0sWzLjgHXICvgRGrm3Wp19OdZ1XN7QUbEKkvcxrYdK6e7tSL5w6NugbofMFDru3cfpmsjkWuDVXtFCeC6_cSXNPduTaLuIDAQQeBD03Am5DEnGFYOGbiLqbW4pTcfj9tTKm4HwTBU4Fgnnf75Jj42JNSNlnYojQWXs2ggwJmQjy-5DRXnOf73H-JsU2CY9udT0fe5hGvqftPO6gL0Mn9u-v2nCXLeZ1SAYmwINe9fBZYkNVFOPBJjbQPR3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریم‌خان زند و برندسازیِ معکوس
#پادکست_کافئین
| فصل‌دو،قسمت‌چهار
☕️
🔹
رهبری که در عصرِ اشباعِ ادعاها و دیکتاتورهایِ خون‌ریز، تاجِ شاهی را کنار گذاشت، روی فرشِ کهنه نشست و نامِ خودش را گذاشت «وکیلِ مردم».
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
🔹
از اینجا ببینید و بشنوید
👇
https://youtu.be/8Hfg6_MHS8Q?si=ZwwAKvamjOCObRCN
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/662504" target="_blank">📅 09:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662499">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
روزنامه معاریو: ترکیه با برخورداری از دومین ارتش بزرگ ناتو و خودکفایی ۸۰ درصدی در صنایع دفاعی، تهدیدی بزرگ‌تر از ایران برای اسرائیل محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662499" target="_blank">📅 09:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1f0a815b.mp4?token=D-rpk4C3mZFtuP5uGy0aazt7dZCjobSigYkYWXGXHOB_hFboVd5tTINRoHRDXI7Zez8OJyXBH_J6HEz6W9qT2P4z6x4cTO9BMd43wAAuY1-XKZdqVOGP3rhsWeTRX8Ybs8i___Q7qILP1HTaFSF10B-P_Q-0-4Hiwsjnn8ZnRU-x7npLjOs8B7VIwaTq1Wrq_jkJCqOgZrhIoaQdJP29cxNTdo4bf67CuN72OXWiUmJaw7ca-JDAZxO4ZJjtRS7dCVVH5-JZmI0tMlJuOAdKaPAnrS-WL5MXc2_NhspvI8dPnlTmX6Mq55Gi_osmO8uueJbC7RtmhOxJzdexEW_TBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1f0a815b.mp4?token=D-rpk4C3mZFtuP5uGy0aazt7dZCjobSigYkYWXGXHOB_hFboVd5tTINRoHRDXI7Zez8OJyXBH_J6HEz6W9qT2P4z6x4cTO9BMd43wAAuY1-XKZdqVOGP3rhsWeTRX8Ybs8i___Q7qILP1HTaFSF10B-P_Q-0-4Hiwsjnn8ZnRU-x7npLjOs8B7VIwaTq1Wrq_jkJCqOgZrhIoaQdJP29cxNTdo4bf67CuN72OXWiUmJaw7ca-JDAZxO4ZJjtRS7dCVVH5-JZmI0tMlJuOAdKaPAnrS-WL5MXc2_NhspvI8dPnlTmX6Mq55Gi_osmO8uueJbC7RtmhOxJzdexEW_TBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سریع‌ترین راه برای پر کردن گونی!
با یه کم خلاقیت میتونی به راه‌حل‌های جالبی برسی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662497" target="_blank">📅 09:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662495">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ثبت‌نام ایجاد و ترمیم سابقه تحصیلی آزمون‌های نهایی از امروز (۲ تیر) آغاز شد و به مدت ۶ روز ادامه دارد
🔹
متقاضیان می‌توانند برای ثبت‌نام به سامانه‌های
my.sanjesh.org
و
my.medu.ir
مراجعه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/662495" target="_blank">📅 09:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5630b934c.mp4?token=L1jjb3Ew6DQqapBwT4TnRGYKDzU1l1bhfF4ewDvfdz_VNMPffJAMu92KBbqtOi9l88Mum5UjhGAiNillWTB4dieWaAzE8Dbn7L2WbB_xpZa6Ny3EHDElWnYYnVHBW7iSK1wG0l4bZEsxJWmcaQuR8yTUTvmWiciWGDJJqAPj0BiwDQV0XPTpq5kAMqmgPi8HA8SMAipZ0DwSVFfsRmlOtFNm9DkHUGSE6pTOPrXNqFlXFxkRKN6QqSxBft0kMXKC-9Qa63vFyu7G1ZQB2HI-xnLN3csZbsxG0zz0fim0QK8Md-tWqXLOqjf8VyVGI4hHJk7B7CmG0BzhyQ8S6vTnGqDYas9ywHKZiXOk-fwoMRb8yU4yEX956PWX7VfKPM0OQft0jKnXZBdCRB9JLPij0Vey50FkiE5xfDO6V0uoUGAhDuuNjV5EBEbGmtEAk9sYZ0wwNf79baaX-iKw-Uzu3UyIFt44MaCJwg4Q4doyES2EgmDAy1mLJuIJ8m1gZt6_vw93Al9wV-G5xZZ2JSc-Tl8tuzXZ0TuBvEjpzwyHp16yCoY8SEcNSRBS2uhHSIIcMc8rnCqu7vMFG3TegmcZeLucg89CsRu2D37QNp_JpdxzKlpTY4SPeYwB93HQrpoiSz8GsZU3umx4-IIWVNg9eQkq-_UhjmSwh9wG1ZkwRIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5630b934c.mp4?token=L1jjb3Ew6DQqapBwT4TnRGYKDzU1l1bhfF4ewDvfdz_VNMPffJAMu92KBbqtOi9l88Mum5UjhGAiNillWTB4dieWaAzE8Dbn7L2WbB_xpZa6Ny3EHDElWnYYnVHBW7iSK1wG0l4bZEsxJWmcaQuR8yTUTvmWiciWGDJJqAPj0BiwDQV0XPTpq5kAMqmgPi8HA8SMAipZ0DwSVFfsRmlOtFNm9DkHUGSE6pTOPrXNqFlXFxkRKN6QqSxBft0kMXKC-9Qa63vFyu7G1ZQB2HI-xnLN3csZbsxG0zz0fim0QK8Md-tWqXLOqjf8VyVGI4hHJk7B7CmG0BzhyQ8S6vTnGqDYas9ywHKZiXOk-fwoMRb8yU4yEX956PWX7VfKPM0OQft0jKnXZBdCRB9JLPij0Vey50FkiE5xfDO6V0uoUGAhDuuNjV5EBEbGmtEAk9sYZ0wwNf79baaX-iKw-Uzu3UyIFt44MaCJwg4Q4doyES2EgmDAy1mLJuIJ8m1gZt6_vw93Al9wV-G5xZZ2JSc-Tl8tuzXZ0TuBvEjpzwyHp16yCoY8SEcNSRBS2uhHSIIcMc8rnCqu7vMFG3TegmcZeLucg89CsRu2D37QNp_JpdxzKlpTY4SPeYwB93HQrpoiSz8GsZU3umx4-IIWVNg9eQkq-_UhjmSwh9wG1ZkwRIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیبایی‌های بی‌پایان جام؛ شادی وایکینگی بازیکنان و هواداران نروژ پس از صعود
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662493" target="_blank">📅 08:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6fk_osMWkLlF4FbvaHkAVnv60NYm8w879V6AvX_Up6bfXLG3LLlQH2ed0_yX4GhW6UgPlmqMvPhJQDQJNCiB77YyTtUnNLp_C-MCVFWmT94CEesY3ZWKY0FKBAaKzhxUZ0ymx-aUURAULyLh1GM2GV-DSOsgfD-sVj3c2ohQ7bYAkMOShqp0a-P8kwgewBcDfbnY3gaQe-NnDY431Y43ss9Z1yYtPZol2PQZMBu-74CAih1RNj79KbSziyWamer6hxqul0yNtH5TXqdRL_F41-MYjhhuzqeAfELAlMEr3t5MjAzGi5Cw2QbIR0Dn45t9gwMWvLio7r7kjqzhiUvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسی به رکورد علی دایی هم رحم نکرد!
🔹
فوق‌ستاره آرژانتینی با ۲ گل مقابل اتریش، تعداد گل‌های ملی خود پس از ۳۰ سالگی را به ۶۴ رساند و از رکورد ۶۲ گل علی دایی عبور کرد.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/662492" target="_blank">📅 08:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662490">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4ZuGVLT8ph8VdIT4QFJtiJIyZdFJdRBInuoY87EAo98jgmZ61cDk0Py3L9jSlYVvMsHP35IBnmmf7r0nQ16xaR27AnpvSU5u1iXhMSKY4YIAbVRgyzeas5pADSKse0UZ9bGpTeimam_Kkhx303U-zE6yX8Tro9yWK1Inn48vYoFRkQYpHe7I-BC2akxhY8XpBWXLxFlqjJGmMzFPoAiRd89nafryT7vLFJ9h7Ze08p36miBe8ISmUBquf2wDyWb9QY4i-7ByqGELqM_30jykh-4-djNOaT0u84iA1zjCKnPt57tKsFyMRcpqphurp86sS07KZNkG85Tjex249SGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مجلس:  یکشنبه آتی، صحن مجلس، کار خود را آغاز می کند/ احتمالا با موضوع بررسی روند اجرای تفاهم نامه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/662490" target="_blank">📅 08:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc9bfa8f1.mp4?token=Vqo22u8YKXqTG4ita1giVdnGpsDS75S_5YcmMAwdeN4sJ6hvTwyqGoh4vsFi2zQiXTL_C2uMJQq6LUpE9emPMeAHg2KVZW-315Phdxq4ER7jBTSu84xszOMK4J-skKil4h832sBXud58sgByCXF4m2uyTJyBgddG2drP80wN2D9zKKEyp2-xW-B0dlB0tEYzZvpC9OvJ1Ss1AcWWVLNOLrblcAk2qasv46Xasqta2K_5_0SA3uOuZJqmJ18yeCKnepUEDkbfMjIA36J5Lz0m4Nkn5vW42IIpWRnAsEy1Ary_Bw4zkMXM-1YP4RdCiFfp_ZM_-TQLJ6edalLuGvDGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc9bfa8f1.mp4?token=Vqo22u8YKXqTG4ita1giVdnGpsDS75S_5YcmMAwdeN4sJ6hvTwyqGoh4vsFi2zQiXTL_C2uMJQq6LUpE9emPMeAHg2KVZW-315Phdxq4ER7jBTSu84xszOMK4J-skKil4h832sBXud58sgByCXF4m2uyTJyBgddG2drP80wN2D9zKKEyp2-xW-B0dlB0tEYzZvpC9OvJ1Ss1AcWWVLNOLrblcAk2qasv46Xasqta2K_5_0SA3uOuZJqmJ18yeCKnepUEDkbfMjIA36J5Lz0m4Nkn5vW42IIpWRnAsEy1Ary_Bw4zkMXM-1YP4RdCiFfp_ZM_-TQLJ6edalLuGvDGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتارهای شرم‌آور صهیونیست‌ها ادامه دارد
🔹
انتشار تصاویری از آزار و اذیت و رفتار زننده سربازان اسرائیلی با مسیحیان فلسطینی و جلوگیری از برگزاری مراسم مذهبی، خشم مخالفان و صهیونیست‌ها را برانگیخته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662488" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
علت پریدن آنتن گوشی‌ها چیست؟
🔹
بررسی‌ها نشان می‌دهد علت ضعیف شدن آنتن گوشی به عواملی مانند کاهش قدرت سیگنال، نقص فیزیکی آنتن، تداخل الکترومغناطیسی، فاصله از ایستگاه های تلفن همراه، موانع فیزیکی، مشکلات رجیستری موبایل، مشکلات نرم افزاری مربوط می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/662487" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9750278c52.mp4?token=myBcHsBeqDaE4cLQnhJ1Zg6RbldcIqivqEz2h0sL80CwKqRMrVAW20v6CyXeVjQ5EF2JACIqGI9ICyhzV9shGkHBMd89tPI6gegyCFi0jtr9Rh49er-5QIp8RlcG1e-_ubF8_jjcOiLsP9ZEOULtGYUJoVO_QjgArmhOMH72K_HUYu0pIGegrRdhrmHoH7ROHHiL8_vgjsfURf1o-zRgSFTKL5a6AN9qKR2ZELCNP5GXv3KWv3U_CUDZR1SrKIv5GmSNfVvjvYpP1aV7PJGcgT21kY0SJhLIIVgfP5JduzIp9eJ_L1AN6Mg18tBzP0uLfmg7oQf5QrZrTj28QRsxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9750278c52.mp4?token=myBcHsBeqDaE4cLQnhJ1Zg6RbldcIqivqEz2h0sL80CwKqRMrVAW20v6CyXeVjQ5EF2JACIqGI9ICyhzV9shGkHBMd89tPI6gegyCFi0jtr9Rh49er-5QIp8RlcG1e-_ubF8_jjcOiLsP9ZEOULtGYUJoVO_QjgArmhOMH72K_HUYu0pIGegrRdhrmHoH7ROHHiL8_vgjsfURf1o-zRgSFTKL5a6AN9qKR2ZELCNP5GXv3KWv3U_CUDZR1SrKIv5GmSNfVvjvYpP1aV7PJGcgT21kY0SJhLIIVgfP5JduzIp9eJ_L1AN6Mg18tBzP0uLfmg7oQf5QrZrTj28QRsxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم فرانسه به عراق توسط دمبله
⬛️
🇮🇶
0️⃣
🏆
3️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/662483" target="_blank">📅 08:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab56180ae.mp4?token=elVF9D1oKJX16OrHdGRxcIfKBBFh_wgniM0NKC6Gaub4X1ifyZo7obLpu7ibLQDx5rBAchZ4tc6KXMbFJVNYRlS3hqrt0RSb0q-YjO3opw8ubfUFxdI1hK2WbyiMk4wEeSvqD7LSHbQ4mNNbjMz5MTWJvqBkponFXgACxoKL2-b6-rmVps5OLTGH7qrhD4nYVPKlIpJWgwPbmv0guKDrNdyV9TeEaSU0OLzVpJC2_jDdGTC7sxnMgTBjQH3rpkUuKx0BiSmmiIpoPFb_qRXKA3Y899T7CYcJBjiWAWOA0mbmn3WUrfZQBtm4g1desR3y4JyfRCpirah-7t7IdXvzVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab56180ae.mp4?token=elVF9D1oKJX16OrHdGRxcIfKBBFh_wgniM0NKC6Gaub4X1ifyZo7obLpu7ibLQDx5rBAchZ4tc6KXMbFJVNYRlS3hqrt0RSb0q-YjO3opw8ubfUFxdI1hK2WbyiMk4wEeSvqD7LSHbQ4mNNbjMz5MTWJvqBkponFXgACxoKL2-b6-rmVps5OLTGH7qrhD4nYVPKlIpJWgwPbmv0guKDrNdyV9TeEaSU0OLzVpJC2_jDdGTC7sxnMgTBjQH3rpkUuKx0BiSmmiIpoPFb_qRXKA3Y899T7CYcJBjiWAWOA0mbmn3WUrfZQBtm4g1desR3y4JyfRCpirah-7t7IdXvzVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشتباه عجیب مدافع عراق، گل دوم فرانسه را رقم زد
⬛️
🇮🇶
0️⃣
🏆
2️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/662480" target="_blank">📅 07:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662478">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
نان در تهران گران شد
طبق اعلام کارگروه آردونان اتاق اصناف ایران، قیمت جدید انواع نان در استان تهران به شرح زیر است:
🔹
نان لواش: ۲ هزار و ۷۰۰ تومان
🔹
نان بربری: ۱۰ هزار تومان
🔹
نان سنگک: ۱۵ هزار و ۵۰۰ تومان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/662478" target="_blank">📅 07:45 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
