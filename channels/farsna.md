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
<img src="https://cdn4.telesco.pe/file/qOUYWIvdmetH9y2S2FoqTTUn8cTs727VQ3Ijv5azNGpO8pMowt_ZBT9JXM6hFwvR74K4u0toAT_DMT8O9HRnlEe_68X_Zf5BzbXB2UXkJ5uyml0gPBO1mjiafdh_0i9PCLRec9SbAP2qUGH8uoX8Tngu2cukfMi0PhlW3cm30sQnbNmt725ymjFzJsfCJlEvgYEF8ayvRD4Gk8FOdns4DvBhP6WCYGH-umL5lUHeVbsH1bzC3Tf5BMTeyddNUo_VsML4w9lgg7KiceCeN6C0aAvTwoTpvqiqxX2brAmZaTIewC0BIynrYbNoi3QbHJQG5xvxC_bvUYPMrDGfFkyJew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-435560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHCCGYltsq01WGwldLAqNR-jTWl2MuMGOwl_n7MV0MYAAldtHubc7XVTuaVtoPTCOxqXuf9VdAWt2bZESdwiF8iYqlAYRt_070-bvaHEnd5GsC8OUxwZbW6dNepbwSBOqJviikZnndSCWfqMb1M9pPsd_9AJzH84YzMTP-Zq5WoFBau9UiidgDJe-jrfIWqoaGNfga_yBsO6s2IRDhhOkNAA1H-q9Bcav-SyyE9IafTIqjGT2X5NPz58sIyrDBqV2vDzdQZ3UxJBQBpXp57lEf19VyqXFe31a9kp6B8QjpJQyoBn8JbewKNs420qKOWfAbgbRIgURel4fRX-qG1kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید رئیس‌جمهور از آثار حملات و خسارات وارده به مجموعۀ ۱۲ هزار نفری آزادی  @Farsna</div>
<div class="tg-footer">👁️ 199 · <a href="https://t.me/farsna/435560" target="_blank">📅 12:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
حزب‌الله: یک نیروی اسرائیلی را در داخل خانه‌ای در شهرک «دیر سریان» در جنوب لبنان با موشک و توپخانه هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/farsna/435559" target="_blank">📅 12:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یارانه اردیبشهت دهک‌های یک تا ۳ واریز شد
🔹
سازمان هدفمندسازی یارانه‌ها: یارانۀ مرحلۀ ۱۸۳ مربوط به اردیبهشت به‌حساب ۱۰ میلیون ۲۳۰ هزار و ۶۸۱ سرپرست خانوار دهک‌های اول تا سوم در سراسر کشور واریز شد و قابل برداشت است.
🔹
براساس دهک‌بندی اعلام شده از سوی وزارت رفاه ۲۷ میلیون و ۹۱۷ هزار و ۲۶۹ نفر در دهک‌های اول تا سوم قرار دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/435558" target="_blank">📅 12:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
یدیعوت آحارونوت: درپی اصابت پهپاد حزب‌الله به محل استقرار خودروها در «راس الناقوره»، ۳ نفر مجروح شدند که حال ۲ نفر از آن‌ها وخیم گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/435557" target="_blank">📅 12:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">واکنش سخنگوی قوه‌قضائیه به دزدی دریایی آمریکا؛ توقیف کشتی‌های متخلف آمریکایی با حکم دادگاه صالحه و مستند به قوانین داخلی و بین‌المللی است
🔹
سخنگوی قوه قضاییه با انتشار متنی در فضای مجازی به روند توقیف حقوقی و قضایی نفت‌کش‌های متخلف آمریکایی در آب‌های ساحلی متعلق به کشورمان پرداخت و به راهزنی‌های دریایی ارتش تروریستی آمریکا و زیر پا نهادن همه قواعد حقوقی بین‌المللی در این دزدی ها اشاره کرد.
🔹
توقیف نفت‌کش‌های متخلف آمریکایی، امری مستند به قوانین داخلی و بین‌المللی است. توقیف این نفت‌کش‌های متخلف ناظر بر آرای متقن و قطعی محاکم صالحه ایران است که پس از طی فرآیندهای قانونی صادر می‌شوند.
🔹
ایضاً مراتب قانونی و مستندات تخلفات حادث‌شده از ناحیه نفت‌کش‌های مزبور نیز برای طرف آمریکایی ارسال می‌شود؛ علاوه بر این‌ها، براساس کنوانسیون حقوق دریاها ۱۹۸۲، کشور ساحلی می‌تواند کشتی‌های کشور دیگر را به سبب تخلف از قوانین و مقررات داخلی و بین‌المللی در قلمروهای دریایی خود و یا دریای آزاد توقیف کند.
🔹
اقدامات قانونی ایران در توقیف نفت‌کش‌های متخلف آمریکایی، برابر و همسنگ با رفتارهای خصمانه و چپاول‌گرایانه آمریکا در دزدی دریایی علیه کشتی‌های کشورمان نیست؛ رئیس‌جمهور آمریکا صریحاً به دزدی دریایی اعتراف و حتی مباهات کرده است.
🔹
رژیم واشنگتن همه حقوق و قواعد جهان‌شمول را به سخره گرفته است. ادامه سکوت سازمان ملل در قبال یاغی‌گری‌ها و طغیان‌های آمریکا، این سازمان را از معنا تهی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/farsna/435556" target="_blank">📅 12:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435553">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvrENRvAKrP5zTsWnlT1ePM53wCeAwERL_aMpXPXKjCZm_EJ4EsmNEhQ4h7QFB5xuo6Fme-9KQKb9Ou1fDvt9xzhr27-BabazKyWXJ_ELxMLFCFmQkjsFym686GBqaCeCjn3TIUCUuWJBjxgUwZBrrqfXrcflkzBJjwQT3fbyzzoSEg5Bo8jkNXuJHHpdoanxveihHuD0ExKLcemdHafc1V_giMvgjBCCGbPw4p0wMdp5DwXx07cKkcjKdOvGkseBQ4_7Yw9VGy_FPHFiEZ5MeKBxMxPp98Aa35SOhP95nSLcx_MFvfjDtVxi-2dWWXDAEZN0BvacE2dQVzr8FVV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxoAWWIHP1AFPJTTQzBPrEPuaOOFa-J5EkVP9EpifGQD-hXV_UWzkaNCq0pnT1J67v7E7zeSp1pL1hSayFT4R8xqpBcMwfCV8Kpf-zdDTEh9IFZodFpk01sUgFhVyN0u70gPaVzhVc7-uCveBNtnwbI6LxzKIS8A5_MK3enFEdp-QMigM-O7oluEhygrjYRHtMVu5SyKj6BjdfpoaWyI-JYgvbegN9DK4B4EUiV2XSgad3UTEexaKXJHe-3LHbKimG2rqL9nAyG2c70I2cH8qrAGCQmOFF0UQXTi9sUs7Z94lK-S1jpqzTrnF9fXwKYN0cpmV422vlmpG8cRWoMytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6hrCsEpdadiIxFg43V7UcSosyjnp-kvsizLSyii-saZ0exD8M5uOCrM-aTmucatJrCchekgIbZsVpll9Cpzsm--J7t_fGu7PfYJcsaOAah5Jl8LROs3u5B1oA2d8sdKgVUDuz0bZaMhijR-RM_w_qxXPiSjkNeyUsWbWt6XaTGc1CQrL330w7I_Sp3RPAIsBaOoQUAb0P-d09RvnyhdtlOGNtZwOL46U4O158Xnv5OCb-Q-kPtuJjax-WtLKXMlbS6JPjEbTSaTfw7I9o4f0t56wpF5I59L47bMZL9TXmeOM3ZjQGtcPgd3t1rPPXrLGZi-GGh0Yjjm6w4dSGG5MQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حملۀ موشکی آمریکا و اسرائیل به ورزشگاه آزادی
🔹
در حملۀ موشکی صبح امروز آمریکا و اسرائیل به سالن ۱۲ هزار نفری ورزشگاه آزادی تهران، کلیۀ بخش‌های سالن و ساختمان‌های اطراف آن تخریب شدند.
🔹
آمریکا و اسرائیل در روزهای اخیر بارها به مناطق مسکونی، ورزشی، بیمارستانی…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/435553" target="_blank">📅 12:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435552">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03b2c65df.mp4?token=uVNa6e6klP_D7_xW3zK9N9K7CPcmndd2NA7_X_Is4WfOPb3NE6h9w8f1mx8-1kcKYC3JqQf908VPFBoXaPVx4H7aOi5XYl6Ar-2H53ONWVom31Gc0p3G2zF0WcqzdqL_QKKbPPD-nlvo27UMbCgq-niTQW8-wDh_lw0lmw7eRB9EqlQZ9gTZRf51Z4CmlPzEe43wfFmjch4lC3hZ46Q-bRNLunjz-Ga2ILb9CZXqpjFA34VNQq8p5UQHLwX0-ZGOrBF0ytnSpRgndLs4CYTuz4GANFKZb6PAjs8KajdaiqVg6W8TC66T82HXI9SQuGmahbvt1JOVMpCTBWwgpbfwY7O-FmlvWJrpj5gnQd6QWRdaR3IpEN_hdEN8lbC5mu5Coo5mSgA6TTabc7yRmoT11EhyDOT0en6oZz8QtdBH9RvUEnEwFf8qjX6syC92ne6D80F2bubXS-7JNt8HhFBd2EuemsmvD2WWBWJMQYwYwTEfwi7Gr6zcmfe-awmGvVNTsSICmsQvHj6qi8Hnjs2jHR87lUzdeRAW5AgmJY-9sTER0y_-SndxJj9MxANIksZqnCVBsIYX-cETZpYZaKoIAVF6umBJAsiFFZnZNHrLL5cE3soisEpiy9Ep2AEtVBpNbBt3BKefuP6RIUwUMGk5Hj9vOGjFDQ-C5UTdrHuQjNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03b2c65df.mp4?token=uVNa6e6klP_D7_xW3zK9N9K7CPcmndd2NA7_X_Is4WfOPb3NE6h9w8f1mx8-1kcKYC3JqQf908VPFBoXaPVx4H7aOi5XYl6Ar-2H53ONWVom31Gc0p3G2zF0WcqzdqL_QKKbPPD-nlvo27UMbCgq-niTQW8-wDh_lw0lmw7eRB9EqlQZ9gTZRf51Z4CmlPzEe43wfFmjch4lC3hZ46Q-bRNLunjz-Ga2ILb9CZXqpjFA34VNQq8p5UQHLwX0-ZGOrBF0ytnSpRgndLs4CYTuz4GANFKZb6PAjs8KajdaiqVg6W8TC66T82HXI9SQuGmahbvt1JOVMpCTBWwgpbfwY7O-FmlvWJrpj5gnQd6QWRdaR3IpEN_hdEN8lbC5mu5Coo5mSgA6TTabc7yRmoT11EhyDOT0en6oZz8QtdBH9RvUEnEwFf8qjX6syC92ne6D80F2bubXS-7JNt8HhFBd2EuemsmvD2WWBWJMQYwYwTEfwi7Gr6zcmfe-awmGvVNTsSICmsQvHj6qi8Hnjs2jHR87lUzdeRAW5AgmJY-9sTER0y_-SndxJj9MxANIksZqnCVBsIYX-cETZpYZaKoIAVF6umBJAsiFFZnZNHrLL5cE3soisEpiy9Ep2AEtVBpNbBt3BKefuP6RIUwUMGk5Hj9vOGjFDQ-C5UTdrHuQjNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منوچهر متکی خطاب به نماینده بحرین: شما در جنگ تجاوزکارانه آمریکا شریک هستید  رئیس شورای اجرایی اتحادیه بین‌المجالس مجلس: سخنان بی‌ادبانه نماینده بحرین به‌گونه‌ای بود که گویی عامل آمریکا، ایجنت آمریکا و اسرائیل سخن می‌گوید.  شهر کوچک بحرین، ۳ میلیون متر مربع…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/farsna/435552" target="_blank">📅 11:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435551">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
دقایقی پیش زمین‌لرزه‌ای ۵ ریشتری در عمق ۸ کیلومتری بردسیر کرمان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/435551" target="_blank">📅 11:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5938e459bf.mp4?token=fQli62oBZl2xqH_1hZXAfaHfv7Savte6iizENBC8vEM-5kq3q2JpGaVR71DICIaM6FdM5JYeU0FykZRlDLKjmsa_JU1ZNW9KwOkThoP1iscv1sFKPkGJMkgvvlPISazSZcRpXZzuejVavPtBnwAEBX0wRf-zZCeJjzgaRQE7nJp3ZbA7EtoSZd8pFqipoWtG0td3ugjQhjhx5INVZI4JtDJVcNMViv1yI1cHdLpVw0auSaEKUStRmSAEiBNsBQXvt5aIhK6Yxxaehs0O5o4gO2vPAGOMoCGd6YNQzgbfg8Cf1-nLD-FSz-uHfWS1vnpY-X7E9spsPLH83f3m92ajyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5938e459bf.mp4?token=fQli62oBZl2xqH_1hZXAfaHfv7Savte6iizENBC8vEM-5kq3q2JpGaVR71DICIaM6FdM5JYeU0FykZRlDLKjmsa_JU1ZNW9KwOkThoP1iscv1sFKPkGJMkgvvlPISazSZcRpXZzuejVavPtBnwAEBX0wRf-zZCeJjzgaRQE7nJp3ZbA7EtoSZd8pFqipoWtG0td3ugjQhjhx5INVZI4JtDJVcNMViv1yI1cHdLpVw0auSaEKUStRmSAEiBNsBQXvt5aIhK6Yxxaehs0O5o4gO2vPAGOMoCGd6YNQzgbfg8Cf1-nLD-FSz-uHfWS1vnpY-X7E9spsPLH83f3m92ajyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وایرال شدن تصاویری از فیلم‌برداری ایلان ماسک در سفر چین و جذابیت دکور سقف «تالار بزرگ خلق» برای مارکو روبیو
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/435549" target="_blank">📅 11:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U21WyXKCaFIi4as67h6jbWN75D5FnTWg0S-WDPFKlBybZkHbd2hUFc6ifMwGTZww5SJlzXJWnio6dw-h1fprTDmJCxsG9iO5S1dWGNbjPaIHIadFEfNUGy9pZAdL8hxeVs8YMFOxZYNOodu5zO4LZv5D1txE7lnhm7YbL33rWsIpUPz5LRDWFwCusHUin-b7UdXW_gs6U0xooxWZjFjn_22Uf_PtZ0zXIzaBtFQaKQg8DZar2oR9kIudsUsjbV_e16uh53GOYzccP4kQqY6bdksEzQzBYc_nHr3DSZgdHhsbuzed2PK1Udgn4eml-lKaZ-7ynzErH36OKuRGoPoBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع یک حادثه دریایی در نزدیکی فجیره امارات
🔹
منابع رسانه‌ی از وقوع یک حادثه دریایی و وقوع انفجار در پی حمله پهپادی به یک کشتی در سواحل فجیره امارات خبر دادند اما چیزی نگذشت که مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی درباره یک حادثه در ۳۸ مایل دریایی شمال‌شرقی فجیره دریافت کرده است.
🔹
این سازمان ادعا کرد که این کشتی هنگامی که در حال پهلو گرفتن در الفجیره بود، مورد تصرف قرار گرفت و هم اکنون در حال حرکت به سمت آب‌های منطقه‌ای ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/435548" target="_blank">📅 11:19 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTHypT4K10Hnj5GdX43pJcDFRC1bUkkAISHCUJnKd_oJgrcaOLqKeQVu9GWBblsRff5uFbHdEn-7lAb3czNU_p_JHwQa_D6UeLqFhxxZcqC5Z7kjvwnSNSdDqg9a0FAa7IuPlPSNyVCwj9erkgHyLCm3hq26ZpPRxi3bYJH1KxNcRu01mMnp7ErER1EOv-wO2rDurkBhKn9z88U5hL1NnJh52_kbboFVR3a4usQB58KOmaoKQqgC8N5-qae4Zsk-psDxwsC2j4hGSxH9YmndocrGYXrfHExHV0CZFRGw8J2xvWtHkSM_7BXSmT7zDDLf7BXM0HY3pjCjTAmMCayXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارو ۳ برابر شده اما پوشش بیمه هیچ!
🔹
یه عمری پول بیمه دادیم تا سر پیری عصای دستمون بشه نه نمک روی زخم» این را پیرمرد بازنشسته‌ای می‌گوید که برای خرید پلاویکس، انسولین و داروهای فشارخون نزدیک به ۵ میلیون تومان پرداخت کرده؛ زیرا داروخانه با بیمه تأمین اجتماعی قرارداد ندارد و او نیز مجبور است که دارویش را از همین داروخانه تهیه کند؛ پلاویکس خارجی هم در همۀ داروخانه‌های سطح شهر پیدا نمی‌شود.
🔹
براساس تحقیقات میدانی خبرنگار فارس، در حال حاضر تعدادی از داروخانه‌ها و مراکز درمانی اقدام به قطع همکاری با شرکت‌های بیمه‌های درمانی کردند و خدمات و اجناس‌شان را به صورت آزاد به بیمار می‌فروشند.
🔹
تعداد دیگری از داروخانه‌ها نیز با بیمه همکاری می‌کنند اما دیگر داروهایی که درصد پوشش‌دهی بیمه‌اش زیاد است را از شرکت خریداری نمی‌کنند؛ انسولین و اسپری‌های تنفسی از دسته اقلامی است که مصرف آن برای بیمار حیاتی است اما داروخانه‌ها برایشان صرف نمی‌کند که این اقلام را بفروشند.
🔹
بهمن صبور عضو هیئت‌مدیرۀ انجمن داروسازان ایران می‌گوید که داروخانه باید پای بار پول شرکت دارویی را تسویه کند، به بیمار با پوشش ۹۵ درصدی بیمه دارو را بفروشد و حداقل ۶ ماه بعد پولش را از بیمه دریافت کند؛ آن هم با این تورم!
🔹
یکی از داوخانه‌داران مرکز شهر به فارس می‌گوید که در ۴ ماه گذشته قیمت برخی از دارو‌ها ۳ برابر شده و شرکت پای بار تسویه می‌کند، من چطوری می‌توانم با بیمه دارو بفروشم، ۸-۷ ماه بعد پولش را از بیمه بگیرم و با وجود تورم مجدد آن دارو را جایگزین کنم؟ مجبورم به بیمار بگویم من نسخه‌ات را آزاد حساب می‌کنم اگر نمی‌خواهید به داروخانه دیگری مراجعه کنید.
🔹
درحالی که به گفتۀ داروخانه‌داران پایتخت، دارو در ۳ الی ۴ ماه گذشته ۳ برابر شده، آخرین افزایش پوشش‌دهی بیمه‌های درمانی که شورای عالی انقلاب بیمه مصوب کرده برای ۶ ماه ابتدایی سال ۱۴۰۴ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/435547" target="_blank">📅 11:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
طباطبایی: معاون سیاسی دفتر رئیس‌جمهور در روزهای آینده معرفی می‌شود
.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/435546" target="_blank">📅 11:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf24ab2a9.mp4?token=m5XpQpdRjkoCZ2wynBt7LZdTfOy8vdpecU3AGWqV5mieEi5IkJtK8tn6UJzu0un81_P0aqHQd19-tZHZx8vtxthSdrofiu7gT9GOEOA9YK0mphfTlrZfGTl7B-fYzuND-6A83AqKvQ2CEsj0HYjLI9o-coi6Ok_FKI2etm3LZzmSMee2IkuBMaRKVf9L4z7yyjWacXdIEXU6BlEBHKpIIsSwAIF9_n8QV-DQLGbPE8ppkxVt5_5M6EbqRVfQyxvCu2eo-i8aogx_-CkAN429xrzEBfXyfjGVbrLBlbZKWrFsAtqOSY2EApnqfT4DJMD07xGEC0OVSrMy9-K9da9CAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf24ab2a9.mp4?token=m5XpQpdRjkoCZ2wynBt7LZdTfOy8vdpecU3AGWqV5mieEi5IkJtK8tn6UJzu0un81_P0aqHQd19-tZHZx8vtxthSdrofiu7gT9GOEOA9YK0mphfTlrZfGTl7B-fYzuND-6A83AqKvQ2CEsj0HYjLI9o-coi6Ok_FKI2etm3LZzmSMee2IkuBMaRKVf9L4z7yyjWacXdIEXU6BlEBHKpIIsSwAIF9_n8QV-DQLGbPE8ppkxVt5_5M6EbqRVfQyxvCu2eo-i8aogx_-CkAN429xrzEBfXyfjGVbrLBlbZKWrFsAtqOSY2EApnqfT4DJMD07xGEC0OVSrMy9-K9da9CAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جعفر دهقان: بمباران مدرسۀ میناب توسط آمریکا قطعا عمدی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/farsna/435545" target="_blank">📅 11:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPtrWXwWH8zSHSW5gt1HcY-vHx5YfZ_uFVKVbNN7dceIwpgbSgtL-e5fI65nUM8Eh1-TrJzysfQOKBpGt7oR5KtoXVbqAPYXxsPeYJPH3XjF6Jwjpi5P_IUDd6-b8c6vTXmh1OBYfWc9NkhlvRgacA7HRaVn4dlymsaUwM9HoM82hfai6gTE_TkRB15MUpzTSzXpWgvgLFWOVtBfqXOatvYFhQx-mgCjsWGC219LIITPuHZZ9cADQDXK070rsGvvGt-pb26J0Iz_AwS0-N2qXoCW2wKL3tngFOxQpNNtllwi_aWNhEQHAAzz5oVMApNry02ZoOcmQxHE9ojZi7UgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c41m1E2W14KdrcxMUcViUVXw128VvpeBGBS7D9g2aacvs1NqMXqp_3gf8I1emYP67H_f06rGxkcBH9Zg55XZ7mxQhLzF0hlNH2eQNLNpbUm-tihxavYlsV00quPosuqEKacdy3S48lyVdOPai5dlSR-crSB53XxufBVL8sUxPzaJSprTFZ5CfqMlLwGG70D7cyEs_cFbnC2d7wpP7pI2VgyhcVWjV9CTzG9hLsOGERza3UI6yCT3NQIePyuzXWwlBiGubW92lbyn2PTPZ9ZhzsJ6TyP8k0p3nuEkYu5r7BFZhRxmxWlu3wQjsZcfKSXR1NM0IxOcr8sHN46XIt-oGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQNus4NnXfYgk0NVrb8rj1LGXzyqNYN7QsSGwZFZBnPxSVLWhx9igeODng0D3DrGqbozzcVfZyT-JIbkUUYagl8UJWsTH424RxpLjWzg9BIPQBLRoeUvUa4XmPJXhCm0ksppgV5-zTPpbvcV6K0Rzga1GTYlz8SlkPD_EPNVrepzZ3dZXDpsjoVMvF_aTgBGRiSSrmrZLZecKkCU60_TuhUzTQSYwU15MPakvDGN97PFUdywkJd6_qvmMhqVb6_1fgbiY-kadtU5TDs__i4sDBsMiuONwuD-18UFaFKb5EY-7L88orPj8-d_P1IOttgDyMONNjenAoCMJ54sg2w4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hc5SrgP-DvBrCeZ0aFkNp1vmHeOEuGm3rGULI7YG32RWx2qcMwSFWGl43q_OCBU5oIEw4N2WQkrgT_e0Lx6wtrNduLcFubHdgKEx_o5OBykF3KID6L9uhq2ilaisw3X6ud40pwZC4ZXrUf9F1kruB3uvv223olK46J_MzMbdZ6jD5cS-Il1XH8i1xIqWHEgrfl87FiWkep5lWbjbGMBVqhnGM99HmpAkC4BQecAgMZWiE8rjEdNHpvRc9zcchZti8qsYK_wJb01zTY1acf-do1pjxoy1gRC9ZAbLCFSavaKcu-fxe2MgPZPpW0EsoRYB1JJdfg2z8a9hmGr2WKYUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qye6Ysnywo9-ppSUEDpv8tScCnCYJg3SGQzQhJePBkUG6z_rUR9hDxh5XnZJzOPrV_R25ffv1xxTGB7C2JaJZgOqYk_Q3CKEBC0xgtvPXnQRIGl6n4m8W_NZqrrm4PmtnWV3apdmAENGDN-fxMddrMM1hMJnR3yS4I4CML1zz6WY1IGryhZiIcEI32qr_pbYrcH4K4ST9TokeWmHHP6YihyNLPVrtAx3G_6goobS-hfAbVx7whBVQQwuSv-IMzKHisjcqrHeCk-YfM4SmdCQFLlh_6xw-AV863-ftK7nQjEieToH_Cs46DwbtNSUZ8iRMxYU0PJjhtOKVHErbkydlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
ترامپ به سوال دربارهٔ تایوان جواب نداد
🔸
خبرنگار: گفت‌وگوها چطور بود؟
🔹
ترامپ: عالی بود. چین زیباست.
🔸
خبرنگار: آیا دربارهٔ تایوان صحبت کردید؟
🔹
ترامپ هیچ پاسخی نداد. @Farsna</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/435540" target="_blank">📅 10:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ece0d934.mp4?token=OosBsc_7e50bBCrxh8w6Z6T-GaAaDwMBH4T_2YORRQpRftCHxD1A4EZF5e5RyIQqjQyVjypCKRyu0jQGl2fgdDWCj3I_7-IeesfvuapYP3A30N3WwvwunBSIVDo_sy5A1Uhuy_0EYmmtwlYIafm7n2FJa2VdOsQpeWfiBDPjAq2J0-MsegMx6MnDrcg1Sp5wlYPuYQNagSQBsZQWnWL0bxZbGbi6WisyB1SqwfonZ-Y1CEsol3zeVesj_0VYCvyj6FHpyexRMWOwM0R2x9HlfEuv4eu1PF5xPZOJklVNk-d7JqBkZod5eIXSbOKEqvnFQKjxgp0iyLqpALRlYjzbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ece0d934.mp4?token=OosBsc_7e50bBCrxh8w6Z6T-GaAaDwMBH4T_2YORRQpRftCHxD1A4EZF5e5RyIQqjQyVjypCKRyu0jQGl2fgdDWCj3I_7-IeesfvuapYP3A30N3WwvwunBSIVDo_sy5A1Uhuy_0EYmmtwlYIafm7n2FJa2VdOsQpeWfiBDPjAq2J0-MsegMx6MnDrcg1Sp5wlYPuYQNagSQBsZQWnWL0bxZbGbi6WisyB1SqwfonZ-Y1CEsol3zeVesj_0VYCvyj6FHpyexRMWOwM0R2x9HlfEuv4eu1PF5xPZOJklVNk-d7JqBkZod5eIXSbOKEqvnFQKjxgp0iyLqpALRlYjzbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: زمان آن رسیده که زورگویی آمریکا به زباله‌دان تاریخ سپرده شود
🔹
برای تقریباً همۀ حاضران در نشست بریکس، مقاومت در برابر زورگویی آمریکا نبردی ناآشنا نیست. بسیاری از ما با شکل‌های متفاوتی از همین فشار و اجبار نفرت‌انگیز روبه‌رو هستیم.
🔹
اکنون زمان آن…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/435539" target="_blank">📅 10:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435538">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f88e62bfe.mp4?token=R-ubVC52C_ndnUqVJZPteRxmXt8_2uMeCgEX9ioVj8Scr7cmnyk28XW1JbrjsCRPPrVWiDXm8Of5iPU2NCiP7hyrBxZVAAMZVgjJkKZHv92MbBA76ELcUJUy4zCn6BJmKct4KXKIE0MokQCfj0svgKFCPuezLT2uW2C77Ls8F0e9sSHUqVoX3IAj-Mqyq07FP1G-i7dO_OabZ0XLjTtkos8tcM_HL_xREIF4kQguZPu7tnHI7JbJFo2vVyDhDSOEG5hpRN27foW9jHUeniObKqMIAO0X8Luj8x_l2PcU0s7LZtdcHKOipVjcXgOlMN_6KfAkf2XnJ0ZXQZpZTuoBkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f88e62bfe.mp4?token=R-ubVC52C_ndnUqVJZPteRxmXt8_2uMeCgEX9ioVj8Scr7cmnyk28XW1JbrjsCRPPrVWiDXm8Of5iPU2NCiP7hyrBxZVAAMZVgjJkKZHv92MbBA76ELcUJUy4zCn6BJmKct4KXKIE0MokQCfj0svgKFCPuezLT2uW2C77Ls8F0e9sSHUqVoX3IAj-Mqyq07FP1G-i7dO_OabZ0XLjTtkos8tcM_HL_xREIF4kQguZPu7tnHI7JbJFo2vVyDhDSOEG5hpRN27foW9jHUeniObKqMIAO0X8Luj8x_l2PcU0s7LZtdcHKOipVjcXgOlMN_6KfAkf2XnJ0ZXQZpZTuoBkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوفان و سیل در شمال هند با ۵۶ کشته
🔹
دست‌کم ۵۶ نفر در اثر طوفان شدید و باران‌های سیل‌آسا در شمال هند جان خود را از دست دادند.
🔹
به گزارش خبرگزاری PTI، بیش‌تر قربانیان زیر آوار دیوارها و سایبان‌های فرو ریخته گرفتار شدند.
🔹
گزارش‌هایی از زخمی شدن ۵۳ نفر، آسیب دیدن ۸۷ خانه و کشته شدن ۱۱۴ دام خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/435538" target="_blank">📅 10:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435537">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f501e44a.mp4?token=iTY_dA5G7s8-_fZZRjGXOtXkTYjAWfBf99STgStBiXg8laHK2raR7_QX4HHHtru2FJwmfKhNwAphjTOvnqgYD2wC9K8767hC3_xr6069dxiAqOkZULqK2QmOMuIXCbd7Lic0ILISrLou1GwRz6kFf-CbIqEbjZDp9Mx86KoGeYsf5s00G66hQj83-mcLfnYUCY2Jzpp5b3RCqfUWumud8fXYwxI2TQ1vRz1pFx61Re9QD1-8uGngMKUS5sb0ZEkQz31MwkABHFMUxXeUj-RUfVMHOsWjbLvAaI27sDnn9TY6neX86nQ2Hevew3ua7UNsp3nBTSbsVmp4PUjh9kVKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f501e44a.mp4?token=iTY_dA5G7s8-_fZZRjGXOtXkTYjAWfBf99STgStBiXg8laHK2raR7_QX4HHHtru2FJwmfKhNwAphjTOvnqgYD2wC9K8767hC3_xr6069dxiAqOkZULqK2QmOMuIXCbd7Lic0ILISrLou1GwRz6kFf-CbIqEbjZDp9Mx86KoGeYsf5s00G66hQj83-mcLfnYUCY2Jzpp5b3RCqfUWumud8fXYwxI2TQ1vRz1pFx61Re9QD1-8uGngMKUS5sb0ZEkQz31MwkABHFMUxXeUj-RUfVMHOsWjbLvAaI27sDnn9TY6neX86nQ2Hevew3ua7UNsp3nBTSbsVmp4PUjh9kVKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان اداری و استخدامی: ساعت کار اداره‌ها از ۲۶ اردیبهشت تا ۱۵ شهریور ۷ صبح تا ۱۳ خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/435537" target="_blank">📅 10:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfUc9jRMVXLlNLqcSKhxXn9QnwDDV-V9b72G5Ag8YWfLgcv9qGmrfuTdDTuGfrG321WQbZ52r6Boewr_Lwfhiq-Ldy2eALwXX_9IH99J9jZI1y3tM5omM6ulWQ0WDuvzOo138SsVut_M7iCvg3dkAgvCPBqE3IF9x1NpY0aOtm1mFUaZcsKNPvVKfGVi0TrmQy6F8gTxSuFYKwufPx9MTG7rpJ5JSE3MTzhqfY-6-XM-n_uDBPxFs4euuAHI_rr3r4hclazn5rSN_ZGe1wW1XIwws60GJYuk7t5qDOsPa1w30MEFora-qDZxXxHTZbn58gALxrF50SdDTzy7olp2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ملی‌پوشان و مردم باهم در میدان انقلاب سرود ملی خواندند  @Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/435536" target="_blank">📅 10:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d0ac827.mp4?token=cNj0sb2_NfHs0LHy8Ky9NQTpPyAGKF6D6zt05O76QSYSeGSVm4W4-ptrwS4rKakFOS2765y4eNZ0AwzcBA6UvU6QOnnwLYHin28rl89VYJoHmvP3SYgbwQ_Qtag9NeP2cdrua6DA5_d-jGZ-bLVmCE9is9ONbbF622I1Oo69XMApSbD-u3kFum8Z0HimgDXSjxwoq6sieHvyRZNoiZZkSiS7JwtteGXjP8wvn5I7sPYY7w0abpf_ihs3bg6r3XkwYCAQyp6lgDofUb5Ep7pzsmSn473_LHzbp5G-9szEA1qZrcKccdA9nA93oZXetN3PO-ZC_KsSx7ABFOrWmKyvejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d0ac827.mp4?token=cNj0sb2_NfHs0LHy8Ky9NQTpPyAGKF6D6zt05O76QSYSeGSVm4W4-ptrwS4rKakFOS2765y4eNZ0AwzcBA6UvU6QOnnwLYHin28rl89VYJoHmvP3SYgbwQ_Qtag9NeP2cdrua6DA5_d-jGZ-bLVmCE9is9ONbbF622I1Oo69XMApSbD-u3kFum8Z0HimgDXSjxwoq6sieHvyRZNoiZZkSiS7JwtteGXjP8wvn5I7sPYY7w0abpf_ihs3bg6r3XkwYCAQyp6lgDofUb5Ep7pzsmSn473_LHzbp5G-9szEA1qZrcKccdA9nA93oZXetN3PO-ZC_KsSx7ABFOrWmKyvejzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکلیف نحوۀ امتحانات نهایی ۲ ماه دیگر روشن می‌شود
🔹
در حالی که پیش‌تر احتمال برگزاری دومرحله‌ای امتحانات نهایی شامل داخلی مجازی و حضوری کشوری مطرح شده بود، حالا وزیر آموزش‌وپرورش اعلام کرد «تا ۱۵ تیر برای مشخص‌شدن وضعیت امتحانات نهایی صبر می‌کنیم.»
🔹
به گفتۀ…</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farsna/435535" target="_blank">📅 10:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590faf174d.mp4?token=cALCCeDWljcQFMx2X_EJFqHKkOkYFg_vhbs5O3Z3_4e_P4Ih8QGruKvBt0sGEVl9znnDlLcL76bHiQfF-Egl2JeENmxAIJ8N15SkP9IodYk5yY8cA9tTIIQTkiE8eE0AIB6sDwy8scKXEDUG9-1yH2LNjNG3QtEB8XuqR490UxRloE_yGA94yLP6G7HSl5Ns8_DKQa5XazzttSGBMo55MHlz138a4mq85YDmS17YMmmpGdiytUyeAcPuF3M1X0ie_ZHNEfJ9H4PHW3z11CSov5Qh7i6T9WBDLi4eIJaadBIFcrhXU8_tvB4rGpJaJM1DmU9rv4FBoy41lqwB-9jgoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590faf174d.mp4?token=cALCCeDWljcQFMx2X_EJFqHKkOkYFg_vhbs5O3Z3_4e_P4Ih8QGruKvBt0sGEVl9znnDlLcL76bHiQfF-Egl2JeENmxAIJ8N15SkP9IodYk5yY8cA9tTIIQTkiE8eE0AIB6sDwy8scKXEDUG9-1yH2LNjNG3QtEB8XuqR490UxRloE_yGA94yLP6G7HSl5Ns8_DKQa5XazzttSGBMo55MHlz138a4mq85YDmS17YMmmpGdiytUyeAcPuF3M1X0ie_ZHNEfJ9H4PHW3z11CSov5Qh7i6T9WBDLi4eIJaadBIFcrhXU8_tvB4rGpJaJM1DmU9rv4FBoy41lqwB-9jgoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صفری: روابط ایران و چین درازمدت و راهبردی بوده و خواهد بود
🔹
سفیر اسبق ایران در چین: روابط ایران و چین بسیار درازمدت و راهبردی و استراتژیک بوده و خواهد بود. چین همواره به چهار عبارت مورد اعتقاد خود پایبند بوده و ما در مسائل حقوق بین‌الملل و حقوق بشر همراهی نزدیکی با چین در دنیا داشته‌ایم.
🔹
چین همواره منافع جمهوری اسلامی ایران را مدنظر داشته و ایران نیز منافع چین را. یکی از مسائل بسیار مهم، مسئله انرژی است؛ هم تأمین آن و هم امنیتش. چینی‌ها آگاهند که تأمین امنیت و سرویس‌دهی نفت در خلیج فارس و دریای عمان همواره از سوی جمهوری اسلامی ایران انجام شده و این سرویس برای چین برقرار بوده و خواهد بود.
🔹
سفر ترامپ به چین از جنس سفرهای عادی بین دو کشور است و اغلب اختلافاتی مثل تایوان، تعرفه‌ها و فلزات کمیاب مطرح بوده است. اما من معتقدم قدرت اقتصادی چین بسیار بالاتر از آمریکاست و با همین قدرت اقتصادی و تجاری، بهترین شریک برای آنها در منطقه در تمام زمینه‌های فرهنگی، امنیتی، سیاسی و اقتصادی، جمهوری اسلامی ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/435534" target="_blank">📅 10:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwBZrtzakYSl5_ZUu8bMOaBXt7ilaDFz2K2q9uyzoLEA0_y2yurWvAdRDrOc9YRfrS-KzB27VPUGAL_Nsd2DhASVFYIhnAbhKq_gK1KYF1IvM_T5VN50j3Jd3ZRabFgNT0xa5XPmtiTftJMeaXTww9pqmSO-UBi6mY4eaODmT9nI6WQMjiOM-vCTG7RUl_veD9AsC41fbM3OrppFIC9Lj7Mo_SwkefeZISL8dDftkPDs84ttYPpIvh-AMfBILfOhtsWFQ8A7XhqapOBWjm_JVoBKDlLCoYNlMTv9nWa7bmTzvgcAlhoY6-SInwaZORLjsNmOJv_KWVVmWVv-8ZlCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: باید برای همگان روشن شده باشد که ایران شکست‌ناپذیر است
🔹
سخنرانی وزیر خارجه در نشست وزرای خارجۀ کشورهای عضو بریکس: من از سرزمینی کهن می‌آیم؛ سرزمینی که رهبرانش با شجاعت در کنار مردم خود برای تحقق عدالت، استقلال، و دفاع از حاکمیت و تمامیت ارضی ایستاده‌اند…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/435533" target="_blank">📅 10:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اموال ۴۷ نفر از خائنین به وطن در همدان توقیف شد
🔹
با دستور مقام قضایی اموال ۴۷ نفر از خائنین به وطن و کسانی که علیه امنیت و ثبات کشور اقدام کرده‌اند، در راستای حفظ حقوق عامه به نفع مردم در استان همدان توقیف و ضبط شد. رسیدگی به پرونده این افراد در جریان است.
🔹
با دستور مقام قضایی اموال ۴۷ نفر از خائنین به وطن و افراد تاثیرگذار در شبکه همکاران دشمن در راستای حفظ حقوق عامه و اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی علیه امنیت و منافع ملی در استان همدان به نفع مردم و هزینه کرد برای بازسازی اماکن آسیب‌دیده از جنگ توقیف شد و پرونده این افراد در حال رسیدگی است.
🔹
در حال حاضر ۶ نفر از این افراد مقیم کشور انگلیس، ۲ نفر مقیم سوئیس، یک نفر مقیم روسیه، ۸ نفر مقیم آلمان،۶ نفر مقیم ترکیه، ۸ نفر مقیم کشور عراق، ۴ نفر مقیم آمریکا، یک نفر مقیم ایتالیا، یک نفر مقیم عمان،یک نفر مقیم کانادا، یک نفر مقیم عربستان، یک نفر مقیم ارمنستان، ۲ نفر مقیم غنا و ۶ نفر در داخل کشور هستند که دستورات لازم برای ضبط اموال آنها صادر شده است.
🔹
پیش از این نیز با دستور مقام قضایی اموال مهرداد ماهر که نقش موثری در شبکه همکاران دشمن و خیانت به وطن در استان همدان داشته، به نفع ملت توقیف و ضبط شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/435532" target="_blank">📅 09:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a382d07f.mp4?token=U4W-RZVawKuRzu2W-yBdnHTWeKSFTKqhZdxXQ06hgB63wUe-Teq3TUt-MYHioJvbbstzThhcoWuCuZLP_RFrifJ7E762hCQAwj5uzMyUB7uVUmwE5lvS7CpKp9fBl8DEB3IWN_h5C1MT4bKjd3Uxd2x8HcOPTB_SVwGX-A1XkSgK90-Ed8uHR4OF_X6FG3VuKpJUEYpVWz6gMDEO85de5ncvhgcm4VDlHVpiFUVp3nJeUwipnt9smF7zXgKqkCOlLpnHuDDUUetz-q6EQkOVViRhIo3ppBOJQOByCyILUwqHE3Xgig5gc4jNME2LPITy5FcybzMKBhNx4qOohF-kdqmgblDKYj7CbZMHhK8_UWg_u9cu6rCZKhddG7Eg9Fh_HGC1uZJ0NDHmE9y1GtmgUGmLeXvzU906fN_s0iw2jM2q940V5SEpkkK9zx3kwB97ebm-7sBJ5m7h2m07tZ6OkKmzWLxN0iVLqpcD7FvgDx3ioKuAcuElFzP039sNBmrNlQTMJMY4RTsrM_EWodVpYelIvb86z7ybNtlLEwvyANmUsxYBwOGwbLRJ1tbEjDikDlguhI_ghf8zkmHeTPzQHPKfMbmu5FWcuU624K-RKt20TVXIKZUN_koJchhsN4efJQ8JqEVc3WqKl1CVRiGLj4ELyPT7VmKob_3z8KCh-Eo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a382d07f.mp4?token=U4W-RZVawKuRzu2W-yBdnHTWeKSFTKqhZdxXQ06hgB63wUe-Teq3TUt-MYHioJvbbstzThhcoWuCuZLP_RFrifJ7E762hCQAwj5uzMyUB7uVUmwE5lvS7CpKp9fBl8DEB3IWN_h5C1MT4bKjd3Uxd2x8HcOPTB_SVwGX-A1XkSgK90-Ed8uHR4OF_X6FG3VuKpJUEYpVWz6gMDEO85de5ncvhgcm4VDlHVpiFUVp3nJeUwipnt9smF7zXgKqkCOlLpnHuDDUUetz-q6EQkOVViRhIo3ppBOJQOByCyILUwqHE3Xgig5gc4jNME2LPITy5FcybzMKBhNx4qOohF-kdqmgblDKYj7CbZMHhK8_UWg_u9cu6rCZKhddG7Eg9Fh_HGC1uZJ0NDHmE9y1GtmgUGmLeXvzU906fN_s0iw2jM2q940V5SEpkkK9zx3kwB97ebm-7sBJ5m7h2m07tZ6OkKmzWLxN0iVLqpcD7FvgDx3ioKuAcuElFzP039sNBmrNlQTMJMY4RTsrM_EWodVpYelIvb86z7ybNtlLEwvyANmUsxYBwOGwbLRJ1tbEjDikDlguhI_ghf8zkmHeTPzQHPKfMbmu5FWcuU624K-RKt20TVXIKZUN_koJchhsN4efJQ8JqEVc3WqKl1CVRiGLj4ELyPT7VmKob_3z8KCh-Eo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی: آمریکا درباره تایوان اشتباه کند، جنگ می‌شود
🔹
رئیس‌جمهور چین در دیدار با همتای آمریکایی خود در پکن در خصوص هرگونه تحرکات واشنگتن در خصوص تایوان هشدار داد و گفت که هر اشتباه آمریکا می‌تواند به تقابل آمریکا و چین منجر شود.
🔹
شی جین‌پینگ با تأکید بر این‌که…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/435531" target="_blank">📅 09:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPjsuMy4LqiZ4737-zkujXWWfhR40lKdDtHsjVfDy6comN_bpuaKpZhRtUBxcAEeBBTLdzm2d1ZEsD23bmUMUnIOmnKpYEp5PlMPFUNTUDrkCTTe1JoeQ12vJnpaRV1X5nm-4wrb3hjmv0ZATcD7gw72lxDHojwmCrr5wl-JBfr2WlmM-An-pkXHxmSRZ_rn3jX-JNf6NhQ-KRG3tlF-rfpUsZP65mSK6rGYzUW6fEG6IfGRd53Pw9Rd0VrwBC5CcR1zelQ84vWw02HxaIxb8WlhmadiH73X5AbmR6XokbH6FF37gAvqRhA2tBqww-yKKtgTr6tUBQajk-VNdAp3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عکس یادگاری وزرای خارجه بریکس در دهلی‌نو  @Farsna - Link</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/435530" target="_blank">📅 09:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435529">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664d5121ba.mp4?token=nmPxLfhZLOL_A7v-WNqfEkiDDgYt_XTwelK7_4R8GBqIrlYLJPrKNBFluIOmQLJbNmZ5rnNgTO_VcbH0-zvZjHSEfI6UXh_1UFQ5VEM05BP3c_P9ZmL8vAPV22zUWT9VPlJUcI8uuEMbJbRJmHzCekrXHUqgADJPyH3yRaRTrVvZgp-osvWTkbmeJ09PYzFRyq5Zpgya0jFA7ksMYzlp0VsXNElpdIzlXhKq4_9SPSpzdY_n2u8HXEvJfmZlMZMYZKqw_N_c-svQNtrIgZdpuX8-Dmx1TV5tsQG-56ZqbOwz_5jSZBRK1cTSymPXiuvmwdl5Hs_cNJdT2LyDnKaw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664d5121ba.mp4?token=nmPxLfhZLOL_A7v-WNqfEkiDDgYt_XTwelK7_4R8GBqIrlYLJPrKNBFluIOmQLJbNmZ5rnNgTO_VcbH0-zvZjHSEfI6UXh_1UFQ5VEM05BP3c_P9ZmL8vAPV22zUWT9VPlJUcI8uuEMbJbRJmHzCekrXHUqgADJPyH3yRaRTrVvZgp-osvWTkbmeJ09PYzFRyq5Zpgya0jFA7ksMYzlp0VsXNElpdIzlXhKq4_9SPSpzdY_n2u8HXEvJfmZlMZMYZKqw_N_c-svQNtrIgZdpuX8-Dmx1TV5tsQG-56ZqbOwz_5jSZBRK1cTSymPXiuvmwdl5Hs_cNJdT2LyDnKaw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار فاکس‌نیوز: ماشین ما در چین ۲ دقیقه در محل «توقف ممنوع» ایستاد و بلافاصله پیامک جریمهٔ ۴۰ دلاری برای راننده آمد
🔸
اینجا دوربین‌ها در هر لحظه نظاره‌گر هستند و همه‌جا حضور دارند.
@Farsna</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/farsna/435529" target="_blank">📅 09:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP0cNl6Tffn00Qw0teSkkJBeYLFauJtGEb-KeWNCLhAr14q-5Z5AUJc0TJcNhngLQSnnS1WYkyuCSFHW0YZMKTOIdkCLrOyPPuFSW6BnWGQX0ktSW857TYR7E3yE0uy2xANi8gjHKne1LkROGaiKHO2Mi8Vp8W8cHz67DBNxpteltT35AMHoiNw6wo96Mvm09n8ZkFuPe3kBJcO4LqGjmVdXi7JcLzHSFgEpbSElYOvazo4mb1o16EmxymwCFE_WZ83bhqFhqSI-6YDr7RyVnmLVatW-lAV9x7cmjXSJdgqGRYnS3DkKgBDU7CeAk07582CbpQS-QiWA5H2nWxQzsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران و پکن روی دور تند ارتباط موثر
🔹
رابطهٔ ایران و چین در سال‌های اخیر از یک همکاری صرفاً تجاری به سطح «مشارکت جامع راهبردی» ارتقا یافته است.
🔹
در شرایط پساتنش‌های اخیر، تهران و پکن با نگاهی متوازن و مبتنی بر احترام به منافع یکدیگر، تلاش می‌کنند مسیرهای اقتصادی را بازگشایی و حجم مبادلات را افزایش دهند.
🔹
یکی از مصادیق عینی این اراده، تحرکات قابل توجه در آبراه استراتژیک تنگه هرمز در روزهای گذشته است.
🔹
طی روزهای گذشته، داده‌های ردیابی دریایی نشان می‌دهد دست‌کم ۶ نفتکش و کشتی فله‌بر با مالکیت یا عملیاتی چین از تنگه هرمز عبور کرده‌اند.
🔹
براساس تحلیل داده‌های موسسه «کپلر»، از میان ۳۷ نفتکش حامل نفت خامی که طی ماه مارس تا اوایل آوریل ۲۰۲۶ از تنگه هرمز عبور کرده‌اند، ۳۰ فروند منشأ ایرانی داشته و تقریباً تمام آن‌هایی که مقصد اعلام کرده‌اند، راهی چین بوده‌اند.
🔹
ایران با تضمین ایمنی مسیر و اعطای تسهیلات ویژه به کشتی‌های چینی، نقش فعالی در حفظ جریان تجارت انرژی شرق آسیا ایفا کرده است.
🔹
این اقدام عملی، نشان‌دهنده اراده تهران برای تبدیل چالش‌های امنیتی به فرصتی برای تحکیم روابط اقتصادی با شریکی است که در شرایط تحریم نیز در کنار ایران بوده است.
🖼
اما چرا ایران چین را شریک قابل اعتماد می‌داند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/435528" target="_blank">📅 09:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYn6AokCBBqfh4JM_o_-xc6h70AmdrdIREBKMH5vllFCQPBMvbgwQbBOH9DWSN_iyvueVbWoyEcK38oePmoQj4PP0C96xvlu6HgFnZDqmVHsJV_sSfTKNshNpenxlpOcYMuC449glK2e8eAn-4EFbYytU9V-T3QCtgM_CJjs-qZqYgVbUj0t0cuBOYUrXk8MQQWvzSLec8hb1CeqosWvGmdtXglFx3sWTqLb7P-uA-CaSsoQEdz2nneoeUB2B7CogJm8jP9ce2y2iLHrgfvjnqFibUIX_i65hxzUttVy2NyQ6APreO9qd5eZqSBem_He4JJB4E6LdpvN2RYD6P12Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیباکلام ۳ ماه از انجام فعالیت رسانه‌ای منع شد
🔹
قوه‌قضائیه: هفتهٔ گذشته درپی مصاحبه صادق زیباکلام با یک خبرگزاری، دادستانی تهران علیه نامبرده و رسانهٔ منتشرکننده اظهارات او اعلام جرم کرد.
🔹
پس از تشکیل پروندهٔ قضایی برای نامبردگان، متهمان به مرجع قضایی مراجعه کردند و پس از دفاع، تفهیم اتهام شدند.
🔹
در نهایت با توجه به مستندات و تحقیقات صورت‌گرفته قرار جلب به دادرسی و کیفرخواست پرونده صادر شد.
🔹
همچنین قرار نظارت قضایی ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت ۳ ماه به صادق زیباکلام تفهیم و ابلاغ شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/435527" target="_blank">📅 09:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435526">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873e2d3fb9.mp4?token=Cm2b6JLL2zsFRLlPNtdjuCp8qeuivGiE8-EKQcKTPMud8oRbppWjPACzrhyTX4-KCrQg02KDjW8m0exC6aMWwVg00GGR33ed6cIRQw5cHbObofEwYe6tLVY7WV5FXXNFG6WNv767_sWMRWq4baVsed05IOjVEpZGGBHaCidaEgRT_Phs5-669HtpyJjM8u0PnqGEzhJG48cBvC-nmFdm7FhDNi6v0aYGc3kSCf-9oekEFZM2M1pyA9nl-txnooPzH7hz-p2cYoA2esadCjEouTyBbmIx_KMkmoFUhvYXp-SkTdnLn3A0qMTq2jt0oFEThKCmpO5mPYEzL4_zMfK3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873e2d3fb9.mp4?token=Cm2b6JLL2zsFRLlPNtdjuCp8qeuivGiE8-EKQcKTPMud8oRbppWjPACzrhyTX4-KCrQg02KDjW8m0exC6aMWwVg00GGR33ed6cIRQw5cHbObofEwYe6tLVY7WV5FXXNFG6WNv767_sWMRWq4baVsed05IOjVEpZGGBHaCidaEgRT_Phs5-669HtpyJjM8u0PnqGEzhJG48cBvC-nmFdm7FhDNi6v0aYGc3kSCf-9oekEFZM2M1pyA9nl-txnooPzH7hz-p2cYoA2esadCjEouTyBbmIx_KMkmoFUhvYXp-SkTdnLn3A0qMTq2jt0oFEThKCmpO5mPYEzL4_zMfK3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی: آمریکا درباره تایوان اشتباه کند، جنگ می‌شود
🔹
رئیس‌جمهور چین در دیدار با همتای آمریکایی خود در پکن در خصوص هرگونه تحرکات واشنگتن در خصوص تایوان هشدار داد و گفت که هر اشتباه آمریکا می‌تواند به تقابل آمریکا و چین منجر شود.
🔹
شی جین‌پینگ با تأکید بر این‌که…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/435526" target="_blank">📅 09:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435525">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990f2cdf7b.mp4?token=ujcFAyRuu2i-T1tKW-wlVCEWo8ndV1RYVp9BpxrY-sPG_HVVDYNUUpVDIOTEqRPZutxlvPEv84Mo0JsVdsHTQNTnN9eINiahRZ_yvGDl0jw47OqnGbElK8CLBYa_j1bBFzIJsh_VazNlHy9WN1lPXv6FljzMRByHeI4FQJkHevsmGsU5MggTEAZ4zvuKeElxyRhdhW_9miih1KLMoQYp_-6ome0qp2s35oVUdnj1ZVJgBw-qqt-VLqQoxK5oX8fdx4frCTjCdSRyh8E3Uf-mPDG082bWyVKZSOaInL71Ju33jaJzvdw84STQpou3nrHzQ5AVSVLZ1s5nrqdqE41RRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990f2cdf7b.mp4?token=ujcFAyRuu2i-T1tKW-wlVCEWo8ndV1RYVp9BpxrY-sPG_HVVDYNUUpVDIOTEqRPZutxlvPEv84Mo0JsVdsHTQNTnN9eINiahRZ_yvGDl0jw47OqnGbElK8CLBYa_j1bBFzIJsh_VazNlHy9WN1lPXv6FljzMRByHeI4FQJkHevsmGsU5MggTEAZ4zvuKeElxyRhdhW_9miih1KLMoQYp_-6ome0qp2s35oVUdnj1ZVJgBw-qqt-VLqQoxK5oX8fdx4frCTjCdSRyh8E3Uf-mPDG082bWyVKZSOaInL71Ju33jaJzvdw84STQpou3nrHzQ5AVSVLZ1s5nrqdqE41RRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ورود عراقچی به محل اجلاس وزرای خارجۀ کشورهای عضو بریکس با استقبال وزیر خارجۀ هند   @Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/435525" target="_blank">📅 09:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e52d642c7.mp4?token=ADPykdYhC23CofXWylDnitA6NZjVJ8eILOCosbOYPTyM7rA6LPQGr1iWB1sSoNyoazfHA2HLOcjecLvyoux6OgaKA-mxl-oBhnwi5F_20dRvoOxJDN1Kd74aE7C7ihKp8-i-wVqDK0rPZORYG-wO5EgagQ69pj3dU96sJz7WrJKZqULRmucbDcnZEhmq9Rlb1Aw5gIr-ffL5cZ3BAYNXKgSQZJLYKO93ejVbmHCW5n6DJGTnmiPsUEGHgAi4Ejn5u-Le34L5Yz3vZSqQJ-mx30Czg9NsIsOahuac-h3DAMUVLyq5OBuzdpEoIxWz-Bp2Ddxh_YzNy_AyU4a2nKa0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e52d642c7.mp4?token=ADPykdYhC23CofXWylDnitA6NZjVJ8eILOCosbOYPTyM7rA6LPQGr1iWB1sSoNyoazfHA2HLOcjecLvyoux6OgaKA-mxl-oBhnwi5F_20dRvoOxJDN1Kd74aE7C7ihKp8-i-wVqDK0rPZORYG-wO5EgagQ69pj3dU96sJz7WrJKZqULRmucbDcnZEhmq9Rlb1Aw5gIr-ffL5cZ3BAYNXKgSQZJLYKO93ejVbmHCW5n6DJGTnmiPsUEGHgAi4Ejn5u-Le34L5Yz3vZSqQJ-mx30Czg9NsIsOahuac-h3DAMUVLyq5OBuzdpEoIxWz-Bp2Ddxh_YzNy_AyU4a2nKa0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در استان‌های خراسان‌شمالی و رضوی، گلستان و سمنان هشدار سطح نارنجی صادر شده.
@Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/435524" target="_blank">📅 08:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn2Lp3wJ_vSxvXOhxoSBbjJEZvF3okB7yMD5TrUp8oLQvSI1_yVCj5gr4OKvVWIBpII9jZxj5qmuOMfGGCtGvJys_8DJuV66w3Mmoq7O63MZkzNvSSJfpvppMf2t_eev-kLdZzWlIi-L9K6L2s5Blx0RDtjMhb34-nhTTAHTbWKoUyEVh_defSiUjgKVuX_Y39MJaVTb8uXDT0eCgI6Fz4UrdN4ey-2ztuOMWe12l85zbgonnV2XhC8TnAY-6wdnAd7om4PRJaCjL1PXGS2mIIzjAQOPXGXLMyygBADzMjrdXWL5n4Og9IKaOmLM3MkeHiiQOQCkGbhxnZo_1SJ2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شی: آمریکا درباره تایوان اشتباه کند، جنگ می‌شود
🔹
رئیس‌جمهور چین در دیدار با همتای آمریکایی خود در پکن در خصوص هرگونه تحرکات واشنگتن در خصوص تایوان هشدار داد و گفت که هر اشتباه آمریکا می‌تواند به تقابل آمریکا و چین منجر شود.
🔹
شی جین‌پینگ با تأکید بر این‌که «استقلال تایوان با صلح در تایوان سازگاری ندارد»، ادامه داد «برخورد درست با مسئله تایوان به حفظ روابط دوجانبه بین چین و ایالات متحده کمک می‌کند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/435523" target="_blank">📅 08:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/489ae3154a.mp4?token=vM9HgHP2cGnZz2PE01S9W1Pzrj9Jyba57kEtTMQzjpbVDIGiIAtz4QkgbwNf-buuaV2YTu81wNW6j1fwar75Sgr1qJvVsS5AVih-T4OLtoodDdaNPqbWJe8_PmxNvHDevqi-CXgbekI43cFpbEDl6D2QQ640qGO58GqtCS3c4WduGpDa7GUXAfH8n-oohUXBOWu9jwERKzamKhRe3zOreFkGZlZtiwO7U_QdOjKtfV65jq9_yEuNOhxW8DKbK7a6YotFE0KLOWUpafN5jWFDgNnzFpJ6_ESdU5rBSsLpBd9k2z160Hq1ib0RvGNlUTJ3CkR-Q6CEwh4F3v8EdJ09pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/489ae3154a.mp4?token=vM9HgHP2cGnZz2PE01S9W1Pzrj9Jyba57kEtTMQzjpbVDIGiIAtz4QkgbwNf-buuaV2YTu81wNW6j1fwar75Sgr1qJvVsS5AVih-T4OLtoodDdaNPqbWJe8_PmxNvHDevqi-CXgbekI43cFpbEDl6D2QQ640qGO58GqtCS3c4WduGpDa7GUXAfH8n-oohUXBOWu9jwERKzamKhRe3zOreFkGZlZtiwO7U_QdOjKtfV65jq9_yEuNOhxW8DKbK7a6YotFE0KLOWUpafN5jWFDgNnzFpJ6_ESdU5rBSsLpBd9k2z160Hq1ib0RvGNlUTJ3CkR-Q6CEwh4F3v8EdJ09pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ به چین رسید  @Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/435522" target="_blank">📅 08:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muocio0G2KKhBqfT-ovg9BXs29ow37V0yHWIaX4fR8Uid2b34gOUJR4QeH--fwg0BbCp8CuZ8Fbj2VWzeBG6m_RpHUdQ5B-8KjyyRMo-wcsW01xkzlZ9H1Zf7uxWEoeet3RJi7z91e9mKKH6VQcPYLAyJwjaYwyO469cY4VU7lCpvopWgWddEtOHI6zP4pCrwG5CQO7WmkC7zhS7LuCd6Quc3LvIBdr6fiEZBFBdhqfW_HQBjAD8nqWR_uyMDj7szQnp2qXIpM3P_ikebkVtNKXF5jPxUwycobKYDuamdrQsQJUkqBpTODV-uV3wpP4lsq5o_5PFHWWimYFQlUCA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ورود عراقچی به محل اجلاس وزرای خارجۀ کشورهای عضو بریکس با استقبال وزیر خارجۀ هند
@Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/435521" target="_blank">📅 08:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed12c1373c.mp4?token=Lv0dZHz_Im94yufucBiswX3qJhoA9AkQfXzgf53Z6soFGV1oww2SAYkS9TQrkRPdLeMKMb1xuCyQ2X50hYTrVVBHbm5lxNJ_VGAwYWpAzbraG2174CbmADjiWALUt8zhh4qEMHIKyAptV5pB7833rm41N2botqRZmlX0m41V5Ec7v9YkT1_PciflMigl9sYiIKuWT1_YUzPwF6I_-bysF4kIp0nTvw1SNIcW8n9mYf_7vT1Ah6qeDAgSoXE5Oj-NHMdFV59XDIRg1qiqrsHJPf4PVSbZVkcbuBsi-OG5Pwq4WfApyNtzOAXxBgBfbEcxY-AXliAuInoi9soLOgVqtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed12c1373c.mp4?token=Lv0dZHz_Im94yufucBiswX3qJhoA9AkQfXzgf53Z6soFGV1oww2SAYkS9TQrkRPdLeMKMb1xuCyQ2X50hYTrVVBHbm5lxNJ_VGAwYWpAzbraG2174CbmADjiWALUt8zhh4qEMHIKyAptV5pB7833rm41N2botqRZmlX0m41V5Ec7v9YkT1_PciflMigl9sYiIKuWT1_YUzPwF6I_-bysF4kIp0nTvw1SNIcW8n9mYf_7vT1Ah6qeDAgSoXE5Oj-NHMdFV59XDIRg1qiqrsHJPf4PVSbZVkcbuBsi-OG5Pwq4WfApyNtzOAXxBgBfbEcxY-AXliAuInoi9soLOgVqtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله نوری‌همدانی با صدور فتوایی، پرداخت وجوهات شرعی مقلدان «رهبر شهید» به رهبر معظم انقلاب را مجاز اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/435520" target="_blank">📅 08:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آخرین وضعیت نحوۀ برگزاری امتحانات دورۀ متوسطۀ شهر تهران
🔹
آموزش‌وپرورش تهران از پیش‌بینی دو سناریو برای نحوۀ برگزاری امتحانات پایه‌های هفتم تا دهم خبر داد.
🔸
سناریوی نخست: در صورت تداوم شرایط فعلی، احتمالا امتحانات داخلی دانش‌آموزان پایه‌های هفتم، هشتم، نهم…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435519" target="_blank">📅 07:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFiuTv-WG-z4CCiEk80z-DlxRZ5q8efxh-Yww3Rc2h2rcKnW3nbVD9VbfnK0MGWWprunBBLGRODawvsUIZWpziG6P9510_WK7g4PAI97_oSWxA--r6ev1y6twPLPUZk-VlEf4ibmT9K1f_ISYfaFLflAi8Ferk4ZzdFAwL_jFsIwG9o26aXoEHMMu60jIEhQgETvDTDQseYtQUjGL9fohDk2jabZY7Pk4OOY9MfhLozczMgD4JDyt9mODKKldOUQNd2hH0Lnv-1gz87ghL8Bwciv8akNpuy8vhRt3XQ8eKx76oHEDMawuBIixSzkLL8dDBHiKho_Seq9SVxqk7TC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نحوۀ برگزاری امتحانات دورۀ متوسطۀ شهر تهران
🔹
آموزش‌وپرورش تهران از پیش‌بینی دو سناریو برای نحوۀ برگزاری امتحانات پایه‌های هفتم تا دهم خبر داد.
🔸
سناریوی نخست: در صورت تداوم شرایط فعلی، احتمالا امتحانات داخلی دانش‌آموزان پایه‌های هفتم، هشتم، نهم و دهم از تاریخ ۹ خردادماه به صورت حضوری و مدرسه‌ای, با رعایت اصل پراکندگی (کلاس به کلاس) برگزار خواهد شد.
🔸
سناریوی دوم: در صورت ناپایدار شدن شرایط و بروز محدودیت‌های احتمالی، امتحانات داخلی این پایه‌ها به صورت غیرحضوری برگزار شود.
🔹
این موضوع پس از بررسی‌های دقیق‌تر و اخذ مجوزهای لازم، ظرف روزهای آینده  به مدارس ابلاغ خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/435517" target="_blank">📅 07:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJEBOhN2WjgDoEhIa9fp_OkGdADDD7aycegVybdPO0Y6O8NnWCSAd-tCxpNXcurmq1MwEMbnk9OpFNR3GbwOFHy6dgdPvyyajHW85m-YJHHkgR8EnrVC1cwPdclkAV4rX1qJvNcICWp4_i5RdYyWb7kijt_Ic86UReJRH3GEGkHGadlQu5pbA02VFnPuJiMDZTwX8uq9SMm_4iUphlwZZiFfuCs7BRMZStSzzgrVOLj_ttj4zDlaRkgX4R0uB8eOltHN-s0Hl4hYUkNdpY_N9sRzmFQT8eH-vURdTmDaUsI5Cv9S3eROFqewG6MqPPyW9dCv-L3jtbwWH6_v9dvTSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهمیۀ سوخت کشاورزان چگونه تعیین می‌شود؟
🔹
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: در فرآیند تعیین سهمیۀ سوخت ماشین‌آلات کشاورزی، سه شاخص اصلی سطح زیرکشت اعلامی، میزان ساعات مورد نیاز برای عملیات زراعی هر محصول و ضریب مصرف سوخت ماشین‌آلات مبنای محاسبه قرار می‌گیرد.
🔸
سهمیۀ سوخت ماشین‌آلات کشاورزی در قالب سال زراعی، از ابتدای مهر هر سال تا پایان شهریور سال بعد تعیین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/435516" target="_blank">📅 07:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ارائه کارنامۀ دبستانی‌ها از هفتۀ سوم خرداد
🔹
درحالی که سال‌های قبل کارنامۀ دانش‌آموزان ابتدایی در نیمۀ اول خرداد داده می‌شد و بعد از آن ثبت‌نام دانش‌آموزان در مدارس انجام می‌گرفت، امسال با توجه افزایش یک هفته‌ای زمان آموزش، کارنامه هم به نیمه دوم خرداد موکول می‌شود.
🔹
به گفتۀ معاون آموزش ابتدایی آموزش‌وپرورش، بعد از ارائۀ کارنامه و بررسی بازخوردهای احتمالی خانواده‌ها، نمرۀ نهایی تا پایان خردادماه ثبت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/435515" target="_blank">📅 06:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqxJQNUCS7VQmMjzNeUJVFYwi1QXksZF1UFG_OqOwKUMBxeJCcaEmbkJw4V3o12J9bFXWyHnuWbjKJBKDP0dvrjvIu63KE9b3rlyCrLEHJI2d1sxJst4HTuhD-wnt34opAz2cI4L7otKAo8tlGM1ziTxBFXKHc75KctGgedqhQBZAytPziP4SVtsBDsg4rhoiHQ5pqyizksuJJURY-HN7vW_k8wVuH2qRYvWw7Zp2LZqZvpnWuA_Hphp10hDVhEPcqxlGYxDL4YcqMr4qoZ7ktf-BupI3_5qAFBGeqi5610KmnheIXiYydFbM5Y4f9dyFt5q0JsQFIJ6tPnSFoi5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح جدید دولت برای حمایت از تازه ازدواج‌ها
🔹
مدیرکل توسعۀ اجتماعی وزارت جوانان از تشکیل کانون‌های ازدواج آسان خبر داد و گفت: در این طرح که از هفتۀ ازدواج کلید می‌خورد، خدماتی نظیر تالار عقد رایگان و تسهیلات ویژۀ خرید جهیزیه از طریق کانون‌های استانی در اختیار زوج‌های جوان قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/435514" target="_blank">📅 06:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آموزش‌و‌پرورش: احتمال دایر بودن کلاس‌ها در پنج‌شنبه، جمعه ۷ و ۸ خرداد
🔹
معاون آموزش متوسطۀ آموزش‌وپرورش: اگر دبیری احساس کند نیاز به رفع اشکال برای دانش‌آموزان وجود دارد، روزهای پنج‌شنبه و جمعه ٧ و ٨ خرداد، کلاس‌ها برگزار است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/435513" target="_blank">📅 05:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4sLaXtLffcPjOgxxqxr-A4Z7RV4F5VfxrZVaBbnJclZy8taM0mtCJD19c24MatG2CjsKWI0MZRrF3sM9UM7LPAuQhumwFRjQXBVm8vM9yvFQxHbERmvgH8z8_Ry-wXuM8XoFgxVPMr2Kf1g2JO_o0FdcfSDQZXoq-5fPaxZrP4RXHY4ApKMhPawMb9lvI3x6_fj4bN9pOIp0o9VBAHrSIZjI_ax4JDnVbMn79RiMFmZMhtJAzEqCFzc9W6G74KgKEO-bfB8JBe99slzEX8nMrxA0ddwGKTQqWKFCx4RVqjyuZbR7-yn1Cc-D_sDFknAZJLqQq_L_zI-nN8lqnE6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناوگان اورژانس کشور جان می‌گیرد
🔹
معاون وزیر بهداشت: در سال جاری، ۱۰ هزار و ۵۰۰ میلیارد تومان به حوزۀ اورژانس کشور اختصاص‌یافت تا فرسودگی ناوگان و مشکلات این حوزه مرتفع شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/435512" target="_blank">📅 05:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGfnWyA3rRHMutOi1h9j78c2g2fT2OlmXDVkoiuIENDJOoYsNGpZ3WvcItNY4m2-OmoEon54L7jO2LoHT7iRJ5aOPHRGwolmHpMduhftHh8ZpUqrIz2ArrFGqOKbs-IRPAa9nM3kcTN7BryHHzeVU-jQqNlREUqQGyQrUBiJPPsJYjsbBVBS4n3oMGAm6J5wSvuhKC-_HJd9_0MCf0HrCQcPiVjemz0sac8RCeFi3bB1KWyfR2jGcYwgjoV9nWnCkvEBAuPcwBlZgRwa7XJ3NDt2AOS-XUZAN93DNin0w0aoPBU3rTBbANNkPIBN5Yq91lPUNp2hxgao34SZOx7HZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات آمریکایی در واکنش به درخواست ترامپ از ایران: خنده‌آور است! ایرانی‌ها با بمب تسلیم نمی‌شوند
🔹
یک دیپلمات اسبق آمریکا که گفته می‌شود سابقۀ مذاکره با ایران را دارد درخواست ترامپ در خصوص «تسلیم ایران» را خنده‌آور توصیف کرد.
🔹
رایان کراکر، سفیر اسبق آمریکا در منطقه که مسئولیت انجام چندین دور مذاکره با ایران را در کارنامه‌اش دارد گفته، ایرانی‌ها آدم‌های به شدت سرسختی هستند و تقریباً همه‌شان سابقۀ حضور در جنگ ایران و عراق را داشته‌اند.
🔹
خنده‌دار است که کسی تصور کند می‌توان ایرانی‌ها را با بمباران به تسلیم وادار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435511" target="_blank">📅 04:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8bnYBqOmLlvtQSFMzLCg00DBHjnTRpI83JHM79OdAZ1VIfMrwSK8hNby08BAT0nKucTaYP0e7y2Xt9acBJznFdns7cpkBnG2OwVqFavlA7_3rJ_9gv7mSK9k0U5DYMpNUqn1BsZFuGTJmv7pc1ZzFl1mCPmu2KvlRxq1I0i3jbuT99-ASi_2f5W4DhieJzo3WrRWKdSv2Vd7fBDDeChEN-CekzlNLASZcOxUL6Z69KGGrtPp7qFK8C2ytAB_Qm1jpIawAY_eLzhs4Ix7ankboMTZ6bKZk6cQKBcYuMfrKKQ0G_gNrHfixdkiWn-t7hDONvcNwiBye1QSzlUOlmo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در فکر تسهیل خرید نفت ایران توسط دو بانک چینی
🔹
خبرگزاری «رویترز» بامداد پنجشنبه به نقل از منابع مطلع ادعا کرد: «انتظار می‌رود وزیر خزانه‌داری آمریکا موضوع تسهیل خرید نفت ایران توسط دو بانک چینی را مطرح کند».
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435510" target="_blank">📅 04:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
غوغای حماسی سرخسی‌ها در میدان اقتدار
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/435509" target="_blank">📅 04:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZADKz5ClIW2S4QvNr0PlvAyHbpADK5GG8mPMOmkjC7S8f61r4HkEmw0gyFvwYYJJdmcMDIorjPNjAGOTMpFv1hz2p91nNY5h3_rxswc7fXzh7T2sVVBKXjl8KXcXyN6I03aXdFeWxr6cu4Qti8daJaVdIwrCMTq8QIAePM8jZGdlczrhOhYMIx-GprOZq9aduT8GZINyfC4AwSJFkchez1-uLJ54_tvXhLGIBz9RKV_09I9HVsNsDGczx2TAMFeTlMt6aPzaDWXUBlzxqNi49OcIu1WCoB3CGMamcvpGeiX3tbgpYqbUo5sd0Og-ddCmjJJKALNjjMvmtrI5Y0hWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقتصاددان آمریکایی: ۳ ماه تا سقوط اقتصادی فاصله داریم
🔹
اقتصاد آمریکا که بارها از خود توانایی چشمگیری در برابر بحران‌های متوالی نشان داده، این روزها زیر بمباران صدمات متعدد در حال فرسایش است.
🔹
از جنگ تجاری با چین گرفته تا افزایش قیمت انرژی و تنش‌های ژئوپلیتیکی ناشی از جنگ با ایران؛ حالا کارشناسان اقتصادی هشدار می‌دهند که انباشت این شوک‌ها، بزرگترین اقتصاد جهان را به نقطۀ شکست نزدیک کرده است.
🔹
مارک زاندی، اقتصاددان ارشد مؤسسۀ مودیز معتقد است اقتصاد آمریکا پس از «تحمل شوک‌های متعدد بدون فروپاشی»، اکنون «در وضعیت بسیار شکننده‌ای» قرار گرفته است.
🔹
او می‌گوید، اگر جنگ زود تمام شود، احتمالاً می‌توانیم از این بحران عبور کنیم. اما اگر دو یا سه ماه دیگر ادامه پیدا کند، می‌ترسم نتوانیم از پس آن بربیاییم.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435508" target="_blank">📅 04:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3AEvY54c6VnT531vERJLGHXvYmPAA6JEGftSduzgx_8p1bSPwXsk9c43u3Dy1bgecYqxiKd62fI7z4Hjduihr6GP1JOOevDzKt4HQMJKCAuO1hHAHeQx9sKZy_UcfUjXt6Jfc7va0AKnBkz2JqqHI1bl6lwceKTowKGjq71O0OuZf7I8RiS2K5ru2jX4x318wEuDCbdax4TTfZYllpdgGRf-vajN7zlg29gh6mj7J7hdB8mpmHEZz-ZRrXzdwPCwoxy8qf1kh9Vml1dnuIVjoOOkWiMw_4L_nYxXVg24vz4HQaAzwNcPiM8nYTZEZRjPdXFknJDOReuuaeRVXtFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط و نشان اسپانیا برای شبکه‌های اجتماعی
🔹
دولت اسپانیا اعلام کرده که این کشور قصد دارد قوانین تازه‌ای برای شفاف‌سازی الگوریتم‌های شبکه‌های اجتماعی، محدود کردن سیستم‌های پرریسک هوش مصنوعی و افزایش حفاظت از کودکان در فضای آنلاین اجرا کند.
🔹
همچنین وزیر تحول دیجیتال اسپانیا گفته که طرح ممنوعیت استفاده نوجوانان از شبکه‌های اجتماعی را دنبال می‌کند و هم‌زمان به‌دنبال تصویب قوانینی است که مدیران پلتفرم‌ها را در قبال انتشار محتوای نفرت‌پراکن مسئول بداند.
🔹
این موضع‌گیری در شرایطی مطرح شده که اتحادیه اروپا نیز طی ماه‌های اخیر فشار بر شرکت‌های فناوری را افزایش داده و دربارۀ طراحی‌های «اعتیادآور» شبکه‌های اجتماعی و خطرات هوش مصنوعی برای کودکان هشدار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435507" target="_blank">📅 03:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🎥
دختر ایرانی که در چین، پایگاه بسیج زده!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/435506" target="_blank">📅 03:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsT9uVp933U1FyTkmd1gGW5RANM4EFdyqVFFvKDuvpOehjUF53Rfd8cYRHfKYVfThi_4QvhcXLBbf5zESYiZsI2D0jV4bBsQLigTIYzJ7gN4E2yzcvPyFh6lxpd4AOoXQ7EhQr5RaL1XYGPhmIjHPSJ1QSdRCOPYJTVAAFbE4wfEQSPmuNqmYxl0u74ENciaENtOixeLR1fMllPxwUeWMXgbxXSZzCDKv-HsOosZnxbZYO50EJosnEWALBAKcfr4QNbEpGuZGS_QfwnJb-ewry3lTkTM-VnKZqerbNsO2CO6r-bchmE7QIc_DbqeqPaJfVhLqkIwaNPWPHBWJJ5iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم آمریکا تبدیل به پوستر استخدام شد
🔹
استارت‌آپ چینی «مایزارویژن» که در حوزۀ تحلیل تصاویر ماهواره‌ای و اطلاعات متن‌باز فعالیت می‌کند، پس از قرار گرفتن در فهرست تحریم‌های آمریکا به‌دلیل انتشار تصاویر و تحلیل‌هایی از تحرکات نظامی آمریکا در غرب آسیا، واکنشی متفاوت نشان داد.
🔹
این مجموعه طی ماه‌های گذشته چندین گزارش و تصویر از تحرکات نظامی آمریکا در جنگ علیه ایران منتشر کرده بود. پس به‌جای عقب‌نشینی، تصویر اطلاعیۀ رسمی تحریم واشنگتن را کنار آگهی استخدام خود منتشر کرد؛ اقدامی که توجه رسانه‌ها را جلب کرده است.
🔹
این شرکت در پیام منتشرشده خود اعلام کرد فشارهای خارجی مانع ادامۀ مسیرش نخواهد شد و از افرادی که توانایی کار در پروژه‌های فنی پیچیده و شرایط پرفشار را دارند دعوت کرد تا به تیم آن بپیوندند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/farsna/435505" target="_blank">📅 03:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پلیس راهور: اگر در ایام جنگ کارت خودرویتان را‌ تحویل نگرفتید، دوباره ارسال می‌کنیم
🔹
در جریان جنگ تحمیلی رمضان، برخی شهروندان محل سکونت خود را ترک کرده و موفق به دریافت کارت خودروی خود نشدند.
🔹
حالا رئیس مرکز شماره‌گذاری پلیس راهور اعلام کرده که کارت خودروها، دوباره و در بازۀ زمانی ۱ تا ۱۵ خردادماه به نشانی ثبت شدۀ شهروندان ارسال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/435504" target="_blank">📅 02:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
عهد دوبارۀ کرمانی‌ها در هفتادوچهارمین شب اقتدار
@Farsna</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/farsna/435503" target="_blank">📅 02:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKE6yryfo1fuadeDn95-eiYBffZbZGiq22NzB68JUJiOGXGQcJjx54CQmGgDKSBQx0-L8BSqAGkDiywL_iQPLM7PNJthjyJUK601GE4K6nXzDhYM9F7otstpS6feGn1TWoPdFjDgYIbLMKy0ZNrMPhpxIDFf1jLCJrHx0s3CZSmDwpZj9E_YcQhmyhxcH1ghrfrZ2PS4mAwAbL_SPuoymRLeH1V2eblYtlLI0yQwLnmXC0cXbA4acrgeRQo5TYnWCHrGNYJAZomlFayWxjxZA32XrcBUDvsTDawWP7UoqmYuFdqLs-WwvMG4lcpEBxxzu-r-9j3RacJl5wuqs29nUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: چین نقش فعال‌تری در موضوع ایران ایفا کند
🔹
وزیر خارجۀ آمریکا: هیأت آمریکایی از چین می‌خواهد تا از نفوذ خود برای کمک به حل بحران در غرب آسیا و تنگۀ هرمز استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/435502" target="_blank">📅 02:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sf0s6XZAuEGsgFC2PYrB_2IGWmKSiP6o1HQxfOBOGvxmVxLPm9Ss64zOlvMUVSLLBLSn2v6-uBv30TDOFVJAbPKpm5QQnNgWYY2GtD_CG5baa-znNH3lPFjJJder70y6BidgGXbldONccJlhFKhJVUf6towH0SnlGwPZPp51mNXhO_8JLuvoqKscQRAe5iwgLOhUsH4j9Vd-lDJD-ks9GeH_6kkAg7i8AQPFdOhiCQMDSYNPcpuFUjesFlIHMQ36qUmEHYCcFoV99UuszFTnUPjPW9nkqxyLSd5_R6WadZnykTytTzjPO4O4QUGXeMasrqVZDt7PYH_BZceHV_5CUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KysFwEw3Dl-JkEws5xF8toknlcPmhDRmFcIIva0NmHp3V-yGPFVDfHauWMObh50mIX3PxlLR8MPJRrkC8rry5jp46sgI8x7nQml2BOT7-6C3toWmUDb_7uuneNAb83OefzshYgs6ZT86YvFkvK67gYpDRdEvu-S6urQ6T9FwpburleMioBao1cL6KmqvosQx3Ptdax7TVrfLVcB9qd-QFBJ1MoAPlYU994rqmmYa5BRwlyT7cqu4bTCMtYdTKD0wS28C_jeaPpjPi_ZC2fdq4Whfu7-TPUOuz6c1bI9C-Za2n_EUG1b9XrTcketT-01yxrWbnJlfbIdNx1BBKFY1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbFd5dEvkzVj0eBPf7WQzkNCD2idRaAgZviglYBVJMRrYXQsuJbTUzZZSl8hDXROcN30BrE9hTL3NkrfUw6Z-cieowCBSKUiUjHQO7DToLr2a1JDncsycHMh0MHbO6kyw3Y-ap5dFd_61rRYqKZ6Y6rOroDoeB1kJyrsrgLNGgsYcHvK_mXt7ShSWXaQYLPXlwZxNDycMOJjuG_xGrUTagRkWngDliCT56A65bSjllb789DlzomlftRmfFId2Aa-l77qnHfzLkkhvEiAeAgE16upkoVyGl1_rAwkXA7rSWQBxneKnw1Z9gu4N8eQ09Yi49teGTiFrJKzNO1_ppNDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qICNsO_IePSaWZZhUiSSAXBi8QKIw_OCBhcxpre-pYDffcMPQ1pX00-yEbp1wdw6LKThE959vZdrNeC-3OG4o3AQUDT11u2hsVwEfDRZ92mKuuS0Mn4YKLiIOw_0tOs2QEksalrL5HBXN8Uk-Nssekik7xQNh4o2NlOkaOsWxNOc7a9C3TAIw7VPsI9ArXzq3nWSNW58QQjr4MoArdj2TipD5DmKIs8kuR2nLx2SfqieG3lc5citn09RUSt9zXKcTx-Exx_acHipzL8bcARl88kAyMlIWRAtsZ4bubaIFWCJX9kvCyXi2FpDxEMs01LIMxicdKrom9f0J4jeTkhyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST8BPUTI0J0qL_0tsNU_eFJCdEpaVlPATb6kwGQocIyZwrtieba86kez3Bv8kR3nr6p6FdV1KLZexEZBJeOXzw4gJ_RCX12j6VIySdpiy3HEDu8teNFObVEDUO9M0xfc62zO01GN97xJ54dogRdz-B9Nd2ZHe4seiPd-_X2ia1f92ihNJBAKyc7r08VQUf4I6LgYsfkaIrKK2Ar4DpOi6qflIdaZU9uJ3KHWC-Kjka0sT96v4CwyRGOXFAvKmlTSco8R9DiuGXurtqbyVmPkIoGJDLX8NlBEwJyGgJJLYs4CKZWbX6nkYpepJY2eyUTFdjBPKhA6i11NjyVzE7mbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRJnn9FzbI-IkvFi6ZjV81RYDDJuls8GWRqKw6y_sPG3vAbveCcAp8fbtMn4zd9DdzkuQRfbg8NOuc8nI8tTSHFXxUDQq-gDWUL0RU4njuQgksxZmKbsAyuFeqXkA2genaK4EM-sghbBI-CZQVTfuLkrQdy6U0D_RuES48K22rv9UW0m6J9xBw94qgDGap2ZYsgGigGo99aZtwxzIf9uwKwt5Lv8zbD-0RvagYe2YZAXySqoHvMeYoKSNHEy-k0zQI_6hSykkqmb-wmFt3AukGMY5QSwcUaF8V50AJzLDeCVB0QZkNf0xoT_EXCFZYGheYdZho0JyeFDKoPX_RFFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3Gux31W1Jmsy0jyX8MW7eQlODrqby0OAViA_kVhPc3p-8Mgdsa2lrfuyYm7DtcBw49f07SN3LSFOl4LZE_jcP6K89q0txCOYPlhm1MOFpvUqu_efld989bsX3k8AN-ZKz2gA0lIRegAnANPanPqapsI5c5ApKIkJ41zed5Z6BjvSyE-Kl7WacL8RU_-tEyqN_MX85z91C4GHH0jrhLgFhsWZjEunY1L1LWnOu2gUtgFoD_Ucl2gEvJTQz_-oqWhJFdn-7nmLNiWlH1q413M0RAdLR_I6S-Nb7HK_--yPNAKk_jljsf4O3AjUINCAaFTv4fgrPBUzzOSTJALR8-4qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقۀ تیم ملی فوتبال به جام جهانی ۲۰۲۶ آمریکا، در میدان انقلاب
عکاس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/435495" target="_blank">📅 02:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sggJu0l9Jjw3oCAXz-ULr19X4qpAf1TFt0hQmflrMG-XErK1k_R96Z4KhWEP9NDIrDoirt5WGKc9K9Fi02ZJS7D0tQKmw63qRS-2yRGpYzEf9VDOOxcGxkixLEvof7lItFXtcgv_eN6n6TrwUzm8u4kr_2IMYyJX9tGB_UC_7MjwrJInObIAB5ml0KuuSBLAnBwBBo9HwP9MK_tOui0D6bntge33O73mXqeR-GQNFucg2qLqPRC2tT7WTzMXOT77YBen4A5u02hwm_SAkYlGmwrWy6bcYRS_2zG-Apj1a9d--Z6X1npbACYCP-uD0BZbHwxwJLgwJmPqB2T62t80nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرانی که ترامپ پنهان می‌کند
🔹
ترامپ می‌گوید عجله‌ای در مورد مشخص شدن مذاکره با ایران ندارد. اما آمارها دیروز فاش کرد که آمریکا بزرگ‌ترین آزادسازی هفتگی ذخایر راهبردی نفت خود را هفتۀ پیش انجام داده؛ آزادسازی از محل ذخایری که ترامپ همیشه بایدن را به خاطر این اقدام در جنگ اوکراین نقد می‌کرد.
🔹
ذخایر راهبردی کشورها به ویژه آمریکا با هدف خاموش کردن بحران‌های نفتی شکل گرفتند اما حالا کارشناسان می‌گویند که این ذخایر دیگر کارایی ندارند و وارد مرحلۀ «تنش عملیاتی» ذخایر شده‌ایم؛ حتی مدیرعامل آرامکو هم می‌گوید، تعادل بازار نفت با باز شدن همین امروز تنگۀ هرمز چند ماه زمان می‌خواهد، چه برسد به چند هفته بیشتر، که یک سال دیگر هم باید صبر کرد.
🔹
با این حال وزیر خزانه‌داری آمریکا هنوز در مصاحبه‌هایش می‌گوید، عرضه را کنترل کرده و اهرم‌های زیادی برای کنترل بازار نفت دارند. اما مدیرعامل شورون، یکی از بزرگ‌ترین شرکت نفتی آمریکا معتقد است که به لحظۀ کمبود نفت در جهان نزدیک می‌شویم و آمریکا توانایی جبران آن را ندارد.
🔹
تحلیلگران اندیشکده بروکینگز نیز معتقدند که بازار انرژی جهانی به‌شدت به ثبات غرب آسیا وابسته است و طولانی شدن تنش، بیشترین هزینۀ اقتصادی را برای آمریکا و غرب ایجاد می‌کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435494" target="_blank">📅 01:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0fba85b2.mp4?token=N_Jv1bhyg8ha64qQ_ASyv7QFvvBsMPfJrbUrTaAaIRnvCyYqxEaMT-Zdsw9hT175N62sgrlAANbtfFQkvSIwsM7pq9Nqg-hny6jTnlt9lV7ufemEKVui0OZ18_WUjrqdXQIvzNvfAaV7Oy3GGd72jTQ8iaYMHlUtLq0g9ORQsrJEmC_Yjo5YAYvtjAOvbVww5nZridSiCBtqpgcKCbJqEXDq35EgEcjoHQlPRgs94N1aK33TkEivrs8mk58NFvV7UybJzUkjxKy4uSsCi7-tUDWL0DFhwZH58ou91QjeC1bshSKUBguE-aGvVg0R1cFfNebMzrzZ8p7JGEqE0l0Plw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0fba85b2.mp4?token=N_Jv1bhyg8ha64qQ_ASyv7QFvvBsMPfJrbUrTaAaIRnvCyYqxEaMT-Zdsw9hT175N62sgrlAANbtfFQkvSIwsM7pq9Nqg-hny6jTnlt9lV7ufemEKVui0OZ18_WUjrqdXQIvzNvfAaV7Oy3GGd72jTQ8iaYMHlUtLq0g9ORQsrJEmC_Yjo5YAYvtjAOvbVww5nZridSiCBtqpgcKCbJqEXDq35EgEcjoHQlPRgs94N1aK33TkEivrs8mk58NFvV7UybJzUkjxKy4uSsCi7-tUDWL0DFhwZH58ou91QjeC1bshSKUBguE-aGvVg0R1cFfNebMzrzZ8p7JGEqE0l0Plw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهرانی‌ها در بدرقۀ تیم ملی در میدان انقلاب: دست خدا، دست علی یارتان
@Farsna</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/435493" target="_blank">📅 01:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMo_6cmNQ20Hir8urTK-_4xWooUEu_dQzY5HpUJ6EzVxFB66aTTlFoCFM3p-Ii0jztEQ-KYHU7-2Uq8IK1Hzp_Q6w5pvDZ9MUUyWhIFTBU-ENZcTuUlXcxhXI0yM2UzY1owk3d0iGEtSZJCXIHF3uVrLVuOB3Q5DCERLyWkccf2gANMhhdKnchm7GcbVRnAsnhifdVnmFPrdBWwEGEHnWn7WELBm8s9gWcX8QbcovftQqbZdnaYUgmPoB6bKukTU1lrjUBENZVMRdPQ7FbABYENVVbFI9Z8HHSTzklq6gWAYA4euu6WGwNN3Qvbzb8YxalSb8LclzMsuOKAV9zp7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات سفر نتانیاهو را تکذیب کرد
🔹
دولت امارات عربی متحده بامداد پنجشنبه سفر مخفیانه مقامات رژیم صهیونیستی به این کشور در زمان جنگ تحمیلی علیه ایران را تکذیب کرد.
🔹
این در حالی است که دفتر نخست‌وزیری رژیم صهیونیستی نیز تایید کرده بود که نتانیاهو در این سفر…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/435492" target="_blank">📅 01:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLYfye42g9CvfEzmD1EvMLWS5O52zboNAFlgiAuGEWOtSSVYU494IOCetSYSBM0Ygc2EODLbpWAbXFWItq9kYGs8SS7CcAziCXse_e5QyFN4QDFpH5kfW2Li_zKAP4Fr6B88rC8gBLhuDzlHer9Olw8map9CVDq0M80hrBdMXQj7n8GjoEzg_neBWb_Gz1IGdk2APTtgPVqPpmIvTGG-Dv-478AHl_y1fKJ6SkFfWT3NZ6Dawp77KhxQS4lhso3a2iP9xYqooSbTpfz67FYoUqky0DcMCM_u1OiAGJMJ2GHaYJ5Vs2uRyfQwo6xAs44cU6kxRFCQABdZQuYUl5Sdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای خبر گرانی پیامک چیست؟
🔹
بررسی‌های فارس نشان می‌دهد خبر افزایش تعرفۀ پیامک که امروز دوباره در فضای رسانه‌ای و شبکه‌های اجتماعی مورد توجه قرار گرفت، مربوط به مصوبۀ جدیدی نیست و پیش از این اجرا شده است.
🔹
این تغییرات ۲۹ مهرماه سال گذشته تصویب و از
۲۳ آذرماه ۱۴۰۴ اعمال شده بود
؛ مصوبه‌ای که بر اساس آن تعرفۀ پیامک اپراتورهای تلفن همراه افزایش یافت.
🔹
طبق این مصوبه، هزینۀ هر پیامک فارسی برای سیم‌کارت‌های دائمی ۱۱۶ ریال و پیامک انگلیسی ۲۸۹ ریال تعیین شده و تعرفۀ پیامک در سیم‌کارت‌های اعتباری نیز ۲۰ درصد بیشتر از دائمی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/435491" target="_blank">📅 00:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edb2a1af5.mp4?token=KEeIg0L3ofgcfBF5F5LdtinBJw7QTy-4a3OVFCByEm3S_uZQrqjv6RvuK5njZZlkWwTu-FUmZqwJ4Bfj9q-yQv59AKJUeSDkV23jfEYjCx40mMYllVmwxgEftjO43R90WL5vo-Be2jprKxIpjkcx4r3Cbb74C0uSDM6mnXVEOI9c6pX3jpb48GQ-6JBEWH_bkHTlm6pVCr9Bx1_aHu971evSY68FfMEyJzIQsed2MD22eN5GjUbU0UfMCaDJv0lXRcT-y7IZQnyQIQUESyPHNOwX3cUgVn8JMbNmxGbvGDBHkEAqx377r9kW3OHBIl5z584QO0DTOD2AWBueCZJhAxHFRzGxjy6iRKe_n87cqtC9GOZOn3trow13GEB5p7DBfMfGywSzMVTy14TrdkLKtQHQra21dKh0O_UIUq6e7hgSNdPp1Jl10V3mDpSM8FEis9xXVdOo_cSgTfoWJYKfzvd0la64DVODt2ryzjH645ioDVluT98M6ytjt5t8fdjUw6hMNTWZ6RtPiZvM2tIUeDbuDfsaLUQTBFcTBDdbo1vUF2JDHrnUFE5c5yzVLe72C4FJhXT_g9lj96Q7rWARt7TYmAwwjKLIZSHaTzdbITOjalHVO_zg4t5yKtjxnW8hMkhpVODBZdRRhN5_GfXyvJbCCBr0fSQ1Fp_BR9ocEhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edb2a1af5.mp4?token=KEeIg0L3ofgcfBF5F5LdtinBJw7QTy-4a3OVFCByEm3S_uZQrqjv6RvuK5njZZlkWwTu-FUmZqwJ4Bfj9q-yQv59AKJUeSDkV23jfEYjCx40mMYllVmwxgEftjO43R90WL5vo-Be2jprKxIpjkcx4r3Cbb74C0uSDM6mnXVEOI9c6pX3jpb48GQ-6JBEWH_bkHTlm6pVCr9Bx1_aHu971evSY68FfMEyJzIQsed2MD22eN5GjUbU0UfMCaDJv0lXRcT-y7IZQnyQIQUESyPHNOwX3cUgVn8JMbNmxGbvGDBHkEAqx377r9kW3OHBIl5z584QO0DTOD2AWBueCZJhAxHFRzGxjy6iRKe_n87cqtC9GOZOn3trow13GEB5p7DBfMfGywSzMVTy14TrdkLKtQHQra21dKh0O_UIUq6e7hgSNdPp1Jl10V3mDpSM8FEis9xXVdOo_cSgTfoWJYKfzvd0la64DVODt2ryzjH645ioDVluT98M6ytjt5t8fdjUw6hMNTWZ6RtPiZvM2tIUeDbuDfsaLUQTBFcTBDdbo1vUF2JDHrnUFE5c5yzVLe72C4FJhXT_g9lj96Q7rWARt7TYmAwwjKLIZSHaTzdbITOjalHVO_zg4t5yKtjxnW8hMkhpVODBZdRRhN5_GfXyvJbCCBr0fSQ1Fp_BR9ocEhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای صورتی و آبی شاهد ۱۳۶، میهمان اجتماع امشب پیشوایی‌ها شدند
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435490" target="_blank">📅 00:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435486">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiPigpZuVM51_zBLVQsQgVtuuBTL_XPlRP5zT0Y9FEAJ68pGeSthOLmRXnVMKn6pZgWsEbPrd4P6il3_I08D67Y6d-826-najmRXYkxNCwiGIITtm032rc7hgYz8QKVFtWSdouF3Mpdjsj-sOvnDG29bcUNV-kRyiJ6lGnmdThmaJMxVY4y5DEQgR7mvLWp5j87wIEAp21KX8xed7LfDCgRQ26xUeUUCBQjbpwxRirvB206MWujS5ZJJFLcgG9tq3OjI2nNScvetOb2g6q1PW5myU1KChjbhd64Pdvb0hFa0cr1gzn0ObqXeUjN-0ZIX66Oz0hWsaa8n4mAIWsj5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckdoDT7D7riBuMey1Ij11O1OF4Amef6a997hdbVv9LrmaZuSuXFKAIZtAaaIci4r3itQufxZZja_NtVrUy_UDIQ0LZYEJN9bCii2GxmXUzHyq8ohzJlXNInvp75P2w9A0YdBDpJfKtOU-EguNjbtVTQXW2jF4nBlY9IuuLS5mmdlbSve8jIepEePTg5iMMIyfIgfB3oybn7jI-pyzzUFBZIoyOxZIi1_PdFhgfsZe_EzHweMu26Oy5wIT8xn4GNUOcyuicMwWNxLV3n2y4joKAXQDrmSVIzHfbJTfPjGKgx4t7xbNNdbE3MicwS1IebYDY2vTz7Yo4vtMXeZxIlt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQBJ_yok5c508nkTOjEe-3_jzKF09CsAhGiXBSEFvwqlIxcv_7zBXvGQp8vRV58baLhFe1_Z-7FW1npRPOOKeFPBpjcNvYfWuEnqqqEfHlMbCArThuymCrcuR1TAoRG-RnVTU-7m42JbJuS_ht3UKvphAOu2YKXp-jpJrdszyhcn4pI9q8S_ZfS7K8n4EYZdluHM2wpmlmhOkGW-QmSxhVC3_uTtnzeCVgYPQ2De5qK4S_Slt1O2Q3OpkzBeT4QwjEQ6qtsRQpLOFs2BgSMay9r7t0tpl0f_5ulx7_8K1joghpAPSokffjPjo1vIMgf_XEmd0e4fv-qQzESqaFopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Poqsx8wcfW58nV0GGzmlADSa9H5d-K6xlTvYXAWffKwverXQ762nLofjtBUeKbz33iZL0tKDmC1jkTKgapO7qhgcjHPjdn5skQ93sqQCLS-W93i2R9QOlrT_7DjO1zoegQelPyXWMdzBCihTP1Oq-srtGhyP4JItowPJPJ49qV7Y30SuQKPvBrJq8zyanjHZ6ZR2e-gfrNJIK5dGuSRY2WfkYMg7ZxWwFV53sJGzpo3rXwJY7nuweopjY_I-TMRJPwIk6SrKXpD5YpVGXGoRu-cW5TzbxrEtNrqVrp-JvPJlpy_6KvEbD7krpRtCWNtVfIe3bDDWkRPEP7cMtq3log.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۴ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435486" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435476">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spNzSMoJDyj3cgJVCoD2PIH81iPDd98oMiWojg3huR5deLoqEouYgmSdic0TIzlnEkHc1SJ1lSYvtFsEqTPY-cSU40JsD3HK5hOODmJWTYzjjwwn2hxOdJmec09S1khDCuGHqEfggmOcG-MdPHkxracswSZ5bqvWTwh2ld0Ouz9UAnmC0Y4-29Ta1EFKmKxjyUT404g2LWITVTpfSHOFnW0mxsAUSmzaiEpzlY4DjwIebq9MESCjwDbt4vixmFdK8GhXAQByVJ05VfBnYAJB5p2h7Zwe2dogESyblSpl-ICa96Ws50CcOrffahCPtc9fksZrOW04auqSdslPPDtOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3y1Uzy6MCnLAoxsal6SlnmV8wf4RA7cN9FIhjL036-MepM-11cdhcIVzOkyum8tzum3zkFOGn2gRmiC81V63zITcDyh6WQ0UEvi062hyuiD2gQlK6lbQ4S1ypstbWhBTqMUefmPDAHQre9LymjenqWkkqS5faLaZDi8IAamVB807JGIJ9xJpf5Xz8k2vbebaQjL7uTV-PzDFvl9BcPt6diJt0qJQlGFJnN8o5sizaLm7R7JXNMS9hDNNtJP3hTW_GZTry1MlZqPMSsDYtIIiHdaUpm9yzecUdM8Dt8So7MUaRSWr4vNEsdvG8m2YY9XBT4gp81ynIe0trwWcU02Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESYjXn5dWXQE8BeYfns_q1RG_JNxU3gcVOCcxcE3oi_f9TaddkPN2CaqBzVUcHliaS-jJdNLcvux3QqNJbKMpdbPgCobWTDgNRHqEDp6OkWHnP0A1gg6FIGQmZ0wf4aOa2So9CT92WurxnHQ0IdpB9sEelXw7OSGeDVL_SuWJMBo6JwS-eIR9UVzKwqMryBiafRI68MeVb2Tuu8HaaUkf4xC-jonWFQz9fmzOQ4u_3TgB4UGJ_WeQCh0oS-QMFr6T8dhB7Rfgc5HU2SXfPHUjh0JNHhTdyu-Rou5P6NqRvZdamLXGNmIeoOLAaA02upS7yjdDTVKMegNkoCarzp0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMrXHfiEU844wgGmde3TvXdm5ERt0lrI8qSqdebBIfmXgR7Fw7-XgFUYGV6iE2DK0lBY2s2jsd24UOfVsLbTytzOIS6UL6uMaQleZMYvntAMFZZpOvaHVdgZ2F-IVgMq_-0_MZDlhSaxqor4TkJ0DMuCvhzriTEt7SstKY1qBJ5uorc6YjCThTw1VIaaMbMlgs1ehEkCZ5PBL2YX0tphIxeutYx-zcs-xBjoJryByFXmbLQHealyKkrFbS6prR4APjEvV_lR-T7_osktYKDpHMEFTaLbBWe2s69FT8BWVQsvpxSIv7cASxPqjgMUZg9MFeQsBBA1xVGhdI9d28Zk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHYDSizgWyNFv5Arz4UDWawzP99ldceXjIjuqZipks0If7cAffX6JrYfB96y2uYR44EvZ-YtB1BdBPtAjxuJOnFMDizmOYn5vZNj6LOgyP59tFkH6y7GnE8OsVM9H30jrb_iPAGdRNQzTmziNLyN_F4gsJ9WTd-4EEQkQr4GNednOX7c9ayl6mno0IV_M57iEfw6HjZ6HuBONou8DOfuuERxaGz7BUC8SbF3R_96MQVx5_ESkdroWPI8_BAZ0L8N993ydDfKC-YZtJUU9XSebVo12gcBLxZEZ76EHtLAGVL2lUIW_rkwSSDhNP7lTfSpSqYCWfkIf_Duvr7fNx9bdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQrZaBB7Tor1ifYwEGRAqhHcZy7mM1ZtaCVURxS_fuq2Hk_jt0145elxMQDT7er0FIr0lT8tx56U0G0Y5khZIcfevVsoHrfsvNb0LRxl8POwhCKdS4U-IyZRkO8Tkth5-st_MJQTFPFIcMSeoQYtCdbkHRnwjAF_13Rn0i97hJA4x0otytfrR4hehxLE_yu53hk6Gz6m4T-YOaRxCG1C9UvCAd3_-53Y6qN-L6_6ZBBkmbIqfjGBX1W8Kzj3rPgM5dzOyOLXyqOLRVpomIiC9De-l0i4Pn_xjRr56nPuTnjVTG96-2f2qg8LohRCEhmygmq41Lrz5dPyQJyFByp5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2BYibI9rQukKJSQi2JpZnHIsstJeU43RM3kSlSsQ8UQyGCfrd6BV6uag4AHpJLmt5I659_MqsEIxR5dO6xXBZKyf4PPpQK-_qzejb62Q83UA_uRtJWcOlIymYFkOMLtU6TTxI_huWzcM1WHPLWUmhtUeIU4BXv38rgi8LZHOPN3JFqVXfWaJXwKWHv5wAv2_kxCE-RtJsd6C6W8FBja2-QJnGyR8VTNm_Bcu_N0e2ClslTvv0zuAjImdrhcNS-a42qDTYZj_N0yrGTUgDZ4jppmghQVnVPRTE1S1JidLKtOp1Rqmk-VXJEEQBIm7vsSpzaipZu4iYricjCq8hNQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiICjXlcMc0WSlgwVtWh8tQsOpr2jV0OQ0GtJZ0yHSCGTsA4bZQdXJLtdeXbFDNGSXvRMz_m4O3lv0yNjCxO0MyATMPO6fQz5FM4Ec9DqcRT-1rxFV-x0wrERjK4qH4v_MBWHR2qf8WMw0cOZz6yvAl6UzG6M5EUgJABjcQOTZcy5cFPUp0SJo-APGzGOHHxjc41ePqOxgHIxr40haBDlfc-RoTIcL6EyDRZBltB1_ixMSelrAtvY5MSh01zp7TvxEUfvpBYMYbmQlRJDGBg5GGEzg0-wgRlpANk6loHzkJ8Krqud3M-ns4EJRy662pPzZo9w3kuGHBrZq6fDNewzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6yRq_RfU8Q182hy3HmEWCg_vODl-MyEGukNnLfgcSfG3VzbXWYlSKJC6VUy-mDsUGUSDC8OksQjXCO4tBmQ3Fk3CryrapaNP19XerfGO9jJtznJP2_v_IsZlITzfVpiehvkiJdJznSH_bywdBC8WrpV5jGjs5Kd2p8OYy7QyXmyjO9LzdeeZrth1jlIji-lnEP9HASouUw1Bpdbkk4C5MXXBUJVa5y2XA4UDRg3vDU8wTZ33gWsVh3SIsp_eSukeXVwu7OR_fJSrQnvnBKGXu45moyr1Fx565eLLalHCl1DxzQ2ry1TASoA2fYzt4pnniF3o71RaFWh4htqbx32aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lB2a-yRyP_3tD3WkWM2-EymL7-2PtMDN5jLww0BnAskYnh8S31o5FilbhpCFThnM70Kqh3UdNqRqbqcgsYsT0Q-RgDpKAvmanOOyIjjjhxGPLU1f6R-a3CzdiOmTM6DoksHG5mL8uRRxmjzKkH5KfG8I8BKpgmjQjlPAif4Yhw9YzmRdXNtSbPsgs13_vlAswEbDSYPyGuODQmbQ3SC8pet_bOMgqgNau7mFKMxIXm-p1japeLYVORc0JQk7-AP31CvgTeXpy9fItOMWqyEz8DQLWH6KtdBV5niQReuiBuvkekWAPlI08sl43TZyMfA1w-tp0NWOI9ME7nXyTfa9jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/435476" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435475">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">امارات سفر نتانیاهو را تکذیب کرد
🔹
دولت امارات عربی متحده بامداد پنجشنبه سفر مخفیانه مقامات رژیم صهیونیستی به این کشور در زمان جنگ تحمیلی علیه ایران را تکذیب کرد.
🔹
این در حالی است که دفتر نخست‌وزیری رژیم صهیونیستی نیز تایید کرده بود که نتانیاهو در این سفر مخفیانه، با «محمد بن زائد» رئیس امارات دیدار داشته است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/435475" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435474">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🎥
حماسه‌سازی مازنی‌ها در قرار شبانۀ دفاع ملی
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/435474" target="_blank">📅 00:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435473">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY6aKY1CEFskNbFA_VfnJmyvhA0tGvuAVZfLYqo_RZq7u09U1CiBIjGnctRveeJqcLK48eY5rGkekOUD4-wPvQKvpCMYEVJL3SolD-cW7Q6yp4zRQSYm1u0tVKuYnZtPScm9M8Tgo1cSK0nLZ7LcVJudGne4hqPMfn1l3VsVWMTT7a_czPxE8R1dEDB4i2Ap4sJZPUI_gzqtPyvp3x_AQ12dqxh8AowDVPqTAnDAkG1AePGEAk2C6d08GAbCReXHHUkvCfeomGME-Un8S-JhEixvqA8i6iz8_LQSjAtf1vCHHBi9l03IbWfkJz_bAMGVl2_TFYCfwdR5cLZN3rrGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است
🔹
نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔹
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔹
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند.
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/435473" target="_blank">📅 00:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oc1aD2aVLBq-ETrJGdaqUgtJPHHmirm7ND1aNxZIq4PvaEhQcGMUq4qvmsajQeiTzWxrzNU_-A0jmOmT7nOCgVZdAeAxozn02frvIoaXDTAwt9cYlG-9Uvde6HT6_Z98Zt7tzquxxrhFGg2oh-itd1jGO56gJeBQOj5X8bRFXGFgHiRwiFL43iAzIDuRInCd5HFY2QSQYe9g5vEa97SdrkWMtSWXJ4rSdxz6Ox8IgohmbJlXHl8n_SLVa16u0yzMSdMt2nWdrmj-QCQuzc36bCF3Z6j8lfeyXrFkvMNj7GMnYVdOKGwwr0gs1Tp7CVoFw_XqtXDmB2Yp4Gq8kTz_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHTQOp2q2JLEbDoGZqZ32YnXooh-gME9RY868Os4GgEFJkRJ2-RBLIT1g8DJXAlEO8Iv3CYpnDJYCHeH9bRfEdugfMVxhfW0T6wTQ5OOnX07F6v2VFogVZN1fXoVmJXAmX3_2iXJ53w7tjVC3G9KPcJxmSoFPP8NU4DshBnJv74VceEzwBK2Trx1tGi6HXfsRrpYrS5kZbed6tBKc5ypj6SA4Vq3bEFpnjYhLvQ6QEYdXCsfUq52OcQLW9v6zXdVg1lymx6uSWr_zs1XnooFY0hszfw1TIrSN2XXG4n6HpQETT-ScKVoQoaIIiZrHz_bcBFnCeA0z4abP2GFQPax3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalKREjS-ZR1bopfpHnVNHvBkU_XuarKg3A2tnCxmURbnQGROesAIc53H2fi0S6jyXlgG4-eaOW96NHWRgRD6bfDifZo1HAQbwN1Ev1BtKU8M3lodZ14VEk6aLcUO1i0VyEYNRyGqklLJNMRgMHSUXquiVg3kuOhip1rm1bPxTS8yj8kt3zIxeOV7wRI7LrGNnmFRm17wxOkGWuzt9q-rWVCjh9elmc7O4tG1XYRd7Ys0U9D7v2MATpLbYmYiMOjXhmzZLyhjBSBEZO5XvIeBnPiSWG8MXqgP2w8ttIOT7QyC_P0xdfkYlplJOI5xuQ-NViGXX6HGRA7Wn84nJ5WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTshZELkCR6pXi47CXWi5lnShu3F2GfH23bdOAAQbRfhNsF_vNjUZxOGDw05psq5uKeJGHJuzDyZV6seawYZsHcmfFWawy7ak4gKYmV_qwvcbDqc2d5-A64vXhDPO8-kigbD5jppSiQAU3cxlKC9p4GHeQZhjYNGy-vj-B7yx4kSYM0v1f8VXQ5yumVEgbm90onxsFmaxpZU1rpkz9ES6tF2_JvQE-VozANkCiWBagJ9AXibyqiolMZxJD8oF_gXRqtcBbjEx45qheghOAwALGZI8OdYPcFKaPPOGEsEqZKXXDFWIDxdf4iHSSlAtll_WU7-bhYGV9Rw2Q4CLtt63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzniWBQWTcdjo2tL_WiqoIDitc2q6cPTpXt1HNkgf_AokrrVDXH7Zrpq9kc6U999WPVBY62ThCC-g-R0CbcuGk59PpOWbOvZRNODxtZRP8ZNvYvkaSDHrjIljCgnAn8BkQP2U2q2q5k8yTWtN5VmLHQAIXL5VgJPgU7EpiuL3CIdQF8rT0_SRoI-2rrLarN99HTSKUOLp7Ts8wiBKRhAasUx9Jbfp7V5s6qou4D9ejEgrb2hN3Tfbb-gJhDQsVI8dCXkqKCJJnYtY9iHfq-T9BC0T9DlNXLG_lv4p2r1KdVakjqKYub78_5N_kKZaUExgoS92MF6NENsI4r2kB02vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAQYGeV1awKB-fLRRDEfCyq2Kdm5naxvLz3hhhjSnc4QlyIlf_JiIzykyFb-_6cI9kZnuGw_5lL7YKMp3oPRLl2gAHJYqetVE8c6v5RTX-L_HjqFT0YOMDw2FheJGRTjBdeKuo8PTEapah0vffL5SzXOXYMc1HLtItGx-lC-fzpNLxEpt3micS4IyXYylvmMcUrIIUd2PxCc3lrEXYEq7NzrmLdgzxpDWmB19fwoLazHKfGP1EzmJg-Q8nf3Qw1yJt6QGTC8HdtZ1BYGIz8NYOY5QFBNE6vPZ-wGVyWvSQlOB9h_VbX64iVcNY2TqN8lXO9RdgA0Ne_LzS4KfrcZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd8gtFgsF5cqUHDREGTp90eNJLEfl1HxMUypC_v9glDrddg1uV7iHEzuM8S4gYsVEIEv3El1BYTaWc38M-CV7v_JkiKyE7i7I1fWxs7qmpKQlxBcWId875cpZlGjsyMVYJIVQBMGGG_VlXy6shld4lSYld4fruP7cuCquX4CWGs6fpVl1lbZPGIGv-GewaTCx4EZjw_hOd-dgKTGlEIXAYB5EwY_kxu5P_YgMHWKcR37Xtm0ikyTfCB4WkcTwIJFv-G2qqnW7OthA05lFAlVMsHyWo0f2TpQ2lJaC6TkNve9aBXMP6LrD6FpM78gHxFvc8Jul5chVjCLTXXdIjMovg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رویداد لِبران (اجتماع همدلی و همراهی ایران و حزب الله لبنان)
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/435466" target="_blank">📅 23:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ebed97b1.mp4?token=JNpGrzgy7eHs8uDkyKrBpgu9nZkleVzPCwDn7b6-BZQimtwhD6pxrzE_u4JgwmWZnBrztT4h6i4qWCqrhKVmUOK3s-9YWDfBTgqHrCBMii6Jv3JZqfR0045QXioi55flIihyEKY4mviDO4d8x32ruQRoRVK5FXpisBL-1eZGhxUSD80spKg5a1lu4F_O2xqr1Sh9B_BBSB2-cJSInWCWSmtTLiFgDvvk9aHhK4TDXDTv-ylcMOTR060lZDVEO7WQxj7670U6CdDILVNIN7f1XXSK5vnz30sbUiDq_5QsEF9oZt3AjdlliKN-q5C25TBidTvC2x_FMMtteWVG8ST8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ebed97b1.mp4?token=JNpGrzgy7eHs8uDkyKrBpgu9nZkleVzPCwDn7b6-BZQimtwhD6pxrzE_u4JgwmWZnBrztT4h6i4qWCqrhKVmUOK3s-9YWDfBTgqHrCBMii6Jv3JZqfR0045QXioi55flIihyEKY4mviDO4d8x32ruQRoRVK5FXpisBL-1eZGhxUSD80spKg5a1lu4F_O2xqr1Sh9B_BBSB2-cJSInWCWSmtTLiFgDvvk9aHhK4TDXDTv-ylcMOTR060lZDVEO7WQxj7670U6CdDILVNIN7f1XXSK5vnz30sbUiDq_5QsEF9oZt3AjdlliKN-q5C25TBidTvC2x_FMMtteWVG8ST8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حضور خرم‌‌آبادی‌ها در ۷۴ شب حضور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/435465" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f969c9ff.mp4?token=Mq4m5Qqk-Eit3jpZFoD4QVYv-kDpjwyEoY-hUpSt85X7TdUs_lErCe670zLHQ-Lzp9eTAlntnftErf052fygpd-Wo6Hy3dQj7HUYxSlc7czF5Vy9VzlEvBjIpyWA8SMwApLyko1IIudfJ0p6dm1iynsHH2r7qH3jbuhzUHt5Dsz9lwyT4pXBiBjN05_FlRwbmrZ7HCDOEenhKjhoOCqGMMJlvzsDsmffJGs1n_WH1AdgiXbzWGKOVOzfF5KlWoO2FdEwI3kXfNpwwm1zGb6jEP484JSI5Z-vWJjv8KC3Gxt6BZKDMo2e2FhZoX94B2VfQrxVjPCt42yyA3dhijUrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f969c9ff.mp4?token=Mq4m5Qqk-Eit3jpZFoD4QVYv-kDpjwyEoY-hUpSt85X7TdUs_lErCe670zLHQ-Lzp9eTAlntnftErf052fygpd-Wo6Hy3dQj7HUYxSlc7czF5Vy9VzlEvBjIpyWA8SMwApLyko1IIudfJ0p6dm1iynsHH2r7qH3jbuhzUHt5Dsz9lwyT4pXBiBjN05_FlRwbmrZ7HCDOEenhKjhoOCqGMMJlvzsDsmffJGs1n_WH1AdgiXbzWGKOVOzfF5KlWoO2FdEwI3kXfNpwwm1zGb6jEP484JSI5Z-vWJjv8KC3Gxt6BZKDMo2e2FhZoX94B2VfQrxVjPCt42yyA3dhijUrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری سی‌ان‌‌ان‌: براساس آن‌چه به ما گفته شده بود تا الان ایرانی باید تسلیم می‌شدند و محاصره آن‌ها را پای میز مذاکره می‌آورد اما نه‌تنها این اتفاق نیفتاده بلکه آن‌ها توانمندی‌های موشکی خود را بازسازی کردند و مواد هسته‌ای نیز در اختیارشان است.
@Farsna</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/435464" target="_blank">📅 23:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916ff1848f.mp4?token=i68lA8tw2a6o3lyo48WPIR4d8sxsfE8s3lPZA4SdQY0koo7ZCb0Wb5fERmcPByJa0BOXPRilEzsMuNZP-FO_mNkUTjI1sIb0Ah347SzCDapMxH3NtZ-6MinnetOYs7Fn7W4GY-Y4O2hLRo79sQpMPdV0_ISSpj76ayGrxWduWSaInWwWBxkhh9IjlN8ik5Pjbo0-nisLDa36wZD78Yp8waCjiC3iaNEpj3tHvqC7tNMwWnddn7cagqiV-A8WBTXvghZMKCEvOQ-RDB4YhcvPWoIpFQ-Fn9P_VcqJ4tVpjY4xSqmE5QpHqftK7DkqpVBCO1oAl_cimsEii2Hy5e1bqa_due-o3NWc-HhxOQwN-gI-Y9KiaG0AX3Z4kLZ7tYTEasnORPlDlL3HeALEbt0us10pzdbIkIhlTUjGtcSVY9YrAaiCN3mMP69XLUDdIPM7MkTD-cI1mVSyTf9Fwpv3ndUrYfLw8JH3WuK1AgmQWoU7uWW88-wTEv_IbnSTrqAZBYk5tSm5Za6DbYKUnSMvkwvIPJFs3sTEWVp1BwIz2rsC9ZEV8eY-zPRSMkVoyrbDymkTcOTD_tP6xFAH3hFYWxdxnLjD_W4ANEUkR7Dt9PzN0FeWYDJ-4gyTn3Mo_rVhF25y8XkpEsdAUzSQIBbr4o4gDeiiqWLr72XqJlNUmFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916ff1848f.mp4?token=i68lA8tw2a6o3lyo48WPIR4d8sxsfE8s3lPZA4SdQY0koo7ZCb0Wb5fERmcPByJa0BOXPRilEzsMuNZP-FO_mNkUTjI1sIb0Ah347SzCDapMxH3NtZ-6MinnetOYs7Fn7W4GY-Y4O2hLRo79sQpMPdV0_ISSpj76ayGrxWduWSaInWwWBxkhh9IjlN8ik5Pjbo0-nisLDa36wZD78Yp8waCjiC3iaNEpj3tHvqC7tNMwWnddn7cagqiV-A8WBTXvghZMKCEvOQ-RDB4YhcvPWoIpFQ-Fn9P_VcqJ4tVpjY4xSqmE5QpHqftK7DkqpVBCO1oAl_cimsEii2Hy5e1bqa_due-o3NWc-HhxOQwN-gI-Y9KiaG0AX3Z4kLZ7tYTEasnORPlDlL3HeALEbt0us10pzdbIkIhlTUjGtcSVY9YrAaiCN3mMP69XLUDdIPM7MkTD-cI1mVSyTf9Fwpv3ndUrYfLw8JH3WuK1AgmQWoU7uWW88-wTEv_IbnSTrqAZBYk5tSm5Za6DbYKUnSMvkwvIPJFs3sTEWVp1BwIz2rsC9ZEV8eY-zPRSMkVoyrbDymkTcOTD_tP6xFAH3hFYWxdxnLjD_W4ANEUkR7Dt9PzN0FeWYDJ-4gyTn3Mo_rVhF25y8XkpEsdAUzSQIBbr4o4gDeiiqWLr72XqJlNUmFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غرق زخمیم ولی قامت ما خم نشده
🔹
رجزخوانی فرزند شهید لطفی‌ندائی از شهدای ناوشکن دنا در رشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435463" target="_blank">📅 23:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎥
روایت شهید سپهبد موسوی از پدری که دختر یک سال و نیمه او در خرمشهر جا ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/435462" target="_blank">📅 23:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7fffaad4e.mp4?token=hHBbkMlRJ26-DwzIEeEurK_s1hjZzqgE4BYsw7-KAr5H6-9FAICBxwqb4C8t0FtVy9vJkJXYbgJjkw9LOlxnQ1tcZZqLGuqiZBYXv7DldIbpU733yFSdxaoYbdA0FIt97OIeDjFp2EsmnAZzhgfx9b066zc0Tft_R52maUO4yBDsiOhEemtFDlKwRbYqlYDysHDo6aK3-v2elF8qHGeuGPOEJigfHSscUACwTTj2g1zbB3cP9oGfu-4Ye5EWX4ov-xfrW1skqN_jeMdpDV6rHJwfjLXzMT02yWKe1pnoqXdOk6LiAtpOki5XlQeuShC1AL6_mRfHgM9SHeSu4vnFkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7fffaad4e.mp4?token=hHBbkMlRJ26-DwzIEeEurK_s1hjZzqgE4BYsw7-KAr5H6-9FAICBxwqb4C8t0FtVy9vJkJXYbgJjkw9LOlxnQ1tcZZqLGuqiZBYXv7DldIbpU733yFSdxaoYbdA0FIt97OIeDjFp2EsmnAZzhgfx9b066zc0Tft_R52maUO4yBDsiOhEemtFDlKwRbYqlYDysHDo6aK3-v2elF8qHGeuGPOEJigfHSscUACwTTj2g1zbB3cP9oGfu-4Ye5EWX4ov-xfrW1skqN_jeMdpDV6rHJwfjLXzMT02yWKe1pnoqXdOk6LiAtpOki5XlQeuShC1AL6_mRfHgM9SHeSu4vnFkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاینده نام نامی ایران
🔹
از سرود رسمی تیم ملی برای جام جهانی با صدای پرواز همای رونمایی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435461" target="_blank">📅 23:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم اندیشه در شب ۷۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435460" target="_blank">📅 23:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTVNdYBMu42XU4wiMZKNXS3o2imI48UQjgl-I_fDykCJR9YOi1zaaEpnjhOP8PNT3yo1_TLVdBmRWijS4uBxM3NQMYty2bD4uycNZrX2TGIHJQ4wMPXD2uYk3zUNgBq0MY8QMkXr0y6qSvewujs6OT5RDvttetcDra9AulDyC95xsmDcJwAenVBHPyhsY-8BLFJVzrhnHSJ_qdTrcVMIn0brZKgZ4p6PWQcSnVidL3kxDiS21FwLUPJRWmI-bx0gTIyD_HHYP6iZDT7iOcAfYCUYSVcBiM-2PioRKfOQ8UHcsLvv6opEiusaSzQjsm9TXTXdUYkLHBK8XQ7dwhql0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرر هفتگی ۶۰ میلیون دلاری شرکت آلمانی از بحران هرمز
🔹
مدیرعامل شرکت آلمانی «هاپاگ‌لوید»: تداوم بحران در تنگه هرمز بین ۵۰ تا ۶۰ میلیون دلار هزینه اضافی هفتگی به ما تحمیل کرده است.
🔹
حتی در صورت کاهش تنش‌ها بازگشت کامل حمل‌ونقل دریایی به شرایط عادی به چندین هفته زمان نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/435459" target="_blank">📅 23:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
۷۴ شب حضور میدانی مردم زاهدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/435458" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">فرودگاه امام ۴۰ پروازه شد
🔹
مدیرعامل شهر فرودگاهی امام خمینی(ره): روزانه بین ۳۵ تا ۴۰ پرواز از فرودگاه انجام می‌شود.
🔹
در حال حاضر ۲۰ مسیر پروازی فعال وجود دارد که پرتکرارترین آن‌ها به مقاصد استانبول، مسقط، نجف، شانگهای، گوآنجو، بغداد و مدینه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/435457" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای چندین انفجار در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/435456" target="_blank">📅 23:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435455">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🎥
رجزخوانی یاسوجی ها با فریاد حیدر حیدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/435455" target="_blank">📅 23:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435454">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09bba4b1ee.mp4?token=Wbu3CmBTZCuGpq04olNPxzLaaRPjIQhQBBXH6tYCmxcedZMEi2ATReZYtthUTsDIdcgy89VrM43TfTVyrseF_KHze6YbGLzt-tImWDT1RufwN5mWVas-g1xGSBsZ2qpIGPhjP2IfOzGMZ_6X02ug0mrDcU-hQpgamz-3974HF179XnEfejXLENTOT07ySCg0m2MIdQRjA-5asfsKAnli6eMOAUyYYbLq3GbbH94qoi9LUQZYynT8EJ4FHq_boBPC8vj8IeTq95yPoEES9sWV5l1KE2GAdb7d74TNeglloZ53zBHR-bALcu4Xp9HCKYGT0wcUCo7dl5E_a4ehzSLm7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09bba4b1ee.mp4?token=Wbu3CmBTZCuGpq04olNPxzLaaRPjIQhQBBXH6tYCmxcedZMEi2ATReZYtthUTsDIdcgy89VrM43TfTVyrseF_KHze6YbGLzt-tImWDT1RufwN5mWVas-g1xGSBsZ2qpIGPhjP2IfOzGMZ_6X02ug0mrDcU-hQpgamz-3974HF179XnEfejXLENTOT07ySCg0m2MIdQRjA-5asfsKAnli6eMOAUyYYbLq3GbbH94qoi9LUQZYynT8EJ4FHq_boBPC8vj8IeTq95yPoEES9sWV5l1KE2GAdb7d74TNeglloZ53zBHR-bALcu4Xp9HCKYGT0wcUCo7dl5E_a4ehzSLm7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ملی‌پوشان را راهی جام جهانی کردند
@Sportfars</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/435454" target="_blank">📅 22:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435453">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🎥
امشب موج ۷۴ بروجردی‌ها همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/435453" target="_blank">📅 22:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435452">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">معاون دفتر رئیس‌جمهور: پزشکیان گروه‌های مقاومت را از ایران جدا نمی‌داند
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/435452" target="_blank">📅 22:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435451">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc347445e.mp4?token=F66z1grCUYFdsjpcOYfoiP5yoHcl55kxQya2Rz4fOHSZ9sWG5ylxc7iKHcSjjwBCbZdAOsOcFrNQzVWjwTdz66cA7NBj-EsurvN_QQaoZKHXxs-bL393FmPAgk9jQzhyqi7TiWeJOg5EAOw1LXlvKYdDBxvWjfY0UwMp3-wh5UkYZZ0UGbPCotFmtF1R4cwEWmmezDJtyuUPDm6lk5KwQFGuy6vjYUOFLGfQLZ9MH4CzozbGNJ7WH4x0j2t9buoWcUqdwLw_X3aJTCcdfD6eFZGcmpYuLr1drneEMvM6xNFNO68pnNH3lvej-i2a2rt5BGJocNKePmKvcU2agqtfyjfa0MTPKrJMbWGkGFt8AWWq6rHHlYHXbmbVAGxYjZOcGYpPGY75rPd5mFFOmyHVT2Q29aXU3L288VDpEd64oASQeImkjE2RFdRvR-CC_M2NjcD52K7XI3nzFYOOwB0mYE-g6dPvbTnHtuS161Oy8qthqW5VNtHBKIbNzJx72jHcjWVi7P19JG3GZHxeKCx5YU2POX94UQxBJyLE5B4IF0ldSt_1GM1NKRy9J4exA2xW4SSQOdginmR6PqeAKlOSBFwOSDIMMQOGs61AWRxkqpyBPLIhKTkO4zmLnE6pu5KG6NHyg1HWCp8oQv_qcSlweqX8IamrUi02sEQT7Cckh5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc347445e.mp4?token=F66z1grCUYFdsjpcOYfoiP5yoHcl55kxQya2Rz4fOHSZ9sWG5ylxc7iKHcSjjwBCbZdAOsOcFrNQzVWjwTdz66cA7NBj-EsurvN_QQaoZKHXxs-bL393FmPAgk9jQzhyqi7TiWeJOg5EAOw1LXlvKYdDBxvWjfY0UwMp3-wh5UkYZZ0UGbPCotFmtF1R4cwEWmmezDJtyuUPDm6lk5KwQFGuy6vjYUOFLGfQLZ9MH4CzozbGNJ7WH4x0j2t9buoWcUqdwLw_X3aJTCcdfD6eFZGcmpYuLr1drneEMvM6xNFNO68pnNH3lvej-i2a2rt5BGJocNKePmKvcU2agqtfyjfa0MTPKrJMbWGkGFt8AWWq6rHHlYHXbmbVAGxYjZOcGYpPGY75rPd5mFFOmyHVT2Q29aXU3L288VDpEd64oASQeImkjE2RFdRvR-CC_M2NjcD52K7XI3nzFYOOwB0mYE-g6dPvbTnHtuS161Oy8qthqW5VNtHBKIbNzJx72jHcjWVi7P19JG3GZHxeKCx5YU2POX94UQxBJyLE5B4IF0ldSt_1GM1NKRy9J4exA2xW4SSQOdginmR6PqeAKlOSBFwOSDIMMQOGs61AWRxkqpyBPLIhKTkO4zmLnE6pu5KG6NHyg1HWCp8oQv_qcSlweqX8IamrUi02sEQT7Cckh5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت میثاق‌نامهٔ تیم ملی توسط احسان حاج صفی
@Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/435451" target="_blank">📅 22:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435450">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
طنین شعار مرگ بر اسرائیل در اجتماع شب ۷۴ شهرقدس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/435450" target="_blank">📅 22:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435449">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a9a739b9.mp4?token=IkhkmTf7KoOZ5Snt222l3JiI0GfVlUR9wuxBWiZM_N_K4iflZxZfFWJknBmcgLJlgm5Dhkhm2omIf3ywKnKGwvMj3gsi8JK_cFij2gg_haPzMVynat7xtXTHRuwH0a5f2rpnvfYEr8Y3NiEGlfZ5d7tqSpJ8OPoZlxzp4p904gsh__oSuN2YuK02z0EsgDGYgJfpOysMB40sS_LHvs8n41pKwyo2JZWJ456tgxoKPk6fi69KclG6g-QhvPDbdaC7D6czIdTDXTWmjqIfzTSogF1vaPYFnYoq4PCIuq-sSoCq7NEu_pl-9izD3AVc39LKK9npDjvq-3CzSmVwBWzq7Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a9a739b9.mp4?token=IkhkmTf7KoOZ5Snt222l3JiI0GfVlUR9wuxBWiZM_N_K4iflZxZfFWJknBmcgLJlgm5Dhkhm2omIf3ywKnKGwvMj3gsi8JK_cFij2gg_haPzMVynat7xtXTHRuwH0a5f2rpnvfYEr8Y3NiEGlfZ5d7tqSpJ8OPoZlxzp4p904gsh__oSuN2YuK02z0EsgDGYgJfpOysMB40sS_LHvs8n41pKwyo2JZWJ456tgxoKPk6fi69KclG6g-QhvPDbdaC7D6czIdTDXTWmjqIfzTSogF1vaPYFnYoq4PCIuq-sSoCq7NEu_pl-9izD3AVc39LKK9npDjvq-3CzSmVwBWzq7Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چی این چمدون رو سنگین کرده؟
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/435449" target="_blank">📅 22:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435447">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
۷۴ شب همدلی و عشق به ایران در خیابان‌های گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/435447" target="_blank">📅 22:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435446">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USy_SOHMr0bohkhah-8Qv1y35OGAwnX4RnJl5EbnFXVobLnMRQYLiy8QBk1H4krZ8owHCy5c22-OoqRiIkM7P5B_yRMc7uGDnRACucQ7LfSk7stwK-ay7IO2H6YyiB638UkB7hGoaaE7LqZ8OCN3zrJ4BK0vejiC0dJXHAF8cMYrDo_37axQmfhqN_arx_No_DjGm3dzQ4YjNC9ajiHjZ34PMPJre9yl5mOsSt9VkMbIn8cnUMX-GHME5_v2bruFlkEvgXAJK0AePorrAv_PHnuVAI0PrYvAfsPjoCrgD-4XB9rgviZdZTJd_6Y-Wgjl8sQSqbkfyjMUNqHZo7zFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر شهید دهقانی: منتظر مجازات قاتلان فرزندم هستم
🔹
جلسه نخست رسیدگی به پرونده متهمان شهادت سرهنگ شاهین دهقانی‌نیا در شهرستان ملارد برگزار شد.
🔸
سرهنگ دهقانی‌نیا ۱۷ دی در شهرستان ملارد و درحالی‌که هیچ سلاحی همراه نداشت هدف حمله اغتشاشگران تروریست قرار گرفت…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/435446" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435445">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708ad1605f.mp4?token=iuTlh0f1_lgtz4Exn9hxy22gyMD8_NiG-tzhwVc5AyQ8xdeE-UzWBjJH0Xm-PLmv6s1MBPVlMEpDhU0XyHnlQMqQgMNZxO39MlLv69bve4uqn7oEogAmPIe_59hHFQ_Q1pHN1t3c1215pvAtcH2aMX76dIXWtN_I7sKuVA9_tyUO9-cNKOP8edzNKoXIFt81nF_HOr6uRRgr41_Mf62eHAgvBKNpDjrub9-kvj53dmctN__emkUEdmn7Q4y5DhvWsnxz4og6zuM3lRF3oDKedG-gsZP0fkorq2QytMHejmkJovg5WAKbx1U8IvGgvihV-lXu6ceoRxpsCMYFqZpv36n3qzMWupaiQ9I9vnY_wgMGZ8-38o2YfEOOPJb2zFjPy_DWer05a7pjja8F8RlRMzAEnpHa26yU7CiS7Uj54gc4H2zFZvxq_W2oklx_zukh2Rqnc0eJAj41NhnVpSb5oXTPpKnfcNY8PsdJWoHJV0m8au-2txYHz8HHHxg-uzcd4YK_pI5XU0vHf8inz2EK7FpFiFMDLKlzdwPnm9XsEk06RU9zTVN15QOfc9iHc1IIRAY0cnoMBXmWaHwdgfFQ8U07ceCBpBOi4baKgaksjJ_DeCCbKuHsFVa9Pfm947qKjWwtuuzXBObYMUUc_UWkpvmnVWSIyWmot6Cbh19f52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708ad1605f.mp4?token=iuTlh0f1_lgtz4Exn9hxy22gyMD8_NiG-tzhwVc5AyQ8xdeE-UzWBjJH0Xm-PLmv6s1MBPVlMEpDhU0XyHnlQMqQgMNZxO39MlLv69bve4uqn7oEogAmPIe_59hHFQ_Q1pHN1t3c1215pvAtcH2aMX76dIXWtN_I7sKuVA9_tyUO9-cNKOP8edzNKoXIFt81nF_HOr6uRRgr41_Mf62eHAgvBKNpDjrub9-kvj53dmctN__emkUEdmn7Q4y5DhvWsnxz4og6zuM3lRF3oDKedG-gsZP0fkorq2QytMHejmkJovg5WAKbx1U8IvGgvihV-lXu6ceoRxpsCMYFqZpv36n3qzMWupaiQ9I9vnY_wgMGZ8-38o2YfEOOPJb2zFjPy_DWer05a7pjja8F8RlRMzAEnpHa26yU7CiS7Uj54gc4H2zFZvxq_W2oklx_zukh2Rqnc0eJAj41NhnVpSb5oXTPpKnfcNY8PsdJWoHJV0m8au-2txYHz8HHHxg-uzcd4YK_pI5XU0vHf8inz2EK7FpFiFMDLKlzdwPnm9XsEk06RU9zTVN15QOfc9iHc1IIRAY0cnoMBXmWaHwdgfFQ8U07ceCBpBOi4baKgaksjJ_DeCCbKuHsFVa9Pfm947qKjWwtuuzXBObYMUUc_UWkpvmnVWSIyWmot6Cbh19f52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شکوهمند امشب بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/435445" target="_blank">📅 22:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVV3WWeLcemOR6oJVbQWeSu1b2TGWgRkgVL3ljlNOyhqFBYWzZhwq1YQHPGwJ-upWCSMLN6V1Obl3m1V7gFIT50GLJVT7B24miEW9fpWJyJstDs1e7uw-OWnqrhucVZh_SaCqqTzF88JwuzjQ8rAMGPxejUDCM7thKC9xsUegmp1vAGM6zhGhSt2kw47yxyDbIoUmiKqji70ygAqDE60mSs4DKkPaUxkzvkmKO4OVy-ewWC93eDaI4T2i5YrqVin1XxIhOuJu6Rk1NdEY9fvkwAicDzEWEG_Sy7O-Ym5OD0W-jxm70VJBoYjgHiOMDsSSGGHeFRuONwtZno1m5MFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش‌چهره، اقتصاددان: در کشور و جامعه در قبال جنگ جدید دشمن آرایش جنگی ایجاد نشده است
🔹
درک درستی از تهدیدات وجود ندارد و بعضا شاهد ساده‌انگاری هستیم.
🔹
نابرابری میان تهدیدها و مدیریت تهدیدات در کشور وجود دارد.
🔹
باید قرارگاه جنگ اقتصادی با افراد امین، علیم و دلسوز تشکیل شود.
🔹
در درجهٔ نخست، نیازمند اقدامات آنی و کوتاه‌مدت برای کم‌اثرسازی برنامهٔ تورمی دشمن هستیم.
🔹
مقابله با لیدرهای تورم، ضرورتی اجتناب‌ناپذیر است.
🔹
در تاریخ جنگ‌های جهان، دولت‌های موفق در شرایط جنگی بیشترین سطح  مداخلات را در بازارها داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/435444" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435443">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHnwPLJU9eT_FEpksX6ymigD1Wy4jo7czfL4pWPGUeBxopVCDcpUqHHZJSySqyabgGCoIHIt-hixTgRYrDRxxvU4X1jq2LyOBVPxFgJxf9lC62sUjX4G-9OZyuBtiJU-a8FjujIZUahe_oehw5fkNLsWLpGZIO_VpHouuRho1hWVjz7-zVnP2wFzXBCE10J9IAUzt1XUgEHAzCGab03SyryKPoQUfEL41TivceR-ipuqoy9afyX1wBKiH1Ew6ZGk4qUQzjpmKenK6BTOosBhn1sCLfIMuuWbJOvSgTBmPvf_ta9rUQCSKlATbaPN2NvKKnpXESO7gJ3nS1m_pwV-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردهای تهران با شروط ۵گانه ایران برای پایان جنگ بروز شد
🔹
شروط ایران شامل رفع تمامی تحریم‌ها، پرداخت غرامت جنگ توسط دشمن، تثبیت حکمرانی ایران بر تنگه هرمز، آزادسازی پول‌های بلوکه شده و پایان جنگ در تمام جبهه‌ها اعلام شده است‌.
@Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/435443" target="_blank">📅 22:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhkzNv1ZV7SryiF4QgKQ0Z4jWgfVoUejsyleu7frrcga-eOnpP77a_WJGkqQ7KntWqm8F0dfGQ2v1FGxIADOsY27b7dAjIFEJ3u6AcqkQTV0Le9gqTGA-GAiZKt0BIg1IODBTOYtA4-EyaG6UpxbDLG_RHPpOdArrs_iH0h9qzPn3yTNGpufhQ19kRb_evL8yt9lhkd9I2sjjKWUo1vCtHKMXY7Bu2qBPsdWXCB8jtCiJbpirMkA_vdV7looJN6a4e6Ue5yeXVvji9smo5d-XsQe0GH3iLpMLlxd8cLgfuF6f2gXbqAcCX4LyKacTEw1UPg1xurpzy7bZuNQT26Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/435442" target="_blank">📅 22:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435441" target="_blank">📅 22:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مارکو روبیو: واشنگتن پیش‌نویس قطعنامه‌ای را در شورای امنیت برای دفاع از آزادی ناوبری در تنگه هرمز پیشنهاد خواهد داد
🔹
پیش‌نویس قطعنامه در شورای امنیت با همکاری عربستان سعودی، قطر، امارات متحده عربی، کویت و بحرین تهیه شده است.
🔹
پیش‌نویس قطعنامه خواستار توقف…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/435440" target="_blank">📅 22:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ccf47277.mp4?token=KQHYcfAEWQzY7GjFBfcoXuTYzGRRs4KyWYkrUmJ4mgCSfWdVi19LSnihmuCvuO2TAuC7gHMQOJYUW9igs9LzcHpWUrsqomHv3mquSAcE6LLjppTzP5BVt6rXMJRQmBpL674h7VBBHOIId0NVec_VCtycWsdZOAZ0-qZs6NkjdMUlGOiXyX_4kEwujgQ0S0ske_ECdZaWkAO6q2Z66YGpueyoZddrwTNOIH8PSwExiQVEyb2GImRbxHz5cuRbzZ-7o5Lun7J9Q9QfoUITVf1vLEpRTKqJS3KGUOzcBQ87g4PZbXnjOQMioOo6sI3ZMF1xPKwgxZF12WVhwhHPPv7Shg5t_Fvt5rawAxYdCsm90vieENONtKEnMSB7I_YUCkQvL72ZZPV_uuybs52gc6OBDQRn4TyxO8XVzbS1kpjBLvzaRocO7gqZ0ngWIUQ5zU7EG2Whocf-Tv8Af4163KFOXLpYB1G-gNmYdOBLt-n6xeJuUCQ1n97l9xJ8zdK8tovAay6dZP6qxVGPU7tmzoPhv-7-mv3uOt32-IaFrLMphLWe55wYQmUdloPoFq-_aL_q3eG4EZ-nzcYHb7hzumWsiJ8hTDqkgcnRIkg9OELbzLXwjAeVi2xg5Ux5cOKJB-c8F4q2bbl8BEWdlgGf3gfjKicyiI0knUyVtTga-kD84NM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ccf47277.mp4?token=KQHYcfAEWQzY7GjFBfcoXuTYzGRRs4KyWYkrUmJ4mgCSfWdVi19LSnihmuCvuO2TAuC7gHMQOJYUW9igs9LzcHpWUrsqomHv3mquSAcE6LLjppTzP5BVt6rXMJRQmBpL674h7VBBHOIId0NVec_VCtycWsdZOAZ0-qZs6NkjdMUlGOiXyX_4kEwujgQ0S0ske_ECdZaWkAO6q2Z66YGpueyoZddrwTNOIH8PSwExiQVEyb2GImRbxHz5cuRbzZ-7o5Lun7J9Q9QfoUITVf1vLEpRTKqJS3KGUOzcBQ87g4PZbXnjOQMioOo6sI3ZMF1xPKwgxZF12WVhwhHPPv7Shg5t_Fvt5rawAxYdCsm90vieENONtKEnMSB7I_YUCkQvL72ZZPV_uuybs52gc6OBDQRn4TyxO8XVzbS1kpjBLvzaRocO7gqZ0ngWIUQ5zU7EG2Whocf-Tv8Af4163KFOXLpYB1G-gNmYdOBLt-n6xeJuUCQ1n97l9xJ8zdK8tovAay6dZP6qxVGPU7tmzoPhv-7-mv3uOt32-IaFrLMphLWe55wYQmUdloPoFq-_aL_q3eG4EZ-nzcYHb7hzumWsiJ8hTDqkgcnRIkg9OELbzLXwjAeVi2xg5Ux5cOKJB-c8F4q2bbl8BEWdlgGf3gfjKicyiI0knUyVtTga-kD84NM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پیراهن تیم ملی در جام جهانی رونمایی شد  @Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435439" target="_blank">📅 21:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/435438" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">«پرواز همای» خوانندهٔ رسمی ترانه‌های تیم ملی فوتبال در جام جهانی ۲۰۲۶ شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/435438" target="_blank">📅 21:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435436">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea2800611.mp4?token=n9sM5Y_mjw0EsbwsPHzMACqAXycPGuyA8Uz100jNJoKvzAZaotOFp6hi_uBP7BGPRYgckt_FPg9gPglHXDfaq9Qpfrlebqbz6Y7E-EmCmZRKVkJrRlNLbkXS2gMO-mE8wK8fc8hnv4fyoDjeCIxzeqqUnigKLWfwCANJX4iHA6c1yV-3svNJlNST-Z7Rt56m6rWlpNHsqpHQU_-qXXDLZjUb_TLyh2_InTjQDISc0MNBwGY7llszPUKVwNU5cRUlRJSohCSgu2jXTFnB7RDZe2NRuaTsK4r3yhxyNelqxpwx42endfDtZjj-b-HgNzSBKzVkHr_BBfGHTZoduXgneIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea2800611.mp4?token=n9sM5Y_mjw0EsbwsPHzMACqAXycPGuyA8Uz100jNJoKvzAZaotOFp6hi_uBP7BGPRYgckt_FPg9gPglHXDfaq9Qpfrlebqbz6Y7E-EmCmZRKVkJrRlNLbkXS2gMO-mE8wK8fc8hnv4fyoDjeCIxzeqqUnigKLWfwCANJX4iHA6c1yV-3svNJlNST-Z7Rt56m6rWlpNHsqpHQU_-qXXDLZjUb_TLyh2_InTjQDISc0MNBwGY7llszPUKVwNU5cRUlRJSohCSgu2jXTFnB7RDZe2NRuaTsK4r3yhxyNelqxpwx42endfDtZjj-b-HgNzSBKzVkHr_BBfGHTZoduXgneIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پیراهن تیم ملی در جام جهانی رونمایی شد
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/435436" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IingY6SMc2ZtUlavvxS3CluvVY5FERA2z72EdspZ3KSxAu6T6r0Tj3uRsiZq18N7OCYU1iwrddX9dmoghxtmkFPAr7DZ67NrvbZLFvuG7SpFzYVCIfj-P4YWdsGWJki4011UHM8JlfQLBqkwlnVmfcbBWUPXA8hlShPaazJ4RHbluo79LoKPOQ1npoZlo0axuJ6plspypIRwZtfCJKH3MCD3YjrMk4KVTRIcvEJkQMO7AYAAiCSaoGzf60pOcY_DFW2y43JW9atiS0VLqoCtj-8dZNmrKkElj-tgMdKSyKelInlL6l_0l8HegawqCU9leLYZYatG7WuRRyYWWbIZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقی‌ها به کنسولگری کویت در بصره حمله کردند
🔹
به‌تازگی از خاک کویت به سمت عراق موشک شلیک شده و عراقی‌ها به‌شدت از این موضوع عصبانی هستند. @Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/435434" target="_blank">📅 21:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0ZMK1mwRVEae3K_3cGKO86Pmje5NNf7pPe4ssr-IJFWTDuotpHwwRTSH2MSKdSx6RR3r2ErR9Nab_kCuTHkoPDLAegJXk_4RS8AWAZOJWSc_3ECn8-WW3zQ5SshIBqyAcE2elhERuvsWt8fHIoVu3X3fmIRGptpTrWxOTaDY_cjAIqzJffeRaLhgqXOLj-0l55-NePQud1Oe7pe-M_q2B9kgjFk_DLYYiwABZknJaHzYfFbIjY_oP44K1LJtSefZKXAJufxQlz4j5jXn0VdQz9nVBwLXykVx6EW5Bg6x5EMvJxFDaeCUG5d6hEwV4mb8JtyeCUErSMvdnE-RvSR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awY9Xq7eaXVdM1BcLpiTKvDTTZRLRH_sQFC3cTIrApHHJWMwrgzYKdwjP3Uv6mcJf-ZlsJUOFZay5BnQxnd0hsUdnexB9Wp-wbaBBeMbpPhkM_hhDFfx2I4v5kDNG-uPfMlrByMq5_jN9ZD-P8XCNm3goqS4acq2kXqect0F10Z3GZ8jNCmq21ci_ZzPzN0ltoGtrAyeugpop878CjXr8Q5JkfWSylbeQI_8NArynqh-vHHe84FYb7ew8MyU8wbdevOIpwftgjHqRVwIAKuwq-66zSvsVtE2SrFHsAfJg3AJ7_1pSY7f88NBlSYViSnQ6vXJmfnYcoAlyIUhLl1nUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcSdMQsktH_dJUCKXYN4x3iOt9buipS4iw9wrOQjGAZi9m-FV0lV_q_Jyq9ZC2-16GjwarrXkywpIPGl7N5yyvzmDun0D6yRCMKI9PEZ7JwsEW8zz3cJBHaEkgUX0aoDGg69yIqkyf0mJN09fiReF-wUvwRcj4dGwt9HQMglK58eDlUmVnaboO7GlSv3JvHD_b6F4gMWUsowSbhci2lQ7It9JfRMrX82mySwxOtbZPIoIYhHnpKAz81HqzHPqKshI1Hu-mIxE56fkJ8jVKp1D8p8_9GxxufBdezzjzIbwPH6tqgLWGQuAbXO-eiwqt8UBgfBgmX-8X2fKNsEvcd3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v39GHaQyDcf-Ar-zKD1Xa0b6oAZ-o_hdvTn4JTwaqGCTP3ch21Rb11PRSCa0bx55Lr-FH1l0FzgLQs0jRtTxewCCwz5G3LMYtZ2jiaB-47mwrN2O8myQ0oylYzYgAaDYQ_ia4UqEBp5F9y81RTQo4bjTHfaKaz6GWwMJyoH2AtBrs3448OeaXcfp-juf_u59vp2KtNHY2SL48kAdzgPitwHmWmdWw-Qq1V3phobewjgpNZLFmNv5N4dXT6fjkFIooLnx8qIsEK24dpxIUrNzweOt1A3jHcvuuV0gu9Dg4Kf0AtSJ-WIrhS1RaUIauShiopgRH3ZET1FgX3wTLsxeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1Jpl3SP3QDX7f0p_D3UbGBIJASfOWFfAKjhYSCUQE4ErFjRVTyJJmFxyHJ8E3tQVfjMvP1RHCYNAESn8j1DP2owUDHqTSeYul4Hm9jhJ3nW_ca842t7tjyjVl6Id1XyHw-nrx_TIxihsG4QIP_9CgtVt0tKIWYwSDO6wLUjkU_7_-5iQA9PPAyDM7UmZUBoQNEovZhw0awITdUpnR0QHEHMd2kXpyjT9838xLRsDCtUxn9u_ugQjAnWS1UFeYTTtf5rjsUJyBtnPCQOSbzhYGyTkCfNAb3FXV3z2E5NGqU_x0vyKisfeGVtX3lAIRlvp4B7IGAXT3taSNSMdCPxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGrOcPx0TQC8_emWEyaSGond4BcoRsiyodIIgq2iM6zaXvwsUsIoPxCNQykzBHAxwtyma2o5zYDk1BovLv84Dk8HH_Lf9D691Om-bnZoOrwgrHKviC8QPK5mOkTIcKvwzCBeJwe7wP2HmJo8F1hFljvVhosqrCKQHrS8eKscc5ZL-0bFYiJtvOPhPPT6YIBOQ0B-h17A-eMJr9i8ewlYE-HbNTc3IaugnAHX2feGRFY2muUIEwrsJLqGq0iwH3sJf0x6Jg1iFqlr_UaPKLRx2qj2zQg2F5_j-qPy9WAWwisPsj4h080rKVYepgtkYTkNT1GXRjr5D6TH8tKAoU7QFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jezo6aEYZAp5AYIpPIbyszF3xb_44QWePSYDKC-53O7iAZQl8or4iUtg1i8QXEV_Ntt5Wg1Qk-7LKF7-BG8I9Dky3spe1L3QzcmQMOfo241Snc1H-3r_bwX2f64LVNHlWWqBavHeayDA5Sn-ihYNu1aQ_f5YhvMUCyXQPX6aWZVM3-pLs-xLIwXpVcJP_fJlQgGVE2Jpgh4orKckKCKCg4BGSxLTALF5KR0IMZk9QErjAqk4RlB3HHlz84_3e3Kci702S_Q5y2JIlxPaZEwCNqg2T2NYaa_KDfRuhHc50uC_ZbwnPRCzBoN-C7pNcpAAFicaf8M-nZ6PYAeIQ1lErg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهلمین روز شهادت امیر سپهبد شهید سیدعبدالرحیم موسوی در آستان شاهچراغ(ع)
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/435427" target="_blank">📅 21:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5de6b3208.mp4?token=G-5AZMlLQP0ykt14EKnCcE31wylCJ9mCNSOPHG53xX7Tu7dzOfPSLPKoNMxtlL8eRGRoZ-8CVh_X1F_oRbVRBHltcTW2FgSgDzgmOyYPHmbvpFj_qHhUcpWZlazGQgDuYtPW_0zIgz_x85H2vNw-hMTXnmqs7vZWl6yn4koZ3ngZWQ9wV9LtuRVy9OT3JZ49aFkPEsWdgSo73x_vrpoqtPAjlvr4Ro4REdZcsqkqysHfKwbU8pV2fo5LVANn9S1YVrBWXAeRflxzHhiAJ1ZttMdbqqj0DVgycf5PMBWQqERL8eISaYr41zXtrXMzsVVRbcpeYXICuEa5oNEsGFPciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5de6b3208.mp4?token=G-5AZMlLQP0ykt14EKnCcE31wylCJ9mCNSOPHG53xX7Tu7dzOfPSLPKoNMxtlL8eRGRoZ-8CVh_X1F_oRbVRBHltcTW2FgSgDzgmOyYPHmbvpFj_qHhUcpWZlazGQgDuYtPW_0zIgz_x85H2vNw-hMTXnmqs7vZWl6yn4koZ3ngZWQ9wV9LtuRVy9OT3JZ49aFkPEsWdgSo73x_vrpoqtPAjlvr4Ro4REdZcsqkqysHfKwbU8pV2fo5LVANn9S1YVrBWXAeRflxzHhiAJ1ZttMdbqqj0DVgycf5PMBWQqERL8eISaYr41zXtrXMzsVVRbcpeYXICuEa5oNEsGFPciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی فوتبال از میدان انقلاب به جام جهانی بدرقه می‌شود
🔹
معاون امنیتی استانداری تهران: در حمایت از تیم ملی فوتبال کشورمان برای حضور در بازی‌های جام جهانی، آیین بدرقه چهارشنبه‌شب ۲۳ اردیبهشت همزمان با اجتماع ملت غیور ایران در میدان انقلاب اسلامی برگزار خواهد…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/435426" target="_blank">📅 21:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjryeLcJmlsC8CxUuNEgK6VTm8UmXA_KqRW6fjSws_9746Fv_AG9VSpi1t4Vh_tcq8wL0g2DyuZO-I4zwA_g2_ffT3N9sRHmht511aaWecY5vHDU2LQBf1Qw1SUX2Gvm9wh7XQDC8ZjDGrhfAdtojW34PxlSuIPFq56nnhAGl6uusvyJEaV1WC-ARCy-IXhdY5i1v2zh5sdor-xaHiMGY1CUCu5MOzJ3wgFpo-Uf3opm51Y4jzytYZ-LU5AVwSW_9oaj6d5PrkD-EwQSdFt-cxtD9JG_nme-o-JCLm4xHMCnbll4xzWLbXqWbu54Q0HeQos6Zi5KzWZ5EfZVdz2u6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیق روابط ایران و چین در سایه بحران‌ها
🔹
روابط ایران و چین در بحران‌های متعدد غرب‌ساخته سال‌های اخیر از جنگ اقتصادی و نیابتی تا تقابل مستقیم، همواره تعمیق شده و کارشناسان چشم‌انداز آن را مثبت ارزیابی می‌کنند.
🔸
«به چین اعتماد داریم»؛ این اظهارنظر وزیر امور خارجه ایران در سفر هفته پیش به پکن، پس از دیدار با همتای چینی است. سید عباس عراقچی در این دیدار ابراز امیدواری کرد که چین بر نقش فعال خود در پیشبرد صلح و پایان دادن به درگیری‌ها ادامه دهد و از شکل‌گیری چارچوبی جدید برای دوران پس از جنگ در منطقه حمایت کند.
🔸
در مقابل، وزیر خارجه چین ضمن نامشروع خواندن جنگ آمریکا و رژیم صهیونیستی علیه ایران، برقراری آتش‌بس کامل را امری ضروری و اجتناب‌ناپذیر خواند و بر تماس‌های مستقیم بین دو کشور در مقطع حساس کنونی تأکید کرد. به گفته وانگ یی، منطقه در حال عبور از یک پیچ سرنوشت‌ساز است و هماهنگی تهران و پکن می‌تواند نقشی تعیین‌کننده ایفا کند.
🔹
گزارش کامل در این‌باره را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435425" target="_blank">📅 21:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdd6667ba.mp4?token=sEGCFChGqsFj4RhKKpsrEjScyHn5iFuNqXlakt60hcQAYjhEvUkNC0x7T47upW5IUwDTs90F6-YYEYE8CIV9RTS87wpYTRbCP1KWtAaZBmruYBLLEBkQUP2SQTszzUdMeWLLU2mS-wGXtuhfwjgRcypDUTn9pmDKuNnRBaM8M_bSO_QoEoHHQrIKKtQZdNEVHXijZXrmUTxJxqd0aWhLHqE-7Qv0Ty6CtizUIdS_0T1HAAeeRsz8cDszbRWMu8jq7dDaSEgWmWy-9OVl113OMLS4kR4hMJOy9UXja0tF8udAj-niLyiTvBBSUBwlgLJxdGSb7OmDl--HQ4YO-pGzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdd6667ba.mp4?token=sEGCFChGqsFj4RhKKpsrEjScyHn5iFuNqXlakt60hcQAYjhEvUkNC0x7T47upW5IUwDTs90F6-YYEYE8CIV9RTS87wpYTRbCP1KWtAaZBmruYBLLEBkQUP2SQTszzUdMeWLLU2mS-wGXtuhfwjgRcypDUTn9pmDKuNnRBaM8M_bSO_QoEoHHQrIKKtQZdNEVHXijZXrmUTxJxqd0aWhLHqE-7Qv0Ty6CtizUIdS_0T1HAAeeRsz8cDszbRWMu8jq7dDaSEgWmWy-9OVl113OMLS4kR4hMJOy9UXja0tF8udAj-niLyiTvBBSUBwlgLJxdGSb7OmDl--HQ4YO-pGzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی شرکت‌ها دوباره فروش اجباری کالاها را راه انداخته‌اند
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/435424" target="_blank">📅 21:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435423">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5577cb4ce0.mp4?token=iJosQP7_us6nhvCozS8Axg2h9oK8m1dPnE-3_Op6c7okIeDuOOQiAN0pQDq3IuPD79ZlfdvL5EFQD1XamZL0HKAXXI1onYYa3ux7qci87LefOJUfAhuiaejhGvCfXa_z6ivlySgFXjrxf3W8NkLEc2c7RB8AELSNinxu83i5YJOu-UjwU_hxddu94g8Rl2cIyWGzFO5P6pQDiQV7OuPAWdADUnEXQr9y6DHyRArVXwH82DvNe5r2lbR3f8Zyv_4PWQiAlKScy_59qWLKzz-MmE4iGT-5CPiqLuEIM-eItT3uQ9wiEcIZy2hqMuXNnYDBZjo68r5dQlp4nMRcmR66KTQSQ3vgUUWDfYqdSvilWrR7vEamK0U7whxQQJ-ER3uwbiy2W6yy35sL4rzXafI8ZNT1qGo0B-Fl5wgllKs0wCVNsG4Jii2iubcn1gYIkxCrYrhaXDV1zt_YRG-7GWFZh9dms0mLIAAt4224if0GfHCKWyaFNhUAQqNnETL12ksAF7JmocG4PWj4zK3YiqaUBsom_Pj4_Veqqbw_nuNwnKiwsLKN0D4Vplx2rDfEpOpN_ygdnYonvpF9FHfyBGYQfw_whqVeY28QOMTYRh3m86YtnigdrWIpzd8_1OEcD2eck_tzch1joxFovIAOOOelKpOPTwZFSX8p_Xdqp1wnNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5577cb4ce0.mp4?token=iJosQP7_us6nhvCozS8Axg2h9oK8m1dPnE-3_Op6c7okIeDuOOQiAN0pQDq3IuPD79ZlfdvL5EFQD1XamZL0HKAXXI1onYYa3ux7qci87LefOJUfAhuiaejhGvCfXa_z6ivlySgFXjrxf3W8NkLEc2c7RB8AELSNinxu83i5YJOu-UjwU_hxddu94g8Rl2cIyWGzFO5P6pQDiQV7OuPAWdADUnEXQr9y6DHyRArVXwH82DvNe5r2lbR3f8Zyv_4PWQiAlKScy_59qWLKzz-MmE4iGT-5CPiqLuEIM-eItT3uQ9wiEcIZy2hqMuXNnYDBZjo68r5dQlp4nMRcmR66KTQSQ3vgUUWDfYqdSvilWrR7vEamK0U7whxQQJ-ER3uwbiy2W6yy35sL4rzXafI8ZNT1qGo0B-Fl5wgllKs0wCVNsG4Jii2iubcn1gYIkxCrYrhaXDV1zt_YRG-7GWFZh9dms0mLIAAt4224if0GfHCKWyaFNhUAQqNnETL12ksAF7JmocG4PWj4zK3YiqaUBsom_Pj4_Veqqbw_nuNwnKiwsLKN0D4Vplx2rDfEpOpN_ygdnYonvpF9FHfyBGYQfw_whqVeY28QOMTYRh3m86YtnigdrWIpzd8_1OEcD2eck_tzch1joxFovIAOOOelKpOPTwZFSX8p_Xdqp1wnNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرانجام این جاسوس موساد اعدام بود
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435423" target="_blank">📅 21:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435422">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8034f918.mp4?token=IxtXdF2XR7BOlFv-g-oQNkfo4JCZdgHTT9ZSFHeHQchx73qhWDS9fKUllzHt_Fq80DAzDHTzGU5o2ntaHvFCpq3i17XqcXkLvxptf66imcylZBJFVHto94yOvxxT9xvvvBgC6Omue8rf6jD_Qs0f2U5nSpuYNgyE44hZBZU3RvDt_Ap1pfmkQa_JyA_WEtxP6HgdWOXzfJ48CAzR3cXbkn18NUS-vn2geqkqRZf-tK5Wa2Xc7cBzy2nPoOAqfC4DGBsaL3rnVPPUey9ZuZHiv7htWzmavljvcY0e5_v69D9GEtohqogYNAkvquUP_exl-IUbTFEMdYnlAhF3CZGAVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8034f918.mp4?token=IxtXdF2XR7BOlFv-g-oQNkfo4JCZdgHTT9ZSFHeHQchx73qhWDS9fKUllzHt_Fq80DAzDHTzGU5o2ntaHvFCpq3i17XqcXkLvxptf66imcylZBJFVHto94yOvxxT9xvvvBgC6Omue8rf6jD_Qs0f2U5nSpuYNgyE44hZBZU3RvDt_Ap1pfmkQa_JyA_WEtxP6HgdWOXzfJ48CAzR3cXbkn18NUS-vn2geqkqRZf-tK5Wa2Xc7cBzy2nPoOAqfC4DGBsaL3rnVPPUey9ZuZHiv7htWzmavljvcY0e5_v69D9GEtohqogYNAkvquUP_exl-IUbTFEMdYnlAhF3CZGAVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر ورزش شمارهٔ ۱۲ تیم ملی فوتبال را به پزشکیان اهدا کرد  @Farsna</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/435422" target="_blank">📅 21:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Mdyvmjq5RzzuYocUH_Zu-X3bvlxj6_KDm2h_OU8WnJ_QXpa1rgHXtvDkjAov9XpTMpflSsyd8f4ToKhmPIkgxv5QeYF5qtjSwTaQmeTEUTqnes4KTqf3DrDyEL9YDIYO6M42Z5hHiGhDl4f-G5iER6K-PpLsj1JFgLmGCcPC1vsf44Cgs-yep1CH_CQdrT9HgnIoDaoFg_tssnZSTGS0yQrRlMQxpwxCUJy74C22tO_FPNY4v2hvk6tZ9NbFcUpTk7rJtRvnPaBpOcPn9eey8L172Nu67-EF7I_rX2oSNmID8UxW2szdcKrbZEafzaMs-sjXR0VQq5zi7zJiYEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای احتمال مرگ یا کشته‌شدنش نامه نوشته است
🔹
درحالی‌که ترامپ، در بحبوحهٔ تهدیدات امنیتی فزاینده سفر دیپلماتیک خود به چین را آغاز کرده است، افشای وجود یک نامهٔ محرمانه در کاخ سفید توجه رسانه‌ها را به خود جلب کرد.
🔹
سباستین گورکا، از مقامات ارشد ضدتروریسم کاخ سفید، فاش کرد که ترامپ نامه‌ای خطاب به معاون خود، «جی‌دی ونس» نوشته که در کشوی میزش در کاخ سفید نگه‌داشته می‌شود تا در صورت مرگ یا ترور احتمالی او، استفاده شود.
🔹
این افشاگری در زمانی صورت می‌گیرد که ترامپ در آستانهٔ ۸۰ سالگی قرار دارد و موضوع سن و سلامت جسمانی او به یکی از مباحث داغ سیاسی تبدیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435413" target="_blank">📅 20:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkiagilIhCnq6FR2jc5FgfySS9TuCYj01Fj0_-it48afqraF4RfuxMVTnv1x7bemqX--z69eiN3sTpDZhR749UIcSqSb3y4-NzmU6yU4z2mygTwc_QuUvAmjUuAYcJMbjgT-NrGOw1rxaueOLajPvu3xowgd0RqcAjzXJEa_t6hZ862ZFbvTdPhuES0-Me5O7hD632aY6HcKB9sRikpKomOuROBRpCQnWYiWX61UQvsJ00eQns-jmpvKCnYoTZAD32xvyM_V9Dly18Ct-mQbb-uWbUL90j9PaEE6qSS4RjhgbsFYHhW4bOIRzeoYK19Q5GpJiTWlbwtrz15oHsxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: اسرائیل علاوه بر گنبد آهنین، پدافندهای دیگری هم به امارات ارسال کرده است
🔹
فایننشال‌تایمز نوشت: «اسرائیل سامانه‌های تسلیحاتی دفاعی از جمله یک لیزر پیشرفته را به امارات ارسال کرده است تا به پادشاهی امارات در برابر هجوم سهمگین موشک‌ها و پهپادهای…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/435411" target="_blank">📅 20:52 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
