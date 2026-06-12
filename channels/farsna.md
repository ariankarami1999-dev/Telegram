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
<img src="https://cdn4.telesco.pe/file/gQQqWhgyXtQWK5_9N8-q6vyUpEBsLNCyQ9iLjf49lGK7xG-CiBaauy06TaP-0AQJslSNIjaWkAb4ImXi5cXdwNNXZmBVZhGsP0UljDZnwtTJROAOpaVjq2TTYnD9X_F_nqGPow1pYVDWeNiWZZ95FRl5RPsPLJOTCm4lY0bKXNmpye3q-EYy4zqHEzXNrU1RWDH4f2ycF1N8TGoY4-5p9i4DSP3ogIvIBvznt-64ixAH6DkbmNnGjZDqWrhwdGdhHhfA8n33h1bDaZlCaRWn3L0r5QmNUMQbHsVSKz5FQKu8agIxpPuePF5u_JTuzNwsdD_N6JEyIaOH16RFloPh6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-441533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JBlgLM25yKBwWL819J0uM6BY9zcvUgHx3tg9askbAl2pM6m8aqdFwXYR9oDEB2QxQBKoOwIPSfQiZ6XfGAHiHaly8DmN03wNB6pRNoh6LriyJn9B-59brIttKCi-73i6ADKvLqYMkdt8VMY8j4ya0y8D60iTVXHOpfWxkLHvk7-QmwnJZ4FCN3z5jYc4TU4fFXNCV1o2QZBtJeC71gFTPRfYT-nNxoVXGk1mFsUpUTaH1XEDPcrXQpuQfD665P4DONYD5EUvkIh5e4NnslUefiwuScVxIUSbSn7RRQiyIOgr4JBuyCdO-00mD_e2WpVijOMLQiMBYBE7-IzWTbAJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kS-Mesv2o1xDfMxQ3saz6ADabJjh1AGzRcNG8vM1KKyuEuiPgME6qEBOn8PHCTzsSXNSVt9sDSaa7QY4eqym7idT4QyL6vpBQ-LN1_PBN_ck3SCElHpbrfGrhTJrmFQkK-4BZhHvANmaLPdUn8vmqWXgDUuaGrFGFbAahThH2WUMYjZ_Hu8kTmcYeTv7LU3W42i2tdc5JZJl6XigtbzPlhrl-uOFKkl6E1wCpkj-120fZKttfHqYM3HD6MK-f5CKWuW8jSfMzMDhyFGQysM8ymOCmucg2tWFvYHUD98jG6WK9ttWLgwMVfYh7-xBA67MGfEuCC62XMVaIsxUZZgWxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حنظله: در پاسخ به حمله علیه زیرساخت‌های آبی ایران، تأسیساتی آب ایالت کالیفرنیا را هک کردیم
🔹
گروه هکری حنظله اعلام کرد که در واکنش به «حملات آمریکا به غیرنظامیان و زیرساخت‌های آبی ایران»، تأسیسات آب ایالت کالیفرنیا را هک کرده است.
🔹
حنظله اعلام کرد که باوجود دسترسی به سامانه‌های مرتبط، از ایجاد اختلال در آب‌رسانی شهرهای آمریکا خودداری کرده و این اقدام تنها «هشداری» به واشنگتن بوده است.
🔸
این گروه هکری هشدار داده که هرگونه اقدام علیه ایران با پاسخ متقابل در حوزۀ زیرساخت‌های حیاتی مواجه خواهد شد.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/441533" target="_blank">📅 04:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARGtrzXo3hrftk-a7pF_4BZMtc8nXyvCmVfY0qejOsQ-14lskxRZvP6VTjz6NcctUNkG7h5P8iQ43L8K1-K1CkohwSrs1z_fCNmha2ajjph0x7KkMyAMz4Q8CApLVCqa3u7ssYgWXUYCbzAVuW43Y2g3Kj4xewtB66ed_NTI9HVdax85_7GQdERR54F26PzkWOcGuG-QvNcJ6jeTAj_E0QKNEZ9plQYEZ7QsTNE3-LLyH5KUEivPJV30eeEeFffuJBu-1Lvw84w3o9czoxt6DXya7-kIXcPeVFz_HVfSrLLaDX14Fop2WrjH2CvnjBABrTu2AO68_vU9DHgKZ3-iAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانادا چت‌جی‌پی‌تی را برای زیر ۱۶ ساله‌ها ممنوع می‌کند
🔹
دولت کانادا یک لایحۀ جدید «ایمنی دیجیتال» معرفی کرد که هدف آن محدود کردن دسترسی افراد زیر ۱۶ سال به شبکه‌های‌اجتماعی است؛ مگر اینکه پلتفرم‌ها استانداردهای ایمنی مشخصی را رعایت کنند.
🔹
این طرح با هدف ایمن‌تر کردن چت‌بات‌های هوش‌مصنوعی طراحی شده و قرار است یک نهاد تنظیم‌گر دیجیتال برای تعیین استانداردهای ایمنی این فناوری‌ها ایجاد شود.
🔹
براساس این قانون پیشنهادی، شرکت‌هایی که از مقررات تبعیت نکنند ممکن است با جریمه‌ای معادل ۳ درصد از درآمد جهانی یا حداکثر ۱۰ میلیون دلار کانادا روبه‌رو شوند.
🔹
مقامات دولت کانادا می‌گویند شبکه‌های اجتماعی و چت‌بات‌های هوش مصنوعی برای جلب توجه طراحی شده‌اند و می‌توانند باعث اضطراب، انزوا، افسردگی و سایر مشکلات سلامت روان در میان نوجوانان شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/441532" target="_blank">📅 04:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KT7SSifEWZK0fPGo6r_w7fSiPtx0NIibmJrAzYMmVIWFeRGL_JoE2LrQ5Xsf7o73Cx_28B_9GMoEW8WPNJEhjg8c-DAkTCvrRQkVfikbxklqnTxcxbPwWPgH9Udsb0gmFV54f9bEJzj8ZQmgJAUNlRXodkgrJwlaflob7k88hZnT6U9kuxd9F4BTFZJcmWBOM0e_P6bnqs2FCQV1xlj1lf4eQTyVCQ8-AepE5VmCL-T3SPFWoft0VHVu3t5eZbTzkxDAqj9WMgc7VB-S1RaqKyaYYuKlDxZS2YwhfaHEuKQ8_qlcDxA2_AKhypzmar59Bnnx9Z2Dm25U588kyjlStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزۀ خفیف پردیس تهران را لرزاند
🔹
ساعت ۳:۳۰ بامداد زمین‌لرزه‌ای به بزرگی ۳.۱ ریشتر در عمق ۱۰ کیلومتری زمین حوالی پردیس تهران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/441531" target="_blank">📅 03:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de09e75f4.mp4?token=nDogg32020Kgg_IEXPiM9feW86mlWvjljsaJ-sH9btJbh0EJJq9um1sLkidKDmluWEerb8MeTvYYlhe7qbvT3SSADMZ7YB92kjkCAdgqhIvRS2I-IBYc3pDIuvM2p3W9rzkjtiHDsl0lB0-rMQCqJFeCIVDvR4S37aJ8pv49jKP9AGHtwkWQ0Mc5QrGoyPzy25GJ2yPB5WwjtTzX1MEI_fEmQryJBw0qsEAINZ7PfKze5wNW7GqgdUFtavSAhtHAwOAXlUVwpa3Lb7_fd34f4SAofD7No5uMNsV8H2Bx0zWAF5ioB8XuQh5DpCIR9te-Pw_UiFFz0DIMWRL8y5HI0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de09e75f4.mp4?token=nDogg32020Kgg_IEXPiM9feW86mlWvjljsaJ-sH9btJbh0EJJq9um1sLkidKDmluWEerb8MeTvYYlhe7qbvT3SSADMZ7YB92kjkCAdgqhIvRS2I-IBYc3pDIuvM2p3W9rzkjtiHDsl0lB0-rMQCqJFeCIVDvR4S37aJ8pv49jKP9AGHtwkWQ0Mc5QrGoyPzy25GJ2yPB5WwjtTzX1MEI_fEmQryJBw0qsEAINZ7PfKze5wNW7GqgdUFtavSAhtHAwOAXlUVwpa3Lb7_fd34f4SAofD7No5uMNsV8H2Bx0zWAF5ioB8XuQh5DpCIR9te-Pw_UiFFz0DIMWRL8y5HI0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ جانباز پای لانچر به سوالی دربارۀ دلتنگی برای دست‌وپایش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/441530" target="_blank">📅 03:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e016e32dc0.mp4?token=AHSPQA3D6QrOnt-jypuFosQXqh4bSSTdzvc1uS5Us9eSSSceJM24alqyUrPtS2k_f28ucShrks6UfxbAFL_UFS36lIOaMjE6qacWsl9djSqCOqsrgcDIKcSpgpNIXoJe2yXd3jPQcQOTPy2LcoWozOx0ckYh0zJtTunMDHdht1Aw5E76D5XEw-8eBKltCeTqCzckkJiCBoHkdmn3uv8RjZxu3CBVqo_iwkfad_5rc4lUG2mbmprKTXPgMC4nB6gJ2v5HAlpKOFLA5X_0lE6nCW9XYOijEoou-uxcSBI_H1jNffAQ1UDxcpJTW0gHMmvsj31WqrPfYmhZ_2beFe5OgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e016e32dc0.mp4?token=AHSPQA3D6QrOnt-jypuFosQXqh4bSSTdzvc1uS5Us9eSSSceJM24alqyUrPtS2k_f28ucShrks6UfxbAFL_UFS36lIOaMjE6qacWsl9djSqCOqsrgcDIKcSpgpNIXoJe2yXd3jPQcQOTPy2LcoWozOx0ckYh0zJtTunMDHdht1Aw5E76D5XEw-8eBKltCeTqCzckkJiCBoHkdmn3uv8RjZxu3CBVqo_iwkfad_5rc4lUG2mbmprKTXPgMC4nB6gJ2v5HAlpKOFLA5X_0lE6nCW9XYOijEoou-uxcSBI_H1jNffAQ1UDxcpJTW0gHMmvsj31WqrPfYmhZ_2beFe5OgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفوذ حنظله‌ به سامانۀ پهپادهای FBI و استخراج داده‌های محرمانه
🔹
گروه هکری حنظله اعلام کرد که به سامانه‌های امنیتی پهپادهای اف‌بی‌آی نفوذ کرده و ماه‌ها به تصاویر و داده‌های این پهپادها دسترسی کامل داشته است.
🔹
حنظله در پیام خود تاکید کرد که حتی اطلاعات مربوط به مأموران اف‌بی‌آی نیز برای این گروه هکری قابل مشاهده بوده است.
🔹
این گروه هکری با
انتشار تصاویری که به‌دست آورده‌
، گفت این تصاویر مستقیماً از پهپادهای امنیتی اف‌بی‌آی دریافت شده است.
🔹
حنظله همچنین اعلام کرد که ممکن است هم‌اکنون از طریق پهپادهای MQ-9 ارتش آمریکا، تحولات پایگاه‌های نظامی این کشور در بحرین را رصد کند.
🔹
حنظله در پایان پیام خود تأکید کرد که همواره «یک گام جلوتر از سایه‌ها» حرکت می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/441529" target="_blank">📅 03:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKe-TEAVU_J_xBQ7zK-TrecFRxaOcOrhY7pKVMnm3UBZ_m2rkqeHW5eIjhJ3KcSYyvC0cjVuf8fP--1gJEFQJZBx1NoXNmYrDZ4jU4iW9vbWN6AaIqyYF3gHu-6R_ncUPnJEWsKkvR9jW1CMMwKqgOhH_WsMk-27SuGa8mXp3b23oXWkQ3TlrrMj7ewxMwtgtAd8aEW1eM2w8e1JmqShLqWv5cPt6kWHzav2AYXMLkIIJ1DcGoP0RYngi19piqszKef2ARZCvCf64-GCwHuUbsfhG9La_1WyuInX6BgxR7xawBOCU8TRNPRBkMw7AeVryJpaTqVS1kYwn9WzOUsgig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ: امروز به جنگ با ایران پایان دادیم
🔹
رئیس‌جمهور آمریکا در ادعایی جدید گفت: «ما امروز به جنگ با ایران پایان دادیم و آن‌ها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند؛ این همان چیزی بود که ما بر آن اصرار داشتیم.»
🔹
وی اضافه کرد: کل هدف ما همین بود؛ این موضوع ۹۵ درصد از هدف ما را تشکیل می‌داد و آن‌ها این کار را به محکم‌ترین شکل ممکن انجام داده‌اند.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/441528" target="_blank">📅 03:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">موشک‌های ایرانی دنبال انتقام از غول‌های فناوری و بورسی آمریکا
🔹
از ۹ اسفند تاکنون آمریکا، اسرائیل و شرکای منطقه‌ای دست به جنایت علیه مردم ایران زدند.
🔹
در نگاه اول ممکن است به نظر برسد که تنها ارتش این کشورها شعلۀ جنگ را روشن کرده‌اند اما بررسی اسناد مالی، قراردادهای نظامی و دفاتر منطقه‌ای ده‌ها غول فناوری و سرمایه‌گذاری نشان می‌دهد که شبکۀ پیچیده‌ای از نهادهای وال‌استریتی و سیلیکون‌ولی، نه‌تنها از برنامه‌های نظامی آمریکا و اسرائیل حمایت مالی می‌کنند، بلکه به‌عنوان مجری مستقیم، شریک اطلاعاتی و تأمین‌کنندۀ زیرساخت، در قلب این برنامه‌ها جاخوش کرده‌اند.
🔹
از اسپیس‌ایکس و استارلینک ایلان ماسک تا گوگل، از صندوق‌ها تا بانک‌های بزرگ همگی به شکلی مستند در زنجیرۀ تأمین جنگ، جاسوسی و تسلیحات هوشمند نقش دارند.
🔗
این گزارش را که با تکیه بر اسناد رسمی، تصویر روشنی از این هم‌پوشانی منافع مالی و نظامی ترسیم می‌کند،
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/441527" target="_blank">📅 02:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441526">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3_KpKWpOzympelC_-YKo7jWuwTBGn-IZX5PHl4B6LSrlB65EPhQYNAGZDQJfs2sc8E1bdKEA5dz_hrepp7K_QDSsp70pUdLrwFoEVMqTpMkTnyONu7zGGmTmJsJkJz9oDni2PYxrY-r065HjMCpTyw6PnYElpPGYxa6JDBblOxmaPVJcgiaSM7pFcUJP86z6KeFsoFevkRfBJYTmOyK15pdgPaXiVClzCaPt7h0p-vrsrEHH8qDN9jnJX9sj-E1CkWBuxpnHxdRY1rFWxxaDpJe7Jb-wNZSUqqXytm0NVOPjTX_HCCMRnagNp4CmFrug9Z-JIPk1A1WbSa9WJItYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی آفریقای‌جنوبی اولین منتقد به داوری جام‌جهانی شد
🔹
سرمربی تیم فوتبال آفریقای‌جنوبی ‌پس از شکست مقابل مکزیک در افتتاحیۀ جام‌جهانی ۲۰۲۶، به انتقاد از داوری پرداخت و گفت با کارت قرمز دوم تیمش موافق نیست.
🔹
او دربارۀ اخراج تمبا زوانه گفت: بازیکن مکزیک راه بازیکن من را سد کرده بود. این تصمیم داور بود و باید آن را بپذیریم، اما به‌نظر من آن صحنه آن‌قدر شدید نبود که کارت قرمز داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441526" target="_blank">📅 02:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441525">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAimPLBCJn0NGzLY_og_F7AUm41axl2Ut6lNVhYyoYh6JHwmTFWZ0XUAKDdgAE7A67EVJ-xixQqRwjv5YwESyEgKx57ugX4BUyzyq4i7QmEy6p7AUHOsGoI4iDXfWdU5ziDv6A7jW6gnySAqahlS5eS4DNnzZc5NsMeDbQ7mM2tvnHSK_JtDdgHd_vj3YlmJsvSfyiwx8mfaTgrPN6xV6SymsUjHAKamDkHjRImCe44-nJkX7PTjmHWYLLH8IVGS8gIe49ir5UQV378vUFsy2cWJzTFpvtQi1ItP0qqpaPXr70JPasSQvhc8r7zwyZNwm0WTVDTc1lo01M02QzhWqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت اضطراری توسط یک جنگنده F-35 آمریکا در آسمان امارات
🔹
برخی گزارش‌های تأیید نشده حاکی است یک فروند جنگنده نسل پنجم F-35 لایتنینگ ۲ (Lightning II) متعلق به نیروی هوایی ایالات متحده در حین پرواز بر فراز آسمان امارات متحده عربی وضعیت اضطراری اعلام کرد.
🔹
ین جنگنده پیشرفته با فعال کردن کد اسکوآک ۷۷۰۰ (Code 7700) بر روی دستگاه ترنسپاندر خود، وجود یک نقص فنی یا وضعیت اضطراری عمومی را به برج‌های مراقبت و رادارهای منطقه مخابره کرده است.
🔹
کد ۷۷۰۰ در پروتکل‌های بین‌المللی هوانوردی به معنای وقوع شرایط اضطراری در هواپیما است که به کنترلرهای ترافیک هوایی هشدار می‌دهد تا مسیر را برای فرود فوری و بدون نوبت جنگنده باز کنند.
🔹
هنوز جزئیات بیشتری درباره علت دقیق این حادثه یا وضعیت فعلی جنگنده منتشر نشده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441525" target="_blank">📅 02:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6587e422.mp4?token=rjIiBup0hIit5r_shF8VOjTUTv7IuG1tZXj8JciW6HDxocjCAHOnqGKL6GcYS5TE7BcWofuolwAqsLbJ4CzZCOWRI0V2GFF3czAaTB9HLWbaru6X_ckLFoqibZWMFCIOxaXBo6YgShRcqPUUPW9uiFpAPSrC-VIS5srb3fT3rqAMgy3UMg4BMr1ZWJQM_WLFiTROpcErlSWb0RNBIGx597x96KOws0WvpU8n3EZ3jqqR0x57C_qrjcWdJNfJh89tvUEgmuHseoy3iOx7Z4SLDd5aE8FnsI7IevcJ9LZWe4paXkolbefE4jEpoJYu65v9pVsKWMtJoHTDZEMSDac5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6587e422.mp4?token=rjIiBup0hIit5r_shF8VOjTUTv7IuG1tZXj8JciW6HDxocjCAHOnqGKL6GcYS5TE7BcWofuolwAqsLbJ4CzZCOWRI0V2GFF3czAaTB9HLWbaru6X_ckLFoqibZWMFCIOxaXBo6YgShRcqPUUPW9uiFpAPSrC-VIS5srb3fT3rqAMgy3UMg4BMr1ZWJQM_WLFiTROpcErlSWb0RNBIGx597x96KOws0WvpU8n3EZ3jqqR0x57C_qrjcWdJNfJh89tvUEgmuHseoy3iOx7Z4SLDd5aE8FnsI7IevcJ9LZWe4paXkolbefE4jEpoJYu65v9pVsKWMtJoHTDZEMSDac5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حق پخش جام‌جهانی ۲۰۲۶ به ایران رسید
🔹
مجری برنامۀ «جام ۲۶» شبکۀ سه، با نمایش سند مربوط به خرید حق‌پخش مسابقات اعلام کرد که صداوسیما حقوق رسانه‌ای جام‌جهانی ۲۰۲۶ را خریداری کرده است.
🔹
در ماه‌های اخیر گمانه‌زنی‌های مختلفی دربارۀ وضعیت پخش این رقابت‌ها در ایران مطرح بود، اما اعلام رسمی این خبر روی آنتن شبکۀ سه به ابهام‌ها پایان داد.
⚽️
جام‌جهانی ۲۰۲۶ برای نخستین‌بار با حضور ۴۸ تیم و به میزبانی مشترک آمریکا، کانادا و مکزیک برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/441524" target="_blank">📅 01:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ایران اجازۀ عبور نفتکش متخلف از تنگۀ هرمز را نداد
🔹
پیگیری خبرنگار فارس در بندرعباس از منابع محلی نشان می‌دهد دقایقی قبل نیروهای ایران اجازۀ عبور یک نفتکش متخلف که بدون هماهنگی وارد محدودۀ تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441523" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/140d000d3f.mp4?token=aB1dynWMXx_wec7mIZ6c0OK-8cAH7SOMEOKZZ1DR0IVre9AXO9iQ4kPTuqU4Kvpf4m77sBnaz_p2tz_fUK14qZU05iG7bA9FNIPFmWX_VOZA6gtXTi0s1cX3aQ4HFPchm5IQ9A-PP1DugR_IGBgXctseRhftF5ybgHDfgg8Q5b4V7_ZKCSYGylHR04_dFnUnvn26wiMi_yMMeJrGVexN8PkVCqxWbXZFtXPbB3bQzgxRxZjOyyaEQjsQj4BV9l_iVSNsppL0onCtBJmEamP_3IJXpz7YK56m6SKWy6REzSGIzNuF3UKRXqvk794RaxmaheDYfDZt_Fc8dtFK6ptR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/140d000d3f.mp4?token=aB1dynWMXx_wec7mIZ6c0OK-8cAH7SOMEOKZZ1DR0IVre9AXO9iQ4kPTuqU4Kvpf4m77sBnaz_p2tz_fUK14qZU05iG7bA9FNIPFmWX_VOZA6gtXTi0s1cX3aQ4HFPchm5IQ9A-PP1DugR_IGBgXctseRhftF5ybgHDfgg8Q5b4V7_ZKCSYGylHR04_dFnUnvn26wiMi_yMMeJrGVexN8PkVCqxWbXZFtXPbB3bQzgxRxZjOyyaEQjsQj4BV9l_iVSNsppL0onCtBJmEamP_3IJXpz7YK56m6SKWy6REzSGIzNuF3UKRXqvk794RaxmaheDYfDZt_Fc8dtFK6ptR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سپهبد شهید حسین سلامی: آرزو دارم به شهدا و حاج‌قاسم بپیوندم
🔹
در پیکار حق و باطل سرانجام حق پیروز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/441522" target="_blank">📅 01:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9NY74aHKxpv3CMdHOmJ2tzhWCtEWOZIrKBvIp43JqXyJibyEyAQmEO08UrZG4rGujb4CmPOBBmXUiISJlwkjuxJPdnyxxjPvTKDh6dcuQrU71ga25n25fuQYihoatGEbx_c8qebsd9jd2BXbLQ04CiVQd_uUkATlg3PPsRqWw4w_RJDdcWDWpW_NpHVJdxT5PLqSRdeJMnlkgjtXUtxIMTDq05l2cW5zv7B9cKvDSYdIGH7j8c25AEsSYJg6yZzvx7kqYxAzEs1uoS9yjRC9_ecFLpkfixgbTC9XZ9zLu9PN2jTiXzh8f9zQgJTWmkMlbqeGfCKCfrwCex1eNTCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ اخراجی و ۲ گل در افتتاحیه میزبان جام را با برد شروع کرد شروع فاجعه آفریقای جنوبی
⚽️
جام‌جهانی ۲۰۲۶ مکزیک ۲ - ۰ آفریقای جنوبی    @Sportfars</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/441521" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVmtSA4Wh9YSIWSj9wgK_TJtoCqFXcagWP3qyixOxJFjj1NXO99u_XMJ2VPEEL_0Rwa7rsYlGiBFCgLGDzdBT44vMZpW83ONAfPo9cgCcZ8POUcQFAvI20OK0CGKLKotgXwp81o1-Utrq6A68PfmwlSpQfYeflK7sKwMDyJGGoTN43AZD2Kmounb1jFRHZcXtYeiXeAo06P1YXifmXwaOQFaI67xsIs8BC2VqE97HPRqnoe5926EzRAw8ow193Drn15dHFgWRBSOPVhArLFCIdi3vUyNP-2-nwg4rz2JDjzp8HMuuIICBpn7eEhv_D7Whqb5DLYmXqdC3fFzM0vCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: حملات آمریکا به کشتی‌های تجاری و راهزنی دریایی، تهدیدی جدی علیه دریانوردی بین‌المللی است
🔹
سخنگوی وزارت خارجه: حملات بی‌رحمانه آمریکا به کشتی‌‌های تجاری هندی که موجب قتل حداقل سه شهروند هندی شده است، نتیجۀ سیاست سرقت مسلحانه و راهزنی دریایی دولت آمریکا است.
🔹
با خانواده‌ و دوستان ملوانان هندی کشته‌شده ابراز همدردی می‌کنیم و به مردم و دولت هند تسلیت می‌گوییم.
🔹
جامعۀ بین‌المللی باید آمریکا را به‌خاطر رفتار قانون‌شکنانه‌اش پاسخگو کند؛ رفتاری که تهدید علیه صلح و امنیت جهانی است و آزادی دریانوردی را به خطر انداخته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441520" target="_blank">📅 01:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-XSFP2UU9uX88u_xciQ1TvMTPgfQcTL_Lok8J9o0BtXErRtYZjfsWvk_VTZOsP7DghQhJhO68oZUkXQ6scDqDdeBCibswaynm4PVTwMEaVFqVHY4OSCIgmGT_o0u9RApU_FHkHOSPE7xCIP74-9Hiv_n7NdDBunNcFLJl9Xwa3gJAcHSPq1AOv4LFDibay72qQkn3l6ZBuP9-2MfJvXQrhvFJF_E7XDn2WP9Z4q3R9nVWcQG5PCAzhdi2q4hMOZDVjKTjyiTKZ1bxwWZXXcW9yUGLlboXlZR5lXGA-nXOwfe-sftxJNALcEyoHoEZnS2jD7n5MXnP7s9wGI3Bbt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ اخراجی و ۲ گل در افتتاحیه میزبان جام را با برد شروع کرد شروع فاجعه آفریقای جنوبی
⚽️
جام‌جهانی ۲۰۲۶ مکزیک ۲ - ۰ آفریقای جنوبی    @Sportfars</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/441519" target="_blank">📅 00:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuVK5bFUBeebSbVszXNm2FYMm8In33JKNyrKH3O2mbkvy14thhe3MjOPQYgaT2B0Fy4Gax9djXGHi5aZ8P3U-QoIg4Ydb4VQbKIEFpiAHObSel-ZBeJ-VeW41dsAkfCYy8G_XtEngfZCz0_ILZ04xWmfPgl2fG8NTqSIjskmHhvrqy96-EA0chwJ8h7D1EDtSx5uG6PORhHMpc8f81B4APfEqaWxt1BR3gex67socGqq2skwrZ6REuiRTMIUBTT5QkDnr-ZNg4yXIoTDBWqpHn06df01rQjPefCx8y23a9GKMMdxMmmcBzzinVJKJN38TChipMbaf-xLCaEfVJXEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ اخراجی و ۲ گل در افتتاحیه
میزبان جام را با برد شروع کرد
شروع فاجعه آفریقای جنوبی
⚽️
جام‌جهانی ۲۰۲۶
مکزیک ۲ - ۰ آفریقای جنوبی
@Sportfars</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/441518" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxWJmEwesfEKFlJGupdJVWUG2ft4onNggyD0dZCftVU2tSM79E6OUHsrHX6DTmPEyoIuj13x4ARBI_cXbEA8p09p-xJT3nXIT2b1GyXqegz4Nn1y564wWLLiaN3mTIz9oNkkbkPJK7BPoGY_eoF63X5hp8GWtCEtAmWjYnUyZ3vCccdk_xgB_od7GwlqroBrvbI_5jyUZmIMrM3Qo5pE_51yMPHMHoXNMZPNCRMWE9hucMhHO1BJmGc91RP--R4Ny5tNwJe-Wq3aPt0U0Jmoy7v2eyNtZ86n1qzJWHtFdKovGmEAED0rBNbylDqBh4K-f2nuQLgpGTGsoRPpEwxQxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست ایران در دومین بازی
اشتباهات فردی کار دست شاگردان پیاتزا داد
لیگ ملت‌های والیبال
🏐
ایران ۰ - ۳ بلغارستان
🇮🇷
ایران: ۲۱ | ۱۹ | ۲۳
🇧🇬
بلغارستان: ۲۵ | ۲۵ | ۲۵
@Sportfars</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441517" target="_blank">📅 00:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9017f90840.mp4?token=YB0U__2AEbB_W63WHXuEUVUsqnceLb8z-fmudDKEsTagNVc5Xr2UBnN9P8Ur_9EaiCPUaVagbE_2P4PzDJw5wzWCWjiB8ouqokptyFDTyg8cEi-upkqAeNgpRVdQ4KL6oL_mpOrFLaA-7e4VKd1zLTlQaNC9mVamqQcJ4deZXw6IVS9vKZAvnKK0YjYn1VcMzJT182tKtgSKL90xQ-sRqPaQRcF1WFaJMKCy2QY5e5KdFQ3Z9YJ0TSrQKbrBlPz3t0i-3chHSCorl1MVAdJbnHhqK-t_S9cciyfEAI7xMT6X8f7BmEhDz_Cf6OJW4RsTmi90QkPwdLrsr4wWj0EqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9017f90840.mp4?token=YB0U__2AEbB_W63WHXuEUVUsqnceLb8z-fmudDKEsTagNVc5Xr2UBnN9P8Ur_9EaiCPUaVagbE_2P4PzDJw5wzWCWjiB8ouqokptyFDTyg8cEi-upkqAeNgpRVdQ4KL6oL_mpOrFLaA-7e4VKd1zLTlQaNC9mVamqQcJ4deZXw6IVS9vKZAvnKK0YjYn1VcMzJT182tKtgSKL90xQ-sRqPaQRcF1WFaJMKCy2QY5e5KdFQ3Z9YJ0TSrQKbrBlPz3t0i-3chHSCorl1MVAdJbnHhqK-t_S9cciyfEAI7xMT6X8f7BmEhDz_Cf6OJW4RsTmi90QkPwdLrsr4wWj0EqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تنگهٔ هرمز به‌دلیل اقدامات غیرقانونی آمریکا همچنان بسته است
🔹
کشتی‌ها باید مراقبت کنند برای اینکه امکان تردد ایمن وجود ندارد. @Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/441516" target="_blank">📅 00:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🎥
سخنگوی وزارت خارجه: ابتدا باید مراجع ذی‌ربط نظام دربارهٔ جزءبه‌جزء هرگونه تفاهمی به جمع‌بندی برسند‌
🔹
به‌محض اینکه به جمع‌بندی نهایی برسیم رسماً اعلام می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/441511" target="_blank">📅 00:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واکنش طنزآمیز کاربران به تناقض گویی ترامپ درباره تنگه هرمز
🔹
تناقض‌گویی جدید دونالد ترامپ درباره تنگه هرمز و توافق با ایران، به سوژه داغ کاربران شبکه‌های اجتماعی انگلیسی و آمریکایی تبدیل شده است.
🔹
ترامپ صبح امروز مدعی شد «آمریکا کنترل تنگه هرمز را در دست گرفته است»، اما ساعتی پیش اعلام کرد که توافق با ایران «نهایی شده» و به این ترتیب تنگه هرمز باز می‌شود. کاربران با برجسته کردن این تناقض، می‌پرسند: «اگر تنگه هرمز باز می‌شود، پس چرا صبح گفتید در کنترل ماست؟»
🔹
ایران تأکید کرده که هیچ توافقی نهایی نشده و موضوع همچنان در حال بررسی است.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/441510" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3137e1f2c1.mp4?token=o1JNzAkBwmUFaauSfG_ceO5UoIOuCyVAiQkOs-NTbphn4Gad1mxfP9Irah_GLE-XaiTcmMeSOrFnAMcmtb-feSo6wXpcNQTfiG9q8H5OmMiLG_Ow8lIcSd0DKhp1jEEcwcajDVYG6UI5jzVhQliinyXl3rk1fgDKVa1jkH87TS8gYy8cOiSBOOJS1T-dcLe6Htf_J-ZngcN52SYx3C27Af2AVSraIWwvml_vsa18ehC_c7tpSTOeYCo00Oa4wSGaGDmlPlFZpmrd9_swLhd4MvWXw27s2Aji_YoFTxrfJI1BEaJ9RggAmq07dWNpDw6j7dgBmhG-wo2nHcLz4K0j4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3137e1f2c1.mp4?token=o1JNzAkBwmUFaauSfG_ceO5UoIOuCyVAiQkOs-NTbphn4Gad1mxfP9Irah_GLE-XaiTcmMeSOrFnAMcmtb-feSo6wXpcNQTfiG9q8H5OmMiLG_Ow8lIcSd0DKhp1jEEcwcajDVYG6UI5jzVhQliinyXl3rk1fgDKVa1jkH87TS8gYy8cOiSBOOJS1T-dcLe6Htf_J-ZngcN52SYx3C27Af2AVSraIWwvml_vsa18ehC_c7tpSTOeYCo00Oa4wSGaGDmlPlFZpmrd9_swLhd4MvWXw27s2Aji_YoFTxrfJI1BEaJ9RggAmq07dWNpDw6j7dgBmhG-wo2nHcLz4K0j4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اعلام تاریخ برای امضای تفاهم، گمانه‌زنی رسانه‌ای است. @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441509" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: بخش عمدهٔ متن تفاهم نهایی شده اما مشکل این است که مواضع ضدونقیض آمریکا باعث اخلال در روند می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/441508" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: به‌دلیل اقدامات غیرقانونی آمریکا در تعرض به ایران، روند دیپلماتیک هم تحت تأثیر قرار گرفته است
🔹
میانجی‌ها فعال هستند و ما خیلی شفاف به آن‌ها مواضع‌مان را اعلام کرده‌ایم‌. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/441507" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اگر قرار بود ایران تحت فشار و تهدید از مواضع اصولی خود کوتاه بیاید، یک‌سال قبل این کار را انجام می‌داد. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441506" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکایی‌ها در این چند روز تلاش کردند که مطالبات و خواسته‌های غیرمعمول تحمیل کنند اما ایران نشان داد که به‌هیچ‌‌عنوان تسلیم شرایط و خواسته‌های نامشروع طرف مقابل نمی‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/441505" target="_blank">📅 00:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b0c3fae3.mp4?token=aV7IzzOddT4QFE4Ey0cZiwiGInrwvKZyUtT6hIeELagFk27x6M_dMVBMWztVWfGgaeAJRBpFmQPIQ1eviyn07og_Gyd6OYjIsjxO81n3dqHX_ckepu5t7rwmpoLupkgBKvUVan_DxQSYmozEGLgNt7wfGqGpQK7iarivLqUrSdL_KFXAdjVKfcqV9GeGa2ACNjFOXjFMcT_gd6lNp5GXUyxW5fKAXR779_ZzJV4snfbtN_v4Gj4YJLsJmTdOI95nUuID5_qFgnOPDitASjguxNZEfTxChAeXYplqejaDw7IpllsaiOCwyuWdPZuF_LAecQVY0tHislQ2JFYgrtGGOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b0c3fae3.mp4?token=aV7IzzOddT4QFE4Ey0cZiwiGInrwvKZyUtT6hIeELagFk27x6M_dMVBMWztVWfGgaeAJRBpFmQPIQ1eviyn07og_Gyd6OYjIsjxO81n3dqHX_ckepu5t7rwmpoLupkgBKvUVan_DxQSYmozEGLgNt7wfGqGpQK7iarivLqUrSdL_KFXAdjVKfcqV9GeGa2ACNjFOXjFMcT_gd6lNp5GXUyxW5fKAXR779_ZzJV4snfbtN_v4Gj4YJLsJmTdOI95nUuID5_qFgnOPDitASjguxNZEfTxChAeXYplqejaDw7IpllsaiOCwyuWdPZuF_LAecQVY0tHislQ2JFYgrtGGOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: آمریکایی‌‌ها درحال القا هستند که جمهوری اسلامی تحت فشار به توافق رضایت داده است، در حالی که ما به هیچ عنوان از خطوط قرمز خود کوتاه نخواهیم آمد. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441504" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمدهٔ متن نهایی شده بود اما آمریکایی‌ها مواضع خود را تغییر می‌دادند
🔹
ایران ثابت کرده که در آنچه به‌عنوان خط قرمز معین کرده، مماشاتی ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441502" target="_blank">📅 00:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441501">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمدهٔ متن نهایی شده بود اما آمریکایی‌ها مواضع خود را تغییر می‌دادند
🔹
ایران ثابت کرده که در آنچه به‌عنوان خط قرمز معین کرده، مماشاتی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441501" target="_blank">📅 00:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e82794b.mp4?token=b2BTH7gwQp3CuNHwXPk2BzGEoHP28_tkC9UetITFQo3RDDS4Xmo1gt2E2fXP1usLmlLj6oEOqyKVblqSVC5QyTFfDm-5Mw30qX3-7ZpQQMPOKUpB9_0kU8tTLjti2BRXvcVqLax36tsKX7J-YaxYsAtvQgOaq9XmAP6VOVLXc-mc7TDNgno-oit1Z0oM6CHOyFSkG-1yv-G3X7XCNM0L7Ana7aUw0-NJEOsz60kF4CgKe725vpsVNWf-xSg4itLv50PJck5KIlBz6R_Ken0hPwG2mvim8OUfDFR3X5J2IOMQWGaLpkusaYj5lqpNNKp1ECIKVaLFUlJzQLV-U82hgSq-n4Grs0B0pE4jmMpIcFdDJLV_tXSmUfxAOTktpebBAZ-v728eZnj9oKzAnxSQHa_VdcyzT1s1bwopkAqS55yGq6U4z3D3pIlWVoE_MhvqMcm1dJ_WCaHjaThCPszlpKqHYt4n308HOeXVmUczMy1P7MZ6HGCrjceGagigx2-aU6gL3mbNValnw1jLiE5GdzNX0GHxlJhyFpAVSfR0P91er8iIzCE2irzIke08G-WpUYuGq0LdH2gAe-6ZPgJrn6SKqJ7_BJ-2SHXAybgbn72U7WrzuRTjhtfG6cFqaug4QaVbsMSsa7g3DA82EPK_YGnyVl4W-wQq9SGzO6V4CJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e82794b.mp4?token=b2BTH7gwQp3CuNHwXPk2BzGEoHP28_tkC9UetITFQo3RDDS4Xmo1gt2E2fXP1usLmlLj6oEOqyKVblqSVC5QyTFfDm-5Mw30qX3-7ZpQQMPOKUpB9_0kU8tTLjti2BRXvcVqLax36tsKX7J-YaxYsAtvQgOaq9XmAP6VOVLXc-mc7TDNgno-oit1Z0oM6CHOyFSkG-1yv-G3X7XCNM0L7Ana7aUw0-NJEOsz60kF4CgKe725vpsVNWf-xSg4itLv50PJck5KIlBz6R_Ken0hPwG2mvim8OUfDFR3X5J2IOMQWGaLpkusaYj5lqpNNKp1ECIKVaLFUlJzQLV-U82hgSq-n4Grs0B0pE4jmMpIcFdDJLV_tXSmUfxAOTktpebBAZ-v728eZnj9oKzAnxSQHa_VdcyzT1s1bwopkAqS55yGq6U4z3D3pIlWVoE_MhvqMcm1dJ_WCaHjaThCPszlpKqHYt4n308HOeXVmUczMy1P7MZ6HGCrjceGagigx2-aU6gL3mbNValnw1jLiE5GdzNX0GHxlJhyFpAVSfR0P91er8iIzCE2irzIke08G-WpUYuGq0LdH2gAe-6ZPgJrn6SKqJ7_BJ-2SHXAybgbn72U7WrzuRTjhtfG6cFqaug4QaVbsMSsa7g3DA82EPK_YGnyVl4W-wQq9SGzO6V4CJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش مردم پیشوا به تهدیدهای ترامپ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/441500" target="_blank">📅 23:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee25fa2f5.mp4?token=i8J7u_XSevu2mzFYAdIYRLx25QJfeyyFI1BwG_kl2ak7b3tHbCSfWyx8WLh5JwJil-5BY9LSozPnDSJtrGQKidhZ16zu8kKbE6CdlZlx5KyshePP-TQ9iiLXCQ7AhhFRUx8SsKdHhMTo4cSSUFkdYJCW_uqhXfe62Zh-vq6Bd3eyDtePbnjDeiAm73rvKf4K1BaZPK7iqOzbFpYNl7RckCt6aw2NXJ5y6pDMREilE-xf4xPQqYr19hd6CXYqZ1Y0SZTSxjOPMhHiqqa1nH9w1-Hsmh5HdYs45lrDtM-IH9pCkY8ciStYPXTV8VY66Q9krB5uj9uV8OoTGTm86Ia8gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee25fa2f5.mp4?token=i8J7u_XSevu2mzFYAdIYRLx25QJfeyyFI1BwG_kl2ak7b3tHbCSfWyx8WLh5JwJil-5BY9LSozPnDSJtrGQKidhZ16zu8kKbE6CdlZlx5KyshePP-TQ9iiLXCQ7AhhFRUx8SsKdHhMTo4cSSUFkdYJCW_uqhXfe62Zh-vq6Bd3eyDtePbnjDeiAm73rvKf4K1BaZPK7iqOzbFpYNl7RckCt6aw2NXJ5y6pDMREilE-xf4xPQqYr19hd6CXYqZ1Y0SZTSxjOPMhHiqqa1nH9w1-Hsmh5HdYs45lrDtM-IH9pCkY8ciStYPXTV8VY66Q9krB5uj9uV8OoTGTm86Ia8gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مزدورران رسانه‌ای دشمن در هرمزگان به دام افتادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441499" target="_blank">📅 23:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441498">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85b89f257c.mp4?token=n5dPVKwM6-IdKPYvlqX5bjpro33huofKvN4SETpi1AzUMcgt0Vd3KSyDzfwMa5hSrDSW6sdlfJ6BDQxqISoiQxNjXG5jgJbvuSGxg6wEb2_fuRy0gmzXuivFtV9QJ-kzU-MPrGpsH8yUdTQjAbe0txAr6K5gVIEgN9LEbHCtXp2DhRKXq7ZhSuUs9_Hud5OgRgGvsAxIDYZZHzI1r_FvD8su2ENsVdAN137SSsEO9GaljbtmcntpvlG9b0vxL0sG_7Eh7scMjnsH5oW25tMGnFd_WXnAayEvJQipKFtfzB7359j9mBWE1hElbOFKn7-Ytb2kOxJtnuX2w_eccFsXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85b89f257c.mp4?token=n5dPVKwM6-IdKPYvlqX5bjpro33huofKvN4SETpi1AzUMcgt0Vd3KSyDzfwMa5hSrDSW6sdlfJ6BDQxqISoiQxNjXG5jgJbvuSGxg6wEb2_fuRy0gmzXuivFtV9QJ-kzU-MPrGpsH8yUdTQjAbe0txAr6K5gVIEgN9LEbHCtXp2DhRKXq7ZhSuUs9_Hud5OgRgGvsAxIDYZZHzI1r_FvD8su2ENsVdAN137SSsEO9GaljbtmcntpvlG9b0vxL0sG_7Eh7scMjnsH5oW25tMGnFd_WXnAayEvJQipKFtfzB7359j9mBWE1hElbOFKn7-Ytb2kOxJtnuX2w_eccFsXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوهٔ اتحاد و همدلی مردم مشهد در تجمعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441498" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441497">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_AF3kQH8lDY87HtURjBuVoS9-8VwJAsS8FFFO1avm8gaxcAfNr794ygfRUInHVBm0n6L0KjVhW_Dh-Lye3RnIDvEjsnjsOht-rYpkLi-B1c6zF3BLP0f18pFfOvAix9c0BdetpdIS1gSNjT4vPSen6Lb1IJvDnBYm-j6rGI1LZmzyo2YMGjjeYk-apJaUp5uI-0wROSiXWnMAWU8sb6UEWr3cPdQs41De-4WMF0bETH9p_3NkvDX1015uNWPHdhu1y5E8OEGGGOJ9I8otOaABSkCIb7GjNN9dN6j_sK7Ajl0BwnFIGozugqYud6VeU5XJ3eK8u1ENuV4NobA-33tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین رتبه بندی شبکه های صداوسیما در میزان مخاطب؛ سه، آی‌فیلم ،خبر
🔹
جدیدترین نظرسنجی در خصوص پرمخاطب‌ترین شبکه‌های تلویزیونی  توسط مرکز افکارسنجی متا در سراسر کشور برگزار شد.
🔹
مطابق این نظرسنجی‌ شبکه سه در رتبه اول پربیننده‌ترین شبکه‌های تلویزیونی حضور دارد.
🔹
شبکه‌های آی‌فیلم و خبر نیز با فاصله کمی در جایگاه دوم و سوم قرار دارند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441497" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441496">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8LC_dHgsmAiR0P8CBWDqAcWpBOurWDUsof46n7PeycHYv8dK0yqx0kwUbc9uu5_AkbYBWAE2q3PelxLsh57q2-MYQBcAId4LDw4eMMdnxWmrxNP06RDHPIa3Tjuf74BE_r1jK5j0JoxF-kC7iKuIaDXfS_ZukyHFZh5thzhPHdCN4g76Z7IIqz8pD54Cp9y7b2kC7rvPfR19wqMnA4d-vYmjoXeHXT5oksp7SEegvVJmaXPlWXyeVlZojLOvdJqwypWfR67qJPjjcyf8qStHXlA0I3xcEYtuP7vvVxMHbCriQwzsb97e6-ED713nQfLAddUWNxeA0WuGU1tQL6nZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
جام جهانی ۲۰۲۶ از همین حالا در «همراه من» شروع شده!
برو توی اپلیکیشن *«همراه من»*، بازی‌ها رو پیش‌بینی کن و جوایز هیجان انگیز ببر
🤩
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک  PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
3 کمک هزینه سفر به عتبات عالیات در هر بازی تیم ملی
پیش‌بینی از تو، جوایز میلیاردی از همراه اول!
🔗
https://www.mci.ir/-9VEQ3HH</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441496" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441495">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/441495" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441494">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc58d63ac4.mp4?token=sYFsZHXgbHLR0nc8TR_ODjoUsM3DPYev8YMds649wlBvxYdFZyGFLUI_Xg90QmNhU1LTn-SMngdY3dWdruEdh3hCelOPPgs00kgA3JIsfEtZNQDKHgZwZxm5urYgkKofgsl4Ja_Ctj7YCrfejwFbaqYpmxgNaL9FnI_QtWmA7I9aqQb3LXnyIfGRhit9vjsRU5fQtKRArv6oJL2gqcio-idErRcCusL6hnrhrSGfVQw2OGOiL3MVtfqVIhRxji8oDG0RRTb87lkGDGUC8Jry2x6OMkWAHnOb8HxtsO975kPpLmfuJzSjFBZo1A80s2sJscDmVszhwuVNKlRmv8QsXV1nkvrUQNYKk5UJAI2ICvAjpo1w_ncuDt4zwDb8YCJZ9nFytP4p-fiLTsNKzkIax66Qg89ZjDvQiYTDZk_5i_vXanCTOE92VWSLv1jg-tkjelwnniQFD4lDvoYbVk5xVBp9uooivNNeNO5078ouysCjhfrZxiJEKunTr7-3m0dmzgK5q9vSZ2c-GkIcoGj41DBtPYPFaKbs5DK6yytZL9_sP8xkNC4aN33DtsAB_YzyRDDYYnlwB9SCpoiXtjYiE2fkYXP_PLyg34S4SJge2qs-ZFYgNt0o8ITv6epbZ9UyWRq4PZ-EMPFsStOEkWQOzmwm86zQ9rqWQUB8PI_i1YI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc58d63ac4.mp4?token=sYFsZHXgbHLR0nc8TR_ODjoUsM3DPYev8YMds649wlBvxYdFZyGFLUI_Xg90QmNhU1LTn-SMngdY3dWdruEdh3hCelOPPgs00kgA3JIsfEtZNQDKHgZwZxm5urYgkKofgsl4Ja_Ctj7YCrfejwFbaqYpmxgNaL9FnI_QtWmA7I9aqQb3LXnyIfGRhit9vjsRU5fQtKRArv6oJL2gqcio-idErRcCusL6hnrhrSGfVQw2OGOiL3MVtfqVIhRxji8oDG0RRTb87lkGDGUC8Jry2x6OMkWAHnOb8HxtsO975kPpLmfuJzSjFBZo1A80s2sJscDmVszhwuVNKlRmv8QsXV1nkvrUQNYKk5UJAI2ICvAjpo1w_ncuDt4zwDb8YCJZ9nFytP4p-fiLTsNKzkIax66Qg89ZjDvQiYTDZk_5i_vXanCTOE92VWSLv1jg-tkjelwnniQFD4lDvoYbVk5xVBp9uooivNNeNO5078ouysCjhfrZxiJEKunTr7-3m0dmzgK5q9vSZ2c-GkIcoGj41DBtPYPFaKbs5DK6yytZL9_sP8xkNC4aN33DtsAB_YzyRDDYYnlwB9SCpoiXtjYiE2fkYXP_PLyg34S4SJge2qs-ZFYgNt0o8ITv6epbZ9UyWRq4PZ-EMPFsStOEkWQOzmwm86zQ9rqWQUB8PI_i1YI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بعثت مردم و هنرمندان در خیابان‌های شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441494" target="_blank">📅 23:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441493">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">سریال استعفای وزرای انگلیسی ادامه دارد
🔹
پس از وزیر دفاع، وزیر نیروهای مسلح انگلیس ال کارنز نیز از سِمت خود استعفا داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/441493" target="_blank">📅 23:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
حزب‌الله: پایگاه «نمر الجمل» اسرائیل را که به‌تازگی در جنوب لبنان ایجاد شده بود، با پهپاد هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/441492" target="_blank">📅 23:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4460115fd.mp4?token=qWMG94Qj_SjDu55053-_Gmy5AzZMCBN3Z_plL3FrLTp4GLYj5Juu5zotWlbJot552AwXeKtsSD4VfWW9uM4T8hZSsEKz8wYGyLoM_jBURnTOX4wwL6Yo7M1-08MMO9XtLeATF9VOwDBfwjJ35T3MCflDgtANuREFaRhGGjURDnQk8wrIgXJfmXuaNIxwY_uTsB-ERBPl6zc07xNOy5UPnnFWO43NT48DJ9USU5-z2ygGE0YALzaJFvixQ_mse_mZMaHtTzjguh-Ac6-jxfIla-XkeMjDPsK8BQP34YDxWDyuex5z9vGyRVlUs7Jmov7OvQbsLZXGA6KTNuygut0FLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4460115fd.mp4?token=qWMG94Qj_SjDu55053-_Gmy5AzZMCBN3Z_plL3FrLTp4GLYj5Juu5zotWlbJot552AwXeKtsSD4VfWW9uM4T8hZSsEKz8wYGyLoM_jBURnTOX4wwL6Yo7M1-08MMO9XtLeATF9VOwDBfwjJ35T3MCflDgtANuREFaRhGGjURDnQk8wrIgXJfmXuaNIxwY_uTsB-ERBPl6zc07xNOy5UPnnFWO43NT48DJ9USU5-z2ygGE0YALzaJFvixQ_mse_mZMaHtTzjguh-Ac6-jxfIla-XkeMjDPsK8BQP34YDxWDyuex5z9vGyRVlUs7Jmov7OvQbsLZXGA6KTNuygut0FLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۳ شب از بی‌قراری گنابادی‌ها برای وطن
گذشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/441491" target="_blank">📅 23:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌ تکمیلی: روایت ترامپ از «پذیرش ایران» در برابر واقعیت میدانی
🔹
همزمان با عقب‌نشینی تاکتیکی آمریکا از اضافه‌بندهای جدید به پیش‌نویس توافق، دونالد ترامپ با افزایش لحن تهدیدآمیز در شبکه‌های اجتماعی، تلاش می‌کند روایت «تسلیم ایران در برابر بمباران» را بسازد؛…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/441489" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdpm3Tm1AswYtsW3dBTjUzpcArKVpXG0sVqgerRXANsAOvg9grXZTIgrBD_TerG4MuoenzZJErCFVlV5UHMEM3Ysj5iBjDsWan6YC6kiyB9Vi97OU1j_-lp0HAVoYbOhE7Y0gXVBqJoW_Rw9f5A5at3iuVxSiCjW9dPrRxrR-YHUlclQgALyu5y-qwzd0snixX25Gbhby12c003R9vV0mLMykW5BGWTuXFQiW3Joqf999cvG-Hdiwj3uVBWC3sl23mCx4Nn28kzGtDhjoRkpnukfgHVJDadTqJTr4W832eYz59F8dCruyfrA5g4xplyllG6qo7Ys_xLkEkjz0U1zoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید جنبلاط: صلح با اسرائیل غیر ممکن است
🔹
ولید جنبلاط، از رهبران دروزی و رئیس حزب سوسیالیست ترقی‌خواه لبنان، در گفت‌وگو با الجزیره گفت: «ما امروز با نقشه‌ای جدید از مرزهای اسرائیل روبه‌رو هستیم.»
🔹
وی با ابراز نگرانی از حجم انبوه آوارگان جنگی که از جنوب لبنان به سمت مناطق شمالی فرار کرده‌اند، گفت: «باید حداقل تضمین‌های اجتماعی لازم را برای پناهجویان فراهم کنیم.»
🔹
جنبلاط با اشاره به تحولات منطقه اظهار داشت: «لبنان امروز از آنچه در کشورهای خلیج فارس رخ می‌دهد، جدا و مصون نیست. در شرایط کنونی، دور نگه داشتن لبنان از تحولات و درگیری‌های منطقه‌ای بسیار دشوار است و ما باید واقعیت‌های موجود را بپذیریم، خود را با آن‌ها تطبیق دهیم و مقاومت کنیم.»
🔹
جنبلاط سپس به آمال و آرزوهای برخی در لبنان برای عادی‌سازی روابط با رژیم اسرائیل اشاره کرد و گفت:«هیچ امکانی برای دستیابی به صلح با اسرائیل نمی‌بینم.»
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441488" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlA2uWtgmGF2YN0LBBOsgjeqyMshzJkR21MshkdhMRcWcWzh1Sj7ijXmHrkWPcltCnDFUv9n_yWq-AppvRrA8IOvu1oQ7UVkng25m09Ra-9KcTqtEOIrbr4WmB0rntzQHzL-gHYlb4I6_Zcg7iBoshzViDgl2EZ_vKwpC6HRR6ubCs5eW4eCES1dBPRGwE5hRSocpGGrMIfToVpOaITcExL-pTGuzX02sqwuaymCfyXFDO8aWmm5iZMpWFcTkzfMwzJ8ZUJtp9FPTjSVDsbjP3KkNOigeHrP6ldSI0K6dHTslAxI-mKQSjRqrhFOsnR_64k_HtKedbQ_NRNelNsyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهسته برانید؛ «هلیا» و توله‌هایش از جاده مرگ می‌گذرند
🔹
در حالی که محیط‌بانان حیات‌وحش این روزها چشم به تحرکات هلیا و سه توله‌اش دوخته‌اند، محور عباس‌آباد-میامی بار دیگر به کانون نگرانی دوستداران محیط‌زیست تبدیل شده است.
🔹
این جاده طی سال‌های گذشته بارها…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441487" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c897c20c51.mp4?token=XEos2oWKlif_LYbtEF5MOCpTysfpySfudonGXhlLanEaJZat87CxJNBPhack1R4smBVq2pMi6ZaamoxAyn9gNd5yOGy6pPVGlx0FCZNE5zHtcKoY_Eszdgr3tviZ5DxxC36rNnx1h-mVnblpNPe_oZoc0jVRgru8xy8GJSoMSY-ihHgjzIUR_ODsMcbuhjeBxXrGmdXD14JiqwtX0DY7wJQl-4ClNDQt7TunAxv3v139clw_L46MhHnXUhz5yMW6LiPhvxzAsoIj0On_qi3RtFH_bMxtubhPt9YEavX0vYSvlHkjjq7sI9Ae3e_80UV1uc4GuBSP8Bfj7EI8jb5iaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c897c20c51.mp4?token=XEos2oWKlif_LYbtEF5MOCpTysfpySfudonGXhlLanEaJZat87CxJNBPhack1R4smBVq2pMi6ZaamoxAyn9gNd5yOGy6pPVGlx0FCZNE5zHtcKoY_Eszdgr3tviZ5DxxC36rNnx1h-mVnblpNPe_oZoc0jVRgru8xy8GJSoMSY-ihHgjzIUR_ODsMcbuhjeBxXrGmdXD14JiqwtX0DY7wJQl-4ClNDQt7TunAxv3v139clw_L46MhHnXUhz5yMW6LiPhvxzAsoIj0On_qi3RtFH_bMxtubhPt9YEavX0vYSvlHkjjq7sI9Ae3e_80UV1uc4GuBSP8Bfj7EI8jb5iaIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرثیه‌خوانی امشب محمود کریمی در رواق کشوردوست
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/441486" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441484">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
مراغه در مدار ایستادگی؛ صدوسومین قرار خونخواهی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441484" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441483">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌  منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
🔹
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
🔹
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farsna/441483" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441482">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
عصبانیت وزیر جنگ آمریکا از مقاومت ایرانی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/441482" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441481">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20a7fd97a.mp4?token=ClQPh8d5VLvuqgs-VWkKaHVSV3z7Rjxzk5dIlpUM1NLDB4K16OVgcjLD21E8ozoeSfS0XzTMpiW37sdfV6H0Y3IefD2I-hwtJzzZRFYg-dCeKJYZ577k6F3YKc2PggvUlNZJN-5YLpiuj6H_R5Qpe6sLAd0VDQJpCV3FR8KMrM-Ue9x4Q4LpaBqv9_NtVDmS0q6AEs7MZ22up2CiAWh_DLpMoD6Jy0er4MntLeHhsg0rl_xQXWAUelyyvVElwXwr-JefBrsc9eMz8RvjsWwWYIR6zLECYPY-tfwoCFX7f9Koc8Wu8_gr0MEYBtU31PBO9EFDRf1KjmWchKGd6xKr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20a7fd97a.mp4?token=ClQPh8d5VLvuqgs-VWkKaHVSV3z7Rjxzk5dIlpUM1NLDB4K16OVgcjLD21E8ozoeSfS0XzTMpiW37sdfV6H0Y3IefD2I-hwtJzzZRFYg-dCeKJYZ577k6F3YKc2PggvUlNZJN-5YLpiuj6H_R5Qpe6sLAd0VDQJpCV3FR8KMrM-Ue9x4Q4LpaBqv9_NtVDmS0q6AEs7MZ22up2CiAWh_DLpMoD6Jy0er4MntLeHhsg0rl_xQXWAUelyyvVElwXwr-JefBrsc9eMz8RvjsWwWYIR6zLECYPY-tfwoCFX7f9Koc8Wu8_gr0MEYBtU31PBO9EFDRf1KjmWchKGd6xKr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پرچمی که حذف‌شدنی نیست
پرچم کشورهای راه یافته به جام جهانی وسط زمین قرار گرفت
@Sportfars</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/441481" target="_blank">📅 22:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441480">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da571543ba.mp4?token=sJUyoqPUSvFtrGrF2X62vkoPJ3p8u8BgUUz_dezd1SzezaL_v76wNkCz2IHbhtToSZ1Q_YAm0vSVeoP8ngi5L3u7k757FVUh7Zm0cHhKYR4LoxmVByoOT9pN0gJFIF4PIj-IWSfd1hMw5uT1suHhZJ5Cel3V5C6NdolWbdS-aOUdO5WZhcyETBtb7ENEflBv7E1bF23r0pRzTPxpSxciRGQxbveOEpMUZt8Qs0hVvfw6yMaB7uYulL5tOJePLufcibccPkIW4gQun4JhS-WXkBmrrQg3o1XBhDR_EqcC1So7F7jiU4FLhqD4kQaY1DaJJHkG9CsjPv50MCMp76jH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da571543ba.mp4?token=sJUyoqPUSvFtrGrF2X62vkoPJ3p8u8BgUUz_dezd1SzezaL_v76wNkCz2IHbhtToSZ1Q_YAm0vSVeoP8ngi5L3u7k757FVUh7Zm0cHhKYR4LoxmVByoOT9pN0gJFIF4PIj-IWSfd1hMw5uT1suHhZJ5Cel3V5C6NdolWbdS-aOUdO5WZhcyETBtb7ENEflBv7E1bF23r0pRzTPxpSxciRGQxbveOEpMUZt8Qs0hVvfw6yMaB7uYulL5tOJePLufcibccPkIW4gQun4JhS-WXkBmrrQg3o1XBhDR_EqcC1So7F7jiU4FLhqD4kQaY1DaJJHkG9CsjPv50MCMp76jH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم باغ‌فیض تهران همچنان در میدان ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441480" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHaxjdzuFBSDU3Xb9-zIJKSdUzRMZ9c37er0jjm_d5yCpmUPe395m8r0Vu8NeSNQRrRCjdXOX0hLObXpnNc-c6q3s9W6MuEOLvM23abfmqKf5JbkJZEgfpq0mXfeAlWo55UymOZ8iougGfu6jL_wAoUo4Jxruyb7wuJqx5ohIpZuc6tPQLuUw02jUYk28Ly6_EGE913mqSx8Kuxs66WEIu17_E31ZZd0rfCRiAEgWRLpcg-NWV7YiO2DY7gJJRSucrenZtsSfHWmxqWUgIMsek3y_hIkNsu3Phbrh8fzCl44S3x5SsEDm81O3Cj54I68D_Qv69FuNWJWsB0UT_QRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihWXbj04qSX9FPo-ITDUQKG7xFV7qD6cSh1vEY5BJEGN1WuhxLLyAKe9XOD_OJ4Og9dX2fuKKh6qYYaKb_df9Qya7A3dxxrmLc1eIZ14oI4GWfOoNgjch6hIrG7Ox6l6QKwG2RbAiAI9U_BbZ9s2UwRrZKNbkzMBNHKSgq7W54fKy6Q4kXaPrFMcyD6mPwyH1MNaIDPiBYPTB6vSoiNzc8-CUc9mMomb1y0zDqoWuMZhpzlX6uxaRpDk9A5ZC5NOtqQtNtqDk5DKMK5VNN5dmKe-WsWjKJoIjx2wJOAQiqnyg1A-ex6A7QQ9j4-iOGjil1_R24ZBYdhVcV81ad4ZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDCIfJxo-pj34UzTEigtK2bH9InNHnlt6q7hiNu92yZ6PAmh40b8JP7fWPfEeBqam1pQIZkYbvW_NBxV4tykADFu1N7DLrOwJ3T_pgzHTxidU-7JGxE8IQx6ypGY9HSqT7IRdW1cgX5L1oHzXsoUjozztaULg2Kd5v-Ui1xSTwKObL6vhWOUET9ZxGZ7nOLYNQKixb1t1mGGW5qJgM2Q1abrSHC86R18roefl6Mg8sYr2zUftZGnxBl9-2q9Pjc7s-emB41tbBXCh9Fixl5OA-4FyTAXM7jMo24yLs1fsnimT12Lnl7shJRCt5siyNHY-9F7pD2X7G6QLwONBXdkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOjkTGSzHrTcs7LafW-UDHmnC4kg_fARyxzd3PqEipwJ6R9DwIq5nPz9x2Oef9-0_FwCxUFUj8lbtmgbxZRRAbfmDWOtWjDEJCo-E0ltFCrYoc5--PQMf_Sg2LFRDYRc6zv4x_ktQbgplzYbyd_opek8KIdXiV3Cw2cweRtZbWxsr0roD3_Zwo0QkDGDlLG1r6uFHw4SutlQ5Yngz1F1DbCygdtiGhjAdwPAKdLDbcFtBSUlQQA72J4Ut0Nb0dTGy754yV2s_DIZGu56XgWrkCvEmjUCX-w1kjZDYqAylwkhwOT6Ht3GdL6hB46dcHBdTQxtCk5W9IhTBnB31SMB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZMtIiCO7Hnml0R9tKFd7tI6VZfq_StHJx7L3T5EEqXe4Pr-2vD9nSepaDq9JaH01P2jhvKnCqsGwjoV17wjZ7WyeIXtEjhYCb10FeKyAR_UdJAPNcrtvpO4h5iVpgzUPmkImc7F17C8ofml3J8oc_guSM08W9c01bz5EtjZ0ViTXHbC65SpvItQtfCp26fv0YLJ-MO21lhThYeq7L26zfIxBKuL4HSW8GJekbqfrDuVaQeHKN-MQsUw5zUZFRKgIe-HCqw6PCgDWwr1s7bJQFnVNewjkYnLnQ-VEkSROqcOZ0t7zyfHfA8qAJXUIZBBj8JiD8KTHpfZnyrZrCLIdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماهایی از افتتاحیۀ جام جهانی در ورزشگاه آزتک
@Sportfars</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/441475" target="_blank">📅 22:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نقص فنی دلیل قطعی برق در شهرهای جنوب غرب تهران بود
🔹
شرکت توزیع برق استان تهران: مشکل پیش‌آمده ارتباطی با طرح‌های مدیریت مصرف برق نداشته و ناشی از بروز یک نقص فنی در بخش فوق توزیع بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/441474" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88480d9614.mp4?token=G8BX4WUbjsPT-ClJYvfCLEdkS9moahZLAl_6R8ALWKQcppgWkk5mEVGrK9mDlOWmO_TvQqnC6RCD8KhA0uoElcCvDgQW28BWjJfE_ilPz0p0KdvaoUrfkH9tdYB3JZwu8bPsxIdSKqvmHlnT6qU5EpYOiVJ53RfQpeRPgcQ6noUFGlKKuDAyfAWdCO-WBcC4SefEVKTwlcZemdJIAg6yY8Gotnzr1X7LzG30DWYNwBnKvOsHW13XH9P9PNVvq39zD6hxXPnh32-Xm3O6nVfyXq16Vjl7lRLBlahM2mvcf4t2XvDaoxhF7BF8--yor8QwIRoT5juAw2k-6-8wKY9HiWL-DqTqaFoafZB9DwJJvXg2lPc4Etclzqx9ApxJogoShvSzXUHUNZ3QhTIxJOZHKm0N2xoD_72K5t5-jqR0fMEqlmYe4HI6UdvxPfz13JLmRijP0RU7K7-GsGTyla9rGwrpIZJfWtdVrgJ07dY0Je3MZ-8K590NWkaSo98K2m0WaxUNWKatPOCr33DCOAEipmj0NtBC8SDPzjbO8Wx57D7PwYx-lRJtojBK0wd7XTBmClzXiEH0M2oiAkHQdt6EpX-RyHKtJlxGJeFgVtRM1Rz-roq9s6PO6Q1fy6RVo5e_2wfc3mDhiVqJ1KqNZ5BtkvOQA9FpAp8Ig2_iwtCALOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88480d9614.mp4?token=G8BX4WUbjsPT-ClJYvfCLEdkS9moahZLAl_6R8ALWKQcppgWkk5mEVGrK9mDlOWmO_TvQqnC6RCD8KhA0uoElcCvDgQW28BWjJfE_ilPz0p0KdvaoUrfkH9tdYB3JZwu8bPsxIdSKqvmHlnT6qU5EpYOiVJ53RfQpeRPgcQ6noUFGlKKuDAyfAWdCO-WBcC4SefEVKTwlcZemdJIAg6yY8Gotnzr1X7LzG30DWYNwBnKvOsHW13XH9P9PNVvq39zD6hxXPnh32-Xm3O6nVfyXq16Vjl7lRLBlahM2mvcf4t2XvDaoxhF7BF8--yor8QwIRoT5juAw2k-6-8wKY9HiWL-DqTqaFoafZB9DwJJvXg2lPc4Etclzqx9ApxJogoShvSzXUHUNZ3QhTIxJOZHKm0N2xoD_72K5t5-jqR0fMEqlmYe4HI6UdvxPfz13JLmRijP0RU7K7-GsGTyla9rGwrpIZJfWtdVrgJ07dY0Je3MZ-8K590NWkaSo98K2m0WaxUNWKatPOCr33DCOAEipmj0NtBC8SDPzjbO8Wx57D7PwYx-lRJtojBK0wd7XTBmClzXiEH0M2oiAkHQdt6EpX-RyHKtJlxGJeFgVtRM1Rz-roq9s6PO6Q1fy6RVo5e_2wfc3mDhiVqJ1KqNZ5BtkvOQA9FpAp8Ig2_iwtCALOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر فصل جدید «حسینیه معلی» ویژه ماه محرم ۱۴۰۵ منتشر شد.
حاج سید مجید بنی‌فاطمه، حاج مهدی رسولی، حاج سیدرضا نریمانی، حجت‌الاسلام سیدحسین آقامیری و کربلایی امیر برومند در میز ذاکران این فصل حضور دارند.
🔹
نجم‌الدین شریعتی نیز همچون فصول گذشته اجرای برنامه را برعهده دارد.
📺
«حسینیه معلی» از دوشنبه ۲۵ خرداد از شبکه سه سیما روی آنتن می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/441473" target="_blank">📅 22:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qjwn8YJpwHN7-emuhFyLvAqJ9N8CKfwz2GmlfVdBDAS3gXUBqJzChm2wR-6_57WJVHJI5iY-zZmaJmK50QOj785LXNGqMaptV2Bv6xeLEUryvNL87dxkOsnGn5L9GOgAP4WwmWWCj6EA8wHCJg58fjxWnOaSNVHzEMFPHMR4hg-6EBlWq3euNnbciVOF2kX5YAOGnPuUxFPeNnil6DbkCVvZpqajhnc6sKgGXnSBz-c_7lMwV-6i015bO3xQIUd-_5VU-_0rCHPA0rm3U8Xmy5PALL21rlfPbHwg5W9S7rjmTg8t6-RrQ8t7TvA4OsbM5sub0mZu0TIDsu0N_0G4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور بانک سینا در جمع ۵ بانک برتر کشور برای دومین سال پیاپی
بانک سینا در ارزیابی بانک‌ها و مؤسسات اعتباری از سوی بانک مرکزی در چارچوب شاخص CAMELS، برای دومین سال پیاپی در میان ۵ بانک برتر کشور قرار گرفت.
بر اساس گزارش خبرگزاری وابسته به بانک مرکزی، در ارزیابی انجام‌شده برای شش‌ماهه نخست سال ۱۴۰۴، وضعیت بانک‌ها بر پایه پنج نسبت مالی کلیدی شامل نسبت کفایت سرمایه، نسبت بدهی به حقوق صاحبان سهام، بازده حقوق صاحبان سهام، نسبت کفایت سرمایه لایه یک و نسبت مالکانه مورد بررسی قرار گرفته که بانک سینا در این ارزیابی، برای دومین سال پیاپی در جمع ۵ بانک برتر کشور قرار گرفته است.
این شاخص‌ها از مهم‌ترین معیارهای تحلیل مالی بانک‌ها به شمار می‌روند و در سنجش توان مالی، ساختار سرمایه، سودآوری و میزان ریسک‌پذیری نقش تعیین‌کننده‌ای دارند.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441472" target="_blank">📅 22:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/441471" target="_blank">📅 22:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT6UPJGS1xhYrqXvTCmrFgfHiPG_4xIdCvdqqR_fviYTqwxbPuo_iigcrlwq84u3GFp3t6iui2EFR9FHGkoii4DG9A0eKt1SZ9BGomsZnnxvO_m3OYC4XNCwBdfNo_SBilX_upTio0XqKHQI9JFZySXJXelo-svy1aLDt5hwDvz-PwUHfebe9EJG4IlPLthICJHwVK_kyq1iGM0_wlOzULWfhnems-ImLj3KEUIgI2HCvwpF6sUFnQqPIFqHpt_E5-8N9ugBinoduXJMUdSSPnxTbY2Ud-8ENn3zxVHXOAhzXBhmTcPt_v3nOjYXCi5VrvroSnRCH8IDHMg-WnmiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجاهد: رفت‌وآمدهای میهمانان عرب به تهران به‌خاطر نگرانی از تحولات آینده است
🔹
مهدی مجاهد تحلیلگر مسائل سیاسی: بر اساس اخبار منتشرشده از سوی برخی منابع غیررسمی، در هفته‌های اخیر رفت‌وآمدهایی از سوی برخی کشورهای عربی به تهران انجام شده که به نظر می‌رسد بخشی از آن با هدف انتقال پیام‌ها و ابراز نگرانی نسبت به تحولات احتمالی پیش رو صورت گرفته است.
🔹
به نظر می‌رسد این کشورها نگران آن هستند که در صورت وقوع هرگونه درگیری یا تجاوز علیه جمهوری اسلامی ایران، مبادی و مراکز آغازکننده این اقدامات در منطقه مورد پاسخ قرار گیرند.
نگرانی کشورهای عربی از تبعات هرگونه درگیری با ایران
🔹
جمهوری اسلامی ایران پیش از این نیز به‌صراحت اعلام کرده بود در صورت هرگونه تجاوز، مبادی و پایگاه‌های مبدأ این اقدامات، به‌ویژه پایگاه‌های آمریکایی در منطقه، در چارچوب دفاع مشروع مورد هدف قرار خواهند گرفت.
پایگاه‌های مبدأ تجاوز در تیررس پاسخ ایران
🔹
کشورهای حوزه خلیج فارس در بیش از دو ماه گذشته فرصت کافی برای انجام اقدامات عملی در تعامل با جمهوری اسلامی ایران را داشته‌اند و همچنان نیز این فرصت وجود دارد. اگر اراده‌ای برای اعتمادسازی، کاهش تنش یا ارائه تضمین‌های مؤثر وجود داشته باشد، باید در عمل مشاهده شود و نقدا دریافت کنیم.
وعده‌های غیرنقد مبنای محاسبات دفاعی نیست
🔹
جمهوری اسلامی ایران در ارزیابی روابط و مناسبات منطقه‌ای، بیش از هر چیز به اقدامات عملی توجه دارد. اگر قرار است اقدامی در این زمینه صورت گیرد، باید تا پیش از هرگونه تحول یا بحران احتمالی به مرحله اجرا برسد؛ چراکه در مسائل امنیتی، معیار تصمیم‌گیری اقدامات عینی و ملموس است، نه وعده‌ها و اظهارات.
شرط ایران برای بازنگری در بانک اهداف مشروع
🔹
توقع جمهوری اسلامی ایران از این کشورها کاملاً روشن است. نخست آنکه اجازه ندهند سرزمین، آسمان و ظرفیت‌های نظامی آن‌ها به مبدأ تجاوز علیه ایران تبدیل شود و دوم آنکه خسارت‌های پیشین وارد شده به جمهوری اسلامی ایران را جبران کنند.
🔹
بعد از آنکه آنها به وعده‌های خود عمل کردند، مستحق دریافت امتیاز از جانب جمهوری اسلامی ایران خواهند بود و در آن صورت، خروج این کشورها از بانک اهداف مشروع ایران توسط ما بررسی خواهد شد در غیر این صورت، محدود کردن جغرافیای دفاعی جمهوری اسلامی ایران، خطاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441470" target="_blank">📅 22:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ بار دیگر عقب‌نشینی کرد
🔹
رئیس‌جمهور آمریکا مدعی شد: با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و تأیید شده است، من به عنوان رئیس جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده علیه ایران را امشب…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/441469" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ کدام شرکت‌ها در کشورهای منطقه، شریک اسپیس‌ایکس محسوب می‌شوند؟
🔸
الکام اینترنشنال: شرکت دبی‌محور در حوزه الکترونیک دریایی، از سال ۲۰۲۳ به‌عنوان توزیع‌کننده مجاز تجهیزات استارلینک فعالیت می‌کند و یک مرکز عملیات شبکه استارلینک در دبی برای پشتیبانی از مشتریان…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/441466" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شرکای استارلینک در منطقه، هدف مشروع حملات ایران
🔹
هفته گذشته رویترز در گزارشی به نقل از منابع پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته و سنتکام برای هدایت پهپادهایش از ترمینال‌های استارلینک استفاده کرده است.…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441465" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شرکای استارلینک در منطقه، هدف مشروع حملات ایران
🔹
هفته گذشته رویترز در گزارشی به نقل از منابع پنتاگون افشا کرد استارلینک در جریان تجاوز آمریکا به خاک ایران، با ارتش این کشور همکاری داشته و سنتکام برای هدایت پهپادهایش از ترمینال‌های استارلینک استفاده کرده است.
🔹
پیش از این وزارت جنگ آمریکا نیز قراردادهای چند میلیارد دلاری جدیدی با اسپیس‌ایکس(مالک استارلینک) امضا کرد تا این شرکت در توسعه شبکه ارتباطی ماهواره‌ای جنگی نسل بعدی آمریکا مشارکت کند؛ شبکه‌ای که قرار است سامانه‌های تسلیحاتی، سنسورها و زیرساخت‌های جنگی آمریکا را به‌صورت لحظه‌ای به هم متصل کند.
🔹
این مشارکت گسترده اسپیس‌ایکس در تجاوز نظامی به خاک ایران، سبب شده منافع این شرکت و شرکایش در منطقه، جهت قرار گرفتن در بانک اهداف ایران مورد بررسی قرار گرفته است و نیروهای مسلح ایران می‌توانند به جهت رفع تهدید تجاوز مجدد پهپادها با استفاده از زیرساخت‌های اسپیس ایکس، این شرکت‌ها را مورد هدف قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/441464" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0245725c3.mp4?token=aAxEPTS4A9VnGFLjqO2voqHki8JWekUVfmbf-e39GgfZzaUPU0HRiSFxZkNyz60ODyz3G97-9XSNu3BoXdaEhKd6h0QI3XyF1EghUtgoVmjAJwRum_UjXz2zWvv6-7q1kKeZ_EzP_-IYYcq1zPSGqK9-zvEOr3eWsjHVSSg4c3FmGgtt3qsoS4aXsV8s_WS1LmhmciQZmbMM5DIyi36nUPMXppc4YieKv4TQwzY6hugpFNo4jdPUViOgUvyn79900ALNzRs9MCZ3_ftf9RbYYli56efNgm66sEwgo2SKzja6cUIgDutJSebR9iiXxgxVlnazDJGrmvwMxlt9n8ldDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0245725c3.mp4?token=aAxEPTS4A9VnGFLjqO2voqHki8JWekUVfmbf-e39GgfZzaUPU0HRiSFxZkNyz60ODyz3G97-9XSNu3BoXdaEhKd6h0QI3XyF1EghUtgoVmjAJwRum_UjXz2zWvv6-7q1kKeZ_EzP_-IYYcq1zPSGqK9-zvEOr3eWsjHVSSg4c3FmGgtt3qsoS4aXsV8s_WS1LmhmciQZmbMM5DIyi36nUPMXppc4YieKv4TQwzY6hugpFNo4jdPUViOgUvyn79900ALNzRs9MCZ3_ftf9RbYYli56efNgm66sEwgo2SKzja6cUIgDutJSebR9iiXxgxVlnazDJGrmvwMxlt9n8ldDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج قطار مسافربری از ریل در ترکمنچای با ۸ مصدوم
🔹
قطار مسافربری تبریز ـ مشهد در محدوده ترکمنچای از ریل خارج شد؛ این حادثه تاکنون ۸ مصدوم داشته که ۶ نفر از آن‌ها توسط عوامل اورژانس به مراکز درمانی اعزام شدند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441463" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZEoPug2CoMMHXJOSGB4Xh6B8GQ19oFe03J-4hcT7_v7nZTBzN0oPiqBFPrl3iQPbEkU8S2UtOt7F00iwkEbYyT0pi2ektRPw9Ozz1JGxNgx7vp71Ofq9M1aSPhB1qXPPg3p3aDaXTU1tSUjW5E_tiBFJZena49A159D1ACO8Sqm08In0w_pF0a3FzY2AfV7B58rPzGbAZSBrgFXgdKdd3pReKF0vTG6vfS75zKwTek7fPovOZnBKWCBg9tvM7rvrDI93TwfE1hjBgRehzBKY8-q131SlkmLTE74NNeAkZO9CljeJxGlggILF_ipyVgd5PsaroYoUM1aoEMDeMtXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«صفا با خانواده»؛ بی‌مسئولیت و به دور از ارزش‌های دفاع مقدس ۱۲ روزه
🔹
«صفا با خانواده» سریالی به کارگردانی منوچهر هادی، تهیه‌کنندگی مصطفی تنابنده و نویسندگی بابک کایدان و پدرام کریمی که با محوریت یک خانواده معمولی ایرانی و در بستری از اتفاقات امنیتی و اجتماعی، می‌کوشد هم سرگرم‌کننده باشد و هم حرفی برای گفتن داشته باشد؛ اما در نهایت نه چندان سرگرم‌کننده است و نه حرف درستی برای گفتن دارد.
🔹
متن «صفا با خانواده» از یک ضعف جدی رنج می‌برد: کشدار بودن و پرحرفی بیش از حد. بابک کایدان در مقام نویسنده‌ای که سابقه طولانی در نگارش فیلمنامه‌های محبوب و جذاب دارد، این بار در «صفا با خانواده» عملکرد قابل قبولی نداشته است.
🔹
با وجود تمام ضعف‌های فیلمنامه و کاستی‌های اجرایی، بزرگ‌ترین مشکل «صفا با خانواده» نه به نحوه ساخت آن مربوط می‌شود و نه به کیفیت بازی‌ها و کارگردانی آن. مسئله اصلی به محتوای اثر بازمی‌گردد؛ جایی که سریال در مواردی مرز میان همدلی با مشکلات اقتصادی و توجیه رفتار مجرمانه را مخدوش کرده در برخی موارد زاویه اشتباهی را برای بیان اتفاقات دفاع مقدس ۱۲ روزه انتخاب می‌کند.
🔗
ادامه نقد این اثر را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441462" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ6ykwVu0RMKiiye8fmAQBLRCuPnKXilEFWvJfH1Nqyk9E_f3Qt1Nb1_6yKN3X_ku1DzvPthe2SA0PXw7XopYhFOuozX4z3PSaKyfukbRF_1k16E5ouVg0Xddo_qZ3202iGs6XN6tNwUPyosmVfcFRsRSqcB-yQfTim8WeQi7p5hWOZ44dQEwMzx4eUFQtiQtJvNCw1oWXgQMSqqoNDW4EAAPElQVb8FHjRF-T89wEHVVgklKJEAI34P-shu8UWbVDnZ7xXklIJGF1R0-Zb6vIsM9isFL-zQ4_E4S3iZrWwl7zqPLyhvqMryxx3zYPmpsmL62rg-CrMRQrs8I3BJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فرمانده قرارگاه خاتم الانبیا(ص): اگر آمریکا بار دیگر حملاتی علیه ایران انجام دهد آتش جنگ علاوه بر منطقه، فراگیر و گسترده تر خواهد شد
🔹
آمریکا از یک سو حرف از توافق و مذاکره می زند و از سوی دیگر شرارت می کند و این تناقض آشکار در رفتار و گفتار آمریکا عامل…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/441461" target="_blank">📅 21:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjFM8FaJYHiFqvs94X7SJF9W4Gy7Ga8L_Xij1KSD16tnZ_IzZTXpDMvQPAyw_3mwKd3mGgrpA2VCbeUNeesT42NeEGbG863zggftFMU6EiegC0q1_pGlnEzbVyl8hdP37fOdViC6rzRvR7pI2j5WMtnXNTDQjLFdIraXBhKps8Q9AleQUjKls9-yLwTWdnnW-bdCL7hkdKOwmZeu4NomLhcxFc7M1HkF5zLjFITYbkhouthks7EM2sZCr9M-lzFADIR1zdq5PRmI7KhGnPaVvkgeyy7XnBciLxpZbBW1ZkoRfVuls6L02L1hPD0Q--n1y9D15hPgez9kJmVr1bEntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: با اتکا به خدا و اقتدار نیروهای مسلح، هرگونه تعرض با شکستی قطعی و پشیمان‌کننده مواجه خواهد شد.
🔹
امروز بنیه دفاعی و بازدارندگی ایران، فرسنگ‌ها فراتر از دوران دفاع مقدس سوم و هر مقطع دیگری است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441460" target="_blank">📅 21:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
کارشناس بین‌الملل فرانسوی: همزمان با تشدید تنش‌ها در منطقه، کاخ سفید با نوعی فروپاشی پنهان مواجه شده است و آن چیزی نیست جز افول جایگاه آمریکا در کشورهای کلیدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441459" target="_blank">📅 20:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_DNLHfsrmddFynQr6dXbtIgqU3nzIFNhWum7T3Q5fNSwYtvVa1AXs6VJ2R9YKN1tryXXVvxeYrUT0EJKj-wokHT9Y9hWw8gw_FgXnMtU5tx3TCKRxuOjSt7dDXQXF8u4Ao5BFc1lBLQUYkBZkWgrxevPO1FjRf0SaYqVHDMkTCkPURiecV0R96j6HR1RvRvW9QZBsJhscZHvWgKUoEVjuUp7zBtNJpOYqe0vygypVzjBSZWbF0oEIb1uAY1e8khzHRNCYEHsobnkmxDmvEVaTWOTzA9XBMNTnL0Min_wcqidJHE1_d_q6ArAM_O2o-N28B5xJ2j4gChkxw8yp62oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط بطلان آمار و ارقام بر ادعاهای ترامپ درباره تنگهٔ هرمز
🔹
رئیس‌جمهور آمریکا روز گذشته ادعا کرد که ارتش این کشور در هفته‌های اخیر موفق شده ده‌ها میلیون بشکه نفت را به‌طور مخفیانه از تنگه هرمز عبور دهد و بدین ترتیب مانع از جهش بیشتر قیمت‌های جهانی انرژی شود.
🔹
او گفت در نتیجه عملیاتی مخفیانه بیش از ۱۰۰ میلیون بشکه نفت از تنگه هرمز عبور کرده و بیش از ۲۰۰ کشتی تجاری با امنیت کامل از این گذرگاه راهبردی عبور کرده‌اند.
🔹
با این حال، بررسی داده‌های کشتیرانی، اظهارات مقامات آمریکایی، گزارش‌های رسانه‌ای و داده‌های موجود از ارقامی که ترامپ مطرح کرده از جمله عبور «۱۰۰ میلیون بشکه نفت» حمایت نمی‌کنند.
🔹
پیش از آغاز جنگ، روزانه حدود ۲۰ میلیون بشکه نفت و فرآورده‌های انرژی از تنگه هرمز عبور می‌کرد. بنابراین ۱۰۰ میلیون بشکه معادل تنها پنج روز از حجم عادی انتقال انرژی پیش از جنگ است.
🔹
شبکه الجزیره در گزارشی نوشته چنانچه حجم تردد دریایی پیش از جنگ مبنا قرار گیرد انتقال ۱۰۰ میلیون بشکه نفت به عبور حدود ۷۰۰ کشتی از تنگه هرمز نیاز دارد.
🔹
نشریه تخصصی «لویدز لیست» نیز تعداد کشتی‌های عبوری از زمان آغاز بحران را ۱۴۲ فروند برآورد کرده و شرکت «کپلر» که بالاترین رقم را ارائه داده، از عبور ۲۶۴ کشتی خبر داده است.
🔹
حتی اگر بالاترین برآور مبنا قرار بگیرد با سطح ترافیکی که بتواند انتقال ۱۰۰ میلیون بشکه نفت را توجیه کند فاصله زیادی دارد.
🔗
شرح کامل این گزارش را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/441458" target="_blank">📅 20:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۲.pdf</div>
  <div class="tg-doc-extra">3.3 MB</div>
