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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 18:58:13</div>
<hr>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRfAmhOZHZ1zWYjmXQUYvHpEPZjnn346TkQ8bUEZbqWj0_kI6J4nSIGT7_6WEvG2eOOb10BUU_mqD9f5Ow4LR97fHUMPbbvg3KFALYXz7XXkwDoeN6yFZw9PrEHj8R4h2WKv-uZtbt7bDXdGiGUsPhcUHJbjm-KNtKW8_s39RBwDD7kfeANosQGhh_Hq0kQcLhPz4GnChF_vEplbRgaNw95mR_7nevF0AStiGIrZIZQwfKuDxldG-uUiz5RYChBoUiZ3-18w5MT1Hz7TIkTCrP5LUVsFE4YdzkJJltWZKBKv_WZl1T8iYX7JbmyNPpj2h8EBgRfl_KQQPYRNF4dotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCF6NrUi8bl98tqOo-5vO2XBmXFZrImKrYZV_zN-Tyfz3ZB8v8uqyfx0JYSyToaqO7R5CYKcLUf_gdd3DsBxj4RcLIzM-vsWU62DOn3LMvet6ajNoiJv3w4IpRge_A0kzcQM8yav4n1HI8vnw7VKpJ8sRoZNz6NN_MYdcKURpHt3nl-36KlIVmUBzZ4LLgoql6vL-wq2l1tpr6-hcvdIfuW58TKVPfRQihqkvxnuaIfLVwsfgLdBTUIYefdui_CP4oviZNoJNmRKgWHu2Kmd3rf3MODbGDH2Z25ousoF9lHIaYJguhjqftRBGEbSUDdcPRdQ4CvJMAlNvJqgGa9y-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=g5If-UU_JfZMIa_-JHQDqpmmximgHUFPT7pDjX5aXiGvQrFSQETAk17f3pqmtH20xiOj4SXko9u5DjBCyvF499W8HQcBlp35I58LlDGYDvR7ehtTh9Smxs95HZR6fgXlvgPP7H1HR7r_CvqtmIy9gZJlxVhkpqsL4Fldc08-QIfy_uvhQrna-WbG9uxdxAM2h2h4ygK3z3O1MjITxjq9yAD4NJLOQzVcitZgYgTMxuYrZMqazc68kRg0vYmosv4mvGb3_o4z1Cvb3D-BOYfNh0b8PFfxurU5XkAt9QU_4-fG7RG4oirGJKx4Ny5_MMNjaxo6dEqPhXA-z39SP1bqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=g5If-UU_JfZMIa_-JHQDqpmmximgHUFPT7pDjX5aXiGvQrFSQETAk17f3pqmtH20xiOj4SXko9u5DjBCyvF499W8HQcBlp35I58LlDGYDvR7ehtTh9Smxs95HZR6fgXlvgPP7H1HR7r_CvqtmIy9gZJlxVhkpqsL4Fldc08-QIfy_uvhQrna-WbG9uxdxAM2h2h4ygK3z3O1MjITxjq9yAD4NJLOQzVcitZgYgTMxuYrZMqazc68kRg0vYmosv4mvGb3_o4z1Cvb3D-BOYfNh0b8PFfxurU5XkAt9QU_4-fG7RG4oirGJKx4Ny5_MMNjaxo6dEqPhXA-z39SP1bqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHwZKSoIXQoAkUGt6bfwPKeoWE1xDniqWy97Jr1VHDGgq1u7cmolnm10pARiMygNo-ddeIWLtKtKsrC4Z2XYAglYqQUA1LLpluZTKhALUQRTkBaCBZTTvPTgPV3qFPo8YCqEgf1NbtkzNFOSgbnoQasF4GL46Hvmy6jK7hpTIpiQIue0lXY2nwjRB_pWRLiCkrPn5hrR3F7J1AzKeZsfUjeF9-r-U9bWU-QOydbO2lwKfbHPyCzNv0gvaU5nCpwGb0fWp7VnNIRYaLak-BRWRLNE8o6qEI5x6PHyxUJi_72SRpyTlI2at_Tx3H9iTFpIs4Lb9UdU0Oe-1wTjg3YhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tekLaxdUGDqYRwCBajwdfnF-pLtxl86cjyqw3AschZ9Nqlq2LjFmjaUmJ7xyCIKCDEwne0bzHCNN-_w7McuC76loz8E_Cu0Ysg617zcqEYxIEDB94oOZclUvrheBCaSmhQ1rTAfsblxAcgZbsaQVRtYJBvb9mR2vlrssNqYC353uYfHwGw0ONp-FDdHyOADjaNyq9XGx6Znf8RLPhf7YCF-pG8v6LDBLpu91ZwJMBwt63wi-f6WfzSRSyJHnXJiFHKjsYQwgqjQFtd8SBe3wymPZAf2-96X4DPY0RazRn9zB1QQ6WBbQZiYYde7mhRPbJ7CUOPcDWsuKK0p77i9I7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=dHjK-0FjGkSjRGzR6s3ix21nG12llZ8YDtWRp61Fn4rTtIJF3NwzK6FQRXQ3bHBjg7EbgfUHynl8V5_t0C8_8OQPhtEVThWqyDHl0EN2peyjZgNSF8Uq2a5wnxjscwDn8BSQKzbK6fqnEnKHNHW0-Cxig7ZGI40-BQdBWnD6ETsmoDf_aVPnFHZdXUvp0CtgY4GfOLTxb1fLm0zYK1q1FHXk025jMxyLpskVGYA0uoIu9Ot76uArBZLiPp__a_dtnQ0_DluFMxYIbOyNucE7oxrU4_Dlb27xrV7FGMgE2Nz3JsaKupjp1V9giQ1KrTzy8TK789Lc7mKmYFikkbav2lul13qTGt9-82XsKp3rlpg-xWA8RN8uzCwFuOEvcplzK3fDl90xpMjw3b-SGWwwqLz_Vfg_JafOSPTciW6xStDz4Hy3spABP7Cc5g_Q8uCzvksA4DVip4Lq8pa90-i-UaQSSWM1K6zTbTos0Zlw5pn2-itWD72ArS75gAHXqhiUKj1yBp-kVLKLVQIsCes7zRr4WrvtSHTmzrxeQL3sGgwEgwdTszAaWrgOAlAczKVQ3DOiV3DDcMzuDpY22SCgKZgjgZdidvTIn1r8NZeckFsd1SobbXLu8u_0VU1tm7Njst6cCUeeFcO2oqMPcmyVDi76WzgzPWp-BsFX3YocQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=dHjK-0FjGkSjRGzR6s3ix21nG12llZ8YDtWRp61Fn4rTtIJF3NwzK6FQRXQ3bHBjg7EbgfUHynl8V5_t0C8_8OQPhtEVThWqyDHl0EN2peyjZgNSF8Uq2a5wnxjscwDn8BSQKzbK6fqnEnKHNHW0-Cxig7ZGI40-BQdBWnD6ETsmoDf_aVPnFHZdXUvp0CtgY4GfOLTxb1fLm0zYK1q1FHXk025jMxyLpskVGYA0uoIu9Ot76uArBZLiPp__a_dtnQ0_DluFMxYIbOyNucE7oxrU4_Dlb27xrV7FGMgE2Nz3JsaKupjp1V9giQ1KrTzy8TK789Lc7mKmYFikkbav2lul13qTGt9-82XsKp3rlpg-xWA8RN8uzCwFuOEvcplzK3fDl90xpMjw3b-SGWwwqLz_Vfg_JafOSPTciW6xStDz4Hy3spABP7Cc5g_Q8uCzvksA4DVip4Lq8pa90-i-UaQSSWM1K6zTbTos0Zlw5pn2-itWD72ArS75gAHXqhiUKj1yBp-kVLKLVQIsCes7zRr4WrvtSHTmzrxeQL3sGgwEgwdTszAaWrgOAlAczKVQ3DOiV3DDcMzuDpY22SCgKZgjgZdidvTIn1r8NZeckFsd1SobbXLu8u_0VU1tm7Njst6cCUeeFcO2oqMPcmyVDi76WzgzPWp-BsFX3YocQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=g1W5ScdiH_hxnzzciYg5un--bNl3aogHQ7I2-q1oBUqz2X-flJ691Vs7sLmaJvxptrCF3mP4UMKGxJpW735_Y4R3A-jxcVOp_tr3fx7XEGDz0qwXjONtO_yuStBaixkG9HNvqP507Bbi-cI176YnsivIQMwK4aFg6sAfSNK9-FDS3LpnF4ItH77_mThJBUZekId61yHc2oaYd81CyaqqSqlCnpEjYCu8hU8kstGw0QQz6oMYVgpswFQj3AQsNDVi3b4ab2Z3GqXce9Rv0gTkpu3tnmBc9a0ZtLXHjXzqKaPXc2oB1YIs_AOVyuQhi4idLmNUWUzG7MHqCHpa0dBLbmtnBs4kty_iJnWcSWi4NfzyhhDbxHMXKJg0UCMrX1P4j4yoScrILx-okH104CdiBRkvDQGItWcYt9x2k5717MYfBvpZ8mFi42iDCExJnH95O15K7kCbVSI4wPdJxyl8aeLfG-HIwMvpXZojZDDp7eCFlyjmMeCYrgRzEb11J3Y0nZ-8GRlXHhZfDNnFWo1FxvbownMTvDajbaWTC__S_d7Z9coWMbm5VXpi_XYxvvQKmxTnm_jBWzWW5l06snALZ_f_Y7b0BAeUmJhTTrYJvFnaL8g5hrA5MR3LvwnSBS3nHiStcqdzlCtcqtM_HXSuFHnuHrN1fe7emeZMtRweZFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=g1W5ScdiH_hxnzzciYg5un--bNl3aogHQ7I2-q1oBUqz2X-flJ691Vs7sLmaJvxptrCF3mP4UMKGxJpW735_Y4R3A-jxcVOp_tr3fx7XEGDz0qwXjONtO_yuStBaixkG9HNvqP507Bbi-cI176YnsivIQMwK4aFg6sAfSNK9-FDS3LpnF4ItH77_mThJBUZekId61yHc2oaYd81CyaqqSqlCnpEjYCu8hU8kstGw0QQz6oMYVgpswFQj3AQsNDVi3b4ab2Z3GqXce9Rv0gTkpu3tnmBc9a0ZtLXHjXzqKaPXc2oB1YIs_AOVyuQhi4idLmNUWUzG7MHqCHpa0dBLbmtnBs4kty_iJnWcSWi4NfzyhhDbxHMXKJg0UCMrX1P4j4yoScrILx-okH104CdiBRkvDQGItWcYt9x2k5717MYfBvpZ8mFi42iDCExJnH95O15K7kCbVSI4wPdJxyl8aeLfG-HIwMvpXZojZDDp7eCFlyjmMeCYrgRzEb11J3Y0nZ-8GRlXHhZfDNnFWo1FxvbownMTvDajbaWTC__S_d7Z9coWMbm5VXpi_XYxvvQKmxTnm_jBWzWW5l06snALZ_f_Y7b0BAeUmJhTTrYJvFnaL8g5hrA5MR3LvwnSBS3nHiStcqdzlCtcqtM_HXSuFHnuHrN1fe7emeZMtRweZFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4qbZQo3jhbIaU1OOI5VnQJHx0goE6WC8pMr4WBKq8JKSnke6mUZyhIzIaJPvAoeu2TmAOd6e0kqQ0x_OSrJpsyEzEm7GEjO4YcsGyRPgkoKQwUaXfO-edtWDVyPx3AL5edQ5S0wf6_a0BmkmR9AzgUd5vLL55H9Tvr9cmKHHFlIYAywC6Ei4X8NEydywYmBkCG1zQvu78-jZvcQD-4VbjHYBpnbKp_wKsFq4jQbZn1iH-q-G5lGKH6g7N8ennWFYmFCJBcULn8TRd-VA5_FS_PhG_0r9A1XB1PFaplmBIAriKNMtPOMK_pnsNabzgjfRrNIE6TOgBcP5KfdaurXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cd19iY045oDhSAlpROWc3WxJwP6tlbVywD3fB0jtfmfVCucQBBJu37QNSZcI9G60-KBqsJN5V-2uAEklU8A6BgXntnwJyRIO-gHFt3cLW7sC6e3nDhBx6X3LHEl10Gmk7zdMhMIQE1UfvaxLcvml4vBGi82NyZWkxy3S5UjjJkxr-sZDCWmeZ7NRBF9jVbOAhYeNn2AJc2FwkRFeFJPQw_WM6eAU-OL288oDx2hO049eVr9FfpH2ypCsXy2sU2AZP8k07XqB1NIEpYCr1gGtUZad7lhYNU2ADC-7dUFmgwxRH_19uQzw-QsT3whMk3I7H1REdkH9UQX2vrDcCgm9WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUyaMGNNppORqfQYc7GdnjvzGYnI6nndRHdUiZC2hUQ1_6SdaKmIvbaQewO6B2ZqrL0s7GVJ7ZQooeadaR2mcr6rsr8ekIqon2ZynbbyY3UjsG_cay4-dmBZL00fQTtEZobzxHxexKZGLdZxm4UYFrxwzTd--429gztWvr5UH4B72xk-6ig2j2uP232_UPb_meS5QQwAqI9vg6XYqlYtLOosk_EnfGhyDn7RbaV2ojdXvB4RzBbOWLiBVj0RjOGD9pbRElTSF6s6AymqV4qLgeWNNtqz1iUrN0tZ0LPSs3U4ICL22wsM5KKrXWk_ydhR94o_Xj07zMDvk_CuykRjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsiF_czdiv3P_s_KBm5wvDzdsO4Ki5s-i3HsWXIxZUReCNC99AGrQkQxYXp16EA5SFEMZKSbFKqZ_A3hpib4CRDsdZ9APVPqmpmNIIFxBfu0W0Bep7I5WbK0pOJqoPAS82u534NYQbLFMV9x9k-607rBtJZS44doOjZu9eYu40kYdxNIOei37rr9pz5xzblUfcdwrt756TtFT1dJSXt-BT3hXhIr58LdGE7-blJ06AyKj7831TqrHMLs5FEVqKDA74iHb2y2hsd7YLkQDXaUqOV1JnarwdmPMnSSfyntj27Nk3gcgCS5cQYd3xUdg4ZC-d64WLsgzbehuUBky3fWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=cAgeY62QBhwzSWEWd6lvcBjH6tYUlse0F74HFGDi1QfNUwvk1ZSv7K7hFzmPVJdscEIESB9QE8J8GA9CkgUvg52F8_YEl8gwVQf_5pBtPW_C9l-CSVnuTu4pS3JLBpPnLx7bcHxzDf326vEHMa63mRJKKLLGS984giRT1DtiR05GEEibMNBEJ4ewNKvWbdXyadl0nEEMlzE4vZrdZOWa5ynMcPaQqUy2UqgKlh3ZDcB1GfRZMo6ofm4-C4SYN0-elCNTFUZq0adr-Tzu2gaJPWBAwLVac5O3aBaXNnwNX0Vhab-LMIywb0wzpIca8GXHUoi54EAlbZYPZv0bgOcKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjWXpJrfEIYdzjudKjnBAw3XwumH2Jx-6Yh9BRDYf1g7QnfcPtN3aG0_YB2lgxyaaAt4jULCnpqppQFc2S1FHz5J-AjC6mvD4xLGdY2faO5GZ5WqMC9hiOGIKt6jzlaqPXgnA8YC7W05eRlJ2SqPMvcbOW3IsZk87RU4Byr8wmQ0gFmF4VdEvoVY3ERazBhWQ_tqV4V1_OQB_bavjjJki2L-Oy9L_tMQXPOvbu9t8n_Gw5XolhOVVXkRqkdNedOA5NaC6AVPVAQBxG9TZOCD0er-XV2RHfBW7Y9dJKNXCDntCEMXImfEs2AtC1IMfYjjkVu9Ot95KoPZzBAJQxRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhHvZwXvtcW6rKnbVk8xW5gdzzZGV2uxGSkNCC4vgMevqm9cdgYLM8PRKCEn9mTI7GMVJI6Jo-kLAByELHzeMHmM85cdJxPtGl00PskrP5tJ00JUlp1W97YMZIWFyfoo0-J5FeDHXAOtIjD1XQPFIdsKn9pdTZfQLGe9nnGJwLL9cEw78ucccum6fSui9WfD3Ya2-me_7hOXCQ53szt8JdvndhQ2_x9qhnGnjvdsfzDiBnFb2Jg-sujLqTJpI0hPl3xYmdwBLvjLyB7ceo5DdL6hxN_Jyezy28AuiOZBucrDdaluIums6WhdYZe4xzg8TJQuLIsn_QummbBZdBM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONhfIFY-F4rSHol8RkawhITl7MiOpP3Lven9H7aTJdE9qDbTiOZ7Yfw_jeMfFRzGePMQ7y6O4GSuZXfc8aKn7tm06UG3ncWiaCy7f7yOKGs7c6C-ELadh96qMMOyn2hZ4BFna5aV8-W-XdkxGg-5NE3AopIJLWsTHWt96KpJLo_94O4BPQ1qZpvNtJ9YSH3EGwJg54FVS9fPXwT-Pqc0NkdeAxJXm_QI-sUYk4B8MnVhiYUG6ChRjFA4J_2HhqtpMco7p5JYyUk-mE8IssjVcIq2XaFLiZjjB3KdHkwEmcAcoTvwDGOE3mL08LKSzKgS4kJz1i16G1V7JdIst-nd8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=cJrkOT37p_si8AB5R89q1d-AY2OVl-JtVgRH3gQp_a0Oj6PKXoouPtzskmx1COitkxuDgTCVhbfGytgLKhWZOZ8ph_rHWowQZBQoXmk35xmu9S2d6p7tL-MCIRIB1HDvu-56G18erxCNQM-Mx5PQof6Oep21B-ZxGjUJLoyiugfiailJfKW47Rwyf2H1bUs5sHeYiFN-xWmsqR10IzaeoxW9CSR7fwzAMt4JDim8a1oWmdKfyW-5Nzj1tSt2FRsj-auM3tLDFINmV3sMA3rUm0K4xE27KmFXqfV6AWHo4iAy8YJyilXRGNCUvKAAUvbtIH-DsNLm-bft2KIVkJYDQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=cJrkOT37p_si8AB5R89q1d-AY2OVl-JtVgRH3gQp_a0Oj6PKXoouPtzskmx1COitkxuDgTCVhbfGytgLKhWZOZ8ph_rHWowQZBQoXmk35xmu9S2d6p7tL-MCIRIB1HDvu-56G18erxCNQM-Mx5PQof6Oep21B-ZxGjUJLoyiugfiailJfKW47Rwyf2H1bUs5sHeYiFN-xWmsqR10IzaeoxW9CSR7fwzAMt4JDim8a1oWmdKfyW-5Nzj1tSt2FRsj-auM3tLDFINmV3sMA3rUm0K4xE27KmFXqfV6AWHo4iAy8YJyilXRGNCUvKAAUvbtIH-DsNLm-bft2KIVkJYDQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL2GR7HnOkcjhS_aRV7kJ0Uhd9EiM3unc4Ua-wZCIErFanq3QRbkVFHsnTmg6AWHplc2qUMzoSzPd1vZ53sRtqYJEcv2FKIdkhDNQOSZtb1t-Hw6ICGxFCAjE2DdsLGBvlc30bLka9xBgWgpD2EJR5IhQwmBqPrr3vNdCQ2-ATbtZHURDRJBsE7nTXqq4gB9vhCZeTkhuwrk3M02E0YR-cD9X3clAvt6ClaT8SZUFfF-94uLqe8VDa2IyFin-EBidvesVnbQRwYjjaf36qys0-PwlPZxTOWTYzWhO0TMoypQ3zSfV0qzkMhmReYBP6ry--r--Xclsf-oPVkCeSB8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-78LdLlGVX2BQ9HF_QF2xRblav2Ol-fA5kQLJk7SGNo9q7OYLk0UV0JCs4vevoHBXnUMmknz2p4MTtA41yOo_N5uB2gTerXwfT8X7nl_cSXuLhNansWlW0PVM0r4t-jEAB5IFNp7zV9QtvQwXOhLg2yqmMOnSMmNiU5mseZQ3XDzdiH0L8yQ7BXgIx8soU-sf91KV4gZM68HYH9PBxrvFeSRTSDBXmETSuFVwrkw8D4BXx_UOudqRz2-QcP3zrE8_kHI1BGsNmJ5IwDG7fOF9YVJqS9BdXgp1cyy4iG-ofCN4hxXO5yfbEczI-vI0Ium__T8nFsFUzrwHmltREA6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=At58e-HGZ7PKXJf8GwZ_pPyqSvfEz8n6yiMdBAZ-YNkjuu_DHNUl-pKz2WpSqP-IZMhBWBpuHaOWU0PWthURIZvKHKHTandYN3OSg4ilb6P7RyBYk4CRu_bj8VCC7HNpYLOy_O3aaVHCGJmSqrMdsygSDEJStQ-vebv23u32yxHm9Lva2bPAVipLUsp4BMLLY9-i8hENI3Z181NT-1q25T3t-1JRwSLg3u1AqG2Fcd4Oe10eEZFu-ZWAj6z1SFzbOaAI9JQQzufL9iECcPR_ik1oZxPa3pch_nuoQz-k_lXawUiXrV5mzUeZhzvDa6M0VEek6p0lAoioBUp7tgy7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=At58e-HGZ7PKXJf8GwZ_pPyqSvfEz8n6yiMdBAZ-YNkjuu_DHNUl-pKz2WpSqP-IZMhBWBpuHaOWU0PWthURIZvKHKHTandYN3OSg4ilb6P7RyBYk4CRu_bj8VCC7HNpYLOy_O3aaVHCGJmSqrMdsygSDEJStQ-vebv23u32yxHm9Lva2bPAVipLUsp4BMLLY9-i8hENI3Z181NT-1q25T3t-1JRwSLg3u1AqG2Fcd4Oe10eEZFu-ZWAj6z1SFzbOaAI9JQQzufL9iECcPR_ik1oZxPa3pch_nuoQz-k_lXawUiXrV5mzUeZhzvDa6M0VEek6p0lAoioBUp7tgy7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6QIiK-IbKxSvDg_vg8banJ7mHM-acvvzrdN48r9H678bYyPEDBRdo8B0J_T3U9hhNMypWgp6xKiLgT8exSYll4PLRXsQjoFQDjYGdr5eXSlKjfwwb8JqYquuOJGqqkiWY5xh_lX3cFqd751xPdqGRFrMoDkBm2CQQKuXzRRPq_drvNsmqQTKBvWMIZTiL6y8TK4Fkv0GCjHlv9jo-8TbWuL5lIyM3khlD1u44QAe7n7esuMtv2K1LR4VImzMb6JOx7n5rJ2odNg_IcJT2x9kIYfo4UGjiacWb4FnIf4e1WcN6dwKOcd2jJIagvv1IutAadrUGkp6ZdnB2ca0NM3Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaV1vPKqDq1qr85UHm5qvrqArRpyMbc7hiLpmD2JUAnSkJuSTgOODeAIqmzQQBYpF0czLSDJH_a7YHzC32rQMhJ2F8eA3DNaus-jsjSCOtAZprM83Dvm6SdkV5-AHaE1rtuoAnStAAL9DuGeFR4w-6k51EryecdnaAfKy0bZSCq5MZ6kPXf-71NNyo8Y8DQ2wKbPCT7sGPn0zaWK4Jxxy_erpshtNQfwmq4ZeI8k_3TvCSd4YTdzM1TCEarrHCHqBNtBTiLr_sjZaN0KobDYi4_QPNAgaFQBriQBCozkohgI1jKimzdy33Y04uba41_kBd0KxYzJPJ14qQLG8oEjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRgbEzzs81qlVh2Hlvq4SsFVst_0CzUUjFT9bnOvMinvVgr-sZAIDP-YMnqJjJt_Dkt-mmgM-UCNMk7xkRronVwLof1CfsfW9JZDH6Y7evNfcOmSzlXAcwGX30bfsWa_XTRoraTpzrbUzmk3Ie3UIwsL9ZFMesTqcuSpzuYxBCoQsbAC50HId41XyIeArHpW8TZsu4oxDsYgAFZqTAmn_n1txqJWKN_809brmRanVFGWPNChdp4RkdHxPnT_i5uD2_qnZAaW8ygxbrAYkoMecQ1enwmUU1GVvDlEjw72S9lzMMgwbzc1x7eal-rvGx-Sz70hlic0UaYkYvifTTHkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RREc8N32yXaTWHUKeMnDE79ZexTI-O8XhODfEOR7jljjAZdwbDMiZADShb_cI2QwodRFYI13UEDGJKIZCOqQDl9YkbH_4EmlYjeyLzSTdZS1wibSN8M9TzDaxpEt7135RKo63hlC2bFw9PhYJnCUjtVFjBcWGJWo65Y5SQNgOtCBUPPfg_W-mgLl1rks5GyWB4mXIlKgdDiI0oEoiari0Y7x1rtrX_F26u-J6dJeT9MI2L0iZvcN2TkiwyeQ_IJ4AgBm_QqC2q1M3vEXxTrawPciS87mRrqNAXF65h6CN3Pki7LNv-XBLz5Vd_PL0jejGOPQr9Z8Y74wPBFNhWi6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=H41TxM2s5UOIOPuxmofdrqFsvvb83TIIwitgMgiydYe-HT6X1Swo5A7yzx4Wy_dq7awgEl9bP5jzLRGrBWRXwZOpuNivuLgA1opdiZFe9oMSPz7WWSKlWDmgDb0ay3Gsh6Qpi_zHHeDLaivKM7EM-LjSAy-MkpGJNtOxe6XkHHK1iLmTqio39PxZBTle5HXYMDEE7CbqlNR0fADCyykSM4slfeh0bWLMImIEpLTzlLzqIkkv15eQMOP9FAD7Jt6mY360TK7Zkuk2eP5ZcW1WUgW9YHonsw44bJc4sCQWR19X5FAc23lynjfmE1M9YAc1i-WlUz6OmJsnSwoP47-b8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=H41TxM2s5UOIOPuxmofdrqFsvvb83TIIwitgMgiydYe-HT6X1Swo5A7yzx4Wy_dq7awgEl9bP5jzLRGrBWRXwZOpuNivuLgA1opdiZFe9oMSPz7WWSKlWDmgDb0ay3Gsh6Qpi_zHHeDLaivKM7EM-LjSAy-MkpGJNtOxe6XkHHK1iLmTqio39PxZBTle5HXYMDEE7CbqlNR0fADCyykSM4slfeh0bWLMImIEpLTzlLzqIkkv15eQMOP9FAD7Jt6mY360TK7Zkuk2eP5ZcW1WUgW9YHonsw44bJc4sCQWR19X5FAc23lynjfmE1M9YAc1i-WlUz6OmJsnSwoP47-b8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl-RGYb4q92uC92aQLF01n5inpoj9HfivknKVIYeYLRfjU_Yfkd2v3PWMpG3qT4hb0ugNVHR1XCes5KFcOVIoAZwmC6ZfaQFVtsOTGRr7KeR2EPthS-Xs-s49ZyRPFGj4iS8xht-N-yjslH3Zl9vrXYXHyf_3a44Xntjk2qcmMRMDTlL2lm8b47dQNpwuwyThfUgTCeqorT8gZP0RSNsxZNh5ohgYWy_ksA0sBxZl26wtmmSthGjG8EfBP5ZVnjPpFu9AO29LM3-6eOHFs5GqKAPifLboNW4HuIN_a9BaKlAJjpe84ZH-0wFmqjEm1ALcziwG4M7KbMXZl7NZNlM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_kcUUOA4emulbHdJHYFhP5tDBFefWAbk4kaq1NSuB8HONOSeW5woWn5fMOnJ_Z09FTftaiOYNkfwVhFxProoTW4HU1qB43XFYA48S6s67RAeNKGhCp-1R9mtNXzRf_kXzQvIkNtLucecMjkxSy-pDMwMMJQsnM4sGK6EfWWCOvFoarNdNL27HITfAg5XkTRyuNjqPILyXeuS8npTZOyDsvIHXxjpPSmWiUq6ckLKA4pjRH5e9zvYGBo3wFiTrf1Nzc2Gs7vrrjWfoA5O-SaHEkV5a5cE2ofCOSMmAzZ9Bp38ds7V7JpPaTO2PyEehSIJ1BSla965PbAxijX4BaGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=rVUD50QUxd_8m8JlsvphQDTWkNlUglXoUWP-Le5H23QFspLakobRqxWMDA9JNBgswLwe6eb4eQsZGRrkhemxBrfyuU7H8yoiyp5mSV12hBmjKratTUa9cFDVV8rytjylg2siy5JwfLcE4fcpc8h17uOeIAsgxko0BHfAPZBrBiyFK7pXTO6Z1YpqdfEx-7tgc7FYnr_wzu-0iwuimrvlRtSRNANF5jTmVwiO3K3q0dUFHrO4wikuoYKgMsezDcMTUrIdXiiqv2CWXaiJzai-urcukK4CdCgSRBx3QTS860Ya5utmBAfjIssbv2oRsXVC_uMCnuBSdVnIFAMshi2D_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=rVUD50QUxd_8m8JlsvphQDTWkNlUglXoUWP-Le5H23QFspLakobRqxWMDA9JNBgswLwe6eb4eQsZGRrkhemxBrfyuU7H8yoiyp5mSV12hBmjKratTUa9cFDVV8rytjylg2siy5JwfLcE4fcpc8h17uOeIAsgxko0BHfAPZBrBiyFK7pXTO6Z1YpqdfEx-7tgc7FYnr_wzu-0iwuimrvlRtSRNANF5jTmVwiO3K3q0dUFHrO4wikuoYKgMsezDcMTUrIdXiiqv2CWXaiJzai-urcukK4CdCgSRBx3QTS860Ya5utmBAfjIssbv2oRsXVC_uMCnuBSdVnIFAMshi2D_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymh8MnPOEMNFy43SfOgFXOvojCBzKWPLeyWPNk1vu2qsNIU1yQcutbMRwOYqL0k-m_yyGebRVwG8S2TWbf5xW6RcJyezQR-TopHhzg46XQMbYxDZqll9PxMPHOs6tQZw5w49Iq576Gjrr39mgiv3JvmiZ0wAF8Ng5tBxr0wkgF-n9maDEh2K7cTSj1XjYen6V1kZQ5Jd7oyaxDmroJlBFwI8TUKA7gbFh7V_FMCXwm-2ntgOXHVY9erazdF4iwZqHB2tJnBOAVGy36i042jhSENTpsa1Ku8LRSixCZ0lcJXOYRH1jsXP6tlhL9evzJKlpLoXhiYtnjvFkKghEuoCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B50rHfkYUXx0gwcXn4IiQZo8m8m37YDG1xYKHVrnIqlJD10edtkztVuyG4qFDvXmyyZT-WMBfiNeyXMgHQldSnhQTPkoNxAjBNsZRmn5-ZALhsyo96mRlsburb0FbXjngI_JizpXGjWeEqf5JvWZxXk0g8Qvni96-1R2h1liWn50beGerx2ep8RvVfattadMBB8XdKN6vGXTD-fRX-3mx64onNeQJgKf0YA6t30d1jhJoBr3ofchitOogs9JSuV3UKJzpL8iSxkL7ttpkXkAxS3IyWBdavfTX-u6aflFGGW3ANVbFBrCI0bMQGntDOrlL-fbJE6TCSFZxXm5_fd54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=evkAJmGrqYw7jFQrlIHZUAavV8P7e80Kzx_AzLvK07HdujaLa9jyQYiQkLDxWktETPRSg22dEM_mH6457o_XUhO6-UeiD5Rbk-YJvUZ_1Cw7XLLUsnKT_48GdpxaWKfzr-uQZkOtSGAOKB88K_kAw4_BcCj_dbBipn2Nlu2heTvm1KXSt2z4rPMgwFteXXU4dXtFUgiHSWjK8hmxl4FLxuEKmoEsyOlv_HM5g8TTp9IRQTVbNweg33bmxIx-n4eQsIVQaM2UJKMN3LuE9f2ZYoGNe8tYi_sFKjF5u9jtNjB5TfqqqBzdWnwwaL871TdEVli9_nQC_b5GP6QoPHMwqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=evkAJmGrqYw7jFQrlIHZUAavV8P7e80Kzx_AzLvK07HdujaLa9jyQYiQkLDxWktETPRSg22dEM_mH6457o_XUhO6-UeiD5Rbk-YJvUZ_1Cw7XLLUsnKT_48GdpxaWKfzr-uQZkOtSGAOKB88K_kAw4_BcCj_dbBipn2Nlu2heTvm1KXSt2z4rPMgwFteXXU4dXtFUgiHSWjK8hmxl4FLxuEKmoEsyOlv_HM5g8TTp9IRQTVbNweg33bmxIx-n4eQsIVQaM2UJKMN3LuE9f2ZYoGNe8tYi_sFKjF5u9jtNjB5TfqqqBzdWnwwaL871TdEVli9_nQC_b5GP6QoPHMwqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyCil_pqEpX4HhfSb4smhBwKSurnCut_HTVnxQW7ZkfCi5PJIQ30DMkaTBr7QyJ8MfR9NBv3-duWRKpzrE4rTMFbDklJ-m8bVKEIcvgYnL_qojwC_1wuJZiGH3YW4kZIjVx815DyjUX2Wu6uc-MQOy0w8JEoLzj8EabEpTdfESU_hrjHf1CuDl3bGJ-EzUXHKRhJwwZPkIhhAKI6nuOJsj0IpaPwCO20UBupizj1XIa6-KJH-6i_ZGYPug-hpqIllKU2PDEMi-LtFIqPFPFAlkJNdXNb_pIz4FbrbPQCadFhH3b-Cf-96Zc2dRuSlc1vmI00VC95KwZ-xmodkkCn2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1Cd0qzOr_lv-LjpE9ohbbApghdOrX915RsfPH5L_-qnmkazTEA2igmJllqzZx8smwlWU6iF7AC2Fr5ATsMCAfi1HKHDmhkvsv_sjzrSy7uGDH1-cl2E2L7x7HF_2_4cSv_uHqME_Tid-4pXk9g9TxPPLd8uHvKw_QJ9X_cCkBAMULqIgFWskLlh_nqGEu-azXjT1Nm3ypJr8ho1pz9EElh8sZAuMiLAqW1xbeus2gDpob1f4rV7JMmMoLmH-MHu7KQ1GdWdlYpuyi-US6BT98pcfbtrgEZNz5yN0DYGHVaa1HLvMaH-ZS9jMN8keD62Fh6ZZMJokXnui6bq8onOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wc5PaqC5dPbFmCLREgQeilEDGMvc8jh4vzxoCNBo7jpQOp9tQG7EkddBICcehTcXUkusBq6Yp1BpEp3Or3DzAVDfvtFusfG7Uc5EQpgxRjPc5JWiMYnSpnKKXM4IqtV7KWOgFhXMZzFD9shhN-1HBKWVgb7r8cuhFjjvx1CTZzIt_rRvLxY0Hlf3zk6evoevXtyWYkJ0twjFa7yM1DJDuauw1oAlXEqjS5e-G2WQfkWvyveasXKxV4vHTP9rAEbmBtNq0Vhl8guUGLudZGkknxOyOHzAAZEIJgjcD6RbSX-1mG7EyxJdmRV1NVH8X4TOIfqy94d-Ajz-m_SOEMJn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=Wfhc-tNXaoxr5O7b0o2cWXsMUKz464Glxc7bu24AVLLeZv_wO357QWNRp7t6CP_TVBCNX-mtkekXJDU3b3MzdpHZvTzMejQGeQU_a-1pH0R-hi5Vd_bhF-R-LhHWfDPl9XEJFmoe4FMbLl0r1Z9gGryQUczgtbSC7RUBP-7h-0hvjEPS9A6CeB8aZU5e-iZiPA6ZzAM8qxP0kxQVWv7PFWKb1ajeI2V03DlhkCXHdCWDeBVAxwaf_5U55IimmeZUY7gvrK6ojzhcBLykueqKKY_AYR_uTdk6M36ub_YyP0rm2rm88XpVfOfcMtagpd9p-_euAml1AHM_4fZI_mIGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=Wfhc-tNXaoxr5O7b0o2cWXsMUKz464Glxc7bu24AVLLeZv_wO357QWNRp7t6CP_TVBCNX-mtkekXJDU3b3MzdpHZvTzMejQGeQU_a-1pH0R-hi5Vd_bhF-R-LhHWfDPl9XEJFmoe4FMbLl0r1Z9gGryQUczgtbSC7RUBP-7h-0hvjEPS9A6CeB8aZU5e-iZiPA6ZzAM8qxP0kxQVWv7PFWKb1ajeI2V03DlhkCXHdCWDeBVAxwaf_5U55IimmeZUY7gvrK6ojzhcBLykueqKKY_AYR_uTdk6M36ub_YyP0rm2rm88XpVfOfcMtagpd9p-_euAml1AHM_4fZI_mIGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyS2qpxeEjfmWBmgtS-ekeidrLr_3w9k1pyyS5otUzL1AzAKWUQtsfQs0J4XejSDosOdFQ1b9h81XHZH9F8bnX78eQxrAGBaO4BCFjLeGadWNN-OFGDeH91_Zl1hEH4XdIUFKLVKQ2kI6UsrwSIF66vkLT9Q80x7m0CwZmA6FczCg-YZi5GJ3_SWMk2bgwtZDrFjwi838CismTU_XPVxI5oegsd1NDJxQ3MvDRvbXLMMdTI9hDEehyPUCJSN4ES4lbJuNgi9hsFbvQ6h0TG-iucANlFtZgyi8GUtV3T7QNAsWeko0Riyj9Iff_YfN5wcFaY3BH7ZiQC3zUfI_4IsiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/njxoL8to3jGVIa_BJRymFySgaTXCqodh6AMQts9HHY8exWMpJAUdA_NSiC17UzmuP_-n1FMeG-G-Et4D4t5z0fUb36YDO12fxvW55KkZUZ5cWUL3vrPBQnVh1WxU2N8zZChVo3u8_2pDGmYUUfvkXWctakmvc_CvLhCmzTa3N4LJKMTBPgc9cGfbJnufSkCZPhKb4JxZeTdWnTUxaqA5xM2rFPSWLUX3RUHfmDyo-0s-h7k3HWZuvgz4NV4lR2ns2YUqw4-cy2X-fPG5_UgQKSvCMjQn-z1Fv70yeXqEHdxE-De1ptPT6Jd6NpsJWAhIIJzHkYi31aaF2rZe3tKZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=mx2fBrfN_LIlI54LFBAb9Gglk1LnrpumeRZ-gYtg_wVtPcGMuCoY5Vn6mqXlkrKGGKM1OdKdHiTUov2_ZFjPcLf_9ZLhq57-LHEqOIQBt07b8fzvsWVsYD1daTp5b5yPoBLFyRKblLM1qAc3uUAl_tOokak5xhg2FK6L34_mQiz6F9fVR8SlrSWgi1o8MhMKbEV5weg7Hh8g74SYwts4hYvs2UoTGuLQsuTfjhJhP3Awz11NZ1tdHP5z66sk-fH4epe1oDPMywWFlCC800nB6NuHADsJP_70A3gmt8k6UDShDhTGZ2AXsJ6PDP3vtr2hk1fXfLaj2GGy8447H2Whzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=mx2fBrfN_LIlI54LFBAb9Gglk1LnrpumeRZ-gYtg_wVtPcGMuCoY5Vn6mqXlkrKGGKM1OdKdHiTUov2_ZFjPcLf_9ZLhq57-LHEqOIQBt07b8fzvsWVsYD1daTp5b5yPoBLFyRKblLM1qAc3uUAl_tOokak5xhg2FK6L34_mQiz6F9fVR8SlrSWgi1o8MhMKbEV5weg7Hh8g74SYwts4hYvs2UoTGuLQsuTfjhJhP3Awz11NZ1tdHP5z66sk-fH4epe1oDPMywWFlCC800nB6NuHADsJP_70A3gmt8k6UDShDhTGZ2AXsJ6PDP3vtr2hk1fXfLaj2GGy8447H2Whzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmpWDgv6O-SKDNeeDBH0QTRV0agM-AOvWOZ3EBQdK0XQ3CNM3N2sjSKPlAhi5glsyBAvDhK_6oei6sIKYXoee2qr047AlyJuKFirD-WCI5-aew8RCfSn5jpBtC0jjZzpn3BoxN4J2sV869cw3VDYC3z-KPwfgnVfG7efEhE2ZNzOLSk5xVptG_OnH_MgPOVh4faP90GlfrT2F-zUkOK6oQhdq4Om7zaQeUdCIlR1vSAeEEg_JVHS-KjSI7zBbK8K92QQMqdFzjNvqqHUwz5HiGnRFBO_mE2FR8TpkYduhX8m08Z_9nNjyhTclST1R_Wl0OQkd4cTmRpJcCaj3O_VCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDp6OhlYoa3exWmBSwR4_SjKpVOnpEFx5ncjc3hZchxECACquhF5wbOei-CdN1p8ftD0BmMtl6fgNTyP-Df071M3BXbsjdpKTZ3A7hK85Y4qCDvUJGDhHA7SyuEnMOkJNwRYM_CnCoYHfGyI2eTduVH3kOfaKqHDFZsmUNTO4FnxpywcgETKhT76c7T93aAEb8ZXFfAVfzD7TxbCWWF-xbxAf076GhfvdUhdRwO01480KB8TtnVjYHUd5KgOtdLPPyhlj3aUAw7Mx6XRMuuwQnkqCscq9AhreZHIIBVUN03KxRRtSflk1BDK3VBviYvthtHzf0geAxJrDpHP5sOdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dVLtKya3zgsXHbeRq6q1kCOjS3uuckXwmXaG0UPpN8bZTsc2wp0778YDlH3GN1cJZtHAgvrxLP-PTtNJdyc1_m2YAs5-UmmjS8vWakjE5YzDQpgQ40gaxic9UK05_hiCovyWbNChpWoLkG05r7CzatJiGpZpUvuMHo6_74RGwnksi6PLdGxliTnl2qiY7e1EuTQtLeA3gUYvas5KLWeBDKVVqLATNEYHA5vBoho9rsedV07LaUVu_lZBqA982Lh7-RZvkN0XV_wRxNwLrD9QtqP_YCDF_S6e5VzmlzXBLZP-ao2F-RyIAbEW-SFk5vVBOtwQeVj0vRu-2f5gjntI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rnfiZedV-_Jp4TbvtWJi4uhBW2Kux90k3bJR174BMoC563YrixZCbItBduJHaDMYLGVX35sVzw9rIAKOXJLWgbgTbtqkKVY4y3ABGTrIdZPmO51kleS4E1s0L8Z2tobyzgCg4RpbQIk22WPrVFYWbDH7NcYMW7OBotI0WfXFlTCwzWyK6D0r3ANFRFSkgRlkrdqE_bvZm1QyxFoB9wq5Y7EIGJ7ZIzwGj7eKrxvICzziD06ZGNIql6kTFidzI53nCxBpBq-so5hciAbqgyeNhpWaUi4hrkYozGjgRjsa3iJ8VHRsMQTOenQVw8nlbGFYTKpq0pwjhMu-crVWVg9wWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhXVGql7CYjCnjY3TY6Pk-sx8aY7I9f6EDWNKjAYRk7RQEwmLnpM8zgaMroHfCI4DYEEGOeIS_cBh3Gi9h4PiP_QTZkLGp9PstEoHOzJUnCZz4WMUT9_Yq1WL_2zdOOHbZ2Er5nwucTMM4Wm6SYP2jY3YSNdEwHj6InnHVBmylPXSImaoV12ATtY6zqqZSL1USCWFYZBN7FnKeXYQBCIW5Kg7N4z9Xgm_yi1hcJt2Zs4p5pceHQlDkpIE5eD3KBNBFLy3j_BCt2dZ5D8EW5NJfq47E-EYuxR0qFXeRG_2ckPGP_Npc3WdVXMArQnFlkqBlFDzlckHX1PSEqOuhMsJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVWZxyQ1SgzMTW_Z9b3OSsCeYKq5NtV20gnSoRNjColtIewbUd7350iMSatNweZ95I6gO8MOCbJYCRVNmQaZ021erY0QTpSGUYGx4kdjusP_dOC42WOlfpkGxHGD6RM4TrS_1npjVayssMabao3XDdQ1spZZV8XxlW-wal9dR3J5vnSPef-YS-dj2xy4eqZjqwxR8sGlnMLjcDlN7vScj_8_ZgzuVyo-o1z3EW4jkaQmPYpLxt6GSC_8QkWjVFknaXGAFUE5odBU9pPOzZ1V_brW33IL3qC-jq_l17E9LVsTtf5WZI-SRkU-n9xupboucy2Zhf0MW7v5fib-C5uI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=Jp2osxt1uzZkTe8waRoUO7lGr79kwUOiL1rgAtjr4I7WoFIATITSTOcWxo4FzsvedbJeY213YfzqLQ20fMyBGd4d9Z8jAPFxzaQe0qyJZbc1F6t2mh_RSF6nKNn-1q1kue8BvEXxO9JCJX6PY-qU3omsIG-4LMN7F_EptfPYcUpN6aA_0VvQS3BG6i0TCmV1KkCXAPXDo_n85xWA4H7LYT2shv2ZXyrsk3ZoP2qANHyCFOMP5Xfkf79mlgdHft8qpVjlzwOllVjpHUFMU_lg-lHWMlRkZZZSZ2WbfiFG88fpSoAWzQOt_obRObVTejN7dVBR5BWYRK0o4nSDYa22TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=Jp2osxt1uzZkTe8waRoUO7lGr79kwUOiL1rgAtjr4I7WoFIATITSTOcWxo4FzsvedbJeY213YfzqLQ20fMyBGd4d9Z8jAPFxzaQe0qyJZbc1F6t2mh_RSF6nKNn-1q1kue8BvEXxO9JCJX6PY-qU3omsIG-4LMN7F_EptfPYcUpN6aA_0VvQS3BG6i0TCmV1KkCXAPXDo_n85xWA4H7LYT2shv2ZXyrsk3ZoP2qANHyCFOMP5Xfkf79mlgdHft8qpVjlzwOllVjpHUFMU_lg-lHWMlRkZZZSZ2WbfiFG88fpSoAWzQOt_obRObVTejN7dVBR5BWYRK0o4nSDYa22TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcXl45Cq6wpAVBaIKLgmIlrQx313VnGqIM09CwLqoQxpf1KysOViqK8aBGBwvukZh39KgW_87OINdylbOxb_uJRFL0l0ZoI5h-OE4I5k58kPIzgr6FKRLc9kxLhW6Q0Vql8W2POYtzA5Z-RrqsIBfSa0HQjJMUzJyrzmJndwu4lyg6xtw7HrvUgOYSJBSC1quGUzd4PXvdQcLACy_wsl37HC_e0i7rdPfm41hG6hZ63TQYK3zYlaTxPs7izIzLfHtEpWBB_cFWu1Tgf229tjjDjlLI5EMLWCctwkQsArLVcDZ8Vt49aWzwAGFAxKMf3DWy6JeazhAS_1mrfHLRLRIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-J2YfaJFg-whMbAfWera9ATDgOJTbkc00iCFMr7N-4ZJEO-08-d_W_FH0UO4zgNV979qA9hzHpL2lwrgAGJdm6r-ma4n34fwrks7VFCyK7iUuYzQZbStiVnLsZh3cMD06DeMxWk0SfJYb8T38nP16J5X6yhN_xcaZrKSbS33DrbtdRn9npI6gXGb0OAC-yMd2Jn1Eh_AC-XLpRFvwrZFlWSjbxlARc163eJGdFoPNRujkQ1ZOcvkekhASqha2aOAm5byGUGeesqKv1SrpGasBis4XKdoniwYl9plwnN2M82nqo5nbzSP7feviXlv9IWaYGp510Y2x4kSyh3xfQ0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijpw50QVcQnAGLREgn4nCnckirnBAmTKQqxtb_pweoNuGNOIaF_lL9RhnH_oMRbJwcwdLI7pedVWPIGMgGmNTpWoFEawKSQKR43fiCgr12MkhbjUkOtQ3JDCwqZ2KLbRX-fVp93EL7JF7axM2aWgGmNqbpYnvFVU0rxx5AUtT6UNzySUcUTxQOJTKMBRcehBgcaP31IPcKeQV2JnjJmE04fZwzChfMmaStA_euiDldSDGg4I0yGMVQtNM0HP-LC3dsGU5n_Divr7QPQ6gxk8lOyxoTUI2zPxi1ogjbI3oXTNw-RJ8yr5hkR5WqZN23Z3jfK3OKXukUsLc5OAbMjKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0k2rSRY_Z3CmF0UE_ACh4dq8pS93uOKnv-zHHoqy_UR_AiJZ0LfQkt2QPBc2WcymHbsJBxetfj_pHofqPdb5rFPNbLGhDkaxYRkBXPwDTX0Ow1ppqjx4iPizYvrLrUtsnP2n53Fujm6RHJc2cDhsdTKJqXFqK4IwUOWa2h-Xbzi4YObVcKz4t8QBa3DTpcnXMyTvnNE9EMPdMT3j6dPICUFUWp92P91VLwGpvvjTM29vCL2JIiF3CzHs9eN6QRG7dciSpzNObdN4VgiP-g7enDbBAvgX5mNPh0ZRnxMnS-wM3uU_YDB0jR8BIdoalekc194f3UZ64TAe9IF_YGzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=mc3lLZYoZkf2i5ULOKklz0W0FWrGrkzHuwQ0m96k0-wnpKIaKPkytW2SUqZAb-UjPNytWxom4UmxNyM5Qq6jdjDPbIj54VMLNz4xO-Pr-xAOXQVGTtT9qqU-CUjUYlOlVK3Vy401HOdNK1EPAy28bPguD0xqCKNPxz_CeqFyTv2RXc42i9UvEExFwjHYokithVwsQlQIxZRzUruT3dp9yZwf6H5M21KEipRTuqtWyAVr6Q8NzLFQ2YsXiM6mbASRZg8SOcc_I2Pr3FgWApnBWqAboN3tnhzO0NgUpiFdqrjUyDI_O3QYvcxT5or-f_RcOBz396I5IbhXKf-JB06HZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=mc3lLZYoZkf2i5ULOKklz0W0FWrGrkzHuwQ0m96k0-wnpKIaKPkytW2SUqZAb-UjPNytWxom4UmxNyM5Qq6jdjDPbIj54VMLNz4xO-Pr-xAOXQVGTtT9qqU-CUjUYlOlVK3Vy401HOdNK1EPAy28bPguD0xqCKNPxz_CeqFyTv2RXc42i9UvEExFwjHYokithVwsQlQIxZRzUruT3dp9yZwf6H5M21KEipRTuqtWyAVr6Q8NzLFQ2YsXiM6mbASRZg8SOcc_I2Pr3FgWApnBWqAboN3tnhzO0NgUpiFdqrjUyDI_O3QYvcxT5or-f_RcOBz396I5IbhXKf-JB06HZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=p7I2JIGjaRY3L3L6t30JwWRXqkGwmfkek4l4WBtzLTWBKvDj-NB_XFefky2ooiob-AGTKChLpp4Wdabxtwz4MhJDXpYy8iDggDwA2AUMr9BP9VvTW2Ts1av3_Ne6r_6IqyCY0jCWh4_bucvLR-V73OzNywk9l8TO-UsR4tP_EGzthJdV0LS6rYYgID4yZTKuFe4zSn16HfEOQG9SNTk3jLU2u0ATK7H7u7tuF7e7raKksIgKqgtuIdZ0_ocSmLrzobmf4zrYc7ABJ2k5__Dv1HIrGSQIbvMXqMKrw3R2HCr4T_uEXSC2xs1Jb08agTv3n2IKiS8RIvOqvXz0f0XioQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=p7I2JIGjaRY3L3L6t30JwWRXqkGwmfkek4l4WBtzLTWBKvDj-NB_XFefky2ooiob-AGTKChLpp4Wdabxtwz4MhJDXpYy8iDggDwA2AUMr9BP9VvTW2Ts1av3_Ne6r_6IqyCY0jCWh4_bucvLR-V73OzNywk9l8TO-UsR4tP_EGzthJdV0LS6rYYgID4yZTKuFe4zSn16HfEOQG9SNTk3jLU2u0ATK7H7u7tuF7e7raKksIgKqgtuIdZ0_ocSmLrzobmf4zrYc7ABJ2k5__Dv1HIrGSQIbvMXqMKrw3R2HCr4T_uEXSC2xs1Jb08agTv3n2IKiS8RIvOqvXz0f0XioQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=jjWu7bDgEGglpARJJ6W9paTjf7ybHq4K53NQkY1diMEm0Vq72e3rlAX6Wa0mREZB3PR_hqkjjkE6kICd_i2w4beCuOP7Er3XlYPIe0o9i34qpq9jEjXwt-g5TuI2GvNPaU6gF6RVbs80pJ6AHMhZGMdOc_N-tHQYOkD5y5twxsh-f-P_--UpSHKs7ilzEYmK9VPri80sKMmdKyseclGkLrOO26ei1eaZ4ssiWDC5wTbdZc7iWyDCKCJj8L-Zi1MZQiNqaFXr1Ms_0ZH0s1sQ7kk9OVHdoaSO2EyIRhYRrAXuo0SQ9wpgV9niO9g7k8lB1d9zXNSX3rkHpxWGoQlb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=jjWu7bDgEGglpARJJ6W9paTjf7ybHq4K53NQkY1diMEm0Vq72e3rlAX6Wa0mREZB3PR_hqkjjkE6kICd_i2w4beCuOP7Er3XlYPIe0o9i34qpq9jEjXwt-g5TuI2GvNPaU6gF6RVbs80pJ6AHMhZGMdOc_N-tHQYOkD5y5twxsh-f-P_--UpSHKs7ilzEYmK9VPri80sKMmdKyseclGkLrOO26ei1eaZ4ssiWDC5wTbdZc7iWyDCKCJj8L-Zi1MZQiNqaFXr1Ms_0ZH0s1sQ7kk9OVHdoaSO2EyIRhYRrAXuo0SQ9wpgV9niO9g7k8lB1d9zXNSX3rkHpxWGoQlb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBhNaEu_S1SdC7qy6qP5hmmy-OFkpyHeT-y39LINfcXdem_SkTJ4UCI50eWiPDBdUx2F9ehkMU72ca-LwP9oyRvGkgncLAtjZU5scwByJpCRauWYK4hu5OZZwEZtuj5IwDvO7lkRdKCd4Dq92VKti_qUz8yeDvGGuMuMJfqzJQR25bpJL9LTlGnYP-eJ8cWjDP6ScnADoh3Aj-HRMPmEXk-7mGNVZB5DntD-oYomOja1gW0PMFfHwIfoFsk4SIiOAp9QRE-lnwEevPQ2xJyzbQ6JMFKEMa7YqzC_aPChjOVnsJ9a6IK_PbeC0WJTrwvif5QGUz8j1u8XHxSFtt98lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtlL6IcX8TRTvQp1gu_9CakoEZS_cLckAmGSZI9TslDyNUKdIc3m18zvGoEKN3c816U4XHNU0T4CH0iGq68iCEG1Mr9p9ZXcK9h0TXanObucjBZP4hGetRbsgxOrjQim4ktXfxszK5AqUaB8nht1ynRzWaciZ9adCgrj7prqwq8-0Bb0FtMoyiYitN34JRzkwE0L3xi3ByIdesmwmWmGQJdljyuuVJqSvDaNwndUQPKGlyR9yHKIfDkc-nxdYqshGnslHxHITz_v2ipY9NyBXUdJM42L9fYM7XKNoYurxBaazz4mFJdER9Q40XndBL02enYLq7dbAA5otEvyRwQTrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=rlYh8SF-8uZwz4YQIPQy_fYPFzUy0OB5bm4YH1Cu2FKuVB0GBfLc2cBzrXPpxXlfyiZinf79CpoqTi5m4ZV-PDU4Y8RBdluxQeXqsgKhFqqP4us0mNCkDheyBQAkLBcO-7AenruJi1SYosxbFQEnZYvTs9hee6XV0EStb-b9BXaSBGMjP-4qrBGjHKCB6DoAbzlcKmmTECA3fCLDl2fHNaSI6TNEAm4X5zaThQjU28tJSe3uznTmn7QhtHcDv6D9IIum-xC-_ga1qAY1vJEnr2VmcwaeuyXzsdRjjOUoXYVNIYHe9k0sIp7UzDUyS7nztDjYuXeLJomgqoHPO_MToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=rlYh8SF-8uZwz4YQIPQy_fYPFzUy0OB5bm4YH1Cu2FKuVB0GBfLc2cBzrXPpxXlfyiZinf79CpoqTi5m4ZV-PDU4Y8RBdluxQeXqsgKhFqqP4us0mNCkDheyBQAkLBcO-7AenruJi1SYosxbFQEnZYvTs9hee6XV0EStb-b9BXaSBGMjP-4qrBGjHKCB6DoAbzlcKmmTECA3fCLDl2fHNaSI6TNEAm4X5zaThQjU28tJSe3uznTmn7QhtHcDv6D9IIum-xC-_ga1qAY1vJEnr2VmcwaeuyXzsdRjjOUoXYVNIYHe9k0sIp7UzDUyS7nztDjYuXeLJomgqoHPO_MToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
