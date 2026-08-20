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
<img src="https://cdn4.telesco.pe/file/V-IDURumeBKRfzRWD2XFEYpkC81_byU5ueuSUek1tmZ6q8Omaffbwo876uIg47sJedshZnnTZ3BSkELKc7iNMKaS8y4DA0b1-pUi8GamC7iEH4lN-bpVwpBfkunEwqN3fP5MW0wbLeHWBIZfDF0IS-pY-wiSDyjRtqXRclY65FS_hQMryS7b31KNg-qhlW0xNH_eVorMb3i7dx0CsyeePrK5eYi2ki4YpK2-xA4aCNg49P3vXkC7ZbeAI6ecd9SWG9WXNEb1XjPCMdO7qz1zpFMvY9--xco0OblMJDBicrRM2bFxRb0vTynrROP_81O7uAaQmCS2xdECmmdjOQwBQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 990K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 01:47:25</div>
<hr>

<div class="tg-post" id="msg-142944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd25da48a8.mp4?token=ivwBcJrMvsS39PqqcgJQuC5FFWbiciw1hZ9dVUGdSOyNnAKZaFvtwPY7A89LMgFYWhNujJdUe-G-1sc9wik-svGBFd5fykTZ4mqhn_CiHHJa31yHTjtByFBdwo6_-VurdZdxX-LVmSkYxX2vHYNNto90_OoqX0kwOHg2YcNbCj-ZjjtKrmSv0IOcsIr6xwM1gekcxs1D1zsSlLQbSFkqhCpJ3lJuh9JiD57rlZPtECCgYjQnGWATk2sK7rqoVMLl6Jv52ZL39Y2jdmG1RyKdfEKZUxRjxECbVY5mIjFsi0IxL6UNCSNVDUYaHFWWzpxrJgTAgrYGZ8EN5gQeo5MOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd25da48a8.mp4?token=ivwBcJrMvsS39PqqcgJQuC5FFWbiciw1hZ9dVUGdSOyNnAKZaFvtwPY7A89LMgFYWhNujJdUe-G-1sc9wik-svGBFd5fykTZ4mqhn_CiHHJa31yHTjtByFBdwo6_-VurdZdxX-LVmSkYxX2vHYNNto90_OoqX0kwOHg2YcNbCj-ZjjtKrmSv0IOcsIr6xwM1gekcxs1D1zsSlLQbSFkqhCpJ3lJuh9JiD57rlZPtECCgYjQnGWATk2sK7rqoVMLl6Jv52ZL39Y2jdmG1RyKdfEKZUxRjxECbVY5mIjFsi0IxL6UNCSNVDUYaHFWWzpxrJgTAgrYGZ8EN5gQeo5MOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیل دونه‌ای ۴۱ هزارتومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142944" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: روزانه ۱۰الی۱۵ میلیون بشکه نفت از تنگه هرمز(مسیر جنوبی) عبور میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142943" target="_blank">📅 01:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام دولت ترامپ:
ایران «کاملاً ورشکسته» است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند طی هفته‌ها و ماه‌های آینده با شدت بیشتری از آن‌ها استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142942" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142941">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190ed7396.mp4?token=kepKSY2QpM76JCAk1Der0cy9GuDGDT8MybPfDunk2c1MnlVKb6qvQ8ZGltp1hzXoOAnh-5Y8OZojzZY8MM7UBnxuQp1r_eCUVdmNiuzk_Re0LfbhBpMU9AShSHWMQkCBKODZnKYWJPX8LtUsQBlJGEhNdxpv0M1EE-n-8u2bw71VcR-abOWTkHsMSBz6V8v-_fPW-63dbdyuc5iExcTgCY7W9vl-SBCWnIJowanbNqCcVah2dsTLU4Mc2-etFV86rTux1-scsVoUJbmTyVreV1n52TRaLmoq2JAnKbEPxBMQvvRnQHw-winZvmxdQJQo8wZNqNSvBKNVp1CMW5aA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190ed7396.mp4?token=kepKSY2QpM76JCAk1Der0cy9GuDGDT8MybPfDunk2c1MnlVKb6qvQ8ZGltp1hzXoOAnh-5Y8OZojzZY8MM7UBnxuQp1r_eCUVdmNiuzk_Re0LfbhBpMU9AShSHWMQkCBKODZnKYWJPX8LtUsQBlJGEhNdxpv0M1EE-n-8u2bw71VcR-abOWTkHsMSBz6V8v-_fPW-63dbdyuc5iExcTgCY7W9vl-SBCWnIJowanbNqCcVah2dsTLU4Mc2-etFV86rTux1-scsVoUJbmTyVreV1n52TRaLmoq2JAnKbEPxBMQvvRnQHw-winZvmxdQJQo8wZNqNSvBKNVp1CMW5aA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏قالیباف، ۱۰ تیر ۱۴۰۵:
‏اگر به سوئیس نمی‌رفتم ۱۲ میلیارد دلار ایران آزاد نمی‌شد.
🔴
‏همتی، ۲۹ مرداد ۱۴۰۵:
‏یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/142941" target="_blank">📅 00:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142940">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpmwN1hcdMKFpX01s_ZXLQj_sX4RB1SDzIBBB_qEPXf5bSFWE1MDQ3Ao6gBmgeL7JmB_tWCwFE5upP5A55cYdzo1rnT0TxejEPcT3GJh7HiKU1xfDw5ApZZNsXFZogczxKiE91te6VRRCx5zhRIzLZ5anX26Ceg2Bp685K5UdSfGegKXjeBqBn_r96q17goJekMroK1rQ1CnkUo3x6xWFtvmLxhgIexYkY2WkqSoo0D5sgxuySv_XgMR-7mDp9UddDemspQ98M-aRveZWMgsg7K1cKZeCRaFuv1e2UERC-zV1rHxj8bsDivJasqET9a8bHJ0iPAuR47HkaEDsuv1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142940" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142939">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نشریه موندو: همسر رونالدو بصورت پنهانی با یک نفر دیگر در ارتباط بوده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142939" target="_blank">📅 00:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142938">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFf_Sskt3JIH0Af3Mv4PxDqf8bCJlBOYjFCtJfysAHsVTMr6Gn2s4TBwYNlImDiCf5SEdAVPi72Pe283usfEjxsgDbcISljPDH7LAQ6uB_4Dr6EwfbV6XTh7xekuq9PKyE7Ppsz1vKQC3OINm2fNX3naHglN3_BYcarENSeiOa7Yr2pBMDUDPrdbyU5AXwBF56-Eu4QUI7fdkfcvCPtKITMgKfp9vX5xZM8maY89hnVrpWq67QFPQBzdi2VEQprRaOEdpUjaR1aQhZ8GuPKDrnHzDRAmzvVOl_Cv2hiB_YE6XBfNItSQ2hshkZK8tgaK2gP3ZXmuWs7_xOFUK7tPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه موندو: همسر رونالدو بصورت پنهانی با یک نفر دیگر در ارتباط بوده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142938" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142937">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
الحدث: محمدباقر قالیباف از بغداد خواست تا به طور مخفی یا موقتا، سلاح های سنگین جمع آوری شده حشدالشعبی را به ایران متقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142937" target="_blank">📅 23:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
واشنگتن‌پست: آمریکا در حال بازنگری حضور نظامی خود در خلیج فارس است
🔴
واشنگتن‌پست گزارش داده پنتاگون در حال بررسی کاهش تعداد نیروهای آمریکایی در کشورهای خلیج فارس پس از جنگ ایران است.
🔴
بر اساس این گزارش، آسیب‌دیدن برخی پایگاه‌های نظامی آمریکا در منطقه فرصتی برای بازنگری در آرایش نظامی واشنگتن ایجاد کرده و ممکن است تأسیسات تخریب‌شده به وضعیت قبل از درگیری بازنگردند.
🔴
یک ارزیابی اولیه در وزارت دفاع آمریکا در حال بررسی این موضوع است که آیا بازسازی کامل پایگاه‌های آسیب‌دیده ضرورت دارد یا نه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142935" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سنتکام: یک فروند هواپیمای سوخت‌رسان KC-135 Stratotanker نیروی هوایی آمریکا، هنگام پرواز بر فراز خاورمیانه، به جنگنده‌های F-16 و یک فروند هواپیمای سوخت‌رسان KC-46 Pegasus سوخت‌رسانی هوایی انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142934" target="_blank">📅 23:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37134f889c.mp4?token=NNuHNmMsse0s6-rf02_hhNgfv9u_Wxv6AlnwoUdmwoRFYJLeWh1o6nhKHqmwT2z7B8bYEAUCXAgtQRuMNZqE48MDSHCR0Ih245iajDbw9DI3A5kiwG5QbjQeRB_Fwiw5vIw86YsaAVWttsuobEkPZcqg98Ik1zJw9H5bTW6YCoCl2RD7QmDMY9wcQ0ar-VkQ5a0r2W5WCpf3VoztF2Y1EJI-8buJbh1eUtA2-XLRp_4U5F8lloTDuFmO0k8u8QIDfk48HbJ-bOKHPHe9aX1mULRLPR5JOuLVOZvv4ocatsd2RUsehylcb8EYYMe7bWHf28mrc2VIGz14EZWUUhEmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37134f889c.mp4?token=NNuHNmMsse0s6-rf02_hhNgfv9u_Wxv6AlnwoUdmwoRFYJLeWh1o6nhKHqmwT2z7B8bYEAUCXAgtQRuMNZqE48MDSHCR0Ih245iajDbw9DI3A5kiwG5QbjQeRB_Fwiw5vIw86YsaAVWttsuobEkPZcqg98Ik1zJw9H5bTW6YCoCl2RD7QmDMY9wcQ0ar-VkQ5a0r2W5WCpf3VoztF2Y1EJI-8buJbh1eUtA2-XLRp_4U5F8lloTDuFmO0k8u8QIDfk48HbJ-bOKHPHe9aX1mULRLPR5JOuLVOZvv4ocatsd2RUsehylcb8EYYMe7bWHf28mrc2VIGz14EZWUUhEmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملانیا ترامپ: شنیدم که دلتان برایم تنگ شده بود. این منم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142933" target="_blank">📅 23:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7078093477.mp4?token=NDq_kRqAx_a1Y9U87T6WwRZ1YryakHA0q9mrOhzMMxKGhkZDVPaUcw7z5Q4esl_Xq0MoJTT9N_O0vxjbnp_zA9xubTpoaUEHcNc-0S-67lGUEo5IQ6kdNuEDWRVlZuXQX5Me19VTekEhIfpSsApzQXIlrbNqp6yxD2X-etFoUx5wnD9Lf_XVTVWVTDGQgobuPE29_JvW1HebDTQ866HxZXLFdAr6bQV4AHevkSfREzusa787xh23xaPwhf972jwX9h5hfcTk5MDCBL4VLbTfQhg-q1WNDtriy3ayhq_hb51p8wUzqtEcLJV6yjDlYTTld-mAXIx4vDNlRzx0EcETWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7078093477.mp4?token=NDq_kRqAx_a1Y9U87T6WwRZ1YryakHA0q9mrOhzMMxKGhkZDVPaUcw7z5Q4esl_Xq0MoJTT9N_O0vxjbnp_zA9xubTpoaUEHcNc-0S-67lGUEo5IQ6kdNuEDWRVlZuXQX5Me19VTekEhIfpSsApzQXIlrbNqp6yxD2X-etFoUx5wnD9Lf_XVTVWVTDGQgobuPE29_JvW1HebDTQ866HxZXLFdAr6bQV4AHevkSfREzusa787xh23xaPwhf972jwX9h5hfcTk5MDCBL4VLbTfQhg-q1WNDtriy3ayhq_hb51p8wUzqtEcLJV6yjDlYTTld-mAXIx4vDNlRzx0EcETWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر مصطفی مهرآئین:جمهوری اسلامی برای اینکه بمونه، کشور و تاریخ و دین رو نابود کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142932" target="_blank">📅 23:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=PJRyRNXrNEikIMCkEx6zorgrw-kAla4UHSIama3L0LO6S4wuFpu_MsmOmYCLgB_dNR2r4cHnONdVfr0yRkfS2pujRwebDQg-VqdlWN3sh-XinALBQXierWoNfulOksE40G02fnOpK2l-PdnefuchMPG5xLuUm5lvBjw6d9sXn7yX3jEXuOg-bbrThQNWGHKI-NH0zN6Z4fteYEhFyRR5yjTjjgInGyrsC8Rek2QF67AHIebPMKcdkZN1_CiXgb4NgpllxuNhTh9eomghnXYUrjj28rDYx8GF54x3DM6e52aXvsbGwyXPcrRAJMRMTke_eYYvEvwqztNfzNgl_C77Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9209031f2e.mp4?token=PJRyRNXrNEikIMCkEx6zorgrw-kAla4UHSIama3L0LO6S4wuFpu_MsmOmYCLgB_dNR2r4cHnONdVfr0yRkfS2pujRwebDQg-VqdlWN3sh-XinALBQXierWoNfulOksE40G02fnOpK2l-PdnefuchMPG5xLuUm5lvBjw6d9sXn7yX3jEXuOg-bbrThQNWGHKI-NH0zN6Z4fteYEhFyRR5yjTjjgInGyrsC8Rek2QF67AHIebPMKcdkZN1_CiXgb4NgpllxuNhTh9eomghnXYUrjj28rDYx8GF54x3DM6e52aXvsbGwyXPcrRAJMRMTke_eYYvEvwqztNfzNgl_C77Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده سابق نیروهای ویژه ترکیه، زکای آکساکالی: اسرائیل نمی‌تواند با ما رقابت کند.
🔴
ما مانند سایر کشورها نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142931" target="_blank">📅 23:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7390372dac.mp4?token=ubYIyAWuBQlaBjg4_LTaBJspJ14phOnOtYjPD4LrH6GIJejwNBHxkS9LsJFnhFWzdr0Iiu66MHPLJ_jhjsVfj00aKf_bd7p3mQAakJGNr4hvAxmYWp7WD2WdFzs6SdF4C8GfDhb81wlM7Z0aw3tfU-4eRLCuPg6IJA35n2R3M8RvwLvVDOxi9tbqtAwI11-tnYPBSFDs_M-_KBft4Vo2uZ7pvyFYH6FSxdkpCUugAVrCS7Nq8ruBzMnP1YHXs_4THhnVsHi7cG9ixRwUooW--9ZnESgI4UXKJx68Lapw7G5yuOYb9URB8W7dM3t6Ul9BvdqoNHG2mDEUDLfANnXyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7390372dac.mp4?token=ubYIyAWuBQlaBjg4_LTaBJspJ14phOnOtYjPD4LrH6GIJejwNBHxkS9LsJFnhFWzdr0Iiu66MHPLJ_jhjsVfj00aKf_bd7p3mQAakJGNr4hvAxmYWp7WD2WdFzs6SdF4C8GfDhb81wlM7Z0aw3tfU-4eRLCuPg6IJA35n2R3M8RvwLvVDOxi9tbqtAwI11-tnYPBSFDs_M-_KBft4Vo2uZ7pvyFYH6FSxdkpCUugAVrCS7Nq8ruBzMnP1YHXs_4THhnVsHi7cG9ixRwUooW--9ZnESgI4UXKJx68Lapw7G5yuOYb9URB8W7dM3t6Ul9BvdqoNHG2mDEUDLfANnXyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره کشته‌شدن چارلی کرک
:
من میل به نپذیرفتن روایت رسمی را درک می‌کنم، اما اگر وارد مسیری از تئوری‌ها و گمانه‌زنی‌ها شوید که در نهایت شما را به حمله به
اریکا کرک
برساند، باید بگویم تنها کاری که می‌توانیم انجام دهیم این است که به غرایزمان و در عین حال به عقل و منطقمان اعتماد کنیم.
🔴
من اریکا را می‌شناسم. او انسان بسیار خوبی است و اکنون تلاش می‌کند دو فرزندی را بزرگ کند که به‌تازگی پدرشان را از دست داده‌اند. او واقعاً سزاوار حملاتی که علیه‌اش صورت گرفته نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142930" target="_blank">📅 23:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=oBM0gdfCVRsHSquZ42gN-hrPH5tVNvC1ZyYa6zVbgMzjOMzr9WDvXmg5TSwNG1FLDPOLIaEL_5LRx7zrHURqoktG5YlxWbCi8fg48GHd3BOAmajxkqyX29B6GCaDTr9oiOYOk5UI_WXXmWF7kiaW-qrGyKop0rRyzRDpCahC-x4wnVU85-5uE11YslKekpHIww-TcdBGcUNaJ4PATHTeBfsoTiJwzv5NEkBXt1sJCYq-__XclXrey8SQtei1ZTq9to0p7xq5b02UBbeqh1z5bS-BU_e6yhWUKtxFXMpX6yn5nfgJHWgIZrQpUoGCId8Ifq9oQfIBa7rVe0Cy42rwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=oBM0gdfCVRsHSquZ42gN-hrPH5tVNvC1ZyYa6zVbgMzjOMzr9WDvXmg5TSwNG1FLDPOLIaEL_5LRx7zrHURqoktG5YlxWbCi8fg48GHd3BOAmajxkqyX29B6GCaDTr9oiOYOk5UI_WXXmWF7kiaW-qrGyKop0rRyzRDpCahC-x4wnVU85-5uE11YslKekpHIww-TcdBGcUNaJ4PATHTeBfsoTiJwzv5NEkBXt1sJCYq-__XclXrey8SQtei1ZTq9to0p7xq5b02UBbeqh1z5bS-BU_e6yhWUKtxFXMpX6yn5nfgJHWgIZrQpUoGCId8Ifq9oQfIBa7rVe0Cy42rwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران
:
باید به نقطه آغاز برگردیم. رئیس‌ جمهور گفت ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
🔴
تأسیسات هسته‌ای آن‌ها نابود شده، اما سؤال این است:
آیا تلاش می‌کنند آن‌ها را بازسازی کنند؟
🔴
بنابراین، اساساً کاری که ما می‌خواهیم انجام دهیم، ایجاد یک واقعیت جدید در میدان است؛ به‌ گونه‌ای که نه‌تنها بتوانیم با اطمینان بگوییم تأسیسات آن‌ها نابود شده، بلکه بتوانیم با اطمینان بگوییم هرگز برای بازسازی آن‌ها تلاش نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142929" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2a22dac6.mp4?token=CkfP-m6wRJwsks_bL5VP3iMmVyEbKbdDuopUztrs_UxCWsZBk9n9VpgItqzG9_pad6qz_eIPrLkMrG2_-lw0yL-64SecvaFzuvlfSuhC0yjvr8I2Qhj_FPHo5wAPZLg2d332GfudxQINRN9C_5vwIqZsxm4T9o0JQptnvzrTv5P_Z2CzxlX3DprfT8ZYeTpB491OKkCaOCRbc4yihggGx6Q3E2NrCb2VBjwxocdjQbqBiiD89D1yXo0HDoj5KUQXVXFAF7Jm0BwXFG11oAD1e1Mh9Me-P5HasfRyuvhcDFeBdWWogIIofo39wvGKeaaZzr7wH9CiP_V_6JkglhVd8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2a22dac6.mp4?token=CkfP-m6wRJwsks_bL5VP3iMmVyEbKbdDuopUztrs_UxCWsZBk9n9VpgItqzG9_pad6qz_eIPrLkMrG2_-lw0yL-64SecvaFzuvlfSuhC0yjvr8I2Qhj_FPHo5wAPZLg2d332GfudxQINRN9C_5vwIqZsxm4T9o0JQptnvzrTv5P_Z2CzxlX3DprfT8ZYeTpB491OKkCaOCRbc4yihggGx6Q3E2NrCb2VBjwxocdjQbqBiiD89D1yXo0HDoj5KUQXVXFAF7Jm0BwXFG11oAD1e1Mh9Me-P5HasfRyuvhcDFeBdWWogIIofo39wvGKeaaZzr7wH9CiP_V_6JkglhVd8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران
:
ما اکنون تا حدی در مرحله جدیدی قرار داریم که در آن مؤثرترین ابزاری که در اختیار داریم، فشار اقتصادی است که می‌توانیم بر آن‌ها وارد کنیم.
🔴
و این یک رقص ظریف است، زیرا ما فشار اقتصادی بر آن‌ها وارد می‌کنیم. آن‌ها نیز سعی خواهند کرد فشار اقتصادی بر ما وارد کنند.
🔴
اما آنچه در چند هفته گذشته صادق بوده است این است که آن‌ها فشار بسیار بیشتری نسبت به ما احساس کرده‌اند.
🔴
ما این روند را ادامه خواهیم داد، زیرا معتقدیم این بهترین راه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142928" target="_blank">📅 23:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0441732671.mp4?token=NmK1Wd4-3T8GMpwcqFtt_ofX7Myn-9bqaEdQjtTBAlk-5HpvNrc-qMzr9E6tVkRV7kdaGX1f79RbAwNI51NiZpFpHcXYPRDQI40YB-cKnl04U3v1zkgGHpqKjO0zPlD4XpXxSN-C3eVPvxY44ehPns7STQbbieXr0jKKfdRl7VIPnWWTQAQj4rhIc5PiJVFeqP1LteYddvac0Nlf7N_QOZVbtmgUP34iEgrBhOai1HHwo-fz1tonZY-uJv5IFNQH31vttqdSq0VsRbp4ng4PdbqXmEd4Tp2HJdGq-i5eXV_NUn9Yulhc3GPA683j7_TmUx-Soca5VYvSLGqP040HhHycz9WiVbJLm6PJ3T8HAAP0TNlYPTmr5JY1YrbQnuVnwUOtQmqOiYGjSRbwNO7kP2uzRV8EmwxAjtK4CH5qjlp3--PD53pO9HUU7qfjS092Rfvxks9NZW8kaOSamf9XRTjHV02LGTHIhN-LcvBkVfVg52H-gjmeR1SJNYJU0z8ER4SGG_QNNY-5OK_dVlZhHuXVVoAUARlsqciUHAJltt3Jt5viCoLwTGnBKB2i_Yv5ajw7yP2gmF-4_TUhWPPs10injfsPHgPX5MD4LcuEjhKe2iOPlDdd9YU3oWboaeo0FIdSe_f9KIMzs9PYNnhbgYygo6c84RHx7xopkXmoggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0441732671.mp4?token=NmK1Wd4-3T8GMpwcqFtt_ofX7Myn-9bqaEdQjtTBAlk-5HpvNrc-qMzr9E6tVkRV7kdaGX1f79RbAwNI51NiZpFpHcXYPRDQI40YB-cKnl04U3v1zkgGHpqKjO0zPlD4XpXxSN-C3eVPvxY44ehPns7STQbbieXr0jKKfdRl7VIPnWWTQAQj4rhIc5PiJVFeqP1LteYddvac0Nlf7N_QOZVbtmgUP34iEgrBhOai1HHwo-fz1tonZY-uJv5IFNQH31vttqdSq0VsRbp4ng4PdbqXmEd4Tp2HJdGq-i5eXV_NUn9Yulhc3GPA683j7_TmUx-Soca5VYvSLGqP040HhHycz9WiVbJLm6PJ3T8HAAP0TNlYPTmr5JY1YrbQnuVnwUOtQmqOiYGjSRbwNO7kP2uzRV8EmwxAjtK4CH5qjlp3--PD53pO9HUU7qfjS092Rfvxks9NZW8kaOSamf9XRTjHV02LGTHIhN-LcvBkVfVg52H-gjmeR1SJNYJU0z8ER4SGG_QNNY-5OK_dVlZhHuXVVoAUARlsqciUHAJltt3Jt5viCoLwTGnBKB2i_Yv5ajw7yP2gmF-4_TUhWPPs10injfsPHgPX5MD4LcuEjhKe2iOPlDdd9YU3oWboaeo0FIdSe_f9KIMzs9PYNnhbgYygo6c84RHx7xopkXmoggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس
: اگر بتوانیم مقدار کافی نفت و گاز را به بازار برسانیم تا برای برخی آمریکایی‌ها در قیمت بنزین و هزینه‌های انرژی کمی آسایش ایجاد شود، در همین حال، ایرانیان به دلیل شلیک به کشتی‌های تجاری تنبیه می‌شوند.
🔴
این کار فشار اقتصادی زیادی به آن‌ها وارد می‌کند و محاسبات آن‌ها را در مورد نوع توافق یا چیدمانی که می‌خواهند با ایالات متحده آمریکا داشته باشند، تغییر می‌دهد.
🔴
آیا می‌خواهند اقتصادشان برای همیشه خفه شود یا می‌خواهند رابطه بهتری با غرب داشته باشند؟
🔴
همیشه این گزینه‌ای بوده که رئیس‌جمهور به این افراد ارائه کرده است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142927" target="_blank">📅 23:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تانکر ترکرز: دلیل اینکه دیگر در خارک شاهد بارگیری‌های زیادی نیستیم، این است که تولید نفت خام ایران در ماه‌های اخیر به سطحی کاهش یافته که فقط اندکی بالاتر از میزان مصرف/پالایش داخلی این کشور است. این یعنی ایران در حال حاضر فشار چندانی برای صادرات نفت ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142926" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=KgXqqLx6R3KcmvzfwtatNnN59I3G7OqZiBYeh2pFDwz3nXOLcZ8XuDhoq2CUV0Uxy5TbSvZj0rzx3Ejy8ljbzEajGXwf6azltzdrKpNlmUp2MnyuQtJEoL5fEdClVGilHj65nt8iGDSbcX6LlFzxtioV4XGkh6dSR_99hOTVaWVMk2PKsgyTWm8fI22_AHeHADEUuylXa5BrNJydAGQf6un2BeIsVFH4Uqmp-CeBRHhL8Rn5HaJWdlp0RjKjHNY6D0VIlA0hblfmBzL_wC2P7j7wX9Tz4kb2_AMAz3O8H0MPuiyeQd1sTOAeGFGd7pDVj0G4IzTg_CJNSJSuv6rZ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c71e411fb.mp4?token=KgXqqLx6R3KcmvzfwtatNnN59I3G7OqZiBYeh2pFDwz3nXOLcZ8XuDhoq2CUV0Uxy5TbSvZj0rzx3Ejy8ljbzEajGXwf6azltzdrKpNlmUp2MnyuQtJEoL5fEdClVGilHj65nt8iGDSbcX6LlFzxtioV4XGkh6dSR_99hOTVaWVMk2PKsgyTWm8fI22_AHeHADEUuylXa5BrNJydAGQf6un2BeIsVFH4Uqmp-CeBRHhL8Rn5HaJWdlp0RjKjHNY6D0VIlA0hblfmBzL_wC2P7j7wX9Tz4kb2_AMAz3O8H0MPuiyeQd1sTOAeGFGd7pDVj0G4IzTg_CJNSJSuv6rZ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سانحهٔ هوایی مرگبار در آمریکا
‏
🔴
برخورد بالگرد پلیس با یک هواپیمای کوچک در فرودگاهی در ایالت پنسیلوانیای آمریکا، یک کشته و ۲ زخمی برجای گذاشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142925" target="_blank">📅 23:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏
👈
شریعتی نماینده مجلس: نزدیک ۸۰ درصد قاچاق سوخت مربوط به گازوئیل است، نه بنزین
‏
🔴
رئیس ستاد مبارزه با قاچاق کالا اعلام کردند روزانه ۲۰ میلیون لیتر سوخت قاچاق می‌شود که ۸۰ درصد آن گازوئیل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142924" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
👈
ونس: تنگه هرمز اصلی‌ترین اهرم فشاری است که تهران در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142923" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
به گزارش i24NEWS، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در جلسه‌ای امنیتی با حضور رؤسای نهادهای دفاعی و اطلاعاتی، درباره سناریوها و تحولات احتمالی پیش‌رو گفت‌وگو خواهد کرد.
🔴
تمرکز ویژه این جلسه بر تحولات سوریه و افزایش تنش‌ها با ترکیه خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142922" target="_blank">📅 23:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1be81d77a.mp4?token=ufJdUJPz9RzmUhS2w6MTvOWgrr0JewMrtKZ9E2BB6UvThQf5G4B3F90rSX-hLzy8RgYevpOpff1rDYDcc6yZTyk_jVKx1x3t2PB9iesn41YtBTuVgjll0m3tuJy2Pb3Ke_TPIf36pGsjjAZS-xpRsktaJ3D1r6GD_vBLblG5sO0dS3GgdrwTlZOmLtGzyzjEC1S6giYFZ4HM9IIElZeCfF53IQqn8DZwdwJqR9vTWtX_Oo6VaxFm157q5q4tPrDjbTx-kJrBCO3pVA_9HGcCW84Obi35Op3R8GLGGhy-_6G-mRmLJXFpZVUC3YyMFRy7cQTV2ppeDb42WYZjFJlIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1be81d77a.mp4?token=ufJdUJPz9RzmUhS2w6MTvOWgrr0JewMrtKZ9E2BB6UvThQf5G4B3F90rSX-hLzy8RgYevpOpff1rDYDcc6yZTyk_jVKx1x3t2PB9iesn41YtBTuVgjll0m3tuJy2Pb3Ke_TPIf36pGsjjAZS-xpRsktaJ3D1r6GD_vBLblG5sO0dS3GgdrwTlZOmLtGzyzjEC1S6giYFZ4HM9IIElZeCfF53IQqn8DZwdwJqR9vTWtX_Oo6VaxFm157q5q4tPrDjbTx-kJrBCO3pVA_9HGcCW84Obi35Op3R8GLGGhy-_6G-mRmLJXFpZVUC3YyMFRy7cQTV2ppeDb42WYZjFJlIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا : «ما اکنون وارد مرحله جدیدی شده‌ایم که در آن، مؤثرترین ابزاری که در اختیار داریم، فشار اقتصادی است... ما به اعمال این فشار ادامه خواهیم داد، چون معتقدیم این بهترین راه برای دستیابی به هدف نهایی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142921" target="_blank">📅 22:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS_OJL44NnyMxHiaLbAlGbJtA5VRhpBwHC9IBh4L5_LM4Z3xdslArnqPzeYvrfw3K2ki3xguXPE_dK4iOlZw83-9PMX9wo2_UMV7tDGlQAVRhXhdai2-zmFqOuIGL-ROLHnzchT7kM5kuKOcpn8VYdlxjRtvfpX5KU1vlZ1ELNtnI9w1L11LaN0vM6TPOulCan74AYFMO97ChQc8SlaJkv7kOkGawz6eRxuOSnOLSacSyLaT0bsqoTea07l84p2A9fi58vaYMKYP87Eg_G-KafzbCoksG0aA2ZnP3m31j9R8GUrIWXyfC4vA_4IYzA8jHSxy_sS9jkYF94KcuxhxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو آبراهام لینکلن، روز پنجشنبه پس از استقرار ۹ ماهه سفر خود به سن‌دیگو آمریکا را آغاز کرد؛ این ناو که بیشتر از عملیات ایالات متحده علیه ایران پشتیبانی می‌کرد، اکنون در راه خانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142920" target="_blank">📅 22:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS6K7QI14iFcrZYD59rka-CaLspYl4dom-jkRQnyihvLaizw6NVhIppPodNmY_w3JOvCY947WJiDtjw4w_NZxJY1TXODkwdgK9WcP_gO8cAljJlsk-dSE4FxaVRUcncck0MWiZv_LKLHRWVlO6CRY6cpy4F_XqOhJqIuavp_lvVxtP4UfMBss57lQe6WcWrGySzHLwVwX2QJphwVDfdJ0rla7EArYKdvVxWbNPA44cjUTvfK6GzdL7_yfQ29hjJ2qFnWRyUB63CYT4lsrJXBg5WDbJS4kkhA19MK-BFkquzx-DNiZVLMPtpSUK0jE1VqhAMr53WquNK5zPEZDW4JDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
گفته میشه که جورجینا تو مراسم عروسیش با کریستیانو رونالدو ، بیشتر از "55 میلیون دلار" جواهرات الماس به تن داشته
@AloSport</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142919" target="_blank">📅 22:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
قیمت مسکن منفجر خواهد شد
⁉️
این تحلیل ترسناک رو ببینید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/142918" target="_blank">📅 22:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یک زن به اتهام تلاش برای بمب‌گذاری در ساختمان کنگره ایالتی نیویورک، پیش از اجرای عملیات توسط FBI بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142917" target="_blank">📅 22:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1609ea76.mp4?token=jWlOIevMv_jGaRYxHltEEDxkKq4D5Ampk-AeHnW6-r91th7DAeQg7fmzzv4420mJVIZ7_Xo_cEXyCAlhaWVvHECEWZwBX6Zz_r1tF1chZwR8ETohGhwkGcpjEMBuTjrvMe4P1EXtzoNRQl1R0Q61E1QiF-nWVkUgztwcHEBGGG7_dIxv0ACswZnR8LuPerBfYNvmuOcf-Blqphg-QoJxKPGDYPQNjqqdJw1eD_Ioo228eFYYG08xrdDYrZEdK5jXnywultf4kOn7JLo5ITDtwe_WQ3nfdMWU3Ds-gekKvIG-F5IcGBbXG_4kNUYNw3LxNOhtt1RWFBykm-clIm77zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1609ea76.mp4?token=jWlOIevMv_jGaRYxHltEEDxkKq4D5Ampk-AeHnW6-r91th7DAeQg7fmzzv4420mJVIZ7_Xo_cEXyCAlhaWVvHECEWZwBX6Zz_r1tF1chZwR8ETohGhwkGcpjEMBuTjrvMe4P1EXtzoNRQl1R0Q61E1QiF-nWVkUgztwcHEBGGG7_dIxv0ACswZnR8LuPerBfYNvmuOcf-Blqphg-QoJxKPGDYPQNjqqdJw1eD_Ioo228eFYYG08xrdDYrZEdK5jXnywultf4kOn7JLo5ITDtwe_WQ3nfdMWU3Ds-gekKvIG-F5IcGBbXG_4kNUYNw3LxNOhtt1RWFBykm-clIm77zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
شریعتی، نمایندهٔ مجلس: ۶۹ میلیون ایرانی خودرو ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142916" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142915">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzHVYdZlDniooaLxepX9_kLnL7lzFVVOP_oOontoLMhbHmL36OMImfDva9Da7rqu6CpAoSUWDmDJRdKg67LbM_hq9_dy4N16Gxl-d9J8ScykbeUymzDniD-Nl5PiqIhE9SYF8DdSvMGRScMPUqXIw0f091Kpc-TFXc8MbBkMGqUkovaUXVYjv0TMQhyHmRnhy6NiITJHQf7nbEfdTRs_mk3WRryMM1q2QaXIK4PrWQ62t2AxDHJnHS09v245TbjTHBdwYz_1mXIxZVgmBLdorum1Fp9OCg1BwWVdPOPNsMXZLSbzK_f7nyxglAy0k0bWFOcn9KS2RR2Uat-xDBUG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس: در شبکهٔ نمایش خانگی با بازی «نون بیار کباب ببر» لمس نامحرم را عادی‌سازی کردند و امت معکوس حشری شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/142915" target="_blank">📅 22:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142914">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش‌ها از وقوع حادثه دریایی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142914" target="_blank">📅 22:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142913">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1269f75683.mp4?token=NaUpneuqZsCQAlO5duam09YqLhQcgpWr1n8ca4JGYtxmaVCnLopS8nkB3FIvFGIy5SUsahRdPLeOpTWGfQQqdi8fyQ12M35lI8zmQbJf1P03EFHSxNhobscodcJ_O62G_o7CSnuWEVOHDqhsuKqqLUxabnzoJt2VfeIzPf8CYDbo39nDZ0tJc54bL3NiUOh-incJB3VQbRRzoHqCRmTN19WdtM3R3kxvMZR1Pv29GuUVWbHL6WXwMF5h0ziln8Wj6YnznIJkS0S9Ez2UPv0PMjLody_wZMhH8_XPgiBcwvRRMJjn9HNxc9x7g4QSvIXAb6BjBVbcVqalJs0N9mSAPr6FExXAhXQkwFA4fC6OIWRoh1USwZeIyIvHE4ToNHy5fM5-ltV8_HFfZYEiJpGOzMYnjsRafApWbuh7x6ohOJiSTYSBL_RVlkSEaTWtS2fNVvsaXEs6cwktj4bgujvYQw2cUcXDfkT7vpUb2_su91kccsUG1AtDVehxcKTwobUFgWREYeyl_oLIZYrb0vqKVQwk6dC2CgwReXtJhploMVJjiaJorveICA9qUligH2YWDBgI4aCerQytztQQuPU-ifyQSqMk5rg4cGqs3fUFBrcwbS1Pfvx2QzPcyXzzT_aRwbGPos8i2dMJdb7alX_lPSGOfmvsg0q0RMosqVPPrmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1269f75683.mp4?token=NaUpneuqZsCQAlO5duam09YqLhQcgpWr1n8ca4JGYtxmaVCnLopS8nkB3FIvFGIy5SUsahRdPLeOpTWGfQQqdi8fyQ12M35lI8zmQbJf1P03EFHSxNhobscodcJ_O62G_o7CSnuWEVOHDqhsuKqqLUxabnzoJt2VfeIzPf8CYDbo39nDZ0tJc54bL3NiUOh-incJB3VQbRRzoHqCRmTN19WdtM3R3kxvMZR1Pv29GuUVWbHL6WXwMF5h0ziln8Wj6YnznIJkS0S9Ez2UPv0PMjLody_wZMhH8_XPgiBcwvRRMJjn9HNxc9x7g4QSvIXAb6BjBVbcVqalJs0N9mSAPr6FExXAhXQkwFA4fC6OIWRoh1USwZeIyIvHE4ToNHy5fM5-ltV8_HFfZYEiJpGOzMYnjsRafApWbuh7x6ohOJiSTYSBL_RVlkSEaTWtS2fNVvsaXEs6cwktj4bgujvYQw2cUcXDfkT7vpUb2_su91kccsUG1AtDVehxcKTwobUFgWREYeyl_oLIZYrb0vqKVQwk6dC2CgwReXtJhploMVJjiaJorveICA9qUligH2YWDBgI4aCerQytztQQuPU-ifyQSqMk5rg4cGqs3fUFBrcwbS1Pfvx2QzPcyXzzT_aRwbGPos8i2dMJdb7alX_lPSGOfmvsg0q0RMosqVPPrmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از منطقه آیاکوچو پرو هنگام وقوع زلزله.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/142913" target="_blank">📅 22:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142912">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
صحنه‌هایی از منطقه آیاکوچو پرو هنگام وقوع زلزله
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142912" target="_blank">📅 22:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142911">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
به گزارش سازمان زمین‌شناسی ایالات متحده، زلزله‌ای به بزرگی ۶.۷ درجه اخیراً پرو را لرزاند.
🔴
مرکز زلزله در منطقه آیاکوچو قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142911" target="_blank">📅 22:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142910">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:ما باید نفت بیشتری را از طریق تنگه هرمز عبور دهیم، زیرا این همان اهرم فشاری است که ایران در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142910" target="_blank">📅 22:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142909">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_ch0lyzPIHtvM60ab3IK9mtmalh_47Ip3ZP9WEzadUyIdef0AsyeWiX7csSphj8MGGQ7vZHylAeE4A7-3WUZPUYKq7eUJ5fQiXsZxwkZBfA412XPGzH0j1-CnTZ9-QY43AX6Y7DXGMzcfI2_E84COVekcp2rTZ5brGw4f-wWjY7_4VvdfTLcctSgqctyGotsshufL4BSaULpTR9oG21lcSABlYp9mrILL5BpehqY9NF_eQaMbV83ZehbaVjBkUSOojlr404OgSh3ouKbfxJnbGpV_AsYnTkiSzcB7LInwT4h4raZaa2FPXVeExZ-CtmTaCeMRG09qxKbJUZCqn38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانوارهای ایرانی‌ چند خودرو دارند؟
‏
🔴
️۳۴.۵ میلیون ایرانی خودرو ندارند، ۴۰ میلیون ایرانی یک خودرو و ۱۴ هزار ایرانی ۱۰ خودرو و بیشتر دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142909" target="_blank">📅 22:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142908">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
الجزیره: قیمت نفت پس از تهدید آمریکا به اعمال تحریم علیه ایران افزایش یافت
🔴
بهای نفت برنت با ۲ دلار و ۲۰ سنت معادل ۲.۴ درصد افزایش، در ساعت ۱۵:۳۶ به وقت گرینویچ به  دلار در هر بشکه رسید. نفت خام وست‌تگزاس اینترمدیت (WTI) آمریکا برای تحویل سپتامبر نیز با ۲ دلار و ۳۳ سنت افزایش، به  دلار در هر بشکه رسید.
🔴
هر دو شاخص به بالاترین سطح خود از ۲۴ ژوئیه رسیدند و برای پنجمین جلسه معاملاتی پیاپی افزایش قیمت را ثبت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/142908" target="_blank">📅 22:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142907">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
حاجی بابایی نایب رئیس مجلس:
کشورهای حاشیهٔ خلیج فارس تو کشور خودشون نباید خط لوله بزنن برای انتقال نفت چونکه اینجوری خاصیت تنگه هرمز رو کم میکنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142907" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142906">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
مظلوم عبدی فرمانده نیروهای دموکراتیک سوریه، ادغام نیروهای دموکراتیک سوریه و نیروهای آسایش در وزارتخانه‌های دفاع و کشور سوریه را تکمیل شده اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/142906" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142905">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر خارجه عمان: عبور ایمن از تنگه هرمز به امنیت و شکوفایی کل منطقه مرتبط است
🔴
وزیران خارجه عمان و ژاپن بر ضرورت تشدید تلاش‌های بین‌المللی برای تضمین آزادی کشتیرانی در تنگه هرمز مطابق با قوانین بین‌المللی تأکید کردند. وزیر خارجه عمان تأکید کرد که عبور ایمن از تنگه هرمز از امنیت و شکوفایی جدایی ناپذیر کل منطقه  است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142905" target="_blank">📅 22:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142904">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
زمین‌لرزه ۶.۶ ریشتری مرکز پرو را تکان داد
🔴
یک زمین‌لرزه شدید، بخش‌های مرکزی کشور پرو را لرزاند. لرزش‌های این زلزله در مناطق وسیعی از این کشور احساس شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142904" target="_blank">📅 21:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142903">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Q2wvyrS8vj4E68qLsVisoQhwtqIqsCwW95t66fCNnHqxULNr0ePRt0tyyhFsJuHUUQFHVfcsbSO54Hn4P23Yl4ZdOgnnzKAgYRZz3uy9G1m5qBU74WGbweIrKR4I1kWFGW4Gt9Y1IZkKtZ4W6b8IEJ2x5DYgPgv9G0g-ltXkz_dyNqnthzQLAUQS2M2WnbROZ1IcbphXdgWZPrmYUmPiXMNmNrBK-aHiwx5ICNqgjH1R3hDh_-gms-y5vJfwqRA-TbPGcApbmDNZZOgS7NW-83iiY5Jbi7HYtI-gPMRpUpdxsdrDe1vZc-w7usl-QYHYNPzRMUuo-toQrxjShvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طارق صالح، معاون ریاست جمهوری یمن: تشدید تنش های اخیر از طرف حوثی ها مستقیما از سپاه پاسداران در ایران نشات می گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/142903" target="_blank">📅 21:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142902">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
گردان‌های "جنوب"، که با شورای سیاسی یمن (PLC) همسو هستند، تصاویری منتشر کردند که نشان می‌دهد تک‌تیراندازان آن‌ها در حال تمرین با استفاده از تصاویر برش‌خورده از عبدالمالک الحوثی، رهبر عالی‌مقام ایران، مجتبی خامنه‌ای، و سایر فرماندهان حوثی (أنصارالله) هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142902" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142901">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777ea22755.mp4?token=uO5i15ctxcWOvJuNk8daAkkh0B6QTvmKs-10Z4J53DEbyryvmh-ZR5kjRi75kNqitWydxuX5-PcS0XlbpwXz7ZAN7kugsIJpQQo0BxKcYrAYmQPuf-uqxmtRu8q_VFcQp0dTKofFljTm6iB-5lxpmokh6vdBYsvxOrMAwv2WaN3MXTAA3zphhx_b9FPkWkDEMlpXHzCYZ_hrnsD-b92omMKkHD4nmmotpInPIBEn6yl04GChj6gU4GiCGpBPV1Gl-tOAGnJN4gArkTKakyj6OSFTs4wbJZbVvYRG6cpY-W3iLYinnZ1hAgdGXbMqMkQLLIkqJ8Yq7wsOGoA4JsEbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777ea22755.mp4?token=uO5i15ctxcWOvJuNk8daAkkh0B6QTvmKs-10Z4J53DEbyryvmh-ZR5kjRi75kNqitWydxuX5-PcS0XlbpwXz7ZAN7kugsIJpQQo0BxKcYrAYmQPuf-uqxmtRu8q_VFcQp0dTKofFljTm6iB-5lxpmokh6vdBYsvxOrMAwv2WaN3MXTAA3zphhx_b9FPkWkDEMlpXHzCYZ_hrnsD-b92omMKkHD4nmmotpInPIBEn6yl04GChj6gU4GiCGpBPV1Gl-tOAGnJN4gArkTKakyj6OSFTs4wbJZbVvYRG6cpY-W3iLYinnZ1hAgdGXbMqMkQLLIkqJ8Yq7wsOGoA4JsEbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور، جِی.دی. ونس، اساساً دولت جو بایدن را مسئول افزایش بدهی ایالات متحده به ۴۰ تریلیون دلار می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142901" target="_blank">📅 21:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142900">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رئیس جمهور پزشکیان: شرایط ناشی از ناترازی‌ها به دلیل آسیب‌ های ناشی از جنگ، موجب افزایش فشار بر صنعت برق شد
🔴
سیاست دولت، استمرار تأمین برق صنایع و جلوگیری از توقف خطوط تولید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/142900" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cce6c887b.mp4?token=sOmAriS-T5Fq5B9X7lgTiZ38nUeaDXfCGZYovkmJF1Qr7lsJkRtGQeKrafNMqL4xGg0Xo1P4hX2qi1J4l6oaQQPJa-6QJSKNZ5Jxz_x24CvfJkZYMs2l1_BPOy4XlBiFNeXhlOYkWGWV7aD5orj2X0PYtFYG_JFnZcMWqQTjE2X6m5w2XwnoAjaBhBfgzN2n-TpFR63pQ5hBqm83DjCWQX-NqJ55Ua-85WGPXJIf6GTHz5mnPSCZ-wgXrvzddmR9Ok4dQJhjL8gP2fmAzi8HeMzAGAmYXfGArzKKfH-ebakm-ogR_wqws1rTihTY9F0k7S8eedomE_CRAMKinnce1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cce6c887b.mp4?token=sOmAriS-T5Fq5B9X7lgTiZ38nUeaDXfCGZYovkmJF1Qr7lsJkRtGQeKrafNMqL4xGg0Xo1P4hX2qi1J4l6oaQQPJa-6QJSKNZ5Jxz_x24CvfJkZYMs2l1_BPOy4XlBiFNeXhlOYkWGWV7aD5orj2X0PYtFYG_JFnZcMWqQTjE2X6m5w2XwnoAjaBhBfgzN2n-TpFR63pQ5hBqm83DjCWQX-NqJ55Ua-85WGPXJIf6GTHz5mnPSCZ-wgXrvzddmR9Ok4dQJhjL8gP2fmAzi8HeMzAGAmYXfGArzKKfH-ebakm-ogR_wqws1rTihTY9F0k7S8eedomE_CRAMKinnce1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش وزیر خزانه داری آمریکا به نفت ۹۴ دلاری
🔴
بسنت: امروز شاهد افزایش ناگهانی قیمت نفت بودیم که من واقعاً دلیل آن را نمی‌فهمم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142899" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا لیست جدیدی از تحریم‌ها را علیه اشخاص و نهادهای مرتبط با جمهوری اسلامی ایران وضع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142898" target="_blank">📅 21:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت فیدلیتی قصد دارد سه سال پس از راه‌اندازی، از واحد صندوق سرمایه‌گذاری کاملاً تحت مالکیت خود در چین خارج شود.
🔴
این تصمیم در شرایطی اتخاذ می‌شود که برخی شرکت‌های مالی جهانی در حال بازنگری در حضور خود در بازار چین و ارزیابی دوباره فرصت‌ها و ریسک‌های این کشور هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142897" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پالایش ملی: با ۹۰ میلیون جمعیت، روزی ۱۵۳ میلیون لیتر مصرف بزنین داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142896" target="_blank">📅 20:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-fhKGJzAzCx6DEVA5MttuKWVbM_rhVss_VpPuJxu0y0vvHV3TClyGibdzpAr8ASLUPG94TK2rqkfoOFnu0Pkk20EdhjUg4YL4OmuoRUekY0Fdq-dd0swObqe50xjVjT0c_6h6lwP2Z_BApmGVDI8KQeO2x4T_HSoJXPJJGKbWwcv0-DP6bonMb2y3-fl3m7xyPqFvkYJQU1o_3__dEx28fRkr0HxJKzrGSMp32RdVBfi8fLWSIaNZVA7gchp-aN1rsMjGDjVL3h4oUY74qxOie9ZDO3oFe7GvRgO9Ptyda1jmG4j_-gqkdOMOx94u440T7GVSxQUFlvkM1lMKcS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار لبنانی: دو منبع به من گفتند که ایالات متحده امروز رسماً حزب‌الله را به عنوان وابسته به سپاه پاسداران انقلاب اسلامی ایران (IRGC) معرفی خواهد کرد و آن را یک سازمان ایرانی و نه لبنانی در نظر خواهد گرفت. انتظار می‌رود وزارت امور خارجه ایالات متحده امروز بیانیه‌ای صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142895" target="_blank">📅 20:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بیانیه مشترک بریتانیا، فرانسه، آلمان و ایتالیا: تصمیم اسرائیل برای برگزاری مناقصه‌های پروژه شهرک‌سازی E1 غیرقابل قبول است.
🔴
شهرک‌های اسرائیلی در کرانه باختری غیرقانونی هستند.
🔴
پروژه شهرک‌سازی E1 اسرائیل، راه‌حل دو کشوری را به خطر می‌اندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142894" target="_blank">📅 20:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2-4DIaBqM8OG1zCE07-quLVWu57MDH10-H0oBK4_2nNIiH03W87FNHJofNP94wyIN8BhrmxbRG02xbuqO4aKgZX5YFJLSuzY8txuSU2q5_w8KR6kTxn1AMS8I-XyejFMakzRyUjoRhb62I7in1AzCX1EmxUELiZ0gVh_NAnxbxXT8RFmAxCqhxgT9ECRXQQK4Y7jfNgRVUSZZr-uxKKnCPUd0LCa-S5-KHmycOxj7B-Q8XtKGsVG_Kx73kPBkBTO-9UnxwxZSLRkm7jF1591YLLt0N4ZX5BCAvKHwhJzPv_BIWTFQFp0MPq02mXIWviyAFLZjrIDnasIBn83nz8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که خلیج فارس درست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142893" target="_blank">📅 20:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه چین در واکنش به مطالب ایران ستیزانه رئیس جمهوری آمریکا گفت که تحریم و فشار به تنش‌های خاورمیانه پایان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142892" target="_blank">📅 20:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نخست‌وزیر عراق: دولت در مسیر قانونی کردن فعالیت‌های حشدالشعبی پیش می‌رود
🔴
جایگاه حشدالشعبی را به عنوان بخشی از پیکره نیروهای مسلح عراق، تثبیت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142891" target="_blank">📅 20:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
طبق داده‌های کپلر امروز چندین ابرنفتکش از آبراه جنوبی تنگه هرمز خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142890" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1zZUXqMzhZ4gNGizk2gWwZAdwk14OvMzPtUKf6pSzG5wyQj82MsYrvMdkBbU4cNnWjdxtHcvJsiud9BvUxN4JocL6UPBo7thE0QNCzjn4orsGJ6La_Q2EpEgPFwfeN7yd27NenI98v_1TwjKJoCAHQhzrFA-IMn6t46VtRqCKg5eKiR1gGGwHEUT3VG9ICeU9MHry_Un6EFGBSXcLjP0wJKqnb1UKHv8PqTUgvxScxlQAF10Grbv4ltt11Au_j135DlkAMhJGO0aZm4OM5a0XlO2e4y9MH7T3ALUjCrS5xZ41Rjx8HiEUqLgBscs46IFhPHOroAPHpFb5s2KBWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورمن، خبرنگار وال استریت ژورنال: این اولین باری است که یک مقام ارشد دولت ترامپ پس از مدت‌ها خواستار تغییر نظام در ایران شد
🔴
اسکات بسنت در صحبت‌های امروز خود از تغییر نظام در ایران صحبت کرد. بازگشت به اهداف ۲۸ فوریه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142889" target="_blank">📅 20:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f44565584.mp4?token=dAYpzlXdc4WyCxDK2Trq66u7dD1S2WNKQhfFKzZ4y8Mx4CPI2WkAVLw3wR9epcKskofF-Y1zv2fNneDBnjIrW-VYgIfNKO5eyUgFw_cD8QKHxC0ECpTL5wirYCSZXFh5vQDc22f4BBYxZ960PJt3LUssS6G5k4kVTaH05BysSYgYtVbFl7kw993AsXWc6chsAkPkP4KDnjYP8sNAuVmvEPdFv3nWLstKMSmm1o-nCF4CtmEC64L5onDKzKi2etA9tq0B1wB2DU3GyAYDleX1ETpRkmDvRLNJhQ2rlkKbnLrviQBPAJEJjJuUMzB7LuL-a4HgEaikQQdzzvI63i7aoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f44565584.mp4?token=dAYpzlXdc4WyCxDK2Trq66u7dD1S2WNKQhfFKzZ4y8Mx4CPI2WkAVLw3wR9epcKskofF-Y1zv2fNneDBnjIrW-VYgIfNKO5eyUgFw_cD8QKHxC0ECpTL5wirYCSZXFh5vQDc22f4BBYxZ960PJt3LUssS6G5k4kVTaH05BysSYgYtVbFl7kw993AsXWc6chsAkPkP4KDnjYP8sNAuVmvEPdFv3nWLstKMSmm1o-nCF4CtmEC64L5onDKzKi2etA9tq0B1wB2DU3GyAYDleX1ETpRkmDvRLNJhQ2rlkKbnLrviQBPAJEJjJuUMzB7LuL-a4HgEaikQQdzzvI63i7aoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای حمله بمباران با پهپاد به تپه تل الدبشه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142888" target="_blank">📅 20:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUPh3Q2WNIMLxf_ikWX6K6v-48UDlOjwubZEXLeODxt4XtPoB6Tn1dYTt2W1yOU-Y5_GonzgFugefSnH9Rgh8ZknQlcgN0GNN0_8g8ycjOaWrjo1oYZsK-bN5Q9HtEyD0VmIuyGwCaRo1dsN-4zpfogzZMKszGBHQr9ZQGS_RRbvFibBriqE0WAcgEovUyabHY_VjeK1NU6eEUBLqmJskN4EZPzgQkUAZWPtPgVD4dV81r4paPaAf7gOWau4xehYTPafWfZTPGc59Wxm3fY8eZVPjzi1y-2-tjUD2Ssx4PbnPc-FJ7BMtWUIUZw0k_sEpudzczX-Vrlraotng3lUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد دولت رئیسی: تمام نشانه‌ها از آشوب و جنگ در شهریور و مهر حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142887" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
شلیک ارتش اسرائیل (IDF) در نزدیکی تپه علی الطاهر، هم‌زمان با رها کردن بمب توسط پهپاد بر تپه تل الدبشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142886" target="_blank">📅 20:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOnZT_g4AprNz9pc1HSyWyVykwZR060MeiE3fdhovkdATna9TXdscA-IP171LluZbJyipBPdBYkhTlIVl51zTnqw5cKTRYyjlcrfOW1ONnKJ8RpOI1cDrOeh7Dq7j3hkYTkJWTdAcYmsgl8YySGQYSQruaH76EoPxxNciY3k4jHMpKVB4ZUODSESNKJOMcIpTbGNcm7_FQNv3ZxrrfPHe2gMWvsPHfl2xQC5239wOQVL6YlEN6qD11do4iKk8t-ls1H2rcP6KBusDc7q_H-PAlPKl5SHvUdqEynBARLF0d8xIJM7lc4AdF9E2biJcx9UNLS8_O-QtQvbW_mdSELEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : هواپیمای ترابری و چندمنظوره MV-22B Osprey متعلق به تفنگداران دریایی آمریکا، هنگام حرکت ناو آبی‌خاکی USS Boxer (LHD 4) در دریای عرب، از عرشه پروازی این ناو به پرواز درآمدند. این ناو همچنان به اجرای محاصره دریایی آمریکا علیه ایران ادامه می‌دهد.
🔴
تا ۲۰ اوت، نیروهای آمریکایی برای اطمینان از رعایت مقررات محاصره، ۶۷ فروند کشتی تجاری را تغییر مسیر داده، ۳ فروند را از کار انداخته و ۲ فروند را مورد بازرسی قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142885" target="_blank">📅 20:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izBaH4TcKaK05k8gvHLZfYLkxZzcYYUNP_ULnMq6AYkoNUsTI70JZiPcoeyFyxFHi68ubOeq4MServnAUKcxlqXcBiKpGODJzLN5F3ZqojMQjY-fAgMBRhI7QoMH7Omx9rY6R5W7wEgFi0TR6dVtIrv9uOQ9-lBrOPj9KumbwJH976qYKkJt1cyHmbbRVhG2aDQNWRqCpxttTlfjtjxsZbddRGMU9JuOTITqeywfGcM88a7HgM9vvLuVOGnILuvxHbIfsjzQEvKDOOrRL-pCnMs1uEnZV2BMRCGYt6prwcUiJxFWQ7rGPqwvnmeCxx3B_5r2WzMN7_xa_PFxKIp4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیباکلام: کشوری بنام فلسطین وجود نداشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142884" target="_blank">📅 20:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
اسرائیل هلیکوپترهای تهاجمی آپاچی‌ خود را به مرزهای سوریه منتقل کرد
‏
🔴
اسرائیل در بحبوحه تشدید نگرانی‌ها از تحولات سوریه و افزایش تنش با ترکیه، آرایش نظامی خود را در شمال اسرائیل تغییر داد و طی عملیاتی اسکادران ۱۹۰ بالگردهای جنگی آپاچی را از جنوب به پایگاه هوایی «رامات‌دیوید» منتقل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142883" target="_blank">📅 20:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142882">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عسگری، رئیس‌ کمیسیون کشاورزی مجلس: وزارت جهاد کشاورزی قصد داشت ۲۰ هزار تن مرغ تاریخ مصرف گذشته رو که یک ماه بود از تاریخ انقضاش گذشته بود؛ سه ماه تاریخش رو تمدید کنه و وارد بازار کنه. بخشی از این مرغ ها وارد بازار شده ولی جلوی بقیشو گرفتیم.
🔴
گویا الان چندین تن مرغ تاریخ مصرف گذشته وارد بازار شده و مردم بدون اطلاع مصرف میکنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142882" target="_blank">📅 19:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142881">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDj_XbcN_cXdsPXz0vxuBMUW6rFH7ehb0t4WePoYK-Bg6TOYINGWTrzgVMaBgARy8pxdQjnozRJsCSZqP--kEpH-SeFAsn4RVcVXXZ9CxZkxVGzrGNEIs3krFhC-ZYNsv9DmthAdd1LKn6c7q8fJYDYnzuzOy4pItieDeNDOsV4pZxPL5jt02ogl2t891Xc4fbq7rHPiDS0h7QrAL9W7SjCnC6bUwe9P2NCcskWhq-ht3ROTdwfH21Vi41b-1zeYq0-btr2JhaebhAiAvSEOETQkA8viRpxtS23HIeAGSol6TRtywg_ryWlsr8YnFMjFnnzLAzKhyOa2PERR4Io03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسیب قوی مرکز، یکی از فرماندهان کلیدی جبهه مقاومت ملی ضد طالبان (NRF) امروز توسط نیروهای ویژه طالبان کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142881" target="_blank">📅 19:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دزدان دریایی سومالیایی تانکر محصولات نفتی SIBU 1 را در خلیج عدن به غارت بردند. این کشتی پیام «دزدان دریایی در کشتی، کمک» را پخش کرد در حالی که دزدان دریایی سومالیایی کنترل آن را به دست گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142880" target="_blank">📅 19:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وال استریت ژورنال: مقام‌های عرب معتقدند ایران در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142879" target="_blank">📅 19:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سنتکام: گروه رزمی ناو هواپیمابر «جورج واشنگتن» پس از ورود به حوزه عملیاتی فرماندهی مرکزی آمریکا در روز گذشته، در جریان یک استقرار برنامه‌ریزی‌شده در خاورمیانه مشغول فعالیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142878" target="_blank">📅 19:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
آنیتا هایپر، سخنگوی اتحادیه اروپا: آنچه ما از جانب خود انجام می‌دهیم، دعوت به خویشتنداری همه طرف‌ها و همچنین از سرگیری تلاش‌های دیپلماتیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142877" target="_blank">📅 19:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
به گفته بسنت وزیر خزانه‌داری آمریکا، احتمالاً ایالات متحده جنگ گسترده‌ای را علیه ایران از سر نخواهد گرفت، زیرا فشار اقتصادی خود را افزایش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142876" target="_blank">📅 19:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0005fb25b.mp4?token=TpTV1jA2kam31sU9BCvyAT25zTXOt0M1yedWnwSGOU7gsMx-tL45c87pyChnHO-w9TkVMdh7qHwJjXTdTlWxiB78Z0pwv0ictaycolKPjPR93d0FiW17WWg8aqdVPGS4J1VelFWGoh9KzdEkbLXE60PFEBp1kf3Iw55O68uVvMydzSr44IVo34ODi0LLvS8FGPrw5dqixrSxlzd19dCMG0u7ojhTEsQSjBdQLHCzsnjlb8-ssNbCcGhmECBPsaXUG14KAMAsDJIuSoZlRvKqbyX2cb1tgts-NkWcFUs_za7Ry2CWt_05-60iVwpxKwdkKcXaIWeMu7h_pTIxY0mjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0005fb25b.mp4?token=TpTV1jA2kam31sU9BCvyAT25zTXOt0M1yedWnwSGOU7gsMx-tL45c87pyChnHO-w9TkVMdh7qHwJjXTdTlWxiB78Z0pwv0ictaycolKPjPR93d0FiW17WWg8aqdVPGS4J1VelFWGoh9KzdEkbLXE60PFEBp1kf3Iw55O68uVvMydzSr44IVo34ODi0LLvS8FGPrw5dqixrSxlzd19dCMG0u7ojhTEsQSjBdQLHCzsnjlb8-ssNbCcGhmECBPsaXUG14KAMAsDJIuSoZlRvKqbyX2cb1tgts-NkWcFUs_za7Ry2CWt_05-60iVwpxKwdkKcXaIWeMu7h_pTIxY0mjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت تکان دهنده زنگنه از قاچاق بنزین
🔴
خود پالایشگاه ها مبدا قاچاق بنزین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142875" target="_blank">📅 19:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دلار هم اکنون 190,000 تومان...
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142874" target="_blank">📅 19:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: زمان آن فرا رسیده است که متحدان و بقیه جهان به تعامل با ایران پایان دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/142873" target="_blank">📅 19:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از منابع آگاه گزارش داد که آمریکا از امارات خواسته فشارهای اقتصادی علیه ایران را تشدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142872" target="_blank">📅 19:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: انزوای اقتصادی ایران بزرگ‌ترین انزوای اقتصادی در تاریخ خواهد بود.
🔴
زمان آن رسیده است که متحدان آمریکا و سایر کشورهای جهان از تعامل با نظام ایران دست بکشند.
🔴
ما کنترل تنگه هرمز را در اختیار داریم و حجم زیادی از نفت از این تنگه عبور می‌کند.
🔴
ما شدیدترین تحریم‌ها را علیه ایران اعمال خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/142871" target="_blank">📅 18:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857974ab2e.mp4?token=U4ZhV67IoTHFhjEFlrUl0nODXi2uoVOERITnWTg2hxY0xr9ayNP6WLbxnDTJKFOPiA0Plyk5ifFQnGxPhGo8yzaMAByaUjxWB067zWrYiIMtBP-_etC-0h_2TnGyQB9CfhB27W3VQZnajlE1DIjLp4LrfKcFr8tHdrHeJwAAEjNKHKrIs9QvxB-DmsoOTC0WD9aYLjsdMg-myrefb2w_vzczE4yXW5BIYW2K_c1G_9DgScbovAhbYRXXs3Le2rX7-8hvPxs6ruscccPIdMv98apAqMuxfKooRUO07GTYp6zCpXy9JzExZE-kcjzjrs_UUq5gpzxnEN8uo1z9mfc7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857974ab2e.mp4?token=U4ZhV67IoTHFhjEFlrUl0nODXi2uoVOERITnWTg2hxY0xr9ayNP6WLbxnDTJKFOPiA0Plyk5ifFQnGxPhGo8yzaMAByaUjxWB067zWrYiIMtBP-_etC-0h_2TnGyQB9CfhB27W3VQZnajlE1DIjLp4LrfKcFr8tHdrHeJwAAEjNKHKrIs9QvxB-DmsoOTC0WD9aYLjsdMg-myrefb2w_vzczE4yXW5BIYW2K_c1G_9DgScbovAhbYRXXs3Le2rX7-8hvPxs6ruscccPIdMv98apAqMuxfKooRUO07GTYp6zCpXy9JzExZE-kcjzjrs_UUq5gpzxnEN8uo1z9mfc7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: آیا کارزار اقتصادی علیه ایران شامل چین هم می‌شود؟ چون چین شریک اصلی اقتصادی ایران است
🔴
بِسِنت: بسیاری از گفت‌وگوها بهتر است در محافل خصوصی انجام شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142870" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH2k8MNf2T_VPo9-kwrLTEWI0v8IwXtnEg6CnVr_iKtOdZZKqshHOozG_i0fj6raa4MONDg6Jvbwxjh096kH2WHNAcP441BIPXsRIvqtvNyy2-TgtYL1y1s3NtVmk0Kd8ooabV9ceCsTMS16srfTERdnE46m444B5lmDF4424BmBTPXemmAgBT1Tsl4J4VLSvudbaU43MKUqtorrEMlOT7KF_Y0RAVmrU6_0Tq0sd7RypJXDe1YYPYWfGbLs9ZR1hmrG8tJbnoQ6ggw-hBn5jaPC-mY2gsJH7r1nW9fLBM7FtfRlOI6gS3d4S0C71L5zXJocNm-SJ4oh4wCwj638Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا:
ما نظام ایران را سرنگون خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142869" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142868">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378fbc38e.mp4?token=Bh8xRmNCNheEy6h8aqUAWWTm6a_gNdvxq2ft0ZgmIikOkNfupCinrBI76e2aaixCQGlUf4cCe4OZNgY38Mx4B6d4GjVLzHWcoCiq6YE5wq_O1X2Zx67usdbP0jfPJhjzNOzC9Jlvi13ORMze39SVyqGRCJQvbArEVYPjouUxo2W6_mSWPVpwf3PibgMInk6-ee9Qdro9EMuKQ3qI-9hDtM5SPFag8xCJ-06MkFz5IvXfB594AghW7byk3KgLUPhNzBR6aFWlUghob-4LTa-tnt9UQDtFJGx-TXxxZ9vq68isvTX3HzY3rb4wCFPnFK5f0zKkWzmndDhOQjS7ejrosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378fbc38e.mp4?token=Bh8xRmNCNheEy6h8aqUAWWTm6a_gNdvxq2ft0ZgmIikOkNfupCinrBI76e2aaixCQGlUf4cCe4OZNgY38Mx4B6d4GjVLzHWcoCiq6YE5wq_O1X2Zx67usdbP0jfPJhjzNOzC9Jlvi13ORMze39SVyqGRCJQvbArEVYPjouUxo2W6_mSWPVpwf3PibgMInk6-ee9Qdro9EMuKQ3qI-9hDtM5SPFag8xCJ-06MkFz5IvXfB594AghW7byk3KgLUPhNzBR6aFWlUghob-4LTa-tnt9UQDtFJGx-TXxxZ9vq68isvTX3HzY3rb4wCFPnFK5f0zKkWzmndDhOQjS7ejrosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناسان آمریکایی معتقدن ترامپ به احتمال زیاد از بمب اتم علیه ایران استفاده خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142868" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142867">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81d0658cd.mp4?token=t8XnzT3zfqrdIsbheuETwsUBeOOWHimvweZkqz60gg-A50P0FM2j5VFL62jgwHcYex8rdBUU6UR0CwCNqJDPsN7j1_j-isIN8op6hrSSwhobskUi8Igj-Diie9xgRK_laKb06Umtd9A4cZTUqyAkbv2r60k1ZZfUFrk9It-FU6S8h1e-zK1jTimYWrwZgFjL0CDBXoa5yvDI6ckiFPMRjoHwXR0Vi2OhX9GpJcK72eGugG18_Z_zZqR_wcuUKx5vBpzBhP2-TCNTw4cTCoV787xD-pgHOoLhNC3xRE1sgzSRZQAyVQSPtxAg7BBzyhBYCO2rJLKof0rWX8UBIzn4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81d0658cd.mp4?token=t8XnzT3zfqrdIsbheuETwsUBeOOWHimvweZkqz60gg-A50P0FM2j5VFL62jgwHcYex8rdBUU6UR0CwCNqJDPsN7j1_j-isIN8op6hrSSwhobskUi8Igj-Diie9xgRK_laKb06Umtd9A4cZTUqyAkbv2r60k1ZZfUFrk9It-FU6S8h1e-zK1jTimYWrwZgFjL0CDBXoa5yvDI6ckiFPMRjoHwXR0Vi2OhX9GpJcK72eGugG18_Z_zZqR_wcuUKx5vBpzBhP2-TCNTw4cTCoV787xD-pgHOoLhNC3xRE1sgzSRZQAyVQSPtxAg7BBzyhBYCO2rJLKof0rWX8UBIzn4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت درباره ایران
: این درگیری با ایران... ما از این وضعیت عبور خواهیم کرد. ما نمی‌دانیم چه زمانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142867" target="_blank">📅 18:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142863">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cI-O8pBewKJKS4BIqY_tNSLHUTDhLgw2fXdRI74INHwi0e7eSWtuj0v8CMHvjavdllbY7A6IyDK6oVBpL2X9DZ-tSPQxA6j4t37gSaMx_0EEopDv6ZhHQij48DFsCROEaFL2tvIzoEk9sWvsiYliNGyMwJhLwXdusG8FwnGPml9XFJjozG04pc4HyE4TavOC9rSWRES93nNpjs4Xh_stz148jjk62rlOr9CNZQIpCq33E7IeyrnTh7Ip1lhH_TQT3dXufb9YphF1HZnlkd6mUsCCTSw0SsxiRBfOr-EvDd4SWxf9DOmMHqEUpZAYnJr1c3oumCukyfbPWcT6nhESFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggtgCH-jwoqHPeFemJGsAPBXLk26Kc53toaGoC1OzzRZtY_YhEHU_rEfqYJqGvgoaYNHm8maHA9VCAqG9EUl4-JW0EWZs2Nf2tOHOEiYpsMZ2sICwHO8kXwBAp1PVFtdoq-oV7CphClaeCviE-C0_NzMEJfjXxNP3CFqc9fBbB9mJ_LBKlp6yDWrl0prrAA9Hlj02lMIt8a0qiEF_H9pA6n3BpPklZQqoq_ILAyIcshZ-uj-2xPi2sOXPGqMgL34ySBuIWyN0HAKMB_p0O-1z1_3Ddu0gvY3zwckTl_OPQiOd9UH69-7q55SYTSlgbnyg4UlvRCdOQL4-XSLTqCteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pY5zfZFn-K1ssg79nESnSO32MXDApHQEgu18FsS-LWXLEDfYAaNCl5vf9CtWXJfVeja0nU9SINrSD-ZscJql0WbVxny4qdGaLKA7PJjjvLLis-5UbFOGezjReY_SbDijWaMAe1d_7TCGMhX5IVuI566_CxEoM8h7eQU7X_NjNK2POJdZyFEaVW1Hw2F9cqo8cEXUpG3rdrdWFH5pqtDNUJvx7tbrrrh_LXqe97C7VlPljmu2AVmm5b2fqKSZJqvWoofUxiotvVs2R5Bv3QyAsLIZao3taW5ppAvrN4h4rQzlx-wdHnaHjcQSGDqDmUf0hxPLvIA1pwjtjSuJ-8eMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0tmrZ4SSqrOnyPncLp5wY4pEhLpoTuK3SZsY8beme6w6HKQDH5eJ1bntwKvwGRBJV6jhda8HkWsDgtUZkOzJWfLXg88UbUNGJVVIeqewhHnwzvrytJBzWpOhcvzNvcR_taswbb9edeRa_u1FHbMWrLe-wB4KKcz98CF5ueOGjF6AHtW-sZShYfh-n7Yg2bnfYDwULa1-mQidmw0c_Lxv5mvJ9DGKezjM4cOyIYPDyxhxYq86LQu2kwXEJxKu84BHEwo7tsiqCOOWYG9XV-apkX_w8NIxQWPTdGqBVzdF3FhdyqdYkWhI5B0ntWm6YQPHo9RjkcrthG715-_m8NFqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از کنکور سراسری امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142863" target="_blank">📅 18:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142862">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0X1jTAhxuevrDKMT6gxESpggbhzQYyoyPwfsAEOFtekysbSAgEhDUhlbC9e5GZjFnDnI2eGaZqtyy73hdVYhyRqDZTiP3nqzSQfE2Z3KvL1Tc7j51JG3fAbE8gTXyqs-YmL5he8g64DVFZy8HlFsCpWPF8ORFGGe61-YVNdUMppP_4RfMzfbpW1pZ6G4gvtNE6YwhOWg-YQy2dq4VG18Zzrx3d3FrooSN3CnB8cLfAq5eDNo--bBJcw8-alblRLkOU-mkcnGXzUE6rjh_WaZWNRtWdjG-XHA_aNXs_o1eNmySnFU5rSp0N3_ICMSMl_glAO2xDp9Qu_zemIc4rt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثبت تصویر بی نظیر از یوز ایرانی، خراسان
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142862" target="_blank">📅 18:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142861">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
معلوم نیست تو تایم جنگ چند لایه پاکسازی شده که سراغ پایین‌ترین درجه دار سپاه رو هم می‌گیری می‌گن کشته شده.
🤔
هیچ صدایی هم ازش در نمیارن که بگن ما کشته نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142861" target="_blank">📅 18:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142860">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b8da31b.mp4?token=Sm5bct2KFdHINHccmx6ABgyA72mVs6IC2by45H21fCPZP_cRbznLR4zJUPtBaD0pKtV88EqYy4f-xVYFEk_mLb3461a_8O4GeRcirxZmh4W8Ie9rC2M55uuYFjwcCuHoApz8TxUYhyNnjAsF-_znvL9jdmm6HB3-vuEicTUsjseLQY6BcwFifH3WGL04gkl9N7BBTX72gzJM5CbHsUlBFXvJIYvvhisNvmLPMlID5VJUqU41qTFdf7WiU4Rm2SRMJa8CU3Oi6CpRCq495ZxUm2fG4YN6VGlk_y2EPVTdfUvIMsKYxOaOBmpcLib6RzGKqPTAzif_S0ctlN-wYgj_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b8da31b.mp4?token=Sm5bct2KFdHINHccmx6ABgyA72mVs6IC2by45H21fCPZP_cRbznLR4zJUPtBaD0pKtV88EqYy4f-xVYFEk_mLb3461a_8O4GeRcirxZmh4W8Ie9rC2M55uuYFjwcCuHoApz8TxUYhyNnjAsF-_znvL9jdmm6HB3-vuEicTUsjseLQY6BcwFifH3WGL04gkl9N7BBTX72gzJM5CbHsUlBFXvJIYvvhisNvmLPMlID5VJUqU41qTFdf7WiU4Rm2SRMJa8CU3Oi6CpRCq495ZxUm2fG4YN6VGlk_y2EPVTdfUvIMsKYxOaOBmpcLib6RzGKqPTAzif_S0ctlN-wYgj_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه آی‌فیلم داره سریال "متهم گریخت" رو برای بارِ پنجاهم پخش میکنه، بعد این سری دوتا از صحنه‌های معمولیِ طنز سریال رو به بهونه‌ی غیراخلاقی بودنشون سانسور کرده تا نیو ارزشیا تحریک نشن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142860" target="_blank">📅 18:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142859">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
مدیرعامل توانیر مدعی شد: کاهش ۶۳ درصدی قطعی برق در کشور
‏
🔴
محدودیت‌های اعمال‌شده در شبکه عمومی نیز ۶۳ درصد نسبت به سال گذشته کاهش یافته و تا ۲۰ تیرماه هم خاموشی خانگی نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142859" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142858">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی ستاد فرماندهی مرکزی ایالات متحده (سنتکام) به شبکه الجزیره: نیروهای ما از اوایل ماه مه گذشته عبور ۱۳۰۰ کشتی را از تنگه هرمز تسهیل کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142858" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142853">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oHn5ZpqWF-PJECphZ5Tg_yv11Ai1_pGpAY9zScKViiVjTmXfwVHpyuKmQRQLPmE80nY6xq903-n9BjPhQmUBYawrPgjpkjXrQigujB3fdHpxUlLkVz6WY-nJ2_tV-VvgkWGkz52Jh3ZprvRXlXE3j3u923DEowWQ6jjsQ0bYML43grby8Spqeoo_1115bV-rrS6mi_7aukcMshmeMEbD2qxkdOd2Sbi8sJhmKboOp886vfEf-S6xhvgdlyn1QBguO7jBqkx1F37HitrdVupgshAs-ugfGQpFMUnlubdBN782SDLdBSl8cGxYouR7peAWos7kpWQg_8epuJVfPP2QEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V_gikAnQGup-BuPN_YzGfIfQrBkOEiPQ220dEtuN0Q7cedPNa5Kdninb41ygSoo9uBTGePd3NAW-S-6gwne3wE1XakL0Ds8-JShM9gslIS58T0H1Uql7iLiSKmXDqNE6-U1kGwyo1VSI9JFbX1oduTi9v9pz_yM5oZi8bAh-h2UyotyrQa5KQAugQ8OCdwB0jh91UksP1P6LQsHcDXo4I2xJhFlMNfAPNuRrK2QoRnWjkKJ0h7ytAKGsd2K8kdPheAQAQOzTRP8ypVvC1BVcpO_vk2gIFmWuaKRPkAqIth4x6zBgRhxv7_R9yqUBIfXKffYp3WqDzM3o6xZaV_5Nbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YejX2_sV3_mgBuVmZloiDsHedj4_jpZWu3vh9a8nT51hzKEirS08fY0enGo-cc4hNwCL9ySWsw97CQwchhYVt8hcukonVqaiUwzkyc4-_ABVBoN-enrN9cUatyP7h3unUIA5Z1jxAMWXXEUfzVLaKWo1GILgSv7tqzO-NAR-T2RAlBFwzeIy7a_ZrG-FTmT3pWdN0aAKW6L5maSTHB-i7soDi0juRv5jUw7brmGUF8C2fRbm0KJX7k3wJDzOB6Qv_vO0ThYb3HqeMw0YixKwNr2rcNY57VK50KU_cRfNMAUUElUvoGUX_-yDlg0w2n9hwC1AJFjNa4bXzQdNsQQxdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=QCg7LXLcN273-qr6sJTSUhdUbVS-UG7c08s5AHujv4uEQSzWFVujPDbMn_qwEyDXOyoI2k9K9cbipBJCJV7t10YJYqBQYD64ILnJURhvF5MX34Z3RaXXrNRH08v4Ug5_d8t18CawFwNEoik70caCeAHKSJMNRNQlBgUBi5pOrZsvmupUGpG0Jx5Wv6XwnNwTT4ZVY20uI4WbsCKB8I59luwuUIFBRPXTR9L5poBH1R1OraBCURsflfDNa3ptFamXYN3AqUI0aQcpmJSj6Q75-aqrhDjvvspG-1MQiP9SltvSE8q5bABTil-8JGe2t95xA4B6izXU1wGwWh4xMlXrK0T0XeRMOHWnKVmY5sfhdyE8zRPxZwgN4u4M5WQeucMDnXhx8UABLZh51AUYP25QN4ky9FnN2Mj93SsIGWx2LRs6FjvuSJ3pBAgJYJKu7Duc4HQZWxSiS56afAot3pGhH6dg-CpPllRPxTkidHnT_v9IDj7cLkVn2QflT0HPWdHwSEVTQPe--PV7c_TC07Pf6FQaCfJDrINxG1xsqGHfBNSsvNusebQn3v4HekEt8AdY3pGFDXhPylntI8A8_4Eafb89v6_TcbXeuHlRmR7NUBL0yr31AtVrtAtY-7Ojx9-WKUXyvH_RP4vLWgfiygPd87x_tc2CYBnOg5S0kRQM9tI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=QCg7LXLcN273-qr6sJTSUhdUbVS-UG7c08s5AHujv4uEQSzWFVujPDbMn_qwEyDXOyoI2k9K9cbipBJCJV7t10YJYqBQYD64ILnJURhvF5MX34Z3RaXXrNRH08v4Ug5_d8t18CawFwNEoik70caCeAHKSJMNRNQlBgUBi5pOrZsvmupUGpG0Jx5Wv6XwnNwTT4ZVY20uI4WbsCKB8I59luwuUIFBRPXTR9L5poBH1R1OraBCURsflfDNa3ptFamXYN3AqUI0aQcpmJSj6Q75-aqrhDjvvspG-1MQiP9SltvSE8q5bABTil-8JGe2t95xA4B6izXU1wGwWh4xMlXrK0T0XeRMOHWnKVmY5sfhdyE8zRPxZwgN4u4M5WQeucMDnXhx8UABLZh51AUYP25QN4ky9FnN2Mj93SsIGWx2LRs6FjvuSJ3pBAgJYJKu7Duc4HQZWxSiS56afAot3pGhH6dg-CpPllRPxTkidHnT_v9IDj7cLkVn2QflT0HPWdHwSEVTQPe--PV7c_TC07Pf6FQaCfJDrINxG1xsqGHfBNSsvNusebQn3v4HekEt8AdY3pGFDXhPylntI8A8_4Eafb89v6_TcbXeuHlRmR7NUBL0yr31AtVrtAtY-7Ojx9-WKUXyvH_RP4vLWgfiygPd87x_tc2CYBnOg5S0kRQM9tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
🔴
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
🔴
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
💔
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
🤔
حرام زاده حکومتی حسین حسین کردنت رو باور کنیم؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142853" target="_blank">📅 18:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142852">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مشاور شورای امنیت ملی عراق خطاب به قالیباف: قانون اساسی ما اجازه وجود گروه های شبه نظامی در خاک ما را که تهدیدی برای امنیت ملی و همسایگان ما هست رو نمی دهد. دولت در حال جمع آوری تمامی تسلیحات از تمامی گروه های شبه نظامی در عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142852" target="_blank">📅 18:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142850">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVg8JhukdJQElNk8-7agcwRi1pCqibxtW1lI57twSpkdUL5A9FZ1g24vEoTn0bQbLFoIZBK1MG_ogzTBF6vu25PFYzb_X2QNav5RpUi4i6fIs3gsNS7AjMZ7N-hBo5PbZ8Jgy9k6UzQN_NxIti-al-ZUecxyyO-pwN6tedEZLrY-2aByDR-f4AVkRN8NZ8GQKrbocHXqAStKmj0hdEpYlmEIJfu0Phog5JbqSVZpCVZaDS5uemZYs7fsdwj9wHJik0ypM4kdfPuO-x4FF8DcQlsSmnkzCG3xoUVUZPHAbQtmcS0jbwBzhOt168NyUOSM8Pqjqntb34rlyJ5a0Kbkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1080cad72b.mp4?token=i7a9AWizrl5p7b-KvTn7zmiJ1LLPZeZyZ8dB2zfoOXNjGjbLJRvfuFL0n2Dh71sqUS_Pktn6TvEASFRx8y--ns4NWYb3Dt2--DRcA4J4F1CKAwHfRrs-n8Lrl1j3eCbTVHOSn7iyjECsXzcKIcSpLsZwd_qeZsTrHhF2b-Tw7Z_dAREeB_Dn212oEpK-tFwrQ6KiRaCk-kVrzHpZQNfvFdHbFi1WS0dXPeNp6hYCO3kos-uHu_knb1vLbblU75HooyjPqgKwDA0gPvJRJYdgzYBlHmoS_mHQVWtt0_a1Dp3miDFU4GOE9u1R-OqbOnNVzC4a_LzbtHk2y_1eVAmKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1080cad72b.mp4?token=i7a9AWizrl5p7b-KvTn7zmiJ1LLPZeZyZ8dB2zfoOXNjGjbLJRvfuFL0n2Dh71sqUS_Pktn6TvEASFRx8y--ns4NWYb3Dt2--DRcA4J4F1CKAwHfRrs-n8Lrl1j3eCbTVHOSn7iyjECsXzcKIcSpLsZwd_qeZsTrHhF2b-Tw7Z_dAREeB_Dn212oEpK-tFwrQ6KiRaCk-kVrzHpZQNfvFdHbFi1WS0dXPeNp6hYCO3kos-uHu_knb1vLbblU75HooyjPqgKwDA0gPvJRJYdgzYBlHmoS_mHQVWtt0_a1Dp3miDFU4GOE9u1R-OqbOnNVzC4a_LzbtHk2y_1eVAmKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، توسعه بیشتر فعالیت‌های پشتیبانی لجستیکی ایالات متحده در شهر ینبع عربستان سعودی را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142850" target="_blank">📅 18:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142849">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCd6D5jvrGJr6aeqzanteqgHAtIftAwqMo-MQVH7qmBkD6VHvgyWF0YGnQmpKIPKb1iVPsp0p6kxcLgbq_3XzNCGSo2JC_lVxWYeZHEYjkKIslKgt2I8dyV3MNcjDkQ3wQnTk8Fug3e1RC5Ermgr0KWMy30D59VQ7WWbg_Dlv8BWqC0_NsnWHffOZUlag1LMhtt3TDrpeA3XBkHwkGYB2Xsx4VHB4z9y13YxDmJaXn8rhSGjQ3_cMnP-uJhiy46cO8dG1mUU5kQNLEMl2HTsZUUIiBwMaN9d7Q5f_qzaFD7dolrXWUeMiPK2lMq5KTBeR9YCVWlvh-5en2Ra8v00ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/142849" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142848">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwb1ePm_BD2zW7ZfqgMrZ8_pVDYK7LPFikC8nSoU8t3RuYfJCbLxLRMTCgSnETpND-CyL0dYRNHoUmIgw6zvV-ZgYVti1Dh4-SpD6QZnHfw0zWaJAA3FP_ooWCstC0REmOSL1eouEmvAbPdSo6GnW9eTIbpLS2LbR9JUK9FQpJ6V8ueVBbjU_oqq5FLbxjpbl3zxn6_E8r6iftyb9WJRxUM9mxjOLY_ifAU6ts2XgtIHRRbnlx-PTtIKmCbR5ozUNR4PnMXYsG9MV8lirqreiE0Ei6NXgQLear7igfUQpj3K7xnNkmro6L7sfApSNKWkaQW2hJwbG4o2rYa3CoTlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت امور خارجه درباره تحریم‌های اقتصادی جدید آمریکا علیه ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142848" target="_blank">📅 18:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB0IMl6YI43laCi3PokJDudkxZMcxX65rg91Dwdoji7C0ye3ZGDkJuaj4yo6INNxbZ2BTEW9A0MAp6JftdYpK2saGOOZBfoJyjK2RPI5k7rxagKmnaIl8r52SsH80hIvZlXuI0Iwtt0oTEkRyhKNVVg2RqlTp_CBjR-g7zAy0UfI3y1UOBkHA4NE44uGMtyc10joE3DNxmkQduXFG76U1MOYE2NEHrMJf0hkD0Luw3_7qJnOY9paLvyEEf6Po4m2sdX106coLO6ocVPnAJwNghoe4ZHYwSopjUDkXdUiGJR4AUYiTlkOPX5_RQut85S_G7FFIDBx0Yke0STTsf1gfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تخلیه کامل اسکله بندر المخا پس از حملات اخیر یمن
🔴
تصاویر ماهواره‌ای نشان می‌دهند که اسکله بندر المخا، که تحت کنترل نیروهای وفادار به عربستان سعودی در یمن قرار دارد، به طور کامل تخلیه شده است، این اتفاق در نتیجه حملات اخیر ارتش یمن در هفته گذشته رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142847" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6dcaf8e6.mp4?token=AuvrdPoTo-bKkDZWC6PcQK7gfi60RL3gD3il_7DPKH2CeDBlGXEStFLEJKrL8ryT_fVNmlSD3wBJxx7fdpv633NaCo_u40dSinKuz1ASD6jwb8FYk9z0-bZJLyz6VUWm1v18gQ5YuVQh_kSSAWyCC-9kU9IlR027QznRi117eA7BbPHf3e4HHH_9iYGkWvEl85gz9lcOm5KB92amnEc6M0PD4-VXXCZZZw4nmEEukU8VqMbv45hWZn7NNZb6xloCQXt2bNzYfVdoCB6zxM_e5wcBasTkheMWA5i0_9wxQtpcY5QrJa4o_mlWY5qiuWsTqhAlT2hNdb1WS-rYjRu38Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6dcaf8e6.mp4?token=AuvrdPoTo-bKkDZWC6PcQK7gfi60RL3gD3il_7DPKH2CeDBlGXEStFLEJKrL8ryT_fVNmlSD3wBJxx7fdpv633NaCo_u40dSinKuz1ASD6jwb8FYk9z0-bZJLyz6VUWm1v18gQ5YuVQh_kSSAWyCC-9kU9IlR027QznRi117eA7BbPHf3e4HHH_9iYGkWvEl85gz9lcOm5KB92amnEc6M0PD4-VXXCZZZw4nmEEukU8VqMbv45hWZn7NNZb6xloCQXt2bNzYfVdoCB6zxM_e5wcBasTkheMWA5i0_9wxQtpcY5QrJa4o_mlWY5qiuWsTqhAlT2hNdb1WS-rYjRu38Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انهدام یک پهپاد در نزدیکی میدان گازی «نپتون دیپ» رومانی
🔴
جنگنده‌های F-16 رومانی در عملیاتی ضربتی، یک پهپاد انتحاری دریایی (USV) را در فاصله چند صد متری پروژه گازی «نپتون دیپ» در دریای سیاه منهدم کردند تا از بروز یک فاجعه در زیرساخت‌های انرژی جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142846" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر امور خارجه لبنان، یوسف راجی، از ایران انتقاد کرد: مقامات ایرانی باید دخالت خود در امور لبنان را متوقف کنند، به ویژه پس از اظهاراتی که اخیراً رئیس مجلس ایران مطرح کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/142845" target="_blank">📅 18:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142843">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCeoLrROsp68g6VWeLCrbbl_7Q8tiIk8-VmHEGEawXITUJjYPY5W5N94tjluear4f-SJK7q8i16UF7GebedUsGs0qWmtDCqo8ZWlrTtIM1dhS8nmuk9kY8eFC_4Fff6iP_OfDwnVhBgSDZfHeLKOGJuEU2wZahINfuqz-YUjSMKOzSG0iBk68Nic4Aeez1ovHpJYnSCm6pztQngY-jGJi5zpiz9Gr-UjrJIbfTmNwnTHxlkTTS5yCXA8yhSrRBZsvn-on3y79P_mfOKWlSYVpi91j1atimjGpl2RQCs5H9rFzTjDGKm2rQneYtFN2ei0hMjL6vTL2R8wCN4ihvSY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kg9Jg0eJJ-r3RYrtxoz49VVTX0krMn3XOX1WqmlsGgN3U3B-ugmQQ7tM2gkzILDKBTbvDn5lDb4oq2W_lK03i2O7k3Gjh2wPrOiwsy4T0xxls97-ZgMD_vaVhm4G718raA8efKrkvppvF_Qk2MyAktgd6loPG1LV2DfAisrkaaQrS-M2VT_o-0F_m4yf__xkDDuSHV9yN9naTkd0dKg4pMtDGQ_O7jYXaIl4d91fJNLcu2t57NUMka3ntt6xpkCsFvAgR9tzReuuJP7nWAP3bFhuPzDIh5hTR031q2VHzaGebEpsF2fNmvfW4CgTWD54tLsOEXUttv8G67vHUVv1LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 از روز گذشته، یک ناو هواپیمابر آمریکایی کلاس نیمیتز را در حال حرکت در دریای عمان نشان می‌دهد.
🔴
این ناو احتمالاً یکی از این دو است:
USS George H.W. Bush
USS Abraham Lincoln
🔴
همچنین دست‌کم یک ناوشکن موشک‌انداز هدایت‌شونده کلاس Arleigh Burke این ناو را همراهی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142843" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142842">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41cef2cdf.mp4?token=EYpHndUHi3rpdl1aLKozd4ickyx_8pO1fIAQCM86rERNxFn4hTa9-409vsbhNhv-JfWPoJOD7drOkLPfazuvqeL0e06FUp4TdBz71V2q1GHP8S4eCKyZ3AZzzteE745W83m9WN2RjyX8TK590MOQsZ56nrnxKJ9ECcNn0ZEWT7LHt2S443y8zU8xP3bv67Uy9QbQgxCQKgLP3p_clOSa02AF8KSwcFSt26GVKCFV-J9N-DnkpxiY7uKjGCyhLsjJhuDJH-j5HRMu31dm4WKodWqueW3VKjlX1wu-LBH6zIvmqA10-UNYTrFuN94DPQ1yqX7vzxMw9tni0KpF_as64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41cef2cdf.mp4?token=EYpHndUHi3rpdl1aLKozd4ickyx_8pO1fIAQCM86rERNxFn4hTa9-409vsbhNhv-JfWPoJOD7drOkLPfazuvqeL0e06FUp4TdBz71V2q1GHP8S4eCKyZ3AZzzteE745W83m9WN2RjyX8TK590MOQsZ56nrnxKJ9ECcNn0ZEWT7LHt2S443y8zU8xP3bv67Uy9QbQgxCQKgLP3p_clOSa02AF8KSwcFSt26GVKCFV-J9N-DnkpxiY7uKjGCyhLsjJhuDJH-j5HRMu31dm4WKodWqueW3VKjlX1wu-LBH6zIvmqA10-UNYTrFuN94DPQ1yqX7vzxMw9tni0KpF_as64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیافه نقدعلی نماینده مجلس، زمانی که قالیباف می گوید؛ به نمایندگی از رهبر انقلاب به عراق آمده ام، سوژه رسانه ها شده است
🔴
نقدعلی چندروز قبل گفته بود قالیباف اصلا دیداری با رهبری نداشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142842" target="_blank">📅 17:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142841">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که دو حمله با استفاده از پهپاد علیه اهداف سعودی انجام داده‌اند، که در آن یک سایت حساس در فرودگاه ابها و یک تاسیسات متعلق به شرکت آرامکو در ابها مورد هدف قرار گرفت.
🔴
این گروه اعلام کرد که این حملات در پاسخ به نقض حریم هوایی یمن در منطقه صعده توسط یک پهپاد سعودی انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142841" target="_blank">📅 17:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142840">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX_q8yQRQ65k5SesK93XJ4kpTUl6fkzAZFvo3thGlDig7zv5lff0aqZzIMZ0U4t-CCn9NxD_axV8AQIRhZsn1D6RPAd4cLThS31DklaW3XUkizWin6RUmJZWQd7Rn19AQ8xDgwvzarW4kFrsFevRp1B8HrBEdrFnPwqJgmych1x6vI9MPqleljr1EEkrup0Q-vVJ2tUNOiSaBTdWkF7v3qHymoyLENe0iZMesBCp9nWReiKfHS9_iw7mfS6fVR3F24SaxupaUW0hty9x1pdM_hut1YeXPt-cGs2yuO3uIm_TkI3rKTyo0hO7zWAUQRxHiBPJtB-uHR7IN0kOswR7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه اجتماعی Truth Social: جیمز براید، مدیر امور مجلس ما، در ماه سپتامبر از کاخ سفید استعفا خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142840" target="_blank">📅 17:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142839">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
به گفته دانش آموزان کنکوری، قطعی برق در دانشگاه شهید چمران اهواز موجب تاریکی و گرمای سالن شد که به سروصدا و به هم ریختگی نظم سالن جلسه انجامید.
🔴
دانشگاه شهید چمران اهواز میزبان هشت هزار داوطلب کنکوری سراسری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142839" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142838">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پلیس گزارش داد: کشف بیش از ۱۷ تن انواع موادمخدر و ۷۸۶ هزار لیتر سوخت قاچاق در ۴۸ ساعت گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142838" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142837">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7428f74560.mp4?token=PHwbemqSgBdNpJqb4tod_UGn9CGJZNJRc0pmS5WNQwYNUVHn8NUvnZEyFv0rG332upKbr_XS-OE3cJ_c8183jVatoMPNFLN1sV0rdn7I-t0Hkn-lQw03NwLOaMRLd7YsAQmky5qjhlPc4Aiym_sbmbEmmpFRV2EkR1iUyOpBHPhe1a_g9gInho5NRevA5KCnRyjaC10mmcurR4Tjd4YOkSMyA8-PSC1EIcj3fIRm8pm1ep-fMDZ5eEl5efwgSVz3CQFIdNsG6jym6M1SZGAf9t3_vhOLmFFSnWHWLZICS2Qvp6TftgrZeh8lwiCCt3sxknQ-GJsTUxEEx-S0CDRRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7428f74560.mp4?token=PHwbemqSgBdNpJqb4tod_UGn9CGJZNJRc0pmS5WNQwYNUVHn8NUvnZEyFv0rG332upKbr_XS-OE3cJ_c8183jVatoMPNFLN1sV0rdn7I-t0Hkn-lQw03NwLOaMRLd7YsAQmky5qjhlPc4Aiym_sbmbEmmpFRV2EkR1iUyOpBHPhe1a_g9gInho5NRevA5KCnRyjaC10mmcurR4Tjd4YOkSMyA8-PSC1EIcj3fIRm8pm1ep-fMDZ5eEl5efwgSVz3CQFIdNsG6jym6M1SZGAf9t3_vhOLmFFSnWHWLZICS2Qvp6TftgrZeh8lwiCCt3sxknQ-GJsTUxEEx-S0CDRRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش گرفتن هواپیمای مالزی در فرودگاه توکیو
‏
🔴
یک فروند هواپیمای شرکت «مالزی ایرلاینز» که عازم کوالالامپور بود، هنگام آماده‌شدن برای برخاستن از فرودگاه ناریتای توکیو دچار حادثه در موتور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142837" target="_blank">📅 17:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142836">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نایب‌رئیس مجلس: وقتی قیمت نفت بالا می‌رود یعنی ما برنده‌ شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142836" target="_blank">📅 17:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142835">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRKPHkcdEz8eoBWiY2U3pAmJMsh9-C2Vg73wFnziDrg35qy0LHYQLffwYFd2J8wyjO0gsOb8H3ofUq8pnSWO10qaxZ9xsBDfv-Jv8VZtkRsFOOCd4xUemF66qD1rNBICnhKTo81JX8evIIHUlj2jd_AJA6ArwY93TD-sIKpKl49mS7g-dbvpvk_nxEYJe33ZtSGhuSo2BWaltfnZ7o2-ShGa-Ul22d8qfA0NLcn6lPoDMheruE9LTG3HhRXy48ijG7LkZl-0ZJwEryeimuAEBCSU551ZVJBCZ4F2Kzg3QbsHhTYxU73G1a34vSomHeqH0bmB3dJibDNgBFj1Vi46-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی به ترامپ: جمهوری اسلامی فرعون را به زانو در خواهد آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/142835" target="_blank">📅 17:27 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