</div>
<a href="https://t.me/farsna/441456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-61.pdf</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/441456" target="_blank">📅 20:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
قرارگاه خاتم: پاسخ نیروهای مسلح به تجاوز و شرارت‌های آمریکا تداوم خواهد داشت
🔹
توقف حملات آمریکا به مناطقی در جنوب ایران بنابر اعلام رئیس‌جمهور آن کشور، به‌دلیل پاسخ قدرتمند و کوبندۀ نیروهای مسلح جمهوری اسلامی ایران است که در این رابطه شکست دیگری بر ارتش…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/441455" target="_blank">📅 20:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441453">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a60b1aa8a.mp4?token=uWCFeBVSNZJhKTOdUnvRSj-nNp0tzh7Kfy2mRD2wwlh8Hyol0juxue1YXHjFvYOgxtuLSHP1xMVRvTRZnqHyIoRgQU1PKYUoAh5_w0-cBnWcvS3p8Vu8bTbgdLszmClse_0onjgprXvGdwnse6NIxQDye6dZqozyvvoxjJEOJSlqmKzrndMC_EJ0nXR9W3YRDV--DYv1waOoFsItRLHx3SwxWxHiCPQOHfFWVkSngSTTSGarXWgZJUkqt8jm_Jlqqj8MOgYindj5RreoW_6xMsuYf8uuJjAu7ZoFZn1QFO7URnee8AFn1oP3lZbUBrzaj3whriHv-EZ_iuQMHPVmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a60b1aa8a.mp4?token=uWCFeBVSNZJhKTOdUnvRSj-nNp0tzh7Kfy2mRD2wwlh8Hyol0juxue1YXHjFvYOgxtuLSHP1xMVRvTRZnqHyIoRgQU1PKYUoAh5_w0-cBnWcvS3p8Vu8bTbgdLszmClse_0onjgprXvGdwnse6NIxQDye6dZqozyvvoxjJEOJSlqmKzrndMC_EJ0nXR9W3YRDV--DYv1waOoFsItRLHx3SwxWxHiCPQOHfFWVkSngSTTSGarXWgZJUkqt8jm_Jlqqj8MOgYindj5RreoW_6xMsuYf8uuJjAu7ZoFZn1QFO7URnee8AFn1oP3lZbUBrzaj3whriHv-EZ_iuQMHPVmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیفا آزادی‌خواهان هائیتی را از جام بیرون کرد
🔹
جیمی‌جامپ برنامه‌ای که هر روز به حاشیه‌های جام‌جهانی می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/441453" target="_blank">📅 20:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441452">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP5M8qiyE8wOPXdEp2MXSt_92CNrWlhBUWvKOMNG_qriPrpO6P3ijcOAeuIuwLkUluhNCZ2YC7XhL97AVtkRw8c7nK5ZjFKlvihYai_XujBWI1LPuO0S3-Jweybb0QZBM4DUIh7uT87sEO3wAMuTpg6CQ7tnigHWV-43QXDnXCNJrfF4hd5ag9uyE_T5JvQa4uLBUE_rH3aAT1Zk_nwD8nekPv4hh4_pRThjYcMp1dOvQVF8UCGW41XrtLsCUBumKu6pkREN7L1d0aY-xu3e21qLM-2Ftw-tlJFbfpV0hFdRg9Mq4oQFWkawwGyTruRFT720iTeSE38PVr1bVraaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان با سرعت ۱۱۹ کیلومتر بر ساعت زابل را درنوردید
مدیرکل هواشناسی سیستان و بلوچستان: طوفان گردوخاک امروز شهرستان زابل را با سرعت ۱۱۹ کیلومتر بر ساعت درنوردید؛ گردوخاک دید افقی را تا ۲۵۰۰ متر کاهش داد.
عکس: ابوالفضل شهرکی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/441452" target="_blank">📅 20:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441451">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd3378cff.mp4?token=B2RN2v1vCf34ABqi7jl2OnBT2oCnOVWGUZVJQwvwRwucRn-MytSoRToKZ10yrzVZZh9MHYiSlsbCeI3tXUCRYvDuZwzlhMruenG1iTJvmbyLxcG8HjjF5GndVKpSJ0ad_VZiyiubLvY9TWzCBuAltQIAlAFBwaHQVQqrJxSAVJHnkqUmghhX6YNAFWeYZDt6QdhV5Y8Ihli08j2tCtK216MjiN4fNwzhClMM16XMgp1NVY2siF49gxhln06zst1j7C8Bf-F0Y2w_zMBY7btR1vent1iINDwZGZ6FWhY7C0PrJ1D8lBzsKXiRvGe0QF_eKTuoH7y1RYp73dtzi8sjczO3PpNK00LSVwgXS9d7Amc5zlvLwrPYo4bsoByGiba3cQOv25tfTdBjJ-IbAsspGwYbFZz3TNlVN1YhzAIKNWkozoAwFlQkG7xEyLaBmJETqdNv7m7St3bxlPV_HtlwcLEFV4A2_XKCbicYJPnVQyOZ7azzAJ9fq65wdJZPU6s8ZF19rQTaFKTCkIGfVR2WxOnTm4USWj24G8b483qXUy3jtmHE9FGObI1gm6cSUx6Zx4dUTbgrlYCdB8i6yDkbAUu0RnQSz-tH022yGZocvhlHIil8DDrsoWZEibpYoNETaM2rSPu8zN_m25IlZQd8y-aYoMSeLWlrMrpRo_zcx6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd3378cff.mp4?token=B2RN2v1vCf34ABqi7jl2OnBT2oCnOVWGUZVJQwvwRwucRn-MytSoRToKZ10yrzVZZh9MHYiSlsbCeI3tXUCRYvDuZwzlhMruenG1iTJvmbyLxcG8HjjF5GndVKpSJ0ad_VZiyiubLvY9TWzCBuAltQIAlAFBwaHQVQqrJxSAVJHnkqUmghhX6YNAFWeYZDt6QdhV5Y8Ihli08j2tCtK216MjiN4fNwzhClMM16XMgp1NVY2siF49gxhln06zst1j7C8Bf-F0Y2w_zMBY7btR1vent1iINDwZGZ6FWhY7C0PrJ1D8lBzsKXiRvGe0QF_eKTuoH7y1RYp73dtzi8sjczO3PpNK00LSVwgXS9d7Amc5zlvLwrPYo4bsoByGiba3cQOv25tfTdBjJ-IbAsspGwYbFZz3TNlVN1YhzAIKNWkozoAwFlQkG7xEyLaBmJETqdNv7m7St3bxlPV_HtlwcLEFV4A2_XKCbicYJPnVQyOZ7azzAJ9fq65wdJZPU6s8ZF19rQTaFKTCkIGfVR2WxOnTm4USWj24G8b483qXUy3jtmHE9FGObI1gm6cSUx6Zx4dUTbgrlYCdB8i6yDkbAUu0RnQSz-tH022yGZocvhlHIil8DDrsoWZEibpYoNETaM2rSPu8zN_m25IlZQd8y-aYoMSeLWlrMrpRo_zcx6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ وزیر علوم: مجازات قضایی و انتظامی برای کسانی که در دانشگاه پرچم مقدس ایران را آتش زدند
🔹
کسانی که پرچم منحوس پهلوی را در دانشگاه برافراشتند و پرچم مقدس جمهوری اسلامی ایران را آتش زدند، از لحاظ قضایی و انتظامی به پرونده‌شان رسیدگی شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/441451" target="_blank">📅 20:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441450">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lN7JvXtqe5tf7VttI4xqwwSRrOc9owJZcuws8u-gUkyJmS5iv4gdAGfvj2590S9LyV4OxPxA2RFMAg2ScnEtHeky_MLOKmrp7rD7lxqTYI9W1l00kzEr1EijT4iXSsYS5uZwC2o9Dz12eNDa1IqUqZruU_yzhAZFbBT8h5xHAvdJkld7b3Iwh7SkMNDF35-iqQZVW3gRpKQVenT0oteEWKsKBn63JmNbnoukW3FS8EBYJJXJV911-C_MEnfpIfBZeQ5Hyx3-Aw0LszDflHtWBi23bZ68eWWa64obSgsVXhcSd00MIuuxCe2IHUOnSg9tUep7fhsZh1SF-N8bqm_wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم تشییع رهبر شهید انقلاب در خارج از کشور برگزار نمی‌شود
🔹
دبیر ستاد تشییع و وداع با رهبر شهید انقلاب اسلامی: هیچ برنامه‌ای برای برگزاری مراسم تشییع در خارج از کشور وجود ندارد و تمامی تمهیدات در داخل کشور در حال برنامه‌ریزی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/441450" target="_blank">📅 20:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441449">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKWwsWgH_3aevHduS-U36zoMeZm20TYvS-s8whIKRrB34V5LXOTLDoRNlgV4YbjGMBG74EHWT-xMdjseKhdxqJz71ZB6folqWtPQJtG6E0RKSkm4_hsPVj97kaSpU0bBavkr49ujl-8P5OH8dIPyEFJK5Y4zyRU398cDgI5MUr3VVrKNCa3jvzIcx5BcQ4JFDYYFLY33bF5soXc2_aJILdtgZATy4iAIDy4VS5q8guzYjtf2RBJhFHdYSGZ2Xcep08CY4-C9_DOOnMw_xNmEYeweX3EBr6PmkRtOvUx0yaWer4qtIaHCpgmk45iEfpKYYKySnbrl1O0uzFCz_z4oAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: محل استقرار جنگنده‌های آمریکایی منهدم شد
🔹
در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا، برای تنبیه متجاوز صبح امروز با ۱۲ فروند موشک…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/441449" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441448">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_jgd7HkMbKYFAU3Q6CZHZjIN5TcZoNqBcK4nIUblcy4KppT8AQ1gEd_zD5YxWBq6zW7Fn22BgGQD8ptGGQY-D0e-g70WyBqNKcNhIgrg6UGLeiZAARqhiDUfAX6j2gRLBgibny60wX8jLKImSDVTYO84fkjvOZK8xz5CNGS_DisHSUzoZYkz0yPBjqx_R2_oG1qCWOiZF_k6kEHxGAaL4zNgsvQ_6tz4kP_805zFAGwBDYpGDIeGwfn0TaNYXb9H-mnROqyRfbtR5ZmOv4nHTFE3R4EOwMn4NMZN9iEPVZ8omtXSMzC2L9EKiKiex3L4hT6MkXElsyPfELFL16TKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سردار قاآنی: پیروزی نهایی از آن حزب‌الله است
🔹
فرمانده نیروی قدس سپاه: رژیم صهیونیستی باید بداند که اشغالگری، تجاوز و جنایات مستمر علیه مردم جنوب لبنان هرگز اراده ملت مقاوم لبنان و رزمندگان حزب‌الله را در هم نخواهد شکست.
🔹
جنوب لبنان همواره سرزمین عزت، مقاومت و ایستادگی بوده و خواهد ماند.
🔹
حزب‌الله به عنوان نماد مقاومت و عزت امت اسلامی، همچنان در خط مقدم دفاع از لبنان و مقابله با زیاده‌خواهی‌های رژیم اشغالگر باقی خواهد ماند و وعده الهی مبنی بر پیروزی حق بر باطل تحقق خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441448" target="_blank">📅 19:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441447">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkHZjgKrVK7vIZ4jlbJgCEeiuaprO4vEICGlH6LgdPrOLCnD8iVZi1JTr_XoZTrRZiRxdIi6DAC9HKdgsEMjHnmc-N7S495M7uDYECZNWkBgcd0z0e7iRXUUgBGsglEJIIiTXRWK1SuAe27CqumU_PHQwwuKLOl2ZIb0cG2uZwZUiGJOXpwnW_ib5Zt8IY03NAW521q93ik5XBNtgQ91oCAI5ilyf9DrC9agd3BmhI6Upt37SLJddjUVe3fyIIyYpNTIacPxcCgHv16XVPYTqchdU5INZtK7MdIETRJGP3GRQ07UJiVHFSA6fq-hUVpm4bXm8Brz6zzUyRvIdImKQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: تصمیمات بدون فکر، زیرساخت‌های انرژی و بازارها را به انفجار می‌کشاند
🔹
این کارها مردابی بی‌پایان پدید می‌آورد که سال‌ها در آن گرفتار خواهید شد.ایرانی متفاوت خواهید دید! @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441447" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جنگ روایت؛ چگونه ترامپ قیمت نفت را مدیریت می‌کند؟
🔹
در حالی که توجه افکار عمومی به تحرکات نظامی آمریکا در منطقه و آرایش نیروها در خلیج فارس معطوف شده است، کارشناسان معتقدند یکی از مهم‌ترین میدان‌های نبرد میان تهران و واشنگتن نه در دریا و آسمان، بلکه در عرصه روایت‌سازی و جنگ رسانه‌ای جریان دارد؛ عرصه‌ای که می‌تواند بر بازار جهانی انرژی و حتی معادلات اقتصادی کشورها اثر مستقیم بگذارد.
🔹
در هفته‌های اخیر، دونالد ترامپ و برخی مقام‌های آمریکایی بارها ادعاهایی درباره توانایی واشنگتن برای مهار کامل ایران، کنترل تنگه هرمز یا از بین بردن ظرفیت‌های نظامی جمهوری اسلامی مطرح کرده‌اند؛ اظهاراتی که بسیاری از تحلیلگران نظامی آنها را فاقد پشتوانه عملیاتی و بیش از آنکه توصیف واقعیت میدان باشند، بخشی از یک عملیات روانی ارزیابی می‌کنند.
🔹
به گفته ناظران، مخاطب اصلی این پیام‌ها نه نیروهای نظامی ایران و نه حتی افکار عمومی داخلی آمریکا، بلکه معامله‌گران نفت، مدیران صندوق‌های سرمایه‌گذاری، شرکت‌های بیمه دریایی و فعالان بازار انرژی در مراکز مالی جهان هستند. هدف از این روایت‌سازی، القای ثبات و کنترل شرایط از سوی آمریکا و جلوگیری از شکل‌گیری انتظارات افزایشی در بازار نفت عنوان می‌شود.
🔹
برخی کارشناسان رسانه‌ای معتقدند در چنین شرایطی، تمرکز صرف بر پاسخ‌های سیاسی یا واکنش‌های احساسی به شخص ترامپ نمی‌تواند اثرگذاری لازم را داشته باشد. آنچه اهمیت دارد، ارسال پیام‌های دقیق، سریع و معتبر به همان مخاطبانی است که آمریکا در تلاش برای تأثیرگذاری بر آنهاست؛ یعنی بازارهای جهانی و بازیگران اقتصادی بین‌المللی.
🔹
بررسی تجربه بحران‌های پیشین نیز نشان می‌دهد هرگاه خلأ روایت از سوی ایران ایجاد شده، طرف مقابل توانسته تصویر مطلوب خود را در بازارها تثبیت کند. از این رو، همزمان با اقدامات میدانی و دیپلماتیک، حضور فعال در جبهه رسانه‌ای نیز به یک ضرورت راهبردی تبدیل شده است.
🔹
تحلیلگران تأکید می‌کنند دستگاه‌های مسئول باید پس از هر ادعای اثرگذار آمریکایی، در کوتاه‌ترین زمان ممکن روایت جایگزین خود را با ادبیاتی قابل فهم برای بازارهای جهانی منتشر کنند؛ روایتی که بتواند ارزیابی واقعی‌تری از ریسک‌های منطقه‌ای ارائه دهد و مانع از شکل‌گیری برداشت‌های یک‌جانبه شود.
🔹
در این چارچوب، کارشناسان پیشنهاد می‌کنند علاوه بر پاسخ‌گویی سریع، اقدامات رسانه‌ای پیش‌دستانه نیز در دستور کار قرار گیرد؛ به این معنا که ایران صرفاً منتظر ادعاهای جدید واشنگتن نماند و با تولید مستمر روایت‌های معتبر درباره واقعیت‌های میدانی و ظرفیت‌های بازدارندگی خود، ابتکار عمل را در فضای رسانه‌ای به دست گیرد.
🔹
به باور ناظران، نبرد کنونی تنها در عرصه نظامی یا دیپلماتیک جریان ندارد؛ جنگ روایت‌ها به یکی از ارکان اصلی رقابت ایران و آمریکا تبدیل شده است. در چنین شرایطی، غفلت از میدان رسانه می‌تواند بخشی از دستاوردهای میدانی را خنثی کند و برعکس، یک راهبرد رسانه‌ای فعال و هدفمند قادر است هزینه‌های عملیات روانی طرف مقابل را افزایش دهد.
🔹
یک کارشناس حوزه رسانه و انرژی در این باره می‌گوید: «مخاطب اصلی پیام‌های ایران نباید صرفاً ترامپ باشد. مخاطب واقعی، بازارهای جهانی، بورس‌های انرژی، شرکت‌های کشتیرانی و سرمایه‌گذاران بین‌المللی هستند. هرچه این پیام‌ها سریع‌تر، دقیق‌تر و حرفه‌ای‌تر منتقل شوند، اثرگذاری عملیات روانی آمریکا کاهش خواهد یافت.»
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/441445" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پنتاگون در وضعیت قرنطینه قرار گرفت
🔹
رسانه‌ها از قرنطینه پنتاگون و تخلیه طبقات آن خبر می‌دهند.
🔹
سی‌ان‌ان گزارش داد که تیم‌های مقابله با مواد خطرناک پنتاگون اعزام شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/441444" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8559da74.mp4?token=NfvNz4pwLbV8Pb6JZ8hQHz2sphqR3v-GP_V27YCY37ceVlMruAXulR1LfUnOZKVHbaZYrfNiCwgJ1abh7Yowk4nGD_4Pesxvc0XLK9jINWeHMpXVy9B_x4AZdR9ZhBJw9lqoLhwfO3wzIff15h61uuJeEYoO9J20J1N7TEQbpOEAs1i2DBE_vC35avjVLOUuBqiGfOfKZpCoMmc3Z-qq0HY1qcyMz7VhHoKbg0Hv9hCYifxobGt9uW3w2JzE2wpXhf95JYPpSk7LnuPYh7va5xU_rgcYPOhMuwKFDs5wv6RPzq9Bhj0QroGGnEljx9Sli9h7Op1AeO7s1UkhtXA10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8559da74.mp4?token=NfvNz4pwLbV8Pb6JZ8hQHz2sphqR3v-GP_V27YCY37ceVlMruAXulR1LfUnOZKVHbaZYrfNiCwgJ1abh7Yowk4nGD_4Pesxvc0XLK9jINWeHMpXVy9B_x4AZdR9ZhBJw9lqoLhwfO3wzIff15h61uuJeEYoO9J20J1N7TEQbpOEAs1i2DBE_vC35avjVLOUuBqiGfOfKZpCoMmc3Z-qq0HY1qcyMz7VhHoKbg0Hv9hCYifxobGt9uW3w2JzE2wpXhf95JYPpSk7LnuPYh7va5xU_rgcYPOhMuwKFDs5wv6RPzq9Bhj0QroGGnEljx9Sli9h7Op1AeO7s1UkhtXA10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ هوایی شدید رژیم صهیونیستی به شهر النبطیه در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/441443" target="_blank">📅 19:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa82a40ab.mp4?token=eFcRwabjVcD3BE5ybBXDzoDWtk355bEExmMKEj2_ddZ0k9VG3dBbKAj3b9Kkmq1-0rxazaWq9JXIc7pF2qiBgqQRFJMsBnqd1eCtlA55wlQS2F7MJzok2OdruyMyz0KrYsx0vHK0cGJmkSLzY3Ep1Rrv4Ze7XQOlMpRRYYuIe3IZWSV6Px9B-dDGl-74UxcP_vXojQGHaev-_s2rxn0ZmJUM2Sik8gGNLqQJM11XoHgxjn47mRkEprJQjxDpnflaPDt6FabBEmNb61ZPq5eq_BqtcoSlgxahd7wtcLs6cvPOxwCy9P_Ngdr_DvmGGntM_rPRGDWgFNQWf908k3RsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa82a40ab.mp4?token=eFcRwabjVcD3BE5ybBXDzoDWtk355bEExmMKEj2_ddZ0k9VG3dBbKAj3b9Kkmq1-0rxazaWq9JXIc7pF2qiBgqQRFJMsBnqd1eCtlA55wlQS2F7MJzok2OdruyMyz0KrYsx0vHK0cGJmkSLzY3Ep1Rrv4Ze7XQOlMpRRYYuIe3IZWSV6Px9B-dDGl-74UxcP_vXojQGHaev-_s2rxn0ZmJUM2Sik8gGNLqQJM11XoHgxjn47mRkEprJQjxDpnflaPDt6FabBEmNb61ZPq5eq_BqtcoSlgxahd7wtcLs6cvPOxwCy9P_Ngdr_DvmGGntM_rPRGDWgFNQWf908k3RsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش سردار رادان به تهدیدهای ترامپ
🔹
رزمندگان بلدند زبان تهدید را چگونه پاسخ دهند، تا جایی که [دشمنان] مقابل ایران سر تعظیم خم کنند
.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/441442" target="_blank">📅 19:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrQoBTjQS3McmoFeRrFJ_boH_zLxYHPqeJ4L6QhtDJpk0QdLoR0KECeHyU6X9O_ohhkEiSDPmDPuiZH_72sm1qmaQfT1bgJ-ZOIVqGLBA4RLmlbUxqp8gHQsrqZTGoobQpG6aWFyR_V8F0Ee04vbvuaSKa6-CG5Ag5bCyLutJx5hPO2ULGL_x-UkNabiOXWkMGWTgLvcVa3Q1rGAItNoDCXdHq_WripPfqVkv1W5yZ1Tz8MFBBzZFsGbnAkdgHhTfS2F4U4AghMa5nUJKWyQoPL8ztHsB_VxvkNJIHi51VC1AhO_4J0AZkvjOto9mAM7okXJ1j-iCkesM5-DGYnCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر موضع ترامپ دربارۀ کنترل بر جزیرهٔ خارک
🔹
ترجیح می‌دهم جزیرۀ خارک را تصرف کنم، اما مطمئن نیستم که تمایلی به انجام این کار داشته باشیم.
🔹
موضوع ایران تمام شده و ما می‌توانیم فردا نیروهای خود را بیاوریم، اما نمی‌خواهم نیروی زمینی اعزام کنم!  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/441441" target="_blank">📅 19:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ukl20IhzRwBh2ubt4b5pEVTnz3bqnyI3N1sLbjQnWuftB75mh5sdJ61M3BqJ5cLUmAT1t75aLiQ3M3P1JvytqMQqfUleofN9LRyTbVbXBXNXFaSMxTVRl9OuDqLqNJ2A_lXhQ__41c8DPF7ycTFeTZPzZqwmip8FSzOU3DS2Nwq15-DtRpSUesXgiTdJR5xpckcQO3BQodswPJhEvfTtsURRShoP2LO3Ezwx2odT9fKReyyplhebrkI_DY40f5ydcawZEmxPYnD4AKEC8o4jdya07Z3si_clmdGzZFzNkknoT2p_0r2s9vwGPyUF7R552q84fToYBQmYTE585v-m8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برشی از مستند «آن یک واقعیت است»
🔹
این مستند، گوشه‌هایی از منش، اخلاص، صمیمیت و نگاه رسانه‌ای شهید سلامی را به تصویر می‌کشد که به کارگردانی سجاد سلیمانخانی و تهیه‌کنندگی مرتضی کارآموزیان تولید شده.
📺
زمان پخش: جمعه ۲۳ خرداد حوالی ساعت ۲۱ از شبکه مستند سیما
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/441440" target="_blank">📅 19:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=mSBtwuIgH_FhJErI41nsAqZmtVmpKheGjt4qPcIAnw1NWNVYa5mJp4l-EBkva15Z8FkLr5AwvjXq_ZsVGlPUjUupMN24xLM3SK1W26z8Kp-vRM6_VqOyXDy8lHitRKPTKeilAFmfT0pPr9baDVDP2cBDcBLYWPsMjcMiZZycDAuNXP0MTHNShPhWHL6qbRIQ2ghCjDYAk-oaIr5-T_zvNOLfkTP6UssikPeKLozNCnEwEWppT8FGy6l-nYufYJ_77MyZIUSRwQLNpLsLaFYV3gRf97haq5WNLpiQNDRCh_EpUdKlh5d7cm9I2PHxjFxFs4zex3Kc3_fyTVUX6mjZzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=mSBtwuIgH_FhJErI41nsAqZmtVmpKheGjt4qPcIAnw1NWNVYa5mJp4l-EBkva15Z8FkLr5AwvjXq_ZsVGlPUjUupMN24xLM3SK1W26z8Kp-vRM6_VqOyXDy8lHitRKPTKeilAFmfT0pPr9baDVDP2cBDcBLYWPsMjcMiZZycDAuNXP0MTHNShPhWHL6qbRIQ2ghCjDYAk-oaIr5-T_zvNOLfkTP6UssikPeKLozNCnEwEWppT8FGy6l-nYufYJ_77MyZIUSRwQLNpLsLaFYV3gRf97haq5WNLpiQNDRCh_EpUdKlh5d7cm9I2PHxjFxFs4zex3Kc3_fyTVUX6mjZzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
⚽️
جام جهانی شروع شد؛ وقتشه ردبانکی شی!
❤️‍🔥
اپلیکیشن ردبانک رو نصب کن و با افتتاح حساب، ۱۰۰ هزار تومان هدیه بگیر.
🎁
👥
هر دوستی که دعوت کنی = ۱۰۰ هزار تومان جایزه بیشتر!
🏆
تیم ۱۱ نفره خودتو بساز و بیش از ۱ میلیون تومان هدیه ببر.
⏳
فرصت محدوده!
✉️
عدد ۶ را به 7007666 پیامک کن
📱
یا #6666* را شماره‌گیری کن.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/441439" target="_blank">📅 19:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocOtKelDniOXFCJLoHH0ED3mrdzUHoXNacChJEttcy1QVn5nYxxhAV5lRjY5GBz0E2ScNcYAlKha9jCRzmdRqTSv6mKpoAnCL5DUAjM5ZcA569uQSZGAEfUF-SMUGMbVQCGPyEbc8HepsfmgKpoqTcf0WBgLYu87KTfwIzw4rw00HQ8a4ZIO79W2jGlgFXAsNzOCg2p8RFX2bnIsuwIF0OChzbq7tIC255o2Ykt2ahkim4yAolK8Wp55KzFeqrbnTvmq19q2-GUQa3hGhjHXfnOq48Wo3Vb6TgJpTVeObgXw9ZdYxGtYtsW6RsHBhHl4uwly27kPY2NJykhXjKCuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
گزارش گروه بین‌المللی مطالعات مس می‌گوید؛
🔰
کاهش چشم‌انداز تولید جهانی مس در ۲۰۲۶/ بازار در سایه محدودیت معادن و ریسک‌های ژئوپلیتیکی
🔻
گروه بین‌المللی مطالعات مس (ICSG) با بازنگری در چشم‌انداز بازار جهانی مس، پیش‌بینی رشد تولید معدنی این فلز در سال ۲۰۲۶ را از ۲.۳درصد به ۱.۶درصد کاهش داد؛ موضوعی که عمدتاً ناشی از محدودیت‌های تولید در برخی معادن بزرگ جهان و تداوم آثار حوادث عملیاتی در سال ۲۰۲۵ است.
🔹
براساس تازه‌ترین گزارش ICSG، کاهش برآورد رشد تولید به افت چشم‌انداز تولید در جمهوری دموکراتیک کنگو، شیلی و اندونزی مربوط می‌شود. همچنین معادن بزرگی مانند گرسبرگ و کاموا همچنان با محدودیت‌های ناشی از حوادث سال گذشته روبه‌رو هستند.
🔹
با وجود این، این نهاد بین‌المللی پیش‌بینی کرده است تولید معدنی مس جهان در سال ۲۰۲۷ بار دیگر با رشد ۲.۳درصدی همراه شود؛ رشدی که به توسعه ظرفیت‌ها در مغولستان، چین، ازبکستان و روسیه و همچنین بهبود عملکرد برخی معادن بزرگ نسبت داده شده است.
ادامه خبر در پایگاه خبری مس‌پرس
👇
https://mespress.ir/x6R3
@mespress_ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441438" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/441437" target="_blank">📅 19:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/441436" target="_blank">📅 19:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmeOhoRTUW1b_xUsu5NPuQhfdWhjlpNl4_WTbYC6TEi8d9eQnmHRTsBpyrAKy3WwV4P5iMIGcwjsXh0D0sg6_-UgJoiW0WIThfb4iGhGCkf0xxm5s0T5TOp2qP7ojbzxcu6B3LC7_Tc4dBfGVcuP279nnHJWHvWNIEeOhRbkrKGuubL5TQ7tZlcNMlkeNsCINV6zroHVMnc2Nx8EzyfAkjN6hVxMEZPTQZ3-tlqWv3VF5xX3LJd3Jz-4xiwLM0gumKFzKDFCMbOsyrvlwdSB_KtMbgXn31iSuRjdiZJmzWtregWBTFVBaLGhjatXly7ptUJQl2RkSXLQhCP8Krwf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون در وضعیت قرنطینه قرار گرفت
🔹
رسانه‌ها از قرنطینه پنتاگون و تخلیه طبقات آن خبر می‌دهند.
🔹
سی‌ان‌ان گزارش داد که تیم‌های مقابله با مواد خطرناک پنتاگون اعزام شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/441435" target="_blank">📅 18:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c4af4dfb.mp4?token=I_04__VsvJ73b-k-AANxSrNOCWET0vguPCiGaX01gr8ufeUhG0dBtJiReGIi47rPCom_CCsZimuTJ5DpCLeWeyqmFnJaZeVR4HQW4RLVkWp1ExEVKXOQ27P5f94hM5KJBSgrGFwpTza0SZsIbQ1x0HkRZ6ndV9hMKMLotPyo--4o0VjHF5JPH8wW5MUCUNm3cD__PF5GVEwn6jOLEXw1MJPUKyn81bh8hPBKwSvdvU1m22nE8R59ISL36NHLhn40mQ3EWwZkCcud2np35PukVDZRIGOXAY6eOlOnBoXbj-CofgU5x3vl-cYY3NqrKsJEuVlsrjIBK0ohT-Kn-8i0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c4af4dfb.mp4?token=I_04__VsvJ73b-k-AANxSrNOCWET0vguPCiGaX01gr8ufeUhG0dBtJiReGIi47rPCom_CCsZimuTJ5DpCLeWeyqmFnJaZeVR4HQW4RLVkWp1ExEVKXOQ27P5f94hM5KJBSgrGFwpTza0SZsIbQ1x0HkRZ6ndV9hMKMLotPyo--4o0VjHF5JPH8wW5MUCUNm3cD__PF5GVEwn6jOLEXw1MJPUKyn81bh8hPBKwSvdvU1m22nE8R59ISL36NHLhn40mQ3EWwZkCcud2np35PukVDZRIGOXAY6eOlOnBoXbj-CofgU5x3vl-cYY3NqrKsJEuVlsrjIBK0ohT-Kn-8i0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سردار معروفی معاون فرهنگی سپاه در مراسم گرامیداشت سالگرد شهید سپهبد محمد باقری  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/441434" target="_blank">📅 18:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e475b32.mp4?token=NXAYFRAdfGl03KNOOvFLu8zaeH6DC3QdwU0qKHBrNuA3UFHgFHd0Si5BH_MtxnzBfbKY00x9iuRCPhlXNEAwV5aNWDaTdmXbQxmWnCFpxxrpJOomKGL0yHVww0aktoIYX4F9GXzc1mlWVMSbVqxoknx3sN99kcgrdZoaelZwmC2Efy8YLzp6R2xZLwTpDvBee8PnM5lDV52RH6lnQCIZQ8CuTHEt8DxhVVeRh7-dxQ_kKZYr5LuXD0MI4MfSTVnIFWMwc7IDPW5YuuSArT1XEaKHW4hEBMK07Ad3_dtQrOT31HHrzWUkxvZN8r9lIJHo5Qw9GOjeX8SW080D2He4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e475b32.mp4?token=NXAYFRAdfGl03KNOOvFLu8zaeH6DC3QdwU0qKHBrNuA3UFHgFHd0Si5BH_MtxnzBfbKY00x9iuRCPhlXNEAwV5aNWDaTdmXbQxmWnCFpxxrpJOomKGL0yHVww0aktoIYX4F9GXzc1mlWVMSbVqxoknx3sN99kcgrdZoaelZwmC2Efy8YLzp6R2xZLwTpDvBee8PnM5lDV52RH6lnQCIZQ8CuTHEt8DxhVVeRh7-dxQ_kKZYr5LuXD0MI4MfSTVnIFWMwc7IDPW5YuuSArT1XEaKHW4hEBMK07Ad3_dtQrOT31HHrzWUkxvZN8r9lIJHo5Qw9GOjeX8SW080D2He4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف قرار گرفتن سربازان اسرائیلی توسط مقاومت
🔹
تصاویری از عملیات هدف قرار دادن سربازان ارتش تروریست اسرائیلی در شهر خیام، جنوب لبنان، با هلیکوپتر تهاجمی ابابیل توسط سربازان مقاومت.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/441433" target="_blank">📅 18:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be371a0dc9.mp4?token=itY7iiIsUNYREb58yt3wuRZvgQZ_h5BN17_d2t6nQt5RfliXCxXisOlKiZ6xf0ECr_jOCD_iLognJTXsHctiUkHjS1GrAuCsaT8ynPwP1d3pKsbMzdfoQ49reWwAShvAd4yjkKoAfGquKZNHVGQ7yOwt3Rn6nq7anTY52EU1O1C85G_F6fFm8qgEDHrd-yM1M1XEraeeaq7lwwYsRWHrDPQkEUebd6-hVVK7V0h4CY1B7nkcR4qnoxrWay54j1Bq_Rm_dp9mtAnit2XXJIozp4RcyLPtaMswtdYa8Tj1SmFtjZ2xEfpZeWvX_2ueTQsOGQf9DEinPX0NnkTf_wPzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be371a0dc9.mp4?token=itY7iiIsUNYREb58yt3wuRZvgQZ_h5BN17_d2t6nQt5RfliXCxXisOlKiZ6xf0ECr_jOCD_iLognJTXsHctiUkHjS1GrAuCsaT8ynPwP1d3pKsbMzdfoQ49reWwAShvAd4yjkKoAfGquKZNHVGQ7yOwt3Rn6nq7anTY52EU1O1C85G_F6fFm8qgEDHrd-yM1M1XEraeeaq7lwwYsRWHrDPQkEUebd6-hVVK7V0h4CY1B7nkcR4qnoxrWay54j1Bq_Rm_dp9mtAnit2XXJIozp4RcyLPtaMswtdYa8Tj1SmFtjZ2xEfpZeWvX_2ueTQsOGQf9DEinPX0NnkTf_wPzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت ۲ پهپاد انتحاری به مقر تروریست‌های تجزیه‌طلب در شمال عراق
🔹
منابع عراقی از اصابت دو پهپاد انتحاری شاهد ۱۳۶ به یک انبار تروریست‌های تجزیه‌طلب کُرد در منطقه «قوش تپه» واقع در شمال اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/441432" target="_blank">📅 18:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7ebf4797.mp4?token=KdLlpeFpq6vOznQGRIEQKmIMtCJYwmrv9ilTdsH1Fn8JG_nQo-vzL8-ZgIVFv_oMN48ak5MoTyZAiVN26AnFbL7nBgSVrGmzR6zikq_dyP93GC3jKmgV4m6hdqggkxuQOq1X-qZ10TfL2YC7VuNkxXSgIos-CmZTsuCMIvRymLuV29Hj9zzQBwpc5lZR-A4DUDiL5MWBlbZ1MVGsABPmpY3mvfxlK3a9WpRH413fYFGT4oVRDDobFH5cym_Bhy25SPZsnLEaIwCk6WFvuvbe6XOZcYGkQsYslPiwOb1G5W1Rsb43CQtoFHu0x_zNW715TO6gAlbtdzTkeQKpi2oqJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7ebf4797.mp4?token=KdLlpeFpq6vOznQGRIEQKmIMtCJYwmrv9ilTdsH1Fn8JG_nQo-vzL8-ZgIVFv_oMN48ak5MoTyZAiVN26AnFbL7nBgSVrGmzR6zikq_dyP93GC3jKmgV4m6hdqggkxuQOq1X-qZ10TfL2YC7VuNkxXSgIos-CmZTsuCMIvRymLuV29Hj9zzQBwpc5lZR-A4DUDiL5MWBlbZ1MVGsABPmpY3mvfxlK3a9WpRH413fYFGT4oVRDDobFH5cym_Bhy25SPZsnLEaIwCk6WFvuvbe6XOZcYGkQsYslPiwOb1G5W1Rsb43CQtoFHu0x_zNW715TO6gAlbtdzTkeQKpi2oqJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین سالگرد شهادت سربازان سیدعلی، شهیدان حاجی‌زاده و محمود باقری
🗓
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۹، قطعه ۵۰ گلزار شهدای بهشت زهرا @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/441431" target="_blank">📅 18:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d03711bfa3.mp4?token=JoAD7o1ug0iykHmatIomiNONfKj9mgwdQh9Po0OpEttLZPyvZr5P3yWR81oOxvGwZz6ZHVzkhyZQckJTuS_mWV7VWJu7nNqWSOTX_AI-s--RlwPX0qdHsgxpWDwO-VD_kaw2Xa7rGIiBEwYOUELet7nSlzR24BF_4tbHPaNsG2ZfDufAa4DAJC2Voj7RTWOICu7Hnn4T-FDwny5Zydg8jge2R97pcitiMSOB-qEBwiY3M1DEcNogX6sRHIkH2LbqIZqRG2KR2-nTc4kTHQ2e4DIgzbvXv12Di8KtvWt00YE0ONIJlXu0Gl5Ro_Tp_a7rlHOAJBOrqEHIpF3RvrNBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d03711bfa3.mp4?token=JoAD7o1ug0iykHmatIomiNONfKj9mgwdQh9Po0OpEttLZPyvZr5P3yWR81oOxvGwZz6ZHVzkhyZQckJTuS_mWV7VWJu7nNqWSOTX_AI-s--RlwPX0qdHsgxpWDwO-VD_kaw2Xa7rGIiBEwYOUELet7nSlzR24BF_4tbHPaNsG2ZfDufAa4DAJC2Voj7RTWOICu7Hnn4T-FDwny5Zydg8jge2R97pcitiMSOB-qEBwiY3M1DEcNogX6sRHIkH2LbqIZqRG2KR2-nTc4kTHQ2e4DIgzbvXv12Di8KtvWt00YE0ONIJlXu0Gl5Ro_Tp_a7rlHOAJBOrqEHIpF3RvrNBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
مراسم سالگرد شهید سپهبد محمد باقری و همسر و دختر شهیدش
🔸
پنجشنبه ۲۱ خرداد، ساعت ۱۷ الی ۱۸:۳۰
🔸
مسجد امام صادق (ع) واقع در میدان فلسطین @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/441430" target="_blank">📅 18:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a412b1ff3.mp4?token=X6QO6ieFB0rk37TLoNxPeFbtnVJTHT6JtiicXyyGYOwJRAs4a-7uWr8TTZ8R51uTEW5SWZy_KHrhKgbpgp7vxWM0qtgRLSk-jmnSZ6YaiFFvwcuniTmJ_QlxwXueCKtEMpFomMwp8im4A2ZSL4-Dwq30Rkr6GPSNauiJ_RZyDxjF4xT5JhHSiRV624Ge6jynWafnrD36QwO4bdP4w3SOdrDqNi6-_q-8Y_9Iv76ESdMPbS0DDlUq2XmUrM1tk14V656_bj8056UrF5rH2lBREMTHnSIl4XJadQeBxKb2UbkQDe7WaD8aGfjziFVRBr6okKIXWLZhLOA1BFaxwI6uAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a412b1ff3.mp4?token=X6QO6ieFB0rk37TLoNxPeFbtnVJTHT6JtiicXyyGYOwJRAs4a-7uWr8TTZ8R51uTEW5SWZy_KHrhKgbpgp7vxWM0qtgRLSk-jmnSZ6YaiFFvwcuniTmJ_QlxwXueCKtEMpFomMwp8im4A2ZSL4-Dwq30Rkr6GPSNauiJ_RZyDxjF4xT5JhHSiRV624Ge6jynWafnrD36QwO4bdP4w3SOdrDqNi6-_q-8Y_9Iv76ESdMPbS0DDlUq2XmUrM1tk14V656_bj8056UrF5rH2lBREMTHnSIl4XJadQeBxKb2UbkQDe7WaD8aGfjziFVRBr6okKIXWLZhLOA1BFaxwI6uAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله یک پهپاد جاسوسی اسرائیل را ساقط کرد
🔹
حزب‌الله لبنان اعلام کرد که با یک موشک ویژه یک فروند پهپاد جاسوسی «هرون ۱» ارتش اسرائیل را در آسمان منطقه «نحله» در منطقه بقاع (شرق لبنان) ساقط کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/441429" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454bfe434.mp4?token=PeGUHYdEkFz8TcO2rE0ZfpTwXCm_nv9gP3yVF5NDQvN_AFaOS4UkhzMPooR7cf8pAr54i1XtVMNF9DAeU52OzA3cuw0fOP6KWATDst9xq5gMAlnM49ekKi1q7MVuc7tHUeEEiTN8LX-Gt-2E_YiJQZalpuXMOEnBshREXPTVLwkFAonpS9tdJr0s4197FaUJFM4-rdUswMNHp8fNkwfklohEjuvLWmTE1-YnuaFHDOuIXwONollFRVM14mK75ueI7Jzqq7uZmiWEqwe3mt7POrd493sWcBO-cKCKArzh34SqXVVzx12q2roXuQ2WQGg2eJcYH9KjUS-NFJVyFBM56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454bfe434.mp4?token=PeGUHYdEkFz8TcO2rE0ZfpTwXCm_nv9gP3yVF5NDQvN_AFaOS4UkhzMPooR7cf8pAr54i1XtVMNF9DAeU52OzA3cuw0fOP6KWATDst9xq5gMAlnM49ekKi1q7MVuc7tHUeEEiTN8LX-Gt-2E_YiJQZalpuXMOEnBshREXPTVLwkFAonpS9tdJr0s4197FaUJFM4-rdUswMNHp8fNkwfklohEjuvLWmTE1-YnuaFHDOuIXwONollFRVM14mK75ueI7Jzqq7uZmiWEqwe3mt7POrd493sWcBO-cKCKArzh34SqXVVzx12q2roXuQ2WQGg2eJcYH9KjUS-NFJVyFBM56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج وطن‌فروشی مزدک میرزایی
🔹
کارشناس شبکه اسرائیلی اینترنشنال: اگر تیم ایران بازی اولو ببرن شانس زیادی برای صعود دارن و واقعا دیگه نمیشه جمعشون کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/441428" target="_blank">📅 17:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
واکنش رئیس کمیسیون امنیت مجلس به اظهارات امروز ترامپ
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/441427" target="_blank">📅 17:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441426">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnqjVB2MiEcklZ5oK_LO8TBe1Okg9xZM_IhaA9by7LB0NONrphhDcTMHxb8pcewGVHyxmJrknRcjjGpbNB0ls38AF3Ng3IuXvU0tZIC6WJzFERR9dhDIJ_ghpelqwpsTlEhpvyBEW6rpO3zwxZrymDC9oCdkSNdY-6I7g8kS_gKj9WOviAXNQpGM2GbMwajS7xtg7bUwomRUh5eRclAHgbTssYHysxlDhSEMK8m3Q7ta625epTZW86IpBTku5dmooFVabMxLn-DBr8q---5IxJOnD8BUTKur7_ZH3rT7SRba7sfbEMyy5XjKrQqq4KGSQClaQzs-2TdliLShVpT52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ترجیح می‌دهیم خارک را در اختیار داشته باشیم
🔹
من از ایران دلسرد نشده‌ام. این توافق خوب است و ممکن است بزرگ‌ترین توافق تاریخ باشد.
🔹
ترجیح می‌دهم کنترل جزیره خارک را در اختیار داشته باشیم. ما هنوز به اندازه کافی به ایران حمله نکرده‌ایم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/441426" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bok75Z7dOFi7CEtdQB6KZWdRFgTNZ3qbJ6c5dHuX3afzxqjasG97XrftoQzoq_3gcvAYjfFpugAGQk0nhpI0rlDr0C-Dt-kMmCU3FP9yGKevxxuSz-Xh18-z0cF8afmmf8SjF6SoIJusRVoQbe4SlOsf3JkutY3NW9ZLuPP88-6KCaronxQWXejT8fzIrFvypfmCaVLc-hhoRuM1HZY43e7Icki6SItEkKFcXdpU8tDW1fxbLE84WmM8WOqI56W1mETSh6ohZMMvtVFOaFgr83LekK-yws4P2-D-fDBLPOi-pkPhY9yvYf202-C_UMhzYzopa-bIGfJvrHRKy4XVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه‌گویی وزیر خزانه‌داری آمریکا دربارۀ پول‌های بلوکه‌شدۀ ایران
🔹
بسنت: هر خسارتی که ایران به متحدان ما در خلیج فارس وارد کند، از محل وجوهی که از حساب‌های ایران برداشت می‌شود، جبران خواهد شد.
🔹
هر عوارضی که به نهاد مدیریت آبراه خلیج فارس پرداخت شود، با برداشت وجوه از حساب‌های آنها خنثی می‌گردد. هر حمله‌ای که ایران انجام دهد، تنها پیامدهای اقتصادی و مالی متوجه آن را عمیق‌تر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/441425" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZcLAnAWdey7lC52zjVKHxy9x7NIDQ12Cz-tw61aZjjb5icYXhqPjW-PyLMLPEew2afhgtwnBTUPXUbHWzupEWi46qpfZduyFPLiIkhV6c6OczzE_-BZ3SMFyWnVdBmr7EAEcTTPSi_aD0GF9ctbNP4a8MTaL0WxPQmTXJ1KD2Zushz1S8EA2n2wdvwnli3mK4qz5QddgQqMVXlxW1ZBrDjnsmFUDG3D7TbbvULvrbtfz_fZfHQUYWyQIHdzX4YpfuJVH-hgmdmS1cxRSebk4X6ZVW0UzABF80lyPlvDMLcoj24GugJ-gd31qtdUcUsCVRfdpQ3SM8kRr4Plr-UUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آمریکا امشب هم به ایران حمله خواهد کرد
🔹
در آینده‌ای نه‌چندان دور، جزیرهٔ خارک و سایر نقاط زیرساختی نفت ایران را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت. درست مانند کاری که با ونزوئلا انجام داده‌ایم. @Farsna - Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/441424" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تنگۀ هرمز تا اطلاع بعدی بسته است
🔹
نهاد مدیریت آبراه خلیج فارس: تنگهٔ هرمز تا اطلاع ثانوی بسته خواهد بود. از متقاضیانی که مجوز عبور دریافت کرده‌اند تقاضا می‌شود صبور باشند و منتظر راهنمایی‌های آتی بمانند. @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/441423" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV2xzK1DId3alpt9VZWiUkhqx0JU_R61_ZGN9aLObcgXuqofDK17NmopYLBuk36VLiGPR8yxW7EyijqP55kE7o3YOe9WoHogp4Y8-5q0IkxSX9qSU6dubELyWDUNg7WgvTKxdxpnXrddVTkTqohvU_qRqimgKXWoTTlYu4LBJcCIy25euRhMHTvLfXHw_puMf44jm_6duNOaWpBQ6d0GCx-LgJ1y_fLKCiWXcsL2whtidZw9jVbJ6mnvmFCuWItisbeOGGf8WZtkRTBxbr8BZ8HblQ20bqJVT5pnDxYQ1_Rn6OAzJQiTppp5EeNDbYMAPkWuCoqehvkHDX0QIVeIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: آمریکا امشب هم به ایران حمله خواهد کرد
🔹
در آینده‌ای نه‌چندان دور، جزیرهٔ خارک و سایر نقاط زیرساختی نفت ایران را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت. درست مانند کاری که با ونزوئلا انجام داده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/441421" target="_blank">📅 15:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piUwlhlAGTKwzK1WDT9LlLjlQycTgHxrTixXaVKPX1X6AF2wU8ZtFQWoJkhd9nsnkfJpL7JsJy-yqwK1P90wFj85ilOR-mERzrz9NpCcfi2xdpTTPbOJMGlJdVX13xvbRQx3dNGd5laEQF0RuJUW5f2VICpm2WPPrpbSJllh1YPHAk9W5ZWp8_50benPlUUZtFHmWkRkjhV26GfRP_biQt-IFhZiY36tWctRRdzibH_T5bCB6FeIjxGK9nikNy2_6wzfwOT2JlQV6m231a_qYcVa6yrIC1rW4Tuqzw6yoHJTEzW2UV9peBTkhNDA1_fbnKB1ZFYU10AwINe2HMN3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت‌های ایلان ماسک در بانک اهداف نظامی ایران
🔹
قرارگرفتن کلیه منافع مرتبط با هلدینگ‎‌های اقتصادی تحت مدیریت ایلان ماسک در غرب آسیا از جمله کشورهای عربی و اسرائیل در بانک اهداف جدید ایران درحال بررسی است.
🔹
این اقدام درپی اثبات استفادهٔ ارتش آمریکا و اسرائیل از زیرساخت تحت مدیریت ایلان ماسک از جمله استارلینک است.
🔹
پیش‌تر کمک نظامی ماسک به ارتش آمریکا از مسیر پروژه‌های استارشیلد و پرتاب ماهواره‌های نظامی در قالب اقداماتی نظیر رصد زمین، ارتباطات رمزنگاری‌شده و انتقال امن داده افشا شده بود.
🔹
ایستگاه زمینی استارلینک واقع در اراضی اشغالی، قطر، اردن، امارات، و عمان در کنار سهام‌داران اسپیس‌ایکس از جمله زیرساخت ۲ شرکت «آلفاظبی» و «مبادله» تعدادی از بانک اهداف جدید ایران هستند.
🔹
یک منبع آگاه به فارس گفت، ارتش آمریکا با پشتیبانی شرکت‌های مرتبط با ماسک دست به جنایات جنگی از جمله حمله به زیرساخت آبی در جنوب ایران کرده و جمهوری اسلامی ایران حق حمله به تمامی تأسیسات مرتبط با هلدینگ‌های تحت مدیریت ماسک در منطقه و اراضی اشغالی را محفوظ می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441420" target="_blank">📅 15:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSXYBadXGklI_e41zOIeKVs8Dd0m7TUpaKZ-G6ywcPC1SckKFwNExJmGK8LGggPjubnvN8RcFAOwxdw46xGElIz_wEy1iVSeu9nkFlzZ_uHJp8Yh1lmVThOK0OgXE4AWVXLmryLKayG_xDnnai8p-koMwXEIwyGLjpoFTU2Xudo6FrjHYjQU07rEjWoInQzlr5s6A0gEvqyjf7Ucvh3leC-fjm_37ZIEb49bt4Mt_BOffcdeAoSQDrf1qnuAW62ncxQHCvW0W1zsBEnN1A712ploDOYvtFl9hDEvI1MX3e2Gc4sQ5d4xwPCIi3vjHH7bPpDP7qlSp6CIFTyMufu0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: آمریکا باید بین پذیرش شروط ایران و تتمهٔ حیثیتش یکی را انتخاب کند
🔹
رئیس‌جمهور نامتعادل آمریکا خیال می‌کند با بمب می‌تواند از باتلاق و بن‌بست خودساخته خارج شود اما با موشک‌های ایرانی، بیشتر در منجلاب فرو خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/441419" target="_blank">📅 15:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک منبع نزدیک به تیم مذاکره‌کننده، ادعای سی‌ان‌ان دربارهٔ مذاکرات جدید ایران و آمریکا را تکذیب کرد
🔹
یک منبع نزدیک به هیئت مذاکره‌کنندهٔ ایرانی در گفت‌وگو با خبرنگار فارس، ادعای سی‌ان‌ان دربارهٔ مذاکرات جدید ایران و آمریکا در میانهٔ درگیری‌های بامداد پنجشنبه را تکذیب کرد.
🔹
این منبع آگاه تأکید کرد که جمهوری اسلامی ایران در روند مذاکرات بر مواضع و خطوط قرمز اعلام‌شدهٔ خود ایستادگی کرده و از مطالبات اصلی خود عقب‌نشینی نکرده است.
🔹
به‌گفتهٔ این منبع، متنی که پیش‌تر از سوی طرف ایرانی مورد تأکید قرار گرفته، همچنان مبنای مواضع تهران است و پیش‌بینی تیم مذاکره‌کننده این است که در نهایت طرف آمریکایی ناچار به پذیرش چارچوب‌های اصلی همان متن شود.
🔹
او همچنین فشارهای سیاسی و تهدیدهای نظامی اخیر از سوی آمریکا را ناشی از مقاومت ایران در برابر خواسته‌های غیرمنطقی آمریکا، فراتر از توافقات مورد بحث، دانست و افزود: «علت اصلی افزایش فشارها، ایستادگی ایران بر مواضع خود در مذاکرات است.»
🔹
این منبع نزدیک به تیم مذاکره‌کننده خاطرنشان کرد که متن موردنظر ایران، به‌دلیل تأمین منافع و مطالبات تهران، تاکنون با موافقت کامل طرف آمریکایی مواجه نشده و همین مسئله یکی از مهم‌ترین موانع دستیابی به تفاهم نهایی به شمار می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/441418" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-441417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عراق در سوگ آیت‌الله فیاض ۳ روز عزای عمومی اعلام کرد
🔹
در پی درگذشت مرجع تشیع آیت‌الله شیخ محمد اسحاق فیاض در عراق، دولت این کشور، سه روز عزای عمومی اعلام کرد.
🔹
در پی این ضایعه، «نزار آمیدی» رئیس‌جمهور و علی الزیدی نخست‌وزیر عراق  با صدور پیامهایی جداگانه،…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/441417" target="_blank">📅 14:28 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
