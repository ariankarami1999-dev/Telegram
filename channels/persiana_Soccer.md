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
<p>@persiana_Soccer • 👥 439K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-30681">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZGpV6dKE7ALndG9hEuNnBSOLN8ZX6GzSGFRF2QX6QPUmAQW15HcCIcgwEAY06mn5AO2rXLMReaflT5oiWFKWEAXFZT-DG-WDUB7pe-KQcwcULqxsAOYU1SV5bD8OYz5w51AHxpYlwk_qnFAv20qlxkqef1JYdx77c1844CDxydMKvYC7RpSV7P00Nzi74spf8pmmf-1_oyhGK07_vk9jNk56zFu29eXMju8IllAkScRsoPjnF24pCwppSveP_f_Rt0LHkckTyax-ZyNvqYPOy3m-hZom8MGmgnK0scXhuItwpirnk-ZQ-u7uwt8jxKlHFzQyNWvNhVNU5SY6d42JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/persiana_Soccer/30681" target="_blank">📅 18:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30680">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKny-cjtOHc4X1--BcqEHlBs27Bi79pfKSIa_N5dSxDu7lAo0mzBBJiLGjeb6EkTetPGVC6hDaAYaO0g-mAFddt7Iu2fnDAT2CbKpVNTLVkmJyu_hDxxEH5iPFLvsA5RthGREvjmuLYg9KMfxKN9iLKHXqU7_-KP8oeoiKfEXv4pJ2gcAwzOJiy3bkEI81UYL4p6z3dgZFt1HojVUheUls3BHFyF-g5rBzx8bvjLw92OXqykv-SWBZp1eSyfeKLYKyiW_DFSrbB8VcuXMXo2AfXC5jIhgpRR9uZvJtQAybX_Ey1xV3ysn_WiPsWMGVIJAcG0VRxNbF6OitZ3EChjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم فیفادی؛
ترکیب تیم ملی ایران برای دیدار دوستانه امشب مقابل روسیه؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/30680" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-llfwoRKibYtMVx5UecwAP4RALeBkzA2LXP8quZr07x4EJ99Amvkn_yFb5_YRH16Cc_ACRrer9Oocf1TGX0owklR-l-AA18lyC-OqgMbU34qYZAd7aO4Xq0lITs1ORAvAaC2AbTFTL0EFwqy3j6dyhaFc3QH0BcC9bNjVfR7seJtjMSexYuJJ7mJy29vbZ-VMUprQOAoULBMMNeKvxHR0ApN6qA_KLmL_eVuSxfeEMO0D5wBqdb7dF2Al39cAmBcKixF8OByxyFA6TVhvlu_qVSHlL0cTkmv2_IqCLT2QEYjGPtJIh-eVsmkxQukWG50ScZ7o5PxMjKP7DAL3cbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAJRt8b5KbkimJsFo8b7l-jICKQNlTCFap_ppOVlICx7EW2OBKbu0_rSg5H8KpHKKdMVR2CTKPaSkn6M_gbqRToQjUmxztpvdgPFfibd0FzwB4oCS1WjUrN_WY3_s9ncX6vgrBhrpo_dudlHMZRyp1FT7WkkrJpnPEUU_-a5bI5nhHtE0c3qkegeNtkBvzpqgABTH6-y-9v6a362Y0RhAfQTwf6d041dMHvlVtcACQMbJBQ4hE-JEMFZps_nEhuXZ9yj3qLxC1gPXaisWP7FnC9yQLIOPyEu4OrINbnuEQfO5jdtRA7hQfy0jhOnYxUejLCXqXZ7qGiBjC8b-BnUTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/30678" target="_blank">📅 18:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30677">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/30677" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/30676" target="_blank">📅 17:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
قسمت اول اتفاقات بامزه فوتبال ایران با اجرای امیر مهدی ژوله بعنوان جانشین ابوطالب حسینی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/30675" target="_blank">📅 16:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGkVKWMsWct_ZgODx_VWSGh2hD8Qv6VvjHGDbJKtofD1jio48OgYH8DvrJwnZAoFWhwsIuA4Br2Cvy2RWNOoNFJ2O4RlO4wqfF3QrHYIRP5c_VKKnj7b8x86UpcOn6pfMyYLNxLilRzVNtWMNW_bi_vf9Vf_wDRSb3cu8mGzuO8yVfVMBYFCpEAiMlK-1rIJHfOTc3rxtA7-01mKseDZ2ex0qdJ1NXHuPnOTKpY8fkm9GB_MgPfugrRFvNwsKXqBc0-3AGjitDa03QoTienfgJ7fGf5HN8TUXrrCj9wbBX7UT1dvE_3CUx8nDQoWyGhEcoHS7k5lKj5xpHrmnziulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/30674" target="_blank">📅 16:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNfNhREIXED4GvXZFB1Wo8xhnwN5nZnkQef9VHuBuA7_oBgNCrkKENhBTTiHFGdBz39huOCMeNsj5_aCP8hcX0W6yeqUaJhaolgpGnAjyA5i47ORhsiHLa4-1GQYU7p6EjG3ycJ6cMHMK2MeqvRWIUvTnII5Xecb-OPM21zG2z70hyaPAlqPzGB-xhEbiNY6UZ4BQLhLoMHN1UNzzAKVp5cHINKc1Iiu449Jh2XT318ki_TDxjyHIwm1o8J2buoeEOGSH0ed08lcJBueOp0h2mQGy2kneIvQ-jaI18No9sQHOpkqJD0SpGzbiwYf_BiOO1IW2WEtHM1X6oQLzGpuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/30673" target="_blank">📅 16:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF-gI_r3kBSHI96aW-mbe9Axl629K3gL0Gi93k4g3gZIOG2caH4qLX6j7hGpZdhTush5lxHjVsVVWlGF_TIySh-38-LdRBOGiF8ryCHRQS2Irp2KXvUIYy4Z8uiQyNRhiVZjt1XfQuX39ab2XlmFDfY6SzSCvbu0tWzZMv2gsH8lkB2sNUBUOSw4LlliJxR6Z__cZc3eElYZ33I287FMjhY6Z95i_Jo9pKptC6N8_DVh4vUE2NfPmtEwVm9WVgwMFp6E0gBkSMoDpqENZnRJuo_SwxZdmxC6o_PCSGCUYmS9q_teegJ9oCDBg_2Dm9rSkO3zgzqEPirgKm78DNxZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علیرضا بیرانوند دروازه‌بان‌ملی‌پوش تراکتور: با کسری‌هایی‌ که گرفته‌ام کل سربازی من پنج ماه است و احتمال زیاد به فجر نخواهم رفت و در همان تبریز به‌پادگان خواهم‌رفت و با تراکتور تمرین خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30672" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEm0zFm43HnrG7tGcsfksSW60dM54pOYqpFd8lwuD3_s27S2jfPdxE2v_BzUdeWkS5_l2OJYcGq5KcyjVQZdcLm5cdEZaMWYduUbu_oPdh1lhBQOXUf1TQ61CD7r9uPbMTRCJ4T0DQuLG8ycSB4y2HD9wp5KJYaOvawxJC9e5pdAd5AzbqVcl_tnwwfCgif7I-2pzk6pPOBTzoyULbeiqMkrChpLiZuV2YdtnTGn5Ob5NGx5_Y6TaK3HtnVb_GWoYW5NLL2Acdn_5YlX7bWd7n9cgtN2a-rpqlFMuwDm2w4bCkfkuG1xjJuOCL9O_6B1id67ejKyL9g1l0pzzlOQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ باشگاه استقلال از روز گذشته تماس‌های خود را با ایجنت یوسف مزرعه ستاره جوان تیم فولاد خوزستان مجددا آغاز کرده و قصد داره این بازیکن رو نیم فصل آبی پوش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30671" target="_blank">📅 16:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6x5i6FoYpcPCjLln5j64keiOvdFeVjutKYT4ZjcgJSDW-Eev3TqgGky2Lwbh8FRy7UU3yJTN-FBnjbr1G2eHDll7z65s62cpzDy582VIRMs8pDeT4cLXvbn5siXVxbBVEvqmqTJAvWla8S2-7JGK4dDm4WjCTzA3x_TWAh8utbn-NEcUPCPXYYGlFglwe0MwLa7Lwpu3yvH4gi-R9DzMeohjQd9ssEgveM8DA6MMefTSuNrCk5jz-zdLNZSyGriJIQx1cyuivCqM2hFFfk-vcR3VA8jOfznz7buhmp3kbibnKLJ5nNuBaT7pWmB9yHmDAfr8zwxzKuHCsAv3gQmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد درخشان‌رافینیادیازستاره‌برزیلی بارسا در این فصل در تمام رقابت‌ها؛ 15 گل زده و 4 پاس گل؛ دربازی امروز برزیل هم به دلیل درد عضلانی تعویض شد و بزودی‌میزان مصدومیت او نیز مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/30670" target="_blank">📅 15:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APD2MmHtwqazxcFgyjEUoqTvzcMkQegMIztVBy-qWSu7Uro6X1_SByWuLWkqCo2YbFpjD4auaEqy-eJmwywCpYtnZK5H1NIPChZpX9KdJ7Seu_hGlMSQBqgeIrRhfufYe5XwIwTehAL8HFMvgIICQ25c3jMBE2omJOKXgWbbXL7GDNa0PxVwBFZOfHvhBrEYyo5OecNBmgvGbTukmEBdEKsz-tCPtJc1rF0asiLS0nvF8afX8wRCjFqCOulvZSVGMlX4bTnxkQfGkf3gTdsLm9EWTQzubbMkOO89_OY3hdVzzDqu6tY2kXo3jbVntOiwnTx0TN0IJtMY9xqZdU8-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
تیم ملی امروز در هفته دوم فیفادی برای دومین مرتبه پیاپی امروز ساعت 13:30 به مصاف تیم ملی استرالیامیره. بازی‌اول بزور مقابل کانگوروها مساوی گرفتند. امروز بااین ترکیب به مصاف استرالیا میرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/30669" target="_blank">📅 15:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmFBINKOgV-Cti53k3NFIriy8wAAz2JOpCxj1KmJk7ifxUdJTCA4FVR5Y6oLlGVR2JdQztA04P0FEwF5KM59WuvgpWITbM1lK7PI2GV3QUafnUHrBiTEoDUpvVvOGL1ywhvlpiJtElT0PJpBaFNzPOW8Jlo1C_UXcjbktUJVRqC6VioRyl72NcdctetUCejUTCu66yMdZ7n1D6HeYZqMQkVsr3qbVKU48h9-WbLVzwXGLw7cIHOblUikzYgkAL-63m4xiHTAPxqvpI3JcwfMru0dMtlDc-qLQqUQFgPujPGKdE1L6NSDO0MioKqf_9EYbZum4o8r5fVIChoE8sgxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت‌مربی‌ای که ۳ تا چمپیونزلیگ پیاپی برده وقتی روی نیمکت تیم‌ملی کشورش نشسته و تیمش دقیقه ۸۸ تونورمنت‌کم‌اهمیت لیگ ملت‌ها گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30668" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVkmLqkYaNDmLFA8XFj3esxcLl5CGd5RlGJ8kQm2PZvQfMuoTfF4grjtBYiDEy6KcSZbb9kUz1d3l_uDmhsU-AgrauX_qam4A6S76qX7JjRSR5jP-96673hLeeCt24WsXOKC-rTOOIUFQBNLf5k1R5t2ZckxZkqQNHRgHbRAFKOVbxvlRrz1JWPdn5GQFinnThE_TDvMGJOjao_I8MTq1UDRUENNNqXP9mibhgOxupQ4dxISdxZMV4oSA4Ec8eze56B-OB-CNBtiTkJs0GkpW3tQmCJv3Eandh_DDz7ZzJro80xPtJA9IGWPNkGEdkP5ylJQHb6lwmwunnMUZpCdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سه خوشحالی‌تاریخی و به یاد ماندنی زین الدین زیدان سرمربی تیم‌ملی فرانسه و سابق رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30667" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
ویدیوکامل‌ویژه برنامه شب‌گذشته عادل و برسی اتفاقا اخیر فوتبال ایران با حضور یاسر آسانی ستاره استقلال و دانیال اسماعیلی فر و شهریار مغانلو دو ستاره باشگاه تراکتور؛ اینم یجایی سیوش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/30666" target="_blank">📅 14:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
ویدیوکامل قسمت‌دوم برنامه فان و بسیار جذاب ابوطالب حسینی؛ عالیه حتما ببینید فقط رفقا یجایی سیوش کنید بعد از 24 ساعت این پست پاک میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/30665" target="_blank">📅 14:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGC1E_dg7hWv4Jq-3d-YDxg2zRahmx79s2Kub_5GWPN7vIqs5XUyXPtOKOR-xj8S_HNaR9Nu0dTVMz7ya9Y4MIu1QM7jaJUsxsQ8ewn8mRgWgptf-2EkKBHuZGSIu_eLtakPmhLZh0gGZE3jVt-TbIBRY4VmdMXGAz9ajJKf3vkde7w6OQBL7hHcwMb3FxettZegwG891NVLbkoaszb05jE9y0f3NvS5QIE-Xt1Xx8DaqwPQqbv9Wwa3Mw3gpUUl4AIQQD4lZdjfwhjB_39ZQxGQB1-TqrFs1BJ4qssumk4QICnD680FR3B_YszLiTIEoJEwBxr6xJ6yeJTf6LzOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/30664" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=lnomhkz36G_UloTpuH7tMrddzSwwndDbzVKxdrYEcNwAQy9EjM8E29sdMqoMfZ0vQK_TH9L4MmVPzkBbfD0sLhzQhA2ku_gYrL74HcQgsx9oy1GghMmbG8kRCadTyjmfdKW4KxiT125ieDgglXBUuprLMt6iF5M0CwgrMUzfgooOdQb9T-_MOtYeuyPHRWA_Kkosi_QRv8EnO8Mx948erO6v9UV-NAeO7cDpejFpcKRwZ9UJTtV9yHjqKxIAlfju_4ThClASLakMKUUx9G4dDcz1uh1d4wk2hENKoRgaXLNynjgWrAlagw6TOO55xLNUr1J6pVW8yAIvT3GewMeyJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eae5a635.mp4?token=lnomhkz36G_UloTpuH7tMrddzSwwndDbzVKxdrYEcNwAQy9EjM8E29sdMqoMfZ0vQK_TH9L4MmVPzkBbfD0sLhzQhA2ku_gYrL74HcQgsx9oy1GghMmbG8kRCadTyjmfdKW4KxiT125ieDgglXBUuprLMt6iF5M0CwgrMUzfgooOdQb9T-_MOtYeuyPHRWA_Kkosi_QRv8EnO8Mx948erO6v9UV-NAeO7cDpejFpcKRwZ9UJTtV9yHjqKxIAlfju_4ThClASLakMKUUx9G4dDcz1uh1d4wk2hENKoRgaXLNynjgWrAlagw6TOO55xLNUr1J6pVW8yAIvT3GewMeyJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30663" target="_blank">📅 12:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzhLRyo-WgR9wF6hgf6NiQQSPxCST4QGK_yxviJVjl10HwxEkAkj6pBG5lw15bvJwlWRiSriO48TMgaFRz-p7j7GHwHBg7LeB-APAVrMikI914Lon4BWpAWufDRgxvRXGrxvCzmm3_wb_IaEmit951BTJI1IdgNxLPY7HfOtMGf21tkeRjs0M2b9rPlQ8kmisfFO_weR81dIjOaYBZdqVW6vnaOXYe5ErAFR42hkavp1tO-MfEljOKFRQiWKxn3ZgGNt3yCuOpizJTXHPx0tW8jqFHBcT6n6OAgVF4AN1AXUjBKZmgAHjCO8dT9uTzUsQQptJRBGS0QwmnHGW0iOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30662" target="_blank">📅 12:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30661">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/30661" target="_blank">📅 12:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNH_S6IcCbnSpxtk5ZQWdbgI7iH3STGvmZXFX4V7TlpWHBrlg1iMfGuZykkD_TvXxJRV-YLu7gvnStrzec5whycKkjSVZXiS0uqac5QYaZgrMCTimCFZh9CNI1z2daRO3drPchaJm3lfE1qYn_PkHn8rlGMJ6j7gfH5xE3Qu2Hv5ArrNhbKxoYdHfTnt-SOqlLM6nQb9EGQZnqHZQRkRWsHW4S4IfKHf1eiRN84K6ob5h6AEf-8B_nqLEsWRzh3x1TJ-v91HiFZFhOFfywmsW15usttMuMAyT8SjlfBfKM4viM55Oqi0XAy5H4oLFAl2WqGIb7GkeyeuAMqugQZJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علوی سخنگوی فدراسیون فوتبال: از سوی چند باشگاه لیگ‌ برتری پیشنهادشده‌که جام قهرمانی فصل گذشته لیگ برتر رو به شهدای میناب تقدیم کنیم. به زودی در این باره تصمیم نهایی رو خواهیم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30660" target="_blank">📅 11:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30658">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQbyURrMG_UQBw0GT2IactvEwJGuDSiEyVafWD5M6Vk8Xu_gyKX6VlYIqyXa3U97SAs5Cr9RYSzgygWYhFZN1XlEbyPkDyYNaKMfZ8ShrhQvCBqx5f1S4Gycbk7zMtLrCeBHRI4tD496J-RJy5A6YWElDnVcBWP5AQlsg5FLYErwhKso7T9IyKuU9SHtnsnFXB9gVgmKoJH6ahrVSEE1kq4a994BKNkNnY3wh2_-rBRyVhWdmS7xgjbQhdkY_aQtqCHbmRJiyr9e7hiTMzEXc_68QNGaUQnrr-rkSnEIH5szHuSBFw7J2xdEG02-U0rHKu_R8TZpiMp37Qs_GGQ_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زیدان درباره خوشحالیش: دیدم اولیسه چند تا دریبل زد و باخودم‌گفتم الان گل میزنه. به گل زدنش ایمان داشتم و وقتی گل زد، خیلی خوشحال شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30658" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30657">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=szKR9roAXrGJy0ahB81prg8OiS9ezo6Vl6EKoqnSJ4ynx20SZKYiZhoWigTg62pDQwTu9zXHAHvUWL0yeomyzLTMYmgMyjVWveFZ3QUwpCGNm3bEJCJm5B1cor2qpa1MIDNAMF0m-hO-ZKGdLW3AwSANgugTyYkz7KJ03hdvgSAoxg9pMhYdOYb4J7cEYdOLhCaLG6SENZoJhU2eHbALQ_zRjPjeZk53bsws4GmNZ1ZR47BBZi1tXCLnD69a7Q5oYGIleWu8oECrjC7G3yi54REhHUxTsqUB8e23UgvU5sPZtU7lL_LbMgGurnrt6nm3ilcrnx78boUibxB8HWYAaDT3XoPExrOomw2lWXylj18_SlNWKIElwX6BnWIrvFTm3Ri03dYgC8XmH1uAiCIbNbmyuaV8-pijPZLoYJ_0cEBAbf5FYjWAw8cV2si4xSmp2j-7z_UpFW0KE7k0Ki7abtPO11hJzDrTWk1iMag9Vmkj-7Nki-iXQIauYMdinRJC-R7pvV0VbufBho_zutpg8R_9dUAh3YWXzCg5Q0Qy1ZQeM7cOQKiYSqcIxxYpkbczTKVo4OfF9xVnCYHT1g_qy4SnBvWbbJatgeOASof1D7oAGXarVflcuPeefqDPAQxZsNLyE1xjkZA17r6BlS4s1hI62lyObLki6txj-2GWDuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eedffb2b4a.mp4?token=szKR9roAXrGJy0ahB81prg8OiS9ezo6Vl6EKoqnSJ4ynx20SZKYiZhoWigTg62pDQwTu9zXHAHvUWL0yeomyzLTMYmgMyjVWveFZ3QUwpCGNm3bEJCJm5B1cor2qpa1MIDNAMF0m-hO-ZKGdLW3AwSANgugTyYkz7KJ03hdvgSAoxg9pMhYdOYb4J7cEYdOLhCaLG6SENZoJhU2eHbALQ_zRjPjeZk53bsws4GmNZ1ZR47BBZi1tXCLnD69a7Q5oYGIleWu8oECrjC7G3yi54REhHUxTsqUB8e23UgvU5sPZtU7lL_LbMgGurnrt6nm3ilcrnx78boUibxB8HWYAaDT3XoPExrOomw2lWXylj18_SlNWKIElwX6BnWIrvFTm3Ri03dYgC8XmH1uAiCIbNbmyuaV8-pijPZLoYJ_0cEBAbf5FYjWAw8cV2si4xSmp2j-7z_UpFW0KE7k0Ki7abtPO11hJzDrTWk1iMag9Vmkj-7Nki-iXQIauYMdinRJC-R7pvV0VbufBho_zutpg8R_9dUAh3YWXzCg5Q0Qy1ZQeM7cOQKiYSqcIxxYpkbczTKVo4OfF9xVnCYHT1g_qy4SnBvWbbJatgeOASof1D7oAGXarVflcuPeefqDPAQxZsNLyE1xjkZA17r6BlS4s1hI62lyObLki6txj-2GWDuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌ابوطالب‌حسینی در قسمت جدید برنامه اش به علیرضا بیرانوند گلر سرباز تراکتور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/30657" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30656">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/30656" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30655">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/30655" target="_blank">📅 11:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30654">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmKaj14Ctp3bkHrHAXz-2uOzgOIVyDnRd3JGJFnMPe5mEb0tB78OBFTwmZfnSkOvTwZCWZ4ySc1KhjXhnKF0AgjRkltG3N_ve2u0JV9Q5KBVAWdHFJIBbn8kXAAjbpsAQTFh1FDUWP-FeaeOvLP7ifKZnonAmsZHs8zfHB6E2pp3ImuBA0C8q-HtA-ybXpN75MdE9j9EWMSVS3sAYpo6alkXHYtxtKIY-Qfjq3h9bUIp6NBXNXvXZVoADuKwuy3mlneyop4g2DFEm2rzKCP5GcgYTZgy-VNxdqpJj4XSm0nZqXQDFK-1HZA-tdGlEIrTOq06zoHw0xN9nStkdK10_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30654" target="_blank">📅 10:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30653">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_edgTfAHjTT_iK3RhmsSytOi9sjVShZk7rvlVkHOqWxAeWPGimrwL9k5-g9tsb_EQhs2aZWiY2LuK_PINzSVJWT_uY5uTuU1e_W8TbeQ7Dih_URhlYuuE0tI6btB-HJ719ZF_E2SRK1t4H-toi_pDFh5jwEizF-ju5-UByggnWPDg0T7sB9EPT5QFNa9fkc-WWu-mApmJ6NBogta99zgV7TUjsfHmHWYnsPrL8MZvRWLp-pYk11rqQu3rHfAu683LmwR466brKgwjnkQoGgezn602Mw-XscEunbkeP83E6vIepIUOTwwNN3hJPXYnQQDxXCGJ8pbcimt88CRX7zlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدار دوتیم استقلال و تراکتور در هفته هشتم لیگ‌برتر به احتمال‌زیاد به جای روز شانزده مهر ماه روز پانزده مهرماه در یادگار تبریز برگزار میشود.
🔴
سازمان لیگ این پیشنهاد رو به دو باشگاه داده تا برای بازیای‌آسیاییشون‌که20مهر برگزار میشه بیشتر فرصت استراحت…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/30653" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30652">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX73auPHm_rtg4wVxChFqiGDjs14Hp3DD-ar5uQyRz__aALrGkOljP0o-dCVyKzFv1RV8nYE4ZBN0WcFf4DsxWCFpTqQEbwq6paE_uwBP4fnkWoPYgB8cwZKwDGuTEPryBkhO6xd-SCSC6YYeivjhq8SSWDMF0xNSJHicxm1ty2TwglWJTDBCWDHY5aVHMJzXces3xKqerwcwxjNdY3Z0Y-5rNDLVfzJhLvtIQ1jf-T3BSPHZT-oHOlJnRPgw2EmrZf3TU1ept7hSZvdDY8_L93W8nx6bJVW120lvlfzIaS5F2M_CsJaDMZgFq7JEfsttMGru-06TilwmYTgrInZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30652" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30651">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=P7PK90b6U8214pBRy_cSK1-e2_5bZilMnNmW07CcjzmIrJU5Jke56ZgWhSzRXn0KZdsXCc-iQHOX89uVMPsvJGtlOyuaQGc3InJFsAt0B8qA9i19XWGTy2O-uKhF1NI0wtS3sCMv-mkuFifem0GWhFiU4JVU_md4BTe93IVjbozPBgmE5vVmveFDWnr2lVhQjssa_hN6esXAii3-b3LHeXz4_-BISyf-EEBXcY-2D3Q-7JHcjK6t7YBf9n3QX4AlMn8G84M_yiMBbTDOSCKCs_yDITqQxD3voPFSTFJVOFuLJPKLYOI7GYu40lKuAkkw3YQ7xva2vzwCi2Q3WY9N-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa777f5fa.mp4?token=P7PK90b6U8214pBRy_cSK1-e2_5bZilMnNmW07CcjzmIrJU5Jke56ZgWhSzRXn0KZdsXCc-iQHOX89uVMPsvJGtlOyuaQGc3InJFsAt0B8qA9i19XWGTy2O-uKhF1NI0wtS3sCMv-mkuFifem0GWhFiU4JVU_md4BTe93IVjbozPBgmE5vVmveFDWnr2lVhQjssa_hN6esXAii3-b3LHeXz4_-BISyf-EEBXcY-2D3Q-7JHcjK6t7YBf9n3QX4AlMn8G84M_yiMBbTDOSCKCs_yDITqQxD3voPFSTFJVOFuLJPKLYOI7GYu40lKuAkkw3YQ7xva2vzwCi2Q3WY9N-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه های سنگین و پیاپی امیر حسین قیاسی به امیر قلعه نویی سرمربی فعلی تیم ملی ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30651" target="_blank">📅 09:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30650">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvk8aFFj4n-o3YtKhkf0Kzhj-zHkEBRBS0SQncTnbgOyv6g2tDawFDXctQ2p92stR4u4dMvpWsa8fhgOE6MzqgqcYrJ_I9pWdK3k7qFAldEceGGmcfJkZyxC1BKoYUo7aOPcMTrgxaMSA7uiK7WoQPcPCxo8IDjTj19ZHqqQx-NeTzs1EGxxDYjLnyiiO_REUQNN9acj82qn1Jw_MROM6TuWda_bd201idMJHY3OA-Xvuig5VIZziM6s6jvTqd0Z4K8z6f6K7jvdg6G5i-aD1UjcvAh4zlGQRusKgsVUFkK_YYcRo2W-0_AH5LBWO9x0whxfNTQzgUXOp-SjeLvMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ معاون‌ ورزشی باشگاه استقلال: جلال ماشاریپوف بازیکن‌قانونی استقلاله و قرارداد او اصلا فسخ‌ نشده که ماهم بخواهیم قرارداد جدیدی ببندیم. ماشاریپوف تنها به دلیل مصدومیت از لیست آبی ها خارج شده بود و در نیم فصل به لیست اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/30650" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9biSMzIzQ5JlAct3AVYbTja7BhwXz125Dnrqj7wdBLrjQ8yLzE5ukWVcmCEjrpGyihIUBgqPqRBAvSHNHDDc8kdanU791S5La7R8tC59k_VY4440QEtJngXbAITJWkXz0clxpQ_Y3sG1jsJYalq0REEOJb-pFhf8v22B6V6FqaoRupf0zQ4eSDl8jjU1fUQGZ1f8-ZIF1e17SvsJCd_nehjUaiHCFboMGbUgKJXWgeSvtQPAEYX0z4xoMJv6VkkCkj3MbeF-p4oZYoTU_EcG2B7xOyvzR6z2rnesYCq4z3jQffpyfdUMy84LVY1A7wtExkwxZX9gh4vKCVRxy6nLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازتقابل یاران یامال و‌ لوکا مودریچ تابازی تدارکاتی شاگردان قلعه‌نویی با روسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30648" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo7N_Xx3J7A1bw5x60-aHbP2253KDoarxvRuL1lTthEVVdQrwcuAeiwTRbc8D8_yU5-sBhL0lekDEjOZo72ZI4C20TI8kx6ot9XNAFLSC7laFf3uAvIx45B71HhN69N5iPsHj_aWcbkGM4UmnNjDtUyy10iCPl-vZVF418DDHPHv8mzcKvIu3SUHG-IEk7IkWJLhNIP_EOlMsXBTziK2MJVPzc6uDbM4T9CAzsCFjTqBA6hByUJc2Yn9HibM2TlqkaJFtCOF8DxT1H_qSHTJMjkqJpGUJXc0Odirl3lpkip31qYI2QTwgjuiUWe3mdnhcc5g4_infNZWOscH_6je7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
دومین‌بردپیاپی خروس‌ها با زیدان و بردقاطعانه آتزوری در خاک ترکیه؛ برای اولین بار در 40 سال اخیر فرانسه یک مربی تونست در دو بازی اول خودش دو برد و دو کلین شیت ثبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30647" target="_blank">📅 01:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=lvrlxwfunv7Ub1s26sH8MU0Iddq_6SwnpIzMBGShsC7lPgLwtclSXmiBSK1wszwGidl6Z6rcv_ku06KazMw_0kJj46-YU4XNM_Ct7uqwgGlTyDbHcrCaX_oAwoHKFI8o_sBbQ797qDzKQi_MHKGJ1O8QC9VSIflUDHk5GVB_gjwsUCceJmzAiVC-X9MHRSdUkL6HdJpcq6NzAxXbJpP_qWJg4dV9czoDeWmbGOeFstWI4oDP93zdIrP2xAZvIsqxe2BX9eKTbzeXzj_aEpgiODwrPx7yhkCuyOjx7BjTJ3CLmIey3RblmJlZMmNwe59bMHaz9k4D3_ZBjagNPpZeSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc93b6b651.mp4?token=lvrlxwfunv7Ub1s26sH8MU0Iddq_6SwnpIzMBGShsC7lPgLwtclSXmiBSK1wszwGidl6Z6rcv_ku06KazMw_0kJj46-YU4XNM_Ct7uqwgGlTyDbHcrCaX_oAwoHKFI8o_sBbQ797qDzKQi_MHKGJ1O8QC9VSIflUDHk5GVB_gjwsUCceJmzAiVC-X9MHRSdUkL6HdJpcq6NzAxXbJpP_qWJg4dV9czoDeWmbGOeFstWI4oDP93zdIrP2xAZvIsqxe2BX9eKTbzeXzj_aEpgiODwrPx7yhkCuyOjx7BjTJ3CLmIey3RblmJlZMmNwe59bMHaz9k4D3_ZBjagNPpZeSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#تکمیلی؛ گل‌های دو دیدار امشب ایتالیا
🆚
ترکیه و فرانسه
🆚
بلژیک در هفته دوم لیگ‌ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30646" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=tZYac7QqeMlZZFbq6O9QEOaIWU_cWwJdpaSll2ssJH5o6eSvNj5t8BEN9w8YbmP2nlAaAe_ngp8xGBGLyBu_3tbI0cKWW_Au5WHHJs4Fg9lusazd6IkOCSthjYdGHQPRHUfJ7KoLpA94M4yhcveXZDgrPARVdj4ynILI_F25ZX4thDQsFThl8QVnI6z2kdUtch16XpPlzydiLoiChho5TRAYHkmsJt2fVE6Nc3pTKKxE2WYobglOObqBXZf0bp_XXybC7O_cC5EUz6UwN4RURYxxBP-jFE3ITUibmDW5W_yH6o-VwNH_qlzly3W3kPP_LxwSVnILVAptma7huP4_4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df13bf46f7.mp4?token=tZYac7QqeMlZZFbq6O9QEOaIWU_cWwJdpaSll2ssJH5o6eSvNj5t8BEN9w8YbmP2nlAaAe_ngp8xGBGLyBu_3tbI0cKWW_Au5WHHJs4Fg9lusazd6IkOCSthjYdGHQPRHUfJ7KoLpA94M4yhcveXZDgrPARVdj4ynILI_F25ZX4thDQsFThl8QVnI6z2kdUtch16XpPlzydiLoiChho5TRAYHkmsJt2fVE6Nc3pTKKxE2WYobglOObqBXZf0bp_XXybC7O_cC5EUz6UwN4RURYxxBP-jFE3ITUibmDW5W_yH6o-VwNH_qlzly3W3kPP_LxwSVnILVAptma7huP4_4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل باز هم تو برنامه‌اش از خنده منفجر شد؛ خودش خراب‌کاری کرد کم مونده بود که تبلت 300 400 میلیونی‌رو به‌چوخ‌بده خودشم خندش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30645" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5Icr5xwQIqbclN9ge-D4nUuwGAd5vv8bLr7qoHOVoEf1Ad__Nhw3CZMyhCWu_YQu7qEaxVvLV7ZPIEIgOC7ZLM72FF6pxkoIahny55RR5tcMjC7vMp_P28e0UfhcHCjXGRSfup2zbkDwVB0UPcE7d1cQU-aB4lRzl7K460J4HQvt3yGB16ltZLbyKSort-Ou77rjPcrFBsMhcNUyu-nNoIKQZZ5_KwocQJ4H7nWWWq17-4HqPraob3x03BUxfJQKBHN07XAN6RUJYeN47BrSE2k78aBxsq3KKVrcgSBVNyKN9VZymCULQ4vpEYXf_94YR1Z4N75fkI_CU9BDTHqxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30644" target="_blank">📅 01:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgB23wPZfkqkvuOIJU8Uj7TLG_0SS3RKLcti2FXSr88h4fQ4GGCBc6DLIFY9c7e-FQQw3jS2LDcxo6P_R2X5oRqrCKF-wUlePXpFar5691NBdYD0ShSfjXVlc3PiDUs_kdonjtsYLDO-khqvdEannOPBU5pjmFNUghGjVoEWRfoILw3HPWqnOhpp3Wv9Or43ciWTTQje1sGvr19gsOacYQe-yQXkYiMsbbpCzc7YdIL65-RwxTgKbv1IvrOAnasTFZ-iKj1aOg2b_IyWwF6pXH_ihVdTIKBn20j3R6ObOz4N9-0P-g3CiYNla43qORV-Vc_sI27J2t4o3_AVisOkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی پرشیانا؛ علی رضا بیرانوند در جمع بازیکنان تراکتور از جمع شجاع خلیل زاده و دانیال اسماعیلی‌ فر گفته درصورتیکه معافیت کامل بگیره درنیم‌فصل راهی باشگاه استقلال خواهد شد. این‌ درحالیه که کادر فنی استقلال فعلا علاقه‌ای به جذب دروازه بان 34 ساله…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30643" target="_blank">📅 01:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGx_taW29U9bi5w7i-Sh4QMXUZ764HQqmZdtzj_g7xGCb7-_RdIh341l0H6OKZJF7d7vsUgfCDJ2PN22gq5jCeQjc6eZBqTa4ly3-xcDWtiORo7w639kSNwraOzZmhzSNJQuTh1ZSE8eP5_QOnmr4UvZyWzjCQFPPYGtHW1Ynk8Lglq6vGhg6QWCnu3JZkMG5hyemlDacPKVLw0ihjlrXBFH6UFZj18sJQsAZR_Vi4mTUXAzknlA49lo-J1au3KB8SgqOYwhVKzeYVs_kD0k12riR4XTVEV5MGkEZ_AFCtniZao0qNrLJhOndiJHRbfaLV0ReMt2OvNHo8lCwUSEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30642" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇪🇺
نتیجه دو دیدار مهم امشب لیگ ملت‌های اروپا؛ آتش بازی تماشااایی شاگردان روبرتو مانچینی مقابل یاران آردا گولر و پیروزی سخت و خفیف خروس‌ها مقابل بلژیک با تک گل فوق ستاره باواریایی ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30641" target="_blank">📅 00:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVsgVMm-5HXiP93k2-pRFa9N9IyhC8giaNSZG4a-ROjmGVZB8PitzyUojs-_kqeQOMGJZWHMdQr9FmbXITXoee_IFhfUfQ3rpncnhZRlN3p2k1rETtzfAGV4ukzZcCbqqQEURr5GMXN7iX4nX7ZcXwiDOFtiaqk1gDjVoAXOmDpG8fMbmA12Mws1bES-bMlkyOPQh7NXwQTNxWIAVOMb425bkl_XFPgESLNXwZJ7tEUtIrB4j2Iwl7oxudvYhMI_o3LwxaYMVDEREe1r3K3fGO1pox9eOGa70CRehD8G8E_EgjvhLKFovVK3oTa-gcEk5EPKIm6qSIim-a4rS3muiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30640" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=lpVmlWubVwh_GU_a6i115ATsoVtIsyTEizTHx8py9htBxBLGoJHCokWl5UoMVO-lzPoFg1gsitVOaM8UcOkcZZMkgPzLQpvWzXmVOjdx0gRcZ356nldLzLKq2g2vJDkFw5gPBJhBhfTgkeFEv5T6rKXWbvhVB1QK3VQyGteKiGnivJjY5mJfSgOPPzYoSz5l1Qw0RbQdHw4imUCZqfL62y8HkW175hTjAsLhFeN1b8dVIt8S1fqAtcbmD5I045ae2jI3py46ocDIFLqiwaEVef_Addn_TicsmQA8fOx_9yKFqAeO1M1re7vAaW4Tg48lhIZyzJ1e2Mfmq0JyDDNPwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd8e0f64f.mp4?token=lpVmlWubVwh_GU_a6i115ATsoVtIsyTEizTHx8py9htBxBLGoJHCokWl5UoMVO-lzPoFg1gsitVOaM8UcOkcZZMkgPzLQpvWzXmVOjdx0gRcZ356nldLzLKq2g2vJDkFw5gPBJhBhfTgkeFEv5T6rKXWbvhVB1QK3VQyGteKiGnivJjY5mJfSgOPPzYoSz5l1Qw0RbQdHw4imUCZqfL62y8HkW175hTjAsLhFeN1b8dVIt8S1fqAtcbmD5I045ae2jI3py46ocDIFLqiwaEVef_Addn_TicsmQA8fOx_9yKFqAeO1M1re7vAaW4Tg48lhIZyzJ1e2Mfmq0JyDDNPwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛صحبت‌های‌احساسی یاسر آسانی: بااینکه برای تیم پرسپولیس و هواداراش احترام قائل هستم امامن‌هرگز به اونجا نخواهم رفت. البته که من میدونم شما پرسپولیسی هستی آقای فردوسی پور! جلالی گفت من باپرسپولیس‌بستم توم بیا گفتم هرگز. اگه استقلال من رو نخواد از فوتبال…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30639" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lD3AifISIHrF7_bws3k4L_-w1Gn_cVuYKXeJIYBMM-V-gNIzh6-hJT50xNG1KdGUAxAQNxOoEFjG6J0V7Ufdw-smkpuUCl0v8e06dTnq60vUIviGpVzwjnKoWpsl4EO5BkTXBojCV9y7RnWrgjDKmFDBYmg3mF-cnB2_-VYMySBOstZBt5jGUQ2lfn_Qzn-GP2Q3m-PX7dX7OxzYXAhYU_pTSrmV_6UWNZvx0l70mnRrT5k9lXd3Nh3BXHeHU7bNjuVasUv_dr4IbZ86VPdiT1CxU_CttwMXLOuzE_g4s_eDfwUTxkaA3UzGiYJtZzmVW23k5N-61oStveZMvJBlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30638" target="_blank">📅 23:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30637" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیاناتوسط یاسر آسانی: باشگاه‌پرسپولیس بامدیربرنامه‌های صحبت کرده بود که به اونجا برم اما گفتم علی رغم احترامی که برای این باشگاه قائلم اما جز استقلال نمیخواهم در هیچ باشگاهی بازی کنم و در استقلال موندنی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30636" target="_blank">📅 23:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=G2omR-U2XQHxyWbJQ09b_1Y1EO7Bi6icO8LdXobha_ydfX_6n-dn3uLEZAjuYp8jk_CkQMnR2KGm5AgplTTwQmIXFpdW2g83RJd0mSD_tJ59i1Sx1oobvA1gOzqFGEBWdaylNkfX9LZetpkLM7cJQQU9GPp-zngWymBhyDyTixsWyC8e4ayg3yqcb55zJzO_OBYt41oyJHdZY0DJBZaTsSYdItoP8yb6oLC6ybfZertRFThJIhjjLel6j1skOk1PTvwVTuhEcy4M9LThR_YdKWv-KlT8hFtd_cBzuycM0IYu9VF6WzijtqXsV_IZrYtnCKXrHmh2v34sR1v5kjJTS3Sl7J5zR8P2AdNVbuYFFIyGYTuRBaserFhnpWindneT-HyQx8MW5nISFcElsIubUz2o9U_TVnADiYic-JWT8nyGoog8JULhZVq0Eb2bnATivAN5zHL-QOnp8h4X8EUDL4DjxL7InEd2x0x8Vz5zwR56C50c0u6qtvF8nhQ49pHhoqbfXgUlIyRtlY4MmEf4z3w5Of3yMi4qjJnN876T1VNo13iI_CBeYGJCrspQLlc9V-MXET5NIGLrmrRteF9WSQEciogaiAw5UGxN0P0r8bDMrAtrs2f0j5siB8nsQO9NpJw2MleTkgr9PR0qiaaswRxy-TZwrFLGTEDAVRqnK7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aab94b2bd.mp4?token=G2omR-U2XQHxyWbJQ09b_1Y1EO7Bi6icO8LdXobha_ydfX_6n-dn3uLEZAjuYp8jk_CkQMnR2KGm5AgplTTwQmIXFpdW2g83RJd0mSD_tJ59i1Sx1oobvA1gOzqFGEBWdaylNkfX9LZetpkLM7cJQQU9GPp-zngWymBhyDyTixsWyC8e4ayg3yqcb55zJzO_OBYt41oyJHdZY0DJBZaTsSYdItoP8yb6oLC6ybfZertRFThJIhjjLel6j1skOk1PTvwVTuhEcy4M9LThR_YdKWv-KlT8hFtd_cBzuycM0IYu9VF6WzijtqXsV_IZrYtnCKXrHmh2v34sR1v5kjJTS3Sl7J5zR8P2AdNVbuYFFIyGYTuRBaserFhnpWindneT-HyQx8MW5nISFcElsIubUz2o9U_TVnADiYic-JWT8nyGoog8JULhZVq0Eb2bnATivAN5zHL-QOnp8h4X8EUDL4DjxL7InEd2x0x8Vz5zwR56C50c0u6qtvF8nhQ49pHhoqbfXgUlIyRtlY4MmEf4z3w5Of3yMi4qjJnN876T1VNo13iI_CBeYGJCrspQLlc9V-MXET5NIGLrmrRteF9WSQEciogaiAw5UGxN0P0r8bDMrAtrs2f0j5siB8nsQO9NpJw2MleTkgr9PR0qiaaswRxy-TZwrFLGTEDAVRqnK7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30635" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRNau65XzEniuV89snwOdz0Cb41njENvE3AuJMwd4UrcOIiiPpTfaqc2XYuiCPiGPawwWHPIgstrF1xnYazrwzXyKgT-m6aSVyVagctJxb8i5Wer46xIaYPwBYz6NfES3A9bh__dBprzmEkX6Wnj1bip-Nx6Nsrwsleq35jjKWbRcqKgNKQiBLT-6lkR24NiK4rO_IpIm_mDNBCBShIHuTHAlzU85cRL7a-k4_WMBdhfk1dMF1APoDtJGOvzRaQMjl9oaVGkEL4B35lGP77-eI2rjKEQMW2Qv-Qc6hivU1XY5027urXb1XvS9C2b83zY_dq6qKKzxVDSHQIEXDt0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از مسئولان سازمان لیگ در گفتگویی کوتاه اعلام کرد؛ روز شنبه هفته‌اینده پرونده قهرمانی فصل گذشته لیگ برتر برای همیشه بسته خواهد شد. امروز در این باره به جمع بندی نهایی و قطعی نرسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30634" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac_4iJL8aJHoMErah_hlVn9bx-l9IbmxJEGWhosHC0So6kURWOtTppy6bI6-4-cmpmpYa0F2haCeRv8yAPY4Qe29BSpYwA5ZHZ82yhrClWYFndcboTg4KG3vOCUoWpNYk9Nc6bdUbqlTxJ9X7V2A7Os-QUaetPU2Jldz_wKKsT5YHR3_avuI-qyOUJ5yF3KTa77nUEdfKrvdtQs7IhJoEymwqJVKhyzMudN7uHRMliG27i4ALc2mdjVJ3MMDeITOrLfCNWoxBVFZtrHEwJ1-TcgtEDbGdORBtqesweCyb5ivjtan1A9UbGLqldhd8VL51xOnWfhHoLqoZadB0JYHMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30633" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=c3nERLIKpv-TBICbQfuTsWCQwM_hcXgrjUv7DVeUS6n9YlWZyHRrnbUywRHRnmPp1x8hA9jzAUTCStO4x-nrvqZIqt_J93cLZ4IO2X0lM3zTPPAmqWbBVoWPG6GLWhUF6_xcd2VzXfe3GIrmynFZrsc1dCyV_et95GPVylYG7y0N5XaONivSkQDbUsowOkK7MMYsuz5BD5dY--gmiQlbPikRYfWpstKSSvvKP0oJBmvqW_ibiqAgMp4Gx_oIxdW16P75SNocZm5XrVNnJK7tMkAPBLp9IOyzHuLryiDtOo1fBqOUux0SFKfsBSolRSuGfRHbbv_1SBYed6OrxnEJ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efdabf6f72.mp4?token=c3nERLIKpv-TBICbQfuTsWCQwM_hcXgrjUv7DVeUS6n9YlWZyHRrnbUywRHRnmPp1x8hA9jzAUTCStO4x-nrvqZIqt_J93cLZ4IO2X0lM3zTPPAmqWbBVoWPG6GLWhUF6_xcd2VzXfe3GIrmynFZrsc1dCyV_et95GPVylYG7y0N5XaONivSkQDbUsowOkK7MMYsuz5BD5dY--gmiQlbPikRYfWpstKSSvvKP0oJBmvqW_ibiqAgMp4Gx_oIxdW16P75SNocZm5XrVNnJK7tMkAPBLp9IOyzHuLryiDtOo1fBqOUux0SFKfsBSolRSuGfRHbbv_1SBYed6OrxnEJ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
پست جدید سردار آزمون: پاراگراف اولش رو بخونید. رفته متن رو از هوش مصنوعی گرفته دیگه فکر کنم یادش رفته قبل از انتشار ادیتش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30632" target="_blank">📅 22:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIFeTlcmJ9PtwBOzD-u30Zk9TjyeIeTUUO9n1gBu0iuexGr_uqnCuzIcom59lh5rokvR8LFY3Fmj7DjbXgMUcMS8-e80xnXeluCDsesiuly5-5eMSSvHUz3n1A7v-sxaE11dYYSFyHTQoLIQh7z6Pjr_PXEqT2RYWbB9mVyKR4kq3K5qFxfU3Q0zlQi6zZKQJTna0bVhbBhQD8rpMvdU3JGwFdmOP5OXajWEPpEU7ZLfnl8Ao2VDaeR3bnBvlPlh-i26tdtPD937kBmsj8DUQhawcx0yA7adR7U_JElQq3jzfmHZYfP3tuQe_0owFOyOE-DMd7aNxmX0jBlxvJGfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنی که یه زمانی در دورتموند آقایی میکرد و به یک‌باره‌سر از منچستریونایتد در آورد و کم کم افت کرد در سن 26 سالگی سر نخواستنش دعوا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30631" target="_blank">📅 21:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL5B2RTAOLrBENqs3rVC1s8Ln-7sLHq26M1e_pZePCqLazJoy7WmevLCZZZbnssJ4zS-WzhR3FvtlYPmE0wsGmPSWJaE7kWRKCxMrDXs7NzEIbMVMjMG3mCf9MCTUV3qzbZXMt_3K1FNG_421Z8SeGM1KBjsX8hNwbOvc9yqBnJcn2UzW1aoVfDmX3jh_YZwznRNLImIEllg0KhOIX2M9K7JN98tnxhsI4lIOrzzvvJLoXItTy0JIbWZIsbTZUFNBKGAh9M5q20KJmlUwArxdq5YZeWDx3vjrTBHxqgEVN53XI94gVtPQfj5ZKGkeX7fZn8LYdUcKKX4SQyIqxaR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رای‌دهی‌مراسم‌توپ‌طلاسال 2026 دقایقی قبل رسما به اتمام رسید و از این لحظه به بعد برنده توپ طلای 2026 مشخص شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30630" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAeOUnOoCYOYF-TOwbHI8BcPRrkvsrmuivfWede29lj6TLKblDrbMKmXQEchh2y236ik1n3xM3-LhL7UFdiFU2ynXW-CzyUjvmtalZthUo2zer_pBSv4cSqcRiu4MQ62Cpd0nPLkNbPiH3RXDAIHqWYE6rbM0NMt2s3ILBxzTeulroIH68zoc8Bh8GL1UFnAkEi5ocsuMSfZ_rrCO0JxCE7vi0pZsPqDWsyKseaRcuEoN1r7reRsiv9S7Xvgth3IxTP90HSpmVS-0yWCZd-ZLztJ3xZvXn1mRWetfGaClXeki6JJTSnZhezT3eaGQe2WbH1DlBJzexlXO-03HX-OKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNfAF1Br8fpbYvR7TwibUlB6UBIbUua9a2e37hLd19Ik1oEdu1tyLbvuAFF_BsFZdCfbF-nK2VL8gTJx_dw0En3w7Tx-okT9O1AA854aqUTl7oJ2DxIjrlE6O5rGytEGCDUbHoVwzWX0AZ18RTZrVmT_KVt4MydVBP61zRZb5l39WmJV1DOcqXG9ysiQDTln6kASvnUSUSe712Dq861FgPdEJdXCt-8Wpb2ct-FO_-IoRqw6AGGuF_Jo1te22gl4Zk8KnWYlqTHT5qkACXmW8wkITEbt1OEVdaDapyjyxb0XTszLwMVadVHGWSoh2nAj8gu0DF2OrlgmRTlgMRfmxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StssIKY6S4D7u99e-sdcs5FFGMLm5jDQKd3KBJZsS14pUm1WN0yBmqhjjI35qMzPTvXgj_EgyUVfA1IT6n07TuK2wo2cyoDlcLuhRQRKv5649OIGBvmVBQVpL9Bk-g04mGAU-Uy0TvG89V8osDJimZ3juPF4Z5iqKnLr1SguV_3s1QSWgbA9WRR-C9IHDbEH-QgffVjT8NClVsf6YAR2lkhSZYZUPmqER7S547wqJyUqwFRTm7Y5aumf52OLGbfrbBdv2CuJ0C1PHtLllFrW8IYsvZPdUmBN8VenXlF0GAK-u9izKSc0LrDSwNnTJ-BtE06abgawH8O9K_6IFYNbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWiEd2BAud1JH-qI5KMdG-IcdISkfccKtSVmCnZc4UC52cxm_ZB-g3n1drqoFl7SghDewMDgimzI0Kr0RvfM5SGdLRE7xyMDxQXdINyR23w7ZO-WhyAvb21CFktvjJQrOGE8uu5BlL3eDme5a6UgKYdyddm-s9SvTnpKRW4OMB4XXskUwglL2_TN7WJvhxV2HrpvGbfJtkN7YUvQwlluNDdAmmUArkfcA6xSkzUTWZV4OtFl4e8f1M6-rBLcgxYLPtbGW6l1aN_FnTpa6yXR3jV3HgjWh8zxMiqnfhFcnAsENZ-BK0priGmZCRJ6Pwud3JDBtZb72ctQ8_mLIiMChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=k0NKn_jQ1crq_zC7yAYG70iA4fP7utBsACYUNihTuDreTaP7pLIE-DnbH0oq3m5hSe8sutdGqC50-0S4rH7mRm0QA2AOayxQi0lVJ-ATahMljjKi2-AEuRClcrSmf6aiJe9S-p-TqBUsQ17htwrIHOwFNZMEeTusVOxLBfq1r6GJdgBD6LNpF7pDUE2S0zWWvuElzE06vUWbAtVlmtRO1H5hJHb--KRHpe6bFXfq_7ziVzhIfKjHdCIyYXdbKBnQ4HosLXNs3gxANnnX5-hq7jaEkpJj99ma74VLxxHOwcstuu05xxL5BMoaZy_1C1nrO9WVX9kXXIA9GW4kkk3X5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=k0NKn_jQ1crq_zC7yAYG70iA4fP7utBsACYUNihTuDreTaP7pLIE-DnbH0oq3m5hSe8sutdGqC50-0S4rH7mRm0QA2AOayxQi0lVJ-ATahMljjKi2-AEuRClcrSmf6aiJe9S-p-TqBUsQ17htwrIHOwFNZMEeTusVOxLBfq1r6GJdgBD6LNpF7pDUE2S0zWWvuElzE06vUWbAtVlmtRO1H5hJHb--KRHpe6bFXfq_7ziVzhIfKjHdCIyYXdbKBnQ4HosLXNs3gxANnnX5-hq7jaEkpJj99ma74VLxxHOwcstuu05xxL5BMoaZy_1C1nrO9WVX9kXXIA9GW4kkk3X5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=ucC9IUHuupKpDU0SIjXTIw8vEILS5lcvmT2sT86cgDuJg8yUX2I8_9Za4uqsxgn_Sj1pqGXcWjC1d9q70iGA-k9lPMbXT62Y-Juole0k_w5DakFda4frE-PC_V1R0DAX_KuRTXGKprH0FSyvr17yboalB9joljZZhEbdWkpilhMhPwaet5ju703OWLaFPXZXdOLUL3cAbptL6O2r_jPTfibvtTbxr9h1NbjchUIfhzlqDfFLNkVib5B8XeTvTTsoeKvYhlEBeeYfteO8oFU6OyXg9KS4RKnUgZoQOs6jz_4HYF42Lfe3VXNA__RXXhLyUmzRPzPhVQH5v0Wz8fvhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=ucC9IUHuupKpDU0SIjXTIw8vEILS5lcvmT2sT86cgDuJg8yUX2I8_9Za4uqsxgn_Sj1pqGXcWjC1d9q70iGA-k9lPMbXT62Y-Juole0k_w5DakFda4frE-PC_V1R0DAX_KuRTXGKprH0FSyvr17yboalB9joljZZhEbdWkpilhMhPwaet5ju703OWLaFPXZXdOLUL3cAbptL6O2r_jPTfibvtTbxr9h1NbjchUIfhzlqDfFLNkVib5B8XeTvTTsoeKvYhlEBeeYfteO8oFU6OyXg9KS4RKnUgZoQOs6jz_4HYF42Lfe3VXNA__RXXhLyUmzRPzPhVQH5v0Wz8fvhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ_ya5XNG5LamPf5H_s9IYi0idPEPWM7wMcWjOgrzXctCNcaJmIzCCNhtXE7SNSd_kfiiN2Kw3XVO1K6zzgtCjE48unNMY8jz9CPM0PCQpFVzJeghG476HLUWkHoBIRJPh8DEMahbxD7Lfx8tR13b7vQVv0hKjMdBMpWN_5CtbN6QPK7871PlAGquNag-sEUOKo99HFgTbp1ClcPfbl88xnsvKZ85RshWy0rpF9_KpBw7jl7p2Wil1YGmE_Mc9Ft0B3xJQCFS554_ieSRCQmcuDEYfdG9IGTqgr5SF_2g4UwdVpJ_DJtWD43eggAvf2JqyY_l_2UMvQeQwkrGVab9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=eB_jcYip8O7RlmOEd6vyalgkrIdsYr_QzpYuGjz1muhQ2m-l0OPq4d5y_7ReKfWQSe517D9OinUB-vV1ceY5hRs9uDA-k_aoGx972WLu2GDTaTLdUPgPLz05o_yn45kFSPQeIeMfMvSSDYvle1AQrLpklmZkmsw7QtOHFUujpTKQ_3OYKjWXmwxlpJqrlYdTEIifuVB72TsqFLDLfyGymqqPpSFBeo8aBwehPR7CgyzpeILxNaoY2VP4cQTIhRQXiFZ4-h3D6bVpSNdH0a009lpaIgpj3PnEWVABHgF-JWRZS0TpaASydqMMNIqPtiN6DKadT7bdoIcZ4ds9Ct2okLN6vnSZ1cITLoaaXeUTaCLTysicKSMh5oX790hT56lJeZfVOTT7iNYHNVBO5qFW_jN_zsJkfxP_Vln4iyA7m0-h-EpdbuKhK_8jd3_rx-Jm70yfJyplwZVvfghRred_wTDbA97jsx5kx2E-mzF0UoH8BDlHEyrzkgiOJw-ruVyxEq3GgX7adF37za2v1zBIgsQVau60lIXPBqQfCutRja1ImeZzNP-fqFnI3inRS4dI86CfjXHvJHJAd3W_q7BQA6iKOkI2SCvEpOJVp3tjb-nzwt6O-Y1eA2ScSZRb6ReIr_QnskjtezCLR-8XuynJCAzovARhYVbQsIDoE2SjXlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=eB_jcYip8O7RlmOEd6vyalgkrIdsYr_QzpYuGjz1muhQ2m-l0OPq4d5y_7ReKfWQSe517D9OinUB-vV1ceY5hRs9uDA-k_aoGx972WLu2GDTaTLdUPgPLz05o_yn45kFSPQeIeMfMvSSDYvle1AQrLpklmZkmsw7QtOHFUujpTKQ_3OYKjWXmwxlpJqrlYdTEIifuVB72TsqFLDLfyGymqqPpSFBeo8aBwehPR7CgyzpeILxNaoY2VP4cQTIhRQXiFZ4-h3D6bVpSNdH0a009lpaIgpj3PnEWVABHgF-JWRZS0TpaASydqMMNIqPtiN6DKadT7bdoIcZ4ds9Ct2okLN6vnSZ1cITLoaaXeUTaCLTysicKSMh5oX790hT56lJeZfVOTT7iNYHNVBO5qFW_jN_zsJkfxP_Vln4iyA7m0-h-EpdbuKhK_8jd3_rx-Jm70yfJyplwZVvfghRred_wTDbA97jsx5kx2E-mzF0UoH8BDlHEyrzkgiOJw-ruVyxEq3GgX7adF37za2v1zBIgsQVau60lIXPBqQfCutRja1ImeZzNP-fqFnI3inRS4dI86CfjXHvJHJAd3W_q7BQA6iKOkI2SCvEpOJVp3tjb-nzwt6O-Y1eA2ScSZRb6ReIr_QnskjtezCLR-8XuynJCAzovARhYVbQsIDoE2SjXlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvtD53xyxEVoNMrp5W2Qqho1pqKezZLDbc_GKx0Q4-t15uHOGVJOFpA7tGbJymbEh5LX9-PGQ1Tg9BAx4WtJMH-TV2zilJZ1KCMbgAg4Megx08Di1A2bF5q5AT-WxzI2_x7_oMJomFwd83AQGlWpOXaIvkWEzNZZd4Va1F0a543RnrpP4ubKlygcwYTDLOWcvOQiX5n9AQLipDI0M_lnbtMd8e9pH-QFCfHc_1kM0NowuI1BoOKOkDBdqJVN_STIrANxXIRwz2_AUpRovw55AjKi9V6CjAhI8FQMX8pn3EUUkdrMtufAu54r24Tnyon_RaWmHNctaoY7JBQzdAgIww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30621" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGyl6d_x0vF0-L4letcCEOaIaOt4B7PeWpkJYJ5rxp1aOK7Z0gbrdTRpHNOf1Et61nVBzS8VOz22VQ06t8BjXeAzbqscPT3OC7rwb_rY89ZF0FLptY6DghZkp2_qp8VZUmIe6lPNA8esCFRLHs2jTSRnD6VrbMRdKBoFzn4iVxPDpps3FO3HPuX8nBdRXMTJ3tWNnl2y6GgVu5j5Jz0sHdy70lVmqJR2ukLK81tnFhILgXLOhu0N89uBnFnhePwjC0fdHR0gwXQfKjpAmzchHE0VCggaFoxhjpXThcr7KB7R366PX4igVMZtb-pZfLiwL5DMYV07qVxYM1Y8vxOj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWjLw3Z9QhlgJ87T4bzcPFSHZzPkYIWz_VBXtUcF3gJVvLaX-LYw7jnPyv3YNNaerdQd_EgfVRPU6bYcdRU5dghp9UYWJiQr5lG5K6U47CruJ1SULMZ93LJEejRUoi8YQzp2tO2T7iER1xF5zBqYwXxyEOhkF-RmjyklPlYIq1p1pOE1CxJ-UF2dm4bDzxUv-A9WkYNndoLHq2xJymB3q2aLX5lUh9BdUqiTWOxL_I1bqZUgKoJUSNsF9LlMQhCEvfynBwBLcKV58Zepc7kRjQ5S0CFK2z6P38RGFpFnpRy9QKuRKup4jq1iJ-8atn5Ar40nE5oUMevl2PoUvYsIkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=m1XU5otX90wbgdveQ5__O6et_6iZtFf1rk9ej0bKuXk0JiYJjFlkWLYSf58U0u-uwZqiXsYW_4D2uyw_KwEhm_b3UuXFh9NGUSRfGTVydPkhHegm-T6zwxNx0r4HsZRZFwpfpd-YvDDh_QnwXzNnodxmPNV4yfDwF-l4OkZ6cAAVUDGnZ250sYW0zLw52hZWoPO8R03NiSdkYnid4d-29Nky8O2aKa_35YkJiepLI3U1KbuJ_8oytqEa7R3oE9HZVJOy2YyVqC3OTpCW9U8v0pMXFV4mFWxtImfeFqgpl42wh2zSyMk4ZdTtjpLZt_pg_oXHNFiBapDG1eF67HuXYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=m1XU5otX90wbgdveQ5__O6et_6iZtFf1rk9ej0bKuXk0JiYJjFlkWLYSf58U0u-uwZqiXsYW_4D2uyw_KwEhm_b3UuXFh9NGUSRfGTVydPkhHegm-T6zwxNx0r4HsZRZFwpfpd-YvDDh_QnwXzNnodxmPNV4yfDwF-l4OkZ6cAAVUDGnZ250sYW0zLw52hZWoPO8R03NiSdkYnid4d-29Nky8O2aKa_35YkJiepLI3U1KbuJ_8oytqEa7R3oE9HZVJOy2YyVqC3OTpCW9U8v0pMXFV4mFWxtImfeFqgpl42wh2zSyMk4ZdTtjpLZt_pg_oXHNFiBapDG1eF67HuXYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeBmhRC2yOBgcWjO11AUZuQPecV4h7YuPP9ZMAL4uz_dGLb3jXtdGKJt5tyGtx8VXpTUMeRp-9Rz7-aDsLKPoDfXvQe499TeUCc23MfaYhLrUSTtnUZ0oyhlCCeULwrrXM8fwVDjIJF6TUfRCi9gHyF_pQXIb1dlKOMqvV08GKNVnCbQ39GosutJWsrAiDrrvFVCOGYyPxK643X42K45cBf3FGssA0fx4D-WbcsPcWoGmWvQdPbBrGZ6FgZOzZGzkB8CwySJP-UTLnlkndc0hB9UHGz-fbIPwO8b-uHdC_0xJ_7gy-h_rRT_BkOgQbGsZmjLojz1KfEsvVLhvsrHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ75UM7McTFNnk6qag8Okpe-JBBDmTeD9dXewLukOxP3Shk9VCAv8HKjN5JCmPDIIBJYIu-tqlLRXfmJeLOX5zslXwjFPUWrYLoZQzaRV2vmo2wELUk-L1TZmb_p2QkkGg544nC1DlXO5l99DJ9ke8eCRJILxe8fE65B_WM98_qxWshXb2V_mIHcrYvNRhvMeyS3cGJoDfJAELPKkr8o51v7gfTAQpOsYYel8TFQE1oXjXtHr2aws02MidHJLXNVf5o4rFTslTGnsFlT1hSL_ElMkKFQwXyYi03ris4G_lZHyvwDDGQz0tn7fecq7ipsnnkhxVUJYCX-12k-h-Ri_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=PqOjAYlxJ0MIfYPl-Q79VV2Td_HoWxWIycAUUGvnCEiN_Xlhc27K9DAOOgYQwSbcjUGQMXqV61-Vzk_S_kJme121zcvd1qz9keMvs0bjyJBPP73c2Z6xiPMFKLIomml9tJwf_kVbdETIj5nBtyhoYKTnsRLZTFAtiBR7oblhB0X7Ch3WkWKoCMy6DgoS12depYNRm_JXC5UYNGoMoDolXQAp5JrxVeEw_LCkpYok03K-mhefHPv7r-fxnxniF8JMyljBiqADRKR6rZkbEygWpikyp8OC9m9ODLlfK4RekxPQTE460BMZIBdxebHKxOSaZstsijtHuZhQDJrwaNeLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=PqOjAYlxJ0MIfYPl-Q79VV2Td_HoWxWIycAUUGvnCEiN_Xlhc27K9DAOOgYQwSbcjUGQMXqV61-Vzk_S_kJme121zcvd1qz9keMvs0bjyJBPP73c2Z6xiPMFKLIomml9tJwf_kVbdETIj5nBtyhoYKTnsRLZTFAtiBR7oblhB0X7Ch3WkWKoCMy6DgoS12depYNRm_JXC5UYNGoMoDolXQAp5JrxVeEw_LCkpYok03K-mhefHPv7r-fxnxniF8JMyljBiqADRKR6rZkbEygWpikyp8OC9m9ODLlfK4RekxPQTE460BMZIBdxebHKxOSaZstsijtHuZhQDJrwaNeLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=lczjsJlIxT4ZR7tYuQySascBicE7YCYAgzVrHas4dcwOOx5j_VoO8KwXNf_lyg7caYYDqwv3U-8PSq7Xbb0EIODf8HnoziJifPh3YEiY2O-hupPQb3JufT4EnHetU_eLerSEqZNwPT8XvegpC7k1IV0a3uEgph1U-P2EtdUhBvEDtCRpbCaEOeqMpLl2w-X2GxW_loi--2HZ0_QFlFhl8AXNBjdKbffhpUB6I3aY-be7mHVSuNbvxP_e1EYFL69UmT3K04SvOTg31YI9S5pnup-HPAT53FY9Rqhbhla5GuiMkPN2q1GJ7IpKOJun29FMARdxZ8FVdsLhzuUpQAd5Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=lczjsJlIxT4ZR7tYuQySascBicE7YCYAgzVrHas4dcwOOx5j_VoO8KwXNf_lyg7caYYDqwv3U-8PSq7Xbb0EIODf8HnoziJifPh3YEiY2O-hupPQb3JufT4EnHetU_eLerSEqZNwPT8XvegpC7k1IV0a3uEgph1U-P2EtdUhBvEDtCRpbCaEOeqMpLl2w-X2GxW_loi--2HZ0_QFlFhl8AXNBjdKbffhpUB6I3aY-be7mHVSuNbvxP_e1EYFL69UmT3K04SvOTg31YI9S5pnup-HPAT53FY9Rqhbhla5GuiMkPN2q1GJ7IpKOJun29FMARdxZ8FVdsLhzuUpQAd5Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30614" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBrbIS8eSWWVqN5gM76Q_VWapFVOYMtzhErZr7Gb2ToyuJ4CyPFUZy1--m7RDfyxyB_5gS6vqhsxVd4ogaorC_AA1IQg-LuMD-VScd-QE8JZrk1Hjt9jv89dlfP0VyIbK3eOCZ855v356fZS_AViIMaeUepqYgyll4sXPqq_iOiXaxtezjsFWHNTWwmV95yszvC6nDggNjaxvuHY8RLyROByecV463zKueLK6_Es9LZ4uHeDx0sQsdZIkBZq62dIwCDyD3HIXfT4tkvzXwry1jE4e8mDXlJUQ5aw2j6haPV0xNPX7LBmd0JQkACGri6P35dUgnbEKPy3_1R4vZVeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30613" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5B483oiHUHjmRjna2OjhysNwEIlTai8GCUCcTZz10BpGqgi6A2BGa7GBs5zYqVpXAPb5eQwQnTqZqV0sXwWkd8XFGZxICiHkoXGuio2Psy49qeU3RE6fE1zAfBAopuNpGb2CdxuUO_DjQOK1n7Wsek6fPP0r_R6SNd-K-xyZWlnTPcEQrx2DV9eaJDtXxayiqEgCp9Kb6_N4u1ulyV_hXhjXsE2QOrzGBpuMRm8nNelfI_vf4-u08UsiMqUmmMM1FL2s_gp2kEmE0-6s7vhTyGQ88r-wg88HAWOa7F15iPMgvgYhEfobsKV5vjX3JDdea00CjtVFYmHggx8wb5r-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پزشکان‌تیم‌امید؛عباس‌کهریزی‌و اسماعیل قلی زاده دو ستاره تیم ملی که در بازی امروز مقابل چین مصدوم شدند مشکلی برای دیدار هفته پایانی مرحله گروهی مقابل کره شمالی نخواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30612" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30611">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKo4MA1IA-ywYEPJ0fNEWwbyVTrmvxahxbX6jb6pm0OcpcBrv09Ro67BbaHvrDMNTk9JaXl9hdlN-SvRUrlDutFr-LeIDc00nd4QBAOjc8RlD2-Mx_waYU1yWvVW62kBzfQ1JfVJZ6av88GggVgJpp2rZZgJPV1XywwXhPVEygekBTnvD7U4b7jnEbe805riJPGW4oGDNHu4rUuauNaSCF3Z9LQEZbgr_LYgQdfQOdEGQplwqeCcdmE_a01eOfjhg_82WsJFMXqKvzdiAvVONSu_gOidjXa4IBEHFrwGQy0TAWFe6y87KsPvz0BOb8GZD5fBJrkHBsEBNgEpH-132g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30611" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30610">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYaYKUSgNZbH0B5z8j2bUqhsx0imjUkbRYCscRx44TaSi9Ey3UO-IO-FGx_fDuJWNPqkbmEVMQq0ILGuo8hTJDApmaWsbkPaJWh_FhGYEeFpPSK4GeCF3UGQDYOtoy8DeGpy6ia1ZZ4O3G52PZOeOviB77iPNJanD34eK2lVZvsK1tGeCtn7pUtfsdKhELLpdm0ZInYYpF_KaAKSeqq-NiylIIp8UBejWqR9Qy-gH98m205L81IgnhOw3UdQzBWUEdmchaozGAVQiq-PSbL4bcWEfbfm0XeF-OtpJtUsR9MwmuA50rF8SfYE6nkFdQWOK_OLR6iGhgyuKLd4U7dDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30610" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30609">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqiSFOdLbPzZ2QDBZZ5IU2MBWdG199EKOLPLA7OdFh0zO-Imazfc2YSpTCd0Fn2Ch8fspzbuY7iK28K5cG9bRZO2JyCW3WeUDk6YN5N8k0QU5b94RiwsbWi494sYyiEE5SQ2hi7X6DKKKbLd73OtL6tut6jX3g3pIipE9iVx_Zl1PWMD96boAQVs9avjjqTYnVOmrE0C7PiA24IOsFN2_I0xxyeQKblDfhq0cVa_we3tS7gi5KiT9SfY6Ecx61xlTe47ZNx-8B6mre-enAsDdTu8MNpvLHetPdCqxVY6H1n23MVRiYLah51WXCJdxXWoZXl1pkBGvvLFvKnFMZcpXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش ناگهانی قیمت دلار و طلا نسبت به روز های اخیر؛ دلار به 245 هزار تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30609" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30608">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=NDD1R_JeNV7Bkh-k2-2hmAHWQvmcTnfpPHAO0Y-CFMWjhjv6cIosYXXPT5zQ4CkHXLCJvaxv5uVXPPn-GJwZqGvZIDY0Pxsp4wDfsIgos6CSO111iyjTwQ3CZ_IrIE7gDAD3bgypvG1TJRvlEtgm3h4Yz7ZHi3kuPGvgwni79jjEkFV_oBnfiXhmWM2TFZGdCnitf3peyO13ni4QD2dzdFpLnrQR1ZzwQElUUdEkrfjZe8EM6_U_ZU7AzAnqamPQi5pom5gvAEK8RNqjP4Mr4AHvhkdhj_k3fQhvMdK8VD6q1hFsbi2KnQ66E0hp3P_YFc694C4QRJCXbvZk2yHeIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=NDD1R_JeNV7Bkh-k2-2hmAHWQvmcTnfpPHAO0Y-CFMWjhjv6cIosYXXPT5zQ4CkHXLCJvaxv5uVXPPn-GJwZqGvZIDY0Pxsp4wDfsIgos6CSO111iyjTwQ3CZ_IrIE7gDAD3bgypvG1TJRvlEtgm3h4Yz7ZHi3kuPGvgwni79jjEkFV_oBnfiXhmWM2TFZGdCnitf3peyO13ni4QD2dzdFpLnrQR1ZzwQElUUdEkrfjZe8EM6_U_ZU7AzAnqamPQi5pom5gvAEK8RNqjP4Mr4AHvhkdhj_k3fQhvMdK8VD6q1hFsbi2KnQ66E0hp3P_YFc694C4QRJCXbvZk2yHeIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30608" target="_blank">📅 14:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLtFfs7gMHhI-drmrcd-2cOcVwCzLehu9hUlAjv2_2IjrBfxusjzwhKelPl2sSuFqSMSPN4aZ2eVCN_RfW76Ll0lCZUQec9RcrjRec4Sukvr0fkowZyY8bQVG2l18QDFyYezgTGdps1P_6M11gnPYTWa8YTkf-Xuuq9Vq3wFq8VVk8tj4ja6dSBrIw966Nq6QhKfkDDn_XowdJ5-kcvyecY7-dl-pKGVADLrPBSYNK4jIsVbgcogM8y4fLYZ2PacfRVWyejoU-tBZdOLPvZMXsGkxrOth4aKyOpQNSDkgl0aqnh2ygfAm-TuYS6r_pM6BRWwwR0Qc5tzHbAQIhZHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30607" target="_blank">📅 13:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGX8R5G_UABH6c32Htt7FwUFAvVeCtqjmsnDk5cYrFQbFH1yTsAs6pfTNlP2yX56zUg6xAjsS7amZAGgqJsCDLZxhYsuCtzTzmJyFJ69A2OrTQUZGkJefj5mnpmbkCac5shEv3ZLhTov4wiY2EOvOPy0uX7brP-F700fV-dGQb-HdKhYDVrKbL9EGbl7cRg9k9QDANqez6rovl0KijUc6N5xk3sj9Rm9U2ernLF4npiLEXEVJa37Wv4yFku22M8GZwY7Kzt56-Vavjp6hyE9KnRFZlwnzQnhMQj18KbkAY0MOgp2MPZBR2-sv_XmKIMfdGJu1p_8-Exam0ppEnG7Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌مدالی‌لحظه‌ای‌بازی‌های آسیایی ناگویا؛ ایران با8 طلا، 15 نقره و 9 برنز در رده هفتم ایستاده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30606" target="_blank">📅 13:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obh-s4IY1T1VXYSDqsq_Uh16vhv2U19bLdaurhTnn-1UJHD8XFef2Fk4cBcTxej6vTMvlWnvKdBVxVfwoVckMP6AGUYwbEeKcBDIOMZJZF1PNyPfdMh2u6z4wUUwqeQKXgTuCmnazscaijoz_KmHuO0I3rTjWZo_ODmMeZZqiwSZ8W5DZJb3Q3I3YFhalJRUF_TIiM6-Ci2YR6cwTK_FuJ9TFuHEllzBxcuPkEctQigPSZ14B2OD7JoBNXlOkylICcVMm9sHP7dzOLOtCY5oZPqqC0RWorQGtK6-eA5erhh5X4x0oVH8IZOGlJM48blE60UjXBVzU7ZJda_5DZk5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30605" target="_blank">📅 13:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcEVMlY5OwK2CphEUsfd5gdkvmXUwXPNRGjU_yXfutUxG05cy903R14GJRUG3QS2P8eta6NhmUVyIyH4wZmUzYyxQQ_wFoLizromJNYqh2KrO7K2JZPyESLRtAnpYZHGGBpfaX_1ueQ7qxKrnwIbKLTY6URoeQwS3j5dAb9EKEgGHMYbBI8_mjj8tjLeIYJvfnIStpXzufyxzBKQ2cMAr8sAoymy9LAU_wsKyDLSG6K4dxoSSVljWeZHzhjOv36ZmkNjpcyWkYKlmuNMTDBm-ieX4Q4nHX96FOUs3i4KrT_OoaOQGJhu1B0LjTtsm0YrVPjRFPXItQksq7f4gEY6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30604" target="_blank">📅 12:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH35Aq7ev21KWTdNbzdyB-LFCTjE7mxzUv9vQDPHbJo2MxPDhAwC-5mvFDZZSSALgbOnu7hvtdyj6wnpvuzZIwaIe05rIaxRRx6PCZwZ9znwtUGVRcywTDohrjmI1wLyF4YgyF8UaFSXhX_ByoHzAq8fqd6R8sZ-xl_rpg0Rwyl6eoku-At8PpY3bwrXheDtK818ghP-fFm-gdKfkr9S2-Iu2IWs3I8xLmOfA6K457pKn555LebO0km_HJxNRUrqJjuUw8LrGwt11NkcS1c3P6dH0vTsIdFYE10dgYvTNQBANA2Vpn6jC-XGXecgxObM6gZEM1IyRcDs1rlY3tBT8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30603" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu7XU8QMExjFxqfR2yzMR9he1PmEya8ZA7KyLmMXB3JRI4ia6bLBmtAf3uOE5fYvWwiZ23ojhBVp2aGWbX8Aiv0-x5tQf5FDO0fAvixNeUg_l-cQ5SeQckKw1iAJ3oMQGE9yluPj-_Bi90un5PjEo0bvzes6ynDU8D4LRr86ubbq-iBH8IyzE6AomrSU0bnpycwy2166OaPRpEf_Pkzss9KsREvxmUSfgsE5LDyah44RlJZtPbxYgfJe_vJnzS0Q3m0Ld_P92p-Jua3rkb3mJ_i_6N8O1QCLVm7pziS087pYNXQMj_GQa6MPTSqihZEAG7e9AO559sV8IUXys29Tsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه: محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30602" target="_blank">📅 11:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfHN6vhTmIVbEBX4jggk4FjTcrGgm3rjQr71yD0tBGH_I07J4rCbg8bfAP1bSSNXGW58J7GZZcI0XR-arwPhW16tCLGljddn4IsjOgUCxQZQP-aI5I7QmtfT9auTq7MZrqaiBgATJn8u5eDGvcdTyQ69jZp7mTQcmGNh8GYfxeaS3EOs6HMQuCZEKGi0_tU0_zvt5ObbN7sg5XNI-B-nhAJPxoK2LHwP511tU422nxUqeWg5QKZtJxnJsTx1ugOrew_Fpevqaf3VTg0CsN2X0Vm6Kn__AYIbzaXymr-aRsTWTjZJKcwSEIePqBjQ7CIk5_kG7uuDVS8DXZ38tLRUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇵🇹
گل‌های‌دیدار امشب‌دوتیم پرتغال
🆚
نروژ در هفته دوم لیگ‌ملت‌های‌اروپا درشب استراحت CR7
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30601" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWInqdxsj7LoX-uqKwE6lfTy12ADiNIgeicPGgo2nL1g7fBJb6wgmqTDP30kLUh6PgF09vyLYTITOS6W_KZpQtmN4WBplo5yMsgNkE7OuyC8-A1YaUcyVYKUzgT39HCRYHTcY6q6KEZwrGqv_KEIrre3BSH9fSOCa0JigSdcHxm1IO4SrXT-SYaQDwcK-aFV90XSQqcB-SGf36zmpmNUgUK62NIuZ2KXe4iuDh1I5_lBPyD3mAr0LieiJqfkBp9BhZwTKOeFIZAV8ZVlQGZypBrUXWaWZV6x01VXWEJAKOq2YW22PLJ339qDRDQxZ_boTZvzBjjMDW6qqPq9eiaW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌رسانه‌های‌ازبکستانی: آسانوف ستاره جوان ازبکستان از دو باشگاه تراکتور و استقلال آفر دریافت کرده و نیم فصل راهی یکی از این دو تیم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30600" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXDsWPS3uAepZO1xg6s9Umz4qCsGbMK3i8qAq_tD6k4OlXRYba6oDTyf23kmQHiDrOxR3XUYnzbNNnt7lvajr8Jh7kiFAZXMPsHv4aLxnAb19THnf7YSJ3wOF464Y1Yi8GTjjsRqD0LLfMoU48rOhu6eziWxsWr9yWHcvw-quxc1Jw4rFZOdJ1MOASkcDf2UxfqqjQQBGww0r-vpzgQ0tAkofelMSCILDY7hEXB0Rn2Pkuhx_gqQ5xonrY6dK8W01yPq_4FszY34dGybvDWFdZnaT1TdlpvL0xTKtkSH5b6zRW8aAN2w0SKJkPDzBTx19tdZIkqktpuFazrhp2JxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی از عملکرد درخشان لیونل مسی در بازی بامداد امروز اینترمیامی در رقابت‌های لیگ MLS.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30599" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30598" class="tg-doc-link" target="_blank">دانلود</a>
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
r6
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
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30598" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔥
هنوز توی
Wepari
با
این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
😀
😃
😄
😁
📌
بعد میاید سوال میکنید کدوم سایت معتبره
✔️
🎖
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
🙂
🎁
کد هدیه 100 دلاری
:
Sport100
🔄
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🌐
ورود به سایتwepari با فیلتر شکن</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30597" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7cr7SU-kFFevTrkD2N-uXK8Ee0Rz9ue0oxHMJDwKT6n1wDOhAYG7TodzVOkJK9K2_8Za0OIN2qYZFuVpZ18KnbTwqwqtfvgHwALQixfw-bkTvyGJFMMcuoAv-Eoi4JJC1qGO0dOfIk0IxwT5fDegnckfo0-imakjqcNsKyPTikp5Bmg0QEQKSV1fIRarqdKsGcZbT2F2R3Jx5UYp7vLSjeW_kSSbnev3p0rd5l8tLfC0N8F0CobH7_YlhaUCxWe8a7spabmkbfXGCJHmU9TPfY2fh-L4cllkGQya6tjO_aNkowyc0AmYZVP64QuYHwhz6hk0Zt3FrOAI9lhSuSaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
سایت‌چمپیونات: شیرزاد آسانوف هافبک میانی ۲۳ ساله‌ازبکستان‌از تراکتور و استقلال آفرهایی دریافت‌کرده و احتمالا راهی یکی‌از این دو تیم میشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30596" target="_blank">📅 10:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbltoWhha6JpUO9JfeJZ8mdunTUVujGJMuzCEQv2gbSrAAUf9PMSzrkrnnxNdKYDak-f_79OS8BSV4w35n7yPzDSeuVeUD42ZLCkoAulh5yxWC9BRW0QQW5QMV2-vPq_9jkuSLzr3HcPraSSRYe62BFTOZI1gP8vt_1kVPIaaA2AnGufogqYNwM3aAJiOM3qcbABcm3DIhH8IlhG_FJHZNqjIvhYMKiqc5Tc52cCq5Bnn5F2XuRhIRNv953vN-FXUqCua6QdDaVyOtwWZL-M_nnS-Y2IAvJVTCSsL9Z1IQ2M2J_ENtzWB1MPCt3qrjkvBNQC32dFpxqGskW-l__f6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30595" target="_blank">📅 10:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30593">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7swx3agQgIsCBJJ3C7Ge-yeHtcBxSk_Ewwo5GqiXy7GeP6i432sNUBp00EpLcvVtYBIwIfsIydAiFJ-t3GPH5ON4E0EYhUF954cXV_pyuog2GUQnheRPs6rO6PmWEdBZsnDTpkBw9bNdG98UVKYFBG7Ef40WOrls2KMDGYk8POaFivuNAh0l-tpghpte08y4nCq7JLEKAbOvtrJl10oOP9WMcccwi65Q8sLy2yQGRcLQZidUaV5CNSBBPzAAY29sfx_wW3aUIDlpx1DMhr7diDhuPdkOhkBO2w6boB6vy7tq9X5wDHxobGHbwz_qyWw4u9tVIXphTvlhiWj5lsEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=BMHEmpCCOfATuhb5j03gtYP1OK5UaKYQlZCfqU_e_Vgy6SsjGsKxJxPjNgTBetlNhVkfJwnIwgsuQQU-Le038XJAmZAdzYt6_T0ufYleJq7CE1Zm3LuAcfP90-eKkmZwbyWECR0NfrfDbkAEEgMxy9J2JpkqSBZvqducWr5BRywFfrhFQYfn9JjfPLSda3fj3pJ_IsjCbks0O-fLnB_yzBXzuuDrd7SkeogPC2qUS8PZfV-u_d1-RyR8z0oQ3Qx3Ia03dbe5RBgVrdrWzun7Vx57VmdJuPRS2sdi2wZLwXAcNzFpIfOuC5ETNLUB_nl3B2fgxkse1OWqayxJbSx4Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=BMHEmpCCOfATuhb5j03gtYP1OK5UaKYQlZCfqU_e_Vgy6SsjGsKxJxPjNgTBetlNhVkfJwnIwgsuQQU-Le038XJAmZAdzYt6_T0ufYleJq7CE1Zm3LuAcfP90-eKkmZwbyWECR0NfrfDbkAEEgMxy9J2JpkqSBZvqducWr5BRywFfrhFQYfn9JjfPLSda3fj3pJ_IsjCbks0O-fLnB_yzBXzuuDrd7SkeogPC2qUS8PZfV-u_d1-RyR8z0oQ3Qx3Ia03dbe5RBgVrdrWzun7Vx57VmdJuPRS2sdi2wZLwXAcNzFpIfOuC5ETNLUB_nl3B2fgxkse1OWqayxJbSx4Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیدِن‌اسکپیومهاجم ۳۶ ساله آنگیلا که موهای بسیار بلندی داره در بازی اخیر این تیم در دقیقه ۶۹ به زمین‌بازی اومد و دراون مدت کوتاه باعث شد که دوتا از بازیکنان کارت قرمر بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30593" target="_blank">📅 09:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30592">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=cgNbZ08sXySHD0Pjww9NWE2s61l9yoJj4pl_qEgYLwC3BESvF2YPf7SS8R7KmpfbU4TnLZXLrJ5qY8FEN5jHR4xsXL6IT2hLl-UtEVZczGQOVCyGvVn4FYU7iJ1sc-ygbLQRwLdk57jMwAv6xs0gxcs7vJOtiOz3-dZzyLa0S_oYkAJMpJCDMUcZUyTqZpdWPmBtQo8hjSePPYTTSiSHhtYIPv0dCk3HpxAWmcO5e4Esc5kYxAlBmRLJBEYH0ztxm8HSmH4mNBy6fXtrxeRDZrDi__UmHRRPBbIhGBSTBbt3iVghIzHqwHhmAtnYfBcKLXzkEw9PSHiLQs3n7Bvup5-IpGJ4lCoyAetL5EheuqAgHvtut3qFxNLzIAvqcQqU2psdSwzj7N5J6pM210IwSncvj1PL9QXTO35xVbzG_qydzxAE03kBfVTf7L3Vcssl8HpF46HQJxVq_keknJcwGrP0Xy3F9QzjjSz_UJV5OVohlCd7XuQxWVjVnH7PX1u5MgmTSRs3da2ByCiKOO7gjDXxLEKsyo29WIQstwcJcfCvcmyf1g1EoLz0nCM75UmYIw3EoP0MOfVtCmTIlSNPjvivmzSCOrcym5TkrV4Wbsb0d6AYTet1r0wF42hjxJDiVh3L_67QlIlhu3VaS9BLgNJSsozUA6HN5jjLVv9VlWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=cgNbZ08sXySHD0Pjww9NWE2s61l9yoJj4pl_qEgYLwC3BESvF2YPf7SS8R7KmpfbU4TnLZXLrJ5qY8FEN5jHR4xsXL6IT2hLl-UtEVZczGQOVCyGvVn4FYU7iJ1sc-ygbLQRwLdk57jMwAv6xs0gxcs7vJOtiOz3-dZzyLa0S_oYkAJMpJCDMUcZUyTqZpdWPmBtQo8hjSePPYTTSiSHhtYIPv0dCk3HpxAWmcO5e4Esc5kYxAlBmRLJBEYH0ztxm8HSmH4mNBy6fXtrxeRDZrDi__UmHRRPBbIhGBSTBbt3iVghIzHqwHhmAtnYfBcKLXzkEw9PSHiLQs3n7Bvup5-IpGJ4lCoyAetL5EheuqAgHvtut3qFxNLzIAvqcQqU2psdSwzj7N5J6pM210IwSncvj1PL9QXTO35xVbzG_qydzxAE03kBfVTf7L3Vcssl8HpF46HQJxVq_keknJcwGrP0Xy3F9QzjjSz_UJV5OVohlCd7XuQxWVjVnH7PX1u5MgmTSRs3da2ByCiKOO7gjDXxLEKsyo29WIQstwcJcfCvcmyf1g1EoLz0nCM75UmYIw3EoP0MOfVtCmTIlSNPjvivmzSCOrcym5TkrV4Wbsb0d6AYTet1r0wF42hjxJDiVh3L_67QlIlhu3VaS9BLgNJSsozUA6HN5jjLVv9VlWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30592" target="_blank">📅 09:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30591">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=Zku-PzebW4-8Zg0mRdKxszPjr1lFL0uYM8Num9kGnQQKA3gIWhojb7g_m_swM4R7hXZhRhUfmQDjHim-n7ZvMcK0R5-wfximLq0KOs4jRmetUMODhbiQH_trQjZz4poM9sJSxqA8GfMxeqLhKjlIR3DFfpRage7KYa7AG9yLqf2dxJQTVuo8GZYH31VdznqqZ03O0E-6kWGh3V2A4UGaqcfj1ij9DoKF1Lb-wdebYB6tigNyp1jGQMZkFMkaXTMNnz1b66t40jWtprzPUZ6MNKZZvwx0lGpf-o8jK0sI6apzB-kyt7flhHppiC9CTBL9-WSEypM8Jqut67wvyr-APRhTjDUPHwWUOsrf_BQj2BO0x_R-Nsfxz9u2o7wnPfTxk4WuRXvnTwdu7Du72IpA9J41O_w0kO6Qy5t9NYvWGQh2LffmFqye8NCP3QA8d7g6m0LdGg357_Gj-vYzbP7qaT19Ai_8elYb2-cu4qtiQOJW-rSpDOf-8TOdURijSdmQ0Me3V-F_Zm1jNb6QwnRHQseUh4VN2FWOitYVpYvQMna3BOzH4RokgLXuPw5s7WWTgPOhB8qQCC5dEpuZGMsWjEcYxZbCfmkNCbvY6KcrUyvW5XDcw957g2zfqiPuYqAZeS8IANfT5jT6oqXncyWuH8YDrCBQY94XbzbWSrtM0xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=Zku-PzebW4-8Zg0mRdKxszPjr1lFL0uYM8Num9kGnQQKA3gIWhojb7g_m_swM4R7hXZhRhUfmQDjHim-n7ZvMcK0R5-wfximLq0KOs4jRmetUMODhbiQH_trQjZz4poM9sJSxqA8GfMxeqLhKjlIR3DFfpRage7KYa7AG9yLqf2dxJQTVuo8GZYH31VdznqqZ03O0E-6kWGh3V2A4UGaqcfj1ij9DoKF1Lb-wdebYB6tigNyp1jGQMZkFMkaXTMNnz1b66t40jWtprzPUZ6MNKZZvwx0lGpf-o8jK0sI6apzB-kyt7flhHppiC9CTBL9-WSEypM8Jqut67wvyr-APRhTjDUPHwWUOsrf_BQj2BO0x_R-Nsfxz9u2o7wnPfTxk4WuRXvnTwdu7Du72IpA9J41O_w0kO6Qy5t9NYvWGQh2LffmFqye8NCP3QA8d7g6m0LdGg357_Gj-vYzbP7qaT19Ai_8elYb2-cu4qtiQOJW-rSpDOf-8TOdURijSdmQ0Me3V-F_Zm1jNb6QwnRHQseUh4VN2FWOitYVpYvQMna3BOzH4RokgLXuPw5s7WWTgPOhB8qQCC5dEpuZGMsWjEcYxZbCfmkNCbvY6KcrUyvW5XDcw957g2zfqiPuYqAZeS8IANfT5jT6oqXncyWuH8YDrCBQY94XbzbWSrtM0xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بهترین گلزنان چپ پا در قرن بیست و یکم؛ لیونل مسی فوق‌ستاره‌آرژانتینی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30591" target="_blank">📅 09:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30589">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZkg1Qt2UKQ68ZGjrRwNFT0_LcrLv7VBRYDF14rT2q5RCaMWjQrOf9w5KReiL0483jDRgwldj3e2fDontd5AT0dj8e7S9ubYSf8p_r3cJ2qbsYTaKJ0Nd35RHn9N2XeRSISMX544EPVjJuM-wQRCnYI2rpJfapdBAxaGNorJg_NEsZymuYCGS-5_fJFXAAmWLHnWP5lddOrG77rMU9Sy2b3aKc43adIVqs15G6WsVFFVnmePnYdPPr1J4W1qBFoiInZwjzN4HDzzueFChDoRBsvloF96ORvbBL4sfMztVQ0FVtkIYkojxk5vx0t1TphProXTOM73EZz6RWseJmocug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFbnIep3m7GQkxWOR_p9TzZL4pUC_8NmdmT1HHR-bzMn6r6SJvK03C8aPHq2gsHr8S6NB_j3Of5VEq56A8xm48JAGuKWZR8cKZgv1GHx1nPxoWlDYP-SMd-Kkfml7MBaT5xK0qHNMAFbvoJ1HLc1EwTncCLS0yO3kOLxlqTjJr_i-NqaC1-PuivtJRhzl_jjO6n6Qbb5nFa5wvbERUUgIZic4sCAO3w5E00IpRHoDFFND8z359WMhKVid7PX-8ocWiwt1mBnCLw0J6PmfVwa4R7B2eCDWpeC1URI2NM9lffz54c-9dq9e52ysVYQtAFy9KLlXqlVHR746zTnW-nmJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30589" target="_blank">📅 01:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30588">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEuZobIbuvAkDge8er_TIOg17Ab_68XmlzwTXxndEkkskHE3Wf0i78NCFCh5OsA3uvW5qIlfE4rsp5rUgDgimih-zCleNqMr8P96jen4ksLRGnSTmxzMm1bQDWoGHBqRuN_LU_W8P5eUokQ4T4VzYqfxZo_x8fLQSg5a0s8ikqke3byuV2u1JIhdCUeXWBhC0YcNUP9r2dAzhwRMyE9RXmiZ2kTKj-q4P5iWoITiipUndeaYd5P0ad_42H0QaGZAR_oTAScAdnPuyAxcE3R8grGmrux62Ck5YdlcB2HOMnHRodxFXX7RZVq-4A6x2OFaDlq6xHhwABk08jjRaDgjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/30588" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30587">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_vXrHhPkKH8bXHmUERh1VY9IhPD3UZVJGaUCy7Xze7uDsO2Z8dF1ot14-hTOWlsJNh--RbE6P-rVZ_4iH50e_XAr6M2cOAmuxC4pitRZ2y8Ujhgw4X32mBoV56ZU7qocI4f_XeFF-kcdkE4jEm8FDyR4ZtiDG_Mck3Xi8EsmtN8rtQGTEB8Wr066vP6kZmhjKtiN1WQSprEOFv6Mf11uhcbEqiZviJohLCowkytNw07QCznWaiiTGH8BhAdWU_rvGImjUMO9mg7LNZ1dOQenm129sJwT4Kb4ebnlaif7BrojuHxo9Cy45vEYsWMyIaJMl-37hFqty8vMY8JsDEqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نگاهی به عملکرد و افتخارات شش کاندید توپ طلا 2026 در فصل گذشته فوتبال اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30587" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30585">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQizK8KtCm8AS-dodE0aFmwoMAbRmZZGrpKpfxwdFcGNr0CZO9Jr8NZxw84qar1yChBeXLzEvzEcnkScMDG5A9BOy2nXVOvshPcwBQOkLOWTPkibVbjdJkzSi8sn5P5qtA7VbowEhaCZIdBa3KsLkDynxr_tLuqYAGQVtDVr8WrorzS2e8oaQ9_eRf3wI14xTQqcDR33NpJjXHGQMGImBEYC9Ms1-wNTQYeBx-UiPFoYqEUSucKwgZDVTmJQ9gKRFxMsWVuLgAt3P1mANiylU45Emf97AMZ83tnO0pTgp7CF40OGrrw3oGbgR4TJSOwqqUPGU7l8m_jIQlsfwhL9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌ امروز
؛ دوئل بلژیک - فرانسه در غیاب امباپه و رویارویی کره‌ای ها با شاگردان فورلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30585" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30584">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJHjc0dBNNyB1ggTrzx_Bzjq4t_qwyEwu3RLECUVA-V6dg64tEWFpwmGqSAqOU5AK9dO8Jr1LPsUxlqaSu5Q1FG05Nxx0s-KjxAlkbhNbm-b_DtCv4vtVhe4Yea5W48DWRVS8Rg35q1vdzRnhklJV5IIhqzJ5mxkeBAwfA_bEpRoPsb6PtMEnQL4XVdsM9SPqJEVxrmPdjJLz5plMcQsdkb6QHHgA-Jpc8GDEOQt5FIpaGDNHKUmYqyYjUmecKYRZWxCit0xAG0SYI0X4V7FMe6JhBy-FLey-2wbsVEIRAtaFsfqM4D3x8jxxlrYvHjEUSSf0nbHCWpC6w39_RM6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
اولین برد ژاوی با هلند و 6 امتیازی شدن پرتغالی‌ها در گروه با برتری دشوار در خانه نروژ و شکست عجیب ژرمن‌ها با کلوپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30584" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30582">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30582" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30581">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLYuyroQj9KK85b1PixDkR_bkH5yB5sQJm_eiaHOKJaz_8EQ_dcZnh6SmqsRg5hImfcwzXzH0kbAw809Ul9hnUkxoxIK5xoloTEkUEA-Puhk-FHL1onvzDT8GwVM1JQngsUybUtjtHkKJLgYInGBycJOKMMIA3AuFodRH8VjbTInlRZyPLaK7Ws_LDgqmjddxvkQOVrRL7b5IRR1MyDew2MEX_-MpWtTwpExzffPFZMBEj_zkHku4ls9Bj0ry2jRY6Fk9YXy4ceBoY_L640qpicYEWRZVO6yq8KNxmSfVz8JlV5I0KG2SGq88g5VbYBXog_gfOHVRVAHZNsIOzPTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30581" target="_blank">📅 00:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30580">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCMctJZqOOBIqpMS6VRlYi5h-YVYShizw-MuIKAsAlI2P_O-cQMFrkyg2dXYlRAEzn8FzTbGbYUZhwD2KjdFQ04U4D6fU845xgC-HInLvRaenoP8YR7MtWZwTaFvsDAVnuuNfcvnCqdeShFNNJ8VrqxjRGUxwSrzNthLl804qVx0E8m6dsRn_51iY-XZb977t_uzB1q8uvlCEJNWBDe2Ofl8fc4RleQ5KE5MGoH1_GVNzuX_lRjlhahM-xdQTshKr7LgjjjAfttPIr1wQKE1NvsnoNRB8wNxBTfzE7TnGQaHt7tkuAPfYzDR9-m8IzRJmGZtYyJOrvcKssiPa7yM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی پرتغال در واکنش به نیمکت نشینی کریس‌رونالدو: رونالدو بهترین مهاجم و بازیکن فیکس تیمه؛ امروز چون میخواستیم دفاعی‌تر بازی کنیم و کریس رونالدو 2 روز پیش بازی کرده بود تصمیم گرفتم امروز بهش یه مقداری استراحت بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30580" target="_blank">📅 00:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30579">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtYmNpagN1u7NBb5U5njcu_xce7cCp6gFJdcsLM7gWCZZvpgTZXph4avLBw7iH5pnC6-_K3ScsIyzaZrmmtZoIUlnc0xuj1ttih7grkx3l_j1V0fCdZvvD9HnXaLd3UD26NM6Zi4YvSCqNR3VFvsHCNWwktkj1JWX1uOBWVpryQJpIFuDXYKn8UluvdNuHv7MZ0hNqOoNIKhVh2Cwsxz6-x90yz4Xqo7wi2nTzIXgb-9RLsB4dihq_dSqX8qfJq5zerFM1mSofDyAKugc8xdBrXgOgTUdZ8oG06YfZXNobPO7zzFJBGknS7IeaWGPcS-1SIrFfm4kFtCCTjuTinv5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دوایت‌بایکس‌فوق‌ستاره‌باتجربه آمریکایی که سابقه بازی در NBA و لیگ‌ برتر ایران رو داره با عقد قراردادی یک ساله به تیم بسکتبال استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30579" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30578">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH4tjfo72-YD1Aoskhsj11x_uPtmZc9rY1tEg6VKpHx7ogcd9Sev8M7Z3g2o29-FEt8XIUuCzMI9uQk02-xEl9bF1PZW1_TJ-Sal5gsbNOOxDYyuNGkNx8gyyp0opNNLCILh3jqV1V9ZTqmCOjchhWSzAVOkA2tvmumDkxNQb7ctQpT0pvnwCXxbx4cdBpWAi9GUe2HMEClN7oXOMFaS44x4oix72EL6sNY2XstIfnnK2BIcRfE30h6iDUkLXhdXiXTXK9-OaD0kUTDduckhNMZDLrYqmnvKhboruvHVkQhmd-a944cAxCFmXN2uJX8jvxGyvaAMWUMQzDj3SbMe3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30578" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30577">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkFhZDmuMKPdrZOZTKu0e-4gvgBZHoAgp0fEhD0wMDE5sNHBTXwXGP-l_q7aB4vq36kWz2dGyQQ4kUSldcyqzpza59ZhAs59ECWBdMHh6hJXPCi0V_Lf8-buvzxf7dFeJUHyBw1mHTmshdKdI9k-3c4__HnPVoVCwyz8BJB0PYQOSkL_1Qw7Te9VuIVMJKVwuEyOEjPXUYqdTCrqJnyhpZ9E4S5COAgfJ55C2uMZv1aDcoHKisYo9XyY9pOl7PUiKPEZ9KVCrQw209CQ3TlEk6fJKVwO00fXxa7UNaZmXDMeX5b7cTGok163l64-0h8TQtrU0NvEcBwWK3t1qXExZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته‌دوم لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی پرتعال
🆚
نروژ؛ کریس رونالدو روی نیمکت پرتغال قرار گرفت؛ ساعت 22:15 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30577" target="_blank">📅 23:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30576">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqb_pMY4bzkfdQNDtLeujbr639RhKyTZBKt19F7kusXtbpdZVVDFIotMcfNpHPTK7VKCc_IzOKx1Lsnz6ASZlrWDQ7rGjQb8xHdifMzDaQf6e5p7zde7IwlW64hp9BIqO83vkli2uQdaGvnEKM-sm74H9RYtOBoN9auP2-FwTuLifJRPUcimO_cQYNaTx_X0Wyggg22wpfWnnqJHWSiw4qU3utgrY6M9BY_ExtIhgqcAurdgTxzTcKs94fWH4qhH0rIyJLgoVDM5qbgzrYSVVPySFABu6XK4psbyFO2F4kG5BeWDLZNzms3x5dP9k68hxTDHyWnXM1LF_MTfA0tRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30576" target="_blank">📅 23:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30574">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B18NjLmlYrdKlb8--lMuIjd9sm74R2NxXnG1e5TgzC2gdsZZJZ1CBkjC07C-xJH7iXalwwOeDPeptTwM1WENfylxCFsxEWxoCCi3k9-RzXgvTEgzQzmFIJrIOpg_UeMA-XLUur6XKA16k7HvRHpdwvDBMnXwQj1cB8VZ2K9ey2wEwEhwT3RaJK757Nlt44x7phIaPRY6X0vmySmW6bmbxSpCiH-cZ0u6v9aIsp_WNUn88EilaQ8S6KC4Ty696QTR1s7AA0CczeneKeSIblvhYcWXIm0XZ2iH0p23fOkXxC8iPVcTu00vOxu9qYnGKerRkdo3I20GWJaqTLX-IFEQzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtIIDzsy6qjcFVAMaE6rbl1PzGg9RGgUGUxhDGwhP3K4cumjmyCgGatnmY8btYBA9BKD3-SDRDSwMmbvCmlJ5gPd7m2orLIX4rIKQjPfUrFWrlCO8vvTaDe7pFz-KvUmhar8mi_KAMVYk8EJoi4AS2G50fwBhyAgvo9Pkl-tJ05u1mHNwtI9OWNU0KQ0vgvODaNLNorjbAHx7zFcnDEU1Y4ibYjpU3vmD2CTAPZl1x7fjFb8vQje9LqmPzKZ9U8FvgKomvuVrnSMg0Tusa0ppcyK0MoEOpm-XTKFDAYNx3YJ2g2otaNzghmSP12Nl9bhby3DHg-kz9-EsjvTeSF8-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30574" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30573">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5bY6hkXmq1NBgVcwByPYJWKrxRgRAJDCoIWEvScCG3mqq2SfN9IY3z-Uy0cP9PEiJxWYQAlOrDM_7Ngct1kYYMExQf6fAZSM7ezP2aeSR_pqRKxqVlObuynL9Xju6Xfp3UfGTDanvZduYHW9oRkfq3qh4idZhqFSOwW4hZ3vfTmm96Uyf_8DV1TgXw9koAjTWoCq15OgpGOu07k_n8uHMx9z1z2zSPV7tX0UrEKzoj6FprNn0z8PDBBHgDWFWzZj_ljwia30zh8lZb6nFXn7lTXpHhfI-x73818jhekzNjntePW9xTx8KV6-x_1oWGvciVX4XxLe6T6cXVnurCGfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلش‌ بک به زمانی‌ که مثلث‌ BBC امان به تیمی نمیداد. چقدر زود گذشت دوران لذت بخش فوتبال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30573" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30572">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=M2nfPBA7VhRET77egIa4S1SZSJM1OGs-unb2rJOcUBgotdr71c-nFWt72C4pVUgE89YVBJtWoXsqjf2lri4KWTkk0R1r66mb6e6zc_8qv6HNJRc31ODPRUs1zSYY2HhKeLLFSp6a_WF9vsTbO-FZKrpjdX4WC9SUn-RMdbm1AcJoGT69rCFtkmYHzaIpQt7r21g3QDzSeE1_2oY4qoWKt4y78TossK3ex2Rfu2OnGzo0znjD8mJKagyrjI49hJzLwnfqZfTrwEIMqVrtbs9M1InXFmSrvwkTyYVMT_e4WGxZYrQ7ChmpaRLz72QiqTPJ-d3ZJoWfKC9Mtjke4vI0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=M2nfPBA7VhRET77egIa4S1SZSJM1OGs-unb2rJOcUBgotdr71c-nFWt72C4pVUgE89YVBJtWoXsqjf2lri4KWTkk0R1r66mb6e6zc_8qv6HNJRc31ODPRUs1zSYY2HhKeLLFSp6a_WF9vsTbO-FZKrpjdX4WC9SUn-RMdbm1AcJoGT69rCFtkmYHzaIpQt7r21g3QDzSeE1_2oY4qoWKt4y78TossK3ex2Rfu2OnGzo0znjD8mJKagyrjI49hJzLwnfqZfTrwEIMqVrtbs9M1InXFmSrvwkTyYVMT_e4WGxZYrQ7ChmpaRLz72QiqTPJ-d3ZJoWfKC9Mtjke4vI0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این‌صحبت‌های جواد خیابانی درباره خواهر ارلینگ هالند در جام جهانی در برنامه زنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30572" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
