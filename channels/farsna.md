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
<img src="https://cdn4.telesco.pe/file/ejt3VVXoSgDvPPpmW07oFM56JQwG74UWeY0JkPlKdgbx5pTL9g6N10btAv3H72hW8xpmxdgyykBPbIm1lYM_IGMxYqMQOvgxAYYRU0sFHJamso4J0WscUb_gMvkNR2LOBD_us-4HwySs-q-n12k9NsHL2gwRcj8kR57-apfI30wPH0S9DP6yRq06f23mjDdSj7_wLkU2fOn24kA_9bO1quwCPqJQ5PhHpQhn2RvRbpZAJ96VtUKPgauYjs6wCd9Ju3KLOQHulov7wFkgee3XnJ2NEVuUx8gKb8JWgPONwDLhxRm3_GoUolpSLXpqbEiJdam-T47U4viScELfmWqU-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 02:01:21</div>
<hr>

<div class="tg-post" id="msg-453264">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تعطیلی تأسیسات گازی در شمال قطر
🔹
در پی وقوع یک حادثۀ نامشخص در تأسیسات گاز و میعانات رأس‌لفان، فعالیت و صادرات این مجموعه به‌صورت کامل متوقف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/farsna/453264" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تکمیلی/
آمریکا حمله به پایگاه خود در اردن را تایید کرد
🔹
وبگاه «آکسیوس» به نقل از یک مقام آمریکایی نوشت: «ایران لحظاتی پیش حمله موشکی بالستیک به پایگاه نظامی آمریکا در اردن انجام داد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/453263" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0qpbrYc9pnO22oXHrv3QSznzUgTUE2MbXbq-q1UtqXXDWYNN1-MVvMuBzBc1bXGst3JFfWXjuPdES9n7penQyvaxaYdE23wUE5cAmadmFIjEX20r5q_C7Ogh2byS2QKDskL6aqWluCdz-mIK1ezLO7tmRRXRhETRS2eJGgbUtnnVhtGX2EQWtknRD2F3-RrRYgZPgJeRhhiszEm7M2LOiC0FzHdmf1R0QAiPeFwBS3pWc_3diFxo-3tpcD629N09Qa6pAR_waJEqyaKbCsroFRqjNegJzluq0YdtRtdeV9uiNfIvYmxWguVrIxIHLjr7Yi3Smk4FWw-vvZGMx1tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رسانه‌های عربی: سامانۀ پاتریوت آمریکایی در مرکز کشور اردن فعال شده و در تلاش برای مقابله با موشک‌های ایرانی است.  @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/453262" target="_blank">📅 01:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453261">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
وقوع انفجار در پایگاه آمریکا در اردن
🔹
منابع عربی گزارش دادند که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است.  @Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/453261" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
وقوع انفجار در پایگاه آمریکا در اردن
🔹
منابع عربی گزارش دادند که در پی اصابت موشک‌های ایرانی، انفجارهایی در پایگاه آمریکا در اردن رخ داده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/453260" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkX1vIAFje5SVS7VSNQepK0YqXKtkP56D00KQfYrpNA_xx0Erh_g4mlKNPdOT6JUdUnMa6wUn5LKQqP632K3BOcAZiaiGXYHMQeHWydsbioCFjrtbqj8nMkxnF9yIlhC28jyXwi3jZtpEGeKgGVzt9Ol6Edw5S63900BLDT3fsKf35WyWIz13pK3CVFUNoxVenUyMbJWnAQxbMq2lG5VjW8HLodDy8kqeaAVbkRUWCpjag1KcAaOvEN3uBPACQJa2HhNhuHqyj8_HlXB5mGCvn_Uczo6riP7kuKvGq0qlkoKeG_WVxhaoTa5FcLslW44gKTtGWVxi3wlGfG4xFLLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
خاطرهٔ فرزند شهید سیدحسن نصرالله از اولین دیدار با رهبر شهید انقلاب
🔸
سیدجواد نصرالله: آن زمان من در ایران بودم و پدرم که آمد، گفت: می‌خواهم تو را به جای بسیار زیبایی ببرم؛ یک قرار مهم داریم. از حرفش فهمیدم منظورش دیدار آقاست.  @Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/453259" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOZDm43Zt_e-C52ifj9OfugF_0LLEJ7gMTYFEwiBqB9KBi7NBQ8rwyPMrbZajaiUqDvTclOmd3UDGIZbm_uzC-C-TxuqvBUj2vyjKtywvZ4ZwzwjHQqVTs0dhhDloyfVYUyDos21cBbuCG-mvXtDh1QicTiMH6QJPwKTYKsHlg1fAce249lKkoLW6pLEl8khptJSQJQ-ckpR8lgJ954Zt74aNJrTkG0O61C_VrBD6mVflD-CnJRBqVzr9JzpJ-dq1u_KW00wGlbfLMkEcDihlM4Ky6qYqpmrszrOEudXrd0LNj2Z_TWsQvF88O0n5IUbvOcenmhRtQahuoStfj8iLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rquMfYKdjAKAOMF01ZB14KEW3A40DL-vkYGsN6BWzgQo6RU6jKMZktEJdvweN2E1zgojySfBw9MpRZA5WzhoH4KKeWVxOVCLUfxdYgoVOHdrVrnr_AnZ9_NLIcUQ7DVvKKOu65MDY73mfNqBa6mMUP6fn_EEZrIaVCsrqWJuPIi1Be95ggt4053GYAtH4NYhEUQYYHKpyZNy8DBhD5Iqo-X8ArGNyHSOK5sqJjdPJT7sfRSlbs4YFa1tOftgPM4HpbktnKsEzhSFVuzO4oUz9vURQVvbFavNkAbdwHVxXJYJrxF6wJKVwmC4JUJ0SYjIAr_lcjd_wGPwqFwW4rkJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKZTDfsWi6sydLg1iqwiPyTzCHZtpK19IM-0_IGZ3ejSCYlbLiDPufpQKtOZ7j-SGMPUfYnA0ls3kCg0_bRYVg1eyjAo0tQnccchVS_20kFuCDtJwvKpRPp3d6P_TDI9epnQ2rzyL1XEZskw5jR6vHORGmRvbFZRsJgE_B5JqaMsYjktLnGNp1fAj8Re4QIe071xpqKd5GxXUK9t7HE5AKgBBBd2dbOJaB6tZheLo5bAOGXfgcjA6eDaIX3rEtUpHWjtbucL4t2_8BUBLdQNEofZKRDiYW8Jj626tZwmJPgSOAELwVxd1J2IwQUv9QKJ1RMKRUgVZLDJXN2I5yXE9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwW5tXAvhUHNFgu6TadtTyhC6rO8Tv7pebovrarPstVWEdQnpGTm3ut4NcG0Qwm34dRTfm70QttU7Sya_Puyk91Og4cBIOD9Ixd2DmWNdFYkKHXroN--uOxiXNpqoz7g0VCW87btirubh4RbskfGALCB_fg_S7oBGVbbxjTXvOSt4OuZun_agpADcwe83bWrykh1b1yPJsXjlLCKumGgEiGuX2r1SJlEz4sen6ztGrSnHfh8iypePHcPkwkF_YOF_kMxjDwOjdUfbqyg1JGfBxl_Cet-X50MwL_cop5HWlvL1fJbH6TeQBWYsGYRGS0iFn7lbgvUBtlmoiB38Derlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnDdrRZVF50z76WOX_rFYL0HfZY4eLBq0GevkiaNXadsaTmEobg5dtpG_E-CruLqIbHH-INNmWSTh84WysguWESLUCM8TOpmxKPVGuYng_tk-CGyGnRfXSSgL86FuY1w_aUS5hyiXp3YwfzjzTphdZBf5S1n5SNNQ7bZ1zp5svX-nBEipTLX46QoZLQQE6r4psA81o7joX_-Fd8-ZAOHDDQzgj7jXCAa1XF4HIsAZws666HemsMu7FjPbIowZs4iZmpjOmTscICmMdVPofI0klgJ8XuHW61idcmxzqcdR2hkA3Nxf5D5P5gfhBVZ7kVAwuq2we8gIZ6an529OXKCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyVP_bP7PcNLnXxwXZFHm6ORHiMR1evhgsgACQCAYpCTEr8SAS5Rm59NWkmjjrssK1FRhI6J3c1_od78NXnOUmKoi7xEsVi4QEHtmwQuk1J63GXGpys0rLQbc5cVuEjA-FQilqX9HPSoCEbbo6k2fGQmbnU5bfSpmV8zam04NHuTDv3_lebIoXGybUtu-tvGW6bHeXVsrKM_iTtBapgacWNCxQzouO1Ki5XCYDf-c0Bf2HgOwFQjAfMcF4DvOrn9-K3dANFpqfSsaGrOFZmiwlIRCaTooaObfDK9eJLrUcajl-UhB26RQOnt4xx4usmFiK3ASpZpcoEUj0jFrOBkZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۷ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/453253" target="_blank">📅 01:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrtF_Su2SswkeCPZNSi_TSokgHkslZCPW81H43OqumKi5PH9k0BBEcm3hmtc6K7PqrMVLly81kBojdou0odwQR7lqNe3Xk04dQs76USa_GxbU47rq7M01EZlEBi4zSvKwp6y48y1q4qISptwXjPfeUEmJsWtAF7_iguOh0Z-2O2-BIoPTquJVI2FkaGDJ2H3EuHKsnSI97xar1FKIetlMrfq0RWQYkppRg4yteQ2WodSQoPhQBfLQ-bzuu9iPQt_B1mqZB9XszEsEYXnTm6aPJLf4OfgwHL9HKwBY1dGQMBPJPG9k5c_onO50k2stjFUy1-pUiMsKM1_2r1s0tkMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgCD4ZCFew_hTHU-ltWkd6vzwCuEVtZWCG5aCJrGLpEyz7djBSDKoYHuA_-N45G62DMdfF19lgoukjxKtUCxBZIQQ7M4ewR5VyM8-Pm-RI1hcPbyD_HfRJak5BUOj2wc3e2FsJiugsV6cuanU1yaQLUI0J_03CeSSsj7Cu_u7TjoFcmZEF1KpqDS2n4fOpAsU4Xeh1rWUZTG-jNzaz49dL79gVUvVS3K5CCsnJip_5BdrSz17ZZLUEEfFTFd-PkvI8v-SbRGvM56i0Utwvt0TH5WtDvZamcjZtmcvL2qKWDdnCAGqCfNbOJCgKf7-HRY-bfye0yQjOUIJd6ox3AkgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cB55yRkzDNFnTYX4GQfmlcnz4jRpw2BTZgugM_y2pzYvZZYIKC3L7YOAePkUPCeojXOfJxweG_hLSs8-eh5QrJd---5NYxEX5M7iTQwjNMzUpyxr3hAIfDvi6Rax7aPhTMKwhrGXMf6KMJP3waATf7kZR3rCPz-6mgc993hvbfeqa7WF3VmpxBqvD1YYn_9w-8R6ru_mh1qPyueJ0Pk5rfOrTwoCzVL6C_ls7LtzNLfbr02o8pEj0fEGBx5CA-0WUL7qSlcAABkrmf3XjP8ap0i2WZ36VFg4mPNPjV8gUEFNR2iVy2z6UO5ipjEuBEFQAqAvo_1w008XMIFpaDonCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QISnJV_ydoMJ_3TLqNEqKLdtbQQixN-CXYW_Y76sHiNw9-IQ21bvs-3xu6V1XVpXcoJq-n7QqWtBe0xTOMasHW0kizu7jqcXB0JU6vmDMC-KR-spNdPtX1qs9G9FiVBkjHq1PvuYqVEMQ3rsflVv7aSSvo1DWr_nkyBxiv_7YWNo7m9zzGshFALdsMnEE879y7tNDlyZv7IpEDIIoM8t5lg3oUYA4rDvzXLhOj2E_UWkCrHDTC9mBat5YRyGy9VISCkUN_Pj1o5IaDOFe8Di0GpzSztDufEYem_77ZjuUYbHkkUo1R09qiyY9xnz05619QFe3umOJMYgly3je80zfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7mWWDVDKCWkJRSF8AeFaT4YRBBmCE-7K_EiFq6fOW_UoAtLqRGTpwl6C81we0dVWind5JxNW6JTmPIrgb5HwmawcP-VxlxphK9bkGvsfFz-8sf9Jc7tNqtSwZstun4IqHY7x8wlnMCKl3XegHGxYQ5-9jjr6UzCXnR9YT2YEAUkmeY0Q_9K5OWrMuXe88suHnQAItAOeBQQL2YZOGW7klFVgm25x9L9P0-Z2w2vzXEcdnJ7uZLUncWyuPzRnT7Pbv3vItjeTNrQFpXbJiG3e4NhdXSXJppr_vtppDAguMi3vMkN09WcGfFKZf4ec6Abu1ewcLQNvThVzmAWqDWhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKTFWMoTAYpzq2j-dsvGmKc7yxLgq95AC6DuovppBU6d9Zw1nqrzepktRx13NOaX9qRZDjVfF11WrWDabOn3H96zoxRkmAc9O1w12VN4MRkSgxSiXsvDpzPl4iBrRkR1YQjMZcYw9tM9fPKHG09SMElZXFjNjI5u18wIMFZozO5KTyBXgPQ_J9iEVzndUZ_YnOdYQ5Rcbvp0bXsMoDEbZ8k_Xl4tHQPF4OAQJbxmobE-CF5Noau6oUnG-PJ5GNdsbzTxB68-WVWSWeZD2VNkyT1WKL4b16EA2I2SWotNUVuweW0ktwWEl-iTdRURQElXELPaHnlen-NdLrLXiN3Scg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZM86LsV1D3uq7AykXIi5B0DYbnCSmMNYuHBq996uREBW0cRORp_xMBd1fsYGdBH6qZ90FlWsp_mIZ5RbHcANvUcfA8yu8cVmcFk7yj9BrN6wDsTcM1Jn3-0HbDZ20P7mBAXH9kdBwWu4yvvvt2TgDrPVTywygXrHcJUNwE1_Osyni0c0cVt-E21lqzL7kY7HWt6i9Dv9_qe844NqdT5z7R6xub1oK_5Mb7r6PKvlcrPjZYTv9gMz6xoldku2BOcqypGq3TtRceAUc81cIzt28tcn95uvfJQvABhMC91BQhOaeALcdhZSPRp-EmrcXI_yzliOOgfHuIy2bmh3egp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R19rK59qeb-wGnY69cXtoxbTkPOU_rzrDqxcMTBru7YBlSuwhCd_k7vQy19WIjI5Qwwp3zwe_8sEI1SHVJwLF5uB4l7GT_j6fEe4SBreoE_vkk8SPTHUdTkqrvj3Z6fXkzaVVk6m-bD-ArfoYtVeuu_07NOZxZmZ_UDA5rN2pPJ3c0NasvPTiLFFNVf36QmQGvpkhwxvpwTY2xVcaCElxqf6ASVgifoo64rnMwjo7amxleDEYhi7x7-q2y0XYqhgA1C9TB22gwmYCwSmY5GGQyaoErsnGuGcNfIiCw7Cv-82FoVva09Z48POXY1bO-fY2UzdY1Rl18b1tf1yfokDKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ab5JtIVIDRHfujT4Djy-RNnAas7GTTNIyIhjTxT4l_aE3bGHeQtUNwUZRZKliJm-ToYi1QMlsHfELk0y8S1JlptUvxGIR60p_Domz4XcAWfjIp5azLgZ0hf15LdVcLLewsHf9qrOcdDonbTYY_4rgZ0NGJhBXi-3TJdfrmJuarcWCS6Fgok0B4zPX4I08dYH7a4BcTUbA9qiZhtWCLcIHOSjdCqeCx3R_ijjnBGKp7I_CsD_z7MU4d8JyxFI1L0twPF246cA7igmhirVycgjzd0OfrJCVQh8qMJX4uhZJuCaxkqlS-dmvo_K5RooFBNXzXM0RqDsnqXJO2kGIs1-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eg3wSJsVGtunzLwWocIfH-EreREXE5cNU74yj2u5KBtXMRBQcePmpB3oaIhYmzy6KIZmMAwoDVA5ftx7lpRIrvzo1MZkkVeF8ohkx8iteDDqnTDfMCg8FG9ly4DaN52vtgFG2hjFmbFFsGHIDu8Cy65k6zMiJUs51RZUxKXmgqTBy3Y9-9nWG9PJkpI5kzHuCifFyQp4G1ApVDs2ggESLSFMA4Bc_tLH9ywEfHv_pGgdf7jrjQEBc7fa8HI3dT0UdoW2TgVNBRP1imM5zV_5RqBjjPEAFEadAILwpmOILmlZmKMBMKwBalwEkgAsIsZbQPX3AD0bWfPxOuALyjCNNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/453243" target="_blank">📅 01:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
«سردار خندان» چگونه متولد شد؟
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/453242" target="_blank">📅 00:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn8OUavM_Nm3U4u4Kzy6Uxo5RhCX9OaZvsWZivANVWsdTrWF8kS-Sczq4eyt6oK83dvrdSo2V3hcJT73TP5jLsbPfSbRUAg99rP4ngHosSWV_EKbIBROTe2U1Nr3lCMmzox7ynkcxjGSvSnbmh7ZwSPiPlgUTqKYV8Gk1Qkp43x52Gl3KWK_6NnfN-3-e5sU-NXhwvizOOU0gGUjbVzdxKg6cwOgMpz_NQc50moUB3LYyZGyNTlN6xinuQeHUgYOWx73z_cc4pD42GdCwaBkgRjFAncqVLOsPQkLWym0wIPxj9kz5bOr2-LBNsCzUpN3ePXTFzrD_SdNANWntoFBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
در این اربعین سفیر خون‌خواهی رهبر شهید باشیم
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/453241" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c620548f5.mp4?token=Fzt0SomIZ4ZQV1Dlnd17Hd3lPjl_ntIBmrGdrsLicCXFeMRwqp1hJx8QHiW4qt0af6HAzzNd47VL6C6kAkGhgevOrm_nmmPsr6ipDZgzheZ-2tyuiLlStNiByUcoyCznC8y_4U0M2SK2dfBR5GN7RvmbdeJO4gXVHL8_I3FKYi8au6pN2YXSrlqxsPAitnUS2q5EYQobOAdLkF6ohQmdtVqJcCJlGqOhvjr3mxxpwGcso--BfZWfK_TZYGsVde5AMZj8zgha0p8_nPY1v4vIwoUQ3SjssVBcrSlvRRx5oD0vbVtDmC_TERZVw_rDXF3QOzvtiYfGt7Q3IJCEEJqpwJ9RV3g3NXypK03WQqRgsyjDKG7wHhfkQqy89KUpfwmJbaw84zqbv8Ls43_EBCJRuH27hJHFwsEZPD87VnNa_0aRKYpzJVDNzwOAv_C6BNiXPh9PzfvvnaVi3YrAFWrs0dxq8D1u0-8IXsCB0MyvwHziRvmWYUlKQhveScRmQ7zBGGYLDfq0ogvAfIIQaYM0v1R2c0CEz2-xWlDQRVDi1jSE2dFdUGhEdsHCYImH2O4LQY-F-ecLOqkzkt54b9abfikUJqwQ_gBQsTgmA_IN1cFnZZbv_uuIX9zE68EqrSn5kj7lgnveqx3J-FFhpPw0Q0JkxVYeHaqIKtZqLOIt85U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c620548f5.mp4?token=Fzt0SomIZ4ZQV1Dlnd17Hd3lPjl_ntIBmrGdrsLicCXFeMRwqp1hJx8QHiW4qt0af6HAzzNd47VL6C6kAkGhgevOrm_nmmPsr6ipDZgzheZ-2tyuiLlStNiByUcoyCznC8y_4U0M2SK2dfBR5GN7RvmbdeJO4gXVHL8_I3FKYi8au6pN2YXSrlqxsPAitnUS2q5EYQobOAdLkF6ohQmdtVqJcCJlGqOhvjr3mxxpwGcso--BfZWfK_TZYGsVde5AMZj8zgha0p8_nPY1v4vIwoUQ3SjssVBcrSlvRRx5oD0vbVtDmC_TERZVw_rDXF3QOzvtiYfGt7Q3IJCEEJqpwJ9RV3g3NXypK03WQqRgsyjDKG7wHhfkQqy89KUpfwmJbaw84zqbv8Ls43_EBCJRuH27hJHFwsEZPD87VnNa_0aRKYpzJVDNzwOAv_C6BNiXPh9PzfvvnaVi3YrAFWrs0dxq8D1u0-8IXsCB0MyvwHziRvmWYUlKQhveScRmQ7zBGGYLDfq0ogvAfIIQaYM0v1R2c0CEz2-xWlDQRVDi1jSE2dFdUGhEdsHCYImH2O4LQY-F-ecLOqkzkt54b9abfikUJqwQ_gBQsTgmA_IN1cFnZZbv_uuIX9zE68EqrSn5kj7lgnveqx3J-FFhpPw0Q0JkxVYeHaqIKtZqLOIt85U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر شهدای حمله آمریکا به پادگان ارتش در بمپور  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/453240" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oD7xhwqDRzK7j-A2ydZj42IvmC5Kc-YM5AZ6U0Ma3FYPa-Vpx1zTH9IdsAtjevXPRyK5ZasnRc_VXiAB3iMjNhfM4Jk1vdlHJMGRuq5fon7Kq4Gmh16M5SLzimM8LGPJsRH2794Q4JCS-3Ju7IpYX7ELXN5XxZh03_sOISunVcn8zNuDPLo9Wkbbut4pKyqaTAdvMLCqo1yqHr9raPN0Cj0oHY_rykLv7BczQxVsBLcVItepvDde6Bd0GUkbGZibNEhLzEGUQzCLLxfQcxmsbocTHk3N-roSs6NH7uDBDpERzwIxUBXkTLETCgEhbIaYi-r10EWmwKOZvUq155Kkww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6djLFlP1_eVSoGau08l39T3BRqZSp_L-NrT1X9jIphsKVSNlG1leFNHimUNoW4xTAqUFjsyvugS9uZA3cjc8rl5c6F-vufGwfgniowqmk_hmmTql2DOcia552sxZ9_kkMZAGzVupe4BIvZAqmHmsZwZSWHejOYupzgllWMG7Qu1PHTd8vUrHAuETEqg9cD26AhPnl9P4461dT8HuTLHoCLJiETEHgS-0Xk_q2EHo0HG9YiZVW2je5R6N-hl461Pjwh6rBOD4pfPEp86xbISDT7aSu4LkX90U3d7VfUu36zCesJ4H1BGo9UbXyb5pnIN3kYterR7d7e8ybg0OeAN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1yBfVDMBcLfohXF8r8i9DBQsR9nTsp9MTHAAY7T2151wxgjY2rwmVNMhJxs-YPV2TaZt8BAITkktwuOW3Q6Bc97-HPXwhiEOY4IyKueKZgMpuKU_vucUXQF-ooM_bC6gyu1dM7ZWCLF48iP9IJmoE2sXBol3HApOggpCBY0KjL2o3vGsEmoRSefNHV6gVoN5SxOzB1g-aBbp4SAwD1y4d9I4HxUJlHhw_JKBNKN1Bp18gYk7URyB-DxCTHIMNdIyy2csHjmXNvqt87jhhC_hNjPSEu_jcpBMLydiLgF0XskXwsrs2tx6OlMx4Wop3zgCGRKejgd-ZfDu3RoD9uszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRe1FUndmyCF8nvWPFE4Lqm7_dojrfn_POtAxOKOhp-uYIie85EoZqByTKWYvqG72nA3O7RnHmu_QpyS83NFqerzXmsDcGQjpLBRdo_pxrYBM375qaHwT1brvQu76a-9NpKnpsE3vb_D3v1O29kDfuHBVpwFDeYUj2nPiGj2PB13GD0hgETb4GI4TUfNt30a_OEpt3g6uWYEDaSUK1KKW6KdspWZAbS3Dpud3AAWhKosL1y7t_6TUw_W9E6On53jCZ8acPMOF3gHV8zPuUn3rvbAGo8cpQdN4KYWeLpmtXD0dDnm4HjvzukY66H-eBrLE8HLsp7rb4xkwFdinmE2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9UVUO9pr2MqdzgnqOLdJm3vrGJrHTp8dVpmeUgUXdMrgmzqHHYOzGQ2vWwZTBhNnGFmhN5rg1-0TZGlUaNYeXh2XFw3VF9C6NyPFNyGIYFMBXUcssjfBf9rUlRUWb_mtGFRDO8Q6As4kqrMt1N7jEk_dxQ8OWLhGCoRmTdGsimlOjrG9DcLZrFfvIF0FLuR0vJOd9BsNKxBIt3-NgJebJocuQKb30mqS3lLJzVBIVIALf2z34SIzltrwRp4JUl_epDf3Mx65Zzu3xkyhSHOM4AAlEZ98jkEQIkJq6SOj4-dqoqry1tVkuiOmAedyVVExIb-kMLE9VaxU5mvsQSmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5S0z8O1umkgbmZKJcl7fBXGv9bIXhca3eJws6QX7-5PSWbTmqe_0Rmo2zMu3EpxkLPFeTJg_MRqAfpqr3ZGOUIsMqAsRuux-D6-cHjRXT_CBn1xt_BG3DSCB24IcEn-yA8w8VTwnbdqV9TS3Qm552hanaX7lTDepnz4vbVcWFuF2KFixzGjA9sSuN0CnELueX_yyKwILXbwz0JHPJO6VuNaYZfQhuJIahxgRaxVKm7cr_hkSvpb5O0qVVwdjQfy-Q4-qBFHoxLsOXTAqY43oNNJ5ctwvItXLMp9GCBzFZu9kWa72XUrutN5YpZCKoQajinKwhF_4TUYTFlKceX7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-CfCKWgp01EBU6pxN3Epzdmy33PbKgDzVJlCTjiBY6Xau6iSCVedd9zNqhUxW_i6cuujF_6IkUl20vXe1BWXMTwmb84WCT3IFwEV-hYR4j7wrciCH569816CbzOz1-AwBP7Mme4KqzuXEhJiBkiqFJCECw3WaM_D3HB2-Ksubp3vBYBWw9iWHv8AnVYBjxbkag4_ZRr30nkA7rSBM3OICmO06Mk7e9jeVO5Bt0Y3qUsgTDkJmus50Y-ZYbO_GNVXSB-EB38fV3aKBYyWm-XMzocJgGOvkCtV5NE8yzQFeJo3opaQsKcxlgwrCebumQxu0BWytF1YjMsIfESbwmcVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ایستگاه ۱۵۰ تجمعات مردمی در شهرکرد
عکس:
عاطفه گنجی
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/453233" target="_blank">📅 00:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVyKneAOzgysvm3q4EMHl-RYl1m6-D3BUZp2oUrQQyzzitK_LVqfj2XJSoSOUC2DmRHxsst4_XblrvRUixj_fJwIdGYRBVQh0agKoGE5FkOkC0HJ51a3ugDLL9Sk4quNRY0FjNIgtjiRBidrIPckulialjihR7CT4UMPwd7-g32pborrULKEzAlXQZCIGhvhs1rxT2k_oiz6b48RZqpJUbE5SM_ikrmeJNYVtNvjG1BVNkpjC6p_EjtaGx5Ckn9eJbHl--2xsAlyZs57Ne_6BJbTvUgpsn5tRFBXDn1XyqKK_magOa53bFK19_i987SHToSpfPCPS1bczoj4q2_-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از آمریکایی‌ها خواستار بازداشت نتانیاهو در کشورشان هستند
🔹
در حالی که نخست‌وزیر رژیم صهیونیستی به آمریکا سفر کرده است، نظرسنجی اکونومیست-یوگاو نشان می‌دهد که ۴۹٪ از آمریکایی‌ها معتقدند که ایالات متحده باید نتانیاهو را هنگام ورود به این کشور، بر اساس حکم بازداشت دیوان کیفری بین‌المللی، دستگیر کند.
🔹
طبق این نظرسنجی که در تاریخ ۲۵ تا ۲۷ جولای (تنها یک روز پیش از سفر نتانیاهو) انجام شد، ۴۷٪ از آمریکایی‌ها معتقدند بنیامین نتانیاهو در غزه مرتکب جنایت جنگی شده است.
🔹
۴۷٪ از آمریکایی‌ها نیز معتقدند که اقدامات نتانیاهو به روابط ایالات متحده و اسرائیل آسیب زده است.
🔹
۴۳٪ از آمریکایی‌ها بر این باورند که اسرائیل در حال ارتکاب نسل‌کشی علیه غیرنظامیان فلسطینی است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/453232" target="_blank">📅 23:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9ddf195c.mp4?token=kkJGFSykc5kQoFi8tF6mYr0mI02O0X7mgrFv-qGCxuDLf5smdcX-NDOhzjEWc9CKlQ255j-maCWdLz0CiYzOV8xhbXQVnxi6FLdfnyrWdisgR4PhYxV6Bh0btXiz7aKbHqjnlfHCJ85oXDTfH4yVrNZeZnaht4ybKt9g2B7fq0r54QEqEpeMpI_WVqLn5B8PmU6eWL7pWNRf9j8KexzqkNP_TZuED9i8ZeDCHlTPCi27bNh1q2lqKgcZHM3zPYINjoBbM8uQrL2Eefuu1LFlmLcQ-WHnO59nrKuIkBko7wu7TbocoIqIWAVArav_AkcsAhee5jXW_kSLznpJQ0y4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9ddf195c.mp4?token=kkJGFSykc5kQoFi8tF6mYr0mI02O0X7mgrFv-qGCxuDLf5smdcX-NDOhzjEWc9CKlQ255j-maCWdLz0CiYzOV8xhbXQVnxi6FLdfnyrWdisgR4PhYxV6Bh0btXiz7aKbHqjnlfHCJ85oXDTfH4yVrNZeZnaht4ybKt9g2B7fq0r54QEqEpeMpI_WVqLn5B8PmU6eWL7pWNRf9j8KexzqkNP_TZuED9i8ZeDCHlTPCi27bNh1q2lqKgcZHM3zPYINjoBbM8uQrL2Eefuu1LFlmLcQ-WHnO59nrKuIkBko7wu7TbocoIqIWAVArav_AkcsAhee5jXW_kSLznpJQ0y4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری مردم ایران و عراق در عمود ۷۰۷ نجف به کربلا که مزین به دکور حسینیهٔ امام خمینی شده است
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/453231" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453226">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1yMPXMnyOfamazQMB7w914O3BJNAjQ8yPzb_F9FP2oIRjVj5PHHU-HhQ9vI1hWEIsQ9EOj3cExgYGLISvd7RUrqWyhdQIC7VGxmt1fxWVSmqJR0hKkrlud63yzj4afY4OX0ZLvYD6mQFLcViMsO3Cf4Bl06l27CGR6t27mul1zY4WmmzkjQGSFBvaOWITmxpNCfgZZNGeffCzNLpdzOdhV4ogLpmjM6ApM3MfD6PDJOO9sxkmEZJHm0D-TFIJTTiRCywO9ZG8u1gXdR4iSr9Eel3W9CxhjoNr5WW5a_lI6YVEDYuFjNdcyuYtaFzuKy-XQAKhyTxcFo3HU0Zhnq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzbS4gmi6AH9GPpP6KxrlywmLJqhY16bb4y8BxO19SwuKdnvYtwGTTlx2ynhv1410UtOBVUNBye0T-7jASoUzWJB53dHnJSMXZc14rAKH106Uso625nQaBrtyWeGqyD0d-9q_bl_4Sj6ltzFpo_TXpYYODeYmziD6qjHG3mBfuIJ2Alk4laKupAyt16zgEmmYnSQQQNIF5GGEUkXr4lgaq1ATVP3ZUHBCvcwuRtNIkMMcHSGS4TGmFoxMjpxr7_gnLO6e5TS8mf5pIWJq5VOXPawiZQcfEZ7fKfbp27CsPch9OSwEte3rhm6EteVaxErS5ixQ8Eo-MocmFI8Lw2wZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BhV160hST7Ovr558PPxGPKbz6HUoD0qnpqsJ-Fy07vUZsjv-nbkI1yCd-N790ooTIub9sQPtPeTkjKDYwnxTz6Zysewb8kJchqrgDAeiyyRC4IQFVXvbZzHdH4q35HHLlIAKO80cEsMULZtgZNOVchpli8zSchBdtu2UuvW2t6nGCTKhu9FIjOe1-FrM1UdTrdwwlDksL7FcInaZgeN32hZurrDOnV-kIL1fc0TH3bMpAgAxV289GpgMq-iKLXk2jfCZ1xk1hoHGeVLW99DfKNY4EeU3ao6pWESCaqF2K4SvOxrzI9NpK2-uKupRWVrV1JdlL4WB9ah1TSlGITL9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XG7MIA5qCcPxaCQvm2Rg_4iZyv42ppFAye8MijUg5pGka2_Pbe6PopdGeUizfLazvKYOa0rewzyHZC4a7NbkjJaOhzlvCPf_2WohVUuZvXRCS-RLHgTEEKG8V5aNbogc5BPQmsOwSMsfrNjkqFBHizhrUWN2AzFzDM5BzUYQSbE8Wv4V1L1LlLz7rrBeLDGI5T-QgRPbyays0E_gbtvOKTX9hjuEEkBbvfgxWH65CySKSFKSoY5zq_LHtVm7BQzJrn3sQ6S8-569fG89wBbwiG_qAzHnKgwG5C9pMhcdkFh4VcP_Y0nsIpzwHwN0BhE1Dv7tLbgbSDbZVaKE5DBnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEAOsy1QVdbEBUn49JCbiE82pAyhn3-BFtn3cG1p-cpmSp0OHCH1uiuJlkUvNIC5OOlvnCtkNZGTmisIv5R5kVmc2_AChsdP5iQ0Lq86figgLUfHosY7WWSycGGdATyQExDL8LGp9wFMRbHuXHlOEo_cr5WmgOQ6swvp0rb9bNNRoNTeKxIvMSpmsCrH-g9wogShsbK7Qp-XU3R9kmuQH49vFZy4WrhMxn0I6bwujzMkWFxTwI4-xJo7u2RynuJKlGH5m90debTU6l6KGdTjVVJEsO78fUtNq9aaboOJQJFd8AlMOwkFVf1DwL3jXrcm_gte_17ugHUfYBXaJGmoPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از تجمع پرشور امشب مردم بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/453226" target="_blank">📅 23:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453225">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be9c7d9.mp4?token=hVMD-CZ8amfa1hP73B2mcFWeTZ79jnWxparG3wDW4S3zEJcLxk9GsfhPBdITbw7uJ5jt-FaPlAFBXJ11ePnrtFlIdg28yp-9VOwbYEbVuPLnbT8oVAIQu188xPjiYdc-vU2ARJ5g8PEWQ5Yhhe5r1Z4CwcQiQUhvebvesozPqSq-SyFjcJHxIQ4Zw30MWAUw17BhX--vuEECclBNSQEnnIWq-vOsTaQlXyNyQAmULvbEpz0-WZwGtoEB6Fbp3kdz0fMj8DokAzzEbS9_oUgvZTcqp6LLT6LCbYz275uoc-huNhF9hpO_EqE7n5BSNYyNuDcX1LGeIkRBdadzQgtZc3jBj1MJSrHtSLFTj6hYP7o1jvmjjLosyBtXo4ElMSNOUzpC10BHDZF6nzQVpVE3O3Hfr4oGgA7OD6SZ1GF3tbU9mC35IUQB_68eRrf88LTvBjBXmRyJMoSDzDk-P3s8xL48g7OGM_Jw9k47WOPwLtORlt2BWUoHX8pFDVPzD2tOHzKueCJ2PydrSq8r3LgoqpF-D91Nh-7FOUE7coQONh4udb6GLU44pYCBRE7FNn4uwzIm96X_-TcRslTXWMA65qB856q2NEE4g199i-hPS4-gzS75v7_gJOHvVp3Q3OsTGs_xnJRHQtIargD0HUocASGhCGsAho0vgMqDVqpSu5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be9c7d9.mp4?token=hVMD-CZ8amfa1hP73B2mcFWeTZ79jnWxparG3wDW4S3zEJcLxk9GsfhPBdITbw7uJ5jt-FaPlAFBXJ11ePnrtFlIdg28yp-9VOwbYEbVuPLnbT8oVAIQu188xPjiYdc-vU2ARJ5g8PEWQ5Yhhe5r1Z4CwcQiQUhvebvesozPqSq-SyFjcJHxIQ4Zw30MWAUw17BhX--vuEECclBNSQEnnIWq-vOsTaQlXyNyQAmULvbEpz0-WZwGtoEB6Fbp3kdz0fMj8DokAzzEbS9_oUgvZTcqp6LLT6LCbYz275uoc-huNhF9hpO_EqE7n5BSNYyNuDcX1LGeIkRBdadzQgtZc3jBj1MJSrHtSLFTj6hYP7o1jvmjjLosyBtXo4ElMSNOUzpC10BHDZF6nzQVpVE3O3Hfr4oGgA7OD6SZ1GF3tbU9mC35IUQB_68eRrf88LTvBjBXmRyJMoSDzDk-P3s8xL48g7OGM_Jw9k47WOPwLtORlt2BWUoHX8pFDVPzD2tOHzKueCJ2PydrSq8r3LgoqpF-D91Nh-7FOUE7coQONh4udb6GLU44pYCBRE7FNn4uwzIm96X_-TcRslTXWMA65qB856q2NEE4g199i-hPS4-gzS75v7_gJOHvVp3Q3OsTGs_xnJRHQtIargD0HUocASGhCGsAho0vgMqDVqpSu5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرشتگان زمینی، زینت‌بخش راهپیمایی عظیم اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/453225" target="_blank">📅 23:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453223">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار شدید در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/453223" target="_blank">📅 23:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453222">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
وزارت دفاع عربستان از تلاش چند پهپاد برای هدف‌قراردادن تأسیسات نفتی در منطقه شرقی این کشور خبر داد.
🔹
ریاض مدعی شده این حملات از خاک عراق انجام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/453222" target="_blank">📅 23:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=HBEfK6jtHNQPjX_HV3cYW9ZnhvOsaLL10sWE-mS1RnrLowM4nUGLP6oBKEXxQ4ifFZ7zhf62yfingqyaUgbhSBBZ1DPjswQUQ0Gc7Ho4hw8lVidHcwOFQd2fRHXpQE1rU4H0keMsvoH4INP-dko4bE2B6ml8SbgJ_BMQAqweua94PIpnG6GJUVZSDd7750yazrOy2UDZDMdPnNkUGJM_StHCrJMhhHEvLwaRDtErG96I1hq3YZUODnA5ewypAF5MwnBcpL_vqk6bIn922fcQWYvBGsJzl8vjl-QLeM868-LESUDjJhiFgDNOmjN16kEIpiwEQkozRU6It4-2jBEk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a65bea9d.mp4?token=HBEfK6jtHNQPjX_HV3cYW9ZnhvOsaLL10sWE-mS1RnrLowM4nUGLP6oBKEXxQ4ifFZ7zhf62yfingqyaUgbhSBBZ1DPjswQUQ0Gc7Ho4hw8lVidHcwOFQd2fRHXpQE1rU4H0keMsvoH4INP-dko4bE2B6ml8SbgJ_BMQAqweua94PIpnG6GJUVZSDd7750yazrOy2UDZDMdPnNkUGJM_StHCrJMhhHEvLwaRDtErG96I1hq3YZUODnA5ewypAF5MwnBcpL_vqk6bIn922fcQWYvBGsJzl8vjl-QLeM868-LESUDjJhiFgDNOmjN16kEIpiwEQkozRU6It4-2jBEk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید جواد نصرالله: آقا گفتند درجات سیدحسن هر روز در بهشت بالاتر میرود
🔸
مدتی پیش، وقتی برادرم سید مهدی خدمت آقا رسید و ایشان عمامه بر سرش گذاشتند، به او گفتند: من سید را فراموش نمی‌کنم و فراموشش نکرده‌ام؛ درجات سید هر روز در بهشت بالاتر می‌رود.  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/453221" target="_blank">📅 23:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453220">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7916efa9c9.mp4?token=CMunWSXWgcgzUZwIq0CieCMTN5ocuTLH5D6Ib7eCxpBITzwZgTxLa1j9UZSjIAE6XAZZJv8xEsNaKxE9FY4G-WLkxTfhtpNW0oN48yAcSy00pIDsfQymLE0AvJFQWOi5jdmpSoYU5dfPK4RJtzO_NWYXutWW5faP6ucHJlGx-qtzqHeCwK5LvHdCN2lvmE7aj9DyyjdRVhJXBY0an7p-s2FViz1gDeH_PDOsWcGLmV_HgHXElp3V12Tg7L1Mtg1DofHGbn_DyFLs-D4Kg89pG8aCrr6yR5rrw_rVuO4dD_J_dOc8YdisXRxMtpnDg0ZNPiSdnAKjl_MZMtx_mh4kJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7916efa9c9.mp4?token=CMunWSXWgcgzUZwIq0CieCMTN5ocuTLH5D6Ib7eCxpBITzwZgTxLa1j9UZSjIAE6XAZZJv8xEsNaKxE9FY4G-WLkxTfhtpNW0oN48yAcSy00pIDsfQymLE0AvJFQWOi5jdmpSoYU5dfPK4RJtzO_NWYXutWW5faP6ucHJlGx-qtzqHeCwK5LvHdCN2lvmE7aj9DyyjdRVhJXBY0an7p-s2FViz1gDeH_PDOsWcGLmV_HgHXElp3V12Tg7L1Mtg1DofHGbn_DyFLs-D4Kg89pG8aCrr6yR5rrw_rVuO4dD_J_dOc8YdisXRxMtpnDg0ZNPiSdnAKjl_MZMtx_mh4kJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله: ایران و حزب‌الله برادران واقعی هستند  @Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/453220" target="_blank">📅 22:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453219">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1de980eb3.mp4?token=ph9KYK7-4OPe1bV8G2WBqE-QdfC4XZQckqS-sjZ2cWdEi_1qv1eS0V6-w9bIOLRxVMJ1VfZ8hrevlqV2aBSARkZE87s2HUjANTW-bjzNKQUNhmCVw6CSgsuCgE8CAFJP-hn86nKWpb16DZRpiwZloD2OxstEUne4-M1DYDg6s1eit1V76hCFyc3YYpE72J3bVR6_mWoebVsAMeqKuekKTfw1FB9nYmkq0LFlv3ikmrQy6UyxVJlhPTK6QzhUGqvOgiprOVYqdNPqklM8-JRxtPKYLJETRryzW7n1PyVpl5k0DSNU9pQm5dD-AdQ-RpjZEcCWIzZCrBGFpfOK4w1pJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1de980eb3.mp4?token=ph9KYK7-4OPe1bV8G2WBqE-QdfC4XZQckqS-sjZ2cWdEi_1qv1eS0V6-w9bIOLRxVMJ1VfZ8hrevlqV2aBSARkZE87s2HUjANTW-bjzNKQUNhmCVw6CSgsuCgE8CAFJP-hn86nKWpb16DZRpiwZloD2OxstEUne4-M1DYDg6s1eit1V76hCFyc3YYpE72J3bVR6_mWoebVsAMeqKuekKTfw1FB9nYmkq0LFlv3ikmrQy6UyxVJlhPTK6QzhUGqvOgiprOVYqdNPqklM8-JRxtPKYLJETRryzW7n1PyVpl5k0DSNU9pQm5dD-AdQ-RpjZEcCWIzZCrBGFpfOK4w1pJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: بیش از ۲۰ هزار شخص حقیقی و حقوقی در مجموع دارای ۹۴ میلیارد یورو تعهدات ارزی رفع‌نشده هستند.  @Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/453219" target="_blank">📅 22:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd452d0f29.mp4?token=nD-rB-83IRYz59LLyStLSo9PSqOBIQ6z_2j9Y762k7yHbLDsIfFmZGoARFeHXMosjdk9PKANfyqs6irho2qtTypqF8tPucKkC5pK5yMafmM2bT3AQrYlcRdQBnaTKrJGCz3iLH4V58fQ72gI1XmOomCo7n17yAsBp2VYp9VVsy_UmCi1mOm3sAgYG3J5R5vmC-mJDTLnphO_13S8e0ds28cEUNabyjOYiN6QCvAac-ZBV5zhzLJJ91NbbyL_UZgq8PiDw6X4b8SbT26n97wvz90mCfJikUrY1mnFPCaLHmyCrPGo7XcarOENJ4V_NpTq_hOIzZJTKSbL9KbLVaMqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd452d0f29.mp4?token=nD-rB-83IRYz59LLyStLSo9PSqOBIQ6z_2j9Y762k7yHbLDsIfFmZGoARFeHXMosjdk9PKANfyqs6irho2qtTypqF8tPucKkC5pK5yMafmM2bT3AQrYlcRdQBnaTKrJGCz3iLH4V58fQ72gI1XmOomCo7n17yAsBp2VYp9VVsy_UmCi1mOm3sAgYG3J5R5vmC-mJDTLnphO_13S8e0ds28cEUNabyjOYiN6QCvAac-ZBV5zhzLJJ91NbbyL_UZgq8PiDw6X4b8SbT26n97wvz90mCfJikUrY1mnFPCaLHmyCrPGo7XcarOENJ4V_NpTq_hOIzZJTKSbL9KbLVaMqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله: شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔸
در بعضی کشورهای عربی مردم می‌گفتند ما را فریب دادند، چشممان را بستند و عمداً کاری کردند که رهبر شهید را نشناسیم. @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/453218" target="_blank">📅 22:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453217">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d17c0071b.mp4?token=QfdQd2_ftnGO0FieSoVyOGwCEPazfEWL6iNrv1x0XHMPXQZ7dziQ9fL0KOA2p6bB8DVDut_gEjOncl8T5DcezJjXkQ2YphlhaHaQPrxUrgkoUYiquVVJ--g0L7saWAE0I8cZ04PbcrXVZxwAqxykXaFOMAnwRxJQVwMWd-V1sOwyKsRBX53yeTnU7zouRLihMhtwbNyEWu39IFUD4a5J8YYBISZxFFpQjaRXY0ffSVeb4qVq9kfxo2RJLpdBB-ydvoiL4pBinzRz3-uBxT7GtR-fkSF-wJsbsZoxU9n1Q1AnvN7xAecyMNZ5ayXVHrtbI07p0JFYns4aFwPz8WJexkb-a-5vz92TgNBe0_DLZQ9krwIGWfgoXdGZKEoi9FtnSdwHHY6m8WX_-BIAfG34A8kT3LmtGBT1XBmDgwq7kpjqGZ3BRKaj__-OwgGaIWhBDH6Z5pjcnxHWhtrKjzmslLSotVN-wZ4aPBTWkKigBCJL4E3P_d_gb9CRWURShXF4j6tXq-8li2b15EIEbs9arBNPrfjhCV8hw7Er8Pi9dss60fBwq3xz8tD5fnvRNSKSnTaKPCC1Lv9togwjpBY0tgxX1K4mgzXg7XQ1n3P8Rm4X_kqNYmNgEHxOb5KP-WR0kIrBn-0yu1tBuXXRTt8Hju90AO9Zlp61wXqzO8q0NXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d17c0071b.mp4?token=QfdQd2_ftnGO0FieSoVyOGwCEPazfEWL6iNrv1x0XHMPXQZ7dziQ9fL0KOA2p6bB8DVDut_gEjOncl8T5DcezJjXkQ2YphlhaHaQPrxUrgkoUYiquVVJ--g0L7saWAE0I8cZ04PbcrXVZxwAqxykXaFOMAnwRxJQVwMWd-V1sOwyKsRBX53yeTnU7zouRLihMhtwbNyEWu39IFUD4a5J8YYBISZxFFpQjaRXY0ffSVeb4qVq9kfxo2RJLpdBB-ydvoiL4pBinzRz3-uBxT7GtR-fkSF-wJsbsZoxU9n1Q1AnvN7xAecyMNZ5ayXVHrtbI07p0JFYns4aFwPz8WJexkb-a-5vz92TgNBe0_DLZQ9krwIGWfgoXdGZKEoi9FtnSdwHHY6m8WX_-BIAfG34A8kT3LmtGBT1XBmDgwq7kpjqGZ3BRKaj__-OwgGaIWhBDH6Z5pjcnxHWhtrKjzmslLSotVN-wZ4aPBTWkKigBCJL4E3P_d_gb9CRWURShXF4j6tXq-8li2b15EIEbs9arBNPrfjhCV8hw7Er8Pi9dss60fBwq3xz8tD5fnvRNSKSnTaKPCC1Lv9togwjpBY0tgxX1K4mgzXg7XQ1n3P8Rm4X_kqNYmNgEHxOb5KP-WR0kIrBn-0yu1tBuXXRTt8Hju90AO9Zlp61wXqzO8q0NXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌‌وهوای اربعین در عمود اول
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/453217" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453216">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار شدید در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/453216" target="_blank">📅 22:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCe3B6ObFCP_H-IpJ5tru3L3l0-OIHoRcRMzF622RFhdozsKlVFykhSdXVz25DZ-jWRkvdlkmoVzo3ZK-Dj8uXTMj4lb0SS5IL4edM-krFCCUbnIwhbxnoWcgFSolkyL21tn3z3Capm7Ws-K0F7dbY-5xCpE5IWzFLSZaWmdHs35h5ZmE9gh8Hj-HdKkmR0Tz9zC57JmohRIzyNgrun9hlCgnQPtLH2oJ3bkRQayPWtyO8-j2uME9iAHCk_MBy7IyqywBr3K85PbE22ayoSgvUiMYArxRwHyWhWf297l6Bpy-JUQSxB24t0TBhL6xbh1OLxueDZhshUM2yv_Kwtkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراینی‌ها از ترس پاسخ ایران با عراقچی تماس گرفتند
🔹
وزیر خارجۀ اوکراین: با همتای ایرانی‌ام تماس گرفتم و گفتم هدف ما دفاع از کشورمان در برابر تجاوز روسیه بود و ما قصد هدف‌قراردادن کشتی‌های غیرنظامی را نداشتیم.
🔹
هدف ما، اجتناب از هرگونه تشدید تنش است. @Fasrna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/453215" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار شدید در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/453214" target="_blank">📅 22:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66680978e.mp4?token=ScjTp0KUUNbsckTqmAWjyvieop5arb6XdGT-1RAcqqhtD035EovNlKXcQP5xEFpDiKzO_Np97TFViVwQf5PcRqhI00wsY4ECJDBQaST6_PY-vLyc-YznGS4Qm4S1CHrrcspbxZcpwOF2-ib-h5ZcVG7lp1i7AiV0LXuusB0nA3V8BiaEwj8TiUbhiujpZAC6agcJkkxACAwNC1lZsuK-OyV3mS3cEF8IQAkbaeG4DgV1rzBfYxNGLi6aIRMs-Xht34sboT_2pWS5fm2Fxw_px3Uibyn2H8AF57pN-n1HAi559TTAnSZm3M4RolSqGWBx0tSMGxt8tkNcEKUaLO5vAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66680978e.mp4?token=ScjTp0KUUNbsckTqmAWjyvieop5arb6XdGT-1RAcqqhtD035EovNlKXcQP5xEFpDiKzO_Np97TFViVwQf5PcRqhI00wsY4ECJDBQaST6_PY-vLyc-YznGS4Qm4S1CHrrcspbxZcpwOF2-ib-h5ZcVG7lp1i7AiV0LXuusB0nA3V8BiaEwj8TiUbhiujpZAC6agcJkkxACAwNC1lZsuK-OyV3mS3cEF8IQAkbaeG4DgV1rzBfYxNGLi6aIRMs-Xht34sboT_2pWS5fm2Fxw_px3Uibyn2H8AF57pN-n1HAi559TTAnSZm3M4RolSqGWBx0tSMGxt8tkNcEKUaLO5vAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این تصاویر اربعین امسال را متفاوت کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/453213" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0254679eb1.mp4?token=lKCZn3kytRziFpyKyKr8VI13uGppjc7w3D2KWAmO7BMngwhyiF_iMlWLKy5oHLkX-YTKIePCQtrJrNECaM-ElhxYvKxQnCcvXIoortSdcyFJ51XjFso-_CZDoDjn_p5WWEQwweeVc9pAJ-ikWTEukti9pe81c_1Nk_xR4VUAEMnyU5M5xyGj2NWLDbWHqqwFx8ZW0FSZHvJM9KBm2El-8fCNyo5ud2pytXg79cjqU6p5e5V9MdG0kp2J-RgRj4JoEok_PBDIcSuK1Zj0mX8lwFzrBjKkh7K7kzGHc7TvVHOb_E7Js-nALdgTMlq0TlYhW3E7B8KQr6hlBXq0GCIg3VWZ3SlUr2oJqUdtdXY1JO_O87YSR37aUqBkTfHpLeLTd_vN69k9FLQ61KXrge0ee1o0zDBRhnRi2wZJx4KIuaS274jsibXQKp1hhMaS0jopelzIJvIzMF1MpK9s5GQ2NOSNPelG2NLUBqZkX1KeX_x8dT9SXd5tZZ_QRaTP64pqpgXh7gJuRWM4QOWk24kt7inSKaxhAbuYAZ8OXWBIAPABe6iiLWFl28SHuEh1gtkICheW22lJjdflEH-7qIX7Cwu3jjmpatpTLamm01DOp0r4d4GPIfERri3yWTtDFk3iaCtxs-3N6xj-eCwjH1NPKjw03sdW9trx2Q7R8faCgQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0254679eb1.mp4?token=lKCZn3kytRziFpyKyKr8VI13uGppjc7w3D2KWAmO7BMngwhyiF_iMlWLKy5oHLkX-YTKIePCQtrJrNECaM-ElhxYvKxQnCcvXIoortSdcyFJ51XjFso-_CZDoDjn_p5WWEQwweeVc9pAJ-ikWTEukti9pe81c_1Nk_xR4VUAEMnyU5M5xyGj2NWLDbWHqqwFx8ZW0FSZHvJM9KBm2El-8fCNyo5ud2pytXg79cjqU6p5e5V9MdG0kp2J-RgRj4JoEok_PBDIcSuK1Zj0mX8lwFzrBjKkh7K7kzGHc7TvVHOb_E7Js-nALdgTMlq0TlYhW3E7B8KQr6hlBXq0GCIg3VWZ3SlUr2oJqUdtdXY1JO_O87YSR37aUqBkTfHpLeLTd_vN69k9FLQ61KXrge0ee1o0zDBRhnRi2wZJx4KIuaS274jsibXQKp1hhMaS0jopelzIJvIzMF1MpK9s5GQ2NOSNPelG2NLUBqZkX1KeX_x8dT9SXd5tZZ_QRaTP64pqpgXh7gJuRWM4QOWk24kt7inSKaxhAbuYAZ8OXWBIAPABe6iiLWFl28SHuEh1gtkICheW22lJjdflEH-7qIX7Cwu3jjmpatpTLamm01DOp0r4d4GPIfERri3yWTtDFk3iaCtxs-3N6xj-eCwjH1NPKjw03sdW9trx2Q7R8faCgQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۵۰ مشهدی‌ها با رنگ‌وبوی اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/453212" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cce6c3ca2.mp4?token=JIBPNINeWCCoD0aD-fJCne4oidZtRm6XP9gxxbgGnzRkQjhX4FzR89J6RFm2beg7Wn3OPCkq_2yZOblx8BX8TOYueIs7I0esigug9ErylEGpe_idWBEvx8Cptel6PKRn-14LgkVI4mEBtpHUjhS-w-bmsSclutpg2Brqg_7khnJmVPh9qQTx_wNxqVoSSDoq99PvnuGr0rYtxoK7-h5yTzOdAgAHSmcf0eNAHdTIgr1fvJ7Q2YCIpZcbhVvZrGSnFA-Lo8sHFp-d3b6R33RbKOWTn4DghXvioYrhb4NCbYdNgX4TZmYH9yaqLb1b1Jh-i5UeA39aLWSsAFpArI-nkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cce6c3ca2.mp4?token=JIBPNINeWCCoD0aD-fJCne4oidZtRm6XP9gxxbgGnzRkQjhX4FzR89J6RFm2beg7Wn3OPCkq_2yZOblx8BX8TOYueIs7I0esigug9ErylEGpe_idWBEvx8Cptel6PKRn-14LgkVI4mEBtpHUjhS-w-bmsSclutpg2Brqg_7khnJmVPh9qQTx_wNxqVoSSDoq99PvnuGr0rYtxoK7-h5yTzOdAgAHSmcf0eNAHdTIgr1fvJ7Q2YCIpZcbhVvZrGSnFA-Lo8sHFp-d3b6R33RbKOWTn4DghXvioYrhb4NCbYdNgX4TZmYH9yaqLb1b1Jh-i5UeA39aLWSsAFpArI-nkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه عالم یه طرف حسینِ زهرا یه طرف
🔸
بانوای: محمدرضا طاهری و حسین طاهری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/453211" target="_blank">📅 22:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daba502cc7.mp4?token=XAb3DPB4WD8WMHSHYwAUStu5APDlb5Vj9F7QZTi5oNxK_UrrEZ87uRNZ_dGRWlyeYyJbvJesh0t_o3eUuWshvHO124cpabIpRXJ8BkQWw9z8C9HqTNY8JV7g5N3Zo2Xr_PAr5THRiizuFVxJTdkIba92zTCzpEsz5ABuuJLSTR5YHu2n-JoGHE3kxtnjMlKA_fZKBYuOF6jzH-9MO7hFK4rMkl0SdNOgIto1LRJ0vV4nbihq2D3S_2UXeIMrEsAgYAJIL02o_CWHZtgygqxCE3NB1v_kLozu_JuhjGWb-BBwjWPqB2tqGgiamwF5cEQtLtHhBHmgXD-XNFLWkpjbFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daba502cc7.mp4?token=XAb3DPB4WD8WMHSHYwAUStu5APDlb5Vj9F7QZTi5oNxK_UrrEZ87uRNZ_dGRWlyeYyJbvJesh0t_o3eUuWshvHO124cpabIpRXJ8BkQWw9z8C9HqTNY8JV7g5N3Zo2Xr_PAr5THRiizuFVxJTdkIba92zTCzpEsz5ABuuJLSTR5YHu2n-JoGHE3kxtnjMlKA_fZKBYuOF6jzH-9MO7hFK4rMkl0SdNOgIto1LRJ0vV4nbihq2D3S_2UXeIMrEsAgYAJIL02o_CWHZtgygqxCE3NB1v_kLozu_JuhjGWb-BBwjWPqB2tqGgiamwF5cEQtLtHhBHmgXD-XNFLWkpjbFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهتزاز پرچم خونخواهی در مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/453210" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453209">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUxxmtIc2ALRaLswKPeGqWzg_tYLhJ2074Fjfojq7U8WFLEZN_hEP7BAuwlNzbemQGqCLON3WCX3sFkxQRg2UC1J9ilTgOcz3S8a-aAJugr06IjKjnK2VD5bFC5argUg1svRQoab489goNG4O_IMCXQ7K8VhUe9VlyrB3CutrjIwZG9bkR849EzOL1iKVIdQkLH8DfqlF26D82Lyl-2YL4S1drejy7Jp2mj9v0WqtFq53aYrjRcWsSGKDeLhG_-_ePRHlNiVseQEng7LAJ1Oqlb7At5F8zop6oQNw59XcKiY-pXc7GraqjtyHNRQanu9ZUHPfOHAo43uGFH2KAvaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: آغاز جنگ دوباره صهیون‌ها مساوی با پایان ابدی‌شان است
🔹
معاون اول رئیس‌جمهور: دولت برای همه سناریوهای پیش‌رو برنامه‌ریزی کرده و خود را برای بدترین شرایط نیز آماده کرده است؛ اگر رژیم صهیونیستی بار دیگر جنگی را آغاز کند، پرونده‌اش را برای ابد می‌بندیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/453209" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453208">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60417435.mp4?token=NE18UxAK8oHO1-ahqIoS0ftQFRjIzohifu22m6g7JrWMtfp9rG3WEMNzkSbA6YkQ6sLfuuprUYrm3QVW3YIL5VBmx708FLgyU08NV8VBOrQIP4vD4w7G5Y-f4gqNciyAn6HndxZ89xoO3IRhPjxtlAggFke1aRa9okr_j1glSUwbzxEuK9iDjdTU3NOq0k_Rgslx1ILJBa0Kg3TWh3Q-6gNApMHO5arSM9LqNo_58sJk64Wy26K-J4JO_3xgs7NG0Rb7Rx_HPQ8RgNy_LuUU_gIJehvlw4DP0hn-JWXkWjFvjfuNHzvBNsQ_i2WSmqyOqj-Fw5-oBwQ8tpzPz4xq0YYAXwa_NL8VF0qM9TJQcddMumYqqOq1VTkqIEM6WQShNwDGflHIaqdMg2wXwNwodwCBQhXL1ydfdqz02u0umApYE1OQYW9bex1QsNJ4FeOsK0h0NX7TGu43nN58bCx-ZbSkBHTkCC1INn7Cee-tFoeNucJGlzD52ZSSeEy4xErY8xRk4Xmc5cyheezECLTSeYjXn0xDuYtWoo2oapyO6Y0Qgldrh9P8SNA-ShavjnXUTvA5Nkfqqs1-Osra-Am1jQnpafuugiVTVaGRktYOB-1wYwd_o-Haq7_UXNyMGfH-6fCN0VALeCqkQfpQhGjPkMwfJSeXdMH9rMHk0-dkA94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60417435.mp4?token=NE18UxAK8oHO1-ahqIoS0ftQFRjIzohifu22m6g7JrWMtfp9rG3WEMNzkSbA6YkQ6sLfuuprUYrm3QVW3YIL5VBmx708FLgyU08NV8VBOrQIP4vD4w7G5Y-f4gqNciyAn6HndxZ89xoO3IRhPjxtlAggFke1aRa9okr_j1glSUwbzxEuK9iDjdTU3NOq0k_Rgslx1ILJBa0Kg3TWh3Q-6gNApMHO5arSM9LqNo_58sJk64Wy26K-J4JO_3xgs7NG0Rb7Rx_HPQ8RgNy_LuUU_gIJehvlw4DP0hn-JWXkWjFvjfuNHzvBNsQ_i2WSmqyOqj-Fw5-oBwQ8tpzPz4xq0YYAXwa_NL8VF0qM9TJQcddMumYqqOq1VTkqIEM6WQShNwDGflHIaqdMg2wXwNwodwCBQhXL1ydfdqz02u0umApYE1OQYW9bex1QsNJ4FeOsK0h0NX7TGu43nN58bCx-ZbSkBHTkCC1INn7Cee-tFoeNucJGlzD52ZSSeEy4xErY8xRk4Xmc5cyheezECLTSeYjXn0xDuYtWoo2oapyO6Y0Qgldrh9P8SNA-ShavjnXUTvA5Nkfqqs1-Osra-Am1jQnpafuugiVTVaGRktYOB-1wYwd_o-Haq7_UXNyMGfH-6fCN0VALeCqkQfpQhGjPkMwfJSeXdMH9rMHk0-dkA94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شب اول تا شب ۱۵۰؛ حماسهٔ مردم ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/453208" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453207">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e9ca0b44.mp4?token=kZkyn3fpBZ35SWnQcWyqJK8fvpzCFOFZAoMGEE5Df37pRATaB560SiXZH1BORH3M3oEjlgg7b5vKCKOAKEn4QkA0JgeR3NQD-Of21eec2J9djNTrhjdOrIbqIig1w0CzkYc_dhmS6iVaMyumpZlrKLofeHlyay7rRNu95-qBimLOOHWwmLXYjo3PFQTytLOYTPRJHXzYz4Y0ND3IFRn8UAJO8mfUN4KdRpv105JJbOrsqqhg_zMM8s9pc6D6gPGcviXjTlP6dzn3hPY7NSgD9qdzpJT1m_h7jeO5zUsbpr5XsGjfJGs2r9WndgTo1kS1GcvqbWTMx3K8BOKLYiMJ5xgN9dIwXGrS5i9vFPH1VYlajaCoY1bXw_hZXUSCcVVRtbi4gO9I8TDOXQGKf4DL9_rjsQUVg3LIeNRLRP2LyHq6NBU5oGU3aHvDcwEiGPf0qEvObAkCfl_oDrW1bYNw1r6y5hScz2LTVMAJXbSaZHprIApKDR9oSpHJKLIxH-N4xHygB-t0ZjENXia9x0Ie3vRuFkDIwRUmiUgWSZE40LIx3shGaxAjWt2f22xYA4NO0CvEPmnsNiPG1ETJ-QnpPo2iqnJwdIVTSNjgaxchNK424S1TRY8ZcPZuoypbYphPwgH2fUARW77FMU4No0lJ4eSLXqZLNJpk88n_R2rwqG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e9ca0b44.mp4?token=kZkyn3fpBZ35SWnQcWyqJK8fvpzCFOFZAoMGEE5Df37pRATaB560SiXZH1BORH3M3oEjlgg7b5vKCKOAKEn4QkA0JgeR3NQD-Of21eec2J9djNTrhjdOrIbqIig1w0CzkYc_dhmS6iVaMyumpZlrKLofeHlyay7rRNu95-qBimLOOHWwmLXYjo3PFQTytLOYTPRJHXzYz4Y0ND3IFRn8UAJO8mfUN4KdRpv105JJbOrsqqhg_zMM8s9pc6D6gPGcviXjTlP6dzn3hPY7NSgD9qdzpJT1m_h7jeO5zUsbpr5XsGjfJGs2r9WndgTo1kS1GcvqbWTMx3K8BOKLYiMJ5xgN9dIwXGrS5i9vFPH1VYlajaCoY1bXw_hZXUSCcVVRtbi4gO9I8TDOXQGKf4DL9_rjsQUVg3LIeNRLRP2LyHq6NBU5oGU3aHvDcwEiGPf0qEvObAkCfl_oDrW1bYNw1r6y5hScz2LTVMAJXbSaZHprIApKDR9oSpHJKLIxH-N4xHygB-t0ZjENXia9x0Ie3vRuFkDIwRUmiUgWSZE40LIx3shGaxAjWt2f22xYA4NO0CvEPmnsNiPG1ETJ-QnpPo2iqnJwdIVTSNjgaxchNK424S1TRY8ZcPZuoypbYphPwgH2fUARW77FMU4No0lJ4eSLXqZLNJpk88n_R2rwqG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر وقت دلت برای سیدالشهدا(ع) تنگ شد این کار را بکن
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/453207" target="_blank">📅 22:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgBeBDnatWAhla_U11jYgRDmXIXOBaAIZvPSZmShu9lLvVThz-W7r8T0fGhwCvjTpb5n20jlxYK1l_hOH_tRh13lExemZb5uv31eKRJYq0KFn2JGN-1MVLsfQs8E5Y4zi3iT62wsdORUTe3ehwifD4Tkh-W8RTqVddfVmBmBF6esnQUQOaOkwE6XpIjMnUPKudzbD7HMp_jzL6nLMclcn_1cwkX4JIsC0DUcxHdpnZljrotUfsvOv-ZA-0i2nWl5t9nQBZcH56D_1SOpnUg0RMindisDziVPIBmlbuVvoDj0zyt8dQ26U64HYJuB5bzeNNBZg3mTGTd4J6Dm1IoLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدارهای محرمانۀ اسرائیل و امارات علیه ایران
🔹
شبکه ۱۲ اسرائیل: مقامات اسرائیلی و اماراتی با هدف هماهنگی مواضع علیه ایران و بررسی گام‌های مشترک در محافل بین‌المللی، طی هفته‌های اخیر چندین دیدار محرمانه را در یک کشور ثالث که نام آن اجازه‌ی انتشار نیافته برگزار کرد‌ه‌اند.
🔹
دو طرف، ابتکارهایی را برای هماهنگی اقدامات علیه ایران در چارچوب‌ها و مجامع بین‌المللی بررسی کردند؛ با این حال توافق کردند که هیچ‌ یک از این اقدامات، جز با هماهنگی قبلی با دولت ترامپ اجرا نشود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/453206" target="_blank">📅 21:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09083fd9a1.mp4?token=rMmetnFahFvKXpgyzV5_RS9_57RSvfIQPWCGtpjCQ0DTsce8k8H48koDlh1lgjprykPM4zvF_EqihsgQ2un-JQ76ES4JmscMQSdL35wM9LwHEbOtCCKRJJqvEK8ilY_5xShRoC6qiI1-sp0V6nPYkVQrgCeEybmavaEpXcCFmf0Vs77lYw_Sgq3XHk1GaOpAibMxVNt-2n2nUxByTG5bIxP9pSzowfdFthNPTro2QrpRfn9jGwxBYkfBQAS8kHemAeiAxjZ7GIGtX6G5iIszoYkr73ExG0HMbM32G4MXDU_YDN9ymAzOI0hyIGpJXr7tetumCQ8e9PZejHcHxJwXAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09083fd9a1.mp4?token=rMmetnFahFvKXpgyzV5_RS9_57RSvfIQPWCGtpjCQ0DTsce8k8H48koDlh1lgjprykPM4zvF_EqihsgQ2un-JQ76ES4JmscMQSdL35wM9LwHEbOtCCKRJJqvEK8ilY_5xShRoC6qiI1-sp0V6nPYkVQrgCeEybmavaEpXcCFmf0Vs77lYw_Sgq3XHk1GaOpAibMxVNt-2n2nUxByTG5bIxP9pSzowfdFthNPTro2QrpRfn9jGwxBYkfBQAS8kHemAeiAxjZ7GIGtX6G5iIszoYkr73ExG0HMbM32G4MXDU_YDN9ymAzOI0hyIGpJXr7tetumCQ8e9PZejHcHxJwXAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: نباید ورود به حریم خصوصی افراد و میزان استفاده از آن در ذهن ما به امری عادی تبدیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/453205" target="_blank">📅 21:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b058b1904f.mp4?token=pOV1h9pD6pdjnk1LIDm96fQ_xFoU6wA68Z_IKzua3vfLXxsDfVu6I6cx-x3Fw1KQms4FnbkwyUZFSzgHehAdTZ_RcqTE6uAHyU8aliqmr2Kjkj2IJJBQ1t1sSuatFd5OJX8EezD2epgqjSRvjZQ7EkvZkKRxn_IMdeKnkoA4A4R0VpoFjUQAimLbqdufxxhAAoFEjneoUYg_9gchCyTP5S6Od6lDFL09Jd_tlXN_b1AorwfpM6sNrtjcHX_wqvgJgdiFltFZ2kzonUVI7iMhnUFDDPi7C2HFq22XWJd4QE_khPPmzp_MkPzbAszzJqJJ1NZEOLf1m4uMVLuBI8_mawxkqwHxGzCKMPfgucakSQRWV39SAH9mfC2ocXWCg8bSOot8qp_1WUJ5oKrAu6gwi3htfX09pZfEUmAs9aoL1vghyuW4yGvv3D3dJxgbt3A8oHRlVN9Wg8cfX72AZ9IOgh8JOvmBWEKits563V3gPEt31osCB228TBajlCn3mP2eL6_OOUwPmNwD6FmXJAjBaG8CtpP5iTRW5Gx3HOWGViJUwa-Ri58FkUPkvPJsB3iIVAy8k3AggbRNH4udoHi4IBTUtRJGUGnmh1EFEFiqL3pxcznvWMaWBtoxf38W0BOwkTTzlGg9A-eWaSCnZv8R2K16ukF7gn_6mfAdBpQWazY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b058b1904f.mp4?token=pOV1h9pD6pdjnk1LIDm96fQ_xFoU6wA68Z_IKzua3vfLXxsDfVu6I6cx-x3Fw1KQms4FnbkwyUZFSzgHehAdTZ_RcqTE6uAHyU8aliqmr2Kjkj2IJJBQ1t1sSuatFd5OJX8EezD2epgqjSRvjZQ7EkvZkKRxn_IMdeKnkoA4A4R0VpoFjUQAimLbqdufxxhAAoFEjneoUYg_9gchCyTP5S6Od6lDFL09Jd_tlXN_b1AorwfpM6sNrtjcHX_wqvgJgdiFltFZ2kzonUVI7iMhnUFDDPi7C2HFq22XWJd4QE_khPPmzp_MkPzbAszzJqJJ1NZEOLf1m4uMVLuBI8_mawxkqwHxGzCKMPfgucakSQRWV39SAH9mfC2ocXWCg8bSOot8qp_1WUJ5oKrAu6gwi3htfX09pZfEUmAs9aoL1vghyuW4yGvv3D3dJxgbt3A8oHRlVN9Wg8cfX72AZ9IOgh8JOvmBWEKits563V3gPEt31osCB228TBajlCn3mP2eL6_OOUwPmNwD6FmXJAjBaG8CtpP5iTRW5Gx3HOWGViJUwa-Ri58FkUPkvPJsB3iIVAy8k3AggbRNH4udoHi4IBTUtRJGUGnmh1EFEFiqL3pxcznvWMaWBtoxf38W0BOwkTTzlGg9A-eWaSCnZv8R2K16ukF7gn_6mfAdBpQWazY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک عراقی از بدرقهٔ تاریخی امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/453204" target="_blank">📅 21:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">نماینده مجلس: رئیس دانشگاه امیرکبیر در شرایط کنونی به کانادا سفر کرده‌ است
🔹
علیرضا عباسی نماینده مجلس: در وضعیت فعلی، با توجه به اتفاقات و ناآرامی‌های گذشته، لازم است پرونده دانشجویانی که در اغتشاشات حضور و نقش داشتند، در کمیته‌های انضباطی با دقت و سرعت بیشتری مورد رسیدگی قرار گیرد.
🔹
در چنین شرایطی، حتی شنیده شده رئیس دانشگاه صنعتی امیرکبیر مدتی است در کشور کانادا، کشوری که رویکرد خصمانه نسبت به ایران دارد به سر می‌برد؛ موضوعی که با مسئولیت‌های مدیریتی این دانشگاه همخوانی ندارد.
🔹
امروز دولت و کشور به دانشگاه‌هایی فعال و اثرگذار نیاز دارند تا در حل مشکلات و ارائه راهکارهای علمی نقش‌آفرینی کنند.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/453203" target="_blank">📅 21:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453202">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpaw04f3hBagBnsd1F_c4L7ev6o0QeCbTTlYm0BiDP21hPk7dHxIj4-ekIE6gvffuhLRxGVz5zGUfETONcy0IT_ReWIr-dmLWMtlXhNqeegoA2-4tvQNwmqkkOSjhfhV_K6-ltfSvamnyqo4WuD1aNRnrhrhlvM5fAZhlwSaxx_muDKORTX9UicFdiqtbGAbr20olrqrHPAfex6jleJN-v26V01ZGsPlTo04HpLX53eANUM84yJ9QQIpRX-k09nmKE9JEd0-40_2T6Ed2OSke1Y0Gc3WglnGfOggIc0PFq2vVWgfxIjo9LJDC19tEEfgasjjhjwXimKHyE6wzj8Xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هیوا» پنهانی از طبیعت زنده‌گیری و به مرکز تکثیر در اسارت منتقل شد
🔹
منابع خبری به فارس اعلام کرده‌اند که به‌تازگی معلوم شده یوزپلنگ نر جوانی به نام «هیوا» اواخر سال گذشته از طبیعت زنده‌گیری و در اوج فصل تولیدمثل یوزها، به سایت تکثیر در اسارت منتقل شده و به مدت ۱۵ روز در اسارت بوده است.
🔹
ظاهرا «هیوا» حدود ۱۵ روز در این مرکز نگهداری شده است؛ درحالی‌که به‌گفتۀ مدیرکلمحیط‌زیست سمنان، انتقال یوزهای آسیایی از طبیعت باید تنها پس از بررسی‌های تخصصی و تصویب در کمیتۀ ملی یوز انجام شود.
🔹
پیش‌تر محمدعلی یکتانیک، کارشناس محیط‌زیست گفته بود که زنده‌گیری یوزها از طبیعت، تفاوت چندانی با شکار آن‌ها ندارد.
🔹
اکنون در مرکز تکثیر در اسارت، ۵ یوز ماده و تنها یک یوز نر به نام «فیروز» نگهداری می‌شوند و مدیرکل حفاظت محیط‌زیست سمنان حضور یک یوز نر جوان را برای برنامه‌های تکثیر ضروری می‌دانند.
🔹
یوز آسیایی تنها در ایران زیست می‌کند و طبق آخرین آمار، تنها ۲۷ یوز در طبیعت کشور شناسایی شده‌اند.
🔹
برخی کارشناسان نیز معتقدند حفاظت از زیستگاه‌ها، راهکار مؤثرتری نسبت به زنده‌گیری و تکثیر در اسارت برای حفظ این گونه ارزشمند است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/453202" target="_blank">📅 21:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453201">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74ef6bda81.mp4?token=PZE7IKwy0fNYTk0VBHBR63ctuQ-5xD7LIwmxTcP1vPLRIkCGf0CYuraC_Bhbc5zUWhHD_eijeDUzfk8pxl4C9EKAuiEDm912tnU-U3BHoHSo6wHXcNsyOAxtcD76iPDL_gq9zpbVMmxHBXTcRWFRjQcQfZ_Hu2emkB2tDJG_7oDggjlx3WGSloHW29tP2wXEHOZZXjFLgu-hV_ndJPARNGFsFXPp9kQqyxzBvwePHfu2oIgvNIgqmzHrAmUvMXDslJ7eVDd_dOsSufglHc1oZj56S2JlrBB0j8uR7RWUifYGbE5dEUNkaNPdcmJ0PgI6OqxrESlVULIu8H-IcvxJNIW4OTtwR1lC6LCDuI6yAeAEmVHphGuUME4QAFi6aSCxqWfgKyDGOzglZvTEHmzef9DNzp6Tm-ty3RnCz1eO4QW4I4hN4W_mbz4AYha0ieT9-O3RtdzkEaVqn6i_oZlny3fF0VO2hJrd3za3LAt2rWEemv8YIyHmFTFcaQXcBbPwOYoKfalJGyC6PrmGZQmXGvJ7IKBNY7YVf2hb8uMpY55t9DBPTWpzVPr04Oo2AJgmDDdcSqbPEJGFPMv3JgUU92TnTHlNKYtlUV5BO9Gl4Gxg0gO4t4jqtD4X9xtMKjY3P7HLhZnXSM0J9eNQINClrCG1MSe0KjKpBVrDVqloKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74ef6bda81.mp4?token=PZE7IKwy0fNYTk0VBHBR63ctuQ-5xD7LIwmxTcP1vPLRIkCGf0CYuraC_Bhbc5zUWhHD_eijeDUzfk8pxl4C9EKAuiEDm912tnU-U3BHoHSo6wHXcNsyOAxtcD76iPDL_gq9zpbVMmxHBXTcRWFRjQcQfZ_Hu2emkB2tDJG_7oDggjlx3WGSloHW29tP2wXEHOZZXjFLgu-hV_ndJPARNGFsFXPp9kQqyxzBvwePHfu2oIgvNIgqmzHrAmUvMXDslJ7eVDd_dOsSufglHc1oZj56S2JlrBB0j8uR7RWUifYGbE5dEUNkaNPdcmJ0PgI6OqxrESlVULIu8H-IcvxJNIW4OTtwR1lC6LCDuI6yAeAEmVHphGuUME4QAFi6aSCxqWfgKyDGOzglZvTEHmzef9DNzp6Tm-ty3RnCz1eO4QW4I4hN4W_mbz4AYha0ieT9-O3RtdzkEaVqn6i_oZlny3fF0VO2hJrd3za3LAt2rWEemv8YIyHmFTFcaQXcBbPwOYoKfalJGyC6PrmGZQmXGvJ7IKBNY7YVf2hb8uMpY55t9DBPTWpzVPr04Oo2AJgmDDdcSqbPEJGFPMv3JgUU92TnTHlNKYtlUV5BO9Gl4Gxg0gO4t4jqtD4X9xtMKjY3P7HLhZnXSM0J9eNQINClrCG1MSe0KjKpBVrDVqloKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای فعلی مرز مهران در فاصلۀ ۷ روز تا اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/453201" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e1b3504b.mp4?token=aBU437GwYJhIbOYZdaDCjYjlnlsg4XUpup0Ofz7NCwr9QcD6TCF9lKhsrdeDlAPb45CplzyjcNxoohHbb8qYXefcpwT1NTPwhbFhZRdtB3rXbiCLhp8P97E5dx-eDsPOVfR2v0WrUD2Z_XllphI9yKhW-3scasgrBHtHcrt9JKlmKEbvzVnghr_ut_HGNlEgxzkbmaXnN7RGAE2ffD1c2o5MEwydxDc54XxXgWtDvvD6yN7l0pMNFDDV2F0TemQ_X_l3jVAPf_xshZCCiFKtvSp934AClclN8deOyWMw7YN24AZAd3c71Oh-ami6hha2id0ANvdZT1OHug50IN3YQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e1b3504b.mp4?token=aBU437GwYJhIbOYZdaDCjYjlnlsg4XUpup0Ofz7NCwr9QcD6TCF9lKhsrdeDlAPb45CplzyjcNxoohHbb8qYXefcpwT1NTPwhbFhZRdtB3rXbiCLhp8P97E5dx-eDsPOVfR2v0WrUD2Z_XllphI9yKhW-3scasgrBHtHcrt9JKlmKEbvzVnghr_ut_HGNlEgxzkbmaXnN7RGAE2ffD1c2o5MEwydxDc54XxXgWtDvvD6yN7l0pMNFDDV2F0TemQ_X_l3jVAPf_xshZCCiFKtvSp934AClclN8deOyWMw7YN24AZAd3c71Oh-ami6hha2id0ANvdZT1OHug50IN3YQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: اینکه بگویند که از NPT خارج شویم و بگوییم دنبال سلاح هسته‌ای نیستیم، کجایش بازدارندگی دارد؟
🔹
باید این بحث در داخل کشور باز شود که ما تا کِی می‌توانیم تعهدات NPT را اجرا کنیم.
🔹
باید ابعاد شرعی و فقهی و راهبردی موضوع بررسی و بحث باز شود. @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/453200" target="_blank">📅 21:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afac18e21.mp4?token=YD_nfu9CjeqanWrsTwZWdoyfaTZ1d2lV48ILVf7wujDAqllNeBvqNxF13aV2B8feIW3ZZZGxeSPK4kMqsn7PCUwBeRNfLPGR13uHZGrBFYQZnmZy5IZ3HFaOX85whEIkSwUw6P2kPfUDwD4taq2Xj_7W2xOscIOJWSkIW9U7XtbgtflmGSYXq-drg8hCg4OgH8GRUUS1nh66yiG8qaO2o7X8SIvoV-DGwGEU5ljWJXRsd2il2HtQG_Sh9YDTPjg7GRSSvsRtBhNrP61pq21wo96jLG8shtzYY2HtaDCU_z_fRU2t0h7snyCvN5Ld8oaWLXsfRrGkvIZB9f1u7xyonA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afac18e21.mp4?token=YD_nfu9CjeqanWrsTwZWdoyfaTZ1d2lV48ILVf7wujDAqllNeBvqNxF13aV2B8feIW3ZZZGxeSPK4kMqsn7PCUwBeRNfLPGR13uHZGrBFYQZnmZy5IZ3HFaOX85whEIkSwUw6P2kPfUDwD4taq2Xj_7W2xOscIOJWSkIW9U7XtbgtflmGSYXq-drg8hCg4OgH8GRUUS1nh66yiG8qaO2o7X8SIvoV-DGwGEU5ljWJXRsd2il2HtQG_Sh9YDTPjg7GRSSvsRtBhNrP61pq21wo96jLG8shtzYY2HtaDCU_z_fRU2t0h7snyCvN5Ld8oaWLXsfRrGkvIZB9f1u7xyonA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: طرف مقابل فکرنکند که ایران مادام‌العمر عضو NPT خواهد ماند؛ همۀ گزینه‌ها روی میز است
🔹
ما با بحث دربارۀ خروج از NPT مخالفتی نداریم. جنگ و زدن تاسیسات هسته‌ای کشور فرصت مناسبی برای بررسی موضوع داده است. @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/453199" target="_blank">📅 21:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453198">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e55aee2cd.mp4?token=DpNlle55RjBCDv_ttFqzQsqL3ZxyfdymtJFpndIrD_T1IR2_axzV7G066PBaXAimgdM422pIp9qIBPnjdutrHxr_lZYmhDZVnUyPVAwc_SaO_V_DkCT77mbedKMHfLUxoWJTUU8VG18OO7avTGMM4hPu4oXNkN7OXR3plmjSGNkATiTzEWN7fU6IxHX9eUHm0J-tG9ZLi-RfS9h5kriO8BlQFeOhSBlXHluXjNhSlsmIbSPnq6ITIfPR9UQRztTQB6TzLg4KK4d_SoM4B9JYeg7xKjp4czKc48vTHveh4TNw0PyMloQrdvLVIFbogMltU2KnKdUrYqyoYmNtQmBLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e55aee2cd.mp4?token=DpNlle55RjBCDv_ttFqzQsqL3ZxyfdymtJFpndIrD_T1IR2_axzV7G066PBaXAimgdM422pIp9qIBPnjdutrHxr_lZYmhDZVnUyPVAwc_SaO_V_DkCT77mbedKMHfLUxoWJTUU8VG18OO7avTGMM4hPu4oXNkN7OXR3plmjSGNkATiTzEWN7fU6IxHX9eUHm0J-tG9ZLi-RfS9h5kriO8BlQFeOhSBlXHluXjNhSlsmIbSPnq6ITIfPR9UQRztTQB6TzLg4KK4d_SoM4B9JYeg7xKjp4czKc48vTHveh4TNw0PyMloQrdvLVIFbogMltU2KnKdUrYqyoYmNtQmBLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: در حال حاضر وضعیت ما مثل کشوری است که عضو NPT نیست
🔹
هیچ بازرسی از آژانس در ایران وجود ندارد و هیچ اظهارنامه‌ای نمی‌دهیم و تمام دسترسی‌های آژانس قطع شده است. @Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/453198" target="_blank">📅 21:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453197">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5f2adbcb.mp4?token=k0NztmydenwEKG7U0F8dFMU1ZmRzLnvgrAzTv39xz29WsH7M8q5850U_5cp3JXC37PqmnEDby5NH-dOtAIc65C_a3lI5b7VnCfV3gL35c1ccqN9X6DYt4PMrjvmYxgd5n5sb0SMwOW81Inm_fD_sThIXupgM_Z-2pjQUicZ6-F9rGD5XO-Oes0iiQFbAxJWe51A8dBJ9AI58xVEndI76lIe7hh55sSYWvJQT8FQRNHfuqu_ggdL9jCPpkaF-58-FVBdCSXYKkP4KnjJiMcUAhvpqLgQTOPox5ZWLT9sUs2AAB75u52hSCN0ohRcocRtScYUpvhJQXmtzQYea8wNvrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5f2adbcb.mp4?token=k0NztmydenwEKG7U0F8dFMU1ZmRzLnvgrAzTv39xz29WsH7M8q5850U_5cp3JXC37PqmnEDby5NH-dOtAIc65C_a3lI5b7VnCfV3gL35c1ccqN9X6DYt4PMrjvmYxgd5n5sb0SMwOW81Inm_fD_sThIXupgM_Z-2pjQUicZ6-F9rGD5XO-Oes0iiQFbAxJWe51A8dBJ9AI58xVEndI76lIe7hh55sSYWvJQT8FQRNHfuqu_ggdL9jCPpkaF-58-FVBdCSXYKkP4KnjJiMcUAhvpqLgQTOPox5ZWLT9sUs2AAB75u52hSCN0ohRcocRtScYUpvhJQXmtzQYea8wNvrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌کاران حادثۀ تروریستی دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان اعدام شدند
🔹
دقایقی پیش حکم اعدام «ابوالفضل سپاهی بادجانی» و «امیرحسین صفری حسین‌آبادی»، دوتن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه ۱۴۰۴ اجرا شد.  جرم مجرمان این پرونده چه بود؟…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/453197" target="_blank">📅 21:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453196">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4db5afa13.mp4?token=QjbbPmAaYpDUrQPH_Q88Vh4hqlsIVNZqjc_9xivFZ7nT55-N0qmF_XTiU2AgM0HSjUjWuFfbr4yt_z6AP615bN2N-_Yo0UJv3qhxEfjaYZl_bQR1DfIis_SlFkF078_G4Y051qCsVYNJMLzroX0QuMBfydj_DUkhC3_yUNpv4Z3xUz9xSOwITrDmy3f8pIa3kStsOrxXjoZsTWulmVj-ACycp8rUE_F2vvNcdcYCYJrO9aJaN52dQf9sNuhIWib0f2Z8TEDrNzolg5Ju6uVTQJ7T5_NM2XLhnfO1VbFEPzVVqLgLhZ_BF_FsxP_yA0Hb_p5gpTvYKvwzXb7F7YBXAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4db5afa13.mp4?token=QjbbPmAaYpDUrQPH_Q88Vh4hqlsIVNZqjc_9xivFZ7nT55-N0qmF_XTiU2AgM0HSjUjWuFfbr4yt_z6AP615bN2N-_Yo0UJv3qhxEfjaYZl_bQR1DfIis_SlFkF078_G4Y051qCsVYNJMLzroX0QuMBfydj_DUkhC3_yUNpv4Z3xUz9xSOwITrDmy3f8pIa3kStsOrxXjoZsTWulmVj-ACycp8rUE_F2vvNcdcYCYJrO9aJaN52dQf9sNuhIWib0f2Z8TEDrNzolg5Ju6uVTQJ7T5_NM2XLhnfO1VbFEPzVVqLgLhZ_BF_FsxP_yA0Hb_p5gpTvYKvwzXb7F7YBXAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: اگر با عمان به تفاهم نرسیم، مسیرمان در مورد تنگه را ادامه می‌دهیم
🔹
اگر به تفاهم برسیم هم بلافاصله تنگه باز نخواهد شد و در داخل کشور تصمیم گرفته می‌شود که چه خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/453196" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOLtJX5iOD7_ajGWpC5dFVjVdxyExSBcBe8-WOqpRTkVVMCarMtharKBXE01n7ufVLDKhRp-G9d34dU5VQ7KyxFjX11xlzwBRopiKIRzGRZLErVbtHIGyURPqEQBChx8SRWraHzsCCGPsQp1R5Lh1as16SpEQ-KjGZWYNjVgW4-mix56qiJmKlVb456onjLgh_Wuk3dyUq9zvDjX4rGLbhxS8EH-7gc9mLKyATw-QFmTJyDMRb21pO8uE4u0-HZ4340Qcn39Jx8aPgHZHBpRRULzC3rQAPZBjK3nre0EAS3vJDv1KyjvlaPMmqjXB4nS-ycy_zYQ_I28QzzUeFSn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pamsv-UaP5Efgm5D6_z8bu1PMOaROe-CgszwesSDd0Vl03WBFVa5q7VXqhsTjptfZfbj10jQNvUycOuRXM4iI80gG0H20vS0-XCz9tkq0ooy5t-iAqeAqlMQbn6fY0hJEzgPjV3FLC1P3u30Oy5Zqq2D7N2Ei3idLDoWDdCCZT2EzBrfdSbcw4DP8xshc8oa_guw938MmeXWjMCHWwBQyq1UEn2X_YurI1SM4g9VQw5feBnYXtv1qH1-eI0nluMltJVlxiG7_YdYMeHeVLvIkzh_Ygqrlqf9ckT3osKkrtCl98DvSD3qTdF9COaCGsN4Z14kzejeY815crboiCsNPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccb1dc3.mp4?token=Qo-qr6-o3HXbWC3Icwdz9VXnkyd8O8n0QVtm5JCd-U7eYaFEzcAAgguSBFpqghyBhYhmeqNr5jhUP7Sm-6_pi7Yj1qSkXrV4piqX42cYZdgQIY0DgBFJAPeDbe4lLE5K8ovIGKCIsNmCC_vQSr-KZzPdSvhkc9adZ0js-zdjw2xRFz86d4Y1wViTa6fNLDdxwdMDjoHfRoGnc2scK3WOi6-eagt66IwgA-LVbvR5CGqWwEB3j6G7bCvjQyooXOdY0KeqbWIvVYEtUI4K72FnRiMVSs2-DR_F9BjAm9MUod7IkmQ6P38cWwaVUS4gUUs5hrcpBcHJ1J0RkngFyNTxsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccb1dc3.mp4?token=Qo-qr6-o3HXbWC3Icwdz9VXnkyd8O8n0QVtm5JCd-U7eYaFEzcAAgguSBFpqghyBhYhmeqNr5jhUP7Sm-6_pi7Yj1qSkXrV4piqX42cYZdgQIY0DgBFJAPeDbe4lLE5K8ovIGKCIsNmCC_vQSr-KZzPdSvhkc9adZ0js-zdjw2xRFz86d4Y1wViTa6fNLDdxwdMDjoHfRoGnc2scK3WOi6-eagt66IwgA-LVbvR5CGqWwEB3j6G7bCvjQyooXOdY0KeqbWIvVYEtUI4K72FnRiMVSs2-DR_F9BjAm9MUod7IkmQ6P38cWwaVUS4gUUs5hrcpBcHJ1J0RkngFyNTxsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جدیدترین تصاویر ماهواره‌ای از خسارت یمنی‌ها به تأسیسات ینبع عربستان
🔹
تصاویر ماهواره‌ای نشان می‌دهد مخازن تحت فشار ینبع همچنان در آتش می‌سوزد و حدود ۲۵۰ هزار بشکه در روز دیگر از ظرفیت تولید از مدار خارج خواهد شد.
🔸
نیروهای مسلح یمن بامداد شنبه تأسیسات آرامکو در جیزان و بندر ینبع در دریای سرخ را هدف قرار دادند. ساعاتی پیش رویترز اعلام کرد که فعالیت پالایشگاه جیزان متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/453193" target="_blank">📅 21:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so1gg2FGBCcf6bC_yGICDcllqPw3O85tf-gpZN_eLXSZFMf4CFwlyLiAnP5sY9D6P9Zf_AwfaN0wH9Z5qBsE_hE101HsoEBEHaes6pEfeJt12wQ_CM9PDATARAsOMwqbA42xmzXRsIs_Q2gNFEhSzdMFMzJHZaEaAzbg_Qy5N5G1L2Sxiedhan8fBIhP2aiDXA77cyIZiCwkDXGP7o82B8wiQtev8pn3kcBTqm9ICNeVgIaA8rAaBH5Xs9YTc0k7wZSIRkG8nC5oni5Of2m7MmGoO4VHxcWb69bsJXRUlO2cyoHPJ_3kaYBuGbkgeGlaHOKwHYDNrYkJu2qdonDVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دانشکده خبرگزاری فارس پس از تحریم آمریکا مجددا در دسترس قرار گرفت
آمریکا با اعمال تحریم علیه خبرگزاری فارس،  در روند صدور گواهی امنیتی (SSL) وب‌سایت این خبرگزاری و دامنهٔ دانشکده رسانه فارس (که زیرمجموعه این خبرگزاری است) را مسدود کرد.
این اقدام خصمانه باعث اختلال در دسترسی کاربران و دانشجویان به اخبار و امکانات این سامانه‌ها شده بود.
📢
مسئولان دانشکده از کلیه دانشجویان و داوطلبانی که قصد پیش‌ثبت‌نام در ترم مهرماه ۱۴۰۵ را دارند، خواسته‌اند تا از طریق آدرس جدید
edu.fna.ir
وارد سایت شده و ثبت‌نام خود را انجام دهند. همچنین از دانشجویان درخواست شده است که این آدرس را به سایر هم‌کلاسی‌ها و علاقه‌مندان به تحصیل در این دانشکده اطلاع‌رسانی کنند.
برای مشاهده کامل این خبر روی لینک کلیک کنید
✍️
دانشکده خبرگزاری فارس
به کانال
#اخبار_تولیدات_دانشجویان_خبرگزاری_فارس
بپیوندید
🔻
🆔
ایتا:
@edu_farsnews_ir</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/453192" target="_blank">📅 21:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b43a318fc.mp4?token=l2-NNC3NdSZBW19X5PP2xup7q3tjjK9ITue8iGsQkdPZrpH0JBDnRbNd8P69LauUbKy5Qui2DfmSTiWeFLipg26WD_sGZSouLK4mr-auQFfRr0RJWvHK2wQpmhMGCkMBRflQPJfSYqAGLDMcEjwDxW11nBhs3JA0X_cWASbSroEhjTi_FdO9sDrT_IqJiD9l_UZQhIcp9I5aLIuUsR8Ks3CdONSLKm8hj9iODafFT4hVfcsLMpkY8tDjM_z1yTKSxjQsKoVrdQrR58iQu5cCIXB7VWycc6-NWBjqnVKau-gLczLFBbZs_8x5ztHJ8iZ_Qmn01L2of1mALgagnc8p9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b43a318fc.mp4?token=l2-NNC3NdSZBW19X5PP2xup7q3tjjK9ITue8iGsQkdPZrpH0JBDnRbNd8P69LauUbKy5Qui2DfmSTiWeFLipg26WD_sGZSouLK4mr-auQFfRr0RJWvHK2wQpmhMGCkMBRflQPJfSYqAGLDMcEjwDxW11nBhs3JA0X_cWASbSroEhjTi_FdO9sDrT_IqJiD9l_UZQhIcp9I5aLIuUsR8Ks3CdONSLKm8hj9iODafFT4hVfcsLMpkY8tDjM_z1yTKSxjQsKoVrdQrR58iQu5cCIXB7VWycc6-NWBjqnVKau-gLczLFBbZs_8x5ztHJ8iZ_Qmn01L2of1mALgagnc8p9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یکی هوش مصنوعی را از ترامپ بگیرد
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/453191" target="_blank">📅 21:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKIp6y7gfTMnY_pLOzmcQ4_QpApW7GHM9mJ3YpXqIOosrP7N71GRpGjVinO9MZrsaCPRyhmx6thscY7t3f1LZkQL3Bq_uLAtz67kTGdTHfxMa_Rhowwm7i_OHjkQcEeiph_ePAamy2EVCpEmK_uK7Je2KRumAnqoGR24WMUhxJRwDTzKdTjNV5GJCtDVDFUJ6KruOUDKIco7SyxdDAzFhoVeJ48tn-YTVXMenLU3pOpnu95ljvGq3Nhq4bCg3N5aHFXfU1zSvi64Z3J60I3vrUHheMr8zk4Yjz11cmW-gbqb9HZnyJZe7FTZUGJnx1OFIM0bhqsaiu35kcPNZC4DnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اقدام «فرصت‌طلبِ مستقر در اوکراین» بی‌پاسخ نخواهند ماند
🔹
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و یک ملوان را کشته است. این اقدامی است که به‌وضوح منشور سازمان ملل را نقض می‌کند و به تحریک اسرائیل انجام شده تا اروپا را به جنگ آن بکشاند. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/453190" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a630d9eb90.mp4?token=VWzKkzIgRfExnqsUCD3RSRNkt1ZH7pzdfsvMg3EMJYvwk-PnljsH0LXxf2AK1n8mdYbna_ADK8wgaJq_Ki_tuEbXDEWeSkGpf7q_Rt6K-AHuV3UAsU5ByDctzI3hgqPuGlztIUnujfbjbdmC4-P5F6gl20m0lCFoUpQoyN0I8i2qBzx3C4arySqQYnrXnQ8OoQo6UJHGAi5PR_UAwIyuyBgINt5mkafBRNt4Q-y4-7Yf5pJPdruT_xjDjWsG4ReQLd4r3zltnCnQQowbwd058iFCQWQVIVt2l-nEp4yOOnWDAKBSPUdi_CgLH5bdhzBgYKMWv9EIhTWQ_mFde3f2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a630d9eb90.mp4?token=VWzKkzIgRfExnqsUCD3RSRNkt1ZH7pzdfsvMg3EMJYvwk-PnljsH0LXxf2AK1n8mdYbna_ADK8wgaJq_Ki_tuEbXDEWeSkGpf7q_Rt6K-AHuV3UAsU5ByDctzI3hgqPuGlztIUnujfbjbdmC4-P5F6gl20m0lCFoUpQoyN0I8i2qBzx3C4arySqQYnrXnQ8OoQo6UJHGAi5PR_UAwIyuyBgINt5mkafBRNt4Q-y4-7Yf5pJPdruT_xjDjWsG4ReQLd4r3zltnCnQQowbwd058iFCQWQVIVt2l-nEp4yOOnWDAKBSPUdi_CgLH5bdhzBgYKMWv9EIhTWQ_mFde3f2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: عمان اگر پیشنهاد ایران در مورد تنگۀ هرمز را نپذیرد تنگه همچنان بسته خواهد ماند و برای ازسرگیری جنگ آماده‌ایم
🔹
ما به‌هیچ‌وجه مسیر جنوبی تنگه را به رسمیت نمی‌شناسیم.
🔹
پیشنهاد ما این است که یک مسیر تنگه باید به‌طور کامل در اختیار ایران باشد و…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/453189" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c21265a1c9.mp4?token=nogx_SekJ-HZeXr2b3KsvsD9XJhyCageMo6c4rHEfERKceVwqsy50cC7mSLfFnluf42HjTxLhBZcbRIjRCe0wOV5pjODyHzEIagzUUt7SqkQZ0U0wwinFKWRDfwSRToOZu0UNrsbRribBvbqDIh0JQb5opDSOnoVWLBT7cD5giRMeUMJGuu98QEw2GmV8FuP3tdrW26ECSPxm7V4hi5BcOAp3ewFu-L3JTwHTCJurPXrO0xMHAYNTHBo6k4f5UGNZUaqyAIwRd9-IRKWN6EFlLei5wo8qIqfdz1OUc6Lmx3CEVLkmPiIW5LL4TXGY4ZRVdtXlAHU5D9Dpufbf2AQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c21265a1c9.mp4?token=nogx_SekJ-HZeXr2b3KsvsD9XJhyCageMo6c4rHEfERKceVwqsy50cC7mSLfFnluf42HjTxLhBZcbRIjRCe0wOV5pjODyHzEIagzUUt7SqkQZ0U0wwinFKWRDfwSRToOZu0UNrsbRribBvbqDIh0JQb5opDSOnoVWLBT7cD5giRMeUMJGuu98QEw2GmV8FuP3tdrW26ECSPxm7V4hi5BcOAp3ewFu-L3JTwHTCJurPXrO0xMHAYNTHBo6k4f5UGNZUaqyAIwRd9-IRKWN6EFlLei5wo8qIqfdz1OUc6Lmx3CEVLkmPiIW5LL4TXGY4ZRVdtXlAHU5D9Dpufbf2AQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعدامی‌های میدان علیخانی اصفهان چند پلیس را سلاخی کردند
🔹
حکایت جنایت شامگاه ۱۸ دی ۱۴۰۴ در میدان علیخانی اصفهان روایت نامردی و قساوت تروریست‌های اغتشاشگری است که ۴ مامور پلیس را با انواع و اقسام روش‌های داعشی وار از ضربات چاقو و قمه بر سر و گردن و بدن گرفته…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/453188" target="_blank">📅 20:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277f11af53.mp4?token=CEtHL8kMPhdoZGbExcWg4tULr8uQt7BVPfJi4xv870GcvUXUtKzYkPOfI3StyQKuyp639DUf27X3BjepSuXpyfvB2oOQMl2WEVqEEg6_mNLPXFQy03Y-YqqYtb_RK2sk6WbzymjeZVhnI6g8kIvSWs2OBd720WBvWXOIvmOLh-LKnksGbEXaUqSR_7OquMH-BfHB9ouPRMHDBc8tBQZ8q5T9jLKQmBDSTSP8I85dpc-mgf2261my-x37FlQ06a87uzNY5hBwiWE6WtEU5rf2lUkimECOTgA5tPNhS8pBP8reI27fgvPKHfkRf0qcZwfGl-1eDoO70Yfeb38-T5wKt1KZ6lZSeKEUP6R8WuF9UKQ1vCR57Ztp89FP0-osOpxubbli2Ekatdggo8jr-yRV9jlxxQ1ThRn9ejRjjCLkl1v344tMAplAf7JXxDdEqetOqMnMBeiTPFHVSy6W7DCLYi66aYKzVYyMfxZckczFneAFbiOgNgeZCvPsY9Db85CWbOeRaMGdUB7909_gNIDa3-CKZ3Soqyw0srSWBqncNtxByDPbUFeqpKxviehF7uQNtXjxWsTFS3RncGB7fFnPQjiw4K6WaTCw30IuPFIXdS3wvp9K762lRiqj8Fu2fshyTrTiZCaz7dOm_1MkK91yYOcUYDJe1fP-RueD0PN2gGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277f11af53.mp4?token=CEtHL8kMPhdoZGbExcWg4tULr8uQt7BVPfJi4xv870GcvUXUtKzYkPOfI3StyQKuyp639DUf27X3BjepSuXpyfvB2oOQMl2WEVqEEg6_mNLPXFQy03Y-YqqYtb_RK2sk6WbzymjeZVhnI6g8kIvSWs2OBd720WBvWXOIvmOLh-LKnksGbEXaUqSR_7OquMH-BfHB9ouPRMHDBc8tBQZ8q5T9jLKQmBDSTSP8I85dpc-mgf2261my-x37FlQ06a87uzNY5hBwiWE6WtEU5rf2lUkimECOTgA5tPNhS8pBP8reI27fgvPKHfkRf0qcZwfGl-1eDoO70Yfeb38-T5wKt1KZ6lZSeKEUP6R8WuF9UKQ1vCR57Ztp89FP0-osOpxubbli2Ekatdggo8jr-yRV9jlxxQ1ThRn9ejRjjCLkl1v344tMAplAf7JXxDdEqetOqMnMBeiTPFHVSy6W7DCLYi66aYKzVYyMfxZckczFneAFbiOgNgeZCvPsY9Db85CWbOeRaMGdUB7909_gNIDa3-CKZ3Soqyw0srSWBqncNtxByDPbUFeqpKxviehF7uQNtXjxWsTFS3RncGB7fFnPQjiw4K6WaTCw30IuPFIXdS3wvp9K762lRiqj8Fu2fshyTrTiZCaz7dOm_1MkK91yYOcUYDJe1fP-RueD0PN2gGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران یک‌صدا؛ تمام کشور خط مقدم است
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/453187" target="_blank">📅 20:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6541b50f3a.mp4?token=paIUKkUP6FKBrNgsCe8oSq1cQel5pmeLJfOw7Erzgz1Mj6MXaWtCOp1Kz3--dwruBiW74WjSXggwp-_kDy76233heRYFFuYPxGKTka7lNTJTllCFgPVsTZwOegNXytXPgNmp5P5GSydT_Cvis7aDb-zoq4sCU3fVJ8LkH6y4i3Qz-7T1qDqotTC0FqWnc3RjrVm2BfsxCWftSdkS-kSb4sxziFKnoWUHOcgGcU0dx6WzV-1CQs9v93Jnw_HBnJ_p50cTVF35BGMVYIjfW-UgrRsI6MQuTh-CZC0FHT_d1w-bI4KDPV-MQb6KgktRWZ2HOV4cTtRjIRC7cQVUX8WUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6541b50f3a.mp4?token=paIUKkUP6FKBrNgsCe8oSq1cQel5pmeLJfOw7Erzgz1Mj6MXaWtCOp1Kz3--dwruBiW74WjSXggwp-_kDy76233heRYFFuYPxGKTka7lNTJTllCFgPVsTZwOegNXytXPgNmp5P5GSydT_Cvis7aDb-zoq4sCU3fVJ8LkH6y4i3Qz-7T1qDqotTC0FqWnc3RjrVm2BfsxCWftSdkS-kSb4sxziFKnoWUHOcgGcU0dx6WzV-1CQs9v93Jnw_HBnJ_p50cTVF35BGMVYIjfW-UgrRsI6MQuTh-CZC0FHT_d1w-bI4KDPV-MQb6KgktRWZ2HOV4cTtRjIRC7cQVUX8WUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود
🔹
عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/453186" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
نیروهای مسلح یمن: یک نفتکش سعودی به نام NCC GHAZAL پس‌از آنکه هشدارها را نادیده گرفت با پرتاب چند موشک بالستیک مجبور به عقب‌نشینی و بازگشت شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/453185" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15afd9322d.mp4?token=jTs3QJ7xgxwcZt7MdXFVtPcovsubWuKv06TM1C8XnkwBzr6v6d-Ui1sYz4tkpoOz64d8a7wvYJkV3AOt-P0yoskHQ0Pr3UlUU8mbaeBHQ20V8qjN2N4hsbjS-ZMbLIMR0IW27K4O_yQE59zwimMSncqHS89zjmBSxGNxYsTAnZyNeuFU747cFo8gliEZ7-JdwgfeW36luHkPAyPorIUdd9G3Vwg5sO737G4mrWE3DFfFoUEjJpq0wdDNEdHtbb00zCYM9wH8qcpYP2gj2udwVSNu-37V96hIqFqzDE8thjwE_6yBueD1qoK7B90JY-0agGJz4D4000Dh_6enGerpXYJ9bhXL-_Eh-RpKzVxSv5t_ALx4m2mw6j5dLYbLEzsRpTucXnjONbYH1CKl4Hy1g1aYHKKeDty6ZDbO3D_GGlaTPxPLBrm8u5lNih1A9507vwDvCXWk1rWcrdiqLVKMH90950zALvyhMZJWgV4ys7HcOH8C_BH9VQpiBqL31Olr8C1eOFk3RtPwX-GGaSPityrgHd7-R_o3MBXtPpTut8DBKvp4C5ezBTvjOvfC6jviIqqe3SONuQer8DPj52xovW2A3ZbyrHUYCVnBwjB2Ok8O8pQUO7Dg01CcHz1BUl73xs_pYyii9yXC87G3PPae1zmFgQouNBWg6zlxAil-2u8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15afd9322d.mp4?token=jTs3QJ7xgxwcZt7MdXFVtPcovsubWuKv06TM1C8XnkwBzr6v6d-Ui1sYz4tkpoOz64d8a7wvYJkV3AOt-P0yoskHQ0Pr3UlUU8mbaeBHQ20V8qjN2N4hsbjS-ZMbLIMR0IW27K4O_yQE59zwimMSncqHS89zjmBSxGNxYsTAnZyNeuFU747cFo8gliEZ7-JdwgfeW36luHkPAyPorIUdd9G3Vwg5sO737G4mrWE3DFfFoUEjJpq0wdDNEdHtbb00zCYM9wH8qcpYP2gj2udwVSNu-37V96hIqFqzDE8thjwE_6yBueD1qoK7B90JY-0agGJz4D4000Dh_6enGerpXYJ9bhXL-_Eh-RpKzVxSv5t_ALx4m2mw6j5dLYbLEzsRpTucXnjONbYH1CKl4Hy1g1aYHKKeDty6ZDbO3D_GGlaTPxPLBrm8u5lNih1A9507vwDvCXWk1rWcrdiqLVKMH90950zALvyhMZJWgV4ys7HcOH8C_BH9VQpiBqL31Olr8C1eOFk3RtPwX-GGaSPityrgHd7-R_o3MBXtPpTut8DBKvp4C5ezBTvjOvfC6jviIqqe3SONuQer8DPj52xovW2A3ZbyrHUYCVnBwjB2Ok8O8pQUO7Dg01CcHz1BUl73xs_pYyii9yXC87G3PPae1zmFgQouNBWg6zlxAil-2u8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خادم اربعین از نگاه متفاوت امسال عراقی‌ها به ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/453184" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96676ac370.mp4?token=ASR4yNzLJJSXMZQ9Vw9JNFW9xPHjXni69gv0jZw_QypVmnL8pt4VcyUMN_67eyV2Zecb6YWuZXGDLW1CGRAYHQwdieKk2IMLe14ULHvwipddKKY9vry8s9wbSHhlV0ztOrj5tqxPG7HmIGYb-h3FeXDhKaUTal0snrA-LzTV-FLpGUOJYVcSxFsX9JlHgGiJ16T6ZDF69Ql1D0Ton8sGnVvqH45lYLolXspW8XYypWfj2-5QvTyRKFuNN1gO8T8-1JithNBa5HpmozRq7t1jjso66_NKqjBCXtbuaj-l9RklN06G6K0gCrYYtDf7CCMduhVPRwJiq86p5im7d979aLiWOmJ7qO2LQl3TIJKdKGl4A3cy2hf4rd_mTuZPwPJezczUK7eWzbbBynay-_05ShUNNU-mwiUi7CeGXqEAMLRy7QbTusTjm00960iHjwzvbO57B1GXnLhav6KxtYVkuyuYkOer_Sf1IKrctO6W5pkXlYWf6RP_SSA-aRmJIp_OPCM8ZcSkZ1kAhEWl4RNtmzVdF_PynJ_Cgt8vTF9MWVOPZ6i974epWY-aeRNwnon7xsOzQn4DJMe7fF_1dWpGhPNpDAbpsH8r1fmIfaqlyi2EWUa8tLOYxQgFtYdGRJQwG9gI9QRvWiKl_Bo2cBpZyr60udRsChCDTYG1wJvr3Fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96676ac370.mp4?token=ASR4yNzLJJSXMZQ9Vw9JNFW9xPHjXni69gv0jZw_QypVmnL8pt4VcyUMN_67eyV2Zecb6YWuZXGDLW1CGRAYHQwdieKk2IMLe14ULHvwipddKKY9vry8s9wbSHhlV0ztOrj5tqxPG7HmIGYb-h3FeXDhKaUTal0snrA-LzTV-FLpGUOJYVcSxFsX9JlHgGiJ16T6ZDF69Ql1D0Ton8sGnVvqH45lYLolXspW8XYypWfj2-5QvTyRKFuNN1gO8T8-1JithNBa5HpmozRq7t1jjso66_NKqjBCXtbuaj-l9RklN06G6K0gCrYYtDf7CCMduhVPRwJiq86p5im7d979aLiWOmJ7qO2LQl3TIJKdKGl4A3cy2hf4rd_mTuZPwPJezczUK7eWzbbBynay-_05ShUNNU-mwiUi7CeGXqEAMLRy7QbTusTjm00960iHjwzvbO57B1GXnLhav6KxtYVkuyuYkOer_Sf1IKrctO6W5pkXlYWf6RP_SSA-aRmJIp_OPCM8ZcSkZ1kAhEWl4RNtmzVdF_PynJ_Cgt8vTF9MWVOPZ6i974epWY-aeRNwnon7xsOzQn4DJMe7fF_1dWpGhPNpDAbpsH8r1fmIfaqlyi2EWUa8tLOYxQgFtYdGRJQwG9gI9QRvWiKl_Bo2cBpZyr60udRsChCDTYG1wJvr3Fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: درحال‌حاضر گفت‌وگوی ما فقط با عمان و در موضوع تنگه هرمز است؛ هیچ مذاکره‌ای با آمریکا یا میانجی‌ها نداریم   @Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/453183" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f443fa20.mp4?token=Nn46RBIzcgN-EDJbY5mJ9_sxtchIhbITGwVUVkMQn286zDUFKOdOxhj1GXpjHzc65AO8GgxoK9QoAbg34hpkkvMIksCPX5jDNnOQ80hVQnSkQE1_iUWnCBGw7xLDOnKWN0szeKcwerR-NYhCg_A86R7UWn97pNFL829As6Gi0EToKiIgh7IyONt4RJs48oK2xyaXbZhWCAHRW95OfbbMFCIoL6L9iCD6ENclvM9JgrfFkV6FLLVc0Y0XOgzd9eYfSQFf39dXZMBIqxHRmKrKzJmU022-jFue8ZQ9dF7hm3-_eLtpoaVO_Cc4kNGDjQ1XbmgdtDRF2EepZhUR1MTugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f443fa20.mp4?token=Nn46RBIzcgN-EDJbY5mJ9_sxtchIhbITGwVUVkMQn286zDUFKOdOxhj1GXpjHzc65AO8GgxoK9QoAbg34hpkkvMIksCPX5jDNnOQ80hVQnSkQE1_iUWnCBGw7xLDOnKWN0szeKcwerR-NYhCg_A86R7UWn97pNFL829As6Gi0EToKiIgh7IyONt4RJs48oK2xyaXbZhWCAHRW95OfbbMFCIoL6L9iCD6ENclvM9JgrfFkV6FLLVc0Y0XOgzd9eYfSQFf39dXZMBIqxHRmKrKzJmU022-jFue8ZQ9dF7hm3-_eLtpoaVO_Cc4kNGDjQ1XbmgdtDRF2EepZhUR1MTugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‎‌‌ابادی: هدف ما در تنگه هرمز هم اعمال حاکمیت است و هم کسب درآمد
🔹
این‌که بگوییم کسب درآمد از تنگه اولویت ما نیست اشتباه است. @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/453182" target="_blank">📅 20:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d7c3e1c10.mp4?token=a-YlJL71DLQ9Fhe17R5X3VuygbqwQRqj-CbDZ8Nzf8Nr7IuXQ3qDXwewvPvvcVmGhewfi815_PCpBYPzQho7htEMrWRnCxc9o0zoZSVxXPZAXj0AAdEm_wlbFYJ6N1-zZAQKq_Uu4k7MBGIOY_C1_80RSQ37HEHY4UsXsWCGq3Hou0XPRKPwi_PPMaqOokz2e47dzf4l_KaIokbkiKvDsKSOVZaOumOPw9gkJhNTcXWbbj-cLzwVP9EaRv5sGwSavCK8kU6FfsZmb8fYomIYQG_c0nptUjdappUHWkdaiWavOFqC8uUGsiuGFlHOCv8pKOhbQ57LozvPh774D8rGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d7c3e1c10.mp4?token=a-YlJL71DLQ9Fhe17R5X3VuygbqwQRqj-CbDZ8Nzf8Nr7IuXQ3qDXwewvPvvcVmGhewfi815_PCpBYPzQho7htEMrWRnCxc9o0zoZSVxXPZAXj0AAdEm_wlbFYJ6N1-zZAQKq_Uu4k7MBGIOY_C1_80RSQ37HEHY4UsXsWCGq3Hou0XPRKPwi_PPMaqOokz2e47dzf4l_KaIokbkiKvDsKSOVZaOumOPw9gkJhNTcXWbbj-cLzwVP9EaRv5sGwSavCK8kU6FfsZmb8fYomIYQG_c0nptUjdappUHWkdaiWavOFqC8uUGsiuGFlHOCv8pKOhbQ57LozvPh774D8rGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ادارهٔ گذرنامه وزارت خارجه: اگر زائران اربعین وسایل یا مدارک هویتی خود را گم کردند، نگران نباشند؛ ۱۲۸ خط ارتباطی ما برای مواقع اضطرار است.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/453181" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1775ee1020.mp4?token=RZc99qw-9EIXOu0DpPVCxxJjDMg0KSdjrp6-HyH1nONyenclAyDQ87vsmko3UDU278lI_a2BexUfBCb0JzljdCO1GDk05XrIpb4vSYDfqOh3sg-vxCyn-I44hClsHBF3_VMW8dEaaXLr_-QjzKXJ6qigD56JEszWirAZXWLLtiaP7fWEGxxXSMlQtgJC8ArQ2a9EOP99TEv8aPXmVSGrMwn631FiPJbjg8RwpI2nZD_nNmPnz8TfJLiJs0pwdyo_qFK_4r8B0Fd6HiY99oRkuvGlhnzC5aUWoJoe63Naef3G18r_1UCIk363Amb8y_8erCz1pv1rg2Y6rWIcghotAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1775ee1020.mp4?token=RZc99qw-9EIXOu0DpPVCxxJjDMg0KSdjrp6-HyH1nONyenclAyDQ87vsmko3UDU278lI_a2BexUfBCb0JzljdCO1GDk05XrIpb4vSYDfqOh3sg-vxCyn-I44hClsHBF3_VMW8dEaaXLr_-QjzKXJ6qigD56JEszWirAZXWLLtiaP7fWEGxxXSMlQtgJC8ArQ2a9EOP99TEv8aPXmVSGrMwn631FiPJbjg8RwpI2nZD_nNmPnz8TfJLiJs0pwdyo_qFK_4r8B0Fd6HiY99oRkuvGlhnzC5aUWoJoe63Naef3G18r_1UCIk363Amb8y_8erCz1pv1rg2Y6rWIcghotAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: ما در زمان محاصره از طریق کریدورهای مختلف بخش زیادی از کالاهای خودمان را تامین می‌کنیم اما بسته‌بودن تنگه هرمز تقریبا به کل دنیا فشار وارد می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/453180" target="_blank">📅 20:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a0c73ec9.mp4?token=LyWQQ-hhLVDMh1sAMukFwehOB_gVjGkAf7yhLuBAU5jXmwLg9lXlGH2pUA_KjPnBriBTfb1VEGZBmbqdBfkzht5aImMw8c8YzPiLC_fYLXb7wBr-W1BBpikTohQXUw_lSnDMOPCsSrf83HUD-oSnZdYsp5iKUkjHaPJjQrm5w1grbdMhvAA1qaN8kRM2jpyXHN2olo3J3coQTCh7rzsw2CZuxkqdSh1FlBwBEibOnwTs-GRdr9JN7pxCBG_mnzfmWREsdFoPGlWxvbrbDiQyBtwB34ptB_44ifJfnKwwloEE6htuOlzO75bvUHB98IDOe4Vw8vvoGiEqpp7Oe0kAiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a0c73ec9.mp4?token=LyWQQ-hhLVDMh1sAMukFwehOB_gVjGkAf7yhLuBAU5jXmwLg9lXlGH2pUA_KjPnBriBTfb1VEGZBmbqdBfkzht5aImMw8c8YzPiLC_fYLXb7wBr-W1BBpikTohQXUw_lSnDMOPCsSrf83HUD-oSnZdYsp5iKUkjHaPJjQrm5w1grbdMhvAA1qaN8kRM2jpyXHN2olo3J3coQTCh7rzsw2CZuxkqdSh1FlBwBEibOnwTs-GRdr9JN7pxCBG_mnzfmWREsdFoPGlWxvbrbDiQyBtwB34ptB_44ifJfnKwwloEE6htuOlzO75bvUHB98IDOe4Vw8vvoGiEqpp7Oe0kAiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان کشمکش بر سر مدافع تیم ملی
🔹
نساجی از دانیال ایری رونمایی کرد
@Sportfars</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/453179" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9f652a25.mp4?token=JahtlzI6ql2B9Wh9qmFka81nwtTe-gXHDYK7wG7Pm7BSg7pMFJSQKh4p9LtuDpwYsEKTWU7jvsIdgKYOzAxYIWYENSOPuAazuwOacr94UpOF4hlBZix_ZEm9nB3G60Vl6gg7kzaJNhSv6npApi_0Z92bnkHA7xJhzTBKpjNx7EDmp1P8KW_c3GwAvIzGpvWELqa8ELVeo9OsMRUJ_mniV-BnEFgQR6PR8Y1dYgd1HyJr3lEqgKpOKxT_8j7Pe5OK7x9d1lQLDYckhOqO39PDFkG184fgUhUylsNZ0e21szdeLm45ngiTnOTGzCm6bwxdOWeujnl2_RgrBPcVWmKUIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9f652a25.mp4?token=JahtlzI6ql2B9Wh9qmFka81nwtTe-gXHDYK7wG7Pm7BSg7pMFJSQKh4p9LtuDpwYsEKTWU7jvsIdgKYOzAxYIWYENSOPuAazuwOacr94UpOF4hlBZix_ZEm9nB3G60Vl6gg7kzaJNhSv6npApi_0Z92bnkHA7xJhzTBKpjNx7EDmp1P8KW_c3GwAvIzGpvWELqa8ELVeo9OsMRUJ_mniV-BnEFgQR6PR8Y1dYgd1HyJr3lEqgKpOKxT_8j7Pe5OK7x9d1lQLDYckhOqO39PDFkG184fgUhUylsNZ0e21szdeLm45ngiTnOTGzCm6bwxdOWeujnl2_RgrBPcVWmKUIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: محاصرۀ دریایی نمی‌تواند ایران را وادار به گفت‌وگو کند  @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/453178" target="_blank">📅 20:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c871bd642.mp4?token=gQ0OwcdhidZO7BMVEDJx987eUWU-lPBeTYv5v4p_ulYLEluAyxB4zutRaGMjcwBxHCOMxYyu2YrtIui2Z4Dra1Nh7bu_MLpv7joTSXX8F0cYErrdBwhAa1k0NIz-__xrV3GMlEdiO3C4Yfv1wNlVgxvKKjC0KxOVCA71mUVZqCJ3t4m5t1Wr3b5w-fb1a3dWjcVCJhRYgxqK3s9rLC_OJN1wuJmtRVPurWdwgLiyQPq2UkUaurP2zEvmQ0kFCBN8vEJhVL9-PCQaI5d4MQoj-mr7Q1Ub0GJQrbP2Knhnlzb1PYJXcRw0tyK8wVvwA2FCbeFjQQZvYJiezgserqlJiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c871bd642.mp4?token=gQ0OwcdhidZO7BMVEDJx987eUWU-lPBeTYv5v4p_ulYLEluAyxB4zutRaGMjcwBxHCOMxYyu2YrtIui2Z4Dra1Nh7bu_MLpv7joTSXX8F0cYErrdBwhAa1k0NIz-__xrV3GMlEdiO3C4Yfv1wNlVgxvKKjC0KxOVCA71mUVZqCJ3t4m5t1Wr3b5w-fb1a3dWjcVCJhRYgxqK3s9rLC_OJN1wuJmtRVPurWdwgLiyQPq2UkUaurP2zEvmQ0kFCBN8vEJhVL9-PCQaI5d4MQoj-mr7Q1Ub0GJQrbP2Knhnlzb1PYJXcRw0tyK8wVvwA2FCbeFjQQZvYJiezgserqlJiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود
🔹
نباید پاسخ‌های خودمان را ضعیف تلقی کنیم. @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/453177" target="_blank">📅 20:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r63ARALz7TqygKkM-wUP4yAqwVQWncskyXoSBZdBAjWl_IDLEEfog0ap7YQx7sx5JDcOUL7Mu4b7dkHm_uvsun5DuO2mzUN1BFnRM2obIx8JY30lPckm83_yds4B4dTKlKgG4AOY9KqoIWyrJvS1TIGEeRpiJgZS-3IIT4dL_2ork8H5zRGGXfCxr--ZRssGgGyXxnc_9OQvSBENEMf37noqws8fIqxo8XosaH98vQ2jfJDqe0cESys6rmWbEe44vRwB1sqeaLkwcN87QJySqfwswalrKTTGhd7REP4UbCda0Ytx_RgTW7RVGMUTCRMaiEfYKzLTHSkhOVXHfWYrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردپای شرکت‌های منحل‌شده در وام‌های میلیاردی یک بانک
🔹
یک شرکت فعال در حوزه فروشگاه‌های زنجیره‌ای چندین فقره وام به اسم شرکت‌های مختلف از بانک دی گرفته اما این شرکت سال ۹۹ بدون بازپرداخت وام‌های یک بانک خصوصی منحل شده و حالا بدهی‌های آن پای ثابت آمارهای منتشر شده این بانک است.
🔗
شرح و مستندات این ماجرا را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/453176" target="_blank">📅 20:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee188f7b3e.mp4?token=p4tdwwNvRgxTjV-taiB4amtfIXQ-y0giYu62JtwthD-GGhHa654qDJ1e6HET7XFWXKcmpd0WEtL1WuhU10b0n3Y3n72TUk8itxHckwVpqww6Ejh9vON9nBsJQ1RphdzpE3FBzXEP12c5nSwDZiOaidwag_qu2LOzGyyg3G5oFtGr6pOihKRsNneO_YIJAzFlqY8ciqzIsmIp0jmna04XaRayGymJcaXuWKP1wf2Z_aPWU1uFUk1Q5IL-aYzDt8IboXSwC7qmTqnQmyibBo_vxsFfrx6ue9dzXUdfvlQ-TLs0hYC2sJOU2fnfN06elki560HGSDyJkzQBPS4ZBLztVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee188f7b3e.mp4?token=p4tdwwNvRgxTjV-taiB4amtfIXQ-y0giYu62JtwthD-GGhHa654qDJ1e6HET7XFWXKcmpd0WEtL1WuhU10b0n3Y3n72TUk8itxHckwVpqww6Ejh9vON9nBsJQ1RphdzpE3FBzXEP12c5nSwDZiOaidwag_qu2LOzGyyg3G5oFtGr6pOihKRsNneO_YIJAzFlqY8ciqzIsmIp0jmna04XaRayGymJcaXuWKP1wf2Z_aPWU1uFUk1Q5IL-aYzDt8IboXSwC7qmTqnQmyibBo_vxsFfrx6ue9dzXUdfvlQ-TLs0hYC2sJOU2fnfN06elki560HGSDyJkzQBPS4ZBLztVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: عمانی‌ها می‌خواستند یک کشوری را برای مین‌زدایی از بخش جنوبی تنگۀ هرمز بیاورند اما ما اجازه ندادیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/453175" target="_blank">📅 20:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6b6ed353.mp4?token=AQi8Iti9ofjNdFSb4udsmsAc-2xBtGY63ZszV_R7f7_ivWjQsecFpGjjG8YQRxdxy34zQPEtyL5XsOnmspy_vhubiOeqW-wuchfQ0JaUHkrUSpk71_RByrDNDwNzcj9sa26ujy6eEyRfS4r-5-sc8wT6WIvWdf3TfpvgKDg-jAWTAARQ8s7SGX1uTgBQ__O_fuz9FFXLJjzPtmqWMi8gCcyOlg6hIgX4SguX3SBWKsb5Ii3fNjKwoyHNsU0VAoNLBDkITf5XITbSYu3UE1bceFCNp5RM5_6O6CuDV0HIGPwkNVjqJTb60dJHDqZ2xQxMECBpwafboBvxmS22m51apA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6b6ed353.mp4?token=AQi8Iti9ofjNdFSb4udsmsAc-2xBtGY63ZszV_R7f7_ivWjQsecFpGjjG8YQRxdxy34zQPEtyL5XsOnmspy_vhubiOeqW-wuchfQ0JaUHkrUSpk71_RByrDNDwNzcj9sa26ujy6eEyRfS4r-5-sc8wT6WIvWdf3TfpvgKDg-jAWTAARQ8s7SGX1uTgBQ__O_fuz9FFXLJjzPtmqWMi8gCcyOlg6hIgX4SguX3SBWKsb5Ii3fNjKwoyHNsU0VAoNLBDkITf5XITbSYu3UE1bceFCNp5RM5_6O6CuDV0HIGPwkNVjqJTb60dJHDqZ2xQxMECBpwafboBvxmS22m51apA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: ما هیچ تقاضایی برای مذاکره با آمریکا در ۱۵ روز گذشته نداشته‌ایم
🔹
آمریکایی‌ها از ما تقاضای گفت‌وگو کرده‌اند؛ آن‌ها همچنین از طریق عمان به ما پیام دادند که اقدامات نظامی علیه ما انجام نمی‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/453174" target="_blank">📅 20:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02bb458cd.mp4?token=CWtPjT8wXbnDR_33DPJxKVXPjQYRrIe35ylUehDo8A_Tsat6WYfYbIJd9CxS0iFbkkgZXV87QUOCarQWJZbN6I_qevc9MK3y8HgekjLHrLlJyBGHZB8dv3_-j9-ZG7oX3lyYwTVQX4J76UYgYRWKe01Um3ZLHn3fN1b5McSjgTgRBeAXDFdBEKOIJ1ICG0ZRv7ZxG73x-atTi-taT4Yac1R_ftotUqzRZrqylcSnVaq0C2-H1ZeliskVKbd36q5BgJ9Q5OuiOUBBu8_Y1pNqb5AZ_2hmeVdkY8W0oM3kZYdn-Z3VoCF8EIxoEAK91XjZnytrrOxvZG3QQpJFv0H36Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02bb458cd.mp4?token=CWtPjT8wXbnDR_33DPJxKVXPjQYRrIe35ylUehDo8A_Tsat6WYfYbIJd9CxS0iFbkkgZXV87QUOCarQWJZbN6I_qevc9MK3y8HgekjLHrLlJyBGHZB8dv3_-j9-ZG7oX3lyYwTVQX4J76UYgYRWKe01Um3ZLHn3fN1b5McSjgTgRBeAXDFdBEKOIJ1ICG0ZRv7ZxG73x-atTi-taT4Yac1R_ftotUqzRZrqylcSnVaq0C2-H1ZeliskVKbd36q5BgJ9Q5OuiOUBBu8_Y1pNqb5AZ_2hmeVdkY8W0oM3kZYdn-Z3VoCF8EIxoEAK91XjZnytrrOxvZG3QQpJFv0H36Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: تنگۀ هرمز شاخص بسیار مهم برای برآورد موفقیت ایران در جنگ است
🔹
ترتیباتی که بر تنگۀ هرمز اعمال خواهد شد تاثیرات بلندمدت بر امنیت ایران خواهد داشت.
🔹
اگر ترتیبات تنگۀ هرمز به وضعیت قبلی برگردد موفقیت ما در جنگ کامل نخواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/453173" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25230ebcb9.mp4?token=tGtnl6srD5cqP07oRGUL1Scd2tAak8U4fRXeXvnhMb-DFtLy4Xn3D6JRwrb8OmB4wZ2vBViKiqzcMG1QbEc99YoAUPKro0j43clOuwnWCjSCAnq4od1klREW7-wcNWkEacLyVC3Ovp9-9ERuumlFom4ysU0z1MM1DX-sFOkz6Nou5Jda00l6krwv8R3F2tTUxulep5xKL0AcukwGmKwmlDrkEfAWJzF2oFnD9Y2_K9O_cEs2IwgZ9Qtuw3i1Updhm-iEDGeTWLdC6PF6wmsjN57gPUkywtvH_iBTfiwy9Ax1P36rZFtOnacXOQyXFdNXHLN06MO9BM_P3CfxJb67qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25230ebcb9.mp4?token=tGtnl6srD5cqP07oRGUL1Scd2tAak8U4fRXeXvnhMb-DFtLy4Xn3D6JRwrb8OmB4wZ2vBViKiqzcMG1QbEc99YoAUPKro0j43clOuwnWCjSCAnq4od1klREW7-wcNWkEacLyVC3Ovp9-9ERuumlFom4ysU0z1MM1DX-sFOkz6Nou5Jda00l6krwv8R3F2tTUxulep5xKL0AcukwGmKwmlDrkEfAWJzF2oFnD9Y2_K9O_cEs2IwgZ9Qtuw3i1Updhm-iEDGeTWLdC6PF6wmsjN57gPUkywtvH_iBTfiwy9Ax1P36rZFtOnacXOQyXFdNXHLN06MO9BM_P3CfxJb67qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: باید چرخۀ جنگ و آتش‌بس و مذاکره را قطع کنیم  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/453172" target="_blank">📅 20:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69add72a9.mp4?token=MBWyds1PUA2uMdrEupgeuMKVWZzNLGvXxzl2TYPzylrbVN1IAmAU-r8tqQSQYCObd5cwCXFb-DX9N3yvXYJ2ttgvhiQQXzXDgr87BGNm8ZLASk0nue7gT8Ne5-KTuemujdLlg_duNfhrFEeYE-JV7g6zCyNeGY78rXm2XpwySriJ2-IaFKmTlYHUmCD6wapu7vr2cmYRaGctbfcM8Sz88jtYPoAflhKPSh-Z3AwAcuGyqGyMDFBGALoo51dlqpbRQXDsqlBLmQ-DWzz4qIwZyr7ReVY_KCm99NqJ9pUmSJ8Co5xyu8wcd4O3z3tRv-FDNDBpbv6TRhXj_nJAXrc4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69add72a9.mp4?token=MBWyds1PUA2uMdrEupgeuMKVWZzNLGvXxzl2TYPzylrbVN1IAmAU-r8tqQSQYCObd5cwCXFb-DX9N3yvXYJ2ttgvhiQQXzXDgr87BGNm8ZLASk0nue7gT8Ne5-KTuemujdLlg_duNfhrFEeYE-JV7g6zCyNeGY78rXm2XpwySriJ2-IaFKmTlYHUmCD6wapu7vr2cmYRaGctbfcM8Sz88jtYPoAflhKPSh-Z3AwAcuGyqGyMDFBGALoo51dlqpbRQXDsqlBLmQ-DWzz4qIwZyr7ReVY_KCm99NqJ9pUmSJ8Co5xyu8wcd4O3z3tRv-FDNDBpbv6TRhXj_nJAXrc4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: ما ظرفیت جدید دفاعی کشف کرده‌ایم به‌نام تنگۀ هرمز
🔹
تنگۀ هرمز بخشی از امنیت ملی ایران شده و یک ظرفیت و توان دفاعی برای ایران است.
🔹
دنیا باید بداند ایران دارد ابزارهای دفاعی خود را افزایش می‌دهد و ما به‌هیچ‌وجه نمی‌توانیم از این ابزارها دست بکشیم.…</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/453171" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc4a5c2a52.mp4?token=kCrZ1X7JtSAZoEIPxPxavGkDZn0G2W-Qfooc96u2PcZjSOav8IfuhZDRf9qYlaNLGYreTCNDdBpF3PuquDP-ZkDzUyW19w4SrQ_4CpGejNSZ1eVvRySmMW_dA6MV0we-K2XrlQ3PKUIT4tDVq0Hu6Sl8hCkpZny9mU7NHMCdhgw6_1hs714wbRubfCGYvS5gT5MV_bCuT0g0o311Ls9gHPIOIwyinC-YgBzZfdRNZLwG3QgpmSpVwS0XPU09_ELJ6bsGYyR0ZVwVPbQ3-5K_Q5q2UwCX3SowG1Wf6AbNcD92koPR65rwtgGTkAho39bXF2VxIPqpKFVX8--bN5WCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc4a5c2a52.mp4?token=kCrZ1X7JtSAZoEIPxPxavGkDZn0G2W-Qfooc96u2PcZjSOav8IfuhZDRf9qYlaNLGYreTCNDdBpF3PuquDP-ZkDzUyW19w4SrQ_4CpGejNSZ1eVvRySmMW_dA6MV0we-K2XrlQ3PKUIT4tDVq0Hu6Sl8hCkpZny9mU7NHMCdhgw6_1hs714wbRubfCGYvS5gT5MV_bCuT0g0o311Ls9gHPIOIwyinC-YgBzZfdRNZLwG3QgpmSpVwS0XPU09_ELJ6bsGYyR0ZVwVPbQ3-5K_Q5q2UwCX3SowG1Wf6AbNcD92koPR65rwtgGTkAho39bXF2VxIPqpKFVX8--bN5WCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: هر ناو اروپایی که بخواهد نزدیک تنگه هرمز بیاید هدف مشروع ماست  @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/453170" target="_blank">📅 19:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8249b58d1.mp4?token=NILBMry-sncfHYi5VLtc_qoRsf_pv5tR-vQxYZLSVmG9eNHUPmjOJDBVEZ3RudjdTrYNFRa3eqJvZqD3uxCqllhec1D15xbKPatIJSvC9dSvfvYC-7MsdnZYZyqWkROGRSTc8ekeMJ8tMf2Bv-G0NlD6SJxTCRTIlRV9vYjK7pqdDoDFNSXXg3fq1cflqqf1vPKOx3Pb2B_CCdcJOeU1QmF1uI4nL20dv8q5htifUn7r850IUQvPZnX6rp91CaLGBXQEs0b5qDT3UldAKdf7iaDq62OyQb0TiMF9RD166-CK-FrgoePDPtjqIY15jsBDcaFQXq530QNJB2GsMX3Twg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8249b58d1.mp4?token=NILBMry-sncfHYi5VLtc_qoRsf_pv5tR-vQxYZLSVmG9eNHUPmjOJDBVEZ3RudjdTrYNFRa3eqJvZqD3uxCqllhec1D15xbKPatIJSvC9dSvfvYC-7MsdnZYZyqWkROGRSTc8ekeMJ8tMf2Bv-G0NlD6SJxTCRTIlRV9vYjK7pqdDoDFNSXXg3fq1cflqqf1vPKOx3Pb2B_CCdcJOeU1QmF1uI4nL20dv8q5htifUn7r850IUQvPZnX6rp91CaLGBXQEs0b5qDT3UldAKdf7iaDq62OyQb0TiMF9RD166-CK-FrgoePDPtjqIY15jsBDcaFQXq530QNJB2GsMX3Twg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: اگر ما مسیر جنوبی تنگۀ هرمز را باز می‌کردیم دیگر به‌هیچ‌وجه نمی‌توانستیم در تنگه اعمال حاکمیت کنیم
🔹
ایران برای اینکه حاکمیت خود را بر تنگه تثبیت کند نگران هیچ اقدامی نیست؛ حتی از سرگیری جنگ. @Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/453169" target="_blank">📅 19:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f437be77.mp4?token=Av4EQM8GGl1pmkw8uwTRj2UDwQODfr4NhE532tm7mL3ti7yaWjkgOK96Irw8aoxHDBflFSUz74IVltMv0C2mEoxh11j5BVP2GOMbrQMqJwJT8oNT60jeH99GlBLD5XMHlFcu2Xv7xE_x1KvyEo8RgjvEZ0qC0coCUlb6yjjc4rmf8IUkxwzkmg0ELOWdcKzznwkzMOAiGtLOJU9RqbfvP1vBatCscfmVNfWq5QBkYRsx4Yjf13scHUfkXpVZnsRzw6PFUqLjBvaknQjSlL7tuSGvGFzh9tjzO4UCnJCQtROsvwZIqscKbmrQTsCgDiyEqmO9-yZs3QwRv9dxwLmL_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f437be77.mp4?token=Av4EQM8GGl1pmkw8uwTRj2UDwQODfr4NhE532tm7mL3ti7yaWjkgOK96Irw8aoxHDBflFSUz74IVltMv0C2mEoxh11j5BVP2GOMbrQMqJwJT8oNT60jeH99GlBLD5XMHlFcu2Xv7xE_x1KvyEo8RgjvEZ0qC0coCUlb6yjjc4rmf8IUkxwzkmg0ELOWdcKzznwkzMOAiGtLOJU9RqbfvP1vBatCscfmVNfWq5QBkYRsx4Yjf13scHUfkXpVZnsRzw6PFUqLjBvaknQjSlL7tuSGvGFzh9tjzO4UCnJCQtROsvwZIqscKbmrQTsCgDiyEqmO9-yZs3QwRv9dxwLmL_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: سیاست جمهوی اسلامی ایران این است که تنگه هرمز هیچ‌گاه به حالت قبل از جنگ برنگردد  @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/453168" target="_blank">📅 19:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453161">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519606231.mp4?token=jt9SuugLW_4VNDCiQN3hpgmeFjoSsV9vX6Z2IeFWIx5T6sZCXoAUDWzrTpP0wI-6FDWD2TcB9R3EZjGRwMsuW6ky7R7epHGYfeC7TmEJcwl_TZwUqPcadsAspeK004nH_TIIc-bwZK6tPCUF9qhrb5bin5DC4NYB7u9xdySrulHu3njcmxt02fEObB_pjgJ-_fHvqL3T4_-NVqiv2NVdLVJIPkSKnawY9IcigNj8glDJVlW7KFbCnYDGlrrmHteYHtztn5Pd10r3Mjz0WSdwEcsF6sQxAfRQQbdHffpeMydfox7V7tTPPePSFcLtrcVhnj1yOmdLRW96epkFsc51yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519606231.mp4?token=jt9SuugLW_4VNDCiQN3hpgmeFjoSsV9vX6Z2IeFWIx5T6sZCXoAUDWzrTpP0wI-6FDWD2TcB9R3EZjGRwMsuW6ky7R7epHGYfeC7TmEJcwl_TZwUqPcadsAspeK004nH_TIIc-bwZK6tPCUF9qhrb5bin5DC4NYB7u9xdySrulHu3njcmxt02fEObB_pjgJ-_fHvqL3T4_-NVqiv2NVdLVJIPkSKnawY9IcigNj8glDJVlW7KFbCnYDGlrrmHteYHtztn5Pd10r3Mjz0WSdwEcsF6sQxAfRQQbdHffpeMydfox7V7tTPPePSFcLtrcVhnj1yOmdLRW96epkFsc51yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خادمان رضوی زائر کاظمین شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/453161" target="_blank">📅 19:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453160">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📷
قرعه‌کشی رقابت‌های فصل بیست‌وششم لیگ برتر فوتبال
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/453160" target="_blank">📅 19:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453159">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cf711cfd.mp4?token=IZR5o9dyFu2l7sVpttpm_js74knOo_3Fd4ofgiVysQr_AyKOObQ200UFMkasIg3C9snSHlRJKNg13pkv_lrCHoeXyrfknZAvnuFC-NykjXoWyfT6e2Z6H-n4C3TJXRPpNGamr3-J416vFW-lsq0eLgjpVMGSq4lqNQS9CmERBl5Jg5FPQyrDvWrWfEyfGIPGSRdAaWTkEugYxqJ50pzE_uToD-HgaT77wGFsAEemGfe5i6mje8xS1Y7Az_YlxCi-vRb-NIhQnzR5anr_WE1raMsCsdMDmzRD1ZVHeT8Ln4oZ5fGusjkwW055ohz7e2kvOnEGLGEqRVHq80QCmaYO6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cf711cfd.mp4?token=IZR5o9dyFu2l7sVpttpm_js74knOo_3Fd4ofgiVysQr_AyKOObQ200UFMkasIg3C9snSHlRJKNg13pkv_lrCHoeXyrfknZAvnuFC-NykjXoWyfT6e2Z6H-n4C3TJXRPpNGamr3-J416vFW-lsq0eLgjpVMGSq4lqNQS9CmERBl5Jg5FPQyrDvWrWfEyfGIPGSRdAaWTkEugYxqJ50pzE_uToD-HgaT77wGFsAEemGfe5i6mje8xS1Y7Az_YlxCi-vRb-NIhQnzR5anr_WE1raMsCsdMDmzRD1ZVHeT8Ln4oZ5fGusjkwW055ohz7e2kvOnEGLGEqRVHq80QCmaYO6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی وزارت خارجه: سیاست جمهوی اسلامی ایران این است که تنگه هرمز هیچ‌گاه به حالت قبل از جنگ برنگردد
@Farsna</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/453159" target="_blank">📅 19:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgQNJ8_xdc7XMjnEoAdp_YkpVPjthiV3X_mIBXSo8vbpwXUDrEJwCK4Xc_x1lWxhyTbTGcnQuT0hZzWcur4Jg6sEb6YRaCvcnRD5S1R2ROK09OwlWL9uLhTuiYADrIvTvvkKr_DLD_WcCxT3JnBsCo2ABJQmgdN3LFTYjjmrAqyDv1wDZwxFmLORnjy95DiQVuz-RZLG0LkYSVomocfVCEgZFhqaRsI4rvB4ow0zj3M0mhUARLR_jVGQLzLzE87WsdORb0qYiOvrUD0GRkQ9bsyUyGwNU9MvQtmlk4MpoA6uLS1qMzhwHLm34XCyabBuDPgSu9R43zRvG4Bay4qYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3FJ1TG708lHOT_AT6J8MaRprLrqf9tX2pap2d4zaDVpCFTent9hPHM-V4xavasSB23z3rpph267Ikz-BM9Cf4yHvBv_v7DUOt-eWFrUtFGrm7qERwsG96sAqT9xtctcApZxEY0RUtMa0IrNgtJc9bw1mtwT2CwFLjdDX3zRYr-n5gHWHT-AQ5W_XvjoEz98YU20iyo9mWrMxx7S61SCrnht8vQXJCFG5dY-KnjU13Yg-n5upfKOfe95WBdOfkZjF6pEAZz6phVYupr8kwg6sBryFeiJPvAma6MMhe3BlhPAN1u9qchHyIzPf-os16xdAJXPfT-zl7YXnwqQ3iBuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N7jbEJU-FDDuwNbpWp2jnhQlCt3y6aYlCEIhreL13FfDFV2ge1Q-CqEBSfJNIYurmTlH7-2Cbex6MreAYRGsFV50IXyuWsugAb6QB_Wpkhc_Pma8x0-eBVagYkmuP1mwKaKrbG8qCv8pTAlHV92wPScKTCIOJW0M1TI2R4fUkbdZb5aED7GF8uOjISIiCtMuTM07H6GirZ3_HBidXo-UNj7NIyqtLdFUMm1a6yvlDrnHC1fM5aiUljhAxWikcrkRXf3seQKrldkjFNt-HUN1GqMAO4qxA2vYtl2FavCZEXS5azG_f1H6eo_eJqsiHKb6Lux05MPd1Ix757ImsdNfQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8UL5GCJBgroq8PC-6OX5H-yTGupg_WJ4XOWeTUrduUFZsuxYHXkCMu70FVFER33-DwwNAdgeYoqLpaZ9xOUSBr-E5yDmbmiK98ocftf6yiIrFMgNBHw8-7mVmqOO_5OEmEIOCKkECjzHBNnUY3M6EEgEleDhJgXqQ9FA2fkDvCHSZUe5AYuL3OQi9d3RxaJCrDWU8PQtaupZKKB2qA766Dd5xCeK0V2tl9RfLN-zBU56_6kTrdxfUKi1ryRGBKWkPPzVWrbeoGgsAY43m3FQi-VgK6L0rbuPwZ0LIEdpVYHxSABwB8subBKZ8o1yTOSjgoya0Wcysr-dewyOLVVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fuWWmVsL-au2wBsAhoNvp3-J7XXecPKJnBHrRRFzacd8TouigksUBQNY1uXAPTvaf6knlhpG7UDBZDPmVqaP8JUKBvde0X0YJKr3Lz0Ajt3XDeDlVon9URPY0IhL-GMYpl_PTjIEAIETaVEP-ZVWxkmASZrBAD8FMq0PF8Ya-ROaJLugd2ACXIegOUAHY9vHA3mTuRxpRmIPubK8FwqHhogHdBGyFcesL7QlYd4fHC3DZ9BsamHQtT58CJoTWfGAmaezU6y0AZhx83gjQQZaGt1YSPU4hADXtduTSYHO7OH3wQF8TNRzm0CSs4BoctlfDO13237a2sxg5R7Hh5y2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-Cv-qtw5zq3gnBqBN1QLmq12YwaWY2R56RxkX-F3dY4egikllu5RE87U-SCqBnripzcIFlTT2d1bVyYTWHAdQ3eDg1OqdOMO38LJv-Y_CAzQzohH85v77dGGp1gwJ9hl8slrdap55DzSAqR39MeyIXnScIuSF5SB8hCTXUrlr-PxoSsLINw9pacnNNkfFHtvwi_59V5aea20agK7kr73sY5didBLqcRZW31QkEN34_9u_gMoUBvSyQ1l2IRveJBSyxy4sd2L-p1O0keZQ5YeY32LIAMuyWeHBQMtIaRxjiyrJ6h_LtlNp5yrTgykvqscoD_DxFB15OLVs1vojhS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qW-tm4D8Vs4NLLlGLzT_P75w416BE4rxHNjvKey9du7B0HtleWKyWDZUpOvkt4_nhWHmCgXBzuzXL1W_dYoYZV2h4DmSJM3PCup6ULmlr2u--dkwK_QrVj6hSnsTDSgMLbIs49FltF2KFRs619iIoaOTYns_x05vm-Ys5BDsh8n-_Q6CdTMdU3kC23Sz94bvSN1ebEo-0qRz5e-TRPeqvATZCgMJlo6njsq6n5qJ9d4O2QLVKT5ZO2WeGpxGCkgZNcnVrOP086ttYhWaWJ2fTF15o_jWSelHmhJVfXSrY6m-rtnznVtDCf9Ahlww8zKiCyafYYo22iyVaNyABxRudQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سوار بر ریل عشق تا شلمچه
عکس:
فریدحمودی
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/453152" target="_blank">📅 19:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtAS17BPTbxnItG_8LYz1TaeVt8-Cx5bBSylQCa-vFguK3hbm_9H9QzThvjBIbENCWnSq4eU-h-xusa-iTkB55qsdO2Wu5RQ5wdhMzNTA0FU_cOutyAIWBNwqf-rwJpq53Igu8UZHnfFdBwEbmgvBmr1grWn8tN1fSOmpqw0BBeikz2DrfQmRf4_OBBPUUp3WxrVh5iPA0lO_EA6ERCe7tglRKdkEsOZRTgf1UkKb6v_Jt5Na88gJI5LRkdovuOBGD6xBSIRcoLWUFB0A2YUdyvVLrLRaEN-y5PSp7Q__o_Pg5HKJxWKk3q_41KRbyjWCcUF26VAtkYJ0PnQmSdE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷۵ درصد پارکینگ مرز مهران تکمیل شد
🔹
شهردار مهران:  تاکنون بیش‌از ۲۸ هزار دستگاه خودرو در پارکینگ‌های شماره ۱ و ۲ اربعین مستقر شده‌اند و حدود ۷۵ درصد ظرفیت پارکینگ‌ها تکمیل شده است.
🔹
هزینه توقف هر خودرو به‌ازای هر ۲۴ ساعت ۶۰ هزار تومان تعیین شده و دریافت هرگونه مبلغ اضافه تخلف محسوب می‌شود.
عکس: محمدرضا علی‌مددی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/453151" target="_blank">📅 19:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a46ec487.mp4?token=va667qitVqmWCxxYKD4uW_hjdWH5Vl-i23fZUv_mgpxPjMQK_1lFr5ZdKuA_GeKYndew5hruIXbVATfwXV-b3mHEB-_T6GHoF1NQ684jE0uiuRNlLc1hR_qiX21h-ftFU69aaFMSqIUdvhp0WnCLRVn1vttZ0RKEQNLnybo53pKfc_3sVzu68G0Wwb7bWWpDaU9x-bjYzO77N27DvvM4oK3i8Z-A1QOEQnOn5f63yQu7FztV5FKxKkyvuIgguIkDX90fJZXfGv47phF4tm92tVzWJVLxSGh8sSyBTi3j4-VWHYimqxaG7_0f8b6ffklh0RPFuOlVH68g5Za1IK-56A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a46ec487.mp4?token=va667qitVqmWCxxYKD4uW_hjdWH5Vl-i23fZUv_mgpxPjMQK_1lFr5ZdKuA_GeKYndew5hruIXbVATfwXV-b3mHEB-_T6GHoF1NQ684jE0uiuRNlLc1hR_qiX21h-ftFU69aaFMSqIUdvhp0WnCLRVn1vttZ0RKEQNLnybo53pKfc_3sVzu68G0Wwb7bWWpDaU9x-bjYzO77N27DvvM4oK3i8Z-A1QOEQnOn5f63yQu7FztV5FKxKkyvuIgguIkDX90fJZXfGv47phF4tm92tVzWJVLxSGh8sSyBTi3j4-VWHYimqxaG7_0f8b6ffklh0RPFuOlVH68g5Za1IK-56A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌کاران حادثۀ تروریستی دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان اعدام شدند
🔹
دقایقی پیش حکم اعدام «ابوالفضل سپاهی بادجانی» و «امیرحسین صفری حسین‌آبادی»، دوتن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه ۱۴۰۴ اجرا شد.  جرم مجرمان این پرونده چه بود؟…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/453150" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhjBzyCcjpjmD9MkpobRSyONLUcjiCGPPC4HF9aAa4KJwdRqUuqDCYFE48EqonC2GcyQeOC44oJ9WRhrSIwEQpx2oaHNjOOS5v-Z4BZ1e7kqkX-NyYObmtyfNBFjAbIWP9sK0k0jS2qpnptSZLt7qmA416w0VdO_1dBQLCshy1jgit4uTv1n4hwDgFn2YXBLWxJ6KjqkbuqDcti3dumWY4ViXSFlXJWQg-RroRdNsQ2xStcUgl-YujW2g2zHFcfR4vU1-Txfo762ofVbUb_Ewmr3SVSn5lHgcK0f8zCpr0ypq7jW6bR7gjg7N7CcVT4yAPsusoeZykM-bu0ba5WqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون فروش سایپا: پرداخت جریمۀ دیرکرد در اولویت ما نیست
🔹
معاون فروش و بازاریابی سایپا: اگر نقدینگی داشته باشیم اولویت ما تولید خودرو است و پس از آن جریمه‌های تأخیر را پرداخت می‌کنیم.
🔹
باید ۵ هزار میلیارد تومان جریمه به خریداران بدهیم؛ بنابراین با برخی بانک‌ها مذاکره کرده‌ایم تا این خسارت‌ها از محل وام بانکی تسویه شود.
🔹
مشتریان سایپا می‌گویند با وجود تعهد قانونی خودروساز برای پرداخت جریمۀ دیرکرد، پرداخت این خسارت‌ها از مدت‌ها پیش متوقف شده است.
🔸
با در نظر گرفتن میانگین قیمت تمام‌شده یک میلیارد تومانی برای هر خودرو، این مبلغ معادل ساخت ۵ هزار خودرو است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/453149" target="_blank">📅 19:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6ba917edd.mp4?token=Dtebd8EfNZGZIYo_ydkaJj2lqSJ5ldzd52-WwuyFGIg5AbPqcpMYsuGttcM9KfMhhxlnzqzr7H-6hq1b0jzcKddtlWLNrMx9CAsQ_78yEjOpNYGMPaDnGyH0T2n6qL3TfAcUIQ65ToybfSxlAfOLhUxSSUQkM1HSD9MaHARREYSAduXl6xlCnqcLiXLG9afAKDOnpFdx9wnqCnnbHx_4RoB_JtCFBN_EeApDpNCzXdEb-3sfFUaRiGFYFXd3WPMPXnfDiZ2U3UJfyI-lqPnSpceiMQfwaeAmNcRsR02aU0b_N4fDbVAMBykUJL_5hrRVx_lw_NetrTkqbsa5aI6cZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6ba917edd.mp4?token=Dtebd8EfNZGZIYo_ydkaJj2lqSJ5ldzd52-WwuyFGIg5AbPqcpMYsuGttcM9KfMhhxlnzqzr7H-6hq1b0jzcKddtlWLNrMx9CAsQ_78yEjOpNYGMPaDnGyH0T2n6qL3TfAcUIQ65ToybfSxlAfOLhUxSSUQkM1HSD9MaHARREYSAduXl6xlCnqcLiXLG9afAKDOnpFdx9wnqCnnbHx_4RoB_JtCFBN_EeApDpNCzXdEb-3sfFUaRiGFYFXd3WPMPXnfDiZ2U3UJfyI-lqPnSpceiMQfwaeAmNcRsR02aU0b_N4fDbVAMBykUJL_5hrRVx_lw_NetrTkqbsa5aI6cZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فروریختن یک مرکز خرید در ژاپن درپی وقوع زلزله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/453148" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mw24UJa4Va6e6GSp37hpjzrWZ5YsmJr1_CFabmfGP0ZG79wgH4eAca1tsdp_IVbLZHJ1m1M7mWbY3rNEPZqMtfhBGWXjd6cj5kzBSD-W1wpQYFUz9hjqeSHXAnxUCDS0dPqq4VW_tC5OoEa7LdugKeqoLSAhmVbRuPsypG1ZcVYyns5cBos1ZKF8U-adkic-HOyoLSa26aSrjC6p0zaDBN-GZTh1WC3HxZBaTH-gRVnw-YDVFkW6SCqivK-FMgFXuu1EoR_Rn-SJZZctr0Gh5SZPJTf2pgiP7Pbt86kr6atCQ5XHwVJqlY7p6g1I71XfHiD2T1ksmHgSxpsIqCEt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی این درخواست‌ها را ممنوع کرد
🔹
انگجت: کاربرانی که از چت‌جی‌پی‌تی می‌خواهند متنی دقیقاً به سبک نویسندگان معروف بنویسد، اکنون با پاسخ متفاوتی روبه‌رو می‌شوند.
🔹
این مدل به‌جای تقلید مستقیم، اعلام می‌کند می‌تواند متنی با ویژگی‌های کلی همان سبک، مانند لحن، ریتم یا فضای روایی، اما بدون کپی‌برداری از شیوه نگارش یک نویسنده مشخص تولید کند.
🔹
این تغییر در حالی اعمال شده که شرکت‌های توسعه‌دهنده هوش مصنوعی با شکایت‌های متعددی از سوی نویسندگان، ناشران و دارندگان حقوق مؤلف روبه‌رو هستند.
🔹
شرکت اپن‌ای‌آی جزئیات رسمی درباره علت این تغییر منتشر نکرده، اما این اقدام نشان می‌دهد توسعه‌دهندگان مدل‌های هوش مصنوعی در تلاش‌اند میان توانایی‌های خلاقانه این ابزارها و ملاحظات حقوقی و مالکیت فکری تعادل برقرار کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453147" target="_blank">📅 18:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969b353542.mp4?token=YCtee1_TDwezSORp_JWz0bo5LIvrkzxLkpAFL5J_RXXMbKP21Fcs0hX55ynoKNgMkBgjQwpOSCO_t7oRYU5YLaVBEyexib8IJhb3PVEGTX4gpl_UguSxpN0CTweIlW721rBIPn7tbL6abHT6wypWqrsTf-yTnNvdygIfGP7NJF9ZyYHNbw3JClOGUZJ3elnkDN964_gPzxALmb4DzC0VQJhSywurwHQxx7n8ofGLJzBRVQxQFtGrizBtGwG0NOehqPUBPiEmCEWNiZ7OVepFQHIpkCDP3t2L0wae72QIn2ltcmYds4gnuGGrDytHhW1OjQT1Zz-foLnCS6xlajjKag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969b353542.mp4?token=YCtee1_TDwezSORp_JWz0bo5LIvrkzxLkpAFL5J_RXXMbKP21Fcs0hX55ynoKNgMkBgjQwpOSCO_t7oRYU5YLaVBEyexib8IJhb3PVEGTX4gpl_UguSxpN0CTweIlW721rBIPn7tbL6abHT6wypWqrsTf-yTnNvdygIfGP7NJF9ZyYHNbw3JClOGUZJ3elnkDN964_gPzxALmb4DzC0VQJhSywurwHQxx7n8ofGLJzBRVQxQFtGrizBtGwG0NOehqPUBPiEmCEWNiZ7OVepFQHIpkCDP3t2L0wae72QIn2ltcmYds4gnuGGrDytHhW1OjQT1Zz-foLnCS6xlajjKag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود زائران ایران از مرز خسروی به منذریه عراق
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/453146" target="_blank">📅 18:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=tygRtYJFwUfU0Lcu3erZMzyh_8iP1Lw8x0_KdItweOFhLHMeYP4AXmE4IStkOIFjnb5Tz1dmHb5Zgf70FgO46FDI0i5cNCmpnP0BE2DjFRlQV5_IJgb-96eIydNxge0G6UIUCIRsCaEuh787Diw5Ji9ldrre6M3lWibRL8MELvIRQa1CC4NPdZaKfyWv9HWZ6GTJScdC_hMFv8m37SI06QYbfRvYkF9zTesuQNzTMlj4RXTg-gsXLLoPta2jn6gEZv3zPTTK9I-SnsmUfbnDb5sOa8HV9DpzxWyR5oVVuqlZQEQKkSqGrG6sH5guYP1o5hpETzxe1zGGywsqqcKifA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5691cab0dc.mp4?token=tygRtYJFwUfU0Lcu3erZMzyh_8iP1Lw8x0_KdItweOFhLHMeYP4AXmE4IStkOIFjnb5Tz1dmHb5Zgf70FgO46FDI0i5cNCmpnP0BE2DjFRlQV5_IJgb-96eIydNxge0G6UIUCIRsCaEuh787Diw5Ji9ldrre6M3lWibRL8MELvIRQa1CC4NPdZaKfyWv9HWZ6GTJScdC_hMFv8m37SI06QYbfRvYkF9zTesuQNzTMlj4RXTg-gsXLLoPta2jn6gEZv3zPTTK9I-SnsmUfbnDb5sOa8HV9DpzxWyR5oVVuqlZQEQKkSqGrG6sH5guYP1o5hpETzxe1zGGywsqqcKifA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماینرهای غیرمجاز یکی از عوامل اصلی خاموشی‌ها هستند؛ گزارش‌های مردمی می‌تواند جان بیماران را نجات دهد
🔹
مصرف برق هر دستگاه استخراج غیرمجاز رمز‌ارز معادل مصرف حدود ۱۰ واحد مسکونی است و ادامه فعالیت این دستگاه‌ها، فشار سنگینی بر شبکه برق کشور وارد می‌کند. این موضوع می‌تواند به افزایش خاموشی‌ها منجر شود؛ خاموشی‌هایی که علاوه بر ایجاد مشکلات برای شهروندان، در مراکز درمانی و بیمارستان‌ها نیز تبعات جدی به همراه دارد.
🔹
شرکت توانیر از شهروندان خواست در صورت مشاهده نشانه‌هایی مانند صدای مداوم فن‌های قوی یا مصرف مشکوک برق در همسایگی، کارگاه‌ها یا سایر مناطق، موارد را از طریق پیامک به سامانه ۳۰۰۰۵۱۲۱ گزارش کنند. این شرکت تأکید کرده است که هویت گزارش‌دهندگان به‌طور کامل محرمانه باقی خواهد ماند و مشارکت مردم نقش مهمی در مقابله با استخراج غیرمجاز رمز‌ارز و حفظ پایداری شبکه برق کشور دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/453145" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BowcOedkSXEDJMcstp5m814lIiFTfCeE_gYAkiSSyV7eWlA2fjTOqvCyKJlDAlBqnWA5tWD4NuSkpXn5uGR6o_wHdpESrLmTCMRpTEBKAF6hHLnbpVaEBBvI_kWn3guxr0blwG3zFqdk32AynN5jAeQXXJ3LTkAy5TuBs8NtfyNXMTqrLOZKoEF3P7IlC-7fVyDDM8geE-d1ORwbQB3OFGnP8OKR51SjO-30fMhesnD1InCcMbcD9LztmGbry6sE-6zuNbVDTbeMzQjz4d8Ndk1k0XDN5QEt8DQt00VIaQukhhZyrIE2lUxe0V81SmSFr7IOtIIklEHn2xoyeQDhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه حال خوب بساز...
💦
مرداد، قراره هر بار که به پارک آبی اُپارک میای، یه تجربه متفاوت منتظرت باشه
😍
از بازی‌های گروهی و لحظه‌های پرهیجان کنار دوستات گرفته تا هدیه بلیت آنلاین و برنامه‌های ویژه‌ای که فقط در مرداد تجربه‌شون می‌کنی؛
اگر دنبال هیجان، تفریح و ساختن خاطره‌های خوب هستی، این ماه بهترین فرصت برای اومدن به اُپارکه
🎉
🎟
برای تهیه بلیت، همین حالا وارد سایت شو</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/453144" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/453143" target="_blank">📅 18:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYUb2E-CmCX2vzl6C6YCybdOQsT0syIar_pWWHk9Yygp8jTSATK56alhdgz90YeBBe2B785TXovEZRbNEvsQDF6IL3BlPYHTJtFPZCJI6fgzaHMSLa0XmPuEI_D482TE6VHG6UHjykarIiTL5149cipjeafE5K_HrwAlgZ-wncsoqamrjr5d202fLH-l3JVZlUM4YzwuHglG985r3SsOiWdJ4YGSjRV-TNK8QOfnOGYPkCQbrO9I_IxDzQ6nl2FQ0tIQZuzRgxeW2BBzkfp242wcr2BkFqsP-RvD8Dw_FjTIfW3QWn7CYHX9nR0q0N-yDhHZgblMCjg0XbSMO7VGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام آمادگی یمن برای گسترش جنگ با عربستان سعودی
🔹
عضو دفتر سیاسی جنبش انصارالله: یمن در حال حاضر عملیات شکستن محاصره را آغاز کرده،‌ ولی آماده است این جنگ را به بالاترین سطح برساند.
🔹
اگر محاصرهٔ یمن برداشته نشود، نه مذاکره را خواهیم پذیرفت، و نه چنین مذاکره‌ای ارزش دارد.
🔹
عربستان باید به حاکمیت و استقلال یمن احترام بگذارد و پیامدهای هرگونه نقض توافق را بپذیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/453142" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-3OJDEWcVDmwww73gW6eeAVkcCeWp3CwHpt9mEU82KKUQTggTk67NZlxoMYpQ2o2Q5pI4zJuqvEIZPqrXwfCfjV4dP39uo4w1AtSExkq3shifZkziS899GfN9NdzHnMcluQFGdrE1B7zIXJ04mNSsrZEweGYeICpy182BsML3dAXat_HYHd2bj5nYpbWceSzD9_8K1SJybDhW43R3ag_DrLhDtxxit4QlA6iPZNyFyllnZj5sWLA3oKGCw7SNyxi7jMmumz02GZ2sbWAGsQMeZCzHtIKG-2TmibC2dF3JYmn8pBK8i51KATI0-4ZXAeCunaUTGfaUI8uvSa6bS5Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBtbWqV3grw6mGDombmvv4OD3meYXPKziRFTzwzIbJUsD93DbPUAsEuYkhL7iEB2zrDWwVo86Bp-Dzaop_jGwHsuJz5s2kjz0wk9QbsS1h6wNStOA3R1FY2NpOC8eA28IpqoiltVFVyo-q4w_LWT_1aoUckB_nA3xc8Uk7GrHRzb5rnCGQZX83gelzlg5P7NPdCAJxINgWYTrFtNcaJfzp3OsPKfcb3FeF-7pv-oXhbptAq4gFTDv5F-__vzS6wQwZbcoMIpisLskntyBvW33ByVXFMx2ByRKKn4Y_xC4GqN6-DRC_0p65ojq-HwHxoJnvNsXBfAHlJ7dMm2iXUwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoWGXjRMDOEkoDeFpDT2XfQRdzpZ-H0mNjnHkjhZsk11McRDeU3PQ9-eWAuO812kA5sf9OjimVBfNHYp6m4i5uBCvSbD6LIJR13ocQPZe-23HEHz8uQ_CUKgoBjYCWlrpTK6oTpF91LSyX6MaKChqdXXnOonrD7Viwkrit8YhR8GlOEMSx51wim_PZ-0mH7RcYRe0pKBS4qcwdfB0mQ4hCCyFpDNG3jjE5sNvQCKZrhEP87R2n9pR7ErDidWfrTsLiQV8k5tc7t8cYXVXQVsBKkBv_kw5T6InEPepNzBya_2KhgwK8cWwwmoZgpTrD_TNS-b9c41G2CKpfz22OuoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRzBpQl_eFNN9HIhXLKBpCtlsT4Va5yFBm1sE9BnUC07Qv4j8F8aSteqOjP0SqdpuPKW34elLbOSzLpfBnqQCDYN_ksd5GAjzY7PyqnX79C7ayocghebKCt4erJQ64_QT11vLnlSd4BTH60sFPezJlXQCfQ8gQYsc3Ehh2VJ8WEb2IwgoAdiCwdWAExo6aY8GEjqhRDFybWo-UYMsawmVaNIjFTnyCMR-zmeGAV0S87ewOSo9F7lwVdKjEkpGqeaZsCrjW52K2aB3ELPDPjT1-pvjDi0ZPFaWDlT3OZmEtvMqStuWcB34H0sLC1qYwjuT6L0kQ1ytXtkOBIozVqSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTlpD_sNzlUyCTjWD8ALkoGStx-VtXyISSL0R0eQYhpeKZpPsoCln5j-SqE00fce8Y9gkFmaHflULeqiSBCWh9dum1KwInZshSWBZAXdAHq8rEquYJ9FO4W1JTMqaR4FcAR-zv6fxIbVFmcNPcfNV6039_gOHeRdlMyTwVneFwCrc28kaNVNX34xFvIU2uyc61bMmDK8puPu-kGZ_ho4T3BZJekVY69yljWaxztrKZePOu1iKQHr0dRQKT1LWUNkudeWIrzrxOFbqwB4XOj-H07ytceXE0UbEBdTR_lXNiks0PhTPvfIUESRB8wE4arBIBA0noKPAjdPAUTfSNwlYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjXe3wGprEcN7bljYjEX0ZtiF7xKr6_h8p-QJkVWHmSmAgl99hes2Dgixu10ebfTdw0vrrgBOVlNHZ2n13kKYsg2IAH26mql7EkA-mlcbYr-X6qm4ecNYsHYW4FM51309NVpj2ehgXhOn5qlzMmYvKwhpOFAFE8FKHJkJchj9rPA7e0mvZRl8qhhrKGQTO7DT2EBlkcnPjR77w257tHtqJ8bIAM8xJXXziaIhs1ZAq7wlXzYvuBdy-Tk7ui0fswuiVVCNReeHybb5kuvpUDxQQ6J-fI8cMvQMKoPWsun9G4rjYnU-VGJwhzb2oQTbB81SapJPJoYSMOL35I4Qg5MTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8ftYq5MJjYSrL8AMK8gFg2PTTzIzWKRZkyhOASXpNU3_O_3PkNvr32lh5gMUdAZiWRRI9ONZgHXEeBMI1v-_Whb11DK-XLlvaH5iXf9jlltKlERttvALkWCEnQLRg3xVhtWSuiTfV7yDysvtp0iYN43WQk4Fw0xSYnGXtWUnnSm4tjXQPRnj7N-eKdCivDoa_QhvrfCgZ9BMw29gyq9kAvff46Kah4zncs8W1InnOZQwHo4OjyXgG5VbBiFK0bDZfc7kqTX3GUXcMFuQddIdJvcPTo0MDesGfpkm71QD3ejoitrE5mVxewyr91X_v9X-FE32QaQ7Bw4qiFCJB490w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قرعه‌کشی رقابت‌های فصل ۲۶ لیگ برتر فوتبال
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/453135" target="_blank">📅 18:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdcifSfYQzkorYQ_pYHOmHHNIW5YZI7rXakC9WKD4WfmI6L6jDu23wOpyQalXegYjBzuuuU2KK6ESoIKUeyNKXs1PduZXNnywZASQRpWjD7uog5jWp14vfgRaBajspPymDFusP4ZC1Kub_knpt6Jl1dLYKwwnZwD6DmuDnR2-FBaT50qj9j5QECHoGVwMy4QB86vqHNkANqoQRv1qCOmbrjWus6KZUAgE0UcbmfGnRti7TQ_tSlyakAL8kNI0kRtHBZK1wmdan8g5TryW1P8eio_SmGcBqy4gFngjuPmMkH8jnbhfpOMC-ZnQTCNywtCrfrr7sEIoMXWvMdmonEqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع:
خطوط تولید صنایع دفاعی فعال‌تر از گذشته است
🔹
سردار ابن‌الرضا: کسانی که گمان می‌کردند با هدف قرار دادن مراکز راهبردی دفاعی، صنعت دفاعی جمهوری اسلامی ایران از حرکت بازخواهد ایستاد، امروز با واقعیتی کاملاً متفاوت روبه‌رو هستند.
🔹
توسعه توان دفاع هواپایه و دفاع دریاپایه از اولویت‌های راهبردی وزارت دفاع است؛ باید بالاتر از لبه فناوری بجنگیم و همواره یک گام جلوتر از دشمن حرکت کنیم.
🔹
خطوط تولید فعال‌تر از گذشته، فناوری‌ها پیشرفته‌تر و اراده متخصصان و دانشمندان ایرانی برای ساخت آینده دفاعی کشور مستحکم‌تر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/453134" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4e97c860.mp4?token=mFOFyjmtKeXCUYmv_rhFQ8xNl_ZJt7rAazUhItprxeBQc_ViifGxaYEscb9Zw215oF2VgX1XJsnN1YT62pqvJXytKUqi1_2-hXscvDDbeDA3gkxoqymmDca2T4MUt4RShJSUJzHXHWODLimA_h9X0aUOwBywtKjH6_YJs89_imjkjW8YBjaS5sZ2Zq9sz-HSvkWzE6xHj0JOVEqSPvTks2JZJXM3xjY-0zfUDecnX-WpIJL6thZxhC9lUijDykN9SKxvPnglnvnXMedAcseZ7J8WqT1qfNMPX-oB0TXLJaGn3fgEjBmw0vloeSWr9PkEce3odQmhtqlJIdZ82GEXWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4e97c860.mp4?token=mFOFyjmtKeXCUYmv_rhFQ8xNl_ZJt7rAazUhItprxeBQc_ViifGxaYEscb9Zw215oF2VgX1XJsnN1YT62pqvJXytKUqi1_2-hXscvDDbeDA3gkxoqymmDca2T4MUt4RShJSUJzHXHWODLimA_h9X0aUOwBywtKjH6_YJs89_imjkjW8YBjaS5sZ2Zq9sz-HSvkWzE6xHj0JOVEqSPvTks2JZJXM3xjY-0zfUDecnX-WpIJL6thZxhC9lUijDykN9SKxvPnglnvnXMedAcseZ7J8WqT1qfNMPX-oB0TXLJaGn3fgEjBmw0vloeSWr9PkEce3odQmhtqlJIdZ82GEXWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از تصاویر زنده پیاده‌روی در مسیر نجف به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/453132" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f7b48f9a4.mp4?token=gYQP7ZhS6JNLzihq4VVnT6QjczzEStO_PmVp7bqHw2SBotRF5Bhks0ehwx87ygHklFMIFB8c5oqOLi1Q5tE-pgKu5vO2GWu5KzARKa-BIte5qVY7U3lg7vqhoo5QyvGJxE5nqnBy-XAHHpFM6SR_z2oxObS81ODsgx2aYB_IpfdWBqsGkJsGOn_qkcKgX-GIZsbTu_8YoghS3D6mhVc2akpKdy8rWp8OfXles29hTau3Ba4lLa8o2NmrN_EwzL9GAXyo-2GKBYsb1yDNcpijzMNWYXEpWQDyW2NZY1cFq2plGxTkoQRueD-M3M5Ees_8X8mmUHp8qXAncXoR0Spltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f7b48f9a4.mp4?token=gYQP7ZhS6JNLzihq4VVnT6QjczzEStO_PmVp7bqHw2SBotRF5Bhks0ehwx87ygHklFMIFB8c5oqOLi1Q5tE-pgKu5vO2GWu5KzARKa-BIte5qVY7U3lg7vqhoo5QyvGJxE5nqnBy-XAHHpFM6SR_z2oxObS81ODsgx2aYB_IpfdWBqsGkJsGOn_qkcKgX-GIZsbTu_8YoghS3D6mhVc2akpKdy8rWp8OfXles29hTau3Ba4lLa8o2NmrN_EwzL9GAXyo-2GKBYsb1yDNcpijzMNWYXEpWQDyW2NZY1cFq2plGxTkoQRueD-M3M5Ees_8X8mmUHp8qXAncXoR0Spltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانش‌بنیان‌ها چه سهمی از حمایت‌های ستاد اجرایی فرمان امام دارند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/453131" target="_blank">📅 17:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">برنامه دوئل‌های ۴ تیم مدعی لیگ برتر
🔹
هفته ۲: سپاهان - تراکتور
🔹
هفته ۳: استقلال - سپاهان
🔹
هفته ۳: تراکتور - پرسپولیس
🔹
هفته ۵: استقلال - پرسپولیس
🔹
هفته ۸: تراکتور - استقلال
🔹
هفته ۱۵: پرسپولیس - سپاهان
@Sportfars</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/453130" target="_blank">📅 17:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29de00b4ed.mp4?token=i2PUsP_Ln71SULSshXSA9aK9TL84adQKae6UHk6Iat7iI-eey7TjMd1-8djqkOlrgL6SGD2S6bHGPzAtho_YyTh6TXOJE5Xrz_oorPrnDwyE3P_RQcdM3gqTwa6DA1sHVQi07nL-BcPPlR4LozW8BnNxcR9gMqmdqHnMHg7WO_S7-8_6bU7IIIv83N6ONr5qS9fAoVRbgxdH2_ioqLeZKeq_CDZzOQ7bX2MztxymIjTjlKESmZQ0P9f83BWW9MgGJxYxPxV2Z-U-8zd_hlzrwcXrn4juo2FmteyE-JHXq0adArJ4G5I4tgaVTWYiwqm273I0NvcPMX2xMWbPFkIiHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29de00b4ed.mp4?token=i2PUsP_Ln71SULSshXSA9aK9TL84adQKae6UHk6Iat7iI-eey7TjMd1-8djqkOlrgL6SGD2S6bHGPzAtho_YyTh6TXOJE5Xrz_oorPrnDwyE3P_RQcdM3gqTwa6DA1sHVQi07nL-BcPPlR4LozW8BnNxcR9gMqmdqHnMHg7WO_S7-8_6bU7IIIv83N6ONr5qS9fAoVRbgxdH2_ioqLeZKeq_CDZzOQ7bX2MztxymIjTjlKESmZQ0P9f83BWW9MgGJxYxPxV2Z-U-8zd_hlzrwcXrn4juo2FmteyE-JHXq0adArJ4G5I4tgaVTWYiwqm273I0NvcPMX2xMWbPFkIiHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده هوافضای سپاه: سوخت پیشران قدرت موشکی، فریاد بلند آحاد ملت غیور و ولایت‌مدار ایران است
🔹
جمعی از کودکان کرج در روزهای گذشته با ارسال نامه‌ها و نقاشی‌هایی برای سردار سیدمجید موسوی از رزمندگان و مدافعان امنیت کشور قدردانی کردند.
سردار موسوی نیز در پاسخ به این ابراز احساسات، پیامی خطاب به این کودکان نوشت:
🔹
قدرت موشکی جمهوری اسلامی ایران، ودیعه قائد شهیدمان و میراث سرداران شهید؛ حسن طهرانی‌مقدم، امیرعلی حاجی‌زاده، محمود باقری و شهدای خونین‌کفن هوافضاست که سوخت پیشران آن فریاد بلند آحاد ملت غیور، بصیر و ولایت‌مدار ایران اسلامی است که به لطف الهی هیچ‌گاه خاموش نمی‌شود.
خداوند نصرت و پیروزی را به ملت ما عنایت فرماید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/453129" target="_blank">📅 17:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یارانه ۳۰۰ معاند خارج‌نشین قطع شد
🔹
دادستان کل کشور: تاکنون ۳۰۰ تن از معاندین خارج‌نشین که در داخل کشور یارانه دریافت می‌کردند، شناسایی و در کنار شناسایی اموال این افراد، یارانه نقدی این اشخاص قطع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/453128" target="_blank">📅 17:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmfwJWw54Bc9hnnHDBgw13stOukoT7WKUIW9sdzYyA8VdseUin1dfqCYrinSMjjLKQvdaWrjKEnwnCUPXTcbt8Dml5W7RhGzJaWRymFErbVjMgywtFb3y3XcwiWhfQY3lw2_w9oS04hqG1ekp9tL_3LCoyhA8Pi_Wfu41ObGb0cNJ-wSWFS4j8YotRBwYEIGP-NhOCaPNqM8Y4lEGr50Kebi91osi9E9Yqek4WvJ8hWmKcSnP7av13Hjq4OlS_jTk70C2SFPUv9JLJ6OUjgLTDRs5UWdVAPgKMKPGvELFv5iwWgxd4SzZ1oE2yp_yDWGS0FbQGrfuwr99mLtGLOERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محبی سرخ‌پوش شد
⚽️
محمدمهدی محبی وینگر ۲۷ سالۀ تیم ملی با قراردادی ۳ ساله به پرسپولیس پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/453127" target="_blank">📅 17:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دادستان تهران: کیفرخواست‌های مربوط به جنگ ۱۲ روزه به‌طور کامل تکمیل و صادر شده است
🔹
تاکنون ۱۴۰ پرونده مربوط به جنگ ۴۰ روزه منتهی به صدور کیفرخواست قانونی شده است؛ از میان این ۱۴۰ پرونده، ۲۳ پرونده مربوط به جنایات رژیم صهیونیستی و در رأس آن شخص نتانیاهو است.
🔹
همچنین ۷۴ پرونده نیز مربوط به اقدامات دولت آمریکا و در رأس آن رئیس‌جمهور این کشور می‌باشد.
🔹
عناوین اتهامی مندرج در این کیفرخواست‌ها شامل افساد فی‌الارض، قتل، تخریب، ایراد ضرب و جرح عمدی و اقدامات تروریستی است.
🔹
پرونده شهادت رهبر شهید انقلاب و خانواده معظم ایشان و همچنین پرونده‌های خاص دیگر مانند جنایات رخ‌داده در لامرد و میناب، حداکثر تا ۲ هفته آینده به دادگاه ارسال خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/453126" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9Y5ZKZKW425vKHHKmRkQYAMgVx8Olz_gzUf8MavP3yfJ98nhMjJkIKKWw9kAz_G0ADaQoGOMpy_mjEtwjiyW_Rra8TIX-BATlhUvAy-e87SlCwsPvTDhB9bxyU7VI7vMXn8SoDMej2YB75Grf_M98NFq7QymecATS_hN16Pse24C5hCEl-hy8ApCb68Ni-s4QNsIv5IOdsdND9xz85zhDVkINr4pzw0NLimOxAXIZsP-B4EvNWZHVGD3kwlRVQKHaeYCUZl5-dJHoZMcYZVC_nelU1Q9IMFgmA2vx0tCwRi-Mv2n8l4PPa_AMVcdIj3b524Mzwe0siPpxea9rMnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره سراغ تهدید تکراری‌اش رفت
🔹
ترامپ بار دیگر ادعاهای خود علیه ایران را تکرار کرد و مدعی شد: «اگر ایران با ما به توافق نرسد، ظرف دو ساعت بیشتر پل‌های آن نابود می‌شود.»
🔹
این نخستین‌بار نیست که ترامپ چنین ادعاهایی را مطرح می‌کند. او پیش‌تر نیز بارها گفته بود اگر ایران توافق نکند، پل‌ها و زیرساخت‌های کشور را هدف قرار خواهد داد؛ اما پس از مدتی مدعی شد حملات را به درخواست برخی میانجی‌ها به تعویق انداخته است.
🔹
ترامپ چندی پیش نیز تهدید کرده بود در صورت هدف قرار گرفتن کشتی‌های متخلف از سوی ایران، زیرساخت‌ها و پل‌های ایران را هدف قرار می‌دهد؛ اما اندکی بعد گفت اگر چنین اتفاقی رخ دهد، از محل دارایی‌های بلوکه‌شده ایران به مالکان کشتی‌ها غرامت پرداخت خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/453125" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ترامپ: درباره کوه کلنگ نیازی به نظر نتانیاهو ندارم
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در مصاحبه با فاکس‌نیوز تهدیدات خود درباره حمله به کوه کلنگ را تکرار کرد.
🔹
وی با اشاره به ادعاهای: من نیازی ندارم که نتانیاهو این را به من بگوید. نتانیاهو این را به من می‌گوید، چون می‌خواهد که من همچنان درگیر جنگ باقی بمانم.
🔸
شنیدم که نتانیاهو این موضوع را اعلام کرد. گفتم: «چرا فقط به من نگفتی؟ چرا باید آن را به کل دنیا اعلام کنی؟»
🔸
من دقیقاً می‌دانم که در کوه کلنگ چه می‌گذرد. این مشکل بزرگی نیست. اگر به توافق نرسیم، آن را از بین می‌بریم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/453124" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ey3m7ChFlIKeEyibK0x6FtNZy8VxcmTpSY9aEWTXgoVbzw-vm1f9L5DgXVAcRSWcbyV255b76uM8fbia37x2SISYkANmhirPIA0j2lez4Jh4MO2yhBFKjbWD48YVya6To0xz6EtHr7aLp_IZtLLLTpoEzvFtFQ6mCwIz0MQMJUem_hA-cUQsB9QbLToiL4lu9KAUCDkqRdqz3rRT5JLTsrcfhGAMAd-iNJ-MauT7GlNNWQLM8eZWJXYjRfYTV7IQ6UHCgtss17iqte7UIBRtqla1MuifE-T0TaZjUFHryQa2saCM0ZX8TIeZDc1aU6QcmfywAHT1Rcpi3oeUFEALtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دربی لیگ ۲۶ در هفتۀ پنجم برگزار می‌شود
⚽️
قرعه‌کشی دورۀ جدید لیگ‌برتر که باحضور ۱۸ تیم برگزار خواهد شد از دقایقی قبل آغاز شده.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453123" target="_blank">📅 16:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gujTDWiWzofkuDXxjyCEF6fZEn2DbMHayaAVkDJ69XFVKOZq7NsJbp7QBV7xUNBuBfXeSjdGDPo5H2hzgIFvh3AKykQiSHvIwIOo3_805XNZ-8UupGeoyIFNWHZkAbnufl5eZpenWcwA9aPEu7EzSyAz56L5v4phJEP6O1EnLe1Comow8Qnp3Qw0NuXZvTPOYO6vbVSoohscwff6nMFXDtzhfs1ToEC9I1DI5R1JWMgjTPISzk-jyineY-DwlkmGZ14JCFu3lwvf0LjkgzUGIUXVCZbgJWL4LfRr-sLK1uAqBjvmHxmbrQXqE5QHtTVLDhdz96mV4mNCysbTZCkoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر من رئیس‌جمهور آمریکا نمی‌شدم الان اسرائیل وجود نداشت
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/453122" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad321b0c7.mp4?token=IVHjd7VaYNAFodDJQtmvOlVV1OqfVpEFC7eWLshChsf4kuSQ9h9T1MTXzuRgYCRMXsu7N5SfemdjO4Rh5-D0KsqJfLMhC0FVCkwWelVQ-RLsHrrUOszosohGpyk9HznpMZOSpde1P4wr2yivnbFCixKqHrEppuBo2490g5riXukfJ7OtvQeR2BjxoH3fEK94jSP9joNAX1moGiiT9o--vv1deyFjaHmlRnbyKqWBRS8oePT3qFxQ_LG2Asb7CFm8GYWmEaE4V1GaTP8RKrUOqxIM22JPZGT46-nyKwhh5ny1EwPCl3nw16lkeSlbKcY2z6IrTabOpubNpavSLofpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad321b0c7.mp4?token=IVHjd7VaYNAFodDJQtmvOlVV1OqfVpEFC7eWLshChsf4kuSQ9h9T1MTXzuRgYCRMXsu7N5SfemdjO4Rh5-D0KsqJfLMhC0FVCkwWelVQ-RLsHrrUOszosohGpyk9HznpMZOSpde1P4wr2yivnbFCixKqHrEppuBo2490g5riXukfJ7OtvQeR2BjxoH3fEK94jSP9joNAX1moGiiT9o--vv1deyFjaHmlRnbyKqWBRS8oePT3qFxQ_LG2Asb7CFm8GYWmEaE4V1GaTP8RKrUOqxIM22JPZGT46-nyKwhh5ny1EwPCl3nw16lkeSlbKcY2z6IrTabOpubNpavSLofpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قرارگاه خاتم‌الانبیا: هر کشوری که از دارایی‌های ایران مبلغی دریافت کند اجازهٔ عبور از تنگهٔ هرمز را نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453120" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030d73d41c.mp4?token=YCDzWaShW2BwyO4-Gi4U2-2Y5090aKMyUxZe7SrC_YvBKYoCzzpJh-Cs9Pfgg6daJGGqdtGF4cjlOaSKkKAfqTDSYbDqROpTskEZHGGNSS89X2Baq3UZxe_gWYbbz5_s1anu5K6pTaKrjKb0e9VIKfoq0_uY7FdHt_PiO6QFsx_TqR25hAfGHwhRwc_7GXoMcVBxtoxmGzG7Nz5nUqpRM2o-m_9LBsPyDYYNYLbmY9KJBtih8slWa2RYAa0l9Yl03L8yQ5-NWP75GspV01KOofug7LPUlLT3U5bthC0YLSBrUVcn--fxn2gq1MmwePZlmUIG11SImnxd1GJCV8OlFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030d73d41c.mp4?token=YCDzWaShW2BwyO4-Gi4U2-2Y5090aKMyUxZe7SrC_YvBKYoCzzpJh-Cs9Pfgg6daJGGqdtGF4cjlOaSKkKAfqTDSYbDqROpTskEZHGGNSS89X2Baq3UZxe_gWYbbz5_s1anu5K6pTaKrjKb0e9VIKfoq0_uY7FdHt_PiO6QFsx_TqR25hAfGHwhRwc_7GXoMcVBxtoxmGzG7Nz5nUqpRM2o-m_9LBsPyDYYNYLbmY9KJBtih8slWa2RYAa0l9Yl03L8yQ5-NWP75GspV01KOofug7LPUlLT3U5bthC0YLSBrUVcn--fxn2gq1MmwePZlmUIG11SImnxd1GJCV8OlFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«نوید» هم در «محرم شهر» حاضر شد؛ دعوت ویژه عوامل شبکه نهال از خانواده‌های تهرانی برای حضور در میدان آزادی
🔹
همزمان با برگزاری رویداد بزرگ «محرم شهر» در میدان آزادی، عوامل شبکه نهال با دعوت از خانواده‌های تهرانی، از آنان خواستند همراه با کودکان خود در این رویداد فرهنگی و مذهبی حضور پیدا کنند.
🔹
«محرم شهر» هر شب تا اربعین با اجرای برنامه‌های متنوع ویژه کودکان، نوجوانان و خانواده‌ها در میدان آزادی برگزار می‌شود و میزبان شهروندان تهرانی است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453119" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⬅️
با مشارکت شرکت توسعه گردشگری شهرآئین بانک شهر و معاونت فرهنگی جهاد دانشگاهی برگزار شد
🔴
سفر کاروان دانشجویی زیارت عتبات و پیاده‌روی اربعین با مشارکت تی‌تی‌شهر و جهاد دانشگاهی</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453118" target="_blank">📅 16:27 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
