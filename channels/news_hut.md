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
<img src="https://cdn4.telesco.pe/file/tqyPWGgS29dBqWB_cTpsyJeCKGnSmYnqJUY7dm68an3Yvw_gsguum4DbR6seRAcB7lMzB-eAiRQU7PgmyKfPLjo4oExLBH5KPKsFFCmhc-L1PK4-8O99kf4dxtHeTbaM7Px9FJ-RgjybB_7Et_oJsNmzGVaZqhhGn3qLpVWeFjGqfSn4rRTnDy9g_n25Hv1_xI5U_MNWrEnps7wo7QVEyBOu8-jOS6VzKhDpb2zgyKrqmHIksFyJ_1DAnqyYOSMpXPmmVe9GRW1yzbFppZS0nosustvNTnqRLNKJ7aUy0rwaLkZ2fyHWOFcwI_Ju4Lwoa-Bzc862PgU6vuVpPPmQUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 183K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 19:54:28</div>
<hr>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz47oX4HCwlfkPryYs7n9U5n7J2U5tT5z8Grm_ewaNuF5hMtmAl00JuZl2fxrciAXrnrAxMr_pKAU0psEUwj52obDXIJBFyAZAaloBY0M291PiwLDEHBlD1ym_k7WYaaGttDQwNN9Q11WJSHnGDGnpP3_fchB4LB_Ub0L08AsxZNnyj3MSamSX6FwacP4dNoxxFN58iNLpbaajet-R1cx_GZH-Tthue5ea8V4wzhTqzV_1pxUSXv_LIXrOqN1laRQ3qSxbuAAaNQJ_qXh4ryaSoT2V3xXPvf3iqQJtF6F_lwmk8NIp7QRbg-PcE6_TPCNjeRTGLYMjNdKceDUXu46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQg1odY-yEUCL-LYsgG9F8cquKXFPWK6_PuzMb0zDFsYCpz_xXeg-f6eeJImnXpWffpzKX7H3SQDVAVa3L3I07iT-H79akB-Zf017DsfAQAINwCgv85gXWCQU1bsY3apepDv0LMxY10CS5Xz2J4BEm3A46n33dV_eaEnD6VxsRUXg_LlODD4LpCwGaK6ZDSia0EoM-KtNamBQySeXaTRln6-Cs-Q1k9DkEB9bMvf-LJGt957yefaoBuFebaclFPbq8XiZRGrxDMVd9uEoewT_XdN7mc7JZiAhwiJpvVPHOqSu3FL2yhhss8-plMctu1XLIKt3MEn1UfwkAwsOzjcSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2TcBq79wEhytebcB7FQbq8WXShpBg9uRIhACJytvxYB_mFT4yNOccNBLQrF8X8A_XhiUlovw7kqkVVFs3GdnRZD2DRq_U7217v4MW7w4lhLtAJ3ZrctoISdWW9XzeGGsrRmsMlnWDv3RAkK2hhvgAGHaIHPQCJc7YhdzLzM16Lb5HShckTZV2zEkyVdsZhYGP-pFSBPglrMJmPx4DCyjjQe-cxewhD6YvKWU9jU7mTfM2vIrGxL8kY-fUS4MgWDyFHUvi0LXabeteImvWbkEt450Z057WCfZVRnYed1fXQSSbvL5VkCyAJul_e0cA5-uQcu6GJEsagrR5hxjNkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUsKyeUwJWagUq9Xmm5M7KjlV9V0ZxivECpwo3leTzQXJLIrYCFu9xhrxh1m8VylDgkPyTvBSalE6KkkjVSFdRd1KonBTrg0PM9eD7W7RjbkA0PllxWkEUJ1xAcgxw2trX1t1u9jUTLSjrBQ4WE9c0UyEsbKTJtKSkFgaySDMWqUSR7e-ipkYHokfjtTTSJF5nFek_r4U71iiMGTjgHgxuegAtyX20Vy5Hea0LvqUusm3vL9yvxllpQrvJveMoi7aJRjfME7RxSsJL7rJcfr3_-HJGRqtI_DhIieYS8U74AnQUwTxXTgncDjfQ96nqgXW9NvSUKIMt8j6Hu66v37eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=oWB1bv40y4YyBeFFKynBiXYUdG3eSHOaw2bT317P5vNJLXAgIL7CpqJguHB4LbJsIhs2ZB6oaQ85Il_IA32TtCrRdgzJUmNybaenq-Dj-RdMATqo5ZOVLRPPIAftP9ltF5jnKcUFXcXko-u2tRmHpx5g2KS8rGzNntkFm_9GczI-PS4KkJI9IdkH8b1_ktXcd-kd0tVd5l-fs7lnQXC2Cmeeiof1kdYUEyOvR-whPaV3x8g6cR6xlXBZ5SRXU3pwuhviBO0HA3ir0rsga4w-iEUwM3IXMRgiGpxzu74NhaoqvuBXyH2BsnvsZNllJpVSpC3WKATBN8W59wzJ-5zKfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=oWB1bv40y4YyBeFFKynBiXYUdG3eSHOaw2bT317P5vNJLXAgIL7CpqJguHB4LbJsIhs2ZB6oaQ85Il_IA32TtCrRdgzJUmNybaenq-Dj-RdMATqo5ZOVLRPPIAftP9ltF5jnKcUFXcXko-u2tRmHpx5g2KS8rGzNntkFm_9GczI-PS4KkJI9IdkH8b1_ktXcd-kd0tVd5l-fs7lnQXC2Cmeeiof1kdYUEyOvR-whPaV3x8g6cR6xlXBZ5SRXU3pwuhviBO0HA3ir0rsga4w-iEUwM3IXMRgiGpxzu74NhaoqvuBXyH2BsnvsZNllJpVSpC3WKATBN8W59wzJ-5zKfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=C0map3kY2GJ3mSOQ6-RwzycWd1ehb_MeIwc2IGLBE58PrhrmeYq6bATDbPomUqk4m-NNPGS6I1bxHwDGTeZOfQWfzSVMWPbsU4R2zCXWGblHubwLRilejoh71uXf-n3SGezyHDyPbYxNj-UThQCtX7dP0hzEwvjvuwy2BpvU8C1Ur1Q6qfB5uzJJImPxwtBn2O9ItQ-ZbB9KMiERTt-JAEi4wieiILyJ2BsjnwOsKzGxPYHLHry_XEabfuYU7Slqa4LifrqDVcZqBm_XPHLdBmCOUF67O3Sl63AUVugSndywkCYu4N8VB7KjHgJoOfRfQSvVuOlRBRZObX8JB6HQcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=C0map3kY2GJ3mSOQ6-RwzycWd1ehb_MeIwc2IGLBE58PrhrmeYq6bATDbPomUqk4m-NNPGS6I1bxHwDGTeZOfQWfzSVMWPbsU4R2zCXWGblHubwLRilejoh71uXf-n3SGezyHDyPbYxNj-UThQCtX7dP0hzEwvjvuwy2BpvU8C1Ur1Q6qfB5uzJJImPxwtBn2O9ItQ-ZbB9KMiERTt-JAEi4wieiILyJ2BsjnwOsKzGxPYHLHry_XEabfuYU7Slqa4LifrqDVcZqBm_XPHLdBmCOUF67O3Sl63AUVugSndywkCYu4N8VB7KjHgJoOfRfQSvVuOlRBRZObX8JB6HQcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm8FhAvXjLMMrX46WIBm_paVAuAyFbF5_nfVY90sxKGgMQDrqgaM9iIdEgqxPI3SSQpkvWLq4ClwxSr1xb7BMtwM7HCq9k6-kJRQhNWlnhc7U1_hEOT4Obzb0ETVGrpMCrorEa3dKyBHsYXsKGFFqMRLZ6nZMvE1eWkJ2WUA4Ppk8npvtBrHpg432ZQxrMKG87ptKNIz3--cjOxdiG19ZdAFwAkmxPP7WuajVTOlGOEbbpiajhOC_Ts6RW_lBUdpajVRV0pmDgsX0E_bTklrDfIQNLmpKkj0Tmg4UdzEQsQ0rdbgOoDsxPMx6oa9fLk1qMvYx87ttVFV21zjqUBpqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fITeOkj7hUw2bgCGG2XC38YbG60Kgxt3o9nVfx3J_CrSjm4jptJ1u2U47dBkVDWOTuQP0NYgtFfhGZQlDLBJUf0KwZeKsIdPY346f8UdV7iTHTFO6BmDNcWLm8Zh-ydQ1YYvCq7aV1i21Jw2adT5rYtQvhL3XcBrguxMd8XEadl2tOXPf8a22TPDPs9SlknltJKAxY0OmDdPBpvpRUA-_Njf4gSAYl9A3gAE1HWtsqOuUudsId-N1wLeaz6qrl2xZFQZPANueFqIPPjR_Sra109iUIJ4iBEBCeKNizWJp9_blii-6IpbjjAnISWBcJAtxieYwVYDYOMF7bo2iOzoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRfAmhOZHZ1zWYjmXQUYvHpEPZjnn346TkQ8bUEZbqWj0_kI6J4nSIGT7_6WEvG2eOOb10BUU_mqD9f5Ow4LR97fHUMPbbvg3KFALYXz7XXkwDoeN6yFZw9PrEHj8R4h2WKv-uZtbt7bDXdGiGUsPhcUHJbjm-KNtKW8_s39RBwDD7kfeANosQGhh_Hq0kQcLhPz4GnChF_vEplbRgaNw95mR_7nevF0AStiGIrZIZQwfKuDxldG-uUiz5RYChBoUiZ3-18w5MT1Hz7TIkTCrP5LUVsFE4YdzkJJltWZKBKv_WZl1T8iYX7JbmyNPpj2h8EBgRfl_KQQPYRNF4dotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCF6NrUi8bl98tqOo-5vO2XBmXFZrImKrYZV_zN-Tyfz3ZB8v8uqyfx0JYSyToaqO7R5CYKcLUf_gdd3DsBxj4RcLIzM-vsWU62DOn3LMvet6ajNoiJv3w4IpRge_A0kzcQM8yav4n1HI8vnw7VKpJ8sRoZNz6NN_MYdcKURpHt3nl-36KlIVmUBzZ4LLgoql6vL-wq2l1tpr6-hcvdIfuW58TKVPfRQihqkvxnuaIfLVwsfgLdBTUIYefdui_CP4oviZNoJNmRKgWHu2Kmd3rf3MODbGDH2Z25ousoF9lHIaYJguhjqftRBGEbSUDdcPRdQ4CvJMAlNvJqgGa9y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Wjk4nRonzYYQZW9y1L3bffNTDfJ-vPG-1w6V5IWMrzvyYjw4as4CaBHmYNani8iO4OlUmCr0pBFzREZI6t0n4XBa6ac-71LM4YcfgkuA44F_tvKWjCVUXSrjSn-b1PQcKFt1uyZq8kK_wvi3uuD9jSbm-EivpWTf_lZHx-pBx2yD7i5MgxYfsFMoNhOXSrYmJxpirPwuApuuUNuex6MSmnfPOivoHwL5nrlz2s7a3cZrdDad6_A6bjzWjEElqOG2gG7mH1D8B2jtDRkOh7pT8FnRzdp_mc2uu3ZspzwqDklVMvtXB3Qv9dybHhM9AbsbR8njgvDKUsy1mCuDOx_zjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Wjk4nRonzYYQZW9y1L3bffNTDfJ-vPG-1w6V5IWMrzvyYjw4as4CaBHmYNani8iO4OlUmCr0pBFzREZI6t0n4XBa6ac-71LM4YcfgkuA44F_tvKWjCVUXSrjSn-b1PQcKFt1uyZq8kK_wvi3uuD9jSbm-EivpWTf_lZHx-pBx2yD7i5MgxYfsFMoNhOXSrYmJxpirPwuApuuUNuex6MSmnfPOivoHwL5nrlz2s7a3cZrdDad6_A6bjzWjEElqOG2gG7mH1D8B2jtDRkOh7pT8FnRzdp_mc2uu3ZspzwqDklVMvtXB3Qv9dybHhM9AbsbR8njgvDKUsy1mCuDOx_zjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=nekfzPd249bmjX1KZ0gshBHiGn_jjNz7S9t5WY1K2x7HI69yrqsVLMonQs4Q3yI17e_ipF2_bZK_FQGH7TVqfnj9fGe3S7jyC6KBiDX3Nqhj9Wo-ACfxJr9KPLUzklOPoSAHFt9M6AXVAzNN992C7Ww2STiOKvdH2BTsZpervX-5MYMFByycUanyOcUKPMIbs0iVeyk0MLWDQ9MthsR75lfyEVEoKsPHoANhUkjcWGB-_PsDO-PwLz6BrVbyY9sT2vEmRpPgCtjpNuJC6DsCWVRJfS_eoGGOL0CN9dIiLKZn1_lVpGbILe_lJzESOHgVGwmmY7HQ0Wrx4_t2a4HlfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=nekfzPd249bmjX1KZ0gshBHiGn_jjNz7S9t5WY1K2x7HI69yrqsVLMonQs4Q3yI17e_ipF2_bZK_FQGH7TVqfnj9fGe3S7jyC6KBiDX3Nqhj9Wo-ACfxJr9KPLUzklOPoSAHFt9M6AXVAzNN992C7Ww2STiOKvdH2BTsZpervX-5MYMFByycUanyOcUKPMIbs0iVeyk0MLWDQ9MthsR75lfyEVEoKsPHoANhUkjcWGB-_PsDO-PwLz6BrVbyY9sT2vEmRpPgCtjpNuJC6DsCWVRJfS_eoGGOL0CN9dIiLKZn1_lVpGbILe_lJzESOHgVGwmmY7HQ0Wrx4_t2a4HlfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uimh0iFZ_VOAET3ya2HKZiOCvfpZkbMPBcBy7A6RmvUzVqTAQZnP6a5IGxojf2lxtGUPJROUwiICfLO6gxd4kcW0xycx9uA-syqebxt3wrfo1X9ugfQS6P54L2zBYfyNQ6SAVQN94dB2EaCARsKvkP_Cv7oO9N9aPGeiCUmOpEwmOSjFy0g_JmNipfgECtpsTSy8AyDAgT0mzkm0xekQK-sB8nlNXfvUBK1H8G3CACSC2wJNoyLlt1iO3o5Qc3IgF58sdc04zqxkjyZq6bCF3Jg9Uz-tFNuORFa5ApzQtBjggKo88VxAG31Nc1bkYy5yGt2hVLFTUaxU0ImgQuJj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H19a7jz5bSy2mEt9HAfgHXqQh49TbZiHqVj2b7WSaDrY_kUBOV2zXEsL4zBUCG9zt6EaArd0mcAldzmO9xZI3HvhF18lmMlZOIqxWrJmiF853K22uBRckPliwmhptJWiURVroEyLsmWEkL78GGRiAl7-L1oBed-4OeiLewTNm6_B31AG9S3YEeNk85AJqcybKUU09c3os92_9em_7BRXpn0UHtc3zr71PaEfPXH5aoX2KcpVIWgzyv8-qNgSzJtI-Gt3LXi5tB2PYruJm1jF3s7vbdZkvHN4LR1Cw-CfHG21pmWEjen6udLKHk17T3M3qMJG9BPYizyjrpTBZCGtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=V3ubRpG9c3ZRgh3a6ohhgG7A-RMhyHYIIgpDf8fMXTxiHOA1QinWRlhVFBmGTYJzUTeFn7OdKWBHHBykWu4BOLeJ4GFy4kKoPcGZKdWppUexQ_-rROFaYeQzoLmr6Z10l_gmVgDOploNGUvop05WPniqM-uP0Svp3eTI1R-oPHfc9EFPV3RpiTBncAPMqIvjtLmYV1TRbtKXIz3IDo_LKUnA9h-jC-BMe_CHHjId0qXhZ9k3qDjbmUh8RL73BQ0B6ZLIRvzk99DxcL_3lFbkBkzvBQY5rVwrWF8Zyhcy274TdzIWX044PWpPCxFKcGEPJoUPAA2YTHymuzWqPKyRD5cJY3-P-DxyXqJw4XFS4zEni6NWtxkSNFGtFtzOCABqGP0RNJL8fzl8LQyWn4z3-Uyk9exll2ocqaYm5_uXCLEuT0B44cqKLPN_6yw2S2iPsh1AWW9FuxTVfDdCD1JgNVsAdPr13oQOW3nOvmkld_SClbfYE6Yup902o3rQsPkKgytxJ3cax52cGJom4c8ct7QsycuxRd6WuPVBflRP_cWxrCFiF0tbEF21rGY9doMXzshsGtlOLXbeUQm3crev3emvBx_FlCo8oQsH7-Rvepa7KO3V2BQKihU5pGsnGx6E7JxSAP8zjxPvpp_H_X6qXGucAU9bTDcdHP-T4SAIAnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=V3ubRpG9c3ZRgh3a6ohhgG7A-RMhyHYIIgpDf8fMXTxiHOA1QinWRlhVFBmGTYJzUTeFn7OdKWBHHBykWu4BOLeJ4GFy4kKoPcGZKdWppUexQ_-rROFaYeQzoLmr6Z10l_gmVgDOploNGUvop05WPniqM-uP0Svp3eTI1R-oPHfc9EFPV3RpiTBncAPMqIvjtLmYV1TRbtKXIz3IDo_LKUnA9h-jC-BMe_CHHjId0qXhZ9k3qDjbmUh8RL73BQ0B6ZLIRvzk99DxcL_3lFbkBkzvBQY5rVwrWF8Zyhcy274TdzIWX044PWpPCxFKcGEPJoUPAA2YTHymuzWqPKyRD5cJY3-P-DxyXqJw4XFS4zEni6NWtxkSNFGtFtzOCABqGP0RNJL8fzl8LQyWn4z3-Uyk9exll2ocqaYm5_uXCLEuT0B44cqKLPN_6yw2S2iPsh1AWW9FuxTVfDdCD1JgNVsAdPr13oQOW3nOvmkld_SClbfYE6Yup902o3rQsPkKgytxJ3cax52cGJom4c8ct7QsycuxRd6WuPVBflRP_cWxrCFiF0tbEF21rGY9doMXzshsGtlOLXbeUQm3crev3emvBx_FlCo8oQsH7-Rvepa7KO3V2BQKihU5pGsnGx6E7JxSAP8zjxPvpp_H_X6qXGucAU9bTDcdHP-T4SAIAnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=Ym2CFI4tJPHS3KUCrS7ZetP8StPGG_dyjlgeo5SWjmIav5wLs_Th7wOYx_aSl33sUOXbZ7kiRylVs0U4U-7dsWeCA-T1Rvdg-klyjF1aVzWOaZXTpnJYWjvKLYeLLHLwx9Y5_B9owZ2A8oI_gwwRvP4BbbG5SaYmmZmnzWSisIc-gZM49bczwLq8Tsy0Jn2PCJ6yicJtMwjh5MvsEYxUqO2_tbSlyFbu0HqiVoZFRpsJFRF7O_HC72lhJbq4X1o59Y-D7n5WOKyfRUFHnRQ3sitn4rmUBaDKz3B0jdEK1ToOXl5A0xCANUoNQY_urpvnUxGkAbU7AYj95cRpb0D-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=Ym2CFI4tJPHS3KUCrS7ZetP8StPGG_dyjlgeo5SWjmIav5wLs_Th7wOYx_aSl33sUOXbZ7kiRylVs0U4U-7dsWeCA-T1Rvdg-klyjF1aVzWOaZXTpnJYWjvKLYeLLHLwx9Y5_B9owZ2A8oI_gwwRvP4BbbG5SaYmmZmnzWSisIc-gZM49bczwLq8Tsy0Jn2PCJ6yicJtMwjh5MvsEYxUqO2_tbSlyFbu0HqiVoZFRpsJFRF7O_HC72lhJbq4X1o59Y-D7n5WOKyfRUFHnRQ3sitn4rmUBaDKz3B0jdEK1ToOXl5A0xCANUoNQY_urpvnUxGkAbU7AYj95cRpb0D-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=qBgiA0_BAuI17Q55ov6HIjaW55mbrjr2AldbxJsy3AKhsbJApFLco7bgDQU-vOxS4kMh6946B-BWYzWyyoj9gf8RisFxFILXMjHvPsGRKimaPAUDzIvxzZvN3uHjmzVcWTIsYZfBk6bEZ2kx6UHoXraIuRQIWvKXu54KusmaAzE8ZTKPoZy-N2BGG7aNAaHSwe6F1wYoTVqVKQps4RRsnCPmMOjBN_81r3Fj4F8LdG9_9M0uLJmuWhC1kcOgbDWWh7fMv67ltXxE5GVvnWxXzItbAu2Cqyaoum1YMZcweENm7da9JueoGIFEM7ywVIrX3GKXVNrpWNHEh7z6SwFyXxj4GVQGRoQKy5PxDqVoVzZuQ0WNBTCdf43iwd5nqhG54mdxptFAQhcSNcs0x3bSaDj3wy0xUCjH6NDT1JL9TRViTVkDzlxAG1xSzNbYMISpTRm3CCGAbevONxum9RyzWXbWFFDxeXo8LJLm43rHibUHmctDHLsKvv72OWmkYHIAnVIyjrbYv4t8mcKhMF2H5rcoZGrXWF0tKtyYGHbtxSqXmPwLAkXGuM435wBIY47-F--sF_0ywC6eyUCw_1ZLjvjBJWdP9Eq_ytW6Ln8dqjhG1GUM7fyLDGsv-TYbinpLjW7-3AirgbkkZC9b2Vwqnx6MiFMAgA1TIaY5L3P0mpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=qBgiA0_BAuI17Q55ov6HIjaW55mbrjr2AldbxJsy3AKhsbJApFLco7bgDQU-vOxS4kMh6946B-BWYzWyyoj9gf8RisFxFILXMjHvPsGRKimaPAUDzIvxzZvN3uHjmzVcWTIsYZfBk6bEZ2kx6UHoXraIuRQIWvKXu54KusmaAzE8ZTKPoZy-N2BGG7aNAaHSwe6F1wYoTVqVKQps4RRsnCPmMOjBN_81r3Fj4F8LdG9_9M0uLJmuWhC1kcOgbDWWh7fMv67ltXxE5GVvnWxXzItbAu2Cqyaoum1YMZcweENm7da9JueoGIFEM7ywVIrX3GKXVNrpWNHEh7z6SwFyXxj4GVQGRoQKy5PxDqVoVzZuQ0WNBTCdf43iwd5nqhG54mdxptFAQhcSNcs0x3bSaDj3wy0xUCjH6NDT1JL9TRViTVkDzlxAG1xSzNbYMISpTRm3CCGAbevONxum9RyzWXbWFFDxeXo8LJLm43rHibUHmctDHLsKvv72OWmkYHIAnVIyjrbYv4t8mcKhMF2H5rcoZGrXWF0tKtyYGHbtxSqXmPwLAkXGuM435wBIY47-F--sF_0ywC6eyUCw_1ZLjvjBJWdP9Eq_ytW6Ln8dqjhG1GUM7fyLDGsv-TYbinpLjW7-3AirgbkkZC9b2Vwqnx6MiFMAgA1TIaY5L3P0mpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBk7ZLIGFAEhLHEr1EOXa67KpJZQJa4fK62GuTYidpFmrYL8ZKmYDIOx5nNvZJVhLIQHlQunhMmRyqQTh1FuEQNeHviK8jR8HDVDMDoq9GTtt-joNxLF2z6eekKmHYb3C2b9Htj6sKVw5b5jIaUNBg7CCep8E8fpJTPAXpWdiPNsOnx5rZ5uewpz6kq5uSxK6XJDwpwvcn_csM1SiRm-fHL5cOs1r0VNbG4ywTU3DCzjV9G_fx0nEK4yxRA6Kb7k8_j3iF6kOoQDUmSzUldOTcohFzwe0BIBfFX2p6BacuzKLRcyFh23yybY14FhMMp46gkpKbumP3VuKpW26_Rdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Uys5KuL3osdJJGU8I-c-TtsHDVHUserww4eNIIbPs2K3IVI2C8-NAuMwgRo-K-hVWONDoszSxZAB1Qaz6E-ROvp7q8E2EmInaMrMJY-qnNRsVohAM294xPT3bKXfn3lUT870vQ-YLHJ7Om-Scw5apPIuTJVXfC6TLWl3Tm4NNmsS9UcUVIgN8CbVLaYb7rfxT6MIVMGbnvQq5cUPSrjCL8pg8ksuYrGykpbJ56-hoLCABet-Y6e2VM1jDcXtii6ejIet25KcGS0btqnzU_Fv33liEUbXCqk8Lhy5UfHtgtYSNmCOHmjZnIMILYjpxFxYNpWR6n9YSTsla4U5CI8BDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMl1p47dNPtlQSOITiUM3QbrU9dk3388erPTHFr3iOOQSkgcAw3JVrsMgPx_o8layU4lqto3aNXmCoHkDXzuR-56CzxIn7uGWARy6r9CAgprD4GD1R_0-xHNuABomepz9Nc1k8Bw_XGQH7YnRG2GYI_KZe8heFCf3FblNKDLSvZR5ry6OtzbEtjPCYp60qAisLv14P37LwU7uzG0i3JjYbRXOW2fpUVy-9NKSJJYGyGsBjYJXYPEw0OYVO-RrXMEkcatmNuVpVOR_3QMT_9zHgmnnogsgZBYpfMBU36sn1_wq9c3mpNIZtjsVIGVfBlYAcVq64fMJAdKfz0U9fmV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCDDRPp2nb9BaFcjDZ3_stZvWx13GbBbEOMoEojfsN5Te2br4hqdUVZxB7HadeUmYoXxlzdEVu0v9k8pJTE72G6m_STmRJJ_hh5BrvaS6HFmj5gpbnCAQkIi8eybOPSw4kqN9_2IhLXwDNiDQGmoovRvK_OAH027vQZZpf8Ol-RBwATL-0yM-hodqqwwWp3EftsqhFg7OQSgz3IVTUCHVzzf9BPff1ETuGp8VvMaNQmJU3C6rC3d0OJeuLDg7xddQIm4iqgbQQQnB25uxnt_bR0cCnOBUEkdIIenhhD-ylFg7leiKvc3CDIL0LL2oNkLjjbalC2VtChRY896pbkR1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=uKali8FUGIaNMd36sDatst3yKkspHqn8LFuDE6FBYrwxn6EkXSpyFoo42KLEzvulblaS-XPX0B53p4DAZYQAYKFnH88PBFNCyiDijeQdtk8EX7bPm0ixGK_8TiY-TXe_U-iH4FDiZE7ea3ELZmRgwIbwUFCXyDB5_gBP_FriioHxUXBkQkeZm9_1i492TUZ5rNwJtcTwJlj-TOTMwQZh53E3HUQDL-IwCbTXHCsxQQ3Bpm-67dNbmJpvpk6h14bA9-KqBRFm8D5-QdJT8IJk_y2cOA9T7wu3p8RitJWuRwI4-6gdTTLryPdtsZLkUO0eEHgzR4lmuG2Ovpvz1zkByQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=uKali8FUGIaNMd36sDatst3yKkspHqn8LFuDE6FBYrwxn6EkXSpyFoo42KLEzvulblaS-XPX0B53p4DAZYQAYKFnH88PBFNCyiDijeQdtk8EX7bPm0ixGK_8TiY-TXe_U-iH4FDiZE7ea3ELZmRgwIbwUFCXyDB5_gBP_FriioHxUXBkQkeZm9_1i492TUZ5rNwJtcTwJlj-TOTMwQZh53E3HUQDL-IwCbTXHCsxQQ3Bpm-67dNbmJpvpk6h14bA9-KqBRFm8D5-QdJT8IJk_y2cOA9T7wu3p8RitJWuRwI4-6gdTTLryPdtsZLkUO0eEHgzR4lmuG2Ovpvz1zkByQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8WGw1q3ia1_osZk8ehTpj2S0LZnhvHSBqCvuxJ2tUhXIT-IYiX1g5CTUGcOXWVitlBU0nlLd0vhQTkpf2wQHL4QzRnB-GKyBhYVD20KS4Fw9ZzhQBi10lOfcuknxgT6thc4houty7lCyttZXSws4FtmAoZ58fevFoeU_UnmMJlcSmBFa-KLGZOjzFI6PkY39lKLhXrQ7lu6uESDw9HzuDVF3F82-7GYcjRHRGm_aqaFJlLlab_i1n3ZUkqPzoEqEXjTiCJz6vTDt4STwAVqVioIBF2N5Y_d31zKNIKuDT8VCCqyFU3SYU3-lh1TCU6Yg1_K1GYD6FkS0rhizqD8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCybRxZ3kspfkgksOw2ZyqLry3dmlh67emUDFXJG7cr8zY-iT4rOIcs8eIJbqu3Z7TqStwzEP5z3UUeJAieI5fYQTfyQgrFvq4VUQGL5YgnmRdIDAPWaObpshAHV8IgPWdSqlcDefseonIP6KhWVX2wUGtwrtLcDYSi_dZWaIhhqf3XGiHv51eVdKSWQrmZpbkC32fSPl9QaNx-DwqtaIUMeQFPugqWIEIWLEE4I2Cw_WOAmVIFZxFm3b_LSA6vG6EFJ06XwIpNBiSm8I0Eh026E1-IT9SdOWQC7xYO81xTbjBBkKWh0gmwY-QNLbvVCrbD5kAsudYvWKGpIYV7b5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FF6xfb-fqFmUTQSqAgLyEaOKBcLvFcfEqErxNudUzMc5YXAGupwLms6JjbmRraRlmSwfE27JvHFi-8j3UVap2sSd3uhQPbbzOSTnQSUEfnxMrOhiYL4P-NdyTOO7-pZPUJBsFMjO_oITPLOYIt1NnPWX6-T8p8Y6cEVGIVZcS-LLfk59ai8a75qohROcBRhQkJYX6n2_Tar1nuVrgZ_1OGurgnLhI0vhT0gVbV3nn4KBIlC1r1Zpwp83KaONaZhA4hjr_Jt3OXateJLQW93d65OQdOMHQaYRfzqumBWYh5wZeW8SqAxrocZP73H1FQDiy1WUBsWXzgqSYFmZrzcFCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=OshVpJGDjnE240IdpIH48M7EnQzaXX-hTEU9M-KWrZLqKcer03KRb4JIfQO1PFdIsPlaQp6wHVJ-Qfl1q0uWpUMstoj9RCFJhwmiiWWFuyTk2X_WBmqIDfHbvSDFudXsqq-uGPAf-j81L24vxJybKqaeh9SRq4x5ZFsAXmb_lBhkcW0tmB1GY6PVGc_f-D1MpJyp2g_iLegsixlBLrUQtjnLdtUr8siGBmTiKnRfnyNqIcXRIhCFBozt9_lHRSfv-YOaO7XfTSPqtS-fUH_dzfNbwZhlDTmnOocEfBlVhaNdYZKtlAe_7y7ZgwuKETOm6ULr4IMPr36SeETwslHW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=OshVpJGDjnE240IdpIH48M7EnQzaXX-hTEU9M-KWrZLqKcer03KRb4JIfQO1PFdIsPlaQp6wHVJ-Qfl1q0uWpUMstoj9RCFJhwmiiWWFuyTk2X_WBmqIDfHbvSDFudXsqq-uGPAf-j81L24vxJybKqaeh9SRq4x5ZFsAXmb_lBhkcW0tmB1GY6PVGc_f-D1MpJyp2g_iLegsixlBLrUQtjnLdtUr8siGBmTiKnRfnyNqIcXRIhCFBozt9_lHRSfv-YOaO7XfTSPqtS-fUH_dzfNbwZhlDTmnOocEfBlVhaNdYZKtlAe_7y7ZgwuKETOm6ULr4IMPr36SeETwslHW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGoekgXYF1YwsFrF_g9C0cN1ToHENvymyJqk-VUNmOsf8qNxebRvebi7yjK2plqOz2x9EvHSH-BhMkwRuyzsaEsAXjXt6hcOqKhbYzIg1B9diVaGTueeUlUnJqZuMRVdFW6tCE5McFXNxQbGmqAsER1Dnbb95TjLaZZ3boBNAJwsK4olu77a9_mQofkNWqFm4T8banAyTRNpka-vcn5gUf5Y3-L5e6vYsMwjeYOdIXGJA-yLKRkrvLPLPiROQTHVVxikq_JSZGhosoQOkC3pPk6LuY5kYWSdsBkI14Aoh4TAvg-q6Pi9WSn2XIBlX_S2FBXa_gVnTdRWLpmqIc2xJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_6n_bpJXlQ3LMDpX022XyLkYemB_J-fd20uBjSdS_la-vGifnb0Rto4Ap-ppsUuj9hDVJT99M9wceJk2RdSxG2QSilvkvtUhm7f_HY8lV2Y71a7vuS_TMgtGXsoIkYtGpsEkoCG5_tWoen_n6S94HoIRI3jQzKtsjF0-rMC2AU7VMBLJ9SRJZMM_2bhkXz0UlMy4miglSZg_50lLxTT8h_12u3Sr1LnuR03Eon8CSY821km2820u-_LHJCD_N6T2j2OmrTS5ndCs2y3MIUxZHI9i2PAng3woUJ6jETE43WYED_pfVvMGE4HOPxZ38drkogwJayCZtF5UGdTyi9BSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=Vd0LG63xOt2hkJ5pLVqzKjQwE0Ye7hhyGGhozZIBdpje0kh2oUJB2jfBGSRk9Gkg61FdJXGhq4Db21mJLf722jjm-bRzSkVD6YI_AsmfQARP9PbaV7TIAdz7iuYyYMVnd88ApqDhPQn7N7Qj_CZF9tWcoYNuCO3RUY3TUykuLuPXfLTAhIm95wI3wJAh3BUVnv9Ot91xuTQszQe2fPobQP_84HfDg7JTPJwMxPlJ3e0JNZA5NEpT4hS-3GUyFUMZevSAvBNe1bgwm5KLsbO6hDSZsVAugKH9uOB4_ONb48UApD49K2yyrQa1h7XZ5IJe39f3fP64YQz-stnQpEOnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=Vd0LG63xOt2hkJ5pLVqzKjQwE0Ye7hhyGGhozZIBdpje0kh2oUJB2jfBGSRk9Gkg61FdJXGhq4Db21mJLf722jjm-bRzSkVD6YI_AsmfQARP9PbaV7TIAdz7iuYyYMVnd88ApqDhPQn7N7Qj_CZF9tWcoYNuCO3RUY3TUykuLuPXfLTAhIm95wI3wJAh3BUVnv9Ot91xuTQszQe2fPobQP_84HfDg7JTPJwMxPlJ3e0JNZA5NEpT4hS-3GUyFUMZevSAvBNe1bgwm5KLsbO6hDSZsVAugKH9uOB4_ONb48UApD49K2yyrQa1h7XZ5IJe39f3fP64YQz-stnQpEOnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwvFLlFV1ckdde2DTUz32N0JbnXKojHRRM2Lhz2I8AFympgtJYSewy7htGK1AYGJlXbvHUkfXLRjkKBhHOiEWBObr0JwPHPaQ6WD3eK16YVJrBlE8kUJ_xuNiPQkx-FKepsT-zfoGdq12dmwPueHcaxJUXD5rWdtYuzCN3NdhLRv9nUp3bqiVXGnAUgrdSG5wtE0Bs9QnBNwoxVNzQ6rzmnrIHU_kntLD8cIT-7AQtYXi-z3iagxvc75-ZjJlsq4rVmyHyWWs9gLpHuRLitLW4TgkvYEI9NnpbqUtAJNwXhSfs1o_FOopV8FAmouP2wkbFeR4uiuq5vAAqbESRSvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omru5rYisXe4_Ip1Ip0xFga1pBcbt1MhB8LJ1Z1HDSZhL2Y-zub5M-Pd2AIqSjXyvtTyecL9_OSyRk1EdbeWErkSCp-4BAhytIKRl1NszFCBMlUwd_JLeayGH8xri-zpkq0LS6iMbyYvC8fpqkohTuud9HGqkGLd4BKrBnKIcYxyZhKgdTdOgre2pvoLPrhWQBVB9aRkJwzM9Zqi3HCrTVHaetHJyepLLiiWB37Sy9G3iFOHWQkVn_Sr722C1SGgThRQ93tt8CMlaiIQMvQHZQ6Yf_HE2tTuXIlUQ9yMh2subtEWZWMtg1uSAAzcDD-aNS4u4C6yHyUozCroNsY03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1fp2KqhSikV2JOs3sQtfV8G5aY4GqBlp4AXnCNTkD1pCHW67gmwyq0MrqmS3ORJ33BOZ7FjHt1gj9hWYSC9IrJrK7d7y-wktJUmApEOEhQolR6SGGz5N7qZZ9xupi8721T3Wp0BG_b1WpJdNgI5KhYb14SKPqDdRuOinHMpNMbnygfnCSpFgdiGw0qwxqSTssvDIy9E4moYmT7blFqfveCl8NLjbKrXGU2tsuVedqbkp1UWbt-ylB0vaze9g8YfqHth8kND49AVkAJiH8ZeCPvZ5MK3OyTLEhhsiSBYc6HqFMg0XcTkXwIa6h_51fAqkFTBO2wrlU1VzgwWBUbW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_gqVwhFqT-z6c-ibeHY-ibji5MBaDKqVooKLCSFY3DcQaIyLZAivGR89HPOFrVOAbGTkDSuemsKefecQLmWOuD37JOWq-5hD9Jzc81uRklVZKawNn19JIX4bH5YD4z770B3to30L_l1rs-mw06g15ZeTXnR_EtUP8yFEp4t_MrILAZZfL2bjmdYdkwcUQZL415FKtr4tTquVO7kWlpizRVVG-18cDcxfjWkmhl-5cq59AnrXK7Hti3_Lpj3GDOx7citlpXhaDZ752DD0zdywEkyFWSl7zsFfcHWmNxDqLoS-XBTu7zF5X7mFmUFknQ8ZLtDwXMS9dviheFdlGG2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=UUc5GfXHPDL36yzZgeCLHNS-8JRR25jdF3xMwpTsNZ4ClBU1JRiAvNbM3qcCbKWZDgAlo8xvuI9otCzUTmLSjji-d5BgyE5wfU7VSSNWRBSP6v5oHyIA15_FaDkEZa3Kp-eh_Of1lY0lMKSSS7eR5uBqx4KsBISR_eGIgA3q7w1_NZCJ6lsy0t0kbmK2_Qwb62cy9-zNHtdBoJoB0PiHnIh6913Ysx8CaQ0JmbIjP867Xnd0iXDHRWgH4TjYbxoCvao_KtrpoDnGscYhZrcoVz_2HRV4D76OJHdlKt-DaAYFFMglh3unygnU35zJN8hnxEBJ6OPekwkP7tbVMJUc1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=UUc5GfXHPDL36yzZgeCLHNS-8JRR25jdF3xMwpTsNZ4ClBU1JRiAvNbM3qcCbKWZDgAlo8xvuI9otCzUTmLSjji-d5BgyE5wfU7VSSNWRBSP6v5oHyIA15_FaDkEZa3Kp-eh_Of1lY0lMKSSS7eR5uBqx4KsBISR_eGIgA3q7w1_NZCJ6lsy0t0kbmK2_Qwb62cy9-zNHtdBoJoB0PiHnIh6913Ysx8CaQ0JmbIjP867Xnd0iXDHRWgH4TjYbxoCvao_KtrpoDnGscYhZrcoVz_2HRV4D76OJHdlKt-DaAYFFMglh3unygnU35zJN8hnxEBJ6OPekwkP7tbVMJUc1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4-D50lZgIwaivKGOO9P63VsBOZto8PL6OPFN5mVpoUqrN9KuMtS9PfuMn5gvn6KqYjHzn3s_7sfajVW71IIFw5P_UxEkAQpnFmhdD60KmHQwFIg3PhfBG-_U4kKFTlSnC0amLtF9dhSlibmlzGsj-SYkpeJEyQeOnTF_xMCLFtbSfk8z-uHTKWeHesiafZ24vwVz-Wcb3g7qQP2HfcAHNM1KH073iTPFWHb7cLuMQO4rclYrYuSK712OLd23-gGwqH4Oswe-d_aOqkj2MKjHvUwcIUgc9hnB8-xgb20KM07TKdp0JwFnn8G-hvI9DCgntdY4dKhZgn7WEbZNmfWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8k_Y5cSFbVL2wyEJhz19RnQB33B4vdEv78gsxvbBe2sTNTfnpa9x_HKZp5PinKdVQ0-jQm_MM4kAJijercg0hRcLPjDsxT2BgSLd_hKtHZD91o45mfts5hI499gqx5oQhMh0YlXRmb2waCDs_tntclOG7PNGE-WWbyZP0H1QQcIy7_jxm1gdmVP5NhmYZl4KkYNM1kL95Qjvvtwp4ty3u41sPBR0NigmSykLn5t8-uY7y1y8SozDGpyIWMbsjt0JWXKtmAoRKniOytWLhN_N4w0eFwB4H9UFpd6NzTLyIqR-7jVMBY_VEAUDxAO1WxoPebmal-ZRB19tsVtjMhUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=bp7U7Z48kqp1GK8mWD2rMoVgbh98CtDQlaXeHtvyzCFuhos-XwSUMQpNKR3E1Ma3rT_U28t7Sn4haC5uretnH3FYALDC9ethsrWAILcyoqhZ-WetwDY2mWTLqCMqt-zgwFXE4Tg4K1pVLVHJY24W-O8rwSxqBUuWVN3yHC4Dt_Wgd57T45GS77n0wKDlQoERjbSy_0VgdyghGQFfhXLG7Ebe9YtNWq3nZCGAeRB22-nxkdr-ruVMMpXnQ1PhtzmUWeM8cvJTsaJKuSXraXWxF9ZJjXOsXVIicJ0WHZDJOfX5_fTj46S3doVsVD3bjNtRa-TtX0NcUNhwG3sZzTRvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=bp7U7Z48kqp1GK8mWD2rMoVgbh98CtDQlaXeHtvyzCFuhos-XwSUMQpNKR3E1Ma3rT_U28t7Sn4haC5uretnH3FYALDC9ethsrWAILcyoqhZ-WetwDY2mWTLqCMqt-zgwFXE4Tg4K1pVLVHJY24W-O8rwSxqBUuWVN3yHC4Dt_Wgd57T45GS77n0wKDlQoERjbSy_0VgdyghGQFfhXLG7Ebe9YtNWq3nZCGAeRB22-nxkdr-ruVMMpXnQ1PhtzmUWeM8cvJTsaJKuSXraXWxF9ZJjXOsXVIicJ0WHZDJOfX5_fTj46S3doVsVD3bjNtRa-TtX0NcUNhwG3sZzTRvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFmNZK7Y48G5JKPfjtTLArjesdlbRzcq4xomUM8WdyGQapr8nrlwm1ASA8j124zyz737iCS5jVK37vbpxqeh6m5Y10ku55VH9zsS6RdrCwxpsZwIySDi2m3YeYNipP24fD4093veP9yzSTlwgDQUtoXiAETtAG9oyHuOTkHDKLui5Y5I37cp9apzEg1ZkSNtsyAguptKxjnuEMSjTvmBOC_FNSrO8bCPSpL7VR6RV0vV-yA16oxHnVBHf9Gxi2aJOeIwE6BjdpNTgbt04VGmJHwNNPcRjzpXCTNSL4kM62eIWchmmi_nV53cZHtYvjfyFBPdRXK3uH019MfvDpo2Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wt_r1lozJfb3JPFkq29bD-9XygXvcG0fsbya1uY0BkPhbpfibcUZddUDdO_MIlsRW0q_WKvbY5GhW0tkIYKyOKR_1L1S5WR_5JOYCzP2MJXYKA1q2NVSU8YYKQeP2r__hbjj0yBKh_k5v1vL2hqBE11n5r6tbinMxuombaEuS6aRunQ7atoEx1aHeaRky-ktQQHWWWHbhJaTvFnQAYwcdXrAsLVlwgUYx4Z0PMjKGxxm2LexsiR6VWKZf7_WkfVDtsx3o3i5OL6cH2Ji-FukpzbKAztizR33EIs9m-2HG35rWWYTFFluh2VXJ2KAJvg1qmGoZQuAKdX2bz6Ru7wi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=Ad8eyWQPC3zqjNKciUvh7T0Mekvd5nJe8ES1cGlgOWdDbPF6UjuEyodOL_z7FY2Q6t2JYh2SiHXZBvOPeP6Ea1Mh_jjd2btFUvKZ-0a6GlBwNGZYp0goQ1qrYU_amIARulCEW8yoE6Ttuii0l03C6st7yqCPWtRCe1PqfgOGxw0axhUumYtDw79I7SaIkyDo2nZQc4iPEoNIuGBJDLMk2FU60uZf6jXHGT3ghwVQYGV8DCp0vgfn57_n_f54HJNd90rL-ep7xGBchQWK1PUH94FcXP7gqKrpVWbOO-kXQncpxIlQSztpSougbfXlfsOiuJ5GEuUNfhyFdvXTiHTzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=Ad8eyWQPC3zqjNKciUvh7T0Mekvd5nJe8ES1cGlgOWdDbPF6UjuEyodOL_z7FY2Q6t2JYh2SiHXZBvOPeP6Ea1Mh_jjd2btFUvKZ-0a6GlBwNGZYp0goQ1qrYU_amIARulCEW8yoE6Ttuii0l03C6st7yqCPWtRCe1PqfgOGxw0axhUumYtDw79I7SaIkyDo2nZQc4iPEoNIuGBJDLMk2FU60uZf6jXHGT3ghwVQYGV8DCp0vgfn57_n_f54HJNd90rL-ep7xGBchQWK1PUH94FcXP7gqKrpVWbOO-kXQncpxIlQSztpSougbfXlfsOiuJ5GEuUNfhyFdvXTiHTzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mm9FGpPp1LTJ_Kvi9e0TyA0L6J_yHcToTT5rul6rjIcxnUYENfgzrWKzFzxEZw4gGcgi2IaPD4bgcOwwMrqpP4v7Y2PJugsNXCbwhwm4W7pWQsg4hthoRIPD1NMJBc0nKaXO_rwixu5esRh5YvojtveDXhmy0ELCUvm3kvdwkqawC4T7Cj7Dcj5_Qv1v3cbGf8ubIBY2cnFvR-ycIp1PI1QKQNkeEDHznEI043i_p1oEfvxHUwNU5006Pgo4TtXk0D0f8j5ZLnthx5ksfsvJE3MMeNy_z8MyrrmpPKMlxgYAjOhYU6zky5xFwDq8tFk9Rv8afzEdUS9KkAQARsLwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=neCggowD4IoJMKXP1MP3iL1ysG1WV2PCab_T_5B01iIm1lioFA0k39wqVZfdZ6H7ukHRu4dzRk-bMz0G1WGg97aRgloF2bKfPFfZjqof6jVj9X5TLE9CqHTznOzSzVw_6sEMDi_Nm0CIi7tu4S_xOJzAUEvcclEqi3KEVOKf_n16cNxg-Zk9ZB4a3SDfZnHJA5CaDFrbPuoqwievxImURg0cNTiwog88UKElr2z4b1geGQZMRAZY2fT-l2R6JzNW7KydzL6Mcq2LhBD5agJ5SOMql8MazTQAvHQ5DLxMpNGGP0Ha0IAYDzA1U8NbXPO5Dmfq4HVYpSvCJi2jFcZvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=neCggowD4IoJMKXP1MP3iL1ysG1WV2PCab_T_5B01iIm1lioFA0k39wqVZfdZ6H7ukHRu4dzRk-bMz0G1WGg97aRgloF2bKfPFfZjqof6jVj9X5TLE9CqHTznOzSzVw_6sEMDi_Nm0CIi7tu4S_xOJzAUEvcclEqi3KEVOKf_n16cNxg-Zk9ZB4a3SDfZnHJA5CaDFrbPuoqwievxImURg0cNTiwog88UKElr2z4b1geGQZMRAZY2fT-l2R6JzNW7KydzL6Mcq2LhBD5agJ5SOMql8MazTQAvHQ5DLxMpNGGP0Ha0IAYDzA1U8NbXPO5Dmfq4HVYpSvCJi2jFcZvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBeU5NdJSK4hTKN_VF4OX3Xnw5GtmK0dqWWYz7kX8dEzD48j7Lqf7wt3cgPyo6hL1eI3J27x4K2Fi1lskHnSVYBVXRcsZ9kH4OkSAIW50j-qYlC_x1IJ1NZYr7e6-ZaUi1G6joQ7r_wJ03SNV-ELhKyYgkdFm07JNZMKC1tR-fWsjPD50MBo68jxZmxYk3fTeCbaPYJf--w0DjUNgqW7Gxd85WNGn9NruQRowxMve6UA7ZrKUF9JWa1h2di7Us7C4DkXCX1bBqdVuOVSYrKGo7mBS65B_xkmV8zp2x4ZyxwEXcOXFJiWWs2m1lk7u4dsWB-aNN_rOzz_i_Hro59-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIHMy1mq0DD3W7OEVrUN-BtZegIH_Ou0rmoe9hB86Xg89dKhdvTvAXv6hulubN7UwLy-rzE2714DDNLwLCwqBg-iNp2-y4jLAiU9AB_d0nwXDloskrk5V5sHGl2wlQ_EEotev7elE7Ar_KlOPg1IX-HLePfoWOQssY7zUjDW7ImfIgF0xHXHBNGW3-I8W16cWyqwvpVcL9TFK9QmCZlkXLUQNu4tFJEttsavIobPqo089GdnfkzCagwZn2srs78j06gEk9x5xQuaV5xGIn1ntkjOAo_JtguI5OHVLbCkwaaNrRz2dwr2m2YpECZRfxH5GDIC6b7YDdm_PJqCiKP_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=Gf_zUW4hiKXsLpLKpLgCFniCVhAU04jCqQwJCqNDnKQwCic8CGG_c_EzmYTFer98xZBwco40HwoeouOXbRw09uwJ5k80ssYR-6F2C0fx8Iw6utH5olHUolsIhfS7u-aEz8-xmL0w_h98rwl00UXTYOHja_l2sODEg__phPbYjycBRZUrcyl_XL3VCaNzHXZ7hqF0QshmwxeOUTjD0BHEEJxH5RaAU1gsFAm80wh9tcqvnbe9Z8LIlDksoT6dOEaTqI2Py87iTpf4LFkVTdl-Gdi98z0Fu3t8vOXji9TRvz2Kv_GGN55CB3OwCmKSYPl3S9LV5916wJHIJWQI5hO6CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=Gf_zUW4hiKXsLpLKpLgCFniCVhAU04jCqQwJCqNDnKQwCic8CGG_c_EzmYTFer98xZBwco40HwoeouOXbRw09uwJ5k80ssYR-6F2C0fx8Iw6utH5olHUolsIhfS7u-aEz8-xmL0w_h98rwl00UXTYOHja_l2sODEg__phPbYjycBRZUrcyl_XL3VCaNzHXZ7hqF0QshmwxeOUTjD0BHEEJxH5RaAU1gsFAm80wh9tcqvnbe9Z8LIlDksoT6dOEaTqI2Py87iTpf4LFkVTdl-Gdi98z0Fu3t8vOXji9TRvz2Kv_GGN55CB3OwCmKSYPl3S9LV5916wJHIJWQI5hO6CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmGyHId9YGQSULieyQAH8wkfTaCq9IA2VhGVMcDvU5lKTYdiOMGoYHixW9Xl7ciMXSBCzS9-_lZre5AKcW_z6qIp96rTJB-zQevq56rlHicUDdlXNvBOygg_bi8uadCdQFQlUeZUc7l0lxU-tGowAD6WPJmkPIcKpVeP7MdHwSSpszTz5VMSC7RHbSDs-PdeAELHWNhB61LW8roRuxKRvnvHLB_X6kk741pNKFHznuYTDv4RupfdoKwmjxJ-8r5-HDWKozk9UUliZPR7ErNGMBlt_mFfsI83neo8G78I3_-hFB2ppz_WN9EHvDJG0ldlj79Aw9BbPTZ_pNxzbxBB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/njxoL8to3jGVIa_BJRymFySgaTXCqodh6AMQts9HHY8exWMpJAUdA_NSiC17UzmuP_-n1FMeG-G-Et4D4t5z0fUb36YDO12fxvW55KkZUZ5cWUL3vrPBQnVh1WxU2N8zZChVo3u8_2pDGmYUUfvkXWctakmvc_CvLhCmzTa3N4LJKMTBPgc9cGfbJnufSkCZPhKb4JxZeTdWnTUxaqA5xM2rFPSWLUX3RUHfmDyo-0s-h7k3HWZuvgz4NV4lR2ns2YUqw4-cy2X-fPG5_UgQKSvCMjQn-z1Fv70yeXqEHdxE-De1ptPT6Jd6NpsJWAhIIJzHkYi31aaF2rZe3tKZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=WEMUJkXZjONXZoZT3p9Dxk0Vpurgyow_pANnrs_xzC842NAw0MCsY6uKwVyVeBWSVH2gRe-Ouz7GvzUV5H6YJoVt6if1kqJnvyv9oRwUr5XVFey0TrEK8ovouUfaCvumuVm0vJxEMyRcgRz5vLiEBUyVgDvNcNg6ggXKboQcFQz8SsrmfLJ--zwjLDIkmhdbqsx1t4odkdu9fLDMJSHWRBqcIupH1YcUoldEyQlzwOzQT-3tvCyPXAU_lviN9pHPXmjy4IHnrzJgrMYdBKLKbCc4iJcMTHxQ24DplMb8ID2Z4bd3kShIUsCRVCbrCB7bgxOzi0eAVPvcPfLsCtIMCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=WEMUJkXZjONXZoZT3p9Dxk0Vpurgyow_pANnrs_xzC842NAw0MCsY6uKwVyVeBWSVH2gRe-Ouz7GvzUV5H6YJoVt6if1kqJnvyv9oRwUr5XVFey0TrEK8ovouUfaCvumuVm0vJxEMyRcgRz5vLiEBUyVgDvNcNg6ggXKboQcFQz8SsrmfLJ--zwjLDIkmhdbqsx1t4odkdu9fLDMJSHWRBqcIupH1YcUoldEyQlzwOzQT-3tvCyPXAU_lviN9pHPXmjy4IHnrzJgrMYdBKLKbCc4iJcMTHxQ24DplMb8ID2Z4bd3kShIUsCRVCbrCB7bgxOzi0eAVPvcPfLsCtIMCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfFzn6crurNnN9oVi-rHgvBM4UuC4F9eMdDQC2ztuDDo6ZIqPD3SelUOEhlkdJ3oIbapzgzhKr1KSXcWujys22UH923kVgPnSIyjkyun9kSgcmeFcKe9TcO5cnLyCbpSlZ7riNLxdnGPRZf-mXIq4kwUYRgPjBpE4reC9Pf-1IYZje7eTfjXSHchSMVoDztRatnyr_ukSUANGOybwzSYR99UTGCqvFxBJVqIZS687qpSNrZ7VAKLUEaS01kv5OJ1gJXu2KMMY-Hbgq_xykVNNA5gL8l1IGE3wcJzkms8KGbkyVgdvwu08mPfWD3qT7cdT-9Qahl50bDhewd1c_8kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=rV-2Dz-gmZXwGqnOT_K16JnKNrEExC32JSvEOwaqF58NRkVJILESp37m3S7I6WhJAVZN0B0tyUrGz0PZjO3LH-ceLcZ1wHTUBt_H0HLgV8X7lYc8-ck_hO5rXXznEZm6ol7uk3idfKh0jBsKf6OTc6o61f8nOi9IqX4Ft_zsErKDUlgZkw4fwmNtFlYYK3J_6qoPdd63ZWA272S5boo7RbAAd2JUNIE0PWZ8-tjUQrbaqR8py2d3y15UsqX57WpP_pxft2N0FJmwzz3-vbaXOXgx3_9eQg5ejkRTK1HDDlGZUyTCSpffc5lZ78NUrNNsL9uUnfHZg3Ej86FcgDGErQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=rV-2Dz-gmZXwGqnOT_K16JnKNrEExC32JSvEOwaqF58NRkVJILESp37m3S7I6WhJAVZN0B0tyUrGz0PZjO3LH-ceLcZ1wHTUBt_H0HLgV8X7lYc8-ck_hO5rXXznEZm6ol7uk3idfKh0jBsKf6OTc6o61f8nOi9IqX4Ft_zsErKDUlgZkw4fwmNtFlYYK3J_6qoPdd63ZWA272S5boo7RbAAd2JUNIE0PWZ8-tjUQrbaqR8py2d3y15UsqX57WpP_pxft2N0FJmwzz3-vbaXOXgx3_9eQg5ejkRTK1HDDlGZUyTCSpffc5lZ78NUrNNsL9uUnfHZg3Ej86FcgDGErQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eEGIY_hlEoiTitM8keQGEniBPzSO4Zz7QV5PbXxRkKZuHLbxIjkGZ0G0khIHacpM8cZMYHAk33And93x2prQZ6VY9hT6B7WvIttQZg8H_VgE0a7VWmOjqQdyfg-lAHV4QVIojAUPHoC4Utdno9UQZXyFJGOHjYIMAsPZz1PGwT2AJ98aGhVEYmgctuBhDLPGhpZs0H6Y5eH7nDFEPPxs5xMRqE3516ISAWBeCkz-refpSAcRs_Uj84lv1oCSijBKRNVo2vQ5LCHwGPRC_C7dbj4E13FnnWWMmXum-tbUBRa81ar9ATFO0UMBnEmXTaHPHfXRKxHJIc0gM8G6jsQ-iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POkF-r6F04o6ZlUvwW5vmapqToAsELFiDX2tAFVwq29OyK9UJaNlROVVCncrZkvulo2cqrr1TW42oRHNM5ipP8mnATpfczbXym4NFZQ0o10lyHat-qiDp8iswUFDdfSSerPP0IQoKZ4HUiVaP7zxpjhisiKUjx__aFFoPGD_g2KuHU9w1hdF8ose4hwkVnXRpbNrgAe-6U2MGsLHY_F8b86Tfu6CMKEyZnh8wQ05TsY43RD-HALUkV5TfnddGjCk50-hrshjq4lX3qS-TpvIhcjwkmIuK-q1pFZaiNhczMuvTLTDWxwiAo40-y9DuYNX5n27jZtrUwMhKtZ0pQDKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nYGnTXgCPB5ktPquTAj9WGc2vjWwOSAhHuKKccbuEMOetISaUEoeGOjDsK-U0RXku_fdzibCzSbRW7q8OTar6Zve_K-0g8trgmTXBwSs9bru2itdthuEmI_ZkRswnbkz1GBUMamLb61ZoszOaHATiVgzfzfmEnW2eNzauJBtpg7P6zdBksTJYKB9oV5gcOuv-kgjQexEhBbxDALnJq0LH6x5ztsljk7Q2WDUpr4cAvBaatV9daeZVisgD3x_sOSSwegKUHcvMRPE7_OpRODjhk-AsYOfPBr5KmYBehtZMGlBGC5269R6PctBSfeNpwN73GRjgdzSL3e_QjPI4Qs4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rnfiZedV-_Jp4TbvtWJi4uhBW2Kux90k3bJR174BMoC563YrixZCbItBduJHaDMYLGVX35sVzw9rIAKOXJLWgbgTbtqkKVY4y3ABGTrIdZPmO51kleS4E1s0L8Z2tobyzgCg4RpbQIk22WPrVFYWbDH7NcYMW7OBotI0WfXFlTCwzWyK6D0r3ANFRFSkgRlkrdqE_bvZm1QyxFoB9wq5Y7EIGJ7ZIzwGj7eKrxvICzziD06ZGNIql6kTFidzI53nCxBpBq-so5hciAbqgyeNhpWaUi4hrkYozGjgRjsa3iJ8VHRsMQTOenQVw8nlbGFYTKpq0pwjhMu-crVWVg9wWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZczHU7FIbIrVILNvrAZzgUs2G2r9R3_oLTFcdBQLLi7ORSf3RbJhs0XJhmKDsGieAPXpbGuiFbIcAkB33-9ecLUEnj7Y5LO4W-Ex25QQsO9qbhFesZnpfEXZWmgvqvOVnaYaqrGrD_idYw_iNPIqkG7BAeatNa9VfK6bZ-ituitd-ee_kEYmx21MiXqorJ380lkRHG4qyoBlygOnVyGpi83Op6R2BRScA5yLgjnpFp3uPkGBkD-fLSZj6lUXxrV7Ae72lrNR_1QFQoNrSKK57znKnt9nhalV4leGaUuhpRBwsVhlyqK3FPpIh4D8JJpWd5evFgaN_r1sxZ5m9RgVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkXW4rKK4-3-TTPsiv1CDmHiFmMaipY8sbkWrcWWPLBR9UypzXhoLzQcl3JUNAWU5eDoEztvXCSdkKX-qfH9hbsfq4y0HNGYAZsm0hJjyzbvZSJ7ObOUtc9_Sv2KZSsQR7ps96ZmElVSRffs7DIUdlrzGPLbnzcxPYBfmrzx8fKEp1HZWtDMctJyyYDZJ70MxkGxO7GwfIgSo-522UE6CMcCHQiFIXbTfZvZd8F9frbj2Slc654SoXvThnrelKJRC65aFgQTcOzP-RobC3ye75b3BrgTgkPosphWo2VoD2znjB_ugiqlmSkEDnMS51Qf2SnjUqds0C9WQeXxLN3xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=T4XKcqwyH7hilgS3HPkZSP21avumwxZSqg10bQPSaQyCD0uQuSX8cBsaMqgFWTGfAjcPR1G2TYOIqo7OcN8HDgckLpZKDCB3ciAT4Q_T-vBUQlrQvOHpW1KoiG-W2mUJOXXm1zZfZg4xtd5SGhgz0_nuJErzb28bE1Kh3hcOUHuB8FauWVVJEo_9OUSsvbPqbFHOd1qfhy21XkMHWjdGIWJ6dLGp9RZ_7g-3UeMCx_-uY4DC25ESXA76e_25WdGgUxuKAkmywRc8Q2GT7iBPuhhfE2EW1dBikYBGJH5928rpLeRpT4xFHmiJAInHdRq7wOzGfvNf4FIgwMvbPxwtSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=T4XKcqwyH7hilgS3HPkZSP21avumwxZSqg10bQPSaQyCD0uQuSX8cBsaMqgFWTGfAjcPR1G2TYOIqo7OcN8HDgckLpZKDCB3ciAT4Q_T-vBUQlrQvOHpW1KoiG-W2mUJOXXm1zZfZg4xtd5SGhgz0_nuJErzb28bE1Kh3hcOUHuB8FauWVVJEo_9OUSsvbPqbFHOd1qfhy21XkMHWjdGIWJ6dLGp9RZ_7g-3UeMCx_-uY4DC25ESXA76e_25WdGgUxuKAkmywRc8Q2GT7iBPuhhfE2EW1dBikYBGJH5928rpLeRpT4xFHmiJAInHdRq7wOzGfvNf4FIgwMvbPxwtSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8RoUiNSPpQYfz9CiOcLtkUnK0zXqbY5MrbdySu0Na0LRbFQd6SQvVWcx8L9Wd4nMUqdGch_ldvtsEMTYrpjKkoC5VRMLpkILc4f08QNMMtBLgo5NhpIGDGDV1pC7rJWCHkxGRYbVzcs1dwSiWLTwD38P-ybTSOSHeDSGhE14_htE2d0Tt6YpyzAnyOdSYsmp-ek4_wNurwQ10BKx-RWnhQp_ghYNSR2EGKi7a8Z_2ROcFnQer0QRuF7axVByYHoN3nJmlQ5CArc6qjnx-Dt5uWOPnAjuld2l6PDHv_IUBEQFEtwG7DrYgTOcTRpxdg6Ubhji_hqS35_zqwTZryUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPPFr3CS6cCgclnioVka5sfag4STvGqWcvTqmgmRKqcZbmz6v8_RmijSOifHcLcZVB3IqxBNmECNIVxeBF8FIJy7YNxgLQSaUSz0h_tNOkJUOxgVkVR0Nf6EtvYvg73MJVAbad4h1DFvHvRMBYz_oMJ-qw7Uw2edU6oT7pGUViTMqs1SWZCc6KE1xO2WQlHCcX4ZxB8Rdq5qbGP916qhTYy2KDs7lhmJNSkYdu9uF6Z7YsG7Hj2psvjLBdZeODOH-dEwKO4y8vqQygvCdxPuLh_fEuiJRSNyjLTdxZ0eFoVG5zOt2a5HMe7wBMOaPygcBjpx2oSxC8jv6R53nFKbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7pwaOqT2n9UWKMMFNBgDCTyq6yPS09eDoTo_RW5CuJFwkiaSgjdVtzk_BBvOQpw3i_H6nKWGMkkJsMBuuxow6MuPR4ZE2RWpVbyWXvMS_afLlvf0aM6caO3Iw8dk4c-CKqcIdLkP7M3l-Kd-Qgn9pJXW7vdOO4k5ru52nOtNSqR-JVOYkeUhbmOv4gxMAxPlzMhyNdHySzzXra5RixINVeC5J0BsuXFR1ccxbPYABdZgfzEfiwVaaW6N4vnyOqVnNPexy3h9A4wNktUkZA6ZZuX-6YugvTDDoVONoy8Jn_UeUHw-K1reVre-0oIwyyrb7OeWzQc5QzdLUqAOaCr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUVxBUN9gDYfOT1SjtmS38QSZWOtalUC4Uv5WvzsAltIKFKeV_mo1T0WC8duA3Uw36_dsYz4u1XX3tSfLxkSVMkbQNVlWYlNEUqU0YgiqrMzY5WeBb4SXnAEq0uSsVcynSiz2SVtMFY36BIs5W2ENcb5z_dDCvQgyOkJ5YL_ae3NCaJzWr35XSYGxUDPWLjzZSeyTx4G5wsk7F-FvYm2yC8mpyqkoRCMY-BSc88HrJeKv-Lwnf21TfUd_n_BivSkYLjWIbnnYhWZuZdGo0g0foaPnmt7vz1RXcTIZUMiTj6S2F-yy02wKNkG5ualrT1b6ju51iykrOMd2y-ZcabN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=NVu81vHcioJeU27V_nVSmrtTpmPzNC66iBPjXCx-1NWkmXApFxfAjYtri4Zm3NSWzyEyMgNo8NXXFEhYVcA0AyA5lpMgWctzQT-IAZ3YmjdOiH3r0BcNxInBMB1keKWlRK9U40M1WXMnhotMgVPdFm8fr-V7J4rB73B5Y8xglN7IljXtRKSeRHLX_Yxp5yavZjYeTIy8E_M-49Ci4QmBhga_0VuHARylRWK9tZ8XITS-XCyLwU31Sy9MLKSY8-IYUwD5FHleeReHVloAxfkwKfbKmYyfDt0DzIq4-zZBDT0Edwse1gIV2R0zFqS5AljU9xoQBWGGHZq6zgMCrDENaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=NVu81vHcioJeU27V_nVSmrtTpmPzNC66iBPjXCx-1NWkmXApFxfAjYtri4Zm3NSWzyEyMgNo8NXXFEhYVcA0AyA5lpMgWctzQT-IAZ3YmjdOiH3r0BcNxInBMB1keKWlRK9U40M1WXMnhotMgVPdFm8fr-V7J4rB73B5Y8xglN7IljXtRKSeRHLX_Yxp5yavZjYeTIy8E_M-49Ci4QmBhga_0VuHARylRWK9tZ8XITS-XCyLwU31Sy9MLKSY8-IYUwD5FHleeReHVloAxfkwKfbKmYyfDt0DzIq4-zZBDT0Edwse1gIV2R0zFqS5AljU9xoQBWGGHZq6zgMCrDENaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=AcJaUE_Kf-9pxiUnSTFlBU4P7vV_PiAVEHgOej3XLF9_hyvBdpfgL_OUXgR22QzGO8prWIoH-Pf81tPCdFHR-hMJT1GGseWLUa9ZO8VrRPElkq3RXGVpAsunAOpMtSlyrxM-MLfBU6zi2Gpo3Xfwr_Nta3v5aTxkYr-AolZSqgSOEO1cSxgzBOMLlBN0FPD-alspjiKFk2Gfg-8hzQjLPwCTvlRBCDl4ubWFTjwiedtNMxeMDOZN4y-9NSAMOYYWrROSq_7TbRbtZHeH6e0SvOdETdSFM9CrZ77Fwu8DDhk5UxxR6habJtriofCnKGJx3x_uEXQUqJvJaGgYHqirDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=AcJaUE_Kf-9pxiUnSTFlBU4P7vV_PiAVEHgOej3XLF9_hyvBdpfgL_OUXgR22QzGO8prWIoH-Pf81tPCdFHR-hMJT1GGseWLUa9ZO8VrRPElkq3RXGVpAsunAOpMtSlyrxM-MLfBU6zi2Gpo3Xfwr_Nta3v5aTxkYr-AolZSqgSOEO1cSxgzBOMLlBN0FPD-alspjiKFk2Gfg-8hzQjLPwCTvlRBCDl4ubWFTjwiedtNMxeMDOZN4y-9NSAMOYYWrROSq_7TbRbtZHeH6e0SvOdETdSFM9CrZ77Fwu8DDhk5UxxR6habJtriofCnKGJx3x_uEXQUqJvJaGgYHqirDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=ksLqg-fVH8kxwHwvOcFSpplH4rKoVP-rk9voMr7r6f8CaFA7GzjoWEPs3mdgDbgtvrIwpcD-x7-JSaLINBMtKXn2o30tbNxVIGuCfjClzCO0bBV5zWsnmROWLpt9TvdJ0ml8fvkPnJ5s8irCgINcEyy1Png6Idx2_pBM2kmmFN5paOTClg9uVr9f4ocwbk-1fdMFOSY9K2YJifADRJL6TVSCMZdR0pgEMAo60to4yNCr0PiOV4yoEsM1r4Dw-jHc10etlqQz84jgO3VnwkIZh8EOwhUW1cGWM9hC3JW7iMFUAqNcaRfb-D7tzfxHYP7T0Kg7ISNDa6qKqGr5xZQiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=ksLqg-fVH8kxwHwvOcFSpplH4rKoVP-rk9voMr7r6f8CaFA7GzjoWEPs3mdgDbgtvrIwpcD-x7-JSaLINBMtKXn2o30tbNxVIGuCfjClzCO0bBV5zWsnmROWLpt9TvdJ0ml8fvkPnJ5s8irCgINcEyy1Png6Idx2_pBM2kmmFN5paOTClg9uVr9f4ocwbk-1fdMFOSY9K2YJifADRJL6TVSCMZdR0pgEMAo60to4yNCr0PiOV4yoEsM1r4Dw-jHc10etlqQz84jgO3VnwkIZh8EOwhUW1cGWM9hC3JW7iMFUAqNcaRfb-D7tzfxHYP7T0Kg7ISNDa6qKqGr5xZQiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUbCsn0bvcF5wH5ru6W8MP6lysNYjyUIJWqnV6YVR2M0QlJgFasemzlCzoB4cp-m0kepy3GG4tskX3jC3eyRSQp9ayHFoOn0WeLHgjlppHYD-xUluN7VUEydrHOA0DlTTae3Re3TfRoi-yLrVH0TjuL354NQjyOZGGdIyqdFMmVS7Kf47dyAbS9CizXrvzuNPD3ig04pbpTCENxnyAguGxZQt6GNDN0lqicz36U7MKTXr3qovFF22lr1o_wi1lRYX1PkJkWZxdKZtmYwm4ZYMiwl2WbcUwpfC0hfCmDazrNJHTfCCJgZHrznDGAg4ga0tpxE7xISH8xWHzOh89suMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yxckwt6sV3CrKR_0xKg6-D1t0KEkoEgdq92ySuv1HpTOME6CZVEoZE1LcbOnGL2R427T0JdxuayVMh-vbmEh_EH-P6OfHfit-B9-n-XBZzkubLEZv6LbE4S-F-krwMY1J-zC2lnLqQ4MufZWPSp5TFP_nHjQJuA14A0T0NYsVBYknX2XwhiX8h00Px1giiu3Uw5CQN-x1iPLOOJY4ci3zl7zztGfB17lrPedutl4ePPT604bgq4DrupNAFv1bxYyr5Tye6Z7LKCAml9eXleu0HXiHx1VlOriTIr8rn56usSOj8Fz-El16GlryPJ5mWOi3ADeX9xY4CgQ8m18HZjp4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
