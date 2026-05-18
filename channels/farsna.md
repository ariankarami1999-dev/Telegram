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
<img src="https://cdn4.telesco.pe/file/Srx4A3R2-yP7fkCt3oks6v_x6h8FgJaxkfrNNZoQcFKyLUpMxFIPb9BHk7ra0FZSmSsPk2H8nHu7Ikd7p_wgTpYIdPHk7nEtLaKkOqPiwm8FeR5N5jIh62uYuMXLDIABDCKCmx_3svbrZS8pU3yGO9w8qNEtK1pG-4kuNADjoPAYLhEaBs4aqUWuFDwp5zBfyGvmbdG2H9aklRW6wEH5VN42EGXcxCBpeNcSn56b8kMmApf-2iZXaGXTW60TfjY19KiyvDl58WwOdq-FoCTVa7LCPvL6XSoVZarKYONQJokyow5WYA-ac_KLc0S4J-c94ob4aprqKdYKuLiuRzJV1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-436423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dd64fcd8.mp4?token=l9mwtd-AQGXNH52ClWALMgFvO4hAYnOIt-QPML8okfxxCPrIZwGlemvmnSc_CHlX3MbNpoat7MjBpJTBQ27a_p7WX9jEeMjfpbFlOxuZhh2L9DnKqKlU905ONA5Su9rIIbtwpioP4TFKiwaD5NqboX2k4D23_exJews9xUvKVvqb5H4ganrVoEIVoFR5_nHoj86Vm4PS65sgMG4SHCEVKhfddKDMc-6GbEbPrwH56wfQwvqApHzLEz_17Scjail5f-MN5LgI14DopCeo2o-OOZZQnoROQlMPjV5_XY7XXyKByvlCDqf_k-Gnr2jNonq8V8AoKDgYB4r4SbSa_X7PFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dd64fcd8.mp4?token=l9mwtd-AQGXNH52ClWALMgFvO4hAYnOIt-QPML8okfxxCPrIZwGlemvmnSc_CHlX3MbNpoat7MjBpJTBQ27a_p7WX9jEeMjfpbFlOxuZhh2L9DnKqKlU905ONA5Su9rIIbtwpioP4TFKiwaD5NqboX2k4D23_exJews9xUvKVvqb5H4ganrVoEIVoFR5_nHoj86Vm4PS65sgMG4SHCEVKhfddKDMc-6GbEbPrwH56wfQwvqApHzLEz_17Scjail5f-MN5LgI14DopCeo2o-OOZZQnoROQlMPjV5_XY7XXyKByvlCDqf_k-Gnr2jNonq8V8AoKDgYB4r4SbSa_X7PFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گندم به بازار سیاه رفت!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه…</div>
<div class="tg-footer">👁️ 598 · <a href="https://t.me/farsna/436423" target="_blank">📅 20:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
حزب‌الله: تمامی مواضع و محل‌های استقرار ارتش دشمن اسرائیلی در شهرک‌های «الخیام»، «الطیبه»، «دیر میماس» و در مناطق «خله راج»، «تله الحمامص» و «تله العویضه» با گلوله‌های توپخانه و شلیک موشک‌های سنگین هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/farsna/436422" target="_blank">📅 20:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a35eed28d.mp4?token=Yn5Oen-bujDbQyQfenKSZhQJga4lIRxH3ee0-wz3U5zjtWkwvI6bPEpzGLI5I4h7nPRzFr85Ad0UWJjTLsZOKa3FL89tX5kLIy5I3B_3H-aWXE1vXAPnZz2Ao4F2xeCP9Vjf3j0XCavp3zOIGG1fwVz3Psm2ggLCxVSHeAo009vI_jhOJvx7BqdhRa-8WiiXnp-ENkBpd-R3cWbV5Fi8xN6jd2LxtjIKkLFmj_-Ps0NRFsNbxt7q_3Vvyx59i8JeqXahdBBlH4ivuCHVzqmEZgGq3O6VS-nFBhs9EiGokL4IOawclygxsykPFJelA8eHZa4jtwtMlqn1ICM1LEazkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a35eed28d.mp4?token=Yn5Oen-bujDbQyQfenKSZhQJga4lIRxH3ee0-wz3U5zjtWkwvI6bPEpzGLI5I4h7nPRzFr85Ad0UWJjTLsZOKa3FL89tX5kLIy5I3B_3H-aWXE1vXAPnZz2Ao4F2xeCP9Vjf3j0XCavp3zOIGG1fwVz3Psm2ggLCxVSHeAo009vI_jhOJvx7BqdhRa-8WiiXnp-ENkBpd-R3cWbV5Fi8xN6jd2LxtjIKkLFmj_-Ps0NRFsNbxt7q_3Vvyx59i8JeqXahdBBlH4ivuCHVzqmEZgGq3O6VS-nFBhs9EiGokL4IOawclygxsykPFJelA8eHZa4jtwtMlqn1ICM1LEazkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مزار شهید امیرعبداللهیان در دومین سالگرد شهادتش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/farsna/436414" target="_blank">📅 19:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2a92833e.mp4?token=Kjzx5kXl1_9vumlXvHGZJZxynwibyXYq6yXCzoCi2Yw2rcckPqXlMDoC8IavsHgsIcZ9r3RLBaGbQxhwxtjSJ7YdLreF5ZC2fp8YxcLut13CdE6kwgooxVJ-eG9AABBwFLB6y19EbkwRbXB9C2WKHkh_vSolvwRkRxei5WoOQCZDOxrY02yH4iN3y271c3n3j5a0yPq40zihf3lQ-6gHLVh-tqygNMTzkMaqaWtKqqdfrEyZKFGoxMiYqU0OUf-upj3NicUW-eHGjISI873VHWIjNSznnVrOyjgcar5THGQ3fd6wfpcw1PfNe7B7tu7mnaaNiJbVUl7Fcj2dJCS83A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2a92833e.mp4?token=Kjzx5kXl1_9vumlXvHGZJZxynwibyXYq6yXCzoCi2Yw2rcckPqXlMDoC8IavsHgsIcZ9r3RLBaGbQxhwxtjSJ7YdLreF5ZC2fp8YxcLut13CdE6kwgooxVJ-eG9AABBwFLB6y19EbkwRbXB9C2WKHkh_vSolvwRkRxei5WoOQCZDOxrY02yH4iN3y271c3n3j5a0yPq40zihf3lQ-6gHLVh-tqygNMTzkMaqaWtKqqdfrEyZKFGoxMiYqU0OUf-upj3NicUW-eHGjISI873VHWIjNSznnVrOyjgcar5THGQ3fd6wfpcw1PfNe7B7tu7mnaaNiJbVUl7Fcj2dJCS83A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجهٔ آلمان: اقداماتی نظیر اعزام «ناوگروه کمک‌رسانی به غزه» را تأیید نمی‌کنیم
🔹
این کار خطرناک است. در گذشته نیز چنین ناوگروه‌های کمک‌رسانی حرکت کردند اما هیچ‌کدام نتوانستند به نوار غزه برسند.
@Farsna</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/farsna/436413" target="_blank">📅 19:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کشف ۵۳ سلاح غیرمجاز در اهواز
🔹
معاون دادستان اهواز: درپی اجرای طرح کشف سلاح از ابتدای اردیبهشت، ۵۳ سلاح غیرمجاز به‌همراه ۵۶۵ فشنگ کشف شده و در این رابطه افرادی دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/436412" target="_blank">📅 19:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
حزب‌الله: مقر تازه‌ایجادشدهٔ ارتش صهیونیستی را در شهرک «مارون‌الراس» با ۲ پهپاد انتحاری هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/farsna/436411" target="_blank">📅 19:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ATKYHGbUg5G_-4IXQ2c2Pm6KjkgdyHku5qeZGM79xqG4LtbYof_aOpTmWkvDPhp3pQEeQM2V-TQFhPesXjBg75fx7MKB1Uc6RHa4jOCpVcfZ4e95J7QZ7uv9HA_UPcth6uDsChiNZORj1KnNWDIpYDz-g0SjYSUCerx0yfGnmVXC1p2BttzLOqDrWXJPsbeDAhOW6mZ3ussFYlT38iH9DAKO-wFXSjRcVlKE7vmqibUxVQ2UGqPWN7Gc7ASToJgS01eKkB4Er4TS4KuDH-z7s9Hm9IeY05jgVqNg1PFYCSlm6590TF3YUGBhrKxl8L_PCmgsgK5srqJ5hHtVzg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کتاب یک» از امشب روی آنتن شبکه یک
🔹
برنامۀ تلویزیونی «کتاب یک» با محوریت معرفی و بررسی آثار مکتوب رهبر شهید انقلاب، حضرت آیت‌الله‌العظمی شهید خامنه‌ای (رضوان‌الله‌تعالی‌علیه)، از دوشنبه هرشب ساعت ۲۳ روی آنتن شبکه یک سیما می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/farsna/436410" target="_blank">📅 19:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee3bbf1fd.mp4?token=jUNn4EXKckEGe2xvluZNRuWjwYa8-DocWTFi6SoEIvme2gErxPFgewTQ93N5vpZAXRcOWLGZGo8pqNEXDYD9aCi91KTMasuxCFarXDFcFNN05WwzdSuoq8-Q2J1qh5aDqje625YadisEaXqnW_sZ1yKEoQbxMYvKsaIPDhqol261KQkIukMon9rFRJ23jqGKOk2jV_cX6Pl5iunOvBFNBqO2y4Z_YnvaZixPzvp82VWkzbRL8y8MZ13xy_v2QjePyLeC3yrhXJLBDNaYoKYtNF8RO77w9D_NUFQnhp1K7_j43Dw3hndqsZcI90R9JWZrybNgHDwehh_QFASX9eHrOi1gFVcdi0SCZGnb9k8RcdyB5WaDdYKCNSEoOJmyNC3v8F6HvqV-urk6hMA4P3xL5KBTNITqBG_DIIRiPLofbMJ0Y5_v7dEMlnrOLz3br2MWzIoFV_NDucTpokFAnOEEU0IPTkHLZpYPTzopNHKi3MZH_3YFdh8fekc0uU161oMQXFbj-tTB0D_uqLqwzXWdow4pn0MtDF5EIAyNib3a7wRacbw-5kmhw-rzutzMOn-4OoP-WbUYaFOxFK61SoigU9U1d9BlcJX7-QERevO8K2Fctzlg8b_o95Tjfkpa1CsrODqhTmSwaOx1VWIXXeiEuM-MoY_tElR3O_G-hHF56cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee3bbf1fd.mp4?token=jUNn4EXKckEGe2xvluZNRuWjwYa8-DocWTFi6SoEIvme2gErxPFgewTQ93N5vpZAXRcOWLGZGo8pqNEXDYD9aCi91KTMasuxCFarXDFcFNN05WwzdSuoq8-Q2J1qh5aDqje625YadisEaXqnW_sZ1yKEoQbxMYvKsaIPDhqol261KQkIukMon9rFRJ23jqGKOk2jV_cX6Pl5iunOvBFNBqO2y4Z_YnvaZixPzvp82VWkzbRL8y8MZ13xy_v2QjePyLeC3yrhXJLBDNaYoKYtNF8RO77w9D_NUFQnhp1K7_j43Dw3hndqsZcI90R9JWZrybNgHDwehh_QFASX9eHrOi1gFVcdi0SCZGnb9k8RcdyB5WaDdYKCNSEoOJmyNC3v8F6HvqV-urk6hMA4P3xL5KBTNITqBG_DIIRiPLofbMJ0Y5_v7dEMlnrOLz3br2MWzIoFV_NDucTpokFAnOEEU0IPTkHLZpYPTzopNHKi3MZH_3YFdh8fekc0uU161oMQXFbj-tTB0D_uqLqwzXWdow4pn0MtDF5EIAyNib3a7wRacbw-5kmhw-rzutzMOn-4OoP-WbUYaFOxFK61SoigU9U1d9BlcJX7-QERevO8K2Fctzlg8b_o95Tjfkpa1CsrODqhTmSwaOx1VWIXXeiEuM-MoY_tElR3O_G-hHF56cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این زوج‌ها زندگی مشترکشان را در میدان آغاز کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/436409" target="_blank">📅 19:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
حزب‌الله: خودروی فرمانده تیپ ۳۰۰ ارتش صهیونیستی در شهرک صهیونیست‌نشین «شومیرا» هدف حملهٔ پهپادی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/farsna/436408" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
حزب‌الله: خودروی فرمانده تیپ ۳۰۰ ارتش صهیونیستی در شهرک صهیونیست‌نشین «شومیرا» هدف حملهٔ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farsna/436407" target="_blank">📅 19:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIW613Jv-XBvDGea8RPtb3quSSdcWktHpe4yQzd-NsOwr3d79DY6UrmjTPYFpRvNmfHuO53CbisGDB7eb6pxIBEXGWC_arjqkT2RR3J270Cbf4oUyaEyGujabee9QDPLRDgfF5lmGCy8arrtPMtNhQfECO107beboHY_zhl1UAXNLwp0OPUPQlQqJkswhVvvpWNW4y7dwS0nZDs-xoeWWQyINYHySIpuKpJrdVcKAEcdfVy2CxnbSGw978fHOTnXGFtkJXrfRnFHE91DJK6vWkoZaz96uRzV9oMgG0NW-KugxjDb7VBcfN6mJnps3uCZC0Wl3xGRjPvta-YKC71XrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف غرب به توان مدیریت محاصرهٔ ایران
🔹
شرکت رهیابی محموله‌های دریایی، تنکرترکرز می‌گوید: وضعیت ذخیره‌سازی نفت ایران بحرانی به نظر نمی‌رسد.
🔹
شبکهٔ خبری بلومبرگ ساعاتی پیش با استناد به تصاویر ماهواره‌ای نوشت که نفتکش‌هایی که در جزیرهٔ خارگ پهلو گرفته‌اند به بالاترین تعداد از زمان محاصرهٔ آمریکا علیه بنادر ایران رسیده است.
🔹
این شرکت کمک‌کننده به آمریکا برای رهیابی محموله‌های نفتی ایران می‌گوید: این نادرست است، تعداد زیادی نفتکش در محدودهٔ محاصره وجود دارد اما تولید نفت خود را مدیریت کرده و ذخیره‌سازی‌هایی هم در خشکی انجام داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/436406" target="_blank">📅 19:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436401">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMemzuQXOLmeqaWOQIgS45Kl0-pL04KdSRz9JMwW8HN6k6H5KuIAJmxYzLf3LVSS1rCjjzyvsFTwYpfNZC3eDzrm-lUmzJ16d7RbdgD3aH7LJ5BqUffi--9gbCP9sJTTQ3ni0qzp5SH3ydP8VsewLktp1H3WlUbiHFNunhor4loPNFYRZBurvzhGCx5bPAF9YHG_HkKMM77jNl8u3k-wK9Z-H-hH-fqzXfuXvdvx5ns_eWEaRT-l88nIsa0QYfsCkfUMdkvO8b-rHU6a5oP3nqo1o0BV6IuRiaUDLj3sxizzzBDzQ7ZrMEk7apjHV0LPziIGZUMz-7Rn3o3qnQeUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBHdyrCfct0ypLVslWmDgU1inh96ka0ATd9_rwFUhg7nETq8t6RafroIZieWYi2un-oXhYC3OzJ1IpxUjScZK54OBrRxQQaWR2i45V8H5pOAWvfBIK7E6nPzkk4BfIOYiI8LZJ3JrdRFdXyRSc1sBuVC7VUPMWYQAgawWFz3fbSNglZSMBL9xgUkmeyCpUUbQe-gATgizv0QeKsBUZHka4ThIkrySMjp2ujMlSRQ6_hxqbLNrFXhopWwWxWxS-JIRzRX9ZVH5Uhrl_TU-SxPq5932LdqhmTI7Aelx3P8U45Jq2MeBcvKJujqN34BONqlYNXcl2p8QsuRt6XpIrvdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htK-oDcZ-joFvBfpp5pzy_SeYtD8PDPAC5hHjX6bZsxywkWKhNVvdyeWw69mazq6jgu1Li1r4SPWRMII5pDiSaKYgRjtIFGb2V8kAwSrlTG2NWyoPKfjoC9dMWEGZrevG8RCm52kMPvkDPs_VuRX83QLbCbFALd-WaOhkeM86Acx_pSQ2U_FXyKsRzdoHY5RVDK6OuAb2KuhjGNEaJI0UvzmpKpONknc_34bIPUShxi9XpU45eYN0AGgejsEifMt_jl5cua_74EAsK4IFw5s6h54oBNXJQWaYDO5mPQSslJozT-99BVzvBHHP83r6jcyC_x4pF6kSYNP1CnUPDq2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-BZQrS4Gjl5dFMZD1rCJdc6wQPwk8AXdql2g7zJe8y429DMf4GaTfheAswaUq_S-RLLC8pYZ4YDyYkqgKvln9t1Mk6CDI20qcngVDioO1eC5oj4-soOLFFaZ9Le1ktodoCmzeYge9JXT7Zqoyazenm_Fl3zFxP9xGTupwjLlKJabTB2KMFUHDSclemNnMGWV4sRJd1BB3F6_YTnEbUPmG4XZq5hq8SDjK6juTzgEo-o6lsojWcd_6s2jSqnbAyr-42SvsyUe-iTtSwCn5AmMJ_VY3DPuuo0WDYg9rGgx-Jkz3tlXnpYNFqO0TAtD23QjmTdKYDc4XIEPp8OaUuNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgDqPH8Mwl4im0vjrMUWLZqB-hsC6KSPaQAqYUfOjJCj3fC8TBgSTHsr7wHnVllQPPoxm2QiIQQmPADGcEmCb7GhdmQjUUK4KD9o4fTIcJmqA1KLJ-Bkt4W2ulFuJ_ynt17gBrRoFDs77ccnlRyTnUbaEBsBKbDDgap-dvvcF4ed4zPT6Qdi0X280tDAx1GvBztfO2G8QRWXY1vAIYKLlYJWpJsgr7WhkPDQyMyhtFErjit7OA8k7-ARCqyJruvITE1eX3RKvGrGkL3vnzrNYisZIf1MCXtEPOjR8q3PrtApVdQV1kLztJJZPzOhmy7dyYxiGRvpWPH8LbWyytYx9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادبود شهید علی لاریجانی در مسجد بلال صداوسیما
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/436401" target="_blank">📅 19:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436400">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1301cf2b27.mp4?token=R1paWqNpES2kighGd9hCDbHZfwF1UvdY43SAuwMK1RtSATbrZB8BY3HLc3Km5NU5yl9Fn66FA_hQPQlVRlIR-bU27YHuYgnM2mbBuQqjrJXnQfvMAUsbX8hM76cF5Ql6SC-v_s9GKmun9PBDNGUPChq-48YNjoeFM5uxlUAQ2wu0KIfkypr8Qa475l9jeQpZCBjvhZHmKHwIhSCVOS-xL1Wl2bBDw41FN6sOKZfv9tx9wMV88ZlsB8xxxz2R_J0Vac_3KM_VxcMeh4zNYu6KFWfuXQ0iX9KaP5xQqo1eUps5uwTtyl5kBd3hEAuS5_y8QDJTcuCTqfKb4641s8uPxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1301cf2b27.mp4?token=R1paWqNpES2kighGd9hCDbHZfwF1UvdY43SAuwMK1RtSATbrZB8BY3HLc3Km5NU5yl9Fn66FA_hQPQlVRlIR-bU27YHuYgnM2mbBuQqjrJXnQfvMAUsbX8hM76cF5Ql6SC-v_s9GKmun9PBDNGUPChq-48YNjoeFM5uxlUAQ2wu0KIfkypr8Qa475l9jeQpZCBjvhZHmKHwIhSCVOS-xL1Wl2bBDw41FN6sOKZfv9tx9wMV88ZlsB8xxxz2R_J0Vac_3KM_VxcMeh4zNYu6KFWfuXQ0iX9KaP5xQqo1eUps5uwTtyl5kBd3hEAuS5_y8QDJTcuCTqfKb4641s8uPxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار وزیر کشور پاکستان با عراقچی
@Farsna</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/436400" target="_blank">📅 19:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مخالفت AFC با درخواست فدراسیون فوتبال
🔹
کنفدراسیون فوتبال آسیا با درخواست فدراسیون فوتبال ایران برای تغییر مهلت معرفی ۳ نماینده ایران در آسیا مخالفت کرد.
🔹
ای‌اف‌سی هفته گذشته به فدراسیون فوتبال ایران اطلاع داده که تا ۱۰ خرداد فرصت دارد تا نمایندگان خود در…</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/436398" target="_blank">📅 18:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436396">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYmgZux_kTxWTQTY73Q9X-FuADu8dl9Oadtv5qZ2V06sAD3QMoDohRckaonSy_a7HQbzOhPBZ6ZSsS0VY5nvw1kp4ddW9s4Bk4VvHR1MGOdzHw5nEnYLKUbrENA4dDxhZQFqR4AH0z4ksCuDbEetVyppNCxTi-OBsXY6l5r0rUeZAQ-FgRRrqiGcnU4G9qLi-BEPillPfuCL_g8W6lp7dQ4IucfQykiCEJORH80g3kaT0x4LfXH46w_OjKTpNdMhmhvixGjDJzIiLrwGbT03vn75qPYqTn_5-ob_BHQdVWWU-H1gfMAqmgNaOduRjUw4LeucVbkDv41R1elHLN7m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: ادعای باقی‌ماندن قدرت موشکی ایران، خبر جعلی نیویورک‌تایمز است
🔸
خبرنگار: شما گزارش‌های مربوط به توانمندی موشکی و سکوهای پرتاب موشکی که باقی مانده‌اند را دیده‌اید؟
🔹
ترامپ: بله. فکر می‌کنم این‌ها اخبار جعلی نیویورک‌تایمز است. احتمالا ۸۰ درصد لانچرهای…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/436396" target="_blank">📅 18:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436395">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfgJvP7I6co12n1arYNJzKv2w0LmwFI2dMXzuWMWyJFnYp-CuzGdpi87xeO7crKV1QOEznog1JWDVH2TwjGsSCQOl_L6qfH22av5X2D8rZ7esQRo3PYHHiBEBjAi9fG8ODzLetvL4mvx_SdC46uGIZtMeNnYj2omK0Qtbq-laa6Qdhgg5AWZodc2Qu7J8Onkyhzjm5wnBiIno7QUoQz6QS4LS2xrFyhDyo7X43BrWbI-N_9dNJyHKGnhbh6PBMphguwod5hnzUNzE9twyL-H48-bj35InDYslDbCP9a2L90xc1eHvRhqDwalMwM765DYZ21DAE6Ar3iwdiLuT1sPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ باشگاه ایران در آستانهٔ کسب مجوز آسیایی
🔹
طبق اطلاع خبرنگار فارس، برای فصل آینده ۶ باشگاه لیگ برتری مجوز حرفه‌ای از کنفدراسیون فوتبال آسیا دریافت خواهند کرد.
🔹
به‌نظر می‌رسد استقلال، تراکتور، گل‌گهر سیرجان، چادرملوی اردکان و پرسپولیس از جمله باشگاه‌هایی هستند که مجوز حرفه‌ای دریافت می‌کنند؛ سپاهان نیز امکان دارد با تک‌ماده مجوز حرفه‌ای بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/436395" target="_blank">📅 18:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Df9svj10_LAsHGFwDOmWrXcjvEEgsyOZSBFngxe5ehXKjsOMQ0MWrYos-Gvwpdjn9hc4_hW1QnnYO62ODUEgJ8mdj9cQU2teQHgkhdN-cIdizj72xp6kqraqf1CitW7iP26xm09be5Yjt56R-dXBaM2izdgyTz6YntRQqn5vGko2RYdtzkofkFNk3hrObG0V75fxhVWrJ_0It2w-C5smHQRkabxjoJbJ4uHSGYmWgKwKW0G8TzKY5JNxwSqlD2tfVYFuBkCf01ZobyLWFR5ENzmYAtZ1wnEs1kq9-u5X-t9gFUOeX6IDKLaiKHTh_KAo6OoCf0arS0KeCceWsVcXDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTNB6HY2I_BPxVBIr3S-Tv2_9-q7_Eqw_Ss1rbiM5HJ7sY_uH7w8bvkw1Y9_KRArykkxds7w38Q7t2Dl5_HBevjKyeJcFXM2r_48VXNIBqel0TRZl5i4bZpwjpKkgYevXbhaopHBSP91gFtXN3XQxHP4r62UFbPz9UWAKH96IrIOV22UWbRgLnNkOVf64TJe2pVXkyUMQRdBs7FgI632A9v9G-haEabSb_0NCbiwA88ppQ9cke6IpeLe8WM_-HQHHBL8UTkiejHpgs6rnDb5MPdcvJbbp9tGu-vOuLK6xDbU6yxnMxQuyaCg5VMkqE20H7g64u0REqqzbBaHNa0Qqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rngslu2O9vgjXmwBO9haB66bbewtTGZigPLkDdX50-Jcv2Zm0HgaBADIZr81tqTF2iaL9-jg_pSA3tLRjetF6Bm8GQKBjJcTc90Y8w6rg7rsUDtlL7ybIRUxqIeA-tUur6Mf_dZkxgUteBx3lbyFpYI7GEtu0DHabY6yaZ2xXJ02l9a_2tdGbPTWqv_BTOpOkiPbomCsVOrf4BVFbAJ6O9ZGCVtPg7owvc4fiy07Kx7gz4V0aXt_gn2jfcOtu-sXeKmFxiZ7ZYXeFf9KHB86VdMF0SBZq5O_h1YHHv3XX0iE6T1DvT1MeabH91NMGV9-zZWAxR8oa22oOIJvQoKo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTWRcDjUSSTI15rmHT0fr3M5E4VroUsB4mh8d6y_oPFLjHXxpPiwDOAL_Ulvq7N1kFEEOHz17D1WIPvFTbyFqD9YNxu-kGzjUFmDtZjth4Ko92xtgToMsStv0OXeoen8QtoDHF4aV4STXjoluin1gLWMpDQxyOlgZHIwyBxvM--mxtv1D9pRB5-XbiABj96aDIEhubTpd2Civ6vfNBkUXNZKuqvyAvPVBZzJNWavfQXJKTWpCUwV-pEtpAUozn7OkfanuGpLPV4ZCQq0BNUYliJ70i6jI3gjy4rOOH-7NubW6ua1VDetKF6tQX3TEBxF5u98919XKPKJDckLIKV5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGIDxLrxAMlawFEMyZTwZ8Qkcrai-Cj5Y-Zb6CF4o9eF2wWE-Fu-uVeFb7fXme2oP2y5LVESb2Dg1B5RH_UYhtxB4t3tuWbo9ewiSlMpOAGT9Ri2ljazrTupk2QfqESYABdaq71tSe2QuUwCk6Lgh44ZnlHPpEmP12O_p9v2Fof6fsFV-bxpFwoa-u_Oas82tAW8Xkatv28IQj1_KOD_rZfW2T40PmhT1mx4uasM8B-YjK2gvrOIUXw6HUSh4QKteAaNSiD9bEGpkH_PCqfnX7XSeE2kyTFt-caJySftsP648pwDfbG0bPS8vKyB3laC_1IMPKuX_K4ZxYZPJakotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WApYYnrsFJXRBjklOBP5MD3H73ktBLJlS3LlOaq2F3gdN7kadWqL2gB4CkfxN2G-RmP9EsphjhC0LZBJqE6WGW-ZNkDvj2gXFVGpGnfxDuvznZ85LNJVWFVTGHte1XT5xqmeCY0FP5Oe-TW0WTWA7iZeufSshP8fw50MgQV-d1UTz2f96PyByZ_ribrejatnHA4Mj3gb9fw9Qp5b5zKQLzdHhFWq67dx3CH-t72-DUsekjX9KnvDYIv9-egmNvFzJ2tWuV0ngelh_OKHm7ieryhCcnU3ac0rKTAa2Iwt3kgBLBMLlYrzNMtobjSCgjzdSC7DJCbJqLxLTueVassRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSk5zAj1P6Yh16xkspQ68VhaYO6tOWi0uKoyVCPGVUedhMx8cC2iTgQRmCD2LDIJ_YloKH7TRGMx0n6yhCByX0GRPYAPNwmwjbd4t7ViTlEkXpZoyV0-CtIVj7Em6eCHtAkg-wqeT0znr6exqAM-H0i2h9aOyMIQC40lhUYrRyOcGhLFVM6phUOWUa4FRDxjpjKD7G1f0ddht6hT8Yt2D9sblsZFTxaTUesl9dvHjwSeyEX5r6GSL1A-8sarZzBUf6aKypfuqBY4UnADMzIs7z2SmP7xnwV7upPHMTmt4DpMPanqlr47fp1zcFTB-YYjAK1hcD9MU5l-ka7Qt_7gSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: در مقابل دشمن سرخم نخواهیم کرد
🔹
من به‌عنوان یک انسان به‌عنوان یک مسئول به هیچ وجه در مقابل هیچ قدرتی سر هم نخواهد کرد و عزت و سربلندی کشورمان را قربانی راحت طلبی و دنیای خودمان نخواهیم کرد.
🔹
کسی که جلودار است باید صادقانه با جامعه‌اش، با مردمش…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/436388" target="_blank">📅 18:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادعای عربستان دربارهٔ حمله پهپادی از عراق
🔹
وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شدند.
🔹
عربستان گفته حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند.  @Farsna …</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/436387" target="_blank">📅 18:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436383">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8I-beKAXwOv42BgmQVYxzxC4e1WxbuovwOlFcgBfKibON0PANrxyV1po-mtJLj60UWFMAkDKAwGC5tQSBx_OC9LNXLxRyU3Nf4B9wGjoeqpb4KzeaCWLAeMmkXah-kJMAlz4GgY9jmVWHEK5xl470fwi2wJ17k6pjyXEQs6T3G-GqMQOWG09SHF7cKPuky-_lY40b_fYNhPGEUcK6o7b8WoIClfGSXU2mDATfAvvQ_nUCJc6-xSCBnQOyp-8DTYEr_jjGoqEataLz1NvN-eK0wUGMwOXsUs067le8dX6fvcOpyIem1EvN72njtynSv3PKZbUTpa0D-vLLs82soCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ علنی پرسپولیس سر سهیمه آسیایی
🔹
‼️
شایعات از احتمال لغو ادامه لیگ برتر و معرفی مستقیم نمایندگان ایران به آسیا حکایت دارد. باشگاه پرسپولیس با این اقدام مخالفت کرده و آن را غیرمنصفانه و غیرفوتبالی خوانده است.
🎙
یکی از مسئولان ارشد باشگاه پرسپولیس گفت:
🗣
ما به‌هیچ‌عنوان این وضعیت را قبول نداریم، چرا که هنوز حتی ۷۵ درصد مسابقات هم برگزار نشده و جدول فعلی نمی‌تواند ملاک نهایی برای معرفی نمایندگان ایران باشد.
🗣️
ما هنوز ۸ بازی دیگر پیش رو داریم که فقط دو مسابقه آن مقابل استقلال و تراکتور است و سایر بازی‌ها مقابل تیم‌های پایین جدول برگزار می‌شود. طبیعتاً این شانس را داریم که با کسب نتایج مناسب، جایگاهمان را در جدول تغییر بدهیم و حتی به صدر برسیم.
🗣️
از طرف دیگر تیمی مثل استقلال چند مسابقه سخت با تیم‌های بالای جدول دارد و طبیعی است اگر لیگ ادامه پیدا کند، احتمال لغزش این تیم‌ در امتیازگیری وجود دارد و شرایط جدول قطعاً تغییر خواهد کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/436383" target="_blank">📅 17:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je3Nz3WV3I7bYzpbLOyqnJ8GL9Jl2sJuhSzC_Ql85P4W5lxmHNpGd3Ym2r25_1BvGcz9heddWjuTbnS2z8V0gNE2865ueJHXEWe_5bRu4y27zmUFHoPFVUfg9H86QffO83zD3Jv_6M8qJSOAQe1UspzsfgVovlwRHeN4irCOtKWzeM2iV03sBXpf1LzWvdl3-v1V72-8iXrwJl3NxficyhACUi6pqOcqJLp-XG9C3BZNzdZj-AATWITtiH9KVsxrF2upAk_nKxsNqdLDRCtOWqyerdHfIm1wx0xHsHXgWBfUA73Br243ObsLJ4qqRiwxQ9SvAvAUpKmR4TusAvYS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KoXPn-KbtSHCeOAAD5H1hXj2N7uFEUurrnD901aFme8E8HuEjtVvhq4E74eonkkXwxXEKvv5iTrVjaLgoHq5rUc0IfZUPLzPOPlno7zC3EBvIkiNHp9NRo-2LAU8JxDV-jhwALTrUgy1PBxxhv0lPnV-Op8jRKty0vfTBaQ9AUsCVJrF9M034cZcuD1Pus3o_849JYEuynf-l7ErwAmWEi5ElAuqNRFlq_tnJswoxof2BQLvmb1LMrEEkhDIjaV7X6EKzR9TQG3fqC8YYTQyXwmSNJK8rSejtPI2hBJSlySqINGWWqtVbMlMyJmy2R6SQmsM0yF9JBL0U4-lfGGieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEeoRcL-AXnAdwu9y1sossY2mHE3_8fDfpFDIS3-J9Of6TL80z43YnzqcwwECseDCtLVIjstkLi5EXmhbKsRGHTwxD0Ybt2IdtZvJODkxNOgHn0efozPC7cnzOBZh_zkNtSQ6_I2mDe_IaxD72TVeykCYl88LLy1-vjlfA_U64a8aqDrn5Zvkw-djulknnKQ82qj29HoOiX5LBZ1zoXPE3wNlObjhfqfUtgNfkVt_7mxjElyWeB8FziNmhd1vm822xFpoNbt5DBUFQiVGNssZ2lzHMfdwl0iMKchNrHKVEKkcoTzKmEoGCUjv9AVE1LpjLpJJOgSHI3IOCTMyyApXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hI8D9YA1C7W3oij-7qr7JyrXlbI-9bAO4FYM9yGqi73Iqh_YN7s8yNolyI7r8WG8FPySYoK2SB0mz9IPZ4rKj6FgJrtm00LzgeOtSMbP2k1QoVJrcPy1CM1oqxmllSKwD45t1H0LQ_RRJErhgcrArdpn5pjv12JGzCqjW_pKb0PclEqefNvWsH99lQevj5ywK0anmzMaxamsgh0QU5wB2HqLtUJbQ5Rv-sR1IBgac1P1Ptt3f5yeP9ag9adN4iDUDw58wx9gRPJLhfXHGAMINxPGufMFZdoFxDUJEByjYf9sZ0KC91NaVrdd8NVxSCVFzoDSlfxazBxWxq0T3nEJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0Zl4-EVSD5W3iKRLFZV74wmxIRzMCfRvvs5hfK1IiVQWErm_g_VEgywXhy2QD32PrE47CZWQz7yaZ0ax1cBo9ertvg0ob9cdDdhFKrDL1BQJ8jXF592OZtXwxEwtIPZzIEwYWTOLzw6oARVStFUDqSLCsbnvSMXl6nN7EzVkzL0o02ZFCt_au02Sx71zk-diavC2NMfzbTH4Lxn7aEuGvlBXK2PbIfvXaqdN4vwHZVkvaAb3wVF6cnZy3x2eZJpRV1x-yNDLF2zhSnoPX7SxW4M_8t7CC0B3J3QG6RcArSZOa8GlFmo3OIcbxUlplM6RaFIvJTdVAM5QymsYpgDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMGjg8WhZoZhdip2NFoKssbtENXOj1yD9SWD_13No-YfxhkUN66v0mIBl6Uc1PN6uY2thOp5tHzWjD04RiOsGAYCoqRagqkVd_Qx4bwPRT8qZyz7PFe4o4DxL0wyNInGphZhnDfBrPgvm3BuZ2DUz7bCknDwwRU7Z_tCc6Lju6PW5fmoTQdd0nDSa-P04tPW3hkz1p9jxzvDQknpoe3Y48RqsN32o6ahxf7T7L4J-chwQFwh-pb9JkLrEVWb0emCVythl82MWNGtZIZ61LryVTZS4VON2d5kPBf-OE78L7DgCumGl8P3fXlzvG3I_dtk0HPK9MxROFePq-90exQUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQYWU6xURfelnc2XYnvyV6ld2JwbKbgrjxLgPEDXehZeT1sSDDUfH6b5TmC87dwHu01dkprUDB9U63PMcYI6oACVKPGZtnD3rV-MA_lkrh2PdZnXnkSTdC72rCQkr0rYgMmDR-qrhkcagRQHVFOqTXYwXNpezOdp7TfMkXUxf6r5v4OqNYVdxejpkH77uHb5YeDs7mBempDgP89d1O-xfEPjUB9Ylt_L12DIti-1bmi0XZaEInOH8gqc1F_QohbRAMtiyCK95nu-AwARhy9oZQH8Nm6Dow3oZIwjiR3UO3NcPO0b1RofyaYiQSCy5cvLQfmoToZBgGle-_dLISeVzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تمدن ۶۳ هزار ساله خرم‌آباد در قاب موزه
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/436376" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb138f5f9.mp4?token=I6hvMOORls_pFRM5Gg3NyjiVdaK5-CPSr3rBtm64kS-dYNbHB1EwKqnUGaVoFkOqV1KfhSg1HZyt0nChszDfxPTk6gwobvWBawe7tQuEMiLjivTZ597xdwWHEM357XSbCZ1SDFkCKN16wzfW_D-5SAli9Q90sSLdfxjAVoTXAbS5W1Ph-YbpFwSzvldHNIHhIX_zo3-DoY-3Tn81bYEy-Qf1qlsNkwJymRmgO3BmwK78NesO5OmuUCc4ItGn8qwkwNJmJfB8rxB8h3dPgP4KvIDRT2s6Sl8GP_f3H2DNHM2RbCyrHQh3ba4qVVAvWcKhihrnxshUXMNSRYvqvT-PEkAJ8JPQLjYJrfT8b5uww5DQ5KHYbwkOk_zrDZIlN7e_OWxffu7nxsJItyIeu0z9nk5P5hsZmN7ncyXtpKEreKaQr5J89mI_loGy4bCO8g8rGkz3R08XJe9k_toR9cjm2krKRu498Ckz9gDtiM8RyaXFZMZNPa1DYP3o33yUfxzmoINdGOe9S-3av6bvQsnQTdGHTRNW66js3NHPxMonLGbBWKqQN0sxORuBhl4_OsqgrfWi3USX4zEiKRLR0UhrF9paMNKO_c7OICvkhF_FG52ATJ0rZp-bJqr8OprvAP-QMJuiJG5CTG7oMwnEkDB9Umef3DqQdqUjdjYwHKhmNvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb138f5f9.mp4?token=I6hvMOORls_pFRM5Gg3NyjiVdaK5-CPSr3rBtm64kS-dYNbHB1EwKqnUGaVoFkOqV1KfhSg1HZyt0nChszDfxPTk6gwobvWBawe7tQuEMiLjivTZ597xdwWHEM357XSbCZ1SDFkCKN16wzfW_D-5SAli9Q90sSLdfxjAVoTXAbS5W1Ph-YbpFwSzvldHNIHhIX_zo3-DoY-3Tn81bYEy-Qf1qlsNkwJymRmgO3BmwK78NesO5OmuUCc4ItGn8qwkwNJmJfB8rxB8h3dPgP4KvIDRT2s6Sl8GP_f3H2DNHM2RbCyrHQh3ba4qVVAvWcKhihrnxshUXMNSRYvqvT-PEkAJ8JPQLjYJrfT8b5uww5DQ5KHYbwkOk_zrDZIlN7e_OWxffu7nxsJItyIeu0z9nk5P5hsZmN7ncyXtpKEreKaQr5J89mI_loGy4bCO8g8rGkz3R08XJe9k_toR9cjm2krKRu498Ckz9gDtiM8RyaXFZMZNPa1DYP3o33yUfxzmoINdGOe9S-3av6bvQsnQTdGHTRNW66js3NHPxMonLGbBWKqQN0sxORuBhl4_OsqgrfWi3USX4zEiKRLR0UhrF9paMNKO_c7OICvkhF_FG52ATJ0rZp-bJqr8OprvAP-QMJuiJG5CTG7oMwnEkDB9Umef3DqQdqUjdjYwHKhmNvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ بیهودۀ ترامپ با ایران به روایت رئیس سابق سیا
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/436375" target="_blank">📅 17:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک کشتی ایرانی دیگر خط محاصرهٔ آمریکا را شکست
🔹
یک نفتکش ایرانی تحت تحریم‌های آمریکا که ۲ هفتهٔ پیش در سواحل هند بود حالا در جزیرهٔ خارگ پهلو گرفته است.
🔹
این نفتکش حامل ال‌پی‌جی بدون اینکه شناسایی شود از خط محاصرهٔ آمریکا گذشته و وارد آب‌های ایران شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436374" target="_blank">📅 17:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPfluk8emtv_fVsJXjAzIqay9NFXRjMstH7Zkm69x0rD_CkooZ-IonFLKVa80RVmKikamSdBqwmjKyBlFp4eEhW339-aysfWWhxN6V5UdmOLSrn1b4DZWAuT8Wa3RsjdOk5YgX90_VRUzU52vq6TZdULBNNjadibhOeG3_XongVsb5GN321ZTs23W3xsYlGlSeW-0R__FbnjhBRDyk5XOB6ICYawM4pRz7mGIaBTzJRVxVEP364WcWvVvoQaS-RVRwWoDgEIeJoSoIaC5uU4NCiUYY1xTFyxHhPzOh5N_z1J0zKad5too2MVeTbd3fyPpqRaVO1XyF0EQDJl1VZaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانات رهبر شهید انقلاب در مراسم قرائت خطبه عقد
🔸
ازدواج و تشکیل خانواده یک نعمت الهی است و باید شکر آن را به‌جا آورد.
🔸
توصیۀ من به همه عروس‌ها و دامادها این است که با یکدیگر با صمیمیت رفتار کنند.
🔸
محبت، وفاداری و همکاری زن و شوهر شکر نعمت ازدواج است.
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/436373" target="_blank">📅 17:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfaqjZYZWvF8qqO2aVvLkdasSbjw3gkrbAUAcPBZR_p-WxHPDmL-qW4GHD1QyF8z0b8UDLhJfbSJKzdnq_pNzthjrm1TytVUlVaFnuX4IZn9yKPVbaxQ-cm6xYpiWdCaQmffJiJXQWlQufGS7tR-drllZOMGdRBuQ8ExsjeX7G86w0OSm8S55mJvL1U7EY3VAsL8GIitk0SpozVuGeBnaJQfoL7jMkz3gGr86V1mahi_qGWopJ3C9CnsGHU1i68sYGe6EC6uOo7XwgrEeNunBX_HciWoPEfLFpQ5xhlHuCiqt2BuS9ULYcYeXvXtwYNe9z5Btb-tfEi5WfVGulo3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حساب رسمی مدیریت آبراههٔ خلیج فارس در شبکهٔ ایکس راه‌اندازی شد
@Farsna</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/436372" target="_blank">📅 16:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e90bbc20.mp4?token=I4JsvOZsVf6NoAAcboKR8nY5s0fCz1Bf6F8Yh41MKW3-ci59eFnyeP8FjUvF9YRx--NRGY9eg1IAHX61z7sX8XMtpSLw61x_p8Z29WXO6ruXyNFL5FzvOXQPrOzD88YTaCC54rRxBwXSYEV_84aBjiS0ofQEL4DcFplcJqnSTKcyu4UUYOmBsMuXLHBhkLilGleBv11cdS93Ms1lQXAxW8dpM_2se9Fvj94vdT3ys_XSg45cCSsXLhWzAJFxxxtsmba0Dw10GeGuL-Yu6GkN9KDfT1b0lT2G5kYKLo0_aswzvylsNQQqBvKXpgB60_CNyQntzjEUugPdNZ88ckcWBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e90bbc20.mp4?token=I4JsvOZsVf6NoAAcboKR8nY5s0fCz1Bf6F8Yh41MKW3-ci59eFnyeP8FjUvF9YRx--NRGY9eg1IAHX61z7sX8XMtpSLw61x_p8Z29WXO6ruXyNFL5FzvOXQPrOzD88YTaCC54rRxBwXSYEV_84aBjiS0ofQEL4DcFplcJqnSTKcyu4UUYOmBsMuXLHBhkLilGleBv11cdS93Ms1lQXAxW8dpM_2se9Fvj94vdT3ys_XSg45cCSsXLhWzAJFxxxtsmba0Dw10GeGuL-Yu6GkN9KDfT1b0lT2G5kYKLo0_aswzvylsNQQqBvKXpgB60_CNyQntzjEUugPdNZ88ckcWBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقامیری دانشمند فیزیک هسته‌ای: از تسلط رهبر شهید انقلاب به مسائل هسته‌ای خشکم زد!
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436371" target="_blank">📅 16:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ جنگ رمضان در قم
🔹
سپاه قم: تا ساعت ۱۷:۳۰ امروز عملیات انهدام مهمات جنگ رمضان اجرا می‌شود؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436370" target="_blank">📅 16:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuqivJiDts25ROqqX_u3-eMVAvUPUXOvYgHOouOHOyHEJYk8Vkf6J1UvU_swJHurqC2IU2rcofawo17NoiX0bPvz4Cm8o21BOwU8-3WZpMKJybViIjnTNjwBFi8bMf9YwqeWF5WTQPt_17jEbdV2-4GJqGeLqGK107zAtzSOC4Gs0wd_c92MLlVm_TW-UmdvIikcQWm3Gj9GHbPZeZAjeValVEZ1NmQtWff2jvtB_zrW9HK6szd_l-H6cE_4_PATPVGPHI6_WVBANSfSiGuZqawm1bz_X75Tsosv-G4abNL9LTYOC2YzYBlo-K-VlZOW-2LVL-XiDop_ppkKmp2BFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای هفتمین بار از آغاز آتش‌بس با همتای عربستانی گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/436369" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBEFQN6_lrbY6T6gKh4nzULTxShEfQEDRyVnw03Vfnz50F4tPe_2wFYcm2JSitTQed0Bse_5lbfkJnEcs0Q2VEPK8itlwR5XkQ00r3i-ry6LlXxrfnAzG4MRXJEWM6plfmio5dLwnSjDbh-BaLHep6A2poLdFKla1nOxfrtQjIY0WDNPDxTFf2F-Ox_dxLN3HYH__kKiK1XrFmEQd7rJIymt7edlKpySSqjf5g69w6Ng63K51PkUQbeertkYolAJyusu2LL52AYCsyCuYgsIYoc6eLFcaHjEfVVHE3zw6tHFT_yaKGkr2W1agh_nKjVcji6j2Zk_B2fSzlyMk7VTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نماز را در ۱۰ روز اول ذی‌الحجه یعنی از امشب بخوانید تا در ثواب حاجیان شریک شوید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436368" target="_blank">📅 16:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ ۴۲ نماد بورسی فردا بسته خواهند ماند
🔹
معاون سازمان بورس: شرکت‌هایی که در جنگ آسیب دیده‌اند فردا نمادشان بسته خواهد بود.
🔹
در مجموع، حدود ۴۲ نماد اصلی بازار فردا بسته خواهند ماند که چیزی حدود ۳۵ تا ۳۶ درصد ارزش بازار را شامل می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/436367" target="_blank">📅 16:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
رئیس بورس: بازار سهام با دامنۀ نوسان ۳ درصدی بازگشایی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/436364" target="_blank">📅 16:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjXQcT6FuiXU0UXweDSpWYjqxUiSZlPSD1CBogh_pZyfeVNcT-mFk-jhUJf8lrhVgX04nuSDLxcogCcoEZDA5awKajFVaQTo1LskoJ8nC6qTqU1BM64WvoqbrTjNDMz4c_QBHw1EiXc-d2sq5gOV2P5DwJ16eKi6yHLoj6z3sHFDOoJmaKLHvhYUHMWFSHz05TmGggRyVbel4yjFwFUfX53cxqe6Mtd_K3EVJo8Jztx7uBEjv-YxBP-4xRohWivDg-JHxbMQS0_F3ur2WUjX6y5VrpkYEKu0m-NrBCXMcQ9lyUcdu3eWDPhbIQR65ti2i7d_xxTnlzJd9oYTCtegcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان هنوز به ۱۱۵ زائر ایرانی روادید نداده است
🔹
یک هفته دیگر مناسک حج آغاز می‌شود اما رئیس سازمان حج می‌گوید: هنوز ۱۱۵ نفر از زائران حج کشورمان اعزام نشده‌اند.
🔹
باوجود گذشت ۲ روز از پایان عملیات انتقال زائران، سازمان حج می‌گوید «طرف سعودی قول مساعد داده است، اما تا صدور روادید باید صبر کرد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/436363" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436362">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705cc3ad13.mp4?token=TYOIGf3H6qARnq1-tCMzrSxUPrCtmvheWfcdJ6abj2SfI3achHpuXRbQ-NuBctwpat68nx8I3V4ktesjuGHF90tdKgtZ-gZCAp1KPFc4BiTM-01XcrrrSlLVIwKQPeAZWu8KmHvu2hNW2si4waxdzTtU_3FgOGuGE_n-eodysb_YQbvQaCmYgyJj_WITDhDGCr1H3BRjwUtj3VYH7jzW9tmA6nJ_sQwD70IvTERkHtST2JzvHzpergKAQBjXtamVKYU25zV_IKwRZsqomhbvXWfkK9QwpAU0rG2EaKf7M8sdZYgV5hHOPaaBmGmku36_CaIh53-rNOSYbSLeXpDDIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705cc3ad13.mp4?token=TYOIGf3H6qARnq1-tCMzrSxUPrCtmvheWfcdJ6abj2SfI3achHpuXRbQ-NuBctwpat68nx8I3V4ktesjuGHF90tdKgtZ-gZCAp1KPFc4BiTM-01XcrrrSlLVIwKQPeAZWu8KmHvu2hNW2si4waxdzTtU_3FgOGuGE_n-eodysb_YQbvQaCmYgyJj_WITDhDGCr1H3BRjwUtj3VYH7jzW9tmA6nJ_sQwD70IvTERkHtST2JzvHzpergKAQBjXtamVKYU25zV_IKwRZsqomhbvXWfkK9QwpAU0rG2EaKf7M8sdZYgV5hHOPaaBmGmku36_CaIh53-rNOSYbSLeXpDDIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مدیری که می‌ترسد نباید مدیریت کند
🔹
کسانی که تنها در زمان امن و امان حضور دارند، بود و نبودشان دیگر فرقی نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/436362" target="_blank">📅 16:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436361">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
گوشه‌هایی از زندگی شهید علی لاریجانی
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/436361" target="_blank">📅 16:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436360">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حملۀ تروریستی گروهک پژاک به یک معدن در سقز
🔹
حوالی ساعت یک بامداد امروز گروهک تروریستی پژاک با ۳ خودرو به معدن میرگه نقشینه در سقز حمله کرد.
🔹
تروریست‌ها ابتدا دست‌وپای هردو نگهبان معدن را بستند و تلفن همراه آن‌ها را خاموش کردند، سپس اقدام به آتش‌زدن تجهیزات معدن کردند.
🔹
براساس گزارش اولیه، یک لودر، یک بولدوزر و ۴ کانکس شامل امکانات رفاهی، ابزارآلات، وسایل تعمیرات، قطعات یدکی ماشین‌آلات و موتور برق دچار خسارت شدند.
🔹
چند بیل مکانیکی و خودروی سنگین نیز مورد هجوم این گروهک تروریستی قرار گرفتند. هدف تروریست‌ها باج‌گیری به وسیله گروگان‌گیری نگهبانان بوده است.
🔸
گروهک‌های تروریستی و ضدانقلاب با هدف جلوگیری از توسعۀ اقتصادی و اشتغال‌زایی در مناطق مرزی، زیرساخت‌های حیاتی را هدف قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/436360" target="_blank">📅 15:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIRBrsr9nJ_qe-q85LmlBn8XfUM-xnhjdIjwvm5Sv5_48oWcSV4bc0cOLF1nNA6tUUiHEaLVkVrySFYAYCyEn1hAXsn0oBCtFDp7CgjogHT_xq4DFp4Yc9uwpTPnjZ2HIur6VW8jkOR3jl6AOUqk8ZUbrTf_jT9v8SUXWuyazic8yRwtO_ye_l5ist-_6zZemaQSsIiqL-KlFiTbz3Xc7DSc6tWtetfYCpUvqSOVntcayawHW9wciWOe3uyeKhCt0E5WiotgW4YuNLr4juJIu7azFyJ4pbmHg7EHC3MFlxorHPCDZ8Tu1UJdU9Mc4tfHHUmfMaIRRW6-ZeXFgz05_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدارهای حملهٔ هوایی بر اثر حملهٔ موشکی حزب‌الله در شمال فلسطین اشغالی فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436359" target="_blank">📅 15:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqg11QB3wMiLnuv4hDbVYpQVFZnjB9h1VdWbNyoQhiJgLgWL0pWYAOPgCr4AqozYzNFSuWMAp_CDc80bZy8D5NRY1LbrijVWFJGJ5uRpGY5dui5u_c2Tskb1PXOjxihgo1C3XNkt_KpukSGScHEy-ujSV8nmMNJc-A0P9RZNjQXO-xr9snWfNAzHfEqxjf0zu11AoRkEsPwPEPKPND-aGQiWzUzGWH57h1A0UGGMVE1yGCjsYQrtcaWTpCOKfUwyeY6MXfoW-Dj179yk2yEoMKO-ovcO1hSO1j71ZwvEE6F5xgkZgOBALySHR1HHMNXfEXkscrrhv6b0rg2opB4UFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: خیام تجسم عینی تلاقی علم و اندیشه جهانی با ادب ایرانی است
🔹
پیام رئیس‌جمهور به‌مناسبت روز بزرگداشت حکیم خیام: حکیم خیام نیشابوری، تجسم شکوهمند تلاقی علم جهانی و ادب ایرانی است.
🔹
خیام با طراحی تقویم جلالی، دقیق‌ترین گاه‌شماری جهان را به بشریت هدیه داد. روز بزرگداشت خیام، روز پاسداشت خردورزی، پژوهش علمی و آزاداندیشی است.
🔹
امید است نسل امروز با الگوپذیری از خیام، در مسیر تولید علم و پاسداشت فرهنگ ایران گام بردارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/436358" target="_blank">📅 15:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460271a4e2.mp4?token=qU4akgTzdk5HP47c3PT2W5A8ges0ulwprsH_WEdup_yhNL5s_ywcUtBmksC880-i1t8VtgrB2fJgenAQ0DJMQc9Q0Kw99K0jSlzYHtEsNsPW4--9_yjuQ4kpd_k-z_MIio-pXHZTzvU4PJuQjMguEipJxNW60-ee3fgEBVbVHmflXNMmrE9-vrIJkn8_S-UG3TvIQ9Fjxpfs-h85DC6YLMonB3HqY5UnIeMFgLiKlaVJ039f1h27r_iisd5cU6bvz1OzB1RqQXeuqTYc1xk32tvjNMFrTBwpTgx3NQ86TZQkBtKfDmEW77WnXb3ntp0SkZ3BSXwVnKRIQ_oHom6ldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460271a4e2.mp4?token=qU4akgTzdk5HP47c3PT2W5A8ges0ulwprsH_WEdup_yhNL5s_ywcUtBmksC880-i1t8VtgrB2fJgenAQ0DJMQc9Q0Kw99K0jSlzYHtEsNsPW4--9_yjuQ4kpd_k-z_MIio-pXHZTzvU4PJuQjMguEipJxNW60-ee3fgEBVbVHmflXNMmrE9-vrIJkn8_S-UG3TvIQ9Fjxpfs-h85DC6YLMonB3HqY5UnIeMFgLiKlaVJ039f1h27r_iisd5cU6bvz1OzB1RqQXeuqTYc1xk32tvjNMFrTBwpTgx3NQ86TZQkBtKfDmEW77WnXb3ntp0SkZ3BSXwVnKRIQ_oHom6ldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گشت‌وگذار پلنگ جوان ایرانی در طارم قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/436357" target="_blank">📅 15:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436355">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb65ec73aa.mp4?token=fj7cVafxeQCk1exEBde2TIPo63t4SA8oJ4aSo1Hp-Nn6mLKbGFW59nfmSURCBvvmnU9eHJhrnijkW2ZSKQcV2oRQ-IFJKtlml__ze1Uaognpx44mecW15H-PF8J-6XWRB0YgaXTfT7hEe3zDxq6kNGd8S3fRpF9u82Nh0-X9pBbItxev3ZLcRmf19UVXVCg27WX4K8JPptABZRmxUntv_Zw_aBXVM6tvnpb8sJjKXqRbbgsnkkwHnqjtTr18JjHHaiByz1GO6ZF_tMBg1paRuziZhRcGNtv8y500lmuoXjS8QQ7vch4VLvQdFjEQq4oMNAGrRq2f5hEZHHAsdvix0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb65ec73aa.mp4?token=fj7cVafxeQCk1exEBde2TIPo63t4SA8oJ4aSo1Hp-Nn6mLKbGFW59nfmSURCBvvmnU9eHJhrnijkW2ZSKQcV2oRQ-IFJKtlml__ze1Uaognpx44mecW15H-PF8J-6XWRB0YgaXTfT7hEe3zDxq6kNGd8S3fRpF9u82Nh0-X9pBbItxev3ZLcRmf19UVXVCg27WX4K8JPptABZRmxUntv_Zw_aBXVM6tvnpb8sJjKXqRbbgsnkkwHnqjtTr18JjHHaiByz1GO6ZF_tMBg1paRuziZhRcGNtv8y500lmuoXjS8QQ7vch4VLvQdFjEQq4oMNAGrRq2f5hEZHHAsdvix0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قهرمان کویتی از روی اسرائیل رد شد
🔹
جاسم الحاتم، قهرمان جوجیتسوی کویت، در اقدامی برخلاف رویکرد دولت این کشور در حمایت از مردم فلسطین، در سکوی مسابقات جهانی ابوظبی از دست‌دادن و قرارگرفتن در کنار ورزشکار رژیم صهیونیستی خودداری کرد.
🔹
او در پاسخ به این اقدام خود گفت: ما نه‌تنها با آن‌ها بازی نمی‌کنیم و به‌صورت آن‌ها نگاه نمی‌کنیم، بلکه ما به‌عنوان مردم کویت اصلا آن‌ها را به‌رسمیت نمی‌شناسیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/436355" target="_blank">📅 15:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436354">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حزب‌الله: یک سکوی گنبد آهنین، یک دستگاه ارتباطی، یک بولدوزر و تجمعی از خودروها و نظامیان ارتش صهیونیستی را در جنوب لبنان مورد اصابت قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/436354" target="_blank">📅 15:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye1fhPQgtXvd86p9WxIRX3AEuA2l05j9Oj77GShDl6iFXlBB2kdsYpR9V07KSZYP331KTsyCEWjvGkGbLcT2mfLwlm3XL4015XjQuOI6dF5xJKHtprVCzVjOkBGSQEM_M49QzwCqdpRMefUmAQznyu0pSrG9B4RhpjOnQzTr8sJYBE0AqepELqIa_XZsLGD946qdNE3Eu2DzfS-g40EFHa3ZdTFia3ISbjTr0D9KTvQNxBvhXvuWrHAviqgxtdueINHui2m9CikmEY5_jsKSjPjTxoHHDByzmJq2oKBs0bK6ap9D6cNMqzr77X38zztMZAknCUpGmsmU0IGUbV08eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای سبز ایران قفل اروپا را شکست
🔹
اتحادیهٔ اروپا پس از ماه‌ها مذاکرهٔ فنی و سیاسی، محدودیت‌های وارداتی پستهٔ ایران را لغو کرد.
🔹
این محدودیت‌ها از سال ۲۰۱۹ به‌دلیل ادعای وجود باقی‌ماندهٔ سموم و آفلاتوکسین اعمال شده بود و باعث افزایش هزینه‌های صادرات و کاهش قابل‌توجه فروش پستهٔ ایران به بازار اروپا شد.
🔹
به‌گفتهٔ معاون امور باغبانی وزارت جهاد کشاورزی، این تصمیم می‌تواند زمینهٔ بازگشت گستردهٔ پستهٔ ایران به بازار اروپا را فراهم کند.
🔹
برآوردها نشان می‌دهد صادرات پستهٔ ایران در سال جاری به ۲۵۰ هزار تن برسد و ارزآوری آن از ۱.۸ میلیارد دلار فراتر رود.
🔹
همچنین بازار چندصد میلیون یورویی پستهٔ اروپا دوباره در اختیار تولیدکنندگان ایرانی، به‌ویژه باغداران کرمان و رفسنجان، قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/436353" target="_blank">📅 15:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f0b356f82.mp4?token=j-FtuTrwx41mp_bZfL4U8W2Nld__DJvKbialampF_y9lfBr_D2PCC9moCZDf9PkykyIis4DylRd_2Y1-YspBi_24fm8fsvbOnHzxxL78lcw72iyYyXTOzT8E-N3xIIFf78KAWaCbhxbn99h6GWUtOsYu6j2AxpbxjkI2tQ4pk28xy39XWC-P__DGaF0zPY8cRJ4lQxsd4rIZk4Tm69aNgUgBNqHaJSPe9YyzeaUn3lg-6LGgMPWeUXem9B3pLFsrTtqWCbkXMy8FyocbiQT3UIPdSFBxC1l-AK_mpoUkf8YZErbRdsShBS_6cqPvvys7d_etJ46gI1WNZHUh3_CeLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f0b356f82.mp4?token=j-FtuTrwx41mp_bZfL4U8W2Nld__DJvKbialampF_y9lfBr_D2PCC9moCZDf9PkykyIis4DylRd_2Y1-YspBi_24fm8fsvbOnHzxxL78lcw72iyYyXTOzT8E-N3xIIFf78KAWaCbhxbn99h6GWUtOsYu6j2AxpbxjkI2tQ4pk28xy39XWC-P__DGaF0zPY8cRJ4lQxsd4rIZk4Tm69aNgUgBNqHaJSPe9YyzeaUn3lg-6LGgMPWeUXem9B3pLFsrTtqWCbkXMy8FyocbiQT3UIPdSFBxC1l-AK_mpoUkf8YZErbRdsShBS_6cqPvvys7d_etJ46gI1WNZHUh3_CeLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: وزرا و کارشناسان ما شبانه‌روز سرکارند
🔹
از هر صدایی که بخواهد تفرقه ایجاد کند بپرهیزیم اما واقعیت‌ها را هم ببینیم.
🔹
این‌گونه نیست ما صدمه ندیده باشیم، این‌گونه نیست که دولت امکاناتی داشته باشد و خوابش برده باشد اما مردم در مشکل باشند.
🔹
برای عزت…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/436352" target="_blank">📅 14:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr1bG-sES53PyVGrLXKNvV-vGb-Qli5D2LK6lcuhUPlb9hf-KFAT9N3jYbh8Fhhve_UXecS-05I7wwnAK_E-zbNYBdMstQl_JZ-oxcj9KwR9KhQ6Apu_AHq2SPwdLHHhJqkwVxh2GAtblrSpQDSIaTm18N90l8nf3TFCAPfT3t47-I8RZoRNAEZVbV0TFuFfswHGAmqdzrHkB0QVfYjyukO2LqIbIL1QT7f6d8HBcGS_cdxxEbwwDbnWAqbAiA3hErKNId7U2uxCSnwmswfwc_ZyvYdb0RCVxPtEa8IbSKs89i3GKCAKeKacG_yAGld3z3xBcG0Hde5DLqKA92NYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ روسیه: ایران حق غنی‌سازی صلح‌آمیز را دارد
🔹
مسئله نیروگاه هسته‌ای بوشهر فقط به روسیه و ایران مربوط می‌شود و هیچ طرف دیگری به آن مربوط نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/436351" target="_blank">📅 14:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFhr1CmZJJpKqX6oZtzeuq_H0OdaIsMuWAG5rhMVAfCJ83uJrDv3ETt4SDGLuGooywRuHlQlAH_-A6jzcyZ_P3asUexXabFz7a6zs2C729mbtOY-HWJNb9WGWsa7i72Eu4EBCXLvxCGo4u8N40RrQDSFn6rLaROO6q1Da7FQhkj6kfjIN2o1wGp_Lhc3ZAwLBGqxGVlNCzj1PfWjeooJT_PeydiDJt5_HQdhOC8P3dVqDF90PfclAoRy-bslWyjUFHWjC31Rm_UUyzESx5xmP1Vnw8dSGhugKa9-7wQ0DC5QB-mfCff8z6U5eG59uCXNPOvRSIt6ayZ6cYcLeaMYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آسیب‌دیدن کابل‌های فیبرنوری در تنگهٔ هرمز، چه تاثیری بر روی اینترنت جهانی خواهد گذاشت؟  @Farsna</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/436350" target="_blank">📅 14:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63673ef16.mp4?token=OQyeUg4fYAq_Kq86VWMh3L6-24GakUtlYS53RswdYvBjfmJScDOQDvwpIeWbHYjXXYWqsKZQCcpCdRRy3ZAcZrWV43QH8apoOOlvD5KQwtCI1w8mECl2SBysBsmhs0YlRhwzgfRarbtEfn2TfrocOKTHr37VXbezCbikXowJMRwFAcoqHBCdm-yRG_JRJ91-T_oCMIh3Hj7X2K89VKFZoeWi2xcQUpIg1URmcrtAN3LNmsjcs4QMu5-kF63VWLW9bH6PECPQZZVrVbIjgDJMewVMNjJ9aOVqu7ljFlDhVtnt8fVdmYUn97t9H8oI54NQaE53aPnumVnLc72Sra8bow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63673ef16.mp4?token=OQyeUg4fYAq_Kq86VWMh3L6-24GakUtlYS53RswdYvBjfmJScDOQDvwpIeWbHYjXXYWqsKZQCcpCdRRy3ZAcZrWV43QH8apoOOlvD5KQwtCI1w8mECl2SBysBsmhs0YlRhwzgfRarbtEfn2TfrocOKTHr37VXbezCbikXowJMRwFAcoqHBCdm-yRG_JRJ91-T_oCMIh3Hj7X2K89VKFZoeWi2xcQUpIg1URmcrtAN3LNmsjcs4QMu5-kF63VWLW9bH6PECPQZZVrVbIjgDJMewVMNjJ9aOVqu7ljFlDhVtnt8fVdmYUn97t9H8oI54NQaE53aPnumVnLc72Sra8bow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: وزرا و کارشناسان ما شبانه‌روز سرکارند
🔹
از هر صدایی که بخواهد تفرقه ایجاد کند بپرهیزیم اما واقعیت‌ها را هم ببینیم.
🔹
این‌گونه نیست ما صدمه ندیده باشیم، این‌گونه نیست که دولت امکاناتی داشته باشد و خوابش برده باشد اما مردم در مشکل باشند.
🔹
برای عزت و سربلندی کشورمان حاضریم تا جایی که ممکن است فداکاری کنیم و باکی هم از شهادت نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/436349" target="_blank">📅 14:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPB2OV75DDLad2F0O4prikd-3ACNRL05yfajCizEXmwkQ1awshmA1gAPQbymx23QsJscmTP062MttwDIudwHPwXui19Bm-PDxcOlRnVt7skw34ZkH6NvSDfPu2YqnMG2-Y8dbO2hm8By2brtIlTiy8uPxinBlA4h17qphJLmLWoDIo0f5bLP4u3rS_2n_ij1w6PTMbopJTWU-oNLfD17L1J81_ox-a387RX0klqPCJNrTTTlZcidg70tn5h4ZvfufRBLQ4KTx_ngpk4MCWUzXkOJRjyipIL2wdg0kok3Dm-BohWY8GqVtB0LjnuTUXVXufdcKRTjz_scHjuYIE1hvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-kfmjEIEDqRs93SqObGlN56mmKsUXgA5h_Mu4LjzX6B6OXmC2NzoAPQ6bb5inhWYTgWrH3dvS99aqz0t8SldG3bWudvb9KhzjpUGYfdHaRcaTybr8R0hUmHU8SbZqR7M05-2hHd24B758ExWvm5bG6GBJWfuZ2ULbhter925g2ib-ReI8nWeU6RFa1FodQi9fkRDtW_BdipxksgkNvVvitH1LwLLRmoYzE2LZbucLysNjvSMPrNyJ8GIJaPNAyQz9qUN6fUMmHpHofnFKJ4HGbOYBgN99SsJo2pIzd1_As3u2RUK6UZB4dy4QNbnjyRk8fd2fJAI2fTmcA2Yflwgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSWHnMb2M2S15Hb0ocYym7bb4VqmBm-lOx-_j52146hqjqz_qBxhFnJC6U-jRxKl2_0JGDW5E34aXs6KLnl8-qsmFXsUMwtAuA1wrZhKHhrgBUaRwEHikHG5HkL6-Ewkke_HusBqjB7HkD-C-W223v3dEIZb3CDOzKamlOJDj4J9NbCLDQ8WQA1DDBKIHeZ_K7RSWICN5G03XsfG2nhKjLs6-OgXkfmN64PK8FUZHlIU885slZZ52T5sc0KbJcvzXs6x-J5r2OABSMhKDrxPLuTEaqR8xW4HoVfUGc9miqO8AIGBmtf5l3sXdnBCDGEIW9sF_vdjuSuiwbOqsAeItA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دستگیری زن و شوهر طلادزد
🔹
فرماندهی انتظامی تهران بزرگ از دستگیری زوج سارق حرفه‌ای که در ایام جنگ به یک خانه دستبرد زده بودند خبر داد و اعلام کرد: بیش از ۲ کیلوگرم طلای سرقت‌شده از این زن و شوهر کشف و ضبط شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/436346" target="_blank">📅 14:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دستگیری عوامل وابسته به محور آمریکایی-صهیونی در ۳ استان
🔹
طی اقدامات سازمان اطلاعات سپاه در استان‌های قزوین، کرمان و چهارمحال‌و‌بختیاری تعدادی از عناصر وابسته به محور آمریکایی-صهیونی که قصد تولید ناامنی یا اخلال در نظام اقتصادی کشور را داشتند، دستگیر شدند.
قزوین:
🔹
دستگیری ۲ جاسوس وابسته به رژیم صهیونیستی
🔹
انهدام یک شبکهٔ توزیع سلاح‌‌های جنگی و کشف مقادیری سلاح و مهمات
🔹
کشف ۱۴۰۰ تن مواد اولیهٔ پتروشیمی احتکاری در یکی از واحدهای صنعتی
کرمان:
🔹
دستگیری ۸ تن از عوامل اصلی اقدامات تروریستی در سطح استان
چهارمحال‌وبختیاری:
🔹
دستگیری ۲۲ عنصر در قالب چند شبکهٔ وابسته به گروهک‌های ضدانقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/436345" target="_blank">📅 14:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe985ac16.mp4?token=iK05zNOZPk-FvFMeLivmGbydeyZpZVhKZ95l7jfs42GmCPNh5tiOzndTR2R6bjX0U5MBGYa-mE_OIfkyigLN-1pcUQpLojluC9IzPHv5FukL0ADqbqCDCVc22ox6H3uoUuw0k0Lwp689Z6a3edUoFm-08RxxikJuzy9xqbGvN2s7LRfZ3chuccSGNvPLPPgde1X6jhmIClYYES5fe4TWtVRLrjukJV7ZIvokDcCgVRN8_guLxgp0DzhzCkQzf-r-CmWl96ghw-1IqX3mnuXaL9HlmK4i99pB2HB9x2r1M4wbmwndakbkDeBAQkt48qs9CJApJyQnTHZkUfet_96g5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe985ac16.mp4?token=iK05zNOZPk-FvFMeLivmGbydeyZpZVhKZ95l7jfs42GmCPNh5tiOzndTR2R6bjX0U5MBGYa-mE_OIfkyigLN-1pcUQpLojluC9IzPHv5FukL0ADqbqCDCVc22ox6H3uoUuw0k0Lwp689Z6a3edUoFm-08RxxikJuzy9xqbGvN2s7LRfZ3chuccSGNvPLPPgde1X6jhmIClYYES5fe4TWtVRLrjukJV7ZIvokDcCgVRN8_guLxgp0DzhzCkQzf-r-CmWl96ghw-1IqX3mnuXaL9HlmK4i99pB2HB9x2r1M4wbmwndakbkDeBAQkt48qs9CJApJyQnTHZkUfet_96g5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تانک‌های ارتش صهیونی با مخفی‌شدن هم از حملات حزب‌الله در امان نیستند
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/436344" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7655843800.mp4?token=EEG2h-_GPYlx8cIDR_aHFw3rwgXQ6mc_PwqYx6RFQd9bqjlTWWoyILW0BWnNSP0CFI2yACm-XwgM1a6IpSvNb_2XqWfhqXiJjI9_wLjB_sOvQyQ983jZps8C-nn2Lnf-azMknsOAUaLD7tmMJvIeiieDBTX5LTtUnAjWQY1pnU2qWwNf-vgDpZnYsaDTdxdR-MEkOmpE-Q4iw2UFM-KIAkHzTSJvlqw7TMQDoyD5GKqU8zLLdRWiG7OFnVH3kBdRmDTXO26e1C2rOTS820tAaE3LQ9Jmck9loiDZNpkVIcqjjcBN86COgpaeUcDXaIRy_EuGPvRUMbE8p22BVlUOMAHdVyyMxSocIRO9Kd5vtJFQJRb3UuVFZYHkEgd18Zvc5qQ_V2SMajLuaPrKldg3CPbPLCW9gX5kOGIcQDRxJZQ_dWGEbnsJt7eN0mHPzjjqwmA1f3TCqlM70HUcQXkUAv4_OVEOFPikmYBO9HZ_KX7TZi8xlc2MUBIjddGwAehFWNwtm3wVase9EpxQksZ68uBNOU6FFtg2QsSfTaZVp8ddGtB2o4tphXF5mLUjfcx-fgA_MT8gwa5mjEBYnYUP_gdMKDSMxdeNcmiPL6S_b8IcCgOw2owZpJ-OoxDV3ljvLYkuJB1LCuHGObJl4yn1vRwN5lbIlK8Ct-W-19U3tuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7655843800.mp4?token=EEG2h-_GPYlx8cIDR_aHFw3rwgXQ6mc_PwqYx6RFQd9bqjlTWWoyILW0BWnNSP0CFI2yACm-XwgM1a6IpSvNb_2XqWfhqXiJjI9_wLjB_sOvQyQ983jZps8C-nn2Lnf-azMknsOAUaLD7tmMJvIeiieDBTX5LTtUnAjWQY1pnU2qWwNf-vgDpZnYsaDTdxdR-MEkOmpE-Q4iw2UFM-KIAkHzTSJvlqw7TMQDoyD5GKqU8zLLdRWiG7OFnVH3kBdRmDTXO26e1C2rOTS820tAaE3LQ9Jmck9loiDZNpkVIcqjjcBN86COgpaeUcDXaIRy_EuGPvRUMbE8p22BVlUOMAHdVyyMxSocIRO9Kd5vtJFQJRb3UuVFZYHkEgd18Zvc5qQ_V2SMajLuaPrKldg3CPbPLCW9gX5kOGIcQDRxJZQ_dWGEbnsJt7eN0mHPzjjqwmA1f3TCqlM70HUcQXkUAv4_OVEOFPikmYBO9HZ_KX7TZi8xlc2MUBIjddGwAehFWNwtm3wVase9EpxQksZ68uBNOU6FFtg2QsSfTaZVp8ddGtB2o4tphXF5mLUjfcx-fgA_MT8gwa5mjEBYnYUP_gdMKDSMxdeNcmiPL6S_b8IcCgOw2owZpJ-OoxDV3ljvLYkuJB1LCuHGObJl4yn1vRwN5lbIlK8Ct-W-19U3tuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک با اسلحه در برنامۀ زندۀ تلویزیون!  @Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/436343" target="_blank">📅 14:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436342">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMth4kxrh8uuvvJ8jw3J8USHNBgjTkOY16h2Q1ZnZNYdxA55al8Itp-k6tvqW0dBWOHDZoihvDwlKYN-sbERNC1-7_3EEnwYDiuhEL7Em0Ie7YXvDvxLdCSetX0mgf_3-Auu1FukjJuX0QLnKMz27FpNWLaetHt2sBIzHRb19YABP6tIAbafPIjPRf5c5UkpXNFraDjpMSjSJFvIMfPI5IHDezTYxq1UXgVXN7BYf5ZnJ5Ds5TO-N7Em0WM9PxC5lM7Mf4pfJ7hvbxRo8vEXNMJ0ewSHmNutE4mX6sggKv6Am5SNiBvc4ohhSHD_VQyQG8vAsqkSGpfNSo9v7ykrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌ها پای کار بورس آمدند
🔹
براساس اطلاعات رسیده به خبرنگار فارس، سهامداران حقیقی بورس می‌توانند بدون چک و سفته، با توثیق سهام خود تا سقف ۲۰۰ میلیون تومان وام ۲۴ ماهه با نرخ ۲۳ درصد دریافت کنند.
🔹
این تصمیم پس از افت نقدشوندگی بازار و افزایش نگرانی سهامداران دارای اعتبار اتخاذ شد؛ در این طرح باید ارزش پرتفوی ۲ برابر مقدار وام درخواستی (تاسقف ۲۰۰ میلیون تومان) باشد.
🔹
بانک‌های صادرات، ملت، تجارت، رفاه و پست‌بانک از جمله بانک‌هایی هستند که قرار است فرآیند پرداخت این تسهیلات را پس از ثبت‌نام متقاضیان در سامانهٔ دارا انجام دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/436342" target="_blank">📅 14:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436341">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxLGex5X458UVC8eelzc1IhR485lZ9y2XnwyuHq3HcJRNu14FLFH8Ptd5bvI_lrwI6GrwFNc0ZM9x_7FQm2U7ZqrkZ3O-LZodD1Q19Qvfh7AKHxcDTz0hPbLWkqwHalIZuOTxmp-1-YIYCXhsWM0pmguiV-6ftLzrF1ZQzTjQncKoQiFy5cDI8bGtXkIwKZK249231efC8-5IXsCRHs1D8a6J1CTp15EP0EbYYM2hYDpDo2FP2igg8wxIxceGushR3GkBkj8bWhZqgWI4nJ0tf0EKYj3pIFNpq-w-LygoavlHGLTAQKX68cKGAZYKUcDVQXHlx6AKOmKOThSIscNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
گرامیداشت دومین سالگرد شهادت امیرعبداللهیان
🔹
زمان: دوشنبه ۲۸ اردیبهشت، ساعت ۱۶
🔹
مکان: تهران، سالن سوره حوزه هنری
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/436341" target="_blank">📅 13:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmZff9dJkTkIlRCZpQsaVMZVrYYhf5Qz_zTrw6kUKuH2qtcJVl92uuZyyUnvNbPwERGk8-SdEvZDTnsF8IS220iQ74qOs1KZ2rxTTf-fvKByYwIjp8O6qPuzJD9HjqLV3RSUhXFQmCuneVxDv3rHCPOdcNs6crglh9NlBp5qfy0F02DQflfd6UfcdEELYtRGAhQijG8ye2jSfTj9tjULidXATlUE5XD9PwE14bWIbcxrrQuRTuY2vZZA6IyoC01wT3zd7gjwJEql5S8c1Vrd3uxegekE4Ovb-WZHKe6RT-_FcrRD1yQwErTPI3cQdXHhVPEaXNK0QOaOrWYKxf2Evg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5RWvVE3Pm-G-TQ6Otpw16FpDCVoJR7LG1kL5Ilyw4EX_aHYayNeHuYznUL8FSfqIta-IoZ2NmWC81yr5sLDxDIbHIh5SpUORnxCvvcPMws2_JLMvt8FP33PJ8ALOa7HHp3UZ4P4_Px2GImm66G2tViLXNd-tFVJM9rvo0HGfcS7h0_Z0V1cR7Lulob4jr135RLO8QEJ13OSALVNmOmHyvdJhgDIfqBnP1ipZq08oaHoWG0VmtSAMTy_L_EGSwBLy6tpVEbTcvkhUvfVgfQz-EzclPQy_pdUgVtf7tY-M5z3lpHzZBgPkSB7nL2_vURLmXWdnOSJuaEEZMBBldtnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmbGVR5U2orokqcwyjWXK1Ur7-oQkfzj2DxjiDlk748Vdg6_h2F2x17KRVWFFwA6pJJvymlJCEjcqv3dHqeXPsaLXxHMtuk90TlaTZr76TEz37VhkOPl1pXEvk1zCt4orQaHGvDRXlMWKfCV0T1pyhSMy8ioby-LZPYXEGLRdyKcQ_2fosigXa6gp-nZp6TDk7kUK-IucPI534MvzOeGRh4r_A8GPYQjc3smuCt380KB-qBbjnvA04YUEIoembyGgvAr_-sUR4lh9cdhGLwDg8Oh1hZouY66voFLwH2Wgqh8FO8fNiQ1pXe1X6BFk30Q3aj2LrPcGxLvuhUIc9psig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ضربه سپاه به گروهک‌های تروریستی ضد‌انقلاب در شمال عراق
🔹
قرارگاه حمزه سیدالشهدا(ع): گروهک‌های تروریستی ضد‌انقلاب مستقر در شمال عراق به‌نیابت از آمریکا و رژیم صهیونی قصد انتقال محمولهٔ بزرگ از سلاح و مهمات آکبند آمریکایی به داخل کشور را داشتند و در استان کردستان مورد ضربه قرار گرفتند و مقدار زیادی سلاح و مهمات کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/436338" target="_blank">📅 13:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e997a2b245.mp4?token=ftWOX4atMEfO4KD6tzOxmCE-yFwEq31VItMP3fyqGHfZYd3BarNPHSpZ55ODfI90ZvHnVi3OqPMObYA0mU5HaT76V9oFtfYWOXbBA4MqPevscnUBvC75c70fO0NDgarymvL_PN723TmQURjypGHJrQE6D8J9bk1YnQVwhAeMqXlwLuJYpfD-aAHb4aXSzlm9nNgvxArMqg-ZGEbQ2e-nVcVXONtQCIvhp6N6l3wToIHyAm_JLJtYuuss6lpckKZyyb8LdbgMRZj2ji13d0r-RCdp4brE3XxUH50p0HkD8qvKV1rS99xCHc-VpgCE8WDjeCBKYlJf5GmglCWQCLf4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e997a2b245.mp4?token=ftWOX4atMEfO4KD6tzOxmCE-yFwEq31VItMP3fyqGHfZYd3BarNPHSpZ55ODfI90ZvHnVi3OqPMObYA0mU5HaT76V9oFtfYWOXbBA4MqPevscnUBvC75c70fO0NDgarymvL_PN723TmQURjypGHJrQE6D8J9bk1YnQVwhAeMqXlwLuJYpfD-aAHb4aXSzlm9nNgvxArMqg-ZGEbQ2e-nVcVXONtQCIvhp6N6l3wToIHyAm_JLJtYuuss6lpckKZyyb8LdbgMRZj2ji13d0r-RCdp4brE3XxUH50p0HkD8qvKV1rS99xCHc-VpgCE8WDjeCBKYlJf5GmglCWQCLf4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم گنبد حرم امام حسین نو شد
🔹
هر سال پس از محرم و صفر، پرچم سیاه عزا از گنبد امام حسین(ع) پایین و پرچم سرخ جایگزین آن می‌شد اما امسال یک ماه پیش از محرم، پرچم حرم با پرچمی نو درست شبیه همان قبلی تعویض شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/436337" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c851ff707.mp4?token=tYGtQMmnbHc0W10QGeA06PaxTsHzGock_gZEDQvuM6ZGEjyhO6f34YlhLRdMPUDv-WOH1G5XPwhpmCFy4MKbh0nMeNy5N0Lq9M91yNxvgrvUFT9bT8UBg45ePU6Xn5H8UyqGMd9EaGqU9DsmisZRJfIPB_AvbAy-J5fhYX3FEekXnAJXXk2pXB1dShoeTTO-soJ64Qo8ew0hDVJVRkfjohPJyazHYE5UAlfNERWwEr3CtX4zrHFVoAYgAe1tHqtC-sh-whRtFp-AcwfmDKSQ74N3SudBJ4HspC3aknw4eeYTTDPnybuIqLCyFsrFMRKqwsiYoiRq-DXi88mgrM8aLaZX4BH-hJRw7GiN5hgpS3397U9aIhISzDHhg4nU_FkfE2IJ9hpNAsNMNtaGADf3SeLvmrlAdhVrWIXlCC-n-yprt256zhWfScT7ijAVpNi_e-tG0J0RzvFhVAnrKZ0md7u3CMrrskoynHAk-aQvbvM5mS9z1hF_A1zNo9Enr2kyzJSJ3R_iqKLdilv-dTYNyHU1Rp9iLpYyfeANcArsm-M_uM62T0XIB7GVdQaCdRumL-UD2DBa60n11M3nvS8fGM_08Ehha2hgpT57VGh4JGtkrw-X14q4_6RU3zu0FRYA-F6zD2D0_a-1xDAmxBbEXhe0GPBo6dGQlsUPadx1Mmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c851ff707.mp4?token=tYGtQMmnbHc0W10QGeA06PaxTsHzGock_gZEDQvuM6ZGEjyhO6f34YlhLRdMPUDv-WOH1G5XPwhpmCFy4MKbh0nMeNy5N0Lq9M91yNxvgrvUFT9bT8UBg45ePU6Xn5H8UyqGMd9EaGqU9DsmisZRJfIPB_AvbAy-J5fhYX3FEekXnAJXXk2pXB1dShoeTTO-soJ64Qo8ew0hDVJVRkfjohPJyazHYE5UAlfNERWwEr3CtX4zrHFVoAYgAe1tHqtC-sh-whRtFp-AcwfmDKSQ74N3SudBJ4HspC3aknw4eeYTTDPnybuIqLCyFsrFMRKqwsiYoiRq-DXi88mgrM8aLaZX4BH-hJRw7GiN5hgpS3397U9aIhISzDHhg4nU_FkfE2IJ9hpNAsNMNtaGADf3SeLvmrlAdhVrWIXlCC-n-yprt256zhWfScT7ijAVpNi_e-tG0J0RzvFhVAnrKZ0md7u3CMrrskoynHAk-aQvbvM5mS9z1hF_A1zNo9Enr2kyzJSJ3R_iqKLdilv-dTYNyHU1Rp9iLpYyfeANcArsm-M_uM62T0XIB7GVdQaCdRumL-UD2DBa60n11M3nvS8fGM_08Ehha2hgpT57VGh4JGtkrw-X14q4_6RU3zu0FRYA-F6zD2D0_a-1xDAmxBbEXhe0GPBo6dGQlsUPadx1Mmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کسی که می‌جنگد پای همه چیز می‌ایستد
🔹
ما وظیفه داریم که درخدمت مردم باشیم و تا جایی که نفس می‌کشیم به ملت عزیزمان خدمت کنیم.
🔹
کسی که می‌جنگد باید سختی‌اش را بپذیرد. کسی که شعار می‌دهد باید پای شعارش بایستد.
🔹
از هر صدایی که بخواهد تفرقه ایجاد می‌کند، بپرهیزیم اما واقعیت‌ها را هم ببینیم. این‌گونه نیست که صدمه ندیده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/436336" target="_blank">📅 12:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed1f3d1ef3.mp4?token=EqQRJsH-7sWoCA3eBM4jEAM8KOQRV2D1G5wqf1u2HDthUKLJY0sSnOxfBQpMaHFJbY8BkY8kMFSo-qH52CpP79zT_znAWbEvcQLtFh_GVf7FHP07aWaR0AFQip1j0Rl6lmEySSQD7AodsWwKt2smOoQx-0QpBMzuwbPZw-9FdYxs9Q8vBCZzILQCkU9qPoko11EK5vuzaL8JKXLv4wPoTL8KwIGYlrUo2-Tgh9XCR1zCqVV1icSdkFVhwTv_ON4lagckm0vGDCEBtKAXR9pJF3u-y4AbJlyjS8AV5998ONiroFA8Qbocn1fq1TIzoENnUEe3KQME6cOVh16yjs6G7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed1f3d1ef3.mp4?token=EqQRJsH-7sWoCA3eBM4jEAM8KOQRV2D1G5wqf1u2HDthUKLJY0sSnOxfBQpMaHFJbY8BkY8kMFSo-qH52CpP79zT_znAWbEvcQLtFh_GVf7FHP07aWaR0AFQip1j0Rl6lmEySSQD7AodsWwKt2smOoQx-0QpBMzuwbPZw-9FdYxs9Q8vBCZzILQCkU9qPoko11EK5vuzaL8JKXLv4wPoTL8KwIGYlrUo2-Tgh9XCR1zCqVV1icSdkFVhwTv_ON4lagckm0vGDCEBtKAXR9pJF3u-y4AbJlyjS8AV5998ONiroFA8Qbocn1fq1TIzoENnUEe3KQME6cOVh16yjs6G7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: اینترنت پرو مصوبۀ شورای‌عالی امنیت ملی است که آقای رئیس‌جمهور ریاست آن را برعهده دارد
🔹
پاسخ مهاجرانی به اصرار یک خبرنگار دربارۀ وضعیت اینترنت: در شرایطی که ترامپ اعلام می‌کند آتش‌بس به دستگاه تنفس مصنوعی وصل است پاسخ شما چیست؟!
🔹
در خصوص اینترنت…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/436335" target="_blank">📅 12:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca68ea7e9.mp4?token=GNpVnIzxZh65hav44rZSkZVFUo8qE_lw2Jp1Cvwy5q_PkYjWH44b1pk-Wg9B2I0Qpu-OlxcqPmosv8SEV3WTiPOdQwOP9iAHxBSQYE9hiNQb3JyWGFHimIlYk2fEcI-44jTAcNDZj1IsYbcvatCr5FnmeT-s0hN600m5bH5sZ7DYEebRJVI7DNlanrAIDzx2iBKLzjCkklibccYXPkLngXD6buyw8MrgM9DRm8bCWG3K_8_tcdv41caJFteNluB8mUUo3iB4UjO2OT8J5lWB-r_a5WfNn4JMKhHQ4K16zPPtVzd2TuzmcDz74TKFd2hZbWhVnIzccKQfQZnxPLbwDWvHEpu4kBpvvBboHr_VxCHdEufASqNAWFdcbf5d5hLX5U7OI8Xw1ctanXCMxZzwiyLOAjsmVbT_b74-SS0vtS1GUuMwq8ZCNX9lHSikTYb3HSjnyYF6pVF9bQLNeLZ2bWhDLnDpsERbQm8WWBjU0v7stxoI8BQAN0dhLlPfSg6_vrXj-u8YnATzLo_FVMs2EZvMviDM0sCCW6R-b3mEtTylJ_vnFNPIXP0yxp96QyaTWlk69Ni3qPljxPBHwYzfhOiih40HNkqtco19Mz4NEUQHIfl600FKGh3mLxwc7bqMklF7YeaECanzdCxpDFOOSuJaf8ieWVV3uZa0QB2QXiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca68ea7e9.mp4?token=GNpVnIzxZh65hav44rZSkZVFUo8qE_lw2Jp1Cvwy5q_PkYjWH44b1pk-Wg9B2I0Qpu-OlxcqPmosv8SEV3WTiPOdQwOP9iAHxBSQYE9hiNQb3JyWGFHimIlYk2fEcI-44jTAcNDZj1IsYbcvatCr5FnmeT-s0hN600m5bH5sZ7DYEebRJVI7DNlanrAIDzx2iBKLzjCkklibccYXPkLngXD6buyw8MrgM9DRm8bCWG3K_8_tcdv41caJFteNluB8mUUo3iB4UjO2OT8J5lWB-r_a5WfNn4JMKhHQ4K16zPPtVzd2TuzmcDz74TKFd2hZbWhVnIzccKQfQZnxPLbwDWvHEpu4kBpvvBboHr_VxCHdEufASqNAWFdcbf5d5hLX5U7OI8Xw1ctanXCMxZzwiyLOAjsmVbT_b74-SS0vtS1GUuMwq8ZCNX9lHSikTYb3HSjnyYF6pVF9bQLNeLZ2bWhDLnDpsERbQm8WWBjU0v7stxoI8BQAN0dhLlPfSg6_vrXj-u8YnATzLo_FVMs2EZvMviDM0sCCW6R-b3mEtTylJ_vnFNPIXP0yxp96QyaTWlk69Ni3qPljxPBHwYzfhOiih40HNkqtco19Mz4NEUQHIfl600FKGh3mLxwc7bqMklF7YeaECanzdCxpDFOOSuJaf8ieWVV3uZa0QB2QXiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرایط بحرانی سلطنت‌طلبان بعد از وطن‌فروشی
🔹
با انتخاب رهبر جدید شادی‌مون تموم شد/ نه رفیق داریم نه سرزمین/ آرزو میکنم نفس آخرم باشه/ همه‌‌مون در شرایط بحرانی روانی هستیم/ با جنگ، جمهوری اسلامی قوی‌تر شد/ مردم ایران و کل دنیا حامی نظام شدند.
@Fars_plus</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/436334" target="_blank">📅 11:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf132fa956.mp4?token=Bbrua-7h1guQntnK36I6HMWccMJVDkljBJ51NkYEuYa2f5AyaD15lQ-OkLuoh0uLf0tqHV2VlxdwucXWlR4mzEu9c-KgPjz6sH2hpoJn57R6iMf-SpelF2yWJryRxlmidu9pUp_JsE66kigN06eyEdFXDTDtykPi3oH72GQmlem42SFKi3dGqiNqwKAYxwyqmpAqAndzKqNlq90v_vJpu0L0n89YRm78W339Fcr8l8Xig-yHHDcZXFJnn6JTuypb77QV-StUC-gim3fswNxoB4K7iogYflqk9hzMBFKkynWtrp4u3KEObn-TMyIGpL21EKMy5If_8ZhEUL69iBOpeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf132fa956.mp4?token=Bbrua-7h1guQntnK36I6HMWccMJVDkljBJ51NkYEuYa2f5AyaD15lQ-OkLuoh0uLf0tqHV2VlxdwucXWlR4mzEu9c-KgPjz6sH2hpoJn57R6iMf-SpelF2yWJryRxlmidu9pUp_JsE66kigN06eyEdFXDTDtykPi3oH72GQmlem42SFKi3dGqiNqwKAYxwyqmpAqAndzKqNlq90v_vJpu0L0n89YRm78W339Fcr8l8Xig-yHHDcZXFJnn6JTuypb77QV-StUC-gim3fswNxoB4K7iogYflqk9hzMBFKkynWtrp4u3KEObn-TMyIGpL21EKMy5If_8ZhEUL69iBOpeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای پنچری خودروها در اتوبان تهران-کرج
🔸
ساعاتی پیش فیلمی در فضای مجازی منتشر شد که نشان می‌داد به‌واسطه انداختن میخ سه‌تکه در اتوبان تهران‑کرج، تعدادی خودرو پنچر شده و ترافیک سنگینی در این مسیر ایجاد شده.
🔹
رئیس پلیس‌راه راهور فراجا: شب گذشته در جریان یک تعقیب‌وگریز برای متوقف کردن یک خودروی شوتی بودیم. این متخلف برای جلوگیری از تعقیب پلیس، اقدام به ریختن میخ سه‌پر کرد تا بتواند از دست پلیس فرار کند.
🔹
در نهایت، مأموران فرد متخلف را شناسایی و خودروی متواری‌شده را توقیف کردند.
🔹
ادعای مطرح‌شده مبنی‌بر پنچر شدن ۴۰۰ خودرو درست نیست و تعداد خودروهای آسیب‌دیده ۲۰ دستگاه بوده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/436333" target="_blank">📅 11:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8488a5fe75.mp4?token=L84akMxMXkmQ6dkkhM4NQ-h4waSoP71fh1BSE2EKDLkcxgwL2yDtRdEBEq9exiEKKZ8xLJ2V-1b0lI6V0Frfrksibcstuium6-zqjBH8dnutUu2dudHrienfdwiE-qp4kHKAEFI22qy7rptlGYFHn8NZELyDBqffI2NrbheoZOEYsBl5m547UubsatNaTxN2SKvyK5e53OZh-pnKrNQCvjQyd7BAqmqPjgyBQqop2HYIndJegfs96ieCMOQch7AciQmDJlITiuhlx3fuc2b3QiVsF_Sv5Hp3QnthpZZCUr-L8jLH26iuOLGsCgcNgnYOkw_NGUThZ9cflopGXik8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8488a5fe75.mp4?token=L84akMxMXkmQ6dkkhM4NQ-h4waSoP71fh1BSE2EKDLkcxgwL2yDtRdEBEq9exiEKKZ8xLJ2V-1b0lI6V0Frfrksibcstuium6-zqjBH8dnutUu2dudHrienfdwiE-qp4kHKAEFI22qy7rptlGYFHn8NZELyDBqffI2NrbheoZOEYsBl5m547UubsatNaTxN2SKvyK5e53OZh-pnKrNQCvjQyd7BAqmqPjgyBQqop2HYIndJegfs96ieCMOQch7AciQmDJlITiuhlx3fuc2b3QiVsF_Sv5Hp3QnthpZZCUr-L8jLH26iuOLGsCgcNgnYOkw_NGUThZ9cflopGXik8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف نمایندۀ ویژۀ ایران در امور چین شد
🔸
پیش‌تر شهید علی لاریجانی و عبدالرضا رحمانی‌فضلی چنین مسئولیتی را برعهده داشتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/436332" target="_blank">📅 11:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d76ab538.mp4?token=LfF5KRfNfOFu2igeC81cnsxXQaORO2uydn_W7-JAfNkWeYZF77KIQuMifTuTyEJ22CGY0C-4ChP-GT4bWQBeZZlbwstf8rghORjG-TyAqro_SLXY7vZWOfrxqhipRgYIl_QmyhlpvewjWyPxp-q3AJ38GO6EMMkuew744BEDi8QnhkS717Zzun70hL3r6SmkSEL4-KIhel6OO1-XjDy0zrELD03wr6la-leuL9--HXB_-8h8eqVTYugjtcE40a1NucNdmlp0BTrutF0HgxDc9l7dw16DCH25FBhHf7n2W2a7y6oVCD00eksfonVrewnxeYefrqK4wXgjyWsPeJvoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d76ab538.mp4?token=LfF5KRfNfOFu2igeC81cnsxXQaORO2uydn_W7-JAfNkWeYZF77KIQuMifTuTyEJ22CGY0C-4ChP-GT4bWQBeZZlbwstf8rghORjG-TyAqro_SLXY7vZWOfrxqhipRgYIl_QmyhlpvewjWyPxp-q3AJ38GO6EMMkuew744BEDi8QnhkS717Zzun70hL3r6SmkSEL4-KIhel6OO1-XjDy0zrELD03wr6la-leuL9--HXB_-8h8eqVTYugjtcE40a1NucNdmlp0BTrutF0HgxDc9l7dw16DCH25FBhHf7n2W2a7y6oVCD00eksfonVrewnxeYefrqK4wXgjyWsPeJvoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مطالبهٔ غرامت یک خواستهٔ بسیار منطقی است چون این جنگ غیرقانونی است.
@Farsna</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/436331" target="_blank">📅 11:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1625c51ea2.mp4?token=jWD8G_TXuA6LGIlaL6HMIubtm1oYrBQ7xn9LyKEKwFbpygzPLQ4jJLJHKEKrj6g-PR3vOOKc02nn1sfycsvkyMYqXonzFOXQmIVZbX_a6nwcVPPxzw21VijFZx-xf1fRsWsJqBRdJ55O5fIi4AiqH-w5vNXbaToVEoL93iSMVxWuNMg_kPv0XgFJeb2XzjqQ0P0oljdzlWVPQRPEI3wge3TSKpu4m37LWmFJ9JQ_8AN1_X8o7grSuU5pYjBeqS7xTfUcfpJ0zPNvI1ONOpnVw835lTp0DKMwKSxXE8_Zqwnfg5713gOUxHlh61jOIfPwBiBlx-9PRLoEN_J2KDi4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1625c51ea2.mp4?token=jWD8G_TXuA6LGIlaL6HMIubtm1oYrBQ7xn9LyKEKwFbpygzPLQ4jJLJHKEKrj6g-PR3vOOKc02nn1sfycsvkyMYqXonzFOXQmIVZbX_a6nwcVPPxzw21VijFZx-xf1fRsWsJqBRdJ55O5fIi4AiqH-w5vNXbaToVEoL93iSMVxWuNMg_kPv0XgFJeb2XzjqQ0P0oljdzlWVPQRPEI3wge3TSKpu4m37LWmFJ9JQ_8AN1_X8o7grSuU5pYjBeqS7xTfUcfpJ0zPNvI1ONOpnVw835lTp0DKMwKSxXE8_Zqwnfg5713gOUxHlh61jOIfPwBiBlx-9PRLoEN_J2KDi4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: خوب بلدیم چطور جواب دشمن را بدهیم؛ آمریکا فهمید که با تهدید و فشار اقتصادی نمی‌تواند ایران را از پیگیری حقوقش منصرف کند.
@Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436330" target="_blank">📅 11:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7QhSZIrp8nzfqd6I2Czp0HU-uMiU6cYkN3ndT0UnJ0IhxmZvo8n5TYJfq4FxqGda3hLmukLW-XkMqrimJ8mZ9dBJ13f2oc7qP5rhirZMJKOxmNII5MNT-yc-ic2MTJpW5Pik79ZYWXzykzjQg-nfGlEoy6fsNwzmDbImojqirD5dhV9v-nBvFSq8GHy_OsK8BmTDJicDdkRoij3hgsuyePX_MSFzkKdnU3mDl7Uq1LWikPCdEBW_llwKCTmQq3Q_Bt_w4ztNWbiuYjok0rdGsTr0Edi-4lo_vRzjGocHv6ijthWYwIjwIR3GPoSjbX11KDH5N5MDHIJuvsc3nGqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روایتی دربارۀ آخرین پیام رهبر شهید به دانشجویان
🔹
مهدی عباسی‌مهر، فعال سابق دانشجویی و مدیر امور سیاسی نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها با اشاره به فعالیت‌های تشکیلاتی دفتر تحکیم وحدت در سال‌های ۸۶ و ۸۷، به تشریح روند دریافت آخرین پیام مکتوب رهبر شهید به جنبش دانشجویی پرداخت.
@farspolitics
-
link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/436328" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/297099f648.mp4?token=ob0vpo3n8aqu7wsgf1saBoWccKeirwecthgyRICoV36rjnLAOngOzjG-rf_v91IiBGIzT2zblzqehgXRO7hk4y-zFHjT9Po5MB-dNKj_jIc6mpI4oYVX8h6dEjmijo3N22DE_zY7BHUXAfYL4V4ERN_xTd1kbDVCEdWG6BWXBK0RYK3QorVW-DN7Qw7b0fin_4IYagZ3wTEDpw_hRU9t11mehZkVhI84gIkZLSMA2CgK0fRYHies_OFmcfNeKwg2Ha3sD4-jHKlmEY-Z67vu-Qn4T_j84yTWJnsn7RfIOXpBknTvqnHqaXONARtN2d3lv0T5l1PAZRQCeKLDRsLJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/297099f648.mp4?token=ob0vpo3n8aqu7wsgf1saBoWccKeirwecthgyRICoV36rjnLAOngOzjG-rf_v91IiBGIzT2zblzqehgXRO7hk4y-zFHjT9Po5MB-dNKj_jIc6mpI4oYVX8h6dEjmijo3N22DE_zY7BHUXAfYL4V4ERN_xTd1kbDVCEdWG6BWXBK0RYK3QorVW-DN7Qw7b0fin_4IYagZ3wTEDpw_hRU9t11mehZkVhI84gIkZLSMA2CgK0fRYHies_OFmcfNeKwg2Ha3sD4-jHKlmEY-Z67vu-Qn4T_j84yTWJnsn7RfIOXpBknTvqnHqaXONARtN2d3lv0T5l1PAZRQCeKLDRsLJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیاتی از درخواست‌های آمریکا از ایران در مذاکرات
🔹
براساس شنیده‌های فارس از پاسخ آمریکا به پیشنهادهای ایران، ۵ شرط اصلی واشنگتن به این شرح اعلام شده است:
🔹
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
🔹
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/436327" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34f44c6199.mp4?token=rm9crY7QXYqYayagOXDGNnb39EYNskMPhOsD_f4Ptb7kdz0t1URrt67_iHLuvW-xAtmsrT9RCA4vkiRXlLvqyxiWE_XubdWIGSi0AcD50Ub-z9_lQgTmvlrcA-xD5yO4skMgMhdl_T8AkWrX8O-jYEUam4-gtBc1T_0deZAQ4WjM3A_qmX_Q7gb2RVr6Ps9YuLPm2HzlkgeylrZ6PLvmMMbkC_J4JPFzemAsUbfhuIvFkVoaF2HtVtrsBaepv3Qs5A_0pW_aP7KVOLUCqTQyBDI5NGW-_BR_IVJf07ZkOXg8BNm6MsKj_8CphanCTknPBDGjrVi-Tr5jXMOTBTh3PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34f44c6199.mp4?token=rm9crY7QXYqYayagOXDGNnb39EYNskMPhOsD_f4Ptb7kdz0t1URrt67_iHLuvW-xAtmsrT9RCA4vkiRXlLvqyxiWE_XubdWIGSi0AcD50Ub-z9_lQgTmvlrcA-xD5yO4skMgMhdl_T8AkWrX8O-jYEUam4-gtBc1T_0deZAQ4WjM3A_qmX_Q7gb2RVr6Ps9YuLPm2HzlkgeylrZ6PLvmMMbkC_J4JPFzemAsUbfhuIvFkVoaF2HtVtrsBaepv3Qs5A_0pW_aP7KVOLUCqTQyBDI5NGW-_BR_IVJf07ZkOXg8BNm6MsKj_8CphanCTknPBDGjrVi-Tr5jXMOTBTh3PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: دریافت هزینهٔ تردد در تنگهٔ هرمز هم مبنای حقوقی و هم مبنای منطقی دارد.
@Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/436326" target="_blank">📅 11:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436319">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuz_okSCCeFORHkZFo18hrsdguECrFHk55HbU29pHvjXFKGbUlGi4J-TUPdr3CvUneuxS8FXSXwv3IQCu0gcedb5WyMaZFNRTsq0Bi3x_csNol9Z_cIcHH_YMpZAsjo68C7-57Lw8oBQBmw2PUZjkuNpWGbGzU88MOez63IRh8oxsVhFuwQLx6yrJZQy6Cp_tdmjyMm2Seo1ml7g2g0DJYpOTHVi3vmkGPfYBbTDhNhYMiTbs88sFDCOtIrlXJx-6hBaronZd3SKV_0X3HRSMqL-jbZWiElkJ7W5Hu5rphwLAirZB8psdTaEFPeTkE1_WoyDsKhd7vRNVNqF2T6hHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNxAq5PrqP4VOJs5LxZMvjSPhjpeGvOQLyXLMIPziYiaZdY1G67OmVcg_fuySQvFU2fwULnikXvkztJQY7kvsIOBY-dYmWoqUER0waHPmHbTRCaEPmH0y8m2Kgk1jcLIMPHxnupwXEG3zRPzEWg5CrL9Ony5JJaicZd31HfwIFjWeMuCXVKJLx4vUZ23jbiYDxIrOL2_m-TsOjWHTVlDP4DVs06Gusk4qNNFKpFe0iAGUQQjpVuD2rujyVKXFEz22Yd7W9YaSV5Y_PqJfAuIK4fEfm4djtwIpLUKMd6wD2NPtHCZaDFeEQP_f3-Rk2Gagk1zzoukkjTVKrzQnBKx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwFSl6ajNgSbyehHnPFQp2sHgD3m4irzJ_PNXa-0fe8Jdbwu8fL2XC5m_EcBMjzsiuY7dYF9JYaqWUEwL_AMwG_HDdRoD0MVMQD0QFZE3zCYHmKhmpZ_o_t7gXNr-98G-vgjPa5s3S3IrbbIfLzuSEOcwZ4kLQWRsjDNhNMcH4vNpjewdH03ilLbCf2pVNMFxUl_Ih01Dt1TxJ2vVF6QQNmKxG1JM3nFYPbZkqXw--bwvCJS4sjAFG75j18PEPk2NFK3PeZ4ZV6xJRwevTEkQ3bQ33c6njcuYkk7RDtgh3yo788cUiEIpz5dTk_t3eBnm5ebI6aJKm-V68Pcjl3B7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVW6uTvn9GfjhmrdnKC_HVtgdUz2k0kv3oc2eNHX6m8Il1MayolzpaFxJgS3To83mzdGkvm-rPQfpRnO3y47DjwHEHrTY8Burfcan1-_7TxHPYEzM1WDMKzWwr_8Sb3fk0tL1TzvDpkTA9KDn4gUNhynjLsf1Ix6y_1h5zEDcRcTygDLYMlFWL3WmsBc6wRSNX3DkUXcreoVDJq6atYOLQOnL3R0C84qWJEvObgSk-HBRxpqc6Ow5KTL50BJCcoMY9iMqcGH_uHwppo5zlLozG17nkgDZy2RlYkOZro8WlFyEV8We2J06TY66oEwjPZQmcL1qMNpGZB2KaXScZYSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djEVhuYqzPAMmgVZGwsnMRg2DwJbieW5bjVi-D4CxegqIV1VrEneuLeK2w88byGxgE4OjxU2kvPgb8ChdGskr5yxbLcmtzTkgQvtaST7CcIgXa4JIFjr34LG2AoU05j-sS1U-eo3APA-IJiz8fT-owyOTyMOAMgujpX7yQ-QYBiy8CylnKfatCszlEMoDw7O54in9ZB8zoA4poCFShyxAjCGAmRQeeyruroSB6-K_wvg-cF9Vy9Ox1V2SFYPaY1iYc0INGitzNNA00_wdeYx2KyIIWdw_txX2hflj5R0ml6QnQABEbNn5_vONIm883FJ-tIVhrwzWg66Po5C1uDobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iH54YlDc4KpjzC6aA7VIjCKqwPOMF8NegsNLhWYOqr5HvjYXgMv3QNWu0DMlLsoGx5WJJvXCY9EZwdl2EIEd6OW8lvZ14q6Rwe734RUvK194klCM6cmAMzpFhMoxZv3sTT5MRTc22VYVpH7lkYMn93SH8j0JAqchBiWTdULNxrzJ4srvMa5VpVbZQhE9sAurhHdCXHFrRy5lVmOta9pkcJHJtOUeyzMKdLJAyO6QlmZek5gorIYQMA4tXPHt8oVSPqq4kdeovDQLn1__bKXlPcvohGwZWKuGsGi66fVxxc6uHxyTGVWvkekaWkBQtQS_3eOz4DNCOIei7s0t-6Rg9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5Nw3LQNLJkuHRmhEFfaP_Wn5MM_kbpsO1YRsEBAOhAhy-5DHgYJhbV8Mun189iZLsJ4CrsWPFiaSyVtmCcwCDmCe52PZ71UxTEpx1SVIiphO1DEF3IQ88BCpMlilFj-xEl2a9IBCzYiuw0wqJHsUTtafnCBrlMEhELaK3cWms9WOUqiBLBoD7Y4tK-qaEa07gWgnGXO6t_QtCTOMg7z4pUjVXVF57rikMCj_EP7XY1pQz0KDj8hH-neZwHaiBNVSWHnHJXDEYWEESAhP09YoHm7aALIBSFiS8-1YQyGfqydna1O129PByOwI_wKP4AqFSoCa-6LA9WTUhcsxKtDjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت انبه در هرمزگان
🔹
انبۀ کال هرمزگان در میانه‌های اردیبهشت آغاز و عمدۀ آن صرف تهیه ترشی مشهور جنوب می‌شود.
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/436319" target="_blank">📅 10:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436318">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720508ae65.mp4?token=IowpEsaOyQo3QcvzqBKn8z2RBUhUo8L39nv2eQIr1KIeqfzY490A2-1o3zfDe-nDnK9j_WcNVGnZpzNVxEkRH0jOojIWd6BOd_zbsQRHHNlMWfVzfA-r3rTLlMW7a7wU3JHNgNMoNiPih7cCtIHKmOrD0o0afO_eJVNtZDBEL7XyZixdqTF-FRnEe13saNL5S5jdtplfgclkkZsFl39sEWCNl_MnXt2d_x2W1jneJyqoAQgd-nLQ2fGg9rYM9s1Nw5JFNfEe-fhdL7Oo_XmdFNO4OPtQtMYoe5EJdaEwIRoVPpOHf4jrFoVGFiDGQEwc8cdJZjPBIAdtGn3VC4JhUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720508ae65.mp4?token=IowpEsaOyQo3QcvzqBKn8z2RBUhUo8L39nv2eQIr1KIeqfzY490A2-1o3zfDe-nDnK9j_WcNVGnZpzNVxEkRH0jOojIWd6BOd_zbsQRHHNlMWfVzfA-r3rTLlMW7a7wU3JHNgNMoNiPih7cCtIHKmOrD0o0afO_eJVNtZDBEL7XyZixdqTF-FRnEe13saNL5S5jdtplfgclkkZsFl39sEWCNl_MnXt2d_x2W1jneJyqoAQgd-nLQ2fGg9rYM9s1Nw5JFNfEe-fhdL7Oo_XmdFNO4OPtQtMYoe5EJdaEwIRoVPpOHf4jrFoVGFiDGQEwc8cdJZjPBIAdtGn3VC4JhUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارع‌پور: شهید رئیسی شورای‌عالی فضایی را پس از ۱۱ سال احیا کرد
🔹
وزیر ارتباطات دولت سیزدهم: شهید رئیسی دولت را در شرایطی تحویل گرفت که عده‌ای اجازۀ پرتاب ماهواره را به این بهانه که مذاکرات را به هم می‌زند، نمی‌دادند.
🔹
شهید رئیسی اولین رئیس‌جمهوری بود…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/436318" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsX3b4IMcR3rvX8shwhDn-s6XNykthdw63ytVY0qZPJ9LcnRNBBqtVcxaSETZIVEFkvkUhM9m_KyDbPwjBxWwWwf2HsGkVyZ49LYrtrwTHHdn0LfgWPcyz0Vywg2B8c2GEG4AYfwJNI_VyxkVLhgCTOnS1t24jIixpumqokPVRypVZDv5ij3fA233e-IBhjANg9ez01bujeZ9xmFCm5OdZ1Rap77zCJHYYcocwmYPG6VO-eiBaIaAOjqIoi_5jHlHCsDbazzixcihopStwb-6D7_L2rn3PcMmV9aLxee0-jqRRIxDUSjaqwvMkCbSZzOhO5OEIHoGNnOHqL__t5Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovQXVKdGuMIaIdJnJGwjmOAZPCtYDpsZr4EO2CtsvPD9QRvBrqKQ4BT5JR_8u3mIpfK5Omn6RLtAJyyC9v8sfemKTfJdUmdRfi6J20VN2o_54XP40H8pEj1WW33DVS3GpZnpZ7_cW5rtjOYPXvY9lYCiM3mb2EZ0gs-XtF-Ek4InbAw8IlIXPLeXJTT5h5hgQsCEBLbQEm4nsb_ZoqlRWVGe619yCKchWWh2QtM4oplxoide0pzNOE1OZVjunCatOgX5N89yonSFpN8mqIvySxgQyCVpoHsDvHFOqlGkzIRHwgM0aRew6scpvy7xaQfCMHuF3Ej3FT5Q1CvjEY77Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvRwOW3iM2IOmqd5ElJlnm-x9D8xqVkaLPp76mh6L9FF30ZB9YDT9l1YPaX4DiKhLSMy40ihFIjAe_VR5gQLteqYYtewFWuPDCZ2egEDqG60LwHnt08xE54Fj0NXBzWxiowoTKFrZZBfiz1YCZ4D0MFzyb2wIYu8wqufR8lnoRrpUds1IadeHNOj_s9UJ9L6dh79y8wutDfjnqqfLCRt3nuHLmvcvfdikrV51oUgmBWhldOxn_w-Lzdgyy9i6sW6EGqolY5MNiAEOTT_Le15-FOTCLwLWBFdIhYMuEExVJdpf43xQZq2vWzFiNyQBjsEk7YTwbfNuo3rvR3cIyuTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Chu8-djWZ521JBOViWKxs3VaGyGW5EUH56ZT-WlVOHmYQi-_KAu2FPFTc5qI4RoVmwuFv9Rt8VVNJAMHiMS9RFJTsEmQX-J6qmRxOyp-PCoUoAJuXbptvVFcbM5R6hP1XlYJzst4FppzcYCQF1n2n-gZvOipPrZuCo-z8eOdV3BVHYZ2Pj6qkWXbS3aHj231JoC-CCL--xji4ZDD2qGZCmgvNjf_n0JAaKZZs-U4p6dEeAAVjFSKd6Hn1Dtkvy6lZUSVDAcCZxYsbudaKTRAylgQF-M7-UehCl4c8GmbiaIZwfZ5XDlpeBiedhvSje4u--7SFeXMaYFQLy6s2-PaPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
قلعه‌نویی: امیدواریم ویزای ۲۸ بازیکن را بدهند
🔹
۴۰ درصد عقب‌ماندگی بدنی و فنی داشتیم که ۲۵ درصد آن را جبران کردیم.
🔹
شرایط سخت است ولی نباید بهانه بیاوریم. @Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/436314" target="_blank">📅 10:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436313">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc49b0f7a.mp4?token=QKMp7mV1ZgtgytBIUKsMNJexsVA6i462oxsle66LHTEaDe86WXfiN2p7erIptmMeBGwWH6nxG131i66oxQ5KfeDjpjbX5lGWD3B7iQbvseyGCJ-Yz3yZrMo-tsAGmanHwzTQa-GOmjZxIlXKYLgyhmRufnZ2Jx4j34e_Sp3Vdbtf98KW28ajkrUy0oHdzTZd5AB8cvJURxmV2BtjoYZM3y3xD3uthJGesZ_TjO7Dev-m8_7q7gjdBfG8uyE4W9J81mz5ikQjr1NxtnwXl7rLKUBwb00t-RrrQ3qG8r69oFBLK_B1VIL9gmrXGodH902OtH1fjaCx1A7wrX2f0Bw9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc49b0f7a.mp4?token=QKMp7mV1ZgtgytBIUKsMNJexsVA6i462oxsle66LHTEaDe86WXfiN2p7erIptmMeBGwWH6nxG131i66oxQ5KfeDjpjbX5lGWD3B7iQbvseyGCJ-Yz3yZrMo-tsAGmanHwzTQa-GOmjZxIlXKYLgyhmRufnZ2Jx4j34e_Sp3Vdbtf98KW28ajkrUy0oHdzTZd5AB8cvJURxmV2BtjoYZM3y3xD3uthJGesZ_TjO7Dev-m8_7q7gjdBfG8uyE4W9J81mz5ikQjr1NxtnwXl7rLKUBwb00t-RrrQ3qG8r69oFBLK_B1VIL9gmrXGodH902OtH1fjaCx1A7wrX2f0Bw9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه‌نویی: سخت‌ترین تصمیم دوران مربی‌گری‌ام را گرفتم
🔹
انتخاب ٣٠ بازیکن برای جام جهانی از بین همه بازیکنان شایسته تیم، یکی از سخت‌ترین تصمیمات فنی دوران مربی‌گری من بود.
🔹
خدا را گواه می‌گیرم در انتخاب بازیکنان چیزی جز معیارهای فنی موضوع دیگری دخیل نبوده.…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/436313" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owJThNQcmKttPI5PgYe-V0UH9jyfC_7MZGa0jsEIhizCW3qI84jvg4YNJtRJQhtYK9NlvpDItIdUsR1gh3RDlvGT4_o0_tz_5bTdValMwo-h-45FzTBKku1X_V9vPOxSiFu2Ob5JUX7MT1c4syCFaSp269v20HcV9kU8YC9MV-4Oc2dA0LpcbQtcA1vn1Ypqqiipt4pr2d_kLOTR8yNuwlZ2B2BJ18O5Uqo_dWb05DUc35HZiixB4bK9q2TTn0IhXV9ppGlha8e_ug9Sy_KVHGU98NRZwhWOcvKN01TfkHvZQT23fSZmXM3cAZ-7cx5YETo_TIFcvfVNFHGbeahbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشان ملی «روابط عمومی برتر ایران» به ایرانسل تعلق گرفت
🔸
همزمان با روز روابط عمومی، سیزدهمین دوره «جشنواره ستارگان روابط‌ عمومی ایران»، ۲۷ اردیبهشت‌ماه، برای ششمین سال متوالی از ایرانسل تقدیر کرد.
🔸
در مراسم پایانی این جشنواره که با حضور جمعی از فعالان ارتباطی ایرانی و بین‌المللی در سالن همایش‌های کتابخانه ملی ایران برگزار شد.
🔸
در این رویداد، نشان ویژه «ستاره ارتباطی مدیر ارشد»، با کسب بالاترین امتیازهای لازم از ارزیابی‌های تخصصی و به دلیل شخصیت و منش ارتباطی، روحیه تعاملی و نقش تعیین‌کننده در بهبود ارتباط با ذی‌نفعان و نگاه تعالی‌جویانه به حوزه ارتباطات، روابط عمومی، رسانه و افکار عمومی، به مهندس محمدحسین سلیمانیان مدیرعامل ایرانسل اعطا شد.
🔸
همچنین روابط عمومی ایرانسل، بر اساس رأی هیئت داوران و به دلیل درخشش در عرصه‌های مختلف ارتباطی، به‌ویژه مدیریت هوشمند خوشنامی سازمان، موفق شد لوح سپاس و نشان ویژه ستاره ملی «روابط عمومی برتر ایران» را دریافت کند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/436312" target="_blank">📅 10:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps6dpvSGXl6YLHWXv7cEn0hkv97wJUnFJPMWq8ZP5X7qkrXkOnh-7p7U3jI1XoRjPf-USqDk28nfsRHhq7rBPBu9YmqXGDJtsTkF8GjoxZFNCD3DwAuNu-FUPe9eYfugzPiCj6MmjVHpCiaOF_Uk8v5IT4E335nFp7_CncDytny0Gmccx-pGdP-A9de_zhV3dhN-5idja5rn6P2wALZLWGM_vpWlr2k95Vmyn21D-x75fQqC7ohFeo5B8msrTRHdlbqYx-MVmNO2hqgGF7IkeJDIRwSHK3F28oBybR5AorBY9gzt6T2MUZgrdOxycTALomr2x1G7d2C_h1Ak64E7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر فوری: کوچولوها مهمان ویژه پارک آبی اُپارک!
🚨
💦
فقط تا 15 خرداد!
📆
میتونید بلیت هدیه اُپارک مخصوص خردسالان رو دریافت کنید
😍
🎁
برای دریافت بلیت هدیه روی لینک زیر کلیک کنید
👇
www.opark.ir</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/436311" target="_blank">📅 10:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/436310" target="_blank">📅 10:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78eb18e991.mp4?token=YC64ABiIh2or3QCXbtsFM0wybfAXWrqOsO14ap2kYxYTcpJTTbPYGDApZjZNeOjuwG-2wU3CwbtHRyWFGf_BLmzmOse0TMTocKtPHgN3hLoDKcsQvx9vpvDJY4pmoADNUP4lzsCAXmtwcoiw7vs9keRtJJx534F2XI25vlCXs_Et1DCWWRolEoOuXYIVP9TRGxjS_30N2RSFto86OfBGiUvFFyhEbKFtjdke_LA_QGYfZdTwcYJ20ZyrKli4tLApOz3GTNrb_Hrwx_cbRny2Dc4JXkQUlE6RXGejQjjPF3-HeM7afWkBe6NcftJXfuqaiKXCiPJzegdXwYnEMtHz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78eb18e991.mp4?token=YC64ABiIh2or3QCXbtsFM0wybfAXWrqOsO14ap2kYxYTcpJTTbPYGDApZjZNeOjuwG-2wU3CwbtHRyWFGf_BLmzmOse0TMTocKtPHgN3hLoDKcsQvx9vpvDJY4pmoADNUP4lzsCAXmtwcoiw7vs9keRtJJx534F2XI25vlCXs_Et1DCWWRolEoOuXYIVP9TRGxjS_30N2RSFto86OfBGiUvFFyhEbKFtjdke_LA_QGYfZdTwcYJ20ZyrKli4tLApOz3GTNrb_Hrwx_cbRny2Dc4JXkQUlE6RXGejQjjPF3-HeM7afWkBe6NcftJXfuqaiKXCiPJzegdXwYnEMtHz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از تنگۀ هرمز
🔹
عبور فقط با اجازۀ ایران ممکن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/436309" target="_blank">📅 09:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">ذره‌بین بانک‌مرکزی روی معاملات آنلاین طلا با سامانۀ جدید
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد ورژن مقدماتی سامانه‌ای که قرار است بر معاملات برخط طلا و نقره نظارت کند به‌زودی قابل دسترس خواهد بود.
🔹
با شروع به‌کار این سامانه انتظار می‌رود از بروز تخلفاتی مانند خالی‌فروشی در پلتفرم‌های فروش آنلاین طلا و نقره به شکل قابل توجهی جلوگیری شود.
🔸
هیئت وزیران آبان ۱۴۰۴ بانک‌مرکزی را مکلف کردند که برای نظارت بر معاملات آنلاین طلا و نقره سامانه‌ای طراحی و راه‌اندازی کند که گویا بانک‌مرکزی مراحل نهایی این پروژه را طی می‌کند.
🔹
پیگیری‌ها در خصوص آخرین وضعیت عملیاتی و اجرایی شدن این سامانه نشان می‌دهد فرآیند پیاده‌سازی آن، تکمیل و تأییدیۀ اولیه از مسئولان مربوطه در ستاد مبارزه با قاچاق کالا و ارز دریافت شده و در حال حاضر، سامانه در مرحلۀ انجام آزمون‌های نهایی امنیتی قرار دارد.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/436308" target="_blank">📅 09:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
مأموران موساد در تور اطلاعات سپاه گرفتار شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/436307" target="_blank">📅 09:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قوه‌قضائیه: اموال ۱۲۹ نفر از خائنان به وطن در آذربایجان‌غربی توقیف شد
🔹
رئیس‌کل دادگستری آذربایجان‌غربی: اموال ۱۲۹ نفر از عوامل دشمن و خائنان به وطن با لحاظ اقدامات ضدامنیتی و همکاری با کشورهای متخاصم به‌نفع حقوق مردم توقیف شد. تعدادی از این افراد عوامل اصلی و نفرات مهم گروهک‌های ضدانقلاب و تجزیه‌طلب هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/436306" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام تقدیر فرمانده قرارگاه خاتم الانبیا از مجاهدت کادر درمان در جنگ تحمیلی
🔹
سرلشکر عبداللهی در پیامی خطاب به کادر درمان نوشت: به‌استناد عظمت وعدهٔ الهی در آیهٔ «وَمَنْ أَحْيَاهَا فَكَأَنَّمَا أَحْيَا النَّاسَ جَمِيعًا» هر کس نفسی را زنده کند، گویا همهٔ مردم را زنده کرده است.
🔹
در این لحظات بعثت مردم ایران عزیز پیش‌از هر چیز یاد و خاطرهٔ رهبر و امام شهیدمان را گرامی می‌داریم و به آن فرمانده شجاع و حکیم که با نگاه فراتر از زمان، مسیر خدمت به خلق را به بالاترین مراتب جهاد پیوند زد و ما را در مسیر مقاومت با شعار «حفظ کرامت انسانی» رهنمون شد، درود می‌فرستیم. همچنین یاد و خاطرهٔ فرماندهان والامقام شهید نیروهای مسلح و رزمندگان فداکاری که با بذل جان خویش، ایثار را تفسیر و مسیر هدایت و ایستادگی را برای ما هموار کردند، با احترام و ارادت یاد می‌کنیم.
🔹
در این مسیر پرافتخار، ملت قهرمان ایران و نیروهای مسلح همواره از حضور تاریخی و پرشکوه شهدای کادر درمان بهره‌مند بوده‌اند. قهرمانانی که در میانهٔ جراحت‌ها و خون‌ها درحالی‌که خود در معرض خطر بودند، از جان گذشتند تا نفس‌های مجروحان برقرار باشد. آنان که در میانهٔ «جنگ رمضان» علم و عمل را با شهادت پیوند زدند، اکنون در کنار امام و فرماندهان بزرگ شهید، شاهد شکوه ایستادگی شما هستند و بر ملت بزرگ خویش می‌بالند.
🔹
فرصت را مغتنم می‌شمارم و تلاش‌های مستمر و ارزشمند اساتید، پزشکان، پرستاران، پیراپزشکان، امدادگران و سایر کارکنان حوزهٔ سلامت شاغل در دانشگاه‌های علوم پزشکی، بخش‌های بهداشت و درمان نیروهای مسلح، بخش‌های عمومی غیردولتی و خصوصی و داوطلبان عزیز عضو بسیج جامعهٔ پزشکی را که در جریان جنگ رمضان با مهارتی مثال‌زدنی جان بیش از ۳۴۰۰۰ مجروح را احیا کردید، صمیمانه ارج می‌نهم و سپاسگزاری می‌کنم.
🔹
شما نشان دادید که در میدان نبرد، مؤلفهٔ اقتدار، تنها گلوله نیست؛ بلکه دستان مقتدر شماست که در تاریک‌ترین لحظات، نور امید و حیات را به مجروحین باز می‌گرداند. حضور شما در میانهٔ آتش، تجلی واقعی آن وحدتی است که علم را در خدمت عقیده و دفاع از میهن و آرمان های بزرگ ملت قرار می‌دهد. نام شما قهرمانان مجاهد، در تاریخ این جبهه به‌عنوان «حیات‌بخشان» ثبت شده که در سخت‌ترین لحظات، به‌جای عقب‌نشینی، به‌سوی جراحت‌ها شتافتید.
🔹
بدانید که هر تپش قلب مجروح و هر نفس بازگشته، گواهی بر اصالت رسالت و شکوه خدمت شماست. از خداوند متعال برای همگان سلامت، عزت و پایداری در ظل توجهات حضرت بقیه الله الاعظم(عج) و تحت زعامت و رهبری‌های حکیمانهٔ مقام معظم رهبری و فرمانده کل قوا حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای(مد ظله العالی) مسئلت دارم.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/436305" target="_blank">📅 07:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuWHbZ18V6gI1lPv-g1WEgwB-7igBMugK-ijI29ZOjU2lXRGUXc3cjrq0BqTDWtJNcyFF4JQjkEDvhBcz20uIrHKWxyC6mqBnCrKo2FsVMlZdJiThDOUrzUZnHa7KiZSLY-yIyDP4QvxgmWoczcswGHEHTCooUeI4gBvvagcsF-8Xb4_KsgJUoxeOhWrURT-VW-vUtYFRQRZ13P0U7D_9x26kqqwim_8FSx7vrpPMz_45kFtY2KwvoIq4zXO-wyOmcRTKd6r6ksS1KQxZNNPin2xLrJ7ZTy4Je368Jymr2vvY0mJ9ctN9e4vxs6F0Huy_-U_jHTMJmoQJBP9Oqq4Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت در اولین ثانیه‌های بازگشایی بازار
🔹
دوازدهمین بازگشایی بازار نفت پس از حمله آمریکا و‌ اسرائیل به ایران دقایقی پیش رقم خورد. نفت برنت در لحظات ابتدایی بازگشایی بازار به رقم ۱۱۱ دلار در هر بشکه رسید.
🔹
نفتی که تا پیش از جنگ رمضان کمی بیشتر از ۶۵ دلار ارزش داشت.
🔹
همزمان با افزایش قیمت نفت، کارشناسان از افت چشمگیر ذخایر راهبردی نفت و سوخت آمریکا خبر می‌دهند و معتقد هستند، دنیا در هفته‌های پیش‌رو منتظر شوک دوم به قیمت نفت در کمتر از ۳ ماه است.
@Farseconomy</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/436304" target="_blank">📅 04:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxivpoNXOMm9MF2-TRvaTUe8KpJj7Vc4-I4cpHQT6_Qk5CUYSUjmQyAMouKdBaX0d574OfvT8e7k349AvK-cAubJg9usenw7TWc0UU6vcCfLIyqxMj5LM2VpMmts-DgH_bWsQAd5ElNzPmOeCOtG6ZMS-IHApMayjGEUQ03Hbg40kWIjzN6iRke09B-F9jSQjzZeFF5d3UEvPuiISxcw2P5cw3td8WxNgpk2VSzrqtzvoa3u1I5NNY2UxEXf-rQOC5PJQ45CF0Qc-6qz0J3u_9Un_eFkrN5wzTsbeDdAb2MTofWkDOM8SwWduq2amZF3R1ll6nkxgahmJpDczaH0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BjSzRsMe-eRTMCtvsq1EnvAXr6yFGuFqkdgB8Pi82MRgc8CsS4WA238zydXDDH5XO3c5EgH0i1bjYq15qfQWrIAZCm7q6hg0c-z4GTKwnHqzLP4bnhMz_DxAL8Bs1OC78XVGDLlbd4rbcUg2HYTigKjUkqfTvVDex8lc_2uVANgAdCsPmdOeR5XpPx51FfL6kIex3CX8wUspGy4evSIlv7JUyOiH88L-vFGT6EPGKYRWaA3E-M-L_2RTiP4rFCCKacQMqDYkbtqRG6B8c3TCgEJcSjLj9RByX2wml09q4pRpNCgZBgVGqHZESiepqAGGySB2A30G2R5rjzz2Oh96nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quIpD177Cr8d15sasUOEQcx9myRwFnsUx4fKWNeAK9E2mXStXNO0ycrFSThKOrUoOFZYv2Qh5NiZKjjq_emMIEQTtYFUYJgfeLCPOd-SxjScK7-A7C6qy3CkeS1G2ed-XUuvgAEQ_WeBosgznqLDs-qipL9qFGDa8Z8bHyIW3-UV1b0kJkVJQn2UucYWUoGlhL82AUbWODYH6gI6YMxCrwXHOy0MOSfs4B-YMN44t7aqYT-YMr_yutuya8Ft7sHSctcAOxFXfibU7bXTik56f4QtVpDVv_xy4JKlw3aOZCFzOuzF6Vml9qauLY5-tcJWxn-6ip_DZPyWfYRdXzOK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARq4oaLExXSl3kMrUv2gwldwF_Wfk8F5ywzqRZSJgvoXi7v_lrMb8RMMbuUqWIhw4RFZo4dfY3xgsub375e9RBF-rfIrKxUNHWB-ztQolRinlVXxUERB-BjiM6dZcH4RrG5ajC4nf2oM0JLVQbofVRVSTx8dy-nUa5LF1CAkeXzUOSQgo_J9ZqGTb4sLVKkuyrePvxvlZSD7eA-uvZJO6yTd3xnlB6w0JLpfStMwOjRkLrDae5LjsBBTZE32xM_lJvWFzQgn1NSjKp11mLpcGKHytoNv5L1MJ5V3m4vhyXNpbKBVAo7F1skYT1VZZx_XCGkB68qh6CSQrD5SEsXz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdVz2L6bXEZFhU7P0vwlYScoi7iUd_nj_uBeslrT3cxtuleRMMPiwvLEYQ_33W9oTIp57tjG8uMH-n1hxblWr3YsnLGSzFzCrCN3SpBpcxONPalbHqzYQeogPKIwLqhBWyI7ZzR7gv9krkS_DkXoiqn1sXC0qGEXrlInBAX4L8NEpnCYfUOeQfRZsZIWv6x5UKkyY8vDlf8iakzXFCR8kcDMo8E56kES1dxvWxg9iTInRnq28ngIOEZgnTpUZfDVa8nCSvSkyQYIcjK9ksuClUYaGZuuZ78UHm5LxTHhIF5YFmvDInUe6AUBNRABfEv6b9Xr9vWuK2NTw_Wp1tI45A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
میدان‌داری اهالی باقرشهر تهران در موج ۷۸ اجتماعات ملی
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/436299" target="_blank">📅 03:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436292">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1M6B_8d9zGKglenpURe7HR3EGRiI7jsblhAKZbWBhxM6RGS7EOf1kOGnIKhnYp15K3EYyN5KzWtoBw5He34uXZLPXjyjJanFjfbMN7lqlflWkuFqlDtdUUrGnDPwPBRpgx93LD1G6V01EGyE8Ixu7H6VvTXn31L1-usUZtSHlTTYzZE_gWww-00wfMdYZ3gSCMg1I4rQTMZObMPooj95p5TtqROl5D4lCR5248wD2WvSXNkN-tMmqLolziWXJrjQ0je_R0SQSduKQvsSi69e7Oev0J3qj2FDCjADSqDEwznloDkpJ890mDtyA3SA1c_9ThGjdzvHEQIXo8W_N_gUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ib5QiT2mTZijTA9fv94HYU3NaIlzcTmnB78Towkvk4Y4MIK4v9XEY0R-oKzu9qOWaAD5nT5F9GDgi1yKCM6vuOFUPnypUPyxJD3zc65oGi5P7lzplPsZqX9Eib5dKDW4zHIjaYus3xqxTJf3ZRZqKag5CPGMRgFWCVilodz4M-JeUSzpjmW9GLyR4gHRAi3RK8Ai9BmF9KcSHyyL7DJJk3tqevbN5cd0wRKBfJN7X1PH1H8ysQiBFjKOhqjfnPOEq3PuHLU_DuvtyHXCdIXigPrvMpYyN-AOf28kiPh_CPTKxh8bCNy5LOq4rXsWqpkwQGD8owgN8xSCSZucoMPANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vktgAVYywTaB2988BiS8HIQhP3Y-ic6r9wf5sEI_BruJ2DCGwhAo3vtApD-fGLL_PvJG6xX0O9HuB1UsB1fium_RTtjYTEMLEE0sgYGQ9Cf-BUc1a9G-wsIt0H0_qoz24s726zhcYuUgZDn_7D0FYYPUp0DUQk1cLWLeBGCOU9z_1pvf7dhjTMNv-rX5Tpj6NV91392DdiTTE71ctYZgerpLXMARDN6hLpqRETa_0ZcyU6br9sEx0SxGAXbj8xFgpEXbe9zbPIIQGC5FSqAQq-out9zjT-7tZFnTASm5ntfPlP2PtIwnQa_KtKpfhBPvaFa8pVc3Xz5_BtvZmwlFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfYZF9_8Vs4I6E19PA0vVq5dMJkj4Mrs50vDIOdrepdX8UvIEJ2x8T6ESCTwbAq9qdrGdeFwCdYHfCSKTPO9lPeH_M5ALF7b9IXD7wTW8nV9tV_PWH9jDwDHxdt3CsABi7HPQbqxN1GBTRWJ6oxDH6seTry8zVKDaQKcgOl80vABJla1EH4WGwnV8Y1CZS10OnDsQkR-4HrovFhQbR_wIEfVdUMjNlLWStnKQhbyFuH51OBI3OgHaAdjKkk_fU_JcXmYXpHBbjFd91rU7x4_a32j2ZVTInuHth109wkjuGvzODxF_E9NmOoRVIL611HetlnG25FMbsQTsKZBWQZnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVAjmOqf658XLixAx_4lRlpiYy8VAQsDip083LSNaQPeqTFRN9SFV6tKafK04pKWoOQszyx6Nm1p6WebF28IwDDn-rdwqY9pTPx7Rr6JmLpJD-5JvxdvSqDSFSOt4KUQgn5wCAg-kUQdMwGu1hYN2KKaDU5wqzl446e6zywkvT_aRf-gufEre6koqFOhXM4tc1CzXXbJa9A1BjGN8XOtP_uw71pAtY2PFvZkMM7FrARizGLcHe8RO_C3QrzMzROhJOe6Qry4F5p29M6sx5nHNOXJe9JeC6A3GhVjYlPY7svbtAawhMUY1ec8zjtEH0puneytQycFC_5-HhtQ-SMHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srhNrbOILQ4OURFnNsj2YLwXmQT2wjxoWTyaQBuQXaXPhvjziX3LDK935lk6kFE3Hs4AvTK2Bl5nhiR25DQrsBH9K9YYMm8BcBQh1bYfXOfFDzcNI85BW9t43A-4zWN7KXGWcduxag95cH57IbyXWKEyfC5ikhZmMiCeBR-wHYqkJqX17A-UBxOTwQn0ZqAPp8iyzwzq8oPddiEaUo4tBr3c7ZjT76rKVCd8V35_T5vIXKeaRhEVTpn5qJ8HV1-pp61oGPlOOC6SpmJmw2tiYIC5iIpvQmTHEbkJxMJtsTqHS-EtcNm6662z3aOleT4jSH-8BxLQi5w39J949zbu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBYExlX7tvz2CLvzJ6UoGd6uBovcXg-HmP3M72-uzlrvPPF3RP5AwrWwqYXZXDzID5abk4qMicCvMpjPD0Smpw9SwfctVY7csp9QpNZNMwsj61fIMa7R1lK5Wno0e77xhtVrSZmgOvUfvO830tMBnal0wwR3TKr1FF9dZWvfuSF-GJG0nFF9D1jZ_6cZ3l0ImOpJepD5z9DyW9tZil721wEyy7vwo52WxyIdJpaaQuR8sBO_HiDJzn7W8L7cvcudhCoxJVpIPTlIB-Sz1AFEKzI96BWj0CUdJhV2MlXOokt9MgXPjQ5ZfYR8iojscC__wA-L0m5syYUNUwbo8V_Xpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شب ۷۸ تجمع مردم تهرانسر
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/436292" target="_blank">📅 03:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436291">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDLtonLRKug_HhJ0FKyRNApMefGVtUXaxOUWifwUsiFhiS9B3oZJ1zU6-D5gbnkbD9I3WYxZMdh0MboLrztcFHldTZgwCoC7QNopy-MKRDbWBZjO7V4vnz7UYUqwQPKCNvSk0Md0uMAepru_7oW2lnQZmgts0WT1X72sVh__2tXaO4llKrpNb6PHCifd6EV9HDVdu4O6NKMkNIFAHLDPOtqAD6wI-aFyGdP6wusMQjKtblOJ8todjMC1P6JMfZlHCdBDRg2ucREU0uxg_YZm3jCkseLH3rCD8YJBN6bLeR80UUEPTEqS4XxHVd-NUped8vnbLzVtUHhbNu9puMJIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجبی دوانی: خلق اثر در خیابان، نمونه‌ای عینی از بعثت هنرمندان است
🔹
محمدعلی رجبی دوانی، پژوهشگر حوزه فلسفه هنر در گفتگو با فارس: ما امروز در مسیر اتفاق بزرگی هستیم که به واسطه خود مردم محقق شده است. بعثتی رخ داده است و به پیشگویی رهبر شهید ما مردم ظهور کرده‌اند.
🔹
هنرمند به ‌واسطه اثر هنری خود می‌تواند این حرکت و جوشش عظیم را بر قلب‌هایی که هنوز فتوحی پیدا نکرده‌اند، بتاباند و این قلب‌ها را هم دچار خطور و بازگشایی کند.
🔹
تصور می‌کنم بیان حقیقت به‌واسطه قلم هنرمند و یا با هر وسیله دیگری که بتوانیم آن را زبان هنر بنامیم، خصلتی تاریخی و فراتاریخی پیدا می‌کند؛ چرا که زبان هنر، زبانی در تاریخ و در عین‌حال، فراتر از تاریخ است.
🔗
ادامه گفت‌وگو را
اینجا
بخوانید.
@Farsnart</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/436291" target="_blank">📅 03:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
آسیب‌دیدن کابل‌های فیبرنوری در تنگهٔ هرمز، چه تاثیری بر روی اینترنت جهانی خواهد گذاشت؟  @Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/436290" target="_blank">📅 02:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5e95c34e.mp4?token=O1o6Adv_OpvGjF8SlJvy0k1syz8trIPsnCor-DhdG7z2MI42bLZm9NavJoHSrM91nADLBMRR4InViHXVsuvEdba2lodDOqjbMkgI7skFWy1Btsw9nAQAHhdPduDEvawrptglcV6FP0IWCOxMpfOHeTVz13MRYi4AwVbqlNCmeuwdTBz5dWhGLxryIUnzcEYBv6ScsG2WDSf3nLVlDteFQansLFzk9XUwPH9hFyKufNpSXrKayFOOme7CIPR6W0XwuFVpKxUKMCMWiEXdR3kb05nyf7ZK4mXWdFTiGCbVRMp0t5omfxtjAMzO9fpWp6druPs3A_68xPjiZ_Q-_taPNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5e95c34e.mp4?token=O1o6Adv_OpvGjF8SlJvy0k1syz8trIPsnCor-DhdG7z2MI42bLZm9NavJoHSrM91nADLBMRR4InViHXVsuvEdba2lodDOqjbMkgI7skFWy1Btsw9nAQAHhdPduDEvawrptglcV6FP0IWCOxMpfOHeTVz13MRYi4AwVbqlNCmeuwdTBz5dWhGLxryIUnzcEYBv6ScsG2WDSf3nLVlDteFQansLFzk9XUwPH9hFyKufNpSXrKayFOOme7CIPR6W0XwuFVpKxUKMCMWiEXdR3kb05nyf7ZK4mXWdFTiGCbVRMp0t5omfxtjAMzO9fpWp6druPs3A_68xPjiZ_Q-_taPNTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ مهدی رسولی به یاد شهید آوینی در کنار دانشگاه تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/436289" target="_blank">📅 01:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436288">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9XhqJ61MepjagxJisU85BpBCHa98YK01V9_DGKxwK_s7In5WPpKfrrLRrCLcjtvXgUqPTRySBUXb0paDhmAPSETK6WZ1K6Ha9K0XuqvwMcNZv6k-cWAzRWw9d5JYChpSrQ2H35N3fPY7rWv0Hg_XGamOWlQKNO0CZfQRKdm6eDRjn785OLdWe6VrRBSE5XiMyMrSmqTIgSKz8Ai7RGsa03yzTmSZMxCG5kSWK9SVwB5c8mSB6gVDeqCw7HVlU8mrEU-XLe_gkz5C4h9is-xwnnTexBIg-Z_am8uagzp_wUQTslUBTwlWNHdYGroSl3TKilcTGaMbWRzulJCVry-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام سردار قاآنی درپی شهادت فرمانده گردان‌های القسام
🔹
ترور خائنانهٔ فرمانده بزرگ و مجاهد، عزالدین الحداد از سوی صهیونیست‌های بزدل، زنده‌بودن مقاومت را به‌ویژه در قلب غزهٔ قهرمان نشان داد.
🔹
این خون‌های پاک الهام‌بخش مجاهدان جوان فلسطینی تا تحقق آزادسازی قدس شریف و نابودی رژیم اشغالگر خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/436288" target="_blank">📅 01:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436287">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21042a8574.mp4?token=gny_s4pRgR_nCmqSzOCBNTPGvjL9RIqHCJrKpBMMnafNlYpj5BOaY2vHB6oRW4fKyidlzCsAfXAdwO7xgaylEv3CASmapPnphU1XRBP8MAkPx9szwubeQmTPqzASedbV_h4OyXnRDn-rf1rPCyphQ-VsSAvPAHXmNeNZxnHkjH56RqF9T5ezdAOFYsKoFvziM3rcu8rNXUKuO2t6UrFkFziFJEIDwTptk7zuIkF_cAQkwVunGYXqp9TAtRY7P4TK17OqEihbhd6xA7BfvO94OA0AKAACmc418KRuBR27lf8hxsK6HukXfV-qME5drjHwz-abqvS1c9dFlLJ3cwm-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21042a8574.mp4?token=gny_s4pRgR_nCmqSzOCBNTPGvjL9RIqHCJrKpBMMnafNlYpj5BOaY2vHB6oRW4fKyidlzCsAfXAdwO7xgaylEv3CASmapPnphU1XRBP8MAkPx9szwubeQmTPqzASedbV_h4OyXnRDn-rf1rPCyphQ-VsSAvPAHXmNeNZxnHkjH56RqF9T5ezdAOFYsKoFvziM3rcu8rNXUKuO2t6UrFkFziFJEIDwTptk7zuIkF_cAQkwVunGYXqp9TAtRY7P4TK17OqEihbhd6xA7BfvO94OA0AKAACmc418KRuBR27lf8hxsK6HukXfV-qME5drjHwz-abqvS1c9dFlLJ3cwm-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطریانفر، فعال سیاسی اصلاح‌طلب: وقتی رهبر شهید، ۱۸ و ۱۹ دی را کودتا دانستند ما آن را باور نکردیم اما بعد از شهادت رهبر انقلاب تازه به حرف ایشان رسیدیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/436287" target="_blank">📅 00:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الجزیره از حمله هوایی ارتش رژیم صهیونیستی به حومه شهر راشیا الفخار در جنوب لبنان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/436286" target="_blank">📅 00:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436284">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io0_NaIIw_esONcbMj7O2lczRq-MqZHsbxYGq6WMmXqGkt4xnGLPLeZ3Lu1WCKcd-NMAsZ8PTQZIKUsCwy8tVeckBtjWaOWysuUxNYXaBDVEvDDzBOaGB9V_SYOP5dgdhuFyOKXzocktD7I9MmvY5wEeNWymWTYQlfRC6CfUWw2epsPHhB7SJFQwv533-f1bbrpvrs4YgtYTkTwMCVJ7tKRDUdmWnWyr7dUcg1rE109ffj4iGWeL6DxwPzFqu-XDBq215VuUhiFj2YQ5s5tE19lG0o6hDw1ehI2katQQ1GQSALORK7EI-SCqNWGTISwnnmgkS0YK7Ku26-GfDGokjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه‌کارهٔ جهنم!
🔹
شخصی از ستم و بیداد حاکم شیراز، که از خویشاوندان اعتمادالدوله بود، به تنگ آمد و برای دادخواهی راهی پایتخت شد تا شکایت خود را نزد اعتمادالدوله ببرد.
🔹
وقتی آنجا رفت، از ظلم حاکم شیراز نالید و درخواست تظلم‌خواهی کرد. اعتمادالدوله که ظاهراً قصد داشت به نوعی از سر باز کند و مچ فامیلش باز نشود، به او گفت: «اگر از حاکم شیراز ناراضی هستی، به اصفهان برو و آنجا سکونت کن.»
🔹
مرد گفت: «نمی‌توانم، چون حاکم اصفهان برادرزاده شماست.»
🔹
وزیر گفت: «پس به کرمان برو.» مرد پاسخ داد: «آنجا هم نمی‌شود، زیرا حاکم کرمان داماد شماست.»
🔹
وزیر کمی فکر کرد و گفت: «بسیار خوب، به تبریز برو.»
🔹
مرد با ناامیدی گفت: «حاکم تبریز هم که پسرخاله جناب‌عالی است!»
🔹
اعتمادالدوله که از این همه اطلاعات و پافشاری مرد کلافه شده بود، با عصبانیت فریاد زد: «اصلاً با این اوصاف، بلند شو و به جهنم برو!»
🔹
مرد با خونسردی پاسخ داد:‌ «ای قربان، به آنجا هم نمی‌توانم بروم؛ چون آنجا هم پدر مرحوم شما پادشاهی می‌کند و مشغول حکم‌رانی است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/436284" target="_blank">📅 00:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436283">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da2f1f057d.mp4?token=F6cXbuMM8sBW1dZydB17ZtwxtIMU-G8v86_8zmThfeWTXnHWRbjX1yeLFyIz_5B9lo8Ol_RZZETEs2qfkudw65RMeLHkXOsEmEzkgCQUxW61DevYF_BiD3g1Duq0p89F93YOtcYlNPystRdnrtHEUiiZPKpCHWSeppM87uWKD8kb-yv7_33wROJ4VxpXJCVeiJU6fMOYJK_wFlzjilexibZC34uUekMrxSYB5Zx5O8GmmzO-wKhKe7SKwb8RpvfNYue9-8mgE7ZOVEmV-PPFOn9aCIzZI528iK7wBsaR9_z8I1arndr_Zn3Hn8_baM6Pg-RADLy8hKAmJ1r3YcpVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da2f1f057d.mp4?token=F6cXbuMM8sBW1dZydB17ZtwxtIMU-G8v86_8zmThfeWTXnHWRbjX1yeLFyIz_5B9lo8Ol_RZZETEs2qfkudw65RMeLHkXOsEmEzkgCQUxW61DevYF_BiD3g1Duq0p89F93YOtcYlNPystRdnrtHEUiiZPKpCHWSeppM87uWKD8kb-yv7_33wROJ4VxpXJCVeiJU6fMOYJK_wFlzjilexibZC34uUekMrxSYB5Zx5O8GmmzO-wKhKe7SKwb8RpvfNYue9-8mgE7ZOVEmV-PPFOn9aCIzZI528iK7wBsaR9_z8I1arndr_Zn3Hn8_baM6Pg-RADLy8hKAmJ1r3YcpVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: تامین پایدار کالای اساسی و جلوگیری از گران‌فروشی راهبرد اصلی دولت است.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/436283" target="_blank">📅 00:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436282">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادعای عربستان دربارهٔ حمله پهپادی از عراق
🔹
وزارت دفاع عربستان در بیانیه‌ای مدعی شد که صبح یکشنبه ۳ پهپاد پس از ورود به حریم هوایی این کشور از آسمان عراق رهگیری و منهدم شدند.
🔹
عربستان گفته حق پاسخ را برای خود در زمان و مکان مناسب محفوظ می‌داند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/436282" target="_blank">📅 00:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSus3I9vJLCzwOLf-6E18PKFWjhmkVCEheLIUZqsYwm3rBCAkcrnZun4xp2ffSvKPoG736iOiDuzkVuqkK9jJ37hiS33EFUo-rsz0zFniMfa_Bn1yWKfurIhPvcKNosviC0RiCbLRAuPr7YU25uvkR3jWs-inlHoY4rjd3lRYVl68RxDDbvKIm6MpyKb6wzURAtPISDg7YS3E9nmSrboKnCwL7Tyh6_Xq0MbyAy3EK3oItt6rJszrv-8YHjpTIBY8EkY1vMRuR5q57YORhOnhpB-O_-8-rVXEa0Eu88vLJhmte49XDnWICMiakB7AimqZwQIlqGlORc_0w3y-EBz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoRhjW8sd0Aqp9r3Mv3RRBRNIW0CZf0N-e1OyrJh8aJNuPFpWYWmlYwfPmd4Z9Gzg44kCvqnZBKLZJ_qcAb2Y9dKGmnUCxhvN-mFgaa99GHQd3QD-GmDUQiT-xy26rtTgPFuuvEv6zM2jdji0oyXosvmN5OkdZlyDhgp9sQjHrYEWF3r1v4QvPuoFa7DIPBBQdNrwxMETFLrlX_0aJlZtwU6Ah-1F2V6wLMDUVjh64B1SGWlHBfSKVjIXM_upRARg7lnKQfJE5wn0zP1ybXJfXvjiSzOs_HPi3cNaZ0zIimhNLS5WLuN6aMmDtDW8QxAI5E-tms_VbigoH5DG94Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3JenI_MKu-nvULSagchAiLtHd6gXhaW98cJZYK95Doy3PEsnBl1h9hMC4E3zPm4mYGwWQPEUNDlI8qU0RaNa0WdQAhmivbr1deF0h6VjMTrqH2m8GDQ9Bn-5GD_qX32QfcZuaEStf7sQhiEiB2MIULZ0jEMxnNRPIDZR9LSE1lJU5OwyOdB-x_lvvvrx7ouRZZnRnA_2yVa_QlETuu2V4bfHvO3TDw8VjPsvZjaUDePIy3cUvYdA1pDrnFPUNma6tFDEYC90zeDfRYd2AUvDLREsH519SyYlgY-PvhaH4JZA_2_3wD1LIiXYpQTFEdEeRv5Qmx_q71YnSi5zf1RjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqkP0k_8ngL4lfJitB-bQsfu3p1gmZTt4MqSeuphtyBXPfwjDOSIpB3UUzYgTLwuyKhtKAdBnoVAjeRFuNxucFg5jOWKa_BapSQ8DPuCyZ2SgGMeNHo1nAAuCtV8Rk0fe0p0fi-kjunWTIAELegqfTDL_Ib7osF8S9BZY-NFTGraBO360IIuHkca0KAGOZ368KZ39Axf_gLXRXWS2ic82GHkKyMfuttd0hKLDYpSzm1SR2PgJLmL-YlGBrkb-H_piuyCCdbM0wdFJuh7rLq9eMFsw6gJPxudTf8KlPJ6YIrM-g4ourTN_vvCG_ECDfJup_UFy1v094Tm3Twaq8Ri1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXYL3ix1h8sxxOzWWMFfKsDObmpRTRA6Jllg7i7OpP7p0t1EET1Z8VqSKqaZri_VREeupA6_PxkMaBK4nlasQ1NkyPp2bBAZ_xf9bymRmz_FiI16q8-_9bOAS65bsIe4520kSZMFFSFrv_5pe2Z8cTeQQBmNN1jstUlNOlyGDZEPiwwnOyOUh5Aka51XjDqYy73_WNvHWlVhMPB3chZ31K4cnQvVICgY1DgBRXcFy1zPPDTWllTMJ-3STlWbdT4mU9Dw13GUsVG93gKCwUDDIz32V2maJoDowm8oBapL5iQ45rnCOmcXS1tlR1srVwqbWr3JcXo9tHMeKPL4d1sVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SC4c7LJjBpbxsg2cXUfhptHxTf56NYJuMYz0_7XxegxvVumrtPGHKC9_jfaUnfvY9WC94PbXvHdPAqqGZG_XDcrC11RVTjDx7rCvhV137i6T-YJJNSalBAIuImvaK1BxJv-VqfGDR7z7HSwuTGFVtX7eQgM-NsX9GzlRyotTWy5jTQ214Xw10fUVd9bWqaYFMAQ3g-Pmmxf3jUNDlY2TBKonxklrl_-iVQ8eK2M6RMG6xT6epmqNVxoVO7QpKsF3-cGC2BuJBHvrUohkBNr7r9Sw0j3JsPxHTAhntO6F5XWrY3FX1n1cEfXhCwhCaMOJ4R0slN4M44AaQm1hP6lS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/liAjq4-eL5YRSwewL4Iro6MkuPRu-WWTSMz1vfJep2R32kzX2i8GvHj5H9K42ymceR70fbw2NTJZF8TQV9DMzkt5oM4SjYPUf4uXvh50m9SeY_nuj1KjVDXytC6UjLuCri4220K0t2eho1cSwW21akgPe71OIDfEE6oRa7vz6Y2dw_h-o5c7nY6nj46AnM4O3guKqTcAts5hFJooefGXzadp7lQILDlAhiOx2B0gzFoSTooPt4qb_HQeeSSgG7-5E8EJArZ2Zp5z8SJsTAfkWxVnaxSCfo7qPy_CcUnDQrj7-FCtcC3Rv26cZwMQwcTy6PdvXlgAZgQUQoW7vSV37g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
موسم برداشت گل‌محمدی در خراسان شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/436273" target="_blank">📅 23:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa34ad2374.mp4?token=o1b9I_6mPe8Oy1YObnKl8sexmYcK7SGkkBbuj-fW_TrGOBPI-yFY5qSoYe1rDi_-HwIkDqZMKpfIopPLu_msNLywfhoKiR-4bd2SAJsrOL2V3WVx7ef3EDDEnUQO22_T7izrhpWwQE4OtjX7ZJpGvgqvW6N85Q9PkOj0kPVmhuwBf0r_Uxx-5BR3GDvGJ9Pxg5UOF78McXUwCaJaLmtUOsLZ3OK72Nnp6I3G4wJHuxmhBqc5p7XMNpfIgNI5eFnAlPNy9grC5qzZTQu_eyLs4Ry3e_Jnch_HIYWI1Tm9bXwvTs1qJxNavw8eIjDY8cqngF52ZvVeiRnvk0TblE9GIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa34ad2374.mp4?token=o1b9I_6mPe8Oy1YObnKl8sexmYcK7SGkkBbuj-fW_TrGOBPI-yFY5qSoYe1rDi_-HwIkDqZMKpfIopPLu_msNLywfhoKiR-4bd2SAJsrOL2V3WVx7ef3EDDEnUQO22_T7izrhpWwQE4OtjX7ZJpGvgqvW6N85Q9PkOj0kPVmhuwBf0r_Uxx-5BR3GDvGJ9Pxg5UOF78McXUwCaJaLmtUOsLZ3OK72Nnp6I3G4wJHuxmhBqc5p7XMNpfIgNI5eFnAlPNy9grC5qzZTQu_eyLs4Ry3e_Jnch_HIYWI1Tm9bXwvTs1qJxNavw8eIjDY8cqngF52ZvVeiRnvk0TblE9GIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین سرود ملی در موج ۷۸ تجمع مردم لردگان چهارمحال‌وبختیاری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/436272" target="_blank">📅 23:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60755d3540.mp4?token=WYImuCo4TRVyt1SJnQlZFPvZom3TD7GIXQDt0pVUThMusd24qeQhlYH9Js9z8vbwlwUzfszSuinG-bjYE63OsDh4rgSOstA3NvgsqN3VtnrJvFpA0gCPsM-RPN9xvIioP012_Plcoyn46umUiNgkAd1Gku_sRIfg72CSH3NXv1mN45bM7lRuPJylBuhO2kMa__hSh_xCeljG3SMqdTwaArcnYZi3u7V6lBDQQ54zZzKC3ko1gONBFgycTcEfdDMTU9qqAQdAQ8V2I5AKi9d6Oc7bnBiwbLMFAHKS7_vFvqeoMq1LlCD8x8Gssv6s70BVae1B8l96eT4UQS8tY4GxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60755d3540.mp4?token=WYImuCo4TRVyt1SJnQlZFPvZom3TD7GIXQDt0pVUThMusd24qeQhlYH9Js9z8vbwlwUzfszSuinG-bjYE63OsDh4rgSOstA3NvgsqN3VtnrJvFpA0gCPsM-RPN9xvIioP012_Plcoyn46umUiNgkAd1Gku_sRIfg72CSH3NXv1mN45bM7lRuPJylBuhO2kMa__hSh_xCeljG3SMqdTwaArcnYZi3u7V6lBDQQ54zZzKC3ko1gONBFgycTcEfdDMTU9qqAQdAQ8V2I5AKi9d6Oc7bnBiwbLMFAHKS7_vFvqeoMq1LlCD8x8Gssv6s70BVae1B8l96eT4UQS8tY4GxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام پهپاد آمریکایی در یمن
🔹
برخی منابع از انهدام یک پهپاد MQ9 ارتش آمریکا در آسمان استان مارب به دست نیروهای مسلح یمن خبر می‌دهند‌.
@Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/436271" target="_blank">📅 23:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dee5d0d6c.mp4?token=lSXbJfoYnt-JX5KVmUzky_NLoSgyHUE3pDKL-St2NcsqqhB0W8mH3f2zaYdN9BRDJAP8HWYyU_rqdwB21kIeNz9MeHkSwkUfpmura4rxP_o1uxCep-8ZppS2P25NBgIAUcjf5mUVhZ-XM5ibeJwwZgLnv37yCiU77pHCPrtSNQJ-hJ1TlxitNoj_tiRhHgUDDIVXRRnI45WrY1YmGR9cQcnEDXGkPm1E0hkNUM2eDWn6XpIcsT99m1OV4IaCXyodOgHYSh071JhPoQB4uV1s6gRCGF5x9kug_zfF9E5ppo_tKdL4xHvXhsjMb4he2HyU9JPl12vjpfiQw-aowB9qOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dee5d0d6c.mp4?token=lSXbJfoYnt-JX5KVmUzky_NLoSgyHUE3pDKL-St2NcsqqhB0W8mH3f2zaYdN9BRDJAP8HWYyU_rqdwB21kIeNz9MeHkSwkUfpmura4rxP_o1uxCep-8ZppS2P25NBgIAUcjf5mUVhZ-XM5ibeJwwZgLnv37yCiU77pHCPrtSNQJ-hJ1TlxitNoj_tiRhHgUDDIVXRRnI45WrY1YmGR9cQcnEDXGkPm1E0hkNUM2eDWn6XpIcsT99m1OV4IaCXyodOgHYSh071JhPoQB4uV1s6gRCGF5x9kug_zfF9E5ppo_tKdL4xHvXhsjMb4he2HyU9JPl12vjpfiQw-aowB9qOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رقص پرچم ایران در ۷۸ شب اقتدار در میدان سلیمانی کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/436270" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b69b398b.mp4?token=Jo882VMW_s9WbkNTqrh0o73bbmqxG_-jary7LWbqoyabFgVUzHW--ATaljhCA2HuSy3lfK5V0F5wI6iVcj7gXSdspitGNfrE4kFFHJdyd_Jwt2FGpCXj6WI6uDthGMk4BUV1TgvtaL1QJPNQ-gEJMBPEEO-5BlalNfXTgov9hPJanhfdoGK-W6vRtGRzdBe50DBikWKinjcKCnxzb5ddk7vmLZJqSMRgLLm1bdiI3LP9IJaynD2fM0ZJIHnjsOYXEn2ASM1-nvBe7RGCkriX4cMeWU6Ixb6ceIs8zOZLQ6pnHdlpt2Q6aIsn-8K-0xlL3WmcQu1sKwNrb0JaRiJ-YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b69b398b.mp4?token=Jo882VMW_s9WbkNTqrh0o73bbmqxG_-jary7LWbqoyabFgVUzHW--ATaljhCA2HuSy3lfK5V0F5wI6iVcj7gXSdspitGNfrE4kFFHJdyd_Jwt2FGpCXj6WI6uDthGMk4BUV1TgvtaL1QJPNQ-gEJMBPEEO-5BlalNfXTgov9hPJanhfdoGK-W6vRtGRzdBe50DBikWKinjcKCnxzb5ddk7vmLZJqSMRgLLm1bdiI3LP9IJaynD2fM0ZJIHnjsOYXEn2ASM1-nvBe7RGCkriX4cMeWU6Ixb6ceIs8zOZLQ6pnHdlpt2Q6aIsn-8K-0xlL3WmcQu1sKwNrb0JaRiJ-YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: وقتی آمریکا می‌گوید ایران نباید دانش‌ هسته‌ای داشته باشد باید به این موضوع مشکوک شویم
🔹
این شک به‌وجود می‌آید که نکند این‌ها در چند سال آینده کاری می‌خواهند علیه ایران انجام دهند.
🔹
ممکن است بعد از این بگویند ماجرای هسته‌ای حل شد، حالا برد موشک‌هایتان…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/436269" target="_blank">📅 23:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b4ca0bb.mp4?token=UhW7XkUZ7iQ1RvrpLMu0la3fXYlRN9Z5al502IvxTJijDmy9gOOJ-qGnrISbxdSmoWAb5KxUJIA7pIf2LEwYMp0fS8O48WfW_uieKxWiJm3HHE8f2j6KjcqWYK72zSwpAshaAQfzdUtla-hApvBF6sRQpurNXYSr74iM9012LzsebJl0wL2UeWOi_SVWX7nzQ67egnbIemSNJlidBEqV3cRYRr4jMM4MLBHKRDGI-tUZtmZlOme70noA-m3h3apRoD07JljPOUBRddntfvkiw2zWeutfxOXg1eqK0DAnVCqTz5EfCMf4K9JxHlP1uaMJ18iAi2lcEMoXiEo-y7v3YZ0oN66Crz9aqpOKIzkNSWhAmuVbm36qywt6XSMGlFgZQE1PGO8LWf-AliuEIVNsv9DydB0YtOFq9vs78Czba373y5FnxWuiuC62H2rWLl2iEBK9qYuY2qxac07KjgIRnB7YRdolZZLQkoTZ7FsjhOJB4U18TrboSTU-9-b6NFZpWkJseMZFL7smxneVXn0-7xgx1ZfVgdVXNiIXxOHUQlPUVLDURT_ZwANDfVQo8xa9YBzJe1_FoUfLbpb9sJXYbRPnvOH6C_6LD6dPlK00hai97RDDKK90V-6kxW8LaDUKC0py3tf5AJYTAyGh7hOtIkHkVdUr6ufztiS_AGCGVwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b4ca0bb.mp4?token=UhW7XkUZ7iQ1RvrpLMu0la3fXYlRN9Z5al502IvxTJijDmy9gOOJ-qGnrISbxdSmoWAb5KxUJIA7pIf2LEwYMp0fS8O48WfW_uieKxWiJm3HHE8f2j6KjcqWYK72zSwpAshaAQfzdUtla-hApvBF6sRQpurNXYSr74iM9012LzsebJl0wL2UeWOi_SVWX7nzQ67egnbIemSNJlidBEqV3cRYRr4jMM4MLBHKRDGI-tUZtmZlOme70noA-m3h3apRoD07JljPOUBRddntfvkiw2zWeutfxOXg1eqK0DAnVCqTz5EfCMf4K9JxHlP1uaMJ18iAi2lcEMoXiEo-y7v3YZ0oN66Crz9aqpOKIzkNSWhAmuVbm36qywt6XSMGlFgZQE1PGO8LWf-AliuEIVNsv9DydB0YtOFq9vs78Czba373y5FnxWuiuC62H2rWLl2iEBK9qYuY2qxac07KjgIRnB7YRdolZZLQkoTZ7FsjhOJB4U18TrboSTU-9-b6NFZpWkJseMZFL7smxneVXn0-7xgx1ZfVgdVXNiIXxOHUQlPUVLDURT_ZwANDfVQo8xa9YBzJe1_FoUfLbpb9sJXYbRPnvOH6C_6LD6dPlK00hai97RDDKK90V-6kxW8LaDUKC0py3tf5AJYTAyGh7hOtIkHkVdUr6ufztiS_AGCGVwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها امشب با شعار اقتصادی به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/436267" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g61E_WpTFgNyfHUoj2lkYAKAvO5_3d7nSOKaxNGw3rlPPc52WTRzgn1gyflZULH8C1jajEJvKRFO7aIHGnQn3JnVHRdbtJ4XYgd3hyshWE5TxtEh473o_lrKeL0WRgRRGLuGwhB0tFST5oMnm4_uldemTw5Bw4O-vHY8l4ElSr1v4ewtCSEU3GqxiAAjAsG8tLdn11hbSkrayX1Ra-mpJ98xFkGT3TojS-ZL5PfU2E_hYjyjW36nrbGnCnz4jiYj9vLlQp6b0vAl1BXBFh-tvqM19FtMAIfJT62GLp1flEfL3Td0Yz3CUy3if9fxPEf_o2nIs5FLKruAEWoZK8nVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزینه‌‌ انتخابی دولت برای مدیریت بنزین در پساجنگ
🔹
درپی آسیب به زیرساخت‌های نفتی کشور، افزایش مصرف با لغو دورکاری‌ها و اندکی اختلال در مسیر واردات، دولت مجبور به گرفتن تصمیمی برای مدیریت مصرف بنزین در کشور است.
در چنین شرایطی دولت ۲ گزینه اصلی را روی میز دارد:
🔹
گزینه اول: افزایش قیمت نرخ سوم بنزین موسوم به نرخ جایگاه (براساس مصوبه سال قبل)
🔹
گزینه دوم: کاهش سهمیه‌ها بدون تغییر قیمت که طیفی از بدنه دولت آن را دنبال می‌کنند.
🔹
طبق موضع رسمی دولت و گفته‌های معاون اول رئیس‌جمهور دولت قصدی برای افزایش قیمت بنزین به‌عنوان راهکار اولیه ندارد.
🔹
دولت درحال طراحی بسته‌ای برای مدیریت مصرف بنزین است که در اولویت آن، افزایش قیمت قرار ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/436266" target="_blank">📅 23:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔹
ستاد استهلال دفتر مقام معظم رهبری فردا دوشنبه ۲۸ اردیبهشت را اول ماه ذی‌الحجه اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/436265" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
۷۸ شب است که قرارهای شبانهٔ مردم شهرکرد ورق می‌خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/436264" target="_blank">📅 23:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎥
۲ جنگنده آمریکایی یک‌دیگر را سرنگون کردند
🔹
۲ جنگنده اف ۱۸ نیروی دریایی آمریکا در جریان یک نمایش هوایی در ایالت آیداهو، در هوا با یکدیگر برخورد کردند.
🔹
هر ۴ خلبان موفق به خروج اضطراری شدند، اما هر ۲ جنگنده سقوط کردند و منفجر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/436263" target="_blank">📅 22:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436260">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎥
محسن رضایی: بسیاری از پژوهشگران عربی می‌گویند ابوظبی برای عربستان است
🔹
اگر امارات در جبهه صهیونیست‌هاست، پس قبول دارد که نقشه غرب آسیا باید تغییر کند. آیا بن‌زاید می‌پذیرد که ابوظبی جزو عربستان شود؟ @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/436260" target="_blank">📅 22:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436259">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
۳ نفتکش ایرانی دیگر محاصره آمریکا را شکستند
🔹
تنکرترکرز: ۳ نفتکش ایرانی با ۳ ترفند متفاوت خط محاصره آمریکا را شکسته‌اند.
🔹
یکی موقعیت‌یاب خودکار خود را خاموش کرده، دیگری پرچم روسیه برافراشته و سومی از خط ساحلی عمان استفاده کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/436259" target="_blank">📅 22:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436258">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a645ff3278.mp4?token=Hr_7B7AYm6froDILoxycQIqMYELXPYpZXzyTBa3c0B7S_JFmwokvPpKZOkr4tte83r0EvmMXz9kWUkeAorfIJu3NKOcVQq_WsZYOk48N_FBPBYJofE6qOKoNjt9xaJlDhWVuNK9tWuWnfgEW9wwtAF5ewzgl8oN7MRBoQ89jFyJ3GTPqkfQa0YX3pzxs1Fo8F_Q5FIDkGa9acLUouPyi-XR4cpgiZEN0Dt8JXtvAA3N4K52gGYZQjZTT6uodtvhchcwCjFdyAITFUOzeME5GIJkbIPNB2UnAKTsOnb66Grv01kx4Yno1d73b1Jx51dTkyrNgWidHRKWmDG6QCnPdcnJ8urmnekkY6Pwi2h_oje1PMkYp39ulGTnqHGlIUdk4MGz0Fsuqh3FLE4zYKMHpQkAhc85bEPcaExySvgqWg8qyj98Vt2_imofVgkIJ6LmAiD8Cg7iQnCtKxs077fkcXU038wYWwdLa1wF7-9NfdNJay9UNs4B3cBNkOhzMGTM4es67nKZYP9n7AEDTJ22ht7BObtXIFPz63t3h3nuARILTuEgFalk7inqvMvc6mrWqHOkZuhn_fqM-ib4ocex6WKS208APvwvYECzYFhc1pwNzseqFryGD8OcJ4PtgfF9HE-s1lsDLlJyRiZ0Fh-KiJJQSgt4vFtt6YTubcMxuJ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a645ff3278.mp4?token=Hr_7B7AYm6froDILoxycQIqMYELXPYpZXzyTBa3c0B7S_JFmwokvPpKZOkr4tte83r0EvmMXz9kWUkeAorfIJu3NKOcVQq_WsZYOk48N_FBPBYJofE6qOKoNjt9xaJlDhWVuNK9tWuWnfgEW9wwtAF5ewzgl8oN7MRBoQ89jFyJ3GTPqkfQa0YX3pzxs1Fo8F_Q5FIDkGa9acLUouPyi-XR4cpgiZEN0Dt8JXtvAA3N4K52gGYZQjZTT6uodtvhchcwCjFdyAITFUOzeME5GIJkbIPNB2UnAKTsOnb66Grv01kx4Yno1d73b1Jx51dTkyrNgWidHRKWmDG6QCnPdcnJ8urmnekkY6Pwi2h_oje1PMkYp39ulGTnqHGlIUdk4MGz0Fsuqh3FLE4zYKMHpQkAhc85bEPcaExySvgqWg8qyj98Vt2_imofVgkIJ6LmAiD8Cg7iQnCtKxs077fkcXU038wYWwdLa1wF7-9NfdNJay9UNs4B3cBNkOhzMGTM4es67nKZYP9n7AEDTJ22ht7BObtXIFPz63t3h3nuARILTuEgFalk7inqvMvc6mrWqHOkZuhn_fqM-ib4ocex6WKS208APvwvYECzYFhc1pwNzseqFryGD8OcJ4PtgfF9HE-s1lsDLlJyRiZ0Fh-KiJJQSgt4vFtt6YTubcMxuJ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: محاصرهٔ دریایی آمریکا را می‌شکنیم
🔹
صبر ما حدی دارد و نیروهای مسلح درحال آماده‌کردن خودش است. @Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/436258" target="_blank">📅 22:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436257">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4a9d33f9.mp4?token=k7SczZJVuVN8QNWhlQitoXHOtN9CFrXYy4XzfXinPbjQStQIJuA3Rj7uONkK4IvjJ9-N964B2vGMtjbXNCwRaqbsukZz6Xe98crVDEXSXDdl1XpJy98JTzQTwCd-mc0rfxhId1GWhyYOUnmSf6vICYYmrD-GW_KYPPgAG-N_vx4rBZHTmRLzpWFfUUaphOiNwZE-63J-kMoLP6dMRFwiqdtxaAlajZ9dZVM3FygSDZiXsYn0OVYh0lLyRFNbakGazbGBXx7OOB9rNQXiXNONsFeeVy0wSUm8P7moCoKHBqFXSm3AkOw_6VYqY2i936KbU-NkBw4cfxjWDhO5FLop9Z57P3y_-Ldp77rsj9gs62Ry6EnbiuGQaXdGD6_jC9eIIXZrdBy-nxalVFsBv4XJ0oN2dmE6bTgO9-b1AaeYkDCGdkbed_0-dJcUB_156BQ-E6ELBktlSkFToU566BAAANoHHkVVHyAts-I_2zUMa2SoewWimOhepQ__WlL6oFbqTfY5IiJD-57o6rbJtDPn7987okpbQQMzQhJ2wqshxw456eSTui60CJ1qsEh8KmLGaOpgRTEmbyE7Sn8M8ReC5_A5QKO6mNJUk3mXouJAh0aewQ19Gonekc0Q_ZdRhJAli0OP2538zPPNitaq3mficmV7AG-BhB3oj6n7brBtAhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4a9d33f9.mp4?token=k7SczZJVuVN8QNWhlQitoXHOtN9CFrXYy4XzfXinPbjQStQIJuA3Rj7uONkK4IvjJ9-N964B2vGMtjbXNCwRaqbsukZz6Xe98crVDEXSXDdl1XpJy98JTzQTwCd-mc0rfxhId1GWhyYOUnmSf6vICYYmrD-GW_KYPPgAG-N_vx4rBZHTmRLzpWFfUUaphOiNwZE-63J-kMoLP6dMRFwiqdtxaAlajZ9dZVM3FygSDZiXsYn0OVYh0lLyRFNbakGazbGBXx7OOB9rNQXiXNONsFeeVy0wSUm8P7moCoKHBqFXSm3AkOw_6VYqY2i936KbU-NkBw4cfxjWDhO5FLop9Z57P3y_-Ldp77rsj9gs62Ry6EnbiuGQaXdGD6_jC9eIIXZrdBy-nxalVFsBv4XJ0oN2dmE6bTgO9-b1AaeYkDCGdkbed_0-dJcUB_156BQ-E6ELBktlSkFToU566BAAANoHHkVVHyAts-I_2zUMa2SoewWimOhepQ__WlL6oFbqTfY5IiJD-57o6rbJtDPn7987okpbQQMzQhJ2wqshxw456eSTui60CJ1qsEh8KmLGaOpgRTEmbyE7Sn8M8ReC5_A5QKO6mNJUk3mXouJAh0aewQ19Gonekc0Q_ZdRhJAli0OP2538zPPNitaq3mficmV7AG-BhB3oj6n7brBtAhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن رضایی: یکی از ۳ ناوچهٔ آمریکایی که از سمت عمان وارد تنگهٔ هرمز شده بود بر اثر حملهٔ موشکی ایران آسیب دیده است و آمریکا صدایش را درنمی‌آورد.  @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/436257" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
