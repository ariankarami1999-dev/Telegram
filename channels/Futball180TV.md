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
<img src="https://cdn5.telesco.pe/file/OZ0kO7YCOaPhZVJM_qAYITFKP-GQ9UlfiMZcIVc_7r0_QuK1_2pIqB99mHEcVlFPCmFIXPEloULgymVVa238xJETU1OrUXKYP13cGRcqu23592m5HkSwGE7x3IMWhoRoy8TJqSSae24QcxJ2dSX6rK2-BG6ZIPZOUEf4A9edlz-ju4KUTkydvvuFEgeskiETUcQYAoloZhWz-f6lKruLI04oU6SFSQassomQRIMXDwrv5B-wTg5o16Y8WdU7HLSUqTWTxw_Wwuj9YvgVR-sdR3pvVIwuwNSnEMPtApcomS4RdFDD7gGVCwpNreLjj8WGu9aoiUSJY5YOQI5UxSsWuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 317K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-91837">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMyj-mMZOiqC6swhm3T7LEmZhGWufhDOkc6yEbv_kkyW3v6C4KWglBLUGmAP5GAMdGjT5viYEp4bvxIC8x9pTAePMgjwyeSC1tSEc7B_pOZwpSTBFzYLIkdAEbimE52vybMFJVSbyTUrdjYqXm0q23AuTKkKJrLhr9Od7SQl9gJHhg96uc4WujgYOT1e5gXT9wFvEOX3q_z0uMu83M9d41ETtBAIj-C1W0K4EC7CWleUJnUWHG9LBx3nmrYrCic8zCYXUb7uyD8ctJZk4AdWJu5SO9hbcOpt7eLrx5c263nV0k6AhVYiW4OkJR5CNWJKPKWk0yag87E2pOEP8d4org.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکتیک‌های ناشناخته ژنرال جواب داد و دوکو امروز 1 ساعت تمرین کرد و بدلیل مصدومیت تمرین و ترک کرد. هنوز میزان مصدومیتش مشخص نیست‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/Futball180TV/91837" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91836">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-v-nYaz3tHOwSf3HORhxrZ0S4i3Ts16ZIZ8IDdlXzfFgRiJ5W2sgZwFxQAsm51Afyi2NYcMirnsbq_Ty9ko27sL58UcIlXmBV0I5qwaG7ocoRVF_y8xHeyyQhmGrVi_hCvVXyaZHZseuV4Ln58IGC7gFRN588PiZq9L6ifzxzebySP8-ioxyL7V8QWv7o2NDQ4NXLqDDnDMtF9MVGHFTVEDbm5nsz3-6KcggjUbOUA1mAgXpjdOfXUBpm0smT8AUQ474zc669o3FrETwYgyJzOnVMjucL_stqyiJm5NWyqmNwHmIG2ovdxwQ6Psp5KfrVZHW_915gFp1p_8OP_FMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عمق اسکواد فرانسه برای جام‌ جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/91836" target="_blank">📅 14:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlcvsJd7MX-FnmKccSU2MMdy33zQ6huqt7xQjc0M1QDo8G3Tt-o4F0tU27doLewRJ7AwP-O8RTRJFPFxB7f8n_iO_yWufmhKt9F5qr47wyX_C1YVbry67YC5V0H4k_U_p1UC2VST3neoVZcMT61vXugasutQVKZt_n2nBIZImMIHMoTgB_R5hXB3ssHLYmeai1fSo3sY_LggYfmxRgIDAPkiitmQvs6toYQuFNdh_yYnAQUqtJ7Xfg3XhtDFczOssqY0qdyPqm97hinoecSWBslk86u5zODTDgsI_Nu3mR-HUvxbHYNrA9_kAThQNCzVBV1kNvZ-qWIQY9X3VlrUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گرون ترین بازیکنان افتتاحیه جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/91835" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_QNHOZJ8NLLp5CpbugPxlzAqeUxQ7cJdErd8mt17fYJRjRD3DBP-2-jIGR7bFWgsBI79OauaYt6HQmKfFq5ymnzeRtt_v8IZFMtoUL6bNhFg-n1kIJ6hNivmy2rBmssGT5YQltP1y7yeY7_1-xk9PjB21d4zZF-yLNJkxsB9cNpgaUjBnWd5_u0IVeij7GwPAMfhyZpiOesVKam2hyYa-BMuJ5Hs2hdhe7wK0LleX2iWn15kuhdzcrKfOq-jqqSa0cSGjNkce2M4Kae7_jBOdMSVoGrvBoHlKHUXwfb7aoK_XJayhlyK9DYzanq7B4KrY1roe1bz6hreUxQb-jT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوین دی‌بروینه:
اون موقع که دوست‌ دختر سابقم کارولین رفت مادرید، با تیبو کورتوا به من خیانت کرد. وقتی فهمیدم، انگار دنیا رو سرم خراب شد. اون هم‌تیمیم تو تیم ملی بود و هر روز باهم چشم تو چشم میشدیم،، تو زمین فوتبال باهم چشم تو چشم میشدیم ولی دیگه هیچوقت باهاش رفیق نشدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/91834" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzE_kmQXSaAMalwwWgp6ripSgNd_0Pjg5OfVuWztt3tI0n1LZ9PNZJOSEGp8MLExJ4yAVMgcE5nEMeAjoWWvOsqMxA8N7sygkzZQ2zxAmLkGPtdzBWtHwy498WEGya5grQ2mbJEScKpTqtfRRI6GKX70qlo66xUgTNIVQYH8mbWwsAXp_8mDYVzApgUW4twB0p597PSBagi7kNoG9W7lQC-aJkdpCmb2J3a4WOE2ohPthjNUAie_0JYFN9KVLFs8-lbgpY18CczoHhqHTfxHu6apoLMN6MTTNEk0cXOi3cy7d0PgcrheIXwMWFHwqhqe0lUOuXODNkMthtqOYbU7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
مارکوس رشفورد لوگوی بارسلونا رو از بیوی پیج اینستاگرامش پاک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/91830" target="_blank">📅 13:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334ebe9810.mp4?token=pbQT3RjGgyqdJpAwxNI2EIo5PSsGdlZooBSX_yoA0GQ-VMVFOf3sSCmLuHLcUdsYfRr-V3jL1wBGKd6kRIQOdrCSe98NBIXRRkPN_gL4SkadWlW5w1E0TKhAuwhIKm7aCbDohlvaUCM4RkiLTAs0Lj9nx8roni_AwUasSBd_2VaWfsydBdQVjoXyGltGCZkC4tgNSynr8Zm78OQe0n53gv5GTjGelzGpvmXFGr6IneT7wYJ97nfE70x1JL91b8KKDslGTY2YMbZ2JkN5gj-jIMgZtYJMVKfvmQwKrBxR-v1c1t0qS8WIRphwVjwWjECCvT709gRhd2NnY_jVIvPgXUFa7JRIkkOK3OgBbGQBwGZLy3YJLqGAzVjX_rR5lG26gESsY_hB01bXbINXF4DWoVRNPevrt1LP0cDAc01gk4Oax7Y8HC97qplv4aUPmt1BF6qFhZ45MZXrTGhnxVFOoHTUtmGjAcgFHny3UU5Q1f2QElp2tAWiIFreJNiy_ky_pt5lguN033Cs-A6mG5sGz1N2mX3cHXtp9PgVQ2Hco5PH-_aMNBYQmIXZfasSzEBkBe1THgDCPj94qZ_5NuxO_guRpFEpoAO1nVS7iNJoBDbY7M9BuQxWXATQPkw6gEiqJFJz4_7loukEME7ue7UUCg1G-gAKE0khITW5cYwc8Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334ebe9810.mp4?token=pbQT3RjGgyqdJpAwxNI2EIo5PSsGdlZooBSX_yoA0GQ-VMVFOf3sSCmLuHLcUdsYfRr-V3jL1wBGKd6kRIQOdrCSe98NBIXRRkPN_gL4SkadWlW5w1E0TKhAuwhIKm7aCbDohlvaUCM4RkiLTAs0Lj9nx8roni_AwUasSBd_2VaWfsydBdQVjoXyGltGCZkC4tgNSynr8Zm78OQe0n53gv5GTjGelzGpvmXFGr6IneT7wYJ97nfE70x1JL91b8KKDslGTY2YMbZ2JkN5gj-jIMgZtYJMVKfvmQwKrBxR-v1c1t0qS8WIRphwVjwWjECCvT709gRhd2NnY_jVIvPgXUFa7JRIkkOK3OgBbGQBwGZLy3YJLqGAzVjX_rR5lG26gESsY_hB01bXbINXF4DWoVRNPevrt1LP0cDAc01gk4Oax7Y8HC97qplv4aUPmt1BF6qFhZ45MZXrTGhnxVFOoHTUtmGjAcgFHny3UU5Q1f2QElp2tAWiIFreJNiy_ky_pt5lguN033Cs-A6mG5sGz1N2mX3cHXtp9PgVQ2Hco5PH-_aMNBYQmIXZfasSzEBkBe1THgDCPj94qZ_5NuxO_guRpFEpoAO1nVS7iNJoBDbY7M9BuQxWXATQPkw6gEiqJFJz4_7loukEME7ue7UUCg1G-gAKE0khITW5cYwc8Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار زیبای عربستان‌در آستانه جام‌جهانی
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91829" target="_blank">📅 13:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91826">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2045d7e9e1.mp4?token=Ccgjh_viNGwfice94K4Gt53Mf2q_LzOVRSvB0U0Rehku5MaZ2c1_0AuZWVUWgDvwpgtMSRJ072XUWadl5DS2AofC0y3EtDZ_HkD0pbRQcVdSuYStXXHoDi19PelI37Ws3EqVq_kL4E3Ob98_c1kbk5VrOJOolpwgSTbny7HZNEsFOE5tTbZb2ki5jN623DQLq8-PsmRNzaCa_JNayKU8p4X_hl0b0rW7ThuWzCIN6PfmTQjp9DtbBz_5f5VxmG_ORENZtYlRAqpFjczfVjigeUt2bR_maYt1A-8ykoitYXpZIDtrx8KXc4Rf0kf8niT12feAdghGCnBtgBt62_xUzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2045d7e9e1.mp4?token=Ccgjh_viNGwfice94K4Gt53Mf2q_LzOVRSvB0U0Rehku5MaZ2c1_0AuZWVUWgDvwpgtMSRJ072XUWadl5DS2AofC0y3EtDZ_HkD0pbRQcVdSuYStXXHoDi19PelI37Ws3EqVq_kL4E3Ob98_c1kbk5VrOJOolpwgSTbny7HZNEsFOE5tTbZb2ki5jN623DQLq8-PsmRNzaCa_JNayKU8p4X_hl0b0rW7ThuWzCIN6PfmTQjp9DtbBz_5f5VxmG_ORENZtYlRAqpFjczfVjigeUt2bR_maYt1A-8ykoitYXpZIDtrx8KXc4Rf0kf8niT12feAdghGCnBtgBt62_xUzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
جام جهانی 2026 ساعت ۴ صبح در خاورمیانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91826" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91825">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaP0njFBjT28akz496dQQpgwNhyr34ZLmj-vPb6D2zNJ5_5fOevXeHv0VbsvOH9Ezn_30MLKx1C3PWe2cPkwA_pDn0YqGspg-9Dv88jhD3St1dMgXQlI7jBfZd3--whcOJ8QChCvQDCON-neR4LZL_NJfH26TSGgumSCcwzUHmLTIOxkUABv0RxIpmlQ1bdGT-717c8NH27DSN9fl7mU180ZKy2PvWC9SCEH-xsFdfyAMCc3C-JLPDdQ39aGaiczT7RhiWrn4M_8eko6oNrgV6_agAJ1Qsj8JyVXtP5d9kdQDRS5KeIg2ES291bwqoXbOIfiOt_JOIJ8Pgs0J3GluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
مارکوس رشفورد لوگوی بارسلونا رو از بیوی پیج اینستاگرامش پاک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91825" target="_blank">📅 12:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91824">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
ایان رایت: رفتار میزبان جام‌جهانی نباید اینطور باشه. این جام‌جهانی، جام هرج و مرجه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91824" target="_blank">📅 12:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91823">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrgBs9nsRfOVy7yx6KBiVgGEIEBU52NXUwtABmaQu3cBeOkyZNqeu9z9MOdL9hHk5EPCnx_DHLyv6OKUwsoHPwUMYzWhhkyGjCsrme5SCkaOO7EdQA6k8wSS7fG31A04Nn-bkO84ZMdqTxy85Sq1P69tScY5qrJDqyxhgIdBQ3teaTHyU7uIIAL7c3CFe9AUnOH3SPyQDdrRQSrhnNNOU-o2ilXMZSbsfQ6zSR97pa4sia6UX23nP-MPVWckasQYyPYalBld61EQ3Nyg8brGtGAvw453LEadPzps97YKEDad__X__3O8Ce15Mq5xS4_CfYcXkflUAwrBN6K7BiGfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91823" target="_blank">📅 12:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de86721b1d.mp4?token=eO8SYkZ8Ziw7RC-TIhaxcddRsSOgRPZW1JNo_VYaGSJUHFInSbM0vog313_0n24pV7IctN_SLqEmYPZdknCQVQxaSsyEoNBcTVHN9RTsoq0rA_g_h84JWcEvIG177557qE3qsHKArg1TpVgPJY3dZDWOr16JarFRs69KyfQvFA-CXf7KmHQ_2jT9AglIVHVrZH_Ma7JQhUZ1SmWSuKZTG77rX5xZ4-8yHnwkCT56NBnq1VdzUdvKXRpx5OxxrP5dWPEZRGu_As0plbiSTlYjykSToWCZc5BFHJtvXZRq004XlIOf19-Jtnt7Gat9d7bczbSqUpXfNIYu5RN8LYYDjHNgtFmdHqDUokWfATPdSjLtDVAIkdNpBuDwsIjbwzJe7FcokThfnwNbHIkj2YUijpKDj9-gJfMANwQbFVt6DFirRCpgVp3AzUW0Nk9xatuU_pZblKg_qy9l5msSM8pVtftpYK2Eijcx_AlF4QqWDOkTGbBAJTTRPi84Zgj46mfgTA_qCu5J9QZh_HXRG75T94g7HxY95ayVHhWnE_bNT5j9LUdlrzXnZcQE2KFSt8oTev0LSEPRwy6OzB4qZotN3pOguypjDhZlfJB5RlO9JQn0w8JaIRkrZx7_1CRlKQov4lKqaZ0NMBDj49ZfPAdUD2baY6feH-RnNbGWuAQr5Ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de86721b1d.mp4?token=eO8SYkZ8Ziw7RC-TIhaxcddRsSOgRPZW1JNo_VYaGSJUHFInSbM0vog313_0n24pV7IctN_SLqEmYPZdknCQVQxaSsyEoNBcTVHN9RTsoq0rA_g_h84JWcEvIG177557qE3qsHKArg1TpVgPJY3dZDWOr16JarFRs69KyfQvFA-CXf7KmHQ_2jT9AglIVHVrZH_Ma7JQhUZ1SmWSuKZTG77rX5xZ4-8yHnwkCT56NBnq1VdzUdvKXRpx5OxxrP5dWPEZRGu_As0plbiSTlYjykSToWCZc5BFHJtvXZRq004XlIOf19-Jtnt7Gat9d7bczbSqUpXfNIYu5RN8LYYDjHNgtFmdHqDUokWfATPdSjLtDVAIkdNpBuDwsIjbwzJe7FcokThfnwNbHIkj2YUijpKDj9-gJfMANwQbFVt6DFirRCpgVp3AzUW0Nk9xatuU_pZblKg_qy9l5msSM8pVtftpYK2Eijcx_AlF4QqWDOkTGbBAJTTRPi84Zgj46mfgTA_qCu5J9QZh_HXRG75T94g7HxY95ayVHhWnE_bNT5j9LUdlrzXnZcQE2KFSt8oTev0LSEPRwy6OzB4qZotN3pOguypjDhZlfJB5RlO9JQn0w8JaIRkrZx7_1CRlKQov4lKqaZ0NMBDj49ZfPAdUD2baY6feH-RnNbGWuAQr5Ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمرینات تیم‌ملی انگلیس در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/91822" target="_blank">📅 12:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91819">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brMgpg1wz-t0haB4qsKUllZIqgzGOWXNgUiPauzuO7vWM1lxPMh7R0A-Fs8S8Sv864CZgm3fhuGJ3OvRCNk8XMuzyAp-HZ0G2sSbQ41uoWyaK0aPTltGNZaBaM2MDV0GvKHZtdQ0ZHY5tMULUm1GlI29ZRHVvXW79T4MUnCabb2owFeYwrXf8WKrpBmCTe_JaJsDW9tamBdoHSTFPC4ScrnhL7EXKeyIa9cq6AhJfyoPq3AaDsrEfz6EPG3oCAQ1Lda4UGk-NL2JNhEpvQ-_mm5Wx1ACcmtT1rtjC-jTA-EncX69zQ7ZCAXGhxkBuXl3ZGv5Kww1YAfskRqDcpR2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJd6Ru8b52ztG-BO_D9JyA0Bjs8Woa4uIgzH2ZR2Bj7H-tBLOP9HI4yjPgtDvH5LvCc30pB2PgSEr3Qwj2PZPo3L4d5h9W8eO459ZCDBe_cDqDuu2dV90CZhGKRdeazdaF3vE6fa7BueqaRRGfPfG2EQIQP8L80uHAmJXK_IsKsxWFW977At2Mv-5x-YorQimYO_9mzna_c1qKUimkhtgrSoMpo-AiMotm0Lu0H3TqqiTNeoRojhwR_qygDfX5i0mxo5ULKyS4SsNFX-G2Y1jpGLVyEz2ehyhAD7AZ5XZq7ttYFhlmhsuffbuksLak4WkL-QJegC06bqR2Y1hxrQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipYJbq4PyaxZi-_6_Zic9tkvB8ZQ4CjYTLQmkgone_HACEvUkg4JzuuHa4RSglh0us9mCubSw1E7JX-_pZxc3vLse1iGMi0AI06qJuOAN5GOp1oGtFdcvSCh7FqGwxjccFkVIgQQu69YF2AeWR1WxxnIAYzQjU-QpLPEFyknj56RDSFEaIbLmFatYjo-no4F1Cyk7QXZL_NBWn9CbCMK0ZjaB4dqbSZDbWRTRbqR7AJRUg-SyUFXyy6DYWLZf6ivkjoq8oqEGugq_3d6ZLBr0UmMmKQn1o3X0kd4SEd4oK_nKh-CPZ3Y0gNq3IhmqcT0RoFigAsnhxdczsZFaEzd1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک و همسرش و بچه‌ای که تو راهه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91819" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91817">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw6PPjJElrjkT9Ax3lZZfQ2m2Vzo-kNMh5nk5UL5MSdNA3tA951FP963_ueu93IpIVC3k6Qzdk3KudRg2TBI1gR4SwzL3to0x0Rc9CFOOklaksetJDZXzASerJ-05B8BF3BanAQ_UREVwqs0mTANgvI0Djr6ungEyQt6av7zaBuD4ezaq1lEJ1IsieRiOVjKwjxgqnbJ4IAmCQTTPZHw2FVp7GxiCZs-qrFNsIG7eY0UxtJj-hoXUd3ibuMf9YaBlyh2BUI4brDDkBx6PoKCUDtiLEYss64djK7f3a8KTB2fsl7OXyeiTHMvGe0VbFkmubAzriy2kWoDxA59Tm4A_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPKmOfOvnP74resIzShUcoJqb9wsfs2kBi7w0B8mdBgeS6rpqJxAQ5aG_lwS3dPI1mEc3vQOR2LFrHzLPITPfLPRbkY_7z3O17aR5_Hm1nbL2bMwS_RNQACRkzcsH-1MJjV-bw-TmTqj8ajig7bRKgJZR1tnkyEgV-tn-hY4NUjJO-AiJyLtA9C4_jBNJYQS0JsnJ2FY5UmUM_5EMsiFgJmEXFjED1i2Lan6B3nQVkgZNrrSp0PapnWQ4bw5gX14jnu_ZnEHCSmtLBFI8cprO-AVr4zZCmUGE5ptI-5S65YSE2BBOc5Bb6U5YptUWB9EFPPtAEVPc3dYz4okzHEKYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حاجی دیبالا چرا هیچ تغییری نمیکنه؟ لاشی هر روز داره جوون‌تر میشه انگار نه انگار که 32 سالشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91817" target="_blank">📅 12:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91816">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfI2P2qTB3PRupDPH89qrKpMvBtFY9e2fL61pbGmVxxJW83LhrHMjn_5huz5jHtXkedwut_rb1WsObBRupB1hvw1vCw-H4icZBCmCbjtq27qKnr-F3-AUVlG4wOzWOiHok5-nIuNWRegm9-1KnJ1gcBrpSA7Dern4qdIE75cdL8-_KMV2tHrbCwYMIlvqBccC_lvHO-imuIIaY4IKMgSp1RK0e6wctBOSh5gLY5cL7hrqQGaxtd7Sjnv6X9LzGeGWqh-Oj1PIoQsXaECK1rrWxO18XkYyv29L4aGWbQiRRneUQ6LkxBvCJl76lWaN47Fk5cIuwFCZ9x5u2slwwOw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇮🇷
پوستر خوشگل فدراسیون فوتبال ایران به مناسبت یک روز تا آغاز جام جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91816" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPA3JeioSCIU6vmNmcbYCt7B_Dx9z-6XB224Wi93mybnZgQWy2UaYwFsb1K6xDrlDl0RHCJ84vrJWgaJ_YXFhsYDNXT6jspDvKYisT0kxv0WLePzLzGPBEe1ru01oQLW0RM5xOo2mSbORizpclGWOavHLnvv6bkP4Md1O8rArSHSYBnUenspO-DK6eBmMG09PgQG7KFdUczVt08QwFPZIDEfErAQvhe_VX_UvaxcA9v0mI7vtfx4AB36bVUvfCCESWx7zrIwLFHDZTOgf8WfWeC24TSnmU-HB37dmVz-jfUbPoTpelacV-NpocfcMgbnh1s4JrITnR7NKAtfbuv11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وقتی در آستانه برگزاری ششمین جام جهانی دوران حرفه ای خود هستید، چه احساسی دارید
⁉️
🇦🇷
مسی:
🔵
بله، من واقعاً از همان ابتدا از جام جهانی لذت می برم امروز می خواستم مدتی بازی کنم زیرا با این مصدومیت کوچک وارد اردو تیم شدم.من خوشحالم، از هر لحظه لذت می برم و مثل همیشه هیجان زده هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91814" target="_blank">📅 11:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0475ab9a4f.mp4?token=o604ttG3j7f8tnjQnrlS-1m8XXYdP46ewtHtmqrgwB_vOHAFBR52w8biCujAvmWwDpylat12htNrO1SVd-QwlU9Xm-jXMjw13An0BaLS7AXtjYqnSH_JetbilV4yKUgWgihwW6HQdS8CQm66mj1AWAuPZQO75daXZyyY4rmzjFe00sHRprH_fYT0I0a9x3f6hfSoeh-HgZzw4sD2FWxA9IGUWBasgS43gAtmhGJe69KXuQ1wJRPWXupzEO8lradcpDd-gZ42S7MmWjRhTbtXtDE9HuhdC2eX_EVX9BIEjACSyEh6HLH_5rveJfE_JO5aN0rZ91MaNbHBHMtrsiQFvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0475ab9a4f.mp4?token=o604ttG3j7f8tnjQnrlS-1m8XXYdP46ewtHtmqrgwB_vOHAFBR52w8biCujAvmWwDpylat12htNrO1SVd-QwlU9Xm-jXMjw13An0BaLS7AXtjYqnSH_JetbilV4yKUgWgihwW6HQdS8CQm66mj1AWAuPZQO75daXZyyY4rmzjFe00sHRprH_fYT0I0a9x3f6hfSoeh-HgZzw4sD2FWxA9IGUWBasgS43gAtmhGJe69KXuQ1wJRPWXupzEO8lradcpDd-gZ42S7MmWjRhTbtXtDE9HuhdC2eX_EVX9BIEjACSyEh6HLH_5rveJfE_JO5aN0rZ91MaNbHBHMtrsiQFvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
رایان چرکی و دلبری‌های قبل بازیش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91812" target="_blank">📅 11:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91811">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzB3twmnmSCIdZjM5hKAO96-XUzDLpPBAMxqybgrGdjlqahXBiy0k6dWOYT6V68W1NmBvyFRdJIGI1gPy-D21HfrFSsk5ll7-4sBB3aUrm2YYSgP1j2Jpa9pb3C5a1ZRhsAD7irLgunLYpgX_Sc5QuOrv9wcUs0V1X9Hm9bU873CWJL74q6a6NUlU4nBgrnGE-Je1NlhizGCuqEgU6tqbACfURIABYfBGJSSLIS551flyVUjWRW4PsZo9V8iZB1B8Yg_Av2ADAo9jSkZAxDmhcTWtYkOGIA0E1HMbXaUx9iacMV7FSC2tRjjlWWjH3CfpcjzYWXASCrOBIVjaItsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال مادرید همکاری خود با آدیداس را تا سال 2034 تمدید کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91811" target="_blank">📅 11:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27028dcf2c.mp4?token=n5ZeJkvas9dRud1mt-wJUwJg9Ai8JeFwEHBzYArX5rcBB7j5t_z1PpMWoLAXxtg72T3JFX8lkjunM6E8zsSg962mQA4jGhSYncWuWbO39ICH8YotwZ6Li7svIAD3XlcdWgKEe7mMQYc5RMLRhwnusasd1zpSQVne6-mTgWXUhxc_BWRDgTiKoLlhto7eddQWr6ndn8am9yU3wy9czO6Lnq3dY2do5a7kftz73U0pS5Twr8_moq-unvsmlYBk7CAFHiJO9O_YN3EFo-IW_z0bWM4prGbqSQm2rmL6rPJg1zenEAJn3Ovze0N5f9eCUyjbmHLwcQR777JVU6EXIDNF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27028dcf2c.mp4?token=n5ZeJkvas9dRud1mt-wJUwJg9Ai8JeFwEHBzYArX5rcBB7j5t_z1PpMWoLAXxtg72T3JFX8lkjunM6E8zsSg962mQA4jGhSYncWuWbO39ICH8YotwZ6Li7svIAD3XlcdWgKEe7mMQYc5RMLRhwnusasd1zpSQVne6-mTgWXUhxc_BWRDgTiKoLlhto7eddQWr6ndn8am9yU3wy9czO6Lnq3dY2do5a7kftz73U0pS5Twr8_moq-unvsmlYBk7CAFHiJO9O_YN3EFo-IW_z0bWM4prGbqSQm2rmL6rPJg1zenEAJn3Ovze0N5f9eCUyjbmHLwcQR777JVU6EXIDNF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حین‌بازی رو گذشته قزاقستان، دوربین عنکبوتی معروف از سقف ورزشگاه ول میشه و با خوش شانسی، یه تصویربردار جون سالم به در میبره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91810" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiFlpeETRnR-UG82N3HB4R_j8at8Bt9aqiugfASuGJIaPkG1yjRdBu6h6y8qxrL-9ygzPtoup1raalUen7E24noBxFzPmVgwavA_duMl6iid71JQMWmDcmEJ2bp4TpkDcRoCgZpJ4PzeriFa1yrI5hpNdSST9-IHcpQiSQOTwukILlC0cHL9h2SFxUtuEAKaFu96Aq8mvSd2yKECdz1KUkv2T9y2Hf_dGxrLOh7jrdRxWCsmwkMZN-P1mE06zJq2wWgBsXFp2AuUbSdy2xTwV1pXlzWEmSkzMv0wAueQut_mdnH01QEqf877TuCOyTTREDzJEXYaZmxOTu0uG0FRRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد مسی و کوارتسخلیا در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91809" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgbRXTUDpeyon-XkXepI3ia_W3WjZpjea_mRJlHkn1mftIKmjBAGdWmadQTDEKDkISNMtAJGx_l67bvWd5_G0Fb8vp0FZfSij3GmTyNLfC7ejGnqXnbErWyr96JXR8m7y8rDZUCTgO94OrlAyc4DssGvSPhF0tmSMTZ8dCtfKOeokkFFD-zhy6_v_3sya0bO8ZgfgSglALj4O5Wxmmp5Bn0G6MeuJOa66tK059APahknkVcNXTFN4Iw5vVn9kd4B3ocpz2IympEkEVsHhpiGLdluKgV1surzoDuVT9dGgQKvhcUuvD04vLg-iNsvOD-xjGAKgJr0kvyXyZgO5Zxqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
کیت جذاب نیوکاسل برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91808" target="_blank">📅 10:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03756286c7.mp4?token=Lwf5oyTzscfmLKdv0gGVsaAp4_Oc068lKCRhA6oKHPI2n54i-XI_8AhOP-DGCrwjpicj8ne8aXLugBCIvJ4q-gohKGttj0s8QQlWR-jzYYpO8teT-e_JY8Uq2tbeHqQQSMc72MgSfK-GpdkHWeS5vIoPhEtDmB-nJf95X7xvsHMoxDL5rlHIrRgl9yIAR8Sq4_-0DWcsh2H26VqLpV1428ch9wUFLzWBXRJeI1MbfhjSonP8yYDl1Ehjr04ZgNoRdHT9iw4LN8ZTu8a4WzrOW8dUERQxfdAVpRNQTjp0fr3W7oG1Z68uBoolATPm70EtLVTMIx_lZThrxGyrkV2Nsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03756286c7.mp4?token=Lwf5oyTzscfmLKdv0gGVsaAp4_Oc068lKCRhA6oKHPI2n54i-XI_8AhOP-DGCrwjpicj8ne8aXLugBCIvJ4q-gohKGttj0s8QQlWR-jzYYpO8teT-e_JY8Uq2tbeHqQQSMc72MgSfK-GpdkHWeS5vIoPhEtDmB-nJf95X7xvsHMoxDL5rlHIrRgl9yIAR8Sq4_-0DWcsh2H26VqLpV1428ch9wUFLzWBXRJeI1MbfhjSonP8yYDl1Ehjr04ZgNoRdHT9iw4LN8ZTu8a4WzrOW8dUERQxfdAVpRNQTjp0fr3W7oG1Z68uBoolATPm70EtLVTMIx_lZThrxGyrkV2Nsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بارندگی در استادیوم آمریکا حین بازی تدارکاتی آرژانتین؛ جام‌جهانی با این روند ریدمان خالصه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91807" target="_blank">📅 10:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t44DSadR-AQJ-VxLWQGSLrIJTpWMEtVmx3zncl88TLg0_SxGJ2pyd9Exa4Rihdoz0etH4SFdjbacTaXeC8Cs8tYbNVVQM-GfFtMBOeWDvV7UJEoQeOL0An7GuowoyMQsIL1J0ZL0MklQV6Gsk9LjhNxnlGCj4DYOMD80CP35vh4qu3dZjiMUyGDZG1greCbDtUL9V7BFPOU3_7cwsbZWkn7gNCb4Xlas2IKE4AnPlkcq4BrmpBOJv3KitIASBtmuEKNu15glFEzE72sjKEK1_RdJRKzdHjtQLTIAE80FMmuEre_AiROwv46_Xo6-M2fW6AS64bErQrf0Mp6IE1u_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91806" target="_blank">📅 10:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNs3vYATSGbT4PRwMBYWsaIKNxL-ZN5Iv37GRFm7IlTS6J7YVgEAmm9KZ_xTA9JyhLrFTrlJlG6_j5cSI0uqUiwkRtjRzoSGoLKahhgTMNAFmzARI3o1N557ftMn55Mk-8rmjnWr_y_Frs-zpowWYs5tGG8zMyUbMBkt9k9D4p3qcxZFCF68yJfcgwajXY00lq9BAWApGKYconpkPISBzMDHfbO_2cQFhOHPtymSI8NzXpcihRqLaY2Tihuy13UGR_57AqljZg62lYArZjJF7WZYHf5w7medSDykAnLwaIcNyqc7N1MQ-V4SXMOeJJ6Vwh2jm3pOMuwz2h_gjOu7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUYgEpXj9UvceXEIrBIkc7LVQc6IvcbhGJqSAzkd5lUF7enoeRk5lTRjSoaguMJXDsqh-vnYZWS_LrW-V-IC2zFhr--ZIwlLGfmTrfPMVkN_GYXP-rhmzF8jKxsPKwDH6wOvyYBYRuk5MzZLFzOmHtyZtdALSrmpepWbyZDra8js723XRri2bJ2Z5LsKi_4zWaOWFRm6-jNGX3zKxciqZAnht7OJrCHsFiNS4_AOUWUpB_XFR8pASd9e0K6OzBpCSrYWIK-rnpKzubqfCyKjWvOTCY8h1BxQMtF8GxZFZc5yGqAUU9wlrxXIhxA1wGhi3m-Ko5Lo3ACF2x5nivt94g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ کاملا لخت ممنوع بود و این موضوع من را خیلی عقب می‌انداخت. میلیون‌ها دلار داشتم، بهترین ماشین‌ها زیر پایم بود اما تنها در خانه مینشستم و گریه می‌کردم.
🔺
شهرت و پول از بیرون عالی به نظر می‌رسد اما وقتی تو را در جایی که به آن تعلق نداری کاملاً تنها می‌گذارد، آن پول هیچ ارزشی ندارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91804" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI6g9RBNo6y8E1n-EM3jc1jIGAfhZpydQLSSlFoi7Nelg5yJtn7NdAyqb7CrxDofMl0pnojpuywKZLnqv7oA_hp-m8PPnY1qVEcGQ9GGBBCWFOi24tlG2CHauv10eijQm9pjCxq5uc_-MoP6mURF2tfghkM8afuaCMx1SbhIiWrmWxGyezfNndpst5zYwkCzyJtFgJPFrdpLGKAm_j2tEHi9BYi-6Cm9Lb6U4Hwmr_ejEPK0i2vRqhR9y6YzOK-klv08V5Y1vvjrNliyJNOFKbirVRsmcOgRGBjwAr1IEXn-a4keccLee_yoV-mBg1NFfPMABY70F7Q3a_taQPccpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfFHjpodc-uVxfY81xYMPMCOtkzBYfglLGoPGet9j8QjvN1mMWtXSz7I4z4qcH3YQLNs-2C6M6lOg5b1CbUtGLB5UPdri-pP_ByY5XrE_Ya1ZEChzVs7Gh3xoFmK7S79j8IAuyWJ3KRyC_-sfPMbLSfPk4wLr0-zrnVGB6wrPzp8qbdT9j0_0dk8qAEDODfWz94V8QE3QJKxQczrhFV2JLq0ZVvumoDMXUXMASA7vx2OTfF10fCQ_4icVUvHgmOUFmdgYYN_n_dfOHIelfcHsfwiayJGPd67Ednk9cjX0enqasWIEMUyW_IAHlEiY0YF3-KI03bMQWeJDnd5UIyXSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🏆
-
ورزشگاه سیاتل (Seattle Stadium):
مکان: سیاتل، ایالت واشنگتن
🇺🇸
افتتاح: سال 2002
ظرفیت: حدود 69 هزار نفر
🗣
پر سر و صدا ترین ورزشگاه به دلیل طراحی سقف که صداهای تماشاگران را در داخل ورزشگاه محبوس می‌کند.
🔻
برنامه‌ریزی شده بود تا میزبان بازی‌های بزرگ مانند مسابقات جام جهانی باشد.
🔺
6 بازی را در جام جهانی میزبانی خواهد کرد (۴ بازی در مرحله گروهی + مرحله یک‌شانزدهم نهایی + مرحله یک‌هشتم نهایی).
🔹
مهم‌ترین بازی‌هایی که میزبانی خواهد کرد:
🇪🇬
مصر × ایران
🇮🇷
🇧🇦
بوسنی و هرزگوین × قطر
🇶🇦
😀
بلژیک × مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91802" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=GI7usFfn5IiS6U_PMOdvgyHpltNCx7I_vVFyujsPM0rJEspy65nEU_kcqotZmhxWnDbaYkxXzENQ8oMBkTV4q_cMWGRcSbXqJzHqzC-x-Z-pwsXfD2KvEBU6zpTcVB73q1U5cjr3I828-qQKgmMknF3VnH1x77SoR96TAj8N3QIgm1_FQM7snaxxyTARpaJ0_em5-UR_UtjmHaNQv6F6Je8YtkuwHAEcC9j3ANoHdQzJU3aGbfyY-5VQ7fLFegeaEhklvOvEsRLKrrD5c_GcJkPhNpZxvDXtJcPDAHz_S_55rLwzrqoKCEVwn3zwsTQhEZ01G6CgPi0NRKD4rR1Rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=GI7usFfn5IiS6U_PMOdvgyHpltNCx7I_vVFyujsPM0rJEspy65nEU_kcqotZmhxWnDbaYkxXzENQ8oMBkTV4q_cMWGRcSbXqJzHqzC-x-Z-pwsXfD2KvEBU6zpTcVB73q1U5cjr3I828-qQKgmMknF3VnH1x77SoR96TAj8N3QIgm1_FQM7snaxxyTARpaJ0_em5-UR_UtjmHaNQv6F6Je8YtkuwHAEcC9j3ANoHdQzJU3aGbfyY-5VQ7fLFegeaEhklvOvEsRLKrrD5c_GcJkPhNpZxvDXtJcPDAHz_S_55rLwzrqoKCEVwn3zwsTQhEZ01G6CgPi0NRKD4rR1Rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دیشب لیونل‌مسی از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91801" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzkbkr-8-Z_nO_tAX3PZLdx2fSuikVV1eEmMRXrYc_dtgdCc6JDj6uY_YXMYhXYpRlv9Cz9TfpZamur0AKr3cw4STZAa8xbznzyCyUR4fiFo7x9O3qvKpls7Eus1ESzRTDhRq-SAOrCThIyDIypxsFax5v4oa7IqC4Dol1dsQDC-c-Ahbvp6WgV1CgwiVvUNwSumIoeKHsM-9HvCydln7GgMNs_X5XvM1imxwCm0mzydJdLOj0WXoAVpLCrmgr4uycYYzDQygwZfsj-Ibd8-R6dqkArGRk50rWlcDtqgn_-VofpITeRDGToc4ahubkL2RgMDUpTseQpJIqNpmroMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNfoW9Zgow4uHvK5qsf5M2p9wa0t1F1ojkjeoWDPiS4cdNfaSzjPxE1qNofXqRjseWqP3_0520zz88EnXpbBm48b1d1ZB5gJXbmqYnwIeYG5HJu7M59ha4cWmmrA-DJtdjytYp3-pAu9B2KfBvwnn6ocbY156rhG7fGFQ9_lduDJEZGGG1N_t4ZQoOCjLS2qbja5N4DM66c9lpucGaa3dy49M4X29jXmZxUMOrHBLcXjRtsnuxfOyMYZffaKsPyGGQ_fLVjFlWOW9V-QkeLFSZ4-v8MNVp_sVFYDcVkl7NCLY3mE5cEkI_KBCEV1yRCIM8YK6AxmklCoPUafYSyiTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوفی رین مدل معروف اونلی فنز: هر کس تو جام‌جهانی آقای گل بشه یه شب میتونه با من بخوابه‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91799" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFlEsmiUiDFqYtzPc0_qEFqHowH8JXBrgr76zUfEM1QR_JQSFqzMbPslhyEonfwBHM91KeBrexf0nQs1FJVxdCrgaKRY4HM9PXhdcPqJM0Euos_btLukY4LaSPd6yBQIommuVAkKCZN7APiqyR1I5_cwrBDWyE7OlCOIq6InNnjnFD1SvDQ9_GvrAbfFfpO2kWdLJtBbaKUxUo95uFXab7ABCcKYATaGSnovX9dgPBGRjPyRLxeQK8XPZFXqEVSvqME1e41ys7k2WtMMP9ve4w9uKoW9qDqRXO_BHZv1t2BPy_QH3QLOeV0bWIPLp4GxXPo32NB0DBfs776Y6PimTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
در ادامه بازگشت سلیبریدی‌های بی‌خاصیت، دیشب پیام صادقیان هم بعد کلی کسکلک بازی در ترکیه و کارای عجیبش به ایران برگشته و در تجمعات شبانه حاضر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91798" target="_blank">📅 09:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
سپاه در جواب حمله دیشب آمریکا؛ حداقل چهار موشک بالستیک ایرانی به سمت پایگاه‌های نظامی آمریکا در بحرین، کویت و اردن شلیک کرد. ولی خب همچنان آتش بس برقراره و مشکلی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91797" target="_blank">📅 09:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HApsA2FcExXZprFLy8nZMhW5pZ_CTqAhksu265ycaH87cYYCM06P-8YJHKA1sV7BdZAXwYpb6vGvL7KrYFPufRaDSCz7Zwp_riuEl3FfM9ZFS_ifT6oRrC5kjl4W5GGmAYcwNo__011AULVUT17gDOhcBh3a1ULVZ73EqKv7bVXjELUYuHF6TAtXGUYVgTGBOba-pPMoHIufaoB4Q7cURNgKPeUYosBOvwl7lZJRUxoqe4NhanecuIlKDFOd0Bw0KrFNexTlyoUjVwnJlsEqBKUMdkgx4cghqjN6EWNWs2_V5Zqvy8YmQWTNRlWAf9OyvkYADDehyJoLq_zcVo9Tvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رودریگو دی پائول: میخواهیم با جام قهرمانی به کشورمان برگردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91796" target="_blank">📅 08:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIbLa1Sqc9MaNuou7qwEBxLIiD7-SnSRvn0NwmrVLM35-Knj1It0qg96xnN1T11NAG2NnP6GNiqDCLvWFWjjxDIIUkGcXUC8ECejfWBnbmauTMyZpgaVgc840v73HRd3vpGlWa8Qn495FpZ11QLW2ai1hE710zF_9b5VW4jzburB0lTJghPRrBrOgdufg2kZAlVT2ytO4NngKd9lbEdYEalOH9pT_4rQv0VqgSLKbeiiZ_QWjHKpfezMpueq40kq-XhmSv3q-Xpr4wS_EIHWrOtnVv1WiszN3hRS2W7EUnB_ajfcLoe1kX67a1LFPX4U1OA82ulbSEQfDWZwGZ96CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91795" target="_blank">📅 08:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=P2m7nFfGXuTOd1N09Dc2O9MEGlb_PW7Vxm-sT5aHoO4j9LyFFWZnqxrVfMeSx9dzYrrTE9BEo-He2jdaGmA3epPrYdAFdCN0a8NEL3ZldjcK3oeDPxCX9Q4J7PQB8KOp6Uf86lH5voQQcCeJcPuKnXJjsVJpCAGaH2o87VGWgtw3VkTufv4nWje0CqBnCb--Hy__9WDg3xtsbh4tTS8A6yq0JOXtJg8IDymfoQkDjrZhLdepFu92n7sAOD9E2r8KTURHvDlwnYErP3J_EYDnulvpwfkTdfAeRr6YreUBCOGb6vCpLZt_1JzSuxKjzpfHvfwn0HFnVDEGXGtiEnOHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=P2m7nFfGXuTOd1N09Dc2O9MEGlb_PW7Vxm-sT5aHoO4j9LyFFWZnqxrVfMeSx9dzYrrTE9BEo-He2jdaGmA3epPrYdAFdCN0a8NEL3ZldjcK3oeDPxCX9Q4J7PQB8KOp6Uf86lH5voQQcCeJcPuKnXJjsVJpCAGaH2o87VGWgtw3VkTufv4nWje0CqBnCb--Hy__9WDg3xtsbh4tTS8A6yq0JOXtJg8IDymfoQkDjrZhLdepFu92n7sAOD9E2r8KTURHvDlwnYErP3J_EYDnulvpwfkTdfAeRr6YreUBCOGb6vCpLZt_1JzSuxKjzpfHvfwn0HFnVDEGXGtiEnOHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گلزنی مسی در بازی دوستانه بامداد امروز مقابل ایسلند که با نتیجه 3_0 به سود آرژانتین به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91794" target="_blank">📅 08:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcNhc3zaD8BH1mYmSdi7ET641-cRB6fJaoHOZxBweoBEbKPjeteh2wu3bJwlooMvbFedzZ0IZQNOsKK6WrxsQMSi6ptgMuSzE2nZvi-405kYVjpPifLzey34lU6NZkriFA8hy342HKRe8M9_s3OnZ5EFgecvAZtqI1GZGeDRYZC5opAdocALcdy936jvl4poIk_LImEchgNNw0qjchBtJ52qbr65LVxq2Hj0sdJIBJv0sMNcf1Xp05fjvYCYpgDQY3Uj9yWM2aqdFT5Hak6L6pa8ZmLk-QE-Bq_GARjRqkyTh3o6F8Cl4VVUZEnCIo06GYzdKxuiQY1k0o--xo_95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرزو رئیس اتلتیکو مادرید:
کون خودتونم پاره کنید آلوارز فروشی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/91793" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=sId5HnOVrV5gaX9Li5an-Pa25ree7rvbh_obIMEfBMWfhwgvCa7WZuvB-8sBNwSBtEV8t4JxPad_rDwBfim50ZdcJsQKtB8_Ob7PPM1unRydBNIrPRcBNDd3_jKqMotsa3hgpWRNlQn2gr6tdb66d9jYJQdHUtskwLWVfjbnBtk_zj0BNGPp0PmyQHDgWXoIyMHta5zeZoigicuK_kIHoB9d0MyLLkG88-iGkqR4BJlrPBR2n4CBkh67ixESYAhVmD6oq8Ei533csrSFxv8YQLo7-C9fHgZZgFvOIDPhh-dwCPXtzxW5I-CqmMgUMLJIlWvlokmhV1ajSXgOAl3seQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=sId5HnOVrV5gaX9Li5an-Pa25ree7rvbh_obIMEfBMWfhwgvCa7WZuvB-8sBNwSBtEV8t4JxPad_rDwBfim50ZdcJsQKtB8_Ob7PPM1unRydBNIrPRcBNDd3_jKqMotsa3hgpWRNlQn2gr6tdb66d9jYJQdHUtskwLWVfjbnBtk_zj0BNGPp0PmyQHDgWXoIyMHta5zeZoigicuK_kIHoB9d0MyLLkG88-iGkqR4BJlrPBR2n4CBkh67ixESYAhVmD6oq8Ei533csrSFxv8YQLo7-C9fHgZZgFvOIDPhh-dwCPXtzxW5I-CqmMgUMLJIlWvlokmhV1ajSXgOAl3seQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که بغض تتلو بعد تقریبا 3 سال حبس، پشت میله‌های زندان و درحال خوندن آهنگ شکست
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/91792" target="_blank">📅 02:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL2aw8x8lrb558ZDsPZ2hf8019L22srCnQbI34vRm_aX_aAKfBHuFmV3pVM-2IoI1l8S5VAHzT8SZDLvd1atvuQQa9Twh8K89myuR1FLHSotINc_WXalkZLIiSoZARQ86V34qttNIXbj3s4QpKfS_Hs5nyRXWnj17QHfxRn9ayXjhlgJ76u1lbpHdTC9Yeey-SyxuYY3xmfqIrzA-dSIbaDTnZmyc5LBGtqCgc3nuyQTz_CUhsAt1VGaJVMCAqpmj6CMrpdXidsrG4D_5_g8YY6usjVdhZJOXp8bx8XJx_P5j33gSq_XBrqdOaKcGRqym-q7LUX1VLLSwEFF7avxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
آلوارز شخصا با یکی از مسئولین رده بالای بارسا تماس گرفته و گفته:
من نه با رئال مادرید مذاکره کرده‌ام و نه قصدی برای مذاکره با آنها دارم و فقط میخواهم برای بارسلونا بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/91791" target="_blank">📅 02:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91789">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=lWJP6lsmBOa0Wv9JF8rIZQUO9GbzNhxIhkLbMhLW2l_tR7pkk27SVGhFMD_JpDdZjwpcfzRL3FKKsFgEXHwO42f_SnbQYpcS5vRhXEKgR_NgUng3UkBid8sGLyfzOZu64Lkh8wnjTOn1ufhHLIJ1LoPqSpuVgR6dv1pfvRSdadyDFXzbDKvoIF0m_K4Bliygoc9wb--JxkWfA0v3besF4Sa10De0fTkZ3EDa35DuwPqSBoFK4v1ljGeAQOkbTsA5va9ZmF4n9f13Ody7kWToV1VUtr6O-7zBfOehxe_NlwdPsRA0YoJYGWiHbULz2vQgqYR-Zeh0iq3UJZ6T4QN7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=lWJP6lsmBOa0Wv9JF8rIZQUO9GbzNhxIhkLbMhLW2l_tR7pkk27SVGhFMD_JpDdZjwpcfzRL3FKKsFgEXHwO42f_SnbQYpcS5vRhXEKgR_NgUng3UkBid8sGLyfzOZu64Lkh8wnjTOn1ufhHLIJ1LoPqSpuVgR6dv1pfvRSdadyDFXzbDKvoIF0m_K4Bliygoc9wb--JxkWfA0v3besF4Sa10De0fTkZ3EDa35DuwPqSBoFK4v1ljGeAQOkbTsA5va9ZmF4n9f13Ody7kWToV1VUtr6O-7zBfOehxe_NlwdPsRA0YoJYGWiHbULz2vQgqYR-Zeh0iq3UJZ6T4QN7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات دیوانه وار اوکراین به خط لوله گاز اصلی روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/91789" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:  آمریکا داره ایرانو میزنه ایران داره پایگاه های آمریکا رو میزنه پاکستان داره افغانستانو میزنه اسرائیل داره لبنان رو میزنه ترکیه داره عراقو میزنه یمن داره اسرائیل رو میزنه اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91788" target="_blank">📅 01:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:
آمریکا داره ایرانو میزنه
ایران داره پایگاه های آمریکا رو میزنه
پاکستان داره افغانستانو میزنه
اسرائیل داره لبنان رو میزنه
ترکیه داره عراقو میزنه
یمن داره اسرائیل رو میزنه
اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91787" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/91786" target="_blank">📅 01:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/91784" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91783" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91782" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/91781" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfUB-1qqEaddmABPm7CIVEiJIB0vZmMRFvz64pB_iTHZ8belA5Hr-7w_1DEyiqJFxQja5sNRRogY8BYSvgrPdzSk_c8kW0SGNb5cIe9BrqQklBwsrhjZ7SK2H6j2gGXBvrjYPxb09q0XGaE3xICJmnpBRGZqGUBNUTbCgU-Y1ZB95m_eg53GOgsOin32YZXq76dMcTMfvHkRMLkf6iEojGQ_GNiGu8Gab8GKYTSK04MAuPlKxi4EQnY5sN4wAdsQfchUQYpzZcHD2wPfeoqpI7GdToQ6AULP9EdaHKF440mb1CDeuCmz-P4Oxm2H2LT-LF9mUKMgsaRPewvZDDS0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙁
سید مجید خواب بود کی بیدارش کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/91780" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
فهرست اولیه اهداف آمریکا در حملات فعلی به ایران:
-پایگاه دریایی سیریک
-پایگاه دریایی جاسک
-موقعیت پدافند هوایی بندرعباس
-موقعیت موشکی ساحلی میناب
-موقعیت موشکی ساحلی قشم
-بندر تجاری قشم
-کوه مبارکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91779" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
خاورمیانه امشب تو اوجه : اسرائیل دقایقی پیش به لبنان حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/91778" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91777" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91776" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=LkWdaWIV8zjO46V-fwcXRs1at2Oui3RxCx47pGUgouTn4W2R0UbN0aCsGD_CGLbQMuU8iJB3OrWJZGJ--HH2EJVMoZL2B3Q35dov4IZDRWGJFfA96YjNI0WR8ujzPYAzwiS-H5cbS3W-RAwiejZSUaniQzbrVB4qf0rPt3zRVUQQ93_vPyo36ZWtZ9SUysmigkmiTM6WZqL2CkjrsZOFkwb1J4eNlxR8mGQlFPppzgysH3Ihd0WCxW3Zx3QELmi_2NObpRMZsAKB2aunsjSUOSGKNcJA2OREhrHDUItmsszWWbbnsHeBjWLTOl-VGIDzd45PALPVoMs0kFzOsXYOZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=LkWdaWIV8zjO46V-fwcXRs1at2Oui3RxCx47pGUgouTn4W2R0UbN0aCsGD_CGLbQMuU8iJB3OrWJZGJ--HH2EJVMoZL2B3Q35dov4IZDRWGJFfA96YjNI0WR8ujzPYAzwiS-H5cbS3W-RAwiejZSUaniQzbrVB4qf0rPt3zRVUQQ93_vPyo36ZWtZ9SUysmigkmiTM6WZqL2CkjrsZOFkwb1J4eNlxR8mGQlFPppzgysH3Ihd0WCxW3Zx3QELmi_2NObpRMZsAKB2aunsjSUOSGKNcJA2OREhrHDUItmsszWWbbnsHeBjWLTOl-VGIDzd45PALPVoMs0kFzOsXYOZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از بحرین و کویت هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91775" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
صداوسیما: کشورهای عربی شب بیدار باشن. باهاشون حسابی کار داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91774" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خاورمیانه اونقدر عجیبه بعید نیست نتانیاهو توییت بزنه از آمریکا می‌خوام شلیک رو متوقف کنه و به میز مذاکره برگرده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/91773" target="_blank">📅 01:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91771">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید به مناطقی از میناب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/91771" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91770">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ترامپ : فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91770" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91769">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
سنتکام: در حملات امشب از چندیدن موشک‌کروز استفاده کرده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91769" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91768">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: آغاز حملات موشکی سپاه بزودی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91768" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91767">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91767" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91766" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYBonctKPMc5W3DVznby2R8oL5EPDbB0yQ8oP3BLTNzuAB0R6LAcP9s6ZXNyT2TzpHqM2-GDk5FZRbaQ-OfeaqIYJoQjJIuK99m-HynZJyD2iPu9AfS9z8p50inEHbqEcNGmo1nrUUJdI2FHWe6eErz4zBKPQN5sYxwxu7CrcGHb-L9BFIDDgDQJ_1OajLGc11VQ1WIc3PzKklFuwz0ZcMoEMPS9us96J069fvHyk5FIa3Bvx3FK8h_A2pLsk1FlXWy1pmDZ84S6kYnv-OuhN8EClW1D84qEJ1UbozTj1w3sCwvJk7pPNrbrK6-N2j4azsp7RybiE5zQndzz4xAIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حداقل چهار انفجار بزرگ در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91764" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم  گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91763" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم
گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91762" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممممم خبرو داشته باشید افسردگی بگیرید
😐
😐
😂
تیم‌ قلعه‌نویی در آخرین بازی تدارکاتی با منتخب شهر تیخوانا مکزیک فردا بازی میکنه
🙁
🙁
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91761" target="_blank">📅 00:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممممم خبرو داشته باشید افسردگی بگیرید
😐
😐
😂
تیم‌ قلعه‌نویی در آخرین بازی تدارکاتی با منتخب شهر تیخوانا مکزیک فردا بازی میکنه
🙁
🙁
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91760" target="_blank">📅 00:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trQtLmmJfy7prQn3scSMLWyXxpSiI_9T9LwYn8a2nixPEVZ0Po5pw24GLydoqVmWRdeCR0FkXGiRXfNUSN_O-8p9YanX_FTbdI_kUu6b2wBban23L7K-yOKIplnGUYAZPfnFIiFJ_NLs04h3It4o5sBKtNZWSP0ew9mtshAFmZwE8QKXmjgh8q21Vme50PIx00hgwAy3A2hO9deiya7rGVe_vpBBaVzmbzcEeignJpfPnR7jgGcMj8jVsMoS9oBlpcsfXHuCqVaPf9T3EmUuDrRmeqmBT5n3QWO-4K03Z_S1DEHXH3vSyHbRfXd3jLIv9cEFXxtkgw6MnnkDttLoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
موریگی دومین گلزن برتر فصل لالیگا به فنرباغچه ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91759" target="_blank">📅 00:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2XL1LHgyFMv6TBDXv8Gf2E3Pb68A5SNkuZzl-fJKREbZdWj_BSpB9jbcqoyCzL39qg8Yd2KN5nn6mP_hFkKE4Ul3KCIcqOAySJGlj95c3Xlr9aUPUVFBlyV9aPO53GgA_HwiINOtymlwq2vbQLVvDzmHWnW-LlWPZt-0TCPwg9xZc54D7SYJMFLNEVDzBa6v5H3jLR26HUjor9D0mg8G4he81YkfJfWRHR909g7WoxBl4gXDd1XPG4zNn_Bz0hPYXdcniJfT-Kn65oiz65ZMHt0Jda82fcDBzkE39FdkmmRPpK5tQDbAah_2Ftihn47bhGStvNFD7e2sRaxbUotOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏆
#فکت
؛ هیچ بازیکنی در تاریخ جام‌جهانی به اندازه لیونل‌مسی پنالتی نزده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91758" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjic12-QPod0OkJygePfG9fJl9UQTLomxiYWfocOwIIi8Jb_8vRT_C0motwy-FTainp7cx318CORx5PSHeo5dbziA4NjcRX2csUzkMnDEpPL-Y_NbEcrBsQ06HpQ9JI2UXTJ6R1rA1261gd1bTGv-AGKo7wPHP2eYS3Vi7AXvlcHMq71BVJ15mOx596UdThoJ7zDkNH0ed-_B3YlK-7mpmFXqAUhbawkeW7Dtt0GBHqDUM3bnTOBYRYo3QJB4-QasNpYjFkfaGjuDno4UGvV3UX70iog8di_8jmbJ1ElnP2iEbxoEePB6fw949AUGPHtMmOYHuDdOMHc0Se4GPABBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91757" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوست دختر بعدی وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91756" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHwBi6EMfXdBQCjU7jVCWFyo5jk3GYxTEajq4c-utPWsyASJsy0cTZqPKBs3S0lyr7qXXhxpjWC0PjOp8G6iKrq4FfZPbfBp8d1AeYsuuIzUefOVBqtC15eVv-POcClWa-l2CCynyw983W3rPwmgmUehyJHv59XGmLBkVC59Ea33ClrDfWhnjvQ72xAt9wjI7c4AR5d5X47g7YUr-_ZNv3IJIiTkqKRZc4br77W3NVPty0flkmZqXBw6Lpxk5wZlyQRTtJGtgncxKZCy0FIguJvva_H9kRTodVhDYTNhKfhNYYmAbJm9p8ngzkbd9Drn8Kj4C2Ghn8XSd8uiEgWpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر بعدی وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91755" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07e18ed18.mp4?token=ksHTgrlKF_0hGZM3Arg7S8ssr1daHUnzFaoCgB2g-jzZAEqqFAsLrUVbweW0uzsHc7NZ-CTqMGaqu3decM4nKtdHxr0QiPZgWpqxLFvBdeWJSndNWs38OEcYk2kRQFbZTobb6PW1K6apU030FvUKLBrVb3cfZCZGutWXw_9BAKGnTCt1bpYLDdepF1i-SyUJgOlVDODEzOWZCwt7UfySjwdeOT5u4kw2nZEG43VNY8yUZyyne1P_DCLqdTLQjzpVhTvpaFaSwvE7K0FxzdmADA-7p0-1won4x4ls0n037_HikFDGRX6ngZjJDeRb6xHrp0jREuhlw0VxjWbrP1-l6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07e18ed18.mp4?token=ksHTgrlKF_0hGZM3Arg7S8ssr1daHUnzFaoCgB2g-jzZAEqqFAsLrUVbweW0uzsHc7NZ-CTqMGaqu3decM4nKtdHxr0QiPZgWpqxLFvBdeWJSndNWs38OEcYk2kRQFbZTobb6PW1K6apU030FvUKLBrVb3cfZCZGutWXw_9BAKGnTCt1bpYLDdepF1i-SyUJgOlVDODEzOWZCwt7UfySjwdeOT5u4kw2nZEG43VNY8yUZyyne1P_DCLqdTLQjzpVhTvpaFaSwvE7K0FxzdmADA-7p0-1won4x4ls0n037_HikFDGRX6ngZjJDeRb6xHrp0jREuhlw0VxjWbrP1-l6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جام جهانی ۲۰۲۶ هم رسیدیم ولی همچنان با اختلاف رو دست این مصاحبه نمیاد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91754" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e12c65af.mp4?token=j620HgrCMBeYc-5igaqk1CkJSFgK105R-axFL0mPadGEHJ6yVgaU2Nibpq_DgGwDj8_YRp7t6cwPovjuQqfJwyD9OG7NuFGbNwpt4L1_EWMMWSYKvThXRU6LMpF5RASFrY-UrxNwqaMD4BlzWln37L527y0kdTqEAGxZ7OjDzpDyh5_C_7tHs33qEIykHQOFWRNO1pBPONobpTKh9ogWTcbQRzqZ5U11HqMjn20cC9dJAr7rgV5ajLV0DUY7Fo3myGy2Bt7Rjxv0VOnYaAxL7587l2o5KOTv3mXja9v4w_PfqRku6cGjJxKbEuAM4gf6zgmcDsHD2JzAyKWS2E6D1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e12c65af.mp4?token=j620HgrCMBeYc-5igaqk1CkJSFgK105R-axFL0mPadGEHJ6yVgaU2Nibpq_DgGwDj8_YRp7t6cwPovjuQqfJwyD9OG7NuFGbNwpt4L1_EWMMWSYKvThXRU6LMpF5RASFrY-UrxNwqaMD4BlzWln37L527y0kdTqEAGxZ7OjDzpDyh5_C_7tHs33qEIykHQOFWRNO1pBPONobpTKh9ogWTcbQRzqZ5U11HqMjn20cC9dJAr7rgV5ajLV0DUY7Fo3myGy2Bt7Rjxv0VOnYaAxL7587l2o5KOTv3mXja9v4w_PfqRku6cGjJxKbEuAM4gf6zgmcDsHD2JzAyKWS2E6D1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کول پالمر و ژائو پدرو ستاره های چلسی تو موزیک ویدیو جدید و مستهجن مدونا حضور پیدا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91753" target="_blank">📅 00:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الان توییت میزنه و میگه: جنگنده‌های فوق العاده زیبای ما در راه ایران بودن که فیلد مارشال عاصم منیر بهم زنگ زد و به همراه چندین رهبر کشورهای عربی ازم تقاضا کردن که حمله به ایران رو متوقف کنم و اجازه بدم تا توافقی صورت بگیره. منم قبول کردم و همین الان به خلبانانمون…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91752" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=ACmMsJ5QnczMCWilKw6rDjqud500oer5aubSsxpKZUe5Cy-ZkrOyo-en-neloVx8E0wJapqO0yeIGw8VhgHxXSjR-AVuQ519pS2genIk9Co1LLy9gGKScCq7Niwgx2Cvf3XGsuIXYAwqpOw4gVKB5d5vSaSbA9hkqOJ2FPyDotKpx2-VzhHcuhhbFU31CWOcf5Ny7UZv0QQ0kHQ5Pfx9xAQMH2s9IQxcLhiIcU-QQga4eQDGLq4t3Y33lmtekM0YfhMgduNxeGaGziMiC2tWlu4YPI3N3wk19pDCRIiKsfFVzk09YHSvUzVBzmH997VjlVaWEesYMIsACURH03I4MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=ACmMsJ5QnczMCWilKw6rDjqud500oer5aubSsxpKZUe5Cy-ZkrOyo-en-neloVx8E0wJapqO0yeIGw8VhgHxXSjR-AVuQ519pS2genIk9Co1LLy9gGKScCq7Niwgx2Cvf3XGsuIXYAwqpOw4gVKB5d5vSaSbA9hkqOJ2FPyDotKpx2-VzhHcuhhbFU31CWOcf5Ny7UZv0QQ0kHQ5Pfx9xAQMH2s9IQxcLhiIcU-QQga4eQDGLq4t3Y33lmtekM0YfhMgduNxeGaGziMiC2tWlu4YPI3N3wk19pDCRIiKsfFVzk09YHSvUzVBzmH997VjlVaWEesYMIsACURH03I4MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91751" target="_blank">📅 23:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=BWYYdVi_r5QQmg9kIPONL2BsqWP9LmbRBoa9-Ue78YQLI3SnIIfi_3DdUmy8-fFihGlL4jTdhqEjYD2_gP7DwONmg-U9oV_Hr8KTDJvX4yAGQFHDPzDWJUo4ifrxxoU2VdoHC48a4qjpaTDH9JrcQ1Oi3Dxoc82nO3QnKEMv06v2nOdSKdV5eudmb3ky9U-VWYalxQ34GRZggwibUTKmQduXfTtBUr-uu1p0bLhQOBC-lD-y82j66H2ejULeQMCXYHTkgZrFq4SyasxBevUcrdGIstJPcWAA330AgSNpHPy9w21JOYgpzQ7ks_IdJiP9cR51p-K8CZW_ybfsH5rn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=BWYYdVi_r5QQmg9kIPONL2BsqWP9LmbRBoa9-Ue78YQLI3SnIIfi_3DdUmy8-fFihGlL4jTdhqEjYD2_gP7DwONmg-U9oV_Hr8KTDJvX4yAGQFHDPzDWJUo4ifrxxoU2VdoHC48a4qjpaTDH9JrcQ1Oi3Dxoc82nO3QnKEMv06v2nOdSKdV5eudmb3ky9U-VWYalxQ34GRZggwibUTKmQduXfTtBUr-uu1p0bLhQOBC-lD-y82j66H2ejULeQMCXYHTkgZrFq4SyasxBevUcrdGIstJPcWAA330AgSNpHPy9w21JOYgpzQ7ks_IdJiP9cR51p-K8CZW_ybfsH5rn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🚨
🙂
سوال روز از رئالیا؛ دامفریس رو پرز فرو کرده به رئال‌مادرید یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91750" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91749" target="_blank">📅 23:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cUM30ZKtVLdmiunf8Q-n3E2MXmMnFqzYVSOgwKqrAef-VTAtI7tvosnXr00vTJgXQ1U9g1VTuBuBKjaNx1p9lwzxVQJj9eAEFwo6946Xppnq3E0G6oiN8Foy4SfavCFXBiHYGDShZ_gTHLwdxhbxsNeaY4z9Z-52WmBXe9dYnTWdVPJfCXS5NgyYVswC9W5cBIK4YzHGUnwfIvl4Qy5a6RB4HxONB3YsXUJqjyAabA7utQLRkgvcBh6KUUmW1rLZKvjW8a4xUO418_yHXeu7rlvpA1JANQ19uC9k_imky-irR8xy-qvOUO0PD9Q2h-6e2eQGoCFZs8XFU4vwHT8zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
۵۰ بازیکن برتر جام جهانی ۲۰۲۶ از دید ESPN
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91748" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ2N6iu-szrKO12lSYjht1nMQabGsRFREvV0zNN077BCot5-WlTCkrA9z0L4EIRpxNDb66j-cn_i86YjezkZiPUSOi5iPfICPXM_jgaJLET-6kJIWbzip8DlsYDDEntXwJqqUimCOBADdUUke_UAV7sr7-oHTiPukgOsMXLqLyAErZGJHSY4Lt4CzQyfmGZxmZoN8Wwaqvh2urqyRIMgdl_w1W-_F2Djs12M7GPs_XSdASrcSWOrON1jfrbwpj9tB7vypfPJp2czjwQIJi-ZbbuOKVwq_KGQcy_WGQpB1unH_XQZBePkVSoYrKMB1cgh-JtlSAop83kyd-SE9eD0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💪
🇮🇷
🇺🇸
فضای پروازی ایران کلیر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91747" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
کیه‌لینی رسما رید به رئال :
⬅️
فکر میکنید اینکه رئال مادرید هر سال توی لیگ قهرمانان یا میرسه فینال یا جام رو میبره، فقط یه تصادفه؟ توی دنیای فوتبال همه میدونن قضیه چیه، ولی هیچکس نمیتونه درباره‌ش حرف بزنه.
⬅️
حتی اگه توی زمین همه کارها رو درست انجام بدی، وقتی طرف حسابت رئال مادریده، فقط با بازیکن‌هاش نمیجنگی؛ باید با یه قدرت نامرئی هم بجنگی. همه‌مون میدونیم وقتی داورها اون پیراهن سفید رو میبینن، دستشون چطور میلرزه و موقع سوت زدن چقدر تحت تأثیر قرار میگیرن.
⬅️
توی لیگ قهرمانان، بزرگ‌ترین رقیب شما یوونتوس، بایرن مونیخ یا بارسلونا نیست؛ بزرگ‌ترین رقیب‌تون نفوذ و لابی خیلی قدرتمند رئال مادریده که توی زمین روی داورها اثر میذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91746" target="_blank">📅 22:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
بیانیه باشگاه اتلتیکو مادرید:  - اون قسمت ویدئوی پاپ رو بریدین که می‌گفت طرفدار اتلتیکو هست!  - ادب و احترام رو با تشکر اشتباه گرفتین؛ برای اینکه سوءتفاهم نشه، هیچ تشکری هم ازتون نداریم.  - نه پیشنهادی برای خرید خولیان رو بررسی کردیم، نه اصلاً بهش فکر کردیم.…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91745" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rufb8kzGszNuKde2san_L5t1P_1NfLdifsh5Ah6cYg3v5UvoadPmPheumYQnK825-_hlD6rN_SX2lHVi01rmz01D4s2i68HLZZLH3pzwuzlwZEeMVPHOzCEXwbAGOBpTe_C9smY_vETvWMCrga0Liu5pe4-wMYKoeo7TMaqVUiyhxq4pAiCyq1HsNV2Yly4cgfZpXLCchukJHfgCoiH9loVJL-WMqQZKaNsebIq6caOVaDbXSMTBIwbPJ28csud2pZUD-hhDRX3eIw9P_ZSU-MiY6WinMvD1tnKC1lI5q0vl7NKWv4DZCzac1Enogf6swCA11gn9wddyny_sP337fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیانیه مجدد اتلتیکو مادرید:  «پی‌نوشت: با استفاده از رابطه خوب با رئیس جدیدتان، بیایید ببینیم که آیا از «دزدیدن» بازیکنان از آکادمی ما دست برمی‌دارید یا نه. خیلی ممنون، رئال مادرید!»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91744" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
#فوری توییت اتلتیکومادرید:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91743" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aqvO3dk3WBSAGNdW-1IPLy5-RAI4QL8fTrjouFJvGugZh7XxkE7Xa2qJa4ycKqcYFaLCY1vATSdzw1WRYbePDMOnJv17h3V9u9pMvd0M87VsE46zgWFVZfXCOo8OfwUpNxWFwt2Brm07qMNn-DXMVOImZFImbWPpKUStZ0SnHhrBVnHGHX9Q3q1MNgKEK2aMHLCIVsQ__Lo8-Z7mJ9KqsM9x2XywFt0oJegI0XIlqBnl8XMyNceKvThcUw5_L6ETDJolKvxaoLN054ts6RPJaygxgSQ-V7cH6wi0dGUu07gIRvs0HhU1it7cxeyBSInrH7seXJQjKESWESDrf2pWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91742" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2t1NmoWvjs-pbHxFGeVVX_ljoAsJPD0tpBqgiAzrmHKKOfsJSkaJWDqvTEIdTaPyDr2Y7uafZy5E60Gg6ZGzt5vxRVCYKYllGBVkdHeLZghxqUvoRAdEAn4xBHwKCLSUN82DRlboB8dZtrk6-YyD6ABIXzRTzuch-qTGTBsbX7G6Ay5G8_JC-jqXAr7adG6wN9EMmoC1NUF9nsKrXIbI2UuoqPJXfgSxVAWbMWWj5z_L74c6O1oateO9jXbFkrgfxNH7Ml9oRmEK_KZHypt5uo_HvDgtYpIcGTwdAwOCOsGUrJIjBijESEdNPYUax_Oeg-N0nF3ZTLTIvaabmeqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91741" target="_blank">📅 21:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OzLuG_bSPg2FIvfFuiX9jRwn1UrTrkTVe8gtpELUD658HQMRWstEFPoNijYsEDZQRZX5r9jyuerbEyr742CtFAueN8ir30zoHs2qSoATr1rJBUBmj_E_L3EcKVWwODhtoPb3H3KyNyGwjz1grVTNzk0IIHDxWKMe3aHvbFyuVRi-ZVVpfG8-ECnepCpWRmIUBXpinw2gqSh5JlB-DKqYqPNJ5HuCg3s-DkFgoMF_iJJS2qpixW6x0T7-PoHYI0R1TKGYAJdGiDD9xdPDWAT0iT_A4GbvZNnm4GZFCUYfJqbMk9oh4AD4YR82jKMLp2Qs2QLfp0kTbM8KQDRkP72RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
روزنامه Ser:
در بارسلونا تأیید می‌کنند که مدتی است می‌دانستند رئال مادرید این اقدام را در مورد جولیان آلوارز انجام خواهد داد و این پیشنهاد رد خواهد شد.
و معتقدند که این موضوع تأیید می‌کند فلورنتینو پرز بیشتر مشغول آن چیزی است که بارسلونا ممکن است در بازار نقل و انتقالات انجام دهد تا تمرکز بر تقویت تیم خود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91740" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91739" target="_blank">📅 21:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91738" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
بیانیه جدید رئال‌مادرید بعد سه هفته: با نهایت احترام اعلام می‌کنیم که قرارداد آربلوآ به عنوان سرمربی به پایان رسیده و‌ از تیم جدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91737" target="_blank">📅 21:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تو تاریخ‌فوتبال بین باشگاه‌های بزرگ هیچ تیمی روز اول ارائه پیشنهاد بیانیه نداده که پیشنهادم رد شد و تمام. پرز با این حرکتش هم یه ذره میخواست رئالیا رو آروم کنه هم کیر سفتی حواله بارسا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91736" target="_blank">📅 21:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6EwxE2Y_CCoh39-IJOiMR6tmOeTtFlXCJVqC9IcXfW5DvVMlDj_A2CZEq6DcArHUE9CgUDP45nbXEGwB1ELjIdq0Reb_BgeFnKFtcygAlZ3PM9EMlF4AAXteP8U2ia6AHkyV-eLW0wuEqZrcgIRRBIQ2j1O1NT48sdDnBtjOaIHnK3IG3TVnd4e8SEgOTIxB55sDL9fOa5Oy2ezkhls2MSyp5UJ3pVeTdWZx6YIQIpAJkffLSASaWSQAEJkbariVlW18lps05fIvi7OkdxJGxhpL5Nz21o2RpBzYhAf0Om9rWG-uNbKnKDZmYKUUEbWKEmQMzJk7nAufYfUTlgy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: نظرت راجب مسی؟ امیدوارم اونقدری بازی کنه که نخوایم به بازنشسته شدنش فکر کنیم و‌ بابتش اشک بریزیم
وقتی به کمپ نو می‌رفتم تا مسی را بازی کند ببینم، چیزی بود که شاید مردم به درستی قدرش را نمی‌دانستند، و آن این بود که در هر بازی که می‌رفتی تا او را تماشا کنی، بازیکنی بود که باعث می‌شد از جای خود بلند شوی.
همیشه عالی است که هر بازیکنی گل‌های زیادی بزند و پاس گل‌های فراوانی بدهد، اما کاری که لئو انجام می‌داد بسیار دشوار بود، و آن این بود که در هر بازی چیزهایی به عنوان یک بازیکن منحصر به فرد ارائه می‌داد.
فکر می‌کنم مردم وقتی او بازنشسته شود این را درک خواهند کرد، و این چیزی است که آرزو دارم هرگز اتفاق نیفتد، این چیز باور نکردنی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91735" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ولی عجب کی,ری زد پرز به رئالی های که بهش رأی دادن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91734" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91733" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییییی :   اولیسه ، وتینیا ، نوس ، پدری هر کدوم با ۱۵۰میلیون یورو به رئال مادرید پیوستند
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91732" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇪🇸
#فووووری؛ اتلتیکومادرید اعلام کرد که فروش آلوارز در گرو پرداخت ۵۰۰ میلیون یورو از سوی باشگاه خریدار هست. در غیر اینصورت زنگ نزنید مزاحم نشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91731" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91730" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇿
#فوووووری
؛ ماشاریپوف بازیکن استقلال بدلیل مصدومیت جام‌جهانی رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91729" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91728" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOFAAVErNWHqnmOUjFJ7pW01FaY-OYWbKQWXT7cHtcx3tsLqqXYYOkFZVPdP-rnpXRG3uuaQ9Re8Kypt16OnfMj_ns9Tl59YXXNOEfJi_84MQF1ZO25oK4ingALsIzeZNbSpmNde-98U6ZrlOpXSxzYLWvFg0WQ8X7ZXltxS3pbjxvC1KgbRd7dAXRoAIDLrOfsHd396TVFuZKC2RnKv_v2WpxSR8XixtakyF75LM0JHQvch-eif4zgh67i2VsOReeNWvWvrjNSRllVJ4U1au6l7o7RS7hMNV0jsYpC5g7cVPu5hglJO9h27eR_7o3tDgWQCuQ8bT5Ui3_lZfLbiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91727" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHLIAfgNQ6r9V9yt9PChpihSMuXUJlUVMMK9WxQ28l9dNcK_n2f8WtZeL-pSWHuycoZz7PvgUC-NMRrKROWrMlyzTkfkVv9IC060pusN0f2TMmmFr6taUlloOscU8ylvAES2lFe6XQ2j5m8tnpR9ziBtQW9wo5TPVl6oC0J5QygxB5aWwfy0mrAZtPYkAXKBVP_rLOoJpti9zmn6RBldYU1CyT5IJQwADSlivzRnXa68a6-Z5rhKmujCg9yzfULftfj9cIuYn8zIBMOnnu0XWWybipZhcr3OR13UUy5MpgSNRDhMxEQEDiV2QjSTzMXSzdWl0y32Pm_wvz404sxEHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری
؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91726" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZmEDiKKPN9pB6SuKbt2V7HUKibBVHkg5uwhJ_5Nk1FwxRw0htFtulH2zp0KUwOL8b1Ug5oU7TlHBOT3LGDWBZaeD2j9z-w4aoxlnsubINMN35UaNxr8YBhsZSBib1yQBucxefBdnwu9UiSebrwzBPHZlWI2JQj0tK5Fq9X1nZ5Jo2jiEvp8TmR0zqp3BX-_pCqpwLKc80UKlkhW2jjAETsiKotwuwLPwrISaaOgo8BJQqwlJTh4f1HfB1RuzyBA8KnumMGKOURQmgqZ811s5SaPDk8JtucW1vHM5y-I0O0OHFzHCwU3GEcOMGil0RurJC3deS0igipwgnY67-4Ftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو ناتالیا اکس نیمار
چه جواهریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91725" target="_blank">📅 20:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91724" target="_blank">📅 20:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo7dxcBz0onFTgYbCZzo5Gx3_jrhbAoZxR3Jn4cHCX7GgCjOOSuVGFYCX9ErNRjDERHf9LtKKThZDRnfqJQkThWlrFyPxJT9bYgoyT9Kk9h9zWpUrGX-YefHWjibjg3G7tX_GGWUJWlAbv7RR0OhzlLYqyqFHv8mEzUW5Zgi0NWHrhdhVeBdpuc4ixQZXcLo_XscYj4N8t4xedAPfKlSL_Jivh-W1itJMRmCnJz37GYl05eLjUPM1F6f0GSOnO1DJBV0gKD6TawsueA539RROUOfji54evflbrNOoUBPKG6OF04DP4XohfbDsIMgYMnanQ0ut_SG9O2kFQP9QfALmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:
«همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن.
دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91723" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm20JFrYJWNAOBOZjTH8_9ymGuEj9Po_s0j64GCYFIt-3V0He7EJmMuuwvQsUxT4lIg7e-eMERwxcG7ATH7u_YBpU5VKD97d4bYQjIcukEz_dKzTP5JHKTeNtD9v5XAe78YkRCwJmsQwKRwid_b9RQx64aZSQmg6v90ClpjUZJm8-GLe6dl8TLHViY4NvVkCzMasyWcZOh_595UMksCHAAEkZ7C0aKSjP_6H1GLJOSjaGUeC7Yy-pxjHrXJiUgjOAUAgcvr-rqVFCDwIS81Qvu0wVCzNfOZX0BNSqo_XZFZ0eMkEHVxsA3L0lwx8EHt6lAU8bwZvwXuSJdhOZaYUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندها با بیشترین تیم در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91722" target="_blank">📅 20:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fqQYiGG7ddKsDct968I9YuvBN0cCRX3BuhRwZs7bYv3sfI5HQBmmdBp-8ZXFWfJ4EAQA_K5oTGglgTNQNDSFtdLkPUBDgVeKaor_SMlNdN0CCnDDoMcu7CKXScAApVqoNWLt5lNOq_OI0iCw_oRxA5jEb9XF3QZ_BDx28x9TvmeCpf-Yt0bEDMNjsxK3RhxD9xK8tEMwdg6Gz81Jk_NPvP7La1DyMInG8vJoCOxhl2tjISyXhkp4Zm17U3Dj7MqIUlDTTvOfrEpYJzWw25nG1SJPKbCw1RkcuO1ebcUl1u_qdYm2LY_0cEvwRTYTsHva74RiXbUmfKD6zT2FH3AQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
فرناندو پولو خبرنگار موندو:
⭐
-
برناردو سیلوا هرگز اولویت بارسلونا نبوده. برناردو خودش رو به بارسلونا لینک کرد و گفته که رویای بازی در بارسلونا را دارد.
بارسلونا سیلوا را فرصتی در بازار می‌بیند اما بدون فشار یا عجله! مدیریت دوست ندارد بازیکن از نام بارسلونا برای بهبود سایر پیشنهادها استفاده کند، اما این به آن معنا نیست که او به بارسلونا نخواهد پیوست
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91721" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
