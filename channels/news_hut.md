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
<img src="https://cdn4.telesco.pe/file/P2NsLXyJldXP7L6X52q6203ws2NgDAtTjUlDZDOvhVZp4P3jEiL8s9UoU4BgGCS9lJfUSqwQkmu99bIWLtFUHQlmj2KM0gDYQkRB5lO-_5RkoRy9piwaHHVtlInmpyi1c-1Dnzt8I62vuWlffNZve1VvuNgkOpViivJ_ooHG4fR_gq1eZbNH2Yveu6CReD2BE0U-ZpTYnsMC6ViX9EhM1qexogITrJirG1qssbu7B1A7Q8yCjrMfkXbpFUxPU6g4-9WvJPvmIsIYm63HHeUwS70W0stb9qP9Iwx5YydTnj0YrBGJRMUK0SJcMo-G2rOIgu8DYvhVEFFCvm_pxKvoQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-65563">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=OnESzgmsu4BSENvnzK0Ij68T2RK-s087V6FcXQYCCIA4HKrDH5yk52a5lZ5SXk3SJ3B-spD4J9dfv9JLqmnZE7-Hvc4N_RbD5NlolR5bu45haXnOiZTSqvdwHkYT-BVEd0p2yLffRiRHzOh-t5uZhA_J4IAp706XaawCDA_YWrXxnGY0S3u5v1G_GuoN1P-5mTyL7q28LIaDAD8AYJDTHiAhlWMr2hAztX_MXymHHM7aHU7Z9Akx_IkxJVos2Y7Irq45HWlJM-FMMpM9vf6zh7USSvOGlSQEeapYm1TTwEXJUJjF-3ty7JAUCSIIn4-bgUBogr0vFNAqrsndKbhQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=OnESzgmsu4BSENvnzK0Ij68T2RK-s087V6FcXQYCCIA4HKrDH5yk52a5lZ5SXk3SJ3B-spD4J9dfv9JLqmnZE7-Hvc4N_RbD5NlolR5bu45haXnOiZTSqvdwHkYT-BVEd0p2yLffRiRHzOh-t5uZhA_J4IAp706XaawCDA_YWrXxnGY0S3u5v1G_GuoN1P-5mTyL7q28LIaDAD8AYJDTHiAhlWMr2hAztX_MXymHHM7aHU7Z9Akx_IkxJVos2Y7Irq45HWlJM-FMMpM9vf6zh7USSvOGlSQEeapYm1TTwEXJUJjF-3ty7JAUCSIIn4-bgUBogr0vFNAqrsndKbhQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از سوی اورژانس از لحظه اولیه حمله آمریکا به شهرستان لامرد فارس
@News_Hut</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/news_hut/65563" target="_blank">📅 21:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">من از این کانفیگ V2Ray گرفتم، سرعتش واقعاً عالیه
🔥
حجمش نامحدود واقعیه
، بدون قطعی و روی همه گوشی‌ها کار می‌کنه.
تست رایگان هم داره با ضمانت بازگشت وجه.
تک‌کاربره حجم نامحدود: ۲۴۹ هزار تومان
دوکاربره حجم نامحدود : ۳۴۹ هزار تومان
پشتیبانی
👇🏻
@khadamatsup
کانال
👇🏻
@apkdownload_sup</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/65561" target="_blank">📅 21:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
♨️
فاکس نیوز می‌گوید رئیس‌جمهور آمریکا دونالد ترامپ «در آستانه دستور دادن به انفجار یک چیز بزرگ در ایران است»
@News_Hut</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/news_hut/65560" target="_blank">📅 21:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK0mWQ58W_OBpyPdF6gEdIEl5DqLuetckNv9fMnmaww1lVdRFw4IHCuw5ZBda956pTrv34iV-e6OQyhEMpHNGaCNIvFhqBvrsrepO79bAodIgWxzwoiLXk490tarQUlAyr1gkxHShgNnT-Cf6w2atPnOrGEKf2fuaSz6k5DXoAr5DAUcaCU8jKSIf8b0bC-r001PXOZ4Qu4agaTqIweWIqOnk7QegNFdoB8kj5AOTCAIfXjiXdQCO9qyKtR9FkhH3SA1S6-CejAe9j5eGVc-qZxM9GPqI7V-VGArGSvjlUmn2FlGyw2GyxY189QGjYcxMT7KaGNInQf8PWbE5aCjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اکسیوس و‌ سی‌ان‌ان:
یک پهپاد (شاهد) این بالگرد آپاچی رو منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/news_hut/65559" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
منابع خبری آمریکا: احتمال یک درگیری کوتاه نظامی حداکثر ۲۴ ساعته از امشب وجود دارد. آمریکا در آستانه افتتاحیه جام‌جهانی قصدی برای گسترش درگیری ندارد و فقط می‌خواهد پاسخی سریع و قاطع به عملیات دیشب جمهوری اسلامی بدهد
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/65558" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
‼️
اکسیوس به نقل از یک مقام آمریکایی: تحقیقات مشخص کرده است یک پهپاد ایرانی به بالگرد ما اصابت کرده و باعث سقوط آن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65557" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02089086e7.mp4?token=a0i32dyVoZQlk0ebg-3TU-JYehF9Q_umokHfSCCKNC-2cm6yODe5G2ISczGkgl4nNH3-wKbCX3FxJP9b-m5gPdPJy1qgThET8_dfEPwfB71y2hQXc3sR3aCDA9XgmJUKeBKzi_dyGcdml4DxbpRZGaR7_kvSNLYItIdFUXTv1q4Sbvp0Ty6pKwDqw1wxwOfFpDySYRCKkaqJuMZ1OTtsudC8Bph20_POeLkkHnZOb1nbhsyhJlsooBvqucVMBxZ1OmZAqaFUeSp4PZneeTxdyotJgOWsk3lEE7USTus3U-XFGCOIIYjWIFwxbDyo0QeH0QESQVajztRAPRVdwx2HtXmBTiD7TE3M3hW-lpNClHWtHDGgOeOkfahyTU9CaTSdAVelDceanThMRuKP2a7kPOaDfZk-EjdKfTfOXGmWCajcjrM60VG4dPnPhfy4hy_Dyo3tFeC2RO_w081Np1r1Z_KIqzZQHQcXSWLknbQbpMte-FVa9rpDHfEm_bkthXmJkR6Nu4iSD-oC8UbiZNI4PtWRz4VV1NNNA3AOxM77CvwBNo8bUAXbm3N3oopGUQVfuEKuHXwc5tCH3xLJFNFGM63Wtolv0gHz9Pa3o1ARMvTN28jbJOIQ2trm4L0XAa7I_pc275wcP1cPf7a7EP9uzaZI4pILabrwaT7fKfeqx1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02089086e7.mp4?token=a0i32dyVoZQlk0ebg-3TU-JYehF9Q_umokHfSCCKNC-2cm6yODe5G2ISczGkgl4nNH3-wKbCX3FxJP9b-m5gPdPJy1qgThET8_dfEPwfB71y2hQXc3sR3aCDA9XgmJUKeBKzi_dyGcdml4DxbpRZGaR7_kvSNLYItIdFUXTv1q4Sbvp0Ty6pKwDqw1wxwOfFpDySYRCKkaqJuMZ1OTtsudC8Bph20_POeLkkHnZOb1nbhsyhJlsooBvqucVMBxZ1OmZAqaFUeSp4PZneeTxdyotJgOWsk3lEE7USTus3U-XFGCOIIYjWIFwxbDyo0QeH0QESQVajztRAPRVdwx2HtXmBTiD7TE3M3hW-lpNClHWtHDGgOeOkfahyTU9CaTSdAVelDceanThMRuKP2a7kPOaDfZk-EjdKfTfOXGmWCajcjrM60VG4dPnPhfy4hy_Dyo3tFeC2RO_w081Np1r1Z_KIqzZQHQcXSWLknbQbpMte-FVa9rpDHfEm_bkthXmJkR6Nu4iSD-oC8UbiZNI4PtWRz4VV1NNNA3AOxM77CvwBNo8bUAXbm3N3oopGUQVfuEKuHXwc5tCH3xLJFNFGM63Wtolv0gHz9Pa3o1ARMvTN28jbJOIQ2trm4L0XAa7I_pc275wcP1cPf7a7EP9uzaZI4pILabrwaT7fKfeqx1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو یک سرباز چینی در حال تمرین برای فرار از حملات پهبادی FPV
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65556" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اگه بت میزنید هم اصولی بزنید!
با این ربات میتونید هروز بین ۱۰ تا ۳۰ میلیون وین بشید با کمترین سرمایه اولیه!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/65555" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
فووووری مهم برای دوستانی که بت میزنن!
یه ربات پیدا کردم که بر پایه هوش مصنوعیه و کامل شانس برد شرط‌بندی هاتونو بهتون میگه! یه هفتست دستمه باهاش ۸۰-۹۰ میلیون روی فوتبال و تنیس وین شدم! هم میشه ازش فرم گرفت هم همچیو با هوش مصنوعی آنالیز کرد تا هیچوقت لوز نشین
😐
•
@Algo_Winbot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/65554" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP0Wl_7HeclNgSHG7z9zT0NKMIxq5WGI6_kS00c4EqGyrr1g7fvhYcnKA7Kd2f6TuAcd1-EGIftP3v5I_vIfumvVpIE_eb77QMcCCo39cSnb793Co0hWgkXoK-uAZN9uGPRAn1QY0cFmMPBYTrKAME0ikbv7M7NAFGWDK4COuuwqeiWpnS5XpMCmyFcEY37mZrAgvml2CpOywDzMYLNVtTj-fbQcZ8hW5I6c2ciK6KEaGSZwei5c96mkHOQr5yDFJmhixbKJJ0oThbfNCR-wP-unFgvNHkogUcK22xuJXme9w_249XnUrd84CfEWJNwaEzcTbQ9_EuPnRXRQHLnEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کان نیوز: ۳ میلیارد دلار از دارایی‌های ایران از طریق یک پرواز از ابوظبی به تهران منتقل شده است.
بر اساس این گزارش، این انتقال در چارچوب توافقی انجام شده که هدف آن توقف حملات جمهوری اسلامی علیه اسرائیل و توقف حملات اسرائیل در لبنان عنوان شده است.
کان نیوز مدعی است یک پیام آمریکایی نیز همراه این انتقال ارسال شده که شامل تضمین‌هایی درباره توقف حملات اسرائیل در لبنان بوده است.
به گفته این رسانه، تبادل پیام‌ها با میانجیگری یک هیئت قطری انجام شده و هواپیمای حامل این دارایی‌ها در تهران به زمین نشسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/65553" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=jgdd7VpITApw08VWBCo1xhRX6RkVGdIgTdJFM5xehVLSw1cymKt0lhcbGSv-GZ_lfmG4Vl0CmF1l2dBC5xmxnQHd0mwsW_QNNngGA9u6IcSpElO6hbSq9wsEC88eOJUxjYFGCwALDTpS5dc6dbDP8JMim-A9gM8pe-tRY6ySOXv_Hp0qLwHSLRWZE7_vz7ZhgFBoMuK1otaqqWND_rxkqnkAIHnJYjD2AjM5rQqk6mK2MZr34UdnL49_KAyQ472dgMzJNDUAXjYPCMB50RSqkjly_D1RXs9SOYqpt1eB7InuFQuFSCNpHGgvFC8fu6ubKZEX61wKeEVDm3nyJB_eAlGLKZo4CIilpYvR5p9CgFOVWrT3BN5cHh2BIN77SY7eV17DsuE-TbbbYDc_QeWe727517OEoLCFEgUm7svbMCH1DtFqgABZbcXWK4kOsJmG65lTk4_QirP4E-A2ZTtdDwfNcMGA8w2AOjyKKONjAZg5WORG0Ui4SIiCeoW9aFHSo3iqGfW0ufVnKL_8GMYX6kVBvZ_766OP6mTM88FFDJ9NWHenh-g0nxfXp-wXqkiAM1QtAI7NIt1nM7MUxptNVHg8oh45VS1sFXgBjjj37KR27bYr3t_mrMJTNs2nUIOoWZO00Qgtx57R7rHD3BtsSXL0LxjdWW0NKhPJngOIZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=jgdd7VpITApw08VWBCo1xhRX6RkVGdIgTdJFM5xehVLSw1cymKt0lhcbGSv-GZ_lfmG4Vl0CmF1l2dBC5xmxnQHd0mwsW_QNNngGA9u6IcSpElO6hbSq9wsEC88eOJUxjYFGCwALDTpS5dc6dbDP8JMim-A9gM8pe-tRY6ySOXv_Hp0qLwHSLRWZE7_vz7ZhgFBoMuK1otaqqWND_rxkqnkAIHnJYjD2AjM5rQqk6mK2MZr34UdnL49_KAyQ472dgMzJNDUAXjYPCMB50RSqkjly_D1RXs9SOYqpt1eB7InuFQuFSCNpHGgvFC8fu6ubKZEX61wKeEVDm3nyJB_eAlGLKZo4CIilpYvR5p9CgFOVWrT3BN5cHh2BIN77SY7eV17DsuE-TbbbYDc_QeWe727517OEoLCFEgUm7svbMCH1DtFqgABZbcXWK4kOsJmG65lTk4_QirP4E-A2ZTtdDwfNcMGA8w2AOjyKKONjAZg5WORG0Ui4SIiCeoW9aFHSo3iqGfW0ufVnKL_8GMYX6kVBvZ_766OP6mTM88FFDJ9NWHenh-g0nxfXp-wXqkiAM1QtAI7NIt1nM7MUxptNVHg8oh45VS1sFXgBjjj37KR27bYr3t_mrMJTNs2nUIOoWZO00Qgtx57R7rHD3BtsSXL0LxjdWW0NKhPJngOIZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر ارتباطات: سیاست وایت‌ لیست در کشور شدنی نیست؛ به طرفداران آن گفتم ماستتان را بخورید!
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65552" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/news_hut/65551" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbKcRhVb91N7rDaW0s0NYT-ulqX2meXWkowASyPYxanNOK9RJ17zwAobqigkKTGt_Gb5kznhL8_QNXcRPGfr2IMIXtLq5UUDKZjuiotLCzNLg58RbpR02zUuBXmsaK64DbgplFI0q_b6aQictSM2UYVzd4aMIvGuUkxJBNOCN7b2opAxU6OSgXMVssOt9HJ6f4p8B853eoNVyG5XRPPEVxDBdljiiLoeQ7g-2TDqAtLLpzBdORvBKoF8DpPPAq_dwhI96zvhkSeHpw7elwwcS4ycpjVz1DvN8Gjd98O3sAZWPSyVWXi64PB2-wdE9bnoAchFZ2gxGPFIhxmmUCSw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/65550" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIU1EIfDq76qOM-K3ssMnFPBreD_MGUW8Qu6DsVCwAq_2S_QNtaX2hTxz98VP7tADEkqNiXp2GsejGjB8jIZ2Y63tYRHRSbpr6HwlGRlQRy8Bg_jlM78f8aLR_sCE5yfRM2XEmeDFxHznTO3m6RUkl4bAunIFUIa3XiH6HHRvAjl63-zhJlHubX-lpQMiv38kkmGfSBE66OLXGTBwxb1BaOlhXH6lF6E312w0n1gGJ5fa-fcM01sae5s2H92lpHVUpJvs9UA2-POnMhNCCb50EOdzaov1eKzXC8QQbeDpDNS8f3aHvqsfYUTieyx7eLWGDz48tKDh90nhf_ZbVskFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛
رئیس‌جمهور ترامپ از طریق Truth Social:
من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده باید به این حمله پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/65549" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65547">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxzsUUg6tvCCqI8wGPdtKWzGmIiuDeJtpo_X7N7LcopkmsGOj9EdfyjNV83_6_W7xb9AgHg5RFWsJhcxymHgPCC_t6OIoHUb_ODJfI0jIORFc2_JbX8UrA_-hPPOcgYNcnAJFbAwB00eo1uPsaMzOX1VplVLAX6pqLjVnHDfTUCxHu4PEv774N4VYW7pPcV-KNMie7wxaDBMDCfh3rZC7U4wk9svx60xRDgx39conusjEtEnDJoVCPw-iuPZF2EPMtkmWt1OKAUCBag9lnFtvkpi5gBlCQG3OjYFOGD9_RwXqD5GIk34zagNSrGCHQqjHfxm6LDvARlvBs0Vr-ptKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جی‌دی ونس معاون رئیس جمهور آمریکا:
جنگ ایران یک سال دیگر به تاریخ خواهد پیوست.
ونس اطمینان دارد جنگ ایران به باتلاق تبدیل نخواهد شد و یک سال دیگر به تاریخ خواهد پیوست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/65547" target="_blank">📅 20:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65546">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
العربیه:
حزب‌الله اعلام کرد دولت لبنان باید روابط خود با ایران را اصلاح کند.
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران برخلاف منافع لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/65546" target="_blank">📅 19:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65545">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-b1g_uaQHCP2unpjR9yrvz_EWVImhlZKxX8WGZNERe1lK2wVk6VMyZq_K9gvhxVpTxLay7lv6lhOC-kSSzgn38Td4sDS_3KAZ28_EwpINNkYO3iDsUKGE1QRANKHEWGdzzMscSZ_5yTHxbZlOP1z3zKPeEZkKIMI2BIYOGiJEruVDEI4z0WzzLT0KuDYkAi0uCfh89KzEf8lAXxKy2U5WoYGufF8blwmX76_nqP-hScVw1iorIsH5b7vPuZXf1xgsAGdC3C2L-0MP96vM-7MyWs4Yz-UWcLyTniIekgmvEI_NoF38LkfbApaF_t9Scp-i8akqkI-gwbjEj7Tn7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب رسمی کاخ سفید در X
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65545" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5-2uEF8KpZUyNsRPFCjTbx3iy7SdOXiocaslQro2YWlonnpeYIhbw2MQjGU5kbYbI0CAV4nPa_JGAyGrIBjSo3VpHiOpzjhnbY-VEJvPK3kbSf2DC-T5QYmjN11V4tjbGBFbmegvkD5uedfL5VaFMdD04YbDUrHiqaq9VzBOkzKSHPGbLhDLrgYH8yQnfXZ8jhE1UfJxYGKSXsL9bObfgvmxTyaGkQudGTniutBqGQvS1VDzgKjYMPJold1tKOv-GywvdNLuhpvkjJF8rs7lQUYAMJPuBGwWEb_fjebQnIys3gBI9E7i_MxVDeig6TdNNDPylTp5RvxO2AwhPmcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=OGV_YRdssRKncwyaHhovSrCVIgODbH36Hz0uMUm-lzM61XmFD-SMeXO6CZGLDhPL48IQj6jK79Ztb9qk530uhAC2WrSBTAmvE86I58-RVC6Z3FLGpjsVLmMxhxGT6aTGn5JzVsNUvu1KgcLiKkOMpGitCknpRVZnmMKKh8MkaMgMsNUPBp5oFKR1x14KFuvHSlEndr4-PHBZ1oOg_A2DnZJXRPXLdu2zBQiVXEqpGYxKNEozYNpxTvT1UrRjpARuUxs3Rk3b_9Xh9gbOu0hrc6seodzYjH4aZpMrG-ZhxQFve097Yby1x3yIr0yy2ISVq4ZtiBJ1EXFzTWHKLBu2OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=OGV_YRdssRKncwyaHhovSrCVIgODbH36Hz0uMUm-lzM61XmFD-SMeXO6CZGLDhPL48IQj6jK79Ztb9qk530uhAC2WrSBTAmvE86I58-RVC6Z3FLGpjsVLmMxhxGT6aTGn5JzVsNUvu1KgcLiKkOMpGitCknpRVZnmMKKh8MkaMgMsNUPBp5oFKR1x14KFuvHSlEndr4-PHBZ1oOg_A2DnZJXRPXLdu2zBQiVXEqpGYxKNEozYNpxTvT1UrRjpARuUxs3Rk3b_9Xh9gbOu0hrc6seodzYjH4aZpMrG-ZhxQFve097Yby1x3yIr0yy2ISVq4ZtiBJ1EXFzTWHKLBu2OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیروهای اسرائیلی در حال انجام عملیات تخریب‌ در بیت لحیا در شمال نوار غزه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65543" target="_blank">📅 19:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzaCheX66aYmYSyIFm8VDDdOpql2aY2Zpy_M0kcnvMdd3dLwraREDzxVUxPTEP55tjEknwIoP3FrfjnF8aQxzdxoIBHptdaI0f24fNqlTx9o6IrKnqBWr5T_-ptyhlmHGKs_b4Yv3xK3cO7NQ3d9NX2HCdsTbOLEs3mDnZX2oIogYmyEpcBkrL7zWd0tCHzG_i0Wd4tFSlWOscr3mGmGs2Mpx-Rtrcf7fha-TwMov5UrxltJx8gYrMweHz8DV5fkKBOSBw0xqylZ10xnzmSYVDmJtMdl2GUwV8mVcNjuIW3u__61rCdJn2cJTJ1ZtD6T1b-icL0Zrwqg2lshAUZBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوژه و اخبارِ موثقِ بدون سانسور روز رو از چنل [
اینترنت نیوز
] دنبال کنین
👇🏼
❤️
جهت ورود به بهترین چنل تلگرام کلیک کن
🗿
جهت عضویت در [
اینترنت نیوز هات
] با محتوای علمی آموزشی
💦
این (
مـتن آبـی
) رو فشار دهید.
🔶
اینتر نیوز گاد فادر
🔶</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65542" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65540">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4KHnhwLRULKp3v9Ng5cvP9GF45ZMR5QUhFEYkgIA3yOHvfUrjqmX-WbZuaYo060zYSBZTLMhL7b-JPYLJTtROdH26Dm8ByrHdozbsvlj1i2HGxGV7NJZsXGlO3oSiIzhh6JhGH0BNcYisCvLmC3E2B2v0Mxxy123x9WY6xQHBF7N9t7xmq1f0KX4WUOTAYDMwDWRB-n4Mlfjyz2Df0BG1NAVQ4NESSuaGAgliGzveKAwAOyFU_F3KmCYUBDt2OveUTmfKNaHm7ry70JiWau2fLXqttJ6exXP2UZsZwbt4hw5725CCX0a2OkPe3KVPIyeX-sib2sYwSqTlxpcj2j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=dM7D1y7r37nSZY2ZjxJoLxaEIAZhx05FRJc6bOk7eoIPGm2pg7xiEuc-8fQr0YfKGNpZ7x9PWUQy-HXCnjhfrSeQIUNXfXIglOIPc5fsX29Y7_TGDnTwa9suBotZxCdPXYfcn2VmIZXCtkBvIaEqq-hoO_tG1VDvm8BJbNfHaRuHFH6QByDtEVRVwJF615SML-C2DpuKXGOUc6QM-gkGCasPDosafYg9bd-ZwNxT9ld_FI7Mscw21EucSjJnZXC3nX0UMgA8OEWLw1IZzQM6iT211OWUbLCtfX5MTBeJDwMvths3tQyK8d9FWr37dW0RSS9yP7dZF4mgwRdZ-vGNjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=dM7D1y7r37nSZY2ZjxJoLxaEIAZhx05FRJc6bOk7eoIPGm2pg7xiEuc-8fQr0YfKGNpZ7x9PWUQy-HXCnjhfrSeQIUNXfXIglOIPc5fsX29Y7_TGDnTwa9suBotZxCdPXYfcn2VmIZXCtkBvIaEqq-hoO_tG1VDvm8BJbNfHaRuHFH6QByDtEVRVwJF615SML-C2DpuKXGOUc6QM-gkGCasPDosafYg9bd-ZwNxT9ld_FI7Mscw21EucSjJnZXC3nX0UMgA8OEWLw1IZzQM6iT211OWUbLCtfX5MTBeJDwMvths3tQyK8d9FWr37dW0RSS9yP7dZF4mgwRdZ-vGNjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر صور در جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/65540" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65539">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl6u-Ds7n6UMyK_e4lqjNoFVzi5W9rTJb-25N0jB6PH52lurg0W-jxqPY6a6eoeOmRSner6QiV6FCIvhE_9IORTy0YAG37TejXgYPNSl5YbxNdpGnufFQBDqMnl1fwjcBXuWNSMNq0WkArTIv48sAMlZPIfTGpvWnxtgQyaSiCE-IIcGzx-Y4c4_tGhzoY-ZqDyiWRt70cGnhS-n2iT98AzcZj6wMqJNCnrUeA4ptpWA70uP_ZhJu26I2sfmCUwlfG59ooKYKDMH_ccPNazm0aLnOw8DQ-CXILnjZ45VvVAsLEUVAbFib5gygFNWosL23cnOcbTyemgaQfOz65TF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس ستاد کل نیروهای دفاعی اسرائیل، ایال زامیر:
نیروهای دفاعی اسرائیل هوشیاری و آمادگی فوری برای بازگشت به نبرد در ایران را حفظ کرده و همچنان حفظ می‌کنند.
تمام سیستم‌های دفاعی و تهاجمی ما هوشیار و آماده بودند. تهدیداتی که به سمت ما شلیک شد را رهگیری کردیم و به سرعت و با قدرت به ایران حمله کردیم.
حمله‌ای که در ایران انجام دادیم، آمادگی برای ضربه‌ای بسیار بزرگ‌تر و سنگین‌تر بود. ما آماده‌ایم بازگردیم و ضربه‌ای سخت و عمیق‌تر به ایران وارد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65539" target="_blank">📅 18:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65538">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65538" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65537">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv30-5M44R7FHgi2M0R4AuEPr5EH6VTWdcf8YDBLSl77LKcPLa7J3x2FpgW67DpWbGCAWdQCSZbKQ3Q6jJszueaI5jcx5GhzFPKRoVG3IpuReOsAmAfwOdFy4ow8ax6Hovfrm3dKgPFRoIUXQr1RkX1M0WFP-CaTgeiaYAe-_dk7eBqpLpTtsaG1cVV1IItBNtL8Xij_lkpvG0K7FFiXxMGOG8ju1MzEPO_05MRjj3gleQ_RT2IS28tUjRzcHawDquUGsmOk2eN00IeIy5xA2sBB1bkVWods3vW0rCC4XPXkS18zwck0CXCqs2uLChuHLsbbHmUj0OGkKkaGE-MIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل در حال شخم زدن شهر صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65537" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65536">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
♨️
پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65536" target="_blank">📅 16:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65535">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5vMd16IFSeybtqJZUKK6r-z-rADIZPVqG9QWSzOIwPq_zlIFQGMWcXR2QI2WarrErgeRKDazmkaqv13lY03l91b8tJAUA3GVckLb6ijUtPwGR1qYOUG98i4CCTkRD2zC0eZmEvfWqKhMONbrFKX5HQnZmIhkQJAePRCLi4Vy5QIQO341OOpfNpRf-ENTiO1r-nDbEOtMTYO-Cz_g0YYSpAHTvb6zIGDF2z7yBXmKkdUFq1pCZr0bjmjq4QyfxQS-OhnTQ8Z7frdz6KEUEkqMaGSqMXtlb2Bu3YwIhyLnWHsx6l0lKEir-yD0OzZ9dzLhQpZtVoVGSfEJADoCbvmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65535" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65534">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km3egB-XDG_WotW2KUlHjUMDTzJUpn-2dFPNuk7G0IsUwcV15JjsbAGKpErBjadSJ2-Tk-HGIxULnBxbGENjD64etvhJSvspVhTz5HWs3M66q4LKeNRaCsDaNE6ndsKdJqVmWz-jS-Gpl5DnTlKhLK9MySdPnE2YMwsS2xebSWjfJM3-uK35AmyorqFH1EoRL_cva-lIGlP1jWbYakn84AV3bhssWXmk6P4Zrrlg7r_x2_37S37SFtth4hi0w4_CB-qZFBbGB05SipQ7d7X7MTAlTs5fk11ncah7H7BNuOec4_qUfd0_fcuFgarFH8bvwWrCNdnFDvDcprgkMmf8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اکونومیست:
ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65534" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65533">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=f_sEOfA7e662wv_cj8TgBnCHG5c01mfl_2nH9sY_iQ7q8qqR1VrcdTbbI7LxyoNVbzmMtYoFLz8IbYV6a33BCMMAFuYCWf03ZUkMZnSBXz5OmzojrK29_gcziMk8UeU-X3cs9TR1Quc7gqC8vyuvPiQUOaJWNRNPj25ffAbCxyAeIkR5Px20saywVoOdmicm1K5F7Pn56Dqs0PJApcF1DslzHeCafoXiqE7D2aoKPpR59AJWQ9tHQML5AeMSmhXcfqTz4LF3TDUjkf3Y38X0Vp-yKBUFaayzL8KdXDjmbgrfoUX6codYkbjeAqotRQ0FLYyUUb808oP_PJpq8UaXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=f_sEOfA7e662wv_cj8TgBnCHG5c01mfl_2nH9sY_iQ7q8qqR1VrcdTbbI7LxyoNVbzmMtYoFLz8IbYV6a33BCMMAFuYCWf03ZUkMZnSBXz5OmzojrK29_gcziMk8UeU-X3cs9TR1Quc7gqC8vyuvPiQUOaJWNRNPj25ffAbCxyAeIkR5Px20saywVoOdmicm1K5F7Pn56Dqs0PJApcF1DslzHeCafoXiqE7D2aoKPpR59AJWQ9tHQML5AeMSmhXcfqTz4LF3TDUjkf3Y38X0Vp-yKBUFaayzL8KdXDjmbgrfoUX6codYkbjeAqotRQ0FLYyUUb808oP_PJpq8UaXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❌
گلایه یک زن حامی رژیم (پرستو) از رفتار بسیجی ها بعد از آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65533" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65532">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
نیروهای رضوان حزب الله اعلام کردند بصورت زمینی وارد شهرک های اسرائیلی شدند
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65532" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65531">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
شبکه ۱۳ اسرائیل:
شورای وزارتی کوچیک تصمیم گرفته هر حمله حزب‌الله به اسرائیل را با حمله به بیروت جواب دهد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65531" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_dTkG7ShZjxn7qLWLaeBbuSeQYBoX09sV8-LIn-ZDHO4w32yVQrLKTTsUF9fxmnz1RbStxfES7muiM5ldgnIOYPu6EUDAjzjFiTG1t2LocrGddgn2GO1ePYmDrkO-qSqvMs869cyNjqpEFwUlGO7MV_gjTGHfbtIzByYdqjxODh62Mry4i1kCDau-7jHFvXHSj9INqDDb5D41R3Zb98iKJuwGhJpjsQeRyRdsUdB2Pc2kFmiMZNaxMPzIyKnE0egqKoSw5pJh3EUTg6MA_jZfDAQVQyrpDzXm69xYL7ESN4ihQgwT91bQ11s-95YfDlD3NUwhKrBF0QNvmcrVu33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHzXqbbY_k8iLZ7j73ooZpKBUFHsRSFNkAeE0qndpevylv3BdyQcR78dzzvjAlcKrqOBGbIlmn4OaFnzrTWW0ONStVvy95WaMo0ZI03i8l15dImOMQnYU96BS6duj6aMDHykEAoaRSAg9eRyQz8_ltQLIuwO0rl3HVQBxnhzbBmW9IvaY8_9OgjDMNFkebkUvNP9uVStpZ0fKeN9CJ8aaWgJvu07AxNJgupW1fi9Zx4wuRQ46gVpH_bGumJTHZUTaYh8AUKoqMzMTg8srzuHxn49jxmRebrQ7U_IWBcUO0L2oeHnC5rLMhwwXG7x3tt2WjbcTeDNUhBjjZj1FXfgSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
حمله هوایی به شهر کوثریه الرز جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65529" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ستاد فرماندهی مرکزی ایالات متحده:
دو خدمه بالگرد آپاچی ارتش آمریکا که در ساعت ۳:۰۳دقیقه بامداد ۱۹خرداد به وقت ایران در نزدیکی سواحل عمان هنگام گشت زنی دچار حادثه شد و سقوط کرد توسط نیروهای آمریکایی نجات یافتند.
همچنین علت این حادثه در دست بررسی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65528" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=bRndwL-MhG818Hp0wd9jk4KFsaHFk3f6dAPkoIY9twX4rGWFTgkzGAjnCt4CXR2CnLPCrXqE7ytEDKknf_oEqd4hADVnuH6wwYmEfkGYjRrGvveK9KFBr1uQSAfI9FrDMkG2tmUg7z5sZarjIM-hDfuhQfnfstEO7YI1Ih0JgR6XeMXVnk_j7k0IiqIVTtrmIX2smaPMFLOQsK_ZBVvX6piJ0Bjk0DO3cMW_DCyKDX48oUQVcnJeCbYh4xckqKSfMHfmdDITkkyUPw7gdsfzP1fIMo7_UYO_P3Phj3-T50CYa1dTZggl_A_uquG28RLNXc8Wtk7JMFASxhZRpTuuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=bRndwL-MhG818Hp0wd9jk4KFsaHFk3f6dAPkoIY9twX4rGWFTgkzGAjnCt4CXR2CnLPCrXqE7ytEDKknf_oEqd4hADVnuH6wwYmEfkGYjRrGvveK9KFBr1uQSAfI9FrDMkG2tmUg7z5sZarjIM-hDfuhQfnfstEO7YI1Ih0JgR6XeMXVnk_j7k0IiqIVTtrmIX2smaPMFLOQsK_ZBVvX6piJ0Bjk0DO3cMW_DCyKDX48oUQVcnJeCbYh4xckqKSfMHfmdDITkkyUPw7gdsfzP1fIMo7_UYO_P3Phj3-T50CYa1dTZggl_A_uquG28RLNXc8Wtk7JMFASxhZRpTuuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از ساشا سبحانی حرومزاده و آقازاده‌ جنجالی حکومت درحال عشق و حال با پول مردم در خارج
تو این ویدیو به دوست دخترش یک ساعت طلای اودمار پیگه به ارزش چند ده‌ هزار دلار هدیه میده
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65527" target="_blank">📅 14:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65526">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65526" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
فاطمه مهاجرانی، سخنگوی دولت: میزان قطعی‌ برق در روزهای گرم پیش‌رو به میزان همراهی مردم عزیز بستگی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65525" target="_blank">📅 14:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=rzrZ44NUsa55ziP7hUbDTmqgtlLo7dBvgyJm4D47uiPJLZjcGFRB97chKu4ee8iftBfzv8uCSoPDr32SJMzLZ3I4H_cLL9hgyVbyRNR916WTDd5eik94D2-1_T59D4g5Dxz3dLoXIUPFtUwjW1T2fiVJlth0piB2VvsM5Nee25rOeS1F-jsYVmzDON_d0anToM7KDGmjW9iLo5xYx_jnLOoEoFkpoNm-3M0o57S0m5sRODS_CSJjb2Dkh_QpNSjq9hGrb55sX6CDaql2uvHzqchHijLveylzxAS9OEzPhcrs9EGYTE9peOdVQRLgT8c2Z_DaRHfA7BZaqN2GN2DWO0ejYw8LgAE-_J8-uj9n7RfJW_pebnyZbr5-vMkWsQGiahcPKFLzLzqobWTdn_KVtzykusuGsznfOMP0YREkb0AnG3KpbhZbQYyIHbEyob8_yd-eLvThTbtBPgkYccj4t3k12QDWjFAanMaFXjLehl617ju4PZtIHllKL7ISwgl9NJhtvuKpCjaFdZ9lW6GBdjr9g8r2LIKUMtTIXdkeNvy4p1iSUp51NQ-hriaW2Op7n5tV4Bw5-zlgljc5NQyJnFEqSm5YfTch0qbdZviTl3-RxPXH_D5Z0tkmIeMdYVYOgqFCPznyKM-4ZuQIiBX_SZZsoI-KcsH6sATu0knP-j0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65524" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
‼️
مصطفی پور دهقان نماینده مجلس:
وزیر ارتباطات دستور داده یوتیوب بزودی رفع فیلتر بشه.
«در صورت رفع فیلتر شدن به دلیل تحریم بودن ایران درآمد یوتیوبر های ایرانی قطع خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65523" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65522">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=Fo3IqWkfzRVAq806_2QueiOMKulS2zr_CmjQ4IxqpFxvRL0fv3gG_Nx6Dy2iQxw3HPuLY1hl6bwsSp7izjqxisplQD0bxE2RbrTeNUzSLufZaGe0CZPgCuTM7mfQiev0tddgpvr0kfd4oAKlSkl3iPZ2zdLVQAn2rglz8k5UdaWWCP1Ttby8_3K7ZjtYDvUaTiPJ_IGNHEgM58PrdL2GRdqh8dojetANqoS9_8bcJq-jENmPTm7F38F2eZJ4jANbIL88tS81Vzb5usB-D0MIi2vuGwcokn0huTRqbPewvG9-IlSzhcBnHuKZD8ONdgV1G8pLq10d-04qb91bVEQZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=Fo3IqWkfzRVAq806_2QueiOMKulS2zr_CmjQ4IxqpFxvRL0fv3gG_Nx6Dy2iQxw3HPuLY1hl6bwsSp7izjqxisplQD0bxE2RbrTeNUzSLufZaGe0CZPgCuTM7mfQiev0tddgpvr0kfd4oAKlSkl3iPZ2zdLVQAn2rglz8k5UdaWWCP1Ttby8_3K7ZjtYDvUaTiPJ_IGNHEgM58PrdL2GRdqh8dojetANqoS9_8bcJq-jENmPTm7F38F2eZJ4jANbIL88tS81Vzb5usB-D0MIi2vuGwcokn0huTRqbPewvG9-IlSzhcBnHuKZD8ONdgV1G8pLq10d-04qb91bVEQZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون با کفن رفته تو زاینده رود و از پزشکیان میخواد وارد دولتش کنه تا مشکلات کشور رو حل کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65522" target="_blank">📅 13:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65521">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=MQANnWiR0VVQfH6Obfp_rGCR5Lmy_P5jQlQ7ZCpb4Qu1ZQZSoXeU8qNyn23DNgml8JLP0w35zN9ULPVp2nT53VBUjsRVDjGilPsemvOES5YJaZD2cXzE5vuIHm3lQ7C8_-XKCZNdTOjqWgFVTP8uYXdTfqtCx8yokMXodd7gM-aBuN5az9dBRGs9uju9NPMZhAwQnMoutGytQofbG7hfKUBWmYKGd8ZwKTYH6WViU2XApwLw3C0WNRX_LoKm_2j_65IkJuWdZPCvg63_KHLTt2dSPvvjhGvrYiy3dQ6k9KYZmCl9J_4WpNinuiKQdhoah9YpH8kCWiJdoK7oOr5sfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=MQANnWiR0VVQfH6Obfp_rGCR5Lmy_P5jQlQ7ZCpb4Qu1ZQZSoXeU8qNyn23DNgml8JLP0w35zN9ULPVp2nT53VBUjsRVDjGilPsemvOES5YJaZD2cXzE5vuIHm3lQ7C8_-XKCZNdTOjqWgFVTP8uYXdTfqtCx8yokMXodd7gM-aBuN5az9dBRGs9uju9NPMZhAwQnMoutGytQofbG7hfKUBWmYKGd8ZwKTYH6WViU2XApwLw3C0WNRX_LoKm_2j_65IkJuWdZPCvg63_KHLTt2dSPvvjhGvrYiy3dQ6k9KYZmCl9J_4WpNinuiKQdhoah9YpH8kCWiJdoK7oOr5sfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آذری‌جهرمی وزیر ارتباطات دولت روحانی و از بنیانگذاران فیلترینگ در ایران: اقدام به قطع اینترنت و فیلتر کردن جوابگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/65521" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65520">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65520" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65520" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65519">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuUld8HMZrPAdVxaaFIxC9u3OI0Q7mK5DY1aMNBBor3J5z8FIhKKjSF9HVIFkQ5laH-cS_o0isEuTk8QNKu9yYz9vZmPotu7EsTq9MPSNN3QvaQM9efw3QpUNydPkc-q2bTAuAmNYUSPXuoDKuYUT0guwFeW5AnrwXafLKDVZPpGisjbMJ4KZTwd7zd7aLPB_W3EzQjNRIGKgApRIxtt_dada4zRGIHeNJBeHv3o7dxtUlz4hE7kXR1vSnV4vUsIdPX6AzPAk1eQtHdZxEbjEMsUWplXM_vo2ep15a_dgVYFcUED-SOcXnZUVqoZpaIYEq5GQ9nu93YVemCeP18_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65519" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=BbgB484KfhmoFwCTwMC-f8sjNlEygN9MnlxURApQlvHXUGld7uAOofCPp_QWQCJl4fBY6dHX7i1I3zugTyCurd1YwpUfkP1OwnhHYtEXq6tWOMmIHq4k9cSiPAObc8vT35aFUDGa7o073i4agwWKrtyqyJQcerfu_0khU_20OOM5mD6a4v172dOH-kiWAmJk--4aSXbtamLtZIkt2XHDny5cJlEr51BwmYZkNOwNwt35LFoz1BUol0UOhHNGSTZmTpnuC21ThDORO2BaoftFRS7SJpbrPDJ6gbnPeGyW_3vRL7eHIBDCdaMghJkFpyzi8llqVtC_Tb6yJdWIhmNF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مقاومت فوق‌العاده یه برج ۳۶ طبقه فیلیپینی در مواجهه با زلزله دیروز ۸ ریشتری در این کشور
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65518" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65517">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش باحال حمید معصومی‌نژاد تو ایتالیا از آخرین روز مدرسه تو این کشور که دانش‌آموزا اینجوری همو با آرد و‌ تخم مرغ و ... به کثافت کشیدن و جشن گرفتن
😂
اینجا هم بچه‌های بیچاره هرروز بخاطر تاثیر معدل کنکور تجمع میکنن که به هیچ‌جای هیچ مسئولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65517" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTwiLoIr7DO4cuszYNQUaNj4jMB3Polp0FcwBopFg0q_AWZPphyUKYGSmvqypcwdrZi1-rBg1lXg4_m8xsqNuS6wBKgUMBlO-6XhfbD6IZssXl8HwnbIUDd_St1IFTLU2PjDi42AO2shrhWWtBntPm5MbdHgLDtp2Tn7Gt4ueDjOGuOq5hH4XLW5JAr12bRd23vf07pzmGzfFsPcHn2U7cpgz6WEjGMZw7B8hSZiICy8wuCynu_gSyalHQGnZJUMHBZzTpep_BTyg4lJdef2Dnv-aAP0ivR9UN-99oZhdhgXDqFiZx7S_ezn3Qes3LjSa5AoyfWX56peDx8w4QPPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
سفارت جمهوری اسلامی در بیروت بجای مردم ایران اومده گفته که لبنان قلب ایرانه و خب گوه خورده
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65516" target="_blank">📅 11:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🇮🇷
ستاد دفن و خاکسپاری علی‌خامنه‌ای اعلام کرد که مراسم خاکسپاری رهبر دوم ترور شده حکومت حداقل تا بعد از دهه اول محرم برگزار نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65515" target="_blank">📅 11:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
جی دی ونس معاون ترامپ:
مواردی وجود داره که منافع اسرائیل و ایالات متحده متفاوته.
هدف اصلی ایالات متحده در مورد ایران اینه که اطمینان حاصل کنه تهران سلاح هسته‌ای نداره.
ما می‌تونیم به توافق هسته‌ای بلندمدتی با ایران دست یابیم. ممکنه اسرائیل این موضوع را نپسنده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65514" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد ایران:
اگر حالا ما برویم و بمباران کنیم «که اگر بخواهیم می‌توانیم خیلی راحت این کار را انجام دهیم» و دو سه هفته دیگر آنهارا بمباران کنیم، آنها دیگر هیچ چیزی نخواهند داشت.
اما شما تنگه را برای ماه‌ها «باز» نخواهید دید. اگر ما بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نمی‌خواهم.
ما یک سند امضا شده خواهیم داشت که در واقع از انجام بمباران قوی‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65513" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا از نتانیاهو خواستید که حمله را تلافی نکند؟
ترامپ: نه، من گفتم کاری را که درست است انجام بده، اما می‌خواهم هر چه سریع‌تر متوقف بشی چون آنها باید متوقف شوند.
این مربوط به لبنان بود و باید متوقف شود. ما می‌خواهیم کار تمام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65512" target="_blank">📅 10:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65511" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
ما اکنون در حال مذاکره هستیم و آنها می خواهند معامله بسیار خوبی انجام دهند. آنها حاضرند همه چیز را به ما بدهند. آنها حاضرند به ما "هیچ سلاح هسته ای" بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65510" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
🇺🇸
🚨
🚨
ترامپ اعلام کرد در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهد کرد!
ترامپ: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65509" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
🚨
🚨
ترامپ درباره ایران: ما هر چیزی را که برای تخریب وجود داشت، نابود کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65508" target="_blank">📅 09:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65507">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=V2dz-pwYT9q2ABqzyU_k513A7fqrsbEsukPhC1eGZ3cS3uVq8Q-NcN4lOaU8ro_JCFELVzGi1Sy8Gl2BPDLwqoEwU1C6YqnXamv1IFkJHCiOxlQwe-mtq4thcml_QD98fvouctcePtbE5Tv4TSr143HAH5DVfeUUc1LfwTB01rvKW8wVgwl9kK2DIdkby0bRL3EzaAxG3kxrBq-TNqhHK6aVpiGqtTs-xYShCnrz8tlqWObibvyw-k55iLOhu8sSVboRos6Jdc7VU7Srr6o4Cxs2OeynTxpjICW-9NH7DXeIlWhqfNKhnQa9bRomBCuh_6e69tNQ2GU2WsqmA0_UGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65507" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65506">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
🚨
🚨
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65506" target="_blank">📅 09:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65505">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
طبق گزارش
نیویورک تایمز
، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65505" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65504">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=KrTiH6DVUPl795U5WMOu52Gom1k6fqC3a3QzA9d5uD-DTEl9SvXg4alIiU4zuyxsi8U6ttXonP2xkyp4kXqstoB8YtPKYuJa81V1j6unbLnBbf9y9OJ7XI86b0B_VY0oCWdjuHiLjVMOgDpBSoiyG8lRAcXuRWgMkT3NHUAiQgFUyqyzvZX1be_34bKpM2ZEXODkoMBAH_nTEgV6buc2jAvh8j_Z3_P1asHxtaXh_4acE3JXbAIV462FVs7KFHjPfq6GApjhIPZyxC9UjVQKUF3GOstpRyXsH1rl6mWz4kPW8EGDUOJFGwviQ9qB-8OjjY1O8PpncOCHzUfOgpDxpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=KrTiH6DVUPl795U5WMOu52Gom1k6fqC3a3QzA9d5uD-DTEl9SvXg4alIiU4zuyxsi8U6ttXonP2xkyp4kXqstoB8YtPKYuJa81V1j6unbLnBbf9y9OJ7XI86b0B_VY0oCWdjuHiLjVMOgDpBSoiyG8lRAcXuRWgMkT3NHUAiQgFUyqyzvZX1be_34bKpM2ZEXODkoMBAH_nTEgV6buc2jAvh8j_Z3_P1asHxtaXh_4acE3JXbAIV462FVs7KFHjPfq6GApjhIPZyxC9UjVQKUF3GOstpRyXsH1rl6mWz4kPW8EGDUOJFGwviQ9qB-8OjjY1O8PpncOCHzUfOgpDxpIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یک کارشناس حکومتی در صداوسیمای جمهوری اسلامی: آمریکا در جنگ ۴۰ روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته! کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها برای جمهوری اسلامی کار سختی نیست و ما به درخواست کشورهای منطقه خویشتنداری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65504" target="_blank">📅 09:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tetvyrmEU38qzKDJJcVo8g2tH_xg5TNm0dZm1DX3Oh4mlp9Mb7rkALCyGcc1BxAswh21Hp82xEoHpWOWmzO438k95quC0nnEUNYUsXaObkZvzCxzhFyfsdHRKX7CZrspxlvAuYQVV3YRgCqGWwzSqXKYeL4wdUHSlMCU6nY5S6j9JgeUJxmCIwnVdLyGh01-UOMDXaDaSo17j_ZFXdfnZxDTkE0ce2veUwzKJlsGKbpreDJhp_URi31PyhXJENYxhPbt6GndsC-2kdQ3_faswiWDSflchuVo-GZCntPx7ZORru20-Wv7zZ-InUjhgtK0IinW81f98PJBYNKWpD2TYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRoDQiu1hnVn8tnidwnEDBdwSjxFMoXHwW8NB02Zm0PqLBb3UIW0SFtrBs4rpLkLy4_ZXM6JPXBhyUgGYTIKAXzg-rFnhSzSsf64970IQ4OtDpoSSLODIUb7y93a_hQDJhc3v67t0gr7cQ_PMlPv_HDLgFSSK2TNSs0_n2SXFs6Li2pY4vLX2k_yQZAGvNTj5UabOyaxwI5E-fjrnDTotFF1O8UJfMOrI7nn2eAYWlVMZ_1Zrc2jyjBWKQTcD7hsjczfNXjCOYlX0UwnAmw7Zeu6FbdYPm3-f00LYTwie3A9XqRyvOaWGL6Es1oPUprINQpBJFNZf-y_2sfQDTfcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اونایی که
۵ ماه
پیش وارد شدن الان
۲.۵ برابر پولشون سود
دریافت کردن
دو فرصت
ویژه
در
سرآوا
برای شما فراهم شده که با بازدهی فوق‌العاده می‌تونه مسیر جدیدی به سوی
ثروت
براتون باز کنه
✅
اگه توام‌ دنبال یه‌راه میگردی تا بتونی درامد خودتو داشته باشی به خانواده سرآوا ملحق شو:
@Sarava_Finance</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7093313be4.mp4?token=S0WDg_CLizkrS_Vhm6FmqX1rmv7qJrEPvBBnTJVRWBkXS4ONr3fuIjbmnGe4OqFSv6DTlpxEKPxEoNJ7JQ8wx6Fa2dsFWGHTgHChua-dEL8yhodxCrtzcOhUHnxkgicNwDZGYwclA_xmANHpeBg4D5lYfSSZKDVuj3w6NRtzK25QpW_Ny6ykik4e5WdnBCFYLO7SmvfVYf9nJREy-Q9T1XGK9YUDOt7PGWKG2zjRkitgq50WDXLZTG2wMTm-tovGR0xVRsJNbiytGI1_ATUS7t5xTIfjjCLe_Cat3V_HwDeFcLOrTwGxb98LVozi8KIpw7qducr6o2kBeKlJEwrMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7093313be4.mp4?token=S0WDg_CLizkrS_Vhm6FmqX1rmv7qJrEPvBBnTJVRWBkXS4ONr3fuIjbmnGe4OqFSv6DTlpxEKPxEoNJ7JQ8wx6Fa2dsFWGHTgHChua-dEL8yhodxCrtzcOhUHnxkgicNwDZGYwclA_xmANHpeBg4D5lYfSSZKDVuj3w6NRtzK25QpW_Ny6ykik4e5WdnBCFYLO7SmvfVYf9nJREy-Q9T1XGK9YUDOt7PGWKG2zjRkitgq50WDXLZTG2wMTm-tovGR0xVRsJNbiytGI1_ATUS7t5xTIfjjCLe_Cat3V_HwDeFcLOrTwGxb98LVozi8KIpw7qducr6o2kBeKlJEwrMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سپاه پاسداران حملات موشکی و پهپادی به پایگاه‌های آمریکایی و گروه‌ های کرد در نزدیکی سوران، استان اربیل، کردستان عراق انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=UXWT89fxw3oUYTXYG7wnVfu8GAvQ-lU7pUDd1CpGvkzO6EjWBxQnIO93G1syyBD8LXpN0owCXRH1FAe9fXtLWJLp3cS9la3UAv4zVGs-r8jK_PUOjUuNKJVqTslIjCt3BwkF-pCEYZJO6TMvskRE-seybFPcPyBtMOPsjmbNwIPtKkSHEM8XdMqZ1yaHUVbyEpx-lrZ0cKbgpR2BOz7Mcg7yneT7kccnjuMP10o-DUimTz7dTjtN02IXSf-zOGbNegzrc2JSdnXIdVZTHKxWAdOiVkS2dIUs1ImaI-yOHrumfkfT5CzBmxRa87OE7KxiNjM-ev95WfebDciiElFsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=UXWT89fxw3oUYTXYG7wnVfu8GAvQ-lU7pUDd1CpGvkzO6EjWBxQnIO93G1syyBD8LXpN0owCXRH1FAe9fXtLWJLp3cS9la3UAv4zVGs-r8jK_PUOjUuNKJVqTslIjCt3BwkF-pCEYZJO6TMvskRE-seybFPcPyBtMOPsjmbNwIPtKkSHEM8XdMqZ1yaHUVbyEpx-lrZ0cKbgpR2BOz7Mcg7yneT7kccnjuMP10o-DUimTz7dTjtN02IXSf-zOGbNegzrc2JSdnXIdVZTHKxWAdOiVkS2dIUs1ImaI-yOHrumfkfT5CzBmxRa87OE7KxiNjM-ev95WfebDciiElFsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رژیم جمهوری اسلامی با موشک به کردستان عراق حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbLDhzY8jzSFiPJ4o4nBK3nFPRWP2PP_ZbhedjvZR1qi82Vw8NJFHZHqzTCKfAA0f4X1qMOv8TFBjORVwinUiy9Bd35k-HhFLzbeAOoaTYiQ0puZepYFHH4wYMM7DzhrIraaIzcIsQ715TA-9OjQxqSMtPjJ_0qBhZBxwPoiBPoQu7FcMqbqJCGngcxALPsJ4_rV1qROOqsiefnPOrjYiarfJ7RkwHh1egAerUY0KFz3nrk_hjGDB0r7S5vdgI_EO-JuV8pZqQYGnV5WCsWJrO_fh5hU72wBPEbpDxIWndBSGDM_7_twYu9CfRXncaSkVCMNMnJmd5CPg7xZJCGl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha3Ngd4SjBWkW-xc7Fhg5et5yIqso8Eb4v2BpsjuTRN2IPB0f1nRBxvvwvu6gaDn0dgjJvzDezgO5VGtjciWG6XrDJmgKKK9vhPvhQ3vtDzSCkJPDI0jcO5sxuOxNmBb7PG-xCqcZBbBVgoH7nM78Wl8BK9bEU4hXVBJ2Zqz5RzYFBasPFuzw9T_nygw5UhDpataXYCMHmcXKBBbjOeWJHUdgqNmYGxC9DL9GjqwUdR8MAWHvR6epnhDgqH6OuAGayYFcEXiRLgnwUBWTliU70SoVMnSMfZCxFqVY6UxheH-APOiF9BAIqcKFmqtfmwOPgh6kMiG_DKTmFI6VawbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=uM9wGSE6P6lJbWEnVSz2wn1_JlQo_25lgJt93O-Pr1M7qcshEpOBolgqOFGXzC5cY0fOWh1fy6TdOkYV194MNDzXSuRCuOUVhoeKGyMpzvgK6SEH36Fnyvk5NydbHEAAQJLAeQQDrrWzmwXayjRio7kaxV-8TTLDcy1FG-CxgSApXYYu2jUzK9JImQCVgruinXEtBduZ_515LMTqN_nT1S4n5kmmT5ZvyuFPnFLyMso50eXlWo7_IK3KgQAuoW_Em00rGPpEzNOTJ5dRIzCshh0HZ_Bz_YWZnG7HCVOl6EtXYBLzLIBqE71yifnOuBT2nWhSyzAXxiYACF3-50KNwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=uM9wGSE6P6lJbWEnVSz2wn1_JlQo_25lgJt93O-Pr1M7qcshEpOBolgqOFGXzC5cY0fOWh1fy6TdOkYV194MNDzXSuRCuOUVhoeKGyMpzvgK6SEH36Fnyvk5NydbHEAAQJLAeQQDrrWzmwXayjRio7kaxV-8TTLDcy1FG-CxgSApXYYu2jUzK9JImQCVgruinXEtBduZ_515LMTqN_nT1S4n5kmmT5ZvyuFPnFLyMso50eXlWo7_IK3KgQAuoW_Em00rGPpEzNOTJ5dRIzCshh0HZ_Bz_YWZnG7HCVOl6EtXYBLzLIBqE71yifnOuBT2nWhSyzAXxiYACF3-50KNwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4Bi4piJVXz-rJcJncxQ6ejSZdXRtYtQEOAq_5Hl03w1U8dHlrg6vF8E85YSxjE5lCtF-0iUZ8Z6CEbWU4Kmc5k5YMcvzndEAbN7yPkKdjok7Giv1XxB2CNndY3nU0vSikRoRPKpaFUWUDeEXSyxozE-SjrNezijDJfHYMInC9uqLY6Zl_HszRMga8m8kyKZFcm3lmCxduc6GPip8kPz2qqp4EiR_70MZtMUilCbwhPkrYiOOGo0qU1oRk-QARQ0xFhZOLdCgyK4Yqt735nXgv88eXN6v5gGLkHS43bUg4cQ5N-KmeReioUwnqv7Bq8E_HEGdGpbd8HKGHwTTOXeRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVdCuXTng3iyyeb_31vGzTIH2VJ8zUQyQ4JEreVa6qNvenD8I4JPmRnLtxtGshfakqPz0n-B9r9Y_JynRXfQtbj9YQ3SxZuVsTU9OD4oIOkpd9-qeN1-FFYpb7GkGztb43DPIDoh-G8K-YlascAvWt2QOI0ufXOAksfn_CcY6uo8YR-Aamy942OtEZEvLeiNaH71upHmQBykpAXECvl0_2EQ7-OaMhqzFJX0NgTIIvFjDKrm7TcZNouBdYEaDFPQW6o5oCjHnhljRJx5Mq-v2J30SZhVxEFkoVnCt06x2vGSEhhQbSy-TMlE4N-MzbaykwqiUGhCIamPjoozAdlUPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65473">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOK92xVTNmU_Oap5S7ICqmbkC5QgJway7f9_DCLxUcyrNpYusiixvYJQVO9YaN3OmYYo6weHvk92TvWUJu9IeV4a3JDVqd8fDFXxLHX-seBl-0dY8pq0i8WLYKTZdzQEns8-Qm0yLyVPdEVv68zM_gfuFxjjtB51z2Q9l8y5hwzg9R1wBxvp7Su6c1fpj1cAunCJJO5BArNxDFcMyZ__52jJ6pzlIGsQblPkr9PVWnRCnQ1tXcu6b8n_4zkwqaip4pNrI_Pgu0PAL942DOZniXZPycJvw9x5M4IFXflqPQ89PpWcfh2EEBhlQFxrUHAtRIJMKyQwQB2yEKJZNOGlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروی دفاعی اسرائیل (IDF) دستور تخلیه محله زقاق المفدی در صور در جنوب لبنان را صادر کرده و به ساکنان هشدار داده است که فوراً خانه‌های خود را ترک کرده و به شمال رودخانه زهرانی نقل مکان کنند، به دلیل حملات قریب‌الوقوع علیه حزب‌الله.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65473" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65472">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65472" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65471">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
نتانیاهو در واکنش به اظهارات ترامپ: اسرائیل حق دفاع از خود را دارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65471" target="_blank">📅 19:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65470">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نتانیاهو:اسرائیل فعلا از حمله به ایران خودداری می‌کند ولی ماموریت ما با حزب الله هنوز تموم نشده
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65470" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65469">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=kDx1m5bWyrnFQ1Yh59wZ4c70hOtIuu3rOZYd_SRPFKZkA4PZtK3_Zws56Xx0tSy1Uq0O7Ys39l955DweZ6yLGe_Ao6NiTces7CeG93eBl9j_4nVYZFEhf423jMRzIVxV5V3rXZXXWKiFFtWb6VFMSfs-4cKkVSw0ujbWNya1Akv0fbkZXdF1Y5dVMjI65oR4q_0OEfIXAUXb8zVSVci5QcVD_jvbNs4zvoeqqVV9cQvYUIGkcwAx0Mqk23P_TpLxCGuoObSWzOByhM8PweMy0CZLeqLIwx-VRzigiUawj1vH9l8fLsZI0Wi-fuqL3xqSo2cbU8qpGbC7sgydyR74Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc930bac93.mp4?token=kDx1m5bWyrnFQ1Yh59wZ4c70hOtIuu3rOZYd_SRPFKZkA4PZtK3_Zws56Xx0tSy1Uq0O7Ys39l955DweZ6yLGe_Ao6NiTces7CeG93eBl9j_4nVYZFEhf423jMRzIVxV5V3rXZXXWKiFFtWb6VFMSfs-4cKkVSw0ujbWNya1Akv0fbkZXdF1Y5dVMjI65oR4q_0OEfIXAUXb8zVSVci5QcVD_jvbNs4zvoeqqVV9cQvYUIGkcwAx0Mqk23P_TpLxCGuoObSWzOByhM8PweMy0CZLeqLIwx-VRzigiUawj1vH9l8fLsZI0Wi-fuqL3xqSo2cbU8qpGbC7sgydyR74Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65469" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65468">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران معادلات را بر ما تحمیل نمی‌کند؛ پس از شلیک حزب‌الله به اسرائیل، به بیروت حمله کردیم؛ پس از حمله ایران به اسرائیل، به مناطق مختلف ایران حمله کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65468" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65467">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
نتانیاهو:نظام ایران پس از پاسخ ما عقب‌نشینی کرد و اگر اشتباهش را تکرار کند با شدت پاسخ خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65467" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65466">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو: تسویه حساب اسرائیل با حزب‌الله با قدرت ادامه پیدا خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65466" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65465">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=EQmrIy0sSG99oUzfjaqywris_DAgD1KAIrv7s-Pbkrp9gu_2gSY294l2TjhKeXzPMdS1YlgrtvjmMOzbjcgsNZfDb0bGJAum6XV2ujgRHdVqXWpm7Ql9wI0GjjHwUbAxHF2B5_gx5ElA1ETgvW__ITzlBUlnLxpRCE-sHuMkFp9jIOZEbXVMdvMFcHa11MLSwUQCeHZ_6Yf3YqDD9jejEjNqKodevIMHGGmRMUO_7xpsQ6FHHE-IJ0zLaMc1m9d597j8yRm2OpkphWXY9OqPm6dONhjNcGvKwUICF6CFZgpCay7eKixZyfOdAfa9u_Ory52gO3BebTBk4IatsoxOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d663dc6e.mp4?token=EQmrIy0sSG99oUzfjaqywris_DAgD1KAIrv7s-Pbkrp9gu_2gSY294l2TjhKeXzPMdS1YlgrtvjmMOzbjcgsNZfDb0bGJAum6XV2ujgRHdVqXWpm7Ql9wI0GjjHwUbAxHF2B5_gx5ElA1ETgvW__ITzlBUlnLxpRCE-sHuMkFp9jIOZEbXVMdvMFcHa11MLSwUQCeHZ_6Yf3YqDD9jejEjNqKodevIMHGGmRMUO_7xpsQ6FHHE-IJ0zLaMc1m9d597j8yRm2OpkphWXY9OqPm6dONhjNcGvKwUICF6CFZgpCay7eKixZyfOdAfa9u_Ory52gO3BebTBk4IatsoxOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
سوخت رسان های آمریکا در فرودگاه بن گوریون اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65465" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65464">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
بنیامین نتانیاهو تا دقایقی دیگر سخنرانی بسیار مهمی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65464" target="_blank">📅 18:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65463">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
وزیر دفاع اسرائیل، ایسرائیل کاتز:
وضعیت در ضاحیه بیروت همانند شهرک‌های شمالی است. هر حمله‌ای به شهرک‌های شمالی منجر به حمله‌ای در ضاحیه خواهد شد. ارتش اسرائیل به عملیات خود در لبنان علیه سازمان تروریستی حزب‌الله ادامه خواهد داد. ما تهدیدات ایران را به‌طور کامل رد می‌کنیم. هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همان‌طور که دیروز اتفاق افتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65463" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65462">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3210944dde.mp4?token=hvi7YDCvQWwzO2-kVwWy5hTdOT8BABh3S_5JAI0Fn1NalDvrNhrzobf_XceRBXg2KcNQ9brGXcF1iVUV5uC0wGWg-i5DBGwtCc29yWzTG9DAR9-8aIOvktK_x7Nn-hEH145EMy3bFwXoXGb35PPRzujVDliH_r7HFyEO8d68JMXGCR2TXfJC8eZWArGw8HFmxNiSW5BhZRQ7R-XITcaGvymQh7Z3CcoXr8JRWN5er0sODOEG3tEdD_VoYIasnKWj6sypiWkzaUBAwUqf8CuhfA3hfVOIn8vay73lxStsl_p5yaZcRvFUGTI12U1VQeIoeaCDxtGI-e3lRYnT2OjREQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3210944dde.mp4?token=hvi7YDCvQWwzO2-kVwWy5hTdOT8BABh3S_5JAI0Fn1NalDvrNhrzobf_XceRBXg2KcNQ9brGXcF1iVUV5uC0wGWg-i5DBGwtCc29yWzTG9DAR9-8aIOvktK_x7Nn-hEH145EMy3bFwXoXGb35PPRzujVDliH_r7HFyEO8d68JMXGCR2TXfJC8eZWArGw8HFmxNiSW5BhZRQ7R-XITcaGvymQh7Z3CcoXr8JRWN5er0sODOEG3tEdD_VoYIasnKWj6sypiWkzaUBAwUqf8CuhfA3hfVOIn8vay73lxStsl_p5yaZcRvFUGTI12U1VQeIoeaCDxtGI-e3lRYnT2OjREQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای از اصابت پهباد به مواضع گروه های کرد در شمال عراق
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65462" target="_blank">📅 17:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65461">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
اسرائیل هیوم از منابع: هنوز هیچ محدودیتی برای فعالیت ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65461" target="_blank">📅 17:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65460">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=tYr-NOv0hcF0gHB_BuiyZaFdkuzz4ed2MoDLPXZ0ObYCXR0RYP0gXyWdcDNdwk9DCgu7jbyFZcSeAiDqsyPGbBPPKFn5ADiwc1GhWSOE-MCcAgrGGuxTGFs4Hcam-mIgslZ1I5wZ93NGTHLbusaVR_22fSLlQ6yMMZXc5MDyKAXwD3wKDBJ-OMh8SUuklhd_wpSvbv4wRnlLnbpQsMkNKd6vhU5oFDHIT-uXa7cF2AzCr3ZTf0w89HHvlLH7a1VKUnVlGxtMlDaequGcHttlqIaQrScBhahQHZakPCxgfamYEpk2IaMxHIKMPrRnkIYx7Ty8ackgShiPTCbJOT_Hhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc72e760f.mp4?token=tYr-NOv0hcF0gHB_BuiyZaFdkuzz4ed2MoDLPXZ0ObYCXR0RYP0gXyWdcDNdwk9DCgu7jbyFZcSeAiDqsyPGbBPPKFn5ADiwc1GhWSOE-MCcAgrGGuxTGFs4Hcam-mIgslZ1I5wZ93NGTHLbusaVR_22fSLlQ6yMMZXc5MDyKAXwD3wKDBJ-OMh8SUuklhd_wpSvbv4wRnlLnbpQsMkNKd6vhU5oFDHIT-uXa7cF2AzCr3ZTf0w89HHvlLH7a1VKUnVlGxtMlDaequGcHttlqIaQrScBhahQHZakPCxgfamYEpk2IaMxHIKMPrRnkIYx7Ty8ackgShiPTCbJOT_Hhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیویی کوتاه از حملات امروز اسرائیل به اهدافی مشخص شده در ایران
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65460" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65459">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs2F7IOdcfxzl9qWJWZv4GuKKTkOus_IHlVdRNDR-v4FwmVjd-uXDaiGurmBvQcpId6h9GUtJ0FTnZLEN6PXF2tOCKMSTqUi-UvhiA54A0jkPCaB75zFpVb1Yy7oeyBNJpWJ7PiJR2iNodS5_8VsWq2A8NjMzBRmO0TevnWLDT_j98Ztdw5HW6GZdsGr0QPU8ZUc7mjVEMIO6g1MPi_xVX2aSulJsqgN4EUOsqqEOgp54Wi8d2s_bmmfuanZnkWCzmUsFEy4CfF2OZRwbhbt-T00p2xfUXMJGOaGunESVOykH4yfrNo-XSfVYcH5oIeUECqKswxY6BtTBuUICNBwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری دیگر از جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65459" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65458">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4N4p0WxMQ65zU6eGuVNiL1ZtxDIMDKU0RCqsEfXykiztlQa-wfFqWh4WRwxFXuatnItmAkT_OAUbb_FFmSGuCD9rzqYhBjUedbvzXyBZeX0pn8DhiUeJQsIzQZ6L9wi3pds9mSbKODNIm9n68_lTwd1sI4X3EqmJNWi3QuOqFT5a98FlFtqWaMvFiOLhasyTRzhs1ySaf1z-1sDw2vVeKZj0GCcSI-WzRNlzKXgCG948nw_1FZKqhQrt14qYMd7qgX__4YqDspCql-lTAnp6mSKPwK3lwCXZ1hDmT_dLXGg9aBd7uDfzxifrl4SsYypHXv3OTvEu02mC3kJPWoCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها حاکی از حملات مجدد اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65458" target="_blank">📅 15:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65457">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAx2yqSgZnK1el0MTjkIU54IsB2zkyQfbW55sZiFp_km0J0DxF-hOalZmsjpfHkDIKSz4TLKfmOjxsYPRLBnN3u8Pvzcm9_6K6U2OtaB_8jCZ2rzEx2OO4_VnmTeUOogOgasxaPgJstYMx217FpGgb5EGS5xaR-Sv9lcNwMlN6bIHPsm0FZKFQzTTa1GFowLmOT4EzXkGYOFWxcagG3LFDA1v57GCHwGoakDMFwwzEKzlfXVpUVfKKFdwLG_PbLLAj_dmniU5_WzV-OkPgntUHnAFuio6fYMJwOgBcILO7ltLE__YuxQsAjYk-TWk3joJMEVsMu1ai1Rp9eQTIVOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما پایان درگیری‌های دیشب و صبح امروز رو رسما اعلام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65457" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65456">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇮🇷
فرماندهی قرارگاه خاتم الانبیا:توقف عملیات نیروهای مسلح را اعلام می کند. با تاکید بر اینکه در صورت ادامه حملات و اقدامات تجاوزکارانه از جمله در جنوب لبنان، اقدامات قوی‌تر، خشن‌تر و قاطع‌تر از گذشته در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65456" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
