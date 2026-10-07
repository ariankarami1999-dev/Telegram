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
<img src="https://cdn4.telesco.pe/file/seWo4KNzTNqOLr2RlujRDogO1mhYdUARB6CO1L05YV-_8mUW25AL4HV-r3NIYCujKXJLMihCaSWzhFOT544PywaIffKK2yV_LeBazTX29bClhVFTD5nJPUDx-Ly3Ei_FNy8Y20r6hd0cNHlQBnK_lfJp5iN3Zk7zpoq-pVV555DlrARwVqZcQZOQYM5yW0ud86DDSlfzbLvKfV8L9oybQRQ-lvEE3IcMTS1UyCPsSsQPlGuM9BnRT-tRiVJiYOdRSjsZdJ9DIUm7CI-gJyIf37ZadT3vGVy8qNZfhKXL6rl9hC5JbmYDF57Yw10at5Usl590tAnJvCXk7TjlxTwIgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 503K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 06:03:32</div>
<hr>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCSSbCNPMwYS3UkYCWUE5tjOFkwajw0nTRBKiDbNV7fxu2Nlhc7DaXy9tvazjlHG86HWyCmdlsuJDN6VL0W8WjVSUZDJUFiiEjCbK8ttaw75bfJocSvk3ZHbbRj6jTycDIRtFqlyeRa4Jt6vg9Ccast87l9D-eC3BsCo0jM7_qgorEB6ArPQOd_cu18YmHlsFd0oVbZzP2WmS63xg-a1R4NZQVZo83IHPjjTtRjP-Q3GBoPFN7OZSGpe-8Og4fFSL0-Kprr_M0eLd5fbTl1t6EpyL_HYjEcMJ5eB22hYvPgdxek-o5h8CvjP6Th5oViSNSSnFX_2DVK1qUsNRVplBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdPZs12Fwqw2IXAFC89nfVdC0HKjPo-AspWpnnLOSvPOBQ8JRGyGN6nX87x_egfasxuBsrDNqkJ6M3CNeVnA9uOmEfj-j5TlyMBcIuEcVnNLQYHDF13QvwBT8YyLe91h2Xb7nh9GzslCb4kltRGvnRF8rNw0i4jfeUoxFvviPNFY_kaRoJS7ALBqoHp1Usjx1myXHyeK1g2e05L6edt9TTztDADrYo4IPFbnvrIGo11_0pmr20fh1fFC6JZV92xNKESvGSaQeww09VVdX6NliKL_DyFveMOe-R1ws3_FtuA5dxEg1zpJoL0WJPp4boPCZQuwuQYxz0CLz8Lot_1DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpBCW2GjAoY7iv5Q6Bn3G0qFlsbqn8x1_0UrsdU4TemaYgcZLw7_3dm15ZEkqjyXTBSKvk81_f1DRQNN1cN-zLB74oMp6WmFoQ59x6iz4TK9QAZA8VupqbJI111qyOcCwWqtnkZ41aJuSFwCkxB5MET5QN2lgz77TN9PU2XWcPw0ncuz5lFPWlGnXDBduYLQ7KMp6VV8-JP4dehd3-ysukMGEYh5SxA4eGe8zHDWD807aMam4Hhv81B_6H1JCVwbneFfubSas7HeUhiIizQ7cPhe6aYeOl1nS2XhRkkVmSl3RgrGl-p_3Jiy8wmx4Dos88JH3PYIPdGa5xXl2f6OEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVxSbQNWOM4MTFtM-l_zT2BxBv1G1oQpiRitJr9rQrzMi4g1ikafm6cEgKXPdd48mONTHny2TNVZdj3YBAhI77DYE48kZm7GKhnMubMvuF6vDh7NVqd5U8oX5RnzxV5TzpZJ96jL1h1XiD7t2kpLw9zFn3ocQqz2zFH1NIzVa3HPU4LrNHtZMnhmyySE94DThRISmh7TkwBhdT9dNH4YZcp5bvXSSKgNlvL6eLh3KviC8XorHqQEED_uijnvdmtV3jkv6D1JBVd_Plf9DOqxMWtoCfBH8Jx31Y28-uamyomEtrsjAzpPdtlE_Vvq1Q0IRwYvsUXlx5-PpGdB4THGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUKILu61hNP-elk6tz6U38J1exzXZfSYLLyas3qqLCTTTFNPamIuKWilEMXcxiZJu56lySmOLiT-BjY6c-rUYynLzWiwEhS8rH2Fii83EnZQoymYYZ0LW3mJNSmXjPgilEOmIAqSJXJN0TfRH33woAJphdO5iMryPQalOESuW1I_JnXotUVoHeMpoLUFuQUmEkdJCZrXRRkf7IZU-EwqnPGf6QQZxbsdsbkRobwzOlY5ptq9TK1u7dLz2AqHz7Rn2fvqtdZrJIrnP8Nc4FyTrC5deyQ-cnqgtaL7f4LHireGo7yam_zE_WecbW2Jbw7QNEPG3BdVIVbXpclHnV4EZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI3iEXdHoRMVyURWz_6ZX2eS7Bwes4F3yLKfSoqS60GjOLWh423GDeqmQO81_0O-dgihuimcMU8rh9IlyoIpp6K8zHQ6pXlumH6UnfFcjMDwt88Jmko9-lIeiuiRekket-4Xu9xyi1TrjSMiPNZaN36CYVTRfP5nTeufzAbTdAkanJgjMAHd9dsee5sWEsPE_DOfsRv4jmjR0nmsnxlEEmXsRsbIFd1YF27FwekCUmlrAjDtlSkpxAbr0MbWW65YB78lPlzbxzE5lzQ5lDfG1RpSVgqeZAZpjMhxbevzkV8GwR4CTT9ges71rLnTioFZMre7ATCotVfsNdI_q50MrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HpD_Z63iQZ6zECQdTMdKtelcGC6rq4_UV1f2SjwNnsSSu1OymNVNlLQss1VZVvjqT9ZpCkxVczvJNOf1ywJGP3Mox4LVtkU4KuaSefblhrvyhQIxOa4Y8zvgKR0__uNgBc-5S5fTCB5jkk6XcslNv4LVnfXfxx2iLSVe_i2b3mWUZY8Le-Moysc9uaElCIlZ7WtcClKsGNUBsQLINb8rfAY_qNsaVPS1C5LxTYQZk6byYtPflzfomA5TEd7yl6fnN_yFnKAjaICIKBaB7jEg35Mh_2e1f5IL3PBrOMwY7EqS7B2-MSH4y8n0csQIvyg9s0VWZzgI-XB7-ij99zftTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در آستانه چند ساعت تا آخرین بازی لیونل مسی برای تیم ملی آرژانتین؛ دانشگاه بوینس آیرس دکترای افتخاری خود را به مسی اعطا کرد که بالاترین نشان افتخاری این دانشگاه محسوب می‌شه! دکتر مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/31112" target="_blank">📅 23:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R31Xu_z-pjw-P3bpO2nzEfWtoFf1t7szm3YegcNy5gAcGSxJO3TqyHeok2THbeHY3L5Q12RubQaNR0n2glQrUqeAtbfnzcRDrclS1wU-b1qIYbewyV7hzbU3SdxsSOGyRnqJ5juqLMrXpsk-vP5k-StlsOeH_vmkkgc08QBKTSexLB1kHGpetDDiyNThTQJ32LfCw2w96bTxFfv8HukDPjTVFmCGdXhjm9d3EOYbWRmYlwmdMLSebXlFR_RA0JKp2mE93IlkMeF2ItDhvZx8H0B8yc84O6IVAclwkhGYUq1aUdqIigXbhfziFSPxGM2xYB-tBF-vGMfymKnrfi-4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
مایکل اولیسه از ابتدای‌فصل2025/26 تا به امروز در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31111" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFoK6UF5TIpUYVFYEhEfurT1GCb089vDaRs5VhOIz2CYC-FZGZIWolqx5Mt1BOnzKF8e1e8p0OF_iMe0Q2vV8SwpuJHNcb1DUNIAd_htRbCjU9cU9RIURo-g8weuppYyllIKvifMsXqZP231nKt1a0erEt1mESLBzjZ99dlq2jC3bUMMtMy4pNo-jmoCkOpgUoBDdQpbK-rcY1AifcqzehfH1yA4n1_NE9cR7UV6zwD8LFd7GiQr9iwJlx5RBvcAIOP2T1I4BleEWC6FKWmQAHw6c229g8pcV4r2TSBPWS54dlN0-Lc7_bR9oxHwBAHUOZUIkEigPnm7-OzQ-Rv3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe4aB3e-UPo-wmi6Ehn07UY8yO_82vIPJmRAS5OEMtf948fgDOTiUZzfrlWYPXAszqmoU95f49Qm-PEZhwZyTuLehR6tVc6oJ858s_R2W21LGIvvuPpORwmNcgOxniEZ7XInzf0QK9Q8mzJr_iIYzzcfkYIk12JN9ASeVSfUzDYYgOzP1F9lItHKoBYqfSV7o2sezzcOaqEgvabtTOZ7B9MmWV2fikBFmmjaiU2Sa_N2JinSw3tk7kMDK4AQLfusPlVUpb7On7SB5Ht7AlQjE77XTIFuo4n4FMowjtCZMlVV5l0Jajss8LTSCvQPbgfqZEXa3QjRS_PYbJJAX-fbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzm2gzU0CpNMaXz0HqVuKbsitAXKuGpzq7rGaubKW3nRtLEs3KQLfTAeicwfJ6MktdsYh1RUY-yyAGoVcnYfT7EUWhJafgutI-DzibTPhyEpXWUCSAR5fSWJx0q9Bo7cVNk-ixXuhYm_3jKArZ-1XGv8vK-ORJQ-CBmJm7_ZiSj55Ijto3pggvhHza2E6MDBCfFNJ1AQvFmAdRm_PwYLDm9aIWK6LAtUSC59f25gdOb9qNzMqD1Cf1zy07zxV5teSV5EXbPZFQfMMWEnExpxwxImcoWbEqWjU0f42Y58DlVTOpzM9JDmJHZqCQL4WTzztLR2hrWW3qKjCUwVPVVSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxTyUmbpH0X1IIb8Od0aSjbbqtEqPRfcJr8AzswR468aEmRwcCdO7jAYtXZcvBbNYzCBTm-FaeCtCAmq6nNSCDIruKVfCGoaJ9-MGYEcidvt2eTlkpiovgXxhhcmUsjyhrKWa0xUEgY-02i6e7d4w9BfykufhrGBzyZwv3EpbniPynDD7lP5lKlZJhx6-m183SiEB1VJy3P4UuqrEXlB5RwqWwOabXdZcuZI0llOX80-zT4JQVzzzGDl0VKcPmFML6IXHajtYnOXbHCFFtlADvv3FwJha5et9sVGausVXNlqfm5haDtGS5CmKfTkW3u-ZLKu1hhl8j_hsgbu_X3dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=gXjM1zZ5ZXglGBR1ztoDOpCu83lXPA6sL14rpKFKfer_ig7P55KNDSiSZiKogFZfR9E_uzHroTlgTE7pKDu4TVAQ27sjd3pIJi7OPg_tmfArebMThL6OWaQstMKEs-UE0lWKscJna5hBOAXpihNxA1hQfsQ_LGEeqzj5idMS_n9DugYb2Zt4ex-uiS2-dZDjKRP-Y4UrCStlewS-6tD3MRMqwC3_bIliq5qI6mFbOUOl_oMACnME-cbWL-kPSPwwk-dMSWtIgz3fwGNPw3x9bpx0Ar4h_SfYhwldS1G6gcQVIH-bJp19ufjp0PKDQkxykOHenKnqL2pqPYE690cji1mohGQ03GmQ0S0ceIaLB_7b5NY7m1Rk1J7EJYIQhGYhFQ1l4iPe3ngL6iBy2NDgqWQGKxtXP8u5eAJcMf-yKBTufzPcljd5qZYapiT0ur42KRWOW3dbjilr1wK1zlXSjgzguQ2es6PVwksqSwDlON93yxoTxIaYomNDOJN8TvHjZw3dzZwAkPHd6rwcBRyoC5teSQZYgqzEqbvzxC5JnAIfrla9xEllJcPIBlKgDtr-gOENgjc4GVNMtpKUKZE0DUunRPk_RX9YZxJX4zX7yg_KHHwLTH-VVKm1_weqzn8RgyZZy_jVYStJee_CPoK2Pz6rDbNcjr_Di4LDqKZJ1Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=gXjM1zZ5ZXglGBR1ztoDOpCu83lXPA6sL14rpKFKfer_ig7P55KNDSiSZiKogFZfR9E_uzHroTlgTE7pKDu4TVAQ27sjd3pIJi7OPg_tmfArebMThL6OWaQstMKEs-UE0lWKscJna5hBOAXpihNxA1hQfsQ_LGEeqzj5idMS_n9DugYb2Zt4ex-uiS2-dZDjKRP-Y4UrCStlewS-6tD3MRMqwC3_bIliq5qI6mFbOUOl_oMACnME-cbWL-kPSPwwk-dMSWtIgz3fwGNPw3x9bpx0Ar4h_SfYhwldS1G6gcQVIH-bJp19ufjp0PKDQkxykOHenKnqL2pqPYE690cji1mohGQ03GmQ0S0ceIaLB_7b5NY7m1Rk1J7EJYIQhGYhFQ1l4iPe3ngL6iBy2NDgqWQGKxtXP8u5eAJcMf-yKBTufzPcljd5qZYapiT0ur42KRWOW3dbjilr1wK1zlXSjgzguQ2es6PVwksqSwDlON93yxoTxIaYomNDOJN8TvHjZw3dzZwAkPHd6rwcBRyoC5teSQZYgqzEqbvzxC5JnAIfrla9xEllJcPIBlKgDtr-gOENgjc4GVNMtpKUKZE0DUunRPk_RX9YZxJX4zX7yg_KHHwLTH-VVKm1_weqzn8RgyZZy_jVYStJee_CPoK2Pz6rDbNcjr_Di4LDqKZJ1Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF3YJIPtQGvS0qyVOvplItJrUSlGcppoEBMEabergEE-lDXDLIwiox41WH1-rHZJcEjwFNdBa_6ZKf_zpAubfBpAZ2bwyMGTREIAmcaOTWTSszTXBsJwSLrvKMKuZpAH7WW2mZHGQVyOSvdE0aObs_Wc7tHJ0Vw3YugmJYyKNHo1t0Amm3_G_dRDJi0DBwMu9FyjPDC1t4bQXsCQWLdo43md-CV8cBxWKJQQl84yEhoUxrDcah8EWXw8NEMpZ0jheGopqomuoSk2yqqDwUY8uyX8Phpguzf9aBTTaj4CA4fHwHruol2bdhmKNMenkoUmbEt02gqaRWItmr-_Tlm0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn2N_-eoutApHdfLUQ-dzjymu_tyd4FNOqbVMX4d4zlP5yH3PbD9Df_EJiqZtRehee-EiKZswzCDauY5MJrsWzmr0h5pruw89oG7-Mg3lq10UkcBgfAFA66-BhFOwxIVASiTI2bAiVu-77KpfCBYa75ITEsyx7Ss2059Mu8go9JqHVnOd1O_ghboKTIj1HOck8znBq8nB-rWOCFDKK0n6x0xQr8a8ozYajI01i8D6WAfbYQvfLumYSAXMDEYjxyLs1Ff6d5aJ6nTfbUAzd67L5dEcFNijFJvAUJ_qPYVbNAEmrd4HCbSP2IrolfweTAoUALr_moT-ANe0Knn_4JE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLVjLFN7sxCGLk795ml7IwnDp6glUfrT5GuXnI_DWGb0Q0XIo35WBFzRum2KhFPFrsuCQEziSQo9Vni9nVwiaNu-3nz8ZQzyBuLHcsqzpuFMQFyFxGAMzEnE3oLB6_skmS341fJ9kwVFKnjmik2-yQWG0EJ7sJz_N1ehj_ZOG5RJ0ne0jyWk2HMMwoILhI_yodMpXnF1t7nhk5n_BVhcfN6lhmjM-2ucqXAtXNiB5A7h3twIGRSXAb4L3EI41VQv18D8rNHyPxdVwqVdDQ3NWMPUhVbdCx5H2INaweHEP26owMhHksd8O4G0stChmPxAQQ4SdGC0SBT0L05wKrKolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn7i1NoFyBf02MFEZ-IkKnQdMGqCg4z1o79MIlXcwz7nkrnmPR-MbD8K1lagYIpQpWHYiCwBQlCrnPTFa5twAwuotH4hsNaZjzl9Dzkh-0PS-Bhks09bsqodCUtnAqZv6-IuDmlbktYL0dNgkEfswnzaB9xJVYfHoeb_lW7d7FV6a2VD9d8_AY2qQYGoiU5OIvZ_5NFzt9X4JaORU6vOYIkSjdUCjBExol_W2RT33OBM_o6z3A0ENf-J1R0PjB_xTYt_yUM6mYf8zt0O1Mrzu4FGCckvl_sYJTE_FXzO-SYHFczJ_g6-7aeJC2VqW-qlXt_Yspw3dKmYkV-Y-Fltzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osrf5ANcsF97BeJd5OXnWa99ONK_3O3y00g1Q1iImmYeRzbav3u-b5ZW-PfHjQEmZicAwARw8YUO3ewB8_PIXf5PWFGAk4-FQC0-3oWq48asHekQXi_ADRjHaw7PKiEeJbfydlsyaXMssmY9jgFjZFKMqahT52QnybPAWviVNgbeInLr2qkHI_eXLqSmFRwT-yPCavgLsICOLKlmkozD-diyI7YeQiUcM7MR0XdrWUTzGw-ba_6sucWaSfsARqkWEe_ApWXkjQaoUeeJygs8LPCUo_ad_F2Y4HcTlKwNHO1RxJKyYBjstYfhFuTMoEMbjg5uSTafNEoJP3sQKv4obA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/31101" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/th6YvDfMTuyyngXjUy7PkUqfjFEpBJCh-0USHYVRq8SXNNm_j8pBYBkq1-mO9l5VkEmShtYhxurEwn8xfac7AgHBu-Zp3wO8vgvEwK5w_vPTzf4P-IvikQYEXt3l0z8RWMyZeOct6sabhGzl62q3BHxUmvkxKpDje4ReqCvcg3iVTJw_VPrULzdYPiuVFlJQE94D8fexdsl15Qhn94U0EvNPqbUX16iYYdTTpR72jSDmZd6U0j0QvjGRzp0wtG1GIwIhlCdjDsDryIK3Trw-y_5Tp06Gq6zfnRVVOhUePjs28KBRkC-WouLnjMU1zvPo09BOurolvcjenM60tZnc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmEbqo67Cy99hVEqnoE5cE57DOHBWnKg5GIVnkViOk4TWtjEhv0lGUYXt-AZaak50mR2HWwml_c3juMfnhltA2WuwcivnFdqRsAHSF9xpIjvQFE-RyKUSqOmmYBl6bqH4jl--A2sckGw6bBFjwnDq2hmvMCLzJ_UDQrVAS1fEFnM-Wy2L4Gxr4CRIcrEnIHRAvfSuknPgTJ306PoevWm3kcTC5K-4X-ONPVz3T0UJWkIa5KOZ07Tj45ZKGrY6CAOECo_fSyQQVjkcOQu2v_IFikKJFb4tsSBRykX7mwNmLX8fyz01Z8SSslKD5mGLFnVWjymkGMkQXhOaeRzUHZMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL7T4WXSGeyG1CUyzeFRM4Xc8MoTaNisNH0t2addkPnbN4ZipQYUUPditxUoTlwv90gMp3B6SDsQOoilL4ldAgGOKQwL6YMLFyExITpXu70QAHmp38iaOmdAspneCo0gnKF9SFkfWTfJBfCbdHdfDFxHXB1nKJAuBbpgBXIqO_Fj24voyrcM2fBsBtNzC6dek7ifa9MoHiSA7nUZPouTMtYEM9N6NYfIT1CaVW1AVZh0afPTokVRzjgBf-DW1OyFr7XY5_VN9zCDm-VlojfudlDPKRP1_dDKYxide3yqIIA4fqZ_0MGI20HXKzP-uZK7YX9QGFTdz8OOS0ks2RSPHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK-uQj4udSWb4arKT8ROpqYJedQ6FaqaGfxq5ECg9WD43QoBwnoEasCPpo59BYRkJeW4qOE16MOJc9SzVxbPeQLLkhBGLkxDQH2aVo5PvnHsrdXatIG6H2wbqKoZhHrTSX3MSGOcY5LJRCjtCDaDeJ8NsU94ALimUg1Q80uqe0cRNJ-FA6Ns9kIXaivtqDQpWMRTxXz6NTBy_e8jQ5aI9xJteGvA0Eh6YR5g_kOY4iVrDbSa_ow-ZPmj0kheV6DsnXq6FWJ-4mYMJmkxzkdyL6BqYzYtN4eVZ8AjcF89dzHpD99-MogqQklRDf05JILktwjhWsja2pJudle0yfKEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=J2lUef9ygKjnoAAOtnzZb4jc54zFmvBSY4ams_R9-RXWvViLZ8p1Se0y-Q9iDFVq-Z_4GtQtujSmLKiD5qpAeJyrE9_JfLtEx31HIwaJoBOXyGWFzZcRVrWHRSwybK1gTLYyZMXf82TF1cdoBfxZyjBPQLrjloH2I9y6kiWSh6Nq8RNQuYMzfJLuqbZSTfXcvTqru9-fLJQmbB9uDIPOrnDU9DTvu-YnDx5S2sZYnij8ztCGWNKD3CyVjT36KEdttTRAEAMRpOY-3HkqC4xmcHVObKdz-Ig3rtQH_vBbSK-iXLkSFS2Uc1Zw2PT6rInhVphUof75q1ba_j69l_WZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=J2lUef9ygKjnoAAOtnzZb4jc54zFmvBSY4ams_R9-RXWvViLZ8p1Se0y-Q9iDFVq-Z_4GtQtujSmLKiD5qpAeJyrE9_JfLtEx31HIwaJoBOXyGWFzZcRVrWHRSwybK1gTLYyZMXf82TF1cdoBfxZyjBPQLrjloH2I9y6kiWSh6Nq8RNQuYMzfJLuqbZSTfXcvTqru9-fLJQmbB9uDIPOrnDU9DTvu-YnDx5S2sZYnij8ztCGWNKD3CyVjT36KEdttTRAEAMRpOY-3HkqC4xmcHVObKdz-Ig3rtQH_vBbSK-iXLkSFS2Uc1Zw2PT6rInhVphUof75q1ba_j69l_WZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=OQkRV0KKP7YYoae5ATaNxv8OthKcRW05vpS1qropZsiNuSTEaSjCKcsYpsWgusM5IQi5LBSNhMeq4o-Ob5O1wdal9YsFz58WX2ZC8mIi3D6UOSCojVLSOP8oGHm81VzO_3IDXsIef4P3_0G47skNhKZJhcGv8liPcpPI0XwClT3KAPk6ssh4UVldeT2SpfvM5PE-iDOMFiaCCJdgNNNhUPCiN5WCN8GdZfWZ50LBNnjYyRnAlmlllluzDrBvPqGhFpaS837IQKEgWO-YVeCZX5vgJM5KBiYiU4anot9rwwltdQSDjx-b_3JVxaihJ9kOkcW7CYrijeDJ8F9jXQxc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=OQkRV0KKP7YYoae5ATaNxv8OthKcRW05vpS1qropZsiNuSTEaSjCKcsYpsWgusM5IQi5LBSNhMeq4o-Ob5O1wdal9YsFz58WX2ZC8mIi3D6UOSCojVLSOP8oGHm81VzO_3IDXsIef4P3_0G47skNhKZJhcGv8liPcpPI0XwClT3KAPk6ssh4UVldeT2SpfvM5PE-iDOMFiaCCJdgNNNhUPCiN5WCN8GdZfWZ50LBNnjYyRnAlmlllluzDrBvPqGhFpaS837IQKEgWO-YVeCZX5vgJM5KBiYiU4anot9rwwltdQSDjx-b_3JVxaihJ9kOkcW7CYrijeDJ8F9jXQxc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFis50W0d5jx9PuJ8jcNXodJWMLo4bBdw3AW1fMKJmncWUcJj2qYFfUFOmJuNzYubRitYrG6lTKU-RIYfnZCG9_BN5ow8fuVBE4YobOMhXgUs-61VPyV5Coo4teUp60n_Qc44HChsXklwKrXsxX17KfPsJPSAOfR26XCM1RPMJzuLD4bFB2V7jX-kVhjHXsrmeS3dfYvHSFjij8K9nSWYJq9MOOzLrursDHGGTvWgLnHQXE7Cg9PWyCcMWKAqCLZ7b0xmPqpUgTHeHrKcdEJnfKM-2FX6Yccn1OTdH1HpHLT-1K6a_s3M9rATBBeT8sUU7gh8xwNT0HM2rOhPTMlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=jeDEva2SHwFP8IBSBnqT6Aqt0BAOhTygPhNzk76YCvc6QYxouTuBNY8mxKS9O-UfDorPt210L4jcYRHQo4avKGF3Cz5P8LX61fAiXz3VMoJkjr5bROvMzcJNNO8Y-ZiyELD5ViYG32l8GndmSCdeWxqIsBWi9734eiuguWWeLDmSIUWVejWrHfTPLLKaRnrR8mf-39Ndgz7ni_Qdt9jElhsS3MzDLLdin7ZEv6KuW3OcVgYwFiF2UjutG4k-_SMMejkceTvYrQ5jKmp1x24yviRQV3tyRbW0y6GE3pXPhsRCoefOahALLR60pSgL0-BIA6oIk74NhkK3TgTbmhbeQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5T4TzUEEola_lVmH86tyKwmoDNptKuH3P5rz-l54W1qUJ8LA9-Hiw2mwMopF-BkYQpk5bWC2xw4xaCYwRnzbZtiu5okkC_eD1QA6JVyr0qY57Tr6135YxwOrrGAHtYQapp0PwS5fsZUBfyRfDwdf5ggQ7ILXF_086jEdvMK14gird36fR1QTa43SZ3BtVHbt2h7dhDKV_VrPg-soih9hx16rvlVBLCFhaZpYPnBK37aKF9a_b8VFcwTlrDipIYgnHkzBhv_5ITYnU2N1R0dq_x0H36Z1oZ5xXmgRfUgSV80mw_PEhnX_f8dNmUmry3o40Q9KCvq7em4_TdIgpXRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA91IY0SvHVvHRZp72xSVkEMtL-6VnA40oi6p-BebTiOvLRtctvdwqTrphdqY_iv-02bC-O0dyJwRNim0PHee8BOeN2eRRxcnb0gffiP0oQRrWIUUFjLEJbE4gvuANcGj6_Pr5ylZLJ73BAXepQ-Ys4I35fWvVNWPByjSg0cAMWEf73DS5yyWZIKfCsZW8jBIH0yK7ynT2LZk-62cpagW07rIBM0uxdj1UhVPwur9fF2DhgKwkoH7ZCRr5c-_DGh76arTkXvkqRjc3eJ8g_tpW3PRGfN3WyT5HrzTjJDBzUy6lc6Ks7zVoOw6q1iX9SgTbM7b-Ls7dl_7OvnETJ6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=hcZylWEmkE_oiBAgsBgvlyACUs-zOfKDhFj2_5kLONWyktm6EzCVgKEI8JDZa_IrzwuouC2sMiIAo5yq2hDVb_PxuTUw0wss9ps1VLc-bCdUlYPpY2E0T9MOPgLY5z1jRgxNz2551ZVJQBrVoLrV0UXHNBhXK2KPqvvADAt1zMUSiBmHewrck5GKyNXqltL1zKitEOpCmcrx8sWSwr-rXlEa40hl0_qt4vhILLn0tHmnNesIFy4syJSRYzkO7AzPFzBXuJhsH5aNlVOHmHCS889HmDCTQAfX3gsDJ4qY-pp_mF945hsP0_YkouFUvFKlSeRer7qrwyVF19erUW2dYWtZmDspvuL6iIn4KQvicEjqQ8xmKkPgKPPmwI11R4VhZBsCsDT1EXYSqRafbh4xDue4p_uTo2pQrcKSiAIM28vbuCXspO_L_LRBLBvXaOfiLUCHJ-ZK3ww-UmCP9eP69dszWB_gmTuNL--nPXQFo3GUSd1s9yLW_oMn0kKO9tMaFShnh0es07luzQ70tVqSxjC_DplOqF2yejMW2Gho76XtQM0POnW5ILOPQXs2UrzNSS9-KCvURMP6_iU--U5jTr3EaC6iwQKGquOnGVuTxx0LJmFh6WuLWTYZzjF7wC9GF6MAsqEyddkX51tC0NdrHBL3qWiVirHgqXfFvq6Ha7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=hcZylWEmkE_oiBAgsBgvlyACUs-zOfKDhFj2_5kLONWyktm6EzCVgKEI8JDZa_IrzwuouC2sMiIAo5yq2hDVb_PxuTUw0wss9ps1VLc-bCdUlYPpY2E0T9MOPgLY5z1jRgxNz2551ZVJQBrVoLrV0UXHNBhXK2KPqvvADAt1zMUSiBmHewrck5GKyNXqltL1zKitEOpCmcrx8sWSwr-rXlEa40hl0_qt4vhILLn0tHmnNesIFy4syJSRYzkO7AzPFzBXuJhsH5aNlVOHmHCS889HmDCTQAfX3gsDJ4qY-pp_mF945hsP0_YkouFUvFKlSeRer7qrwyVF19erUW2dYWtZmDspvuL6iIn4KQvicEjqQ8xmKkPgKPPmwI11R4VhZBsCsDT1EXYSqRafbh4xDue4p_uTo2pQrcKSiAIM28vbuCXspO_L_LRBLBvXaOfiLUCHJ-ZK3ww-UmCP9eP69dszWB_gmTuNL--nPXQFo3GUSd1s9yLW_oMn0kKO9tMaFShnh0es07luzQ70tVqSxjC_DplOqF2yejMW2Gho76XtQM0POnW5ILOPQXs2UrzNSS9-KCvURMP6_iU--U5jTr3EaC6iwQKGquOnGVuTxx0LJmFh6WuLWTYZzjF7wC9GF6MAsqEyddkX51tC0NdrHBL3qWiVirHgqXfFvq6Ha7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPnTL09kwOqZZqOR4zpq2s4MkLcdkglArIciHEN1j4fMisdPaYGKln8IVxy1VZ9FekqhRb5B7VrPZ98PBHHXQFAPIQ1--w4MXrniUF1F267Wiw0QUCIZXtzo-HkHLDqVSaDTjbYPhtC0mZjpOFBVRKNj9pspkGanfI_-frP4SMxpila8KCZaIY7AHeQAm_MYHrWrD5J4Yr--3KVcyX4-zc-XfX4nF4BFrRbrREX5u7l4LNuBQmo72iljTT1_ewTw85_zSH75pYpNX7qz5B1LY14ECGEUYMd3nv9rCZcTqB4e32lGnPJlnMr6cXAK5IS4yd0VTUFS827hRHrEsTUxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDC-dLLnaX6s5UbEbHJYuBxe2h16y43T8tsfZ_pafdIuxsrUQAZO_w7MqiHW83GN3Io4UHuiPJynG3rnQYbleO8ml-TrM_d_pYCh6geO2QoNdVOgOvkuSMHkAm0krValWCLw7oJGyjdicDNTsWHIt5NLLjWaHUlZMsReRB5yCGwjEi1Q9iXVsaQc8mb7B2djaJyxvFV1bcMg1ovLMB_ag1Z2VTqkANMilXncw1jgB_SKPTI0hcce6HgUbGdd6KaUD9rl_mOwJPdJYyT3MudxqdaRD0j4kVr3ypaiISUkOfp30RXQEOQAdVEQv36dv4jWTV0mdWIZDYxnZ4RYUA2twQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNZ7yOn1PqVnNu-PiLQMESEKPXu1GNFx7J6Iq5e-zsCdUlVPjxnVU8ScRbFORTo_We9zxJnopxbTcGu7dJyu8o0ccNuQplyW2QN20PanHfdr2Q7rVGcVxYIWOJm5ZYOeCooGDYLoGvYMGI8wnAdhZl3l8Bf-46cGVrNwXnzE-98BWm8KGJSICKWmpRVp0YhZosm7opX5YvWPA8IeIDZz6q8jEONGafgy1avyc31w0u2rRXJ120VeStPLPN7SMnQkotlohVu7b6KAkVYN3XAMNWRRgtyi6PrpSXOG94hjnp8aWzo4qIY1G34cBTIbbq9yTlDa2n9y86ufjYv87s8bLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3uTru4YeDA6x6S-7tj6r9IDJAr-ozYATKUwAWwK9jZBa5zjc7WS8RqvpBdlh6TybWCS7HNeXUvdhwZslTzSXv09krc07SDeBbxZ__hUUvzG7i5g9dZ5P8ugTgL2HuP41OZDLGOhtdlZ1odSnua7DXeV1mjahkF0yw13u8ADW1O-rkCdxUPvF4yDJJlzL9FRD9mNdNF-JLs7qbtTz2GsclKpPW39SYyBxQykA6K2gTcEcvZfkUQEyou89ykcMnSa77kI3-v4DOHlPHNw7unuMCUraQ0P4eLjrS2mVxUwK1xbx1_LpWCNFTZWvll3rrUcKZNpMoJMcYNEKoIOt1ISyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm0LVeSU4SKCzJzdpV-6SmP2SmPVEWsCT8hdWAzQv-zE4PNL3hWxhvIen9r7xEq3z3ovBF8m6wnpeiI1HbYeMG5OJuwYj3JpOB7NnwaQhTyjJkkCaSxlMyTE_GGemV5xzYodSowscK_N0QH3W0W3x2aUSLBHCgM-1pnWsn7b87YYyFSO2ZAnefz3m4fOUB0F9N9GIzZXHnmxM_Bx0ShZBVcs1c-Txuxv_MUxaVnCUaimHN45sdK7Ac_y_LAdP7ojoGK3Tv2r4sZEBK9hIUDPECjhV4vjajpG-YBvjYkxUdZCg-DAlHGyPk5lbY-xqvv0YMfSLPkEV9FpiUmKgrBQYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGhsvYTmn6imSZmZ_4jK7jIRN4ToiWU9DLKBRfloLPxFs7Yn2BHfZtiMGLljlwMnhFCOXazNvhMXe7SW-61e2tm6PCTS8IVTPNZ_B3GaC9cwU7I-6j02TSDXo4XrtbP8ZEYjsVLoc8nBRrPBEawNko42V7dkLjkLNc3DJoHN69JMNjX3oep_sTBMuEy_U78nb8ZJThB7JyjHOvojvvTinGSipeMf0AspMZhy6aeZ9fr80NvtmHaWF86sJziZouVq99hpuAWp91pb45pb5OtR_TPQfUUdzIsrmhCbBxM4gjdAfjMIoCKTTBSM7dQOGRNSvP4wERTLLp0XETQZGEzowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqTzISy4DjrRzoi7CaD4pj5O6MYZlFhZzxu_DSG67ar_N_aSdQbnAUNm8Lw3oQPrl6SYEbUWeguuq30Qc_Pv4eVjmvSv7Oqif-2CY4lB3bHLN_phOhef-X6ESWmxl5x5ar3QdwI6mIq5Rw_rBR29zuLnyHVLLqsn3Y_5Ip1TtxFqOli-qLLCJGg4_D2bfAzwTjDnPfTmSVAM2PLkbKpzCqut8i8tr0EOu9ebNQP3eS9gPe3_3_G2HnGurswggkBVbs8am-yUhsSuBekYuZLQyfsMt1C4IQ8eHx48PaPwCRNS98aE5z9uTGZPSqq5Wf8JIMfewKL7OveOiLJuUUvewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic_ChDgzE1MpbFcrslNz4Zh4u1y_rxUtUdbRF7jhbBeiX5QTAWcfDIa1jNB54Y66IvxoEFNyQKHvfpIgsGpQJH0bRMzjlp4oiwW54wuWet_NMyr12QIeXJtfPzgvC08h-qU5-1qd1ormG3BbhJNnaDPfKuBnddsGlfZqqKvGxnF6iI7OTwoUujq9RMF4thV_3ImoekfpaaGB9ygBwWEKtnkJV2aUp2Orpw6lrOvFUmMn_GlP-EeMGMzDif3ZLFiFrYW_ypd-APfRKA69lLgRH2ozz0Zf8XsPCRss7ZgUS5Qyr0kLU5DGmXl0_jK9siw55SA94xxYVr00FSe19Io45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=OuVmM4aIyBxEGxm_tbnLqNk5EtffiAWdSYPl2EG4a5UK2tRSBMs7f8-oedV45Vu7iYwRE1sVk1wkrE5POiojn80ewdzdQAunF9pS28lmOYCD64MFYegdWGECW89JPnLBvZHYL9RZMorvwRlJI_sRmoFXeOPMgeY-VM-ekZ-YV0yqg_a3LVyUKgAMpR7lAwFJBytmNYxhio1eVhaveu1pSbJN_Z0HHmhYaa7pQ_bNsRbcZYNyu2mW1TmFxuMQ-g-CMa5R9DtLTAA8duozKqIqKQWbmXi21jMHP8QN81r7e1T4IOpoiB9vx7Y6iJJAMZCJDPD6ldDpe1do4gpvItw4xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=OuVmM4aIyBxEGxm_tbnLqNk5EtffiAWdSYPl2EG4a5UK2tRSBMs7f8-oedV45Vu7iYwRE1sVk1wkrE5POiojn80ewdzdQAunF9pS28lmOYCD64MFYegdWGECW89JPnLBvZHYL9RZMorvwRlJI_sRmoFXeOPMgeY-VM-ekZ-YV0yqg_a3LVyUKgAMpR7lAwFJBytmNYxhio1eVhaveu1pSbJN_Z0HHmhYaa7pQ_bNsRbcZYNyu2mW1TmFxuMQ-g-CMa5R9DtLTAA8duozKqIqKQWbmXi21jMHP8QN81r7e1T4IOpoiB9vx7Y6iJJAMZCJDPD6ldDpe1do4gpvItw4xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbZqGUGUuyoUvcg5GdHz_0Z2PnV6EVFFVloU4Wu03WqM7z9mL-3JRSKiNSV1zRD9L8j6OcelG7TAAiC9T6NuQRjABo2H4Tm1LO6OXuuqwUGy4fzUZorIlOUkaYbnx1nFiO3l-cPORlmqLGz8KytrqzJ6x-qf4jJA-R2ombhjKbcQASEeIgAIsEIvq8AK886uLCkardem2QlVEeZPCY9AQw2ox9jl5AuFTBg_7CsXpfxOLufkiKIeIxOiCwSZ4sC1gSpCvl7ejPXU6N-STvAa9vWlsaXaEpPXqdkF8nLQ67kKHR0Il6-cW-RLl65oG18f-Ce5TXkgEeb9hNhpI3dDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=cX0xZF3Dd9IFOGLAgTI7XlccOUIFeY9NO7q4mJ7VCgLEJo_tA2f90dc0NwVAz_vbw6PkZ6ZxKPrzWH1r_NxlgsxQD5Xg4c8ykCjgWei2_8CFO80QR_7Wfehnwb3C2wuFKn1o5KsejbMpSksgCw7FwKkXpZuVEE-0MmF_-zvAFO-vo4Z9gY-_AqbyzEuJ054Q1zByWPcLw0oWL6dvn0YfOgv4WJ8GYKBHJcdZBfxSonL3KVwHwRtpfeQvrKz9Or5d5Bm2XSrd7ZL1tskVdkWEmZlOZcpPrbPA6JnqHd-RIK0-xHGD80n8Hh1NA9ykccLkCNYntxiU9fKuX24hhgrwDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=cX0xZF3Dd9IFOGLAgTI7XlccOUIFeY9NO7q4mJ7VCgLEJo_tA2f90dc0NwVAz_vbw6PkZ6ZxKPrzWH1r_NxlgsxQD5Xg4c8ykCjgWei2_8CFO80QR_7Wfehnwb3C2wuFKn1o5KsejbMpSksgCw7FwKkXpZuVEE-0MmF_-zvAFO-vo4Z9gY-_AqbyzEuJ054Q1zByWPcLw0oWL6dvn0YfOgv4WJ8GYKBHJcdZBfxSonL3KVwHwRtpfeQvrKz9Or5d5Bm2XSrd7ZL1tskVdkWEmZlOZcpPrbPA6JnqHd-RIK0-xHGD80n8Hh1NA9ykccLkCNYntxiU9fKuX24hhgrwDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5s79DSU1Mxo6xrCV_ZyeQWMjTk-fGn5Lfbx-8DBDhiSwrqzsqtXKCPqzOPTr92WyY0L8ApogxTa5-V4gYnOast3unIArnM_swSNsAXvPesXG9JECj-8-2mrlLCuaLgFVFnL3QAcSquE1q9i8BrbU0Mc7AqnR25IZqeOp8jybG9uPFgMdmf1I2G7L4cEfTZ2uAluAnqph5mjmwqED1Ml_Z15WIpIY3DcS4HJwAUuJClsZDOOx71fOihskk4mMm6lVl8sZAam51lx5Wy828-gKLKm0gt4qSgiPvYWG-XaUOOM2Yz3sVIzYNcBOH_Zwmfpc8AEhd9wQtXOAubK1tvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=djp916Z1T1zyy2-B7y5JPHpZ6RxJStD4Q9ZIr1s0xaH4T52fEI2qVNYt3AMUg3Q0LhuRC2Fl76fUDOtUNF1daIvXjpuMCyj2h4XPUGvz5Jq5YAtouqXu8uzuvnOPg7UmOfqMK0dean2wS5TzyBFEUVOx_p60QmfcqIMDC7feHhB5vdVXK1TqiSExvmNzjdVQuCb-Vpk52sJOy2ZmJSEMt7n-nHHww5c22_eHhrBAo1hhxFyivJ-woGGNMXZGUrNVxgyvWhp_Gh4meujJKD-FN7P1g3TjtVEwj7-Iy5_MqJ8zesqpaqh8uDlA70M9PJ1AG2rQUbiisfsdezjgw6TiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=djp916Z1T1zyy2-B7y5JPHpZ6RxJStD4Q9ZIr1s0xaH4T52fEI2qVNYt3AMUg3Q0LhuRC2Fl76fUDOtUNF1daIvXjpuMCyj2h4XPUGvz5Jq5YAtouqXu8uzuvnOPg7UmOfqMK0dean2wS5TzyBFEUVOx_p60QmfcqIMDC7feHhB5vdVXK1TqiSExvmNzjdVQuCb-Vpk52sJOy2ZmJSEMt7n-nHHww5c22_eHhrBAo1hhxFyivJ-woGGNMXZGUrNVxgyvWhp_Gh4meujJKD-FN7P1g3TjtVEwj7-Iy5_MqJ8zesqpaqh8uDlA70M9PJ1AG2rQUbiisfsdezjgw6TiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua0_OcDA3ttqECoIoWQ8WICcB_lFhiganEf_t7DfsR9TeR4HSK6ypxIzyZYL6kK2gEELInI5W6iM4oY3EOxyJjq0gY_QunU4jfBaBdPQmpPRDSG9CQi0iPRQMTG_q9ZSru_kWBOB_XF9TGn8GyzZ6XqfqnFovAOXeUn4NFLaFNpe8XMYF0PctGeBh6wkEzN7clhe4azv1BO-1wnWrty2r5PmdyZhSp8C3FWRrEXjdXO5DF8tbyFqDyJOqwAyTp6lVzQ2a_kcqNXluDrFpZTvdm5_sySn_IClljHAoXk-XJuG_W3UFgG2yrjr25Klt3ISwXVtDl42_Ye2zRj8TEFK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31076" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6vLH5HCKTbQpy3n7NT4Mlf21SCjsryZhLTdlrqzcZuPh8lRNPGUlABHvhvgkggxPXlL04hEHLGXHfH_LbnB3gxJR29uYfxGUPwDkx8fe_Lv3ZTI5x2XtDIPWB02E8sZQ4Pa_i5TZfko8hRm2UZFn8VJGbLH2J8VDBm60-jOx144q7q2FHeHg7mpijDeh5JvO1KfKttPluZ_yI2fUiWLiCtTSAy9a9ooPhzvmXEklWNZ9u0gXEufqIw61H5BdFj-_XNfSO4x1PpHIoke7QBBdLO3Y1VElbSX2ZHeTvIyOKI-Zc7PZo9ktIBO1Wm-ttuhx8E9-Jcn7xMYfYVvEVrlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNNoZC81AogirozZWYifng_2LGN5SJH8oUQlFKvQt-w0h6BPTC2xpB7tNARiTl-ZFnTnJrqvTQA5JUuhm1ckKVQ32rZsa8d0LvS3A102wxu42gqzXIyC9AFeBYQVREJbT4ZU4kIlBG-ds0zlahPiuC6NbAnMew5zMpKAwETB7WbLruKqtpwP9mN9RXQ9puXFZQQ7X8SYXvBovM960MHD3QVvR2Mmf3j94cz4FB0x-MzTQVErZcCYBCAGcO1PTzJsEtD3R_hg6QGN5whwzCoQ0HFxH5_RP-OSLukb7zKfBETO_1n8gBgZtfTvjVhqSUF_pXLAmut5YeH0ss-e1aoj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JldiT2ZdSsEAw4vlZLNxc0uMzNR847tS8X3I2HbSsNeRoEx3m0ou3BIthqoFR2hKNvaDKAzne3cIsvnnSzFMtU9MYiIsZpr5_ZQ132LNDavjGeJz1jvCeCGN647hNzD5MZ35cs3KBriN9ew0ceWk9hRAOFfAfjB0tr46tZoPUX8masXjf9k0BRR90YZPk8cLiEFUFYDhA_pCGysECwSCWOSWWTxtCa5vXK2qmhjPPJz0PJUb5RiVIfct_b3QsQz3245B-SS3Y5YmthTWRZv7RLDChSNRQPp0FgGtrmqO9w_FEPpW3qdbgG50Ot-ZwXCUbaiMygBN_mt5xidbaiGpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBJzYTq_T8ffXoWwKEB5knXtMGlkpGk8o2gscbqibxVMeFVoXsVfCyTZsJ-iiDJTpATNrmwWgNxVXyzAmSOH9gENOJLWKvErdG-y_fn8J59ypJImoeGK9NXS8Szbh-XCO-BecMGssHtTdRr4wtYsLzK0EAVHx4VqnZCYq_RZc9JbYfTmLL6NBApF9adN9_ZqkhA_oWf4GmKlbXhoIsA1XL0Od1ygTwSu8HkfeSD3DuOLj_wEU2dWdZq5NPo5ZPQ7zhFIZrECOk5xzS89PmZBJ6uqUx9c_ycuJnxMi9pGVRTx_RsmCVSIRlBkCUSqA5HwW1DpFRb5AEZFODknrCUXhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=oJi9pCmTqJ7d2Gy3WZrvkLbWKEYPOW9AwSYEDZE8fi831SN-xr7h21_VrB7XllaeXnmPTahHY0na89VhvhM_dPMbh3t0CbO08HQP2njhwnVgqjRJ_Pl6N0kmFZlXUITUYLumSB6qdXWObl1hfLb61NE3BVFm_Ma6K4_MLqyXy8tG5FJBaXpXvmgm7g_aT_ORviak0ZDsujTQFdU3XNX9Z5sc5h1nV5xWTkw5GS5EpZYr_Vb7fsEYcLaxDu1ZlL5sdS3bk_HHi2CW6me4ixNvRxVuTRMNSH432nvaB5grs6kp35ajG3v9mi8pEfyZgV6q5Vx4J330yKqZHYEjZyimFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=oJi9pCmTqJ7d2Gy3WZrvkLbWKEYPOW9AwSYEDZE8fi831SN-xr7h21_VrB7XllaeXnmPTahHY0na89VhvhM_dPMbh3t0CbO08HQP2njhwnVgqjRJ_Pl6N0kmFZlXUITUYLumSB6qdXWObl1hfLb61NE3BVFm_Ma6K4_MLqyXy8tG5FJBaXpXvmgm7g_aT_ORviak0ZDsujTQFdU3XNX9Z5sc5h1nV5xWTkw5GS5EpZYr_Vb7fsEYcLaxDu1ZlL5sdS3bk_HHi2CW6me4ixNvRxVuTRMNSH432nvaB5grs6kp35ajG3v9mi8pEfyZgV6q5Vx4J330yKqZHYEjZyimFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_JFvo90jZPQx0GqnZA3mSo8B811VvUQWwKaLgbjhT0vtjcKbVBT9RfFAJZurFXBfKyFfmM2gLXFtVG-C9bqMy__wXW_ayfezYGVHUOJmBk2iFYIL3ExdsjjX49N19tj6JRfMy5nBH2ZQHZdsHYdZ-xoojmdLVDoJXSGku0dASf4DdWUepIPfYkNfeeB_TPpcVSpNy_vZ_GTay7UqMG9Gady3MuEjdClsVGxiNbnwLy0E3YG0CEZRzwCRS5YBk8TsnYYR2sw8bxeKPHadQuO0wPApjK0H9YvzVQh4i8XBpgO655fL4b-4aQWJNZDhcD9HmruipAW8W_POMsAidrzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu0yYr_4kuWqRqnbtsAPbv_YWfS4Jz2oyKijswJ78zMdYe5N7-0d9fjb10_g7he_EpXCcJ0unffSUz_6B30aETGDFHmU4iRrMKTMt-z9KI5gRSuhYJKHwiysLzC4YEDVBdFNXwQIBkNnblNcMklSlJSjpYO_f3tquQ047b70M45_vq9xY9yCg48RQS0HB8zr498nHFBFA2K8Ke1Rf7octz9xKKje-bU7ZVviMNLUtZtoCZFSKLQXhDwhpFNSqJR78nqUk2twBA18pD2NFdSiMXTkJ9N3PgfjL8eNGrCa0ZrPjQqXpIyd4yCdm3HPtYS8AVIrA6shaDWy9NklqkhoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS8FCYwuqpfQVKbNxwg-NSegj3EQgDuPdMOO0Yp6VjX8orfwRQrWU36E6Y4Jm6ihRSzefpeFwAq9uKWoltjUDAKAkGFBcuRBDjPpLzz9ngYVLdUtx_NvbJF8112G7sharpV5M5LX7PJdvQulhCaZj2F0P6KZcvuLMA7DqO4mOS61-Lt_Q_Zpe0ueOTLRYFeBt5EP-M15ut7H1TzrH5wSDxiOwNEQ3LHmXRDPdSHHhr8oKWlf_CTkwOcRJlWchwz22OUqdYfhtqU34Z9wl33WULRe1KTuIUN8grOpPluS4nYahVT5yI3Tz5gkvg9vg8IMyu69JzeT1NCddGDMUh0TPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=MtBB9jlnQkM17YMbJZp5MK0URkKpBf_QQv1CQ_75tedh_jorVG_66QpWWAyJ7dA-j5R6WeibnYNZu61-F9tR06EbZ-XeXYUdy798gLJp3Z8WLfnRkQHJ7oSnzacvYwZhNdmqJpY53HJfxknDxJ7YxVDUcVoSEPiRwx50lURucs4mVqvedzmIgp5UW07Or0PCEw8bzc7awXjJQDFx6EBgLHGRKpSwiyRUa4FkcLbtQkUd2PapJ92GHBfgU9B_lz_NOiXZNfynsbQLVrgdD4rb2x85iUyqk7raQaWVxpLnXoXLbd_-bLL1o19m7MM9UCRa3LXwNdZ8imKwXGMuWr6YXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=MtBB9jlnQkM17YMbJZp5MK0URkKpBf_QQv1CQ_75tedh_jorVG_66QpWWAyJ7dA-j5R6WeibnYNZu61-F9tR06EbZ-XeXYUdy798gLJp3Z8WLfnRkQHJ7oSnzacvYwZhNdmqJpY53HJfxknDxJ7YxVDUcVoSEPiRwx50lURucs4mVqvedzmIgp5UW07Or0PCEw8bzc7awXjJQDFx6EBgLHGRKpSwiyRUa4FkcLbtQkUd2PapJ92GHBfgU9B_lz_NOiXZNfynsbQLVrgdD4rb2x85iUyqk7raQaWVxpLnXoXLbd_-bLL1o19m7MM9UCRa3LXwNdZ8imKwXGMuWr6YXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byCSgWlwGTa-ZcDd09kDtGk_AVTS25DcnWcQsE9QaILR2aeVxO3wV-4Kks1_AK9L0KDjVVfpaPBnwEnr_xoAWFgW-l_dh_Xaj_8RXZ8-EgH2ixxQ-yHcUNBz9JUMZ8b6ygSr2fRFjPcUqM4Q65EuUWh8KigZGNP9aggwFUFv4HGNOrUrjCsIOdNbeHf4XCNwcCwa22dFfrtZXNOdAla6LsxFsU2oAL1B8NYOUTz-dSEOmEbQ3KjL3KWOx0GfZX1D3Kxhjp8vtp1ZNLoTM3SJnBs85BDOcwzm8mMlTbYLP-YMKxcE52ISJsSG-NN8CykmLz-8bFYu7pyJ85sj3BNe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVNLCa1AXuINZSkxcqCTJYiX9027hEnDmbPbHAkBCVB275uCVUgdeELtX-J15Y619Fq_kgsLb_VnSxJTeVVgUBUj2Ho50AcDXnWvhU9UrZFMuahxixwjhz-LcOeK5dd1FY1snZONVjCNX61XiBTgybvtQ6byHEtelzhujSoy5edpEQuEsevlreNc-31hVmufgdzDzXVoLJIi3QN7xHOQFsYbEtqAMz6ClMHyvtOpm8zS5FjR7ZInTm_3zxtZwdI29SK4c1ay08VENRBWCy2AYQJID_LIJ6H5QSsq5ZdxDvdSEdPI-6TMgq2B3EukC8-qHXhLUtOrmxrbECmZ0JSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=dvqOYwB44ZtEGJESZFMaCy8v9fmGIZLw3H4N45OmGQ98G-NrNkG6pEKPGdhEp92l6Ay4r_He7YxwkkcX4Z1VS8dCgRm21mt-O8AIu4Lzu4MhyjXd0j6GNpbbUx2ucPMCsLQacXex2wMy_g4xFeuAH-KUh7A1f9VkqP9gzilRjU1DK6Q-MareVk6hExwYyVkPM__t8pibAG9z7xAuQTzjngtjiW41NxMxniSLq7wTCZzbeHNswbw4cSPpLtwheTywN6VAHbwLzQ6Ow0VRfae1ZITkQG1tT7q38H3yCNNfNyqe0zPNWDzTywxnDJVbsCMq5kz7eKcfNHy5BqslwrSbXAk9zVR_KvGmC_XZOtXoevUAtr1FSdogo1rQ0-65qAweZKA-rxSg22KkeOjMA3U5kPD7O3U9a9FVbWMrV6CQVT34K33oYrh-dGOCOCB4BmwTh9w__QnRq4wq8Ym-TK5cJK_bUZygw09cLXNs1K2F5QFqwQFVLmndSa9AdFxiO2Rusa9Ui2h0f3DWK6dHQ0E6DgD7uuxVGh-USCaNwT_9Nz7gFe69UkNY3qk5hrxHclVoij8IGfPJ9QQMZPMAFRnKMWeZnwMW52Hlp66sugVArgik35dj-Xn5k4fl4DHkf8sME3ayKJLWd9sgePAy1BOXfgvcPAHoRIBS5GaSegf7Z8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=dvqOYwB44ZtEGJESZFMaCy8v9fmGIZLw3H4N45OmGQ98G-NrNkG6pEKPGdhEp92l6Ay4r_He7YxwkkcX4Z1VS8dCgRm21mt-O8AIu4Lzu4MhyjXd0j6GNpbbUx2ucPMCsLQacXex2wMy_g4xFeuAH-KUh7A1f9VkqP9gzilRjU1DK6Q-MareVk6hExwYyVkPM__t8pibAG9z7xAuQTzjngtjiW41NxMxniSLq7wTCZzbeHNswbw4cSPpLtwheTywN6VAHbwLzQ6Ow0VRfae1ZITkQG1tT7q38H3yCNNfNyqe0zPNWDzTywxnDJVbsCMq5kz7eKcfNHy5BqslwrSbXAk9zVR_KvGmC_XZOtXoevUAtr1FSdogo1rQ0-65qAweZKA-rxSg22KkeOjMA3U5kPD7O3U9a9FVbWMrV6CQVT34K33oYrh-dGOCOCB4BmwTh9w__QnRq4wq8Ym-TK5cJK_bUZygw09cLXNs1K2F5QFqwQFVLmndSa9AdFxiO2Rusa9Ui2h0f3DWK6dHQ0E6DgD7uuxVGh-USCaNwT_9Nz7gFe69UkNY3qk5hrxHclVoij8IGfPJ9QQMZPMAFRnKMWeZnwMW52Hlp66sugVArgik35dj-Xn5k4fl4DHkf8sME3ayKJLWd9sgePAy1BOXfgvcPAHoRIBS5GaSegf7Z8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=Zh436LkqIFIp3klEgG07-RXf5PhQUh_dTRtQRif-yVTHqq3tNo6gI7mfxFL6bU01dGm7zgl9M3mE1SkuDfVNr2Q5S6Y1GkbOrx6cnJ9tOcCx1Pek-OIrd61qtf40G2kloebi0vq-54JYuScMELCKSkUiRdqKB1jAUQCUgzhoIyjwVnZScWJR-NWGDYdVInc_QST2L3AiyFoI-pQoQosG5b_7_WX6rhshdLCAKmGhX_QrBnVMABs8asf8G6fiRBVCO03tUgTjrMuk79JcAxIZS1OA1mOf1uHgAiKGfYmEyg35oiKRXpVOB39d8hqnXaN0KPHJCSqPx2AE4f_ds1eFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=Zh436LkqIFIp3klEgG07-RXf5PhQUh_dTRtQRif-yVTHqq3tNo6gI7mfxFL6bU01dGm7zgl9M3mE1SkuDfVNr2Q5S6Y1GkbOrx6cnJ9tOcCx1Pek-OIrd61qtf40G2kloebi0vq-54JYuScMELCKSkUiRdqKB1jAUQCUgzhoIyjwVnZScWJR-NWGDYdVInc_QST2L3AiyFoI-pQoQosG5b_7_WX6rhshdLCAKmGhX_QrBnVMABs8asf8G6fiRBVCO03tUgTjrMuk79JcAxIZS1OA1mOf1uHgAiKGfYmEyg35oiKRXpVOB39d8hqnXaN0KPHJCSqPx2AE4f_ds1eFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIyDljmYLknthG5u92JIgzbvRV44aBJmrYgU-Wo3_lILTyNGushXhLpjuxlKvWtuWQ9maehpt2Dx6-acfjsBWiY0YtmmNQW_5zZfj8DXM73CnTbYXIWAJd5f-QOKM0R4yZnpXTnwxDU4mLmd4bcpFiukfJ71_t9TT3Vf3Fq19Ego-aPfu-NvHQdpMuSKZWDwihBO-s8Cm-csKzqS-T9oVtp3-TqeCjLfeZlZsrh_EtL7Lcc1glix1gMdQCL8Ck0csXK6ci7h0HCEsLFEjYJjcgLK9q0GVGtuuL6X5JyvZHz72By8ziH0dHnTItX-WGQVR9yn37QN6gxfUYvQJwuMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=DoDCEd8xdexjUoKfI8RLHUXZf3_gsdkOltAniA4Wu6ZRcR4NRTbFoblWvJrk1rz3HuuXIOZZM3yjw-f-Qbh9nLnR2sdO5g6OAyQsd4E5XBH50rJEAx7aHdMWdc-bF4m1tfTiIwk35JyBd8EBaxEaogRqNSj-UOY5H6gM7-skRTuvPwtHXNGa2pP2erCjP7v66WZniiVE6EPp1LNIVHVYprh6Z6S46o-bFX1uooKrC_I69xbNtOfD8w-MJiGEnlm3gu_m6gv6ddrOvKuNwJ1XIaTjBFPA5HSMB4TCXmtuNmGEljkj5o-MVvwYU9INd0s_Uo1zznEgG004kH5Ffa98bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=DoDCEd8xdexjUoKfI8RLHUXZf3_gsdkOltAniA4Wu6ZRcR4NRTbFoblWvJrk1rz3HuuXIOZZM3yjw-f-Qbh9nLnR2sdO5g6OAyQsd4E5XBH50rJEAx7aHdMWdc-bF4m1tfTiIwk35JyBd8EBaxEaogRqNSj-UOY5H6gM7-skRTuvPwtHXNGa2pP2erCjP7v66WZniiVE6EPp1LNIVHVYprh6Z6S46o-bFX1uooKrC_I69xbNtOfD8w-MJiGEnlm3gu_m6gv6ddrOvKuNwJ1XIaTjBFPA5HSMB4TCXmtuNmGEljkj5o-MVvwYU9INd0s_Uo1zznEgG004kH5Ffa98bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtRj8dcbzG0F5TLgc7WuYU8l1RZQs9BtJuxK4fr1UyGpgZpFfCnLKgOlXMDHxnBRPBS6XMiSBVt53C3wdVzQkCftmd9LdcgcA5jlJnqyt-EurG84i6sNwNy6qatlqemzCRzH3FXHgg_vscwxeaCN1cqN1_l2pQthKg6eQAngFGlXUeZxmSaTQXIC4AYiDTHGWy383-y8qZlBal9oTHIQAz0_urN5jt8yXVZLY-qcVJRtR5jVfqXFpZbJn2aXQhkoUcDPbt-o4HKWoVbT7gncLdbXILsjoJE-yEijC-O50ewJCFqJF4U3BoeuiDYS7zllQt3AFycSACwlSHgiL9EELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdqnqAhMyhuuVAjKsX2AfilZWVvzpdtzTM9VZR6kCHrVRUPPkStAv1TU1rbWtez2dZ599rwNGvm5UTngQSYMVMlPCMgMvTk2gQNkduF6s-43kXRW0BUy-XzmbrvACbdUDbqSftiL3XX4Jr4frJENerVP81bSLvBWBBQEvmj7UnyeGzFG8i5geOhPehFeaICgB6C8vsjIxmRLfxeA72-kl7arufRb1b6ByuVBv_IIAIKwRcA4vSAcpdyuE_7ty0rKpIuMFBeWN50OLzKmlvtuj4A3UqJI6xVHHk68ZGwp09DXKroIlkGEhEXod0hXU_xahfbieoPnv6vIJ14vALdb5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=pmmdo_MKyQKbzEsmSaIJ0HLNTsQ-gRS79e8i58mYHEitBTrOUZdn-ZI43Lr-PBfqjRUwuPIP6O-Z2a9ac93cp0t9h27qMy9fCHIS4gP-j34wgUbdUg92AbD2inZElVSb_oI_rfLU6zcBb9IkGrHkxw8umcFuIjkvRcci1OWvvB3hVHhUOnvHZ32fSMFKSn623imWGNpIDklr7wWrmzPWmVXtRgLE50JLf1AV5M16MZmNkcJ0il-zcOkGLPbK2N37Vp1wpXOZnqJK-n7Ji6hJ99LzW0GAPeea3VL6mPJtg7LY4jSBRuCy42KLsAn4BnGsN_vBUGj9YHYHkODE9JzsHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=pmmdo_MKyQKbzEsmSaIJ0HLNTsQ-gRS79e8i58mYHEitBTrOUZdn-ZI43Lr-PBfqjRUwuPIP6O-Z2a9ac93cp0t9h27qMy9fCHIS4gP-j34wgUbdUg92AbD2inZElVSb_oI_rfLU6zcBb9IkGrHkxw8umcFuIjkvRcci1OWvvB3hVHhUOnvHZ32fSMFKSn623imWGNpIDklr7wWrmzPWmVXtRgLE50JLf1AV5M16MZmNkcJ0il-zcOkGLPbK2N37Vp1wpXOZnqJK-n7Ji6hJ99LzW0GAPeea3VL6mPJtg7LY4jSBRuCy42KLsAn4BnGsN_vBUGj9YHYHkODE9JzsHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5O7j680IKQ3wNSFJJrQubJ5BGw_ZDKfdm-TB18yag23OZdZrjfg2M5rIpiVfIdCXM5HxxFEk1zCyhmQM3iPRJzwud9LWkWpNzQY6PLmHnfbUWo0ED94MkkgmHrJ6wFHuVabN39L_odJ5bkrPjWDQaa296LTuxrb0sqoW5tYfGfRzeESlCTDq_LnY6CxGPVNe-lRXhQ0Qz76a04BOPpCTzupq9q3wlHikFgbSoklRZQ_rBQQ7Njry1XYNVXE764nRfQe0fN2Y7TKbYaFd_T3AOvGNagPD_uDpaCbny1GyerE8iJ9pEwHvZ6e3HKRTLe23XJZ6rkMF4w87FXA3nvqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0de4aIxGQUHTrqW0T4trIUCkwJZvUifjWJnMCaaAULopnQYauHAewv6HzVHocv5vYzMzoH-kUmWIQXg0MXJbi6hi_HFoahlxFsX1DTJepEY3VGst6QzGNO3Vn2BdWnH57o2JWQfsd4SZy9XKeorCq74i3B0zhgnBiK1cJSKiujpe5qNHmEYM8hT21CLKdUsgOynOAPwLfWZyzki0-uIS-Ld69pVlstmJUfmAzC4ZyFXCwdQkvMe4ee_1a7fgXFbnispeLz4IP7BE6TD483wdwcqjAijQloXxBFRjg7HtyLH8fFXVqh8kb6bUfx_2eCvIl5hq4i8JdSqqE6KvqitEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=DemKofjR6R168kafUnNCrqQjJTdIHvbGJVkMqabtKy4w_a8EP6e-sVkk_-GmXFI1LSKJvJFOjzDzYtsKXlXkWjWjouM8I09fBpg3df824TjnJh9zzMjMMfaduMHYF7cv88fh8vwHVtpH5RdZfdL0B_uQLoZO95POfKxsGmiOOUfT1NUlKgU15xhb7Ib3En5FfM9bZUtGNMSqfWcC4CrDCbjHn5zhhQZSodvhxH8sKFqS-9OlfvJZWmpeEvu6HvVaekeWu_VFxmo3aLShPPDK8bFQ2kLw7aqxduvCxLGB9e_m_d4hnGDAkOBc79IyHijr8H6Pv9lUIOmTImWmss55FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=DemKofjR6R168kafUnNCrqQjJTdIHvbGJVkMqabtKy4w_a8EP6e-sVkk_-GmXFI1LSKJvJFOjzDzYtsKXlXkWjWjouM8I09fBpg3df824TjnJh9zzMjMMfaduMHYF7cv88fh8vwHVtpH5RdZfdL0B_uQLoZO95POfKxsGmiOOUfT1NUlKgU15xhb7Ib3En5FfM9bZUtGNMSqfWcC4CrDCbjHn5zhhQZSodvhxH8sKFqS-9OlfvJZWmpeEvu6HvVaekeWu_VFxmo3aLShPPDK8bFQ2kLw7aqxduvCxLGB9e_m_d4hnGDAkOBc79IyHijr8H6Pv9lUIOmTImWmss55FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31049">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRl4UbnGcILUzi3d7Xmmsb3JhLLUPEQ-m-WtjaABo47jytCfEhnX0oH2n-zL34nq3OM7sSuNbk_XNL-tb6cyvLWnR0Eiz8ipuIPcX9_VrYt92bvoTib25AhVpGrVUGZ101Jwttj6DJAMnAbRmBPvdsi9s9Jiv8FXjwk5QfANL4qwjMVTLoHiwQOzan_wxS5o8u9LHwsZjAKnciZBk0fmy1_swUc1futX5YyGLoo8Yg1yXpTYJCS1SwbC0Up1NCLEKJvBxsi6rTGz4gpL24SXOOjWFL14Tdt4GzuSx4M1rCHURvSCu4kAMUENlEWvRBRn2DW3DKfvlD9B89CpebY8dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سکانسی جنجالی و جنسی از فیلم جدید دوس دختر کیلیان امباپه که سروصدای زیادی به پا کرده. کانال دومم داشته باشید کاملش رو اونجا میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31049" target="_blank">📅 23:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31048">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=AoTQSdonEinLsRNUD4pOPiFTxbsFL15HfD83iQcGJG2A6k7fmXaRNts_cbDKu6Co-Y4J83We96tzi5QgBpAH2DHRjLACEqyNqPwcQ5QMkI_w4dV7D1I2XbUhBMctvIzrUderLhE28Ltfbqko9khxbkijG903SwjsopIRdj9KJmbHoya1wP-m5_B3Vxr4YUe2aX_RUe2YjK1r_4ZCiLaEzP5vOisnz7vOa8WK7b3QHq4jt75rTHkbcVX8r7ARSJhIEcnmpwHOmUoVHB1JXrzCIOceLVv0utsuUwapxCUjp1F5OcDl6y8hBEH1MRXeOYq02GnWu5MzUtbeKZY2GaE_dY2QE2QhWcJqoNlNFNU-YGmJzMFFb1WIIDq3qWA2552pTqGeblhcYD8Cjqit0B42lMRb1_FGmGpalpqt8CNq2gLRt4EvsKdZrLfn4iLoAFF-IDAlziWhGANq2DPltIflI4HQdfJ1Ol6HTIj7keBU3FOay4vLX2SbMHtlP7NYQR6Cmnl4nud31hpVXYtJRPWLnoiyoC8dsOLRropWIasnIKQG06cqORWeu64RYB5nesDDvJ1q9NYwMz8JrO0j629Xu31bBiTeNmlcbkae7NWVwEQMii_JpHaeGQ-FY_SejDedbTOLPNUOjrIoQAu6GfFNUPe2QfXF0Y49hes6dhbLcrU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=AoTQSdonEinLsRNUD4pOPiFTxbsFL15HfD83iQcGJG2A6k7fmXaRNts_cbDKu6Co-Y4J83We96tzi5QgBpAH2DHRjLACEqyNqPwcQ5QMkI_w4dV7D1I2XbUhBMctvIzrUderLhE28Ltfbqko9khxbkijG903SwjsopIRdj9KJmbHoya1wP-m5_B3Vxr4YUe2aX_RUe2YjK1r_4ZCiLaEzP5vOisnz7vOa8WK7b3QHq4jt75rTHkbcVX8r7ARSJhIEcnmpwHOmUoVHB1JXrzCIOceLVv0utsuUwapxCUjp1F5OcDl6y8hBEH1MRXeOYq02GnWu5MzUtbeKZY2GaE_dY2QE2QhWcJqoNlNFNU-YGmJzMFFb1WIIDq3qWA2552pTqGeblhcYD8Cjqit0B42lMRb1_FGmGpalpqt8CNq2gLRt4EvsKdZrLfn4iLoAFF-IDAlziWhGANq2DPltIflI4HQdfJ1Ol6HTIj7keBU3FOay4vLX2SbMHtlP7NYQR6Cmnl4nud31hpVXYtJRPWLnoiyoC8dsOLRropWIasnIKQG06cqORWeu64RYB5nesDDvJ1q9NYwMz8JrO0j629Xu31bBiTeNmlcbkae7NWVwEQMii_JpHaeGQ-FY_SejDedbTOLPNUOjrIoQAu6GfFNUPe2QfXF0Y49hes6dhbLcrU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل در مورد بالا رفتن سرسام آور و تلخ قیمت دلار از آغاز هفته اول لیگ برتر تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31048" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31047">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=jV7bpgoswZwmTjedtbNZ6OcGzyPNYKFmO-58FdqMraL4cVwilfhTpIvb3qoDcj-xzxN5GSH9ZfuU34ErT0hEyeTj5o8-Ch3riRyYo3cZsQrcRHt_zSLy3kgaQPXEnK1RsRPwSFhiyXNyEBd1Z83aNv0TzgorTrBU-wSRjteYiU6QOcbdlQtTjEN2syHzZtu7KVLEn-bwtIWCSAKVsKrYBiz5A9KOCEjRdsPVMqZGGrvvLY739GrPUf-Z84rf1SkMWjAt2WODmu9Q89P_Yqp3n6RMV5HDgE8zyAsgsqSMjpDn8buBH7pkF5GYbiAPwvvzEoeWV1fv1q6CoRJkQDuqbYswMfJf4_ZOyMXof849W-fmHKujFiha6v5JVSRvk5gqLcUdyhcqpzr_55zN0O58YS6uUvyA8-DoBMLo50a3IEZabQD0XRomYkpiYZGbiipndA7JUflAm8U9sJORF6PGyjw0lYNKhYywsHjcCdX1-YszYW5c_U2DrTAvPIvTKlUxalKGbbGBm7p-iX6tgBvCtQcyEYAMEHEMJexXWB_XVOuWJz55gIMASb4cuEgWxUVI5sNEArIGXp83iAUJY433QAY0uauGWxpvQfKvvso7DbpD2NzTubVmLcSykpMlTS1CZfQnPrUktdC-2KfLHXwu7Fn_MvcbL_FzFVEKRp9XRJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=jV7bpgoswZwmTjedtbNZ6OcGzyPNYKFmO-58FdqMraL4cVwilfhTpIvb3qoDcj-xzxN5GSH9ZfuU34ErT0hEyeTj5o8-Ch3riRyYo3cZsQrcRHt_zSLy3kgaQPXEnK1RsRPwSFhiyXNyEBd1Z83aNv0TzgorTrBU-wSRjteYiU6QOcbdlQtTjEN2syHzZtu7KVLEn-bwtIWCSAKVsKrYBiz5A9KOCEjRdsPVMqZGGrvvLY739GrPUf-Z84rf1SkMWjAt2WODmu9Q89P_Yqp3n6RMV5HDgE8zyAsgsqSMjpDn8buBH7pkF5GYbiAPwvvzEoeWV1fv1q6CoRJkQDuqbYswMfJf4_ZOyMXof849W-fmHKujFiha6v5JVSRvk5gqLcUdyhcqpzr_55zN0O58YS6uUvyA8-DoBMLo50a3IEZabQD0XRomYkpiYZGbiipndA7JUflAm8U9sJORF6PGyjw0lYNKhYywsHjcCdX1-YszYW5c_U2DrTAvPIvTKlUxalKGbbGBm7p-iX6tgBvCtQcyEYAMEHEMJexXWB_XVOuWJz55gIMASb4cuEgWxUVI5sNEArIGXp83iAUJY433QAY0uauGWxpvQfKvvso7DbpD2NzTubVmLcSykpMlTS1CZfQnPrUktdC-2KfLHXwu7Fn_MvcbL_FzFVEKRp9XRJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فلش بک بزنیم؛
به وقتی دوست‌دخترِ کالافیوری اونو درحال‌مصاحبه با یه زن دید احساس خطر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31047" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHbDxZtIShjrAFY_yUAdDExkCAJkYm0-_Auyfp3M0CMEX3o5MrVf_Aq_nCr-e3r7n-zeqAGGM8fMmwT4nbycQt1TayzSnesvWbJMuxqiKcXMt4FZ_h99EOlStgZpKZVjbU0gGpgn-8VlM7cp961dhsDrpAau890r4EUjJ7OTUE60HgpJxWJcjtSgmO7ce9WPkFnRfV2Ucj9pUOK_07njRjNYSyr4Piq1yjwXdeHVJ9lyivoSFOpL3PXBnCD2nh7k36s_45JZ_IL5jHcmi0ERkozluI4BbHe7Rbrnw679TN0_NkYiOUmafcP3vy5Iag_fC2zVvsPGna33unmqCF90tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=G93B7GQElnlhsGRV62k-HLbFk7TJXjLevEMvhSi6MHMUWxlQDPIyt_2ps2KIDqCbcDgpjgqbZX5KW_MV5gtXw9GlC0PFzVS_mOvzohAD3gOkjBSumk1rTCqcyCPVBwxks1xaweOfpR6ZqlrisU1j4PTNbmrxV_avwWsuMiJHl-Ag32Q9n3gbkCxBAgNiqpnZy37AMSwZ2J_VpmxiAlvcB9eEw3T5xlha_GMYZbl08lVfBSbDW2dpijzG5QpnMy1719MDlfYrrg-Y4lzMR3tugz2r1eyAiOVIRx21zSRzVYnsz-8bJS1twCYxPqP2qq-fB5FLI4hWPycMePlWbZYMyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=G93B7GQElnlhsGRV62k-HLbFk7TJXjLevEMvhSi6MHMUWxlQDPIyt_2ps2KIDqCbcDgpjgqbZX5KW_MV5gtXw9GlC0PFzVS_mOvzohAD3gOkjBSumk1rTCqcyCPVBwxks1xaweOfpR6ZqlrisU1j4PTNbmrxV_avwWsuMiJHl-Ag32Q9n3gbkCxBAgNiqpnZy37AMSwZ2J_VpmxiAlvcB9eEw3T5xlha_GMYZbl08lVfBSbDW2dpijzG5QpnMy1719MDlfYrrg-Y4lzMR3tugz2r1eyAiOVIRx21zSRzVYnsz-8bJS1twCYxPqP2qq-fB5FLI4hWPycMePlWbZYMyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddp-if2Uk3k5YKVdLyM_w4iM1YCOIhF0Xkt9XCnJ9koGfQho1UdS5NgQK_K-x8SASecP17kj7NOmhV00eN7NAoFpSIaNTS87hCofxp6j6tcZmz4lpXewArbr6pfxGX6jqBMYeMCcRaPv9juIlTjJ1Lx4zWvGUq19PilMsfD_xqTptsjmmSRRYsWn5XaKllb1CRy3hd09o7FA7hPRe7qwDAUpdtR5UuBCbjYvfy6-I3Y-PdXnXvsEs4qyRuM0ge-KpSlhq_zGbAYkIeNxCuKzhs-iDQEVnslgrogGlryiJ8URr5GN9R-NdWOhvB0qPMcpu8gSpoQGu47lWHKzC8lvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kd-FdpXuagtYir5wde3TM8qNddyX9RyBLDK5v-T9go77A8bbSrB4jDQlMxy3gl2KXM60KcB2-1p3erqk__M_IwhNepT0NaHzi5m29bO2FCyZji1DPKMRjI6QVdm8IRNAY6OoqyZp2vLMaBwaE9hmQ8R2EH66RaM_nwW1nc1dsRs21Lhc01cdNpdQCGppNGMrc5cFQY8bcvzolpoDTvcDljViAuKdVYdWriGS6BeiIrbpaCquoUNJCwXpQhEETqT8KxhSt6ULqSV_2bBH_WSYaCgpkC1zjg0pHfeSzGwGS_XXidGwuK6VDtJs75V_R9xPPpdf7hwDwt_5wWmVL2qzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsVvPHKp3zvwCkE5nezt4dNudk52-f_x6tc99gGGQuKlY8CQS-t0J3cqUH9TPV7tq0l-lgt74Zc-dy_W249wYrZWSXPvAw4vG2wVItwAg5gKSPz-Fg3KVyYZxPJHtgy8lJAFmU-mv2DU-_ySlhwGz06Icu1xYUuE9YacmRJP2540w2htBvpYbkO2ygsq5iMX3MLCd5Ccioe-45r89dO02QM4m-zkdpj7LwU96UbEy2hbAOgm9NCy1ouc8c7PNo-7waoUlaOhHYNM_IHMs9oP-ssqY2r5PotKc91plNLJrzs3xHwyox6txDBvGIK0ynlIKaMUplzunXuFIKRlYR1YBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=MSdELBnmrTIOuDfBDv4b_aEvH0nNqYH_K_4bEXKi9gpZsKQ1JXrCRQqTjQY_5dHMh-35Y2yfG_xW1owEJmJgg35NEYysVTZSpyYmTVlpTNB7aEY1O3aGN9DQdhD2eOV4ceDgwkmfXBcX6p4AeScVo8MlVrwI5TwGtgGdI6TbJxOs7VA3YygMn040lVwtEATFCjxvOfco_BWP_umOKHiuHA2CHjioo5yXIVI5qsy1em85HqYpfbRqW3Uw1aLZ4xtJlqIoRaLznPO2Z6BDMhN_OB99Lz1CDyR7oReCMVKKHwed4ZdpnBsZlswUty80rwZWhHVzGq6heYCjdREtj7mnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=MSdELBnmrTIOuDfBDv4b_aEvH0nNqYH_K_4bEXKi9gpZsKQ1JXrCRQqTjQY_5dHMh-35Y2yfG_xW1owEJmJgg35NEYysVTZSpyYmTVlpTNB7aEY1O3aGN9DQdhD2eOV4ceDgwkmfXBcX6p4AeScVo8MlVrwI5TwGtgGdI6TbJxOs7VA3YygMn040lVwtEATFCjxvOfco_BWP_umOKHiuHA2CHjioo5yXIVI5qsy1em85HqYpfbRqW3Uw1aLZ4xtJlqIoRaLznPO2Z6BDMhN_OB99Lz1CDyR7oReCMVKKHwed4ZdpnBsZlswUty80rwZWhHVzGq6heYCjdREtj7mnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pryBUpsQ8sT7kj2EI0AzB-49efFMEEzO_Ayc3DNmnvJK0IsajGwZTp_oCV_FaipJiEbZMq90EHGY8A1DUwQcDTuRutk3uTd_B1Ro9fx7dS4Bvj9-TRbBDqUcG9bvMfqwA8E8wj167m9T6lQubr-152HyNe-QpIsv7XvJsFyJhdgF7gBRBexmLEON2J7jgXnD1--9iLs7bcWeLg2TtfNO32xsZ3IhZiDh0b1-fsu4e68vu7deemwnGFxnvZYPhjwigdXtg8H_Zj0pKSGW2jbEv2Bx_qRqIHbRdioJCsO1FZuM36jH9x0bzGnBcgs_kM4XmDSpDu1j18PlAmhSm8U5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31037">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T93bIWCVuSDjZ00CibZ-vtvXyiDjid1EcTZkM626cxyDrCyUalujVwZo_ER8A7_1YYiCrX67m4jmxIE98sktrMC8P0mPrQoJi2XAuJcRUyFirNxoVRAqt2fMTVkNMN3aWLu4Aoqbf1hp6Ykb3ETKDLcuSihsQASbnTLTz7wUFRx5mawHEKJ_T-JBmvVEkL8lJhPhYa7SOFNwSOjhltJ-M8p3JQPBdkbU_JoSJt1ZrvZrOHFFyFXWeT2pSukxnqlMcIUWYsdu0CgH6mEwZvhESiulZ26iXTSLy4SyQxAozz-sF5IYNy6RVawRIUlIFOQ6aGIgNcgeaqEituz5YXWCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31037" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My_VCe1d04of6qU4bTpOc0uzS7BckdDKl4tghVIsUqA8AusL0VcAHqX0bKdy6-DN9RA7x9NPqvdXjq5yv356TMmvnnQH61ecHyGucLPDLs5V43sxjnQRKjhQXEVb8DVydagboPmt4dAquqa5NoDPd3k6c7hjSaTFCMmq-QmFJ_lflrAPOkicz2gwi1DwSVSv9I7gYs1yAg6Oe3zB3sEh_A6qh3AFtEZGwORBe415gQs34fE2C11XMHPY4X9kKvqZ-ZNm6vPW6GwBvBgDLeQI54uhX0by__RtW4O_apiszG5V5bIq62CzhJKcsenboeqELdPtCBIfB5zZfzD-qRATMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌جالب ساغر مرادی و فاطمه از هدایت یک میلیاردی سردار آزمون: این کادو برای ما خیلی با ارزشه. سردار همیشه به بانوان نگاه ویژه‌ای دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31035" target="_blank">📅 19:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-jwSdQgnaFqXPVWItK_cO27kHVZcYuBGN17AwknKF6HJMrtYDx07TZikjqqtKjoKLdeKqABOErSSKfgkwrzCgDM4u3V9B9KdMfaGRa9Gu8yOcxCZqGKQ9xu-WYEVkoyAchX7mgoQHuqz7YyQZ0Z2Es31elW_sHsMyIHKcZvnKYRGfFSueTmTwgHaqBtjbufI7KvKx8U_ORwzVZClhf8N-SnmYNfWrZdJHmFytCvT7OtTOmbdbPlozeJ2evOPvwkSppPBISnqD6uWMKNe_2I5fHcr33mk391IKwci-hxgpZLO9Yl3IBn-BM3mWjEN4Rofz24sJqgwdvSfJvP927VVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31034" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1JHVxjp2BaFKe0FtPa4T4OmhiSkEyo5yfWWIqn_dZ-mT41bYZhaGIjP60IxJ_OR6SfXo_tTctR9ja-v0TVVpFLkva-IpXpS6j-aOnSy8P5XM3-e9q7Dde6ICVUFMUW_mZwgSHl9JUsIRxpeNoA-Rzohs6w3bP9om8hte5KY5MoD04M7mNVOPLsDJ8GPqoyiYKFe4CQ_9Rm_rNdSrFh_44OUpRSwTYEAKFYlwkyP2s2ktbo6hTvNvEhYhP7hTx7ZZWz89Dx2i3dBlxfCdDiSK8Y-TWJXtikeCt1eDn2rPvJFmSnjwi5E2XSUzeG7TYdYt6cWwwDI0qSDGmLp6npjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31033" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZV21grlaahO0c2gHrA-V6vOWigXwvJvO_RRDXbZj2WhacYreiFJn0YMHwVWpb-0OcOa-2h9SiRZ3gYTpukqx2jvARTNU5TfsxHPRZiW3nrFaMC1NUEJuvXoNocuEZyuAiMV64pH1pa9cm3MgGUH-Rgpxm51P79ygwK01r4a8wtzDGJNmG15BRgQeFzS4VwRZauAI_qhdzNTais9QPRX2ChsiHv9LjDKhXpgKv2kwiZbymnOQ1gHwOMLzXTr6qsbzcpofFmhA_Qe6Q6UiHNWmRSsqozXprx4m-T3r4y3kcJVfVULkxlb1qGaMjG6BO1MmxO1O91_eKw5lobJXLs0OCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31032" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5e65ci0cvFEDD--EGMInxrscxqyFNxICeVr0jd84eXnz1ENPlCijcSScZIzZu7NnIEB9ubXU3nUqqLc7j_BLfM2GcdNCy4c3vDtfFmUT7WxAiBzPK2jLawU2TYDAQcAy_hgwJwgS439OHoUcOIrSrMeZKhSOe1Tm9uE0uQj20fvRwiFE4SzltEfM8BfSHjZ5lw-OG3w5U3I69uRiL8jbQ2lTjNHI5I5x3GgiqY-eyfAQLe84im5Ob_lOThCQoRi2BBMJrguV8mateZMHzhHAftXix-Zrd5xe_WSpUX7KMwfXG1B0QWsyN9YN4PpelE62Cahjdx1bV5vi-BRIx84_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارش ESPN از ایده جدید AFC برای جذاب شدن بازیای ملی:
کنفدراسیون فوتبال آسیا بزودی با الگوبرداری‌از اروپالیگ‌ملت‌های آسیا AFC Nations League رو راه‌اندازی می‌کنه. 8 تیم برتر سطح اول مسابقات به مرحله حذفی صعود می‌کنن و مرحله یک چهارم نهایی‌رفت‌وبرگشت‌برگزارمیشه و نیمه نهایی و فینالم بصورت متمرکز و تک بازی داخل یه کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31031" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYUbPLjfi-eKUPXRDClQNb3KnZKp5d2tEbrCln2rropt0wWE7t1fDYO1XUrmdoJdQk9IfddHhXY7J9yfmpmRevT-Xec3i6z1478hBcxskaTwx68RV4lI31WFDGx4uUxRe6DDUit7km8WRgtCJuN6unxxLaRATU4gIWEOIjWA9JOx-A7aDuY6AoT5QAzyYSf1_kC700rKqjTFbzPCp5a7eC-LuWw3dg78pTJqUMbRJJwBEqPrObIGtW3HqKhqh9jvS4wF72oc77wyCrt2PB9zwVQhNDTO4iOo2ZJnYlfOz3SM91kE3LDdNPhHfuGbncW5Gz543_IGoUChVyDNdRb52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کلودیا پینا ستاره 25 تیم بانوان بارسا در بازی شب گذشته مقابل رئال مادرید موفق به ثبت پوکر شد اما فوتموب باز هم راضی نشد نمره 10 از 10 به‌این‌ستاره آبی اناری‌ها بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31030" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrZez2UN9_vxLh1drfYc7eYni1ti5-Q6i4tKBSDgtvOXpAtfhnERkBk2edUnmtbyEYulIM0UFmMgggTWrVEjBLFDoypRTlF2L64OUCtdTbQiL0BfXyuFwWZm518yKYLqJeixT7jgj_4k9CXVQOiAOS8eGsobfeXlBbxbHcsPRqcSKQUZfpCgttiTQyrSGw86NXmJ94qI99CuLV2b_YQEMNWTkLeIcolxpGbkudM8nBFE8WOsBUnlTGAT_A_pdNnSSNLjute9O0iQ2LgmAsYvOE7JOyzgWw0qJ6UfAkfXspi5d0_57ZFRPJgYC3tT0YazWGTTWwPoAHTxrsc42tQCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
تیم ملی ژاپن امروز در سومین بازی دوستانه‌ اش در فیفادی؛ دو بر یک نیوزیلند رو شکست داد. ژاپن در 16 مسابقه آخر خود در تمام مسابقات تنها متحمل دو شکشت‌شده‌بود که یکی از آن‌ها مقابل تیم ملی برزیل در رقابت های جام جهانی 2026 آمریکا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31029" target="_blank">📅 17:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=u7Y9rqnnOONfXUAqBgafzF2X82-ogOn2r6QTR_t2D3NWBDB_0guc4rN17HBnKd8YtvpyBqJ6AtfNFa_xrPodufPW8drPaqc3ks-L3XXVj8q2ahLzgwP-tfNRxkVMEktRBem5jswXWlIK4b92QmIfuMUEl6ofEZd6QQdcVrsxcI10jWjabzyx-NmF1xt5WhQ7vhAsjonGdc1D0UEl4DU3wBnFA4IQ14TMFr9ZRPmZcswMWswUHoappP7lJCvjVOCX0ChTRzUGQtmhIt76LVhA-lH1V2o7Vhjmc4XAfDvao_JNAk9vFCirInofAsALe2PRZgHtvtUUZ0wxh64T65qZCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=u7Y9rqnnOONfXUAqBgafzF2X82-ogOn2r6QTR_t2D3NWBDB_0guc4rN17HBnKd8YtvpyBqJ6AtfNFa_xrPodufPW8drPaqc3ks-L3XXVj8q2ahLzgwP-tfNRxkVMEktRBem5jswXWlIK4b92QmIfuMUEl6ofEZd6QQdcVrsxcI10jWjabzyx-NmF1xt5WhQ7vhAsjonGdc1D0UEl4DU3wBnFA4IQ14TMFr9ZRPmZcswMWswUHoappP7lJCvjVOCX0ChTRzUGQtmhIt76LVhA-lH1V2o7Vhjmc4XAfDvao_JNAk9vFCirInofAsALe2PRZgHtvtUUZ0wxh64T65qZCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌شجاع و حمال‌گفتنش به دانيال اسماعیلی‌ فر دربازی‌اخیر تراکتور؛ عادل: یه روز باید یه مصاحبه با شجاع بگیریم و قطعا اون روز دعوامون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31028" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrvoyQl2mc0pd3-AcIzgCzgP8LiyGioDQoxrldTYkoGFk_BITbCv6jVDCy5cypKTQjPLGID8045mcvsQsjjNMboCKxZ-ionItH6LrpJrF_5lvQ0EkbuiizP9FqTgjf3_JItK6NnOLKPHb73uggKuuHpxaqE0Akg1IhtelrHIhQ0Pkk5Lz_A9k_l6oJSF5fLams4P7V7a_PAC2xrMADKr1zYEc593aHR6lT0qb1AYpxkzMtuXda_Bvuy7bkTVd1fVzI0NbFYSkGtcDY1A26oDjsFST_Fg6COj_rWnJtabQ1PL91bF8g59OXwjglU7Ku2GjKGMJ0KV2TrWQB8NconYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31027" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=jcqKx8aTWqiGm5a3aGA79PgyQlFko2A036WxeEKiNi4aweFRyQKSy0mTMpVECuorvhYwH8FXrpeghTLrmGr8ajujgE8dJ-WgVqEG_CSczezdl05nl5HD_FJmBecoDgqkuJQMAqwVMbLyUCww5w7joklAoc4lfuzEQGuOqg1EoK4SZMO5jQyZGyLF8pQsSZGWna9fUxaZrwyoJHMg5QbmD6gQBACLYKcTjl6VUFHWRM-Xf0UT6WIoxd162F5yr_COslxscCxmOkPNm1IX0iNfJZnPad6V1lRrVIbYnepaR3cmKRnIjEC4o2MoViAsT25CEcpV9m0yxmAlgi2Uiy7Z2Tzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=jcqKx8aTWqiGm5a3aGA79PgyQlFko2A036WxeEKiNi4aweFRyQKSy0mTMpVECuorvhYwH8FXrpeghTLrmGr8ajujgE8dJ-WgVqEG_CSczezdl05nl5HD_FJmBecoDgqkuJQMAqwVMbLyUCww5w7joklAoc4lfuzEQGuOqg1EoK4SZMO5jQyZGyLF8pQsSZGWna9fUxaZrwyoJHMg5QbmD6gQBACLYKcTjl6VUFHWRM-Xf0UT6WIoxd162F5yr_COslxscCxmOkPNm1IX0iNfJZnPad6V1lRrVIbYnepaR3cmKRnIjEC4o2MoViAsT25CEcpV9m0yxmAlgi2Uiy7Z2Tzi9-jZJrK5lhZgizM9MAeTWAYlfZBQzcP55v8efELKiGX_HENe6NOuc_hVSfi5maRrMK8qnIJRYv7SzrkF7oPM75QJkSOGOXYeOSksBRgI01Ibom7o02w8UEGF4Ax2sITjwag6u9CHpD4FMvu3UsXRN481FKdLZyI5KYSZ7ExdzOtG_DRdBOGWLkJ5s6qYQSJ6fLujsezUfQfmlNuBoM4DdaP27pv3hiLNvOd9lmROrTG4B-HFAtOOrDsjc7DVD1ik3zKjKz7p2oXLnbazS0iwiU8ZBfCRc1mmmhL0ZJ-FeLigyYMeJhAgWn3DZ_hVhZv_YBabLs_C8RbM9xoCSys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعداد سوپرگل پشم ریزون دومینیک سوبوسلای فوق‌ستاره‌مجارستانی لیورپول بااین پیراهن این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31026" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=bne9PAh4USa51QTFZU4MZr37g8U4jjg8DbdpPotUezvWyg3vpDF9_kUdiFjRhlvpRRlf0gjJcYjDqvEorRCFODN6byCoMYszcPB8aiiWuPsG5m-yhWtH4W0GyYt9MnLcOZMbSJnXHG3ees4qu7BkqHpHzjfTpMCAZRPDIw1x7oz5UFFBobZh10Nug_ha6t9MocxTVfmVuDv390AL4ckMylZngnBqDXpFm0Fp3Pm1QZ3oJJs_BfxP6EuB6UGPl4gI3ZHHJbxggtFMyM0rlGCee5hnI-mjsSulL4jFKMaI78lFiekGWCa6aX_HgLXUTispxJ-YDyL6bwH-WbJQQCehIzWbz0MzYPHt6_DD65QrUhZfr7AEUZ7RXGwOeQ7eJpoHDFeeQ5HPiJ90iVAS2wgydkFeLkH1os3IHDPytYZwFCbKQfHAOC27sQIgIV9AS7gW0sLR0tzT1bxe6aKgIY8FX7cJmuH2aQUfmkvmRUiGhiKfCrsvFwIOzyow3YWYX-xM4I4zLe9-kUDBBkflBRdyOw0aIJpuRPzzJM3HxNt4pzRou4rnNYAe_NRi6BnyPRZ-_CqZz2O3YDx2ikFY-LiCfwrXgr0KUOLeoK2KjfJDDnNK1J6YK7bKbXNvhFnyRIJmgKKDXWXzQSLlaZ3jb1fVUXWrxgtKK9TGQXAaaPp_PbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=bne9PAh4USa51QTFZU4MZr37g8U4jjg8DbdpPotUezvWyg3vpDF9_kUdiFjRhlvpRRlf0gjJcYjDqvEorRCFODN6byCoMYszcPB8aiiWuPsG5m-yhWtH4W0GyYt9MnLcOZMbSJnXHG3ees4qu7BkqHpHzjfTpMCAZRPDIw1x7oz5UFFBobZh10Nug_ha6t9MocxTVfmVuDv390AL4ckMylZngnBqDXpFm0Fp3Pm1QZ3oJJs_BfxP6EuB6UGPl4gI3ZHHJbxggtFMyM0rlGCee5hnI-mjsSulL4jFKMaI78lFiekGWCa6aX_HgLXUTispxJ-YDyL6bwH-WbJQQCehIzWbz0MzYPHt6_DD65QrUhZfr7AEUZ7RXGwOeQ7eJpoHDFeeQ5HPiJ90iVAS2wgydkFeLkH1os3IHDPytYZwFCbKQfHAOC27sQIgIV9AS7gW0sLR0tzT1bxe6aKgIY8FX7cJmuH2aQUfmkvmRUiGhiKfCrsvFwIOzyow3YWYX-xM4I4zLe9-kUDBBkflBRdyOw0aIJpuRPzzJM3HxNt4pzRou4rnNYAe_NRi6BnyPRZ-_CqZz2O3YDx2ikFY-LiCfwrXgr0KUOLeoK2KjfJDDnNK1J6YK7bKbXNvhFnyRIJmgKKDXWXzQSLlaZ3jb1fVUXWrxgtKK9TGQXAaaPp_PbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سردارآزمون به ساغرمرادی و فاطمه احمدی دو تکواندو کار ایرانب که در مسابقات بازی‌های آسیایی ناگویا به ترتیب مدال طلا و برنز کسب کردند، نفری یک‌میلیارد تومن هدیه نقدی با هزینه شخصی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31025" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=lvSODPn8VN54K8RykBJkU6_EzIQLXSuzwuWghyikzZCE8Qqs11kcbG0V9R6BlyODVZktTmSuTTaZcrjIeqkN0hb-UDoUghGKes1Wjd2tZ8T-gbSg0eGQ69wDwdIS8KpbbtO5WFE4xTgdJ7B7METxgJpP2IurCY37VqCwSXvDBTehMr6fbdrUSFbfBPAHAJ7F58vBvRXJA8XQViVu9WF8BR6k0KcDkKHF6fBq0NuGngBW-pqtmLewnww_z7Z1E2oX_wSwLE33eJ-FKogxOkwv3wy0gAW7mvBHqvE9IhG0CJOrc8xwsyiRjQBPj5IRvksPUspqaw4-oQB7auVlBfXv2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=lvSODPn8VN54K8RykBJkU6_EzIQLXSuzwuWghyikzZCE8Qqs11kcbG0V9R6BlyODVZktTmSuTTaZcrjIeqkN0hb-UDoUghGKes1Wjd2tZ8T-gbSg0eGQ69wDwdIS8KpbbtO5WFE4xTgdJ7B7METxgJpP2IurCY37VqCwSXvDBTehMr6fbdrUSFbfBPAHAJ7F58vBvRXJA8XQViVu9WF8BR6k0KcDkKHF6fBq0NuGngBW-pqtmLewnww_z7Z1E2oX_wSwLE33eJ-FKogxOkwv3wy0gAW7mvBHqvE9IhG0CJOrc8xwsyiRjQBPj5IRvksPUspqaw4-oQB7auVlBfXv2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صفحه رسمی جام ملت‌ های آسیا با ویدیویی از بازی ایران
🆚
ژاپن درجام ملت‌های آسیا نوشت: تنها 94 روز تا شروع رقابت‌های داغ جام ملت‌های آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31024" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNgx8zpSS_SXHlnceJUh6-Kcu9fIioBcMCzBvb5Hpqvj8H6G7gi-wNUlJpQQxVYTykhZ9ukUTkVJCcoNll6HyO9DGX_M5tgCWV9eQ5rVGTAO1Op24vYSqLD04iMcasN34gvH8U4-72HVecqdNTBZTBvMXOKHEYW26IO2rvL2uzoNCciIBWF2VWy50z3hV2ogSObIi0WIveY-qSoAxNz_AUGFS6oW1nEnecXimsqf6RVLctstJeOqMUn-hrXmuUre66ETLd3KOkDSIdrFoWZvwLLHrsqr_kC0vaMmYEtyrjUd441atADx3Y70jwtPDTHZAPYN0ZdbhN9WX_A50byFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمیته استیناف بعد از برسی کامل قرارداد یاسر آسانی با باشگاه استقلال؛ با انتشار بیانیه‌ ای شکایت سپاهان و مس شهربابک از ستاره آبی‌ها را رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31023" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9UiNlbRttJjKJ0cevdQ3---RoFkO57-Q4G_RNvYc4mKcgAqzDdOVroF0C5R8ZQmK7k9D4ceDNmqbTigJ6mIwLJEOK7BNuONP5f1QJbW1Oe_-qa28yrjqKOdgFuBC3RncLxa0Js4VvvIM3RemcE6oFNIqhe1oaA1ULZGTHOtGqWxfUIt8uTxX9J4YcZ5_ULuFSjqmzuoZhK2MPVmzvhhOV-Ci-fylHBIN1NmS5nrCq9ySzYs49IPEKLTHT0a6oTdVMZbZ5adQc1WpL2WAg7ub4oMBHn9_L1zrNtS-NpVXL3Wh8H3T_uhaIEfCW2xkfo1huB1eTjwcYI5d2UbSbjXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ خبر کوتاه است و دردناک: لیونل مسی آخرین بازی خودش رو با پیراهن آلبی سلسته از ساعت ۰۲:۳۰ روز بامداد چهارشنبه انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31022" target="_blank">📅 14:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eefG-vPIRvIPzfQN9fFwiNy2fRZZQi70Lnp9QHOM9aifs9K1zINLf85677AKxfGRWrt5XdBM6PsSk7CZoE1Nq5utQSWndjAR-3YBud-5NEMBZA1Bz6_JcOAegas-psk44fiv1k7j7ZVE96FJU0IkjHaE_dtl8uSqCRsX3_ml0q302PM03xYDEgfNZwuk9G21jXfxVm2t67QjJaU5TPJ9R3fFngb1vNLnMMceU4-kOWCGaEhPVougW_Q2qUuQ8y8kybAOXk8aY3pjh_AnntYp9vXnWnsPnE-yZwX3nmKCLVSZK-k7_7UQxvz89PRI0JD2jwFthtwUZ5PUG6JfXe8unQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31021" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTf2ScygjNNAAqt5A-q__6vEsVHyXVX_o2_eN-bnlJXs6nX1_HUOP_tKROVVVzFIvgcZUDbZulM0Nb_0bmIm254tBpgng0BbupyFNQAtiKpAZJGYriHp3Bvn_qU2LFIjmwaKRiMeHbiFJcF7JSnNYsUxYzxSM0mW8K2Z2WaDpgiH2jTClXHubyEPmA4DgJkKi72uAKRwvlRjczyVBX_c-1oUpJdryZGXJh0zUNmm4ry1-cmNb346Q9uMUr01SCrtl9iRrvZwZQigEHZjvOhrsas99UAqav18-q2XniRzpgzV4iGcAfHOBkmC5TbySoC--04BxBOXUM3VgRgjelwVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7X7eVEFmNhzOCUnhjwJmzi4VntQpGVME0vVfZ00uWG-Q-xBU47Ifa5wvcvwAgMiaZAar0rAFMh2E6l7gdA2mWIzcx03mC8l05MJC7NmmwRtq48dza-G5qm06yH-QzZ16-CGsF3_SNgpRxVJqVZzWZEGCrgTjIDvTKoe_v99T5z2PPpB8xYkp67To9KaHLebu7PYeT8LEfcFMK2aY5PnT_RV7LsFXNw1wXvmbTn6ukZ5LD51jWbIPyI-EkzKyiymfDarNj5t0_ocmlEo399DMdB6ec4uDDnW1dPvX8s35CfOnOpvaKFQQCxRzms323r2cHKDntfPPDfm4xIMpX3lCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31019" target="_blank">📅 13:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HptXgHMgl6-9z2Wu8sRwq_JMSVVNIQl25JcF7FXBQHX_-ROJIfZnWsEP8Atb-p0E7e0pz-mpkal_G_yF1Xv2V5FRFNb2YYN6ucCxnNwx_r2cB30ciFyr91QzQaCcLj_d3WinKZHuYTXB6C9YzPdPy3NABc5CDDWXKaN0bvk0oJgH5HIuRxS41EmhYgxAOBkO6JpBudK5Lm8p0oRoM4RlAbhcMXAcmQsEEWy89IWBft2ZBHAWEppFtatOXRt-LuTv7z3tc9qxY74jww00JTYj4W8RKQ9TBr0_ZgiFScaTr1Q5CEdFV65HECYJamB1-mOR1e4h_92s_bR1HRlOI_h35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31018" target="_blank">📅 13:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=SUmYM8lNIpH9cmjPUwyNRUIY-PAYb3Wppkuj6o2j_3oW_obFY7w9nzrPq9NzD3_QWeRdgWz33OcS7f8ID6A9ET7WMEuhDd5Q7m_pJAbjqPxcfdGB3UHDc7avRGVcvTEAOH5v116v-ZwZOGdPmdYDXdPaEQfJFujStbiZppcaYaTTQOpvkjYJ3RHj0K9iD_gSTBU-lH35sOkTukAE6pHV07u4n7AtlQICU-vkHSCuZ1u-MtDnb4GMGpiuW-TTvzoYmRRgDdE92OENsAbOmX_njaREziCdC21GEr84tnxBKtj70EEY9r5C2rNik5jDtat201Z5sZERVRhlCab0MaqjhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=SUmYM8lNIpH9cmjPUwyNRUIY-PAYb3Wppkuj6o2j_3oW_obFY7w9nzrPq9NzD3_QWeRdgWz33OcS7f8ID6A9ET7WMEuhDd5Q7m_pJAbjqPxcfdGB3UHDc7avRGVcvTEAOH5v116v-ZwZOGdPmdYDXdPaEQfJFujStbiZppcaYaTTQOpvkjYJ3RHj0K9iD_gSTBU-lH35sOkTukAE6pHV07u4n7AtlQICU-vkHSCuZ1u-MtDnb4GMGpiuW-TTvzoYmRRgDdE92OENsAbOmX_njaREziCdC21GEr84tnxBKtj70EEY9r5C2rNik5jDtat201Z5sZERVRhlCab0MaqjhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
چراغ سبز سرمربی تیم‌پرتغال برای بازگشت کریس رونالدو؛ خورخه‌ژسوس: پرتغال همیشه خونه کریستیانو رونالدو بوده و هست ولی‌اون خودش باید تصمیم نهایی رو بگیره. من هیییچ مشکلی با بازگشت او به تیم ملی ندارم. یه سوتفاهم پیش اومده بود که برطرف شد. همه ما منتظر بازگشت…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31017" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgCIigJefEFwFgt6_mjEEu3gIlTQqeweE0xLLUK7OK-OmYhQcOtic3u5ThBeCJh7xgfopjZ6Sv0Vi8xpZSjISjvXvljFKegwPVtasfJMaiUr1R6eU3XnEmuluSPWUjvvtPokZskvP7NL26Djn9Z1Yz0Ayz129HkOqDM8eo7dFRe4vb1OrepO-mehwGeHWUeEdcwX8pKLMrMXITmFDfKkcMLcLUWJWoIYq6g3vDy5ApolFyRPmmnyiH7KyLrSoDxqwecwvor2PagZnTOA6PtDYrNnbN8gnFdpd8dM2wlxB7_5EI0EyuYvF9z6BX4yoJ1FTVHUaE096Hms-1ZjEp5XPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TpnQLlKm1yF1BWudL4I1yQKCHdqB41lrpaUVw2Sp1NsbTizq08kbRvg8zqBoB0dPOXuElOdLDK5rmJaowJPaShr_yqVOsYMMhHHBbWcZkwCEJudDVLD89iLAuyxDwsVQB6lOJ-ML3xs1uBWHYJGc3ifXA4aWQP8fi1OTNxGcdAX8c3yQcM_WpN4QKnH2g7Tg_mBknPZKzhBOXVZis6pcZiu4vCrqVl-R570PTL8IKge43OK0b0vvfYcfa4uzygmVvG6yAE-dh6pMx5ThNJHgFhR1cyHpF4qfMt5jePJZTXb9ZUXDwb222z0rnqsorfctuK6jnedF84NeBLQ2JoxTEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_ZnO-rTw2kl5ykL6GfFtIU1WZKzpEg40Lw0IFuAQ0lH7x2lcm0eUu5AvbgWcf98z-bFtA8lUetVGabAuWPmV0kBy60WX48tP91VF1rVtFnTxWJSSJGJxKCwTcv-wt-zGv0pHFuPBrRNHVXla3yjYSlrmtp4uF9o7ha10c-0nDNcNmZ4ybon95fxitvTn6I3yec8GWBhdj9BGLfaRfgjPTLEQUgW-kX23V0AwbOXqQ_PRr7m1HkfCZhCMpiGcNBV_JKg1oFH0mvDcXcgafzq7wxk4Nkd2u7bCByDWDgC9pzO6n784QxrJWOtQDUoi1zm-aUflRqJ871mTm6cC12YOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUTQwEE4zHF7idP1Er_7rrfHZHDibwOoTbu-ObhKpM2RYPZ8jqU6ZQXTQ0QlAhsvvvwl_scz75ofmxEidfijKCo6K7uaROocK9INaLG9DXlojW5d4YzX1If7nfYAAdWfPqeI6KM8CSNTJKD1CJC6fNi0LYsmyUg43Pb8b-GG4bMjXeRi_XaM2a9CbzLLbBjwZ_xK4IOPQEFckx1Qz3KteQ8RU_Pih5Njvjtt6w85y4JSw4ckW3dWwXNZyk8Hn97Ew8LWEa5iVwZ-O7JLDhXWM0z6UZ72I7RZH4aI2AMtANK2wkfAvDxfcopvei_HMxS8a6gR1mJyM33Gpss9nTKhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق جدیدترین اخبار دریافتی رسانه پرشیانا؛ کمیته استیناف فدراسیون فوتبال بعد از برسی کامل پرونده یاسر آسانی به درخواست باشگاه پرسپولیس مبنی بر غیر قانونی بازی کردن یاسر آسانی آلبانیایی برای استقلال پاسخ منفی داده است و بزودی سایت فدراسیون دربیانیه‌ای این…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31013" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC1TFlLS35FrQbjtps0zCi0CSyQCqdWz3ZjcpSwOPmEsgf70_tqntIToj34h6x_yC_Qp1kyKuJ-1LGWJexpO-cGTJ5tNMIXkmMCrEUfJE_jdPW2y339Juev1WVX7DgvbcPztCyloEN0RO6g2OsgYGB4O5GSVsN8j_wCjVmeC8aSjANWIeqQs3kV59WmrxbV1JMqAGH2wdOMDRE0EeM-SeA6-wzTzSBRUEYysaaFl7AZdSj188dIZls6TZBUZOKaKjcXUmek7Gtk85KN1qszIAbWBH1_XDbLFs5BH1s7Wp94LmfupHkf6R1aiLNg7zbpaj14lgAGHP-vXEGeHOCpfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31012" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8pwJA1nH2t-M6zDt_n9uRaOC9StlLpaZl49DPeh-TGtuoV0bzaGXsyhzurypVV6dYbIRsPXD4cHFm4DNA5qVCWb1xOKmPvkazXSBUFQrnLUDefIffgWzZkLDpFiI5Xjcitp_B_vNzN60qlYlr5kulx8hSPytraLZIttS8rqbtejM4q3OaAHtBKZbbXuBBTbZ8uiz_ypQcQBrJ3K7Muesinr5kratvizAxoSobZW7BS4OqjUuhzUOJpEMXj1HVagesjSdi2VYlsDgmU9bIY5n08kM1eHTIq_QZUhJp1gLkvoCuS8wuS1VJFsdnzm7xSZiqrBNZ8St_UJXPugL7VZhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه آاس:
بعد از فیفادی رئال مادرید قراره از وینیسیوس‌جونیورتستDNA بگیره و نتیجه‌ش رو با هوادارا به اشتراک بذاره تا بشایعات و تئوری‌هایی که توی شبکه‌های اجتماعی مطرح شده پایان بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31011" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=F5doepAr8Qc_5P25BhnCIT3m5SYVDeS_uL01EgmEWM8DEmtXlAL4HBFtD4o22BhR_jgMaX-wTij6rWrH0BgXEK_6zx8ZoRyS_VPgeP-Kcrk2vu_CwBEjWgrEwRk87tLiL5IQ2CdSCXtHgk0pNUsCYqEIf4wMrCmLaJ6XbsYzxs_ssDn_5y8Z7MHSkI28qO5zDgCsD7mRV0pgwZYkyyyHKUEWaDD7BW2xKZRqe3mjmZOYLpbr869G8rq8DyAhp9Ab5oRpAcLFSzMIyExYHGERwAdQmPxupo4l-DDcWxKmjZwpYZ6HCwtTIiwgfDxcdOnSD7D25nhjgVZqEkLs2ppgWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=F5doepAr8Qc_5P25BhnCIT3m5SYVDeS_uL01EgmEWM8DEmtXlAL4HBFtD4o22BhR_jgMaX-wTij6rWrH0BgXEK_6zx8ZoRyS_VPgeP-Kcrk2vu_CwBEjWgrEwRk87tLiL5IQ2CdSCXtHgk0pNUsCYqEIf4wMrCmLaJ6XbsYzxs_ssDn_5y8Z7MHSkI28qO5zDgCsD7mRV0pgwZYkyyyHKUEWaDD7BW2xKZRqe3mjmZOYLpbr869G8rq8DyAhp9Ab5oRpAcLFSzMIyExYHGERwAdQmPxupo4l-DDcWxKmjZwpYZ6HCwtTIiwgfDxcdOnSD7D25nhjgVZqEkLs2ppgWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تیم بانوان بارسا در هفته ششم لالیگا؛ با هفت‌گل رئال‌مادرید رو درهم کوبید و با شش پیروزی پیاپی در صدر جدول رقابت‌ها قرار گرفت. تیم رئال مادرید هم با 13 امتیاز در رتبه سوم قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31010" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct4N1rivJddHmzmxifWZejj9jJhb_xShuxjiD9rM7g_dKFJ9Hf-PE1S8fw2xHLV_ZEPyPU809JJYUSj_32uZsEcMM2BuKJlLdzepYvO-zePGt1UHWbmnx0P3YG_yhIwsfV7ZFzfqXH10hMz15NMMsBI-eBKVoRJWQsgeZAaLUVzuEBQA8YbUbdcy4aO89CcqwclgxmMqu15gipXg6a8Fd2ZIbRVR8GdMURQ1hmkr03XyuHDmB_TpYPCmaPCs5AaXNXLHabhad9pHfZgx2lirg_kKARHWBrcgAS7a2WVTMkKtbkKlYrsDOk2D2uLD9sCplfQlfImvrzlz_UoJvuk8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31008" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMeFcpcsNfGMFISGHOD8d91v_1ClBYWxobF_uNWJqghK8-DbpGadewRNQtjQLjLsDjNBk_u2buYScUa9YfxxkvwbdrogK_4N458efu1lZ06tUhct8cUM71Usriz7A1KLLYib3CuaRol6Phx7HrYPBO3fKom_THFpSTEssVenveVBrtHLCP9h60UKRIIbvau5GEdhepo96_zm_C62gUrLnGoxQ4sgmaiJ34pqFWP6Ukim_XiXfKZnkNib3T0nNaymVQdYuQLhRYiidc2jTgCnzB32ql2GqalfA-a9T-Tx1xx6TPNaMzf1Ewpkt9yb3aMbwCZ1UFCQzmrGnd4863fN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31007" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=UCPmpD5SZu2jyhH4OY5P4onw3ryvziSejVBUjAoSf2QGp0xTdF4nxGHFrq9nJ8fUboyIhe3wQqtth80eTwF_UdBJF1CqXsQRROjh7QYm3fZ4XLjS8bnOywRLOMo_OlRwAhOKYx3qhl4Pt7JIj00oB9kekSAe24GRWmL_6BYCUwj12RNDt6jELo5CqxdSXhlHw4cdKg0_Av57ESYuXSJ_XoiH0vCjPxQDdsfIcTgNt5bmwwcjiUSvFZjr8ZD6687f7XraKAbVZIKMQ17chOcoAyWKd-AZhfaKdMBt0XumLLSvzmpNuu0LXb91XoQkTfW--Q_2zXupSNyQKlLYijDs_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=UCPmpD5SZu2jyhH4OY5P4onw3ryvziSejVBUjAoSf2QGp0xTdF4nxGHFrq9nJ8fUboyIhe3wQqtth80eTwF_UdBJF1CqXsQRROjh7QYm3fZ4XLjS8bnOywRLOMo_OlRwAhOKYx3qhl4Pt7JIj00oB9kekSAe24GRWmL_6BYCUwj12RNDt6jELo5CqxdSXhlHw4cdKg0_Av57ESYuXSJ_XoiH0vCjPxQDdsfIcTgNt5bmwwcjiUSvFZjr8ZD6687f7XraKAbVZIKMQ17chOcoAyWKd-AZhfaKdMBt0XumLLSvzmpNuu0LXb91XoQkTfW--Q_2zXupSNyQKlLYijDs_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی اسطوره‌آرژانتینی تاریخ برای انجام آخرین بازی خود با پیراهن تیم ملی کشورش دقایقی قبل به اردوی تیم ملی فوتبال آرژانتین اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31006" target="_blank">📅 08:39 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
