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
<img src="https://cdn4.telesco.pe/file/KhMOWGOoMRsXjZHHI0sGMIGRT_VfO-9Tcv0vb2q8nVZs4m-fuoof4Pdn4qcNnCbry1cPyqkGUYJqPK7ooJeLKT0uRaRYqawSYrZ-szeKvjEsPLM9yEoAFmjjdMAGNkguZ5Qhuzajl-eHWxewtlPu8oHQvidW6VNFYE2xTzunFc1lntIoGUFXd1hT3KNsjERQIivdCdRjJWjQLX6y7lV4dut9hE9ivIfTO4Aj-ASyeFj3rHjnZnecGA556SYD6jEv0m77mCL8osoj-r7Oj8mjFJ8ngYQgjN9AWrn2rP74lNHk0BSW2nQMRVQlHcqLo5PzGLNHwXIAd0rd246A2QhK6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 14:19:15</div>
<hr>

<div class="tg-post" id="msg-437423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR_d_euR8798mk_6bdazRy89oGN__CRo6sejb7x4Jp2kzWKp55jq2odYpwltI6H-4GjVJ-boplWErlo74zhOty-ESr6MEEJspBLuODnMmhD9RNKYNkKd42dEpObcqojhxvYrg7-P5jEu3fAV4euL5gdomyrbD_1ErD8LG37AMqL6ZuejhDhbEbdlfYQtthTA10QtFTWP1fkRir5MxoQWH4sUgVrJ40GIPpUe0E7JJiitaHVMdVssN_VdE5cuNCh_IsDr7Y0GKbmqenqnNUdLYLntpB9FsasHNacVEjFOAxOe4OXMSErbQj8SvQVUdsHlIVZ4ZBKedllTuYTSw1SRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در آستانهٔ یک ترسالی بزرگ
🔹
بررسی تازه‌ترین خروجی‌های مدل معتبر جهانی CFSv2 نشان می‌دهد پاییز ۱۴۰۵ با آغاز یک دورهٔ ترسالی گسترده در بسیاری از مناطق ایران همراه خواهد بود.
🔹
از مهرماه با عقب‌نشینی گرمای تابستان، سامانه‌های بارشی غربی وارد کشور می‌شوند و شمال، شمال‌غرب و دامنه‌های زاگرس بارش‌های فراتر از نرمال دریافت می‌کنند.
🔹
در آبان، تقویت رطوبت مدیترانه و دریای سرخ می‌تواند بارش‌های سنگین باران و برف را در غرب، مرکز و البرز رقم بزند.
🔹
آذرماه نیز تداوم ترسالی در سواحل خزر و حوضه‌های مهم آبریز کشور پیش‌بینی شده است؛ شرایطی که احتمال بهبود ذخایر سدها را افزایش می‌دهد، هرچند خطر سیلاب و آبگرفتگی را نیز بالا می‌برد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 492 · <a href="https://t.me/farsna/437423" target="_blank">📅 14:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gzpt1aqf2YYUhelY0rp8kPYBtWQHrRWqOeIzf0e_YLyl-_FQYfEGp8CLO2VP8UwjGzgUwEZXXw95050iVa5Y95flYv35AtvqiHk1KdiEY_z5dVTD2rQYE7Z62ufOWFQs6puPt9eXryONh948Qw0tiO8KuwgRR6SxeSWFH3pQ7xh2hzEbUX0FzWDTFBY8iOyWpuYJOAZkkAWaQGixWTbg4NKbHOIUJ7vvU-T-k8yjRcS0Dx8ixpjual8hdfHLH-qgZwo7kgxpyDgXVTR2ZjJojk0mvJTKQYyJ9TRXiI1lpbrf9G1_MJiWVnzXJ1kuqD_APJnSEQ8PamhCewdhHiy8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2aHMtr-6B9G_CuqXIYMFnwnN0HnQsraGpxFmFMieL-l-Wh3xU2uC9btP64vIzYGMddVvJRq9uWAcqM-xD-gma7lx8hpxoPjwTcKhQzExAqmluucoZNFyyusDkEK1l1MnEUkrT2joqHiS-q3hFOq9EhwY9kDZxnfXYy0_Ht460kNx0t3QsEBR3UvMrp0aHGH1uIQf5EATwBmYOdqim1MWE9O7lyVoWncs4Lw8W0fo05G8VZnzLKuuyVukBmis8Y0HBndqw3HRd1LPbzZJGg91ggOoMAo3ZTx-3t55f0ibTBFxI4EIizYjl4COhJPpJCZmNIBBRgarNyp0zrZJjO-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVGuL_POg8Hm1gR-oMqMdNzpDkkfWVm_0UciAOAjt1OMvrTZ3qxEsXZTwRJQ2qGoGm1PHVRtoOkV6D_3upSWrKorr61Y4WavCXZbhASlH5YbaOPHbj52n09UasENEwZyHtFn_6Ysr4JjK6Z_GLhRycGCQbAkKgsOrbxb-BtXmvKjvKyvMfJaxgdh3CxXJsSHBJ3YBXusbREfuLGOeXaOgVCcZGbwatzyivM2gAtQXW7CZ6gx_x4UnNompVl7_AS6NB9gVA0OrynmUSZnOuNqbtDNJR58OYXICYJuaSBurxtrAC5-2fWdMnVYONBCptn7DKOd7cVb0L4gqjxpnkIveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itYFdgYKBL-au_C0l_FuN1OhAzh0sGSJdNkLDMu5hCdNnIwuniR4rD16Gr414raNIIRqbY0FOG6wlDe5i57SpIFbxfgBG57kNb_zfptNuutCetErhNkEOK1eK9Qmg31P-1WCBGKt-wqOf_JaR2j7Q9wA-hnOsKRfzDdn2d7uVojLGbt-EcQsGhpuQLrGkT76ecgwVj2cBRSL_TgANcIwd5Cz2CsCswWXhVAOBFuxkBWTR7sKy7dDPGxyQ21RVTlctW2TFU4yo23L34uLnbtEcsU8OIRiHNioPA8blVhsKA8Z9c34zHqFMBfZOZDxdIHrPdLg3rAZIhk7eRrkgZhLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGPSJC7mYSEBbmdJzfZfGTCv4o-eiWRC8gM-5tBkFZQXIHIGBMT39-xcRFmNAL4TeuF7U4y6zlTH9ZJad5fkWWuph86PTuECNiDIzXrs50qCn-kHF_jq0avZ11pwtFfzygliFf9DlZ94Qh731MrE1Dxcnd61mqP9Ts6pwQM8Jzk2FCakWFitcWWUOGup_Lt33sKavHBh2mRd4Qlm3XKqXZqywXlV-WjTvM36U8nYA3j7H6HSfOfaSnlEZzTqHi5tXyGqEuQMul7IMGLe_8_nYpulh1GBThiGZMtCss7WQ0s1jqS8i0EkBhLF5ucu_E4Bkcxczyv4uixCD1t5U1U6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAeuttkPS8rriQJi42_pKeY58mMoUdSYgD3tZ7Ig41iEmoZFu3CaLO0x3KSnMzsCZq-apNUzmxOLwp0d7vDQLFtjbrL1noz-yBZds0GkLqsyfhhOzrZdSJtXdOKrUFoxZKnMSOf9OxJ9wi05I07_lFP7ixrzWb3rIF6E2AYf9sZFEDBdZWwLqY9X1iLYm3HeVu1oQl1Dvip_cu3sjrkEsIrPwdI2lIeA-_37BdWO3eo2xqAP-4i-heL-rmWRkc7iMEvB-USRuXxjzOLXPt5iP60zJMqrjEu-nyGU2WEQrMJSi4XZwhj1jCOQyTx9nmo0aHZZcMuUoPUR3d7qbXpong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beoapVvSj0XjgitltoEvdWeZC2VuQZD9sfGwP2lqfOpgJ_reoY9H5XFsD2OJHeVklt6bofKw1uDh_6uAMBZG2Gl7mN0rewQ8NAC-2FUjs4zbR2WfdB6sizffnAWB89wEJJ_8xgxmG-adQ93rJmjY1A3gzq16r7h0PME6JAkgyJD4pmRrK1yaNu6oIdOyzJOFmCLo6n6e1hYU5eGpiriXlRqgMAZterxRLQbV3Ji9BhUB4_6ZAnyWvy6Y1XvAX5WQdbawnJZXd-vVSsMfTRmNzrcvzWMwurPLS5Ph-t6k5Kvwt8pJJHC0fbyBe0smL9C3fBgwkgxuZ3a8Pe41EWJFgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کارگاه موشک‌سازی در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/farsna/437416" target="_blank">📅 14:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رهبر معظم انقلاب درگذشت مادر رئیس جمعیت هلال‌احمر را تسلیت گفتند
🔹
حضرت آیت‌الله سیدمجتبی خامنه‌ای در پیامی درگذشت مادر کولیوند، رئیس جمعیت هلال‌احمر را تسلیت گفتند.
@Farsna</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/437415" target="_blank">📅 13:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDumkzOnPCyUS_nX1z7WMQsF7T9uzSDM5sOkQiWWm6cKYzZTzxfxFqNUrHxn6rcsej67xNOzFQ1Vx7uj5ZKLchMIbZJsAAn8HP2ZcAmhm9_xSSr8_JPlMerD9EPOydVEzp-5pE-UhfO1Cmi9vtIGeZ3zrLLmHevj6QxyzKcsZAoYgIA6pPwETP1HCP1Lt8GEnqVh3RP-8SVF4Sfxgbj3Q0M4Ru7XjknstLYbikO_V3n99DM8uH9rFXBTTaIF3wYc5WP1KEEWfzSpyoGPBQqM_xrDNa1eTt5GmwJURdk2HNCEQjxy1KVYKus9JvYDYateghay1cdXHNPhqCNMJEFVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUHh4C5SouytAsRpLmknQUMxNnMLpg-hxpqsO3SqJl0yZn3NR8Jl7pUIWiLLazfnyIGOy1Sm5TkNzIXPt3cfdWfNfJ9LbxSmGS1B7nfoUJpeXOO2-MhBf_tnliLYQCrWNR3wuS6ddL5Km1s-2TAG-o71T01W-5G4v0Bp1iJEHEmyoJyMSbv-zsI2iXBPKW29szKuG4wq9zTjpRZODGOlnqUIBBAmOpIaP9ANCXD9wvO2-4xFaaEGDGZp2-ssBOaxSjDsvJ9J18GSAn9EiKCKQJama0Js9G1zuTXTHSZR3rNL9kKVNhsSILp7jbzD_ulliLAei1CVEMyjjrdizjIDhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عاصم منیر با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/437413" target="_blank">📅 13:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSE8cSLA_B-u7BSq1wa_I1Gq6Jwl_prAa2rBu8mt5KVbBMZY7yoybOoQcGh-gsXfy-eD5MtSAzNoGhyTOf1McJfinNz66t37ZKNCEgfDzmKdTg_BYzz8bcDk1611UnC-zsb5HuTjMaYXtQXSnD-HSB0opzLcin9g-_SIs727uQXpKHM93i2LiUU_mn4Smmt2hvSrsBNLySWcUj09BNY-fJITAu_Yq_SLHYwyD7l0WiURU-syIOPOiiYAqRKq0W6h8D0ddkIuFlxAT1ghnehmZ8fUPR1GTgmkie-9qPFPJwrVbZPqSyDuo51F1tNHqjTi3F9rlx8mFtRKOxQ_RQ5u7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBtipVJLI5pJ-ILsVQSKlXkTgeqrMcNQI-K8a-w-YTZYSLSI0QIisec55UxhyMubX6utMWtzfUxC9YFlFPfWQ37JO4GmlAgW4xwPlxBtdAazw81LYQQrsoccNDYnqlSlHnBocUwO8Vsj7WDAlX2IlTGsyVqWxe_6bZ4WlvCBdGEnJ9kM7IfYb1S7Am7PXvzVQV-h_bbHHxeOW-LpbCfxNEMSF0Ipz33IfWtECNW-ozZp1OEyYghOnEWeiM-NNq1bI1Kuj8VVubqEx15PsgNAopkPaSXycJDGGgA3mbZ703KH-Zp8C9vJQwOC0asN0CbVTuyizO4i-cVfINYwH9ltmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیدار فرماندۀ ارتش پاکستان با عراقچی
🔹
عاصم منیر که به‌منظور رایزنی و تبادل نظر با مقام‌های ایران به تهران سفر کرده، دیروز با وزیر خارجۀ کشورمان، دیدار و گفت‌وگو کرد.
🔹
در این دیدار که تا پاسی از شب ادامه داشت، طرفین دربارۀ آخرین تلاش‌ها و ابتکارات دیپلماتیک…</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/437411" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPb5OsSFm1oCBuTcfbUS5fCWhZ_bsq04zvlWUGYsie5j07Cs3atle2f8qy3_FTcsHT-bCkRCiycoJmmnQhH3nmo2xYFvUiqbg9yre-HltwgS-vWoS4cU2tWu9ncOcwdBjjSQweAtaQCdzzRRpmm1TSmxSrTHDoVI4d5eo7hgE47owhqX-hrEVsDff4cIaJtocSbteBGXLo1fT6rizCdEqnMbVSOnPzwSQS49U2Q2lOq1VEospCLrygpo05cHRCAA2qvMNvvxZLmgOYEp_Te8cBen66-eozyEQXhSFP98N7_o0CwJU3Ktl86TQ3nKykkuUubdfwE98WRwcCee-UkAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ۷۰ هزار واحدی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۷۰ هزار واحدی به ۳ میلیون و ۷۳۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/437410" target="_blank">📅 13:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUB4XN_ijHNpbA8Sd2hiPSPjKbl3duKxdid911D2oT3fpSEZJXq8bJmItjdy4rDagYE8nZtujUAePX7K6HxY51cTgmJWy_nR1Pabf0evHzlkYlpSrUQNUKQkT2cMcfUe0maKg7imQHpCQOFRTZ1xNfbYyDpZ05GkAZsML-0lzO8IIC7sqfo_uxqcbqk9ZK0vLHPzivSZ1PsQD1j1dhD0hwzJz-DTBoG-OHvx0O7aejvK6zTzMV9wn4jAtBMLcF-sP0aMc-5EpqURgCp9VYhWjCGKtAvd8YP87hPWNQJIx6TR7stFWmiwc9cXlVRG6memA4CyKlgY5RZSndWCgDIItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش متری خانه در تهران آغاز شد
🔹
مدیرعامل سازمان سرمایه‌گذاری شهر تهران: عرضهٔ آزمایشی خانه‌ریز در تهران آغاز شده و از این ماه کار به‌صورت گسترده از طریق سامانۀ شهرزاد شروع می‌شود.
🔹
قیمت خانه‌ریز معادل میانگین کل آن ملک است و افراد می‌توانند از چند متر تا کل واحد را خریداری کنند.
🔹
قیمت‌گذاری برای این املاک توسط کارشناس رسمی و در روز تحویل ملک انجام شده و به مزایده گذاشته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/437409" target="_blank">📅 13:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437408">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محکومیت
۲ عنصر همکار دشمن در سمنان به حبس‌های سنگین
🔹
دادگستری سمنان: ۲ زن به نام‌های «لیلا رمضانی فرزندکمال» و «فاطمه ملک احمدی فرزند احمد» که با برقراری ارتباط با شبکه‌های معاند و ارسال محتوای تصویری و اطلاعات مورد نیاز دشمن برای هدایت اقدامات ایذایی علیه ملت شریف ایران فعالیت داشتند، دستگیر شدند.
🔹
علاوه بر محکومیت به حبس‌های سنگین (۲۶ و ۲۷ سال)، مجازات‌های تکمیلی قاطعی از جمله انفصال از کلیه خدمات دولتی، ممنوعیت مطلق خروج از مرزهای کشور و محرومیت از عضویت در هرگونه احزاب و گروه‌های سیاسی و اجتماعی در نظر گرفته شده که درحال اجراست.
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/437408" target="_blank">📅 12:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437405">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada4667039.mp4?token=D-g0cEt2jMGTEUpYaIZEtX8EEys2adg3TOL3T1CL7TEQ_VTbolH_5Lem5RhcY4fmD8SJwZzBqYB4YJQmitjcRkTvcD4OYGoiwIr8IJtt1lR1noAjBNrQbTnM7SkUirDu11c6kGDjyBMDUZrXMKCV3qIyVHohLzYzIcGKHDKmomDXVq5BfPR91XKx_E9Z6P-bMsdX5FKDjxbeEOHh0BCGmmTX79z_DfIIxDLk1i8bFk3WuOy20jddYPG7jzG1E2FC26FS4RyFhiZ5qIRBbU3iP_G9MPdUQ4fv_20GZU5P35Kkw4ZkwONN3OnkhDx00PtJgUr0OZF7kxteXy4CyCZT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada4667039.mp4?token=D-g0cEt2jMGTEUpYaIZEtX8EEys2adg3TOL3T1CL7TEQ_VTbolH_5Lem5RhcY4fmD8SJwZzBqYB4YJQmitjcRkTvcD4OYGoiwIr8IJtt1lR1noAjBNrQbTnM7SkUirDu11c6kGDjyBMDUZrXMKCV3qIyVHohLzYzIcGKHDKmomDXVq5BfPR91XKx_E9Z6P-bMsdX5FKDjxbeEOHh0BCGmmTX79z_DfIIxDLk1i8bFk3WuOy20jddYPG7jzG1E2FC26FS4RyFhiZ5qIRBbU3iP_G9MPdUQ4fv_20GZU5P35Kkw4ZkwONN3OnkhDx00PtJgUr0OZF7kxteXy4CyCZT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی طلایی شد
🔹
مهدی حاجی‌موسایی در فینال تکواندوی قهرمانی آسیا مقابل نماینده کره‌جنوبی قهرمان المپیک و جهان به پیروزی رسید و طلایی شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/437405" target="_blank">📅 12:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437404">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عبور ۳۵ کشتی با هماهنگی سپاه از تنگهٔ هرمز
🔹
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۵ کشتی اعم از نفتکش، کانتینربر و سایر کشتی های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند. @Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/437404" target="_blank">📅 12:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437403">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c569f870e.mp4?token=XpZ3Sof8l-32ohHvSQcQsm9mJ6yL5xnE95HI_mT8OX64_lECCau6NEbAhpMT6hV7MxeihEEvhDyr1UNqFRA3DCpFmNs-PBLsFbb52tk3hD-2t3xrdLs8JkQJEI3fr_Mn_h78qy4Y-VjpetK_uRvRBcxLi_dIAjlJ3CuHTEogT-_22z2k6bnVIqV6pGTtlVpUP35BtQLP9hp4xxp3-d9Y_pD7l4dw09WUcBJNAEF3oAj3-O48sWmfSpANGBHqZ8IjWAImvH0tOJkpEE0c3081vI2EFqkKiqfkuwofFP-Un985WltIPLR4wKUqQlJj-XWJCcf2KwwXCBInEOyd-RO2xzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c569f870e.mp4?token=XpZ3Sof8l-32ohHvSQcQsm9mJ6yL5xnE95HI_mT8OX64_lECCau6NEbAhpMT6hV7MxeihEEvhDyr1UNqFRA3DCpFmNs-PBLsFbb52tk3hD-2t3xrdLs8JkQJEI3fr_Mn_h78qy4Y-VjpetK_uRvRBcxLi_dIAjlJ3CuHTEogT-_22z2k6bnVIqV6pGTtlVpUP35BtQLP9hp4xxp3-d9Y_pD7l4dw09WUcBJNAEF3oAj3-O48sWmfSpANGBHqZ8IjWAImvH0tOJkpEE0c3081vI2EFqkKiqfkuwofFP-Un985WltIPLR4wKUqQlJj-XWJCcf2KwwXCBInEOyd-RO2xzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کرکرهٔ من‌و‌تو باز هم پایین کشیده شد
🔹
تلویزیون من‌و‌تو، شبکهٔ تروریستی فارسی‌زبان مستقر در لندن، در اطلاعیه‌ای رسمی اعلام کرد که به‌دلیل محدودیت‌های مالی، ۳ خرداد به پخش برنامه‌های خود پایان می‌دهد.
📌
این شبکه تاکنون با دلایل مختلف ۳ بار اظهار تعطیلی کرده…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/437403" target="_blank">📅 12:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437396">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfoyuSwWgZ0Y4OPHzwBYUlFfawJz5DEHojnfaexz0yjEK8J0Jk2VCsRLRHgQ39_YqOleMChyKsn6exIHwyqJcDJD_C7JLa6SMG9vZEtrdMb721S301oXHCIsODY5P4tONwvdnwL7330OO_vtcP1Z3pbSsbR9ECmd3XtX1HuNWjfNE6MYIzPDrtde0efIqv35wd18EWRamV-FbKivpoHypmwp69aakA2g1kmy2h4N87YhWEa73yty-lU2YDqb7riIcHaCR5J3_jzlC7sSPwmC6p6P337ebINbUKXYLG70bZTrSW6cLoJJ1Kscm8axY1nHskC8RAW1XQjzpQS0okqXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogB8E0699QsZ1nVMCnhc-RKK9yGD8sPRtrDmSf9knAW-aDmuoC6dAN54tp67H71h2qfoOs1Wsg2w1WEHdq0mH2J6NvkRgDGEw0f9X1bsID6zi4ec9dDlfuXcO5-43WjcRGUc-4Pye87ZB3mwv7O51cMDH9mzuiRJZReLbsfX_IGQP0ASfEcbomoPE0YL0b5Ueav0XftV81eZSNYOVbSZIT5SDlRk0z8dP3qQjeTCnbli0YlV0hghMXtjY7Rd63xbq8pBJC66uFfU-RnHT8FbmoFX5iYIi_s4VOdW7zT_QvcbFeQk_s_H4UbNWAg_1jGy8EORxuLgnAUol4NSEumFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnyOtwt-DxpcNYaFOMf1KN8HKklyPw1sP9eBPdg9fHXoC0xK4o5uV7NMaaR8hVeU7fGGT90Lj_oI8mPEotTMZiRlO2kGFysXxQnhEU5qs5jjwLpqESxA3D0A548QI8vpsEr-pbHuuWD2DFljqjalGwvDk0YR4Md8Macx-Y1WF9cyJrFchysZyFQvHWG1MRq22TV2QHKkfXgYI40dgFOdc7BUQa7wohRT-Vg9lek3p-qkdI2eRL3umSIJCp8JvjX-MVVrxpTLghgDXCgH9GV9ah2rmeiJzPWCgCoxvGK0YqjRy_FKgrbFxCRQhvDTZC-PfQvT7NeOCkzWK7Z1CpveIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bPAitTfuT0pT0HByt7ou6q7SZ77t4WpaSBwnSGBcX0kjBIdaLWtpHaQn7coo-HhY5vQj6MfIKNbrFhCIdvMYjnF0zN_Ga5ZKZOdKrewRoOy7A3H3TL7891jdU7qX3foYTWx3Sd2tr9g-an7lFhf9_zgcvmptuHTtuezwTm52AlHC8yOgh9tdXBUTISqRI8Pf2A_VNNMjtxnysPxyziNuKJ0q9_8Bi0GVl-NfBCDFOwD0kx4c0bZkhZaqdbMqrtCdB-n5zr5diBIGJSueHdhBWOfFwe__lOMeNXFZFYHTtWgbQWT2FgnvWJSyY8g0T-qwnF49vsQHnrf7uPduhYo1ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjKfdLN61c1FInpD124Dil7LeH9XafZH8eyp2-vX9QSR4xPONSee3KCKx7YF6zaS8RlNuD01RfSj_OeESe1H9bobZ8HQz5IS187zKNvCoanbkiwbfungngQcX0s7gM10uVE2V2XiT7gZUlqLDDvHfVn7rxnW49Ekf42UOiXJQ5q8zn52iz4AocnK7r8QCOITHQlPTOCXHgsUfpNWagxJPPIj3QR424GnLFnSbmf9S6sfsq9Zs9xI7gKIs3UdGT9AtbOV_yDf60DcQk5JE3k5gwpVPoWlTB4AqI3XamEihHJSLbv6lArZIn49bUmfFW5hyfI0xEcQa98BURd2G-U1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QutdBaMDkrwLbsD9VVhsKHEkcamBJv0QQOIN35iLg-0Oe5nQ606oDnuxvbmiCxe2BWzzZso-o4IMRdQ6Jcto5M2xQsi2mLmHRNO-vM--9fcQZR5QC0T8m0Mgg5oX4XeCuIWDV1g59GxA-zJvOLuSJRnl0Ns8nQwXPf51ftaOisi_AVNlaPZu77MFwmHb0mpcGd1nQtoO4E3jmrhWmmLypNdCsfSzYBjfgOH3A7GD8u9FImqAzSq38HkjUxBmQZfWOSL2djP1Iaouwoo0ZwTHj9SRtYgqzwTe22Cc_UC9bAp5l5l5bWocJADlSOLeDR5rEkKLDXgfdcbqSEoqpd85fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XuobaS33gck69uCy3VM6VCefCav3dsSWflvjMd8-7iWU6ITBhByIB-2GfO0DmQ_fo5oiKppSrSJsSH3j7bGzZNtNv3oqwXIfa9rbjJBjQy5aGBqvgETD-rNyFMzdp8a4EZueXkEVrpWj5GRALF6gSZQ9Jttqz4zAYkb58O_FG3f9GW2iJ6_oZpX5xBVH0grxfq_MdI-i1Ff76VKxTS0NVf-Cce3yuH6BeWAzZddcWSCKG2uPFqPi8W_xPiN4KeNmAp6wfmTKMjDLaYTKEqUv_R2A3AY7D0DiDvGZJ5VmEVKEG_I4xzx9wu4Iu7c72g52WlK5o8Nsaw-Rd1iUp-VgRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
از لحظه آغاز زندگی تا نخستین آغوش
🔹
بخش زایمان بیمارستان میزبان لحظات شیرینی از تولد نوزادان، مراقبت‌های اولیه و نخستین دیدار خانواده‌ها با نوزدان تازه متولد شده بود؛ این لحظات از زندگی اهمیت توجه به تولد و حمایت از نسل جوان جمعیت را برجسته می‌کند.
عکس:
زینب حمزه‌لویی
@farsimages</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/farsna/437396" target="_blank">📅 12:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437395">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">توقیف اموال ۹۶ مزدور دشمن در قزوین
🔹
دادستان عمومی قزوین: اموال ۹۶ نفر از مزدوران خارج‌نشین و داخل کشور توقیف شد؛ همچنین برای ۳ نفر به اتهام جاسوسی و برای ۶ نفر به اتهام انجام اقدام اطلاعاتی، کیفرخواست صادر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/437395" target="_blank">📅 11:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dS04F0NlHndJvRwm0lrZ5A0GWAbFmlxRQ0ceq1XDvdDSFDf9VWWcm5PNSRV7tTGfVHjlZSl65GfOg8S1TJrp3C9FK8EqeuZPToVYnG_NkQeM0A36YZ0y0QI2lcj2zRMDMv9dyY3w_P9zvMfVIIo7E0TnBjlOKUxK4o5HQa40qqpi42mS_bOwRVTTgDfSsuJWfEVk0qEXbEAzTI4NeAVOLS6qKnuG4L0B_psdDktD-bFzz_Q5_EUJciVQ7CjDqo8V9JWOvrWtcyp1_qOa1qkRMPHGprqYKcjjNzGyjNd7m5XPEPAYU0lZU5cvw1BKlgRQ2fhJjCC-OLPxPVPh6H_kOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UK6mPFAHwjB6Cpe3NpuGnYi1I_--mOAVzS2U8vl7u-fgcCZ1qJr7u5j2fEqEOPUgQKhKoQ6nGzOnNjdjmkJLniemjCEtqH8QYVQCUaugluKa8uySwSAF_-s-z16NshZAxWbYAn9siCRyvxaeMacVkz0copH5wwcowI1iKbUuPR2K7oQXm8mQMfFOUlszy4AF2dK1dXJxI7PazVuVcLw-OLwuv9L3rJ8H586aWhPwr10-rWDYMha3u0eXH2KNLIX9RjPiKzptsu60hulXD9xP61Hv_wWx7V5ru6ASm2m9amd6Pb0Lh6RlcLucKw1s8tgIa72io0MXjIQaeeNX8EASoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPZjmfOn8sUB3Ai2NNoKozZpWI7YuNJwD4k18bOpVL93LpssG7vGNjkcwa4yFcd8944teWclERvc6iRb98Ao0AOFnrlyfV-7Vm3_mtT3trvizOaVrNAjLKRViL5bToZnJ0Zwaf-l33jt0S09yDjJ5VJXeh9O1_o6vn_17kkZKdGJ1rFeFOGV8naa0IBipFq64X4MKzvOKr515Rbu4ZfOu9tpeCMocBQueIFZvSRCH3tWGgI4ZAmrxa8tCbtHa9sXgs8YC9zengTuMxYvUwzFWh6VbzoxuzThCbuQCAebT04SBt3QbXLa1SHQv5yepIMHueu97h8VcLl9Vt7w3MFfdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نصب ۹۰ هزار پنل خورشیدی تنها در ۴۰ روز
🔹
معاون برنامه‌ریزی سازمان بهینه‌سازی: در نیروگاه خورشیدی شمس‌آباد که با کمک سرمایه‌گذار خارجی راه‌اندازی شده‌، تنها‌ ظرف ۴۰ روز بیش‌از ۹۰ هزار پنل خورشیدی نصب شده‌است.
🔹
این نیروگاه ۶۳ مگاواتی در چارچوب مصوبۀ شورای اقتصاد برای سرمایه‌گذاری ۷۰۰۰ مگاوات نیروگاه خورشیدی در کشور در حال اجراست و به پایداری تولید و تامین پایدار برق برای صنایع حاضر در شهرک صنعتی شمس‌آباد در جادۀ تهران-قم کمک بسیاری خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/437392" target="_blank">📅 11:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N988dqg-wKWsg48qJFq_z8bG7FFrduhet5L6GKMlU5Ng1pFFLiN1PcHiFA8lHYfoocybN2CtovqBPfjLPHtQ4UTalH8r-Fzk3CU8ecQcBMbCBSzcxaoPm3DbmkWHb_QJpjRaB_h7WcMZkHT0qi5Fawpp59vgTbDRRyzThpeXgKQGWZFy5PeeYBvROhiOBKCA6BsQ_aj1TegtXWxWDv5H5kJYWG02VBrGn9wy9cYRyk-DXWQoKYOiPkOkVCoGBhcj6M69Nn1KPZ-_YHELfR8evuHL96Iys6dRI7n2-8BJ57fQQ01GMNAam-5aHC6AisptkwGfnaKVJi0PDdtFoiS9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
پنجمین چاپ کتاب «مرد ابدی» به نمایشگاه کتاب رسید
نحوه خرید این کتاب
▪️
پنجمین چاپ از سه‌گانه «مرد ابدی»؛ روایتی مستند از زندگی پدر موشکی ایران، شهید والامقام سردار حسن طهرانی‌مقدم به‌قلم خانم معصومه سپهری از سوی انتشارات خبرگزاری تسنیم و با همکاری انتشارات شهیدکاظمی در هفتمین دوره نمایشگاه مجازی عرضه شد.
▪️
این اثر فاخر حاصل تلاش 13ساله خانم سپهری است که با سبکی جدید در خاطره‌نگاری جنگ نوشته شده است. کتاب، حاصل قریب 12 سال مصاحبه و معاشرت با اصلی‌ترین افرادی است که حسن طهرانی‌مقدم در برابر چشم آنان رشد کرد و «حسن» شد؛ کاری که هفت ماه بعد از شهادت او، از خانه باصفایش آغاز شد و با جست‌وجو و سفر در خاطرات و اسناد و تصاویر و مکان‌هایی که شاهد حیات و شهادت او بودند، تکه‌تکه ساخته شد تا آینه‌ای بی‌غبار، برابر زندگی مردی قرار بگیرد که نه تنها مایه عزت ایران، که عزت جهان اسلام است.
⬅️
علاقه‌مندان می‌توانند این مجموعه را از نمایشگاه مجازی کتاب تهران
از طریق این لینک
خریداری کنند.
@TasnimNews</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/437390" target="_blank">📅 11:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6Qx0QH3bQSpoCzjz6LKoRW8OfQoaPFdSyYNKOKMZ-AAWi3Sj-zadNLzAXC8VAXHBFGRa6zkiK3nD1nqePo7yx7vFnHy-v9RJEfJ85Wwo--_hhVeL1hTPE1QciwUXKHhSmq099EUxwjrUZzXswyd7r0lSBOqpNBLjUBlxNT6AXQB7okypv7kKL90WkIPd2IQpTTHOwzMfuMASqb7yhS_UKOQKyxg58AsyH1UgrEmPZr2l5EwNdM1wi3fal8uOZyYu74Ss5iotix54uqqZBgr_fRSIT2SvURNU1PyYPq_Zyz9Ph1jL5PkxGLQ8C-8LnbijDzASppZpJUtOj4oCjb1Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/437389" target="_blank">📅 11:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/437388" target="_blank">📅 11:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/437387" target="_blank">📅 11:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN8RlMX60H_STiFGgWlR5JsSJG7JzvGg-cw9okDs8HSEdPZS7vFphiPCjmBtHbcCt1GHDPhe6DL7ME0vqT3ivVZTxEV5X4kd9aRqkaMMyM1fSWrqSALPA9N3hBfL3mHfUNXrf83A1EsalMO-HPl20040fGep7Q3rNAveDeNBvx8GxP05VRqv24u2yyCiOHzQEh_rNbXd80ErQV6Y_TkZhs2W6OCggK-74Lp62QjwqsUAkr3q6BPR-fia1Fh1nNhoiYhw1ZS5mgFcPY7joUTJXAPx55wBDFB2r2HEfHROdELphgN3HV7egI_iXqGc83B1b2oIqRVWvxfX-0A5cFp8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماهانه ۳۰ میلیون دلار پ‍شت مرز بازرگان هدر می‌رود
🔹
رئیس اتاق بازرگانی تبریز: در مرز بازرگان، ۱۰ هزار کامیون ایرانی منتظر ورود هستند و راننده‌ها حدود ۳ هفته است که در مهم‌ترین مرز وارداتی کشور متوقف شده و روند واردات کالاهای مورد نیاز کشور کند شده‌است.
🔹
این رویهٔ توقف کامیون‌ها، که با محدودیت طرف ترکیه‌ای، تعدد سازمان‌های مستقر در مرز و نبود هماهنگی میان دستگاه‌های مرتبط مواجه است، ماهانه ۳۰ میلیون دلار برای مردم آب می‌خورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/437386" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELsCXbUZA02eiTFSyjnmM4KT1kXDxImi2Rw6GjA8c2zQYicb8HZSgTiivZbrNzhjqu1_Du2_S8xk2mr2vU0GavMrRyPKBr9Erp3hmopIRqjXIgHXJr8adnxb-eK9uc7U633WAMjNZDn5SZkVxxuIhRAmnuwwFXpoCO39Iwtyq_K8D8a2Y1JBas78EZpn2C5yqaeT-doCDVyeo-bIExhLNPkJSasdERzWEKHS2RAUOZGr9Ykcqrq73BWB8Ir5v96-d92SlkeW89tME4ZJOaY8-HPKNSrlQy7VrvCWLVMZlOYtddzjYRZ_p5IXWObG2yJ9Shg5xoJh3SEFe9FOCFq01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مزد فروشندگی در جشنواره فیلم کن
🔹
همان‌گونه که انتظار می‌رفت، مستند «تمرین‌هایی برای یک انقلاب» به کارگردانی پگاه آهنگرانی توانست برندهٔ جایزهٔ «لوئی دور» یا چشم طلایی از جشنوارهٔ سیاسی فیلم کن شود.
🔹
کن بار دیگر ثابت کرد بیش از آنکه محلی برای بروز و ظهور سینمای هنری و مؤلف باشد، ویترینی برای نمایش‌های گل‌درشت سیاسی است.
🔹
آهنگرانی در وهلهٔ نخست، وجدان، اخلاق، انسانیت و میهن‌دوستی را فروخت تا صدای لرزان کودکان شهید میناب و دیگر شهدای مظلوم تجاوز دیوصفتان آمریکایی-صهیونی به خاک میهن در هیاهوی جیغ و سوت و تشویق‌های ممتد و در عین حال میا‌ن‌تهیِ فرانسوی گم شود.
🔹
او قالب مهمی مثل مستند که همواره مجرایی مؤثر برای طرح و بیان حقایق به‌شمار آمده است را قربانی جاه‌طلبی‌های سانتی‌مانتال خود کرد و آن را به ابزاری برای بزک چهره جنایتکار بدل ساخت.
🔹
پگاه آهنگرانی به وجدان، اخلاق، انسانیت و میهن‌دوستی چوب حراج زد تا در حافظهٔ تاریخی این مرز و بوم، بیش از آنکه به‌عنوان یک مستندساز برندهٔ جایزه «لوئی دور» جشنواره سیاسی فیلم کن ثبت شود، در کسوت یک فروشنده به یاد بیاید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/farsna/437385" target="_blank">📅 11:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Ga7wsQGWbz_IkqLazM0cMJ2oNA1w4Vfvi9iHPmUqTEi51-Kzi6ZicxmP4Wk06q_Sqbxcv60ZfYSgnuP6ThslcJy_mDQnZpXW0MUNu2hO-rB-1bFgtkwf32w8DIP_xU13prvRIjn3u5nxcsNLhv1ydJYY2wLLzn9gOq5hERd9jy4uF85ns5roqWwtJK_V4e0uuWbo3Zg6Hqilmui8nT_CbesAlb2CBsEP85XrB9rnsw87cHBR4pXOP4QREX35tMGMOCSj8Ia2azkWX0ZaCOj8M85cL4CGJNXz5Cx9qAiAzXFJjOfj82_vjy6uWYcUPut5YSBIWOLHhT96TCVvcbVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ جدید دولت برای احیای تولید
🔹
سخنگوی وزارت صمت: نزدیک به ۳ هزار واحد صنعتی در کشور آسیب دیده‌اند؛ دولت برای احیای تولید، برنامهٔ ویژهٔ بازسازی صنایع را آغاز کرده است.
🔹
واحدهای بزرگ مانند فولاد مبارکه و فولاد خوزستان در اولویت بازسازی قرار دارند و ستادی ویژه برای تأمین منابع مالی و نوسازی فناوری آن‌ها تشکیل شده است.
🔹
همچنین برای واحدهای کوچک و متوسط، بسته‌های حمایتی شامل جبران خسارت، تسهیلات بانکی و ایجاد «صندوق جبران خسارت» پیش‌بینی شده تا روند بازگشت کارخانه‌ها به چرخهٔ تولید به‌سرعت انجام شود.
عکس: علی معرف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/437384" target="_blank">📅 11:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a365e584c.mp4?token=povlEIQURbpi4hbhNrGetoAACe17NDZ7GnGD6quroLv9OUzDJMGmRM4ORhvmQb6aRffgPqL5kKAX2caMJh73zxNvpE4bLW3Nie4eVSADGjUpuPOAknJaINPMTBGpewr3-6haLOFam-5wi3pqwJ7bBiwS5s0wfT3w-iiqxspcIffTgtw67RIOnEtRT2cHjrRRPrc21vSuGun6XwAT34PasAgv2a46mZjmBXBGBjFt44Q0-iKX0xPVRGDHN4G9rElWnysqkBqgUjQISEWJERJhgQJmB0rbuyPK-fRUkuT7pHGXI9YMKgIEKcA2S30yxts8LeW07J5-IeQo4L395QaDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a365e584c.mp4?token=povlEIQURbpi4hbhNrGetoAACe17NDZ7GnGD6quroLv9OUzDJMGmRM4ORhvmQb6aRffgPqL5kKAX2caMJh73zxNvpE4bLW3Nie4eVSADGjUpuPOAknJaINPMTBGpewr3-6haLOFam-5wi3pqwJ7bBiwS5s0wfT3w-iiqxspcIffTgtw67RIOnEtRT2cHjrRRPrc21vSuGun6XwAT34PasAgv2a46mZjmBXBGBjFt44Q0-iKX0xPVRGDHN4G9rElWnysqkBqgUjQISEWJERJhgQJmB0rbuyPK-fRUkuT7pHGXI9YMKgIEKcA2S30yxts8LeW07J5-IeQo4L395QaDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ طلای دیگر برای تکواندوکاران ایرانی
🔹
در مسابقات تکواندوی قهرمانی آسیا، زندی حریف کره‌جنوبی را در ۲ راند مغلوب کرد و قهرمان آسیا شد.
🔹
امیرسینا بختیاری نیز در فینال وزن ۷۴- کیلوگرم رقیب خود را شکست داد و طلایی شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/437383" target="_blank">📅 10:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3kuzbjC2qUKTF-KpCP8IAVP3EEFaf1Ivk1y1gq-xkmfVIXYxus6XL0bmUJLZEBNCd-_kPhfODhwNDkIXKI3W5Drdr8SwQS0U4FtxU_Gl8ADw8e7LySQauzRfh1G2GAkneYbdZ2j79wAV43mFrpf8DmoKluP13U6DVF8MK7ea_qKl0Pcy7Cns-AJjamkJPXj-vkOZLPtvNYNvOSeFJjysrFGJAFBstQ82XnFGujafHDJ_-PoW_oVuzfFd-2X3cCq6wS5NenG-uYGIsdQyWkVifiuW4NcZDhsUHftolYcyveDfE2HPOpwof_5bImjqVwU_GnHIQ0Unf6ZVC3TQyz9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیلی فیفا به پهلوی در جام جهانی
🔹
نشریۀ اتلتیک از منبعی در فیفا اعلام کرد که این نهاد قصد دارد آوردن پرچم‌های دارای شیر و خورشید را در ورزشگاه‌های جام جهانی ممنوع کند.
🔹
در جام جهانی قطر هم برخی از هواداران پهلوی پرچم‌هایی به ورزشگاه‌ها آورده بودند که از…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/437382" target="_blank">📅 10:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e50744150.mp4?token=B7vc07APqFy5eoxc0CUyZPhhzkt6j9hXNM6ocs-AhY-8eMdDZsyF81UHtVaBgMWYLS86yZrbKtJ9OrUAHmeejHzRnEYok1eOuddBTqdOs9EwF3v-wh9mMFbUci_e_AgLmJuyWEtksU5UJ4dovV4VGlnm6Nqz2YZhMHJZYlLTgzRCXoVS4xuqykA7W6CFlH6hAJ1z_1HbgHcByCaVSiRxd7_e1kz7qlRnEDTunnjHYGxnxnDhuEmFXNVD4jBodS9MXUYPoSatrNJAh_Fhb0q8ICryezJYZ2AuMsZSM4Q7fQ8H4n4n6GX7-kjEV2nNgRMcCMUC0Pf8UD7WtyKpE_KhhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e50744150.mp4?token=B7vc07APqFy5eoxc0CUyZPhhzkt6j9hXNM6ocs-AhY-8eMdDZsyF81UHtVaBgMWYLS86yZrbKtJ9OrUAHmeejHzRnEYok1eOuddBTqdOs9EwF3v-wh9mMFbUci_e_AgLmJuyWEtksU5UJ4dovV4VGlnm6Nqz2YZhMHJZYlLTgzRCXoVS4xuqykA7W6CFlH6hAJ1z_1HbgHcByCaVSiRxd7_e1kz7qlRnEDTunnjHYGxnxnDhuEmFXNVD4jBodS9MXUYPoSatrNJAh_Fhb0q8ICryezJYZ2AuMsZSM4Q7fQ8H4n4n6GX7-kjEV2nNgRMcCMUC0Pf8UD7WtyKpE_KhhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان: شهدا سند حقانیت دین هستند
🔹
استاد حوزه و دانشگاه: شهدای ما «سند حقانیت دین» و انقلاب قرار گرفتند و اگر این شهدا نبودند، بسیاری از ادعاها درباره حقیقت دین ممکن بود صرفاً در حد یک هیجان یا تصور باقی بماند.
🔹
خون شهدا در زمان حاضر آثار خود را نشان خواهد داد و این مسیر، در آینده نیز اثرات عمیق‌تری در جامعه برجای خواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/437381" target="_blank">📅 10:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فروش ۲۵۵ هزار نسخه کتاب تا روز پنجم نمایشگاه مجازی
🔹
قائم‌مقام نمایشگاه بین‌المللی کتاب: تا روز پنجم، فروش بیش‌از ۲۵۵ هزار کتاب با حدود ۱۰۰ هزار سفارش در نمایشگاه مجازی ثبت شده‌ است.
🔹
ازین تعداد، ۲۲۵ هزار و ۶۱۰ نسخۀ چاپی و ۲۹ هزار و ۷۴۴ نسخۀ دیجیتال بوده…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/437380" target="_blank">📅 10:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPd6mIKk6sQfOKsSl3L_34DOA4MBPFSum6HHV8XQ_pHHNilefmiHhYBwfZbr-N-MGOxeqlbYTFr2xmA6z3veU8v-rIkNodDvmyIbwmdz-Iun62EO5LlWiavqNwOKl1qNHfk_YsMl2UtCF8oalJrCWT_PdUXRLYfVN4AlMKobiTswQYe1mUyyPpW2ymSXZzhjNwjF9Eik1p2nedcnfLewTBJ3yKGF70Uyekv5K6gF91ZkwCmp-KZtxTQBFKNSC-8e2kyBvbOf7MCGYO_u8PFxzlsEobZbW2nFZub50dHMirzyQLtJhXn2Suy_kDcrDMlCIkNL-g0Opx42fBV2kSCBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعیت مجردهای کشور از مرز ۱۳ میلیون نفر گذشت
🔹
جمعیت مجرد در معرض ازدواج از ۱۲.۶ میلیون در ۱۴۰۳ به ۱۳.۶ میلیون نفر در ۱۴۰۴ رسید؛ یعنی نزدیک به یک میلیون نفر افزایش تنها در یک سال.
🔹
در همین مدت، تعداد ازدواج‌ها از ۴۷۲ هزار به ۴۳۰ هزار کاهش یافت.
🔸
بیش از ۷.۲ میلیون زن زیر ۴۰ سال هرگز ازدواج نکرده‌اند.
🔸
بیش از ۹.۳ میلیون مرد زیر ۴۰ سال هرگز ازدواج نکرده‌اند.
🔸
بیشترین نسبت مجردان هرگزازدواج‌نکرده در استان‌هایی مانند سیستان‌وبلوچستان، کهگیلویه‌وبویراحمد، ایلام، بوشهر، خوزستان، هرمزگان و تهران دیده می‌شود.
🔹
کاهش مستمر نرخ ازدواج در کنار روند صعودی طلاق، زنگ خطری است که ضرورت بازنگری در سیاست‌گذاری‌های کلان را دوچندان می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437378" target="_blank">📅 10:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZitiYpSa4N06fgnWvinrfiNd60hQdswSRYZt_RLF6O6iuyiLX6KxY5GjJfOzfh-MXAiAYoZa35hwvM-DZKo5JshxWBI0u__jeXpwZWxRQjDK3ZOFTpoCP7cggsPtfCuGwj8MOszZ74ukYRXBO3EuAFKirxhvVEwBjDelsbwgIIkf2PTr68b54C6THb4cv-2U_KFnX2G1-MAyLPj3ie824I-Ho3ciTL39Vh7loWxjiwPtvFdmTJBrKouZvs7hmeHbFoy3x2nLpbbogN3DXnI0ca5R7kWyMlhgurDYwRo3fIKNeDvt8oKVR3GxYt7RQJlGg5DnMtvokv2bj6cyySnnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ روسیه در نهادهای بین‌المللی: ارزیابی ایران از وضعیت مذاکرات به واقعیت نزدیک‌تر است
🔹
اولیانوف: ما پیام‌های بسیار بحث‌برانگیز دریافت می‌کنیم. به‌نظر می‌رسد ارزیابی‌های ایران به وضعیت واقعی نزدیک‌تر است. پیام‌های آمریکا در این مقطع کمتر مسئولانه به‌نظر می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/437377" target="_blank">📅 09:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec896485e7.mp4?token=OYOlKivblHGRThuZHJaC7BZ3kz27r2JYUuDszI-C0MThYpoAJ1U9ujLyKSrXxueWwX-2jrolA3eEBVx38BnmutWkW9qsGgHNoUZcscfkhrVfjdPeSNDPOdw7qAVyIDNBysNF1xMwTGr3t0lKmmtktqodc2IRfJaP-lo6U_TsyLudeaXwrv0IndiO1jCexsabx009XseCSeHQ3FQS-AQ0MvSm8s5UvvW48Cw2vqx6AtiPkpA7wz_uimhW_FXrlMsOVqOkc9wpPGWSR4zZJtWIdgsA5onA3hMnyfvWJfw7ZoojeIUzxp16cB7a6eAqQWIVaml8RKitIa8LSSybRRQuyCHKn08CvHNv2h9D3kcaLKcj665tQHrOT543eHAGk90jwT7ae1RHOB_YLPFLP3T76bs-Qp_O1ReDNEmvMwVqDGorLc9hOqO-f9lV8rQ8rCdUADZp8aSn7_-iPQGbAkDvWFRzGY-ci3u4JA3k_yjzZ8lK7WmbyHnft0_a-74qOuBRrN41Uoyrg7VWrYR_gDi7hCZgx11S4oZrxrNM0Y0aLTYjtde_FclenfnfuwPZAEX2VMihSKhjJq1TKU6TDVqUX65iOolIxRLSeLgHkpmqFIbqXepTweYK1xzacurBslKCbrU9XZk-59MBYl8Ht8kTBQG6GrxBAaM-FBTv1MqZSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec896485e7.mp4?token=OYOlKivblHGRThuZHJaC7BZ3kz27r2JYUuDszI-C0MThYpoAJ1U9ujLyKSrXxueWwX-2jrolA3eEBVx38BnmutWkW9qsGgHNoUZcscfkhrVfjdPeSNDPOdw7qAVyIDNBysNF1xMwTGr3t0lKmmtktqodc2IRfJaP-lo6U_TsyLudeaXwrv0IndiO1jCexsabx009XseCSeHQ3FQS-AQ0MvSm8s5UvvW48Cw2vqx6AtiPkpA7wz_uimhW_FXrlMsOVqOkc9wpPGWSR4zZJtWIdgsA5onA3hMnyfvWJfw7ZoojeIUzxp16cB7a6eAqQWIVaml8RKitIa8LSSybRRQuyCHKn08CvHNv2h9D3kcaLKcj665tQHrOT543eHAGk90jwT7ae1RHOB_YLPFLP3T76bs-Qp_O1ReDNEmvMwVqDGorLc9hOqO-f9lV8rQ8rCdUADZp8aSn7_-iPQGbAkDvWFRzGY-ci3u4JA3k_yjzZ8lK7WmbyHnft0_a-74qOuBRrN41Uoyrg7VWrYR_gDi7hCZgx11S4oZrxrNM0Y0aLTYjtde_FclenfnfuwPZAEX2VMihSKhjJq1TKU6TDVqUX65iOolIxRLSeLgHkpmqFIbqXepTweYK1xzacurBslKCbrU9XZk-59MBYl8Ht8kTBQG6GrxBAaM-FBTv1MqZSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهرداد بذرپاش: مردم ایران طعم شیرین خدمات شهید جمهور را از یاد نخواهند برد
🔹
وزیر راه و شهرسازی دولت شهید رئیسی در تجمع پرشور مردم دارالعباده یزد در سالروز شهادت شهید جمهور: با واردات انبوه و تولید واکسن بومی کرونا در کمتر از پنج ماه، آمار فوتی‌ها از ۷۰۰ نفر در روز به زیر ۱۰ نفر رسید.
🔹
روزی که ایشان دولت را تحویل گرفت فروش نفت ما روزانه ۴۵۰ هزار بشکه بود و در روزهای پایانی دولت ایشان به یک میلیون و ۸۰۰ هزار بشکه در روز رسید.
🔹
رشد ساخت مسکن از منفی ۶.۹ درصد به مثبت ۷.۱ درصد رسید.
🔹
رئیسی دولتش را همان‌طور که امام شهید فرمودند به دولت کار و امید تبدیل کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/437376" target="_blank">📅 09:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b60645fc.mp4?token=JHf6h-pQdIucF6kq6DW0Y1QR8lKyOgJDBx4dJxyugWZXKG2ACpF8rSTj0ubq9AhRjdzxtu2LJ2joh-nFhrcNpNpfaaqHm4K3S8bBINjDRFP0IDCSY27wgG3cKSuplQHcZdDxfOY4g1BdAaKaiziAnrTH30tgDJmLlv71zD-JQ2gyRpntZtoKzi7-7VU9RY9PyNudnrVBtAdfyCbK8PqcntOGfLOP6gAgRpR_w9XB6PoW73CSlzPLBGUjIwqZ5eJQpqaWyA6vL7qH_dc4GtxmLIc2uyRFSRrQ4asxdKJApsQZDOsp6_FoEU18vmjf3Lu4bAJVkSgFZvdMMqxFq-rntQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b60645fc.mp4?token=JHf6h-pQdIucF6kq6DW0Y1QR8lKyOgJDBx4dJxyugWZXKG2ACpF8rSTj0ubq9AhRjdzxtu2LJ2joh-nFhrcNpNpfaaqHm4K3S8bBINjDRFP0IDCSY27wgG3cKSuplQHcZdDxfOY4g1BdAaKaiziAnrTH30tgDJmLlv71zD-JQ2gyRpntZtoKzi7-7VU9RY9PyNudnrVBtAdfyCbK8PqcntOGfLOP6gAgRpR_w9XB6PoW73CSlzPLBGUjIwqZ5eJQpqaWyA6vL7qH_dc4GtxmLIc2uyRFSRrQ4asxdKJApsQZDOsp6_FoEU18vmjf3Lu4bAJVkSgFZvdMMqxFq-rntQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستیار ویژۀ وزیر کشور: در صورت تعرض به ایران، باب‌المندب به معادلات جنگ وارد می‌شود
🔹
سرتیپ نامی: ۳ تنگۀ هرمز، مالاکا و باب‌المندب مهم‌ترین چک پوینت‌های استراتژی جهان هستند. تا الان بنا به‌دلایلی فقط از ظرفیت تنگۀ هرمز استفاده کردیم.
🔹
اگر زمانی مجبور شویم…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/437375" target="_blank">📅 09:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437368">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLzQHw6iuJSEK_J-JHT0D85rOiddlodc12P9e-T9J_qgwRlWuqv4IQoQnTswHjYfRoAAAyBP1nko9T-YA1gUQ7xIsNOQyYEBndtaU7LdghFfDwV9wt9gQ8DhxtAOijY7sn1_vzuciOUEpPhqzC_a5mHuqzRkOtsW6cbdoCZexqwtLbOLkxcrWlk1ha3zu-g_Z3XBKlFQODx1S0TqhCEMfMHK2X4kHJ_TnYWafkLaZa5tgUGds2VAaAYzfh0-6spkZ4levSjot1S_UEJu8mKpJV1SoyNeX57wRAAi_X8sRWwk7yYClX5z5__wzHVfUU5kfO_P800a5tF07j7yZxjLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uprmq9zm94zNjzBy3CDarVW4Qf-GB4Bg4O8j1tH79-pujmJ_-p6y80m5-FWIICBlcxs1JLtDvlDJ7-OdrkGWCU2O5bclChNPrYUpDbGpuwJjqydkwJYIS82dnXHcI6Bhpvw7n4535SxkFSuhkwu8Hx_CysvpyOysNk70ig1qMPYpvzEs9kyKB40tCNwXQHkQxUNk3qy4nL8rzQ-Z-omhijumKL9UcJ3BzZJoKcKX1nHVjo4w-qoWp_rn2eL6QUfdTarhmEabjHTcmU7gvVVAdPohQx-pEafqGqWp7oRtVkpk9pPwvgkJ9nn4oPn6qXheg01o1yuGF7RgmnrethFxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqyRH4_E-USaOPzlsPFTlEDeug3ZigSuSXdV9iOVsG8cJz4XOJ0ZZuIoq7c0sAd4YBykRmx2QcoWhsckn9Jj9S_6ziZWd9dBiciZwLBV8Ix1NUz08MBBBYm-gXh8aWm5ifY7MQiUevs_0_T3LEzg1Kq5_iJojRF7go21ZuO2WIYnoPT0FkRhqYB5En42a5NvABxCJbD7AnPTaVw9hLGbJXk5FvhMJxgjhtXgc0XiJaLX9gCET4Mkpa_vcLtnXP8kBa7_oDzjy4fHiBQVGCU-MyiyelrpSKEG_DZB0GuKRBE14Ya0_tn66HFyt8NUM16N3azc1VWaB4S3u14aUxuQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyTWBRFErAkuTv1E11iapGWib35gxdshu9a5eJdMGaIkrHAJXg4gpc7LPqAVbjITjQLdAmWifaw62e8mKW68ydfmlyQGAmPAPE0nUt_rghLKUC-ZmzxzDu7YTW1AYJE07AjLNjx66RNSaL6ngKPHU_qk6SFsQcqBl6qx1JU_ah_ONmz1KtjzT6ZdJYfT4Dk3pn6Dcvr1o6D0Vj1HV3JL9-xL3cnSGM5EIM74qXMVf48kBUDu13xaswb4DwSTzrgYXohKz6OEKZvnGOqOGg_KluigGTVMh8JRtBzgKw-CVsdT41oaPSTCByS7hCbhu5IIv4wd0zBzevgkCtzyozmNXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLo6omQohlQxvVXe187cIG1tdkkNWB2giXj87nf9t-1a1SFBpPwtbBV0XRIvylLXzgP9vqDwS_UOlVoGJyxU6ITmf0godVDj253XUQnTebfNSE49afARyY5BH5CNODbf-uDb_t3nV3U6lKWWHwFvN0S_cdggfoDICyvHQWOX25Nd9Bydvq3IE_qYCHvOwXo79FqP0If3L0rbG4XhvXU4G-Slaj-YfYW6-I5swLTYzQPZQH2FVq_e_9g8Eqi384tYzlSMr8ocAT0iLDjGM04tzc7CFUsRW5l9H6i5ohtNDnLPLFFjHCdGcwk9y_t-kOdIgA9tQ5wWuIgfGkl13TTT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6k_DdTnuYMmhBjdJRkcNRuDf7gYZ8qhiMXpxT1t9hutPp_4fI8RQbNdFErkdtbYJOYMshR-1nEklmygw6xwVFOEF4xKpyOamWMDMlM2parV3aTOP2YkpzGQkmoUmb07EochbCe51hfkIBV_jhaAHeo8QsDXQmTLh8DfcmjAqgnGy0FPrMSG7Kood5xBR80j3-6peLgxhN1x9njO_--MyVVoq23-tPpijW9Q1mqSMv4Vy55abG6Bd-EinWMsPU_YWHvBt_AdBy-WH8BQDclisnrFfh_pEgrZsqdp0QI5saRCyYp9Lm8A35ofvV6j5jbYDEsjIAwTHnXtJ2H1n59QBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVGBhQpsZNuPDlFxEMrRibT15AgWia_HqquID6wOFWCVnP2CEYNYVJRveJcsT7ROvdRiVffKhNrJ0KuQFhQN8jMNQhVW7KdfWBS-i5mK7HouA4WUbImVQ4OsEK1dcyglfAMpMeLPxNyTFqUiEAPEugozEbRsJAFsoF0WuD9jXRYudBNGr1sPZD-H3GsgFD3yc5C2axrjFPTCj3Xi-st7gSj5FZW3oHan2AcsPB9fO4b8G0yZ-jZPEdLIR0sS5u_mVrwCvjFDoV7WYJ4iopXQYolF4z5GqYCTlFZLhNg5eG6sUJyZlXXxfTE-x1sFTgyCv-OTxz4oxpdMRQgWN4pQXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعۀ لاله در روستای «اسپره خون» تبریز
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/437368" target="_blank">📅 09:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437367">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9d099e73.mp4?token=QiezITeciZ7r3-GXUPYnAXAbswSYrsrjuwIHbx8D_fHLtnD8NsoajZXfj572Tul5QUi7bYefc9nHm0Ccm_zaoDjA38j998cWrBo6VkxhSo37wsgux3-t4jhhY0lqNgzlvK4WGUkLA5gxgCc4Xpor1zpRDnOmGo4GAtClmBN0ZWx9W0NDwJwhG7W8ghyh8o-0txFt5KP1Omy2e7D_wLf8Dvpl6THRjD2VpcVr1bMpskeybMUXwJhv6qtIDqUVeZPIwZfb8o2TC9TB71wWmHJB15ytxqwfH-HzHgbZQTHJM6_aI8YY3uhbXVNsT9k-nYuE1f-5dOpalnVKl0g63oG3iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9d099e73.mp4?token=QiezITeciZ7r3-GXUPYnAXAbswSYrsrjuwIHbx8D_fHLtnD8NsoajZXfj572Tul5QUi7bYefc9nHm0Ccm_zaoDjA38j998cWrBo6VkxhSo37wsgux3-t4jhhY0lqNgzlvK4WGUkLA5gxgCc4Xpor1zpRDnOmGo4GAtClmBN0ZWx9W0NDwJwhG7W8ghyh8o-0txFt5KP1Omy2e7D_wLf8Dvpl6THRjD2VpcVr1bMpskeybMUXwJhv6qtIDqUVeZPIwZfb8o2TC9TB71wWmHJB15ytxqwfH-HzHgbZQTHJM6_aI8YY3uhbXVNsT9k-nYuE1f-5dOpalnVKl0g63oG3iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم رضوی عزادار امام باقر
(ع)
🔹
در آستانۀ فرارسیدن شهادت امام باقر (ع) خادمان حرم رضوی مشغول نصب کتیبه‌های عزا در صحن و سرای این بارگاه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/437367" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437366">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654f03f44d.mp4?token=TJvAuRzLRU8dAW2gU4wFHZgbohE7x9P1wtdotit9ti_lbbaq74rfhmkL665JJIAX1TtLL4qfABdNo9dEKM7tI7DeRRpbDUnhzEfnrbMowKVo9NcAZfCNNfsyMdYCbecMMjoUwUceGROhCZmyiThMubTu6AJ5rMEjRU9gmFzzjM4AyKxhjQaMh_emXRI-dS45S11OToOHLltpyJzeHcRVzalz2C64XCN5Ve-vJOFOViX_gCLE4lhr9OGRqs6UevPkPkkFiysnO9BhU800fndO8wfFquB043va46kzINJkhVtLftJlEDzaOkgOXhhEFdy-rX1khDv1DqKTRXtrR07JAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654f03f44d.mp4?token=TJvAuRzLRU8dAW2gU4wFHZgbohE7x9P1wtdotit9ti_lbbaq74rfhmkL665JJIAX1TtLL4qfABdNo9dEKM7tI7DeRRpbDUnhzEfnrbMowKVo9NcAZfCNNfsyMdYCbecMMjoUwUceGROhCZmyiThMubTu6AJ5rMEjRU9gmFzzjM4AyKxhjQaMh_emXRI-dS45S11OToOHLltpyJzeHcRVzalz2C64XCN5Ve-vJOFOViX_gCLE4lhr9OGRqs6UevPkPkkFiysnO9BhU800fndO8wfFquB043va46kzINJkhVtLftJlEDzaOkgOXhhEFdy-rX1khDv1DqKTRXtrR07JAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در معدن زغال‌سنگ چین با ۸۲ کشته
🔹
رسانه‌های دولتی چین خبر دادند که در نتیجه انفجار در معدن زغال سنگ شهرستان «چینیوان»، حداقل ۸۲ نفر جان باختند.
🔹
به گفته مقامات چین، با توجه به شدت بالای انفجار در این معدن زغال سنگ، احتمال افزایش تلفات وجود دارد.
🔹
وقوع این انفجار مرگبار با واکنش رئیس‌جمهور چین مواجه شد. شی با صدور فرمانی تأکید کرد که مقامات سراسر کشور باید از این حادثه درس بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/437366" target="_blank">📅 09:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437365">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلیمی: انتخابات هیئت‌رئیسۀ مجلس هفتۀ آینده برگزار می‌شود
🔹
عضو هیئت‌رئیسۀ مجلس: به‌هیچ وجه انتخابات به تعویق نخواهد افتاد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/437365" target="_blank">📅 09:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437364">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur5BiZ8penCby1s9DHzJEKU4R_4ypbS9f7xPiUHrC5BW-5eUuIyKmC0CQ1V4tSZK5FhlqCt8WyHBYOHDhxBgVazdZxDiT5lERKozkuBkn4sqbVLFWMc2HyB-Tt1vhA4zAQf5uCtvaaEWd1cW7k9eZ_Uw-_FKuD0fMFg-GshpUt8e4B7qlozl4C8tXpRI7-7fFqoFwR-c3E1hciOIaSTCzpnSb-uRaRqwEvj86D65Bvhsbfd3lUSam-fms5Gru6ds6FPhqde_elZQ7HXEjEiNkZ3cGa2BS79OsdSr3I5OE0qoFbWjgcxSuvtO5u-jU7Pwoi8JX8gkUpeGFmQQxuqumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت دفاع: تمکین‌نکردن به حقوق ایران شکست‌های بیشتری برای ترامپ رقم می‌زند
🔹
سردار طلایی‌نیک: ترامپ هیچ چاره‌ای به جز پذیرفتن مطالبات ملت ایران و پذیرش حقوق کشورمان ندارد.
🔹
در هر دو میدان رزم و دیپلماسی تأمین مطالبات به‌حق ملت ایران، تنها راه برون‌رفت دشمن آمریکایی‌صهیونی از جنگ تحمیلی سوم است و همچنین ترامپ باید ضمن قبول‌کردن پیشنهاد ایران،‌ در اندیشۀ پیشگیری از خسارت‌ها و هزینه‌های بیشتر در ادامۀ جنگ برای مردم آمریکا و جامعۀ جهانی باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/437364" target="_blank">📅 08:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437363">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدیرکل فرودگاه‌های خوزستان: پروازهای فرودگاه‌های اهواز و ماهشهر از سر گرفته شد
🔹
اولین پرواز مسیر تهران به اهواز، امروز در فرودگاه اهواز به زمین نشست. برنامۀ پروازی به‌تدریج افزایش خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/437363" target="_blank">📅 08:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437362">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f5a54da4.mp4?token=Le9iR6p8AfcQQIlY1LF2DYLQFC0SawXW4kV8hT-xVQy1m7ljnW2cg_YGGirpjRgDRmBlki7PCHdgjZcvYHAF7o1Bf2gzhwwvixOHAWmXsX2IACHIylEVVVoauoDGuCZoBOEPGuDkuZCG4HjbZkuPAnQ0_GZJDt6_uxlvCDlnei2tLv2IJe-dr2YMh-6YNds6eAQG4XnPH3NJ0nxAGpCwTxUoTuYt4f-qVk9LEKi78zz_tN-ED72h4pfuDN10YuUkkxsfnhtxMvriEzXg1osfz9Y60qLmWIlYNmmfhGSC7IYPpmVB4Cihrmisp0HCCU5N2x-JHZCPHc8YSivFsawhgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f5a54da4.mp4?token=Le9iR6p8AfcQQIlY1LF2DYLQFC0SawXW4kV8hT-xVQy1m7ljnW2cg_YGGirpjRgDRmBlki7PCHdgjZcvYHAF7o1Bf2gzhwwvixOHAWmXsX2IACHIylEVVVoauoDGuCZoBOEPGuDkuZCG4HjbZkuPAnQ0_GZJDt6_uxlvCDlnei2tLv2IJe-dr2YMh-6YNds6eAQG4XnPH3NJ0nxAGpCwTxUoTuYt4f-qVk9LEKi78zz_tN-ED72h4pfuDN10YuUkkxsfnhtxMvriEzXg1osfz9Y60qLmWIlYNmmfhGSC7IYPpmVB4Cihrmisp0HCCU5N2x-JHZCPHc8YSivFsawhgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش استفاده از اسلحه در اجتماع‌های شبانۀ‌ بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/437362" target="_blank">📅 08:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPG3cYI1bpPpc2pQBglQIzGAmP0U9x_dpJXU45p3l5a9Z0i9IBgT4gQ3Qh2ZdvP7RIrx4VPxlVVS_HOW348x-SWX93dXnlA9CIdKXPAIQYRkrcXpNUUgCzt1vCECaBVxbfKw47edaMt92ziMzTNmu7llFNry2scwg14xxZ90EiHsf6mljOwHEjagFjZUlGPquA8CKvXL7fWQmbA3bBP0c1-FOzo1UevUKCOUV09CwGu9uEtPejITfzvmCD5Oea-lrdaA--aqgt1Vx1eslhH9VkJiLuNwQNvbN5lgGC3F-mgptP7-wAaWaUQ5es2GOKRA4LoLOkmvEAvcE42yisLcHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
طبق اعلام سازمان عملیات دریایی انگلیس این حادثه در فاصله ۲۰۰ مایل دریایی غرب سقطری در یمن رخ داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/437361" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo3bbxFvTBBc3Fp0xfGl0g0yBoFeCvNEXjzbE-n1dxr9AmMxBrR3mZtslGGu7j1VhuoFcJ1nMbW_q4GrUW1tTwJ1UV5Sk-_ZuH8ZY7OXkGiymXjCsHaBWxKUJ3YvQnsSov1GPCHdtis3gyjFszMg4mOuZJ2Sk7POm5RWA6-DTClJH-Zg9IQL6qxnGLfsPPFBh24sU4AzSjNgx_OUkXB9xp7A11twiLKsR3eJRnInA9A80l_0mNdbHnz__aWdwVcuDvlZ2iid0sWHtAFB7AQOigPonBr9C8OwUh5UvrFlbkoZ0YS6YyhyK_fwCmivZ2PzGC-qXUro3ybZLPXr0lgihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، آخرین مهلت ثبت‌نام کنکور ۱۴۰۵
🔹
ثبت‌نام آزمون سراسری سال ۱۴۰۵ که از ۲۷ اردیبهشت آغاز شده، امروز شنبه ۲ خرداد به پایان می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/437360" target="_blank">📅 07:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437359">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHQHgBx6ZM22wdRarcUNoA9s7Hznn9_kNm5EHpR491_f2YpYnf4POl3gU9EAvcYAWvc6iEeOzSaozPCxke862oV1iaJ6edt2_poaO-Z-XFlw8w-NgyxUYdVnAnPVJU4FPszBupvTBj-sFkH1x8Md1YfHwYfWFcxJo-Vr9Rcux4IWOrh3O69hFXLHav0yg641B4OnbvBSahq78QNTP2AdkLHQqjAfm3M7GfNxawMOTSAMYZP-lTndD5-P7o6Lg7WXWPD9CFgp-WOzugzg7oto_1TvqvsJM-fCkKZ6nyJwN1F9FXuKbgfy6aL4xTs6L5gvzdOLxFRutR9xVQ7bCok6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/437359" target="_blank">📅 07:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebae69aaf.mp4?token=HB3LdBRyD904T-9xGNG0Uiw9fr-sg1-mAZcBnkCT-wpxZGFXzt1ad79re4rYVtJsm2j360PCon43GWr4APVRLUp3Gwo971lMyDZIk7pdewIqganr0bJ8hfkyfFUzG79OqVqi-Q-dfdQW_rkK7QL88R4IOjUuDabVv5oPV2ajBu-qhPFjD7kGENb-4VY5kMM_byhXgoPYkypoCHBwjP4h4HLEMRZAoHmEHXmSwJPrZms4xD41Sxbq1Z0DeoAsZSMI6W32KRTWJzx5W_fQrxFMpp4l99Zya-Prc2U0G9GS9CSLW-CqnVcBBIY_ZY00MRsy2OnMfXr7HLgApT2yD7HSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebae69aaf.mp4?token=HB3LdBRyD904T-9xGNG0Uiw9fr-sg1-mAZcBnkCT-wpxZGFXzt1ad79re4rYVtJsm2j360PCon43GWr4APVRLUp3Gwo971lMyDZIk7pdewIqganr0bJ8hfkyfFUzG79OqVqi-Q-dfdQW_rkK7QL88R4IOjUuDabVv5oPV2ajBu-qhPFjD7kGENb-4VY5kMM_byhXgoPYkypoCHBwjP4h4HLEMRZAoHmEHXmSwJPrZms4xD41Sxbq1Z0DeoAsZSMI6W32KRTWJzx5W_fQrxFMpp4l99Zya-Prc2U0G9GS9CSLW-CqnVcBBIY_ZY00MRsy2OnMfXr7HLgApT2yD7HSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال آمریکایی: اسرائیل، مقصر فروپاشی زیرساخت‌های آمریکاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/437358" target="_blank">📅 07:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4AEl9_DjdJ6SYggEQyLIIhESL5QU1i4GJzUeZ46GMoWsdZCNsXs2HBJ1e_Uu-BU6bd9VjYfY-F_KsYo2zwOZoX-JZVxHgliNi-QP_llpdWGhMTEzqL-5CofLQwhII9IwuBU4OkV54I2myKRJYcpreziFedx7n9TNyHUrme1DzGEINq430ImGO6BeNt7MCdKcIvLAIvAszpApvt6D1OchqRq919zTHSkeljE27GkvAzROOl8k6jArx0v6SWU08OetxuvezI9bfTcKz5o9Vm85fmwRfy9XKDCKAF9QWZshEHe6DtRWuu_c3KsYX4wSozmIkQKh4JuNSlFWLPEbiPjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFbjK-UZyZ5f5tAOlZAEVsaDcLrPcseE1UdGG6Gid03ucWs0Vpm9GZuRR5nQSUZApPlxRL1H5Qvx9KeQxasYYDcbGeUzXFtu2Szx3yeRKxam548xXjxdsb5-RgsMh3pKANFMJlqe5OF59Lfl59WCNuEXHsp-qhceqaRdR9aMBOX3S6WxLh3t5YCd6QQsKz9pryK9RlJ-vJHU9LeeAk5M5BaPgLiBtZCQnOnH3-tskxaoYhrTYf7Lqk5xH9Bi_bLFeZr7qEDU1-f_b3iaJlhFj9Zp5FW7GO_BEMJEgINKjAOcLvUnDVRPon9W8b11l8ewkDKaGPTQUhf3iHhSa7M8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyC7B4tPd0mC1kFvGj_FQVvUs1bAo5-EKvczxVFmEPYT1XxJdDQMDiWhZYLh-1vmTAKds5SQIM0J8PZKd8OOeQfK4XI5LLRXcmVVDecHcRD_zLtYWaOeHj40JB9BjHCNjcNdHDdD6cBX22qHtLZYK90fehXf-L30f7EtXG3kD69g8frGl2y55yMz-iG1qmCFzsY7Tnkh9RBYoVekGPeLUUeca27dRwFF-UDjPyOx6y-Yx0yngf5EbJOgRGJT2xZkYROGV3wOZmnQ5ukSsjSCQ9F0r9cLMgG6oMIG1Ik6QprnZOPRAB4ajpeRNOYnV8DrtF94wjpQg7qbFkG3-TXS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ki5w9be6GC5_D2-M0ywtyc_Yq9wT9tSo209Qp7dzaWbcMeZeNjfddl1NUh9DSnX4Yz0aH8FafGBtHtuJqHNiET9iI9Y8W3bOGMwbymPtg74Rnd-0Ll_rv27JEfxwF47i-jX4IpRhEHmJmoVTgUjNLlJEJ-j3wpCvvh5i1NaQezjRuBuhs40FIeM8DtsoNIlCyC4m7gIUtDG1HOEfCPW8wiiG3WtzNfXYLR8a2mzTSeGIcAfPx9-yepxX5J8f8ms-TcwXjlq6u7me9HPi5GAsLWNttAFLZlJiB4oLJrnuc4KdTEkUq_f5aFQbbVa3OIJg3a0y0mwiQR4hJFlkmOXcug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jr8WE_C2uV9AmCEmFYeiiniWUXhw_2O32TkaJHVR37W2nO05JZbkSlE0bhbHNZFrUzWW7TkKhofWa-dE-rwnSebsM6mV0z_wBh7VcCx2rBv0Fmr-t_k7Htw4xYOxP_dpiJ9KnS1uyWuOc-1e-CMRYoUi10T6IRbQzTqahnf_jwi7IUm_5hzyJPaQP3r42cVmdeMWH3QKJvSx_AY-9_6UZ5zIqsEYh8JZY7M0lcReO3y2q8T6rASdzGj0jmdu859GMFFL3_etknH4uNwppqAgmudyBfJX5u0Mpspo08omfHOtqRetqV5vaU_ZORsOTS54KTPilN4nTjX6GWd5bnujfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HifLO3YBv2GAHGP_43StPVeE0sl43QZgLSx2vL4NSFEkYxn001CId_sK3LKguOa_rJwuvmv9K8dBJWnvVST2ZNwefpUqrRVnE9zkGJ5B5PUjP0Cm2KDbMrYsf2FsE8kh9kpdwElkK43R1SvwDjHFbDo2RoyFESZ5ipKNyX1wqiKUK-0J-EI2cdmIEqMqiwqAkOSbmEz_eBZPq-LGMB2hOnJai06ToHVdVqxTQyH_ZPbrJVtcyEP-BGZr35PH36m_Gbkt6HqRDD4Wb2z91br8rsDZldB8a0fnFhq4CK4q_-_BNrR4uZFerN5c7IR7FQcQpZtsBKFgbi8fOX7RT6uQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMMz4fPnKsnqbV7pUje1mb50M2SLCcYQEBxJcf0S71Ym-tt5PbSNzWwFm1Dl_U5g44kEl6LgZc1D_02cxWa9K7ta5BqiXTCXvffCuw5NZVZVUlKvr4W9PNaBGISBNpyRz0W7M-b4FjYGIFAQ06k2xTDbQL1lKJXD89J4C7Rhh_0v-YyEzA-2pHo42f5-IwmibwtGm9Hxq8PlxwICjRxTEQZgWyJ1MdD9aWOD-gmbm78z1DiajLz_OVe6_YyxsjSPCytP7szi6VGiR6ZUHbpPt20DBLOItN397MgcZe0bhBiZaZs2Nwhfm2uPQeI6xUgyM3Z0f9j3Ajj50P1nGPmAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nKyJHmG8TP-KHBq2TdpQEhUfMCh5BdBEmnGmjE1UYf6OIJxzN521L5htsVmMF9XBm_SEo1i0Do72Py5uIFB2w6DSehukRBul98FOP6dwDfJfyMgc2KbVU1UMPECkcXB5-lg01ukvINRj0rXnegTIvPoT7LN53_I0fMJbwN_vGpSoXR5hqUtoRiPikQyM8yH1k3WaBibbxsILOuz_zxQLhxzteJk05_Oy1ID6B4rH9XJmdk0GopLobjvRFoNjGHKsU0Aqfg75U4EpP03ouTTfQryRBT4sj33NF7BnNVWvCMu_j61_aK7WCjAF6tebX8JZZ-CQc_YkOCYpADLZUbNVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UsD2sgyiMbU0VZIz2VYDkQF1LT76hcPA-Xy5cDMKSKTOCd1yhuX-B32O-m8kxeJyzNgbdSOr14ME2v3BW3xTivV7XhlFnjtBsi77J4JTX17u5xx2_Vz3XideyNcgrHH_uJEsCF6c8jod7GvLtqusMTsbI6qVZT4MWb9MYL-hzkECby-TaUnOefJYr0TL1eulomEgg-S-mk9RjI-spqu5dtO90k3Epyb6emGimLKj8culLSjFkgyNJvw4JWi2jmMjjLqbGgua-z1xAgOFCxPjXl2P9weyyPN9s1XcDUJun9z5hpz7vOomWR1UvU0HJ29PqbONoB3K-mCkxtk4kdzxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMcVNUalF3vVtv-puD6kwEf5lNl7FobAEVUnqNTp4m-YDgUg_gmkvIPW_7B2tEtEZ3uoeF_XxweQ0HP-hvoqNnEYmf--DTjT8z6Z3YHiviSGB1p3Sg92QhXunrYqNtxpo8O5Yh_x97D-tEbY8V--eFuG3ipPIoHhAeuw06b3Ci9lkfYQJDAi7Y_NHkbMxjrW_Z_rr2Zti40_l94R08N8803Igk0zA2IFCw9elRQLJE_HCc4Xjz8OSNlgjMKbqqSK5ewL0Kn9eVvFu7UHxAHprAN1sedWGl-ss6KHuNhVOXrFm9e_oNAyfj9zywJrO_31dlY4wMsH60JQcdn2goKkoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزرعۀ لاله در روستای «اسپره خون» تبریز
عکاس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/437348" target="_blank">📅 07:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پایان بی‌نتیجۀ کنفرانس بازنگری ان‌پی‌تی
🔹
نمایندگی دائم ایران در سازمان ملل: کنفرانس بازنگری معاهدۀ منع گسترش سلاح‌های هسته‌ای در سال ۲۰۲۶ بدون تصویب یک سند نهایی معنادار به پایان رسید.
🔹
آمریکا و متحدانش در بحبوحۀ جنگ و حملات علیه تاسیسات هسته‌ای ایران تلاش کردند واقعیت را تحریف و توجه‌ها را از تهدیدات اصلی منحرف کنند.
🔹
این ۲ تهدید شامل «ناکامی مستمر خود آن‌ها در زمینه خلع سلاح هسته‌ای» و همچنین «خطر ناشی از تنها رژیم دارای سلاح هسته‌ای در خاورمیانه یعنی اسرائیل» است.
@Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/437347" target="_blank">📅 06:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAXmf7I_4u7zHL4nZY18vthj6sMsLT4kRZOEZHk0I2gX2va7cbyRZXsFVipgt9acgfg-9yeK61iLfsbrqxGNm3a7zr8GA25RPvkOoGvYMIMmN-GQe7bSt_mMDJFb4LD2LKVjS26-bFVkKAF6fKqYHCD1dxNChWD5FmW0YZrZiEsnK-4I0GiAOvweFyM_cJGeeagBhCsJ30yE_x4mkSvxvQEBQpMuRDaJ7yczYs5CJYgLa0FMOI_3RVIkdhkAfZDRy3H19godfEkR-vYwkatV7kRInFHWpAwv6ENqa402rGUMEQPMHtj56W4zr294aaAL32IMW-BaOwStRPpa-2lGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از هر ۴ کشاورز آمریکایی یک نفر بدون کود مانده است
!
🔹
وزارت کشاورزی آمریکا اعلام کرد از هر ۴ کشاورز در این کشور، یک نفر تاکنون موفق به تأمین کود موردنیاز برای کشت بهاره نشده است!
🔹
کارشناسان معتقدند کمتر از نیمی از تمام کشاورزان آمریکایی امسال قادر به کسب سود خواهند بود.
🔹
کارشناسان می‌گویند که این بحران ریشه در عوامل متعددی از جمله افزایش قیمت نهاده‌های کشاورزی (کود و سوخت) به‌دلیل جنگ ایران و اختلال در تنگۀ هرمز، تورم مزمن و سیاست‌های اقتصادی دولت دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/437346" target="_blank">📅 06:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7e771c78.mp4?token=YZL91vHGi-5g5F00utHOxirg-MdGy0ZMcS1Fd7lyZ3SwBITJrRW-k4yOseAaFeCZbjbtF3HH0JCgGpYtASYxtU3tr64MEsZlx9rgWfvyBlOoVJ4d3vOYUZc05kZa6gSFyIZmpjS5NK9rsDdrgy_4jW5SzbQFsgejM1fdrywdAimAGp8IVh8qepD6jvu2rrgED-1pAWRW5isWqF5CT1BcrGzO5F1e7sWXDwDykM9iyaoyIKWa_Fi8cvkLeYBJ8T_aAb99TAjjrvw0JT5Rn4Xkw5EnjK0cf05MdWoc3eYAVUCi22QHtS-4yFzw_yloUCLt4N--_jT-TbwciytlXwZsLZ9q5voEBBwxCEQC5QA5lH7USJ3sCiWAxUzzepQLQrSmLgfiX16vb3wg3Iw_Q9_u2ACpe41QXo_G-xVRIDKJgJ2tKJYLLtnU4y-FFmqLcUIL0p_S-ZIWQENQvgwAoPtUCJPpBXDqfs2C0MJaqtfh_SE6sB7_S-ArejGz0L-LOjbDnemjivhzMZcE91Wn7apEBxYXhbo069hosgaSTnFrNStk7v-2_S5VFAArcXyR_hvPyigSSUsMVfLQ6hYCxC8mfM9rnl4QA9grcMaECDIEun4B_DbAzzaoasLPoxMypiYOdXedFimJeLqhPfc1TF7kdtP-FmLJTrxanJKkUqDU3lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7e771c78.mp4?token=YZL91vHGi-5g5F00utHOxirg-MdGy0ZMcS1Fd7lyZ3SwBITJrRW-k4yOseAaFeCZbjbtF3HH0JCgGpYtASYxtU3tr64MEsZlx9rgWfvyBlOoVJ4d3vOYUZc05kZa6gSFyIZmpjS5NK9rsDdrgy_4jW5SzbQFsgejM1fdrywdAimAGp8IVh8qepD6jvu2rrgED-1pAWRW5isWqF5CT1BcrGzO5F1e7sWXDwDykM9iyaoyIKWa_Fi8cvkLeYBJ8T_aAb99TAjjrvw0JT5Rn4Xkw5EnjK0cf05MdWoc3eYAVUCi22QHtS-4yFzw_yloUCLt4N--_jT-TbwciytlXwZsLZ9q5voEBBwxCEQC5QA5lH7USJ3sCiWAxUzzepQLQrSmLgfiX16vb3wg3Iw_Q9_u2ACpe41QXo_G-xVRIDKJgJ2tKJYLLtnU4y-FFmqLcUIL0p_S-ZIWQENQvgwAoPtUCJPpBXDqfs2C0MJaqtfh_SE6sB7_S-ArejGz0L-LOjbDnemjivhzMZcE91Wn7apEBxYXhbo069hosgaSTnFrNStk7v-2_S5VFAArcXyR_hvPyigSSUsMVfLQ6hYCxC8mfM9rnl4QA9grcMaECDIEun4B_DbAzzaoasLPoxMypiYOdXedFimJeLqhPfc1TF7kdtP-FmLJTrxanJKkUqDU3lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما امروز در قدرتمندترین ایران تاریخ ایستاده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/437345" target="_blank">📅 06:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzpDuBS8jl_IIp3lhmcQwyfiJOT-0XQEgRmx_l9fWLWeduhc-xA6NV0knagPQfVb31gZdV9bGFktYTdVwCL6rs3xK2FnXa9VI_JugWhA4vlgghtLFvm0Ac0g_ZFDgSGtQezLnBqGUnuJ-ANj4D-7CrqNC-F0J0HO6XbEmyny8I-mmkVdkm1fKIYJEiFEUFv0DxjENR3VJfX4wmV3600CEgEBHr85_VDiHSHZwMC5SuIWL7FlYl-sdo4AOmqW9W9zBfRE_2MV99YR6IEFLvoXvHx-SagwIY2V3FHcMeKTrH9xwT6zlWI7NEWq3P2yBpxEYg2b7Dsl8LCIUxJSyWWnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف صادرات خودروی ژاپن به خاورمیانه در سایۀ بسته شدن تنگۀهرمز
🔹
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در ماه آوریل، به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران تقریباً به صفر رسیده است.
🔹
براساس گزارش رویترز، این فروپاشی در تجارت، پیامد مستقیم جنگ آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن، مختل شدن کامل مسیرهای دریایی در تنگۀ حساس هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/437344" target="_blank">📅 05:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4790e302d7.mp4?token=CL6y19dxEVF11FovuabKosydD2NO_2Y_V9dD7RsCb-GJvQiEcN-ECbstvvewzSGLRIw6zQwJTp5tKSKu88oH8V-n4LfhEGkmlHplASq9TifUnn7aL3r8vUBnCDa1NRiQNcrVQ7JuLgGTw0rtHls3R5kZoun6wh0YyqjRyDOp0CTF5juWCyTy6ZHqqyYuwJO-OXXyUaPBnj_oHZ98m7DClfVo2LUGcwMsqHGT8yJO1ckMbIvg6DVLNmqRxmodrIPT8tYPMq3xu2RnDyGVCY4pda6Dod3RAx61vJHOXKc1r9fKoy7sFJX1oErgoWTensvXX159gErMDcCg9W6gjJ9FpmVyLZRolly5ixea9qmmjLmI4rHcdJHy36RU0N0K-VUGwJc_sjJ2FM7wqAYmTmTxa6g9Uly4H3bMUCC5lB_mY9eTqiiF4gMBax0aC3iNdksqWxz13nemGggQ_Dy7WMgjYI_l6d_6FeLW_OrLNhzbf_0mUyyVi5Ry2ZhKW8cBCXUmanMsmbM5t7tyBpMlNpicfG9z_01jiRaBYbl2obEpHNKx2u_dxgxYbQiToVHeSR-rGnlw4CCu_7wTGOMKbdACkCqACcJJejxKoy8qQP6BzbvlrpBzy5uy-AwR_rfsi_rdNJTJjJeGFvklixUO0d889SnsVMm7kqk4CRGHlk4TcMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4790e302d7.mp4?token=CL6y19dxEVF11FovuabKosydD2NO_2Y_V9dD7RsCb-GJvQiEcN-ECbstvvewzSGLRIw6zQwJTp5tKSKu88oH8V-n4LfhEGkmlHplASq9TifUnn7aL3r8vUBnCDa1NRiQNcrVQ7JuLgGTw0rtHls3R5kZoun6wh0YyqjRyDOp0CTF5juWCyTy6ZHqqyYuwJO-OXXyUaPBnj_oHZ98m7DClfVo2LUGcwMsqHGT8yJO1ckMbIvg6DVLNmqRxmodrIPT8tYPMq3xu2RnDyGVCY4pda6Dod3RAx61vJHOXKc1r9fKoy7sFJX1oErgoWTensvXX159gErMDcCg9W6gjJ9FpmVyLZRolly5ixea9qmmjLmI4rHcdJHy36RU0N0K-VUGwJc_sjJ2FM7wqAYmTmTxa6g9Uly4H3bMUCC5lB_mY9eTqiiF4gMBax0aC3iNdksqWxz13nemGggQ_Dy7WMgjYI_l6d_6FeLW_OrLNhzbf_0mUyyVi5Ry2ZhKW8cBCXUmanMsmbM5t7tyBpMlNpicfG9z_01jiRaBYbl2obEpHNKx2u_dxgxYbQiToVHeSR-rGnlw4CCu_7wTGOMKbdACkCqACcJJejxKoy8qQP6BzbvlrpBzy5uy-AwR_rfsi_rdNJTJjJeGFvklixUO0d889SnsVMm7kqk4CRGHlk4TcMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از اجتماع پرشور مردم محلۀ نظام‌آباد
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/437343" target="_blank">📅 04:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khCfEEME5J5Eifztr9T6EaghEXN5oUYmhtVGQo1S-VQ_O06bwZUxhqt1pUvt6GdkbxaOu4Ahii6L-XAlkujXjhDyJg9GHKCERzxuXFDwfJsqOvvjx-UvrWEWRirlHa4kRBaxcAiXke7t71Oe1X4Y3hbUpVYTXpHowOi4Y2nWBXULSv5rRTrPPiIwhKgRDHj7BjP_dAU6G6fEQjMWb2rMmb8T5FvIeH8TqB8W37QHWNTx_xLLVwB-OHbvWyjmnT2Zlxd_aQTri3IzMzXk0Da8dB0eWXm0ri2v7ZHhJvPGWvJCaobt6IerfXc8QYKpBkMyyyr_x4fKROLNWhF9qiTJJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkcET9COJ0fjbJkCXItC4yWa0z4b_ZmQvRSdQCAgFSSA2iP_HWFHFimHfgOf6wQZq771bFc-dJADCXMjQMesv3BaGsd46lgf4UEMR6S-YV7NFKmo3woCnCto4fHqjL55Bp2bPRXiU3U3E4fKtzzSwRDcDjsYPpW9J2SyK6WvgWEDxO6n7SzJjYJlt28f84VyOkbXT0MvV8FZrrDdCWIfvOIiSwELcr-wxak3OvV_h8kVOIMGZ6F8gc0KLDLaH959pXMBoNhkYzSKS3L9m5LKh3-KAEYQ1BAunENSwTZd4jOK5ln09N61ngYPyyRgNpQibgUaJ82c1k8MT9G4ejWE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/di5YZprVG9lxSmnB1NAiBfK0OLmLE0phySB3gFqKHzmpUZJmZjZISH5Ih_9TiwNJWZg4rD-bc8lmkTAqT--uzQ5S64ukHbVR2qZtr65FBbhTTiRkDVm9n5wUxnEqMfl_UvtBtGl5JgWvOw689LbdfMi0D1R5dcw9lt-URwtP4Aj4sow6JKsVK1cwz06drsVznCiV4ssYGq2V1Q_LKOWOPbmt__SmtQz0N09Coa-VFO6hxKQKJ7EaAWMBtbjtH93jh7Gufck2uHw0UTSjGcdWISLYGGWMeHMZtFEXeHVrpwY0FnXI2tDiGz5W_w3nUUTnacKX5wFa8Ntw3-CVJxWygQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osDmpjwa50ebSTz9i3oyu3nu1GfGKoYyJfShXcNs7cXykwujc1wPQOtqLug8SbVJ6dioX7XtjzK1Jr0KIE1w27tJ8F2df-e8JclqSpcQ6oVy3-66Szz3kbHEMG2DRhBrHIaXoCdpgZoGTOwalDijnUANgjdDrLF3V71CDts8YXGWqap5-E1ZWW8AGMk3aZXMFLbnyF6wfz-lLsUX6VI5iFYJ4lld4MzQQq0ZItkcXpA-tteTpmauPABJ6iXH161UXMRPZejBtMTVQKClM5vybuueOpa8OtRkMtoBZ9mYliCXezPciMS0Kgs5I1j2Pw8yUd6qPt_0Wm72jm7t-0Nedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrDxoWsrlXSUF4tkEXd44buBk6jLvgfpCh1gE_LWOQnVU9VJ67I-g2tJL6OGnS0zHm9l3KtzdjZogcSxCVSRHNqIO-iGnI2UESa65XLUUUYDhA_7hd7s0eMNFRhf94_3e-VbuGuQBIh-l7aV48R3IgDwD-YeXr_m60MqNtRiRURmqeh7d66zEz84JqFaYswf2CapTRhHZD__3U2pcQ4ZmbutFEVTp3LzHBO72D34VLBeRWl3aU6sECtM_vELyqT8Ir4-Kf5xjyIFnYXyAyW8bIZbepYQZuFfwqRWz75s5SdJHEAhSexC4YGMq8SN0eMkkuIfk_K6W0GnccfWORg0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT1iDBqw9m97I02YaSlBAnLeFKkwvOxUb3mQMRhxuGvE1OV3rREUwDAjDQjw8R_y3nsbvJ04Ivn4pC0G3_75AZX-PQwk8jMBQowjTZBbYuT27wGMUuxK3kU6a59iictv5aEPFD6P-PMgrg4hRQUs0JfpA0UfZmMDjdQwp1rJLG5606Rr1YYHGPQo1BJ-cmHdD43rsS-5BZYlvZMeay7NQsC0ifECZJiTjR6bHke85vNEkSAfULcCwlTB1bbXGNedjnDRlfVzy-Z2_KJrSZLQL327pURH39LMP_Ka1mD-BvEL9mgxtcRgyxduLESxDwmQjIsLedxBhgww3gx4vfZysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mi1Gf2uD686Ba3bx3ZIj4Bq7c2xbDwvsNxOCL31y4eO9gi11fj-JrkPGlj4IdAc6XVAH8XSnqc13Ffqm2mIjHBS_qhjeb-4S8yD9Xxr4hKWRJUvLCfvGGKD0b9x0tK8Dw_gs3ozhzq5Aj68EfOhPL1UO6STfO_TdFl2mf_jQ6TzdGEBMkL14Gw7a9t9n_Dw6EaJMRWSJXk3d7eTa_xey5UhZXy1GRdlPeOPoVzcebonVKs6CkuNB5Hfbir5uoHQCieG-6LgBrzLX7vjgAxABUQah-DLEqlzDGB3nBik_diQhZrhxnfL-WSRxfiab1vGzDJ9Vv-BbfA1KF8zF6diDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovoUw7DxuuHqHeDUPObeJQx2ilwKNZx57aXQRSviEJ9OMhf4G-YT121LKjVGHV9dwsEYHMdee8DHGkr5WhpsY500n7F7LEwQxSWI8TuEYnITaH6JDst1241zeb7yRlgKqmwwhoxCPaNUI5Q9X1oL5A8hcMrvW1h1nbq2MdVBRlDq8Ofg5Vm2KlKWgnGl922nXYVA307dnQcFaoiCSf7TVmvY9OWSKzIsPKKwiATF_sb7CXz0o_1ffVfJjKaPYx9t5tAZzqlqpawLobDOjl3H7VLmBWNREZNueyg56Vkn9GjkwhmJAowbQCzIf-4OxO416kApaSniN34RSUXc5wQPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lcdt44x2U8B8ref64crS0Uw8L_2qSQylFletDehav2IM26iCh89DNVC3M5YBGzDY7_aR4XHdR0lWsut7aIhgX-5zv-c8QYLl2lMRCgKJju-rF51Kic7m6xKglLAezf_q2sMJKMWq25serD9WiNLE5V8YegC0wgXjn_6N7jTUa5xiMgDnQc4Sy6-3p_aGK7SG71xXBzhcJjodJDtFKpqRWMUJ0htsGt2Yp_xutp3kJKpJ98Aj1gqbxoc--T5lO20X79BvwXtVmLi5zqJrIhE29Gqp6H6DSqTdAw9c3pV_Go5Q0nf9gMrpq1YapEnhEMmBJ6Y7ghlWt57JbJptTc1dWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxcF3PU3qPr7g-DqGwzls9ZUTN8n0Qv1AwAypu0krv8W3NHI54ENV9OOiAaqYZ5x6Samkf6khl99L2-b0uGQqXm21O3i5Y6Gfej5Y5alClmZ7HqiPgBQkRK6RyC54yGPj6VCav27lXqbdEdrKg5iLB_yjXt4uWjb8ASAh_cKWWofBwJyDm9Lh9wkY2OuOotoN4_w916RgNyf7nTeRFg5M-PTVoCH07kpkQzLkEl8FrYGJsqc0cNIORe7RI0ly0P_cNr3fx8rxRcvvtRhxj2X6h4wa2YRaAThjM0KhjVgH2nEeiPOIWa_1wKp4Guma9o3_Ii_QodMIu3gy2HAUwYFsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قسم به مشت گره کرده
🔹
در هیاهوی تجمعات شبانۀ میدان انقلاب، مشت های گره کرده تنها یک مشت نیست؛ آنها اراده‌ای هستند که از خون امام شهید برمی‌خیزد. در این قاب‌ها، تفاوت‌ آدم‌ها کنار رفته‌ تا تنها یک چیز بگویند؛ ایران و مقاومت.
عکس:
فاطمه‌زهرا اربابی
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/437333" target="_blank">📅 03:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMWUEglBAiJl1Z8Rx2eepnt6vODiLBafzVf1d5ItBLybEHfeT6ZcLp_8MCJeyJxls-hnyfQcLlAoQUTI2JeczaOk2zkbfmFZ5Qd9PiyJoNgSkcotbe5WeL4lQSO28nht-2cEQK8Z0DmVmE6bfa-fESYPxrmWZNgKMh0OxKpohih4KBHyqSHsjzEYtleD9yK6jZ3WA7AHkH8_8k5UBUHzjl1viFnksAb8PKkaEo5N7Sn5Te0kuYeWLLhuJ7yNY8TbSN-55RM9F9iuKby6MzgUSqOG8PmnVqJyT0XS_FSmfzSXK55sxvCYT-usVaWENVpG7GN_FJ1cqWAi6A4X43fRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش سی‌ان‌ان از «ستون فقرات اقتصاد دیجیتال جهان» در تنگۀ هرمز
🔹
سی‌ان‌ان در گزارشی توجه‌ها را به چیزی جلب کرده که کمتر دیده می‌شود؛ شبکه‌ای از کابل‌های زیردریایی که شریان پنهان اقتصاد دیجیتال جهان محسوب می‌شوند.
🔹
در میان این مسیرها، دو نام بیش از بقیه جلب توجه می‌کند: «فالکون» و «گلف بریج اینترنشنال» یا GBI؛ دو کابلی که طبق گزارش، از آب‌های سرزمینی ایران عبور می‌کنند و نقش مهمی در اتصال منطقه به جهان دارند.
🔹
در نگاه اول، فالکون و گلف بریج شاید فقط چند رشته فیبر نوری در بستر دریا به‌نظر برسند؛ اما در عمل، آن‌ها بخشی از ستون فقرات اقتصاد دیجیتال جهان هستند.
🔗
اما این کابل‌ها دقیقا چه هستند و چرا نام دو مورد از آن‌ها در گزارش سی‌ان‌ان برجسته شده است؟
اینجا بخوانید
.
@Farsna</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/437332" target="_blank">📅 03:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqtD9O0ZdrxGKLyYr9M7Rzq9F4fuQLAyDoBP9UToFODQLWvbnrP8PHB0tEg5P6KCwpEG4Ho-YK8WLNSxOD7KBYZ5Es1UXNrlGdLuM1ClNUK8Yo7gg2PRMuKthivCFsBjNEns-gDnpZj8iYKqtr7FpvqNBpL7gx1yguf7fAvvXSMhPKYwi1YfCiB7w2IiKb8WaOaEEjbKai5ryEGC8VZfyc83_PuPqur3Tn78bPAqbRU-nIVkB99VdgXkmR8K7SWqyw9Orwy4NtE1493S3hQjxvQibyCl_YkrXIhAC_RCjWmQkyqAd3hlllmt7WIvQ2XD-1r8OSamKHhw_V37pE-uTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی طارمی به اردوی آنتالیا تیم‌ملی اضافه شد
🔹
طارمی پس از سامان قدوس، محمد محبی و محمد قربانی، به‌عنوان چهارمین لژیونر به اردوی تیم‌ملی فوتبال ایران در آنتالیا ترکیه اضافه شد و از امروز در تمرینات شاگردان امیر قلعه‌نویی شرکت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/437331" target="_blank">📅 02:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277fad787f.mp4?token=jYYkm92w9_MHewhpXsb_RXlAPaI5ClqFBaFFFHZezNaa-LBzBR_5i--egX_gRC4mAZeCc-NIe8NTX7C9W9BpsU-zTbTj1dqnCfGf7a36pqcsdIlDjdcGIPQio4Et2HyRrs5yF1hCAVX6sdN9GZAfnt6oJ4T0zDEEGB9_miUb8sPf7WC2uQE9gqnafZU5QdxNyNNOTsqbkepG9JBhAhm1pE1TaHGFrbgk27wJQt2-xka70cgA-QiAcxoSfXoa_IcJlqjLS3nIPPtvg2XUNgOIgFiDFaykCmUjRyp0p7s24xff4308rsDpsKD0aaMAQkOaFD9I_GykhCTaBnBxVeVHxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277fad787f.mp4?token=jYYkm92w9_MHewhpXsb_RXlAPaI5ClqFBaFFFHZezNaa-LBzBR_5i--egX_gRC4mAZeCc-NIe8NTX7C9W9BpsU-zTbTj1dqnCfGf7a36pqcsdIlDjdcGIPQio4Et2HyRrs5yF1hCAVX6sdN9GZAfnt6oJ4T0zDEEGB9_miUb8sPf7WC2uQE9gqnafZU5QdxNyNNOTsqbkepG9JBhAhm1pE1TaHGFrbgk27wJQt2-xka70cgA-QiAcxoSfXoa_IcJlqjLS3nIPPtvg2XUNgOIgFiDFaykCmUjRyp0p7s24xff4308rsDpsKD0aaMAQkOaFD9I_GykhCTaBnBxVeVHxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت عکسی که به اصرار ماکان گرفته شد
🔸
ماکان نصیری دانش‌آموز کلاس اولی مدرسهٔ میناب است که در حملهٔ آمریکا جاویدالاثر شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/437330" target="_blank">📅 02:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303b09821f.mp4?token=XV70Oks5yL5i0H-YNEvD3Nte-qiC-bO3wQAgbOj_P5tD6KOCZSJkfWaFV49BWzbIw5eCdIFk6cXwNrkm8iBCSDFxN8QQrmQ43-DlZ6eX8KiBsj6USbjYGCz87zpAPhSolfzsCBwK-hBTzmaEwH5E8_vehI6ex1-WYciwfRwPOeQIO5LIDQdaEhdE7sAc-xQjnXssZBpX-_RAQa_buuHFBvhXZW2QfUr712iit5GjB-rCOBn07qCzW6spNyrmY8uSzADCAo_cRg8OABcOdCk3dpPlU-Npok30aMeP3ROsYgU6srR0q1GZYrmj8_gOZoEjeNiTGYeA2yJCOfDucVM2Jov69IEhUFxSP5SS483Ey9OmAPlx3aWke7e2rN7f_c9KE4c0lpTpBd8IyfsgKSUMQfU_6mVj3JEGmkLduSejp736qOAQMnpAaYgSyDNMHqR_EmyplXeSOuwyGsdQZqsZQQWYgIy09zhWC12yDHgrI4knMEJTyMynVHroKlmCOuoCZ2Lk9t2dR4gZeubU9nM_ZTR6Q_4GPqeChVp3DNPM021Jg4Y9c88pJSMxAIKwTKX17riYaVkntY8Iy8kuH_DpfVJsmDiaeNkrbc-a9U1tT_N5uEHvXwPWZ4lQ097V4HFvIj2gf5YzFp4Tf3K0csnxG8tSoui96uNSsuD6OACEY8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303b09821f.mp4?token=XV70Oks5yL5i0H-YNEvD3Nte-qiC-bO3wQAgbOj_P5tD6KOCZSJkfWaFV49BWzbIw5eCdIFk6cXwNrkm8iBCSDFxN8QQrmQ43-DlZ6eX8KiBsj6USbjYGCz87zpAPhSolfzsCBwK-hBTzmaEwH5E8_vehI6ex1-WYciwfRwPOeQIO5LIDQdaEhdE7sAc-xQjnXssZBpX-_RAQa_buuHFBvhXZW2QfUr712iit5GjB-rCOBn07qCzW6spNyrmY8uSzADCAo_cRg8OABcOdCk3dpPlU-Npok30aMeP3ROsYgU6srR0q1GZYrmj8_gOZoEjeNiTGYeA2yJCOfDucVM2Jov69IEhUFxSP5SS483Ey9OmAPlx3aWke7e2rN7f_c9KE4c0lpTpBd8IyfsgKSUMQfU_6mVj3JEGmkLduSejp736qOAQMnpAaYgSyDNMHqR_EmyplXeSOuwyGsdQZqsZQQWYgIy09zhWC12yDHgrI4knMEJTyMynVHroKlmCOuoCZ2Lk9t2dR4gZeubU9nM_ZTR6Q_4GPqeChVp3DNPM021Jg4Y9c88pJSMxAIKwTKX17riYaVkntY8Iy8kuH_DpfVJsmDiaeNkrbc-a9U1tT_N5uEHvXwPWZ4lQ097V4HFvIj2gf5YzFp4Tf3K0csnxG8tSoui96uNSsuD6OACEY8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان‌های میاندوآب آذربایجان‌غربی بار دیگر به صحنۀ حماسه‌سازی مردم تبدیل شد
@Farsna</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/437329" target="_blank">📅 02:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5Uxc8YpbWPhtOQuE1qO_ywlkfbQsN_vmpEelWgACok5QrEE6sIOpXLC2V8EihMR6iv34jv8dthgihkWrTLpQgclaKXCH5dTro9CE-vUfc4_XTT9BzHHfEzoOsjYBIWWm22fj599jeeEmL4jlc65znX2pdYzcfo2LNUkgnytkd5oOo5y_jU65wZuCT2ZzSzO-ek93Q2sstx9HaawGMp_y8T-pUKuBYaLmOdPOuR2earNRTFiYN5M0VSVIqYDB9aRb9CAo5LrJnMXoPzIFIYyJK_toorOB4tPxBeeQtw-ZsdF_e-DOMHqje_Tc_ZCO01gCRxMFwqJXqafT6ZS7zHk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آملی‌لاریجانی: دشمن در صف‌آرایی مستقیم به زانو درآمده است
🔹
رئیس مجمع تشخیص مصلحت نظام: ایستادگی ملت شریف و نستوه ایران، دشمن را در صف‌آرایی مستقیم به زانو درآورده و او را به سنگر تحریم و محاصره کشانده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/437328" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎥
آمریکا آرزوی همراهی نسل زِد را به گور می‌برد
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/437327" target="_blank">📅 01:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437321">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdH0LSmreodG7I6st36fQ22O0PnUlzskJL9ijTe_NgnnhaSAg9zlQkQeiXQAK4byKKjUWfCjLgKarIEe5iMBREUPFjOoKiClxgKAxretBairGfkg5LLgrQU9rDV3aZajFWgBGdipK_9hAihSsNianiguvzJcDngWLvfNBIKAZdacoTZwXx_T4WQvbk62_0SzVuo8L_R51kYV9xnUDnFFXFXP6uZMFa0INZ6xPx4xWWh2AG9ZO8Z3m3xpGwTyuYstU0twAL-TnrU_UZSGIDNduGNQdJ27DMicffibETacAO9EX3L7mO1NwLZFKiiJRiBmN6sMr6gK150L8G-qaB7HBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyxUpSTR8Kesph_s82XdxsZj1C9B_8FjLPKBW8QPYrl8JDjOg7UP_LaTiDDf3UvQhPoyOkwFPquaWzlOMBu1wUpqiv81bTKwK256KCI4TuXnXulaQl99NvcPS1VNB34Z7LvoMKMjutco7jQz1XkQQ8ib5fIOWKvbLAxqc2c8Y456t6qYDT4DfzGhk5iHBZK_M-QG_CrRxlen-XdPDzIJH-AWFxgSL4UqXqaLV26dOqg6-fZtSnJny4J8wq5RMQhHAKrXCgh08M1xwHCWYaUSf4O0dBIx4pKlV1o3a_60HHdC1xRRbfPP7BkBoiTrs6rhQupWF75DDwcRK9zoGgnHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShOzSwOTnG8Woq399nS_DxpdKmZVmakGCauQUqfl7Gptw-PTHkSrZRnsJvg5WF4Rr4PrpGyiWUqW_l3noou7hyPn6AqhQnP7Cy4_-IcMyOL6IGV8zuX-HxrABpb5jZksXKNJ-R497IIXkVshog9nIXG2KV34E5-6z0dV2F1hTi70mV3u16wg4bI-Bek2_7aF7VFaJhLxb2LZHL1rhn79sn7GoR0AJ3A8puYLXZ6zv4VjUaeU1mxa_nw13JucA09Ydbk-p60TzT5Hms8D-lvF4STHVdlkbZIVTT9SQi0H88aT0veK4tDzrukUUzw-_aOOVPJEZo5rVCPt6gkH8-Rasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1bQiWrlmXl8fK-m7EZ_SeH4M6jTU1Evex2F_igcdL5-QX-GvGzp7wdrjrEw5lvCf-oimfPv28gI54BqjDfMUVgLf1HTKrhDIKlc14G_SNMFKa8GYKd17RWTAhDSbqNG2dQvQNd8Qv91tuKde10sglZorrJITE_UVT2rbqk9wRVScpE5nlAEf_a_0NHkCpfheb8ZrHCC1qv7NduZvLrmNTVDO9iZeZvCb98qgRyY3yC9SKZrab9Llr163s5Pqe1RISyW3CqIb3RmHuPfLQz8nxaR3ce-PL0Jyaa_k1zdXW04k_3jtcTWXcpJM7zhPygAuyVlmgmCypMKkcxUt_0yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGv4hGeUPjxrjfXXrA2J1b0zAV1llym6avZiHrSmxHsMKxEyISle257y9VxWaWQnJfXI6y-5m1mCbRdGk7guOFwMzgHbJfUV-VSEfb50M46oIS0slaT0WoQ_4znF7hPV3C9Tei7SS0uCSgIjJ5M8eFGy3SJIaLxxWTimq9Nf8f2fQyboZ5H4ZeRTmGeaE3SGiPodEl7iSQmTddQj_AXMVo7RI-_NeY0PVnKzYpS5iZluempKPoqIz1uWezbNIcOTHBEefcFvYgKJNdw3i1DqGeLxPufAaUd-vWRBIBLF4MBMMC3Dl7FfCA1zV6sXCHYN41az4bL4o281NJ2WWV5NEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0Iy_MhK20HPhMhSmqeL_xoOqq8yLQ-m7nX9K_N5ScvjW5rbpwIdWFfpXvcpJRvkzMg1t6PcVmpNXF8VNc_Ccpvm7IFhu5OnTa8rOw3Zb7sYDchZsKu1wAgdFtyqyOIYrdECCZ6PqlqIO_OFuTVLfUjSosWJdOm-S4EGWmtMZshiwG9pOhT90kjKq8nk6xS3Gj94I_FJulEJ8b8UqxfffVnWKLDAdJv-juPkShsVXTjkoubKogsRHnuAPyxgB2ZRj24hbJMfs9ZDbflq5Kn12WNp9tRw1JGufP9TP0Wm5n2vPoKeq2QHKdlrKC-f-HxlqpT4dhP3NGPiEALcq8KoMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/437321" target="_blank">📅 01:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437311">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX0DSMI_3XKHXq-0YjVELt3ihfVXP6jFIo6MIGjbVRQ6bOKo8pWKz9Mq08CWuhMtPD-3EiisWcQvYzOY18fx_yo4HLaxDpbPknlvuB-apX6lGZNSzh1pA06GYHaqqrs8V9t3RrotUA9iqpJbk6C0IQoLfiAWdpgseWDUifL42HQpIs3MLb75aAI58hqd-sNyJ4eufHPO3dxTIFjkXpbjh-uNlUbCudpE37xFKN4KX51ya0hG-FG75QrBegyIYt3xf_p96sRjQaJUTEj_CNMmOgirc6H3-RL1EDE_Qd3e0WpZBBgPPVeK0UN3Udvud8WZ55l1fv9nmL9OtkopR8VawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIfpRvq4eqduVQArzZJTjz0-qFtu_2pynI6tlhKRPZkJSUANzzC7lVzXTPipGz0YaB00SacabRre0H-gsZLKz_NdpglhWONhKpFv3VtaA3yufCHrL2P2fggyxPtb1PEa0MHgLdHqOAEUKXSKt3vu88SvFCkuVDqvgb0QwJ10gxonpUR8AcbN-6EIWPhz_I9w_DgbgcGGoNNZM1HgeZOJhke9E26qfe0crIx_2HAt7ScsJ_QDMbEglwPbCn90FQcifoNe6GSH0z39QjOqOh0e6LdzUN7K4GKq2MdivHdSnTMW0NOUN_MqSicgjGUydc0fX5FWxfxVNff_yLArcg3Kcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjaNx1ULjK1CP491b5SsaTn91g8Iz-Cdp_JVEzEQpItIAmWu53AUkYEFi8UUZ-DKYW0s7PpwzgGXXlYjT6yM9fnS4gkC8al0XDYc_faxk_JDyKbmlhE0PMrD4O5Jn2AnCRTpiFXR7iWr5sIyq6OkEhoq8i10Hgck7Cr4J9OHrNepAmkr4HGk009EuXoK71wPnumvgeSmqRmmjOZ0OGEmEWapxtGYbb7w4wTK8eKqkCaXdt5VVPxSZooqRzWGDJcU-RRSW7KlYqKKjHxg-ZZUlSv_prksdX6Il7Yg6SDErxuVx9sPB-NHsmSztc8kgXqTg18LswY29AsgKrjnlxy_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEjdSfG3bDWMwVBt3yE3kLL71DU16sryn0h1YksXXbkTk-SRGmOBahNqmL_PWKWxEYJoi7PD78AMHTJ7NBwBD_uO9YKFWVO9oekT0xVSIW0s3cLmV0sUFt2EJ1fPlFaQFENAkBpH0EhzXk4IsvlLc1OPxqgJGabUApbGodQl07PPYKmmhIITfK3ofJkAO89h2yjXbzRH3te6HRlr_DUoC1Wj17aARmfVAfkEcrkEXT24LrTB6nd9BCxO2D4k-4zKhOowTQSJwGT7rBOQUYSCB0gSZHzRZSt1y7k35A05ajVQ3Yqk2ZJJMBnKVY3UhvEhhF5JsIiX3ZJMkyzmPSD_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGl5l0CneT3WLfoN0krilrKaRKL32xmCXsE3I3sRlM_SI2BP-f01hh_bKbZqbKUZgWDWyr5nvRoUOBeV86-vBTBjXYYeQwXTeQyx4-L3gGC9v7LRnnFlF3tMEzMKxnr9BE9ikxkFG1EaHT940lDlpg7dtsrri2NG1Dn_CDE2wP1Abp0KF3pAnHvV3pgKpM7J6Lcip2V7RNibVF5t7f-g3wq_pBzkT8nGc0-8GQdXAeXlwdvgC4Kqbu8QmtpxBN9FWqyruOH6-P9-dfelOj7XFV-y9yP_BpIFP9IMYEQYyNSK0JYdq-oPHh3uUTH23KkSMbWMN59PLJZEpxlzM2Rqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUZX35auIVCpMuk4DDaISK-oGnYCCrzKEME2UorYXe-bNR47XA19z5_rEPm7jyiwlgAmoLEJqfXpQwGnscUEQKAHO3ZqkCr9GLCc3BBznAUPVWx4XaPOD1o2cH3nNJzpJjE3FjZybrTC2l4OV5lEP2AYDGISdbuU8MLIXMHJ7tuYRDErnHxL1c4Oo0ANJZm1MBOGeWbuefv7ZIGvMr-Bm3CcjD5ip15IIOpBEn0DNwJPAEhu44VOoIMGG-IUUoHHLTVy07XTuXG_saZTiR3RbOle2LQEi-2XrA565THFv65_oYdiqkMWhBCDCTeoNFLP-FWlzVsNAngIpUr7tXH8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2jdsRlYIGP4_2flID5mj2mfDMy6BWdk8mMSHuEhLEwQhiNKzfcoksnCxqX2tBe3L0yNYJfuH3qxDRIlNTygTptJDdcEx9S8y7PUYYHaeQm2ChxXmAKv8cX6vlbq1wywQqBfWSDfHU4DKMgrlnHq35GoYkFHHHWAtOP_SGITn2SlCo30vZ671cc9ejFoQTsue4dwUWFmQ38kam8NybVF0-iyeQmGotnjy1AquM6uoSJC12W0N_Sapyk_oBb2xT_7SbXEGYppVpy1xlNoVTmc0jzjfqn7wVSPLWyRklDyooHsbvgFbhAtFFC0Y1uPCG0IIjFNLg506mOQHBS5ghVhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v59WRUC5fotuGFV3lrz7P8uaNdO6eQfTK5e7Iiiq8dBm631UinjtjRn9CO7L-kd0z-SaoCCIy7aCgiMEg5e5djLiAx_zgIFMbGTAYbwjmIAlJegxNXACTUTFNoapgj8cK2QIIbBz-mXC0xcYRTSlScBguhyns5Ai5eYD7uQduzYeSKXdasCezyjX3YA-VYSDBrCfYkoT-DhQQkm6B2a1284fH3-moDPqHcPAFXgg8f22aPyDPe-LClgmhS5z9w3SFdNsNfC75u9PxVFQs6DkcqXvMynQLFMoJJ33tVW07PzCZ_ZtCDPQy6w-TWmxTMLdIB_3vrWfupRmQUSdgqx43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6ORN4-zeu-WRiUpQT5-ctbhhPpu8pa-Pcm0a9woTnFg5_Xh-kHLhSPsUpZCsb6y7gphzeQMcgSzgKG8f1olaR9TNwVhr-_Gt5h7JMM4xaB1Ss99YUdZgabNdWZy4ZWAzYvFz5QQTgUMZm0cPaoEszHh9T5xU_wxQEzKupFVxLOnrXx9jHw98Z-A-BxEWaCzhm5PgN6Is4b2HynR9Phf0HbUsRMmL7s99p_lwdhAwUzwsPrfwSthoAnapKJyTW7Z1bLZrDUS5vcr5CHL2IlQi5iCdEMwGvNf3TuvniQYJ20HWtyHiCBsHNaIa12LVzHf92EygrpN5Zm4qZbzyfArZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbfUc2oGE6GIJr5tuSuVUBJf1JuiirsK2jkigb9obtc0T0smy-zYQbwYyz3KNv73lNXMFn0M7i7dw2Q-gnHDtIa24h4EcRhJMJMndf7cbCSeDQS0z4j0jc_VRg7N_BA-pB9smP-tC6sa3i2CN_xfD2pxRIy-2HmA7uy77DAkXAanh80GbU_aTOWkX--c0TxLPC2V1FTvXDb3-6AH2ZtLz8diIrw6S6AvwuZg8teX55g5YygANghSofWNIE8crdOINvCfPvCwjs9L-1HvxAO87TTidlLwmmwr4cH-7E8MMVjpUM0nnfBom66VrZ-aRCowrGmHUzvpUnHc4hN0w3iR4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/437311" target="_blank">📅 01:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzZaAvOruDYP5cPUeTumS5AVs9SLhhZU5uQ5y9hCLhUikJNcUltgc4oF4QTtwLD1qPBw64icZ9Z2waFe1h2uH4Heowkz97MdYT_w9vBYjt9191Sfs2AvQCsQGnLOKCTQkI-bDThYVuglYtmr9RUfjfdZtVpTFilMRKG98diqSKP9pnoKQ9w_TQA2JZMgGUSDAKXxinyHYebqA7MrjQa8vqeJDb0UBXOgp3oFk115Dfy-KffVo_Bmf-T4xW5ILyjP5AcvNpZ7JrGbBdG-unJEV-w9sGuLSR52YqpwTzdA4mPWd7GAcPIT-6JBcejkXRHO07NANEEueyaBVbCAM5c9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با دبیرکل سازمان ملل متحد
🔹
در این گفت‌وگو راجع به تحولات منطقه‌ای و بین‌المللی، به‌ویژه وضعیت منطقۀ خلیج‌فارس و دریای عمان، تبادل نظر شد.
🔹
وزیر امور خارجۀ کشورمان ضمن تبیین آخرین وضعیت روند دیپلماتیک موجود برای خاتمۀ جنگ تحمیلی علیه جمهوری اسلامی ایران، سوابق بدعهدی آمریکا خصوصاً خیانت‌های مکرر به دیپلماسی و تجاوز نظامی علیه ایران به‌همراه موضع‌گیری‌های ضدونقیض و زیاده‌خواهی‌های مکرر را عامل اخلال در روند گفت‌وگوها به میانجی‌گری پاکستان دانست.
🔹
عراقچی تصریح کرد: جمهوری اسلامی ایران به رغم سوء ظن شدید به آمریکا، با رویکردی مسئولانه و با جدیت تمام وارد این روند دیپلماتیک شده و برای رسیدن به نتیجۀ معقول و عادلانه تلاش می‌کند.
🔹
در این تماس تلفنی همچنین راجع به مباحث کنفرانس بازنگری معاهدۀ عدم اشاعه که در نیویورک در حال برگزاری است، گفت‌وگو شد.
🔹
دبیر کل سازمان ملل متحد نیز با نفی توسل به زور علیه حاکمیت و تمامیت سرزمینی کشورها، بر ضرورت پایبندی به اصول منشور ملل متحد و استفاده از راه‌های دیپلماتیک به منظور برقراری صلح و ثبات در منطقه تاکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/437310" target="_blank">📅 01:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35821f22ec.mp4?token=Gyn_ZWpGml7_j7X3ctkyTcUCT9wm5L9twrtHPQbUSJzppB1lMQmySzJ9BG2oKQZtTJJ6hUl7HUMbdlWRy8ypMJ-yTY375029l_HIyKhljxED5qqwhXBIQ_SrNBk8fafaAh7wi3h-wPHQ1EVS81DXhlWLmH-2YM1JKOhPIiEPCFaHl7nIZt9UvVcd5oMGr5pLeNKqJF2FRvAJbpxQXtWbt-xQzBVxLYV8Q1HUbrQZajyiNKfsNzSkCjEHU4Td9iWaBfDEOyClMQ9J5VEeNCt5C_u-PGB9k77nFGy3nAgk9CzFviHhy5Yn6qgddlLfcnNcP0-bawjBMTT4wM80vz7Skg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35821f22ec.mp4?token=Gyn_ZWpGml7_j7X3ctkyTcUCT9wm5L9twrtHPQbUSJzppB1lMQmySzJ9BG2oKQZtTJJ6hUl7HUMbdlWRy8ypMJ-yTY375029l_HIyKhljxED5qqwhXBIQ_SrNBk8fafaAh7wi3h-wPHQ1EVS81DXhlWLmH-2YM1JKOhPIiEPCFaHl7nIZt9UvVcd5oMGr5pLeNKqJF2FRvAJbpxQXtWbt-xQzBVxLYV8Q1HUbrQZajyiNKfsNzSkCjEHU4Td9iWaBfDEOyClMQ9J5VEeNCt5C_u-PGB9k77nFGy3nAgk9CzFviHhy5Yn6qgddlLfcnNcP0-bawjBMTT4wM80vz7Skg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طرح جدید فدراسیون برای سهمیۀ آسیایی
🔹
سخنگوی فدراسیون فوتبال: طرحی وجود دارد تیم‌هایی که می‌توانند سهمیه بگیرند به کنفدراسیون معرفی شوند‌ و یک تورنمنت برگزار شود.
🔹
البته بحث قطعی نیست و فقط در حال مطرح‌کردن با کنفدراسیون هستیم‌. در صورت تأیید AFC مسابقات برگزار می‌شود و تیمی که در رتبه بالاتری قرار بگیرد، به AFC معرفی خواهد شد.
@Sportfars</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/437309" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OifbfhBVvo3p-yJ5fwLeQMGFMPIDRTIX00EQlS2IkEpvzgWUukyG0Sw6fEjBAEUF2mc9RYPQd-pvzH1tc_UecXA7TTZJFasma_HXUXApJNMetAfZq7YCa4EjMBVSy_YGtyMcvpL5GuixeB200blbFQVfT8nDUJ8XmTo-fGsY38S4q7Bm1JC5Av7wuq1oA5oZnMTOKTGpgai5sjPM9qUOQjSu1gn578iPaKhGH4vJOADDxglbhE1I0z62NRHLr8IeWD9YoBVydpZCDubmmU_D15qblHWluBAjlBm7rqTfnpoG_tOrxZAXYWqLZAiWaaXB2Duzk6KvZS9Ogqlg7aHw9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ فرزین برای هدایت اقتصاد ایران به مسیر رشد در پساجنگ
🔹
رئیس‌کل سابق بانک مرکزی نوشت: اسناد مهمی که محورهای اصلی برنامه اقتصادی کشور را تشکیل می‌دهد، اسناد برنامۀ هفتم توسعه‌وبودجه ۱۴۰۵ است که هر دو در فضای قبل از جنگ و با پیش‌فرض‌هایی تدوین شده‌اند که نیازمند بازنگری است.
🔗
یادداشت اختصاصی محمدرضا فرزین، رئیس‌کل سابق بانک مرکزی برای فارس را
اینجا بخوانید
.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/437308" target="_blank">📅 00:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugMKcPTqrL6-1EgrvvHHmQiLGpaeCPhpxFVBaUrbef7bZ5QlHBfQ2PcwrU_1QCZqPnbwECRV0obomw5L89nj0Ngn_5cNu2byRSTnT-MoFHJsFKRutovjs5FDhQkC3_8PKXEQ1CTK2otwUhxF4WDhE6cLCem0pirE61w1fPZrue_0CZeHfwZZT4UhD19IKlI_v2j0jzxtjPWvepQninnSOm1371oj2D2nGDutIf4JeAiw25LLFlqVT8-4J3wL3zcej7rFz69wqZ7KPU8b08vwkQeHos293K-dRrbAMEMM8M0TUigeEJvf_m34cTZcwNnOT36xFAm5urnNGlKx7vPuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پروازهای داخلی و خارجی روشن شد
🔹
پس از جنگ تحمیلی سوم و بازگشایی آسمان کشور، از ۵ تا ۲۹ اردیبهشت ۱۴۰۵ در مسیرهای تهران-مشهد، استانبول و باکو بیش از ۱۱ هزار مسافر جابه‌جا شده و مسیرهای جدید شمالی و شرقی نیز درحال اضافه شدن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/437307" target="_blank">📅 00:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48df89f74c.mp4?token=LmM9avg_qYzAkqSCHYY16H6pZI7QNtJx0jpWLWel7BFuqMsO93h2eAQlAi9fy7O9D43JaJ0l1IFEUl6qaEtARVFNaf2Bi88u6QPUbOeKQzs6ihKYNM-C6mSLYnsyjjoGeaNrG8QIz2UFV2gNTT81bIstOinvTjJbQx1G7rXOflo4Ir4hrGgWqGz5HrrC2ro4mlyzGqn3wuDAmCXl8lu5OE14S9ucCDEyQiwRTR3YfeAGp3spqPy7qEIIs4oIPt9p0352cUOBXs_S14xPuNntI71HT-OF6-ITHhJTzs3Aky2u0rIt7YpSSMGt8GtY4u0vcOR9OCoNbx693FzYCtInMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48df89f74c.mp4?token=LmM9avg_qYzAkqSCHYY16H6pZI7QNtJx0jpWLWel7BFuqMsO93h2eAQlAi9fy7O9D43JaJ0l1IFEUl6qaEtARVFNaf2Bi88u6QPUbOeKQzs6ihKYNM-C6mSLYnsyjjoGeaNrG8QIz2UFV2gNTT81bIstOinvTjJbQx1G7rXOflo4Ir4hrGgWqGz5HrrC2ro4mlyzGqn3wuDAmCXl8lu5OE14S9ucCDEyQiwRTR3YfeAGp3spqPy7qEIIs4oIPt9p0352cUOBXs_S14xPuNntI71HT-OF6-ITHhJTzs3Aky2u0rIt7YpSSMGt8GtY4u0vcOR9OCoNbx693FzYCtInMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسۀ حضور نطنزی‌ها به شب ۸۳ رسید
@Farsna</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/437306" target="_blank">📅 00:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad6eb8e738.mp4?token=DEYAoObrutaervUN4E1Etx32mrriOQn6tfEc7WkLs5KMPkXwiuacAXl7uKSBcZUAX24jL0WSZSaREQxivBGQ7k44CdA9UrdKB1FQigcSUcrZ4fOvLATnHvVkpJILSQpq0gHZCKthSMJs-5zpBbEZZqciTNCa4tHRUl5Bo_ySUIutYtYhnFEDgFvVKiQADKkh1-yL9PXfJX_Z_cj2cg5H9qI7CXlfc_4v8ykOchOhx23P2dfANZpOZmLo25Yu_mNrPHp7Z0VFxN1Aizu5fegIHFL7ZIX9aUoInvZo3RN0e7cM33OWcsQOEZYD0J_Z4RCZO-q3v-qFkzq8FNPAl8q0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad6eb8e738.mp4?token=DEYAoObrutaervUN4E1Etx32mrriOQn6tfEc7WkLs5KMPkXwiuacAXl7uKSBcZUAX24jL0WSZSaREQxivBGQ7k44CdA9UrdKB1FQigcSUcrZ4fOvLATnHvVkpJILSQpq0gHZCKthSMJs-5zpBbEZZqciTNCa4tHRUl5Bo_ySUIutYtYhnFEDgFvVKiQADKkh1-yL9PXfJX_Z_cj2cg5H9qI7CXlfc_4v8ykOchOhx23P2dfANZpOZmLo25Yu_mNrPHp7Z0VFxN1Aizu5fegIHFL7ZIX9aUoInvZo3RN0e7cM33OWcsQOEZYD0J_Z4RCZO-q3v-qFkzq8FNPAl8q0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: در تلاشیم پلیس‌هایی که به من رای ندادند را پیدا کنیم
🔹
من رای ۹۹ درصد نیروهای پلیس را به دست آوردم. باورتان می‌شود؟ هنوز داریم تلاش کنیم بفهمیم آن یک درصد چه کسانی هستند؟ @Farsna</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/437305" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437303">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJQG_x5PMKeYdea02z7q2u4vOuSK6w8cjMlbsgXjBCNHhl-lKUFm7nb8ZzzwXWnwlIzrhKzYKweZlNxOOFMw6gVok5cKQW_5ctQTeCbeKTtMYV4_DlDimVm8gqRLBAvesj0FqC8QrwWdSRAAqLCos4KbWgl1G4dfzP2Etcm9T8ow3xGPQEY-ShiL8xjI8Q3pRuMmyPEx1x9P1f2Y6Y7vYu12bMqfhMwDPUEWlPb2G8uftKmIlMtlg0o1QHFuC4sKXFXUWxEk9Frkdlgai_2_vor1vbSOeL7lvimVlun9GWLazd23OLAzTcu0O93CgO59K9vpvHaO22SQEVcW8wdIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسفر حج
🔹
مردی از سفر حج بازگشته بود و به دیدار امام صادق(ع) آمد. او شروع کرد به تعریف کردن از خاطرات سفر و تمجید فراوان از یکی از همسفرانش.
🔹
مرد با هیجان می‌گفت: «یابن رسول‌الله! در این سفر همسفری داشتم که نظیر نداشت. او مردی فوق‌العاده متقی، عابد و فرشته‌خو بود. هر جا که برای استراحت توقف می‌کردیم، او بلافاصله به گوشه‌ای می‌رفت، سجاده‌اش را پهن می‌کرد و مشغول نماز و عبادت خدا می‌شد.»
🔹
امام صادق(ع) با آرامش به حرف‌های او گوش دادند و سپس یک سوال ساده پرسیدند: «در این مدتی که او مشغول عبادت بود، کارهای او را چه کسی انجام می‌داد؟ مثلاً چه کسی حیوانش را تیمار می‌کرد و بارهای او را می‌بست یا غذا آماده می‌کرد؟»
🔹
مرد پاسخ داد: «افتخار این کارها با ما بود! ما با کمال میل کارهای او را انجام می‌دادیم تا او بتوا‌ند با خیال راحت و بدون دغدغه به عبادت و نمازش برسد.»
🔹
امام صادق(ع) نگاهی به او کردند و فرمودند: «بنابراین، همه شما از او عابدتر و بافضیلت‌تر بوده‌اید.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/437303" target="_blank">📅 00:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437302">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ac83651c.mp4?token=RYJZFiTlwpJv-yO92EICP-1osUg9Dd43p8UCxSWDOASjFgHXTPS9z7GlfmzV8wB4CdkWlJ7rz238HrkFO7N0-o-UG27cHhgZ2Q59aCPWKSSjSvzz0kyxy5IY2wdFbEIer2JwsXSC2n8yRteHbRlpLdsn7f8AP8LzMc1yGaDdgHkgKqwxnejsbeY4eoUrffeEVfDoT7PRv_uZw-AGSTFOZctaVP4_kpouIaGK5xlxE7Qz-c4ChQsbHniDqekq5960e4sw64BHGwXl9aU5LNGqRsVJXtd9hRFhqVSKsiqxA3gBVE1-DTOaV-bhsHLuXB48fAqyQ28HsZqLc36jRq1b64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ac83651c.mp4?token=RYJZFiTlwpJv-yO92EICP-1osUg9Dd43p8UCxSWDOASjFgHXTPS9z7GlfmzV8wB4CdkWlJ7rz238HrkFO7N0-o-UG27cHhgZ2Q59aCPWKSSjSvzz0kyxy5IY2wdFbEIer2JwsXSC2n8yRteHbRlpLdsn7f8AP8LzMc1yGaDdgHkgKqwxnejsbeY4eoUrffeEVfDoT7PRv_uZw-AGSTFOZctaVP4_kpouIaGK5xlxE7Qz-c4ChQsbHniDqekq5960e4sw64BHGwXl9aU5LNGqRsVJXtd9hRFhqVSKsiqxA3gBVE1-DTOaV-bhsHLuXB48fAqyQ28HsZqLc36jRq1b64WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم گناباد علیه مفسدین اقتصادی در تجمع امشب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/437302" target="_blank">📅 23:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437301">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c7bc1872.mp4?token=qmLMMmTDaKnOSVihINQw1SoGUpyx4LnS8RJOzzKcj02zX6_alw9a0yGFu4eLw4_Am7xhyRRsEMJ-AgNOFkxvYelhj99oX1XF4oee1jLmdmflKyeEfpV9fLCci3vDqguf6J0tpYkGv-C-WpMaVC4F4nR7O8qWeJlH9XkLFoKD66nnX1prlLq_okGGU-IewgZuLQhHu65D2GHD0RXlkJs0N2rmMo6C8go4R8Wdy4qvHvSFkS3q_CNxzOiw0QEGkV738JiEuAMWlt9ISb2eej7P2I9cwD1LdOwUSG4hiPQJYzYv9Qk3YFN4Y0-Fb8AzYhIfQ1fsboL8lZNNJH_8cPhAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c7bc1872.mp4?token=qmLMMmTDaKnOSVihINQw1SoGUpyx4LnS8RJOzzKcj02zX6_alw9a0yGFu4eLw4_Am7xhyRRsEMJ-AgNOFkxvYelhj99oX1XF4oee1jLmdmflKyeEfpV9fLCci3vDqguf6J0tpYkGv-C-WpMaVC4F4nR7O8qWeJlH9XkLFoKD66nnX1prlLq_okGGU-IewgZuLQhHu65D2GHD0RXlkJs0N2rmMo6C8go4R8Wdy4qvHvSFkS3q_CNxzOiw0QEGkV738JiEuAMWlt9ISb2eej7P2I9cwD1LdOwUSG4hiPQJYzYv9Qk3YFN4Y0-Fb8AzYhIfQ1fsboL8lZNNJH_8cPhAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین هدیهٔ پدر آیت‌الله آل‌هاشم به فرزند شهیدش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/437301" target="_blank">📅 23:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437300">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daea970878.mp4?token=Vun1Y5Atef3EwWPStlM-B7BnLHpehxi2D6tqurJuj8UXI5wYVpx3ypKI0Efm9c0kAliYy3hV3bV6SPZZb1truz47OAwjvYRaa96xEkm9PMzbeBR9xbOW4PIs3JPQHdCfIcUWFwcjJNqbawUmsOimyjUNmA2IkQqE72R6dn7oIzrcZJwKGLtd13otqN7ea3v78uSo-_fnpdbwX57kpkVjMBf9JlqYvgz_G4W9M8jIzGV8thbJj-5Ar9BDV9GVlwbTEZTN2UhjdMJlhzMbhzky1-0Wkk4LMuzMJKPKgUFBDvprXnKUV_vlIHCsLg-5VLZ3sTrPJGWN2o72rArMcF7btw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daea970878.mp4?token=Vun1Y5Atef3EwWPStlM-B7BnLHpehxi2D6tqurJuj8UXI5wYVpx3ypKI0Efm9c0kAliYy3hV3bV6SPZZb1truz47OAwjvYRaa96xEkm9PMzbeBR9xbOW4PIs3JPQHdCfIcUWFwcjJNqbawUmsOimyjUNmA2IkQqE72R6dn7oIzrcZJwKGLtd13otqN7ea3v78uSo-_fnpdbwX57kpkVjMBf9JlqYvgz_G4W9M8jIzGV8thbJj-5Ar9BDV9GVlwbTEZTN2UhjdMJlhzMbhzky1-0Wkk4LMuzMJKPKgUFBDvprXnKUV_vlIHCsLg-5VLZ3sTrPJGWN2o72rArMcF7btw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: در تلاشیم پلیس‌هایی که به من رای ندادند را پیدا کنیم
🔹
من رای ۹۹ درصد نیروهای پلیس را به دست آوردم. باورتان می‌شود؟ هنوز داریم تلاش کنیم بفهمیم آن یک درصد چه کسانی هستند؟
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/437300" target="_blank">📅 23:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437299">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce61e2cae.mp4?token=V8HbKADPyS7QmdtQe410owpaAMjm04Pk5IVku5DZeEcYKqso5UKCCH8HJe4NqEpyUh-iMFm931fi9JEbJOqf-BpNTpH4k0f2LhOYRzRrhcjXfIuzCTKCtB8IQqt4473UDAH6o5hpsIeMYxXP79VQC756MAGxfpbJXOgWTZUJBshRlBBBseYWE58I089ueYNvDrFiJ7Pa-90ppiYhckucKIqpEgDa2_AE0kr8gTwZWIy-T0MWyHUSY734v4FR0itpZDqnmSd-8Yhd4WZ0eBu4MHmL0yJ1s3owyRw3_LiSdOqoZQNluu43vGIHah_WdIhrfRw-nQ_qNmt6qNn3atvVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce61e2cae.mp4?token=V8HbKADPyS7QmdtQe410owpaAMjm04Pk5IVku5DZeEcYKqso5UKCCH8HJe4NqEpyUh-iMFm931fi9JEbJOqf-BpNTpH4k0f2LhOYRzRrhcjXfIuzCTKCtB8IQqt4473UDAH6o5hpsIeMYxXP79VQC756MAGxfpbJXOgWTZUJBshRlBBBseYWE58I089ueYNvDrFiJ7Pa-90ppiYhckucKIqpEgDa2_AE0kr8gTwZWIy-T0MWyHUSY734v4FR0itpZDqnmSd-8Yhd4WZ0eBu4MHmL0yJ1s3owyRw3_LiSdOqoZQNluu43vGIHah_WdIhrfRw-nQ_qNmt6qNn3atvVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌هایی از ایستادگی مردم آباده در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/437299" target="_blank">📅 23:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaZVPY9KIKS25fODp9sfhE5xGiNymBPzd0K0tCkFy7jRu9cRwqWiEatkVKi1dC28svfDx4tVVmgvWOgqlrUU16ZEVjAr-MwW0H90iTjYbBIDvZ-kxzFmajQPNYHo5wchgbyuzNOQ2dwswvC2Ou3qmD72ZJmRMzu_Ofi8IgU3WP0KOaY3WZS-peWop6Akzwyu3ZBxjam2_14zltJrmv1EDTHy-K8JktncI1yj9yvcOUU4cPNYBlFQNBuKEP24nrRxT3C1KacCY0j3-TeWP_fPmeYOHwUBW4YXDQQa6xOyySVOH5296Eo7ex8GvS-aL1hufzOD2rTyh0-7QQEhc_f2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCImNxKz9VPEPjOgctnS5M2VpUX2a5EfOTdiJbyHBmM_kEeOVkfs_Raw5VMzqvGgKavX4E09IXOIKwv-V0DlSzIFNAFbN17XgI7WYibbzsFzQe75V1oRASMI9HkEUhTv0p64qJ7hi8bRk0wFVxEEZ3Vw3IRbKfACrvljbkO5qCgHY8D_R9Gb9wrjY2SaVps_MWSwZ7POffMhbLTyMf0JvNmBXDywKcump1BiahEGwajPWnLGAaYvvJ9Sjtkbjc8g7D0IYSkEuJrQahmzAn4gYtasfRFKciiJyxL8r4XDhHckFfQgSOT1sgr8gmggohppVlWtw-D7A9xsE3HBcIKEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/undh2KAFr0FmUipCsd21GVFfmr_d5Tk9pxxnWyYmU6pJJisAOPqWW50h3lZN0QvVtn_-DIcsDx06GGtJoFGf3NGOK0Su4Buk6H1wrFfOKqCVQwANF6XlIPJYqBWohjedLyv86Xotu6wkQkeHNZeFH5QAcJ24bikx6zatwktbCEsqOHLEp7btEt1ZZgjn5spYtVHeDGHG5VLwlTi7PfML1KkKHJXUdYav0L_PhKT3NoPMbE7b1zsR_cczfemswbASpyfwCIB5cm0PMB-sjz27p7YATBIhqjk02OYpxQbuhCco8w_YffmGEYZgHScfHW5NehzGZUiaN91NVnvQVhpNwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کشف لاشه پهپاد متجاوز به حریم کشور در هرمزگان
🔹
لاشه پهپاد اوربیتر دشمن که رزمندگان پدافند هوایی جنوب شرق کشور آن را در شب‌های گذشته مورد اصابت قرار داده بودند کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/437296" target="_blank">📅 23:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9DwlLHyUQj9PaGmHCZKR9SlKfFsbUwIZ8HTSZ3BTxbfZikAexIAYosGwhvOyXARQxywfP0RUnbK7TGKTEGNoUzAIzw4SyqQC7XZfhuBLxL9LFtKD1y_OrKnt4-QVG5hHW6y_8nOb0ofauqbBv-xYbLmjPhO_KAIMTKQRL7CEu-KuEfCDAY4YpPnG7df6GftDHWWxb6LAdbE4xARyCVvlDp7KtrpMqijGruQpkds63vQdoRXMc8qNYIZkedsylweBm3uU_FDXHYdEKfSKfsFoU8HyV9_7NZZJ67I3pk9uaos2HmWGzYpHfwoJWTpxljm3-sUTjlS-VTGdttuo3AMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزیتا ترکاشوند: هنرمندان می‌توانند شاهنامه‌ای دیگر برای ایران بسازند
🔹
آزیتا ترکاشوند، بازیگر سینما و تلویزیون در گفت‌وگو با فارس: فردوسی درحقیقت یک شاعر حماسی بوده است و هر زمان که اشعار او را به یاد می‌آوریم، در کنار آن مفاهیمی چون حماسه، شکوه و غرور جریان دارد. در واقع یک روایت را در قالب شعر و به شکل حماسی خلق کرده است.
🔹
به نظرم هنرمندان در امتداد این موضوع می‌توانند روایتگر تاریخ روز باشند. حماسه‌هایی که مردم  در دو جنگ تحمیلی آفریدند، نشان دهنده آن است که پای آب و خاکمان با غرور ایستاده‌ایم. می‌توانیم از حماسه‌های این روزها، شاهنامه امروزمان را رقم بزنیم.
🔹
قالب‌هایی چون نمایش بسیار می‌تواند به این موضوع کمک کند. به نظرم این روزها می‌توانیم شاهنامه دیگری برای ایران رقم بزنیم.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/437295" target="_blank">📅 23:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
شوروحال بروجردی‌‌ها در هشتادوسومین شب خروش مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/437294" target="_blank">📅 23:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارهای کنترل‌شده، صبح فردا در کهریزک
🔹
سپاه حضرت سیدالشهدا(ع) طی اطلاعیه‌ای از احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در ساعت ۸ تا ۱۰  فردا در کهریزک خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/437293" target="_blank">📅 23:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0bc381f8.mp4?token=pBdpJSNfN_4u6wmgV0PIwPDJQaQKeYmYDQfCMGalkylMi7Eke-SeU_aGSdgDOddyjeM6fzNS2HOw0Zy1NfYlKmZ48DE4VmbyaZoppDLzyly_jvsUZkfcorGyVOPMfYQmR0WREEJBrYE1dZqN1_UYgO2uV10xtFZraMRIbttOhHkMD_16-exvkhnHCbEoP0MNCa8QkLHpS4FPbi8fY6yu9U_yW-ylVLAouitG7i_pYPSdRYf4f29cPR0Z5pulTyH9UknRKr49YByOYqXf5knln0LvDKQeWtkcm5qi_nou4trPWN0qtcLwXIfliSIDk6R8ryyPT49rkgXRISPiWXHbZbXtlpTQmOVLOzyUoZxhKqLhWXhpX8cruCu6WtPCOMOrym2LRDI9l0TSRwCf38kJ0TXh7bCmDFOx9K6ClwhIgvqG8ZGLHcpP2gbljf4LyWo3B2AYwbuGh3vXxHfoki-JP2ZKagn1pnHC2AMcCYW9D-7wngsBuuv_MhxGj7s8t6oHH9nTyO4r3p_c6CiQZzC8OF-v3IQl1qDLbEL_xKWu6drS-cMM-YCvV-noGgG0i1bE9FB9AI-r3XseWQxAx4JAGUjelvQEFJEO3UDrdlEfmrGuF-AoN0KUVuQgAkaiG_RbSEbPnokkO4Mrt0cZv2OBHBoeveYTj_4UHVJ7USm_dis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0bc381f8.mp4?token=pBdpJSNfN_4u6wmgV0PIwPDJQaQKeYmYDQfCMGalkylMi7Eke-SeU_aGSdgDOddyjeM6fzNS2HOw0Zy1NfYlKmZ48DE4VmbyaZoppDLzyly_jvsUZkfcorGyVOPMfYQmR0WREEJBrYE1dZqN1_UYgO2uV10xtFZraMRIbttOhHkMD_16-exvkhnHCbEoP0MNCa8QkLHpS4FPbi8fY6yu9U_yW-ylVLAouitG7i_pYPSdRYf4f29cPR0Z5pulTyH9UknRKr49YByOYqXf5knln0LvDKQeWtkcm5qi_nou4trPWN0qtcLwXIfliSIDk6R8ryyPT49rkgXRISPiWXHbZbXtlpTQmOVLOzyUoZxhKqLhWXhpX8cruCu6WtPCOMOrym2LRDI9l0TSRwCf38kJ0TXh7bCmDFOx9K6ClwhIgvqG8ZGLHcpP2gbljf4LyWo3B2AYwbuGh3vXxHfoki-JP2ZKagn1pnHC2AMcCYW9D-7wngsBuuv_MhxGj7s8t6oHH9nTyO4r3p_c6CiQZzC8OF-v3IQl1qDLbEL_xKWu6drS-cMM-YCvV-noGgG0i1bE9FB9AI-r3XseWQxAx4JAGUjelvQEFJEO3UDrdlEfmrGuF-AoN0KUVuQgAkaiG_RbSEbPnokkO4Mrt0cZv2OBHBoeveYTj_4UHVJ7USm_dis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری آمریکایی: ایران می‌تواند شریان ارتباطات جهان را مختل کند
🔹
لئون سانچز: ایران در تنگه هرمز فقط بر مسیر نفت تسلط ندارد، بلکه به یکی از حساس‌ترین شریان‌های اینترنت و ارتباطات مالی جهان نیز اشراف پیدا کرده است.
🔹
دست‌کم ۲ تا از این کابل‌های اصلی شبکه ارتباطات جهانی در آب‌های سرزمین ایران قرار دارند؛ آن ۲ کابل گالف و فالکون نام دارند.
🔹
ایران با گذشت هرروز بیشتر و بیشتر به اهرم قدرت خودش پی می‌برد که هیچ کشوری نمی‌تواند این اهرم تنگه هرمز را از ایران بگیرد.
🔹
اگر ایران تصمیم بگیرد این کابل‌های اینترنتی را قطع کند یا حتی تهدید به خرابکاری در آن‌ها کند، بخش بزرگی از اتصال جهانی تحت تاثیر قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/437292" target="_blank">📅 23:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مقام ایرانی: نیروهای مسلح ما برای بدترین سناریو برنامه‌ریزی می‌کنند
🔹
الجزیره: یک مقام مسئول ایرانی امروز به ما گفته که هنوز هیچ توافق نهایی بین ایران و آمریکا وجود ندارد و تلاش‌ها برای کاهش اختلافات بین تهران و واشنگتن ادامه دارد.
🔹
این مقام به الجزیره گفت تحرکات دیپلماتیک ادامه دارد اما فضا  برای یک توافق واقعی کافی نیست.
🔹
این مقام ایرانی هشدار داد که نیروهای مسلح ایران با نیت‌ها سروکار ندارند و اقدامات خود را بر اساس بدترین سناریو برنامه‌ریزی می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/437291" target="_blank">📅 22:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99c0b51c08.mp4?token=Mk326J7Cm-mpbWm2ogw7wyH6QvcWRx-coXbXUP9CXfqFStwjLA9e3Ho9QBKuAeDZaMrfWe-SgSYbHX8StghxWsn-xhjIzHBWTFIaguUknWA30d-nsiuuQwIZjLq1-RGirQDfkY8B8UWyVMZesEW8teGIsB19IVDCRAZUUxtTNqj9HSaLrphZHoykigRZjroyr856wiwG9UiOP4yTw3GjGf8Zw5vdBFjq3vtBDn7FSSqB4npb4ILE3nL59JMHaKywZZ9Umb2vxDIOxRjWO5ITmzGvWvFnrUQBpjQ3LDb_-XZcElm-e-_nXdU4SnbWb7lyGg4RJRPXq_ItGLEPNcMGfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99c0b51c08.mp4?token=Mk326J7Cm-mpbWm2ogw7wyH6QvcWRx-coXbXUP9CXfqFStwjLA9e3Ho9QBKuAeDZaMrfWe-SgSYbHX8StghxWsn-xhjIzHBWTFIaguUknWA30d-nsiuuQwIZjLq1-RGirQDfkY8B8UWyVMZesEW8teGIsB19IVDCRAZUUxtTNqj9HSaLrphZHoykigRZjroyr856wiwG9UiOP4yTw3GjGf8Zw5vdBFjq3vtBDn7FSSqB4npb4ILE3nL59JMHaKywZZ9Umb2vxDIOxRjWO5ITmzGvWvFnrUQBpjQ3LDb_-XZcElm-e-_nXdU4SnbWb7lyGg4RJRPXq_ItGLEPNcMGfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال کم‌نظیر مردم عراق از «محفل القائد المعظم»، یادبود رهبر شهید انقلاب در میدان التحریر بغداد  @Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/437290" target="_blank">📅 22:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437289">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11689cc9c.mp4?token=V9ct6G8W9OgFOAHvz7HXrjO2YnTLQ9BgbZh7x3mcgtfDvlrv0Ebk2FZ2QHcplaCO2BLp5qlnbwNDvMMaTSNefpHPpBigGrnxQnXx80J41jBQEDriBzIy57cgI7ESVcRdElhqcZ0Fc9KHgHhUFu5CTF--nOeuYKDQh-dkUK3RMqfqHW2vIIb7cOje4Orf5sUQ8IfSl4IRgDvpyUkx1Xeys_arswoaGYQz46b_QAi88G_PbO3qpvosh4Qaj07R9EzhyT4_jeUMyl5aiZ_zuZ8kThS3Yc2E5dTQmzqzm9HXNloqU3EZSW3EXGylsDYRT158Jor2V_dqEhMVaIJL6iw7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11689cc9c.mp4?token=V9ct6G8W9OgFOAHvz7HXrjO2YnTLQ9BgbZh7x3mcgtfDvlrv0Ebk2FZ2QHcplaCO2BLp5qlnbwNDvMMaTSNefpHPpBigGrnxQnXx80J41jBQEDriBzIy57cgI7ESVcRdElhqcZ0Fc9KHgHhUFu5CTF--nOeuYKDQh-dkUK3RMqfqHW2vIIb7cOje4Orf5sUQ8IfSl4IRgDvpyUkx1Xeys_arswoaGYQz46b_QAi88G_PbO3qpvosh4Qaj07R9EzhyT4_jeUMyl5aiZ_zuZ8kThS3Yc2E5dTQmzqzm9HXNloqU3EZSW3EXGylsDYRT158Jor2V_dqEhMVaIJL6iw7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: سفر ایران با هواپیمای اختصاصی ایران‌ایر به جام جهانی تقریباً قطعی شده است.
@Sportfars</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/437289" target="_blank">📅 22:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437288">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad727676c5.mp4?token=vtaq-eEPluewCVpyClx-K3IeRz6qBbsToUdArnlJZFgVewnURyxbc1h_FAUtxWrP_Idajq6Coj5woK8_zNoqn0-w__riXc0DzRVSaUeIRngqILuWcdhkrXvznBVTvXE3QLa-_UUlFPmxL534i9sR4ahUu-qZ9crslYHoJG7hUTB5ok345VRXGiNGZYbp7xZhpduBRDYnGaVVyMqfBamH4GvdZ5VFWbbES4KKvUrl8W6nmAHECTgE8bLkSUX2SHQU38geb4VhYz4e-Dbw2sp2Y_ore1mkFTLawgSmEhbUOAs3-ffulp8snJDGNAMBlAEQ0zw2BqOBeoF9QWiGcmYwbT-devD5tszLcosLIWlENb8pQ6QiPbJ7kb8nbBvegYWXcax2cqQopbHEEH124h3YKI7NoI7opKfbxU2F4vyhnLRHPZvyM2I41mNoDRzIsdDo7age4hn0b1FosbRmwwxdHjYrKkQejnBRx70IRSEGzurubsSK0F4PTFiH6m1vMMbnK5e7Lv2BBpuZ5WiescKycIwlxeFWX9tPHFC3KhlHbO-rr00uqfOx2D22nHL_NuEvaKAHfYrKSGSut24gIQ6Tz6BTAhHWADqEcVvDhBA7ZCDlfrysFb6ZEVDfdRJMszy-8duv38DPvYP2TzMQEKxupk4bKfYMK25oP_85W9KnbKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad727676c5.mp4?token=vtaq-eEPluewCVpyClx-K3IeRz6qBbsToUdArnlJZFgVewnURyxbc1h_FAUtxWrP_Idajq6Coj5woK8_zNoqn0-w__riXc0DzRVSaUeIRngqILuWcdhkrXvznBVTvXE3QLa-_UUlFPmxL534i9sR4ahUu-qZ9crslYHoJG7hUTB5ok345VRXGiNGZYbp7xZhpduBRDYnGaVVyMqfBamH4GvdZ5VFWbbES4KKvUrl8W6nmAHECTgE8bLkSUX2SHQU38geb4VhYz4e-Dbw2sp2Y_ore1mkFTLawgSmEhbUOAs3-ffulp8snJDGNAMBlAEQ0zw2BqOBeoF9QWiGcmYwbT-devD5tszLcosLIWlENb8pQ6QiPbJ7kb8nbBvegYWXcax2cqQopbHEEH124h3YKI7NoI7opKfbxU2F4vyhnLRHPZvyM2I41mNoDRzIsdDo7age4hn0b1FosbRmwwxdHjYrKkQejnBRx70IRSEGzurubsSK0F4PTFiH6m1vMMbnK5e7Lv2BBpuZ5WiescKycIwlxeFWX9tPHFC3KhlHbO-rr00uqfOx2D22nHL_NuEvaKAHfYrKSGSut24gIQ6Tz6BTAhHWADqEcVvDhBA7ZCDlfrysFb6ZEVDfdRJMszy-8duv38DPvYP2TzMQEKxupk4bKfYMK25oP_85W9KnbKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجرای متفاوت در تجمعات شبانه مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/437288" target="_blank">📅 22:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437287">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ab312ad2.mp4?token=g61ss13hi8KW0d9kFPoqYJGBoCECPYSsZO4NfSIqYwdagdPme0itvUYKjzZ6Ffn3ANFRBQUaClrx0V4rKs3shik6ccgVKQ5mqnZGi84bcyZ5YcpWd1LP7xox58_ejN9zgtRdc9rXiSwKGUYRmWQPxsGrCWzVRWHOHEfxQEFmV23IZYKaqentGW3yRf2bxrwtAtn7XUowgbnT_M5DCvFkbX050sePnN8E0DQqd5WzUdlTIyF4lJkkhELO6YEkfZX3oFgAI6GKB2UilzIYZpozpKWIn_gRxoJgx7hX549a3bkr473gsTpAgQMaHKiXePpok45uSNCskbAIR4p4GXe3JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ab312ad2.mp4?token=g61ss13hi8KW0d9kFPoqYJGBoCECPYSsZO4NfSIqYwdagdPme0itvUYKjzZ6Ffn3ANFRBQUaClrx0V4rKs3shik6ccgVKQ5mqnZGi84bcyZ5YcpWd1LP7xox58_ejN9zgtRdc9rXiSwKGUYRmWQPxsGrCWzVRWHOHEfxQEFmV23IZYKaqentGW3yRf2bxrwtAtn7XUowgbnT_M5DCvFkbX050sePnN8E0DQqd5WzUdlTIyF4lJkkhELO6YEkfZX3oFgAI6GKB2UilzIYZpozpKWIn_gRxoJgx7hX549a3bkr473gsTpAgQMaHKiXePpok45uSNCskbAIR4p4GXe3JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال کم‌نظیر مردم عراق از «محفل القائد المعظم»، یادبود رهبر شهید انقلاب در میدان التحریر بغداد
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/437287" target="_blank">📅 22:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437286">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791d9999f.mp4?token=JRamccXlN2ssVJn6SQAmMEuUVTsth5w7XeXP2pnYFlNPZeMA8V6SRQ45-mZB6irjjIVRPo-Nibj8NFxpvj_cvrwgYffObpcDk8FiY7HhupbzJS_BXBQ1TYTT-cQSGsffccmMkKzqu-C4WlaUGQWW3ui0s0psWb8xr5u2kvXM0V--NfPCzx1IMWNlJ6iASwbGAFLMT65KIp83vc2i_nUzfzekt-ygv0ZtXaHmVFhfyO6M3zmSgalXtIIezFus4z8ug7hUyhlEhAbQxhridML5AdgSnJ8dc8WBqCwjH6E_xU3rgXlwbjYWhUM2mvoMqSf4vkFqFLvfdjJinJIV233a4B6HO7I0wnTVNF5MehOObPAEiLdq_CXhxjZomQPSXp3YijiIxgRpirzkjUf1WtsG4-4J5JFJhPD9j08l793q18XURVG9u2WonlkJo0249FjZY0Jsm8xNN-1fW98BqETP2gFXlJ4qSkuZ6eM2E0LMuOSbvEyGjYKYAeGGGfHP9hUAO_fLhRul7FvvEjq2UB9-X-sZgVci0VArsqKqfsHh60GCihTEeR4yjj3SPVUk6uTeCqesCyB7Ne3MQfoTO9XqOeAlvWo6EcYnbHbgucCF_Bw--syCzj0kbecQAM2i1_5HiFDZmUi8hWQa5uU9FgXR6hzwwqb0CF7VFMUguXNrkBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791d9999f.mp4?token=JRamccXlN2ssVJn6SQAmMEuUVTsth5w7XeXP2pnYFlNPZeMA8V6SRQ45-mZB6irjjIVRPo-Nibj8NFxpvj_cvrwgYffObpcDk8FiY7HhupbzJS_BXBQ1TYTT-cQSGsffccmMkKzqu-C4WlaUGQWW3ui0s0psWb8xr5u2kvXM0V--NfPCzx1IMWNlJ6iASwbGAFLMT65KIp83vc2i_nUzfzekt-ygv0ZtXaHmVFhfyO6M3zmSgalXtIIezFus4z8ug7hUyhlEhAbQxhridML5AdgSnJ8dc8WBqCwjH6E_xU3rgXlwbjYWhUM2mvoMqSf4vkFqFLvfdjJinJIV233a4B6HO7I0wnTVNF5MehOObPAEiLdq_CXhxjZomQPSXp3YijiIxgRpirzkjUf1WtsG4-4J5JFJhPD9j08l793q18XURVG9u2WonlkJo0249FjZY0Jsm8xNN-1fW98BqETP2gFXlJ4qSkuZ6eM2E0LMuOSbvEyGjYKYAeGGGfHP9hUAO_fLhRul7FvvEjq2UB9-X-sZgVci0VArsqKqfsHh60GCihTEeR4yjj3SPVUk6uTeCqesCyB7Ne3MQfoTO9XqOeAlvWo6EcYnbHbgucCF_Bw--syCzj0kbecQAM2i1_5HiFDZmUi8hWQa5uU9FgXR6hzwwqb0CF7VFMUguXNrkBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در ۸۰ روز اخیر پلیس بیش از ۴۰ هزار تخلف مربوط به مخدوش‌کردن پلاک خودرو را ثبت کرده است
@Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/437286" target="_blank">📅 22:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437285">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c32ab1459.mp4?token=IyAo10KVrzUioqnJvLb2fFT98LHb225iYgW7GwfrRxD2PL8DMp4jxT8-EWd_Qax433tqm8NSCknyz3g9VANaGs999M4klIMfaIVvzlaiAxbV02hlyqRqflmpVRLULfdONtNCywXxlVhpbtb2Km2GUt6R9vydtsXV8WWLU0nVpvnuShMnwjTF8PFj1h6RXWv2JMgtpHzR5Me6mj38qVkdZLRcij4s5mFi9S8VpY0MfgGdCd_8v-2i4FvWoyEzkEjNRz88pEmiXA7M44GX8QKjnFaCKWdHh4SlhwdpJTnH4y69wHHHVp3sCq3yGrllrixEge4VsC0_QxQpuiEcmY_v0b2B1ciK_iBxrpIj1BXjq61v4nnquyvtiPnJbmmPCSUUc46qhfkGfMEYQrtV7NKFIX2zYb1seYG8rdUOqMl2LeGp1JujHKUnPWrPqKjSQ3oPMq6ArIkHpCMdwWe7pjMT8BX_Zz9m-9daPtRW5OdHGDTrazI-H66VPzLnBdDSmhLPpB5R4izquTrmeFPwS1fMATyPfBq2DZu0bSq4sZS80Ugsu1SL2k59HCueLv0X-csMQMnxqyLwB67vm8dtJBo--_C4Fvjc0KaushvnkJtYbiqKsyGed2Ejzcroyjw7HpYuTMqS9C99TPwtlQjPEgLERpkZ-c8IPzDJP3UW7Z1wlZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c32ab1459.mp4?token=IyAo10KVrzUioqnJvLb2fFT98LHb225iYgW7GwfrRxD2PL8DMp4jxT8-EWd_Qax433tqm8NSCknyz3g9VANaGs999M4klIMfaIVvzlaiAxbV02hlyqRqflmpVRLULfdONtNCywXxlVhpbtb2Km2GUt6R9vydtsXV8WWLU0nVpvnuShMnwjTF8PFj1h6RXWv2JMgtpHzR5Me6mj38qVkdZLRcij4s5mFi9S8VpY0MfgGdCd_8v-2i4FvWoyEzkEjNRz88pEmiXA7M44GX8QKjnFaCKWdHh4SlhwdpJTnH4y69wHHHVp3sCq3yGrllrixEge4VsC0_QxQpuiEcmY_v0b2B1ciK_iBxrpIj1BXjq61v4nnquyvtiPnJbmmPCSUUc46qhfkGfMEYQrtV7NKFIX2zYb1seYG8rdUOqMl2LeGp1JujHKUnPWrPqKjSQ3oPMq6ArIkHpCMdwWe7pjMT8BX_Zz9m-9daPtRW5OdHGDTrazI-H66VPzLnBdDSmhLPpB5R4izquTrmeFPwS1fMATyPfBq2DZu0bSq4sZS80Ugsu1SL2k59HCueLv0X-csMQMnxqyLwB67vm8dtJBo--_C4Fvjc0KaushvnkJtYbiqKsyGed2Ejzcroyjw7HpYuTMqS9C99TPwtlQjPEgLERpkZ-c8IPzDJP3UW7Z1wlZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاوید ایران
🔹
شعار هماهنگ نیشابوری‌ها در شب ۸۳ تجمعات مردمی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/437285" target="_blank">📅 22:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437284">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d3480c7a.mp4?token=FfsHPRL-K6TDHGxWW-_iRUNe1Yk2VAoFULW1cbCVfJjVPr5ZahZqy3qYbQVqF0wGwQeev--P5DFRRdu2kfwooiedMUbe-trkdyRw2lg6Xrb1My6JySSg_jFbsi9eDWBoGHmx5PR2Q2j9Wb96RXm8sSDFqPeRk-eJQZl4V_5M3zNUKLUUHQOWkjW7VQO6czj8o47BYPSjfoSJoPBXHy5iDJmoQif2kB42iJC63xx6f-90pa6IbRDI2H80nVy6DzNXGZV8npNiZB7iIGax_PnP4wOofiPipBBhmt8jVloF5HWV_OGD0g5eb8glhKDHosTDukGhTFlJUtssO8CQvvM6H7cwmy7Q6v_kLYf_00Ys-TTvLz1NdmCFU3zGyqT9nI4o9p5YUHpYKcMesrWnQGUGLdrhe69r1ZptEXn8uKZ8CsHaezoHPF4PBNaLk3ztKakdGFgFPwRjnCcL_iqIQscu71Wul6mh88zJmADUU49jGQNnq7q5I_mVZ4vLISyENVQWoBMJaDcAIDIqr2zoPpBCPPJAb9r_KetYIN6c5Mr2rUmqLor5iBVO4r19uOgmE2u_J5Dl5E7w8KKoPK49cmRysDR7g4vTlpNBPJ-KuJK5gRMLL51nIDAwcANh44pNuyWqfUmy30jEGMqxMFGeGyKA_PK9_fajstQNOpKj04PazWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d3480c7a.mp4?token=FfsHPRL-K6TDHGxWW-_iRUNe1Yk2VAoFULW1cbCVfJjVPr5ZahZqy3qYbQVqF0wGwQeev--P5DFRRdu2kfwooiedMUbe-trkdyRw2lg6Xrb1My6JySSg_jFbsi9eDWBoGHmx5PR2Q2j9Wb96RXm8sSDFqPeRk-eJQZl4V_5M3zNUKLUUHQOWkjW7VQO6czj8o47BYPSjfoSJoPBXHy5iDJmoQif2kB42iJC63xx6f-90pa6IbRDI2H80nVy6DzNXGZV8npNiZB7iIGax_PnP4wOofiPipBBhmt8jVloF5HWV_OGD0g5eb8glhKDHosTDukGhTFlJUtssO8CQvvM6H7cwmy7Q6v_kLYf_00Ys-TTvLz1NdmCFU3zGyqT9nI4o9p5YUHpYKcMesrWnQGUGLdrhe69r1ZptEXn8uKZ8CsHaezoHPF4PBNaLk3ztKakdGFgFPwRjnCcL_iqIQscu71Wul6mh88zJmADUU49jGQNnq7q5I_mVZ4vLISyENVQWoBMJaDcAIDIqr2zoPpBCPPJAb9r_KetYIN6c5Mr2rUmqLor5iBVO4r19uOgmE2u_J5Dl5E7w8KKoPK49cmRysDR7g4vTlpNBPJ-KuJK5gRMLL51nIDAwcANh44pNuyWqfUmy30jEGMqxMFGeGyKA_PK9_fajstQNOpKj04PazWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: با تکرار تجاوز دشمن، جنگ را فرامنطقه‌ای می‌کنیم
🔹
بیانیه سپاه پاسداران: دشمن آمریکایی‌صهیونی که از شکست‌های بزرگ و راهبردی مکرر از انقلاب اسلامی درس نگرفته و بار دیگر زبان به تهدید گشوده بداند، اگرچه آنها با تمام توانایی‌های دو ارتش که پرهزینه‌ترین…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/437284" target="_blank">📅 22:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437283">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDBPRtaxVueS-QrGWW8WT8h9_CoAAuwIGO_hZnQs7ZK8AeeIbTzdrCGUG6547ESgTmnyXtT7jgf-fpqZlJrGnD8kZXTc0k_8RVLG6Z36FyyLbLFDqsFxd_hH1jKKixKLFONHL5D0_Tqs41mNrwKP8ZgWfOlAHqtluolyoHcK7dieFbWmTtulGKOMHEuz6Hogoz7KbbZlVWckYziNnY_72YHwbpi8PmSKDZSqqzPKdjUrDTIQIrPyh_ds12GcipS4mh-ESCoUpMiyF6C233ROrAUP-CZ-8mKqGUZObiihSaV3oeaJXDtW08Ays8lPknXMVun0is5udC7-TY36CZh1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصره دریایی هم قفل ۲۰ ساله بنادر شمالی را باز نکرد
🔹
درحالی‌که ترانزیت از سواحل جنوبی زیر ذره‌بین محاصره دریایی ترامپ است، بنادر شمالی ایران ظرفیت واردات ۳۰ میلیون تن کالای اساسی را دارند.
🔹
بااین‌وجود اما پروژه اسکله رو-رو امیرآباد برای کاهش ۵۰ درصدی زمان ترانزیت، پس از ۲۰ سال همچنان در وعده‌ها گرفتار مانده است.
🔹
اسکله‌ای که اگر ساخته می‌شد، امروز کامیون‌ها و قطارهای حامل کالاهای اساسی می‌توانستند بدون تخلیه بار، مستقیم از روسیه یا قزاقستان وارد خاک ایران شوند.
🔹
کارشناسان تأکید دارند که اگر وعده ۲۰ ساله اسکله رو-رو باز هم در پیچ ادارات گم شود، نه تنها فرصت طلایی کریدور شمال-جنوب از دست می‌رود، بلکه ایران بار دیگر به مسیرهای محدود و وابسته به همسایگان شرقی و غربی خزر محکوم خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/437283" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437282">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw-HOgSwS4UTAAnTIiH3211GeM626cstTOYmyOVr7rIfwCgIGhGxkncI1GMXtOhp9g-txYpbkC4D_9XoUiD0Jz9L1vWg-Oa1RglqupFcblM49HD3NNL1ZLJKK2Rvj_AMpNiLAv9XrFKfH3qA717VW32Ilq9ByQx70kn4bjVIURqDIDYoM6xVePQMfkoWUPC6uKYWiNoEysLgaELaWpbVS2GGIKh3vvWkt17w1mrXUj5_Kxhw2BDCj9EfJIPz8P4kqOqLhCfs9c4Yj4RnBwojVvh9W2IkeBc4dgjNzDYrQno5dvWSnsE2J2Nx-isGnujjbYwYeMwNMg-RfURCvrbMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر اطلاعات ملی آمریکا استعفا داد
🔹
فاکس‌نیوز: تولسی گابارد، مدیر  اطلاعات ملی آمریکا از سمت خود استعفا کرد. @Farsna</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/437282" target="_blank">📅 21:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437281">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: یک هیئت قطری امروز به ایران آمد و مذاکراتی با وزیر خارجه داشت
🔹
کشورهای مختلف برای جلوگیری از تشدید تنش‌ها تلاش می‌کنند اما میانجی رسمی مذاکرات، همچنان پاکستان است. @Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/437281" target="_blank">📅 21:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437280">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در مورد مباحث هسته‌ای تکلیف خیلی روشن است؛ ما عضو NPT هستیم و حق داریم از انرژی هسته‌ای برای مقاصد صلح‌آمیز استفاده کنیم. @Farsna</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/437280" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437279">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: فعلا فقط تمرکز ما روی خاتمهٔ جنگ است
🔹
در شرایط کنونی ما باید ابتدا با مختصاتی نگرانی‌ها و منافع‌ ما را تامین می‌کند به خاتمهٔ جنگ برسیم؛ اینکه در مرحلهٔ بعد در مورد سایر موضوعات صحبت نکنیم یا نکنیم بحث دیگری است. @Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/437279" target="_blank">📅 21:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437278">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: موضوعاتی مثل «خاتمهٔ جنگ در تمام جبهه‌ها، وضعیت تنگهٔ هرمز و خاتمهٔ راهزنی دریایی آمریکا» همچنان محل بحث است. @Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/437278" target="_blank">📅 21:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437277">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6HmGqlauDFXmEv5jxc2fa6B_t1znCz9CIHtqEJTvHTPTdg_6WITK2Ij0eQoqFVFyTKca35QBKKUhwyq_EdGIRDp0JPPsNCxP_yrCMPS_y9GQmfG4gTYTZVuNHELZmPPi3gf_VmAjp2gb7tXdPFaE9eH8vf_gk0PmJrGKIGe4L5sEZtBVzgazzXASmJZfgbglRSBfTAdoZbrYPNB_qv-zid6gk33NgxkDudhjNumgHxoeW2EO4uWWl_ZfdqaLlo72oEbYfDv_7Xb5vPiPonkaApC4JqQy3nTkLRAe4zLLhjbzr83jEornGNrfmOosBB7fcip3HVPKD3fZzr-aD3z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر اطلاعات ملی آمریکا استعفا داد
🔹
فاکس‌نیوز: تولسی گابارد، مدیر  اطلاعات ملی آمریکا از سمت خود استعفا کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/437277" target="_blank">📅 21:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437276">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تمرکز این مذاکرات بر خاتمهٔ جنگ است و در این مرحله قرار نیست راجع‌‌ به مباحث مرتبط با موضوعات هسته‌ای بحث شود. @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/437276" target="_blank">📅 20:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437275">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم. @Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/437275" target="_blank">📅 20:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437274">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: نمی‌توانیم بگوییم که به‌جایی رسیده‌ایم که توافق نزدیک است؛ خیر این‌گونه نیست. @Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/437274" target="_blank">📅 20:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437273">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر فرمانده ارتش پاکستان ادامهٔ روند دیپلماتیک است و نمی‌شود گفت که ضرورتا به این معناست که ما به یک نقطهٔ عطف یا وضعیت تعیین‌کننده رسیده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/437273" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437272">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/437272" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437265">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci7usPDAwLjd7gEzpjzTcZOFu8uzTZEbPcTqudsjaD2b7TKvErQwUMq56mm5e7jcCp1eI_qXcqCBBFZGV-FtF2qvqbvTBrpMGEMksI4XSXVKZGKI_UsoiSTZ0C1l6Bgrozhm7xsYg614hbQvqBF18RrdHdp3OAfEBbttEcbZCmQ6EOP7JmxehJRY9HFEhTGeHenQRe2VntNjZH_RDHuFkOOFdkDCHyaEdPoUTBY6zm4ESDvWSRbtGDA1uFO72c8qiqWhUy7ad_D1fRkTbXu8VIMapLZcWCtY_MC6hkb-zdR-uYw1wQ21Ix_nH6kFUdlKtBZEM-KbPUcsMGiStW5eXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eeBetZzuyEuVZb4UBScjUyJh33uy5hN8djBIVa3wVAtXMhSpXyk2h0MuasRR3TdvDAZ95FY8kwuqJInuIwpWzisU7UlKcyZl0jYhc81VeY6ZgfTfFz_nGDZ1wh4w1E_KOpUC7hYpvTtSipxhIWt-edMoU-g2ekmmN6tsp8uM5E9DEs5d-YLV9buAUqdgbQp_mz3M2O7alvHpR5BjXgjkJTiufhyZrZhEa7oDxR-wEivRd6llGenjUTJZBVDuvYw-y2BK8_Ovp_397zo94CND-WCcl8Z1lANKJlsKKDbRLe2v4fZkFiPoTYJK4h9lJP6yfEA2E3zlQOMDiTQ58c8iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZrgneKfDy2WdpOGG8ToOyR1UEjbr0LZNfFDi4BGYwqSCGV2AXcOlzi0X0zfxsFaCRTU4P5F9nWfjSnhtOx6XTMvTzGR_pzaPlL81TejVwtugLECm4GYYQLoh9gNHxmKZIdRbePh76cdz4rVFxmNcs5DH3iyaxGpvBDI2cpWNbGM91LWk3yrvKaNV2u83n89_ECMmYPewDRA1PHr9U3aSh82gwMYAjsSdqMKTr62zivdl3nA-M1nb9AmydXILTSO8Y10NA5Nf2OgTw1JVpTj0DXKpTXnBCgg2PS_l_wfd2VkWhmvL24x14P2522_LnnXUZ-OGpuirIjFe5J_dHGbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTjUTeLsXVUajY_z_feHE4LsYR2WEEN3aQyGgY8SsGpt2YD1PABrsljqZ84pAUd3qWQJO2KwPJ4J0mLbkOZfmUo__RzKGdFaJoxtfvbUJAvteULX5m9OvK3gkoaXw0TwW4GYfbsz98BNKuL0YLeGe4wO6-aGcBocksNFKsXYcr9cGQPd8H601aJ7cnCiCx_ZCBTx8XFbYdZhQ_CS_zfEu3Y_PkjSNs7V7t8zbnHEjKNTFLgyvWdKVvcAnClASwiYsSf--MOaAG3hFqram4IN5m0_VDtaWQyRKJ9X83zJyXkEtlriFj9sy0mft1Ky12Zg1R1-mqH193NQC6F2QjugDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SotXNwXsvJyFJGUcnZz5OMZWzC36svceF5kol8IqN0_1wL_9YvobRcK_K3ghtnuXgnWUmbSarg9L67LYuqUJBfL2-uYw8mjzD4CRhFPcmnG7H5z4Nt44F1NgGBgsPmYp7njNbPkQjkYGT4BA3mKPKx4pOo7dgvJUd3K3iH4U0LpxbqPDQGY2AQkYjuWqOkTHTblEjVwg9z5sDhzBqpB4J5Ek2ipg7Rrg0oFmdTmcXngf1CF0JisaXEnuVCQWJ9ByQ4Wph23A25cWQ351J3hg352m9EGb8C7aSGjqgUkKTWczosZrIU_Zo0he1FQVge6BnFjleVJBWDF2-F6NY-ljCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLG3ZR8s0QqM3oB4TejHJk4aqc_6nrb_JgVhudjpiZm0LTZrGMfXo1AIpIYNgsx9actT6uCKvEUhuOAZiN2SZ9XkgGz-YGzMmqKdvEiwB9vhp9qpNTzy-B03HVPjsTGA9J6Pr9X7zbs0MMdcF_2JLp-LJ78dj6QUufAtwyiJGxZ0COV5oNbFbioUjsczm5F9v6BfFbbk3CXPTNkvMhZcVucANSJvG1mqwcSJxpRm2ka791s_Ka2lJdfRhLEIHLjqG5CsZ3Adbb33ZR6u-mpeoMg8LfYdjINv0RrThUrv9d2xT53L9vrPKLT_5QgBQOSwXT9aHvOPjsKKEhv6hA_R2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xnh6b1zQ3Wd78ElwBNwEp5vANgYBOk0Q2_cIlauLn1X0v-I31T52uaYImzX_0XhggHIagEtiJgBwCfRUhjiEE0HHooZIH3JfvHyog0Bqejhgn-TWymLLbYYW7sdVItewmwH1yItMaHifN7o8ROt_P7KL5EzqS9_otxVDiwOZsda7QhWYACD5TDf6pe8ip2U29-WmVaLjK1s6F7SGlp-nnyjBWbnnCh0onOmFZNeZ9AdOK6xnzCf5kIxCd562hl6W0u3m5tx6IkUI4NGW130JOvLMudhWgwcgl-KIzqXJ1N02J8h7UsL-tjT_2jJRcYVS3vzr9I1H0A1i1r50WMHc0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سردار عباسعلی فرزندی به یاران شهیدش پیوست
🔹
سردار عباسعلی فرزندی، رئیس پیشین دانشگاه عالی دفاع ملی امروز به‌علت بیماری و جراحات ناشی از ۸ سال دفاع مقدس دعوت حق را لبیک گفت. @Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/437265" target="_blank">📅 20:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437264">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993985f526.mp4?token=NlRUJaD5GDd96o1PriZMzper5-d_TAvqPdLf2Z80ZR5_V5666CZY49YyfDBXH-kThFfX5LLO1NZGdYLd3QhwvgA5uGGLwAHIaikFDmMKEKRMdvebJFs3DSMw6tBJWHICyJBzpwmZjt8MbY9pzaiWELKOap0VreU2vWybYhGVpz2xcQwAezaTQ09G1CKD6aXWVMHa1J9B5n2eZ9SOuHUBxAy6o9q0Y0dtksqa61FUyIuuTPXTJlAbAjBQrAAAllazcRG7CAP8yzZ9LIVNh83w6x72nguiURP-DvfMWS1dE38lKWX6jbDtCD4t7Mbkx3nZVc8UNScQToE4rapkuEDw1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993985f526.mp4?token=NlRUJaD5GDd96o1PriZMzper5-d_TAvqPdLf2Z80ZR5_V5666CZY49YyfDBXH-kThFfX5LLO1NZGdYLd3QhwvgA5uGGLwAHIaikFDmMKEKRMdvebJFs3DSMw6tBJWHICyJBzpwmZjt8MbY9pzaiWELKOap0VreU2vWybYhGVpz2xcQwAezaTQ09G1CKD6aXWVMHa1J9B5n2eZ9SOuHUBxAy6o9q0Y0dtksqa61FUyIuuTPXTJlAbAjBQrAAAllazcRG7CAP8yzZ9LIVNh83w6x72nguiURP-DvfMWS1dE38lKWX6jbDtCD4t7Mbkx3nZVc8UNScQToE4rapkuEDw1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور گزارشگران و تصویربردار رسانه ITV در محل تمرین امروز تیم ملی
@Sportfars</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/437264" target="_blank">📅 20:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437263">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2hlUxSudmBZjdTUQSETrgi-ev40z6O_TklVjg3BeXmHxZolwFHxZc7daqKUlG9TASS38MxGKiA9EZlJjyBbUU23gFFnWdPGiDMYyMHvnW1ThJphxb6VjAtsVLC-XdZtSkBNIv9sl67vOV2fXS0XxF6XXVcRhi4V64H40_H6J6PT8K0gm4DWSR1yd8TwjvmBON1__tVGuqzN2g54yCzDDmOstkYnTtWgBUs9L-kSBpLUewSQFH16ywojaoEufpPZ4qdNqGHnXYCqeZNxZsT4zwdQ0xI_8PeZNyuFVIAMoGmb8dYyG3-TNcZkxLzR5jPnc23mYZzDx84NHPUIJIvkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده ارتش پاکستان وارد تهران شد
🔹
عاصم منیر، فرمانده ارتش پاکستان با استقبال اسکندر مومنی، وزیر کشور وارد تهران شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/437263" target="_blank">📅 20:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437256">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N23x3ULqtIF35A0l8WnBSKsG-C77XaSjOAbos8o3UA-9eQHaFpxhB7eZPoRLE7c8XGb47uubNwOeIBOZy0M4w_c8RvCU4tzo27U1GTfnk-j2BiOYFpFt8dIY7mtkaHQIv_e6hMYLmk3ROq-2zFoK3mBmzs9Bf0n2yfGScjMQsxjEap4tGrs0hrDA0xNM84ZiWdInCUSWASY8DpzQrTa7wHU9du2EHJ4qLdDrbW0ENI-me36Jq_Z9PyOAgq0vyW4ufHZjmd3p990AApDv-tg0zyLi9eWUm9tOUG8IJed8RocLdpQhDOqXUKzmnuXDjBjky_TXhB1f1mKQfSTXquzvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsvr5KVGGn3Dx_3ggoAeMCQLSdZKjDENiJDwjsLhbJRjtwttmO5yVUs61J1i6NiAHPtsRacsCFv1xLzQ4QuueUtjLlmaGuMNY1h7v2ZXSwRV0PuJoS05dXlUk8Ox5OF--yaZdceyhR_UYjba233bmkDCE8vQjo-EaPDWyenCnBf_uYQGjTK5ujxmBC37EMLdOMI_RilYwYwdh0MXJa1gCahHY1lU7hivw1rmi5OtzX8Zw4h5ogRXewCUHzvQjPZgA7GC7TvltVDLyr3NDA9NS75fVuzzPYBKhdzYI3d-4E_IIWvLGfXUx1M4ZqU64JHRT1RHfzVyhe6XAj50bhk5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G69j4Os5ejNAGQzA5YMl2X0_hHlTxQoZkXg0r6iyHZaF51S6Y02AyM3YAobkgdqaOymwd1ST_KXK-5LqnX2vnfAFSo4BOiCbbL867GIG40-s9QGvkZ1lc0qe53QKLtzZCdBVSEyYEeEC7FIRzX4CyDHzAMmlZCaKr1NDA8ILWanTRYrcLCZokVaNVpZF-BkHgUz6FvHu0whHIqeJdL0txbYlXosOhAO5f-deaSMU9uVARVm7nIAXuG4V3UivTWGPhbLiMMOCaF-ZKx_HLdsipyQsX93oeYkVjf3ybHvN6xJwGhYGPshtunn990VJFGBwn4q_29elM5805FUtiUTa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT6zNjg_rZakp1M4XGY8cLqGejOReb4GnFHyH4A_WVFlvud-aa21jkI4eOIMYrqEeTu07ACHFDSpfdaHkuSA2HT7ITTHFjR4okZkh1loyIXCjETAQzVqHMx52j6wV3_N5CRB5_e0nPdd6nngcUBYaqoWKt_midfKMEsGdCvjciBlUZoyETiRSgIsrXRxk85lULdQPmTP3g7eTX9KYTddbLxgMLkthI63zw6u1BtA2bj_RG-sVfIZgUjy8TCrpfiLwOSYWua3WxSidr4iqDq8-4DEV0az16WHVAK3uX2EXPRWuG43By4Q6QzGhOgsg8obH7nHn3vcPf_EiHTzSsp8nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2kkyKrhaqlgZq6GCwrhBSw2Ym0Rui078BB-FHVHPJJNthJSgDgQzbvR7iy8OyE76Y07wU-rrWtskmGT1Ui4FU902xj_XeMpy_MdUz3xNwYha7DLiSfKtrT0f3vkZOqZgDNKjOflb--347PDRdvMi9vLwP87QWK7OUso_HcwRjCTbHIi2jNqLZ7tMyNFtDxnWuz7jz3URBwmyb5zGDMmxwnJ0vne3g62XdbIRyuPfF7ST5RZYwE5DnuExoQX8q0L1QhLscWytcRtjd97UWVnH6caKiuLEyA3PFdgQpTognL52XT_YsVrLmdr0tRsZ-6eD8ZEkKgXQaiHqFBUmVzszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMtUAnGZTBrDK68EbWE9VGzWftjlXtxmFx_9oj7ESz_6l3y9hdRoX9gb4LN1jFIL0ocq8HP2x4mJ3qosavKTgG7OmYWlumfyOZpp08y2KbpU6Mn9porEVhptwWtbb2uurxnAI6X4XkAGW9_RD2vjs-PpLjRIspOZ_K59TWnlPgsGiL_uZKVTGyoJ63MNZW9DvrJYN3l9HF6IPJb71hJp_P2a378jjdRaX6HwIp0UbkQyZBwDWL7-4VfWniRR0kkLfX_bdo4ucYA8-z9mNLX6Qn5a_UBYI5unehat1YxhSP4tM14zER0dZSXZdr7xZgME_Xdqr1xYOmeh34NO6IviBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N23x3ULqtIF35A0l8WnBSKsG-C77XaSjOAbos8o3UA-9eQHaFpxhB7eZPoRLE7c8XGb47uubNwOeIBOZy0M4w_c8RvCU4tzo27U1GTfnk-j2BiOYFpFt8dIY7mtkaHQIv_e6hMYLmk3ROq-2zFoK3mBmzs9Bf0n2yfGScjMQsxjEap4tGrs0hrDA0xNM84ZiWdInCUSWASY8DpzQrTa7wHU9du2EHJ4qLdDrbW0ENI-me36Jq_Z9PyOAgq0vyW4ufHZjmd3p990AApDv-tg0zyLi9eWUm9tOUG8IJed8RocLdpQhDOqXUKzmnuXDjBjky_TXhB1f1mKQfSTXquzvsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گل‌های شقایق بهاری در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/437256" target="_blank">📅 20:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437255">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW1fdOMZfiLY_JzazaVMf7Kb4bhYUsCxxIDgI6udheg0Rj5znbRUB5VnjS3h_iHJ72V5-0VEDnSd5plY9ra3PjQaKmDzBOuJ8kVC-nry95CRWDnBmDqR6_TExr3sAkIfb8s6KVOF2XXSFw21NIZQmntIFu15W76r3EwAe-mwQ0gm1uYhNdhp183hc5UlZhH6k-JAu_SbJo0TbM-GqqQ4aVW1MX-MjAg_KV0hl1Z6gHlGLeLPhzD_KPVu-ITNUuvT57rjEMczhzsRwwNVxfGElPNyGcvVuDanPLIYeZDNY3d43P-lw9FMK_xS8ysGBr7FgphHKkoj5V4tyg4t7LVuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: امارات از جنگ‌‌طلبی علیه ایران منصرف شد
🔹
رسانۀ آمریکایی بلومبرگ: دولت امارات در روزهای اخیر تلاش‌های فشرده‌تری را برای پایان‌دادن به جنگ علیه ایران آغاز کرده و با پیوستن به عربستان و قطر، از ترامپ خواسته تا به مذاکرات دیپلماتیک فرصت دهد.
🔹
موضع ابوظبی نشان‌دهنده چرخش در موضع کشوری است که همواره رویکردی جنگ‌طلبانه‌تر نسبت به ایران داشته اما بیش از همسایگان خود از حملات ایران آسیب دیده.
🔹
اگرچه امارات، عربستان و قطر در خصوص نوع توافق با ایران با یک‌دیگر اختلاف‌نظر دارند، اما هراس همه‌جانبه آن‌ها از تکرار وضعیت بحرانی دوران جنگ مشترک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/437255" target="_blank">📅 19:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437253">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTYKgk9xrz2MFszw4vrYFklcPZCOYhgTZUcWFgEgwqhRMDYaPmkorIJfCVKH4Xt7xPL-PnjbwQbmvK09hGQ1bsT6BLS8kXHnTXqJkbTRAh6Kt0l5kSGlX4ffj6ojVhSWpIykorSyfWuyu6YVqEBNjlegvhey-36KCH67dCl5nNZFfFXfVJUdQLePQllwxKJgcFfVIDkmSlHsAr3bdEKsqTPYFCie-AO3FQdhKumFruMwAz-Wjv43sjdILehS5AuRbrr_rLmHsqC8vSxtun9_YW8-PL9rfuSkTvnFzU9NxiMIhUV0K5XNfqrZjD4e4hAfHVsTIwHjcgm7MwfJu-gIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگزاس امنیت واتساپ را زیر سؤال برد
🔹
دادستان ایالت تگزاس آمریکا از پیام‌رسان واتساپ و مالک آن یعنی شرکت متا، به‌ اتهام نقض حریم خصوصی شکایت کرد.
🔹
دادستان تگزاس گفته: ه واتساپ به دروغ به کاربران اطمینان می‌دهد که پیام‌ها رمزگذاری‌شده و امن هستند اما مسئولین واتساپ به ارتباطات خصوصی کاربران دسترسی دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/437253" target="_blank">📅 19:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437250">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUqFRp_6LmWfTOjbGgoW2Pq_N2AUZKFpgN6Sp6PpTzOpIW0YQ2FYG4Me3TzEB5wbZ0x2m-YG38t72Wv-T2xMvcRg02uHxx4Q0TpG1dVe3rEwRwfH63Lgq28r1VB8lV1GI4mb-U2PLatiGPF3UsH0kN9O-QvqgeishWGYwUGuIr1nK20CdJiDg9g4xKS3VNOXbtsDD6FsOFt3UBsORL_kqaDP1XY88J68oGnffiKy9GLpY62yiMwypL7elqRnjtT3cURAueroMiU7Khkex9ziBSzbSul4QkQtoR4aV_L8VtAGnJv0GNbbdzXKuFsmxeAFtdmsa6DXTs-pjvMK92jYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyFqMdelbEReuMgwyYr_oXbdyTKgF4shBmoPTVaW4HklO5SgvIhFzxtenM1WBjDZDLK8X3NTIUgc0SCEfSlN0yRe1UvSas-og9qiuwTbx9d2059T4D6tT8esxnQkM0UlBmS2BBDQtWLrECiv9Z3SZ0Up8mj602SsYmvHuHPXSPXAHYbd36nWQDRzbcZ8xKQxbLxI_TUIlMYW3W9597UIAXo1rora_VXmr8CiiU6Z5Vs_kqYjrD8hGAQdVO-VBDjhpN1VC9lCF1klLu50hW2NJUvHH1RkQoFz-nW81dOiCoVSCOtzBFqgmmxUfT-9uf8Zc7rzGUlzvO1FynFQNGm89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erkHWQGutT7gJE7kCOkl0LFS9FIikeiMoPWkcc_BssFoK9x79sCaKH6-FQCTUa6ijj5XVtmuEtEfR46Q4sOr_RV9H0ZLIG0_lpj1Y068uHgTfMbMQsgrQK1l_BiwxCBVhCIbkbj7yAuzdWlLV9FIW7PEiUPsm8WSudDrSO9Qd9yYFC2KC2U4P3idAUmBgalEui7yUdjnV5UAE_YPclL0jLqq0VzpQv1uBkVcW9AG5fHLPNklLV32D98Cz1nV8Sx7jPsxWc3opfVogJK0nKzYW30OJ5yYp_dTmZTuB9vOLGx1_0X5s_3SLrp_1mNeFUpdxLSFsPw6nDnyaPIqT29hGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
حملهٔ وزیر امنیت داخلی رژیم صهیونیستی به اعضای دستگیرشدهٔ ناوگان صمود  @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/437250" target="_blank">📅 19:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437249">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
جنایت ترامپ به روایت کهنه‌سرباز آمریکایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/437249" target="_blank">📅 19:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-437248">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878a398064.mp4?token=jiwM0uqEtbOiFofwiLeSUfvBWlAlPjRZyYrEtmmlHMvu5EF_dJhaGwSlU6S4kGbenUhyiiRIlGgfTkKmJT45yCKFf5RmJnemNY3OOiCwvIfqGymihAhjclaDuJ_LRihJqFAQyw0LDE5h7ccB9FITeFU-gwGrKZq7shVBtEbD58_7RFDULT_HjWamNkArZ2sPrtqe7hL0txDqdPVT5xsP8C89AS84aIdg4_ds3INikp0yWHG2A7zPEFE9l_wYg_ydC7soIJC74dh_UqKE--C8uLHyWp1-la1DTlzhb7xloy_SwuAR46VvnBpd9GxA4xC4txsGwKE7fYC1mSXPxdk7HnB-3asoU6Gts5SAxFBkMQgqGsOEzYP89apBru32IaKPWuGp9vzam9XeHiabe-AcT1NDiPtZvxZ55DZjPYFxH1VTZcHCYjJeM0JDnRf9C8DEljOeB_PCqfLI8PXXjZOvYKc-8U3nj3QWycoptBEv6dG0F0YL0upwtKCbF6smZ9JoEZjtlFytNazZM91BKl6XspS-198maXvm1MFuzWnon6qlCK2bsEoHDAlef72ziC9GJsZJtRFmNdRtLPsKb57TbfHmUdYOPZbL5QLrueHbAuBv06NfBwup9HSLPcXRefqhHyif5AhPgzYELdC2BmGsSSsQSo_gF8nsBCPTkzc1HPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878a398064.mp4?token=jiwM0uqEtbOiFofwiLeSUfvBWlAlPjRZyYrEtmmlHMvu5EF_dJhaGwSlU6S4kGbenUhyiiRIlGgfTkKmJT45yCKFf5RmJnemNY3OOiCwvIfqGymihAhjclaDuJ_LRihJqFAQyw0LDE5h7ccB9FITeFU-gwGrKZq7shVBtEbD58_7RFDULT_HjWamNkArZ2sPrtqe7hL0txDqdPVT5xsP8C89AS84aIdg4_ds3INikp0yWHG2A7zPEFE9l_wYg_ydC7soIJC74dh_UqKE--C8uLHyWp1-la1DTlzhb7xloy_SwuAR46VvnBpd9GxA4xC4txsGwKE7fYC1mSXPxdk7HnB-3asoU6Gts5SAxFBkMQgqGsOEzYP89apBru32IaKPWuGp9vzam9XeHiabe-AcT1NDiPtZvxZ55DZjPYFxH1VTZcHCYjJeM0JDnRf9C8DEljOeB_PCqfLI8PXXjZOvYKc-8U3nj3QWycoptBEv6dG0F0YL0upwtKCbF6smZ9JoEZjtlFytNazZM91BKl6XspS-198maXvm1MFuzWnon6qlCK2bsEoHDAlef72ziC9GJsZJtRFmNdRtLPsKb57TbfHmUdYOPZbL5QLrueHbAuBv06NfBwup9HSLPcXRefqhHyif5AhPgzYELdC2BmGsSSsQSo_gF8nsBCPTkzc1HPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارندگی شدید باعث آب‌گرفتگی خیابان‌‌ها در گرمی اردبیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/437248" target="_blank">📅 18:48 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
