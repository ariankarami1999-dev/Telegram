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
<img src="https://cdn1.telesco.pe/file/S_0mSu0b7DxR5vJmhVFAp2xFObgKvnt5JL8fSMrk6FYPcOOR5ckzU8kjxxZGLfBKwboy634LE4eCRLLM86ZxccZPkJhog4WH_njWZn00-fwnMz-0YmKbeyhS7l07HMXoaVSJH2ZLNHmq4gLJLv8h1epEYqk0efrxcQDPIcxGT68u8eIAHTEFQweZ4wC9fhXfg51C7m7_47bftml7BZ1fHN4JiFskcgapzCInRo432OHmJFnMsEokw7iz6RiKQ0MFZ0EQMr04zwIZD0bFVV4HAu7H14-Yw_87DkpxeCWciHwH4Rp05gZSAGXaxgSRwxIbP-eOlo7z6CDqKTFox9Uhnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.42M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 21:50:23</div>
<hr>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=eT7lt3LVHOaE91thej9C0kNCQ8h_SBAnpmq3KbFLr5TIHYEdTdVtN7FX86n48yNa8B-WxZ7UGuDuakc5zjF0ZsbeZMKxerOlcIQTHZf3uhrhrJY_DDzlJVnBm9vaz6vAWVfWizB7X7KjVLm91J7MY0mz616sY7XV3FsKMcv9UEdhSQbjh4dkrox5myJ6JyFRksZHImbMzQn6d7evbpfy0c8emVY6dzbHLnh8t1xoO6RvWR9OAgKZvOEA2ytrOEb525j8DmZpQ_6rnb1FG2_SjZN1sTMNJcNLy1_mC1x29tKmmNR9FYXfNSz-Mtpo_4TzEGQgLJjm8AZYdMrtquXevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=eT7lt3LVHOaE91thej9C0kNCQ8h_SBAnpmq3KbFLr5TIHYEdTdVtN7FX86n48yNa8B-WxZ7UGuDuakc5zjF0ZsbeZMKxerOlcIQTHZf3uhrhrJY_DDzlJVnBm9vaz6vAWVfWizB7X7KjVLm91J7MY0mz616sY7XV3FsKMcv9UEdhSQbjh4dkrox5myJ6JyFRksZHImbMzQn6d7evbpfy0c8emVY6dzbHLnh8t1xoO6RvWR9OAgKZvOEA2ytrOEb525j8DmZpQ_6rnb1FG2_SjZN1sTMNJcNLy1_mC1x29tKmmNR9FYXfNSz-Mtpo_4TzEGQgLJjm8AZYdMrtquXevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jDbsfJc9od5p6ktnZYr_sM_Zh5AZqr-eq_peaRgLVDcBA1LEYoW-hAnCeqS92J-69FrRA24R6BVKCkTDd7w9oopS_0pYa8DHgEX972yHM9wHKjh0kX8XP-ZKCyaoAjBBcR--N2TeUBTo8Eq9a9DMimZa6CgYlw4xdJnfFXFxYLk6tmWoLhS8nf3JaFE5_He-jWCPxIpvoNG7W-pTOyUwn5OQBFnT4-TNDQNNWsADbe6BHoGOCPHWC-nIvdwxPkL7cE1ArG6LogVweeQjaqrOl-KxMem8fREm2r6XOt47wmaEgQBKYNSnmLqEbo09YNAgom--NZHikAqv6eg-daJHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CLC6jyyLwd7nJGOFmpNfASCUorifEaSdd5DkwNPTDKSedehxS2SUWOaWUNthQSY5sZ49Uw92prrry3-6iRyjp4Sv6SXGrwM98KSWJFOrvQsBawHWzCpN5GZ3ccs6E6YJ2mPf_V8aJJTIbe9BN02c37Z-vRyJq32X8EMFhX4oWEp3luc1Ep3RwqTgfNNq-AzqiG70CgP2z-r3fvqXNXSMdaW4oAQxX28UYEG8EvT-tpXs6_dBvUODNI-_2x4CRWif_kHNzwyk12_MDMJcNQf7Ux08skXKFzFekJCNqM0bMkwUpESnqxCOq3S8r4Z0R55yhiGks7ZFBizc-gjsC0NR0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pgFml4gUnAKYFUnxlqqICUr1YkxWfVZOtx5x3F90X7pF4SfR46c1sl2Z43Xh7JxgAUwntMvNbojnU6xwVmE1bC43JJZRinVwWnAHaqXHuiuLybHxpHMXge1P8ssBdvp-Z7_pZsWO38eDsIzT7PQf_no5SYCvfUYw1YrzgFnDrAQ-3He2S8wAydByRIchsADfIgmdbmIaf_fhY5XEyv6O6tleMtsubJqpITi0u22_g9NqfIxmP4TByDh2q5-2u74NukK7eSmSpXmrqFikZW5m0PX6_ZhhHveCy1aPZdRrZvpLbjRHVQ6XLkqYj_o_q4VcaQzj_zJ4k71XRFtSTKYTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KLh_rwotaA47bMYH-qK-Weimih6kqcivfp-L8tAMdrnP9LY9FD7wr4k35N0I7lv2nDk-KLwHELuAHRb2zUgoTpI_p0NcSQkBoYuqa4bKwKGbiXAsojsUsdqq4MwN_8vzuKauQtYgTy5vKbhyD_iTvc8y5-krmXchQYb3QbayIqJ6VQXHLZ5xWjUzqdZUz1Rxe5-dQxZ9UnSp6L72bMe4sto2N36uGlRohV7DAs8kvpjxka-tSrYi5pKdrEgsdMAArGv41bJEA9sB3WNNlwh0FhLqrnZrBbS-x_YjhlVPkqG6v9skmYEjxWyS5uiwE7nTnbfVr5UtOG8dvcSGPQPDYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjqmO73OFaASa-dsLiPmBnfAwF89Tji9roY3H1oMYURb4Idwh4jPNNqcs7Fnq96CCqMkkk4K8J14jZyX3GqFhcier02BTvEy90MxRQlCPz17NR8YrEv2VvBNFRetMEiPVEar_E4NsvPMnnZ95RDwh2RYimz-7nSWzxODcCJwc5dsYbYRXVt-AP8hMlr7rMTH5NoZ5tLbu7i21MuiI-LuVD5uIDa7ui9AprWKIXqWeg57hUyBTEfSP4RsQWJkEmJwMeeMzTESM3QUgjBhGrSsLVMfrVTP3leJVLKRXBNgvzcjH4r-jVglsF0DftWzxtSSsUq1Jj10KZkACU_cu4kyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_141Jha0blIeqRy_aoZPPZHwvI6ciXhbjJH2bPTb2iP33Uyj7EH81P1drS3Ap34HsEz4hZxsVMBwD4CRWeEpVMZKjzpYaxl6VTR4R6grd1vb7tjDUWMRsXpSrYAXcUhOnCvZ04oOgNreWyT7trA8XfdZzF2hok4vsEUYzAYLfwgKtYhFUstHY-9KtvTS91Pe5-4HZ6kgOMn9_SjIZvR3KDv0huQ8dX7xvZYAnVtFMVNFigOZLivRxiFAoYwxrRAnQvSKEOEPzIljExDbsYI4cqq_YdOgPPRTcwKEOClszLsbKCiKHi-8Mz6qlLhqIShf9sQGPaFE2IUlSG6_RgXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BBXftSzO-C2c4tRCpRe4RYvzN80xRebvuXU2uh_0PGYZfFEnbVsi3p8_BXdnkPNO9jKG6OSJXOBES8YXdLunzOs4wtqRvgQYjb5b92b7y4ljaw1IaobPU-hbNeVmRamAq_EVqbki7sL_EkSXKz9FMONCmCNUdBaZh2fNeGg3kEDZ9WH_wM4SW3yJMc6hGKCK1jR3PmbievJcrBZCNuve2KcvIQYeaFBGe2XvdaFSKb6EHU00by0XneqXxfyltQKqZMMOyZ7x3549Xhu2dlvROpB4IS96X-DzPOWagYLSd85Q7e8Bp0U4Eq2OLF8wMrjmjkseGPl6fmlI2F0rKWVp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eTKKQUC7yWVoLujFfm6m5TQUJ2FdsEixZSc40SIIKw6jtpGRPL444uhst1DZjdgSBCPVk2T48hplsAP8xyz5qkAcwJ5jIrQ_B2R41BBEd6VfaSgDpA8t9-IgT7gPog1C32JSpfYW4Kg_T_RFQyHhZSm0gOLFvKBEegAaQ9GCJ9dq6BLwCZx8-SnmiCgEDNYWHjggUNkB2iIES6sqbvWYcdqYeitZdJSSRsTo6VKcUZrJI8fLEfqMSAKszsVwc00kjcTxh-S-kPjJ-DfgDwjV22hz6oL8DMhQSrf4wEgwGSgC9v1j4cleIAHvvyBr3Uz-1C_Lsjo6765f5ilBwliymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=dLn7parbLY3YQr-9BPPUaoMcABIp25VkieH0ds__aIMYwZdJxc4pvsmeevc54Bu4I5rZCw4UAnNikVTliV643KeGnH3jSgt-J1sJN6K-lPayAOiVPbrUJxIgTXivIOYjB-R8Gg-x8c68FOmty-jutfMe00p2mg8aKEpbj-SpgTy0PBfOmdaqcwAtACAdGjdvyNW86MoB9pOzd1BSmrBBlZ-RrNCjv9fmc7QPqHgMs8nT203fbDDOry0w9XdGryQ3M4gZsWoMHYQekczsmrBbyy9Lu_ejTubKz23aherIEIuBqyr0rJzbHr8bwug3szcEO0CPpjXaok4KhnQabS78Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=dLn7parbLY3YQr-9BPPUaoMcABIp25VkieH0ds__aIMYwZdJxc4pvsmeevc54Bu4I5rZCw4UAnNikVTliV643KeGnH3jSgt-J1sJN6K-lPayAOiVPbrUJxIgTXivIOYjB-R8Gg-x8c68FOmty-jutfMe00p2mg8aKEpbj-SpgTy0PBfOmdaqcwAtACAdGjdvyNW86MoB9pOzd1BSmrBBlZ-RrNCjv9fmc7QPqHgMs8nT203fbDDOry0w9XdGryQ3M4gZsWoMHYQekczsmrBbyy9Lu_ejTubKz23aherIEIuBqyr0rJzbHr8bwug3szcEO0CPpjXaok4KhnQabS78Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/md7QewVNv_VC3aOgWmrdWpYKVjgxl5yGG0qGxJPL3L9kzeRF0iu0QiSbdQ9pT33oIM4B78v4xFoa7QDWrR2k-Fk1zku3UWpky0OqoTw34vEgg5_WwQtZsXnBTzK2zCFDR7e_WKIOcKgwLW28e1meUqUqGH3c6bftOzJK2u_zBtEnoeAR7BZrdRr6r0XOt6WJTUCCaS9RRZFu2743x7oCJgPBgP1fnEFk6LN38eya2XhAILH-Q-unIP_MjdxA8UO6M5wcRd0qixfY66euiVyHMC86NPoD6XR_1CG19S755hKxh_VivMJiyVEvveGiAClp0LOMZXCQORf_z-3QPRaA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pG1Jz4Mz90q2wxPSSoUZsmcX2zEmWBr6H_W5PwEFPEGW4PDi015lmmHTsElSBYYqjf6yhy0_gVBxx_YbafRMxTOka34j6a8R9wNmpelUaI6eYwzXmTLzs1BflqpP8Nn9HbSIPXLEZlQALtHPxAIVlzQFWlGV3Pj1S0GWkdD8Hz4FgAjyrbF_AbJAN1IvCwkmrSrbI3ViHZksZiimlD9ed7tP1sr2qjbs2c17I_lz_rcZK_3WM8IYJxvbf4bQ7U42z0UhvZqaKsIH7SO-vtPAeNJkVNobCbrmYiFdu8r5VME_97RgvuGglxPFzPzqaOvOrpOrTIeDCCDfze4j66vE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Af8TxWUsIRwj8ArEAtEE9bh5YJhDWAOm3lhXkheHxHJpdggTz7QRIP9osdtHsEmaCXnieU_S06WcB6IBpo0EhKNuTfYTj5mXpk21cdE5emv1ooWgK94p0auefwwJ8rBIus7g6fpMzZddDz0JXDQ4BeC2lTLbsfZKY0kH6fvQDyRy-Mf8X0taN36V7OpGYpBqYNvKItWVuZswXBIViH1lxC5YTNk0bf93czDVJuUcT8SfBH1QFc9XuX6943o7pU2ejbK8-e-xs8d6vaHuAqun_beYJvNTK-rByjYqI8hpVv1Q7Ivx5AalkLTDS5bWrGU7aIWtkM0AdkVhF8V3EUhLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mbg5FofsAtHurSHKbRZgz-Xfysb8nII9JpnEydtWQzfKX8zsSG3MzaZFIvCnofE7UIBVzFGiu1CKXUfoV1aL9e-eigwNdE9p4RFyFqxvErVY6IreDGR5e0-BaZ9l8tk6OFRsYWKJ72S7rir0XuKHWNEJwIMt4kaGECi79J_v_PlCyZpHQ4XVqmuUTlflibHJ7xQvYj2BynHRlX7CpCnqA9YQ1wT3J-D53saR-BQOkkhv2pzgHxTHbtPogjWtYTqM9ofkWN2aQAhPyNh43xckq1m9qsoxNwOLL6_pnehgp6OjFCHKmZ_wIKIv1V8Se16nou1C7RvnTDlTENpKiGBgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jRc7nxsKt2HiocgeaFc7JkEgTVnxaObLY7Ian6gozN_-1vxiZe0tFvrR5HxcAW7DYkjU5vROY_pya-HDKaImVw4jC4BXq59eJP9Ivw5VbJXHXIXX4GNL3V9ucdDH5J4YqtdW9LJfPHsUVvt9ZGc2UyWq-c6Vpy3g3iYA3i-0MBXZ6Tb6b6jqCYV_Y5gPs1mPdGxyM09rDQd68hsAZggqFpAWJ_BMtBFE-J8RpcRDpAIgfeolAurlJF9I8GGIsEDLzFiqZmrm1XE1kOqDKjxR4Hyzb9Kc7ntL0XGbAfx-oYzxiqYcsmuwfFfm_uZQX6J1iN2zMpeK3x6Vu2GmZxZ9pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uyoAf6MSmuLSo9Xhox0QqkCJBAYfSTl--_wCIxTkbYxO9cTkMcTWGjWC1he5SckY4MqvVJoC_A7xh5BlBSDPqN_i4ll2DdzNd0IBYNKX653G162mBb0DQ5mzI3LeR666sus53PC5i6jsSoGc0ZW7DO7U-Wc6G30zFWB0r7C4KNoqikkuFCl1IXGhSdFnA8H6jTu7GPsOGVcQYdsm1-D8hm-hsqKOzOVbXre0blbiwiDz2gVMzbFU_eZdyxfO_YYUj2ZLjPnO1G_h0e2tNGA6QYKXVLyJ9MW7NPoOpNFkEu1k25WsusAkSgl9W16AiIbCgvc2-6NynoVPJyn2h7S3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bw3kGGhsJ3OiYLXuzCAqQ2p7WHHvP_QrOZV20n5ByZKQG3XGJCXUIJNDxvj_Vka9S2MsJjQqBix-YuVbq93rFpY6kDFhdRMI3HQZDPpoEYLhHXx3GBMNfD8F6bFasivZyrEykXieDWQqvJJHXhWgMrtEfi2CNbzg_8SdHLhB21xDYfQOTeO_naRBy4Is8D0h47hgxv8nbpA9UGUMjEHigEpfzdt2HyTTWYWLVuk14UFf0VNeb4TgxGknBJK3YHhhGTaNuhYwWtIKdyIHo8j4LRlFVkN9UkiGgj-0TWCIZjS2bOyhYd2C7Oq421hCcd1ZAOjG-slwuqbF9WZWwyA7eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YTVJmbIGjOIWS7Sltgh6mJCfyETu5VlGq9V-XkeSRR8fu2jDKLmVd3XVzw8aMT1HkJYcdv2hRdBth4DYi0S_D_Oqkm9R8931t1WkpEE0pTkLTo74HeK72fjqwdbcNr-iboMs8lrdimtCkPhMwxgchKNIcKD9bkj3K5bdbB78WJhn8CufiTvbwAt1Ljtwm3rFrCxwh6yo46FIClo2FR5uFjiijttjn9ZhsZczJ9qdp4shS7E8i9hfX-NjUZ9nVjLgY_prcQpL62ecpf8rj4sRPYrHpQf5JuCLULSzSt6b1y4ZVrPoB94nfnZpTpcxW4LM2QmroUUx5Vy7S8OFkbeasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77936">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nc3tC7dTD37YEReleqclAsBdV-cdOoRdp-c8B7G38Vm6zO9qR4SkDRUp6CCW_onLa2MouCDYsb2TVZycRwu-QDVtxpcigQU0G756co1buMhhFLI0VHw-CEEuB8DaRzlxS3ATkhChecMEUTXK9jlnFJ9hKhuBkT-IyNuHhgBvUqcSgYsw3nApz44wd7gelCB26oEW5TaQpmi_j5PRURqyajrfBDxeB8evkQNZFoVfThYfTwFhkkFldQBbIyESCtq_0eO_7ZY7DRnjPv6nU4tGnCkoSdZneBb0tkHpPIsS4c14900Yxx5BIfCy7lSgPr6b-xcYTqSTRyWT1nkLWAjcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه ۲۷ مرداد در پستی در شبکه اجتماعی خود، تروث سوشال، بار دیگر تنگۀ هرمز را «قلمرو ایالات متحده» خواند.
دونالد ترامپ با انتشار پست تازه‌ای در «تروث سوشال»، یک تصویر گرافیکی را به نمایش گذاشته که در آن، تنگۀ هرمز، به‌عنوان «قلمروی تازۀ» ایالات متحده نشانه‌گذاری شده‌است.
او پیشتر هم در یک سخنرانی با لحنی نیمه‌شوخی و نیمه‌جدی، این آبراه را به‌عنوان بخشی از قلمروی ایالات متحده معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77936" target="_blank">📅 16:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77935">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZAayLoUB-Twq0R3wcOUEZHyIofc2K5B-Vxof-hsZtOX5Ac_meOsSSvcu_vtalRnF-vQURVWJ0XHpwmWPjshuGfFs45h7-Lth99AI5Hn_XxMhz1YwfaUy8zxnEnPaHc62YS6BZON0rUTAj2BYcu-K3sU1hmOVkW68LayxEe4eNQezXt-qIlvwlNfZL4eHKbOtTi3PzeKcy2cPkDUTSOFaTS113H1I4LDXu4JAhsxDoRXeiPH2vwkdKm9tS35XkAgfrOvhp3p_H0LIHXTJnpPddMjdo4m2CiQqIRaEX1W5oc7ZAsNgLopndbkKuq37zibmVjU-3ODeKV7661yO0b006g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر درخواست جمهوری اسلامی ایران برای ورود کمیته بین‌المللی صلیب سرخ به موضوع خلبانان ایرانی را «ترفند رسانه‌ای» خواند و گفت ایران هنوز به دعوت این کشور برای بررسی موضوع پاسخ نداده است.
ماجد الانصاری روز سه‌شنبه ۲۷ مرداد گفت «دعوت دوحه از هیئت ایرانی برای سفر به قطر و بررسی این پرونده همچنان پابرجاست، اما تهران هنوز به دعوت دوحه برای اعزام هیئتی به قطر پاسخ نداده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/77935" target="_blank">📅 16:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77934">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=IOhrmEqVtPjPUfZe3h7C1a0EV04_x0mhRw32CSfBJ-6CvYY2Bi8gOk6QDpHzGxeHoSq790lD6YshJ3ZP-xaBzGJO6UjHZD6mMpvzpwe_FZ0b-1-lif7ODFXLTW8Q5YNsIAe7WBP_nL4cBudjONJSIcWrA-7IhUKVnsURWvkqNc3vqa87EuPpzWJiKrknlEkG94GAV_DFetLdmgc0V9XxxOFQ7cNAZZXS1ApgOgrhlVn7Y1KnRDBRI81xTOMrmAnWqm5KRxZPWN8QXWgdaQ7UJcEgpUhziBLkM2FX2pe60yEMyfk9A5WT4dJsR1nIEldIJqJW_M_0IxAppFXQHxcdZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7722d713c1.mp4?token=IOhrmEqVtPjPUfZe3h7C1a0EV04_x0mhRw32CSfBJ-6CvYY2Bi8gOk6QDpHzGxeHoSq790lD6YshJ3ZP-xaBzGJO6UjHZD6mMpvzpwe_FZ0b-1-lif7ODFXLTW8Q5YNsIAe7WBP_nL4cBudjONJSIcWrA-7IhUKVnsURWvkqNc3vqa87EuPpzWJiKrknlEkG94GAV_DFetLdmgc0V9XxxOFQ7cNAZZXS1ApgOgrhlVn7Y1KnRDBRI81xTOMrmAnWqm5KRxZPWN8QXWgdaQ7UJcEgpUhziBLkM2FX2pe60yEMyfk9A5WT4dJsR1nIEldIJqJW_M_0IxAppFXQHxcdZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی و مذاکره‌کننده اصلی با ایالات متحده می‌گوید تهران تا قبل از رفع محاصرهٔ بنادر ایران توسط آمریکا و انجام برخی شروط دیگر، تنگهٔ هرمز را بازگشایی نخواهد کرد.
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس، دیگر شروط ایران برای بازگشایی تنگهٔ هرمز را «آزادی اموال بلوکه‌شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه‌ها و دیگر شروط» تفاهم‌نامهٔ اسلام‌آباد دانست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/77934" target="_blank">📅 16:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77933">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7a2Wh5sKKYnfMT0may8kpnweGwoPS4lY62O0mLcuB8m87entLx-_PM5Gf8J_W67AKN4mBixf0RFoJnFKCeGlRFEiYCtVTuYWRPKgEDIuAIgh1319540RBKbEvOF-drPUhFxGYXJbM0WU8kVnPl9KTRIodL8Mr5iQiRwqeN1YW8gZUmSBaVNZNx8I2uAQIPc7VXrgGCM08drx2_IPtL-094QTiuxbAcovcdDr3cG-aRZ02mps_5QEQJ-cWPKjbNNx2RC8u06Gz1I1jNzJvLI0-IRzfTLK8eZ48BzEXL_w7IngUksDrsiXQm8rgSOoZym0yhxorGH4b8uuxJj_9jqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آنکه دونالد ترامپ کانال ارتباط پشت پرده آمریکا و سپاه پاسداران را تایید و دولت ایران و سپاه آن را تکذیب کردند، شبکه العربیه به نقل از منابع آگاه جزئیات جدیدی را از تلاش‌های نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، برای برقراری تماس بین آمریکا و سپاه گزارش کرده است.
العربیه به نقل از منابع نزدیک به ریاست اقلیم کردستان عراق گزارش کرده است که آقای بارزانی در تلاش برای کاهش تنش میان تهران و واشنگتن، دیدارهایی با مقام‌های باندپایه ایران و آمریکا داشته است، از جمله دو دیدار در بغداد با اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران.
به گفته منابع العربیه، آقای بارزانی میانجی‌گری میان ایران و آمریکا را از اوایل ماه مارس، یعنی چند روز پس از شروع حملات آمریکا و اسرائیل به ایران شروع کرده بود.
دلشاد شهاب، سخنگوی ریاست اقلیم کردستان عراق، دیروز در پاسخ به پرسش بی‌بی‌سی‌ فارسی، تماس‌ بین آمریکا و سپاه از طریق آقای بارزانی را تایید کرد:
«این خبر از یک جای قابل اعتماد منتشر شده و نام برخی افراد به عنوان منبع در این گزارش مطرح شده، ما هم همین اطلاعات و جزئیات را داریم، همه آنها صحت دارد و ما هم تایید می‌کنیم. من فعلا اطلاعات بیشتری جز آنچه منتشر شده نمی‌توانم بدهم.»
خبر این تماس‌ها نخست در وبسایت اکسیوس گزارش شده بود.
سایت خبری اکسیوس به نقل از منابع آگاه گزارش داده بود که آمریکا حدود یک ماه پیش از امضای تفاهم‌نامه با ایران، با میانجی‌گری نچیروان بارزانی، رئیس‌ اقلیم کردستان عراق، با سپاه پاسداران تماس برقرار کرده است.
اسماعیل بقایی، سخنگوی وزارت خارجه ایران دیرور به خبرنگاران گفت: «خبر برگزاری نشست محرمانه میان ایران و آمریکا در اربیل کاملاً ساختگی است.»
حسین محبی، سخنگوی سپاه، هم در واکنش به اظهارات دونالد ترامپ که وجود کانال ارتباطی پشت پرده میان آمریکا و سپاه پاسداران را تایید کرده بود گفت: «این دروغ ترامپ، صرفاً فانتزی‌هایی است که به خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77933" target="_blank">📅 16:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77932">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=DSyBwfuS-ECsb3r64hHLXZYZ3mfDUnjJR9t1RVQr3bZZbkHeWZ7ItJ92zdH9x9h3J-65ASA5nSPV5NvzTVPYfFf2XEiG1sW33Sr_0ZFJZBJ-NTJYR_CNAnoMTEcAL9AIX_kYqNt0st2qPzXa7VUJqJahTHCHr0zDedEk5Qw11Llsz9-_P6V4ujra67DAAiagdOFI8_b6vHi1p9sqGf6-mMilHBk2uzYjxC04NHS1oBSP3EzmzzOVnk694V9gtb94-5yueF9t9L85-b3aXHfPa1gbBZy7v5Dms0FyICnlrfsIsnGFAAga5c4sicwO5ui4DLZ07Mn75UF4EEFmeXcJZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ff868c2485.mp4?token=DSyBwfuS-ECsb3r64hHLXZYZ3mfDUnjJR9t1RVQr3bZZbkHeWZ7ItJ92zdH9x9h3J-65ASA5nSPV5NvzTVPYfFf2XEiG1sW33Sr_0ZFJZBJ-NTJYR_CNAnoMTEcAL9AIX_kYqNt0st2qPzXa7VUJqJahTHCHr0zDedEk5Qw11Llsz9-_P6V4ujra67DAAiagdOFI8_b6vHi1p9sqGf6-mMilHBk2uzYjxC04NHS1oBSP3EzmzzOVnk694V9gtb94-5yueF9t9L85-b3aXHfPa1gbBZy7v5Dms0FyICnlrfsIsnGFAAga5c4sicwO5ui4DLZ07Mn75UF4EEFmeXcJZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید که افزایش قیمت بنزین توسط دولت مسعود پزشکیان «تدبیری حساب‌شده نیست»، چرا که به ادعای او، «دشمن» برای این مسئله «برنامه‌ریزی کرده است».
محمدباقر قالیباف روز سه‌شنبه ۲۶ مرداد در نطق پیش از دستور مجلس ادعا کرد که «بر اساس اطلاعات پیدا و پنهان، دشمن مترصد ایجاد آشوب و ترکیب آن با عملیات‌های نظامی مانند ترور و اقدامات تجزیه‌طلبانه است».
او بدون ارائه راه‌حلی تأکید کرد که مشکل کمبود بنزین باید با برنامه‌ریزی جامع و بسیار هوشمند حل شود، به‌گونه‌ای که «بیشترین عدالت وکمترین نارضایتی را در مردم ایجاد کند».
مسعود پزشکیان، رئیس‌جمهور ایران، روز ۲۵ مرداد با اذعان به تأثیر محاصره دریایی آمریکا علیه بنادر ایران گفته بود که راه ورود کالا به ایران بسته شده و دولت منابع لازم برای واردات بنزین را در اختیار ندارد.
بر اساس آخرین آماری که دولت ایران منتشر کرده، تولید روزانه سوخت در کشور بالغ بر ۱۱۵ میلیون لیتر است، در حالی که مصرف آن به ۱۲۹ میلیون لیتر رسیده است که نشان‌دهندۀ ۱۴ میلیون لیتر کسری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/77932" target="_blank">📅 16:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77931">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WBWm8Ibbb5JuoRldCmN1BgNFzftWJkKLU6nhxX8uFzrXjdYGzOCb0wY8ddFSWwGVviewVZAzWkpJdtOp1gxUPbbW6EE4GLj5aAvVee-XmYL_ZVy9iQsl7R2JuvpHcRRoCzfDRtz7GjMRZD6RwZ0bjpho6vqfBmG2yLypplRsNqQW6A2WylW_iIrfxMI0TjHswK6Rz82cEfjvueq1HwdRbAa4nrouqVVgQ0Y1VKW6t7Zt_0nP2TSrDE2oqNl88qzAjQ_FGd1NmRfJGFgv3l-AXyz3jPtSckA2m6dtCEdRYGRWUJC0nSPkev96NeUIZPwmb3g7wmFEWvKXT2-YdGEQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک منبع مطلع به ایران اینترنشنال گفت که محسن (مهرداد) تکش، شهروند ۳۳ ساله در اصفهان در رابطه با اعتراض‌های دی‌ماه سال گذشته با اتهام محاربه به دو بار اعدام محکوم شده است.
تکش، ساکن دیزیچه اصفهان، در جریان سرکوب اعتراض‌ها در هفته آخر دی‌ماه بازداشت شد.
منبع مطلع گفت که او در دوران بازداشت به‌شدت شکنجه شده و دستش بر اثر شکنجه شکسته است.
به گفته این منبع، تکش تحت فشار و شکنجه ناچار شده اتهاماتی را که بازجویان به او نسبت داده‌اند بپذیرد و همین اعترافات اجباری، مبنای تشکیل پرونده و صدور حکم علیه او قرار گرفته است.
خانواده تکش تا حدود چهار ماه پس از بازداشت، از محل نگهداری و وضعیت او اطلاع دقیقی نداشتند. او پس از چهار ماه بی‌خبری، از بند الف‌ط زندان دستگرد اصفهان با خانواده‌اش تماس گرفت.
منبع مطلع به ایران اینترنشنال گفت به‌جز اعترافاتی که تحت فشار و شکنجه از تکش گرفته شده، هیچ سند یا مدرک دیگری برای اثبات اتهامات مطرح‌شده علیه او در پرونده وجود ندارد.
محسن تکش پیش از بازداشت، در دیزیچه یک تعمیرگاه مکانیکی موتورسیکلت داشت و از این راه امرار معاش می‌کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/77931" target="_blank">📅 16:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mxHG2ODEW4YkFkRNmnPt4iX2MU--3KAmbU-or9VzSKpD8zX68i4WdonVB0zcCB_nuzp-M7DM14tODBppYZpfJw_AiQ4GhIkbg2nPaWlCEwecSYlKU7qw1xo-457r0HF7LNpU6HbNxzf1oFA02sWEvbI43O3zLAbpCYnKJIPn1onjgDAWILCbf8TcBIk1usZds8UUbH93Ysnv1m9HyKoVVE_FhYURInBo-gZlhKqrq0Sd1EFHiCqVaEcAInAXBL0zLMtlKJfkuN2qzS_MWoBpM2Asxg0ici9i8f7vj7_qQXG8wMSMHjP5EhUyTSPy9qpSWHuzDPHmQ6BD1kKOaxkCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
افسر امنیتی شرکت گزارش داده که یک شناور هنگام عبور به سمت خارج از تنگه هرمز، با پرتابه‌ای ناشناس مورد اصابت قرار گرفته است.
این برخورد به موتورخانه آسیب وارد کرده و باعث مصدومیت یکی از خدمه شده است.
در حال حاضر، گارد ساحلی عمان در حال کمک‌رسانی به سایر خدمه است.
تاکنون هیچ پیامد زیست‌محیطی گزارش نشده است.
مقام‌ها در حال بررسی این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77930" target="_blank">📅 07:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nLkfyCrtcnFFeCMaLqryPl8jSabSg8BpPGpShLg_K1hMh83Jw1CpltLmmaUp6G7wcLq9TrU5USad9w9PMm29ZH1dWeMmiWbruYseQ87vppnebZRSKPPY3-17qaW8FEkcTYymsL5L_us4GJzwwOBIr1eP8V2qn7zWTkU0EEXTmAIJhPiWrIO81HiuR8dBwJG9AhgoaMUPpdIXPgeNBRhQIJav6vuuYA7MtkZut-LtODYGUgBg4nKaLNPiWBxhvF-7DeiSNy6MLMJgTFIIe3oKNHpUupMW1UTdHrARz46PGUwu5FgWRb9dylrpN3cb-74BYmL7AmXnFHHFfcJCZiU7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه فدرال کانادا در حکم نهایی خود درخواست سلمان سامانی، معاون و سخنگوی پیشین وزارت کشور جمهوری اسلامی در زمان سرکوب اعتراضات سراسری آبان ۱۳۹۸، برای توقف روند اخراجش از این کشور را رد کرد. بر این اساس، اداره مرزبانی کانادا موظف است حکم اخراج او را اجرا کند.
سامانی پس از استعفا از سمت خود با ویزای توریستی وارد کانادا شده بود. این در حالی است که بر اساس قوانین کانادا، مقام‌های ارشد حکومت‌های ناقض حقوق بشر حق حضور در این کشور را ندارند.
سامانی در درخواست خود مدعی شده بود در صورت بازگشت به ایران با «خطر شکنجه، اعدام یا خودکشی» روبه‌رو خواهد شد.
بر اساس حکم دادگاه، قاضی این ادعا را رد و اعلام کرد سامانی در مصاحبه‌های خود از عملکرد وزارت کشور در آبان ۱۳۹۸ دفاع کرده و هیچ مدرکی وجود ندارد که نشان دهد حکومت ایران او را «خائن» می‌داند.
قاضی همچنین تاکید کرد منافع عمومی کانادا در جلوگیری از تبدیل شدن این کشور به «پناهگاه امن سرکوبگران»، بر ادعاهای سامانی ارجحیت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/77929" target="_blank">📅 07:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VOxofoMb-3Usd9T5Ev5vt-mT0Xl7AStSD1cE8VH9TRuFsnJPiHfPTrgHdVznSaTaWL-jCJcbhzn_6f_AZ-eCnrRzJPZdGrCr4ja5HBQbJZY-61HtSHrr_aRuyvRFU36FIVah-cwt9GWXCrLhS-spHBvtu6AK3McpMYWNo3tFmik0m9PiFcx3A2yzCBqGxPzbxJEpZMY7ez84WWoavNMdrrG9D5dTTZ6BUFaGbb7cmoQpSohcHydVunzKcEwQ2RTWZBwMAUC9Pbu_kNkfZ_ybztkG0tz6KP2FgKdGF7KPBe77jExcE95DOOdpk4sKHr-opcCeSsWWExsSU5DeXBAFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، در گفتگو با دونالد ترامپ، رئیس‌جمهوری آمریکا گفت که ادامه گفتگوها با ایران برای بهره‌گیری از دیپلماسی حائز اهمیت است و ترکیه آماده مشارکت در این زمینه است.
دفتر ریاست‌جمهوری ترکیه اعلام کرد که در این گفتگوی تلفنی رجب طیب اردوغان، آمادگی آنکارا را برای حمایت از تلاش‌های صلح ابراز کرد.
پیش از این جرد کوشنر، فرستاده دونالد ترامپ، رئیس جمهور آمریکا، گفته بود که گفت‌وگوهای ایران و آمریکا جدی و فشرده است، اما دو طرف هنوز به تفاهم نرسیده‌اند.
آقای کوشنر که داماد دونالد ترامپ هم هست، به فاکس نیوز گفت که مذاکرات آمریکا و نهادهای مختلف حکومت ایران احتمالاً قوی‌تر از همیشه است، اما دو طرف هنوز به نتیجه نهایی نرسیده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77928" target="_blank">📅 07:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=dbaoF3mHTYWN7xMnsfddv9t3b8YFrcejsyv6KqAT6qTkBLt9qDUemv3az5N4t40WoeingqBxjgm2ukywtygzXS5frUzZprBC7e3ZXpzHYoxfCl1Dq9xt2kJ-nMbVNj-2p1uAVowsr2AT0td6nwPC8fDmsNvcAO0YSCUMPILkgd2phiX_aC4PgnePEWY_1oC7hMw6KbBccQbsDg-MdiXQcgLREdMFXeE0MhLHEQZrI8WDoopUoxAQ1FbQyHdwzt43s021z7egBXgytLUpCMiLELAg3N9RLio01u31HoB2GNUDyNIfxFus1f2-7nfEtdHs_3MFWM9faY1J0dmSTsyDUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e635bc1048.mp4?token=dbaoF3mHTYWN7xMnsfddv9t3b8YFrcejsyv6KqAT6qTkBLt9qDUemv3az5N4t40WoeingqBxjgm2ukywtygzXS5frUzZprBC7e3ZXpzHYoxfCl1Dq9xt2kJ-nMbVNj-2p1uAVowsr2AT0td6nwPC8fDmsNvcAO0YSCUMPILkgd2phiX_aC4PgnePEWY_1oC7hMw6KbBccQbsDg-MdiXQcgLREdMFXeE0MhLHEQZrI8WDoopUoxAQ1FbQyHdwzt43s021z7egBXgytLUpCMiLELAg3N9RLio01u31HoB2GNUDyNIfxFus1f2-7nfEtdHs_3MFWM9faY1J0dmSTsyDUoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان ترامپ، بخش‌هایی مرتبط با ایران،
ترجمه ماشین:
🔻
خبرنگار:
درباره ایران، امروز صبح گفتید اگر عمان مانع بازگشایی تنگه هرمز شود، حسابی عمان را بمباران خواهید کرد. آیا می‌شود گفت صبرتان در برابر عمان، این شریک راهبردی، تمام شده؟
🔺
ترامپ:
نه، فکر نمی‌کنم خیلی خوب رفتار کرده باشند، اما خیلی راحت با آن‌ها برخورد می‌کنیم، مثل کارهای دیگر.
🔺
ترامپ:
وقتی اخیراً با رئیس‌جمهور کره جنوبی تماس گرفتم، که از او خوشم می‌آید و واقعاً فکر می‌کنم آدم خیلی خوبی است، به او گفتم: «مایلید کمی به ما کمک کنید؟ ما برای ایران به کمک نیاز نداریم، اما اگر مایلید، درباره ایران دستی به ما برسانید.»
گفت: «نه، ممنون.»
من گفتم: «یک لحظه؛ ما ۳۹ هزار سرباز آنجا داریم که از شما در برابر کیم جونگ‌اون، همسایه کناری‌تان، محافظت می‌کنند و شما نمی‌خواهید در یک عملیات نظامی خیلی آسان در ایران به ما کمک کنید؟ این عجیب است.»
گفتند: «نه، نه، ترجیح می‌دهیم درگیر نشویم.»
من می‌گویم خب، پس چرا ما درگیر کمک به شما هستیم؟ من می‌خواهم به آن‌ها کمک کنم، اما وقتی از کسی می‌پرسید «مایلید کمی به ما کمک کنید؟» و می‌گوید «نه، ممنون»، بعد ما داریم در برابر یک کشور از آن‌ها حفاظت می‌کنیم و خودمان میلیاردها دلار می‌پردازیم؛ این کار برای ما میلیاردها و میلیاردها دلار هزینه دارد.
نه فقط برای آن‌ها، بلکه برای کشورهای دیگر.
به ناتو نگاه کنید. ما صدها میلیارد دلار هزینه می‌کنیم تا از اروپا در برابر روسیه محافظت کنیم؛ صدها میلیارد، عمدتاً در برابر روسیه، اما در برابر چیزهای دیگر هم.
بعد می‌گویند نمی‌خواهند وارد موضوع حفاظت از تنگه شوند؛ همان‌جایی که بیشتر نفتشان را از آن می‌گیرند. آن‌ها ۵۰ درصد نفتشان را از آنجا می‌گیرند و نمی‌خواهند درگیر شوند. پس چرا ما این کار را می‌کنیم؟
تمام چیزی که می‌خواهم انصاف است.
🔻
خبرنگار:
با منقضی شدن تفاهم‌نامه، آیا امروز به رسیدن به یک توافق نهایی برای پایان دادن به برنامه هسته‌ای ایران نزدیک‌تر شده‌اید؟
🔺
ترامپ:
خب، آن‌ها می‌خواهند توافق کنند، اما قرار نیست آن نوع توافقی را که من ضروری می‌دانم انجام دهند.
ببینید، ما فقط به یک دلیل آنجا هستیم: ایران نمی‌تواند سلاح هسته‌ای داشته باشد. متوجه هستید؟ ایران نمی‌تواند سلاح هسته‌ای داشته باشد و سلاح هسته‌ای هم نخواهد داشت.
و همین حالا، اینکه آن‌ها بعد از کاری که قبلاً با بمب‌افکن‌های B-2 انجام دادیم یکی بسازند، قرار است... قرار است خیلی طول بکشد [نامفهوم].
اما ایران نمی‌تواند داشته باشد؛ خیلی ساده است. آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔻
خبرنگار:
هفته گذشته گفتید که به‌زودی تنگه هرمز را قلمرو ایالات متحده اعلام خواهید کرد. می‌توانید بیشتر توضیح دهید؟
🔺
ترامپ:
خب، به نظرم ایده خیلی خوبی است. بله، منظورم این است که ما آن را کنترل می‌کنیم. با محاصره آن را کنترل می‌کنیم. ما محاصره داریم. با محاصره آن را کنترل می‌کنیم و ایده اعلام کردنش به‌عنوان یک قلمرو را می‌پسندم.
ما کنترل کامل تنگه را در اختیار داریم. حالا آن‌ها می‌توانند دردسر درست کنند. می‌توانند در آب مین بگذارند و مردم خوششان نمی‌آید کشتی‌های میلیارددلاری‌شان به مین بخورد و از این قبیل.
اما محاصره بسیار مؤثر بوده و می‌دانید، داریم خارج می‌کنیم؛ حالا شاید این متوقف شود یا شاید حتی بیشتر باز شود، اما ما هر هفته میلیون‌ها بشکه نفت خارج می‌کنیم. اگر به اعدادی که ثبت می‌کنیم نگاه کنید، داریم این کار را می‌کنیم.
تنگه باز است و قیمت نفت در حال پایین آمدن است و به پایین آمدن ادامه خواهد داد، مگر اینکه تصمیم بگیریم کاری بسیار شدیدتر از کاری که الان می‌کنیم انجام دهیم.
ایران در دردسر بزرگی است.
آن‌ها تورم ۳۰۰ درصدی دارند.
کشور به‌هم‌ریخته است و ارتش کاملاً شکست خورده است.
خیلی ممنون از همه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77927" target="_blank">📅 23:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rPqFL38BCnvU_VnP-ldeAWKbneOTjMcLmRz7aMV9LpHk3gUiGnjEDwkIX_4gUp7Z4-eE2irS5I9RwxwjJOANAR2YJpHVlaUE5CItJae6WYCWdcgvDpQqF0swpxlI_GaY2Y4eXoLTzjWL1fAJ-zL5Z9KgBhqDW4BvH2N5cohPVljtnLOVUWJBRTXfGSqTNURQJm4OnU7TVkuSsYTnUtQRb2KJA7lh_qwTE85F21MgleXC09GbfS4uAQ-r0UudbwGYznZJE6vjM8hxsjlt8QlLFTFaIW4J9FIGNFOf1meSjsyDKrN09u4VaX9eSc5lVgo3T5BFD3G0vmPw_sgjXqpd6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=uPm6MmEpTVK-7HGrGtj6pZNNSW5y5ywfod8NbGKH9cbDS3BiLZAU8joQEGabx-28Px6dyhrhsmn7yPCHcWQHXSBJku3ZoA_a7MabRmAqN6ssLJuqxzIec4zEwHrkqyJsVKD9IamfzcVf1xP8xoVbeKIMfjGJLuWD5lr5DLsaDSZu0Yt25KOR6MwEDz2qywDAz-kTIhvRM6Rtyqw9SHw78_CWODl0Oe7jaa6jDUUtciHyDikLqDY0e2DtXnvWPto-EGiEG-DhH2WFXjr9M46sd7OtBOqUuEwS7u1YYiziMcVpPirjMjYW2AfQBAT8_B4ZFH7K4A83g_LeHubpuWbuWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4485798f8.mp4?token=uPm6MmEpTVK-7HGrGtj6pZNNSW5y5ywfod8NbGKH9cbDS3BiLZAU8joQEGabx-28Px6dyhrhsmn7yPCHcWQHXSBJku3ZoA_a7MabRmAqN6ssLJuqxzIec4zEwHrkqyJsVKD9IamfzcVf1xP8xoVbeKIMfjGJLuWD5lr5DLsaDSZu0Yt25KOR6MwEDz2qywDAz-kTIhvRM6Rtyqw9SHw78_CWODl0Oe7jaa6jDUUtciHyDikLqDY0e2DtXnvWPto-EGiEG-DhH2WFXjr9M46sd7OtBOqUuEwS7u1YYiziMcVpPirjMjYW2AfQBAT8_B4ZFH7K4A83g_LeHubpuWbuWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: آتش‌سوزی بزرگ در میدان شهرداری گرگان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/77922" target="_blank">📅 21:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FCMD5Epu8TRD7MEIfIAeCFssY-_SNDvOvejcpM1eChnG0-erb5arc130Pob-AoJv5_yvx31RBGjev23_J84Gn70nLZWMCtv6L36ER4-FXq1KLFOU2_4MpxlSrOU8QjyY_-vouQ4f5I0JR8GmmkETG1QtPs2JwqPN_SwasjM059E8HxXLy3UaQ016bMwxASDhZwtkE7h5P1PObOu5qzwoLR29K86_jnxwRuIrXPMExSjALJBj3t9OisOWX3tIA5ak0qjCVZJCfuaTtGeQwFPHnEqsLtdFWWYhgYWyMjiyor9iSLU5btv_B-tF7q0sjqJNdUbAR86w0sD0autaLv77Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43c261d593.mp4?token=OoQJtTPrlDkVcz_TjvHrBqkYwtPVXVZCyFkpp1ojXCk6b3gW1nRUsL0wNlnJSsnvVpVhlELAzIxT_WciH3z24MbxLMJgeYBOUCJVLy6uHGNTxnSO5PtCLwBmB6VfnqfXJQcGM2ZABbAgqZqyGDXK37BahLetyMsXUj8_-3-R9ikeUWWAPK0msFEMu08FMxPOZCEmo0IQb-2h5VYfyC6iyTI99kJMYfffi85DauaN9-nadh-G5lv99yQ-FHtrHODwnWhhQ3Z5sXPuywGeY4JweQwL1RrJIUReZhN1sTofqs9uRGZP1y-n438z51g-Jv-Nh-XL15jh0W4jmxhteOzcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43c261d593.mp4?token=OoQJtTPrlDkVcz_TjvHrBqkYwtPVXVZCyFkpp1ojXCk6b3gW1nRUsL0wNlnJSsnvVpVhlELAzIxT_WciH3z24MbxLMJgeYBOUCJVLy6uHGNTxnSO5PtCLwBmB6VfnqfXJQcGM2ZABbAgqZqyGDXK37BahLetyMsXUj8_-3-R9ikeUWWAPK0msFEMu08FMxPOZCEmo0IQb-2h5VYfyC6iyTI99kJMYfffi85DauaN9-nadh-G5lv99yQ-FHtrHODwnWhhQ3Z5sXPuywGeY4JweQwL1RrJIUReZhN1sTofqs9uRGZP1y-n438z51g-Jv-Nh-XL15jh0W4jmxhteOzcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی بزرگ در مغازه‌های دور میدان شهرداری گرگان
تصاویر دریافتی: 'ساعت ۱۹:۳۰ دوشنبه ۲۶ مرداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77920" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JgHQ4oCVhK-eh5q1id3FheK410j7cs3P3aMWdKwpPvrA8vf4O463MuG34BqWQlTDQNfd4mr4nKPn_7Q9L21jVBeEVGuBDaP1X0HK7G_HZOjWXFWPQzW3Q3vZunbEAF6eHhZ-Ixyu48vAdCwKhcnkrIYJrDBuD1vkR95tvLIwB1Z-W00YsYiypUII4G6rp86LBlwiAz3THcRNwe-qmKwrP0oQQWIoq4aPcw6yVtcJNcFOq036JqTJQA15m5bQXFkkg0OjPuf3o0vbUm-beT9ehIP68zHlbdqc92cpXkKSlQ5iogxQci5SSEwuuD2Pr20j6DSgHdopHdnGANNbgL6aSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R9pkaQdyieTg3Addw8D810iPVz_AM4Bdo-7xj-gm4A3F_u6CiS55ygPiG0TBTbUMjmP6gIfcs9OHpJPA8mcwXoR2ABzxRGgcz1hwZ2yn4NEh2AttIG3Ci-RslKWRoNfi7H8rqAolZMlf81qApV3VOM9F6IbLd-CqNjEcDfFX6lsOdmBelnRAMLNgWeA98bDCudN1NrmU9f2oulnFW2vrwi0IUfw2xgP8mpaDnUsg2y9BMjRYtq7XA9Bs3ybYoqX4uOc2rPZnNg-4fPXpQ5Dgt9ifawYMBaaa327mPj02eUMti78twk5KoOjboswUEeN7k1GFLMw00Tr487UW98txpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا، روز دوشنبه گفت که در مورد پرونده ایران عجله‌ای ندارد و به «کانال‌های ارتباطی پنهانی با سپاه پاسداران ایران» اشاره کرد. او افزود: «ما به صورت مستقیم با مقامات سپاه پاسداران ایران صحبت می‌کنیم».
او به فاکس نیوز گفت که «ایران باید پرچم سفید تسلیم را بالا ببرد» و خاطرنشان کرد که «محاصره دریایی آمریکا همچنان فشار اقتصادی جدیدی را بر رژیم ایران اعمال می‌کند».
او افزود: «آنها در پوکر فوق‌العاده‌اند... اما دارند می‌میرند.»
پیش از این، رئیس جمهور آمریکا تاکید کرده بود که «ایران تحت هیچ شرایطی نمی‌تواند سلاح هسته‌ای داشته باشد.» این اظهارات در آخرین روز از مهلت ۶۰ روزه تفاهم‌نامه اسلام‌آباد برای دستیابی به توافق صلح دائم و فقدان پیشرفت در تلاش‌های دیپلماتیک برای پایان دادن به مناقشه بین واشنگتن و تهران مطرح می‌شود.
@
VahidOOnLine
سخنگوی سپاه پاسداران، ادعای «دونالد ترامپ»، رییس‌جمهوری آمریکا، درباره وجود کانال ارتباطی مستقیم و پشت‌پرده میان دولت ایالات متحده و مقام‌های سپاه را تکذیب کرد.
براساس گزارش خبرگزاری «تسنیم»، حسین محبی گفت: «هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست.»
او اظهارات ترامپ را «فانتزی‌هایی» ناشی از «توهمات و کابوس‌های ناشی از شکست و استیصال در جنگ» توصیف کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77918" target="_blank">📅 17:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R81ojUUNqxm8CQgWXXyuTsJwN8d2-TJH3f7q4T9-aTEFteyGoxYb9gE8Z-G7MmDuu6i8_IqhZ2i7Ps8iLDxK0tiBnOdIXHX3MJJEtLNBIimI98j8WRWFhwwruBQsOem_nLsuLmFhqvxe-tiEddkbPZ98syGgq43mpjRPieonqVP_lmTLdInBQM3N3zDYIt2iD31bp_G5zvDqeHXS7Rr88jJ9Mqr2QPjwa8cSqrazUdXnXTH04E60qUs5aAfZrGZXrykUC3_7qi-a5MwTv_tMYOmXhIeHdCDdcF2qUTWkWFSoKMdtGF5dRSgpCIn4FVYNO7M8vxqInqegFWbbKRD-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره مبارزه با تروریسم اقلیم کردستان عراق اعلام کرد دو پهپاد که شامگاه یکشنبه ۲۵ مرداد از داخل خاک ایران پرتاب شده بودند، دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق، و همچنین منزل رئیس اطلاعات این منطقه خودمختار را هدف قرار دادند.
بر اساس اطلاعیه روز دوشنبه این اداره، «دو پهپادِ حامل مواد منفجره از نوع حدید-۱۱۰، از آن‌سوی مرزهای ایران به سمت دفتر خصوصی نخست‌وزیر اقلیم کردستان و اقامتگاه مدیر آژانس پاراستین (سازمان اطلاعات اقلیم) شلیک شدند. خوشبختانه، هیچ‌گونه تلفاتی گزارش نشده است».
مسرور بارزانی در پستی در شبکه ایکس، به شدت «این تجاوزات گستاخانه و غیرقابل‌قبول» را محکوم کرد و نوشت که «این اقدامات به منزله تشدید خطرناک تنش‌ها و تهدیدی مستقیم علیه امنیت و ثبات منطقه است و چنین حملاتی ما را از ادامه انجام وظایف و محافظت از شهروندانمان باز نخواهد داشت».
انتشار خبر این حمله یک روز پس از آن صورت می‌گیرد که وبسایت اکسیوس گزارش داده بود دولت دونالد ترامپ در دور قبلی مذاکرات با تهران، از رئیس اقلیم کردستان عراق برای برقراری ارتباط مستقیم با فرماندهان ارشد سپاه پاسداران کمک گرفته بود.
@
VahidHeadline
اسماعیل بقائی، سخنگوی وزارت خارجهٔ جمهوری اسلامی، این رویداد را «بسیار مشکوک» توصیف کرد و خواستار «هوشیاری بیش از پیش همهٔ طرف‌ها» شد.
عباس عراقچی، وزیر خارجه جمهوری اسلامی، نیز در گفت‌وگوی تلفنی با فؤاد حسین، همتای عراقی خود، گفت «هیچ اطلاعاتی مبنی بر آغاز این حملات از داخل خاک ایران» ندارد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77917" target="_blank">📅 17:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=Ed_BeL6HMeuSjOJ5KB8cP3pdl85zgOON7jP98yXmBSmLuAroyTvCul04BV58mq4WKSz0Y1f3WDrXXMWRsdJoVTwlfoQS6LqjSuxifclQsxjHddmQorKiCz272jYOHWER0OYz77Z4al0ipnLm1IJO5QrSB8sQpeugN0Lysqe7ue9s-Dca1t-LaEgOkGWuEO8Jh1SOBjYi2L2smsXp39WPr0I0LQNjMdBt_KFiXFGsIb6LvJCUDKGVfaoIGJCgTIjMa1YnDHqJvFmGe2IwkpUkBz2xa72SUDycjSH02zlBGPe9nHpCwPeaIaINCsCwbjJ5X83sYwScClbt-ARtNIm_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d5ca5b6b3.mp4?token=Ed_BeL6HMeuSjOJ5KB8cP3pdl85zgOON7jP98yXmBSmLuAroyTvCul04BV58mq4WKSz0Y1f3WDrXXMWRsdJoVTwlfoQS6LqjSuxifclQsxjHddmQorKiCz272jYOHWER0OYz77Z4al0ipnLm1IJO5QrSB8sQpeugN0Lysqe7ue9s-Dca1t-LaEgOkGWuEO8Jh1SOBjYi2L2smsXp39WPr0I0LQNjMdBt_KFiXFGsIb6LvJCUDKGVfaoIGJCgTIjMa1YnDHqJvFmGe2IwkpUkBz2xa72SUDycjSH02zlBGPe9nHpCwPeaIaINCsCwbjJ5X83sYwScClbt-ARtNIm_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از صحبت‌های یکی از مجریان صداوسیمای جمهوری اسلامی که می‌گوید «جنوب ایران، فدای جنوب لبنان»، در ۲۴ ساعت گذشته در شبکه‌های اجتماعی فراگیر شده است که با واکنش تند کاربران همراه بوده است.
خبرگزاری صداوسیما روز دوشنبه ۲۶ مرداد با بیان این‌که این صحبت‌ها «تقطیع» شده است، ویدئوی طولانی‌تری از گفته‌های ریحانه قاسمی‌زاده را منتشر کرده است.
با این حال، آنچه در ویدئوی منتشر شده از سوی خبرگزاری صداوسیما هم دیده می‌شود، همان صحبت‌های پیشین است.
در این ویدئو، مجری صداوسیما در واکنش به انتقادها درباره حملات هوایی به جنوب ایران، حرف‌های منتقدین را «دلسوزی دروغین معاندین برای ایران» دانسته و تاکید می‌کند: «جنوب ایران، فدای جنوب لبنان».
در زمان حملات هوایی به جنوب ایران در ماه گذشته، بسیاری از ایرانیان در سراسر جهان با مردم جنوب ایران به ویژه مردم بندرعباس ابراز همدردی کرده بودند.
@
VahidHeadline
با توجه به چرندیاتی که قبل و بعدش میگه به نظر می‌رسه منظورش این بوده که مخالفان جمهوری اسلامی درباره جمهوری اسلامی این رو می‌گن که جنوب ایران رو فدای جنوب لبنان کردند.
اگرنه وقیح‌ترین‌هاشون هم درباره مسائل ملی مردم‌فریبی می‌کنند و این طور صریح نظراتشون درباره «ملت فدای امت» رو جار نمی‌زنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77916" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MfDxWIvRLEwArkvF_2WwFpP7-Yuid1atw7Yhv6DFcmPMHrv8c4CcLrTodhWMnzlwBC_bz_alOFRqBXywjN7o5HKnK4cIa_C7xvFM1EzTE7a4GET4uCpoOzdHWhzkAPZ4XFMOtPxz2Rtx31sodUFTiuQ-uXXyMrKEfjSXxdhn0r-VGfNv2OrV6jwpxZPFw39bG4jKGz5X2_t_QoVSKo1d0x8aFX3OLlN4Hicf9HndbJWuKk4ghhtivgKdCjpyf7hmrYuqphcEmZLjixkJ4zJE2cqUUp7iOvUqKnGmRsp_BxCTK_1JulDv-adJmA_NTyaYp_c3nqZEQnpSZYVWUOT4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتشار تصویری از تبلیغات حزب لیکود در شبکه ایکس نوشت: «نگذارید آنها برنده شوند.»
در بنر منتشرشده، تصاویر زهران ممدانی، شهردار نیویورک، نعیم قاسم، دبیرکل حزب‌الله لبنان، مجتبی خامنه‌ای، رهبر جمهوری اسلامی، و رجب طیب اردوغان، رییس‌جمهوری ترکیه، دیده می‌شود.
روی این بنر نوشته شده است: «این بار نتانیاهو نجات نخواهد یافت و ما به او اجازه پیروزی نمی‌دهیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/77915" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mXSxPZ4dweTJ4ZE--wmiZ5Ra0ro6Qz0CMYj6De2G5JNuYv16Z8EdUX26PsGTWxhFioZtNrJCzZ76aQEdnhyj7-tk6k_vDMS_Hz4tGasgortMC2OM0vQbZ0mzV_oyMgyPUYY_VuXowPRRi8fygMXY7U-IIDAAzt8Kx-J7DRMqienqN6osizPf3Ikae2rdzZfNnj9lHPc9kWNCAdHhKv6nCoLzZunKK0sRnC4_KkXGLuDcVnJxLDmkvpCWt025EKxGIyjBH0aZhDkkk_IrQH1YqVu_nxb4SsIEwn5vz59ob1pvDH1RdmPSOFAMzuNohKuH9_o0LBu3jqTOQUT6QFkK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«ملیکا همت‌زاده»، دختر ۱۳ ساله اهل روستای دسک شهرستان نیکشهر، پس از عقرب‌گزیدگی و در شرایطی که به گفته پدرش امکانات و داروی مورد نیاز برای درمان او در دسترس نبود، در بیمارستان نیکشهر  استان سیستان و بلوچستان جان باخت.
پدر ملیکا روایت کرده است: «فقط یک خانم دکتر آمد و گفت سرم می‌زنم و پس از تمام شدن سرم، او را به بیمارستان نیکشهر که مجهزتر است ببرید.»
با وجود وضعیت او، مرکز درمانی بنت آمبولانس نداشت و خانواده با خودروی شخصی مسیر ۷۵ کیلومتری تا نیکشهر را طی کردند و ساعت ۳:۳۰ عصر به بیمارستان رسیدند.
سعید همت‌زاده درباره ساعات بعدی گفته است بیمارستان نیکشهر نیز به دخترش سرم وصل کرد، اما پلاکت خون در اختیار نداشت.
بیمارستان چابهار نیز پلاکت نداشت و قرار شد آن را از ایرانشهر تهیه کنند: گفتند یکی دو ساعت طول می‌کشد. یکی دو ساعت شد پنج ساعت اما پلاکت به دست ما نرسید. تا ساعت ۱۰ شب منتظر ماندیم، اما به جز همان سرم، هیچ خدمات درمانی دیگری ارائه نشد.
ملیکا همت‌زاده سرانجام در اواسط شب بر اثر تاثیر سم عقرب دچار تشنج شد و جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/77914" target="_blank">📅 17:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=f11xeA1uE3zMBOJW82eX8PdByvolO1ZbOYMNWXITeUlqtF8t1tlzkUYl6gFx9pgQh6qaqZ9eI4FZXRdZnOo7Ke0yZ3nIa_hdMNVE8vXU1VY6Dr1BAb7FQqTCz8W6sMumICFXUknCVkLioSE2cpxUIPukjGCACfPTxtArKk-qGlhnk34lAJSG1GhJzI2jpaCSMvdpT7u3CO4LV6aj5-7waqdgB7SAHCWDi9KoL8h8gnSkCCCW9z8pBG1rQKPCONzb1v5TG_mQah-pbN_3YkTPbZBchM_or6IPN2Ccw3YY1R5j29knekr7p_Uandu6LO-9DYjhXSBIs3Ez-4582nxvFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37ca2442dd.mp4?token=f11xeA1uE3zMBOJW82eX8PdByvolO1ZbOYMNWXITeUlqtF8t1tlzkUYl6gFx9pgQh6qaqZ9eI4FZXRdZnOo7Ke0yZ3nIa_hdMNVE8vXU1VY6Dr1BAb7FQqTCz8W6sMumICFXUknCVkLioSE2cpxUIPukjGCACfPTxtArKk-qGlhnk34lAJSG1GhJzI2jpaCSMvdpT7u3CO4LV6aj5-7waqdgB7SAHCWDi9KoL8h8gnSkCCCW9z8pBG1rQKPCONzb1v5TG_mQah-pbN_3YkTPbZBchM_or6IPN2Ccw3YY1R5j29knekr7p_Uandu6LO-9DYjhXSBIs3Ez-4582nxvFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
پولشان بی‌ارزش است. نیروهای نظامی‌شان شکست خورده‌اند. کل نیروی دریایی‌شان غرق شده؛ ۱۵۹ کشتی. آنها ۱۵۹ کشتی داشتند. تک‌تک کشتی‌ها همین حالا زیر آب‌اند؛ در کف دریا آرمیده‌اند.
همه هواپیماهایشان را نابود کرده‌ایم. آنها ۲۰۹ هواپیما داشتند. دیگر هیچ هواپیمایی ندارند. ندارند. و می‌دانید، شگفت‌آور است، چون این داستان‌ها را می‌شنوید. رادارشان از بین رفته. تمام فناوری‌شان از بین رفته. تورمشان ۳۵۰ است.
پول نقدشان بی‌ارزش است. پول ملی‌شان کاملاً بی‌ارزش است. بعد نیویورک‌تایمز را می‌خوانید و می‌گوید ایران وضعیت فوق‌العاده خوبی دارد. می‌دانید، واقعاً باورنکردنی است. تنها چیزی که دارند اخبار جعلی است. همین؛ تمام چیزی که دارند همین است.
اما خیلی زود اتفاقات خوبی خواهد افتاد. در واقع، همین حالا هم اتفاق افتاده‌اند، چون یک چیز هست که نمی‌توانیم اجازه بدهیم: نمی‌توانیم اجازه بدهیم ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/77912" target="_blank">📅 17:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=F4F2GcXKvs6jJGOqVxBTwRkGuHOPonbcjOhXKQaJIOeeOS2f-3X_RAiI7icFNkVHc1H90rI3VlDiaijnZAAGsp2DWeh1TTdAq1toVOcYb2RQVrnlruga4QK3XpzUIaB7FrZC6f--UlbgZAYczIdHYkeeNfuG1KH-oC5M2lpxZQG85pleZTbNsmnPVZPilmbsuP2cnv0w59ZK7am5NsSEKIJFSTK_UgvmTnzjGLhiPIYjxo7p8N6H0QOQx9pY00DAyH_-bpJY9N2bNZhRxcHSRMsFaZsh5-K1ulYQS-vkrIz5fK2JL8E5U4XGLcTnB9i9IMlu2YuiQB6Fc4L5Kg5rbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9e563043f.mp4?token=F4F2GcXKvs6jJGOqVxBTwRkGuHOPonbcjOhXKQaJIOeeOS2f-3X_RAiI7icFNkVHc1H90rI3VlDiaijnZAAGsp2DWeh1TTdAq1toVOcYb2RQVrnlruga4QK3XpzUIaB7FrZC6f--UlbgZAYczIdHYkeeNfuG1KH-oC5M2lpxZQG85pleZTbNsmnPVZPilmbsuP2cnv0w59ZK7am5NsSEKIJFSTK_UgvmTnzjGLhiPIYjxo7p8N6H0QOQx9pY00DAyH_-bpJY9N2bNZhRxcHSRMsFaZsh5-K1ulYQS-vkrIz5fK2JL8E5U4XGLcTnB9i9IMlu2YuiQB6Fc4L5Kg5rbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر قالیباف تفاهم‌نامه میان ایران و آمریکا را «سند افتخار و پیروزی در عرصه دیپلماسی» توصیف کرد و تاکید کرد که ایالات متحده و اسرائیل در جنگ اخیر «به هیچ یک از اهداف خود دست نیافته‌اند» و تهران پیروز شده است.
قالیباف که در جلسه‌ای به مناسبت روز خبرنگار [در تقویم جمهوری اسلامی] صحبت می‌کرد گفت: «با تمام وجود اعلام می‌کنم که ما در این جنگ پیروز شدیم.»
او افزود: «در جنگی ناعادلانه به رهبری ایالات متحده و اسرائیل، ملت ما با قلبی باز و بدون انتظار هیچ چیز در ازای آن، شجاعانه ایستاد و جنگید.»
اظهارات قالیباف در حالی مطرح می‌شود که او جزئیاتی در مورد اهدافی که معتقد است واشنگتن و اورشلیم در دستیابی به آنها شکست خورده‌اند، ارائه نکرد.
@
VahidHeadline
قالیباف: ما نتوانستیم آن‌طور که باید این پیروزی بزرگ را روایت کنیم تا حس افتخار در ذهن و وجود همه مردم، جبهه مقاومت و آزادی‌خواهان دنیا شکل بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/77911" target="_blank">📅 17:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=AXlErL74T7IUlwX-yJGESDq39r-8JS4uyT7ikr8lhEi8yPhKuUNQVJeeCR9Cl313j_CBPHEmuG1fpb-brFL70KaVTeQ89PLR8Ubrj07dIZP3xMy3eizsQWJXAjIyW0HYdB58Ii-MMWWCetJmMDlhek0DhpSRaxL05LGZz14Np_Q34k_bLMq89V2SvFaAP3v4cQU2iKPHFyODh-JjiLMWuzImk7jsjaN5XVzXBpXFnp2DbFF7pDQ2rPmK-x6BKm6jkbfanohxQV9mhnLieQ565G7sXd2hiZ9kic2wgClaUf1Y96NRYPqz2HpD8NYwZirontKp26kiigRkKrRcT5MTJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/557e36e83b.mp4?token=AXlErL74T7IUlwX-yJGESDq39r-8JS4uyT7ikr8lhEi8yPhKuUNQVJeeCR9Cl313j_CBPHEmuG1fpb-brFL70KaVTeQ89PLR8Ubrj07dIZP3xMy3eizsQWJXAjIyW0HYdB58Ii-MMWWCetJmMDlhek0DhpSRaxL05LGZz14Np_Q34k_bLMq89V2SvFaAP3v4cQU2iKPHFyODh-JjiLMWuzImk7jsjaN5XVzXBpXFnp2DbFF7pDQ2rPmK-x6BKm6jkbfanohxQV9mhnLieQ565G7sXd2hiZ9kic2wgClaUf1Y96NRYPqz2HpD8NYwZirontKp26kiigRkKrRcT5MTJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.  این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.  پدر و مادر مهسا…</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/77910" target="_blank">📅 16:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidOOnline وحید اون‌لاین</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKDqV0lmZWdYRYYXmMtBKm_cZ1bYRt3gDUQTNEwz8Md6jlZ8f09P7IkVjIcWBBMUlbgRfAELojFoO5lqAinDCGngdZZRG34KY_luR0wjKSBUu0-_CoL8Pbxx-OlxAX6Hl5gjIW_Z4urFhB-HQ0EdUA8OI2me1l1qZsJw-vANtEjAmaSCSWOMmO9Yzz5b-6EG7reteurSIDUPm6ShYubqpdvwTgO0O0VRp7AnWDO9iXfwvY9GNiUC-I2f8rhlRxjFGO8XBED06beXqGrl__68lmS6QWpwfVbUyJ0Kr7UijALsuNFcHZWFOM-v05JxQ_UZfvWyoJ4yxrdovLiJzquz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSJSZ-OgRyS_eLxZPR3ZAEmDdETe81JWWyTH_6NFqx3GT5QuSSzmBhxF-1X0lgh-jz4pyOecOYIZ-V5KeXsVrkZM8WlrNPyyr_KgW8mAqFX1y5Fg9Oj2jKL-kTlAbuoOD_96vDDVhn71ttSBF9YGNLr72tLvZpLBlAw8Yv6YEXgVGehdSNQgl0BWHulM-Hi81300u1Q-pgo2JS0DP8byZyyjvf6Cin2-d4Pk--eKgm0x7GCnSdM8wWrh9RS6mZdHACDT0iBa8c0zhSn0xSQD5XITMjqrMBawJ5pyKOVs21mVCyLWCXyFJDybwkhAoOs8MDtaH5C5H2BeBNAMCdPqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYbw9uVRa7lFItG4nEcxT4vI4aI8jS_B-5kayifINa9y7pMFiRM4mVYs0aOekZ8mU-mFfN50Gtecw7bTG3y4iNIj6TTCUSydG5LZuUfR1Uh-w1L4LAq9hZyp6cRflVuDmwYbYizT7An3NdPqtdgppDrI48qRq7a9rGMFXL54LsoohCN33puDHJe0qCpwuzvWFtHmza3tFTWijsXENNIxBDxk0QhAIvn1HSs7ZZfzKf8Onn8ZxBnlZA17DqfPFHefUatys_AnCXtb40MgjBlPG9c0a5EYkiIpJCoeEQ4ZKANc5dH5oe4-1uGiwPKYeTF-WiRua5Qu9JwFHb9y6wZTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZtT_KEXfSbnKEe--ubKcuyHOl8cMw00RBSL_GVSGmzyws8Q8llKYjL9gprfrSCqOnkvusTBLXnCgFkjF31mGwQcIzqVn05B-52EXTySeR8MdSQtd0U_n6m_EF0h413JUr5OoAYpVZRj1iTJ_sCgxzkmJ47KqcQPaM-INVuFWLlfKtFi83yNymrGlbnZfiN4aXpC1bPLDnf0hDDSzPoyZCfjHgE0f9XgGQXqdTPAAyoSUYQrPGSAlRU8iQEcP4wIz3EdKN2eOtLVCCLle7oH2e3oFSGMU32nwklpEBi6Tf9f21YOS6Y_TJ8fRg6_d-MW4PqeRtl1NvkvSkJyemTKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JF3jdS-YaqX1lwj_Om7W00VEjCaGMGK8u1G5XpKELeQ-PwIr7O_HHx474clyClypqYGYu3fzA08DM5wxEZkGoeCdYUSOYZgs23-sxXA1CK4ogBm8caw6GuknjC1_C9tT-QhjeZbxTGKPRr9D0Ypz0aKhydsdeDdMNVAhgyOa1U6YtR_bmhUsiq_HzgMs004WxfJg2pj4Rwb5BM11QsUg1qMB9IRDfhv7_I_llY1kwsytvoc5VbMvQogDwJKyrW6F58_u12lkJmqrTvj6fNg5bV2Tvbd9_egftUUhF3oYbaEmvjav_sWXFk_490yb03a20GaKRAa6O8DM_xuV3cSbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7zrH2mN2fBiygbT0qdtSxPesrak06Wo8ODakxnpC8rMOQOQZthkwBF7wpcnLRz5ckGwslALNI1SNZVgietCgkBLwBbUNMR4TBRBNCWlWpeTnMfVx-6kG4f09ao22kXoYUoCWcmAs3UUPoDAtkSYB4RLhRB6v_pHLldFFg8iIVpYhIqI2fo7kPXX3l6SNeOX8WBNvPFoCWMwFg7jY8pn9o_xYXcvUU68ULIwR_HHCXCT5gqO8Ihp8GLjRp15_qd_AP1ExpxF-OhfH8XkcYaBTr5zaz9FOPOq53sAwMNkwv3mVjxZvtS5A2DllDBFMA2JqIUd3C8Se7KeqchOyVQfMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXh4EzLrc5mQ2Xze_oIwz8GyP0aSOBu7fG2h1iVLoJiIE6-UoEPDwPab79XTZB0r8n6xTx5xA1kD1JkV3_zEhgIBYEQ8-OTp3KYz1mWrlRZ2xqkRK3fLL1LHpUxfFunwaZXRxZMV7S6GYDuthYRMubhbQRYZuISYABK6hT8-XNTDXHJE1HTxMZOu_UjxfSQYBNhSt7dE2_2wzqUH7G7JDOenDGfEqpf9d6euVCBSsyrP-EJ0VKZTWItt6wkZVPRx58qUJ2gxSZP5lpoK6BW72D1uudIRhDZh2V8IAqmu7h_e9g_xCOs9r4Z7WC3QXogczCta9EJxE7zSKfvh3IYZmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=sQHhzzEthXSDMs4ft3wlpS-3fHj1e6BA2fzWVFDLVVrAiP2ExKK4kPRC6CRi8jHwnmX3Nw1PasJoWb7P-BkGOP-TZZrwREffn78apwhEeUXbwhFpRB7c6GzOmvU2akKQWFyaomgAJ7JY8Ob1UJuxZ_37D7Foy0cCANxcbWXCndORCVVsMgH1sNItFQwkpXJX9pf_YeYjbCPEzmEyjdw205miCUWi9AuVqteDeyD1ZzP2-jSa4-1-MldJPM7MFwT29jBfTU42cST18CN5FVpmHQNgHVpTM8XP2BLy05w2IgcXfNyEuYUT-xj3vRUnbvSEFIPkLeIGFX7PSSQ9K18M6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1adb18b17.mp4?token=sQHhzzEthXSDMs4ft3wlpS-3fHj1e6BA2fzWVFDLVVrAiP2ExKK4kPRC6CRi8jHwnmX3Nw1PasJoWb7P-BkGOP-TZZrwREffn78apwhEeUXbwhFpRB7c6GzOmvU2akKQWFyaomgAJ7JY8Ob1UJuxZ_37D7Foy0cCANxcbWXCndORCVVsMgH1sNItFQwkpXJX9pf_YeYjbCPEzmEyjdw205miCUWi9AuVqteDeyD1ZzP2-jSa4-1-MldJPM7MFwT29jBfTU42cST18CN5FVpmHQNgHVpTM8XP2BLy05w2IgcXfNyEuYUT-xj3vRUnbvSEFIPkLeIGFX7PSSQ9K18M6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران از نگاه جهان: مهم‌ترین اخبار و تحلیل‌های دوشنبه ۲۶ مرداد ۱۴۰۵
ManotoTV
🤖
@VahidOOnLine</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/77902" target="_blank">📅 16:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N05NGM_PiN9LBMVrxaczPMluuiozEs0vRfmCu-oCKu8FIEpIBo5NlW4jHNHe97F8nt79TlJYgwlYrh1pjy3C-IlcPK9Cwo6DHXVXuGaYYAZS2Mu1ojWh_HtmX0VUnBbbhyASMr36uwvVylLR8gLQY5ryyXFg14JbW050Mp6wU8KcZ_npv0Fn3J8Hz8F0graA1affA0xtIqMbOWQ2skvKDg-IpZJQbqnwdPOimASf17_PoU2GsnOlBa-tbesNfmdOL510Eh2Lz7OWVEDdM0aNQ0ZRG80dk54BvDDfhG1FOm-oTQxsbxcKSpJCt1ZuM_su9Pnlp9eHsUQtn9lA3cEnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArmkpuKNyYlthuVoleYLy_QsyOk1DoS3mXIweMQgYgrK1RIYMiEzr1bV-ThiPwQ-ztOzKfQK2Ayc0OwQeqYTh-WO86zwECL1B8CeIQhJi895aAUbiRDiLqqMqNsgCYEvAirP5VaORv46CIIXwbxxx0ljqJnTxRemGYoS-ZneepQa2rvQu09entXBw_MKx998tXkxnC0UKi8J6DfdyGqHfvNrhAFghHcVW7KHVuOOiPsw4RiDZOPjGhRkwxzb0sE_LYQSH39m2Ivwn9z8tUr7kqu3n6ERDRZk5J46c1ENu-4lIbuZCKatibiL18emegRPOahJdtgMhtqqc42DfMzmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmW_tVByh3SG-Nw09gMo-McVwaZ4Lh6DmekISblWIiGz0832cstIvDl_zL27X3fXGUfDVtBT8Ue7sSx4873ckukhOXSMO2oLNpxVST_k-MamubTBZU9mU-nrQcTGfFYaAm54yVI7XV-Ssothzcp9O9bac_QCHPfShUDpm4tcodlRuPTUt66LRUumHPUIzz9ACmIThbag8PsgLXPSyxlvSiIz8qvbgh7xVT3zllAdlQdJu96ycqTfMYB4z1Dju1L45TnY-WhLIL8QPYuCGdHdWCVX_sLyyY7jjl0Dh7Lf9_e3hQyHwKGmDM1jgzY2VQBFbrBHsCRJhKoV7V3_jMNIjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شاید کمتر کسی بداند در سال ۱۳۸۳، در چنین روزی یک دختر ۱۶ ساله به دلیل «رابطه جنسی خارج از ازدواج» در ملاعام اعدام شد.
عاطفه سهاله با استشهاد محلی و شکایت پدربزرگش دستگیر شده بود. او قبل از آن هم به همین اتهام در مجموع بیش از ۳۰۰ ضربه شلاق خورده بود.
‏
🔸
نگاهی کوتاه به این واقعه:
https://www.iranrights.org/fa/memorial/story/-3134/atefeh-sahaleh-rajabi
@IranRights</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77899" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5da532981c.mp4?token=nhXNRn63Oc_14HYI1sHTVRDu_KfBMvgZ5MC-3Zt4fS3IPttJEuhDnuuyoaUUGf7Pq4hHkYEVp_v_vXSA7_41c_eTr07YUn0ZqAPHdvHYi9y9dkz0-NCha2eYo2kHj4ol7Z8PTFV-23V4YOgRE69SAAvkWJi2pBqY8NKM3PmuyxqWMCzTuCm52DFMdXBjMaVWDYqub-v-39RdKVMy5g3BwDBrd3Xl-VXWmmROXYBx8HIAKl7k_IEgl_vBU8PURvDXyqqUpxZOQiqqPriM9JILHVnfjFb4yugMlFtZzjOasBeu8d-p5_DKa-Qav9Gxb_qJ4b2rT00NJUbavaz1NK28Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5da532981c.mp4?token=nhXNRn63Oc_14HYI1sHTVRDu_KfBMvgZ5MC-3Zt4fS3IPttJEuhDnuuyoaUUGf7Pq4hHkYEVp_v_vXSA7_41c_eTr07YUn0ZqAPHdvHYi9y9dkz0-NCha2eYo2kHj4ol7Z8PTFV-23V4YOgRE69SAAvkWJi2pBqY8NKM3PmuyxqWMCzTuCm52DFMdXBjMaVWDYqub-v-39RdKVMy5g3BwDBrd3Xl-VXWmmROXYBx8HIAKl7k_IEgl_vBU8PURvDXyqqUpxZOQiqqPriM9JILHVnfjFb4yugMlFtZzjOasBeu8d-p5_DKa-Qav9Gxb_qJ4b2rT00NJUbavaz1NK28Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر حاتمی، فرمانده کل ارتش جمهوری اسلامی، روز یکشنبه ۲۵ مرداد در مراسم گرامیداشت روز خبرنگار [در تقویم جمهوری اسلامی] گفت: هر کسی، هر رزمنده‌ای، که یک  آمریکایی را بکشد یا دستگیر کند و تحویل یگان‌های ارتش دهد، هدیه‌ای معادل ۳۰ هزار دلار (حدود ۵ میلیارد تومان) دریافت خواهد کرد.
بر اساس  گزارش صدا و سیما حاتمی همچنین اعلام کرد زنانی که موفق به این اقدام شوند، دو برابر این مبلغ جایزه دریافت خواهند کرد.
@
VahidOOnLine
او در ادامه گفت: سلاح هر فردی که موفق شده نیروی متجاوز آمریکایی را به هلاکت برساند، به دو برابر قیمت خریداری شده و سلاح جدیدی دریافت خواهد کرد. سلاح فرد نیز در موزه‌ای که پیش‌بینی شده، نگهداری خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77898" target="_blank">📅 20:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VHQlG99aAXiSEEUt-0oa23sDXhGCMqeJ_JEwRgEzJiV-R35mOaQWuOgdCa1SrS6_GVX13UV9cqJm-w7anK_SV8Ioi4vIiHMsUM46EzwXrWOQ8rsfH6d84elW7w3JForM2yp70YtIfjyS5Gy5QQVAVAsz-N3xdEvuWgyDcjNg2dufodw1DdGwxweHsdMisin52C6cstIE7a3lukxHJJrbb79ZPXRMc7y7Ij9cqGQdu83LHqpGPfe8K-wDe6zkzeOlb0OXZyrDGThbaLIgVWnm5k-hs04cosiAoer8bFfOhgtEroBa5XAxXVHWE6d72OaSzFg-iDpIeh5CHI0ChehjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dQ4ct5T6FG_rKqfVGAac5mGT2ly_Od80W1U3CjLnqpydDK1LkWXn9RHONhtkprudQj4-XRzPjY-E8hyvbIhtXbHu0wcJYPxbqsl5vC73HBnb0zVzvmgdS-te2u8VxCLeM1mZgyRjQEPnW7qLKdOoQEV1Lv-viNvf2-ON1G0z0OZOSbH-39ObsLvJGpDy43ZuuiwDs1b-SmhWZlHFJL2AcYQzmcbEu57zSva1d4gW3ubB-WAhjT-bG5BOWRlCARjU__bTOe7LOCRFVp2302Zya9wKiKu1HF7qhkz2oTsdZDRONVsu96d08X0iUgr2QCcOGfEwVVuItonzpfe0i4celg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وبسایت اکسیوس در گزارشی نوشت، دولت دونالد ترامپ در جریان مذاکرات محرمانه با ایران برای پایان جنگ، به‌دلیل تردید درباره اختیار مذاکره‌کنندگان ایرانی، از نیچروان بارزانی، رییس اقلیم کردستان عراق، برای برقراری یک کانال مستقیم با فرماندهی سپاه پاسداران استفاده کرده است.
بر اساس این گزارش، مقام‌های آمریکایی در میانه ماه مه نگران بودند که محمدباقر قالیباف، رییس مجلس، و عباس عراقچی، وزیر امور خارجه ایران، اختیار لازم برای رسیدن به توافق را نداشته باشند و مواضع آنها از سوی سپاه پاسداران تغییر کند یا وتو شود. به همین دلیل، دولت ترامپ تلاش کرد مستقیما از موضع فرماندهی سپاه درباره مذاکرات مطلع شود.
تولسی گابارد، مدیر وقت اطلاعات ملی آمریکا، در همین چارچوب با نیچروان بارزانی تماس گرفت و از او خواست برای برقراری ارتباط با احمد وحیدی، فرمانده سپاه پاسداران، کمک کند. بارزانی به‌دلیل سابقه زندگی و تحصیل در ایران، تسلط به زبان فارسی و روابط نزدیک با مقام‌های جمهوری اسلامی، از جمله فرماندهان سپاه، به‌عنوان واسطه مورد اعتماد واشینگتن انتخاب شد.
بارزانی پس از تماس با طرف ایرانی، خواستار گفت‌وگوی مستقیم با وحیدی شد. چند روز بعد، یک مقام سپاه با یک تلفن رمزگذاری‌شده به دفتر بارزانی در اربیل رفت و تماس امنی میان دو طرف برقرار شد.
به نوشته آکسیوس، وحیدی در این تماس به بارزانی گفته است که از مذاکره‌کنندگان ایرانی حمایت می‌کند و موضع سپاه نیز حل بحران از مسیر مذاکره است. بارزانی پس از این گفت‌وگو، نتیجه تماس را به گابارد و او نیز آن را به کاخ سفید منتقل کرد.
پس از این تماس، آمریکا پیشنهاد کرد مذاکرات محرمانه میان مقام‌های ارشد دو کشور در اربیل برگزار شود و بارزانی میزبان این نشست باشد. طرف ایرانی این پیشنهاد را رد نکرد، اما درباره امنیت مذاکره‌کنندگان ابراز نگرانی کرد. بر اساس گزارش آکسیوس، مقام‌های ایرانی نگران بودند که نیروهای اطلاعاتی اسراییل در اقلیم کردستان حضور داشته باشند و احتمال حمله به آنها در اربیل یا در مسیر رفت‌وبرگشت وجود داشته باشد. در نهایت این نشست برگزار نشد.
آکسیوس این تلاش محرمانه را نشانه‌ای از دشواری واشینگتن برای تشخیص مرکز واقعی تصمیم‌گیری در جمهوری اسلامی دانسته است. این رسانه می‌گوید جنگ و کشته‌شدن علی خامنه‌ای و شماری از مقام‌های ارشد جمهوری اسلامی، همراه با ادامه درگیری‌ها، نفوذ سپاه بر تصمیم‌های مرتبط با امنیت ملی و سیاست خارجی را افزایش داده است.
به نوشته آکسیوس، بارزانی اخیرا نیز پیام‌هایی برای کاخ سفید فرستاده و آمادگی خود را برای کمک به ازسرگیری مذاکرات ایران و آمریکا اعلام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77896" target="_blank">📅 19:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eorkizh48Et9_9sm6LiM-JEmNZMMq6DNV454QXFGQ2jAZfUQV0i3HdFeXyKqkyNKxG41JQ6yDi7dRsNQf6gjiwQAGun_dko3Rfxyi-6gWIFizFwhFnTV4LAntB5MEYnUm0kDIOiy3WjMTJKjd90HFteoF7wgbNMwXg-3YhVOpigvsGP7EqL9jI8p0eK2T85RPnfxOTZWW2fgsqsnhfCMaliGG4f1_P8WFIvtzWZBJmTpQ4jghXDLWDHQnfLuca83DZh3e7MxoGppgga-R-q3rMffuet9ZaQFRyDHDxpVFVjuEufD_kNWMqfc90I23RXpMMSb6VlEWnuRzZJs1nsS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fk9p38MTaEdxp2uZlWWHn2YVmENq5NK-uMb2XY7T8G_X3l3Lv574L_FKIicCBi6gIifsr-Wbh0O1ccjDBW3XfRcfbiG0-ENgNJ8lh-bEmM2p0C62-voxm0tjdrnIUbvA2W7URyoQuhEj4azuijprD4GhELqoyOyiu07uIkK83lxIz8hOFwkdNPyYupYVqVdlSwD0gtp8MsQdAHmMtfMe6kkhyBcDHYo7_A_9rJk8EVUH2e9KzuZRmU4xRnOGj5JOZA-GAjORbuAfoSxolGnOuJ88zAyr-TQZJMihhaJajqj8LBVm4p0-0Z71G68CzrEE8B7k2ffJ0y6WpaIYk0uA4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=Zuia0b3R1YDSKzZiBSsW0qyYr4Vks1XrrHrTMxvlCdu9memjHymTKQOYCv1da2DPiPrKdB8PUPEf3VK7UBSOXc9APCXEHQAyYXgzFDrVjX9XxEcyISrp2CPyT8t3moYdD0krtek_qIRpRwEuYxUe9Fo4i3DkVxAjAOnhaE93zLWS1vxgmYDTPIJW0bI1pgPHtbs3qWh8Ctv8o874IGosqZYxIC2b1s5pwYQ0OXlWYfdQf7XGtV1WnU1speDDduQywULWnVyAx4KMenYgRxVds1sspyEuURFNU6VkrDoPCt8802UnSNFIdb4PEg_e5lpWnEnISaI_UlTGhsEKhCppEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1630a6bff7.mp4?token=Zuia0b3R1YDSKzZiBSsW0qyYr4Vks1XrrHrTMxvlCdu9memjHymTKQOYCv1da2DPiPrKdB8PUPEf3VK7UBSOXc9APCXEHQAyYXgzFDrVjX9XxEcyISrp2CPyT8t3moYdD0krtek_qIRpRwEuYxUe9Fo4i3DkVxAjAOnhaE93zLWS1vxgmYDTPIJW0bI1pgPHtbs3qWh8Ctv8o874IGosqZYxIC2b1s5pwYQ0OXlWYfdQf7XGtV1WnU1speDDduQywULWnVyAx4KMenYgRxVds1sspyEuURFNU6VkrDoPCt8802UnSNFIdb4PEg_e5lpWnEnISaI_UlTGhsEKhCppEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از آن که قالیباف اعلام کرد درباره مسائل مرتبط با سرنوشت مردم ایران از روی حزب‌الله لبنان تصمیم گرفته میشه و اطمینان داد که مذاکرات به خاطر حمله اسرائیل به اون‌ها متوقف شده بود و مدعی شد که تهدید کرده بودیم اگر ادامه پیدا کنه "
این‌طوری، این‌طوری، این‌طوری، شما را خواهیم زد
":
شنبه:
‌وزارت بهداشت لبنان می‌گوید که حملات روز گذشته اسرائیل به روستاهای جنوب لبنان ۱۱ کشته به جای گذاشته است.
ارتش اسرائیل گفت که این حملات در پاسخ به حمله حزب‌الله به نیروهای اسرائیلی انجام شده است؛ حمله‌ای که به گفته اسرائیل سه سرباز را به‌شدت زخمی کرد. اسرائیل همچنین می‌گوید که یکی از فرماندهان نیروی رضوان حزب‌الله در حمله به انصار کشته شده است.
این حملات از مرگبارترین حملات از زمان آغاز آتش‌بس میان اسرائیل و حزب‌الله در ماه ژوئن به شمار می‌رود.
با این حال، نواف سلام، نخست‌وزیر لبنان، با تاکید بر غیرنظامی بودن قربانیان، این اقدام را تنش‌آفرینی بسیار خطرناک برای ثبات منطقه خواند و خواستار توقف فوری آن شد.
@
VahidHeadline
و دوباره امروز یکشنبه:
ارتش اسرائیل بامداد یکشنبه نبطیه در جنوب لبنان را هدف قرار داد.
این حمله تنها چند ساعت پس از مرگبارترین روز حملات اسرائیل در لبنان از زمان آتش‌بس با میانجی‌گری آمریکا بود که دست‌کم ۱۱ کشته بر جای گذاشت.
بر پایه گزارش الجزیره، آن حملات صدها خانواده را به فرار واداشت و جاده‌های منتهی به شمال را مسدود کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/77893" target="_blank">📅 19:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TxpnofvqiGbx52PLtzeOYqlR652OOVIvFvSgllRygvs9wSU2DYPEpYcFABiKx0IQ-IYXBdOE4NjpFkpVSu2MpJ0TzXYX-Nd6jHwbPpttYFUKDIUJLb-pW4MTAKZ2QF0Gv70zsNvZ0TuN3NMmPGMF3Iv4oo8h4cOAjc-K3gE2bhIbZbNo3eRwj92O0UnLjvrVFeRzTBjqqDCPyJHVdukK3-OTnTU3FswEDJGfiN6PigMlMYkHvg1l2a0Empm9yWFZ75TBy-UCXpRJHPpqsocnFAcxmTZHnbLC1JbtR1I16AkmzEze3iNI6n2Kd1gj1Zx99e4-eFEhCVfpQz9O8yYTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hk-du3jh1cQ6Qq9G-6mTgvp656jui-9K7wP8rSLDN9wsH4HRUP3sGpy4H5WBVrwm4W4lLf9pQkUNFQ0TvqLUNel6TjmxmMB4LenxQk4tTIn0oijcQ5uaS7D9wAKY1oiD9o9UumCmvimZesKGNnp36gwqgFNE8tpzFhWKBQJPr-8wtH9ZReqaqIIRsmaUCDf5wNqdk50EKhi3Y0S2-CFQTWPgrqfT_O1FD12641bTDGJb7R-ySDpf9NKK6aF-LKXdAEkEmyV7z8hEeMCdmwUQv91QmGZybFzKGBV1x5pZGtZY9sQ6FgaDtc3ulkNam0RJ8pKwo3ni3mUGoouUYZAdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nd4-Z1oDYZ4FvGKVA44cmlCzpMh0VGKLCVxq_75QtQ7aaMMLTGUiz0jMKcotXPI4XHjeK8enMlWifs2yrQxVhodmXcGp2VXMXLD6_bO7gmFbSAEDHCkStSnpLvzT5HraXFu3aMBX29N-w4TMvJYNRqSF8Y5OFJM7fUD6fRW_jFakGuLj2Jbd0pfEiAS0VaxtAaY64oCR-Z04yWGoz3ayoFzSTPZ-F_4fKQY5FnNXAwbwTvL-H6vfQAl7EcvGfKr9JlBn1H2Cs5ieONAudKxwNEWPK5cUYbg6ff48NloXITo3kobk8Ztj4vA9vdvP-LD-fzEQX47H_JqOJr9g2a5AEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iOUHd4ZuzBwIoN8YYNLUy2gTjZq2mh6EHG8y6WRLRPZ-rG-xURgnxuAuzh2gNPWz2tTgkbfFcguOJkt4LLI5nwvNGuU3GFEQHCj3x-AGtMyMxkPr4-WE887Hl_s9GweDyK2ufCyyBln7WuiVTHc_Btq_oByqx3E_AEvGEYs8T5a7_A6JUTu28cEgk0U11vDCt7wB75IfAjCMYhL11ZM7h7Ud7HAei6--enFELJKrEGaIR8BlZvavIUwuDJeiN6S8ZuygGGwsE111IEBYeOQTEqq-YZIQrjEsVNYybRyvK0lL-t9vCU2mci82nf4iTcpMo4prAfXTqRt9l1bTjyfqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k5rQD2-kbFkavZEVHNQmfIb46nzMGr8DPJtyYma7Z97ik-Z_wltTpJVi7gMg3yEZ-r77VhAMAMuWN1VPage3fY_pABb9sgzJL7BVgwCkdjZd428dV0SP0LqscA-inIROhz2peXVNCriN3YRXGBx2xx4xF0B6DBW_WadV-39Riczs-tfWjBi6haIhgzileB-sc9JbZvpQUx_2ISc98jq5jGkm_K02BrplWY45kqlaCr-c8-GwFOU9fXlToOPoEwQ873L3X2cSi8kptiHrrDOhmrT9YLMKx12OiIUt5BoTb4gHaK9D-PIxOQO2Du-LPnY7Mxhg0ugG4fQETb_r9742nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/INeiMlPJa_Co-aS12sASJI7CQ5kKCbHNlPFZm16XsPkEeb_WeknCCOVKigW7zf1cOIdNeXR1iECWudn-XWwjFRSig8siIylMeIso9kTLpb8FTpLRV-4YBOqX02H_t2oZD0DfRo6z7dXrFN5acibw3Ruy946GG4C9IBsidWfSziwxnMOTFbJlWg6Z8j92qP-0TLjeBsgHAnzlY1uiMTaiQf2mT6c3ogblkIekBALSwmQotgxNjo5r1fgYdBT-PG2PxRTpVR0zMp9DKZkZJjh514I1WZTPkj-yIgOtIoPaB3TtNslFkkBZloShvqWFhyEe50umpbv3vOeYaY6GnU7XgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qrQTXRc9dP_1VCwAZ6VOmME2g4aBZvz8h4w93fX-LZfTfc-uPy6vSo4U0-SnzSfNwmJh3jy7JVLhIkUBtK-9fq7irbtTyXZDdUQ4yjkGOvtdxG9RYhQYAhUb_AEWZrdjkfsAz8GVUHv01BClSioW0Na5UUnySEaS6al_8sHNN3wdyy-kIFMOdosgq7vg6s73deVWRZIoAobZ3RDCjQ0LmjmmAq0gv9YjJATGYvI0v5V3zrJ-UbZ97iYt5zaq8BRin8ElC719YdHLJGRItx7fSHUB3h2ndpgEVttu5YXW3Lbr1dhS_hH3_f8D8w5cIvLIzyorXNVB64nQ5hMfq0RiDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام کردند که کلیات این طرح تصویب شده و جزئیات منتشرشده [
به نقل از "پایگاه اطلاع‌رسانی وزارت کشور"
] هنوز بررسی و تایید نشده‌اند:
مجلس شورای اسلامی طرحی را تصویب کرده است که در صورت تبدیل‌شدن به قانون، مصاحبه و ارتباط با رسانه‌های خارجی، ارسال فیلم و عکس، همکاری علمی با برخی دانشگاه‌های خارج از کشور و شماری از فعالیت‌های فرهنگی و آموزشی را جرم‌انگاری می‌کند.
طرح «مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در کشور» روز یکشنبه ۲۵ مرداد با ۱۸۳ رای موافق در مجلس تصویب شد.
براساس متن منتشر شده از مصوبه، مصاحبه، شرکت در گفت‌وگو یا هرگونه ارتباط با رسانه‌هایی که حکومت آن‌ها را «معاند» می‌نامد، مجازات حبس درجه شش، معادل بیش از شش ماه تا دو سال زندان، خواهد داشت.
رسانه‌های آمریکایی، اسرائیلی یا رسانه‌هایی که از سوی این دو کشور تامین مالی می‌شوند، در این طرح از مصادیق رسانه «معاند» معرفی شده‌اند. دبیرخانه شورای عالی امنیت ملی نیز موظف خواهد بود فهرست این رسانه‌ها را هر سال منتشر کند.
گفت‌وگو با دیگر رسانه‌های خارجی نیز به اطلاع‌رسانی در سامانه‌ای وابسته به وزارت اطلاعات مشروط شده است. مصاحبه بدون ثبت قبلی در این سامانه، می‌تواند به شش ماه تا دو سال زندان منجر شود.
ارسال فیلم، عکس، صدا و هرگونه داده برای رسانه‌های غیرایرانی یا افرادی که در خارج از کشور فعالیت رسانه‌ای دارند نیز با همین مجازات روبه‌رو خواهد شد.
اگر ارسال اطلاعات در قالب همکاری، با آنچه «قصد مقابله با امنیت کشور» خوانده شده یا هنگام «بحران، اغتشاش یا آشوب» انجام شود، مجازات به حبس درجه پنج، معادل دو تا پنج سال زندان، افزایش خواهد یافت.
در متن طرح تعریف مشخصی از «ارتباط»، «رسانه معاند»، «شرایط بحرانی» و «فعالیت رسانه‌ای خارج از کشور» ارائه نشده است. گستردگی این عبارات می‌تواند ارتباط شهروندان با خبرنگاران و ارسال تصاویر رویدادهای روزمره را نیز مشمول پیگرد قرار دهد.
وزارت اطلاعات و سازمان اطلاعات سپاه ضابطان جرایم این مصوبه تعیین شده‌اند و رسیدگی به پرونده‌های آن در دادگاه انقلاب انجام خواهد شد.
محدودیت همکاری‌های علمی و آموزشی
مصوبه مجلس، همکاری با دانشگاه‌ها، موسسه‌ها و سازمان‌های خارجی را نیز محدود می‌کند. وزارت اطلاعات موظف خواهد بود هر سال فهرست مراکز خارجی مجاز برای دریافت بورسیه، کمک‌هزینه تحصیلی، انعقاد قرارداد و شرکت در همایش‌های علمی را منتشر کند.
همکاری با مراکزی که نام آن‌ها در این فهرست نباشد و همچنین ارسال نمونه‌های پزشکی، تحقیقاتی و باستان‌شناسی برای آن‌ها، مجازات شش ماه تا دو سال زندان خواهد داشت.
برگزارکنندگان دوره‌ها، کلاس‌ها و کارگاه‌های حضوری یا مجازی که به تشخیص حکومت با «فرهنگ ایرانی ناسازگار» باشند یا تحت هدایت نهادهای خارجی برگزار شوند، ممکن است به حبس درجه پنج، معادل دو تا پنج سال زندان، محکوم شوند.
در برخی گزارش‌ها مجازات برگزارکنندگان این دوره‌ها پنج تا ۱۰ سال اعلام شده است، اما متن منتشرشده از مصوبه، حبس درجه پنج را تعیین کرده که براساس قانون مجازات اسلامی بین دو تا پنج سال است.
افرادی که با اطلاع از هدف برگزارکنندگان در این دوره‌ها شرکت کنند نیز ممکن است به جزای نقدی یا شش ماه تا دو سال زندان محکوم شوند.
محدودیت‌های تازه برای هنرمندان
فعالیت‌هایی مانند تولید یا کارگردانی فیلم، سریال، مستند و تئاتر و همچنین تولید موسیقی و کتاب، در صورت ارتباط با نهادهای خارجی و با تشخیص نهادهای امنیتی، می‌تواند مشمول مجازات شود.
در متن مصوبه از آثاری نام برده شده است که «احکام دینی را زیر سوال ببرند»، «چهره سیاهی از ایران نشان دهند»، «مروج فرهنگ ضد اسلامی» باشند یا با هدف مقابله با جمهوری اسلامی تولید شوند.
تهیه‌کنندگان، نویسندگان و کارگردانان این آثار ممکن است با جریمه نقدی، محرومیت دائمی از خدمات حکومتی یا ممنوعیت همیشگی از تولید آثار فرهنگی و هنری روبه‌رو شوند.
عباراتی مانند «چهره سیاه از ایران» و «ناسازگاری با فرهنگ ایرانی» نیز در این طرح تعریف نشده‌اند و تشخیص آن‌ها برعهده نهادهای امنیتی و قضایی گذاشته شده است.
@
VahidHeadline
کانال  مجتبی خامنه‌ای، بدون اشاره مستقیم به ماجرا این پست رو گذاشت:
🗒
لازم است مصوّبات مجلس با مسائل اصلی کشور و نیازهای مردم نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد. جامعه پیش از هر چیز نیازمند مشاهده‌ی نشانه‌های واقعی امید، مسیر باثبات و چشم‌انداز روشن از آینده است تا بتواند بر اساس آن برنامه‌ریزی و حرکت کند و نمایندگان مجلس با مواضع، مصوّبات و نطق‌های خود میتوانند مجلس شورای اسلامی را نهاد پیشران امیدآفرینی نمایند.
✍️
بخشی از پیام به‌مناسبت سالروز افتتاح اولین دوره مجلس شورای اسلامی و آغاز سومین سال فعالیت مجلس دوازدهم | ۷/خرداد/۱۴۰۵"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77886" target="_blank">📅 18:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u8oTDyGHMMpxkl4CmCUhz8aq1a_XqSdzCqVxvAO_9QxQDa0IFSULqN0_WFMjL-hzV0OqVoL9_7NsJ50RLOYEMjyMfU6jaeTvRMiE_hRca2o8YkSvSOW2Hnox290JvzZZhGOxfLZE4JX-o8ogJejB-6-jN9M0EFlqk3nMyPFn7EQlNhuMeZn5x3-UK2BELmdIgCXs0H1lh8ALFf_DE5-cn1wpNTNTAg_wiwz8Dq6gsneUkg6U4iRWkbi0Ru6FxDJo_ZjStoYw2SiirFyogRYdJqKLsJaP2LYneo-hX1zpxVYq4RU8CCi8mJD6JwxktM14RNm2QyNY0duhjgQMNmY7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J-5yijm1t6e3St97DfunYCFxuMFVzun4vVKNrtcSDKFWRTwFnJFF2JRk08p0jphTsYPX7YNdlivK62cQmlNmqC_XlC1CGUDbnqV3IOPHteg9piAKfBnO_tws__7dA6CNvkpHBE8fI735Yhyz7m-mX9CQUtndm8TeVWhvHwWLmiS3UpLj_U7drjwrMntnQrBuT5z4dceaYAr6cqQst2U6U23FTj_HijhJWUQHXrJlmDw1SJCpok4fRCQgR3H5avcUgBttQ-iy14PRoDG_VPq8xKtighJ9f9Tk13djM4HNgTrtl4xzez_ejgx2G1VsVLE5eU2ashx7BU8-a49qgr8lGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R_0EV6ASPB5L8Lt7bTb1yV33GDOFeoHlAGTTWVFSaQ8b62sA7hVm3BuUjMr25bzSmgu6zeqdDITzbvKyiyuBOoimHZhTBCjmnaiJnYVLzJoKc13MfaA6KmXKtTjwKUTbkTPuE7rbJu8bRDBVxB9y9oDn7VK_viVEj1R7L1_USpXqUwxBrQGL1C32B-udooN9lO_yVs75cQJs9YRXrye0EnmXKMtg1fKHJewxoJZoaJspXoM8ksusRJS0uQqIpxME9Wu5OnuDEWZl1baTQE5OnrCNyQi_gQbBgBsGcFrRDhZ1e5D0fAWGNM5yZCS0p-BpqtuCF9RXW7jaDBK2ogegIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KRvOPK0Ju7R4CA0jZbgMXGVWtjGUb1ykikAK9mYm-bwY3YshXYKpwrYI_hjWDsgtx3dFZpoE7S0my7VeC74zQMlurSYaasFdj1LKqOXJfpQw6tWZhaYp4ID8A5kNs0-COur1_AkEcboUPv0d_XCriGuQzTV4pwRDRpDV4rG98G76HBXKo35cBbD1_qAF_STlQLoKt3y7cOTj-U9LIu0krN5RwicmdnjB9weLhLqm4-mWe8SqH7-_o_vzrw_Gi7_LJjyW2Lh79Zbv3df7hmlZV2zV4faNh9p5zfdnRsRB4Q5xdFlUI5jhOioKvVH0ZhDp1J5lgvGbT6hZa8_ndSb3yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=eknI7SD3oYOBbMn79UDJHegxjdIIOxdu9rFXKqHQgONrSn3KH3U87vopS_7qiNJCfw5Sjo0JMc02sL4uGijU4K4UfndXgKHGYuCASWTDBTv9p6HvRGh724x6KUXyIzg4VyN-gHGtq9jsK0UXXY6XmjA-N-f7GFzkmUjHnuMQP70m9G6lOMXovBO6KRFC0woFI0v8GZlDQZNJ7NdbznLb_YYMFpYFzU6pCtIm07xnWb-gf37d6iRooufhUWw5tJMH_z-crfzuJk-oJ_10TR2Usblukqi2Yo0hiWTObABMmFO5nwQy-bARc9GPr1dLCKQM4SSlzqSqIwUW7I9QnkGLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0bf656d54.mp4?token=eknI7SD3oYOBbMn79UDJHegxjdIIOxdu9rFXKqHQgONrSn3KH3U87vopS_7qiNJCfw5Sjo0JMc02sL4uGijU4K4UfndXgKHGYuCASWTDBTv9p6HvRGh724x6KUXyIzg4VyN-gHGtq9jsK0UXXY6XmjA-N-f7GFzkmUjHnuMQP70m9G6lOMXovBO6KRFC0woFI0v8GZlDQZNJ7NdbznLb_YYMFpYFzU6pCtIm07xnWb-gf37d6iRooufhUWw5tJMH_z-crfzuJk-oJ_10TR2Usblukqi2Yo0hiWTObABMmFO5nwQy-bARc9GPr1dLCKQM4SSlzqSqIwUW7I9QnkGLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد آریایی‌نژاد، نماینده ملایر در مجلس ایران، در یک مناظره تلویزیونی، کشته‌شدن مهسا (ژینا) امینی را با عبارتی توهین‌آمیز توصیف کرد و اعتراضات پس از مرگ او را «هشت ماه اغتشاش» خواند.
این اظهارات در رسانه شهرداری تهران (همشهری) مطرح شده است.
پدر و مادر مهسا امینی در استوری‌های مشترکی در شبکه‌های اجتماعی،سخنان این نماینده مجلس را «توهین‌آمیز» خواندند و گفتند چنین اظهاراتی از ارزش و جایگاه دخترشان نمی‌کاهد.
@
VahidHeadline
امجد امینی نوشته: «مطلع شدم احمد آریایی‌نژاد، نماینده ملایر در مجلس، با لفظی چنان‌که سزاوار و شایسته خود و اسلاف ایشان است و با کلماتی که در هیچ آیین، مرام و معرفتی جای ندارد، به دختر ما، خانواده ما و تمام مردم کردستان و ایران توهین کرده است.»
پدر ژینا امینی همچنین با اشاره به وضعیت اقتصادی و اجتماعی ایران، خطاب به این نماینده مجلس نوشته است: «عجیب است در شرایطی که مردم این مملکت به‌خاطر تصمیمات امثال آقای نماینده در اوج فقر و فلاکت هستند و هزاران دختر و پسر هم‌سن‌وسال ژینا در افسوس آینده‌ای که ایشان به آتش کشیده‌اند می‌سوزند، باز هم سراغ دختر ما رفته‌اند.»
او در بخش دیگری از نوشته خود آورده است: «می‌گویید فرشته نازنین ما به درک واصل شد؛ بریده باد زبان شما که یک مملکت را به درک واصل کردید و نه‌تنها از عقل و خرد، بلکه از سر سوزنی شرم نصیبی نبرده‌اید.»
پدر مهسا امینی در پایان نوشته است: «نام دخترمان در کنار هزاران انسان بی‌گناه دیگر تا ابد در تاریخ این کشور جاودان است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77881" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drce0VURU6pqJHY5O6elZH_S8bYCR4vOm_91V3JNWFR-77nKvqI30StAUtSZ-W8Gx6Ym595EIiyJbQNBIIZJkCh8awmw-sc3V7pdwWNJtWGiZvKWh8Y2AYvCk2XscjZPNMiUG_OGqzIY3wIPEVXEE_WkAOr2XEJiDBAVajJNIJcj6uPFZsifYOG7BAo9NJFyhBKGZpOpzKcwwYCCeD7KaarJK3wG3ftnyQpF4z4nOE2XD9v2wJSe6BbcTH1gGaiLPeGlS3_btWDpnT-yxCv00bbKAWJo_1Wp-1lkTlevYASRdw85hyI-l5j13j1KDWx-n3O2_MqIq2TiSw8egPtO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه جمهوری اسلامی، گزارش داد حکم اعدام شهرام صادقی، از معترضان خیزش دی‌ماه، بامداد یک‌شنبه ۲۵ مرداد به اجرا درآمد.
به گزارش این رسانه حکومتی، دادگاه انقلاب کرج صادقی را به اتهام «اقدام عملیاتی به نفع اسرائیل، آمریکا و گروه‌های متخاصم» به اعدام محکوم کرده بود.
خبرگزاری قوه قضاییه این زندانی سیاسی را متهم کرد که شامگاه ۱۸ دی ۱۴۰۴ در جریان «کودتای آمریکایی-صهیونی»، با یک دستگاه خودروی پراید شماری از ماموران یگان ویژه استان البرز مستقر در چهارراه گلزار کرج را «عمدا» زیر گرفت.
میزان نوشت در این رویداد، هفت مامور یگان ویژه مصدوم شدند.
مقام‌ها و رسانه‌های جمهوری اسلامی در تلاش برای بی‌اعتبار کردن صدای انتقاد شهروندان، بارها اعتراضات ضدحکومتی را «اغتشاشات»، «آشوب» و «کودتا» نامیده و آن‌ها را به بازیگران خارجی، از جمله آمریکا و اسرائیل، نسبت داده‌اند.
شدند.
میزان در ادامه گزارش داد صادقی پس از «حمله» به ماموران یگان ویژه در کرج، با «همکاری اغتشاشگران» خودروی خود را به آتش کشید و از محل گریخت.
در این گزارش آمده است: «او با جعل هویت و در حالی که اعتیاد نداشته، در یک کمپ ترک اعتیاد مخفی شده بود که بلافاصله شناسایی و بازداشت شد.»
خبرگزاری قوه قضاییه نوشت صادقی در جریان بازجویی‌ها دست داشتن در این رویداد را رد کرده و گفته بود شامگاه ۱۸ دی از اسلامشهر راهی خانه خود در کردان ساوجبلاغ بوده، اما برای صرف غذا وارد کرج شده و در آنجا خودرویش به سرقت رفته است.
به گزارش میزان، این زندانی سیاسی سرانجام پس از مواجهه با «مستندات و دلایل متقن ارائه‌شده»، اتهام خود را پذیرفت و «اذعان کرد» خودرو را به سوی ماموران رانده و سپس آن را آتش زده است.
خبرگزاری قوه قضاییه افزود حکم اعدام صادقی پس از رسیدگی به فرجام‌خواهی و تایید در دیوان عالی کشور بامداد ۲۵ مرداد اجرا شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77880" target="_blank">📅 08:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDcl-8H8Yt0psrRG-dTN4Z9PW3Ol37Ro9edlg7EG0ZTUnGb1ieLqcoTcutNbFZBUV42UMmjaDbtXmaahn3yRknWLMpzCWgkSlkhtWMl1Cb9eZD4LmBXpI9drCt40KSs8f6si6_mzZvcooZOaJ9Kksfg9Oj_oQk0e0VxQlsUWS8mJZH6dbrgUkeHNcN65IP5EkJUXG9vTprsKVqgov6kFCmJcDBVu51SnRFxtDKsRL6EmPcj1rMI_VB5RyqPhe_io88n0daYbL3AvKktAjsALEgtmbnczAbAakcdIrE_Q0x5yedQR2O9rsIEtOO_MJisIv7XretCur0QpYoycsiD75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجد محمد الانصاری، سخنگوی وزارت خارجه قطر، ادعای جمهوری اسلامی درباره بازداشت سه خلبان ایرانی را رد کرد و گفت نیروهای قطری پس از جست‌وجوی محل سقوط جنگنده‌ها، پیکر یکی از خلبانان را پیدا کرده‌اند.
الانصاری روز شنبه ۲۴ مرداد در شبکه ایکس نوشت ادعاهای مطرح‌شده درباره بازداشت خلبانان ایرانی «به‌طور قاطع» نادرست است و از انتشار این اظهارات، به‌ویژه در شرایطی که تلاش‌های دیپلماتیک برای کاهش تنش در منطقه ادامه دارد، ابراز تعجب کرد.
سخنگوی وزارت خارجه قطر گفت پس از ورود خلبانان مورد اشاره به حریم هوایی قطر، با آنها تماس گرفته شد و مسیر هدف‌گیری نیز بررسی و تایید شد. او افزود پس از رعایت قواعد درگیری و برقراری تماس با خلبانان بدون دریافت پاسخ، قطر اقدامات لازم را برای دفاع از خاک خود و مطابق با الزامات قوانین بین‌المللی انجام داد.
الانصاری همچنین گفت تیم‌های جست‌وجو و نجات قطر به‌طور کامل عملیات یافتن پیکر خلبانان را انجام دادند. به گفته او، دولت قطر پس از پیدا شدن پیکر یکی از خلبانان، برای هماهنگی تحویل آن مطابق مقررات حقوق بین‌الملل بشردوستانه با طرف ایرانی تماس گرفت.
او افزود قطر در ماه آوریل از یک تیم برای بازدید و دریافت اطلاعات درباره جزییات عملیات جست‌وجو و نجات دعوت کرده است، اما طرف ایرانی تاکنون به این دعوت پاسخی نداده است.
پیش‌تر فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی مدعی شده بود سه خلبان ارتش که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، به اسارت نیروهای قطری درآمده‌اند.
مقام‌های قطری با رد این ادعا، روایت متفاوتی از سرنوشت خلبانان و عملیات جست‌وجو و نجات پس از سقوط جنگنده‌ها ارائه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77879" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AK0kYg2Eve0XKDvORUU2zIR8teOsXpGog_c6z6-hfA409B9wIRngXm4DU36ogrQZgt871lj-hCaErJP7xWoeiI2Vjnr7IKUlcUJHKIyAbH67YnGbodn440Fj9X3jOERxYxmbYm2fvVl2wNImk81ctSFsTFiRmh1K9zEszpwe42X_l9u1JQOIsPvpuWeetzU-tyGvKJzh5HgyxvY6KHsf1CyEjUy2TEXy264YhPxZwBJncovWaREvgTLkmYnb5BpoHmkFjA4HoA2vRD1dK1F9JMW8CRmLZ-DT7EpaQdo5a5cvGfgByL1Jrm1n-i6gZ3KI9BgFQd7HPxBTrgY8y9aBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد باقرزاده، فرمانده کمیته جست‌وجوی مفقودین ستاد کل نیروهای مسلح جمهوری اسلامی، در نامه‌ای اعلام کرد سه خلبان ارتش جمهوری اسلامی که جنگنده‌های سوخو-۲۴ آنها در جریان حملات اسفندماه سقوط کرده بود، زنده به اسارت نیروهای قطری درآمده‌اند.
خبرگزاری فارس، وابسته به سپاه پاسداران، این نامه را که خطاب به رییس کمیته بین‌المللی صلیب سرخ نوشته شده، منتشر کرده است.
بر اساس این نامه، جواد صالحی، عبدالمجید دشتیان و عمران به‌روشیان حدود شش ماه است در بازداشت نیروهای قطری به سر می‌برند. باقرزاده گفت دولت قطر تاکنون اجازه دیدار، مصاحبه یا تماس این سه خلبان با خانواده‌هایشان و مسئولان پیگیری‌کننده را نداده است.
پیش‌تر مقام‌های جمهوری اسلامی گفته بودند به جز مجید کاظمی که پیکرش پس از حمله به قطر به ایران بازگردانده شد، وضعیت سه خلبان دیگر این عملیات به‌طور دقیق مشخص نیست و اطلاعات موجود درباره سرنوشت آنها ناقص است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77878" target="_blank">📅 18:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5168e558df.mp4?token=eOJQwJ9fsTTY5u7b1Jer_5PCHqSvaVL1Un9slXMwWDAH2_Eyoiw1_hp-Jyem5S95nQWylKUP6k5JkRSwZ5bxUHLQxtERoY61PoleFf93MpKZjjEeIUJ2ErrHz9p-sDK7eEgmf-rzdUgjpqVtPufueRDQd_vvBUoudao2odZ3dach4msZT_vgcULy2zJLNfkBLDhnyGyqNzvZJXv95QWY3G2E1tNDZIfOpiVBzHXrZlQdE36YUvdOQChds2JdpCHaNh7pnvVX4q146jFg-VyUczRs7pMwzKjtyrWe2uH9wPiNpbbVXm42IJeh_CBaIiiqxFDCRszLnXZ8hv_AXtQt-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5168e558df.mp4?token=eOJQwJ9fsTTY5u7b1Jer_5PCHqSvaVL1Un9slXMwWDAH2_Eyoiw1_hp-Jyem5S95nQWylKUP6k5JkRSwZ5bxUHLQxtERoY61PoleFf93MpKZjjEeIUJ2ErrHz9p-sDK7eEgmf-rzdUgjpqVtPufueRDQd_vvBUoudao2odZ3dach4msZT_vgcULy2zJLNfkBLDhnyGyqNzvZJXv95QWY3G2E1tNDZIfOpiVBzHXrZlQdE36YUvdOQChds2JdpCHaNh7pnvVX4q146jFg-VyUczRs7pMwzKjtyrWe2uH9wPiNpbbVXm42IJeh_CBaIiiqxFDCRszLnXZ8hv_AXtQt-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دولت در ایران روز شنبه ۲۴ مرداد گرانی‌های اخیر و تأثیر آن بر معیشت شهروندان را «طبیعی» خواند و محاصره اقتصادی و تحریم‌های نفتی آمریکا را از دلایل آن اعلام کرد.
مسعود پزشکیان در نشست با دبیران کل احزاب و فعالان سیاسی گفت: «قبلا محصولات وارداتی با کشتی وارد می‌شد؛ اکنون کلی مسیر عبور می‌کند تا وارد کشور ‌شود و قیمت تمام‌شده کالا بالا می‌رود.»
او در ادامه افزود: «درآمد ما هم کم شده، قبلا نفت می‌فروختم، الان نمی‌توانیم بفروشیم.»
مسدود ماندن تنگه هرمز علاوه بر افزایش قیمت انرژی در جهان، موجب فشار بر اقتصاد ایران و تشدید تورم شده است.
گزارش‌ها حاکی است که با اجرای محاصرهٔ دریایی صادرات نفت ایران از طریق جزیره خارک به‌شدت کاهش یافته است. حدود ۹۰ درصد صادرات نفت ایران از طریق این جزیره صورت می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77877" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=fqyzCaLA6WG6Siv-ULXfbgq-vaQAbtEb_feaxXe-_0jaci4Gj3IlmSc2AxMvs0EnfzkYUdof5JREZeU64B1qQVUCT8nBT4mYUpT_H3RGwSVkcnlLur3_qxujTrWVcVAGedX85FSq6NAC9Z0QkmmjHnej9jVzUw1k1B5wRia-E0tbE4c4DuPRCefFGTzVSGIf7jUYplpZkH4ngNI_osXsO_OIWXFu7wbUuu-1BTNLjNzkGSHbO3_ccVOttxeP4QQ2eQ-gTlsHxhSrTm1NhDVrjdJ9zLCxr56-MYhA7lvr4WMCfBpvx4IHpEoNU72Gh936qVjYl-ZpIs_MektWwEw-sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1eed77d1.mp4?token=fqyzCaLA6WG6Siv-ULXfbgq-vaQAbtEb_feaxXe-_0jaci4Gj3IlmSc2AxMvs0EnfzkYUdof5JREZeU64B1qQVUCT8nBT4mYUpT_H3RGwSVkcnlLur3_qxujTrWVcVAGedX85FSq6NAC9Z0QkmmjHnej9jVzUw1k1B5wRia-E0tbE4c4DuPRCefFGTzVSGIf7jUYplpZkH4ngNI_osXsO_OIWXFu7wbUuu-1BTNLjNzkGSHbO3_ccVOttxeP4QQ2eQ-gTlsHxhSrTm1NhDVrjdJ9zLCxr56-MYhA7lvr4WMCfBpvx4IHpEoNU72Gh936qVjYl-ZpIs_MektWwEw-sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس و مذاکره کننده ارشد با آمریکا، می‌گوید پس از کشته شدن یک فرمانده ارشد حزب‌الله در حمله اسرائیل به جنوب بیروت، گفت‌وگو با آمریکا متوقف شد.
به گزارش رسانه‌های ایران، آقای قالیباف گفت: «در آخرین حمله‌ای که به ضاحیه انجام دادند و مسئول اطلاعات حزب‌الله به همراه خانواده‌اش شهید شد، همان‌جا همه چیز را متوقف کردیم. گفتیم که امشب این‌طور و آن‌طور شما را خواهیم زد و اگر رژیم صهیونیستی هم پاسخ بدهد، همه منطقه را می‌زنیم.»
به گفته مذاکره کننده ارشد ایران، «همان شب محاصره را برداشتند، نه ۳۰ روز بعد از تفاهمنامه، همان شب. توییتی ترامپ زد و گفت ما امشب برمی‌داریم. زیرش هم نوشت البته ایرانی‌ها هم تنگه هرمز را باز خواهند کرد. وقتی این را دیدم، جلویش را گرفتم و گفتم ما چنین توافقی نداریم.»
«به میانجی‌ها گفتم که این توییت اگر الان برداشته نشود، می‌زنیم به همان شدتی که من گفتم می‌زنیم. ۵۸ دقیقه بعد ترامپ بخش دوم را برداشت و نوشت تنگه در چارچوب تفاهمنامه از روز شنبه باز می‌شود.»
«این مذاکره یعنی مبارزه.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77876" target="_blank">📅 18:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77875">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTmd8xYZZjkCLvz7wRYauMx6-kCOiUwJmco9zgxc7lBlPKrCZ4LD5qIYhN9dRGxG4x_0ph2vEcC-unPcDzTvLrjDyDbHDLmjspFm49mNiJGUbJ2XmPBYGUMDAM6YwDfgRpxuvq04sMZAvwvYOdE_6vOQGs1BzNnmFkkEECh3s54VVkXFYSH63kB_ojmQ4w8N6JmaKBUToN7uew0juUMjSedL8ia_aJdodIpGujduV9MESbzXpzNvz8McxAXC4yXs5DJs21aewIesni_mwjkWq7ULkQVVwLhtlEhtTXe8IB3lydvWrXSEeqRFXOAtaQ97Pg_8syeo-vR-5ZodNrDOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپهر امیرزاده، از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴ در اصفهان، از سوی دادگاه انقلاب به اتهام «محاربه» به اعدام محکوم شده است. پرونده او هم‌اکنون برای بررسی در دیوان عالی کشور قرار دارد.
🔸
بنا به گزارش خبرگزاری هرانا، آقای سپهر امیرزاده در ۲۳ دی ۱۴۰۴ در منزل خود در اصفهان توسط نیروهای امنیتی بازداشت شد و پس از طی مراحل بازجویی به زندان دستگرد اصفهان منتقل شد؛ جایی که همچنان در آن محبوس است.
🔸
جزئیات بیشتری درباره مصداق اتهام «محاربه»، مستندات پرونده، روند بازجویی و نحوه برگزاری جلسات دادگاه منتشر نشده است. آقای سپهر امیرزاده، متولد ۱۳۸۲ و اهل رامهرمز خوزستان، مدرس و نوازنده موسیقی و ساکن اصفهان است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77875" target="_blank">📅 18:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fjZjT7Pnx4vnpfUxitX2t0EFu5ncjabqszkJJ0nJzFl66ES7A5BvBNTGEkzQil04TUGXLGNfbV-aosKB-3e1ywoyu8oD31QP1Ku6I7zGbV1m3UoViLEaA-ksf4aNhE1nhMQfB0W_kvR_roHDqOi-DnnWu6XI144k3TVdULaVRbWom1fG1vHS7kyHjRSO46mAkHSots9hzIQsZ5peFOK65SYEsuWCIvl2XVRAB8-8uE_zudNCDnj3f51M37HpT8CnvwXmDnVW6YcxSavO0iT7aa2_tTwjaAsl4fbxlrAtfbBgCUHD7n7G_vKtom6DqhNRe1Z7HylIALtdExquOGZg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ روز جمعه در نیویورک با اشاره به حملات آمریکا و اسرائیل به ایران گفت: «آن‌ها دیگر رهبری ندارند. رده اول آن‌ها از بین رفته، رده دوم از بین رفته و نیمی از رده سوم هم از بین رفته است.»
او افزود که این وضعیت، مذاکره با جمهوری اسلامی را نیز دشوار کرده است: «یکی از مشکلات من این است که کسی برای مذاکره وجود ندارد.»
ترامپ سپس با لحنی تمسخرآمیز گفت ایران «تنها کشور جهان است که هیچ‌کس نمی‌خواهد رییس‌جمهوری آن باشد.»
رییس‌جمهوری آمریکا همچنین مدعی شد سامانه‌های راداری و تجهیزات پیشرفته اطلاعاتی جمهوری اسلامی از بین رفته و توان تولید موشک ایران ۸۲ درصد کاهش یافته است.
به گفته او، جمهوری اسلامی همچنان تعدادی موشک و پهپاد در اختیار دارد، اما این تجهیزات تنها بخش کوچکی از توان پیشین ایران را تشکیل می‌دهند و ظرفیت تولید آن‌ها نیز به‌شدت آسیب دیده است.
ترامپ در بخش دیگری از سخنانش، گزارش‌های رسانه‌ای درباره وضعیت ایران را هدف حمله قرار داد و با اشاره به تورم و کاهش ارزش ریال گفت ادعای عملکرد موفق جمهوری اسلامی در جنگ با واقعیت‌های اقتصادی این کشور هم‌خوانی ندارد.
وزیر خارجه جمهوری اسلامی روز شنبه ۲۴ مرداد در گفت‌وگو با «شهرآرانیوز» گفت هیچ مذاکره‌ای میان ایران و آمریکا در جریان نیست و تهران هنوز درباره از سرگیری مذاکرات تصمیم نگرفته است.
عباس عراقچی گفت قطر و پاکستان با تهران و واشنگتن در تماس‌اند و میان دو طرف پیام‌هایی ردوبدل می‌کنند، اما این ارتباطات به معنای آغاز مذاکره نیست.
وزیر خارجه جمهوری اسلامی همچنین گزارش‌ها درباره وجود یک «آتش‌بس ۶۰ روزه» را رد کرد.
به گفته او، در تفاهم‌نامه اسلام‌آباد از «پایان جنگ» و تعیین یک مهلت ۶۰ روزه برای گفت‌وگو درباره توافق نهایی سخن گفته شده بود، نه آتش‌بسی که اکنون نیازمند تمدید باشد.
عراقچی مذاکرات تهران و مسقط را نیز «فنی و تخصصی» خواند و گفت ایران و عمان در حال تعیین مسیرهای دریایی تازه‌ای برای عبور کشتی‌ها از تنگه هرمز هستند.
نیروهای مسلح دو کشور نیز در این گفت‌وگوها مشارکت دارند.
به گفته او، ابتدا یک مسیر موقت برای رفت‌وآمد کشتی‌ها تعیین خواهد شد که ممکن است مبنای مسیر نهایی قرار گیرد.
عراقچی در عین حال تأکید کرد تعیین مسیر کشتیرانی و بازگشایی تنگه هرمز دو موضوع جداگانه‌اند.
او بازگشایی این آبراه را به تحقق شروط جمهوری اسلامی از سوی آمریکا مشروط کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77874" target="_blank">📅 11:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=C2rRDQeHWtr9BcoOwWXwrzwsyLZ5jz8h0_qXP7E1j2WQNE5XExCt_2JTo3c54CfxybDaUiRz3d68aEnN4R7Q696z4atyk729tlUKbJ7nqWEMO7CLdHecZn2CnDcjNcRmeczqdRI-_Us9K8K89CJSf6xkVAUox-RgCIdQ_0BgR1n2CDBNf7JOW1fvlZerMKZ2ZWGgRALe2ASmBdhB5llNWx7LyJTQo9wH7DbyPhpmjIIwKVc1-FuFycITPGBDjqJ7DjO3RjPYrTVq0uQUuVJWmhxRTrDMx9fr8uSqQ2JaU5YJ2CSq-C9t8RAfyBTkceuZu6bFYlgdRaEDxJ9G1TiajA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3500bcce36.mp4?token=C2rRDQeHWtr9BcoOwWXwrzwsyLZ5jz8h0_qXP7E1j2WQNE5XExCt_2JTo3c54CfxybDaUiRz3d68aEnN4R7Q696z4atyk729tlUKbJ7nqWEMO7CLdHecZn2CnDcjNcRmeczqdRI-_Us9K8K89CJSf6xkVAUox-RgCIdQ_0BgR1n2CDBNf7JOW1fvlZerMKZ2ZWGgRALe2ASmBdhB5llNWx7LyJTQo9wH7DbyPhpmjIIwKVc1-FuFycITPGBDjqJ7DjO3RjPYrTVq0uQUuVJWmhxRTrDMx9fr8uSqQ2JaU5YJ2CSq-C9t8RAfyBTkceuZu6bFYlgdRaEDxJ9G1TiajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: تنگه هرمز را قلمروی آمریکا اعلام خواهم کرد
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، طی یک سخنرانی در جمع نیروهای مجری قانون در «لانگ‌آیلند» در ایالت نیویورک گفت: پس از آنکه شکست دادن ایران را تمام کنیم، که هم‌اکنون نیز به سختی در حال شکست خوردن است، خیلی زود تنگه هرمز را قلمرو ایالات متحده اعلام خواهم کرد.
در اصل هم ماجرا همین است، ما محاصره را در دست داریم و هیچ کشتی‌ای از آن عبور نخواهد کرد مگر اینکه ما بخواهیم.
@
VahidOOnLine
برایان شوراتز، خبرنگار وال‌استریت ژورنال می‌نویسد که به گفته یک مقام ارشد کاخ سفید دونالد ترامپ، رئیس‌جمهوری آمریکا، با مشاوران خود درباره اعلام تنگه هرمز به‌عنوان قلمروی ایالات متحده دیداری نداشته و هنگام مطرح کردن این موضوع در سخنرانی روز جمعه خود در ایالت نیویورک، در حال شوخی بوده است.
آقای ترامپ پس از بیان سخنانش درباره تنگه هرمز خنده‌ای کرد. او پیشتر نیز درباره برداشت رسانه‌ها از شوخی‌هایش، صحبت کرده است.
رئيس‌جمهوری آمریکا در سخنرانی روز جمعه خود اشاره کرد که آمریکا عملا تنگه هرمز را تحت کنترل دارد چون هیچ شناوری بدون اجازه آمریکا نمی‌تواند از آن عبور کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/77873" target="_blank">📅 00:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=QrUIpH63aaZ2KSW1VpVSURryQWvrTmUmsMhqUErop6RJqmwD4NM6AS0nuoQ8FVOaJUBSLBpk70e9YQRx4AA-wsrOwvWY5aMX4RRSdZAbUpMV9MGgMvYAkmNB1xpkj-Wq0OIt5cPV13UYBH8W7GHhyySDetnOOQlxRNHavdpyufor-lZBKqjhnZhDvrutvvyOcaeoFYzqDHg4BMHCwJ_F1ZapVRYKMbOjiGsQMSVEGWzozFdCyn67hVy0_dirkUkqOrv8A6hkzK9xWvyaMkIIvR2b5MTbpXDyxcxGvHuFGSndkeM7DrcfACApLG8-lmMuhE9x_I_D3XS0Xcdu8ua3Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d41b4db679.mp4?token=QrUIpH63aaZ2KSW1VpVSURryQWvrTmUmsMhqUErop6RJqmwD4NM6AS0nuoQ8FVOaJUBSLBpk70e9YQRx4AA-wsrOwvWY5aMX4RRSdZAbUpMV9MGgMvYAkmNB1xpkj-Wq0OIt5cPV13UYBH8W7GHhyySDetnOOQlxRNHavdpyufor-lZBKqjhnZhDvrutvvyOcaeoFYzqDHg4BMHCwJ_F1ZapVRYKMbOjiGsQMSVEGWzozFdCyn67hVy0_dirkUkqOrv8A6hkzK9xWvyaMkIIvR2b5MTbpXDyxcxGvHuFGSndkeM7DrcfACApLG8-lmMuhE9x_I_D3XS0Xcdu8ua3Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«بریم نجف» از نوحه حکومتی تا ترند شبکه‌های اجتماعی علیه سفر اربعین
همزمان با راهپیمایی اربعین، انتشار ویدئوهای بلاگرهای حامی حکومت با نوحه «بریم نجف، پس می‌ریم نجف» به سوژه کاربران شبکه‌های اجتماعی تبدیل شد.
کاربران با استفاده از همین صدا، ویدئوهایی متفاوت ساختند؛ از سفر و تفریح به جای رفتن به نجف تا کمک به نیازمندان و غذارسانی به حیوانات بدون سرپرست.
اما ظاهراً همه این ویدئوها بی‌هزینه نبودند؛ زنی که ویدئویی از غذارسانی به حیوانات با همین نوحه منتشر کرده بود [ویدویی دوم بالا]، به پلیس فتا احضار شد. [همه پست‌های قبلی‌اش حذف شد و پستی از طرف حکومت در صفحه‌اش درج شد]
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/77871" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=gbdDIL4hmLvG8kJLshoNd74dIoCSumCB7Ni0wiqu6fUXRdw9JYo4z7LfjQO9bJSRjg7iAK-0mg7Mc-dN4OiG84vaA_uX6XkBYYoRczAJ3yPJgw_hLdvNAme6bmVSYt7M09NeFDAHhJjBNbJIkjUG9KUxFH-b7TuZqHfo3zyONhKpvJg0B427y_YYzSmd7mvnH4rRWyYR9DmJpQ_DYP6RB7yYmZt2QdUymVK7rJU_oS0xnwHro4coTbRrz269MyfHgRzv7yEcjzoudOpdTo5duTfOYfcWvNbH7wzEmxuIbXUg-7wWDLyi1jrC8nol-m7tDzkQtmhvn1wRzgrSIFgrQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c594f01e2b.mp4?token=gbdDIL4hmLvG8kJLshoNd74dIoCSumCB7Ni0wiqu6fUXRdw9JYo4z7LfjQO9bJSRjg7iAK-0mg7Mc-dN4OiG84vaA_uX6XkBYYoRczAJ3yPJgw_hLdvNAme6bmVSYt7M09NeFDAHhJjBNbJIkjUG9KUxFH-b7TuZqHfo3zyONhKpvJg0B427y_YYzSmd7mvnH4rRWyYR9DmJpQ_DYP6RB7yYmZt2QdUymVK7rJU_oS0xnwHro4coTbRrz269MyfHgRzv7yEcjzoudOpdTo5duTfOYfcWvNbH7wzEmxuIbXUg-7wWDLyi1jrC8nol-m7tDzkQtmhvn1wRzgrSIFgrQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدر عباس قنبری، در سالروز تولد فرزندش، با حضور بر سر مزار او در گویم شیراز سوگوارانه می‌رقصد و یادش را گرامی می‌دارد.
عباس قنبری، مهندس و ورزشکار اهل گویم شیراز، روز ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در مقابل کلانتری گویم، بر اثر اصابت گلوله جنگی جان باخت. از این معترض جان‌باخته، یک دختر خردسال به یادگار مانده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77870" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/azBrVx2zAJNH2KkQsveRnvIiN1ZvYh2MJY8Xr8kprwVfBMrom5um_grYLMtaFrsmVZj1vlloXT9-k2dsR3jrwz4PvpbpmT8dK5-2wdQlwJUCU80ZS3g-JD8Nih6RfuuwKeSS_UbXRYxH03lEFI_CbT-fFc2-G_6sMsgK5ZEcd9RIDz-ejm0O6wl2oi9XCr4zwdSogLokJlLAWonFcTAuUm0UsnNmXVMwRjmKylLsKxG5Wwjy4XP-WWEVGJbUXCvEfdTIsJ57fK9e7pLyboAslh_Fc5ozHHAPtbIt2Y5BUCnmt3NvN8R3ShaRr1uPOvwxuSKsBB58O9PiwEfrzVXjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم طهماسبی، عروس معصومه ابتکار، از گروگانگیران سفارت آمریکا در تهران، که به همراه همسر و فرزندش بازداشت و هم اکنون در مرکز پردازش اداره مهاجرت آمریکا در تگزاس نگهداری و منتظر اخراج از آمریکا هستند، نامه‌ای خطاب به مردم آمریکا در نشریه «نیشن» به همراه عکس بی حجاب خود منتشر کرده و از عمق علاقه خود به آمریکا صحبت کرده است.
وی در این نامه گفته است که او و همسرش عیسی هاشمی، «معلم و استاد دانشگاه از طبقه کارگر هستند» و پسرشان، فقط انگلیسی صحبت می‌کند و از دوران پیش‌دبستانی در نظام آموزشی کالیفرنیا پرورش یافته است.
پسر و عروس معصومه ابتکار با ویزاهایی که در دولت اوباما صادر شده بود، در سال ۲۰۱۴ وارد آمریکا شدند و چندی بعد اقامت دائم دریافت کردند.
دفتر سخنگوی وزارت خارجه آمریکا ۲۲ فروردین‌ماه اعلام کرد که کارت سبز (گرین کارت) مریم طهماسبی و عیسی‌ هاشمی را لغو کرده و آنها به همراه پسرشان در تاسیسات تحت نظارت اداره مهاجرت آمریکا نگهداری می‌شوند. در این بیانیه به نقش محوری معصومه ابتکار در ماجرای گروگانگیری اعضای سفارت آمریکا در تهران اشاره شده است که اندکی بعد از انقلاب ۵۷ اتفاق افتاد.
مریم طهماسبی در حالی در نامه خود مدعی شده که مادرشوهرش «فقط برای گروگان‌گیران مترجمی می‌کرد» و «ماجرا مربوط به ۵۰ سال پیش است» که معصومه ابتکار در پاسخ به یک خبرنگار خارجی که از او پرسید «آیا حاضری اسلحه به دست بگیری و گروگان‌های آمریکایی را بکشی؟»، پاسخ داد: «بله».
معصومه ابتکار در دهه‌های بعد نیز اعلام کرد که از شرکت در گروگانگیری اعضای سفارت آمریکا در تهران پشیمان نیست. گروگان‌های سابق از جمله بری روزن نیز معصومه ابتکار را یک بازجوی عصبانی و خشن توصیف کرده‌اند.
کارزار درخواست اخراج فرزندان و وابستگان مقامات جمهوری اسلامی که در آمریکا اقامت دارند، با کشتار معترضان در دی‌ماه ۱۴۰۴، شدت گرفت و همزمان خبرهای اخراج برخی از آنها از جمله فاطمه لاریجانی، دختر علی لاریجانی، دبیر کشته شده شورای عالی امنیت ملی منتشر شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77869" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AfSXD80tLHbT18WCW2mMofa3c9R4b2zFt65twlsSgWKjDcU4EBZw2UbOkIQmzNTG9CUVgFcT11twrsXgFks00zn3m5xgSfR563Q369hI-3IM4fulGTaiaDi53YCnYjpldNoJSfQwopvrl30fd8_KXfogHOUC6WlO4E9qutfyEW8n7JausnW0rvuLuXidPZSXv_twoVa9haAJEAZZqNlBYwdAB8wRKC09vOeUHh5XHpguC03bKCHoW_R9Wo5HC9KyrsT6YYjn0V6nONVKLvW1ZWFg0kGjCbwpVnUovyiDN6oIvb1R8QXCusrdWKN3xwJOh9tDbGoQVwUVZhPW14-iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=RLLFy-xPdP9b0bEN4b4H85dozPSh4MXgSSvcXlzaDgpDppqkLFNKjVzjXcw1XwjIc5n5si24IppcfXw6FAgEPI8eWKHH22ts03fyoILgN14uLWpcBmgqhFHnCLNKZ5K5HUEfbhNSImiGYkwSX4-a6CY685XIvXbxVUvaJIDId2pYsVOjMQorlcTDyvnIKUWBp-I5r06k6-6mbcodksZW6ry9OX1PJUbaxYnO6iPLZMi4IQVdWMAEsaNxTPAMe6OMps3aMhvfvCcFfLkyogQeGJkVGL8aCJ03BnuYmeBAR_hKTkz9wd5F5I4T7PCdxlK4wZzz3BPW6ORptm6KMlIgkw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/193ca661cb.mp4?token=RLLFy-xPdP9b0bEN4b4H85dozPSh4MXgSSvcXlzaDgpDppqkLFNKjVzjXcw1XwjIc5n5si24IppcfXw6FAgEPI8eWKHH22ts03fyoILgN14uLWpcBmgqhFHnCLNKZ5K5HUEfbhNSImiGYkwSX4-a6CY685XIvXbxVUvaJIDId2pYsVOjMQorlcTDyvnIKUWBp-I5r06k6-6mbcodksZW6ry9OX1PJUbaxYnO6iPLZMi4IQVdWMAEsaNxTPAMe6OMps3aMhvfvCcFfLkyogQeGJkVGL8aCJ03BnuYmeBAR_hKTkz9wd5F5I4T7PCdxlK4wZzz3BPW6ORptm6KMlIgkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان یک درگیری میان عزاداران در صحن حرم امام هشتم شیعیان در مشهد، دست‌کم دو نفر زخمی شدند.
به گزارش تسنیم، این درگیری پنجشنبه ۲۲ مرداد حدود ۱۰ و ۳۰ دقیقه شب رخ داده است.
رسانه‌های ایران می‌گویند هیئت‌های مختلف با چوب‌های مخصوص عزاداری مشغول اجرای مراسم بودند که ناگهان میان دو هیئت درگیری شکل گرفت و عزاداران چوب‌های خود را به سمت یکدیگر پرتاب کردند.
تسنیم به نقل از امیرالله شمقدری، دبیر شورای تامین خراسان رضوی نوشت که دو نفر زخمی به بیمارستان منتقل شده‌اند و حال آنان مساعد است.
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با اشاره به درگیری با چوب میان شماری از حاضران در صحن «امام هشتم شیعیان» و هیات‌های مذهبی در مشهد در شامگاه پنج‌شنبه، نوشت که بروز اختلافات سلیقه‌ای در نحوه ورود و خروج یا خستگی ناشی از گرما، امری طبیعی و قابل مدیریت است و نباید به دعوا ختم شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77867" target="_blank">📅 17:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LzeJQZntwEOom0kS-CnDqu5L2EMroJxu6UqMGx-nl3vm4et-RSBCUqZCP82_Q0i1PCOfrLSjyeo315RLWEEK92KzVl3Ahwij5Em90DBuh0zrCIiJHo4G7yNNiemGCBhN3I0G59pPYJkp4jJ2PfDJqXNc2VpwxeLEInW9mTN1JENucyLHRw7Lg5LxtiW125PlWCvz6UQ8hbDSCHncutIHtlkbFqV6zdcbjjxe0LsTFFsxJig1zpU9exI0wOzWqBqAUv8ipJD0tx6NDFCBhkVRjdskJAUa5oNwmhQHENokEIW0pHyseyYbLBpRr83xAlcXoj7tMGNbA9tDQ1QiH2lXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rO39TotvFtm8Ve-GyjsoMoYelhW2CQ-2mqyM1WOndbrOJAom2v8td14Sbtb8wp0CSCJS-eK0bviXvhZ4bnoTZjA6jXSr8sLSbtgg0-fA4uGb7PXmOdDxZINVFmghm4hV_VnH9pao_0DSZ5AT1uQyBWt6aAI536LXg0ktNyJ2Qcp7ys0166EEx_Zv42MOsZyNs-U_-yYYrpTCPH6HAA-fqGBg0DNte2-U834viQLbEsDzij2mlrJvkn4pM1RMUhNhn41A2CsTQLKnYKWJDngOqJYrcu3re1Oo4PF3J61qUaQZVZcB54DUoKxvt2pqG_YpAncDx7JCyggY_WIIWyfi2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با بازنشر گفت‌وگوی اسکات بسنت، وزیر خزانه‌داری آمریکا، با شبکه نیوزمکس در تروت سوشال، بر برنامه دولتش برای تشدید فشار اقتصادی بر جمهوری اسلامی و رساندن «انزوای اقتصادی ایران به سطحی بی‌سابقه» تاکید کرد.
بسنت در این مصاحبه از اعلام اقدامات جدید علیه جمهوری اسلامی در هفته آینده خبر داد. او افزود واشینگتن قصد دارد سیاستی شامل انزوای شدید اقتصادی جمهوری اسلامی و ادامه محاصره در تنگه هرمز اجرا کند.
به گفته اسکات بسنت، این محاصره مانع ورود هرگونه کالا به بنادر ایران یا خروج کالا از این بنادر می‌شود.
@
VahidOOnLine
وزیر خزانه‌داری آمریکا نیز روز پنجشنبه ۲۳ مرداد با هشدار به تهران در مورد اعمال مجازات‌های اقتصادی بیشتر، تهدید کرد که ایران را در معرض انزوای اقتصادی قرار خواهد داد، «به گونه‌ای که جهان تاکنون به خود ندیده است».
اسکات بسنت به شبکه تلویزیونی محافظه‌کار «نیوزمکس» گفت: «ادامه محاصره در تنگهٔ هرمز... مانع از ورود یا خروج هر چیزی به بنادر ایران خواهد شد».
او افزود: «منتظر اخبار و اطلاعیه‌های بیشتری در این زمینه در هفته آینده باشید».
بسنت رویکردی دوگانه را توصیف کرد که شامل فشار مالی و محاصره فیزیکی بنادر می‌شود.
ترامپ اخیراً گفته بود تنها در صورتی از حمله مجدد به ایران خودداری می‌کند که توافقی برای بازگشایی سریع تنگهٔ هرمز حاصل شود.
ایران فهرستی از شرایط را برای بازگشایی این گذرگاه تعیین کرده که بعید است دولت ترامپ آن‌ها را بپذیرد: پایان جنگ در همه جبهه‌ها، لغو محاصره بنادر ایران توسط آمریکا، پایان تحریم‌ها، آزادسازی دارایی‌های مسدود شده و جبران خسارات زمان جنگ.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/77865" target="_blank">📅 17:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EHkmwx2LqkuuSWyx_yVLNL1UhBjJh0xkvBnAfdYbQlIYKTBfkvZ60MfbnxU88ZXQoCWEssIh6nI1B4RmEPAMnUEGoma9hMqBpfXxp7PJHR56vZthreWx9phOois_RA8qb00FRxJ9MP75bgq7EJShNelHRIq2jNIxtbnDidnRtMGC-xYMi_qPwwEFrY7V5kZ2wnaefcYhjn2HNPXq0u3lo9OTt2iWsV5iXwCk2_-cw_0D1XsphweYXsrAA-hlBeh555ad5Tf4zz0eqU7sFBClwChv8eJsaAh8zVaSFQabTkIXs0cXqg4GjdVREuB10dC1OE6XdYL-ndnOL95fYhiiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در یک پادکست رادیو ارتش اسرائیل، با انتقاد از مواضع اخیر بریتانیا در قبال اسرائیل، با لحنی کنایه‌آمیز گفت اولین «جمهوری اسلامی» مجهز به سلاح هسته‌ای، «جمهوری اسلامی بریتانیا» خواهد بود.
نتانیاهو روز پنجشنبه ۲۲ مرداد، در این گفت‌وگو با اشاره به تغییر رویکرد دولت بریتانیا در قبال اسرائیل گفت: چیزی شبیه به جمهوری اسلامی را امروز می‌توان در بریتانیا دید. چیزی که من به آن می گویم جمهوری اسلامی بریتانیا.
نخست‌وزیر اسرائیل در این پادکست همچنین از مواضع بریتانیا درباره جنگ غزه و سیاست این کشور در قبال اسرائیل انتقاد کرد و گفت اسرائیل در شرایطی قرار دارد که باید در برابر تهدیدهای منطقه‌ای از خود دفاع کند.
اظهارات نتانیاهو در شرایطی مطرح شده که روابط اسرائیل و بریتانیا طی ماه‌های اخیر بر سر جنگ غزه، وضعیت انسانی در این منطقه و سیاست دولت بریتانیا در قبال اسرائیل پرتنش‌تر شده است. دولت بریتانیا در ماه‌های گذشته فشارهای بیشتری بر اسرائیل وارد کرده و درباره وضعیت غیرنظامیان فلسطینی و ادامه عملیات نظامی اسرائیل در غزه ابراز نگرانی کرده است.
نتانیاهو در حالی از بریتانیا با عنوان «جمهوری اسلامی» یاد کرده که این کشور متحد دیرینه اسرائیل و یکی از قدرت‌های اصلی غربی است. استفاده از چنین تعبیری از سوی نخست‌وزیر اسرائیل، واکنشی به تغییر موضع لندن در قبال دولت اسرائیل و جنگ غزه محسوب می‌شود.
این اظهارات همچنین در شرایطی بیان شده که دولت اسرائیل همچنان جمهوری اسلامی ایران را یکی از اصلی‌ترین تهدیدهای امنیتی علیه خود می‌داند. نتانیاهو در این گفت‌وگو بار دیگر بر تلاش اسرائیل برای جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای تأکید کرد.
اظهارات نخست‌وزیر اسرائیل با واکنش‌هایی در بریتانیا روبه‌رو شده و برخی منتقدان آن را توهین‌آمیز و بی‌سابقه توصیف کرده‌اند. این اظهارات بار دیگر شکاف میان دولت اسرائیل و دولت بریتانیا درباره نحوه برخورد با جنگ غزه و آینده روابط دو کشور را برجسته کرده است.
@
VahidHeadline
سخنگوی نخست‌وزیر اسرائیل از اظهارات بنیامین نتانیاهو درباره بریتانیا و توصیف این کشور به عنوان یک «جمهوری اسلامی» دفاع کرده است.
روابط بریتانیا و اسرائیل که متحدین دیرینه هستند، از زمان جنگ غزه به شکل محسوسی پرتنش‌تر شده است.
دولت بریتانیا تاکنون واکنشی به این اظهارات نشان نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77864" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SCrl72VUS_H_t6HtjH5joAMD5Z6UqmFd3bPHTteuXCgPqcjcQPpORTnhONM4P5dmIovElErhO6mkEKDMyV1euW55hKWO8oe1426VBKO5vi_0sOSsoDjAKFfz_QMbvtA1BCPQaIP3zHoQbnU4TC0ACik8wpOci9MvO7Y9cJbtkfKNvqSMWT6c6ozKP74VrLch0CHi0i8P6yHU1qUnrKenPOhc0BQQYu4ciT2aJkU0KCLx-Lj4YiPgdS8Ghzc0W5kA4_ZdnhncyeWWm2957Gpw2Dwaz3pqREJE4m_5iCrMC7cu0tQxb41-iHbOUzZQkDJ-GTkgfmux8BMwhMROFrflsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه امارات متحده عربی بامداد جمعه ۲۳ مردادماه با انتشار بیانیه‌ای، حمله به دو نفتکش وابسته به شرکت ملی نفت ابوظبی (ADNOC) هنگام عبور از تنگه هرمز را به‌شدت محکوم کرد.
در این بیانیه آمده است که این حمله بدون بر جای گذاشتن تلفات یا مصدوم، دو نفتکش وابسته به «ادنوک» را هدف قرار داده است.
وزارت امور خارجه امارات این اقدام را نقض آشکار قطعنامه ۲۸۱۷ شورای امنیت سازمان ملل دانست و تاکید کرد که هدف قرار دادن کشتی‌های تجاری یا مختل کردن مسیرهای بین‌المللی دریانوردی، مغایر با اصل آزادی کشتیرانی است.
در این بیانیه همچنین آمده است که هدف قرار دادن کشتی‌های تجاری و استفاده از تنگه هرمز به‌عنوان ابزار فشار یا اخاذی اقتصادی، از سوی امارات اقدامی «دزدی دریایی» از جانب سپاه پاسداران ایران تلقی می‌شود و تهدیدی مستقیم برای ثبات منطقه، امنیت کشتیرانی و امنیت انرژی جهان به شمار می‌رود.
وزارت امور خارجه امارات از ایران خواست این حملات را متوقف کند، تمامی اقدامات خصمانه را پایان دهد و امکان بازگشایی کامل و بدون قید و شرط تنگه هرمز را فراهم کند تا امنیت منطقه و ثبات تجارت و اقتصاد جهانی حفظ شود.
@
VahidOOnLine
عربستان سعودی نیز با انتشار بیانیه‌ای هدف قرار گرفتن این دو نفتکش ناوگان انرژی امارات را «با شدیدترین عبارات» محکوم کرد.
به گزارش العربیه، ریاض در این بیانیه با تاکید بر مخالفتش با حملات ایران به «کشتی‌ها و نفتکش‌های تجاری» در خلیج فارس، تهران را مسئول پیامدهای ادامه این حملات دانست.
پادشاهی سعودی در ادامه با اقداماتی که امارات «برای حفظ حاکمیت، امنیت و منابع خود»  اتخاذ می‌کند، اعلام همبستگی کرد.
@
VahidOOnLine
وزارت امور خارجه بحرین هدف قرار دادن دو نفتکش شرکت ملی نفت ابوظبی (ادنوک) در تنگه هرمز را به شدت محکوم و آن را «باج‌گیری اقتصادی» جمهوری اسلامی ایران از کشورهای منطقه توصیف کرد.
بحرین در این بیانیه در حمایت از امارات متحده عربی افزود، امنیت در تنگه هرمز را برای «حفظ امنیت انرژی، ثبات عرضه مواد غذایی و دارویی و تضمین جریان تجارت جهانی» ضروری دانست و خواستار آن شد ایران از آن برای «اعمال فشار یا باج‌گیری اقتصادی» استفاده نکند.
@
VahidOOnLine
وزارت خارجه مصر نیز در بیانیه‌ای خواستار توقف همه اقداماتی شد که امنیت کشتیرانی بین‌المللی را تهدید می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77863" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XPax1i_8XXg-72paSHV7wYYUU95W0tuoW4GDRnAurClh_rWEwIBDMYQU35s7tHdSDArgGfSp83L93-7ZzrOrNn2LogLea7PaQE5W2xeSySCoN8rxENss-B1RS5o8A1lWlA2I_9eOFD2ENXiee0UKVHSWhPlqp6BD3PrOiFWwBgbq31CO7ZlE0muY8Mwr7E-1v5UqqvlcbMl2ANCVznMhRPeqrD9YF7zE9Q2mCaZfnoymoyfuo1bP7eoSKKzvQ8u9U5mi0EKIKHyvlcQSRFhVLUDLgwRwboq1i54Uizcsznul_u3BvGO7avf6MadbWyZIWHkKN733-iRtPhRBK46YcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی به نقل از شبکه العربیه گزارش داد که مواضع نیروهای آمریکایی در نزدیکی فرودگاه اربیل، مرکز اقلیم کردستان عراق، هدف حمله پهپادی قرار گرفته است.
بر اساس این گزارش، چندین پهپاد به سمت مواضع نیروهای آمریکایی شلیک شده‌اند و به گفته منابع محلی، یکی از آن‌ها به‌طور مستقیم به یکی از این مواضع اصابت کرده است.
العربیه همچنین گزارش داد که در جریان این حمله، سامانه‌های پدافندی آمریکا فعال نشده‌اند و تنها جنگنده‌های آمریکایی برای رهگیری پهپادها وارد عمل شده‌اند.
در پی این حمله، فرودگاه اربیل به‌طور موقت بسته شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77862" target="_blank">📅 16:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJFmXtiAAgS-SljbGrbZREZh4fWu-s9roda5GO2XuQIX9QssX083LBAw0VaW1XppQSH4jI9c45Q0UFwbkoAOD6mXqOPGHV989C1C7Z-ltKz1j-x5LjOEJMoMvgmltTBYCE3xpWQyBzRxcYVkGy6g1ogSaLtsIflZZw4RHLDQZeWzjTuphShUuGZtAi8Xt-iNiNx7ppjGIixlVreybtUPb0hkOqLvqqtlf4hOeUGGvL-ZHUNXjKY7DYxx5MFYWnrl_UDmpnldKtsKGdE3TW-AXkV291ojfLoxpTDn2RQWCqhNPH6nqWV4GPgYfNfWL7bjDimt8jmOZdkGrRy8k9g49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد یک نفتکش هنگام خروج از تنگه هرمز هدف حمله پهپادی قرار گرفته و در این حادثه خسارات جزئی به کشتی وارد شده است.
بر اساس اطلاعیه این مرکز که روز جمعه ۲۳ مرداد منتشر شد، در این حمله همه اعضای خدمه نفتکش در سلامت هستند و گزارشی از آلودگی یا خسارت زیست‌محیطی در پی این حادثه منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/77861" target="_blank">📅 16:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BUQcvJfqx9v3iS8MYd0XP7YcU2cWNHPOTHTTo-hf9_WQGzRx3DMkr5lHXfI5Y69EdBNcfsK9nPUg1pTBslnWMw_BoEnjioqBpM15TJIMPdlk1gTAuHueP7YlDpXGT-qoEpx16NjLDxYbexteIe7iLf_aNdqsTZYdfvFgNIx5LhOaSF1Y_MwGL1EC-81ibzW-OtAsR9EJFjzqGh4mm8leGuDAf8i8lFxQqpUFvKuBpWwo8Mh0N3nhClqjCIT0w58yCO4oayyvKq4nW27qDGQtbb46osn-1cHRe4OLRy7UTb4NxVhlaBbFgSyu8RkZ46fx0f977LSr776K68PgFc593g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد تکتم رمضانی، زندانی ۳۷ ساله که بابت اتهامات مرتبط با مواد مخدر بازداشت شده بود و دوران محکومیت خود را در بند دو زندان وکیل‌آباد مشهد سپری می‌کرد، سه‌شنبه ۲۰ مرداد در پی پارگی کیسه صفرا و تعلل در رسیدگی پزشکی و اعزام به بیمارستان جان باخت.
بر اساس این گزارش، رمضانی در چهار روز پیش از مرگ از درد شدید در ناحیه کیسه صفرا رنج می‌برد و با وجود پیگیری‌های مکرر برای دریافت خدمات درمانی، به بیمارستان اعزام نشد و از رسیدگی پزشکی مناسب محروم ماند. او در زندان به‌عنوان کارگر در بخش جمع‌آوری زباله فعالیت داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77860" target="_blank">📅 16:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n6xX2DblhWY9JI_Qhu0-T7a7X98zgPamQPLHC4VH1rRjo8-YBerZaiixTd-7PAT0rUA1cxUimNyc98c_QmaYBlU-rWDvbklcBz1gmn-M9II2CtPl13ug7ohwZreojz3rfDDed0G3GmNBYlaNGbi1PYJQid6COcEzv2afiN3bvFdwOiLYgeRChQ7q5F4PNWO08QV7Ldi4-hWC6pHSRFJQO2xsEyjX84IH7t4j5NjY8ueI2BJJEcAVjswRCcyeFjP-dUJCOe29cPfCDZiIoaOMMohGWdxdUOZQGctDZzZJBIg-dUrT8SB0ec9z0cOMyTKzmvBWcnnZrkaGa7iETvwkQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PM9ddEewbXB9HBNI3oSPkFOH0z7vsFdAqdJv2Y2WxyOLhvgf3PfsQ5qbPd_-HCLmFp1aS9x928TZbynnF-Hd2q6TzPwSuULnsBazNwB3eGzBSQb_W45YzdFmdjXjklh-AXFvTPKXLy6oLBJ9fpPIBzD_SCllo_fELLJMtNE_JL4SRnCDFHkrEpJgCLRh6x9lRONJGYDYwklilHYA_AHo4jBfBqWZ2UV-fKnMtsUFBLXwu-s_FdywcDP8I-Fb2RevmKPogFeNZ432Y07aDcXvbgXlOrGJkjr6rauo702gXPPeYgj136qOfSXPl_1CH_Udss46nLwuKN6wz1x8P2W_Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واشینگتن‌پست در سرمقاله‌ای نوشت توافق با جمهوری اسلامی و تزریق منابع مالی بیشتر به تهران، به رفتارهای «مخرب» این حکومت پاداش می‌دهد و زمینه‌ساز دور تازه‌ای از بی‌ثباتی خواهد شد. این روزنامه از دونالد ترامپ خواست مذاکرات را متوقف کرده و سیاست مهار جمهوری اسلامی را ادامه دهد.
هیات تحریریه واشینگتن‌پست جنگ آمریکا علیه جمهوری اسلامی را از نظر راهبردی ناموفق توصیف کرد و نوشت این درگیری نه به تغییر حکومت انجامید و نه توان موشکی و فعالیت نیروهای نیابتی تهران را متوقف کرد. به نوشته این روزنامه، هرچند حملات برنامه هسته‌ای ایران را به عقب انداخت، اما انگیزه تهران برای دستیابی به سلاح هسته‌ای را نیز افزایش داد.
واشینگتن‌پست همچنین نوشت تفاهم پیشین میان واشینگتن و تهران نتوانست اختلاف بر سر کنترل تنگه هرمز را حل کند و ازسرگیری حملات نیز تغییری در واقعیت‌های میدانی ایجاد نکرد. این روزنامه با تاکید بر تاثیر تحریم‌ها و محاصره دریایی بر اقتصاد ایران، پیشنهاد کرد آمریکا به‌جای توافق، فشار اقتصادی، محدودیت صادرات نفت، مقابله با نیروهای نیابتی و سیاست مهار جمهوری اسلامی را ادامه دهد.
@
VahidOOnLine
شورای سردبیری واشنگتن‌پست در مقاله‌ای با اشاره به موثر بودن سیاست مهار حکومت ایران و اعمال فشار اقتصادی و محاصره دریایی و در مقابل کاهش کارایی کارت تنگه هرمز در دست ایران، استفاده تهران از این اهرم را به گروگانی تشبیه کرد که از پیش گلوله خورده است.
در این یادداشت آمده است: «تصرف تنگه هرمز از سوی ایران را می‌توان نوعی گروگان‌گیری دانست، اما گروگان از پیش هدف گلوله قرار گرفته است. بازارها عملا بسته شدن تنگه را در قیمت‌ها لحاظ کرده‌اند. قیمت نفت، هرچند بالاست، اما فاجعه‌بار نیست.
علاوه بر این، تأمین‌کنندگان نفت در حال دور زدن این مشکل هستند. دولت ترامپ مدعی است که اکنون روزانه ۵ تا ۷ میلیون بشکه نفت از طریق خطوط لوله ارتقایافته و پایانه‌های جدید صادراتی از منطقه خارج می‌شود. عربستان سعودی نیز در حال تشکیل ائتلافی چندملیتی برای حفاظت از کشتیرانی در دریای سرخ در برابر نیروهای نیابتی ایران است؛ اقدامی که واشینگتن باید با ارائه پشتیبانی اطلاعاتی و فرماندهی از آن حمایت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77858" target="_blank">📅 05:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hAZZomJd7JfPIrTXehLTaqLKhn4CMMZA_q2DD5LF6esWXNmaHNGK9DhmC21qI2HMbvx-7noz0Ofeq6Kj5GYmc-stLxoEw8_LuxQFvPoT24h0D2acUasoPmRcAAT565Xhw7SKuFAMetHa9ZgR7gRi45Ee9ftXY_wFEBq9uRyTtpbQpR9-SvExsAtSNMHbfn5UOaVCsu3rQaFgfA60KwmXTtMbeNTURs4Gsdx5hp52ql1epFakySkYo20LLKoTkOqwIGpAV2O3Yi9BXUh5QdTh295MxmyRwcTUizddfgyeYaUaCoPsVCojuqsXFcpNoA47Ccgr8MGdVxp_HyiEOOik-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عربستان سعودی (واس) گزارش داد شاهزاده محمد بن سلمان، ولیعهد و نخست‌وزیر این کشور، جمعه ۲۳ مرداد با دریاسالار برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده، سنتکام، در جده دیدار کرد.
بر اساس گزارش واس،  شاهزاده محمد بن سلمان و برد کوپر در این دیدار درباره همکاری‌های دفاعی عربستان سعودی و ایالات متحده گفتگو کردند و آخرین تحولات منطقه را مورد بررسی قرار دادند. دو طرف همچنین درباره تلاش‌ها برای کاهش تنش‌های منطقه‌ای و تقویت امنیت و ثبات گفتگو کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77857" target="_blank">📅 05:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1726204da.mp4?token=fXVXpbTENanQ9eMJhFpofyycVDox3Hbpxqvqa_9cdDOLcWk8v_pUdEoZpIA9Yxa5ZJ1NLLMAg1DsKpP0PTsOSJFptD4FFhD2J5sGMGLofyvaaGFiWq8O-uNpdvSwZfXStntPjvx-5hB2_cR7eSikxoEv4OVXKa5i1NN9sLprC5NKXh_6WFrrL8Q0lxTej3yrzxR52LZoGbpCD6_GKsNplVIUIXjPeJ9Hd3jLe7en715_wlooHtMCxAZGvvbjq2hhOtr3agkS47nYeO8yBqy9AKU03oGq1uP8ttr-mb-OnpkRx69L43lRpU6PTqYb1sK5Pvbm8uZGK14MX4BOFAzJag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1726204da.mp4?token=fXVXpbTENanQ9eMJhFpofyycVDox3Hbpxqvqa_9cdDOLcWk8v_pUdEoZpIA9Yxa5ZJ1NLLMAg1DsKpP0PTsOSJFptD4FFhD2J5sGMGLofyvaaGFiWq8O-uNpdvSwZfXStntPjvx-5hB2_cR7eSikxoEv4OVXKa5i1NN9sLprC5NKXh_6WFrrL8Q0lxTej3yrzxR52LZoGbpCD6_GKsNplVIUIXjPeJ9Hd3jLe7en715_wlooHtMCxAZGvvbjq2hhOtr3agkS47nYeO8yBqy9AKU03oGq1uP8ttr-mb-OnpkRx69L43lRpU6PTqYb1sK5Pvbm8uZGK14MX4BOFAzJag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا گفت که اولویت اصلی ایالات متحده در جنگ با ایران دیگر برنامه هسته‌ای این کشور نیست، بلکه کاهش قیمت بنزین برای مصرف‌کنندگان آمریکایی است.
جی‌دی ونس به شبکه فاکس نیوز گفت که جلوگیری از دستیابی ایران به سلاح هسته‌ای اکنون در مقایسه با برقراری مجدد جریان آزاد نفت از طریق این تنگه، در اولویت دوم قرار گرفته است.
معاون رئیس‌جمهور آمریکا افزود: «می‌دانم که قیمت نفت امروز کاهش یافته و نسبت به اوج قیمت‌ها در روزهای اولیه درگیری بسیار پایین‌تر آمده است. این هدف شماره یک است؛ ارزان نگه داشتن نفت و گاز برای آمریکایی‌ها در سراسر کشورمان».
او تصریح کرد: «و البته هدف شماره دو این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند».
این اظهارات در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، همواره برنامه هسته‌ای ایران را به عنوان دلیل اصلی خود برای جنگ مطرح کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77856" target="_blank">📅 05:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XzosrMehtAEiKtgZo9JcH9zOIOAFCq-Sozy5C-U22Mm5DJDwD9d81S5A9-WsY6SS9_jXbxiLDBmR1oUjsDqmWURNvJZI-XzhR-6HgO6zmp-yHnTFij9HM0bKLB1crp3MYyUFqAHfQ7SkTSgXn9qUsQUTChydKVXSu1hKDWAjUuAcfwvVGTRENzfrSJQ1nEVN-NW3g1FAnbFfUN7a6d8gsuK4bzLr-qFLM6yzvPT5xdknjsA0-OatUisB2AEhRFSgPbQfWW-qfYnDmdJWbxjl-UebpqimAqcBo06vP96v_kosfO6Uqgz7snq6eum_oOJW0F-HkSeSU_niSRbgKldTIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پیام‌ها از زمین‌لرزه حوالی اندیمشک و دزفول در شمال استان خوزستان خبر می‌دن.
آپدیت:
تصویر و پیام دریافتی:
بزرگی زلزله: ۴.۵
حسينيه، خوزستان
عمق: ۸ کیلومتر
زمان زلزله: ۱۴۰۵/۰۵/۲۳ ۰۰:۵۳:۴۷.۹
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77855" target="_blank">📅 00:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLLT3RsZ5GGYyS2L1LARFJuDK4OO9knZ4iAhZqfrkzh29AUtxBXojuIbu2XsXWZpWR9FDqnhdadobQ4rc-9RXt5veybse9NSArPMOnNGsWPxmIBuAmVxI5FAI2gomTMbvQqFhky3v1dugX62qI0HdYSHjQZvWxSRNXglWfCk0i2fBVVex4KD5uc7_DY8VgxXfEPDbovhYxik2chjsBQGZLo2k0s13YRPn_VNwjowmvzzCVXHw235zI5tBSPYBOlX5nYEC-N68AT9v3Xb0ceGDsB5-uUtpMNwQxEFIXBB-m21fB_JXmaxYHnBOzGKVQ8UvqrGNo4nFXqdP-iVOLxNAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، سنتکام، روز پنج‌شنبه ۲۲ مرداد از آغاز روند تشکیل نخستین یگان چندملیتی و چندحوزه‌ای پهپادهای تهاجمی خبر داد.
این یگان با نام «نیروی ویژه فالکون استرایک» از پهپادهای یک‌طرفه تهاجمی و سامانه‌های بدون سرنشین هوایی، سطحی و زیرسطحی دریایی استفاده خواهد کرد و نیروهایی از آمریکا و شرکای منطقه‌ای در آن مشارکت خواهند داشت.
سنتکام اعلام کرد رایزنی و دعوت رسمی از کشورهای شریک در منطقه برای پیوستن به این یگان آغاز شده است و با پیوستن آن‌ها، «فالکون استرایک» توانایی‌های پهپادی تهاجمی در خاورمیانه را در قالب یک ساختار چندملیتی و چندحوزه‌ای ادغام خواهد کرد.
«فالکون استرایک» ۹ ماه پس از تشکیل «اسکورپیون استرایک» راه‌اندازی می‌شود. به گفته سنتکام، این یگان پیش‌تر از پهپادهای یک‌طرفه تهاجمی در عملیات نظامی علیه ایران و همچنین از شناورهای بدون سرنشین تهاجمی در حملات ماه ژوئیه به تأسیسات بندری ایران استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77854" target="_blank">📅 21:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FVNxoEk7ALyIXs2ZrsQsK7gh8vekGODCtOS_DhdlwjeVuic68tsL3RLlMC5047SSVpQHYZguGX-K_AfECLMu9oBC77x_8PBWot_AnzzBMmXjLjiig420dpRhBcGalYNzosYA_5n1AdfNIfjx4K9XG1F2F17yKDkWsiAD8F7d46qGWn8wEz6aqzEJOQZNQnWLxdZ-oWrRc8CBunTdaTMOv5GrqeBMS_N2e_kzws-7jgq1ONXTkXM59mQ9lIlbUk_kNmStf97sXHCHUYqugnCdYeQhH42ltyqsdGvAsGks11rRKM0a58JWWU5Hueo4iGvzrHTKndK-BJtTDNqO1diIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها چهار روز پس از یک حمله پهپادی به بندر جیزان در عربستان سعودی، خبرگزاری وابسته به حوثی‌های شیعه یمن روز پنج‌شنبه از حمله‌ای دیگر به پالایشگاه آرامکوی مستقر در این بندر خبر داد.
در حالی که هنوز منابع خبری سعودی در این باره اطلاع‌رسانی نکرده‌اند، خبرگزاری سبای یمن نوشته است که این پالایشگاه «با دو پهپاد» هدف گرفته شده است.
روز یک‌شنبه هفته جاری هم این پالایشگاه در پی حمله پهپادی حوثی‌ها دچار حریق شده بود.
جیزان در ساحل دریای سرخ و در نزدیکی مرز یمن و در تیررس حوثی‌های شیعه یمن قرار دارد که از حمایت جمهوری اسلامی برخوردارند.
آرامکو روز پنجم مرداد پس از حمله حوثی‌های یمن که به مجتمع سیکل ترکیبی یکپارچه گازسازی (IGCC) و بخش مخازن پالایشگاه آسیب رساند، فعالیت این تأسیسات را متوقف کرد.
حوثی‌ها در آن زمان اعلام کردند که تأسیسات آرامکو در جیزان و ینبُع را هدف قرار داده‌اند.
پالایشگاه جیزان ظرفیت فرآوری روزانه ۴۰۰ هزار بشکه نفت خام را دارد و فرآورده‌های پالایشی از جمله بنزین و گازوئیل با گوگرد بسیار پایین تولید می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77853" target="_blank">📅 21:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gscGffddoRQzuT1dufkfwoK0HBmfZsDIQWF7chwSOZteQaZJh1LJn1kJJUcPz-G2vKsiUp_2oTCIBziE0lTI2Jwf2A9wZ2L4_2xAGqKjHp6pm0-PSE8L4td1VSaWQqLkcSgLvXb6RldOlz5GnT_NdF0j494PWffelZutoCfHs5IUm4yhzYqCnM_x-VkrO7cP__Nd_SEEOrbJ2_JPy-mBu7FWmBwUG7p8kSUsfY-VMDhvA9E5w-Mnbl4qnf3nNvM67_Po-bvoj5oGPhBhLu_KEFv_fGt22bznKHjn5bVAHu0N77nzb2JMMbmpYWx5G3l5_3v1uiaf14L8purrEV4t5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mYRvZzCiksXp0eWeW-0m2GeGqFez-0rmutDfSuJjc5OEqDAzdb4M4cwT1wtXq7EKxyvFtqLMVv0e9j1Dk9l-Ubi0kF_eBClSxmBPHktgZWvRXV1EgsEHHPRhmOqKoVU9pKjxlbJ5GDXbv1hmUzR3Z2_05KtWgM74Z4EOcrjP41dt-gyHNzpxezu2A_6m5hAW24TO6hZrXMkey5ek_ha-er2JEYayUdXGbjh-KZLSHjeUAKvtaW_TEu_VbkOf3rIW3M_zbtt0WhbvRcV34WGfdVadx_EamjtHnWA7IFgHMDvI-osN0DOY1w7Dtrcw9nJGUG-hwnPAbXYq7sqsEestdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا،‌ روز پنج‌شنبه در گفت‌وگو با خبرنگاران تأکید کرد که ارتش این کشور قادر است «تا زمانی نامحدود» به محاصره دریایی بنادر ایران ادامه دهد.
هگست گفت: «نیروی دریایی آمریکا قادر است به طور نامحدود به محاصره دریایی ایران ادامه دهد، چون همان طور که تا الان کرده‌ایم، می‌توانیم کشتی‌ها را [عوض کرده و] وارد و خارج کنیم، و به این کار ادامه خواهیم داد.»
مجیدرضا حریری، رئیس اتاق بازرگانی ایران و چین، در هفته جاری ضمن هشدار درباره این‌که «زندگی در محاصرهٔ دریایی به سطح نازلی سقوط خواهد کرد»، گفت انتقال بار از چین به ایران از راه زمینی «حدود ۱۸ میلیارد دلار هزینهٔ اضافی به اقتصاد ایران تحمیل می‌کند».
@
VahidHeadline
روزنامه وال‌استریت ژورنال به نقل از مقام‌های آمریکایی آگاه گزارش داد که ایالات متحده در چارچوب یک برنامه از پیش تعیین‌شده، ناو هواپیمابر «یواس‌اس جورج واشنگتن» را برای جایگزینی ناو «یواس‌اس آبراهام لینکلن» به خاورمیانه اعزام می‌کند.
ناو آبراهام لینکلن بیش از ۲۵۰ روز در ماموریت بوده و طولانی شدن استقرار آن و محدود بودن توقف‌های بندری، نگرانی‌هایی را در میان شماری از قانون‌گذاران درباره شرایط زندگی خدمه ایجاد کرده است.
در همین حال پیت هگست، وزیر دفاع آمریکا نیز گزارش‌ها در مورد شرایط بد در ناو هواپیمابر آبراهام لینکلن را «کاملاً تحریف شده» خواند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77851" target="_blank">📅 19:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7ENjh1dqprpdUi8JC-gRIMI5C-f5iXafFwARrJyjFDppZ0FfFa_fi44sCyHofqlrsLZU47WVPEwHI3LFmUfX4mODjCX4cckk8m3gWqA8Y0FnwvmmaMJs2IIDKyU8kAwc_ERT4Rtmhs4HQhzIS1UfNx90wd4wdvfAK_dcVgfWymYCiRSYpGDoqNgIqsvSNp2nRG5-fz7YZbiaC7kL5o4GwXzQgdyebiGmWp2ELGBL6LdVoKrNnhwveqJZLsyXGVNHCQsjCRoxQYHJcb6esbQRvR8SRkdGD9ERR_4IwDVffhYsNGO65zhRCthRhKC_A0ZGko459KQIrkOSol-l7POgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور مجتبی خامنه‌ای، روز پنجشنبه ۲۲ مردادماه در شبکه اجتماعی ایکس نوشت که «راهبرد قطعی رهبری» در صورت تحقق نیافتن شرایط ایران، تهاجمی شدن جنگ است و این راهبرد «معادلات قدرت را در جهان دگرگون می‌کند».
مشاور رهبر جمهوری اسلامی در ادامه ادعا کرد آمریکا در محافظت از متحدانش در خلیج فارس ناتوان بوده است. او اجرای «سازوکار اقتصادی-امنیتی هرمز» مستقل از تضمین نظامی واشینگتن را پایدارترین راه برای ایجاد نظم جدید در منطقه دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77850" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDs7cwz3ixLFo7y407jRGEkcrzUxw9xTLppD9RPr9AvkmSYHiPqlL1QH0l0M6yhhdVdC4BwjsL2auj-JBRx0WKQwy8EOhPSsU0FDi0FAt3CM-3UEF9tnxlUKgdyyQ2pbGkPu_pMnBSbnaV6fSSTg_S2cKKeBeqW90h0n_i6CVfRBHzjQ-O_uVo5NCpAIK7giG6aH8FCBok67btAlicZMNPEfbWqlAOeGpmhaAgc2sHZ1JPsDyaRQXkneV2B31k6VbawPRn-rwjsHrHai7ZYgCUUWxznydb3t7QRp2MacfAIJ0t2kZ4ZLhqJSBxfMoqi2CWb0gmkVDo6NmJ2S0Lrdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrnCHChXXCgSJ394oRYzuEalXHwdvbsoU-fH0s54ByGN_jbVhFWz5MT2WVGySOqIqFlnbhy4AhDcbcfihv7G3h6Nb2at2Aqzu7GYuL1JrTqzJMK3mYk_gzZd-PYKB3jL8xAUKbfzBsI988KJH1FPY2oFPchrVCetwktn6Is2qb-fzz2IuWzUNormh50u7HLr8A42Enqm24U_frLNEmthpRAuPov_skWi1Ev2lcOwZToMBwXJzblTA3jRy3rkyO-yyvfthaeDorG4D8SEPnj5KZiUSeQPHoxG7SIqkEATCnOyjXiAASwl2mDykhPm4WwlZK1OrzZc7RgDY3OriTsg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PnTGYsZd14iIJSpnLNcHjCToe-JNtGnpEAembOeueFizb65gDGZI8qohudCvxLjJoseuai637tVADuyGL_24Ebn7Fk5B15Od0SaOOsR0c8cq5ZDhXg85uOiBT7K0mJYNlu4H-a3gxvDnCFYlGYBWXrYWXmG--jKl0LFbKxbDEAfsacAdvwnL8vOdm9VrAAMArfgYCuTD3uYK4XRsu1kZ6rhW98J5lNIceMdC_bslFk7WHJNyUUYlJdoNV7jh9omj9ATu_qGvCOjJL5UUlb566EIgIQg03O7JJyhJ5xYZfBNXTCQlE3gH8gCIzSN8j-GCwNQrFbTjFmDRLcP5NaMblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcwbVE7sGHbYzyMS1IIHmUVtj79ZvM_sMrYl-6u98lBc17nBTZmMAwuZriAJ7oPRevw7ITXTwyq9cQLi4mhYiaJOALLFYhjYifFtJs3Mtlb702d49cMroITeYNtwIEL6xfguUTmOi4uOrZ9tQFRL_Xa5pm7HkRXSeiv-_t8IGjBHJkns5MmKuX4Ny0KPMzmFc8he3cSygEgAyd8IPEo4924ClD0LFofr2JYHCc6t9nidyChsD4JdlTKKblrzQnRuoWWZNURAyfJkWBCN0d7v3edYAgZrjxlLvWHYYKipzHiwvrmvbQRBkeQzciGqQmxjW9cjvInoLQ8T4HB2yx8F0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jv4OrHHqzbrve5u2XYbWWZjvHXcdHgDpCJPf5ib-GPZ4y7PRmTIu9GqDx66eXEBOX8AZRvhPB8VoaTtJ2Oh_OWj2HAOaxvgogBJ7mNkm70kOJIC9CzJ-xnjieCMzctDLC3jRhGIU-Cm6gv-N-W-FjkMiEHqDu0RCIxr6LNYrctaoFDPTQWVK4odmaAvshwf6lTj-cWhIY3k7K9p_lAQEU0JeuKAMhShDhpp0f7HyDK-Tw1UyBi6L2ZMtiaAz0-6AdUM2F1-Euw19Z4nfBGlZ8tA_RkpTDxi4kTGHNWxIAZ86NBh6LdpFSPjD-njOh_4tdMFemUm0XkV00gBSPt5ALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTGD309nF-YchJkdaWzKsGvgPL5zv_9YHItE5UxeO2racm2HqmxhUVF4bHibMy6QWz8_XJrJgiGdW6xtig_gCkDaSGEl5xxGX_I-8OSnKw5x1EGdoYp4sbOr6rSvMqyzLyuRH5c0J10J728mHtyaSo3LUId-qjJZO5_JcK6KaoobGYdFlDbLzbukuIsGKHCUBNWZRuIL1foMfg2pBJM3fa9yLBGgsq6xgKdEPjWwui9I-VwXcqbhv-TUxqISSrj_mH7VveSfp1rVkP5y22-yKytlna4sbi9wKGu4bIm01VfHBi3tRppsdMC5ngOVWF8zS085eWutW4BpKhtQRZYkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPjoqu9c0r67d8vEsFtPm7dFi4ZRvQ6OYNnnrOAKFc_M32gv381xuT5ML-bD9QQ8wQ-2A2k6WQVHtz7vD2Yby-1ww0tuIR0RRMybNNLafMT-3qu6K94TKyS-ei7uysguoZhD6c8ttT9gw2BCIVPdpTs9s2G5pLlyMgkb4SxJuD5ex-TqHVwpoEbTkGFBlF8UVSHGubeFlRuIYgiwKPwt2QSrc48iL6tZfLDtxfEKd9wuGw3HwiCc1FaH9gxuINrd4j8YsGGxUc2f_h8QKipUAVLMnwV-xfm5CYQRqiXiqdjwhozrdF1w9gcpM4GRIButJ4ZJJAU5HEcLTpCF6ZA7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2L5rdxknoWx9FNgojaCrNitGUJDlGNg-QCOuY6HrXBBhbIh_qmn444snAOXaXOJhvqzE6NbjVHUROaaupg9hK1-Y85Xbmh4J3Nv6_y65sNmktDpu2cRUM7YT7A8tKAn3nqMrBad-rO5-6b8wheyG84aaGP_YBetNlXBRqJyGwI5EZZ_zfdWV3-zCZ9huftw09U-sEBN82Qkm11AcCtfZWThJ4ttzU-H9FgRCXrRpM4XkT_PHhOFttUcRXk2cHX4ml82DZLCuiEC7i5sN9nN4kBzHtv61z-ruBoZMvlekSTtkB4L91gh11sWii4rYANKUdEwYRgt9qxZwOETSMQ0zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
شلاق مجازاتی بی‌رحمانه، غیرانسانی و تحقیرآمیز است که طبق قوانین بین‌المللی به‌طور قاطع ممنوع شده است. با این حال، جمهوری اسلامی سال‌هاست از شلاق استفاده می‌کند؛ نه‌تنها برای جرایم عادی، بلکه به‌عنوان ابزاری قضایی برای سرکوب معترضان، زندانیان سیاسی، زنان، هنرمندان و مدافعان حقوق بشر؛ ابزاری که هدف آن نه‌فقط وارد کردن درد جسمانی، بلکه تحقیر، ساکت کردن و بازداشتن افراد از مخالفت و اعتراض در آینده است.
🔸
بنیاد برومند پس از اعتراضات «زن، زندگی، آزادی» دست‌کم ۱۷۳ مورد مجازات شلاق مرتبط با اعتراضات را ثبت کرده است و در پی اعتراضات دی ماه ۱۴۰۴ نیز در حال مستندسازی همین الگوست.
🔸
از آنجا که روند رسیدگی قضایی شفاف نیست و بسیاری از قربانیان و بازماندگان تمایلی به گزارش چنین مجازات عمیقاً تحقیرآمیزی ندارند، مستندسازی ابعاد واقعی استفاده دستگاه قضایی از شلاق همچنان دشوار است. با این حال، این کار برای آشکار کردن الگوهای سرکوب حکومت، حفظ شواهد برای پاسخ‌گو کردن عاملان و به چالش کشیدن استفاده جمهوری اسلامی از شکنجه، اهمیت حیاتی دارد.
@IranRights</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77842" target="_blank">📅 18:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfNKde7p4rGp18_fpEHrH6dNN0Nn0NkYFY5KJJ5R1bZVpLwFBHKFCXboRKEnwxP1Bp42EGNfsPvupGnztlKrCv1ZTp-ZcwThCT-K8kqgI4pYb3W14w7Zg9yGQ6I_Zq1qv6dWR5ilGQx0Iu0ZOZ237WkEsHrsM_UJEWuwjj4Miq0jQxIj4XDeZTE2uPQHZ5b1LvVa0RJHGRiTlGoi2tM1NQy2lkLt3tu9FAvwXGJgj7H9U92EC47TjjzaaD4y-AgDM_uhbyRFWkBunuIfGPZEgeGJWIGk-Nj_k8KSAjGUrDlr6db9G4vGro6J78XdPvQo1LEkbZUoJjrUm2FA81iANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیما:
«توقف اجرای طرح عرضه بنزین با نرخ پالایشگاهی در کرمان»
مدیر شرکت پخش فراورده های نفتی کرمان:
🔹
پیرو مذاکرات امشب استاندار کرمان با مقامات کشوری و نیاز به بررسی بیشتر در خصوص طرح مدیریت مصرف سوخت و مقابله با قاچاق، عرضه بنزین با نرخ آزاد پالایشگاهی در استان کرمان متوقف شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77841" target="_blank">📅 00:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lU2Z1AbPB91zDYJJPeMSDIv047nJE68DCxNO-LBhqGHVlM768tk5u_E79Aj1J4AFU77ki_xV2254kSYtM_JQy6OLrxrEviyr5RZgXTsXTbgPzXK9-JQx7YvSXaYAJ3rw6RlNdBWz4gWGx_aG1ZX6InwBTqhvODzA8w7ph2KfZVlRyrbt6OPOiHoxux7ZMu5GB5z0xFu0fLoRKqNIDo2xhXa8Rp9ZhVImG1nvdHb-lK-auvqXbyfeRgVz2y6aay9qi07dtydriHtrVmtJOaQG3oKjrrJC47aKkv27XMZqmgsXDpehdpeHTb4mntkGENw5uz6wfDpUsied6F1EuWLLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون هماهنگی امور عمرانی استاندار کرمان از آغاز عرضه بنزین با نرخ تمام‌شده پالایشگاهی، هر لیتر ۸۷ هزار و ۲۰۰ تومان، در ۲۰۴ جایگاه سوخت این استان خبر داد.
به گزارش ایسنا، علی‌اصغر ذاکری‌هرندی اعلام کرد که عرضه بنزین بدون یارانه از ساعت ۲۴ چهارشنبه ۲۱ مرداد، بامداد پنجشنبه، در جایگاه‌های سوخت استان کرمان آغاز می‌شود.
@
VahidHeadline
🔄
آپدیت:
متوقف شد
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/77840" target="_blank">📅 23:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77838">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lmd8QCzGcoTItY7LXRHFNBvkmBEh95EwtdDzxTC01Lu7KuDgV647ORIRdKriQhNNVNIN3j7kSV08Hezjha7ObYNfAmjTFslYugaE4stpJdIXBMN2Mlu6-yVyJrOpGvPBphs4neVrtQRjwlRv9gtPo1WKEzCn-CN0BTZCyCGBLa-DAiN99LbximDkHvlKPU8tSzRqdIzuRUUCVz64ejM-5IJpdj__njS_TYPjKm1-4Hj7JtDiMy0PJxX_CQfe0ruGtQ_YxYe2x-B_RxsM8IeT91sEw4wfDSoPPkbF-mW8dklIRtNM_8JUZYrnE40RgUNtxvx_9CkLWBnz-u3XrCRXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O_y1QnHtlan-374JHM-xoeEzB2frey3ZFZqkHx92CGmPFJuCTXu5RcV-zHhYAsprZSPuaHD3AwzVFyUPne05lUHnjvtGgjbPeMMOa_F4W947c1q6Ppd5R0Q9eO3rw341Wn6_yRg9f1eabjRM57V0ELKWKwUvGMaroBcB_OVY25kYBYdcf1pzIrO4YVXt__oBjXfSf9WY0ooo6MG3FTz4zAQX4eMPE8kWJKC6TwgIPPH7-DuPZCm58HHphADQvSYCfgBIi2v-H6N7PG83cgq72X4sPyEcIJ96jGM_B-hR0UT_9IRU_XiLMeCA88wQ2dAfbNwiMdK_NKu1_o8jfpMQmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتحادیه اروپا و شماری از کشورها، از جمله کانادا، بریتانیا و استرالیا در بیانیه‌ای مشترک، با شدیدترین لحن ادامه اعدام معترضان در ایران و سرکوب افرادی را که برای عدالت و کرامت انسانی اعتراض کرده‌اند، محکوم کرده و خواستار توقف فوری اعدام‌ها و آزادی تمامی بازداشت‌شدگان اعتراضات شدند.
در این بیانیه که روز چهارشنبه ۲۱ مرداد منتشر شد، آمده است که استفاده از مجازات اعدام برای خاموش کردن مخالفان، ایجاد ترس در جوامع و مجازات افرادی که از حقوق بنیادین خود استفاده می‌کنند، به هیچ‌وجه قابل توجیه نیست.
کشورهای امضا کننده تاکید کردند مردم ایران باید بتوانند بدون ترس از آزادی بیان و آزادی تجمع مسالمت‌آمیز خود استفاده کنند و از جمهوری اسلامی خواستند فورا به استفاده از مجازات اعدام پایان دهد و تمامی افرادی را که به‌صورت خودسرانه بازداشت شده‌اند آزاد کند.
فرانسه، کانادا، آلبانی، آلمان، استرالیا، اتریش، بلژیک، قبرس، دانمارک، اسپانیا، استونی، فنلاند، ایسلند، لتونی، لیتوانی، مقدونیه شمالی، مونته‌نگرو، نیوزیلند، هلند، پرتغال، جمهوری چک، رومانی، اسلواکی، اسلوونی، سوید و بریتانیا از جمله امضاکنندگان این بیانیه هستند. نماینده عالی اتحادیه اروپا نیز به این بیانیه پیوسته است.
در ادامه بیانیه آمده است: «مردم ایران باید آزاد باشند تا حقوق خود برای آزادی بیان و آزادی تجمع مسالمت‌آمیز را بدون ترس اعمال کنند.»
کشورهای امضاکننده همچنین از جمهوری اسلامی خواستند صدای مردم ایران را که خواهان تغییر هستند بشنود و برای تضمین رعایت حقوق بشر، اقدامات عملی انجام دهد.
ژان نوئل بارو، وزیر خارجه فرانسه، نیز با انتشار این بیانیه در شبکه اجتماعی ایکس نوشت که هفت ماه پس از «جنایت‌های گسترده» علیه مردم ایران که برای عدالت و کرامت انسانی به خیابان‌ها آمده بودند، حکومت ایران با افزایش اعدام‌ها به «ریختن خون» مردم ادامه می‌دهد.
بارو این سرکوب را «غیرقابل‌تحمل و غیرانسانی» خواند و خواستار پاسخگو شدن عاملان آن و آزادی زندانیان سیاسی شد. او همچنین تاکید کرد مردم ایران باید بتوانند آزادانه آینده خود را تعیین کنند و حقوق بنیادین آنان محترم شمرده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77838" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77837">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IrXDrpRltlsVRCFnKfkKDhhTO-Ahcrzve6rnTTErWUQpksa51VPHCmKepU2cVT-4r-gjkD1Piu7QTng3y_MarrpOT_qHpzq19bVfj8cUUe2On0irQugI2nU1arX9xUbDz5Nb0-BLlD250Sa8kaPkauyIwI7fT0Nd8QWOEBAES9GDPaqLgGrwxoOLt9ofdXeg034Xjhk_TIAnBN0-WaZPJC8pNfJ-DET84MB1MrQGEzLFfzCsQ38jY8DaV9BpycSoC0ERRzCHXd4cmdMc9NjxkU8kchJmJj3fFfuGd9i7FPIGT7E3JrgHwvXGXg8P0LZLb3Q-yCi-Qg-DGAUuVrLqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایالات متحده آمریکا کنترل کامل تنگه هرمز را در دست دارد. فکر می‌کنم آن را حفظ خواهیم کرد!
محاصره دریایی ما را همه «دیوار فولادین» می‌نامند و ایران هیچ کاری نمی‌تواند در برابر آن انجام دهد. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق نگرفته‌اند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است، و «رهبری» آنها، در بهترین حالت، نامطمئن است!
آنها هیچ پولی ندارند — کشورشان «از پا درآمده» است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است، که دارد بدتر هم می‌شود!
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. الحمدالله!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. has total control over the Strait of Hormuz. I THINK WE WILL KEEP IT! Our Naval Blockade is being called, by everyone, “A WALL OF STEEL,” and there is nothing Iran can do about it. They have no Navy, they have no Air Force, their remaining soldiers are unpaid, the IRGC is decimated and fleeing, and their “Leadership” is uncertain, at best! They have No Money - Their country is “shot.” All they have is FAKE NEWS and 300% INFLATION, and getting worse! Iran is all talk and no action, the Bully of the Middle East No Longer. Praise be to Allah! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77837" target="_blank">📅 18:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77836">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=rIJDVs59YvMVOjzDmKBBSsmPSqoIj5k1At6i00Wt2cpHlJlVzBdRlcDoibTG9vP3uu3iv0SJxnVM3hzKlPaKwd-43ucleH3lO69ZvnaNUSJvqCMbGJoP37w_Ydr3dM0TeiudO8wKY3m3ZyAxKK_2f5PL0mrYRZYMZIKq9nsuC21QHeeWtrbOW2WdqivBsc8mQEEtmYlpkBEyDpXYihggRYjhsmDnOUirqZOCvPDokGn7HVmI27xX3LYkiZR4QGXgHaPgiW-DVnGp8_nxPb50hdi2vIxTVqZihwD6b7xqnC4zyMKYV3RJ46dv9BAzA2YMUuVXTp_x7_JhFwkP3HvJ4RN4eAVDMY6dLxRE8l5BZ-oBlFitr7Q-IhLQUJ7b9jj3yRNooNUmIE4cWliAe8yg66xY7SM40fZIfLcihCNjQGmdrGxbKud_xOWov3i9Vhag9IzwvUvJ_wpPkEf2nGOgzLIZBXU2TFNvdPpb2gvtfZ2ZdVawzd_OZyNq3iTaSinekadnO_5fVLnplnIOTe-Dw7xACbIUwoFJgbtHul6_JK8obQwHQ4r4Ouy_cakavti1JjylpOQPFMksuBkeHvMXYYZMFKbF-cVL8QbT90C3Vw8wLT93Hf2urtTvhPSRQKs-S6EmTYgpEkFvrMFiMtFN4C5VExSYZrMXDPSffGt-Oeo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/56807a2a8f.mp4?token=rIJDVs59YvMVOjzDmKBBSsmPSqoIj5k1At6i00Wt2cpHlJlVzBdRlcDoibTG9vP3uu3iv0SJxnVM3hzKlPaKwd-43ucleH3lO69ZvnaNUSJvqCMbGJoP37w_Ydr3dM0TeiudO8wKY3m3ZyAxKK_2f5PL0mrYRZYMZIKq9nsuC21QHeeWtrbOW2WdqivBsc8mQEEtmYlpkBEyDpXYihggRYjhsmDnOUirqZOCvPDokGn7HVmI27xX3LYkiZR4QGXgHaPgiW-DVnGp8_nxPb50hdi2vIxTVqZihwD6b7xqnC4zyMKYV3RJ46dv9BAzA2YMUuVXTp_x7_JhFwkP3HvJ4RN4eAVDMY6dLxRE8l5BZ-oBlFitr7Q-IhLQUJ7b9jj3yRNooNUmIE4cWliAe8yg66xY7SM40fZIfLcihCNjQGmdrGxbKud_xOWov3i9Vhag9IzwvUvJ_wpPkEf2nGOgzLIZBXU2TFNvdPpb2gvtfZ2ZdVawzd_OZyNq3iTaSinekadnO_5fVLnplnIOTe-Dw7xACbIUwoFJgbtHul6_JK8obQwHQ4r4Ouy_cakavti1JjylpOQPFMksuBkeHvMXYYZMFKbF-cVL8QbT90C3Vw8wLT93Hf2urtTvhPSRQKs-S6EmTYgpEkFvrMFiMtFN4C5VExSYZrMXDPSffGt-Oeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرج درگذشت؛‌ جناب سرهنگی که «پهلوان آواز» ایران بود
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، امروز چهارشنبه ۲۱ مرداد ماه در ۹۴ سالگی درگذشت.
درگذشت او موجی از خاطرات دوران طلایی موسیقی و سینمای قبل از انقلاب اسلامی ۱۳۵۷ را زنده کرده است، به ویژه در نزد شنوندگان برنامه‌های رادیویی و یا انبوه تماشاگرانی که آواز برخاسته از سینه ایرج را از لبان ستارگان فیلم‌های آن موقع می‌دیدند و می‌شنیدند.
افسرآوازخوانی که حسن کسایی، اسطوره نی را واداشت «پهلوان آواز» خطابش کند و صدایش برای محمدرضا شجریان، خسرو آواز ایران، «متر و معیار سنجش کیفیت صدا در تاریخ آوازخوانی ما» باشد.
ادامه مطلب
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77836" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77835">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrTIQ1NvbHGyMy0mkcAX7R-nsuk7orJTm-oKIk1DP_DYMaCHHrKd9Xn8aCW5hWQmh2cHAEqwDwZdmvQpVfJ9f3i4AXIQ6Z-Uc-jf694mAX3aJ9btfypmGwOUa3zq_IErRoxcyXor4aQYVjOPlVD_hBKciicITJ2O8nMCR2WtGfREiWY2OBqH2vidS6Oj38RamMfgHSx-bHzAUR6zzJsNFQ42D3ROXBMEV4_cgwXOffN5MA3Wzd41-55BN3Gn9MmBa7wdTVyG0YFjoR_odaGPJFVlQEyrDAdnQ1DD6v865iZm2ACj8ISx7pTduli5d39gq8mBzlp4v2QokX45z63TIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت جمهوری اسلامی می‌گوید هند در واکنش به انسداد تنگه هرمز توسط جمهوری اسلامی، حتی در طول جنگ یک کشتی مواد اولیه تولید دارو نیز به ایران ارسال نکرد.
محمدرضا ظفرقندی در ادامه تصریح کرد هند ارسال مواد دارویی به ایران را مشروط به عبور کشتی‌های مرتبط با هند از تنگه هرمز کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77835" target="_blank">📅 16:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVPrhJbv2zMTLRoorK2Yu14TH2FhGinz1FUt-NP8T4KLW_SZf7gk1y7r2HSuIE85ElNls7Qgg2BxQsvLZgAZuPDqQ5uTwFu0CO1KKmiD0dan_IxcSDMcsgHxC6fJcY10zTGd8LJ3iQjsgjMCwZ3Y4SxoXTWqKzB6vh_PxMEaExn8_c3iUjJT65ucKBz5fl9Y9Pl-d-GvP3wdLqPSKK6s0IygUGMNissfNB13KlSKdPKQRJ_iiFnom4XSePmlrAc2RJHFM7CqrMRnMMup0Z_BII53RrWwgpnuSHXOvAof-SVnQJxfrn-ChyGQBPy2oPTOA2aUI8rqHKcrYDBFyAyySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای مسافربری پهن‌پیکر چینی، قرار است روز چهارشنبه ۲۱ مرداد اولین پرواز تجاری بین‌المللی خود را انجام دهد.
این جت جدید که به عنوان پاسخ چین به هواپیماهای مسافربری بزرگ بوئینگ یا ایرباس معرفی شده است، کوماک سی‌ - ۹۱۹ نام دارد.
این هواپیما اولین تلاش چین برای ورود به این صنعت پرسود است که تاکنون تحت سلطه غول‌های هوانوردی غرب بوده است.
پرواز هواپیمایی چین، ایر چاینا، صبح چهارشنبه پکن را به مقصد اولان‌باتور، پایتخت مغولستان، ترک خواهد کرد.
این پرواز رفت و برگشت به صورت روزانه انجام خواهد شد.
برخی تحلیلگران معتقدند که ممکن است سال‌ها طول بکشد تا جت‌های چینی به رقیب جدی شرکت‌های شناخته‌شده‌ای نظیر ایرباس و بوئینگ تبدیل شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77834" target="_blank">📅 16:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77828">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IbjK6b3fhO6oSah1wO7P0PqudbkojUtRh9sLxMaHyIFmG8VnZj-gtN9W1gB7WXZXi_CnLAX99zPMQAAlTNuHmLnopqDQSU_HT-BDFs1n8OeTg1Met-0_ziBTfatI5hVpnAHL6vM9uT48-ojy4j1uA3i3YqJG_Q-_ZRWL3g9DNGvXu66hO3FC8DjLtUq0vcFpR5hX2PE0Bt-QeN03Bx_szyxsoMd58F7ilhPwrZCUqM3gKFyAyynXvhCTEJjZrvVi7fcBlx-LC8X670tAKLc5Lx6CAwoBEcTblQMlRYokLVyz0W98vc5nOP5Y11y-tkCRQb-tLY0LVEeFgr-qxTZJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BnOyB8faQ2KNHCBZMWn2PwR_eZ8TSs1lblb0u1uk-ys84S55SrGbd2PZuCa2BM58CHSwftXON9eEa-wjPDGtkni8RnlisGQT_yTGTikmqmX2hGYvJp2Z83tQ3272uA2LNLLc-iOZenxlNBlQGwgHJ7F5NF_qJXpNcrHGnLsQ2f568x33jdgWWaAfIdwC1qoMzhMm_n0XN_NWrhOo8EgD7yXpF0BRMNCj21yZao14TDRVJqtLxTLu4PnivDLICUAUXcjtMPswpII_ESsJiKCRIWQWFRiHchkPK5AUBm1q4X2mogicS7MNrO4pYESjkWKsVhl-hOjsScUPUD7gIGzhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ErbVq0-lvPU5ABo8CUsm5zeGLDSZLj7Xu5rcupKL-BiT_VPe3Tk21r8VJVlvQ6gHBl6NSpD5IFQyV8omXnEshVG2eez1hCozjXuAxo1rXhNhnjgLfVrXoav1LDnAjkIX21MQGKvgy2MHrTHbL_0fmb5jqqX1FiQRnbE3PYjCZMa2-xV5FOsGn9uGfCB3JPu1HBGsM_zaFCH6JgNdeCF5hbGoAilQr1n4_Ev8JdycHj2otOWEyws4YsZ8NOlfrnIbnB0GUjVE56tT_bGDcxWbJupf1vCbOHwcZV3sP36Ldm-q9CgbLSb3CByK0rOkMHE2zoRRE7yd75NX-nq9Ghed4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OJVwk2EjnWy3atQxvw-vTE_RDd7Wvzm90fvIRpkj9i_2b2Ob66bjejpUFO6rBEga4x2LR8rPJIOGuV_O6N6wkHJAakX2C5dVDgIHu4KgVlH2s3AXSO2Y0UhLnP1oLR_13iMM4IkNKQZTH7G2PcSc2c6Cig9GXazLxdMLyVzID-sCtURbMCImqREM9M6xED6KEKoJlRvBecc6xvcsdzTaaTu1eyE_19UsCO22QPbm6p4UsHm93f2TAaCRmVlgH-QDFALgxLzY1TQRMsj_pis-fqCvftUh01YUsBNuiygoDjoPks-suOLNv35TsktUD3B_yJHBaZF07kYUE9T5aXtj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KhknjHU5I-OMQvVQGgvyRS_bL68pVM6q_HOwCHjMvyF34CQl5kIutJPZ22uYgMxEPlZDbg9tkGBA98uZ1Zz9mXKjiqibrgKNvlZ70wKkabr3z97F9Cjh-_7YnhPS36StcL0rZG4scmEfFrprcizxK_tW4kW_3QDQSAQl719BdXWRxxomVlWqeTdsIP6EtUMfU72XBTMPYg0qpTUMcqI_ANsEP4rdJnAUi__cEIEzwy7weXdwcgH8CvCY7wonbA9qvjDirSSMq3MTOC-gT2QHYtoyIjimYXP_kVs67KbyKKoPrQrO8Gp7fPqaOTUvQuhVs4T8CLE0f0psCu1Tn0kEcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=RCo3ic4Wd31ko0M9lAYICf2y6ZnpWUgwwHXI8OIEHntdb_BiGC6nBrDtH_5BaMNhgN69GvOSuMhpxFfaVuufagFwihLq_azt7QfFMuzzgyI-OdS7V2IJh-hWKh7R1EKAFJzhNRNLqSM7mdVZwtfZt-iC1AK-6osLZLxbN2M3aQh0ohMSHbAEKGsN3yLX4HC_K4Lj7A9ICl_6NixFY4TDhhxHYCwEjEHkXh9ZA2n3xyrf7uedLsB7ZSRbRdDnTdRJp7jTEf-xHdchIbBaXOvfUdjyRGA9P_FUavS_7-LZ_qEYUCwEBpdTeuQeYuoX4VoRX13MZCwRlKx6hPoFnl7cQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a19a9b2a0.mp4?token=RCo3ic4Wd31ko0M9lAYICf2y6ZnpWUgwwHXI8OIEHntdb_BiGC6nBrDtH_5BaMNhgN69GvOSuMhpxFfaVuufagFwihLq_azt7QfFMuzzgyI-OdS7V2IJh-hWKh7R1EKAFJzhNRNLqSM7mdVZwtfZt-iC1AK-6osLZLxbN2M3aQh0ohMSHbAEKGsN3yLX4HC_K4Lj7A9ICl_6NixFY4TDhhxHYCwEjEHkXh9ZA2n3xyrf7uedLsB7ZSRbRdDnTdRJp7jTEf-xHdchIbBaXOvfUdjyRGA9P_FUavS_7-LZ_qEYUCwEBpdTeuQeYuoX4VoRX13MZCwRlKx6hPoFnl7cQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آلودگی نفتی مشاهده‌شده در سواحل جنوبی جزیره قشم به محدوده جنگل‌های حرای روستای «نقاشه» گسترش یافته است.
خبرگزاری ایرنا روز چهارشنبه ۲۱ مرداد گزارش داد بخشی از لکه‌های نفتی وارد محدوده این جنگل‌ها شده و عملیات پایش و پاک‌سازی با هدف جلوگیری از گسترش بیشتر آلودگی آغاز شده است.
به‌رغم گذشت دو روز از گزارش شدن این آلودگی، رئیس اداره منابع طبیعی و آبخیزداری جزیره قشم اعلام منشأ دقیق ورود لکه‌های نفتی را به «بررسی‌های کارشناسی و جمع‌بندی گزارش دستگاه‌های مسئول» موکول کرد.
جنگل‌های حرا از زیست‌بوم‌های حساس ساحلی قشم به شمار می‌روند و نقش مهمی در حفظ تنوع زیستی، پایداری سواحل و زیست و تکثیر گونه‌های مختلف آبزی و پرندگان دارند.
سواحل هرمزگان در بهار امسال نیز با آلودگی گستردهٔ نفتی روبه‌رو شده بود. مدیرکل حفاظت محیط زیست هرمزگان در ۱۲ اردیبهشت اعلام کرده بود آلودگی آن زمان در پی حمله به پالایشگاه نفت لاوان ایجاد شده و مواد نفتی به نقاط مختلف سواحل استان، از جمله قشم، لارک، هنگام و هرمز رسیده بود.
@
VahidHeadline
در عملیات پاکسازی نفت از سواحل قشم، از پدهای جاذب برای جمع‌آوری لکه‌های نفتی استفاده می‌شود.
این پدها معمولاً از الیاف مصنوعی مانند پلی‌پروپیلن ساخته می‌شوند و نفت و روغن را جذب می‌کنند، در حالی که آب کمتری به خود می‌گیرند.
پدهای جاذب می‌توانند با جمع‌آوری سریع نفت، از گسترش لکه روی آب و رسیدن آلودگی به ماهی‌ها، لاک‌پشت‌ها، پرندگان دریایی و مرجان‌ها جلوگیری کنند و آسیب به سواحل و اسکله‌ها را کاهش دهند.
با این حال، پدهای جاذب به‌تنهایی برای مقابله با نشت‌های گسترده نفت کافی نیستند و معمولاً در کنار بوم‌های مهار نفت، اسکیمرها، تجهیزات مکش و دیگر روش‌های تخصصی پاکسازی به کار می‌روند.
پدهای اشباع‌شده نیز باید به شکل مناسب جمع‌آوری و دفع شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/77828" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77827">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gguph4ldirzYdNCy9W7DjjF9ikGtZK3V1rJ7KZR9xE1H9LKOur3vQfZ0gLXgm8Umo-Br9u1Wq0w91NNKlWYiW9z69hdZNmIpsHbzLJ5NAug-jIYNBe2Rx225Op3uIREo00dEaklxFXjZOGfBnsodWCUEyiO8aWzEWYXLAMYbc5sdwhXeuNgZWi6AmpGI9maB1YLNP_e2STIOEKEEhj9EX_f3LceQLXxPbXA7nuy1qv50h1PhDuaZi6Ux9fGEoTEs1-SCKmjHeKrN2rc7Sfpz4o95xxwUYnV-NKY67FZbBad_VsGJpbGmB8JFKXv_fqnOkwhrqL7sk12ehZdD-5V6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جمهوری اسلامی ایران از ابتدای سال ۲۰۲۶ تاکنون دست‌کم ۹۱۶ حکم اعدام را به اجرا درآورده که از این تعداد، ۱۵ مورد در ماه اوت رخ داده است. شمار واقعی اعدام‌ها احتمالاً به‌مراتب بیشتر است؛ چرا که حکومت ایران برای جلوگیری از افشاگری، نظارت بین‌المللی و واکنش افکار عمومی، آمار واقعی اجرای اعدام‌ها را پنهان می‌کند.
🔸
هم‌اکنون شمار زیادی از معترضان با اتهامات سنگین و خطر جدی اجرای حکم اعدام مواجه هستند. روند صدور این احکام بسیار شتاب‌زده، ناعادلانه و بدون رعایت آیین دادرسی منصفانه بوده است.
🔸
جمهوری اسلامی از صدور و اجرای احکام اعدام به‌عنوان ابزاری برای ارعاب جامعه و پیشگیری از شکل‌گیری اعتراضات جدید استفاده می‌کند.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77827" target="_blank">📅 16:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nHZbIfVNHrA_p96HIiAcEQZ-q7iN_o1tAjPi_tMUT3w9Xh3KpLu_FdcxOY72pyhytwwhjHs8sdkQ6ViPWUapNXF7XXbNCN6Hd5X2EbFt4KuW7y59WEMMhlu_hIozHUihDwmcwTMU099HEr1R_HvJew3MiL6ovnL8eBWlvfdQetwmhhbUmK1Vjc4j_01ZPcRXRq5a1jBWXgTpYpHCvsJXfSb-MZAijDUvy1z0ar6Gd8tJFyfBY9H0UkcwVQYkah_IW0wbuA8aSYXcUqiAm2XphabWR2omkH--87NiICPyk9xJjduJaVORX2sDWzIPbJhahvKaa2NVEyR0su8Nj6vMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a-8c7SJG1fZabfKjkxyw-RWzoapujpbenBlBjENRtI9W56hmspzu5W33IrTXMElDl8Jht10CN_p0HXW6mDMqVXyfD0cWv0BGOD6ObeQGO0IJgybcEsparCSFIBQybscPH86gcDaLiVX5hFa8n9Jdm8Y8NmmPn5eNvmkuUR6aYEs5hByNrImOmI4juMJkmBulMBzbkqRaEZxNtTFCDj7eYT2h-ChEZ_K8qeoIl8yIJdPI3MAsNIcDvTIlR6K-duRoIjybjYZwpNbVBV1vUOEaddfBE873ml-KcVBBTQxVI3uIFtm_IbzQvkdSFKoCkZaEHDoHsrVJQN_HMw3ZGU6bkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد  ترجمه ماشین: واشنگتن‌پست دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با…</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77825" target="_blank">📅 08:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/49def3f074.mp4?token=XsyuJrGlAdx9b0x-Jx4_8f4mTMy3OBd95EIWvxLtI3o6yF__DG-ROftjG2-BbNAxSuD4648z3nnLyiUE_uSupsf1m9hQ4dComp1FjqjRanxU0ps7i29W3CtpR-JOzHLd8yYqYGwxV8rIA6xXcCFIKlPDyuidMAisQ5Vt3_KbkvpHAQEUPZJVpojMxT2bDARRAficaer-t0PrpOstAemplGvPhytty2hSyoKkgVwc6XlNIPkn39ivnlXjnLl9Jmqf5RpU_8VKm0R1hc9vmuENX-xnb7TfoDhCzaJdVq7fknZrOD_IMpFMpx4nR_IFmlV58Dc8A9ogmXSmWFE1pj1FkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/49def3f074.mp4?token=XsyuJrGlAdx9b0x-Jx4_8f4mTMy3OBd95EIWvxLtI3o6yF__DG-ROftjG2-BbNAxSuD4648z3nnLyiUE_uSupsf1m9hQ4dComp1FjqjRanxU0ps7i29W3CtpR-JOzHLd8yYqYGwxV8rIA6xXcCFIKlPDyuidMAisQ5Vt3_KbkvpHAQEUPZJVpojMxT2bDARRAficaer-t0PrpOstAemplGvPhytty2hSyoKkgVwc6XlNIPkn39ivnlXjnLl9Jmqf5RpU_8VKm0R1hc9vmuENX-xnb7TfoDhCzaJdVq7fknZrOD_IMpFMpx4nR_IFmlV58Dc8A9ogmXSmWFE1pj1FkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با خبرنگاران گفت به ایران اعتماد ندارد و افزود: «من آخرین کسی هستم که به ایران اعتماد می‌کند. آنها پیوسته به من دروغ گفته‌اند.»
ترامپ همچنین گفت ایالات متحده در حال حاضر «کنترل کامل» تنگه هرمز را در اختیار دارد و افزود: «آنها کنترلی ندارند. ما کنترل کامل داریم. اختیار آن دست ماست.» رئیس‌جمهوری آمریکا در ادامه گفت ایران دیگر «قلدر خاورمیانه» نیست
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77824" target="_blank">📅 07:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=ukxZxBjuzmxEnuu1e9z2PelZEik979eGonTGSZz-gWPKtPbN5caMwotntn9CdpA0CFnnNX6aGn65iRipYAxuLGl08v_OVXP1dRXtNfZEA0MktAFWs9pkGAH9dWvaWTxTBvRUbpvFtDbDqlXpcbjWgg71djRe5jm9BbFf1SfLRD-iz4cBzY53u3os8TUhzb_2UVarn38GqehE_M14lb6gSIGzcaG3gFGcqARm6kqhxszRCvUkYtmoaNNfpocX_r1EQalV2GDkPTslctJ_A8RbAH8pvy4sb12G3gm5QeVoMW31s6CDhzCvYyaputUPNOR-6QNIWKqjj1SkGqQHzu_gGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9b0ac932.mp4?token=ukxZxBjuzmxEnuu1e9z2PelZEik979eGonTGSZz-gWPKtPbN5caMwotntn9CdpA0CFnnNX6aGn65iRipYAxuLGl08v_OVXP1dRXtNfZEA0MktAFWs9pkGAH9dWvaWTxTBvRUbpvFtDbDqlXpcbjWgg71djRe5jm9BbFf1SfLRD-iz4cBzY53u3os8TUhzb_2UVarn38GqehE_M14lb6gSIGzcaG3gFGcqARm6kqhxszRCvUkYtmoaNNfpocX_r1EQalV2GDkPTslctJ_A8RbAH8pvy4sb12G3gm5QeVoMW31s6CDhzCvYyaputUPNOR-6QNIWKqjj1SkGqQHzu_gGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری‌های ایران تصاویری از «آلودگی نفتی» در بخش‌هایی از سواحل قشم منتشر کرده‌اند.
به گزارش این منابع دادستان قشم دستور شناسایی منشا آلودگی، مهار، جمع‌آوری و پاکسازی نوار ساحلی را صادر کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77823" target="_blank">📅 21:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDS_0CUeRGuaDwfRNA824Hqq3RXO8zGbcJkWNaLJ8mrCmwknrSVQ5Px0RoEKWXoG-IHWRPbU1aXSpLM6EW6sldoaD-mIXhMucHUTnfachFCho9p_BBGz9aCJXjXSw1fUCOeXZoFDKhN_K2sCYnlfrUMY-wGLtTPo_CV9CsPkPX2_Z7M_UmKe37jI_K_zMpxyaoiojGjYAu3_zwHH0fLIorSXd7g2VLsTS5CCF6HHJNDALNqgH3plaM1j-ZYXtlhUZxgac3rP4rYCjsHFpvtIqdp0sJleu0AIOtFKT96lQShRj_qoycNKe8-vNG3iXRiKLsz6HXCul6d920AvzZgoIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر جدید شورای عالی امنیت ملی جمهوری اسلامی، در نخستین موضع‌گیری پس از انتصاب به این سمت اعلام کرد برای باز شدن تنگه هرمز، آمریکا باید جنگ را پایان دهد و پول‌های مسدود شده ایران را بپردازد.
به گزارش رسانه‌های ایران، او در دیدار با سفیر چین در تهران گفت تا زمانی که آمریکا «رفتار خود را تغییر ندهد و شروط ایران را نپذیرد» ایران اقدام به باز کردن تنگه هرمز نخواهد کرد. او پایان جنگ و آزاد کردن پول‌های مسدود شده ایران را دو عنوان از شرط‌های ایران برشمرد.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در کاخ سفید به خبرنگاران گفت ایالات متحده کل تنگه هرمز را «مین‌روبی» کرده و کنترل کامل آن را در دست دارد.
محمدباقر ذوالقدر، دبیر سابق شورای عالی امنیت ملی، که رضایی جایگزین او شده است، هفته گذشته شروط مشابهی مطرح کرده بود.
محسن رضایی درباره مذاکرات جمهوری اسلامی با سلطنت عمان درباره عبور و مرور در تنگه هرمز که طی هفته‌های اخیر در جریان است، نیز گفت اگر بین دو کشور توافقی در این زمینه حاصل شود، «این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77822" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r2LuBMtDhqNqKuVVCtViEYXrQYz37LOQK4cBowo9ogmfQ9ipEY_SpMtAgOKNgh60EK0YocZ2RWZOmlaR3UL4teLx2EG-mcWZnmb-WX3b-R9KM1vMog2Z_seaqLzwfVxHtpoZ5srSyxhSqB94p9GWvTFiFzKmm5doHEX6CKhjglgE2UeFc1qKBMyUqkuy3ggFr5mlrBlMy4NAKqi9Vn9-lFCSWb4vOxCKHPsrma-rKdclQqmhlSafhn_1aUmcR-2immDavF_8lUg9MOIjicFWm4n06ug7_ViJ3pn_ufNjPeqqUEfdtV8UCPD82PeBxQX8mJ0C9FVyiE3uEMIlXO91tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر مانع دستیابی آن‌ها به سلاح هسته‌ای نشده بودم دیگران ناچار بودند رهبران جمهوری اسلامی را «آقا» خطاب کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77821" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iM2c7I_OcQbsavOZCueS5uWYfh-RnyGqI_UPR01ls7w0WI4CVc1iYGz8EcMC0cbCNwQvs3C9byE6aJsQoJy0CaW7FYhbJGmsiKAWQzbYYu8e1bvOsnLYKbuS7miT_fEFXkBttytboX3PqDCt5-Noj37iOo_tKiQb7doCHfGrGRUJpR3D_-aCxHhGEkqT-7gP9npmVh-NDgSjcXOKFNcgQpzI4Y17Kx_tJyewWXm-qwvZzOdXMVLEyNwtivl7aswjOb09VC2pn_OIyj2h0lH-CAXlXKEg-kxZ3STggLMlnpdK1lMYuCASbCd0nmjfv-zVivfmf-5jFC616hVDTIqogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسی کوهن، مدیر پیشین موساد، گفت ماموران این سازمان در گذشته چندین بار از تاسیسات غنی‌سازی اورانیوم فردو بازدید کرده بودند تا اطلاعات بیشتری درباره این مرکز هسته‌ای به‌دست آورند.
به گزارش تایمز اسراییل، کوهن، روز سه‌شنبه ۲۰مرداد ۱۴۰۵، در نشست «مجمع جلیل» در شهر صفد، گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک کنیم.» او درباره زمان این بازدیدها و این‌که چه افرادی از سوی موساد در این بازدیدها حضور داشتند، توضیح بیشتری نداد.
او همچنین درباره حمله آمریکا به فردو گفت: «بمباران آن توسط آمریکایی‌ها تحقق همه رویاهای من بود.»
تاسیسات فردو، همراه با مراکز هسته‌ای اصفهان و نطنز، در جریان جنگ ۱۲روزه اسراییل و ایران در ژوئن ۲۰۲۵ به‌شدت آسیب دید.
گزارش‌های پیشین حاکی از آن بود که حدود ۴۴۰ کیلوگرم اورانیوم با غنای بالا که در این تاسیسات نگهداری می‌شد، زیر آوار مدفون شده است. با این حال، اسراییل بر این باور است که ایران پس از جنگ بخشی از این ذخیره اورانیوم را به سایت «کوه پیک‌اکس» منتقل کرده است.
کوهن همچنین گفت اورانیوم غنی‌شده تا سطح ۶۰ درصد همچنان فاصله زیادی با ساخت بمب دارد. این سخنان با ارزیابی برخی کارشناسان هسته‌ای تفاوت دارد. دیوید آلبرایت، کارشناس حوزه هسته‌ای، پیش‌تر گفته است اورانیوم ۶۰درصدی ایران می‌تواند در صورت تصمیم تهران برای ساخت سلاح، ظرف چند هفته یا حتی چند روز تا سطح مورد نیاز برای تولید جنگ‌افزار هسته‌ای غنی شود.
کوهن پیش از این نیز به‌طور علنی درباره فعالیت‌های موساد علیه برنامه هسته‌ای ایران صحبت کرده بود. او چند روز پس از پایان دوره ریاستش بر موساد در سال ۲۰۲۱، در مصاحبه‌ای کم‌سابقه با تلویزیون اسراییل، جزئیاتی از عملیات این سازمان علیه ایران را بیان کرد.
او در آن مصاحبه از انفجار در تاسیسات زیرزمینی سانتریفیوژهای نطنز سخن گفت و توضیحاتی درباره عملیات سال ۲۰۱۸ موساد برای سرقت آرشیو هسته‌ای ایران از یک انبار در تهران ارایه کرد. کوهن همچنین گفت محسن فخری‌زاده، دانشمند ارشد هسته‌ای ایران که بعدتر ترور شد، سال‌ها در فهرست اهداف موساد قرار داشته است.
کوهن در برنامه مستند «اوودا» با اجرای ایلانا دایان در شبکه ۱۲ اسراییل نیز گفت که با تاسیسات مختلف هسته‌ای ایران آشنایی نزدیکی دارد. او در این برنامه گفت اگر فرصت پیدا کند، دایان را به بخش زیرزمینی نطنز خواهد برد؛ جایی که به گفته او سانتریفیوژهای ایران در آن فعالیت می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77820" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfFDIzgj1CYJSScpQ296WxaV260DTe1K4SLGimEZLcmQOeGyQDI6jGNA8XrFWfP2PjZIaMHQTle4z8-2LQtu_kxZz-EMlAU61RSbp4GYlHIHqND1UGcew_eg586Jd0o0m_x7OIYwQgLi5-SewX_Cq1gDehhTY_fRgIpPV2eb1yVyPQFx9Rrm0oul1hNqXPn8v4Wbhmz4rg6_IREtyPaQDFPxcf-3yZZ1V0n70x9MQDoOySVAt2127-cJrbA2LfaG8X-eBH4o77TvMh82jGNmx0U9MhvNjZ_l0NjNleYTN9IeTdof82job6DYRCQtqXOHToy6HMrc6ZNkfCfoQTFJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار شبکه‌های تلویزیونی العربیه و الحدث عربستان سعودی روز سه‌شنبه، ۲۰ مردادماه، گزارش داد که در پی اصابت یک موشک بالستیک  حوثی‌ها به یک کشتی تجاری در تنگه باب‌المندب، سه نفر از اعضای خدمه این کشتی کشته شدند.
بر اساس این گزارش، قربانیان دو پاکستانی و یک تبعه اندونزی بودند. الحدث گزارش کرد این موشک از شرق استان تعز شلیک شده و کشتی تجاری را هنگام عبور از باب‌المندب هدف قرار داده است.
این حمله در شرایطی رخ داده که تهدید علیه کشتی‌های تجاری و مسیرهای کشتیرانی در دریای سرخ و تنگه باب‌المندب همچنان ادامه دارد. باب‌المندب یکی از مهم‌ترین گذرگاه‌های دریایی جهان برای تجارت و انتقال انرژی میان دریای سرخ و اقیانوس هند است.
همزمان، درگیری‌ها در چند جبهه یمن نیز ادامه داشته است. بر اساس گزارش «العربیه» و «الحدث»، نیروهای دولتی یمن مواضع و تجهیزات حوثی‌ها را در چندین جبهه هدف قرار داده‌اند.
@
VahidOOnLine
شمار کشته‌شدگان حمله حوثی‌ها به کشتی تجاری در باب‌المندب به ۴ نفر افزایش یافت
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77819" target="_blank">📅 18:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K7d15ju5pqF4NdPTMjgxqiZe_P39nfXGaFn9xjzmpzppVUq1-L91hso6dl_wOgdiFpxZiUfl45AXm3LWrQMSidhO_RBjv3GQfpU8JU-AOMpGqkFHxzE0-y7NxqZXUW_55jzYAA3JwTIfTgzZgqksXT6M5CqFd2KndR_dwuAdCWXPDZuo3PcXTR0tVdX-igfn-dZ9Ujbh8ylp8IZuZTRlScSBU6CYRgE2_2ft5dT0Sc5K25hiZ_gqDOuwWLvA3Rom0vlHTcstFg2fFdT0gMy1Z5XgjXT_64i2YYwnB_kvOmatfbDmfaQgz2rRVN1SXjAiEOYvzh4yaaD0KelVIceIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی و منابع امنیت دریایی از هدف قرار گرفتن یک کشتی کانتینربر با پرچم پاناما در دریای عمان خبر داده‌اند؛ یک مقام آمریکایی می‌گوید این کشتی به هشدارها برای توقف توجه نکرده و در تلاش برای شکستن محاصره دریایی بنادر ایران بوده است.
همزمان، روزنامه وال‌استریت جورنال به نقل از یک مقام آمریکایی گزارش داد که یک بالگرد نظامی ایالات متحده پس از آن‌که خدمه کشتی هشدار نیروهای مأمور اجرای محاصره بنادر ایران را نادیده گرفتند، به سکان این کشتی شلیک کرد.
@
VahidHeadline
آپدیت:
پست سنتکام ترجمه ماشین:
اوایل امروز، نیروهای سنتکام تجهیزات هدایت کشتی
M/V Vela Nova
با پرچم پاناما را از کار انداختند؛ این کشتی باری در حالی که می‌کوشید از خلیج عمان عبور کند و با حرکت به‌سوی یکی از بنادر ایران، محاصره آمریکا علیه ایران را نقض کند.
پس از آنکه خدمه غیرنظامی کشتی هشدارهای مکرر نیروهای آمریکایی را نادیده گرفتند، یک بالگرد
MH-60
نیروی دریایی آمریکا دو موشک هلفایر به موتورخانه
Vela Nova
شلیک کرد. این کشتی دیگر برخلاف محاصره آمریکا در حال حرکت به‌سوی ایران نیست؛ محاصره‌ای که همچنان به‌طور کامل برقرار است.
تا ۱۱ اوت، سنتکام مسیر
۵۵ کشتی تجاری
را که می‌کوشیدند محاصره را بشکنند تغییر داده،
۳ کشتی
را که از دستورات تبعیت نکرده بودند از کار انداخته و وارد
۲ کشتی
شده است.
نیروهای آمریکا که در خاورمیانه فعالیت می‌کنند، به‌شدت هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/77818" target="_blank">📅 18:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77816">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qUZdPRnB5owmdpo4Hdl5AGosIdkzgv69NmIkWK6Mhcn3Gz3uH4J-KQ58lBAtNuZ3kI6PaoLEzlcrYa0iA5NY-cGZsRUo_fnkRuc4EP4dXRgfIs9lrepGbkmVH7eeF3VduJL16nDES-67DUl3-4P4icpD2jNVZY2Xa5sLrWK4AopkAcbaTNFoDmPCTtR2kIDd4GVf-rqd17HN_o3cbzqxwYtGYWbf7tRW7KW9p2XZSG--oBS2GOf0OXYh_xmnEauX1MIcEY8orH2IcszyVaNQHLEODBxs2xKrRTssjgOtJBCUc5gA4zZLC4yS9t8PTPbndGJ3opBOtF6Mtdc-H-4aww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Aj8AGkLPCsbF3WezzBOsKPd1Ptx3Veamo4cl3oCkgJAprK4Y-Kugo5iPy379jmdJHV7jIbIQxn1GxFg2Q_oNyjAfGJC6WvuayPglyQlGp4ZEKDmmWyffq9BeP5cezpNyQDUanmDmPwi-293spDfL-a7yK8gLUdGDdzHprMI-ZSegDdB9jz-0FoYaFnyb1sMsU7mwluO2gJsMZol9Dyvkz8I3P4b44DVgUlWF94FJMX-EL02E1Rngr1LJmAM1krqXWUnnAEZM1qFMH_GCutKJJq12iLLjeKLdl9Ff1AUwPmXzWf_ydHdWa0OFgPHo7904vn05CyV9hYKzKZFCkob0jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی وزیر کشور پاکستان، پس از ورود به تهران در عصر سه‌شنبه ۲۰ مرداد ماه با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران دیدار کرد. محسن نقوی پیش از دیدار با عراقچی، در تهران مورد استقبال اسکندر مومنی، وزیر کشور قرار گرفته بود.
@
VahidOOnLine
وزیر دفاع پاکستان می‌گوید ایران و ایالات متحده به «شکلی از توافق» نزدیک شده‌‌اند.
خواجه محمد آصف این موضوع را در قالب گفت‌وگویی با بلومبرگ، که روز سه‌شنبه ۲۰ مردادماه منتشر شد، عنوان کرد.
این مقام بلندپایۀ پاکستانی گفت: «روند تحولات جاری، بار دیگر به سمت‌وسوی یک توافق یا تفاهم صلح شکل گرفته است».
وزیر دفاع پاکستان تأکید کرد که «نشانه‌های مشاهده‌شده طی دو، سه روز اخیر حاکی از نزدیک‌شدن به نوعی توافق هستند».
هم‌زمان خبرگزاری ایسنا می‌نویسد که محسن نقوی، وزیر کشور پاکستان، «در چارچوب تعاملات دو جانبه و میزبانی اسکندر مومنی وزیر کشور» عصر سه‌شنبه وارد تهران شده است.
@
VahidHeadline
همزمان با ادامه تنش‌ها در تنگه هرمز، سخنگوی وزارت امور خارجه قطر روز سه‌شنبه ۲۰ مردادماه اعلام کرد که مذاکرات میان تهران و مسقط برای آینده کشتیرانی در این آبراه راهبردی بین‌المللی، به مرحله «پیشرفته» رسیده است.
به گزارش العربیه، سخنگوی وزارت خارجه قطر با اعلام این خبر گفت پاسخ‌های مثبتی از تهران دریافت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77816" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qZp80ZSEM9AvasLjNDKeflFBoMeUen43StUtb85lRtCn2_LDfp8BCtdaNqsauqNquTU7KbNoCTiZIdMCxej-7hMdfyJ-BsQOMdbYZBxSAHECiiYPpukpqDdLHBHe5xyRFYxEnTRDCq9zGLeDN500qrNy6N0utUELYpFeLVIunycxcgb24UpN8hhVCAW7JlJSeK6Nr1VHumzHQc8u-5ABazLiu5GvHNtWsOlW2oB4pOKQo_n6A5LUaaRXf5ge9gGJ9Xlgbp2Bl7MUzKPkMjGcWwc5TSkonawK0_u6unXE4qiWCjm0oUZ75DnI4kHJq6co7Sy6w4JKpVtCsURTYZO5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=euqBWQcxobb8GHtDztg3sqnW4Ja4bx4F4GjQaaHJ7prGIfgPIWYqgxzKcyXdgh0VlWQ0eXAjRcSIgW9yoIO7WuYbwSFzehXm-7Gp53FfBjnZc9rqypeFELoJmW2RojW3uCSl7L7m_3WbuqVCeah1sP-9oxfyt7NXIEbHI22mm4bTPh00B7NVqAjMRGHpXeS-5vT4DWLQ_DI9sgR4HXEMYgwOAdLU7hzjXgYbMEXJtdLlCrSshOQI4emFg3M2FEX7-R2R-sOktsYNTp71CjS1jXWlvR4o6k6CpdIOWdUvUIDuT9csqb4AetGZHvQrR0Xu2DEEEN6yrc6RFK2PuBhxOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7660fc2a52.mp4?token=euqBWQcxobb8GHtDztg3sqnW4Ja4bx4F4GjQaaHJ7prGIfgPIWYqgxzKcyXdgh0VlWQ0eXAjRcSIgW9yoIO7WuYbwSFzehXm-7Gp53FfBjnZc9rqypeFELoJmW2RojW3uCSl7L7m_3WbuqVCeah1sP-9oxfyt7NXIEbHI22mm4bTPh00B7NVqAjMRGHpXeS-5vT4DWLQ_DI9sgR4HXEMYgwOAdLU7hzjXgYbMEXJtdLlCrSshOQI4emFg3M2FEX7-R2R-sOktsYNTp71CjS1jXWlvR4o6k6CpdIOWdUvUIDuT9csqb4AetGZHvQrR0Xu2DEEEN6yrc6RFK2PuBhxOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاهی در دمشق، پایتخت سوریه، روز سه‌شنبه ۲۰ مرداد ماه، بشار اسد رئیس‌جمهوری پیشین این کشور را در یک محاکمه غیابی به اعدام محکوم کرد.
فخرالدین العریان، قاضی دادگاه دمشق، روز سه‌شنبه اعلام کرد اسد به اتهام‌هایی از جمله «قتل عمد، کشتار عمدی بیش از یک نفر، قتل عمد کودکان زیر ۱۵ سال، شکنجه، شکنجه منجر به مرگ و سلب آزادی به دفعات» مجرم شناخته شده است؛ اتهام‌هایی که دادگاه آنها را «جنایت علیه بشریت و جنایت جنگی» طبقه‌بندی کرد.
دادگاه همچنین شش مقام نظامی و امنیتی سابق را به صورت غیابی به اعدام محکوم کرد که در میان آنها ماهر اسد، برادر بشار اسد و فرمانده لشکر چهارم ارتش سوریه، نیز قرار دارد. ماهر اسد نیز پس از سقوط حکومت برادرش از سوریه گریخت.
دادگاه کیفری دمشق از فروردین گذشته روند رسیدگی قضایی به پرونده اسد و شماری دیگر از مقام‌های سابق این کشور را که برخی از آنها در دادگاه حاضر بودند و برخی غیابی محاکمه شدند، آغاز کرد. این افراد به ارتکاب جنایت‌های گسترده در جریان جنگ داخلی متهم شده‌اند؛ جنگی که در سال ۲۰۱۱ با سرکوب شدید اعتراض‌های مسالمت‌آمیز علیه حکومت اسد آغاز شد.
در جریان این جنگ بیش از ۵۰۰ هزار نفر کشته و میلیون‌ها نفر آواره شدند و ده‌ها هزار نفر نیز ناپدید شدند؛ بسیاری از آنها به زندان‌های حکومت سابق منتقل شده بودند.
اعتراض‌های سوریه در مارس ۲۰۱۱ از درعا و پس از آنکه ۱۵ دانش‌آموز به اتهام نوشتن شعارهای ضدحکومتی روی دیوارهای شهر بازداشت شدند، آغاز شد. ساکنان درعا اعلام کردند این دانش‌آموزان شکنجه شدند و در پی آن، اعتراض‌هایی برای آزادی آنها شکل گرفت که با خشونت سرکوب شد.
نیروهای امنیتی برای متفرق کردن معترضان از گلوله جنگی استفاده کردند و اعتراض‌ها به دیگر استان‌های سوریه گسترش یافت.
خانواده اسد بیش از پنج دهه بر سوریه حکومت کردند. بشار اسد در سال ۲۰۰۰، پس از مرگ پدرش حافظ اسد، به ریاست‌جمهوری رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77814" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AyQSTVY6roAM1F8imLdTeOrt4QWbUmt5s1BFdBJxa0TPPvpttw98upTV7oaYzGgqG9DaU4--4i5aQgMSdaRhuxkhFRADvBxsWPoY3o7nyN5RI2vKyMMBiFsJl1odk3snxNimKxEYglIokflEKwOWy8OoBvVDOEgsiLJ7xBd8nFYtQ6cpdw6GPWZXmhddWjsFAki7f3UQ3AE5prfm9ComNI4Yu09QqKcbIE3W_pQ4ECTzp8kpvbAufvmM_2OU3XmZc8nqaKNv2PmU6xMDS9kpaI58Ke_a3Sz29Eyy5p-_wfvpH9s1ZZQN5TGpnkqx9MXR6ZOwp8OGO0UhcpBYbwgnPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارلمان لبنان روز سه‌شنبه مجازات اعدام را لغو کرد و این کشور نخستین کشور جهان عرب شد که این مجازات را با حبس ابد همراه با اعمال شاقه جایگزین می‌کند.
اکثریت نمایندگان پارلمان ۱۲۸ نفره لبنان به لغو اعدام رأی دادند.
فراکسیون حزب‌الله تنها گروهی بود که با آن همراهی نکرد.
عادل نصار، وزیر دادگستری لبنان که در جلسه حضور داشت، آن را «گامی تاریخی» برای کشورش خواند.
سازمان‌های حقوق بشری که خواستار رسمی‌کردن توقف اجرا یا لغو کامل اعدام بودند نیز از این رأی استقبال کردند.
@
VahidHeadline
بر اساس این مصوبه، مجازات اعدام با حبس ابد جایگزین می‌شود. با تصویب این قانون، لبنان از کشوری که سال‌ها اجرای اعدام را عملا متوقف کرده بود، به کشوری تبدیل می‌شود که این مجازات را به‌صورت قانونی نیز از نظام کیفری خود حذف کرده است.
عادل نصار، وزیر دادگستری لبنان، تصویب این قانون را گامی تاریخی توصیف از لغو مجازات اعدام حمایت کرد.
لبنان آخرین بار در سال ۲۰۰۴ حکم اعدام را اجرا کرد و از آن زمان، اگرچه مجازات اعدام همچنان در قوانین این کشور وجود داشت، اجرای آن عملا متوقف بود.
حامیان لغو اعدام می‌گویند این تصمیم علاوه بر جنبه حقوق بشری، می‌تواند در روابط قضایی لبنان با کشورهایی که اجرای مجازات اعدام را ممنوع کرده‌اند نیز تاثیرگذار باشد؛ از جمله در روند استرداد متهمان و مجرمان، زیرا برخی کشورها مجرمان را به کشوری که احتمال اجرای حکم اعدام در آن وجود دارد، مسترد نمی‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/77813" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gty-EqD4hw_GeIE3tw1wOLWYe8wxTYuEk_S4BkSOn-C1zeWO9LwSDzTYBIAPiXIUXPpctrV64CiLGqpmyxltbMVLZkykYyuDwAQ5EmYo_PVdd4Y-Zpvv7013DFKtZLrdjzKrQk0M_nKdp0OwEbZ_z3uCJTfXAmPWvmh1LaP0BuCTrk1QkVlfU9j0YokA7JsTXA7gxwCI64JjUCQu1OTQ2ZoMHZdYuapQ_H-h_Eib6NxaXirZQhELliKeP2nLV3YWvcgWIpEhGZgtfGMkQJmd16ZaWz2rF6A7LV3EnsVgs5iFDh8ZmstguSOEIQDh42lL46tjmwAtK4cuvWp-yQQzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا می‌گوید واشنگتن سه راهبرد برای جمهوری اسلامی در اختیار دارد و در این مرحله بر محاصره دریایی و فشار اقتصادی تکیه می‌کند.
دونالد ترامپ در گفت‌وگو با برنامه «آمریکا سخن می‌گوید» در شبکه «صدای واقعی آمریکا» گفت: «می‌توانیم همین‌طور رهایشان کنیم و آنها شکست خواهند خورد. می‌توانیم همین کاری را که الان می‌کنیم ادامه بدهیم؛ به‌نوعی آرام و راحت جلو برویم.» او گزینه دوم را «واقعاً سخت ضربه زدن» و گزینه سوم را «شکست‌دادن آنها از نظر اقتصادی» خواند و افزود گزینه سوم هم‌اکنون در حال اجراست.
ترامپ گفت: «از نظر اقتصادی، آنها به‌هم‌ریخته‌اند. نمی‌توانند پول قرض کنند. ما پولشان را کنترل می‌کنیم؛ پولی که داشتند و مقدارش هم زیاد بود. من بانکدار آنها هستم.»
او افزود: «آنها ۳۰۰ درصد تورم دارند. پولشان هیچ ارزشی ندارد. به سربازانشان حقوق نمی‌دهند. سربازانشان دارند ترکشان می‌کنند. فقط همین وضعیت را ادامه بدهید، چون قابل دوام نیست.»
ترامپ مذاکره‌کنندگان جمهوری اسلامی را «بسیار فریبکار» خواند و گفت: «با چیزی موافقت می‌کنند و بعد می‌روند به رسانه‌ها می‌گویند که چنین کاری نکرده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/77812" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77811">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vx1XEU6-9Vi_kb-2LOWkFKc8VFbkaexNRmaxUD1o4I2WtYS_DEGFlt2tTQq3kG71edkrjyqA3grHyA6pKPhJppiIimgISj2-DZ5pAztA6dhxv-rB01BXVXYUp6vX_O2hS0hz7dQi4EnjnCJ-TeoZaBIiT-GYjf7DFiIGOiC3-BYkABrNL24zz08P0R8RQYFa5L3Ph3Zdvq3k0Ybxatd6coECXqdOKILp9mB6trXKjgz5ZkgxNAcVeTpPc-pbp3Eo_jnXlRBaKgzlkbZS0COvNA8m78ANWabugS7_achaF2pqYS6TyBfpLOp3wAU0HabA92GvSGO_QVdeSSdg0z0IRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی احمدی، معلم بازنشسته ۷۱ ساله، پس از بازداشت در ۱۵ اسفندماه در ممسنی، همچنان در زندان عادل‌آباد شیراز نگهداری می‌شود و نگرانی‌ها درباره سلامت او ادامه دارد.
احمدی هنگام بازداشت در دوره نقاهت پس از دو عمل جراحی چشم و پروستات بود و بنا بر این اطلاعات، اکنون با مشکلات قلبی نیز مواجه است.
او با اتهام‌هایی از جمله «افساد فی‌الارض»، «همکاری با موساد» و «تخریب اموال عمومی» روبه‌رو است.
با وجود داشتن وکیل، پرونده او از زمان بازداشت پیشرفت محسوسی نداشته و دسترسی وکیل به پرونده محدود بوده است. وکیل او نیز پیشتر یک بار بازداشت شده است.
بر اساس این اطلاعات، از زمان بازداشت احمدی هیچ ملاقات حضوری با او انجام نشده و تنها یک تماس تلفنی چندثانیه‌ای در روز عید برقرار شده است.
همچنین درباره وضعیت جسمی و روند پرونده او اطلاعات دقیقی در دست نیست.
احمدی پیش از این نیز چند بار به دلیل پیگیری مطالبات صنفی فرهنگیان بازداشت شده بود. ادامه بازداشت او همچنین خانواده‌اش را با مشکلات مالی مواجه کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77811" target="_blank">📅 18:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77810">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=ry4ySo0r_012vlJWHw7gmqhYybhl3QkgHtrDHQKjKHoRjOH3HvIWHgOerSKpkz8Qzm4825tZbSR5LXML0ePcbDldN_K21GiMF1dHQw5BtDDIct5fEQ6-Vg7Qptmbirw7sf3SIpgKnKxXVVKwdYvExsr-7t6u65oiUr1kyFubxb_fqsY2WvFrVHZU1qT71x8ZN7pRDUUK0CUWeLOf3HsHHdIDz1Z8p4PnM05uJ2MCkY0flEvFmXjcRjP29ZOzUsFJxHPCF6xbxV9-gqLSiPH_TH1VKumputCw0bsESokuiEmkOcy5yXSI_vJJc7OhdOIxVOh2aWjX3a1PDutuAWGGbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d54b46d0a.mp4?token=ry4ySo0r_012vlJWHw7gmqhYybhl3QkgHtrDHQKjKHoRjOH3HvIWHgOerSKpkz8Qzm4825tZbSR5LXML0ePcbDldN_K21GiMF1dHQw5BtDDIct5fEQ6-Vg7Qptmbirw7sf3SIpgKnKxXVVKwdYvExsr-7t6u65oiUr1kyFubxb_fqsY2WvFrVHZU1qT71x8ZN7pRDUUK0CUWeLOf3HsHHdIDz1Z8p4PnM05uJ2MCkY0flEvFmXjcRjP29ZOzUsFJxHPCF6xbxV9-gqLSiPH_TH1VKumputCw0bsESokuiEmkOcy5yXSI_vJJc7OhdOIxVOh2aWjX3a1PDutuAWGGbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات علنی متناقض؛ ترامپ در پی تهدید ایران، مخفیانه با پروازی دیگر از ترکیه خارج شد
ترجمه ماشین:
واشنگتن‌پست
دریافته است که تهدید ایران به ترور دونالد ترامپ، رئیس‌جمهور آمریکا، ماه گذشته باعث اجرای عملیاتی فوق‌العاده شد که طی آن ترامپ به‌طور مخفیانه با یک هواپیمای نظامی جایگزین از ترکیه پرواز کرد، در حالی که کاخ سفید اعلام کرده بود او سوار ایرفورس وان است.
این مأموریت محرمانه که پیش از این گزارش نشده بود، بدون اطلاع خبرنگاران و حتی برخی کارکنان کاخ سفید انجام شد؛ افرادی که تصور می‌کردند در همان هواپیمایی هستند که رئیس‌جمهور در آن حضور دارد.
دولت مدعی شده است که ترامپ روز ۸ ژوئیه با «ایرفورس وان سابق» ترکیه را ترک کرده است.
در آنکارا، ترامپ در برابر دوربین‌های تلویزیونی سوار ایرفورس وان قدیمی، هواپیمای غول‌پیکر جت، شد. اما به گفته مقام آمریکایی و بر اساس مطالب تأییدکننده‌ای که واشنگتن‌پست بررسی کرده، دقایقی بعد به‌طور مخفیانه با یک کامیون پذیرایی فرودگاه ــ از همان نوعی که معمولاً برای بارگیری غذا و دیگر ملزومات پیش از پرواز استفاده می‌شود ــ به هواپیمایی کوچک‌تر، یک C-32A نیروی هوایی، منتقل شد.
به گفته این مقام، در نتیجه ایرفورس وان، با حضور خبرنگاران و برخی کارکنان کاخ سفید در داخل آن، نقش یک «طعمه» را ایفا کرد.
متن کامل ترجمه فارسی گزارش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/77810" target="_blank">📅 04:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r-jSDp6-4_VhNTk5NDwG29SgHm3OvHHgdMNV7RLzEbH4nK8IvCmHPc8V6VEevMv1EqerxPb2hWwlk2yepvEpVH6KK-uVFVk2mk5PWOYNW04AW7YPm4KmpDNlv8NyuKQIsb33Z4M4qiuj3VZIySGmz3Rh8Cwj0lXBaFMYXLL3WeLOws3f6t8KGvVILTuE5SAYxgGhzJkVK1juWtaDzKFypNA7UwIVOTFst7lfx3AsLL4gqFokQj1IOI7jIVcCp7Zixlhew8YrdiUXhfuQMffy-4wkWNIiQOOxYRNEhSmvc3Poaq7WjePzDgq1fRvSFSiqZCNUvlMi2iEyq6bVIMdwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا بار دیگر نموداری را که نشان می‌دهد ارزش ریال در ایران در دوره دوم ریاست جمهوری او سقوط کرده ‌است، منتشر کرد. این نمودار نشان می‌دهد که ارزش یک میلیون ریال از یک دلار و یازده سنت آمریکا به ۵۳ سنت کاهش یافته و به «داخل زباله» رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77809" target="_blank">📅 04:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXISaCy3DPfX0qpo-lnW3qYHkxlgBlI97ZTVjqFrTtXGdyDMLUUWp3SBoAWupQ6YlktX8IXfRN8Fs1gQk7QOxnt3cufxACZfvBoAnixo9I_l9GgbdtxJGDzpbOaKuN6VwG584ksDUvl96Eso4JSK7VFmYS3rEtPLK3lnlQ_VZK0WyaKF-pqbHpDxUm9HkruXxbjjig6lZWdwHJVhOI4Pmwd229OoWbK2ynojaqm7_e2tKk8WG4vJU1P5ua7MZEFdGJH3dXinViviEJWxZlkTUCakt-ejun49A7JCnuf3s3qhObE-dCDcA0GfKnCq2GoTxigYWUUEsdz9uq_n1hBW6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «آکسیوس»، آژانس بین‌المللی انرژی اتمی به‌زودی مواد هسته‌ای باقی‌مانده در یک سایت مخفی در سوریه موسوم به «سایت ۹۹» را پس از توافق‌های محرمانه دولت ترامپ با اسرائیل و سوریه، از این کشور خارج خواهد کرد. این مرکز که در زمان رژیم بشار اسد برای نگهداری کیک زرد و بقایای رآکتور هسته‌ای «الکبر» استفاده می‌شد، پس از سقوط اسد به شدت تحت نظر اسرائیل قرار داشت و حتی ارتش اسرائیل برای جلوگیری از دسترسی به آن، ورودی‌های سایت را بمباران کرده بود. اگرچه این مواد برای ساخت سلاح هسته‌ای کافی نیستند، اما مقامات آمریکایی و اسرائیلی بیم آن را داشتند که در ساخت «بمب کثیف» و آلوده‌سازی منطقه‌ای مورد استفاده قرار گیرند.
براساس این گزارش، در ماه‌های اخیر و پس از مشکوک شدن اسرائیل به تحرکات حکومت جدید سوریه و احتمال مداخله ترکیه، تل‌آویو تهدید به حمله مجدد کرد، اما دولت ترامپ با مداخله به موقع و وارد کردن آژانس بین‌المللی انرژی اتمی به ماجرا، مانع از تشدید تنش و بروز بحران نظامی جدید شد. در نهایت، سه هفته پیش توافقی میان دمشق و آژانس به امضا رسید تا این مواد خطرناک به صورت ایمن بارگیری و منتقل شوند. مقامات واشنگتن این موفقیت دیپلماتیک را نشان‌دهنده رویکرد موثر دولت ترامپ در تعامل با حکومت جدید سوریه و حل‌وفصل بحران‌های پیچیده مانده از دوران اسد می‌دانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77808" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=cKZswgoHAE2nfNpjod8z-3GOUgEr_ah_FKyECcqPfP9WN8Klm59Ma3pSKdxzOfjcsMKguJm0A9PM_PXy8WE-4kbZduXz1ZGeep_iIiCJZYedPRmk0GSkOPC1GYj3EECIn3PJDsqATagcLciqthzI1vakUlemjGifZoX7FX9essRaRSuVJDUXzfIQ6Ht536TTKMZMgMNyXbKG_IsCUP7uoSOjcj-WAKe1grl5iwIakB03q1yul0wSVXZ1Lf50K46QA7IHX2d1pQ-TIdzEm1WgYWmm3rTveRkYj2NnskxkOcrnvGZNkW5vHOAAsIbDmoh1qqWsan7EJEKTyC87RoD_CA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/996dc0281d.mp4?token=cKZswgoHAE2nfNpjod8z-3GOUgEr_ah_FKyECcqPfP9WN8Klm59Ma3pSKdxzOfjcsMKguJm0A9PM_PXy8WE-4kbZduXz1ZGeep_iIiCJZYedPRmk0GSkOPC1GYj3EECIn3PJDsqATagcLciqthzI1vakUlemjGifZoX7FX9essRaRSuVJDUXzfIQ6Ht536TTKMZMgMNyXbKG_IsCUP7uoSOjcj-WAKe1grl5iwIakB03q1yul0wSVXZ1Lf50K46QA7IHX2d1pQ-TIdzEm1WgYWmm3rTveRkYj2NnskxkOcrnvGZNkW5vHOAAsIbDmoh1qqWsan7EJEKTyC87RoD_CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز دوشنبه در گفتگو با خبرنگاران در کاخ سفید با تاکید بر تسلط نیروی دریایی ایالات متحده بر تنگه هرمز گفت: «تنها نیرویی که در حال حاضر بر تنگه هرمز تسلط دارد، نیروی دریایی ایالات متحده است. ما محاصره‌ای برقرار کرده‌ایم که خطاناپذیر و مانند یک دیوار فولادی است.»
رئیس‌جمهوری آمریکا با بیان اینکه اجازه رفت‌وآمد کشتی‌ها بر اساس تصمیم واشنگتن انجام می‌شود، افزود: «ما اجازه ورود کشتی‌ها به ایران را نمی‌دهیم و آن‌ها اجازه ورود به تنگه برای رفتن به سمت ایران را ندارند، اما مسیر برای دیگران باز است.»
او همچنین با اشاره به پاک‌سازی مین در این آبراه راهبردی تصریح کرد: «ما تنگه را مین‌روبی کرده‌ایم و ۱۰۰ درصد بر آن تسلط داریم. آن‌ها ممکن است مشکلاتی ایجاد کنند، اما ورشکسته هستند و هیچ پولی ندارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77807" target="_blank">📅 00:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMhU93iencLrXv0CU26G6CKTJdyLsNma9-rB857P2dZQkhIXnbcRKcX-I_1zbyYjDQX6bs89J-8QFGs97WvLc_0Dw_cpHTp5jsmlWaoIzzE7t4Lmsvu3uoX2A9UUNrAicyOaj6X2EgXzvSzKwDdRKpMp0uDYeiEK8kZanzQf60JhWKflOT3eQKtj0NTwCrpUhPc7_RRyPPYXkVSjLCC7ebMGsNJyaf9hwu3BCEHd4Q_h567HgMns_rXjy90GNeSqi_OnjeagaN6NsfrZYcQE2HvhZaSu3CP2x6BdopA0ucPfb29PsKwaTy2rANTGYeQszJDG9hSEz8xaGty-TBBhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه ۱۹ مرداد و پس از مطرح شدن موضوع پرداخت غرامت بین ایران و آمریکا و کمرنگ شدن امیدها برای بازگشایی تنگه هرمز حدود ۵ درصد افزایش یافت.
ایران اعلام کرده که آمریکا باید تحریم‌های اعمال‌شده علیه تهران را لغو کند و برای بازگشایی این آبراه حیاتی، چند شرط دیگر را نیز بپذیرد. در مقابل، دونالد ترامپ، رئیس‌جمهوری آمریکا، گفت ایران باید بابت «تمام افرادی که کشته یا به‌شدت مجروح کرده است» غرامت بپردازد.
قیمت هر بشکه نفت خام برنت در پایان معاملات با ۴ دلار و ۱۷ سنت، معادل ۴.۹۹ درصد افزایش به ۸۷ دلار و ۷۲ سنت رسید. نفت خام وست تگزاس اینترمدیت آمریکا نیز با ۳ دلار و ۹۵ سنت، معادل ۵.۰۵ درصد افزایش، در قیمت ۸۲ دلار و ۱۳ سنت در هر بشکه بسته شد.
درصد افزایش قیمت هر دو شاخص نفتی، بالاترین میزان از هفتم مرداد بود.
هر دو شاخص نفتی هفته گذشته بیش از ۷ درصد کاهش یافته بودند؛ زیرا امیدها به نزدیک بودن ایران و عمان به توافقی که می‌توانست به بازگشایی تنگه هرمز منجر شود، افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77806" target="_blank">📅 22:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ph9h6odh2T9Ugy3RSoY6A_vB16l0lyISXdEoBz_yeI9xPbFAogX-JnO7TJJsHQ60sB6bjyks4X2SxMa7wyOKuggN6SzZJUcxMEb9__yewy6YD80wSHYvrcDe-26z33qSEzPx5iHBpXfz1yccxZZfZc75SJ4HaNirCOnCsSd8ZkYBImZRp8ZrgAd4X7NBQz9SaSb_mk-D81HP7bSxVUO4F0r48P1c8BRiaIHpsaMvH5_4S20HXy2RRDJyO8In-Yt5MMRmdfaCAFpkLted2U7vJXZWLgSp54ex6YJzJL0H-fskE-xVJgUTk845SL9Bm1O2x98Ql0uVcSZml-hRmhmhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست تازه ترامپ در ادامه متن یک ساعت پیش:
همچنین، در ارتباط با مذاکرات با ایران، ایران باید مسئول خسارت‌ها و مرگ‌ومیرهایی باشد که برای مردم لبنان، سوریه، یمن و غزه به بار آورده است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/77805" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77804">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOBWgdY_NeuTK7nhVdjK6jxuGshQdUk1hJ0aXRV3Xq9ZN6BovWskQq-k4mGrCCbqTjl_mS35D6oAaFdtAYEENkmrZ6CKTyrm1S_6DTNUCpKnTPNMtBLx3AYyfpYgj3lHwTBHBr7s1WNfm7EJqrgNrrTU35bYiJWV4Dqbrq-8EyDCtHpbWhXfPEtymtq53xtKbaKVxDy2oyes_Y1HohPW8RufM-2wPAXnmt7FjSu7AHTlz6a25gjbOv91TCmMgk65gvatboHXThR-NdFAJbdkV6fcgS1Tz4YrH20cGoXYyfbLlSirpYAPDH3U-gs29t5P9twuaNkHEaLJ4cyC9oP1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در مذاکرات موضوع پرداخت غرامت به ایران مطرح نشده، جمهوری اسلامی به خانوده‌های کشته‌شدگان غرامت بدهد
ترجمه ماشین:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار دریافت غرامت بابت خسارت‌هایی شده‌اند که در جریان درگیری نظامی پنج‌ماهه اخیر به آن‌ها وارد شده است (درگیری‌ای که به این دلیل آغاز شد که، آن‌ها
سلاح هسته‌ای نخواهند داشت
)؛ با اینکه این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما ایده جالبی است، چون حالا من نیز به همین ترتیب از ایران غرامت مطالبه می‌کنم؛ بابت همه افرادی که با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد ــ که به آن‌ها شهرت دارند ــ کشته یا به‌شدت زخمی کرده‌اند؛ اقداماتی که در ابتدا تحت رهبری ژنرال سلیمانی انجام می‌شد، از جمله بابت خانواده‌های کسانی که در ناو «یواس‌اس کول» کشته شدند، و هزاران نفر دیگری که در نبرد جان باختند.
علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته کشته است نیز غرامت پرداخت شود؛ چه رسد به ۵۲ هزار نفری که در پنج ماه گذشته کشته شده‌اند.
به نمایندگانم دستور داده‌ام که این موضوع را قاطعانه در تک‌تک مذاکرات آینده مطرح کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/77804" target="_blank">📅 20:19 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
