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
<img src="https://cdn4.telesco.pe/file/hFKH2Nz-yflLidgTchok_cRdkvEConDCDdA348uGclv2P_bDvnS8eFCYGuTsSk2_IstKp3pUbmROw0I2-pBMCc0Rn3bca8zZvorWuBJdoSfKhDlswVy-RHEUiBfMAGPaZqjieuo_AjvEM9leLphhZQTkcwtvsaxF_Q1qlQECoakTm2je77zzhG4eukLFIsA9xMnfBMZ9lirbbzYgdBRVnL2Mt73AzR-gL5ox_JcjD6I5y13h0xL-uvysOWaK2t4PqrQu-YUYN-OOhlRcJq2MEVq3kRzf4Op-Gx_eElwTkmQscNkHVh8qNPfOsFVBxwl75z-SBqfdJpp0WgtvMKFSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A62YeORBEqOd7lDyi3pTKs8q7wpggFWY0i22_qRN8xeEOmcZJdAyUPwsTdsIo16oZtk6gxLJ0MclufRyRbR-z-TnRh2fvb9PZPEXcl9AgtovuYSVRLXmjTeFLcReqFtgYFnMsIV8Sevf2nl0_pXS2lgZJXDzih-5xxuAiQT6KrBCGdQAb2nyTq_-_bWvZRtq9zdWymXoA61mmiLBZHNpnq4hQrhffDtv-hJJbN7ejN1BpW8prCCX6wAhHASUI0BYrmMQ1gJT90CARk-nxjL_bjGqTNA9g3GwpMMo5yzZ1Ye7Z5nymikCNClci4B_Y6_GgMILNzZ9Yc_BIlENFuEQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=npCBaLvNhxWkgtq_2P-qY7cOGmgqRkJpG1JRs_S6jHJnwTzoquWfbTK4pmnBFZ8LvScfwDQ9_cwPhrg9huDTxXHt7IG8FWjs-smke7g1IA45L0SwV7ggYSjzYJF1XV7DHanUZShTl8nshIkXfScJCA6442BfwNxKH-TR2GfiZxz6w5NZxDMEOiCgGoonQ6WqHaYz0OZfSMM0xVJnEHp07hI13S-xX3EpMxhSsu49LhhBn2oJY957ulkyDarOVqIUkPtAkqBqcdBBsgPkQj5MG6Ee2aQczH_5wo5ohUu1LIC7kSiaggtel2A9LsW5_VPtG3c9m3HLBmkOrcQbPYQ5pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=npCBaLvNhxWkgtq_2P-qY7cOGmgqRkJpG1JRs_S6jHJnwTzoquWfbTK4pmnBFZ8LvScfwDQ9_cwPhrg9huDTxXHt7IG8FWjs-smke7g1IA45L0SwV7ggYSjzYJF1XV7DHanUZShTl8nshIkXfScJCA6442BfwNxKH-TR2GfiZxz6w5NZxDMEOiCgGoonQ6WqHaYz0OZfSMM0xVJnEHp07hI13S-xX3EpMxhSsu49LhhBn2oJY957ulkyDarOVqIUkPtAkqBqcdBBsgPkQj5MG6Ee2aQczH_5wo5ohUu1LIC7kSiaggtel2A9LsW5_VPtG3c9m3HLBmkOrcQbPYQ5pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSH8-X5E43xJYN5kzNZJIkof-nwHRadEfjIQIQy-OfGkL49m77uMLLh5YLer-QKDNQ1dKEwnmNaAQgPIfTZ-Va4d4LAHsdDXZFqaCW4ULO-nz-XG6OUeadXUQkn0LRoAh6HZ9tWhiNyotCRpihxZxNVw17W5VEUfndVrAHuDVdJqQzBe5YAZdFmNW3ma-5IC4-VWMYiIckXPEMTUZC0qNZ4zqi1rIwwqlzdMQKb_Ki9Qyd7Jkmc3Dkwzq9nnnb1x71B8uAE2C0BzJ7zhaN9u6eq8EGEQn4iz6Jozjh31NapdtB1O0YPobNKz5aoNz1Z0MnezTZh5_LkMLi5rtfk2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYpsuU0F7Db91lkw2stWe9Oi1uGV_k6s9laUJ9OmmMlqhsJjzfja4NlIatEIXuWH2TifamnKoOlOl3urojmvAtyumxGA02lh-esG5_MCOPDlPbExi_jwJTZJuVoTy0NqGhA_0i0ENbNBqcXgEwlXUTTB9ZaxO8gjqOfiUfPV-2XdICrbwDhE6HiKY5rGmTCdKav7rYAC_t0Ef8BdBIwf23vJr63Y_UiI2bnGWCoPdYP1ORxjFPd53_P-JfQOtVUDXzzM7QzaQMK4Oc1iN3K87HBFqrhwoJcDFyhJqPoiuC14U2wLAskpyd6SnFj2H0Lv5mYSSYdPgH1gnbUO0gnx9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRx6DIH98SCfcWdFxzyry_R0-UX5v4MM7is0wCZX8dV6sgR3JOxYeSZEvWS5CfqutlL4GqMcNoO9xbUxc3M5SFOhjtWO-YPKym5yzpSn6uQrSc4u4IvYlUzzgWOIm3UMBaepTz1k1-Xo6AYI_NCtsCvI84r8wQ2-TybsXGga8kGO9qEBbAr1BkVbdhwTqN5tN7Qfq0D_4Hh_V21OoIVD2qmp4PSyH15UY9-pk4_PYss-NjykoSQ6nh2-xmbOOuu9yGGr9LAW6iw_058mGaMkhpyvTsryUsF5DW5Urg9dYN3O9c5ESctEnSdSgTDjJdS47nENH8zoMn5TwEMbcdHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myzUStoTmA4XWTeQacdYUUh3MvLqOAfLx1BMDF4vwOZNzQU9UrB89mieu2EdnWvACxFVAP3n25Ifa-3f4tScqpnH5HIFzGnGcKG5wsMP3C7UEQ_ElfzJFdanQYJXFgPay6UNDPvOB4oPOoV9QKrOaxozRVGy7UKj5zijU2-FgE-Cv5huK8jODWMQcD_PQszwIcchyis5wDUa89sskdjEd-x4yhEDShQcHS-Gv_nS_DrLMpSIhUntxB1KAont1Iz0c6qbncz80XtqEgZU9x9uTI2wbrj9MBPLkzs7uc9055r2mpvpBHCyh4mDmx594MOHAWbmGvQm_Xn8567j4V9w-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHRyiiMLQRUORNRe7mra8mPHrVFeYYs_HSvY7G9YluaNG394MzKMkHkXB0vY8xg23uWnR0NBGU4RzagmIkxJPxb5fshXUwTL2R0otSl2coC6UycVBSMDb8e40-AYNq6Lf4kbOk0J-nnJQRROWrecTMuDaojPEZNLc_BtR2_skdYYAH9eiY52M5mg6mjVW9lFRBhn_UmTqHAJYz89_EBROm6VNmvl_06OwCzwHvJ8_qmZPNlxS8lD-pZsNl9NeyzXTWDJkxKsBJ8ttfQTRYxZJZf1amuNJZenMM5aMBTpipH2099s_WAk1t5CEb1Y2OfSuRrhD-TnhtwN4FFjhBvDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3u1zFo5vR-nu97moXX_W_T-pUOU4Jr8mIUttzAbUXzBymIDkJRLpaihGSoZa7yA1v6_R4x3AaU-tf94EOgINiwdXu-ZfegvAtIBXacSylFKb-RXCNwfAe8jRB5x5WoHj7vbGotktPeCyx5GuvggOZ9dl15W4k35WOP5lycaOknpIhJdkIaXlWOTr3FgKjso1HKm2o0FF-zE7bGRjqb7_u1tYmgELHMvwqEVqRdBkPb2eAMiTeoLf03p807lIJcKPOK1Jn3ZRwLYtud1Nw7MxDNhNQBbRQ9RjE8MFGjd_h3NFtpNHU5OakMHKd6Ov5s6NdbaYPUCZLl_V9zZg7JsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw4qI7OFDO0L-eMgC3T55yIoPOKJhV_IeISOqGGTHL9yEAL8oLpr2Zbb9lscELL5mkfnc1TKTm3c_3ygDxWrMcVvfVme--gVlgX8-HtCw6xDG_GH1U38hNuwkeUjckCbIEf9RJy4zZOgsHxbv4Tt8DzA-8-fTFzN-FKYRqgGoMODYb4M8OONFEgyEZr-g8B-S3m9c4B9fe_vvEF6xAdgoOqqE2nQEYsTIExoZ-YTxl7TM8gEq0rUgP1fbCEALO25pn7k4tJTpmeBo0T0WCPfsiAEh-Kq39mvzjConGznYQpRzfFy41h9MsxUMbI7Gd3BkVu63zBmrSryM0IoyvVIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=NmRxyFKQZQmZNF-rL22RMwovQW8dGgf2mrOuiDYppIC7Fd_AdIYNpXaCtDF0GORKaqpt89VEXWwJpy8st0SezmMmaBWSvsP2ctIz9OnhYh9hqm8vtM1Id9lr0issIsYK7nIYdE7OHkS6GxTHsnA7wuPXDqMMyBB1uKrqGN2lJ_Df2a8ZREa9NAux9eYmY-fvXXlUnkdewXriGlV3_V3FSpHZNzuM4tydIpEaJtVcHVoXvQ-PapmYtVdOnwu9Z9Z7hy3HG6VVxgYcZkrmnmwqA8F0rGvay5uIaH4hro0hQeoQgVDTyPO8VOZo0-KpLjvy5Wk7ELN_1gQE2Zpxgt7oIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=NmRxyFKQZQmZNF-rL22RMwovQW8dGgf2mrOuiDYppIC7Fd_AdIYNpXaCtDF0GORKaqpt89VEXWwJpy8st0SezmMmaBWSvsP2ctIz9OnhYh9hqm8vtM1Id9lr0issIsYK7nIYdE7OHkS6GxTHsnA7wuPXDqMMyBB1uKrqGN2lJ_Df2a8ZREa9NAux9eYmY-fvXXlUnkdewXriGlV3_V3FSpHZNzuM4tydIpEaJtVcHVoXvQ-PapmYtVdOnwu9Z9Z7hy3HG6VVxgYcZkrmnmwqA8F0rGvay5uIaH4hro0hQeoQgVDTyPO8VOZo0-KpLjvy5Wk7ELN_1gQE2Zpxgt7oIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I08cQio5M-iBdJoF4JL9dtg0XkzVbRFO2et6tlROxoOpHqmT5VYDS6Da1byy56JgWZ9GHY-9uQDGcuy2GZGyVyAcIHCCjnzp_7I_TkFEYPCrCQsgZWsNamVeWjXWhpdor29y8h2fmh_r3mpLurVFMygzzYXZl5zn2GSavDLI4EjnFn3I-llARjlvvMHX3GBIQtCAhXpveEq3IyqtMN8ulo4RbInDMw9IjcXXFuIr0ooSyS7pPDmoxLxkkXR727JxnwE8lj-1KB8pzifPhflmrpyRuLwiboz46RqsI5l4QqmSMZRBBVb9Nz1lWbIah_XhRey-gcsqvJTELf_MjIskjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBN0arrz6E9sFNwP1cMcNEgEEjIVbz8OAzV7zwiUzY9aw7rTTynruQugMMe_oUQNxl158YKIJKbhuzwPDmiv9TQXVgwbzly6F2cAfjRUymNw9XPiVURE4Agd8Nc-R0fdI0NHebIch_7MrC1QJTvnlg5nGvcyGA5oYEp4hyArNrVwqJCUmxF8S6tKq_nL7kR0wNSkOq6uiBHieVXZ5rNxpSb19cLl2SX3kPuMCWfdqnn7qZCAK0_mnOcGEPcMjqfQqGBohdkyXBoZFUjnYmR8kWh8O17yI1ckWzjq3HMuZbfHG1Y-_RD68ZkdexxKEdizzDqAUdZXMUZY5G7Pfw8bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=Uzg0lpx3IomAYZUwI5QpTkPH4yzMhZM4h4cWDFKor6k75lq3blQMevffpMn74k6-L7aVRXn5FEa9EmmEtjg9zbz_3YzrPUqMnJ7GrKBOmOW1410r5TPAr3kVPWpBMQqlmNvB9ADHSQV43Z2-zZ46jgsgO2IRoOrPHXkCva3ik_h2oG2JvQCjEIHGO0FNmCB-IPC1uVrsUGmT16x-FZsIU7rSHgxiT7OQHOo29zhS59pc_Mhk04ULLUHrKgY83gY4qHViDmlXt2DLwlC-Cme39xtwTeoEWngDVEs71UD2qcW8LNSfd0XvvO8YSgtxPY3MCttdSteP66oMyXkxf3QEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=Uzg0lpx3IomAYZUwI5QpTkPH4yzMhZM4h4cWDFKor6k75lq3blQMevffpMn74k6-L7aVRXn5FEa9EmmEtjg9zbz_3YzrPUqMnJ7GrKBOmOW1410r5TPAr3kVPWpBMQqlmNvB9ADHSQV43Z2-zZ46jgsgO2IRoOrPHXkCva3ik_h2oG2JvQCjEIHGO0FNmCB-IPC1uVrsUGmT16x-FZsIU7rSHgxiT7OQHOo29zhS59pc_Mhk04ULLUHrKgY83gY4qHViDmlXt2DLwlC-Cme39xtwTeoEWngDVEs71UD2qcW8LNSfd0XvvO8YSgtxPY3MCttdSteP66oMyXkxf3QEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=g0PlDDOsACHm58ms_tJzY7o7dCuTvvsuXUiR6idHiYw7r2IZAYztH7H8Z1068l8uhGbW8syX64l8Ak1qInh2Mw4u2lEal59SkLSL06nbk5nEsCU71YU7CE9zr9IPxwNiq2hlRrF47vuzY0_jIP8kzf7AcCSWm3BikvIrC4aHOMUCepWB8javMb7IVThvLfp4nj194UTrI36WruFdN5SDbkmplIbLTbfWFLuW5JdwAvbSHVO8fdZdEoENPwcexXcLD8qZEeU-NNs_TvOkHWm8ie-6sk1esfdrrwRlQ8AziEzKEZ_pOjdLEgu-v9JihgqhBRbRuieguJYAjzubyM_b5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=g0PlDDOsACHm58ms_tJzY7o7dCuTvvsuXUiR6idHiYw7r2IZAYztH7H8Z1068l8uhGbW8syX64l8Ak1qInh2Mw4u2lEal59SkLSL06nbk5nEsCU71YU7CE9zr9IPxwNiq2hlRrF47vuzY0_jIP8kzf7AcCSWm3BikvIrC4aHOMUCepWB8javMb7IVThvLfp4nj194UTrI36WruFdN5SDbkmplIbLTbfWFLuW5JdwAvbSHVO8fdZdEoENPwcexXcLD8qZEeU-NNs_TvOkHWm8ie-6sk1esfdrrwRlQ8AziEzKEZ_pOjdLEgu-v9JihgqhBRbRuieguJYAjzubyM_b5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=Edw1QaUCY8lbAYxR3B63Ybuj7JhUaBlFAl1wtJ5hQTt-zIIXwqCSl3r8evdeYKe1OmugK63IK1Fndt7KbElTT2UUq9wXJ8igJyox8EZhdr1y2FsypuBVSwASmVmNKHzBaHyOjPcJb53VO_KUpiSTm3ndSHnCl6ped0RGRzZw9uZsn2MMP-h40rMnE5H_3QIiagNKWaMMrsEalVjN5mx6Nt_ojTM3VLe--v9l3vTO0zfERtSRV_L5W4PNWWcNLGaIcEDPUgLGNJJcXJbkkBDBLyQcd7Fin-NdJXKztJphgG9vv_KFEyQUAKZHOWAKNqY0FCmDedhm_GfduIqW3xLF1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=Edw1QaUCY8lbAYxR3B63Ybuj7JhUaBlFAl1wtJ5hQTt-zIIXwqCSl3r8evdeYKe1OmugK63IK1Fndt7KbElTT2UUq9wXJ8igJyox8EZhdr1y2FsypuBVSwASmVmNKHzBaHyOjPcJb53VO_KUpiSTm3ndSHnCl6ped0RGRzZw9uZsn2MMP-h40rMnE5H_3QIiagNKWaMMrsEalVjN5mx6Nt_ojTM3VLe--v9l3vTO0zfERtSRV_L5W4PNWWcNLGaIcEDPUgLGNJJcXJbkkBDBLyQcd7Fin-NdJXKztJphgG9vv_KFEyQUAKZHOWAKNqY0FCmDedhm_GfduIqW3xLF1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=Eecf9l21DtjdXd_xvsFMJENKhY9agVb0bqGaKINcPKoyflCk_LgoWOK8-x9Y4pvWRUfN_VVHi5jgpHMfP9WqCBzeVxE_MRjUeCHvp0fiBiQs17tgbArLyVr9bc-GdfdYD87qpd71CCpc3ks561VzmYHgPW19H720XxU5N4SKGTkpYMNS3d-FeLubJMhrp3LeMOqbB4GA946rySWqIQdsVEyi0OnEIWIbmoxSURyR8FzvyLu3Abbewr2XKOzHpIZ9H5gPr8wuFhqeqnBRURRXUvg7BXnsIJuCsqbrNg8zEOGgCW_a3Vv21bkyhO-13A1XHYnHm13wKB723OU5-iNkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=Eecf9l21DtjdXd_xvsFMJENKhY9agVb0bqGaKINcPKoyflCk_LgoWOK8-x9Y4pvWRUfN_VVHi5jgpHMfP9WqCBzeVxE_MRjUeCHvp0fiBiQs17tgbArLyVr9bc-GdfdYD87qpd71CCpc3ks561VzmYHgPW19H720XxU5N4SKGTkpYMNS3d-FeLubJMhrp3LeMOqbB4GA946rySWqIQdsVEyi0OnEIWIbmoxSURyR8FzvyLu3Abbewr2XKOzHpIZ9H5gPr8wuFhqeqnBRURRXUvg7BXnsIJuCsqbrNg8zEOGgCW_a3Vv21bkyhO-13A1XHYnHm13wKB723OU5-iNkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=krMQB2K0DgEjIL2SPhWv1vDO0iIqB1gZOP8mxSirX-NrX7lWKZE9F_xGHc0_7Hff22uVIscZfQfTF9EisQBIQlhyNAtL14ehYlAJEclUjx8QtWHUJ7Ln0zzMQ-jFnbDaNJamyVW8665orARY62KSNUwdvQgemkdR5VMsXuNQQC176ZoKL2__ajAgzRsUUArRQ-sQDSLGAWxMzdPxftLsp7QMkQDznrttLXTT-b0WChK8zD_KoFnEadi9BDZ1Y56VeEbhYMjJ83HJxH_cacSDx0nJEN9JT-_pOqqx6PosZbsx9NIYhmHx1ZoNtLuD8i4AN0dYNYshaG_lgKBOQWOxZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=krMQB2K0DgEjIL2SPhWv1vDO0iIqB1gZOP8mxSirX-NrX7lWKZE9F_xGHc0_7Hff22uVIscZfQfTF9EisQBIQlhyNAtL14ehYlAJEclUjx8QtWHUJ7Ln0zzMQ-jFnbDaNJamyVW8665orARY62KSNUwdvQgemkdR5VMsXuNQQC176ZoKL2__ajAgzRsUUArRQ-sQDSLGAWxMzdPxftLsp7QMkQDznrttLXTT-b0WChK8zD_KoFnEadi9BDZ1Y56VeEbhYMjJ83HJxH_cacSDx0nJEN9JT-_pOqqx6PosZbsx9NIYhmHx1ZoNtLuD8i4AN0dYNYshaG_lgKBOQWOxZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjAB9PXHSx_6Thupg09MAoOI-ofld20LzkdKVkTjKcIGEOwpcNzH7KDahDDJLLgCPjbTPutB3c_0_uq6xZjGc1zkf6dymRhG99ASkyfpAdI3PI21Eouh9s5dNUq4zSFMCGTqnq_Sd6Zp_KAE_lyE9YqkDoJXvIEaJX_ftN5Axe2Hnu_qpNe9tpalJZAygxp3icHXIZGwml--B7sm7-yaCe0ciB9732Q08x_KI8wyub90hNC0rpOawiEWWdrJhTFEaS9zzXZQIpdJX4EgaAE_7_0jJM-2YeSK-Srf8Outo01_rJsZXUWxvEfT7Zc3tzcwlSbAv6YRo_LbS0alrEeEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbkXn8gO4N1-6HfPLN6R7c3L2oX5lU_hr4eOY_Gr6MYFPKzaUSajulguxXYuAeUrxQR0SjWRrq-HiCXdsraCHiwxyrmhPwgCeBz2sjxS2ZKEvBaW0xQtG1DWh4HVe0AHhcEOLXeCp0OSkOgjEmjw14Z9L4TvBrStSl7fx9Ogw8qM_owD3SgZfVIZ8BS7BFi5zJfJoqGUJtDIs0gDMuxz7MwDb54mQfuOCMjyev7ME_psYT5h_n1LfxvhKrDso_pUy8vB6nHCJ2K7fiLU_mADtX_I9NVLMiRIUjJhJuInC6kGApaT8ouW0clIs5JrpV8RgFE-wXdrp031yBSGnp_Byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQNVTBRZjx2aLBg6J3ES6PRE7oJMQ4lgSwUHuE-L-wbft3cAEi_5w91pq96TpqqjITW7XJUl0nqWEDTfo1_JbpE-qBs-em3Bw8SOqVa3tGAK2t5dP4T5pRaZLg7P2soaoqQHqgrZrb-5Luz7bHs-71cSTvr_DwMAeah_04j3ELAJ9WSx1L2igxrdcJV5uuV7R4liP8oryu9i3tpbbK0ok0iMlaPR4SCzf7wGLwbyDLI5w9xBPLk_YeU6gOggvpeo43xuJ0MyYcAmd94tjgbygLHsy9Rq4GShSViZY8nXZSy7XsoYc2-iPBU0oJw4qXlR_I5XOHifI2XOxDkngEu3Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezbF-wfGTizc4k_nRacRBGv9vO28_em2XoIf65I3HwGAjD2uu2fB5V_xd3PhH8LkXbjP0HnnT5c0v_sJuxKBxDUfvIyhcCpIc85U4cJxplo95VDgHs-EAoBNJf8MLZ-Aupfm0MB0mDNrMmOB3m9EEUceMejj4N7uYFmlDlYC-3-wXd4GsoRaQ48Qy5KzgBdBca9OWrHwJBsYmLZsa_jGUZi5J7A8sqw-AFJ_wM35EkVuH06r-e4KZwb9aLIyAtYGTP0Jyp4_0QNmlUa8gAS7wRKyjKyoGtjHPnyI-UmY5y1Q7RoIJIPbW0SQK3swFJ7EQ1KgxzrUwI3-WVo9o1yLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjCwyTkNznSDKuARCjAVaMLHtytHwA8wpS7fdwamWGiKGhMZsEcI36RPk1TCGNBX9YHKzZwHa0V73wYQN4wtJ9hJw6O0ZHcJ5TmKvN2uNWFNC6fk9LmUoHxWao4wOIHBqBMSEZBE6XPBMtAdvB4kN_4oaZBzoqgW8cE1yuXCcpxraNzcw-3afm3He8iykXf7hzABF_nY0XkJV4c7C9xu2qsIskQG8gedEtL1qk-RrG447oqfFVBUeVlgwyi5KOCJoPRZrdQYVw6Iyccto2r-SJsVTC3287-fBzgV7fLIbEU5uLlTQOQYxBXb9sYSEVdsUjdqMK1CD0vzZIev1cykNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyifKWL6E2h6VxfCUKDOz7cu0hdxzQWy4TrM4_tToZM3rOe-zaIU53BVfvhDfgSK8yiLyLVSZKCdhFhRtUQ_lCOxi7ZhugvgdDMTHjvtjbgrhgypOI75f0JC9VreRdtAucmBG5oGAmsHerfKQStYHIwQKPjqT0HZKKqZKm0GFuKnhB0Cai4XFo3dMrgLrDp3b-QrUFtdSdjp_jJdeV3I_wJhQoWvkcXGKXZYuL7AY3pxHVvtPQxSdniWAowskuUOFR2hZgfAGGr10LwhoqIqPU0OuRn_f7MrpmeP7ZtFEHNc2TNdJ7V0Ekmrzqs0dCT0y3ulbij8HbnamgC8Kt1dzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQqdLd7SdUzFTju45dvye8gpnyLLEMypeX1tZic3txaImEiXShC4qHxG6RTblVq_9tZ3NGS__Vhd1GISViHcfl5ccLASSHCUJEguyvs8RWFnIsrXf6gQM1FJth6l1kyAd2PQ7bdo1j0CqRvqd-2jvmvpBJcA-wIz2p47lZQsxdJFtfZ0yUf19nGrKRP1qbm13hn9ow8Lw7AJPy1qn2WqkMv07Nbfq1nushSJDBXi_4h9pc0KWWLcc8sMVhm4o79OKIMc0N7sNqBScBcdCExtwAkGjnjWdjaPrs5P1rRszd-tAcs2ER5ebU0rtZOiPVR1MjHiZ4n1NEp7WI6FZPRu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUrVld1XL8agfQOBnX7hy-dxPU5IBV23MYvfgFWst-3pGLdWtM92AEpljjIRHrqXOFs2KLxud1zHHjdyJ1jFcuuCY8ozvrOn0kheWcI7Tzdd9TynxhbsnR2n0qvu07eKJmcc97oVHUxCcPddbv77YPi2XPZaAZd8M7rcGrxzhjKOUH25LtoDOU2V0a5wTWAFPOb-0cFc_EF1gZRYHK6ikphlJ-jBmgLD2NudvtN4WKhPg0trJ4XhEElVrCbLdpaTVTt7ImXjfxpuaa1lSntoIjYfkXtPvCB7X8mOwwY_UZmy3rqeFcsF2zZlV8BcENcuiEEXaZkyjhLhd7tTLwCNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfJugIgp3RvKlz9_1aLGwjWMXSy2xohDH-BSYp-um6BQIWLldPtySWV0_3ozVyhGMx_CdgrCeaLNrIB4868XT5w3jkIIqxJNkEqHc6WqTrCZP12x3pRuX2b-II6oU95Mh8xnzy4oIyLxjzKHUA5lD0hOIpt9omFQhjErMEWTTINkcx5QI0xU6UqGOp1Nq3_8qvCY0znoBif8xHY2FGtr0Z2TwdPDkBKkwOmfo_9hzePg-Z-5ecjPxyYj-VOMGPM4pNk0GeC692kW-kB0RVhnfs81SzE4CYl2yFnO-N6KiKv807_NZdknTdtVYUkdFGOoyl9raAXt36rpbaSrrn3B2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QadezHP_IlHUnk1dktlLbRG6VO_dmMTqSbUNhf4yurJPViDvSe4cRYcZNnNItNzFpsVHidxk3kFTRqmBm6_vRa-Z_ekoUfpVrlfCSl_q52X_65Ln-OZqFCcE8jZaBKnPo0VOhljtehsylj-en0uMQVQ6y-uXuGRMN8G_Y9NL-vPaYomniAk6vHWTXhXrf334L4uTq75AZuqaGLnNuz3GcI7Bnf-gg0LlaqLlV-aqThsYN6OOyFVJhpjHa4ewR6wzoPvpzSkT1CKjCUFeiOfkDViumQPEb8jKGV0FWlpaHO8xnR1QM8xzWJJb_aibf9a5A0jbTa1h5O9zWWM4QxoAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMYczhvNIRSI4YLOiixvODPFn6d-Ejg7n9bXqYIV-3_POTLN3xnOQtt5043saQQJZE3L7CURACFN1y8pGLMsji3F80TsSeUllk2VoNUQjK6WlzDzOdfPH4W_4foGOJHq0kFrSAPY0oj3dyyp4ihllCBgKwlX1usRkzHb55Kd83CvSMgoOFgqzjHSxt9J9XDK5Oklmd0SMYx_OHrtunj2AfuTlJ5C4ea2hB3qIsXSqGMa270WfMfWrf6qkV5LrUUlmXVSyRaemuPUwn4lHNW3ytAwl7T_RDDw5J64fgOAkyDCVIB_ubtBo3ifT2qf9lomAJ5sTD6TxyEtVfARr_zS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhRieNflSjqmbTFGkCBjvMN6FWb-ttnPlZaU_vDpb0xzYT1iUu78mztcfkS6VbXWBD8ytpGR6BAVNV1BsIomMYQrzaVQAdt7m6cvT7-Z9a8KH7p8jsNKCzoRLMsZX1GKAZwqhIVvdrgyxy_UwOF2Mypd4BMB2nrSkQQgiqpM2WUbGLO1oRSdUqwiTHfb2FNCmgbkHBMjWktYrO2Cohj-i3cH-54-NXzPV8YgKLRhLYrvPvaLV7Yt2Lq7C3RNUZd9pLqAzxDrNcNUx8sUPGgotGWAAa7iaPTxIcFXO-rgPjxJ6op7hWZoU5fqwRjkUy-5qxvyVwhssuNbUgnjUgBXMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=uHnSu4fMU-5SaiLlasMfwHbMoE653cb2UnsD-3_f7OR6rL9pknYb9XNvWD2dRebuHCEr_aHVxRpjSN9-kDW9DfefK80XRLyKLu_SDRLCBP-AYDdTHH5zUFE1PLnMID_-5mHEeo6wNE93l_pNs7jkjZTZmZJUi5d7bGtsgq5VYfflS2Y47Evco-w11KiDYXgDRs6egOTrX6aKNj4ReiTwVmSkzOm-SZ-9TX-JS1V6i79XnIhsvnIVJ84MpFz8kSqby96EFAg8MOdEkiZTgAN0AVczMhr84JsQjbrPCu8BtWoR2o8rCbfkSf1iXO2uYPTuXQlac_t23QAQVYEFV5YHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=uHnSu4fMU-5SaiLlasMfwHbMoE653cb2UnsD-3_f7OR6rL9pknYb9XNvWD2dRebuHCEr_aHVxRpjSN9-kDW9DfefK80XRLyKLu_SDRLCBP-AYDdTHH5zUFE1PLnMID_-5mHEeo6wNE93l_pNs7jkjZTZmZJUi5d7bGtsgq5VYfflS2Y47Evco-w11KiDYXgDRs6egOTrX6aKNj4ReiTwVmSkzOm-SZ-9TX-JS1V6i79XnIhsvnIVJ84MpFz8kSqby96EFAg8MOdEkiZTgAN0AVczMhr84JsQjbrPCu8BtWoR2o8rCbfkSf1iXO2uYPTuXQlac_t23QAQVYEFV5YHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=EHTk70GxoWsIjLQ8hu_ZDvKhTt_7m0sf4wWRyRNYHwoU2kyXJTSAhhzHAkCKKqJkugxSP5vu9M9OxkOCVV7Cud09O5Phm8xXx5tx2rLWKqGzXOtjetk_YutPLfMg7dTd1Z-VKX6Q21I0fA7VjwfSRjqNzCUr11L5BKJPhcppA3cph5mznZL9RDpHybwNzVNgq38zJ1PK22hH-OmkWuZJwOPdftxXdB9K901pluDVZ86XfLnHIWOleYf0S5QgdRhg7v-3JDhGMdVeybh_zNzxE0TMcU0U6aeVUsnkaiCd672o2a5xdP3H0CoLIGzpBmTuRLjOXVhch9ehMPThLZmFFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=EHTk70GxoWsIjLQ8hu_ZDvKhTt_7m0sf4wWRyRNYHwoU2kyXJTSAhhzHAkCKKqJkugxSP5vu9M9OxkOCVV7Cud09O5Phm8xXx5tx2rLWKqGzXOtjetk_YutPLfMg7dTd1Z-VKX6Q21I0fA7VjwfSRjqNzCUr11L5BKJPhcppA3cph5mznZL9RDpHybwNzVNgq38zJ1PK22hH-OmkWuZJwOPdftxXdB9K901pluDVZ86XfLnHIWOleYf0S5QgdRhg7v-3JDhGMdVeybh_zNzxE0TMcU0U6aeVUsnkaiCd672o2a5xdP3H0CoLIGzpBmTuRLjOXVhch9ehMPThLZmFFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=ph2Al1KoRSSSvBhgBg0icZERDEpDQUxsI1I5x6Rk_lttCBHy0NlNilFyVtvjpYCp7GPdsjF8ma23V1HSjdPVup9UPwT8TH4f7CsYpeGmGybqGZ_RC5-sQ0aNeCjAfQueod4mcQ_xz62wPn5PHWCaf9TYGVa6WDCmR6J69AtvNDt46DlXq_veAYxNa3_87bNXyzvTHP4pi4N2ACchzLaVFgFMdYrbf76teBOPbWE0g9qysqH-wKwh2sqv0xiDB39bzTIz-k6s85B8inQjLx-l3J8i-z31fIfDCW4-3VARAVVorGVAJpI8KYfHlrn4--Nn-SjuP4_PpxNL4AbVvJbcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=ph2Al1KoRSSSvBhgBg0icZERDEpDQUxsI1I5x6Rk_lttCBHy0NlNilFyVtvjpYCp7GPdsjF8ma23V1HSjdPVup9UPwT8TH4f7CsYpeGmGybqGZ_RC5-sQ0aNeCjAfQueod4mcQ_xz62wPn5PHWCaf9TYGVa6WDCmR6J69AtvNDt46DlXq_veAYxNa3_87bNXyzvTHP4pi4N2ACchzLaVFgFMdYrbf76teBOPbWE0g9qysqH-wKwh2sqv0xiDB39bzTIz-k6s85B8inQjLx-l3J8i-z31fIfDCW4-3VARAVVorGVAJpI8KYfHlrn4--Nn-SjuP4_PpxNL4AbVvJbcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mga4SZTC85KQ6dvDsNa__wlCBU8qPydyRy728YU6onJDParndtfPOa_4KC4HgG6xiM2acMS98Esesgn_7oDgmhfG8pAMhfFgUlTjSXK9emzqm386wQBhF0mXcE6Q_JITqyfHmkL2_iXdWD_Fz3GKeDMxw90IG_-C2mBPUhIuJFNF0wsCgeHvrvdZXlxiYfQFnEtB7HMNnLkTvxpXcnFnmiFWFwYm9xsG4nEFqep_g_cSOBIaYd67Oyj-Wqsiyl8tZjTiIkbvQ-XZi7hGS7jkAGvsfCwua3oFKtfw5IVHiIPHDWOPaOd9CCNpeSdMUcoi5L0VA5nzTi7v8C3Fh7ovvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HbwJa9FJJd43b-bucxF6WymmUDlDSfNco6k-TlCYknOk5YuCtLkWYCqjkXYtTr1E2SDURlFaa1tdf6rFEIh5jPb4kL087VJJsTEWFPDOga0KsuvBEWlfqr4bMUricS0lhK09L3WO5D1AmZZpHQG_eoMC01jehnoJcuFyINhysNCReJ36z9SFYlkvJIS9D9lJS-b9BnjWLhsLsEtPtxzIhSDcXbRotpp9Nsp-RTMtOcScxDuZAQlsDKS1EbLsDk2HANdky0LqjKjyYxPqSAi5-2016NcsDIFzjv7EM56nUlpfbi4OX--iZKHjQgWG0l92aGUKzAHiQT0ruCYmovfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu9VCnP756er6jbg69hvFuKCv4t8CPnf9gQ80JWxzMwsZcN6_Ew5SxeXXtt_oEwQqYVGra6ybWpXgbF-g5bIFJIpRnoqwcSEQaCbMSD_YEK73inCNrwWgcXUZPMUkT99CZnTR80QwiWVwYBlHtZlzRCipDI_B_3gI7WXfjFKvcFP4XGwLsTM0xk7Mq93THp_0fyYcaP23Og4sqZIOgefU4i6_E_IRu3kDtZTY7s9dhPszTQmvIQ5bmFw07gl1wZ0gSC2CWcmoEwAAwIy1AkFo2e0kjGPTi2fmQJZFqSAyptwH6tSWriAnOGQsyxTABtE7p9H4q6vU4OWSqVVBhZfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=VBdh5cWDhkxayFeSRnEm3w-Shcjf8kdAnlOZA4wvjZyG0uOgmlVIiTeyCWKhOMRErFO5wQgYq9XyrCmOgIo_JmPatK_Sn1AgdvXbRdbs17gA59bQjh9-ciNWmfnDiKEYBgGhTZz2UX0DWz4u_mwMI5zyPbYGOxrkZ9qvnhrIl44KEdmvx_9Fj5jvnPX-DpkOe1AfjZYAy_3vJwnuTDeY92NHrhszrWyZ90g-xWvhPUT2q9-lDq7b9QLgvtPQTA3BY1FFUcivotHc9lWiCNgSj_Dmyj0scfOCW70nuREQfiddyik4Vcvy6AKHgocz8tcjJjuHDCdhN7PWrF4E5AnM9qctOnIa0pjjTjw6SVGGTXe3NCviibKiGqfObVez1A1FCDK3Xn2BfgiQLcAT_ArI0lLLp1sykyOI1yXtL0enAiSYilmF2CiaW5pUO3jQbBPdzaHNPhc8vn-2Gb2zC1xU-h6zU1zLoX3iA3Ku2rQm2j5kz23TPEb72a0eX4ouxdtVufULj6-wb8l4wepWtgLZbtFseIEtY0y0gwfqZnrOkv4Fqqj5aNNgts-CZHkKnKXmE4jUmdot53WThMCoSyLYwBzc_r6Jxw-EaXegorGwqXSr2HdvT3k_3H6IFjFNq0MKVMvqqPPnSmKMavLcl4hPKwCCOvjvnrHYbj4HE2QkR5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=VBdh5cWDhkxayFeSRnEm3w-Shcjf8kdAnlOZA4wvjZyG0uOgmlVIiTeyCWKhOMRErFO5wQgYq9XyrCmOgIo_JmPatK_Sn1AgdvXbRdbs17gA59bQjh9-ciNWmfnDiKEYBgGhTZz2UX0DWz4u_mwMI5zyPbYGOxrkZ9qvnhrIl44KEdmvx_9Fj5jvnPX-DpkOe1AfjZYAy_3vJwnuTDeY92NHrhszrWyZ90g-xWvhPUT2q9-lDq7b9QLgvtPQTA3BY1FFUcivotHc9lWiCNgSj_Dmyj0scfOCW70nuREQfiddyik4Vcvy6AKHgocz8tcjJjuHDCdhN7PWrF4E5AnM9qctOnIa0pjjTjw6SVGGTXe3NCviibKiGqfObVez1A1FCDK3Xn2BfgiQLcAT_ArI0lLLp1sykyOI1yXtL0enAiSYilmF2CiaW5pUO3jQbBPdzaHNPhc8vn-2Gb2zC1xU-h6zU1zLoX3iA3Ku2rQm2j5kz23TPEb72a0eX4ouxdtVufULj6-wb8l4wepWtgLZbtFseIEtY0y0gwfqZnrOkv4Fqqj5aNNgts-CZHkKnKXmE4jUmdot53WThMCoSyLYwBzc_r6Jxw-EaXegorGwqXSr2HdvT3k_3H6IFjFNq0MKVMvqqPPnSmKMavLcl4hPKwCCOvjvnrHYbj4HE2QkR5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkY0aNkF_sNfA_TlK2DG21Ps8sN20jO1HeQYaS3_VaTHDnKSYO2pnevF-XV8jGcuK_plsS-TEfE-hwFH_DZ-QbzT9SuPxVEGoLm2kPjQaR7FOV_r2FtvLbT6WkWnm_bWtBz-IacLr4JyuN0xz0v7NzbU6yyJd-3Vmfl6dm2AtZp3Crvg9iUOS_-V4hIcwYEhfrFpdGEhq2TyhisMKJHtdfpLdGOK5_wVfPst2TLjhvaKL4h9Hxzi90-EfReOJnh0LUVNqqEICATPnS5ObVKnTBq4v7nct6Y8b8b07M205rmCnJpRcpTvSqodLPV0dU2JpH85ZH5OpaQShUNJq2NVYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHNO-70boQEbcd6koBR7FtATyXOih9IiK3o44OMejPViNa_eU7QwFh6CufmxLwFTH8FNiwDcNaE5nfrss3nUHVDtiC76lmxznkpLozUjo5ef-FZ2OdFCqEgBVS7UGVbHSYykKh8IGEP7Dny1mGryw0c986YGSdJEuJ7jij9AN7OXBa5bFopIoyCzQ_yPdlsPNmJpVI6kDm9CInDkXvkieedAbHarNubWom4ze8jI0pKj7qA_O3qThxGWFPW1xVFR6aTkZ5EykX2hfv0lyM7c99ujIyUsBh6WGll6xOswu3d4F5_fR7KmE_gXRKsqPdQGpXHlfA6JVwMj6ax0ev2I_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcTMjbUPYgss_kvapSudYbvLhPBeooc3DXTsnsT2bYZoEAV3Rq9JY4NAX3n-nCb-nEOOrSawz0f-orSOAc-q2D-58oBqza_H3P0ExS7URCSizcPnMfWc6cEkbo8YNcb_ISh7rDx_v83ROPM9Y7zVDQ748e1CYqCpiNAtQppF69B4oLm4VBLs53egDJXNwKvJzDnwO_a_4X7HWpRb6p8jSlvaVXO1aFC7piTwp1I6wYEs8hlZmtmHmf85a395YidnayQjG32IAXFhhizQTi1yG6rSWMBh5k1teJN5Zp_0PKl1rueF3wgokd5pLpE-TYvtpWEk2KjTEdBcMRDUB-SF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFM63S8VKP9FrnEYdnX6fejvttoaNEO05-mpEWW1F3u1Q2_K3CQ1vbyqvhWQbyVz6p2SzltBXmbl6gb2IQKmV5rmDW4L-HkvsG8HK5n9CnvCI3MhKo6ujZTfrl8-vuC2yabzFyE54cD--s-_NYICde6cajkVRfKSqzgUC2xVD2fNxZzotU5Y3HXd-NPh4HeOCCJxyWiRir20e1O5pVbpz5J6ADNG1ZDZme-Se93DbjWZSvvyqDgWNNyaAN44koC2Z2lFJrkKjEUl6RLLQ8j7mH7Dkm1bkdcho7Njdn5aeFTu9ZuyHzY-sui2S4aLjWdabWLeQcWf_Sf5OHPAB_N-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND8FvYCRyqAFE3nqw2vMhsnWA6T0HzLi8ufi6-9VkjUB1JC3ae-FKEqgO_V1SniJQs9iEH6Nrr42lLpNFC4YFY0SJxymF8rCsgdBiqr64IKWL0dr8_mhylZwvEmbVBROL4mnARQvs_lSQaYPxq561pxv4TLHZmI037EswRnt_NNjJ9wJK12BJJt44Bwkv8lrfjYYqgAbx2xvoBfOv_H6GxTfiZuEeaDoFq02IGmzLc9lzGgc8uzLb8wYni7FEswVYr2RBCNw71PRt7H7ZxAIC-V5vKLFCu2Y-m0foReY7HiPmz1eZvcZcObvvEiTyZdIq54tpQSdjHFuR9NsLRcR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWsvKUc_sPs980esvyL-b0NesYG_KbGvY0komtPWHPLO29Jwqwt4nuG5IhRZir43XPgg9t2zyksTNrkcwTYkFiPQu7bAmnPTT3LhHcjSMgN2_-tzMe_Ql17mw0GCF9Ycg2pIYBVgd8O6ylk12dZ0bL66NvwlFAXLaHfR53Y6YTUDt6GUw5OtoY7KMXJbDjrGbsIt1YxwBBCjG9vSclz7E0Da7nQSwzMnEUXegz_ivQMRFtAO7xCWjqYOBcMkTN6E41GDwsG0KcrjBxZxriF5PLUEp9VJK5bQYvYbgeoEQMGfHUQDiHFNt3KmIvFzMkCy5UQZG5qhG2tYJRvsvRl0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqo2w0evO7dCZg7xauVPo315o0_rmNY1Iq4ZtK470WWUhOvIiMYUcsGXrv9BA2UBx6ecdRYV8Z2ufNt-zoLi7VhE5uA0IRnNSDLXzaTXNFw_pEkv3pn4LkRlmMwuAQpVSZX9INt2yL5vSJl0-DeuvkjpQ6BmdGxm6G3vYp2zsk9OMKXDjPEPQZpJoY9H-odDUi9mgdhQ8pH359SdCHt05aB8sH8fwBAAp8MMXt9uedltDvXyxDAE7PY1w0EojE8LfOQieOEV9B404pe2Ig25LTeaIgX0oWI5C8BI2Z3lzpp6fKiZVJoqB-HybARMXkVtaHE04BuWLHbeknRLre1XZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZEu0zSpwFKMsGCHZqm3gUPEgh5MpWV36j7DjGLxv-Sh9oQXCFZhWntpJ3US2P4noSH51fSv_1wXl3IWQtIFBNxqj7StDlCWXZrbQNMPRVyhV__tynFkfSHm12rx7Uo4blSpLNANVJp9nPlo7o7Tr0BE0tI5zHkG2SoY9jYWcqcQOQvp27EcFiD7m8DHwjQba5sLToDkbw1T3vtvVHReZMvPspqSyMXr2D4mAuNYEl1o5W1fWoWwCjgI7JXWuHHbM_AnkwbwjK1md2CrfGkmsMuxce7AjOnCpNJv8zKOoza5fQZby37dhFvnTjBwWI3yTowIFippIcjfJzCkTvzdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyS1yPQer0Ae8ZWkcKT2sgRkb_VFErvw3QYR5sAsLfGLUtnDvA26SM4lW4ftmqfoNbDkoWHiSN_78l8W_aKFdd4xbzYSup3xbTyb3w-s2n46JJlFORNK-RnAWK-bBPglOBkS5vo_Jc-VSGOlNZdrDJSga1-BDywP6ypNpnydlDRAvDcSB5ndw4HBroI9pa8O-t-amRiG1lQMOYPV_7In16U3JL4EN-T4V5Squz1BChLjXct_T0-KnfwozCQln0PYlt_HgoN0tDKV9kindEWuhhnCejsVDqK5GxYEtlgz-vtd39AJQnGLsFSU7tS4k50Zdi2_m26wvCQ2JhY3tlBZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deUNkXnlvfYJinwGFyhUn4FcQHBX4wB8MBSf5HZFCzPH8soEdhqCEe2_gTM8gAx5tzBaUFkwmAg3ra5XY2RY9AlCxvnpmFBhxzlVfZ2gl5Ug3quVvRBQQGIAhy34xoJBrjJyOdLI02D4vk8pr10ySN-E-U_XwkEjBD1rm2vyjTNsH010-d4xRSGO7hEl8pG_OYLdt3S0JDjuQbZyV0waaB3HBygkYZWW3jQc8Zru_KwH8D6j0xnYDK6y07zAHH0ZbhCog_bz63Pwtu_I94IVhoGcJp7ud00L5kerSY6-PeNXTvJabsxHRp1UazlxRoQi-to5DMTGDsSJWZhnSs6-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6XB1Gq80900Fpty_tCGjcmGi1UAYRNjOE65TgR1RmN_wHhcttG521F6o9JNgFRUVWakmBzFIrpX1VSilxQQfWl_kcYG2C0HjRm_6B7QfDdWcZXh4SkL7RHiPRce4hfgy2Qly5kvc9u-W45izODmxcb3pOjnQwMWISDoGTI9HMmet2zfylwjJC6kl7kuF9FALzdTQFAb80jsg27WO1kuiopaG0zCKpQ2lnL89HZEtJiIUzXuOg-x8l65lfcxEngFikGoIizs136zJEx7XmNmkIXqDGpcrxY-c-0q0F8kMZu5yI-wRBRe3W4mjoWhsJWyC-DZfYUxUwsSYiYyqutg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7bGRE4DV2PKY51qfswssl47ddxuSEAM1Bp7M6yY6khikJSIdvIGQ8Qe0CW6CuhbsNEyIWytLVkViKs7s3oSmr59dn5tUFLC6OzpOHxQGMMLEYu5NFtuoHbQ8FeXCW-Cr3y3NKB1-6_q-qbCyzHE_4xuorkRmqkZ3SdZ0FRdZsdMPwSjptVRsJjXLicgjywgEUuY5XTG2aPNol2S_6e4pDlbn-3wLLzITj99H_x6R12a5TfFbBCZwQsoAXDTCxprUdVSPA421lliQcXYF7q1n6Xwh2gsjUQ0Grm9Rz0_--UgdC3KbpOOwO7cXev-wIelHK5VgP85PIGl3Vy5BVaNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=Py8xQ9EJKu-Xx6JPIKgfmjj_b1EMG_lKMPXfID8SLoWb9a3ai68VXV00dOcqRPHkXRLisONUe6hwN-jdHqPtiG-lAiyH4WmAKIU3RgApkzlf7OY4AlNcZbVKTKkv6UDGCZ99BXOnWLj_MIF8VLTyrk6s9RUBd7B9FHRtEnaeN-7Qos_npbbQKILRsbRDUOpGBg6No4aBdt222Q1SH2lViG7XubBz9JH-vR-Qm5kIOdlBydokSRRd-X3FbifRnx-Ou87ipTOaMDwnqRHuQmQD5TkvSnnTxUNidewWIXTWlAl5ZCIkYof5r9YCIs5boDuQY7V2SjSw-7kfsjON1k8WiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=Py8xQ9EJKu-Xx6JPIKgfmjj_b1EMG_lKMPXfID8SLoWb9a3ai68VXV00dOcqRPHkXRLisONUe6hwN-jdHqPtiG-lAiyH4WmAKIU3RgApkzlf7OY4AlNcZbVKTKkv6UDGCZ99BXOnWLj_MIF8VLTyrk6s9RUBd7B9FHRtEnaeN-7Qos_npbbQKILRsbRDUOpGBg6No4aBdt222Q1SH2lViG7XubBz9JH-vR-Qm5kIOdlBydokSRRd-X3FbifRnx-Ou87ipTOaMDwnqRHuQmQD5TkvSnnTxUNidewWIXTWlAl5ZCIkYof5r9YCIs5boDuQY7V2SjSw-7kfsjON1k8WiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=LVJsLjRON3hQ1Pdy6JFeXvqz1Ak_avt737DYSOxgzAtdrwLqvLn7XSwp46Mna6Tp-Y54mHZIPBadNsMF_qG4cLUAv6WO6asPkDddxi9WlK3VoJE6atSt5aP6AidbRUfIzRI7ULpA6DolLq_oFSDvnT3QFXyB-YnPJajrYwgzLGXf_rgktZhwvLjZg0sVl9n9Ie2EDBYezEvUjD8X5Ltzs4zxO3eJARmhGKoudKLU5Oan73g8InXq1Bx2Lw1r9L8vvvqkGDb1vew41HNPBOMySefUzcqDlJmGeWc0l5YfvFglwdGJSWZqIOIOJKYM9bfHKC1h9McrpH6L5UnSp39Lwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=LVJsLjRON3hQ1Pdy6JFeXvqz1Ak_avt737DYSOxgzAtdrwLqvLn7XSwp46Mna6Tp-Y54mHZIPBadNsMF_qG4cLUAv6WO6asPkDddxi9WlK3VoJE6atSt5aP6AidbRUfIzRI7ULpA6DolLq_oFSDvnT3QFXyB-YnPJajrYwgzLGXf_rgktZhwvLjZg0sVl9n9Ie2EDBYezEvUjD8X5Ltzs4zxO3eJARmhGKoudKLU5Oan73g8InXq1Bx2Lw1r9L8vvvqkGDb1vew41HNPBOMySefUzcqDlJmGeWc0l5YfvFglwdGJSWZqIOIOJKYM9bfHKC1h9McrpH6L5UnSp39Lwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ar8rfmYeFLs5ui5EmhmmOqR77Lpf0zKxVYTxNgluPI_oFb9VAfH8J_ccLk_BRTyqBq1jARLtuFg7jxyBtA50B1W5uc8gGPooqry7x7bULCWvs9wq55Xg2SX8qM_SfJ5x3R0XCpgtZp6amhcVtIboCOPtr-UPgA1pkotgHGgJa4dS8kiiAiL0FI8Z-mC_XTky0imtqXw5vmC0S-Li1L8djNmRAw_R66dKcJkkd2hkzCKD6JVtfblU67ZqVh0Xkv89BTZskhnlDqdNiZrBy_z7T_axJcMX0ONV_hN3AGEZ0fnkypurX7_nTbTN6Hc9Xu2N8H-6LyOjBUWskwECX5bUug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9L7ntDs3VpibkwE8yvFZmTXWSLqX5wDqUc3YbHLmuQDip42p4zyRk-AK0dId8ruD4EUHmD9_PwPn_fo6-45EeK9Uon5jkIb4cHfGCK6R33yaQl_mVhKWP4ItHnno5RZZAC0AG2Pj5L_Tof87VtRoeadudmZedDpZp7X_mjqNPacnSdHMU6nh4s4SzXI3ZDjTqdoxF7SxpePLhL1TRHlXAhyvt0BwSJsaM7P2swfRq3ioP9zlI_ZHIvhRGJFoZKVhLXr6rITmP58AKQbU193JLrkp1Uk_iPMaNRMu_c3gfXZQC3Io7pXE4FjBu9jIjCGR9MtZiewYPd2L-_IP2fUVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NFlFwCYFyxn4_4SxwkUc3fOJwtvOrFO0S6vc1giTeAZog50bjPnRzJ6xOE2Z7Gr1gdDmMXvRdIQgHv2BzXOWjB-QsvFFNqgbMDoSPlQ3Z-U3LbqJg1wYGYu1DAfsh1Id6MklsalXjrQpCcdRDN5xwAj1aSAKImQDLqthGPqCdsk8N_5j4craOongkt0jkU61BfIR6Te9o8YS3Fzv9XJpaL8L0R1abPIcze9Y1DJ3lqHTkI8HesACtIB9GgRIy3j4dpIqTHcTslFkPdez6f2m-uM8JOdm96lUadLoE9JdhTD5n_ClqW_zQpeAa81XFxYnm5T9f6S5muz3d4ZwyrIZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0ACcmVySiOyE3anz3Y4f39-LGFj2SuGtSXWvOsWu8juW5MaUEem30dIVJK3UNPSndONBEHw7lK7YbcNaXk-xDpxBWNkOLRxX9N7fl1WPFueQwdEwdiJPJwGru8Vs_tcFX6DTD-omPGAQaI8hafWKw-GjK-Yk_-w3sA3fLRX2kB78EjINr1VOsGauFmwhVkrd7zyzBtovdFomnDhDyQqbmWuAki6Geb6EwhWK0eIbsYyyOFLs9MYMwbZjKfhfuKnUoRhkZys_U8yqhnQpKj3GxuuulqWLFrOYgpiFuhJL9g2cGRuEe7eIWjughJ5aKxlV8OOdgmsPl2483CGjhIEIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_I6j4vLQjVugongKD6-uTnPu5Ig4XkNW_4XO-xa2YFy6-JeE40Lom27yNzTzYhUSubbXGV_CUMBDzijuqTgZeeDKFkScEZ4a7My8WfnrqItYwhwogZTvY0fkrtGOI88zjZUbhW_XvDjHTlUoikk2sOx6gsoAUbvcMU9b-0Oc0DgoEbaWP9qEbDpsCpE9t4RYJiHyCllmkqbiNyKZz8udNrELpHPFDOefdAokJOLkQuOcsW8723eEd26_YsOrIXkDwRnaCD2qWu2vOTxPP20x3U09LvRQQgsixcs8q4wysdrNXtXTc7M0La20xkKCUt7EsEqq10BBiKHQxYBKASvyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7ADqPknO0UjYJ09oRF321A_mtKvV40B_YRcj1AN0AgEQjMsLIt57-5mS3JqZH8-fIVGuuSK2ugWWE0YncqewLIf9kz9PO06iJrQ5gc9eyGNeKcJlf6jD2aRCp6T5yvxrqreByxccr23SLQb1VxTMu6-3ldWYgYoMeqiuJ9eJaUVdLrLl31KRs5fWK1uLtDg1401aK2Azy9wDdKSZlHArDwwM1B1uMQ1u_IeMZX69K1qQtciSIVota7cP1noPcgTNTLDp15flkgVn0PbrXPtNeaA2uxOIMR46_x5Fo_jUZVhq-Y4vCS5CuksSZIs9jYIvNZyJfTo9LNPt6FiLqOdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4e7dKpbrB5Zrs5B3efkFeFPnSMhXRMdFXb3sGmSb6HJ4xrj9SHLEva6TPgG1AKCXEXpMnm-9isx0M52g9Glqgr3lWuVhyhtK6dVedClLxdzWIb7-ZW6YKHPTMkMntzJ2psPBAWbvcpLYeOZrjTeLWn2YDh1jXeVjYx2dOA52CQSwQXJfOHAcRaCrNgEU1xVbOv565xHeZg24r0b-D0dMDfVyyHhEeE-LLJ4QsQC6xI1y_C-ECZIVZ-nbcpqRA8q00_8CvHnBnyFbQYxG6yea3kc_21jCtvD4Jyd1Z5wfCpS9w8LUl_K7WZLOeOWzDPrjuUIBuAD5pl1XluRJ3tebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjVEmAyc0UXFkMeqe0K5V-jh0tiYBNBGl_xKWTrw4FxKQbQcLIED0Il7Y12lHLKTsjPlT6PfvwgQMWRKAPBxWiAOSaqlcQut959Wb94MoLWkL6aQeHR1QgNQcWfraD_yNKgTdvLxhmlU1FGVs_mUK24AyxkH8H9AwU3luK2eanph7otWl3yrxzCvvtDNIa2d1_Ni99CdsmZdQlcOZH12Wg13sps0UB2Z2rJXl4xsU0CxculjzG5NHF4HvU4nXF5oJPmsIJ1LnaJLUJu7PGe9VOPc9XQJHpHPreG_lDC87cWPtLG7Hg9vyvvMbKYif6eorOtRjLiEbc_TU32IVJvExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Di_83hvAnbC2gVkXAEvhbyotjn0I6f7ADQtFJumRMXm_-PBrHyoEKcHD1M86jTw2SipOFf90VYvW2lvZ-L1CNjst8mMddLf_VKsr6FirhtJANi28RM-qgzqsBsMNjxidRPypqVDsuKKX-NZq6RIYLyWkWyP8RvpCxYzrcZjcxQhodkkLu36AARJjdtqWMxYUK7KHb8ee7d5qH7NUyB4-2TQgIA14qFqZCFQngsY1Dc1fHTLHaQ4qYV3sS1jkrr8SUmt1eDQq6vvYkpshmZxDW7VuKCci2RoUJV-rj1KYi7XdpmGkZf_P1a9TkDEhWgaCMXet7SLV-wL_kdplqC8pag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBZG7ru5nzeayTiP6b98cPwVBInXSCr8DEjPwnLMQeLuGpRuABsRYVIZW6YBaC4I8om6NYFZtC5EtKLkpjvSvwoWZYmngPrOvfyKxKv3r_01s9gRPdKZNHXZzqYd30Y8tLLELMze7fcKpRpsg73FNm6UrdDeTtHf1H-VH8K1WalcfNtXCSFOhkbGnqkp7CtT88zhFelCXTZjHurw7Fwm3e0n3Ne7vzkr77ou7RmJShHMu8iZhDfzxLQF8Yd8vlCQmLyk1GGkM4V6-p2cAm7Z46WvtRHliYUEc5Q0i_RJthKtSRxNYxqtiCWyTFYLzEDUs8pCIRbVRFpZmHPELI51SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=GqVXBZIaAmP2phq36rWXV979_6YSigGBpU0oBUVxt79tovWs6Q5-TZxcrd0yPEbQeQebvz8TF8x0gYGNVcVX4eDL0ZOAGIInnyFXX3prk4e6IaRobZNflgV_LC9BeghZ-63ZN5svs8sjLpFTqXCmujaFJKb_C4F0a61EoeFy4yGBI9feUPUxJc8iHUxZVQGdqp12A67-1kjxyYcsktOr1quvNEMnO57NKgh1ZR6NM_TkrnPoSLmZDMpxuNrX855GSHBrYzay63_uSL7ZvgTC3mpdULfih2JKvkJDT3Y2OBzjp0yznDakm2-75xAGC_mU6rS2nGTyQDXivUynx5IvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=GqVXBZIaAmP2phq36rWXV979_6YSigGBpU0oBUVxt79tovWs6Q5-TZxcrd0yPEbQeQebvz8TF8x0gYGNVcVX4eDL0ZOAGIInnyFXX3prk4e6IaRobZNflgV_LC9BeghZ-63ZN5svs8sjLpFTqXCmujaFJKb_C4F0a61EoeFy4yGBI9feUPUxJc8iHUxZVQGdqp12A67-1kjxyYcsktOr1quvNEMnO57NKgh1ZR6NM_TkrnPoSLmZDMpxuNrX855GSHBrYzay63_uSL7ZvgTC3mpdULfih2JKvkJDT3Y2OBzjp0yznDakm2-75xAGC_mU6rS2nGTyQDXivUynx5IvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS78Xv8YZ6KYEFqeHQk1pl3TjGPu8HVce5me-wpqkuhjMFGbM7_dp70OAeheSK2fM_gRhCXDQDcG4vDSLY25WBJkB1WuznAMjh4SegNy8j9GeubjLPLDHlFOus5gT0dnODvLljImMZcQdY-kNAVbH8Qx_ArIdSxb6D2ElvMtV-tubBa-4SxwvqwhKu5LWNl7aank52FC75iDuP_leria2biLr4rpgm3ulJosm8EBOAikurbUofLwBU2L-5v7l2ZyTsfUCGfgfoXDtuqT5nN2ZDaX_QIwqNG8XgKrD0KCzoiaHlrghw36MG2jNzCBZI-PoPwMNdj_JSfrQsmWqfOcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=Gp95PZAQ0UCh6tjzpBbhIG6OdDlAwG_52mFPsGj39CdUlgAJ3QoNVSZ4UQJF45CamdRFKIZb-L3Ti5F3ADvX4usCq8VMG5iZQxzHLMiujgN1RBg2wcLlKNyAJDCdY-qFtpFdoECjbnlMyQoRhRj8MRIARGUOqK040ezpmMPGZRg1shvXKzZWPw-3UVNtXPMFVFrHkUZPhP-8wDDS5d5OH0sbDwHfQHqCyCniOfn91lV59H_fUMJrJblQ7BlDqIX_2naAqwV-SRiHFYSijIZ0N3acihH6s-fFA5Kqm7z2kQ9wiYoT1yrj5PjPO8MZ6KbciGGaTEUBmrxtb_foXY0DRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=Gp95PZAQ0UCh6tjzpBbhIG6OdDlAwG_52mFPsGj39CdUlgAJ3QoNVSZ4UQJF45CamdRFKIZb-L3Ti5F3ADvX4usCq8VMG5iZQxzHLMiujgN1RBg2wcLlKNyAJDCdY-qFtpFdoECjbnlMyQoRhRj8MRIARGUOqK040ezpmMPGZRg1shvXKzZWPw-3UVNtXPMFVFrHkUZPhP-8wDDS5d5OH0sbDwHfQHqCyCniOfn91lV59H_fUMJrJblQ7BlDqIX_2naAqwV-SRiHFYSijIZ0N3acihH6s-fFA5Kqm7z2kQ9wiYoT1yrj5PjPO8MZ6KbciGGaTEUBmrxtb_foXY0DRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXIXQJip-tpm96kg5l9rAgJ9GzUZHvwIGDHz-2NkN7KIJj5hPF46jFFpaNsHWWhrNIbZ6kD4JpG4f7InX558b9nhW7YGFeNXsvGa0NK66OP1BiuglIu4FH9wtUvw8q-YByqKXcGg6q3QIAJb1mYL7h2swyNYM4YsS6cQjYOg7A1ZTmhBcJqS_DmVpI0EUzpv3j-bABXN4w3qNl4sKE7FcOKdz_EybnwNCS47atml_4PymQHKC-wBghyzku29dw-QPHLGrc4JmcUS5T2MQh9C8NR5aVDiJfkZgxm2-n55-QTs0AgWX8MhdZYOwGL80sAVaO56NgSToevvkeVqzn1wUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsuUREkn-XS0cyUPIbq1kWLINYM62pMySGvteIFl7xqkVwMHsSbo2603LmzGOg9KKpkJAQQfRCBxa45j4OeYlb956XMJG0iTF2BsxnLbGfkZsriycPyr7uj9wQGqgJjI-FJ-zm4cbYVroFi4ZHGfZ5UKEj2dgKUCWnSfZ3AtWWsue6bwvMNqaleFaRvGKX2rANg63SzZYxwnrHcwnXnT6k-7iFslzNIqd_uIl4O0XULT4JejxHDyJJludd29FMX9Rgbb9kperaEMeT5xin7q0nfaV2j4LN_FvdLXCFKyTEOfylW7ZfsVdtGtk71calOdaSgItQRWzMtqhbqZi1hErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=Zf4WrjTWfJ043MnFFHjQmCg5k1_4bDIiEbWn9mTAhNOIKjzN8tAVV8qEVPRanX2UyLDgZ-QKiqma_QRVyPGCSxoLXBLncYPaKxEM0x0ijJYrHatXK44JSBqIaGXmbR0lyFzRndyEtheY2bv17_chjjZKilfjY83WaC7_VnS1jjTTyhWD_5olg_sHnrEPX-xskgiJhOjXwN0ApoiYWonIhmLfUjd7R8BHQ_qvEEcL1JHqeIBHXdA88c1PqKzTs9DakXNVbxruwjwGH5FG38vd62BhS_JJWAsuWexHIFranc7rchZCMlUaCsVkuKFxH9Ob3ahlL35PFe_20Ui4QJAD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=Zf4WrjTWfJ043MnFFHjQmCg5k1_4bDIiEbWn9mTAhNOIKjzN8tAVV8qEVPRanX2UyLDgZ-QKiqma_QRVyPGCSxoLXBLncYPaKxEM0x0ijJYrHatXK44JSBqIaGXmbR0lyFzRndyEtheY2bv17_chjjZKilfjY83WaC7_VnS1jjTTyhWD_5olg_sHnrEPX-xskgiJhOjXwN0ApoiYWonIhmLfUjd7R8BHQ_qvEEcL1JHqeIBHXdA88c1PqKzTs9DakXNVbxruwjwGH5FG38vd62BhS_JJWAsuWexHIFranc7rchZCMlUaCsVkuKFxH9Ob3ahlL35PFe_20Ui4QJAD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3SQ0VyiEN4ftYHRxW7rvsyluoowUmXimWMluR_pSda40D1oluU8BhmQxeaBwAAZmFauFxIaVd1q8k6834adtw8thK7Ht1YqSIZZcpWaThnI3qDRSzSY77hPcjP7MIYINDTzeHY4Bl98ntGC5JOddTCgEr5Q3hAS1yaIPVajPpqmakp7SIQdt5C19eEx0VILVTSIun-EcptqJ2HCzn5MV81sikdT3v5cTDodsKBw1HKklw7YRwISGFTJVODkzxGe5przXJJoyK-RbynWsEUIiiXmDyCGaJIg4BbugMx0OxIVpt5s1vZjfpiYgBm3Gr6gCRcgdgp5rlqztpHApkzp8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fozh4sctmoXkwYMnz4U8JmAiEADoMjipUQvKQjublNUAP46SzejPjwtwmhma3lBM2NqNK_cbK2fpKr3xorvVXgLWLrBSdRT2pTmVXrefQKrea1GRlKgkzgauXQfTwgAX-a3w4iQHn92RKSgD2y7K7qW44Iwa9z1-MgGBm7iNSM8iqg9mew2NTZGIYd_JwjsXu2g1mZSuQUblXVjI05z1kELX6OschxzQ7yTuwsjc1-WTf21fVydp61M1XjIAA6UXPJpG2mJkdqBMKwuLdAZFHqOlPMdZpLEBAxB8AWmAe9IZ7RnASlvmJv0Q1YVePfCz2xvU3INkXBe23f3q03hGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5BEbDZTCCXmz_Jg0PUb2YgNpLYtireQTgmWrt-3OLa3eYg9UebkRAcvsLXTg50DG7jJwP9tWN5olhUv5a973czQIAAMFfzHv5kGaVxfwLb1ccq5bZ0L71HkBprQk4dkbMn49SmqIPIIJ8UBC6qMJrQCZ9Ugw_zPyiqRyHWxnkYH11ezOVivDMa_P5hyiTrTXykib2ozEgZgB9o4SVdb200NmAu0wx6QbvrFQn7TLeFHoIx7fMSbIKwNq72sP_582j1YQsEhWgeDIDJNTGmHgmNdMU_hywzD6owOn3-zp5urLoV779f98-vIhAdCM2SzFnyiSwY9TxDb14onppBYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3Z3whLl3XBgR_vFaU2P3S3jrQzbAbvr6mv-5mpxoDX3T5UrZsHY8FGqNlZyk6LQdUiXvcxUO_8jBv2futVek4uQmlApQSEKqWGKaZUwUB8TVIUc5l5Zo6iRCDID9cX0Ot0Em7Gukxa6ky8WMlZJL-5md4jd8rKdHHiecFmX1ZHcZWUgETwDcoOQvPYJ8kztOdmfhlFxhMDAX3xkbZgXTFzGul2XLV5rmIIJlZIxFIT_8lgIN5pZkDRvH-gEZh-LVt6hDB9awwE1OYh6TUNl4sSHTtCkwKEA89dCWPTro781EyEPaIZHe0zuDK_ITAFeY5kZ1IyLIBw0qYt6P0f9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcZOnIXI-gcg8ZYe9HallphG6xLx2g1FWj8HsrciQJ-MoUcW8Me9Td_kpqJwIvKXTrTCZ0xMJoHUK9Q2gOv6FSJQ2juEBLa4-Nl30_oBbv_1aBYK5zgrk1oHUGMr_Jv5AgDGCDiulTZCRjZBBN4FE4dumGtDjh4TD4O7qap9GEfK92Me-sGCuJdJa9YmaDXV7PCF4D2mjUUpFrMc6uMzAmTI6XUeCb5TBXJ4_AtQozqfV4rfIE2gmlcrYWPWP0fZcGSPPO2qOSb10rVqFEwp9sgXeMRe8-T2Oil5S85JHyRfCPzEB87F2XfnfSNMBnT_dbPsyoVlg5TD9CO_Y0GSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De90GfLlEj2IxGCPAXk9WhnrZZxoEbjFgTEYv5lVxI7AlLyaBH9avmBNlSA4X4UQETLbbv4YNP6Yjwhu7VFd-KrYqcwXmAMYJ652uQxa-b6VlPVeQjRvCs1GicmjYj31PvfMAgCuMDhLKfmsVrhewKAUsRw9w3yWZTIx4WH9p35FeYLz0NY6znRoKZ6uC5sxocw0EI2r0zIf32Xm788AAdUsvoLTzW8Qb9BrrMMqhAbrDQdQ_qIhGy23XPcdK7R2iNTwfz4buWRoy3Jbt3n_GOTc4aaD-njJp3lrzoth7RUtBsCyu3HeCIjn-3qag9TzBD5nEMhS-1ejfIBDAwSKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4MdPZfv0SAXnXaYUOq9Dnoha1pagwJZSP8LJUSzm2OqlKYWsYkS9DvSJR-kOt6ia2BnhCAXw5_al5610A2W9HBkN9p37SXw2sp4zNxZsxyj-qjbHMGKxgxIdrSNS4zLJewH_SI1MdVfREio97mLqywmOd4SmtrUliQFvg70ZFAirX9ikQAix78wGO2er-_EROku3BlBIwmkKLSKfCYlmbnNJnRzhRhd0ZMVrIPLPsspglRcoZfBpBZTlp6cXgQXNkReb2ZyOnccpg-opsade6AxKskoLysjhFzUOT8I3tIgyjgnhgwWW79TVB0GU4k-jS4Yoh7putaiBuzrX-ONGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlrqxgledqgGKl0_ny5BuF5QsT7A98EZrO1R_pYL5PZH_tdPhu8HrVCivZAZtdcLQtHOjdR_T391BPON51HDqj5TFCXrNsAeQUu4gibuLZhauwWtV8VWV6t7LEtcdSpHxrfqivtf3fTv0HgTpZTM7DAKBFnIZnGmuXaEpAU6iOhq3mkPwTlY77BwD-7yAJFD-clCLA4fexKK3ZSZagMOFoHNdkgNygCImzWgP1hfPxGFG2VeBltszq60hmEHrAgmP4nC9yDCfVvadigv_iTyfN9oKLLmNuOvM9smmHYeUShjlIpVPsRK-ptHCwiEUqumQIEc3wxB38OISLttDEuVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBb6B9IPTpch30WgoBCOzQoUhkSm7QVnAoTmWdFr5zsX-iYZEgt4tEot3YODkadauv6PJUgFpFa9fykCplJ-j2WBoSrnItgK9SGmySGrvuk980D5qwXhrUO8ocNTid07jX8ICMQJJawcTIPpch2nnJHLe7rSxCm0mC2gJ83KaXwJ0gQkXfQrnLOi52mdUlXSJ5RLiQXxEt4qGbPuWH1lgD9af6jrGzUY8agmROtMF_8irSZFZe-Bignr9OyEGB3gbhwf_IQDTJl8B0pEqUVBjg7DWoCjobpkjJJ4aPKWdy5H5Un8Xfp6oo3JUnTRyYON6-aEKnjku4wLRw84iQ6oYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUa4l_udm8Q5CL1I5CoteaXk4yfQVems2ZVoWfjn3pl5aStypmQUDVlANKTiK1MMK6ulaXtnkZ1vf3GnpZk8x9-RlIt1Dc2G3k6G67fKH5YKN77vYtjEl6TOgTVM6bTUjGvT6LSr3d8rG6qC4nEojEmetkkqhFgSDe7zYh7CvLfhgQWGCQqq0LxjQGHGTKln90SH8m7Dmk6VWgRiNzppAZSl4z28sqJJ_zB1lhj4bYLC4pvmlH0s74oA5vB-VPRN-kBqosj-SnMAVeGPf3W0A5FT4O_aZsEKgFDyaXfXwZt96CzjyFDKrauZydbioMCI6KAwy1kYR31dyCsrZi3Pnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa0Di64FWeUftPQYIP10Dhl6go4PwFftWFFWXPRKlXBYY2iEvbArarJZ_iOvzaYFSIYzN8QTT6yuMMwlxKWJNYswsBVvBoexrTD3xlKVbLBDyBTOO0hRwQoQF9cTeC-1ZdSMLaF-uUmfcQScMiNDbEmMJZ0IJs5OK88KtW8Q9-cLKW0LpSbdAyFo3yKJoSfLNEWHk4sohN1pLO_cmhh1HsbnVv7ZnVJ4B4VviCfFSqq_JQEgmnJP5UsPSiz9qKyQTPl1bSBjKDQrs1YKVL_0cDuAhtszwy11ve3soRRCDVSgOc6eF_NkxH5uC1tGEJb4SSG2jQEt9nbVV3WkQNKtfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnF8YsBeXPp6qyG2lpaPk4AGPYtnOiJcWCR-KMAOrtTj74-MtQ9_RkiEZuW86soZoWxbJRtKmJNWgHLZ67edOvs7V5-_qFdUF6mxlhCqgBYmlRyssMv0vahp51k8Hv5P6Y9N4ylcxrrBf262OJtSA2tZdJeZ_5HwnNj7diyUxOfu7b0CSQjQEjthClO1Xfh4XPphNvX2HIQ6BZLdjB8d9z1gC-bOMZIQUKCE-8_TkXF7sFJ9Ze0UdpaPYdm9N2REIVr4MLB_0wqN82f_8cGG0VsOFeCvosj2EbImPJkqXHEpdompv3PsBtqUSkQaPsNiHFG0180cEJ-WHVzDClXrEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwvxzbvGTJeam2MtyAZmyOZVQJ0agzAKhFkskzH9InVxKtG3SFQLpRGWzDMxVyD5-mnEAXb4DB6Po0M3H5ZpMt5UMe6zZl2K0cqigV4fxEeA5kc0rl3HAhSpMLikyrh_hMt5nB2u5t9OaaxS1HkJG_XsTs-h0aSwT5QLUUgkshVqzWSAqb01cxvxhjjHwtxxk05J-5jSkvY0piFzTj08U5LQRkA2wxHdiij_A3U-2Q98GQnVgX_r69fnMvIxfsalEe_XBy2Rr6a8pNF3X6qhIdDPbCIAfhQQmhTrXu6s8fCBpOjUBpzDaTg8cc2U4emMslutNvuB8S6NOmnXNjmAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-mx3zX4uMIa2Oslqo83ZVh21dIbYME2-12EPLtTm7LERDxfqbsJXF3OMGdkjjZy5WbJWSlsqcydSwzWUJUXVFGD6I5RiUeK8wvfp65_LRLap-3paCaw6mBRzccs_Gv8ntK4jw-O4fK_pBgLDMq5R5bbW56xvdXPQwwuXNp7RSaCKNnPHKieAA5sJ7aB40BJw54720zmbYTzlQMD4ELjtE3P99ftW6B3Mbeaf2HZEsNXOXQ5c641KwnVHePf7pXvGPX8EU7VvZi-9ytUjQZqDzXbLpHOf_8UXkr6ksbWoNBgLQEykRa3vGdFiIi_iQeEo8rcqtGzyVacrAsX5rsLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ9elYh5P9tyrp62nzsBLDv-KnMFmV-IxHFhnZKBWnnB70RA-zG7IdO3tzOQxXE8H7AojoCl3tvWeeN3N9giWnzPv9GYjP8AjX4kTtwZscaix3OTTA5_-zY9AHWLF6owdnJk-O4DKfL_f9F-SMgJi7ZI8btam_H-eJwGfirZTc_xOSsXcwTLtYSJRzDkS3BIdbkeVe2A_5uoWSq4FWmWOvMuYEmTocNyAb7to192TnPTHSFkkVFkxyhQfbKN6aiWQ3HmVQLVNTnldkh_6JpWR4ooj52AEFv8Y21LvQA2L6M_pcpp6bb5ixbo-XrsJFssl140tPoHWNdpaeGsC10sEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF8BEAIGuAu039JlLavbIB1py5C9tQbqcDGltEMsRZQHg00otM8GvyXWA0fjye9TrZujtH1K0fSWuHfBIrMtJKpILIqqCQ2G9pUIdTAU4JQruotIgqPjI9B0ROMvyYCvn6FM1ANYkD_T_PIzJ27vWNXifTWpkUsDkNsd9VofJroHy6KZw1zKlZXSka3QPkfHQBBzUjddKL_L4Y_OkBuuv89frHbnSzdA8s6c9nQjZQo8jyaJiNYzAzIL-vt4J3ZVs_ir09ji1Q0haTcarmQQhB1r2bM04tfjzaZQOP0Mhw5nzXXw8mv6P73uSdarB6ZGEJazo9fbYz6S4WBapSsgyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t--VKKAEMxsgwq3Ntp6cDguXGQU-P9kI27hgWcP4Q5JRx42rEkecgRnNY7hnOswWcoDDj5oJZiifrmMPtA-D2aNn4uW4lIRa4BXKIgNeRjXnOzr19nWjjYh8nNZ9ynztF2bDoCEjy4ZSLHllC5vOD5EqucmziT-zYHJGSarw8sRFykqYm5J2Wtj4MaDGqXG0vxjj15Zo5MQD4idI7s3Rt4xdBlFtSa_2Zfbl6IkN6qm_VxDmszHYNg7bil4gezSeh0I6Tb8rQ_SzmLnBo5cCxo8zNt-f2XskOveh3c3lBCGcAlwKe5GQznFp8x5DcOAZ-MABNLaoUD6dldl60oJQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvYS1K2mRdxZhhjkrEJfyudP6MXR-Fl0LnJ10MJRTtdfGzqY9Ew6jWaU6LKbgd_5z8covX8GtJHo1-IV62iNqlRX_QoBXxp8_IDqDCzT45j0Z5-jawv_olJlR24VqdLGOTGq4N_6Kt78FdsTtrelHg1Uh8s_wL3cSg_P51EuFDrccmlhE17RO4pHsvKjMpzgWw4CFTqfwIFzNmKnB2LOt8hDTy69t5dS24M2MgSBo8733JecBx4kBySktEP3xi0jkV73zh9dNV_4LFIvi3hELOV6UuA73OzczsNUbCCA-ZJxXRhYlU3-lY2D-yrE0Aj5D0dvoCb8UJbhlni-OFzC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgTE_woPiRbbbd5bfWjFS8cx4yghXnUY2FOmWfKIDO5vmi1ru7DXz9i3D-LriZ4QdKgClvxFTyitFe0t-_tnQ2-LoMpZs-2Zdq_y2nlUEfI44ksLOERD3Ws53C_P7WMQyD2oHZurQfn0iuvYlzi0tIIIltgTa23DFgPLUXBIOvlUrefD9iomRe_w70djgHQQhfuusE52ZKlxZxo4g0yXNcBOtBY_6tumFP8-1cC8ksTF4IHGPD7C2BjBG4Um6EFcXbxis2AuZ71_4YAgB-yprYgfsa4wsaxtpa8ui-O4TS-rREDxK9aX4VMSGg5TN6nwQ7rKSsJCLtgy87lHuvNSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p72maMbDoTVz-KJsM1VUzkDZckxr3yFlFAiFC4M29_dZUb4wrjE60meZ-QAGPpfSJvA0UnqnYPOWSxRT_AdEpK5fEHmtQ7ECC7ArEK50udaV6oV0VW_TS6MKP_9Emif3oCMUe52IKNXoKd14v52RvaUI9X4Pu2zjq1QM6SsXfRcfuk4934GeEt5CgA9AxwB5xXYiun3dalWJDRbt1rRIvGDcNP09PlT2Ge9JSbAHR8zCQ3WL4W0eo5OutOpBp_slXDuT6fvOneAy8JyYZnpXBdDqwZhqowABNkTDGnPwXiSvxuVv0WfO9oqP1xqsMUaPoU-La8vmoVMUAvX5WBKTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0zCArJ6rMGDdyKmLMvz1wvpQ9pwffjC1GMetDBKzakOEfW0X2tdSmTviMJkzvgoq2BgRtC7ucZosDGmzUNOGAAJAXKqgUCLd0XOPEw3k_Fqv4Ke4bmwhxVwefMe32oGhVxpo6Md0ZkBESAN-FznEcT2dWZ8IK402HWY592b6KstSk4CgMHZCYP7ntm0CUG5AxJ8SesEFmHm5FhlN1hdlpWHMT8qf324QZqxZj9bta9Bv0gChjiNUarFZ-8E-3vJOqsjnXyhk85KtcoRjwRytPzip-PRE-VG5a4diVBGQw6AitQb2dMJfgk7hDX3IY6jHFcjduM7vhODTOn_CdOcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=kXNzuQNItFpDZl8VYBj-oa5LBDYURy3WcSxDHdLGnlWdoavaZIe2MSiVMo55N_QiGTXTJBp4rEIrapLtNYGnvmGrGMYh8CrbX5a2hVnUyVA29EjlQ7bMmXZ2ZzD-ME9bGXG1zE1PGTzFrht4aHhRkTMJSOhIn15GKSqEoi8jRgtm1I5W1ION6E07BKjeemvCKNsvSkEHI9jt5YF6OnpBQzO8U4Fi_7srRJ1vFyw5HJcthp3ALzR8Hg5AdlS9gErhsUxnUL9qOM0d-mFt95UO8z6yQWY86h06NeMkJvtUKtcA81ME4r9p7b3GKDJZW3AK8P4KtJ6VPit4LIBRzhiIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=kXNzuQNItFpDZl8VYBj-oa5LBDYURy3WcSxDHdLGnlWdoavaZIe2MSiVMo55N_QiGTXTJBp4rEIrapLtNYGnvmGrGMYh8CrbX5a2hVnUyVA29EjlQ7bMmXZ2ZzD-ME9bGXG1zE1PGTzFrht4aHhRkTMJSOhIn15GKSqEoi8jRgtm1I5W1ION6E07BKjeemvCKNsvSkEHI9jt5YF6OnpBQzO8U4Fi_7srRJ1vFyw5HJcthp3ALzR8Hg5AdlS9gErhsUxnUL9qOM0d-mFt95UO8z6yQWY86h06NeMkJvtUKtcA81ME4r9p7b3GKDJZW3AK8P4KtJ6VPit4LIBRzhiIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R40ia_7SBTJrqGhLavVRAMQ2MLin1Z8CW5fNh4ckQgXdBmsH0FNLaBbdsD28SChPJINUVkuAJdXMsDJx_3h8CfuL5IDuqgJwLvZ2wJkNjvJWNQCD1Ycb54Ze111Q5BzyIkatEtR_C_nEfTj9e6rUzlpWeLK6hjBc7oigVgPeBXxEEHv6fhgXlKKm_MeVDk71ALNWFy1iNKSnrO_tV_wJ-KAPJK18pARk-VChSxtY-4VW7VIhrP3ePUTMMlautYs_Gi84VqFHc3r2YVLN13_J9tx2SmAr2kIfZwzly4mhwmHcuJgSSPaOhxGLWvkiw73L5BUl2jqjdTBZe0CrC6HGqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=KZrc8TT1EpA-TWRBGEIjVGEWQYww6TINUGIv166SVttVvK-_hiT6RvwBcBF52T9MCaru75AimHr37v8BxR06F4IGS0RFypi-GQPOulwJeHHB8e8JGjBBXL77Rjbcl_38MN16QRRXOn5gOHDgS5iOeNfpkaLaRd7Fgr4ycQM0Fl3egz7V22B6jNEYuOdYx5rtA4kYmoJwYITUankKSLc1JoKDVFNx1FjMl5pVtFdqUiKMYVLaXzbKXAr_vnW0C8kuEFnMGQP711nhNtAPtZKrsKUKVPo-D9qxopostE4H5_oRjBcMrLgv7QN4_XAGaZ_dvrALuXiV9HtoO3eG6yfvcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=KZrc8TT1EpA-TWRBGEIjVGEWQYww6TINUGIv166SVttVvK-_hiT6RvwBcBF52T9MCaru75AimHr37v8BxR06F4IGS0RFypi-GQPOulwJeHHB8e8JGjBBXL77Rjbcl_38MN16QRRXOn5gOHDgS5iOeNfpkaLaRd7Fgr4ycQM0Fl3egz7V22B6jNEYuOdYx5rtA4kYmoJwYITUankKSLc1JoKDVFNx1FjMl5pVtFdqUiKMYVLaXzbKXAr_vnW0C8kuEFnMGQP711nhNtAPtZKrsKUKVPo-D9qxopostE4H5_oRjBcMrLgv7QN4_XAGaZ_dvrALuXiV9HtoO3eG6yfvcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss0uAiUOPhLo0WxJEE0Ik9-xruLkkPjlgROySzTMeOVBzpMfvaDbmlZ6Y3OO4UTY9M1H4CdnbsEE5Ir7lswaXEzyXUDbUi413Mj3QdtytzXjvL30TFOgP0WaXVunEEwc6lOAaFFz46SEbLqUA-PHakuuKIyhrd6LpAXinYUXUgjsEu-4ajOorml2UjCHBYB2kkZOBMufcYAoDm3z4gFCZLbZ0Mx6jeUJ4uF5CRux-DOjocifr3c4CYySJf7oA_LEWhFrDu6GqpzlEpYmkSyAWumSPGoC-Z4yhjxAtLojO1v9WQr42qAueRIWeBu21PF01uX-GR9N7UXTC-WsNkPJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=odU6HeSO3Bxum33dbcNuu-THQ4kgawgj47-ESQNQND6rHkCocMcF193_7j5hBIxejOyih1MtwOH6OG5oT7udu6fudAEunMntSOuZIjmkcWDdDLxL4unHpEnRYch6pTIM8aY57GD95dPIyF5Xn9xrfs8rcFHdYD3GUQitDAbkipUqC9fSPBVOGjdcLfRIeXL_zOUt27tUN9sbNhoUPOrnNCoNTDMwfgJTYnWjak77WHVc8J52kwYjNGZdTBPDzD11x01j0N5jXcgf7MWU7DTql35YA0JJMql5D2eEXe0qDehFbqDtCXI_EJSa5-dR0vrNhPNM9cDPBw33rGi2VaQyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=odU6HeSO3Bxum33dbcNuu-THQ4kgawgj47-ESQNQND6rHkCocMcF193_7j5hBIxejOyih1MtwOH6OG5oT7udu6fudAEunMntSOuZIjmkcWDdDLxL4unHpEnRYch6pTIM8aY57GD95dPIyF5Xn9xrfs8rcFHdYD3GUQitDAbkipUqC9fSPBVOGjdcLfRIeXL_zOUt27tUN9sbNhoUPOrnNCoNTDMwfgJTYnWjak77WHVc8J52kwYjNGZdTBPDzD11x01j0N5jXcgf7MWU7DTql35YA0JJMql5D2eEXe0qDehFbqDtCXI_EJSa5-dR0vrNhPNM9cDPBw33rGi2VaQyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojFr_nM2NcJh9PafBKKflN2ADNKfKV-g8HujgmK10EMPB7ztm6wjeTDYbCmL4NULKNP4pDM_us3ot6W1_GoHxB9Y6Kf5ZXDC_hVwTtVYZDw7st4pdRp2mbW8H73wWM7FJ1RhfMvHMJ0PHrYEvjr9lwr8haOKTguiTH9XIoNsmwicjrD7ScxtX9u44bmHq2ijaj9E1AutX1vLN7bWhnBmY5lr_G-Pk6HnRPt-2R_t8xqcHcwBILbP9p-oAeut9jqd-vPwEWJRkkH_qLgseZ0pT5N90oEGXpOBJ6JYhnbSnnb9cEGhs6tTzs6oH8BA-F5D5jv-UPwFF3EE0iomdsXBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X94WpKb8jC-5SGNu7QQaiDTXRQn2cpq9sdL3Eg3rwpcagHvK-QFEYSiDxrNSU_hvJ8_GrkNlC8BIs5SVMo5TblVwEqWlKco9E_w3MJJ5QrcMFqMRJl1Taf4jzz-6QfS_j6E5XZbEP_bQdicKJHjar3YciO4E9RVekme1Pgn3KcyBiIVbuolb4nloYVpjpfV7jyyCMK0B8vkAtuoWdFWEEc3b9SybBpsu9uS19_FD1Bne_ffZqZ2X1J7sIZQFMgRtswt_SOeIAusIafGW06EtKTFPISi9wccCcOjk7mvI7hOVXQA2LXdFV56URzJ_sT4VR41e5V_ol3E4WBtoUYeSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGukzPA-RvV76vnLhgVT844sBX065DqdQdz3nZzrEnpsgEyaYs2yEni4pUpFrShNRBao98r4sC8RyqtvecaabjuK5a8T3N_rs3T8ctJDRhxYnTMXSucYw34VjnITLHyVY1_Oxg0tWPelZ3R5Z-gUK-jadN8tDCTdWmHI0wt_FdozZVgq8aUNXqaxYbHYcIfQazf2rQjGWCEGXc6ZV5HPsIHtAV1nPxNDtUwjdARh2TAG7WKWY6yocG5CTDNBGurtUv94IXGipdIfHEZCP5yApS6NGuUBhGHvQ1VCD7VTdFHsBdZbuWDJhNqrGz3TOXZxRvTpzH_xP7y8MVsEMDBKIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPJaiwlLxR2JY01iuIVwdfZjVlBN0ApRxMRJIW4HZCYhRnalip2wwZ2X_PGLHkoP7gfAnS2FgcgBy8XEYWTOfNDDBfII19JIO9p8AumrNS-aWT-5_c28DV65XhR3qKAEh5sChuTz5xT0XnnrqxQHKsDVE5n-HCCf3AxNRtF_WTgrM3YTadOpeIJXTZHhW0BcrUAHAfz9T2MuJHGOMFMd94ZgcYYw7gbkaM4gmZZlqcoVhW_3G7olz9TX0szx8BUdkuVK3L7h2tLcAYXgf8SvLiBo_fbT_x1kd0_S8hyYHXceWoEPBA4Wf2g-fcwPyVCWUep1DhfZSJkj6itwEiDq6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-QNBhuZoAE-tcqI2RT-Ue8bNj-k-uHVZlZSvHfGzPnP9x2p8REYr5YW9xWHdUAhCx-7GC5LzdZmoI7B2DJA8FkXmJIT33JHHBZKQacqTqR3WBtTITuRKOj6nlFI7OP-ug4q1rSsL6Q_RsKDOHNNM1h0x-sjPbMgpJcI0BKfTV21XCSqH3fUTAImuEkuK_T-8tMmtfu8nI9i2W_kxpyoqbm_K29yG1EuLR6GlUFzthT-KUkz8DHv_6o0GRaASShX1rxBwyBk-loKjaMNUSRD2cM7GnyuqbMieRqgOH5Md4AYn07hwfoagRP2SzZKWd2N-MxRJDFhh9oPmw5VRry8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0DFY6zyQRqhR2E92ch3cPc-k6nZt3Nsz1J0ICEKZ6MXz1qZJadfLPFG5Dr6wFrILur8AmC7PwUhPUTivtZ60b-5SM9lQL0N1CiPkypKdvSgvsQrQ3wZjkRwKhkt8pzRjyMnGxsw3r5wWMPYxx47t7Eb9L1-gPi0rvquaFhEwZP9egEAQ_qw0fFcrIpJut32UjW1nVSe5pZtmO6oP-dy3oB8wHBMqVVJKmdinqUPMCP15b9Kyp3ZDSiRA_woXVGC80BSJRH77rWMDV04pnS2I9TYK4XUd3UZaHPVzI4VDR6PE6qlU3lp13KYCTL74sWexKuGzKgHxNOJY4vo0pGFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-AainCvF6FFl7QHEf4fUs4rsSIyefzg0D-AXMPX17MggunoCDQa_9YXgZSO7mF4d2GggM4TshtnZvMAEIxsAm1j3DOQTjNoSOwGKoei9g5cDHnAFQy-vhuMbCNVozGHCzRa5eb93-H8QPrm3M8jpgqqF_dJJiXV1XfyinU-29-iZAgpWprAX2bg5BUoMnbXvumqoQSUGs_Bbz6WLURK_2uFUVH3ABW9WPBKkoXE9BFws36F9iva5NFiFDvSaZqmy8Lf-cIhweAXTumumN6WRWjepUQA_frJ5fUzjmLko9Ub1ZB9qK6QfOjRAOP7TJI90zmuyyFsYZ7C5W1YYpgz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uangLILvWzhV1lfXkMdJMC49PdL_njNoTK8G--wIXE14rI27ECaPpcITn8FZnAw8KRL_1B1RA_l3bexXXRau3uyA5TGGw-Z7gvVgD31AaFdK5Ns2TcfdC73ow9PrQyg-sBRikBmDVeZR3SzNOMGQq8vwuFAFYamhWs0NwIHLCWbfo8c4JKWS3Ibt1g182gbsVFNisBzRF00CPIAmKUIevX8O-Xk-cx4OPk8dxu0fQqApqWIMRVoYWtCNJJrNV-OI-XuQNjsA5Lhm5DiKSd_ivY2B9X9KkGfFywDGMcFmoYr_6LBnr2erPy15NaSK5LOOgz4jDck4lru_5VOp1HGitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMOh_sOnGEz2Ddl_FbitaRR9btYNeoZoouNssQm_B6EbuqaJATfM_Qs2V-wFyH2KCrIhXerk42U-r_Kjokxr_bCYY6piEjku38MT7ODEEFf5gbolfe2JrLAu4cAaHft4W36HjcYPz6uHxzOOurAEv9WnfWAvszicVkXVENgcZVrMZlVK-PsLscUKhNfQ0Nbolx3g0DsQys1wMZPdI4hz3uYyw_BJrFTUHuIbgEa4A7lC2_OlmfYpprskxpcYszKlS8V5hhw0Wr7nqx1OX6kkyacslhvicL6ygIDH_EUj7__u1SS73M9GEMSpFMFRYn6Jrpe2nA1EbCbtOmGzE625Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVjl2migQXTWVROS2YOSR6ZaCCAPOOyI9QC0LtUu094B8k-wC0IYFbpV1tkG7H5PrCIyf2dpBIo59HZ654X3Jy7iM_z1lsiniW4RK2ZEKEfClOdEGICavhrC2nuNFKAe9609_mbjGvX3WYj821blL_hNs5Ii8YOTKTPd4VeXMBd2ZXmYq6u9rp6YLn-3sT5zVMHHDTkIvfGH9ol6D3BdEZRV5X0yVjcRhYRl0ZOwPsb8wKnX2GRv2cjTPQ3a7eKXbI2fHKNpMKWk5c1V-emDCXYF8HKkdQuJtmJnmSC6-2D8tHzvWYCQXTZBRvHLamJ_hfSt4kIslaBprLKUQsfzNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv9bfDNDhxUEsmy-3W3Hf4MO8qI5W1obBL9Yu5ZY_sRb5D6yx1VdLKKcZ16vwjBjJ-gKTwzgXJcqT8juuglAEU2qezm365GAiWVskZhAvk-FwPIVlC2xSPh9E3tKxmOdUZgs0TjUf2RJETi0HbjdSuco-tYmYgznFeAby0B8ljGWYNf23OGP7lnoHSjFTwiWXXLSv5_X4ZilZrv_7ctqRCPF29L2NRRAyeDhHSh2iogEct0-umHEtqB2SrxLR7BU3BQne_0k5lN92cbnGR7qGXmZkc5xn8iX2EBENlIP8AsjhGfFPnXZcCOESRB4gCVC1ViJO-b_EFrD6S3jZBIM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
