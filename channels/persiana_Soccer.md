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
<img src="https://cdn4.telesco.pe/file/K7JEMbDI4S3D0s75jC35Oj03MbfFijuxTTrM_EE7ZJpJbo_8AjqCY5FeA7RrNoqBE0f-eeVnLxlxIGx1789CaxVXtOYwTjPE4FcBfO-ayUQqf-QKPuFxbGic33ityymom9X4Kyo8spMShEFGxl_5Sa59n2-qdr9o-zxtKxNrG5_17xzk27m6O7WTeVbu77wU3XnmfKYNxsyV1-xfGs5TZ8Y4IQNJ1baxPs-zxdXTx8M2C0WdXfNaOs1_YykNChwS1dYpuabmAnor3QQD_rMcXO3S1e7T16BW06C_L0bGvwISZVGjIhdssU8jHtC1qvir9CDn5cBehWg1Hy7VFqjqzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 438K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 06:39:04</div>
<hr>

<div class="tg-post" id="msg-30710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVEz4doFd0gVvJoPlQq1BbvwuRV3qvYvOsGt8wajHaIbEFHvIe0Xcc4YJlsZhX2BdRczEVfrdESmn4shVv2P24Y8nPz27ueIc7l6HKCTXThlUNEn9Nf5YJt5Bq66caVKE3ITG4ofHIxFbgB5q0Dh22wbV5cILJf_F_RxpG589zYxum2aOY3KJpSjTd7c0YRxohh6OyM0nluSpxhelAaWTgOqVgW5JK78_6-Lvw2vM93jj_Hyv894Dgj-YKL0P2fsEjgeCm9bSqgLFU68VbSKmz_XILDcL2ny87MU7mgBWx1Z4ow3-fDp0xclLgaejzgAfg57Ms6XrnldoZGW64MPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف تدارکاتی شاگردان مائوریسیو پوچتینو با تیم ملی شیلی در سن‌دیگو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/30710" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOpq4hEmenhJEBMmQRjrJO3PsyLyDXlYp6y1GWoEUbuVIpR3HQ0qxh7tRdKObSrce7xfjEdjRt93NxrIEYcc-7oz0uQgqxUje-BNzz3j4fo7GzSKnsnVpx953D67a3pw8Tec4cg_YUDRozzukzKkFe6e3LPncGRX9zE83jhZczyGi985-cEiqu4_AqunhLy--g019PmKDVAgpGsYmND_VuJi7qih8Kin9rPzxp_hykhb2RLztUEoWZLeo5s2rC_zyV3FaNk4mRoSv0pvwJ6M3bJt_bZG75zBoelk8SmKnkf0-S0YJDRnDtIG3eZl1995Fv3L9ZInB4V5dGkCvEpZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برد پرگل ماتادور‌ها با درخشش یامال و دومین‌باخت پیاپی تیم قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/30709" target="_blank">📅 02:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7U1hiYILN-Yv87uYQNFayQOOK3giWZSCz0_Co9wqGs1-tDpGaMjYIG6uGWUbmd1w6yAsRt1paVgCnRlAyzNJELO2l7vTaJL1WEbuIuBStdC1MFRPIEa9Dd9xcrn-9EOl2d8JSw1cZScpRSzN9ed3pmlkfCnB6p38Yrp1ZtTlbeGx4k0dAlkT_XTC0wD2fHJVcTpzNZGl4MycRH-2ezzpInHG-H1AX3WES8y8Z64KbqVmgBkF6DGoJJuoLXSQDfQCo-XGp0GTX5n_9EZ10q0Tds5SrlTz67JjRKtPw4M87ztftm8n3lcZHTEqfXG6o45u4jEo62WTGJnO9Gm7xBrhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج مسابقات تیم‌های آسیایی روز اول و دوم فیفادی مهرماه؛ ایران بزرگ‌ترین ناکام این فیفادی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/30708" target="_blank">📅 01:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIATTGQJ-vfzr9bfCCqngfArnX43bxbIIYZqFN0pkl626vl3fcIGjXUABF0xCo1cTZ8062-mWoA4zevs8sI5zVLmXu4sECO3OK10w1OTuETVvLMIqLAQsJ8zFFoQNxvVVy2YbSnu-7_zLwQSIEjpHcqDO_NvEQrkcweRsTAVdIekxpApcKDfdYolzXEpsHrqQhxcZanHctdiyQecMU0Cc9MKzAItkKtubsrP-SBSp9KltqP4igkIwMw-j5Bj0nGgRDRe5hlQWFQNwhEf-1PwO64XMY8Ljzp2nKI5DgH5BN3X6EIeELHzbtQ3xPJ--yFA35vnHJVbAWI-Z6iQcudeag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/30707" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuEcZEqMcqFvqIEyGJFUnYtudlOgcLrmrCCOQBGhmY2nOjx2xh_3p29PtwOLl6pYDE5421HhJfOFAjOcRQnnpFYYVGGe4FJr_B-w56aT7o6q8vEHi-K55TzWn3lvEJdaUWNxWYeTI526q-blxQrtUcV-YWh5AX0Fqmg4Q9_B9UQTKYK0xyz7hsEWEwPNhodgyFhMe98nMSQ-ZXnfY5BPGjMUHApGhFvQefFXDotPkRTBcti6ofnDzAFGTHnid3npYa-3RX6nmFWq57VhAgS9vPcrCm6LxxAvjECXLo1VhDX91bgQdYp70uMVghRCVCb6O6FbSNJ2b6THaRuwej3k0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با شکست امشب تیم ملی مقابل روسیه؛ پروژه اخراج امیر قلعه نویی از هدایت تیم ملی آغاز شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/30706" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEeoyG2QCl50X3xhS5boHx002F2NjfkyKM1nvVpGVVLOu-qYttylD1REFhhecS-V5sBdpMThTELa3wQoFfups5U-NrMsiFHMUCaZE92JOTplgbAgD6qHVKB68n_EmyvnQjHTIIE5ktd6Q0ahB3LVtSO37ZbiNWe0hlP_g6SyVla5TZtuPiL3AHzIlgl4OztHKOw5H3JKIchgrUElcLiidSrDiwHAEA9EDGeyXUhrRZDyWR91rzoR1IUalZ7TfAGv_yBbKUwhMQd0sAo2sOq86hNSCZpm6A65R3nDYiAZ7p3d3C2RKwuVxkjIOnPDW8crbxbUZiNoDKHkd9f1mwjiHA.jpg" alt="photo" loading="lazy"/></div>
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
P7
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/30705" target="_blank">📅 01:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1smZ2P12HRfRCZXhtmHEZoPc4g8KQJkaxJ-ExL3eHEH8xH09BV8ouCWDGuad2SE5eAAvhSImzvnCkMLHEVosjGY47-R28_B2vcNkFi3Fsz0olt00RcpT-YDRwxdQc8nCU-SP8WUu-YHjQ8J3oXbh8Emc5bPfM5alGVxhZq1Y4VHcbHkjUuo_oPj1ILjvZBnDEUVOAec-2TIXUvtLyUDVs0HsazHo8lFRyo-q-TA_hRMHa-B90TTcdYVuxcPKzVpS2KzNA8a6AVhQQIVoGAJlJPF0dwCtVH2NowTpXCqp3yoCZCphIB9lnvJ-550I5z_OpZQvBb4Q-aDQ7QhPOjsVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ طبق شنیده‌ها؛ فرهاد مجیدی اگه اوکی رو به فدراسیون بده حتی ممکنه در جام ملت های آسیا رو نیمکت تیم ملی باشه چون تاج بشدت دنبال اینه اون رو بیاره سرمربی تیم ملی بکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/30704" target="_blank">📅 00:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های اروپا؛ پیروزی ارزشمند سه شیرها مقابل جمهوری چک و آتش بازی تماشایی شاگردان دلافوئینته مقابل یاران لوکا مودریچ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/30703" target="_blank">📅 00:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY9nFbSN7hmuz_7tGfdXAXsRGxsmBR2Hgsj-IUv7rqpcLvVHaBUvOuVdWFEe2tU4MpoH-UsI3URH9dKlLNCVC7Z-hTmCmrNATz2vFV0zWSNZc9vUiO_1hK337BzfkGiVrI0p-wUOVdD3xNSUhoaFfP3kamE23BCR-iT-qaso-BsSpg7rhRgmlErqMQ6Muj5-5Vr5DHe1xl7r_Y0UyRWUAdTG5g5PxOEg3aY3sUtuA6o09dSsLVH1GQlxzFUhvJzyijVhVkHiManll7v6uHKPxrX1sHLxqsSaiMF3hBB58DC5i_iqWEvLhYI2evhv5XpsncsRxiKOAATSgFZGpb4bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/30702" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c014a889.mp4?token=h_kSMZsOU-km52jlx1SRzIrBqKJCD7ddq9Jxmf_LIRKFWYofv4TDLRgJWdMva9YV8pY6-ObyX6_gVehFMCEV8lVMpq5F1CvymRppmeJPtnJUsHViC_zlu7t-Als_uDcfjbcmy42cMukH2f_bTMa5_h2igvO2ScTuUCT9OSMY_rygyDywn3VLh4Hx0Ir-7fimexZ3FjeCNFN4SExHGrxunRa18yNx8FnXKiGGrCky2rg1_jb19JLUR0_mcIHHBexf6HHv7kwcKkP2p_5zMXRaCxCWnZlUcDGZgAopdlXgf4l2N9EbzZezaHzjVFDBcUznWnm7_iKg-owXyIFAMUK_WCCCvaGTHilORZVzSmtvQ6yjomnxyBfxDpQ0HhXt1LP6kd2MpVblD9IbNDtP32GXK_ABWF0LX53IyWJNWkH6PxbeZK9H1si5j8JHkKLnqV-c8RHC6nf0jIM6UERHMKNqXvizX0RXeOs_XOTEOlfatfnSBsthqkRX8tNqCPKFhQExAW_2HPNCRybOCvKOIA4f20t9iAauXk87e1xCfvFFWHNaC7F4xzghREaZg7KA3u2tKj7mUTEaGW12VcUWPIK9o8lusyHd9Qp7xEFgxS0n6X8DCE0Ou7YuKWRBu68yR2-0V8gt5UI1-NvY6ysRpbcqknwXWQjmMpN5S2UUfUC3Ei4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c014a889.mp4?token=h_kSMZsOU-km52jlx1SRzIrBqKJCD7ddq9Jxmf_LIRKFWYofv4TDLRgJWdMva9YV8pY6-ObyX6_gVehFMCEV8lVMpq5F1CvymRppmeJPtnJUsHViC_zlu7t-Als_uDcfjbcmy42cMukH2f_bTMa5_h2igvO2ScTuUCT9OSMY_rygyDywn3VLh4Hx0Ir-7fimexZ3FjeCNFN4SExHGrxunRa18yNx8FnXKiGGrCky2rg1_jb19JLUR0_mcIHHBexf6HHv7kwcKkP2p_5zMXRaCxCWnZlUcDGZgAopdlXgf4l2N9EbzZezaHzjVFDBcUznWnm7_iKg-owXyIFAMUK_WCCCvaGTHilORZVzSmtvQ6yjomnxyBfxDpQ0HhXt1LP6kd2MpVblD9IbNDtP32GXK_ABWF0LX53IyWJNWkH6PxbeZK9H1si5j8JHkKLnqV-c8RHC6nf0jIM6UERHMKNqXvizX0RXeOs_XOTEOlfatfnSBsthqkRX8tNqCPKFhQExAW_2HPNCRybOCvKOIA4f20t9iAauXk87e1xCfvFFWHNaC7F4xzghREaZg7KA3u2tKj7mUTEaGW12VcUWPIK9o8lusyHd9Qp7xEFgxS0n6X8DCE0Ou7YuKWRBu68yR2-0V8gt5UI1-NvY6ysRpbcqknwXWQjmMpN5S2UUfUC3Ei4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد سه دروازه‌بان تیم ملی ایران در فیفادی مهر ماه؛ دو بازی، پنج گل خورده، صفر کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/30701" target="_blank">📅 00:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMBIcXtmNtPxAKk1dKFTkBmlnuqwQKnkCAHjeHcNVE5PYJr3sPuWx-TomeLRiSNAWjMrWc56nUe5r_aZifG6qv0Wx3EgHT7CAFt2uYNmjQpmZIV1kQ88NFrVgn2XipbwpwoJuUOTGAKRvL8_OB7l8fjCrG8NA1vCj3nYhsCxljHuSa9NGNzHD_B7fqwM4CdXpxU4hnZbRwz4MGT0GEwuRScTz5vhBHb12FovMovRmslTH0ISPMovm5bJGkySjKE2qKIHNmauJ4Bzyo76nhRR6ymZrucCCF1-cC8tBW7qey0wtKpnHITA_j4P4cbFdEfgNKrOI-aZUjNh_Yj3SjgSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛ فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/30700" target="_blank">📅 23:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4PUbPaDTT94eIzfwj_F-T35uImPOPJGkhIxse7fYOYnJkCPUxrdrWoJCO4LyVQO8NDWD4zdH69p1fXpQ-kKotlq7ecP_B2ONbA4CFTchU1yJAPQNXSLRdEeupcSLvtq_33NVyVI0riQJn3g9o2pUfHNYKBL1RubFV9hCj8JfxppJJ11fzwMy8640PP-tkpibxDWCtA655up56yJm85Vgu7Oh1uC0-MH3sGY2CMuoStIcHD2eIgZDE0gPJ3E2gLbqj-KMTlxX77Ohl00akhRqvl2_VvzoeKMsEE1-CH-AQOzwL-eUu8jT2Etlf89FxZaEEyY7fO8mUEeHz8jE0uPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30699" target="_blank">📅 23:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42de6680af.mp4?token=Cmpul-cCXyJqqkgPyFvG-UxJELxBrxJOB37h7UbKaxxtWCQQjWGcMhr5gLupB40FUIB1-Vjgo3kxKZsu9JebL_vR0PY80f_XT3cDzP9XF2cj2Y_gHEPF3vkrze9-xsYTkVvGToY_JEFiiN5dbSQFQQyk_4FylvoDwCWTYbxic81WyHoI9C02dVFuDGbgk5L6UkFx1TNTwgF_rgraqDl-npKI_JvlkgjwshP5U6tulnCfZ9iY0QoP_VXynCTjRPscqmaJi7lNjKXRPGc4O6rMMPSFgxAJgUzgKhw8HKZPwBoTLL6w62-Oohyd2vFP9AhWSEzPZszHrLzK8TKQvhrPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42de6680af.mp4?token=Cmpul-cCXyJqqkgPyFvG-UxJELxBrxJOB37h7UbKaxxtWCQQjWGcMhr5gLupB40FUIB1-Vjgo3kxKZsu9JebL_vR0PY80f_XT3cDzP9XF2cj2Y_gHEPF3vkrze9-xsYTkVvGToY_JEFiiN5dbSQFQQyk_4FylvoDwCWTYbxic81WyHoI9C02dVFuDGbgk5L6UkFx1TNTwgF_rgraqDl-npKI_JvlkgjwshP5U6tulnCfZ9iY0QoP_VXynCTjRPscqmaJi7lNjKXRPGc4O6rMMPSFgxAJgUzgKhw8HKZPwBoTLL6w62-Oohyd2vFP9AhWSEzPZszHrLzK8TKQvhrPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هایلایتی‌از دیدارامشب‌ایران
🆚
روسیه؛
فاجعه کامل؛ بی‌برنامه بی‌تاکتیک! گلزنی‌هم فراموش کردیم؛ خوب شد نیازمند آمد! دو باخت، پایانی اسفناک برای فیفادی سپتامبر؛ جور کردن رقیبی درجه چند برای آشتی با برد، از نان شب واجب‌تر برای فدراسیون!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/30698" target="_blank">📅 23:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi_tOKOcmJ_qzb2jBjkSavZlHduFXCgcyaXjf3htxne0WxPpUratuiXDeyJrdMJWLAVbWWq76Vy1euNZcLa16neHbXVKwfCGcEXMI8OEVtbDddLZQM77XBSc8aKmRwYsUfPleBvdMbT1g97LoMWp_GBM8Qh88rP12A-2uupk3PUic8gTfmAHDDQ1uBcpyD0ZVTnYMppBhq80MRSpCGQmI0_0_9-r5H2BzPgWKXP8Z8RUekAJ8_jhiVtpiQPARHhS-d1qQ2XtSf3YAW1qh-Smlmo0smORX-0EKZq3br5fpDP_A26ud1kAMmPKoa6Jdd60WEYJVNLKQ4SJmGAiEqKa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توپ طلای امسال یه‌وضعیتیه‌که از بین گزینه‌ها هرکی بگیره هم حقشه هم حقش نیست یه جورایی. کی میبره بالاخره این جایزه رو امسال؟ سایت های شرط بندی میگن شانس یامال از کین بیشتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30697" target="_blank">📅 22:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVgPu5yMFpDWwmIP3qMVBZbZWrg58LIgsi6Tj9M03Lzzw9XL5MUq3gw8onxhTkD9V3QACbMTHyF2IWwqRtX7g9emRLnPd5r4HQR6NPqykjz7DYgBP2V64lT4vmITe6du9DUI5FMzXqYUDR0YeRayU2NzDr8EidzH0lhSR5jjBnyXbIpp0MCS-Mm8LXCMfLTdVlVERAEXfykSYnZzqQ8TW9e4ZYvLZf31lXRhC5xLxA-QqaF4uY7-5ZEV1wF3yODY8QLBMXCH804K7CdvhBCB_np82GvZ8zqGZgeOVkCilltFq_aFbu7suEggJpis7EYQUL9FGpmW5Ypt6WeyMNFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی؛ شاگردان امیر قلعه نویی در دومین بازی تدارکاتی خود 2 بر 0 به روسیه باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/30696" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZkKX9KIQvov0Td0ktNAReet2THfmlVTg4dO434VgMErKluDHkH13R_V5d10hUeAPLa5OReM9SpEwGmowyKZXyt1zeqlMVckXRBd9imrv_FHGT2kpseuV5SeTYaDlBawPabk6DZ6hGiE5_4drTzA_oM5H_7hd56Xc4VPQii_TPwGcDxRnyPShFPuuHr8v29JNwYLlNfKvAF5JZMgqHRQZI6we3iS1oBAZKSfYYaRmFLA3sH5X7Htjj5XbnM2UyxeEskFmFfBMC_STX9brSLvIEPRsT-rATBRKdMBsVbNW5iopWGVX_lsR_rcO81tE2pte5Gmlce9T58QGrZIwoBjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره ناراحت قلعه‌نویی روی نیمکت تیم ملی؛ حقارت سرمربی‌تیم‌ملی فقط اونجایی که از یکی مثل سعید الهویی که هیچ‌کارنامه و سابقه‌ای نداره مشاوره میگیره. یه استعفا بده هم خودت راحت کن هم ما رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30695" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=pa6zAmizOuB7sx1z5OE9JilX9bQIAU6iWwKqhSkx1ChDqP1-8OBaEjuJiwN2rKgXXQKV4uEHpJW8PsL4Y06cq76TstLEnNoq4cGCy9XxLlFXyZqiCf1Gvksif7GdjSkTJO5ANYPFG71sFxvkYMUQ4xnRLaTrhMJo2MPg4a5N4TmKPO0sfpdvkCw4_aV7CIszswDgu0QWJn_49aZ2kFOuwo7oZ_qgVniScGf_eaBEo6-J6pOLdEsiVTgHTxWlHa8zFgdMoUsj7ypY841SVltTJSkNuYfD8hmqXU1v4M0BmAnn-bhNbVjnw5wZOGx-F0ZTS9G5UUB9d1-jwg8a9-pctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=pa6zAmizOuB7sx1z5OE9JilX9bQIAU6iWwKqhSkx1ChDqP1-8OBaEjuJiwN2rKgXXQKV4uEHpJW8PsL4Y06cq76TstLEnNoq4cGCy9XxLlFXyZqiCf1Gvksif7GdjSkTJO5ANYPFG71sFxvkYMUQ4xnRLaTrhMJo2MPg4a5N4TmKPO0sfpdvkCw4_aV7CIszswDgu0QWJn_49aZ2kFOuwo7oZ_qgVniScGf_eaBEo6-J6pOLdEsiVTgHTxWlHa8zFgdMoUsj7ypY841SVltTJSkNuYfD8hmqXU1v4M0BmAnn-bhNbVjnw5wZOGx-F0ZTS9G5UUB9d1-jwg8a9-pctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار نیمه‌اول دیدار دوستانه ایران
🆚
روسیه همراه با نمرات بازیکنان تیم ملی در این مسابقه.
‼️
سیدحسین حسینی با نمره 5.3 ضعیف ترین بازیکن نیمه اول این دیدار دوستانه لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30694" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCAygj28hWv-0Y0KJMX6P0pBjtqYNMDa3aLQcBOwNTFOInsoiJlQCTquEtMuC9rZB-l7MieKzVmTiEopcfK1-DIr3SRyjN9LO0Z3TbVj32nwJkoFgEICFgGOuZt6FBUeXGwoIPMfNWUH-iVgDoAQKSurhrIeG4VT4-xphwz3VzGhCAMzhvFdDf4ElcFNGNLzP6E07lzZH9qgOse_hxhUIbsa6OurvLX-qCO972ezNeckmH9GfQn168LK5GoCOR70NI4_Ur4Vg8JE10nj1vTOTcds-BvcDbzfyfd38exW6iZtSSIZwMw5nw7cdl-ZHODxy5geaAG-XRDF319vwDDscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30693" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JejV5PSQLXN5rRO_9_qIkpXSZl8_Wq11oB9hCoiDhrdWO3NjLjH_gOj_N4BVMVtyOonioLPnpWs31buYitqL21DyN3Pq1tk-P4VBFDDg_Fqf6lABuI8JfRhcFjyVpLNgn6Xd8HMS0WHQGMTNR1GsfyoexlBiW9GxeG9WMKKHZLlDsBlEqvRPK6PvvYXEwdal0UowS0UgSMIPldeW98nqVRbcaWHQ9lQ3srsWNqGyhwqS3VyHXU6zpM4glsuUZG1gtwKjcHIj2o21o7UGETAb2_QY53Mf2S1Z83GUwxk6Jyu7N1-zU-MkrUqPKWwhOFCgNe23ievIOsDsTsmPMUNROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30692" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=aGxQih-fMjS6mcGT3xTtE8OSFsysU_swUy8RTNyAk7Y-vBH3N9wTf2oDyQ-XqXfnCcnwEo6RdWmDqReUsgh3AMzpUPhdIhBVRX-6DAY7sNEJSXxXDvrg_C3uLvMeR1i55rNtXQQ0PSIXWXwD-lX5AwXUiPNeGC2CV7pDZq31KJb3bMw5c14L82fFZKtnIaJIFFN2Zk6SggslQRc5JNHqHvRm0nNL5DqkT6LOzgBcUvcFlbt3zS6F51CepdN2cZ7HJqaNbeoMAMrDErrgzuLwPFlm2m0pZ1xg09R7h1SJmViuBTzFcgYRFckPhgD5P4hZy6fg60I3LoSneOZtFnHTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b7679a9f.mp4?token=aGxQih-fMjS6mcGT3xTtE8OSFsysU_swUy8RTNyAk7Y-vBH3N9wTf2oDyQ-XqXfnCcnwEo6RdWmDqReUsgh3AMzpUPhdIhBVRX-6DAY7sNEJSXxXDvrg_C3uLvMeR1i55rNtXQQ0PSIXWXwD-lX5AwXUiPNeGC2CV7pDZq31KJb3bMw5c14L82fFZKtnIaJIFFN2Zk6SggslQRc5JNHqHvRm0nNL5DqkT6LOzgBcUvcFlbt3zS6F51CepdN2cZ7HJqaNbeoMAMrDErrgzuLwPFlm2m0pZ1xg09R7h1SJmViuBTzFcgYRFckPhgD5P4hZy6fg60I3LoSneOZtFnHTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله ژوله به قیاسی و قلعه‌نویی؛
وسط برنامه زنگ زد به قیاسی و ماجرای مهدی قائدی رو پرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30691" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗧𝗮𝗯𝗮𝗻𝗶 | 𝗠𝗮𝗳𝗶𝗮</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl7Evj4qZpKpVIJW9MpcmEG07YqD3K2AEDGsj81XDFV_n6CmMBsUYX8tF43hnyqmVEqLq8BRr8da-cDwQ4Sn-dByiSawH9rVtqgc05W7_mG6byVK1rQgKxm2HWzYh-zcQnRZ_6JSCnvD3bAU5JtjvKa29zy93GSrKbGPuRS_GEPgt5H8vs_bOpYYcp2vdc9w4FflbS8FBF8IoyHyv01BQKVKofEmZynBviFzaVI2PGK2JiZGWRr_WL-PhK8Ul_lp5ckfUic_jHKRGJeaPfY0Xjs_B9C6iU4QU-TGrzzCjbZ5u2CCOBVrXFhcNXI3cnw4Wm8vSQz1CxJ3SGpC8f4kBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30690" target="_blank">📅 20:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHmhuyUJRH0dKi4cdC_Pr7kcSS4-8Wzsco1YiWwFpGqc3yPihDjNA0ZJSmdFZaAxmbAb-UjwRVZyHBsci99L7kRE255fh4DsSf1YotJdOZIM26QPujwixCOGxEHHTDGH51KkcTCAsVZHaMBWjGgwtxKbBbuShHgAXa110EixRb8NYmkXKBgkdzfzZ9uAmf7yyAF_d5QftVX2q_gjsUNy95Fus5rHV1TZtkFOLc8nnsB7ugBWlF07Sxozs98fdvpJCytPX_X9_rywl6fRCZMnObJMYzYzn2Bw-YcSS-VRZtEl67jPjERmlBguxYLxJVBiWHrGVtwYmRQ59wpmaHwhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBSw9dZij9YjG-jp1txJ2CFWcAyK9JZaVGmk3ADpwx2PATPvyoyBAieHqexoang5RiEETaagfrtnOMSGt9w2smWtfryv3AUb75CxqtGPhzDZ9KupQt-FJVdjeTzrWGOWYPlTNrs0Ye2f9sapwIbE3c6chCU18UgaAnhc8ah4ETRMTO1tbQC7OczVGQIQWvPDiMIugVq9DriYDOvQM_-Vrvx_suZBT3X7lLLBJJxoohligrHHNRBDrFKHtPfvkb38RfbEkUlk5qH13UjgsmJeZbxomOxp-Y0YDdFmzfAx2qZlfrLKHmVtHx1QfKZ_FB3yDuVBYWBO6k7m42C1De5h_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دومی رو به این شکل سوپرگل خوردند؛ گل دوم روسیه‌به‌ایران‌توسط الکساندر گوگووین در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30688" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=s8FuYUPGj9cAVrX99EzN-fUDnTtYa9S_AkCrQqpwlfUzzsd6HGnbCcxtuFIlGzZTxkm1bZ9sVqiRrozZeqnJLOHWjnevgNoZ2FZkhAdb5NiFAkxsHtZ2op4x7KDcIs_beWDS1ig6ZeXqErgFT0n1OC4tSEuuT0iCxPE5jf89FJrpd-Ax6EpmwGoZd-TzxrtVytHxxgSL7uwFtSxNhEEZAuWCO0MUxeewz8K3VO9dEpuzOoDf01Ug0-DX-mwvOTVtJbMd4slAhaveTsRYSabOOt-1LZfiLJ4S0kRXH7uAl1hzGDd1ZvzH1_qYX3oQi6jBrmVquTecpKYzyKQ-r2WNQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8d2eb7b.mp4?token=s8FuYUPGj9cAVrX99EzN-fUDnTtYa9S_AkCrQqpwlfUzzsd6HGnbCcxtuFIlGzZTxkm1bZ9sVqiRrozZeqnJLOHWjnevgNoZ2FZkhAdb5NiFAkxsHtZ2op4x7KDcIs_beWDS1ig6ZeXqErgFT0n1OC4tSEuuT0iCxPE5jf89FJrpd-Ax6EpmwGoZd-TzxrtVytHxxgSL7uwFtSxNhEEZAuWCO0MUxeewz8K3VO9dEpuzOoDf01Ug0-DX-mwvOTVtJbMd4slAhaveTsRYSabOOt-1LZfiLJ4S0kRXH7uAl1hzGDd1ZvzH1_qYX3oQi6jBrmVquTecpKYzyKQ-r2WNQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولی رو تیم قلعه نویی خورد؛ گل اول روسیه به ایران توسط الکساندر گولووین در دقیقه 21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30687" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afda25603.mp4?token=TX0mTDFLP5HQE4RW8W1ltV4bOoNf1MMIl2LluGDA-ClpsyytVyr7ZjHKKbV-YuVPFe-d0_qTzwearFrRf037DDooPs9uR-miJDpvsB41vSbgoY6C5CKxojc5ecgX9NhTP_jNjyT1mzK4xkhNzW1O523ISNIe0c_GAAeyZbCURtMRqJ5RNqDkErqANOucoYUBx9LOlNOLxXsILiMXrpm4gJxlGlwyq-MY6iMCtg1gHKhynjLMFOuu8Oje4QNzm_3j9CES0n8GqHjot1s-kX6VIoUo9B6cLSf2ItBvZ2GvGysmAXSgrLCUObNlvj4iB0vEjI968wO_gIw5w_JAPnWngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afda25603.mp4?token=TX0mTDFLP5HQE4RW8W1ltV4bOoNf1MMIl2LluGDA-ClpsyytVyr7ZjHKKbV-YuVPFe-d0_qTzwearFrRf037DDooPs9uR-miJDpvsB41vSbgoY6C5CKxojc5ecgX9NhTP_jNjyT1mzK4xkhNzW1O523ISNIe0c_GAAeyZbCURtMRqJ5RNqDkErqANOucoYUBx9LOlNOLxXsILiMXrpm4gJxlGlwyq-MY6iMCtg1gHKhynjLMFOuu8Oje4QNzm_3j9CES0n8GqHjot1s-kX6VIoUo9B6cLSf2ItBvZ2GvGysmAXSgrLCUObNlvj4iB0vEjI968wO_gIw5w_JAPnWngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/30686" target="_blank">📅 20:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKHDarsg67XMb08l7RdtjCmJq5tljUYf5ICE3sYGSafPPOEFfzc8hDetX7dvCU0-nxW944NRfTunq-0e7Wmcb_jjQvSKmycyb29BiK_tWoHB5drpYdkdsAU302grjUTugXlxAe3L9rgMY7hrDvDo9fdJRCkFMwm8nNVw61COmvECL0qsY66m4iYr9LpZtLTFpT96ILmxAQxZU34T_60NgO5LVD4RwGc1JQRhyAIiiMIKzquhiYGXqqDpvXzGO6XNhPjxF1ThWLn6aCqrs2ZW406Jvck8hkFSdPfHEgnjNEM_Gj9QJ-5BeY4Lk4KJ3UrRGV2C0WWISc0I14rpO8yyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30685" target="_blank">📅 19:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn1OFM7CODKMzdomTnBrjWsqJfiTLFthHiR0B_QHtJD2QDUunZ6478QbtdrZYup8U9H9t23CAt5Vpm-5YJtx5TnpceLPx1GVUKhvYrat5XCAIpoyMliydehBnKDLT1RVRQc15OYAkIP14iBuWkXxUYn0gl1MifqborchzGABpKBranfzJ46-ZG5O7S3_kBIoh61F5ABPEi9WhW8rg2CMqDJ3g2ZtJJxQP8h9k3bW0XYYBCkSGB9YYkU3NPi_OI8UZ_WgTfI_S8WDq03GyM9l1i4qCWzwLr2S2_Q215hrDlNqN-BD61SndkTzVuLSqE4mX8gRCunREaMop5ZSKBzdZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30684" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_oUjQik2GOXQxhER5QH4PS5z-KMPkEJkDj8ESl_ZDNWOIEbgbr_4mtGVIkckopGuqK48Uev60I8zI0pemSajijJ_30puWMdcnlGQfoFv4BWBZMYHRVYKnO7lhx_ICcknn58McaTsESralrBq47du42t8IU81Wtu0A-_kQPhPIm6yj86nsckTqTI7b-BEYVPr0UKzcMSC2_jtGkXxBuAxVzxVLDUo194CJr2FIDT-XCYDAZXJdpq86arGu8De-v74ZevBoTvqNhF9MkcDa30oVwZmeuCLGc-PZg6u24UHWHSVtaN7l3azq2n-fpBEf-jUmhEzgIqglEobcGFWLZKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته ولی شماتیک ترکیبی که قلعه نویی جلو روسیه چیده براساس‌پست اصلی بازیکنان اینه‌‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/30683" target="_blank">📅 19:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1xsMPhE4GeUuZWkJFz0qFRkq8-TiZKkHwOJdicL9QkOhmnEH10WySPFW9INWbKk4o6JRu9oZkCVjX8X2DNRQ_Hdul0aDhyaEdEjJQz9b2ycgZBTXfkr_ZarXpS_s_fvZNbg1BqIY7bHxUoCPPCxvURKOnDgO0D2gaTSokjnyBRyvgraQvGPoT9CcHQGfSgE-Y1NWsyXMvq4d92-_BgF_rozfPI8ZeH-ftYRtfLXP83WUODpVjBgAdbJtOaBXo9sdhpcHCIBoyuB4AJTXDpPTyVG5jiNQZpfhXeqllljTES-8-yLNOZhxSMbkYxm7eVSnMHbwDX1W62JFTXGxr3gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛ ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30682" target="_blank">📅 18:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZGpV6dKE7ALndG9hEuNnBSOLN8ZX6GzSGFRF2QX6QPUmAQW15HcCIcgwEAY06mn5AO2rXLMReaflT5oiWFKWEAXFZT-DG-WDUB7pe-KQcwcULqxsAOYU1SV5bD8OYz5w51AHxpYlwk_qnFAv20qlxkqef1JYdx77c1844CDxydMKvYC7RpSV7P00Nzi74spf8pmmf-1_oyhGK07_vk9jNk56zFu29eXMju8IllAkScRsoPjnF24pCwppSveP_f_Rt0LHkckTyax-ZyNvqYPOy3m-hZom8MGmgnK0scXhuItwpirnk-ZQ-u7uwt8jxKlHFzQyNWvNhVNU5SY6d42JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKny-cjtOHc4X1--BcqEHlBs27Bi79pfKSIa_N5dSxDu7lAo0mzBBJiLGjeb6EkTetPGVC6hDaAYaO0g-mAFddt7Iu2fnDAT2CbKpVNTLVkmJyu_hDxxEH5iPFLvsA5RthGREvjmuLYg9KMfxKN9iLKHXqU7_-KP8oeoiKfEXv4pJ2gcAwzOJiy3bkEI81UYL4p6z3dgZFt1HojVUheUls3BHFyF-g5rBzx8bvjLw92OXqykv-SWBZp1eSyfeKLYKyiW_DFSrbB8VcuXMXo2AfXC5jIhgpRR9uZvJtQAybX_Ey1xV3ysn_WiPsWMGVIJAcG0VRxNbF6OitZ3EChjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-llfwoRKibYtMVx5UecwAP4RALeBkzA2LXP8quZr07x4EJ99Amvkn_yFb5_YRH16Cc_ACRrer9Oocf1TGX0owklR-l-AA18lyC-OqgMbU34qYZAd7aO4Xq0lITs1ORAvAaC2AbTFTL0EFwqy3j6dyhaFc3QH0BcC9bNjVfR7seJtjMSexYuJJ7mJy29vbZ-VMUprQOAoULBMMNeKvxHR0ApN6qA_KLmL_eVuSxfeEMO0D5wBqdb7dF2Al39cAmBcKixF8OByxyFA6TVhvlu_qVSHlL0cTkmv2_IqCLT2QEYjGPtJIh-eVsmkxQukWG50ScZ7o5PxMjKP7DAL3cbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAJRt8b5KbkimJsFo8b7l-jICKQNlTCFap_ppOVlICx7EW2OBKbu0_rSg5H8KpHKKdMVR2CTKPaSkn6M_gbqRToQjUmxztpvdgPFfibd0FzwB4oCS1WjUrN_WY3_s9ncX6vgrBhrpo_dudlHMZRyp1FT7WkkrJpnPEUU_-a5bI5nhHtE0c3qkegeNtkBvzpqgABTH6-y-9v6a362Y0RhAfQTwf6d041dMHvlVtcACQMbJBQ4hE-JEMFZps_nEhuXZ9yj3qLxC1gPXaisWP7FnC9yQLIOPyEu4OrINbnuEQfO5jdtRA7hQfy0jhOnYxUejLCXqXZ7qGiBjC8b-BnUTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=AydTMoS0B9wMvrg8TJWr9bGuG-ucXxzsKeXQ_boGPEDpBMaM3TX7RzflajbJzQdNEBLRWzd4M-3s2cncc72siyCdjX7RFletuv9uhJa3p53AO8cSC7DccAgokH6Jlc7q4kosqGhSPbkCZrjYB-Mq-conYX6_icawUzDc2-doYMaMrFKRp4CmRGSIX0WVcv5NjAzyw35IrHrewP0M_tZdbPqvnCqvHCSsY8DVCpXuO1p6s7ph5dBisWC7kwETByzhao1Fb04SqR8tvxViVXfnf-FcyBEfjwNlnCuBZrn5e2YQDV_4OPSmo0IBWsZIpWwQvuuf96NZjPYj8fbj48WuQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd12872c42.mp4?token=AydTMoS0B9wMvrg8TJWr9bGuG-ucXxzsKeXQ_boGPEDpBMaM3TX7RzflajbJzQdNEBLRWzd4M-3s2cncc72siyCdjX7RFletuv9uhJa3p53AO8cSC7DccAgokH6Jlc7q4kosqGhSPbkCZrjYB-Mq-conYX6_icawUzDc2-doYMaMrFKRp4CmRGSIX0WVcv5NjAzyw35IrHrewP0M_tZdbPqvnCqvHCSsY8DVCpXuO1p6s7ph5dBisWC7kwETByzhao1Fb04SqR8tvxViVXfnf-FcyBEfjwNlnCuBZrn5e2YQDV_4OPSmo0IBWsZIpWwQvuuf96NZjPYj8fbj48WuQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابوطالب‌حسینی یه‌تیکه خیلی سنگین به ماجرای حضور خداداد تو مدارس مشهد انداخته و لحظات با مزه‌ای از وقتی که دانش‌آموز کلاس اول اون مدرسه به‌دنیا اومده رو نشون میده! عالی بود از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGkVKWMsWct_ZgODx_VWSGh2hD8Qv6VvjHGDbJKtofD1jio48OgYH8DvrJwnZAoFWhwsIuA4Br2Cvy2RWNOoNFJ2O4RlO4wqfF3QrHYIRP5c_VKKnj7b8x86UpcOn6pfMyYLNxLilRzVNtWMNW_bi_vf9Vf_wDRSb3cu8mGzuO8yVfVMBYFCpEAiMlK-1rIJHfOTc3rxtA7-01mKseDZ2ex0qdJ1NXHuPnOTKpY8fkm9GB_MgPfugrRFvNwsKXqBc0-3AGjitDa03QoTienfgJ7fGf5HN8TUXrrCj9wbBX7UT1dvE_3CUx8nDQoWyGhEcoHS7k5lKj5xpHrmnziulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNfNhREIXED4GvXZFB1Wo8xhnwN5nZnkQef9VHuBuA7_oBgNCrkKENhBTTiHFGdBz39huOCMeNsj5_aCP8hcX0W6yeqUaJhaolgpGnAjyA5i47ORhsiHLa4-1GQYU7p6EjG3ycJ6cMHMK2MeqvRWIUvTnII5Xecb-OPM21zG2z70hyaPAlqPzGB-xhEbiNY6UZ4BQLhLoMHN1UNzzAKVp5cHINKc1Iiu449Jh2XT318ki_TDxjyHIwm1o8J2buoeEOGSH0ed08lcJBueOp0h2mQGy2kneIvQ-jaI18No9sQHOpkqJD0SpGzbiwYf_BiOO1IW2WEtHM1X6oQLzGpuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF-gI_r3kBSHI96aW-mbe9Axl629K3gL0Gi93k4g3gZIOG2caH4qLX6j7hGpZdhTush5lxHjVsVVWlGF_TIySh-38-LdRBOGiF8ryCHRQS2Irp2KXvUIYy4Z8uiQyNRhiVZjt1XfQuX39ab2XlmFDfY6SzSCvbu0tWzZMv2gsH8lkB2sNUBUOSw4LlliJxR6Z__cZc3eElYZ33I287FMjhY6Z95i_Jo9pKptC6N8_DVh4vUE2NfPmtEwVm9WVgwMFp6E0gBkSMoDpqENZnRJuo_SwxZdmxC6o_PCSGCUYmS9q_teegJ9oCDBg_2Dm9rSkO3zgzqEPirgKm78DNxZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEm0zFm43HnrG7tGcsfksSW60dM54pOYqpFd8lwuD3_s27S2jfPdxE2v_BzUdeWkS5_l2OJYcGq5KcyjVQZdcLm5cdEZaMWYduUbu_oPdh1lhBQOXUf1TQ61CD7r9uPbMTRCJ4T0DQuLG8ycSB4y2HD9wp5KJYaOvawxJC9e5pdAd5AzbqVcl_tnwwfCgif7I-2pzk6pPOBTzoyULbeiqMkrChpLiZuV2YdtnTGn5Ob5NGx5_Y6TaK3HtnVb_GWoYW5NLL2Acdn_5YlX7bWd7n9cgtN2a-rpqlFMuwDm2w4bCkfkuG1xjJuOCL9O_6B1id67ejKyL9g1l0pzzlOQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6x5i6FoYpcPCjLln5j64keiOvdFeVjutKYT4ZjcgJSDW-Eev3TqgGky2Lwbh8FRy7UU3yJTN-FBnjbr1G2eHDll7z65s62cpzDy582VIRMs8pDeT4cLXvbn5siXVxbBVEvqmqTJAvWla8S2-7JGK4dDm4WjCTzA3x_TWAh8utbn-NEcUPCPXYYGlFglwe0MwLa7Lwpu3yvH4gi-R9DzMeohjQd9ssEgveM8DA6MMefTSuNrCk5jz-zdLNZSyGriJIQx1cyuivCqM2hFFfk-vcR3VA8jOfznz7buhmp3kbibnKLJ5nNuBaT7pWmB9yHmDAfr8zwxzKuHCsAv3gQmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APD2MmHtwqazxcFgyjEUoqTvzcMkQegMIztVBy-qWSu7Uro6X1_SByWuLWkqCo2YbFpjD4auaEqy-eJmwywCpYtnZK5H1NIPChZpX9KdJ7Seu_hGlMSQBqgeIrRhfufYe5XwIwTehAL8HFMvgIICQ25c3jMBE2omJOKXgWbbXL7GDNa0PxVwBFZOfHvhBrEYyo5OecNBmgvGbTukmEBdEKsz-tCPtJc1rF0asiLS0nvF8afX8wRCjFqCOulvZSVGMlX4bTnxkQfGkf3gTdsLm9EWTQzubbMkOO89_OY3hdVzzDqu6tY2kXo3jbVntOiwnTx0TN0IJtMY9xqZdU8-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
تیم ملی امروز در هفته دوم فیفادی برای دومین مرتبه پیاپی امروز ساعت 13:30 به مصاف تیم ملی استرالیامیره. بازی‌اول بزور مقابل کانگوروها مساوی گرفتند. امروز بااین ترکیب به مصاف استرالیا میرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30669" target="_blank">📅 15:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmFBINKOgV-Cti53k3NFIriy8wAAz2JOpCxj1KmJk7ifxUdJTCA4FVR5Y6oLlGVR2JdQztA04P0FEwF5KM59WuvgpWITbM1lK7PI2GV3QUafnUHrBiTEoDUpvVvOGL1ywhvlpiJtElT0PJpBaFNzPOW8Jlo1C_UXcjbktUJVRqC6VioRyl72NcdctetUCejUTCu66yMdZ7n1D6HeYZqMQkVsr3qbVKU48h9-WbLVzwXGLw7cIHOblUikzYgkAL-63m4xiHTAPxqvpI3JcwfMru0dMtlDc-qLQqUQFgPujPGKdE1L6NSDO0MioKqf_9EYbZum4o8r5fVIChoE8sgxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30668" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVkmLqkYaNDmLFA8XFj3esxcLl5CGd5RlGJ8kQm2PZvQfMuoTfF4grjtBYiDEy6KcSZbb9kUz1d3l_uDmhsU-AgrauX_qam4A6S76qX7JjRSR5jP-96673hLeeCt24WsXOKC-rTOOIUFQBNLf5k1R5t2ZckxZkqQNHRgHbRAFKOVbxvlRrz1JWPdn5GQFinnThE_TDvMGJOjao_I8MTq1UDRUENNNqXP9mibhgOxupQ4dxISdxZMV4oSA4Ec8eze56B-OB-CNBtiTkJs0GkpW3tQmCJv3Eandh_DDz7ZzJro80xPtJA9IGWPNkGEdkP5ylJQHb6lwmwunnMUZpCdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سه خوشحالی‌تاریخی و به یاد ماندنی زین الدین زیدان سرمربی تیم‌ملی فرانسه و سابق رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30667" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
ویدیوکامل‌ویژه برنامه شب‌گذشته عادل و برسی اتفاقا اخیر فوتبال ایران با حضور یاسر آسانی ستاره استقلال و دانیال اسماعیلی فر و شهریار مغانلو دو ستاره باشگاه تراکتور؛ اینم یجایی سیوش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30666" target="_blank">📅 14:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
ویدیوکامل قسمت‌دوم برنامه فان و بسیار جذاب ابوطالب حسینی؛ عالیه حتما ببینید فقط رفقا یجایی سیوش کنید بعد از 24 ساعت این پست پاک میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30665" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX-v53cPOqnG2FBxMbcGmeT1CBBCPyznz1mbxEWCMB4T7pBXTQ1uxTugLHWWfdckpCN-BQ0Q59fiXIkNBN88JNLmmIjY2KVM5yW6nTz-nDZHiZGMIjatCx1xV3X-FdK93e3rjXo7UGmQ6ahJ5F0qOSQrTzvuZ2aUpdwdIfZBMbe374_c5Ybi5seOMwGAvDOwxbsWq_uwa6w7hk1H1PnWaJgK8w9wg_-SQBif09Ipke5ipS6PdtYBkv3nSyJAPWeQhwff-kRi11twGZ3cTsXbq01JrdoOici6-rlfYmACmqTra0dc2GraP5YkEYnW0MyIfRgfW3eeKNt29KHfL8B8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30664" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=EW1aMJYYYco9nk5EOzf1Dwdx5pQCMeabwwp-zHtpGrkjZLDUb2M9SGVqPkdyYaqxJFT5IGLqE7RCpPRjUhkeyq8fjvvBj2dAKI5f6q_vink3mml4vytm3OoKeAsSjFp3OU9M4sd-2KoBPErd0_Cq52CbjbHXNgnrirC7DBYMIPSTtDlKkCaz7_mcA6Vankd5cd3NT992RI8l46K5o43d1OUekEzqlSzgX6lU62ohlvrrX-dsYVOfu77l2p_taA5BbkQ2TFrqY5l674zjrr6KIFmID7Poo7eaXAcro3420--Jn88Trg9ndtr_vg6TigQMpGfdUvE7K7-UhopTTzQflA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=EW1aMJYYYco9nk5EOzf1Dwdx5pQCMeabwwp-zHtpGrkjZLDUb2M9SGVqPkdyYaqxJFT5IGLqE7RCpPRjUhkeyq8fjvvBj2dAKI5f6q_vink3mml4vytm3OoKeAsSjFp3OU9M4sd-2KoBPErd0_Cq52CbjbHXNgnrirC7DBYMIPSTtDlKkCaz7_mcA6Vankd5cd3NT992RI8l46K5o43d1OUekEzqlSzgX6lU62ohlvrrX-dsYVOfu77l2p_taA5BbkQ2TFrqY5l674zjrr6KIFmID7Poo7eaXAcro3420--Jn88Trg9ndtr_vg6TigQMpGfdUvE7K7-UhopTTzQflA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30663" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzhLRyo-WgR9wF6hgf6NiQQSPxCST4QGK_yxviJVjl10HwxEkAkj6pBG5lw15bvJwlWRiSriO48TMgaFRz-p7j7GHwHBg7LeB-APAVrMikI914Lon4BWpAWufDRgxvRXGrxvCzmm3_wb_IaEmit951BTJI1IdgNxLPY7HfOtMGf21tkeRjs0M2b9rPlQ8kmisfFO_weR81dIjOaYBZdqVW6vnaOXYe5ErAFR42hkavp1tO-MfEljOKFRQiWKxn3ZgGNt3yCuOpizJTXHPx0tW8jqFHBcT6n6OAgVF4AN1AXUjBKZmgAHjCO8dT9uTzUsQQptJRBGS0QwmnHGW0iOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30662" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=A8zRS6TjGtWY8bOvwrWISB9l2ET9FvmtThvotvfATBmQCksdWoSspUrNCLv7y9lYcLgleq0tWJQe1QdTwrar7SUwsymVziULgZxhG1SKAC4DOKmyBQCwtoosseMoxENsQFk-6pFugXlKq1CAFm0gVA-rzp9Dd_SH9_blnoOXvLoKIghLPnF9H8gReBkNrqiwdzWqAEGC5vn73sia0aHq4By6VrQql0OFLVMmDiuigPmyw4txU7oOmpm_E54JZorY5sub8VFKxyrjBLTVrHfYJcWq9FMBf8rq8GRtjLWrJSA9F2Kux-L1Bt0cpAlQx5i1avab2patUF4nFW9rC9N23Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5f074a0.mp4?token=A8zRS6TjGtWY8bOvwrWISB9l2ET9FvmtThvotvfATBmQCksdWoSspUrNCLv7y9lYcLgleq0tWJQe1QdTwrar7SUwsymVziULgZxhG1SKAC4DOKmyBQCwtoosseMoxENsQFk-6pFugXlKq1CAFm0gVA-rzp9Dd_SH9_blnoOXvLoKIghLPnF9H8gReBkNrqiwdzWqAEGC5vn73sia0aHq4By6VrQql0OFLVMmDiuigPmyw4txU7oOmpm_E54JZorY5sub8VFKxyrjBLTVrHfYJcWq9FMBf8rq8GRtjLWrJSA9F2Kux-L1Bt0cpAlQx5i1avab2patUF4nFW9rC9N23Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارتاکاشته‌از لئو مسی فوق ستاره آرژانتینی اینترمیامی از یک نقطه در کل دوران حرفه ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30661" target="_blank">📅 12:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXyUNr-tZXQQkC-LqhUpjBDpfPPhtrm3D81rgpnsimBYYe1_Ne9Dzji8FwQQg1dTHJOpGbVKIFuidZace2SKe05G-xOwppGo53D6Ke0mAPkrvYuhQ2KW1Sg81fNcH8SN1nOuCHn5i7FNdyt1mL9eoBCXphzt4CHHOmjaCNYY3bDZinqxsix5pIwuqWrpFntzvKPio2DxEio8LuDT4DjrP-rr6zQsIVFQWjTHDS5m6uG_D11YG3j2rJcx5Seh1R0Hk8RoZ_zeCoQHDn1qPtm-RDn1L9nyUiOW6nOVRP0dUkEofAQFRxVREg739hD4Nz7R99aAFZmGA7axsEIizDxpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm0RQs8S_BYsGV7fOKaGOkZRy6jm7Nbojq3br1yecF0xexcxRCLO4cM6qvbU2QQT4RVW1kTdDHp2wFVqGjLJ4ONPxqAftClbktqXRg0xZsRWclBSBSXOWFezMXmPYZoSHTOoVqzpQv9dl2cpuLdaqZqiZNiq_58cJx10s3dGBeIk7M1Fj6XNrOa1XxkPbq-ry6qf3IYf0Ei6S_dKxHBOXvRqImur-FL9djCluuxkp07hUaosjW42WngKHZVWGYoVf46ObL-cHTQUx54m3zDlpiyOkI51KgvifSLtysYlA1c_iNjwl2yD6BWyaKJzBVY9CujC0kpTrNWSMTOG_xGdCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=u57cWZbu4c21lWe1oxfyYmrmAePWSJIDCrZmqFaUOJHTgColvB8UD40lROH4m447Sw3L0Z-s3UVkFkHUIE-st5dVKGCMJrIifvoyKUlGJlsyk3A2Y7Vyfbh-SacqJcyg4qS1oYuXXlW9Id4FIHtpcsUMZR1PQUzpFq3EXM3U0e_qw10wh8aHtVmU6OMsD-5Tmk3cfqn2fxOdI-inhjyYfTSfYP8uuyRiFM5XH27aUbsfR0hUEaJctVUha1FbKcx1RjCAHxBuqNDQV-vjx0OVFE1gLb1n00dMszSi7ojiQBNr5UqI6mtXWBPMirlB5Q93_hUdXWyNl4g-xtfmQ56Ca5vY-9paGCiM321HtGTY8wphawETOfVhHrCewmrHT6JPDXc-V4qHkwplt8AgxjU9ni6TJWurVbUecTMUe-4Bspd-smxmcesA2XthaW3SGhoxUeHPAB0U45euFYzXqGOOdmuJx3Ej7R7XWOYLNhQYgbitmxyeOFRtZX2z1gzyFuXA3E6nI6gA7If4wHJwzk6DWMdvdjg0Xpx16tXB59kf4C4oaQeiYpzDP77yu4254gpbFBqVT3BZQoNEcyKaIlaNUFWzrU1QeLfkZDy5EkL_rxW4uOTGXR2m0p8v6GtUpBK_9G3OsqxYlzskJWUdbZSUCiVba8DvQhZcRMe_jnEqP4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=u57cWZbu4c21lWe1oxfyYmrmAePWSJIDCrZmqFaUOJHTgColvB8UD40lROH4m447Sw3L0Z-s3UVkFkHUIE-st5dVKGCMJrIifvoyKUlGJlsyk3A2Y7Vyfbh-SacqJcyg4qS1oYuXXlW9Id4FIHtpcsUMZR1PQUzpFq3EXM3U0e_qw10wh8aHtVmU6OMsD-5Tmk3cfqn2fxOdI-inhjyYfTSfYP8uuyRiFM5XH27aUbsfR0hUEaJctVUha1FbKcx1RjCAHxBuqNDQV-vjx0OVFE1gLb1n00dMszSi7ojiQBNr5UqI6mtXWBPMirlB5Q93_hUdXWyNl4g-xtfmQ56Ca5vY-9paGCiM321HtGTY8wphawETOfVhHrCewmrHT6JPDXc-V4qHkwplt8AgxjU9ni6TJWurVbUecTMUe-4Bspd-smxmcesA2XthaW3SGhoxUeHPAB0U45euFYzXqGOOdmuJx3Ej7R7XWOYLNhQYgbitmxyeOFRtZX2z1gzyFuXA3E6nI6gA7If4wHJwzk6DWMdvdjg0Xpx16tXB59kf4C4oaQeiYpzDP77yu4254gpbFBqVT3BZQoNEcyKaIlaNUFWzrU1QeLfkZDy5EkL_rxW4uOTGXR2m0p8v6GtUpBK_9G3OsqxYlzskJWUdbZSUCiVba8DvQhZcRMe_jnEqP4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30657" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30656" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30656" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
WePari
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن وی‌پاری
💯
ورود به سایت وی پاری (فیلترشکن روشن)</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30655" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOa1lLp21vPPri_Rz5t706UQw6XHL_bMnecqZ4oejkAHL37LhcOeyl4YyqyJrD0MKjyLTsKq7y432MDYifd21X2JFM3AyNy-cG2g2MilCxvZoZ8J40ndVa4iKCtqs_jWGJHXsVUrt2mH4F3U37cnGYQbGuK6CiM0oIDnLsCd2utmw6EnN1VmH_12QWX2xvYjC7dTaTdCH66uelJVm0236k6L_843zMYm3K09vD0hewg1QC5jCdvnYwRyE7tSrznorwIqXNWg0jBdiNP9WERUHQ2SAjGD9HBndG2Ef6L6OpnwDEACrCyAJVAafeKl-glWbGYIp1M_7sfLp9esFb8OIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30654" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-WKvc6fOuqB-hIF3Kj810pWs767ba4fszCz3hyCYfx8Iy1s09AIAa12LBH80EJjnczAX4As0BYOqCPzS4dcEIi3uTNJKzq8sZc1Ujiyzm2OKdj9KLEG-0z1LduwpFSYPNH9lOT2S9Bwkn3e8MIvWDY0a-czWECaqSaZtCcIN4__NgNY6JFd_c1S_JuOv2_f4cbcb3Hiw_9y5GZqGJvYsPJxJiAzCMCltke9oqzGaS8hvEU696B1r0x6-wxuaKp2MAI2j9WxPe7FBR_JBzrhtnUAfQsQJCKVF-Wh-NaQaOuArGa3mqfsCxangF6PLSMWgpPEaMzAu-utnBP1FYXGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدار دوتیم استقلال و تراکتور در هفته هشتم لیگ‌برتر به احتمال‌زیاد به جای روز شانزده مهر ماه روز پانزده مهرماه در یادگار تبریز برگزار میشود.
🔴
سازمان لیگ این پیشنهاد رو به دو باشگاه داده تا برای بازیای‌آسیاییشون‌که20مهر برگزار میشه بیشتر فرصت استراحت…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30653" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmkiJEGGtMjUg0oS0D9nycSMAn0VVBMF10Yy5FlZTjdCHykI-kl59q--SvudK94LaTFcIqEiHdZrHzuqL6E5TIZuTvum9Dgy7lC1rm-fkmG6ug06uH9WpnoMsnzPfE0K_HALKbTkSGnm38xpQYqcNpBm9luBmZhoJzMP8vEsfVplmhAAiCTp7SnsBAhDQ32SoX3oHjOpIFcbyXWlteNrCnZZNv3JaQxdyNMiJ_6GW3qUgTLoP9Hc4XKWtb7UnxXNXF-VL5G4rVpA9uNgHgP-GeGYaUkXvZHuY-OzqN6K1DE__kvCSdgnJE2xr_DvZqDISPaeIjkMu0DyYzhoUcD_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30652" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=u5XGiyS-M2bvc8devpBBBRtm9DZnaNdTeUZABCbK_1Vulaeib6ukag67sdtymaEZUv6UWZTwe5ZQckdhv5b-USn_Lr5bdDr7IAF-Wrhf9kYk8AOBN5IF1OwbXUmaJ02Qz9uCULCigPL80kayCdx02NiPFc2ni2VjhPencKU8ud-rX7DSyVt9E1kH4P7fv2JgiL88MFvDRX0whIhWX9cY_FfznnDQiUhWLW5lqiZj1h3YBzxoTFWtSZLa1Er7vtKUCjg-lWaOkfiytNxt5gBsR6Z_nZ8QDbl1_0f0QVZ1SvKjiXxbWHu6Hi_i_L02wVAwAIAqVOfnHCj_D06XcL2ysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=u5XGiyS-M2bvc8devpBBBRtm9DZnaNdTeUZABCbK_1Vulaeib6ukag67sdtymaEZUv6UWZTwe5ZQckdhv5b-USn_Lr5bdDr7IAF-Wrhf9kYk8AOBN5IF1OwbXUmaJ02Qz9uCULCigPL80kayCdx02NiPFc2ni2VjhPencKU8ud-rX7DSyVt9E1kH4P7fv2JgiL88MFvDRX0whIhWX9cY_FfznnDQiUhWLW5lqiZj1h3YBzxoTFWtSZLa1Er7vtKUCjg-lWaOkfiytNxt5gBsR6Z_nZ8QDbl1_0f0QVZ1SvKjiXxbWHu6Hi_i_L02wVAwAIAqVOfnHCj_D06XcL2ysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه های سنگین و پیاپی امیر حسین قیاسی به امیر قلعه نویی سرمربی فعلی تیم ملی ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30651" target="_blank">📅 09:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD9rUY9V_F_JROz2vt6VxsPG5dR9ojoNOKRzz_r5RNBiGzZS1qT232MBg8KAsxLqpleimYp93a01yaQ8jf-Jeayjuoq5axSZvEBLZXWod1efghQYsMcB2JcYOo8lKUKvoMcAxDiEkH728atihOYlCzxr7rT0T9UvrgSy_p1WpW_zBOSU4FCTZyKDoEzhJhLnhT9Ps1d28EfiJvyLD4AAe1PzDtMCBfkaI2vskMcCjlG3o3wrYIHNz8ZpiSF6NONKijWbkD7GzG5iSMx_Hpd3VrYFIQnAJNV7dMhTo0q3ntbRlCByB42WfiVgnw0firCm4KbJFTJjr2ZS6meLhxyhFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ معاون‌ ورزشی باشگاه استقلال: جلال ماشاریپوف بازیکن‌قانونی استقلاله و قرارداد او اصلا فسخ‌ نشده که ماهم بخواهیم قرارداد جدیدی ببندیم. ماشاریپوف تنها به دلیل مصدومیت از لیست آبی ها خارج شده بود و در نیم فصل به لیست اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30650" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2pTab5zXvBhbt36UcBNCE4Z9BvV5rGcNHKLqqZ2bQH7fhfC5q9myPqLgLxtVraXVq_NlcOUDdbReflNjtIMdJbOEvpMn6Iy_ZCbEartmkZI1-MiSy7dYvFjV5AGXlbEptHa43K66UoGvLmQJvyIOLDVp2e_tmQ1TeZ9pJGQ8YKyB7NnSZeEHxfaOgHcPJQ0oRbTMHDiv2f5byIAuhc6wH3nJovAla70bhcO-fPqeIopigH7bzXzHDdLfmwqTE-QT8DU_TkaZMNXQL8CgbmKzp4ygVOt3Tujj23XTq-49kKT2m9GBsxmoeR4dE93D4_sZ1XARKJUcL62uUd5LGSjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFGhRN8aInTiZHUoDvzyW9pAovhjtfz8TW-Do5f94ajmm2OFIJW-AxxVi_SUpBVrGwgylz-12aIjs5D-1OT7_VeccJJ0wZu_qCyEneGj2fa05jggB-1A9f_wcWjeJX0BqK7lFxp0A1Q52mUES39zriFlVQurK-L1aZ7pCSbm802QqsekXHAWXOIXvpf1tSCXYN_PNyBBEBZEyzLcuoBaDLVqdPbI5Id0BqwxjIlDYqRRg8ZDhyFy6ZSdbWZtIuj3QjIFeG0dxdAQtOn6DIxZ2A_diy_VjMjoH9_gGqoGiiOk5W5oqVQ3O8JD3el36HCYZtny7_Hpefi8BGzapu1cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=c22UqL7lIUpIGlcJQIPiAmyqAMHcIkdgZZXBT0Gq3ykWZRW6jXtOrVZw-ipz_XLyIBVFBqpfs2rVKYOmg2QlFS-NKpSOiRAxrMrgRxJE4y9wDZV41GXONJ1yKWBxJBull7jdYzVKjRzCq_PmutfDT9Uq1gwefNOcBL5gNzSPCocRbOORYdpHuxavxeAQw7wj1Qcc4Cg6UFWSRpCE4K2AoLbLYZ84t89lp4v84nn8MymqcqHykcYRIyYDdQsFaGitn3U_-PLQk1FbN3yh5jNF75Go-ZpmrxDwctm1yikHcLbNn01U_tNVBgA2_1GKD3RXRc9pEzi9hCgK6GqLsWjhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=c22UqL7lIUpIGlcJQIPiAmyqAMHcIkdgZZXBT0Gq3ykWZRW6jXtOrVZw-ipz_XLyIBVFBqpfs2rVKYOmg2QlFS-NKpSOiRAxrMrgRxJE4y9wDZV41GXONJ1yKWBxJBull7jdYzVKjRzCq_PmutfDT9Uq1gwefNOcBL5gNzSPCocRbOORYdpHuxavxeAQw7wj1Qcc4Cg6UFWSRpCE4K2AoLbLYZ84t89lp4v84nn8MymqcqHykcYRIyYDdQsFaGitn3U_-PLQk1FbN3yh5jNF75Go-ZpmrxDwctm1yikHcLbNn01U_tNVBgA2_1GKD3RXRc9pEzi9hCgK6GqLsWjhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=KndM4hRYYJJIYN9DoICqzr8CcLKVZvID2BKqjcv6bxgOU__rDEoTm0punFgmxznBZ5LidpMR5azWPSeqCUJDDerSuBKeXajHXMhREW8Sny-IY2FEUDyilFpwHt0-wL6A-c67MA8xJbxJH42aI3HPJNWtG07Y4Jb98eLOP1L6omdImpxKfRrfy7lYkX6sk9IqEB9vmb09svoaKBcyjsXHnpS67ShuWb94av1onCPXDYECgsywyiWBLLxDyCDYql84ilafQFBkEZT4YTx4OH5LMJPTz7Z7ruSG3qYv9FwP95-sSJBQ68Ca4XcvGe8eZJlNhvqQPmhpKVx_FfkPbo5uTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=KndM4hRYYJJIYN9DoICqzr8CcLKVZvID2BKqjcv6bxgOU__rDEoTm0punFgmxznBZ5LidpMR5azWPSeqCUJDDerSuBKeXajHXMhREW8Sny-IY2FEUDyilFpwHt0-wL6A-c67MA8xJbxJH42aI3HPJNWtG07Y4Jb98eLOP1L6omdImpxKfRrfy7lYkX6sk9IqEB9vmb09svoaKBcyjsXHnpS67ShuWb94av1onCPXDYECgsywyiWBLLxDyCDYql84ilafQFBkEZT4YTx4OH5LMJPTz7Z7ruSG3qYv9FwP95-sSJBQ68Ca4XcvGe8eZJlNhvqQPmhpKVx_FfkPbo5uTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6-rKj64RjdOIePkJTrgDW3rVU2qIUSKfPY8rYI40xaysdLFFkc84a1BIbiP6TCfMHEjiTb3EEptuatrYKjgOcN4wKQezx8l60XkLPiKglneLaU9PK-h6xDM9taa_aATydd4gPWIyPTfkk_WnyrPgyNqOMHqmuJwVCDRWSCNdoLJiqZKey84zohigc4Mt_sppAJPufE-KkZvnzqB4qub_tX5T3zwbzzdCqRm5HsrywXweY1aHulygkPj1jGGgNhouWxDtYwe_uAohdVWMChlkaKalMsWKTSJj1jJEoJpwdz2fjzY5lKavwen0RKAzbyEAw2HeVlcFO3O0egnK16yfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
داداش فوتبال می‌بینی ولی هنوز ازش چیزی درنمیاری؟
😏
⚽️
یه سر بیا ایرانی بتینگ
👀
👍
✅
تاسیس‌کانال‌سال2020  اینجا خبری از حرفای الکی نیست؛ بازی‌های جذاب رو بررسی می‌کنیم و فرم‌های روزانه می‌ذاریم
🎯
📊
💰
اگه‌دنبال‌یه‌کانال فعال و رفاقتی برای پیش‌بینی فوتبالی، یه سر بزن… شاید همون چیزی باشه که دنبالش بودی
😎
🔥
👇
بیا داخل، خودت ببین چه خبره!
p6
🆔
t.me/+3P2wZvzhZbsyY2Vk
🆔
t.me/+3P2wZvzhZbsyY2Vk</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30644" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbkiynt9WfJ1QknrV42m48_KC5wrRvmphDoHNBLItZ0Eql4sO8CSqH2-1-VNH9-IunFDm8e2chLgf5I9Jxz8FvQ2sToeqSpiHMZEQgi_bFKXkpbOvWGlb31Yjz6L4Ht3-DDOOw5x4xnU_stmpOJN1ZkzjNisyBlB_kIQJiThrdgQXIPdFWpQabshHrEAOjuBHUcqMXCP0Oqj237nl1Fed3x5_ekcfvLEZpe5dti1o1hfmLbTXDV0kg_3DgZRP0BHlFTGPuRURZfTcP7zT-462_Gl2N2AIEuAs5tOwrDlkKPWTdzqzhb69KAt1DCQ2D_Y942kSO9OJ5nAUAs_pC-80g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJT2hRoLuKYowRzZbgPlpZL9r_CAm4BqslqlXoH7cf_4M0fBSXi0EevQl0V8hDvDjhyIbwMygW0EijLM6w2LFgL3euI5gLsJMUyNdqcOn-jirXeFhTZEguOKKcxn758VtH9xnaIF1yXMTHLyKs7QRHBylMqYv4_tjaHb9IUoDaK7qjvVgeOooKGkRrggbMKo87w5lAMrc1s96fOLMBbEsQk38UYtuixK0p4asxkzDxcUqmC8DNBddb116K1zstZHiL3i_HlnfAspFV8yW8kIhDVgdJNeHrr8SybqvICeRJPO6yUQh8idxglPNd58bDf82swa8MsXLxeD-TxUyGOl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baUCDQGbLBMe53fPjMBrwwB34XObAGvuLHl4DA-gbp3Y1RRsmPocnviIwdll0eFFMwsejnqOUd5WYyR9VgUMKpD8VB-BhfDLlzqsqVJ2yFF0GM3BxK0XDvMWVWPQGyY3mkgLVHRdnjQqZY_1al16kgY6BpdUysDqbFQiCgnA--Jtih1K18H6MXal5_1B8T6YFSJCsbtY6LB326yPKcB-QPoSEW99NyEVryzeubn2rspuBG85PP4yvX7rJaq6kdKb62xQvQ9f7WpNWfx7aehdr6L2tiYzusbWN1HjisvbLjrjbLLIDaP6XehTbYrt1BxV2I1GwoidII84wsmJi4NQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=pkfl9ZfpImLY5Fl9Wwti5z-MDM52Tl3tdHuqzcK6btuUoJD6-oCMC9gzJg8CaWP9H_s4ZODkX5ONdXhVY4wjuGCFHA5g3d16PH9isGfg0gP2F0WY6TpjqGYILB44zz0uK6nJ9Jsn9SbPPTYhicmYaVSPM3XG2X_RbHYao5mDlCixRXX_tMTAkgbu1yUUdsFlS4AFgQ_vwWuw7CWEcHUBzEklZmLtmya2JBbW1timNDDxoFhCjLJuD-imagmxcCisUXXDUWPKTaH5OKVlIUIKn34jWnbSbquPwEJquBS7UcW8Ois7WSR-07u92O4SupugrH7qQ_0rqenRyO0GCe5ltg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=pkfl9ZfpImLY5Fl9Wwti5z-MDM52Tl3tdHuqzcK6btuUoJD6-oCMC9gzJg8CaWP9H_s4ZODkX5ONdXhVY4wjuGCFHA5g3d16PH9isGfg0gP2F0WY6TpjqGYILB44zz0uK6nJ9Jsn9SbPPTYhicmYaVSPM3XG2X_RbHYao5mDlCixRXX_tMTAkgbu1yUUdsFlS4AFgQ_vwWuw7CWEcHUBzEklZmLtmya2JBbW1timNDDxoFhCjLJuD-imagmxcCisUXXDUWPKTaH5OKVlIUIKn34jWnbSbquPwEJquBS7UcW8Ois7WSR-07u92O4SupugrH7qQ_0rqenRyO0GCe5ltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwR4jPuXzudRxU-O-mtjYqvR_ISuLm2d_3DNNWz1m18qgg3jqNZuZYNSqqoXmQpoORTHxQmhjIne7qR-C6Bh9ihhMfF31KRzaIpQPHeJITRIVDhM4kK8vwHHKKWlZn4taZjT0m7ncOaDhtRlCQE-qJu-Zej_Bhl6QR7YXSEfbTfSLrEcg6vbxLrTPM_E7htyNBbFFk-ngZFWt3M5OK6YiO-sfmmtJMW7Yi8zXex8kMSgReAVIRf--eZxY5UaA-tg1XfoDcPhmvFdZ-lEfMCgaz-DFWRfUSgEoLHaajnhpv2OoCHci383-JxOjymkZMfeCG-rNuULLP0xN0GHXX-Uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30638" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30637" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیاناتوسط یاسر آسانی: باشگاه‌پرسپولیس بامدیربرنامه‌های صحبت کرده بود که به اونجا برم اما گفتم علی رغم احترامی که برای این باشگاه قائلم اما جز استقلال نمیخواهم در هیچ باشگاهی بازی کنم و در استقلال موندنی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30636" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=F1hcbyyMm8zkBNQIliMQu8Gs734wWBpej-j2idIDOuAmMhVHfaCcowVN0-mFROyel_0aQE2DM5ml69butdtP3M1eKFYkTKRSRnGtjhL5ZgCkQ2JSkUsTZgMe_BZjR-011ASOyTMiWBlV2vDiti34Plj9KT73WlToaXqqV6GTvIVVrKjAPNZOpMaMvxDZ2AZXSCVRe5aoRF1T3ghFhHXw7y8ck4iIKAM0sijG7SnwV2z3mylPpOrSzjsElDjn920BEMDkEYEEJZ5vs9m729zHOYV6OdKX3L_WEIt0Tjum3cGHWyiFhoi5RI6dzWMZbu9Rg3rOz8plvEgi9YfsQWZ6gz9ejct8eheYFiURqe4vhyc6zuFt4BkFcqdU_VpiyX6EnYAQTf-zuvNI7kFrz6nf8GKMngRub5-H894o_1HByjzZEQN0VZDqXGN1Y_KFf3r8s5WI9Jb3S5tIBM6ODqiPPlZ90cXy3J6MTBdpS9J23qICvn6g9-kcIqA-HXUxfTLtm9rxMDArtKVYte9c8cyBrYbIEsEY5SsA_S8vUbV32QRX_pm2tHF3p2PIZZX5PXESoelSrgF9zAQBR9bg_jZi90GDRvrtyRb8_KpoAzgfhfauXQy7NwSYOfdxPFmpeDgDuMKk0rxCER0Ue9CKoDuwN7TLDfN3CTA65CN6Lr6CyGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=F1hcbyyMm8zkBNQIliMQu8Gs734wWBpej-j2idIDOuAmMhVHfaCcowVN0-mFROyel_0aQE2DM5ml69butdtP3M1eKFYkTKRSRnGtjhL5ZgCkQ2JSkUsTZgMe_BZjR-011ASOyTMiWBlV2vDiti34Plj9KT73WlToaXqqV6GTvIVVrKjAPNZOpMaMvxDZ2AZXSCVRe5aoRF1T3ghFhHXw7y8ck4iIKAM0sijG7SnwV2z3mylPpOrSzjsElDjn920BEMDkEYEEJZ5vs9m729zHOYV6OdKX3L_WEIt0Tjum3cGHWyiFhoi5RI6dzWMZbu9Rg3rOz8plvEgi9YfsQWZ6gz9ejct8eheYFiURqe4vhyc6zuFt4BkFcqdU_VpiyX6EnYAQTf-zuvNI7kFrz6nf8GKMngRub5-H894o_1HByjzZEQN0VZDqXGN1Y_KFf3r8s5WI9Jb3S5tIBM6ODqiPPlZ90cXy3J6MTBdpS9J23qICvn6g9-kcIqA-HXUxfTLtm9rxMDArtKVYte9c8cyBrYbIEsEY5SsA_S8vUbV32QRX_pm2tHF3p2PIZZX5PXESoelSrgF9zAQBR9bg_jZi90GDRvrtyRb8_KpoAzgfhfauXQy7NwSYOfdxPFmpeDgDuMKk0rxCER0Ue9CKoDuwN7TLDfN3CTA65CN6Lr6CyGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30635" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y015zZSTZoEsDeWB_vH0luYsiKddlezGsOzh7IIHar8GAAr7hFcOZTy2aSRXLyLx3Emz6LZdlCtJMCOMFEt9AvP9hGZno0md2eLoAr6FL0mSOmzrlzYnZ9mQ_PHbdkZ4P9fD5cStXTNhFG8tfaWnMFQhJWzGQQuJknR7i4P_DU-NSR4vOPqHy3kW-ywi8XjvuyVhnNuQC_BEm7_i-arU-lgS8mL7U2enk2Z5QXy1-UlgJy0mChH6nnTlKoTXcUljYwZwMF8bmN2WksXSXGDSex-sP8i96HGmm3SDtUTO59G_9XIMJh5l2RdCIodp_HE4LeYKUsaEVSWWo-1pQ6DmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30634" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGCw5OPZWFi9_kDVJ5zxQ8jieo1wFTrkozBx8xi6Ts-VY5iKnEZ5uIe1HHUkqDZKOaKqQY8MRZyGPYgXj_Z5qKWxQUjMYsdpIrcutCCDycdLU-xz8KKXxxMFsgYfbnynEzTPPVLagLuIOXmhOLimDD_jgX8_MKhpgMyunwzKYmWZOHB_qW8REJNiZhUnw7sz1SIlypDhJfVMjHd3iFrXxhsps-_A6Wp4mIu4dmyr5Bgw9idALcnzK4JtSO5-1JxHFC4dCaBsbm3Cnr06aBtebXvtFUTmxOKJosnkkRVsZhgBAlOLWv9qLfbI8Uq8KM7lqJb1YcXE_t9qmUA39uWR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30633" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=o_s6YlWTdboiDykpWX9VvLzIrE6L7vHX5L-3DJneM9kAIg_MuscULV0P9Oa5DCdZz-miWKmc5RBtR1yAR31rcO-JY-sJL0W_X3Us_jqeQBMnMZjeM2avMToP_TXa48Z-85iWTHhLIAmJ7CL9qvM-JdITQc0RGeuVnk-0ewiLB8k_nxhD6jSJ_gBOAKnHUWpBuDSj5FDfWyEbIp_VkcATDH8-FFSR_QHIOSmdWcM4q31fnhwSwkKB_vSfQA9SPp2GxcztOWJ5co7cpdtSnY3Sbvtlo2hSufiOigGSd80aac0jmMDs0kbfTnolcUuL7UAw917k4Fle_D_CstVhQjI2MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=o_s6YlWTdboiDykpWX9VvLzIrE6L7vHX5L-3DJneM9kAIg_MuscULV0P9Oa5DCdZz-miWKmc5RBtR1yAR31rcO-JY-sJL0W_X3Us_jqeQBMnMZjeM2avMToP_TXa48Z-85iWTHhLIAmJ7CL9qvM-JdITQc0RGeuVnk-0ewiLB8k_nxhD6jSJ_gBOAKnHUWpBuDSj5FDfWyEbIp_VkcATDH8-FFSR_QHIOSmdWcM4q31fnhwSwkKB_vSfQA9SPp2GxcztOWJ5co7cpdtSnY3Sbvtlo2hSufiOigGSd80aac0jmMDs0kbfTnolcUuL7UAw917k4Fle_D_CstVhQjI2MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید سردار آزمون: پاراگراف اولش رو بخونید. رفته متن رو از هوش مصنوعی گرفته دیگه فکر کنم یادش رفته قبل از انتشار ادیتش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30632" target="_blank">📅 22:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYVuDHLAAaz0PDCtNpPSorQC0Lv-sscWIVL2ICh2xWOKtGS6UGLoKWhGcfig6FRebbDrXy4_kY4Om481n-N4P2qrkNjQKm0hJIMt2c3sdxWVHukAKCok0N0DZWc-EqmjWzTJfCRVIXivkGJzKavHh4LpRChlIT-KsrhhK-lpdN6UmlWlTDXc4dvinotCQ3xN1JVhPa8olx0pZ4_BU7f1IbST_9pZd61RVgLbGtYmcbIUXSXZliyrdvGj0xUFzs8AdAU7f6YOxTKuoYBIBMfKm3QzOaCUEwQjJbCPzvp_jXwJuUA_lSBHqJt7o0LUpY7uxwlGUCInBSRn6YvwDBw4kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنی که یه زمانی در دورتموند آقایی میکرد و به یک‌باره‌سر از منچستریونایتد در آورد و کم کم افت کرد در سن 26 سالگی سر نخواستنش دعوا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30631" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMN-hN_YS8RitjGkOX-KTkXFGw21iLUeA8unDim_tvB3T2tEUbXMSFLM0YYossS5jpYoW0vdMhdxXwPOGuou_BvlYF93xpXmducubHM14uenoaFKsOUd11m1lDdQF1GbOG7mYwVKxcpHE9hys3Xbc5Bgm94-TH7M981RIHG2J1RTgiSNPbYu1C8khxkUjMIE2zEPkQD0EEpMUrj9Pxa_4JdJ2hf1xMoNSKWCMRtAAHGyCceAmtzVkaqA7-eIZ6BHnvCpihNxhpx8CTVdMae3vfXkB-VgySLq9mJCNE-bNCMubQlWj_ARWfzBbgTD9pl0YUDOdMoNzySt4MnzDmQoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رای‌دهی‌مراسم‌توپ‌طلاسال 2026 دقایقی قبل رسما به اتمام رسید و از این لحظه به بعد برنده توپ طلای 2026 مشخص شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30630" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbEy8ZA-QLQFRzSL7gZU38W0_GRfaX55_0JtCZuO6ioqiIeXovo9a6-fW3lAH6JNb2SAp4j69maN1R3S0bDTeU8Gw4iuoUEAUEYJk5ipSmGbMmrp0eZ6q8A-UjJC1JbiSIY1FzFYYUEYmlF5LGNVUBl796l09VncXgqPjZPNGIWEW2eBdmugeVqig9181AFpmFB7GRYPSkTVhkLoarI9Qqlmk4wWbr6jmypXC8GezszGMBT0UM2-Qd74LCNcjPD3-v6YbAlwFTJWT6Nketakhn837MpMAvKPRQiGwUb8W5BaNKNfin2F_aNz-b7GgKzxMHsxHIbJAG5HwMjm-bYu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMMjtqnkVa0CWNjsmBl05dSJItnywlVttdMAB5tJc6aQtBXWmjQFPfu0K36n_c8rxwkKLAwZrEce5K4dARBELwrpIuGf7dmQPouxDzYSDfPH3WR-oCQw80L3m6NsHhJ1wSiK_Xl9Xy-refpioRNJjVQvb6GG1o2ngxmUKfjNVmz9X_TFM36lwMwni1MWc-PPjO64pM-ahy47oUV1Lc-GYwW_IiXE2vKlYp1haNSCVREKy-wmT4c5qigyMGnydSd-lizlh7QCZ6oxIW9vRnGoxlD2xhCZ9kRY2vq5WEQkzjVSf0XxioD3UQ8scHvgXrIdiOVgyHJFISpshat9O5IWdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptgMH6nGpHh0jMnSO5nElZGz5FGelhslOYBSckuxLHcEIb2gV0RdEJ1iw9GVbHF-mYfCcpRi5XygumrghZPNak5prvUwlM4BGfL0-_o1l01IhhIJNmownXlrJRdpxUBO90_7k51Eg3_I7pdN7ZC98QyIpJ3352y3boqswjKWczeGQdUG7MSdMsf2JzgSXe_xs3K_mvYBeV_Qzla1KcLsiBX7juqxLQBnpEF5O3FFZPB_t3vNhQgEwM0HcjuRi2oRA455g25YF4-Cs-Z3WgxPe70Ntat5P_VPgzTJAt2i4Y0c-ljfzGYQDhbIG_BgjehYtiOaoamZSRW5GkxDB5QIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIvfnXBBZGkGDRofHzC7ozk90qb4x1Oc5N2HyvrwcFqUSzsYQrY3lYgugUQIMn_Jz__PZMBgjJrRcSbnXkHFXsSH8EtPN6Rjae60SjSzuiLCJPM8F579vOza5A0pOjit8IbRfNQN3z57CUFXIiBemzxSaPSiZ-I6eGzSbpRSUcujWRAty1Vj2m0akszLK4xP6Bs7hFyBbuFY7yDz556_NPCcqATJ5TWlcjBrXwCwQ3_L5tJUz-05IJ_uZ3SDGz4ZUFH-_KN_AD-y0GBgltsrnL-bZMzwL00aS71k8kFjMcJfmM8KU255hkRShse2wyfRhmGAg8SXALwKsR0IH5s0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=M_RRUd8XPFJMdB1g_Ly83E4g7VEyvkWCGN8zsq_zr8Z6vIoCVQc3t8t40sG1bld0_AlAv6eOvKk6HKuwnfLRQb-O0HH4JsVa1l3jbGtCdH2HNwjMqEkS-d8vStvt1wT7cxE1PSyEbjqqeZstGnJY2hPT4052yOLh9u_DZMFti7RnJrouyHvuMTVFpi2wonZqXqYm_fY7gKNiakfU_ivkIrepA14GJZ5rZDGpqI99fA0g--QOvrHQ8ITAaOR8Z3U4Tgsqp1d1RXJv9Q0R4EjmYd0K_SmweOmFWEg_eKveUL2bULVtNlwKGo_cbsClIM_rX3lInaLB26iFkg8wA_82aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=M_RRUd8XPFJMdB1g_Ly83E4g7VEyvkWCGN8zsq_zr8Z6vIoCVQc3t8t40sG1bld0_AlAv6eOvKk6HKuwnfLRQb-O0HH4JsVa1l3jbGtCdH2HNwjMqEkS-d8vStvt1wT7cxE1PSyEbjqqeZstGnJY2hPT4052yOLh9u_DZMFti7RnJrouyHvuMTVFpi2wonZqXqYm_fY7gKNiakfU_ivkIrepA14GJZ5rZDGpqI99fA0g--QOvrHQ8ITAaOR8Z3U4Tgsqp1d1RXJv9Q0R4EjmYd0K_SmweOmFWEg_eKveUL2bULVtNlwKGo_cbsClIM_rX3lInaLB26iFkg8wA_82aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=HxOWYXGYtvMFgEIlG0kgYvGoJDzUqR99ufagwfpMpYi4yGvWkpVkdkoVtSk7qlT0wv0IoBBXd02IeObM9YZSa3B0daHLbIEW-X5KcJCMxa8gRZ-H9qhqwCe_vsq02IE98qOS39gy2t5jhOtPU0a4_I_jQW0AcPwejkHMH1ulaeXc2nqnW-ovkymKLpr56axQIpN_UowCyShM3l1Z2MylijJFcY-B7DlbABhNgXP64fNk89aePinsau_Sj9hkV5nOT2Sawr9Ef_wMANH8i4NiV0rkWE7A8cyWoWcxWUl7lYOGnnQELjhqUVmqMqQ0HArm5jp9OzxciNuJt0Qt2Jc1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=HxOWYXGYtvMFgEIlG0kgYvGoJDzUqR99ufagwfpMpYi4yGvWkpVkdkoVtSk7qlT0wv0IoBBXd02IeObM9YZSa3B0daHLbIEW-X5KcJCMxa8gRZ-H9qhqwCe_vsq02IE98qOS39gy2t5jhOtPU0a4_I_jQW0AcPwejkHMH1ulaeXc2nqnW-ovkymKLpr56axQIpN_UowCyShM3l1Z2MylijJFcY-B7DlbABhNgXP64fNk89aePinsau_Sj9hkV5nOT2Sawr9Ef_wMANH8i4NiV0rkWE7A8cyWoWcxWUl7lYOGnnQELjhqUVmqMqQ0HArm5jp9OzxciNuJt0Qt2Jc1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1UkROM-5wvr-rdF6AZUVy9miN0S3Rakwx7Z7SI7nJV1__gegu8ows3eO9aMD-fnkPGmtraE1-GpeS8lPXMBrAp9iBHwJg4aYd7jNNcz8C02wgFNNUNH8qjt67jYePHx0YmSOAeCl9ybC558jhitdRjrAVclRKJs6gl0TWTy9G2CKIlduttSWnd1gojZaA4oR9pDHzAkWXaGWBO4nsqCFTT7ynHpSdK3bGGqb_54hESSVJ20Jqb1e3nWuZi8T0twTH_gcyLn8NnTWvdhQgN5Dqi5EZyMVrQ49L4w3K4ltLNXVWEInnUarcYZerSwCTbzDrY6LWjuglZnst7KwrnlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=OY_fHla65N26cBBTZOwDrAC1hUEp-r6CncOu9z7q3O6KzeqYhm8KeR5y0tl9w0E-ZKgFNY_veJE1lTukEqU91hEDThWMagsTVij0cx1HnCvxYUU-PbByvUw7xVJJeBhW-1SuR3u8MjvH1pK4qzKlYl8J_Z4c3Wi77oshMMMxekuI_rI-lpkOrsuXo7ufqrOnLGSpVJUlMs0unMuzujjXkS3NX7SRLM3ASme33-FUEhVtZO5X3cKI4-pbld3xW0cWQi90_9YvL2KYhDBOazV6P44NfuOS-ZtMYlmen-6bhW_OGWi8TF_rlvnLJjs1NPiVwRgvGOXrbvHHbLqFwlqdBJeWF6O6C7C8-xWWIs_O3qCGnY3c5ibcG_bu2Z7vWFtX9d_j_1qEBQu09F_sD3ZyJ_GoNQANT3wOEtOQHAXkGBvmxRw4rQ-bszQPnL1MR62ux7yPFU8QSdtlVS1qp5Kpzs-pAgYvE9pnZXJwnp6cSHukXRmB-wBfucgs-iDwP9oMonVMqX8wX7fxgrVvmQa_--puUSnOyXVN-1pDnwnhoHZpnHbFlb5PQL4067cTGW-Kkqfd9CPoInGF8pVtC8fD8lxOlmsDcSustZfAgUdP_5b2Q4ObwpAxmkZWuZSTKIgyacmC6Nm1PSRc7Uln_lFfB8SpOo20jWBgO_x83T7GiwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=OY_fHla65N26cBBTZOwDrAC1hUEp-r6CncOu9z7q3O6KzeqYhm8KeR5y0tl9w0E-ZKgFNY_veJE1lTukEqU91hEDThWMagsTVij0cx1HnCvxYUU-PbByvUw7xVJJeBhW-1SuR3u8MjvH1pK4qzKlYl8J_Z4c3Wi77oshMMMxekuI_rI-lpkOrsuXo7ufqrOnLGSpVJUlMs0unMuzujjXkS3NX7SRLM3ASme33-FUEhVtZO5X3cKI4-pbld3xW0cWQi90_9YvL2KYhDBOazV6P44NfuOS-ZtMYlmen-6bhW_OGWi8TF_rlvnLJjs1NPiVwRgvGOXrbvHHbLqFwlqdBJeWF6O6C7C8-xWWIs_O3qCGnY3c5ibcG_bu2Z7vWFtX9d_j_1qEBQu09F_sD3ZyJ_GoNQANT3wOEtOQHAXkGBvmxRw4rQ-bszQPnL1MR62ux7yPFU8QSdtlVS1qp5Kpzs-pAgYvE9pnZXJwnp6cSHukXRmB-wBfucgs-iDwP9oMonVMqX8wX7fxgrVvmQa_--puUSnOyXVN-1pDnwnhoHZpnHbFlb5PQL4067cTGW-Kkqfd9CPoInGF8pVtC8fD8lxOlmsDcSustZfAgUdP_5b2Q4ObwpAxmkZWuZSTKIgyacmC6Nm1PSRc7Uln_lFfB8SpOo20jWBgO_x83T7GiwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30621">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huJ7iGVFTMSG3P8om--9TOsKPcpZbFnCcAEvPwgaxJ_gg-vywjsRL7oAAvtX6PFnNBByG1NLCY7btRuwdoYBCL54P80bJe1xMILa-OmJE4J6h98dPVydfcd0AnpxKuqZxhdlzxWsnDpIJjb4HefT7HXgmg4KoHbaIuDcukkwSKNVvdY3id_IGiHvfSp8d_JW_OxzqhMqG3UwXWYkP6511eD_BReih5UtiHUWZAvJQfX67oGE_sxg74O4YiTh0YZffyCZqGcoPw5hb4JZheheEwnAb6wpqE45LGZyaLj0zLy7K5XCxF0Rwx61q1-PVDXDP4tu8b0NAjBBRHmOV_HXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
خیلیا نتونستن از فوتبال تا الان سود کنن، ولی ما امروز با فرم هامون
400% سود کردیم
که نتیجه تحلیل درست و تجربه یک تیم حرفه‌ایه
👌🏻
هرشب بالای ۸۰درصد امار بردمونه
✔️
میگی نه؟ یه شب
بیا آمار چک کن
😄
فرم های مطمئن امشب فوتبال با ضرایب بالا از دست نده!
👇
👇
👇
https://t.me/+laf8I3RIuq42MDk8
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30621" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngWhy2qsktCBdTxHjhm2gBYoZ8MBKoSxBEItYAFIaFUoSedTU9vUfV13F20pfyHX1F6qirdorufGLbYfh7TZbXXARSCV6v3qDDAnjDZdf6GpyAEG6tOr_COfMWVQlCD6M8Cfetdan4I2pR6sRDdWq46LmQr7KMyQKbYfEjwp1WFsuRnlMyF0ssiQzQBDXPBJMt-jVaYW96Z3SPjxFx1EEB9PA0eyFhmISJnvAvDChk1zzqgepQTNrv1Mh36MqLXaeuIEN6daMp-YzzQ5VjHtbXM-Bsq4YK0Grsjq37dtTqMLWOgJWmljB59fWrv2D2aAYEPvRetkYFHwKp0HfoF-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQgVP220uW9wDz9JsqmBPCNi7Kv8ifIER0fwTyeOpOQwhpCuYPeJCXK6XZO2Xdyku3ylitlTjzkvUp1T16Sx_59x2va0FjOXNaifj5Lz2whAvqR6DPq4irEwA5bb3U7ZZ-YIXdB-rW_eI0-1CbCsbKZg0Uw0Rd3wHpKXiwiQ5eccHA9yu2QiFxIHeqz_HsPMfQwi7FrkBh1RBlnwdp1IzfIlOGXUHUxomMvYxYL0S4Lvl4prd1Sc1MIZy-F3JtIwoZHSmofx4DIpyaxUspfrZlkWrNFoUsp26Fuskj2t_OjHeL0P8KomT4YKmzYnxJdkkYdSRBr9iJc0GDcxxyKkoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=JGCQVjbbkuRDXWFfSzAnyEpYSKsbE4SQ9ckcbdErNKY6cawglKW_IZAAAuNSTT19yH4YW1-tVu_DkQzRptsobCfrQxnKqUkk8Gxa51LS-Tb9xA9KQ7RJRLCyVso0gx-YDyJczR7Z4MAYBD-PqG1UZrABaVZHpVFa2uWA-BqI5r0HPNUilgWxNu0U-7eSNbJy7W90Fix5HKgiVDjjHESk7NB7vKVFSryz5FW--WHNmuyK72J1brNVfZq2b_XKZK1o68uN9PWYCSfDFBw7BPCgisCniHbxQLQ-Q8ZVSr0RW23N2klgrAAoJWq6TrERio5ZDAA6_EB927aE220P5CtLPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=JGCQVjbbkuRDXWFfSzAnyEpYSKsbE4SQ9ckcbdErNKY6cawglKW_IZAAAuNSTT19yH4YW1-tVu_DkQzRptsobCfrQxnKqUkk8Gxa51LS-Tb9xA9KQ7RJRLCyVso0gx-YDyJczR7Z4MAYBD-PqG1UZrABaVZHpVFa2uWA-BqI5r0HPNUilgWxNu0U-7eSNbJy7W90Fix5HKgiVDjjHESk7NB7vKVFSryz5FW--WHNmuyK72J1brNVfZq2b_XKZK1o68uN9PWYCSfDFBw7BPCgisCniHbxQLQ-Q8ZVSr0RW23N2klgrAAoJWq6TrERio5ZDAA6_EB927aE220P5CtLPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLMgCVPJnWSmNHyoaFZ7Do4MLkpNMxRHpTgkEpr5sOQgb0UEiAD1LWxcvp2Im9NLQVY5DNMked8tI22DB8dPAmwbYhawy5WDsSwQRLn7b81wcHo5GYkDftCTDmipL9PED5n3eT0E0pdFXsUm7kmzYFljic5HBHETXVtKegzW_kgncflo7N47gXnJzhWIHD68hCH4EvLn5wEvDPNk6539owU-cVTUFA8r3mn2pJjNUEjLQyk2HT_5EqInXIxn1X8kb21VZvgsGaYrr2fyruDG9YqJSL9uA3BvOiKYP9A93U_TlQUM2z6NdC_JIEe976X1nEr6wMTvp98WEr0Tt-jF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0-VouW3KO7lYKqPrfxSyoFGzoZBVwxPTkVh-V1GxBKem149xNfP5l1ZQCR0J3-bjPPRu7h7FX6HjWMiGYqFP-2sphM-vX9DEP4vxdHHjNmfAmx7ZDbRQ-Qv7wxpsK0KYdJ0Dv9dJ38bzOESA-noDwsPNM2FwBV2vIzm-p_EKG2BKR0sq9QA6rodiHiQiN5qK4lnjWdaAlKzJ8nlkZosECf0aJ9MmReiPtuuNuVtdvqDwWPBpTD2FAZ1PuZbsjh85a75mVb0IozqwCwZVFruxuy0zbd2HJ6NX1T4ejXML_u50PgRTB24tHSx4jnqg6qOBJLw9WEXDa4kBIys9O4KIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=ZyJt6KO3cmRV-o0nIURJrQ8QspicvUwBRRn-yB9He24ZGaeJshZq0VEd1Oqn2cvbJRLht_Dog7GY7076c-CmY1Xf4iV_-n_FYPFShJ0OGVas2vRjtZXnnjqkzISyARVVSzsfkHasTM5Ukm6PEZRMbY6qUJ-gaK-8j8pEahC3Z4Fd6bMIo7ipEkze9YH09UCi4Bkhzkbt8tmz8QzCPjsQ5ESEV6eW65vz77KfTt2KLFFg9rm5aY8v_HzSvrsKG5hZwXhN-46Slv9a7UwXNnKec5XJYwy7Iub43l9K8bc1yJAOk6S34_vUnCZt8Fgu0JuzETJkRSjuSAgOLEVhDh6c6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=ZyJt6KO3cmRV-o0nIURJrQ8QspicvUwBRRn-yB9He24ZGaeJshZq0VEd1Oqn2cvbJRLht_Dog7GY7076c-CmY1Xf4iV_-n_FYPFShJ0OGVas2vRjtZXnnjqkzISyARVVSzsfkHasTM5Ukm6PEZRMbY6qUJ-gaK-8j8pEahC3Z4Fd6bMIo7ipEkze9YH09UCi4Bkhzkbt8tmz8QzCPjsQ5ESEV6eW65vz77KfTt2KLFFg9rm5aY8v_HzSvrsKG5hZwXhN-46Slv9a7UwXNnKec5XJYwy7Iub43l9K8bc1yJAOk6S34_vUnCZt8Fgu0JuzETJkRSjuSAgOLEVhDh6c6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=P77vXs_AD3DAF96uYCf2upC8dA6aci9T_gJVXE-0E0suFuhXTpBK7jlqlvF6HHUuS2Wm-2WhZLKwLwB5FdcKxzn9cgxAoao3btD9l7Z6TQP-PVBMxrFSGc4Q5OHi0UTcWl7Yi4EuRHn8e3pMOiiBNfsimb3JeLFTffz3mvWcd1o-BBZCJO7QQIm3CwDZPZMNcvh9P_fQL8v-npH8WmOiOlQdDxqBMIq2pq89Fmn4cusOu4jkQlH6n8d3aVCqyCwzcMjhR44SOChH88VlIFXtOYEWqJduahXm06j9j2eaBPrfPkrhQYN5K_Qgf-tvUDw7sOjPZQ-ept1UWbVmwzRnlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=P77vXs_AD3DAF96uYCf2upC8dA6aci9T_gJVXE-0E0suFuhXTpBK7jlqlvF6HHUuS2Wm-2WhZLKwLwB5FdcKxzn9cgxAoao3btD9l7Z6TQP-PVBMxrFSGc4Q5OHi0UTcWl7Yi4EuRHn8e3pMOiiBNfsimb3JeLFTffz3mvWcd1o-BBZCJO7QQIm3CwDZPZMNcvh9P_fQL8v-npH8WmOiOlQdDxqBMIq2pq89Fmn4cusOu4jkQlH6n8d3aVCqyCwzcMjhR44SOChH88VlIFXtOYEWqJduahXm06j9j2eaBPrfPkrhQYN5K_Qgf-tvUDw7sOjPZQ-ept1UWbVmwzRnlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30614" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anA6hodoKi8ySz7A17ecqJJ0lCo8wJbd71Pk-ji_OTSe0L_kWDoW-7lB45_xQKPsUwUJgckJg_qzmfz4b_hr7Qlk5UhoZw7FZf_guRFvcoT38Z2429hENbz0HFqUMDfEoPB05gvPkjuDnV9M9WrH6jXv4dM7HTJdTNlO9ygW9vQkAbk6bQAM-hiBh8KbW9z_XmxakUbcbS63-9BaNP3P4qctZWrKS4qTmt1cdbSFYpDZfCueRkPQev9LI1ZnKmOygBew0ul2vuixkBpeuo-9sNXHDeqzl0ppN0WAs9QZLE283n9PaCO7N0oExUMvZZvVmlliFzftMd-QJBe8chipPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30613" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2ReHORq2gb9_X79Cnsb2CqyAWvbzmTc1PADqTrG_TQMXV074kbQRzplmMNnHnoAbUAvlrbTCxJRhtv4Lm4ZU5TKEag3nOIU6hwRbVh4wt8rhrH1qMESVvL_bIsE2qlWWYG-iOSI9SoKuqjO_sTv0rBeG3d0jf5-lTSxl6nLd-wGVREZS-ESSJ7QmKoUtqeHS3CROiWCTMPO96reAhy362wOPrGb15Vqwi_V-Z3QhkuPsDZjE2m47-hxg_xacR47-njVIWooC1HwYDn-i-In1I6P8vK4l1NDXAAeUMWT-XNvIp0y47hhan1ScaNh-LopuJ1kOHTnQPvfynI6dAh9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پزشکان‌تیم‌امید؛عباس‌کهریزی‌و اسماعیل قلی زاده دو ستاره تیم ملی که در بازی امروز مقابل چین مصدوم شدند مشکلی برای دیدار هفته پایانی مرحله گروهی مقابل کره شمالی نخواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30612" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn9G7u4k6lwY_eEsqB9r9itRmFlTaxYDWSSNZn2h2PB-g-NQUoe-Ixwt9apugHnbbcg_Gf4TKa9GjpZPI1Q5xz8eari6HcbSDK8o53bqDQZPsDMA9-gXxogaIjx8Qucy4Hn6eQiAecfqby2HEGe7KXUpYf2NlIsy_DsGAsqjhwMaS0MspYR4uSwkHLzUW-whhLeA5_ruln4KW2fIcLewby3WPxtdPJ3Q-Vgyfn_qQ35n-Ydno56-8VRFn56HcLFrC30Hg8o8Ot5SkiHUoNqaFo5o5bq8Vnt1MAb5hmCEf6PKq45aZLQjvQ4GOc-JZIvVE-fyJtRabujVCYVsHaZqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30611" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clGoCw4DNjw8YaxDWsEuGxnZ6KjaHS5ey0UlG6dyx_lvUW7rdLWxemqTK2oFzo3P0L-8iqE2dLmECGBWjh6-IYAkhg2-QJa-2Si5jxppdBrxCcRAyZHAd7lvu7iqkrVEBWoRCjnxIWX41LzK1z8lGvU6nI25zoGbODbtQNgo2S0loOYO-86BMGuUyF-yloHQAsFPqBEgB1rjpHy-OzuXIRZ9TRrClw9Z3ucdY2ubplKxgioq7HLTXLKx8WSaWJwMCz9PWq-dkkgSLEJMuyf36U8ZzctWQZ4x5HUFZTp78xRfcQ-1nFwqOkUR2Zud7yfghUdg4en5GM7OSImJI5eZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30610" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qfod50IXwka8ViveMIADyrGRdFUTEHDPImW13Dq_MR8rkiOH3KEGS4uZGgOEA389m7QgcrLH9m6bxLGXdHZjfW7_rQvHg3SUo7htMBMFYvuqMMUuuKS4MDNS5psUwaQaVUs593QQCHWWSCXm9N5b6nlrPfry7Sc8dAPaIcmjqCqYWWn8dMGOtYFKY3F1_E2QRHDapY8E3FicX7V93U_5isG-adw0qCeZx7v307NA3HsKQcg4jVw57Mr7BBnm4GacT84Bf7FqsVbGkIk1Z8-ciZuydPtN1ZTeQIqogDj5JLOLmKZM3GdsvdQGdt7kSBz0mwo-aS3nWFALefERHYm19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش ناگهانی قیمت دلار و طلا نسبت به روز های اخیر؛ دلار به 245 هزار تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30609" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=qdYe-Crc861N20q1FlrMixpFnhv8A8iRv5IfkLS63A__U2dv8RSsKq8Is7QG954D5USxo58zcMMmlc5qsP6cRulUe4nyqFPIcnVGcq1hvG9twT-o0MZnZx0pq0bwjdrD9o-uxb7U6c1oYM_IkXWMdXVI_rNGwStxKvEDr3UI8kbHH5jPPKQnWny7mED8oM655jV0kR_8MNF_zN8IpJan_tAZPuICBSIYqm4F0y-pXDaMW9IBiVrOwFP4xfi_GBYrn9vbRsqeW0iJXuJv-n4vYgxoV0iPMhBSd51L_U2KZFnJAbURSqCd22D0W3lSKWB6qizRX7FPcA-y_rpDsn2tvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=qdYe-Crc861N20q1FlrMixpFnhv8A8iRv5IfkLS63A__U2dv8RSsKq8Is7QG954D5USxo58zcMMmlc5qsP6cRulUe4nyqFPIcnVGcq1hvG9twT-o0MZnZx0pq0bwjdrD9o-uxb7U6c1oYM_IkXWMdXVI_rNGwStxKvEDr3UI8kbHH5jPPKQnWny7mED8oM655jV0kR_8MNF_zN8IpJan_tAZPuICBSIYqm4F0y-pXDaMW9IBiVrOwFP4xfi_GBYrn9vbRsqeW0iJXuJv-n4vYgxoV0iPMhBSd51L_U2KZFnJAbURSqCd22D0W3lSKWB6qizRX7FPcA-y_rpDsn2tvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30608" target="_blank">📅 14:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_S9URy17m3aaj_Thf5SxHnaBiK16VpOJ2vWJ-x4-IZC3AsjGXiPhL7mny6EMRHQlvuTflzReXOgXZpaPCmVKiq0bF8D14M1WUGQJn5lQJfhmL7j0dpgcNYnN-sU25LbMp4hkNEss9gYyiQp2M5KBKkXqWEf0tjq2BSVl-qBdxP0UQ12BdkFvWY4_yp_Z6jGYp4h_CIuCB51mYoxYX9_AwQtqKv4aMkvErnz9gHI9D1BDfO1mx9I2Ew8M0xWA7ZQAPVQMJBQsE2aSbBDMALq12VU7KSb-o6ZXK8M3hYIDFDm6As5EXftCNkdtXJO784ZYsh4h4vNw-tGsaopjaD4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30607" target="_blank">📅 13:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdnFWXPz67wKK2rSYJ5XyC0YiEojnVjYTp2mtdqjM_h0HMvZQG29T9zW4ryeBE2_xWOw5tECv9YedwH20D-_pLmNZTQDEPa7CE0A1qxR6AgJSiF47XDHK5AHedZPNG4HFD7Av-hAqkTaOxwtYA2yQG4_rdJ26v18tfk18zmr6iLTlMCBuCGm0rY-ywbsez0xNvpkIY5oYNfxjIkCEmhFhLf6pxNpC3zsBjZ4jjeZPQdjrMhT0EBbSDwX4WGNqRPAR2h-6KHiedIFmC5I1ohXKYyRCYJyNIx3Pc9B0fqqneX2H8cTu3vtjJQ0rpYJjvp9qtbWZRpYPeukuu2obvNCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌مدالی‌لحظه‌ای‌بازی‌های آسیایی ناگویا؛ ایران با8 طلا، 15 نقره و 9 برنز در رده هفتم ایستاده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30606" target="_blank">📅 13:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJdjsn-sNgpukawTxMsRRZv2fDNV3z-pqz9GShn_CpxQiZje7APN3lnzwKy7_LWggxnVoAbzFqil-3_tuCiysnwBFVZBeWDN2gXRUDcBLE6ZG4Pch0LRvdMvliMsRkJrNxoWJgh3OW-sOL8Njz31qleY41mVyQLwkRdob-gKe_fl3mcm8_t_NCubh5PsBpN-wO0wJOuriK8-21bE2fpH3cBZaVUHEcwo5eOj9xWYg41-azWLz3y-GKDNAhMCL1EbZNFE6TTdHSpA10IwTvKY6yzMH9DfP0f37Kvsm2vKByZFxm_NqZ52amTCJre5trEzgZJqDN9yQ7GfxbGxYQxXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30605" target="_blank">📅 13:13 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
