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
<p>@news_hut • 👥 141K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYQsmBj0xYdXYni8GcA0QRnpuTBSeLNLLXUIQl7OM1HZpFIaZwQesRkS-yjTj7_1ZHD_uRhtsNggvcHpOFh0Fz8kVru6qAf9Z3E5iz9GCD4xxfCJVLmHXVmuCs8OXGoQTxpknbHoT72GmdHvWR5th07tuhn6yoR8WhoEgvV1AOh-qAGGaWTl9vPBOlyI_H9gEToVe4kyTNCvzTX-IHQMYzYHaDU6EnLZqGNh7apcPwwlYbMS0KPTT2k3b10EnkO8S5Kg3jrIOjcsVDSBi_r2f4DcqCePySaZiTTyrhcpnLehWM7cFZSaDIChw2d5EAdIos9bt_uwCjaXipMOv_99hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBhBfOZ2RHAlWjwbjxviJYLYlYScUGXRiWGPYRjyuJfkJJwjtEPeOFSakrseImM-rcX02dfi3QiSCHgYtAPEE0cy3mipNpIOhJ2-Rgw7nntcqy1iOa5_YcbMxGRYaNZ_LSbys8Pove9nkvu-CJhsIuEiVxL5NaVS_oM0IzZiUMTvWw5KFIhVJ2e9hbBAK_p53_21Khq7AXkUFQEXRpQkvBb_OKVHssoQLmPeU1ZD4PJfrx36ZxYlhNNFNbSbvsKZ6ryGW0MdoZZg1TX1QHsDCDCV4teYoq6vGBaQjNFJen9ngw7w4zNB3yxDdJIlZu7xOgnk9caAXbrrg0tcrHSgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69242">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69242" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69241">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎙
خبرنگار:
نیویورک‌تایمز گزارش داده قبل از شروع جنگ، شما به ترامپ گفته بودید برنامه موشک‌های بالستیک ایران ظرف چند هفته نابود می‌شه، بدون اینکه تنگه هرمز بسته بشه و حتی ممکنه به تغییر رژیم هم منجر بشه.
اما الان بیشتر از پنج ماه از شروع جنگ گذشته، ایران هنوز موشک‌هاش رو داره، رژیم همچنان سر کاره و عملاً تنگه هرمز هم بسته شده. چرا ارزیابی اولیه‌تون این‌قدر اشتباه از آب دراومد؟
🇮🇱
نتانیاهو:
این اصلاً ارزیابی من نبود و چیزی که نقل کردید، درست نیست.
فقط یه پیش‌بینی می‌کنم؛ بعد از این شکاف عمیقی که بین مردم و حکومت ایجاد شده و اتفاقاتی که رخ داده، فکر می‌کنم این رژیم در نهایت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69241" target="_blank">📅 10:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69240">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/69240" target="_blank">📅 10:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69239">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7LhBOFsWniZLYRpxwdj6guOJuWwsza91uhlwpxzUiv3kKLdABJ8KooPvYtgy5KwFBmxpvKjrE1XAU3KifajSDtXzQECLPjU0h0lBEjTMpvrnfXEp2cWcWd7BDNpftRnCnv5bFPixKN18V68Am1dSs8YcDj4U8_aPL5KlzpN0CmOLx8vpcjF_BMCuemhvvL5_BA2Hij2-nXMZq-_SNLcNhoSCZX4aR7JgFp7PKlk96GROmCGjKfUQ_kFXgRRri8Boj8UpPGTaUKhpnlMrQcU6ny_EhKJTmAARM5Q1MtgkOFLOpp6KuxcKAFduKifVW2QuyIiNBGxjvnMkauihUPDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇺🇸
تحلیل مرکز مطالعات استراتژیک و بین‌المللی (CSIS):
ایالات متحده اکنون تقریباً ۸۲۷ موشک پاتریوت و ۲۷۸ موشک رهگیر دفاع هوایی ارتفاع بالای ترمینال (THAAD) باقی مانده دارد که نسبت به تخمین‌های قبلی به ترتیب ۲۳۳۰ و ۴۵۲ کاهش یافته است.
تحلیلگران هشدار می‌دهند که با وجود تلاش‌های گسترده برای تولید، تکمیل مجدد این موجودی موشک‌های پیشرفته می‌تواند سال‌ها طول بکشد و در صورت بالا ماندن تقاضا، ظرفیت محدودی برای سایر موارد احتمالی عمده باقی می‌گذارد.
سی‌ان‌ان گزارش می‌دهد که منابع پنتاگون می‌گویند این تخمین‌ها نزدیک به ارقام داخلی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69239" target="_blank">📅 10:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69237">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=OubzCpTMU7c__Ege2Sxd7WRS-4zGU_wcPV5hH9-IL34l18ceDQUuwA39dkDvK0g1bNrasa4dJFPUdP1j7fqrarVtM_gNtHrsGdBsR6emVU5UuskZ5mPg2f4ABFqFKv1oFFU6N8q0Dw-F6zu5BCGCoEIde8hnvAXbJPgf-Copcy01DThppOTTCNMVRYKBR5a481y1AOcgpeJ5q3cnWJvTuhl_iKxiRVBmr0XVL0tO9wqHe19zaj3ynp6JCOW2FF7cjGs8thQ5GM8vZ4SHGIDaR-pYqzmt_RLEpV302jQXCMQYEzoca7dIZ_J3Cw2DQ_HzaA5L1p3KV1mXoMD1OPTCsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d926097b7.mp4?token=OubzCpTMU7c__Ege2Sxd7WRS-4zGU_wcPV5hH9-IL34l18ceDQUuwA39dkDvK0g1bNrasa4dJFPUdP1j7fqrarVtM_gNtHrsGdBsR6emVU5UuskZ5mPg2f4ABFqFKv1oFFU6N8q0Dw-F6zu5BCGCoEIde8hnvAXbJPgf-Copcy01DThppOTTCNMVRYKBR5a481y1AOcgpeJ5q3cnWJvTuhl_iKxiRVBmr0XVL0tO9wqHe19zaj3ynp6JCOW2FF7cjGs8thQ5GM8vZ4SHGIDaR-pYqzmt_RLEpV302jQXCMQYEzoca7dIZ_J3Cw2DQ_HzaA5L1p3KV1mXoMD1OPTCsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب آمریکا به نقاطی از کشور
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69237" target="_blank">📅 09:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69233">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Ihcpw7gMXPRV-q-P3rnju31_75xjjS4ncNRg246ncbNH0vRhlOe2yNilslYmUAyx4e8fidXxBlfzmlVtlkP0aoP9oA5ZLxBqDL8t5oJLKKY_M4QJ5P6L6bhqGQjCTqp6INlcGPN1C19E_uoXXMOfISAQ6GN5rVZ5NmtyJi0qmbSDZkh0L1FAMq3VQ2fyPGa1RPYD_e6j0aizRh0pG8rxVw7Iq8XEpD7ss3Vr6j01O163k1ShIhaWPiIJeB18VIb2sv8dsxyl-LYbgXN4174_XBOIeszzHVp46m6YPqF6GZriHUa2i69D5MbbPr7oaJny1-zUNTWf11l5aV5iHGcCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04e8c731a4.mp4?token=Ihcpw7gMXPRV-q-P3rnju31_75xjjS4ncNRg246ncbNH0vRhlOe2yNilslYmUAyx4e8fidXxBlfzmlVtlkP0aoP9oA5ZLxBqDL8t5oJLKKY_M4QJ5P6L6bhqGQjCTqp6INlcGPN1C19E_uoXXMOfISAQ6GN5rVZ5NmtyJi0qmbSDZkh0L1FAMq3VQ2fyPGa1RPYD_e6j0aizRh0pG8rxVw7Iq8XEpD7ss3Vr6j01O163k1ShIhaWPiIJeB18VIb2sv8dsxyl-LYbgXN4174_XBOIeszzHVp46m6YPqF6GZriHUa2i69D5MbbPr7oaJny1-zUNTWf11l5aV5iHGcCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
هواپیمای باری C-2A Greyhound متعلق به نیروی دریایی ایالات متحده، دیروز آخرین پرواز خود را انجام داد و اکنون پس از حدود 60 سال خدمت، رسماً از خدمت نظامی خارج شده است.
🗣️
با از رده خارج شدن هواپیمای C-2A Greyhound، تمام هواپیماهای نظامی که توسط شرکت Grumman قبل از ادغام آن با شرکت Northrop Corporation ساخته شده بودند، اکنون از خدمت نظامی خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69233" target="_blank">📅 09:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69232">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69232" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69231">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kiO49vuwQRLCeKCn_BELVoFGp3FR1XPfGBcep42A7N0Dy5rl7voLpoKL6fJM1fybqOfaFfa--1wSkm4CunCiutKhKutoZ6tdzxuQsUWDp_kDw7eTt7ZVIKdcJfDvp7zf-66vLfA-oNhP6VCrMYlSO07aYDBEjF2W2GUVXZNfTJHsfdh9fhiicsdFjfhZ5MIEyiwgZq1E7ajqE-6NUW7fzXEtIPedcmsTpUWksBvW44giRhCfki-IXMdPBvl0E-NyqmFU7qujwy3V6vGEV9HPLq_PsQ0qHF_DUcX4wM25a9iKjQDsBnXkWbqzyHTSy09G1JkHPrhuDAlQhwA8zh-6JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=kiO49vuwQRLCeKCn_BELVoFGp3FR1XPfGBcep42A7N0Dy5rl7voLpoKL6fJM1fybqOfaFfa--1wSkm4CunCiutKhKutoZ6tdzxuQsUWDp_kDw7eTt7ZVIKdcJfDvp7zf-66vLfA-oNhP6VCrMYlSO07aYDBEjF2W2GUVXZNfTJHsfdh9fhiicsdFjfhZ5MIEyiwgZq1E7ajqE-6NUW7fzXEtIPedcmsTpUWksBvW44giRhCfki-IXMdPBvl0E-NyqmFU7qujwy3V6vGEV9HPLq_PsQ0qHF_DUcX4wM25a9iKjQDsBnXkWbqzyHTSy09G1JkHPrhuDAlQhwA8zh-6JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69231" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-bB7Um9I0KKrCYrGKMWa2lth2iTkTi_Sx3PUR24dMsXUgqtL7JEZi_KCUkdsVbfuAU3XcwWSWRQ6P4wNCjwW-qLALsiGvtZvlsQ4ifzPJjSVTlEdyvgSPGmwkHEW_iMq6pencaEbcInWHZ3E02BPYo6h8d5vtfGMAHdsHpT4qFopiaDa3FmJ7NjYR5q4SZ25WTbVEVGHrh_T2t7pq9VW1yaeH1MBJK89QPBBLFaiHRdJBjC9OYV6eY7U0w9rzjJRK0c3MWTpY-XouBgzAR3iA6QfKCtUpTVFG5GuvDO8rPQWlHpdxcCyKoDvy6bE82Ug1Y1_5elVuEl5o499fL49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0hSuQicpecqXwzUfzH5r44cD98jx-sjsVXBeEEx0QkmdwkNOkXP5vqyzMZmfTPvSlF2YBxFfkFp1qYZyXjHQTLS3jOgf89y-WhiFR8OwTDsO38-eg6A8hETQ6HW1bGX_6Tcu8tLvoclqwOMV80Cej1ljJTz7IW81ksZN-_hSrVV94kxoLp0DWiWwCUWmg9SWHpB60e9phFZ2nt7uzdwCrOMzACZ-pZiqrIi8uhNVt-1k1Ul6Fc4mSG7OCsQl01wJZw9_-c_nB9f61tYv7jYZxaxfaOH59c-E0OsGWlx77_y4ImpzMhjwUVGcVT04LVA8bucyvcSKv9PqNW1fGawUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وال‌استریت ژورنال: دریاسالار برد کوپر گزینه‌ای را برای یک کارزار هوایی تنبیهی علیه ایران آماده کرده است که می‌تواند تا دو هفته به طول انجامد.
کوپر معتقد است اگر ایالات متحده خواهان اثربخشی اقدام نظامی است، باید برای شکستن بن‌بست موجود، حملات هوایی خود را تشدید کند تا بدین‌وسیله تهدید موشکی ایران را به‌طور قابل‌توجهی تضعیف نماید.
این رویکردِ «اقدام گسترده» — که یکی از چندین گزینه تدوین‌شده توسط اوست — نیاز آمریکا به استفاده از مهمات پدافندی را کاهش خواهد داد، زیرا توانایی ایران برای انجام حمله کمتر خواهد شد.
- مقامات گفته‌اند که در صورت تصمیم دولت ترامپ برای بازگشت به عملیات‌های رزمی عمده، نیروهای اسرائیلی نیز ممکن است در حمله بزرگ احتمالی آمریکا مشارکت داده شوند.
- کوپر در جریان تشریح گزینه‌های مربوط به یک کارزار هوایی شدید، از حمایت «هگ‌ست» برخوردار شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69229" target="_blank">📅 02:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUu_isiW9ZD5lZd0-rUo5qQyyK6U_-DXtNOkLqeFD22xH485Qktu3u9P1yHNjD79V9ijjJmhUFhfldvwkrV30m40cZIHOHIt5o1ivwRfWSbBM7DWqMDGOrUmlqHgwwdPmT2D8q1V3RArKfwYl-qR51yk1oEl4CIXFhdkFebV8ClWLrhnmDHtLg4gjErpK-9HJCka8Tb-h1EIZ5Byn-_Dy9M5UKj-hN1pBzLFZgVbiF-b5-8b_mbIewG_-fWOnqKA8xX17zh3kyeUA3T8WJ5KxA0OykXAoPFz9GbLUh_c6-Vc0axa5g54Aejb0fIB9T928QdD60jL8DNcuLJPNE3roQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوووری
؛باراک‌راوید:
یک مقام آمریکایی به من گفت که ارتش ایالات متحده در حال انجام حملات هوایی در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69228" target="_blank">📅 02:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در نورآباد ممسنی استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69227" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WskFvZjc5PuDqiTmuVnJGrfS7zCM9NjsTUYiFdZM1iLYqWS8wxRurfKZ2sdy9mch7vnxkPby2TzNVfhtJJMuuOO4wIDixeXPNZ-UKa7wKFt-11V-cyBKisxO2lCG4PbZW3sD-EcSpdCj-4f0yY1sc7MUqbaoebEiV7cu0u2bro1Z7nZLvnwZ6ppF8pGASxCIm0PHxmDh6FxpvHi6bhAKUjl8OFBj-XYFr_VgT0ZL6_TBAl0rOQU32cjrcsU6jHQnJ-xpy_o5_MT_r-hCKYMMN5TPdUIr0OV6YBBD3hgureVazMzd_tusAmtTC4duMbxMBo_6FCYQqd7azRtbc3aQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بعد از توییت عراقچی درباره اوکراین، خبرگزاری رجانیوز، عراقچی رو ماله‌کش خطاب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69225" target="_blank">📅 01:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjhnK6Ow-Gji33bQt2gs31nU1IwWgwfTDWdTDc4sA8CFmlqpOaE3yLIHdZr6tzHAdI7IGnbwLsnpXFcDwQWQTl3Q4ZLSaG1GawjwCPJQSGIKiIqWFxdzs6lTMgvTCKyx0wx9Fu5tEkS8cxGGL6m4Omzn_IVBHTmYFTq71vncjTdIGBZUmjctqLLcp7s5f86APrafenJk9zHLVunMX2Yz9r4ZOMB5WQZ5TLEx0RKX0K6xAAMUsoW7MxIb0E9UxvLVn5rP5S9G-m3WBM_heVf1FHKWllSz35kO1QBnBiBeKRHjOofXXRmLw2ow1RjEKl_cQvk5VBVYW2XfAgVRzwh3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حساب توییتر خبرگزاری تسنیم وابسته به سپاه بسته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69224" target="_blank">📅 01:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUvol7mj4B93Y3sRuzxzXiiMe_pcgrDYPeFMDe414Mc2Ndhl4Yzm1qCEfQrZNK04TCt9QsgArdD_RqKcgwgw9a1HFWl5RbRkxA0nIPQen1NeJlYPzeaeiiyPXNxYT919qozrHrD9LFBHWVXI906hDcn-gVfoyUXoFd1hpngxJaX5A6nP4hToCSS-XlDMFvJ5Od7_8BjdWsQ3STJMe2ogzBwPQnTTvygqchhJPK1gCemIkHlX-2NiifJKCPqpBDmC2So0M-go7qotWFv56K2ZeB0flfUb0g4OPGXVD286GQpuTD6BmZQ9w5B5uebspKqvQmRIn4nnzc0m0Y66XteyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏9 فروند هواپیمای تانکردار آمریکایی و یک فروند هواپیمای هشدار اولیه مدل E-3B در حال پرواز بر فراز خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69223" target="_blank">📅 01:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_9RTRZdKD2SlUdu3rwjmdf-f6ku4hWuTjTPFHT7aSP0Jg8d9iqE2DfCwRed8dF2TwRBUknEuQfsGYcT9Wxvv3cTstofeVdpGbna8FcB_Fvzm3VJd0GBsAofc8Soz2CewhjjNhf3Ojo-yKcEojhLzRw5TH8e7vMoLWBA85_CVG-BcKflATQcAVIZ_xD-elMCUH3002iSu-VkMRlzP1NIBBPdE33tuKT18NXa_U0w6cuQ3DrBLS8Frxj_HpPjMVyKOjXcKY1lmL7U282VGZCt-bHQ5foo1z5_Y-SL9KktJMDTAiB-yWpmuNsUs2UTOdFqupP965jHVJCYUNUTW0-c1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شش سوخت‌رسان آمریکایی در آسمان منطقه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69222" target="_blank">📅 00:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69221" target="_blank">📅 00:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6qTIE2HXz9spqjb7kBRVC5vj6CgsJdzSzz5DkFn1_aS_dPiVDpGu0e9519qBqGDGQWk1nKSs2a_N2oDRl6v0DyQ30_xuHToW3tH9GO9Z3qcPgaZhfMSqIRYgIe0TQpAW7IuwbgxA7J_PH01zGk_IYoEvMxV8e-KFtpAeDAK2UkwNBrSDFPWjTxR5hLhtgrIwV6kt3VudMdnuwqop-OsRx0C7t0Eub4ZbEyu7zWy92NogHAMXkpCtJrxZXWaVb45Z_u3OWugAqW2mylHSDEPOw4bAmsf-58LgleYx1dfcay-g121HFdxEnMEy0O7fLrPLCbxtySiT-Qj_8pskjrUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه تو تلگرام یک کانال و اکانت ساخته بود گفته بود هرکی تو اردن و کویت تحرکاتی از نظامی های امریکایی دید گزارش بده؛
لحظاتی پیش تلگرام سیک اکانتشو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69220" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69219">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های غیر رسمی از شلیک موشک از یزد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69219" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=HTCY_J19E2UV2IZ45p934A5aHT0Gq7kOeOGf-RZ8nKF_fSFHvMpLspsD1WCFY1XlheKxP9v0Tp6Y7vvmVS3z_zPQqxMdRWrRKy67gb7wulyL2tozPdBiAFmFGy67v5bOetb8hyYAkI2adHkit2eZauSai7QfQgznvPWAvLLHiBiQWiUSUEfycOEHCm5BgVCmu5NBlV7p8WLIsWwHpWYT-Rsd31METMZ2LtWgeD3x0-A5NPM1uKrh93khk8greJV0CSUxftqP4zqAbkuNnMDxGnGEqFxgAWcjhw4tJGLyFC4XZkkVjYgz3LP5UsWxuG5-E-56YFyTwSnz2RSxp0tjQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c08d37ce36.mp4?token=HTCY_J19E2UV2IZ45p934A5aHT0Gq7kOeOGf-RZ8nKF_fSFHvMpLspsD1WCFY1XlheKxP9v0Tp6Y7vvmVS3z_zPQqxMdRWrRKy67gb7wulyL2tozPdBiAFmFGy67v5bOetb8hyYAkI2adHkit2eZauSai7QfQgznvPWAvLLHiBiQWiUSUEfycOEHCm5BgVCmu5NBlV7p8WLIsWwHpWYT-Rsd31METMZ2LtWgeD3x0-A5NPM1uKrh93khk8greJV0CSUxftqP4zqAbkuNnMDxGnGEqFxgAWcjhw4tJGLyFC4XZkkVjYgz3LP5UsWxuG5-E-56YFyTwSnz2RSxp0tjQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی عجیب از تجمعات چند شب پیش خرم آباد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69217" target="_blank">📅 23:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69216">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند،</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69216" target="_blank">📅 23:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69215">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6df873441.mp4?token=AbjhAvcm5EzO73KUJeUGOfflfD-ytFrCmkmdj-cMKWJm01SYdptXU_ae6wim4jiPYTK3NPH53m_6wPDKDEGUK7p2fbaPe2_norm5ugMyecR9ArmEuIwlZbQV7Hnbv__9A_SJNwcYJsUjksmEcFGalr3VZfANZw6VOEwmYzRZ2fGhfASSVnVv4r2OKMBjzZQMY9F832ICA_9gOrzbD_PBlDBCuYDOgzBIkYXyv89rXH8Ea4rGptBdquPbqgacreJxML0CT_uU4jwRd5hOJcfxTVEAWcqbDssxaH3hQrHkrgYmYtbyAKPHFKqCiMqeygPZXlA3eMkuVfIF2pnUHRGcDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6df873441.mp4?token=AbjhAvcm5EzO73KUJeUGOfflfD-ytFrCmkmdj-cMKWJm01SYdptXU_ae6wim4jiPYTK3NPH53m_6wPDKDEGUK7p2fbaPe2_norm5ugMyecR9ArmEuIwlZbQV7Hnbv__9A_SJNwcYJsUjksmEcFGalr3VZfANZw6VOEwmYzRZ2fGhfASSVnVv4r2OKMBjzZQMY9F832ICA_9gOrzbD_PBlDBCuYDOgzBIkYXyv89rXH8Ea4rGptBdquPbqgacreJxML0CT_uU4jwRd5hOJcfxTVEAWcqbDssxaH3hQrHkrgYmYtbyAKPHFKqCiMqeygPZXlA3eMkuVfIF2pnUHRGcDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ضربه بسیار سختی به آن‌ها خواهیم زد. این را می‌توانم بگویم، چرا که کار زیادی از دستشان برنمی‌آید.
این گروه با گروهی که ما با آن سر و کار داریم فرق داشت. آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، باید کمی آنها را تنبیه کنیم.
شی به شما گفته بود که چین هیچ‌گونه سلاحی به ایران نمی‌دهد یا نمی‌فروشد. گزارش جدیدی حاکی از آن است که ایران ۴۰۰ پرتابگر راکت از چین دریافت خواهد کرد. ترامپ: این موضوع تعجب‌آور خواهد بود. او به من گفته بود که در این کار مشارکت نمی‌کند. او می‌داند که من بسیار ناامید خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69215" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69214">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=HtIf0l0zq0xCUY1F6G3X7Pt15-OCpIOANJVBOiuO_A9RclDTeZ1aScwu3wsPta6xYglUtANTXJpbNxcPEFIkStN2rljwPqIUUrJ0kZKs3jPfp1dTcJy1ipahKOWU2Ay_fSc-OFs5Ak2Ftm-KKUQ462qpK2_PtTaeaGT4aMtE2HNnSTnjR29JhLX0VaCX5k4bbzuncRkTr9Yuo6H-4KsI33Fjm7O0Z2koRYMYrwiuBAbSkFd2CjYPRzUVatucL8FVpBhaOG9s_F_0qI5D7llGEG5Qpe_B3YCb-kZSxp3P2tnAr2C_n1pca4KsINCHV4HfFR0T-y2R2ykHMNEyJ_25qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad144cccc8.mp4?token=HtIf0l0zq0xCUY1F6G3X7Pt15-OCpIOANJVBOiuO_A9RclDTeZ1aScwu3wsPta6xYglUtANTXJpbNxcPEFIkStN2rljwPqIUUrJ0kZKs3jPfp1dTcJy1ipahKOWU2Ay_fSc-OFs5Ak2Ftm-KKUQ462qpK2_PtTaeaGT4aMtE2HNnSTnjR29JhLX0VaCX5k4bbzuncRkTr9Yuo6H-4KsI33Fjm7O0Z2koRYMYrwiuBAbSkFd2CjYPRzUVatucL8FVpBhaOG9s_F_0qI5D7llGEG5Qpe_B3YCb-kZSxp3P2tnAr2C_n1pca4KsINCHV4HfFR0T-y2R2ykHMNEyJ_25qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69214" target="_blank">📅 23:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69213">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687c44382.mp4?token=b55nupAQJaXzI8RCHHj3JhRAjYiJDyPIgfvoxPhHHjU8inV7gQLGgeVYcI0FZSwiJF0QiLgtQpGzHfYN4KXMrjrIMaxyADZh5FhBGQazKlFiXMEMs0H9CBEHpti81vurBOnS-pkgENMyQszRmxycTLjH1tpzHEjwfODisjbRlXbQBXqWeAwlzQrK743SXW-wnCvb7QuceujB7KA0l6dINXaGqEs1vy0HMD21fH6uGK2HLRQnUbl6l_Ca9x1QVMqpcmlwm9BAiuRimpgETYLKzunZDeAllsf3N2rTpIuw_4GAVG3SzcsS58a86bdIdruJbRkwxS0rpJYpSuJ-P1vA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687c44382.mp4?token=b55nupAQJaXzI8RCHHj3JhRAjYiJDyPIgfvoxPhHHjU8inV7gQLGgeVYcI0FZSwiJF0QiLgtQpGzHfYN4KXMrjrIMaxyADZh5FhBGQazKlFiXMEMs0H9CBEHpti81vurBOnS-pkgENMyQszRmxycTLjH1tpzHEjwfODisjbRlXbQBXqWeAwlzQrK743SXW-wnCvb7QuceujB7KA0l6dINXaGqEs1vy0HMD21fH6uGK2HLRQnUbl6l_Ca9x1QVMqpcmlwm9BAiuRimpgETYLKzunZDeAllsf3N2rTpIuw_4GAVG3SzcsS58a86bdIdruJbRkwxS0rpJYpSuJ-P1vA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69213" target="_blank">📅 23:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69212">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ویدیو وایرال شده از یک پژو405 که درحال فرار از دست مامور هاست اونم بدون لاستیک!
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69212" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69211">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbe_dp7zHRFNNDnTBZoHT2eXPCxYqwcRkwVE3_syVHsYxhr2BQ5dFPyQGCF6m64fDTfodS1GXjneaQU1mG3YrgM9kklmfRkk-QfjazTWlFh0PeQieiNpSy4nuKC3CcSkOPbXbyR86pDRt8HVY2jX8gvC1j3scZBsHw5Z7pCqW4rcaISCNzCHc1YUY_YRWT0LmtuD6nrEd8h7shxr1HjSHdjBqTAKuzi5Wnp8uS2t3LElCT4foA9mzlfbVLF8lRdvWY34tJ-Hu3_WwfrygrQ2J3ExOAG_qTfUkvFXUpQXYOxPnZF9mI_VEuGX8kYBMBSIAfj-9H_Xrn_Dm5llSFe0mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.  حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69211" target="_blank">📅 21:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69210">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5AOTH-wmreUp3RQDZxqBaiJSbbxaAcL3gqpmfzLQiXq6RlfmGkruJG7QapyxujsHJeo8PSyRUACtF9XJrCp6eubvlTR0op8JS8OEq181iwRSAKCf_P6CyFhMGSg5xZKq5yG2_bOaiqTFqXaG8tOOuVsVRONmoRZoTWw5yP0-naLEvPZHiVj2zNQE3NK4g4GGySpCcFiEICd5thtpVcTjEloxaLMs65VpfW1LWwVBGgZZrDLmoKIf8kY5wuzJF5nv_4ld2zL98Z2r1exH8WovWTKPtaU8DbR-rxlxqYhFvZ45ln14PXq9dx6GTzR25_DKLYbJHY_jcW9Afe5lN4d0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
❌
🇸🇦
نیویورک‌تایمز:
حدود ۲۰ مستشار ایرانی در جریان حملات شبانه آمریکا و عربستان به شبه‌نظامیان مورد حمایت ایران در عراق، کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69210" target="_blank">📅 21:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69209">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YkcKuoIna8gtUeQsKk8YJ3JMqReFmirHzGPgzpwIKoj5v8LdM0-JFXxr9VSxKHC05LpJNZzLajuug3t8wLXB1WRENAD-NaMC3BKBgQ3dQ0YOIAXWT_Eh93aylykrTK2eDtLNNIvvjZGqpbu8U-p_Bg-ihw4XwRdc73I7lq6i2y1cOdTABDsiICcnfcoedOsuU1vxMVK9Dj_1Kz9X5hF4Z27k8MuTCot78qV2SBqhObhT5b-4zZmVZzBgZTTr_9F6dqufDTevUtLYSmyzuBkf7VzdKNtltGKK2_P2KgwZsQ2-u4HV9wNGDWA9S2c7d1vr9kql1nJokuic8anmVeQsYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله دیشب آمریکا به حشد شعبی عراق، ۵ تا از نیروهای سپاه قدس هم کشته شدن.
حالا حامیان حکومت میگن واسه اعدام اون جوونای اصفهانی خوشحالی کردیم، خدا چوبمون زد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69209" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=VrtXJqG0-ere1ozPvcQDZL5T9sPEXa8pvpx3B0RgZwFCnZx1KLkgM0oBuJOHLoRzguTwrHHV4HFhIUr6CmLceTBdTb_dseVXqmvYdNw1-KjSeqD6uw8exhkSE6YrPyJZ4B6R4vqNTrFXtDq-EmiZABEsVCUKS1AFMkEe6iRv3nflFvaQcF7wYliSxHts0YGtpEf-CXe2GvuNvt5z-hBqX8_exomM9pbm91rutqpSxBUyN01FMSf3AXiBL_EH9R8HF1PReGtqVBrlmx7avHelmKM3Xy4kT51J_JVLdRUMdx6X71LDB6TzIrdU_vjz5oaugOCnNalT1qGw-Z1IlAWu95-UoRbKwHo_gVSpo0HoT58pdWe40Wuia_Ls1G-c5n9fXt3EBZYPo4PcXkChp8rceI8Ylgjl6GDxWqXEB2zibyDx7kC-06w78rh3PVeAgZcEUftqwHSqD3M-vwYC6fQbht_PehjROvA-Hx3cUtuayZS_cOio-TWiJzONRwo2dGx02xSrR7LUmsHC6OWgqCjIIkKFN0sRx-TPHupu9herjzKQSCc80COI28pibxbEChigNO-CGoUetaVnR7OLJjgS-GAbUC9UJYlkQEjsoXhSCPO_gKXLeyIb_krrkmh3pbURPbBNIv7yN7htaVUJr--y6q8rT0A7_5K1ByCUK5975iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f736bc6e.mp4?token=VrtXJqG0-ere1ozPvcQDZL5T9sPEXa8pvpx3B0RgZwFCnZx1KLkgM0oBuJOHLoRzguTwrHHV4HFhIUr6CmLceTBdTb_dseVXqmvYdNw1-KjSeqD6uw8exhkSE6YrPyJZ4B6R4vqNTrFXtDq-EmiZABEsVCUKS1AFMkEe6iRv3nflFvaQcF7wYliSxHts0YGtpEf-CXe2GvuNvt5z-hBqX8_exomM9pbm91rutqpSxBUyN01FMSf3AXiBL_EH9R8HF1PReGtqVBrlmx7avHelmKM3Xy4kT51J_JVLdRUMdx6X71LDB6TzIrdU_vjz5oaugOCnNalT1qGw-Z1IlAWu95-UoRbKwHo_gVSpo0HoT58pdWe40Wuia_Ls1G-c5n9fXt3EBZYPo4PcXkChp8rceI8Ylgjl6GDxWqXEB2zibyDx7kC-06w78rh3PVeAgZcEUftqwHSqD3M-vwYC6fQbht_PehjROvA-Hx3cUtuayZS_cOio-TWiJzONRwo2dGx02xSrR7LUmsHC6OWgqCjIIkKFN0sRx-TPHupu9herjzKQSCc80COI28pibxbEChigNO-CGoUetaVnR7OLJjgS-GAbUC9UJYlkQEjsoXhSCPO_gKXLeyIb_krrkmh3pbURPbBNIv7yN7htaVUJr--y6q8rT0A7_5K1ByCUK5975iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کشتی ترابری گاز آمریکا نزدیک بندر دمیاط مصر با پهپاد هدف قرار گرفت
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69208" target="_blank">📅 20:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69207">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=R7dsRHonoV1F2YcxgQYDPwIQlNBitS9FahcAT9mYuomze7Z8TJfJU9kUf2h92-qtEMQhzOIueWA-Js2sIQg7zqOK1225Xwndazjpg6JEy5B_jpyTVOtNDWcwv-BXZ-oMAcJnBq_y_wiezP4KFbjvF6A2OxBxXvCwi6elhUE4fqkoDQE-CjFv3AxuGc3jAHG0ZN-axZOKPibAEoIkwn3bDh2MxM9vAR1VAPyc-GP6lvdOsk7gsT9h89OEXSZ4N7LIKjy9YUtuP8-klXMaAq2naaMp1FljyOU7Z32_qet2Bw0g4vMAlbZJdaImavYUoLNz50ORLLZkltqKj7jnq9o_ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f541b0693c.mp4?token=R7dsRHonoV1F2YcxgQYDPwIQlNBitS9FahcAT9mYuomze7Z8TJfJU9kUf2h92-qtEMQhzOIueWA-Js2sIQg7zqOK1225Xwndazjpg6JEy5B_jpyTVOtNDWcwv-BXZ-oMAcJnBq_y_wiezP4KFbjvF6A2OxBxXvCwi6elhUE4fqkoDQE-CjFv3AxuGc3jAHG0ZN-axZOKPibAEoIkwn3bDh2MxM9vAR1VAPyc-GP6lvdOsk7gsT9h89OEXSZ4N7LIKjy9YUtuP8-klXMaAq2naaMp1FljyOU7Z32_qet2Bw0g4vMAlbZJdaImavYUoLNz50ORLLZkltqKj7jnq9o_ezzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69207" target="_blank">📅 20:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69203">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvH0pWfv_f2Fe21V6_s1qdsm4bS1O-5Vcoi_IpNw18VMljKF4Fn6LpijEv6U5KuaVOYcnMtcBEmguRYmWj1fzdIOYoAKyi9QzxEXSi__GAzhC8F5cXBxOJWKuz4y5N95O9hf7BDl8OIimareiq6nL7nIdqJT1rSEBRlwK_61VWF2CwdknaBM4cORFJmS2u_06wFyNwMffCEfC8w5nt9bRmAok9tWM-A2JYoBTfDEsXEzfIwFPN0xM0rJ1rN1v3W6S-ur66ThqBV4Aaz9o-s4Fwr9V7Cp0Ob_0M9FQb9jRS-okrDqKYU58tWiGWrwFwKxC_sPVm1LNu_7jbBXinMR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=PsfKuHA4AZUGm34GOLL2s3750G4b5Iq3iY1NVIPvYgQJ-HqZvrpNKJHvancArS2WUE3mSuaJaKuihSgASA4umIAmRJp5KxyqrL3Escb9dFbWbXoxYcFVVK_wspPba3wIgLq3qQkHIb2WoN_QRjzXy1HRYLFk1myvDwYxRoHz7ETVIKagwMjIDdbIoEjfvMxXYWa5xTZUITUn9ezkFA_lOrux9Cg7gwLFtSNI1HloCKNFZdMVBRZi52yk-gFdsLEY1rqjmVXa2GLC5gAVuoRg2p5ZCasTOuBlLbkwhAjSijVRQxEw1vGqIhRUHICzuQCZmkFaW1s1xznORU4V1X-fEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f829b75e.mp4?token=PsfKuHA4AZUGm34GOLL2s3750G4b5Iq3iY1NVIPvYgQJ-HqZvrpNKJHvancArS2WUE3mSuaJaKuihSgASA4umIAmRJp5KxyqrL3Escb9dFbWbXoxYcFVVK_wspPba3wIgLq3qQkHIb2WoN_QRjzXy1HRYLFk1myvDwYxRoHz7ETVIKagwMjIDdbIoEjfvMxXYWa5xTZUITUn9ezkFA_lOrux9Cg7gwLFtSNI1HloCKNFZdMVBRZi52yk-gFdsLEY1rqjmVXa2GLC5gAVuoRg2p5ZCasTOuBlLbkwhAjSijVRQxEw1vGqIhRUHICzuQCZmkFaW1s1xznORU4V1X-fEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین با حمله‌ای گسترده و پهپادی، منطقه ریازان روسیه را هدف قرار داد؛ در این حمله، یک مرکز لجستیکی بزرگ متعلق به شرکت «وایلدبریز» (Wildberries) آسیب دید و بنا بر گزارش‌ها، پالایشگاه نفت ریازان که تحت مدیریت شرکت «روس‌نفت» (Rosneft) قرار دارد نیز هدف قرار گرفت.
آشکارترین خسارت در انبار حدوداً ۱۸۰ هزار مترمربعی «وایلدبریز» در نزدیکی شهر «ریبنویه» (Rybnoye) رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69203" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69202">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
⁉️
آمبری:
یک تأسیسات شناور ذخیره‌سازی گاز طبیعی مایع (LNG) با مالکیت آمریکایی و پرچم جزایر مارشال، در دمیاط مصر هدف اصابت دست‌کم یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69202" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69201">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=bFCj7sn5O65AhdU46ZkWfBP2xoFJ-ZJm8_8HUuhvMYKBD6FsIF_1q_0_lwcpS3UDknBkHod07RzJMNKvZ8CuWT3eD1XxGdUFOnRsV8KkabIMUjwh4IdAPt7dejDfLWC_2f2fOAjsDFJ-7YCAs651Hld4TYVMMFdTo59IhvC5RhYw-dqcuAzDNRBIZRuN4Ghfycvs24nQyZ0QP8gFCIWrbYogW2azUIhpt4vCOiknLyURVcBaM_Mz1QBNMr9ksMXbKiU9H6M5jBYlnb83Q91gcHUCE8pTEqniSsvYJyHTvYvObKDE1rUO0brF-FOgZwkbXlPgTU0p9FizZQel8lHMhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c2f2b488.mp4?token=bFCj7sn5O65AhdU46ZkWfBP2xoFJ-ZJm8_8HUuhvMYKBD6FsIF_1q_0_lwcpS3UDknBkHod07RzJMNKvZ8CuWT3eD1XxGdUFOnRsV8KkabIMUjwh4IdAPt7dejDfLWC_2f2fOAjsDFJ-7YCAs651Hld4TYVMMFdTo59IhvC5RhYw-dqcuAzDNRBIZRuN4Ghfycvs24nQyZ0QP8gFCIWrbYogW2azUIhpt4vCOiknLyURVcBaM_Mz1QBNMr9ksMXbKiU9H6M5jBYlnb83Q91gcHUCE8pTEqniSsvYJyHTvYvObKDE1rUO0brF-FOgZwkbXlPgTU0p9FizZQel8lHMhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیت هگست، وزیر جنگ آمریکا، در واشنگتن دیدار کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69201" target="_blank">📅 19:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69200">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkdCj1yYCq9dnoO8h9aZK-F-AY1VIa5d3snoXOdymOZx3dsxYfUG_fZFMFl_vntiHwXifLs8bhn_N0zX4vaXn-yFJ_wEpD_nWYEv_nhZsqrE1HbQldBZ9bb_CPsKOFpckTocHXKYQ0V_GS5eeUSYoYngfKTZCvMtpP20IqB28_olSIeC-nS-eXCX5PvPvnFQPlYoCjKBVCaAXowHcB_cSGvXPUfQwUr1DDhA_4QzN-DPU-QQTUsWmwl-qjxV4RHEdwwA_t8IefWZsrwMyM0dDsPUPY7rdcFdujRaM9RYjbmdPTLPuu4xTl5pkfBN8XpxQCeE92uGoO5-dJo1nhz81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنت‌کام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) پس از تهدید و تلاش اخیر برای حمله به کشتی‌های تجاری و دریانوردان بی‌گناهی که از تنگه هرمز عبور می‌کردند، همچنان مدعی است که دریانوردان بین‌المللی باید تنها از مسیرهای مورد نظر سپاه استفاده کنند.
✔️
واقعیت: تنگه هرمز یک آبراه بین‌المللی است. سپاه پاسداران هیچ‌گونه اختیاری برای تعیین مسیر جهت تردد آزاد و باز ندارد. کشتی‌های تجاری همچنان با حمایت نظامی ایالات متحده از این تنگه استفاده می‌کنند. از اوایل ماه مه، نیروهای «سنتکام» (CENTCOM) به عبور حدود ۱۰۰۰ فروند کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69200" target="_blank">📅 19:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69199">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🇮🇱
یک مقام ارشد اسرائیلی:
ایرانی‌ها سانتریفیوژها را به «پیک‌اکس» (Pickaxe) منتقل کرده‌اند، اما اسرائیل از انجام هرگونه غنی‌سازی اورانیوم در آنجا بی‌اطلاع است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69199" target="_blank">📅 19:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R73cotSOaHuvCfo9BUjBwlKWxEmTABV65rzyR6DiSkKF5hVOvTbhRC_b3iCj3czNcCGmyiqRocgoFC-b0X24Ew4DJRq5ySyDnBKczN79kJtC3fFXHx0whk3C7GVPBnboruuplQSDbBE73sA-027DuHG9ak1SfgH2_WwTMvAE5G5R6IhAfI5j04R1pPNK4woDA1MVXQ5QbBjQMhjtOxkzkjAMZsYv1wI-c4bzNl-00ScmChdEmFRMttbAr8rjmeZlgmG3yq271tJgbvzJw2_e1ZakzrrhrKnFNp-LHCzAFuxlQkqZyVFHvuMxmW59c6gE5phVQoolJ9WeIDMBfMYQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbHtDvpmHEvi1AMeUSD5MDxw_NPJi7sEJET1yrxsSyGkJUnw540nQkIfYH5YddH1lCKiJ7_FQPQsjxE9yYcJL2BHKIUjFh4hNS6MoxvDUYuW8iaO2YlxrC1dp3gTAgacobl9RIAc1zkBAOsjFtjkArDV0ME74nM9Ct8mihyg9lmFHrGGx6l5-VSnRc57o70JbmQrtGrk3h3s9Gicr5DaMb0m1PDVwRG4_b0bkvnZbWw0asDjcKZGM-PG901R3dxHMlsYzERp9MRGFuE9DpFZfX9nDbUR5QpWJ6cUwR3F049B9AEfZbeG6TNCy1JQXYgrtgQ7ab9x3FiaLxOIkXcQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmOxFKTGWTP_ImVZXbuKafd-MdEeDA9OP0LTlvxoiS3xJWXiLTHt7lmwPBh9dKG1Hc_moX_28NXyC7ZtTd0qNsvxyFrcuZ-FH_XlqhBamVb8iG_zg58FaiT7p05wguWGuWDZksK5swS4Ka8c5fqvMyeCWe6nqEHTdUAV_MR8zeqYvYYTIQQ1aF1svr_yKVIfVKNsPFqgUIESVSgULn-4oePxt2WZE383r5Z3D82IY_SVS15nqwfUZqAylLnXSTqdIgwTnGLSOcH_hRHuK54NJZhUlbJQ5MDBpnWFR9wUl0PgMTlxthqnvY44I5_MiqJSB_erijqQNiJE7YLAIqFrlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=YaoqPXWSGm5kW_IopE1BuKCFYkm7puUFt4IdCLvkwn_JbcFi-YnKBF57eoe1AQ0AUwdUVGp1-SS7jdR0yzDY5U5_CQVr4S-NTE681FwRg2twnJJ4h_xF0EPs5ExCfmfsIYmv6JymOfqVH9f4am7C3g7dOH2wO3QpPO_jbZs8_NlOtICbGILkPnSRyRMBcEJB--a8q3LLltkMbdrZpCriTlX89Ioyba5DyEGloNt-Z_NcaFFIKHyBaJ1obOW1uBxuZT1MPVUSh0H5j9ixf-VSShx0JAWyZyiV-h_C7WGnD8b2IWJ4OHTOsJOShgY7cmenk-ifU-ZJBIFxWyp6bUR-bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=YaoqPXWSGm5kW_IopE1BuKCFYkm7puUFt4IdCLvkwn_JbcFi-YnKBF57eoe1AQ0AUwdUVGp1-SS7jdR0yzDY5U5_CQVr4S-NTE681FwRg2twnJJ4h_xF0EPs5ExCfmfsIYmv6JymOfqVH9f4am7C3g7dOH2wO3QpPO_jbZs8_NlOtICbGILkPnSRyRMBcEJB--a8q3LLltkMbdrZpCriTlX89Ioyba5DyEGloNt-Z_NcaFFIKHyBaJ1obOW1uBxuZT1MPVUSh0H5j9ixf-VSShx0JAWyZyiV-h_C7WGnD8b2IWJ4OHTOsJOShgY7cmenk-ifU-ZJBIFxWyp6bUR-bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M64GctS9v9DYt53wOZVudVt704dxvlz_hDEVYKuDRW55h6YiyykFKzFnCbPD51UDv3tCUKfZpo7hZAIG7pcROnjChiJFK19b3SOiBZVCv8xCJvXMFFVX1luMgIDTGeGKcmyDVPwBxX24IXOGftc0XtHoNYabceknI_2zLi9Kd07dD84e3_MUzT5p6LKEAMzHWxVY034xJs_oEKLfIl7qOlm2Lt6qEc35ofNMhFDy8PRKsxIprH7c-Zot45l-yFHk5XUAJm0liwmMOX_cy9ZcSwlV9koI8lcFLKx1-wHVmfcsDpkCDNsv13IoirCjJhMXYZDFSA0so8LNzKF4zC9F1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=tq3iO_wvA8TYvN_-TypPgyYHt6hLsKQKU-UefV3h2dkWguWQ7cx_Q-8RC8v5VE3_WUakNf06w9sbo2dgx74-P0tvSacTQpksjgpQkcEjWO8JpLCf4nRSvRSO2c85g21zEnfU4bAwkhR3l9X7egiSgGpk7d-10LV39TzF2QY5URIQOr_pgn7YOSRv9FifNfWLZmvhT2uT7gcFzZi_28mjyEvVsmg1310t-Q4r_-43lisTwcbtb96QP_Prx0Mzaksu62Kb60rj8R1Y9RvL0L5H9_im2g_wShVkOoQ3DQSJMI55dEoufHbxYmUp3te_vaYBeicjXMljUXzsrWH7WKl-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=tq3iO_wvA8TYvN_-TypPgyYHt6hLsKQKU-UefV3h2dkWguWQ7cx_Q-8RC8v5VE3_WUakNf06w9sbo2dgx74-P0tvSacTQpksjgpQkcEjWO8JpLCf4nRSvRSO2c85g21zEnfU4bAwkhR3l9X7egiSgGpk7d-10LV39TzF2QY5URIQOr_pgn7YOSRv9FifNfWLZmvhT2uT7gcFzZi_28mjyEvVsmg1310t-Q4r_-43lisTwcbtb96QP_Prx0Mzaksu62Kb60rj8R1Y9RvL0L5H9_im2g_wShVkOoQ3DQSJMI55dEoufHbxYmUp3te_vaYBeicjXMljUXzsrWH7WKl-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=Pz9V1UPlojgANs4Bf95ts9bBpDx1R3YEDpVqA3eEQQJlmktT_pzcJVfINwMmII6J2H03j3l5L4I-5U0uAzkRhdMEwgBhBBZlIdFBzuLa87iT4QPNz1yPwoUSWaVqtlu2qzCuiHBhaomrxywxxgExVpe2QbmQjkFlXifkJYGHDClAmwmHeiKdFS8QMm3WCgnPwIJK86PqZFpeIJ9HIYuQVHI7SOpwTCGlP1ZPwwxD0z-1qTlnZw-cQPIzwd5ywuSqaZSMwM_TwduMf4IoJD-LHOWLvCTEd4vFoIzBXZZN9quaSLCjXuQhye0gbayhkvP0lFKiq3Y-WzWWPXTL9B-Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=Pz9V1UPlojgANs4Bf95ts9bBpDx1R3YEDpVqA3eEQQJlmktT_pzcJVfINwMmII6J2H03j3l5L4I-5U0uAzkRhdMEwgBhBBZlIdFBzuLa87iT4QPNz1yPwoUSWaVqtlu2qzCuiHBhaomrxywxxgExVpe2QbmQjkFlXifkJYGHDClAmwmHeiKdFS8QMm3WCgnPwIJK86PqZFpeIJ9HIYuQVHI7SOpwTCGlP1ZPwwxD0z-1qTlnZw-cQPIzwd5ywuSqaZSMwM_TwduMf4IoJD-LHOWLvCTEd4vFoIzBXZZN9quaSLCjXuQhye0gbayhkvP0lFKiq3Y-WzWWPXTL9B-Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIzUb--KgkMj_fx6M2hYK-YmUiOjtza2TUBgXNkMGj0_0bGgq6jlz5LG1mdIue6zqnkp0x7SN2lDFpy2R3bxxwjN-3ji6AtTV4ezRZcXuDLLeVYjvR1a5WRU2XxuVtCFk1QJ2dqhY17zvz35IX8LdIq2AYyM66thGvQpUmSomMY9vYV2xQOHFLZCdvrknGIkJv9H3_mSHuWDn6bnEjdUrixT394a-YxtAj8sTMOj8cSqL2RrXZxAzQAvi0QQryxCyJPDklRTEUTVbUNR0QNScdsJ5xE-_FASa9VkQsG8JhrwrqtF4ZgkWnAi_1p0tlW1XityuPn-KBo2ygp_9UAM7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=ZJDL5qgN9A0Hp5UaSpz-oRzMe58Nm0Xd2PmoKZuhCeImoV1wQSsWmfrtVnpoBsh1T_5KjTS9MvFSw672cgHng5sjKCw2x0fk6cOGUMqCULO2Y9MG8aySiVwHorLFTU1Hq2NRhYjUcE8Qz_8J3AGmOsrW2MzDdTTJQ47EEjaB1FfUcqZXdcCYmm3dkSW460lKUHGoEhIH-tZUBTCDNNOZFOxPqQhgvnBe5vdIa5p8pxZ51eqLSQdyfRowMyTn0PYNge1rdHdl8dVf4JAULNg5HYezlMiLcRD5GQx6E6DeAJVe62wrJgwWrN0gLlESfwz391gZ6c36tTDt_DOlnWtpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=ZJDL5qgN9A0Hp5UaSpz-oRzMe58Nm0Xd2PmoKZuhCeImoV1wQSsWmfrtVnpoBsh1T_5KjTS9MvFSw672cgHng5sjKCw2x0fk6cOGUMqCULO2Y9MG8aySiVwHorLFTU1Hq2NRhYjUcE8Qz_8J3AGmOsrW2MzDdTTJQ47EEjaB1FfUcqZXdcCYmm3dkSW460lKUHGoEhIH-tZUBTCDNNOZFOxPqQhgvnBe5vdIa5p8pxZ51eqLSQdyfRowMyTn0PYNge1rdHdl8dVf4JAULNg5HYezlMiLcRD5GQx6E6DeAJVe62wrJgwWrN0gLlESfwz391gZ6c36tTDt_DOlnWtpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTv2I4U6Ij3coqyS32LAnehObBctKJhPMxfNOenxfCFRPo0BFroTPkfhgyyeHAsCqxhZuz44lBCCK8YpK23rR4OMW3VTf3-Awkv28Dr_tjXpbcxeRJIDJf0RVWQ6GjqgVKH2tztmPjAMyTnSTFqCd7ks4XQsluYbrvKMy1F1SuKDEWB9uU182EqoaXs1Ldkvi9erGnFjztVU-kM8n3vsmNBJPa1noBTXwu_yQ3G-Xnr4Zgz9t0w8LXFmyT9p-TubSER0omyMSGvLvCkrfTVqFD1cAR51FqCPRuLhk2Yos6hZfnnEzugBiOnvGaJuhLVOtb5LprkEw-Aegq6vH1bz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSk0IRcZpJ0pp1bT_CyysvfngSXd-spF-vX1qFRVPm5Gh6puqpaqxshJOxuix_zWWgiVfdZadv7un_6mz6RxHuuTpYIvTYPzKlxkITKVDeUSlGBZ0rFSXDl_hiuQiCGw-OvSXBd-ndtz6Fk07ZnqWbNvIUaHYp1i0puuEqpZ0wr7zJ-4Hgcudn5hPhUtARSsTi3zjqWMhx9xX-EIWNibZYyGfvgituUZNIqc7Uh3EgEE22t5GUgB7LEol3kdoqWwtyav__TJz1QI3NOjVuVBacXa494DwXE7MQw36ImVEcET4mD3vDvreuYKdbqTBRc5I3Z16XfKL7ZDENO9HTj35g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=ReGnaO4CWTclaPOYiCNfzTjQqyIDW_mBDbTtYhDmORApx8o6oH9c5U1rSkqj_dbRj2NMX0vT-3QyahCy_6bNMHwWrbgBY63nre5bwjdmE0T-JA90dgPCnk3ETOqSPNj5zk9yX4bRimVp6lDSoUwoyHzD5H2Q6i-EywKuvzc90NCTGWbHzKFTLy4VXqDORgpxskXTGorY--pU6-gHSrX_S_wc57kIBO07fXIviYOsQms1j8d-GsxO8c3SMEtl5_7xhJ4agQhoJXra6aRK4dlKNZJa0mhN01GNKI1oUALD12Ay39vOh_W5Eo8zvTUmq5HWqOInXM02lswXFMawojhf3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=ReGnaO4CWTclaPOYiCNfzTjQqyIDW_mBDbTtYhDmORApx8o6oH9c5U1rSkqj_dbRj2NMX0vT-3QyahCy_6bNMHwWrbgBY63nre5bwjdmE0T-JA90dgPCnk3ETOqSPNj5zk9yX4bRimVp6lDSoUwoyHzD5H2Q6i-EywKuvzc90NCTGWbHzKFTLy4VXqDORgpxskXTGorY--pU6-gHSrX_S_wc57kIBO07fXIviYOsQms1j8d-GsxO8c3SMEtl5_7xhJ4agQhoJXra6aRK4dlKNZJa0mhN01GNKI1oUALD12Ay39vOh_W5Eo8zvTUmq5HWqOInXM02lswXFMawojhf3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxXmbcKipYNheJ5NuGpVTpRmhWIobDkm09Sx_6_Neu6oaIEySu3vysBFYHEGrqHeufQmMaiuYn2qJWJ5RXR69ivI8Mi2f4iXbyys75eXHr1YPAFjgR7ETk0O94ls0xj5w0fMOnN3qOApxWy2Psu2Q7GtPJAjM5dVMATdV-PDqLAgofuUflJzYVTQh46Lkay7yDQmJN63vUvob-KwUanKeqIVK6P9KzO8flZPkmNdMXU8aVakGiStbLUo_RpRFRf1zzNRC11XcHke13Q0PJtVMA6uPWmcJXOu2xtaCqQDMhr5Dem5ZEok6GrZ0MtE1CC0F6h86_0WfWXfitPoxNrVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhBypXvvp8JoB0uAeykPZaTbfrdUHdHuGJRc0-4oNrc4b_ajBMrWafkllkEXGCOWlnesg7y1cG3sE6fNs2U3YLMC8jFAUw08U6Y2RGCL-3oZxubN5rvauzumBbHCEOAML5lsdri6-foqOJ2b-s00XYRZp3G0DQGCBZmOwg9ozGPUk2fIXjjUJ_1j-X8wwVMLB9ytGgDQwUaW9XIt1SQeAmPDi9fcIWXRHsUrYpxte1pifrR82hSuZ5tZcGQ4ER9jxi8pr6Gf840p9qlRGVXF66lTcPj1XtQWYr6B2Kahg3C0ORFUwwfrwajWVBKK5B5LsHf8MUUzpvNRomanWrL95Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=uoDJq-dsgNms2_lruMbyvUQmMQ-BWiG0gHhv-1m45hPnCJM9r-5G9OBzjvcz-nzfHoxy1nv5nUA5mWwfrDHOTrw9k-ecNAixRSN22iPNekJn38Ltb1wPYoUOZwhLu9a8uj0k_qqxc1123-vxrYaxpNLnfr5-qZRHHeZ3fLbJimZewGAI4vJhxq1RScybhRjl9dzf6jOPwKqCbWnTg8AuOVacdT5i0zwq-7Lvmi0LSYnwlZH31Lzv4HS2Tt7YFWUUXq9vXdS7jLOKyt_oASET-4gkbtfFRl8u9sLdi6yGcyT4_zQ5jjIsAB5pQf-0yyCGiW05jb7lEjuxTOTA_KyYBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=uoDJq-dsgNms2_lruMbyvUQmMQ-BWiG0gHhv-1m45hPnCJM9r-5G9OBzjvcz-nzfHoxy1nv5nUA5mWwfrDHOTrw9k-ecNAixRSN22iPNekJn38Ltb1wPYoUOZwhLu9a8uj0k_qqxc1123-vxrYaxpNLnfr5-qZRHHeZ3fLbJimZewGAI4vJhxq1RScybhRjl9dzf6jOPwKqCbWnTg8AuOVacdT5i0zwq-7Lvmi0LSYnwlZH31Lzv4HS2Tt7YFWUUXq9vXdS7jLOKyt_oASET-4gkbtfFRl8u9sLdi6yGcyT4_zQ5jjIsAB5pQf-0yyCGiW05jb7lEjuxTOTA_KyYBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=oiaF4JIyEJNvUCy88Ye5iwCGARV0GYED0RtMW4tExg8BxmKJt-3LvpSAxBJWWN7FC8-t-846gvsBb3gL9BShdL6sT9UrewpApRxmrbTrnPWtbiEuE8qeyJZkfXnlTTm5_FS_zwcogVJPUh8P2BoWFUZpmadZTRX8LCMf-l86_28Tn5HErAuxPVCbN0AU3UyfO7Dei0dghmp6LRRaa8yoqDGvwMvhB0TEkMU6vCAiE7ovjaly_1TveKjfmSfaDb9kX4XdlUPEx4VSQtSu5FPhGfgX7T7fI9zKlr__MgozGd4xkQ3A01J0V4PYDEi_Uf2atI85wfDzReGLU8KySX9FMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=oiaF4JIyEJNvUCy88Ye5iwCGARV0GYED0RtMW4tExg8BxmKJt-3LvpSAxBJWWN7FC8-t-846gvsBb3gL9BShdL6sT9UrewpApRxmrbTrnPWtbiEuE8qeyJZkfXnlTTm5_FS_zwcogVJPUh8P2BoWFUZpmadZTRX8LCMf-l86_28Tn5HErAuxPVCbN0AU3UyfO7Dei0dghmp6LRRaa8yoqDGvwMvhB0TEkMU6vCAiE7ovjaly_1TveKjfmSfaDb9kX4XdlUPEx4VSQtSu5FPhGfgX7T7fI9zKlr__MgozGd4xkQ3A01J0V4PYDEi_Uf2atI85wfDzReGLU8KySX9FMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fns3_QqMhdWuijrNXYy93h3ASIFgVaHnNj6ie4o4lLefhSAGyY8_p9tq46TsuyRvgplYVADWp5a1XeG1bptxruojvCXKuploh82w2DmI8XNc0QqpgrC80ijZUnSI1ODc4EPf4fZ2OTwmdUC6FU3zdHwJ2bboP-LXmzrN1lswRAquTmq0iVAiPTo8lg-mLhpqJd1EaPkpMt78CvEelqftXKILnlIP2TXJ2nQ80zIgTzsQDfRzU77y-DVpOehvBseNwfZ880SVfmYjQg3hDheVHYUo9mcC-fmZSCn9DTUmcpZRnbdiREldHVVHfLPqER4aJ3u6NGrdEgrce1XMOmZJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=FO0-XYuDshD5vmWw96FqpHo-UAKlEZAYpLWEhtW00zCnB8ZTTMd_Bz1Cm0WySMiXi-m3Md_O1Cei0XbvrSqYetiQEX_EotdW3xwJuGn2oOhDiytL7tESxqpVp-BxcObxrZ7zoG_ykCzacO4B5d0J777sHvPxTuX6IcV6VB3dctdqwDFOeW4hd5FYW_u4yOYjvYhv6xQQDWbOoIg5xtS5E72AEZ4hZTD-a4JBl2defhmPwbco78NxKBRDhCGfLXaZR8lmr6j5gU00As5T6lvlRzdsKdPPbaotG0IoqsdqhSNEKB1xHopitDwGSmyPqcFxgFwqTvUyaNRQoE2e6qTW_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=FO0-XYuDshD5vmWw96FqpHo-UAKlEZAYpLWEhtW00zCnB8ZTTMd_Bz1Cm0WySMiXi-m3Md_O1Cei0XbvrSqYetiQEX_EotdW3xwJuGn2oOhDiytL7tESxqpVp-BxcObxrZ7zoG_ykCzacO4B5d0J777sHvPxTuX6IcV6VB3dctdqwDFOeW4hd5FYW_u4yOYjvYhv6xQQDWbOoIg5xtS5E72AEZ4hZTD-a4JBl2defhmPwbco78NxKBRDhCGfLXaZR8lmr6j5gU00As5T6lvlRzdsKdPPbaotG0IoqsdqhSNEKB1xHopitDwGSmyPqcFxgFwqTvUyaNRQoE2e6qTW_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=bGpjfxrGS7ZF6prWsEHYjlh8xt7tiOEXVWwnDkSjlzv6s8olTv3X37lAqf0fFJv0gQcbCKfhcZDvcpTyqhZCmUoosiCSF2oRTIwIj5JRiz9fmWMJgjCnWflrC4DpUS-fLKc0-JmZ1tsmoHd7gUxUrbEHQRJS2VFehxXksNKVpIe8J9dDHDsaXTd8FShuiaONP_3W8pC2ANjAtfMvBxfVYKPhMxa-BQUeNuyWFADP6q48bA3reMojTULUNWE1IOLeso9YIO2vTUwfLrBmKK2kALvSM7hRvDL__nf62abdVH9-paT3gmNgj24dBh8A7JHs0djgWpZr85-PyXdHQOCe1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=bGpjfxrGS7ZF6prWsEHYjlh8xt7tiOEXVWwnDkSjlzv6s8olTv3X37lAqf0fFJv0gQcbCKfhcZDvcpTyqhZCmUoosiCSF2oRTIwIj5JRiz9fmWMJgjCnWflrC4DpUS-fLKc0-JmZ1tsmoHd7gUxUrbEHQRJS2VFehxXksNKVpIe8J9dDHDsaXTd8FShuiaONP_3W8pC2ANjAtfMvBxfVYKPhMxa-BQUeNuyWFADP6q48bA3reMojTULUNWE1IOLeso9YIO2vTUwfLrBmKK2kALvSM7hRvDL__nf62abdVH9-paT3gmNgj24dBh8A7JHs0djgWpZr85-PyXdHQOCe1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=HmG0deJxv8P5QQCysTtEtaaLn4DpfxuM_q3WiPA9VLJ1yCVwGTfTOg3Yb5r5Xhd_0WJsIh-_kzJu_AtEj04GTRtXmgesyTdBEgOp5lTHQ50PzcReQ3fSj8YwOxzZaZF115jqvBC5sW30UZANglMYbstlYCr2aScFi7EvuxLqiGGjG1V-_IFy8BuXqFc_odnMOrOd4bVgp6zCsBXZnjUX4RAgKX6T3YM5pWgCzoC-SlDb_Z_qZzl8jP6lPpp2raBC0h0NYngU-Kh7XWfo-NfDKMTKK2p38M4Ew2sEd1_w30O3GEkTPLtepmJy6iA1SA8E07uU5i-0Nzk3GYmlwNBxgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=HmG0deJxv8P5QQCysTtEtaaLn4DpfxuM_q3WiPA9VLJ1yCVwGTfTOg3Yb5r5Xhd_0WJsIh-_kzJu_AtEj04GTRtXmgesyTdBEgOp5lTHQ50PzcReQ3fSj8YwOxzZaZF115jqvBC5sW30UZANglMYbstlYCr2aScFi7EvuxLqiGGjG1V-_IFy8BuXqFc_odnMOrOd4bVgp6zCsBXZnjUX4RAgKX6T3YM5pWgCzoC-SlDb_Z_qZzl8jP6lPpp2raBC0h0NYngU-Kh7XWfo-NfDKMTKK2p38M4Ew2sEd1_w30O3GEkTPLtepmJy6iA1SA8E07uU5i-0Nzk3GYmlwNBxgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=FLeGzoACyzTSwpqCG6JMNUpwmRjeO1l8AY9BYJkVCYnmE7YfTFrPNbFPehHvprIyjck6sLSF_FIXBXINItrH-f0E_FwnTb3xWy81ak6DQI_nK2WAymeLs7_hpV_7ar_EC6bObgV9H45wgfU83gkTnYJ8GbdynRQpYbzBJcFyWKJwLUi-aRqRLcAzNyhsl6GRXpYQKtwG13Ffr3nPisz3p_c_5-AfGuhTFpS6BFA6d9nBlZI3fAA6D11Wda8roZA-wF8fF6RhVaQwcWtQWyNn5EUfWViiV1OMKfg_EuLaeiSkJ6yKP5yTz6dliDS2goyky9lQodXp4fJyGeKNXoMXGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=FLeGzoACyzTSwpqCG6JMNUpwmRjeO1l8AY9BYJkVCYnmE7YfTFrPNbFPehHvprIyjck6sLSF_FIXBXINItrH-f0E_FwnTb3xWy81ak6DQI_nK2WAymeLs7_hpV_7ar_EC6bObgV9H45wgfU83gkTnYJ8GbdynRQpYbzBJcFyWKJwLUi-aRqRLcAzNyhsl6GRXpYQKtwG13Ffr3nPisz3p_c_5-AfGuhTFpS6BFA6d9nBlZI3fAA6D11Wda8roZA-wF8fF6RhVaQwcWtQWyNn5EUfWViiV1OMKfg_EuLaeiSkJ6yKP5yTz6dliDS2goyky9lQodXp4fJyGeKNXoMXGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdYn2HLfas7mAftCnJj3PS5fAbutA_yxa7M2pC6Yn4bB_fDzdMt9IuDPTp9hELgGit6sZ8kciCSYxAvwRNNB7PCcBq4pqOIcTLwH3UFTNQwaCz2Z-MFz-mcrYyWmGEY2JFqGnltbMNoUJaRDiAaBAmPQEljeX8xW-AnoG6ObGKPUxXSDFct_zAb3oXyB7-_6qdGddSj6pcyRJVQ9Im9XOPsM4S1v2_8UIlP3CYUXgRLdcipy6aG8XExFOHw3rcdqazSxyq49ZMYYoQvzNqrU3RHG-0ZIzb1PDFBf0kQLWM1MNvbniaEku6-fFEHnQPeqr5IBHlPwFg2eJlU7QxwM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVqyfPPNsC028Mp4a6edBGa2zRlgpP96T1eBlzQWPRYTpk162wOzqOucp8QPfpqskZmIg5pAZdP8kaJHv1au3Lj_uEFLMSna5c7vi9nzIiqhIy-jA05I1Y6uzy3_RvnyiEUPam1Aj3NO2kxqBZ0emA9AsuoHUJ_fEt6Ozm6fZmMOb4gFEszmX_8ZMylHGGBKyC07aVVUNw-HC2H7TVJi-Qzx8k-cTcBsyMLvhpp9w1cO-dc6Ytm0EvR42HEy3KIRqUVVpEyZo0_OjMY1G1P-n-_0PMPFXgqZSqwW5HhCv4QGSa8pW-PwtxNQj-X5bsmyM_QiZua5916-KhfesHU2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=JyA8a_xUGlJwU6LsMwLHfbh9HB4lcsB5OHGc7x-ori0dU2hWh-4HLbopLnocvtfBMZyA2RxA_0pGai62KYkqlPNI108TzwBFSvXxcYZnv6XEIHuLgRRZM9DRKNvjJqy2TSn_Bpb-Dj5QwGqWS4UkjDX9JN5JrKciZiorZFE8oZyz1noiY2_YOzhwwGHRzWNP3ejCuwUrfI0CGH3Vcb2XbmYMzBONIjLz4GIFw67m6Xv4CnsXWXEfeSfs6Iwy4IJLxj8rFKnEk6YaejSMaqIwjJDHMwsYyQVu3lXJsW91cBx4Mr7vz-xW73LkfNIPfeLHPEdXAmSVLIlTUpLO5AxG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=JyA8a_xUGlJwU6LsMwLHfbh9HB4lcsB5OHGc7x-ori0dU2hWh-4HLbopLnocvtfBMZyA2RxA_0pGai62KYkqlPNI108TzwBFSvXxcYZnv6XEIHuLgRRZM9DRKNvjJqy2TSn_Bpb-Dj5QwGqWS4UkjDX9JN5JrKciZiorZFE8oZyz1noiY2_YOzhwwGHRzWNP3ejCuwUrfI0CGH3Vcb2XbmYMzBONIjLz4GIFw67m6Xv4CnsXWXEfeSfs6Iwy4IJLxj8rFKnEk6YaejSMaqIwjJDHMwsYyQVu3lXJsW91cBx4Mr7vz-xW73LkfNIPfeLHPEdXAmSVLIlTUpLO5AxG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShOC9giz83vEHK8APxfZGUYCxklb4SYHIOqqF5Ar1DIlsg4oEYlFckn3FjQ0y9hoI6CiDRiyVC-uxemJmiL6NrgjM_D1hvN_l6rN5CKTdMAFp6ha3HanQX2EJjo200Osg1MI6f-O0_2C62ULLC9OazJcYUrJoGWGhXSCh1vHeJpdpknj4wBB-tCujVNBfXHzlRM-cM0WjmjRTyzEoGIlih0nfo6WM9_VWx9WlTQi7jPd-YMy17lykrr1YCmRUcqiaWr5MCLokJQz_xpzGMbS0Mc30unWcYRbmVrsZbeuJJCrtFxmwgdZdbCfShbMKGVkaaE6knr-4tutVJl0STTlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrX0huXcRLF7QXzo0u0nH0hTiUW_SP0XNLUPWydCjLGleo2FwMkeO5BBcRNV9VapK7IPSvfuC2CV3DKgRshVqAx0g0uDxiS9iEtJHL8JOtL6GnF8DtIMABeWRqDpOZnWQCxLgQgFoZ628HcARjxMOObTC9VpLjoFr19VFYrVnsBs8IG1-2dpjAbCKDAZrJ7uRdph9Zhznc8WjUri1OypVJwQX5n2qjdmc038jvauHKMZKHAZtolHTjW0dFWZmiJ-_j6fT0n8UhyYDTCd37-7g67qB4N0QF9Qgf755u_cqcIuExnMIquaHaVUm79PUoV92oxGkzuDSYBDj1kIL-_66A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HftFZaLU8522oZ4y0v6greKobFXeswBkNR_mPm-GndJ68QlZD1Db4fx9OQt5iT1J5IR_WvOVMF-120Ja3fMZbVIzpq05OC6SjqCH3KoQLvYL_-IEjSI5Uy8VTggM3_lkNnjnPjhpIrSo7ZvbtCBYB9pconp2E4aiy5RpCkC1ePnd5CdwGJctDI3sbUby5g9t7eRHBrzt2tOqdz8tMsIHRqUns9h0TQfWBw8mHxWCuLcv6cwr0G-S8A8f6IUdh2w_DrPXYhRVRzia9xV6wBEz6VDLaLmqtbgu0QWPk5GijOe7S5VEQWnL1VjPHjUPcdqaEv02BoFLGnzT_iHSJxdM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FuQgO1riJ4tJzYt2ws-ftdykNVRuGNP15fgnvt_FDxPeudKitjBpm5YLOuDDvvE_ylmdaih0H7QkSGj6psvxGy-a9tgxnzfkipn-bGoaM1p0ESIwa-cJmk7Xgjscys3YsOInwuR0X3OJKmqzEsz_jr9E0BDm2tvrTgJs4y6E14dNLyqw9QPiG_VHSmBb8RD4yMOXrcLP0_royTfajGm0bdfKhVbQUxBbmAS1Qk0-HRFOIz_KenvnyY9UgRLc6YtlzVDuP78G2hLtBWYMNza4fDo5Wh3bPNpx6MyQMq6t7PwRNFYkT0yVHP06CagskjZL7GYs6WV34lNCMpsv88ANOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=RIxpf4RMGZoPf6tjJoL0FTZvKhnhthPZrtfvgmBL1fvlDg7wUkCQjAWy1QydURq97xCLA3qgbdUIraNWQYuMAwTz9TzJvcFiDCPcd8xnE5_ZBlQDM26XYdx5a0N5cEBn30zoduk5dQpy2bJc3eCpGm9b1-DgrizH7nP1chfybOMooeUhYN5dadqpl6-LMJCh4HAxNAYRQoPD6WxxPzQHqIS0YPWseAZonk2JWKgv1POTJWuUBAdvHogYf_VPmBIbtogS6WYiL1tT2AAcXHzan_p7TOjdJs1BHvphca45I9PSD6Nx9BlvivxxXAvH4YQdOUuPMykQEJ4m-2oyWTuevA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=RIxpf4RMGZoPf6tjJoL0FTZvKhnhthPZrtfvgmBL1fvlDg7wUkCQjAWy1QydURq97xCLA3qgbdUIraNWQYuMAwTz9TzJvcFiDCPcd8xnE5_ZBlQDM26XYdx5a0N5cEBn30zoduk5dQpy2bJc3eCpGm9b1-DgrizH7nP1chfybOMooeUhYN5dadqpl6-LMJCh4HAxNAYRQoPD6WxxPzQHqIS0YPWseAZonk2JWKgv1POTJWuUBAdvHogYf_VPmBIbtogS6WYiL1tT2AAcXHzan_p7TOjdJs1BHvphca45I9PSD6Nx9BlvivxxXAvH4YQdOUuPMykQEJ4m-2oyWTuevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYGVEyMcBej3baoAVUmeV0OlPaxUT9KtQ4suUlkIS6VYpnXH4EBllLtp36kvpwTKrkbMiHPrbujC6enGS9WT2Nc8AeV7H1Cyln-ZUpDcgWeBlpOQWrUef1YXeZCYeEnq2tldVJZzd1LMRWDT9PDZiBMFqu2bPuljOYONZlicoQwL4UGKPkmJdZ8FydeE4uek4YGB8dmTQrHUnOK7Ri3IrWn806EF6Dj_lxdQEvH0M1vBGpFkzP56DEloxzu0wNASa-64cF0qhxOIGO8l53_M-IGfaLkp7J79rqRp3vS5aSeEkEHmWQvCq2RyU9Gi9-8lN7AVXUU3p1zcUHu9VG4n1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=bb3oSzZkBsNYxmMjBKWzkeDdu1j2HzTNg-kUNrvirA7m6TYsDbZ-G7iic0mbfUpmviKCG2lq7KVkaof0Y2RKtCFT1TFWC4fygSt0iA0AhkeAvmORd2_faFQ1355H290G47sFpZ7Gl9zZg3n0RJdtwLmDfHMtM4OqIeMspVwjtVtmeCX_Ko7GjJjcvu5ZvV5WCLVh4H0ysZrSJztbiio5rsxnF5PPksIL4rQ5SgXU9jWbNjgbyNayFQcusxM_NePyPWGTenvUJxRRVOxvQtLaJLvnCK_3YzhtVvOccmxw7SV09ncK8sLYX0ftrjVJ5CkWJS3gG8RxWGnTd-35SZ4i2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=bb3oSzZkBsNYxmMjBKWzkeDdu1j2HzTNg-kUNrvirA7m6TYsDbZ-G7iic0mbfUpmviKCG2lq7KVkaof0Y2RKtCFT1TFWC4fygSt0iA0AhkeAvmORd2_faFQ1355H290G47sFpZ7Gl9zZg3n0RJdtwLmDfHMtM4OqIeMspVwjtVtmeCX_Ko7GjJjcvu5ZvV5WCLVh4H0ysZrSJztbiio5rsxnF5PPksIL4rQ5SgXU9jWbNjgbyNayFQcusxM_NePyPWGTenvUJxRRVOxvQtLaJLvnCK_3YzhtVvOccmxw7SV09ncK8sLYX0ftrjVJ5CkWJS3gG8RxWGnTd-35SZ4i2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4Moc2xjdqx2gs2HcN6sIgVWDVF6fy4L_XiQYJA1VPDf2vJYzrqnw1lQ83wsE0IK5j_9GbJ67PfLIj9VpsD5sojopNsKkp_0qtBjUwdH8Trvf_LEqShFx9TVd7zFvvZQTnO9h1KgAXQ5_DbxpXupCszcDy591W-fUEOw-JJ8rUJzTSQXxbHPiSNvjvwiLMUBRUHSMdXiEtctCqwCDd2ild7JXVMromR1_7sJn1BMyT7WG_xidU4obPpfy6VuwZY0ULXvu7UB2SvX1EOTxIQDoYraoHFrb0mobrebWD9nQs_aDfE3DEpCwI6v7Ji2SlZjw8uAx3XszN91xKcCnzcShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7dV8ZRJ_rLA-58Z1VWNgbf3uZDrrk9DvgLKOZk2EqA9j6IMD4k6lIPojopc0FWq8UWI2Lv0lY8DROr9MW7O2ltPz1EHfNLHDLDTItyItuIWJWKzD7h-mqGGiE6SRyPkhFfjZ3bMl13VjlFPeW50K2fO3hLCT9fqElpRwFSAtE3wSDk-8UGG6HubPahDSBFjedn3q9H6rpHjyx_e3bf3ALwzp3lawTx0jKgQM-fR2hjuvex08iRnAx4mgM9qpjWXpMVoXLMhJzs_uZ8gYAu9tDCM5t1Ysb6IhV-eDYaY1uf7I7A55-UdezzFw4kEEpDLDbqCC0dauRXt0S-LPfsMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=YObWhLmb-Fz1ZFPHncUAH3pRvVzUKgsvJxPwHaU7k5aErGigRqvKo6PphMSnqcqh1vmGTwdrETFzrHCGtfQzJGp1JkFZWYTdtRBLg_tLjAFhvCT473fynZ5ZbIC2xIog49qi-3mBr3XtySsNuYtGVG00r9uIs-8Kqlf1KnbAP8AM1mky3G5sQJZg9XsMkzevry2N0HBinpZL6qTkw3pGw7-SaBi3Rk11_46YrXkaS7dp0F1UqJ4B2FcXhQLyTR5SmPgfbtFYNCq884vIBWYc-XcmicfprgajwbnZB9zqgzf5DqHDWzui5a7Mn3q-LgNa_SFb94zpXSzsGphsYAGWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=YObWhLmb-Fz1ZFPHncUAH3pRvVzUKgsvJxPwHaU7k5aErGigRqvKo6PphMSnqcqh1vmGTwdrETFzrHCGtfQzJGp1JkFZWYTdtRBLg_tLjAFhvCT473fynZ5ZbIC2xIog49qi-3mBr3XtySsNuYtGVG00r9uIs-8Kqlf1KnbAP8AM1mky3G5sQJZg9XsMkzevry2N0HBinpZL6qTkw3pGw7-SaBi3Rk11_46YrXkaS7dp0F1UqJ4B2FcXhQLyTR5SmPgfbtFYNCq884vIBWYc-XcmicfprgajwbnZB9zqgzf5DqHDWzui5a7Mn3q-LgNa_SFb94zpXSzsGphsYAGWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJx0DkY8qmXfe_6OchxZ_0ZSeIYJlzo8DC5h0pAjJ44XGXY__Sj5VubpD7m2J0O0jM3hi2IPg6Y04ZBms_ZOvl89mCTf87MKwudfkMPeWZff7V3A1QHVo1th_acr-cugxfgapuS6YXj9nD2fW2fDAuqSpAS-IajnhwmftpJKHRi2iQRoXBHDQ_pY03hGMFDi_B5p5xr-91z1xzAX-PjI4UvmO18pUPJuUNUuTGAFN34_02ORKMhd3B3wGPOUagYYQapXKVSF4cgpVXWkwUjL3BS5GlKHKGxE9JBXh7UzvVGGghn8m4FFDOUMt4TVFiWUi6t7FZaR5ps0qKAa0VhUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=L6AzYr71MN_tIpz-YWTvYkogS7iJE-cbCODOz23biIA07g8KxE6PJDvGwa3K5BBpucGKyyB8pmsIC78lIkLkoMugoxIguBb0amOYlURcSkyK8FofIIUfjrNqFbbGsdZG3G4o9KhwUNfMjnNOHTVvPx743ghEUatE17OHOoajFbSPaxFJAtVTVNlVUKcFZVL1oJ1m-_W6wU_iZlwFDlv_iXGZ0PS9Oxs55W-DdoQzne96k3Rsuty3vw58kvLrPxcksbctbUBatShDxl7NeIzqgv9HSTp9aOkIaDJSdY2T8xiSuqMEwsrq-P2mzyHSSnMjiEjctw1ZqzjDkQZjS2w13bTda7XslNYkL7XlROoH46Bv6qGWq855LOfhTm3wkmwdK5m83sQeMYk2my2zCx8G-XpeV4V3Mmq78fTpy9pasPaN8Mw_L_aSjVjXAQHIo3YEZMVmstmZcmLXB8GyrEU6lS9WuN5GDZAmvA6x-VxL0rs91OUiTRiXts5Sm6nwE2kI8ieXDVRbpI2Z1xbim5E_qpkVOktwKnIYQy3m7j4DPxIDuDwOfjTLT6fMSpNXqeoqx0AGSZPLZ7jFZueml4rwU9geuwwLp32i2j-quCpTOluCZiZbR6Ini_nZfuqooVgfY1hUZqLiGHzbMrFKVHLD3oXtcQm7a_KreWPHsQfXfEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=L6AzYr71MN_tIpz-YWTvYkogS7iJE-cbCODOz23biIA07g8KxE6PJDvGwa3K5BBpucGKyyB8pmsIC78lIkLkoMugoxIguBb0amOYlURcSkyK8FofIIUfjrNqFbbGsdZG3G4o9KhwUNfMjnNOHTVvPx743ghEUatE17OHOoajFbSPaxFJAtVTVNlVUKcFZVL1oJ1m-_W6wU_iZlwFDlv_iXGZ0PS9Oxs55W-DdoQzne96k3Rsuty3vw58kvLrPxcksbctbUBatShDxl7NeIzqgv9HSTp9aOkIaDJSdY2T8xiSuqMEwsrq-P2mzyHSSnMjiEjctw1ZqzjDkQZjS2w13bTda7XslNYkL7XlROoH46Bv6qGWq855LOfhTm3wkmwdK5m83sQeMYk2my2zCx8G-XpeV4V3Mmq78fTpy9pasPaN8Mw_L_aSjVjXAQHIo3YEZMVmstmZcmLXB8GyrEU6lS9WuN5GDZAmvA6x-VxL0rs91OUiTRiXts5Sm6nwE2kI8ieXDVRbpI2Z1xbim5E_qpkVOktwKnIYQy3m7j4DPxIDuDwOfjTLT6fMSpNXqeoqx0AGSZPLZ7jFZueml4rwU9geuwwLp32i2j-quCpTOluCZiZbR6Ini_nZfuqooVgfY1hUZqLiGHzbMrFKVHLD3oXtcQm7a_KreWPHsQfXfEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=n-2QMgBKnFdJsFOhaZsHfKM7pIM3tcKvLiI8j-sA53XLqiIsOxVnDMI9edduPwQnDnJdGQD9N5-xsSdrIGsabgLEzUhyqw4sTouRrwc3vNbTNBdatJxEbAykahXHEisvkjFPK0wg9FfH5lESFc-uVzze6It5GbOyZcWRfe-ZwPPv7Y0_9bJKhPu5AWW--8MYDWOUgKuR6ytnp4q6GVdONPgN0LtbDl7Ouk8b301p6SZeLaT-lJ83qXtnhM4nd6myepmQkc8lYbylN4O35tiL-UMgEfazYrXGYSE_N-h7t6RaPAX5r6xPE3c_809FPJR2RcoQ5Fw5QytPFBNmuwzK4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=n-2QMgBKnFdJsFOhaZsHfKM7pIM3tcKvLiI8j-sA53XLqiIsOxVnDMI9edduPwQnDnJdGQD9N5-xsSdrIGsabgLEzUhyqw4sTouRrwc3vNbTNBdatJxEbAykahXHEisvkjFPK0wg9FfH5lESFc-uVzze6It5GbOyZcWRfe-ZwPPv7Y0_9bJKhPu5AWW--8MYDWOUgKuR6ytnp4q6GVdONPgN0LtbDl7Ouk8b301p6SZeLaT-lJ83qXtnhM4nd6myepmQkc8lYbylN4O35tiL-UMgEfazYrXGYSE_N-h7t6RaPAX5r6xPE3c_809FPJR2RcoQ5Fw5QytPFBNmuwzK4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AugIP09d-HhkLf_cQVCk6OYrxZMfqTJ4ThMvm4Rfkqd7Ufa-RZ5-npX5gpf5-_3YBKUwM1NSUhC3iAE1ygRq_MA74NAv0JwGWY9Irg7FKG1CGwIhC37qgtMPRWwZgIk7P5KxDi69ydb0NbsZRYD-P0gaxN7JjnVqE9vOOkJJFX86cnlUtRQ6WXkdDK-bDtAKD5UcyODHukaB32Q6ArGG9aRc-OV-TMORZdimLKbMMYHQ17zBwf1wtxLMLRYOZ9QMTSsNo2h7PtOptBiT4xbg_iop2GowEK2UXnD_v5W4TpQ6gK2J1ggoDztcuHWbvOV9OzeWVdC_VW3Ah3SsMdeTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=kJKo-E07Ooe3_YhUX70fk0_F7pVDSpmcK_IM9Uy1Zrxm57OPmgZo-z7RDfQMw3maHJYqprXiIE67iNg-TCF6BThwWDGlx98JdMx1vSpFFgv77CDmVETvmyr4n5ljBP9HCTcRfrEMcZ0AVr9yfn8V9Ggw9c-wjHAbmOshzFmufXhePdlNNzQTECD9CIoFVPrpK9sLmjWbrpDiSHsjjfHNCbWQPPjjdMSeEjMuzRkDrwkCC6unJoNMtpWd5PaNS9F2rB39OG4xJ9mCLNJEk1EmvcLO_Nu37wUqLCmlMbc9QD_ho252tDfwFrUdWGYvitexTFTkQA4Y9Og2JZC_rm4jAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=kJKo-E07Ooe3_YhUX70fk0_F7pVDSpmcK_IM9Uy1Zrxm57OPmgZo-z7RDfQMw3maHJYqprXiIE67iNg-TCF6BThwWDGlx98JdMx1vSpFFgv77CDmVETvmyr4n5ljBP9HCTcRfrEMcZ0AVr9yfn8V9Ggw9c-wjHAbmOshzFmufXhePdlNNzQTECD9CIoFVPrpK9sLmjWbrpDiSHsjjfHNCbWQPPjjdMSeEjMuzRkDrwkCC6unJoNMtpWd5PaNS9F2rB39OG4xJ9mCLNJEk1EmvcLO_Nu37wUqLCmlMbc9QD_ho252tDfwFrUdWGYvitexTFTkQA4Y9Og2JZC_rm4jAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=CeB_z116kyjGxn1I3IhSKR2IgVhEAaVL6wHUPYpCJAzO16y-e8nZYTfMmpnynSkMwDzNKE9ywemPqRY4X7hUOAf7LKyAEVy9io2fVctxOfLymw5LKCjQ8ljmqDDVEK28AfRWrip6_E9DWkRzoOF0NQNH-Qdz-SZkD9KrRhpWfhtBO93xXTpvMzOgZ04f3A6mGSAngjVaLTsGKIGruNUAfZyCZ0GJd2HoClHQQdugQBeQj9R4Tc2rcHZmPF6Xjxf6FYwMTef_LBVgv7j5dCG4m4F_OD419Amcs9r6QNvcMe5ZwZZvkUeAqNNZLRAc9dBX8olImTMlQggGeS8zLfjAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=CeB_z116kyjGxn1I3IhSKR2IgVhEAaVL6wHUPYpCJAzO16y-e8nZYTfMmpnynSkMwDzNKE9ywemPqRY4X7hUOAf7LKyAEVy9io2fVctxOfLymw5LKCjQ8ljmqDDVEK28AfRWrip6_E9DWkRzoOF0NQNH-Qdz-SZkD9KrRhpWfhtBO93xXTpvMzOgZ04f3A6mGSAngjVaLTsGKIGruNUAfZyCZ0GJd2HoClHQQdugQBeQj9R4Tc2rcHZmPF6Xjxf6FYwMTef_LBVgv7j5dCG4m4F_OD419Amcs9r6QNvcMe5ZwZZvkUeAqNNZLRAc9dBX8olImTMlQggGeS8zLfjAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L02qLNAsEecCNBE23LU1hVjClfIIb8Bb8QWaAgLyjE_xivhVwiWnwHrwNI1tgc28JThbaguomEDsBRO0cc-Rxlqs_QaG_EQPlOcy8grdTRxEIko8N0rCBN4ggAGJXV03kvijZfdOEkn6HfrigoHHl1e5H5uZ_mteD2ElEn-qtuCP7U-GUsoXPAgj5kxnK_QXBljuFj77lCmmXysfSgX0tKO6v1HP6jS2ryvX-2xB0RzNj-9lFoqpdHVGkUd5khUCwakYAqODdDqDWEsBgfl_pg5dwJtipF3iofV7dhKnMIEwlBC8FB3jKCtss19gUDnWUod-lBfOMEUEpGexchA4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=b4-8cBQcBQnPjOL8y7IsQAxc0Zb3l4G7WwHwSV5oiGCIJHcEYtb4RVLQX2HoygGJDa84h23OB370A4HhBkzudIt-ErLvBSgLWV5ktH664SNfe_8tGG3ws6vyL2PkTZDTAzM2bpCWWRSTtgPTZAYN9BSMN5t4qCUYTYONQs9Hsxa9WmF4ioHD05ytaGweV2MrRDYEofXQ2b1ZEBiBIkwgX0KhPuRGKraYE2QKGez1VDCZPzL1YBlzwFenNP-59FS86L-PqH6c67vV8zf7hfgcfp6FhMEZu8PRNjEwVAbgj1Pk6MhTM-N-bDLa7Xhs-FYnhAR0Sc0Kys0GsTxvBgjgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=b4-8cBQcBQnPjOL8y7IsQAxc0Zb3l4G7WwHwSV5oiGCIJHcEYtb4RVLQX2HoygGJDa84h23OB370A4HhBkzudIt-ErLvBSgLWV5ktH664SNfe_8tGG3ws6vyL2PkTZDTAzM2bpCWWRSTtgPTZAYN9BSMN5t4qCUYTYONQs9Hsxa9WmF4ioHD05ytaGweV2MrRDYEofXQ2b1ZEBiBIkwgX0KhPuRGKraYE2QKGez1VDCZPzL1YBlzwFenNP-59FS86L-PqH6c67vV8zf7hfgcfp6FhMEZu8PRNjEwVAbgj1Pk6MhTM-N-bDLa7Xhs-FYnhAR0Sc0Kys0GsTxvBgjgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb-d406rM1l3EBA85rhEFYfQGRj2WC2Ao8d_rwGoMCfslMeim7nIaFEcOy8r7MIzGrSaev4nVTYht_qR5kjyY7ZpxtbuwjhaYsJZUB1hcqAkZAp8e4JcnyT6XBMV35gZWZVEEtcGk-M6JstDSdSg2zuYmklUTdN5uFRcgDpS7knUOwGIfyhJCmVZ3IZG_EHyUS78U2qI5shrhOc5FkQ1WmpvHpqoWfgjUp1jBAlAmTn2gZUymh48yp2ToXuB19LHOTFK6vqNSplM8s2uUjBrKP-GtF6qDZLuBVqehR_vOMhiDbV-Eh2sbVHHmu3OSRDIwHCaZq4PmTii4gTs4-5rGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCrJbKBmiMJ4UxZe5zkRyoM86jpmxdA2l8cfu4cdoA28ReVzSsMy0tfye7jD4sy5EhVEmOCMQfQ7yc43Ksq9DCcmcveFr74mY6FlhymYZaft-VkqFv3latOz2n8Qzaywq_oBwyl0TkfjTmR1AFdMCx_e36KRjpt39TnBrrHm-_xaMQMA64xmcMODayU_Ac7yv0WSt78DgLZCew4lcCrthFqybbhsk_ixiZw8aDDAwtMGkqNe0NhMX_zq-IHAyolGn3kTNfAaWORUJQl8rM71J3-P0LhXIIRKfQk7YdrYeRcpzPqWJ6hXhY_tEUvSO4XJDgFPGLBlQWuTUnYt9rs5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3xb-i4qv8DV7cz1vgbHqNfWj2EahqY3Aqh4L93DNoTxKauqagJfbYFImV9lILJYDrsrgehIHDs6SIRzQHj_YpEPWDjnMVaprTdlMK4CSR-IG7a0IORmJv-pZbn5jbnZnQ8FenDFjya8hu4CJU_7KkJhf_o5CPE-3GxUA3JuSQ-YsUeADnphUjTqGJCGdDjl2njeELEDaJaZ-RJZYo_xBcqIMR5c0lgNL1BXqene3vCKeslPMQm7JG7rzf1jOOqwKZOX4hR4AXuo8rNJWRYQvzVf7Pbsp4UMdpM1UpwEhX2AJLDC2F6HB9DogBRyJ18I_FsJGRfofFJn5mgX3l-XxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAyuf0G7dNW1Q81GqOpAOjdUNnPrK-IhVEB_5WudcUQ9eghzzEn2sNVV7LqpPs1_bHQ--nQksgI6fsj2rWD-YtDGb_5fjJz00A7lnG6pRtuI7SiGWF_ZKfUguRtOAKklBtImKbz5iNUPIHhFmsj-jagtEsO8VDnydjLLKyYmcjaOS42Invxk2O6HClniMBTPUpqwXigYZd7xGeAISanYvUTE_VtXDUOKqRQGis1VTVKvSrmGPl-t2pTkf8PD7mOJF9V2geZ6rkyVkvQD-C44voEpUjzitq2DsCt1VUTqeiEpina1y7lTj2ONrgMXHrpQMRKgvnzVXNSN7jVxloYPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=C_0RyTLqDA6ZxYVap2XTWXxOh54zOPa15CQJ5pahoRkS024psSNVXGmalf8Or6s6aaBcAZty5GaLU2RpT--CbKPtDul1rQNFHQvflo2eXKhrct1BkJskpHcGqZQTvUbL1ZqOtcMRYxkA1yHwkda2PK1o1xkSR13XTe7u-wHd7a2L2PTlsLV2G7ZikXBBWQg9HY_fPd74I7253evM3CUNu4u6dCcyXuXt8Zr9C8Ufuq5ak_AMX-EJZe0JvWD7G6axAYOKlUaLBPXWrnM9_l_Mc66OSzABhmOCDpORcYer2H-S1TdHmmpkEtO4-ninvfagGundofVrMbEfqSIQZ75BOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=C_0RyTLqDA6ZxYVap2XTWXxOh54zOPa15CQJ5pahoRkS024psSNVXGmalf8Or6s6aaBcAZty5GaLU2RpT--CbKPtDul1rQNFHQvflo2eXKhrct1BkJskpHcGqZQTvUbL1ZqOtcMRYxkA1yHwkda2PK1o1xkSR13XTe7u-wHd7a2L2PTlsLV2G7ZikXBBWQg9HY_fPd74I7253evM3CUNu4u6dCcyXuXt8Zr9C8Ufuq5ak_AMX-EJZe0JvWD7G6axAYOKlUaLBPXWrnM9_l_Mc66OSzABhmOCDpORcYer2H-S1TdHmmpkEtO4-ninvfagGundofVrMbEfqSIQZ75BOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM9WSjHj50SbomRWK_6EXr-wDA8DOJujySN1xkmdrN9WFvOLuKyioYibJoRWq4BBi2IsE5I4uzjw925gZLDuLZ4APSEVssj6WAsm2J6e3n2DmpktCGDhQYy1XK3Vb4p1i_DvJrEvJ8hFce3LyhCE801Jp_US1Ed5-A8t5v3moyfGvoK0BnRZag9Mh4sgfVX5u6KwkbEUcWPf65L9p3M6M1Jz3GW4r7ot5TgXudoXSVHljE_hfzy462oayQPlvVuzQgWSU16ThLJ8zxkkExw2PHLUQSa6kmC1unFFebu-90kJR8mL_OXUXnByJBQlNjdxachlJSGMa3WXMUnFZk7mQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=ENt1vRHxQ8QclUQeQr2T06brAaHIf9v5KJ-zwFXnSlL50v_AfQQEAiXmZqq8uFrRQTigyZw34RwJtg3MrJTEzazZXSwBQJZSXpa-YPxnj5s1Z0IGgxC-CkNWudAmOhslDIuCTyRfxzT_uJQvIdyAIcoGkawQOrQMDxop7AMSE5nJqc6B5iFyYQ9rV0iwY0xfwsrSCNtkhwBViehl21zk2F3v4uu_vVC7nKTVKTkDK8X16ssUxczKWQpeXEf7knnHjMo_gWAyvFpgLx5EIfdYfkgJhXwraJpxBzjjHUfl6Lp5o_rGkcG-I12Cr3n1RGuOyAcjpZ3P6xHlbjdxQKZAGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=ENt1vRHxQ8QclUQeQr2T06brAaHIf9v5KJ-zwFXnSlL50v_AfQQEAiXmZqq8uFrRQTigyZw34RwJtg3MrJTEzazZXSwBQJZSXpa-YPxnj5s1Z0IGgxC-CkNWudAmOhslDIuCTyRfxzT_uJQvIdyAIcoGkawQOrQMDxop7AMSE5nJqc6B5iFyYQ9rV0iwY0xfwsrSCNtkhwBViehl21zk2F3v4uu_vVC7nKTVKTkDK8X16ssUxczKWQpeXEf7knnHjMo_gWAyvFpgLx5EIfdYfkgJhXwraJpxBzjjHUfl6Lp5o_rGkcG-I12Cr3n1RGuOyAcjpZ3P6xHlbjdxQKZAGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s719vA5TSEK95EbggPVKMFVzGMIbVkq_LwLGvouM9IqYgccZ3f54I7aw0o_nD8iW1lWK6B4qQkkKNIOfOAJJGWGTUbz9ITzT9iBk3jLoQF7k6ACnJ2E98eQ49ddt-UbcTs5kqEmY95dMyJsdjbKvfp4L05bWOBTsyL2AtrivPx5DHDESaQJOTfgm_RvXrfWK_amIMBTgTMoxQey33B3smNvvq2MeqIbER8ho0O-seV7f4UpKF9ffaIVYbsnKMYKNgVtCjCkm_Zl-x4dtMT6J3M5lgIU0Yf_3x2z2SaJyw2fdQvf0owBlYW_fw0K9NQjQdBb4ffaCt7XIXjy9f9_gQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGAXk0QwP98bKT3uIpttuJI9nba5w8RLja62DT6KDDt2TGhnTtIKsPLDogBMQ8ItoH9zrollzBAo1miP9YDVOVJn9JAVMgF3Rn6HeuFIkWQrh3PnFk7QdEoyLkoKQU2ksg0P2oB3wrDazYUZJ4VSo8vCvoD0LXVBAZeh2qhKT_8H98INX71cFo_ME7ZVrgRMgkPi6zv-vvKsV-8sA27r3qINJG877GNW9uO8HLqV_kPXMW_TnBMs4AJTxc0mUKVsmt6xJLD01tRa9Va8-vGkBH3lMoyXXwNnOGzYLENtwe1tftwwAtZ-0XLZ1WZveeupz9UCi25eDWbmPPbYnV1lyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTaeSOCOsoY8R6IjHUDimaKXZie6ZAPKsTM5HprMceDflVFcP9q-fYi2Jvq4IByIz_pyfND-9gci1NVOeXN2fxm056RF_-Px1OOrJJuri-JfKQSOrjnN4pAN3HpJqBDf-oovSwcCOCwfCjOL3vTE5ogzr-wCQLQHT3Th5Rx3RkB1IBEApOm6tX_3q07osAcB97200Chr-zKxjIuaNI-Ll3iu_XsYmKTQGxfXDV2XtfnGV7KCGs706_ldW7Q_90LKpDaQPqj3GXE-JaFMWJ-WkVPsFSq-0sTjWiTA_6i2z7DHThjrfi0LLHpYLf8qVjJYpdoTgGcnnosNCnLmt5u19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/izc1nsLiMZrViUoS59hL6klJPVJtDa0AXst3Dw2yc0eX9Q1mOZcunXW-6CSFvgu7Fmv3RvprcwYnESTAV0vbvdn91zU_n8prvfmIhTqKs2Zs9XDZM0uxHvLrr_i-vIOXwEQ1u_o8SlEwnQRTN2CCeUxQd0V9-Z-7_BWEw5sVKAyXFZUkGygz9gQXuLbhPMIEqTf92NzHgsUSsEvb20kDX7XpZqCb8qQtKFrEr81LMGVtcUraxrZHS-45qrA3jFX-EJ71mv_sSd7j_c4S2CsxqXA7YN-3Q6raYn3GwAfFXJHmpla2ze1e6tzzU84mKYpeqP3qTbgi1r00FmJ6zv0INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZycMHc3cPBrsIUb5WxReWFLzhDnwhZ16sRCsrSaudn6qkPrX9obRhAyiz0lZ0edazDXg3CGRyrfSCDYyFOi136eJCKpP7L3zj98pW4QFEusqh4UWbf5XHuVqJQ-eM_oYswcxUOjpzfy9avqvge1r631LtxRtPLo3M-Zzl-8oRV8f3fhYbIxNVxW8eHGLQpTOupTra_3H5-XVg1ZmGKwb9yPBdJqRKqyxjmsb_saVv4huIHA1lLwj-YxKGiCC0YfHuc8wP_V6bxMieuSDORgfyI49pznlvklfunOO4BbddPUSAMJ1D-9Fs9GeHpJksaXEdkHsPaMqyrEH5qub2ErJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtN3KWP3cuTt7jL1oI5iRTpmrzB71LSlIK25TUUlGdqOJM86KZFjmUk3QYEGJNlCfEYZrg4Y0wWR8jwZZfEsLeUSsnWVruzPNCOsWA3mTXjPl7JVmpNyXo5LTXsx8DoBPNaug3YQ0XJRa2YDbJt7xXFjs0Gyq3-jRzPNsPAxYTYNdXm8IXbLrzZSRcMyoTVlxozcPNlcU3AVM7FhrZvdch9V_xPf-orrzrRMxB9BM1bPlz4TbfATtOFnyx4uzHAgXqpnjuv7Nwnlc7bLKuH4zl2uDaTz3Gv6Aj-3yTYmDX0Cx0NeV8Sm0VnI26CqOUhMW_k8Aj3uhYN13TjLlV3s4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOt3ZEcOtttGpprp6D6838Kl44P14uGJbQUbTKj8y8UqYUBFrYqhqt9NYAVgI8x4ITZoD9Yp-yCmWF9f0ZW60LO1L5ZCRrvSAScvFSeemk9ykEyirBH5nBudgOlhruJMD8q-OALOiIGtwHnbk3Nn9fdvCLKfT1psXtGXk7eogcs0JLd2wAjQXCJgvjHZpLtEXNH9EUrw4N3JCwrJTOzvzCX8ZRgIGQohoARPxpw_toyVZU6oe2M59W8ZfpIx2l44LX1UVb0pLVk-OzVh-Is2BoL3BKFXFmxTjoAVQYs8jxQbiYUhFLY8pAD9pGqQo3BI_elWkxM5DdTVftrvxc4PDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=CoeSb8MHKTnD7Kpfh82hHlaq1BXIyJ6L45fXbqcXeCvlmd360RfnS3MVIcLY4D9xktu8b4ikfSyzKT0ouc177ozD-JcbsZOML6gejAzhHstcqmWXQrsIp8mgTOcrsX7SX6QJQIjTqFzbP7xI3RnsyNyrmloR-ddqz4SqO0rinuyeR88CvyDfNTS5tkXQHBlDwJdtreOZ80pN4k6XVuLoz2O-w9ub53BTOX8rHDuLxOufHwkCQrRnGre7qatlvpwvw7CSQ6rItdhXGWV_UjTRDRQBoZ9Hx4juMbxaMlm0k4bvHOKTM8x6BU3wWAy_OxxOSjr-ACcbf2_gcZ5LS7e3nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=CoeSb8MHKTnD7Kpfh82hHlaq1BXIyJ6L45fXbqcXeCvlmd360RfnS3MVIcLY4D9xktu8b4ikfSyzKT0ouc177ozD-JcbsZOML6gejAzhHstcqmWXQrsIp8mgTOcrsX7SX6QJQIjTqFzbP7xI3RnsyNyrmloR-ddqz4SqO0rinuyeR88CvyDfNTS5tkXQHBlDwJdtreOZ80pN4k6XVuLoz2O-w9ub53BTOX8rHDuLxOufHwkCQrRnGre7qatlvpwvw7CSQ6rItdhXGWV_UjTRDRQBoZ9Hx4juMbxaMlm0k4bvHOKTM8x6BU3wWAy_OxxOSjr-ACcbf2_gcZ5LS7e3nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2r4rJUvCofRR50zctx3dYKe90Qnzn8H2HzehBc8-D8xSmwcuGsS_rV-tJvXvATrVW-S6AEv7ckeccmpYp7PGKvjL6qfmeiZ6kgmXogCN5HUt68J0nkH5ZBuZOLMS_-vyfzoY1hKEq3oaZvBOiRDIqE0G6XDGjgXCIGB4YKvBzzJXraGpM38x0AQ1h1yL1G1nth11W0MCtQcFF8-xm30q_b50hWzFlgf09gX-pW1nUVMzdZrr6gePR4COWR7cr61hFatp5FzEAOTO23FET10_IP8HgqT-Xyx0LEFPzokatYxWqROI8Gvpff4SrPgSNOpV8a_CeiA3OMsMa5-xsntDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
