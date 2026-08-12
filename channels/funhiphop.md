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
<img src="https://cdn4.telesco.pe/file/VmhfVL2HADI1SVl6IBT3WQTyMJnaXcARXt6JqZyF6GbbIGfyAX_I17vYzDNucRinoYs4OmChMrpc1mcfOvOSgZ9l5H4ZGtWgUG5kOSYbpx2WGbyU53IqzS1TyLLJ-4msjlNqoV80Wu27nLJfAPoCbhUQRu9ycPv0S-SpuOVjMC22_Pc3vE98MObMg-wd13k2xSXnWiLNSkXOH9x4qYs0A5X356as8rs1TwJLfGkRl4wP2Qzi-cfN3n7VvQ6_vwGkTAS3fNc3eAzVLoDfBGIYlp_AD-oi6dLl1xHKvx8UCndUg-lhpEXAwKBpQxNR8Sc9BDi8r103e5av5gBrwx0fAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 19:54:24</div>
<hr>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxRxaITMWARGjCPQrbUiUVo5sQaFooy1o2t116rRKfswzOXnadhG5dn5wTX6I1tymNqGnn-UA0RKP1A24MDi7KrylrIxpKSs6gjlIV-sR1SlwUxyClPkgIqoTnLw0ahDo0jZ5uL9uXbgSM_cFAi_numvq6Ifp9bkFZZH6NPh4aC_tWwGEtAUvAlp2hEN2VwcfqXQmnYfH1SRXtSw9ZVUkwU2QMlu9LggwP91BXtuLH_iZH8WW0487ygnoNCuYL4MGLvl6gJCl1qY-VZ-lC6BuVSzLNdNPtwkJI7T8W8wLuuovFsddNag-c6IbwGUYhi0CciiQaCHCtXaLG-inHUIrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادت باشه اولین چیزی که توی استایلت باید بدرخشه، موهاته.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/82128" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=Gvr8cCVl_-mXb_ClkAg102lqpFKIRhJMyiqp4BHKeiidBQMhB_lxGqLVN2Q-zQShw7aNtKekoVoSgL-zTMGiITzrxBT7RrxPvHn8XLFM7JHxuRq5guZDBSsk8qPWPeSvxzIHlzc-Ryf6EAAHTg8Wkln6yBpb06vskBlbsgJ3hDYdBtTFRsJnjCThX5mbiVnt64yre4MwqehaFdbFecB7o3-ssgphSvm-zQpDayIU7vfJhwvevFGt13BFtmYfEX9cl5hajU4IAQd0yjNU5EGHr-wQ6rR7IykSOuVuVPwcwYic2HbfUMgdaxuIsVL4FsZHyY9EaNO4SaK215nBD7SXNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=Gvr8cCVl_-mXb_ClkAg102lqpFKIRhJMyiqp4BHKeiidBQMhB_lxGqLVN2Q-zQShw7aNtKekoVoSgL-zTMGiITzrxBT7RrxPvHn8XLFM7JHxuRq5guZDBSsk8qPWPeSvxzIHlzc-Ryf6EAAHTg8Wkln6yBpb06vskBlbsgJ3hDYdBtTFRsJnjCThX5mbiVnt64yre4MwqehaFdbFecB7o3-ssgphSvm-zQpDayIU7vfJhwvevFGt13BFtmYfEX9cl5hajU4IAQd0yjNU5EGHr-wQ6rR7IykSOuVuVPwcwYic2HbfUMgdaxuIsVL4FsZHyY9EaNO4SaK215nBD7SXNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زاکانی، شهردار تهران:
موشک مستقیم به طبقه خونه مجتبی خامنه‌ای خورد!
خانمش (زهرا حدادعادل) اون روز سردرد داشت و نرفت مدرسه، موند کنار همسرش و نهایتا ترور شد.
مجتبی خامنه‌ای خودش هم مجروح شد، ولی تو اون شرایط دائما دغدغه نماز داشت.
با وجود زخم‌هایی که داشت، خیلی مهربون و خوب بود و توکل به خدا داشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/82127" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82126">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYl5neIHSPeCzQJR_-Ay0dM4DympCb5guNHL4aMTRQ_XKDUNr2UXLhHHANm-VoE1ahx47Onbd40bfM6HTgyc4KiQFi0AB7AHp-j7P-lDAiU0eQnZm7XSqTNqHtyW4UQtoJ49QpLwiHCJ7tbCOBXlE753MQq_e7mFFJWchyQO_GBGzH8H-95d-_OXVU5wpSYzBKrHuHBFHZqcJFEsFI8yDV1TTBgNYoxWo2rUFq-jsyeOvLfSvas2GmovzOlxOwS_p2iFknVaIrPBAch06Yon2gK4FOsoAGzejQG8SKnW7FYcGGQfdCRAUXPCuQu8SaMJQQPKntDyE-fmdM3A24B1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴
استون ویلا
🏆
فینال سوپر جام اروپا
🇪🇺
🕔
چهار‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا، سالزبورگ
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، ۴ برد و ۲ تساوی کسب کرده و در ۴ بازی شکست خورده است.
✅
استون ویلا در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۱ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۴.۱ گل در هر بازی بوده است.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/funhiphop/82126" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82125">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGdvmO1nVzZZfxHUJSnzNp26UwN8SdI1G1UCfyGclxBFpIoiBigFMVgx06mxZYUDx22nVgDB8xIXezawkxl2LcGCQb4_A9bJCuUScHxHxNxedoOLMFTqIdNemIdXqcTA3Msm9DlngtIaEkERyvzLsONx43_KwQytPr_z3ChXQAXMBB_laRa2KA966wivw0eqoURQ-_T7jGfa8Qh7gmCAQH1rqt9I4Wax7ilnNi9AuHFTFRizIarB5z2TSVHSXDcuYGI4DgGXCHnpifHrE5oAxCxEdz008EUBt2o92Cnv32RR8EClPUtaxbWjqJKTDuX_P9bMwqnXUrkiri_oiQd_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلنوشته مسی برای پدر:
اینکه دیگه نبینمت و نتونم باهات حرف بزنم، واقعاً برام سخته. میدونستم روزای سختی داشتی و رنج می‌کشیدی، ولی اصلاً فکر نمیکردم اینقدر زود بری. هنوز کلی چیز داشتیم که باید باهم تجربه می‌کردیم.
همیشه دوست داشتی آخرین جام جهانی رو بازی کنم. چند روز قبل شروع مسابقات حالت بدتر شد، ولی من ادامه دادم. رسیدیم به فینال، اما تو دیه نتونستی اونجا کنارمون باشی. دلم می‌خواست قهرمان بشیم و جام رو برات بیارم… ولی نشد.
واقعاً نمیدونم بدون تو چطوری باید ادامه بدم. حتی نمیدونم تا کی قراره فوتبال بازی کنم. تو از همون بچگی همیشه کنارم بودی؛ منو می‌بردی تمرین، بازی هامو میدیدی و هیچ‌وقت تنهام نمی‌ذاشتی.
خیلی دلم برات تنگ میشه، ولی میدونم همیشه یه جایی کنارمی. راحت بخواب بابا… از اون بالا هم مثل همیشه حواست به ما باشه.
ممنونم برای همه‌چی. دوستت دارم بابا
❤
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/82125" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82124">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVmriylmSWxWLo6VUkNsk7D5TNAbthu2tDIWaGV3udBsFjDuVCCMfe2cNZVSbRAyY05Ka167vGpQQcQIFitzfKlCCUh34n9QoN0DmHkehwoQCMrI3bRUWC6DBnBYSzRE155Z2s45HsPVXp_jOCT4CXla0-ZwVndKb52YyUd3_kXAcpzGmpl74ak6L6cUV0quyLS_3Ly36H5zUsv4tGLbQqDREz3kXDbgCCQFlZKHX7vbeloh_G1VxrUmNJOu_dePYwPviscVh2QL5qfDOX2Zb4KfEv1uP6A6V8YLS_ddGkwPwfIpXJ2q63mORY0JiTnC_iwWOK6yHMXjzUnzEKczDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر پوریا ادرویت به سپهر خلسه ویو بده؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/82124" target="_blank">📅 18:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82123">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEHCJOQ8hWqYPXB2HUQBuGmeHxpp3_VVAt5Kl2P8Z4vNV0PpRmn6Zd0gDJ9odD2T4Gj1GgILdodqWvdAB1qxYdK71kczEU3Sdigum1dNtsoQNvijJdVikul8biR1P_6Q9cRZ8DNH0f0JvHJ7qlgshiqmQ42Ui4bv8FUJPvzkt1bl8bgBaM7_M8fSzn6uPlTrOLuyEZ3QFW7nX_uREdt2O-6hKGIiwgphYDs5ioOwZloW4VzCMe3Hd7jGiopPi4OFGEhXZ0SUr5200AA_ca6I_-Iwpe221xX-TUtVTc-AmWCLsVyL0f8itZwNGj9IYdL9vAIIl3LNbg5KtnhZkMdaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر
پوریا ادرویت به سپهر خلسه ویو بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/82123" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82122">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_xrH6ILd1jS25tMf2KcwYL9cDp3mISWh5f8CUgByEn3pKtV6aq19DOrrh57-v-hTjd6SES8oi9qL_lU7xj3NsZXyiSpOdqFKBM6HvUVjazsoCWrgdJtPp0N9-D42PRxIlwqZq2g8z-JNgqdQ3PQpHFpBvQWxulZgSsiX0974Nl5y-WokEvhF2jjTyY0-9LSUQCgu6nhOsR_AaghOsEbtRIGqwzMhkoOOES91pUbpsGY5kYc-bxRLvWBJTudQAZsGx0YnFZ7t8iqLvPxOBqbdV0nuAhEZPfxBPvHT3cipC4PToQ8cYRNRNJ1ws5n3EX4BbYDgy-nKTZ6qnK9NKH2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی، این یارو که چتای ملتفت رو پخش کرده یه ریکورد هم از پیوی مهدیار پخش کرد که بهش عکس یهویی داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/82122" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82121">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.   Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/82121" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82120">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW24n0zAUxEML6c_F4Ys9_YgasKuycfw6MVWY-0exmEYHwbgl8Hf0FxERwWn2NaQ1JI8v5BoE1ctWMC1skk_C2FPZY5XkLYt3v_NC8TbeebiIeU7ZJt8ldM9N5vxXX4BKbqgdIqKhn3Ue8rTm5Yh1K1FMl2lSrlOSUsoThyQdCOLjYbSF1rClkM-Y-GerVKl_Wtyga19pAeulQYR_G4tc6SFgQ2XoiUSGurZIH9ZQ6Qn2ui_F-APUjuX6wku78sSyuH0aB_RmykQ2rBBl9cfrIhonlWsCpq9rwDrchdBDBS989h5LZZ_-fXPOk3mHypNljqOaliOv89jg67ggMQ71Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/funhiphop/82120" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خفه شید عشقم آقای واحدی ترک داده</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/82119" target="_blank">📅 17:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82116">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOjKE4618ers6qPbPazS8jchmhVfbGKlNgOENZlSOVH2798rSF4ix71d3ivokiMqLVz_IwoJBAWUa_S6LhfenY5gPetdsl3KK25JlvRtz3llHRQSHs2ewx-F7m9c5yeoKHnFAEER3nMEc6xjgwUdD0-nAEAGepITXe3--q_SivxWUufJZ08p9EKbvxJwRpqW31PcThIzV_19bqc_WJY2ca31yhp69FA1iohwwGPtCeaYegktNLKakt26m1CK_KpwpEhF-4FhSpA-eHIGiHw6VGQ1ZO2vsn4wfwJSiRGB6p9BMoN1uhNnHCV8sGWeLEiJNX1qkaGX35_HtaaSt_sgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/82116" target="_blank">📅 17:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82115">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV6LDqCgLDoeAMHalcpNlXHpFi0eI1yhxEZGyqOTxE99mZngY6P_DyPDiaQcXEB3sZOkZtoKsa0z5FIEE84UJlX2XJh8cim0GtxRP5JzhIIpaiJZtZrUOWymLs1zjuAsMFgr-2NFifmew6y_0kCEYgfqqLRMHs3FPaYcM0pcHUcpjD1TGp6VerLZP5gwPPs2vEGFwhFp5-kKK6HJYotHd_qrqNEpvo7QGcOa4nDSJ-NWdIc4vfV2V90C4Q6Eta97XeP5j4heIT7eH6hJ2MPOI4L3VbMxdULBgqjWcp5gPgwUvss3DpAN09e0CeCq6Mq85l6R0AH7roln5Zd8C9fNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو فنا و مسی فنا باهم دیگ دوست باشید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/82115" target="_blank">📅 17:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82114">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBzza6IoL414W1KBbGkg2jsWgYEBC3RC05Q2jQO3rErpCKYwhvUVIsiByiLn-bbZlokix96IpQiCKkQu8Nk6gKYr0fGAPv3-hmm_CGYaVTNrmkMnwdtsnxEW3CYnh75amkcbXWjPj6zC8to-oX-dnvg4V4ou8-heN-rJGDVvkhbGHsKBx-XMqHr1mxAmb_w0jhtAO6WJcn1mkN_E2fk6LKoxBhuJAdbzF93wf6TSX-oVIRioGVeEdN0O2r6opT14eJBVM6XGfz1UXhQCuhZwKojBIqiJ1EibUKDOphxzOaz9chKM7lV7R6bw9n5PjY2B3xmywDGDxkh1xHvaQ4baFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/82114" target="_blank">📅 16:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82113">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیروز دعوا سر این بود که کی کیو فید کرده، تا خلسه اومد و نشون داد دود از کنده بلند میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/82113" target="_blank">📅 16:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">زاکانی، شهردار تهران: موشک مستقیم به طبقه آقا مجتبی خورد؛ همسرشان، شهید و خود ایشان مجروح شدند.
پس از حمله، اطرافیان قصد انجام اقدامات درمانی و بخیه جراحت را داشتند، اما رهبری در همان شرایط نیز دغدغه اقامه نماز داشتند و یکی از حاضران از آرامش، مهربانی و توکل بالای ایشان در لحظات پس از حمله سخن گفته است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82112" target="_blank">📅 15:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82111">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ویسای خلسه یه جا خطاب به خشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82111" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت خارجه پاکستان:
پرونده میانجی‌گری بین واشنگتن و تهران را نبسته‌ایم و امکان تمدید دوره ۶۰ روزه در یادداشت تفاهم وجود دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82108" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv9-MYHNjnCW9GoU49NLDfWIQ9C-Lj6PDhF91I4ZHljf2X4kcLmrmTjsIB-1KYK-9QjbJjrneDSJC8gcnx-4vOwpVmh7USwMMLUjOjweGfaZpyUuTg5oPe5SGo0ZIuo21TP3L8SnCNcGTy9W0bw1VJUE2ToypEnriNgCxgvH5WM3YS6SMVZs2S5RshukUyj2Jrp7H1vC--wEbPIVBBqOz1WkWDg4h8m2bao0D-_3EV5odq88pwmcgkje1gCPvXwdQrS65NkU-xn7ReOOrXY9LMIeuQPEK7dyH98Aa5b-dyw-U1BgX0FDAiLSTJN3iwZ3oOqAdgKvH55iHFPToo8BGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به مناسبت عروسیش یه قصر چند میلیون دلاری زده به نام خانومش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82107" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJQn-ksn_Nh6YDG0ynD_NfEYMkzTvq-nMtaCzG9ldgmOaGVhXnnZ5bmfdm5ncFSEotAIEjuBH_m8RlmUeXkI5NOS29MLFz8d4ORNHNEPvwJlqAwRM-rm3WEgcoZp9NUdwLMBUeWl_JRa6SWix0J3UTgZDqVIBfdI__BPGsHN2hVrTlau4ZGNeyaxGMkzZj-TCFuYDOv871K9d9YAeVqkaKKW4AHakYMVMCoimnBaLEd589HC6CjUsn8I6bUTVK-GxYAGiq6zCSoG5p0ESfq3mlg2L3XIUFXLO8ZnfgKxoEZ8ig7Ib2CEADXGIc6u-1H4rLpazELyNt6_bW374QIt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پاری سن ژرمن
🇫🇷
-
🏴
استون ویلا
🏆
فینال سوپر جام اروپا
🇪🇺
🕔
چهار‌شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا، سالزبورگ
🎲
با بیش از ۵۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
پی‌اس‌جی در ۱۰
دیدار اخیر خود، ۴ برد و ۲ تساوی کسب کرده و در ۴ بازی شکست خورده است.
✅
استون ویلا در ۱۰
دیدار اخیر خود، ۶ برد و ۱ تساوی کسب کرده و در ۳ بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر پی‌اس‌جی ۳.۱ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۴.۱ گل در هر بازی بوده است.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82106" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82104">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Foj9xasy680V36xP3WaPfbZ5qbT6kgSr_6bkk7JYwPjqdW479DgMzXE6W4jHJrX_TWFBMoWOo88fuSCsDD7keQngCj7Qg5EQJiNMmZVm2_KxT0aNWQRd-D5Xcj5xdQZ9atp2tZVmPW7pmz-WRDVstXXyJIHQfOaC7TawtM_9Or_-Yr9t1VH11bzsIkCZBMHeg3JwKE-yrMBb1mHKnSccfqbzXditZJVtbj6sPiFV20S63SDAR3-ZF2-kDtfTcjKzAS6XbJWTV7ONgg2lYG6KCLbNyqYs2D6kNHHPrCv23WKf2LBSSCXlcV1O1iZdqHBjHEYg3y6IN0NMQPB-E-JdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLH5gQl6ZAgjojf_U80WaR1buwLMxt8DzbhNp-bYunB3dgQUj1pQvXmgjk0ia5CbsROUx4GRddqMEE5Ex7knXuGGeu4i67pr1YYOEkMT5IoYMI6o6sa5nShz0QFLoSBFFH8jC8Snn7OnW5Q5zFquJ3aYd3qQ3MKYud8U8i00AZSrU7zkTOCnla8HEH4271CLbLGLYi_owFmhX9n56H60atcZJey1Zu3TTigEmHdSRIY8i5lIHWhZ6g4Jo2asu9xIJkEFd9svk1DQanctYyn-97Pf83tMQrrAzEmSJwY_67yFJr-g6QR_Ba5TaWTyuQTEsI04d0OrI1o00CSk7991-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پسر شایع نسخه مینیمال خودشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82104" target="_blank">📅 10:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=sKPBBIPqXSkn3sRvGuzKZ1hgy5_POHZmJO3Y-RuMeRUnyCI-1frOuxeF6N4_j4GEXWwHQFsSYmZKmHft-rTgZRphDn5dYpcN19RIlyiCJlSyzRFJwsTCLX3Ut1NTKR86HbGNaZB6D74np_u3CJzwhnEZqYCPgL-HkIWoQ0HwtHc0kS4oUd5VmcJ-vYtyLtAhy2QNsZRd6f1fbBofcSwb6BY63kWCun4ILypRg_j2CL8pTpWG31pVIbHzijUba1DKWoYaUh42IBhM1_d0nOqOvN4wyn2iy_MhjvwdLsDtJPrE32QjUEIc4KZlN5AsDPuiyIGDPnLqBqzt77WFHXUm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=sKPBBIPqXSkn3sRvGuzKZ1hgy5_POHZmJO3Y-RuMeRUnyCI-1frOuxeF6N4_j4GEXWwHQFsSYmZKmHft-rTgZRphDn5dYpcN19RIlyiCJlSyzRFJwsTCLX3Ut1NTKR86HbGNaZB6D74np_u3CJzwhnEZqYCPgL-HkIWoQ0HwtHc0kS4oUd5VmcJ-vYtyLtAhy2QNsZRd6f1fbBofcSwb6BY63kWCun4ILypRg_j2CL8pTpWG31pVIbHzijUba1DKWoYaUh42IBhM1_d0nOqOvN4wyn2iy_MhjvwdLsDtJPrE32QjUEIc4KZlN5AsDPuiyIGDPnLqBqzt77WFHXUm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا یکی از دوست آشنا های این ببرتش تیمارستانی جایی درمان بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82103" target="_blank">📅 02:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کیر تو بارسلونای بدون فران تورس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82102" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم دیگه نخونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82101" target="_blank">📅 00:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">چشماش دنیام بودا
دلبر بی ناموس
🤙
🤙</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82100" target="_blank">📅 23:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpd0Bd-kBfB-MP45iYldJzE3f_xrF0fvOCx3H4cZ-eL0FBnPkzkjOX9footsDXXKcMOM8OG47gZXl9hQimM3lk14ssbITdKrE8FTcDMbroU4wAICHwRJ9-qGsxtFPoEfLCcP_e0Lj8vfRPwfiAGhioU_xKxtY7lPWNTEFHBAVS-JQAJvc_g_-qKRIDZxL4RD6KIeq0Tsj6DIyfJHPPgM8NEjf1-nKyGZEPrV_liN4ChkKUV0HHSxB3PE3K4-FGJjP2_c618Z_d4nrb1whXZmaLftUD8PRya55LKrfyKcJMvKZtQ3MiKBIjh2A9LWWR9r4A-eS3cTUCaIfMLatCIfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس فقط یه کپشن "حسبی الله" کم داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82099" target="_blank">📅 23:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMoIPqbAlCag2yVEMzVDawQ6ZgqN9pS9yekREUmaVa0GMrk4Yw1JYydoTPRtnQBp84GNrYxD-McHxvha7xUuU3PB-IBiPj1XpFzZVu1xcePWfAWI8CSi7w-2TmEypoQKHmwgr6f6YlX8JOyXYUOZ4rp_vD5vy6iJX9rMT2jTInviePexRs_ylWe__SGohXgFJBAYE9mBwwA-toksmK0da9fgEBx1NicB9YLBnE1YwhNGMwaEIB0iHhZRcUIM-xOXxT7qVBP1OgryX6hIqAYGMJb17-AP7hzPZxGV5q8lQBR7F2qcldBFn5v01FMqxoD7wrn0mZ2Eug1i0x9kD9kQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو حرومزاده یعنی چی که اسپید رو دعوت نکردی به عروسیت، من بت زده بودم روش</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82098" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSSuC9suB7PjCsJZUntRqN4Uw3wGFYs6jKVdE2oD698q4HD6IBBEOXOsbHhoqG-BCy8EgtZlibrHE3D1yWj7Kn1wRGKKt-_dYJQZr1jE6H0RRQDcwSnw2G_VFLaU_quH_pa2ZAz9WtOZbdAq0Vd3g4kMU3bk27gNJd-MMZjMeBpLBp9vez0vK838kJnbyuoiOkc7yFkkQJ8QGWORbD6OVWNNIexazaMgrYgWfuFDjrejxXOIYXx2YbEaKzN8SNWjXLNaCd3gw3kSMaVJebpbwqE7yH8umTXr1JPI1Ery6KM5aDEWhh2wg2OqktQkxWTg1ZyjXl4jeQnewj0k4ATtgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رسما دزدیه‌بخدا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82097" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رونالدو و جورجینا به قاطی مرغا
هیر وی گو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82096" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBxH4kaByKYJAU3U0UmXS8pJ8Remwos9xHu1sKFjMfK5uU_1cTDozD-tNec0lmfCymAEhtfnoMhCFqzkBeK2EzOGW6CQjpqwS3gy5kNz_XsBvakgShurBgW1ZOn0Uo-m_f7wRDtqC4Pjw8t_Gguu9ZS26gl_jkf7QQ-NEHBb2pRjWXGh0F7cJLvRz2_sWAzpNOSpJX9Gk4x3jazTXYWkkYQHjtcaRXRHHoiN14pLsgfHajXPO-k-WwvepZSnCvkH6VzkmO3283wrRk09ypOeoYfGusnCrh8vDVg4L2KYlsH4aPepgP4BL7zIEOwiadM_K-vSALCl3pHGYxNt8ShqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داود کیم، خواننده سابق کیپاپ از مسلمان شدن میگوید: صدای اذان در تمام خیابان های کره شنیده خواهد شد و گفت امیدوار است بتواند به ترویج اسلام در کره ادامه دهد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82095" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82094" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82093" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mST0_T0QvG6jSeOqJNW27_xmgEOLZ6Gd2KDmT_MrexTyCL0tHRrQd-jf4Jzpp8xNG3MDPa-go40tme6m5BvF-i2FfrSGQhBQc-LZ67tYDztVzSqxwDKZKlGG-5kIW6gNK8fEl4y3X1eRbjnJhLYAXR_csDXz6OXuQMnwB1dJ33rfR9YG3zyzKOc_F9PzmFt9fbEKvg8_fwy_zD4O1KVZO3cwSkBqwoRpKef8I5NCpEK5184TARwxRSjJflIBxAPjPnQ7JFObYO7reUq5JKdItF99RLaHm_bgOq7T3_0aIY7ecnxpUlj6UgoYJdOJGaYTnnqRyAGrUjZJ90raiRWTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید خلسه به اسم "
Margo Zendegi
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82092" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNn80o4h5JJ2f0ZTQ8rOkKsZZe6d_QpvBb8yZaDskohLxs4ifohb8GRa3LGw-ARMc0Cez3lBAQ2lZT2CjQSOkA5v1D_VscsVqSZGDGnrpMTcX7azNn90T_q30uD3dF6uCUdk0wUItdX1ePPoCF-Sha6cAXwVj4n9EJORbsdFn6XyIbNleJQ2tpN4Th1VFnrM2KQQHJKKJvIgZ-3Sa5SKOHLtVHlXl3jqfwuCETUA0HerCgXBM3Q7RrJCqJFSsagdJe6Ddbxh4yOamGGJ-q0zGdaobCTkdPQoSfkasggc1pLcTfHK2qtvYan9xnEd93BviJD1wd5Jz8JVxZ6UAGohLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ایده
#تتو
#مهدی
#پسرعمو
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82091" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbK_gODGcVvrlpgPazFu7HR9UmrXmVV-OhLFd-x-xUtZx5v6vv0FClycqxv_9xLMY_Nqa3KzmCPc3cn81ftY9pRUoGMkAiXCpfSnBFaovWquAfOJ_6jmer8B2mgt5rMKgYxAIkB3RuA9PH7Naqfk4cQQX9OEvhTnGhw9468qot2jhCdcrtVUy9FzBoqh_BSYKstSfyp0hqX3PWG6Jwb-PEpqzt4htHcZh0jkOt1M6cYDn5KRsdlZEJnTV3XNksF5fZSQOvoIdjS4fZeLT30SobIVNFndRJ773vHU2inoresjeD1m_7-GJ5b8WwDXTdO9QfUL5a4RGvEppHlcxVXfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علم‌الهدی : اونایی که داخل کشور میگن جنگ رو تموم کنید، یا بی‌عقل و مریضن یا منافق؛
فکر نکنید اگه جنگ تموم بشه آمریکا دست از سر ما برمی‌داره، حتی اگه همه‌چی رو هم بهش بدیم، باز راضی نمیشه و در نهایت وارد کشور می‌شه و حمله زمینی می‌کنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82090" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfozuaypOmR7EC5qr2gX_xaDNThcXpfIfiOz1n-1h2IdEJ2A8fzLckLmr44vTj1n1Fsm4NocgtPy-VZuGMpz9WQ3wDr8-kkr-Yo4eAowLN0FwDwpJBmK1g895zf9OpymeLx-mdAQevydjfvDLi6wJJrv5hFHfyQGZrYKak1uqVF-33iPRS_36ryK18GE9aC-WGaytHd2C61IPWjtufgcg_nXYNZ4qaGCMhydY-XLbfU1ArXNpUTPutX4fcbNQH4pJ1eucv4DDfFrQuHrXS7-1TXGcahGK0e2yZdbymiFncvbLULMk164VleN7T3fHHZa98kKj3P-ROKBHIeV8nD5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دولت لبنان رسما مجازاتِ اعدام توی این کشور رو لغو کرد.
مجلس لبنان با اکثریت آرا به لغو مجازات اعدام رای داد و این مجازات رو با "حبس ابد + اعمال شاقه تشدید شده(احتمالا کارهای سخت و اجباری تو دوران حبس)" جایگزین کرد.
لبنان اولین کشور عرب تو خاورمیانه‌ست که مجازات اعدام رو به طور کامل حذف میکنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82089" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okoR854haWoNxZ5d7B-lE_w9AVFYTiu4QYrYEcIckhVao8o1dYxB_LT7W__5XJXDOADm32tm6aRmXbMhN7pxw88XXlnVlLZKKg6j-ynnk48SqfkrWv-43iPrN93EZBGjm1pi_lXP7rWQZa_JeIZXKuh3hLtkntRcpTdBSoHci1MxMSUG93pbxjOLl7Q_CrAtYMkX7DKdFO0vujjMcDv2PK_HrJwLFf9JrbG273ADrEZggbVteKPXaqFno6ZRmnNuFo8WTp1mzRvsR-xLgA9f-ZN6mh4V2B_-uJfBNo4bc2QfD2UEAvVG9BDQ4pZU9FUyiuqrV0GxkMqpgvLH2WcBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82088" target="_blank">📅 19:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اوه اوه آریا یوسفی از جنوا و مایورکا پیشنهاد دریافت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82087" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=EFCtzaGRmyqDlA8xoRgToPBW9Uqs2nyf179EFZWCE0Kw09i03_ORy0Qln3VZznQyth5BwQz2uhgV8wHZvFO1otU7oCVi0l3QBU9xhxf56o-zV9uw2NDB6nH7GZgW1Ifvp0MrRNgAMmRXhCmV7yvaVRd7j32-qhGlcneZNI5FcgxFZwXmG5FkPyQe0Fn6PlpHGeC6xx6oJLbMaqhFZayFVHmHre7p7I70_WhqbGjwDzol4CHEj0Kna3LYGmmzVA61OOJciQL2m8h9TfpPunWtfcn8u5-ngBx1ljY9wvIJ-7SS_gFAHArF55VtBdIU7BCABGFgZA_j9OipRrpSuk7P9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=EFCtzaGRmyqDlA8xoRgToPBW9Uqs2nyf179EFZWCE0Kw09i03_ORy0Qln3VZznQyth5BwQz2uhgV8wHZvFO1otU7oCVi0l3QBU9xhxf56o-zV9uw2NDB6nH7GZgW1Ifvp0MrRNgAMmRXhCmV7yvaVRd7j32-qhGlcneZNI5FcgxFZwXmG5FkPyQe0Fn6PlpHGeC6xx6oJLbMaqhFZayFVHmHre7p7I70_WhqbGjwDzol4CHEj0Kna3LYGmmzVA61OOJciQL2m8h9TfpPunWtfcn8u5-ngBx1ljY9wvIJ-7SS_gFAHArF55VtBdIU7BCABGFgZA_j9OipRrpSuk7P9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان: طارمی بخاطر تیم جلو بلژیک  گل نزد که زیر فشار نریم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82086" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=ZciqqGvqW5XmLawUOM2kgKTDY2gr1AMBXd10oqegoQhbPqMiQJyZWuKrP_CFrahRxdKguAp_Zn3Io2M9RlmKIENeHu-UYoE2ooJM0254G6mWkq4eEtSCmISTwcpn97Aw9LsU6M6vvTcByjrDy0C6BHbpZYOCKBODfcOaF_v4RncI_A1Yt9cDnyIq1c7PPDe4FFiXeRA8jYMpx2odFcS0cKsIqLCV2gFKKNqCZjXdiZ7bCa-dz_TvrdKN2pplSxKyTrpzsJp4J5ZpnXxZZyL1plXJcqo1oe1iI461hTcVwBeq5aDdrd7s3FkDdtS9FBIY2YUJbo9U18siMM-Hi4IaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=ZciqqGvqW5XmLawUOM2kgKTDY2gr1AMBXd10oqegoQhbPqMiQJyZWuKrP_CFrahRxdKguAp_Zn3Io2M9RlmKIENeHu-UYoE2ooJM0254G6mWkq4eEtSCmISTwcpn97Aw9LsU6M6vvTcByjrDy0C6BHbpZYOCKBODfcOaF_v4RncI_A1Yt9cDnyIq1c7PPDe4FFiXeRA8jYMpx2odFcS0cKsIqLCV2gFKKNqCZjXdiZ7bCa-dz_TvrdKN2pplSxKyTrpzsJp4J5ZpnXxZZyL1plXJcqo1oe1iI461hTcVwBeq5aDdrd7s3FkDdtS9FBIY2YUJbo9U18siMM-Hi4IaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چقد عجیب شده، تو دیجی کالا مواد می‌فروشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82085" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1tGgIJzytYUKNtb5XkShG98bW9_cbIZZl0wAa4JR3mJWofSejdtPS6nGMUtx87RlzM3DbTSpTYEoEXIQBjKZ_JY95ALmcHY2iUjV7JbTKY8Uj-IW9d2AdpsGtanxkpJbReOjnQ1UkroFR60iwDW5P8VjTe5VR1JeuHK01kcNmc7CXOW4qgAODv7PMmE6asTybJ7SfnjXYMYXE29iIGpMlbGXJ23ibJKCd7brDqgK7FK49uz8V3k_WJvu7gwkacbscrydlOIbFY6IKoe0y6C274Vj0qDnZ3X0dKdqGKS0fvwyzD1K6qkACDTAAIMosawH2q6bKR6yjaeDkQ1dLGOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دورچیو
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82084" target="_blank">📅 17:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82083" target="_blank">📅 17:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82082">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DT6gYyTDILS9nDzwZmsGjtaSQHf7jBwUQU8NdI5Nr3lWcgobEvzgugZiLHGqh-I83_wXjYwm1i9vkkkF81QFjVaU8hkkbC5m3MbMqKpzloKsWXinn0K8skF4l4NGdkf0zkFAuZVKFT_EfBp8MgjlmJQ_tBhh65ZA6uqftLRPi-zQbmL1rVm1vKgrjsrageL-pObegsMIDV_lbiKgdLeOgVGh-i8GaR7FX5XRRDtXQMYKpE4n0Em4p4WhMvcz7Yr5Ix3hSF4H7vJaYnc8nV9wh85SEf5X1OmPSCjGjm7H11wN3YSG-DU8nWlMkSn7pFv5srjGIy9qaAl3z2ca_RMxBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82082" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82080" target="_blank">📅 16:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82079" target="_blank">📅 16:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGzjWysZMSmiKR_yclvhubpdTRoUlX2XPRdFJtpyrNYS55R3CackrWQErFPMFbqEutePjkjMwItFLctNG7nXmrftnbkKbOS9e93e0JGvxq00I5uvcIOeGBPklgxzgVM4zxcQVXcBnyOVdpJmfuw4vfTHYyX0pp0BAqZkqu3YUzqY4iozih2EpbJfDOR7gMdgwEPBpqjWxtKRfjqC_AIg8YaYqKGtooTT9nO1MCuJoLWjNJkl551WLMh_Bkn5VnEBrFQBYgnpGZ4RPH3TljVZ_1OiOUqJQl1RmRCOG1q4pG9VItRjlU4mVgpBnERrqvzGbBgPBTZip_JVKXv8XxU0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82078" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بوی خداحافظی از فوتبال میاد
مسی بعد فوت پدرش هیچ زمان بازگشت دقیقی به اینترمیامی اعلام نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82077" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-gHW2qERDQwEDLGyoPMGB4LhqgLvBq9XfiJKMrU_l5GBq8qYGKIdt6jOsUOuslGC9SWmLyQMwa6z0zl3d67RowYUXhF9z3W4_OY6TOllPH0fiJke-pKE4mnejqsFYqU90PyemXrtwW6VK6Q96sx6Pr9zsPf8hKrhD7X_z-IG6xNVjFgtk7ExahUlfvKsZUc81DCC4XKKFY4NIa4qRc0QzvzZ1FVSdYWjOcyImJsfTFcSekfW9BTVId_o9GI_Mpe5V1YZo0oS_qEXjVzNTtTfycOTTb6Pddr_EUaA5lZKZnOObJHxzPwIqe4alqFRAIE8DThn7qdFqjJX7M_u0bkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه میخواد بگه دکی بیا بدهیتو بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82076" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYoE98jlnrY16m-smKt2cVzMGMHDXRokkbG_LUVpt0VZVX3-B5ywNfD13dQMsslhTJ7yE39OoY1Uz_uhhr4l3AYcQ-6OQaD7YdbDZd67UDPn667T5rP1GDPRnUsnTyItg0JGvU1OMeIghiCsw0N66Jq0IIUf38eh-AUKWTstYrgI-pHkC7y48irtWFWoor0Iyz_ZjRaiwEvbwuRTHQDN0dPsF4HLHPDTewN78K6y-G9-LyRvxp1EmY9kyXmp5E7lWkMJ6BiPBU4aQgrJItSG4VA6xfcNu80MgEF52ZzJZ-B-Pt6qnBYQrM7FmLWmjpeFtpYi3wmjgoldvjtmXL9Gvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cJfWGUdLiQWFomUUyihKYt7tgNTR9ZewW3szY0mSbjF1RtC1Bfkasb6S0A9iOx_BTyViLi2ucVRe8Kl6XBAGvDh5NoyF4tJVO8ucm6xKvKOzLC0ANWN105m1dRX8gEsKMZ1qDUUomZJYUtS5l5Sy7qVFb6_rzK_vBHa3Ck7ia__e25UveW9gfYUFI6B510FmzpNeAuPie4qjXWVA43PeqmMWWaTcdOwr-NcYrtHta-6MuZMfLCAFmxDa6jO2X7Er0n2fa-1r4yaMl63P_IHvpOMBOrUR-mnQ9JobwPt7CFq1KsHJzV6QAl5m4gtmY-zZlohdTODq0nfvmgd-jgpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82074" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlA5MacPEgsh4I8Bt1ep1i6sShyGWdYjQw_OSEv5aRVu0duxGrUs9mnP7F2_AVNvkTBC715uEldphzY2UexEo1wSVAasORnIhyIk4TBEAQXOPTP6PlKU3CNK5GQsw8Lyd5oOL5QCOLgu2S3LxiK-khKS23jnIFzrgH3535J4GjQFUp9wg5xQeZfdQNITmxE-191PbbAbFDqcDaTMlwUi9hUnN3kB3CQTSsLUEnME7zgq7IC3mrxa5hTy5UBqwb0O08b-dI34FWTKXx7BTCc8u6n_fAjNLakoYPHVG1r3pkPUYIpCgpAWJdNyrj5-gskgtz4yroNweEznA9-S01zb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82073" target="_blank">📅 14:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82072" target="_blank">📅 13:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82071" target="_blank">📅 13:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq8Vky40tycb-yKPdF57Dd8xIscpuEIKIoeEkwlGefKtaeXz3XTt6eItFnHAS2HMIJ5ObHGP-lgFyYs8uJVQ2BX5IyL9E7lwBSWPOAafZMYt7w_JlOUgrA-Gd-aYtVAYPT2tQdCO_s4jOfu6lD6oVMkMUXH2QFDtCThkdRVi3SDcm6NZ8ACwnpR2e3cuQ0RbNcT3SDx2qSEhoJFdkKL7REDS7NtrZE7B17jlStfw_Gi2ZQsattWYxJvvIsnQcrXr71o_8PZp6D_M8K8YkjQuxOoXOgju3MWpIYpVeG-519j3rjGvEOaesVKrXv67w6MzcmeVN2f0n3vTNrGXK0iyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک پولات به گا رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82070" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_9fi1PGQKECEHkdL4KTTGD_W7u_ZaQw_FLvMS9xgcOlEbdURFY-gELjG-ePq6icQOHb3RoNyrpd86OcPAoPra78z06laJZ0sD1dm5C2rlCzpU_LJdjs0ttd1B_V0xjjyuYPsIT3TXQYY3PKB-4qJvBjgoryKObvR_O9WC2qe2I9z5swP2ihHUYyCh5MFlGOWMQOZQeoOTy9_EStGulFS3AkgZueWesY8PmEzYNMIuebdl4Zr1L0CIPMHx7MIDp6nm-sedrPmkxT1Crcw08aU7aLI0H0iUDfn6DHP664R8XdPbBshzcYG6GnB5xPF9eWiPI9YPFza-b2Qnv0BP9knQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82069" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZd5tXuy7BLoTFZFJBbCo1BNDeuS2mb_vpb9oGEY5sQBuV-ujjwRx0VIc_AWZmtdJ71UTWkSePZ7EOWoH6B1uZFQruwGnDQel-LHJcO3ryM0e5LjJV0Y6-0tuqUeq4fyT9iIwGm0kWwCj_3V4f9Oiwg4dbY5CPDUS20IczF0zXEz5Uz90nnK5Y9qfWLdsHYEZrv9URZCRn4ANijAgfeoNdh5hQToQvB9K7COoG6rkwqC_hd8seofcu2unh4RdW4PaXf5Y-HgAPF57RIluvJDOIxlB6gWl3SMm6Nmob33eageVERaK1EzAVL8kPguyYw8EbvTQdF_FZWJDMk8Hw_DvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82068" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKprnrkmi_6aJoC2UmlpKAy7tL3cYuD-7n5THFRL-6S6yqS8iKmk9sjFyGJH2VEejCTxZhgknpcrqiCyM1NgXMY3_Pnmz4VrHHOn3DknCw3nuklAp5ZtsvhME5t81UfI6ZGI9v3U29PTqsMLhqJQVlBMP_9y-q7tdehkHLElyRRo2XcS-uuUeFaujbY-Yt_lm8f916upCKmH5u3uzhLmRXP5qTeNqFqzhfju1ivTjI90QDA_KEGzQV5zMqzkAmBYE5VS2G09Ipts1Oax2VqZb38n9Fv-JguKs-vWjWrKINaCzknOYXGZWYa4CYJkUSHCDPPrNRa8hHLPsLNhYJ6V1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری احمد خدایی همسر جاویدنام صالحه اکبری از پیامی مجاهدین خلق بهش داده شدن که در ازای پول علیه خاندان پهلوی استوری بذاره و اعلام برائت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82067" target="_blank">📅 10:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">داشت یادم میرفتا
کصمادر جی جی و دانیال ددان
کوروش
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82065" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpE4c56J6KfGPMYDEniYgxHnVxQbXH032OYO0UoZDIwTp96he0yS747-T_KLJOUOQaAc0mkR-pDu69qg39Cp3kyiyXfadGVxrjOvkJ6F4sv_tuQQJMBLgmZz5bbbQ5v-iB__450hk-tJ8QcwQdwt-Dbu_RHvMJkkhpMlTnPQTAUfnlvlSv2Rr4oW55fzV-vbDzZKmvFHQY_70ZlZUMOEUm3i89eSPrPppDvjndS4oXoxEPhD0JtUHRNBi9WAnz54-DuuQy6VvzCfH9lFRKKe9fPErLnNTlBrVAsxzIxxbq0BKdBqdcBDKGuzyf8sbgsPE717yHSoYm2NOoh1oJTnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریک پنج ستاره از ایران داره تکنیک های مارکتینگ یکی از موفق ترین آرتیست های تاریخ تو این زمینه رو زیر سوال میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82064" target="_blank">📅 01:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دیگه حتی دکل سیریکو هم نمیزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82063" target="_blank">📅 00:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UE0JWuV-reQ2U8aEkKkKtAs8L8T8MKCD2oV0J1Qau5S-v_oNhFDLaQBxyNoakfFsz5nuHZm2WQOZbNkA_ki2WJRlPspN_iA_HGepbEQW2K2EZTGi6aY6jrz_Ee4B22cwzVTApBiGJM6jTwhVLyEkInJbnvApCvGQ7xVox9bthGcQxKyPvAfd-SgG4tfikNXyeAULuaX-WPcjpSkkVKciHo0VAIfOZP_k01-S_7hCu0zMUtYQex8Otq8ruL7L3TEBqJdf5B24xzs7wFkNeRKA-QPycQTfnFDNS9qlSyAxOJGP_FuM-nf1tHtVZ2DJ-CHmkyTI2oQZX-OQzRoLgvVHTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح امیدم به زندگی :
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82062" target="_blank">📅 00:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید. _چمن در خاک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82061" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqTjl5s_DV2SpTwgcinBBh8rVd8guFb2O3-EnunSyyp5Lpc1WAZ-mbxqfUoat4Pejp50ZZW8Mfug9pYQ8ID2SItsNMPQEg8HBmt2X_KfaHYlh4eDKEX5ph2h454119ccZVJH5cg7RT6TfGtyS_drgyK9ft7Id0LTpFwY2u4J0FVCyARoWTmLxzMJ98EWG0gxHO2567LEJkTXeyAhYyyV3L-TSigXeqj-u1LMVcgMxYphkgFK9sK99yLj1cky5gmXJ5I0bUGCObtU2qlUAG2mwlgO8ZQACWbhJ9wVE7r6Wg0yrHdI9aWYYWi9obQqGotHbTllzNz8zhqW5uh_gRiLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بی‌بال به نام آزادم زمان منتشر شد
YouTube
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82060" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUmG_L-gYJOJF8Z5-UA3A23lORYlTRL5suC1yhZhnehZ0giChAJ7bavhEdzVEd7ugqvrEI8d_WdVfK60wtNhdfRpNTBiRUWMKHwfDMvEwiAVmOW5uNNSvyxwd7KEq6ZvdZJKX-QTYfvnnEM3YxmFWmqYO09t-NwrBfaIPlLjfKUPqfUozHubnNMCs3vkT3-iBW7tEeP_XxXzAcm_wEI-QOtXGbNCgHLyrmGyW-Ech9qn6tzdDa33b6Ebb5rMeOH-piyCq510wGUXPAOr6CtYDvQlu98G_DTjyhClV7Nsxvx3Qiss-c2r8vcLQsXPpamHcWKfC2N74cV388R6SRPt2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82058" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ عالیه
گفتن خب تنگه رو میبندیم فشار بیاریم، پاشد رفت یکم اونور تر محاصره دریایی گذاشت گفت اصلا خودم میبندم
گفتن خسارت بده، اومد گفت خب من که خسارت نمیدم هیچ شما باید به ۵ تا کشور خسارت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82057" target="_blank">📅 22:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید.
_چمن در خاک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82056" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82055" target="_blank">📅 21:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=ElVpy6Yub308EpBNFpdDGxnlWyT2TMPxMwZKv9HFpm2C13sb03TcGt4MyBbswQFept_QpROz53CiLniiyP3R4umffGuOuwirHOTqtL2j2-a8s1xPULdyUUwvTQnxHO1xK6BjKIZuy20qh4BzYpQMZMIW1cTv8MpCWsGnmX_GteeEsECQ03yx9IGfictKHAdS59Cm7HvbT2oJrnuV_D2zOcyFxATquysjcyZCr5vfN98kFbd5Np9W7xEQ8iLvv3m8khaZSLU0Cefk0t_i_zzPQP02Qk8s0DdcReQb5a1UAA1GtOHwMmhmKjBuJ4blJSxsxfF78mxQA0V-4rGeAPDk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=ElVpy6Yub308EpBNFpdDGxnlWyT2TMPxMwZKv9HFpm2C13sb03TcGt4MyBbswQFept_QpROz53CiLniiyP3R4umffGuOuwirHOTqtL2j2-a8s1xPULdyUUwvTQnxHO1xK6BjKIZuy20qh4BzYpQMZMIW1cTv8MpCWsGnmX_GteeEsECQ03yx9IGfictKHAdS59Cm7HvbT2oJrnuV_D2zOcyFxATquysjcyZCr5vfN98kFbd5Np9W7xEQ8iLvv3m8khaZSLU0Cefk0t_i_zzPQP02Qk8s0DdcReQb5a1UAA1GtOHwMmhmKjBuJ4blJSxsxfF78mxQA0V-4rGeAPDk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82054" target="_blank">📅 21:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
-
من می‌بینم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماهه گذشته به آنها وارد شده است (آغاز شده است زیرا آنها سلاح هسته‌ای نخواهند داشت)، حتی اگر هرگز در هیچ یک از مذاکرات یا جلسات ما ذکر نشده باشد! اما این ایده جالبی است زیرا اکنون من نیز از ایران برای همه افرادی که با بمب‌های کنار جاده‌ای و بسیاری از درگیری‌هایی که به خاطر آنها مشهور هستند، کشته و به شدت زخمی کرده‌اند، از جمله خانواده‌های کشته‌شدگان در ناو یو اس اس کول و هزاران نفر دیگر که در جنگ کشته شده‌اند، غرامت می‌خواهم. علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است، غرامت پرداخت شود، و ۵۲۰۰۰ نفری که در پنج ماه گذشته کشته شده‌اند را هم نباید فراموش کرد. من به نمایندگان خود دستور داده‌ام که این موضوع را به طور جدی در هر مذاکره و تمام مذاکرات آینده قرار دهند.
-همچنین، در رابطه با مذاکرات ایران، ایران باید مسئول خسارات و مرگ‌ومیر ایجاد شده برای مردم لبنان، سوریه، یمن و غزه باشد! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82053" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0ejUZtI3wdDuYgUTuCW5w45dg-o3CHQaMTQmY9-jBBs25-ZmdIF2SUyovsLXlFMU1wfjkc4WN3-zSXV9GXdiR9SPA9_MdatS_BJ3_94sMQYGcO0P2xK9-qaBgR7YL0JyzlKB3r5RHSQfSWYUvWSEyRMY6TzDTF8ikKPmFsm0YhoC8yOLJoLzCLqUbUElPxu7q5-qtnCLdp5xdL-Imm4eSvRJT-9zLqdjeHwniUWIQc18NfHBMMH4tQESMSwq6mVP6OSEScJui4L3KLXQVEwvZjh9AMlcAOJzBLBp56jgRJg0a7BmuhGFi-tKn0BTPqVKoIhciX5w-GgVFiQTGkuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید امضا کنید لطفا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82052" target="_blank">📅 20:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0KEhXlldRHPnwSSbpo941L-c0nMyzIuYcOQVYOCn2F50j-I5frCCw8TX6N6xooOiNNyoq32xA2ICf2C6sz9syw_PngLlqaFuheJD41fxCJHPiiHvRRBf6r7SRoSOqqojFs6KsqVdS0-Alsd8JzkwVqz4Fthh9yqU7DFRs_lAIpOngjsKZhAOKvh99h_NJOn2GJbHrCzGJaQIlMsQk7inj5I6cz9GnjslWaly51Mt1iGC7TSNCXoGoUBEOvPdQ2oRs6GXiY3ivsZ4pheVtZQ_ZrsHcOwdSeenZfuCQoO9fvo_-OZDOZIcPg_-N84MT1pFWTn0bIBwpO2CZ2kmZ2C9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش سه تیتر زده جهانبخش رفته تیم صدرنشین لیگ هلند، حالا چند هفته از لیگ گذشته؟ یک هفته، و تیمه پارسال ۱۳ ام شده بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82051" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr378ncM1vISHg2KOK21u9VVJ6tD_Yy2D6JsFi2mJAG7LmfqliNjx75GA1VoaAjPWOSCD841LZflJ8hw4heO1TGY4sQ_GvYBoA2uGBQ8K8sV5MqRr8pE66yQg05nAGzsPDswiI7StT-Q7MdKUft9mSkYxKP3q2nJPcj26k6KOwOb5bNkOF8qA1DalwM1xT02H2nE2F3Iy-l6Hx0H-grnJAF6V9KdhY3oofDd2C7aD-SkgkBPdnjPpqkzh4a7Y_YBIAyl7LMdQI8gk4IlsaszLMjq4m9DRN8ZGBacLtSOQhUbkBu0BisfbvopDMOqTS3pP34hvadCfE94UxQEct_9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82050" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7uyuIjXuW7WAUFZWDdZz-TnuyQtHvm7s_HN9hJZlqMrQtEi63JX1Vv89pU18mu1RbP9xIWd2GzxTQJJ9g3i9f1m2fmUL0I6Z40lTudK1MvJB2g5fJetpkWt31xW4lnzD0-OJIg0Ogpo0klKl6CF1bPhNgjG2oiXTFNl7GU_1RWrYjWg_-DUuxNmCyDSM4SZaVestgzv46wm2CunpafQbSEQeK5_6kK_o3ssOJ0GG6NbIIz8xQpxdxa4YYrhO8QAk5PjTXXB9MdT84DGK9Pv7YWzoCgTI74N_K_IwubHhrP7CPxiHjecQENaA6HCpIKBIOmUs81t0MxnwOdVihfnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید بانو لنا
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82048" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhtDZN6S42rsnOzN6GC6szpuiwhS339W59I4RSnrg40RIS7J6bY64sCrfMthX7PpXRYcXp8xHy_QkBuf3BXXFuU8jrkjIynBxr305_L7G0AzuSKXYL9q_SNL6U2riyRYB6tyDavpmF7NbGWWultpSdmw5WAXfQS9cyY79N7y9knTJVD-CDVdEfktmz48N586VzhViN4P89NbAZ86rq1ZkyfKRtHtMcFr-B6N3r5rht_fcte4Sm20WLa4rqNlRY30jKR4Qy6wZuGMBBrxwDM_G4xiA2FBGfE1A2Rk7iUK3GAXgW1dMBFYrsWREymBpdgoEAeLdB1ayoDjeyDp1uqKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ویناک میگه دکی لندن نیست، ترکیه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82045" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq7p0EQdWQtmr_zICAcAWrumykNosYEw5nw2SZHnhAY5M85lkJYq-FZSCJY8czwTwDsKRkV2mU8yWxO3xO04f32Fm6N7r5QHQEsTlvtR1gqx8020SDB0WnJWnS4KcT_D0u9ZIv5eTQPaQgO7KlCOEvqZto9KDH0_TlsbakHnRXJRypdmNqJo6CY3TTtAmGCm3H8hx_IJzcFMpm_0YL74FQoTxAKiVYtGGZedziZs-9Lj42xFXl-T1YmyCEzvcuqP2MD4GSyOrU4cLcJws5AKtvIqwcHABMamyGTmpkmCFvos-JIrJ74bLI8eZAuumh8G734khM7FLkzGZGRKph70eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو به روایت دریک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82044" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=KJ0_8upwG67y0u49-qwI8eKc8Hk9Tm56njMFlfQny6QtlA2eIMJRELviBUP1Aftnqx6RtPlGS1oo1bHGMI-6WSVlwyk-ZuVzzkgWOmHgg4I50bd2zLNQ4xb8x1Tt_7gKSCfmQFybxZ9oF5897aCcI67Nv0QLRLkHk0LyoJWDsnkj44GW-hU9lx0vTXWCmRez8LcEcn7is7XgFqDzyk_mdDYhQGSfqQKeWcE6q2o3hILhD3DWE_uBwRzTwzDMlthfwrqcC3o19FWuKrz7u33lmRT1LPC3uMQ96dQWkcGpddWtgkECjK4Fgs4TU30nzRub3glK8qkhgamIVTz7Aawp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=KJ0_8upwG67y0u49-qwI8eKc8Hk9Tm56njMFlfQny6QtlA2eIMJRELviBUP1Aftnqx6RtPlGS1oo1bHGMI-6WSVlwyk-ZuVzzkgWOmHgg4I50bd2zLNQ4xb8x1Tt_7gKSCfmQFybxZ9oF5897aCcI67Nv0QLRLkHk0LyoJWDsnkj44GW-hU9lx0vTXWCmRez8LcEcn7is7XgFqDzyk_mdDYhQGSfqQKeWcE6q2o3hILhD3DWE_uBwRzTwzDMlthfwrqcC3o19FWuKrz7u33lmRT1LPC3uMQ96dQWkcGpddWtgkECjK4Fgs4TU30nzRub3glK8qkhgamIVTz7Aawp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگتم بانو به روایت دریک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82043" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6LJvCsKpTYLJoIkYheNvHftrVu3XsATb9qEhXgr18CKjD8xHcfzVgR817VrwCsgVKzNLez9LOZFyFZNnOBov2wlfcgRCA-21n1cfD74BTO90HJlYzJv0FJ7csUkvRuvHGXbRL9_nc85HaYgOOpXUTWtUzVrpistamqP0ZeJ-_IHlnNbKp5upUQ2SQOp-L2pxrlyQPtj7LRwL-9nWPzbnJfv3jOkrBS12Hj8xUe0tFrxL4oiB9KD2BKHoEdKeZiHFHfgPPBvsaA5po7ggVmuOomppzrVGt9COmBgLNqhb2PIvf2uu6hiMVwrL7bAAvaYjEJERxa3pAHYP7HQMzf2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۷  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82042" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فابریتزیو
رومانو و اهبر رومانو این روزا سرحالن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82041" target="_blank">📅 14:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mThg6Mp1unJKBvE5O7bkjZnBFwS6WBb15opj2bO4xV0oBsnAbIbqFHuPtJrlZkHJi-LOiT-LoTKeufQFvXuBv8z9BK_eUA0QBBkpNeHctewZww9WlrECMKIbHvGBLRSx50sKgPgkTgh51lgGWL5bhHchkj07z6BXtA1wX21UXJf3c7-yu9tUbbU0fovCR08EU48cUN7r8_8wXyUpGU4-uBoZLk4JzJ5ilOe91QIRhpYtJXZgwGoNeSBAWkCW_u8ww18-DSS5tG-jyLwbVRaby5d4W6G3UyDvoHW9n4fvXlnci7hyDF0FkwVHkgEkUrcyp6MecDucT-yE70j6O5Ml4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی ترین رفتار پدر ایرانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82040" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_brzoddLhiv6shm3eo0QltWlYZ3UD0xwCpXBaBiQG9edkhMJFestfRuAgIfkOYJTwT82oLp2CI5g9m_dS56CggoE1gkLmSXELJwtcr7NAvuhrjKarS_33ImBHMhwbsJEXkafrq5TXCS6N8Z83E3wy62nIWdlgnelPELQlwENHFabynHiShYz2fFoJfRFmmr1TayUh4Phva1XLrWyQK-jUvM5v2lJhl6yAecFDzQUVcCdIGF_8WIlOD2f5qJ3yBDj4UJQ777u5hCi4XzIefflbpGbdKaYt7-IBAkKJNMIbh1J15g2L_lcxP_KoJ_WtaCC12Yk43ZRbsYCixJ7lTKgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده خامنه ای در شعام، محسن رضایی: باید برای رفع تحریم ها بریم یه اکانت فیک از ترامپ بسازیم و توش بنویسیم تحریم های ایران برداشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82039" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTgbQKv-TWy8NP7hnsTXGLSVUwESl_fvrdRE0jCWfYsdCG9YaiUGQHFcL6FKeC0VXtkB2W5mnnfpNzMnhHdHnT-E0uPhZv3yIVof3LSc3EVrAd5nMJtS_tN2BvsLs-x1tR53262ABRJxNzsxIAYh4lakznDi9oRXc1JLrYHIvmG1wf34DZ0F_2nETbAUOIQkASWhR14NipPTa6L6j07sUSynidWM2NnqYUEmn9BYM5ktYdx_45i-Wc-KjD-QIwQsRaoIBNulMH0xDmYYHaf7bTvs2ctL3tOCgHJ2KrbZL_vvqXjZ0zoxkk4DUmL2G1LJMqRV8Z5M8wjtH4QZyLHt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فداییو دیس کنید تقصیر اون کصکشه همش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82038" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMrnZU3Io_S5eMdwoYlv8ktso_svD_KbrjUpzmU_81Wt3s5Uo88T0SG7jritn6zMjDviv27TRIIUZZZCE2JlkXgJV7bXI56zoxtRdpDanQjSLhoBbMaqDvUNv-uTGiHnESOfqoKhuDuPTV5FEtRcAq8XjEx87jdfCUJgooXcNA2hslhysf4lWqnXDHeDJ3NZLQa3HemFpKO5IuAUrYp2NhKfh5l1xG0f1BsfDfRqNjL3Tr-IaWRWocVX6Fs_5gumXOSkDhPcHV5Nj8C60bU4KJbhfbpmbetbJvmwJDrGusgJvYaegC03y_j_dRLxb6_vuXPyKddnIvgA-t4knyX3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ راجع به ارزش پول ایران
کپشن: ۵۱ سال بد رفتاری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82037" target="_blank">📅 12:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5yIrXts_Lp0ngczaUqG4vvSAX39NMITsx7vtDw2SGqESpUWyrSrQX4ZQ_dEa9nvzzSAUtJijUXeeHW7RHcYKPpA4iB73jdIA0C1vnPctuJfA2xh3WzJRdXKoO_XAhhhR5fMdNPKOfH3NTA6wsO6RCVFg0YWnPcTtPvWV5WS763LxjLjzIKL4zlizGg9I0X3CKHCExw-IV_9TfsIkj1flxEta8RwsVHkZtcnFuJbwE0R1-k345E7t2X9fdqu6MMttfqr2kSvzGmX-9bw94WGGaekYAmdyYLYVbpIardmWrDByJxKHp8DX2FPnM0bYDOg-Aj1XktiEL-yy7Wk81uS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به همین اسم که تو تصویر میبینید بزودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82036" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnT7coKygm164pdV8TAxgoH-0fSo4FWtBt7LXoOfP_qpi0NeGpCWVN4RJcUI_oC0F3BjAjZ3hSQT48jTlCxt3NPxsw0Ov7USbB-898oIC6bwi8o9d9I3VjjfR9xghcAPgMlA3E_7ANTrNxXCQ1nvWWjA9cVXHqC8dFcF6eeRgtflEw5bNCUkvQI3CDZMne1mveRGHybla30cnEqRfvZ_I3k2voInl3l8PqKBRCiAajDu7DSLxl4wJjPo1SCtAtZutrNLEeRdXGj-cMQvWn7VQ9gphq6HIaZgAIOOBS6ihv-AbO9gY0mL-maUG09GnG5XbqLPJjj_S3LLVR-reNkWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپو میخواستن دوباره تو زمین گلفش ترور کنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82034" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwT8yN60qvNUQyQHP6AF9ZUDVKRcExUNEVPuyop-sM_et81b9oMeKw_Jxb0w18dC9v0xPVEm9rHVE1lRQMlznxFQOwyyPXZMLbL27TPvvB8btdX7pazHz0wns-h0DmeM5dpYGUGkU8-uYg8QsWAFE47XPqF8vQWg85_gK0A-jHoE-che4_tjlaTaV00eSlZ7aU6kr9x2m8IbQ8F2BxqU5EGKJzILmGhRcgHG2knYQypLT_Lo71w7l9daAdkuTKtsiMLCLwDFKo2YgmhthyYq9jWbeXHlG5mSZRzUuDGSQBVb_-PlQCRgZdp8rWaNtkJX_b4K6A_9YrRG8rD6VRz6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5U6KM_oXMcz0Gdf58evpp9QoFhxqWZ9A7M4L8pQBTzUuMYmPeeRVzUeNTW89lg9iMQ9RzoZ354HnTfvGLCl6bVfko_bRa-1Lj0fPXY6ucvzN-NbhKDuz5N9sHwHi8GLSSSGtR7ZBzJCHS4GjvGz4yKfmPtWDSLLJXJ-SZiQYRaVIKXxD72fVMKMdw3mB9IHV5osLU778SZeqIfTeiixpOka7gkxRiCLILm2OHeNstbwOHij6-59oKykv5M3NwjspMJqaxNofOsB6sE83Z5TxOKzjTbdnN-X7KEdPvpnOiXVzu-0E1DPBbaf7W_3ueQIsz5VwSiUIAn0lsYFQq4P1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P60fgXcm7xSHmAQRKNPNo5Vg3pKzAZeJCJ0c9lCUXD74tm8PXnbIN7mMjHvrxRyixsxNfkLZUwVtIgagvCCrSh4JfSzmTVK5ndSzqMy3jdIV2iHIxjU_c70ABBiKjLGyW5mI3r_Cds0JMg7D-vsxjGOPIuUt1oBKVj7E-TtoWKOnhq--pHdx0PZ0HssLgBvh92Ib_dEjnNBpLgkPiA0s1iSexdwkYmaBcNOOa6_BjWh-jmfgqsSxhiYT_w13Mmu9h9XXaUVOo9woe8O2him3qKzAzAcJgovRQe6hayH9P1RTMcIbaLQlaUQOxaruLasz25UbBEN2FOVCT9uf9AYaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=b2TwwUwZ4EcXk24bU54-rfsyVZ1i3n9gXk6AFMt4KPxuKQ2Rb53uAP0E3ETv4PEqsHzRZPx3aHls-EnhbRZPnR0IhOW-5ph-lkzFk326y3UVeWxQOLMFH2KWRaLPARM7kDvOam-eJ8nS-ERKuO6tFXIAcNj_YLRnxqqkzQnelwgX1gAHcB0qcZDIwuSVPNwt_a8yFt1k3mW9ZFeEMGEI6yQXMFCWKFdvyDQgPW1N-cAFbIUhF2v_IvdILaDJ3zqw4UjaQlgl6x0VAyJU6uho78OuD-qjBrTxGPn-cVsb-SdJ4NG-RTPPHQQaTarf6u9V_ZRca7YVKxfVLjFJOAjyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=b2TwwUwZ4EcXk24bU54-rfsyVZ1i3n9gXk6AFMt4KPxuKQ2Rb53uAP0E3ETv4PEqsHzRZPx3aHls-EnhbRZPnR0IhOW-5ph-lkzFk326y3UVeWxQOLMFH2KWRaLPARM7kDvOam-eJ8nS-ERKuO6tFXIAcNj_YLRnxqqkzQnelwgX1gAHcB0qcZDIwuSVPNwt_a8yFt1k3mW9ZFeEMGEI6yQXMFCWKFdvyDQgPW1N-cAFbIUhF2v_IvdILaDJ3zqw4UjaQlgl6x0VAyJU6uho78OuD-qjBrTxGPn-cVsb-SdJ4NG-RTPPHQQaTarf6u9V_ZRca7YVKxfVLjFJOAjyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=PNbO5SOmwU9_h3InDsiItO5bC-uyaEkAZ6-Bd4sKq4LOP2GRhSzWuJKVABIQKrQ9yD-Er8iL6Y93mZTqNwm9aJBpONLr_v-tkBlhNnGBq1WQCNVCCitCAQ7MPhLY7B8WHgF-O2Z8tEajYcRPN01s5mEVzVyF3K6T41dbwsevC5_ryadlhPUFVszVsUx1uDcpMNdakgiky0uJ9V_FpLeT4AmIrsTIaV31z6TvWzySLvpJnXQh1Gk4TQFCMhutZeohDI1aOadDwWQ83o4LN8F2iPfarxxuopsIKNUZ9_4GrvVd25juKUB7b7GHgPhPODrvwJW3oS799Kglp6Gq62EQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=PNbO5SOmwU9_h3InDsiItO5bC-uyaEkAZ6-Bd4sKq4LOP2GRhSzWuJKVABIQKrQ9yD-Er8iL6Y93mZTqNwm9aJBpONLr_v-tkBlhNnGBq1WQCNVCCitCAQ7MPhLY7B8WHgF-O2Z8tEajYcRPN01s5mEVzVyF3K6T41dbwsevC5_ryadlhPUFVszVsUx1uDcpMNdakgiky0uJ9V_FpLeT4AmIrsTIaV31z6TvWzySLvpJnXQh1Gk4TQFCMhutZeohDI1aOadDwWQ83o4LN8F2iPfarxxuopsIKNUZ9_4GrvVd25juKUB7b7GHgPhPODrvwJW3oS799Kglp6Gq62EQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE9X6irpi9vhSNSVUz1_7VyTeH0FVAAOVqu3Vm0n4_jwws15jpVBxC8HlZgrVztG10kIz66WlFLG6UIaSHm8P1J5W22r-UlAe1RqGTQH3JF3lIExg6p67YdpBcNakm4aC2daY7_WdGz16JxYBfhs5sWt8zKpbD0diGdy6wUqBNe-R1EI-ZJzzK3MzqLImfwtj3zqNVEpkAXIoxQKZ3U9SdNv7i_91BkAmwXzU2BYq6LugkSbYmy_I2hb6tAgUISurQs3KHj_xFEGXs0HKpcpLsqcndPjHXZGJn5iBYc6T4xNuQL0dWYDV2SmBL3ma1nqObUdk9xQiTLyAnVBNPBMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2b2aW7DBRd2G3Igdij5_moKSEUzLPBcBS-G7lZ6kELrdB35T85EKB-JtvdffuRzW2dnVmOr6Ubx1Vdp1GrFumbdtmkzQCVx85jXgN3KNN54w2ZXva_kesoXlkoK_PN2XuHEv5QN2BYSEci6nKEpguwN4uvEmUeJX3JZaVVngCeTbNnvDotVHJpn41WfYBYG_J1cSqxvp6Az5iJZP35r_qfhQlNk8NhmwwTI1kwoc4UVOFgiJzyA2Hn3oewtH2lnm2UmvLA3vu0cZVgFtdHKC13nn5dmP1bcpGtyFfdTxGtJGSfy-pLrG8P0irBV3Ex_ZScegNH1gtKp6bIZidbfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXQYAzxBmANIfJD0C9giWpIAiFLktzJlo66h5BZ2kuIByuCJ_D0hkRSSAUa_7kB2CtPozQElMt8mO-bcZglA6OC7DnkDxW25wPOOQ_8p9_L32UCoq7PVv6YZNQ0GvxdAIp5IgFiQDQrHKjDJQEhFx12HtvRekvZ1dL0RpUICowJjWPqVQ0qXpYk0s3xQW3w862p_eWXCBz67xUsm_KprGR4pv2jifeOC1ZZwtcGjZsR35SY3gJZH7c1Y7YKvxQihnZXBc5i_eD6gmQPBbrngnX63ub6iWt6SDAa2d5Dnpe7ARLNa1LMZWrEsr-nHP3tc--ga6Dti7Cjxy7T0xUIcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HACAtXANZ1EAjR6zKKOmBFA7ukQPy1xODul-jGFmwdipB3xrT5PHVQpj20nuV9lCeRTcVM0jkwUnTWFnMnpW83t2GKtrI1lO5MO5SzH_0Yec6Tu2cU93XDjNWwKfiIf0tUJ77EQb7RtRVMpmeRlp_CmF8I4Uw4JHzT-54KdN-oGdX20cpD50pEYKn9MLy2PBUp8fh1EGwSlw3EfvCWixG2bAdi0hurA4eAcnwPsyuhhM9rn95v9fYE0tMjYK-DLdDsG-J8APOVLLO8KXhTyJt1kBtA02WmEX2--ZZuJWGbPFoBCzh3EgNUy2eoGpmn3dd2VZAH1biUqucd6W3BMsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiYPVWy8uznv_BM_BmOV8BErei67nQcI-inHVLdufIbx3WhvN3Y_yRukupZAoy2QFv0UiBcMABazW65dIfpCCXgpcdFRSra2x3mJUv037WkWQnmOuYYq0b8xkwXSyw6H2HGAWKxfT6DBW65wzQ7SNxCbD1EYwN6YsEnAFex0dc9EaUwPbXdUiYrW6Gc_uT7ci7SoHxS6aHIOnkaT0Tr4kCqtrph6bIpIbPs14RWnqtoxDEr4La6nYOXre_QsTNhqLI8kbpo9GAKKN59uzedUTaK7ShHPmaX_zNfTWWUZ0iMfSejUPz8v9Y3A_bU2-ebiWVhnyRSuqPNUPxulmMODug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=AWTJ09FUM8XkebynM8564FgdI7qhIaIilyFJaLtH1ZN6wf-xKTxPYK5Whu31ueBHvSrloCTBghqw5ZhDPEYIaypAM1Px9gPswmJFTrfiopcXmKsdSTUFBOXvj5B1kdJRQj8t316WDsbGvcKIUV2k-GZOAdYlh8XRIDMVL6cwcqm78HDoR8lfeFUszntcg7j97kWWjiMmGbutsmr2W4gqQ8Hy_KlmOofSbaURo3gOw2dN6jvTqXxw8kMCKjqRzWz3ZP_V1KlLWR_QHHZM_6feRJPZSqBtLebcv7C0D3_htYiWmZ_pRGa2b54Hs4OJXnMQ-RX9XKZCawNOL27DrRqJvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=AWTJ09FUM8XkebynM8564FgdI7qhIaIilyFJaLtH1ZN6wf-xKTxPYK5Whu31ueBHvSrloCTBghqw5ZhDPEYIaypAM1Px9gPswmJFTrfiopcXmKsdSTUFBOXvj5B1kdJRQj8t316WDsbGvcKIUV2k-GZOAdYlh8XRIDMVL6cwcqm78HDoR8lfeFUszntcg7j97kWWjiMmGbutsmr2W4gqQ8Hy_KlmOofSbaURo3gOw2dN6jvTqXxw8kMCKjqRzWz3ZP_V1KlLWR_QHHZM_6feRJPZSqBtLebcv7C0D3_htYiWmZ_pRGa2b54Hs4OJXnMQ-RX9XKZCawNOL27DrRqJvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvFrMx8RvRSOCd9Tps6-sByvvFvkRQNE8SKtkNCOWxC6eG23qeICSydu8jDFYK8Ev6eysJqinWGmnaQQsUh_aSrXW3NOxmw4A61qG97MfQmJDu-r-dY-qsNytCODNwHl625AZ2tOWWHFnz1YXpuClzHL2Oy14VET2XMPWqEV7SgGT_KJI1R1M5L-H3N7XKKPXKcUBqKoawSj0NkzwnHzycwwd29ba4HEpCmsLWRV_mlsbBhz1u59W4e8013IEu0eDsDYgijTTRXC2EWE4ameX8UVXdbtk7gkJB24sePJN8CG0DibMwD9gqLzcp_KjQmGdXGGzqFr1qidEhqOSZPCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
