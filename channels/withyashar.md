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
<img src="https://cdn4.telesco.pe/file/g2nn3WqY8y9A5w94Pqvx0RsUMtDBqLpDALBHluUUFbrowJBh6AjiPYn5aTdfFb_LcgS3L3_1XrWLPgy5CFWBDWUIMiagYvpdbKaExRzOfCTCVqqkjCkQTYFBpF-4LKLASFjGtiECvCXnD_hF97n2atcji7yL9FKhR3XOjCS8kY5YMOe3kK8fchlvmhDyjTLiU6DTgYuFXInV-uqBeKegRZwpmz4Q8rcl3_1Cxi6mGg7b0Ju_mDjlWepbQqN6uoaCSvZKC22Gkat0s5g4_FlgUVRhU0TeP-WljddVMvFw4qJeTXfQnXwXKi8ruXpgZrGJUjGSvCJRqnBHyNlJM0seCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
@withyashar</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/16152" target="_blank">📅 17:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیانیه دولت لبنان پس از دیدار عون با فرمانده سنتکام
ریاست جمهوری لبنان:
رئیس‌جمهور عون با فرمانده فرماندهی مرکزی ایالات متحده درباره آماده‌سازی برای آغاز اجرای توافق چارچوب با اسرائیل گفتگو کرد.
رئیس‌جمهور عون بر مصمم بودن برای اعمال حاکمیت دولت از طریق نیروهای مسلح خود تا مرزهای بین‌المللی جنوبی تأکید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/withyashar/16151" target="_blank">📅 17:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16150">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید
هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است
@withyashar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/withyashar/16150" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16149">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=iF9ZY62Ky28ZCYsPYj1ny-eJudLGgesZ3h8dZXsv5ogfnug3fxKKtZbCMa2Tyip1RY00j_Ar_yC8ti25c-MZFBsub2RrCW0xcZ9PY-fGTftADLsW3PtJkv2pfPpommjg0pv9LEIk4HCmIAfIjYCStJsp49exNAbkDSaw-iI_n0v0YOZRVS6eReKNyBCzAVz_xufOjoDkgJL3Vom-alpJR4B4EZ8up6O-Y3Pzkmex0aElq0kj_jhrxFoYQ_IeR4ZSG_0OgXUOX5SNeY2Lyc9EMxPJy6Oqlxvo6xLc4HGvBhlSH3UjPdVsu3viurHuM605ME2PiAmg-wfvgrLozhCi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=iF9ZY62Ky28ZCYsPYj1ny-eJudLGgesZ3h8dZXsv5ogfnug3fxKKtZbCMa2Tyip1RY00j_Ar_yC8ti25c-MZFBsub2RrCW0xcZ9PY-fGTftADLsW3PtJkv2pfPpommjg0pv9LEIk4HCmIAfIjYCStJsp49exNAbkDSaw-iI_n0v0YOZRVS6eReKNyBCzAVz_xufOjoDkgJL3Vom-alpJR4B4EZ8up6O-Y3Pzkmex0aElq0kj_jhrxFoYQ_IeR4ZSG_0OgXUOX5SNeY2Lyc9EMxPJy6Oqlxvo6xLc4HGvBhlSH3UjPdVsu3viurHuM605ME2PiAmg-wfvgrLozhCi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید؛ پاسخ خشونت با خشونت داده خواهد شد،
سخنگوی کاخ سفید اعلام کرد که آمریکا به هرگونه حمله، به‌ویژه حملات اخیر به کشتی‌های تجاری، پاسخ نظامی داده و این روند ادامه خواهد داشت. او تأکید کرد رئیس‌جمهور هم‌زمان به دنبال پیشبرد روند صلح است و از ایران خواست «توافق خوبی» با آمریکا امضا کند، در غیر این صورت واشنگتن آماده استفاده از قدرت نظامی خود است.
وی با اشاره به عملیات‌های «چکش نیمه‌شب» و «خشم حماسی» گفت در هر سناریویی آمریکا برنده خواهد بود: در صورت پیشرفت صلح، توافق‌ها ادامه یافته و کاهش قیمت انرژی تداوم می‌یابد؛ اما اگر ایران نقش «مخرب» داشته باشد، به گفته او با انزوای بیشتر در منطقه مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/16149" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند
@withyashar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/16148" target="_blank">📅 15:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTKW_dvtVvwiWPzma9xftskYhR8O-OzJeNL5Nt1-SwakzxxmuyOcL8mVSSBQ-x4tihpyHpooRETfR3yw9n7vJfG_nwiIJE8VG10lcsIzN9Uie423JKxNSmT-liVwm4vrMRejis2IKanSUGg3vjiV9GcOK6sDC3cvkYkzDQi_AaxuhJrmswwrxgOmBTWKr1IZ2JnPZde4jJXzYok1Anebi0TYbBIaheCic7e46FAgZA-trW19sDKGQ1Mu_mGc3OYbJi58w1srOHm1DrFFy9TQQfRlmSFTQ02SljUgYx_j_DDT7_Bu3ElttKSz8C3JpBVV76g6v_KWH-GR4j2qwxhDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : نفت خام ۶۹ دلار، و در حال کاهش است. این کمتر از مقداری است که پیش از آغاز غیراتمی‌سازی ایران بود
قیمت بنزین به سرعت پایین می‌آید! هرگونه تخلف در سطح خرده‌فروشی را گزارش دهید!!
@withyashar</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/16147" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWCpKflsQpv7ZzLEeEU4bSAlKI0YZol6eC_F5svhzuasg88jQ-6ZGMXWw1J9wJIsbb-cy__eDXe_5ImERF26rXFXXDRbHx2_cCgPqSe5cZGMTafVCh0stfVIsJsYVXXsybNjzs2Tea-kW709nGO0R0udUjyCuBqf6tOgvOfTbErkmpZ_20cxo6CcpV6uibQ2WLRR4jiJF3CftlAOC4K-9rT6DGeoqgEMlds2WF7uDp9wyNQ4axCE-lm00azP9HWXmPS_01kwFatoYypzcmu13-CEIVKpvYxPkbVMYGR-xD5QrxLvezBhGsLfhE8JXXwBKsNNtX1DPeyV7V56OhxBOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران درخواست ملاقات کرده است. این ملاقات فردا در دوحه برگزار می‌شود! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/withyashar/16146" target="_blank">📅 15:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16144">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwWptg0oZnBaE7ihVR4qb508aLkz_HTk9AbQy3N9idJ8IYb6s64SuphQ-Wc_kvygBZhhtZAFE_P6d_EakNhtjX3IE5Ge2Hg7i6cw8rjdyBdFvL5Apjk4mKt8AuEmfvANKGLGcfLb06WehJU-gEoW3MjfNtK4mFqcIdiznFVJpirEaoNtocDB7ASkhoo7g9aUVI35cbJtpLcdQ_u9NPON3F68YJrOe2_bPVPGq8s6vrkbzuZSjkHIFrt2qhU2Dq8D0Pa38axC95UxhkkrQpZdhbO6Z8mFyUZX7WXP9naaBGuvZRgqApmC_PSJwwCuhTKxbkcFB2mcTyFU0Q0nlWxBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n34EBI9E8xB49mGG5-QULRTpVsnzsgDUwqRBIi4LTy-etjDeGFsDQ0vxApvTRtzv0I9g4IaX2KTpZrPx1tP1VZyAEQ_fPkMzyA9IfGu0zgly_OChqhryVr96IQp-sisB-YLKqYPVZxANuXPDWCMRfxUBckbY3ruRe62dGyCBgXELs6K75_eN3LL4FbDA8qhuYZikG9hFXiN6Z9mlvOaafpYsVmm0lLBlXy2MkMDgVblIls40ieMGIXYXPGqRnuFlPWJ9l1BZ_uFkN0LouVB0H85rxlKtjv8NhWcnTO2_vyFHEHIUb-_jo6KGCngLqvjXFJjWpjCabF8ohCg1H0DOoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نفتکش شرق لیما، المحبوبه (شماره IMO 9340415) با پرچم عربستان سعودی است که از چین حرکت می‌کند با سرپیچی از دستورات سپاه پاسداران عبور فقط از جنوب جزیره لارک از کریدوری تحت حمایت آمریکا و در میان اسکورت سنگین هوایی نیروی هوایی ایالات متحده، از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/16144" target="_blank">📅 14:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16143">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز: ایران شرکت در مذاکرات فنی را لغو کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/16143" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16142">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGZd2xWmlBL97sb2ClFaXGBcP5t0Z1Azg2WkG_fjn0ti-AMaEurV-aG2sODGLtWSoAQh_lQ07_PmgBAqMq42nnlrViCoSCiAAe76J2VMcdONPja6rfNkKB4lUYp2vgX2HxgJeePs-ayjQBj9mCN6kHwYCxX99sj_svhrnmxRRpuSVXR_M2yKgatyR1n8C09MgBTqyZGKvLvqUL99WGG8xTWSq7CzQYOCLv96HevQ5s5UxSoSZ7q35gJh4L5Wqkv9NFXgudN16lvH0jTSa5TbmGR8v2Di5JH9mfLw-wNNZ9SG-w-DUrRJ5ulmv2RX89xBZh3PE2vS5h6_3oE250toqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل اسرائیل، ایال زمیر در‌جلسه به مناسبت ۱۰۰۰ روزه شده مبارزه : الان جنگ به یه مرحله حساس رسیده
@withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/16142" target="_blank">📅 14:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16141">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgvMrI6T1TBxs1QPVZjAipyQa54ARSOdh-Z567Pc2GefpGrVc35vj2STbcn4sa3Q-mEQiJSRjebeGNJ1B6PC8DhUPJTFADIz7mJbKy3SZsP_VLQORSmn2QLTCtGbs4GW718suoXuGaB_EdOZCdlxUb9uv6uBXqCQyj0OsDEXFKANXow0KnNUo8bWKSqHaLm8ULR4mX1V5_3ZA2igvrSgXXLWIR0G6LMUjYY7sVT8lxwo43wXXYnrt9Ka2W0dpthrr8cZZUrFXFpYvbpcEEPHj-tanGzFK2Nydd5jmuwSyJ678rO3nnhTtfC9npbh3gSvM7xcVBymIwHJHS3VNqGnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بالاترین آمار نظرسنجی‌ها تا کنون. حتی بالاتر از روز انتخابات، ۵ نوامبر. این علیرغم این واقعیت است که ایران سلاح هسته‌ای نخواهد داشت!
@withyashar
یاشار : نردبون ایران
😂</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/withyashar/16141" target="_blank">📅 14:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16140">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کانال 12 اسرائیل: جی دی ونس و افرادش کسانی بودند که طرح مخفی موساد برای تغییر حکومت در ایران با کمک کردها را به اردوغان، لو دادن
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/16140" target="_blank">📅 13:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16139">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کانال ۱۶ اسرائیل :
«این توافق تنها زمانی محقق می‌شود که مرغ دندان داشته باشد»
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/16139" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16138">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جزییات مراسم تشییع خامنه ای درتهران
استاندار تهران: مراسم وداع از ساعت ۶ صبح روز شنبه ۱۳ تیر در مصلای تهران آغاز می‌شود و تا روز بعد ادامه خواهد داشت
پیش‌بینی شده است نماز در ساعات ابتدایی روز دوم اقامه شود و پس از آن، مراسم وداع تا ساعت ۱۴ روز یکشنبه ۱۴ تیر ماه ادامه پیدا می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16138" target="_blank">📅 12:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16137">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ارتش اسرائیل و شاباک: یک تروریست دیگر که در ربودن شهروندان در ۷ اکتبر نقش داشت، از بین رفت
@withyashar</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/16137" target="_blank">📅 12:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16136">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الان صدای انفجار‌ در شیراز (از قبل اعلام شده بود) مهمات عمل نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/16136" target="_blank">📅 11:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16135">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYJ-yUUzX2ADkPHVVIdvyCMyXtLToSITDZRmOuh44VeLRHASXOLHiCFqS1_5ddosUq462KVjkOp4yWkiLPY3C_3ZLuT4IfjGyTnZ0sdb4dw9PUBd9sNDAsw-Ia9imqhNJm21_FTk71sxQvK1Qe05HAlfoyAhBT1oPNkFoBToD0G3M2m0xQQqL09iBB1uV7vzXV63jHSPKCEmLcUM5LO3E3zXOKyZ6ckiRueV7hi2Kab1MHYJ9fgCUW0ojGiQb46ZNjqLZuiqkj7zKHOlGH4XQq9N_ykZEE7DJFUdd9dimoYUV2fl_a-dilLWLSyx0VToHI0rq4H7tK6T2L4RaK7lIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود اهواز بعد از شنیده شدن صدای انفجار
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/16135" target="_blank">📅 11:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16134">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صدای انفجار اهواز
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/16134" target="_blank">📅 11:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16133">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور:
۶ میلیارد دلار از منابع مسدود شده ایران در قطر آزاد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16133" target="_blank">📅 11:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16132">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس‌جمهور روسیه، پوتین، دیروز برای اولین بار اعتراف کرد که روسیه به دلیل حملات اوکراین در خاک خود با کمبود و مشکلات سوخت مواجه است، اما ادعا کرد که نیروهایش به جنگ ادامه خواهند داد و حتی به تصرفات بیشتر در خاک اوکراین اشاره کرد. «این حملات به تأسیسات زیرساختی ما مشکلاتی ایجاد می‌کند، این واضح است»، او در مصاحبه با رسانه‌های محلی گفت و ادعا کرد که «کمبود بحرانی نیست»
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/16132" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16131">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر کشاورزی آمریکا: محصولات کشاورزی آماده ارسال به ایران هستند
مجری: محصولاتی که قرار است به ایران بروند، احتمالاً قبلاً کاشته شده‌اند؟"
بروک رولینز: "دقیقاً درست است و آماده ارسال (به ایران) هستند.
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16131" target="_blank">📅 10:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16130">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbEmljx68CGaYb7wXih4wldSgWDjC2Pc911_5clAB2GMEAnCMrUPrOFugRAV4hpuv57FbOxjcPu06TIA61io9ZdUp3Eum6WTgQoIY9QXthzCW2Bwo-8f7yhC0qpDOGQp_VpCz4acS3cJ-biBR40adF99di5r_-LYBxFHolkVwoskBSjYR76l8Q_e7UEmNAIoK-LOxFdbQuTwFKyfwF8-ExXULme1_B5r14vg9mZhOcz2boug0O7FPzzu3-Pf_7nSeESnDXRAPqw51_Ijm88ILSwg05VKsYAeKE7pcMJuMipSxUQO0FzIY6udHPZ2cCTSmsPxZaNA4AUyHErvqwMqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر کاظم
دست کج
به عمان برای برگزاری نخستین نشست کمیته مشترک هرمز
این کمیته قرار است به‌صورت منظم برای هماهنگی‌های منطقه‌ای در حوزه امنیت و مدیریت تنگه فعالیت کند؛ اقدامی که می‌تواند نشانه‌ای از تقویت همکاری‌های تهران–مسقط در یکی از حساس‌ترین گذرگاه‌های انرژی جهان باشد.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16130" target="_blank">📅 09:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16129">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است. هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/16129" target="_blank">📅 09:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16128">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جاسم البدیوی، دبیرکل شورای همکاری خلیج فارس:
در مورد بسته‌ی ۳۰۰ میلیارد دلاری، من چیزی ندیده‌ام. نه به من و نه به دیگران در کشورهای شورای همکاری مطلبی گفته نشده. ما چیزی در این مورد نمی‌دانیم
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/16128" target="_blank">📅 09:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فیلمی از حمله‌های سنگین آمریکا به مناطق جنوب
@withyashar
احتمال زیاد رادار سیریک</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16127" target="_blank">📅 09:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16126">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124ea90741.mp4?token=lR63zzwPsSyaLGbj8xh0t0HFW9cfaETWeJpvrBM4IkiiCtPHE5hkIbKTJBq6AhwK4Pv4hcitIfd5Q_XM7UX7OiIGIJ1w55thVslDwiVeBVN41OQ830dDdJNLNjkEEjZvXbu-e5pJzyJcDNUlUtquaCwOxILLmKMKOfx4YkFkLwX9Dfeoi5sFIU_PQCa4zWQ5qRr350vrod-LlzYTXjxE3LPQp9wdThHvcz701zoELjvE0Z5M0LVNrD4X9eB0cntHAB6mQNlcxpYaS5ogzAhyNuqvCQqGYpfhjqTtz8FUc9IOYKSIuHer6yXutoiwNsERnUpolefsIWFyCWp9gN_4wjZ0SBgpjbnLjrQLH1hGehOVDi3cbDyM_h0ePLnuFIs8VQCA-UjeJNzdJphB6iWrQjFaNeUOWTvBHeiYFKmQUBao9ErKEZ3SGGliWSnGAXyejQXqLbLMLkNSoCAFHzFls2laskFQa3tzm6NR2lDWUybjiq1E-sTDLmVFgvTLlrEUvWvpW3xI0MIL7lvjo5x0YhEfl7vDwUJBA4yOgYBqQFk8zO4rU-yPxtQFv8jD46UWxR-wp5mnf5TT-KXHkdvu4xjUnJtg895FEGl3ddWOfTJbU8yzSQ544KiodK1HLDgtuIZh13QihIhBUlf9a6-DBU4F4Va5qVHuRyozNKv09PI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124ea90741.mp4?token=lR63zzwPsSyaLGbj8xh0t0HFW9cfaETWeJpvrBM4IkiiCtPHE5hkIbKTJBq6AhwK4Pv4hcitIfd5Q_XM7UX7OiIGIJ1w55thVslDwiVeBVN41OQ830dDdJNLNjkEEjZvXbu-e5pJzyJcDNUlUtquaCwOxILLmKMKOfx4YkFkLwX9Dfeoi5sFIU_PQCa4zWQ5qRr350vrod-LlzYTXjxE3LPQp9wdThHvcz701zoELjvE0Z5M0LVNrD4X9eB0cntHAB6mQNlcxpYaS5ogzAhyNuqvCQqGYpfhjqTtz8FUc9IOYKSIuHer6yXutoiwNsERnUpolefsIWFyCWp9gN_4wjZ0SBgpjbnLjrQLH1hGehOVDi3cbDyM_h0ePLnuFIs8VQCA-UjeJNzdJphB6iWrQjFaNeUOWTvBHeiYFKmQUBao9ErKEZ3SGGliWSnGAXyejQXqLbLMLkNSoCAFHzFls2laskFQa3tzm6NR2lDWUybjiq1E-sTDLmVFgvTLlrEUvWvpW3xI0MIL7lvjo5x0YhEfl7vDwUJBA4yOgYBqQFk8zO4rU-yPxtQFv8jD46UWxR-wp5mnf5TT-KXHkdvu4xjUnJtg895FEGl3ddWOfTJbU8yzSQ544KiodK1HLDgtuIZh13QihIhBUlf9a6-DBU4F4Va5qVHuRyozNKv09PI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلیل آخرینم باش…
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16126" target="_blank">📅 02:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16125">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سناتور جان کندی : ایران الان مثل یک پیرمرد خیلی پیر است که توانایی گرفتن سرماخوردگی را ندارد. ما آنها را به شدت تضعیف کرده‌ایم. نباید تسلیم شویم
برای من عدم توافق قابل قبول است؛ توافق بد قابل قبول نیست.
در پایان یک دوره زمانی معقول، ۶۰ روز یا هر چه که باشد، فکر می‌کنم باید دوباره وارد شویم و دوباره مثل گربه‌زن با آنها برخورد کنیم
باید آنها را بخوریم و استخوان‌ها را روی زمین تف کنیم
@withyashar
آخرش حرف منو میزنه منظورش اینه گربه گیرشون کنیم‌
😂
😂
😂</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16125" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16124">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16124" target="_blank">📅 01:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16123">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لغب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16123" target="_blank">📅 01:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16122">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است.
هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16122" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16121">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=YpGQqbNu_aU1P9w8iI-dayPX285VymzE05DgFR8ghP8tiJ464J61kJ4-DGGw1BV9iI93t_59GY74vim-vCm9pbcQPGiDu4MiaGYtl47YSjOchhg7ewILFPwxK_waZM9iS2E2x78GiwtBvxBZ2AsOPIqxNQ34PjeG8ca18o5eobmpd_2-Ca6r1NcHIFJ7jlXW5Th8Ykl6mQKDjRRcrWwau96aZbHSpN8Vm_Ka-E3JoEFveSkO8KkoLvSY9RtIHIsVWrZ8F1y1hjbX4LBoBnB7ZqzHYWJXMccFsYDbHsR3NNy5nL7TTedZKmHOHtke4xGpTLERiFrwnNojdxJuMavtBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=YpGQqbNu_aU1P9w8iI-dayPX285VymzE05DgFR8ghP8tiJ464J61kJ4-DGGw1BV9iI93t_59GY74vim-vCm9pbcQPGiDu4MiaGYtl47YSjOchhg7ewILFPwxK_waZM9iS2E2x78GiwtBvxBZ2AsOPIqxNQ34PjeG8ca18o5eobmpd_2-Ca6r1NcHIFJ7jlXW5Th8Ykl6mQKDjRRcrWwau96aZbHSpN8Vm_Ka-E3JoEFveSkO8KkoLvSY9RtIHIsVWrZ8F1y1hjbX4LBoBnB7ZqzHYWJXMccFsYDbHsR3NNy5nL7TTedZKmHOHtke4xGpTLERiFrwnNojdxJuMavtBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل فیلمی از انفجار تونل در منطقه مجدل، جنوب لبنان، منتشر کرد. ارتش اسرائیل اعلام کرد که این نیروها تونلی را که در واقع یک مجتمع زیرزمینی ساخته شده با استفاده از دانش و فناوری رژیم ایران بود، منهدم کردند. در داخل تونل صدها سلاح و چهار سکوی پرتاب به سمت خاک اسرائیل وجود داشت.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16121" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16120">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.       @withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/16120" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16119">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار شود. تشدید تنش‌ها آنها را به مکان دیگری منتقل کرد و دوباره بر تنگه هرمز متمرکز شد.  به گفته یک مقام آمریکایی و یک منبع آگاه، انتظار می‌رود…</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/16119" target="_blank">📅 00:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری اردن: سپاه به دنبال ترور یکی از فرماندهان سنتکام بود که موفق نشد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/16118" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">من مشکل جدی فیزیکی‌ برام پیش اومده کمک خواستم ! همین ! کلت زیر گلو کسی نزاشتم که ! جم کنید مسخره بازی رو</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/16117" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع @withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16115" target="_blank">📅 00:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرنگار اسرائیلی: ایران تونل‌های عظیمی در جنوب لبنان ساخته است.
مقادیر مواد منفجره‌ای که ارتش اسرائیل به این منطقه پمپاژ می‌کند، بیشتر از هر چیزی است که در تمام جبهه‌های جنگ وجود داشته است
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16114" target="_blank">📅 23:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16113" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16112">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📩
درخواست همکاری
اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:
نام یا لغب
نوع فعالیت / حوزه کاری:
سابقه کاری:
آدرس لینکدین:
(خیلی خوبه باشه)
آدرس اینستاگرام:
(اختیاری)
آیدی تلگرام:*
(الزامی)
توضیحات:
لطفاً تخصص‌ها، مهارت‌ها، سوابق و توانایی‌های خود را به‌صورت مختصر معرفی کنید.
لطفاً اطلاعات را فقط برای دایرکت همین چنل ارسال کنید
ادمین (خبری، بازار های مالی،گیم،موزیک، ورزشی)
برنامه نویس
و کسی که بتونه ویکیپدیا بیاره بالا
ویدیو ساز فقط با هوش مصنوعی
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16112" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16111">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله…</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16111" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16110">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله خفیف رو احساس کنید. از سمت دیگه حزب الله اخطار داده که با این کار تنشها تشدید خواهد شد. خواهیم دید چه میشود.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16110" target="_blank">📅 23:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16109">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نخست‌وزیر بنیامین نتانیاهو و وزیر دفاع اسرائیل کاتز در بیانیه‌ای مشترک: "در چارچوب عملیات «پایان جمله»، ارتش اسرائیل اکنون زیرساخت تروریسم زیرزمینی حزب‌الله را در منطقه روستای مجدل زون در جنوب لبنان نابود کرد. اسرائیل پیشاپیش آمریکا را مطلع کرده است"
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16109" target="_blank">📅 23:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16108">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۴ ، جنجال در کابینه: به دیوید زینی، رئیس شین بت، دستور داده شد تا تحقیقات در مورد نشت عملیات «غرش شیران» به اخبار کانال ۱۲ را (علیرغم مخالفت مشاور حقوقی) پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16108" target="_blank">📅 23:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16107">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فضائلی، عضو دفتر حفظ و نشر آثار آیت الله خامنه ای: امروز قرار بود مذاکرات فنی برگزار شود که ایران آن را لغو کرد و شرکت نکرد که دلیل این امر درگیری‌های این چند شب گذشته بود و دلیل دیگر این است که منتظر اجرای برخی شروط هستند که مثلا امکان برداشت پول‌های بلوکه شده است یا خیر
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16107" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16106">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش ها از رهگیری چند موشک برفراز اردن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16106" target="_blank">📅 23:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16105">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت خارجه اسرائیل :
شادی مردم ایران از حذف تیم جمهوری اسلامی یک چیز را نشان میدهد: انزجار و بیزاری مردم از چیزی که به رژیم مربوط میشود
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16105" target="_blank">📅 23:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16104">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هم اکنون اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16104" target="_blank">📅 22:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک مقام ارشد دولت ترامپ امروز به رسانه‌ها اعلام کرد که مذاکرات میان آمریکا و ایران که قرار است آخر هفته جاری در سوئیس برگزار شود، همچنان طبق برنامه انجام خواهد شد
این اظهارات، گزارش پیشین روزنامه وال‌استریت ژورنال را رد می‌کند؛ گزارشی که مدعی شده بود این مذاکرات به دلیل دور جدید حملات متقابل ایران و آمریکا در منطقه خلیج فارس به تعویق افتاده است.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16103" target="_blank">📅 22:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=NrtDlTVs5WLwymt8MxcVsszBPOBXoXVrhlLbSx0obR9yNTGo42VywhZ6u8ToK27wQpTZXWG_vu00XPuJfC8vhqIUB8S5byKi86gVRHTg0XrxFQtgneZNtQGttwoF-fSZY6Eql9zCkf7fje4POEm3f74380jDFl3XgmfTsIaCd-HvldrAzLe-lLNh5fpvu-l_2qfemNHRYAw7-hwh98W-b2lSs2ih6OCA5X7rQ8paOMoS-bdggdQfEMChnl3t0YuUNeiwUDkui62RyIY_aDJUQVkrzDqAlhPyk68LhvRtcag_5-uyw3HVU_W5reIKnB1NKVtLCc4ehh8SaL-37mMj8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=NrtDlTVs5WLwymt8MxcVsszBPOBXoXVrhlLbSx0obR9yNTGo42VywhZ6u8ToK27wQpTZXWG_vu00XPuJfC8vhqIUB8S5byKi86gVRHTg0XrxFQtgneZNtQGttwoF-fSZY6Eql9zCkf7fje4POEm3f74380jDFl3XgmfTsIaCd-HvldrAzLe-lLNh5fpvu-l_2qfemNHRYAw7-hwh98W-b2lSs2ih6OCA5X7rQ8paOMoS-bdggdQfEMChnl3t0YuUNeiwUDkui62RyIY_aDJUQVkrzDqAlhPyk68LhvRtcag_5-uyw3HVU_W5reIKnB1NKVtLCc4ehh8SaL-37mMj8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار ۱۷۵،۰۰۰
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/16102" target="_blank">📅 22:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16100">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/16100" target="_blank">📅 22:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16099">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">والانیوز عبری
: اسرائیل در حال آماده شدن برای احتمال حمله مستقیم ایران است، پس از امضای توافق لبنان و اسرائیل
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16099" target="_blank">📅 22:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16098">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امروز تولد ۵۵ سالگی ایلان ماسک، ثروتمندترین فرد جهان هست
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16098" target="_blank">📅 22:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16097">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دیدبان اتاق جنگ : هواپیمای c 130  هرکولس ارتش نشست مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16097" target="_blank">📅 22:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16096">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارشاتی از شلیک موشک‌ از ایران به سمت اردن @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/16096" target="_blank">📅 22:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16095">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارشاتی از شلیک موشک‌ از ایران به سمت اردن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16095" target="_blank">📅 21:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16094">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">افزایش حالت آماده‌باش در اسرائیل به دلیل نگرانی از پرتاب موشک از ایران
@withyashar</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16094" target="_blank">📅 21:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d7be6f9.mp4?token=YiAaGOiqpmguOfx8JMLM9i9ParU4grvNjs9PnqjJ7-hcJH_yDVq3HBLwne2fSyvk6ovBDPochUHxD7EWkNJ4RAp2xaUL1PVHH-Ipvn1XmsSmyrvoWu4Tld6jBPoC7xRXoZc3P5BQWK2wJRGNkvHnNnA1vj60mbLtzjMeNtjHNv6Exhwek_Z79OXlxbSlU2DpyYvFHRFXS6Wruo3JfIIfIMjDN-jPlaPELGKVuBmCz0uh5Uc7S3OMzhEaQDkHqt64Yf4fQiKWHJ8lSNjxemcJ1EapWTMatntwqZ-MvlezIeKvS_PD30BRXdUP1yIyLykeOL7DPpaZ-BZ5yqnNj6Glzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d7be6f9.mp4?token=YiAaGOiqpmguOfx8JMLM9i9ParU4grvNjs9PnqjJ7-hcJH_yDVq3HBLwne2fSyvk6ovBDPochUHxD7EWkNJ4RAp2xaUL1PVHH-Ipvn1XmsSmyrvoWu4Tld6jBPoC7xRXoZc3P5BQWK2wJRGNkvHnNnA1vj60mbLtzjMeNtjHNv6Exhwek_Z79OXlxbSlU2DpyYvFHRFXS6Wruo3JfIIfIMjDN-jPlaPELGKVuBmCz0uh5Uc7S3OMzhEaQDkHqt64Yf4fQiKWHJ8lSNjxemcJ1EapWTMatntwqZ-MvlezIeKvS_PD30BRXdUP1yIyLykeOL7DPpaZ-BZ5yqnNj6Glzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
اگر ایران فکر کنه ترامپ قراره در برابر ادامه حمله به کشتی‌های بین‌المللی دست روی دست بزاره، کاملاً در اشتباهه؛ چون همین چند شب اخیر نشون داد که این کارها رو بی‌پاسخ نمی‌ذاره.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16093" target="_blank">📅 21:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به گزارش i24NEWS، ایران هر شب حداقل شش پهپاد را به سمت کشتی‌های تجاری در تنگه هرمز پرتاب می‌کند که برخی از این پهپادها توسط ارتش ایالات متحده رهگیری شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16092" target="_blank">📅 21:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16091">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تایید خبر توسط ایران: مذاکرات به دلیل حمله آمریکا به ایران لغو شده است  @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16091" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16090">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شبکه ۱۲ عبری:
توافق میان اسرائیل و لبنان که متن کامل آن، از جمله در وب‌سایت وزارت خارجه آمریکا، منتشر شده است، دارای یک
پیوست امنیتی محرمانه
نیز بوده که همچنان طبقه‌بندی‌شده باقی مانده است. دلیل اصلی محرمانه ماندن این پیوست، درخواست صریح دولت لبنان عنوان شده است.
هیچ‌گونه عقب‌نشینی خودکار و زمان‌بندی‌شده‌ای وجود نخواهد داشت
؛ بلکه هرگونه عقب‌نشینی یا اجرای تعهدات، بر اساس میزان موفقیت در میدان و ارزیابی نتایج عملی انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16090" target="_blank">📅 20:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16089">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد. @withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/16089" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16088">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکسیوس: اسرائیل و لبنان به این نتیجه رسیدن که برای جلوگیری از دخالت جمهوری اسلامی باید توافق کنن.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16088" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هم اکنون نیروهای زمینی سپاه مواضع گروه کرد در کردستان عراق را با توپخانه هدف قرار دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16087" target="_blank">📅 19:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16086" target="_blank">📅 19:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16085" target="_blank">📅 19:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دلار و تتر ۱۷۲،۵۰۰
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16084" target="_blank">📅 19:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">طالبان افزایش قیمت اینترنت را ممنوع کرد
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16083" target="_blank">📅 19:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16082">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
این بوستو بترکونین ایموجی اضافه کنم
😕</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/16082" target="_blank">📅 18:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16081">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مجتبی خامنه‌ای بیانیه‌ای منتشر کرد که در آن خواستار اصلاحات گسترده قضایی، اقدام سختگیرانه‌تر علیه فساد و ادامه پیگیری پرونده‌های حقوقی درباره جنایات جنگی آمریکا و اسرائیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16081" target="_blank">📅 18:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16080">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba88b4582.mp4?token=C4a3kV9e_JoeNPtHlwzGICOP3EZAMPUmMEtPcwvu5x_wZnUfuMRXzB84_1FH2VouQ_kAMIYw4pv3EvxouDcrVqEsmQlD2CI6B9I40BVROh3EZCwoZIT1KLkKWtJ2O7eqOGKaykzYYBj9pUDWjFW6zWH4zMzdq3y-_cMcS9oC4mXe5JxqfCIefB4ACgMExGVLWqNnGQytPNabOr71dOtF6KvEO41HbBh6fAqjhaYXrG-YfCDx3Mz8K2XbaVNsu37UuwKhHGeCVjsL22ZZOwYkuLZr5o5Sp7JjwQlGGO3ZsUQ6yVdLK7Kxn_ao3DUWtdJrIsLqgz2iwCf6RHht7M3eN4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba88b4582.mp4?token=C4a3kV9e_JoeNPtHlwzGICOP3EZAMPUmMEtPcwvu5x_wZnUfuMRXzB84_1FH2VouQ_kAMIYw4pv3EvxouDcrVqEsmQlD2CI6B9I40BVROh3EZCwoZIT1KLkKWtJ2O7eqOGKaykzYYBj9pUDWjFW6zWH4zMzdq3y-_cMcS9oC4mXe5JxqfCIefB4ACgMExGVLWqNnGQytPNabOr71dOtF6KvEO41HbBh6fAqjhaYXrG-YfCDx3Mz8K2XbaVNsu37UuwKhHGeCVjsL22ZZOwYkuLZr5o5Sp7JjwQlGGO3ZsUQ6yVdLK7Kxn_ao3DUWtdJrIsLqgz2iwCf6RHht7M3eN4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: تا پیروزی کامل بر دشمن باید جنگ کنیم؛
جمشیدی، کارشناس صداوسیما: جنگ نیمه کاره به صلاح نیست؛ باید به نقطه بازدارندگی مطلق؛ سلطه و تفوق برسیم؛
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16080" target="_blank">📅 18:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16079">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرگزاری رسمی عراق: کارزار نخست‌وزیر برای تعقیب و بازداشت متهمان به فساد ادامه دارد، تا کنون 47 نفر از نمایندگان و مقام‌های دولتی به اتهام فساد بازداشت شده‌اند. @withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/16079" target="_blank">📅 18:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16078">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بنابر اعلام منابع میدانی،در محور پیرانشهر به مهاباد درگیری بین رژیم و گروه کرد ها رخ داده
درگیری در اطراف روستای گاگش در محدوده مهاباد رخ داده و طبق اطلاعات منابع میدانی عامل این حمله گروهک کرد پژاک عنوان شده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16078" target="_blank">📅 18:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16077">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16077" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16076">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی ارتش ایران : ما برنامه‌های جدی در دو حوزه داریم: تولید داخلی و تأمین تجهیزات پیشرفته از کشورهای دوست.ما قطعاً در روزهای آینده به سیستم‌های پیشرفته‌تری مجهز خواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16076" target="_blank">📅 18:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16075">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادعای کانال ۱۴ اسرائیل: در توافقنامه هیچ جدول زمانی برای خروج وجود ندارد و هیچ چیزی اسرائیل را به آن ملزم نمی‌کند.
در واقع این یک توافقنامه بسیار خوب است، اما حزب‌الله از این بابت عصبانی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16075" target="_blank">📅 17:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16074">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فارس: جمهوری اسلامی در دوران گذار به نظم جدید جهانی، چاره‌ای جز ساخت بمب اتم نداره تا گزینه نظامی علیه کشور از روی میز برداشته بشه.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16074" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16073">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فارس: ۶۲ نماینده مجلس که که پیش‌تر اعلام کرده بودند روز یکشنبه مقابل مجلس حضور خواهند یافت، برنامه را لغو کردند
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16073" target="_blank">📅 17:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16072">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حقیقت : نیروهای امنیتی عراق یک عملیات بزرگ ضد فساد اجرا کردند این عملیات در منطقه امنیتی «سبز بغداد» انجام شد چندین مقام سیاسی، نماینده پارلمان و مسئول دولتی بازداشت شدند برخی گزارش‌ها می‌گویند تعداد بازداشت‌ها بین ۷ تا بیش از ۱۰ نفر بوده و در برخی منابع غیررسمی…</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16072" target="_blank">📅 17:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16071">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گاردین و افشای سندی محرمانه؛ خیز «هیات صلح» ترامپ برای کسب مصونیت مطلق قضایی در غزه
پیش‌نویس قطعنامه‌ای که به دست روزنامه «گاردین» رسیده نشان می‌دهد «هیات صلح» مورد حمایت سازمان ملل که دونالد ترامپ اوایل سال جاری میلادی برای اداره غزه تشکیل داد در پی اعطای مصونیت حقوقیِ گسترده‌ به خود است.
به گزارش گاردین، متن به‌کاررفته در پیش‌نویس همچنین به این نهاد اجازه می‌دهد تا اموال عمومی در غزه را «به‌طور رایگان» در اختیار بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16071" target="_blank">📅 16:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16070">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16070" target="_blank">📅 16:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16069">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حقیقت : نیروهای امنیتی عراق یک
عملیات بزرگ ضد فساد
اجرا کردند
این عملیات در
منطقه امنیتی «سبز بغداد»
انجام شد
چندین مقام سیاسی، نماینده پارلمان و مسئول دولتی بازداشت شدند
برخی گزارش‌ها می‌گویند تعداد بازداشت‌ها بین ۷ تا بیش از ۱۰ نفر بوده و در برخی منابع غیررسمی عددهای بالاتر هم گفته شده
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16069" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16068">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رئیس جمهور و نخست وزیر عراق دیشب کودتا کردن هم یک خبر فیک نیوزه !!!</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16068" target="_blank">📅 16:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پست ترامپ مبنی بر‌ اینکه مسی بهترین بازیکنه فیک نیوز هست !</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16067" target="_blank">📅 16:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16066">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">زلزله مازندران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/16066" target="_blank">📅 16:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16065">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">زلزله مازندران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16065" target="_blank">📅 16:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16064">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فایننشال تایمز به نقل از یک دیپلمات گزارش داد که میانجی‌ها در حال انجام گفت‌وگو با طرف‌های درگیر [ایران و آمریکا] هستند تا تلاش کنند تنش‌ها را کاهش دهند.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16064" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16063">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هاآرتص: سامانه‌های دفاعی اسرائیلی به قطر و عربستان سعودی فروخته شده‌اند؛ با وجود اینکه هیچ‌یک از این دو کشور روابط دیپلماتیک رسمی با اسرائیل ندارند
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16063" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16062">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اولین پارکینگ ‌پناهگاه تهران به پایان رسید
شهردار منطقه ۱۰: ساخت اولین پارکینگ پناهگاه تهران در یکی از مناطق پرجمعیت و پرتراکم تهران به اتمام رسید و بزودی بهره‌برداری از آن آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/16062" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16061">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی رفته عراق ستاد مشترک تشکیل داده برای تشییع جنازه !   عراقچی : جنازه علی خامنه‌ای در بغداد، کاظمین، کربلا و نجف تشییع میشه @withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/16061" target="_blank">📅 13:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراقچی رفته عراق ستاد مشترک تشکیل داده برای تشییع جنازه !
عراقچی
: جنازه علی خامنه‌ای در بغداد، کاظمین، کربلا و نجف تشییع میشه
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16060" target="_blank">📅 13:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqueqrSxJ40FbQQI7nT3NLSpZZLZwkH6uuOePsa4NsRXrTAJChgmJyzkluuTPDQXQ3j7-ONwIxoVfWWL18a-Jl_kZdNWC-4ZYGOJUxPouoYeq-XbJROclochErpnbaokTk-pCol2qlao4pajAUlvvo-Zrlp3sWENEtwQn5WoQjGsp_P6-WUIbKLY6XwvxazkosOOEf-kj1ozjh1ERxoQX8r9xXJ1XZfs1Zyrnj9P_RWZREhuxQd3LdYD1kT-wp1RqE9rb-ySbO0jGtaAaDK_1-2PTf-q4Uugx8Aah3orWOyTZYrYOLH_P3xFvDcR0z798sLaLXWNC4ButXXWRx8ipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری خواهر جاویدنام
صهبا رشتیان
،
داور بین‌المللی
که در اعتراضات دی ماه، جونشو اهدا کرد.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16059" target="_blank">📅 12:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arr_cza9yhCFvI4epeRUt4ha3P1jZecvUwhpKQrClWEpQw7MldtdhLZ77UedS4eYeBeRwepXIB2DhL00SOW5O3yUF0V6d_sG9wCeu67LczUF-pNAsLH4BZtKHIAnt0ivuzl08B5s2EyyleHtDGrKyRJn_ykXpJOpn5n-uqc35_ATat9vTatPQGkUWlWjKfuf9hTAKEaweALHwi92rF82u31sSFE7MfXpXDvUnES3ajTYIaCPsavJ3hoQ9xWFRjco1NCcu6PtIBdO7hsvDIPVJhM01k1heTUor6M87pP1nMu7XLNpu9RzWyTJHjiPQyWLrPsp8C_BYq1I6zpzXyIj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16058" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در ساعت ۲۰:۳۰ هفتم تیر ۱۳۶۰ ( دقیق ۴۵ سال پیش و همین روز یکشنبه ) جلسه‌ای در سالن اجتماعات دفتر مرکزی حزب جمهوری اسلامی واقع در محله سرچشمه تهران و در جلسه‌ای که برای بررسی انتخابات ریاست جمهوری آینده برگزار می‌شد، بمبگزاری با ۲ بمب رخ داد که منجر به کشته‌شدن ۷٣ نفر از وزرای دولت، نمایندگان مجلس شورای اسلامی و اعضای حزب جمهوری اسلامی شد. سید محمد بهشتی رئیس قوه قضائیه و دبیرکل حزب جمهوری اسلامی از جمله کشته‌شدگان بود.
میدان هفتم تیر در تهران، به عنوان یادبود این حادثه نام‌گذاری شده است.
توسط سازمان مجاهدین خلق ایران و عامل انفجار ، محمدرضا کلاهی بود
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16057" target="_blank">📅 11:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16056">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16056" target="_blank">📅 11:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt-9r7IiPu8QYhpfV64m_x75byrUtiWKErTpHKzM55IFjKHVEd7nc8zfCSHRjKyitwRQrBat90hstaqh6-JTqrIhO-lq7Sq7yBQEd3uz-AEYlejpclsAAAWtExE-zKmt9zoBA_D9qDG_2FxmlzVLhxqVf_lp1YHvYAF1djLGonJHSICWxi9ll4JqciV5fNzWMY6FrmRA_IkbjiiMsGoKxS8eMvO7dhLGHAliUX3YKTpYe7F78ONI1a0KuKEmAQDTHtbP3FSorFa0LV7z0OKsNcuUH5E8gglSQihSgN2mJa5m8FJwXM7CH3Fv50zEfnMVcXDiC2WFgWW2sZ7BRIk75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر اینگونه عجیب رقم خورد تا چهره میثاقی بشه تراپی
- ساعت 00:30 اومد گفت اقا غنا کرواسی رو ببره رفتیم مرحله بعد؛ نتیجه؟ غنا بازیو باخت
- ساعت 03:30 اومد گفت اقا این دفعه ازبکستان نبازه ما صعود کردیم؛ نتیجه؟ ازبکستان بازیو باخت
- ساعت 05:30 اومد گفت اقا این بازی برنده داشته باشه ما تو جام می مونیم؛ نتیجه؟ بازی مساوی شد
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16055" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">1$ Tether = 171,000 Toman
@withyashar
🚨</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/16054" target="_blank">📅 10:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه هنوز برات عجیبه پس این کد رو ببین ، تیم جمهوری اسلامی   ۳مسابقه + ۳تساوی + ۳امتیاز + ۳گل زده + ۳گل خورده  + ۳گل مردود = ۱۸ , که میشه روز ا‌ول کشتار جاوید نام ها  درجواب رامین و قلعه نویی و اون کفتار شغال شلیل زاده  که قرار بود به جنازه…</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/16053" target="_blank">📅 10:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF0Q_bsxBkFqs-K1pEWOPS0Fezepg8MZv2VwIspmPZZdvLYKsblqPEGT6jP6u7oaVkyzUePD1V00zB5i9bzIhl9XrmomJnDxzOnVYlYf8Y9ZOtweohLtnhTK51X2IEE2H6bEx_SY7Th-IpyeP5DWrrhQrt_VLL37AtE14p_eL1UtUPCAgjyojiJP_JNXcz3hCiE3fnQmZxQ2fpJ6q7VwAyTECw7F4Mgp4Mi0CPYvTY8ovbhVcmYSgOmlWIrwZABbgb3insJRuvpG4RQKQtzG0ddLBPg90qcBRmYlO2Wk52BLOT_6I4K3uCNIceKb3RCw0oGlC8IXHnOuI3HGNUjqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی ارتش اسرائیل به الخیام در  جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/16052" target="_blank">📅 10:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه هنوز برات عجیبه پس این کد رو ببین ، تیم جمهوری اسلامی
۳مسابقه
+
۳تساوی
+
۳امتیاز
+
۳گل زده
+
۳گل خورده
+
۳گل مردود
= ۱۸ , که میشه روز ا‌ول کشتار جاوید نام ها
درجواب رامین و قلعه نویی و اون کفتار شغال شلیل زاده  که قرار بود به جنازه رهبرش تقدیم کنه
@withyashar
اگه شما نمیدونید ما میدونیم واسه چیه ویا اینکه چرا خدا باهاتون سازگار نیست
پاینده ایران</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16051" target="_blank">📅 10:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLDWegXplQgfkCl8j_tgKugvlEWrdPJs-oXfM_gsCCxPzqmroLUdHLo6pmEVgF1e7RJHMBebOId1MwvZuxvfbtWvFzrQN5XpMOKpAtR23b9TlqX8sp0JHg9OSS9aTbGk80x5gdReRL8Ghxl0tmQfM4VjrULRWLXDPjBzd9VgsHta_xKdQOvSyEA3OGPcF7MVI9F_ahTwaxtbzKARf23tHQHMQBBcGBhzHTffZCNJMvxd-YMfGU7dH9VvNHvq080YaLZeVCzI3bFs5-lCa-TwTDeJQqS_m1HPIEccb_2sztk2IvN7rC0iEDfyMYt_iTlwck44Z-rDzd2vcAe_cMkoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/16050" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
