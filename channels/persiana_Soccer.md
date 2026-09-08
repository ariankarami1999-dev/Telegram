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
<img src="https://cdn4.telesco.pe/file/Jiw9pe1vta3Gog8mIMz1nQVW0XegOH7KG_VvJzsP-GEQmcdKN-PyCwF1eZlxVBLUQkNwPNkKv-XGIuBKCdRd4L3fGyz1lvZTBYMEhmknE00td56WVSuMAxIG9MRWUEOmGkosGtQ7voKUqQDD269zyo3x6rIdpaWfO2InDF1vWIjrarr4tAvLVt5fHSLkdsab0g5Ia37psYObv3tBlm4xCBAp2tWs8CaQa_xqyfK0H7gbBymgPiOj6c3RjCwy1U_ddrVGfLyxyF7KH28VEYyk2vtXRQXbRNJA6NVcCBQS9egSbL1jcvDrUm61CUzHbg_F_ib40binEsXso8SwYUYwuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 569K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BioZb-vyVR1ZUHejTYoY-SJ66f5UhLzgQS_77kaqhtWHKWQaPJ__vvUaTLaZrNiOFMNJcB35VMv4PsyjULjM2KRQYkNRxnY-7j33U2EqG-tWIU4i1t_-Dsr_uxW5yEsM5ITDN8lfA9r6CXJMzNZVGqIOUf_B_TdmkWkpfbQWjLdqv91ycSo457T5HSmlVtDk_7G2pkwpfXCTZgtgjTinJoUdUfTzKOrBo8RArHE2s-z60sRqKvAQv-UztGCHTzVbtfRnLkIb-UvwGBUpM3hDj0VMCSfZDliPtDAfViGNXVHGlIeCmUssF6D0NvXpxdDvxFam0X4wEc5f3oshuX9JHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbHerOwSqTt5xI9sePputFlz3BL_yOjnRc8-Rq16zGMRU9uk8B9sHirdIJdICN9gNUy1rE3nzjOnIp5T7KzLmcSnFjEF6Qdo0rireQ_KN0MltyD9RR3drlNJnTLE7L40yVqUgwUcUb3U7_J6OMwgr_mOYxIZR9ArupfwB2JdqsoFCBzYxj1_yu5ECUcewTN6CtYyJSEVL3Pq1Mb0qNOpvcWQjJG96iRJte13t5bFI9Li7udO--skYi5jBwChMOPT-WWVKXy9bx2RzTEuDPVEtao8U1eCFVlx1yjSH0w7p1QeqJVKM1Qqs8pcySZbxdOhmbO9E1LrrgODCsfUq2mocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASgS6HDXc8zKqrMt5TA9BwOw50lndc8oXPVZnfeB6oQRPGjSkiBp2wQgmvBDtfDjNpgXsjNYS8T2CaWVYx9GsyNLuWw1ckbpheYRLUKcWCmTO5jl5t6u-4Jh0Kx2VQ1TeSHpGK8BQR0xMXME8mK0raHnXHPYKCQPv3cGNcA4tfMuguDqkt3uSqXvpexN38w56U_cALN-daa4GJ607-ZgYb5JVcg9bA0t732MAgp3br7hj27Q5th4MPy-HWCiPbxGv7155tw0UEFQF0CveaYUUmYNxJk_Y4CGyRjTGL-73pyEyoLdNbsS2SZPCvA49z_i-NTIcELkSg7UnVrT5mGPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4y2_gPVqVvapKJUKCxAUiS9myHcip5gXauIyJ1Be5ST-9IuiYU8qIXTWSRy9UMAht9MaAKM8Mg4vkMXXLuKJ04SVo8XY7SHNdhuj6AT3nKe8YgOGZIa1L8jKcqaV76mJYuEcwHWdRjDH4O4vups7AG4AfPivCuHzDaoM521dYbXn5q6mFfZf7MJLcGaFwg-U7anzSwqymv6LmLGt4l5s_Y_ZCRsv81dP8mN4Jrbwh0qo72glrLM4t9_DW3E-N_q3lk4murEUWrlhwogtFrvwWFFAqwuxkki3Drtuq_oamjWxuaeL0w5krBgqEmFle6x7QwE3TU4jMwE-ladRS7ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TppZR57SsC1ECAQhrZ0oIMYGMZG2zuF7xkos6ATt1XsFUuAnl4xRM-dVnHTU7jCfWS9Gjivttt7os9y0Ua-nXIk08yNWh3I8OsChDBEbw7D-smOhgTRWCU3y7X4r-mYTeJBinDtbS8ytQ1cwr4Fp6xJFz6uc5VpZ1KPI61tRUCb070ezfmYq1Vv2vKGSAmKshLC1a5VUu1IFwE9Zn0JPP6HUad8a4dnG0B7ahy_-U_G5jXuxDDHIjJvaRW2nZZM2XUi1FiHOf9OWyHTpGFLkJLTRSMNL0aGNM6lHm9kDAo0R49ofGP4abg59IxywSQ1zzxOUbxhdSM-tagLumb4hsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hGb4XwN5bSSsQFQ9NrOmioccd-pMBs4Ciy_XL3u1i0gd4tVApI03Yb0587bbJCjG4Zjw2gqh36Q9i7BbeNUz5ETdly6lTGA-_nIUF-rgLhG9T9N7-39SIeBnKXvZmC59rKfTV1bwfhhvxBnJni2MsSqxtMrWNy4dA_X7eU3lyZnxfoJdaRIrB-tmREEx7r3_xfHT_xpoMRCJeSbkg7QTyCawAh4mrZZmDYHau0ACmtrlE2QCy5fr3Kl9TWy7K8fRm_-B3GAgh4unpNSTiRlTtBtfzAW3aiIpy0IhFA-2Z8ZtKIWZRoGpbtq9_hHvS9HzndJY4e8SEzWtWpJ5wTdK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hGb4XwN5bSSsQFQ9NrOmioccd-pMBs4Ciy_XL3u1i0gd4tVApI03Yb0587bbJCjG4Zjw2gqh36Q9i7BbeNUz5ETdly6lTGA-_nIUF-rgLhG9T9N7-39SIeBnKXvZmC59rKfTV1bwfhhvxBnJni2MsSqxtMrWNy4dA_X7eU3lyZnxfoJdaRIrB-tmREEx7r3_xfHT_xpoMRCJeSbkg7QTyCawAh4mrZZmDYHau0ACmtrlE2QCy5fr3Kl9TWy7K8fRm_-B3GAgh4unpNSTiRlTtBtfzAW3aiIpy0IhFA-2Z8ZtKIWZRoGpbtq9_hHvS9HzndJY4e8SEzWtWpJ5wTdK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIItUveZwRjND2tIfH_a3Jm5PTcGDP6oQ_lMbN-5kqc-rgT9edogYZngloIVgp2YnGB784Ly8ZiaDGlNrvRq0eWBvPPkipufa_L4mck3myjaAabx6Y0BIJM4Tfxd7fUAQwVIJWbyn5-pCsg6068xhNrhsr9SM1gKdWrjXx3LkHxFjCMbZuujzeQYQ2bNMM9cOfNTt4JEvt1ZavCYHP7cNjECwX22KySIiUDAxp5BrsyjiaWHNohGsosk2lQfKyDSNq9hgfExmNTPeAB99zY1QgYmDswRpwEr6UZFjlNRa08QkAq5pvsb94Kcs-_4pz0tL1-lno4nBxcXGPw_kU25bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJKovoVNMys3kNlEjD_-4x6edSC0i6X7M5om3qwYRcd2BuaNFzRHvZcoIfMbLMhCMqwFdtRMAOjcPf41rMlAsMpfq1zZIwXmkMbFi8NbDv0Gt14ZTvqMnkBAPBEWwnAN8L6E-5J_4TJdw0RwfiRsP1vHJH-i-qUDxlWm17XjCNRGAliFbMOilBkC1xbHmHOUN8dwJFx9M-Qo8lBE3OMGabaj923_yxbNrugDcB5iqbm1X-lbFT9knU7SWUlZeeRJXZYUW6ihE5maG4YjheOXe_qi9MCm863JHVDjf7MwXVEWHG9mwSZ1bo2Bm5vFO49UoqRVWWhmcuOrCXe58CkJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
رئال مادرید
🆚
اینتر
🇮🇹
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/29320" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=ATB7vprJvoGUENvcgyovPAoDU_551V3GfxEHYrv-6Q4HcFA1avZyDynjPgBId4vWVb9X-qMjiKbYrJ7cZWMKxKpmCHxeVhx3SaysXdMsKkvNjozGOSaCvmCRTP7u1wdrGoyUVTUGQM8Ve1q-8ITbNAY8uRPyt6TiEEOgIlzKuEce1PDohayZlAzQrrjNxLwzNfAqIWdmWOLrGF0RgtZxJpIeF3ye9_cSByEGE5rAqUbkGDay54x5p_YH17C5dY4MKu1GY8z5r8dk1cCfYBFzzV45iG9b3Bc8VGKLtQpKNBgXHHB21ABgbCqLhYbKL0LWZN9LmM91wNOZtxxFirA6-A1Z-I1hq4PV8ia3W6kITkP9YkCwsD99eEqhphWDr_037srPdaqKxIbrA5V2iZLLZLSC__2ROWxs-J1LUlZwkzszXjdgq5TZudZDc7gttZqWWVRoJ_MlNFTTvybHhMFMvgWHW6TlARRmugoOTzcizzXUz6lelCtWJK17t3Ew6Q-oI_GxjdTHC7D7XqPNj05uT_8ey8mb8hOHNzy2mtAI-K7KtflraUZar_yN1xQvL9k_-MrSxK1ePGUjrKA27eAfSCE8JCYMx-ZbF2sAjlvPiwggEN_BkpY7Wo8UUBn3TA_rw4SWy_rk4InSXj9OClVKkXCQpoxrUZz3jSdoUsFmxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=ATB7vprJvoGUENvcgyovPAoDU_551V3GfxEHYrv-6Q4HcFA1avZyDynjPgBId4vWVb9X-qMjiKbYrJ7cZWMKxKpmCHxeVhx3SaysXdMsKkvNjozGOSaCvmCRTP7u1wdrGoyUVTUGQM8Ve1q-8ITbNAY8uRPyt6TiEEOgIlzKuEce1PDohayZlAzQrrjNxLwzNfAqIWdmWOLrGF0RgtZxJpIeF3ye9_cSByEGE5rAqUbkGDay54x5p_YH17C5dY4MKu1GY8z5r8dk1cCfYBFzzV45iG9b3Bc8VGKLtQpKNBgXHHB21ABgbCqLhYbKL0LWZN9LmM91wNOZtxxFirA6-A1Z-I1hq4PV8ia3W6kITkP9YkCwsD99eEqhphWDr_037srPdaqKxIbrA5V2iZLLZLSC__2ROWxs-J1LUlZwkzszXjdgq5TZudZDc7gttZqWWVRoJ_MlNFTTvybHhMFMvgWHW6TlARRmugoOTzcizzXUz6lelCtWJK17t3Ew6Q-oI_GxjdTHC7D7XqPNj05uT_8ey8mb8hOHNzy2mtAI-K7KtflraUZar_yN1xQvL9k_-MrSxK1ePGUjrKA27eAfSCE8JCYMx-ZbF2sAjlvPiwggEN_BkpY7Wo8UUBn3TA_rw4SWy_rk4InSXj9OClVKkXCQpoxrUZz3jSdoUsFmxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqBxV2AQ6vETsvSD9ChCSX1G7YIf7q5CuQN2HwT4bsGe6QwvykrCvOZxH1yY2TMPSdDXH4IZwwc1oRjVslZfx1OEGcHuyGyx6hpd36eFiHLdI38Mqbl_mm3hx1ZYBZlcZoV-U7iEQfwue0E1TmCt6DGSLSqAoi8DySG-PfH6CcWG-EpY6XnoxFvgGOmXItrcII7EeI0t8B-Q8l-lXfAFdZUIIiuMAzjds5ZKh0SfkxO3451HW6HfUt_NloFn-0h6lUqZVeIZypSk5J2vDnEq4J_8IibC_muyf8VAoo4Ay5TNSFw0shrY6QaWslzoCKInQ2gHj6JyCzx2c1DXsShp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFYgF1y13wXM0rqVk-KiA-fUfWpWDgvFaNVviAoMcweZ84R86QLuYA97xBRGfcsSfA0CT5wsWiwrHhqRmYrIAA94QvZTlvNLrJVV-GXgs_5EpIlTRnv38KGcKMMgm6y4P0qYjusiBSntHvSfEbaJKhuBd95TZQY6Joj1Kvf0u2-PnwGiVMXbMTa64gVMyaVwxTI4Ba_QGMCPlWA6b39jeSQLw1qwvN0cwxDCrGIpEpspX83NhoxBptipWjPKogYVeWeVPUd6gjemVyOSi7Y3Z1j9_JZZEt0zPgHagzlQwzKs_i5Ou6kCWcCFNfA4t3pjvabROhLOBVEXocOHg7ZwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=LeotnZRJThoN9b6Pi2xmJBcrEPlWevC-gAhqbmkuVpkGc0auYANS4H7mfukJ1QUMg1qjFuXV4K4Sk4B88zaVHfyduhm37mqk76QFrb4dPARVkZHTb3m6xvpQpYAGjh9d1NWqIj18ePIamSbth7dIrDi4HJwpfACdAR9AE4uL1OxuakVVr0cz70-CsiD39UBf0VYconuAx1VUKjNnJIO46lDLaFNJzqgTBV0nvO35xN72BWjUtabHIsBWunXfZl_7LzVOjnkPzPRupVsXLkZEktetfuooqpGClcp5MNv8GvYFNdZfMCqg1_U92aJf75LGBlBda3BLq6TogudSvI-Y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=LeotnZRJThoN9b6Pi2xmJBcrEPlWevC-gAhqbmkuVpkGc0auYANS4H7mfukJ1QUMg1qjFuXV4K4Sk4B88zaVHfyduhm37mqk76QFrb4dPARVkZHTb3m6xvpQpYAGjh9d1NWqIj18ePIamSbth7dIrDi4HJwpfACdAR9AE4uL1OxuakVVr0cz70-CsiD39UBf0VYconuAx1VUKjNnJIO46lDLaFNJzqgTBV0nvO35xN72BWjUtabHIsBWunXfZl_7LzVOjnkPzPRupVsXLkZEktetfuooqpGClcp5MNv8GvYFNdZfMCqg1_U92aJf75LGBlBda3BLq6TogudSvI-Y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=REfLaLa8B1i1eIxkva5zeyHjs_Hc9zL1BYz_bffap5iwi06agU6LTz36T07pOIqAWFUpYZngjkmDSfyW0gYDLhaLF31dCvtR0Ndda1vgYmH_O2VapTYb1pdRhK1yo00PqqMnRbeHpdPcyRJMgo3RGoLNyHGifWnfVtpRhI7flbFS6LsHDNYY9TUnY2DpPND8pZL6DgoeTWyaAixOcnbKvSBR_rZ4_rKihJn5Bwm743jtSAt3ZAvMVVEZoaKgMa7BSCW33y248ufU7HZ8QkRb8hFD8CWFFarIV8riHNaRj6XBj1_2e7Rdir-yAAFJEvg1L9v74my50l4Vy6ua7vHh2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=REfLaLa8B1i1eIxkva5zeyHjs_Hc9zL1BYz_bffap5iwi06agU6LTz36T07pOIqAWFUpYZngjkmDSfyW0gYDLhaLF31dCvtR0Ndda1vgYmH_O2VapTYb1pdRhK1yo00PqqMnRbeHpdPcyRJMgo3RGoLNyHGifWnfVtpRhI7flbFS6LsHDNYY9TUnY2DpPND8pZL6DgoeTWyaAixOcnbKvSBR_rZ4_rKihJn5Bwm743jtSAt3ZAvMVVEZoaKgMa7BSCW33y248ufU7HZ8QkRb8hFD8CWFFarIV8riHNaRj6XBj1_2e7Rdir-yAAFJEvg1L9v74my50l4Vy6ua7vHh2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGJA3tB0W7QzN1c8QlThCkwNaNmac1TGBxQEAQFkQdhZ4jK94kvjB60ZbFRz7ZtC7NO4MwAFa_jEeCs-qcNZEed5ULKnjtJBrIddHMB6l0INoH7WxXzwt-0aFAVVC_JkD5xS6-YDCIMaMiUd09wQ7JWqUZvLS1o_qNAJMJJbgEU0UjRSI7EJ_Je-bjiUKJyJaxmH_Wr9Xow_9iy2uN9akE31TwHUkPR4p8AT2SQSkvhvXu9xHCoN-2PfFq9_0b1FhB02nY4fl5CU_m6eORJ-DpFkK_Zf62y6qQcWWOUabv_KUNu5Nl6m0n9w8uSpx9sld7k3daIWuayTsAe4TJlLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMM6fq_YQttxFVlvM3fU_a8G1N-QCuaWxcthm6DyjAxvp1TKUTiBYdLVbKR6ubYi7zEbnPtrR0ILSRc5Q-8h39npe9-gl0UgeUqpiLqAfAjoaJdlgca-SFXgE89ArbLZkVY13dXhc-QC0I2j6DzJwWpE-AtCVR44x_7I9R0ebTJ77bK9TQq3z2BIZKTOYJADbLVPGeC57eZvrqGvWyBNRpiMMgHHphL-F83Q_quRaJS3N4fEuYv4mHe0X0OIOQwTCq9ys4D2KaO2BaCJ5fxXLBaKCYsOcK1diOxpzPZG_S0QWOJrlAgLVciawEmLwiy-9KXrgguBw_Uhqgf0Of09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R93EB6xcySV-cOGp_XBTzo_gYg_gP18KZoXP_2-McSBW_dssPSoYXBndFYV4lxWausHIleGfDJUPt0nQJF-ZPD8jUNqVnQl0xutf7Ss1XnFyrkiQZGDVyIjgHQhJf10GLIivkEN6DUuM1YHXBn8A9R6kmuDdIEZF0dNqHzLGOA3rovub_k1OCOMsQ1EfNSv2Y22WfyJVaJ9PrJ7fiHRToH6-9TDj7-Psf67MAqNpAnY6jhS5atDT6iZpaP19qEPEdNm_w3rcGNzuI72mo_i93BhyzCQGzPwiT0mHz3sp24SRAKutOKAhodd18veXYd4O9kxr7I9VlOEGjA9rhuGvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWY-ENO1T7QlrhRKez5WGtY_9vF6sW9C57o9-PfOof4kHWGaofSAPGDpqX0XV98dlE0U0bJQLbxXIC8J1-0cxQnXZmRZsJzxf5FhLXfFi8ZEfb1sydy6j266RlumhcKw1ccfPjpzY0cO8sYcWEw43r9hukUux8NJZlTXu_-xel26f1EukYAp5H9D27Nus1qYNTpt53f4GDeSctA-j48GaamC0Q7_MBtXDqwDFrEbUQD4Xh0eJbY8ZDhqT8IWyDd0gQT0b-3LWwrjqKFJyIR8M1w7MUeKqhbmN8BV3pm7e9LIQ1FYeeM5lwDxhwCuWcElgt_6RL6O_VKYvbvx6rx2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt4bOvzdbnxBJGmgn8Qnfw7p6IaZLF5GlzFU1kM_MlqFBeIDjs_GtL6LXcG7pAeilqj2r4W9s971a5-6FLmf3Ls6YJcpWBznZBFNtFtIdhCpkN4Tc4uSu4AsLRpeMEQrMbb6q-aD_TOXBb5iPt38qzt66jzc0sdUNdlHvw5AYkrZCYPKztWTsYSagKXAmh9l6dbYBNRrd-eZJsNYJhmAwHwhLtKnc72CzkBx9gRk3pIVFcF-L1D-aCd42OhLVl6k377_HQccXEJEEeNVJrqnCHFpi-XOSSTIx8QPfE88pGgyTHGD7bQ4B6Fe_4OL2OLpdekal6CYCeJferbU4eYz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGy7AvCRogbR8wGoce_YAYdX-Ng5_qFyCDBIOwM1cjKbZkS_NAcba1Ug1rbvkdUeGvx8-wHKS-kStgnZjmMNt8qC_cuAb3DUV2ZBXMboCIeFwvlf88Ghw59-JXk4tYu6eP04gtN8RvVTAqJfnL4xOBp-_VSZuAtDOhCu__1VU1OACoWA0WR4rKHPWsuS_2qhzE5DD1-8Nt6-r5ynpKQ6YQiRfx6u6ihtthUzwsx8gjUgbudRKEO-dmey-nXo_gHwCQEKMKPln3srEGUm5-T2mKW5ADKFVZfjdjvUTUgaO37EHYlJeUCTmzmftRTOZa45DvDwlgoKBk8Cv-ZznFkgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=E47ssO6SJuAua_VwNFEyezpnuMagg-GHe0Sx4Q97IGe_FHS6tvMEpDlwx9FzH7H7rRE0Wvr2w2tBy_6jjFADozuYisvcEOEjOLPMsHWfRLcgOa6KAEElepP24hd730HI5ttpU5Y5mBud1vCNUUijj7po6vsGPvkfbCa4-UipYNdkJGEUQrD7BiHSH477kKGFgOnDDlFiD2798hobeDoHW_JRqJm_dAhvrPgFinAoDcA7U8HUhflHvHjXxMBlajhD6LU-spEK3Khi0SDp62F6U-AwX3ZgeTtC20tYQ24peEJU7HUDtmjl6yPFglCoUxps25GV5Uki3tObF3XV-sFRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=E47ssO6SJuAua_VwNFEyezpnuMagg-GHe0Sx4Q97IGe_FHS6tvMEpDlwx9FzH7H7rRE0Wvr2w2tBy_6jjFADozuYisvcEOEjOLPMsHWfRLcgOa6KAEElepP24hd730HI5ttpU5Y5mBud1vCNUUijj7po6vsGPvkfbCa4-UipYNdkJGEUQrD7BiHSH477kKGFgOnDDlFiD2798hobeDoHW_JRqJm_dAhvrPgFinAoDcA7U8HUhflHvHjXxMBlajhD6LU-spEK3Khi0SDp62F6U-AwX3ZgeTtC20tYQ24peEJU7HUDtmjl6yPFglCoUxps25GV5Uki3tObF3XV-sFRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgXwFaaPoGaAX0jlpju0BohhQhyuIAVHdXgW7ssTdUWYtU49LsrZjbkqJ8IeJD2lZbjXgat_7hXTqYVzvYtaHf-uUH_sOr8v4Z9Bcf0CLYaTpUVBEGjJRY2CvtPsJvc6ya3LA3rcvaFpm2Qt-HRLzcwmW-W8e_1ePXpv8DhDlTyoouTihbQOtNR2Uz2IIkrsko14nyXYP8ik0cnEWq4ST_d1D2yMLPxsMmNHYtkuseYgnUH55FNrVU0yfTClwfuWsJb5wqjJ4hkV7r9TsqRbOR4TW7fov1U03GgbaTtGHN_R6JZSlRd94jG6yivLIxmehUDKxu2fCX1b4gYbwejBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH7J7TggoJbQ8uusB6UMs4q75YweS_ySFxZAZfSvNlZ23P5aZeoEQGzjPDHE-DVg6A1izEHOtvz6dwbXANAXLWIrJnS1CsSFjXuLphbsVvd5P3FlSnFrX2Hi4oJTdq56--hxG9s0GlbsFP9xSpdb5wXCTAbCfip3mhDWvIvMmsTCXArduaCtZ4V2z8epjHOgZGUiYjGUihkYDdGRNDJI4dPsTgXTHihXNru6ufEvVkVguGbXZQBeiYyMKEDalCv3dEl9XaBmlH1BpSvHpxaFLdOt6jmAS9Keorcxfz0O4RjHZJ8wg023-hhBOAA6JN96U-CUpmYRaRZRNXa8THV1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBD4Zgnu2QB1gd8KzIbgmvM-yi2jV9U9J4ggG6PZes-L-KVbkevz8hUAK6IVMUrmIlJC0ADMfpeqPFqvogXQFVoKrP8HbNSMReDR9kp3RWQbQUO2KIcOeJA15nTDBM1ycATegjlXUCT7WGn230VK_dezEL30Um6kOaAog46l8g4OJCqMUMdKnudyDHVt3yUHR2vp00vAo_SeYpnmdxqloGwUgSudo7tDX-kvKLtSXntNVjc8tFZJa9-MXEfPCh0k_S5HLcjp_jpv6wklXyVW_KxCusbzizty54Nf-Bxv8CEqBt5uNKxog-CEBqYuHAZ-E_KfXb0j2odXT5C1rT7ReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=UK3AMP-eTWx5Dhxyp2N5Tc3Ky9AHfKlwiuRrfC3yTKL84R-n2o9Wjh_6SeaeAs9sPJZygnm4lF5LT6D5Yqnd7EPtjv50y2YpQI7cvVtVdoL5a1NpA6t5rvoWZfogs4EJJNX4wlkUVZSTWZobWdqkgnvPCxwKiPrspwbcSLnjieWn0YcQ9wQERop21VJc13bQl17dCv7Dqekdn_bskWomYg3BTRxiEi_7_SFP2ZER17DYhqbySl-WEwbW86QLGI4bEaOiCYOWqDdZZlPGg0fVG6VRtEFVdM1fQmpTafa2030OmYgRVh-3L1uZGF_CjJRKsCtmGXVG6LNT0wyB6-QBuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=UK3AMP-eTWx5Dhxyp2N5Tc3Ky9AHfKlwiuRrfC3yTKL84R-n2o9Wjh_6SeaeAs9sPJZygnm4lF5LT6D5Yqnd7EPtjv50y2YpQI7cvVtVdoL5a1NpA6t5rvoWZfogs4EJJNX4wlkUVZSTWZobWdqkgnvPCxwKiPrspwbcSLnjieWn0YcQ9wQERop21VJc13bQl17dCv7Dqekdn_bskWomYg3BTRxiEi_7_SFP2ZER17DYhqbySl-WEwbW86QLGI4bEaOiCYOWqDdZZlPGg0fVG6VRtEFVdM1fQmpTafa2030OmYgRVh-3L1uZGF_CjJRKsCtmGXVG6LNT0wyB6-QBuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCJPOi_nb9pUO-N4wIy54s4cJWqC1_NgAlaKjWpjk_F60ovf5pZO2Ln8LOppYLSM2UhJFg5YY7FqkbXwsmfDKDn-OZOyuKxTxiJWQf5WL9SED_gPwn3dNjTmVIaFKVinG4ZbT4hu2P4SBg_sPTp7V64f2h24ZNxKzZkd4u4x87M64nvxu5w6OsvL69b7_RkY5Zm_3foh4kt7Kk0tDdkFxdBXWf9S7hScT8ilWqz-krAnOxGFkB-i-zil7UvmCdP5-kyBAqkMK_eCB2rzSWP0EL-JSyPja5JTg-qi0qG2ze_GuLGdwS2_sTkgBn1y0I1ZkXbF6UuXDmffu1up2G2enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s06Uf2PCBkDXxYuj1962IMI5aSnsxRVK6VqQWioH3ocr6sTz71w-kiNve_koCLF-6PvZG3n_USZTh6GeHCUTAxEOpLLOExic4UHxVDhLeKT9LnM_qtNjRzpAPrp9ylrRt1gA7rsnV1BnSpHNcj2qi9rUuW0gDZFOud3_G8J9LbPSkNrLCyqpGtdNcQjAbZCX0u1stWeAvhXUoq3z_g-78IQieYB8FnSJSYgkaY306XHUfkSq29kWNkqYy1HO-wPFIWiEory2J6P4cg8O1ON-Oc0Xv7DwBKpiz_C4cOmL9IrKizo89auTg7fe1Uod6jXJsCSRWGCqUtdNWoGxFeWFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8RLHy9ykZD7v8pCNYAeW6MyR015ibnj2MIIDeMc1CMmS4IzucdZOqu5O7CFQuLaDJEDAneOy1MrbasAtiToWK9_tcicqDPUVNgqfYq0fU7TYwl_WR7f5pxq7r_5HNqaHjDRemUGHYBIBstXFlbLKiDZkMDCBQFOLLERZLzbQ_3nVmxI8yuaWZeCs5WsRj2eZCk1f7QlgiRg6paBrtiSlJzKwyog16rGRWd8P_zGESJMU1IREAeqqd7OFzGh0rE7GBiblsNX7BzTnDmuGvZ6P19CxG8WiNm0QhupALOhvWZvUW9yxDBrYytHEwEuhxRwZBDtKGhWWbzvh1Mnp8vF2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyyIE0oV7ATWAmqnYtGsiNRLz0HREuRvN2MsIhCEqGLFZYaQYzcXL0AbtLc7RpMYvV1FkFc570NKXplD_1KwuFrXzaPDZOJmL8bNso_ffHBEA0ch1dl1GOXGgsj8XguIhz4phmBMH_uBNUyDogtH5Ieo90AhQB325_qTcOWZDJajvztcrmDl6titcddvl-L09yecgqsiPIOtn3IfHicOMIGySrqUKdtJZnbW4j-Payr4TLBlyxGenmaf4L4zdbEi5yzfm8DLi0kAww3ISbA16C3ee_LZ8RrU9G68cOTVtsV_VAYtXkD8K9MZPq2cvpSX8MpY9hI4hqIUnL_bFTMwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omwyTy3ZgxH4ydfG0rSWK8cy8uwBQl1vAojVqsAJi0dqEY8zv0ouxAwSfFYQff6_5UfZ43XBNr5soQakNS-ndFqrdfIPHtssa-utJODwJzclDJG3-NKhEFRYvsgx8DxV-YWR5SboqeB4TI9-bfCgPVGgVVX5VXi3nBri7hK9Qgnq3RwvOHvrkgY6yiFOHbs_SwQVvg2VN2VN8OwV-fWTNMRqrWjv0ij41Ja4KVZagG2OTx8XIzrBsa0x08ufkDwZ2Cs8xMpgnfHmUOgaDCL4b2N0SSQ8eA6OASxORaBY9b0ybqcDKbgowH84CgpU9y2m5-vHOL5y1xs4MIqFQPeHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE80mNxQZfg4VZDpSQnJpN3jIiTOoAripR1N1JFqrD6gfsqdJw-5h0a60ujB97bYbAnxG4Tw7e3aAv5G3c2kq5iK3TuG_soy17OgT2B_MuPNZIuMatV32Wf38oY7vLUnMddURFcc43XaklTsOMduEaPAKfv1w4xS3KNLP4SWpX-skY9amAlrbgkssfr0-ZhbmgFlTPokXxHS-RDhnK4QPiAfXCKKx1Dj314GOfAGBK1EVcxp2mwvGhHUezsewxIMTKCKArcoeKWVPuzqwcVbJB5093fMCbNbnDCYfrwX8ZadN0706yW8vJV6skXv0fRbQ0rERYifrdoNfBUx-dQTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REG6MATZ5ifdTY1yPskm_YKbPOzBdaqk71zMI6JQtNiEqm8x-bzcEBYRJbKxx1QKU4grQtc0z_j4zuiifchWrikernUqwsQX_vkDTQu3FzndOHcW3t2aBJdlSGfPGvc_EcPomAPYFPb0k6k3MFodysEJkQNtbqd3WhGiS7Fc5Xaeuq7iwke1wqLqoEP13DNqdOloP0GiHVHWTnQmAsqmM1iQTY_9hDX9bksKNQt4Z8OR2RIErO2-OnIQDKLvKPqNMk1cy6zHRjBVZEK9X__OLHq50Hj8CSAHGNckNprFZLwl3b-glPTS9KbEF4FhvzXfnGN5XD-ILFCVP3xdz2AISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfPA1tsCdJv2xnsQ5xzVO7-kvLH_hC7zd4rz1T4pbN8BihTQIlItIeCQZhqDH28-bcd6IEh9xESc4hId7okOcZSia0QrnpGo6IVX9p7jtt4YOo1qnbbREmCFSD4GV64IVBWFAi1UHGQ34QvX7pvX8WtYxrSZxidetQo3p-b9yERP4Oot717fVmVIXEU2o-2cKk2EQw_1JF09Kn9vxKQgp7t0MWlZQQ2dxeygIBCJLEbJFBm8CKQ6FFxmM2d4yivNSIKSL1oRAsg8Rubte07mlVnIegLvyJdrRVNCurNZXuHJ3eAcWNBRrfe3ZsdpOioLci7mpba5ZVJUohEuj2dn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jInb9oV8PzyrlRUQ_yTak5xMQobfrEA1qIPJHZvnR80qg6Fzp5NYU0Yah9LLhoj0bTMyRUHHxIUa-jdiPsZTNX33YcaBBkMuWe3otcDwz9ibtVxFqtDuLC-ItopfxDIIndjJxqVjtkuJq9GJ42kuHSVwN3Rk47mkteYXR9NQpL75TskHvOtZ4Z2-XkMRnNtNySz9mZ2tqkxxnwMgnwOVkGTAG-WOoq90qZ-Dj6A-SeHtSehX03JEdOc-ZU5zkXn4xMIO3LaFJSa0qtNb_jfkpH4mOjZhziXBAiND2-zIEX85b_o-dfJhux-UKBcEqls7oNvbNcMNuHWH0TiTPyszpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPGHge9v6PpQDyL2LFZoNJTGpphZVoH4OaYRJI_WdhZy27VhdtAfoN4E8C204Qhk3IAb3X09L23VqwhQYBpdLW2PD8IphdY183gnOAMxCN_eKUqyexvIvBTPfYRvORuNliIhGQOiIuXkZXQ915RBy2wgviULRh1y_Bsuxs8Z2knpSOta5-pZMm9xrBDfBBa6Y29gXUW0q7-UBTq4w9a961AvoAJAJ599NKvHW9mvI-5ElTFiMD4FVnpYJIMQkC0Bb7aS49_1okcjMPN7smceDog2h7CBLqvcYLXlrHqapmBNNliu5-T7JXOygP1OZO6pXD2LGxxxKN62ewCXslo65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCUOihDFFR8nJ3zqB3KhupEwI2FHPzZBPXUvVC2NVNuUisFB0InRSbBbtoXqBMyyiYdN1F3DPgNtaA8o3_Xg1Kqt_G9nJDC1H3_SkrnvVZxH6iQP0h6ewwBuLXoXA5a6QXZJTBTD9FrtJGx4kaPBTDXWKqqBduuUEmLPZXPa7gsaXL-DewOOqg_S84djNSZOhwQvhUAJz3kf778g-77Ol1HpdMLM4y0iOatyij_Bnk3H2Z9Aw1-_IPfc9LaVtFH1LYtyaqA-kBxOt6IAh7PP4dZbuPZr1MYeitcYAn4Z1HkujOe0EMrdYyg66eZajqEUYvoC9XQNhmKyD_WMLRRcKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJ89WI-tDk9X9aONVbffXP2LDbk-nZPbEB22aQNXYwL9D2gj7-_N7uRTp1TaAfwSeiqCulqjM05owP2O4aGCudPn0q7CNktNTEf8-K8kT29yaVB3bIjfKUhUgbmgyuDJC2MRNgjw-vVMicY0k_YDh8DxVjjNe46juMmWC2BDLik8KYVzKwgAZa1NraaK1WSkSnKIoN7ZqQeLNbc1493W0aO9riQs57YPs6JMM6hdS9IvrxmGzP7oiPi86_1UMIHXrJaWfX6w2p8CQ30CABV_rZrkuES4xW3XwtzElDqs4whI7Q-wMkIFp51ec9DVbyX5KUDnlqYXxmtXNKzdzk67cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prRISydCrGW-yIRv8sqRsQjNKvSS-80LA-oygw9zpXVqU2emTYEp40AlqcpDF83T3eGRv8J9SFIAeI7Ea9C9Z2e_E2-ParLD_fx718AIgAjN1J38vfmwgNWmGo5_ejZKjRLtCuQymqsnMk2FcqEZqTs1OID2A4x1gHCwEv7bKjnHXIkuB3OFnVObMdVMv9cz7nDyCk_gLR5yYC_TICS1BCHyapQrGc8IeafYplrwdN8_BtaOu2fC8FPsWCqFTEwbNZ2hL86KUr6XDBu3_niykSY4mhmS7cz_vgZuWQJ0a3UItW4qj0V4WM5p8Gf23DGyUJxgOEEuPP-wKFzGSrfM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwD-4Wgpb-YjQ_ajW9q_r0470-E3fJzQ6TuhGWk7F2pKrM6R-YZsWZ4YpnIYVqzlB-nZEoDud_NQ8dwAq6yLITfyK-mOe4-mOPB3y67_d8ug0dHQOkdKPsuaAvYZn7OJOtWNW1ZcCDkxIyLM98U8-B4Ph9pbLSWIwfTbh4hME6HW8-vWRhR0qKM4RZz6cmv1dXTPAMIF35tNgi-XNcmeiTFThpMoh0TkDD7WykExTJ60CVp3HTY_ydsijiRF_-CtsUMQm0DHAYXdRt0hiK5G8UjRbKwXPyLcH1aG554RTNvvS-Ucz3ycXjkXCdyxrs9edhf7M3TNu5f8bgKLtxYcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi1AoQfkghIQNiu8bI1dBtwAQItpH8nFXcrsWBProe0xLNGeM5fMmF6w4cWeELzPxpE5PwpezD0r9goFroY5sjNcpwGkFSo-ySd6dCj3nKrsS12rFuPHINTYvfDS9mVzrcxpNnhLygWyZ7j63MR50E81E8rPFNUYk0fEj18MN8ufIRUPDYJqBP6TfRMrK-ws9LFzR5woOakxpCnDfWAWc5sp58VrxIIul_wlufAo6zthFCj2pADL92zMjCr25QCucbx3m8i0gaLrtsWbbwvrVB0V62NIfrt7cTTNyG0znYzJKBUPfAm6x9qm4LBE-lAY4_O080UU9w7ZfUBdxjm7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=T_B9a8vtuh3zm-j4Ca2rTonGk0N-tJ9e-GH5nz6M-JPs7NV2q6f9n3sakL7E_taC456etxrGVgHSVUOD0BvnR5H4GatnM8KlIMpypQJ-3wN7PLkDedTo6Lz5DIYtewe5YoPHPlJnmjy9CE-Xx9caJJWK11VWFvtZ_rgEukNXApVNQY5rIX4Bx5MJ_zTmYI2t1eCrmw6RNVFTV8R7uV9GCy5Ot5njPBu1Pmf79D651k3KBQ2li_i3-xCgyfQxIPGLTWXjOCAJ1UI0c_y6o25CK86_GXfFo0VF-yDdcsJ04S85UDNJC_fnVpUwa3vEBNoZrauDG6S-HxE6XUSWlUpbBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=T_B9a8vtuh3zm-j4Ca2rTonGk0N-tJ9e-GH5nz6M-JPs7NV2q6f9n3sakL7E_taC456etxrGVgHSVUOD0BvnR5H4GatnM8KlIMpypQJ-3wN7PLkDedTo6Lz5DIYtewe5YoPHPlJnmjy9CE-Xx9caJJWK11VWFvtZ_rgEukNXApVNQY5rIX4Bx5MJ_zTmYI2t1eCrmw6RNVFTV8R7uV9GCy5Ot5njPBu1Pmf79D651k3KBQ2li_i3-xCgyfQxIPGLTWXjOCAJ1UI0c_y6o25CK86_GXfFo0VF-yDdcsJ04S85UDNJC_fnVpUwa3vEBNoZrauDG6S-HxE6XUSWlUpbBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=n8Hv9BMn3AhMdxsb-giHGziVOxs3b9J2Ua7DhOdaotVrSP_RmryyVefEbFL6iy0yqTmlAK5sefR__mpGv3jwS8oJCxfVWzSfHD7pwfn4oZxBfWAxZhHDgBMlLs5PWA7A4adPoPnukV94vROsKtmYnRFphMW7aYMfjKWErGliPkGSAVFK4gXmR-mPkDfvOFoBMA7jJ6LVCWVqvqaPHRPegHsvUMTniYwHHbyd-xy8y88M5nEBqXGXPcr1FOMqGTFz2jgaNFBc3FFMbfKTzWgfymvtN4ybxKgZncXxJAE0ZrWeuwDiXM0DZ42IhN9RfPVFXvv5IENINjM4U9YgUGxvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=n8Hv9BMn3AhMdxsb-giHGziVOxs3b9J2Ua7DhOdaotVrSP_RmryyVefEbFL6iy0yqTmlAK5sefR__mpGv3jwS8oJCxfVWzSfHD7pwfn4oZxBfWAxZhHDgBMlLs5PWA7A4adPoPnukV94vROsKtmYnRFphMW7aYMfjKWErGliPkGSAVFK4gXmR-mPkDfvOFoBMA7jJ6LVCWVqvqaPHRPegHsvUMTniYwHHbyd-xy8y88M5nEBqXGXPcr1FOMqGTFz2jgaNFBc3FFMbfKTzWgfymvtN4ybxKgZncXxJAE0ZrWeuwDiXM0DZ42IhN9RfPVFXvv5IENINjM4U9YgUGxvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=bkwEVjIfRdC5qq_fmt1CyszP2ebGlYvELKrtIxXQTgrNBJezYHskB5Vz87O_oP9W1l67eOXboNb5fNVal5xf100HENgJ5iKEl0yD-ZTpZELB1NesZ_1zy-ww8Oso8psiV55bdu72rv9gd0c9-s9XCOFAghHQPCiMZiFCnVoXlXvooyS9eLbvV6j1AvzV51hQSp_c6pnZB6cpl7JUyUJwc1hOmAJXkYHO_HgrW3ehi-uRPAsMpQ1_BkqwmRcyYILJSs0vC85huyQxuwFA1LfdhjquJ50DnPR46We7jbO3djdCVoVFM63eNz7x8Rzd5bU_WQgytRSfXbbjbRDGcR1Wig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=bkwEVjIfRdC5qq_fmt1CyszP2ebGlYvELKrtIxXQTgrNBJezYHskB5Vz87O_oP9W1l67eOXboNb5fNVal5xf100HENgJ5iKEl0yD-ZTpZELB1NesZ_1zy-ww8Oso8psiV55bdu72rv9gd0c9-s9XCOFAghHQPCiMZiFCnVoXlXvooyS9eLbvV6j1AvzV51hQSp_c6pnZB6cpl7JUyUJwc1hOmAJXkYHO_HgrW3ehi-uRPAsMpQ1_BkqwmRcyYILJSs0vC85huyQxuwFA1LfdhjquJ50DnPR46We7jbO3djdCVoVFM63eNz7x8Rzd5bU_WQgytRSfXbbjbRDGcR1Wig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuyzMwzZInKY_1deijfY9W7MKwpOQTZUdx2eqgDNU_j7u4_W0NziELfzgdaY1QW1ohdSzLUl8pp7n2AUsIiXjW0IxL-gLnKTKdRF1OxvKwuf-gtk6Dd4CIcMi32MJK9S2DYqVppVjNhsqMG410Pl_LK03tz_Zn-0fbdlodrr0Q8drNbjmD_Fgwj5TI1BBM9A1XfuLzB19B0BVDsks44144Yl8FK6unvjaZEYKyY0W64fkW7_HoAw3rTM-ZCQ4iTYoIrnjkEY8LmKXNL9JplPEAbmvukOeSV4EQxObSs5Fwty90_ZJKtYrBQQVSdXzEsOZcIbyRP9GJkHWc4rbjXCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYDt1-zJKqQjCXCDXBC8sG1hyXZ0FseYXYJLUxMi7W9wKES1YWhMrEiRl1h6zVR3jjjMRAZuslsenIJlqxG7RXYftze24oZ2-3fN3mZrtcjSMqVWP941W2eoFQA_uaPQmaizYRFr9kKcpV3_Tte6VkGYApy-J0ppUw9QAOm3UOHT6ff04eVSjM7XcwIfplxRxFsS2qtC4qIOSyESlV3HB-xxJr3rDe6lTUCRsFCqB9i0U49Gw7_CdPSmQgQsf0Xxh1pcGpcK5qD8OXlxOUBFxlbIER4JViWTnJXqSuzLJG1wMAu3OaWyCMEW-HzIOqZAz_ZBKZ8pmoma0ZKdvv2LHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw87qcA7T0QtMdkNsSsR9zPt4dcmuWC9uLueaA5TaquczYLvstunZrdj2XgCVwdcvh_5TE5hs7UG3rSNsfR-7KajJojpXYOixE1wmL5krnzfy1SW5paZxxPmx3L6qj1mNG3L1-Mf6fKNBq7GgiI0pn6UkzxWOGZnS1eerVy9j2CeI2EAVdR0wtTDBYZ7vIDRoKCI_Cbgfw6heaRCh5MvW28PNrfXBWYibuMQK_qiNqUmvsoyhMY5MVMmhTvO6ksdAqLcyMJ1JMnkCoQnQT0hImB9QJ6CD2ZAkxd19Qh0-De_Ft9ojRUYe-CxfvNbr7Is8e0spN642XOpK_wK3BcuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=RWQgx_Wwp6-VoO82DkAmYb2CsLshSpC5a1DDUljndBaOcMRdqiXPQSNWMHlaX6Bcd3JPZ8W68qD6i1JV-jLg_wcwnh-cgEmehQG9g1BUDl5anBdQmMrC2EAUNrEAFhkMRDveszIty2BuE37YZHyN18nY_jNnKw6IFhx85FwlC4GfA4ZKzsMzRZehl4lYKSNEMnubBgsko8NxM1R8pfWkmxer5VhjZDexqEygKQDxWdTW2KHkybofrzWsiOEg7L3appZTsbKuThWYfRpiuoVGN9jcBmHr3ay2sklhKwgPPvvECzaX-JvDhH0WAJ7_d-kL9CC82QGHK9cAyYB_uhtRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=RWQgx_Wwp6-VoO82DkAmYb2CsLshSpC5a1DDUljndBaOcMRdqiXPQSNWMHlaX6Bcd3JPZ8W68qD6i1JV-jLg_wcwnh-cgEmehQG9g1BUDl5anBdQmMrC2EAUNrEAFhkMRDveszIty2BuE37YZHyN18nY_jNnKw6IFhx85FwlC4GfA4ZKzsMzRZehl4lYKSNEMnubBgsko8NxM1R8pfWkmxer5VhjZDexqEygKQDxWdTW2KHkybofrzWsiOEg7L3appZTsbKuThWYfRpiuoVGN9jcBmHr3ay2sklhKwgPPvvECzaX-JvDhH0WAJ7_d-kL9CC82QGHK9cAyYB_uhtRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=C390fcVXf7JSl8kmWIw6Gd8ebcqBzzCJIryXBO0juygaQG9UZsCJXPsub8q-n__DMhxZcDn-pbUHGhX97MZRLF5r4177G6Rq-Rom5XdFz2i4cezc1D5zj8dA8b1W3qdS2k_J6ztbYlfZVkXSqnIaCdTt40kKHHuM-KLkLCkMh11vNPOrRZsI8-zVAzWqVgnCHLTdiJhl3j0XWWS9CMA4u6sDc_QkL0eIDSA1TLkSWPXB772L-sNloZ5QwjX2J4fTOAVD2AewIt6RS1-zNCCNS03tdhcgonC14iwNcnYTnUKLD_f6JOQE__GhwgeoiAHphpV8tTkxuW35pwBG3oUAMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=C390fcVXf7JSl8kmWIw6Gd8ebcqBzzCJIryXBO0juygaQG9UZsCJXPsub8q-n__DMhxZcDn-pbUHGhX97MZRLF5r4177G6Rq-Rom5XdFz2i4cezc1D5zj8dA8b1W3qdS2k_J6ztbYlfZVkXSqnIaCdTt40kKHHuM-KLkLCkMh11vNPOrRZsI8-zVAzWqVgnCHLTdiJhl3j0XWWS9CMA4u6sDc_QkL0eIDSA1TLkSWPXB772L-sNloZ5QwjX2J4fTOAVD2AewIt6RS1-zNCCNS03tdhcgonC14iwNcnYTnUKLD_f6JOQE__GhwgeoiAHphpV8tTkxuW35pwBG3oUAMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_r1SJ4wObqwW1LAqtb3B6bpg01nhmU6kqh164XgEyRiVEvVRv9yOh36chJR6LuRXqzsIvP9KUgiQ4rufUB5GMIikFSZRLgiXGg79x58_HZ00xr5soEaqFEPhQo2g4EsZw1mVzsC3J6TdSiZw-OFw4NYiZDYGEANjhS-mGULo9KmuJSZ04GIfxOYR0q7FYkLqmpyFG4fi9g618-8NbA3A79-fDzkFe1wGdKeK6_V4eX87SRBGmi3EFqwlX7viLTpCrtHudu-sCMQgujM8W55T_vSJhME3xj_uPev10qcLPCekJPtWc84rmR104mJ7zs0rm3aETcpi7vNnLDIVogShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEUxfg3lyVXLRZiTQu48BMTOcW4qIrjOpIjhm0j3KawLF0a3BNiPjM95BU8lg67GPkWk6mZuWtvBLiwmIcnS-5PBwwXG729rRGfgSZLuJXrXMUCnyLPyxSpcF2NgudRmXdoe1JAc9lKHCEmcPogBHb8wS_WH0iFede_RH9yGCwh73eA2DyBwsqwv-faO7EML98B_IHmhtXcxamcQ35xUW8w3dJDRCAPBqyrS_TucJPgl885Qn-qRRc0OcsDmpqZTK97fKcjIRBkaIgCafyh4SofH4tl2E6uK6HGutIjR2Xt9eUiziVJr0TQ0NjD8tX5sDZ-GiDoAuytqb_fxvJZL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvUojFHYf7tT0pweQYHSpEnPEe0oHcfYBnF8G9GpOxc-n_vC1Wt_m0oU6Wtm5Sf03_Ypp32Bo-mlZg2kvCVCsJXPsWc4pjLqjbDsF0SvSOIAVlI2isoYizgaT5NtaI_6l1Rww1MWGIpybQAtrgb-Oj82gX22teIM9DU0Z9FptDpcv3Xo9pyhmiVEZvW8BkN2RPOY8H9s_6fceWDxgc-8S_8ly948kJGiYHRtFe6KERqWp-0dZv4kCMZLcE_9Do6Q4t8lOLZiv40_2ZKGCl-PzN5Br4LSQ9Mh7BY9maUwLHgmDzRXUB2Ujgtz4qvrUHvgKv3zib5d6Okf2oKkYgSz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N29xxIVuG5wQo9jVGfNeUPZ96lIAhy6nNXG7zG7YZN4XSMYWbrRtNoRMTAM0zqEFd1g2mcbjR5El6SQ7Saf_YoS1HczteRbTImeUwTcOquxYORIvOC0Y4tYpWzCaNcScS2x_FuhjcEfAel_C0z_qUu-XO403apHcL1b4xMxIWlnfk2ODcu8LEBSLn1kTk18HWM5Nr8rVzqTwtNG1LLNXbjlViq-J-MplT5KVO9INkOvVvrs7JWfk0qH1NiFsXYZWzGnt3avmToHOyTsmGSyk7_O3PoQNOT_6H6dH1ErODdNe-5JNsEAe_Du8KRLE-h07tlcdycImn_LVhp26BrBNGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tG_qsAMkGXOdvCtpo6DSk1VIda1TrTedMmknZmfu1lH7d86JB1V1qsMeRRH6xaqmCd2eVGxfKfwm9I3kqz5mGQcvQDIq3hFcJCpqRVdM4wdD78UUgbj9fSlBc5xu0KYOj1egXWXGnfH0BLf9-85FKpSVBLBI5Xww4ygX56G401YhCBb7x6Yv4C4ee1Hp6MxOiUZQPLv-ROc5B_NjPItmi-e8LAnSK7Ycz7Z4Dn8g0VCBmRlk1NfJCr2UB0fz_SFVXHpDUH_qijlwn0JVAYZ0YOKwgTOCnZL6DitJj6zurYf9d5PAztQAo4D3dSnMpA_Mdv3a0w2rdfZZtD_knqjwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTwImslQhxv239t000oEFR2dZmYdHnHeOhxxnsXJt6OoIRaFbI5HD3FdRYTVaFFuQXiOGPkIk9d49wocfL0NkCkv0NMZzaL74UITicbzLaTIo-YpZWSOj4XGkBNX2Ih064bC-RV_kqLiLo3gvbLd4h0zelUbWFDQyYYliO09c9IPG3bTo74YwrsHXvvth-KUpCuJbwxKOfyfvaRQ8-SQH9UIs6ytAAYtevXg4FHDKNt4w98CJwalwICUpsv24KZYpz3uJCNA2xp37B0_URlI71H4NNXpYbN0a701pMppAZIoXwS_Sqy4u8MqUoNfOswX8j2bf8UtzsVB3N08PEFuaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=WTgeISweVub3bqyJx3Re4QZiG1mTwc_sXhRzUXlXCCc__lhvJPkdpyRDSqK9-bouXeVn_G-dmFvK3DVqDSPfMjbg3JlnunJP6HSWg-3epfxFfoCRtyVdnn6xD75B7WaHaA8s7fo4v28a9OvAA03S1VG8mziXZcyRAFckTpMfb1aGb12kLITJupCA6LX1tmMNosnewYf0TiuPbo9QPXPrpwcpF9V4BiytjS6fzCZw2TFFoYMsxsYz-LsmQ90n1MFNHE6eLHlJyRCS2t-UgoZMB_HGXB8OwYA2Yv7PLVgluWQWYA94efqBp9Ctf4crlJJCkNYbNC2fd0oVYXvEWQdBBzl9LiZ9S5wOSIBe5-A4KDFqlw2XlDW2I0ddyFfRdrGDz_YQZ4JyPVUyEmpsVe9q1QnOZ_DHlWUTet_p-6TRiYpeS-ieqdOgbOROD5D_Yj3g9jIfmaHAuvChQz33VMhxnGMjJiRGKcsH_N7b9JoAmXgowjek297usvG_RQw6Y2nYMWc6BHa77lgN6pxvDPsVvnciXC_KTnhtVyHKL-_HiGmRxBP0qHfbWbpZcX1kuL2eR4Bz53dUd68R18br9LW8-m5FgE_cECXe5vGgJDxLbwnGEso57qPqcnNFiwFHTYBbzeyyNgAS-sm6tTcbcTGrEjGTGVPZHgn-QVDydlB1CiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=WTgeISweVub3bqyJx3Re4QZiG1mTwc_sXhRzUXlXCCc__lhvJPkdpyRDSqK9-bouXeVn_G-dmFvK3DVqDSPfMjbg3JlnunJP6HSWg-3epfxFfoCRtyVdnn6xD75B7WaHaA8s7fo4v28a9OvAA03S1VG8mziXZcyRAFckTpMfb1aGb12kLITJupCA6LX1tmMNosnewYf0TiuPbo9QPXPrpwcpF9V4BiytjS6fzCZw2TFFoYMsxsYz-LsmQ90n1MFNHE6eLHlJyRCS2t-UgoZMB_HGXB8OwYA2Yv7PLVgluWQWYA94efqBp9Ctf4crlJJCkNYbNC2fd0oVYXvEWQdBBzl9LiZ9S5wOSIBe5-A4KDFqlw2XlDW2I0ddyFfRdrGDz_YQZ4JyPVUyEmpsVe9q1QnOZ_DHlWUTet_p-6TRiYpeS-ieqdOgbOROD5D_Yj3g9jIfmaHAuvChQz33VMhxnGMjJiRGKcsH_N7b9JoAmXgowjek297usvG_RQw6Y2nYMWc6BHa77lgN6pxvDPsVvnciXC_KTnhtVyHKL-_HiGmRxBP0qHfbWbpZcX1kuL2eR4Bz53dUd68R18br9LW8-m5FgE_cECXe5vGgJDxLbwnGEso57qPqcnNFiwFHTYBbzeyyNgAS-sm6tTcbcTGrEjGTGVPZHgn-QVDydlB1CiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpbA606eWxc0HpKFrFDdRzhdxFmrPSqEmWCM97Lvfdx7fBSIdyt2wbYOnjMuG2542k-P-QhNLZKQs-tC-Fyaru4wrwlHz8J5OOWulAG0eIQSfl1m3GfUAGCMB_PflzsLbngBmfLDOdhHnodiQbO2iR1EdYGxxtWAxcFgGq8i49WjTUjpRbfG8jnRDps8v_WdAd1r1ZWeMJpMjW5NbLxubBh0Bs_oJI9tdlryzJX80ZK_97UU--iharx_6H2SzakfK7o6q3eUekvK9AhfQtowyCSUCPDlnU-ph36Tu1AS_36K0Qkc2Y_rIXFNWQa_w1bHp9AiTO-NDhj5XGtgz1l_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxkXmgeQETMHs4c2dud68iAFxlhbD7UMYfL8OLWy1TPUw8E-W2sqJ0M5C6Zg_AgPchp71IOPvLZc8iiSgVZbiocbVPsx0b__5RBcyEVzX0-4B3oHDPcjr670MvkF5F-Lkc0S-IJ4sxns5kXQZuxGRUBBFeXpWIPVqq95EPovPQTvex_S23gBmGLC0r-_oGuffh9BpK6TJ6voQUDjlaTbfm88w-pudv19O4q6XK6BXxXqVBxaeaIuuerVVtReOE4zGNZ_kbwnfk7Rf4B5tdFmlRe6Xsm-uqSqDg-ZsU8tZCwU98pyYVMB8w7moxNkYS0eabIB2bBPUy2LZh93hXmXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=lNU5cpc6TdmzGF4gcWZZv0DE1MkGyU7lO0dzwH127cdb3WOGJUkbbvYXwePTi0ySqkOOwdJFpJHThrPEJTo0nYu8sslYplDO5mr_hNvOsLYC8lERMb5oCo4oZqVL3AB_CUABgsdqkrgPOe6DV9ALE82lzoL7CZXU6QxJF3Uj6QzzWN4Xss-YE79Gz6mvNgfLW3fkab4toLLN-he5N5CvoHxAbEuNXQLt0o5KqbDT19m2U_zlvmzSBHq3xpX2fnr4BCnlQRd84nod6K0375SyX1MXinFEqj3XK6QkoFNIsQ9LFEGBgrUT0yZbt_W_SaqLM8hhl2Nzj4sLiSZuHqaAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=lNU5cpc6TdmzGF4gcWZZv0DE1MkGyU7lO0dzwH127cdb3WOGJUkbbvYXwePTi0ySqkOOwdJFpJHThrPEJTo0nYu8sslYplDO5mr_hNvOsLYC8lERMb5oCo4oZqVL3AB_CUABgsdqkrgPOe6DV9ALE82lzoL7CZXU6QxJF3Uj6QzzWN4Xss-YE79Gz6mvNgfLW3fkab4toLLN-he5N5CvoHxAbEuNXQLt0o5KqbDT19m2U_zlvmzSBHq3xpX2fnr4BCnlQRd84nod6K0375SyX1MXinFEqj3XK6QkoFNIsQ9LFEGBgrUT0yZbt_W_SaqLM8hhl2Nzj4sLiSZuHqaAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvih2B-reTGsb-U_ckWgkDM8VlsFDDZFWbq6gJ9F5DEhb9rU4Fc21pBCeVxpSRB9LcRtVmRqkaqHFxes_tGZZy7W-Eh4Y9LQl1TC4tit12DY1tgSq9F86QBuXxU35BEOBlovphlXfj1NC85kEQJOx5W6gpDga_h3T6R2UmkIdokK3369Kc9Zamm24XFI_auPRFVwSXpK71STwadhmEbFe6OO4dlSYJcbgs7PyVRxVo4fVROKtj77WuTvgxcbQy9rl7IOK2XW_S4EFej8fQeeaxPvdJ8dGKdc1CI40GfMc7MTjdUCGfEeyG2kD2dN5AD40hp8fzEJ0L51Ore7CMC86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBInyDXdYAuAdbzcZJ3N_Dxfmyt55D8glygPBOuPGG_q-vuD4ZI3A28YFrqqrb8m_x5CKngoUCbFsz28iVV3Av997rKF3k_XXQO8F5QnBhaPG7dWHF6yPrrVHwIhM7o6BWzRtHzU5-GPTju5dyVlAebiTJ7-RQ4kZQeC3LSblecIU7DE_FPystNX4H5fvW_kzEv7tmuh925lULrcSy-Dz43KxymGB5ZFKLOnGqpm5clNeRhXuyMBbuoQO2ovM8y-MJHGE5Z3hAxBp6vPabKxs21NgW2q7l0id4qQvdyBnTHts0aoCNP2wvCdAJtB5vGESbpxNrQQ75fPw2FYLA0BQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=VDZQ0A32eDH17GDbDF2l4pUaN2Xy1Ur2OqhNGJ1nVa15vQEUqLWaP51eyGkzKLVKEpfS7OF4QJylVTS1H9xx2vgVw2BJPI7muWBvNbfzatikwMW5MIPGArBRy6NDYacw1ObytwjOzduoblmP4kOmsMuIzQRoD8RacRPpRdYOdP54sKN8yYubgJhLjgXlymKneLGZjGZkVTJSh1qfzPO4MnrK9mKd47r_9-cSgcNmewl4gXbCM56f1ZxgSBQ6x19iWILJR60E4GJWK6yOmzvX-RNNfu0AdJFXZUMXKCKc3Q1OSMW4wYEjSLAXTUpbSuo0diasw10kPB_Ch86VGCEMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=VDZQ0A32eDH17GDbDF2l4pUaN2Xy1Ur2OqhNGJ1nVa15vQEUqLWaP51eyGkzKLVKEpfS7OF4QJylVTS1H9xx2vgVw2BJPI7muWBvNbfzatikwMW5MIPGArBRy6NDYacw1ObytwjOzduoblmP4kOmsMuIzQRoD8RacRPpRdYOdP54sKN8yYubgJhLjgXlymKneLGZjGZkVTJSh1qfzPO4MnrK9mKd47r_9-cSgcNmewl4gXbCM56f1ZxgSBQ6x19iWILJR60E4GJWK6yOmzvX-RNNfu0AdJFXZUMXKCKc3Q1OSMW4wYEjSLAXTUpbSuo0diasw10kPB_Ch86VGCEMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpDtz99MfZX0yDVA-WGqIUFzn4EJYPzgfScTaT8S9cOF-CkL6y4YCG2AGPi4K8MigDXLAZcvtQpfeZ6oqlJgtcrI5rmH7HyNH-duhGidb-32urNAcbKnGOiQl0AjdkgQhinOPfKVAQqW9ybRsGBjFDuRMFy1fyZowHhEosDyg4xuuHlYeoXV-E61OccR_LqpDVcOdVrjH6TpQbYEGjwAJk30JCxwstyvWKeJn8_6GCLpv-HwMzoFiF32UN6n6Xd2iPtDXQy5z6qx-1u6QYCHsZoe4b2onVVtA3SxZi3IIH0mdViE7RK3P3UgObR8WRJb4NBB_sULcic8CVNM8kZTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=u2KPzfN5_dzw0n08el7Igl9suVw3kP29bFkYqaKPi5EmXlwO8OO2HZZ46bpPVLPXg4e3jb-z7jKB0WT5-tSBjd1xeeboz4RQBMWlh-ydVK5yKokp_qEcHEbuerXqw9PgIFcuX2eCYH-LOe-MPCIa4YTXGuqMhN-XndcjfAC20J9vyDwAlfDjsju20aKxg4mrDmqaQgXjxnIRX9_PaSkRn8zWMWbeM1HcZ_htiPbOvxjZG__ofCrinwytGa8x_cWVqMo1XWlAre3DAViKh54qrhuk8HYUgX0zZerdEpq7doRzTfspW04OPveu-7jc8PI9sxeXgrBJOJlxnR9aj0CmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=u2KPzfN5_dzw0n08el7Igl9suVw3kP29bFkYqaKPi5EmXlwO8OO2HZZ46bpPVLPXg4e3jb-z7jKB0WT5-tSBjd1xeeboz4RQBMWlh-ydVK5yKokp_qEcHEbuerXqw9PgIFcuX2eCYH-LOe-MPCIa4YTXGuqMhN-XndcjfAC20J9vyDwAlfDjsju20aKxg4mrDmqaQgXjxnIRX9_PaSkRn8zWMWbeM1HcZ_htiPbOvxjZG__ofCrinwytGa8x_cWVqMo1XWlAre3DAViKh54qrhuk8HYUgX0zZerdEpq7doRzTfspW04OPveu-7jc8PI9sxeXgrBJOJlxnR9aj0CmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29258">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=CpyS9uQa2qFzS0ziIJG2e0zjayr2gZP7mnJKLv_ojEtxaZWzFg24Ai2_AxaE9bmuEYeRB9tjLrjpLAeU2t70SV47YrYaCvdDqgyGG9vkWI3QPAX3uZFthK_vJvWsRhFhDenkEhxmVLoWUTo9OPb5Fv20hl1X31a0tKzBL7SJCF_7bdG0pb5Brelu6G5ERO7KO8j5_NtyCsV5l0SVhbe81KnqhzAsJdLhTzrgCfeWri8b4_SOMWl_cq_EPUGrls7lqMuaYr6LocI0Ar6gIeg80a31mxp5B35z-dflrWqsvKQw2lCX1QUBxXpfb95Dr5w7QYhvNDi15BgI74BtB_GrIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=CpyS9uQa2qFzS0ziIJG2e0zjayr2gZP7mnJKLv_ojEtxaZWzFg24Ai2_AxaE9bmuEYeRB9tjLrjpLAeU2t70SV47YrYaCvdDqgyGG9vkWI3QPAX3uZFthK_vJvWsRhFhDenkEhxmVLoWUTo9OPb5Fv20hl1X31a0tKzBL7SJCF_7bdG0pb5Brelu6G5ERO7KO8j5_NtyCsV5l0SVhbe81KnqhzAsJdLhTzrgCfeWri8b4_SOMWl_cq_EPUGrls7lqMuaYr6LocI0Ar6gIeg80a31mxp5B35z-dflrWqsvKQw2lCX1QUBxXpfb95Dr5w7QYhvNDi15BgI74BtB_GrIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ لیست‌بازیکنان پرسپولیس و ذوب آهن برای مسابقه‌امشب؛ بازگشت محمدحسین صادقی به لیست هیجده نفره و غیب ادامه دار دنیل گرا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29258" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=hNsFr1yuEKZIrnCvErmNJZjRFl90covb0q0VBw8ZeywC8uZOo9sT37nXZPkJ2xgXdgnWY1dnJOGtWhCXXCDtnkppA1y0y4-v7qsruyZA14ZDSC55jo6zRDp6Ddh4Ic845WinlzljDKSa3-xW7UeEhZ0PtxXHPYqyD7vWH77drhLU4xWV4jVHZft9U8Rlt5ZP6yPBQccw9gyJeeBuQeBAs-iV0B32-ci5_GcFe-CcUzNcBoU6woRuStKPTMd2OC3DnFXH9nocXFRmEx3V89WkOhS8oFlwPmi-YItpJV6MyZUm4lf_hR0MfKOkBnEdvdEOZQmKceFJf6_EDkfwGc9ycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=hNsFr1yuEKZIrnCvErmNJZjRFl90covb0q0VBw8ZeywC8uZOo9sT37nXZPkJ2xgXdgnWY1dnJOGtWhCXXCDtnkppA1y0y4-v7qsruyZA14ZDSC55jo6zRDp6Ddh4Ic845WinlzljDKSa3-xW7UeEhZ0PtxXHPYqyD7vWH77drhLU4xWV4jVHZft9U8Rlt5ZP6yPBQccw9gyJeeBuQeBAs-iV0B32-ci5_GcFe-CcUzNcBoU6woRuStKPTMd2OC3DnFXH9nocXFRmEx3V89WkOhS8oFlwPmi-YItpJV6MyZUm4lf_hR0MfKOkBnEdvdEOZQmKceFJf6_EDkfwGc9ycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYbauZEQqs_QPpJOc-2w3GAXEJXvX1aMffi9EavGOtVY4RqTFX0s7KlwVJgjH9e_j1iQtVRB60GmHQxI1L0nu0WhqzFc5QEEO6oAJg_vRzMYai-fLnINgE57JK9ZCxRoU8maiAE1OLQ2MssyhOlzIas2-CMwMU7uenX7Qg62pB5_tbiek5ljii7azO77QULkAVOcREnJVpwtxnvyxtID06CcOkRWtqtTawufK6VtAr_evp6WCasMzfCOJpXu5dAQsZGtqtbPGxlU-5CDihKf6-nzeY5o95vAgijDrf_QgQ7smSPqmhxm7u7jkCHD90zX98yL3heJYMg_rWuItXFA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=BarTOuYmmWgQKOMyomT1IQWByT_7aG1YlTXJ-5EFDzWrOOixH9SAw7H07cgK8ZS1MsudVr2E9mzJSxM2TdfJ9oco5C5BmF2siDtXOUZN5Ov9JeUiYeuqeZHQVIqmQKJeyvE9FEO6z3YB9_HD82K_byYT0h_1HcfwHRanCD8vK_ujIhTncmyAEAvNWjOxoZ4VXYbbM3o6_KQ-FRZjUnMo8b7l_if123YIIinu9CqTpkO2p2eQ48BohZN9Uk_THKIw9FGOnKTEZEykyKl7dK9eKCUokKx6NUuVND-lZ54EglCjO55Wox42yFG4rBkub74IpgEg64FD3mE5ge-Ywh0zbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=BarTOuYmmWgQKOMyomT1IQWByT_7aG1YlTXJ-5EFDzWrOOixH9SAw7H07cgK8ZS1MsudVr2E9mzJSxM2TdfJ9oco5C5BmF2siDtXOUZN5Ov9JeUiYeuqeZHQVIqmQKJeyvE9FEO6z3YB9_HD82K_byYT0h_1HcfwHRanCD8vK_ujIhTncmyAEAvNWjOxoZ4VXYbbM3o6_KQ-FRZjUnMo8b7l_if123YIIinu9CqTpkO2p2eQ48BohZN9Uk_THKIw9FGOnKTEZEykyKl7dK9eKCUokKx6NUuVND-lZ54EglCjO55Wox42yFG4rBkub74IpgEg64FD3mE5ge-Ywh0zbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=eG8NrpBKOHO-yL_Bp99UVWRpu9RubuX68Kj6otRdbevUhquOu97Tgdk4ZRVm_i2ITiahZnZFin0QowIbEqDR2gpIKhWmJ7Gk14tt90J0QIwlwKbgxTlYVt4wHIGClJWOQumz1LoHguNg95bed_01tpN_9CCqpNu4zgJ_MptJKSLWsLPaMaFTTWZMiLnZGWvOd5SV9tNe2IA2TaRWmKmc65r5tU0OOpmg7bh4_X6f_vFLBEc05VBfGpGaEhpmTwdk4_WtH8-_ADp3fn_6Xi9wJMZXMttbWJgN3vyxFTnT76GAN6bVXpqBIOV4TRGfiXJRHnoxrMD24FToJn6UffIcD5ZenO3GXke8AnEGuY6EoI7rjwRizgcWSOhoTyDXkvZ05BoH1xZwXJHWwgsDYFM1QqNuWXAPr5MXOlWTiym-tZQ48BOQrhR7xW7BhkCPMdsELK6tvdLOXPNEecdc-tJ2D0tag06n4HZeVm-KRdDqkmUAgqAXGn83h7edBYkH3sRF5SK8PFPLIQYbpmyDD2QhGWhmPfjm7xijYADgVNz76Dy--0xYl2CAWwFUREasj9eXktgmWD5QW9Dy9ZJ2P2nAr1CZSJBMaK7zfeVPAbwtoQG7RqZ3fW2pYR1mXXaR34Kk_PHkWQhogJbPfmlZlEvuyDwzStPl2t411zWO1EB4ZaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=eG8NrpBKOHO-yL_Bp99UVWRpu9RubuX68Kj6otRdbevUhquOu97Tgdk4ZRVm_i2ITiahZnZFin0QowIbEqDR2gpIKhWmJ7Gk14tt90J0QIwlwKbgxTlYVt4wHIGClJWOQumz1LoHguNg95bed_01tpN_9CCqpNu4zgJ_MptJKSLWsLPaMaFTTWZMiLnZGWvOd5SV9tNe2IA2TaRWmKmc65r5tU0OOpmg7bh4_X6f_vFLBEc05VBfGpGaEhpmTwdk4_WtH8-_ADp3fn_6Xi9wJMZXMttbWJgN3vyxFTnT76GAN6bVXpqBIOV4TRGfiXJRHnoxrMD24FToJn6UffIcD5ZenO3GXke8AnEGuY6EoI7rjwRizgcWSOhoTyDXkvZ05BoH1xZwXJHWwgsDYFM1QqNuWXAPr5MXOlWTiym-tZQ48BOQrhR7xW7BhkCPMdsELK6tvdLOXPNEecdc-tJ2D0tag06n4HZeVm-KRdDqkmUAgqAXGn83h7edBYkH3sRF5SK8PFPLIQYbpmyDD2QhGWhmPfjm7xijYADgVNz76Dy--0xYl2CAWwFUREasj9eXktgmWD5QW9Dy9ZJ2P2nAr1CZSJBMaK7zfeVPAbwtoQG7RqZ3fW2pYR1mXXaR34Kk_PHkWQhogJbPfmlZlEvuyDwzStPl2t411zWO1EB4ZaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29252">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_Qo-JjlDq1WRvozWyUvTxTv-vn1-8qcRhqYZYCPCT27SKNCyxrVSDOuWd5C2kQVcp36y5wHzMRtahJ14_7CEDalGPxSen1yfz0zwyw2s5eM69vPhtf9nQ25YGmkW0KhpHuUysSgnXvexj2jtjX0_pBbbLGyP6SPzrPFtSnWiiKzK_ub_7Y_0hW0CspwCbAw-5oxAFh5jSbCWhxVRJeLoLeSpEo_tr5aEyqTPsE8PkamALjpFm2MX17cQf-kg7JDhVtXSJPQETZmdrrM1bli_oW-55EIEb3rfyckFygCoArEhqq_Nybsi2a0JRNotjBrlxJYahWTVltsVIZB6S4yHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
اودینزه
🆚
لاتزیو
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29252" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwLpGJ-ztpr2kxp_VeRqbH7R8E_HydR6pkvV63trhfJcL_Fpl3XJKn1WwAYqybvBDdph48uMLMDzc5ftDmx5GvVJ-XEoU0n1-fkVNqnFwbUx-3skSbcyG5MXC6UWe_aoTb2ePpQGaQpBAV3TOMvsmIOos4G_96WDJ5FLdV8aGtA9S5sw_1VI79XXHKwbxaA3KeQsD-5b3VI5TkTnqBgnbiLAYa4PEHfUIV0ugtF98d1gUVzmKTh9FMxlIL8q6nndnfQm0oVTS589KANLWPSPHO2KFysHoR3MktYJVpzFzGoi5gfVv5fibXVEkV_WI9ZjHWHCGFcpNUH_pCmMM1KuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb3Snqtp-3kAT153FwHY1IG3S6TNEN_t_KyGmpVtFGMAHuEQ4gV0KMg28hkkWn3kanWgeiV6jkFQWrCjTXwqaJS-Alca3c9gYInGV7w05XU6ffzT7F_yZFS2PRDv8veSTDOjJs_FuAkJOOtdPJY1kRQb0d8oWDk1GRX4CM-1AGkH9JJZ6e-p8isPIpagBpAfzJaNKBZu8L3WYk9MVDV8jgRLbuMHtUx2LTTdguMcxYdmT9qQNDm9DNlTsrTjjNHM6MFRCJrFyweLcdCNjNwY4sYSdCs548JJXZqj6GrQNmjUFh3lWjWawKkq2ZIe33POz3ekjCSISX0WD95GedZRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_Dykf9feAoOkdRCxw4G2Cbr1gtMgQZSSFfGX0gwdF-8DFj8G8_Bkhj6p1fY6NAGgX7FnqSXcg1azaDjbMDJGTIpwqtS7vIb_O3019YDfHhM7uWtMiu59BXm5csxZ3bfjWizgURo5PGMz7llV8dlFBdPCe40ZhD0RSNuaDdjzJP-ysy-3uw15m5NHJGY6RjEmbjkP3KPxLpWbcnznpRlE5jviFSMm_kn1fncf4K6OpwHD39C18FQLiXgxrX6uiuMKhbPkYwgk9p_9OBXBNIAkjgk3K5fB6Np5avRWapqSBBOLamRNVq0s9tZ9DoMPbYt2Dv49lFsG7dJfZPQsmdbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QawrK6yhffAQupGx9dTiLIhaCSrBNWKSkmraflmMN-7mj3OcvTR3uQ7Fai6ZNzhZmr0-DhjErwx10Q3DrdNLpdi95Eu__ZVB8SMdLmrVDDOMepm8yyNTuE53yYfvnubxRLny8L9cvywQfF_kje-7IHiuYJmRHE5tG3nts5CYBN4gCw6Jfr8NK1hxehiB99kivcGro0GamL4YVhY3aGjbAxf_6CKwhhUGDHYDrYV13ym8TP4CyKDv3drwrSB1qKal9WpZyfqTNMe0YTHndE054CqrOi2gff9zQ6VkThYQa04g-pV71xZzsjc0mNwMJqg7OfbX3KDjRhIGhk5U0orYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=IcYgldedYIMWsBustN_mlbIq2y2-WHN5pFlsaiCGECIPvDVd9V-l5vmd_Eqswcw0pU2qHDSOtwU-qSuub6OIkZ9Hen9aQDvXuCDqo-_wJDnWwvEc33h2Y-0TVp_W9zXBZIBoRs-PbYmecEhgvu7YmZ3c-y7QFF7KCpvOg1A1-EEjNoktyx-Zcew1uNEO8z6MrVTkCzzmCtj58kjE9Vqym3VFDCaeEC4b1ZirK0cdyd34xoZVPe5rQy6woWwLLuIJ5lTHG-zPQBFVub_MsG6xEHgn77sbyLLcaJgE8ltKvJ613e2uNZqSpk-TqYvjcNTlLFjRV59fpEYYvdWDzrhEbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=IcYgldedYIMWsBustN_mlbIq2y2-WHN5pFlsaiCGECIPvDVd9V-l5vmd_Eqswcw0pU2qHDSOtwU-qSuub6OIkZ9Hen9aQDvXuCDqo-_wJDnWwvEc33h2Y-0TVp_W9zXBZIBoRs-PbYmecEhgvu7YmZ3c-y7QFF7KCpvOg1A1-EEjNoktyx-Zcew1uNEO8z6MrVTkCzzmCtj58kjE9Vqym3VFDCaeEC4b1ZirK0cdyd34xoZVPe5rQy6woWwLLuIJ5lTHG-zPQBFVub_MsG6xEHgn77sbyLLcaJgE8ltKvJ613e2uNZqSpk-TqYvjcNTlLFjRV59fpEYYvdWDzrhEbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtXVqT9pRhQbD_C1Q_lF12CwI4BSM-I6skRbrYxPj_nqWTfoQ6LCL8QzehO98EDJDOxeSD9nzMtXYMh9wqqqBZcLoOhfoH_wkP11nWcRjQ6Qz34jBQqcQCeryB0ilxfXVQh1vBNRJimwe310ug_3b0Dp4hZF2rDBGwqWFI3LNMWFScdfgDaLt7wpMvWqYBB7f9C2nxm--3QPOvgn_vo62MGJi1d9x3m6bbatBKHx5W4A2JnOMmngDL4ZRoz2KaXY3qDcyBTdEyzGGQkJH4NNR2mB2LsKbiXMGDLfD5Q0Tx458iWhjae4-WI0-SOfZ94vgtX2X0trdVdAKSrX-RtpgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=phQlYRe61Dy8bi6WOiW6L_L0h2APckILhz3B6y97YZb-rWChPkq1vvvYqMUAzdCIQJJnzCa6fSuKdHc4XODFBuVFVLv8QU8JgIgkEFchZj5TwfOqIcH4TTF1_sjf0IirSrCwDvc0u6q-cLpHZnQXW0Hsi5mHtW_xVOCsRdrOYbi8I8TCbrIQ2N3mg2sgjILdoLqgO2-RpC9vPIZRDRAFtbMwkSmvx_hbO5MO_fLJxO0mqXKiAKYyZQKWhq9Orf8JQQg9lFzrKxvQxN7EKiZXzWxK3Y1K2898YyxPf1HIipBBTEuZkiS12QFJduAZHlRrZwQ06rIrp0cphTuQeD-e_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=phQlYRe61Dy8bi6WOiW6L_L0h2APckILhz3B6y97YZb-rWChPkq1vvvYqMUAzdCIQJJnzCa6fSuKdHc4XODFBuVFVLv8QU8JgIgkEFchZj5TwfOqIcH4TTF1_sjf0IirSrCwDvc0u6q-cLpHZnQXW0Hsi5mHtW_xVOCsRdrOYbi8I8TCbrIQ2N3mg2sgjILdoLqgO2-RpC9vPIZRDRAFtbMwkSmvx_hbO5MO_fLJxO0mqXKiAKYyZQKWhq9Orf8JQQg9lFzrKxvQxN7EKiZXzWxK3Y1K2898YyxPf1HIipBBTEuZkiS12QFJduAZHlRrZwQ06rIrp0cphTuQeD-e_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNO8DBF9jYVSiaHXyzXKZU1toQOv8cjzKf0tN9cbC0xOLFAMeBLfmG23ZP9WmGik1P3fqdpkjhFVq5_juKZp-w5JeVsYQ3Wrnx_y1GEm0xA0pvzyZDW47WdER_QaH4xdPaNQ05XPdZ5IZhZ-GUOLapTdpfnvMHC3dhXxnzSCvhHzeD8wmG4uyEWeU8VCmV_Tv0g0b3048OkDNUW2opHM-SckUvIsKkDOmaZP8xde_aylWgh03vyXRWgIlpXj-DD_6gsdKPxgT-Z_mIlHB8msKuO-CWuJjkWp8iI8UWSTtT-qbb2EiQrofF3lW5DxbvbTYBeZdu7bYy3UcymMAZ_dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOpmtHmQRi4_5cCB1zkDw38SovY0q3dsliWiZ0WgCPhRqLTasTA8PZMxRAyBNrrZJkmdqpTmRhvQoDeJi3x9K3x1joVA0e7p26yN6d0KdEm2nvQM9BZJJ9wij9Ni0NFx8KPwFcxvVIUHd19Ic1Z_C7cTysup8cTXsJfB6cAYYBxuT8LLJCD1C4OoT2sD7-HK1KX202ZrGIH3es-2-TPdcAbRfoINvcerCgrZwbblQZRhIQBsw-YKs-rHQmUxSOWUj9yV1yVsHtAOe86k6jfLjs3cGevBySmIfE-qul56n5A9moRznzlUph3OVuTfJO0c-gAVKeb64C3JZp0dO56GYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-Az4rIlmRuk26P54PF3ZkhqPOH2v9iJEmsSVKbdm4Ut1RZJ3kvB8GQzRXg-1bD_Vq4aALmwI32lRTdwkraDGC99_g9l50RCiHBm0xB5sKj9QGfQdH8ltFKvaRyLqHppA0vkhcS2-s_LJWG3-EO4uaTBRATfYCrbdFFhHpSFQUm7lNz2h5njHKPLfKP9T2nK4XdDpZfGbcZblhh9ezAll-muuXoSlwPtdU-N8oj0m0G0DgvUkMI8lZ2d0ZXI2b9Caa32sJA2dBP4QgTprjNxYJJPapkyPq6tTzSJYC4c3pecYLZjS0cbFJv2QlVrYU20asv3yMhnJhigbekA4PyINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=gkbNA6lf7ChAzaH7P2IgEDJVkieLIRFIyEStqvl1W-Rx-YBwtOjv_D6MiYvtxgXHp2anJW4IzlCvwIKxmGEVRrtn_01hozFONBYmJFmA6DT2ln4NlTmAgjJFhKXBneQefKnM8Sex2qPWYzwn2V4lszs7dSkt53i0f_ZAntOkG-FQkbcWjzQerGi1rXMCDRHjtNe9v_OZLfM9nVppuqlEG1rlVv3DaCFALsofJWrZXdFGffHmYsgRnK-y1jGkJOEEbSEj79SoEOzCk73APFypW5BTksLRlVa0Ng4MIUnVCXWY9zUF8RdAyStiHfAyjcMgapGE0B8b9JFmQ9-K9cRk6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=gkbNA6lf7ChAzaH7P2IgEDJVkieLIRFIyEStqvl1W-Rx-YBwtOjv_D6MiYvtxgXHp2anJW4IzlCvwIKxmGEVRrtn_01hozFONBYmJFmA6DT2ln4NlTmAgjJFhKXBneQefKnM8Sex2qPWYzwn2V4lszs7dSkt53i0f_ZAntOkG-FQkbcWjzQerGi1rXMCDRHjtNe9v_OZLfM9nVppuqlEG1rlVv3DaCFALsofJWrZXdFGffHmYsgRnK-y1jGkJOEEbSEj79SoEOzCk73APFypW5BTksLRlVa0Ng4MIUnVCXWY9zUF8RdAyStiHfAyjcMgapGE0B8b9JFmQ9-K9cRk6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwwRaBj8SoZf0B9wYWxwQL4hTzGKlzLI5Jf9Ft9Dt6ZEbwasbO0D3NZ63uDkYP56Svc07q6MYs_lJSefOu-yrW2Y2DW7lK8peLJS7NquXfIJ24oJQzZziS3D8uW5NshRjYSAhV9jw_3ZT2peU1N0khmrrCay7M0lKIg8Xb-Z0IskuiFYSnW8JUbvZhVFQxfHIqdWiZYM-cietTrzYbyiRzeNN8AfJV-5UPpbIaQbe5aEvh5cTE2eJOmCpFAAPfmQYc1H44uoGGdURJ-tLCcDIY3YCLbN-iL2Jr3o_cqOdgM3DIP6gdPYxeAHLw0Vd5fdizgKr596CnPV657yo2JDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtEDTfSq62YYrUDBMtFf06Q_zIsDVDLAZDbNzuP8jMkRg7BSHUhY7LD7QJLCSkBRP1IW9P5EBcD3erS7fbYHMxLLwkTKTVAxdZ-W8GC1c1bXondO_f07b4W2FpdM9VnjV7tJ8jHgfRliKsDj2zuN75GbwVwS04Dj4PycNbAIncrAK-FjiQTHPbE0yEj3ArvJENRxl3Pz2rp_dCfW3FF63HCHLBY8phmT-jQI-0JDn3FyQOvVhN7nCbrvqGO-Qha5qBERvj6bS9B2eYlPBDC7Vb7crno5mSSdcTIqvP123TfM_ji5DRGYhAR1ay5FG1jdcflxY7B7P-wvIU4k-KKywg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29238">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Diat4pFMwmVq9Y9p9DCzf0XMRW8n5kKubh21b1zVifdJaaxPMNsvoYxn1sCdmb5VUwHmm1bj9QbrgGoP9nFTVeENE-lYRyA2VQPCXy0WvHxIFdkdp6WQAEcynsYPLIyCyn94f7AMPktoba_dmgGa52onm5EdBR8h70tunqKXXJ0Alo9y25-popRuXMjsxrJ3eZa0haimJJwyc2VkDs2BD-qnnYKJaUqUnxbuejvItpfWhLelWk6BNRcB1iZ2wG_s9ou9n3_WJGhX9WUs47KdZWjnviIbjlKbuMswd5FvCj1FGmjIHzHui2SdYCHg4UYFkZELSSW2ocVevofH_P4pYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریهTYC اسپورت خبرگزاری معتبر آرژانتین: لیونل مسی و رونالدو به‌مسابقه خداحافظی کارلوس توز دعوت‌شدند و ممکنه باهم‌همتیمی بشن! فکر کنم این‌آرزوی تمام هوادارای فوتبال جهانه که یک بار هم شده دوتا گوت تاریخ فوتبال رو تو یه تیم ببینیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29238" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29237">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zye7FcIr3rUPdG_u869JttT-v40a8GAWfl3SDkNwAI3LXP0s4mvJg_eFGlTvp2m5jRlQZWpvaOjtQYJhUmAqZV2mvsryfezCl1qCIABsARzC19WL5fEbYXTy79f5Rpa9EyBEn0YENXsE9LUkSoQwyDmuesk7IGP3g2ZmSEUpz7njp27d6stwtsrQADG6h0YytXCL2UwDyxh8djSGpv7abK8p73RKInKvx3pYcO9bnsaLfpOCbbYrhORW6npAJICpBBx4uEfPpBhkPQ9cpdtBE_BGKqDX8ZBb3uAzO406TDk24URjpR0YmsoqJPbOLNqpO1ZV_rq6ZoXYPAB4t8TgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29237" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXMMoXcpk3GvqKFyR3OEAKAlgvraaoAOUFVi0e-Nd0IZO9ShDE7CkIBNsHPmf9rkrhIDl9DuYDKeCMTs6QkDb_n-4m_YWSFX4F6ePxHZrI6_IxhwUgl6u4fAFphxhKkU8QW1ydc3SeSZyfXj5_rKlnwj6taMhC5yxnEa6W_kAlDvOabP7nUYj-v4g1XfLFip4hLA-KiDMTxa0GTCeLuj4Cyl2qYdQnnXGfCG2qH0DEwfSRMlqcMYt_qGuCo5L7GyhTRAo9ZJg08y2s-oTYMI1WSCkVFDCLbCgzWhWIygj1R_WEvY-WnZPKq_1dEcErcUOxEE-z2ADe5DcjaGmLeX1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fit0U1ojTU4IisPkGOl6EclA3p1zwNAUsZXpsWQDca54gOcwuA78x7F6FNf1sJihgMwo943a9GzM6PpKhn9U8YVBkfpi8j3C62m2TtFrHSp7bOxL7YBiPyj_rXTa_Qmm5HAi_e7Lfeo8NI4bLRZNGVEIOtagJf0VBwWCX0-kJ5UVW-rxogW9-sDoSSTK2t9Goj2E2U7bzztpeFDUwx-A-_on1-79Kr54k4KG8q3p4vyq2vXC5V3SK1046vOLSNYu3Q5xCCIrYTu689JZDqdtHMoGhpY-z4cXhFney6XYA_zip1_BK-ySWrQMFiBNQJEkGkVEH_eEIH6Om3yVozLkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogXwFz9V2PDtRIxhFZkB0Di1Ayjk3JqGkvc11lUyzxF7nQp2ibJAoAh2LS7_iu0al8ZoWOm_8CfOIUAagCbx2OkFI8ljcq5mI0001mKCgBGd30Q2zQUTs28i2wl66GcHtrXlF5PHsjsBOKBpoxNDIdykjXHSKnY9tNL2KmB_M0FdrBjeMne_5RjAtjA3ETlGDQARWTfxYBsi9WwObyBWtv7mzsojHrhbsVhydRj38g3XopVEYenwjLW0M86u27THZld1Z3AUF7CSIbr3a212lFYZ53bzNibAYTLifF7RCu_KtEcCVdlgs8F7b1XuumJ9BOkjG-l9zpb4PN0Tr37Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTAE-2AKW2aCt22g6JLXO75BnBGO7cAEOT71BWtHGJacBNlyvOefNUKgYzw_CVgtl2itSEY-iomk7Jd8a3g7v5TDAHmLHovtwWzUA7Ytqn3O-ZSA4n3cIEjeI9SBKvpq-ehONfcy6drvX4sIt2lUdjSNqYXL2xUe-oKBluQagNhKK5GBPhEyArxUUy-VtClZAHagfSYWROVFm6AOnn8C561-RuAEWbWEbKzRfOl5zwwGvGtMsnu8P4W9lCkrKILJv5aidrcy0mgLDpSgZHxCTYJnVceXl02xJdnSp_kXicEKr0Vc8Iy9LsEtDD-LAEvdBm5hs84MddYgnpWY8d-sjGDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTAE-2AKW2aCt22g6JLXO75BnBGO7cAEOT71BWtHGJacBNlyvOefNUKgYzw_CVgtl2itSEY-iomk7Jd8a3g7v5TDAHmLHovtwWzUA7Ytqn3O-ZSA4n3cIEjeI9SBKvpq-ehONfcy6drvX4sIt2lUdjSNqYXL2xUe-oKBluQagNhKK5GBPhEyArxUUy-VtClZAHagfSYWROVFm6AOnn8C561-RuAEWbWEbKzRfOl5zwwGvGtMsnu8P4W9lCkrKILJv5aidrcy0mgLDpSgZHxCTYJnVceXl02xJdnSp_kXicEKr0Vc8Iy9LsEtDD-LAEvdBm5hs84MddYgnpWY8d-sjGDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmtVbRhfdldsst71PkYBcgvLgcHfWF3kQqglHXe0VCpyKjoE7asLXbhWblGXlrm3_XCw_lYmv1DlhzkU8YVHBGGXl0ocWP-d8nOkQ_-_JA3GXCX8rAB67Qb-LxpSfva-Y2b_7YXwZO_xIFI4SzkBMWvTyK0ai6x6wc1FO4t-5o58hG5EHyvEb1GGBRRtoyW94T0Kqqq6KKy_T932NFNfoV77g5p3eeo5QSAGbclq3BQrprRiFhTozM-CtU9n5I7gKVybMnbmERojEe5g-oupBZcQ1QuckXYbNN_tSDt2HZyH2Jx0ndZfo_48KGZXiQmcVR5GCn3S7dG8UD_HqB-0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXjtdzNJUq4FCLEJGCnhug2ooDXqrYGY6gSU9eY0rd_Vk2RkATJBYVexoLThIQEn3xdQLLiVLteM9XPwhJdY-6-fmJ53oxUuLSGo0JxMJEYZz5y8CkvJP2khX7jFGxQTUVE_enyC2QfqAj5kRYVXB3e3Fl7ZzhCGm1w5XN9Yx4Be_RBj80Glo_wQzxE2UqkEHBlvgmrCmlcRR7_MckZkdb4cgo5eEZuwCvSWSl4y-WvfP66SKBPSXkzzuqnAkqbeAv1euUItJYrOjutOpX1AkLI1ykaUSYxrq-b2gM9fjwCVLVTObBu2EMyrGNc6Nqtcl_mAN3Jl_VOi20p9frTV_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29229">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sugz-Tt1McNBOM72wZ23QhZd7nFGKmo9RClaMW0lIgvW5dPzrqC4JsdxwUeWlbgqhOsqzEA40_nzecitKPF-S4z7mO4XKoZz6tiYZ2R207fS2Q4LuuwpCuE4TCmEYkD0p6Kzo4VXs8WJR7SCmebprbcSPg-OvC-PaCOsI_vcEaX42laW-b3atWNpKZB7IeedVrxGbLJ0xYcggHXAMIZ9yOVKymSSP_Jvyj4TqfdHO-TWf07a8QhKS_KLFgWmXSN-U8QsfnpyFlbqJnh6eOZKWJltA2zEo6E9hoQiPYJU2dIz8ZFG7mOSGY5LrsPLGbkDlqXYi7FT7jmDtDzX92Zi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29229" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29228">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUEPZQoCaFJ18xluQG_BWrBxbReMhhtYFPOvtUfQfwSxUHi57BaCMNEdZQu9XHQ4Pua9JHstPHWRlKKwcRzcNuyFS5ugBp8K1fhM_P55ZEQZNRWAYBQBFgZCipVQOMEQjVsxl9qu8cfpGwoHmvxBSkWegHMiC9FJx4MBzzm369LhEGfrCOdcUCAeBQ7MX_VPj5bQka6p3bsZq4Xx9HvMxIx-M6AtqrMKs0FLtivfBSAbspInye5zKN8ggA-k6QSmSyWr51FT1437Wb1XteccSkb1zgyyidrvZJTJgZ7gGeqpKX8A-8qjpZo70c1uMihhupG0zocL6wmppM5u_Y_V9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
آخرین برد ذوب‌آهن‌مقابل‌پرسپولیس به هفته ۲۸ لیگ ۱۹ برمی‌گردد و این تیم در ۱۹ بازی قبلی خود با سرخپوشان تنها ۲ بار پیروز شده. از آخرین پیروزی عبدالله ویسی برابر پرسپولیس هم ۱۱ سال می‌گذرد و این سرمربی با ۱۱شکست‌مقابل‌پرسپولیس در لیگ برتر از هیچ تیمی به این…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29228" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29226" target="_blank">📅 11:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_B61OAzsfUg01WYLklP3M8Fwf4AQ2S35K8aqKI5N7PnlSoAmakYYB_zsPB27wc_H8EfKVkV_fzisjZoms1q40rjTD4ghocoRzTIgdzhvgQdBUsFbL11dikrJTgmoy2rhHLl3nMNeVoMfIQcKZ1s5HvL9EjHWr63VuoXuGNhnlNPvGTc3oI612J6izU2tUqSqkl3TP6QmWRVMeeHCFfYv8Km3ChDoX-YtCiehEqn8e7six_jueMYuHLNhaSjpLUGlf6c3JFxMR6m3-doBnxpM-L9oaSxV4b3weFmL-cmhBNMpF2nVNitD1SgFLk5a_3Q62T_NkKoY_kftv6GP685MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خب‌رسمی‌شد؛ ازساعت 12 فرداشب به بعد بنزین لیتری 10 هزار تومان به مردم فروخته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29225" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29224">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxm2Z_aT-9OTDgT6qbyXhFu78IUHhZpQUoRdhn8dJEV63VVXFXgJC_OGgZkLooylm8hsRpF814d_HJGeL36R1mFMw4hs-d4kyUeYtOByV_v46UjR2Fl5T5W-1JlA8DSuXkc7g0avT9kTYLKCcY8FvAYrv9WX2kpqkkGZhpdouj3I0qLM7wR_psiqVTZl8uUg3nN6AX19WbSWdw0vPjXpf4FMD1h2ICIlm7r8ksB9EKmhJYFdiYIP-lg_HKi-B--9LyGMr9HTxwspquMtT7HxH0lx2TVyq91mT8dYQ7PyZAREEjo17LjCw--BXF0d7tNSyHB4jHyUmtwyi1cNGIpTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌بازیکنان‌حال‌حاضر فوتبال جهان بر اساس جدیدترین‌آپدیت سایت ترانسفر مارکت. لامین یامال و ارلینگ هالند همچنان با ارزشمندترینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29224" target="_blank">📅 11:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTddtp7OEFXd4n3Dq6GV-CeChGLayHKCVpcpfi8M99Me1FZAAeP-MP2P70RRnbF_gsQt5ao2ge_HuX8k3QXpUK-8TCjEhTSkbxuVp_UG_kZXB6j57h9Oq7jwqJF9v-6FIbHuFPOrnyskGPcRS_GJCCi7hRS3sBvFNwCerCa1orvIyIbLK7sp02SCv_8EyBKEdH9GgGa_YVhKGtsrOONfIFVhRJ0YKuiEJYzLAdQqoyL8_VU8dVuQdRqVa4EZYgEikkrnnl7maos1qNQnRxpyrOZ2fEQltds5Xf8L7PEdW5zzMexImPWu_3ql9cUJ6FUKS7rKkYRDRVD_yClbY3AOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اردوی تیم‌ملی امید به دلیل کمبود بازیکن لغو شد و شهرآبادی، لطیفی‌فر و ایری سه بازیکن پرسپولیس، محبی بازیکن خیبر و صحرایی بازیکن گل گهر که تنها نفرات حاضر در اردو بودند به تیم‌های خود بازگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29223" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqb1MSNtjPLfrwNQ4E7sbRiNZ5cpgaKH-fwrmK2B3IO91Ixzebp3LeHGGeEpC8tn4cthMi9Jb_6fIXgxKLZc2-lFVDnibjIfGezGyGt0ZxazQob8xaMF8Ca4GWfGcJ0NgFGUM3RZdX7kM8gLCWvG_cXtU-nEuZP_a6CCVS8hdND9kTJvv45v8pRclB7kF_3MypKuVgsIi_29h2qCLj5_OmeJughnpDJ-lWBeLFwVMYFrjgi7E8gQjvhgPiOzOpe6ZoGyJJC4dmrLR_rtcPhnWZ3JTuYi0IR5AG1LCid5xaEXpwVcgw2pj0TBpFfV8PvOP8nkdYkCNHJGYVForBY3AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29222" target="_blank">📅 10:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkyQoVm_CcW2LH94uxU2skvetVF391XWpOexYNI6bhr-4AAiyHKTLMMYLoE_cJTtHgpoUAsu8_6mm_miAWiuRJMogGiGIrpUAaLfZXug3Gp9b4YVY_DRVvAmHJAm8ra-QpLx6H0BZboZ7TLcYrHrnyjnyDbEQM7nC36sRGxSxQQACGJ78ANBxpDkWGPJT0S8HaqN4aAJ8IY10INDa3TvrdQ7VEh2phsAZAIJiUFn04KBOVqZEwkaospQX8p_TpHimxqNUW6hn9Osgqozog2HW0zoBASAdoF42VXFOSsrxFwro0E4U9HMxgY59vMRtvY-XgDMYYipvmQAOyq0nzJDAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4Ot-hF1nOCERRQcex5ZT48ONLz7pD-DMPz6aIQuNxePRMV7iOybedsArTYai6yxl-fuldUqx93eH_o0Hyt2FQplZgHf3q2Ie9dCwsg7spXwUJywH8xGmKzbu0wn9QBzVVY_lR3XudIBK-AhJTBPcugCZyqC7khExqzbBrzjW_gonFKhfK-rVdKAt9p6I5LPBnQm2eZpWCQzZdbiepPJs3LeYlI5rNurOLLBtjLrXjsOJB5E4HfkqzlNuyV8tCdJrCeGmdV3w5oThE01vmPXslofhUfnlwlKPrLnMA_tXc1PVusJH-QphF2tfbIFKiQvHHQT3RZ9JLZmImhwJhx5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXWNRDs37qS1FOxZ-DUovVBtQSWF7fxyLDcPcIKtDi_NLx9HVQ71NuKeTYHU2VXJd-TzgDqIn6309XR1NpIAQIO2VWlKz2BVqoGobwc5xodB5QSPggdJx1WGKJEEFAG64yVN8N0HOO0WfvNbrZ3wUCd-n3xdWDqs1DjUqr0qeK1fRehaODnTxNV293BXuFEyOAEii_zM02b3g4NNGsYDJVxTc-ERvp39l3Xfv4Rm2aNI84vmbDP0Hjl17NAF4Vhalp2Mya8m3i3A_jm1z_Y-gvBpFvbPC0cwjfML8rBLCg7YvEF13EOkveonEPV1JwofbOdMyoQeMJmT-GRuvo229g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
