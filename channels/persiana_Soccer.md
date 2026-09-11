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
<img src="https://cdn4.telesco.pe/file/Mm1QRsHlM6A-W2CyiV4U0RNaha1SWCnq-H4Ys1A5fIadHeRKqNDpDVjeAIwo5nk4ydeo4cxbgjlD8KtKq3tvZcR7Eye-9-aDMfTEqsmZRQazNEiE8uACIcFDjFeSn24OOS818GhOzOWdKPnMb418RKkenDd6pkQBvNKp6bd2E3iTzGAPn8B4sD-LkKGbpHEoTvqmTSkubi8V13x3_tP-BaE6n41U_gV3JAdDsbSY4cgUSqdPmV3QzElN1jTrxPkhkjHXqYPt-rFbcpuJ9CJm-SXu5MWS777BW8pxgMBxlbUfzB6RdC-WxelAjeCN1cyI19-kABnD8GxG8RowLPs7SQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 534K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gU-16LJajKqUzJ2QQgHb9jVqa33w2Pvcvpxs0HE1DBnyrUTSQrRZE-9r2cWqCps-6wLZRYyf6HoWt49sBudEHl64PPvzvGtG0Q1NEwvdX4HsNd-S1te2BqM6afjLu655lobu-EghEvuoHJ_JFLcmtb__Yo79Bjfga592sm1sU6_WtaDNTwsSbi2z9vZK5Bg61ZqQu-ErUy2d5a4naJ0EJOM5b0yUbf2p587wz9dxdqrl00UnkCEsrgIwRGPrjzewmz9YXOycYTmgP6sSyGdUY49PGzZfexHu4NUbgzEOeZfgnDyNvIgiWNtKFYVBX5SkVBwTNn4SDwMCN_NM6oZHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPy33Fsj0bR8V0MqfsAAMGhhCxkDQIAIKe2Y3KMKBpGRH3SkdVVBbEh6myOxxx65ODO6Mw_eiqbFrGg6ERx6bF1QmkydVa7XOEHV_Ct8tJk-OTG1WV1fxG4ZMHShR8vkNSZc35Ym6c64oAmsEU6ynazlipw2jwRImCwop5QKfeDenlvTN8S2zdfEFhwwCBMDSBpuq4sUSJLj6mJX4ZgodfdEnoWjbrll_lt_yjzo9mrKoZP5vIxcDzFH9-9aoyOSzEQCMi0Q5j2ruxcqguRkbvpChchhcP8636cweFU5RX3ASehYdBy6e__IBLh9PTkGub4n_ZamLxTC0C4KQccVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcOqjuaw0ozs_tmLUvj9Gcqkkn5c5X8xU1j1h5n4QKb3NABHVljFA26VfX6R3_skcmtMJjyCRiR8B9wTKr1LZQflvd7Gq3KxfmHjtt9ihxOw9VPcpa-hBmrWGaUy0Shn9dIzx3VALJjSCi0iXynI6_i0xI4F3nZN5fEut1GELItw9jTU3hdDfjcvmsIxUQF4S3eDcmIrh8UUrDyRwDSp2KkP5qEmoEeJ1YFB722TfUSgmTWvltKq_gXUZXujzSZpYYuG6Grc4pvN9mUi3-Ifr-TTLXJG4W-avTmoaA7WA_teZRC1ikDN_cg_q6zP8lIMivC9nHWRCyaIxkhKuklzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHhgE38MKs2fQJabHfAuDehKJ_IVrKqmYGtXi1MtoWepo4SeNeAEPXUckoGLXgI-6SpqLxkiHWo-0ERm8uk_D3hfajFwtJ3eorhdwxHUcQVpLiMir1nMXPwLIXNPOFZHOsroB3dCMAh2B1mMo9KdP_p1YJ5oSY1ejHLqX53RxUjHuzY42XbQJj91Jny0xhF6Wdd72sytvQPPNBohqzIbXrSWD6a2fZHq8FS5Nod2HAxNjTX3PYPgWqMZK4yLwGJ-8LiuwRdNbHi94GLVwvIZ7lRi1Brz4lBJiaunKKYSCR54iPp-dq-TfyAlj2_OWzt3XFC_urAfXfk0P7GCyp-WCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7MqCbQH99GDyI6ANWbprwVRqiR1B5Wxk1eaA3gB4okKHs4fkOWQg-WwtCiqahmAk6Qlg-NHsY0RWzN5Jm_1nGRCp8YPYwJjyEHGpMxfyB831uVUFAjUMOlbnJm1WneKxPU3wUl715eIhZdawdw7AurwAtmRcmWwX7ydlia8ljBBmyc53ah3WFf_YySHfcnaum_HyroNxYpWQykOkQ2dKdHCFBceUEm_eOkldH8OXCo3xvKjIgouMox9wQbTgVrCG2EkzcOVr-8bdngJiCAbtZFbLrU5qxdPHRxbpBXljKN83bFQL8XlC7c8XW_C4fKFZZkZWHRcs5VF0aX9yy3P3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjcUi92iXvt2btCtfPraS1WWDYRAu_i5PyjNjPB34Z3eNrORwRSiH4TgUHstO7AF46vEwMlvRqkW4fU2U4r4YkrkIDuVsHwKS6KjgMJcjOXbxOtnUhDInLCHOKZkDtmLf_74KGV8nYJCYm3mX9WHf4QeQ6GpO_9Mqb5Uy3xGN-qnT6f7QHZrS7qpZK0xxliQ_Dvrnxj8fFmWqkY7qb1Lv9ue50X90QB2AWT0E_8y_9YVLqJ7Dc2Jkc1Aqy61MeCAVwTipFr7Re0xwWzO_8yE3QuAkscLnBkGxT3jhPEs1Q_dLTZ8RqjuhY_yEgIu2f05SIVBttHJGlIxo-L10jF63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lvs-x-meWay4WZsgr27l7C9rgeFAQhzmqFa0CaUcefsK493nfwLRVuV0t3anB5TG4oZUXjqlaCURayNligdt-jlCP0XqgDZaIWOkW7MdmMH8gwnFPuC56SSMOEsLEvAW23roO2SkW-lbjSihY16N6EOzweVedFpoDbmOZqVJiECDqeXjXWlYeht7Du8Yu0yOrub3M_en3iCEaOkz3TXV-8d8B-YOdDU_qI7qKuMEbyzryZcdCs6p_A4C4tf-MAk36PDOnkiz6s1EIgafdKL1Nip1cN3ugRH-ViEYyNvX6SWYztowBpQJBL5Yigo8GxX-vFUX_7gmjw2yFakd-4Fpqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6AzB_UowzcgK0oEmyZ66yDB0O4YbG-jvdxsF2-BQtV1PptY_t0XD1FlcWHNyN1n6HGJrOM6TsDbIGmpwOoPh_-JtQnkjNkiYRZG08LRL-yBl8wgdfpTd4hXQWUyIho8GZiRhl6isViZmgYvd_-smuBZnSQ06Gc-im0bEj1QVeMP70oMXuHcbgGUfRVJuvCer9kODXuSxVbtjiyfeXCDy0pOL8v9FAPoShKvWvZ5fS0tfmdNApvD-RNGCfZR4UmOi8Sid34nfDkpZcGix-r1jjRoXayNnFzlGufU8e1eVZV_qdl4wfdwAQxmyT3Yo-chhw4qmBD_WcemtZ58nRP_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2FfLcRbCmgcTgJBSpfM2lVDua7oXx0MvjDJ1ESLSVbejHkLiK6pJPZ7jcpVvRwMDSBN7Sj5SqUPbchCzR_3175ZkN3V_ytt5LaVTaFG8TYWKZu4nloToZfjoTDQ8npP6f9eY_yIn2BeTd3t1AIQlGnzV_xAf3QQAsjXb1VVJ6Zry6q6EJa7D3taEy-G9akA6qG43jzSM3EOvzLQpw2cbktW_cfETiXV22oAZ0z_LbNZfhXiwLytcPjTP32vgj37kxbw0kgMeXKUDY4I9E5BfGs4Ti8DXsway3yB6hHcbaU4-TT9h5_xLhdFHmPBqXOaw0zJnVtzdttVnEDytVfUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJmGW_SolXxuv5kTIv_Wx2TMeRxKosnIAM6CvyQjGBaSLuiqWjeOeTJavau3iyexVtYWgKOl-COgh0NjkocruJiRbsPQ26RMluyqiQmVTUkkyX-EpzAbdfWAGlzGnZbsutWbL71cQTveXdEckPkVUJ7X3aIJGaeys9gxwX0VEDJTdysEsToGsx9EoIhTynDeKLhpA1kSFN77hlhh7P8bOlBHXQauC-Urnir4beWrq7jl9ALYrlfapsU9JGsaZjIL9zpznsu2pDYOzoMKVmLUrfz6cCK05Jl-9DWyHYKbhepswjrdS1PZvyxg_Va1r9XK_Pg-1m4J-BSl1YW59kwtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9CuWr_6VVkV_sYfAKQ4x0THsWx0JPi0uPfg07RYfAUk6vbMj1GXq3OKF0sDeUj_oJoKxjA0rJ9l2HjCoD3r3nc3wV30-JUZ1P-ki9oEJ1x6fJfPHtMOgcigA16RLJuh4s34AIb6RKBd-9xn7AqkTSb4Tjzr1vUdAyUN1ocIk-z14ll8OlDdoIF8LVAQWZ2JtduAY9ck0j-NzLEssTsSAU8Wh4UcOqczfdravuQrmCwLzfclPJbbpK0YTJXI8sVfQFNY3NTfQxrKrWaB2Pt-wJG-a8ndhd29ZGwWOGpMZWX1pP5kI2WXiGQF3ChcdUV38uC9Jt8MQ0lQZB4FLGsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3wkhJVRbLFLzI33JQ64cIeL2MYywWq2k7dYudYPz2eKHnvdj4jtVE6l7E1-FDQCCqolFb-S3syiQ0j5BdSbYYydajYyHjkWeIYRzfhnTmEoFFsp8RSqKlcfuATRpLqcbXGU8IBcULUEzi_TgJ1EfGPNI6YzbCEpt6CpKJRSJpdUoWq40lFBmOrpLflMlexj4crshR5YWjcqJ_RySCL1-uMIHwWBXXhbJ5xQFnEkjp2zy8f2sf1lacqTaNG8uu_ENnb20H2dfX3b9JTDC-BdrLF1ZBfqvT1rCeV_BVLqp1lh1gpMJ_pxu-cORyY9_Wi9m33XtdchSHBdhw2lyPEdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2CRFjQ7KnUDcDgP9cOsGv3m2Rt3jsPTXKVkJ6F7yrjKuMHZt4hrY_ijH2tio67fT2u30eWsRycuZYpGKEPyJ3h8Ji4a0_cv3GS7mtV_AduyOi_WSfYbNYe5wheW1mzUf3fEvfnJgOz5lz0d5hEMsfqSFHeewUZQ_6luya_2z3JNhdRqwv4yJolp3RidhpiFA-QRzVEYa-sVHwRvIf7lXgcBb1xBFJl27mr7HgJBKnWi6C_UVMef-i0o-wTntiqum-h86_rZvXsstxLAvfGxEPgIHPT696sx8ZDHb6JzxGkv2Krq4qdK-5soizhD8WokATIJvvVisdjYSnA6SU0yeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ30_tlNYP_9wefwghcNfOyrpu98VCCjjqjjBK6zVWJfbm5WXDjjle8ukDEXmV166mTAT3MBURM3bQ1WI1CXsaUuPeEGe9GXM5PFOayId2cYd9JBhl-QI2uZ-uTsItcmxH8p7qWQIc-9EpNP5Ty4SfkFUATOkfxdaEh-rkL29Q0NE1oU3xSQTkOHUS1rFk1q7Fkd6miVuTCXEJSSUzdTxln2eBk-KzYSAmupYWyfraOHqpJ_p518vF00WsB5tcjKND59yLpixBTheubdb088Q9nAYxkR58M8SAYVRcZQwAxWcH5RsNRN65-BgGY3qsGADHTDhQTwESWBDHloMlsjVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=t_b9YfyXXBwxWvYlac64pRM4UUOcR7dI8fBtEBxRnLPxfBzDjhQ03wJtETOvj9PMwqNdfFUAuncYuO6BQy_SbLIx165MrgcLZNV2pF69hNGEP0ACgatr-BazPIs00gOjYrPhO7DG5zNJW5PZnNyNu8MwkNgL46hg08Zgex4kLrmrOxtaqt8YjP4gD7lcdD4wPeMFDMrnPZP2i_QfeoBUEggAxJzlOPOauyC3xTerwhgVMLbB4To8g2GsBwmYFmIl31Saeir1vmU6_k-iMiLVcu9IoRpbdzje-jD3l6_MN6bCo-uDXe5C-7BpC8Q3q9N6YrKyMjdL2_nHXq2R7FMjbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=t_b9YfyXXBwxWvYlac64pRM4UUOcR7dI8fBtEBxRnLPxfBzDjhQ03wJtETOvj9PMwqNdfFUAuncYuO6BQy_SbLIx165MrgcLZNV2pF69hNGEP0ACgatr-BazPIs00gOjYrPhO7DG5zNJW5PZnNyNu8MwkNgL46hg08Zgex4kLrmrOxtaqt8YjP4gD7lcdD4wPeMFDMrnPZP2i_QfeoBUEggAxJzlOPOauyC3xTerwhgVMLbB4To8g2GsBwmYFmIl31Saeir1vmU6_k-iMiLVcu9IoRpbdzje-jD3l6_MN6bCo-uDXe5C-7BpC8Q3q9N6YrKyMjdL2_nHXq2R7FMjbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=izb1RTtewSIevB-eeV_rnhLYpJ8ieqtFs8QBC0SpOxflgoeMV_AxS4mpH2UAkWLkSI6zeM7R6o7I15sOTnLuAgzbXa-BiOk9ri4B_1_ZHmM6Y2OpLJh1qiOGfORPrYk6lJrTSMXYWQVuR1Sn5m2t3bzAnoJJyiQYvuYgrILsMBeiVXZjan8Vvzsmk86Q7Hc4KCLRkGsArE3BoegCFuYE2GO7Hkfw2XfKn7ywNrJepCXG1NFIWRo5y3Fo68INhcy1ZLBgrgG8yEcdW5cF56uZUwqExqr0rVqcma7-SV_CW78NlO5is3y4U6CXWti-7foOzWrMtfc956xSx-2gMJBrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29507">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29507" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=ei5w0t-zUUo-y31fFj_kK984QUx0Cgde6zsdAgNbFMwbFy9OyhnKAzfrUPInCN8UVoV3fmK9m6Yq89kg6jtU80nKyJYPQIjDOSHcEhf81ERo2YFp1reT6pDzOsfWogxCOAlRZTzlhgQC2WxreGKc5CPigJKtSwh8zJzk8vVNgOeS1bkcfI5_SogsgAEpJ4eiY0ZTJzwVJFOugjJAA--KYN0rpA_rWwlNSnv2VLK_ZX8UjcOEvuFqra3vvBPDueLjxeQw9rstB5Id_1iBeZLXMLj2RXpjRyktB1LAni9P2SH3gmU1pbXZktM5Zhd36Q8JkIZOgOwnoqYc5nAUefyphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=bF_45DXNAA5EjUJY60iasuezeGmZd8ek_uRUA0zhsCJAQ2yAcOVvq1YVsbmibmXxb42oO2oWLqRVRYwLd8tsbQCiULoJS_WNiISB4gazUfx_zhVNuheM80Ikc4Xs0O2QPVEYVO1qKnuHIxss1zIi6O30nPpxIHxUiC5ff-jU3gyANX64hY_vmOItgOkO_MMSu6TZ1WNcqaaJetpoBC4cZ0MZhSEuQeh_zludApTJW99I3psTysM6NNWaCZGUJX7metCsyfSawxyiHlNNRow5OXOcpLxv0Yh2clF74ZtFmX9HXH6lQj7bHAinIggVGpIhMg9bYCL4PGk8LsNq8ft_9KEar0vOlmI28rKa1KtkqVj0m5c1DANizTiZ0eG2KjGkJpk-jMk0_2BZqG8cdFHL4IEnVZGrot2JT5VD03Uf-UtlKEnuGLEGOZbANsQSSqu4OrbcnHWUs2opcE0bsGKlk50Btrmf3QtmYH_1YEn6tJ68g5ABkpjFfaTlvAt_RX-wUTmfxrVuCHOiqFmMGcpP7ak37emfaz60adM3iHHJuH-Ws-VGFNabG7DvYc3NzKHGc88TuFjvLC7EeoGBuX2dOsLXn6fVD4IJywIpW4DmTclcNq-7xwhURek2V4c_3OPpXC84_7ejnWUKO4FMbrs_rxOLKKBTczJ6P8kUyv_g6r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=bF_45DXNAA5EjUJY60iasuezeGmZd8ek_uRUA0zhsCJAQ2yAcOVvq1YVsbmibmXxb42oO2oWLqRVRYwLd8tsbQCiULoJS_WNiISB4gazUfx_zhVNuheM80Ikc4Xs0O2QPVEYVO1qKnuHIxss1zIi6O30nPpxIHxUiC5ff-jU3gyANX64hY_vmOItgOkO_MMSu6TZ1WNcqaaJetpoBC4cZ0MZhSEuQeh_zludApTJW99I3psTysM6NNWaCZGUJX7metCsyfSawxyiHlNNRow5OXOcpLxv0Yh2clF74ZtFmX9HXH6lQj7bHAinIggVGpIhMg9bYCL4PGk8LsNq8ft_9KEar0vOlmI28rKa1KtkqVj0m5c1DANizTiZ0eG2KjGkJpk-jMk0_2BZqG8cdFHL4IEnVZGrot2JT5VD03Uf-UtlKEnuGLEGOZbANsQSSqu4OrbcnHWUs2opcE0bsGKlk50Btrmf3QtmYH_1YEn6tJ68g5ABkpjFfaTlvAt_RX-wUTmfxrVuCHOiqFmMGcpP7ak37emfaz60adM3iHHJuH-Ws-VGFNabG7DvYc3NzKHGc88TuFjvLC7EeoGBuX2dOsLXn6fVD4IJywIpW4DmTclcNq-7xwhURek2V4c_3OPpXC84_7ejnWUKO4FMbrs_rxOLKKBTczJ6P8kUyv_g6r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=Lk8xypvZi4DTkiDDhwj_qlkNo7lzOc3gIyQeZzgryYkwiYv1jWytkPggPY970sMcDKbGhtFLvnl2IZtZRNMbDgAeDwY98XvbQPhcnDuqesl_H1Hoao_c0oVGzRJBYKn17A5zuGbRuGZleRWmjDHo81ZVF-y_wbczwD-VAHsEkoYEYFAK-k3QBXncfqBh4XlnYfMWw8fBgtSTZLdiNcc-PdWiZODLR1pGDjbkNii8y4z1ZembkT8hZRjWFx9YCpyl4jFpkZ3MtkCo3xPUk7I1ZcYggvDVg6i1PgJhiuUula89Ev5bojevhkjHGYSPojmJA2tQfFF0PKio9q7sjgY8WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=Lk8xypvZi4DTkiDDhwj_qlkNo7lzOc3gIyQeZzgryYkwiYv1jWytkPggPY970sMcDKbGhtFLvnl2IZtZRNMbDgAeDwY98XvbQPhcnDuqesl_H1Hoao_c0oVGzRJBYKn17A5zuGbRuGZleRWmjDHo81ZVF-y_wbczwD-VAHsEkoYEYFAK-k3QBXncfqBh4XlnYfMWw8fBgtSTZLdiNcc-PdWiZODLR1pGDjbkNii8y4z1ZembkT8hZRjWFx9YCpyl4jFpkZ3MtkCo3xPUk7I1ZcYggvDVg6i1PgJhiuUula89Ev5bojevhkjHGYSPojmJA2tQfFF0PKio9q7sjgY8WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95470742c3.mp4?token=mDQeajxW_DfLK758ChSertkZPZsDgWld2kqgRK-FftU-YWGwSutuzv4gu4ccPnASTbHR290vvQhIto1DeHuPmwFmrqdLldzbvCNayaqp0Yy-Ol74T47pZf5d1iGlQIqahiwB-_CH3PPcHHW7Y7zFruZgA2RobgH_1G6GQCdWf90nv7vaQ1KEMmqdusebXoLWN9zXYGvtC3qUSryiIXmDqhdMmPmWDwGUOppQ4pODw_ziob5e8J0DB0B8NRlN7dUrgdtdBoPnJm0grT5SDTUsGvmLSe9UfCu6rVfMyVRQ6vKeT0Ml79okyZEj4v91xbjozlPEjWbGatZUrPR42981SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇫🇷
درپایان‌بازی‌بایرن؛ خبرنگار از اولیسه میپرسه میگه حالت‌خوبه اولیسه میگه‌نمیدونم، خبرنگار میگه حست‌چیه دوگل خوشکل زدی؟ بازمیگه نمیدونم من همینجوری فقط شوت زدم توپه خودش رفت تو گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29503" target="_blank">📅 09:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgwo1kX9_WIj_NVT4O3rW6Pe81v3YbmDEUD4F5I4LuXXOp0aKtfum7iVJv2XpUccPxx3261TsCkKov2rzpqDMUID3OJ2AwM_v8J-fbsSZt1qIeqONNtLxe_b_UkCdLwIJNjNmoC4InX9qVeWcQ-MUyAASOJujVRZlJvbOTSqEBsLPtXj56bij7gWh_9OMx-wlfkk7xecHwnb-JlzsQOpDgo6YMA-ZdhM_m5NOlJHHibniKlm-tnwnEtDaGDmin9if5UWOJoJfMIDIJs6mHPrprGvdSX3pjXBXu2SOIptAvFyvQppzYQnImK6G1U1AzxtVM0RG0ZT-xnzhvxULprj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=DArD41qI5-mmlyfC2GiMg_z0rXJu5Ib8YvWbiCTrzMaSqE3i6YZfR0Vo-pjmv4vqWB_Z9ukzAMUZ6teBfdBJRxJYDShiJi84jNZyxaWt5HzT71ZYCCOOQOrBbj6xQTAVLMUu0Et91TMIlvr7fBvtoyQjAa4svm_cxhx9qxEAWJ4nac-gVYC8UcpJdPQuAl8S2rMAFIzaAZOAuWjv96RnzjTs_uc94_igezBmOuuuO7xAJRwJUNYwSmTZeZ4-mUCdbKpKpf4XZeR4gWEcItgENtZ8Zc-g2yISWRkzzbdxD6JhtjmdMomJHKLSTlnSWePjrn_NOd0UhNduIjzIiALg4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIpRo1GGEbxOw0oKqgn4vpwSn833-sv_I-eRHe6RLLuro0i1umi62EhBQKabcqPdbP0brgAZRnjz7CTGy7Nzas7ONYX6rEOKWa4IbQ3L03i6W7rrC6KuHes9BgC_BTm3l92OL3xuzJMiExj52YIq27FUf3qPWcon0Ai_jscQdJclHaymvf9JfLUc7DsfV87bRDOQsTNWVJmjLCBjI8_ImLNt_ms3ouunPh0LH4reHRdYR3FO8uABtUZIPCZP_4NGuQaJW3Hzjsoq_keZ5PvONq05lxJwbu15dONOkR81gLSCnfzroFe1NiPvy0f6W8QJbn_mNAswbbLQnFMnvusXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivKrwtlbILpLX1AS8lX_BTiVEni2yuScQiaJ0RXxg8CyZV62LiPCeKnnFWv3LnqHFy927PyFLEKbrpoQU7xmBGj7mC_Dc3q6-PGLO9jGHGK1IqX5P-npLqNVVfJnshueFffYAZRtsqnJpFGBqCn-gPjAVl8dVBX7xlFOkIPd-RqHdG4x5-RtO_aQPWPTB4B_v7WcBYSUxA-iGkYuXfSYnPKSxspiTHsqOoAFFSOhtEcXZef4KkagM1vZmOUL8aDUmv1crEI92CtaEUil7yWWqMSTgFgftrsgs37o75_2-lpBHNkAXEjZa2Ut20EB9N55Xm2Lpt_jmGShoWnOoWO2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFaCNyQKmRpZQRmIjPGZ7yl4myMCf3PBqaAEhvztsAbAi0oYt4dZ0WazxqGmvE3CYVtp0mU3tJp4TAyvXO5jJNZ_7nTKfnwDnnl5IWFuMff42baE20pqbv2wZTGNQL0K6zDpJENgRFI_kY8rnqHg-HyXU-eYOq7z948lFNNfhXM16mr7ZyRW4w1rtJHgwbRKOi2MW1r5UYzKf5iSjfdH8LtBkQW8UtORFSQ7AsY2xscIfwiYOydHTIl8vMgEmBsYblEZTVV9aN-8-dzDE-aCl9k4OpFFSOuS9SrZ7XFhPDcqB8LhBjlVwSZK9vGR-FLuQa0Wi9dmKpn820aLr-ZXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgDveMCsnu9oaZ-hqpPumqVjEVXmBoHvSXgip6Ro9LmV7fV6bGOJSKmNbNsm1mr0flTSB_SKgFTFaFClK9SRbGzjWsy5zJ2xAloL69AdTClC9zzHleKyQBmTAFaC8AwGNLmEZbl7iBWqqUqxnI6m3isZlHK464l3RuXFKNozgCwT8vpr4uHqnPyNdjsPf6Gv4q3wBOf0qUnKUFbQuBn3v7dsBOGsuGLPGu7DbWl5kp25c0grPT-rBhhUMI-40uEn_LOXoe0qThE_gr8X4UszKOnrRWK601mjSUv3L3h2Vyoh_ldUs_IWL9Y2d5J48nCy6C9W2leSFt_xpbHiI8qCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM73zCvRta__xd_Y-HGxaZI64X8q-idC2aCuo-H9kAWM5EqXFlRFifgOBL1xONTfif57vmng_C1lOYlZa06GBJn131z-vzh0CaAmPsPM5elGmVJ0WoVSd7zjmGnNOzhsGWsk5qdsx6NVZq4LGw7zEXB0DF6XY0A5Gt79_OOoKyWoNSCZthRG87zzrc5tyL29wXl7iwj5UZPlC0LAK9eWLC0PD_xmOoxpT-OOiySA-9STUfA6nXvE5ZX4P8MRjGTQVcqZzDJF84dGGp7pf778iZjLzbYixnoQCccxSCH-8L-1HvDlXiN3dHy2gjdjOCV-JOit8ct6GB2c_BDpK9ho7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YrsGg0GD2xrr4xJGhdsSr4wqqm3xFz-rbJUSFzXQ8LCR8Neb59AItwwFMZ-HX6bZ5RGR-Hhz8WxP_prKF30KGWhtv3cAXJxW4B2WX1bgUZg9CD2NxnII9BmVUXhwdC7yETt2fP8Iom2hgrqdtke3p4Gdtn0tZrfLW07CrdI1r9b5XF6lqHy3scDd06ZVB7vP0e2vvlLODudroRZxcivG9O1V_tcf_Y8SmemUJvfGsd3M5SdBY-GHN4U5b9p2nI7AlzVb7k5HJ_Dt0VWIqvOP7dymDfLiUPWv_cclSNhfGDkYVSUkBnejEjc7ETSEEcKdt3hogzLeT22bi53dQ3US8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b2fW9Ih_7AF1fy2L9R6dn1i17R-fbY7RMrtvVilrJktwyedrTLzMOPU81PX85pHZxsK9kvtR2_ZdcDAcbKV7kOQolfSTaPsI2PJ-b5g_Me-y_jd-0BhiqeHE_pEklitsFLgwT7mJKITAM4yLA358BawikTUOmdL_iM87mVeQWWrbipbRpMq1pAC88_upkYy-6_vcdymy71ZNsgnB5SkxbgSwB-28g48cb7adrpg12Sn3ASEBVjeBAzT1qj6lgqFrcGyC0Sl5RAD4rMndjdhQlOEiM2d-7u8uInhtbRPvzcrF5qHpttwtsorSiGcaefGvBhXpBdgVjvqvKPDKqTxlUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29490" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/29489" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtOAa5smF-du9zR1PjO0edAqx0VXnu2o6ZSEVQguP69BhNSYKs0KZcwfqtv5YAucPGkLEAthqY8PwFlq8rBhF6DwzbbwBTH3M0HZvd0LhekU0iL_xfredb8r6VCxf51dQe7qkTGevccxrQZMSPUtzs4Ejs1VeyshtTTDmjjSH-gjjd2uhjH2wyq5jbKp_wS57Kgm4HeIdCXJJvmwWaay1MyOJMiWs2vO__5yC__SzomMjwD2uU8B_zZdVfclSGej18m-GJKNctLimDS6tnvLgOb4Ow3U_qspCdZApSe16ANWIpwOdXXZHLZC_J2qSDwMe4V37s3KrW0DgNGdV_kzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/29488" target="_blank">📅 23:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLH4OQhePi2rb8Hm-3QkLdbXtZmwCgFX2UQbsgGaQRQ-xB6gFlM41qmaeom0CYMQbX7y_-7lrbte_whEKZTk1n1y1S3NnlV3vmJ8TvirlkFMEI_2YR0o9eUnOQd3AeHLdpYwagHta-iHDkxI5Ibe211JclhLMwmSuvz75TKYEdqFBTuguE84Jv8_EysFUo3rWR8-0YtRDMoPAV8hbXeTWR6N20u3T0DcnejGd21yLuQabAoif_sV1DsHLddNx-bJqy1GQr0Ix9X82gyFIQWsIsNGtGRdfuycrhWyg_git8dJNMoENwkSPZ31CsQ1567XNoEXS4eJOQkgOEc190cAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تقابل جذاب دو فوق ستاره سابق تیم ملی برزیل رو؛ فلیپ کوتینیو از نیمار جونیور برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29487" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8AcZdAkWLWZ2h-WCUcW1L2jydAJhn4OOfvjGcDV1H3Y4Mfkg1ele7Pa0I5zX4MvsSZRiASAGVMBkdwFsm2vCv5WRAvMox_K6w7oN8MlP_coJybBeA1pRIRz5Y3VserGDQdzZk7azyCObUhs1Hl6_J8LH4vsI2zR666ORmrDV2uwdWJaNb8WTVedR1gveHkvoMJu-5tGM1QlVHuBGYGzeomOMbPpcgCYjcqMCEJNsQ7gmK9OshtBpEfdvFffRgDcOGSNymiaigqCyctgdD89vN9i0aE6AHcUdHlHz-MIwjreei3mn61mjPglgTOXuKmMUlTxYxA3SPtAO3lF5L7lQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکالمه و پیامک هم گران شد! از فردا ۲۰ شهریور تعرفه بخش قابل‌توجهی از خدمات ارتباطی افزایش پیدا میکند؛ آنهم تا ۴۵ درصد! برای مثال سقف تعرفه هر دقیقه‌تماس تلفن ثابت با موبایل از ۶۲.۵ تومان به ۹۰.۶ تومان رسیده است. عالیه. همینو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29486" target="_blank">📅 23:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAigRvbLHCYSM2LGgwGr0dMhB4JRNsGROAWgEfYlwGMWp8QrrjI6Ly1sx1jUqknQUU3jfxN0Qq8YoQraNutVkPl3h2ZX_sGBaHvRht4pf51Cvh7zDMjNwI8JAt5spfYcN-BdjJAlxGSiGVs_zw8TaZRJq6GzoFS3YucvdMPjqQxiZeZvT5mM1kact7LIYkqOuz34BMLJW_c8GvEx10m2-V-WlGZ-f06PDgqSeWxYSyg6lMKMxkUG1SiYk_F_WPyh7gLzLkDEPvUolm5nJmg82DwFrKdZ2lrdb1Jz_SJ91HKVASuuVHZBPofUSRH9g1hBOfIeMN41oNimGPnzUZr4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29485" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbUxtz-t_Ull1B56eNvdVwsPAXm7ademhkEfamQ0AfODLZbDHbEyIj5sOxwCtf0gGb8XJdZWgQlXgTJe05MX92_Scc4E1iFqsJxSlx2YEDnwHKVFEN30CSallx7Wa-af7v3VfnJPNcaEQrWsElXJ7HQ151p81cVDyTtd3lQb6xR9SNJBQSLqLC7C6I3p3XjvI5zQrw0WCbHZFDkck3B9AQabfGaNVtB-22mMDdorBuxpWLIIsbNUElK0HBkOjy206Oimy7jeZT_hd0NPWFjDGPhutnLiyOOmwq4_3gcaCKu20ODqn8Q_5iKDcKO5-qdjTNku6CvHhql6hOL2sdj2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29484" target="_blank">📅 22:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRQJNrRdDemTp4mp96774UKTjU0XLLt6iY8y43ME_WOOKp6S4UadUKD9H56j08b9m8N02VWhmADLZijqka3U39ThAwkY9q61uYS6ziu3b4PH9CAz21J3dmJ6crHOHnMDBAM4MCXgp1V_cxH46C_jyhafSVeTz21rWpzplh1yerP-yXAwmcgpm3z8LWclSFjOwEZRtvdpfI4Tnw-y8eTiDH6dPZ3TC1l3pkJKrDKU8gv-dL-3bKq1Ni6G-U0h9TFMyh8jAIHHudqEduzd5VL-mDAxqSO8AuizBgoFSrgGgfUnzXDVTCRVaWavIo6Yj6DIw3Hf0NpvgdOkH6CWQZnTQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ شنیده‌های‌ رسانه‌ پرشیانا؛ فرشید سمیعی مدیرعامل‌سابق آبی‌ها درتماس با علی تاجرنیا رئیس هیات‌مدیره‌تیم استقلال‌آمادگی خود رابرای بازگشت به استقلال و پذیرفتن سمت‌مدیرعاملی آبی‌ها اعلام‌ کرده و به تاجرنیا اعلام‌کرده درصورت‌بازگشت تموم مشکلات حقوقی آبی…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/29483" target="_blank">📅 22:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/At9OEt7s-P0mImJFpuvFaJGwdJdrAUA2Nh1x2YuJg5v8apKTMQwC3SuKD0wmQ-XxUWQ6FjBmEPJztPkxrw_oQsg2_uNzrU4djjxHBqxgD8tNeZqnt2gA0_hbUQXz3yV_xDuXou_g1dqa73HRsAoVuBGiOA2ZPvtGhAt9aA4ElU_q1Rjw88qZ4xokJ5gd8IqNRFRD6YcjrC-JZ-h_rgeOP7qIKEGuZUx3NXgoxFmx9LDPXpnvYHlK_DIDmM-zfqxKHVW1Ucjkyuz9PPaH-K0x6a2Lr41itNXgPjnpAWzlk4OU_IyTsdNjnlmAlvOsF_FaP0JmMnbnenJY-ZtKt2b7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ابوالفضل رزاق پور از مدیریت باشگاه فولاد خواسته با انتقال‌اوبه‌باشگاه پرسپولیس در نقل و انتقالات نیم فصل موافقت کنند که گرشاسبی بابت رفتار حرفه‌ای رزاق پور در این پنجره به او قول داده در نیم فصل همکاری میکنه تا این انتقال انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/29482" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFMaoTJJ2XCbN_VWrBs25FRY9lPfVzEm-ATrQ8bFJs3OqIjOx4mNLXQR2PWUN9zYjlX2e8nun3CtvTERdoN36qLD58fuqrRpMfoNYj0_Q-rYqotoZJFj2JmPMFtaPyErDjDB5W6dXkKxzEom-BLEkf_RYY4FCRuy9Lvo20NcrtCeggevfhaWx8J9YKHvdDq7HoiqwF5u2t9QfD9r96NX9Iq1rVApsNcWRo2yae5PQ2REFwk2U884DD0PGEIaBD8LnTfGO8kklY_1z04-l82vp5gootij9BUJsxEdmdzmBS0nahkoSrqoGojNWFMUw6UmakC-zDsmqFdZQu9dpMAnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛ خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/29481" target="_blank">📅 21:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q08bj5VbovLU5G-OVJE8KLAFCWLGygzZtoZz7VGnybHfsnFzE5WVMgmemWDcsHFYJa_lqKa5EVzk24ZaCP9j13OEFk71s86yogNvSP2WLIhBMISeKso859z4Zhq6upoobAdGn3qWm_Sjkc2zYSSLimB4djgZc4RyDHx0ENr-fdFDBcfgu1y8ictuofz5ZzgDOcNCGG-kEMDAg1T8DmPfWWUscp71lYDWMkVX20rZj4XT9v11PhaOMt9PWKjuUnxlyrZI3Ft5BTubbUZzrq71uOREILckUznraeCGAdD3rHPIABUOyjNLwb1dD_SrW2ERR8TgiqS0YtuQnq_PUHol6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29480" target="_blank">📅 21:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-Vv_2eg2jj0Ejpfc5ECv1TM_6keExibmQDe8NC80JWNG059-jXeADnGlfN3m_F1tGkWaTX_OvHOP3asE9MsS7KcDw-Lq9vDnqqYvx2NTrg1Z69dd8yzp_Sc0edmmU-fYpVrVwe6HHqP-MPkjuy0rHMAYd1b5gk0G9gsfSjR9hX6sVLy3mOcTKvzHE1GgdjmmIBqXYg_91NOOmYbSdwNNXwJeY4KkNhYrof9fvOjJVSIsenNXBGxBJpLpFE7a0j8lu8TCiA_U76otuX3lhd0raskXGa1t_8di4Ibw7chg-LXbp6ea9qcyaRXY2jnpLwg8e6AvaBGAghYVeBmORIBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ درحالیکه باشگاه پرسپولیس و کادر فنی اش به شدت به لغو بازی با خیبر معترضه و اصرار به برگزاری‌دیدار برابرخیبر در روزیکشنبه داره تیم خرم‌ آبادی تمرینات خود را پنج روز تعطیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29479" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-piF1Dvh9n6MFRsIkZOM8UU44udIPeN0Ns8XVcWXSiaTHb4dB8_q28T7t8gYgMkQO75zzJqMgz6AQNQRCQ_K6Zcd_L8SQdg5W3zBdTaPUS05LbtPzocuajQF_dBCC5Z3eYpH2iyezIOK7Jb-yos57BLzmCfcVEIbocOo2GzAVbLLcd4LBZD_6nbqrWFrXAIoY5axuioZaxY8_g4MNNG3TK5MxK2WQoDER-LBUGuyXOBFi4txf6svvh9SWg2zDWtap6ULQk7QRszrvvKk7icMXVhY7zHRfm6llgMhfV6KUXHRIxAohX1X8SypoFvWL5i7U4pzm7vhc4-haAskYgYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29478" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alCsuupyHk7DyfIfrlfMNHH2Uhs8ZnFci1-81_zxOF1q2-D02E2Zs0pvfi9UEwKWGZjHqPzjawKGMTu5yVREqb5rHiwcPROytKsE6f7X_v-8makyyYVHsUwGiUt9mt1ALUR1Z_x4MamB1HwpGVgk-qBOEPXOJhDBd36UTPVIk-86A9yWirRdYwV_a4K4x7pmCESCTql_mbQ-HOlkdcqn8tRy8Iud7NzN_44ZaV4QN1pud5AfLWxhlWTi4qrBTpGOWiBkqZk-VP1KPLkIdCwrvoVKXRrKGAX8eKUgTsQNJNoKNQUVjKEWQD2lL-JgQfwL81QCUR7yb0CWDjMz8DfbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇩🇪
بایرن مونیخ
🆚
بودو/گلیمت
🇳🇴
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29477" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKJc9KQS-SRfRa7PcATvlNy0x0jDm8QESgPvYjNYuo1wYYQbUzTsnEOfobL3DBuXtcu82WX3o_KgKR4Q4tDbDx7IsS6NliBRJUuI3xdvj9srOEPGYNAQ1mmfWpoAJPJRlbIXchS2ZN3r4V5J4yIO8WXT_JbNB79dLnqusOZjbp3z7ASUyV4YPtPB9wpv91a7GoCahd7lvqIZvmuJ4IGS1G5WkTRao02IEFr0iHqfGUbWXgYmRpKpuEKUQWQjEkz2SXVtX-eLOihae0YGy9uWOC5iV1ErYDjyafuJsZfy4EvshA7AzTIUTASlp01La6CnKxRmf8LUtRX4x6x_xV3MSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29476" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya43awk1tJb12HXYy-01cngsM4WI33ZeVrLu5bSAfRnztw0uCqCKjctTdF63ZkApPSNHYBvs1DOmUFTOWJA-1XtHOZFPJbJWgKi4LUBev_MAV6Msn9Il3Bj-5hl8X-hnWPpvHt8iVGXCZ2sTFYWVmRyOApCXWZRBywbxB19-bi5t9ipJdTds_P2Se_2zAMTvNUtyJbEYok0cckFLLaVQcG1hbvgLZYRZ_sCMtxjOvK_B5S5c_Gpba4T2z2T7-RUsAJFaq9pglTlerNGcxqvkP7pq3jUhry5qV3t9XVSFDwSQYKIen0V5JvYqkN2WbzA8bHowy1VtOWPD5w1Yn8Bd7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس هیات‌مدیره استقلال: بعد از بازی امشب دوستانه اختلافات رو حل خواهیم کرد. صالح حردانی بازیکن استقلاله اما باید قوانین داخل تیم رو رعایت کنه. او به تمرینات بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29475" target="_blank">📅 21:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cd348634.mp4?token=Rsracwb3ectnY9cBoLysYe0LnTF-cRguq7_f2PVXO3IUtdyxMxWwT0kwv42SbauZnS04xtqtw9i0lCcEBEJOvs08VjyxKObY-jhtcSs64KbmijSCRfhprUekawoqP6Bu3nsLFyrjOA49SGDdfoadqtreP2GADn1SSK8vmALXbN-eGLnIq14zC93LNAPiMjEng7HdZpd2N8sX_7jDynljQiHUzYhn9TZeYPEb9oImLRgekH6aESfmZ1sdFq9DrcCaxffj2H7lPxVJxsK9zcGR8mbzoVJkbAH1BprMdFZR2usX_o-mRLI7v1lnh_6VkCT_-FZl4wA2vrkDsus5ADZn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی در دومین‌بازی‌خود برای الوصل 70 دقیقه فیکس بود و درحالی که تیمش 5 بر 2 تیم خورفکان روشکست داد نه گلی زد نه پاس گلی داد و نمره متوسط 6.7 از فوتموب گرفت. هفته پیش هم دربازی برابر شباب الاهلی نمره 5.9 گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29474" target="_blank">📅 21:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29473">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kuc6kJLety1KXiXxNa7ea4ZQpI41feil3IVjLoHV5Jyb0Nlqfq_vdvpNQLYEAZS5fhT-73T4sCoNjvjDI7O_enZ1LbjHaMcb6OUHuE6pL5gN3eRnSbm0LBLQhxnk9yIdJ4AJQPBmKnay2VhJyPg7Cou_zdqGtG6xRk4Hb0Tz3gAXa67HVR1FpHM1qzTB6M_RQjw39bB-34ttI4hboVzGBbo4F6wKJc0zf0Tk9qjsa3SycBUbC2ETo3mWFtSyyVRyfL3UTs-LkDEZBbcpnBbI5H8Fljxys6BTnv31TOoRF-I5kcQBDkBVYAJNn18iZCCmvw0hUhp0_etfVsbS-P8d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29473" target="_blank">📅 21:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29472">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMq0eNz5Hd2VEos10jY-VkWW_ABvt6NedCRF5Ni5Q3wZUu-GzYnZ5S-I9Zilry_oxuMYYivABWQutWZY7AbWFpzrPwKn8saXef5wmAw-VjVpiM5fh3d71Nllqe2BvsHYuE-Upaa8tXp8iTkCyieVOk5294VBoVGq4PjWwYSn1Mtjfi6WnGLywgBiKY3KLGOuqowt4-tveuXNR_70UsZheett9imqrLCjynfUsrcXcTgInz4gz5PN4p-HJ6lobkQ4Amj8QNqz8F5uQzOREF9k0myepUZu4KV-RFHoT8p7QVEumjotP2gwKZUMoC2g3hcFaa24dyhZrUifARIAt_4tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم لیگ برتر؛ پیروزی سخت و نفس گیر آبی‌ها در قلعه حسن با گلزنی ستاره آلبانیایی؛ آسانی سه‌امتیاز بازی‌خانگی‌روبرای سهراب به ارمغان آورد.
🔵
استقلال
1️⃣
-
0️⃣
پیکان تهران
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29472" target="_blank">📅 20:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29471">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7Ub2vGUWHAUo8rvibK2NXa5S_F7pu4EDYdpkuaqzBtXiqcsEWmExvQFSTbebf01gHq3eeNaNBYqJnzeNu68_HjDt_qzgdnXnvXJefg5Y1MXIT8ZPQPHsM-hiNO8qLdh1E4kLQgk1HUDNwNhxW_aFSbOK0g-RFr0qDZNGfGrwTE-7jMWoeLA3u-1GoDL0bzTCVH96uOgAym28bCDfiRXEHUM7KTev0vNYGv8ZwnAS2ieoXSP6HZIwatNzz-PvwBgHuBVcNVlAt_vJ6GEo6Ks7C3vJGopIaPKziNeo82vZApJ05-W-YE-Zs-iJF6nWe-HwWduz1wcMEkDWFwGPYJLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سومین گل وینگر خارجی آبی‌ها؛ گل اول استقلال به پیکان توسط آسانی از روی نقطه پنالتی دقیقه 76
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29471" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29470">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=gsT7UXEVvT682AR2DAP66ikrIG4ECNKDXQOZVE-Zw9QKNh3Qx2RFJGu1teWX8wIqCtoqjn2YYdqySiER3502R6fCSZfMUneTnGgyzFpQb67nCjeFrTIW3zMyE0bJPRcUnO-m60xnDw7OPyPhqgnuF6k9GYGMYYLAbOmkWAjMQIEOk8q_8aF84vZYABryWPhEp5B2P8SvyG4HoH8v0Y631mb48aQW4C5ZD8tvVB3AwVqXg2BIcDR5iQbYIfiCiThdmBOqypVoaLxiYT5dh7xMWe66cqHmXc9JQLCttoNemcdACvSL4GFzxnMV5uBPsQ-6kgL9l8RJxAavI6dHyJoc4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399d4e43bd.mp4?token=gsT7UXEVvT682AR2DAP66ikrIG4ECNKDXQOZVE-Zw9QKNh3Qx2RFJGu1teWX8wIqCtoqjn2YYdqySiER3502R6fCSZfMUneTnGgyzFpQb67nCjeFrTIW3zMyE0bJPRcUnO-m60xnDw7OPyPhqgnuF6k9GYGMYYLAbOmkWAjMQIEOk8q_8aF84vZYABryWPhEp5B2P8SvyG4HoH8v0Y631mb48aQW4C5ZD8tvVB3AwVqXg2BIcDR5iQbYIfiCiThdmBOqypVoaLxiYT5dh7xMWe66cqHmXc9JQLCttoNemcdACvSL4GFzxnMV5uBPsQ-6kgL9l8RJxAavI6dHyJoc4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29470" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29469">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=pl-WtGAGize0WXrQfbkhPd7pX0jNj111DHmbNgeZoayNs98eb5SInHg5NbWkJrc6hkArWbXP8uPScCc00XEvlM1RSjYPKwqnrnKu0Cb4-mHziWz6k_Vd7bv_LaT-uLRG5PEivJbWAtnJ7EWvZLnJ8IJY2CW5Gz6NLtL9bl3P0UoXj09q8o-W-t2QPMnpnm8XUuZJlgeCgopnoxexRrBThw1p2YvhxVkxekYGZYuDLK8ql2lzPPKhC9UUv6RmTSmDl-zzcNY9Ni_aDD-4pJqxooc1PxucGm9rwsRJoY1mi17--ImXKbuy_40uSbdMCxyMbpuW0xCdZpmd45xA6rVysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6898eb4b.mp4?token=pl-WtGAGize0WXrQfbkhPd7pX0jNj111DHmbNgeZoayNs98eb5SInHg5NbWkJrc6hkArWbXP8uPScCc00XEvlM1RSjYPKwqnrnKu0Cb4-mHziWz6k_Vd7bv_LaT-uLRG5PEivJbWAtnJ7EWvZLnJ8IJY2CW5Gz6NLtL9bl3P0UoXj09q8o-W-t2QPMnpnm8XUuZJlgeCgopnoxexRrBThw1p2YvhxVkxekYGZYuDLK8ql2lzPPKhC9UUv6RmTSmDl-zzcNY9Ni_aDD-4pJqxooc1PxucGm9rwsRJoY1mi17--ImXKbuy_40uSbdMCxyMbpuW0xCdZpmd45xA6rVysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب استقلال برای دیدار مقابل پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29469" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d96077f7.mp4?token=cQKz5xMye2Cio6euvzq6_qmOKKzuizVIXc8JE7QGTkcQwGJ-UEdE8SdFTiOOOv5VFamydgCrpdJICRSvwdAocD04EG2ta8iRqrk_JMcqRf7fbsSR0M47O6W_6gCuzmRgGtmpI6hvbrf5sWK754LUJb19tWC_Dxyf8YRybA-ys4J38y-YQ1TIfFh-UEka9psrbVDL-YBMpc-sY3jNIo59NelQrF0EVRMvS99JEX3kH6iugS5l7-zZQng7Q7P-l0lIHoPk9nGUtnPQTZ-K-ASVYvpltQxZX_6FE3fg38Uc_Gl9s3V2sKeUNB2VNGlxag7fxnMEvUwiHdKJ5p9VPMlx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛ شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29468" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efbaBEPVxqvvnHXqYNNASm7Po3qfj3P7DCngIiOzMTTs-CBK2K45Qh3NPaspyeFv3y6FlBnk8MzWIGFcJWHxgy0_v-oarAcTd_rZztMW5Y7D13hzVGhHehsumwiceMxBuf4awf1SYgbYNxHvyoYM-ClWXhbiR33F2tK1YKIPscZXakTmYTErIA8gLtZENahyDc_3bARU4M4vVizF8qtGZwXtpLBfEzwBBiuET6r9Pv-2wd8RdEXB8fx9ckviXirjj6vTpYCvTRGOtjvF683Usn8SlNu3QI4cE6QnN-OxTurDUlCM5m4LmKp35wM5arOD20R0LvR9R2kYkNoGz-Us0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wr1tUu_98333AryS64Hzs9W98o5J3vUSzS24p0D2kBIM1v9J4XveVmZIHI9s0wU4CBIBdtPFvCBXdNfVGL2NNubtkPjmy4euKR0kQgi9UJ6ens0NbsZcmtBaEi62yTVxqVExVWA-dV_DWfcjh0rtXCdpJue46_wacERvvObLazCK-36m-5hK-1abevLZQB8Ywa5H1ZCL9WcM2t4K77gov09otCpF-DafkZhrmFnxP411cbebN5fVOBOrvmwZIDtpF8cDxFnK6ykoOltZh1IK-QdLDl-70nSkh7Iya1iKy5jkwNW6p0jIX4-HduasIcpU6x6tY9AMTQzQ2BnSWfkRpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29466" target="_blank">📅 20:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdvMzebALwKQGZ-AtzmRDtQkStJ1yIwOrjrJgUaWM2UF-YtS9izbZtMXtJKUu4VrvJMERMT9z2TVBaPKQu6dhDApbswmlVumIJupxYwbSG9tAKUlsX9gB739VPy_tZZ3kkBlgsYZTkkNJIBWr2jQ7n1x4YoXV0_kXP0bGYM51Lg3GaZOwUfvLTmh2ASt55YRshBUOkgfUX6VxkaWlC5T7DjqY1wLqHiODFZFkhHFXMqU80G9W6_FO7RpG4BDRStsAJVZZaSRM4Yml13C0-mgg1sgT6kUDOg3F_aYdPugtU3zgxGdVekY2pI_R9rRqAhwmOE_Oy9anWFacLBT2Bubpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29465" target="_blank">📅 19:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oW8PFYrGaCy3NY2drlxYkx1mVwE1x--KGS5ntWFIX9VhyynyQloG5udIdteIpp30Qnfj-iqkz5O40lG3_m9c-lJ0hYCvPKFUowsNzMAKaKbpJblK8LoYri35xxCYRaiGvW-99VxOhTN85SXRMJe3OQ7zVcqAsXTYjLGD6XsMwDHZbuBrX9JONWtmuNivt2cqPhl8Sh6IEwtfvTySZQrF0c-3lw99mNwaCq9Nj2uJuDv_enRbrXkLl7hcBjtjWNiwQJYXojCgYmsJbpzkYNoFg1GXkeA2ydLf9hzhUTLPxOK4fNJ0Ueocn7A02MSt9zQIv3_XRFyazygNCTl8d-GTzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویو توییت جنجالی وینیسیوس جونیور در سال 2024 به 490 میلیون رسید؛ وینی بعد از اینکه اون سال توپ طلا رو به رودری دادند یه‌توییت‌زد و گفت برای به دست توپ طلا 10 برابر اون سال که با رئال مادرید قهرمان لیگ قهرمانان اروپا شد تلاش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29464" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OklfogxFaOa26Tq6u8ya_KLN6hAkJzj2dvEHseBY1gPz0EIrz2Lwj9yFIEiGz22I4BpbeArEmiLzXoLVvFdTw8CMOzFSndHQ4Qb82-GgRJE0sqQK6-oSaI_mrWWUDPQxuAxYOnN1SDc1A8puz5k7JqIPBof3eeyi0nI-Nvc4JoPiAunQChdlLpKR3wgU5qcmfCXOwnrrjjU4rS3wcfkEFnTCanlUleXKcTSeTBKq0lO4FpKfqWakLaldLtWvncYG83eXw1hjIt9XzhgnDJ7_zt7TXEzzz2fkymacDAn385WLrGf80LbVRWKpl7xtzmKnolZaqY9k-3SWFRJLhIAUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های تیم ملی فوتبال ساحلی ایران در جام‌ملت‌های‌آسیا؛ مسابقات از 28 آبان شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29463" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=cHGIZnqhNkTLBOP9Rq3QIXePPIm938JxPGMUvzI-gk2GAH2fKLYFlbggqLh1wvcQfSlZyHop5dh6be8zGXazmpvxIYQ3Wh79HpSgPPdFz84vx391fhm06czJD6HCPNzXo3n0G42qSCcUkwfWIZzEovYc8uBUM7j2hJAstHIULjUbh7K4UDi71fOVR-GM16xddrs8ByeHscVF5PT5n1xwhveNFxsMyLYKB2Lr0_HWVLfMHNp9_MvIUrvfwFhLSjH7iGNz5CBBYT8lbZ-W4K7ZTT0hDdTufQ37dYyW-AcG963H7NJvqNR3bOBgPmol6wPjPLlASbyO_pnyb9MXSG3yRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf5ffd776.mp4?token=cHGIZnqhNkTLBOP9Rq3QIXePPIm938JxPGMUvzI-gk2GAH2fKLYFlbggqLh1wvcQfSlZyHop5dh6be8zGXazmpvxIYQ3Wh79HpSgPPdFz84vx391fhm06czJD6HCPNzXo3n0G42qSCcUkwfWIZzEovYc8uBUM7j2hJAstHIULjUbh7K4UDi71fOVR-GM16xddrs8ByeHscVF5PT5n1xwhveNFxsMyLYKB2Lr0_HWVLfMHNp9_MvIUrvfwFhLSjH7iGNz5CBBYT8lbZ-W4K7ZTT0hDdTufQ37dYyW-AcG963H7NJvqNR3bOBgPmol6wPjPLlASbyO_pnyb9MXSG3yRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
پاس تونی کروسی هافبک مس به امیر روستایی که این بازیکن قدر این پاس برگ ریزون رو ندونست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29462" target="_blank">📅 19:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=ti459KeMyhxkCKZMSwi2bQZjFYN8kKO2FmgoRXBhBKlWvl0ViEcgnZxURXeRrHTA2yZIfFbcmaK9JMp-_9RBQ2IGiXKYm27lFv9xoUOQ7peXUVefbnvB9eH2szknVqfmgqoILWIQTsJmnAcRHjnUuU72ck0QuSBrTY5jqYUR6R-uRNxvduQjSLywMf0d8tVoVmvyjrl7AoDm7ExEOMUYE1mhxq60V1atQMRrZE7_E0R-MrWflyhEuDxS_oIfweJ2ZcJwmjCaQrdQtV9_SdOa7RNYhQEK8HhO3uE5JH--Bhl82TMJxDQJluMKKrpFV5KuH-DTQAMj0pgaCgZGoGzsfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb94cff9a.mp4?token=ti459KeMyhxkCKZMSwi2bQZjFYN8kKO2FmgoRXBhBKlWvl0ViEcgnZxURXeRrHTA2yZIfFbcmaK9JMp-_9RBQ2IGiXKYm27lFv9xoUOQ7peXUVefbnvB9eH2szknVqfmgqoILWIQTsJmnAcRHjnUuU72ck0QuSBrTY5jqYUR6R-uRNxvduQjSLywMf0d8tVoVmvyjrl7AoDm7ExEOMUYE1mhxq60V1atQMRrZE7_E0R-MrWflyhEuDxS_oIfweJ2ZcJwmjCaQrdQtV9_SdOa7RNYhQEK8HhO3uE5JH--Bhl82TMJxDQJluMKKrpFV5KuH-DTQAMj0pgaCgZGoGzsfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصر پاییزی چهارشنبه از مدرسه برمی‌گردی و تلویزیون رو باز می‌کنی و این شاهکار رو می‌شنوی. یادش بخیر واقعا اون روزها همه چی بهتر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29461" target="_blank">📅 19:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=KuW-gxXfQZVzXeMoixDNTbkmfDqx0xcd4FErLtto3hZ0VdcvecM_kpuqol4Wwc5aKVKAmpDuUDdkiGx7uEjAs2qJrTpX1cBubT2pEnDoOVjxQxYU7O4tvrLBIJa3KPlWf_cUx0FqRyfvMHQhlzN7oW5lkJPtoSDmeadOHBqHIuo0I_KVQ4S5Ax-dTnYFIu8CfXCq6ZW-Rtg4Ylwt4uOrdZsoVLDVSCwXf_WGIknPQX3hMGPLEXWtGV3MNkEGVAJ2vd1wyadddv0Synn5B3H56vRK0xDeNaLkLHc5AeTN_KfYznydsGH3cg3A85RoZXjPBxWWD_4cLnHBb7_FheI-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1961c125.mp4?token=KuW-gxXfQZVzXeMoixDNTbkmfDqx0xcd4FErLtto3hZ0VdcvecM_kpuqol4Wwc5aKVKAmpDuUDdkiGx7uEjAs2qJrTpX1cBubT2pEnDoOVjxQxYU7O4tvrLBIJa3KPlWf_cUx0FqRyfvMHQhlzN7oW5lkJPtoSDmeadOHBqHIuo0I_KVQ4S5Ax-dTnYFIu8CfXCq6ZW-Rtg4Ylwt4uOrdZsoVLDVSCwXf_WGIknPQX3hMGPLEXWtGV3MNkEGVAJ2vd1wyadddv0Synn5B3H56vRK0xDeNaLkLHc5AeTN_KfYznydsGH3cg3A85RoZXjPBxWWD_4cLnHBb7_FheI-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/29460" target="_blank">📅 18:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Hn5TL_eoCCloWDl3f4P8SDf4vX8DHY-2nFqHw-9mVA2VrdBos-VwurDcwbivBwUsWSosZ9xoRe84LOHbs5OL9rGSou-4Lib5AyyYyAgcWCIG9T2wVM08Ea3xYd8NWAWBpg8V8XN4112ku_rNPDNrde0jajZd6eNtKC224PScxhQHVZQYPfTjo1SiIgkv_ognWFiMaZiGqofg_N2dNJLJ-Djxn9vNmu1Ece7Ma_t8ycfCutElmj8vQaKRjKj-vpX7osaLUShzr-jwbpfado3FoJsV9Aa629D93QL94N6WEQcYqcHfj6SNt3toTa5MtiAJ_klU5S6uQjwg5lNte08mtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4f9a05ab.mp4?token=Hn5TL_eoCCloWDl3f4P8SDf4vX8DHY-2nFqHw-9mVA2VrdBos-VwurDcwbivBwUsWSosZ9xoRe84LOHbs5OL9rGSou-4Lib5AyyYyAgcWCIG9T2wVM08Ea3xYd8NWAWBpg8V8XN4112ku_rNPDNrde0jajZd6eNtKC224PScxhQHVZQYPfTjo1SiIgkv_ognWFiMaZiGqofg_N2dNJLJ-Djxn9vNmu1Ece7Ma_t8ycfCutElmj8vQaKRjKj-vpX7osaLUShzr-jwbpfado3FoJsV9Aa629D93QL94N6WEQcYqcHfj6SNt3toTa5MtiAJ_klU5S6uQjwg5lNte08mtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا از نزدیکان مهدی‌قایدی؛باشگاه‌النصر در روزهای گذشته قصد داشته که قرار داد این بازیکن رو تا سال 2029 تمدید کنه که قایدی از طریق مدیر برنامه های ایرانی خود به این درخواست‌پاسخ منفی داده است. قرارداد فعلی قایدی با النصر…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29459" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071cf92014.mp4?token=a4Ont0u32AFyQ62bHYFgY5HZFkfG-H4xWp15kyL4W4F9nrVqOEsuqW73HVMK_QleWMt312Y2QCYg7I1KEFUkNanZ-2Zmvo-wJWAUSJvUmkzgOcfUZ77E3SSRlt72wmoMsvcYLOqcC7jhm5FwUPDEdU2p9zHh2zcxIxYsU8imFxnAk0YIFiG95DPFZ0lR87OS_e67TADSzhnA7olVQ216fxpeNH65ifQIhmUBLwcUM0maslt1dbxzYkEoObc64cHLVvGQ0h3Vg5hoTMSGGG82VGYu_u75felrqvYM6DC1eHKlS-zX7e0-Ie8ow1myxonSQRN-OeTjnntVfS3FFnQyim_HRDvOwLK91CB96KFvgzFHycQGl_5qqFiUox540zhf_RgEzkNX2JDno4LAvAi_aCpREcDlPzzPJzvFybldXlWeo4d4WERcuBYWe6mO1N03FB8Nbqj1Nx0A-6wa0QdyomwyWFDOi_SSAjvyEwFQvSK-WDzhyaaHzP35UIvjGKXLvsFYbXPJ7lhcHGHzwkRuWvXKLOaixQbt8S5kMmkQ_nZhZk6dzh9i5c7crar-OA3yhPwckpZaL4cdedIe5TOF2ZK7KSEwcPr0cStSJ_vBU_RecoFWuVDnSCS5Sj8Uxa0JRvd4Y0lt-5xwKvIWAzpfOYNF-uAVrEcJtK1POvElSu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
👤
ویدیویی‌از آنالیز عملکرد فوق العاده علی علیپور در فصل جدید رقابت‌ها زیر نظر مهدی تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29458" target="_blank">📅 18:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJYbBRonxKEaaA2M7vuO1Dbsn7k9dIrwHs9Ygj74rRwDOrDHefuRkFJAn5-z1sEEKwDnyRfvoNdkpXlfpY_1NVRj7WgmAR_0ya7KoHRs59nHJh5FE6xSpIHnHeF9uqeTR_68kojkVYOPUryFZndasfIC-0rxz7tQEPsnXhdxf1RRyIFYDTV8byWKvPOFElZMrFl-VplQYU7n2byU5GNZKmypdIlLqXMGshLPduABquMy2OoZURmaYLyXbt09jXhGtc05j-IDD_AnK3Au2RZBSzJCRtl7j9cPhj6R-_lB5ocYH3NokP3C68v86J4_mCa2gXLek7XonvuScaZn1QQaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29457" target="_blank">📅 18:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPTJNn5TFov7mzcSbEowJG5roXYkjVCsXhJtDcHWaqOpfyimtjOXkzRLHOgVC9qQ26GSjoRtlIBKRKez4u93Fg9dq7pMo83_7c7Vh2QoI-WIIQ8Fgs9Oeob7JqWwMH2Xt8VeNX0-0_WKbjgJMEFRGwDTU-rnaVB0bcfMkOFft-ntxyNhege35i2TJYjJpX05B5kxfCKyD9ddciqjruptC5FjPeZznBcZmIPLKpC3spHFcq0NwXlXV6gQ5oiNed5LlzvrxeMzpKpZTrKu109R70smrqJF2WsEqkQEctAClCgeR8P0o5ziVjx3UB4PdjU_GI0luMR3aI6NEtgfvDUVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
هفته هفتم لیگ برتر؛ ترکیب استقلال برای دیدار امشب‌مقابل پیکان؛ ساعت 19:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29456" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29455">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f74RI1WL6YdX6PNLaVIHSeraa2-Uc3SMWlwBPI6WGpgVJZP0MCZAA5VThIuih3TAzbVAkD19fyuYjJ_CbJtEiqiVuxMuEnGOfKgqULMvlZXMY7MwDIczZOUdwQHtFPD5WWaZuaW22q1xTcaKQSCZr7f25psU7-EKLwu6W2JB7mf0WOjpRTmojF8OpUvn8CR3X4GJeZ44rHv2Dc2YwzkFO4A-C28VfLA7KrFF1y1Uj_ubgJTPZIHkQHh0Nz-yOGunyP7gUBxxOO9z0b_1zl5txGZXOJC6KoYBbDvsKwivMp_LEZlilWg2tGXAdZJEjqj1g1UcVZ2BRQf1rCaoOvZ8WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29455" target="_blank">📅 18:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29454">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdM8XzXhuSYpJWNfr6ndqha2u3kWCf2WiSgdMf11xMaWXj-dNNsaau6rZzmGAhHoVTjP-K8KtHor8ZSSCXtaoBktxnBiKEVwsUhDvFf4Gv3ot4BD15k79OK2UchylYYNe59BqtcDl7hPXHdCaFSEjlh0sHNYf3mDdAK4HiyyukrSRZeAXlotvzHxwbAjsdm5X4XdhiY4F-OsN4AeyyiY0xa7xzYcE21sLJLyDVUDIgGIUX5AAtCRJPTV5lJ08bpRKY5SR6F2MeKTuMjVBvxr0vxS7aFSpF9fTK0oyqgHRTG2K6oDeHEHC7hoxcuNduVxx0nf-5NjTdJBqluAAiJ4zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
هفته‌هفتم لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدارحساس‌امشب برابر اس. خوزستان؛ ساعت 19:00؛ تا قبل بازی امشب کسی نتونسته به تراکتور جواد نکونام گل بزنه ببینیم امشب چی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29454" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YElRa6ksV8sP_hIojdVBmSqA1AcgRyR9iwvPLZilKc-LGpuvMqQeYX9DDs4jk-bb3fBmyt22_UaQ1Z84RI7U_n8VUqUpBmUNr7_3BVrmy_7cfUD47HfRQMqTkigmPY2rAFqj4yqJi0sMbmPBjhBcZtAHOit1qWru66nXzmNw5lN_O8LDU75Aapt5jL8Fzgc_xKfzC9hrotogy-aaO80ftacPde2otaDr19pC2VZS9gfgK1OFyfQsdYc-sHBsl6ZmgX5hWlsu72AdkmGdQ4arDuXAVTAKGh16fu1JZFqb4oS0pDNT0ibfo12c-_jFIJyUfFUbMbVjihZlNvCi_NBTrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29453" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpkiNfJ8VR8SWfAdechgkdYienfkyEeO3hNgZ8JptXXjG2dLqwVwEa7pSeYrnmPRrWtMDZ8NbebvmtcNR7ChQRwGBPX74tT6zdgU2UctVHsAm1qw_g88TRholMu18nC-EDPZJcjZK3qOAfLOnR_UXf3XUNdiw53nDEsSsKd88TrQ6DUBxaP0RLjBGYF900KQYvf37NDJOpBQIcwJBWWro4mvlWlshU32wagblnyYlGNRFVOjFAR-QrdYW1_b6KAPu0tIQhhvdZuP7XmEY0zxcnrW2tcRzs3zXCbrCf8gzf2Cs9m4GRxd1f2RfiNxCfXBtTux1HSRc7UZOleqPU5pLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29452" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX8hc2zlKkolUd5TmjYtVy0SdE3k0qnB7n_jR2GiVOivtoPg2BUmI3dkVmKzHzFLDPIDc9ovJSwq1Pe65DtKGybNsHMKciwzbiiX_4O5V6Z9exiSaUkbE-wH7G4GBwRGx03og-t2gpgpZNY7yz3fovBlNHQknwWb_yUrPUVUx9BH9uTJmg6nRevfhsOzEv3INkWNp_r78q-hrgixH9P3idqTyz6b89Urx_mqvZXWx_bpljwFBy0Z-BUyqE8kv-40dWDYt3T-NxiAWyK2sGpPg5PuhLMv4_GVxxx6wDgxD0jz2O9_CMfeUrYiCeDyllZNrn4ZdydFDIcUZTFiFrdaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29451" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29450">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=GwUDNyuS0rn18ExZ4AoNj8hP05tZXDYjADb_8vHSuqH0gxSNJTNEMCSDTH-oWXEUHISDfP9kNMjmdxVXE4qEAeS9CPFBqv8U6SWGExmwi2XzqJr6Sphwe4r5SKgtFFRxhzIjBWIEidJ-Mu3KpDSoWFZzzfkobKFegF1LLpGCUkrKhgTKJA1Ggd0QoTcZFwRsX3uwzo09Aurm_9DxLYs8xXypYg-MtLNIEFqQsdD1MXz2uqYPhyESXHkE7IbYN0kiYWxYYxDL4lx_7LC9yWYW9RK1kYtgdSLW22XBNh3F-kdSeOWSzcxKrzYHcy3bAV_W4239uEsQyGSK3W-4dOuubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a53c9dadc.mp4?token=GwUDNyuS0rn18ExZ4AoNj8hP05tZXDYjADb_8vHSuqH0gxSNJTNEMCSDTH-oWXEUHISDfP9kNMjmdxVXE4qEAeS9CPFBqv8U6SWGExmwi2XzqJr6Sphwe4r5SKgtFFRxhzIjBWIEidJ-Mu3KpDSoWFZzzfkobKFegF1LLpGCUkrKhgTKJA1Ggd0QoTcZFwRsX3uwzo09Aurm_9DxLYs8xXypYg-MtLNIEFqQsdD1MXz2uqYPhyESXHkE7IbYN0kiYWxYYxDL4lx_7LC9yWYW9RK1kYtgdSLW22XBNh3F-kdSeOWSzcxKrzYHcy3bAV_W4239uEsQyGSK3W-4dOuubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صفحه‌رسمی اینستاگرام AFC با انتشار این ویدیو و موزیک تولد 32 سالگی مهدی ترابی هافبک مصدوم‌تیم‌تراکتور روتبریک گفت؛ ببینید چه اهنگی براش انتخاب کردند. بیشر بخاطر آهنگه گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29450" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29449">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRxIDFTV2wCJaMLluDz-HF0pXezrypiUT4F-FSyqv6NtBCFS4sERw5xfsVcovyijEjY2b_TT-4wxinl1-p7FPm3ENR3YqDIRHBepYF7jKgFKxJ0Cy2bauQ2GyCqokwJXRQNYvQXkY6GBli74rMM3ObEWXNjV6Nuk7PUnooA9SvybV37vvtm_2Lph0-5FN4rQE6RqJ9V451iaJetBC04SQ2OdTZGs1MyILvBhQP4PodvG5Y7qhZHMrNUhAbjUM2f7KNTnkVH7PHJHFCufBTUNiNqLkkZ2yPRjjAjULmbJkRh1N0vbh8WhhkefqrIki_9BYRbzDXBNy74eYicVmEdnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
قیمت جهانی سری جدید آیفون 18 اعلام شد؛ آیفون 18 تاشو قیمتش حدود 600 میلیون تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29449" target="_blank">📅 16:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29448">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKx1nXOrVt4tiHu8in_ef72Kc6xNfxZ6AyjTRp2Odj6oH3-CVGK-vuYYH8V0_m1cqoYOQ9QSPUQ503CNmBEr-aDjynQLrT5NQQmg0Eb7ujieDwwrwiWxre1yKMiq4vxOGKPRoLdOA0zEChYa5Mtqi9c2uS5sqE75YkKkPA5yoReu_nhUWHlQ9dd_KqSwhRBqPl5ngjJldDF4dpmU2QJMuCcPhhSHSG68DJBoo_7YDmbR0Y0edCPn_46lR-khiWGinBqiopyDAhm1m59xFIG2lIOMhL35RtwgqcocGJNTBElo5hst5B44lYCcAMx5e8AFcwNzi5N5IDZ9jUzDUcQ7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارت‌پروژه‌جدید؛آرام همسرسابق‌سپهر حیدری کاپیتان سابق‌پرسپولیس رامین رضاییان رو فالو کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29448" target="_blank">📅 16:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29447">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPU6mJoJ3SgLkBmUXd48Gt3YyWAEVZABN57bg6wg4gxJzyYVX3oFXlJOfe6gZKNV7h496qdokk9lwsMtNsEfeTXCpqnNJ5VeQQiWm0yJc_td-MVDXffCTr2LBIhatiQYTI_vxwW6_6wdYCk6RjLHMr-bHySBRvN_OZk93VxU30YSdeqoeM9KJmLXj84IAGECT8iGNtk7Y5CiJYCMXFh5iJ-FM197Z_xzDAb1vdEoMII2wg9EVJSesaG450MtPRnvY4FDkcr3l9oG7ExRrUPQccPaNrfdQltfA490D-6tP18Eweh5D4ZQYmyX4QKwi3hkBysyRhuEqUXs8cnAP-ogEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29447" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29446">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECIQfeArggEx2P3yN2XBa245yA5wcst7vtuKgL22vOUXM7da6tbnuqRBMdE-PMPZcaKFI-6B_0mkKqhLAPrUvVaeX0QkHS6-XHvkqxCDBp9gecT_A7eaOzmPQEt0cL1qp9E75CPU7KhTpGeFengDealLLv_Pvw9iTz01tAiF6en5oZve25jVts9adSNFE-Ou4xNKjE_36YluGPuaULXKI-1JmjN5sjQoRL_Ljx6uFCd-xWn3K2bIhfwVk5QbqqMjmHpQDxk7FamcfPgF4IGlLf6AkoNjZhJETDHzPabV6X1AQuPNtV6vGxU4fwNuXHu_Q5Ng47Pz1oKjy_DLPVrK9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
خبرنگارباشگاه‌اینترمیامی هستن که اعتراف کرده بخاطر اخلاق تند رودریگو دی‌پائول جرات نداره در پایان مسابقات این تیم‌ باهاش مصاحبه کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29446" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29445">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YI1NL2-8QdCxRyZ2K8QsXg-fTE6EGyqWgOPAjCH3eoTxeeCQmkX0IOAJN3ZIKMGWmW8mH6qymXkEqZ-Ii3xMCELIzWBFqM8jsSwtbAswQdBzX_jzBJxiRG_weN2AQhGYbxybfs3vppPZjymWPpKAIZMgtbhu-xy6szr6Xh15qSW4I2Lh5-eiedc_eq8HTz4mQ1b1Rt--0SPNvUkpUewDwmmF2sNGgiUKlaFFR5xEu2Uu5XnlHCRshvPyKT7DPyocEEuh4sLIqchTikeqK-oaQqHF2BUPYw103aWwlSHTabASEnIHXPc-sDQIuXoRTtFnyAtDJMK1CmW5SpyAc0CrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29445" target="_blank">📅 16:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29444">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwdASPjohfVEIImpoQoO8AuiSBFhHt29zjKufqeasn4irV3yRbuG5VP47gIkiiBSehHk0QVsNI4H4EpvNHfEuNKczdbUFESr0LjT2Hw_fvacTiZUMbxsxIc1-g1R6TsJ1Jww7RnnOGJqgOJ6ECdkk6lx_qe_sqE8qfOJR_Tle_fIuCGmGAR8WlkI0Nd3qt29eG0mwKiYxz3w-HZQy33tlossjh4PAtGBn1GXoiSD0kp-oFt4vNi5qFQIfyst6CIrUM7Y0r2E3DDxHyfntBqbgNI23XH_qk8axMyncusmTQPorunYOQjtI4SfH0LTh8LmdUMOBagYvcuEVLWxYP4CsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ وکیل‌پایه‌یک‌دادگستری امید عالیشاه؛ با شکایت بازیکن کهنه کار تیم گل گهر از خداداد عزیزی ممکنه سرپرست باشگاه تراکتور 6 ماه‌به‌زندان برود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29444" target="_blank">📅 15:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29443">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afef3ee6a5.mp4?token=Igk89FLcYBIg2fF9NI6H2dDSGLJITrwdrxEpV4C9bBvJ48MHmREfUCBhxYRzytyfZRbW4XjyA1Z8kPCpHRJof3AvmZ7hRECf1Et2Y-6vjlEumZJehtBQMnbCxTxEm_FR-DO4SWfVRGbM65aSUvOol5Hernqut7AXBIRZThaqQlmvuzX4oHWwnLwLAGPxC3mh5bGpIZSRvZjaK8QGo1n5aK2itzUY0luQAtq3bNoR7gffqguwR62qtdPvBscDJ6H8C1Yp6qaQavmuhZnkCGG-1yp2z4d0p9ZpewxCypA0ZgjyTwWziEhOKw2Ql2W7xs6bnIMKcPMe3sFd0kTpWdGBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلایه مهدی مهدوی‌ کیا اسطوره فوتبال ایران و باشگاه پرسپولیس از عادل؛ سرنوشت مسی اردبیلی که در ۹ سالگی وارد برنامه نود شد به کجا رسید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29443" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29442">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOiJ2H9Y5BZ1JknipBy81H9-wXdtK_x8S-JYBK2Z_F8rtowHmoDxVmeyD5G2i7n3VhLeBzynW4YH6VgINJl71f3GUOymZHqppJZBxwyqQd6pNWFKIcLbDgzG41R0HXHDNdhs9CCWnCZ53ugwxMvySQiXxTQj0zwDNZydPJhiXhiXyfObXT4DdDGBfcTeQ4kAQ9Kk86noTVwZl216HssG7tYuURa77PjNjg47BbT9-YdduLWPSvNoktHAffI0U7raQ5eDR9DSlFSGHEEqXuBtz3y1sPV1rd-GPJkric6bOodgfC8DUP_2VWp5-7idNLr0rPRiGaThPRImTzdiJ3_tcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29442" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29441">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeAq3ipklOUbC3oKBTuHTZaqe0GIUmlLzCvTnKb5vFG0IyAVYf05igd-rNijsbObi60Mofq_Gpo3obS6f9r61ccYQIJr0PFNk9G72yjxD2ZwWa4nex-nt9kT22SOnn5nSQqHOcgHAtuS-sqNL_jIQ8yrO0Wg6X51bcqGYHLf5v96B2RumQ3lhTZTZfxsao3G00u7ihGf1_UF8uRASIrtjOTiAFB4KPIih5aykvEBflTEDrE-C08m_0lLCJeMvkdIr9Hy0cx9tSvl5_TxEUtx2wE3Qq1TqCJlEf1XFS7IdalJ1e3KE2EcmrPOt8aVsCDP_678q500wi7bQg3UqIGOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29441" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29440">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8GkscCN3OEYbMcx-tQw-rJG53ERxC8yXqlKxF-2qVms8zmCyCQLPwfp1aZPSkI3Q-gNcUczjJegMUu32oBj7hvJ0SbxtzvyDOECyEAd9U1vmoFHwXX3z7wWtNLvjXVAQE0sOp0WJNyHJZYkHxVorESeoKpxzVEKqscHtL97XDdSSytN86rM4rxSUlN4bJnInLerRZRszBZNcSEYgBzK_BbmovrRgho0s9err9mnhKP9WczMFc6DYdE4S_7rMNxsoIJgEP4fA1xPXUKU_Xy3d336X4EIkSzWEPrr0_wubIl-vCGG-AuSXcCblX-rVRyNdOw-ia077-WOTZrtzlni1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته هفتم لیگ برتر ایران
🇮🇷
استقلال
🆚
پیکان
🇮🇷
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29440" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29439">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvlma7TiUgNWtQEkhyPPgsWTLgKKL603_Ot80dvnxNeohLOQIjvtN8t7lqipg7VssUmMh-7OIMFfHHFBk6T2Jg66LUUkne3qnlmJm_AA38siMmXYFvA7DYDyj0g9oHI75-FsEhg-FbxKs0U4OjG_LGG2IJijEJficwa-qi0xLNQ7f7_x9Nj919RN6NPh8FIM1fLesS7XrziKUU65fGkn3TbDkZliCdGhXoVEF7Hry4wWWXwrEDRuCdsReYpDGNSaUJmckzd8_gJTcDiX6P-p6gtZEBGBzbnSXYlPzUOhFq-kp68ARjgA6m5fxvZbPpB-KZOpEFBWCGQdfEIq8oT-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29439" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29438">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m49YS_9Ty8vd8EfcEW6nPBlgQZnDbBO5TR4ii_idz_HYQqYN6yt0ndBu89zkOR10WF2vFvICVpnnEtwcdd6OUw6wLd-zZBWa8aEg9KK3djHVdgFTcmfUE2UZ0kl2N8wWvo7ULaKReKrH5RgqXlRRi8TaK1l_yl9DvFXilaVOXxvq5raRmHC2GF4u-MusIAJyNvdHtEBEyAHE_LgYDuqb6oHUdqBUYBuKRqvzt1M_79z0-zApY3mXpK69G9TGIy5QotHt0brsMt-jE7RzSaR_QDUql6m-OC7eWCQbiaUH3lPCfvooctNMBEmhpi1emQvRvhRbO5eL8IYSqcouRhRyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس:واقعا موندم چرا بازی برابر خیبر لغو شد. ما چند بار اعلام کردیم هیچ مشکلی برای این مسابقه نداریم اما سازمان لیگ به دلایل نامشخص تصمیم به لغو بازی ما گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29438" target="_blank">📅 14:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29437">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9WtPSrWe67YPlmK2oZ0hr9gT1gcTw4p1pz7_8FnUTVnsXaliWVadFKujDkdpWUrYoJ7M9raYZB3WenB2Wci3MhesF-p3g0VWtRqCBJkl_t2QbDMnHsm576mi1QlJaswwQz07XUSqZPSpBGwzFvRFEM1OYpC5nwKOYpqMyTwHzNutnxGzZmALMxnkRtcN5Cauy3g9CiP4-Tp2Xcxt93J5p6g-YJkG1I0o-uLSaUdJjuuZ-eCAln3Ah-raH_X3-FWJFIIRnbx-Obs9hWfYj1NauYmC67g7Ls2o9UacmThwA6dyy-r8ZyHWUXtXkZ424BZSjwjLfTJ2umA5UB6bkHVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29437" target="_blank">📅 14:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29436">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvY3JHMZKdkuxhVPsByj8VMrsEejqVRMSNUOkVEJ9hjt9LJ4NUlAnbgvmq3QQlQU409XHHU9nbpwBwRYO78Hlk0RbmnL8jbsZBckyF9UgKsfIrsOmvS1g6iWRK3s_KO26WhqUgUOrNOQGalCJh0h1dRiNrkDdlbT8h35QNkoxc6nr_5qQYX36gEccqrEtfbkOdoREePWSrz7-L-JB0iTBq5IrUkpK8rS-sV2skZFTeCU3lwH5H8gMOyOG0DUD7tIDEGCyG_H5PRsHsT0q9DJf7B0TUoCCPCi9yp4m0SwboPrTp963qpGoTUlOqWUbh-Bqk68D8J67DhDw_IE2PSUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛علیرضامحمددستیار مهدی تارتار در پرسپولیس درروزهای‌گذشته‌با فرهان جعفری و محمد قربانی تماس‌های مفصلی داشته و از آن‌ها خواسته به تمام‌پیشنهادات خود پاسخ‌منفی بدهند تا بانک شهر در نیم فصل مقدمات جذب‌این دوبازیکن رو فراهم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29436" target="_blank">📅 14:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29435">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Ah3153MWdv62pi_CW3o0_GvKiAGGjS1UTfpqVcors7hvbbURu4wPc6HI2Y7WH-EzaaKl0iuwIzFC4w8CyEAOQiUhUSP-9iZRM2DhTZcJj7vN_mzdkT72Cbhr71Z9QorCV9kVlQsJhgVYte24AnWt7JEjOK871Zm-o_AMwGD6jvBS_rK4LgdLdk99MH4kbFabsHR99D6CD6J5Q9gROl2lLZF0JvOOQYwmKzWNX8c0ynbQNTFUWaFPXa2tt3vEzxR0Ddvnto6qolUbPsvgeGtndPiGshErRJQPQwbIxRkx40G6A5u99B39Ap3a8NogtJ_YVaT8hZck1KHRx8livwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
بعداز حمله‌شدید هواداران کریس رونالدو؛ دوست‌دختر ژائونوس پیج کریس رونالدو و جورجینا رو در اینستاگرام فالو کرد و برای او کامنت قلب قرمز گذاشت. دوست دختر نوس بعد از اون مصاحبه علیه CR7 توسط فن‌های رونالدو به قتل تهدید شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29435" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29434">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSeOrEfcnhYjgCE25oXa5hp8V3MvMgDv0uiQyfAIjtho7meX0FtumMRSUykvfpGlTLCVB8xhWiy-G_5uaC6trtrh8JzXtl4gOsb93_eLI-C565Lg6HqkMP53I4RuiiEQ9GmPb7HhIs9YXBLDUQCHTWpAvANmGlPA_rs-IsVp5PMt7a45ApDd6CiJlhcRMkH4CY_s9k-6-aiBDjJAO8GwAjhPrwrUTlfkM8wP_azWoTQK6EdUYzhy8zcX4YBViyg98A3q4bxicekekw31psLEDZiRX3oqUZayasiqCcjM4bSlPKpPbbIkmXKROuGv3ldjbwBsgC9lFV_dau4x1LZIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29434" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29433">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs21k2PiGRKLzkVTfem-rNP3ub8wleMvsM2RtXLkibqpkzLrz9wUyPbYcRMzoH-auaomnnk24nNCpkqjIrIOaY_quTtWtaBWvuKDyMgk1wnkAU3Lbif_A-7Tx54GPX8WgRFGoT8V5Z_HvxQ0yj6pa7VlUQ9-ClKX6jggBHWM5iY5OO6EVzzZkRE5wCRl0r4uiku-OunULSGWmfhLL7jp5Bj3ZQfSnO5vv7ou-8yBLP4nxXElqZhlUv4ELs6iN-9ztKXqrSjhcNC_ozypgeiS-h2OYaL52PmANEnnMfvuQz0QqmH7Ph97mM1u-yS64HaOKa97IUxH2i09k9F0-9coDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تاییدشد؛ باشگاه‌پرسپولیس‌ اعلام‌کرد که هیچ گونه درخواستی برای به‌تعویق افتادن مسابقه با خیبر خرم آباد نداشته و این بازی روز یکشنبه برگزارمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29433" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29432">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbNoKtPoWzTaPiWErBv1hAlVVJJPCgFY56dVL_w1PWEmUAY-CeeMI0CAi5Wt4ingHX4y95rl-1buwrjZXT_uv3Vz6l4sPntPV3AEqB7_DDn33B9szV5albu_KkRmPl8v15at9hJUQt8wA1G1H4-yW8QCPfSh-shr65nbs1UJwbIiH7S42eF8atpVYyK_7kdJ4BCbHi5KI33Zhn7w4JyY-D9ZChySYnvT_ubAJY1qxVwjR1XD4BLMds1zhvyVlu17sKbvmrzRPseWNehqQEew4YO8X6l1ETQy9ARo9RTrGWvSWD1e2ysQbcoG_YVf0AOswPP9TH3eLWNA0VqQonmgLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29432" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29431">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kokL146fvdlqkQra7bv0B3cEVJL9U6005eO8McSQYCZ5HDOcicfcONdYJtlmxbk03fdO_UNiD5NXKr2uCfQ_DjwyhV8ObHc5zK3meDr4Ts3odXxJXZ00Nq37Vh_LULyFcR45x8f1s9uMdD5HhYNe_TQC8wZ6gt0L5gcYZgl1iY53CH-ZERi28sQCCUBuqqL_Dgdg5YQ5_LX35sTgYkUa2gn4qRXzLmIG6zHneaNWMOLcTfAfvz52esn8BB5AXrWQm1j6G6b6Xipsfr6Q537UjHSZXisSPdHPkiN5QluUjxLSlHr_ljUrs0olfnIRK2gflg-qwnWxvtPJifWY8BEj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29431" target="_blank">📅 12:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29430">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPO2ujWD-Hok5tKPinmUb8yhrBq7IQAsa7C9nIbqgwyEOwvnNsxKw56MsvULWM-LHTPdL9_SZrhD69INLGq1ozmnkVAHassWMUozOdzXnQqB7UBkfvJTvhsoG5Uv8jI6Yobkw-IDuB4ht26r0D4qsm-VP6zXW2CwRvOOI-Aus2TjNh9YDQZWX5Gf7FYyd9VupmQM9w9DZDE3EXSNfjJoXG6amFCAk4iOVAK3uOZPZigkW3aVQBVUuIE39PwNQbNEF40nu0qsCYls86ZzLufAsG99chDzGqyW9cltpATeJEbiOHcG15pM61mHj7mMjH48BdXwljBvrVwYFDRWRCVyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29430" target="_blank">📅 12:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29429">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=ks2YB6M4-rxLGpV8Aw9GhsxzpeUElo1IXFfJNIHm_-qARgfykDWFABZ9Vm_XoptiTopHXBHrBWvF2EvI5Rt72JAA4VI3v1nqa7cMUuC2Lop_Tbyh-UwhwRJA-xwZ2wfcq5d15LgmRogf-bNA9CUXbhQt2MM5CU1FWBOgegkZ5v8BzKyoT-AaOZKuFFKXV-44kYeM-qaoA8A4nwogazL6fxSZGK_4mjueNnxDQJ83sJI-FeoPxAQ_QYmooil58-pcCyoRXClqj2c8ggVQ928f1Lz2xZ1UFWoCynSELVb-UYUwpyYhaMRXskInnTH-6oy7UCc-8STwQfLdwaSv-3Ub0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f985df7eb6.mp4?token=ks2YB6M4-rxLGpV8Aw9GhsxzpeUElo1IXFfJNIHm_-qARgfykDWFABZ9Vm_XoptiTopHXBHrBWvF2EvI5Rt72JAA4VI3v1nqa7cMUuC2Lop_Tbyh-UwhwRJA-xwZ2wfcq5d15LgmRogf-bNA9CUXbhQt2MM5CU1FWBOgegkZ5v8BzKyoT-AaOZKuFFKXV-44kYeM-qaoA8A4nwogazL6fxSZGK_4mjueNnxDQJ83sJI-FeoPxAQ_QYmooil58-pcCyoRXClqj2c8ggVQ928f1Lz2xZ1UFWoCynSELVb-UYUwpyYhaMRXskInnTH-6oy7UCc-8STwQfLdwaSv-3Ub0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های سه دیدار فوق‌ جذاب امشب رقابت‌های چمپیونز لیگ؛ لیورپول با شاگردان سیمئونه، تک گل دیدار آرسنال و ناپولی و آتش‌بازی شاگردان انریکه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29429" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCXTVIsehlYuDh6s_idX7RdyDZinwILwMc0NzKL7a6ZKYYch2KHy_0ChHEwjDTa9q5xLKvwp-9LrtFdICwCmtJ2HVCxQLdytiuh0j_5ukSejLAisW1vNARr80wKvTi-Uor9rlnWRQB6nxobck1RTNIM4fBC6ouIuLLh_VAFepCmM7Lz5g1sl9FgeFOmnA3DzrbkEi42QdJA03b45tba9wri5jZz5vbDvKH7gmt3aJWJvda2-ArwhG5_-cdR0s_bvasrcIPlwhf3vOxunyhOPvaKx711RrY9wPc2JJ8bMUpINoavUJvzRwzWQGU7B2P6kLjWDFw-3MrnsStSprQQYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJw6NZIdcesB8d5D9dyUlzlM54GMBTn3YXT9XLDbOaZ7-IGJ64KodgNSqbZZk7jKihHJcmerEP1wALU19O5eLd_9I6U_Ox-xEW777QvBi9DG7Qx2rB6F2YFIg8qdkloArIxKmujWdqmHAHYjpik9RgBcDLgrhU65QocmEz-VAuMRzQCqqCcu_fY-Ux2K8gzat0aHaD_fJM1Emd76rYe07YyGBzylUnFT9AFgX7LjyFuzh_dCSB0ysX4PAY6D5qFp46l5toq-s7sxkgGZQGsZ6-NQRkQdSN4C5zFDjOGSGQ0Evn3NeU1sqiE5aDAZABBPi_4TcjbRZJBeJHGJmsd_DQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
🇦🇷
پاس گل دیدنی لیونل مسی به کاسمیرو در بازی بامداد امروز اینترمیامی‌مقابل‌شیکاگو فایر در لیگ MLS؛ بازی با نتیجه یک بر یک به پایان رسید. این423امین‌پاس‌گل دوران حرفه‌ای لئو مسی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29427" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dQX0t6_pjwfmTOnCVbaHPOSz9aZs_kYGjRaidHH8JlK23--lZNuRnTMMUJ_4oiQvuzJnTxe6Hzd1K8ENmRhlwgcrmO5676TdNDOnV2rzokqTaIV3H0gu8kZmvgYxdOEMaWAkMIdtpsMqmTBFLA-ykYZLTmP2FMFBFDEUjFWchAjAYv7CfKfgyqUIsXN91r6M5eJPv4HkDtDj7ZuNJb92liPGz5IrmTpkATlH61pUGT4ZwYmZJqkOYRIcIbbJF0rRiwoqN7FCC03aJ7n_MIoL6lRy_-Y_5nTzetfPH_Wq4UIf2-Ap4cMFmPAEyqhFdvHUNg2Er9gCMwvduZShnv4nSDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b139c692a4.mp4?token=pR--xMYep2KMI54_NYF67L2qSPkS_sWefxM9GC9a7Z45kPZAfgXnMMTtWHKkEppJVJeLNFBKnQel9iRAdPp41qf7QM-cZllCUGxwvVkHak7w_igoD7V5d__uGyFlmQLiNGVq6XH6x8rVmC1tkb-HMbltNQeyaXmkQJJAlI-MHlAMAOIEMO66yBGb0aiyVSoDHZGAoq0kE8ATfhAA7nvEadFL8XRcOmRVmTKwcWJkRMBESvHwD_bwdKU4_rF_ZzqKyE9EugG34veRP7B6VaxBN59hmoqXQ3g6G9IzNo3xV39YSnsFnWgZtLGeMtMp9lxrld3dv0ulgf0I6IZQIV9-dQX0t6_pjwfmTOnCVbaHPOSz9aZs_kYGjRaidHH8JlK23--lZNuRnTMMUJ_4oiQvuzJnTxe6Hzd1K8ENmRhlwgcrmO5676TdNDOnV2rzokqTaIV3H0gu8kZmvgYxdOEMaWAkMIdtpsMqmTBFLA-ykYZLTmP2FMFBFDEUjFWchAjAYv7CfKfgyqUIsXN91r6M5eJPv4HkDtDj7ZuNJb92liPGz5IrmTpkATlH61pUGT4ZwYmZJqkOYRIcIbbJF0rRiwoqN7FCC03aJ7n_MIoL6lRy_-Y_5nTzetfPH_Wq4UIf2-Ap4cMFmPAEyqhFdvHUNg2Er9gCMwvduZShnv4nSDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو جالب از حضور ریما رامین‌فر در جشنواره فیلم ونیز با تیپ و استایلی متفاوت و واکنش نقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29426" target="_blank">📅 12:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29424">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-XLM8BlIO6mBnDLMUzO9hxWVk-zHSD_Z94Pyj2iNyxiXFuk_9Ybz5Ko2xY4YqWA4kgIqlxb0_lOKXaQq-qey8_l88PJjzVuOz_bS7yCwMCwU45SNEmTSKTxC1rqR1RI3yXbI-s1iCfAgNp_Pnem2MNNvZiDUeOaomlsEst8R_ItXq2BK_F8NyG3xu3tHckOUsR9ZZwuKLYmmjo2SLzS_oSNMUMEGOv_ElpUUWMnfavI-AcL63muUWutdtMfUELaQC0VrW_hWYPdnvQhlc_fjaOUrTIwFaMsPjVEKpOOL6s57XZXtcWJgisaCpRSQAUUt8STLIe2RThLxM1Rq7ouow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان: حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29424" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPhO1czPIinwXX3mCSXX0Fq4sg2T3rLCj97f7AR9bEgNEOOxcrv4o1nWHVzRjayRcnEhfeUAuW0IBXY-nO16Vr7wE1caqAEX5kjasOpn_tCV_7XStLHcByDnnK5PuQd04XjCjRyEziYneJyDaWtntsbkewKubGhOmWoHnIFeSLvUAcPTZwSwY6-p-GecuqdjpfmXDwp5vaCps9UOPsZUBUs9TFZ9zsmxe1ggGFALvdLygdABlbWah3Yo7epWabvWsz_oR2iDhFVD0WmXekxz1WepMVKs9J57C7Pw2Kw4KOqkIoK-Rwd210QimWJpRwxounpnhyBbQ0s-mXlAA9kBRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQI4QFnnf1N1XBmhBlDJYn_ZxmcsKB2yp1P72DpR9_ruLeoEwqeFpi6k7FfjLAYUkhLDt3GQCFZ9E46FkzIWkqmzryf_MqDvrtZBjeuHW0HfoljDcZFKcYSlInh60eubP5TNjtxIO6xyv7t-uFUYMEJeLoUEw8hOHjcPX1--e35EcxEJCQzCXbmM5LoYw0mvM9CooAGhsA0IeVTIm0IKIFyZ4GFLVCiLpUMdN4G-dkFYnWFRzsLR_78mYDE_6U34LRq7QDonWCnF_x3Em1KOXO9svYNZNOkXs_fj7guilx-MsFF9cEV1y8XvndKFpBv-EE462OH94v9cN8wj5spfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🇹🇷
روزی‌ روزگاری آردا گولر به‌ این شکل با رونالدو وارد زمین میشد الان دیگه شده فوق ستاره رئال مادرید. رونالدو در مصاحبه اخیر خود گفته آردا پتانسیل این رو داره یه روزی توپ طلای فوتبال جهان رو از آن خود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29422" target="_blank">📅 11:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRzYvnkGz5pyFIdHLZ3U9tTMsmI-vPdukxdziBpastJYCmbXKch0u_ng_yarGJ7nC52lOiorc_5nRc-lPTddb4RdqjzZFvJQp0OHE6A58fcjAJYITKYp5eNo96NMf_IJSOGOeOP6pCbwbOgvawYM1i7XJTGB23DxKYWwVZbVyqSQywKtEZU61pvEkTz0y9leBkanmvuzsXkGC0_rijqI7oYdYpL3gTrQ0DIKIPWyKExA5cjzMNki0HomXTdG_22rrH9FS9RUM151Zn_104UeIsMcNCdJl9gZ4mGpGoyz4KyZLuxd0yYm2vJiV54fSfalTdYwyqdK6nlebU6yWL5AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ترکیب احتمالی استقلال برای دیدار امروز با پیکان:
حبیب‌فرعباسی، روزبه چشمی، آشورماتف، سامان فلاح، حسین گودرزی، سامان تورانیان، امیر محمد رزاقی نیا، اسماعیل قلی زاده، یاسر آسانی، حسین اسلامی و سحر خیزان؛ ساعت 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29421" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=Y7fPsUqRbiNv_7RQAbPuBrd3Bq9X92wsexghMKix59WfRkF6MrouUmZHZtmlHWH4NI8V8Cxa2EBYBZ0pL-MD8e0wnRiieqQGEZ4Qy_A4cXt8y-sy0PYB02vAOJm3_L54Lguusr13ztGTKYQoTcGYdiw51IsAI4Q2zmqnefMHeI6hWlKf96VlNBEOH1KAtNGKYAY529Kv30RBeYVeRK9h301qFWnYaVBMPFaNh5YUSDDktK-UHVxW6GUHAebhRB3U3D2GM9yuW7RKT-nzV-qxC1gxwBySlbSgcyGvlC7JUnGfpWdUMiYw8hCR5Mb-6lPPBZ9JZgluTWtRzHWGuAZ8N7TWxsfOud0Lsh5DINWP76gklDRymuZ5fUbFwR6Ci60pqNu33zwHxuRkepb20Mt6Qf7wkYphpXL_a-tHYkgfX0FxF6fxw2euQnFxNArySIbeSNnH-bsITwWssXevMm9wZHRL4b3G4tyC-gbdgiqCqyPAZK_IR-A2YRRo4q3QeTCWLJHrEiRbs8-jpWg4dQJlVxU5jsM3TKQhQU9ik-CCc-gchZm4m7-vJAxhoHHoV5n4bvpTX_jNBSOOh1ihG363LCZc6yg5fSDXKe8FC8-q0hhtss5DJm331dhkwRmURLYEZ-QW1rOcDFnXU5AOU1wDDQLowODOpObR9jFudUpkXqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d0b23c5d.mp4?token=Y7fPsUqRbiNv_7RQAbPuBrd3Bq9X92wsexghMKix59WfRkF6MrouUmZHZtmlHWH4NI8V8Cxa2EBYBZ0pL-MD8e0wnRiieqQGEZ4Qy_A4cXt8y-sy0PYB02vAOJm3_L54Lguusr13ztGTKYQoTcGYdiw51IsAI4Q2zmqnefMHeI6hWlKf96VlNBEOH1KAtNGKYAY529Kv30RBeYVeRK9h301qFWnYaVBMPFaNh5YUSDDktK-UHVxW6GUHAebhRB3U3D2GM9yuW7RKT-nzV-qxC1gxwBySlbSgcyGvlC7JUnGfpWdUMiYw8hCR5Mb-6lPPBZ9JZgluTWtRzHWGuAZ8N7TWxsfOud0Lsh5DINWP76gklDRymuZ5fUbFwR6Ci60pqNu33zwHxuRkepb20Mt6Qf7wkYphpXL_a-tHYkgfX0FxF6fxw2euQnFxNArySIbeSNnH-bsITwWssXevMm9wZHRL4b3G4tyC-gbdgiqCqyPAZK_IR-A2YRRo4q3QeTCWLJHrEiRbs8-jpWg4dQJlVxU5jsM3TKQhQU9ik-CCc-gchZm4m7-vJAxhoHHoV5n4bvpTX_jNBSOOh1ihG363LCZc6yg5fSDXKe8FC8-q0hhtss5DJm331dhkwRmURLYEZ-QW1rOcDFnXU5AOU1wDDQLowODOpObR9jFudUpkXqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
تقویت فوق العاده باتری آیفون در سری جدید آیفون 18 پرو و آیفون 18 پرومکس. قیمت آیفون 18پرو: 1.199 دلار حدود ۲۸۰ میلیون تومان آیفون 18پرومکس : 1.299 دلار حدود ۳۰۰ میلیون‌تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29420" target="_blank">📅 10:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=md-XfXJaNM4MZKApxAcCB3EF-t0WwFWohi4RL5aHLCJcWJSxjSCs4WNgpT1RobFBPnI0gafHio3TcsZL3UdiJv9PgayZ1wV-R930Qf2jHRTMeFAc-R_tLOFXqBLqst96JTuXerlBqbtsbhDy8XxhbmVgLzRaXdEwhIMv9YPkcnvQCT6mm3Xg-e2p-e4heMAmT0Q5GhFhR1A2cQc_QDULOzpQrfKWqqLjSF4vfnC66RdTgjY5_NIY69xmDCCJwTntk7cBD6AWH7X6R5r_UKg2aMOWsXMCnDVfkK31VEmb_905LmTgZVN9BzyfF3jbDz-on7V18a3Lw9IlofqmCuLrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573430f5b6.mp4?token=md-XfXJaNM4MZKApxAcCB3EF-t0WwFWohi4RL5aHLCJcWJSxjSCs4WNgpT1RobFBPnI0gafHio3TcsZL3UdiJv9PgayZ1wV-R930Qf2jHRTMeFAc-R_tLOFXqBLqst96JTuXerlBqbtsbhDy8XxhbmVgLzRaXdEwhIMv9YPkcnvQCT6mm3Xg-e2p-e4heMAmT0Q5GhFhR1A2cQc_QDULOzpQrfKWqqLjSF4vfnC66RdTgjY5_NIY69xmDCCJwTntk7cBD6AWH7X6R5r_UKg2aMOWsXMCnDVfkK31VEmb_905LmTgZVN9BzyfF3jbDz-on7V18a3Lw9IlofqmCuLrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#فکت؛ برای اولین بار از فصل 2017/18 و بعد از 9 سال، ایران هیچ بازیکنی تو لیگ قهرمانان اروپا و پنج لیگ معتبر و جذاب فوتبال اروپا نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29419" target="_blank">📅 10:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD2QDCT4Uf1W_nwY8qT3BkiRIztog_NvHVbCJzhiaybHDN8kogpQyOo0Sl7bxE-BG3D0tWDYGadAEGBw_lSceBfrKLIfSOH5lgP7dtn9g7huYTUUtfUwBqu6c7jfZRVQa9Q52IeuDzQ_1VEnhDdzYOaj3DpZ1PEGN-nx15i97ak1v70yBAlZADQNfd6LFW0UP77DBMex0vsJdxpfcSQlZfAg5bLaOjYiv73ydbqJlJu8lar8Xd0-vyu0QjN1BLcdEkRjcSq3PW9z9krvYbawg_2O9LcPB-T7-UYcbWAw-R-O1u8eyhctJvyY1yrDQ9jKs6UcWk6LQj7DJ32E3-M63w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر خرم‌آباد ارائه نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29418" target="_blank">📅 10:01 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
