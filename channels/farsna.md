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
<img src="https://cdn4.telesco.pe/file/JI9FzIr-8Vmh9ACDwmBaOWxaVxmjYLmuTwAlJGyk1e4kYnuNgCxPMD628W1I4O12_UklTbV3aXMwllqF5zBuWOqYCxpIGubDK2bIhx-zvX8-3zz0qpyPp3pYuPpvZz10i9WJvLoCI_xPD60XIp2btMaXli7O1T4FY7Ax6HUSkrEw621PvIdDPWM5FqKw81STcUikf3LugpUrD-NYIWtjme7HvZ086pubjhiZhCzaz1CxLGNZqxf9uyoTNLfxVTwZwz6PtpYFHn1tbasOZCq9sETnaa26zhuwp20pcnn0-tLcxNmznlLRlDFd9J9YSCQ4fIYxQMepk0vQnLDSGfY-ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 03:28:51</div>
<hr>

<div class="tg-post" id="msg-439138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نتایج بازی‌های دوستانه ۸ تیم جام جهانی در روز و شب گذشته چه شد؟
🔹
در ادامۀ دیدارهای دوستانۀ تیم‌های حاضر در جام‌جهانی ۲۰۲۶، روز و شب گذشته ۸ تیم حاضر در جام بیست‌وسوم به زمین رفتند.
🔸
ژاپن ۱ بر صفر ایسلند، و سوئیس ۴ بر ۱ اردن را شکست داد.
🔹
جمهوری چک ۲ بر ۱ مقابل کوزوو به پیروزی رسید، و کیپ‌ورد ۳ بر صفر صربستان را برد.
🔸
آلمان ۴ بر صفر فنلاند را شکست داد، و آمریکا ۳ بر ۲ مقابل سنگال به پیروزی رسید.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/farsna/439138" target="_blank">📅 03:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439137">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZiv11GVPRg2aIG7qoF2GnwuBqEEy1cPxwt5O8sDFx18nfwEJOCRIYG5qTq5K4ZR43TAN4quw_gQjz0tD-p6n7dbJeCg-qqK8KY4o6ITPf6M1Gd1BNAi27aUYE64E5ToN02ambn6wmcQBsIuCzr3Wa3sKVx8zqNetykDmkZHGSDBHN_mdT6V4VW87wLb_rD7xU4gsG9rxBS3q-4hl4hdPqdyg1NQRUEkTfkx5_gHC3T57IOWVQeNWRNcatrwfAbECR4hDcxtwp2EL1mRONBwX3YDk-X-_dGcpvRP9uGqmfc-gFl4flERpxnWE_7N8gZHw3Unyw4sxXKc1Wjho-PZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحۀ اینستاگرام کاخ‌سفید در دورۀ اوباما هک شد
🔹
به‌گزارش راشا تودی، در جریان این حملۀ سایبری، علاوه بر انتشار تصاویری از حاج‌قاسم سلیمانی، پیامی با مضمون «کاخ‌سفید تحت کنترل شیعیان است» در این صفحه منتشر شده است.
🔹
هنوز مقام‌های آمریکایی دربارۀ جزئیات این هک و عاملان احتمالی این حملۀ سایبری اظهار نظر رسمی نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/439137" target="_blank">📅 02:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMabA1JW-UZh0QRL1fWyNodlsQi8YswufYd5tK7Bn1a9DYpln68iytLwHR0nGHioQXeaPBTIsOV_htqJASj9K4X0UPXeyLdCW8J8aTs0dY4szn6UGnTRlf__G5o_Jik5NQK7rrzzL6Mqh8iYnltgSVgZ7v0CzgFfs3iBq2Gejg6VbIrz7ffMNYSWEq7cozc20ulJJqRQwvnwQWNgVYM4uu24Mck9247ibwHExtsv4ire-ZJd9OaPhxtj0_A2kKpcMpCLWG_JmMqMbxY78I__aLFtTmlwrQCFf7MK1K7qSV8otH0GD9oDygDS33jP2eSg0zJ7EfCcOw3JJODsh0beOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سپاهان استعفا کرد؟
🔹
سکوت مدیران و مسئولان باشگاه سپاهان دربارۀ خبرهای صادرنشدن مجوز حرفه‌ای باشگاه سپاهان، شایعۀ استعفای مدیرعامل این باشگاه را پررنگ کرد.
🔹
علاوه‌برآن، منوچهر نیکفر مدیرعامل سپاهان نیز نسبت به شایعۀ استعفایش از مدیریت باشگاه واکنشی نشان نداد، تا باز هم شایعۀ استعفای او تقویت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/farsna/439136" target="_blank">📅 02:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6e4d90c2.mp4?token=GQmPUIQnqdQaa59tKEcAmARx9TXflHC8lPWLi9kyADM3cMmjFD-czPZUWbS3sarNnFi2cuyisebYaY4lt01RmB38qCV26pB-8jexwZw4Wbdq9bXj70__iK1g7QBSnw5w82TPDxGrIuORRIXgh1hiK6EUoR2g_XZWi0SNl3H9ytvW5OUPuEEi3nlshhishj9BRJkIrB8s8vyMVB3A3z9irfDgKDSG0YfeouibKOhOMCIg3gT3QngVI6I8vKNJ19Eu_YZtDohpjaFtZjFPoDffQmdDpcu_YPksOg6GDqLB46_XJzkWaJo3GzSQ2UCthPRwW0x_5j_vXAP4ev3oDLZegw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6e4d90c2.mp4?token=GQmPUIQnqdQaa59tKEcAmARx9TXflHC8lPWLi9kyADM3cMmjFD-czPZUWbS3sarNnFi2cuyisebYaY4lt01RmB38qCV26pB-8jexwZw4Wbdq9bXj70__iK1g7QBSnw5w82TPDxGrIuORRIXgh1hiK6EUoR2g_XZWi0SNl3H9ytvW5OUPuEEi3nlshhishj9BRJkIrB8s8vyMVB3A3z9irfDgKDSG0YfeouibKOhOMCIg3gT3QngVI6I8vKNJ19Eu_YZtDohpjaFtZjFPoDffQmdDpcu_YPksOg6GDqLB46_XJzkWaJo3GzSQ2UCthPRwW0x_5j_vXAP4ev3oDLZegw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی مردم تهران در میدان انقلاب
🔸
تو این روزا که جنگ اقتصادِ
🔸
کمک به هموطن خودش جهادِ
@Farsna</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/farsna/439135" target="_blank">📅 02:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439128">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8EAQvXewNUoK74PxQaBfoNsLdIbREQsQ6EFkk_FXzdxHv9WjAv72Sp-QSNcfg_8gYh86kMWD7lNhJNNx6lPvVF-aidXWJd4UEspigkXSTJhwoF6MIVKec27w_NO_16sFpszaesZtkbPwfao3AM75hWa2VtxGL_lgSwQGiF81tWCtwfu2o2N2itad2YplMqejnov6ZZBrDdzzAgyXJ4JIpEL3Ob6iQT3c2PL8tHtWSruoLjRDNKWUkrNalmho32rbHNCgI7UhVtPoM_GNAFNX7Zm0A3Ms29KEm7jv2x-i02ba4ak7s_JjffKtZ1Vs37Z5dEWtqhCgGB6fAYUGtqBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJy8O13KNrtJMhFyuXWTgZQ9hWWjUQjCEKTf7QYWOh_IN4tlhQ752p4BwbHieUBVkxghmxmGj1Hy2Ax3-Md8JEuRbH7APU2PQ-5b06KXvd5Xbhmmr3C6YVcm5GiSNBNPQzSHNpyDAnjAz1VJk_QmKtrCDD8vE-gwVinXIUgLZ5EdTTUIH4XRC2Lj_IFv4eFR_3pohvm1KGHDbbpZUbOHk9ts6jeXV4A5q4mHlPGJZ6PSuYJZXa4U9KxL1fRM3c98bh-MeZAr7ven6NQ_6FlWtJnMrG9i4j5jYUtc6t5zHd3CdpVosqh-2euhkSEsYNJ2NWw0FSJhrbwPKDDipbrXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKywJq373xNS5lt0wzyjEPjInIs-3x7Y6k92yeleDRvi7Z7nVyB9vK4wVpArQviowDcL7V62wi-7f-D67ax0sl4cxtp1h5OReMys1wqWv87hSKftlCIlmAbQGDU4_A5H_tXE19e6XQ_5tbmJID9TEmx9PqQhT6AoIj2dux18zP01OHIvFv1xzjNQkbfwb9MFaajkIgPy6OdlWEIs85_qQmiXdL594SJol9lTc7HsHJURApxuXnIzBaZhL0YKHG6gJN5XVCJNqqs3InsBb2AcCaf2paBYVV2opQSy5MAZSRZ5vAlUhSDngNejRa8y9WIrUAUg9NCkryQ-KW660Bl5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhK75Q5Y2jaoHWJmdjfgW8-tP5t0rcSUWHHPhnKhxhPUdxXFmXLBUMrZMHDXcgSGnaRCiQDSbiDMkyDNfMmWgm3J-YGBa9_vDvruuYG4XeMPZNsRxXaa4tMMf3hLl9NqyP4apkTtuZG7P06aIhTujZzH1nugGJ2B948JIW9-2JK2qLDjs1KUs3OaowVEKIFyDWEb6g71Vv1MWhIUl60EMGbLCdEwPffT97ONdSRResEqhzRoImiglBpNgRcHTamrR-CJAhvpa7CoFyCvDwQXYPSpb7ggeN9EEj3YRsVudA2J-cH1Z_kdPbhAiiEN0wXJdLudB5Md02SgtyNoGnz3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcuy5eBTZRbh6vUw_WmkKkLZaG92Vv0zlnAhUq9fa1-_xT_Rtj7AxBJenh-RBfiG2rf3v-KNUTRCN4lAW1TXRE5JSCS8t_yQR7XLQb_DZvc5moNOZyuOJyBN5KbjLcHWUe62CSM-01hc540j3ix_ONXwPGXIQ9RHFkUfiMCZnkhpD-IjJrXiV3fV13F24yzME-LfDdcRt0MYiY2UJgRdS4WSgQuCPM56RcE15kLmpkvZGqEeJDwKUAsMnMI5TC2Knu43Ano3Y05ULsVkBDSeaBk2A5GwIEUO6gEYgnDT9z8f_1-j6iIb-iHow1y7KPd5mGIDvARV1VTvLbL4Fwb4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsHjNXAHvJ8vZxI49NHLbaop0zUgRWvq4BlP_R9njumKjhKoYoTFw5OS4OkbB9KoWhGAajuZN9i45pGqOp0ASW47eyTEhjaVkfNW7s4-3Pel-gusmblOgr9_VLssezTuxSOEd1s55_D4IgaS7ebdS5WPR28GgOaydl_SwNW3nvcQMzpFltXgJOKJ0NlXPQBY2idj_tbwwQIwozXqNtfTwohJ0jb8WSpmG35uFztVdi8GjNH6J8mOFbkd8e8w7GZujqgi77JL5kc1JrjOgCSqpk3tCJltdKx88xCV9fyYpCXcJYJW2_OMDMyHsDG0XZBeX0Ou78-gYpOUoFUUoZGCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_a1Ky3O03GU77ViIsylNZlUXLOASzbcbBch0Xsqcr0UST1MD2wQWKNDnjpUgDfQqfaW4Bpgv9hUSsk2fpwF36XZY93xdu4mo9LeXH9UuW1SAz5S1K3RXTOz-Ny48qdUVthgsd2CNCqa8qhGd-zu6QMgcEaxqdkf8m2Rn5_tyOs0JHkwdRLq_KMzq10TJ8zzEDaHO9-9nSI2cFdaJc890_QvAXIV_DUYLovH0iqglYlsLEm7HmqIbuBIuMXrmr9UzJnSsgKGPsjoKxOG_1NuT4S7MORquPXQIEajBgfVSOktNez5ZETEG8tAgM6aD7OBXJ6hqcDOp66nKa5VgTcFgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اختتامیه جشنواره «قهرمان ایران»
عکس:
صادق نیک گستر
@farsimages</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/439128" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOXCfk7tZYo1zNCzAeYEc5sCDR_UUElqB4wzU4-5zxo9kMOX0aMOG0tWTSP2Qc43lqxi_i5342mpiG1Ba5eLWivIbZHXB2M4gd3oDqlQowgQ-wtxLCHtnone1PsyQDE0VL_6NNxVTahVh9suOFot0fMEPh9iUvh46ABLiIsJdhBHWNkM1EdBd2e2yPcZ9UwsCNaCAulYTekY8VzpIzuEgH0sTCojf6oQz1EpoBWHvzlW3Bt7XdIpcza8L5r2PMSaN5rEd9lgRaWym3yVylwfT13hu3gZsKAA9d6Vn5lmhb5J9I01kLRLdQkmfRKj2-iA9ikdXg829R3FTmVgSVaHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMTU56kzgi-sp39MXECUSVpYtGrYl3-sHO-DydksMjj25DIYZ8-Slf07IFjb41t-6x0G5HgJym8V7f7Xlq8Y1pQ2KVdU43GMgfz2qN4ex3UsYGM5KWRFLeRfP7hMRRmhr9yYHBXWGzPqCLUf1QVGFtgs7ef35ZWOH0kGPt_qLvXo6XYSH6z30G66WVU1qRiECQaXtSK4RXltLwltVGxZ6bGZi_xpxIMRgSOOVYp1mxyc7pvuMPLTggHGmSwhhQrDmueDXMDwsclUh-lcu_84yo3uzpmn4DcCU_C1vSMxkfo2_lCyue21ZnDmZSQeP8ILz89U2_PkrjIh7mwDlGbQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eP_KGLiNFoaA1QlvfsXButNDLHHbuuNBlRMTdSD-0PBAVfrtxsHDM56739IdRxrDhmU9YKPFtiqOqh5NKuoSm08cSvwFKTitBOzocRjewnmVly4EEtZWFwXzGF1GKCe0filBbERSVig6ueVc20rU9kq-6NPj583BCgu_ta9edYjad3Xsc3jAwkPMLC_ksT5ZNMcs99Ks6xXj37dDPAD5PqakCm02rHj74Ug6nYzwmgg8T0iyFQi86vZH2nNpCaRSyH7AW_GomsIOvD-HDwDQ1GYHm2tY6XETlwluir9f9cxSHVHNFfsnlwDsFgJSC2oFtW71HbdQuRPhQPjvrIEPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTIMHZm3pp0ppOg8pSTYWvFHUAdACsUxMNobBsfNRu_GTWNETqdmqwACx821P-4t6bx4Kq5-vyGoXEBtSAWQpoAwJYG__UIqKXehv61L30JraD9cu9bRlrZQDZvlmvScdEdwo-83hQOgl52XUl7638OLd8_s6XydnNrhAlCLepFQ69nJyfYPOBp4n67kol8U0R-CSPqbLF-PutORUE-kKEaAELti-q2SQiYjEX9n-DPeoLiypRF8mTPMZ_ROKTlCxxud1EepxiahK1WMGHTYjq5qgtMMPLKngyrDceNAI7hhBuv3dKBmL2stDcFcpknePnEQXvKaLaEABBQOqCn7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdNUbq3WO_q-hQ-6OGDmJdQcYWG8VXGBBXciW92fnRYfCQYxdVd9V3wkBTh6UaM1L0KazFCGq8Q7sORmE7bRbzgGkxsnLMbUZraDV3mXLwNc-kXXtR8wHR4BHdgozRH-8FoxC4CSEsGvkgNH5bQBWO6Pi9XMRJW1Tqb8rvYHUMtMTAyWP8wRWLKFKfrgheWdIKDbCd_gcpiTi7P3YypfHkglyiyQvHCuQWjkyuiIMd0SZwMxoDeKFETHc2Q7kme2vPFjP7coEBF5Gu3DOlkCfxHH0Wrf1y9dQMrfFZfm7AXEALhgW_ye3J2LhVM0-MTAjSRE5RohNAFc0X0aq4_yMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxgfQAAyFU7kP7-8pF02FJc1phpmhz-xTLLTofv2-8WLMh0STMXXq2gtoiz9OJH7dGH_qmXdvSlXlkOEMW0iupQTldHGVGA9fLRuM9wbAYyyzdnLyrQ39aNM7-DCEHOtgTUBG_8Xhm1Qijep5CD851ngTLzXgQF7HEM6IYszCi4j1gViwV80o4NMxt7QujM625v7TbPxRPrzZuMzvV9Sx8u1Xu4sAb0eXQ_erYOwPvYWbuwMOxCnWMupsKItbJYJ4tCpKm9mu8DPnLvGDBCsCP4FszETYH5XLNFzVVsBo_GZRUoxW1giTldRVGwYqJ7cBzbjViH5IOCqeRtJx2f-dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۱ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/439122" target="_blank">📅 01:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad5z34Z1pTxpOQwaoc5gdlLy3QxTl2wlvT9QksSLezUV6JjWy_MzwVMOL1DbAQiGRUYUIKSBqSI1reZ-NUH7IhfggyEnax1x4gH0QBW7RcHCtDpkAxDUfM32VNNfu2UspdT_q8rjUU4i-kXuaE1sezyX2Pt6aZcH_aSgUMSg5YxAvKYenQXffGNdaCKBLISTE5JQ8HzTqXET_ynBbYB9Qn2ydvMzlrNV9jFxwsMM-p_j4SlYu-5_-n2NBErCJCtKD09e2Prw_D98gBM_rr56LzfxIq9LYniLxtEIPZo1Xx7VlfoVWKeiGB3TXNgFWf04yY9MjW9pH_l1L3es32sC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3mf3eHD66y060AlU-uLD1G-3T1Ir97kBRBgD4KTg-8bl7KCE-_sb1A2CSWat9hA1TKpRi1pAgnPV_GFSeVw6s6mLfqRH2MqL-e2fg0VICMQp_a16HkskpVyNmeFiwZN00UOwu1otWRgaJwEMHXP1kdQMv3Jku-LDxy-y9Y4PzHOCe9lCt9pAoyPaELZ1UOLCaUo6FXcXD1J-fNuqQ09Rv5nXZXP14EKj96vgC6FvbM3mrN3j_Fj88FouyRgQ1YFdHTPgfhil_dhXLT0C9Ir7HY0s7oLOv2o-QHuN2PSsWdRNPIFyFuDjG0qJLO3AT1k8DrqD3S-DvfdJ7tGTVuO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kjn9PBYwU2SE2i6Mv77pXp6aUZ58MYRMtFViMVikDDktK_Q_5D6YNAIjOlB0EK0UL0YqQk-vuAFnJNSfR3G0bloeCawnc7komEBbZH6M2DnzRhFPNEMvms6tfmv2ygoS5F_fhF3KmjFJVvTwo-_Jbr2wAsgztkDv-OHtYnTxqH81R6Y-V86SU6hg7jcS4l-ocutMEpTMtU_rK1h_AtrZBLft2_LgYeH7vPwVRXta6hVUg5Dp6Gk-VFJbNnpGLHYycHPk73AaWegJygYTjQ2w8MEa3MhJ0nRyB2Ywyz-sNsRE9PXsg_S1tLK1F1EquOm7AkXJjAuB_le9G1iIHJ9wfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrpqI8RJF3keW90XbTaL1k1LIrNaBGEDARFWH22U7s5LTffFP4SecHHHmnKZESV9FQyGx7xAEvuVkGFKaQQWU5gAv93cMNDqAj2bV2ZGyn1lQJq1oLT6MYnmwxU23aKxC5fdTH6zaMlNl5iUaRWTYrzRuJN__Z0YMTNd09k7sl3k_QqOsWB1T1JX_uQ02z6nAP_xbBJZTEecIx-ImVapWBywuVqXwe4shYNzdJT4UiHs7XDSYbZie26pwJD7Xlg5oLbnVt8vqcO8g5WbGijuuOv1RqZ8Vj7C6SLQkKN12Vsj7mpstvPTVDrhpRRy-qN4ZhbC2f3Yb9R2RCapvWDu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbDTAExNTNdq2Zt9rJCaL7mmI_QOp_Y3ETjZ3UkwPQ51_ELw-Egx4yNVBM3DIRrnbpOnmIuu7NSCjZZV1E6_NkrZwF-yAkHN0hVUYb-l69ord443oz0Mf5R3GgUA1aIYQ3oIG_eFA1Wx3equbvrdIQgjd-C5FPQVHpIHAXXjhPKGqPHSBJs0Db66EeorVTAqZZ2Ty_d9y-9ZLSWDxTROSp82PLfMRxr7BxP14EJd1xxyibDsHU_wjcXzgWee783Xo-sCK1jrpamzfNuuzr_nhXRe7AYv8HMOjKRBaeBAt6KbDpExlb_B-QOru_UNj-Btb6s9p0iKxvyud07KT44kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB_KLhf-RpN6YxZPgT_6FjOfSIN89-IjLQypPtsoVV-tl9q7-Jpgv_C3swmHesoWd2ReYvLpd8PPOt_ahejCresEyE8jp_38Z6hidyiz80XjxZ990FYrWduVYT3otns6SOmmH0o3KOTi5JDNUOmZwpNoPUjnLXlVWjq6HDDQcYjgySQDhpLt2tgV-Ht3vW8fkB6T0d7YICne0QzZ6WOP9e5ZEWdsqdbXR5KbrRcQAPGWYFGY0UGXoYAmLsjl826mKlrmxDm0jCxSs7fbLsnbvX5qQ54Eyx0I8yzUeH0Rq453IAlCyd4K7m1tyrB_fqcDe9Jp1EZMgEOG43QnPdCxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIODA63B6unorVKJ-LeaEYh01dqU2Yo-D5uWb8QUYWz68RUsScvaxfCx6dCYZPa4Yac-RCGLNUgwUO70C4M598kJrn2aLV9NywcC-wMVzk_nF4H9OaqtLJUpQSjf7xgN30h4NKYUYzUYvSwEoSJ2m4r72EBXPHTnKAnU-RfjyMtj7tAdz_ZF3MAMe7VRZQdqDUBv_CbbD_w77W3uDClZ1gaj_ByHK2wKJufB8awR-86Nd5wnDaHhhAMTz2eu4EDNYs7OsUtGyoOCZQXyRbczJBITfHmasrRNXu0-IgSd67qci-wDfawGXfzZeilsbEPuYLQTHNhVp6BWqysY-uRhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYesyr0F-igKGVnEW7GoKXollmJQB0Kod9n4BJUZtyLgfj1Md2xe9yjqzGnPN3eCs3iitKFt6FWrvTWYgcIp4XcCB12Pjq4OqY-HBpUSCVC42pRTK4zvoXzwQVIoxsHy6nFXFPD6Rtmbj0KoDzjljtlp9l5u3pHeyujoOvUEknk7RJI_1CZYECh9wPvRFyVO1tZsTUyUsAAZE6-VUFDLordPz89uJGUhGGc5zDdwJiZCq_TlGl5eL-wx5urYHThHC8E9o7zzLzAdQ4baxZpkvRbJLrdCBnxyMzXqdzQNrD-YpbUIWXxCMpbsBXWy_-JC_yiWGOHv3q7Ya9rdTRmfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wq6zoMqg8n5hbGKn5ZMfOyB4T4VPlUbKmrqtCmZGTp2gCtw13TECiG0_55y_KtVmoK4i57HDJoxJC4A12NLGpfVeRpxLYKd970pk1-s9UxdyDYCGnVyP7PRuEP3J5BGKHaJDeZjvPC9nFQfrjZsLsVs_NJhRZ8J98V_wABXW6bEoyVe9hs7O7kWTSzmT3CM6OhAN9qNfuJUjJW8--7JC-dxV-ra8i5IVV-Pg16IpeG-zGYr7NJNjXT81KRKvPqC31VNtEaAW15sIht4d4EVCOi1mOU2xnipA6pewQeSMXGK-GENauntnujfsxcj-g3hZ909zqS-sGygJUxiKjhjgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWBGsiR_Ee10SvJWqdUCsDJP6iCACpFCB9JNfa_JlrJyCZXxdxwcIZQpAyW1UVJ0QAckiDAKIif1KD02EAqKeHPESuXEEpdyWiFZwoPYaj2Ife0PY_rWGmX3Mx0tV80_fJPJGJGkNndio9pc95T_oSjLwtvKUnfj0C2PDlBqkdddz391r0z1hdXqzdQRL0VSnXo7jXfm2xgb9MhNiFK29aL6aKca5J5sZgDzsR5Hq0-dlAX--k0p4NyoRXRmPdp_MHEqskl7EVZfXkcTIXoVPjPZoR_kNtCxo3_itRzqzH4ftAGRrKJvTmXcivqEc-iNN1NmI1RiiDWZVNbDs6T0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/439112" target="_blank">📅 01:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj2r0u6mukWCmpBU0H6d7akrKk5FPo4gNFQUveuPocJEHI3NfsV8q0PFaOYOtdOCJf00qLIvz1W2lpOwQEno_Nl5IsVt0IUFycHocw8Ek1o6dQjBqaFENAnjUu3EnbB-768hCievuCi9AF4CwaJxN6dSUozd1Lqy0XD_1WCGeHgeqxKt_gF2-l8obYatamKE30HBWTDPpM8_ew9g5RY_wEjhYHb2DiLe9E1czAAQQtdXE0Qa7AECXD7CpVmOFMX2u9bVGGOoLh3Rwwha95AMvTL7ImP01H7V0Qd3rUEkVi6zF-AD_QcF_qoh5RenYhR1BmT3a9dwsUI4wJU_5_O-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آزمون‌ساز شاد» پولی از کار درآمد
🔹
در حالی آموزش‌وپرورش اولویت برگزاری امتحانات را سامانۀ شاد اعلام کرده، که آزمون‌ساز شاد بسته‌هایی با نرخ‌های متفاوت ارائه می‌دهد.
🔹
از بستۀ ۵۰۰ آزمون ۷۴۹ هزار تومانی، تا بستۀ ۳ هزار آزمون ۳ میلیون تومانی در آزمون‌ساز شاد به فروش می‌رسد.
🔸
در صفحۀ اصلی، آزمون‌ساز شاد به‌عنوان «مرجع رسمی آموزش‌وپرورش برای آزمون آنلاین مدارس» معرفی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/439111" target="_blank">📅 01:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdRKXo_Y5f7iVemsMyONKWZykB8sxaycGnYDeUnHZITqeFmrTvFf5jtSGMU9ZRm2gGhg_sxM7hJbOBzBLuu7kNvlpJ63pHoCSnaK8oT5t4OVkcAMrFpNu7zYimWeNnUSiJMb8fGD7rRV8mqMw3uXk3J_OXkOsCPWU4XyGhiTHBDXJPG7W0WgtEa1Da0qKyIWL8PuYbrqyj-WUN9x9HeoiT6HboPO2TEeOn5ab3StRQa4MCXMosP_GxLANV6lEPbAKCj9utaTlieTJ1fjA2juafysNvJqBG3yc5nbMCUOzG0KM2Jp8DeLx6BY7Qr0xOGUIx4vHfy4jyNlxCPUPDSYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست باز ایران برای دریافت عوارض محیط‌زیستی در تنگهٔ هرمز
🔹
رئیس مرکز بین‌الملل سازمان حفاظت محیط‌زیست: دریافت عوارض محیط‌زیستی از کشتی‌های عبوری تنگه هرمز دارای مبنای حقوقی در حقوق بین‌الملل دریاهاست و می‌تواند برای جبران خسارت‌های واردشده به محیط‌زیست خلیج فارس هزینه شود.
🔹
آلودگی‌های نفتی، فعالیت ناوگان نظامی خارجی و خسارت به زیست‌بوم‌های حساس خلیج فارس و جزایر منطقه، ضرورت تأمین منابع برای احیای محیط‌زیست را دوچندان کرده است.
🔹
در نظام «عبور بی‌ضرر» کشور‌های مجاور تنگه می‌توانند برای خدمات دریانوردی و جبران خسارت‌های ناشی از نقض مقررات، هزینه و عوارض دریافت کنند و این موضوع در حقوق بین‌الملل سابقه دارد.
🔹
ادعای غیرقانونی بودن دریافت عوارض محیط‌زیستی از کشتی‌های عبوری، مبنای حقوقی ندارد و این اقدام می‌تواند در چارچوب قواعد شناخته‌شده بین‌المللی انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/439110" target="_blank">📅 01:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۸ شهید و ۱۹ زخمی در حملات هوایی اسرائیل به جنوب لبنان
🔹
وزارت بهداشت لبنان اعلام کرد، در پی حملۀ هوایی اسرائیل به شهر دیر زهرانی در جنوب این کشور، دست‌کم ۸ نفر شهید و ۱۹ نفر زخمی شدند.
🔸
منابع خبری شامگاه یک‌شنبه از حملات هوایی جنگنده‌های اسرائیلی به جنوب لبنان خبر داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/439109" target="_blank">📅 00:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AePzS7f4Vj3xERiIuxnWrFOK6c0c1EltS7My4UZjCsbuwWDYzwRtj6VtmTkNWYhlLeVivzEvzmfK-y4LAH3MlX39ruZU2lnqi2kzrclNq9Slp05kdX2BmtmkNkD85YBR2R_piqtvgZwh3gwsfFZgF06wRj-xArqALSYVCGCXvaRylP5xGKJ1aaarvNvDTY3pB3sK0-V7svfnMgYsB6G6Ehc02SbgHhZEmedvlvL_CctoglVS4Wsb9FeKsNz0Gq04yxzlUkhGdKVOkGktTOVjanY1ST7cKKdkWmCq3RrfAQYBGOR4HwGUg_jNrK4NknXBziErAM8mwut1rGoSQbJfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔞
رفتار وحشیانهٔ پلیس هلند با یک پناهجوی باردار
🔹
انتشار تصاویر برخورد خشن پلیس هلند با یک زن باردار در مرکز پناهجویان شهر «زایست» موجی از خشم و انتقاد را در این کشور برانگیخته است.
🔹
در تصاویر منتشرشده، یک مأمور پلیس این زن باردار را با خشونت به زمین می‌اندازد…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/439108" target="_blank">📅 00:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFz4DBNd6MEtL05XmSIhaRtDfCH8XsFQvtWAgQlLho6uwfMHEWtCYhT2tqvBLWCbnWwSdJulb-sHfLnGBDkpjRTXgZLnma8362Jbmasi5t-NeO062_3L15zdNRiJF6J7U9MGFA2bLh17ZDht6M3F1smlJlLEO2a9mrju7xXi-Wfto2UTXc-VfT1yWYyUGtQpRVKJY-mBd7yK2PcJGazbSfXsFsg81t-knIA7wjE2vjtut_YMQHEgfcf4EPZ96wvpDFIG5tB3e5D0Fws7xWZ6rBb7JdgtTbE_gj2izWMZseGQHE3hvMapwv9z2TWYJGG70icZ5lQUYh9806agjHmISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معمای سهمیۀ آسیایی ایران؛ پرسپولیس جایگزین سپاهان می‌شود؟
🔹
در شرایطی که سپاهان تا این لحظه نتوانسته مجوز آسیایی را بگیرد، باشگاه‌هایی مانند پرسپولیس، گل‌گهر سیرجان و چادرملو امیدوار هستند به رقابت‌های آسیایی فصل آینده راه پیدا کنند.
🔹
مسئولان باشگاه پرسپولیس در روزهای اخیر رایزنی‌ها و مکاتبات مختلفی را برای بررسی این موضوع انجام داده و امیدوارند در صورت حذف سپاهان، شانس حضور در آسیا را به‌دست بیاورند.
🔹
اما قوانین موجود دربارۀ نحوۀ جایگزینی تیم محروم شده در چنین شرایطی شفافیت کاملی ندارد و همین موضوع باعث ایجاد تفسیرهای مختلف شده است.
🔸
برخی معتقدند تیم بعدی جدول باید جایگزین شود، و برخی دیگر بر این باورند که باتوجه به عدم برگزاری جام‌حذفی، تصمیم‌گیری نهایی دراین‌خصوص برعهدۀ فدراسیون فوتبال خواهد بود.
🔹
باتوجه‌به سکوت مقررات در این زمینه، به نظر می‌رسد نقش فدراسیون در تعیین نمایندۀ سوم ایران برای حضور در مسابقات آسیایی بسیار تعیین‌کننده خواهد بود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/439107" target="_blank">📅 00:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فعال‌شدن آژیر خطر در اراضی اشغالی
🔹
فرماندهی جبهۀ داخلی اسرائیل: آژیر هشدار در جلیله‌علیا پس‌از پرتاب موشک از لبنان به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/439106" target="_blank">📅 00:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c385a45a.mp4?token=RgKZ7bum21SrnYq62WxCfX-lqTNAvB8uZM9oeZf9r1cn5a_pKpoM9nQaIdht5RP22cbUMY2gxgDhjlcHXThmYcKXoDLYrh4I8sj2Jyx9pilLNKfojIuYV0BoG7I5qpf7uzPf9W_qki5vTzDKhLsR2oPJTnbuwJUQir8NQIPEUcNBYsJjdUttSanlzA7CYNHvaqmK_wFxq2wPYuNQJeXhE6v8pfLysa8uJhxZwmbzrVCHpp1eXSoimAhPrPywaDkuvn1WnOWYr14-f2Kb09pXdTjx3nuKbWawYjsQPOCc_piGn6obrLMkWd3Hhpa9KKuqLrSx78-az1ATMrDUq6f8HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c385a45a.mp4?token=RgKZ7bum21SrnYq62WxCfX-lqTNAvB8uZM9oeZf9r1cn5a_pKpoM9nQaIdht5RP22cbUMY2gxgDhjlcHXThmYcKXoDLYrh4I8sj2Jyx9pilLNKfojIuYV0BoG7I5qpf7uzPf9W_qki5vTzDKhLsR2oPJTnbuwJUQir8NQIPEUcNBYsJjdUttSanlzA7CYNHvaqmK_wFxq2wPYuNQJeXhE6v8pfLysa8uJhxZwmbzrVCHpp1eXSoimAhPrPywaDkuvn1WnOWYr14-f2Kb09pXdTjx3nuKbWawYjsQPOCc_piGn6obrLMkWd3Hhpa9KKuqLrSx78-az1ATMrDUq6f8HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: مسئول میزبانی ما فیفا است، نه آمریکا. با صحبت‌هایی که با مسئولان فیفا انجام دادیم صدور ویزای آمریکا برای ملی‌پوشان ایران مشکلی ندارد. میزبان مسابقات برای صدور ویزا به ملی‌پوشان تعهد داده است. امیدوارم فیفا مسئولیتش را انجام دهد.
@Sportfars</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/439105" target="_blank">📅 00:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qleJuGusO-7Q5qjXXGoQDxu3cTZVKw2IvSLQ1PSiFNzUdSr9-ADHLRHMn_xFl5pdV5HxY1k6OsOglvA-V6o1jNdiSRYgW1ROnL7lbnE3IRApv8Vdw1cioeh6llTej3yNJrFGwAuISTM1SZdDnXKQXDbJcbxnMYbKOv7COjN_v4_Ic3KgqdOLNhZcnMGT52Idt0zvMtNwVx89HIogb4cdLRMwPNJdmgLYun58RZ3IeWSsHfEysoKZ7q_PqfOPBrTtigU3i60Bj87cYeg7vxAgTyoDudO1tGr2RKU2jEQO6HEq6m7ldBT092zcQowpy33LaFutc63RK92RTAGd_4i8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرد شکسته‌پا و کاغذ
🔹
پای مردی شکسته بود و در خانه استراحت می‌کرد. هرکس به عیادتش می‌آمد، از علت حادثه، چگونگی اتفاق و روند درمان می‌پرسید و او مجبور بود بارها و بارها یک داستان تکراری را برای همگان بازگو کند.
🔹
سرانجام مرد از پاسخ به این سوالات تکراری و بی‌شمار خسته و کلافه شد. پس کاغذ و قلمی برداشت، شرح کامل ماجرای شکستن پایش را روی آن نوشت و بالای سرش روی دیوار چسباند.
🔹
از آن پس، هرگاه عیادت‌کننده‌ای وارد می‌شد و می‌پرسید: «پایت چگونه شکست؟»، مرد با دست به دیوار اشاره می‌کرد و می‌گفت: «شرح قصه بر دیوار مکتوب است؛ همان‌جا را بخوانید!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/439104" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439097">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpQKJ_yJT8ye4Q-GIWi7vfdmLhNB9kG-77PA-pv2CThXSbEZtAnswxCtHCpW_w7cYfshHI6gBg4F3gZsXq5XfQesD2k2BnMhVBiJSO-jhVupHPPVLxM9YYAcZGqcTEV5PRcFhtoYkvu3Iom-3qRFSJ5FkMyZDwY8JfWKr41IHpwmHzsZRMO6UpwpkmjcDxxfsYbqPjt8KjX5xv_AWq6rQ3Mye7LZf9at86Qq6hIGKgqBXily04bRWkKVgwmXrsxqVhh1sHNH9dWZokkebBhbZmWXx0KoaWZhWCC7UYNUXXEi3-2CnBUcpaf_DbRW9jbL3WEuSoQXn48fPENywrLsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWFMhQF_xecPcBSm-tb4NRAwj9hGWHO4blSgcWbOQEn_-5sciLsVIcMvUwf-DhFh7TO10cCinrr7xWDSb9aHbajSd8eXxOvM8z8mIvqZdgZkTVCX3RmiUzVLG42x9YoNKNZome-C-0UGNgHSB7_P8oflBzso51_7NGXN4JNS6_BUTZVoLZZZwxW0Yfp19vZmlQeqHDg2OJawQEwvEJmBZfpLMOkOzAL4iqcbNlg6KyWMiujfFdaPQE-RTM79ARazSjZnca-nJ2pna8deRZbMlFS3DlwDhr0Jcj2OrSLGIDkIqQNL9ibJJ_B27WaHdoD_toAcSfCw66FzalLY22TRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqiKsGfSMNforDVkyFJNnoaPsJ4txBh40Ykr9bUMtlgs94JfiKmWg4Prb5QrTinEIKRNKyNq7RMvrSDN7nVowLNplRzlO-jQboo0f8dQcZmSadfSlWpJcbeq7V7ZdyNuBhvcD5FLK5K8dr7KEDof3TeQHSC5C1klhFm_dO2WurFG2mLK6VCT7S1xv8RuGUDELbIRvcy8spikMFIFtJigbxAsYerqVApNQ7dtS8dyrMZboYtY6HJY830WoFmBIEy7lCNA9PugwpkoARZSKaXpnPLAQjaygrTxg9_oobj-plsCjlvSqWFO5y5mOnZABqKs-H5dPVG_bKpw9ankq78dYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCINTFo5c0rg-q8cA6ljJSZAIekj01lOv4KuRIZHYppgY-31Xg1TZynBybBIHWMY7xTeBmqj8RgTC9x59kSrFEO24q4L04Kw32z5P1Hvb_9k2rA7QBFYPDKTuONTKwdPFG8kWnpMbc2ls-v6E7WX3ixnq-u1HyHqkf5vmIvLkldMLTtnIKp8d6mXGM8Sq5nrOnK1GGjpRcB75Kq2jd48Pxa3pv0DfeeCjpCpUsauBrmDyjKiMKJz_AO12IZXjlohFbOWQPaNBl_HV1Zo87bi3jeCriD9uUkC_hLTZV0dmu4Mke63pygzwp0SYcqk9vdHNRrfgvy57zpxUivmabMaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEtCfDlyGNJoZ1YIetHLEggWafm3OMrWC3zgSL-1wN1OYdcT2beXPHU4KPHnbUKOsZjhacbJtReW598jaKc64STVVnWveb513DTNZqtB5qXQcWl6G4hiI72FsYOLC25wSAfdJFN7J8HdtOmhLUUDQIW7GECFIed7HMSsVSLWFvdSZXMjquS2mYli13R_HGORTbcWlJ09xlQQVTMrd95DvS2KnRMi7JJTdyAoYksoXqfn8ra0Z90TGANDUIUDGPmbacvRtZOZ8phVxsa8FyaKwaZMYqP0O9S3_GLeVAkoQZCwTFJO6jL_xpLl_BfH9br0uMBFTGp0yq-fWy9jRO5okw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYkGlMm3bVd6AWcvwd93nU9mJDnUUa5vtqxT_7Ah0vddaJxy3z-bA-rdZC8SABzZb6AIGcg_Cws7x5Cot_f2FjS52jCLLdjKd3rLuV9Ns3uHmvQV88d8u91APu8x3mqWEE13yiYboEY24zUIcmRitbjOwGfmqj0_2yHPUbViwMVzGLCqD5MBOEc_XxwHiJsrQUNsv4uVGQrX0YebrZrv2BgvsG8TYM-CDw7Tz8u_3YUpoFc6PF6oes1Ev2UPsWr0PNSUTZgVLBjBoHiFvzo-zm5QQOSOT3W8Zow-9Gq-DyFCuplj-0PuEGlNR0gFTwdJ2oKVaRz-RIzeImKC7KUxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q192qZnlX2_x6jqVzTkd8-VZNOa9C6ImZv1_-vYDZvVcc0rCXOsei-1m6WfmzsuJJJwwUXODivS2SEJ91dcBb9jJMIQ11YRYEe3Qd4iiHUASshMuvdVcy9KhDiHiz-BIORxLTf7pce8ytIMfOj4riRwAdKBfGNmCsOtgaDMLbrZoOEHiFCbuQ1kX250Kb7sKPVvmvvlObHi4Z3WzTpEsL5CEmkBI4WcjTXQv_frsForBmm5egjmlmUc-xKsIeXkCUTVP6-llPrS2SOExHvn0ODrnt6KcQwMOpODplwbVfC6NI4bTYR6lqRKDHGdVepkkrO_Ru7mCwcpKXhlrbN1mfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت فرماندهان شهید سپاه در بندرعباس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/439097" target="_blank">📅 23:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439095">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada0223afb.mp4?token=JLGu-QfnQiTY04P1AeKvaV6p0VjrkmGB2iqsh5KTqF9wL4ax2yl-bfqAWvESexw4Ut82aJQNk6SMCRw7nVHnus4GpjlznWm0KvVuZa56XGUtDW09Wy4N0XK7su1t4RsUaPCdK9oDfJAawV0xnLw2TPVoEODtIxibNtjxs64V2HtMW85eWK93UGlgkoVac2Uj1tKOCrP_1mxduj3kto826Ot-_WkDt0eNpmfOIgyN3xELZs11tXVXgsk8rWqaeSx5OiCDfiVGIB4DbTWjcXXroAoO0A7eG3_CAFYQXwO46AznETvx41JkmgZzIYZ_prBPGzGkZJJVgxQ-PtgcO9Bj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada0223afb.mp4?token=JLGu-QfnQiTY04P1AeKvaV6p0VjrkmGB2iqsh5KTqF9wL4ax2yl-bfqAWvESexw4Ut82aJQNk6SMCRw7nVHnus4GpjlznWm0KvVuZa56XGUtDW09Wy4N0XK7su1t4RsUaPCdK9oDfJAawV0xnLw2TPVoEODtIxibNtjxs64V2HtMW85eWK93UGlgkoVac2Uj1tKOCrP_1mxduj3kto826Ot-_WkDt0eNpmfOIgyN3xELZs11tXVXgsk8rWqaeSx5OiCDfiVGIB4DbTWjcXXroAoO0A7eG3_CAFYQXwO46AznETvx41JkmgZzIYZ_prBPGzGkZJJVgxQ-PtgcO9Bj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ بجنوردی‌ها به ایستگاه ۹۲ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439095" target="_blank">📅 23:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439094">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a31e292e4.mp4?token=PUCRirAM5da2KIPAfRBOtJ4DJ9y1TE4g_AtGFQjq2GQVGhUI6MFYlvjDbUJjNG9UeCM4X5PxwZ2E_T5mHKH-mRkBWIlXbmjppB9nJFMj3t4ai_I29UsIz6gofJudrMobdYG4g5lOR-veSjZOCGu54MB3dzmo8Z79hdnS6h-Yz2it0KeV3neKliQqkq9HXclydhtIqMbKFQSTd4c-NpVoy6LP27KL3f6Id-vS_3KpgNcmLkl2ajBivVjDRQIsCiIwRduzNRD3msw98EF4CBrOn-vFo-DL0vTx9vlExYzuOLCQyvNPI-_tX_PBN6rlm57wL0zFHsSFTqcBEf_kK56q4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a31e292e4.mp4?token=PUCRirAM5da2KIPAfRBOtJ4DJ9y1TE4g_AtGFQjq2GQVGhUI6MFYlvjDbUJjNG9UeCM4X5PxwZ2E_T5mHKH-mRkBWIlXbmjppB9nJFMj3t4ai_I29UsIz6gofJudrMobdYG4g5lOR-veSjZOCGu54MB3dzmo8Z79hdnS6h-Yz2it0KeV3neKliQqkq9HXclydhtIqMbKFQSTd4c-NpVoy6LP27KL3f6Id-vS_3KpgNcmLkl2ajBivVjDRQIsCiIwRduzNRD3msw98EF4CBrOn-vFo-DL0vTx9vlExYzuOLCQyvNPI-_tX_PBN6rlm57wL0zFHsSFTqcBEf_kK56q4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این عاقبت بی‌وطن‌هاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/439094" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439092">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
نوجوانان مشهدی سنگربانان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/439092" target="_blank">📅 23:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439091">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
بروجردی‌ها: مسئولان بسم‌الله حمایت از حزب‌الله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/439091" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439090">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خلاصه جلسه 1</div>
  <div class="tg-doc-extra">Ostad Khamenei - استاد خامنه ای</div>
