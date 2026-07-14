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
<img src="https://cdn4.telesco.pe/file/evxyKxp_Rdk8RQ7MVdv85MZb9QEASaCZxHR7ZcisCvwiTlfRXr068rKazIzXPxCtu4rVH5RI_rOz9uFCiPuFNXBjee-2pyljm6EQnJ_FB-pVWD8vDBLbP7TouIRRAjz1JaRECXyvwl2lsVybPLkCM80QnLGLIur3h6e-ki7fSP0jAbD2kS-F66iajV5tTdylyX7-wqjLmdhYfP2AnXc3ABi7fm2mnNK4QY2eNXZnqnnZ4g5Jbl9kIptPYPjxm0pJuKhRVhIyVmTYEPu7-86F0g8-Bx52V2YzHxO3UatHZgG3zGH5OIAEf7qNWh1iNQHevKI7HcFTQ0aOGUu4hWU6cQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-135762">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان…</div>
<div class="tg-footer">👁️ 121 · <a href="https://telegram.me/SorkhTimes/135762" target="_blank">📅 16:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135761">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
عضو هیات مدیره باشگاه پرسپولیس استعفا داد
🔴
علیرضا اردوبادی عضو هیات مدیره باشگاه پرسپولیس، از سمت خود کناره گیری کرد.
🔴
علیرضا اردوبادی در ۱۸ آبان ۱۴۰۴ به عنوان جانشین سیامک جلوه به عنوان عضو جدید هیات مدیره باشگاه پرسپولیس انتخاب شد و بعد از اینکه پیمان حدادی به عنوان مدیرعامل باشگاه پرسپولیس معرفی گردید؛ از سوی باشگاه به عنوان رئیس هیات مدیره سرخ‌پوشان معرفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 452 · <a href="https://telegram.me/SorkhTimes/135761" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135760">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6WXLAxQ-qW8oj9wTs0sOLfkMWZx5IsS1Czx-5Dn2Fv34kxx_mYyKNrKm5YqiXOoCyUU75-4HKaS76EPHq6wBsmdlVGScdeu68YxacNxWDhB7HiduR19RKWGjDPeCR3p71dxIKj38hqE1MH5ZfHCBRH0nDUC_8lu4OV_zHpRKsKAI7TlQmH4I_ZTSjpXoseRHq_tUa7Zr4Elp8LyaXaBY2A6FspR_wZJm1Htj52sBsdTUyj4rDATKEVHixyKNjoDA4lVmVeyp3rEXZhEz_KGCLtKfY1YcrW5V83fKU0yVkLo4Cx4pK9TgIaSuSvMceeyAPZ6EOQpQOo_N0OSAH4TaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
❤️
فوووووووری
پرسپولیس دارک تا دقایقی دیگه از ستاره استقلال که خواهان حضور در پرسپولیسه رونمایی میکنه
🔹
👇
🔹
@PersDark
🔹
🔹
@PersDark
🔹</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://telegram.me/SorkhTimes/135760" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135759">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
تسنیم : رضا جباری با مسئولان باشگاه پرسپولیس جلسه داشته که ؛دو طرف در این جلسه به توافق نهایی دست یافته‌اند و گفته می‌شود جباری به زودی در تمرینات پرسپولیس حضور پیدا می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://telegram.me/SorkhTimes/135759" target="_blank">📅 15:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135758">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
🎙
علیرضا جهانبخش: می‌دونم که بین پرسپولیس و استقلال لباس کدوم تیم رو می‌پوشم اما الان نمیگم. پدر و مادرم طرفدار یه تیم هستن و هرجا اونا بگن، میرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://telegram.me/SorkhTimes/135758" target="_blank">📅 15:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
فوری :پرسپولیس برای جذب رضا غندی پور اقدام کرد /خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://telegram.me/SorkhTimes/135757" target="_blank">📅 15:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vypdYjnh6gHRQunoemVqlSNFYGrqUgBgE7SfxAYjWfZIyn3H45X71snrWlmqBQoMGQLQzUh31q9WvNIVeIjfrLkv4Im4qlRbOHFaP6jYhKB5Tw02naCdFc0SgZXCXyjT4JsSItSRLx8z2o79wRVTQr0MF-MfADLuKDhvdMpKWpc12_zh03LB2d6dLuhRQL7kB418L2_J7s9Tm8uMeI8KskgeU4j2UYs2ElvcEekhH-1dRhvj-96cihPBPIj9OYhfufX__GseS6w8DGVM8NsXE_fj5_cy3XWK11WPBxbvo_33dSYZdYvPRySAbkDjItEAUqA1IJZ5U43kgQbA4ZOgng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی رسانه عادل فردوسی‌پور از امیرقلعه‌نویی: سرمربی تیم‌ملی قبل از بازی با نیوزیلند تهدید به استعفا کرده و فدراسیون با پرداخت ۱۴۰ میلیارد تومان پاداش به این سرمربی در یک بانک‌خصوصی، قلعه‌نویی رو راضی به ادامه حضور در جام‌جهانی کرده! حالا هیئت رئیسه فدراسیون از رفتار قلعه‌نویی حسابی شاکی شده و قصد داره این مربی رو برکنار کنه مگر اینکه تاج مانع بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://telegram.me/SorkhTimes/135756" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🚨
قرارداد میلاد محمدی با پرسپولیس تمدید شد/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://telegram.me/SorkhTimes/135755" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
ورزش سه :
🔴
بالاخره پرسپولیس و میلاد محمدی  روی برخی نقاط به اشتراک رسیده‌اند و به این ترتیب احتمال دارد در روزها و حتی شاید ساعات آینده قرارداد مدافع چپ ملی‌پوش پرسپولیس تمدید شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://telegram.me/SorkhTimes/135754" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
تاخیر ۷ تا ۱۰ روزه لیگ ۲۶؛ فصل جدید فوتبال اواخر مرداد شروع می‌شود
🔴
🔴
براساس اعلام سازمان لیگ، در شرایطی که قرار بود فصل جدید لیگ برتر فوتبال از ۱۶ مرداد شروع شود، این مسابقات با تأخیر  یک هفته‌ تا ۱۰ روزه از ۲۶ یا ۲۷ مرداد شروع می‌شود. گفته می‌شود علت…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://telegram.me/SorkhTimes/135753" target="_blank">📅 14:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gohFdMI2dljCqauTnmDP22tZQz1tMWmskOW98Rh4tkiizighceT6kyFLsuMoKkW0azycpO8Z4GEfyIuGmx2nZ8OkWcHUQi7bd6PfJLH4N_3pQpoQ4xC8Vpno159kUo1ob16-DbhVIzjuewILQQVqeKdzuRRk3j-tGGBTbdJ1rR_Wv3ijmqH46R_exEpX-O7EBEYfCWtBSU3dOIsJzqimrC92nY40LtDeiQdWSM0v52RgjqHjqVVdwsSlUbi-BvH1c2P6GKeP1tv5SE-35Up0S7r0j_MCG_BSl3NI0rgXs7eB1VjVj5kEQAXAVN4ucSlrCdVwxlHeHs314nCWOeWc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://telegram.me/SorkhTimes/135752" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
میلاد محمدی نتونست تیمی از اروپا پیدا کنه و احتمال زیاد تمدید میکنه / طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://telegram.me/SorkhTimes/135751" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🟡
علی کریمی با عقد قراردادی رسمی به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://telegram.me/SorkhTimes/135750" target="_blank">📅 13:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
✅
فوری؛ با اعلام سازمان لیگ، برگزاری لیگ برتر در اواسط مردادماه لغو شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://telegram.me/SorkhTimes/135749" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
کسری طاهری مهاجم جدید نساجی: من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://telegram.me/SorkhTimes/135748" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
تایید شد بازم
🚨
🚨
🚨
فوووووووووووری :
🔴
کسرا طاهری: قراردادم با پرسپولیس فردا رسمی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://telegram.me/SorkhTimes/135747" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
💢
احتمالا علیرضا جهانبخش جانشین امید عالیشاه در پرسپولیس می شود!
🚨
جهانبخش جدا از عنوان یک بازیکن برای پرسپولیس قرار است سفیر تبلیغاتی بانک شهر هم باشه و پول خیلی خوبی قراره بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://telegram.me/SorkhTimes/135746" target="_blank">📅 12:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
امشب ساعت 21
🔴
شنیده‌میشود؛ باشگاه‌پرسپولیس امشب از پوریا شهر آبادی و ابوالفضل جلالی دوخرید جدید خود در ویژه برنامه‌تلویزیون این‌باشگاه رونمایی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://telegram.me/SorkhTimes/135745" target="_blank">📅 12:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGYaLuVq4rH7811jn2yenE6iL1DhARYB17rzf9LuUsjKjfy7sMy792kPfkp_EloDEYHuMk8s4kkjbgdxWNSeh6hACdHasyH0yfdIoWK5eO2hpc_Yljv1xrWM-qPhPPeTEbn15w6zfzVtiEAgZj0EfXWbF-iL37wyDcD8Lk6lZrOcnh4mIVAFvyOKPVHc7UHDK4j2i2rtt96RUzUG3REb8lEdOjp8Kh9xg_PHKmCxRE3BxB1oiQWtfVxJ3iaU93L3LzNpZqn5vEVN49TdkluS6NnPqgUL2efY5t-oP4ggwbk4Qgnde7lW6rYH0rjKaEVcU7VThuzrqYvxnwqD_4AqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://telegram.me/SorkhTimes/135744" target="_blank">📅 12:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
جذب ایری برای پرسپولیس در یک صورت ممکنه که نساجی بدون دریافت یک ریال این بازیکن و به پرسپولیس قرض بده که احتمالش صفره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://telegram.me/SorkhTimes/135743" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936ce7543f.mp4?token=P0IiJ9N2IPTblql1lwn1rsXRs4KuBSOMVxc3vswV6-IKOtmgipjEDxhwBWD-YJfsgwezh0U0i9no336AOM7eWnCnmQLcXfYee39ggoZl5-n-G5wEfgZOkrKTdDl5Uhze5yN5H_ggdrmWgHpEIIaol0bJsnMjHzjoyhI-3kut8IqP1J-QXYu7IJgKCLkizfYzHSbH7WAjVpRrjcYQkEnfZ-dg8JYVoLqVZEunAaKZoSVtK_9Wj0a6CR5tfZvvKwFE7E_zYOInSko37qgN-B0S8xr1kraKsxSF28Wunf28heNURu1ju5wHiAq99myVuoqTuLuS0_P4ftQMUX2Ix94QHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936ce7543f.mp4?token=P0IiJ9N2IPTblql1lwn1rsXRs4KuBSOMVxc3vswV6-IKOtmgipjEDxhwBWD-YJfsgwezh0U0i9no336AOM7eWnCnmQLcXfYee39ggoZl5-n-G5wEfgZOkrKTdDl5Uhze5yN5H_ggdrmWgHpEIIaol0bJsnMjHzjoyhI-3kut8IqP1J-QXYu7IJgKCLkizfYzHSbH7WAjVpRrjcYQkEnfZ-dg8JYVoLqVZEunAaKZoSVtK_9Wj0a6CR5tfZvvKwFE7E_zYOInSko37qgN-B0S8xr1kraKsxSF28Wunf28heNURu1ju5wHiAq99myVuoqTuLuS0_P4ftQMUX2Ix94QHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برای طارمی چیکار کردی ؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://telegram.me/SorkhTimes/135742" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://telegram.me/SorkhTimes/135741" target="_blank">📅 12:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
👀
شایعات: حدادی امروز با علیرضا جهانبخش جلسه داره!
❗️
❗️
پ.ن: طبق گفته خود جهانبخش مقصد آیندش تا ۲ هفته آینده مشخص میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://telegram.me/SorkhTimes/135740" target="_blank">📅 11:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyGSsu4la66WDE7_qMFJcKLFDe79xHRyZvmwToqlPCCDPSPbyHCKvztBRV6rMevt1sPa42d_1xPMicgeNM1AjlPz8mg-fGvPIo88KgEbp2ETvyVluceMDjM_Aut9A1H8nBKBsLF3FMX17OEyfmjOF2ZIuLYWFqtEjzwL2k_SXiAFLR0FUfRmXeXv4HVEo3zta_tNWUPvEpVbtTJWecrodu2eqCNCZLnzrTF9ko1LjBVGnzPVF18Wolzto4FCxmLqiXzRqxp58FOIBDsEhlwxkmR7EehWUU9iEVqSIbkYb2DlBDDcQuTNtRaTx1Co4k0r93lYUXJiubMwioxX2xGQgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
شایعات: حدادی امروز با علیرضا جهانبخش جلسه داره!
❗️
❗️
پ.ن: طبق گفته خود جهانبخش مقصد آیندش تا ۲ هفته آینده مشخص میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://telegram.me/SorkhTimes/135739" target="_blank">📅 11:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://telegram.me/SorkhTimes/135738" target="_blank">📅 11:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135737">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=B0brPKXs2sMRo_jDqhmfvIrD4GwkytvhjpGPDJNYcnt7-q15fsrsNTb4DbDdYjR1QltMyAnms2WGTIz7GyAjoMlIdpIddqiF3OKdDxhA0Q9zMxhTu8mNJ7evD6nne-9D60GahoBKxKcl3cnFlH21428yo0o4zzKm33oWd7gO--UdmirAEuod6OrGPj0-TzEUh1uSj55DbPTsvs3VYPqR5A2Ne2FZ7kGAx8psdhnQbvfmdOh44xWFJKiVjnRTYchJjZMVpCyc-wA7ph9ytnNfmCjca48WHjzN3zWOGU8hl-rpzYj8L9kQlY5jx2WYeX6pbOpvb4c4wDLUOOTUoaGyeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=B0brPKXs2sMRo_jDqhmfvIrD4GwkytvhjpGPDJNYcnt7-q15fsrsNTb4DbDdYjR1QltMyAnms2WGTIz7GyAjoMlIdpIddqiF3OKdDxhA0Q9zMxhTu8mNJ7evD6nne-9D60GahoBKxKcl3cnFlH21428yo0o4zzKm33oWd7gO--UdmirAEuod6OrGPj0-TzEUh1uSj55DbPTsvs3VYPqR5A2Ne2FZ7kGAx8psdhnQbvfmdOh44xWFJKiVjnRTYchJjZMVpCyc-wA7ph9ytnNfmCjca48WHjzN3zWOGU8hl-rpzYj8L9kQlY5jx2WYeX6pbOpvb4c4wDLUOOTUoaGyeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://telegram.me/SorkhTimes/135737" target="_blank">📅 10:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135736">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
فرشید حقیری :
🔴
احمدنور امشب با احمدی مدیرعامل بانک شهر داخل‌ تهران جلسه داشته .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://telegram.me/SorkhTimes/135736" target="_blank">📅 10:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135735">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
استوری جدید فرشید حقیری در مورد احمد نور: قراره شده احمد خودش بره رضایت نامه بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://telegram.me/SorkhTimes/135735" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1608df5b.mp4?token=IAP5AHluoaxiL5KAad7KmGK8waZrDkliSv8rdz9KfkfPN3pstSzS-3gf5a5WpOsr30EfVPTxIv8g6WXlmJ0IiFqdVGn4UaFEitzlLPyySKwczuWP24sqLxoZfx84nO9QBiEEM0uDxp4nc7whdq87vTOKRvnS9g1RQNZ3-lWqhagM4je8RUTMAOTEzjOI7IaHCQ2abiCk8c9y8tKvucEd2hxjGpPQMYNp7XIuoa9vP3dD3PXrHl2hgUoTA-k8TO-eYLbGO0XYxOkDiL3O8rn0QAohOtP6LVMUv7BOYKBc5n2L5jTubLX3LSrbT1JdN_w1i9wk4e1Je39sEODe8PhYuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1608df5b.mp4?token=IAP5AHluoaxiL5KAad7KmGK8waZrDkliSv8rdz9KfkfPN3pstSzS-3gf5a5WpOsr30EfVPTxIv8g6WXlmJ0IiFqdVGn4UaFEitzlLPyySKwczuWP24sqLxoZfx84nO9QBiEEM0uDxp4nc7whdq87vTOKRvnS9g1RQNZ3-lWqhagM4je8RUTMAOTEzjOI7IaHCQ2abiCk8c9y8tKvucEd2hxjGpPQMYNp7XIuoa9vP3dD3PXrHl2hgUoTA-k8TO-eYLbGO0XYxOkDiL3O8rn0QAohOtP6LVMUv7BOYKBc5n2L5jTubLX3LSrbT1JdN_w1i9wk4e1Je39sEODe8PhYuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمن ورزشگاه آزادی جمع آوری شد. پس از پاکسازی زمین و ضد عفونی ‌کردن آن، تازه کار اصلی آغاز خواهد شد. یه چند ماهی نمیشه ازش استفاده کرد 1 سال گذشته و اینا فقط دارن بازسازی میکنن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://telegram.me/SorkhTimes/135734" target="_blank">📅 10:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📸
تارتار در بازی دوستانه امروز به همه بازیکنان فرصت بازی داده حتی وحید امیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://telegram.me/SorkhTimes/135733" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
فرشید حقیری :
🔴
احمدنور امشب با احمدی مدیرعامل بانک شهر داخل‌ تهران جلسه داشته .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://telegram.me/SorkhTimes/135732" target="_blank">📅 09:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
جهانبخش :با تیم های پرطرفدار تهرانی صحبت کردم و شاید امسال برگردم ایران ...دارم فکر میکنم ..نمیگم کدوم تیمه .....ولی احتمالش زیاده بیام ایران چون می‌خوام بازی کنم   پ.ن یعنی میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://telegram.me/SorkhTimes/135731" target="_blank">📅 09:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyFF1N5rKRB4Mj-7DnDXc95oEGWCqQ9VfGfh7D2y2yIjqdmU92Uo6FXivFR4eDKiepdzEC0--Q8ovO9GDus65BR82OiPmhg2pip4HFiLs4IacC_smjsa-u_L4zezOSpp3MKvLfB_tIPTw50XkfBs0757Q6XACscswV-ERI-IuLEjAEwwtoL4vyz_TbZ6zjMhmAtpdx9XBKUg95GKJYFJkcvwWl8ZB-hZp_qsTFIXD36bqg5vs36MskOMb01UeAFyfL47PiovIzIGhQ5XLIcWgh7wfivAJ5NuPjeySUH_OYHGeP320qZGyyLkVdYlodiZmQp5XUm_9dJgCMc8IvhrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://telegram.me/SorkhTimes/135730" target="_blank">📅 08:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
ظرفیت باقی‌مانده: فقط ۴۷ نفر!
فرم میکس ضریب بالای بازی‌های امشب جام جهانی بالاخره آپلود شد. روی پیام ریپلای‌شده بزن، عضو شو و فرم رو دانلود کن تا بازی‌ها شروع نشدن
👇
👇
https://t.me/+ThBeycRt0x1lZWU0</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://telegram.me/SorkhTimes/135729" target="_blank">📅 02:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOELz1rFXOjo9ynDz4WyFAon8uWj9O5MJtLUfr9EsvfsUdsq-F9SthaVLJAnZpuoDZBTRwSAFkX2F44jV0Q5fvx7Cqxy1VJYoINQdfn5W74NJp--YCdUx0kf8WnYM0_8k_KFB7qnPW-WmNB-jU6GnqYLGiq81XVPpz1pV55WaMbU9uBcQc6nZk2_Kk4a9LrxQPA49JRIwmizwO3nxVuYPjPojTQvjMAqIeShFDQwTt8SO4121vPX3Elq5eceLrcvAcouPSyrCFHFtj3Q33DzCC9Gl5AHrXsJD3m8jBKZcWwATCIU_3qzhpKiGWmcxXSqzLFgI0WZOyH8UG9jcMB-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ رو به کیف پولت وصل کن!
💸
دلت می‌خواد بازی‌های جام جهانی رو تماشا کنی و هم‌زمان ازش درآمد داشته باشی؟
دیگه نیازی نیست شانسی شرط‌بندی کنی و سرمایه‌ات رو هدر بدی!
توی کانال ما هر روز:
✅
آنالیز دقیق و کاملاً رایگان تک‌تک بازی‌های جام جهانی
✅
معرفی گزینه‌های امن (تعداد گل‌ها، کرنرها و کارت‌ها) با ریسک پایین
✅
فرم‌های میکس پیشنهادی با ضرایب جذاب
📊
میانگین وین‌ریت (نرخ برد) ما در ماه گذشته: بالای ۸۲٪
فرم بازی‌های امشب آماده شده و به صورت رایگان توی کانال قرار گرفت. روی لینک زیر بزن و فرم امشب رو بردار
👇
👇
🔗
https://t.me/+ThBeycRt0x1lZWU0</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://telegram.me/SorkhTimes/135728" target="_blank">📅 02:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://telegram.me/SorkhTimes/135727" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://telegram.me/SorkhTimes/135726" target="_blank">📅 00:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
خبری تکان‌دهنده برای همه باشگاه‌های جهان؛ علیرضا جهانبخش بازیکن آزاد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://telegram.me/SorkhTimes/135725" target="_blank">📅 00:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135724">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
دنیل گرا و ایگور سرگیف دو بازیکن خارجی پرسپولیس به تمرینات این تیم برگشتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://telegram.me/SorkhTimes/135724" target="_blank">📅 00:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
🚨
🇺🇸
مجری: به نظرت وقت این رسیده که مردم ایران دوباره بیان بیرون؟
❌
ترامپ: نه! اونا اسلحه ندارن و هر چقدرم بیان بیرون باز کشته میشن، رژیم بالای ساختمون ها تک تیرانداز می‌ذاره و با اسلحه مردم رو به قتل می‌رسونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://telegram.me/SorkhTimes/135723" target="_blank">📅 00:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135722">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
☹️
ترامپ:امشب، تأسیسات هسته‌ای ایران را در کوه "فأس" (کرکس) نابود خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://telegram.me/SorkhTimes/135722" target="_blank">📅 00:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135721">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
☹️
ترامپ: عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://telegram.me/SorkhTimes/135721" target="_blank">📅 00:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135720">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
اوستون اورونوف چهارشنبه‌ وارد ایران خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://telegram.me/SorkhTimes/135720" target="_blank">📅 00:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135719">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
ترامپ : امشب و فردا، ایران را با قدرت مورد حمله قرار خواهیم داد، توافق‌نامه همکاری با ایران یک آزمون بود، و ایران در انجام تعهدات خود در این توافق‌نامه شکست خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://telegram.me/SorkhTimes/135719" target="_blank">📅 23:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135718">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
فوری / نیویورک تایمز با استناد به نامه‌ای که بررسی کرده است: ترامپ رسماً کنگره را از شروع مجدد جنگ در ایران مطلع کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://telegram.me/SorkhTimes/135718" target="_blank">📅 23:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135717">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://telegram.me/SorkhTimes/135717" target="_blank">📅 23:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNfSwT1C99bmshILkYZXi573Zt52bevMdInEMjfBKVGwX0Tqa9Dta7YeX4-eiOnANqWoGl7fMFoui4oUt8ZOEcfI4z1-pL_drmZdfXK5OXxtzAyzTK9Y9tKDtgiqbPHM_fqezEczPKUbhBKl5VOsd3g-2mRuhEYYAxDQ-wrGrCUmyQnZ8L4NEVNJcmvkx0dcBdf_b7it2LrhwQvlq20MEP162I48vrkyZ1CvBEwGBu4sQGv_BCK9zi9zzfX6M7wVSQIrrbc4F1nFaSMe4h6lwV9GthuIOd3XPBDgkm-XGCrRWVbFq0g9kg6qck6xoiH2bTp1E1Uud6sdGagBr2lsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
فوری از فرهیختگان: قرارداد پورعلی امشب نهایی می‌شه و از فردا به تمرینات تیم اضافه می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://telegram.me/SorkhTimes/135716" target="_blank">📅 23:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://telegram.me/SorkhTimes/135715" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135714">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🔴
🔴
میساکی: اسکوچیچ سرمربی فصل بعد پرسپولیس است
🔴
قرارداد اسکوچیچ با پرسپولیس ۲ ساله است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://telegram.me/SorkhTimes/135714" target="_blank">📅 23:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
باشگاه پرسپولیس با تصمیم مهدی تارتار به دنبال خرید مهدی ترابی است. اگرچه ترانسفر مارکت این بازیکن را آزاد و بدون قرارداد اعلام کرده اما باشگاه تراکتور با اطمینان اعلام می‌کند که او قرارداد طولانی مدتی با این باشگاه دارد.
✍
ورزش سه
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://telegram.me/SorkhTimes/135713" target="_blank">📅 23:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://telegram.me/SorkhTimes/135712" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToC7mSr3DsOs0ppwYbdoQRUfj2K1kLRLWIknQegDMaUiJaGwIKcSTdRbOGEUmUk3kW4q4X5hr_T9HFzOFcn7VZF3Ns14NFHvjkQeZZD_Hvx0np1on2tB4b1jTsO6AbMHOc8TY8foPIWwCjL3yEM70iFC5WUNoYvwTzylbw3aKQ41R8jxlOiXyTMDpOgut8PTep2ugsG3pOXX55PXotHqnkFenGlyBFW0NdQFkZQMgKqD68kFxKZqP4RaIiXbMMuR2r582GO6UMRKs6NcdDi7AlNKjIJiacYzL2AhsZtca7sbRW3Ir-jClx1qA61wLejPkdmbLaXehErMlgZbX3vYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تارتار در بازی دوستانه امروز به همه بازیکنان فرصت بازی داده حتی وحید امیری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://telegram.me/SorkhTimes/135711" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
احتمالأ پوریا پورعلی امشب رونمایی میشه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://telegram.me/SorkhTimes/135710" target="_blank">📅 22:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://telegram.me/SorkhTimes/135709" target="_blank">📅 21:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://telegram.me/SorkhTimes/135708" target="_blank">📅 21:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
#فوری | نیروی دریایی آمریکا اعلام کرد که محاصره تمامی بنادر ایران از فردا، در ساعت ۲۰:۰۰ به وقت گرینویچ آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://telegram.me/SorkhTimes/135707" target="_blank">📅 21:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
فوری ترامپ:
❌
امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://telegram.me/SorkhTimes/135706" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
علی علیپور و میلاد محمدی امروز هم برای تمدید قرارداد خبری به باشگاه پرسپولیس ندادن. پیمان حدادی دیشب گفت که این دو بازیکن فقط تا امروز وقت دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://telegram.me/SorkhTimes/135705" target="_blank">📅 21:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://telegram.me/SorkhTimes/135704" target="_blank">📅 21:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
ترانسفر مارکت: رضا شکاری از پرسپولیس جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://telegram.me/SorkhTimes/135703" target="_blank">📅 21:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
پایان بازی، برتری در دیدار دوستانه
🔴
پرسپولیس 3 _ 0 شهدای رزکان البرز
✅
عمری، تیکدری، میرشفیعیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://telegram.me/SorkhTimes/135702" target="_blank">📅 20:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔽
پورعلی داره می‌ره باشگاه برای معارفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://telegram.me/SorkhTimes/135701" target="_blank">📅 20:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
🔴
🔴
🔴
🔴</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://telegram.me/SorkhTimes/135700" target="_blank">📅 20:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
🔴
🔴
🔴
🔴</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://telegram.me/SorkhTimes/135699" target="_blank">📅 20:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://telegram.me/SorkhTimes/135698" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrZV0G2IciBQmImSOua15xfkQOYNHkkEYfjOrf52LhQuaExl1HdtQTCpZVcrapgh0fHl9NewnBqm8mFGvKL5y-1qC8eA029QxqmgoJ9cJQNO2_E4HHCzZwhoHYxmYPXcRXnCWP7unTLRFKxMq8z3qudQBOTr7YiYintEJqhhb-D7Ygs7vIg5GdraofuUBP1CmBWSc_wbMXXyiRyKBpP3tMSnEVdX9e3fs_vcHyGT14bMfLgEvK7j3r0Zhg3S6LgOpk5N7S6SAxGD6l8CwPj9SDcHu0NtQqWYcDwKqsxI8jR3AWWecrCsHJel0SqjtpDtPEeMinEWcXjnDXCh2qFDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از بازی اول نیمه نهایی
🏆
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
باضریب
⬅️
4.38
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+wuaT6FTz8iViNmU0
◀️
https://t.me/+wuaT6FTz8iViNmU0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://telegram.me/SorkhTimes/135697" target="_blank">📅 20:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚽️
👤
سوپرگل سامان قدوس به عجمان در جریان بازی اتحاد کلبا و عجمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://telegram.me/SorkhTimes/135696" target="_blank">📅 20:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
فوری؛ قرارداد رضا غندی پور با شباب الاهلی با توافق دو طرفه فسخ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://telegram.me/SorkhTimes/135695" target="_blank">📅 20:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
پایان نیمه اول با برتری ۲ بر صفر
❌
گلزنان: محمد عمری، مهدی تیکدری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://telegram.me/SorkhTimes/135694" target="_blank">📅 20:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
🚨
#فوری | ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://telegram.me/SorkhTimes/135693" target="_blank">📅 19:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
❗️
قرمز آنلاین: با تاکید و پافشاری تارتار آقا کریم موندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://telegram.me/SorkhTimes/135692" target="_blank">📅 19:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
یاسر آسانی قرارداد شو با استقلال فسخ و ایران رو ترک کرد / فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://telegram.me/SorkhTimes/135691" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گل اول پرسپولیس توسط محمد عمری
⬇️
⬇️
⬇️
https://t.me/+sCs-XrTYp8ZlN2Zk
https://t.me/+sCs-XrTYp8ZlN2Zk</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://telegram.me/SorkhTimes/135690" target="_blank">📅 19:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
ترکیب پرسپولیس تو بازی دوستانه امروز
▪️
پیام نیازمند
▪️
حسین ابرقویی
▪️
حسین کنعانی
▪️
ابوالفضل جلالی
▪️
مجید عیدی
▪️
محمد خدابنده‌لو
▪️
مارکو باکیچ
▪️
مهدی تیکدری
▪️
محمد عمری
▪️
امیرحسین محمودی
▪️
محمد امین کاظمیان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://telegram.me/SorkhTimes/135689" target="_blank">📅 19:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
نخستین بازی سرخپوشان برای فصل جدید
🔴
تیم فوتبال پرسپولیس در نخستین بازی دوستانه خود برای فصل جدید فوتبال در دیداری دوستانه به میدان خواهد رفت.
🔴
به گزارش سایت رسمی باشگاه پرسپولیس، سرخپوشان ایران، فردا(دوشنبه) برای نخستین بار و در دیداری تدارکاتی با هدایت…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://telegram.me/SorkhTimes/135688" target="_blank">📅 18:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://telegram.me/SorkhTimes/135687" target="_blank">📅 17:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://telegram.me/SorkhTimes/135686" target="_blank">📅 17:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
قدوسی: مذاکرات با احمد نوراللهی در حال انجام است و مدیران باشگاه در تلاش هستند این بازیکن رو به پرسپولیس برگردونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://telegram.me/SorkhTimes/135685" target="_blank">📅 17:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://telegram.me/SorkhTimes/135684" target="_blank">📅 17:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://telegram.me/SorkhTimes/135683" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
پیمان حدادی : ما به میلاد محمدی پیشنهادمونو دادیم فردا آخرین فرصته که قرارداد رو امضا کنه اگه نکنه از لیست تیم خارج میشه این پرسپولیسه که واس بازیکن تعیین تکلیف میکنه نه بالعکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://telegram.me/SorkhTimes/135682" target="_blank">📅 16:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
عجب بابا عجب
😐
🚨
🚨
🚨
تسنیم: باشگاه نساجی مازندران رضایت نامه دانیال ایری رو گرون کرده و به ۱۹۰ میلیارد تومن افزایش داده!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://telegram.me/SorkhTimes/135681" target="_blank">📅 16:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
رضا جباری به کادر مهدی تارتار اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://telegram.me/SorkhTimes/135680" target="_blank">📅 16:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
پیمان حدادی : صحبت از مهدی ترابی، دانیال اسماعیلی فر، آریا یوسفی، رامین رضاییانه آیا تیم رقیبمون به ما بازیکن میده وقتی قرارداد دارن؟
✅
مثل اینه من اورونوف رو به اون تیما بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://telegram.me/SorkhTimes/135679" target="_blank">📅 15:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
زندی:تیمی در حد قهرمانی بستیم.
🎙
برای خرید محمدجواد حسین‌نژاد با باشگاهش‌ به‌ توافق رسیدیم که روی مبلغ ۱.۸ میلیون‌ دلار این‌ بازیکن را جذب کنیم اما خودِ بازیکن حاضر به امضای قرارداد با ما نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://telegram.me/SorkhTimes/135678" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X91yliwY1bLIdwQT8nPqyncE6p9TTDxDQJOAmtZ8ot2HFJCYAijuREXOwfSO7K2KN3yXG0bdeaZ2JHeNizAa5bz1EGAZEiHl3_cePZcln2zxCiR0032DKz6iCaEssDYEfxlDmJCP8ao-7QbVMSYUUXW3p5zfNSJyjMDIrS_oijR3mvrCjy1Bb33jxMTcrF2-AI5y7KhbBG4x7ev7yNQRewHkr5Ga6wd-GMc6nHqyg_4usDCy3gynUHMwXxSXuISoP8gKJuKSrmoGnrnUj3VaPRsOomu-oEH4D0t9np_8iBnLmc3ls39tiOO2EOLB3moRDMRr9v8hIGnwxklw-qFIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیژن مرتضوی، خواننده و آهنگساز ایرانی مقیم آمریکا، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://telegram.me/SorkhTimes/135677" target="_blank">📅 15:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://telegram.me/SorkhTimes/135676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://telegram.me/SorkhTimes/135676" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
🆕
معرفی سایت و اپلیکیشن مل‌بت
🆓
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://telegram.me/SorkhTimes/135675" target="_blank">📅 15:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
عجب بابا عجب
😐
🚨
🚨
🚨
تسنیم: باشگاه نساجی مازندران رضایت نامه دانیال ایری رو گرون کرده و به ۱۹۰ میلیارد تومن افزایش داده!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://telegram.me/SorkhTimes/135673" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m5DyqEYTZqAO9kh5bTGI8nunQQo1IV6aMurKuBAWTef2UfeL5Y4jlROLTxVwyVDxWdMnAccnXQdTcpDrSN3Up_6PNs50IGimukYcijwJTUlDkwDzjZtlarx2gxeU0y6RTthNXoKc5ROj7n4nE_mmPST1fD1hLxFnc1zBOBbnHP3bFY4k5heIkjAywCObde4-R8RvfbQ-gPv5QSJIgI28sSksMDwA3wjeDY8rR3RgSEetVX89sboiZctfDQh2WyMIe7rA_P13X2_DTuAeuPS3pHh-KgV7Wfh4wRnBEmi7c2JQxVLmJ7fr2NeQeU_-FsgzZxfKCpzrQ44PAZixZnusNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
به پورعلی گنجی اطلاع دادن تا تعیین تکلیف خط دفاع پرسپولیس منتظر بمونه احتمال داره اگه نتونستن دفاعی جذب کنه برگرده
🔴
تنها شانس باقی مانده پرسپولیس مهدی زارع است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://telegram.me/SorkhTimes/135672" target="_blank">📅 15:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
شهاب زندی: دانیال ایری بازیکن ماست و دیگر قابل فروش نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://telegram.me/SorkhTimes/135671" target="_blank">📅 15:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://telegram.me/SorkhTimes/135670" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
🚨
فووووووووووووری
⏺
حسین قهار خبرنگار فرهیختگان: پرسپولیس می‌تونه کسری طاهری رو بخره به یک شرط که نساجی با همون مبلغ به پرسپولیس بفروشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://telegram.me/SorkhTimes/135669" target="_blank">📅 15:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSCNEZtoxKoLb0ppeJ7glZZHSQVIjGHg3UfX9chmEy2CmA092y85ollMOdnugqIkaVYMcDIaW_pH_C3B6jDAsvO0Mj-Of-mcoFGnGNOuJlp04LD9PWiSniJmU-hYk_jnHxbn3iA-r36DuzyjY8IunvE3QT4MeOU_W3TItOfPoBWqBecgblo_1mBJUz67aITXoXYpXxz1nc01_PJrTmL0JFtKE4b9yhZYvYBaA7_Bpo2DYkHMT2kAXqaaoCrrqo0RMep9huAz-nxBi0MUIYuHTLjbPtxGQyk6ADL4UCTtJj5h_9gpFwyh4YaGZOfrklN1UVZRXo_FPoc9yoZSzFROMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://telegram.me/SorkhTimes/135668" target="_blank">📅 15:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
🚨
فووووووووووووری
⏺
حسین قهار خبرنگار فرهیختگان: پرسپولیس می‌تونه کسری طاهری رو بخره به یک شرط که نساجی با همون مبلغ به پرسپولیس بفروشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://telegram.me/SorkhTimes/135667" target="_blank">📅 14:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
حسین قهار خبرنگار فرهیختگان: خداداد عزیزی از انتقال طاهری به نساجی خبر داشت و سوالی که دیشب از کسری طاهری کرد برای به حاشیه بردن پرسپولیس بود. حاشیه ای که با جواب کسری طاهری میتونه سه پنجره نقل و انتقالاتی پرسپولیس رو ببنده
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://telegram.me/SorkhTimes/135666" target="_blank">📅 14:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
فووووری؛ پیمان حدادی پس از عذرخواهی بابت مصاحبه ای که انجام داد ، موفق شد رضایت علیپور رو بگیره و قرارداد کاپیتان جدید پرسپولیس تمدید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://telegram.me/SorkhTimes/135665" target="_blank">📅 14:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
شنیده ها
🗣
پس از صحبت های تهدید آمیز پیمان حدادی؛ علی علیپور در جلسه امروز با پیمان حدادی شرکت نکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://telegram.me/SorkhTimes/135664" target="_blank">📅 14:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPNyB0Msc1y1pVwZqfOj9Be8ISgL0rqGK4qNK_vVzTs4DV1hl_RWSCkc77YrLjrMxhO2mxzW0OtFM4HmxuMk12Ym9JfcJCVUiPdyL2KH9YJd6d-sKGGgnaFE7EhfHeXwK-5a93xLTgrjEJ_NYd76_j9dLacGAO1h9hJL9yqShDalNb7Gwsl5HIh-_Sbe9PoqUo3fkhYITFuorWeo_jtL2iuMzi6rWvsi_cbCee_6vBB1TQbqzt4VKXt5rp1uZCdQXthfwwejl0zv1aIBE2Bfp1BE4KOoTILeiJrwsfG68m8SRHRjkz_IGdUFLDPGSihQNqpl5wRv1LvcaGbXrI35Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
علی علیپور مهاجم ۳۰ ساله و ملی‌پوش پرسپولیس بعد از توافق با مدیران این باشگاه، قرارداد خود را با سرخ‌پوشان پایتخت تمدید کرد تا در جمع قرمزها ماندگار شود
.
✍
📝
خبرگزاری ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://telegram.me/SorkhTimes/135663" target="_blank">📅 13:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
باشگاه اعلام کرد با کسرا طاهری قراردادی امضا نکرده و هیچ قصدی برای خریدش از نساجی نداره/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://telegram.me/SorkhTimes/135662" target="_blank">📅 13:45 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
