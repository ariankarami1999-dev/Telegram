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
<img src="https://cdn4.telesco.pe/file/s5lKNLKN_QUChbChMKQrt6y_rMJIgKRsieIlWeXi1R2DVBGMU_baC25V12IJ6GLOMgfAui7Vo2kNXjOMBMGupdKDFpmSM6z3GFYegW8tBoTMyyZx0KvtyP1FxBq1temqZ7Leo6na8bOG4sduRPXwFCkxpZm08nQQRpUbOZ13rXhfvGUHWXHwt0PW4j5DhJUw35ezan5SHlBtAloeH3vWq3nYMbYKLbvlGZNMT01v4fl5E4vPRMzAKrtAEHLOSSAqy_c_PPj_7aEmD_HuC0HYCzQOa2jVPL5CHB3sGNukvIgkkkloTG-pMgH0eMuWfKhNmPxg7ENvoC_UM3v3aTKsyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 140K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 22:22:45</div>
<hr>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcxD3gHylBdltS7-z2FzbdSblFwvrryUX0SCyMOV83nU76OXxeVh8xovRXchGcESvaF7ZXTELAZQ6Q76BZ0TIlgk_JQromIwQicBtSilP_9x3aqaCgRu6U4piVDCUlqmLDfIxFUwlkCzEHphmKlQjSJfSSXXq6LkqhfKYUXy4JaxoHRmF3k9lHFiQwQTmX9OZ02GK_6FQYf5cb3GI_KSiBw1rfWihv4sVHRYnQ2FQUgc023XU4FFUJMy5rm4BpTlv7O-xnR4P9UaQ-IOZguP3f9Nk64RNDuuUhJfVyMMkNtUzEVqmAEuiuylGkXYQRUKRtJNchFLdnKBhWAU2NCIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o3D_aSjMu6hcimYnpDq_vb_1zcNVKaFw4PBQJoK0dVtOcPd46rzHKTYnY8zXKwRnU_T8IB6kj7zyFzeBeYjpUkHvDRU32q3tRXPBJHKTD6WDp1AVYlyjx21TN2HQU0UgmYk7tXUbJGRXn05IEfyRuIQMRMMzpy7pTQsOx4agmjVX3h79ZDvjpr_qMrDHfEXAnY57gfvmx9qDfXeYJCx2BifI243rG4ek3lxQDXoyiFrtj3yWvHZVgM85pHgD9h37faQ2Bb75bCV_LyecJacFqMurF-Az-pAOgUmCorjCx_yO32uHEO4O_f05sFwjN69FOIZ8SQn5QjKGhY4XNydg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=aKfwenQoRhZmgr63_e5QNrDWY-CKDiSg4bpq38szTfchGXsnc3JSpd8t6VOMfGpg0thrZ1cs3Kw_hSf7CNUvjSY7PukHmnCTgj-PBlXOR46DostSjhSEbDg2dmLPLsJ7iVCY_3lpyevBpyCf9O5T-yU56Vi8knIRlOIYWsdx89NW4ylQ36juITr37VphfVqZpx3mtU279PZf8VNF93l-QbWisfc_3abGDzUdiEw7Yr0rNT-Nmz_a80UAufuW2c65WGaa5jKkpsDM8Nagt2DBVlQFubAzay6Fz1GnHzdYRG6nEusdTZecUy6wkurWznxaEaEDNmAWGMygBw9rZgp4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=MqcDt6-UdhoGF_TnqCIahQXMIk_7IRwOBhMH2cyF0CQyBP55auIpARcusjE7uTy3fduAr_E1nMVx9uYv6PMSosu500dKf5KnYpCNQumrbWcR8VNhazwZMeJ2gjy5Wwi7qE8-VKpj_ZZbL1ew1p9XX-qJecnETZAAZc4NryMufrgMDxoEGuFlvrGWOLvmfGTMq4RA-Ega6Dqc3BY92f0BxKIwoUYQnLD7svEdQ-D3CqPsMlAiu2Ik61mVxKZ_oz962w95a90NX1DGufWVYiZU8Qc25l1i3KM8R4wAMT-5jkZ5ArVlgD7Q756vQsbqyE3iaLfyz6dks0FgmXgJ2yYEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=IcADLEpyFDv0Zd1WCJlYSymZk-ST343KSgJOhcwp_SBsPz-NMNC32L1FJyU3kGHys-7hs2y-s5k_yPBpf4qPwGErZYQX7S7hKzFKXpFtFmhLhq-WR-KFlAinb5LEa6PNUrdKvIr1MWnDrBQ1L3t3yb3mCeNLdDaU6eHMZ5CTb7a6Pw8ODuBFqs7t-UtTI74HxtOwS_z9cjnM8uOx1JytI0zynSlHis6H82iVEAA2A67va40Hzfgz6z1uH3oKCyrssqR8F36ym-2BfHD68KxQ7mIz2n9Lgkd2GSTadbQFLmV2YqA6Pld1NfKBgZpmIgBDLuWILs1cUOKJYq9quz2sOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oXrHfeqV2s0UU-Irhs_RNosN-sV1ggQWDORH1ZZhCuiQ2w47Qsb04k__7mvZd1mx7CbrwfWzon9ELPymh9VZJgSNqrQm7avxM7Y2m58Slc37S44jLHUUlKLnEfo2E-fBNp62qQqKKuv6TD8uCzE8vcSutWxvxEO6UjnenWb1GTn1Yo5hLGTPbEDW-R9-rbuWLdQSQzaCtrAhBsY4HRhDmx6lfP0jZJe7kPSaWOWvdlvjj0fyqUGEm2Uu5WhHggI1NPP2HXxP3lW2V8wbyg3nU16SqLF045XmzQph2Hfe1TueT760ohKvd3r_twk8ENE-qwhtVoGaEWH4dZCPGrP4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8Gtk89ORLtNLS9KOhO2fyhYYNPReqwGaInFqlxAsf-wf7FpxovBISjdZkqM-lvoMGCYJswhjzhaxaGG3Qwl0f4ZkbHVAhahZPs9oKIRSbikoulEU93ev3n1RCLPwYySdA1DaOvb_fArsBB91Oo30LrZ5yatsXkg6fpWA8fX_cSsU1FPR_LOBXKt0l2SwT_Ske9qWSq63mQ1tS3kxE2Mtwmk_icH5qict3ZpR6ngeSCejZPH7xp15fanjElTjXtWqWw18xYgl7rbSfJp92YsUxB5UrWcTJ8MRgyUZqMz00nWO2PzYv6YNn3O8qebdHQ6jWHV_oVao0ee9IuFOuXe2AG0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=lVGrkgrwP8pW15USyxGS1c4CrWXTf48X4aWuOYZBd2Axl4po5jUEr_0ffvVzA49LoCmbG0X3Ppxr4b4WXwhntEEz0cfFVH4Y8WW65bcM13IvD1jceo1S0IHI1gZxeq7rxet37AcKSHD3apGr99GKaPBpr0Hh93_Wd3qjZOKjsJs2G8PmMDbrneIyiLoKAbCBmdyyWdN_TT8cbcPtUGb3nrY9wDZFsZSfSwJ99B1evL96K8HU43jSek4iJTuCUCV-jwuw9I0_CYKDiajjzPGuFs_7WbXu5CWHz5t6kYXiCLQsl1z1oJLEM52qiU0PqzFJYEaZrvidzMh8B77M0EedDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=SQWQxD80COsxZM7kzBEhb4e4VxuMG7T5zKUy4GuPTMiApFqwrZyGZdvt8q8EZSmBiInP1Er4DoyIip8T5GwAlOtqCb1dw13Esw_lf6rjGzGw-Y-WUoCaF46HAmXbq9bVcI1vPT3w6WpI4ZnzbCbIINP2WXd8Vw9AVdqmhCBRylOuuc7RXQPurbuMsLUX0dXSksMZwI30w-2PMwCoThqYRTtQEC48QH6IJjII0pi9MuJPeOiZ1ZQD00-Fd43yo_DAGHgVNSrm50Zagg-THyqJ-P3dGoJGjuk3iu5ZzkP1rgPYi-Wv0bX2fKisFEVBCcd0svou2ZVWiN-k9rr9FCO1ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-bylJvyGsbdiWQ85IhiwJm0OD9q3ERz6-uiis0JrKka9YhZL94xx5mJngNv5b1ChVKXLPRKU9kmPR0JyvJZoEwhLcw4qupC2UVIabKJVrSt11ALJ3N5qCrH-eDyH6JZ4CvpnjQOFFTug_euw9HISuKJRqNr7XFPvs_rSnS7FKds8UrKJO5gWwJBn9keLfrpu4DDSmOoIqyr0FC_zR3It_OcY3WToeHGEMgLYFyecWwQoofGuNeyrWuPZNyVU_3rcSjlAEUrqtvdnIsaRAT7S3bZv8JcQh_JJ-JAo92THdWEnYrlesmptAYdC4cUujfVrq7c0wfcmD5ogtocYYdQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYj2uDZdxuB9WUMjDEXDk0GODgOnFkyZlYdpKh_2mWAGpLRo4Mr_Y8gHIjk92Iu1o6UjVr6RrTFI0pNam4fd7JY03sHO_eOpPNfXE0AIswyZP3C57slxkqUU65gDGQW80IOQZ6GcpnVSUSMmuzxMvIiE3M_DOF-BKSOOfyLPh-rZKPjUomL9-exu4lqqELKv16WFAOLTSqbXNq-HLMcJbZbycgLEfpTQnZF4BzbMu8gpKRinZzj90hNHfbRq44UB26h0aMtf4BL1WvRpx6KmjJGWoYfpXsVpP2UXeq3oG9sf4JcbSvFTwRR9hpBmrXXqCQXo0kBgek4ooBSboozTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=hCOUfUQ_17Vzuw-8NWPN16Q3joZzNjjfpyESUG1BxPjOx5DieO4ul4hH8Z1nihXv0E2tr7ojNq_6FkCT7yvweZmd_1m0uXr8gem0UopsmOJQazjOFf3sRbtnFz-LWFV094gMHcJrdxrbcWgVhOB5P7w5wNMKMGUvx5QT1VuuHAKbuF_hNimU_SD_k97kTLCO9vkbzLU64_HDXJUJejHVVKTVaplPExFFK4Z-xY_TYbdeKlF7akarO4sGOeca75E9vmLjVKoEZP2xXJJijxpKn7gHt85Kuad6MJ4pHJ73vnWCiVVkix8hl7txZ9UgZKpMz163TZIiMuKOcLmQuTvcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=EiACp6k7Fvx5cPIpvmAzZho7T6ZnaRSQAfL2Naq8uPgFY-rgNJ5MGm_A4DH7F7w3EhaSQdMPBPy7VTE6wx07urPSQNJss62MNoPJ2W6j0PqHy1y-xLso44KE_0V3k0hJh9aWTSy_ddgBs-TUgsctDFrGfqnoEu8arBZpgXOR7z-LkzGZ6t1FLkSmuvh_GuBT5EwULfXdPQQhwF9xHjjgmzyso5_4lYFqgIKkzaOW5NmiFSN9rUQ2Bb7-XVlUXACao8sjMpJBHQQdeHOIhl_JCzd_EEZb9UEDEfdK9cfpOVsyIzhPMmmWFIJXDKMkvKDTTQBupVsh1BzMcTiaQPg9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=rVoy8cBdYlNMKyZIKfDWMjr_haz9aLFx4JYR8QDYrOSQoPRg3vo6vjNAHP59IFYEJiJ2q2tq5pWdg2jPlmR6Kzb8FdIa7-yOrEmMQDvoS_sGLeawxQrRz8vLF8OpGHONiWFcJmskCWN2tTkAucLl7kR0lRJXPUy5VrRZxm8QLx1xUS2LBpRIdRChI6AUrnA9vhFg5xTmqD5o62qCfnc-KtYMf0iX1uelf-v2Mz1o28De76i44EG2kgbFf1yuymWaWCOfPb6_wrs1Rs5tpKGNfsAb3agTMZvtSUqQXmbT9CNU_5ShauLE5GrkasNVZC7pdjF4s6oj4T9NZviXWPXFQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=O2JzYNZla5Mp24EokcP8nAvVuhzIw5PJZUjbrdHCKVV7hDmbDm4GiRroAnnS4P39H94AH0EDBJphF0eeoTwvNgnUcqWJ2DD1dUKhbN7CD1-TUpJXSuFfFBicAYR-rRc3eTRAPyZVA5btmO48QKgufzaKHZft1VYH6UgDsIQz25uOd6lkPIeLE360zqjn8h4I4zWYwnCwkPmf2K4qAhR4-igJZfEzdLZ-ykOBeVyJQObrftqMNtLHBHPIsvscJE2GheW1hp5cofJy1OQxfTw-jnwNGOE-dyRMvC4qXBDlIdfk_ekDju6_iM4kBbHhOQdD9Yo5if0MawkSZRquRDQ3Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=st1mCNPfWqmv2_LjRWVHIZPTrsYPGlhbj_HLAQSPv3Un7fh8t92n1j0tp-8eUGEq3S6RyLM8jKHYKp8K1PplMnaWPSQJ_1jHQePq0Gc5I4wZBFqA7KHF_MHQI51FPVjr0eml-47sbBibyn9j8bseB9xfk4Nvtc-9HeCi-A1VhotR92UTOo69rZXxGRGZu_I7yIkzjT4LR9LhMOU9uq2O1-CGJ3_fAChCEKx6jzJauEMhjSUs23MSJTcnpl5ZJvJTyvCFSJpzjNj8lUeU_1CSyE2Cj5kElBKT7Cs7vRH6dt4SL4CrBDUPc8nvlVvEN6ypoPReU9aihNJ8dNJfUl48SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/et-fccib55eslOMEVbD73D4-Z8-sk9HrN5QGPetS7Sgacck-K3VwY6xkQ4lXJNzoExH52T5rHRbhh0mnE3vGyhW3Pt0FaH8yHOfxyVaEgq_VOvOLhmjOt6G7qEzOHgwdMTjGpB4c2IcbH8UWVSLIHGwkeLQap8pFooiPvB0HEsN8VPfmIJ2ek3gsvL_Cvpqw2uIHLXDNtMHLsV0rYYDt7l6Y6CTr0k_dN9WzOSHi9K0BqN26VUUPaH2WDD4fUZ7CiAO-Y-ytwc1lqWCnr_9paV0ICFYLOC0G9U-e-EJHEvoZseUIcEBKP60wn2HZut6470ic0m8IcPB5x9XrTLrLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=AzQNu25m0bq5qy6d4VotAE2xOD4jn8XMF7xDOhJfurRm8HfEqoaVYMXQAf8fP3qmaj6yOGEHgwQgfep8QfXmLwTPgl7UNo9O9H8Afgd9PHXfP1AlsKGynG4H7ruhgd2SEOAKbq5aX0BSNA7FE_Ep2I0tJb3phgGOePk3kIHC0f1yy37IytAKfRd6oDL0hPnHN3iMzVeourrohrhFB6dCIL5dFUZ3tQZyDc9q5ELceC9tme0275HeRIoO7Wat-gRjJf5Xqn3hnAeBd8tpWQA8AWg3lMkzO_ul8sM52mtCvRMVZ1JAzb7oOgBfBwjwObDJguzm9oU67qERXz-Lvb-25A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=FOGaozU8fkS_F5IaTOVz_y4SNEvvthIIt7h-w-BjC6Oe7tSzeKoH1jJUiazHSDW_8GUDgCvYOMnt-z2zv1tzfXRaznM-pX9tDEcQ7ff845-73w8-wMGrVYsWLpgLQ7r-pNaRS1dpHaoyvCVp534sHDmTay2XaBgZjvdQxZdMq_MiSlJP2jaMROmjIG8BIyB2BFX4rGFfp8HULQTEqqLi3zQbkrNGZAW2AO-W-Dw1Sk7dw-cYeT6maqf6ADo6vVDxoKnZ2B4TCKHfl7qGy0eVD-lB-1TNPOc-vn1u696W-ItqHP-rzrEUm5EFZKbNnEk9eT6iQN7SncLXw7B0OrOp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQsmBj0xYdXYni8GcA0QRnpuTBSeLNLLXUIQl7OM1HZpFIaZwQesRkS-yjTj7_1ZHD_uRhtsNggvcHpOFh0Fz8kVru6qAf9Z3E5iz9GCD4xxfCJVLmHXVmuCs8OXGoQTxpknbHoT72GmdHvWR5th07tuhn6yoR8WhoEgvV1AOh-qAGGaWTl9vPBOlyI_H9gEToVe4kyTNCvzTX-IHQMYzYHaDU6EnLZqGNh7apcPwwlYbMS0KPTT2k3b10EnkO8S5Kg3jrIOjcsVDSBi_r2f4DcqCePySaZiTTyrhcpnLehWM7cFZSaDIChw2d5EAdIos9bt_uwCjaXipMOv_99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=A921GVZGEqWlYrbnSKtBrsnRkUR48-VL3kgms6qTRqEcfeigeo1vL5sZgh4fyCTfc_eeZHPvJZUJdcD_tcUWgnsw7WUgeHcgfFxPoyLFyw1dTYkmkC9UPi7eXSrH3lGp97b8Xau5UrN3belk0bKaXeMkEkK7wuhXgt_oJQ4CLijVhWM-IAPxC64h8az3-zoxp3xwujX0YLNXQKtACEKsGoCWjnw7E2qO7M7coNHIqFGGAaNZrMDL2NUsvdYnp9wNJ3MNXwm4pffRF_TuDR5x0SmbowJMStrfaU_z05ciEoewuKmfSpL-Y0YBkG7btg2JUpmMPuU5XyyuhY2lit3lTGTuc5RgCCpK29SqkS65o3DrknW9_u-V2xunFIG-XzbCQC6xsg3Zw4CBo-IlQbOqmMROj13HijI4kY82v3VEPupw0NiwnLfw-NX0MN0lJMcYS6wlq8rP47bfwAOYI4c2q4OQsXNBcU2cxpJrzNFCiDzRRcXwobJ9PAjz0WtGsDAaO9JezB_MnvNmoui2I11Xl2_ZNvNTRyP7UvuIskF-J6EFaeT7E8ld6I45aDdoy85gGIRiUJEwYKaNdnVUTMXZ4tUWVsRlbOkvPKelRYT9k1Ct-msmeZq7gVUK0xjG-_yvQn-_FP_-jN9VmCRiexH4Z5XSB2KE0D7v70daxDgSyMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=kOwLZpsk7j2QzdKPFyMeZdtaIccHlHOwGibWyn-zDsN07jh8yK6hmk4TV8crKaWgY3rwFi-8N0g4icRLSdhBmEpfYdBkB2jZjpO5BmaAMf3OYwv2z_BPRckYWJfcMfzHn5Qrhi7wmKAEiRsKQerrG1KZY0bC2izceihbds96seVg5R6llQpQAbSUR-QsTZ52XGfGXJcVnrn00mh9tzr4RDQ2jnmpFg1DsazMKz-mn1ezrV6zV-I65v63J7xc5Fm0hMUuIffI7GR3NODlH7OLZUwf42Xtmkp19nkARcSTwcdGFdPjweWAB3EmajoXE9hP20f7EcttOz47gGwW_6WRog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_N__6-6oZS138d56uSjwYhMFcjp64PxOYmw6bJtX2D7eu_TQB7cugaKvRr-qbe1CGBhNa4urgELt92BCy02MSRpYwsCbYrCCCVLjvRAfKBOc3a-a9Wt2gscGhFgPHIfIcoiUb_v1KLItPfe8QYrNOY8_jsZrnYG4GPK89_FbpYeY3WrDEKQtwcKd0SHehcpI-LSSi-Gx3Bor_ypPsQM73iVubcwrw2B3ZyWLdYCzqIS8A6YFYwcEyZPwsnfAKY8TbUvNYDpAw3edIgfVtK9YlvP9dVvtWwkxpiXVaQYDd4j3L-eQbS22dqh95z4S1QPLmeY4p7BkBEd9yjzPm7Vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5tshjScOqoxyy2zCmi75fZHUfeHJTjRbOC2GRgs57mnboHqXA5Ha1b_-fSYbuk76EnfqI3VCKMsIWbkg_pi9CwQ9CFAfaKn7OZ7_BiiLmcR4Bj7MIrRfvrLYmojRHbFupFfS1oGIB7elrYF0WS_yefprvILM2_TM9KJDxOF1gITNXLex2pQ4S6HAnwSn6p6ecu744XI3OnPuQ3S7tztbhiH-jxO1mmSRDsG2NZe6O7qtlfjZ1O57-TKQXKr5AIkWUoAbDVMBXbUAPq0uJEYsgVVWVo6RV8JoPJPZ3HzIXu-8JNDtCrKI74v2Ee8g4r8KbUEyZTLukBSKagwMIzxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=hbuqNeGQiSIc_tZbt6QFH1kJ1ZaKnbPCvYj3EPrUUKmnl6WvCvac34v55C2nZ_Q1rVS_btBtj6Jivj03yjpFKZE2CADPvim6LGVEGeMHu8v7h9pFbwyASDFIyilD4bhIJbN5mazLk2BCVHtsd6I4Sdbe6Rk85uRtlPLB6AT3LRFUfrCY4KQj56qGmqsS4MOHRE8-S0cJwpl9UYXUOsCYh12ZaOg-WC7H9M2GaCSQ8RqGO2vUATs9OTwd6Gu2bdSkrDFlIKIOm0UiaWOgoJSQul8KnlR_oCnfAKNEH3HSl4DTrMONhPU09WTXbCa441-j_aD5pZTFOsXcid9khMwK8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15118cd8c7.mp4?token=Jf6PD_spakTFkqbRov_Ooi4TcCTu13oFTfhCnHN1DgB9WBKMsj9bItvmpoNd1XAEdxR2wdqmadcqM-zqpZXG0DEw6_9LIMSCB4uD8LAq_68mhmXQ2s40Qse6S9Dq3sHpXSw0fbHkPikQn6GV0njUCaCGLZZW7FH4hIyACXa3o4V_nSgobj1bSRzXeKbo7IQ7R1TinhNk1JNnVmiH_PxPvistkwaQ-YC6dmBR_mSq-4YirFHX5mKRcWUIs-zdiR0OlcbO13J6hQegU7paUPRE6PCwW__BaYMiMFf-KEJTKmjY45z6-sH1ryTQKVUhhx-4jNqb3O21i8CnYWJArdpNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه این خانم در الجزایر و تبریکش به یکی از کاندیدای انتخابات بابت پیروزیش خیلی وایرال شده.
"
منم کلی سوال دارم
🙂
"
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988916503.mp4?token=ahCoxLffdCweYDYgCZhPFCE4J2TdDVaZXRz3l8ZVkSjkuwOfPCvd2PMOcq4D9SlMDcOsp9vfjkN3WGSBKlQQZE4u9YhJXZq8J8gXz_eo8pBqVkbPn4jjACqbpIHNlNjEjxh-lChVj_owD58yxfhSO8m1JLt6MxLQc72JHKQ-droEqHQ-EIS5Hrpw466LbpMsP5jKq6bwX_PnFvhKhVakv52CQz9KhcqfmUOAI8E1b8pAtvLebf8Je6FXefi0S3qKsVhSjOOiSjZ8FIhgrYGJgxTOcRiyR8pvvOeyL0eh4LdPUw5yIDEW6jjvo7kpOqaKL09kfhdmIlPNR8dWwvdBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سؤال: آیا هدف شما همچنان تغییر رژیم است؟
🇮🇱
نتانیاهو:
هدف من این است که اطمینان حاصل کنم ایران، با وجود این رژیم، به سلاح هسته‌ای دست پیدا نمی‌کند.
این موضوعی است که من و ترامپ هر دو بر سر آن توافق داریم، چرا که در غیر این صورت، با دنیای متفاوتی روبرو خواهیم بود.
آن‌ها با سایر کشورها و جوامع دیگر متفاوت هستند.
🎙
سؤال:
همین دیروز گفتید که به نظر شما دستیابی به یک راه‌حل دیپلماتیک بعید است. چرا فکر می‌کنید ارزیابی‌های شما تا این حد با یکدیگر متفاوت است؟
🇮🇱
نتانیاهو:
خب، نمی‌دانم آیا واقعاً بعید است یا نه، اما می‌دانید، من نسبت به شیوه عملکرد ایران تردید دارم.
آن‌ها همیشه دروغ می‌گویند، همیشه تقلب می‌کنند و همیشه وقت‌کشی می‌کنند. آیا ممکن است این رویه با اعمال فشار کافی دیپلماتیک و اقتصادی تغییر کند؟ باید امتحان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQcBBQOU50mu1zjgPoS_TyHADiTZjeR4N2jT82_U1Riz5kIVa_JeGOMTWmhXxl4nuBz-XyTEVUZAxAvlBs0TNDssbvPQAli9dLh7dkfN2QjqS-fY-qNExRNR00PCp13RFRGbSU_G_jmyQorbIQJJ-_rQIvA2QD8ECOO8PUELIqaDyQ85zjaXXcfCKpVbKjuLJ9bGYsHAqstBcozJrjWhsxvTZQgGD-rRIsTHaEa-1aWc4-31ixyRr496pAu2lZL7psQ-wT9k4awoVRrj5sYNjcYU2WKTdSY8fLT9PGZQaiOWLea2PABjIolTVTbbARlakPqk2ZbvXdNm_caM2m0tjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=ALe3XEyMGNvkCzPA1Wqlczb8nkQdntaFz0at41hv9sTxG513xvKJm9svA3LuFtZg09Z3zew0c-iKnJoxnRTvVWpIbspY_8TbU5RzXsR0DjZTWKDbEI5giMv54Bxwu0KxpQUgp6dUojXJa9q9m631qVcInrzxsBmUV2AQU4zfxBegCWdSGcve5aBZ_bvYCK7qo4M3cAIu6FzSqBsYCmgfF3nqiM70akH7vYM7VclBDtQQOPJIWOuA6smGAP1TC3cAO0PCftub_4ZDMgWwQUYHxSSJMGieFsnBtOt1Btd-jONowOh9xEw-5ELmLeCfmO-Tc0kmJpNjsl_xZ0fcraWhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=ALe3XEyMGNvkCzPA1Wqlczb8nkQdntaFz0at41hv9sTxG513xvKJm9svA3LuFtZg09Z3zew0c-iKnJoxnRTvVWpIbspY_8TbU5RzXsR0DjZTWKDbEI5giMv54Bxwu0KxpQUgp6dUojXJa9q9m631qVcInrzxsBmUV2AQU4zfxBegCWdSGcve5aBZ_bvYCK7qo4M3cAIu6FzSqBsYCmgfF3nqiM70akH7vYM7VclBDtQQOPJIWOuA6smGAP1TC3cAO0PCftub_4ZDMgWwQUYHxSSJMGieFsnBtOt1Btd-jONowOh9xEw-5ELmLeCfmO-Tc0kmJpNjsl_xZ0fcraWhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=hh9gGhE1JQeL0Tn_937kngYrUdvl5ykNlipNDMDN2xPZa90ykDiTDfoyaXJORyHpPeHViRiuI11vXRj9K3W9klV-ZuMn86lu3XPzLWXYRjGo5izl594iJsHEzMuh4OQeY_E4OKoLu0eppY_-xn7Q0Ty9svdpPdK_hHN7tqhIZdV6upXvRCOslCH4_aMHNrGXqyBYmYNdTn3jmYR3tKePrjSUtVkgg9GnvLImhN4J02IB1kQV7GHNtZandHz0xFleffQHSi3YIN2dGTDQOx2rXZChZdGHmhVSEVG8OSjNzH7kCmcuR-TwErcCfHWH5puFuve2qbGTYBK740MGECuozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=hh9gGhE1JQeL0Tn_937kngYrUdvl5ykNlipNDMDN2xPZa90ykDiTDfoyaXJORyHpPeHViRiuI11vXRj9K3W9klV-ZuMn86lu3XPzLWXYRjGo5izl594iJsHEzMuh4OQeY_E4OKoLu0eppY_-xn7Q0Ty9svdpPdK_hHN7tqhIZdV6upXvRCOslCH4_aMHNrGXqyBYmYNdTn3jmYR3tKePrjSUtVkgg9GnvLImhN4J02IB1kQV7GHNtZandHz0xFleffQHSi3YIN2dGTDQOx2rXZChZdGHmhVSEVG8OSjNzH7kCmcuR-TwErcCfHWH5puFuve2qbGTYBK740MGECuozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tYrsb__rbWy5zxYdARfhV8INB1sumgiqUvhpZzbd9pEpDKtTyM13BCBlvCSp5K0rNkgILNzclTD8WlNhyxS4SJwRDe0_Qimgnivx6WXEbNwlGDzYEtRXuXH58CY7ZlSU_wQ3BKG9kgjFHZh5CMk8PJS9JLlIsLMv6tL6qWVIT51zCxdHbeDjY0KONyQ8LRTPeMT2JrsAwh2P59RkkOs3BXTt5FMZghnglKG5RERDPkATlaw2ZvHco82oyK_NDjMM4jGT8GEc5Cuxni5v2wJiUXRMhV8E91ULWoc-DVbEFwMi2pJeLqACN6UEFVEk4xmAXDOIhtzoOnVOSJPAvy_BGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tYrsb__rbWy5zxYdARfhV8INB1sumgiqUvhpZzbd9pEpDKtTyM13BCBlvCSp5K0rNkgILNzclTD8WlNhyxS4SJwRDe0_Qimgnivx6WXEbNwlGDzYEtRXuXH58CY7ZlSU_wQ3BKG9kgjFHZh5CMk8PJS9JLlIsLMv6tL6qWVIT51zCxdHbeDjY0KONyQ8LRTPeMT2JrsAwh2P59RkkOs3BXTt5FMZghnglKG5RERDPkATlaw2ZvHco82oyK_NDjMM4jGT8GEc5Cuxni5v2wJiUXRMhV8E91ULWoc-DVbEFwMi2pJeLqACN6UEFVEk4xmAXDOIhtzoOnVOSJPAvy_BGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOBjBZ5BgCF9Ly74FCMz_P1u8e5b3sOtNVFSAStzdwzaLJvrjvNuzhkgzNbEv14N2WF2HKGkLZBnBRs-IPJGnPsB_fVkn4sOsOVyDnO6M78V3t_ymhX6KhJeNP7JxHX2lrmUC_uEPZveFFAEm1O33mOO3204cmbb-u0wxm-ogOc1tscF5EL8EcOocQa_4j4uDmasJBFe-gwjIniuEKTzuQCnEyfa5rvDWgw-2lxgT4IZAx546cYtVQt65XcUL0HIyy5DuJwL_CmuUioqrIP2T0sMZ7fC7ghlxereEDN0qf6R325IKxAjgpGef5I7z-HwItFYwSSDQGB39F7mlb5rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRIvvsQDyiWv9EyJLkMBXXJtL_TG2oIToPTeBe3lzqHoROkO6m6Vwdy6MDh-INgzYoyiRNeBUjAiqoxDGjJz6ijjTN9Tk0ctSsd6J47QkBqWZmh7RV1eheoEASjmxu0lf4NCcxQUJo06WBJeToajM6SLKKdcqRkOPPqPchcsoMog3KeTPmzcrLZD7V9y07wjeS4LxTfheQkD0_kciL7segk5SQ8QG5q74v1VV72HqujHPWL6MxZOxFAZ9F9kW0Bgbg4qu9JYeFk-reoGAIFUaFEsRuEf6ZN21YhHmx44_0cjGchoj-Cmmc11dE0PgeJ4GTKIumqEHYQfjwESEsfE7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-bERYZWhZwUAs39VmbdueLslRK24ZFHe8EODyK-sLB3lngXy53h6DbknZEf0mHumT6bzrwvZa5sdkyP3mxoezzn-ujPp-9W9d85BrZJzOIqh78pDLlWKc3ndJo3cEy06LeZDjWXPoO4GaKGiiBTVqdKA-lkbh2GwKobbCsz6dSv8WRJiFjXYcUgYYl7LynstO30HOUs2e-DTmhTIriZkYEIHN0TJ3BxF3aqgHlgprMKvbUIQM3H6kROA4DUEPXoTPJOTH7MqfPkb8OZwAfNwv_DnjMp-dsdJu49WM6G7ogR9P0jBl1QvLQVhXW7XehszFAKBv_m6LnIRw5OaZ7ogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGB_hIJ4x_eeF4liERJ4531TJLXigjXpmvYRDEc-s3vDBHkCxi26ld3tVP0WWgEgV3x1sB18CdpC33NhU3Nap1cx98I1ViLxCg2_Uc2SjuyLEaqxGOTbJ5B0NRq4ofwk-rziQLwnxtifq0P0rx7t-Jf26HaKzuIN_LxGNtU51_fFNOkXQiiwPFU4oqbZKbhOGt8RKlU1VXMHWiku3BMcXvz3jeHNYf29uljLQM-7_sPjiO-FqP-YRwBbbMkGuflryZQFzC2t4pf5foojAo0UxHLICP-e262dhTMeEudFhLyYWQcOcQaZodaPLHCyKyFIfqCi4ZiBvurQ_ZYsmSsxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrLIoSt7QfZ9FVIWJfy6pdftUrpt_Ju1hlt7vPBQ98ivQySKckRrklFTdlDbgZVxAJQhL7pPZNeVGQhzYvjL6MnGA3f-BNoGM5_ZQs5A2PUpeRrKFwjrhs1VcHhLKAOzSTBQhNKOLTUB9q2gsImtNIm7GG_aEsDwI26vfpjy5p55dokIgSC2zMchForSDEJ4vlMf3SGK5nd5OKDvHzR1_RJwkrd_DpjYgaEyRpaFBIIonI3x87YPFpkdbVbr_Bok7iYSi_9mlv7uDnUgbGC0x_y_HCPRffnWLiGzOCovr1v3Fqff64yR7-lPs_gZoe1jJrCbH96ZhtxpcT4PPocOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MryE288iiuyg2pyqk1Lzqq7bl5o1GZ1NsyrD3fy1DBQpOV1ffBnnJ_8kQYO46Oi-65YvDmmFiRHGZUdE_dfx_D9wW1antRZ3mCqsRKmyQVKNti3cmOchdImBjUJhsKnvXySftSLgjISqm49JZIyzEA4TGSBimrpqHKeMvrikGM_094zXW96luHqv09R0nOpHNoGLenn78BHCdkAHkmx2jGBQeh_givX3d4Ex4tClGm0bNlQ6Uxty9AjRMEctCqAqp5T6CjrGeG7iVVcBEv9QeeTm71B02cEqEQH-AZZDwOSXeeuYEbXi7LqlBcD2PX6fCbCaug0G39hfjs0iqfuVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN2ng2yqFG0m_xZf_ZIviGi8Upf7SVfUJrNly0tkcSC1E2uR3EmOdbsCN68LdhY7wpeQR10h80EkiQQJyTGkth9OtUuTvZLQYPvqmkWr9lHV9xsrPsYP686OkC1-akuGL0adVEfVTaG7w3Sls-aSoUzOJtc4RtWO-7rUslh8RMcqS0Tl3FhrQq3Yq2g4TBqE8lYEEg5ikyM7EgJNXPZGqEw7ihkivR-EM0xyTxx82mrC92YeC9AHc3DLysn8A9QMZq4d8Emh8v6Kc0GWV4gamO6gRO4NyRDsJa86NmbFHOgxkYWfsWo5Fp92Ucr-9OMwxRGznt-U2WkfXZ7r7lViAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syrvwY2RNDkvuBpzr6dI9kBySbICZM5sV3QF9OhQ0GXv_gXQyUFxdu8mWRoK6zFnpg-Io7RNjkq2CLFUF3rx5KBjYFJDMQ5lxBh-okNoRecgUuw0PK1AMz1k1LUwyNGy6R8L8FjlaY2cOKlqW6KnwRAmvJwsWviATUwGO-NdQSY_wyEqxg1YZjex06STpcXo6JpPCoLjx800vgkSwkJ4AenUreImy8awXTALs6qCEW6Ir-gC7QFGJAp9jrB-enXcMSC_q14VLxARG6gIYqwDUfrHlu_2m3ZeA_nIgKo56PZEPYJkBwo6XVmKyCe4Sfuc1fsatm-TF2_iOD5ocqCxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=k83ukwEhxZZPdxiE-CvApob0Rqm17_G7100k5ttV_LIpUfHzhK58uhqlaDzCkAUnUgAo-s-d33BC72MJ2Y7Usa3vTM_gaqnyrvdwH3a0o_cZq9bMO_BKJmAtDUzj3d-DHpIJHi9ZV3DxCjINMj2FNXklS2LngasOQhLP5oKZixcqQSJJxBWq11z2Uw-TtckfVgZ0LN1kyghRFFqSIMgX4dYrxQDdH0pRgQe40h9-xBHY8unrF_wqJsbOgTEYpqlqK6GPO72fa61By29766thcf_UvHxEycrh0DFDHRLpsvVu2EMZYZuVVJHHSEEnMaB66un9pgduKSAZB8snU3z6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=k83ukwEhxZZPdxiE-CvApob0Rqm17_G7100k5ttV_LIpUfHzhK58uhqlaDzCkAUnUgAo-s-d33BC72MJ2Y7Usa3vTM_gaqnyrvdwH3a0o_cZq9bMO_BKJmAtDUzj3d-DHpIJHi9ZV3DxCjINMj2FNXklS2LngasOQhLP5oKZixcqQSJJxBWq11z2Uw-TtckfVgZ0LN1kyghRFFqSIMgX4dYrxQDdH0pRgQe40h9-xBHY8unrF_wqJsbOgTEYpqlqK6GPO72fa61By29766thcf_UvHxEycrh0DFDHRLpsvVu2EMZYZuVVJHHSEEnMaB66un9pgduKSAZB8snU3z6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=ivyhmlpxL175jt_BstLqP4w7S_RCbTWDhBDTyaU94QrQ1t1UM0eRd5j4KmhLYa7zy3hiSjWIE4BI_VsiNM5UAxRp-hDs_xk3LiEUKT19iI6opqYGZ3NddwIfZHt_xb272yfFO2v1QyWSKibn8Dt7JyI6HK-UQGK8RPBQoY4MwB5KRmCwYU9TMm2pgsA9Pb35AWAGVWohpq2s-b_xQKTJ8pUKxCrb_MiyPkSWqtD219qTayPOl4ImcxZvF-nwOPF0CW8jeBN1jdtZMxnpEXEUblhOVupj5a-t-RqwVYK4XryFTtPn6O_r05TfwbH-CbJXMVgeNGj4Pk1EvNmg47V5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=ivyhmlpxL175jt_BstLqP4w7S_RCbTWDhBDTyaU94QrQ1t1UM0eRd5j4KmhLYa7zy3hiSjWIE4BI_VsiNM5UAxRp-hDs_xk3LiEUKT19iI6opqYGZ3NddwIfZHt_xb272yfFO2v1QyWSKibn8Dt7JyI6HK-UQGK8RPBQoY4MwB5KRmCwYU9TMm2pgsA9Pb35AWAGVWohpq2s-b_xQKTJ8pUKxCrb_MiyPkSWqtD219qTayPOl4ImcxZvF-nwOPF0CW8jeBN1jdtZMxnpEXEUblhOVupj5a-t-RqwVYK4XryFTtPn6O_r05TfwbH-CbJXMVgeNGj4Pk1EvNmg47V5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=qX3V84a7G2NgS_mikQQ53z0o1umQYtSyhyU2p0Xj-6TeW-p4CI8sYb96qozOKDUxE_4cLn_7ZeL0v_wwHOTkSAWxcxA5NoQDDQsTxDQmLGAho5UcJnLOTwlyNKtAirwEFODh2AtQefOy6gqSY5OkzAysIduw-S316SljTky-BqHO3OALM2AsT-fJUDD-R6MHlROW-bQxrjUTivAj5LFHmy_vObTHvzS87gSE9QSY6fOIk8UmaG99ql8sS43CmY_Y5HPGq2BzFhqBhYzeCJPyxptjiQGd9nQMK_1wuIQEAiu2-6U_FSPTBZ2ZE9gD8-z4qiRJtkfPIXxAzrGOGtqyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=qX3V84a7G2NgS_mikQQ53z0o1umQYtSyhyU2p0Xj-6TeW-p4CI8sYb96qozOKDUxE_4cLn_7ZeL0v_wwHOTkSAWxcxA5NoQDDQsTxDQmLGAho5UcJnLOTwlyNKtAirwEFODh2AtQefOy6gqSY5OkzAysIduw-S316SljTky-BqHO3OALM2AsT-fJUDD-R6MHlROW-bQxrjUTivAj5LFHmy_vObTHvzS87gSE9QSY6fOIk8UmaG99ql8sS43CmY_Y5HPGq2BzFhqBhYzeCJPyxptjiQGd9nQMK_1wuIQEAiu2-6U_FSPTBZ2ZE9gD8-z4qiRJtkfPIXxAzrGOGtqyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
این ویدیو رو بفرستید واسه اون تعداد از رفیق‌هاتون که عشق دعوان:
دیه‌ی شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
شکستن فک بالا : 160 میلیون تومن
شکستن فک پایین : 640 میلیون تومن
شکستن هر دندون : 105 میلیون تومن
شکستن دست : 160 تا 210 میلیون تومن
شکستن سر : 120 میلیون تومن
شکستن پا : 210 میلیون تومن
شکستن گوش : 350 میلیون تومن
کبودی صورت : 6 میلیون تومن
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=pQwfvFnurR50n5FZuXsyHkATaLMJdN8v-LX1QIvT8KERUXg1vlfPhMKKNGhsb0ml5QLYW30qXhAUYnGLRR175tXiUuYSr7IE42qJmYtnXx1WKtgeVhcZnXosoeIcsH2ocqgQtyqtNgAygWjcGnbRXaGZj6bu4UJ8209-h8QvUkxMnPVl5aUcLNijsjM8g2dB51LVzBfMAEw4iZbtCKviNunI5xI1lervZveICGLGUsNOd2N_KRI6L-u-wJvsmyudybWog6nXsqpNb8P9vxoDIwvgUdFWjy-ezCUASwbYlrjdZ0jKIPYHS6h5WNS9AGtgMBbalvKp2-wpaJfMQxCI-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=pQwfvFnurR50n5FZuXsyHkATaLMJdN8v-LX1QIvT8KERUXg1vlfPhMKKNGhsb0ml5QLYW30qXhAUYnGLRR175tXiUuYSr7IE42qJmYtnXx1WKtgeVhcZnXosoeIcsH2ocqgQtyqtNgAygWjcGnbRXaGZj6bu4UJ8209-h8QvUkxMnPVl5aUcLNijsjM8g2dB51LVzBfMAEw4iZbtCKviNunI5xI1lervZveICGLGUsNOd2N_KRI6L-u-wJvsmyudybWog6nXsqpNb8P9vxoDIwvgUdFWjy-ezCUASwbYlrjdZ0jKIPYHS6h5WNS9AGtgMBbalvKp2-wpaJfMQxCI-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد، چرا که نوبت ماست که به آن‌ها ضربه بزنیم.
آن‌ها می‌دانند که این اتفاق در راه است و از ما می‌خواهند که چنین کاری نکنیم.
آن‌ها دیشب تلاش کردند با ۵ راکت به ما شلیک کنند؛ ما همه آن‌ها را رهگیری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQGIaE10sFECq8UtntRrAqd7vpF6ebH4qwH-0mqlRi09w7C2Z7z--Nhpg5GB7MSv_YTQbnkCGFuaXq2WQyTESd7rUOUu9SDSFx0Njd7sIxG1qn4TPbjvuEuMZCJAtEGEf2AmjHaAUJaIo9naFhDeA_oI0Fsq-k4MhVmRJD3Rlun-nq8b2wEiOT0G_vxyRv5BuGhOKafBuo8fCbYzDYY3asTWUSZysUj0dOoxac1u-Dbu9-qdLV9n83fjE8yXLwITP5i-gUiZiGEkw_iG8_7rlIPhJx1_FPv_0H8iUEIQ1j0ciieK8TJF8louHLEYiETA5yz2NZovrk-CEfxe3ugMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd2TEldGYrCDZCZMHyPsL0EefnZqsHhO-p3a1AouX4FbduLiaKfa09vv4jmgCf_3rH-ZL7KxqSdJfnz5oYelmKDzv0ppMvcf9iz_BDRm18BOJyZv-KtwueyAjKe5-Vnl0exbWTvTg6AfObFzvJB2DaKmsw7BAkZbms0InC9Y8mTVAJ4GHwDA9j1p7crxcv2O_OeeGlSchBe0fAe8RS_2_SdP581gbNDLBcqyUUw18b8Zp6-w1FmjDSf1-BVBUxhna1F50bmFFcOjHFzccL7-KbEJyT6wGfDPLKLTeH8-qTndIW7WxPTy-ERV9AVeVipul_optNj7GQ1q4be9GaGtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nsv8lx8MqNDtIFtRgWAkWUIacITpODLKdZuXl5btWz11vBWzqWmoF3WXP0No-KK7NyxqKjU990OFa8KHnBHS_wYs-U_7CDYTnV41KV6lCwZ74Odp-S3nN2FnhK_ACZxsbKOFsBfzBWONKVwMSbCvt1as-TpDgNmrmx7oupipryoG1A9bNUd0COYdyISqaRl8PyvjbOlSlE5AufQGuol-NCWFUrgkoZo5aolv-OMTYVN9Sigfn5sXWmOJ3buF__57-qqYsycHKNdEIA1uR2J5LmyIyRdEbk9H10YXwIIxaL0Z6rts1PZN-k9GDmui5lTBOPYsgz-V6DI8HDbpablshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=AiAJJx6raXI8I0EqgPNxe4FK54wuH4_Zk8lZzn5LNFRfe7yTs0Ncx_UHvROLjoE47hZ8y7tc3vLqPPOgT1YQ-OYs3VZS09GMKt5wkM9HTfalY7GnHfzqQgxsWeMZbfqVFIz2RPb41yLRSOmRi_CvyufP5kW0HZNqpcSoB8AhvlAfIvY72T5q7XENHa0Bn_QoO3A6rR31kXl2R_WlhX6L4eT_FV18wNPHR9fx_GsC7Lcg9fyQK3sh13Xhfqk4L-ld1UstaOMehxPsMuGQGk3l1SUp29rJq9yS-1qmcbFiNToWYtQCbiw48yfpQISqUppjAeObaQYXmyrIAZn0Yh4c-BYRvdRcxow7nABZiSSiAxZTDk9mDDondueaZLpQa_4HCI0FheuPwGbPvA8aieqw_AETbxEAwV1uZ4x6rz0pRQcR3ahVhaVLU5driGcTje0NZyhg7DnsfOwY4-CtpR86E35apVW60CqKNboLQRe1gN8c9MPGhLXJ4KnQLGaapPyMitKed5XWLCdIvUu67Vbd9cDmdKcKCe9UUmLZ2kPWIdyjEeycnB-McCij7VxljrllwOQQMbe87zev6cKpxNJdpVFkKj9nhSTT3n2SaLzt0rEriU6abkBV1H6cHr_m__5oQg-fjRkr9QP6SMwpgoWBR44EPDEd3maXPfNoVrc8A0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=AiAJJx6raXI8I0EqgPNxe4FK54wuH4_Zk8lZzn5LNFRfe7yTs0Ncx_UHvROLjoE47hZ8y7tc3vLqPPOgT1YQ-OYs3VZS09GMKt5wkM9HTfalY7GnHfzqQgxsWeMZbfqVFIz2RPb41yLRSOmRi_CvyufP5kW0HZNqpcSoB8AhvlAfIvY72T5q7XENHa0Bn_QoO3A6rR31kXl2R_WlhX6L4eT_FV18wNPHR9fx_GsC7Lcg9fyQK3sh13Xhfqk4L-ld1UstaOMehxPsMuGQGk3l1SUp29rJq9yS-1qmcbFiNToWYtQCbiw48yfpQISqUppjAeObaQYXmyrIAZn0Yh4c-BYRvdRcxow7nABZiSSiAxZTDk9mDDondueaZLpQa_4HCI0FheuPwGbPvA8aieqw_AETbxEAwV1uZ4x6rz0pRQcR3ahVhaVLU5driGcTje0NZyhg7DnsfOwY4-CtpR86E35apVW60CqKNboLQRe1gN8c9MPGhLXJ4KnQLGaapPyMitKed5XWLCdIvUu67Vbd9cDmdKcKCe9UUmLZ2kPWIdyjEeycnB-McCij7VxljrllwOQQMbe87zev6cKpxNJdpVFkKj9nhSTT3n2SaLzt0rEriU6abkBV1H6cHr_m__5oQg-fjRkr9QP6SMwpgoWBR44EPDEd3maXPfNoVrc8A0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=Sqd8asOjtQ7thwNiDzbS_9Si43tAguN2VZ8lZwJiq5Dsq7Eh98nkB_uC3Xr2HXEumtIAbkxDgS3carwKy87GQlnPKE9G23ph15XYgl05YFLsudlJdsoWfOfBup_mUo8pkChW8teKcr2ovYuX0IsWndkvlOqE_Ozw1r0DySQm2FjcKP95ZZEWpBGo9yGcZeottexZ3sOdplvDardSFA_GPb271ev9QQYtmIwdApv66sihKc-tIkcXFw8RiNLMhIXwN9LE-YcsxJvZv3leF4sf4L0PZ1mhr_pGTXfIyM3pQ1Ad083KkjOZTeZumGoQ2oRZWZgUzt2nSt4SDt1Fx1Mfx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=Sqd8asOjtQ7thwNiDzbS_9Si43tAguN2VZ8lZwJiq5Dsq7Eh98nkB_uC3Xr2HXEumtIAbkxDgS3carwKy87GQlnPKE9G23ph15XYgl05YFLsudlJdsoWfOfBup_mUo8pkChW8teKcr2ovYuX0IsWndkvlOqE_Ozw1r0DySQm2FjcKP95ZZEWpBGo9yGcZeottexZ3sOdplvDardSFA_GPb271ev9QQYtmIwdApv66sihKc-tIkcXFw8RiNLMhIXwN9LE-YcsxJvZv3leF4sf4L0PZ1mhr_pGTXfIyM3pQ1Ad083KkjOZTeZumGoQ2oRZWZgUzt2nSt4SDt1Fx1Mfx4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نخست‌وزیر نتانیاهو:
«سفرم به آمریکا فوق‌العاده بود.
همیشه درباره موج نفرت از اسرائیل در آمریکا می‌شنوید، اما احتمالاً کسی از موج حمایت و علاقه‌ای که نسبت به اسرائیل وجود داره براتون نمیگه.
همین الان هم با وزیر دفاع آمریکا،
پیت هگست
، صحبت کردم.
اون یه حرف جالب بهم زد. گفت: "توی دنیا کشورهایی هستن که اراده دارن کنار آمریکا بجنگن، اما توانش رو ندارن.
از اون طرف، کشورهایی هم هستن که توانش رو دارن، ولی اراده‌ای برای این کار ندارن."
بعد گفت: "فقط در اسرائیل هر دو رو با هم می‌بینیم؛ هم اراده و هم توانایی."»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVZ4orIcTM2D8Uls3eyfbx68MSH_zCchVEJFomQajeY6526wZl5Rg7UvewnmndwIuZNF-I7dUKIcrQlXpcLlOI_x-iKOB9WpojGntWpKAQHJoVNb7Sm3r9yRH8B549cm7sMYE507jBc2wlxuXOSo2CVaed3OTsNyLAopcCqL3963O35pkro_n9Im10tRHOMFT5ZJ9jfm2Yg0Kx_8LEBNvVkeb-1w2_ItcNOKyr34ORC9uPG-GJwdbF75IlN6n0AheU2QCluhlnddSuely1f-Yiko0RNr6DuhFuBWcvBVbVCAS6DfIPnEc27tM9Kva1jlVcrmWPmOCXjb_9QRpAakFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=pIO-g8SsUZiAMD8BsTX4E7omT4HOG3ytFn2G9He39yKBKew4khtTcVmOxI6CeXrOwyc8g7TgpP4a83jhq0DNrdTHwiknuwd8gVI5jXhyj9cK1HS4um7WCvKb9s63xgwOgfQ28mhuNcMjGqt_9bghgy9BZL_5uZGG5ZK30zi53vJDG6VJ7Nphs_CTXryRHh4-vfbQzfakzJixgxp-cfE-ql8q_yozWWzttcTvgx2y2AMmnWqC4auUmLTgLl-5mHcsikrC4gAGj9d3s7Srm6OcBADrZMP8NVD8S3upoC8Ei4xrD9uH8N91wDSJUwWOLFrbNv6DmkBsstZwn6F0ms4LXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=pIO-g8SsUZiAMD8BsTX4E7omT4HOG3ytFn2G9He39yKBKew4khtTcVmOxI6CeXrOwyc8g7TgpP4a83jhq0DNrdTHwiknuwd8gVI5jXhyj9cK1HS4um7WCvKb9s63xgwOgfQ28mhuNcMjGqt_9bghgy9BZL_5uZGG5ZK30zi53vJDG6VJ7Nphs_CTXryRHh4-vfbQzfakzJixgxp-cfE-ql8q_yozWWzttcTvgx2y2AMmnWqC4auUmLTgLl-5mHcsikrC4gAGj9d3s7Srm6OcBADrZMP8NVD8S3upoC8Ei4xrD9uH8N91wDSJUwWOLFrbNv6DmkBsstZwn6F0ms4LXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=JqfZwoyqz9ij2hXw7hNPTgJmnSNFzPWbLoi_dkN0RmvKKMbbsfri1nM1wMBPXxmVXWnpuZiqSz3Oaz8m0haLIzXRPe_Eho27_wNlyxPTufXOjZo6XRH0jPp1L-OAIkdZpbFn5howeQk5bqTqfi6WRrJcBoUiU48EI9SZMS00pkzfk8_NwrvqzOwgZVK9UFae4saQvdxcvbfMPyLnSjjB2rA9g9l3XuqfH6341BQ1dP_n3orgoag7wTHuH84g4-5UqrN5o_NquFT84WDbDJM-VNJHnVEKV7j88YZ9sn7H3usNdudq_0PHc19_1RLDLqVrsol7C6X-JRvvO1j8muqHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=JqfZwoyqz9ij2hXw7hNPTgJmnSNFzPWbLoi_dkN0RmvKKMbbsfri1nM1wMBPXxmVXWnpuZiqSz3Oaz8m0haLIzXRPe_Eho27_wNlyxPTufXOjZo6XRH0jPp1L-OAIkdZpbFn5howeQk5bqTqfi6WRrJcBoUiU48EI9SZMS00pkzfk8_NwrvqzOwgZVK9UFae4saQvdxcvbfMPyLnSjjB2rA9g9l3XuqfH6341BQ1dP_n3orgoag7wTHuH84g4-5UqrN5o_NquFT84WDbDJM-VNJHnVEKV7j88YZ9sn7H3usNdudq_0PHc19_1RLDLqVrsol7C6X-JRvvO1j8muqHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbBWdhpFa5pBcc_mAUpD7EiHmJas4RURpDe4_TO_eow61If9lkK-aWkcOxkkS7rnP5CXj0Cn0F2ibwmUQLJF8-H_lQ2o_zO2iGEu-2nD_UGgb51y_0waBzvA3PQfAtfcOAlwzaFqeQ46WvwJU8pPX8-yd-IxUNqoL-MbPaqO_MguCQXachCAUrTebc3QvTrDAvH3f_cWWOWc1Oi-Q7dTpCo7R_91QaTI97dCheamOG5DWSR1ksrV2ghZeLhvjH_GD6Zm0Gfms_oKNHXqsi7-CtD2wcg9hMJzPqYZZuZaPqZ3RbkTSZ8m9VwxrB6zyiNGfADqg_7THCF_09K2LDWq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSTtj9gmGGk6xKfeDWENNUTjuPrisFTMa0bGSGEVY_yQkhHwgsAP7YD_CY6G6HMIcR1JlD8GVzpsmXW3wsOI1fRJ9JU9bQ3reCzYkdlYo1zUHAuXZxFbekEzEn5Sp51WXcjMXDIKgPHt3HTN5DvmBuTUle_ATHDkmJdH5HWbWD7hX-OImTAtVIGxfCepozKFozzNouLNluSm6oDiIhHJkdvQ-h_XH2JqTPrjSBhO6ju7EPvNdo5a_Eq-168FaCgOzakZE8fPi6pYTW86G1KTiFqJrbXeeXP5OjP_bHAL2wz9x_CGUdlpLMpvyacm3ny3ZYv-zkaTpk2v365IxPXfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvnqatFuMc84HI5XwuOQFJTDpyipvE3zVr3baigQTJ0ksu3QeAa4smGGlxV7PBXwDdjRx3xgm4mbtuywr4eHtMwjRGJx5csN_VXDWBfRnORUfsf_fUBK1h-oVdTxAlHDAIS0s5DI5pE-EhCJX4MtOfOUb8hvhiit9hR0tEJwWjchLcUqIZLZ5mJN_UOMjyE7FZj8FLN8Qm07eugQN7tUFp8lo9ctsAUuwetoXsgiwY7FOPwDcwNMjyr0uzgc6MJxLPokwKfkoG9beqEVzgAxWsvZH2ugd-zoKc8NXGL3GoJc4aRFMeIp4n_pmnNUq5VTyn0bwP5zcfd6qFsD2NyX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNZU_0gjW_nwXStObclEaS9pCeM6cNJIwm3cB4O_6rjnDN34InRydo1z8-oo9bIpmok9QQ7TlOsNrSoObGBkEWQ0QA6-Q9iR1sZlH7VsQBgDMGXyTcD74DWjxx1ZhW9C5P92rEJhRM_2tnO5dcR9BDhrlt1Pnuo0cmdgu6Z4Qz9CzOrjdVTDwKTxH5t2tQN3VufbeovhMyCmYv1MS6lNxgZEJzr-vmNTqpbNXvKK5J9GMnrf0Ru9xm1zs4pLRvxPXARsdzzesTZoa2CIo0WPSqIr_s7b7uNrSFS--6XN0_IOIqLe1z6eaz6j45NhsIy8t4Fcg6Q9Ie4nMDyt13TjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=uZnhzZL8iQfUZH5qdKcdEVTjqe8l7LBESUIoUXJs9OwX-8Pr7P1iSnbfaa6dAJ5yJUcw6tbY13LPpLjDm9nprdIFHQMxwamUqFJWaiPGs6unyUyooCRkluSN8DoAYDsUH3FwhuMZp5xrHtCXGTVlCikYjXTWx6UQPNy7Xlpf38J1FCp6DaQgB359kfj_2vx8rD6xcv-23d0Gv6MDXora8F-ZYP-BqFuOh6AcWGzOoYs16tNnKmwNdz17nQlNlMFKMrHCIyCjyxLsFOTn5HDPIiG1OLl7k8m9u_OIJgChACaBcoTGRwA1QeqtT7biX8_v7JBs22x7JaGauFDdCaBAaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=uZnhzZL8iQfUZH5qdKcdEVTjqe8l7LBESUIoUXJs9OwX-8Pr7P1iSnbfaa6dAJ5yJUcw6tbY13LPpLjDm9nprdIFHQMxwamUqFJWaiPGs6unyUyooCRkluSN8DoAYDsUH3FwhuMZp5xrHtCXGTVlCikYjXTWx6UQPNy7Xlpf38J1FCp6DaQgB359kfj_2vx8rD6xcv-23d0Gv6MDXora8F-ZYP-BqFuOh6AcWGzOoYs16tNnKmwNdz17nQlNlMFKMrHCIyCjyxLsFOTn5HDPIiG1OLl7k8m9u_OIJgChACaBcoTGRwA1QeqtT7biX8_v7JBs22x7JaGauFDdCaBAaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0gFG1kLZBDHUFyjTr84WEftxCRtiwVsocnv4MCVARsr66Cs1CQ7SKkIXTPdmiFcT7H-OpoF8PozZK1Iz83ZX9Lp0JOtYmYWI_5kkDQgmq7MIQASO0j1-cqW6bSluNprc_DlZiqfJCf6MWzqAwIcybx5DFSwHRXCXJWC5iS4x-Mglq1akgO8XjQBIz7Y6y0YEfLQL12WNk2HPKhXiSCMp43NuY1A9ZKZwPP2pNm2M5fQqgQVwh1I38FlfOl4FTYMbeMhi6o88tVigaUS7rp9UE88oVuWvP6eqJVwuEEO8xCJkVr5MvCHTFmCCaAN6ufKgiPD1jjdZKghvtT8Lffm1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=U_CY1P_DjRs8bpAbU18_IDd4gin3aBP5vzhL2WWNgzFqw2jIWDz52NoBGycXVXAM_IErcrGRi_0NavLJU935MPsqNvVBy7qdmhAzOadPnFhybdou80EhQxVsjs63A-DgziZhllOmLHw7jxs4Wf8GpPwHcSQE3jBZYhFQ64r85eL53_tIluTOlow8N_Z1-HbHVknmmDXTYWE-8eLx-FgMxMvCYcW1CbFjSeHAg0MF4PuSzpwr5sltgsvnjy-mbjvkrb8M4tyaVh-85GkFJZRoTy3Dop7YG84Xm3sKRkDDIKH0cLb_rDR5KC5Q4Dhaf6ehS32JaXcGrj4HutufWYRYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=U_CY1P_DjRs8bpAbU18_IDd4gin3aBP5vzhL2WWNgzFqw2jIWDz52NoBGycXVXAM_IErcrGRi_0NavLJU935MPsqNvVBy7qdmhAzOadPnFhybdou80EhQxVsjs63A-DgziZhllOmLHw7jxs4Wf8GpPwHcSQE3jBZYhFQ64r85eL53_tIluTOlow8N_Z1-HbHVknmmDXTYWE-8eLx-FgMxMvCYcW1CbFjSeHAg0MF4PuSzpwr5sltgsvnjy-mbjvkrb8M4tyaVh-85GkFJZRoTy3Dop7YG84Xm3sKRkDDIKH0cLb_rDR5KC5Q4Dhaf6ehS32JaXcGrj4HutufWYRYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=IUTtPD4Xl7uvRyS80mjOrihBPL8An0uq7f4TPB6XCt7LRKkWbJyaKTd2OchEG335zIZY0HXPp9yKk6C5D_FBSjQI22pNvlMygstFS7t7PfUjfaz1cRaOKaAOKNF3Dv3AUW786lRz7DTp3_kbHPUcYLVW8H03jTi3Co7blWnWW2BxhU03HNsZF0VY3Muc_ARQ_MhKmLWe5iluv8iaA78ZUKxXoyWQ-oV5E5TuzmjK5xGPSVpnRHqXxp4NGJy-82R_5xwJB3QCd256ekKI3H2iJYo8w8kT5MvKETEBAoW5sqHUdaSkXxdmPyWhfUxSzVHaIJMeuOWTJpYWCsIC6dZgWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=IUTtPD4Xl7uvRyS80mjOrihBPL8An0uq7f4TPB6XCt7LRKkWbJyaKTd2OchEG335zIZY0HXPp9yKk6C5D_FBSjQI22pNvlMygstFS7t7PfUjfaz1cRaOKaAOKNF3Dv3AUW786lRz7DTp3_kbHPUcYLVW8H03jTi3Co7blWnWW2BxhU03HNsZF0VY3Muc_ARQ_MhKmLWe5iluv8iaA78ZUKxXoyWQ-oV5E5TuzmjK5xGPSVpnRHqXxp4NGJy-82R_5xwJB3QCd256ekKI3H2iJYo8w8kT5MvKETEBAoW5sqHUdaSkXxdmPyWhfUxSzVHaIJMeuOWTJpYWCsIC6dZgWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPtjR7vMawViEWJyencyl8tCVcxQ9qSjAne1WJEM7kiJDvnHbR69W6i-ppQNbMJN8WyeWj6UODs-WjYnb76vvS9HKDh1lovgL7FrLDNzfbfK3x_MY-8ejqFPZTd9GMtKvFc7GGPVaLXpanXeN8Z_XUlH84MY8AYGyKn1FSmFKSga_qw0zbprGUcJVUilrCLI1gZudGp3IIEHA8A1aRbDBJDf_voOys81tY7FkvoYdqV3tL-A5l_XsvrqZ3n8foI1hasnJiOZCAd56oQdzoJm6g4GiYHpPFdYFe1EqdNTL8ov_0gEWfHFk4ihw6ouWZrOsHbEZANt0p2e0Zyx0kRrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=bKuGZ8fWB5rXv8EOyeBDrbMWuMV2qtyHFjCUeVHqT6459ML-IIjcEfLkzQ3oT342ucbQS3RygZvqiKAh5RN0y0Cr5u1rGyutQ9HIlNrG6sMJW3jQy4XZvlIjtm2ECv-F_8iZqtOBiflABxt9RrCBkQ_eWuxUWeIh2AUmvSLtFa_ddZhMOQBKtDQUddKJLsDSC6k29eyrYAeQsfENBGlyAUR6HmnPputcq67dW3f6CdSxpOLWZ6Xv-S7LLlnJmz0982C-J7KD3POzTEahoyJJvq2mMv5P7A3px8HfP53qynlmHiEu0_iK-DZWW04PrXlYZ4IatAGSGpIfW2wQWUhZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=bKuGZ8fWB5rXv8EOyeBDrbMWuMV2qtyHFjCUeVHqT6459ML-IIjcEfLkzQ3oT342ucbQS3RygZvqiKAh5RN0y0Cr5u1rGyutQ9HIlNrG6sMJW3jQy4XZvlIjtm2ECv-F_8iZqtOBiflABxt9RrCBkQ_eWuxUWeIh2AUmvSLtFa_ddZhMOQBKtDQUddKJLsDSC6k29eyrYAeQsfENBGlyAUR6HmnPputcq67dW3f6CdSxpOLWZ6Xv-S7LLlnJmz0982C-J7KD3POzTEahoyJJvq2mMv5P7A3px8HfP53qynlmHiEu0_iK-DZWW04PrXlYZ4IatAGSGpIfW2wQWUhZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/en9YqlWWDxWzLDtIslmXuAjPS4ZdkqQnOapOvtUTCrwJ0aJBx3QwodlxqXupJxo8hvt-xgT2PTZpKjG8Q7CQRBPpPAH2xKRwVNv6p5eaMOXKzD4gU3xsdlx-dn9xQAnD7khwe8K4QG-Rdco6kPv4H-IUt-wlb-41YfC8js8jVTzNMIcBMc6IfRNWDQFrLE99jJT5bd1AChJBAGpdyBdVHMg9RCcCASe8lYSiVsh8tnjzj8rUrOXs_uGuELfUICj8tMHlsmZCVeYuDBI87aSBuHdF5jp0SPt8D1da29ssffOFr9AbdtAzU-D3_GRGf-N_x0yk65QJ7tVK1veeI1PVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZgj_a-IvqDVF6K3I52jGL5_1MnD7llIr0a4ZrDmHZxk9hUdV0nPIjpOGPem9bqyqAoo_69vo5icLj4c0gHR-afNCQekeYDweP54j5uE8HQjkGiO9PJaIZzWd3ZgScSLBfjgPToWjP221OdxOI-oY_-HgrSvCFrxVX2imZC69haK25Lcnao7rYXN2woW4GfSGWjHMaEj8Rppb1dt_A_Rz0D7Fy1DJQPAlc2JturdVYMsqjEK6xmi33-JdFGZ7SVtOUnSBw-x0G1qzIiXHJYvZVXadEv78g0K69zsiP6mB5gCxGvxAHpA9Z4QNCxgCgBdVBCh--m2r2CaRucEcavX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=FFfcPVVOaSAU1CuIkRkS9gd1Q7N1-hY81-75oA9esNzo_3Yd9a7qa8u60jgpMu-0coGv6Ovje_YkcPUzZC3qjM0JqNycPPOednd_qEh-iRnaGDiPSvz7Aj1Bw_3McN3ZTlLNi_JtPiEwZ4nqzuy3yiN07ENdXDCCZTABFLECn3pgzioireJ-pPdmWlGU6JrmE9x0uKS5M5nL9jAW_EliyFeYKwptSB2EWId01PJLhik2J8zJZxhyRrR_tgUcsOTDwd35Nx916IqSDfFL4zD2pNhRAxbk165ugozzJk5ezquhXTfmn6HPbCbnbnsnyIpDgfQUggz71iGKZkgnoiPKcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=FFfcPVVOaSAU1CuIkRkS9gd1Q7N1-hY81-75oA9esNzo_3Yd9a7qa8u60jgpMu-0coGv6Ovje_YkcPUzZC3qjM0JqNycPPOednd_qEh-iRnaGDiPSvz7Aj1Bw_3McN3ZTlLNi_JtPiEwZ4nqzuy3yiN07ENdXDCCZTABFLECn3pgzioireJ-pPdmWlGU6JrmE9x0uKS5M5nL9jAW_EliyFeYKwptSB2EWId01PJLhik2J8zJZxhyRrR_tgUcsOTDwd35Nx916IqSDfFL4zD2pNhRAxbk165ugozzJk5ezquhXTfmn6HPbCbnbnsnyIpDgfQUggz71iGKZkgnoiPKcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJd7ucMVO6q-xIb-nVk9Uvrqv-NINUuTenqSeczhI3AmYY0dA7DYnp1HJLcWJjyCu9koObv_zR8yJqNQPTVe811xk8H3dq0HUZXwzmBUBYLEA-QeN3USRWotGtNX5JHSkDMWTNzg3VAk5AUVhrDcTTyWP0XF1Ia_a42m1XAK2kOfRpKkgpuiFYhJj8aqund6p79l5Y7laoL6524ZI00K2OP3O-4gPeZwbEudrP8DgKOQdr5fK-szt16m2XnaRWXd6KDvdAbPM_ZNIPoJwB-CS4r4iEHpuH9YKTLYnLOoi2jMbGITVPiW84-H7jMK1hz5iL9-_3-cnFA7GoIg9mjfXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSipnG5EXq5NaJLMf19KH4R-hePHSVNiNEBdAtXPaCBe0Kg4sZR-a8mMyu1rdFjVvNnhpO-FonpMKMerNLE9aNjEb6no5z85_s5bYMtIVpGdhc13KSndfm6Q3B_16u0P4XIa1CdXoPlwU0LDu45UnXbUqmyf1lS83OMUBX2sYanLeaDx0MYe1IBiiiPaewuvR9LTWUE-hl-Mj7tZHTibi5qFxZxzRCaCd_nHhsTX0gWjfELUv-ywMGTKVVGEbk4xj8Lz9azXOSJ2WImjK9w6B-74MKflvwlLXQf9rwrauP0qCEuXBBXHsT3RQ47Sf-qayxu7lHQdfLB41UIT9PDugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=CsnJxEDdeOgEOyM6YzJO1w6FG-dgUW7-lqfcvA68z8qe7NSMoFnrMF0DQwoVXfw7xeDrJGkW8kROTgoNyac9V6f1tEIsGIJHIuu_rirokKs3j6VL1G0fldiOjDWoyo3fu0OX04Riv52oF_H93_4nV8abUb7sNaHmBdroSEXycIWGiMdB92qPQRXyC5A-4rWLA9B6BkpCtqwjHCmOMu6HIq-RvAmT2nhmlzJHRRhASHxxEY3XkQcu3y_wpvWPWwFiTnlkLSPrDJCGcB7XAFVnwQIh3LtkspBp5IDFejyxpxgSIx4IaSRQPoFgefPC7BcOWYik9GdthqqCCE6fB8KWHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=CsnJxEDdeOgEOyM6YzJO1w6FG-dgUW7-lqfcvA68z8qe7NSMoFnrMF0DQwoVXfw7xeDrJGkW8kROTgoNyac9V6f1tEIsGIJHIuu_rirokKs3j6VL1G0fldiOjDWoyo3fu0OX04Riv52oF_H93_4nV8abUb7sNaHmBdroSEXycIWGiMdB92qPQRXyC5A-4rWLA9B6BkpCtqwjHCmOMu6HIq-RvAmT2nhmlzJHRRhASHxxEY3XkQcu3y_wpvWPWwFiTnlkLSPrDJCGcB7XAFVnwQIh3LtkspBp5IDFejyxpxgSIx4IaSRQPoFgefPC7BcOWYik9GdthqqCCE6fB8KWHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=OUXI4gIeOXkALFS8_qKrw8oZE5giHW-Ez4l9gUFz8fkAhaxLGyuIPMdAKffyMkt8zqYTlqGGjONXhGnH8T8COpIZKXkYcsr1Q1w7xaYpAjsOT9IlXmXVrWZIdasY1p1dh-WSS2zXQB35c9HONtd6Fp06v_w8mI1IZ0lOfEZyfPSiufqJvZejgTmLiLJX-aMTu5GYzudwBbp0jJ8ATZINtllwEHecrw9NoB6oSm8c7X4_u-6Mtlyxy3uyy-DqA8R1zuDLviCMNpxkKL5Yf0hl1tT3jxNAhR-4HjXFCw_MY5LSI6c29U9q26UgxkPiOBESJtSl7x0VECUp2hAzcuASSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=OUXI4gIeOXkALFS8_qKrw8oZE5giHW-Ez4l9gUFz8fkAhaxLGyuIPMdAKffyMkt8zqYTlqGGjONXhGnH8T8COpIZKXkYcsr1Q1w7xaYpAjsOT9IlXmXVrWZIdasY1p1dh-WSS2zXQB35c9HONtd6Fp06v_w8mI1IZ0lOfEZyfPSiufqJvZejgTmLiLJX-aMTu5GYzudwBbp0jJ8ATZINtllwEHecrw9NoB6oSm8c7X4_u-6Mtlyxy3uyy-DqA8R1zuDLviCMNpxkKL5Yf0hl1tT3jxNAhR-4HjXFCw_MY5LSI6c29U9q26UgxkPiOBESJtSl7x0VECUp2hAzcuASSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCjJ9KTSFB5KIw47M2FYfudsyBbv6_PBVjplYvvuy0wQs-CgpkZUqt8OkeUvh5bPvtEBFemdoAQOq_JJou6yHTyjfb0KZdXAvzpYZEgyLoKyILawEYNjjJa6UiFVDnHJr_bfOR_D_3UoDGWD34GJQYM5ZJra7hUcMt0p3CIFzu9mVzT3gXuTWv85JocNkDS-2KbB_PWN-u0DWUqSoO6N9Il5Tk9_Dq8BNZY3O-QKIqNzt9iUmgPOK3araD4iQO6p1i3Jhz1fEFBxJahYXkGNqKT88yvmSCC9pf805nZg4tL0zaJs43cEe6NW_xIil1oPsRW0N4Gl_BYhy4FMnJy_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=gurhfvRGWBME-tPhj0BBohoTOSj9-yfl7smmhFirBD4c72C0drKjboykbT4QKFMT0os4s5PlmoWPPBpdGTNjvOuZkUvqgh1_UaBcOxK8hap7ogEdjbMiE3rVnBi6PREsP0SWyT6xYBPRnHHsWpcfpA27WOjBWYVI5GEkcQifI030JO_aeeb3QnksUtKRFC5w8OftBhOZsvDY7D0SgP47o_qIdlVaqqx6y850fiRqT2tpH7qILFe252bIggPWCRZS0actOxFJWpU1i-hyMGpm6fflV9ohgaQRBTIeT-Lger6T0E80UtCBIDJIT20sAfOTo_qQIpHOAdE4ndG9QceIfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=gurhfvRGWBME-tPhj0BBohoTOSj9-yfl7smmhFirBD4c72C0drKjboykbT4QKFMT0os4s5PlmoWPPBpdGTNjvOuZkUvqgh1_UaBcOxK8hap7ogEdjbMiE3rVnBi6PREsP0SWyT6xYBPRnHHsWpcfpA27WOjBWYVI5GEkcQifI030JO_aeeb3QnksUtKRFC5w8OftBhOZsvDY7D0SgP47o_qIdlVaqqx6y850fiRqT2tpH7qILFe252bIggPWCRZS0actOxFJWpU1i-hyMGpm6fflV9ohgaQRBTIeT-Lger6T0E80UtCBIDJIT20sAfOTo_qQIpHOAdE4ndG9QceIfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=ovLZR91LeOMZ3X98zHjErWje1GRW4RXj3blWDjDfaDAOKlrQU4T4XEQ4qNcLhfm6cSGJu1sKe4C8d09u9JRGaIrKnO8S1FxGuSo0l7wdukwOPM41fpWDMa04tgrEJC1u-vdN-Z6jLMUwxmrL07hfEk4xJ5qWSCw5zTKIqbG9lMfuDTMU7e_6PPdKXMyms0hdbDQRuMEDZ2dyct-cuYwA3GEaMIOAG0XmQjr8C8j54v_JvwLGBmAZf5p8ny57sPDiqb81gKpbHHYbIMw1egIZpR9UIwGcC165MyoTIeVuwnhsX7hlD_Qi-9JTiC3TOn48Mfsx9AteyqYbeUd57NfwYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=ovLZR91LeOMZ3X98zHjErWje1GRW4RXj3blWDjDfaDAOKlrQU4T4XEQ4qNcLhfm6cSGJu1sKe4C8d09u9JRGaIrKnO8S1FxGuSo0l7wdukwOPM41fpWDMa04tgrEJC1u-vdN-Z6jLMUwxmrL07hfEk4xJ5qWSCw5zTKIqbG9lMfuDTMU7e_6PPdKXMyms0hdbDQRuMEDZ2dyct-cuYwA3GEaMIOAG0XmQjr8C8j54v_JvwLGBmAZf5p8ny57sPDiqb81gKpbHHYbIMw1egIZpR9UIwGcC165MyoTIeVuwnhsX7hlD_Qi-9JTiC3TOn48Mfsx9AteyqYbeUd57NfwYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=F-Z5snJbgCPrP9EpHm_20_oYPCUOBodcI-z60CQLAEOtP_s_s9QDKieNhdJG6CEZ24cJFxELG6QSBA779WXZ0yPNUGWd7Uv1F65WSEmwgnvUleW4VUDelatBVeQmKgQy3uc1KhqQeG2xtNsTMj1dx_70QbDhoZ468o2LEuSJpb48ETIxRCnwEeGX8MIQ06jacbP_vtVycwMAGeM06ChlCGyow9kB6HDDdbjfCh8HEtNHudDIzf1LvimRjeyDzD7BLAdL8wPjqT2xkCSwBvxotOZq9Yiq2jGwussh22T67UL62wMyOsTp0iHGHhatDK3KzgecV9Kzbm54HqZFzzC9BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=F-Z5snJbgCPrP9EpHm_20_oYPCUOBodcI-z60CQLAEOtP_s_s9QDKieNhdJG6CEZ24cJFxELG6QSBA779WXZ0yPNUGWd7Uv1F65WSEmwgnvUleW4VUDelatBVeQmKgQy3uc1KhqQeG2xtNsTMj1dx_70QbDhoZ468o2LEuSJpb48ETIxRCnwEeGX8MIQ06jacbP_vtVycwMAGeM06ChlCGyow9kB6HDDdbjfCh8HEtNHudDIzf1LvimRjeyDzD7BLAdL8wPjqT2xkCSwBvxotOZq9Yiq2jGwussh22T67UL62wMyOsTp0iHGHhatDK3KzgecV9Kzbm54HqZFzzC9BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=VGrM880oOkVvgSwX0SjwDZCMHdH7LMVKbm6h1FaVFu86iisjeCA7-WMlEJBE41H0xCWsP-dLo-uEHOMDVdK1zqcZmKzLtbAwXt17uhesJRdNLl3txTuDpI6936mqIdz2suBE2KVIznZGaEkQZNLfPtdtZUgfvwdXXnlESi3evQsSxapSOP2EABte2j8cjoPNGWXoSlZjQEe5XcFmHZsWX2tluliRLHC0bAI2nDnpzmCMlBz1GkVnnKvJ2Q-JSYr8FBABYZ-4JnNPwvx2KeyB7t3q2v1iFgLBXvatMDjL9GJAFTk871VQF4zRUwM7deARc19n4IsIxFH-C44eK4PRkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=VGrM880oOkVvgSwX0SjwDZCMHdH7LMVKbm6h1FaVFu86iisjeCA7-WMlEJBE41H0xCWsP-dLo-uEHOMDVdK1zqcZmKzLtbAwXt17uhesJRdNLl3txTuDpI6936mqIdz2suBE2KVIznZGaEkQZNLfPtdtZUgfvwdXXnlESi3evQsSxapSOP2EABte2j8cjoPNGWXoSlZjQEe5XcFmHZsWX2tluliRLHC0bAI2nDnpzmCMlBz1GkVnnKvJ2Q-JSYr8FBABYZ-4JnNPwvx2KeyB7t3q2v1iFgLBXvatMDjL9GJAFTk871VQF4zRUwM7deARc19n4IsIxFH-C44eK4PRkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtiQPabWPd2FkgdqGulVLWIKAWDWK-T2ZpqDudkCo4XnGYYTmho9qcM2Z_VL6rXF7lwqnsfRbPARZRbBlTctvIlVLZ3Sf9vb1HxAbpipNt6_YuiorGllDUsyN3qb0ogNpDpG_QhMLb6ptWfujKlQjQjGzGGsIXntO0fhQcPXjcW2INls31t6I9QRFoFY3VuO2WD2ehr7TPybr2OYC-7apSfSy4Bq1vY8hJItYR5R8ccR7dG2gTK7YBRx6Z0LKScyTO0J2o3pXQZYmh17RMVhZ_P4kGbdASEbkYe9R-kgyN3ZfIug0CNoEE2-veqpvD39E43wIvbimysmPcrd-R0JPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l30z6CCsbuLroLth0prZFee2oNaEwa5gHnP6Fl9l4VKsJh3hEYaV9TcpObUo6t5cbgQx6tLSufqT5j1EyhYLe6WbfoJInkMuMHstIRh0FIHCeqb_f2_2iprTIzvRauqUb2EdP3SJwrQdfSc-ZT_QgT6Nr_BOJLxfusl7biRv3ps-lRQiQPJpmrm_Ihqa918PAwAEWcj9R68fRqQDVdC_7X4CcgMuWa4LLL4Y1ArVDDHBOCLDpm85iEl5XlM4snDTXIxOSec_lOYEZT8xaOKv4pidti2F8SUej3zyM7XjnSQH7rmJ5PaQu134xuegO10RLavxekN8_HsmnCi2aGL5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=AgBMxL-iRoUgCT1R28F65I_o0cM7jFXDsw7y95c5n2ikbrRkivJfW-PnTNWs-hhJTSM0-Lmx8aHHnHORsEcoZZU6u-cJuiTfRmFXvTEpkXZKLXx9cEwoMwYAGY1XHbiKOwgtabJSkMuGaGJv1TV14H1teaCCA5EpBsDbUiHtUYDRwGSUSoxlsmVo1XH3jiNVkwN5Wx5CQ0VmOio5RMmXFk6IxzoM-0mjipFcNY5OstcyF9seG2R9LrpfOLMhf9kbEgvrpZreeSXiDOPZ5tmrEgE9AuOwcQb0K5l2wkAsd1hO3FNugFmWDZLP8ZgRc2jCNKSyw-TAQA547z8ualvYNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=AgBMxL-iRoUgCT1R28F65I_o0cM7jFXDsw7y95c5n2ikbrRkivJfW-PnTNWs-hhJTSM0-Lmx8aHHnHORsEcoZZU6u-cJuiTfRmFXvTEpkXZKLXx9cEwoMwYAGY1XHbiKOwgtabJSkMuGaGJv1TV14H1teaCCA5EpBsDbUiHtUYDRwGSUSoxlsmVo1XH3jiNVkwN5Wx5CQ0VmOio5RMmXFk6IxzoM-0mjipFcNY5OstcyF9seG2R9LrpfOLMhf9kbEgvrpZreeSXiDOPZ5tmrEgE9AuOwcQb0K5l2wkAsd1hO3FNugFmWDZLP8ZgRc2jCNKSyw-TAQA547z8ualvYNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gD5OYSFqm3jM7t-LZUsPNbi1pls7WXiTDtUDB6qyssPuzLUQRkMld3ffYHsC_DGKyWNVgxx6kMwDzyH9nRB99-NH9nuHonujQF0n8YEuVDNho0tkMWmypEdWSCvp8k26WmTo23_5lgR14E-NIUxrJ_GR_rlEKFciIFbpgO382apHyOWJ31vOQoX9RltbzTY3tqU7UvWWghKJDyDt_TN4qzscIXHNAWbzfpxQRbnh6hfWmbZa1Uiqgm-ZEBcfFktFR54IRGI9uszc_cwPzfyFvQe_12FORht-jf3sT1N6sFygbF1A8xqi4OKT0F1xpks2qh0KQfCMoMSDF3EpWsJ3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbdaFOOL6RlPFk15GrP3tnsfmhjjUyvhdPr22-G5xHrHVirSuATq74nDmib0U7aSxla5lx5lm6eobJyTmnthzTgObo2czBUI8U59tWBPiu4ovaYs2jgS4XaL701NaecK-6-vHdEcQ2kTfxg7OE8s84t7bN8k8wH8IzUvj9EaNPIbdiIUajbsLBHXP1Z8SMmdXAPxBTy7cn0fv2Anqz-FZFyPTxml-WSo5zDNeGdaIzp-sRThVpIgcEQwAgT3F0VpjbQQvBX_xwE1zpn9EyxKBalAjNe1Y3py9MZmfgAI8Qzu5DlTsdnHfEIPhYGSch-r51ka6004ngL1uYDR9itYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ehXWV3SNM90Lj3J3XMfBlTj4fS7UxacL5UB0xOeghHliUEyqotyOks1IxulIxsqO3GIo8jjaBT9Ewc8ZwALkrXUedJz0u1zffisLjrjbZH6laXfVWUCCXOfMr6cgkDq258CWXHSLUSv0NY3KXT-Ox4XCFHTluvLMpaLxXq6YwQRWokj_IeTdOKnpGxseHMq5FNmciP7Fy08JZkysjOA_Em8fnVCFKQG3i7iBgU_KhnqIATCKHP5soKn4_kA__ICqGkM4tblxnxQ62z7D75HBreYBWE4rqQ1ulIq1OttovhHY7xSekkEIymuZFxJbHxKfqz3XQ6HGt_XX_hwE8UPpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oQypDYiUQd6YsY40K2s-yEEUZipxCvXJvDu8UMDqjiDHkPFDNeGASZcFiIM-j7FIBJACaW4kmZbKtXWt2uKa-OygS_KCpIAs7CmRJASKbceVzj_S_HNuZNL0jQKu4MOOPT5jcYNs7v-hG8n1jkWQPNblNQlQ_0sKbCMbi2MTXlL7fwJSk2H8iXiDCNHFUV26HRY1XlLUXWosR-0XyArxGVNuFz3jT_fX-dSzlRXqzG3v7h9hJjv4tNthGHXtmQIuNAEYFXmmv9ogesUcmibQZERPFXVhkdVMOEaP5Hteb4tWlXKwl11dYZPI-n6VKWgbfZ4N4TGHUl2nrwirW98C7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=t3IIEsTR0pplgP01r9l7_xxLYWgbIj1auobpHT9BhSmX6HAvntEQR0rpqwd5sEYFv10nLYj7DNnC6HSb2dXFG6M1TFjuZ_KYWDkctuFjxHbvK_1vuVwRxdMRaI6ii5ohPmY0aNUTXVHRQNODyPpfaWs5PPUpyX2lWzGQBGyQFpYZg-GYytJEPLV9_seFFfaBMWAk7tu0qKg5USXk8RPAY5e4PyRE3p24USHip38S4nhJU4vbUuT0X8t3hhClCbktzuaYgHEWJj-di3xR5C_i2gJr2otThtk7sPWFHHpaHqFGEk8gLmbMQvJ4JH2I3HAkL_AxmDCVB70jmI2F-JXd6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=t3IIEsTR0pplgP01r9l7_xxLYWgbIj1auobpHT9BhSmX6HAvntEQR0rpqwd5sEYFv10nLYj7DNnC6HSb2dXFG6M1TFjuZ_KYWDkctuFjxHbvK_1vuVwRxdMRaI6ii5ohPmY0aNUTXVHRQNODyPpfaWs5PPUpyX2lWzGQBGyQFpYZg-GYytJEPLV9_seFFfaBMWAk7tu0qKg5USXk8RPAY5e4PyRE3p24USHip38S4nhJU4vbUuT0X8t3hhClCbktzuaYgHEWJj-di3xR5C_i2gJr2otThtk7sPWFHHpaHqFGEk8gLmbMQvJ4JH2I3HAkL_AxmDCVB70jmI2F-JXd6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DFiUXhyJbPaoBahRS9_eeSNVkb8oipL8MyBIPJ4ykQNDMoSQYhcJ_jinkm4ocyfnSicRfJR5QqPRs1meLDegYrJZ3yTGryquIQwCXS9G48JcnNDWWWUJfDSrLzPkfXZ9kx4Zb99sq8X2TXcK5FiX9-TcqyujNy-vGzHBHgvjIbwRAV63V9oGP_-XUrSq9_XrtYMBbHKvpOqroc-S7m5UG7580h9nKvMuF2BNfSp6Iobl7RxK-E8NtqX5mqCGGoPgGXJjdPJgXzYzJh2WvU8B_ZxMrgZlir7j_b9GrYdo9TCOSpOI8YAvLc4Lmh9gqsZA70u5WVscei4A2G-n_uZ3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=Sy9WLYuw5tvv_s02JQShoxMApPFrQ9d7Ou76vzRAfl7eGnquNxB_4dwQQPZXwhr4yCn3N3GEivXs54CYihlcbGBOMCnl9vrv-wXnCEnYj3SoDNHQufA2QmjczyLhe1KBluONlP2xKVjbCfc89PSvMickO7EsEXH1jSC4K-c9UgW7C1N9dG3zGO9SfByMbFyFW9GwiaZQ-PhesYwegn5lY6snO8dcCEFK_ffblYZhfulVpYWOjPgndBI0J6R507X9xgcV7bCOluPtemxtyKDxO54XCHDyhF9O6DzGmv4T7jgppskz-RpaFLBMC9sEtRwl5WnPpNJ7QcsZfKbfBn77Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=Sy9WLYuw5tvv_s02JQShoxMApPFrQ9d7Ou76vzRAfl7eGnquNxB_4dwQQPZXwhr4yCn3N3GEivXs54CYihlcbGBOMCnl9vrv-wXnCEnYj3SoDNHQufA2QmjczyLhe1KBluONlP2xKVjbCfc89PSvMickO7EsEXH1jSC4K-c9UgW7C1N9dG3zGO9SfByMbFyFW9GwiaZQ-PhesYwegn5lY6snO8dcCEFK_ffblYZhfulVpYWOjPgndBI0J6R507X9xgcV7bCOluPtemxtyKDxO54XCHDyhF9O6DzGmv4T7jgppskz-RpaFLBMC9sEtRwl5WnPpNJ7QcsZfKbfBn77Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O95ypk2Y8SeMhCcVhoC424sWGHpHb4o8K3UV9cayMMGDMolg-xIhfUQ5bXKIDr_dJIXvV5FPZ6FBH4gaEC54QeFdVf4IBDioISL0jhN58CEcyn1J1mrFVT4Dp-Q8RZboA_G3q8P1OwKph1suFnbyiZEfIJZ6gQwT18ckKGlLtn20G_gixWqa3G78upFQh3SSHneELwc2VK_4n5q5L9jonmYHvlco7LuRK6j0seunnws5N3h9f6jY8Kh9x85UjH5mrqMnYmFwr8-j6-mmzNajKltKnR7WzlTJcWDLPoZLcRaiJj7R_ewscL8q91mrs5fIlUaam4D9feBMrqXmNjXh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTOGRQpk1ROI1gpvrXeeMhm5WkNqRvwEtVO_gXQRkDsCE6vXKl8x74APs3fVelncNWO5DQOUjEFEenxvQS6C0fMQzNXrWKuCfEdfWsSO9AgagjMkKcspq_uWxUpX5hRxOiD9aNsumY9nEFo6cGsvpqm-RWsO-e3g0BWHMz1FFGPLGEbLQTfBpHACiyfmPc63Z3FXFqLuHDrL5vNUaG-Qgj7kD8QtjaVNBjOO8TH_uXvBkLoczfznzgFKvM8XezcimhV83F67w1ikp33ferpUooXdRkIngNb8oescNBFQzFG7rspSNkLtfvYUDakwANY5RUEWUmg0DLy2jkdVK6Ib0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=od5aYlfC0xuvzLnyxabQ7v-8c39I4uauYGv1x07OSUD3HfELvTUWv6qmE_DS07sqlhk6gaj5fcMolCKRoiC8-bKxuqoJSUyxTEZckEGOetR8sZRrQCDaEn2L4Q9GZa4ipLPWuRn0hiDJB5P3InHVBt6clPo_bzZqFnjuTOdgJYKh_XEl9BeuPjJsgB-1j1eyxDEehNGIJMlmW_vg86gL2Zu-u9TSzwAqezpmXD9IljqvcOi8W0817OjeVwxetijYAFAXDPmuNmHeay4RPqxeuyV9hJ4nlKlIc414HeTVuIlFhzJuKetmLUeIPyGFAqAERp8Ms_W37qKg1loQAkSEug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=od5aYlfC0xuvzLnyxabQ7v-8c39I4uauYGv1x07OSUD3HfELvTUWv6qmE_DS07sqlhk6gaj5fcMolCKRoiC8-bKxuqoJSUyxTEZckEGOetR8sZRrQCDaEn2L4Q9GZa4ipLPWuRn0hiDJB5P3InHVBt6clPo_bzZqFnjuTOdgJYKh_XEl9BeuPjJsgB-1j1eyxDEehNGIJMlmW_vg86gL2Zu-u9TSzwAqezpmXD9IljqvcOi8W0817OjeVwxetijYAFAXDPmuNmHeay4RPqxeuyV9hJ4nlKlIc414HeTVuIlFhzJuKetmLUeIPyGFAqAERp8Ms_W37qKg1loQAkSEug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFKswisOKsbzUazeK9yOyepr1bBGjuqzYVy7jGa8ZTFKu76c0gzZpeh7LQhC_FtFlIMVZCtjYYFyoaMuUEzDR3BmoacVDThiePQ6UYgFaUUrDsONuICMuifP25mhqNpht-23fFAN7LN7cqGSkJ9egfgxtpSuEDydA__RG5lCrL9Sli5d6uau9zzqyetQTJARacWYFieI9LXxRudvmkJmDGCb0VzRnJjXswN4Bw60CY3nYDqDeeBICyi7FxU7ygsN_B0PpNuxY-yB72-TVNqVcN9hBmEbRctVLVfHeMvYefqZOyBHYtEFSHsHOE93U1V0aWAGzWgAyd_18N7nbHqqMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=KWK8xWTuEU-V9tayZvwBwn4d_m6cUNl3s75Q99_gcy9IlGcbwUBQfhO6hFalOQHwxXfLlcpVVsoc9EWF_mSAFChWq-6LeolFyvu7pRXOnFlfVDkofyqrwKFFo46JEs54VzDN9CICMjtm0X1gGPOSTA8tEKsdX1YzroNrXLUvG37yj8RzpwRfOT135Hl1zKG_H13n9wG7adNHa2ixedCALdjtrYxV71P7yQobhLkyRfvJdrxopHeudOmYrnyRD-mt-Rh0D-E4vnCJzVLQstaFd-X8l0ioJ9tYGPA2pGzNymoEq06kbVZ7HW7eSsLMNxXL2eS15kG-xkBDKixuAwpSpQ8N8odCzGK7x_MbFbqtbItHm4v9mzJmyvqu_QO6Sh1X2nIwldegznOyo_az_r5rmA91lR6-C4c8y2Z_QtIuTqlGieDWa1F4xWYfZSR7dd9mWzRY7flWpR5sL7RTJxi7HSOYBGq7fpxuRfpOuYvSFcennbHElLl-1MWcS4LM5KYYC81CJfe1IdjkLW3CxMe60BUy6FwOZdHxWWf-uopB6sQIsDPcqMoj9Pkur4d3vU7kllIUtbkdm-MNRhpwwf-egNOHMtHSpo1C50CJ4XF80z8zm9Ayz1qB7nh2DoGAx7RTGgPIpgFh06FBFQKD7y2LjG-W0KVUKO0Ca2hXUoGbs2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=KWK8xWTuEU-V9tayZvwBwn4d_m6cUNl3s75Q99_gcy9IlGcbwUBQfhO6hFalOQHwxXfLlcpVVsoc9EWF_mSAFChWq-6LeolFyvu7pRXOnFlfVDkofyqrwKFFo46JEs54VzDN9CICMjtm0X1gGPOSTA8tEKsdX1YzroNrXLUvG37yj8RzpwRfOT135Hl1zKG_H13n9wG7adNHa2ixedCALdjtrYxV71P7yQobhLkyRfvJdrxopHeudOmYrnyRD-mt-Rh0D-E4vnCJzVLQstaFd-X8l0ioJ9tYGPA2pGzNymoEq06kbVZ7HW7eSsLMNxXL2eS15kG-xkBDKixuAwpSpQ8N8odCzGK7x_MbFbqtbItHm4v9mzJmyvqu_QO6Sh1X2nIwldegznOyo_az_r5rmA91lR6-C4c8y2Z_QtIuTqlGieDWa1F4xWYfZSR7dd9mWzRY7flWpR5sL7RTJxi7HSOYBGq7fpxuRfpOuYvSFcennbHElLl-1MWcS4LM5KYYC81CJfe1IdjkLW3CxMe60BUy6FwOZdHxWWf-uopB6sQIsDPcqMoj9Pkur4d3vU7kllIUtbkdm-MNRhpwwf-egNOHMtHSpo1C50CJ4XF80z8zm9Ayz1qB7nh2DoGAx7RTGgPIpgFh06FBFQKD7y2LjG-W0KVUKO0Ca2hXUoGbs2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