</div>
<a href="https://t.me/farsna/439090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
جلسهٔ اول اندیشه اسلام از زبان رهبر شهید
🔹
این صوت، خلاصه‌ای از اولین جلسهٔ سخنرانی رهبر شهید انقلاب در سال ۱۳۵۳ دربارهٔ طرح کلی اندیشهٔ اسلام در قرآن است.
🔹
هر روز یک قسمت از این جلسات به همراه متن خلاصه در فارس معارف منتشر خواهد شد.
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/439090" target="_blank">📅 22:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439089">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برترین‌های ورزش ایران در سال ۱۴۰۴ معرفی شدند
🔹
بانوی ورزش ایران: زهرا کیانی
🔸
آقای ورزش ایران: امیرحسین زارع
🔹
بهترین فدراسیون ورزشی: فدراسیون کشتی
🔸
بهترین تیم سال: تیم ملی فوتسال
🔹
سرمربی سال ورزش: پژمان درستکار، سرمربی تیم ملی کشتی آزاد
🔸
زننده گل سال: مهدی طارمی
🔹
قهرمان فردای ایران: مبینا نعمت‌زاده
🔸
بانوی پارالمپیک ایران: هاجر صفرزاده
🔹
آقای پارالمپیک ایران: علی‌اکبر غریب‌شاهی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439089" target="_blank">📅 22:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439086">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFGORqXHaGDaVy37VkAeLKUKVH8GKnIPxpSB4IfcuenLnK-yKuh5ymjWAtChmop6nDAFfLK0FguTlsKsJGCmEf9vPaS6z8FaLgNgH7UlUqF9yprMnPIaVVW6emL_3ugEVdUUUWNCi8zXYCcOBjPtOBrd_AyEhnMtI5zSG5IVHeBfiz5-gX0ZFeV4Rev6AaJaMBl0yFwAXxiPf4Sg1LSck1iZYVTCURohcB6idv4scp0alve528bVbqs2kLlkUdZ_eS1UPCVmlZNMEA91l4ogfNWC7ZWP5O88JCkTuMgHO72lJEH1R3okHMY77bd8gIi4o_GUEaQ2SPY3Rt0jn7wBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGwPdARTuOSaaZlW6ZflZSdpo0tocwXQpSbpHsaCqx4aFOB0VYOIDihK-8U1-D3HLkDEWzkI97_9lxonS-CAK5w_CrNe_lc_S0nNlbo1l3sLJjSMVE3NT6EmWM2VF7uw55ujDsI_u1xuuHJEkGuK0sZ37Z7aaVCboVruWFZKvX3pFwfE-0ZgGVgcwhS2HmdtZE7t3zId8z6hCeCierksQNaXdsbG3e8kKaaIVtCbEmJIpncAg0iTYSlGVeKcdhSoaPlZwuJU1v82s8NE1ah3izHfGkxBo5oePUpG_kgZ5_167FXFZeqKjE8A9IJGRph3iMk76-BgwUY3ZIHsF6GcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWpuKHB6Khj7CtY9k6yGLbv-h7QYnnbpxGBV1SRJ93f1sGV3lssDXwATVBVajtHN66Og6nkyedFH1rIAzeDQAte7YYb4dMlSfQEBdySpZ2VhVDX-9xggBX764BGsJGRoU_JyiCusj-6lyzcZs2SdIcpMqztueWkxPQGrpSylsh6gEJPrpTUZ7T49d4O2y8IKnIRaYMX2x_Xvgt710Uq_ZbrdVUyBgJ6GPQiT3auKykRwxrrcmETL__FLjjC5gUe_ke10JDpW7IVY8CBlOeQ-PFgsfpSLOdXOLjmych3t7hFPQqq9ZwG8-LrGNwDXqrbeJybOJHiR4ky_hZd2w5W-Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: روند را با قدرت و با صلابت تا جایی که جان در بدن داریم ادامه خواهیم داد
🔹
یا با قدرت مدیریت را ادامه می‌دهیم یا شهید می‌شویم؛ جان ما که از رهبر شهیدمان بالاتر نیست. @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/439086" target="_blank">📅 22:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439085">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0142c54c85.mp4?token=v_rBo0jDF09_TWzgvvQ24KDIxkpXXiTcZZFvg_rDxFNM_KkJOx-QS9Dfgu78aY0VIbXKSzHoVm0y3XwbK17VqcceNsaOn1nBIbUo7C2OgKYETXwlQLle1-mb5MirPPKxLH43yX65GMuA_5pVmsIM-YgqYjmStyiJTDWXUIhBcd3Sg6MV3pyvUYp6vNKMlAdEArbTKu_oOgI0h-2ErzKnf4RYKajyIut5czBQMwo7wgoBVzSa_zoK6tW8_-ssuN01U_uakDiZODsxj1LxVMH5m5GrGcdpdY5KI1iW9LAIujS7H6UVLipb4ezN0Sc5epP2vU65eFISrks5c1ywaVllQlUAvZg6NEtThA_jmxnkY4vgoN_-JCKcwfjAGCGme5lfi2UZg6Z3RLkmDMVR1LnvXLk94b0j31-GjEAtZP70S7ct4kq5MAH-b66Rey3N7zeMNasItlYy6iWVFGVPLWwEDGD4XK6q78mBR860mosQNgLz7nhxhYuJ5R_FlrzZLTAoQ3Oas72L_uEdJWRYLqJG8DKppOP-XvuCCOZa2u3e1dSzq66m7npPPyXrRz_2v05GHV2f59Rgp3RyKedd5cLy08iSwEsTXBdV8CHdU4nRDIPX1Kl20e-IPLWI1SmisHHJsZLFpn65yeP_tcHEYqVAOrmPcacd73YYDIRVIoFMaJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0142c54c85.mp4?token=v_rBo0jDF09_TWzgvvQ24KDIxkpXXiTcZZFvg_rDxFNM_KkJOx-QS9Dfgu78aY0VIbXKSzHoVm0y3XwbK17VqcceNsaOn1nBIbUo7C2OgKYETXwlQLle1-mb5MirPPKxLH43yX65GMuA_5pVmsIM-YgqYjmStyiJTDWXUIhBcd3Sg6MV3pyvUYp6vNKMlAdEArbTKu_oOgI0h-2ErzKnf4RYKajyIut5czBQMwo7wgoBVzSa_zoK6tW8_-ssuN01U_uakDiZODsxj1LxVMH5m5GrGcdpdY5KI1iW9LAIujS7H6UVLipb4ezN0Sc5epP2vU65eFISrks5c1ywaVllQlUAvZg6NEtThA_jmxnkY4vgoN_-JCKcwfjAGCGme5lfi2UZg6Z3RLkmDMVR1LnvXLk94b0j31-GjEAtZP70S7ct4kq5MAH-b66Rey3N7zeMNasItlYy6iWVFGVPLWwEDGD4XK6q78mBR860mosQNgLz7nhxhYuJ5R_FlrzZLTAoQ3Oas72L_uEdJWRYLqJG8DKppOP-XvuCCOZa2u3e1dSzq66m7npPPyXrRz_2v05GHV2f59Rgp3RyKedd5cLy08iSwEsTXBdV8CHdU4nRDIPX1Kl20e-IPLWI1SmisHHJsZLFpn65yeP_tcHEYqVAOrmPcacd73YYDIRVIoFMaJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرگانی‌ها ۹۲ شب در خط مقدم خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/439085" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌
🔴
حزب‌الله: ‌۲ خودروی هامر ارتش دشمن اسرائیلی در اطراف قلعۀ تاریخی الشقیف در جنوب لبنان با پهپادهای ابابیل مورد اصابت قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/439084" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f63808e3.mp4?token=su3Ks2vtXL5NZiWOi-AOwQJ3WSrs5C5iFbb8m--8zFb5LzVIWDB5MfyJwz4lIYXMTLYBTMnL7TAu9khfJSTRkEAtT53RQOauE1iPVoeFapW8ZM_T2HdcenvHL-H_RHCnGKR2ILm83-_HfHAnogdfitxFoxaa1EvnehysLPiYw3luU0pDFKwK-Xu8TprZZB6Pzzj9fI4vEN41_GTGojFlflAvV3j7Sy9zZEtfZhe7f_ROB9HAK9Wg3TlpBkXsKnxSqVnsAJwVzMjPJzXdxcO1bLG-LH0S6ywPo60fl-3dhnuGgLQxWoMoM1_M-EexhYXp4a1PHHRLEeiT3Q6uzs4EHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f63808e3.mp4?token=su3Ks2vtXL5NZiWOi-AOwQJ3WSrs5C5iFbb8m--8zFb5LzVIWDB5MfyJwz4lIYXMTLYBTMnL7TAu9khfJSTRkEAtT53RQOauE1iPVoeFapW8ZM_T2HdcenvHL-H_RHCnGKR2ILm83-_HfHAnogdfitxFoxaa1EvnehysLPiYw3luU0pDFKwK-Xu8TprZZB6Pzzj9fI4vEN41_GTGojFlflAvV3j7Sy9zZEtfZhe7f_ROB9HAK9Wg3TlpBkXsKnxSqVnsAJwVzMjPJzXdxcO1bLG-LH0S6ywPo60fl-3dhnuGgLQxWoMoM1_M-EexhYXp4a1PHHRLEeiT3Q6uzs4EHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«امیرحسین زارع» آقای ورزش ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/439083" target="_blank">📅 22:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99175aab.mp4?token=J34RxgGsUNQA-SaWVIOnGUQSEjzfR8v3HEH5FX5PNf6Ue7FLeINUAL2gKo_mxkFUctn4J2Jv_fVX8ti2n2YkXLQ9lmbnyxDj4fsFE-iEL3t9l2WjbDY5_zIHsLMakdlnz-_Kt5SPrXN8fWqVACR-S04nXDwHHBD3AZL1D4jzcHSv5Zj7TkdKtLyZkWS5FROEOsUtg2rkbn2uEvBS_tkcCA2fw6zRyOUDwoo4xV3F0wrDAO8yTySuHu6f1zEUEDzZu19Dm0fLQye1OqdqoR7hgHQx1He-Zf_Eer3201AAr-THfZY9cE7C70ZpC-ZyuwrIQ2pTnVQmNdigxsi6tEGZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99175aab.mp4?token=J34RxgGsUNQA-SaWVIOnGUQSEjzfR8v3HEH5FX5PNf6Ue7FLeINUAL2gKo_mxkFUctn4J2Jv_fVX8ti2n2YkXLQ9lmbnyxDj4fsFE-iEL3t9l2WjbDY5_zIHsLMakdlnz-_Kt5SPrXN8fWqVACR-S04nXDwHHBD3AZL1D4jzcHSv5Zj7TkdKtLyZkWS5FROEOsUtg2rkbn2uEvBS_tkcCA2fw6zRyOUDwoo4xV3F0wrDAO8yTySuHu6f1zEUEDzZu19Dm0fLQye1OqdqoR7hgHQx1He-Zf_Eer3201AAr-THfZY9cE7C70ZpC-ZyuwrIQ2pTnVQmNdigxsi6tEGZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهروز رهبری‌فر، بازیکن سابق پرسپولیس: من خودم را فرزند شهید می‌دانم؛ چون پدرمان امام خامنه‌ای را از دست دادیم
🔹
۳ ماه است مردم هرشب به خیابان می‌آیند و نشان دادند که همه‌شان تختی و پوریای ولی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/439082" target="_blank">📅 22:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f74332a29.mp4?token=lYXIoAeqMv84Zs69fs0g4ZyA33blkfaTKPL_S0PeUM0EFwRIzYDA9EmAsO0X5aIzRDw_aJA6DAa5SgW9oZL0ZTmLs4iLkQ6kq1wifSVcgDFxrZKgZqPaT2n57ZhAgccZUaFA5obviE6KAmgL_Ok5_UvSVGrOPczDkUPQeYdltsgv2E6-eBXnz2Ok2HoVbz42NCenq5SOlbGv1R2kEQIpBGKHXDtzq1eE5hn4jtq9NU7VkxpUo0q_kQ1Ks6nPiCbc4_CxmQq2kIK-bTkbwOVQJaGxDzA0HbfOkRX-0Yh_Q79MX19V8sOLsXrN2xTZQwhyqlHY_Fdkz4qobuozosEjqyNb2n-If6FTOFRMdk8-UfJQiIcWwHXoFw2x_a-NnykeO30KBn5sm3js_CSYjo9r8Di8ZRpEGCiEfQaxGpf83wL9Dywjvz3UWDdyo9ZeV24Zm8yRaTNdyG5rbavHIilv3LeJi-j6twfWczWxRXMyIp_Yar279MPz0vTgbKOSQIFiltYV00GlLfM7T_Sr5itUwkHWzqbQ7gG8jKynGQB9m8Jdfe4EXJk4zAoA2SPqAkyvyHiol7Sanlu54maIV5kFKK367-ngm2i8izmXUg8IoyVMxk0YX3VxmIc0-1-oAnvimjItkU_XY2EMXI9_stJS7Md144sx2GctgkKAQJaZ2jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f74332a29.mp4?token=lYXIoAeqMv84Zs69fs0g4ZyA33blkfaTKPL_S0PeUM0EFwRIzYDA9EmAsO0X5aIzRDw_aJA6DAa5SgW9oZL0ZTmLs4iLkQ6kq1wifSVcgDFxrZKgZqPaT2n57ZhAgccZUaFA5obviE6KAmgL_Ok5_UvSVGrOPczDkUPQeYdltsgv2E6-eBXnz2Ok2HoVbz42NCenq5SOlbGv1R2kEQIpBGKHXDtzq1eE5hn4jtq9NU7VkxpUo0q_kQ1Ks6nPiCbc4_CxmQq2kIK-bTkbwOVQJaGxDzA0HbfOkRX-0Yh_Q79MX19V8sOLsXrN2xTZQwhyqlHY_Fdkz4qobuozosEjqyNb2n-If6FTOFRMdk8-UfJQiIcWwHXoFw2x_a-NnykeO30KBn5sm3js_CSYjo9r8Di8ZRpEGCiEfQaxGpf83wL9Dywjvz3UWDdyo9ZeV24Zm8yRaTNdyG5rbavHIilv3LeJi-j6twfWczWxRXMyIp_Yar279MPz0vTgbKOSQIFiltYV00GlLfM7T_Sr5itUwkHWzqbQ7gG8jKynGQB9m8Jdfe4EXJk4zAoA2SPqAkyvyHiol7Sanlu54maIV5kFKK367-ngm2i8izmXUg8IoyVMxk0YX3VxmIc0-1-oAnvimjItkU_XY2EMXI9_stJS7Md144sx2GctgkKAQJaZ2jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرمانده‌ای که‌‌ از جنگ ۳۳ روزه کابوس اسرائیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/439081" target="_blank">📅 21:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439080">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b5b05076.mp4?token=OEIlAZGLKaE8evPMN0wybwtRmKSwYYyphRYh5aFfp_zZGp_c-CEwGG1DtVSRl_i7fnUvzGRZEjoqjRReu-mqeFWMZ2mIQKMv4RXPf-GpcF-8zeMfK3hh5z3uCY3JKK33fQazN5BhmxOg7K8hycJB75Css8dGfJ_QX3bsszgttJ9fM0lLEozYDmVXBqhVz0zn-tZTN9BfflQ12MMHX95dfb4gTLDpjGWSWtBPtZ0nhfjGEF9O9ofxvTsBiCxjfn-8sLF7GDzskdsUXZypaLvi8cAVvM5KGjIplRGUW-MIq-qQx9c-Vzz6aEfl8WencZH-Qp0k_TmU4xp6m5E3hF3mPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b5b05076.mp4?token=OEIlAZGLKaE8evPMN0wybwtRmKSwYYyphRYh5aFfp_zZGp_c-CEwGG1DtVSRl_i7fnUvzGRZEjoqjRReu-mqeFWMZ2mIQKMv4RXPf-GpcF-8zeMfK3hh5z3uCY3JKK33fQazN5BhmxOg7K8hycJB75Css8dGfJ_QX3bsszgttJ9fM0lLEozYDmVXBqhVz0zn-tZTN9BfflQ12MMHX95dfb4gTLDpjGWSWtBPtZ0nhfjGEF9O9ofxvTsBiCxjfn-8sLF7GDzskdsUXZypaLvi8cAVvM5KGjIplRGUW-MIq-qQx9c-Vzz6aEfl8WencZH-Qp0k_TmU4xp6m5E3hF3mPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زهرا کیانی، بانوی ورزش ایران در سال ۱۴۰۴: عنوان خودم را تقدیم می‌کنم به دختران شهید مدرسهٔ میناب و خانواده‌های داغدارشان.
@Farsna</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/439080" target="_blank">📅 21:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebEo7XCvdoZEgrK_juh3JspjU0im10_lFXGNEMgGnjbPcEtkfJ5R_iI8JCY88RnY9odBlnfEwTD3q7kdJoNqjBhBzQ-x2qTKq8Nny4Cmq7kiouZOhZrO-xkdtYUhjYlcvJqqOIt4Lwq6fd7gV7SWAiV4SgNl3lTOKhBF9gQBAIKJxnK28Qy48egYkMe-zGPM2fiy32fs_cX5DmfZXw4Wf83zLIE_JaTXN2nv8EIOx-6h4gI7QzschD_kCbrhduNEkNgfCV2pbx4pLpsQcVFRuGyekMM7dklO6Vi6rmn6Ti-E5RF1JO-p5f-KO6wmDsONhMFNmVi9IcsaRcjQHtaBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: در جنگ رمضان به فناوری‌ای دست‌پیداکردیم که حدود ۲۱۰ پرندۀ دشمن را هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/439079" target="_blank">📅 21:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a71937ed.mp4?token=BiMuAbwlW7Lxm4LZanWc0OwTr7tc6QppzOMZQJEyxWJn5gZA5eucgwjhDn_aGSeNSSsQnt-f2HklxarInOwWgD7oGjPImm-ehAZ5askyna858qtFkC4ZnM2dG2ekQFlTJqtYJt1M0o2CczUAUDez60ryPCqNrBx_0wpj0fIymGbLuECqkSc4kMti63Ug6uS4Vv7yoqUlgMFZJasoMxJjdeODLKN4_lAkNyJ1qGbxpbldfgKZy1GDje2AB2TfUGL8Ivacc8g0XF9_xXfT5sP1pTSfsoM3K6j5MdfS-sf1duKzk6Z2TIJ1yFiHeS6W7bmnD26O59Ro9VXiyX_lz7vW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a71937ed.mp4?token=BiMuAbwlW7Lxm4LZanWc0OwTr7tc6QppzOMZQJEyxWJn5gZA5eucgwjhDn_aGSeNSSsQnt-f2HklxarInOwWgD7oGjPImm-ehAZ5askyna858qtFkC4ZnM2dG2ekQFlTJqtYJt1M0o2CczUAUDez60ryPCqNrBx_0wpj0fIymGbLuECqkSc4kMti63Ug6uS4Vv7yoqUlgMFZJasoMxJjdeODLKN4_lAkNyJ1qGbxpbldfgKZy1GDje2AB2TfUGL8Ivacc8g0XF9_xXfT5sP1pTSfsoM3K6j5MdfS-sf1duKzk6Z2TIJ1yFiHeS6W7bmnD26O59Ro9VXiyX_lz7vW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پژمان درستکار، سرمربی تیم ملی کشتی آزاد: اگر ما اینجا ایستادیم و پرچم و خاک ایران استوار است دلیلش رشادت‌های شهدا و مدافعان میهن است.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/439078" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439077">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df801dd95.mp4?token=FJr2qHeeQi2kBW1k4tqpVb3PUJElDvbpjfJNxizAtTAjcQ6JCxsyrhD0_tiFWuf-dLnxO9Wlm77DBBTmx77EX2viqInCNNe4F_nRA_1BTuXCI5-4c5uQiVAUJUHZdPhjpa9eh4j_e7Q50ff_BIx3K5JgXeX_07r5h_8KBrTWoZMkAL2pIY_-IOg4TyE5JMrwtCaxYNlVxG7hKJN7QjevWCp9fq9OWwRkhyYhKQs4BB8Rj2kexyARaKYrCxicXTkrQrcTR1gJilFiHDvs2mFeMzp-b8gsAmnaWuPSm3lyKpM4_Gn8u8EubKY6rEFAmU-Z7ysmzT9cvjvauc1ZJYg7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df801dd95.mp4?token=FJr2qHeeQi2kBW1k4tqpVb3PUJElDvbpjfJNxizAtTAjcQ6JCxsyrhD0_tiFWuf-dLnxO9Wlm77DBBTmx77EX2viqInCNNe4F_nRA_1BTuXCI5-4c5uQiVAUJUHZdPhjpa9eh4j_e7Q50ff_BIx3K5JgXeX_07r5h_8KBrTWoZMkAL2pIY_-IOg4TyE5JMrwtCaxYNlVxG7hKJN7QjevWCp9fq9OWwRkhyYhKQs4BB8Rj2kexyARaKYrCxicXTkrQrcTR1gJilFiHDvs2mFeMzp-b8gsAmnaWuPSm3lyKpM4_Gn8u8EubKY6rEFAmU-Z7ysmzT9cvjvauc1ZJYg7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هاشمی‌طبا: تمام سال‌های خدمتم در برابر یک لحظه فداکاری رزمندگان ما بسیار ناچیز است.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/439077" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6AxmUycal2TBhvn1KnFcrFqbMw66m57Jvk8WmpwAnRAPoXRvAwJ5SZ3BqqY2gmj4cHciTK4xCxcgiTTfQlkEK5VIyyW-qp16YBGBPuSkEzl6Kk-ZtfOQN88axNPu_GMdcXeqSGIK5ypGGGr_Yz1HJSuIh_6yhQiYekYUSKWMYbfQpFZq3cuTn0h2ocRge-kYASnXfz7XoI6m6l0uFApkYBwJl4-_uLao4UlfIpS5_tmzggsgdrId0bH02cNobUHhdgE7lNEGxhhmhOexdZwkWhIZfsRvQlc50Xs5dBQD0hJvvX8P8utkeYLjn4V_qKzjWN-aiYTRwsmYANbBl0D1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: مصرف برق ۱۰ تا ۱۵ درصد کاهش یافته است
🔹
با وجود اینکه با توجه به شرایط موجود باید انتظار افزایش مصرف را داشته باشیم، در حال حاضر کاهش ۱۰ تا ۱۵ درصدی مصرف را مشاهده می‌کنیم.
🔹
مردم در مدیریت مصرف همراهی خوبی داشته‌اند و این همکاری در کاهش میزان مصرف کاملاً مشهود است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/439076" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fc237f0e.mp4?token=ORIX-YZrScqfBXhb8llx6V22jCVYUHHEeFgi_xCfJwyFe8HsQdl2RZwOo-N_wzSjwv7bdgTW5rXSMc3LeCWz3Qc_aZDFM7Ju4s3cGQ1VaY4AQ637s0Ii4EwKOY23X6mZ-Z_rEhDmnbJQ4pedGsCx1JmJfpLKR6J_YL3iyGdi2g4aE9EwzM-HqWzD-7N6xY-abCQOsZTaRLnAX-S3jP7YB6UEveND6uWNJAlH-qFRQ1onzQl8HO5TnQgIgsiYKD_yJ3gx2o5cnktoB_gX2DUMTNk4i1Ebm2OXKTpTFbou_pF795-kfCJ9ER_cFKmtOsr3rkRCTY2z7tUHfQRZjw57AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fc237f0e.mp4?token=ORIX-YZrScqfBXhb8llx6V22jCVYUHHEeFgi_xCfJwyFe8HsQdl2RZwOo-N_wzSjwv7bdgTW5rXSMc3LeCWz3Qc_aZDFM7Ju4s3cGQ1VaY4AQ637s0Ii4EwKOY23X6mZ-Z_rEhDmnbJQ4pedGsCx1JmJfpLKR6J_YL3iyGdi2g4aE9EwzM-HqWzD-7N6xY-abCQOsZTaRLnAX-S3jP7YB6UEveND6uWNJAlH-qFRQ1onzQl8HO5TnQgIgsiYKD_yJ3gx2o5cnktoB_gX2DUMTNk4i1Ebm2OXKTpTFbou_pF795-kfCJ9ER_cFKmtOsr3rkRCTY2z7tUHfQRZjw57AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: به آقای پزشکیان می‌گویم از وقتی شما رئیس‌جمهور شدید دیگر کسی به ما گیر نمی‌دهد که چرا کت‌وشلوار نمی‌پوشید
🔹
دیروز هم که رئیس‌جمهور کت را درآورد و آستین کوتاه پوشید و ما راحت‌تر شدیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/439075" target="_blank">📅 21:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed3a553bf.mp4?token=m1FntmxFFeaVHkZWTZMpgyP-4eko5x9uTaZUyQCTZXLWyC2rvpPLra4zqKSCAtCOi9vQq0bUZfCE0ONV1Iw5C1UD44ROJhWPJ0IPmrgQjp7-zbTzCJvW14AZPTkMZBHOSS9eKqkcsWErFB1nRLkYJgww4-fcokn81N0k8kYRVO4bTTBqoyGgFlN0muovCg0hdZ3A7-JEmqqUdnuuzM5WnZPkTHB-3xN9ZG3jDUvnO8gXVzeADS3qqa9z-CAwclKS6jykx3-IQ3YvEHaRwGs28G2lJ8KJvX3tUF8FXvDo4y0vhYinCJOUVMCSFW3-2eVqcQ8apxm6LsiJPN9mPc4PAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed3a553bf.mp4?token=m1FntmxFFeaVHkZWTZMpgyP-4eko5x9uTaZUyQCTZXLWyC2rvpPLra4zqKSCAtCOi9vQq0bUZfCE0ONV1Iw5C1UD44ROJhWPJ0IPmrgQjp7-zbTzCJvW14AZPTkMZBHOSS9eKqkcsWErFB1nRLkYJgww4-fcokn81N0k8kYRVO4bTTBqoyGgFlN0muovCg0hdZ3A7-JEmqqUdnuuzM5WnZPkTHB-3xN9ZG3jDUvnO8gXVzeADS3qqa9z-CAwclKS6jykx3-IQ3YvEHaRwGs28G2lJ8KJvX3tUF8FXvDo4y0vhYinCJOUVMCSFW3-2eVqcQ8apxm6LsiJPN9mPc4PAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
واکنش معاون اطلاع‌رسانی دفتر رئیس‌جمهور به دروغ‌پردازی شبکه ضدایرانی اینترنشنال در مورد استعفای پزشکیان
🔸
رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/439074" target="_blank">📅 21:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439073">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌  فدراسیون فوتبال: شایعۀ رد درخواست ویزای بازیکنان تیم ملی برای جام جهانی ۲۰۲۶ کذب است
🔹
فرایند اداری مربوط به دریافت ویزا طبق روال انجام گرفته. @Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/439073" target="_blank">📅 21:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439072">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qV_8fBmIF1ZosPLPbS-zvjwIk4kyQqgxtpT4drb6byArdW9AMus8oPCu4yLDsfm_kmKpzP1mEHjAXV_4Ax2IUUnaFJgg2vY4BqBdk2-Dm6LG6gJ7KzS1RMDI1T_qbz4FhI6T-sdedxrs3rdplAzLnXC_2o0GyhU28uDyNBHyl1FYaL6URclK7kQQLmXuugB5bnMsAwS9ZxfBe6qDyirSx6c4p1qDNQhLNbkd8VzLJsE84VuRC8N5NTgg34xGrQ4b6C9cDwn-BlkscQh8P0UvRRMPL_gqsXbTAt_DCskiSy0EF40eRtCdz9RODqvvbTRPwuKhKeYPcxhQLTc97S-Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون اطلاع‌رسانی دفتر رئیس‌جمهور به دروغ‌پردازی شبکه ضدایرانی اینترنشنال در مورد استعفای پزشکیان
🔸
رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439072" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439070">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd63434b5a.mp4?token=HPa0NVQWbjJuC7YDGirv4gMLJh1jVAjeFKz3FBiJGmemrSgEtJounqprPueIyzLWvngehW18UBClTh8oKxObCnbrz7z_jATlmypcCKsR0Ge3TjSsUGPqtTyXpPAi8ze1bX2NeAdscl89a2rzYPAyJC2_mu3zCLcOeuz2ZJY4AJD95uMTHVYrsabyjLmcSJmSSJu1szKfgQkCwX6qFrOzR0QIsOFRbq4ZsxmFSljbr7Pxm4w0SpEXpHS24NhfPbL2Qb90dGQlbxF5I1NhrruD-dwlVM7qwVUG_CuqSZMuxm2gXrH7U7i2stlIt3t-2dDzyqV0qKkZFgQ1ox4xPmQf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd63434b5a.mp4?token=HPa0NVQWbjJuC7YDGirv4gMLJh1jVAjeFKz3FBiJGmemrSgEtJounqprPueIyzLWvngehW18UBClTh8oKxObCnbrz7z_jATlmypcCKsR0Ge3TjSsUGPqtTyXpPAi8ze1bX2NeAdscl89a2rzYPAyJC2_mu3zCLcOeuz2ZJY4AJD95uMTHVYrsabyjLmcSJmSSJu1szKfgQkCwX6qFrOzR0QIsOFRbq4ZsxmFSljbr7Pxm4w0SpEXpHS24NhfPbL2Qb90dGQlbxF5I1NhrruD-dwlVM7qwVUG_CuqSZMuxm2gXrH7U7i2stlIt3t-2dDzyqV0qKkZFgQ1ox4xPmQf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زخمی شدن چند صهیونیست در عملیات ضد اسرائیلی در کرانهٔ باختری
🔹
روزنامه معاریو: در این عملیات ۴ صهیونیست زخمی شده و وضعیت دو نفر از آنان وخیم است.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/439070" target="_blank">📅 21:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439069">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
اصابت پهپاد حزب‌الله به یک مقر نظامی ارتش اسرائیل
🔹
وبسایت عبری حدشوت بزمان: در حمله به یک پایگاه ارتش اسرائیل در شهرک «بیت هلیل» ۵ نظامی اسرائیلی زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/439069" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439068">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82e87bc58.mp4?token=fDSTaCGrZEz24nlWXhe6rn_PP_qpXJ9t-FTApruy22mtkW6zYEEQvM9h66EOdMJxDzdg6AxdHnN2Z2zKHW9vS_BK_GeTHdW1OU2_tpk457uYUjH1A_8ClIViYBx9Bu5Hvr5kB6by3ZdBwWZAu65lOWIwfS7LEORs2zg1WRn8CWWtJAi_jmYHJT2LrudVHHRxRCiUz7Xsibq04DTxoiWN7rhNMwyOCfs1U4ulF17h0rbzGxiuZ6V2eUv8Z5xskK2m6kFPCljaVTwdxIiLlQSiH0uCbxN8KyNn7ohUO3zShfZFvNFFjH0BgKhEhpfLwYRutZhRf-Ka7IYM3UCmNdW7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82e87bc58.mp4?token=fDSTaCGrZEz24nlWXhe6rn_PP_qpXJ9t-FTApruy22mtkW6zYEEQvM9h66EOdMJxDzdg6AxdHnN2Z2zKHW9vS_BK_GeTHdW1OU2_tpk457uYUjH1A_8ClIViYBx9Bu5Hvr5kB6by3ZdBwWZAu65lOWIwfS7LEORs2zg1WRn8CWWtJAi_jmYHJT2LrudVHHRxRCiUz7Xsibq04DTxoiWN7rhNMwyOCfs1U4ulF17h0rbzGxiuZ6V2eUv8Z5xskK2m6kFPCljaVTwdxIiLlQSiH0uCbxN8KyNn7ohUO3zShfZFvNFFjH0BgKhEhpfLwYRutZhRf-Ka7IYM3UCmNdW7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در مراسم قهرمان ایران
@Sportfars</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/439068" target="_blank">📅 21:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439067">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عراقچی: تبادل پیام‌ها در جریان است اما تا زمانی که به نتیجهٔ مشخصی نرسد نمی‌توان در مورد آن قضاوت کرد
🔹
به گمانه‌زنی‌هایی که صورت می‌گیرد تا زمانی که به قطعیت برسد نباید اهمیت داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/439067" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjmA0WmNFlA4Wx5ivon7AO0bq_DgWJR0_UL058yI52meUOE95brEUIcO4QA2boRtgTlfC931MqguXwkAJrFMU1U7f1lgV1ms4meaqkVyHdQJPaVGEWdEsr1aODXh1IPs1jfy2Y4dCJM7fYhTc9AP6jbGf8_k41w9GpHemuvXnhzYW7eX2dpgp-TdJHW2rv_-VramFvOh631fP2pBreie-yJ0TkNZMZ68zJR9vPkRDaunWV77KItPctX7xRERKid_WL2hxHDWKGnNXSyrtqF5K_f_896cEBUkZBs7yFRh56tmPchnZ3xkSEKZWIO_ArGFdo6EruMRrhjbfwIy4hKYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ فرودگاه کشور میزبان حاجیان می‌شوند
🔹
در عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور، نزدیک به ۳۱ هزار زائر ایرانی طی ۱۱ روز و با بهره‌گیری از ۹ فروند هواپیما به کشور بازگردانده می‌شوند.
🔹
براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/439065" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا به زخمی شدن نظامیانش در پاسخ ایران به نقض آتش‌بس اعتراف کرد
🔹
سی‌بی‌اس به نقل از مقامات آمریکایی گزارش داد که در حملات موشکی ایران در واکنش به نقض آتش‌بس توسط آمریکا، چهار نظامی آمریکایی و سه پیمانکار زخمی‌ شده‌اند؛ درحالی‌که ارتش آمریکا مدعی شده بود که موشک بالستیک ایران را رهگیری کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/439064" target="_blank">📅 20:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224f2690cc.mp4?token=gfT8TpfV6OZZSEbg5EgmUo0JUCTbS4DgNEgZspI4beUtzRTtFQBqlQQ4esjAjvQ1Ibtkm23N4CI5yfp-BqfdSLCSEMWE0bo0zmXrf4_sYqqH5_GaO6nZEb80W92JpV9pi-lMdbMjlf9RmNBrgG4FpFa8r7OBCu9HWQww9rfWlvCHUXcVUpvoPM7W6p8kxTfStCMri7GM3eUj8t77xdrQSeI1kknJ1bJKPgE-xDQgnLUG4GWWdy-a3jlyIzAjs2pzOLMbuQvLCmnLqAQAWSsYbJ5nBxC37WJtAnPs6v1RUUolQLQpM_r8wRNm5j9W0ZlmgTcdJ6Cnm2kAqZJT5KicIanwfDGg1inxDZePnv2cz-a0wLOX6OBYpj6aYVjgWGEykUI8YocE8v1ocXABp_rXumA8v0iUWjrQluHlnvM73kNzobwAWAmyG9GF7ZwNKzdTKPk0PR71XqKbbK_XxErHWePFIyE3AaDcZhhkFYisMtS5RqoSfzNZ7M5aBWUQuktfFA7tcwXJMy72ITnMV0CVbDhfOgqYZiReg30s2by-N4k4G-RfaIgO-8MI0JYLIrT2lRfyiRd_fsaZCagotsXG1j_cJlC8e2eVmXE1wZV9i5n3ZRcdCwSFZ3jAXZz61QVbwnmmLX5MrCgyIo8Q2XlVktklrqlNZuC9-QsBpXn7fms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224f2690cc.mp4?token=gfT8TpfV6OZZSEbg5EgmUo0JUCTbS4DgNEgZspI4beUtzRTtFQBqlQQ4esjAjvQ1Ibtkm23N4CI5yfp-BqfdSLCSEMWE0bo0zmXrf4_sYqqH5_GaO6nZEb80W92JpV9pi-lMdbMjlf9RmNBrgG4FpFa8r7OBCu9HWQww9rfWlvCHUXcVUpvoPM7W6p8kxTfStCMri7GM3eUj8t77xdrQSeI1kknJ1bJKPgE-xDQgnLUG4GWWdy-a3jlyIzAjs2pzOLMbuQvLCmnLqAQAWSsYbJ5nBxC37WJtAnPs6v1RUUolQLQpM_r8wRNm5j9W0ZlmgTcdJ6Cnm2kAqZJT5KicIanwfDGg1inxDZePnv2cz-a0wLOX6OBYpj6aYVjgWGEykUI8YocE8v1ocXABp_rXumA8v0iUWjrQluHlnvM73kNzobwAWAmyG9GF7ZwNKzdTKPk0PR71XqKbbK_XxErHWePFIyE3AaDcZhhkFYisMtS5RqoSfzNZ7M5aBWUQuktfFA7tcwXJMy72ITnMV0CVbDhfOgqYZiReg30s2by-N4k4G-RfaIgO-8MI0JYLIrT2lRfyiRd_fsaZCagotsXG1j_cJlC8e2eVmXE1wZV9i5n3ZRcdCwSFZ3jAXZz61QVbwnmmLX5MrCgyIo8Q2XlVktklrqlNZuC9-QsBpXn7fms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم خطاب به دیپلمات‌ها: صدای رسای اقتدار ایران در جهان باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/439063" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439062">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMyZ9xn4UyYFKMilIfvJwaMxBTkA-C0pkfiSzO-eRWHFx6Dm928nM51SM0K5hhuLuytpra8cVTkjvcQYOhh7hc-ngHRSCURUt3hhNkj-Bo21_NUf5bj-7oolXTC2Gj8bDycMSxSpZHOrP8jx2FQO8zEFWmZyCKsZC2YAdp_3Bvt09cMXDm6QhXLdtuk4_oh8SssIYyOB7yEXd6okS7SbLzcuq48Pwx2uYf-GHjFWG4OtrQooQXuHN1Q8eJF3DsM6gfSKKlcduaj_xTmmQguwNxTzg5jPG43Qc1ATlTl7fyd7Xd3rOtcfMgiOgAuu2pvLsmypUCtkDhHCVS2fbDRDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت دولت الجولانی در برابر پیشروی‌های اسرائیل در سوریه
🔹
شبکهٔ روسی آرتی: یک گشت نظامی متشکل از ۴ خودرو در میانه نگرانی و اضطراب شهروندان سوری و بدون هیچ گونه دستگیری به سمت حوض یرموک در حومه غربی درعا حرکت کرد.
🔹
روز گذشته هم گروهی از نظامیان صهیونیست متشکل از ۳ خودروی نظامی به عمق حومهٔ جنوبی استان قنیطره در نزدیکی نوار مرزی با جولان اشغالی سوریه پیشروی کردند
🔹
تجاوزات ارتش رژیم صهیونیستی در جنوب سوریه در حالی انجام می‌شود که دولت الجولانی در قبال این اقدامات سکوت کرده و در حال انجام مذاکرات مستقیم با صهیونیست‌ها است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/439062" target="_blank">📅 20:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkfnZ7mk9lNF7IJxretAMo6t9fV7zhv_e6ojGM15F-yDOgcMgWdfjOEELZRpcRcxVmQ9JVATkYqGTjeWRW6DQ2ojwKEjpR95XFgj2OiRPPwRMfcH6fq66U1OsYyHMXYyFLLZ5uToC5ToJwiiVwtZ273GcXritWuECWaGUEgjHpzzggAjQ3O2KeXXA_Z_WcGw2l8HrdWmCb6NQ2qkZpcnr74AXP8kaBBJxdIkPN3s6GQa3Su6JPmz28NFQVTFWj46-ppVxobeW8GyvK8gkDE-q0XFpztlyHYRfjQNRx0z83xUFpeb8jSs6CIn67UnT-C-uTGKeIwn4dd5rMm5F7QDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ تلویزیونی «ثریا» فعلا پخش نمی‌شود
🔹
برنامۀ تلویزیونی «ثریا» که با اجرای محسن مقصودی تا امروز به صورت زنده پخش می‌شد،‌ در صفحه مجازی خود اعلام کرد که امشب روی آنتن نخواهد رفت. و تا اطلاع ثانوی پخش زنده نخواهد داشت.
🔹
صفحۀ مجازی این برنامه نوشت: «امیدواریم با تغییر شرایط و بهبود فضای رسانه‌ای، امکان پخش زنده این برنامه به‌ویژه در این روزها و شب‌های حساس و تاریخی ملت ایران فراهم گردد».
🔸
بنابر اطلاع خبرنگار فارس گرچه این برنامه فعلا روی آنتن نمی‌رود اما مستندهای تولیدی این تیم همچنان به پخش ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/439060" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVb_eigUIy8Xtgj0VDDgSXVjBrKs-PQ5Z4mPsXV7RPEIpbJ_nuNIcrbkZITjD_zIjrauTXmMK1bENLSGkNGzIqz75HXJmOtIKJ8zTGrqmzDvaL9yXgQgTdESR4lz53KDbzLfqNgOH5wmeLS-EYZNWRsXWBC2SudcjkZbxG41SO7Th72Ts4P59IUK4NtmYl8ykbhyt5sINabfwclcU5xOdQa07NSX8R2ddPFo1ct0xk8mlH2Vf8JYqcmQobCxDgAyjR7emaL7rNUpgWgblPqoYOIHGwYDktGQ2iqzRimOPNDsAfGx1hgMbnrGS4gKvLgheId91wK2EEMnmllJfQhK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن…</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/439058" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sskH-2TVxmD-itMxamvPxHoeqBDVW-Vfg57r6gZ_iR5MUcW4YnRW3h8sKgiji2JtVDnhNWbUaTBTa1kW0lnzaw4w_q-Z7SqwyUqyO8bctStEkXSRXBQl-gJJFvV5yLp4MXx2Qed4P3daCjM-HlCaf8v9iaCtLncgP0GLYbBxq_WaTs-qO8QTUT3UvWqUYxFQ0JA37nJ3jiLGj3DR1Ed_aYyG_HLQcBLxaxFQo0okfpLnvXLTEl1_V9LoUsMC3AOAIlFR3qS3vOfM-jmIzigh5eN9R0qFCe9BLczVksR1oMBmi_kGZ8WiTEATCA3wwBgUtl3KkH2ENirezTpTR_E3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از حملهٔ هوایی اسرائیل به یک بیمارستان در جنوب لبنان  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/439057" target="_blank">📅 20:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ae5815fc.mp4?token=K9gJWMvI4hJmqoJAgVzIJMOKxuzfpkn9Yb18G4O6iYxIl5y8xUPtSnqnF1TpnNnQd4YUwsUhKV1rR2Fr92LVATFQoksvZuusyZQSHyswYrJHKDD3MQTCBAkdkAptQpesrntmh7x1feqmW8lxJMSQpGwyITotmx2HlqhJF6to6VCYL01yoxN53jHa8rgMl-KUhr-PlGF7ulYdgFi9PAfQ9yt8HeIV91ZmRQCq89DqblfF2cyDqDEpftPU9Tplh38IpnwhXb9KKFFf89mezKiDsUWNcur331kN2RjME8gtRDOtdNb3mCRnP3MLNbJU2zEhPnrPZiIn3E4JSTjN-yB8Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ae5815fc.mp4?token=K9gJWMvI4hJmqoJAgVzIJMOKxuzfpkn9Yb18G4O6iYxIl5y8xUPtSnqnF1TpnNnQd4YUwsUhKV1rR2Fr92LVATFQoksvZuusyZQSHyswYrJHKDD3MQTCBAkdkAptQpesrntmh7x1feqmW8lxJMSQpGwyITotmx2HlqhJF6to6VCYL01yoxN53jHa8rgMl-KUhr-PlGF7ulYdgFi9PAfQ9yt8HeIV91ZmRQCq89DqblfF2cyDqDEpftPU9Tplh38IpnwhXb9KKFFf89mezKiDsUWNcur331kN2RjME8gtRDOtdNb3mCRnP3MLNbJU2zEhPnrPZiIn3E4JSTjN-yB8Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: جنگ امروز اقتصادی، اجتماعی و فرهنگی است
🔹
اگر به داخل کشور برسیم، نقشهٔ دشمن نقش‌برآب می‌شود. نباید اجازه دهیم که جوان ایرانی بیکار و بی‌هدف بماند.
🔹
همان‌طور که می‌گوییم «بزن که خوب می‌زنی» باید بگوییم «بساز که خوب می‌سازی».
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/439056" target="_blank">📅 20:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: در برابر زیاده‌خواهی‌های دشمن خواهیم جنگید
🔹
ما تا آخرین لحظه در برابر هرگونه زیاده‌خواهی، پنجه‌درپنجهٔ دشمن خواهیم جنگید و خیال ملت شریف ایران راحت باشد که فرزندان شما در نیروهای مسلح، با سلاح‌های آماده و انگشتانی روی ماشه، حافظ امنیت و عزت این مرز و بوم هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/439055" target="_blank">📅 19:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eChWbMqyIbcW0HIADq-FcNk3nkp0vj7AxGLDBJ7LjxDmG0tKJNn2rSyvSM5G3sHjV04aFaaiQPqwfXozuQUvELK13wAh6sLYaWOBkQFHR4aRgNPcXRwdkOFDy_Wiq_6pRPcFrwtCkdjqkMy-JP2cTj09jfnGOOmYc9MEEk0ebKdsGzteikdf4eMJBSAVKIk1wDszMk-hWURac8P-7UzDKmL3a6RmrqwVtDvqWoXv3O3Ud_vphpCXFTNHV3l58iIQK0uRNnQ63IeODbC3k-BINvQ6iHfBpvduHojvfgElrC6hr9uBFLguJZxwOzWlf3eUCDU9gQKXTdCu2dvc4hHpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکرار زیاده‌خواهی‌های آمریکا از زبان وزیر ترامپ
🔹
وزیر خزانه‌داری آمریکا در مصاحبه با فاکس‌نیوز با تکرار ادعاهای آمریکا دربارهٔ ایران، ۳ مسئله را برای «پایان کار» در مذاکرات مطرح کرد.
🔹
او در این‌باره مدعی شد: پایان کار یعنی چه؟ چون اگر تمام.کردن کار به معنای اطمینان از بازبودن تنگهٔ هرمز، گرفتن اورانیوم غنی‌شده با خلوص بالا و نداشتن سلاح هسته‌ای توسط ایران باشد، این یعنی تمام کردن کار.
🔹
این درحالی است که ایران بر حق حاکمیت خود بر تنگهٔ هرمز تأکید کرده و با تحویل اورانیوم با غنای بالا به آمریکا نیز مخالفت نموده است.
🔸
وزیر خزانه‌داری آمریکا درحالی این اظهارات را مطرح می‌کند که رسانه‌های آمریکایی سی‌ان‌ان و سی‌بی‌اس پیش از این از زیاده‌خواهی ترامپ در آخرین دور مذاکرات از طریق میانجی‌ها و «اصلاحات قابل‌توجه» در متن تفاهم‌نامه خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/439054" target="_blank">📅 19:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651087d349.mp4?token=d6YCUBj77wLgzjygvEOPt0PtBwqy3gyE22r4mKeq58GQQOCcjtEzup-xRg83jA2PPcvbDNUn6CjvXx8g4_xZkZ_3TGfiZgK9K8xwUxMvvCkaBfPdC73rHEOnsrJhTjg4uv4YJuwOiEGQooWsdcTge-ux5E7IN4UCDX7SGIT5ICiOQfypKeHXH2rDJ6CGaggflIVBV72VgzFN8OmIlaMEc5zrAytPV0bcxJMh3YnS2tJoN26qRDNoc3bMA7japX7oFY1FP-W5l-yG51Ewt5UCCdjDpBF6xy_tLYpPtHTkKp7bjlO3ajBPH1fnw9X6_EMVmlVeqN9BdaGLzr44L5pbpl3KpMUoBXzuQIE6vSxjqvsZw6BdYtHkWBNcK2sPbojgzSGV2VZAF7_Kjgghrp9_lk_k7v4WDHahEon10zmvvNntCopVgYooLVxfYHuQ7DZuC9K-SvMDiOODEunsMGmbjV8xS_hVq7PgWtM7ElBEdqYgUxfBqBzv8COmX8ZBV1sdWaErc3xVEJyV6c_kwIEDCd1i5jGEYLWeiG55rq4AnifLq5U801i-lFeL065xrTkn14Cp2gwfDDLVYVL2NlysDu2BKnolxtFBEv-_YC_2UCdqLNA56JXWtMSReUgLXGq3cOEPBCx73uCGkNP7PGHmTp_MVEBC-6wj76ntbA666QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651087d349.mp4?token=d6YCUBj77wLgzjygvEOPt0PtBwqy3gyE22r4mKeq58GQQOCcjtEzup-xRg83jA2PPcvbDNUn6CjvXx8g4_xZkZ_3TGfiZgK9K8xwUxMvvCkaBfPdC73rHEOnsrJhTjg4uv4YJuwOiEGQooWsdcTge-ux5E7IN4UCDX7SGIT5ICiOQfypKeHXH2rDJ6CGaggflIVBV72VgzFN8OmIlaMEc5zrAytPV0bcxJMh3YnS2tJoN26qRDNoc3bMA7japX7oFY1FP-W5l-yG51Ewt5UCCdjDpBF6xy_tLYpPtHTkKp7bjlO3ajBPH1fnw9X6_EMVmlVeqN9BdaGLzr44L5pbpl3KpMUoBXzuQIE6vSxjqvsZw6BdYtHkWBNcK2sPbojgzSGV2VZAF7_Kjgghrp9_lk_k7v4WDHahEon10zmvvNntCopVgYooLVxfYHuQ7DZuC9K-SvMDiOODEunsMGmbjV8xS_hVq7PgWtM7ElBEdqYgUxfBqBzv8COmX8ZBV1sdWaErc3xVEJyV6c_kwIEDCd1i5jGEYLWeiG55rq4AnifLq5U801i-lFeL065xrTkn14Cp2gwfDDLVYVL2NlysDu2BKnolxtFBEv-_YC_2UCdqLNA56JXWtMSReUgLXGq3cOEPBCx73uCGkNP7PGHmTp_MVEBC-6wj76ntbA666QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بازدید سخنگوی سپاه از خبرگزاری فارس  عکس: هادی هیربدوش @Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/439053" target="_blank">📅 19:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIRaeWAw48Cxkoh6nmtdkpZSXACaT_zNJd0XGTPbfYr1oUtR7wFRdCrB9A0xq4r8ooNcJWgsBkFU_fvPoeTovy7NcV7nIDdave8Ozzw9lF5jqrR58R8k2SuRy_eEzUvq5dryXCKKmbNSRhsHiLtYDvfZWiDoOHuTyfrQdKUfzBqVal3rMtr_3NT2iGcSgacbbivR_tGiKvtHRYagVmFEjBsjdoGzyirs1MzRHyFdAxu7i57vC4wVoYVcuWO2Svwc7MX1T-lkTct4_PBIB3BYU3gLPjqozwVBdIDRr5O9wy7w_KlCIGialY-TJvhQY6bTdlpTKkMEk8iTpEhCdvTdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8eb409d44.mp4?token=EQ_gYkuN0v2v8TsH_38EcNQ1pwHEFokj09RiDpzXLxW1Ns1nEqrpmJKHxruik7dBg6IzWaQ2qYRoNw6v3XquGzyXPLWCWG-RSWJBaxa87wSj2m9EMwHrdO44U52AjvS_qKAndKeFhY3IAXaVGX-epFWNleDOu1_SXaEhgvGbcVPSlgheM7hOz-hdF0Ripdmp6Lrb-5NyVAmsNQonaaWlMBRiOPmHtS9GsN8ISNSlPjde9GmpE46X0DYIMVWlSpfbxOhhpYquLnTgPPKB6bOWlVi_AbLVO4SAxgiJ2gksVhRKDzJUINgpRTf6wXnXlCzUXDVWM2RhL49tJVS6CIg5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8eb409d44.mp4?token=EQ_gYkuN0v2v8TsH_38EcNQ1pwHEFokj09RiDpzXLxW1Ns1nEqrpmJKHxruik7dBg6IzWaQ2qYRoNw6v3XquGzyXPLWCWG-RSWJBaxa87wSj2m9EMwHrdO44U52AjvS_qKAndKeFhY3IAXaVGX-epFWNleDOu1_SXaEhgvGbcVPSlgheM7hOz-hdF0Ripdmp6Lrb-5NyVAmsNQonaaWlMBRiOPmHtS9GsN8ISNSlPjde9GmpE46X0DYIMVWlSpfbxOhhpYquLnTgPPKB6bOWlVi_AbLVO4SAxgiJ2gksVhRKDzJUINgpRTf6wXnXlCzUXDVWM2RhL49tJVS6CIg5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت پهپاد حزب‌الله به یک مقر نظامی ارتش اسرائیل
🔹
وبسایت عبری حدشوت بزمان: در حمله به یک پایگاه ارتش اسرائیل در شهرک «بیت هلیل» ۵ نظامی اسرائیلی زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/439051" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLQza-_uoMqcTz9p4Z-RTwdZC9EWB9BId_VHXZgdSK1t92416aKncV9PO3DbUDLVv_9JVxy9ZWfP0wQKBi-qXS2aFBd2y2UTROW5yoaK2iVNb0VAmlYW_yLniUHXKZISnVYZR345O8Qg-W-WUwLmPQCMpgprd5ZiCAoqPKRq2C66jeptMtXryw2kc9x0DLLRT83AKRgokwdgSdvIIOzOiYOW1HZb-Zm49Kcw8RWQh6LYASj-1f0RWJQDvVLsy-tSibkvCD3sPizaHxHKJq6zDi3Siea7K8S7DqOfW_4gszW6kpd7afY5AGJvF9ytFvTAVTp1IOgSODCX436Sh8wz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رؤسای ۵ شهرک اسرائیلی با گسترش حملات حزب‌الله
🔹
رسانهٔ ‌عبری واللا:  ۵ نفر از روسای شوراهای محلی و شهرداران مناطقی که تحت تهدید مستقیم حزب‌الله قرار دارند، برای مأموریت‌ها یا بازدیدهای «غیر فوری» به خارج از این رژیم سفر کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/439050" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d41eb6ba2.mp4?token=IEZ4w6vbcR7a5fG6pAcMeVpPBE9hlrwhjLfws0OH0QfFYF3RIlPam2mjrVLMdV7sJcyRyln8z4dQhQ8SdGZ_7_x1aU-Cop-AO3kNeorJUGN2MmCpZnR-_nRIINEDxM2kvRyyHAhJXxHXPymVEhz_R9KdfIPKudeOVToLxq_up8xyVCWSygb3ziWr1U086s9YK72e4rkeANTwuROhXBtr69hnvibJXb5t6PyTwIz9GzVDtdegW6zfTOO71H_3y9Sv_BHVO8twjg-wTY7pG8Triwwsb26o4ssOEUL93aO7Q0kobWA_Xq51Owe9Xj1Kg88dKin88EgbgaqxkEUUmT2lFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d41eb6ba2.mp4?token=IEZ4w6vbcR7a5fG6pAcMeVpPBE9hlrwhjLfws0OH0QfFYF3RIlPam2mjrVLMdV7sJcyRyln8z4dQhQ8SdGZ_7_x1aU-Cop-AO3kNeorJUGN2MmCpZnR-_nRIINEDxM2kvRyyHAhJXxHXPymVEhz_R9KdfIPKudeOVToLxq_up8xyVCWSygb3ziWr1U086s9YK72e4rkeANTwuROhXBtr69hnvibJXb5t6PyTwIz9GzVDtdegW6zfTOO71H_3y9Sv_BHVO8twjg-wTY7pG8Triwwsb26o4ssOEUL93aO7Q0kobWA_Xq51Owe9Xj1Kg88dKin88EgbgaqxkEUUmT2lFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت پهپاد انتحاری حزب‌الله به خودروی ارتش اسرائیل در الجلیل در شمال فلسطین اشغالی   @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/439049" target="_blank">📅 19:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن خواهند بود.
@Sportfars</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/439048" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66ba635ed.mp4?token=rjDEJv5314R4BEPJwbuG2zWS-k9YQ3qNPOphKaPdbEx5RL5WSWuyO_t5VOahaAJaN8uyP6x6Ip58FGTyb8cimvkJs-eBpXd3jV4JRrfi0iZdH0Kd2lKAYqoSTj_L7YSnWwTCyMDEYQRZuENeAT-Ae8ya-D9fhn4xfEgOuj-SnjZ6qxsN0XLsT2IZhgAfY5UqXBY1VQ1L6SiFzCQ9Uv79HviVKQfjKh1N9sPIZylNTroOUzI4YlT3rzzDYqBKvjFVZLLE088oC3q2a4DDdM4tRoZv1t64TGriyLXhrKvY5dzZUDcY6oeE2pV718lmYWxWYIBIvLgesWQkirQfO5YPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66ba635ed.mp4?token=rjDEJv5314R4BEPJwbuG2zWS-k9YQ3qNPOphKaPdbEx5RL5WSWuyO_t5VOahaAJaN8uyP6x6Ip58FGTyb8cimvkJs-eBpXd3jV4JRrfi0iZdH0Kd2lKAYqoSTj_L7YSnWwTCyMDEYQRZuENeAT-Ae8ya-D9fhn4xfEgOuj-SnjZ6qxsN0XLsT2IZhgAfY5UqXBY1VQ1L6SiFzCQ9Uv79HviVKQfjKh1N9sPIZylNTroOUzI4YlT3rzzDYqBKvjFVZLLE088oC3q2a4DDdM4tRoZv1t64TGriyLXhrKvY5dzZUDcY6oeE2pV718lmYWxWYIBIvLgesWQkirQfO5YPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای برق‌کاری که در زمان حمله به پل B1 کار خود را ترک نکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/439047" target="_blank">📅 19:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ac1caf9e.mp4?token=jiLX7UwPY6IV5OcJiyGdgIhAnBZKiobILUptYysDbz_oPyRe7OHKaERMyb_gSM4NorBsKIsorXW0v41z1MqVd4npQXdRllddPHvzajp8OuFk9NLxhO-VvwqzcGf9cVgLYI2tiCSDn_YDJrODz0boLx9HCr-zGrc_YVcdn3JKQ9r5wk1kcIBF_g6mx5CAM4xFcdu79ZlZCF3tbJA4ZKyUK45rb6SFRRcg2xI3LVBW61HN0pJuJhpeQVzucuPuHESdCqhj6AURtf6efAmMvnaXlFmOtBSejvxGWz8OuWId6Oi6vZEfgtbWUjW3GxCGGW6DRtdBWBmW2uyg0KJ6d5mE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ac1caf9e.mp4?token=jiLX7UwPY6IV5OcJiyGdgIhAnBZKiobILUptYysDbz_oPyRe7OHKaERMyb_gSM4NorBsKIsorXW0v41z1MqVd4npQXdRllddPHvzajp8OuFk9NLxhO-VvwqzcGf9cVgLYI2tiCSDn_YDJrODz0boLx9HCr-zGrc_YVcdn3JKQ9r5wk1kcIBF_g6mx5CAM4xFcdu79ZlZCF3tbJA4ZKyUK45rb6SFRRcg2xI3LVBW61HN0pJuJhpeQVzucuPuHESdCqhj6AURtf6efAmMvnaXlFmOtBSejvxGWz8OuWId6Oi6vZEfgtbWUjW3GxCGGW6DRtdBWBmW2uyg0KJ6d5mE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع ۳ نفره که هزار نفره شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/439046" target="_blank">📅 18:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439045">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eef00ec67.mp4?token=FJ6fQrnRrGCX5RY4ZoXMEtGj_a-n6Z4ecCmrLDh6O1-a3SyPUPiFLrw7egsdbhZWuSr0AiZbCTr4fF3C6fQryPvQ9aeP-7LgrWC_1LsvsmgcOX9V7uBStz7HA-YzjEtLrr2F089II2nxRahpNGEKbBhRCsAfFQpIH-WCosOQVnUvUImupI2H1kt4Xk7cq3R0GWFa9oT5lVYnPaN5wTQEqr8LO1ZrWmWWPLmQcCn_bEVSeXouozVq0AsDnvwwIIX1n9mcJsdhq5l8NY9EWZF9IxGFqr7udo3kU4-Y7g2L0wHhOrJcZfdLmfZMn4Yu1UDO4SmDcXqIST-AZHJNmBQ9jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eef00ec67.mp4?token=FJ6fQrnRrGCX5RY4ZoXMEtGj_a-n6Z4ecCmrLDh6O1-a3SyPUPiFLrw7egsdbhZWuSr0AiZbCTr4fF3C6fQryPvQ9aeP-7LgrWC_1LsvsmgcOX9V7uBStz7HA-YzjEtLrr2F089II2nxRahpNGEKbBhRCsAfFQpIH-WCosOQVnUvUImupI2H1kt4Xk7cq3R0GWFa9oT5lVYnPaN5wTQEqr8LO1ZrWmWWPLmQcCn_bEVSeXouozVq0AsDnvwwIIX1n9mcJsdhq5l8NY9EWZF9IxGFqr7udo3kU4-Y7g2L0wHhOrJcZfdLmfZMn4Yu1UDO4SmDcXqIST-AZHJNmBQ9jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما نیز می‌توانید سفره‌دار مهمانی بزرگ غدیر باشید
🔹
در هر شهری که هستید، در مهمانی‌های کیلومتری غدیر و اگر در تهران حضور دارید، در جشن ۱۰ کیلومتری غدیر، با هر میزان توان و وسعی که دارید، حتی با تهیه یک لقمه ساده، در اطعام جمعیت میلیونی مهمانان غدیر سهیم شوید.
🔹
برای ثبت‌نام و پیوستن به پویش «لقمه میلیونی» از طریق راه‌های زیر اقدام کنید:
ghadiryar.ir
ارسال عدد ۱ به ۳۰۰۰۶۰۳۰
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/439045" target="_blank">📅 18:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439038">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNtm6uwUvH-H9B9ftVr1xxflJ2204Jv9F399JybprNaXaRjJVm-cNlMEZRRcM-IXkDQtIMWj_XkHuRdgfajkxB_-1EhIuWYKhi6VdfzER3AR5O-RxF8UtxoFc-5fe0-6qbLdiXicLOCSUjrIpQB4WFe-2bR-aVjPjoUtfotUv6vzwoend2FLMTo1DFnQ9PuBfNzHoCGTaRxkv9JwrcfWcj4oozUGDYrfVS5OEyMS7d8As3A8O6H2oo79qBBwWc6H_F5R5b8pm0RL1FBGzwZn6_A9EzPeUXhn_Eae0BySUa4fS5TAaWiuV9g8HTVA54rh0iz6_u14QvljiDYczTOKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuI6YZHLxoqRk9N-UKlccLFwsVFmoyyLQcQEauKmCGEilVH5ba9zlzAaoyXir9vBsH1KB2ddopEf6NkTPnK3Eb6PM9By0jpWa4hxiz6QXpsK-TJr9544ZM6QHVgKOitjuXCbWeKtrTLrbZWycNPZ3CM9DfiukShpi46TBMJAte5sV_pGOW9ILK_TAwUCtPv64TA41fObDUs9NepRlVWS2nlBfXCMqhhIQdBwkU0KE89Iu6W9HpZekSa0IEaU0aS0XAoI4fHJddWQdQEMroj2UmOtHQ5Ai8oR3ipXrnRL5b3wNZgPVBzo_nTMAMSe0y-SS2QWFuh8_L8sN_hhHeVjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAa3zzVmRJRuLBXlV-7fJ3HKeawAJnCZNCHqghSnMGj5gtk5l9UWwgYFJh8UY6X91LvluFcuwZZ3BJ8u_YM-T_6xbDzjNZogYoWMDK-0VLFXvfFCHnlZ8U8ttQ3rpaIOMt2Tc90j58bz_ksB_6AaO-PEqS8uoEit7FOx0ZtYJtQ71f-iiQAaLwJodROkPol4eu0gJkZkKlv4kHWYDt8G0P5BTCaAcuD8vp2-BgzeZHyZM_Q4cxlKMULSrXXE7YuSPpSNUP4CKq6u8Y8OoSPn1SNICYHeAZVeiaTDrDLqa2JMaadur8swgi3Wa_3wflCRlqxMh65uJk8AD4yapYsGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fl7mhTVKsvrNcVfLyz_slL7YLmG7De0BmCGcru-B-YtHghA-chThzK8HEOX3DtCTZEp91J_VXscH_-o0fbTM6Rvtdwqn7z_JlpgnarMB1OdeNyM89vvpCC9OtRIk3GoVEFX173GmC0by4XM5UyFFcZc5RkggP5iZQrVIZAI05Ixv4Yj_7E-2d6JJIZ29wqwQ92wOsdHVvNGzy48m00ymiS1JzskShwKTjTo_KoIAwgJ2dYaOskoewubif6imzgVsEOjEWm2IiuJB6KOPsFk_vL1gXVpnHVMWL_4ZiK_Bq63JwoafGcPNkcdbp9bHbi2qeR3M9vS8ObhgqhPghQ_APw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzY7J4HLQv7GxRLOiMiaIWT62vkLI6tK4iW4_X3yxVQNAotDqgC_ZyTzE3Xo6ni9lDyfAVBoDKZikmWoWPM5mIKI4x9AM0GI1XODjYx6VseLyDfafm81O8cy7I8bQEJ7ui_ZRKS2uZ02mJxIeHeGSH_PQofIzFFQKrrHx9B8i-x7Npj0EO5RLSb2FowfnQjGVL6bslcqlu_ed3N-hejk4scsyEV7-jiFNJ2mhSkeWQ_N-2U5ONEQ6Tla5jAPpepoVsA4eNFZKWUaDGKORinwF8nuOFparWF1fYHVieBfShRezkf398hSQt6cna917Q3nWJ8IG_ZGf5C8tZXzLrIEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOXQJItWGi5oVqPYrb1EOZ6k66ds5qi52roWax6zXzTnOWTO_Qyr7AuBhjHbQG3KKb38Lsk1dzd_b1w860bolfucnndosM2IrEs1g8Gh_AEyRamApC8_gv6UkuPBWb9zzgDz1uTi2YfGPGzzQ_ZVuF2S2mhsixeggGClpqsJTb_Ff-PDZrvLTed7oZsZ_DQLQf6wUR5Tf80_-hH9vPtP3O_kFWFOpmhuD_EZlSL6wDJHbwaAMIJrJrALBsrlmGoDALRaSnnPb3VAuCi1ZPK8w_DToakOVoLhlF3zbj6nHsX--67yhd0-XjYygsahkPxe9D0NSpDnB4-BOUW1tY27oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O09wR69YRyRDeB0Tjm0PvxRg4eASDEMXSVP0-rM8EiIgbBI4JJd-FRD5T4jTPyuZUdYhd45gASMVoBb2_PlkPl7GRq19pJYbNJCWZSwG48x2WwsOjdiyi83zF9oMBoYyeqO7tv3VfDDcXle28EeRP0rLBiDLh0dxJtVwS9BVQRoeSkcsyX-isItxfbpHnllue26zPsaYpE1t0dBTergQ7OPQjwr-0dOgygY6ned1TgUrKLhh3Bj9C7O7wzi6UvEcGI3HP4F5eIoVN5ybE6l_ed41Mmzk-t4qdLDlZzt-yLe8JPhf-tXP3C8X66KYaN8-iKVRwGk6yJh0vlqM7t6aQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید سخنگوی سپاه از خبرگزاری فارس
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/439038" target="_blank">📅 18:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439037">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5bb3d4e6.mp4?token=v2XFZuOAB714eyG61eb1IWUXk9guMoZCb9FgAPOffLHQww2jIIcELkecM3nF8XSs0SwwH7gCBk0FneQPVbvzl8rNxqaggYvHPjnvv0P3685du_sDSpc5WCCwAUut1puICQq8Blp0MGUojMJSQLwCCiUNLG_IegPHdZsdHYb79LrU8DDsNkeJhaGT_BApoPR0hUxBz5wjMjzTY8CZtkp2eBoXaZ6hwFQ46o2Ai6Lx7YGt38UZtHGpkWfUSK0V6vwDbnwKHkJKkvxSx2QJkzrujXV3IUsKrsEZDNFq7gSSg86M4EMQuJFgCM8qiROooWu7WwZCOYsfGtfsJ63KkH_NrCa2RAc9KMcYhYjg5Hxicp6MrOboJeciI63nrKF8HZnaqvi0CpqkBtfRwUuQmPQYGxnBfoDMsJNDuakFKn7e1TfdVPmlmm8BoDKT3vAKAkdA52FdsZKTJJJXXGFERG05amcQxjuk7L5335pLz_IBGVUweygcSkC5Rqd6epbl6ZTg-L0gEz_7uNFKYoi4jzTYcN5mgq7R9UoLRIVMjwM4R-lj1vwvWey0GTycw2GxpBw7Im0iIqMrwFTLa_gcXEiKDxqAM9ILJRgVfJX0eMENM3rbAmw3rKUfnWRNfRk3QYK2e5SYr4e1-7ZA750mcCrTCix1PW5HLNXNP4-RuXQDMZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5bb3d4e6.mp4?token=v2XFZuOAB714eyG61eb1IWUXk9guMoZCb9FgAPOffLHQww2jIIcELkecM3nF8XSs0SwwH7gCBk0FneQPVbvzl8rNxqaggYvHPjnvv0P3685du_sDSpc5WCCwAUut1puICQq8Blp0MGUojMJSQLwCCiUNLG_IegPHdZsdHYb79LrU8DDsNkeJhaGT_BApoPR0hUxBz5wjMjzTY8CZtkp2eBoXaZ6hwFQ46o2Ai6Lx7YGt38UZtHGpkWfUSK0V6vwDbnwKHkJKkvxSx2QJkzrujXV3IUsKrsEZDNFq7gSSg86M4EMQuJFgCM8qiROooWu7WwZCOYsfGtfsJ63KkH_NrCa2RAc9KMcYhYjg5Hxicp6MrOboJeciI63nrKF8HZnaqvi0CpqkBtfRwUuQmPQYGxnBfoDMsJNDuakFKn7e1TfdVPmlmm8BoDKT3vAKAkdA52FdsZKTJJJXXGFERG05amcQxjuk7L5335pLz_IBGVUweygcSkC5Rqd6epbl6ZTg-L0gEz_7uNFKYoi4jzTYcN5mgq7R9UoLRIVMjwM4R-lj1vwvWey0GTycw2GxpBw7Im0iIqMrwFTLa_gcXEiKDxqAM9ILJRgVfJX0eMENM3rbAmw3rKUfnWRNfRk3QYK2e5SYr4e1-7ZA750mcCrTCix1PW5HLNXNP4-RuXQDMZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسول نجفیان، بازیگر: خائنین در شاهنامه همگی نابود می‌شوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/439037" target="_blank">📅 18:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83bb02bb85.mp4?token=I94HjAGGN7y_-0QGPda5En6Xqc9SC1poXDaNz04_A4k16QsgO94G7z7EAcS2awPhnT0xBI3ZA2eOOSBLPoWbMitMnqXJQgAM2E40btIQuPnR-yJtH5ucWYjj10NUCba9IE4nOFBfihzPcE5GiHjcW6mkC_O1--Nn-IwLYnYhmZvzUI11g_I5BXIahDASS2BopQtKaX79p_JG_lOjS91CVul0nEffogfVmr2IcQcMDAXfMLacUaPhwQp07zP1PKeySJTRk5qcqpKbhEQ8rKwSN78OOIWgwphnI0MgSwoqAwQHPMo_qdZ4YezGeg0hPyKj4tP2n5xZ-BpSapIFM6HRIUSCkRF2crfiRleu0-AY1rNg3d-n9PcMBsobpX6wK2-d8x55B5Tnv8PxhCmxQ79xlrDe9Lbmmcs2PT6y6vK9-_ug-mEmEK7jNBGu84nZ1P2vztoMEQ4vGnzlvRJgZyzHmr2poX-7i97UMMbCcChOk82QvTdfYhZEKhAqa52ojkfSmJaiW-LEH6A8sa1l0CO8HeotSP9IS8e53BJC_MHSvW4rT7C0JhevDB-RpvuZzaz7YhdSzVXwWwJ3HO05HJpODm0Yz7Ij8NpY1KFhV92ngOI3efGbCETkzNzOQien2yvWv8mzbdEsM7u4ZdLeKLT2XT2ZgtLtV6gdZMcWgE8hTF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83bb02bb85.mp4?token=I94HjAGGN7y_-0QGPda5En6Xqc9SC1poXDaNz04_A4k16QsgO94G7z7EAcS2awPhnT0xBI3ZA2eOOSBLPoWbMitMnqXJQgAM2E40btIQuPnR-yJtH5ucWYjj10NUCba9IE4nOFBfihzPcE5GiHjcW6mkC_O1--Nn-IwLYnYhmZvzUI11g_I5BXIahDASS2BopQtKaX79p_JG_lOjS91CVul0nEffogfVmr2IcQcMDAXfMLacUaPhwQp07zP1PKeySJTRk5qcqpKbhEQ8rKwSN78OOIWgwphnI0MgSwoqAwQHPMo_qdZ4YezGeg0hPyKj4tP2n5xZ-BpSapIFM6HRIUSCkRF2crfiRleu0-AY1rNg3d-n9PcMBsobpX6wK2-d8x55B5Tnv8PxhCmxQ79xlrDe9Lbmmcs2PT6y6vK9-_ug-mEmEK7jNBGu84nZ1P2vztoMEQ4vGnzlvRJgZyzHmr2poX-7i97UMMbCcChOk82QvTdfYhZEKhAqa52ojkfSmJaiW-LEH6A8sa1l0CO8HeotSP9IS8e53BJC_MHSvW4rT7C0JhevDB-RpvuZzaz7YhdSzVXwWwJ3HO05HJpODm0Yz7Ij8NpY1KFhV92ngOI3efGbCETkzNzOQien2yvWv8mzbdEsM7u4ZdLeKLT2XT2ZgtLtV6gdZMcWgE8hTF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناکامی‌های آمریکا در جنگ تحمیلی سوم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/439036" target="_blank">📅 18:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439035">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8847b20aea.mp4?token=NasFRiLu4XMIeLdbUQmgYG4__yvOBZ8srr26FyXEqfOT1E8BBtGLFM_z-QSjfV656MNYBebGvmHXl-V8P40urd2gnMhL20M4NiN_fHERWNBTIPzBc-3a_xtqC3B-Km-1dlNVuKj6j7uCdTeIbC8cqCer5Fh9Ensot5z0HSjpDyypvPWcr3edZMZADpwSokc4-GeNa4pNmbkI4O0-8K-TNvRn2jG4a7zwXbbfDlhhVRE2Mg5BxX9G1WyaOLX9aJmh_6ddGWu-eWzTibMwvLs3pvaeSaAIsbuR1akfaXEFygsi3t05gIJJTz4RGEpm8hCVwFbvOwaPQyDjvcBmIcGn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8847b20aea.mp4?token=NasFRiLu4XMIeLdbUQmgYG4__yvOBZ8srr26FyXEqfOT1E8BBtGLFM_z-QSjfV656MNYBebGvmHXl-V8P40urd2gnMhL20M4NiN_fHERWNBTIPzBc-3a_xtqC3B-Km-1dlNVuKj6j7uCdTeIbC8cqCer5Fh9Ensot5z0HSjpDyypvPWcr3edZMZADpwSokc4-GeNa4pNmbkI4O0-8K-TNvRn2jG4a7zwXbbfDlhhVRE2Mg5BxX9G1WyaOLX9aJmh_6ddGWu-eWzTibMwvLs3pvaeSaAIsbuR1akfaXEFygsi3t05gIJJTz4RGEpm8hCVwFbvOwaPQyDjvcBmIcGn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین ویدیو از خلبانِ شهیدِ جنگ رمضان قبل از شروع ماموریت
🔸
شهید جابر طاهریان از شهدای جنگ تحمیلی سوم است؛ که در ۷ فروردین به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/439035" target="_blank">📅 18:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439034">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54e4849a3.mp4?token=oXX0fajICprh7yn_rnKEjVV1X9eQRS_P0GPSD22Fo5E2dyE5hlxqYHEKvCLkBkynsLs0VrF40JcdL_lOS-_Yl6V0W1mJx2qXI3kNbsBqsVRz4IpZ6V_B-uDXstgbDcv66z6dZMeCtH20-vFrE6Aku0bKWSKLTmIPc5OUl7N3MFK9sGymgghrlq7CGcX9rwdXG_AWl_ugFnLjzgAXH-0R50SR2380gMXU6ZLNeWWc6SG-UvdOS7hPuv3-6Dx1vrHHfPxNMNSegKYzUGmbA-UvyPydTYxS9liqJm5NvQfF_KKp5GywDABeghCkIA1Ad8S0VRare01Q06tpRrqEwgK1CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54e4849a3.mp4?token=oXX0fajICprh7yn_rnKEjVV1X9eQRS_P0GPSD22Fo5E2dyE5hlxqYHEKvCLkBkynsLs0VrF40JcdL_lOS-_Yl6V0W1mJx2qXI3kNbsBqsVRz4IpZ6V_B-uDXstgbDcv66z6dZMeCtH20-vFrE6Aku0bKWSKLTmIPc5OUl7N3MFK9sGymgghrlq7CGcX9rwdXG_AWl_ugFnLjzgAXH-0R50SR2380gMXU6ZLNeWWc6SG-UvdOS7hPuv3-6Dx1vrHHfPxNMNSegKYzUGmbA-UvyPydTYxS9liqJm5NvQfF_KKp5GywDABeghCkIA1Ad8S0VRare01Q06tpRrqEwgK1CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امارات بازندهٔ رقابت کریدورها شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/439034" target="_blank">📅 18:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439033">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yuiz7OBjF8dgQMOwYP5QmDmfE0mtekdQpV9sxtJEk8iglLW6bkOk_vInCJ-2PREM6VW9MlSXHYWwpbb3G9g5S5_S1GshglFu8dX9LDMKHIUCK-MoywYbJPMP3uBE-ViMiJ8W4MN2F2W__Zihsw4tdkaNoTgeI4iYTSqej3KLOi0ju76Nzu9WzsSsEH29wQxrZl6FqtuEsLj4Xsyqg_tdBBFWocAImFqdXzPTsLWxKof09ir2Hyo1Jc6vppVCku26AhDp2Cv6RmkQdfx_eos6uxUqMLYLVKNMKmRQefKn6WBCGJayTbnRZuuQNkQjHxg_I6KgjgDAJSEOF7miWtAztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ سکوی پارس جنوبی به مدار تولید بازگشت
🔹
مدیرعامل شرکت نفت‌وگاز پارس: بازیابی ظرفیت تولید و فرآورش گاز غنی در میدان مشترک پارس جنوبی با اتکا به توان فنی داخلی روند مطلوبی دارد و تاکنون ۳ سکوی فراساحلی پارس جنوبی به مدار تولید بازگشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/439033" target="_blank">📅 18:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439032">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE6PM-Zc7-pxdtzsVVQsag-6tXUAyk8gRE5iM8v7Jsqt_MnmXlvLzZ1zsafbkdr1lsRpKyMpqRpU26rX3UtBUBybeL9XCi2sKFKtIyy7MR8eWCZ4MdfpOMohB4YrIJFpjDL_9ilUrQjUXlGT8ZLClgi1ectoxzZ-Q8fkQ5OQ8YurybQ8gGlW5B6wL2IeNORalJEwBmrfbTcxKCcu8JnthZ9MvqfrO7HpuTsSxJ7iD67hPS-qorebJzR31Utek24HFNx84TBMDSwgkcEz58IAKvQc_M-xSryvCFF6M06mL7jrIpIjZoRThOXuqjAJGBdeNN7BVpuS8tFX5hMfe8ggCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فراخوان پانزدهمین دوره
#جشنواره_بین‌المللی_فیلم_۱۰۰
منتشر شد
🔸
این دوره از جشنواره در بخش‌های «
نبرد برای آینده
»، «
نبرد برای کودکان جهان
» و «
نبرد برای وطن
» برگزار می‌شود.
🔸
آثار کوتاه برای راه‌یابی به سه بخش جشنواره باید
حداکثر ۱۰۰ ثانیه
باشند. تنها در بخش «نبرد برای وطن»، آثار
تا سقف ۳۰۰ ثانیه
نیز امکان حضور خواهند داشت.
🔸
مهلت ارسال آثار به جشنواره فیلم ۱۰۰ تا پایان روز
دهم مرداد ماه
بوده و زمان برگزاری جشنواره نیز
شهریور ماه
است.
🔸
پانزدهمین دوره این جشنواره به دبیری
#محدثه_پیرهادی
، شهریور ماه ۱۴۰۵ برگزار می‌شود.
📰
جزئیات بیشتر و نحوه ارسال اثر به جشنواره را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/439032" target="_blank">📅 18:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439031">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">🎬
#تماشا_کنید
🙏
دکتراخلاقی در نشست بررسی راهکارهای گسترش تأمین مالی غیرنقد عنوان کرد:
✨
بانک تجارت با تکیه بر تأمین مالی زنجیره‌ای و به‌کارگیری ترکیب ابزارهای نوین، آماده همراهی با مسیر جدید تأمین مالی کشور است.
💠
دکتر اخلاقی با تأکید بر ضرورت عبور از الگوهای سنتی و حرکت به سمت ابزارهای نوین مالی، گفت: بانک تجارت با ظرفیت بالای تأمین مالی گسترده و بهره‌گیری هم‌زمان از ترکیب ابزارها، می‌تواند نقش مؤثری در هدایت منابع به سمت تولید و پایداری بنگاه‌های اقتصادی ایفا کند.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/439031" target="_blank">📅 18:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439030">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/439030" target="_blank">📅 18:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439029">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-52.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/439029" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-50.pdf</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/439029" target="_blank">📅 18:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439028">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌
🔴
پزشکیان: اگر می‌خواهیم ایران با عزت، اقتدار و ثبات مسیر پیشرفت خود را ادامه دهد، باید همۀ ظرفیت‌های کشور را به میدان بیاوریم
🔹
ادارۀ کشور صرفاً با اتکا به گروهی محدود از مدیران و مسئولان امکان‌پذیر نیست. همه اقشار، نهادها، گروه‌های اجتماعی، نخبگان، فعالان…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/439028" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439027">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌
🔴
پزشکیان: مسئولان کشور باید در کنار مردم، در متن مسائل و چالش‌ها حضور داشته باشند
🔹
مدیریت کشور در شرایط دشوار نیازمند حضور میدانی، مسئولیت‌پذیری و همراهی با مردم است. اگر مردم با دشواری‌ها مواجه باشند، مدیران نیز باید در کنار آنان حضور داشته باشند و برای…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439027" target="_blank">📅 18:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439026">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
پزشکیان: جان و مسئولیت ما از رهبر عزیز و شهید و مردمی که در راه دفاع از کشور و آرمان‌های خود جانشان را فدا کرده‌اند، بالاتر نیست
🔹
آنچه اهمیت دارد حضور در میدان، پذیرش مسئولیت و ایستادگی در کنار مردم است. @Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/439026" target="_blank">📅 18:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439025">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت و مسئولان کشور خود را برای هر شرایطی، اعم از استمرار مقاومت و تحمل دشواری‌ها یا پرداخت بالاترین هزینه‌ها در مسیر دفاع از عزت و منافع ملی، آماده می‌دانند. @Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/439025" target="_blank">📅 18:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439024">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
پزشکیان: خدمات‌رسانی دولت در هر شرایطی ادامه خواهد داشت
🔹
دولت با تمام توان و ظرفیت خود مسیر خدمت به مردم را ادامه خواهد داد و ادارۀ امور کشور با قدرت و صلابت دنبال خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/439024" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439023">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
پزشکیان: دولت درحال برنامه‌ریزی برای تحولات پیش‌بینی‌نشده است
🔹
عبور از فصل تابستان ممکن است با مدیریت‌های کوتاه‌مدت امکان‌پذیر باشد، اما برای ماه‌های آینده و به‌ویژه فصل زمستان باید از هم‌اکنون برنامه‌ریزی دقیق و آینده‌نگرانه صورت گیرد.
🔹
همچنین در صورت…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/439023" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439022">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
پزشکیان: مدیریت مصرف انرژی ضروری است
🔹
اگر در حوزه مصرف برق، گاز و سایر حامل‌های انرژی نتوانیم الگوی مصرف را اصلاح کنیم، ناگزیر بخشی از ظرفیت‌های تولیدی کشور تحت تأثیر قرار خواهد گرفت.
🔹
کاهش فعالیت واحدهای تولیدی به معنای کاهش درآمد، افزایش فشارهای اقتصادی…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/439022" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439021">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
پزشکیان: جامعه باید نسبت به الزامات و هزینه‌های مقاومت آگاه باشد
🔹
اگر قرار است کشور با اقتدار مسیر خود را ادامه دهد، باید واقعیت‌های موجود برای مردم تبیین شود و همه بخش‌های جامعه در این مسیر مشارکت داشته باشند.
🔹
رسانه ملی و دیگر رسانه‌ها در کنار تحلیل…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/439021" target="_blank">📅 17:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439020">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
پزشکیان: هیچ جامعه‌ای نمی‌تواند در شرایط رویارویی با چالش‌های بزرگ، انتظار داشته باشد که بدون تحمل سختی‌ها مسیر خود را ادامه دهد
🔹
مهم آن است که این مسیر با آگاهی، همبستگی و مشارکت عمومی طی شود. @Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/439020" target="_blank">📅 17:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439019">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
پزشکیان: مردم باید نسبت به واقعیت‌های موجود آگاهی داشته باشند
🔹
بخشی از مشکلات اقتصادی کشور ناشی از محدودیت‌های بیرونی و بخشی نیز ناشی از فشارهایی است که در نتیجه شرایط خاص کشور ایجاد شده است.
🔹
دولت و تمامی دستگاه‌های اجرایی با تمام توان در تلاش هستند…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/439019" target="_blank">📅 17:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439018">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/439018" target="_blank">📅 17:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439017">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
پزشکیان: شرایطی که کشور امروز با آن مواجه است، عادی و ساده نیست
🔹
مدیریت این شرایط نیازمند هماهنگی، همدلی، گفت‌وگو و تصمیم‌گیری‌های دقیق و مسئولانه است.
🔹
تداوم برخی محدودیت‌ها و فشارهای خارجی، به‌ویژه در حوزۀ دسترسی به منابع و ظرفیت‌های اقتصادی، پیچیدگی‌های خاصی را برای ادارۀ کشور ایجاد کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/439017" target="_blank">📅 17:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439016">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f774ef204.mp4?token=OUdW-TFK7GcAyf5qS9pR4S1fquUGRQSnhxwCfu8RGHHh-GkUpiFNNaiXD5z1tBGfsaRCmNEhZfNpPqT03lLNyM99k1yuyEJcW0q4rh_Z2YFhsQA4IY3Fn9VmBbybZN5mcll8jbTZhDxpe4yCulTGyNmAGbLewMEO8bXHOKk1-SVy_Ce7VPPiS1Pe9GGCR9203aMNtyE3Y0XGdqdz0CNgbE1MZGKYnY4RtsmA6Kx1sFHn2uUR5_TiLNua2Oh7cIgDVLso-PdWE-c-tWKNhOyEXtA0EUX10_Rqqd6wZj_jUlurM2dwekNIrMZgoV3x2bbrbEK16PrqaD0sSkbkUPnoeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f774ef204.mp4?token=OUdW-TFK7GcAyf5qS9pR4S1fquUGRQSnhxwCfu8RGHHh-GkUpiFNNaiXD5z1tBGfsaRCmNEhZfNpPqT03lLNyM99k1yuyEJcW0q4rh_Z2YFhsQA4IY3Fn9VmBbybZN5mcll8jbTZhDxpe4yCulTGyNmAGbLewMEO8bXHOKk1-SVy_Ce7VPPiS1Pe9GGCR9203aMNtyE3Y0XGdqdz0CNgbE1MZGKYnY4RtsmA6Kx1sFHn2uUR5_TiLNua2Oh7cIgDVLso-PdWE-c-tWKNhOyEXtA0EUX10_Rqqd6wZj_jUlurM2dwekNIrMZgoV3x2bbrbEK16PrqaD0sSkbkUPnoeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت پهپاد انتحاری حزب‌الله به خودروی ارتش اسرائیل در الجلیل در شمال فلسطین اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/439016" target="_blank">📅 17:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439015">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onbEIwAWVNTZIX6dMw2bfm3D579EGRIgQVlmC8mo7Reoz8V9hsdebTno7Gk6xFimG9tzkiq6FPgQIehj7BsjB6vZhL0QcrwAm34XjzOIEpF4VUB8ribE0ioSssmsp_E2yxr-l8Skw4HREowDqBA4gmbEVIJyrwScfJyTZHWHUO5-XlO1Iu00c850pW-6J61QQqep1MbEOe15N2a_PSGuAbFzfGyAz_zV5tSGnbK6qUR8UeSwCFUnM8js2BYa_gSemoYk2rWZxgXBSoHTKTZS506Yg2JEkGkhK3ATrPU6aq0mVHMLlmq6qXrjeT33FAB-B0jAs-xSHCMCMGpamb-KyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیعت بزرگ ایران در مهمونی ۱۰ کیلومتری
🔹
عید غدیر، عید ولایت و امامت است؛ عیدی که بر محور پذیرش ولایت شکل گرفته است.
🔹
ولایت، یعنی پیوندی آگاهانه، عمیق و استوار با امام جامعه. پیوندی که در میان مردم ایران ریشه‌دار و مستحکم است، هرچند ممکن است در برخی بخش‌های حاکمیت هنوز به استحکام مطلوب نرسیده باشد.
🔹
جشن‌های کیلومتری غدیر امسال، جلوه‌ای از بیعت بزرگ مردم ایران با ولی‌امر خود، امام سیدمجتبی خامنه‌ای است.
🔹
تجربه تلخ تنهایی امیرالمؤمنین(ع) در ۱۴۰۰ سال پیش، نباید تکرار شود. از همین رو، مهمونی ۱۰ کیلومتری غدیر امسال بیش از هر زمان دیگری اهمیت و معنا پیدا کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/439015" target="_blank">📅 17:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439014">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=c96kowPVj-trPATXmwPkrzRxMVPi8DYiuC5lBI_HFNje8K8sE4HTQB-zribNdbRAcyy7tQiC0bjf36d5jeAfBUNw4OR-YWj_b3zF3T2PuSzaAlS2qClScT2UYBUDaMuoG19-KwJC9eTGodLohLgjegeb-shBqNQoLWjl3UJr3MI15OinA7tt8NduAU3pe35oe9-Hqcs88c-06tWjv7ekB-QkiVnYOXC6en8iH5JLHK1QTvvz2UAAtmQCDdHEXAgL00D_PPXq27HznkByDWEjVXNEajOt51Xw9Cqj72REH_lO_S03sKp85PEmLd5APzPr-9nNhg04it4uy9WHZLgr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae626b6d9b.mp4?token=c96kowPVj-trPATXmwPkrzRxMVPi8DYiuC5lBI_HFNje8K8sE4HTQB-zribNdbRAcyy7tQiC0bjf36d5jeAfBUNw4OR-YWj_b3zF3T2PuSzaAlS2qClScT2UYBUDaMuoG19-KwJC9eTGodLohLgjegeb-shBqNQoLWjl3UJr3MI15OinA7tt8NduAU3pe35oe9-Hqcs88c-06tWjv7ekB-QkiVnYOXC6en8iH5JLHK1QTvvz2UAAtmQCDdHEXAgL00D_PPXq27HznkByDWEjVXNEajOt51Xw9Cqj72REH_lO_S03sKp85PEmLd5APzPr-9nNhg04it4uy9WHZLgr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: همهٔ کسانی‌که درگیر مذاکرات هستند، آدم‌هایی‌اند که میدان را به‌خوبی درک می‌کنند
🔹
آقای قالیباف فرمانده میدان بوده‌اند و آقای عراقچی رزمندۀ زمان جنگ.
🔹
نیروهای مسلح دست‌به‌ماشه هستند و تیم دیپلماسی با همین نگاه مذاکرات را دنبال می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/439014" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af89c9ac9c.mp4?token=p-Q0nu5LcGCAgzBSkE6RDE_vHRptyzxhxwLhMLViXm79EAaYNsvdWvRz-b68vMnylV_Jtxlp5hJo87xJvKHckLcx-R-GnGWLzU4FxoMD3x46-v2tmFRGzCSFSxfveQoU9rf4KMja73ehwqzGO2-ctbBPmw6-Xla4QYWaSa2NEf2PKpC_uEDjc-SX0KDmOW6UPu1cf-8dMOSiofbS8KliFjsOinUPiestt_YnnAfe1tqs5LiC-I_9eVwolbQrmrRA5gu17L03EMmj8ijQGaU-dBk4ywp_OgxMNBZ8Za6iccWI92gReUrdeSEt2USEWRYanKvICfYBLCbKhFDdRCyvuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af89c9ac9c.mp4?token=p-Q0nu5LcGCAgzBSkE6RDE_vHRptyzxhxwLhMLViXm79EAaYNsvdWvRz-b68vMnylV_Jtxlp5hJo87xJvKHckLcx-R-GnGWLzU4FxoMD3x46-v2tmFRGzCSFSxfveQoU9rf4KMja73ehwqzGO2-ctbBPmw6-Xla4QYWaSa2NEf2PKpC_uEDjc-SX0KDmOW6UPu1cf-8dMOSiofbS8KliFjsOinUPiestt_YnnAfe1tqs5LiC-I_9eVwolbQrmrRA5gu17L03EMmj8ijQGaU-dBk4ywp_OgxMNBZ8Za6iccWI92gReUrdeSEt2USEWRYanKvICfYBLCbKhFDdRCyvuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
🔹
افزایش مبلغ کالابرگ جزو مطلوبات دولت است اما واقعیت این است که باید خواسته‌ها را با داشته‌ها هماهنگ کنیم.
🔹
باید در این زمینه، مطلوب را با مقدور هماهنگ کنیم. باید بررسی‌ها انجام شود و امیدوار هستیم که…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/439013" target="_blank">📅 17:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی دولت:‌ افزایش مبلغ کالابرگ در دست بررسی است
🔹
یکی از مهم‌ترین وظایف دولت‌ها این است که تورم را مهار کنند؛ این کار را با نظم مالی و بودجه‌ای که دولت پیشه کرده است دنبال می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/439012" target="_blank">📅 17:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag4hHsJKEIDqbWFbSaGO0o-ANpenZfnRLDfJoxF-3p1_0CpNOWwJ-eM1V35kSePTrAPhknQTfgJ9G9snpKCzEnI7EKoKRlCVnLsWLQdfbfoWEm0sCnXZqOjWC02bo4gvJ3i77LJ9N58mHVlmLc9dfrW5DxpQSJN6Vt3trSCecYmCT-d2D_guChUdojvwfzy2Oso-3g9F7CrI_g2vpMJbgyNRSsWb1UUz1oD8qMe2Bk7Oi7Xz2tqMTkqFoOJlvc0F3bIE7QE_iNQplutNw8pndsr5AxIr_wcaVtUZXkErg9tQ1x-kTZhQaR0XBoMnc9GqEdQUXyFISdAOEYKki-JWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم ترانزیت کالا به ۲۰.۵ میلیون تن رسید
🔹
براساس جدیدترین آمار گمرک، در سال ۱۴۰۴ مجموع ترانزیت کالا از طریق ایران به ۲۰ میلیون و ۵۱۶ هزار تن رسید که نسبت به ۲ سال قبل خود افزایش نشان می‌دهد.
🔹
عمدهٔ ترانزیت کشور از مسیر ریلی و سپس جاده‌ای انجام می‌شود که کالاهای هند از مسیر ایران به کشورهای ارمنستان، ترکیه و آذربایجان منتقل می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/439011" target="_blank">📅 16:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9894ffd5.mp4?token=SR5W_f86Ul5W5K4dTaYfXaleEUtRPBvNjqAaJ2k93VheIs7YUypoga9-4kfcCiyCr6GkYz4NsczpxUNwYvEjW5Gp0IFYh38O3C08masRt9y9onlFsemp0lOb6rpjUJ7Hx8fclywXP5ASp47nx9rsHAo9pZsYsbYqIsTXO3KLttvZ2L1pXntZQVQR4oFd084WcOWIFuthN1n5dW4i06K-jgzNKjycMtl9AKWkmAlQfWJeKwT9TTJiDgv3x4UoqWMUDCMnyCo_Gb2Kw4XW3sC_QII7iVYryS-DYSVyOF5sNdYAPW0486qjoq_KrS4cGPEYVd4rb_D0wiEGVR9JNmfw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9894ffd5.mp4?token=SR5W_f86Ul5W5K4dTaYfXaleEUtRPBvNjqAaJ2k93VheIs7YUypoga9-4kfcCiyCr6GkYz4NsczpxUNwYvEjW5Gp0IFYh38O3C08masRt9y9onlFsemp0lOb6rpjUJ7Hx8fclywXP5ASp47nx9rsHAo9pZsYsbYqIsTXO3KLttvZ2L1pXntZQVQR4oFd084WcOWIFuthN1n5dW4i06K-jgzNKjycMtl9AKWkmAlQfWJeKwT9TTJiDgv3x4UoqWMUDCMnyCo_Gb2Kw4XW3sC_QII7iVYryS-DYSVyOF5sNdYAPW0486qjoq_KrS4cGPEYVd4rb_D0wiEGVR9JNmfw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات جنگنده‌های اسرائیلی به یک بیمارستان در جنوب لبنان
🔹
وزارت بهداشت لبنان خبر داد در جریان حملات هوایی اسرائیل به شهر «صور»، ۱۳ نفر از کادر درمان یکی از بیمارستان‌های این شهر زخمی شدند.
🔹
در حال حاضر، حملات هوایی صهیونیست‌ها به «النبطیه» در جنوب لبنان،…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/439009" target="_blank">📅 16:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439008">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کشف محمولۀ تجهیزات ضدامنیتی اپتیکی در منطقۀ مرزی ارومیه
🔹
قرارگاه حمزه سیدالشهدا نیروی زمینی سپاه: محمولۀ تجهیزات اپتیکی شامل مقادیر قابل توجهی انواع دوربین‌های پیشرفته و تجهیزات شناسایی با کاربردهای نظامی از گروهک‌های تجزیه‌طلب در روستاهای مرزی ارومیه کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439008" target="_blank">📅 16:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439001">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBjFuuU-Z2V7xvqvBFj9MAddVd1L-RFNWaO8GY-tlBBaYsdlSLn_FamQfzWPifnQgIigrnH8_Qh6dsQzUoF4OFvhnoz0gIlpavrMjozTDGglpEa6KhqwUTDdCFGBwKUUXeLG3JEBcL097uTQpBltQ7WVW73NXBu7rGT3YjP83IBrblPLDrLMWDtAi8ictPj4F4s2eSzbMyFnKfJNeXJEeiMjknTBLvqTaJAUx23514JtWOEi-ZO_GJWXqp9NZK1FNn-5gGtxUjDCI5XbF0x6Zv-ntu3EWZqg-7ZKMW5K3T1Y0ScVv2escFHh6f9cW5nysaPSbBGBUK5IWC608abukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTql2iDfBGMolbHJAQZnuAI_St8mEZ4h1deUAY4E2czFOph6m29owSLhTcR93-FNYMWH_LQ-VSnG54fYknnC1g9wiGAA4qI814YLxEjqYUAUctcageuDkkBLD_a1gcLKii6AGv5POeR_XdcRz_3pNAKVJF3XvRRXKBngQxrwmCUhXFNsZWQejAMnpHaMgyd4k-zwJ05ghufH9NcQfGQk7yR4431gwHxByz6fwvD2Fm22Nn8lVMzWlRm1nhUF5kc08o7kJv9Cj2Rawu9VrIN6pM_dX-hQ3dnL0OTbmh1n6XK5j2ukrmQ9dL-U73jCo2zwDCLhn8ns8cdqILBKvPEriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYrX-HeV9OQ2-T6U_z3KloYBJbVCj5lsJqURzleyT-yR-gurgTA2NWAx0_K5cA_6-c1HVXM1FHURruISrmLR1TiIExiTZJ4xaIWsTeRNYsI11ODTJGLVNNDqvplOZHdr4Wj70Rsu2dd1qKL8GtKhB4FW911LH-hZj3eu70a4TsBvyV6GIL6Y-fb_VZCEL2YYKs4-QVCrancltGpsY1a-l9eWxWdAv0hbsv3rI2HpzeD4wnGHcYC71K3DxVHxNedLtOtSvk1-qqpW9IQx55acneBI8A3GAg3rlR1-WF_l-VmB73-QUHEEPoCD4ksaZvLC8ZVxF_3hWazd_o9uV3Q_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Woci0KQLuEmCE18Sg3FjfJnpm6v1lxMAhqy8MysBcK7Kwr8STaGcU7jFda-sMFuIwUnED8XVmoWsSrbmq1FVeD4AW3nJVvlLtX2BcQBQN_hFijXJo6h9XHIdRV7fec_dALHVjt-mtnYGD1maV6UzqEanQMB-_Jht_Hz_N09Hx5r1Cd33EyrcdaNfw1rzZngWvE0Be0t0VZ_HIlE1VxMRq4JIDOtNDUQpwWbySOFxRaBxGCndoB7ocT3VMsB9rvW6JTnKmU5SvA76ciWQ4s1_xSA33hQo9aEneOTw90I96J57lx2iqmY6WCCDUBFbR4bdoqQUU1PUFSrbSLlUJSClMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_xjFJ0x7myFu6dIk9XWBej_c4AWc4TptLl9xojmnC2T4OzRTApSo1h5N1i7GcVWKUZs4jWLqVaZV1fBM4oRl635W_0Lk9Pf4xMpgTtaBTpiUJsth8wY8zuvPfYsRKlOBP-tjzp-k41C9CtNXWqiI3QLCJcDg9b0x52a1yQey6YGMIYEch7-VInMxvBjeLUw-lYsGAz0tQsqqIwxyDOwlhsD3FWFL2atoMRMucvB4rZR1raCZshRnnh3u3-h6XTz1FHXf3clB5z5l3llUd9qN95ZCzZhMjU1m4aNRhGA-zLu6ef2AHRsh5IQ-OI_WkGxqoPmNXPoJCVqkIJYi5-RKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Auc800Kl3sBmUU322PutjS3aZ9_5qY46_A3PVUbJdBoS2jOc3jFSjCVFPPG_1ZAbgmfbxlB7tSFKZZr54Ey05SbVwcF8YQNrhPh3Anm1_tPOYNW_dq-ebAyeAAza8mBwpIrhNNIM5JQ4_dSjqMFRcvDN5__dlqC7ymuFP94h6IaEmDfk-HxBi84DwL8jglZENlDTuXmLG_00PM1UE2QVGEbtRmPxBRiPn_LLEPZebOrCkpRR44LpamCuVvY2RnwIrifP-ptGgleEQ45ThK3JHS0Yx3eQLpNzvN31vK5i7seLpY6_E8FIPQFHsW2YcJCA0-zBRA06qEsHAM1A9caXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSU8rVyllEcGW27LaHYb8J1_8HKjIHgpNSm4ROzrYBtdN3mdZF3VgkanQRsuVFHsd4Rcpb420obOnpiS2aBpcfsAtkuyOOo87Uze0pWOSoz-0TEEEPK_5gC7JVAi2Nj-8h9mbxyTGtw1i0uuHPqoSXPvybpRq648_vgdEbRFwHwjQijNUL71MAoy03OB-3JzIeDAXFDEJW2jf90DqDXSxtmQm0-DHYLDVfPZclgdSH9ohBp_il3XpoVTpBTiQIIkddK4fOFQYULt51a1xyFX7-IgThY8U__GuypNzcFdcTBS4uEFPQZBUEp78Q17-Wz7G1Y-yVgU-PFXhAiwHAVMEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ماسوله؛ نگین سبز گردشگری گیلان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/439001" target="_blank">📅 16:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439000">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
حملات جنگنده‌های اسرائیلی به یک بیمارستان در جنوب لبنان
🔹
وزارت بهداشت لبنان خبر داد در جریان حملات هوایی اسرائیل به شهر «صور»، ۱۳ نفر از کادر درمان یکی از بیمارستان‌های این شهر زخمی شدند.
🔹
در حال حاضر، حملات هوایی صهیونیست‌ها به «النبطیه» در جنوب لبنان، ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/439000" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438996">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pw0zHzXPTWLRqGBXP3Nny2ED_IJAMEBo6Oz3WgG9zI76byRMS2KUSbNY5WqPgBAI0O-aW13GedX7Eq1GS7yUkRQRu6tqYAY35yn7mbf54IZJcD9ohq23GM9GmTReQ7KAkr8trLPcDA-4tZfeKXJiL1i86GAAeTbwf7RwQlGFcawJO1MTgUgBhrDcc1GBqsFCmytFF8tWewi6L6b6JXP2WVXB8FrOO3_dHCKdkbv8MPg6JauRq5XpK0iMnHxepJqaf3ln__CeOV4SUWr8FfaXCgMKKhT9xL-7M_z7yg6I4ZWcAyhIhZqGInudEauunj5w_2eNrXjt4NWw0xFEV_UE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvW6imRHLzFe-FeZbEj9aQzG7OtPIkBJ4mrC_IKEfMAPPwIGTi7w295S_efqhM68PpRjCf_juNNykrrpvlxlJSGh5KmXM_0QOt8GXvzrT41Seuy6KV_roTZh8ZaGGhIeRNQSiBcRj7sLxXeGJvSClxw4qtqe8AK1ZkCNKarTerO_T8BbZc-6GbaWu7VdBMtZkKxiYvhVNarTWgOb2dscpE_0ofkYELpkUKkNJXlI1JVLp4BycRRMQubBD4HyDroQ3aKRFyL0JUQoBMg6M1vb4Ps8YA5l2y00wkmDm40aGUd5aL78Dsqm4SoLwzovUHOyprcR2bG7BIlW3ck7Egqj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hpWvhJxyYGFyUomXuGU-eSeowlFg_iDhNciNQe-yz7x51P4WXhMymI0FxVFfJNyQtK9GFbsNPlQt9jXm4-OiOdMytGF4eJrDMMb-GbTYIVvFv9er8dqidaKpu0Cf9PKNSvLJ_8I2xaTja37qBfvPJsa1ho9fFeIGb4TDr1O8kPjbUBGZ3MgiXSJqA9IINePImjmPRiIWwcFADYq54819eJDLola2G80UICi_h2IlvgSi-dbD5qyfa6RiFCCG8AkgCp0-WEsIQJTfhNKmTkg5-dhQHbfp0UaIrI3uIetNlw6eQQF4DuiP3FgQTeB3FlTIs38SeMNwNsOd3K9oh2CHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7WFPYCzQSnaK8atO4GFE92xWIWPYDaNGR-kfRCrBEvHPFqOkCTYQ77BwRQftfFzAcYwla7-2PM5kJPQCQEEKZdHd4L7xitDypBXfzS_kgKqpqlz5CjX76YnE0FAPgPfn2dRDfjsA_QTZ-TMr-oPOTsBpCvaSY8ZWLLdxuZBvAnTHoCpxxMpOB0e65XgLTQ6602fM8kyAfrNhLKmwwMM1LKteGoHULxwSqlb8YAZiKRO5acZ3a9bjFUhdx0TCxJwIq_YOt2_HRhhvEJLyoX1G-B8h4R0b9-hLpizvyEeag7ZBs7XpCTJC-3-1-8u3mNILzuKgvmV6DduRrTV-hskmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کنایهٔ حنظله به رئیس اف‌بی‌آی با انتشار تصاویر هک شده
🔹
گروه هکری حنظله در تازه‌ترین اطلاعیه خود، با انتشار تصاویری هک شده از «کاش پاتل» رئیس اف‌بی‌آی، به موضوع جایزهٔ ۱۰ میلیون دلاری تعیین‌شده برای شناسایی و دستگیری اعضای این گروه واکنش نشان داد.
🔹
در این پیام آمده است: کاش پاتل عزیز، بی‌خیال دیدارهایت با یوسی؛ جدی بگو، آن جایزهٔ ۱۰ میلیون دلاری که برای دستگیری اعضای حنظله تعیین کرده بودی را چه زمانی قرار است پرداخت کنی؟
🔹
در پایان این پیام نیز تأکید شده است: ما همچنان منتظریم؛ فقط وعده‌هایت را فراموش نکن.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/438996" target="_blank">📅 16:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438995">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1lz9dzuHmjX5MKwyqk5kUIiyaFVEHXM6i4lGTMB5dDuO9ErwmqgLu4V9kurHWNfAEQT6BzgRniMtviwRPOBXjSmMhuIY9AAu_AtmOjk4D_OHa3Me1-zfWhN0NfsG_NhwrUTg19I-LrxpDAO4K_3vjMTJ7SSV1RFap7H5Rdps-um_h6gaiBiuPOMsfiLuJMUQECPtcNakSUjYZ8PowN0Hff1Yl2Yrcc55OzlUgivwcAZ38mdg4-KKaD6SVuB0Aqz9x8sxZzIZ7v8itV_xTdPEVO8uZgm4Nyu3K05ucUv4A12MJCpMtoEEXKbnkvs_g3Lj4-3QsCEPi8QmpNQ0OfXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ازای هر ایرانی روزانه ۲ نخ سیگار دود می‌شود!
🔹
معاون وزیر بهداشت: در ایران سالانه حدود ۷۷ میلیارد نخ سیگار مصرف می‌شود؛ یعنی به‌طور متوسط روزانه به ازای هر ایرانی حدود ۲ نخ سیگار.
🔹
چیزی به‌نام سیگار تفننی وجود ندارد؛ حتی یک‌بار مصرف به‌خصوص در نوجوانان می‌تواند زمینه وابستگی و اعتیاد به سیگار را ایجاد کند.
مصرف دخانیات در گروه‌های سنی مختلف چقدر رشد داشته؟
۱۸ تا ۲۴ سال:
🔸
مصرف دخانیات در مردان: ۳۴٪ افزایش
🔸
مصرف دخانیات در زنان: ۹۰٪ افزایش
۲۵ تا ۳۴ سال:
🔹
مصرف دخانیات در مردان: ۱۹.۶٪ افزایش
🔹
مصرف دخانیات در زنان: ۹۰.۸٪ افزایش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/438995" target="_blank">📅 16:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438992">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnHKrVbGLsJanI8NjJsX1Rn9z7Ew92aGM6WdTuImInhvAB8jIEbtibW6bWfZn3CwuB1VmJjETNU9hsIlIvquh89cBZoCgUkpGjMl3tDh1lQOKdSYQGI6H1UvmmcTe3hwtML4H3MvtaW93kkawg0xOMf7I9L-sbMNXc60L2jOj7x8Og-9JDJa5VyhzMVbDOsFWyFa9z154IBoiDSQ2LrL_OY-759tX6yu3MQLSYgixb_hRtXsqryh5PbcOrkA9KVjcNnIxYRoKeYGAgaInDu3cBu_olZHYNliTFrvO5qzFnT5w7cDeqK6Hggo_0m10vhlTKwQzTQgMKAdEbVR82h3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogJYZpm6CfVUKea-rGPYA61x6tG_L_kMKSefPe6Lhn2Ypzft3Mf5GyZ1JvwLedTH1OEIIsdtHyU_X9jvxfiJv7hNeWyzvNH_jfA0sLAu9LmNzc_CbKX5iIzuPJH8cLVk0FeI9OSHI9_ZeKCHjmgTtgA4hTrfE_zTHvRdknMYYZJK3pCSSX-ggTLm7n2irdU8o8HxQUDRNXK4C4qy37t8Le1NVF90RjEV1qwrD9f2p9RTOJk9gjS1mS5IqkNCr5KhvcRpP2vfddeC39b75olLh7GeJP4BQbv1aXNGXU_dgxu1y_-GzQPRZIcsLDAsmZPMsu7E22UXd4stluUx4WOLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdMPZqkLGNbGPt2oWZ2FUz3C56bAZtkhW9IcEravvEQMv5RoZw4LU2ExWL1eOJnyBoXlvw-sLKGhlKy-q71Nm05i5uHRj4Kr9ZcrbDmCKsU1gM9-Gzjd494Zhyn3muxB6E_jbieSzZ4iZcPBKCdDwYalGyBWxRUA69mhJ2wTKXh90ZyNHb0MfFSDcEpQCFwVct62QC08XliVIzpb4Ux0LXp3RJI_TCVzz_RGXWtKRrYRbdEQ8QX9b8tOJtbd_IiNjMF6AvqJClEvJ2Nd1pPuPq-6EC9JZKBuopd3Q-_ybJ8349I34Pc0jmV4dochVhjcD46vJ_NRGXEDqqNh5eF8sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کسب ۳ مدال توسط آزادکاران ایران
🔹
مهدی دمیرچلی در وزن ۴۵ کیلوگرم و بنیامین آشفته در وزن ۵۱ کیلوگرم کشتی آزاد نوجوانان آسیا موفق به کسب مدال طلا شدند.
🔹
امیرعلی راغب نیز در وزن ۴۸ کیلوگرم با شکست مقابل رغیب ازبکستانی در فینال، به مدال نقره دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/438992" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edae0f30ff.mp4?token=eJriAfnylaN2i6-LWaFh-hpPLgH5_Cz8gBtZqXfDtFU9sETFBi_eeBRjZYDXEqJUPfixBAbzEnzk76o7CF0NACRWXJJf3jYBZXyIYQbbfSKhGE8Rqfd0w_5T5HlnaVo4IwAxOQOmx6ayWUDUWd-6UiVNje6NkLao0vFaQtAWHDKzAMV4vKM8n9khxBNjAM8ptjzp_2s5kVqm1En5okJT5frotFs1TTmXyB71NJyX1FzYMDrztun4N4Zb7dt4Df6w-8hkhKR2fU3RCNUwHocdBopv9jzNHcHR7tMhJlerp0Q2J_wNsAUQmIiLVyoF2_cSoKHhYAiwFpx8EyeYCRTdkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edae0f30ff.mp4?token=eJriAfnylaN2i6-LWaFh-hpPLgH5_Cz8gBtZqXfDtFU9sETFBi_eeBRjZYDXEqJUPfixBAbzEnzk76o7CF0NACRWXJJf3jYBZXyIYQbbfSKhGE8Rqfd0w_5T5HlnaVo4IwAxOQOmx6ayWUDUWd-6UiVNje6NkLao0vFaQtAWHDKzAMV4vKM8n9khxBNjAM8ptjzp_2s5kVqm1En5okJT5frotFs1TTmXyB71NJyX1FzYMDrztun4N4Zb7dt4Df6w-8hkhKR2fU3RCNUwHocdBopv9jzNHcHR7tMhJlerp0Q2J_wNsAUQmIiLVyoF2_cSoKHhYAiwFpx8EyeYCRTdkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گنجی: حاکم‌شدن نگاه عیسی ‌کلانتری در حاکمیت «سم» است
🔹
کارشناس ارشد مسائل سیاسی: کوچک کردن نگاه به آمریکا در شخص ترامپ، یک کج‌فهمی سیاسی آشکار است. مسئله ما با آمریکا مادیات  نیست، بلکه مسئله بر سر «وجود» است.
🔹
کسی که می‌گوید «در حلقوم ترامپ پول بریزیم تا پی کارش برود»، مسئله ایران با غرب را به شدت ساده‌اندیشانه می‌بیند
🔹
برجام سال‌ها پیش اثبات کرد که موضوع هسته‌ای صرفاً یک بهانه بوده و مسئله آمریکا با ما یک مسئله وجودی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/438991" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbd9b8a8e.mp4?token=utFyYU0A7tPCCacNz2Ltxycnq88KmFN4_4B_rrIE5uT5HuLoFaxULWu-aOmkTORPK__TMjHp5ObY6JcXuLme4cyiQGz9M9-hAyHq6W35xPQTyr2q8tWU_AURLrqeC_7UNmVjlHPD-fcwRqbW8He1hiEo4kGav33QR2GgN6-r5sunAh-Uop3oM86YteTi7ZVT-LoeStwHqR94-UBUoeat1-29BpGZR-cwqiTAIdCTKO0j0XAWTbujbxQargSL7GQCM03XwIi9wZchX0fvY-sS9P8ZHB3QAfFDUjsZZyZri8tTLFBzEWKB7mj91M3OPHc6yHfzHacpHa695nSeEDWcEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbd9b8a8e.mp4?token=utFyYU0A7tPCCacNz2Ltxycnq88KmFN4_4B_rrIE5uT5HuLoFaxULWu-aOmkTORPK__TMjHp5ObY6JcXuLme4cyiQGz9M9-hAyHq6W35xPQTyr2q8tWU_AURLrqeC_7UNmVjlHPD-fcwRqbW8He1hiEo4kGav33QR2GgN6-r5sunAh-Uop3oM86YteTi7ZVT-LoeStwHqR94-UBUoeat1-29BpGZR-cwqiTAIdCTKO0j0XAWTbujbxQargSL7GQCM03XwIi9wZchX0fvY-sS9P8ZHB3QAfFDUjsZZyZri8tTLFBzEWKB7mj91M3OPHc6yHfzHacpHa695nSeEDWcEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از دیدار اهالی رسانه با خانوادهٔ سردار شهید سیدعلی موسوی از پیشکسوتان گردان تخریب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/438990" target="_blank">📅 15:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159b83282d.mp4?token=LZdQ7UHEpdYA90FjQU10VHmetEuY9zckW0oQHLDx8tkBSo2TZGqm443Rp0FQ69jOSgcL9wD1Wsl6vVfTEyXXNGPuy3pIvEEIDHp_Y_5sCDTalo0Nxtk3595oicybTDeKS1-n1VBF42rgYp2lol_SzQgksAAkobzSn_evvCAGdZcCvo5hWBJSYnk4Pr5uNaHccWvX5EkXaGbzsWjr15thqSweks51PQedme_F8hFJcfqqBc2_dNFdSKOSafWvlZhena_PxQeEJRQif6ycLcQRwB_5s2ZV34siu7ZBwIpRMKvX5qZVbhmUPT2F4DUVqSLFHhLabI76u42g4Q6Gvt2z5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159b83282d.mp4?token=LZdQ7UHEpdYA90FjQU10VHmetEuY9zckW0oQHLDx8tkBSo2TZGqm443Rp0FQ69jOSgcL9wD1Wsl6vVfTEyXXNGPuy3pIvEEIDHp_Y_5sCDTalo0Nxtk3595oicybTDeKS1-n1VBF42rgYp2lol_SzQgksAAkobzSn_evvCAGdZcCvo5hWBJSYnk4Pr5uNaHccWvX5EkXaGbzsWjr15thqSweks51PQedme_F8hFJcfqqBc2_dNFdSKOSafWvlZhena_PxQeEJRQif6ycLcQRwB_5s2ZV34siu7ZBwIpRMKvX5qZVbhmUPT2F4DUVqSLFHhLabI76u42g4Q6Gvt2z5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌موسایی: برای شادی دل مردم سخت تلاش کردم و مدال طلا را به شهدای مظلوم میناب تقدیم می‌کنم.  @Farsna</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/438989" target="_blank">📅 15:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOVHGcrCrS4qFaBlIdKgjXxHjBFCmi2guc5AXDMB_-cDzlScPKHm1X6apad2oh8V8s5vaMpj-rEjLOyU-AhO09OG1rNcp7FMgdeTPXf2YSlODoZ4bS5DSwvX1iT03yTR961vRNsuseC1IiYw7YE1_FqDTY0z_kgrni-TD80r9_tUYnslxn0oqwhHCIQWFVNnMj4WuddGXlj1SEdOs1gGKHQFOf_bnMrHgioF_ulVfz__WBnuYiUvzTwWHCHD1nUtrvKNs-Koy6X2so8dFBC-5FFykVWyExgna3h3u6TB_YvwMcQD84_5SGo6YczUKMsTawzWEeIJqzbImqzXCw0Zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامهٔ مجید واشقانی توقیف شد
🔹
برنامه «به من چه؟» با اجرای مجید واشقانی که در سکوی روبیکا منتشر می‌شد، از دسترس کاربران خارج شد.
🔸
این برنامه در روزهای گذشته به‌دلیل محتوای ارائه‌شده و پوشش برخی شرکت‌کنندگان حاشیه‌ساز شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/438988" target="_blank">📅 15:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nllKq95XiUrXbUHqBVIYhydU66KEYjc19nLrJ-0GBqdJAUpH_NZwQc7zaC235_JkJDF39ODlO4YcqfEKi8wDcmwzpi707fSYkgbwms0tInX8Q9Z8y82W-LKND9cmG4wRzKfYF-spWdayEWtcXVqp0Y9wQAoBfQq69NubqUKEj58s4B1jT7zK0UVz5YiozRCQjmz5DkEdqJVZd4-g2SP9pKjQ2_27fR6GW4xmufqRZFJwyiItxZVAUgP1iKstNToTrcRBIWLAC_dSS-OAvQZxuamfv-FqVI1PZ3fznvLQ6xgbxh2uHtj4WIVDhdplE3vSXE2hz0iRg949n1770Us8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع برق ۱۴۲ ادارۀ پرمصرف در خوزستان
🔹
شرکت توزیع برق خوزستان: برق ۱۴۲ ادارۀ پرمصرف در سطح استان از طریق کنتورهای هوشمند قطع شد.
🔸
ادارات موظف‌اند در ساعات کاری ۲۵ درصد و پس از ساعات اداری ۶۰ درصد نسبت به حداکثر مصرف در ساعات اداری همان روز، مصرف برق خود را کاهش دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/438987" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=MfFAQeXUEkhzrTU28lLJjIR4Xl_97HWojJkVFWgvEKfyQJlqrzP_nIKjRysGX4fOiPYnaZhh75R8K1HUMffGhSvfQT6SefbCNv-dwrkafCPnT7aaV7R4rAqZSfYrJ8msCQe7M7Uo1Z1kc401XGGu_0RZ3L-tMlkknF8pcTi_mOuBZU6nvCqszUS24pxIlvgdUHOcVzhRpKAhTCcSnVOgXyo64b7OqmG-NKNxDXfcIEKSaMroEiAVDWjQ-4U_g_khNmerv_uqt0YgUXzOo9e9sVlDaJqmIdqOoF13Z1lrRkmdBhb7NeQXOyus6W33OSgTsIJgDGBxN7DipZmFOjFuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7106a3dc12.mp4?token=MfFAQeXUEkhzrTU28lLJjIR4Xl_97HWojJkVFWgvEKfyQJlqrzP_nIKjRysGX4fOiPYnaZhh75R8K1HUMffGhSvfQT6SefbCNv-dwrkafCPnT7aaV7R4rAqZSfYrJ8msCQe7M7Uo1Z1kc401XGGu_0RZ3L-tMlkknF8pcTi_mOuBZU6nvCqszUS24pxIlvgdUHOcVzhRpKAhTCcSnVOgXyo64b7OqmG-NKNxDXfcIEKSaMroEiAVDWjQ-4U_g_khNmerv_uqt0YgUXzOo9e9sVlDaJqmIdqOoF13Z1lrRkmdBhb7NeQXOyus6W33OSgTsIJgDGBxN7DipZmFOjFuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمومنین(ع) مهیای عید غدیر می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/438986" target="_blank">📅 14:58 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
