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
<img src="https://cdn5.telesco.pe/file/ATROMVnxPMC5NtpmvHo4fvTSBY27R_jgdJyJxdRwHbjyGUIcdzJTyQS2d8yfyU5wdgM-ur0Ny5X4w9Oa_xzB79xZTE1umRa3Mezmo5wJo-9q-cLWkXr9pG8RtAAWtUVrnSDwye1D7tTFz0qS2LxQ6Q49d2AqYCNS0Lgn6vDGhje3vY6AsbnWTrMTvquWbMwCn5_XDQgleoZy1P04-3YTsFZZnJQkybScxHjrRLTju098meOPOQo7clwLBU5j9p-g5u7MLpr22ltQfydPUUcwvzjVWdgNMfOJOK9KCJE2DL2vii1G_dvBZ_WZHnV7Nf1jny7uP3lDrkokqL5QPMG0RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 585K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 11:40:09</div>
<hr>

<div class="tg-post" id="msg-99909">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsgsfH3E8fY8Gr8aNzHi3KKgtHCSDGd0upnsVcJ9BhgkcmPZKBvbcS9Ho9_UU2pqUoUbbrqtj80h3fbKUTMq28pZuwXme3gQU4EUDt919Kzh2E6hjWx3Q7XGqS8-i8N0FIW9dM__XWGAEWiL_g6qUFA210fZtABdB2dUlQAOA9nao1j-nVkhKzZGtCLkkvdZGpqNeIF6ksqBeG_y91kllvxvo6QMiCbV9o8UAhWIZRX4c67S0-TOncFo9XsyTCAToAjfwkeeUvXL8_zIfQvtkQIsNRloSGmZLKKEscPVr40Z7HzIBMd-Pa8r_N_cboWz1kOeTAK_FgSN6xtmyN00mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😐
🔵
نامه محمد شریعتمداری مدیرعامل هلدینگ‌ خلیج‌ فارس و مالک استقلال به عزرائیل:
ممنون که جان سناتور امریکایی لیندسی گراهام را گرفتی اما گله دارم که چرا صبر نکردی ما خودمان سراغش برویم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/99909" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99908">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=eZb-OtcScw2zHMx2rEM-Cv1xeAMfzB-puNDT_Cg3UVJUmUnetBUbiB104_NRi024lRY5wtVC2lLedSUEUaHsFj0PPKvKC2DgoZJzp4t-l6tGj5ZlzclSK76deLceXNT3UkvJYd7mV3LIpEr1qx5GuxBksX_1Ox5FKBi-WQBLaI5SrOFI23xSSAR9OTOjGlP2vBKIjVKwQJDQcd_t_ivZgIl7Mkg7A3YuuijybSaRmv_WLJ_6vwrYtLoWEEZsFfiVReuDgdjldgz4QHIXPSydBl1BRRehrkEjOR2_SbD-yFhVZk0O4ZGqF728fxxP4eU2WW29gAru8G-FYhDxksIgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5142dd144e.mp4?token=eZb-OtcScw2zHMx2rEM-Cv1xeAMfzB-puNDT_Cg3UVJUmUnetBUbiB104_NRi024lRY5wtVC2lLedSUEUaHsFj0PPKvKC2DgoZJzp4t-l6tGj5ZlzclSK76deLceXNT3UkvJYd7mV3LIpEr1qx5GuxBksX_1Ox5FKBi-WQBLaI5SrOFI23xSSAR9OTOjGlP2vBKIjVKwQJDQcd_t_ivZgIl7Mkg7A3YuuijybSaRmv_WLJ_6vwrYtLoWEEZsFfiVReuDgdjldgz4QHIXPSydBl1BRRehrkEjOR2_SbD-yFhVZk0O4ZGqF728fxxP4eU2WW29gAru8G-FYhDxksIgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏆
🇩🇪
سال 2014 درچنین‌روزی؛ آلمان با گل «ماریو گوتزه» در وقت‌های اضافه مقابل آرژانتین به پیروزی رسید و برای چهارمین‌بار فاتح جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/99908" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99907">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNeQVsFCGTE_IOaTJPe8BRgp9lD0iv5Vzm78rbLPPpnXCYvIBT4OVyI6vgbDec1OaBu194VrgXTKsqlMtLmf1ZVEr1Jd_2-ecfiRgSPYWEizNmLeOfaeRfUQNtOgDwDL7rR6K28qAK30s993UJGIo-sxM2_6aoCwq0Z1goMyERqyd60cSjiyQeG6pQLE2DuIs_MaZLZtWUV_sdFTJXnjWdYzkaZOgoocr_ABpY7ccopJpnzqAC15aXvbtm5hHWgGprWXZSGB1SS0-SWWD5cj--8CMFsSrlHHn7bWU18KE-3uNdjblS-jlSgGZOBSzSK7T7VW7xCYnZDP72JQJMqEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لامین یامال بعد از اینکه سال‌ها 18 سالش بود بالاخره امروز 19 سالش شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/99907" target="_blank">📅 11:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99906">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724b974651.mp4?token=ABd-XAgSmzn2O1nLXvcMc_8TSTKf_DrxUMYt1B27euHEKoCkmoowUdJ4e-LtHCUnOq0iD4wn1eSk05eFYD3xDM4RL9zmbKj-SVtKIl7uGQUz3nanUoJo1JXn_lsZ1FYp5M9pEBDgnzkmXyCwLvfdA1R_iBq90VFKEqbSCFAa5tarVV9ym_FGCK3288jG_gqQIhZ_weZmCV6t0mKAlypCif-T_9AC3tpsmdL_ZXvh3tXzffbQfF9njcrJlSXPnsO6aKQBaL3sZg_VXr2haD88gH0MSEC8-YYCjtKKnzEN3jTqAKLz1msDroZhfoxF9XqZpwn7nSgvq1B_TZj3CFNk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724b974651.mp4?token=ABd-XAgSmzn2O1nLXvcMc_8TSTKf_DrxUMYt1B27euHEKoCkmoowUdJ4e-LtHCUnOq0iD4wn1eSk05eFYD3xDM4RL9zmbKj-SVtKIl7uGQUz3nanUoJo1JXn_lsZ1FYp5M9pEBDgnzkmXyCwLvfdA1R_iBq90VFKEqbSCFAa5tarVV9ym_FGCK3288jG_gqQIhZ_weZmCV6t0mKAlypCif-T_9AC3tpsmdL_ZXvh3tXzffbQfF9njcrJlSXPnsO6aKQBaL3sZg_VXr2haD88gH0MSEC8-YYCjtKKnzEN3jTqAKLz1msDroZhfoxF9XqZpwn7nSgvq1B_TZj3CFNk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید وقتی میخواد از مصدومیت بگه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/99906" target="_blank">📅 11:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99905">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQLQz7t4rlzAubz99pGUx1XMlZeZmK_DtdzGEj89RQwhVnVlgxEdup7SBIqumsAAncqYESv9-OWsZjzCW3KyWOSRCf1nVV8oXb8vfR3X5ac_4V_MKF7Y5DvgY_lzQcdgyshD7vsqJEAh3gl30ktZHC_up8S0jSmXn6VblWV3u95lrNwj35XCZo-ANHXCbyFestDJd7OrFy9VmDyTuC5debQN9HV6yAFAm9Gi3utMbI904Cbq8C9hjxlCvP0HQ6XB7EHBW_CV4_nhW5dZXt8vCLp1YPQ6jT9nuQuLb0AGU32xHkNTu8N7ybOUQUxSh5bCtluG-NBTZICnjQk2eORC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇫🇷
🇪🇸
استوری گاوی قبل بازی با فرانسه:
اونا نمیتونن شکست مون بدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/99905" target="_blank">📅 11:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahnvmazHVPX3VIeRs6xyHP8NnC1O47mBFPwKHxn464PgAciB9N-tqJ0NBJixhdU_btwgGb21BK3AY8kAchewtM7NIUoTS_k9QrK5dPA0mOZ2wrVlDZEkL9MNCM0XKZNVHTBIdvDxlp87eZt8UXuHt3LJ0n85L6yKDPpJFI8mzWi0G4DAhvd1v2D90ROfY8epMeQSeoDnK06S87tmo6ZG5dqYYDNPnL--DY8iUh4oa7Elj12paEehhEOY0ch-3hbDIYTNrskDoM7cEJpGZXFQ46pIYUy_nTrweRNdqgBPkdwC2mBdaHkXEH622oRSkIxvB9zGgVcCQEUX5_uCXTSQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
نیکولو شیرا:
پاتریک ویرا کاندیدای سرمربیگری تیم ملی سنگال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/99904" target="_blank">📅 10:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=elBTL3Vns8aQghaiyO7Ktq4g7_OrE-MTL-1cYzLbzp-oL4DVBgNn9gBqvOWdYW6VewvghiG9IY_tHw82jvvA8flOsoe4Zc1V6g_mc7YbFr4Jn_7eaQ3vW-RECnxuvzExBUkcHV0-HZ79UMTDsj58kHXi4YL7RC4FCZ-PM5DqJ7MSo-QcvV5nW4z14IfHoiFQnMTIQ4ZYgRfGH4EI1tUeIdGtP7IOkdXfc1V6Oxi7NcM6Hfudw0IFY8VbSZGG809iKUGecfQn_yP65qkf9YEQneT9QVPwYbMwD20SMcy78GR6quwThCzOp6R6ZrEf3jbuVittGwrW8Vhm4caegrscDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e42b519e.mp4?token=elBTL3Vns8aQghaiyO7Ktq4g7_OrE-MTL-1cYzLbzp-oL4DVBgNn9gBqvOWdYW6VewvghiG9IY_tHw82jvvA8flOsoe4Zc1V6g_mc7YbFr4Jn_7eaQ3vW-RECnxuvzExBUkcHV0-HZ79UMTDsj58kHXi4YL7RC4FCZ-PM5DqJ7MSo-QcvV5nW4z14IfHoiFQnMTIQ4ZYgRfGH4EI1tUeIdGtP7IOkdXfc1V6Oxi7NcM6Hfudw0IFY8VbSZGG809iKUGecfQn_yP65qkf9YEQneT9QVPwYbMwD20SMcy78GR6quwThCzOp6R6ZrEf3jbuVittGwrW8Vhm4caegrscDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت لیونل‌مسی در بازی سوئیس از ناحیه چشم که خطر به سرعت رفع شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/99903" target="_blank">📅 10:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzIENjrFoBglLezmIMb_JaQ1Hok7VEg3iQk8Lc_3Ni67QOdC0Mokq_7Bn87xxLkc77IeJYoqFMOLkDI_hjnANWBMbWuQR93orVwZTG0N0PT6b4hzIOyd6R12TIojdtSlLK8uycQFYZoCE4WqyQJwCs78iKmmacBUhTVK7cJ3jJIe5PQSWBMwL8asrTMi7I6WWG_c5YafZtu9SpH3-9aWnN52J_WeVL0ljQVnQNBv9FH0AlvYx0wD8HZ0Z-rU-9rj9hqU3YUP7n0epA38zIGHgncYzlw_rrHHZzisZVfUtrq9EKxmgp8fIVJKyQXzcmNOsTLqyQfZCbMkdtC72aoEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9F4jbyPOYEo5jEurrtHh0X52lG5g7p14DzSko1gGfUswWq-UO69dpT0ngs6ytlTTADeWlC7GgNAl4ejD6fT53G4ngD0oLu5xBabRNt_jN4HjcXksz0HQmUFtQTgtk7gaekc6ohGFwRkPWo_xwLKsjL_M7hyGgIeorC7M2Tay_nX-zoGlzgCTFpMTkfO-VSClR_gSrem3ItZxZYb4X8Ni7stR49u8U496zNvUWlhHsh6_z9EZ6TCmwK4r0xN5tNng9uS8msbmz0OdOsaJjCE8VvWJL6AXcUAfj6pSF8igxdRBZNkNKg_qGGKXIAOQY_SQuO3rkBpaNZtavXMHaouXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oluk-eTn8Co8kxSnvBPmqfGbWLLMF1kVzha-a_QiqBVr6FqxCE7soc0zRKw3emBbNFOX3z6P3OLYrJCgxYEySrWA3RyGsZDURNfFqkAt50n6CBVuY9hWQhV3IFia3tTRjFPmB0rlVA_mgghF4Q7QkGEixzmqe03wllZ7Lxn4lCiEt2OvQsSD_9SMvaKTbsA71a6abkKGQAlXykLBnzqbCAV9di8FCjLma63CYTOhZO7SL3KHCJPxsM-avpjSS_ksh_B2RRYtjTM2-XHVceyXs1bXYwhPBxH7X79vm_lcsuQh4DJmm5QMhAYPdamcuJbZmhaUDQyGFZAq2G_GcZpK_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
یک سال پیش در چنین روزی چلسی با برد 3-0 مقابل پاری سن ژرمن برای دومین بار در تاریخ خود قهرمان جام باشگاه های جهان شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/99900" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=gUwXxAVyrX1x4T3Y7M0nRK8A5SfvO3RTvE4aykILkaO34Vo1k_ceYgaL_yacLvVXwzDmt9WxW8fDIwaImgIsgVvoJXKZuJuOXnYAqSYLxLSHdoPUbKE4pXppj_YMisb370sh6c0nSo1EsOkjDkUh__qGcWoHTvX7Lfi33a-Ity3LeMUR30FD1nHgrnB6-0O4UKt4sDnBolaH5FgUswW-X1pr_E_HcRszWuUIDIROQZp3A2UjWTTNP258ykDNvnFrutjTdi8buYz98MJAq68KFPFVpRGRjEnVyq7Ke16fmXTpeLbUARnU2of2x-BWcesyOKn4tBGZMUnr1x5hYK2zSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7079ceb818.mp4?token=gUwXxAVyrX1x4T3Y7M0nRK8A5SfvO3RTvE4aykILkaO34Vo1k_ceYgaL_yacLvVXwzDmt9WxW8fDIwaImgIsgVvoJXKZuJuOXnYAqSYLxLSHdoPUbKE4pXppj_YMisb370sh6c0nSo1EsOkjDkUh__qGcWoHTvX7Lfi33a-Ity3LeMUR30FD1nHgrnB6-0O4UKt4sDnBolaH5FgUswW-X1pr_E_HcRszWuUIDIROQZp3A2UjWTTNP258ykDNvnFrutjTdi8buYz98MJAq68KFPFVpRGRjEnVyq7Ke16fmXTpeLbUARnU2of2x-BWcesyOKn4tBGZMUnr1x5hYK2zSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
جیدن آدامز؛ روایتی تلخ از درخشش و خودکشی در طول یک جام‌جهانی!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/99899" target="_blank">📅 10:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeYIr-42A0UplpFprR-iscW601g38KsL-VTUpatxwEEEmw91W-cB3o7kOF-uUkHVFrGSqyun6c0ijtl6OuwYcYKRiKQs4k-2sKoemiBPyNmeHLYuBmx53i8dc6_4TjINOnjQOVuYoM4apeDOlE53k3GmZQ-wfMMRpyfapA_ch6dAunpPp21dHIKwzGTUKGBUT2IdlrpeupTe8-tonSwssbyJ9umyISwLzsS5YO2mYPJHR4QJgAhS1pkCkqnoZXIqYizvwbLEyx5Qpm4qBl7HGgGsrONQNHalUngJTPUaUIkurE9tbKzJK25kh6Lp82T9Gnukrc8FYdd91KBaseCYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
نيكو ويليامز [
🇪🇸
]: امباپه یک بازیکن فوق‌العاده است، اما ما بهترین بازیکن دنیا را داریم: لامین یامال."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99898" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=fNJVRXNspI4K92-WB6n58L-kIr_EpMJNdVd3LWj4SfxWc3Z3rd4uDIWvSTSwSDRM4YFB5rnXaxcqxMlkgJGkdmZedumhEzWIr_6XAdPYf58tVNoZAIwxrlbjkdgvSwbUI7WsqEqJo2Txx0SzKDJgod8meNEko-PhmCQgNLO5na7b0YSQ_owY-mMz85CSsHUJ_lSKxwS5shER5ZNjjzvsCFF9gbjzQKEANCByBrbxfJcjAoU6sT8WW6dttdWAvEteYDM07xouZFtEu8-aEr4n5ZTN22NK1mhKe9cuaJ1TOJfIwesIMA5CXzciceHH8dHeHJWAaoLM3STjfILzgK6hAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2501cb2ee1.mp4?token=fNJVRXNspI4K92-WB6n58L-kIr_EpMJNdVd3LWj4SfxWc3Z3rd4uDIWvSTSwSDRM4YFB5rnXaxcqxMlkgJGkdmZedumhEzWIr_6XAdPYf58tVNoZAIwxrlbjkdgvSwbUI7WsqEqJo2Txx0SzKDJgod8meNEko-PhmCQgNLO5na7b0YSQ_owY-mMz85CSsHUJ_lSKxwS5shER5ZNjjzvsCFF9gbjzQKEANCByBrbxfJcjAoU6sT8WW6dttdWAvEteYDM07xouZFtEu8-aEr4n5ZTN22NK1mhKe9cuaJ1TOJfIwesIMA5CXzciceHH8dHeHJWAaoLM3STjfILzgK6hAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
خیابانی و خداداد عزیزی دیشب نزدیک‌بود وسط برنامه زنده به همدیگه تجاوز کنن که برنامه رو وسطش قطع کردن
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99897" target="_blank">📅 09:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=MFI9qYvAHfq_AyxoqJaE1c5XlfhACcGUpOotvmYRcFVQj_qHVxqCFj269nwmrD6MNUVMEfdKVZbTc61Bm4MtTbXwyEiuHGrhWYvcvfznYbRe1IeRiHCVNMvN9fIhGDxP0FGOcp8qd80rxZH28QdgHoRwXkLQ4sAqmDBOnelBkU9PJZ0MQvXK2yB9nUMw0Oi8XuY-l7CXmhNKc8xdJdq27p2DRYTKRH13Y4GogPO9j-C5wXDKkzAnoC-iK3x0MCgzmzvRcmV_v05U4CC0yAwvuEzJ0nRLMebR8kDG-8DcMlXY976tMyj4AXCfwEjTtxQB0zCnLpsB2A0tKGU63SN4Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0aac58e8.mp4?token=MFI9qYvAHfq_AyxoqJaE1c5XlfhACcGUpOotvmYRcFVQj_qHVxqCFj269nwmrD6MNUVMEfdKVZbTc61Bm4MtTbXwyEiuHGrhWYvcvfznYbRe1IeRiHCVNMvN9fIhGDxP0FGOcp8qd80rxZH28QdgHoRwXkLQ4sAqmDBOnelBkU9PJZ0MQvXK2yB9nUMw0Oi8XuY-l7CXmhNKc8xdJdq27p2DRYTKRH13Y4GogPO9j-C5wXDKkzAnoC-iK3x0MCgzmzvRcmV_v05U4CC0yAwvuEzJ0nRLMebR8kDG-8DcMlXY976tMyj4AXCfwEjTtxQB0zCnLpsB2A0tKGU63SN4Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خاطره هاشم بیک‌زاده از احمدی‌نژاد و روحانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99896" target="_blank">📅 09:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=piCVvmZybIRhjvv2HAgIDkkGceW91R93TDTLyx_9HG5tPu9dcAg2uluCE5ToTHbG0BolqUKb5cJP0u9umboL5YJpJu-4JGB97f-OszW6RTHLW1ogTFchYJU9WVecfaWBhiShAu98AM-51H0fmqY2XNdJi0JTkfpOduAUTRT8wEtPPBEECc745bTuCNxqqzLKGuQHGUJblJB6aHB5q__rpgQ0EA6S27XByJvvIMUO6tJVJp8wecTRavuRHUnZKUyat37As26BtBD-z-9XystjKYujN9tji9CzcIc8w7dGxSACMn78lI88eRSUVWbWxjckqOqDCy_uzJVxE3F7yvVPzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a56d32af8.mp4?token=piCVvmZybIRhjvv2HAgIDkkGceW91R93TDTLyx_9HG5tPu9dcAg2uluCE5ToTHbG0BolqUKb5cJP0u9umboL5YJpJu-4JGB97f-OszW6RTHLW1ogTFchYJU9WVecfaWBhiShAu98AM-51H0fmqY2XNdJi0JTkfpOduAUTRT8wEtPPBEECc745bTuCNxqqzLKGuQHGUJblJB6aHB5q__rpgQ0EA6S27XByJvvIMUO6tJVJp8wecTRavuRHUnZKUyat37As26BtBD-z-9XystjKYujN9tji9CzcIc8w7dGxSACMn78lI88eRSUVWbWxjckqOqDCy_uzJVxE3F7yvVPzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
🎙
خاطره شنیدنی رضا جاودانی درباره شکیرا
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/99895" target="_blank">📅 09:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HyhNIu_tvETGUxXQdKoDh07F4ivZCC9GzqV8InDCMsc42eMEPxYNpNiN9aPG4b6Xwzi88C1sVuOzll7CFmkVwSaWK0QJgnb77VTLD6Efo0amtysJOYAG-ivJ2DTztoncl5Ocv3eMGW8WArfu2MY_yXjDpC8_skzR7HHcu1BxeH3HmvEt6b3T7rSedpIr7Sqkrel-ytXxorgCW3TYbkFNYAwZjEfTeITlS6ZeQ_thfWPX4lwpAYmZgGAoRcil1sTbu6gnI6_JY-nctPKFpNFHfoQObstqMdSUKdTpC_x1tkrrky1wFPhLU7frL7AG8msixb-spNT3AdIcQRdGiQ9asA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
ایوان‌بارتون داور اهل السالوادور بازی اسپانیا و فرانسه را قضاوت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99894" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9ykGQsB3opHWoaXLHx3oEjK2L_LvU7B5jBzuduJR5cy5RHBUEiC6Sh-58aO4xviiiXJlO_106w5LWAbNDiEVX5WvngzdcAfoUnuGdSPuHvgCBytAEs3WkEZYdYDu51Dt9Q4bC1HPBhiJog_6YjqepWeNpdixtqZZs0Z_sGLMugbdtlmnXGrIg3e7PaNSYfVR8uFBrAsUYv3fu2aNawPjEZJsDHkyiFWKnNHoAuynHtgIswnHuPDcAk3ozwVtbdQeDr3wuPAOfz1Fjc79xI6h5Hb-WxPRFtw43iZ_ljz78QLCoXYCKg--Z0rj_qOaKXGZ3HIqWnLxzgTfN4AtHaGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLI0sGZIP5DHpvE_sW_TXQNNB5bf1dMvr6_bpgyrYRhzH6ThyFpThHWO3WOyPiz5J2eLkrtr7yZN6cDRnHhtitE1xlKFMQdAYL11FkNYcJQe0aMS3KFvLH6rFCfIvQtOfNJao-FpLhJMv21CC1lJwSgMLRkZGKizXSUrPmaz3jLcBEXClmKk1usIy0sI_io9-u32gI4ubTPYdZ582F9-mQ_xAsuDX1GT-BLBl_RSVKCKBYgxIhZUkFELX8GNaFZ6X4Edt9Iw8EwrhUhjuuRpML5Hqu4cHRcUWpYEXFY6FVBcYlYAE3vkq84U2dUZ4bvrdFJT9TQYeGl0CrvO7ZuuIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99892" target="_blank">📅 05:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1MpkHxCuzrwfTG_BpQ_fBb6sB8Xv8u-k1Ue2fAu-LKUmdXd4PnEfoAAOBurYyJmqhsh_IvXTOHCJKiGQBMAnBAm9vtwQjWJanJqiz7xpgGEOpUq9FxVB3tqJabNJiKGxqNxOejVzxehwK8zJJH6oq3CSQVNmgp_tm34Wa_WW2MkSuW70UR94LVpia_KZvTr2KSy4qQQ31bwAXJ1iBGA7xs7j2XjLBhFKFZ8mXmPPVxjPOd1WQ5NRRdqBWugcOn86R7VZbv-KG4Q5T3W8emYhDGMNzo9Iz7wzFEXNbHVFUrBug0qvXQYAMf-pKkN4HyOA9XwxR4gZ8kmEFCIf4ZqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوری
از بن‌جیکوبز: الاهلی عربستان در ساعات اخیر با ارائه پیشنهادی نجومی به مارسی و دستمزد فوق‌العاده به گرینوود خواستار عقد قرارداد با این بازیکن شده. مذاکرات گرینوود با فنرباغچه پیشرفت خیلی‌خوبی داشته و فقط دلارهای سعودی میتونه این انتقال رو منتفی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99891" target="_blank">📅 02:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=OPmuzuAp63MhAIxW10_zKYPPq1Im41Ge8qlpsWX0BLFoecMWm2H9-Gob1SnIl__KuMqiFM0SId_15OMOe2wggz_oswgfKpWCNVtZ8LtN1NP_BFLLHm178Zml3GUMIE3dSt5nCW9BUzM1X2UlDEMJ-0aw9gaJOa9q7AT4n6cEcBAW8FH7kNIbbQXuJR6Ux4d2fquh8pjOGUxwXjmNkNOTaXsVyGcEETmNVZR46-CpCJy6srnHTCQZwF-kHmz9gGkwXW7JDVMVHcL6_fCXeIsdxk-IzRYovtm9w1048H_Byz-WOzfVLYEqtjz68f-y5MOEJJmzetCt3Uck78c-bazjyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f230afe8.mp4?token=OPmuzuAp63MhAIxW10_zKYPPq1Im41Ge8qlpsWX0BLFoecMWm2H9-Gob1SnIl__KuMqiFM0SId_15OMOe2wggz_oswgfKpWCNVtZ8LtN1NP_BFLLHm178Zml3GUMIE3dSt5nCW9BUzM1X2UlDEMJ-0aw9gaJOa9q7AT4n6cEcBAW8FH7kNIbbQXuJR6Ux4d2fquh8pjOGUxwXjmNkNOTaXsVyGcEETmNVZR46-CpCJy6srnHTCQZwF-kHmz9gGkwXW7JDVMVHcL6_fCXeIsdxk-IzRYovtm9w1048H_Byz-WOzfVLYEqtjz68f-y5MOEJJmzetCt3Uck78c-bazjyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
دختر علیرضا بیرانوند: بابام استقلالیه و دوس داره بره استقلال
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99890" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇪🇸
🎙
خوان لاپورتا: ما تو بارسلونا برای هرکسی دولاپهنا نمیشیم. یه پیشنهادی برای اتلتیکو ارسال شده و هیچگونه تغییری قرار نیست اتفاق بیفته. بزودی می‌بینید که‌پرونده آلوارز به کجا میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99889" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6_MuqOXpfY33DAfjo5zNjnIXrZkAJ8p8Kh712HkIzH7VdwdJAt-vd44x2qzeAdyXk0m5AP38-s7Uuxs8Hx4Mh_XJEquEBiYjR2hejWEjlKMQWFlYerQWpkQ2rVM60c3mUTGs4LxFP6530qqJTyTLZXBlL-ZvRdmoUOiaSqxzNahLNAWIW4SNysq0B9PZky0Qc_gF5bGDhcwfaMjJGDvr3iSW11Y0BAfifnEcNDzC3_fuwt_WB8Bx5cX3e5MpVhcDCq8q6fwuvqzyOg7MEY_VEISAxEEYIWLuMkIXpaqOyTohANTLs2X5d3FOcxgP2kXdfyZjbBfQ0haVY43k2fotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99888" target="_blank">📅 01:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpeinUb_4yNFA_GzYZ1w4FaRJOKl6GZl22-migZ9J8KKP7AlfbRo2iL0QFrMuQ3F4ExSkr4-aWSl31azgSV7bMOJDi5cPLyWyrtlTrtETv6COAsvBUPCbmMAyBh61wTuv7MLVWUFpL71iDzBLkhmC5D1tmKTkck7vaYK4p9ffx2_75HoHnmWbVSsnhts7Pb8PCltte_3Z9_wXew1DiFfCjEz8-EGWQEaE8v7u_5Wo71_n9e2QtBPm_phOPSH_KzPXNY6ZHKajusuvD9IeVWq-s40d57jwgV2v9US--dYTi69TEWdes5DqP9fw50XEvHkWQZJQFu8xH6-Q6ffmms89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
💪
‏ سوخت‌رسان‌های متعدد در خلیج‌فارس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99887" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2Nm0Za5btTUE8UejvOaA1zQjRlWxDfiavAL4VsztLSlJ18a9wAwssBqamj4cHz9gP_8uzE0hp1ClUer7zlMrFTfEf2cFa5qjZfsDSzSUWw7UAyyBbShRAstVk1YWXsvwbwRqeydWhVDvZ9IcCBGqlB_GXOLO_VHmmRR5AGgYe4XQDccCzMgcRkedtMK-LkhQ149EcSpXLALQAZI66Kl2RK2G1xfAjPpTtXPUaL_iB-If2SEKCd1ayUeaike78twwl4KpeuJ_l7CVNxpgGh8syucxEcNIrcMHvqtyF_O7-Jm3EacmmnXr1B9cHRSeXKTVp03dNpa1c8_LzofBzOu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوری
از رومانو: رئال‌مادرید درحال مذاکره برای تمدید قرارداد یک بازیکن بسیار مهم و حیاتی است که این بازیکن وینیسیوس و شوامنی نیستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99886" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvXAKU4ph54-DG5YYr2s1r5duA1PdK9bhbfae9qjcJ5eAOSKFcO_c83HG662VqW2_inO8Ok0pGxDs9oUzXZP6YbuC2oRmx4QUQu1HC4wdnzxfaCmSY2-95qv-JneIeYf4Hf8NXYwX9JXtOgRwQa39004sUnkDfCyW9r3B87j0ykaA1KPoRqjgop1vfB_6yGdJ8hiCxx3mQdDpMm6QI-7Yw8Jzs45FD-q7r-DcqHglv-9Afh2tf8k2rGBn8MpMoThmJCfE5MBPxHybzCnfccq54yELGcgOoYk9nNAioU8U0QymSiZPolxTGDM1uOy0gAPX_A94T6JpExsWjl_sfKndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لامین‌یامال با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99885" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6AVIHPuXV7COfxdy0tUQLnG2cjqWNqFK81Kwh0FL4SQOv_1Y6XatiEd4ikw0cQVATXulKBPL9MXmt-M2DubURBDW1a9oI3mRmHodaeAJqgfo3RKzMbSBHXKx9Ff2EFaZmnOI3S2ClpPCqFVsywkOzeXVGMxw9qEQjrVEDwPEXsHPPYHMImhorAbdhvlOx__vzpHxrUcTjD9-fF0B7d6MM7LWt_0N-I4fUt4lYA5EPL_n5_VzZ2Vyfvz60R-CoO9xdM--w1sN_zQAHiMIG8zPsPO0sJG-Lwr7MFZO1xMEqExf9Cc0GB_PEh76vzT9hZnkNIgqYTt-VOs5gObleMMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
سنتکام-حمله به جنوب ایران آغاز شد
ساعت ۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی آنها در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند. فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99884" target="_blank">📅 00:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
انفجارهای متعدد در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99883" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
چندیدن انفجار‌های شدید و پیاپی در مناطقی از بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99882" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99881" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M7NVehrm82z0G5tp7ik7wuM27a0A8hGBmwAIqfBXAlmbskG1F5f9508cXMbgO_AsPk8MVl3fbbUJkWIslLarF0-u4I8Bu1E_iq_HgYjVoEbpSdQu6mpEhpBgC5vubAvtBJAPZHUsvvHUmYXMnPEyNNensON_WdwAB9cx92DF4LizWCl3dhdEf9eIfkZJ1X7s2HFfMSSrvUZ3_tnY7KywhjhOGb6XlfjNYWc6mYLURKkMAznscdZQ7h4rJdW3gF9wdJS7bJ8U93nb1aj6jtH2uDeUk-jj-ca5vw5K9hprNfkg8GmUDasm2MjfiiZzgzM9j8sUhS8ZA03fuX4ZBIgx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
پرواز سه سوخت‌رسان از فرودگاه بن‌گوریون اسرائیل به سمت(احتمالا) خلیج‌فارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99880" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
💪
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99879" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwI6DbPu07jb9oq7-Mk-m6oBC1UNROu7NiF-s_CIvhbGVPpI_qFnwxI81kjwarrRlfTvtOGmVRN8DJVmSzhylgtEG9sr0QgBgaMo40F97KK5kgEYvVF7T-WhLIWvxM14GyZVU7bHuMcbw4Zjt0R3oPQ3s5bJVcdzPUzXEmvTRQuedGtakv2ornkk9QRtA6-EmjexH0XP_L3jlQrMg8wJJ8GgFN_OSzq7OjtlAvIeQa6iygDPpnge9yg6hRLi3uMB7JKk6KkajV9CdsIb2x27gjh0Yv2cYajG9BgiX8pX6sNWX_ImgQE2tW8-cx8u1AIJy0CYGGkzRrIbRISoXUl3bWRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab9b193566.mp4?token=OwE_mE5RhDRyREzDKtMRJlSDq6kgvE_chI-Bb7SMx6EaYPGd-pPCBWjMpYeDp2FJQpnHYQqLm7l6gHznamEB06E07O-zYvLupCpjSbXfFojZKTp6FwVsF-hLBsItPgm1Hb3VpxcYVVCmL3g92xhSIFXEhoTRGFgOQZ_zC3Uky-AthLc0mKld5jA3Vv0ylcSmgvqWlKSyzg1nM9E_0IoRQX-p4aRGKFtL8TiuQWUYHfbz04cvUT9vKKrbEZwGVLegkxZoy5rGbwafjAaUMCfqc2cvhjJUGLca3uajlzomIe4vWb18HpLT0KmS9vJ2ZEAlVIV8G2XMHt0ZUucRDaDRwI6DbPu07jb9oq7-Mk-m6oBC1UNROu7NiF-s_CIvhbGVPpI_qFnwxI81kjwarrRlfTvtOGmVRN8DJVmSzhylgtEG9sr0QgBgaMo40F97KK5kgEYvVF7T-WhLIWvxM14GyZVU7bHuMcbw4Zjt0R3oPQ3s5bJVcdzPUzXEmvTRQuedGtakv2ornkk9QRtA6-EmjexH0XP_L3jlQrMg8wJJ8GgFN_OSzq7OjtlAvIeQa6iygDPpnge9yg6hRLi3uMB7JKk6KkajV9CdsIb2x27gjh0Yv2cYajG9BgiX8pX6sNWX_ImgQE2tW8-cx8u1AIJy0CYGGkzRrIbRISoXUl3bWRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: این نیوزیلند بود که ما را دست کم گرفت و می‌گفت کشور جنگ‌زده هستیم تا بتواند ما را راحت ببرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99878" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=Bc1yrtcUGH-5ZgyjKEy7iZjipxiemjTtdNFX6jwYPL0ZnxnaHviLd664-gzG6jI5SFhx8HqN3tWwBK66RhJ3rxS5fJb-x2JyGCeB4vT7OCX4Y8WHLYO5EBmCnPSCUncrSeH6zWfm-8iO7HWItCco2F_d4lnLXALyCcoOJNpWFOWsFo28qMVzGKyEsTWKIveIPrf9k6aq0dk6rVfhyR-4A9AaktpwHY0RjE2eeEccj5C7ldcVnt-CP_fcQHJ4AjkEvzxofGvlf4nZt3ulNngL4zN9OKxN1h6pR9CSeOiNwNT8chKOMYs9CSUj4wQIKiaX53bj8B2xmlKW3eRBzpTnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6782dde8a.mp4?token=Bc1yrtcUGH-5ZgyjKEy7iZjipxiemjTtdNFX6jwYPL0ZnxnaHviLd664-gzG6jI5SFhx8HqN3tWwBK66RhJ3rxS5fJb-x2JyGCeB4vT7OCX4Y8WHLYO5EBmCnPSCUncrSeH6zWfm-8iO7HWItCco2F_d4lnLXALyCcoOJNpWFOWsFo28qMVzGKyEsTWKIveIPrf9k6aq0dk6rVfhyR-4A9AaktpwHY0RjE2eeEccj5C7ldcVnt-CP_fcQHJ4AjkEvzxofGvlf4nZt3ulNngL4zN9OKxN1h6pR9CSeOiNwNT8chKOMYs9CSUj4wQIKiaX53bj8B2xmlKW3eRBzpTnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
بیرانوند: آخرین بازی دوستانه ما پیش از دیدار با نیوزیلند، با کارمندان کمپ تیخوانا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99877" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=Q_HnyMIsceIyRt8ReVy45RVugEidj_wZv8FAUTqK6WNQ5g7DSuRm4dtQPIQMX2-F0UvYXLyj0zHYBu6N1YeiYfZ0ze16FsONw8pZAV0s3T63n9oT7OZblItHg8GBZge7hC0Je02sdZtmPKtMqWPSVbDz6dMPYI9YT-YozjvbJKRZFBj6YWnu-fM3FwaJRjIzSYMz4ZtAToCasNn3amzRNHeprbXGBkyT3k6Rst9MI60QAaZfpQQNnvgLFpAZl5c1BcqVISjhv0FhddDLCjG9RNy7uRmhB5aWEu3A4eH2JazoA6zJFBk9KA1GC9yGZ8YQhf-ADChlIw8ZHYDi0Fhi1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b76e61623.mp4?token=Q_HnyMIsceIyRt8ReVy45RVugEidj_wZv8FAUTqK6WNQ5g7DSuRm4dtQPIQMX2-F0UvYXLyj0zHYBu6N1YeiYfZ0ze16FsONw8pZAV0s3T63n9oT7OZblItHg8GBZge7hC0Je02sdZtmPKtMqWPSVbDz6dMPYI9YT-YozjvbJKRZFBj6YWnu-fM3FwaJRjIzSYMz4ZtAToCasNn3amzRNHeprbXGBkyT3k6Rst9MI60QAaZfpQQNnvgLFpAZl5c1BcqVISjhv0FhddDLCjG9RNy7uRmhB5aWEu3A4eH2JazoA6zJFBk9KA1GC9yGZ8YQhf-ADChlIw8ZHYDi0Fhi1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه سه خطاب به بیرانوند و اعضای تیم‌منتخب فوتبال‌ایران:
از ته قلبم بهتون خسته نباشید میگم
در ادامه رو به دوربین:
به زحمت این بچه ها باید احترام بگذاریم
😐
😐
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99876" target="_blank">📅 00:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7990a07676.mp4?token=QuAKVx7rDWeAI2o_cz_q2ZURtb_VQ2LwmC5zfJ31ZYxDgkGciv_D7VwDF2zYs0miWxneOuVy1vBCVEwNqNr6cU0v_v9S2iLcj2F5VPorNZ1BO53m1fMfpR9s6hkMh_5j2efxGzbMIgoMwUg9fYHhiLQwGTrA7B1wzticacTt6y5MRwzs6iVbSKEd4RZjbNRtsyD5S97hFUpuLUDca9tLfr8QNTIy6XhH6DRvW9JAY8WHwrRUONLqTigpL6dbzhmUptje0wa5USewcVOL3senH1_oeTFoMkIKLBpg3JN9cG_If6P0pVWAc6yDU23CW8gnbYSRvla2rfX7-w6qNVbovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7990a07676.mp4?token=QuAKVx7rDWeAI2o_cz_q2ZURtb_VQ2LwmC5zfJ31ZYxDgkGciv_D7VwDF2zYs0miWxneOuVy1vBCVEwNqNr6cU0v_v9S2iLcj2F5VPorNZ1BO53m1fMfpR9s6hkMh_5j2efxGzbMIgoMwUg9fYHhiLQwGTrA7B1wzticacTt6y5MRwzs6iVbSKEd4RZjbNRtsyD5S97hFUpuLUDca9tLfr8QNTIy6XhH6DRvW9JAY8WHwrRUONLqTigpL6dbzhmUptje0wa5USewcVOL3senH1_oeTFoMkIKLBpg3JN9cG_If6P0pVWAc6yDU23CW8gnbYSRvla2rfX7-w6qNVbovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا بیرانوند: هرکسی جای قلعه نویی بود و با این نتایج برمی‌گشت، مجسه او را می ساختیم. خیلی از کارشناسان خارجی گفتند که باید مجسه بازیکنان ایرانی را بسازید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99875" target="_blank">📅 00:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDdcxVkKDx7tnOzFVeY3Lal6wTbgAr-NBGzjmaMPfD7IjSs9Wk0xwdPMkl4aUs2bJzgICtBAUBUCvRAQCyzcXzR3c8epjtMwTqk-xnk5zzZeUHc_mPhXqdM2qcCsUQETgLCV-_U49X4w0dpeCbDAT4UsUNQR99nbprV6Iyjo71UkXGuA67wjw99IegtULk11Nlx0NJRbxfyINp9AZvrk2zJsorpzApOtSXbN9jXal9Nrf4qtOInq8sXKqs8NkdenRcOQr3i5DBTUcJlRu9YV5_MPzUE0dIKN_ALsBA_LYz4cuzNze-8tF3qm1J_YesBHZGPt0AqNc61qLKzvGvC0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از موندو: بارسلونا در صورت جدایی فران‌تورس و عدم موفقیت در جذب خولیان آلوارز به سراغ پدرو نتو ستاره چلسی میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99874" target="_blank">📅 00:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElQ5A83nJs-w9_-LtjYNOLsdPSLkASqjsTDbFujmirAmGN74LIdE7ePSRFK3mL_-YOWaWMBHB8TmwZEu6dcmCBiaW8RADsHleGB93ZFxu_I1H1yoaqtOdQSIN6DhUFIsDRNt7f5AWBzOsvb44hZFGdZ_-kVXulimDDGasN9mBwD9IGXAnEa2U4bWMpL77-1__2BIN-CNfNMUBhYR8lq2EeDWpBqlf_d96djMCXhYWVJmp4fH0YKlnvkMJza0Gh4_nptRTV20CQjajB7jKF74fLiUZvHddYzqUfqDJAKK-byRMgNCXj-ruSvmLXYThQHNgwixrGqTpWR-DOpFhMYw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جود بلینگهام با توپ ویژه فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99873" target="_blank">📅 00:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: ما بدون باخت به ایران برگشتیم و این برای مردم ما یک افتخار است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99872" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99871" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99871" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usZYnv9uNBk8SrgLo859nE2t8Qtl-ZwLLzhIZ3vnlpt_OFrcaQm4njDNSS6NL-DAPnMpdzMlZlfDON5WpMmrYUrwLB7XoU-eoxemadxCTBO0auUVgVGb1O8-xwaHIbCecqMtuqwCOcejnmlWyvvMpawb54DuUpW_hPgNll19djQpSCg_2-wHTbAMaSohu51mf2k1M0wOTKuLVBG13BAuXt6aazn1uOUOSgkqv2lprc9wcXLEAYWuDx6MDZvo8foBCzLUVueDyCFj3JXhrzZBUB-dgvNBqWNXIPvURU3ZfcuFsRNgTzRaS6OQY5jmI3i82slFFM29sF_hKa5L2_69pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99870" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99868">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4_0MGUZB0HOddHEC7tH2cQ3d0VDdpImdo_Hh1-5R7fSyO_AKkQKpGGA8vnM_3MzdagFznkdUUi-30G9H19oJmLhZ1onYaIeiodIxpwvJNThXehsjE2ibKH8cl3hRVDVHmsZc6Pvf9Pk5VB7V6Nd7aKa0yBcb4haUjToFXOdQOPK9n2JLgZ95Nbnzo0Ri3lqO9VFBw3xOLzBjNQFvJQWKLAUK1NP7nIOdGEPy7DHUphQgWP7lG-cEg28m5Jl8eKvJtGOVpmAnHmvob-H6Z4g7SHo9TTc45FvdCCgg4ANg4l8z22UPaDs65iy13PpF3zsMd-z4DEHUoulzPLrnF7p_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#فوووووری
؛ باشگاه لاشخور اینتر درحال مذاکره با جان‌استونز برای جذب رایگان این مدافع مستحکم تیم‌ملی انگلیس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99868" target="_blank">📅 00:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99867">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
⭕️
🤩
باشگاه نساجی مازندران موفق به هایجک کسری‌طاهری از پرسپولیس شد تا حضور این ستاره جوان در جمع شاگردان مهدی تارتار منتفی شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99867" target="_blank">📅 00:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gw-ajKB_VjParP1T2kthzOWp1UO1g7_Ao_GgUNdWNOmKTywKQmWSsuecD3afuDcFC1NTt4o646nCSUMg5J_vSpxxGB-yhyDenFhIXu5Z4iMs8i5uYoB8LK4dlvwTTgVYMdpqlgQmLp1nNHGoQgcoCgKZSL3zgnwEJBTywKTrCmiZFayzqdasuYHwhGDzc_62Dhl2jPCRQPwJVjXijAiiyjwJc933thKjoqv2EqTpVQPS1riySeujotfkxTTjg2734QqFuNdNEoJbMZl2S9e_uCVCRPG5uJHC9za4q31UWG-Z4minbOctK2CtNR_gIFJUlCTrdpbjayhwUMin_-ZrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
از فلوریان پلتنبرگ: یوهان مانزامبی ستاره ۲۰ ساله فرایبورگ پس از درخشش در جام‌جهانی با تیم‌ملی سوئیس به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99866" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pmhx-M1m0MeOkD-872bC55lG6SHdk0VHToG7NY1-f8hPZOV2hj5WtA5Kx22U72sgHPtz-XMzeDBe7y5rFnlldMsr6AXQEZbCG34JbSWJq4qrsmNJkvR-eb_w-tkmg1xs_QH-STm8eQxCjh8q-cZu0HBxAhOi1UbHrDNhwFLpHnhMGdRl7L37Z74lVASjES4nt9qTDkOwU8rQlYRlgG3uNIMeiqBbg4SMxbr5mRNfYe4qZaCXTP_7bwvxH_BbkabVzuVgzLE-hNqt9sTvEFPOjkxGihvZ7mgO6atNwXeHbud_14_p3ALpCE76TPQ9DN68ONDdFtxxn6DDJbpVmeBv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری
از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99865" target="_blank">📅 23:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUOuE7476kx5iUywdVAS8yz1rlfqJNpxg_ihw1cegi1DOuMzomljxaCXuLuGz2RuNg-cPomgacYtXdxmh8qHoYZ0scwh_3jeMulS5KAw15JUjhN-o4mTJtitxPxJ5jhmClNyvD0aQ2Pyfx965l-fJn9C44nrQzYIvxaL5xNM3P6N0jNgu38AeAHBCBG1QyPSBBlJHLv637q5PyCZrHkJn1my97DDvZyrztYZA5TOSfvpJfPyz8TIolMmP-QmyNcZR95OUPWBMr7mzxQ1xyI7gMZlolgsz8TSzkl7IiyziEFbsosJy49pbKh1hjPjb4g4pMSPQ4kvPNRFcuo2uSW0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو هم دیشب تماشاگر ویژه بازی آرژانتین بوده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99864" target="_blank">📅 23:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZGV7sLR0FQ_SPQmGCtaUJZ0xR5dT38I-dKRm8_Ch6PZjiG1j2JTSGlBDGWLNj78ZnY6z1VvP1v6Bt9kg2QXqcxF1_MZKNz2D5f3x7u1tQQ4OTYWO_JXiyH0RIi4quacsZeAvEqpq2S8In0UupZIcylToRm5RdvGckO5hMd8OxTOdZR-Y6TuaPvsjG6_p79VGV-6F0sCDLOXx9yCQrCkJUV3iC8i0QCxUdQVUAEKBCraeeABJS4azO2gj6B-C7JWCgyYefUl3-lMTvVi-_Wy3pUdc8eTXlpAPJ9xEXb9yV-8cxnOe0y2KfXdOOguVkwwxYU2vWwTQHl2KbYgIHw3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز و دختر کوچولوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99863" target="_blank">📅 23:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDFNbMsVbgRJMKG_Yei0rq_dc3IdeKYkR4EbPd5opsSKyQkriH5dSxkVQJIiasE1VFdgHFrbCNbA9OTgsdGnQ8mFmUjFDSxfvcNHyuOTh8ZvtQ1BBfd-1DwVBRSk-ascj5-g50Iiy1Nl5UwGA3v7a5-mmokV_Pn0ItPKUcD4MbjjeOjoSpZV2CSBuCCv0-jFoF3j06dv6EfjEMSc_-cW8xXApsmECEpHajxiOxsTPiijz1g4nzXzhvS7Vplq5Ki9e-O6g2X9d3cs74fdJrrLn2rINvLABxJ8mSBtx30CRtSZvWcF9OQB53YWWNTxZado0UVzPOJCTXOHTli_PO5vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیگو فورلان ، سرمربی جدید تیم ملی اروگوئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99862" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCW3SwoacmvGhdWUf8ujg3zvCq1ZuB4ATgzHm6XW71ILKNEkJj92oYeloPzWZ8zSo_hJ3yIRfteYQcfdZmd_eYvdhKnRWvQLsXh23GTTeBGXccmntz0S00xvaacq-LubiRSwWJ7MxU0LOQxKEElgdl02rbs9N51_bZfYSVxfQwmT2-dezcMeMkMhCqBFzhT_n2VVewB48-swSqyt-P78jiGOdD6cqDeFKx30T3r-iA_S6Wdtgl8Eg5ne4g5T69HVOxxzi38eBCC4twSdlXE41rme53S7ulUoyboIFIJ2a2Os7yga5Jbbq3a8Agi4nwEOzHGjCZjb8aQud8NGAG178g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/99861" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INaOaXen6rzDBx4u5sycL3sTbu0JGyQvoEBZRt9PjrA44RqNcadAAdA4NJxvoR2lxrEPgla8DsRS_e0yOtOgamlONvOzC7LuMPcdBgQprOC7gRmN4D1v-kk3fL8VArzbsVmnz8Zt5iP3dyKW_6YG8IdarqNDHcxB_6LvifVTBd2GniUCigYJTyaY_wqRFXm8L-2Deo4U9vJtdQEZbaAPmH_tKJDuKDzZHB5eW3ApMqznBlnfChndtpaeWKGkqpJ40AF6a9WydSbhdF27IjsxwKS6zT7pQ_fx_akVLIxsikx5RyzYWImYLgQTfEreNIoPt4MnYzRatiyukbjyklve9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
کیت دوتیم اسپانیا و فرانسه مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99860" target="_blank">📅 22:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBRAbLmT4ICBZT4Fj8dve-AyDkEJJ_jrtwqDiX0szsXnXArMhmramo6ImUUj_pHolSWUDmUW06VQuAAq6FEns_stejx3IF8I4XKYGsW3CtgSQbXlrg4V5n-SS7Ftt0fIOeuZEfQja4zb1-mK7nxLB0DnJXK924BHhbGtML45T81gNhCrCyRbFrD3NQVoadOthvFMxytWP8PAQ-_u3wWRfK_usx-ytg-IVgZZQphCFlveOBQNpYeBN0tSuP26Oo2e_Gms5BOlz2TZmV0hjhcVpNmK3dkIsxm02rBuQX_-aJr-EVwj968AOuLNLcN_qhViBJMSHr9nkNMrInY6ncqpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دلا فوئنته:
هنوز لامین واقعی را در جام جهانی ندیده‌اید، فقط منتظر بمانید تا طوفانی که ایجاد خواهد کرد را ببینید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99859" target="_blank">📅 22:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1daixLyqf8gB16zaj5R8bcpDDiN1_i6SQgQAmD1alzN44DkxUoe9JIWxgA7HL3w5hGQPvqjsUjO6-C7vwWs9V5Z0TNe_l7ZS9JIlenef2fl5s9VJKnQmK8Ygh_8lF5DDyrvMKwZGizxj3jAmKogzI0d5IO8pjXBvGCwsBfIy_VxajCJ6WqljYu6it1ZqH-YalOP24Lp-by6qcGLMxdRr3GPUbODywTd6yJak5NOuCb5nq-4OEIcdLyctVCEVbOAIxg3Bbd8RS3oesIUqJI0gfUvZYujlVUzJbbOTaXKF6CVObwdGVyjPHx9A2173jCZr6zUeRGoBkgvu8SB9oOclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید معتقد است که اگر انگلیس یا فرانسه قهرمان جام جهانی شوند، توپ طلا باید به جود بلینگهام یا کیلیان امباپه برسد. آنها معتقدند که این می‌تواند شبیه توپ طلای ۲۰۲۵ باشد، زمانی که رودری به دلیل یورو آن را از وینیسیوس جونیور پیشاپیش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99858" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
رومانو: آدیمی چهارشنبه در بارسلونا خواهد بود. سپس تست‌های پزشکی و امضای قرارداد، همه ظرف 24 ساعت انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99857" target="_blank">📅 21:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کانال 12 اسرائیل مدعی شد:
ایران قصد داشت ترامپ را در جریان سفرش به ترکیه ترور کند. اطلاعات خارجی این توطئه را کشف و به مقامات آمریکایی هشدار داد، که منجر به تعویض هواپیمای ترامپ با پرواز برگشت او به واشنگتن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99856" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MouxN2bbdCHnAeTpTHZQPKSKNERHWyoWb7jjv8Df4Z4Gd1q2XcROIi_8FRMzza_ADXnwdoDDSs2h29SV89_p4q69EW3I-IsqWinCFRvuXrO3cbhezv0jw1Yin86MdgExX1aSSwqTKFYboEwX3JmEggzUFQgMePuiWqQFxSzgtd9-70wgIMVcbPHC7aP5gi1ScMeO5obRNlBaX_mOhRRrD-057kI_xwX1zIoWbskKr1NmFknVlhxzxC7ciQm8qngjdeDQowYiA3LHxqs9N38wFUgvNHg3a0PMSYYofNSgvhY1FkpWSrBPxj1mQTFHOFBSoyRgXVai3uH1BaT4uZR-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
#فوووووری
رومانو: فران‌تورس علاقه‌ای به تمدید قرارداد با بارسلونا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99855" target="_blank">📅 21:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwIUcETHtMaoc7paj7reqbRmzboUMdJDenBrKrpj9ihmQgGTRS44nRoIdf_3UOdFt3eQNVraJS3HXKsUXs4YBNr5yNCJir6z4eGvsGeY6BWJUvd43IL_-NCp8k5Ecj0qrGNm7S8ZimjD5Hdv91BoqKXWF-tFMmvv1mmVNtW-njyD-up8F9iXeTZmptjrsaew2CWknXRLM7JDCU5JoxLO2K3LG66T02VRp8QVN3xXPLMf3MlLp45fmXQuIKEIJLyE_MJ1HtVuTlaRDNHYhjEcPj0YJAxlqbFY72zpr6yPQKSjTMabIGe34bJjYuJU3CzRtODDw7wjf0SpzHdc9tPmJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#
فوری
؛ رومانو: میسون گرینوود در آستانه عقد قرارداد با فنرباغچه ترکیه قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99854" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMmrLamz2PKKDv8mE2pa7A5jpPGPh3tm90Bs6-k97q4lTEtdfBkvvlB4pFlNKe5nyncvf2Df4ewf9x1BGSFXYvavtoPHYEiP7cxV54ysR54h3_P-Ve1YZnUnwTUvqo8VAzDLGD-Gg7UpbgPWvRVdKR-YHTcXBeSjyFXh9pEyaffLJ142iK1YzFX_5-bT4jsw8fCB3VGK2Eh2_-T4nPeBONKIuklblStLpUTzhEUJERD6QY5Vp1tg9BQY4mrofrqQPeGwhsOAlYa-jDX9efB3tKKI_S70amZE0LPTksyDsrsXJW-eBUgQkMjps2t4cewT3X24Ar3pgTfhRj6ndv56JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوان لاپورتا مهمان ویژه بازی اسپانیا و فرانسه در دالاس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99853" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWVoXIpD-fGti9Z96FWqtCeMaSEQiQP_4SKqgY_aOnQiYqfjgXKS9vWvA2oNKa19KOe7WxRYuUG1xkl2go_0NlD1cwIPk3OigstvMfgjGQpjdGOhv5o9Jc0XAAJ6ifSZPXbLPOJnwBCg1VCBdIJw-oq8N5XzVLevA_Iy08iFdyhqYO2JuYUS1-0nCjuoS-iNyOBaHsgtwEcNCnPI0MQe-5vrjydc3dIKrlu9b7d6ZyL3P_81MI8CjbZucyTt9R4SDnCqQLc8oTOIHL6e2nG6_OlOEBiErrgh_H4BrXDTB3L6XFmCUmmXoA8ClbQPwdcVZ0qKKf9Jn4zzmPGKGHipMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب احتمالی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99852" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXuJsauhhhPrwYskKXiXeYe2bk7anASSPr1jgD7JhOdfyd3LPvemQ8N9F-MYmfWWfqMrLyVhLQJkwJ_V53sIcKO84k2AVExHEKAZqzjrkHqMkBlW5Gr8XvO3CLoZ_C_CnKKoY-NcqxtN_o6hxgQh1xxQiHLlRZIcvmUAWm43G7fk5-KOH7kzov1ZKQHXdZgUoDfwfBJqukc8nldQcumJ3zhzNZzIb_sxYS1KIBnQGOZVq6HDYgzklnc3E3ewYcLyXVCpLBv48wm45-py-iakG0tQCojQMKsGtvqhYORb406kPF-19ymuLX0e69R8Tj8k_8xqyaiXFzrDkrJUOyPUHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین تعداد پیروزی کسب شده توسط بازیکنان در تاریخ جام جهانی:
1- اسطوره مسی، 22 پیروزی
🇦🇷
🤯
2- کلوزه، 17 پیروزی
🇩🇪
2- امباپه، 17 پیروزی
🇫🇷
3- کافو، 16 پیروزی
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99851" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99850" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99850" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nkTf1ygzfoacKlU-5aQkO0SRPcuFlfXT3gxzp9-QMZiB9gbNQj_SdKjtkQzxH4zdtuwk7dab1adqSjFZSamH_AEtGQ4vWVcFwaJaHNCg1-0bKwgKGwhZsDm-S3dGYPT7wfW6GGLAvRcPgmf0S3KhBlmyYhbCZRroy4QLvIvd0yhKE5IGDdUlbM3BHS3vWi_bzrf1q8OUSAUQdZVyA2ZoGttsdJ6KoWaLzZeeFk3LDtHUOT-0zEJtOePfqVUQsz6ISj_hy7FTqpPcB_-f7SJuvIqmtslryMr84jnteWj6qubzxML7Hi87RKBnqpV4ZVPeh9V-jMMAunabTZwByhkKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99849" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi7tO_g9jJD9HoA8FX0Wlfi74BgtZV3Az_sEU2GmJJVDHuwrKLOmfG7W0oDfIi1HrDxS7CqJUag0Eff5Ptk3gvN1eUgeYRzkfm0iWlgA7hI8YrI_DisSScJg20i-wUaetdAyYDy6sL_yCF_nXTlwBHsUyrbjtcYm3OGUl1jSx3elj8SyvCREb_o5upatXlbrFkT-RtptJ6hsjSrp_5hsypPQtjOYtFiPp_dXK9gC_GXqQK8EqRZVbIr-r_fBEWkxyrqMin3aosYGAEVP3KRN6MIDd77rHX045w2IoQlbYw6ffYgCPne2ttMciDLHQXRrHEQe-ngNqDMN84zZkWy-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فودن و پسرش تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99848" target="_blank">📅 20:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نروژی‌های دیوانه بعد از حذف جلو انگلیس
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99847" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMG87x2zPW-od7fdtCCX6p7DDocWCL-ciPj0wv6F-4adI5E1Af8-W14MJN1FlPh849khu1svCCLu_updmHLwhSxgOrUurtBEN1gY5L9_xNt6WnIQu9Onwdx8LshlN1JXtLWAJOlvItFoSaDnzS-M1Rkdpi7ypi-ddJgu-F-4JTGXHQU60qqyvw15yY9Ox9OH_7c-sIWXDn9ok8gIqDcTIBqxoY5LBH0Pc3QpKlOJuwNm6AUTE0gkEUzYHvywZuhcnJATOI_ixkqmijvyFbd3yD0QwP4UXb5HpNYvBwOZtpK921CEFCGRlv86bhsEFrhvD-1MdgHABBSmWhOWoZICTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
یک تیر و سه نشان، فرصتی متفاوت برای سپرده گذاران؛
از اعتبار یک میلیارد ریالی تا قرعه کشی هزاران جایزه در جشنواره حساب های قرض الحسنه بانک کشاورزی
🔻
جشنواره بزرگ قرعه کشی حساب های قرض الحسنه پس انداز بانک کشاورزی با هزاران جایزه ارزنده و امکان دریافت اعتبار خرید کالا تا سقف یک میلیارد ریال، تا پایان تیرماه ادامه دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99846" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdXX5KNZBxHDQeaAUHCthstJbwtFC3CNB-ODvHm_T3tZzNMWr6Xlu5OngQYnvl_rrz8YdZnMn8Ni-00ma9xOcg3dweJuzDK317zHQG5wAgFVeUwBXUcfVGS0C93Xae32QniCr5OxApgBTGuHaNbmI6CqJ4AfmW3mpZZo9SPM_3Fib6MbkHM8HHKbhtQtjYVtZh4FZl45_rE3dNLAzz7q6-_IJuP6Dpbby05mDIKG1-yeRME8ZA7FeUOh9eg0BLABllm_OOHsX3UK0Aj9ibbco2CuhmY_651t3_reA6BvK14PuFPWKLx3yKDL1iJjYUnrB9F0eaOfaHhdDb66lD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
چهار تیم برتر جام‌جهانی در ادوار مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99844" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه به قشم در عصر امروز خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99843" target="_blank">📅 19:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حملات آمریکا به جنوب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99842" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
رسانه های عربی: ایران با موشک های کروز درحال حمله ی گسترده به ناوهای آمریکایی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99841" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99840" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99839">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=avxmIAEqZDAD9zOUISgWEsZfZnqTS1ezembzEWkccZxllcmhAD2RwU7zyH0_ifgALBfaKqiwL-GbBmGXHTJ0FTU5org-o5gsaQAYUKb1dAbdFWF__1XTIhiC5GMNZFpmyG9o8HqKnJSakPMZSKxjCGU7qyMEHx3MYaTXrMCSqkVzic25LySVwiMzg4D6-muHjChb7uuyE27iocSNZcAo0Ky3hF_4vR9Yo6mOIXqWZSxLdtn8ro1716zLQZFFQF8uT6ggWzaw7iUDbeyGDvD2XNVufh14QeDw4NFF5Lc6gY3Ay1uWGIWQuhsus1uyGSaz42rnu4O2yOo3r06-21SSSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=avxmIAEqZDAD9zOUISgWEsZfZnqTS1ezembzEWkccZxllcmhAD2RwU7zyH0_ifgALBfaKqiwL-GbBmGXHTJ0FTU5org-o5gsaQAYUKb1dAbdFWF__1XTIhiC5GMNZFpmyG9o8HqKnJSakPMZSKxjCGU7qyMEHx3MYaTXrMCSqkVzic25LySVwiMzg4D6-muHjChb7uuyE27iocSNZcAo0Ky3hF_4vR9Yo6mOIXqWZSxLdtn8ro1716zLQZFFQF8uT6ggWzaw7iUDbeyGDvD2XNVufh14QeDw4NFF5Lc6gY3Ay1uWGIWQuhsus1uyGSaz42rnu4O2yOo3r06-21SSSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
وضعیت پشم ریزون پایگاه آمریکا در کویت پس از حملات دقایقی قبل سپاه پاسداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/99839" target="_blank">📅 19:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXP0esg629P5skPBRwATsFyZZc31NcQ79bP6opgWO4AdJ9SipAt9DrgI-JtMTsEMP8v2GeL3M_TYEnepnag3zm0QivX98FJq2vWF06Pl0UlZH4Ig54aIbSIemHBL2HDMPTMnzFjzCkgs_YgjU44cTClpt90vqOCLD40HUK77LUc7DULn8Js3DXZW-AjZ3kLGYSw1tce2g4uwG4jS0bTNKhLEEg9hCR558RLnoi_UzsHaJuPa-otrWVvMDEZ2V0lZfYhve_ayt4Xeyqd1siLLOMoTYBMuq4g6zJIvUVVWeCEm2znzghzEO_Q5ftLG5X8y_FhvOnH3bph_rOG3fW2RXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaC_VxJUZj8NPvXgSA1-Q_6TKQ0GXP70Lq409_3Y4eOKpNzQJ7teZxDoN1qsL7IInNjBixyNY9CX3cZR6pUR4ciVYDDNFgPQElCnFV1IaksCaZkmWelnvk88uYaO_8KfYh2_eD1QYrlFTMTVl2eVC87SDRG7i65TOqgU_2B4JsmdXJWiQ3KXqOS_BKt5a17Nq6Wf6EhuGxd34XVsjgRttb_zmlTPZZ1ogLQvWTHSt8mt8cUlSne30E7vPKSnM0ok-NpsYtnuubHUdI3qUUHwbFE0pwHwBZi9l3OUApRpc5D34HK0Epx8pOJzam1UoU4jg8J-9TqyCddjUVO9671G1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه افتخارات تیم های حاضر تو مرحله نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99837" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er-1EeXNMIqYJhfYmSh9yRSRXbadFfvxPoAXX1cbAqci9bxjRUBV9alufNWkthmSieEq4OdnDxTmYKJ7WKrhycVpr-IrFWvBKgnyICNOH8uIPexkRcu8B3c5T836gWfFV0qBXq2KU_5haxxZCkuDpehT0TJBkGEbr94AXrz9maddq1GtXQzURhZWnuIaRVFlbRmuxnNwqS3FcUnXVNkLUIQw-foOjq3B6y1z47Ngb1ET2Haj5d5RKCoLrB8f2zb32pFSnqwmYucBtgTJs3CnYHFDqVyYENp6FdgzsLw1fIoALjMSeaVrC1VnEOPVdR6SiCk2Zs_l14mVuLkDI_7m2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
بارسلونا و اتلتیکو به زودی مذاکرات جدیدی در رابطه با آلوارز انجام خواهند داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99836" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN6ejzvGpezPWeE3KRCqN1m8JnqnhLdA7jY0vuV-jm_-jX-P834RYmbvDWRGgu86Cq-YQacpAFiH0N8OaWyxDd5xKphIM_o_ogY7CzJCUJZCRNeyvKAocnV9oMLrVlW49t0HDbmus6iDW8WBy4sZSB_7caeMTCJPFoKbYStFlGSdR7EJqKSEU4EinFZN3fuDgXaeYXK3yErfeWqic_E2Y9tWH4wD86FNVHZJclsywQTPfxlih3zRZ0j26nfAR03D4gcC5Tc566IlfD6YtG9dXhSHhFPiwo0ZSPccvpEIdGXEyw8G2gup7UcyDeGiSDWIo2Svr-rVyOM_-CedDdUdTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99835" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCQOn9IdPeFOhu-binJFzNqATBOsatVZ2o3Yg3WlhWZENURmNSxIoup8gNCdOYwIgUd06L27QI6rMEqrP54kHGVLsIL6GeU0ibMEZDKA0QsjL4WqU1Xim6YMO7lxYWaNZHspG_6IEtvxHZDsgT27Rxw1r2e4FGsozHRp4erZW6j6XJuDohO36Nno3nJBEqOlWdiJfyR-gBVCbL89OeIzPyUKmOLEzFuEPOYoz7sccPR7OmGo49J3vJAuWy2Vs7Dh7iE_p7NiVbHriXwqzqaWaP1_4pffLEo6bltKp8rMl2wNjmI8LiMcicWsPwdNJK4Yn5sk7EA3eH9NyJHuERJ_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فوق العاده رودری:
لمس توپ: 712 بار
مجموع پاس ها: 638
پاس های صحیح: 597
پاس های موفق در یک سوم حمله: 170‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99834" target="_blank">📅 18:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04227938e0.mp4?token=hd_nmbdmUa4Gm0kHCwk21gFQ539wCShIvjunUc-pWj0ha7CE5zQhXTuKjxMfhztpim6yCD98e63bTqv2-lJu97KcZ-X4aDNH976u2IGEScUxRvjYh7vyW_gO69G19wYqBTWE-jOK3-hG69as9e80G8VnMN2ntJtDqQht6xdsYPYnP9bpQuG5qBKQBP6ZoRACdYLBgcseOOH0Z6-DMjEvsczOZdJNvjtIb83lpP-eSakrurS1b7pVHUIF03-v9t4L7nYwpg4_RALXgpiFJJfk7JzNchZv-l138GdkT1JOCkYxznHnvjzWLnqjnHOeTBszDO1LSDslQok2nadLiwUsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04227938e0.mp4?token=hd_nmbdmUa4Gm0kHCwk21gFQ539wCShIvjunUc-pWj0ha7CE5zQhXTuKjxMfhztpim6yCD98e63bTqv2-lJu97KcZ-X4aDNH976u2IGEScUxRvjYh7vyW_gO69G19wYqBTWE-jOK3-hG69as9e80G8VnMN2ntJtDqQht6xdsYPYnP9bpQuG5qBKQBP6ZoRACdYLBgcseOOH0Z6-DMjEvsczOZdJNvjtIb83lpP-eSakrurS1b7pVHUIF03-v9t4L7nYwpg4_RALXgpiFJJfk7JzNchZv-l138GdkT1JOCkYxznHnvjzWLnqjnHOeTBszDO1LSDslQok2nadLiwUsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
ژاپن این‌شکلی داره فوتسال خودش رو گسترش میده؛ واقعا همه‌جوره باید حسرت بخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99833" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=E6QjqupqB3-8Bn1cLXhvr85rPIASYMjsPO6iIapPXSjAW05UoS63RaOvbrMHpGtcAFUStHnpvyJq-YPNoDrBuWrYyD7fphNsjG2jdxjExPicyf6XFeFrYAjM9h9V6t9DcUqg7vRDsspuqV9zzCyQYRletzQnqe38fd5Hhk1-cGGBw_RWhAKZRZSJL-JRMSY0Acf3TDWk7sZ00NhAc49U8CA88hw0P4E90W_4_0rrBvmGeVWKartpDCqRHu5LnAM9j1HGMbuv8KrYyx1ZvdQYlOEqRWJnnjK-QbtVmd-PAtgahB-4wgbf7q9O8tdHkl4NCx8B8O_oiuP-GWOEa3XQiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=E6QjqupqB3-8Bn1cLXhvr85rPIASYMjsPO6iIapPXSjAW05UoS63RaOvbrMHpGtcAFUStHnpvyJq-YPNoDrBuWrYyD7fphNsjG2jdxjExPicyf6XFeFrYAjM9h9V6t9DcUqg7vRDsspuqV9zzCyQYRletzQnqe38fd5Hhk1-cGGBw_RWhAKZRZSJL-JRMSY0Acf3TDWk7sZ00NhAc49U8CA88hw0P4E90W_4_0rrBvmGeVWKartpDCqRHu5LnAM9j1HGMbuv8KrYyx1ZvdQYlOEqRWJnnjK-QbtVmd-PAtgahB-4wgbf7q9O8tdHkl4NCx8B8O_oiuP-GWOEa3XQiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ماجرای تل سر یامال و عبارت EGO YAMAL
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99832" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glK4frOVLcab7czNyHD0vs03aCMmorhcjBoB1TOaEyZdD08BqLxQQbdeMkSz-AelYd-fSaczkzEcg-uwZOFQQkOiQEleqFuydZUDd2G1hSqIPrv3HSOUihfAca6uLXZuofgotuY3BPIB42hwQkWflEgwpEPe_YASt8xmwBiUwT9Zm_WRVBkr1xhLCMFDqgmB_qz9LI-Oknn8injnfvQdSCL-YbmXj3NzOY5-iUU30O_Q-ESqPtF50NYFjAWD5OcxvI_cXkt8czHMvz2rjnycRlpnlBe5iHRxrMj6_5nEiGzk0237T-LuCiRgIkjVks1X_tzhuoLBeO7mcZABleXLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
اسپورت: الهلال عربستان اعلام کرده که هیچ قصدی برای جذب رافینیا نداره و این بازیکن جزو گزینه‌های تیمش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99831" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=ALxuZ9Wfj1ZtOmbXeIkufrR39GffkyCeK2Wf9gHXPfyDJejrs9zK-loPV2B8BYHB3Tz-Frqxf98f9KqD7uApMeYcW54nB0ut3ptofuZ6X_z0o8v9Ny2CFXU2iG-rOne-WfVGyb2X6IfEeRK42UJORH80bOLkNifSBcvvei2MC5vJmxKIWT8-YwPghXgPlPHOREXUvf7IA0GO02qVPkAFQ1ob6lFEFeICWaeRbvXdQ3GK_igLKmwdb6qdXX90serTQKnE1jdugrxSyUUkM4sM3I-RYd4WhSjxe78zADIZHnKd1Q9VtCdjfL-T_wV5EzJD_cM8zgVtrb4xGvzEWfUT2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=ALxuZ9Wfj1ZtOmbXeIkufrR39GffkyCeK2Wf9gHXPfyDJejrs9zK-loPV2B8BYHB3Tz-Frqxf98f9KqD7uApMeYcW54nB0ut3ptofuZ6X_z0o8v9Ny2CFXU2iG-rOne-WfVGyb2X6IfEeRK42UJORH80bOLkNifSBcvvei2MC5vJmxKIWT8-YwPghXgPlPHOREXUvf7IA0GO02qVPkAFQ1ob6lFEFeICWaeRbvXdQ3GK_igLKmwdb6qdXX90serTQKnE1jdugrxSyUUkM4sM3I-RYd4WhSjxe78zADIZHnKd1Q9VtCdjfL-T_wV5EzJD_cM8zgVtrb4xGvzEWfUT2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇳🇴
هالند تو این صحنه خودشو خیلی کنترل کرد که کون سورلوث نذاره. احمق اگه پاس میداد شاید گل میزدن شاید صعود میکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99830" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=QR9qab0Mc2NXvtKx2Em1ejjZ0_bC0rhEbdsy_1DxzeiEpkNpNexDpSH4s5pfQ-ivJ1tCOHx14qRQS29HRBfuRUmhbDHhaLtVC1kZRiKfOO3FON8NXeMYJBZsHkhlCmipYHA7P29JHiROYFkqFLgS_3P5DOk5P6gKwTYcFNltZLsHb-NVl79qYQk86Z4Z4ihd6c3EWV538pljmVr_1lirnQJTl-9CmakouWHe_b7iugAICihg8qPaSq-HX-8CS6gMGsbranM_GUSUfeQy6pVNbRyDLomPXc6HuVD7oDgeJDG2R4jSHA60_eSy6zknTzP-eX2DHXOcDT5hyumEekfPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=QR9qab0Mc2NXvtKx2Em1ejjZ0_bC0rhEbdsy_1DxzeiEpkNpNexDpSH4s5pfQ-ivJ1tCOHx14qRQS29HRBfuRUmhbDHhaLtVC1kZRiKfOO3FON8NXeMYJBZsHkhlCmipYHA7P29JHiROYFkqFLgS_3P5DOk5P6gKwTYcFNltZLsHb-NVl79qYQk86Z4Z4ihd6c3EWV538pljmVr_1lirnQJTl-9CmakouWHe_b7iugAICihg8qPaSq-HX-8CS6gMGsbranM_GUSUfeQy6pVNbRyDLomPXc6HuVD7oDgeJDG2R4jSHA60_eSy6zknTzP-eX2DHXOcDT5hyumEekfPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
نیمار بعد حذف از جام‌جهانی دوباره رفت سراغ عشق و حال و کار همیشگی خودش ینی پوکر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99829" target="_blank">📅 17:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=eiyDUQ7HB_-vtBFZ1kiWomO51dzKbVDejyskmHBI6YY7bhvtVsfJbrt8Ba27Kuadgy1ph6jyPA4bqCZpFTy8snCzu9CKKTYy3rSVwxuzpHlXtzlDvTjbeGDQdSmRJwlOYQEZOqfB_1ieoM3RnTRYOHNBnGwQ2VJWXUg95vxgjGsBZ_4rmi-7vncRHp0Gj_fCQ-Pjd234yMRO4fq9aqtwS5bBLQRHTqP2ZWGdf4PbAi5GkCoVOWLy9YzCXvcOvJpwjkEMGvBXic1Dcp_ZFnFJHvSdKtEgmEK_10niRJVZxw_mFhnoUbQbHicP2W8Je1pDJVPAgrZpzeVNyRmp57HRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=eiyDUQ7HB_-vtBFZ1kiWomO51dzKbVDejyskmHBI6YY7bhvtVsfJbrt8Ba27Kuadgy1ph6jyPA4bqCZpFTy8snCzu9CKKTYy3rSVwxuzpHlXtzlDvTjbeGDQdSmRJwlOYQEZOqfB_1ieoM3RnTRYOHNBnGwQ2VJWXUg95vxgjGsBZ_4rmi-7vncRHp0Gj_fCQ-Pjd234yMRO4fq9aqtwS5bBLQRHTqP2ZWGdf4PbAi5GkCoVOWLy9YzCXvcOvJpwjkEMGvBXic1Dcp_ZFnFJHvSdKtEgmEK_10niRJVZxw_mFhnoUbQbHicP2W8Je1pDJVPAgrZpzeVNyRmp57HRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید آوردن تو ویژه برنامه جام‌جهانی غافل از اینکه دوباره برامون حماسه آفرید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99828" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=QBZspxZfUq76d1zhrF-XcP1zgKwMA5xKfWVlUGEynC25ckmH1M9QzSdy9zwQRW2Q7o_GDTgR1DbEDeZminpa-gGzpzO8KRbCr3GK4Ikel4gwBo5mIKXyT44ipqdy7pn7621G-HnehqjbAjzaY-e4yc40dDj4tFb4rrZwSJrriwmhRbGJQ89dTjF8nLnFssIOYuvdbpQxUxfkpB7XI4oJcahGmgef8yvDA3M-649IJErtmwJOd7H88sj0Yd1wEXV-7S3jkdp7OoBfcJaZ8PTcGnvtgBlS_Dg7zGnsKIqs1kDkNT-wr98w3g88--SqQ8nFa2Fyp-oyzKm0FiWksq0I1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=QBZspxZfUq76d1zhrF-XcP1zgKwMA5xKfWVlUGEynC25ckmH1M9QzSdy9zwQRW2Q7o_GDTgR1DbEDeZminpa-gGzpzO8KRbCr3GK4Ikel4gwBo5mIKXyT44ipqdy7pn7621G-HnehqjbAjzaY-e4yc40dDj4tFb4rrZwSJrriwmhRbGJQ89dTjF8nLnFssIOYuvdbpQxUxfkpB7XI4oJcahGmgef8yvDA3M-649IJErtmwJOd7H88sj0Yd1wEXV-7S3jkdp7OoBfcJaZ8PTcGnvtgBlS_Dg7zGnsKIqs1kDkNT-wr98w3g88--SqQ8nFa2Fyp-oyzKm0FiWksq0I1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
صحبت‌های جالب سیروس میمنت بازیگر سینما نسبت به اتفاقات تیم‌قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99827" target="_blank">📅 17:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99826">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJPIwq5b_0rYDjIFJPDLh3wwFbWWtegTGOQH73cHglqGMtWT1XKOI5U708FuVUmuSxGvAmKUAUL3lxgEjjPSBEPsm2gqBhield2JpilCk831jM5yUzMh5htMnxr6dzHa1tkqe3fLha6UEtU7ywr4RJVFaHmyjzhYraNRr3dPU2KBBi2QogGrpkK7PHgOkUj0_pjJWAG4Av-WxjmPVCO3oE3ur8nbGlrLlglv2aQVbhp_8KRojVy62TM8gYXdIpMvoavBVP-B3YlijvwMDYEU6imJMUOFoOz6ot7G2LdC7hlv1JUsOnjC3LjYyfZBb4e850_O4xmpY9DPUVVW2HMexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
ترکیب منتخب مرحله یک چهارم نهایی جام جهانی براساس نمرات سایت هواسکورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99826" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99825">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
ویدیو فیفا و انتشار تصاویر ثبت‌شده از دوربین علیرضا فغانی در حین‌بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99825" target="_blank">📅 16:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99824">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=HWCXMTuV3brkTMpKGlC5QWzJUC1OFGbYpGGA98g1EGMPxy52Op4Z-0w0f0QeDgbG0-P3-Dl-QRnsfDe2iH-B91CKr8Itn7hGf3ye1DvuZ37ANTiG62Q7MQVfW64QMzWDoE0JJyVJiPAlAsb_MjrKHiZQdZrXpU35mfhlpRVXP8-KKt6I_1q-DIRrWt0dMmimniXZa7v-QtaogY6N9sEkdljUr6ga7kM3lBizgjz140aqcMUDScZh3fiOmEUGmF5wvXibtnnUcWFLXmY8Q3NY9VEAnP352ppShvSGPgPpDN9MNaP965Q7WZW48HqiCYXiwryQWEsrGXTrDH9pABoBnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=HWCXMTuV3brkTMpKGlC5QWzJUC1OFGbYpGGA98g1EGMPxy52Op4Z-0w0f0QeDgbG0-P3-Dl-QRnsfDe2iH-B91CKr8Itn7hGf3ye1DvuZ37ANTiG62Q7MQVfW64QMzWDoE0JJyVJiPAlAsb_MjrKHiZQdZrXpU35mfhlpRVXP8-KKt6I_1q-DIRrWt0dMmimniXZa7v-QtaogY6N9sEkdljUr6ga7kM3lBizgjz140aqcMUDScZh3fiOmEUGmF5wvXibtnnUcWFLXmY8Q3NY9VEAnP352ppShvSGPgPpDN9MNaP965Q7WZW48HqiCYXiwryQWEsrGXTrDH9pABoBnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👀
عاشقانه‌های حسین‌ماهینی و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99824" target="_blank">📅 16:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99823">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=ORtygYWDjp7rNABjdhu3mGKzaC71MJmZNhvizmBONBP213Cjl33bHwfNFoFDe7LHY5wJtn1O0jzqrDK4e6WrGgGa5cj2MyrL-qGwzdmCyNmBZeX-1bPcaLd4jPPwKo_5o6P_NMJ5FL53WsJhnxHgnjJvppYFpLbwST6UQXGjUZD0TUmLVyIZ522q6CmV62MQLqevWU5wFSy-4VCZPqhtJRPOQzY9CV3MvGONgvPoxiqZn5K3wwc03kv82elWMk0CCvCieHg2ZzYMO_5FMdk9-xF0AefJAduuOsOmWl8Aubea2n5138BUk_nopt2Hs0aDZEqSdlHaGYLF2eYgQIdT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=ORtygYWDjp7rNABjdhu3mGKzaC71MJmZNhvizmBONBP213Cjl33bHwfNFoFDe7LHY5wJtn1O0jzqrDK4e6WrGgGa5cj2MyrL-qGwzdmCyNmBZeX-1bPcaLd4jPPwKo_5o6P_NMJ5FL53WsJhnxHgnjJvppYFpLbwST6UQXGjUZD0TUmLVyIZ522q6CmV62MQLqevWU5wFSy-4VCZPqhtJRPOQzY9CV3MvGONgvPoxiqZn5K3wwc03kv82elWMk0CCvCieHg2ZzYMO_5FMdk9-xF0AefJAduuOsOmWl8Aubea2n5138BUk_nopt2Hs0aDZEqSdlHaGYLF2eYgQIdT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
واکنش دیوید بکهام به گل دیدنی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99823" target="_blank">📅 16:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99822">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=hwGocUEmpdMqC9tqs9vT4BACPvUP5GC0EhYuRVUceaM51mvmvoEGuIwsVXUQEPk4Lw_af8K1pDQ_Ue56NjZuhBc30ExQ8IxSN77JS4jtarT0oylLxjNYp-eWHmUQbUhJelAw3fI2vY4_iM6WjhLZcsQjE0lH54m4Y737vEeZBrLBlcdgW1QyIcUMVHg_ZkCur_7WBdPtf7okSOulkfWtyntv-kYVSiU_JBKWcp5ka4bTwi_XiujbE4N_Stan7LoowyufBb_AqijEONUiG1U3U9QNUAkTe8E8t_pgQCsq6Nh5_6swcFe8S1GdjpZm1scsCm3TXmfstYRShwJAJiwIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=hwGocUEmpdMqC9tqs9vT4BACPvUP5GC0EhYuRVUceaM51mvmvoEGuIwsVXUQEPk4Lw_af8K1pDQ_Ue56NjZuhBc30ExQ8IxSN77JS4jtarT0oylLxjNYp-eWHmUQbUhJelAw3fI2vY4_iM6WjhLZcsQjE0lH54m4Y737vEeZBrLBlcdgW1QyIcUMVHg_ZkCur_7WBdPtf7okSOulkfWtyntv-kYVSiU_JBKWcp5ka4bTwi_XiujbE4N_Stan7LoowyufBb_AqijEONUiG1U3U9QNUAkTe8E8t_pgQCsq6Nh5_6swcFe8S1GdjpZm1scsCm3TXmfstYRShwJAJiwIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عیش‌و‌نوش محمدصلاح در کشور مصر بعد حذف شدن مقابل آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99822" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99818">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFy6lxjmqQoQ9AbN2HHBXZhgdofc_X7jljE6LHSEe3sUw7N0D5N-6B4itpU_3fM0mWmaUk7vT8ocilT7TSkwzH0KogUA9_FCzJM1XEPPJYKSBKvv3a7vKhM4IkQ5Op61PE4Tp1KVHj19Ntlg_WDZZgprvh0HvYPI-ko99WF-a2Z6UPIl34H8gRjKy_HUGR1MzWiq82PBwU9Mel6sts3LsKBy1Peum4fGa5rPsuFzqS8_7Q1o8-3h1Ni3Ta4IKUvRPYFczGnRhgPOpNiyMqJGBcP95fq2MNwqqkfNkP7YDcA4iSrx0OD8_9xdKV1rumkSAavuYCHhh9teuT1ivCDI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsVW90v2CV1xbyxWKbzpPygK8M_5rOBv0CXDmcQalxUR70Ssxzwb2QtRq_tKFEIe0pQzDNkawthH_iGdfQdnf1E6ZpU5utJP8t7DsxnoYvKz8NWHQt7JUogOErrxTOEs30WqqND936UwKKcY13zRxPrtsp293H4CvA_-KHP7kow0l0ys8wYWYsFYLP-ox1jyY9NP3CN_9CInXXwcbh6YjKSNyvzJvWR3bRuXdWKNJDn2qZfOqsgU2QlfIyVjRFPejm_0UMTHJNkLB2q-DFj2MyrdaxS1mf3uaCRqJ_0qFBEXAU-KgKBVIy0zGISf-Xl-Bh3uTtYRa8dNAObEQrRGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUTfL2APCpGXOMtY3oLKWFrrrrMA4-UN5RKxQiMCi-cgiGIn9u4QIGr8jeQjn4Qc8IiUb3OWb3cWy4va7g7pEci_kaybLSyM86ERZXqSf1eXWi6Qn1fHSpSjtl7XbP8sWxN_oZzB7bF3jOQHR18OHmzBocafXKzTy6X62-oIDH1h63_Smw7ASNRB1IElAysT9NKYK_Hbkk7rtCqVrLMRb8OvFPRSo1jL-skjNHB_j3r3YWwcovBh_A_3HV0btqrA5uY7x5bErmhH3qFu10Mj08M6vTbcl2TW6Db-g5r-EB0LHSNcOg-bjI6x_w5wy-cGkWWs7vzxitO4NtEzAjmtXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ey71ci9o7PXglccVfQx1FKFG0ZCSuW6I2rDTxNkT2r-m09N8dDY0U6-KD-8Js9_ndcXPYQ4HQ3rMyJA5ms3e0T2YotlA8T71HIuzLw-R1yZr-lS9sh2KPNV34OWmnDevBpI23FaLgD5J5B2TF-_O5hiidzGAf6ujCpNmIP8-xJfjLN7a113fEj0gWpXPSnCOC0ip8pLeWoqd1Q2ceFYKsJq6js-DmhLaCsIDM5uBqx-B6uezxxHz-Os82R2iiJ77w1JgWEf5HQpBZietmrhj4x9DohEPPvxLR9AvTnWGPRwd53bWh4nOgw2ZU5gt99yxfGJwxcTWxIpoqcF-r7NTfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
استادیوم‌هایی که میزبان ۴ بازی باقی‌مانده جام جهانی ۲۰۲۶ خواهند بود:
🏟
• استادیوم AT&T [
🇫🇷
🇪🇸
]
🏟
• استادیوم مرسدس بنز [
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
]
🏟
• استادیوم هارد راک [بازی رده‌بندی].
🏟
• استادیوم مت‌لایف [فینال جام جهانی].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99818" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99817">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJKpWDjxRs6ZY_uzcn_fbFFpe3sZCxA6GM-_G-ZcrQSt_umq4KwPbspj8mMMhaBrOn1CG_aUr7TUeiM-1pTg9jNJXZQABgMYfoUZI4Md8HJn9VZgKUs1or9Q479rFwDevqe4yKi3ndkR3HipYxl4JObiNHsyUU9THOb4EbQixyh786CcwN-zTTQ0Igek_ypuFXMMNlAkHkoVSkgIzdratsTTo5_h1GioUYs68DbiENOCeuqp78jKe7s_PNJRCbGe1JyiWFVai5nanhOERdnkVOONZmcIjKNRHc3nu3ct30WaSwkj0JRzAf9PoR9K1ahEoVv55ZlnKDsgIloVUHY1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم ملی انگلیس در آخرین تورنمنت‌های رسمی و بزرگ:
🏆
جام جهانی 2018 — نیمه‌نهایی
🏆
یورو 2020 — فینال
🇶🇦
جام جهانی 2022 — یک‌چهارم نهایی
🏆
یورو 2024 — فینال
🏆
جام جهانی 2026 — نیمه‌نهایی
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99817" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99816">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=J5RDqqt57b0fXOAWy7x3ca2sLlC6q5V_d86yStpLE_Act8LQPe--wNVoR6kUT615EzvMpX7goUJWxe_uiC7cS4uCaV95lRY2lC8kNyWUDYjW8KHQRf787mq_0YXQBw6RwBxsBc0EwXzQOZdGFNIC6jYSEs9wQsF7H3YKlBgvNY5hyYZCvCmQNdn5xmGaNNpM6RiDGoTVY09eaG61uQgHajG1eSxgWhPTM94iPG6E6X9f7KTuqPBFvwU5T3WYCqun_tCw-dWIxcO4gskg9rtHoZVWYkm6WkAxpFPg8m8ioopBFg88WgpKXkqgsdKmtqeGBWv-FL3d0nTiHy3Wv5OKx5KdmzJzuDvi549jTyLUJC3cwQbMvnevvm6aU_LsZCEATMqjAK0lY0eNoluPmnfaoKAw3V5N8gwv82GypmJb5imhpVHlhbobH-VcqT1hnU6q6NoMe05AMCgE-U0B4A55qscAnycMyyDOWMgr_5rJwwYmsV6weuOX0C4ZczLawDQ_KCauPVjp6jBYBbDCBbjXkdvRgnvumC2pLbPJ7sNd6DIrTC7ha86pS7yqgRqyl4wk4PhEFyUyKUJsFZ5FEjN5Trs_yFjVO1LUMNBUcllLuHIXjx6uurG39-UvNC-nwo2d8OX4_6me6GwF3P7mTFyhJJz9iDLWKtQX4kodRinsrBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=J5RDqqt57b0fXOAWy7x3ca2sLlC6q5V_d86yStpLE_Act8LQPe--wNVoR6kUT615EzvMpX7goUJWxe_uiC7cS4uCaV95lRY2lC8kNyWUDYjW8KHQRf787mq_0YXQBw6RwBxsBc0EwXzQOZdGFNIC6jYSEs9wQsF7H3YKlBgvNY5hyYZCvCmQNdn5xmGaNNpM6RiDGoTVY09eaG61uQgHajG1eSxgWhPTM94iPG6E6X9f7KTuqPBFvwU5T3WYCqun_tCw-dWIxcO4gskg9rtHoZVWYkm6WkAxpFPg8m8ioopBFg88WgpKXkqgsdKmtqeGBWv-FL3d0nTiHy3Wv5OKx5KdmzJzuDvi549jTyLUJC3cwQbMvnevvm6aU_LsZCEATMqjAK0lY0eNoluPmnfaoKAw3V5N8gwv82GypmJb5imhpVHlhbobH-VcqT1hnU6q6NoMe05AMCgE-U0B4A55qscAnycMyyDOWMgr_5rJwwYmsV6weuOX0C4ZczLawDQ_KCauPVjp6jBYBbDCBbjXkdvRgnvumC2pLbPJ7sNd6DIrTC7ha86pS7yqgRqyl4wk4PhEFyUyKUJsFZ5FEjN5Trs_yFjVO1LUMNBUcllLuHIXjx6uurG39-UvNC-nwo2d8OX4_6me6GwF3P7mTFyhJJz9iDLWKtQX4kodRinsrBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوش‌شانسی یک‌آرایشگر در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99816" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99815">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=gLzUxV8rcaMqX6pL0bofEI9SItL4gA6fIuZiVFRrh_-0v1s38VNwV4L8_e_XZpJwO1SPduIq6OcEd2bhR755hI0KIRar_sjztpq13_jRGWMMf_oewBJR8hy3SKWn_8XClOHZbtZdi6xTIWzCWY4Bzrt_aXYS2NRqpnEBl42xKolTGHl7dN3A84Ogwmx4RSsqhRuOilTyNCo6V5PXOt9H5ld47ydWwQaUm6iuVGm0g0YsSD0LFfxt9yEQsP15TSc_ch7opp2sG0xL1Q9k0Ji9YzO3h74mPGs8qDgEmnjHIiE8Ik--RkIDCffwJxaGuvaFmUaKQv4wAP9s3j1B2lCpqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=gLzUxV8rcaMqX6pL0bofEI9SItL4gA6fIuZiVFRrh_-0v1s38VNwV4L8_e_XZpJwO1SPduIq6OcEd2bhR755hI0KIRar_sjztpq13_jRGWMMf_oewBJR8hy3SKWn_8XClOHZbtZdi6xTIWzCWY4Bzrt_aXYS2NRqpnEBl42xKolTGHl7dN3A84Ogwmx4RSsqhRuOilTyNCo6V5PXOt9H5ld47ydWwQaUm6iuVGm0g0YsSD0LFfxt9yEQsP15TSc_ch7opp2sG0xL1Q9k0Ji9YzO3h74mPGs8qDgEmnjHIiE8Ik--RkIDCffwJxaGuvaFmUaKQv4wAP9s3j1B2lCpqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف نروژ از جام جهانی به دستِ جود بلینگام.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🦁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99815" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99814">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzQ8yiOhAWvWsRkxNuy_0mCdDurVM201455uAmdvyH7fPT9OYYqsxObpU2PRVe1rY0Az8Bta97NM9XT8vRQsbo6hrSXTNEmhutTtRuPEauJhz5LrYO4MUZ1stC32NSKAVMvqqmXMnlsk9P-WjxUh_vAsDfZSRYtRAFUekitADUACTGEKYcTh7EpcIZFo3VGDuUrwkH9WZ1PFYKTNeDTX5gfVSOz3I1xXEcZWL5I03sUqK23AH0WlRZT6EfJXDWYCejNJrfLkDv_OEU6vd_bNgvKHmbyveEVK-vyQG2aWpMMwWlA_V_ejLIFUICn57bPGmmY5Q17CD7-x3C1V1DU7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از حواشی زیبای بازی انگلیس و نروژ
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99814" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99813">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=M8yD_wvr7tlSTzgFdJJ0JMcu2hUycIcoKz6JDDMfL6zF5-sSt2uS6ED-8aHjBSk6jbmBCZuEAfkdgypVwPh5BQLvmm_TokfXNBhVJX5fAlkN9muL7TfAeXs-rH56fZLg5CSM61l8dgGa30mXjFPE3gXxpY-clHXQjHgyBb6i2J5HqmPRXdA6FaXKyID3b3DZWOvcsPtiZRFqFq8usgHVpzYfTutOwocBR3wQ_0sWF8Lso2TpImePbWnq_zRfjBdiRts67FsIoKMGHwf-IoB9NV-exxLXM3j9tTD2dwRpF5Sekyr8gehw8GmpEPIRexhDTUfljJT2xWkKhNYMtcvglg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=M8yD_wvr7tlSTzgFdJJ0JMcu2hUycIcoKz6JDDMfL6zF5-sSt2uS6ED-8aHjBSk6jbmBCZuEAfkdgypVwPh5BQLvmm_TokfXNBhVJX5fAlkN9muL7TfAeXs-rH56fZLg5CSM61l8dgGa30mXjFPE3gXxpY-clHXQjHgyBb6i2J5HqmPRXdA6FaXKyID3b3DZWOvcsPtiZRFqFq8usgHVpzYfTutOwocBR3wQ_0sWF8Lso2TpImePbWnq_zRfjBdiRts67FsIoKMGHwf-IoB9NV-exxLXM3j9tTD2dwRpF5Sekyr8gehw8GmpEPIRexhDTUfljJT2xWkKhNYMtcvglg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
کنایه عادل فردوسی‌پور به عادی جلوه دادن شهید شدن مردم هرمزگان توسط صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99813" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99812">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🙂
اگه جام جهانی توی ایران برگزار میشد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99812" target="_blank">📅 14:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99811">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=Uq0ayqTxFDiqefaUWTi_21avtc_aB9blbU2Fm8hvBbIMymW7cKWocNo1f0mwC9cTen6MJpRtgAYoClTxewt_NiATAOb2r0ezzJM-9_UbecOIniM-glF-Q3JRUfLeM-I7pgqs1Civi4hUryS9YYA9uYe556YCHULIIfz4--pLNysHEmY7iHTqTNB-k2FoZ4ddb_wqFCtLcogzjl2iryOS-s9dOqkyvSGwK4YZMFxZPdgDrkIsys8PO6k4NRnfxxGTfOp-XWeV-CFdtbcTImcmgIzJi9xrkzIQh-U4Nz7SN8LPupw0F4PRYhT7SmB7DnMinAOuSTruCl82bm6YI_5bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=Uq0ayqTxFDiqefaUWTi_21avtc_aB9blbU2Fm8hvBbIMymW7cKWocNo1f0mwC9cTen6MJpRtgAYoClTxewt_NiATAOb2r0ezzJM-9_UbecOIniM-glF-Q3JRUfLeM-I7pgqs1Civi4hUryS9YYA9uYe556YCHULIIfz4--pLNysHEmY7iHTqTNB-k2FoZ4ddb_wqFCtLcogzjl2iryOS-s9dOqkyvSGwK4YZMFxZPdgDrkIsys8PO6k4NRnfxxGTfOp-XWeV-CFdtbcTImcmgIzJi9xrkzIQh-U4Nz7SN8LPupw0F4PRYhT7SmB7DnMinAOuSTruCl82bm6YI_5bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇫🇷
حمید محمدی: اینکه کادرفنی فرانسه بعد از این نتایج درخشان و رسیدن به نیمه نهایی جام جهانی بگویند بس است و این سکان را به افرادی دیگر بدهیم بسیار آموزنده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99811" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99810">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=NACPunix4Fnxuh0HO--r9kwGk7Rkjgoq4Rz2_HIT8VUG5sLNy3yRtfl5gXMJm9MUF-prN1vRW49g3bwQWWRXrQqcwLpjIPXPRd4vSciypLCK6aK5kLdUiyXgGosx9KpYZDA7hHV2q5_XPTEoNU2lBy4LzCIXnC398kOZtIvNOPS7W8f-_46JwyJGmUMCOvXXVeM3UMS3t_11IvoM3dgWDv-Q6Vs_By9q5NOb9HVsDAoJq8LcsjWkjj-woSZ0ZuQGMBoJBz7SFI6ZmY1FTG49vp2x_NUR787EXJzuyelPnmYLDJywG6g7F9efoIrki6d0ZvBYe5ONti57Mpas6069rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=NACPunix4Fnxuh0HO--r9kwGk7Rkjgoq4Rz2_HIT8VUG5sLNy3yRtfl5gXMJm9MUF-prN1vRW49g3bwQWWRXrQqcwLpjIPXPRd4vSciypLCK6aK5kLdUiyXgGosx9KpYZDA7hHV2q5_XPTEoNU2lBy4LzCIXnC398kOZtIvNOPS7W8f-_46JwyJGmUMCOvXXVeM3UMS3t_11IvoM3dgWDv-Q6Vs_By9q5NOb9HVsDAoJq8LcsjWkjj-woSZ0ZuQGMBoJBz7SFI6ZmY1FTG49vp2x_NUR787EXJzuyelPnmYLDJywG6g7F9efoIrki6d0ZvBYe5ONti57Mpas6069rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکثیر ارلینگ‌هالند در سطح بین‌المللی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99810" target="_blank">📅 13:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99809">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5445db9621.mp4?token=A96c_AzzM10NYprpqPXd8IxEmZLrdkm3UHykVtHyLfh35NPWyEfT897W49CIGIbEElGHHK64omYKi4y5MLF-pStjNzCyGjFZP5jm6wxHA01SjdBR7OUELegb7n0QU2HhUwPza6yj-DI0g5wUCAyMaOtKMxR8S9feRkBaFeI963NqjmOfieU708HzMChJM7Yw96wTow5yJ1VuVaAgq4ACQsOSwrt7JJ0TzAobOVt_29XGJqKmXAtBXBr-hgsFKC66ZLmkw3n0W6qkMC_T4g5Pk_9qsme1bF5s5HY5ZDGuP1CyHc96z9yVFYDgm5RNfKV5kaWvFeFOf9kHUMVqZOvhFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5445db9621.mp4?token=A96c_AzzM10NYprpqPXd8IxEmZLrdkm3UHykVtHyLfh35NPWyEfT897W49CIGIbEElGHHK64omYKi4y5MLF-pStjNzCyGjFZP5jm6wxHA01SjdBR7OUELegb7n0QU2HhUwPza6yj-DI0g5wUCAyMaOtKMxR8S9feRkBaFeI963NqjmOfieU708HzMChJM7Yw96wTow5yJ1VuVaAgq4ACQsOSwrt7JJ0TzAobOVt_29XGJqKmXAtBXBr-hgsFKC66ZLmkw3n0W6qkMC_T4g5Pk_9qsme1bF5s5HY5ZDGuP1CyHc96z9yVFYDgm5RNfKV5kaWvFeFOf9kHUMVqZOvhFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
راز جلیقه‌های هوشمند بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99809" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99808">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFtcm_oG6gbKsLN8mGCg5ZJKpuY1woSG_o-iJ1J-cvoPUxthmiTPGeCLKyGQixRQxDb7ndp2D-EVVue2hBz2L5VIdqai6eDn3z-Oe0c35_mziLnQZHGJyUMh--MgODbiiQ4iJy_tUsWODyMcIWN3DLOtLY2WPNUbKOMZ9o95W_7g4RR8d0wmSNK6O2I4JmhUlgg7TQMXGYXdbapN65fjsuXwOTJ9iflIADIbtxrFdauSPxLz3Nvds6EWZWFDFnxxKZ2epUPy7iqmI88xciU4SlQbnpw1MzXVkUUwZTgqKtYzpQ7oa6T2EEt0xt4_lVz7lT3Z9z-ZJqlGxGSxO1HmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
• درصد احتمال صعود تیم‌های راه یافته به فینال جام جهانی (بر اساس مدل‌های پیش‌بینی):
🇫🇷
فرانسه
- 58%
🇪🇸
اسپانیا
- 42%
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
- 51%
🇦🇷
آرژانتین
- 49%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99808" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99807">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99807" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99807" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99806">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oztw2u8MuYJaxu65Bou8eeNa_LDKxOnHrtIiX8FA2G-xntuTDr4mjndWgP9tAGK1XBOG-YvUTf1CsBBTCTVgZy4P7AIrBpP_vDZevMw-UjQ4r4kfenHaWbGQtjG2sB8s31S4bXkXMRusd71Uz-usnCgaHG-2A83H8CscmVVVSh7qSD0K6-eCGQBNy_076QVl_tASa2vbaKQjOO7DDxNoWP5NFCJxL2WZlnXajI8mA7E7Cy5D4HDWxqpvdOkVRpOHbgj3v5bNBsrgNW5r100hf3jGjQttoFAFd86YI0zFIYHOtZyfXhtfO7IpX2jD3A9HBqBemR3_w8psDnOH9WP6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99806" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99805">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22252f139a.mp4?token=gsrK_9yc6aDmMDgJm7sBmhsKbsIgAOeMuaTjU82drNVEARf2emdCFN2HSXe6V7Hc3GrvpAjYn-kuN_ntQmb4RsRV4eSnvACfSp-oKxcgAxO1EQPc-XFh-OPZydnaNFQcBXNmvZ7ppw4hr4P-UvUYls8M449_NRKLIUcZKgRa8OoTprIKX39E-J_p7pNu_E4Z-Fb7ZFEQHhsuOSfpjcN1ObvKaBXfZTAQ2jgEU6uF1sYB1tKHIU2M9j9xO5Sib1mnN_QadphVwqeQ0_qk6DuPG5sOmx9hdLMQot_52EU4OHDlTKu9mbTUcBO03RXIToCwL4xkUrA5FTan3jKTOKndrx-WOnJAgXcXVFzrNFtmadcb0dJYMxr9ZcEzf3dk8TYGTgjwQL1FGa2vftpt7FbSTGByt_rZbgjk9xGI-tXsw0p0oiKafdSnKP4fTH5-QVp8L24KrceZMDHVkyq1b1urTCgwqv6bxP8QmWnB7_VWqEthatWHssLi6YaFeESa5F869HDniXqypIRqc7DlWGThWeuFFl90m-w6iinEtDyhfBX5V9wsA4TH2vTLLviLdbEElSf0LaU1_-I4-lCgNMI5iWEvwD0cXC9tAhC-iOU5uVPEbkTlN9YEm71eGECoIzchoBkr1K5MkNthJSaf8NduZJ5oSfoLD1NaGPzQZTxFGYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22252f139a.mp4?token=gsrK_9yc6aDmMDgJm7sBmhsKbsIgAOeMuaTjU82drNVEARf2emdCFN2HSXe6V7Hc3GrvpAjYn-kuN_ntQmb4RsRV4eSnvACfSp-oKxcgAxO1EQPc-XFh-OPZydnaNFQcBXNmvZ7ppw4hr4P-UvUYls8M449_NRKLIUcZKgRa8OoTprIKX39E-J_p7pNu_E4Z-Fb7ZFEQHhsuOSfpjcN1ObvKaBXfZTAQ2jgEU6uF1sYB1tKHIU2M9j9xO5Sib1mnN_QadphVwqeQ0_qk6DuPG5sOmx9hdLMQot_52EU4OHDlTKu9mbTUcBO03RXIToCwL4xkUrA5FTan3jKTOKndrx-WOnJAgXcXVFzrNFtmadcb0dJYMxr9ZcEzf3dk8TYGTgjwQL1FGa2vftpt7FbSTGByt_rZbgjk9xGI-tXsw0p0oiKafdSnKP4fTH5-QVp8L24KrceZMDHVkyq1b1urTCgwqv6bxP8QmWnB7_VWqEthatWHssLi6YaFeESa5F869HDniXqypIRqc7DlWGThWeuFFl90m-w6iinEtDyhfBX5V9wsA4TH2vTLLviLdbEElSf0LaU1_-I4-lCgNMI5iWEvwD0cXC9tAhC-iOU5uVPEbkTlN9YEm71eGECoIzchoBkr1K5MkNthJSaf8NduZJ5oSfoLD1NaGPzQZTxFGYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انشالله برادر عزیز آقای عباس‌قانع با اون صدای گوشخراش خودش گزارشگر فینال جام‌جهانی نباشه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99805" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99804">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=dn1T2csVJEIbMGFd_K0sNWTjXnu5TgmM3Iw-euAR9O_Ak1-LKKvBbdDF8yNm5QwvoZJZssDVERDvQam52nVDv2erOWHM7uIJ2N1o4gBNEBvmKRwHM_neb66NBzUaZRrKo9I2HiWi3juPRVEnZhzwRoDzkaA3TbqeawdGZMYZgQ9jFoQpnoV_ilttdvjA7QliSHtRbvM-BtPj85Frto7JFd4xGLWRFQCKDjck9Q4w8Vcahz4rZ4t_ewWyBKGN1P4IEvNfYDpiG9k9CZoeCKHNbzsrDyGOL4Xe1Skp7EQSfj5xEIYZB4bU0FP7PuWCROG2oHq1d0wraAkDmwbCXXBMew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=dn1T2csVJEIbMGFd_K0sNWTjXnu5TgmM3Iw-euAR9O_Ak1-LKKvBbdDF8yNm5QwvoZJZssDVERDvQam52nVDv2erOWHM7uIJ2N1o4gBNEBvmKRwHM_neb66NBzUaZRrKo9I2HiWi3juPRVEnZhzwRoDzkaA3TbqeawdGZMYZgQ9jFoQpnoV_ilttdvjA7QliSHtRbvM-BtPj85Frto7JFd4xGLWRFQCKDjck9Q4w8Vcahz4rZ4t_ewWyBKGN1P4IEvNfYDpiG9k9CZoeCKHNbzsrDyGOL4Xe1Skp7EQSfj5xEIYZB4bU0FP7PuWCROG2oHq1d0wraAkDmwbCXXBMew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😔
جوری که پیمان حدادی مدیرعامل پرسپولیس دیشب از حقوق ۲۰۰ میلیونی صحبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99804" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ts77SuHdvDkcRR41K1Fo4kNBT5_zu3cxf0kaY44VBD38Sdgb8NMyLTYpx7nEgbSy26O8fXDRNpS7g12SOpNWd2InxUdgk8AFLHEKDAWY76YTF7bpRLFkvXswyIl7DSyrbzxNlf0bvfso3wFMuoyBJ6TB1jBFJKJtxjsqPtLD0vRjwMZzEhQ-WXJUkA69aEvyXTMbFIBK9WnmbOjtQOEgtPtPBrWRmurFKwt20PGI5KeTHjjDg1Pnni3kWhh4p-0CQKIC_0oLhmvdmNfg-GQbTtnJfHkHaDMPgLpajQrvU1qUlmmsz9uybXyNqIvYC7TDcthfxyPsyJcchoP3xNRWZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rsnvZmxgZ3iABvKtAZPqzgmJQE2vgCr9wBEKIv_sop4Q75VnA1HrzJUNlTjqpeVK0ntqlu5uBdMDN14F_PRDW5WSVgtDJ7PPsaHduXoA-McluOqejYDe_gWZBD3kh1-qAX6iaSL2EDR3u6oSeFvCSA8ft7dmWbiWzaJPQGkQBd-bLrrAx1qZtbdsvWgDPtBWaX0nzpd59HZsTuPlvtyrVGbaO9Ln00NoO_quLia7RsthpZHcFDCgf9i-pSh_NqEJjsRTZLJfDJ9msPvr3BtGMjGJE_XZZVfvaPxkxeHrneTH5kyPTf8wOwCGFBdEGBQBTt9GNxsCSPaz4zvUFEPe-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A33f8snEWTMzaf3M7LE2ykMDagZa15nzOoWsNtHVlFEnbmLI3nuCzVaIZWyvkqyik4ZL0XjYX1CZkwPaol6pFgHOEnhjukYEDCYUpC-NDlkGY9lM8E3SCRzri-2m2xBL0trgi-12wyiSf5g7cGcYas3dMdQu6jdi4cX_4Ef7ZqJB4sQOUw0nO3fZ7fOgIkUaekJZXND8pI_XroRktWh95iTxqC8mL495sBXg-5MYzmyabXzPFg6qVze6g7MRFmGiLL4qT3R8M5QyEGBwP9eImICtqLssRVPUWl-foZa2X-8UfmXzU0VZxzvzqTrN2qmjq7VuXCFNlMx6YJDZLS7w6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوس‌دختر بلینگهام در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99801" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007eae865e.mp4?token=WVADPzhUXFoaSg3HP5dVfagkDNUc4OTiwvGRPo8dc1atTi1nf3ynkEOoNze5xWK5nAei6iWJjxaxdcTSTgv2tZ3jMsMW0depakKotvCDH5Ob7PIMsqdGykPyCCNfFI1oIn9xZSzTKSfSWAGD8LhhKkp2DIA7avU-9Q4eD87hjSr27A0fkybDQWN85POTCfJ1CRa29iPSEWuJtQVG0dGEzrMyGCDB5BlSrPMx42FHa9YVwFuhzqRIFQsZDZs3uE_NH2sowuqB3vaar8x2DytMUgma-pguOBhzd9ZUFmWF1SCq56vpOpLTNgqx4j1hEfubtesbhNnwHVh2iqc96ww2bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007eae865e.mp4?token=WVADPzhUXFoaSg3HP5dVfagkDNUc4OTiwvGRPo8dc1atTi1nf3ynkEOoNze5xWK5nAei6iWJjxaxdcTSTgv2tZ3jMsMW0depakKotvCDH5Ob7PIMsqdGykPyCCNfFI1oIn9xZSzTKSfSWAGD8LhhKkp2DIA7avU-9Q4eD87hjSr27A0fkybDQWN85POTCfJ1CRa29iPSEWuJtQVG0dGEzrMyGCDB5BlSrPMx42FHa9YVwFuhzqRIFQsZDZs3uE_NH2sowuqB3vaar8x2DytMUgma-pguOBhzd9ZUFmWF1SCq56vpOpLTNgqx4j1hEfubtesbhNnwHVh2iqc96ww2bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
مود طرفداران آرژانتین در روزهای اخیر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99800" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99796">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pql4nJv-qRi2j2SlMSeCv-N8qmozWcxT49QQVlDfcfmZpjpj05rGQTQgWZhQhZktI5PSN3Jx-SYyj17k-8cN-ZuZB5bXa8s0jT3FWJ_EGwmdRRQyg0LtOaaIMMmabXqBMqWQXDfUo_W61La2cMmauPmourUX5deK7IrYXdz7GQOtuQpraWmAk4MOO2LAwej7zMLJhVJbJBoXd4EUBTL43fWWtMcPivaGSIOkSQEtPKZl-aAW7dOSrd8i_86arzY5X_WUQzAGFbYDqaLabIXgdIjFoHIL46rZf4QS4RCVa-3xtlixG-LJtfPmg3Ar42EclPaJ-8FIefUtqulV0MzsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWrSFgDc2BjE8TKMedbZMAt51E2SVtFxtbt0fGHxMRtZ-Wl6cGSwl6CY_pKcIKkKjnzy6gbmvaCH-e0H8aRf8iY0pfXfittBEukEUuH4jL5t8Mz5wItHReXOOzyFRezif7Rp-S86QjKxZd_FP2DezmrcK38xme8UznUjKzlLjLpkyC_SCQV8Ng8L9owrDV9TT1x_ezW3Pbjyjj-XM7oL5UFz_CrEGXdNhA_MKNcPLdgmNFLU6IsbTb-pBM2hHDTbdbNeL08QfYe7hAIozshhdpZTH8pa0WEJ3WBYIVhdjaaM5DULSyRlQjC7ux10J5muP8s9yOlW4jXTS3FE0bFPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltpEvaKZpOZsnMB7b6psIrK7uVaycD-IXVSAKbje_GqxX0iXhuK3bzWvJVhccsre8PnBraChNw1UDMozhk0bqIPRQUwxRiEMoyTsJJRxAMOm71Lj0U_lfpEQd_cZSZVENY37lEi79MPjPjJ7-9x8XzAGrak1BL41wq5Kf1BQ0cGY01WWJ47LLSwAAQaeL5g3E0MXj6uk0gvIGyJPYiLuvJbicRmEW7Zw4RlFUBgQANvcDktHrdTlAP1Lph5A1sf4nT2k48tniNrYyVxgepOSDULyztzB3JwNV-JTHzUG1izM5IGgP7PXszCItxxIedj95eXaN7GL4Vft9EjQXaEJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0fC4sKNYwgSg4JcZRm5I3KnnEeZt9LABcWJ38p7dS3-_erhbwqC6OVm6fSHAv6ROw4c1syg7b2Pr8XF4-PbsEFZam4070zoRa4b4_QROx6lNx4trFEQcp3UXktlxRfYNemy6mB90eXsz8RtdxRJMW7oaQU65xF8pd0h4a27i8W-uCLsnfpO_KdqaVE3tYIvmEJmTNFmGO8Q31UimJOLMr8328L7ztiZSTCkJ_l-7dINXl01n2FI48QYrS9zWpGFdId1igPOzm2SpKSq_WGpgFTHbOuc5rrzStxJk70ThVCz_ZgRZpyYhpDAtkk9ZVA9HhScbwW0QwEGBKOC9z_IzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇦🇷
خانواده لیونل‌مسی در بازی با سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99796" target="_blank">📅 11:31 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
