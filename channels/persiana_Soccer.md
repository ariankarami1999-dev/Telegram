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
<img src="https://cdn4.telesco.pe/file/uS6TEvX0AbxU5_4YZmbrIq7ZkWqdW4qxEZ5NeWkd99gmsj0ktVpBvCR8-CLPxXIeYF3jhPtBYaNBp4Z17n5W0Pv5sDi1M0Z-MrCjfg6-tUJpxaOgxILINeygu2W5ANrANIqkKhnvfwDCwg1jOL10pfJrYhAwX_WcoF94aKARMQAH3qzizQkHbN3JBsOCRu64qV3XhN6M7zJ_jSElJh1Y7D0u4CehuOcnIh9rHLTTFeuDm2gpyvaKrG3J-4jABfx--m1klgMVTEUBz4OBm027v9mOjU8Xi5T5unHeHYwcZnl4AwcAOpSdS-IY7TMT4dr1CfIhqp9kt2fHIE9he9IczA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 188K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsBJEBq9kXYou_GdvGEokKh2cjeZWO14SqJ-zryTZxIDmJljE0-O1MwzTpHVe995mz_Xe4d7Il9YKW1sv8FOrEdbVN82M3S1vx6pEZyK5U2g5Isa8nQ5C-K5dXpUYbBDbC1iU6uRbuPkGuy6RYCcZqMafpBq7pPu-KE5UQyg3LZoqGLL_fmlOTgjBItpd_IXStkKfhsIFcC8UjDOWYKKjVU2FwdpzSTJR2jlCm3HQomQn7jl1_8AY1YHwmejZ2F1iOJ8ksSkPNkAK_o6qAqNbPGgubjyzhHCjFiIeA6y_oQuT6o9QiOEaKTa4G2nLa7f74ceUvAqTO3k1WMJT4EQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkT4RhI4x1O1Iq7KBrO6BJEjmqhFkPuZrRzKk5ekNGSHaJTXQ_kFgIRi92Qoma7al_RgoLVL4WfcMxE3PqUeXP4pUHDK1frNi3g-bmKiyyezyMzxrl8ulob6UDXdMXcjbxVEZe6sd_SaBC_XCCoQg22X6UQV9pn9-UVaksUjrTkatX9vecDLz5vBbRJoQY6xVX5QHwufJVJLiWanqp2caZqsRDGsvJgDPgbecDzVmRUhd1d-a2ScvXq0weLBT_MRB6eZ-FIRl4HLT_XqmX8NlbOKXH2aeJ0erejAKjPv5AvY-u_ag7WbCUmKcckYH-ab16WryjEtPwJBvMhoBP9yNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljRElpNqKVtiH3LlhNdz4M2uGz_uGQQxXz_zV_FubXynIxhQ5NTmUoERJXyzocsmoaKGDcDUWgdpZA4kupcIHhnFJpEo7_8HEFKfffB0XTo1vjE21unOHX6pkMJjs-nTl6KbcGXlcMxlEt2ydX6Vt7gb0rw4LqxHVRg7UdhK3Pt6t3GlD_z8Tfj1nc4IhxhKRRNWf7qxeI-2ParPgvAcVs-Tzlp7LIeTX0tygOiESXlp61exoUJtgU2eUTuW5NCe6ZvkhJJm_QjZcpkBLZpftuppgnadqELuvl5l1KDnTY-wCzSZkirvYSniFT_mJ7NODxJtQvRIJr_jM5TleE2nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlvUWY96dGhwyxHUXyL7H95kmaBc8JGLjBiYm82swTjJDtk6c6l7gZWSdDd6sIHWAiKxHz7pkEGV-JF7jd75TMDAEyutRSr0xgVijKi3dSfwPTKs0sTpJ0hZnMPi-EQQiQtpNCXzF0BYanYXx7wOH6uGNj593nHC7XBQaWAyEM9TXbJ7hDvka28FeCyAVeQccd-tBE8p-NJSsUiRJpdAJegKyoEy6_yWduvsjhuSRWyxIxLdiNyAcJ6dzVdKvtTo_pEoLxEv6BN7aHIEp-QhqrTv9Ye7p3HU2pCeJb12Chk6pUfXsMuhBZf6vngy4wXZwcZP5TPXJXT1HbYQF4R_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4zedjt3e15udnZJXO4iVMyVmmTdhqiXGLF-FSmwvgCK0hGgqp3LZT-HelLjSTYB6FUd_0f_SBcWQZXInq1FCHzzM4bNw7LWzkF6kZB-tq5juYVsYaXmKeMK0f8egd-iVlAL0QA3PfPIqzuyws7J7eE7X6v7ueQi-hbO2xzB40BAJ6zqijVZHv196ltXYGPLKj0Ya3KR_P9dleu-nhhvWnubMdutQqt5vnY_m08RwDY0KnvHmYCdKfzGvQQkjFA-f6INIPbqk_gwvpZtM_kZU1gbEkQnYkEdbMsvQEi5oc6S5kVeQC_AezMgSvuyinPiQrTZx5dqXiOiutPyXA2ekg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان‌جایزه‌بده نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22337" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=Kbp9hojtQ3Q1FnPX-V1AYDVexIl2Mbs1pTr1ZwSqeo0FWDhnWD4diGI2ci2jDQbwzfsmxkhbMJ4iPn4en1TQqu_JwhA5tEBG_YRwBsOO9hku-9xNorHtG6WfAji8EwrAXqT2UdN9RYFxWbcpk0rWDT3_HEIGAhhMKQ49TSWqEgFm4ZdFY0f6g49n_xqbjvjMJNHJDCB5tR-E1K4TF-ZgtMf7eE5scn1BcMKI-rseR-wSzSMWa2vCfD9N8f_cM4XoC5uza7Wiplx-N5mni2V-eDLxkYW57W6r8A1keMEPH-5JqKnchzEGj7isvtC1cmL5TFXIHU_Xs0JJzJEep844pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=Kbp9hojtQ3Q1FnPX-V1AYDVexIl2Mbs1pTr1ZwSqeo0FWDhnWD4diGI2ci2jDQbwzfsmxkhbMJ4iPn4en1TQqu_JwhA5tEBG_YRwBsOO9hku-9xNorHtG6WfAji8EwrAXqT2UdN9RYFxWbcpk0rWDT3_HEIGAhhMKQ49TSWqEgFm4ZdFY0f6g49n_xqbjvjMJNHJDCB5tR-E1K4TF-ZgtMf7eE5scn1BcMKI-rseR-wSzSMWa2vCfD9N8f_cM4XoC5uza7Wiplx-N5mni2V-eDLxkYW57W6r8A1keMEPH-5JqKnchzEGj7isvtC1cmL5TFXIHU_Xs0JJzJEep844pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quIpiXLjBbZLHTjMhKHwE15VA3yNkcqsM7KMkwHTxtzt61szQyxbt5Yq2w366HptHrPqKAtER6CJMbiIknK7Jgvc4N15qPjYn42-WCUYciD6JW0i1DZ2FTLSDxxGP5DBuo2YaGBfBH1mNbO2JwGS6uAHJsBVUjJO6BSiNj0VNcCFAbRbiVEsVh0Jt6Z6AKmq6hVtZiJbSHgyk1VSXN-lNRJcp4hAPndz5IoVfQpwM2E7VPIikq9aH92TsVhpsKDWvHSLXnBMgNCpMQIz97UBP08K9ICuGeNcAQiIypcKiw_bUbgqmX9ZvUueAu3XUgHzOhQkYCF7Jz-E4Uy1xBQUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVsK0VzXbXrtj-C_n18q_81z1CB-8peCKvlPxe92itfMHiblWwyP1HVKMdj2Uu4xO3QbF9LJFYXYG05R8BeYcKXBsA4GH0jTgFZ3F8cOS--dxsOnAbrZiLDgVM7jE9fCqjAx_P7J2bsGin4sV25XdzmfmewnWl1e-wmg1JhasL8W_2Eo7wQC-QB7cCf1M28GybB3u-kfD82iFWd9y7yP2_taENUGdtETRcCy3Gm3Pbn9kalOnivyXn7ObKisanL0EH_q-OLeN30ak3tracMhmGevab87VelB2jN7yftVkviF43XU8yyRGqjFoj2nS8xSbInpCZqmPGInMCcKDErrqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePh49sNI9ozXd7EDAW2gy906hJDaYgLUtL72KATSAVsIbPYTZ5dIZbNmXMvwpS6XP775l70wg42nFbCOu_a9hpXUK7karyibpzBoNMNiZMhlERqke1s1rEsBfAXn50c9D6wzAlyvV7itvjDto_Ak47lQuTJz_OO__pDv42fLsmW3sFcRFvMhMT-9nE9oXIgmRCexXtGJttcmkrDgcpoj1sZh9YfbvjQJ-HRWZdKGs5yPCMVnGLbPPZ7ZD9Zh2_eqTAIZdoce4ZvpOH1ER-x_Ji80y1XGTDzAay00I-oYToZZskvprTtUHGUp6Pp44KN1EdYBdQPFgXUvinrPPqBuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wya04iMi3fDHwsikLbPkR8YnCX6PlohI-NJnFMdsPynAC58CzA4NBiPzg7WSsf0T_VJHv76B2AAceP3wK8nIsyBZyRdzMO0GVEU8rFzQsU5qLAstz2wCinbd4els-S60jSP93UQlgpWp9hKeilcaXo4ArEXVms4RMZy16nTvjfIwHaTEzx4d4yXfr15rplox0Ai-Jbj25XlV1w3g32rYOhws_d46bDPEGEZqjtyZSiyNHqa3uaQrUiR6kQh64ZdUXW44QgSurELGNdKBXo8zxqORoIodHHZMHdZJEuqTIUwtjUKinALNca1hiSNzyEtP9lTEM0wDFAiFH_cyO5OwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-avINjLw_pNn_G0Ufw_TG_HP-zz-B1ct3yH-6RqGJMSllQuVV7uDH9zSlUlS5gESZclFgFdifyjqk06JTUhHrdODDlQwii-O6QDwLrC0o5XoS9Zq8lFxJgAuEBG45zvALb9rkHB-LKH9AeL9KrSmuTlkKfhONxCIGSRlgDlyYsjbiytwsA2FUzdQewXolD0dFcdNsGnfSdkj_mIxtgcaTJc13pPuUMq03WiIrcLcLKr-mW-Dq6uO_OYBHiMwiKP1015DTbHsPkDTiEpnQJvWAdPQqg1MpwpT95ylmkaAuYdncBtQVWVFJZbnLbXyRQNO3IMMEyB6EIaXsORtZyBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt4-wW8JaghtjHkTrQ-xTLLArB4-QBVK9GYok642ZAsbVxDfs7IijMq7UsXkjkRWCZMp1BJA6hOetI4NwO44bKJY3JXp6dCeU4aOt4VqU3d5dHDMYU4ZSUts2ztiCz2C1W2pFLMAM-iwE8RnzCnzkcVXY7j_nfxdBhlZicCiil-D_o4l4veXtnpvqJ7olG2vjOv2ne69nET0dkK6LWMfizfqmu2C33l6lBu17vAfj8junVmy2QYbgcc_4L70vTboxf8J1IO6mjc8EfbaeXbP0I2S14iT6z_Ma2U8VYgIn9anEyc5ZdeHztuWGhGBsvyeMkY_uOOob4HV-IkoL1mZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndFq-HjEsF5sIzzLrENNpiANQK2p8-04ngCErs4OkFkYfGCblu-iqmJETXt7DUkxU_x3po-jRIcJ83euvJ6SK91phIT15G79ca-uhgGk7fAacrMcHzdbDukY76zJ79Ip9gq8VSQzuSndMbUJYSnEWyDfowptbk8LqI8sXg-481t55D5eNAuh3kAlCgjyIsALfn_C-KOTrwBDsMlLKGhDTpyL3fgT8WNGk7JJBbEDKJxonqLF0Mz7eZO4v7pE8GwR-EeSbaobK0Iolhg2xTS2dXQw51gAhQZZAsfh-jJAgaJXgfwsJOeI9Bb49ZbPYKheDFAChWuCvr4V2m0vgxTC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=corzCcqP3mFwWMuW-54Io3jNfNo6tvXCpuHGOinYdDJCtytsecibTV_M92my0ravoBgvsLszmQZbAq1-0K60X_KXcnfLoUL0jP7OSSzzvS1VLuGeXkBdIe-dx2vSpfFPJDRPxk6XRA6s-c2vNB7PNyNmwDHObRe3P-H3kVABK6FuXaXdlA_Et4rg__WLTHnyOSEdXdPnj_gSCmZ6h7Ax3ug_G2IRh4odIDeWWvHy3WeVwHt8sdBfTVIKWeRl-Nz0r8UpwN600oxQMFh9xviyKy2ZEgC7uRbO-avsxl5N8NFzVnJ2V0BKAJmsclTZZSo2f-7kcOP9Tr0vcZgk-xNLmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=corzCcqP3mFwWMuW-54Io3jNfNo6tvXCpuHGOinYdDJCtytsecibTV_M92my0ravoBgvsLszmQZbAq1-0K60X_KXcnfLoUL0jP7OSSzzvS1VLuGeXkBdIe-dx2vSpfFPJDRPxk6XRA6s-c2vNB7PNyNmwDHObRe3P-H3kVABK6FuXaXdlA_Et4rg__WLTHnyOSEdXdPnj_gSCmZ6h7Ax3ug_G2IRh4odIDeWWvHy3WeVwHt8sdBfTVIKWeRl-Nz0r8UpwN600oxQMFh9xviyKy2ZEgC7uRbO-avsxl5N8NFzVnJ2V0BKAJmsclTZZSo2f-7kcOP9Tr0vcZgk-xNLmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doZvDeKRq1HYJH3WmTIqrQGFyEEmmpajclCGbD6H44ZQ8M81D5RhwNRkiCP1v3k-tNjjbFnVuYQGIXaN2CZSkB9hNsgKDyuTCbAsYS_EF_dUpca42llWmUDOQVJu0bTTPQz2jHi7SAXmWymYwZgIW7sZiIbibpBKMhMNnApcanbv5ZcEj5CftQib4fHQpMF6jeyLdr9995Mrqb2ZH25Gr4K-rPfhnVhrAg2D4RO0iIorrkRbMB1VMFbvG2kzNb45_V0nQ7zX3kydOBuzqA3qHZfwtJBcoKy1FgcSIpxYWL3DYwwJQPXRgZLBMPVNDCoqzBIg0igsOBUXKI8cVTdH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_aT9-NHlli2deICAp1dseGPytwby--7gPHWk1Mi6-45i_UNMdhO_Xl_vfLIiFlBOaHCTToAyadGnCDJrFJ5tFkN9zof0zyt6IiA6sZjHhtru0xlDTZL0k4VHMDlMKmN50a1x7KC6XkGh5VP68g-4CDXU4oHmsWW-c6cNQeJhw7Oz-tNp9aEBYotWUDvyCVUF_Cbv0UZb4Fhy2UFIJIDxNZdzAn3rYVTeUaAzk1iijsJFvqBxqiQZE0aIgGhSCV1dx5Wd8HVB4OMvt756UI6p3RQGlpstZzcr9bXeP1bnBSHCPTGnAuozO4g5TSAsOIb-BS_S-NXPWfz_4FJZ0mUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=K8ufDeNRJg7n9UNm00oFyTi7SU1j72jMDt2wjs03nJdmoMAWT2TXUpCvdxe5xokza6vQtmorTruUvoElNyadjB-bJnabgg1-J_QemsUs6v9gkhwmzKJeqVkZ_RIE9mr8HbIAKPRDvGKrNSoaCAaQlcURvDgTSlcz8T4xcUJI-Ves9uwzTUDXY2cTNyd418cpQbUlOWar2W1OGyHADoVvmI8O4kWN9FBRxMQCzabrxMbzjNugkgZg1xDJxMK7ZDq9y1MK1jopjW39sxLCwJMTEoN1hZHl7zDrhL_C_xbUcSNs5Y8uI0uTYRc1162J_zFfvCp60e-zxt0UvbTqH_fDDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=K8ufDeNRJg7n9UNm00oFyTi7SU1j72jMDt2wjs03nJdmoMAWT2TXUpCvdxe5xokza6vQtmorTruUvoElNyadjB-bJnabgg1-J_QemsUs6v9gkhwmzKJeqVkZ_RIE9mr8HbIAKPRDvGKrNSoaCAaQlcURvDgTSlcz8T4xcUJI-Ves9uwzTUDXY2cTNyd418cpQbUlOWar2W1OGyHADoVvmI8O4kWN9FBRxMQCzabrxMbzjNugkgZg1xDJxMK7ZDq9y1MK1jopjW39sxLCwJMTEoN1hZHl7zDrhL_C_xbUcSNs5Y8uI0uTYRc1162J_zFfvCp60e-zxt0UvbTqH_fDDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etHIygBC-8fBnduXAfDmC0bV5xuVqhLQwCmhUS4zgdCo4l0HYIIDg1VEmkX4etLOLI0UFyHOqrzT_LLGptjWS0yjMxuEfFAbVCulR96nudTcTiy6QOYPY28Ay7c2rVXo2D4p-l8OTgDvpdTEppsvBSLOlkQm9XDaMBU2AEQYiV_LAlzSLy6tPxJX2IXu1djeA8dhJ2MHBIxo4uWohvoC6fQxqFgeDIntffTrQlOEov4rz7qAhXCvxYzvI9mMlvSn1Tg90M8SOVUjgSS57ZzaK9aSNw7AKwpUeHzQa1TZ3gE9pUzhi2Hp0iDXRXsaeDJtcgf6XBGxD5Nxx5TnfuztOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3cqlhWMclppfjY4-H_u3N5m5Jml00bfb4YkxWc6O4mRxuncfP7ni3Z401bb9aMmjCcJxm33P1gJipY9VBm9fy0fEa2PpF2cWFVB105azUWurSTfpplOpdv_auoQAvNZq7VkQJU7205ztOk6ghihFPO0q1zRrl8xAD2Ybexldk-vEHCa0PerVdBNB_-kb1whH8YQlWC1Km_0wCOP8fBcMgdqf2WbW_awjQyWPzsZ__OdiwScdcE94ogvdX28BMeDOtjQL9YXN5IyOpp0VN_FpRBVPHKM2Y60HU72YfmVtx9IC9rvNIjJS6DAcXJf_yQIOxvNxwovcGMcHEfy6k4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQspzWRWoNuwZgBBzOtBNL8LX9wXXuxWASyUBou5QhGC1sz6_i99sCXHp92dZXlDChFEKo7aSLlXMd8eUixXc2AZ8aEDpRpnGVRKqF06KWDuLCf6cXSN0c7Wsyji5lGXJtt2X7yxDNacq0qEizqahqvpraS92NejsLlLyeJK8JBX1clkIroIz4kgBDjVZfAsnXTbZEf1Bl80qzfBdpwEpz04cqWv8W9n1x8ersVojL3yv4ZM02kVWgoLKRqjp9skPBKyYn6Kqq-8G2HS97XG0fU_nwDHjyGeUnuYYf7tLnlSOF3h4T7Cs_BXcF7-l-VBpBqgLuWG2FBlp7z90Tc9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKyvVkJFwJaozxOOlArXXJRDQLuY8bVB96frqJ4UoBUW41tMk2Wu3SQ8I10fPDvcInVPwOo4gt8z2sjtqZZv_csKpYz7VZiO6sSY9v2S57HOBn01lB5Er8AMQ41dFad8eI7LiNzUUOVpDshpZNXh55FKwEmYQPKMCPsxM7k5LjSbA2RFCfpMK_baWoMk1qkf29_f7YaAdh0x59gSCqFoalM8f7mt1w0sXKvVd4CwzAgJglv0QeFWq9Cu5FdaF7tS6CelZX4ELBfyZawplMlKfSR4fjguLdPT0hu52fDYZqcS7BpIgquo4kRuVjhdHK_eJUBs3RZUSzW8RlJK1UmatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hpRDSoEGXx-67v__ZjxdwQ8M3_svekB6dEYfKFEYzpCU2YuedNDev5DEbu9UPmzY4QCRCJzTbnH1ztaxd6zZb6KTIrH0zT1q1hZFlhIZo30TSNuhHsNdoXtvBGte1cLnpkCeFoLgz0IvAAPV3c91aa2UyhxA04C70-VPQoMQrv1KGpdTnS8zB6C9-I70YZyVTWYZl0bcbOFwgwPOjmorNlJKmVXr19yIo8UGGOqVlHP8dJ6Fuu7r4HQnL_V4bXixftWggAVuNWHEyQgJpxd5pirEmt6YJASmoieUUTAY_-gElvDE4PzOD68PKpoHqtHl8ov9CZpZDEQhINmU_4ONJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hpRDSoEGXx-67v__ZjxdwQ8M3_svekB6dEYfKFEYzpCU2YuedNDev5DEbu9UPmzY4QCRCJzTbnH1ztaxd6zZb6KTIrH0zT1q1hZFlhIZo30TSNuhHsNdoXtvBGte1cLnpkCeFoLgz0IvAAPV3c91aa2UyhxA04C70-VPQoMQrv1KGpdTnS8zB6C9-I70YZyVTWYZl0bcbOFwgwPOjmorNlJKmVXr19yIo8UGGOqVlHP8dJ6Fuu7r4HQnL_V4bXixftWggAVuNWHEyQgJpxd5pirEmt6YJASmoieUUTAY_-gElvDE4PzOD68PKpoHqtHl8ov9CZpZDEQhINmU_4ONJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5icr0swW9UrKXjupxuYI76-k2h7QCWNI3bpijV0SzAVyHpE-vGp6sruOp2EJ-X0Copu-IYpbglRfOOs_jteSnWEQcdj-FRNDDljMuupCJWJItd7M7RrPVif2BCR0V1-I45_sCJ4phMbGxqAFkGyBKQoh-7JdoEYKXgTHwqelmd3pNy-0x8b4y4BNoOKGLbYyeYZTK4IPn1fimnItCGZPYOZZbdd3XExZJ7l6L_CpxvEsBL7LaCQ_uPt_yuujkOYbPcb3HdSWIQ4lHguSFMuqHqqx5bQ8SN4RmQBLarluMlffl_xUJtfozT3Y48NehKrhNasIBf3upKk2eAq81GQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvX7k1CBURV-EBvVXpAGH49RDJKId_xzQ1bqQjcBataXbK1h-bWzynRBu3V_Ve5ZVqvDiJJsL6ZRvHvVMobjMYxS7DJw_wYdtiI2NV8whF69TZSv9C6_zDXP-3UZHNXmyAEYlymBVpc3wVF-KTryN0_qGa_A6zVguwEBK0nBCFvF6LbsKSYffO37ccKHecpFkT09-fAc-ju-MADB7At_tTOvbr4sbuIks8lBiD8zi-oUbwunU4zCnSrgC3iWriQdQ5K48S_7Yh3_nIg3m5mZFxkHYz_higxAAGLtKqPwetRCxlBW3Z16uynGpVlvPNEMnTTIEmbQoym4Qz1AaeiRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD3ixKeawunK9TsJwFWtqi7TYkPIcwFtkuUnzdlo2vkJn7TaPeKRQ7XnVvdccHpKTf5148pGfYCRVEL-RMrvLleIsqN_LspsR8sL65YWhbGPBFlw-dIFt4uWJilGeIwXFjNPViQJrU1mRL8A30H8QqM4lH7uThXhJwRDXM1lzWtcRmeLj8F4DdOIlIj6qcMBd_lTBa2KlJj21uhhuvz9LirGQOqy7Y0tRWt9xO-ZexURL93jWJBXo0pZlvEZj5WEq2tKkn-h8znJRKBZJVwUrb60hCNs_nEo4_ru3ILHKtjXlrTWP6lEjU2U6DavT0LMVY9HSfysjsdjpcEgeXiNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gogOwmLJXqmcJMsx7KuzM0P1CYheB6G7eZF5C0RceQrlrB695XVWFM5BcPtrOTnyV_WKWqTxqiUVd-XWEhANLBnRy9iZimtMCQ0I_6yJbqnMRNi4b_Z_VzRkqeVKQXEOQ160_QgU6BEMcxZ-_mDgmctf50tCxunLasMbiBQbCgZa-GXfb7vTlXFL7zBEL2SOQ7UijyBESXoy0IHPx5W9MPaBSNauFmY7LJcm7M5hrCzEnrp1h0YimzBLs4SYWvycvNbGxu0tKyEyRZ8vyRq_B7aSPzsTgQI7HkGyD14c9tHql30GVI5zLaQIXavnuEvyCKglvSlOfNZXzTesYVHEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnLEy2jWgPj8Ke0HxCoK3ieD1JCcmH1y49itYGI_z12Nhjc27aMtV20BA9U894lBYzjoZA2IgdHLc0OglTwwKNkGuFTHHMGx8b3NJJckLzy9DTOX8s1eFkGuP9Y1a4bEuXCOl0tM1LDOJ9TRdVRhy5PGwRDQKtvRl2N3ztmNNzcVHgRnn-Xs0lSsXVPGe003Ydx9nSsMkKvJ4W7joLGlAGFDAgtFWIk7uzRN1-NGT_iEopKcdtkAXcTy5EN1fvgBrFN4oMlRLwH9v61dHMdjUTXEvkWVNLGoCQkIvoybg-V2d6iAbFkoYfPebDdnh1iX8NgUhBR5d5wX-LbL8pGMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0f4zOBsN_fdloG9G9LS28-oQq_eIcZ0OV-bS46ZcE11vo5N5-okDzAmqbWRIHLvgQ39T7D2cLZ_aC4fL5R1rkNA8mZqwLvLAqICAPdv_I7FmLwBHcn5PbT2HDfmPgciZmzEf0lHGP_lrpQr4GQnmoCPkmnVdmr5tFH_BkEpige3-lkJpa1Sg2_SC3H6-4jdxt01P0Jo5fpWg6ZrMjYQsOG46vzB7Gxz9X94tloPUT3nLnG_KmiPP3hL5PleBrWXbkLHHxXT-LzEjWxkED806-u2i-C9TLx0mH78hwvk6tIGzeGwfJZ2M-48raWUCMDAjeygT9-_jWWquFoc6kCQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGuI2SwmGrxRxU0RjH0Uklv7cuqXcFKqIaJT6vLGWyRIgUE3wJ6UIJaTBJGODdX2DnqhLyL52LtRr9tYRNJixPx0N8ClR6RPmPFHzPBsveRuxY5whmTJhd9LkNFTflR1e7WVcEbjrgDgQVZMa_vJL0zfw4mpfMdJWWU44jO8DII0qdFvR9Tmwk1ls59rnF0soBMFAy5SzRMQtskITrq7UOaNcEpRrujo-mVWaLSYt_Zj8_JDpQB6YAlTrLk4KC5gM5g8KNMqjAp7VselVxEQtCv3a6LqOpPadWLXyyVZCL8OY0W8PlgrvDpHZK-MnqtOIKjRNMInb7SWbfq-2QuW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-CbO2dsaWuXVZhivMfaYEGRe6OpWAjcbD2FQGTafrObIor0Cg94odVg_ssYDhwP5lWZ1nFOnBfSsNU4n0cUdRFngD-Q-OvdGcuif1BPR1PZPJK_vvQi7KUpBKpUwS0kBVHFgplhnYFCBNQ86elGAVP7zIcjnFD_px6lj1TzmFpoxeZl_eWPbDhFDI_WrWw639btDF5dBqhHg-kqkgZ7BNT7Re54HTp6vehNFO33knbnWj-74iHS77cbU201LL5IMauZ0JofMd7N3nPY9JMuPxLRE2PtDZT2NoOkCuZBd8T68_cDNq0gJwmfj1tqyOXeGOfQpTaQeob7L3cY1XeFLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mi2YQi4itn-FllnQfH5IvNYEzGzaGUVg0-u9f-Hvow9e_8qbRvktZID8dI4GDTloOHwrec-2VsbNaN4Fgi9_p9GubeOASV2151gYUbsLvWdDtoxCucXz-i4HfQMlkcvlGUUAmQX6rYnf8br4XJmJbs7_eYH8axIKefCmhgrvZqpp4ldvHByQvwzTYZ9u2ozyXeHyogJeeM0TFNlGZUnUssqZBQVE1Vv7YeJ9M_6FS8RGQAy3nDMfg3-8u25F0xTQFIxwKZ9gsyezWzoIh2IkV52r8qWUwW17XmQN02IBcIJ176pk-O9qJbYwlZvcB3aZP0g6OI4uqhkCxG-PKXp4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5x7e49rfT_SnSRz9-vILzKHDfmomYQBSc7g1PL-MM4Sa4hSTtVriEd47jg0xW4YH3OmBlUi8v44fm7CznYkh8MGWBFN7IDXW90EnNXQA58QTHtLq2nCEMn2zn_q2WfEWyHvosRiNrQ-aEzvt-BYM4b3Cby2R5VyFeASbMikwTZqKtvfyWbNTW91Cg3-xMxu3W6jivyBrtzR0IU09Vhjy7vV-zfvVGxZg5dDFySEUYfGTh7RmciKyIyH6Nm83It5ftRkbvUOjt_P2-ZiT6yGwiKZxppLIr2bJa9VCim5HuxQuO7X8IU0dtv2ADo-cUNs0GRdgCyl1BEVrzZcHDCQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezPb2Rdx0_fjpHfkNubeTjt11m6CJWZg7XQayGfJRHdU7VtxKDBnWikj9dBm_YuQjihC1OBeoeW5moEpdF1nF2hy-8vwUspohEei_OQ37brpGu6mz2cUkmjrS1ADu0OwxcDdTRs7A6rni8MhzYfRs82UWR5LOhYBZIHP9nHEzPGUKUlYUFKxS7z8drUBkkzgptUvyC4sGoWVjgkRNwseNpXgpSx-Fu6j4gX51QOXk7EXuVZk4lNUYpwnoWBrJTF4nB8QLbyteCqLor9ihYBGwykcCZETZgJT8QOMB0j91y2cUwJi0sm48KCEV3E2zXSALuneQfd1WSk3go0w4N5bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVAs38i9t4M3dmkXOR8PT5ASKAytubHMKSzhZGMl0h0LfQ5D_Tn3qX0vpIUImft140cH339Dc5RBIusejnOpNXBt52o19xvEMPdYpNo3QBrU91K90ZzRDVTtFGXDfKNqlqNW6ouLT5Wb67Ji1Hed1RYxEdkEd5o8xcTSLWrLWN8ppWv6TE4fVbR0Bs7-_RJhQp3kNOtt5zWcv9FdzZvAXQnX-iO-ZqQu16NgQeGTkXU3d31a8SaU-Z9Vsbi-Sh15hQIyUe_Jz-iHQCzAD2kjBUq0Pyx5TzAj5V-MZIOBmSy0WHNK43-wqft0Wfx7HToA28d9d7z7sBwaZDkwRzdwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jb3XVmvW3D-m63EgD6KtT4G2DqS5cGH8Sezo1nt9cYcIANUKD4sl2jor8ZfZcO0baXETvlmA-lXCc63RsOn7k0ym__gtYhnYJEict7DtQgT5m89r5U4FXEk927nkDTsWk3LsTeWYxSJtHdPRIxR-yJ4iKqB9YgsFAHSMAx3P7pU3A0ftgTBILJbXFJz9fhSaqW1iLMse6eEoSL-KwfGE5v7wkpyUNth60f_6WhV3P5R6em5ZT3VaCdbTn3g6dTckYxoP_qlYy04yrVxU44J4oen1hDRH7e9XR9sdNumywJ1c160tdnoNWOQYhVPZaQxl4f5rH4_yNSypGLNKzLafNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhxrU5QTG612atCm_ShCpV7MO3cVnJ-14moVokUjbdz_6F7I7vyQWTPA0zSXWIS7iESb-sCVwGpJCh1G0KGHZuvyg8om-FyPP3bcnpvDOCVupX-n3KOeAdbh38n5u_0kug9SJR3ZIqsz1Uwe55uHUseUiNSZWMSIEozM6503zFE5ff9ImVm6LmsQje_WatVz_nbdtx0nSEP_K1bbyt_TVheIPA0E7GHyM7ebg-ltztR5S-M2e979KlWIaIaml2zRKmZSHt9x1ibXEpGXsJXxvg_gP3gR8fjpRJ9JgSlSMw7aSamcMJzm0EZpPq7ZpQjIzxHFfNHbbWIXPrKCJgLpiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngUhi2lvlXvvX67VIfABfpe9qaN4QgYGjAi941NDO-cPOfiU567_-2FyYggnNrJfpty7hA3a1aIGto5s7vMICyDxZe4XCZlU-Fpx1WbbRJGnAUMYfrp94-P6RR5YwcIuomNbqqebNc4322FF8AgXuYM3u-ZqoGW5VpjSQshG0Iu1yGhg7CgAxBjeUvrNAG5p-0jIwBCJqTu0L_OKxBj6ZWseuPP5H6M8dZKHKOGeqz7Wkne13ZC-VN1a2aURf3FPWfoESRC44sEGrjlhJFU9b-0pVMRHSTioTZCbJ7Lz5WzkOeaQwJ4Vu2GTa-TwfBivIRFn_HpQVWLkYLA9CbIBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K65vnVO0lFjWgq9-DtFKMocXa5GM8gpMi-5fi5rAZFIX-0O51vC1xkC9nO6ru2rrFDbovmER5NmYp0v7cPLmKx7ZHQNXTglJOY-Uk6RmT38urfm3Mm27opU7J9EqMyi6Y4ttkulzt-M8iTvpBKV5zEwbX4yZu0E4UwtcmOyTaPpXYEObOnkRV0CG0XwbHIkWmyG427ZxQYE-wh1gP1LbRhIN5d4fqPtZp2RUnHJc92i6ZE2SLUTJzhOg6GmwaWKppSoxjMAoKu5Is6Ehy1hSKpLsP7EJdCEhyy1w3tabzbg5ReQEICoFePYTmaiyp1tYoDJWsphqzO8AvUKNLs8s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWfmbOXZhx_AFS9zODrayYr3cNpag2p1Q3etyMzVexDygOtlGnhfJNCujkNGeqLtwnPkKXylFR1zpLGaNBfZ5NPwTUlF4uW1d8cjt-1mPI1XJY1_Ms5zXHI4QnwmjDK1PStymu3NfJ-8pO0gQKF60zgOzni-8kR_ODp8buuHrOg4yKSogS3FdhOe5t1DdonK5d8IHmHRIcY4DGHR9AQfZXj5-wZs0LlBXEkmtspI95ns8Gk6joGVzlm0viQtAzIJrBANeL8h2FDyaxiJRB0RWJpecI6YexxXm67PZKe9xLZJLYOe6OExrfdLDz8_xsvwoarA1PxL-iwfShYG1WGVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGAqtBDoqPVyJu0AzHGfoKIsVuRC1hr5oS3W2FvZRW5MAlPGUIEaZtqnzm8mVdLRCHNu74-J2PXPCeXHgbCWu4u7XAsh_PS9dnUDBTIlRlDMvNVxBOMNn6awlK46_xq3YBhsR9zekyiDiisfA9I8wp4tAX9n4RYyGg54sIn-8--xW5Hh-f0BSdy-Y0KVBSxh4CQtJBnbwOaxb0b45nwgEDLvtY_SwHnscpngZQZOTqHI3Sd_tzP1OvygBXa0f_RzkIugl8xkHNojgCuF7jC_aBNjjdQH3mqBBRuaDhI-rw9eaLQEwn4aKG92QrTLI3avb3Qc3MKpj_h90615aHIjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHjcN2152Agdkq3Yx0mxX8AHrbp-wdQuBpqkn8b3IXVBNk4_wzS5BJlMjZlYQUAQ0RvCjNhzLt0wY_eoJ4V78aeMNsyYqq9uIjUCrwUmX7QW4w6Ss-oY5HsYx3X_3ppoYrk12Lr2DU5sOPjCCOqgKp0To77cesakW3VocleLAPkmngr1SZEdfPjRQvcBlBiB7i9Ns21BLRYeFO0Nj6FDuEwjFFgKw1-uT2Y3WRjv8DjjIzORkldEkuemvGXnAlYWFCOX79n2z9nuocRfo-Jx5HxDBNLztL3dghy5v8MfwLq5l7nfpjVRg70-rJN-X_5ZYhjKe1U8058wiZ952073gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWWc5GewzJ-z8iilU-dOPJg5RI9QQJ6Jbr6PIIWTaNt0jWxPqurSr3Mdh3RAKOm2Ihi0BpM1SWSdxLMW1rGcRz3IIefHp9F08rZG758pb7FO-CAki7UaDB2F0zo-rikG6x69fl8CirQlURXTThm-XCgBfNa0j7KMl4pfBrXYc7pa6GZLlGOlr03yHt1ZDJ6-4Pl6G9m6JXRm-HfHWOdruT5Kezq35iCNqJ5FwF-pcZPNY5XgsfR8TMWxoivm8jD2frdy3NpfWhlJwKZ3su-FtbaXAZr7gkOpDCpSvXMnKlngvilUJp98yhHQEoAE-rau0K8IUTL7Fxge2lAVG0pHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvOHlIWqQF_ycr-kI_iFl0faxCt4vtsECiyVQ0S_mlqBZackRXwwlj-5auBKDoqSIGX0ZAxMogvklmRs1XydV7OJNjBNEMKTB1nGYoIsLMbwhAAFnqpszHXT3Jy-m5saOGeTmkFk47N7vQqfZWRL3Ddr8qGhWaEaUr90xVPVm_LWUhYhzcmoOt0qGNDOkq12ixfRkj_W185WernKJqC4Nwmioz6FtasCkLN5N-LDS2fRCIZ_3hhdk3rtRdzbtEF0xQgi4BTywpnFctVD_NIxWItvW-2iMgNN0RDrWIKk0fnXZEVPaBFv3eQFKbNpcMD_cnNqLCcmnQLnlVbOZmMMHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKbDd7vTPn5sGMd2J4xF0VtqznpmGXyUZeYpEd8tf7KM_WYJtIoe8nKwdFxCE703jf7eNjLnYWil5yLJSwhoak28kN0u1fqPqhaTb_qmngAMqwMtRqAXvjls9fXmfaWFgSlcdq8YnzrLmTtcb6BSGkI_ILWX4cUjv3qTOsO0zrTf5htHRFznAlEZnsRtAsqug4KI4EhAhdQok_XjfyUl1F4tlwwcugJ1bv1MXHSYrdnfkADI-q7zo9Qp-Kjx1KCsTo9GIdLDMbdOskgcOgOwH1nJMqcf1LIt9LK14tqYBoThgXvIIJ7dULuGbXqc2SYT5-bnZYrnql88mQ0zqpavDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIPPzEUqEX0nm4bzKrMaJmH1CJ2sAyADWa0qTK8Qo89hYXYikcm_uuTl6RubR7Hohgy-5kzyAAtoQ-ej3hjq5AG6vgRR__sMaDypjgmWI8I7DUDO_X7jTt7Ri7hTe9BN-xdjDvnqyoG1dWXMbdGzqNPnsJ5NZpgF6ObNh1h1b6TKypFoxoLc01-SqgwIOCGZgqP-pdzi7DvdqMnEMoi4bZEG46btYSXKQJb6TNK-Uo_XkA9N6OCShZGUdrw5Qz9A6NcUQqcOHB5M07BOkV4PlLhInb0ga9YU54n7WC5wo2YWrgctTzj1LTB51vlUIyoejFTUovRSdjBCIunI1iK6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNjjVU2AHyTSXYblKzSAt-Rt__genpOKONOyaVswIzIUNbdu9ejIGxgHzfCIZn6fpABZ0Bcrut4xGOzjycpqnXcxBe8XJD-RJSHQQIjBwhLEx32gcJfvvb2I5FfE0IMeRHv0qbSeB7KwG5bzqvMkGNebqNwEoymZEAM22euAAG-bg-Hv-pp4yagb57QeEcjX9ZNnggy6CNe9CFelZIxGqVnKRPx946DIJ6DFlsxAVeK_LW-pGDuL8ZWg_AqLQilOLnGYUPv7iPZreCT-j3FXlN1ubpGuFGwnmO11dAtNQA5bTVojn-VTE6RGYT5sHIe7HfcgYxsdeXxk5MoujOECBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eboCrn8fSJAiyeTt8FU3WnEIi9OEBOkE0M2Bbw8CihlRg8ul3gUjlhtIF-5fwdb7zyENhTbb_1mcJXgp_cbMWMI629q3LaB49IpoZWjnOPvsdKCtdSXoAFXijZoLNjpdgrc733KELacu2BpcljO77uz7Y7pWaE0tFRj_RT_tNkk9iO1aadbmvdRmYvS_xGsCS-Wj_fyVAFfzFXf33og500XLRbpouO6ETOxempj7aeC86eMgubzxjr8c_xRKx559gh8nxZMN5bKoFe2U7CYXBi0RnL2-VpI0myKAbDY86juAgpEJs1phUcz56m11F2bklE2Aile0VzlweHp7kLEcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlUsfrL__ZSK0Hbq1PheEzMAT7qKhKHxi6e5OmbZJimszVMUv9nhuqUPimUtaW3bPGbJBpF_X2a2h525BtkWGV293-LN0uZ1aotKh7C4FjOcPDGZ_ZZYYR7IxjIoWKaNWxVxj8Rjlg37WlvpxTR9OQ6rWnhaD3hMhTLGRE6_B4Vg6PTXloZlFG8PGhtMZHuNd4K5neuN-scirhbaSwIxBwE_fbZBB-hz4qf1QZEt6AWMXoSA5BJf6SyrPtPa16wxbO56_Cl0PCMLaNccRNZJ-ufU-yOGVpd-G1dMdAY-OlkC7VITX8L9TO5xaYF0xgnle24-CfQcZSNs1gRzi4BoGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWfemIjcO0otI0aRbiErwWgxW6ABU-Db0-JDEWYqM47XawggSG7vVkFNn0uBz11kzhZWumEayR9G4HhaJS00heyKOW7oa6S_SG9bQ1USGk8VbfHT_mdgS4uY2WxS8YGHL3SSfhU3WwktTHGRNDv23QqFqgqR9f-co8wHuChyKdJD66GUZ-qQ4qBGHZdIkBPmGmgkANY9dsgG3YX67QYl7FK1_RursxvDYWO_SfAMYC8X1biNpJtFflXV5kQSR6EDdP5rioOCmrubVAzEa5Cj3DWSdj2NgBFm0N6abNPeLXwICgkjlK9cV1f_8jnO03Je8yxdaq7HBelW3OwW5pDXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcH34wb_ySQNkWpJj5DYHug_tkWjhv-_1YZacLsKx1_-ar-kIfNjinT8tNT77Uy9GT_Y-asDDs_Ral3AeQ7tpXDLJajKAHMBbqNFasPUlRBALNgf4iw9qF0wnXdc-uKWj3tD5C0289NgBa6lPU3XZYVYqjcWr4Lcpd5K8U9cryEveg5dmx-q_ZfMx_NEwzdPA5iyGYUaC4Wyy7yfQpUamn8EKkFdHn0OFbk-WVtIXolAcVaLbwNK2LrIyTavfpwNkJMXl3LbEw67XItaCBAWICX1YLou4mE_hwhjMMPRh74KkL9jZqjV9njCzu_KZacN432mrsPMfbLxKWouzufBfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_JZRYzz5dZkTqF3kcbiy6o3wCiQ4G4DoarSodsj3ZNQ_Ms9QZeNHX_b3GdbsyNmxsw0hzeETlp4dJnif-Lv6USu07lCHtrn3qcA7OBfi3GUQk2PX4-ZHcZZm9mkMtbiIgT6BIMv0mCWG6t6rgokfh4sSqjiOUd721ob7kEIJl4CapuJS12Uix8PTy9ZM2j5sqvgcG9psJBrsTZW2almDgHQrlPQmOPvIzxa51y4rq0SqwsHwvzupUfRPH8NNUGBf5BMvj2Tr95FxNXTjsDmtTTfuj73uiqqyp5rVbqSaUE2wAXT9jROy_YzrNaxZBa6Bo5RUg_0sfJPYZG-zfXY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJMBbh_doyZKs6cHFaLrebKxaVT8GMjjH62SvONHNIr8gGpx6h3uQz0chzU5ST91yAT3mW_OAm5HTUwjw_AQrhTEzSTi_pXVUzZvDI6bSO3vStd_dYguCEJ-D2geN6mrkRiJN8eRbdSgpkDyXozNsOc-paHCYzpDSyNE9Tx0p3CnJ26SJWhFdyttAePjYtujkvxG1yj2sTewasKK0BMlfI05S8oND9jXyg0eEFv4ycQjPyWoUUn4MV4q5fsOOhiPTt7tmGsaRGpuNKrpSg3rxvw8INhelMfMEsUvdbgE6ep9qrEMXKE8SbNPNNyNvq7B9MbUlHlGo6xxNDizNmJIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwDPnBxdMQCTT52-i-sGpAYX3PSEu1IjuUnkzpa-wn1LM2uavDkY-Ovrg5D5Qu7NMrBC7TFNzkDoI4c2fynhwlIlHTuK5MC6RCABrjgwNiRV7Kw3jhxae6-G8iHxTYf1ZHWiAjLkha1uiS7p5i04a9a7dNRz39wruVvoHPgI9lkDZWqrF9IZJ8YfgukRpJg3HH_cODRB3rgleqzb_mqeXvtH1BQotYP-aPdBJDmi8Xx-sDAkFugwjT9GXyeqm5oKB4Q8udgR3QHY-rOChc2oCZkyjLuc4tGhRPyogcMKe56ejjflHA5gl995ClVEozE7vyMFtHb0DbKioHJx_mySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjPXMtUwTnCEkDUweS-__5PrY_ypKoa658BYFxtkK_wAhsFcQwYpImFPuMtVrf5-A1yRpwuzwqeA7cfC_Sfh62x4WqhVx7X9eUNnR0G2R8-290_Jfkju2ATYjcRW37fAJg9z-J5gPxnyiOPZTe_naDaB2q7LmJF1l_-RetUy-dkvpbuEbE-8zS04e8X_WQ4FB_FmRkcYBeD4jGUs5YWPTTaHdKEPrrPz32LJS26jy4asyjZv3Ase0yFrKwkbSZ0nQsuxLLS3Gte2P5fdv__Js4uUJcM6IjYFK5sXUpzzmAOtle_pJuE6DbpBkNYUnP-EhqKFgo7bL0iTyTGENTY_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QY1I9x7Fcifr6IIPRKUSXU9TwGRHLeA6-Za_7wnpHINVJIUgauqg6eQnu8JiJpBIP6jB2xeXXlv2WQkRi4JHMb-Ut6zD2-MRoKlWfwDzHSvLvyj95Rd926rikNK4JsCmNtSxDH8hDemxdQjFPfrDUKkX4PlQhWqQPdVlqE9z5zoWsmQGLPqiwcbdWyRTXwvnN6O-7qjqUMUVX9r8CM_J5HKrvouIBKkg8je_9-uMvC7iANp6Hj07ZA2k7OPbUhLXL98EA8MApZH0t1VcFGU1v7b_EIiqLnpn6lScJmwy5aVj6Tr5qZ9JKqMkUDZpxirGybCuGe74_7DXSEMYLmnjSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OCF4oAk800zbsl41e0xuxeKV9mbOQsTOemA6-IkFmcBors6sB2EVW7WDzYf4S2rOkkXjW2k9OLT3cTFK7_STFpaanTMkpKXG28SLrWjEslK05PS7824FqZHN9IfXEAdQYNfADW9U_QSpPEDPXgDeZcODXI5uTtQ2h-MFx6X889IzNm5LQpSMKkJtN_boOB2dEl50u3SSyRtctSJ0FL717wAiHdnnlctfD5dCpQNihkBi_4hhSfLGf0kmHy4iNcT4ZdYX-DsGPsWQzQpbgB_STioBlclSBkg6IFpEVKfynZDDGpdgeGa55_uplQcoNqD0zhEt6ZkH8vzHeYKKgpMFIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ng09xiyUhnvVnw1SYnK5HvNLR0FR4ZH6KhxYIwM_g3U7t__yQfcSajp4QQGdqztMjNVH_EvIUtQK-yFsRe4nNK4MdpPkkg3HHtRfGkVcJo45yEr43sBZWJxtPhGSxPnt4Q-Q9Sq9sEuDQfmMzgdH3FkZTOOU1E_WMW62-Nf5SgtaTksdwrff6AyZlZgFamJmWCksSLu9Zn9_mwDrm0_M8JUn-hsKzpX2MnfY1LcC4sfEDm89-KH_uLlAqgp0H_kPB79t8KDDdpbO-N0kRXSonHFKNvuX26JAB30OpJJF_ZgaNQY5I0rVf3tmBJH5i7Xf03wLO135eZsP1PjIOyG0Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCwkuLbJZ8Gjr0b-V4U9QMQxPXG4DsZDtY7T75Qo9mwAnQHP180mlTJ6rBgHvahXFGSyM4gIhRVRSoxtGM1QVqBQ4jN9i22nfS7WuJjcUr2fHAdT649rUTyxkzJUB1QcAt13OqGngcMn0nn4J6EkAW24UsZRyju6HFVuU4M5jGPBQ7uixD-5WRv5RlYkliBetQS7ce5N_DQi7aZBvot2a8X95Wg54Yad3AqihRS00U1FxDtQ3FTBsO0xejJV9ZynLmPF8ucZq2HbRoR2Lp2MH5hZ1sV2fpg0eHEICV9veJa1vIk4mynNUM6spwgUZ6CE3sMqRHODVKNIK7-DqbiXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgsmR9h6hKlbWypmxvD0Jq1lbKfCK9ok_y9kftrvpGRBJ5Le-IbNcZ5mVOvLA_rYsbtVj1c5C9AE9VjYdNCFNQrnTcDUP3E3wFL4P6rtFEF0AnWA9qNpUMhe38nRpvbB6FNbiWYA0a7Ch872MwOGdyOU97-vO088gauPQKD8giedK0C6MkTrP4YVr_aNBqOkuzXZQFbXLwN9J4EwjygKqzwg38y69lg0NNHvPKXmcCoPyBzXdst8N8gssVTmNNztkE30xmUk-b44vL3fkESx0-lAv3_msKQPwp_kIxA8V7CFy6xauVZkLd-XiAYg07RJ0BB7Ey74sYZz1NNZuakOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK0Y51_Tcy9vHZA1EcHZ5BbkAZ5KPu1YJvdhAjeiAGpxcd5jNG72NFUww0KCd_JTndF6gULLqkICm-8FvrROZidbsA16lr1DLo9zMvnJ8_CYZKaXOufhVdYbOP0r0-fIueLnb6poVjrekDAJyemIgIbqaBylpRBhDY8OAWC_uu3XS7zF8-w0P_kVMLwbd5SCr0hEHMO8jQyzuds4vjE7RYzDNyyT5B0ZxASJbEag2WwH2FurD4oJbqgap_Z58t6PGipOlpGjIcG8aeN6R230d11qEcQhiaUtSPMB53FZs8k2IvRZofBPkO0NyvB0TD6QVUAcRSjlD2e51fkzIpim0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxnY-2BVcp5wCSme3Bo5bDCLxMGVbIA_fgMqTr5PiObct2hH_scY6xaOBpzCspf7vv4vD874ESPbFNTXY5Uj4X4fB3ARDT8uI0mYzKThWkRVYq_VJXcfdBOOQlhKLVMY8VuB2L3gZZXgi8uiD3UOxq2J2-tn53IZfuEDjDjkY4dhPjNGpxYdsOKO06_hT0XPxHIhuPgkqmlHF8cgNTR9scAB6uWfsW1NeR9uWvwxfkYShjGSyS_WJAVJhI4KKIj_OuJydg2rXLy96KsNJAQXjUvDDr5XDig1g1Ct9xwIWM597KbW8cysXDWyd4hi6P8PcJxMvWUOkrMQNwEtbEHkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1XSbCIHAxW1D5Q7cfKgK8rT1znmRMtkyRH6HUj9q7u-on660S0OXkY7RWJJJhVRKpp3-cN_zTi1OojSrbqQ3lMy7YpyDWQHLKpqkw2h2gv8wDCeqiqgnamP8i1Iu8Qgd5Y_NG0dlC9XkRKvUytJJvZb05pShowr5PLiPgoe3IEJB0s8r3H-q_HO-EgH3O6XAVW27PlJGRPPRy-7KP1awssMtbGYT1d6I3FL3pWvHM4VbDpTvQf61Na83lKa5qfaDKy_Va9SXNlm05no8MikFzoAd2XyaxIAQMxdrW8rWXlNXm_xwf5LOxAuERT6Y2lkdizU8mJJ_EfLLJpZvJYXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDwUy12IktqiT1UPP47dU4T4A8q7xbrrRI8nAlgwnh7qfaTm9xc2b12VfCZDj5a7WXeNF2dQaYrvesoSYs1kKb0KBWq9ahlD5j17VeDpi4AW1-6i2qV1VC_OjnALPe1Fqz9yVY6Eh_FbaHcja3PzSnUiDClgAMsekygutuly2kPZqVEQIG4X5JwnTUbUDKKl-J-Rn4N8Xm5PQYtiHqVyvaTAMdS7FTOf996dZhnj9ZrcGxJ4swhWFBmPUJUOmaL-PiPjk3hnJ4lDM92fWS0L4ol-AZkMhJ32TQY7UstzjLSsfNf5hHYrLnFFcjXp5BN905cqJmTPCJXdpx_Xps3LvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBEQSjjId-5EGuxBymQSLShMG3gYWrkvV1UDQyi9xVqx8YgHtVyncWbttCeOGUFdjVR4jQavcyqF8Rmiz6YnJt5rLiA3LnID-mz5SN2ifg2iQHBOT9i87FL8TFiRm9xuBpwKUJEcBmme1ctQXtOhd4WnM_hJOlP-Au9ZA7tvrrRG8dYzi58anOqu7xiSs3Q6_EviiMb2jxvgpGXCAzNPOwh8gEVECSx1MzayMdPCB7gVgGagocyHJgnYLhPSYLcJA_JrWoccL0cpItJ23fgLE5pQ5hesJvr_1h8ZuW9aHmV1-mMjf8WFMYwnVjtym4l6InbKGZ-We4HLFs_-UTJZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJstFct4vQeQpYxueBSwQgOSzmJ5amWU8Akv9anRqeMfgHqKf56G36VVxjpTMktn2HGODdzZ3HLM_EoWmviLfk_EARdjm-k2VDPq2XL5ldIpw6AL2AxcuNPWqjHmd8xiCXK_gmFl71gVqEWezgdKRpBDH2V7C4-izEXiBjXezKvuPmaW62ots3fwJdpkwh_Of-hCn_ci9i1aZ6oicmzFu8PXZ5rwGtDaMBvXPvNP4TUuCR2HC219YnEOhJB-rmdWGnM9xvCXthnGP6tJG1GBuLsSetfOlQc96EfATqayjIqeEVwVWLuvlz43USkxhqwUdfHS46ARaYsDQBY-CHyYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbhNfe8v38xEJRhfq2nxy-an7Aifmj2s7-88gQ8Z8xerLSkpDSqWGcHvZ36O-P61qf6DgtHxlR5IIwAoya8LKw28deJG2gDC33vc7xaIbaD_AC-sWx3zwDbLumQx0a8WKfzNiPjLHx-g2HBV7PvOnZY4GBgiphNTKbJUcWbU-CufjkJPpvVN-28CvLb1lnzFm3GMFkj7kEgMIM8kgypd6PJbV2ZDu_40qVYWIlwfQ0L7I5pGx_D-pFN-snkdHMO7eOYq8rKNqfCN9DUWRtOX5KmdyksC0mXHPIlu4Zm84R2EJlNtmnQR8Pv3Ou7tigKyifO0oZ2lLiYcR_7GPnBw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=kwgPXqFEJho-Qk7lsI0Ekux0CqPKv__t-pRiZ3j_oYQQGmfzUdrev2CyusMcTtX1Znmmk4JNac0SOxAAAR2j6hwZMCJ4ADLCQ6uFlV8LvTE33H-i9C4kHi_AD3YAe0Zm5Z2nFB2NE0_dxMPGLwv8BouNU_qSUmxYlOcO-cJWTocIOdz65H8oMVwKTWQFIbG0O7_aQwkAitpYl_2EzyR9OTpWttpj301L5Mlkzzz88KWtjx83KhGzuCZPZSHIJKhs0KINGSo9YdZZbtBwQb5FdqxAA9gGrzuN_rgjBSN5278n4HYQUAwbVKIGIc_pns304JHWCuPcgtnVW4vpuduSGaurkMYTuqESNlX8SUt7g_Y5iJIksl2IGETVkeUuFPoPHQQ4z4vXZoIwDuLk8Dmw_a0ic76YascIanBOj2ty8JDuXW0Ns_h31KOA-Qf_2ZncZr8JCV6RaXkbj8WX_4NnbsP2q4Nc4ytXHUpXYVzyVpLwY8Ff0lOmdK43bEe26bgO4uNZRtRvYk8sW5SwZZou6hDSNbPObCxlUhJan86eRlsIqzr5FTEoR6TFjtG4Ll4NWbSqvPL41Ccf7a8AgtTpVtY-xKlSFy0Nh8IFJKmw0ifyl0nZBf0AtyurvjwryfJHMpAPQFkwWK6tWbA__Cqfw8ghENUFCMAaIMTKjQVVD5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=kwgPXqFEJho-Qk7lsI0Ekux0CqPKv__t-pRiZ3j_oYQQGmfzUdrev2CyusMcTtX1Znmmk4JNac0SOxAAAR2j6hwZMCJ4ADLCQ6uFlV8LvTE33H-i9C4kHi_AD3YAe0Zm5Z2nFB2NE0_dxMPGLwv8BouNU_qSUmxYlOcO-cJWTocIOdz65H8oMVwKTWQFIbG0O7_aQwkAitpYl_2EzyR9OTpWttpj301L5Mlkzzz88KWtjx83KhGzuCZPZSHIJKhs0KINGSo9YdZZbtBwQb5FdqxAA9gGrzuN_rgjBSN5278n4HYQUAwbVKIGIc_pns304JHWCuPcgtnVW4vpuduSGaurkMYTuqESNlX8SUt7g_Y5iJIksl2IGETVkeUuFPoPHQQ4z4vXZoIwDuLk8Dmw_a0ic76YascIanBOj2ty8JDuXW0Ns_h31KOA-Qf_2ZncZr8JCV6RaXkbj8WX_4NnbsP2q4Nc4ytXHUpXYVzyVpLwY8Ff0lOmdK43bEe26bgO4uNZRtRvYk8sW5SwZZou6hDSNbPObCxlUhJan86eRlsIqzr5FTEoR6TFjtG4Ll4NWbSqvPL41Ccf7a8AgtTpVtY-xKlSFy0Nh8IFJKmw0ifyl0nZBf0AtyurvjwryfJHMpAPQFkwWK6tWbA__Cqfw8ghENUFCMAaIMTKjQVVD5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtGMfZ3Q_tdVGWyPwptMNZYhDJAwhJIIW_Q_uQIaU49L4QaKKahlPdO3eeV_0SY7_uaXbDnzC1iippjr6d1FuayF-Q_oEgO8tGgYLj0jatfWmFX5TlGNxlSaUBIkCQFoOCQN090Sepw-bhLp9GGQXYTGtpRlaKhnWqPA7sqrXXCsGBQQ_AMyEUM5SE57hrMiaEbWLGCPlRBstzRUg8X3OrExIl_Z4eFiH4uiJhl21zcbOGJHeiUnvLu-4-WVML7Pf0NLyxEE3i4dRFssSES5QtTQX9PRF3l7GeGLnVReRnEOxzNtu7531qpvym2_wsMgcqj5das1QXjvj_sGSKe7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=TmFbsdVkRdBH_ZgXPh72RAID6gaQkI9DlaXpJhIuaVn3Y9Fijeorf5F1xoS_XDUx6oaWHid_uDvLF0T-9ngNloDgpS9bwST7EeLo5DPp1kBK-KHI40fsJNHKeQf9UtiMwE3EVPXpinDETbi4LOI66YbvedDYxDb9oRjGiV2OwJZXHErkBBcZrLd4yHbBLafYLAUdXvxMQQaME5z8EOZRProREBRt82hc4XICtx0viPbkOxPD57qTJDW2nxozv5HNVp2WyR95tVx2W4ujFCnnsAhjpulLg-zMp3qE9-ZjhEEO5Imo3wU0rUccReTAifIsTKxqi2JXRhTM0MBsqgPVlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=TmFbsdVkRdBH_ZgXPh72RAID6gaQkI9DlaXpJhIuaVn3Y9Fijeorf5F1xoS_XDUx6oaWHid_uDvLF0T-9ngNloDgpS9bwST7EeLo5DPp1kBK-KHI40fsJNHKeQf9UtiMwE3EVPXpinDETbi4LOI66YbvedDYxDb9oRjGiV2OwJZXHErkBBcZrLd4yHbBLafYLAUdXvxMQQaME5z8EOZRProREBRt82hc4XICtx0viPbkOxPD57qTJDW2nxozv5HNVp2WyR95tVx2W4ujFCnnsAhjpulLg-zMp3qE9-ZjhEEO5Imo3wU0rUccReTAifIsTKxqi2JXRhTM0MBsqgPVlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSUiWSQkR_wKmsfPivA6N3VsH747d30xwUfowOQ-w4Jj04JAOr3wQf21THdm3JRXpEN3yk37bvwxCNRhURnBXCqN5kvTmTWQsNb_30M5_tbPJ1HNNA0O_JxDorSuxPQO9PZIo2Sg_oM-_kC6iIyy7yVd_JwmxBf2a9kDIxL_Vqi1vnd4QvpilyXb0hE-5LtsKAFqPJHFSSk7j5IUpZ40E0qNi5U7V5KrWs1G_6rjElue_iz4mrSzXK0-3fZMKGSw85BdDBxk58_cobWE9JoGtA8xiBXWp2fzQNCWDzJwdKhpiYhA0KXdTN70kPKzFG9stJV0KyVuSjKabMxBmEq201MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSUiWSQkR_wKmsfPivA6N3VsH747d30xwUfowOQ-w4Jj04JAOr3wQf21THdm3JRXpEN3yk37bvwxCNRhURnBXCqN5kvTmTWQsNb_30M5_tbPJ1HNNA0O_JxDorSuxPQO9PZIo2Sg_oM-_kC6iIyy7yVd_JwmxBf2a9kDIxL_Vqi1vnd4QvpilyXb0hE-5LtsKAFqPJHFSSk7j5IUpZ40E0qNi5U7V5KrWs1G_6rjElue_iz4mrSzXK0-3fZMKGSw85BdDBxk58_cobWE9JoGtA8xiBXWp2fzQNCWDzJwdKhpiYhA0KXdTN70kPKzFG9stJV0KyVuSjKabMxBmEq201MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdElWcAoFZr0lqBlmGlAJUi9IyFb0-ms0tPvlIbWgvcmRWH5jRP1SN7eW0vOnZMjpIllC2TF35qBAy3z7gYjBb6GR9gNI8SPrHCP_YlySQgWuvC_lZVKGZnvtUOB45Yh12TD03VsmCjijPEron6atSF5_iq6t37lys7JsjMN647mD1pWEgx5Z2sd3XYsiWtIdlwmudtFiIRDtay_iW4IyE2UIyz7eq-W64YRtDnJSSolvLeF80-J81utGnoa0t_ugaMjn14wX5XkOQhwfrEsdAbiiaxsTsNfSKn3iT42noQ77Vmh7G0MxdJAkrRORXeFsY8VgkXmAb-oKNULA85l4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlQ6xMiBnChy_Ir_EcT9XencO08VwSQ1vS-_eXF5rHh0vhTfEPhqrbzGmfAaaKDKV_zgFQnF11VvLI_BqTLJGhKzclqSo_0tkUEZ__b-Lcc71_MG3MjYGy0aZ7BsiQMwJ43G8A22I6vPv1yS_6kAs3M7snDgIN72e91eIJI7Yvd8cGVDBtOo-5mgwXe3rQsqT_kpBf1cEUSmzU7KLzPDbQLw8K0wIDUNr_sgdO71W66VwogoDLKvMluzV6rRFA_cvsS28Eel9KbhWmps0yC_evCiYiu34a0JdfRm18QXSiW88snRM2Gt0vJIAg5FSvVSV1AS_2Di5Hbr1uxihX9klQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpLeefD4WJ3DlDA8vM8F2TvzKEpdxbIZwHkljmGmO7VRF8bt4Lki03pRCh2iZTJeFM7b_NBBaQHUnzMN2ywsLWeAe-Cyh4LMrFn5LcexltfhhJVnGleZVHB1ilWd_i9JfIjoNRnb6XOxwWb1hKYd_TR7IyjYMYvz5Ak3YH9H19hhqtaJZPRKmG-raG9c8N2Gr5r-dBlrB6ue_W8DTGjdSKEosXhkzzH8C45BgZSHXYtMH1o6-A25YDf2WyFMKQ51ze4S-CVAoQddXegFfJNMO95R0jmepU1mmT4B1NTE3FrBm3B8_KNfPpth4K26yqbSETuqM1YqEEUNpXaKOnrBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOcTyzBDK8SP5sbzpCwGSWQVWLHq9MCoIAM1yQkUfZp88A-8WMLjFeEKgpo8C3CNooAVtnoJXWJWs9-YwKrzjyI60QgZEA3GJHDS48VMkJoaN4YmToDDs8hTOpNaOju65KE6f_Zy0K-KwAyqzN6dP0u_LJ-wbC3hYZr9aV1PYKdEDmjDe7niF5f99JRjKn7-KnUX0p2-duc0FVpjeXfSyIAN9q-c4DxN7hjfQOjjYNiGwwSVg91Y8aWo3uwS96p4YzVOBx_7lvN9RwVLSAICsrSYJgOcSqwrF8QwEsoGr6oqdTl-mIQKnmWvYNEB0CzKo8q5SNqtJiH9mycjaDehxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZqwZvgKtn_M9hqUm-cRtEUwe_7RN3EPoTRbIKtsBOKAyxwRk9BXkZDoDHxbQus29_T9tF2HxkBP5rWAskLDknmEG_JawJZtQ7R8AzEmVKR5wdqiz3AbniAh-56_yFT5THeZNhgktH4f2Ml1rvvg26T1dUmPYsTR3nGw89DARFZo_dPEIngy_OjOVCJz2-hzcTN9AUmqyKLMZGP5MgEURzbj7VvZExWjf7_SBmttCkTEL0qjTbvCYr4gDiO7Oqn7Hmzjwf00gj26NcYaDBUfhIl0NEyKZy1ibjuIVXWrXH8O13ox8fIClgGajLxefy_0F7DSYdu4lY1fp03wlJHJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfpYLtSzC0Tvlsmyvuvjd4U_njO7wV7nScY0J_6drk5dOvYaJYm5AcqZ8w7vwiId6K96Hzarl47maxKhiHy2eL_K5sEWVsJ6yUaMIHVGE6eNwhQNPx6L3ZpAUCq8KGQQFHd9MYS404vbC0anNf8tMmiE1HEwCcNbpF2PX69YlnY-z0rp-BYRnV9_H3qBrvq_scThn1japK0P-hyufUxHJjNqq4H98tJUBllrrtjXlGk3t8ZFkarJicabHG9veEM1RYgCUaOT8gu4RWLhKwbt3mY6Jzl3yr_vCwXdxcNMnHAnWrm68dzHrYfAqBG9fn-Hlvy4aMjszSNc3-74GOEvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnmrbg6P1V1Fm5wzkbx4OP87img3oi7bfkL0ZSWvbRfOGXkToY1pI9CUSSQsAm6gmFaRR7Ivd_m5-oXvEDnmJLCPvuoHeEQ0Thqmd2Y2v3HqAW4geahMEhjKK5gvuuYCCW2umj1zqilFDxDn6r1UikP07K-WZkcBYTUgYpbDp-XQu4J5cudSakQd1K5DOUTryL9ASrBV2zm7xRXd3PswR-SoHFBm3Ou_zmAYdAvD7CswQv2dipR2WW-44nyCwDsrpTlLOVoflsstV3n_Evtzw3cIick0tPR_AxTcsMMdl_A1GPnToe7u-O1v2rvX9DIccq_lcWkQWgx6GnSo00HE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKIjmRPYq9q_Vi1tzixy5eu7mUSZStqzE7eZsrOp2yiidvYinL9ipAOsb6H6qGfoUshnWElOFSUvky3mL3c50G0e-dICFs1Wtxna66wPlq_AfFkRxJK4XU0RS1tohh_BQbVoQzSPHrqly7pp0ca8EKLL0nv1mNrD92bx4E49ppy_zpW67N0Hq1N7zCi9f6R1RiWZMTpLF0Z3L-FeZUlwuX9Ci3SIn7ZUXo-10Zx3-upBt-pMNo5YWUuRwWTdh8StOBsUMUQ71eldh97h48T08_MoUToRgK_tvnT4Gy9BN092qiNOa_abQlhRHFB8uLwZBtXJ8bPjAGB5WXH4zdhr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB87vy-ZvTkq5BaGeIhTcoKS4XXgyUi9KxkxKqZGIFXEkVMqPxGeLL_QYZc2BDf2uE_Y_b5QFp-hNtdOdWQKPGaBqqNMMKfPH7P40sPFAmfCMPx7zq3Bo2IWSzZq02OiYGifTAY1rCUjC5uUOpvObacrAwE30EnTpU24-1xn2P69hp0YEWI-SQ7D-jSBBXPA8W0j39y-cKULe8LP8Hxhc1H2hNieo34m2Lo5oOWWY98vxIkAbhv_ux9ry_k9pDX7mB56m3VnCGWG3SdBTiPLELt8GBobKX4PaVa22_8eU6D_tgKib67FbVKaP_saqcDFCRoMc5K8j0Ni-q6hyuBzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfT2qI7XjztHSUIuihk2yEdKxFPVFcOx8d9JUn52rgXe4NtBMNqvt1EitfkBw923vf3LWQ67giwYoEFQ2EEfysbOFr9YVEcagyTmWyYJ59FktPPg3df0OD6v-fHvItMMpE84E3JftoNmopli2vBzTXn0nzCwVD09i6T3m-2m5seb8v2h_7CHdYoT1rTUwgEBdK3q_lrbEW3-LQxD985BwhMZPNej9NU3PIb9qMyUffhPgOhqWIZ2raA2gxqZp-AKRJ0cUit7wsb0GOGUB9YiEpYwAyVl08ojDgD0DAJo8_BUD0EG2ce8iqPEOwbWYKJ5xchmjCfJH9xJwx3u4gNIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv4rsVaKop90SktS3jBg28rsU5XOdE74IK73cSuHqsFE9vcWzEAR8hfCLBRFgcbJXb1WbvHMhvQajR7yzIn2l5YbrJ9jZZkZsOiT58zahdaZ7I4Y475G7r-XlSn-sOq2HnZR1AqMja_9DNphGNKa0qOdX16czgBQ63MgpbQ1ZNlwsXMj-tIDU0KKsmUKKbX4PYk4cLtNFTof7zCsyqZxcjSKIprKnGm-34egwnD65thsJkRz-QJKzDaCkyIHnD-VwxotyVNzyLw2UnPWoUWF2qQoW9rSrOpQlelJHeYCmgFjqyLQAwbp_DiWSTqnrr_JVXwx2_qL3g0tA-R0MyD8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSRuzsTHBN06kOI_GtA76s335irUylswR0mc7OqNqdfWVPFV7DWthQlYm8oYBI3pSUfyItlI-r35VE2W1O1Y6I8FLMGTz9VtLMPXH8jFGTiGuFcQ92W8_PEPOBlanwf44EJXbFCKDvUCw8KaJflv9THSoLwewiRPjJpqqQmVaelWXeb89hiWHyJ0NjcSo5hLpVJcnRsMyYx2RBQAgN0qMJwKNQPMfpU4MfQ1Uk4uQbdU499wi9M9ps6vMyalG5UddZ0uMjJcr_tYMg_0CPl4E69nL_CpSxUojrcWzW5JWB5elsVdesv0XDGQqeFs4xSLxmhzN3LimWsRguL4p5s_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHVtoODqYe9YcfBzYBC6cOpQYEVsJCXolblSjLMLRWlr9-XOvL1VOLSvbUD9D09jqjlUGUGLhWApG5rPp81EWAu0-Owi9O3G6ZBTaPq--2AEkwgec1JiMU6SUvPR0bDACf_eem6Vl8xarz056kwqzNJRfXmV8YAM6af0Cw9mmtqOn0hHhY5Ydc7zxocs6op_lGpMh8rh7KGpfim8J4RLuyyC1YBnpPM2XHUS-Ok3IrBi-KdfUX-J_mzlfc6C1S9qFTWzlOoyc7v0MWN_sZNm8v-2cPikRdTHuWWlSRd9_gUZzKLlVUaYnJE58aR1oGuAsau_BXQbbZPIZH_xRwWAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-SjycOn7O-xLqrUHktQ7HAOOJYty_ZRc0PefJ-jY8VEAV8CNWtX0yTQIW7d3rAB6rVuEKTtQhpCghCzP8Ws9fyRB6Ahc-HZU2nBLR8yo-8sC8x5VZUrHAPqbVc8v3arcdDW193rcTOmUlKlWCL2dFqMz0SLZmZgUbJaGfb5BXftssSLOsyEq7IygrIJeJX-miuiIvU4leoww_3FyKQ4wm9NfzqtU-KVZ5CZb4NVoCPGEWaVf_F6WprmPs67Tv5rbUKNx1wUNBJvWQGLQevZl-08zSTYEUwj5Crs6UvSlrzXQHrrQoez0p7dW-V_hitaTNiTUi_TP5oCfInWtGqBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTsrOfgEeIn_mP0i2bCeM720NK4ENGPIJFoVtNw-Lo9gwdRbbgNy5pBEcT5qpRmKCn4xHVpTSSoebs_U5o3hKXxQakGA9J3SRQaUJJ3MYzu1G3BUGGQ99FSFb7m0EH-i8I9aZB7MbUCmus13v_q3D0dTMX11R1v2FfwTInQK8o-qzkonOgeQFFHD8q8mfjZ6V-q05ssBWVWoP0kXIQbsFHwzcqlNP1uZw0xUpZwn6xwE_RGmWYzGn-Se1npOnCNzDS02XSEqEACy3HMPGXfD9pbz5zN59Gg3KJVT0iFMGr00KrrF-CyH6JPNFZvY_JO6bnZLXIUgfUBocghePqqQmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4cu0-MXQKQMiXf1zOUQJ7HV6P62NLlcMcJ30Qzwitk604nTOjawEZl91thXyImhj0fwis_pYZG4HM-_2yx4z_SbfnV6U0NPFyw0Dy4Vc2rtN8wfKZ0B-dZs_rlRh2B-mvN7fBoph98g3XszU9erdZVTZs4IAjf0U3dPigLlfHP9-ERez-hzAKmDfWP5XYV2_KvwNtf5_aWpaQh8Hr_UuJ6iS_O7ishfk5hNBhL8H9UVj9ieFo-8WlXpFZA0lGaJA-xIxJ5Uca2YXXrAlEsfNe4alpGWBNqCOX9BTo6uV9ox3XGhXSzOnUJrE4zyQQGKl3YfbftF9xzrb2GQlr8KwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWVGygrDAXIcEN9kIOi7_WTsm-POuQ-jCBe_VcKLr4B-sAnPwSeSHc2rpoOknB35-QiVxgeh4NAZ-np57QX8YD6y9GbjbUPrzuZEZFS8jadiL70BgnVzx5uaUbKQVxu4Y1i4WU3xkyx1mx3fkOeehYu40p0oAtCdC6V7ayZ38dB0b4FrtJAc7vXfVUwfJTrCIk8xbBXFfuDRQawIxGh24t4VKrt3ULYKWfHqfg_3to4Bf0WHCEQPBYLJxXha_pvCpn4Pbj1ee7DIlENkfP2kjqoVAS4Zd__QlaaoXjSj632_3vEoSeWsNecHy7ySwSHLYhYT7H9fSIgTkmhBsji68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7b_e7Bv91Ivq2pM4EX6kbHJgLj_7vA_xNAyRcwT3nFmSzVcAMz7UrbXUYp2NqP8sPHDrgY9eQCo9L-eKPDFlJfqdhFg7RT0uRopTCTB_NFj2WZ5tyRuJiWfdtZGhKdc38dNrhwaokIfX9CVvlbytENKUQKLpNhAJBlJC0sC0CE7tLTovk0S5eWpJqLzbEJREEz37vPpzxZaMO_JS3l94wjOGrka3kaf3gkAC8HLB9u2g32yGvudo1xAR9dFe6CM28_ouHjyqG7U05ybqYrxDrGciPFdsJjHH0B5xZsrXObjRoCxEmsDZ-qYkLpPtinepFYZ1QbnsvTXZGFH9nD3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-6PsNfNYy2VWBFUlS38E_VrOT6BX0bgKo5y4buUdLDIgMDylCRMG7MU4LkDW2wBn9saaVZBHycZ3I4W5ZkOq27cvGyxWQQG-FYLdjFZyHiuQp5J_PdIiuSONL7-DiltyPMVmghxZV4DwEztpAOrTieyCrKIyeqisA8L2HUOQFPV8BhW4JISWPEBX89jOef5FhEgxIrmqzHp0OVwjNPAAH_JBMYTa_t2zfF0ck1qtXChZkjLLB4bWA4DPeRYTJB57yD4554n996lwHh2ck7AYiiipJNfvSVI70z2b5fp-8wAEDSxWb40HzdUdipMyz4WnvSWpRbD7BHVFRoXzQY9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuwTxsnVJrKEi79g-pIbvssx1rn49Am-sm2l-slYDsz8TZN6Zfxs-112waL6phBlLa53lU6t4u5h6QEfHGLAUi2aT9clxxRASUMWXfPAuU_uFfyGKhP7yeLyI49bSItQ7YjwdUR6YfJ5w7BVI5TZM2VxamEMHdwwQz-oDQUo9EDiIZKBIUYYHF7a0CW67mRHS6MkDcikvlfXBMtfJ1WXt83Q9-lqJPmgjl6wQMrPY9OgFPWsDQBY3t8ydKeroUhZRaCGA0MHUL-Tm1x2q9qaVQucXQObk7TnURqyULMnSEa_NS3hxnXZeG9aARCFy31bAhAXyzUPWS16GX4QBEAAgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=TdpJIOSiO7zflhjZhOvMaN4F-U_A8e6ltoqBeC0nI8W-B2s6mWLQaNGm58RX4HX2F8exmmsHKGrcQ5u5eOs6bJ1eBqcEwpQChL1MLanohN6ySpTYBgEiC0DKKr1WFuOIjfyniCZ16jtmj7jr5zwmtL5_VY5zOsiSjnyL_s2aUtt69EtYn_ToSbN5keIiDzSqFSJA7AXhGsM4FFP0C-n2KPYRJZWraSdaySP6b7_Gg10r7Y0xFcU37QjD3r0uIaNB2Iq5T8aDbTc0VGVPdKN4hiAKslpprDmKRY8xx0mQQJJ36oE0RXIjzcuDCpjKQ6NJa2P12aLzaZFkdXiJgxukuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=TdpJIOSiO7zflhjZhOvMaN4F-U_A8e6ltoqBeC0nI8W-B2s6mWLQaNGm58RX4HX2F8exmmsHKGrcQ5u5eOs6bJ1eBqcEwpQChL1MLanohN6ySpTYBgEiC0DKKr1WFuOIjfyniCZ16jtmj7jr5zwmtL5_VY5zOsiSjnyL_s2aUtt69EtYn_ToSbN5keIiDzSqFSJA7AXhGsM4FFP0C-n2KPYRJZWraSdaySP6b7_Gg10r7Y0xFcU37QjD3r0uIaNB2Iq5T8aDbTc0VGVPdKN4hiAKslpprDmKRY8xx0mQQJJ36oE0RXIjzcuDCpjKQ6NJa2P12aLzaZFkdXiJgxukuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJP1x6uLZ-abyLfoYSAJ9lh1L5ySpXJHEJKw1yurlKJ-cjPJHV0z7iZb_eHppUs7pzbUVGMxQgqgxbhB4ACmoqfNVf2g938cBQhimFU_0m2U5a-AO2wkSKKkpR9LTtTLAv9yhxlDDWqocr4GnmM28kh5uI29XrCxQaKfFEvYbA5ljFIdHNsgDJWIWT8yjDjK5oL5FUxSbDMDFBvbOy8v_AtFtMqKUx8GNFgBdfGkSNw4wATnh9BSlbxekJkO7leDclW5cd9OEedPdJ_zJPTGfPudg0LZyzbLGjHD_xu40SJqNhQ9fkKaFnAeeFbnsczXd1B9OMFnAK0C9urCiu7EAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqluGlF8VIVAj8y0WMnQeeqFkAYkw7Q-XlBoSTPzytECDiMjdHjcwTujBSI7avB0-tBp3lWnI-g1i0QVZ5RerJU-CQ-4-zF-WUDfu9eXD5Tb_tZ8G_tZ-VVeNvCjkyS7pCe2G8dDURKbHocRQuWptAITnvHy_D6lezXQ-O-o5CoezY8A9DIWrPVFewoA2nDW7IuS-5zXyq0L4avfTdLrX5-wFgkGmS3wEUGq07NPFc4gP-o7oeBS6pfq6pk3TdqnQ-F7zrfgC23JBvpEc44PU84UHfle2BItzmtjWOE7fGv70lH-Y5X7X0fCKIqWsUkXxelBhSB-2qqmsASxQechSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5E8LU1E7Bcj5wSypaZfhKUKCdXuVSscTpDrMPXmO3zLtFrUr4MGav8r6qJZtiOpntjFUZSrNGsEr0unTW2asglu8r7MnFtfa41k7G2V_KfKFRvxxYpVdbUu2TfhcNaqkRakaMdSHmOjlhBvLrNDroe6Tp_wm2Zum1afIZ5NfRM2hA7J3b7mYvFV-LJ88nAISaqmEg_4debMEfVhb9frYCzGdahTcfc2QCD713vePj17wNErw19IMdV20n8o1-NVEaTwpArjfVB0g6-T0-2hB3bAjrAUc6iKNiuNJ-7QB-VCQ1zB5HChlgK7yRHJb-Yke8sQVMmf_zcwXMrwRPRVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esgLePNwQ4O0fyTGLG1fmL2eQhmtlmrao_ulWaS26cvf9tMRfJSuoXa3kL57tf_YegdMUO4noWt91b7qi4yDsV1yWkF9oTtd9WRhvoWQiHG74UQelva6TpjFgx-TbOsTFkCMBNJLXLB4_25I2jNxS9aUitHJyGgek3crt0noj3EquAkCt2UzdKTS6XEUYBM-vQXJ6vgvveEoxN5e_SZbUVA8MT5Op8mhVa6SXFwiIdNNii5YP4F-A10W-WtZKBgwOo95iM1YzQY_mpmCPb9qyeTnzMtYhkn2twsDbsW2GdOS9WukkA5a4McVK4yMtp5ixQ-NnviBP1U9UadToMtHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_lr-38jcCwC4CpMEFVnI2u0TT7_EEBXfVER8ES8XEUeOb-YjuuOiMk3M-lxGuMWhXACyOqFgRBo62eRaXkzgvNYOcXI64ezh5HbmEC60hJdvqSKzny0D44jjOLf0TPthBqxi5VzCIkkC7MttzqCgJkjoQmOo3xUZWw6Zekp96iCdG9dJp3lqlT0-fWkbMNxjSVX_3RLH0viA_A6ql4gbZFhN5LMhhtoSCwyj33zSb-oRpIldRtcUzO1nBt7WMKD-02AS_a9OvFNLmRRscSFQH0gFoKCy6XSLyCiQw8LsIpIPpy49hLASmQihSrRES6MiMXwELF8pQ5axQqQzQzD9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNFVcIuiBybnNYMOXr8QKuW1IONEfAarTRJNMTuYPRfjceYvCRl84A76-h262M_BULTbmGSiFEuQaBNFB2wpyi1-rKaRS9VlKKlNu9F8CbALk0GCFeZvxUQok6pB5F6VTh_OE0Kt360oEtZlvYF4F4g1RUrzLHBrZlMdZDH2zTzK0TwbMJ7S6YLKaOFLPigimN0iT3Mm212PBxK1lP6pIH9PEeKvNOz-DRS4bbEv5ibtiu-Bqxk6TFoM1EXLxavd4vMlqPUoPkFo-AZKnaAl17D3uH0vNVlaucNY5hCxhgjn88OXJnxEz03Ky0XpZcYSrRIiDeG8xDVkTlKIfowI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK2rz9eOwF7A4UlJR0Iu5xNbCgPeLnNLNzp06GssmyQKzpwP9CNsLrbiQ_5sRyYcoanQCq4Egl00dTQSe62rIM732txt4N1OR3S6KKd25imFdT0nFuVCoObw-mbh01prK9ZpWtjkixnoa5f0-XFlH18BAGylFGkIsnuTpJu2Ahfz08Od1bvB8ItG-XkOFoUTCAwKY0CB3rNrVwD8B5fVJI5r7pN1-Wj83C19eSc-KOLs4iJa5Itd6ImCWw3oB3IsSFG08UGUZSkoVtt3i9fpZh9Rdxxzb1bJTcRgkCegMyRmVRC-dsIZr1Eb8GxjiYdHp0oe8kKfKh7_EKfDFJARHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO5DzBsQY6uBfMDE5DjM_YXWgQkqVirWL2ObW0aguwc6e42VKZ4wpve8TD0HmIHYJdL0SEW66fipSFhONbzQjpf_Z7ONXZgtcqARnbC8hvWUOQgSGfjBTRoio62JYnafgbH3H8taByV47njpjFdny6EMt4v8wJxHKPRBxACM2DUYyYjYxwDpBRl5S954f-7gBdgdMor6FBpi8ofrOnRJj2lALoCabuR6Kf6Gy-DX9H0LLMr997uYvK202mx2b0SVaKFRF8iuiviArSruE2MhVv0mhyDvN_Noe4SsWAKIaJTeOLXuP2EALsWyyPcw9h2DLhvJK2GaNMVRRtL1xukAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijwQOa_clUzSGfxnGYTE55ZZv3YhuiE0YTj_CDtiO4pTfVQz_YtMER2fb0UMG1qDyE9_klCVwsvk_A7Yk4D6-Cm082itYmLzJmN4MIUqgTMGC0Oeoj-Wc-LU221ATuQSX2wBThWKqzMqH7cTMmwiGUGBtDPO_Dm3DPEU3Rw0VYz1nz2RivlDGmNs5eahKRrs9TJlzlNETSto73RCpOtpRliLVDP6OiGiK4LmRt83sMr8hlGlVLH3F2YfSNCYh7etIEK3JUi_LvyQfgXmSkWSurFwKyOLcyrTB2_HEb2GcwaXZQybKP7jBJAqEN9od0MQCArMxrbK7a161na-EadjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdXWAghiFv4go0aX4K5mJbKpmPMZNEV-bcqesS-GUsGOyr1MG2OvvLdD7Qn2OWN2-ylU0Lh-orupG6ne5YlZa8i5HSP0WWFPfbohq8RONEELnTtAcZy0ptfUJGuWQP6gOceXLkk75itcTiJ8jY7X0M-Mrza9GPOdAb3PRLx_lmNM9WnI9ZTqzvPDm8nSN5QPoCl89EYr9-MiNXZXCGAZJNDyGMUwcpsVnV6S1H9B9qiELMM8XnEc209lNnwUfT1O8vIsKRjN0RrDILm-Iw6bZ-Iz7c6ZO1GHwAZ9UMjq-yHSbllINxTFaxFUjm1ar2l2L4BuovMNbqJU3CJ1IGHurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1FbY_AXFsu1_pUc921FYCRtcyu7lBfF3Nb4Yr89bwuAfbmhgv_FSOK1YKeJtXF0RWi-dD7cRlIhUkR72r7oDrKCB6G6Di_lHSmV8-zvuchHofqQDNq0d9EKp-CnH3FeUK7a-lHrUoQcXECjgATOGgUVPra6rANTfQcsQ9uOVKIZXDAvFvrC87JYqGOqB-0xi4A7VYJTfN_xr6VoDao9_7_St1XLtDuDnLco-BYh0MZAaJrsgP_xEpHnUW3KOeHJV5_0fcMR7Grxcz_W0JZao7QyW7c6lgbZOtDf0KmSxmhuE_ytez_hGCGdp-zYW7qKJIFa07zeGixuiiBEqcHLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQIsvEblQ9-1FV3Q4nWexF_w7KeF6OnwSXDvZ_qRIsaFIBzEFH1am2x-QtdY0ojd3NjE0HqzEx-jN60b0yQG2iRPK3jrcChBbJdFkf3hXMuYf7d_MlzTPk2x9v82iIMgQeJcWz7ZXnHHr3oYeIC0PdDI3-p3IwMFVShvQxrJodme9_NSbvzhGnlIBJkB4LtqMu8Uph5SAvpbq-0l_t1KoAIJPqxC7gOwPtsj5n4fYFk2FUTWS2Zh4LN5zp9qRAJ9QLTNvMvoX0jZwPCEEHH8Fu-c3VwQjo-_IXRAuphiNaeMwJU_NNPG0-ocx5BHE_GXULhnTBdt30uwxiJvULqowA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SD-tMpkC_LDgca-AmeWgr4nwO4iebhlULvsMaf4YCJZiOJQawDrk4ZQGujI-hLhHjcss-MQ10Et09_TJNZxoNWD702w6A3XRUMWl8ErLxPi4JUh1Y6qvkkOi8dfqFNbRSBuGC4FbN4u4F_cI2cDW1MgbSq9KKkBeu325hMOgGv1KdTQxaR2-Gi9Yoni3c8H0pr-kPbtJO6qBVMY-Wk0LqR_6OnTr5e-K9GW3u7cghpzev5GjfFsSF019suyy5EJyob1ZH2kRLpp5G93xNFCZ8R8t9LB0-0CI0MWwi2azc8pdtH9f7VO35sr33n0l-rNE8jQZug6D6T-Ol_y309ZqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5IR6FMc6jD5ZVuJV1IX0PZvxp_RNmmSn3voAD72Gx7QWDb8_XWAea5BWE3fRoU-ZbbT2yioUcSd6Zc_2I2JwkQfkjTt4B6yNs3ZVTnv6z90KEBeXHBam3-ziXNeNanFxz9X--HVe4OUiVHOCp1wudU7fH9JTB6gapz_Zs1N16K997r0pXc4J-K07vFYJNsyatik8zTyrzV0q5e7Sf7hHJKoSKMahgnFsTOkxo4uSaJpP-1Dg_10HYeNX6mGXElkYZAy3jFCUlXg6xJ2AIy0OCjQ5AJLOOgeKKHK6VXJs21K_Alrb1uWD1ETid_YJ5GAd4sLA479IB6427geunaDKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
