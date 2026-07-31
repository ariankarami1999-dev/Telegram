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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 608K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 06:17:17</div>
<hr>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmnGHnr7PbmQ1wVrNn809iH_X2zLXW2LWxEi8wL8nK5_d-2XEA2vNahnyiOl9n-atrauq2IqhjDURjMffwY62TXXpKhCmz26KlP62Ho7V4_qqVKuuy0au0mHcqmZAz1hDj44CXUjUyoGOz-E61LFY7L_cAOwv0n1jK8jdczaSMgzyxYO2xFZPPqdLkXP4GA6gyPRWoMTa3BbgNhKNcnIsw8GKm47-9-msu48IhNRtGWYp3DMXCQ_dVhJJU5mb65x1x0PUphHzMZBzEiBMRKkRficIDqO2mD3beM2tJVZiIVOPV_LzYukWuHadqPIFdtuwLoAlXDPUEVN0LuWi4lB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLbnlz72t8ZjFqZUgCMwjYmEeggfC5xnvGDDXeMVBcdxx3QxZMWR_I8GORrLrfZm7EAm8SBWOOAAqP_9Y3M2fLy7CsHZsOWH2h7BrKK-4qR4i8edGes_7k20ac9Ut1nIwtQ0NuAHlIeMJmrgQS98EbvkFNcSM5To5OCNNXtHJuC_6iHmDXgec5xcAQk8HmUnj6iLImsZvLEcqxqTHwyqZDTELJFn5IPynna9jgoX1AwPpUTd1iNARBPDsANbs76TMlKhQzMByNNCUbBtWhAba9qiZkz_f0j5ADOv_mlIKnI-QSkwVhIFz3CIYbguY-NaqbpiV1NgSDhtTogwQYySbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpG5N-ZLDcL1B_PR7KwjAT-z4dil1syubaox35gB_s6lkKYofpjHAj1c1GVtIM2Vsav1iAIn79s7hW1up20iB4GQse0SKCMvcSXgnwi1ObrNl5vzDrBDtR7BOo-UQu_g4uJ6OM4fsawrSWAMEN7scdXHkb79Te6OnfywS0ntvp3-5X9H8jeSx-Pde4ZV7ZxeJDZjwh7NvPBrpO3MvoY4mtHoinTXp7QWB_Z3-JLpu8sxsN0kZPNg2vefSzu1swTjFFkdQcZNrYeZEkpKcR81r3c_SNaR--JSgcPXHd_6V0Ues8F356j_RQAXZrXc_VbVYnqocQnKe2lCeKXc2bCweQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBO-_Kwd4Xgzz9gj-f_SbV_bCITtVJuyDps2v4mF58J8gpPxUmAOWsKni0yv_LCFae5WL5XIwVECmSWceRVh3FtfPZ468U0pmhFKHqmuQ4e_OYfMEDWLLCkcC3OWb8zWDaOZxG7_vXlDqOat_fsFQD93oqTtnGHupcGvPti_HwDRVDOCxaqykd8TwfGiDulAfS0tIfl0aNJ4fXwuQzHkmrhALryF2KdH3Lnss3SE01HFJ1jTuEOfUeynPJDzm4EKAQ0oZzY2r-hspihrIefNNADOpY4N_WwMrBrnDkwRNBv434wAU76HrZ5_09pyKoBeG7pTcV6M0pSsv_t1gUfn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF_CCyMsZL-6p8RmSh2qpiy1gGFKMrYaQro3Tpw1yAWJ0rWEyajWQMapsyeZXq9b_zAxTIUQbj9CiB1lA7JAOrAgLYJexevucrgYkGjtuFoonso_BFpx6ZNQYeLka2CkjejLkUc51tXA7vMcQ7VnqHjcFYcsek3asFr2705lx4_5AiSGd9bWWFhfJvSQErdCSBgnVyAZbQ4HyxDCjlCAIupBTJwzHk74wjqFO9rEmtXyHmLfXdR1P5sM27XbZqePf3HQ-sxp5q-M1zSWAmNW27jojkpmV5p0uufSytQf5KbazBcuKy6C1ijtJ7UJWvbowktswF64jQUknq40GOhmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmMVJy9t-rZ_na5e5Rw95-kaFWNvd24Le2PPYJQpwlxjJWeqiLjZe6Lr1J05Ww4GztNtmnLM5A7pgJNe2q00OW24Ggo63V3lj2gS_jYU196fOwH0Cx91vHockfm3gwvLHtqYSWWhJzgwwBbT0YGSr6NTdxUDltPx4ORmUPckaooo-jSApis6UXod_BhD9CEXrvxHhe2ziriWoSHQxjDw3lGdlDhyuQiWVexB0Xl_fwzrU60X0EVadnpsILobOg1ybxJiqekKAmq1Dx7I4OPofbeUR9rDPZR1hXYSNO4ouTBH0sw4fnUr1qeoBrvi5duSx6VW_zubbKZjZFWcczwf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/26851" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLIuunfxjuG6ukPRieIfnqzIYpVncUqPPAD55msckHLO8f-907knZycd_UWMVSuC2S-DnIkzLgxuBBQi59QVnkShUatHr63do4H-ZS_M8EOVg6bc80YtMKXhPbw3-hGcK_wzy-gVr0v4DxVdKHGyd0fz2w-iEF4XiK_IeE_l9yVb-2ponoEgMRNLnlUdjuKOpjRiz4VnPYzJg3YxNcF3mDTIV1_LAX8Z_BdLMF46m_heidGgJtKk7cuSOf5Zugx2UB8XDbg9J5k3gX76zzQZ1Ajn9t5ZrqBxx52pmjUAIl80yyeLWEE5Bm6Lk7maaXfNgFQpiVQM1OeabCm5afwLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wxWjSvo3G8glKAeIAAdEWP8A-htiAXQVUrvPS486QpjDRCbRhdMguexT1bp9HRGoGQmNFp9OzA6iQXOIwxzaJmvSRFk1OsnrviYlSD0CB9mtMHumOdK4lEhOMoEvQI7K2X2ckZ-ShZfLWZzzBsK4ViHi6KiLfwuhXuvI__ui1oAwGsVx2C3UYd5i14qgeQcl6z0SHcSQoZHzcmht9HNOO8B8ODs6uK0oPyUL3OenNMmKcN9rlPWTzjR3grn6Bn0DoQlPg9nMwpJIuaiM4djvR3B_ZpURzBFg7g3s8DLkwunJx9Qlk0D7uymtshU0Sk1VQ2VVOapb-N6SxQhGbS4Deo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wxWjSvo3G8glKAeIAAdEWP8A-htiAXQVUrvPS486QpjDRCbRhdMguexT1bp9HRGoGQmNFp9OzA6iQXOIwxzaJmvSRFk1OsnrviYlSD0CB9mtMHumOdK4lEhOMoEvQI7K2X2ckZ-ShZfLWZzzBsK4ViHi6KiLfwuhXuvI__ui1oAwGsVx2C3UYd5i14qgeQcl6z0SHcSQoZHzcmht9HNOO8B8ODs6uK0oPyUL3OenNMmKcN9rlPWTzjR3grn6Bn0DoQlPg9nMwpJIuaiM4djvR3B_ZpURzBFg7g3s8DLkwunJx9Qlk0D7uymtshU0Sk1VQ2VVOapb-N6SxQhGbS4Deo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol-Wjk_y5vFzpU1A4ces-dPib-HLPV81VPYWQuRhPkLVOzsRFMQswsLodUP3dLd-O5AMj3EH1mOQmuUMXXNBwsnlxgyuYG5Sy6baZsruG4LWISIdt7hISKg1CcE_apV2BkNofsuhLTMeNnEjYlOQ1srYXQGRHjRyHQtJ9aWNn9TLXLALuWtbV8RSJgklrOQb57Dq7oseiyCLhFsA626tFo9mWqmjM3u2lfRhnLFbyTatdX2eBiYEHItem-GrwPW0VtZuwdizBVlgCIXJoDXhwbc8auufwahjJqYIvnhGIvBb8sRt-mZgSuXPIwverdSSp0V-1Prk7vbFR2ulvPWrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Got-z9q1q3fd2Zi_UQOealoB_yIwPkPW70DZJkEgTYCiOuCzq6ad8DDrHczmgsBA5WOTzmlaQ5Cb-Yuqt0Y2XE1WkzDdvTwxdWU9B5NsZ_hWVHrS0UnZV45Bq-rn67C0KgYwOyzMHTpMGeXxQcfxw3z7_mcpHTgLN5uoowYp3ftRH-GtO035k3hjj-6izpvx2roo577MDDQZsVROJCS7zZSmPaYyfBZHrZKqWRklSEpbYB2bzmHbS9Hm7t6tIoDuWDAF07TaPvZeFcD4Qc-JsSTn6y9reC7FLKJSFfop_LIFFeBbbwu9rmtFmazWeyKzbkbzKdPhLSGeFyQnOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBX6P3XQ6KewSczJlS-jsyF6bEpG8m2TzqmkQYog4c5i62xKjpXy7tBvRZsihsemx9cQEttiIG5hUsXVGf1MXfKTL1aJhc2iSOI8fsx-O1T-afVbGKWEL_V51LBpqw78XKhDZcVKORFIXk9TQkFurTjA3-nbghei9eXUR0_ov2S0DDCOzM-9tHP4Py-b75n3DStIn2JwyFoGApXVPeTHlMaY1idiR6ElKCaZTNy1rsTBnSqE3AvNrJKdzhQeyQYXhxrva7k2uYu7hCxYpO6BjvBnKyblgt6Xiq4EXUFdgXIqNyExJ_IN82hH6QAkkBk0Ip3Udv4uaG9RdAjllG-Rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKhPC2kTVuKNFa5jO0OCEaIdjTqE02sZTArXVAT1S9ZCZRNzsYvwOYUTWxa4k7Uz4Me2Wwiy8RDqtshNROwup55Fi2YBnHz0L4lUfIx9yqFkl1X71Ci4CNtRJAEbWuetVjQcgUspOzQV9_dDb6X_mzBL_0qSHNW90MES0eMib5SaABihrzfJDzly-T4eSiHvC-IaAfg_jYS4wGLrNEwBUgyWFqJrXZNubtNAQ3FjuGSjI00h7KDvmEOGrdFZXq1qaeZ0N0TCbV_UAC3knjGRt98RNtZPNeUyEGAub-A3RJIEQiAqBpjgFpdGEgjZUUA87gUBjxnWk5WT6_jVXCdDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eniSSEHLNdYSVF-gF9hB-pN26jmHKmTRa0sGdcHyr4bnqH6y6aan1AmjeDcmGSlKheoh8XEK6SqoNNsxexePZRU0DKhgJ7eI__ZaswUoj2nnZaNHvPZ15Jj9qnEZmXlRNrWk9oq5nHEpoubYvDbNRuTw9m1nF6Gso_tmg67dBQva9j35GBlDjXlAn7O7C67nTcbGhll9b4R_3IagbUEc09YYGPkbJjarE04wVceLz-69k41VI6qTCqyp1-4S9nMHZS3NOQFLfsnhn3rDkRprAf9VKKU8CrkgwsuanzCblQS4X2zZbnjODxVrgU8ngQj9EhuieaY47G62pW6_z28Xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzI6gH2FyOllQAcazWbfOsqx0Xp-gqRycyCE62_LbLLOv0L2GWiRTVmGuvzgEswn8axgSIvuYsU4IZaFMgV5IwwjJCOLCf05e7PgRmHS-s8abKoNSLfOAoe-YpJ1K6WGZTQvr8NnMoCfU8gFHPibe4s-Vu5nD92IWmRicedaAbayQrFFC80tba5kxrIKTol07UknIohBSfIaRDnqTymZXi74PpJR3ncMAaj3TtECkjmtDRNuaeIBjhyB5zz8SyoRdjv8YXGP4dWNTaB6wERigu3AvFhlwulPdKbVis9C1awFiRdBAFOppjyVNffsESvpu1x-bh5nFPubPzItiYdeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POPEdQE00uvwXeMSQ7Ki6XrKUZlG8qViZMyRQX3kW_wO2wmZYrdYhUVW-Q8cWv9AvMjtIDM_b3pqcrUW-g-0afTtv3qW4YNQwDx8sx2FOzjrC9oDlmK5ydtCCZ-pCqtlcdTSnuUZ7w7ftQWv06lATIcBADGUIjnjJDVuXfTolkbbvF2g-AUGb4S5u3uUnFCegjLYN0aatgTwE7ZVq5AKdI9dPkkiJFBqY1zX6KgS-DKHK52pyGio1mt8jRGzbNNnrI8TuQYdtyLzMLLzRcqLSVI61Yj8lCjrKhzYCx5yp4AK3KKZVrKDf1rfkWw_BGuc_GLeGLc7M8d9A3A-l0DLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqS8sRrVRy5vrVYFO8ANhfqpRkWS9p3x3-X4KV1BDmOGaESKaZkXr5edto7gGKY1VQrRfEoTM2sWVZlhXCVX7F75TiwPOn8fU7HDYOgLPbjmz0UmH6tzSiPD326MC2RILGFyGQUe4thglDrz-GLTsdRzsNfbbD7XiSghOHUiSj-u8uyzrYUmn4B5pCv5vaO1EQyQsQIpH6SghFVx4ZVL8179C83z-TfbfBveWFRI0QBHb11Vgx2AkZrm0zX6a3-S5JCFApSbxIdf3oxmiUDQkHXES75NbR4Si_6M1GIdCzmCI6TmoNicd8MWNWseepCky8idqt0JPxBSxCKyMbPTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDNLBSHn7CqbtP-LJH_IlkL51XrLIDj2vIldPRcc72f7Y6iRcr3nTcOrFRS_RSyN8TmTVvxhVGEXT1bpt-gluq1JRuU-mFD1DHfq7locnaiw7tS_xI3xajtbkfS8ZFbMLuDkryoAfggaqJGEZVPqqsNg_zlAnRZ6IwMJiegsDY3AMKIixAISi5P_hi1EF50OGOna4XFJnANmp2gHtWUBCtLPxrTReqExz4aVVmrReHwx-TI3yD9FTXUSEZ3DN9oDWr1PNuW2xDD1Vw1YCYfI9mkL0Nblq3S6txC81co3loGeHatqn2sRH5oxR4zBHXe-0zp2VVX_p4ZOCBk1i_yzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgakwr1s6-mQ5Y0r-t8g2SiHGm43u2XGxsxwnj9vRVAPP2E3TLPmb9ZwzzrK0OCBQKvFOXpy6cNIhwVDAXBVjZ-W0wrDn9-v3TYJSpuxFcFe8sUFlP0dHY-d9s4PHR2dD6na1fHRkM6nF9kNzimcGqKo-qNzF9-bYpseCeNJgIcrezh7gn-pS1cCANOEiBpYoRDVTeueQBtFwowcjqGpeGUUH6XzT4AI3OAnO4lprrsERZgT5QAG2lmfm6OuJgAp39w1la8Dme6d51aPkgvEXEdXM7YbKKGmd7QtZxhcFAiTpEZS2OwlfkjKPQ5VRh1ds5_-s5JC-eFMTH3Koo5LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwaFqYb5pvwYCpJJqiQg4-q589168mhir3aIVBv9N6gzxOtKmRWdETp0Zt47Om18aQlHGDk_AD1JkagZq1GmLtwUNo8DA1FSzUUpwsVWNfDM4zNt5OVpbn47wZh-1oi6PhRU3h_CbuX21DOsK4hxGsSlzw3f3zASk8HgbfXb6cXCBNBmOvmZU4i8NHEQs221_ABDHrt9Mx01VEkGQMRrtcYi6y2nN2x-pX9OYEE96oISeUP22iZC9nWD6jnmWTRd5JUqvQwj-nDfzUIL5m3X21uOBRrht0ZhWwvtpMm4h7B1iNwQo3buGDuiq1_CmsudJNprfVlzxeiy3uAGQOSPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN-VoIX_PKsJKYMQnjmk-DJEJN5MjfVjxGB12oMT698r-NF2s89FUcTQ2G0n7Ygyo739Pji1h-IyYa2y0izIqgAh5nzRMoOOECyBknn8PbyQNascpF8GfBrqU6GL1CJ0ytl-20b2AwQlMNAaYsKpsO-QQuEOjFAJwHz3pEUTOGiQq1yi62p3JtwDaWBSk9O4URqBDH9sLf-p8TT7cRbOWcvZUvCw40m7-2TafufHSjRboNKGqreFGaVadnYgjifLTbDTWyx12LNPZ7G_nthtCO-K8nSHSYkt32U9NHCbyRlI8hmI2Bt3lmIuqElDOkp0ng8lxo8WiXG5Ya35VHKrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26829">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfxCx_-Ahoxj7VP5BDT8A5fwR5H87T0T6LbfV28CFobn41KOLwtoQ62V8ph9HD95IX_Hkgo8XrQrYUcBiJZYIv0lgtvC6Sz7JFwgO2QZ8qUymp4_de_m3wKimSXtLVSCx97QujTxnBlyy5GGiB-aELjcf_2uQrmAu9BrQE2Z82BWxDrVYd1LTl8766Vx6byaCcyzAGUHTrwoXCj4upIelDGiPchWJTgVD20GW4qzR_vWuA_eaY4_p5JbEpubIax3oMxihLa-mwf7HLYHaO6xVnrzwEVsc0yvCYW5U46Et5yb77GuWClpWxMYbdAqSRCzt3qTodtShCCEEA0ftmxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26829" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjOM9ic8-rou644tw9MsuYLwPMYa2LgrtR29lKUxLZuQYTogdYd_R6SllmHD9ky3_TT58WHD4hlonTy7OLAzTdxZ-NizqGFgJzQWu_WCTVsAfHhKKQSyXzEYMYcV4ktIO_qZkfmW-NYxKFtXWCRnjyRE4VODXFe6Xj3_1ur3rQNIsuS7kbKX5gAb9dipjzYaJfOvKpYIvBgl1AR-iqHZdXwNLWymZTqFAGuKhQ28S8_-wJz9-81GzQ7OHfOrIj7b44NCjeN7_cMJvMxfq6BfuIXqgKclK1cTYTVMSZ4bQa87MWGK41p3DMkXMwHNzJF2wjxbsPCWzxPdgPgL0v3URQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkhZdNoOuf7_sCmUqvOhYsZEAXDvM0nO0Ml5IkB-Ht9bHRnixPKR7tOQ2phtqk05JNsP-_ah79hE6NdqHQx5jvzTJUP1C27IIi08wrsabKxFgsX7R6bM9rgKYpy0NBArQdxk21Kdfs9AvvVMyg5iwzfnMMfwRTQvmFxbA_G04ykoFZNR5ZPRJDqQLCURycRhctXUv1bj5lSXkDGUlGJbMkFUBlOGwAjr7yHrdBRmiUpAwi6EBYksZ2b-hHhKmOsSVxnXW5-d8MzRdpyuWiDwvg4XA6bLgmUxS2Y2jYVs1DkD9mPZhyKxrPEms25B2jmWkPRam1W82Qq-SEJfw-BBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCdqULC4GAPG4TCEeugmvMwf9BaPD-WUqWhhA3X80BrKZFf-h-c28jiSdVKrJ_aVUNXwgiGwTyZwcX1sI4O2ehBtWoLSCQjVCv0qIx9cLbmVR3677cL51EBfys_gBGR8IkRgidwSPzoA9oHaJMgdN_7-zAwRq1-9RHj9HLZtT00ATyFNEsGc6PMHjmNaRRYyn-_gaLjfvNJTYa0HhgRBEH-qOI6AOP4rXmFsapuINAxmZ49gvE0XZ62woq4LCthllMp9llvuepUH2yYpOUp527qCrPE2_y_AnBXcjw3ZWaKMvU8pXTbSDzE3tKCeuARM4WVvIz1ISui9epyS97pVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2wTqhvpeOKG5G1nLJOOaA6_jPHMzNEcwevFkzd--WQAMKOE2-79mnIvmJqFu27rXmjNrPMxcx4W4dDg1QjJ0NlRLZq0OsbdSs6NQ42yrsKINAfTvws7PV79yrX2M-TcUbQp2etzy3iGn2O9amNvZuTepwXvKXAZF2IkmBhmzNjgEq3L3biFjkM9ZkBokxyyYxP3Xmz2K4lrqg3NuXAKYEceD5Mb6sq3aDO9M4gqHdWQz6ww5YaX0J8NJU1Le8oOEgLcdJkQtJ1AjjqEd63ooYv2LqrwNjesH8eU3KzPcGb6LGK2IPG66DomcKClP0x8w4U8bcz3pTbelzLRqMo8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsACNJ4YoHSjKfAX_iZ5HTKzCT_L3WFMnN6lcmHQFs0kZnWWoMmsEyckprrJAnnZuZ677fKzd84qWNSJ6NaeDOsT-Q8tCCVXwFxZ5CYMch7qjNODxOVJhaPyiioa_ADM9cIk6mRqI6ytACzqOxYy1wXZGhFkPFlo0V2F0A3lV4KKA9ZmfPZ8fRixMrXxZu5Drn6lnGMaZPsh-OmjAwiA1p1oRVvHjxB_dU4cMZj9BS6ldknNpOx2W3VYecAaLSdfz9otjJ9dimlKp0Bj087Fyyp_KTmKUd_9el0sXOSLql3t8XsBU_4X4_a-AjIzCXz7cgTIGuM9uyNADRLOXLvQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBcTR-r6hd5DRAGavn04h9FrXVCTqm5zE1k6pGMAz_iKtWdFQKxTtz_3VZDiNVlV4qZWBm7ZR3JHaO9C-9hHIIX6N13NmOGhnckkzd_53h6vtG0nsLzCFzFgdWoLp5mYog5lWp8zIcVFFhMHRCQTi4Z6ecUL_xkJl73SmsVMO3UyCNi94EGqnMxep8BVB140Hohu-05f3YC6MEGx5SwfMSleXfU0uIrBUPpCvWubg80Vd9brveF-y9HsE6LLLlwRjrLvw7lqI66moETnsKJIiZQz556TfUrE0NTfxsp0kgPEHxjVH8mZf_HY9emo2XIqyPqIVh8f2Ad9qVwiZNY55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=NYlMmbZtNPVMi9fi-iAUWcve6uczhaZw1BYwkAa4gSzwL3VgRcGTCX4rqBHajqhZ8ixCuuqVEw6CI7m7JZ3e8wN3HHlnKQs07FPHmaD-A4HWcXeozdVcqWLNk-qfzFpkZIdIMuPezcNQNz1PKpZdz4b4wJVHLhHnvSr51D3atNANMhbcvOg6e5UZF4WTxlVm7RhibboSUj_e262Wp5qk-tYphbv5tgn3qFQD6szAxQNoMi6pcbusfb47yR-kl28bETtUfgzZVWFi1bkH1p6Bx60q4WYyvSgoSSEja6mTGcphozVtakZ2zRTfVMFc6neYEIlesY2AJ8KoFT4ypSiDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=NYlMmbZtNPVMi9fi-iAUWcve6uczhaZw1BYwkAa4gSzwL3VgRcGTCX4rqBHajqhZ8ixCuuqVEw6CI7m7JZ3e8wN3HHlnKQs07FPHmaD-A4HWcXeozdVcqWLNk-qfzFpkZIdIMuPezcNQNz1PKpZdz4b4wJVHLhHnvSr51D3atNANMhbcvOg6e5UZF4WTxlVm7RhibboSUj_e262Wp5qk-tYphbv5tgn3qFQD6szAxQNoMi6pcbusfb47yR-kl28bETtUfgzZVWFi1bkH1p6Bx60q4WYyvSgoSSEja6mTGcphozVtakZ2zRTfVMFc6neYEIlesY2AJ8KoFT4ypSiDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXOfp94oinrIAP0vWzYCqqZsHW7voi6HuIFgXNDb_lSIBKxi44hKLZvMoJtAt18sTJQyd_r-_7xow1wSjzVJx8OX8zRPgAGUo7oCbz0SXMoj2okJUkiQRhSP-SyesfHzauFQzcJ38EUVtQBRgfSOjLA1PQGPPBu9mkQUWA_LjJjpEiwoC-4hk9Rp0ueUzZX9qe6Kxq4wqR6fzYqYjjQ2JsXFS8BpB8DAUSqaBNP-gj-t7V9_vqcPQwyv9Tnw7T1UzNA4WPgwFsHuj1q3NOT78JmWcOBbcPrmAuPGC93awTkCJx6lMPCsh_XbKZih_I-ZQDn5kmP97W9UBuocbw-FeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU49xYALl_zbqfSiOIbPx-Mc3leYBRCAYtXOElYiyaG3LO4tNE_YDNKjZinqvZd-KH2KE2qseMPW1UZIx-Rdn-GBE9Beai5OlEdfx8tvn1eWmorGkikCbFQSGfu2x8lQVLLmHlX7eJ2ONu_WqBEF2UIpmek3AlSP9BZEkTRsFbygZGx5gdrm3swljch7es5JIz3H2-HgC7_PMiQpEu4gKIV9EA-pL40r4q5x_M-TYwzXtj__dcCBI0lGmdiXn51Y90OwRS38EX_EA7bbhMOJX0SabaD9wtr167FDaQcADJur7DR9YyxYDceBJLLUNMlWc2AQOUSbqH_BY4VbitGtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TblPU-PWvrwSe2u1JVjWw6UdsSCZj4mDaRay569pbufgOEHG7YsWX5oWUDDn9cUzT-HIEskowwUuvs4_ZArC-xUC5OhBrE3mcMyAacp2mGURQHjboprsVRcUyTD_0GJVvGYz4Zva-LMhwsU6FvupY8lHSkH0T4RZd9fpsideRqdifKzYSFW1K4z5RhKELUgKkcQ9xzI5xjv0iEltlSIhauMZCLHKnBcmC3_jD3b5J3je8xXS6XkNQPhPiN2Y3IKIZ7occN2htOzyU5pdMjjDmOc5UKVjT3yMPBe7iv4bA5rd0fHLfnopCwQHhDEo08jj4jMmJlyPZLoXNeU_jqKqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6sqPrYyg_DOgBMM-NyUCBQ5r6S2fBac98raHxSUxXFTiQe_E6D2AM3EC6_SRY0C0sF-Odb3BTVaVUL_lNye9Q8PA0LLbPTTBEya4PbYAgN2u1CQYQ5O6wQQIAqfmy7pL_Bcr_IpCvtHmmoyY-jWSYNQZqGa97Oe-vTnCZP94xqTHikKSTtN3LzvSCYxxJnrZywmZFChe8WXOAJKx9TaIBzeK9v6u4OrY0_ISYgwq2H3Vm9Gp9YdY8QM27KSkNACcdT69RjFrDDy6hxNRevZF5kUcun7vBaPfe4UISSBd5u7szp1J7gnzaSrrlOXzN8RFAMgZtTkX6js4PyEDepZCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=l1ojcAwUJtWuFCH207DoHXUD-UFTlqT0T496YugQPovfz-GzKXu_yBOOb9YCUrtr6wkqAVLhmiDbNlMYBL_fWFD0v0t65aVnzt0SDBusF3iW7_H8OaT-4K3CFIfkU_TOD_7SSIxhaqEJPb5kFM_3mtzMIBU7BfADjzzOZSKYYtC8GemMqFk-2m3A7ls2tm36zM4CQ5kMrO-rWVg3dzG-WLpf_cc2BCBpgt_XWdaFgkcplOr82_rz34IhTbzMmh5Je9PUHtGQ9euklswnkSmS0kGtnkqVg-IIpKbPoZPfrmwUmWTnePjweHGsYbabZLRmt9eN1eO3F4L9g-8xfg247Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=l1ojcAwUJtWuFCH207DoHXUD-UFTlqT0T496YugQPovfz-GzKXu_yBOOb9YCUrtr6wkqAVLhmiDbNlMYBL_fWFD0v0t65aVnzt0SDBusF3iW7_H8OaT-4K3CFIfkU_TOD_7SSIxhaqEJPb5kFM_3mtzMIBU7BfADjzzOZSKYYtC8GemMqFk-2m3A7ls2tm36zM4CQ5kMrO-rWVg3dzG-WLpf_cc2BCBpgt_XWdaFgkcplOr82_rz34IhTbzMmh5Je9PUHtGQ9euklswnkSmS0kGtnkqVg-IIpKbPoZPfrmwUmWTnePjweHGsYbabZLRmt9eN1eO3F4L9g-8xfg247Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goBUFuFnhHG3od34J74I30OF3K6QGAT6NWKinyqCSjU9XRA6TuGS4Z094eZMuBONGVOc5nV0c8joNRtK_vfN2hdVP_gRK-sC-0ZIq9vAMg8VnXRK3CkfP7__TgV3Wg5vHbVaHVJUvEJteCIL684DNPK27lM6lMtGnYPeZy1ezbhh9ekp_psiBBjNK9MDhekaOWYoTn6IS_7ZW9uNmX1VIIA1oPZoAnyzcHYnodzz4kyyGFRWG4nKvPK34OjLtiaqzVBEnqxyYS2c3J_3hLJQWrkwZbuoTBf5N0_tFr5d-m--Rt-rSJfgPer85NggkW0rlUBhEHhbJMomSDKOt3qVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB1iEw_gQwnAr4hLECf0FPJEcR2Z9wcalLO9kPAPycfz1g7KJFUOujhwehaKxOzP8UGYakBzShi76mlfGHW7w-Y3NOcvN6jJbQcq2NGE-BJElCvsvg_XhEF82tTR7fa6eHy0EWliZH7JLSeVS32mj0PIzu5pi3MfHcGgSx1xYZbydZG0oA3qc22PbiatX6kwkbv8TOR5OjatG-7V38DF7BvPsYezTJsr_5GfNYDQpOdXFmbBqqFXPHvnJ6FY_7Wln2nGrLUjMeLtRKVpE5dhJgs_ijoUF--LWvzept1IACi7ei-qdOJkcdzu1RXKFvuW6LStzHtYdoX39zS0Y2LQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=esUp9_pZN4H4NhbeDepjAYf6AXw48Sm7OZm3vjquW6kPmwhWywnN9PcupzCP5kmwGZtvaWrq__ZWrxg3ltHrxsOGHo1MnS2T7kGHe0SrhjBIDLPm_oUv6Cama-N3ALtF4cNKjX30EZaQuOVm9Dbkb0kFEWzlFkP2OeNRUETpFwyjrL7vcjNsDiNTG7bpkre-jqrB-AHkN5xf48_u-S1ENRmu760tRv89xD5AXEH8HNi3kPrIdaKIfA3xYQ_J8BK74LqaSViWxxs5n75FchFj6SOFILXrMIY67a0wq-SRsuJ0b-s8g2OSuhVd6rAbBfKbdCbBWL2eeH5ayxFYnezylw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=esUp9_pZN4H4NhbeDepjAYf6AXw48Sm7OZm3vjquW6kPmwhWywnN9PcupzCP5kmwGZtvaWrq__ZWrxg3ltHrxsOGHo1MnS2T7kGHe0SrhjBIDLPm_oUv6Cama-N3ALtF4cNKjX30EZaQuOVm9Dbkb0kFEWzlFkP2OeNRUETpFwyjrL7vcjNsDiNTG7bpkre-jqrB-AHkN5xf48_u-S1ENRmu760tRv89xD5AXEH8HNi3kPrIdaKIfA3xYQ_J8BK74LqaSViWxxs5n75FchFj6SOFILXrMIY67a0wq-SRsuJ0b-s8g2OSuhVd6rAbBfKbdCbBWL2eeH5ayxFYnezylw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=lfJkED73G_AdeDN4UfUhS8Bi3amRXc0ubVwtofgpZtf46SCbJxaYH0ECZ6eXVx6IcUmBAVUGetUALuqgvZ7Zh7VrxiX175RXHXunb_WoAe43gyOCckiL33lGdAQXgoKsRDIEa8TIWrcp7Ey56LoxkrsXcBodPuAR0wKZuFOmDqHXTxXBGhVunJ_QoI26ExFJ8wxueH_-8TPYZ678D6t0qIJiOQO0NWoYbs-JrDBzM9NIqbU2-Xd-X3r3YL8bVg5T3guTWjC4U9u2HsVydB-Hwm8KDN4sJ-BebhwJgr_Pob7oBnYlKE7Yft87UQt68iihI9M8UArJuZAzMFO6XlF2Z1NbRA6yyehlyCwVuaWmcGjGwC2jGT8HbFa78mvaYGT2EVZuzi_UiiO8xH5TYyWJnA_K_RrPi7p1JMpRwtOV4DBrgDIRXNI9jEoqq9j1lhfpXACS8abnf7Zu7mi6mM5ZbV50sGRBjQI3qWYycG3u9ipaHFWYmWxJr0pUtQRJ_E-6fcVLlAbDndpUUNdeD65eyJ-5JAe1NNtSVh4xMo60ajIg3l6DQbeRywuMBrdJPy797CBTjzSVmGF1iEtKeCzWt_8L9grUsYNIu-6kKZ97jEnK707dXkS0Oqgq--qTR9VCQGZ73_j2t8sK-oPCGpbNhv5lMtx_6Hkk_mgFZQwNSrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=lfJkED73G_AdeDN4UfUhS8Bi3amRXc0ubVwtofgpZtf46SCbJxaYH0ECZ6eXVx6IcUmBAVUGetUALuqgvZ7Zh7VrxiX175RXHXunb_WoAe43gyOCckiL33lGdAQXgoKsRDIEa8TIWrcp7Ey56LoxkrsXcBodPuAR0wKZuFOmDqHXTxXBGhVunJ_QoI26ExFJ8wxueH_-8TPYZ678D6t0qIJiOQO0NWoYbs-JrDBzM9NIqbU2-Xd-X3r3YL8bVg5T3guTWjC4U9u2HsVydB-Hwm8KDN4sJ-BebhwJgr_Pob7oBnYlKE7Yft87UQt68iihI9M8UArJuZAzMFO6XlF2Z1NbRA6yyehlyCwVuaWmcGjGwC2jGT8HbFa78mvaYGT2EVZuzi_UiiO8xH5TYyWJnA_K_RrPi7p1JMpRwtOV4DBrgDIRXNI9jEoqq9j1lhfpXACS8abnf7Zu7mi6mM5ZbV50sGRBjQI3qWYycG3u9ipaHFWYmWxJr0pUtQRJ_E-6fcVLlAbDndpUUNdeD65eyJ-5JAe1NNtSVh4xMo60ajIg3l6DQbeRywuMBrdJPy797CBTjzSVmGF1iEtKeCzWt_8L9grUsYNIu-6kKZ97jEnK707dXkS0Oqgq--qTR9VCQGZ73_j2t8sK-oPCGpbNhv5lMtx_6Hkk_mgFZQwNSrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4WeIzespiqcaDPOubUJgsEuXgTPXo_SJHMN9tuENeQbESX5BeKD0CY9XsXu3CIdi8QclrsR9Ow_mcaYW91oCeI0Rd3_h27qVQVavSCsgZfcjzsv0cpauAHwE2d3Thrz-gpQSXz2lOailYk77fFRQs5UDEcxN96A-wFzRGvdpla9RcA-J6AT4dO5_6Wfp4219LOEcUlrfOxfoMG4SWB8tqvxVFVV3O7nS_cJGjb8mwYAC-DaFhjD_h_BeTi0Tuh1A03RR2BXHcxw0DwWB3nUT68gOScAx4TWIFBU9RYIcNtDQPsyzskuN4drYmmKwSexVa1IBB6AFoI-BcbLqavdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6Yhu11-ndCA2v_6veefaWTXglI-ymvvquFZ2lu3ZgFqFxjYzp_NTM2m50arEG5t4EomDEXAMhD5MIHlDe7LZGuSeOQHJqUDgpQsRRXk4p93C2ow4RrrQuyPy-TFlwTBrZdyEafLPKIGEmPtvwBAKtuxzIVzDnB4LwOLd4D0s4kZry5YZBJG7h9pPa0CYj7RMxSZAeklTlcSh1_B61hfVcA9XGji0UdWf7FdPGKgku3u1uHtIhWABviBjq6_vLcxFSzd3UKLBlsRUlO-mELSjdUujToQggfOKI-DvGbty9do1Fo8MMGxKSGY2-y4ynW_qaV2rwbfKDM0-1xn39Z39A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuRXXRmRLfqDy5vOghl_Xhx0yrGdntvFoE2lXum_40NFh3oOXb0hOATeSZcV4Q1HYGSPzZZ3Ftp-EkFx6-uO58A5gDFMOTRjchSTUCa9jEFEVZ8UJ9LEXTgO-imcejB46EqUKhrZWaAzmi3ZNzATLAAuhFz82YvbNVFyCKg5Nb9rvQCrkEwWq-sYJeRUkNMJ4I0E906I7xU-i-ncjqQlEGWtzy1gWoFmw5dBGMyxZrG7v1OKN5TrS6xBOiMVyHA4jdHBEi3JgBrGcyejDooyNtqJwgTUjaBcZLZjZ1xBI9vVJKblYnLXld2eAcZILWYD9vRl6c1RM4oxz-gfx6mYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2elMjd8tKzFQjc7oRrP-0i6YoNiemkBqxHlGBMOUdqQgnNa-CcJPpr-ThO6oEHWd1S9X_T9UjXEPuuOUhs6hGVENdaecyOqOFpIgy0ENR1x7nDRg7OXl9s4B0ExYpHBlY8p6O8RXKODGJcQeiM54uAPuWAAeTSAt1i-R7E--dt4GLas9u-giFF3p2zXbjnLOXLVT2NQFuMiif4RYEolBmdKJBGIcV0JcVCg_FKUBhFwhQBo0d5dWEqEImjKJQUtgLAChU8fAb0QxgJFii9HwyHVIA6G-27VzudZ4pp--OH8fQ3xu67NRjQCYCQfIULCkM07wuOzq1ObcpFAQathUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOR9PQaxJDXr1hdwMWdnigQ7NPyesr6L1epjXhnwYCSs0Mh3U2WF4K785sYHNNYjo-2eitpiV3b0iQZnsOO8kcyTI29xLepsD0kV_COP8nMvptm-Or8n0aPkIIjtF_rKqaRdSKSxBd7Z0vwObNei8uTKNtY-_eFE7Cyhrpza_hpALkNdy6GQQbPxu5gOcwH-8NsENBo8z734YbJn1IoI11r_jMBnTR6JvIVrNUj6z_3mBOktwDGgB3eE-v3u3IrblFxQl6To5B1KuCLQzb6O_N46MevQN4Vy0dAf7Env-4D3_Tu8Lqmg88q7R3X37oFQC5kC4ARul6e9c1PsYqt9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k702930GyW_f0-6eKkLY1RwLxLzavP2geUw4eLg4uv7fPTu6fCS4HHOKmQnId339tYIyoj1DIMXJC8R81MhwglPqNriyojUui_nnRMnO9tYHdMIE9DKnpncscRbSLguLENqT5pQmS0uB9ODZqcIwzlZAhaoHfrX8TF6QI3hmwVyBEEjAOHuROKJwNuVIkEnqgHKlWUaBTD44WdUFswUgPA0ONP4XdCiS_xsvXFA2Y0KKOrD1oY0isRxdIBhKYA1Gb5rsQNF5iZ1N2YTZx23VQb9UiKf-i_WoXIbBJwguTMYkVnyGTRXchIeJyxj5JPdsxfuVWbHfwt-2DjsykO20UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=UzRVr9QvBZ38r5J_8Vmc1BYVq0lRV6dJxD_GpmnMqG28srFwuUhwKLmmF_0MWYIksIUycK83uKjbShq9oo_wUiknprqE9IOCt9AmMWd5Gv6pk_lQT6lovY4x9oLj4SptbiUgHuQCnnIoIXfK2HnPXBjO9RhLlAYiPkFsq_42E5qjJ1ikbrBc3alYeoSo7BWbZCAYMv7vmPX96vud0BTaSMKrapLX1rFJJ8ColPb9oX2i-CihBVLcU_NrR1egVazzvJASNR0kbI7rmj-CFh-JpX6YZbPyvt6DR3XUtmVXTlNSO_Z0gb0C1jDJlKcfabCg_vBQDs7Eb6YtYvw9ESZFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=UzRVr9QvBZ38r5J_8Vmc1BYVq0lRV6dJxD_GpmnMqG28srFwuUhwKLmmF_0MWYIksIUycK83uKjbShq9oo_wUiknprqE9IOCt9AmMWd5Gv6pk_lQT6lovY4x9oLj4SptbiUgHuQCnnIoIXfK2HnPXBjO9RhLlAYiPkFsq_42E5qjJ1ikbrBc3alYeoSo7BWbZCAYMv7vmPX96vud0BTaSMKrapLX1rFJJ8ColPb9oX2i-CihBVLcU_NrR1egVazzvJASNR0kbI7rmj-CFh-JpX6YZbPyvt6DR3XUtmVXTlNSO_Z0gb0C1jDJlKcfabCg_vBQDs7Eb6YtYvw9ESZFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=Fr5ydjgglVnrC7xIjjAfpPNeRVO3vKSKpYuJfM4zwcjZyNPXrFjfQ2rlnNhAhn7oeQvPCAFj0MW-6SZk7oX92oE0yRk8ONvphI5BZLzGoLsApORa3d7-ZHMr6GMuqRyJ5-zyKVq1NzLCM6Y84Y8JKgYhqdsUYnh_EXv9ZavjAh8LFsalVgsUAbjBnYU-kotjvP3eCgzoxj8z1MDmOjCt2D8cOHiyMVtQiR-WxcZtY0YRryVeW0i8QiUVkXSDemePEj0nfoZC9KSfEcXyPSBQ6UMPGX5bLXGfz3TRNMsk1C_T6yvkVfRgJ-NCL3qoxHrqcLTXyN8HEHU4b87SC80aqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=Fr5ydjgglVnrC7xIjjAfpPNeRVO3vKSKpYuJfM4zwcjZyNPXrFjfQ2rlnNhAhn7oeQvPCAFj0MW-6SZk7oX92oE0yRk8ONvphI5BZLzGoLsApORa3d7-ZHMr6GMuqRyJ5-zyKVq1NzLCM6Y84Y8JKgYhqdsUYnh_EXv9ZavjAh8LFsalVgsUAbjBnYU-kotjvP3eCgzoxj8z1MDmOjCt2D8cOHiyMVtQiR-WxcZtY0YRryVeW0i8QiUVkXSDemePEj0nfoZC9KSfEcXyPSBQ6UMPGX5bLXGfz3TRNMsk1C_T6yvkVfRgJ-NCL3qoxHrqcLTXyN8HEHU4b87SC80aqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdOS5eXzGt54bbh63RJ5iUGSw_Mmg7lUrwKPs4wFW5E-j1rmsEDVaCbl1vuEs8-ESQXD7eapeRLQhUnV7W6uN4vh5SYHtuizp94ck_uF8E8CiIvmMOop2hgGDtnpdF6sv2r5CMGk3PqVFSWo_mr8yfvt4bg-6b_oB6t8ixsgiF6hERRlTNMJtcT6Ou66nJDjyPpzL8hloV5gSnd7jjoPYTzUVs327pDoBOLWD0RAiP-zAXQRlw9rGyHoV9zQMYVtucP_ucxvTedimTwgX2uLxNaVfLqosrKG3OZXEODYzEgaUQbG0tqf4pQ3ZdB_SeJxQevQ-qMUPjLSR4Tqpxf4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6HhgGMzDYqEeJH971gXxSMrinQK64222PvZ44rrV9Z2k8hSomnDQTkebnr4aD5kxtqKR63vcPmYKC-E1_Q5ZjQaWhmLEN9kfcBNvkRT_FF3t45HEVUQORogY7qarsLNpnUmhMxxJs8riZNrTFrXH7-rPRSuXRU6ErjaxYixQkGkt-YIp46LVefFbce_hmz8ys8l0wGzWb_U4QswIyYf5PaTOjPcYJtGpE08ZX83gGt_cOVCgGzMbmnH6nkMqQTMgcBIYSP2xEEKxS0AsZzbNoDRCJZm-9JmHq2ad4FFjDgzbW6tQX-J2xU1xB_q6Aczp6Ye4E-7ehJADtv5SNGZ4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jB6Wjdr23HQzoCAkueTSrQbJ7YQYBBP19DXsitXc2rf5AmV03scnmx22O7lp7Nhq-TRETtWHJWbGk7SGPT9zrPy9e0dnuQhKpoOMknpOZ9kTozADuXJYXWeAj8g2sJzPXJZEGDKppO5M7ZbL2XnlChFsYX2m4z1JUVEgckxKmDU4z7oSa94BsVfzqjUi_oFVUVav0PpTQreKrAozuYdXHLN0QiKbMj6Wv4T3UsHUBI7bcca1KXjMHB6uWIiPXnZQfiA03WcuVMURmYPuGYGjfDDz1Nkpa4BRhWZ0Wr929cUDvkCFv76K4I8FgKyQ8uRqdbv1EzIG-UcPWsie_lt_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jB6Wjdr23HQzoCAkueTSrQbJ7YQYBBP19DXsitXc2rf5AmV03scnmx22O7lp7Nhq-TRETtWHJWbGk7SGPT9zrPy9e0dnuQhKpoOMknpOZ9kTozADuXJYXWeAj8g2sJzPXJZEGDKppO5M7ZbL2XnlChFsYX2m4z1JUVEgckxKmDU4z7oSa94BsVfzqjUi_oFVUVav0PpTQreKrAozuYdXHLN0QiKbMj6Wv4T3UsHUBI7bcca1KXjMHB6uWIiPXnZQfiA03WcuVMURmYPuGYGjfDDz1Nkpa4BRhWZ0Wr929cUDvkCFv76K4I8FgKyQ8uRqdbv1EzIG-UcPWsie_lt_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxvYXlyXIDdefpEEosvh2sYb3OwxbEuD_MCUHDfAAw9fBRuBEI6uo0fPcUYD1hK5P5C_3JsQ9BYZ0L5v0kZRtHRJr0EnK1A7ftYrRRhVWM4H21zVqf7Sy35YmMEQi3T5ed0EbzIJnO7KOiUtBJKtk2EuTBb4FhxGINV0YRlc-BzV8nwhc-9MftLv3K82FXlT07adNUtFgCo_n2X2C7FvcFTzYf1JpBGi6l0gufpKMmzVUpR3HK_uTk1i5NUOKVKdnZBW8fr2_fDFp9tkByUVJACE-HnlHeg14Z7vuyXNceZZCcfjfCi7dl8npOv2AsYEKIB5S8MifyzVxcLS2XnPpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNeYcPmS5nuR62S5Z0sDXRr8huYdVLuSRGGGJsFIxKNAWUxItwCfFCnG0606npIDVnTD9_Jxft5S2BSQ1nY7yq7Tjf4FKv1VXluMZ_KjtdX2asxldU3E2Kg48m2J2zEUQRIuY7EdBfG9xaLFp6ehqkpHGR3m3NPjy8bWWdTiqJSoYh-RDu0UVl21GzAY6oZPcygeRYxwzq8sATujYKPt79uZGylWfuJReWeYV7pyVlFoJ5bUNNbfwZioX1mA5EhkuWpBKPOl10SDgMGsICmLg1_isJWzdShZGtjZPKyKcVktjwEjOVY6FiBNFXoAQMXTcxuxHPB3MaQC1TuTLrudBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=JIpDWnYAX0AF20BSU54A_UlDbmfzy9ZBPz50eyaWABQ2jxJzMRge_u6DCgE5mlNpUHqGGzpw9A5JQ5eWpAXGS0mS1TyDg6BpZMl_9y-0wVCtfONRYTpy2eVXZQrHAmtnO7e2kYcZOlRDxazEpOS9VsRkbPkRrlEwgCSXIteIzPBoUk_uVwTmMO0SU574LQFteebvgAa-ZjVWBHBouHvbapKwidB2oizqjWiG2-i_2BPm2XjYVxINi6H24jC1OjE-9_AJdzp5AKbX29DRCtUzycSUgeOtc66uRMg7ZZAtLGPPU2x64Q9Xabfudb_FwDRTRCr3sCp7v1U5P0-IGL9Zvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=JIpDWnYAX0AF20BSU54A_UlDbmfzy9ZBPz50eyaWABQ2jxJzMRge_u6DCgE5mlNpUHqGGzpw9A5JQ5eWpAXGS0mS1TyDg6BpZMl_9y-0wVCtfONRYTpy2eVXZQrHAmtnO7e2kYcZOlRDxazEpOS9VsRkbPkRrlEwgCSXIteIzPBoUk_uVwTmMO0SU574LQFteebvgAa-ZjVWBHBouHvbapKwidB2oizqjWiG2-i_2BPm2XjYVxINi6H24jC1OjE-9_AJdzp5AKbX29DRCtUzycSUgeOtc66uRMg7ZZAtLGPPU2x64Q9Xabfudb_FwDRTRCr3sCp7v1U5P0-IGL9Zvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6fiYRgCnYQodob8-EnUGYPlUltZgVko0RsyBSnsgXId25h4kY9xnaCIG6kNENFdK88Tgqv_Uo19YPGgP7ebLr1-j3Pa9xi8Sz3V3OMiDwdDjEaZby4ePnEq2r1bCF9bVD1lD7cNublKlNGA0NcebNOLjpXTIb3nR9DWVP66KAmb8nzJQhaK9KSyJAndC9CskeOwzpeAkXBzAOQUW9pOH6Z4Tgu_VhSIFzL5dfNpAYEtMp2t-KAD72ub6WLxCs899zAUExuIppCjEhuowg7U03waTOeLjBn4rnkwOxKbPfv9HiF075DGFj1ylbYeQnMZYTDjVkS7p8RQ6OhSQT-1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzyJDHhyCWbmwgGf4FXT6coPIKZWBlBKzOqfAf1QBOjAbh48ymdvMAWXI7RClLja8wR0sRgvf4jgQZTxb3JFUOhOJ0GrZM9_VrQcLWis5hJu7bpkFWZEu7yd8AhGDFrGsGlqp-PiC3oi5pU_Mgpe_Sie2d12sN340QqDQXLvp2XqJfb0LZ_zx9niT9dCtMnJi_49X1dU4641n8riwnhh5WiWkYbWuev41SrGQsGnGNQdyEHUFAfEpioDOvpHnIISE8-675jwpKZn6miY4SiS6b_y4kXFNImdM-h4iXCTFmoz-7I6-_m3x_r3IiN7WJABVwBAko6Vn9Vc7WedYBfssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=KiCYw8o1K19EQhQbSVXudEPK13cXSmQqJ4d5RkB55eLBS27nzpgdQQ1-cbVkWz1nCAUj1Q70oL-OxWcdDMwpzCGgIffR4AHJBe4W6cvS3qm9Jep21Ukw5IsrR8Dl7H7fJn51lfjwyPTfVEMnGKc7WZJA0lS2uFqKmsF5Sq4VKOXemuoca7awDE5ojtzwP4T3KZ6n5zX2B23ThH4cIIXQGaS-6Tust_d0YZGimb9sEv5DlrDWaf6BnC0i5DF83C7d1VmbIfwn9ra8N3_LD8RAugCWpQMd8R-esb__gF5gOZbVI3DWcrdIOyGF04FJdVnzFqOH4ZoFT71jLZb_Jl_KXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=KiCYw8o1K19EQhQbSVXudEPK13cXSmQqJ4d5RkB55eLBS27nzpgdQQ1-cbVkWz1nCAUj1Q70oL-OxWcdDMwpzCGgIffR4AHJBe4W6cvS3qm9Jep21Ukw5IsrR8Dl7H7fJn51lfjwyPTfVEMnGKc7WZJA0lS2uFqKmsF5Sq4VKOXemuoca7awDE5ojtzwP4T3KZ6n5zX2B23ThH4cIIXQGaS-6Tust_d0YZGimb9sEv5DlrDWaf6BnC0i5DF83C7d1VmbIfwn9ra8N3_LD8RAugCWpQMd8R-esb__gF5gOZbVI3DWcrdIOyGF04FJdVnzFqOH4ZoFT71jLZb_Jl_KXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsg9YMY_Oaoa64fM8zshIPP6-4Mvk8Zept-APjULcEcNe8qZu1IWKyphHHIQ94dx-_H2aE8k9WfXNufsQ5Jm_Y5AALiiYnCNnD9saPQ97jao7N5gj5Je0x-J-O9QWosV3vhp9KsxHDsGMN0hxkZhGDBciCuFyGXJukyU6qkxgjTqLfY5QUxdfisFce88516hP0aA5XDE6JY8fpS0vKTaA78Mzq0SFAX3IpFwBwSjx56P1W4qnZ9Z0Kj1gWcCYG6fVAuMR5x_yxVGcDlcbYXUHcOKac528Z2l0A79SIudP7s4d2d4vV3wUt214Emz3tfbIHMJQlf6sS0GCj4frxHLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xbl8FI4YWm1jQi-pQmKuGneTBCtmSARn-UMfHUYHt1y6504QrnelT5Oaxm53zPLKs8k660A5Ng5nzSIpFiY_vosc_hilif3NUHZ0DgbpZ8MTBoqo4V1UhQReAd7UPwVjRiMA74DBbpb5ZdZDtrV5EfYNdrYszjLjQkC0h1PykmGj84HFrGyTZ0yVSsSCWN2DWMdzvZFWGeAbiZi0Qw4bgX24ZeP3rVNJWsopioj2ZZZs5_O9sDrKa_n6JGdaI3JhCFC-3Egc5WIzWqaHvsm44u_DQ5kBjRkmvoO_qItPb7Yea5J3cJG6H-Um3F7FEOrvSjz08idU0-syAGaFpBEbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAYD8LIYaH3KotF1ORUubwUgqfO7bWxjHQoIbQR1ppCjuw8P3tAEqdt3foKbnRxKWr1dZT6dKx4a28MEkaQFCVLCpsHL6gMsIx4yHCkZlcx0UUaYgTb4UksqDCyiGE-Y33yBwMrPxGsXIGZdPkwZUlDFc_jp_exWqhFjZbehkOOzMqhhnbQ4b0X26z3OLPiMr3h88teHkaZdM9l8Ha4bGSRUowe9F5Y6rNe9q8Fto22kGuEKKoQtL263IRuszXOBaekfcxDTVWgyj-nnaC8KLWLc2dEVqWWvxFek282KPwGqhQm0SJ3SiBoc1pLAT_zLwVPbzQFPs3kavW4G_Bm0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uB25WgrViabL3leAHzvPa36yk0X9whQ34LAlDccPVhJjlQn2ACfuRiO4GU6r3vAChHCSdL0IggroBHaNWgwlj4AuWDxRS9XmZv8Zg6xTC4YTOmqx1CBzBkjJfCAeCNu7cqkeGjRTxURw8tdr3RYtUh_whzmQWqf-OqvJIhFQA2h--Vh0pZFOMfUrKJJJV_khoh0dyZbZLBDe1WSXE9eqbx-oI_1omHf8-C9MHrmeon-ifgd5bYaqqKTqB7ZX0yl6P6bkgY94hluvW7nna8ATlEFGtpx1n3sVP25lFECnAqMHEcXrJwuyXS437537nSMzfkFMbAQM_ljXywDRMW9Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWHBTXp2WRoEFVFOXbkGIuClt2tCgoiMfufU6ImmwclrqG9GVK8yGEG7JlaO39ya2JrvgTXaWuTRKH9lPv0UBqeeyXJ4BAvfWryw4NXr8Da9yx2gP3AfH-gc7N2CxKKWGkqNIVorIaM2S_v6QHqQ1c_-zZQh2rDS6FWBOSXo5FPo8A-GHjjrHgI0dMBFViwTaw3riO_q5FE4-YV4Kw5mfK7lVYC95X235aZYs98Bw-xlaUziRmjzm_PobGK0P3CY9Y0BomEnkwkNdeZpZM3vqTrXEOLIwggElGSLvKwDa9aq3w6ovW8KC9NvsMyPjdBg8d1JlmMKEr3R_RSztMtTfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=jYNzh2o1S5nG9MyMK2U8oEd5gLYNuODm4VDBCrul9CVapJX0KZPMlT375CJ1a8b_niYhLRpwkpNqiKwI9IoaAFgmIh2QlPVF_s8IImLGQd2ffH9Db1ViRbIcwaX-bBkItuVdDXzVtXZMLDMZ9rNTrFM52IL2X2pEseEqaMiCQXioiYNDnHuDNGBgIr2uT7eWnwGjgU8xWhqcXjUJXOvlP_Q65ffYCMFQ8hYBoGB7XEQRM0rxUtoihkoZyI5HW-O_VTN1xGMN9nsmsEGqbsjwk7DLhQC_4L-5_HlITXe0edlPzSoW3V4It5q_rnHda_8oZLrYAalDy3krmfWrVp6fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=jYNzh2o1S5nG9MyMK2U8oEd5gLYNuODm4VDBCrul9CVapJX0KZPMlT375CJ1a8b_niYhLRpwkpNqiKwI9IoaAFgmIh2QlPVF_s8IImLGQd2ffH9Db1ViRbIcwaX-bBkItuVdDXzVtXZMLDMZ9rNTrFM52IL2X2pEseEqaMiCQXioiYNDnHuDNGBgIr2uT7eWnwGjgU8xWhqcXjUJXOvlP_Q65ffYCMFQ8hYBoGB7XEQRM0rxUtoihkoZyI5HW-O_VTN1xGMN9nsmsEGqbsjwk7DLhQC_4L-5_HlITXe0edlPzSoW3V4It5q_rnHda_8oZLrYAalDy3krmfWrVp6fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnoTMR5KhREuA6XQwXpi8eGnkXxKHZVBRl91g-14Ao_dUDFVfsHt02xlFTLtuQQS6nUl-2JMo50n6LMRTXmMIDc9QdLpW0wRThzoVY-d6ChPaINY0Y5m0pmdZtZ4-QftbRyVo1wGFePBwX5vzqJ7X0u_sPdilzf1N4UETTZY4evpQ-X8xPhBoRGFA7u7e2W5VUblhYb7ETj1W-I0QrdY_W8uBRuuUk8yAWfAPPbLCcXKZhmD0Mj5Q17kfW_MeBNnuBY9ejHzKiv4ynE8PyFwVqMqWgAfJ_InwJ_a9hvmmQYM3opLaQlamor5Sb62_ljSL7ajLnpgwR9dt0Jv64NaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5L5ULwVOI8KY2-JfH9a4hGfnFboNcGQ9yDAzXrR_LbvZT2YNDKYYRkzqysSp2l8p5HPl8cWgjxRrYJippXdgv9tnQ-la3_eIloN_sXAFzCH9aKU_mzikuloODoxCruaO0TJl5dvp_A5XvIb4nIUP4AdOrLMEKZV-BAglT9eHb9p7HbxdtEgTpDrJ9KHvHCwNriP_3ax44zEfGLhFG83sU6RhhYbxgtZzKuyIX0-heAvhxZiS_z4rYvV5UbeBWl7qpAIWDldBlhROnzahhtAUHBCcHpz-sH3tO_JyeWVpFs-nGONrRPd0GO2x_gk9rRwkHGozAobDDRazmQwkgU96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=vAcEBzKdaL9Jz9C_Jb6QLAUF4zyrHxztGbK-OtqQOT5nfLc8MgOmCMyvKsx8EI4diLwE0sHWpb3vIujjJIsk882N7evz7SNASjwgf9nE1geq-F3F3C_7-RfKAkvSk6K5qnIV5qxmhOJp_-Ws2g-_RNjOofZK9avodwZb7AMBW79NOvxqqd6Kdc5Yn71QHy1eJpACCfoNf6sbVNDNz75dyeJoo278B9XzZ_0tCfGpLq2FiO3XQVlRGPHQWglbzBZFvd4ZcVVVXjx1CiCcQV6MY0aof_6nfFtRFO4RHnaZJRhFSTH_K0ywK1PioSSUu41Xbf2wDpvQXTdQf-pqjMFxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=vAcEBzKdaL9Jz9C_Jb6QLAUF4zyrHxztGbK-OtqQOT5nfLc8MgOmCMyvKsx8EI4diLwE0sHWpb3vIujjJIsk882N7evz7SNASjwgf9nE1geq-F3F3C_7-RfKAkvSk6K5qnIV5qxmhOJp_-Ws2g-_RNjOofZK9avodwZb7AMBW79NOvxqqd6Kdc5Yn71QHy1eJpACCfoNf6sbVNDNz75dyeJoo278B9XzZ_0tCfGpLq2FiO3XQVlRGPHQWglbzBZFvd4ZcVVVXjx1CiCcQV6MY0aof_6nfFtRFO4RHnaZJRhFSTH_K0ywK1PioSSUu41Xbf2wDpvQXTdQf-pqjMFxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAsKBK1PHWjyjlhQVRKcFlODcSM8aAsmHcP9YOYwxikeTCrKfE-1HZgy7fgGG0h3p7hie74Hq7BZd2xIcCyroyPTuCvv5tMW7_I-8ZvFKl8nZYERDUUTR8cFiBZ1pymUglwsXoQtTZ8bD9WLo6v9Ozemc6Ny9I_UE1Q6bgx5xbNQgSeX3TY8E7BTQg3fS2Ie6nXuALx90aMyV4bxzCXrpA-UfXC5rHLv6SFzYpeNl-15cQaXlYdCAChMgRcIRZp0_dWeGaKeq5yjahtthHRksnHthdrUun3O7ICeBcyqajKRudrZOgxtVfP61Bo0u1pme3FAf-wCVT-9exF6D5aKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYBn0bms97ikHWTxzQYOhLUecK3JN4A-qZ1s1k3wZpVChqcg06V6DjrA7hNIHasckE6kTKpp25Jx41OfjpHZoKKIblrLNefxaZB90fRQgQB2Vpc3dOrw6dPgR_KpKJqzIrS3Azhs3V7x6cT9wCwVOBl-hgLbRcaKb-k4Y9To2IibiBfrz35oj8dYqKmBREXcRgqWeIER-oVKktmgcXhSxCh6JzYYFEtWU4yYZF_M26dmcLtgWwIKvZVtILXIZqjEp4fDvWnieSIT3C-A7xrCfzJLoG-z5pJn0U9LE-A-lqLcsD0Lq02H65kHuUguFrmndadYqTW43L6pTmQXDn3edA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWNRl8qBPJAuITwPb5kI1YOVw6mzsGExlBQmIhVsLmg1tFvJgwaDbfm2MMzVYKuZDVeohq1b5Zz27wGLKJ-w9Ok3naMGx7ELs0dYSR13TXhj6Ji2Md6u1h3oRip7REYhQrSkZIKg3z97wLiakIkaGErKL06Bx6bKgqjWjzI2HxLR4S1gw_f_CB4n0I_BcVJj0otIeimaEEq3bV_y1i8p91e7vPfsATmOSBw7Je_PPyVzxBQ9VaXWsII9gXQhJDHLekYmRxz-LgEY28s2p8Lk94Yf2QzqROODvT25cbkpIMwKMZcBW4iDJtDzxd4dSAYfwTaeroP9nw_dPnGV51CwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1lSMo-pB-b7VGQ2Ax9zwv-QFZ9MnQlAXrwxAqpsClhJsnye4ROH_1nWbHoeR8PF63j4X5M_dgEJdSUsqx-C2xgDj0wymYWdYEAhGczVXkzSrEuBKpHJlmR4NU1MC6ybw7xBQ7t-vVcxIzJWWZZJX3y8nrfwQji0yey6e8OzPXd_qELNtUtJF94YBnvn2E9UFDFH3-s1jcrTCOVhKqRddutP8GayQpTNDlZ_TFExKxebHJxW8mgVN7_XPUYKDGemSh-KNxeY5CNqlhnX9ZHX1fCLRY1X6BBPa40otwUs6TacuJPZKJdUkRop_SNackiL7iH0mivBI7XJFaMk612u5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeOuuv2deszm0Ft1Yyp-b133aobpwEXMIIBOHEEZ3qSeAz3ClBqdjKnHQt7JNhdmA9VI3mqJ67KTJbPQO_Q4XTVPOsfi_19o3xoBHrtM8Y01B6J-ld3iZuU9ginEE0d3Ngajt1XLKir8Y7bcxKiNKAA4zE5ADapVPy19XqQQGMOmdepLvZtH5PJW6e-uf9pLKe8q-1qklR9EnPsYg7Uz6I_6S8VGa-xH9QuRbuy9qR6YRmb7VDzT41yKwLbK6OneYsmpqOchXwSwsgDWGBW_dIoENZQzn1o_qv9cBUkTCHKMg9xQYO4KKnlS3AQswokEem2f8vbtpGSATwvTL7JJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=bCnPLDjZiO4OIgKlpVYIBPlM_HhKxRW9Yz0lmCZjwJgykAxxbqYvkCjDbkRLgA7owJhQ6IAKEQxa-nGPA5PYlIW7UjriXbGWJ0M8wIPMzHxCRhBmB0tJNFAAjPo-rEoHuAESh_XNLkov5lHt_cBWfhTik_i7bJKLIFMVCZrearTKf84en_EwJLcWWiLcRvoNmrlKa7wug-GZqJXJExoLML08LbN9OsLmIhsWnhMeXWKeG27GSnZTIUE63x6EOFJFP4XNNv6SgJOcLSBzoj1oEVYY-FWmp-eRZYyBS6VVmHYYO4-f_yIEV1-iWQF7VVXwtXrLLV58AuImIlulcZ_jFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=bCnPLDjZiO4OIgKlpVYIBPlM_HhKxRW9Yz0lmCZjwJgykAxxbqYvkCjDbkRLgA7owJhQ6IAKEQxa-nGPA5PYlIW7UjriXbGWJ0M8wIPMzHxCRhBmB0tJNFAAjPo-rEoHuAESh_XNLkov5lHt_cBWfhTik_i7bJKLIFMVCZrearTKf84en_EwJLcWWiLcRvoNmrlKa7wug-GZqJXJExoLML08LbN9OsLmIhsWnhMeXWKeG27GSnZTIUE63x6EOFJFP4XNNv6SgJOcLSBzoj1oEVYY-FWmp-eRZYyBS6VVmHYYO4-f_yIEV1-iWQF7VVXwtXrLLV58AuImIlulcZ_jFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kL_tNax38Nxiann2k3E1v6K5ArIb2-XEqBDu3HnJCQO1TlTepDdVyTk971MEKOaAFx640NfDAuc3U5lEevsdv3krNnSGFBr-KOc8Q1gDbdQj6er2M9cSVavTnEj1sJen9NgRsfUEGtR99MJPKP8UYdD6MQhSimtyNYp6kHeTHD17WzLJbhqPGZEffpimuiR3StojxxVXAn5u6e64vRArrrNlnvNrKP4G-V8N6yVYIA00K0Cgi6VO5oexYzWGnpXcQ5TW6NKAq0yQ9Snh_mpmwj8v8DNk3j0YgWbqKUSzJqGr342NCvmJRwSH8G5-i0hIreSGyGG5InighYQ8VZMmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvEmCBpobx5qDPwJXyTLCX3MFFcPI7f0HHOhR1BP_FJiWxuyewHwQKqSszFSE9nGId9IceM09tIQquFL91Nlt82b0P5qQVhzEh5CDAd73Z5tr6zdYpBJwE3PJX6GZBl_YQIHXd1I9ALYbFI8YHTG-K7eYg9BQ4fA9rutgS_gik5zpoEzO7rjTGDGvhRpdpRf4ZEPS2pP614bjaEgdVaN_Vtc_5fjTkUKhFU2da6ftPGPnrhl_e7CCEmgx577bQhwy244cLI571kXMVdMrFlSw2WTlsEAPrLCM5_IA3vi1whkDwg3HxY4wI9hPd6dIlBTX2ruB103fuSmRmffH_f50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=diOvySd2Mia_6TlT0qHKvLzXkCHkifnMZ1QSgqgj_rWZuSyi2YAyVhPktfCXZGFOsNz5ClUT1I5xBWAxR0ZHqA3tkpQxNQffJKVLBwpkNjvDKkv31Cex3WpsB4rgQ1R6U3JAWy65pNwG56sV67HMz6trXG-NVOIpX4K9OjcCBaMimtrjmstc1sNRZSLvtUtgMucRRqAnGmKZMFQUHn99WnqR0d64NmIU1XjffBWqUQDuYe5V2yjfg1dXcmqd7AzJzaiqICkM7CDPHwVJhvGecAi4aJBm9FQRtDrEKPwWJs3iewZGFgOlXt9dg3hrwAb1hJMsbeQHqcpKsAeQ0M5FaEQhYjAcYJwjCtiJA-jXf1ar0ZKHJArsXDxVIb330N90aFVrPEooS4Uigk4SJXpw-K8CbO7xZDrhY8Vogc3GdOauh6_wyBAh2zrdbuuLRLe1CqThMawX0YqOetXQIPpoUdC_F2e1QtQ99i5QAJYH4o9OJXJRJb5TGogP7v-XgB2QbMuQkb1p57zSAz1SB2ijGq9U6cBugjR9YUFR8I-hCAMwBtthz5k43pqCNTvwkSKTLElK7-wAYRMx1V4SlKohAD_Pt5aD-LdcciTq4hcNubcbOJ2G_t94zbrdT2F6SgASHVm2e8j3Lh_axUcUIW2PIebU8ncWZACA7mOawLLMae0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=diOvySd2Mia_6TlT0qHKvLzXkCHkifnMZ1QSgqgj_rWZuSyi2YAyVhPktfCXZGFOsNz5ClUT1I5xBWAxR0ZHqA3tkpQxNQffJKVLBwpkNjvDKkv31Cex3WpsB4rgQ1R6U3JAWy65pNwG56sV67HMz6trXG-NVOIpX4K9OjcCBaMimtrjmstc1sNRZSLvtUtgMucRRqAnGmKZMFQUHn99WnqR0d64NmIU1XjffBWqUQDuYe5V2yjfg1dXcmqd7AzJzaiqICkM7CDPHwVJhvGecAi4aJBm9FQRtDrEKPwWJs3iewZGFgOlXt9dg3hrwAb1hJMsbeQHqcpKsAeQ0M5FaEQhYjAcYJwjCtiJA-jXf1ar0ZKHJArsXDxVIb330N90aFVrPEooS4Uigk4SJXpw-K8CbO7xZDrhY8Vogc3GdOauh6_wyBAh2zrdbuuLRLe1CqThMawX0YqOetXQIPpoUdC_F2e1QtQ99i5QAJYH4o9OJXJRJb5TGogP7v-XgB2QbMuQkb1p57zSAz1SB2ijGq9U6cBugjR9YUFR8I-hCAMwBtthz5k43pqCNTvwkSKTLElK7-wAYRMx1V4SlKohAD_Pt5aD-LdcciTq4hcNubcbOJ2G_t94zbrdT2F6SgASHVm2e8j3Lh_axUcUIW2PIebU8ncWZACA7mOawLLMae0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVq6rss8QFENkmmxI5KwK33cC1ruiiVX59ZvnE4iKPs9_1gDnclUDjzjkfiwnQdQyotnHg57eGRIAYJSKgSsFPS4TcIAFF2chPeDtGCahSr777t666qPoZ2Z991YbNtgtMtte7-TS_EKF6ZxAaaBd3V5ne6bAZkLHpNJSNIMT9DWMGzyykdZKlMldSM6aJVGDjl9bLudJV-eWpw_vuPx0_IOiabnExHKyS8BAcNyE-eBdYaL5q0ls02zv2iYKlk7TGR54GWiwNqOrGiJNm1WdRG6TiptcwQNpoxYcetwO2vZoQUyRK403t4aEreznujG2ESEAOOLU53RPQw8l7mz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsC6kBle1fed0PxEw1UciMhHhzo7OlAWc-HXjn_I-RAZth40in-1bJ5PH39GgCbo4M1vD6rBEl0_0HJV1pviyeXKmXzE_odpvJBOUiDXURVmlRuU614tgTMb7JTDSDmwVfsiwb4TNZPFoozVR4gbuUR2rIwyJNNV9G2zshZm23rXjcR81eiqteAuWCid1Ry9aQI_2sH60pXAhAMMSaxjuOzy10LEAN6NlldUzqhTj9ksd2DdeGUNdpjhU78zpgUGWSNkXeAfEIz7J9zDFthsmLjIjGuWTt2sp5mdvR-txitMs25AYthBox9RIrCOrdmKE_12zo0lzS0z4b8-pBgtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
