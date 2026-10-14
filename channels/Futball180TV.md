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
<img src="https://cdn5.telesco.pe/file/NPgNU6Upn7n_QkiwczOxy6nsArHPrZjdfeAj97nBBnnxr1yw0fEZ6LDS2Ah_NaP-gWEFHYNpvTi-497vBifLfy_CyjZTXEfNobQ-tIgZjONrcGCba0g-1sDUc9YmsarFiGHM9-6S656QuvGc_G1stUEGZ4VLL9K--4wFBELcGmbliQorYTsYH7i1u-o5L3KWZmHl5pEAseUphXqCqqYTz8iiZgY-rkILNk9UU0-bb8dosRB5qKBf0dThdJfegHluIZ6-TwtoaBjiErPpd498FuiSUFkAYbBlLMfet1MZIzoeQcLjEfqSVwtPXXSqfqVBq4qHKP-MzqWup6BtWkm23Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 382K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-108782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvGD1JbM_qwbYxDHzkK_roaFFDFbGlsYmOEml91s9_RPGH7Y1hr0gv9NRg54yq3VDf87DGv9TMaQn5q7vq8whqg4vWCejP2IBFCnm7zUOLDBJLgMfMoT5RSEPhkid5izNtAyp61PWss-6-7hpdhE_btAiuCrJyRsx1SLZv8ovex1XBDA_jzib0LZjnHbRj5i55hbP8lzQHkpz5fLPFPRg3aaaKP2bUNWtkEMYNjR1BK0ljdXBvqsPVufvwSVn8jLx4-8f-EKMrz6o_lR-C0-4KwSV6X3u7fV1xDtKcTCkom6o6JxJo4bNfahGv9_dOYISmNLjEOGiPx4aasC8kOK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
📊
ارلینگ هالند با ثبت یک رکورد، عنوان بازیکن با بیشترین گل زده در 60 بازی اول خود در لیگ قهرمانان اروپا را به خود اختصاص داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/108782" target="_blank">📅 01:13 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b162b7fb.mp4?token=nZHjPAo4htMSNR8neRbOIb4tPnHSedCyJAZqLGDlMzcpZUKI9leh94O5uMk9mKt7Naf2qT0XDVQ9Sp6dCSTWNKpfg1Agv2Br7qGDqLPuOqdtq-DrJFKO6NDmol3u_EAX5QXAHzPo-JdT6MTxAkb_7hQ_Etc83OYC6t8NbHImTUemuYl0HPoMbAQVabAcC0ANv85nUqh6nl_0ibWdoLngkCx69Qt3Fnh_oplpRoUn1THjApl88T3-VRbmu_2TVELYiN8jxJtWqR6MQONX5eJ2I8lZYo8Djs8KY9IRIaJpKmHypNCVBx6WZgf-pdBybYs3guY-QB-w5A9u9MAF8II6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b162b7fb.mp4?token=nZHjPAo4htMSNR8neRbOIb4tPnHSedCyJAZqLGDlMzcpZUKI9leh94O5uMk9mKt7Naf2qT0XDVQ9Sp6dCSTWNKpfg1Agv2Br7qGDqLPuOqdtq-DrJFKO6NDmol3u_EAX5QXAHzPo-JdT6MTxAkb_7hQ_Etc83OYC6t8NbHImTUemuYl0HPoMbAQVabAcC0ANv85nUqh6nl_0ibWdoLngkCx69Qt3Fnh_oplpRoUn1THjApl88T3-VRbmu_2TVELYiN8jxJtWqR6MQONX5eJ2I8lZYo8Djs8KY9IRIaJpKmHypNCVBx6WZgf-pdBybYs3guY-QB-w5A9u9MAF8II6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو اعتراض وینیسیوس به نیمکت رئال پس از تعویض شدنش جلو رم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/108781" target="_blank">📅 01:00 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZE7AVbyLDRRmdqA3yeIBAo97-RWedM3ziWJ4SqvPPKH5m0OrolfJw0aqvt5v3bbUb-cf-RmY4yc5MDusV32B0aJYJ6k0ojkOJ4uPr7wnZcMKwgZRkZfTohKmVM8qhkPqG18qYruM-VKgdD5awc4xQyqcrgTfM8anXZC2CkQ56xtTq6wAXnuUibNKNX6aAtB_Uzl11kgBmqYNbgrC25sRdqTig0VN2lS8vntQ_Aa1FJ1481LvjDss2TiyP20jRKavVgYIt9obiv7tIp1ENUPj-3StNEIXoMb1GbS81hInHq9wQL9aZKG7jAyrmaAkKz9agocOASapNHKJiZ2wYTvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🔥
🇪🇸
ژوزه‌مورینیو: بازیکنان رم بعد گل سوم جوری شادی کردند که انگار بازی تمام شده اما واقعیت پس از پایان سوت‌بازی مشخص شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/108780" target="_blank">📅 00:58 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzBBQPgNgyFLTM2rpHy_WJdzmUhUNmXXYLr2JdOE3UUoeYyqPeRBfHA__aaGQ15khKhFngN7eXyGZ8xSAMq7ZsbuSYt_BBqO_zqsrQjD4_JpeLp2c7zq0rhEtqmvP3BhSmN1ZUuM3KqP8TZoR539P5DK8bU-Kt7VBa0vSnSu4RG3QTTJfiBFhmNqnE4NCMeQxzzzmSjodZAXp2ssgzB7QhjiL6nxNNg5-JxWDl1WAJqkMqpn-_-KnZl_9NKm4WJ5rviqQ32mi1WHSlWWRo7zgnrjS-mt5QeljQ7gWGUPOf8PX3sUsSXVxvB0OHADbdMSCaeGqKZoCeqB_c8-Y0SUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇪🇸
استوری صالح حردانی مدافع استقلال بعد از کامبک رئال مادرید به رم: The Next team
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/108779" target="_blank">📅 00:44 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsTX38FodDL_7tGdLyZem7FWIQOPU6MTBVJ0e_DFS0qMJo3YDB8LZM8CTe_2UIZcS3PgZPRC2-i4SFmzkOMv0pOXSX-UtV56qqATDDkGKuU-_iGMvkI_eyGcqpTib6L_OYWjOUyULwS5Z7XRFUUsLESjq1IOG88b1fsUywPJqIC8DZcQ1Hw9RTDccni6pF7E3dFhDyoPa8G4637e2Q15DpFvTRUb5S-BxO8TgZYrpjnJF2ayZ-pNil8SOlyTzxQVs7mu1lNhNBJ0TWF8VfOvLwGpLZmPPkPL4hpzYYpsF2RMO-RJMO2N2PxYWTuhYlC8RzNGvA7Lz1mD4DorTQoAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇺
جدول لیگ‌قهرمانان اروپا پس از پایان هفته؛ مهمترین بازی‌های هفته‌سوم تقابل بارسا و پاریس در فرانسه خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/108778" target="_blank">📅 00:38 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1yByw3laPC2vq6BgaExfyNobyCw1J-svTAqTWVylPQodtP77RWO5wBpBPq8m1diAE965nNnX2UMXdzrHn21HB2Q97znWIGyHaoWQqirbrHtYSNnCOb9QQCNp98fzOTBPFrlCEMnx2niCyxCjZaOCpe5zASheJuSr35XkTqpDPitmP-68MjtUBJA5ZITOYCpkPmXS_fAKyp101XFFxF8uVYBSSWZ7C_X7MVC-9FFdeSxIxDW2XMr3SWNWjlKK_8VuhHdfdg5502mjUHDUo3GRWUzuT4vmnskIjRidtkT4_fPdDrd9CAXGJe3h4COqszNDMDNLZt9vnNOATifciz87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
😳
🇪🇸
تعویض های امشب مورینیو:
اندریک: 1 گل
اسپی: 1 گل
گولر: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/108777" target="_blank">📅 00:33 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AywV5GZxooaHMxzRWc-6zB1n_d5jFy5ZjR2iG0STGRYe_nXewhhWhKFTVXqtdfC3cUUJzRcZ7dAIuRG95Wedc0fHQ5gnermj46ti7mO8Otauw4XhE-tfIfjKHf95QdgzLoX6ReZ2gV2e2bs9l2VZ7ub6MfJ9Tf171vjTGrW4Zbgl09CEpE3tw3Zkbn9YWg3FRraOV6GiZVNHWCtXKSi6q3kOQ3PPjh-mOndJYtV3Fe9GmMKHy2azbolfFQkPFTbsqAGbJmOBzGg3RMBeoahfpZegupn-NdZnZOWt8a_OnK8bhPtyH8gzDYGKmhxZAOV_EgC8Efic9_MLnFkKIXp6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه بارسا نباید برا رئال با رم کری بخونه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/108776" target="_blank">📅 00:30 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G73-sFdGcbq2QQB6I-zDkcEo019aputaTCgm9lcWO3F_0-Ujzg88lHDceR1DulfsaHxm1-dQurMzlaQ-Uu4QgFIlnHVMk_dKqPUW5P-R1Pntz6xVLuAKbit6KFVJVjotn4XfYLe1wik1NGulZLRWFkd9Bcg_K4E03jo0wH_Ow7H0iq3iBb-zg6KmEn2EyvkXZ8Kg2k3GU3ycUiWs6ynEc6p_oryG6G8UPstqs--6zxkCldss_8pgEHTLV0SViVWUFIM9bCw3ct_Llot2OskBuOKkB_4M2TsNR5letKjtF6oj7JNpijxErQlSBP4H-o_2KHrL9kPUYLS-lZHt-obVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ جنون محض در ایتالیا؛ مورینیو نشان داد چرا خاص است؛ کامبک تماشایی و باورنکردنی مقابل تیم چغر گاسپرینی؛ وینیسیوس طبق معمول پاشنه‌آشیل تیمش شد
🇪🇸
رئال‌مادرید
😀
-
😆
آاس‌رم
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/108775" target="_blank">📅 00:29 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBtm8yuhkMlmrc6M1lJ4wvmDnhcPF3p38Gin_Ks-XWhshRuiVSFlNekja1u1GUD2th6vc_TzQuXLa2AYQevenFyzpiDrrv8zeyp9RFlXFXSZaQ417XUf1isOwkgHVFbaqf4RYxz1hdLexcLWNIybojGvpRaGtFmH2Ok-GVpjQgaW1mwepTpFDBmtNSQNot8QGNCJzrq-CxY0B4fJUDclfb7uROEw1TFd0UBbBLyQgRrV-ltIEhPKa1eQSNAWfGooi3unZIPrsLG5iyj5VvdF7vOYG-PHFkwKRBgmVdBWVxGKJc1XJgVPlJrKZ8Q3jfkcbebtUQ03etD5LOQjiNL2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/108774" target="_blank">📅 00:28 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLAP8BWZXeG4PmrIS1bbw41qtffjW1UBgQmuZY_FrcsZkWfV5m3C_9z7Pp_dBTBjvlHF6AtYYSU63PdX2Ai67dovwZPKUliHwFc_roAofziN6sP77X2JwVlAbU5JJ6A7KbZcTFLAHuE4nt26nbCJyx8DbqULG0sQeeZp8j9HMU2UES88HMCsNMwpJfvbKT3SgD9GCm9yuAu0RPTpQnrVSMQESmedPzSMw4iLmu-fd2rmq25R0HUvHGpp3iIw6EhnfOdKLDBNqAkZkgsQwForIYSpIELGSY0i8lmvsVFxb6KEPjMqbFp2qM0mLJO9AlxiHrHNpWGwFDE4XxluGz7pDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ قهرمانان اروپا | گواردیولا از نزدیک افتضاح سیتی و مارسکا را تماشا کرد؛ برد شیرین
شاگردان انریکه در اتحاد
🔸
منچسترسیتی دو - پاری‌سن‌ژرمن چهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/108773" target="_blank">📅 00:27 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5cyyUkdjRn20Co5SoRJrhg02zvZ1E-F5lWfa4hA3ZjXPhtdgwR--tg8YMqeM6vRV6fz2WNJhMMKgtFQzZ4GSJW7BKqY0JIf0_n55pYAYwanMW-wJmqd40A-8zV5ulC5mW4NH19uejF-QCExDbyaccZFCSuqp1uHZ2AKkA7xHB65x1RxAHCzbegRjQ9mrBQnWbNVMO2E_PMyjmdrBR1psobfzJ6UhmqDTb-K5DL0IXLKE6wEbM0Gq6wawN1Mu-YdMMvEWnmb02so2Y1xALsvvyhZuXC5GLRvAvMTvA49xb7uv9oCMR0BRqngilqm8X7fRAZvVnR8fCwgasqS0nVPyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ جنون محض در ایتالیا؛ مورینیو نشان داد چرا خاص است؛ کامبک تماشایی و باورنکردنی مقابل تیم چغر گاسپرینی؛ وینیسیوس طبق معمول پاشنه‌آشیل تیمش شد
🇪🇸
رئال‌مادرید
😀
-
😆
آاس‌رم
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/108772" target="_blank">📅 00:25 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108771">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720a7bcd15.mp4?token=tT4iOBW7LwRBcoghocW-WhPXEL2hOTxNwzWkcy34IO5jlkkraFdHHJQVIbjoQrJ4P60iWbB2xE7sch0bnzhZUmokNkIN3OKBJlsupcOmJEyMAZQVQ85rf18NrWOkjvXXgnHcB6PQcAKvVM32a8G-SDozFBFo5GcZpZela1MVY4IPmoOEGJGkOpfYkpwzVjWihCbxApAFewCUZ8-5ju6X5KLFuPtBXl4Wj5JO3oKIsWq8j89b_0R69j1uuNYm9Fvu976u_CxJJUlPYulecLvNqvUtfPs1YHAhxhK9mPNYxhDyEnB5ZJ5d_VEIokoGKtfR3Gz8MRN-hMvmVdIr4DZibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720a7bcd15.mp4?token=tT4iOBW7LwRBcoghocW-WhPXEL2hOTxNwzWkcy34IO5jlkkraFdHHJQVIbjoQrJ4P60iWbB2xE7sch0bnzhZUmokNkIN3OKBJlsupcOmJEyMAZQVQ85rf18NrWOkjvXXgnHcB6PQcAKvVM32a8G-SDozFBFo5GcZpZela1MVY4IPmoOEGJGkOpfYkpwzVjWihCbxApAFewCUZ8-5ju6X5KLFuPtBXl4Wj5JO3oKIsWq8j89b_0R69j1uuNYm9Fvu976u_CxJJUlPYulecLvNqvUtfPs1YHAhxhK9mPNYxhDyEnB5ZJ5d_VEIokoGKtfR3Gz8MRN-hMvmVdIr4DZibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
🇪🇸
کامبک تکمیل شد؛
گل چهارم رئال مادرید به رم توسط رودیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/108771" target="_blank">📅 00:22 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108770">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مورینیو چیکار کرررررردی با تعویضات
😐
😐
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/108770" target="_blank">📅 00:20 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پوزیشن سکس رم و رئال عوض شدددددددد</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/108769" target="_blank">📅 00:20 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بزرگترین کامبک سال ۲۰۲۶
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/108768" target="_blank">📅 00:20 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رودیگررررررررررر زدددددددد
😐
😐
😐
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/108767" target="_blank">📅 00:19 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یا پیغمبرررررررررررر
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/108766" target="_blank">📅 00:19 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئال‌مادرید چهارمیییییییییی</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/108765" target="_blank">📅 00:19 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگلگلگلگگلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/108764" target="_blank">📅 00:19 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پنالتی برای پاری‌سن‌ژرمن</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/108763" target="_blank">📅 00:18 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe2687886.mp4?token=Ko1xxgeXgml2zgqxQv6oE1WrG12U0rP9ATEPLvSv0yrwd6Nde-a5hUIFDyJzjuR_erRLsSGLQLs9-eOR1f21TCkmF0doqMlJ0krbA9LM_-O3OAAbD1YOZrRbtuEd7qrr0NTgAyYqKa6bEVp00cji1lfm6PnhwskFpzMbht4AAWJWid_wpyfo94I2ULRR3DLT0qzSUDhN6ZvBe8epWxA5YtRd1QRCEiCVlKMPSQLlCDU9UIklx_qjNGvvNjd5jMAk3GHW8HsNggsH4rMK2jYb0QA3TcaU_5mWW8g71phbSySSwgLC0zW2MnA2FQ-teM-FOWfKZG8Z_WQEbOehxovv9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe2687886.mp4?token=Ko1xxgeXgml2zgqxQv6oE1WrG12U0rP9ATEPLvSv0yrwd6Nde-a5hUIFDyJzjuR_erRLsSGLQLs9-eOR1f21TCkmF0doqMlJ0krbA9LM_-O3OAAbD1YOZrRbtuEd7qrr0NTgAyYqKa6bEVp00cji1lfm6PnhwskFpzMbht4AAWJWid_wpyfo94I2ULRR3DLT0qzSUDhN6ZvBe8epWxA5YtRd1QRCEiCVlKMPSQLlCDU9UIklx_qjNGvvNjd5jMAk3GHW8HsNggsH4rMK2jYb0QA3TcaU_5mWW8g71phbSySSwgLC0zW2MnA2FQ-teM-FOWfKZG8Z_WQEbOehxovv9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🇪🇸
کامبک جنون آمیز مادریدی ها؛
گل سوم رئال مادرید به رم توسط اندریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/108762" target="_blank">📅 00:17 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ffe045bc0.mp4?token=GryJ6zcbN5yEgiHgOyNUqlz4cjflU_oGezTPch2I3wwdyVYwtKnmfcaFZc-MmwGPpRwz1tPL7kfMMSVZALhKdup21iZsquHEBUs1W8SC1-Q4-BBTZxpTfZg12SqQLH8nkl6nW9x_1aIfaH_TfeHpy3tyxL3oWQUdPRHqnCBgK2mpSxbVz0L-mv_zw0zHxKdAoyEOZVg5WuiRHOaMG1oppauy345sOg5sKSqj2x63dqmhQ3VUCZ77IuRavSvJc_cc8PWvW8lD7cJ34Yzq6FwD062IqTQDWJwz0YbjhQnxl6DY5fsfmx9NV2wTdfbBi-ZslSe0Atm2KzoODSCd0A-Ozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ffe045bc0.mp4?token=GryJ6zcbN5yEgiHgOyNUqlz4cjflU_oGezTPch2I3wwdyVYwtKnmfcaFZc-MmwGPpRwz1tPL7kfMMSVZALhKdup21iZsquHEBUs1W8SC1-Q4-BBTZxpTfZg12SqQLH8nkl6nW9x_1aIfaH_TfeHpy3tyxL3oWQUdPRHqnCBgK2mpSxbVz0L-mv_zw0zHxKdAoyEOZVg5WuiRHOaMG1oppauy345sOg5sKSqj2x63dqmhQ3VUCZ77IuRavSvJc_cc8PWvW8lD7cJ34Yzq6FwD062IqTQDWJwz0YbjhQnxl6DY5fsfmx9NV2wTdfbBi-ZslSe0Atm2KzoODSCd0A-Ozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم رئال مادرید به رم توسط اسپی
پ.ن: این گل در ابتدا آفساید اعلام شد اما پس از بررسی وار تایید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/108761" target="_blank">📅 00:16 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108760">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پشمامممممممممممم رئال چیکار داره میکنه</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/108760" target="_blank">📅 00:15 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اندریکککککککککک</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/108759" target="_blank">📅 00:14 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/108758" target="_blank">📅 00:14 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عملکرد اندریک از وینیسیوس ده برابر بهتر بوده</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/108757" target="_blank">📅 00:13 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کارلوووووووس اسپیییییییییییی</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/108756" target="_blank">📅 00:12 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کارلوووووووس اسپیییییییییییی</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/108755" target="_blank">📅 00:12 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
گل تاییدددددددد شددددددد</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/108754" target="_blank">📅 00:12 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اصلا نبود آفسایددددددد
😐
😳</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/Futball180TV/108753" target="_blank">📅 00:12 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108752">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رئال بازم زدددددد ولی آفساید شدددددددد</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108752" target="_blank">📅 00:11 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108751">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگلل</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/108751" target="_blank">📅 00:11 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108750">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0856dc827e.mp4?token=HGgWqaOIels2gBmES8ki4i7jQUqqxCPzweApyGLqNcj7bR2vD0fJDg8OJWpp4N5ghPM2TQ_9Psblpo3-bj0vrqLXITZh8eLsWlUSO9I7Yow8cNfekjzHHvje5AGVkRzLe-2AbiFvn_96jGz4f2LEuWrt48XpzG_4f7Qk57052ChNDeXo5YHOa-YI79BqUhnbBdfwgtDWaCsep1bx9FWxdJPqClCG094POabJ8k4IdYfsa7jo6_Uhl5ee1RYVQl7bZufVBggev6ukbMGKcXeiPfn3Loo2PpaN6xRqBSAFbuYgksLVUs07Ixp2MTAu9ISPHA6tMFAT9covxjEGE9w8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0856dc827e.mp4?token=HGgWqaOIels2gBmES8ki4i7jQUqqxCPzweApyGLqNcj7bR2vD0fJDg8OJWpp4N5ghPM2TQ_9Psblpo3-bj0vrqLXITZh8eLsWlUSO9I7Yow8cNfekjzHHvje5AGVkRzLe-2AbiFvn_96jGz4f2LEuWrt48XpzG_4f7Qk57052ChNDeXo5YHOa-YI79BqUhnbBdfwgtDWaCsep1bx9FWxdJPqClCG094POabJ8k4IdYfsa7jo6_Uhl5ee1RYVQl7bZufVBggev6ukbMGKcXeiPfn3Loo2PpaN6xRqBSAFbuYgksLVUs07Ixp2MTAu9ISPHA6tMFAT9covxjEGE9w8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم منچسترسیتی به پاری‌سن‌ژرمن توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/108750" target="_blank">📅 00:10 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108749">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هالند دبل کردددد</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/108749" target="_blank">📅 00:05 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108748">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگلگ دوم سیتی به پاریس</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/108748" target="_blank">📅 00:05 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108747">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2ihEuRSTyr2Rc1PWV13I327S7J-i5wo23aXh_U29fgas_YSPpW9ycTpINe8ovKNWe5At5W9DlY1syrMWNKH6oqHVCc17AkTFCxJn_g1qtpG2tYvCZR7ZtBiqkwBz93JWczWcY5DtySKqMBOFgPMbD44ry2HLEsSsiUZToLOKCNd4gLxXWCst7RzsbeFGasM8sXE4yau18fdc-UDcXfkHgJ7KhddiqQQ1exnZjLn7eDhBdlHT8s0UBxR1KNISf3hWnSy0O7D5PBX1KO1ob8go0_sq23phwAKU6MuyNLNW1ISdzM8kv5cFxPTHCgKDmrfuULBweLpLcXaPMKtReQuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرفدارای رئالی که سال 2024 فوت شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/Futball180TV/108747" target="_blank">📅 00:02 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108746">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آفساید امباپه شدددد</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/108746" target="_blank">📅 23:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108745">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئال‌مادرید دومیوووو‌ زد ولی رد شد
😐</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/108745" target="_blank">📅 23:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108744">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/108744" target="_blank">📅 23:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108743">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873d979dca.mp4?token=Lz71XYhgPEbMLY5elPyxwocPI04YVkZMYd2UGUU3d9ULVre1XCzXh9bDx19S7dvcahDlEYS73y9N68Ml2FYT8s_EutfurEQjUbbGZ3D6JqbGcAHz_G3hygdC-m7u2KJ65cSurJBd_Xd4PleWuFFmSE-OFb0cBIbLSHuerJPl2Z72zxmUxMI36TTrFfoJfqKqhKYCL6J1SGn9S-P-2dZJh6VqdI86yDSXT0ULoHgAuH1iZCvC84v7w0pnJtCrqP12YKR5B3xNW0R35XBpUPvCeQp3K9s0ukQVl9Pm-J7cOsSWGf6vp_EWVyljhTT-KeEEeecmGapLQKbQDdEA2KkBzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873d979dca.mp4?token=Lz71XYhgPEbMLY5elPyxwocPI04YVkZMYd2UGUU3d9ULVre1XCzXh9bDx19S7dvcahDlEYS73y9N68Ml2FYT8s_EutfurEQjUbbGZ3D6JqbGcAHz_G3hygdC-m7u2KJ65cSurJBd_Xd4PleWuFFmSE-OFb0cBIbLSHuerJPl2Z72zxmUxMI36TTrFfoJfqKqhKYCL6J1SGn9S-P-2dZJh6VqdI86yDSXT0ULoHgAuH1iZCvC84v7w0pnJtCrqP12YKR5B3xNW0R35XBpUPvCeQp3K9s0ukQVl9Pm-J7cOsSWGf6vp_EWVyljhTT-KeEEeecmGapLQKbQDdEA2KkBzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل چهارم پاری‌سن‌ژرمن به سیتی توسط آکلیوش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/Futball180TV/108743" target="_blank">📅 23:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇫🇷
گلگلگلگگلگلگلگلگل چهارم پاری‌سن‌ژرمن به سیتی</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/108742" target="_blank">📅 23:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/966aa9f0df.mp4?token=HZbH-kYFvqTtSrnUJ5vfNK2AeWVBq9IRTlQcHWn6tM3R6WNuKEO-Tq5wAqZNk3FlVZAL19uo9GvDnfvP24CtM7ocvbCVQHirjcwk6IIgc8bD56UaLOfhl5-JTmqvFP9WspYKLH_i6VWmioISBnnHYbeAwb0dFOMK54OEJXa_7jfecI-1sZZdWrz1yl-KKJUpOJkAIfUjlAMZ2GSdwKLYp9O-mB2K2g85i5h9rR923IdnPt5-zFWsaA7l4gi0BIMhuitOZ5ZXDq5_Gn51Bdtb-Lt71mo7555YsWryp5W2eMVoWjIA6AzMTTxNFcnVFCdqNJRVb5xrwOc7Oj6izmzlXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/966aa9f0df.mp4?token=HZbH-kYFvqTtSrnUJ5vfNK2AeWVBq9IRTlQcHWn6tM3R6WNuKEO-Tq5wAqZNk3FlVZAL19uo9GvDnfvP24CtM7ocvbCVQHirjcwk6IIgc8bD56UaLOfhl5-JTmqvFP9WspYKLH_i6VWmioISBnnHYbeAwb0dFOMK54OEJXa_7jfecI-1sZZdWrz1yl-KKJUpOJkAIfUjlAMZ2GSdwKLYp9O-mB2K2g85i5h9rR923IdnPt5-zFWsaA7l4gi0BIMhuitOZ5ZXDq5_Gn51Bdtb-Lt71mo7555YsWryp5W2eMVoWjIA6AzMTTxNFcnVFCdqNJRVb5xrwOc7Oj6izmzlXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇺
🇵🇹
سوپرکاشته استثنایی پورتو به رئال بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/108741" target="_blank">📅 23:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108740">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0b13070c.mp4?token=F4Z5LsoPeFgiJLJqKp3NhNZy-FEthH_NRqyo3suC6yrFtuXE2vOnWirXJGWlMxACaXcB4P6b4wQ0JAuBdMrECdKz239uSeiH1ZDvG-UMrfiJ8LSFkGlfu-DsN2CGe_C0NVxDlSb9v6S1L9IZypFuG1aip-7ZtcYUpg2uQJUMadadPx0ya6vmSZX_9xCJfoBfNIX1g81Mm5WH_tUmS9Z9P9o8DkOac9qyG3e1QUJntsKcu6Rw6a13X8KN7ualBNTJUiL4_4r87K7IEQsnkld7hLePtgjkRsvuJ89xGedLgocnICLnJIm1MWA0o8uTQhI8p05t3JqozTv-RT0prsDJEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0b13070c.mp4?token=F4Z5LsoPeFgiJLJqKp3NhNZy-FEthH_NRqyo3suC6yrFtuXE2vOnWirXJGWlMxACaXcB4P6b4wQ0JAuBdMrECdKz239uSeiH1ZDvG-UMrfiJ8LSFkGlfu-DsN2CGe_C0NVxDlSb9v6S1L9IZypFuG1aip-7ZtcYUpg2uQJUMadadPx0ya6vmSZX_9xCJfoBfNIX1g81Mm5WH_tUmS9Z9P9o8DkOac9qyG3e1QUJntsKcu6Rw6a13X8KN7ualBNTJUiL4_4r87K7IEQsnkld7hLePtgjkRsvuJ89xGedLgocnICLnJIm1MWA0o8uTQhI8p05t3JqozTv-RT0prsDJEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
🇪🇺
دبل مالن؛ گل سوم رم به رئال مادرید
✔️
پ.ن: این گل در ابتدا آفساید اعلام شد اما پس از بررسی وار تایید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/108740" target="_blank">📅 23:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108739">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وینیسیوس بعد پاس گل به مالن تعویض شد
😂</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/108739" target="_blank">📅 23:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108738">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مالن در نقش عمو جانی
😂
😂
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/108738" target="_blank">📅 23:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108737">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اوووووووف چه سکسی با مورینیو دارن میکنن
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/108737" target="_blank">📅 23:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108736">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
گلگگلگلگلگلگل رم تاییییدد شددددد</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/108736" target="_blank">📅 23:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108735">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آفساید نبودا
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/108735" target="_blank">📅 23:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108734">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگگلگلگلگ سوم رممممم ولی آفساید شددد</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/108734" target="_blank">📅 23:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108733">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35b55a0570.mp4?token=tBMCKAA8Tm-V5Zxo4N_BUwBGfIE0g3ZRb0LD817iJfpth-i70eZcgQdJMQDv37njnAJpMc5CgyVi55EWDHEMZypb3LFw0y_UB-ukD1ydNPd5moxOG9IrkPLYK7KgNbh_dOhwK9DdeAlB416wn5GM_6TdjoNx_ExH8coSzi1m9kNCeSKS0cx5-0DnVX0CelZspjRfVlWWhJhM-zUN_V4MSecuwA-dOzrUzwMeNEkMcR2vsMh_aDkRZrBZTonPt16uPpSSVvA_DjjcR9ZwwIwNwYyuUiBJX9P-R7-8uuJmROUPMwFJ-9xOuP6rg-VziPZ_BFfPs11AlTXik7llSNqHcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35b55a0570.mp4?token=tBMCKAA8Tm-V5Zxo4N_BUwBGfIE0g3ZRb0LD817iJfpth-i70eZcgQdJMQDv37njnAJpMc5CgyVi55EWDHEMZypb3LFw0y_UB-ukD1ydNPd5moxOG9IrkPLYK7KgNbh_dOhwK9DdeAlB416wn5GM_6TdjoNx_ExH8coSzi1m9kNCeSKS0cx5-0DnVX0CelZspjRfVlWWhJhM-zUN_V4MSecuwA-dOzrUzwMeNEkMcR2vsMh_aDkRZrBZTonPt16uPpSSVvA_DjjcR9ZwwIwNwYyuUiBJX9P-R7-8uuJmROUPMwFJ-9xOuP6rg-VziPZ_BFfPs11AlTXik7llSNqHcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول منچسترسیتی به پاریس توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/108733" target="_blank">📅 23:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108732">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگگلگلگل سیتی یکی زددددد</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/108732" target="_blank">📅 23:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108731">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb86d45e15.mp4?token=uJLTt39TTxq11cyKXRWTJXAsWQrcqFslJ1Imy7_y2ba9DY9VtVsr3IfrNRG0QoWvC4qespmGyZR8P1-4iDpIamAO8qSzAgv1W-s4sSRjMA79QFwUioDMQBoGYu-_ylebdIG9jkFF9ZHyRjEDcykRUGlbElWfhJJT8HCvvOHZso6cTu1rLbNQTFgUmK2UzvQ-VU1-JyrF7TJZkdxYOUNpiWLDQ44rZ3yDOE7id9BV4qsV02sZRGJNEjAhUbjbNdo9r8eW0h-djqFgtUNzn2Xf53WMb4SKgujD5YOlqM1OW7g8r0rhQnAbqq-n-LuIUShgYpKanOF9tvY07eu2OOlr6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb86d45e15.mp4?token=uJLTt39TTxq11cyKXRWTJXAsWQrcqFslJ1Imy7_y2ba9DY9VtVsr3IfrNRG0QoWvC4qespmGyZR8P1-4iDpIamAO8qSzAgv1W-s4sSRjMA79QFwUioDMQBoGYu-_ylebdIG9jkFF9ZHyRjEDcykRUGlbElWfhJJT8HCvvOHZso6cTu1rLbNQTFgUmK2UzvQ-VU1-JyrF7TJZkdxYOUNpiWLDQ44rZ3yDOE7id9BV4qsV02sZRGJNEjAhUbjbNdo9r8eW0h-djqFgtUNzn2Xf53WMb4SKgujD5YOlqM1OW7g8r0rhQnAbqq-n-LuIUShgYpKanOF9tvY07eu2OOlr6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
گل دوم رم به رئال مادرید توسط مالن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/108731" target="_blank">📅 23:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108730">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئال مورینیو جوکه ناموسا</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/108730" target="_blank">📅 23:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108729">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اشتباه سمی وینیسیوس
🤣
🤣
🤣
🤣
🤣
🤣
🔥</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108729" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108728">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مالنننننننننننننن
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108728" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108727">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رممممممممممم زدددددددد</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108727" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108726">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/108726" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108725">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🏆
آغاز نیمه‌دوم بازی‌های امشب</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/108725" target="_blank">📅 23:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108724">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh1WX2BREhdWqyHI2KzuHSF4ojbH8jTF_HAUsCn-QHP2Gfa5ykgVYlRAxG1Q42cGhtJwdaL1JKDYqMjhKRBOXrB8Fveku1D_Qn30oNW5TAtfZ49rO62rh2DqoDhSTiUQIeAr86TNdI9vUmp9AGkCjKBrByAFzcxsKyxJZ_mLYjqOXzLjQBHhd7i0pKUKCr1is_YlcNbW2G_BE1PhTpRMnfOcplJr1lh9ObZNA1ubuCAt43y_9UU7beBgX4oE-VQ6Da3O_bDsNloNcrK6olfOVNRQwiaExinZ_bVJBbGvZdJ9k0JGNyrrNg-DU26Kx-0VnxdSDGHGqlJLh23tHQ5oOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
کیلیان امباپه با عبور از رائول گونزالس، به پنجمین گلزن برتر تاریخ چمپیونزلیگ تبدیل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/108724" target="_blank">📅 23:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108723">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2200a192d7.mp4?token=j2CZ59f72uI1KXVRJSuEsaGI3_-a_nmIIQrDbqCLPmKdam6jy8bSIT7aOR_lLJRuZnOCyi6MocZWnHZcUuYg2UW_LXf1EMas4-NnHhRUH1XOSesIpJQ7wzlsirdXR_UQl3qWHrUqGsx_-QNwRLdojVYS4acmX83eDJ-QTPR2T_c6JatRVFvi3iiYFHjeJ7NqYurEzoxAWrOpw8PbJpNr48LwqOFLAs6-7yRqZrNn2eI0yWEads_-ltVQxv8mTMFHSfZjTYyn9CavMwIqdkDWc_TY3YAFcilZVnZuNLpdkA9euIwFsC5aaFT0Sb7jol8Ucan-W2WUTBabWTvKMJ8Wbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2200a192d7.mp4?token=j2CZ59f72uI1KXVRJSuEsaGI3_-a_nmIIQrDbqCLPmKdam6jy8bSIT7aOR_lLJRuZnOCyi6MocZWnHZcUuYg2UW_LXf1EMas4-NnHhRUH1XOSesIpJQ7wzlsirdXR_UQl3qWHrUqGsx_-QNwRLdojVYS4acmX83eDJ-QTPR2T_c6JatRVFvi3iiYFHjeJ7NqYurEzoxAWrOpw8PbJpNr48LwqOFLAs6-7yRqZrNn2eI0yWEads_-ltVQxv8mTMFHSfZjTYyn9CavMwIqdkDWc_TY3YAFcilZVnZuNLpdkA9euIwFsC5aaFT0Sb7jol8Ucan-W2WUTBabWTvKMJ8Wbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
🇫🇷
گل سوم پاری سن ژرمن به منچستر سیتی توسط ویتینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/108723" target="_blank">📅 23:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108722">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ce1546c046.mp4?token=RmIb11UbB6aOKZleMMjKXAac0ls2N-ykUXU0PL1ajQ5R_5yAFRj3rqEHJaGfurKn-8dl0rcyhsEBXrvNrv84i6niM4Qyel7Y-8KJAU7X8-9cJgz1vKjq7-qAC9tSl5-7I5WMhZRcnpOgv6LgzskMW_-FZ04IkanIwIx2zUUlXXXRh_KwvXssSPnBwTCCR0GMRJdPiyoyWgOvj2Rhie4psrbsOJrJa7CskIM2bk-Gbx2U5zgTioPkD4l7idtWBz3SroeBe1Cn3CtK5TfNYwwBo4qsGyaJMfMKfRm-2XvcjtzcYhoR4lF5Ui59u4hhHcVo8k5jlaBCnr7vSvQ_mgsj5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ce1546c046.mp4?token=RmIb11UbB6aOKZleMMjKXAac0ls2N-ykUXU0PL1ajQ5R_5yAFRj3rqEHJaGfurKn-8dl0rcyhsEBXrvNrv84i6niM4Qyel7Y-8KJAU7X8-9cJgz1vKjq7-qAC9tSl5-7I5WMhZRcnpOgv6LgzskMW_-FZ04IkanIwIx2zUUlXXXRh_KwvXssSPnBwTCCR0GMRJdPiyoyWgOvj2Rhie4psrbsOJrJa7CskIM2bk-Gbx2U5zgTioPkD4l7idtWBz3SroeBe1Cn3CtK5TfNYwwBo4qsGyaJMfMKfRm-2XvcjtzcYhoR4lF5Ui59u4hhHcVo8k5jlaBCnr7vSvQ_mgsj5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌اول رئال‌مادرید توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/108722" target="_blank">📅 22:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چه شوووووووتی زدددددددددد</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/108721" target="_blank">📅 22:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">امباپهههههههههههههههه</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/108720" target="_blank">📅 22:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108719">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گلگلگلگگلگلگلگگللگ</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/Futball180TV/108719" target="_blank">📅 22:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108718">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a05da81d0.mp4?token=vAgwoqj0co3ZTPaySnsXdn-VGpa_PNJXeNzY5y14X406i8vOqUxMxC-n1PtEvPsqaEmvjSyrumBDyIAwl6fyJmyx8MN7VVjG6_HPF9N1ScQ4YoGL7iBZXqQ6Id8yzsb4B9cbeUJe2ts8tkg9zRNHs3UrMCWhE2wJYzRg1rFXlORIlpjURIruGp9eI2UzPGfIlOXaBtHDBvMGxHEMaHyv6io3aXEdWv1SNelE8IbkWYZDMIXR-_OpDQlPEdKDDK5QIVDDK1yaJoIh_Ys-ASfpI1TdneFyItIHOoiPOkOn1bMvKhOQfNbmS7P4kDmSSDZ1Kw966vFyPwfSASULe8tzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a05da81d0.mp4?token=vAgwoqj0co3ZTPaySnsXdn-VGpa_PNJXeNzY5y14X406i8vOqUxMxC-n1PtEvPsqaEmvjSyrumBDyIAwl6fyJmyx8MN7VVjG6_HPF9N1ScQ4YoGL7iBZXqQ6Id8yzsb4B9cbeUJe2ts8tkg9zRNHs3UrMCWhE2wJYzRg1rFXlORIlpjURIruGp9eI2UzPGfIlOXaBtHDBvMGxHEMaHyv6io3aXEdWv1SNelE8IbkWYZDMIXR-_OpDQlPEdKDDK5QIVDDK1yaJoIh_Ys-ASfpI1TdneFyItIHOoiPOkOn1bMvKhOQfNbmS7P4kDmSSDZ1Kw966vFyPwfSASULe8tzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به رئال‌مادرید توسط ده‌رون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/108718" target="_blank">📅 22:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108717">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رم یکی به رئال زددددددددددد</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/108717" target="_blank">📅 22:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108716">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگگلگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/108716" target="_blank">📅 22:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108715">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f643783689.mp4?token=nhBbdkMQh9rHzc7wX091vQi6ybY5Z5Ri0B3KfO7SAKrqNjJOEJ119S0IW5PPvp6U6MH6VQYBmjhXyRNqToz2DxIgo8Z5X9HZ3AEX3gk2xCUwDIve1PqQIAk0SBg6SvV0bTNFfHtMwtct5QJJqQuMMIgMNkmzvGA54mr0CmfOQQdDuKD8U57c_lZFQLuwyGs9aSy21ilPZGztQOhhhbmWlL3ppp8A21WhvCh1cVRLFFYi9b8bI3ieEjbbGvq8HPnyRXYRZumvZ4FcAUgbyKcPT8qtD1SO3ykL2ALVm1-z5oLmfOHC1DSHwL3QjsEkxmg757j9WnGUAVSZvOfQ6C_7Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f643783689.mp4?token=nhBbdkMQh9rHzc7wX091vQi6ybY5Z5Ri0B3KfO7SAKrqNjJOEJ119S0IW5PPvp6U6MH6VQYBmjhXyRNqToz2DxIgo8Z5X9HZ3AEX3gk2xCUwDIve1PqQIAk0SBg6SvV0bTNFfHtMwtct5QJJqQuMMIgMNkmzvGA54mr0CmfOQQdDuKD8U57c_lZFQLuwyGs9aSy21ilPZGztQOhhhbmWlL3ppp8A21WhvCh1cVRLFFYi9b8bI3ieEjbbGvq8HPnyRXYRZumvZ4FcAUgbyKcPT8qtD1SO3ykL2ALVm1-z5oLmfOHC1DSHwL3QjsEkxmg757j9WnGUAVSZvOfQ6C_7Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
گل‌دوم پاری‌سن‌ژرمن توسط عثمان دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/108715" target="_blank">📅 22:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108714">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbdb76e007.mp4?token=XqRGXcbQInic909YXCKXqqoukcPP8C2UtB4SUkqiFz-H9t7QNP5yEOm6nWcYcmfnzDv2gn6giSeOKfKTpLrIf9qHpXwveCSWiLHTnnXDgTwdyQuhbgEy5599qY6bhx-0irFEJVYwUj2Q7R8fWNGcCMdyGFd9KT30yXf5Z9WE9gsASUhZD7ts4h5KXcLQ8FjvIPItKXQF0b5WASohmyak6XvgEyHOmHUrR6U-3YAVw2NiaR69L1Q_tJKHMi04sa8SJSbBwAleCXqQ30wxycOuSYiYh3QSsr5SrJGyHYqz4ezSnKoLSkd8lGXv4N9zWpBXNvgoS93ztvWskLX2umQ0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbdb76e007.mp4?token=XqRGXcbQInic909YXCKXqqoukcPP8C2UtB4SUkqiFz-H9t7QNP5yEOm6nWcYcmfnzDv2gn6giSeOKfKTpLrIf9qHpXwveCSWiLHTnnXDgTwdyQuhbgEy5599qY6bhx-0irFEJVYwUj2Q7R8fWNGcCMdyGFd9KT30yXf5Z9WE9gsASUhZD7ts4h5KXcLQ8FjvIPItKXQF0b5WASohmyak6XvgEyHOmHUrR6U-3YAVw2NiaR69L1Q_tJKHMi04sa8SJSbBwAleCXqQ30wxycOuSYiYh3QSsr5SrJGyHYqz4ezSnKoLSkd8lGXv4N9zWpBXNvgoS93ztvWskLX2umQ0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل‌اول پاری‌سن‌ژرمن به سیتی توسط دوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/108714" target="_blank">📅 22:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108713">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
بررریم سراغ بازی‌های امشب اروپا</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/108713" target="_blank">📅 22:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108712">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇹
گل های دیدار پرگل لاسک سه - شش لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/108712" target="_blank">📅 22:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108711">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxg3lvm4jEz4ujCWx2lmQZUANXtJk2Z90B1f4LucxUrJ4vhk8y03FV7SiD9-6n9HEOlpIcszEHGq1c_8FgWrVBS1zBVZHKlxITb4d0KeDQsR-bSmpVlsy1X9JX5QsZJ5EkChAruM3_hbSaFkISY2vU8MHEOv34BzhVDYvkfEi3knDH-CMr5dq368I2eD1uGiYBSqyKsOd2BczrvsOtEr-HC8ZWQqSJ7he0yzixrXxRewnY1JgsHySjB2pe80hOOeWtk61gfmNgInRx5BOUWQUSY6H9JI7TLXPfefHzflJUSEV9H0qrph9wGz1epTJOD0QNvA78GDHRll2jrNUbIPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
ژوزه‌مورینیو: به عدالت لالیگا شدیدا شک دارم. مگه میشه حکم وینیسیوس دقیقا یکساعت قبل از آغاز بازی رئال‌مادرید مقابل رم اعلام بشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108711" target="_blank">📅 21:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoKYVXKlgWduXO5hCsq-Q5JcREaRl1tDdBGesSr7XqdhuP8MHVcGcgggtqRuMoTJwINn_SBRGwrITqttauPZctsESTp05LrGq62Oag_JqoQF9h_KlmShAmTsqIyDhG8FVT00OjQ7KUivXSFrtlIy7rPQve1sCD6B5P1aPSP2Y_dz7GdxL4uFbu23ZBdixiFtDvW06HA4qyCHFffdnLcVgm6asyz8voDKT75ot4oBivF3S6fkPTxvSXmJBWGLkvqjS3SSyt56N7fs-L4DjVTSadZPYVckGmOe_UkdYM5ep5BmuDxFVRaj_zWfeh8UfyOLbESIAHATTKinUrXrYbSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🇪🇸
وینیسیوس مقابل بارسلونا:
- ۲۴ بازی | ۸ گل و ۷ پاس گل
- ۱۱ برد | ۱ مساوی | ۱۲ باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108710" target="_blank">📅 21:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇪🇸
#رسمییییی؛ وینیسیوس جونیور بدلیل تخلف در بازی با ویارئال ۴ بازی از همراهی رئال محروم و الکلاسیکو را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108709" target="_blank">📅 21:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqlUeK6XM7TdPFZoYG8fKZEcAN_8HROqc1hFaYcVkwiu3FSaFxi1lLDfHG9_JXt34VO9it4uRGADtru62XEU8Mv_cnABsUkaq6FeTOJB-oarKVxbysBXKTkM3sH0d07goLmw4e6V_msHDOV0xx-jMqXficzOXTWQSGtjfUIhusExQo-3NC-JKglaDcoF3_PG9o0GSZbKqJMZUDd4u71Ha_iyzCrUaV3lY6mTSQwRZI5m6SR0wCMKzBJlYbWPDsT6t5csOWdQlAoh7I-2sII6xl8kXSraWSzZ9DY9GEN8ruXgPhSkzTH2Hz_FBUzm3_UTNZqrt8zVltx6zWI15dwCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
🇫🇷
ترکیب منچسترسیتی و PSG
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108707" target="_blank">📅 21:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5I1dZ4-o31T_laqUNI8SYLopIG49Chgu1Uyt-B6lsbXEn7z0nTBmoFaS48ZSgPTIqcJDT3xlhaQpobSkq6-0Ek7EY5Ys-Gtqy7inVm0skLeFKAayC6FHNebEIbxePpj5015KzvCO2w46MQ5gdVmNrCbWfAhvBMvhXn9kPXw2S6tm288itl_hNuXp-8kRv-M5dj9ODt67UuMYXddP5Rm5T8IRm5-rS13pwRV9gG9XjlInGyvBgHodpHEgFQjZYXJx4vZgq4EZDIrbg_zq9mKoC82B4gbmNKS-k766bBGL2DOdBegExhzv2IP6a1tkXIrcdABBope_4Ija9dfjuRF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
🇮🇹
ترکیب رئال‌مادرید و آاس‌رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108706" target="_blank">📅 21:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6fa60164c.mp4?token=uuVph59IYKRS74D2Ez5RRjlgYumZzo6lwMFk-1Pc_RVwbbCYa-lfnwBOF894WVwCId5oaQE-7JBN2q42WNOKK7HiDgIPhm9lo_Wab56tVubntfu9q_d2Z46gbRingRUc_6xoDHRZ1pgjSQsrY71GTIApDT1wW2Bi9hxrCXLbBtkbuctomR_RtzeApgpiIR4NnR8ynElfhtuEo2hEqOso_DA50YF03EjiVP_3t-RjCivzI5uUOUjZQM2gTwoyfmMxiS86NFnxJfc4fMirRKK_TAACxQYXXbAdBtTPee8Wsm8z-I2jEP8xUV0hf9kJqEarlRwUMQknTQ2ONUV-J90FRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6fa60164c.mp4?token=uuVph59IYKRS74D2Ez5RRjlgYumZzo6lwMFk-1Pc_RVwbbCYa-lfnwBOF894WVwCId5oaQE-7JBN2q42WNOKK7HiDgIPhm9lo_Wab56tVubntfu9q_d2Z46gbRingRUc_6xoDHRZ1pgjSQsrY71GTIApDT1wW2Bi9hxrCXLbBtkbuctomR_RtzeApgpiIR4NnR8ynElfhtuEo2hEqOso_DA50YF03EjiVP_3t-RjCivzI5uUOUjZQM2gTwoyfmMxiS86NFnxJfc4fMirRKK_TAACxQYXXbAdBtTPee8Wsm8z-I2jEP8xUV0hf9kJqEarlRwUMQknTQ2ONUV-J90FRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بطری‌باران سردار آزمون توسط هواداران الاتحاد پس از گلزنی دیشب مقابل این‌تیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108705" target="_blank">📅 21:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYqXn2BpWoglq2va9fTflurEEPCnjgwo-z9j7N0RAYyFE78gKVoANS6Hy8DYAXV52-4srbYqKWK3wZT7k4M6_DgFup4EiSi16bUf6vvJayCMKYGilmU0o1dIzwyde35OQE4TNidWNiiA1Zj6bofJUlbZxc0PYIJqlKw5kVdMleRmL9uJcVIJznFD2UwfmE3Pui5XLQ-pkYdxjixeHKjseqNMfW7if9t34lVX_YN8lSvQguVlUvLsfdbKc88VDyKIfNpgLTMdGSMukNNZsZqhYAkCB8eBPlUedA7DAS13j_d0EtZPS8WzAJ18RxM4juQ7GfOBvtDifaugRMm34co3Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمییییی
؛ وینیسیوس جونیور بدلیل تخلف در بازی با ویارئال ۴ بازی از همراهی رئال محروم و الکلاسیکو را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108704" target="_blank">📅 20:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6d0eadf8.mp4?token=I8bqKBmJmbM9AIxM2NwUOUgorvayI1SpzuJw2MQ_usKBmrOZK7v5QSLvoAl30NcdvWjnCra7cdK8rwtC4YJdFvJHEHBocMos9SYajK8DMJPDth4H6oyXN8Ls5eh0vN3KEkIb2F1ifRjYeLPfwfpIHJYa-mJbcejgkrAuwny_R9oHc4fPewdJ4aZjuP45ydoIuAla40CEtjvUunhL6tyZyZoMQXGzjlalW4CRjMTLqeOUC1HPV5qXcAvUUms7jQ3VgV_hC7Lvu3jfyjb3qqkhU6QytrFEBUTKaVJKLtEVp-aMSALjk0vfiUf3OjPhLLKCR3k7rEUPQx0cA4bzy5pRNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6d0eadf8.mp4?token=I8bqKBmJmbM9AIxM2NwUOUgorvayI1SpzuJw2MQ_usKBmrOZK7v5QSLvoAl30NcdvWjnCra7cdK8rwtC4YJdFvJHEHBocMos9SYajK8DMJPDth4H6oyXN8Ls5eh0vN3KEkIb2F1ifRjYeLPfwfpIHJYa-mJbcejgkrAuwny_R9oHc4fPewdJ4aZjuP45ydoIuAla40CEtjvUunhL6tyZyZoMQXGzjlalW4CRjMTLqeOUC1HPV5qXcAvUUms7jQ3VgV_hC7Lvu3jfyjb3qqkhU6QytrFEBUTKaVJKLtEVp-aMSALjk0vfiUf3OjPhLLKCR3k7rEUPQx0cA4bzy5pRNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل اول المحرق بحرین به گل گهر ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108703" target="_blank">📅 20:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81f4ea6e9.mp4?token=sZz66SLzHtc25nc13Nu-w57oRtYWthYIQVhxrO8gL0iOfQqHRVbzGM82DXIl3lF1D2QAGLq-TbMDfX0KwDv5c-_NNRSI-v8iXEwcEl2y2rRlp4XoPiTD_3x3pb6FzVaITXqh0gFL81RMgxmZQv1u8_zGGXbgfpovNLM9CTLYJB4CJv3Z2YEIiDVsyVjX3XNtqjhfFG-CmNfReWGdujuSSFcxSj5Tb6JElBmlxdyqwLRBSI5M9rbUUv3NJRTcZlfCIdSmt0Okil_5bG61AsT7uAr5BxW4rnUgpHXIwCOa0NbRDvAB4LYkiR_cRhokKIDyxpS8-xX1OKwR3Fgyh7qY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81f4ea6e9.mp4?token=sZz66SLzHtc25nc13Nu-w57oRtYWthYIQVhxrO8gL0iOfQqHRVbzGM82DXIl3lF1D2QAGLq-TbMDfX0KwDv5c-_NNRSI-v8iXEwcEl2y2rRlp4XoPiTD_3x3pb6FzVaITXqh0gFL81RMgxmZQv1u8_zGGXbgfpovNLM9CTLYJB4CJv3Z2YEIiDVsyVjX3XNtqjhfFG-CmNfReWGdujuSSFcxSj5Tb6JElBmlxdyqwLRBSI5M9rbUUv3NJRTcZlfCIdSmt0Okil_5bG61AsT7uAr5BxW4rnUgpHXIwCOa0NbRDvAB4LYkiR_cRhokKIDyxpS8-xX1OKwR3Fgyh7qY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
باشگاه خیبر با انتشار این ویدیو نوشت: نمایی دیگر از خطای واضح روی مسعود محبی در محوطه جریمه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108702" target="_blank">📅 20:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1370be90f0.mp4?token=hS_0NYYECiB0a0_l_8FvsCxbggQB76hOHmblfG8rVKwVOXdO11rxExYZqKnNnWh7mwK0tCTYFS6SK40CX5h-IlfPSxzvWLOwV0f641_30tc2BoYVmtjv8RGQa3fAq4CHLzYDd2hbkKE1xP42ZYQl2pz_kPfGuCkmFEMaWOyGBXH8SNVqitzAUl0Rp0UP9J0n8dTULanG0tYaoGbpHCvr60a3LfNZ8O-WaYTvblUhfAbWimTVvGl41itYhi0OLN3cQ_qVmo5BZeFxbu31_JeieLnOaVqnIVaGUuA89BDdgTzAsu6hgov3hCDPZn9VUI6lteVLYxU8SwMcZKpVBr_Npw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1370be90f0.mp4?token=hS_0NYYECiB0a0_l_8FvsCxbggQB76hOHmblfG8rVKwVOXdO11rxExYZqKnNnWh7mwK0tCTYFS6SK40CX5h-IlfPSxzvWLOwV0f641_30tc2BoYVmtjv8RGQa3fAq4CHLzYDd2hbkKE1xP42ZYQl2pz_kPfGuCkmFEMaWOyGBXH8SNVqitzAUl0Rp0UP9J0n8dTULanG0tYaoGbpHCvr60a3LfNZ8O-WaYTvblUhfAbWimTVvGl41itYhi0OLN3cQ_qVmo5BZeFxbu31_JeieLnOaVqnIVaGUuA89BDdgTzAsu6hgov3hCDPZn9VUI6lteVLYxU8SwMcZKpVBr_Npw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برخورد زشت امیرمحمود داودی‌نژاد، روابط عمومی هیئت فوتبال لرستان با خبرنگاران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108701" target="_blank">📅 20:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❤️
محسن خلیلی مدیر پرسپولیس: بیفوما در بازی امروز بدشانس بود/ بیژن حیدری بهترین داور ایران است و در مورد پنالتی باید دوباره صحنه را ببینیم
.
شکایت استقلال از دوپینگ بیفوما؟ اگر مشکل داشت امروز بازی نمی‌کرد؛ مس شهربابک باید هتل ما را فراهم کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108700" target="_blank">📅 20:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNRnhMyjuqC7FSrai8kOi0NfwfKPmTQ52GL6YlGewazPBOhNhpYiRE4tOmUCbYg-OMj9QiA7Uh8HqNNVYtQIv4zKBmtUz-8p_P96UZ3INLgGXxhfxHFqAmopye-_w_4s6vfKhfhT9dZmaSA_oH875ORQdUCo6tGQIF3Uougcy4pG8Wr02kj0W3tK8UQ8860cozpgN6KY0L5T7bECAdUARhKHahXVScm3Wc7BoaWfXK5dlLwCSf51dboX5AK1-HJRawjqsh5UPvUsgP_WCAbLrwggxFCnGAwN23UyJqEGPYiVcMmGMxv1eH0faQM395HA3ot87Fbfgl3d7byQytyqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معوقه‌هفته‌هفتم لیگ‌برتر؛ تساوی بد موقع سرخپوشان در نبرد سنگین با خیبر؛ دیناروند ناجی تیم کمالوند شد
🇮🇷
پرسپولیس
0️⃣
-
0️⃣
خیبرخرم‌آباد
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108699" target="_blank">📅 19:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108698">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDC978w9JPdvLatLvPHqnsHTFZUdn0ZVUD8S_NrzAMWvP7b8ZVHFbEffunxWBkb2fLvWXU-COLpgiaAE_shCCzRlvo5Cf4t7Z6f5W6oO7QfFph5drnyWLcuMYLyFkZM_x2QShD4bDhvAl4iFfjOd7tZ9MpNLICqqo4MuzXdTUol9ADzgnEwLvMa33VoUfJotLJcGih9mxo8LbgHVp6EvyX7XaIxgJxtB2wV4MIVz4V8fD6zZsZ-Y-854HDEEXJGz4TUTGOYT9hljeAtQlsG71cnlgFPAmbWusbIL5OZzaAWbzSA_KboTX-v2IuDFei1wh61B5HWOnullhUQGUkQhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معوقه‌هفته‌هفتم لیگ‌برتر؛ تساوی بد موقع سرخپوشان در نبرد سنگین با خیبر؛ دیناروند ناجی تیم کمالوند شد
🇮🇷
پرسپولیس
0️⃣
-
0️⃣
خیبرخرم‌آباد
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108698" target="_blank">📅 19:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108697">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpYz2s5xgJBQJt562ixGb5PM-2mMtZroOaBa0VA-EUeFtI0689EexZsgMqj6htpShQmvHfahg62WW6C8v1ZaYpIKDdbpHfhxrQRujk_YxXkGxgrpc3q4J0yX3OPQaMgbTyI02HK_DHdhTth4jkI6JQsWqPAQMr-5cntOpraOR4nb5mNI5cZcJXZCjR62Dk4ZK6cBv6An2ew675Sijgp_1N3lfGvJ09ai83ELGPx5BAXwOhLCT4ksQEVGkbyAk1PplKWVb1x5inGCqXd-0_K3Uyj--AALbvnZRRLeFhHDB6vZKG53xq3u7JM913ZYW3hjtdbGlCPNQSr1zGjFxsOHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇹
ترکیب لیورپول مقابل لاسک‌اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108697" target="_blank">📅 19:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108696">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fd1c54704.mp4?token=SfbymqdQnTxqm8CvHy6_BAkG8-j0efzcOkvpHUS22O-0rfWdV6DQRXGQu7-CQi4zYen2h5dtX3iV1zGNWIAgvfcialxQUZgSLJ6NcVriA1t7B4BUyDvFBTvo-WfWvE9OhuCoEBafFgQONJk1BzD5PFHQ8SrVGw2ZW7Y4EWlu4k-BXqnDQJjLC12ZvwWXLs8ZqOyfvDOPOrdNCdKxIGaskt-OjJRu3mse1KMrClWdrkj0cMOc64q1j6BmJou48DXb7kelmUqkhGQ_Kh-QjVC7mY24oqPRHB0E31A68lO4xNI__xOAOMYiktvnTiCpG582OGny8iziR0XPy9DbE4ykhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fd1c54704.mp4?token=SfbymqdQnTxqm8CvHy6_BAkG8-j0efzcOkvpHUS22O-0rfWdV6DQRXGQu7-CQi4zYen2h5dtX3iV1zGNWIAgvfcialxQUZgSLJ6NcVriA1t7B4BUyDvFBTvo-WfWvE9OhuCoEBafFgQONJk1BzD5PFHQ8SrVGw2ZW7Y4EWlu4k-BXqnDQJjLC12ZvwWXLs8ZqOyfvDOPOrdNCdKxIGaskt-OjJRu3mse1KMrClWdrkj0cMOc64q1j6BmJou48DXb7kelmUqkhGQ_Kh-QjVC7mY24oqPRHB0E31A68lO4xNI__xOAOMYiktvnTiCpG582OGny8iziR0XPy9DbE4ykhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
عباس قانع گزارشگر دیدار خیبر - پرسپولیس در واکنش به موقعیت‌سوزی تیوی بیفوما: تیوی بیفوما کاری کرد که شاید خیلی از هواداران پرسپولیس تی وی را خاموش کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108696" target="_blank">📅 18:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108695">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv4Lq814we4an61wqGjnwPydaUQ8Z0Z4lt4EtPMgSiG5634BkBhRqxSz8HkUqbG6xU-V39wj5QXwOmRJRpuW9wv96AJDvi-bRSgtM3W6BbwRq54R-w5cZOIzRQvU9S4XHpKZh3i2TAAza_X4WWZidWuosOcz42YaMsLDl122CN6RrN4dujy7K163rscRiGpdHAXp0DvTXG-4QMsBf-7MuLy5sur0wIZ5WKe9kHwms6q59k0hIquObgyRfZ33tUnuHGTYN_XApUMk44l7CBrLVnopi6t4vPEgbk8d088qKvYMGQj83MA4ORcDdsjrKsuy8biF5phRJAfuqUw7o0O-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب گل گهر برای دیدار با المحرق بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108695" target="_blank">📅 18:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108694">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ff4c42d8.mp4?token=JTQ1TYZN2Wz5r_ohV1QosHnFOZf5goFrcrrG1xtYvheEAbh2X1wazilqMx5rLoG-QT0MQtcpJdejAH9zJqTdDMNepwUZ7DF66Dhunb-Bkk_Xem487ikRYixwO0znijtio2cSRcOtLVlcKUZrrCJKO3jyI2Rh4L10jOrku0GVQSBdG7wDMh6UVunRaUy14f4YAtPXpO5ng5VIMtVTvCu8YRjc92iCDLSX20rqwlFwOZSmPpwAYhMpr_du6ojf_BND4vhruNUIADwPSrqoBllrBfFIi2bqdKsq0cllZI8l7nK48Ceg5VqBRZrz4rMSFUaCs30EmIapacyxQiacVGj2rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ff4c42d8.mp4?token=JTQ1TYZN2Wz5r_ohV1QosHnFOZf5goFrcrrG1xtYvheEAbh2X1wazilqMx5rLoG-QT0MQtcpJdejAH9zJqTdDMNepwUZ7DF66Dhunb-Bkk_Xem487ikRYixwO0znijtio2cSRcOtLVlcKUZrrCJKO3jyI2Rh4L10jOrku0GVQSBdG7wDMh6UVunRaUy14f4YAtPXpO5ng5VIMtVTvCu8YRjc92iCDLSX20rqwlFwOZSmPpwAYhMpr_du6ojf_BND4vhruNUIADwPSrqoBllrBfFIi2bqdKsq0cllZI8l7nK48Ceg5VqBRZrz4rMSFUaCs30EmIapacyxQiacVGj2rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرصت سوزی محض بیفوما با وجود دروازه خالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108694" target="_blank">📅 18:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108693">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0b102f02.mp4?token=S3ZDUuD3g24j38P5Q2wQ7ht2GPpcE9cLybXfSbQjFOgroKH-8vJ8H8p0phSjmgFkL78gFHQzoyejdL33PDJ0Fupy35t12uUAsbKvOW-NPDxqANf0udOo-VBgp1dGb5khhtb8y2GlcXFYE8XKY-rYNMaJXQZeAexljgn8C62DK_z0jK5hxGlXKxTnWrVNLcBAWmaQgnK6N06DcR5EpSy9U9BKcbLB8PexQ52En49jZdzrBByzTS-Y3YMlZ5_eN4kPFzT4kxfxwQBRXpsmavqyCRW1_BAj6X7LgXaUYrNtVRsWv1rXafpmknkPHrv89iGkM-IAh8xdHnslpj0TLWZt9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0b102f02.mp4?token=S3ZDUuD3g24j38P5Q2wQ7ht2GPpcE9cLybXfSbQjFOgroKH-8vJ8H8p0phSjmgFkL78gFHQzoyejdL33PDJ0Fupy35t12uUAsbKvOW-NPDxqANf0udOo-VBgp1dGb5khhtb8y2GlcXFYE8XKY-rYNMaJXQZeAexljgn8C62DK_z0jK5hxGlXKxTnWrVNLcBAWmaQgnK6N06DcR5EpSy9U9BKcbLB8PexQ52En49jZdzrBByzTS-Y3YMlZ5_eN4kPFzT4kxfxwQBRXpsmavqyCRW1_BAj6X7LgXaUYrNtVRsWv1rXafpmknkPHrv89iGkM-IAh8xdHnslpj0TLWZt9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فرصت‌سوزی تک‌به‌تک عجیب محبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108693" target="_blank">📅 18:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108692">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575fb08f89.mp4?token=Wq2TDiAjKpwHTIyQ6fhUBBaCtHceVHpmiGvJ_c6KjySQtkifg4a75TJCWYmX1_tgjaIoVU9yoUjRjuClcUiO8PifFr0AXTwDSGEhsmDhNevHlgwO6h-Oxv8Ysj1QaY4yp5yrda9VXQa56tVJBrRzqOS1y7lCXVnleE0EW8-HWS2gOgrzjFKZugKDz6HL7hqP6jG7GNsMZpy2jWC4NRVSIMR72_RyPZWkc9Zn_IWFlQBRIilRIEdSr15T6GdNLYqyawVKSxMW4-nSdQbttTiWtjjbkktT4AqLM9mrNpnXjSLoYDJdXID1AWFgg_fQ8KjQ87tBZV8NvmIUQuU1p0D0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575fb08f89.mp4?token=Wq2TDiAjKpwHTIyQ6fhUBBaCtHceVHpmiGvJ_c6KjySQtkifg4a75TJCWYmX1_tgjaIoVU9yoUjRjuClcUiO8PifFr0AXTwDSGEhsmDhNevHlgwO6h-Oxv8Ysj1QaY4yp5yrda9VXQa56tVJBrRzqOS1y7lCXVnleE0EW8-HWS2gOgrzjFKZugKDz6HL7hqP6jG7GNsMZpy2jWC4NRVSIMR72_RyPZWkc9Zn_IWFlQBRIilRIEdSr15T6GdNLYqyawVKSxMW4-nSdQbttTiWtjjbkktT4AqLM9mrNpnXjSLoYDJdXID1AWFgg_fQ8KjQ87tBZV8NvmIUQuU1p0D0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماریو لمینا قبل از بازی: یامال کیه؟ من سانه رو می‌شناسم ولی یامال رو نه!
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108692" target="_blank">📅 18:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108691">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108691" target="_blank">📅 18:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108690">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnkLDWMxGtdmXyvlcEfFj6UEYZpzO38dn79oK3fr1u7NFP6q3VR_uXqFsdJvTe05q5ICX5JIeHlSCpbdlNhvKaq9XVkN5brBDjFhjzkSFKiz4DChbElvbteD7LnnhDYISTzn12HnRtjL84pAr2fukjvc_eCtO7vaQqmhqjpHYCoiI_arFJlr_PKrP0_SEB3aeDIy3jdRJH9yB91i73NJz9pUi7-q35Bq459AlMswIS9Irqj56LFZq86ADGwb3Qj3_xCdf9RYzha9ff8ilVh7yoJKuK0TpFHl9lMpr09TidUIYDyjzGuM8qTlv9VfyrboD75_F7Ohf0DCb45aHU9MYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئال مادرید
🆚
آاس رم
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم در ۵ بازی اخیر:
رئال مادرید: ۴ برد، ۱ شکست و ۱۱ گل زده
آاس رم: ۲ برد، ۳ تساوی و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108690" target="_blank">📅 18:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108689">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
لحظات بررسی صحنه پنالتی رد شده پرسپولیس توسط بیژن‌حیدری و اتاق وار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108689" target="_blank">📅 18:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGxgyuN0e5mJlGAtNpKORGaQWispNLVMcx-k5LIQvWx12crXYKJRFhW3snWled_acMx76CV5vaqWRc08bI_pFC7-ERdkUuiPic80chKbA6v807Suu2XB3datAkh6PlNoxSetxcjFaLsxc1wlyoIdKwkY8_LdzqPFbYpaKAcjn3cWamHEC-Fi8sSo50Y_W_5bjbZIZbbuoYIX3YrWCsbsKqrMZ2YiVcQjBMUHQ0vNiQlMjzaHzqNZWYmhw1Ah6mem1E1LfPOHQ0XT2SKKgPhVv9wvK14STQMu_CEBX0Zr9aUKouHGaKxG7_aRMMZGp4BKil9vnv3S4EjKwK5I5HVQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇩🇪
شفق قطبی، آسمان بالای استادیوم تیم بؤدو گلیمت را قبل از بازی آن‌ها در لیگ قهرمانان اروپا با تیم بوروسیا دورتموند روشن کرد.
🌌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108688" target="_blank">📅 18:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
لحظات بررسی صحنه پنالتی رد شده پرسپولیس توسط بیژن‌حیدری و اتاق وار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108687" target="_blank">📅 17:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
پنالتی پرسپولیس رد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108686" target="_blank">📅 17:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇮🇷
صحنه پنالتی پرسپولیس روی اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108685" target="_blank">📅 17:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=naEDxlLzvDuAsB6wAII3fAIk6SsfacqzRIKCaq05FoS3TDO9klGQhb9I0I8fbCU-plmbNeu7Yx14vlxjz4VeTeCzaitd0OP4_sDb2ghsnpQfO59roXPABfCIoBrJE-vrEV9eDWsdkj7Y9tmSieppby6uqIm9OcMSR86xvrvipP-jV-yDwKWcBGE99z5EPsR2hdKrbezqjt0fFUFCvEEAao_qNrMy3oSCW6_a_J8aRJRLo8zXH_oHKM5iqqnEyTD92eQb5BLoJ4z-Dm_wXA5fy9zpqueSd_Ny-RMhBoXhfQlcm4aezFshGLT0c5mLWLPGemxWFB-cX_6kHlqmfurDpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=naEDxlLzvDuAsB6wAII3fAIk6SsfacqzRIKCaq05FoS3TDO9klGQhb9I0I8fbCU-plmbNeu7Yx14vlxjz4VeTeCzaitd0OP4_sDb2ghsnpQfO59roXPABfCIoBrJE-vrEV9eDWsdkj7Y9tmSieppby6uqIm9OcMSR86xvrvipP-jV-yDwKWcBGE99z5EPsR2hdKrbezqjt0fFUFCvEEAao_qNrMy3oSCW6_a_J8aRJRLo8zXH_oHKM5iqqnEyTD92eQb5BLoJ4z-Dm_wXA5fy9zpqueSd_Ny-RMhBoXhfQlcm4aezFshGLT0c5mLWLPGemxWFB-cX_6kHlqmfurDpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
صحنه پنالتی پرسپولیس روی اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108684" target="_blank">📅 17:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79edc7079.mp4?token=TPlozajcRauM2-YO4jhGyF_TiTMU7i3HUuj5OVyMo_5JANDJoWMtPQEbHQYCCge_Qo84F3NaYwKe84yQhihrvQdNqJuFizZiQWvvLKp9FMa6BdoSbm6AXPi_0gWOZg0nr4nHEcYcoIBGr2qwGYRgaMuPjVooA67wXNPYCWvpRHY3b2ohr0S14Q5G83hFiay-y_nCgSKLd9LobaeNCU1ohWluyVU9uDi6TyFXEZkKUJT2weJa9yl9hVv9MXURblrIJ9wLH5KuKa76o7r-Lxmz40kIy6MHGo8KJjVFMsQ6HErB_NaXjNP6Y5H0LRTclrmoIaaSy4wL4GPy-BiRBcWkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79edc7079.mp4?token=TPlozajcRauM2-YO4jhGyF_TiTMU7i3HUuj5OVyMo_5JANDJoWMtPQEbHQYCCge_Qo84F3NaYwKe84yQhihrvQdNqJuFizZiQWvvLKp9FMa6BdoSbm6AXPi_0gWOZg0nr4nHEcYcoIBGr2qwGYRgaMuPjVooA67wXNPYCWvpRHY3b2ohr0S14Q5G83hFiay-y_nCgSKLd9LobaeNCU1ohWluyVU9uDi6TyFXEZkKUJT2weJa9yl9hVv9MXURblrIJ9wLH5KuKa76o7r-Lxmz40kIy6MHGo8KJjVFMsQ6HErB_NaXjNP6Y5H0LRTclrmoIaaSy4wL4GPy-BiRBcWkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇶🇦
🇮🇷
#رسمی
؛ ریاض‌محرز ستاره سابق سیتیزن‌ها با عقد قراردادی به الشمال قطر حریف استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108683" target="_blank">📅 17:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVQl3Uw8UCyTMM7i_awSMnbEBts5BJtqVeNpaGPk7xTD11B6PfvDmFHz6SC7DV7dW78YGQjl1y4_FAeD6sqKz1VzVnGFB1c_F0hutSvJmKfTwQMcl-oGiS8FixbbRwLU5VcEsZ7k5szb4QXBbsLCxTJGbUKSc5S-h7rT1um_w8RlvJsLdXiKOMKsG2TGeduxHq-cutOjJB3OiLEjmYTEqTp6bt3rJ0I5feVSzvGqav7dwSHwJlAigmiP1c9X6Gqxaqc2jR0dBcF-KnwJbsPHO7xHIcVUAfblkznOvAKDlKWWTT2gMDminQ6Mcqb6hvjOLbe-OL1c7kJdJocF5ZKN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
ترکیب منتخب بازیکن رئال‌مادرید و آاس‌رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108682" target="_blank">📅 17:16 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
