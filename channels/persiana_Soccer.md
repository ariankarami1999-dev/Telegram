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
<img src="https://cdn4.telesco.pe/file/VO2cJssef4P2YPvaPMVzTiAtFQHSriiDGMxFTmSqxnAysmVrTFqLS82a1pREDNLYYqTTU0wwixHQuNdNsj-GqwgIZ5OOSKr4W72I2bDqs_xPQqrt0NwrWBmEQ7wjYiPK6v7GfWjI0cnMPAWJrpdIrPRaMiyLrG3_z-AYfsUdjGszLGAx-esScgEeJYeL_CctM7nCKAlp6aqwFEENC2ufXofmfq32_0I7U66sMjxWWlWD9Jc2BVyX8CtR-JwGISGgQ-t70eDF1eezQ7851htifW2A3FegzVlsjoi4LhYQdPhxXMZcgI0l4Kuk84V7nE4HdvjPe9pAEpv_3BAKnLkLkA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 515K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 20:15:02</div>
<hr>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntVQhJnay-t_biNhDj-9PaycKdk6F8D7zLA9_xr529YRYZ6yf5M6hb3v8BRTyEGwYnMt2onqI3V1vGAUBM-egE-uRctI5iOm3r2TzrTWcLZL8fLvnlbWeDbnL05immLhCjHSjhyVfqcetQdBOhRZp8FUNfNNd_S7XQzyVVWn-5h30SzsfVjbHHcWzAXwbGpKkESl0A1aV2EDTQD6T54HQ9htSEn7__cxaLL498i-BpVxD_YozJCgl3FW4bpPhebUjM6lX88oLPNXwcJFmENf-kqFfRH8XHat5wPD-oquruKR9JqpYKBbBxR87mi1ZhDmtT2nlfLCRMH9SrTSJn1gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNbS6FrDAXcvTuzmu8Tydtn4j5FiEyU7nLZUx-KYYNwcbxSJa0UboVHiBk8HnlINK-wBkJY5I8RdRMHrK2H2Vx14EAwCJyirJqU__9yzE4EEzWd7QK9QCLbyLFEbxCAFS7myOTbY6B0DonK2vq4mFF5TiV4HLh5Bg80lbmdsd7bgCTzQPYESo03QzbMshCt_FHHO_QMxLMuheVqfzeeSDY8HDl2jSama5-WTJGPOMG1VClPXlQxWmmEromiyrGOy2OZPPlrmOR0_9FAbyMzIVlzyJTTFpxZFNGGzido_yO973z5ck_hd-7EiICGXB7WvcGY08MQu-neTkqREr-gbhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=EAMbJqf3oQ8sMyud_PqagSI86atBqirxrWb-vuKuQ_yIxNyg-0X4x6mYsc6q-Rsf2Epy3HaYzEhJJA-wXZwDTO2BDG4tAEpHBqSkEuxf9NAoJhnEjq3TA7UF00wf6OWKylyZsKjaSKkkZ046L7a-tBnqmi2JehZPm4OGNtelnPyYHl5iwjOPAP_qwcS0Yw0VPOLBDzwu0lz0hHT6HayVO-_VsPfmYBV3AkXtJYTvS5MGAXJBgDNXDDiVlwUm2tw9pq7onUERMX5GHlEVhu4Xi5s18_T4t0n6RXKduLa6_eS8k3NhAE77mzhxF_E0wX4Dnd0RG07qQiDjPW5E3P1bqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuAfZjPtzJExFzxg-B2ntzgvj7NJcA82yPuQvYgroIb2VtPOPWirRdyIxlrvcl0z0Ye2rCc0E7t_pGlR3W10L0nbJZ4EbfIoFHZXbeve1e5ft8ragpB-e9hBn0uY7t7rFadV-0_0uJp9p0SX8Xl3rJ03bxpfJmZ-1THWfCs6fkExgxSMSTkynLD9_sRQBCPfWK1XxOZ7FiolPyrB9pUtAVMhAmk6UpS7tBH2W7n7MWzRrkzMwLqm1IpQhHIXvI7j8191WZ2ftM6z1JvZeZxDw3N_3Ufs-co0QKWmGDWmtuHB276qBy4kkzGxkNenXMSeQvvBYTP5JfX07sRMZcn0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqrzsWDt9uj5HDBnY0vh3EscernLFnmaN4rFkoC2E95QffbV91hqnJ6bZ_CtpiAzlmggcX7UWS4-mP-Kh9BrkXCW9tWU_e5iB2RcWZ7rPBLLx1PwXpP18PwaILzSeYIUNvbzj35URkbxm1rmktqfBVVFTS6Ehuo1jU2zybCwhRIQyvhPnOFgaJuTdgObEaqpbB9mFsFR6-DaUfczBX4gCigJ09pPCE-gPuibftwIro5UiLQScJZ1rDH1ihxOJORkpabCe5KVY4Z7oMrXRLZaMC2OzkxsIftjHKXiT4ui89M3V-YZGkkprJBfZgZM2nQXeymLvG6y1BH5F2A7GmDlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKGOy63wrzxyddIIfto0pi3i8cSOWhlqXvtyowgROtNKG5DyUp0WnHVP__8xCYjP2j4HK_s4y68Q4uGvnA8buT7xMm7S9FGwBwRjUxyBwXOf4ih7oyb5HoBC9l5RibfyOCfoq-Bue8Rw-xobR6ww4iddJkXjxEiC9Kg1Mr5c-KSGWXyTO1_ZP75pa12SkR0jaGb1BbT8SmwB3UeuqR-BdeVDvEX4L3uGA3iLJ9HfHUgmdO0zWm9oPmzxc4R0TT56EIWUhhJwB0bESIUFCIXYva2y-9DVBer3Cw_QrZZE6kSRmaA1N8atQwwewucLc-z0oPmlYUJFuKy6j8CfKAVWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1_برد مساوی فرانسه
🇫🇷
2_قهرمانی اسپانیا
🇪🇸
🔥
💵
ضریب:
2.18
‼️
سایت های شرط بندی به دنبال صاحب کانال ARON_TIP میگردن
◀️
https://t.me/+6L9plEThEMk5YTJk
آمار روزانه 90 درصد برد
🔥
✅
با آنالیز حرفه‌ای و تخصصی که روی ، فرم ها انجام میدیم میتونید به سود مد نظرتون برسید.
🆔
@ARON_TIP
@ARON_TIP
🆔
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/25999" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K76ITIPye2q7Zd2O3zdTKd8-lXKjBaEEy7jKT3kxn162JPHvy13snh-os-4eoDv3vUXyJ71soY2FkqWhJZjmuGFqW5lY1agvxMp4DblpCWYzFPruoefe5Q11ap0puxZ46UUDe93XGR8jgmArDmnJnwh9BtlPOgYKjadMT6C3sPmpN0CDHYTp_pYaHXO4O9yWtskhIs158coVy6WOMgXmhzAMANSnGigPQ8BrGxh1eVT-KaT_yS8gVvpXnqAMiRjyloTzpiByyds3CZvqQLYs_L3pkcYYZyLvOK3RKRm-t6KvYnSLa4Li6IcqjPmzcy4UifW0QbbarAwzOt0qxsOpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQQwEkJlv71g1BV-WSIfFaGABErZ17w0RJnSYkqM3HzLf8FNmlNLipSRHRRPrlUr3p6gl75Gdpkm6R8ShYpBaHM9_1QJ1a3DhdGZQpuQbLBKgFtZEYJ3_JaECUgOGH1I96sYTdtRxYUM-GXmYKHePfjx2_yh8BFciYWRGIgZSNjZ5VsrbQOfY4qgLI_YL82FE7ye1PfxK71_22kg6x4k3EYn5L8h04b1zIGDwUyARkG3qc9RQfzAgAJ6pYdesoPElh-MQlqcD-WkhCO3Uip7xHdiKHKl1xGUzy1dTIm5K8yDFRxEG_uVI3Lj_NgbSSyB7v60rLnHuZ4IK-bCHy9uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyDZUAa_VtdKW_bNSgMy6PxNeoPM4ESVmIWGTAAGGaxzQpq3m3a2IICX2Qwcifa1Y_BpT6zvZ72D3yQV5p3VuOwIKLD0JI_vlcwjN5acyem4mHmVtdIE2r6wPLdvACxvcnU8C_zcn3qh9Dr7oaM2sZtKNUBQxhooGJXStDWW82tvin42d9-Xcci6eesyTwqrq2N0_k5G-5yoCB11hOVxwDldmeNfLVWjEQ96kXeM99FkWm4nfSYUuyTXDhCaBLynJ7gfSQ8nm1xgez-2nM37gIPgZOlof_8WB6lTU9NegOkoPLgPuFexJvv7ou2z5xH7mQ3zra23Sixm_mLJFtCnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt3xXJ_Vl725FJVZ1IiKicgwsxF9yA7p0LvZQNPPQSzogXFMmY208G2vf9PreMO7msF8gfoI6vN379cSCx8lY94UhT4rHPKfwXfFquRg6PB2EkNejPM8-_iq-WhtDwD_gtFNWq_xxnM1gKXLHZnQAp93pRWaP9fdaeyzaX_elX1qleEi-BOmhIouUurrRWAWIXtOw93ry7laMmHp-9SAQ9w0ZjZK3CeJVQxAuqK3GV3qJQBN4uI8SR7ZTv4w9rRRPGnMH0rpujiENVYlgqzW9pU7cQ2ckSeDLNL3A2nLmgBNTRb8vtCKFGZU8eX5cCs2UsnvHHn8nwFuwifKWLJOzw5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=uGRACek6CZzol1z6-MBSxSr8vgFv2fEgGLsVKvdzEiO2WSZPnHjB4XXTpkNOqwjJkup3zEg-ZWI68a1VUq9Ni5_34py1a2bHsLhT7crB8BEevc_Xi5nKtrhEWB5aKRSGsK1XkD4vjIngII28qKxQXtnaK18LS4XlErJcgzAxcGxpJNQck0pgGjkMIu9CaigAGDVYiTFbfi2p75WHNpePT8jLsUmuG9rmQ3Mb_CPGm0baVHGVsCZMHGMWR_-6X8MuhrTKHzNZbcgZn-dc7o9oDRO-IVpDlDA1aNXgtsFEDn8Qjqw7D1xic7ver1hmQ4qDz_FBwwtoZ6noWhE0bPvL6mLqebpD1ztGv7_fXRrOSGQJrfirUguBfPk3t0xmy2BuONzfkye2WEzs5tT1AMIrkaiLS7k1pWbLahRjT_T4hZVPePXVt4xiVzjIBgKP-w1YAKhFWY226eUSMWoN608-Vwiw6tn52HUrJgYjgCyXtb2tWMTMecPMh2AJbhN8M0HAl3jHO2zt5nP0o4XLDlnKTdW4h-_TdQShIhH_UwGW4Sv5SOV-nJFBf_PO23phwan-JERBb1sn17iM_G1HE27Xi7sxT40p04CvWPH4pb48Ua9AZOYPpDIJ5DmY_EW35pIUROTCuDTJKTNbxzTxo6U4XBR97JThl4r3gyuROltR15U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfHEcZQIiHq-oYa48qM3xYnESBnUbmYyWpqq_xsbxjdIlHqLcBVkiUSrGlH4qC-ZYDhVCC5bi6-oDo4TPYMu6oqse_s5krLEKW_wuZk0rj5vPGTfmwfTyLeXPy_F1JDrf4KOdI1S6bR2uXjen__bxsAjkDk4BO0xKCUfzEVZv1vYB5xQu39hKJn1hBC-9nn68jOtoXyrcQMdtuGZseeMPwr449jqwhTZcyU6YUhTkjJiilMQy2K1ogzGSxczPaceCvS4JVRNAGCz683pYKjAmBY-RRhTLgl3jsQbtNrHKhfS0aheo3ABCQkSnil0h3gPZ0Q-WkldlpGKHsbabNc02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpxbr9jJmtSjs2SJEE5zULTliOoEc9PvRUDRvZmAFUr9Un_JUkB6NMRyysxbVYUW6VYT6hFXujwfKsXhUAdY97womn3kFOd3S0HB6HghFrsKdVf1TRcy1jHtko6ZoZHa5dvEA7zhzCU5BFslYOJwoateakkZF8wZHCkC9a4uchplIRyZR1N-myDUr2pmyr1hdM3J1SpGwRnXI1AbRB8ynoQWbSDx9_pb-Ui0h1sVSqdfx1UYR0yBegSU1KjrndqLQlX9A9iXK7o0Nm4aDJRtVrPKO2Ytp-6-1AGuP5mbSjc3mNl7OiETXB9ASpOAqmOv5DmNXOP5ScUAsanaQwYVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWjLMQ_B1ubGfPIwrha36UKWIPdIut6OSwVMb9abrtfY3DjPcVZIrbO0bE4gf_t2FDkfRecLd6Nhh1vbPdNiWjIVasr66Od9EdjW9K-FXBmN-E1IWMVJqyEKeP8aWYAvaocGpl_sRG5xjNXWRdvneUa-jxumwH2k4GzbYZgyLC2Xbdo1Vzcw6UKB9YibCc-fF3oGhO45umxskuBufGSF9xCcwsiauJk6OBTaF2ZnOa3gQxk3HWjLfuuU8mwjv4-purr70K-ifhLho-B3d0CTxRwd3OSrLk-KwYXweChLLVgrrtWDUhReyVujJAhQBYHbma5YmY2Yna8ODR8vRVKQ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMC7lz8zOjEcu1YjVKXHR2lv4foUP8Zt0CtaT4clyPetU3TNbz7fRkJ5eDmfIfG7gUzcKePRmQ2DsT7NcQuNNTPWmuNd7R03UlKCRQUiOsFM6dLYbezcqQXXVlgKN_b52ydeMF_cZ2SMhbtKmVmvINmBbZlwwPGXR0zE4ssFM-hZOp_XGO1EQ81B_6V3CMPuq3oacC5dkPGZgrpXCGbgTdVQRszIbfrgLlJ87-dJGnb8iALsuW-v25H_5TaqlhJjkBJxHvUmfZ2qCBg8uKCtHZHQBH7Noo-JrHj3KrsB_Ht5rUBUg6L6I5PG5Ubl2aPCcbbiPAIQPQn-K_YTrIcUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi4gzXHJN_1j3cw4gMCwolOiZaP8N4-9eqQp7wb3eIuWsQAcL_zTK8QlDoyNh2OG9qXqCj3tjv-6j46eWiTWZGWwSKiibJE3d1074ZqIKsiCXfJRyWv0LFhnxJIsPRayLRXvcL0Sp4QKK1q4Ep9bZfOxk29VvH-RXL2NoduTMA5F97_ipwbN1_nKbKioD-ahA7PAGouwLRwkyKtfqgqUXaFc0rc6jSuvkGeNlznrI8M7FchweHLSFe0E9YBWvw2RkmPkO8OVViJ7YphJDsl79oz0KA2T76Rw7wsbhRuidqFpTgdS_bwT7BvrNurd1E-una63FS85I5aj-6f3jyFptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPPlSrofad9kEmVu1ucNgvjcclnAmyvlehcCDl66S76O1kHWXwg4U_DT6w3fac_1MGf3RSwere2cbzSX3JPTWP5iQJUA1kaWho3bZ-9UoQDCKcCTWKfymBA9k3q5ie1dBaat5OHvQsiQbBR6XU3HQfstykE0-jQhQtUipUJQ1KVgBOIqFJLQbD-CEWExeftai4Et-V36ZPEmwAorOG6qKHXeFrmYDnGfYCRN8s5PrUSnIbGknnO7PDjGuIlVZOwiiZXs9SoayRv6uTj2tbg77uQ3mug7Jao-FuwZqbbd1_K2AjCITFPvGnjEQ7Bqciy9V1nkcCTOmaXsaFS5PFfPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/letSSacSNE1zBj5x7PYPzZgL9qAVbMr9fyqNKmZRiNTz_1K4tLThRojlrULGNDr7PukkhsStCsIrI69N51g2FcmMiNcYfot0937WID_NIfi4AqzAStXQNQ6SVH_ZWFJ-As3nxPvtPgTEmnopdtCYMEegmXBaOWBLXrNm4YSE0QmrcHxmyvpOcr6cf53R6AVRv8YS4h-ooPBZpuCjW3xM7nlwaK6PuBzRyQ6LGwF9J0O80nQ_ep15LJlpScEX8XjyZ6rYPtWOGCrBDPOINl7YU-BuyWa3bxjoWdavVD9sw-FEtbGwOaZqH-PqZ3cCK8veEk_LYJ7zilc82wTQR5vqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYxb19mj_Ive4DUdSsZfjcOaqOoIhSO98PrqLsM471ECXC8uXehtSzBMamuQtTRRAc3F86isAV3skG6ZvAmEytcsqdqAt8Ru8GwVFZpk5XcQ6kpaBz6d8yfiMOmXesrNDa9iQ0dy23ByGOHOS-0BMfDwI3aEIRKOT-SYQtyF_uinaPppNFalge2tMizF1aWBatYjSlGZhDO47G1d5u2lVscpbBQ6utl_BKDSAZ-3rqUjnFWxcqmMnNaUdCweDTs32T9-qLXaDuIOhYWhg7fG3oFiPK6ivcCcPYAcaBWCtUoDqt-d3QIflfuLJagDa0YDWAuFsB0Sc7w-HsUMl-fTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp5DHZdLk7b4hnn7zRpL51RkFFyo0i-gIHOUe4Bo8Q6x5BXtcjf_rC7jye-an5jTVpFT4zMUeL2SaV-sC9wpd3B2fRFZ8WoqGcyi-lOFoDbVKeu76fXNGhlLFqLAciGlbY1FqHPUndGx4mNNtK1jsULa2HUeBgz0UChvaf_7pUudT9LTICcKu076gRIcI7jMDcfpTRCOR212NVqbrGUY3jP-yxyE5SCGdtaPxFAOpy834JT5B-fyXT1hL9sXTLkRek20IxrhKLtcbLO8nFtJ4QWj70R4HS1i9OtupS630qIpV0wY1Qks1ePBO-RlWwr8-AW2_ThTK5Fpd82CWCYLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFab79s20IHbcdme0YcNP1wzFTGcQ3-4SNVFoxCovKDm8jDv04a1Z7Y9UsWUIBJ0Fw8Rih5JTyn53lS4Wja2vipheLNIPtkpE6nx2I4xz00xv-Dl53ieqoKWT5wXpjQwKr-4BVCz-vbLOsKd010gjpsC1OD_CP3LBGYKFlw2k9ifOtP806sAaZn3XsRbcvsoepMdolLD1VTxCRMbHgTr2pHhWsFD31Ie6Uffc3SiXFnsakl7QvhJjfTN7Ur0_EAgfalBYCnyOA0IY0QMPd-gqBb4qjEDS9u977g3KWmuJvK5Tc-83j2wDU4dwR7wIF_BjsYJXdnDMVZYMuorGQq9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl5rvXXabkvRgJvwWLmDlR5RYgqu9jGToSKDh_JJdmgWf1KabqdLdRb3L387T9P3sRZEXBKJrgdDeYu-QLY4kjystEOjpusoF8ePC_auteCFhJlrstGo5QlP-IJQgUylTkg4uA8N1SEStMVV8h78uY4VnReYAMf1zxkPmoRoSuG0Nk8sDe7AxhDcDc5fawknYSEwBhZzPOZdCrrz1iW22sAdt-fQFe8mSPOyFxrBFve-e-kwGogYo7-sL9-9lWPxDcAA8A2eXxf4JvpARkUjz_NIg6EaHDECQ6dTUPjPHvNafHTSSyFMIUogrklOVF8Qyuvm0xsSa_SMwtwGdrGBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB5SqCnaWBlgH3PVcuI5iI8Xx1Bq8AKtjA42bXQfGZmrvKwXHl0oRn_1IUosPN5r_kAR5qitf_LakcfZ40JNleQ1758u13JZ0fhrDVPUxgXqQQ517z4byUy5RCPSKcm6DdZAP52YP52iGSYqDWvVTc1l2tYp-y4-WJ9D9kJP7THPxCLh7to-uoSGzzOw8s5ioWt9RJu0U8RsBxtlNVXB22PrA7y06Wim5sksj5ru4Ylzi9Zo9kOaaKkoAdoJwuid500XZvG-oTUkqYD-H3gTBlF6n5kDFybSpnju97FNzLmwcYFwPqPP95D6Mk6WIcgS_NeIJBWRxnN52S7dd7NjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byooo9WLllUMShqtDCUyHpl13gdFhkqvwnGqGMQRBBDwsQfnJIQMnBadcSzuLgmlgelrs2enIB-VBFKBE_nnZ7qeLFdhcu_uov-GpDNgmoDUHOmkbfdGPEoqmkEIMxXdLdEgeFyNuU4wqAqljGQ6JHWQFCLOkV92m3mq343I9hJ6fgFqz9qhHx70z8PWD5KNkS-9aNHcR9Xy33PWo0pguHSZps5Q8CiAJOov1CToU-K9xGDJBytl7LrWMtAtv9_3ovdofsmLmMibpbhBkzDrdnneVLW1Ga6neuMHIq6SBbaOR8l2iY5gmRXVQv3wZNipKvLh0kxp6vN8ik649LmQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce_57n8xP8fj6w8xEnnhaD8iWEYuRCp0E-WCZ3XidBPWcYE9A4KO5DzTj2kMp3RmlRGVhdLWOg69kaRJaFC9E2MlY2lntAJUWOnr04Y5OKRFQo5H8_43XzCaDT_ZK1GJLb6UBShOxp_tRxWlg_O0zWSrOEo1p7RV4qmwXepkfaRI6Lka-9g66qdRK0q5aIdlqCS8p1MU9aNAeXa6IlQlvDqMAjOHVFGw6vu7RDnvSnna9SqSqZpWHvpvYgDCQkbyZT5GIYWsxukJvxDZlhabWmQQG9HV-vjeTIlO4RG2KOwpv03xlULwUYhRbNTx1lyKwLTdZMTQWJazerOHBTjhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPfZ-4_YgjAumi9rYQ19hCSJ0NnRQSrOCPOrNPCep_t2FggqLUSFDyorZm3dvcB5jP3ZOjkm-gqUgg_o21Ohl9dh8Iw_3NuRmcRe5EHs-_7MzGYBDrwD9Xyc9REerbMdS357OPlVMtEedMRTUyUMfvYo48HIRyGq5szyEvyvgLZoM_Bqfd-Q_qk2Fjc1dohk54c7xqqlnu9QQudcHdV-zMsFLtqbHQuyh19Z8jcMu31FgqQBRVFUXP8K4LOuy_ULpkzUJ5LsDBGuAkZBNXxi5dA1lmmMByLF6Yz39JGEKxiwp1zC12gahQpPbUjNdBQbgtRD1fcrH2j-t9UuAO1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVc5TroZW3eTXjs9abQ-L1EszDL47znjY3hazgu2Pj_z30GcXB52lX8OrSydC9LVVXtq2XILvlKp5vsAz-VM-wWG76DF0l2STcbuA5AAx3_6xvQJSoloroHnaamyNDKb-KeTtbZJTErDcDyD8IYi6m8sqwEW8CLz-tdqgZsv8fnJJCsYxEa6xBVCC-qURAvMyqdyXvxk4IZo86KZ1fj_Fc1_O6YQ4cFaIp4aoLyirG44qUP-TSuq2DudbXM72_5n3dpzHKRCTJG-7g3jegWB_kXkc03WAw_3bZtZ-V-9O7lqE9lhEpVMAujUlPwPYu-GHBi2wp59gZ-fpPhI7YtVOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnN1IQg1SXn8tC4h0MKvxcb0qkmzXNtqLFeHQ2333Wtz71zUz1m36Ohjjlovv3kWqIPaAcXogjaQAcxM9ghUxIIRy0ah6sL_RU09I3SdcddhLwOSD5YJz-y0W86zOqQq8MqXyS53DwzUUIHNpec9DvMt-M-OUIoSSUtNCYE9WXoSXoMuUosiFiG8XKBL9MMcA3XRg388hQBRHnXNkR7e9YrZHxsY3_EHujxxgmliu4AjtehlY33RRFuElrZPqzSnjElJcnmXbTBNRJIhfcpxv_UvxmIrYAC00IZf9tZOKi9-2pVeceLFuAkvntWYIYXc7-lNyWCWnaQh4BTPPGuRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e239GC4BC3IjqDOipMysJQt39GxZ-wY5LVRx195e2iGyp30O7C_eOVEv5D3GmSR69GAkvIcDTeTYmEJaFu-nZ8bXRiO-E33Ka-3X9ZF2EzNYUFRIXi8V7rq-WvufrJltm8mQlilCDPz805TI-R40qNhzh6y7VJ_wP5UBLBdb3_TjMRT9fCwlQQDpoT4aNBODPwhfeY6Chtye9o-V-vi0rxsfQKunRba5kPnNXIXuB9BFVdQtM4D08BkQU3zp2M1DuQRkzaXafHAGovApQGuVZPs-yzRn5kEMJ-6H0h06sc7NPITJ-sXtQR1a9IKorBLnZUmwRKTGkU4esl0PvWChqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gx_QqqqWiIoBaIP9zlW63Q9KgWxOuOGG1zbo5EtuQabaaH0OfLoZsKx_VcMuloMQs963GLRXOADYMF8cM1wAcxoqeq8StHw61i-fgg8mrZH8SWRYShZJIDLF5gMDscx5FqYzXnjkHguWNdEdqfGAIrHUHtQ6T7S7gNyUoN8oxqkWJU7nIH2PZvpAOt_KCzJN-vpY2j_VP548W8PaG3Hw5u0IYEkjXwTsW4HFQcDs4uSXv2WVYWGh7JwSaR_GHXgCVE0VnX2BuwWDST_9JKoCKduAbf7K9EuqZfiLJzBtt3-K4LpSQalwg_17JdMS3R6cimS_hSGCunrht75ghaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKNdW_F3KqkzTcIo3C1-WM7f62OUNVKjmMFindwGwMRXG_Da2cm2o6Xm7q5-9aXiIUlqRbcFMxTTo1lSDmSjo_EQ_6aqMJ7zWbHqHKOAiZCcT68d7kPiax5ZEAWqtJeDfIoHyuDHppusckEktaT64odi59vDw4oHwpq6JZfqHJWS_zh7O2ffi9JvoKI5tdEXkoM5W06yHdREtu0gW0zwdBt-kpqYL48VigAypLAXsB-SQ9KbfTCDwMJpe-Ntauoh3aC0thbiuJ4gBPwQzhj8MrMR4UIjyMIK7x98aua1-EAXSFar9H-ROS29WKTN0gs7tUyWUE5tdRM65qEVR0PnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=NQbxTB5aP2hMHtyPeCGBN5YeqipB6x8ReCmzGaWu-gSoOCKAZotf5o-w_mLkcStMo1321THyeQZxu0WnLksZsRz1KSU8n9WllNbLSPELgCxRiIojJpChgqpxnFsd6by_kD4lQuzZPnswuOSymMd4v38MCao6oSU1tVikoQkqVDutD2mA4p8QCBsEgF4wW21oqqmel7sRS99BNEyamlj0TKYmTGFGzrcfp6zIuxPuOaWP4hlxRs-u424eYArNToC3vomETbiXfXEyFyFgqBYBx5Ao2IOflYq4cDImmxbdVaf3PXyPKT2B-mi0FCyRObHi1r86IhnVB6ND4sWj5MbVjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSC7O6H3ZPbAwtKI538ttRGqpnFSAz1mSfsckRv4A1CUh4-dqnycFVricus-mkwI-QjNXYVQusq_Es4jRxknfTpMX99UM7qDoEROUofm49Vw87n56QbMachAEeSRf7HjzLPgjUtRlwPGT_Hz1REwfwHt340I7c53PPvFqhbQJwT_H71j8jas7Eu8X14uWblsnUUZu3ogpRSUgeQVRuisuVzug-E0xXvuYOfHUHtqlBZUnYoj06s531IpI3KuloChtQk_6ujPPO1FqgKwGkZw2v0u6F66g5LDv7uKwlPuZk1z2mZoM3YUxUT-qT6JL8_IN_NfOt0tlNfY6h0lse6WBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwI6XqoeL7xi0vk-ZAW687-dWSIRw-2WWjV__ft3hg7anvDhz02JHZQirZsVDV2CgAL47iNU3OTYFodOuyjo7QLju5CjvxffpmXHwkBK7w754dB0yBuzwxfAnATRjUr4qSjHRzgdh_EwjIl5kFiPKZQfG7_RGZpywJS6FB8HRzdtjjY8rBAGUFVJLkLOpdZfH6TM2GqGklTfi1mh7Zq_R5NPYIjsauQj9vxOk8X7nQb0nCpSUBg0nbQcG7HCeP_VgG-7LSbGNb9o2e1KTLnmm1YUNGn2iTu6tZlTey-Nentpdvl96RKuF3nKm5B0qmzuQKNhKjfJ7BjNVdS4JCLamQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پیش‌بینی جدید پارتنر لامین یامال از نتیجه بازی نیمه‌نهایی: اسپانیا بانتیجه 3 بر 2 فرانسه رو شکست خواهدداد و راهی‌فینال‌جام‌جهانی 2026 خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25971" target="_blank">📅 11:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk7Wg_2SbOwTuBqzaNRagWIcOHYI8mmCmq0SjdBpjHMmKb96PiUqzT3l8NZOWhbx6VLFpJEQrKVUqmSzwQ3ONeclMXpZlMzCJMAZk3ynS74IpzlZgC0re9om9rgE_ReF04HWyARGb8bIt0pbq_KRkwodNlbH_josMwis3BHNx91T048NonL3PL-aV6879nUSQu3DYmR2KoxFv0MzO54Zx-ZSp0r88HZW0Zq8MVJNy9C0NTiG0gtPfWzxsZtPd-V1B9UnOfKHSNL-qkpZtEY4n_gM5-vPEVUIvu_hzsfbigR45FdgvROmKlpTObiYjYrOoW-c3ew_JSzZSBcp4UDNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برترین گلر های فعلی فوتبال جهان که بیشترین فالور رو دراینستاگرام‌دارند؛وزینیا بادرخشش در تنها یک بازی‌مقابل‌اسپانیانزدیک 16 میلیون فالور گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25970" target="_blank">📅 11:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrWEqnf16GrP3-gRisdf-YThIYdoTIDhFPTsEZfo0aolJU5jdOWKcCk27zVvCOdyIAcwDJUfWcV9Z5TC6Zz-R5gmgdmASJ1WyJGhHYix1RrJyM0-Phyfjc-UrrFrl1wGCiIYoqWH4zP93Xld2D-0T5quwYbNs5XBZYCpztkdsexyKLTnrmh_9k7AyleHvgyXTZTA_MZrea74RafO4WTDr3GAL8S8de7LGQkbVLVByJSGqHLpiFdYVhgLLD9HgXv3sPjBHQLkUSXBQXXrODHG4GlsbgN9_YpYgQHtBBTxoq5ea_-Jmvsa3O2QGftgfzXp-cdfEYLVvY0JaNB3OV0XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25969" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQLzrtWiw_Fllx-haSvJ2Vx8d4IhRDdBa1Lk0TVGCgtkLOa1ZD8alvnR-nenunLaQJa8wULUwr2BMZSdCu__T_-YVVLD4PWSVJIlD4i6fWMy3Z376CeYIk-1E8xqYlqM6RYgpyDXAstyxGWgyIPm0Xg_ap_EvmOpqzN8zq15_gWBuk_V92uOnjcWp7dweXydKL8oHqfl3dwwRBXXeuJxym_M3tFxmpBoVDeuU4cOsPFOb9K6OYrE4lRrJpKgNKNjV9F3588ryE601ueSs-aXy8tjF7OrzsoFYpmNSGelkoB-NlCspA2RfoB44Qk3NGbYvb9UFq_Olk76lOJn-b4Yqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25968" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=JCFAQ3dPcydpdwZpiO2PveiGjt4W946WY5fUlx1MTVeVP5zMkgtox8NNlC8j5hS6Z22_N9lzAo3XuqTe7SPwOCL5SSw8tduVwodzKd5FSXbR5Fc6p5geSVDcK5E8TJME7XofdaUdt9ISyWpwLrhDJrrbW2pdIay06COASTX6yVKREsaerkOSY71lNZ6HWcbJwEL97EVn1nm01h16SZz_ZEmG82q4HPJImJRN-Phzx43xSwLwpVtkOrYFAst4lX0nX6O5FVQqGlNGLwrxjJwkw-ikEdaDom2IVgmkSq3mCQk0sdpZy1xzES_UFOloTrQ2D-K9JPmsKJvj8oJWU8l1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fe4cb625.mp4?token=JCFAQ3dPcydpdwZpiO2PveiGjt4W946WY5fUlx1MTVeVP5zMkgtox8NNlC8j5hS6Z22_N9lzAo3XuqTe7SPwOCL5SSw8tduVwodzKd5FSXbR5Fc6p5geSVDcK5E8TJME7XofdaUdt9ISyWpwLrhDJrrbW2pdIay06COASTX6yVKREsaerkOSY71lNZ6HWcbJwEL97EVn1nm01h16SZz_ZEmG82q4HPJImJRN-Phzx43xSwLwpVtkOrYFAst4lX0nX6O5FVQqGlNGLwrxjJwkw-ikEdaDom2IVgmkSq3mCQk0sdpZy1xzES_UFOloTrQ2D-K9JPmsKJvj8oJWU8l1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25967" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p190H2OyRt8qTQIzbWvWjKLn49izLRuiUrtYbId-pEA_616y9QGYU9QgKZ-JH4d9_KgTL2clZI5et8s0IYvv-lI8FbFhKUSNpsBIUL7PiFIPOIVhZX9OTf6rruyO6S4xAaKYzXMJFEiRodm59kJKet_AMpHswiBUHJ8Is5U1MsKVbKtN0_Dcj9mdKO5MHBgFP0YdcPvozZic-5gfIX-7CeKf67tUs_8TbJv1Py37gO0OE1mGNAZCkG6LSFPfD3AteHtTgJKCKTTF3XXeNX35bsiecO6hAfRI_iTRdbrYTij_Cc0MGv-gAVST5wyU9yhNMdtR0tivrYXdRz9rCyPCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr27
📩
@winro_io</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25966" target="_blank">📅 10:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEvkHzJPU_xD5fncaS0RHPCmefYieGDqx7jCPhgFmnFHoJ7aU90i5Df_IOh0akNxjqShE-VUffa6Rtpj5Hnz3C-FA_XsRF9-Lvp7cWXum7OAFPtRhqyNmAA8Z9vbg2aLjx6XVRETCwmhV0vk3E6AxzKI6l4teANeVeXxbpMiwEyrUt8aGyQx2al5-gQ6o038DYjT58cXIyG5zBZR1oEf6_FyLS3IcrQ6GRDFy86QeL_EJpB2kwrzAEDrLP1k2GNT18u3eVYabrSoAVrS_CXI01ziAy7oY8tlQCOX1yGPmSdyANujPssBuEeWhLAR23_pgrfpBvSWjDCM4kYiZRGVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25965" target="_blank">📅 10:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSeT2USR-tjMBy9BtKxVJIh_gvGE3qoc0EsUfrcjV97tndyaA7wksXXOGBrDtZaymUunFqrj47hkFN8Z6Core8ybgvNkw0K2VoD9K9aMg0As4FTgVWqFOCy_bOxLi7C7PfGmL9FYaI0GNzMHZPP1q5isbxIwCnqFzurCCNG2H6hME2AwvftTpDUX4awOFfwXslEcEuhsFO_L2EkpJ81cFSOMBN5x5UGp_0X54ZG2ZO3mu54EcJyrSuCtBZ3u1Y5VqYSM1pqq3mdIYzD2xNcJIU2pRqYSrsWrrNI39LmMy9UvGkotioOlN6eg41Xlt1efqlTvxPQguTa9ZpYO9npkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظات کل‌کل پریشب وینیسیوس و اوتامندی و به رخ کشیدن قهرمانی جهان توسط مدافع آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25964" target="_blank">📅 10:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=q4UV0Q5ZuptC_oitGr9GmSt7z8MYsOKpclNNM5c2XbHAhigqgefmMZW6L1A__v6FftpVRzb05q76N65DAq6uP-388HlgwTX578XXPydbS6t5LR94pTYuDR0WB2Yer2Sk7yawqRNmTtKLxkkQuf3iv70y7pOMc4KdLP3l59W7hA3egOaJyAOCuu_Ltyrn9_cKX4uFvka5_X2Fs8rAyxIFlQ-BKhwq6rrKk16uQ_l3meBliJzh1-j1iX_rGh0EiHfqmiKs-5_lZo71EC6LPno1vY9Qt3ipD2BQPowpzaYaxfX1XsCzt84AHDiocQPxxTQzcKGx9JkCtj_e9dauChTQGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3687e3b81b.mp4?token=q4UV0Q5ZuptC_oitGr9GmSt7z8MYsOKpclNNM5c2XbHAhigqgefmMZW6L1A__v6FftpVRzb05q76N65DAq6uP-388HlgwTX578XXPydbS6t5LR94pTYuDR0WB2Yer2Sk7yawqRNmTtKLxkkQuf3iv70y7pOMc4KdLP3l59W7hA3egOaJyAOCuu_Ltyrn9_cKX4uFvka5_X2Fs8rAyxIFlQ-BKhwq6rrKk16uQ_l3meBliJzh1-j1iX_rGh0EiHfqmiKs-5_lZo71EC6LPno1vY9Qt3ipD2BQPowpzaYaxfX1XsCzt84AHDiocQPxxTQzcKGx9JkCtj_e9dauChTQGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🇪🇸
درفاصله‌کمتر از 48 ساعت تا فینال جام جهانی؛ لیونل مسی فوق ستاره تیم ملی آرژانتین به این شکل به‌تعریف‌وتمجید از لامین یامال پرداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25963" target="_blank">📅 10:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmn-vZ3Hh2X_4Gjdb-3IDY36hzYi9Gr5AnVVmhuflrW4bqzR1h4peZqRoWAqBPW9CQCiGYawKJ331t5PAw3J0uv2OsTM6syExZnPLHn6Csg3eK9GbqPAlbPvPjoZu39_DTcjeFoTirAyQjhj1lnkhb5QuxLuBnrS5aKpUE9ajlc1t66uudOR99JDk4hWSbUJQviw1cPKqDaDyRYI-6V3rk7YQZbgpGqozr6tpvsB5jEdCdn2vj8qA-v2nCUkQKF3zpCiw2E5HoBG4orNkHLbaQXeLITOCD9ZwjAO9-6YNaTD5_Ox5D7EsWVgIvSXkaM3oP3eecNHU5A9_Ur078n5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ همانطور که در روزهای اخیر خبر داده بودیم؛ محمد جواد کاظمیان وینگر پرسپولیس در لیست مازاد سرخپوشان پایتخت قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25962" target="_blank">📅 09:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnaGoTXz5BGXyRW7sa-hiYhMj-Y8LUcGH8HdlKdw2nrcFl_IO8cCxdR64EVVjRV5A9KRXC-_QFkE938_-lYE1PXxgXOLquoDsK2GhbhlVlUXwEMehZacZcjaBhAyZcegUDAqYnXdqxZyFRiSQed6jhR0dyyDOfI2thoZk9ZiBFvZBHpce_K7EFsh2_cGQT3JVbIO5su5L8VWVGsFzZ1DE0yXKh6off9cSvppX-oPUm10mbAeqvNcJFQv2lkOtdcQZX3GRKT0UP7juSS_nFNsUY9RVd5gAuCLlSW66L8RcKJj79XZcy-Q410LQN1q1f4ncgvizh7ew1QwUqM44F15-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
با اعلام مدیرعامل باشگاه نساجی؛ باشگاه پرسپولیس درصورتیکه رقم‌مدنظر باشگاه نساجی رو پرداخت کنه این باشگاه دانیال ایری و کسری طاهری رو به سرخپوشان خواهدفروخت. زندی اعلام کرد که طاهری میتونه با قراردادی قرضی همراه با بند خرید دائمی راهی پرسپولیس شود. تنها…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25961" target="_blank">📅 09:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeC5RYswVDnwg8egxJyHqqeIc_RgVnx3twe3PA5SJWq0SWAemYnjtd4UKQY6vZ2RizhYJBSdF75w5uR1N9T0i4EPHEaQ0PmF-tM-KfYpYoMmivvF2CmDuQ2d4b9nOxvIIYVI5eydWH_WJ1pc1F-dFioKVLl6c_vWifxhTZkg746F72u1F8G9Yprkp6zM3Kf4bWjiB-nKxMhLwIgb2m9lYrznMBPfSeHsiccf7bZI9BnRiiDevmRrWUWftnG1n69O9esdUgUYnL_204U5GVNsGj9P5KCnDGToVYsJY3u-ytlZw65F4pJAC4wmY0fAPW6bkQbdvuu81aB-DCuwcLRrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تنها مسابقه مهم بامداد فردا؛
رقابت فرانسه و انگلیس برای کسب مقام سومی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25959" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxJ7fpzvG8CnEXg0G6iYF7Lf2w6RHA4N6WsNUIeCPxhKPx604PqOMBXvGyBG8khJl0eWNnvslsCnBWFFAZSn-pjVkJSp-mq2jlmXmIqXpOrmZKI06HYr1qXD6vFkaXuTI79MNk5ToDu9_SHX3pQgEFz8lA9v5_zF9R0jkz_-4UjrRfZFrdPRKhrTBqUpxdm7D9VS5OybLiG6nPChoIBohbaqKMOpIFyLFflab-FB2Fzw0M7R5wMkv2jMG-Ajiedu9-8fLk2ZftDPfPupo_fJfItjABpZIWD3j5oh4V8Gse_fTw4RKEIGMQfrsUDcJw3s7BZvO3EN6034-aefA3t1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغذیه بدنسازی‌ویژه قبل و بعدِتمرین؛ چهار گزینه پیشنهادی عضله‌سازی عالی برای قبل و بعد از تمرین
‼️
بهترین‌تایم تغذیه قبلِ‌تمرین‌بین ۳۰ الی ۶۰ دقیقه قبل از شروع تمرین؛ بهترین تایم تغذیه بعد از تمرین بین ۲۰ تا ۱۲۰ دقیقه بعد از اتمام تمرین
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25958" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=bxSrdfL2lhd7JrawxCg5q_ymeq4GNUDvoKfZDabkRht-_SiGlICIzaSl6NTBCgybJn-FWUi6exdC84LFVnaL3DE3jX5stbtVJ5Kaea7Nb99XcISj-pKzGWz5_h_rIi9ThsTf2Sx2HnEx4bpTYJc4k2Xrnzochmi-yFt81BOKhLHV-kxDHz2yB3ln6lR2S5kPsdDETxgxilVj53nCJ3fUWTo56WbxBLFJ4hOEh9OrHXdfVc3j2_149-xs9LIXuxUuNzyqj-kUQDcqHQCuQUj0F20KpnTyrFzbtnaOS6uNPxrrpia5IW1lSRYM8xa8GyutsmIiZdDNjr7rELssTcXzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06c4bd948.mp4?token=bxSrdfL2lhd7JrawxCg5q_ymeq4GNUDvoKfZDabkRht-_SiGlICIzaSl6NTBCgybJn-FWUi6exdC84LFVnaL3DE3jX5stbtVJ5Kaea7Nb99XcISj-pKzGWz5_h_rIi9ThsTf2Sx2HnEx4bpTYJc4k2Xrnzochmi-yFt81BOKhLHV-kxDHz2yB3ln6lR2S5kPsdDETxgxilVj53nCJ3fUWTo56WbxBLFJ4hOEh9OrHXdfVc3j2_149-xs9LIXuxUuNzyqj-kUQDcqHQCuQUj0F20KpnTyrFzbtnaOS6uNPxrrpia5IW1lSRYM8xa8GyutsmIiZdDNjr7rELssTcXzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌علیرضافغانی از علی آقا دایی: طبق قانون سه بارپنالتی علی آقا دایی رو تکرار دادم چون ابراهیم‌شکوری زودتر میومد تو محوطه جریمه من‌هم‌مجبورمیشدم تکرار بدم. علی اومد گفت بجون داداش تا صبم تکرار میدادی من باز گلش میکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25957" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baIOoEeDOhetGv9jSzkBZUk2iTdhmbuVueVQCQQQZ6moV-BLIVAKvg6Da0ZbQ1f9M-lcRg8LNTm0-gNezQhYyiU1ag_53RuehbSsXUr1EO35VJZmHnc-vHkblBC7xEPazjxoSqnj_MNaF_-n2qdSC8tAC0HtbuSgZFaAVdQqdrhbMYAakw1qvWasn3uMaxGWJctPfkn2SnVPoBpPC4k2mM7Stw5Aqm3E0EtoGH0cqYA2R0XViqdMi-JTMHD37vA08ewySkbc0mWlFJ2UJQKhXy2mv3G9exY7n4d_kwb6N3ctcsPGDk3tYEdeXQLTWqLjHKYSaWT6rtEaiSG0kNoHug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25956" target="_blank">📅 00:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gki1NtmWo0lZZ_7sZmNQMmdjegBLPCSS1Hr5lROu6rVh9P5GF3z--ZXvEwt-_Wa_-lov47g9ghaT6IiKIO5XyJgQdd3K2UjT-KGcngeo3ZUZ-rnCMnpfmoH4fHuw6-ukbyvPYdgLEWswVM3kdmqFFoldgVU28BolKGjRpASDtV_FEy-MMVKwYpsoPZkbg1PC4hQxA3XWNg3nvhBu382bL-m2rlSAb2TlDpsh5A2OYs4pjSxyCPJPP0560aOccAftD6G8POtzYqSEVn51bAt4PPCnUUXjtoXeHoVMgH949Tryg8IcdvKmIC4iNTqv2VXyf-UOvfxk_aDzwt8cGVYMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
👤
علی آقا دایی اسطوره بی بدلیل و تاریخی نه فوتبال ایران بلکه‌فوتبال‌دنیاست. اعتباری که علی آقا نزد مدیران‌ باشگاه‌های‌ بزرگ‌ اروپایی‌ نظیر بایرن داره بازیکنان پرادعای‌این دوره‌فوتبال‌ایران حتی از نزدیک هم استادیوم بایرن‌مونیخ رو به چشم ندیدند. زیاد به اون…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25955" target="_blank">📅 00:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3aBtZYVgr6eYld5jLcHwjitiGhTA8z1IJT3sEsVkIqI3lKUgKPIl9rx5fkjkqON6A2g3Nx8-LdoiacU0zVlKIex2KADVChmesYVjedZMBvrgNqA8CdYf31O52n6V_-jA1eleT-9X5WQlPFYrVu9t5yYjx7i34H8nEnx0HhHbfY_M4anwuzbcUvV7xI_er-8Lxjs8gDJ9GUZWdQt901rN11kkGrwR8uhawOB6JMIrbk0kbj8WQ_HYpRU-DON9CVXQQe9LDmBsHdklKdWjaaVCaqA7IJ7bG0T2wealrX-JfPkwidSzOoNvdhSa1LmcOnwU43_egyRMXdxKbJlmXcFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25954" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLH-XADCRe0AgMBd3gWihahb9IW2QFyc5CsmgyYWzblRuDwDkiKImuYEHKnvNLjp3AtEeHO38yV0GrRen4x_Iqg-8cmNnnZ8FXttQ0QDQ9VPCt8oi-fBezOBL4Z5xY9i7QiFYHAKrIn7clAMANY_4vkP4iT3nEWb3fj28dS44FMMmDE7X-RK2FldfhwjHbyg_RbAGOym2sGjVPtTR8HPofKQDhBSm0J_yBId4ZgP5hr8GAfVYZBXJYTZVluJK7NaM-6JSStBdI7MVQb9etR5CKlpvunWHmktBu52Jfk3Tcz7ysWhya_24UgrHCXlwNCDf-Y5MIHrW5-Wpfjw8252hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کانیه وست پیشنهاد ۲۰ میلیون دلاری سران فیفا برای یک اجرای ۵ دقیقه‌ای‌‌بین‌‌نیمه‌‌فینال‌ جام‌ جهانی رارد کرد. کانیه گفته آنقدر بزرگ است که اصلا نباید استیج را با افرادی چون شکیرا یا مدونا تقسیم کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25953" target="_blank">📅 00:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkWg_xW4COSKErgx42hk6a8I8oYsNIZHgjUiJQ86t7Je27hRLcMfpmj9Y0tlfWSpQ6RYKUitJTl2CtWupjO8rYbjbx2OusPXEPiKPhuoZLMMkrCYS803Of2t1omDemm6ybh5jI_TRJnT-JWoQkim-uyRy2ZbOeph3tAZwKm9XwSGVX3MRgVaqWPIee5gO-Qlygys47Vu-FgB_NkC6QCTGvsMsv_rTVeUXf2eEXGK6dNzXivAdrtPFnL809aWsVlNLIpSY9qEWms3WSh3zCEfjx8ZoW0RL6kaefDENKG-kSX6eJKj4vR4Ng_dvmz8Vp59gWQi8wnTwRXFFLVrrfg6qFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d160628032.mp4?token=pcHd5owqRxrXHGe6rqWUNr2HTo63M7DxdCTkKevu9LBJZJuzDZlrA9-qULLawf729-H5Sj3ees0KdJCQfY2XAAgVoSft2TA6baxD5Hxx_H72vA4QK5-5DDJJjwq_lLqsNNnCIttl1DNoAPQawkFxK-vxlpkUjSSv6mFMU_6quKWbr7WPq1oupna6zjL-gmjM0jKRRpRK9ji2JOXiQjNShCB4CT4wdO9BxjRuMMRfDhp28p-lvK6f2l9ov9tCjgUCHUi3V3d969UDngN23WFe0LZVFgcnyY7Ivmtmh9BNykkVWXsjeuz5TEEi9BIB7Cwltmp5bf5lHVnIL9y7uMkxnkWg_xW4COSKErgx42hk6a8I8oYsNIZHgjUiJQ86t7Je27hRLcMfpmj9Y0tlfWSpQ6RYKUitJTl2CtWupjO8rYbjbx2OusPXEPiKPhuoZLMMkrCYS803Of2t1omDemm6ybh5jI_TRJnT-JWoQkim-uyRy2ZbOeph3tAZwKm9XwSGVX3MRgVaqWPIee5gO-Qlygys47Vu-FgB_NkC6QCTGvsMsv_rTVeUXf2eEXGK6dNzXivAdrtPFnL809aWsVlNLIpSY9qEWms3WSh3zCEfjx8ZoW0RL6kaefDENKG-kSX6eJKj4vR4Ng_dvmz8Vp59gWQi8wnTwRXFFLVrrfg6qFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25952" target="_blank">📅 23:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL4sZQgYZc9x0eyjXOctev3n-VdzNkHBAYTkgwtrc4jCSi02etOfM0jHllicRPOwD4MoVbtMS8_5yW9MDFHQkmhfuL9Pa2JzjrdcsERJZmFsS8qHmSGuKyn11WyJfFAUdaWK5FwHFiywPFDov0U0TMfR8ecgkioF8X6R47QxbTCNQ5EmYQZiOL0iRW2sUK2EgY8Z4Y7N6rhXVr4ILIaprjTbdi6DFJmtOQ0UVs4WgpsQDGXpAAxA_do4-xF7a_PnmNhXCYB5eixU1tiOMJjd3qBAkPesPXwo6Nf7qCPj0DFPlyQLkC-x_T0EuKM0vM650yl-AHEHlNukMSyqzbwquCuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33f152b80.mp4?token=IZi4E3JPTYStTEbepAXcvEP4lfrZmEZA8zfUcbJ4qadPvdbmmLsZn5ZrM9FeIE2gEBuuld6dXnYhLVSID4I-3ERQ22rsGuzokUdsBO5vqXz1ZqGGSF3hNBA7DUElTdBB5FT_Cy3xwaYgP3nTjeqoC2EfC4QySqsn2hIgKbxtHvpNN3o5nWUzGLCDs4YmNvl0M0XqwC2X8-xWP8HCcx3eugYTQwA8F73fDBxEqcwY7AGuuhe-k-ic1CEZiLq-6Pr83wLoQrFbvGmJQv1b58-hJnvBHIOL16DrO9DWYdfFHJahRk5tQjUnge0gTq5oIL_v71r-mqgh3Hu5F3Jq0EyVL4sZQgYZc9x0eyjXOctev3n-VdzNkHBAYTkgwtrc4jCSi02etOfM0jHllicRPOwD4MoVbtMS8_5yW9MDFHQkmhfuL9Pa2JzjrdcsERJZmFsS8qHmSGuKyn11WyJfFAUdaWK5FwHFiywPFDov0U0TMfR8ecgkioF8X6R47QxbTCNQ5EmYQZiOL0iRW2sUK2EgY8Z4Y7N6rhXVr4ILIaprjTbdi6DFJmtOQ0UVs4WgpsQDGXpAAxA_do4-xF7a_PnmNhXCYB5eixU1tiOMJjd3qBAkPesPXwo6Nf7qCPj0DFPlyQLkC-x_T0EuKM0vM650yl-AHEHlNukMSyqzbwquCuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب حسینی تو برنامه امشب میلاد کریمی بلاگر معروف‌ و معروف ایلامی رو دعوت کرده این بخش ازگفتگوشون جالب و شنیدنیه ببینید. میگه  قبل از بلاگری نمیدونستم ده تومن چند تا صفر داره.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25951" target="_blank">📅 23:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzBINvXeKBt9CXxrfpiwM9FL_vliWMJpLaEJUHHZeNol7kinQymdz7wfDIDtMD6ZKcECYJ_GksDqODkElTiMzdo8YYHHRxBcc_vHCnjhIJORusszcmkbIKu53vrgK46pH25OFDVOK1JE575OqfbRHSdMgVyf8kaDR5Od7Pg_KNt-rlr6xn7QslhLZs9-p4c1lQolwmnJSYnqFeYWPmHyvlHnfVfwU8G-c2uMDxk16RlOuxoC1QY_60jiwy8k6BOzujP3F1f6L5SlR-QB7ivrvF265nd2Yijhw1NBCbw67z5Orr3YVJ0Ih2dXGr8uK3HDLGMcCMG7u5B7cPpJAoj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های خود را در تمرینات نشون بدهد گلر اول تیم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25950" target="_blank">📅 23:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=OzLnqqtm8r9AxnUVIVMoj5frAIGoGt3DEkmtTkMIzBVOAfVntyZXAldVzsjGuOyo91PV2CtkNiZZfxb9ONCUfjRhCTKz33MeXZed4z4hErcrSNkGxv_xQ30tyqs5b-j4X4aigvZkHrNBWUm7BrSGWhic3hy5HU2k4Lwcn-JJv6KvLjLl6EHheLsMj5Fy3YatIfgnUWdw0ubRyydZGpgJ9_0ZZMliltXDJJjprFxE6w_0ovY37dKfFA82orNTOtC6hyhgbWk9hUltBwWj9bHVp1s5fIWrF0V1Qn2nF1Hh9vrpp-ggxzm_F-pntgQEzcm7ZY5ZpRk9ZXV94cOH5Zgfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e604eb6c6a.mp4?token=OzLnqqtm8r9AxnUVIVMoj5frAIGoGt3DEkmtTkMIzBVOAfVntyZXAldVzsjGuOyo91PV2CtkNiZZfxb9ONCUfjRhCTKz33MeXZed4z4hErcrSNkGxv_xQ30tyqs5b-j4X4aigvZkHrNBWUm7BrSGWhic3hy5HU2k4Lwcn-JJv6KvLjLl6EHheLsMj5Fy3YatIfgnUWdw0ubRyydZGpgJ9_0ZZMliltXDJJjprFxE6w_0ovY37dKfFA82orNTOtC6hyhgbWk9hUltBwWj9bHVp1s5fIWrF0V1Qn2nF1Hh9vrpp-ggxzm_F-pntgQEzcm7ZY5ZpRk9ZXV94cOH5Zgfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علیرضافغانی داور 4 دوره جام‌جهانی: اگه توانی باشه در‌جام‌جهانی2030 نیز حضور پیدا خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25949" target="_blank">📅 22:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUHRkgltTTiJVGXLD7IRNG_8ANDiRP3mU7nq00woWYz1HdcApik_5ynodTlv9b631URWBXwBeyKHc6RHCatZc9M_n-tlrON9xWwPwoxOzGf6jzslN5Jb-coSF9BG7yWCjNiDqssV-P3xPlwotMSts9Da79lPTmh8M4Tx_d1azP0ghBLX2MT3KdZj8EZkqr2HUFxYAiD14yH5EToYJkeuyZubG4o74FU2wf5XPrdDDR8FizcIWqw3ss8F_ki6X7ljOjru50JLbgyaEbQtj-GMe4XDsth6O0WiZqNyEcI0mW4uu9ZKVRRIS7cFSvQtkETfjxINodvwNHrswoRg55d_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25948" target="_blank">📅 22:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=cjjX2ZQFmFKYpeD4b_T2q3W3GzwwSpYG2Hd9hrsjJDFCBrlVu5p0bUP0hnexJQNx6wtR99XDCJQfBBWmFULG_hYSJkoTlsJiBBLHGw1FfGGoWRr3jIYR8WDH7kjeYbf_QR5kCoHS0hYQwekt-F5m7sAMPGhNk8iylOt1paNB76NGXWZVeLSgU_Q6Cyqw7wfQwfo8DxVR1RC4XyrRqd90F0GDRTd-On-UZbs0o7eZqA8PU9j95RU4eRtt8YwnbmytQETFHKfniRAtDd3uZI69CZpjCNeCCpWnbEE5h2m-l8FiFADZVvLhvtIb-AiF5W1br81VLw6b29lhWX1mlBDGWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985ce0bab0.mp4?token=cjjX2ZQFmFKYpeD4b_T2q3W3GzwwSpYG2Hd9hrsjJDFCBrlVu5p0bUP0hnexJQNx6wtR99XDCJQfBBWmFULG_hYSJkoTlsJiBBLHGw1FfGGoWRr3jIYR8WDH7kjeYbf_QR5kCoHS0hYQwekt-F5m7sAMPGhNk8iylOt1paNB76NGXWZVeLSgU_Q6Cyqw7wfQwfo8DxVR1RC4XyrRqd90F0GDRTd-On-UZbs0o7eZqA8PU9j95RU4eRtt8YwnbmytQETFHKfniRAtDd3uZI69CZpjCNeCCpWnbEE5h2m-l8FiFADZVvLhvtIb-AiF5W1br81VLw6b29lhWX1mlBDGWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ رسانه‌های برزیلی: علیرضا فغانی داور استرالیایی علی رغم داشتن کفایت لازم، به به دلیل داشتن ریشه ایرانی از قضاوت در فینال جام جهانی محروم شد. گفته میشه دونالد ترامپ در این موضوع به دلیل درگیری با ایران نقش داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25947" target="_blank">📅 22:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8JML1nCv8VtJOd7MAQ9RmRN9TUATYLQunZGPc-DILeHdAaXGaGGecqwFJh9jcmnqVLCZkOujGK4Jays22jVVNfTb2BAzrf7UBfoLuxPBajr5n8cfi83M96kHgyaCugpZM1OzlAFaZT9BGrCusEcBgc39DhI_UcOPR1XCMgN81GyTo5rTxBsGYmHZdKJkpjlqzM8Htd57wW2gkyj5nnu0fkorKdZcLM5LLBAIb0--f4x5_37nf4mHSVcXMVjycVtLWhn0Xf0tqWp3H7yE699tPoy2BFbnnuMJ9xCF92OzkpIApya1OMT7JojgeFC_tHDvOordEorgo4PARtYGoN4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25946" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2p_nTsn-FkBg1wE1dGxOkG80i44JodiUegbcSUubquRjeD_XdmrsJ-0rhxJfFoD6Ji1i-6lm6EpNUpmWa4Bg9iWBzX54S9YtxHIEnim3isKszE-HpFDPQ00Lhm-8t-yzz9U5LL4IcnkDWQ_cHBILa7H0Xk9wuMguVTiw5umKIFA1J0tzM8FSkxN6ZcQ1E9zehOUeP35YkUh8qqQRfhG7FiSpxzgFDewEme0CSqxGw5hVVQvdW-7nJ88TEwGJZnsREVdaGvEXq9VP0D3QcEzwEtpi6BinyjZM1NhRT0ksBDfXWa7vNyxIWT49A0Kmf803qAQF0ksUfxcjwmle_liXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌جدید پرتغال: من هرگز کریس رونالدو رو ازتیم‌ملی کنار نخواهم گذاشت و تا هر زمانی که خودش بخواهد در این تیم خواهد ماند. قطعا تجربه او در یورو 2028 بکارمون خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25945" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPT6FV5Z4zf6mzSX40tP-wLNgnuX_2aMfac6lKOrXYFpqxjg0awThJm1MwOk-LSi8gFoELVlcMINlzg31c_Pl4tkpfIIxL5kX2yg8JuNtss4ceQyGh5ySM_rdRueZFjFikS3HMnKkC_vOEq8EIomKG7j-JtCdDUomCAeyhNb_VHIjtwelAkxihyvuSYohY0EBIJX6DJv2I_DxEDccP4W_-mjTJCMrJx-dofstdkA2b06u5SR6MDl6-D0wTo5HdMLDqcr1ELH_PJuuYasBnvplJJjmKqIAt69Ujh8fmhkITxOoLMdl80gjTJzB-UwcZFQygd-mEAYnvsvZzWNxWmYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25944" target="_blank">📅 22:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=vUvmk2fbWGOrxyqpsOdNv7afwtRoSf3znGhB0Uuk9d2oYAuIKQxITeANn4600HR9PRMfuID7ZeMxSolY0C7hmfT6OZ9swnw007EqyQTsIXyhYby6YGxNfVa0bCU1mKAdrsXAZoKnW1bSex4VyUrxDQFjdN3S--j3Kz5YLIv-ZeWjO9tw3OODGYgOgk7DeG3b0yqb_6m1NTb1hO0wUxKcQBqR51psBbWPOMrAFzW_IcGPAf7Kly5DAns9RwF8oqUf3t2z_rGE7AHcWZ2aIXIf96BI4bmjdjdde-87c74Aq0wDURLHBoFKbgXCceIQU6CgGkRhrJU6QqsY8y7iencJAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e7669a60.mp4?token=vUvmk2fbWGOrxyqpsOdNv7afwtRoSf3znGhB0Uuk9d2oYAuIKQxITeANn4600HR9PRMfuID7ZeMxSolY0C7hmfT6OZ9swnw007EqyQTsIXyhYby6YGxNfVa0bCU1mKAdrsXAZoKnW1bSex4VyUrxDQFjdN3S--j3Kz5YLIv-ZeWjO9tw3OODGYgOgk7DeG3b0yqb_6m1NTb1hO0wUxKcQBqR51psBbWPOMrAFzW_IcGPAf7Kly5DAns9RwF8oqUf3t2z_rGE7AHcWZ2aIXIf96BI4bmjdjdde-87c74Aq0wDURLHBoFKbgXCceIQU6CgGkRhrJU6QqsY8y7iencJAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لئو مسی وقتی قبل شروع بازی آرژانتین - اسپانیا در فینال جام‌جهانی 2026 لامین یامال رو میبینه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25943" target="_blank">📅 22:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=WQjvm9l4HXpH4TjO75wMDQpWX9ZYVNRsuHPTKTV6LYGXj1oPZX-4hW0q-J5UdgLOaGfsuQSkS71pV94agWozVb4n_wavUc2VITayvpMrVBwcMcdl7SamWxM9B_xEhiIrAqszMWHFXTwUmoSNgJuMIUt3kHgvs-1YA_MRGBuAoP2u0lMLvhVx9FQ7iL6kouSbQrH3IdeT_zBcOL4M7VA0LvEG5z30uiHMoPbBg_cLGP1ZHmKIns9sRN230fzgWDfWpX3Me3HFdOKnt0cpR-ROsADRriJZVHg33khbG1DOggsi4OKQUH0c890II8rdfyeCgA-yf23wBo3D0IIVlJbA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfa86464a.mp4?token=WQjvm9l4HXpH4TjO75wMDQpWX9ZYVNRsuHPTKTV6LYGXj1oPZX-4hW0q-J5UdgLOaGfsuQSkS71pV94agWozVb4n_wavUc2VITayvpMrVBwcMcdl7SamWxM9B_xEhiIrAqszMWHFXTwUmoSNgJuMIUt3kHgvs-1YA_MRGBuAoP2u0lMLvhVx9FQ7iL6kouSbQrH3IdeT_zBcOL4M7VA0LvEG5z30uiHMoPbBg_cLGP1ZHmKIns9sRN230fzgWDfWpX3Me3HFdOKnt0cpR-ROsADRriJZVHg33khbG1DOggsi4OKQUH0c890II8rdfyeCgA-yf23wBo3D0IIVlJbA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره‌جالب‌وشنیدنی خداداد عزیزی و جواد نکونام از اهمیت‌نماز درامارات درویژه برنامه امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25942" target="_blank">📅 21:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxcq23krzaCnDCZ0zPF1lNTj5fipY9D3XH6o-gLnayq3dWwjEZCEAShHrKF_sxB31-XWDbmqWWt2EM9xacoCaUg42WZZE25lyZD9nJpoXHIc27yVzQqMrFmp7oiQcX4oE1uW-IZ_A2DLGmW-pg8xWnjiFEBfcjCeumdW2PTreNZZUgT9Jrb6cKDKRXhavJ0GHToEIxhc-LvgQXk3jW7T568xnNrKF4B94EmJry8gD-gGSkqgrhBhhUmSrgdw7zOIOUc8FeWUY7FBHRJeKLH0h4v3LX8eMIYODZVAfX9Yw01bo9MY-9ncw3F1d3BPKOCzaA0_zwhkeuDKllNvNIdouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛باشگاه‌پرسپولیس خطاب به مشتریان قطری اوستون اورونوف: چهار میلیون دلار بدهید رضایت نامه اوستون اورونوف رو صادر میکنیم.
‼️
این اخرین خبر دقیقی بود که ما درباره فروش احتمالی‌اورونوف‌ازباشگاه‌دریافت کردیم. با این پول به‌احتمال فراوان محمد قربانی جذب…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25941" target="_blank">📅 21:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25940">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=PQdmZYXrf44Du0j6ZOXQX-CvN51BTjh7Tj-mAVGRUDbsqCceRxCODSGtDV5660q2V4KIS7PG3g73cHNZjYCvT7Zijrc3CB4yqd-31M-8nDXHI9bHrMs7fMH3WPS9MwDoAzpSMbTFyPeFCAW_eRsAGXLO7BvI_Rl-67VZbuwiCliXXQ2r5bJKDnV9sui-ACUCx___Nn4LyOT7REXkOc5CnQI9mZ842VEj87cBMGjN26vi6elWDijdyIzVVnnsym_aX10DIrKu23Mgzex3tTDyewpKMpe8OKwI6Zm5EjLWNoNQWvjnEhYAfrMfKsIalU6dL4g2l3qn2_6g9TaBapQ3zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03df1d2600.mp4?token=PQdmZYXrf44Du0j6ZOXQX-CvN51BTjh7Tj-mAVGRUDbsqCceRxCODSGtDV5660q2V4KIS7PG3g73cHNZjYCvT7Zijrc3CB4yqd-31M-8nDXHI9bHrMs7fMH3WPS9MwDoAzpSMbTFyPeFCAW_eRsAGXLO7BvI_Rl-67VZbuwiCliXXQ2r5bJKDnV9sui-ACUCx___Nn4LyOT7REXkOc5CnQI9mZ842VEj87cBMGjN26vi6elWDijdyIzVVnnsym_aX10DIrKu23Mgzex3tTDyewpKMpe8OKwI6Zm5EjLWNoNQWvjnEhYAfrMfKsIalU6dL4g2l3qn2_6g9TaBapQ3zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
علاقه‌ شدید پوریا پورسرخ به رئال مادرید
: رونالدو هرتیمی‌بره دنبالش‌میکنم و کلکسیون پیراهن رئال مادرید رو دارم. عجیب رونالدو رو دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25940" target="_blank">📅 21:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25939">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWq6qpxTBJu_k3SWupUwQBmPylQfjJ1NGoZbsM66y-QlgUbBM1T61kKzS9iLW-VDhZj2AHr6rQWzP3yzOKp2TneOUT9mdZo_FsMJ8RSlwOZmEsOZueKhiMG1zUU-wXkmxeR9xpndbtdvuky-ECKSU6MGrMg3gx9v_KS8aNMrykbGwBZvAzJWtstfbCBNGOf5sb6HVa47tEWkHxxdAmx0Pu18CE8WRuTyyjl-3bASgktoIiLR0pP698VPco4D01YcBgd6EXUaylySezdteCSYiIw1-oW6tJu8jj_iOiC2C1d1Fqz64-buL_rkWwS6NZO8gtt0A5RHht3Z03s_7Wshvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ایکر کاسیاس اسطوره‌فوتبال اسپانیا:
ما اجازه نمی‌دیم آرژانتین‌چهارمین‌ ستاره‌ش‌رو روی پیراهنش بذاره ،اسپانیا ستاره دوم رو روی پیراهنش میذاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25939" target="_blank">📅 21:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25938">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzAYpvArO0yArJE6-Y-_WCvlRedHa4C4uzDPNGnHE3SNsAOuSuHMFpXM6HoP2gjgyYAT-ih1f_CHXrjmxbp9YJ9skE8uNpeNDkoDKyfk71cLq2VbpEnpUlcpEjm3R01RFmIDQExZBG3aurVY3n6MLQG-jd7q8cTwZaGr4wTdvSVXDonIrbGrGKxsv2ZVENpdRsa6F6sbRM4_9-D8YkCg5-3H7d7DAKcePR_Bb0K4XTYMn2aXcgNRUPtb9GFSwmyNwHuYGXAtoKcZALuPV0vjUWLC49kftQRHnBD6BSyJs-lNQP_6KN5C-niezZIkIxgOLHjNhxMRJieSjvgUqkootw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا:
محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25938" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo_ivAuTRVOnS1TDWuDJKjb7p2cGnDf4L6oLRmhwLIMcR4bzbjdvZEUjO1ZA8btHAzGD9GY9sXmCMusXJcAtWWqeUzuZHWUEX9NDyOobKbBpJvD5Hy7lUqKRm4uDWp1zyg_hzOMDs_0RBMMKibuPA3NKuGeBvmLxqPkZ49qD6A5NLHdJHH5usAtc1ObAUM2vlHqpMo7jeVqXSSo9sEnvcKDKLwc1DfotD38g62gjy1aMD0qGkRv3Jz2BpWEjYO_f4rlUJFCvA2Ln1_GAwnRIbaI22UjnZQl7eb7IuwMgiYNlokU4WYKPvmVzw9pFEP0kOLAASsJlZY9Mn3N5jtGAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25936" target="_blank">📅 19:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMXK75zYPkSm1yvgNE_3Mk_79CtASok1z2oN3akobbL8XUHJvorP8OzRGCJVi6ucH4h-QtY0EercmJgp3tRObzmtigyC8-YhYXJ8lfWE6xzbByqKP3bW1YBVv14gyQ9QmoxrHHd881ZJSIZY48OY8rynLW_gHW5x7zvMgJ-bKyEYR-n1RTGDyl7C_scg0qwdoA-TE1m6og40q5o_DNKYZCfCCXzC5vRPWN3F09ahaJCp4DEj_pRV32z0D_xpruVcBA2IvH3Wp_9ZwxVwGDTt7Md1Muy57bjo4S__ivn9-IlBNh9GvxCknuAaL6D8Bh-c22FedzximDTkWNmqZ3OnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسلاوکو وینچیچ همون‌داوریه‌که امسال در بازی رئال - بایرن یه کارت زرد سخت‌ گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25935" target="_blank">📅 19:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT9lMeQ_kTJAOPsHBpMgSWVS2Cw2DSI9jMoKkVc9t7yk-GBd4jQVfLjvI4sHXO6JDZJi3OApvFdSNt04QMnbT8MTSbnx79spaz6zH9U0dEUjhVCvAH_Z_y-kqN3MvKA7i-jvupYZO3gpFGKmZz60OjsUfUuCfzFOb5V_AWZe_fk50iG6cXxw5wIN4GLJjD1KbFOqbxg8ugtjv2th-Q-4KxplKfgKIaCZ_n3QMu49mNojW52_i1jBfh6QKTgmDVRfsQX-80sdX2jzSFWaBf2bYLdBvTVvuhJQD9cPVhot4MVZJRuJ0mL5WUTync_LXibLRBPVtKdOKLWd0jn5wC4Iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
7نفر از11بازیکنی که درفینال‌ جام‌‌جهانی 2022 برای آرژانتین از ابتدا بازی کردند در دیدار نیمه‌نهایی جام جهانی با انگلیس هم در ترکیب حضور داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25934" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuBIrRaOjIOkiGggcR5MXQHZ4zwKESg1nI54-sGH8lGxYEhPFo_B2Ep-Y5qPq_ePX2I8MoymQwt0MYg4yA1mUSufFO-eszvJYdW6kyTjNG2caDy7ZQvLc8--Hen3GAQoeWOG3GspJ8sidv0AELigatCBghaEcr6p_UqjfmJg1YvEvikiip3v9BdpY7c8b68yUKhLCj4rKg5VQcDK5peokUHN1Vdu6Y1QgmMaK0h41WQbeqMUQHjVwnJFmQ2pLhoCPuRSkpin7b6DW43KJJfTQPEfsTso5gmLDqXzhGbnXzaKLpmtETDkz_4BvVIlFU6RL0xHx6Mok4Zwd4TCLIgQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25933" target="_blank">📅 19:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📹
اسحاق نیوتن درسال ۱۶۷۶
: «اگر توانسته‌ام دور ترها را ببینم، به این‌دلیل بوده که بر شانه‌های غول‌ها ایستاده‌ام.» اگر مسی هم دورتر از همه رو دید، یکی ازغول‌هایی که بر شانه‌هایش ایستاد، رونالدینیو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25932" target="_blank">📅 15:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=V0gVHG-q2Q1RelynycHu_JkbSIDYp6K6VnkDfwHYejdin56c-NydFiK1vZnvv0BfsU5OCDFjmvv-0C88IXyAMdNBGgbeR_EMMjnFTqwfhFRDltSJfhDfuMWUv0BEZuMpxCuGYcvV4cvhhwtLLlJGmLZ9VOyW33GLdjrVUZBE7sr8LvY0jIiitigAS1tSZtDnJQ9JeJ-2oTaLy2WVc5_6evnhZGWaNaMACTjkpKuEs8D9fXOPCZOcOkxwmnYV7TigF5oY8x_os5DcaCJC0PqFLO9XOXZzYWdhNJo-cooeWTX4IXKnEAiZ034FP317J2sGydfTNwA5YhnHnxJFZTZwwGPitw8Csj5t5fcZXA60ViEVF_VzuT8zDUUhDPLvwaQWd4swVQ5jbFzfqeXl9icfCZfCnkPiDPcRrLV_e-60urMYikoZabxFzOvbTaTyUiMvJiMDtykUnTOUZvtg9rHsd3f6IF8i5hbh2SiLfbKxI8b1KT28J_F_pJ9yZ24CC9WfmSUE2JxWo8vZExAljs0PCUVdDLIe1y1iESzf49xrhGmL2n2Y3cp2Wr6wcINDngeRTfO9yO3xBfKXlMVcnVDKsQZI0_O_rCR8aTMi6QcanYRgm-Hglsvm6GnaQ6xi6gfnuMywIDr5Pa5CSwXrPp_7RHSHfCHd6fW0rhNu_AYJSeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf1a14d4d.mp4?token=V0gVHG-q2Q1RelynycHu_JkbSIDYp6K6VnkDfwHYejdin56c-NydFiK1vZnvv0BfsU5OCDFjmvv-0C88IXyAMdNBGgbeR_EMMjnFTqwfhFRDltSJfhDfuMWUv0BEZuMpxCuGYcvV4cvhhwtLLlJGmLZ9VOyW33GLdjrVUZBE7sr8LvY0jIiitigAS1tSZtDnJQ9JeJ-2oTaLy2WVc5_6evnhZGWaNaMACTjkpKuEs8D9fXOPCZOcOkxwmnYV7TigF5oY8x_os5DcaCJC0PqFLO9XOXZzYWdhNJo-cooeWTX4IXKnEAiZ034FP317J2sGydfTNwA5YhnHnxJFZTZwwGPitw8Csj5t5fcZXA60ViEVF_VzuT8zDUUhDPLvwaQWd4swVQ5jbFzfqeXl9icfCZfCnkPiDPcRrLV_e-60urMYikoZabxFzOvbTaTyUiMvJiMDtykUnTOUZvtg9rHsd3f6IF8i5hbh2SiLfbKxI8b1KT28J_F_pJ9yZ24CC9WfmSUE2JxWo8vZExAljs0PCUVdDLIe1y1iESzf49xrhGmL2n2Y3cp2Wr6wcINDngeRTfO9yO3xBfKXlMVcnVDKsQZI0_O_rCR8aTMi6QcanYRgm-Hglsvm6GnaQ6xi6gfnuMywIDr5Pa5CSwXrPp_7RHSHfCHd6fW0rhNu_AYJSeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25931" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2McktNWjVNZ_cDX4dlkFe3u76dPh5E2JhqMfhVcvcW35w3eLr8RgnOV6mscgFGF0WvsMvAg9SIl7e5bUnj4xAA15EUTDlVs4JymTf2Gn8lYgn4WsM6TfpsKM0OBqx-KsXXqRC-uNxP1pM184tiXcnNKL-eiFrE1S70kSY0R9T7DO4F18sKi2STnJgdFRkDGB4KddObdc-_tSy7WLdIDjdIW24iy7rUVlKe4U84_6yXAyX0i0GlCJQqpEevQY3NObC6u7JQMyjump4rP9oStVPGtSqKCuGn24BuF_Wxwo3_7LTwd1kL6mWHMx_Fp0-zRejC29sm8croRM-NX9eTzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25930" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaiD7EWtHLBEzFFIWh6R2tpXMVpc0rIeEij20Y6R_v3Em9FQs8S9Wz7EKNWv_dYCYXamMPrSvhvT-oTPEqGW9h4tFlRgm8Wla4lkVjH8LJ1tx0mJ_TSQVzQUcbZLF97YzRO65J14PlQGvsxcQViYVpGtRsIXybKyqS2SYqdPdLgWiHsoH46kRHW9b_CGzCCHF7uqR-nYSLShIHFkDyCc2x0TLZMisrp8Ei0Lki214IMeaTQxfO8qu46PmwbcvAMnmlfaZ3ButFaMEG-T5s9O0k88JC42HFYeVyXB6jQBYMORshYIk8S8ihVkoxdvuGujZ0QpDTNMfTElIou71FZeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
نشریه‌اسپورت: بعد از جام جهانی؛ بارسلونا مبلغی بین 120تا150 میلیون‌یورو به سران اتلتیکو مادرید پرداخت میکنه و آلوارز بعد از کش و قوس‌ های فراوان به جمع شاگردان فلیک اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25929" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAgNZ6g_3Ls9O3wwHn0VuTL5rXj_DeJ8oTJZPPvzyazWq9d9TxNXel3gxv1aMoAytIgQCIC_GK4Ldz1oCRX-PcbYaSmiyVdsoSgS_rp0ZeW6AnjcgqmWmLlJY067TFdIbCpZoCrqB-6UDF_ALNsps30ovvVnWkvcwnmnMnTJ93uG6w71mBVBK7-atikI6Y-j2TUe8HsdmZLyI18VC7pA0gnLBjyERDLVVIdAuiwRheeMCFbSjA5BJeg8GDord3p0UlhJfDEUdvEzh3MoQg1fP0NfFFPldCc9aBtR7x5QrBNS1cHGEGYOv216pR3cccgCmIqiV_dQAqJFWjCmHs41mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25928" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk9WRI_CRu_UcNVR8KF9a5xZIoTruZzzc6V7J42odg9gM5yjOacQzCPzVZB6-EKEvvxkSCHTltOJCU-2Hg2UFe_x0b_OiKOWhL0xF-xBb9x1xR1UFoODQ9Oo9_k0aiyUOEDQ2ohaFax4ttVzj_0o1XMRazp7A9QkUgIiNSubnjZfpePxKfyzdVZU6XfMJO9hWx3rqhzQZu7kHnb9-yIKtR9y8_lZgYpkP7I42jgc3-L1I-qufdFjDAgfSwwmHxWltpdOBwWfH8Kdt79vqmSpKEmP-AcI87HzdfnC39RJr7l45T6KzET9KUnY2sbxABzbJegH0_83Ha1bbGW1rkDUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💰
ثروتمندترین کشورهای جهان درسال ۲۰۲۶
؛ این‌گزارش‌بابررسی بیش‌از ۵۰ کشور، میزان رفاه کلی را بر اساس معیارهایی مانند قدرت اقتصادی، برابری درآمدی و کیفیت زندگی ارزیابی کرده. منبع: فهرست ثروتمندترین کشورای‌جهان شاخص‌رفاه HelloSafe
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25927" target="_blank">📅 13:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF2w0W-RR1I8YbK_lFvBGBjwYGs0XSDO7aXo8r37EN9uIJBVmyfvd_jB9c0DKRhMEcgcOGcKXwlHoRlRXm39lyr-uGcGZ32B_mk2BSOv9ajhLauPmBgFgOQE5AzS-hxvpIspylhtfCM-2WISSJLG1dQwFEJNjuRqwDJAbCY5VsIT0gtSDWVEl5n7EiFMjd3l54oh0noGINgZemNsgkgl5-7THYrZGzBhU7zqmJIx41NKClUF5yL9D3tdlNe3JZkN3qCW3hwHbi9unJFmq3l79KEpXBX43sW9d6LVVklp-KdNBK9RrNMAZgyHv4Gz-UOIDYjHd_PbfxrUpiGL98j5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
شرط اصلی ورود به تیم ملی اسپانیا: عکس یادگاری با لیونل مسی تو بچگی؛ لئو مسی هرکیو تو بچگی مالیده الان اومدن قهرمانی رو ازش بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25926" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXc-yyQZUSNaIX7ywgFshZdz4-PR1YieyfwfhLlGsMDHtPzieIPaTQpn8JJ8liLlGcZcKlL6Q9X6or_XzkFHjiJEG8pfYTcIKft67qbu5RAUPuPtX5WDPFHMfrrMvlkL-ShJol0TB-v0bYkol1t4JZzoC8FH2MdLA_-CaHLfSSlEPFZEODURJkfIDcL-Rlx0jnXjoYMqufqem4xbVcYlvLGJnN8t2zFNWvO9fej_k2VQ9bYldgzYRIDCAr1wEFByq3LaCC8HCC8Pzur5kqOReHaJWAno264QuNjJdMy_EIoTwX4yLoNXWKz5w1IHA7nn-MAAOlRggZvrVqpJDgB1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
تیم‌ملی‌والیبال نشسته ایران با شکست سه بر یک بوسنی، برای نهمین بار با افتخار قهرمان جهان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25925" target="_blank">📅 13:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Asj4SkzrsP6Vx15fCOixWuYkmcRu44eo0N5AaYlXqh6IaJJtiDNRfNkCgwSLPzJ0COR4cCRKp-YN22v8u3Lm2EJs6XabeSL3CbtH8-MLUKCRZ1fgQ9KYo8XFxI1Bn23Qzlp75PL0ewcPyZZZRsSGdKn0T8CR4OpQuoF2kZSSXbQxZypUdkcMIgmlXTXMRHvZfnfGOuDQO2X451Rbejvo97NGhCHQG5-ivQCgeeMFPXdjafl5ZpV9a0f_VBphslxprm18aQ_rHrg2xaNS7imJpuuczwoJmaFPe2A9o-mKKN3qM_0GZXqTzyPx2-CbWEqOnl2FNVcEt4ruxDzpopVZtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇮🇷
#فوری؛جواد خیابانی: از نزدیکان رامین رضاییان شنیدم که این‌بازیکن باباشگاه لگانس اسپانیا به‌توافق نهایی رسیده و فصل آینده به لالیگا میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25924" target="_blank">📅 12:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=JlGT4AtJvOL5aEatRSnxO2sE-BKxrUPO4M5d67-ORLdTtBK7MWMN2MKvtfdxcAMFf5OHdEbyu6OU70UCaHvxgW2vTGMukf-M6WUu8pKkaA12DMQmvWd6r_T59xkfOfewOKRPrz2bmoC_DQiqkkYtm00fGsoYpKA0W3-5utikp3z_fO7FC5SBURdNR52vY3HFGmeK881jb5CcoLA9fs_KCsuSQcfGY58pX_DW-TUd9QA1QbCS-3AAwMg4eDkbPqhgDJNccfQAXyH-9ox-mLO8TD8nZ053N7Tod8pbGbSoOJ8kAZ_LOqNj3F5VhRvRDxNxQg1vh8R8fya3ha9g7tKg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02ccca30b.mp4?token=JlGT4AtJvOL5aEatRSnxO2sE-BKxrUPO4M5d67-ORLdTtBK7MWMN2MKvtfdxcAMFf5OHdEbyu6OU70UCaHvxgW2vTGMukf-M6WUu8pKkaA12DMQmvWd6r_T59xkfOfewOKRPrz2bmoC_DQiqkkYtm00fGsoYpKA0W3-5utikp3z_fO7FC5SBURdNR52vY3HFGmeK881jb5CcoLA9fs_KCsuSQcfGY58pX_DW-TUd9QA1QbCS-3AAwMg4eDkbPqhgDJNccfQAXyH-9ox-mLO8TD8nZ053N7Tod8pbGbSoOJ8kAZ_LOqNj3F5VhRvRDxNxQg1vh8R8fya3ha9g7tKg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آداب صحیح نشستن از زبان پدر تشریفات ایران درگفتگو اخیرش‌ باابوطالب‌حسینی؛ چجوری بشینیم روی صندلی که به کسی بی احترامی نشود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25923" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ-wlLuL4AQhC_-MwjvgePl7ObYk-kA6cLMVgOEJuxsS9N3aQi9pqzMOaRnwn8LrBFeAOXRCUOIxlHQ6vNrKbGrXW5Tz_zZhiJbeqwX6Jc2ShboUwUz6cDo_fkQUky5Ap4leyERsdw-gRmKBdxnAYwn7l0LJaEhSwcX6zDfUip_zTwXP8yY6tPN8cBtk3sLf0EkbN-9AfZWFP4i8l2qiK0aLDCdq5MmgKyNZO7VVFCS2ZZvPuwm1kjH7BJivjyHwEZ2K3MaD3cQuclQ-NnRKKAkmF_WJTSgIVyTFlqWy7K-2Om0FdL4W4CTmZv453KOOByp5FeLEkP8KFb2p9wgQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25922" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879626611d.mp4?token=eOj0rU0FPXXVISwycPzbgjw0Zw-jtHyjl_6Lag_vB3U5wZ86ePK3lrKWEHXf_X9QbHbG7kqVgNByyG8wGbXQSfxN36LmaToSGey9bh6jX2hm_ej1pfwst_gZTsd1n0e913cnd-QabrpP1mGG87nc0oPdn616EDkQK_JR8H5vl_KnZx4Ay57lWvbmfNOaa9IUtEojI4WvEyzlGuKHRE7ApORF2RMVtSq2EOfW3-uubYKsYxzuw6wLRdMfQ9PLyxhEN8uuoTegOzoWRj1VSQFuT4Ta39P2eVssRxF-W4k2XQ3bi58PrQYNR2AIk87BFtO0nfdurBloAfwu7Q8XeYrkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879626611d.mp4?token=eOj0rU0FPXXVISwycPzbgjw0Zw-jtHyjl_6Lag_vB3U5wZ86ePK3lrKWEHXf_X9QbHbG7kqVgNByyG8wGbXQSfxN36LmaToSGey9bh6jX2hm_ej1pfwst_gZTsd1n0e913cnd-QabrpP1mGG87nc0oPdn616EDkQK_JR8H5vl_KnZx4Ay57lWvbmfNOaa9IUtEojI4WvEyzlGuKHRE7ApORF2RMVtSq2EOfW3-uubYKsYxzuw6wLRdMfQ9PLyxhEN8uuoTegOzoWRj1VSQFuT4Ta39P2eVssRxF-W4k2XQ3bi58PrQYNR2AIk87BFtO0nfdurBloAfwu7Q8XeYrkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدئویی‌از پدر ایرانی‌ که داره برای پسر نابیناش بازی آرژانتین و انگلیس رو روی تخته تصویر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25921" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdQkhw4HX5VmsKx6gTE8psY965sEKpDJJGJ5cIRRwK13jNhedF3qn6Oo-VRlWg0BVaLdCae4SmQU2IfjBBiJbD78E7z1cWHc8JnfP4wcorCsKc1GbX4hlr9KEjvsp_0RhJepUmwO3_YvAUSdGwroCxtShN6IbySFnep5VGAu768H3abnJF0CAEYpDRYEbfNC_6s_RRCI-zuOQeoLMf2vpam6ldZM9hq7WeiwhDusfnBjhEegAtgUaN3ajC11uTPWOB2aHQnbWoOFm0_TRe6PpKEZYYsHnANRP9fwOU6PQRYC7uqzwnkGRwnuswSey8w_njb48hY2csxIHqW-IKtaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25920" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
جلسه اول برنامه تمرینی حرفه ای در خانه برای ساختن یک‌بدن‌خوب؛ این تمرینات برای دوستانیه که بنا به هر دلایل دسترسی به باشگاه ندارند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25919" target="_blank">📅 11:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX1W7OBpKe7ZbARjkoFfFgbotWrZn1f130NI8j85O9c4aquSAlUSEldHZOdyvvH4pBUR5YWY6XIy4h2-Jk_ovGUXTlutFuAg0BZpG7xxuDJ0H7s8Vtu288wZOyTWbHp3fzrGbSLMWPcGctTcFpYjpeR5rQ9qCFRC2LGvgN052LqZY4_4SWhBRpZlVVY84aC3Y4MckqybbJH3wjEgtGka4Rg1_w9xW2ck1NuOoQ5hjlGRuH73baPvgyb5jcPHuozVcJEzaa1izVqJy0K3V_aA-MMl4jiWXXIWDe1eyTroyFIG7k7XPC_DeXWwYtUzItjHpLeFPWflPVTKil5CS4JBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در۲۴ساعت‌اخیرسرچِ‌جمله «لغو عضویتِ جانفدا» بیش از ۵۰۰۰ درصدافزایش‌داشته‌و به سرچ اول گوگل تبدیل شده! چی شد اوزگل؟ ترسیدی خجسته؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25918" target="_blank">📅 11:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYkf5zU65tBDK1FrpzuXeVjQII5Bl8oDJqfLXKvpcc2T5pA2ezMVYITNJuyItlgFr_RgZ08OeBLnhqkT9QSx1ynLmrHcggtj6OBKTUqjaEI8wVEh-EYVfNaeyGgTmN2MkIcr3_x03nKtsY4OwoQHGezoeYsm5MAVjG8d_8i1AMxqFRIDtQptN1OaUMeLUGA1wCcy7yoCDP9-GHbHMONJU51k_HpLqjKB9zifJjguviWvM5v1ilU_GjaAD8Grbmeq88uxxQMhZlLrVvkGQDmzWoQQmfeoJxKypRZlmJbHDPCU4w5vys67qAJPg4IXKNP2m6zp0FQ5RJJLVi3FnH7sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25917" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enFt8jQyYTpgORwrFIoXPrd8VU-3cXuzNtWJmlAm1jsWV389I_twPmSTMXta8hkenqlMSaqFY7tsJdxYYB1PBVD2ITDzg5SzrfMVnpqhXXwoq8BzwI1dZGlApjf1ng-61rfcbHGsZwchdhKItFO7yIddiLIybG9XjKcKqkRfyYhjsIoJWXq-V5CU1ahRT-j55x662dt_G_Ib6hpNSJcmuOJEqPg_AX5uQlX9B9U5byj5isD7Wqr-Yh4-u5BzjaKN4G0JVXbP5RIuq6Qlwpfzz9GLLYOQC52scnWb5Vg79tJn0AazfWYJARmiUUJHAd_9f_3lVrvyuc4ukLYxTUy2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
عملکرد خیره‌کننده لیونل مسی 39 ساله در هفت مسابقه‌جام‌جهانی2026؛ بجز یه بازی که نمره 7.7 گرفت بقیه بازی‌ها نمرشم بالای 8.0 بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25916" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtartDAE2RenrjNzlpm1RdxGrxXYTXm-PzWAw-ZB6-Lr40UBh9V3tT_Vy4vFUKMxr0zFmPz-nkwdDZVFo0BqEdALk__h3SxxY6fiTLI9EB910HfFFBHxVCkTLM6PKPd17w9CUV9KwncItyKhVxw7TUbpZ3JLYOp5bmqP1Z0kDjnNswjfWtKdQ1SE1DxlOj9x8Ymt9iGRLJBbL58yzD6j8zvs0dM3CDa9papEH1ZecKrNvxNnmO_pvyg8KaM2P-C6SiE_j9GqxQQR_NaTa_NYzyT2Zd4s7zKFDVB_Q2per6hvGsZkXZQHcRaaSrlMkpMYSATyPdmCWQ65P6mSC-uc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25915" target="_blank">📅 10:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25924a633.mp4?token=fpRfryiapVJVQF-fgItlpPrcE1HQkLsGjoMYKF-APahBEQP_wz69wfLRogym0PrTYglKIqtrjrUd8XENx66TgSQe2ldZgPDDscJHtyi7lYdfLODhL8ZWy63IvmrdqfkWKpQQzGqBHQz_NZJP4EieYSVfKOEV3LJ4-uJd0sC9v6L0zd2QLYmCjLyyYU_rmWjPTgjv3esSub8Nk-zjag6Fw4S-1JiG8OE161Y20r_sq0iU3TLF7pSsgAc_u61-mZ6zrXYvufWY1FP_pz0xF7P4HsIVsaf0HgfoHUyLq-f5YMPSy9sZTe6uR9cROev54Gqwcy3AJyd1Yka3SK_hfdtMqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25924a633.mp4?token=fpRfryiapVJVQF-fgItlpPrcE1HQkLsGjoMYKF-APahBEQP_wz69wfLRogym0PrTYglKIqtrjrUd8XENx66TgSQe2ldZgPDDscJHtyi7lYdfLODhL8ZWy63IvmrdqfkWKpQQzGqBHQz_NZJP4EieYSVfKOEV3LJ4-uJd0sC9v6L0zd2QLYmCjLyyYU_rmWjPTgjv3esSub8Nk-zjag6Fw4S-1JiG8OE161Y20r_sq0iU3TLF7pSsgAc_u61-mZ6zrXYvufWY1FP_pz0xF7P4HsIVsaf0HgfoHUyLq-f5YMPSy9sZTe6uR9cROev54Gqwcy3AJyd1Yka3SK_hfdtMqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضا بیرانوند خودش‌دست‌به‌کار شد و به این شکل مجسمه ژنرال رو در تهران پایه گذاری کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25914" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L6qvS8nS7_AdfVs_wZ88Yj7q3zWIOyqqSjG3Llq_vcAlA1c5MSj8YKT4GvL01SG4bFeHCSXoQwikfIxoE5Kwk4lPAn761zwIwz2L_rKFd4g_7mbgpGdY0vaEkWgyQS1g6-KhOjO83R04fO9JzDargqtq_-XNHddOj-uqj1e5WPQUgwfCgLRKTxeI1WnOYDy7cUjkKPFvA9TheRsvKslqoP9tMzvNjwTwzr5vxZ8x0mm320CvgSsV5QxpfdjaXii7GyR6kuD_dUl6sT-fdt1TR7xowMXMe_yFD5M0X8_WVJxQlaYxK-mDDwEDfUwmCf03s1QzlNcf1wwdaYoV9BsDpZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2acb1ca35.mp4?token=rPyP6vVenDLlfbkzbKkQytSsZTVhv98nzxOyctHGzySEMGbquIFCXNSq-I_h3efZa_aLrDQwU8KG0r-WpbC1rDEPgCzeeksxLJMTbNJHpWIVMIV4kaQHPkdebAWoPossyNma6tcerINeSz_KoSblv1NSJ-7v5V1Tk_8HkH4PkPER7xGKCzNZ-0nwXUo-E4KrLMy13tLCCLu1O29PPsAxbGzkE6AEmLesbUcrU1Z294ZWunCJSpJfb84RpPi3b8FhbAiyWgIDzGtkfuCroQ9LPbY1k6x-dtaLFCVQGiZd6WLXuG6vs1Mr3DiiW33Y61_OSxB_4bY9F-OG2pgbn7S2L6qvS8nS7_AdfVs_wZ88Yj7q3zWIOyqqSjG3Llq_vcAlA1c5MSj8YKT4GvL01SG4bFeHCSXoQwikfIxoE5Kwk4lPAn761zwIwz2L_rKFd4g_7mbgpGdY0vaEkWgyQS1g6-KhOjO83R04fO9JzDargqtq_-XNHddOj-uqj1e5WPQUgwfCgLRKTxeI1WnOYDy7cUjkKPFvA9TheRsvKslqoP9tMzvNjwTwzr5vxZ8x0mm320CvgSsV5QxpfdjaXii7GyR6kuD_dUl6sT-fdt1TR7xowMXMe_yFD5M0X8_WVJxQlaYxK-mDDwEDfUwmCf03s1QzlNcf1wwdaYoV9BsDpZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تعداد گل و پاس گل‌های کریس رونالدو، لیونل مسی و نیمار جونیور در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25913" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9fiT1SXR96MWeEaDAseovhCvtthPkCXJFPqqheqp6oTj19GLcf-KPKlzM6mM0a72MMd6asQS2bncuce8Q3TQIrI6m-HKW25HH2aohwUlDJBxGPFaivbh7-S3MZ8fzVIvyFr8ugwjuTQEh8lJEvOu6UfHCF1ZrVudQmHpNgWCdOCeFZFBrn3k_jW5CdyfrqZdKrE1XwwtPajtfqtrgZgkXneSMWQbceZPK2-ySwh5mel528NaQ_1RtnpOFQBhyC_Qww7BfUJbs1pDUqSTee9FyyK6fye2CeIoooVGsIOQVmzMhh-LCJvmrT3KEajeo0tRzk-hvSqHEemQ83hfal08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25911" target="_blank">📅 10:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=aFr0ef59sF1hPHrOEvY3mucGd48mxGCdRtyvtX7kx0W_HYz4sLJj-O6SuV8mB-BzE8IqYnclL09_OGjFwYbYhEwRT1zT6vb3UBfPXZ8f_YwqyKHd0epMZUm-LKUl-eOD5oBcB7lNs2QFW2TWyCphJlawsyx3kps-AMFoLAW0J7KCFnrgV-wV1knWl5sj8BRcBNHZ1enAZOlt3Vrcqy2YHoTc5DnrljBNRYmX_V4SuRDtZQnWuwo1mSu0B_JF9GtZaPGN-TL7waG6054PNjWZWFlcKKTTUbTccgqdNiMaNhVedMTc4Xzbrt3A27DmbfTstkiEFc1hCewFMD178LyyTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace8e97f1d.mp4?token=aFr0ef59sF1hPHrOEvY3mucGd48mxGCdRtyvtX7kx0W_HYz4sLJj-O6SuV8mB-BzE8IqYnclL09_OGjFwYbYhEwRT1zT6vb3UBfPXZ8f_YwqyKHd0epMZUm-LKUl-eOD5oBcB7lNs2QFW2TWyCphJlawsyx3kps-AMFoLAW0J7KCFnrgV-wV1knWl5sj8BRcBNHZ1enAZOlt3Vrcqy2YHoTc5DnrljBNRYmX_V4SuRDtZQnWuwo1mSu0B_JF9GtZaPGN-TL7waG6054PNjWZWFlcKKTTUbTccgqdNiMaNhVedMTc4Xzbrt3A27DmbfTstkiEFc1hCewFMD178LyyTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجریه به عمو رشید میگه از فوتبالیست میبودی و‌گل میزدی شادی‌بعدگلت به چه صورت بود؟ ببینید چه حرکتی زد. جمعش‌کردگفت منظورم قلب بوده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25910" target="_blank">📅 10:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=XxVCdKfpDvSUacErDmeHKTlre0rm3HzlStRP4-SsoLFv8DZCmBGDY5vdu82i1gnHLAsuNYhGa2ISnDeGza9F3ghDkQLNSBl1PJBfg0WK0FiuSstcVNaMctGzlwjtcSQbumNT0R7TAJQd1dzK9qzduiQOJMUtzVVj2snZGSvaJZW1OeDhpbdJDes9OieVZXWeCKR1lkvtyIAWRoIulFA3jfLXY7cEWe-3GBZNnkFzqbmQBggJsvUMzd4IeNxZFhp_x4x7Xt2BG3SGXTL6VtlNEc6cJVvIj_l95tgdBui6dorsU-1GUc6KnNUa5l8JE90bYom-cI_0wQZN5LotKa6tFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2009a903c1.mp4?token=XxVCdKfpDvSUacErDmeHKTlre0rm3HzlStRP4-SsoLFv8DZCmBGDY5vdu82i1gnHLAsuNYhGa2ISnDeGza9F3ghDkQLNSBl1PJBfg0WK0FiuSstcVNaMctGzlwjtcSQbumNT0R7TAJQd1dzK9qzduiQOJMUtzVVj2snZGSvaJZW1OeDhpbdJDes9OieVZXWeCKR1lkvtyIAWRoIulFA3jfLXY7cEWe-3GBZNnkFzqbmQBggJsvUMzd4IeNxZFhp_x4x7Xt2BG3SGXTL6VtlNEc6cJVvIj_l95tgdBui6dorsU-1GUc6KnNUa5l8JE90bYom-cI_0wQZN5LotKa6tFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25909" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=UWIR1uPQ3TFXbbmaka7IYOU6aTUWf6ffkKp4n1k7b736eEEoYwoNxRbs3MVIyXE_ZjLOXtrL22UPRsV2BZTzXOtbCB0aR1ZcpK_q42AJpR4N1MIosGZfL1Dhgsl-NnRGabFFOV9shHen6MY65ba8FpNskDLZylGJ2PWHK-3N2HMmxTHFYNkE6SLgWK4e9-cLLeVGzJE8V3pMkyRUgavGPjRcRCei8XEzKv_LX5zfR-30DWBebNuRbHTZvBBKAeqaRu9d-Fa-k8BWODPJubflS14Z9e1wtrqTLNbDBAuKkMHKwsKkR72ql3EwJ1MUrtlQm9xzUmhC9623LM30Q657L66TxhICR4bM8N_RWiwsvUvon-Nsqs5eAfZAkBUbEhmHby-8i7rUD2EtELaLnpVQvLoiy9wYt8KAU1vOWkNTyUzx6_d0ztUqR3XsjT0utRV1SBUCcKbCZWmkwEKKAQYA9ajeoMLSc8LOkjZZ7OkWxOe5DNCvLAxaiPmtHeomysHIDnPucCva8tnGAhAktipL3GGmqp7UW04OpkDq_KxZVZzc5pwzD6FT7MPR1Mg0j5UmGEyH6nZ7TRs3ewKGKNk2Zy-gPyXwquAmFdCnhj2m-L5tde8A84KPyUo683HTsewSiAtLNgdHuUoka0CGk_vKZiR0GTLiJVOD9RRvZWahAjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=UWIR1uPQ3TFXbbmaka7IYOU6aTUWf6ffkKp4n1k7b736eEEoYwoNxRbs3MVIyXE_ZjLOXtrL22UPRsV2BZTzXOtbCB0aR1ZcpK_q42AJpR4N1MIosGZfL1Dhgsl-NnRGabFFOV9shHen6MY65ba8FpNskDLZylGJ2PWHK-3N2HMmxTHFYNkE6SLgWK4e9-cLLeVGzJE8V3pMkyRUgavGPjRcRCei8XEzKv_LX5zfR-30DWBebNuRbHTZvBBKAeqaRu9d-Fa-k8BWODPJubflS14Z9e1wtrqTLNbDBAuKkMHKwsKkR72ql3EwJ1MUrtlQm9xzUmhC9623LM30Q657L66TxhICR4bM8N_RWiwsvUvon-Nsqs5eAfZAkBUbEhmHby-8i7rUD2EtELaLnpVQvLoiy9wYt8KAU1vOWkNTyUzx6_d0ztUqR3XsjT0utRV1SBUCcKbCZWmkwEKKAQYA9ajeoMLSc8LOkjZZ7OkWxOe5DNCvLAxaiPmtHeomysHIDnPucCva8tnGAhAktipL3GGmqp7UW04OpkDq_KxZVZzc5pwzD6FT7MPR1Mg0j5UmGEyH6nZ7TRs3ewKGKNk2Zy-gPyXwquAmFdCnhj2m-L5tde8A84KPyUo683HTsewSiAtLNgdHuUoka0CGk_vKZiR0GTLiJVOD9RRvZWahAjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGnKBRhMvA2Ry911qda7614npzMYNAztyqff_NHPel44GnCwNEvF7Wv8gRwmpoBADKVEiB0YxXkIeFakHvGtLJdDFm6dFobB4XMRWSt0kFmxvUZlIhRUnFhVpBCqtL9D6T9925NxwB4ibEeoN2QtEnpMyYULhevgWrVg5Km6yiNYtL4cPzDAb6u2ZPRGG9APi2zyZj_2i9vIVV0qV8XjQDRuxmPWMQLMjgw0cjAsXLPeQg9-o-mE0A3IHV66nhWO7VAlEzqWEMsiWiZd_zgcAHjLrs216BMdTEWnpmsumTMFSRyapwgQ0fRq9-MDuzSnJFwNf5hpsfnVYgejkUy_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=oojryuOLG8psa5-BbfaWIfE1M9hzsc1u66cnz0iCIrHnPgDm3xRbXw8mKsB8sHzk2krBWIrX5KC8ITPAZA_G7xAHe8x9o2-7yy7bZtfI1mJHaWi8Yu2KAF-1bcxFDadsjevSmVyKJyH1QXJE0NyAr4dJcxjgmGN0Vn4ZAtTUrvKapnpCW-TMsWl-ayg8aHNLk-HJpJhejM6s-EjLjFtb89zKn1iXmnwRSx0F2mu5fH00sX-npFP0jP1m_mPicx_Mi_CP80Mq74YX5Wrsxnr_NGaZ46maa55uUKnx3np57nTcfcgYjWrhwhgcEWnHELL25-VUf1aRM2DROCfaFrgoUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=oojryuOLG8psa5-BbfaWIfE1M9hzsc1u66cnz0iCIrHnPgDm3xRbXw8mKsB8sHzk2krBWIrX5KC8ITPAZA_G7xAHe8x9o2-7yy7bZtfI1mJHaWi8Yu2KAF-1bcxFDadsjevSmVyKJyH1QXJE0NyAr4dJcxjgmGN0Vn4ZAtTUrvKapnpCW-TMsWl-ayg8aHNLk-HJpJhejM6s-EjLjFtb89zKn1iXmnwRSx0F2mu5fH00sX-npFP0jP1m_mPicx_Mi_CP80Mq74YX5Wrsxnr_NGaZ46maa55uUKnx3np57nTcfcgYjWrhwhgcEWnHELL25-VUf1aRM2DROCfaFrgoUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=laeILhf3B8FIfAhfXQY7yvIOzjuimKiYwcneMWo7Mw-kyH07DDh7d3fuJacRNxmROsoJA2scrMZ30EPAT8MfGO1RwZLKZ-pYWub43nnxY4hzZ2uNFnX5B-8fnwV_dbk_-IWrN6PKh-9SEXDhRbH3epHT1qcKTVNeDoxlobaJ55Nst4upWbXMiwaHSlMPMRruHsKTq3G_u0RD31d9KdKX7tF9INJIvQo-ce_R4Q0uquIKfJgs7inM8aNAyL3M1uH_9nZNOKLXJu1f37kbRtSfWElxhX-c-GW98AbQtS46fbIF7_uFYlMBfQbqqnrPqUE1uohbbXeqLM29LZ_8RpBQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=laeILhf3B8FIfAhfXQY7yvIOzjuimKiYwcneMWo7Mw-kyH07DDh7d3fuJacRNxmROsoJA2scrMZ30EPAT8MfGO1RwZLKZ-pYWub43nnxY4hzZ2uNFnX5B-8fnwV_dbk_-IWrN6PKh-9SEXDhRbH3epHT1qcKTVNeDoxlobaJ55Nst4upWbXMiwaHSlMPMRruHsKTq3G_u0RD31d9KdKX7tF9INJIvQo-ce_R4Q0uquIKfJgs7inM8aNAyL3M1uH_9nZNOKLXJu1f37kbRtSfWElxhX-c-GW98AbQtS46fbIF7_uFYlMBfQbqqnrPqUE1uohbbXeqLM29LZ_8RpBQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NiXqFIVbsEEE2_-BPoDvXauuWP6PufSYt_Q-BqFm80bZs2MHVhR-LNigowfygx_XkI67waG5zFUwS0-GeimK60Ck9zTSHozbo16NlTx6AxtVtFDnck_dcij-oZCM6N8Xt7gwYmllFhwSE1nruwr_Ebm2JPMeuo600VMO2Kl-RmZk7NpOpmJ1lErS8Ua2GxXglD-wvdC7V5E06a8GoWOxmzKjKIuFpDoVk_nTy8WRfN0HMPWyVAh3qy1pnarx_HVjWSMTfijxS9IBAso_3sIVPDbtmoPFIzOX-LVXWE2L09N_u0IPGQTmh_tON5b0LV_Qp4odZKE4Ait29Lrav3JAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lap4yVXAqis2ywT0DkeT7NySN7WN82h4SPTxwPdqhIAue_WxivjwzP19yFLjKZTtc3rglsnr8QJaZD3IyDzBCI6pBrlfW-VmJphQwFZxRReG2cHLFwhIbDo1KHfOzR27WcVfTKRK78ld67DkghPw-XK8m1GFUTuhx9-lNc-OHmvGW7wduxHuY-0XP6kugUt9oW-Ns_lXfXN9fYBKh4AsLxvGsP873N93HJIoN4DXI1uSI_x-S5JgpiUSdwWjJfGJJAJnoWW44KW7oMIdBEWtiIKHgqhFSqmoPLcJQLncKBF2pZYqd_NMJeWGhkj3GRcQ80EbaSlUU_hJ7L-Dy5_Lfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb25TOrrk4CRWMBgFu9HSa8IcYYHPwS8pBEiuRbqCBfWfCR5wm_50G-xaWf0fF9_hCwAb5Gz3yfV_bDwkcyo6jNebLSUFgo9EaQbG4Bz6D3Matp-IM4Qzqv708bOS8Vh5htQO6dikedCiOsCXCiqKFJU2kvesfzlOck-wlQsbyOZjt-geLgyVinPuB3Qie7nBSvJp54nmIoxu7vRcd9N2YAnCFibaWqVpodvU-Hq2NjUfg3pTO5qLkqy0Yl8QNiLlW1vZauqu-sdxUOCXmvD9OIpcE7IWfa-lFSzdfqdHnurBb37uOMtZ3cOaWJKqwhM3KnWpLoc6VRiDrwSCKvuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwryClEc3qzKgf_5aD276vLyUiqmDq1BkY_p2rHpA1-HrvbVAy2KLpH2OK6n_egw2nYa5ioIfWlEyX2-NuSFjiU8aM3ARqowZ1wHEggGaijAf-3U-dV-XfXOVDD74xc5XLfP0osLKzjmJejLjvSmQ13yaM0uhwghJz4Vs7_JeN6JAB8-7KH69Eyu9s7AvDIyfQ5LgPjR2rXFBM5r5cXO49m891qKMLqN6cNjhZCqQJqOlFmIgFfH6QYzU4Y5mJb9P6R0sxExnv7peAaR0emaWLBGQ13eAa2jUHzEwAYGOL17mI6pyIpy9K4rn4WB2qSU9nxpOubRLQyh_yOsqr5HbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_TXkji7H4ZJTatVAT7ovKSBW8dc8U5r3Oj2Gwli4KhuM4zKYHbC_iX11N2Y2xyYr1t5DAmyEejl2YnSByuZd1UgPudyYf-4vkPlGXtLVoNGJJReNOTZhjgUtlANGCFU41qau_FK73zfLeVc3DxVBA-Wq3VpLsERgHvevx2Sdb2fJLjb9mR7eUKI6Lujs89W72EjSbTX4dgCRYXnfTYDZyPiQh0R-uE6uWo3Y8cyRIoY3nGdTJ2dLwv1wV2jnto2scKH4jWSbf_khTTPSoMbd0xhAGNyq4wCsxH0GjSrHV6MgF0A-yRZ9uYoCABAimXDL-mUJaPmaCSHTS8qsx_Ykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
