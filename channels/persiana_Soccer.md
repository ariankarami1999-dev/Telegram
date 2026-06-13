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
<img src="https://cdn4.telesco.pe/file/ssDHd6s_djXWaajl1LAI4_MlYBwQRQj0VEKv7ISYDGdPUG6qgk9Lgai81jzGsn_Pb1R9Y5V1l9dcjbxKBOVkHd5XNfBA2vDtGD-hlYylTk42MVg529VS-JocyhaLU9j_0EHoIrYF1FIwJwuZC0JEKAeKI6G6UZ0zHGsK5532HrenFI8lvDgjR1sX8nYuRjvRjQU7BnpP5YY6uzNFcqY0oldsiJm1uSQp2X4ZGnCp3-nk7EVeHpRMkleqKvbr6p2S1xFTthq0X7pUeBQmNy5fnzlUpn2Ez5_ak_9SBPQLAndK0AcDOVYRD1p9XpIjLtwcvP-Yaz2uITSF4YrFftZlYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 247K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8lNXny4QshOp8GKeNBGbJlvZlE0jLWTr4iyUA9w-6Z3M7FGNqQ-r26s7qc2L4YncWvg2r8OceKnm-2ypEQGk8LE0TPjYVwJsyn-dTYFmddT9N-ZlU5IqUUBT0H0ZS0t9PUrwt1_M7GQcqbA9cZutmSo__3J5G1QL03g_BivH5xh9a_s_soUS5GV-sLE7XGj2HkRWX46tpkNSkjN5g4NU0X3IAMtCFPyRTSm0M5JDH8oiuFV7XQ2L2qpkDSHSYpwoWU0K9ZAn5mkvcfwtVdkA6N1Ka8T7QOuX2rvWCXV33ABMO3cFWRaSUTYP2F7QhkM2_KvQwJD9a2ABYLJhe-5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jannjw0ZsIoHL3O4M9Oujoka8bgKhGgJI_MdRP87zOW7_FLbnu3TtEaKKOozPmJXvM5aNfRri0nyOMM5I2zlb3g_4i1LZekulUyFX-gThXwUEYbUPNUDcqR-xcminqcrZqTQ9duzM8JUMZdwwhZMC2rwIJvtlRx_5xs74BhDljG-NKg0ioVPrdhPLjnlJ04WJ7jvqaOMDkru8mVYu5873x-NXNLRrpQfZ27ukZnX7HgcOleRhEZcU5Lm5sBYLfkG0HUAcQvGQQh_HTtbUlex9kzGKVg2FXv8E-a2ZLcTf-pt-M6SKf13fIrDWVSR3BL-fmbIlulLeyzrXTO5bux3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nH6stHv_o0F_oSMyYd4rKDDBKEUZLYOQjnSwWBrVAXYgYMOYD0YRhJeBDA1QLuWpibtN25d9StZ_029zlJD-q4-DyM6TzQj86P6PtTdvR4A_apnfRS9H4vUdpwpt8JD52WGMOizhdbv2kAZA82XgCBcjFb5LASWBBig_tActPbds-Jrc6IN61roKIj-NDGBkPqOVEO8Dza_D2OGKyG-RyVs84yv-ijbhJi3CsLuGLoxuYUjFKNUCafCU-LKCGEA4tggfgmlIVTmPhxmNG2hMxF4B4TP7LHYa8D0DgLQWh9uii9zPHm29x0pPdU25zfm9WPG_bycuJ4U4-67nLYNtPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0LGHdFbG1iAWhew1nGr2ah7Tg0GpN_NLyd8EmdYO8m1xmg2jqfFVTdk3Y0Cj1nmbqzoa6s6jdFfBaxJi7TDnfujkcrhJtiG75a-foZchIg33bsUyU5yIo2rEXNlpLTFCURbdGjxdAJMot9hUGPY6kMts4X5l5ee2efnrO8LN6auO8ND57gX9GSX--lxW69kcqSKEbVu0tBiC_asZUU9orEh-b-76laIhNd80bN4cAgByguinWGJ_ZAX9XvX-dDGEYVa6msCrJTKgR7KT_99hFGFn2D5wrF9DLR33vOStYL6qoDmBBLJ8F6p-VX202OfsLVcRffr2w7PkG6uIhVbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf_zA0UakYS1XNQROrnRk-MSjyTYAieK86s6FV-VqNndXh30BIoXYowzM5aQPLrG6hm4tI-Z7v-U6vEBrFM7uajFJg3vlU-tpxrFbNB4ltZ7R6rvBhZ7gjxtc_fvqacmtkO3SsZaPbhFOq9G9BHGHGyX3jrBaEi5WO-Epu8yqhicUzMTba4DEJ8aCcrgGm0nizT7hfqvbaHat4prC9ifToDqKtZQtckW1KbBXhPKF7F1EASUUEZeeMGWoncdUoGXFuEZ8vneUVkGvFXj48Kd-_bmArfWozmeyRkiJI18P76Tjl00AUBIRTogHexy6Oi9iTMrynI1B_Gf8EjPf6hr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzthCDx6slHgdv6Wh6hkCZqJCKvyD-Ixfwrb1S4C3ANODnr2G5j_50VhiCxek_MUSfZJaQSOiSNKF_FQmyB8esRTlluAOgp2TIEjh_rrIwGPqd4IW9q0-b6dN0cJ6PBXpRakpXVopWcXLESnUr3cqHSGKNWdL1sgYo50CqjlchH2Ti2Fu0c9-5sm9fcCRkeuyn-xxb7h8F3-8iWgWxtpz53yOtXSaReAVdfzVHPyLpZBdVVKjWOkVCRLTzwCiBSIz0j_ENl8LJXAV191UbBNkLVoc_AcDuTfh0IptkCg93gAKr6uyIZTRp-jIWJBHNveAheHJyqiX_E6QpWniM4UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWmGbjFCv08HXly7ON7RCpRnWbockkMxkvKoV7zwGtdYUb-g6LixBbqJi4dZ9LznoqjQnqqsvoIOk2-U5uKMhW0btIqvKnD48ExJbv8jmZw3dgBz68zszlko8dLpz6tChtWS41QR1nJcIG3zHMYyZDTK9DIUzVLo09mjJHPe6YmdCDT-aeDTp-4Y22llxpgBs9FHQ0yTgf6sRZSHH4NqsCitbaP9J0m2vOyPpaqPEqxPQOuHw5O4UO6WjamIha0RrKVjSZ3sth6cUZy_95RWWmB5mKUkudFcrtKAIN3LQAq-TPOvHzCI7etjYiuoQDJ9IURqyNNEkOv2sa7eMqrovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K621DDLouvopBxfi61jgtqZxd6w6VmddHHMySdVtLW539ZR1xxW8n_TyUd-Y7AjOFOh4aJ83vC84QGJXlVcMmatmJRTk2VHUXUbYcfeWXotuc-w2_A1Hq1nZuZHP9V1NEC-FjdcToPLJsN7ujf_uzYrq8nU86Y1nimXink8rxeoH9mfLAmAfl67Ej3y1WXY4ahf32l4DoRvUvre4T7yidItM0wFjLjWav-d2YjuicosKOyguox-GQCw3uCa8lmQsnBFH8V7tszd_9rlmO_Y8OUmOyoWFzp4imjrNNIQIKZxxIqBrQJo5rXafwNZunfAWdO5-sixjNFrRjbsrtACAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwTyjC2R9Yl3HPxzD0e5MS2pAvU6zJKeGp0F6iQphnDLQeYAAcZdWzBHZEmjJ_OHBeyMI8HpXGGSeeywV1-kkcUZM7dd6VRx_YnP-Zqu7TGyh_-WjiHo7KfOqYwtnT2yg8jsJ7flZ5m0XAcCFeFfzbGXTZZphbfqIoj_VoFlXK7sX-8HCS08-v_W6H9e38JLCubElwKE_FK1B8qDYh-7Plvl3Z2O9lNMZ-dzogDt_l7EjQIZnoe5VaLWtXCo3wmP-VQseTFIkU20R7mYucw_V2zttPZMgrIyKRYFNQbV_ftdw9ERkUpHd2WQckn2H64_ELvOUahXOMoZeEpr0MCDkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1VkY708ayw_NLWrsn_yCeJoVO2LzZDbHLoUFzzYuNIEcaVlbOvPZ2Sl9Ra7H9JmQ6g9Dvn89XI3cwSWHQq2OMQ9fROpKlX1WL_sWNZj_o1K1uCKxBDJ8cx2hxDJOlT9siRLWquvHaIDCJXgoZQSz3Cp50f6hmTvwE_jIiwRNGKQVP9Yb5L9dJyXI_k-4wqiPP9IpJkTc4vpeICQnD1ceU4haABJ8lJNqQ1aaFt9gcF7TnpVrJ4vV0orfVEuOHEdb0Uog2oAHnUxP-d6aUIC6QdS159mU4zdx7VwM0v7W2SdHJxVXsVJnOw8jgDRu3TXI-9ba4nBiuc_SjHvM5AgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGO-m4Z-bBzSgbbIOL2wUynaBFFYDQsdrqlWqkQDrHePL6hoHh5NATqbuYy1J6yS06NaVou0SZlhLvNyxIyqbYIim0QJ0v7BdgaV0kWNHFnt6J78NB_UCVZBw-iqsDGdOCNtdn5OGRrLt-m5rK1QvUrCrHe7GGGwPyvQQ8OBPItLJ34ujFrFD8ZezGw1URKfu7yJ2GEqqDkOR1hJSEb5h39Z7dY2Lb-zU9jVn28uyPB8JtzyuuEG90LnzZBw5eb-uYf6JeMBVXsoLlqGis1rr095tH4rOuTsASAMtpxgbgcC_G0sY694ZwjqtTdXBRCXv_lKoyYnATGbFw27dajcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/23313" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPxmdVB2bYlpiMwcG9hbOKhfGzbRAfxQGRuoDRL4xp21NzJ8OLFpQgcXOJgLDuqUbuSoYYa-knt0DwL3Jyaq71hUpz0jLhtlHGI0iBYQzYTafqc7Zn0D9wVtAeaj8iy2EQgWYfaVwBYU9r3tcJ9Vwe26XqZ3z7FVDvk7dPJ44rKhO9WmUikqb4EdFaIEsrBWZOcKACtdo5vx-foSybEl7R5pM4x_T378_eldUxB9UY_2d6FcTOU2I0Uj-Ve9JD-qUExasN-pUL_3Zk8wOFfbZc7C8lERW_cLG88jPWsmkZ1McCrpYs5d5_jSlWDI_4h0HEW91sMpp49yyZxeptC-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=tVlX0RfYw5kbZjEEt8E989JwrUrT_bm4_zVCDmmpoNcxmF8u2PbVYbbasdgMRAzo2N_b-0I2x-2PoQRaQ_EiZ2lyWVxnLKOVGTgtSdw-sz5n-0yoJNT1Yxl0tU0LyjNrMalUxdC3-DeTe1Zx61gZ5HnYF76Rdo0WvQP3sr6RQOI_8WEnnEYA0B2a8vr62s_uVpST_9IYDdEOn4vJZV7q50wqcdSFw3gIJaCH43p11eSwvdnB2r0CBzoR6L0sK_sSDOiSi_9NywCUNy7uR9lEPOix5-hLl6YHaXbWhbNV9wBeoLZka5LZQvlrV-cMeL_x5RRu-S78a9aSCg9Zfth8q0eNtUkzOQ_25sUzgffN0fGA2T-Slp5sOg-xnKcAfORlOF7i8Z1syyGkzxv6trTJ1E4IXOkYcwFcK5_aUMVTOQ32EDHtD-U9k7tWplucsUQijrWBPh-ydUX-aWWL7shnLvKVr7iVa0ZVVJBtah2PSL3vvQNGH8MEPXC-p65GB9OWYurgLNqqdcmz_0R2pnjAqYhZ4vP0CHYEkYPsTr4dgnULYWPnaZ2iyikqrvzNhYUFbzXEZKDJFNLVJ9GnGDX2FcDSS7Wu_kKBhzzGFzWPyMXz4hdY75XeudZOYEvdITDGdEhVgqf40k2M-8IOLMG0jV-c7Un8aEom5y8I9zPAb2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=tVlX0RfYw5kbZjEEt8E989JwrUrT_bm4_zVCDmmpoNcxmF8u2PbVYbbasdgMRAzo2N_b-0I2x-2PoQRaQ_EiZ2lyWVxnLKOVGTgtSdw-sz5n-0yoJNT1Yxl0tU0LyjNrMalUxdC3-DeTe1Zx61gZ5HnYF76Rdo0WvQP3sr6RQOI_8WEnnEYA0B2a8vr62s_uVpST_9IYDdEOn4vJZV7q50wqcdSFw3gIJaCH43p11eSwvdnB2r0CBzoR6L0sK_sSDOiSi_9NywCUNy7uR9lEPOix5-hLl6YHaXbWhbNV9wBeoLZka5LZQvlrV-cMeL_x5RRu-S78a9aSCg9Zfth8q0eNtUkzOQ_25sUzgffN0fGA2T-Slp5sOg-xnKcAfORlOF7i8Z1syyGkzxv6trTJ1E4IXOkYcwFcK5_aUMVTOQ32EDHtD-U9k7tWplucsUQijrWBPh-ydUX-aWWL7shnLvKVr7iVa0ZVVJBtah2PSL3vvQNGH8MEPXC-p65GB9OWYurgLNqqdcmz_0R2pnjAqYhZ4vP0CHYEkYPsTr4dgnULYWPnaZ2iyikqrvzNhYUFbzXEZKDJFNLVJ9GnGDX2FcDSS7Wu_kKBhzzGFzWPyMXz4hdY75XeudZOYEvdITDGdEhVgqf40k2M-8IOLMG0jV-c7Un8aEom5y8I9zPAb2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1ab9p7dev3o5hUfXyKO2zjj7R2CxW_fYR_A1mexqQ_bx_i-LyeHj-GAHd22Huc1xfjaqqQ4S-o0hkqQqsv79AyjuB5KTSTVfZBDaCmEGuwYuT7HmfxKb9-p2WrmLDZQS8jC4ZO-hC6K8tuVk-TCsKDw6K2HMF-Pb8dHQwr-F_vcqd9qGhyDEwVr1fB8-wvHy_2uiZ4TCKASLgybIgkkU8AqjG5qxB1qbt0DBBZFKrCIwRtJ_MUelY7dWkLCYyGvSKf723l1yIdLVYhpziyHBwhTtWXaBho19o557t7QPzfsxiLz_oDQZjR9VzpZrFJxZ1BmqW5Gyhi7uvV6e2Jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4ZUdA9G9S95p6pmUTuCFYPZi9mJZmw0s0L-LS6rBYrhQYveC64Ez0fhw5c2LH_uZfVCeAlDkQH1bEMVfpZjzRe2co474uKlDM7CVj7hVXs7XtfAHIFFOxx4Q9JLlqymHOMm3nj-db1dsQD31XxwyEY5whxVDrn59m0nmw3csh0oC8mFbuDK4sg-wnAuE-rJORDQ8rBUUNGKVyBQ7wnuO5Xv9df-ra_J58kh_zzXwb1WwsQoYHXSzoV-7t1lYzvtX7y8Y3UW1PWqsuzIigAgktgLXWHvtYmg9dJzKjtT78vikXRUTDkVYB9BJ5upmcBctFv1Mizj8CZvcGmvZoi6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5kPEWe5Cs4SjDdxENl4TEpYoHxFv15_VPK8DSIxTDMqucvuKUitznbWwfzm88F9B7aeGmOaWWTihyBt8dOLrOx_l1nRga_IMIjt2pZimesOvnQ-17EiiScVrkzZPwt4EwDdoT6JxXewaOYn2iYF1BFwPoUMWiYYGZA-egjQsj65FLel6wEUwF5TQHM1xF4YOs5uC9t1eDQT3NhQ6O1Vdf8OfvdvTaT4lLxs-QqSqY-fDTGNMVSNQx5ssP4Biq8DsraPg2orPcRXwNLpucMz1cFV6Cj0IDXVos_jBzscOzxR8no8KqUNctqxNu6h3JbHjLdnn-r9QgGxT2OGqqVRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTBNkGYUgi3nqCMLTlnhHz8hfC4bo588kcemZe2PLHYe4guWEPh1k_rZny1tsasufFd93GbS7y6ZWjXfOWYM_9QlNl1A0D4x3aIj4LpDMtUpZh-ZQT9u8hIKx9BvhonAzb0lW8CjPdgVPnCNlOWxb_IXa5Ei344xtwtZ_6TRlvfkCfv1c-TVxIgfxHFVPbKtPYNydOtSwVhtnCSOJgJrE57pRTK3d1vtw9Ce4gnA8vqmwMMxAxScC6yB89gv6C4PFeeu_fhBMOgNCOlrfOLkb-SHyecKuILa5uAnRRQsNb-Du_A3DE1BJcIlrgAfbar8XBgTs1Am9J8uuNBU5Fbh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoqkCNRlTmke0NEEwLaUUxDxxTgQjBoAndRMOHLbtw9gSyPHJ85Kr1OQtS7Hd3N1NEaFKW8_-bUmFarT97yC5OofapapTHrqBsrpQgjn14dOMfGH1d2MMiNz6AJGos6tl3dWEfsHAQ3BzAKh0D--cc7mjxLOkByy8NT_zPIxiZy0x2Hu7kb-0z3BuGhYhIhyfRfprHNa68z4SaeDiHaCpVBq5kqV_L6c8o1ZQt1GltdVREHp8N_OSYU1RTwOGUJKX_JYjTuRo_5Dqk21HLscEQYy16prFnSowNWizFDKh3DpVy3O6rPrvPw5ouJB20qC6tf4x2Jxt6aFgzId17IW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrl-uNMaiSvWeI3Kw1yYR3SMVcTg_fIyOYBhh8aEf0zNiDf7nUgaWflNQ-WFmYfj9Fmw_gn_JI7TOWbrQr8W0qsK5YFfSQ0Byx4sMV4pE8PvYKH9RQfi1mBVW_x97V_o5YjB-hV9kibYFgjisWdB8MgSn75gr-aEKvA5d9Q4s_Cics3XNzGPgx1GplTFce76Yxh3_nC886Tcq5S4byrhf6svGIj40LcqEP8R8Am5vrCHdo2bxcH3vexFzY_xKMNaJqXoAZtyZ0Z0Wr1aXGTBhXi-ytcqrIR_EZ3e68uFAQde5U0QkKAYPekN0jCXJm69yRuhszQAZNfkqZNz21vsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVgxPAv5tVJkOhlZE468VOR4SF-SPMgT7vt_dR4OBouYqgKGgvsdLBX_Uotmp1EY9lvyQKnKQeggGdboDIzOUe4br8rZX6wuUPN3jZ-URMSSVjQwaOn8vBEDILLm3t8mm2qbc2Ce964atVYIKjE4Ca36zZ5yblot8IJdjRr3Vkw68jK5l-vM1JB3wxnYTku8E-nTKNu11Al_hpiYLiRQdbSf7kmv83pXPYuFNQwDg4qkMaQ43p4Td-uvteMOzFbCiPqE5n7aCzkc1fyVM5aMiyu4WBcumsQ9XfaBsio7rVaNto38nxTY9PatrX3ORfjkHlVQG-mBoB-Fj8tbiYbVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNqgMmXRqFL7pSIkWVgVsjtJR5pOCqjvEULw0R5NHO3A3de5n3frovK5_LWii17I4AFuU8sipxvqKvpM2hQoHA6ko-QjElr_Dm4VecUvtW4gzDV-ZPbsn6grw6ZmkQvduIZwSDw00J02alvByEswfzavBQ5gXXgGjLBnZH28sTZCbScHipxcT6EedrEe5SBfFc6fYW8E8UwKhUm_o0-T_7h6RWVkYF0dkov-21ukKMZ62BDliBoh_at-ghTS6ZpNTzGSr34DiAA-djPT8WFznUpjuPyaA22M9pcgZek_fxEJGMonpGSZHzhGR37F_QTzeaNQOBQ0XNKQzFmc-o_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmDY6d-v3lkO1D8uQAywztmSAMtRZpmQvmy8Mbvf21b_TmnJwmE3uqxKXeWPE0FP87k4SZfb7V8cOaGKxR620guTuckpFsrr-yp-QQiffYsvNrb9bOErk2z4lElAVN_XIlSTi387uqubGAFzCwKO4_kGcPgYT8sBSVWwvdv6mCVZgaQ0_CaoPbxLQq9S9eGAeMb_dZnLTgh4kvuXYQLaZThPpZ9aUtElofl31i5IypDWzeAwo-fdfrp4HVF9JLoim9kXKtLhAy9e3r6ABRxcWU9iOKgUsnGWO2Zgk4f8_54kTFm8rRyfWY6JjbzGAeLr6ExkAwmnlxtGTfL2O2qYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjA1qL0Ntk_uVzwY5W5vnE4tgNGfncDUxzG4HJNuab_cZxx_rouj0oYJRDC4DYjT5pqkeFWgkv9_H0d7azNtJ_9PJLtz7LGexHJ9Gypai0U8JcOzjVJyv8BoarrEWPrCZiZvX6cCL4ALTKzPiN1wsPzg-e664wcxSRDcKWvbYyJvbE0JJM0obX4Jc9aWKmX4UbqZrOEQShq4nUSeFHwifpA9owbxUUNYwDNmcnBPElTBAGffpORPUKIwVuaiDYjriDzhvYl3VnTsffSTqvf8_FYSsGN65eKhlpOOWZH4qs-rO5Ck2ttIMOTVW3aHzj99as98LlFdbzrPbxQHGrhg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz2aNl6B7zkEuGBQ2DcLVQy09Nt7AC-oDhgXoA-ASvnhAR2GBGt6xULDjNGmoPigv3qu0EP2afxSOaU4sdnIgJz-7_wqYGmaqdVbdVwKpFpAEnEx938SalljbP0RyJlTJdVdi-Nrs6gCfdV3U9MxVRX25hQY4H947_1U0TlAq5rQ5mTsSJixgsiNO_txstMC1VmePx0VqKadt8vvFGOPoh8g4rSELDx1LrWHRgAQjnPKu12qGRbYBxeR8CdyMGXvr7LwOWBKm-eAdAgUfTXfjx2cL_QLNtzmbW3QMIs9RZUG_qff_Ffk0mUZScA5kGgMeUxK2g2xY7XVw4OpPsFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf186UZeTroH159ws62VF4IzpN4yiqz1f7jgGdVgxBFC7QmsRUMw36yqfPko2keXaep3PleGExBTFYuGMvx-MAI_ESG2rVXDU6bG93EePfIyR_DszXqtmyy41garAKTJxUHx7gz7Ll1re4ZwVzshdb2f1-bcCst_STN5p27ExqNaZjgbzkA5dVnWLTnA-qJd4JaThjJgdpB7f7lvveBQ2r8iP5boaaR6wmNkk0fxJg_5juQW7XYIXxm--Bbmefh82N3413T4TCXSX-Q6YvUtMKAqPsgjDT5g8NLLRBvpHO1KA72sFUHQicURVdjd2Tm-87ATgKD7yWoTagFHWaTOwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQvr_JHzJK9U_BqI-gnq7Ryxiwc0n-hJKKCp1znbROu_cNhOqITx7LpIB5RsmWVmNOljURBUlx7eqA-QXFKFMto2sEjZx8VRn4ReO7091gsWxT-mQ0N6YXKYG06VAyuAM5mQsFt_K5iPBJO7wxxRL5uzas7vw7kaRTUWgyRKfWomkJWhtd0F4qohSEI4FpbNluZXMc5Civokl2gmd5BtvKRGLEf5Xeqfjr20Tk5B8TUxjizoCme8YC178Pv9WJ2RWTjrfbWOYYn_NYEtL6jA0S_jofOjG1nZfxqUTUc1WuX-maO8gJJpLzBXx74gbAMD5J04Vi2L_kP5KqLLuXpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EayyDHbwUp2Ti0oyMgZahpe6zbfI5peFzWXGweiNAkbSNTDltVoYFh_21BGqPAwVdkzw6NzXqDDcwowATSFIjJ9R7h3iuk5AiPA7fCMA6upU5NrtO32_WSxyKr-t_UbdMZ5OdauyV40VIbBZ_yvehyBuzIiJK6dLl1rh-U9na2uLp3RgvErR-FkE53RasDiGeoK7FoMdX4yCZKJRf7Vu4Q6eI3tPSPCG17alYEp7-6qWFLCVxdY_yClHzWjBMbVDmO5Hn1lyDmgpKRVZamqNdACcSRkqiOqTUdgdhrL6P13Ksp-4rltdciEai_HxSB918HwhPW2EVY5vbZ3bP_j_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5d5FmErc0ypnl0SNWSBppAKhEETLbTwT_fbH8q5RNrG0QlXmruQt5I0Zfivtoxg_TicbuEtivJkCetSxqIaQHQ27QsLi9voO4vZuTwPtp2by4VDHx87gxmCxuafVygwItQaBoFPS4DPnB0MGzrJZb5Jp3J4K0k_fOFXeWICRs8Lgs-t6VEW54sy1tah9C9Fnx4_3e4nKtez9R1XmLlhzUsuCSjsMsH60p4yRKV6x3VWjj_J1N4I9LP2ekx8JVIBEyZ-XHbrKmJKszlML4Q9N-6apsJwGhWX87RgzioQrLy6ihcFTvlQM342HAm-TFf-bSDMsS4yBDofbqiqaO4A1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLJ07fZMpjUqIa4BsUpcd8Sy7O-2vhV30kgm9Bn2x4QGBRIGNU8BcFKoGabC0Dxyp2a6y82YbUIXJ6aF7O1er5axMTZgjtsxZfpz69ZIkl5v63VJU2GS77VV_-FHnbI9dSu5L03NXrvzpaOF_n1oOeEaOKdmm1u43LEaXBYFzFam6V3f2m_NBOoME-gTcT5iUTAHEvS0I58MxpUcW9YkqMpp7ypgHJpNB0GEaCY4ZgEjG8WHpAoe2qWs7IqRC1fjlchDVIgRSj0ntmLDDMncQYLhS-1Gf86kZNLzpLvgZrXzaodnYhp7q59MRTtE9CSlqhmp1Sog_4ifd33pZJ5lAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJky9QgM8mtY1dn-aFQCQJ9cgChY0QY4CynLacVsCD_6DlFUI1Bkumr2jV86JbvMjgrvd9gbM8cEi8_t6AuPsJ-xmeqpS3klIxQXkDrboX6yQ1jSsJJvoROfrH9aq9VlY3g7cT-QJA9lmypgmt8bJId2-wF54ThkN-l8pvzsW6MoOfKNr6qHR0hozfCPJWjCQ8Dfwf37pVqO2A-KQ3tGqwmiseh8SjwN43axBPj1YH9LEzW9OSyYC0MO20ADd6gnaNL6gJq82HmWou_jnymgYksam22YR8lKNh1EEeC-byFdBixo3ZSVhBjJhJ_96gQIXp9RkVUSKscBCWYHp4fohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r06agJUP4QT64g63xhmysjV-5xe0VMYEZ6gIBT4ltVcMy-kQK-NlnlvPwkwk3ocQY9436bo2zTP4d4I9YGbJbZqGibWze5Hpwgn_qlVmk9eY820mattF1IGSx8pReZiM3DCxdSoVQ-_esCq5VKmEMUVbsZ_189bdk4PUdGSZxOfXWb33H7d50xd2LA0xo03-pRiTqTuJtooajnRy1f3crxbUGEcjghufmmLBAjRsidBxPooIv584WCp0k9k2cUHYjjSlESoMIP5Vrwnzsoae31WnYvPQdvT2H760cd0H5Yw3iQenMz7B024Zmq8_cLZGRBLfotHxFF4xj5wR4HlUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9VfSIJ6UlmXksjujY-991nZ_LBfbGTTLMTHSgRnK9Cu-a4iUyMXgaOhqien5Da9z98GeLxE7KQ5gzkbPF4se2HCLmsDXHeHZgqZzkTzIEtu3jTtNUsJi2Zts6BXFRPfE6do0pVgvFB66NxTpDsL5CS7oe1ihO8DyYpNf8sDYiMtfq8GRYcKOhy9YKDeVh6t4Z9cXKOqQawH7D4eXrj_M86eStKIi69vLlDnmg1dNinQgt2wMtlmO5sE4rZfPF-EXYNmzbUrbRYf3FhlTF1DHSczGX4nCSMluOzeOIjLPpg2zTXCR81Ul81xkaBqz-sXfIUUhMxaJue5HwrJFzA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDWPtvk1nMrpfRlwrkJVn2LBP6BPLyckD5P2ubZNiVhjBYCKF_kwuAUUj8uMwFTtWznybOAMT8gcs-uaFmnoTEJsYSSR_26z5kn0mrMC-Iod1hxt7k5s2JUV2e_gCTwWFWQx52uFXdQKkBb2aM28YEz5ihFRgAJ6aO98A6b_VN9IEW4onb7MW9JH9RNWOaeHJUPysYyuSuxXnFXCPN-HDN4uyOj-MM572_tuGz3hnlnF9z-ERrjEEs80z-kgE_YzZyu1MPpaJs6BUw_1iyEy8-A5CU4mK3ufGA_qEwWjPlxxbsHOmXQmW1u1Lr6EgFbm_XtsWUg1r2NjUwuiFWxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joHgx8ZAXmUIQgkjd2EWnM_rD9AzU3dXJJk7-C-K7JuXOXh6VOtPa1_8mKYTKzTNdoRLdA0oLClKRMCk39Lx7h1e_CwNc5X3CnW_rGu-rRrkgFU8qtIwIzLOKMzdOf0tXvPBg9CT-gsLkvzi-96_dCO_RO9urO_cJcmaWsQAVZjwVIwYhwxMgI_idYVL-EzGENTfV053tuPLBg1JQhmC1vTY5LaJySrQjHkGyUV2mNPs3CeHGw4HVgPHF0hI8m0hEgwu2kTrMQDPCKUhm7tv-4LCAI0VwNqH76_zWz7AVbk3IFzf9Oajl_N6h_ekFQzj6-Asiiln5NZFbFsT6Mkt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=tCk5nXxlqu5xX4q5UNXTNGaEia9TG3bCHumHGdt_L8CaGGyF4AqhFiPG17KILPdRXAIe13EccT1zrJM3IJKKH9hSEY6aRXZgpamIqZVt5uhZjDoTyPh8zck9u6ZowcpwkRQIZtHe9Xlnke499QP77426s18bkJcXnJCVu6Qxft533C1Pi4XuDdCObADPQDLsjuHbWtqTQrBfgCAppx9Xgch487gMJ9NOsKdIPZsjF6sq3J3goeM8eLmZEMftPjtgSx3uRtVUcTv_FF7df7PCSpDQkjJ8oMgdEJCVbrqPuaFIZ2tbJG4Q0wt5MxdEW4JwUFGghkYhPwX4DdXNJpJ5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=tCk5nXxlqu5xX4q5UNXTNGaEia9TG3bCHumHGdt_L8CaGGyF4AqhFiPG17KILPdRXAIe13EccT1zrJM3IJKKH9hSEY6aRXZgpamIqZVt5uhZjDoTyPh8zck9u6ZowcpwkRQIZtHe9Xlnke499QP77426s18bkJcXnJCVu6Qxft533C1Pi4XuDdCObADPQDLsjuHbWtqTQrBfgCAppx9Xgch487gMJ9NOsKdIPZsjF6sq3J3goeM8eLmZEMftPjtgSx3uRtVUcTv_FF7df7PCSpDQkjJ8oMgdEJCVbrqPuaFIZ2tbJG4Q0wt5MxdEW4JwUFGghkYhPwX4DdXNJpJ5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5MxG8-1ay2_jYJ3ecLyLzaprZerQHfSHzjrYALc8i8vym9On5Q7J27z8Lr1amVUvSTlHEcZV-Ij9M931iHqmfp5M3XeDMeVDMGyZ7fXsj_ORQ_K9nPH2Wl2x5M9183imujvGBgmlQxaEAbJBew9riRfJXRTYjxywAQdDNNxkzIu_3Ugp4WQe2IF1WL0hkvQksFymt9IMXvHw9NnCsD2Z-GN-B-JM7K6KxkvKnrvz9iCgEeUxZozj_2IGNBXbJx_azVt6C-ci9exx-5lCQ5AfymaZzKyLQeJB4brYz6lzJsVyJ0LEaNrxPdrZ7Z_wtTF7UmOAk5hMRkvJdY-z35Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=RzXf3wSdlXoXDwGM1stdBIIh5eKAYYzt-fX9u_nhy3NgFaeQdjiuSFPFnbhuXHixP0O0yNwY6yNjwj0Mih13LwSXM7RGk4vigmLUADGp5b6u197EaoFNBptJbMsr4FVTzZTnh1KneN7FsX8L9RixCwD0jNJtlMqd-TxqxDlOXdTkmyAsEYzkOVSK9uLEbxWm4BLfKPF6tNQ23CwMTbhvenabF6lJeIssd-kxUHULPfC50gff-X7Ud_bBPY8UaXxUrUND9kFBn0RH69-VSoA6R1Do6XUVa1nTMH3DT1rYV3DwEj7wcufGphIpLhuGkgtI7ywbTcqiwOaZTbCwqmc9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=RzXf3wSdlXoXDwGM1stdBIIh5eKAYYzt-fX9u_nhy3NgFaeQdjiuSFPFnbhuXHixP0O0yNwY6yNjwj0Mih13LwSXM7RGk4vigmLUADGp5b6u197EaoFNBptJbMsr4FVTzZTnh1KneN7FsX8L9RixCwD0jNJtlMqd-TxqxDlOXdTkmyAsEYzkOVSK9uLEbxWm4BLfKPF6tNQ23CwMTbhvenabF6lJeIssd-kxUHULPfC50gff-X7Ud_bBPY8UaXxUrUND9kFBn0RH69-VSoA6R1Do6XUVa1nTMH3DT1rYV3DwEj7wcufGphIpLhuGkgtI7ywbTcqiwOaZTbCwqmc9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=ViE2FITiecf88E8qRjueL8zyJcpWJcFi7c1mWCI9akRoLl8HVwLp7lbkHmwb2ensBFSPYKb-13lzEmgzzfqHI77VcsoCM6nD35QjqWznM5gbzcr5uclxDtfC47kIHI0i8hmCzYYUtHsVTF5323B0lyv6ljzvD9ijLbEMYnI3_kN_grORskGFIHHT0JhDQsEIZ9OTuqjvMNKRnv9E9byBFWBFFWY3QXteB66lh9fRz-dFxyEREdP5uhSvhs2MAfT_gwEXgV_IX3fJjK8sy79EAimxk-Xota_--nwwTTERvoM-CFvwF4av8Zak6mbzQoIME5yE6sI4Qj0Fnc8tofeHtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=ViE2FITiecf88E8qRjueL8zyJcpWJcFi7c1mWCI9akRoLl8HVwLp7lbkHmwb2ensBFSPYKb-13lzEmgzzfqHI77VcsoCM6nD35QjqWznM5gbzcr5uclxDtfC47kIHI0i8hmCzYYUtHsVTF5323B0lyv6ljzvD9ijLbEMYnI3_kN_grORskGFIHHT0JhDQsEIZ9OTuqjvMNKRnv9E9byBFWBFFWY3QXteB66lh9fRz-dFxyEREdP5uhSvhs2MAfT_gwEXgV_IX3fJjK8sy79EAimxk-Xota_--nwwTTERvoM-CFvwF4av8Zak6mbzQoIME5yE6sI4Qj0Fnc8tofeHtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23277">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUrJlTZcvjOkmtWgE8Pusy-UVytMoCrGv2FN7W0HAOgJ4uQQvq-HmRbIfAf7OUoouB1wlgzVDwTtev-A-ub5GTx6SrHw3ZqyaMMv_EjaOxm7eaRj2x1K3OZ4krppGxuJjKjR7F2QesEw_odEYqDLn3iWZ1_2aKaFee93cEiNpo4NHtsTF8T6PsUkh6tBXkXa1-tLpIvLgdaKS8s0qH_xRV-KZVYU8jKj1ti5VXA6jL3IMeeVGdcv3Wz7MMkAe9K06wLHlbQ5ekG4khtZxLRWd2_tTkUrWk1g9OgnT4Fa4E7qkOG-WTciOdDT8Ri7jnSS-qTlotFor1z3jXsOYmfv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23277" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1TtGqXMQAyXNZbXBknXkwVNCvUHKFXBJuoIRPawWC2lf1mflV1NX0muxrCUNw_iCmnbiKhSNA5ppATf7Cx4b2sZ9C8zMcUnzQKKto3JLNcxNwoiC2IjiatJ0gvTBXi2ybzELlINKwis_aTOu8K2WIXBsNKvgh_FAhYGXqPhQHZYe1KbJxuo3H8c5poVAXlXV9dI3vv8IKJJuNnQJafJUgxOejeb_X00-Z7XAUYmwbPKDhraPUSu6U9tUEDKChq5U7sE08z59k5Qzo0fn-uJwqGdI-ZMX-Bo-MaUzPmBp2UvfmO5JflCdo_ocgCIBKhZsGN3mizjQ-0mOcebiWvChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=T5ao2llbyZiPGMwE3VqgSzUeb-oRIxZnaLmyNasieqxjVdEmGfCWosyJf688Ove7EHEdScp65TEb5BH1WiPMuHd8qnFzGlHD8bXl1WHW42yY6mDjm0yYi3O0gxAdV4Qalw7_QABgQHS-OQxxNZkaHlG2N1aLjxLGt73LK7gmUchX62Zxx58NH4_yTbv6RWt1kcoG0CnS3BO94Og5KdwEWkubp5JBxsGa7BCWISG8JzPubrnjzsL2XnwtvmfWEPOsGxBZV4Uv9mBWuinYF2OfE8S3os90UWzZlFt9XsbipaEHPgGqvYBvb_htdG5052iSVhKDgMclYMZA5BXo4jC1WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=T5ao2llbyZiPGMwE3VqgSzUeb-oRIxZnaLmyNasieqxjVdEmGfCWosyJf688Ove7EHEdScp65TEb5BH1WiPMuHd8qnFzGlHD8bXl1WHW42yY6mDjm0yYi3O0gxAdV4Qalw7_QABgQHS-OQxxNZkaHlG2N1aLjxLGt73LK7gmUchX62Zxx58NH4_yTbv6RWt1kcoG0CnS3BO94Og5KdwEWkubp5JBxsGa7BCWISG8JzPubrnjzsL2XnwtvmfWEPOsGxBZV4Uv9mBWuinYF2OfE8S3os90UWzZlFt9XsbipaEHPgGqvYBvb_htdG5052iSVhKDgMclYMZA5BXo4jC1WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKZd3jcl519E9PKSBerQ_cgo47QTweZyNx1cDFByktMkELhbgRNtc-HKAh08RIP5Wtz02utZqyPJtTi-uB_Y1aocDDmoEodtJphLtQvREStFz9QtdsI-v_bjK3NL0ro4ccmmjYRMc4dA_GIXG8L0jTCU8VCbNr3bHgyVhmkPn_kdE0fqC1Lre8E9gUc7xYjOfoPnOWVUNgehmiNf6Zfv0SXFJaFPprO7gJY17gTTTDaeOYlL3N9ed1RPkqQvTgpoOFjfiACeIRIQEbHhtrGzOQBWAbdSr47tLy1bMSnuyKzL4lMO_dE7L1H470SV8LEZcioDLbTGC1DNug0B67xIJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=Ydu92ATeZO63lmMmPDpGPE40tpeD1c7MLT-L6hJz988VRbcfiHZewr7BqB1Ajf5V5N1hx85Uutu5gxQyaMqxSJmZVqJyb7o4T862l5bFHkkvg4Nptsxi3FXdM1fvRvkWQFdNVumdPnGAUO8UpWfa10vlXChMDiuvx4ywcrm4I_0CyK0gK6v8dSUX3B8QuMOGvT-U58u_kouMe6OJeQ76DHo1aXtP8yBqzxhHcLiXlAQdzTtT2FRfMg1FjjsJw_MDTMXG1Yb24HkJ4MQys_EqfRtyhfRQx92Ch2Jgf7JX7azgntm71iiHHg_ju7-YdzIKcx7MYB1iDVPG_g8WL5Deww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=Ydu92ATeZO63lmMmPDpGPE40tpeD1c7MLT-L6hJz988VRbcfiHZewr7BqB1Ajf5V5N1hx85Uutu5gxQyaMqxSJmZVqJyb7o4T862l5bFHkkvg4Nptsxi3FXdM1fvRvkWQFdNVumdPnGAUO8UpWfa10vlXChMDiuvx4ywcrm4I_0CyK0gK6v8dSUX3B8QuMOGvT-U58u_kouMe6OJeQ76DHo1aXtP8yBqzxhHcLiXlAQdzTtT2FRfMg1FjjsJw_MDTMXG1Yb24HkJ4MQys_EqfRtyhfRQx92Ch2Jgf7JX7azgntm71iiHHg_ju7-YdzIKcx7MYB1iDVPG_g8WL5Deww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1a4HIan_gDMgdX7WkaTGsNjaHSMG41x-rmRwvLZrGsWpqg8ETj1vVWsXMx4NWCcg4pIUNUk2xt7xVKYvjxY0m5iog1eO8oVmq6NbIn6GlNZgO5IgYaFoIL_r-GcG7d6GJ_LxO-pdH1gteV_QkcWeog0ZaASMwIKoDoZofdnaR32JqLVMJ4lRp3Y_TyHmNgLni19j4l4HU5aEPdodR9Qc0uEkiJlskN5uh8bhohm5M-GBMA1wDWRjcFQZujjd7UTvuYlm1RUh2tKeux-8LenCmL4IRlFWD1SWWj19uV2z3QPztjR7sUpSzZZYcyVOgMVuCr1fmg8IymG9rD87h0oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrGHYYQI_Zl2eixSqZVgkkUc_BsPgqDAlxYQypapXh_33es8q8PaDQjKEIoP2z48CAKGxmxvwQmBPBW4ugWUDozweXCp2Vo-eFcJhNvKqRaxmEDK0DKoOgPb4nZQHUk_n04-dTpsXes8GavejlJNmQeYkevzsVkFxGcF6FzhWQRlpbNcj6jxQXtggqd0V7FGifoluKwPepjUC_yG0HTLVub6O1fOwSX0k7khYKMTogqDsrNGxpMoDTaZb2jnwVnp7I1cxBwi3CzpxdAxd2sIuOoa4aO5mXlYoDB5yHXonhbLUnysLAtfQtm3QGQ1uUvzfRCxhjUn-MaPLVTnw7AiGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=BQeN_b8DCspLVTjDP6D51O2Xd3P8W9h9v8u5Kd6n56nmi_RdqxHeqgSc6nZciOihkGSqDlS8befBGyB15tp_mhpoZhs1UbIhzMkBQkqxTAJ1t98qQEr3gE-K7OZtIlpThs3BM76QOa2It25-fIcDw0_JN-RSKrBp_4iLdM4daqMVgEP3iVy3eso9T5i3JKwtqiC96es9c6Q1Xz3rWLZFqop-wNznFBsKzZ5RaqcdzeQjawuHtXp4UT_zTwWw5zzUeKdeX79RilQiJni6azu3qMYgkZDCcKIQAsp1nKGYkHY3UiPSSL_gNHUev7cWQZmtSbcklsnM_bchxGQ21wJ1dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=BQeN_b8DCspLVTjDP6D51O2Xd3P8W9h9v8u5Kd6n56nmi_RdqxHeqgSc6nZciOihkGSqDlS8befBGyB15tp_mhpoZhs1UbIhzMkBQkqxTAJ1t98qQEr3gE-K7OZtIlpThs3BM76QOa2It25-fIcDw0_JN-RSKrBp_4iLdM4daqMVgEP3iVy3eso9T5i3JKwtqiC96es9c6Q1Xz3rWLZFqop-wNznFBsKzZ5RaqcdzeQjawuHtXp4UT_zTwWw5zzUeKdeX79RilQiJni6azu3qMYgkZDCcKIQAsp1nKGYkHY3UiPSSL_gNHUev7cWQZmtSbcklsnM_bchxGQ21wJ1dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uziv-EEEJt6JT2xHd63Z7DzhHkqZIx8GgQUdWfNwh7_xR0TfkyDpkKy-sU3SGHN48d59OTo24zqsJVeeVv77JPdhzY-laahp6hj8EwFA5DI9giGo7U06GrPk1rZOADxDQKkRvaIQ_ByrOVYzhm8H567wFbwjPaKZPvF5udiIzZXCRsoLDXWQ46sYJENzyGM0wo8nlFNVNhCfS82S74pl2jXW0sNB2WHF3Qamz71bVLGjrRKbzen8CtETwpgpMRD2RTDnqWNAhInQZd_ZZ4_dAU7gyRcoB4dc_rUHEo2MTS13JtyQMEWuW1u-Mw81ve_pzJFZLDXc1VSKJ1VuV8FAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_DcqUUJFa04EW_RDh5X_KHNfL7xV6WUVisyZTpDwISEbgXX2teSNtH8jvLlpMcdfHnwlL7_5xpQLnbANcCADrNuLglzCzKjVrg4j1FHls8lo9bFNBWBFNWfFmM2f5CX20domzyfG6E-SpeoEo_zBSyEYDvTIek39hJcgDA1DIQwUFZ0ZxN0hLaQ-LelSbE5pm9Yqdrj_oYox2vSVobSXFmgjJfQJ5G6MQ0bWeQozMZhDsLI8bz4_lGkOW280phvl_a3zskx6izDJmpLab67lD3RmDBRTuYKRgOqhCBnFSSMYGnaF6eD5O8kydXXb1Te3e5yzJj2QRSkrlJnF3vruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=NcWqRPPRkSoSwHBbPIzX4Ah8bI2yWOOQEK1xBLIfWiN64yeUQx0vHU7tPDaNum5viLAsUrppVO2-7DiO4iHFz7-_L9y6B6LZbOFyKt2KCucZ5aKG_GvljA37WR0AnndsEyYsTJwDB19ejcR_v8k3H0eKGSiAEWdsgLa-gKMgqmIDq2Cy0PnwxMyCKCuVDtdvRZvwKc30jRap-3C6EfQVImh8lhc3iy1SzUCscwoS2JGsI39elobHW_GIretonMx2pDdbqksxQcGC_GIaNL68zEJtIdVOoqkUqelePLH2rYaHcBo8_ZN-UgBXX1EKvvxV6fQzUA-9kFfItAB_rHzJUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=NcWqRPPRkSoSwHBbPIzX4Ah8bI2yWOOQEK1xBLIfWiN64yeUQx0vHU7tPDaNum5viLAsUrppVO2-7DiO4iHFz7-_L9y6B6LZbOFyKt2KCucZ5aKG_GvljA37WR0AnndsEyYsTJwDB19ejcR_v8k3H0eKGSiAEWdsgLa-gKMgqmIDq2Cy0PnwxMyCKCuVDtdvRZvwKc30jRap-3C6EfQVImh8lhc3iy1SzUCscwoS2JGsI39elobHW_GIretonMx2pDdbqksxQcGC_GIaNL68zEJtIdVOoqkUqelePLH2rYaHcBo8_ZN-UgBXX1EKvvxV6fQzUA-9kFfItAB_rHzJUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAsokkGht3PbJ1KEAO3xLVm5xVZuc3n7Y6f7AJAUwWWUSsrhp_cF8SI9FHTCVgKPTC5A_CxqPCN9-9MboI2po0pu9hwU3lRJlik-ujL15UF0F5jyufeADeIYGXK0IB_VCPQdoYttv-sE8h8dB5pZ7BWW8ufYkQfUkKoZYztXZwdt0ISH38NiYluucxQKFzwAA1s58Z3HGv6dkrQLp4tEIMn5gpZWq4SBTXp0qdL-e7ybEVgAgg0Tt9IF2WzjBhpk8boWiesiverOdZTO-g13Ft3PfiL3ClZ5k7iieSQE228WT_vvc81YRDokZ0KisMXjXikoiGgEepBcrfW1A6nHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=qbIrGaeI4Vfd4VIAF2zfnCDSfQqf7FxX3rc39LeFPe4gDtfJlSnu3UAVYnxRiPs-u5rCGOlkXhQSVOrGFlUCc8BGwJ8x3LUBIk_dUbttn2F7iMeTefEYcr0SUQueiyquD68D8dy5pEruwVt137vpy7M6eTvohhEmwiVmQ8qniBfW-dmiv_6sZ7KAy78HJReQNJnsbkG1s2gXiLbtblQoN3KHsBQfZ6hMHpkWs7jap5eSlGwlsP_8zRo8PODLvieZYawIHC7GQ44UG_GWThjz1KwMpXP5Qfwqd8gALh1bo-wMqi_Uk4FNiqieXyXd_IDVkV_mjh0oDi8JfE-SShwmN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=qbIrGaeI4Vfd4VIAF2zfnCDSfQqf7FxX3rc39LeFPe4gDtfJlSnu3UAVYnxRiPs-u5rCGOlkXhQSVOrGFlUCc8BGwJ8x3LUBIk_dUbttn2F7iMeTefEYcr0SUQueiyquD68D8dy5pEruwVt137vpy7M6eTvohhEmwiVmQ8qniBfW-dmiv_6sZ7KAy78HJReQNJnsbkG1s2gXiLbtblQoN3KHsBQfZ6hMHpkWs7jap5eSlGwlsP_8zRo8PODLvieZYawIHC7GQ44UG_GWThjz1KwMpXP5Qfwqd8gALh1bo-wMqi_Uk4FNiqieXyXd_IDVkV_mjh0oDi8JfE-SShwmN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFa9fuzKpxtfVkVty1_75J5TiJiTZf3hletj5QFIfG2xaRsbecFmHJRniiewdxznBE4y6Yao2_8GIlJP9IlUlKMgvzwrH77E920B0EpI9ZWu8T_UPWInAOcwazD10UZKpbaOOKmVAmYUM1_Pyo7KQ9rOyVb5Dwio454ynKkzbRtA2i-0FPd-2OKOCdOv0Qm5QBz2yyhkNqiMNT3tFNm8DqMUpe97cQS8XKEEFsw3rPOCnZ6vUkJzyMQW7UkWORDWHL0-h926exzaVkuoRfpwhWq_4_cKjtAW6h6fxqa2FXVbEs8LC7vfxNKcrYxPzysaOScYAK3LSI_SnkABtcpPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=blirRHtpfOOty2HrhW55nZGpSoaABlxDsICYPX3J2urB09RZe0tnFlzD78F4SbGvupC5QG9JBhDddWKH1VlvDWc63-K0w5pPVBI_-i-aWM-kQSPsCTlptEvXOJwUVthP4rwbfGAKJOjBvKA_aFiCbTouMWcTReZGFgCM0QGzegEMzjCAVrCJIv8AW2M49xMqfO0MGkom6ZMUoPXf_4Go73ZmL_Ft9Py_pxMh2Icq3gsxHvBDDSW1GnztkM7Rqkb0qnKiM5YkB6nxxTWvYomNMion0Yh5OotMDijDYbetGrXztAKUfFh9d_Dxo2LhO_RkEwTqNM2Cgh1XqvO8v8YZmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=blirRHtpfOOty2HrhW55nZGpSoaABlxDsICYPX3J2urB09RZe0tnFlzD78F4SbGvupC5QG9JBhDddWKH1VlvDWc63-K0w5pPVBI_-i-aWM-kQSPsCTlptEvXOJwUVthP4rwbfGAKJOjBvKA_aFiCbTouMWcTReZGFgCM0QGzegEMzjCAVrCJIv8AW2M49xMqfO0MGkom6ZMUoPXf_4Go73ZmL_Ft9Py_pxMh2Icq3gsxHvBDDSW1GnztkM7Rqkb0qnKiM5YkB6nxxTWvYomNMion0Yh5OotMDijDYbetGrXztAKUfFh9d_Dxo2LhO_RkEwTqNM2Cgh1XqvO8v8YZmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diGf5gbiQE8_gFnNBQbBcvh0lQ0WglRJLdFgr8ZfiVdT3tTqCDoUpsHeBxVMPE17gGCIdxLiK3ViPnnrKnKe2EWTiAUJ0bhEWWXU_bop8TxLCc55ewSzp3CG_Nlid03SStrNyBrepXBFT7NyZB5LpJh0obLyfi3029mqCXMXMwlAtu52_3GGK3kMJIl-BofvJDgFfdKx5Z2wx7xTev23WbxJo4cgtYI8Oc3dFuTzFDXthTOT8k65H8EK3hhV5s6FO1OkiZOmy_6Td7HXnpNcCqXVnSYQf1W2rOBWkba2FKW7cPJpL7A2A0RXGOqlYvoJ7D0jZ85anhdZL3M7Ogeotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=m8Hc5qXJ7do-rxU_w2odkyU5j8gScAIupOksOPZRDPrKKtdMFjTwVrSueFcTG7svmKLS3nBzQlocPNoOs71gJhD4HsOiOITPOf1xiRN9FFjr1rVvZlivvGbQWZZajAmH628JgTT0C-trKAUWwA9i2n10EeqfkyKe7qdz2kT0qm7Qtl6lti_T7bR3aQhIhSQ-fTjwopOY2BjqMeILRMk4kwJE2-HzQy3lTdpNTAtmJ6WRGM8ZCF6n-J4wHyN0EnCt3v7sGNnDqnFkDEiykV13OQvOmwKAOyb0nFx-4TZprg8ra8_hM6QR_QpFd-g5JCDvvwgbDbqsbIzgUkiKm9w_dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=m8Hc5qXJ7do-rxU_w2odkyU5j8gScAIupOksOPZRDPrKKtdMFjTwVrSueFcTG7svmKLS3nBzQlocPNoOs71gJhD4HsOiOITPOf1xiRN9FFjr1rVvZlivvGbQWZZajAmH628JgTT0C-trKAUWwA9i2n10EeqfkyKe7qdz2kT0qm7Qtl6lti_T7bR3aQhIhSQ-fTjwopOY2BjqMeILRMk4kwJE2-HzQy3lTdpNTAtmJ6WRGM8ZCF6n-J4wHyN0EnCt3v7sGNnDqnFkDEiykV13OQvOmwKAOyb0nFx-4TZprg8ra8_hM6QR_QpFd-g5JCDvvwgbDbqsbIzgUkiKm9w_dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C13XvoRfMmAJoxVr6-_IcTb2ruRL_3odLus7HXSWKnjh76YCUtZr-7NnCKlJTSjzbMf5uoJLRmkjfmAU3aS5-0qhMtzQIvsPHNloCDanMZXOexk_UV7pTh2YnfapOlVzmPbdumoPJbXe6Lml4p4OpK6Brp33wF5qjXuKUOENRtBNaLhDS5eAWjRa3GxffST36xJKBY3RD3D0NEzqrCeJhpCtW_bh1AgKPglr2knIEWMZHkD466rVbERky0z7HujGR6nBlleM-wAnHXpdaNgDA-krjX8fOWxHeebom5FWMgIm1CBervj4knfAU01SEW18nqL_7WGMGFUw5qh7eKmhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFF_4Yyz1q-BYTOpDOiFBHv-SdMGvna-XI-TTqPbFx1ju_o19aHzm6YcqM6TgYFIXbEftaIO-PAYGjUeNsf6XthIYz5QZkSouI4XbVEQ8HZTsn5_ZOrQgsVtpC7QSHiI-KaqubKJPOPp0qCVjuMmS8WNs4U2eIGcCONbxHstp7B4LVLZwpkwFgX6FzHKmtPKnbWL0XvDaH01kxldRHwUGH1ei-xBu5SDndUNyp-f91T-HM4urPZLuThZRGeYlQRTb1E90NK-cFJXUkp6lzl-9fxEns5T9yKWXcS1s6yWI9954imc4bTX_dYNiyGPgY51vL2ZyV6vJBIiNWfd3QolEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d62cMLR3cL4zZIotCGw5ijrGFGGIxxEZtkpFvYlBgZf6EAuXl_QfbEaaDm9gFj4FyOP-8JaPx1Mqyzrasi9OjbYeYNNsQgJXlipXwcx48Sc4MA-BvsXt_87mdQ-Tm9alB6k8p6u7JADr0G02lVzFYyFh04JHwxbqzXJqkjF2e6ghie7AuZdk3P99j_PmPWLiaZJypPZfETPiQrVlEaMBIxbGzNz9EBwMaga-9T7qIxqy4VZhQ1Y_WAFCVGRk1tQHTzCkAqBcWvEumCQT_cTcI4YwiYwTkbChhXDgZTIMNUY70_lFLfHYwMV1qbkp-xjliiVbJO3s2bGHCvUqqkK3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdnhordRtiy9yBkVC1WkIwdWoc9riiXRYYPz4McdJ3rXzGAjrlHKkZLgpexK16OKftq8Sj4cpAS_aeD-yNdi0CCwFt-7BUucgE41Kck5UNli6HvxWDGM5VH6oaVXFAPrKpBwkMilE0LX9DF6gEQYtmbcnBFCvgMQ2AjbgBnc4O2soS0XoWfda_fGOsYTnktBUTcNF90eKJhQjXkSCOsPG1lRoZozeBb19doZo5kaRAm-sB56GXkC8p-4WrAisf1tXPsjg_RE-_hJF5yjmOmwyqDbQas-XPYLe-IK89LVZsClHMvmy6RI3RbnIOX63MWIicNH-LujQgARIkZsclAqvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=AVuUjD1Ej8Yvw9QBFdlm0B7fd9KI9h3F2GzawGkKBYcVQqYW6tpqxzsvUDTKWTFYV_sum-rUUhTKDS5NpmDCb3A9wRqa4cexAjEHxH9mAhjLz-0Zbca881DxwbqlWBec1H0GAt1pSIiadweJN48IT6SPsgt8meeHuMn5hNOBlasUQh4j8WU2bahCflm3-Z6RgLR87UEVOAlLRE9qRAoIOYuLg9dmnGtWwMCAyPvXIKDFmQb0bB7D97stVQOdt-Z28j1fuISNE2gFiSKPvWNuJyxozOyD9Ft50VwzCWLeTZAqQmuI1UNeSJXcZ3erhcZkCS8cxwtSJDdrgJgBBpPGnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=AVuUjD1Ej8Yvw9QBFdlm0B7fd9KI9h3F2GzawGkKBYcVQqYW6tpqxzsvUDTKWTFYV_sum-rUUhTKDS5NpmDCb3A9wRqa4cexAjEHxH9mAhjLz-0Zbca881DxwbqlWBec1H0GAt1pSIiadweJN48IT6SPsgt8meeHuMn5hNOBlasUQh4j8WU2bahCflm3-Z6RgLR87UEVOAlLRE9qRAoIOYuLg9dmnGtWwMCAyPvXIKDFmQb0bB7D97stVQOdt-Z28j1fuISNE2gFiSKPvWNuJyxozOyD9Ft50VwzCWLeTZAqQmuI1UNeSJXcZ3erhcZkCS8cxwtSJDdrgJgBBpPGnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/binreRkLAH4CEtr5V33p9EUx16VdkUiquAYiZ87g2rYgAOWaGT_pwKXxZa518PTvWJhLRdF3AxwKTBSlHT-ibp7-nr6BNj_487C7c2-6zrgTcxxSVMjIJuGvLH2wxpv0GtZeCLPNguE_5Kn3dHB_roC-MV8N-Kr0RMXiNgUbpdyihwaqIzSjuEcPjHK_AbD6uSGR2wiCNd48oo_034A-i9CmlVyg67xd6pbFgYlcvH3NUEabHpxajSyMYTBDxwIS5wOSyiNkN1r8vVcgDq8bm5qq8IK4Mamo4aUAyxWlBb17DaBq4zDNoYqXMRFz4Zx4QCj0uyCfXb2hci2upmy1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtntpezvhJ4WcuYtI-m9ZHiCszm_kfPlkSwxHjrSxvKbwXpRM-wKVDQG2AphIn0vJUZZcwt3myp4x9moiKsfjt43--XuOHgzBJ7_fPb53cg1kpYSId1TMics8kSu8FQCz7G-VOqcfIZQrxBlX1MEESDSrB39HNVIhquvlUvWIaUyTngd35TyXvQDnmTUw5ndOW1S-KzmoFtd6ORtxuaSvnLJrhSmU0lnPgUkrmjCSoesCyN0bpCKLxjPbGTx7bnJK9fpgFYEfABJCtTAJdoRDbQQoqcRL8KH6ruJBJFKyaXHTiwa5Tnw-exVKS7lEoidwkpdk6MmJoW7-t9XTb4nEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndthugoiICknJWo6O0DlI9JAxPHawadJOwy7awBLDcvvIdUc_d4ub_Ut-QKQ2Shpzq3uR9YUhaEIoSC13x7xWo7XY2q9XmN96G8Wtphuhhnxypo5bPZVRo_IzGoJkIjFOIVTEJLJyUMI2rnqh2SrJsDMKzxbe09PPEJD118SGnnxtTyF6762mEPGMiBkPRXkS9F7cRcRh9UEkSrzCJQqP79lAUqciW00zIbFo3nOMgK0lGxzqlQktyFdMfRIRIYFaGoDH6A6iGUBb8m7eeSxPoXUxhZrv4K7zpxB0xOEyZ-6Om9WSDgup9G8Pi7-Lyi7Kr_fVK5a1eYjFWeKzHqs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=NR0yTEJSZ9ME85g0V8fMP0RhxKorBOwPUeU8dsVt_5tLWxYUH_eyApc6ZiuyZO3NUgmG2Ju7Lixmg1znUcEh4fKLW2jwOVFOUaDFLVKcZvmRGu5gr9ZgIW2s9E8-zMhadxgok2J4IzhGF6K2o9p9VaQ2V-oS1VN5Pk3Ov71CWib25maSa0-Ll12M7RMlHRyP7gAf_kwwTpd-7HJRqZvDyZ04lSeq86Zox4AMi3xawlNsF6kOrSLTjCakeBu5e8YmEpMLSw9H1luWiiXvlLwlHPQqN6-6Px33cBPmZpUynV7Z5tojKuprVKhla8etFD6jtn9agqV5iPL5ZfyZJerzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=NR0yTEJSZ9ME85g0V8fMP0RhxKorBOwPUeU8dsVt_5tLWxYUH_eyApc6ZiuyZO3NUgmG2Ju7Lixmg1znUcEh4fKLW2jwOVFOUaDFLVKcZvmRGu5gr9ZgIW2s9E8-zMhadxgok2J4IzhGF6K2o9p9VaQ2V-oS1VN5Pk3Ov71CWib25maSa0-Ll12M7RMlHRyP7gAf_kwwTpd-7HJRqZvDyZ04lSeq86Zox4AMi3xawlNsF6kOrSLTjCakeBu5e8YmEpMLSw9H1luWiiXvlLwlHPQqN6-6Px33cBPmZpUynV7Z5tojKuprVKhla8etFD6jtn9agqV5iPL5ZfyZJerzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=h5eSMroMG4f1K7CElsuvzYoIipmJCWtqVNgmlcSsPevXKRua2pTI4wJbK2jzSJSXmoy58fFxssebZnzkhz8ZI5qBGTmAIE-v84q70xaO9e73ocivMVl12VcnrPzEay3ut3SfrHSEME93_PHXoy_a6vVtvTGKqFplidaxrpoX1kgGJvmHuZGcDE34QE2KINLM5LBAstfccz1cbrJyD5yVF1UmBoQXeBXEaBKPebx8aLtWVd208l4lD66uMOD5ttIVgyLi0D-19YC4V5Dr7-gP0PFZuTrshmqYZjIaxEgH4eZDej2AzZwcMptre3WegBQXS16gxTsPjoyRmMQFoqPyFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=h5eSMroMG4f1K7CElsuvzYoIipmJCWtqVNgmlcSsPevXKRua2pTI4wJbK2jzSJSXmoy58fFxssebZnzkhz8ZI5qBGTmAIE-v84q70xaO9e73ocivMVl12VcnrPzEay3ut3SfrHSEME93_PHXoy_a6vVtvTGKqFplidaxrpoX1kgGJvmHuZGcDE34QE2KINLM5LBAstfccz1cbrJyD5yVF1UmBoQXeBXEaBKPebx8aLtWVd208l4lD66uMOD5ttIVgyLi0D-19YC4V5Dr7-gP0PFZuTrshmqYZjIaxEgH4eZDej2AzZwcMptre3WegBQXS16gxTsPjoyRmMQFoqPyFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=pq13GXJnZiHVQ-5ahuKKQ4u1Thh_FYsr3OFDZCFCNiyxSPSmd2LtmhfGIvSZCJBMJmzn-4mkp8MqXRkCU-2NO2UMVnAbQwbXjqDUzfnGDwTeWJ3faaYaLN0YnGM-INF5Sfc2JzqNYvfG5BLSYqrNuRnZa41KqIrBVj2L2b8PH-f8zW0Qvodu9dJTSiYLZzAXIgocupPHRGxRq1w8VsKgICrgOT1T8q1bbJZ7zT5qWgov1zCj3WdQoVpzDOL1nc3OjLLF_6wR_1tRXMu2xQQTcoVHHg5i38bHS2QfP2W925i3cNR6qfLmpVeqG_Hnzv0dIXti6AGPz34Hxm4NoCUNvC0Ru0degHmQ-VbzbVVNBH-S5gp4_nKOQ-nP1njdD4xVAco58saXc_47NICtY11seSS4wFLFu8PlGW2nhD2dWFsxGOgckTH-B0HGsFCPqRqSM3ChjRh-FDGo6szJzTSPCUms1mA79bncXJSytJbEI-1bFafvEkiqNWqli8PeA9p8dBb6dfsGoZG21_CzzeHTc83gsYkV3tKoM8mIqOMIUjRJBL3o6PzPf-exze8I-EC0uS3Ho_L177A42rvly4BKdqtAMo8CUIrUl382oTBv0ymUwY97TrjjiGL4HRV8wFjRiJ0ecKcHquwYCHbIbR-4uLA8j3ypsiY83H0gnTfFsM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=pq13GXJnZiHVQ-5ahuKKQ4u1Thh_FYsr3OFDZCFCNiyxSPSmd2LtmhfGIvSZCJBMJmzn-4mkp8MqXRkCU-2NO2UMVnAbQwbXjqDUzfnGDwTeWJ3faaYaLN0YnGM-INF5Sfc2JzqNYvfG5BLSYqrNuRnZa41KqIrBVj2L2b8PH-f8zW0Qvodu9dJTSiYLZzAXIgocupPHRGxRq1w8VsKgICrgOT1T8q1bbJZ7zT5qWgov1zCj3WdQoVpzDOL1nc3OjLLF_6wR_1tRXMu2xQQTcoVHHg5i38bHS2QfP2W925i3cNR6qfLmpVeqG_Hnzv0dIXti6AGPz34Hxm4NoCUNvC0Ru0degHmQ-VbzbVVNBH-S5gp4_nKOQ-nP1njdD4xVAco58saXc_47NICtY11seSS4wFLFu8PlGW2nhD2dWFsxGOgckTH-B0HGsFCPqRqSM3ChjRh-FDGo6szJzTSPCUms1mA79bncXJSytJbEI-1bFafvEkiqNWqli8PeA9p8dBb6dfsGoZG21_CzzeHTc83gsYkV3tKoM8mIqOMIUjRJBL3o6PzPf-exze8I-EC0uS3Ho_L177A42rvly4BKdqtAMo8CUIrUl382oTBv0ymUwY97TrjjiGL4HRV8wFjRiJ0ecKcHquwYCHbIbR-4uLA8j3ypsiY83H0gnTfFsM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9LtGSC1lNztqeigyXCEAffUeVQNr3leVVD452IsOcKA5EycP9QYNlNbHVc2JFPdL9De4vqzYexLc2LYH6UppZp6UESxVkd-mjxspxxv07EXKeLzVfn1iAm85qnVIcfU1SexsluVsZTRTYwSB_NjMqv6geAEaPkOEBWylactjnYeSI9KsoBYqy_GeSk0rJ4AtNIEAyzHMf92dXiwJtcM2F9Ers5SD68ssGS7Ri-3K0HI3Lg4a-5BeN0DtkUpWGVl8piz1FuUr0MEcK_N0KRRTcTZ_EA-g-gOzTkicfxhDEXoQltNB_55gpVbJn2w_s0Lk4IBJaEPA33lGHOuVP9ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=oCFwG-5D6wSfrMfR85LLRAkCyk4dftByQUchWEC5Z9whmB81kFoxvYcvfvZyYnX2M2A88hbFhgtc4_DL3RyN5qpHRl7DNMDl_Oc10SPuOpEsEWatLv6ipAvWJvVgI4Vw3H_ZFsfgrKaM8n6zfYuI5Hz4Z3CHXajvxt-2p15kTdjpgCJf7nn0hCaaMErCCup1XdWYhfuYNBoZI-WDvGCP9m-c6H88dLVDkJIIvPi5ZuIrnDwVPTPgyckqMPSbNcqPDIK7tIWEMC0JsPjlcGx4ESOWVEa5XGy5fQMc-WQsu2QEdrtEmLq6CAM3xcFmUd_-HY2k53A4_mL75d3rqaDNYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=oCFwG-5D6wSfrMfR85LLRAkCyk4dftByQUchWEC5Z9whmB81kFoxvYcvfvZyYnX2M2A88hbFhgtc4_DL3RyN5qpHRl7DNMDl_Oc10SPuOpEsEWatLv6ipAvWJvVgI4Vw3H_ZFsfgrKaM8n6zfYuI5Hz4Z3CHXajvxt-2p15kTdjpgCJf7nn0hCaaMErCCup1XdWYhfuYNBoZI-WDvGCP9m-c6H88dLVDkJIIvPi5ZuIrnDwVPTPgyckqMPSbNcqPDIK7tIWEMC0JsPjlcGx4ESOWVEa5XGy5fQMc-WQsu2QEdrtEmLq6CAM3xcFmUd_-HY2k53A4_mL75d3rqaDNYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hktN_3clOf3FklGPp4V5liIfXhYn4Dt26KTAs3sbg_cAVvD555BC3BlfW_UcUnYJfHVeLFVnOMXQPRxGiihs3d4uv6lXiSmnXlwTTHkTkQTdR-Mb-o1tHuK-WgoPpvssfQdT27FVpGEIAr9t_nrs0QlwhvsRXjFEj8ugnt7FkHDU46AZwkOX4kF7csof0hhK8YvUnEU79YgkUkvTVKBly1GUI7BToDSVaK5yFFEzIiRGdCn5dkK6Wye-t4aapzQiRWZld0RxCXtqWPfaSVhKuG-E7kglxZK3WOWiuLIk-vkK_zzP6zR8eGCWBmxAy_PBvpPNw9_aTIpURgt1YJUgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=vcNXb11aWAKMdyBYuE693n23vSLJQzaPa_0sfq6BlU8aTaXuDvUrMQjHHI_3DLzF8av5un6Kk0_x8Rgy8hXI4TXh4KG9G2fcn9MhZWHiGeL38KeCJiFizstC4dVRREJVFG9qksjTid1Wqt-HFpOMor9bNMufKiYuoasyLKCjBNlVo7BQsf_4VO9poQOfosQnnEIMj4pWL9gN1KZiCLp-S0aTCKdWghSpFNACmVVR2REzz6kzNCaZnZoReqjYNAclUGPBod5fS8Y02pbDkkBp8F5vuqjABhaTeFsNmHlGO5eZ5xByu2Fujr5uqii6SzLZIMlbcgS9GMtf4G6lP3T8H188WluteWKpbKcX-JOy4clKXp9QfSFuJM1b-49EANmH7a1ySczwEedRZDSeHrjgCR2Xt2otitF9HtFwdvSQzmcbMkVUMzEIt4U60zdjtOhsRfX9DzrmKtAZSJLxkLj9UDnSgKJOv-YPnNpPhyPwt9Q02f2UtUvdXkmqDUHHSurOCLiMBPHanWF3L3xSTIsYXcBkJhdSIVwSXsd0UlAHvwuUzwmLbjl7iMhc4K3cvIDyf3YOTraydtzu_RJ_44rXhEYd2tQ3s72xt_QXkDW2DqOvJynPpMy255MvQulZwMEV0ni6FoWg_WAI9VvEjKsu57U7Fcz7wsh3NNDm7hCVpk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=vcNXb11aWAKMdyBYuE693n23vSLJQzaPa_0sfq6BlU8aTaXuDvUrMQjHHI_3DLzF8av5un6Kk0_x8Rgy8hXI4TXh4KG9G2fcn9MhZWHiGeL38KeCJiFizstC4dVRREJVFG9qksjTid1Wqt-HFpOMor9bNMufKiYuoasyLKCjBNlVo7BQsf_4VO9poQOfosQnnEIMj4pWL9gN1KZiCLp-S0aTCKdWghSpFNACmVVR2REzz6kzNCaZnZoReqjYNAclUGPBod5fS8Y02pbDkkBp8F5vuqjABhaTeFsNmHlGO5eZ5xByu2Fujr5uqii6SzLZIMlbcgS9GMtf4G6lP3T8H188WluteWKpbKcX-JOy4clKXp9QfSFuJM1b-49EANmH7a1ySczwEedRZDSeHrjgCR2Xt2otitF9HtFwdvSQzmcbMkVUMzEIt4U60zdjtOhsRfX9DzrmKtAZSJLxkLj9UDnSgKJOv-YPnNpPhyPwt9Q02f2UtUvdXkmqDUHHSurOCLiMBPHanWF3L3xSTIsYXcBkJhdSIVwSXsd0UlAHvwuUzwmLbjl7iMhc4K3cvIDyf3YOTraydtzu_RJ_44rXhEYd2tQ3s72xt_QXkDW2DqOvJynPpMy255MvQulZwMEV0ni6FoWg_WAI9VvEjKsu57U7Fcz7wsh3NNDm7hCVpk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=uVXEV2zCsuZnJ3KHXo_RbVQDIx-ZNMaB-Q2mq-FRu0RbSE5exT_a-47KWHbs_IerVpkqu2BRpcUTYJ1zxnnueRHfOl76dbTE65j3AVPo9OxU7AuCypRLJBSgjhgM5CeJwiatcezzauzhgPT9JHRu2MG7nP0N2FRovSDLx1sqzFIUgKSg8WvLDshp4gXib7hdi3qXINStbV2d00-0vauz0GLGjWb2F4MM68IgDhcwChTe2j6DPcQn87C5QI2utwVbeoS-ZHyw6HsE88p30UVJwjZURR7avVKKK7hSn2V442yzqUpZGbwOw-1vjqAFGW3MFxjBbFbiZhtg8OY4r7V6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=uVXEV2zCsuZnJ3KHXo_RbVQDIx-ZNMaB-Q2mq-FRu0RbSE5exT_a-47KWHbs_IerVpkqu2BRpcUTYJ1zxnnueRHfOl76dbTE65j3AVPo9OxU7AuCypRLJBSgjhgM5CeJwiatcezzauzhgPT9JHRu2MG7nP0N2FRovSDLx1sqzFIUgKSg8WvLDshp4gXib7hdi3qXINStbV2d00-0vauz0GLGjWb2F4MM68IgDhcwChTe2j6DPcQn87C5QI2utwVbeoS-ZHyw6HsE88p30UVJwjZURR7avVKKK7hSn2V442yzqUpZGbwOw-1vjqAFGW3MFxjBbFbiZhtg8OY4r7V6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJdpJoMo901pCEFrQDNY_MyB4U8ABRmEru8wcaAJYrZgqF_RT7L6_Hb33gNDmaBQR4Nw6O7a_fs0NmCt2Q-p-nEUmooVff-TccnkhPbt8oaBiRM-lnNFgw7C5OcK92gInOsK7MX_RhHrqCX9Hm7ojOD8gmPiRKDdVxeFehkpCZKaMx4UtAqBEjMMXcJeiuJ3bmlZRc1Ji-akLri9EciP36u3NF5Sgqwn98AoIc-ucG4Uvnc8EqxBcmaVEXrrlmjH926ODmXXoj2JTCYL5BEdUECVK2Xy6xF3ATGlZChQk-DQtCKo6lPWw59vxpuCE3jYiRiq97KsSgR6ABysqY0Reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=g7bNriNWWElGesd2KzEXunyTFFyqYO7jUS-mujb69OQhmJY1WEDXggs8SlVjzr1mLwHI8RWeOtSRsReAlvXae4wQby_pZgtHKtZWu3lH8InSZOxmEH1V_fN7rhj6GTu1EWgTpOGlv_IqEvV0Nq9LGJjL-VOl6E6MopY4Q9pK6SfcYu6MokXkGyIezkGz_KlUOj9XKh-ZjXnKXYt13_YF7Wl566kxRCZDvJeXgFl8ViXfXYZ1F1QeIL6QlPdjsC30OPoPt4R8ZyCxzRNiGFJFKanECr2M6xkQsBZEvTJZaSDqIr_sZNlHnDQtqBM4x02MYX_zoccWpOm2pFs_WxoS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=g7bNriNWWElGesd2KzEXunyTFFyqYO7jUS-mujb69OQhmJY1WEDXggs8SlVjzr1mLwHI8RWeOtSRsReAlvXae4wQby_pZgtHKtZWu3lH8InSZOxmEH1V_fN7rhj6GTu1EWgTpOGlv_IqEvV0Nq9LGJjL-VOl6E6MopY4Q9pK6SfcYu6MokXkGyIezkGz_KlUOj9XKh-ZjXnKXYt13_YF7Wl566kxRCZDvJeXgFl8ViXfXYZ1F1QeIL6QlPdjsC30OPoPt4R8ZyCxzRNiGFJFKanECr2M6xkQsBZEvTJZaSDqIr_sZNlHnDQtqBM4x02MYX_zoccWpOm2pFs_WxoS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbY_7IoQrFDx0Isu9dM8QcyQXaKTaF4djGlPp18-bUVJ2gOxwivu3CX2Rs4IeL6upEfx8rLcarMUQBZNW_B4WDjmKo9p8gxonEAshKUeEBH6TdR1xtRC1EJOeG75SyWc4V5vs7n8LY5g3md6mjr-jKYWLb_YETQst7J7XllmDOrFpjPG1lFoiVPyQkbwonOm35YFwWosDvtNqu4kMb7uZ_xQZPWv7IN_efY2i_ZX3pBUN3hSyhfeIjIBo0YomUDP5jX_VSlssyWyR7DnLkd0sk_ly8jHxv9xV_5lADoM1yBiYwAP5RYmHoXZlgCOWBM9rVS-TA8YBiNuTKq96yGKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCpwnuJtIUDuTJ4kJIs1AUDeUug7VydLqvw9P9hpoqviLOnkdwMLqjiVrkpfrrasWsPz7nPJ3ZlU-lNwIedJysfROyRAu38wa46zKCnEwsR3S_eGGCkT4-ZzBNddsDbky_BSxck_WcDESTDZljpRRdYAdJn5CU_Kv43FmT67729nv7366NdDdLDarTGnXxE6qCu_8Dp_v6W0O2MqeqQqyldd1F7EAP0V4oSO8BdcpAGJeuAwV7dibBVXuCbBU0r58UIHYDcl-Sdz7zCsvIDzBrN8Ml9ochJUMc0Her7oqNwQSSdGmecw1qilWRiPIPHgEsm_cgXqZ1A3mPapEZjMmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5hrAV2WbzVvo5B_alKlV4y5gsQ7cH8Af705ORVO-mOHvnWqdG9ytxrQm42ZHc7bGEojoCT6Hv3b1lPGT_pN_457Lnu4K70sGMJq3u0NziLm2UYsbXQo6WhjtowOZgQF-eruppcc7RJ4I-VRTfAK3Mi9vX24pqp_gOkKon8lnuVVUa3FUKkyBM1h93ysDGjAAHgHg-Zx6_DZBkup5570Ocuux5XdhugvOjZsL0Du3DT7r1kclnT9U4BKrtNUgqVrkhRUcH3wHLtZmssRGnw7NWUB21mY_LQwWkpzEXg8B7euPvyY0hbyv04Dd5xSvss8guZSM7zFkLsO09lxDuKahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=dSxKZqTgkGfSC3VmKslCj_cOj9A92mzswVnUCIp-C6J9qwYQa_fmw5LhQLFDJrxGcht0znD3hHtkyNaxyD4S8gfVuPMXtnexNiKKLkTw5tUXD1-S2zHi2mJdgJArdKt354qe9Ojt_SIFSbTCMPoSp78Tf5RkJ-iF-Dm_ETQ51DPDo6NffOZe1qyb0T3FvFdNi9DsmfpukhTDWTREpd4WpsZoqJRfaypUSXih_Luri4Mpye-tAMw3TJ-W0Uc-IdJmJ2zMO2WhNfzYHNkzszqUA-i56_jnv6vuv2G1f3j7sgAP8Tc-yzSyfc4dmGFXNDkusJKCmaXuntYEpPcpkV4dJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=dSxKZqTgkGfSC3VmKslCj_cOj9A92mzswVnUCIp-C6J9qwYQa_fmw5LhQLFDJrxGcht0znD3hHtkyNaxyD4S8gfVuPMXtnexNiKKLkTw5tUXD1-S2zHi2mJdgJArdKt354qe9Ojt_SIFSbTCMPoSp78Tf5RkJ-iF-Dm_ETQ51DPDo6NffOZe1qyb0T3FvFdNi9DsmfpukhTDWTREpd4WpsZoqJRfaypUSXih_Luri4Mpye-tAMw3TJ-W0Uc-IdJmJ2zMO2WhNfzYHNkzszqUA-i56_jnv6vuv2G1f3j7sgAP8Tc-yzSyfc4dmGFXNDkusJKCmaXuntYEpPcpkV4dJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=I7AqUbZpAGyTzA82h_jrTGpvD-X6NKi2PLrS0tRTJcIRmHejgAnOjxscNrpbx5aHoAPkJ_c8CUds9aPcVC-sajpKBU550nrgj6NAfxxwTa8thBy20MrnpRD80wv_cnxNLYaCc77w0Skxme8I9gycRNguFL2Qc4lhs-mR8mpTI7ghsrOwSok9o855ZxrBuOxs7KhBxCXPysR_YkZ3w6bjXpre0B7tCfH_sf4weW8dIGs73vh4SF_t-D2lDxvIWCWMfjo0LrdQFwmfnC-aaaoXmdSbDUf-elKGF194BJglZPedT_h5aRjXGKqy2ZeNIB5__C4AR7t0Zk0JBk1T_Go2EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=I7AqUbZpAGyTzA82h_jrTGpvD-X6NKi2PLrS0tRTJcIRmHejgAnOjxscNrpbx5aHoAPkJ_c8CUds9aPcVC-sajpKBU550nrgj6NAfxxwTa8thBy20MrnpRD80wv_cnxNLYaCc77w0Skxme8I9gycRNguFL2Qc4lhs-mR8mpTI7ghsrOwSok9o855ZxrBuOxs7KhBxCXPysR_YkZ3w6bjXpre0B7tCfH_sf4weW8dIGs73vh4SF_t-D2lDxvIWCWMfjo0LrdQFwmfnC-aaaoXmdSbDUf-elKGF194BJglZPedT_h5aRjXGKqy2ZeNIB5__C4AR7t0Zk0JBk1T_Go2EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv8vTa5y8kPu9BUkHcAtxVg2D7jdeX070NPFCbZv0FLX3z_fe2XVfHTxikUep8Ym3LmwlR0SDolVe1LggwJBGcCnOuOa9r0x0ScPImUPJ50EL6BZ-vPVwLx0y78pO4JYYn0V48csbHsAQW8QhiXEATnY9jXk23CZpZSh82hcIYpH9PhTOgYSv5-Tz1Sl_cCqDpIULBzsy742E2BPh8PNmE0-4KrapvRhix3xtOYfpSTZlc7blUG32rt7QE61E2lH7-kmujRFSYFiMvqsLVyxHURJorhfejWXDlLrZPaQilMnWRdY5g8cgxsuH7d4ctIq4AWRnuDVRRrMEla6U0QFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGv9SAE-fw6kBtEibD-yr48u0lXXmBczXNOB2e64VQphpwx829Iza-FeGKa5TjegXbOH846vE4beeRihMb3jjcmYLXUi-tdEjCaQD4WVDqcBPUjLxIArZ2XV8cFYairQ2Ii6SOg_MTAqR33AvRLAt223HdWxkV_Tnh1ZIUw35aAK6OvDJ97sEpvp1L70GpGTQ-XS5q8moUV6EA3DeR2tP1k_Of_x8DzeMIkQsrmejHdMazguHVBWdpifgsj5yA9GJPNebSuhDTLStbGaTT7LmQkqWCigD303lKLukQuJJavvrESpaNUKgkuz46ZxrVoDe6I27uvUEhi9O5-6esZYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hT4f81bt3xVYL30b0HNjnKyxoPzQlzfF3vUi0VrvGUzFMwPG7BkvCUuonqPudqZ5irWy0N4vMe-zStIC3nygof_KntMGo6lpMlg3mgd0mKghP6rf3r0ghYFpH3opt3Gjr23NWmMs6SF5pOgf-ZtXuytWcbQ8hzXt8Bctn1nn1eQvTSQhoaj8yZEP3nUZRMa7JP3_wnTWAiBxrPQi43ofajn3Oit1hXUfnYZD_ZA2ZThb0NBUl4gy3AhaZAosbAOAFB-KpZxsarW052305nEPX4q2h7jqbFQhQZ2KlFoPPX5IiMElgxBfc0xuqC0qLM2_zZZTpa8Acfr3toCANVwiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLr0WnkPBVXb5hutfiKtvF_xGuxDNe4y81HfiumcgKWxsbJy2PmTiNbKS5l_hTeVL7fuvB-TiQ8pUi9O-p2NTJQtgUf2QJlnsVfAPCIEeYufuSYF-EddjzaYbWGBqhlw8PqpwoUqMb18gGO__UiZ9z8jtDCQe7uTIq85DEOcdQy6CNCwkcH-5gpnouujprZtGjXXU5gDC1rvA-GDnHXF2X4QzE6TSVXVKv5HM9DVzjFD4coBBZZsuZEonvehsxTAcZL4c0LaHHinuqB7CNiBqbtoOaot6Qlwx_2cQWCAXgaXKGjJ_vMb3Rpe-PfGw5YwNd9VowhZR0mxqrfr2cIAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmsdpsQm9LOnWLOaQIJ2NgBPVT5i5nPoLviLBwBjtBgvi-Ol7VBPp1jnFWFUYlbCyIhqiF9Hbd5NqfTxluZQBBPFg8J8E0E8nkHyS6DSEB5A-V5W9OUEqVyvafBldYJzbmRvg06rg7592IkAbVCQlJG1KlRn3Qxvf7k_a84eLD0BIygavJfKs5Fp98npQ4A7Lx_SNQfjB-zYhQfKlqtZ9fFSOZUQtHjn6BUJl0qLxb8fJu47j3GvXgalpMGvselaHi0bo94ajLkRiC3hHt7G8y4jOtvi55LYbvJ2DcBRyLZ4l84WWk-DUHg_rLcoDFYmFz8bN06zy2gq7tKKYuw81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eISMkQILSC0kGdsc8bB7xT_YBnTHVzsmIAAVcarCE6nJSLM-mxUftLQYlOWPp6vqaeweIEpWP1zGwuACE6UfTeWLyduimn3JKgloPjZMSvOCEzRlVJx39SgaaA0NEPWWYsfi5wDXVNFD51saAwRl5-LIB-OuXJOHYLI5-YaRJw_So_P2juGbjRl6DghSBKJIvFm6qOyprEywqJLxEgA51cZLq33OSk5fvd7-BQ8m9kB1CrCDDxyL659jbLYS-771facKZ1hJDvcSKiiEChKzvWcV8kk-Sh-W9iXxNXfoVF8lwBBycAAIG5zSLmZsMz3e3kmV3l0KBTIQ3Z_awRH_Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crQw1j9k7ioS6X3sL6sePsQOF35PHZQTiJ76aEriypKbmPo8baGjusalvuL1y2tyg2py-2VXNWgkZVX1VSM5ISpkR6A8hbDFg80FG6Fc3hlc334H-toJljlND7BWlA2AIA7hQGyGqteGVmV8aEGkzITy9_ZiNv6L0eYuogIlYcbvZUJA-Ed2WZgjV5lVB8d36wLDWSzsi2ryjBFGnbrIcnNz39PXJGf54yYteFajJLTBXmbfiQMsstZYr6sQboV7tMwU602NwQrwUIMJ1NjcYndH2pYg5h7B8zv8Cti8eMqSxwDCY1o8q4G_h4qVXE5Rqza1k2WLCDbdIqWMaMLAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDmxyJFXZdVecQv0POFfrBcP2HAtclmtxIC5U9g-v7-d6yx_VNrV4qOipmz1ExH_ajLGdP8dOzwHZQ8z_BK_7uSEziujvAzlsnvGgEQWPRRP30h9nD8nXNPwkrFfBVRaZqtqbkMjLnPVz4_ypUli-voY7vY2DfmQtAYaeuNZspaOhtJsU1brnU_2-Pu5pVch7FoyNxCQbcN05KAdLOc7Rn-_vP7PXjioiY5meqLKAkUzEQed3N2ChzuuJj5qkU0oGd8a2-OOFSae_vaekJ3rB_CNBi2nCfkZ2sEJk8tAMFovHRFDiRBZbufDFtiikBbo-X7jJ0RtKygKGZVlnCPoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAj5nbilxv3vkubHho6poKZgYKdB7vq9mxvuA8hApMthMbIzy_du5VXInjTOJW40n6zk2ATCXpU2NhGNmYl2NhPjH78cwGw0wArnJfnWeWD5OtRnSitaWedn5HVR58UeSM2fvQBGfCbmV8sKUFdxk1TWHU8DY1lsRsdGSe_9DLkRqg3nNUDYMm6hM0DdAEiR9pbbDECit3nOZr23S2l16BCp2nmwrjxRR_NpuGGSHib9z2gLASL9Myq_czYJampZBTK3gMt4aqTXelr16MgT9HJIIS-TPPNlP7mMAuq5ULh8j_IzJ1Bu_qsd9waKv_5aONZ6EkWEafb3G7Nk3OA1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MilztJ9k-ShR7qR0ItCQXcwjRDQGCrnQjqbwUguJPK-kdKk2bDbLvRW1M4igh1RWEH0f_R4Tp31hxOIaYpxHISmfin4Q3eS1adiFxccmdC8Hzdak99bzoBQvTuigbcHnzanwni_btLBy3sfQzPY2x6eogVvOg4ZWZ1P3yJOpgC54HfbbGGa7mc0xkFWd-nraw8tvmYYqirgXSO0KjrfK26ZfoD38-CLGZywNvN5YwAdLO1eNd__Jr-GQTuWjjQLy-LMu48OAjLeVEUSJxExDS7o3I1CIqpivHL_IC400gtL67WdZUrdx3JP5C-eKq8CUgi69Q6rGHaGuFVciVwd7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4eAoIZZH1BghvEmTHbnPAWipOzTpQTb9GRuSXURs-lW1_Q1xeRN_eTLT8S-ApOO_UbcLLjypfGhvMEjztfF9vkTsvxG4Yx6Hx0Zo-vfnzrvn8tkWl51JafKhvn0txjCHMmUWuwiy1PtoCNgFUQD-q1toeOOJlz5AVhW1UZ_-JyzQxivSuOgGiEyDJCmEehn39o3i4qSzowet9taYPPxSG_7bqQR0tpl1Mpm9bFF-PRzXqv_lOBPna8DBrlfZXNlEeNTLi2eisHB-FXcBaYsD2Th1IYTMR5CLLWWbnGtCYlKoWyODPXzx0FqHjI4zw6lrHV3WZuhBigTSfr8Ou1ROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVkF-w-dENP5mJWed7trRJ8XSL81A-7vbVDU8iG75dVdP9yNyXMFdi-k6p73cWHf6wjNk0eQOJWB-QvSCyxaCHkJFp97qNqHkFiKko9pDrT7lj4BH4cgDFfchjX7yZmQB9woqEDhpBLPjjkzu_7hDDZMqFbXexKkUVdoH3-2NobOuVo6qUAr4WqlbAB9_yM_lNGxDq3058aX6nMI6C3tjqpfp_EgXTgKGkVXeNwjemsda1YI5RetsLWiMf-fDL7H0L_LYqhVJ_YH5Xb1DIHZzdFp3YdrjzEf4YET25sicl28DocLT-ZGmMmGn1ndYE6incD2sqpLRjcjsnnm-OBNeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGmSw2TprPSQD0eMj6-MgFM9d4ySu2eXtBBHvTFqPzJsY6FQS-3GYfBUp9cM7LhxoN1G8vrBZWo5vy8lKHoMaU9OGEx5eRl3upKE3e0srnf5ueEZpOnce5d8bbf5IiojTUO7n4PEPHSzDCzMUf_5zYaO7Ef2PbeBDGbigk7V0Dj7wFgzVqhkzeu7HENqibCWrJvD8qOz6H8lmUTNqh1cbtScHodDOI3xIMXnFeZ47yVd06UMp4PV2YpWeYt6MgdWtfTxjCUkK9Ri4_cH7DqGAF3TvkRuQJb-rbkNo04TZrnFW3WH_T_Wt_5HwODWXTzS_ot0UHr9nZafI5D7Q_GxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=D4Ndv_FBRHxDsCRYAk69Y9zvXwZ-sJxg_N2Bjm9B13RZvhqegxp2_0cVADK18I60cQiPEQJNVy9L_KurN5frVPcRA3aPnvPN2_97R5QBkmWDsggM7JHpDZRPkZ7RJ8yv7MuTD-ml1N2zNVzzwWmUUUQcphJH1JPmqfH0ZSKu75-8cPKOQyeoShu7Kb8dt1wLWGfzmlXwSdt7DUgVPwtAyv63Z3RRHGGWo72ByexOYzEP7sC4_pt8CLWz1uC8JH0DvUmYWnC2RFvyGO-NnozfCJxEJIiUHr1Pr408enQHVN53YOxmHcnaQO1mdVowUpZnMJGZ2ChMBbKkeablg-0GbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=D4Ndv_FBRHxDsCRYAk69Y9zvXwZ-sJxg_N2Bjm9B13RZvhqegxp2_0cVADK18I60cQiPEQJNVy9L_KurN5frVPcRA3aPnvPN2_97R5QBkmWDsggM7JHpDZRPkZ7RJ8yv7MuTD-ml1N2zNVzzwWmUUUQcphJH1JPmqfH0ZSKu75-8cPKOQyeoShu7Kb8dt1wLWGfzmlXwSdt7DUgVPwtAyv63Z3RRHGGWo72ByexOYzEP7sC4_pt8CLWz1uC8JH0DvUmYWnC2RFvyGO-NnozfCJxEJIiUHr1Pr408enQHVN53YOxmHcnaQO1mdVowUpZnMJGZ2ChMBbKkeablg-0GbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
