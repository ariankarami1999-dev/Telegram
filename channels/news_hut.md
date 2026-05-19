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
<img src="https://cdn4.telesco.pe/file/vc1geowBBvFRuk8szsd1Yl6W_hWUUDmwdm6-XPibxRacoeKClnHVbmOsrKx1U6Jl-kCIdEVx3VZoTySnqm5HRccBhUz414zFOfYRx89NIILyFSiMmpJ7rsfOUFR0Y2Yw_RlhmfUB4Gs_ND7ZKgP_DrA0CpxzMNDtvffrLoN9bklKGbC8_MV1lVB1k5oNxo1EG93xWrFJbqZxcAn6XS_JYwkhHmxVaMrYdcCA3XG7KkCZGZRRYQ8-lrPmzRVRL-KB-42PPD-MRrchOc5L36Nco-rNsH82-ejZwFM0A2mJOsCfwzhZguxmg-wucEe3bidTtWSDwrxexBo68nNJm5V6oQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 144K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 06:57:32</div>
<hr>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc1MQqGJ08MCePeYpvSASVmEfJ-WoTNbreiXhrDA7gHhvV-rqCdpx0p0b8Mlh7yFu1FJYnYNrrNiFXkwFjKt0NimfPgCmYFMDtuvcbrgObLT-twGvkFPCaCuYZ_i0KGbeYY-Q9Y_IpJ4wAFy3574uPlPu13xr2B4lNe4skXPuAVrznMiLjop2ttjINoF4fU0HApECblnweg_PyILpiW94IL08cEwbINgqyW8Aw9Nncow3VO6Ow5IbdW1HYIyZM_e_9x9r6WDSMHGV1P8L77J205s5j46hRiLnV6qHr6QDHDrESET1VH9k7oVaoHzC2hhdeGgGSw72mdr3HM_QFD-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYjERLEY64-U4uYhPgkfPG4BFiFB9JfqImhyFZyDPHUV2T5eJyAEYq_wOWmT2UtUNjWESA9tAKR2kxskrN90jJBNgDQhAmFQ75NCuBHNXBYny5iRSZWnGsxPISf4EmAHZlOK7Z5hqwKpjMrk0PHjWFtUMOUq6d_sWWGDnUQAvkhHsdd4c9uOSv5Pmf7RTUb2MOq7xG0rjJUD_Zgn05POEcqKkDhlg8b5NNzCU-3uDGgng3a7GDMgB15pOY9Ogui5hrj48qSYXhNfkTFMu8ttlUiYh86NKMTFYtIanPJd26tp9tv7s2bnI0yIS4AxxYTiIDbpd-qJsvVkjLwMZReRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به سلاح هسته‌ای دست پیدا نکنه.
با توجه به احترامم به این رهبران، به ارتش آمریکا دستور دادم فعلاً حمله انجام نشه، اما همزمان آماده‌باش کامل هستیم که اگه توافقی به نتیجه نرسه، در هر لحظه یه حمله گسترده رو شروع کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/64962" target="_blank">📅 22:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgmrUZ1Yre1M4d9ZPIctvlD2Z83yu-FUYYEiE5PitQ3cP9nowFzhYr5WACOaDOaFkJZw6rgA1NHnceskOXQAz7Q066Dxc-CeaVcad38w72wENVkTGmIkMYcULrcTeSUxVumd89RmJrFT0a6evpqbxpJqs4rhbhsDP7VlQmHsc1Otaah8DIPAhr8EODApPEoNAGXnNGFLd4bMzIfHW86c8mdlMT0fPPQ116T60bLec5qnAVgfuhnF7mDewx4e-Ij7vqatxC2HWNbtpjDWL691VBPgIRuabhzEgHlDqv35CRxLUN8p_2TprxjHGoQwqxw48T0TfU2-aKg_4t6Y1faEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPBLePufAL-uLBfwCt2dSCHyrdue-5VoGQ2rooCcJuQ6u9nM2ABKWW12HF1o4BTZrYpkzsE_I759a_KqKV7CkcSQ4ZenAiFJcBw6ah0VSefEmqdF86lSxn0pYbKxWAvEssy5nfDwS6DZqpB5x9CFAT8qjZf_sldXpD-q6UsqNBjnBnGHfmZLG2NdKIDUjlGqTdKYfbgfgzMKvDdK7JCIdf2gtRJiY7eaz4yPp66yd6CzWr7uuNNe-6Hl-kp_9BM52BC524WnpmRaSSolvTL5lmm2dfligjqsWtKcnl5u36uL0w0G0LyLWVKdhmjUfPyaNA3y892DfGgYqhAfu9_0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0e7TY39qUxSg1bpkG39JX-ELps6sXz0sKCD4rMqDwVnGaGU6AwH88TLFr9WJS7lUlJYueEVk3c9Yn_g_9NaiL2gsIf99XVLD9GfVH2akTpcARtbxjYX91S7fPE6wc9mVPRNo8eV9LoxJ6jc6FEvMS7rLfiNMJWFhelJKid906YmMheCU46lXBmSR1ysKekqwAQ9wwac7wZWa3Wz8de7BCwA4dDR0a7WT68vWR0JdTnP1nqj7x0EircPLAiGdR0Hkf-aloj4PK3JnAWd7xAfEbh-xSKVg5C9pNLBkKv7DEP--e0dt1RTTLw3v20oDf4MvYS7inlE03KsRAE2KUW4ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_Ii_awOWTsfVZpeodVE9vm88Ha3NMPHkAlpjaRmAsGuCFRXfkfVhllazTeRNw0RFZAWk5qNT5gWLNASrwYoCuCcscPUUiBUmtjG8NVw7HKfq98syx-kaQVD_kQqEulVqKYx-Ae_oV_ui0GVYvwg_vYesP5EXJ7BWMwUhgGwjFtdHTARoNCGZ8Paq_r18MRLIbjQPqa5U9IH-YLd7qAgfFASdypKgsmsqZgldRX91O09zeh3f3ma9z7QK29yQ0jR9SdAkRjPXboMuymmxKDpBxE1t6-Digmwh3Vx3m7eMGGbhh7dU-lL5khdUcTrT_25iuYL_H3FyikhCS8oeJ6ILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KvW4UgxXR9lMSGmQEVbJGWklOpsbXWyxJcicQ8ayMzaXihfBXezm9KEUwhWNfDUOFNMnDln-u_QviaoIGFuo3L0iGj5UuiiemRx9ROSRVSRDtW22pRzA30yHc3GKo7OxD6Czm364LaSPczyk9dLPHNUvNlAeINK0aV-2WF8yfWBEQQnMtNp0bNka4ZfRPaGAXU_pfoOQalaQOuZsSYNv7Bcqqs1fjRKfMi7vB1iolWFxgj-olXafeH0KsQatuuP-s3AyVIv2kpzlIwrSe2cA93HzcrtPjc89b_RHIlDLR5ZZR2DMwUNimDEzm2qg94OmSU0DvFpA5efmxEERr9rz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ph5go0P8twqx3GDZKFPjDJuSwhWAdUZa-mNflZaPr9xJvf0tmbGtpJgGPYMpA1liW-TSEGBGMRIg0aIlFj8Ki1-Jx0MoBT3jDdA-aGyFlo57zlnAZIjCD9WLj5OGaqNN1lJ6aG_j1orICaQtyyHWZK3BAuYE8jXto-BIO8dHXhSixFlT3AgtKFPB5VkzslKP1MGiVq4PfMuVM0RH4vwJYPAFNHBOAIaoZEb4DBuEJ1VsjxV474K9uRR5k-brsZIfs0caveFclSCKASYCb4S0qMbX6VSyKylPzMD7RrrclU4FUeTjU9BPdzU44LkrwhUbunGrNevQ1-Rn8gjPwzVrXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d4U-YTM-BRw_2-VJ3gwKkYMhbAIY-K3tuGiGT07njfj5qCtZIJiKzUIYSwCTnZoj4KUJWYHMmWybNISYbxnURG1FBeEOQavp_XR0bxYRgaI1UmiYY3X0DBJupz0coMjmCU31WcU49f-UfCGTJYjn1nKdUcZi_tIAXn3DcxnYgY9v61qLI2L3ujn1TOBKIIkov2S8obhd8kAmPOYH7_OHScWO57o1xFXSzdUGcv4aJ5ryRPDVYr2M5VH8Tjs83Q9X2eNhgrFTFKxXDxbSOrWlFbkm9lesL0M6m7QXgBpC8N3yqUmgQ-zFuCRNomim_JF0MMBmrlrXw2TzKshnfL4VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eMhJihqDvGC3OuFkTccJl05N6sBPJs63QGPsDo63pWE4E8DYgMx7t-eevackNl5f1k7Zg9QfJsauo5Bf2uUp3olgjcjqArzutw1D-VTnDRVvO2qU3LbXyhSLXAO4OmgriXmjYuX7Mkc_oqG6sAevGPJYM-Mn_zCrnbTrF8j-t2XhIs4awpyCpU_NZGjTwLy0w0tBERZMWdnY8LnzqtWusdikaWizMaspqxvSUbe-7i1WQv8GSAF9DPVBqRZ6dVl1HDOZT1CsZI1CnRhueRA_8mOvSJTHChQ0iPZm-_5GEx2Z_OR3sHLXL8BAhDKQ8mdOJVqM0-kBviwj0vthEfayBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UdRUzIF7L1MfRvQXNboMUYKpJSeEaHTF4yyjC2i20U6j4VYovNzCWtJFyKDORT_V8yIKo153EiT2YsAM4mjqXNosfccaPhP_mk7VIFdZRriAmDOXDwAdmbE89icFK_7fnEBecbz0v6W52P24jZ4B8v_jXigOGikbAS8R-2vbbxjB7Tl6CvYGHHAlW9-rLcVPHkGGFO-nqVdp2brukT7M9-ed4K-Xb9NX0VJ9L0l8zTFS8v8DNJdwKBhdmz67xS_orl7qOMp_CRUykTTy1mL5QqMsQlSIcnxTt7EsPGMhzTtckTWJg9gBo44mf51EWdlKNbzmmCP5CJkK3UJina5UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WnbuOnCuU97LrQxIYg5RM6wE_aP4HBT-0T-UE07dMspoyADCaHwH1FGkTktavsZJxeVWZTxFmxyg_mQeFWKYNKIUGfFpTCL1eDgMYpd94uGIa6KYwiCBcqKCAXhuoExAwU6ayLb8lITQWuOxqhpAcuIflzESiyHy70D4lDhmM2vfrRDQcAL32wy5kkwRvg3GggBl7FDjn3nRY1gCVAzHDmog_lXwFXDMTq3oDjRpKlhG3TyfErOViHnqErdnmkD0LQHg2sPbxHYEbaXL9AZtgj2EhqAmYAGIoC9KEW8TmgmXhkwrq3PRRYkGm6q3ju9U6--bYjmt_572BpNHnXSM3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmu58epFkcfCr_UGg4fWuuwjLqfTKt-nqYataDaKirAb-zDmyf9NN19aOe65JGiNR7mkc1JEEL00-4iiELZ1IYcAjm97-xj_FymFTbEn4QNdTuzhJbMBGFd4_oe3hCH7cMywHEcIKP54eIQJaSjfBsXy4YHFMsY7weeWuInrjto9d7bck_8LVAFmeFMkRQqnQ1flvYLXQtuth7-qViVYHPCKFTptq5QL725GeqBh4LiDfs6WTdQmx0hQHV0qPmPmVMdoC_qpm45oeIecR42ayLXPOAQ7JyhMHg5NGGTvKleq-odfYo7SjkWy1lyWOAbW6V9QRgfPCVXbApks7QtmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VbmlOV6y7DVyNi2Tbfid02Zi4A38jQIoMtfqxKnangRQusGW690jbGA7_jExgJ3LWvxUFVkDInBY_Ue6FOIb9XmNflnlIiqn8enHfbHZLvOPUa6LcrFDhFo7cUyDjuAqgy8ijgwJalV5IdmiZXe5gkKDNdQJRhshO4ScH6Q_V7OCvRFY1x2jipr1miThYVKGrndZHHrnD9k2yZZLFt9uH8k4F2u_d896VFWlkuSUCVEtoQO9eNraE3W0DYxntFH5dZaTdekbCYvVxp1KTEjj4tGottbPgo6cM2eECfnLJwV2cWS-NfP6DZ5zaA74Hvh_0ox4eCeFPqopVh_UreQ6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAtaJutOjt4YEtFis2-H8u7RJYZi0eYaubygoiSKORN5J0JJZjxzUAa4ML6iNnqiCXkvZGVx3PCrZ2St4tHQ5N7R2YKrDMOjUNBdD5zvtPboC-AEgEcQX4JKFjASwAlzeING4f_jRhru2CsTZLLEp__72vV8JxnuZUojCiI-GCIZu1Bq8iTY_uogdcbBfdEfc6zSz0N44j-AiB2fxZETfZd4aYRmkhnMIhgQnYkki6tJN51vuP2yKzRXK98yS7uxnc5L4n5hPeSTSV9GrYR8BPEbN7EEWi_NS1_ffjwSPC1BCvv-RT0pJg4KXn0dGktknObb9mtSXVAf3pd1z-yhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=rW3C1ejYoh0yF1I2vKTXCNHE-Q13tnjTqbCIn2pUY70WKsuLvm6eUceBJSlbuG3bzS-J_Vp7T7bdLvepJISL7g3RpztWzq2W8Po0yqucfalaUSZ3cbbMMxL2rtkOp9hKXWTqNQ8xTGylv-vYaGGLd01NbSPtY3F1-3i-DpEO7ZEidkHwlx57I2MYrx1l2p18EEyrRxSH7MuXM7YKWwuDqjTp8oO5lA6IzfP4ov1RNVLb9faGn-ichtzwQagVo1JKMH-_gieS1mdClpBy9qlBHmL4fXKDaoscB6jEi-jsdLGp72ueMzO4f-svvi4ug800pbIBzE44Fjs6nXtpLWW2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=rW3C1ejYoh0yF1I2vKTXCNHE-Q13tnjTqbCIn2pUY70WKsuLvm6eUceBJSlbuG3bzS-J_Vp7T7bdLvepJISL7g3RpztWzq2W8Po0yqucfalaUSZ3cbbMMxL2rtkOp9hKXWTqNQ8xTGylv-vYaGGLd01NbSPtY3F1-3i-DpEO7ZEidkHwlx57I2MYrx1l2p18EEyrRxSH7MuXM7YKWwuDqjTp8oO5lA6IzfP4ov1RNVLb9faGn-ichtzwQagVo1JKMH-_gieS1mdClpBy9qlBHmL4fXKDaoscB6jEi-jsdLGp72ueMzO4f-svvi4ug800pbIBzE44Fjs6nXtpLWW2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=jUSyDLNh_Aq8O1m-CmTKTAx8ROnVdUwB_KL_Ne-NTlovIW1BqOAIZ0GxEEZSKcrFj30x1K-d1SiZQBQOIyd2FBTmeZNwKHRgzwORtoyEZUnV9L4fxvsFedNy3Wet98tNv7Z8U78nnnAZDxRYe32W0KEiaWZvACPLykucgLYBycORy6naNASBlU_V1P08_8NaM4Wxqxd0VFsId3RDdKI_AoAMFqQGfLpUnOjQ9ybiKI9ZI_kluPEiZtI-HCtx6XH6IXFXehgZhlZGsQLVSJ3Dc-SB57O5Zi5QlQVAYSVVZ2fnp4-wQ4uyHdYbpPlDF9HaFsfjteu7JEXJGzltHm7cqA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=jUSyDLNh_Aq8O1m-CmTKTAx8ROnVdUwB_KL_Ne-NTlovIW1BqOAIZ0GxEEZSKcrFj30x1K-d1SiZQBQOIyd2FBTmeZNwKHRgzwORtoyEZUnV9L4fxvsFedNy3Wet98tNv7Z8U78nnnAZDxRYe32W0KEiaWZvACPLykucgLYBycORy6naNASBlU_V1P08_8NaM4Wxqxd0VFsId3RDdKI_AoAMFqQGfLpUnOjQ9ybiKI9ZI_kluPEiZtI-HCtx6XH6IXFXehgZhlZGsQLVSJ3Dc-SB57O5Zi5QlQVAYSVVZ2fnp4-wQ4uyHdYbpPlDF9HaFsfjteu7JEXJGzltHm7cqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/guw7xdKKGHun7SMwDrmn-sm2DDfOY3rJjsPbHA5yu4i9Ye3eSS9pSBXZ-pbizK99BJovXSkpDMj0Um8sg61QYPuQ0iqt1XPhfQA9NMytmyUnjxurQVmPqh2f0GVCajNcBra2RbXP8VZl0SEm7HxF-jhn7eYweGHKrpJpeVJq1niipfdMhLjzrcO21H026wLKuHJEoo888FN3hcXWsLc1H_y0ob2j0mvjWfPNniZPHo_hpAV-MhTDc15BsJwwiJeMFgEHCX5waaoEZNOBmRFbHNYNdF5r9zH3aB4-inDbaxiWvzMK-uDultRLRsQ1rnM4RSkop9rmkYF9d7oYTEEZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDwKqia_LBpCddxNMYGHXw5oc2Y-HpU4gCbtly8fXK-NgrRTE9Hn88NbrDp00x6J1wxgsccieZ_JJf7ZtSnFX1vC48-7Hi6MrA7-3DTUB9Fw_9-O_ZPEBa9rQhWhFF1Mf8hJTCeJLqGF5wh_tO9UdS4KlbKsu7_98lIX-NgGV_K7F_hSE28-0CPUHy5rxl6mfY3gYWVC8HAbrY-QM9fwObzZRngUAAvebN9-14Vi3c8K1flQYPJbs2KkpCg5lvMGHOtAkdnK2js6rKLBGgL1sRpoqDANEBZYuv7IpKCSJvi0AlEIxZe2mEVJypYZEpfp0_IUfsmN4qC6Z-xUnM5xlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjNPVwmIFpmEGL3vjOciXOHRaK_r-POPtEVbOcpr98c9rkOaIfzAAeVCsKE-wwIc73w7jAY3Oj7TFHDOPLcNK5_OYcv8CR4Dw4-AMO7ntCgSBRd89IkDVvG3ClepG41WWZtg0hR203rXzoZJZ2FwjvprxFx2pd2TjdHGsPyPe6LinmuqvyceIR6ttDxfmtbIF02GTBVktDlT8Z0EFkkQfyjM2_LUZpsmB2ihaErK04AsdXwibhzZ7LG81nagtLMvJCpnYHUmCdksdyquzLuMtgPOwKOIa_q8MjyFaKX-7JZ3wwlW57HmQ27kPU4iuCi-Ozaqb4OY2KtugZ25xBRS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=jma-NmpQABFOzMCodIz3S-Z-AlM4SajKwwdxzg8kVV3wqCjALD7R_N4fzd2QueKrQ7XgdWyyLQJScqbTfgDkqzwE4V06xT-7Gc0806tzjDlTxljnKbO9jyYsR5Mw4ujiDvHoQW0Vrugd5ZST1FohChpY-ROr9GWph4OMPuiCMT9XG2Kq-y7tdMWVHGc_gAGPYPRK5S_PJlhfFoNg0zUYEfIJwzzFGUYmLGrg61687KVMgf280s2LYA55q5-0su26hS2J6TrOo_EJuhD6ScisVY8qnyQ7H5nqZCle4xJoLU6TJ5Itg3bhukTcLYJ6lKfJo0x4M35XapOZMVK9LJjfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=jma-NmpQABFOzMCodIz3S-Z-AlM4SajKwwdxzg8kVV3wqCjALD7R_N4fzd2QueKrQ7XgdWyyLQJScqbTfgDkqzwE4V06xT-7Gc0806tzjDlTxljnKbO9jyYsR5Mw4ujiDvHoQW0Vrugd5ZST1FohChpY-ROr9GWph4OMPuiCMT9XG2Kq-y7tdMWVHGc_gAGPYPRK5S_PJlhfFoNg0zUYEfIJwzzFGUYmLGrg61687KVMgf280s2LYA55q5-0su26hS2J6TrOo_EJuhD6ScisVY8qnyQ7H5nqZCle4xJoLU6TJ5Itg3bhukTcLYJ6lKfJo0x4M35XapOZMVK9LJjfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDABFqERv2STIR50Hy0-b25J8qa8dAexOdJP6VicdPw1pNwgWULpudwakx6I7lcQH2cOu8yM4QzwWeNYo3V80lqZWM206cVDaQodBHEBCBfXPDtC3rVOI-F19aN9x7NHfzMD5sSNfq8jjDSWt1yFH2x5bqd9o1hVpwrG_d4TlhpmiGRDnTBM56QJ17VG9uOyNGA1-wG_45xg4wCeWX6TN1svONimu3cqSgNGrF9_hvvWoywGbYWcXNMHVeAxb5dIkDTQcS03nGWO03hHEziEZeybvLLeTO379u0-0dfHDnyP5rZXYSgUkQ3G3ojUuyysthmFVdLtdNtObxst-H7XIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWMyItYYOI77DnlOLWvTUriFFB9ZkeHEtx0Rh1K-MlrLq3igoSyV6qiLiqtPqxclXSIP9Epo8f0VP98dXOQFcsrTuyJZt_Cs29W-XZ3bqtXWpTVqvvBgl87sHvMTO5yG5E3YTToSkevCuKVbyL4IMOTyNkgujCTL2B38uPCmuwuNse5_CaXA61XkH98-6h_8_8Kp3yJfr68ty-4EHvuYUuRAHaK5cwHt5gXmnDTlpeg328_k2W5SS6KV9j5a3TPObcL4LhhxKevLyELhTAiIhQpOSzTYt9SNVHyU68fb_b6p75FJNcvFiY9pBi2IlkwGiAbqGDFwnTErVF-2QLUpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLj1IjTUrfx39Z08CHnhw45Jn0NN0FydAFVWl7XghZOMBv8qd1Voks2ka5VovD9UgZ04wNQb1JjJRLEm_Yb9wJx2f7V7rFo07p3-1bCkcDHOKbSvKWtl_f2GbSrMmxkzMhGN2cJ4o17hANuM05jdesokaKOYWpEwde6yx_YhUGZ1xispWnku543WJruCr3T_0MuReRIUO0kgItAcpFCfgWqAxsCWOwTeBcX1UXaPAoM4rhbO1t_nHos2znbBES3eFb_uM8apZXnPrOUcEUl9TkvGl4iQoatQJ44JxRl2ji1oOqFIDw1Ai-MpE9y0U1Dc2rW9yt3THD6k5d3fHhMFEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKcdVd3pEDilt3FWjotwdhlKsAQJBCw1NtFStHN8IabxW3E5BetPAuCV0OrgfUVIxxMQUO9eW27f-Be1B-TwDV5YXeB3seA82JK0fOJ1JHBzMaq1wxrm_7KVLK-3-kF_AmNCkkW7Q9Jk0Zl2U8d3QfCFzlfrl-Ee1IJa5QjM7pHcQeSDqFMGXgo8q_jYjPRsflyW2UkvhhFMYL_zb_qNamlag-j9R9amoQ72crFwRNQHk5aXqyMhe-EWPTjEc0_eqEljOgr1nuV_HFgjkoIOq3C897LI2G-OMt3sUIpTcyqZWdH9JlzdB-sd6feCMyr8MCpQhfNMl3RXZp56lP-LHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=nn_WlHMOLvgcVVnSp39ECUVpHSXDuwjflI6XM9dDlhsLzYtqJFmw9omKQfaCYloE8lqwm1-V42bUNe4W-Y6SZ89oReE0OgOVNOp0N_ahq5eiTmOanXmeNs3_xyh2Shsrg3_eq6k8LM0-e6SON7iXzULlC9nfI555xSAG-iGE7CxMXROtm023eHwQCzxLesM9SZDYQkhZQbd05-dAm-fM9Mjw-h9jPgO4E5zACd2psCM8SFKwoTbQVSF7b0keSzT7Dr19Fh0NLW1hmOaugxk-k2Gj77IwU0NEYbyaO7dbHAKA6eKI39keUkl4iQvRgRBSsiGufioDlJVfVrst_x0ePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=nn_WlHMOLvgcVVnSp39ECUVpHSXDuwjflI6XM9dDlhsLzYtqJFmw9omKQfaCYloE8lqwm1-V42bUNe4W-Y6SZ89oReE0OgOVNOp0N_ahq5eiTmOanXmeNs3_xyh2Shsrg3_eq6k8LM0-e6SON7iXzULlC9nfI555xSAG-iGE7CxMXROtm023eHwQCzxLesM9SZDYQkhZQbd05-dAm-fM9Mjw-h9jPgO4E5zACd2psCM8SFKwoTbQVSF7b0keSzT7Dr19Fh0NLW1hmOaugxk-k2Gj77IwU0NEYbyaO7dbHAKA6eKI39keUkl4iQvRgRBSsiGufioDlJVfVrst_x0ePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne6DhGJydiz4yJAjBLRyR6NKYxcs1Wsq-xjX2u6D0cV72taXWXBuk4FvVMakAOVTonahxGU45jJHNz2QWyT0Y2MD2zNbEeQu059RhFBSL1mZLjaJZec7VbbNQzmkDjTBOmLNNBNmMT5V377sEPWsKSqNGQJsnBTBWJ_08Zo0DGV71zJ1q2DxNgIw7O11jKkvLdy8jPeHpmSoU48yCAc7fDYiekolZjhue8quP88UgTR9XZLLGSfC06rkUjDR86udanABs9D-mJeNB6Tn8S1jxRLylQx45VDmjJyLhMvhnMhq8JZyPrTDJ4jeBZaj2w9By_POgXqWXMQg3LOk7RYL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHtvZIhJmeRn6-J5X8cKmRjMHoLbxezDdOwyLs5GqNK6PWc_Z6llluw2AlsQpfsxDRSVFrsBpdgcTAkSzle7kMs_nwroi7BEP0ER73uZY0hupWQsHZgU0AoB3SvcnXKpYIWvHIT2rAb0Eo4CRKJlZpY3vcXlzIlh2OGllWFDGQEwQH8vArkE4YjkhehSJ7bN588rViCeJQ7MU2p1QBqSzjDQq306YgJQ3_NIzryFr-HFjEgwdUtk2q0IUfxKqPrbXplUSO5AyjRtepI293K570RQUnp85Hj1TCIGUhI2gvZGWD1mUhNyBTagkFgKFEX136uOZZuA46syTBlUeKiEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKEhaUvxQY1a-fi2D32OskJzufV-R3kKgv8awYkPiEttohhtihpwM5QbT1YhVnKsgdNjqZD1oTnJ8iC9FDlitxftPjLNc_DPEaW150D9RJr6wQlMPh67HXpnBuOiTmH4RHzQTs837fzSncRWTPtZm5Xo-NIE5dZ3THGf49eQlfW0urV8JWKEB-6u1N9w5edsoh7eBRDIXT_K9r0BdYMoM4iWJnuATvGaolUXa0uYs6TkiIxYIKSU0fClU3TPrhOthr6LgU_INZ76UUicaNE66YcRmtrlXUyGWu-cQJKErRpgLLWlEwZpGdXt92zY9SeL6f7khOBi4sQ_RUf5JZhLnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8JUbAvdhR0pbFibvWV-p1hbS5B0soB9GkuQsdFPxVUIKeU8iDF4tiB_93w2MW3ALFuzyyPiE7Uj6wgKq3v_KNWuDY9b7yZK9X48LslS7J12OnHwWxtvjU0PaFIlfoEjkkHMeKMKbqRqwUL-hxNkqiWi3PWW7UPAZwFzh63WfdF50J2JJB8yXnTPhO1bh7xyf4GdOBpJMToeXCmJZvQkF67aygZ9pwD6pPoUvhbp_7Ng0ZqThrhEoC1_MB9PeiJj2sAwsyOm8QzkXsvmoJ-ax8FvhLc8ubvRSi1xZWEAtGYfGxuwArOUhkNcY_acsmNQdAroUfAkfgSggI4bUI-9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI7FLNERnA9bdy6n_1ESK3ty-vqD28iiv1U42yLqyqhZC9KVEUqiLF_sWJzIF2QGJJ846J9Pu6Q4A_j3daOmAsfYX0gmyhiZQTdafBfkLxF4IOgTh8d_iClAXZH5uIBTSLzSD3p5MZj1AlB3PeaqNDupGmZpCcljpUNkpNAwCM2MAADN6pVJSqOBQ4WpKGZNyszwrx3OV0Wbtvb6KyEw1XC3VRd46ne1KSl8fuKnZg6cMWxtMks1n7wZppvyXBI6bs_4NrlS44EoozeKeTE93q3P1tG98he8TzchvPx5_olSOANSLH8djDJ0Wu8RpaMLKTG77vqseEOkUH07mP8HkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=a-Q4ViDtraRDAWSao4ur-wgJ4RvOpIL8UKwOaHCE95Y2_b0N04fGZ2zmItHED2wjLcUM5wRwC6dm5vCouxtAuhCjOY_hx1hVxi2vk6qi5zk0Hst_eOyM5VwR1AIg5AsssRavIgfo2BvA1dl6UHfdekhsDMdJ4uSTCsAn5e44jErOqD1O5VHB0VQP5HMEnacfxh-iZp4yAK_3Q-95nhp8assu_XfvAyElbDe2z_qeVj31ayjcVkorcc04b1CzPb3ruGYCm5NnaQLs05zqcEpb8QiLNDQ_ESBHPP-uXpha0NXCthXMfqax5ephSPqZBWJnNs32slNgPaA1rSZp4fVboQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=a-Q4ViDtraRDAWSao4ur-wgJ4RvOpIL8UKwOaHCE95Y2_b0N04fGZ2zmItHED2wjLcUM5wRwC6dm5vCouxtAuhCjOY_hx1hVxi2vk6qi5zk0Hst_eOyM5VwR1AIg5AsssRavIgfo2BvA1dl6UHfdekhsDMdJ4uSTCsAn5e44jErOqD1O5VHB0VQP5HMEnacfxh-iZp4yAK_3Q-95nhp8assu_XfvAyElbDe2z_qeVj31ayjcVkorcc04b1CzPb3ruGYCm5NnaQLs05zqcEpb8QiLNDQ_ESBHPP-uXpha0NXCthXMfqax5ephSPqZBWJnNs32slNgPaA1rSZp4fVboQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YkKetyvp96iCMa--aeWHpe7sYHha1tdSvkhDuwa_0P5N0NGg5iDzlN-ZHPs0J9tp5p5DKBd8OeP4rQvrJblKJD0MgbaMsa_B92eHt_9q6bLtRWpYd6xWqKGsFUsKOIerfDNHqZL_Dg44kSvMhp3ZEDYhe0v5DlNKcAJyWwQkO_wuYpnKwHaPZug8uSMFK3-xrLf4f0gUDJ2j9H_UHC4d2_4qgFIU4-H02pmNQjE--70bxxCpdgYH-wMSGwOx9qZk870RcBtCLUjqQZs8iVAsDumRmQhe8zSxU5sZmwgww-BO5bZwwkiCKZclU-Kyv3i4w90ReL4XHrg5AtEglEVMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPtSaSNAZsKCQ-fwvF2GVoFAxRZKyOpyo2rxg58-0aWmi03kD5YAQacxq-gp8N8gRuTOWSi3Wb7JSUPEdQvnOpzr4Mp72LGQmwK2tePNFBZpwdjLZBVx0HfUp_EknODMI00ba3FkRrKdGREraxBGQylIxeh2C_vqVW2MqmUg0yAOc2MVzh7ERcQfC6CGbS58mjqjv-moKo1mqUyQulyai9bbBW5ybq5C3mp2JnlBPtQYhrkN1DAwO-JLKCwGpdZcj3fK2qpdIsFTKtXGiYRwggZ3XLESAK1AJypbYs8WmQHgl0GtyTBoeSwJcLvHO4lp8ebOKDI-3XGm3ZjL5geiXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=g7x7NoLJVIGZ1Jm4CAgCY5yxT3FRDMI9j_tCFLqIn5XpbBCWtRGPkNtVGgU-UCUDH1ZLhnIK4ZzeiRCCIqwnzF_KLi3iyTEADYu8lfqxwpE9yi-PGG88grPIx-lcLy5W5t6Wnl3bbeGa7b4AfBloVqk4Zp75N76YScsuy5StiVxnctUHBp4AeVZuR8x6XoG2vzlpDg8mNSWmMP-BaXlXriTJD4-YAalXg9ZiBY8pniA6C9QdnZ8r99ewv6uRZO556Q4b65hYEtM6-L7hz1RX1E1SvAhuVspogZLNWel41vRhpadVC5IXbCOQtjmHExgQNcxhplAzon7V0qWFhh_Ggg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=g7x7NoLJVIGZ1Jm4CAgCY5yxT3FRDMI9j_tCFLqIn5XpbBCWtRGPkNtVGgU-UCUDH1ZLhnIK4ZzeiRCCIqwnzF_KLi3iyTEADYu8lfqxwpE9yi-PGG88grPIx-lcLy5W5t6Wnl3bbeGa7b4AfBloVqk4Zp75N76YScsuy5StiVxnctUHBp4AeVZuR8x6XoG2vzlpDg8mNSWmMP-BaXlXriTJD4-YAalXg9ZiBY8pniA6C9QdnZ8r99ewv6uRZO556Q4b65hYEtM6-L7hz1RX1E1SvAhuVspogZLNWel41vRhpadVC5IXbCOQtjmHExgQNcxhplAzon7V0qWFhh_Ggg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRJMGDehRexrA36F9l2xxkQlN2BQirDs5krMjC-kOYr2cZTmKoyjcGoWWl0s4TyT3_nR3NlTj_GCssS9Ty9mDWxT_LvswdxP4-RowAmbppWbfORzq_r1ZCJk247IILUFa919f2lTeOe5ub_UJrXGKTSG2qM3VukgEx06C2pyVNpjCYLjksDsv7FqddCb5kZPaH04pZysF2Ii3AuYE-FU4UKu-KhDS7YJc7kLsl2D1BIO5LBlrteQ6iiJ_WcMquFySdypyBoqKzisvvytQOdvRWEZNdhclwMicAceS-TDJiPI0Xxp5bnMFeCr70Ye11DgKCNZ0I3C7H4BwSBhekKUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmPvg95ublcYdmOsp1P3Q-xPs3Fiq8wp0cMmPIsDNw-40CyXJ5IGZYt2vsDvdMhcOsqdXglMz5-esqueMV5U35GeowmVSa3hORGF2wElwSIFD0bC63pSKuegpCzy47qnhSQe-xZIt0iXt2Y4nrvleeGt6Hp5cZA6Muy6j5LZ1c0dIrBHJx_mC1FQ3wwPG1YjLWpzeM5ZX94GWst9gAtleHeegj3_9tCI0OiPO2uf8N-aCuhe2Xiv3MUu-EvPQJZPZFA2t8yrKNWd_MUHpie5p7boIDUZBNA9CQf5vbkSuFPFOPkNBRaAZ8mNBklfzLmVC9KJ39YWdNNhcHuQRnFGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvHLoh40u0mHLyeJl031jYhbIiPhFgq3vEfiblCP9e1SQ5hUUQ1WyFivsldVDsjC-WG0qHOnm943wGAguv_MapdiDuDB22mL07uU-H0sb8C8V6a55zQtiURiQA7ezylK2HbXHVOEGlXrosIrVRTKFHYNPWpV5O0IqV5NP8ehusPH4G5qRkqBId22mgO1fNz-3Wm6mtiUhtUcwpNJU3YpytqOHpbv39O6Suj2wvfVMMQmq9X7Jh1bJ0Z9jNBmBuLINW7-Zsd0bflv5LDke0tAD0YCi7jy3xQpvvi4xKmHMLawlvgXzvPhJsmTji7uadHzWCd6Rhe9jIlU-B3PPoKEfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=rww3YuN3Ne6huA_u648aNQbLeuhFY-wa8QTkM719HQEnnHvFvukWCqV09TYriEGb7GSU1b4k35CRkcpADCSfPNeL6ph_2_dyx8Q98e7RXnRBW4BcZLAS7Z-FWTzBnwdhTo8nfqEhfxOlk0XpA8JOJpve-jP12VW7fFzuG2GWA8Bqm_LWi7md2XCHTtxrBeNvYELzBDkn9W5TX14OwH-XQNe1VRrBptlzePmzff8qmidSHGgMtZR1k698op_BWoxmjpoqSq7YIg1iS-bMqJW9hDRlXYafJqQkoSyksxBqMmFToiXn0pb9K-g1bzpr6rocdt_BWa_82XrCPdK24aUoJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=rww3YuN3Ne6huA_u648aNQbLeuhFY-wa8QTkM719HQEnnHvFvukWCqV09TYriEGb7GSU1b4k35CRkcpADCSfPNeL6ph_2_dyx8Q98e7RXnRBW4BcZLAS7Z-FWTzBnwdhTo8nfqEhfxOlk0XpA8JOJpve-jP12VW7fFzuG2GWA8Bqm_LWi7md2XCHTtxrBeNvYELzBDkn9W5TX14OwH-XQNe1VRrBptlzePmzff8qmidSHGgMtZR1k698op_BWoxmjpoqSq7YIg1iS-bMqJW9hDRlXYafJqQkoSyksxBqMmFToiXn0pb9K-g1bzpr6rocdt_BWa_82XrCPdK24aUoJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gCT2--HEK549_VwKc3JSGtj6a6ykdBo5Bl_7npIGO7W8WB3NMHpMb7dvLelcn_8XEuk3EoAfOJvjfl6ulfhMnKzGjXkBVQV62jVsZUq-a2qwi4pRX4fvvMzeToTuQsIP-CdNTzCfxuT0p8J9C-W8CihskwyJE4s8AX-zRihu0kxx8yxt_LZ3nOHUpC0pF4S9-45RU8ILqrwZmVOkiB00wU9LmKBMHA4GwvUpIN3PNYjak_3cGMQ5yGE6oInwj2DspIc_0qlgHquAXybq06A8yov9WFZCrg3dRDE6cJjsFxa9iB4i__3hrZS-disFt9Q0D-EwnwOM_FJNfAbvQcbU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ie0IR-in4sD2qWsI6XWfLhG8hG6feLMjhwXFFwi1dDejNCIshYz6rN2_e3TaJs6QNCu4IaZ2HKxnZoDbe20ZyIVwPQd_PtWeek05OmTIJ29Qo77nQ-IGfH9aVuiFJQgDV1Hypd85A79K1gaseOWpg2iVxUaejg7oPU3dEt3XEIMjFASZMkDMmBT0HtI51ClnjEzGgMP-6_M7mUtZcYh16wGEtDheBysb4XfXG0jhzk-1zhrPQmQoTPeMMC0oAJdOu2qd-nBRy-QXcXYWyTUCLX4BdsUTtRtxl4v7td2iCM_YM6dwKe8TbsuhS_uIw87bh0GtZZqhPU4D-I5HANb3eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNE3Hc4x-txyuWLDJKPc1X61qQD6I-e-_Ml2GktCdKSQ1rTTmX0Tth8nJa-kqRQcajlTyoRgG9cmypcTxTsLdlrCo938zP3_Lrp8vr4M5mK5m82v_dtHcJ0GeuMNtuF8D6jXCao3LniQVnzPkHdg557Ia0Pn68iZUKzGDUQXVP1j-zBrxtP-HIvdSSG2HhGhmk4eIz5_jzSmjGYjM9nR4xFpwZGoOhn3_wVgQsJ-3CTkPJ-8zq0eWgp6IYcjy6AT8aqbsDGIC-vZFWolX84U9_EJEbuRyQUBY20aC0QSsUrKKlrrgFIuqt0VJ8bBmmID-EML1UNybLQWTsa-ffrT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/succPn7xd5r7zhJBV26GaMRTf7IEcV0AAEHtvmrUjaoAssWHzj5Z986dLjhxiujnUUrJNULbu8CBxm_aWv10K6lDr7ySHorUOSa-sOjuHP-uLKphSTLUZBAwTQBjkvmUB2ZXwQTrE_uNrBCcpZ4r7RzUMj5dHCFPA6EtNyhGpmz_X4jiX6L5uHauR-upL7qCi9eQiXocSmFJl33z9CsXw1llzq_-SVYf8TyyQCqJL2EwOzyylEGst58dWbgbeW7ALsWyVuZIGC9no7vbEKnelyhwi3N0WbyDxsP_5jt5JjGd3Uz2wEZepJwVHUKfYmsGj0I8-UFzGAgh9ym6Wn94ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WEMOPHfpxpQHML3vyNct0C6ENgRYgwLExfROahCvcXLrhCx9vIKIz3LRgkKmMfJ8R4Gt0g01w3pmuV2pSJz16wZ7B3Rbjad8xj7TWrOnfuQ096Uyi-wwQXzhLTlAVe_0FZN7XoB38kHM8bRoQn4Qx1dlwgRDkJxmNjg84v8OkVRief6i6V_SqU2flCWYdCGRCXJihio_9QCYn21amNnoYjcy5n1rBcE3hA-SP1TCUlVv9-0gSoqVqacmSoibcQu1CQmb-q6nY0MsrtJnjqzM1HjTYzdRKBOr4eEYPgeNzCs1ZD5oT8fatGB2iSTgnX6Z91wnclEWYGEnGgAPHNJCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PpgQEI9PLWSdLGdS0ExgNApmDIaH5d7AO5_fPwUxhiadATAeOWYBxiTsNxpe_aO_Huzgz284OlVp4dHUhkX2A5OIuX60SU5BhA-bLp3CiDL7UFnzq_7dEuOwDEKn13jjIfePicOElBvFrVQsM-fEl8RPaebIPTsUd8IVOHrg3H5mvX4nGY_JGb-9FMu0-c_yvtGRQfdvL-Qu9zOPxa0iW9-ciUTnouYcaY8ukHjLj75IkYBj5mjv3etlvOWkLVa-TTgDWwF_sKf5RO5bIrsI5-77v7RX8Wf5jJDJsHslOTKyp6mTdjq76R4C5_jyb-aC0mc1IxG44QcEPBUdZDp87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=S5w9Bn9EAePhYaz7n1sfmwLSFpJLuw-27ZfB0aIgbq96EAB2UXOBt5XU7vjjVCbORJ_nCdIMLNySO6-5-NFuIm6QmdAbOczZlIP1vLZVrdobK5wE5gzU3gRArjfgpXTRhGW5CCtnI-tdI6slq2MznrnX6jfk5TpBZtknecKWxujaK8UPr4k9X_ecbzS3yeUKnIvrTvLhUllbzVOLyzu5j0IDfmpYiFrJCZV1xNWrTd3s4c9qcwXYgyBuhRE6FNEKvLDk2Yy3b6ZDn0sZ0JnKoSrCDTDVz3UoWMovrMfotP8JV5W97qOp3nfJ3clvMUMpGwKgjR3t3bXDmHD1UFHTNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=S5w9Bn9EAePhYaz7n1sfmwLSFpJLuw-27ZfB0aIgbq96EAB2UXOBt5XU7vjjVCbORJ_nCdIMLNySO6-5-NFuIm6QmdAbOczZlIP1vLZVrdobK5wE5gzU3gRArjfgpXTRhGW5CCtnI-tdI6slq2MznrnX6jfk5TpBZtknecKWxujaK8UPr4k9X_ecbzS3yeUKnIvrTvLhUllbzVOLyzu5j0IDfmpYiFrJCZV1xNWrTd3s4c9qcwXYgyBuhRE6FNEKvLDk2Yy3b6ZDn0sZ0JnKoSrCDTDVz3UoWMovrMfotP8JV5W97qOp3nfJ3clvMUMpGwKgjR3t3bXDmHD1UFHTNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPzI39nAGas3-BhBokiQVEBlsQqlSOAFttTJbTPh4U5tjV1X3p1BEFieanfQXA3APyReusvGW7p3k5dNpF9f4aunTNoVqOWVX16t0ArNGrPlrWFYDPr7EBKlFEHEi4uDtTLM05hKSc33Pc4uYs84r0Dp8mlfAXXahJlSLvW5lQiScI0TuflyBtu8KCVvNyj4eBInhi2R31EV963K8x67VV90epDrOofiQCWIdhDYVaoy2nZH_dLv8h4f_NxNhYtJAHyHdyoHDutBrCAzAMQkFWDtoXEv4eizsTnOZPeD1w4tqcyemLdNUKnjYAA5e8KHEW4Aq-hf4Gz-nBz2LMitpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQWYzI28xrMk5t9DD__IbgI2H3OSBpm5eWDs0U3EycaEVtIg69_7VIu2Wl68KZne4zArCmhjHfcmbwzEoFYxitYH0XyIC511BlLt1o2OYHCD07FuFeHwxUTBK1xDp_uAGnfiMgS9hjHt02wUlg_2ykpKrRSvC3Q3D8g1nwvcr-reKx9YqFCrssHtVtJIY3rpU4ehn5ecbaKCoHZQuEwC7KdMpC2ogZMKyJK7zchPKq8xjOiIdifVYd51F1U5dSwZWTz6jg6fp-zTyGDGAnkVOIBjMxUBIFc19gMoCR5vwngAmMZuN9BNFvl3HYugL5qw92SVLHYpSeJy1lJC0cGB_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awc8EUYc-yqlmChsN07mCPQ5inLL58p8M4imPInvNMJl1T81_6vReruDpHg8KcrSt0RraivrGAaAC7HX4U6LSj7BrLhvi-bdoLde79hxaeOjFmrg4XSetvNk4-OIdP3amJEpXhM1VhBE29--iSLWKBGyR8iTnt9LnivIT2lT2st1CL8oAzJfOMxV2bGjnTXg7riQC323cjg_MMyg5EUBHLzEwVqw8XJ67kjEdILXJFuIwPZ7NZYFQnngGLX84Aes3XLm5Y1XFbAt9bV8jABiUEILD_5NHZDeu29fkNBIMKZQBLt1j5P637elMzFYnnMnKkYbnOPzYjFOcvn2UbHLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=R6uwt6u3B3V_iiFh7F7rAaU5ticIrYgTWHC1p_RDIO2dqOGZ18t9ym3_UWtzJmbWkuIfoydrYFSHKdQFJD4I9xCwPPor9_6wHy_PPMUxw8qM-pgbMEiReg7sgx_s4aidT5-vI6qctCaCEFAS3GgZgnwnAQtiEpbgTNcsH-AHgAG3affrikO8TQMP7kQN03Y8NZ6ipMa3rrIHEuRkDRXfcFW1SrvQBxqYIWz0mBCfzm4LT9yO5PXEvYjhstiC8I1v7uuzT3I1ax6bfDw8H2mn7wg-TFvk7ApURfpWQlxF3vyG59xP5SVzcv3Y7Qcd0U0FSD-34Ejhte1BGZLyV8w8HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=R6uwt6u3B3V_iiFh7F7rAaU5ticIrYgTWHC1p_RDIO2dqOGZ18t9ym3_UWtzJmbWkuIfoydrYFSHKdQFJD4I9xCwPPor9_6wHy_PPMUxw8qM-pgbMEiReg7sgx_s4aidT5-vI6qctCaCEFAS3GgZgnwnAQtiEpbgTNcsH-AHgAG3affrikO8TQMP7kQN03Y8NZ6ipMa3rrIHEuRkDRXfcFW1SrvQBxqYIWz0mBCfzm4LT9yO5PXEvYjhstiC8I1v7uuzT3I1ax6bfDw8H2mn7wg-TFvk7ApURfpWQlxF3vyG59xP5SVzcv3Y7Qcd0U0FSD-34Ejhte1BGZLyV8w8HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LDSYfFRgfo8d0Lasi8Qpon84YR33o4IosKLMuViLtBwVCpNrgNIUpxV53qaS2zrwWCsg9tSoU9SlMnzagMDTxtRySA8A9gQvxlNlXvzrw_ZzNxQP6vtD_oIy1zGM8chwymfkMJf0LbCOfIG8zhmY5hZhiaft3I6FlSer-fYvCKVEr8_IBR71wsFg7htZt8mm87fzKBAEBh3XSMEUwzps5CLTe4g4WqcTmFdNNVskBwPrcBD96nmqG5ZaqXarzEhbDGEDY7fEKn6lohqpg_WiSQa7bfK-Te1taAn_LAcqetl8w0JhwNohiocOysxCrNmiz9nq2ANtq5Ha5dW4Aoq8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LDSYfFRgfo8d0Lasi8Qpon84YR33o4IosKLMuViLtBwVCpNrgNIUpxV53qaS2zrwWCsg9tSoU9SlMnzagMDTxtRySA8A9gQvxlNlXvzrw_ZzNxQP6vtD_oIy1zGM8chwymfkMJf0LbCOfIG8zhmY5hZhiaft3I6FlSer-fYvCKVEr8_IBR71wsFg7htZt8mm87fzKBAEBh3XSMEUwzps5CLTe4g4WqcTmFdNNVskBwPrcBD96nmqG5ZaqXarzEhbDGEDY7fEKn6lohqpg_WiSQa7bfK-Te1taAn_LAcqetl8w0JhwNohiocOysxCrNmiz9nq2ANtq5Ha5dW4Aoq8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSPQhPZiQ9wKd4Yc4vTbJCHPMUkj6OOlnw03MbU7prTSJJ_pfkoH3PH7YcbBPiuXcZ3k6zwlJYPeVJEGRwkBkQg8ysh8YGNDMNUugv7pSDCZ4eOGtnQMILAl1MLw_7j87KpV4uuE6UCXNjg9vlwl8EtxEWbBPMNLXdPQ1e4ZA8bOyUO-aqRk9cM9atjLZlTfbxjNAKTwpCcc0V7YKPu00CBNrGCH3b7lupMntQOK9EzDsuRkFOkGbP1asGLPpRSrUeAZ5z-F4ko8tCSVitdBo-LfHr_XEuORWsoPTsGf8hLyWFvxKCSJTz0b2YYYUgChLN1QF41-sxECbRtTFp8wnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NJd3GaJHGWR6z8l7d_fTiUJUNf6L35SbAr5ghDEdQCnKGAymDlzUHE5bmVXMK2eMjVsuhqyPqu0tVwLva1jNG6DHWHkv20lHkklfBmpy0dqJ0eex6KvwZmwlBkPcCzdLTQ90kueqC-V4Xgd98wEGCvC7w71gwkc0oxUE2UmWEU2ucA2hdv8Z6B3LRvbIfE4kRncY360qRI4GR98mz39ckT9fRjw_ARtFY8F_xc49wqXV4d6jVJGdjzDpLecru1-5ck6woe495bdyeia6yemROIu1oLYhe770vNIdQ4dusKXtAK2Zf2hfHJno2RRWAkArM05h9C54UJ2g7YBFkt8UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVztn94p0mrHb03A-P8PngHWjPJv0LlY28RqpwuCl2aPDaBScvf5SkRxtGuK09lx1I_CcHKz09BINg-W8Oahn8mId_3tQq7Ft2Yol4RwBmDwMFPZPGEY7muJsdmHKdDIFfJ7CG7A1JyCkixsidUteeVoCgJol6_gP_-DPceUgv6jU-WvvMzkMtZ_KHOqrLbWvxpThsoMG75f_Oh5OjZQXMUdyziY3P5O6WXfjAnXCpC2GEor25eta4T2fcC847XijBGhoMvnGJJuvQ38ZHHHZtxr1I-RWLn58ziiQ0-KsN86qbRmHE83HEGqE15nuLrch7hjIINsna2vd-FAZmMR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyMt-SLM75cGWdf9-tzVgOFounFA5eEKWzDroGLWyaYpbptu0M6qqXzl0Wd5VNkAgnXPG2ZCWR-rcTwG81yktQA0xqmnQxKpHNMxcmfIN0PaA4lEYYWFnUBI2VlOnaMMl2wR5yiie3WfBWcAzfO92FZ2VbYaRkYiM3hPwRXHlnAe3xbc2oaBdEETieFMJYh_U5ePEh2LbiGmgrs8ruTJhcY_YQMsl0ybmPWO05EV89qVWIFQUbzkGSt2jGwIrbHmv_OYvENrfFaNlSwPxlZG_tt-82013432L2Y1sYVN0eapIU89VFPKa32ND_qNZLh-ClPlsZwv8558fEbeThDROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMqiCXM43420PHWWXKzAY2wow1tgQYlYZUGQhV2-U6yjJH5pmTrRJKTjos_4slFmjnhOLNVjFV9bzf9xZd-wUO2RIHkBQKuuy45CNHDSFTOupb1CcVvwSI3g307M0qo2kTlolCM1sTH09MmN4gS76UQBhShjzWiJlInwg8-lviwakqd3bbN6wtKgue8eWMmDn5WCoBjx-VF_PZ0XBxKF2oE7J_vzL1HhAjrNFjhohYeDJ30GEyEG2Q4RlrPZBbajVYtyzVnBFVx0nGV-Ihplh4sqfhSlk4dVBONCd965ZK-OfDTVEZq6U3miXw3dYsT-Y3T8GaU_o7iiEkHLsQIvUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=e61qwCXBr5Dun4GB9WwOooJ2AP96CPURaTO3UwwImzDlQQrC8TKiexD-E8Au-6-wEkysjdlz5cFgGcgcp3kYKWbNXtxP_6MjtjL1W-PicmxRUQ0dRTbWTnID_byOx7orKeLimq4d9GQ7mGoTiXKNZg-xwFW-0o_v9BRFOAEgbrW0TVUr1JSb2cOPbHL9Dhh8CCfsvXTm9n3-GBzJVRzGzxiq7nJvmo8nsgW4ypPX0BYvj2Gmk9-Y3GI7EmryNv26uOKLtvWLGjmSuvUlnCcQ0IyZMlT_q6Xb9xttHB7UXL5xDzxCQ5vkcSm_W6A_6StY-WTgjNhx8t4l8iPxqTK7rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=e61qwCXBr5Dun4GB9WwOooJ2AP96CPURaTO3UwwImzDlQQrC8TKiexD-E8Au-6-wEkysjdlz5cFgGcgcp3kYKWbNXtxP_6MjtjL1W-PicmxRUQ0dRTbWTnID_byOx7orKeLimq4d9GQ7mGoTiXKNZg-xwFW-0o_v9BRFOAEgbrW0TVUr1JSb2cOPbHL9Dhh8CCfsvXTm9n3-GBzJVRzGzxiq7nJvmo8nsgW4ypPX0BYvj2Gmk9-Y3GI7EmryNv26uOKLtvWLGjmSuvUlnCcQ0IyZMlT_q6Xb9xttHB7UXL5xDzxCQ5vkcSm_W6A_6StY-WTgjNhx8t4l8iPxqTK7rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=tLhPIaksOTM3oD1gkqcFSMKWeKqva_DRhpa9ePWuVhDCNPGNmpUonyB8UdzAnPt6rWcDYz77TLgOGt3v2d8mzTKTtZckDpunZV0UAMOAYzb8DRsZBHd4CFf57cQ_-NATOBgL6GSIitOpX-u4zQYiE66Rd_dwSIC_XZvKz3pgwK3GxQYoPUWkIxqa63Qmxwp6KAgmbyhEaLkLYh1EGPrbjTaLKbLvQupLQIs_EAU55OfNXz7j27sOIoXU4VDbaJMqohy2h_WCsl_gmciFuFjm-XdXGYIJMDFXXdq8kCr0jnPeOn4gcvsryccO5yxsOi1vIRVJfUQmXoqgR9YdEQ3NVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=tLhPIaksOTM3oD1gkqcFSMKWeKqva_DRhpa9ePWuVhDCNPGNmpUonyB8UdzAnPt6rWcDYz77TLgOGt3v2d8mzTKTtZckDpunZV0UAMOAYzb8DRsZBHd4CFf57cQ_-NATOBgL6GSIitOpX-u4zQYiE66Rd_dwSIC_XZvKz3pgwK3GxQYoPUWkIxqa63Qmxwp6KAgmbyhEaLkLYh1EGPrbjTaLKbLvQupLQIs_EAU55OfNXz7j27sOIoXU4VDbaJMqohy2h_WCsl_gmciFuFjm-XdXGYIJMDFXXdq8kCr0jnPeOn4gcvsryccO5yxsOi1vIRVJfUQmXoqgR9YdEQ3NVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PS_UrsjJjbgjXc3xDVcTF2JE5Hh91leySepn9xmEpaVjjaT_I97KhabWlBtxBbzF9TMpF6jQrxkLx_BAiVoNvXqHSBBS4QyTK10o78bez_umNvkmr_178ZYhwwV9NE6zwRTBiA32GKpFJV3hvEfZFg8P4OrpzO3odh48WybQYOvxnl9_T_mutT375NEsvWId7X5LsBxZEDJjlOywTOD_7q0fSNsQJXQILnWBvKdW9qMJEWjx0mgMi3Gwra638fWpxawRiMxvVBta8PR7nfWe516xRkDgsFCS9Uhd0bGNJENzR7jSs63nH2whojpbj1hLGmL1wH5viSVJ84W6fgTwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/g0V3CRCpEh_fD5ISmp3VlBRwIBP1t2RAZGx50CMx2TnTUeZbUbUyhH4bNG8SAYW_J5v86QsUD0-0M4kVejbJHIoQ-tPjlTwV8YPIPccYrmitGa_jhVRJPaV2vIdrw_lBGAM0leeNxvIhw3ABg9WP7UOpGXzfLKzV91ycXuZK-FIly4tMqj69r88WPxLwt_K6UDuYU4hvAMIVTyKLG7s4fEsns0FRtNhJy4Jzg1Sx36kzSggufKyxTQtfn_9Vlt63Vf-Y9fJF1xRYDGnRJmc4vg0u7lpskz66xTCjrzySKmK4TtX-b5V1PF9HYLOeGvM-fhlehUO6A61T1VDt3ToZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRx8SyzvLhYo7bsIv5KPcEzPRAZ48ujqjShmF0SPzQ-JlyiLTSg3kKbadYCWLKWBaSCwjLhBsq-szO5zEBrDu_6KE66zfJcNuhmM8Ag5ZlNk-LkEkmEpTPs6H42VqmDWzSKGVg0WQWnCpNKpxFOM4XJE8RbuijyEfxXgLTj8wFfaOSGv_pjlQjRHess6FrL43vmN0bjfxVHyM5ExjyxL3OB-buDgjrn_QVUVdSbNNlx5KvPGymLuv6tPrf4uY54Mk-N8CEDS8dOd6YX3llRGtEm1f18Zau3uC6UF46XLbu7i4btKQYrz_hEjsU9fknFo-ZK3YwIFgdPlaf-BRkpH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBCu9Z6Z-8yUdsK2ybcUr-546dhpI8ZTAgl5IxLFWLNVndn7N-JFcycWyBiaFvTAMK4XOyxRsgzwE196WfNfmVWZILPb4z6jGH7on_rTLfW406Onj4tZ1M-_r2ys09uEA6qmZUMEAQGYVShXUqPJsc3g5Vu06UB5GKbKBHqWdOgmep7IIt4CXFyvniGO3kUXCz1WpGUB8d-2hcvzsItUz5Ex_6uz97k0eVXzp_cHIXoVgdDrv7pD8YLKhA1g_jbMlY_k4_vQ_DgUAV0OLec42eXQHs5f_ljJbKVW8izF1OwubvHY7vs296c6JIykgmr4R6TDm0FMAsyyg4jjr6TZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=IogxRLE60pH1eD_YS64HANon95Mb8QIH7DZzsPjBIfWH-xkmdGG2zBdFw60dinrkJ8iY3BkdkMSCU66KhW9Ft1N1vTNeHGKP8GfhOUhpB_1tmQVV4yTQeji8n1XG8oFcyzncND8vHlnTdydKLstKfvEuShqG5_i1qcz_Rqh2wKry4cwn8GIaiMtGRfIasSrvrKaMf1RQStuviNlYwWfiaFJaSeR3KWNKF17J7C2vrCGfsyp7KMmxMGmR62uEJXaHey6buKmOswB7OZDeBxAjstOexFwtUivBvVJb-stcbANWl8Zp-9IwUjVivPh_pcM20LaFVPYhUfY-yXTTI1gksg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=IogxRLE60pH1eD_YS64HANon95Mb8QIH7DZzsPjBIfWH-xkmdGG2zBdFw60dinrkJ8iY3BkdkMSCU66KhW9Ft1N1vTNeHGKP8GfhOUhpB_1tmQVV4yTQeji8n1XG8oFcyzncND8vHlnTdydKLstKfvEuShqG5_i1qcz_Rqh2wKry4cwn8GIaiMtGRfIasSrvrKaMf1RQStuviNlYwWfiaFJaSeR3KWNKF17J7C2vrCGfsyp7KMmxMGmR62uEJXaHey6buKmOswB7OZDeBxAjstOexFwtUivBvVJb-stcbANWl8Zp-9IwUjVivPh_pcM20LaFVPYhUfY-yXTTI1gksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml1p5aArZwbpJT2ydRrZQIRr8vq4rTelrrPmM8ff6kHrfFEYANjLCF9dOAqHN4klFXawnTDxC0cMuYZkC0MfIzxOzWSPKIdcnF6-XEC3ILh3Q1q-QVGpAiP3RwqIcE6zhPMxchgiO-fuJzkkSY-1UDe5ihZCzV57jui47WcomE3CAmOAdzcyOGv4kAIkTttUdQ4OE_XyxPo0TE9YsPI-8Q2jGRM_jpH9Ya9_L2iSM51vyf-JPU3K718wabtGC4wWylz-wLMGdzV2XR35i4f5N2NFgj2qb3oFKIuazpU5cEnCpvCZKf7kePLNaZYbZyoLbt-SDfs7cvsg0bD4_eu7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=hqFDdgyiropsrGe2bgq8q_D7IPJ3fwETtKIQEVW4BZsO-UmDbL7PSdbCoy-oBBzwq1s3fkbWYlmODoHsPPFgZUxIxAcHIamdaiRwrFY9K4SVdZTGwHKKnTA6BYXAcohTr141ysuyKh6Rwjyse7vhdxIJ8mc1QnzJ2yn8a25B82sigQc9Tu9PHDWAPX0Hizw6G22AV5j2GSFyNwBo3zyYG7CoICkCOSGb_DOxyUVKWGrFRm9gO_e6Qan28EL8Ov1sfYU8GdP8sHMOSrIRwtamz77kVbQwKYEUA0OzDXnyf-xTOBRMnco_kC7RwblT6Yw6ySJrpUz78Cbqyz1T09Pp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=hqFDdgyiropsrGe2bgq8q_D7IPJ3fwETtKIQEVW4BZsO-UmDbL7PSdbCoy-oBBzwq1s3fkbWYlmODoHsPPFgZUxIxAcHIamdaiRwrFY9K4SVdZTGwHKKnTA6BYXAcohTr141ysuyKh6Rwjyse7vhdxIJ8mc1QnzJ2yn8a25B82sigQc9Tu9PHDWAPX0Hizw6G22AV5j2GSFyNwBo3zyYG7CoICkCOSGb_DOxyUVKWGrFRm9gO_e6Qan28EL8Ov1sfYU8GdP8sHMOSrIRwtamz77kVbQwKYEUA0OzDXnyf-xTOBRMnco_kC7RwblT6Yw6ySJrpUz78Cbqyz1T09Pp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=fAc9VU7dTt-Xyh_ezaN-bS670GdYoKCtDHd22Gb5VhMVI4318snxtLdHCI8Ov8xgR0VSOm3vm8ZECcX57tycDArK6xzH1lNxtmaT2_NKEGmYPWPsXE8UC2exOdkuhq8PN2ERKogBRX8y0l8HNBElBopJ7InRoNI97K6rDwk2DBpynbcTrmOEt2QqppMrtHi-0KVOcI7-jO-dsxJ1-yMVobnkSOIjPx3JZTLBruk90wMjB-eCdAWWPmWXvJGhtukER0YDxsKseUnuPidqbJ3eYO8Fn5-IBl0mo57J8ICB6kjVnkkXbkZzm0KNymAlD8oSk6g8o7StL4L54ZhZgqKOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=fAc9VU7dTt-Xyh_ezaN-bS670GdYoKCtDHd22Gb5VhMVI4318snxtLdHCI8Ov8xgR0VSOm3vm8ZECcX57tycDArK6xzH1lNxtmaT2_NKEGmYPWPsXE8UC2exOdkuhq8PN2ERKogBRX8y0l8HNBElBopJ7InRoNI97K6rDwk2DBpynbcTrmOEt2QqppMrtHi-0KVOcI7-jO-dsxJ1-yMVobnkSOIjPx3JZTLBruk90wMjB-eCdAWWPmWXvJGhtukER0YDxsKseUnuPidqbJ3eYO8Fn5-IBl0mo57J8ICB6kjVnkkXbkZzm0KNymAlD8oSk6g8o7StL4L54ZhZgqKOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MytEHih_Izz7vFEhpdouwmxeMBtS4FPMb6QsOTtsyZfZ_wA80yNXFuyGo36LFLU6NZk0hWPX4PkMkBhP1SPf5ob8yHdZa_geMGMXDp8B4ihGRNMMOK8rPNhT8gAdXa1bJXfjnbFjrbgUIlO-0Kwd8B2JOXrGJFCl5o9dXyusX9lI-RGh6HJf3Ek5vCK7P8qbt8IJVBAJjaLsS-Jch5g2QJLlxmGWWWqr6ZoSGZncoK0DJ6vt9b86g3HZ0G1_QJjpWKG28GMlRNwUMfSCDdBVE-yI-Zs934eN5x_yGy1qo2xWasys7Xe2sI4KhE7fntka5-SJA_gLTZZdfpRa9QnCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QpAyuWe_1gxWthGk8DemYQ1uqgkAHmv1jEOuuaD6l-XbvnNnFmK-rrLRWHYHXr4lsA8jc7PUo47YbCq_eueBmEPdOVC5ewug3vIJcwCgsdbQtqcdMti-FYrok-wUV-XleSI-sjrobbiTwsQT_Ewd5xNNBC1LjB2q8zjPMpCzZyP0iHmf49InHXO3RSZsq8odoG67894tfaymms6U40OQce5GSoBo33Tscrq-hVwZzgzzlQZ9ZLmUXXxZR_LYBssyWZuL_nxQeuWVffNCwgkG83euUMSilu7WjG6Iuux8dveAMRsk-WEBiNRJwHVGw808gh4klviPRK_ieB4aNfYdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=Ugdd-Wi6E9zWaCUn42Dk3IhBf8VQ6XWDk-_6S-ZCUIBucrbYlcNi7aDGtICPPAN6vWuuTNi-AIDkV1abn35opCnzEwqKVncRy32LApgcpnQh6uY7jVTKNyklaK_RwKaFydE0JQnwsLWaDcjGxznSVqq291xLKVInJeWHrm_rEGzaPMSISYh82PssbQYn-yGU1cc1gs1gO-EoAdm9roHwBURBdZBwPNuQwWrtqr7jolMdkO1x7cjBo1X8cczscCe75HVNmxAcOqtxfj7DYJwa0f_z4nXSDJt3g6UDbUe87a_6Abm_TSv9mLE5i7uMwHeM6aHb-VrD0Ficf2hPcdxtOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=Ugdd-Wi6E9zWaCUn42Dk3IhBf8VQ6XWDk-_6S-ZCUIBucrbYlcNi7aDGtICPPAN6vWuuTNi-AIDkV1abn35opCnzEwqKVncRy32LApgcpnQh6uY7jVTKNyklaK_RwKaFydE0JQnwsLWaDcjGxznSVqq291xLKVInJeWHrm_rEGzaPMSISYh82PssbQYn-yGU1cc1gs1gO-EoAdm9roHwBURBdZBwPNuQwWrtqr7jolMdkO1x7cjBo1X8cczscCe75HVNmxAcOqtxfj7DYJwa0f_z4nXSDJt3g6UDbUe87a_6Abm_TSv9mLE5i7uMwHeM6aHb-VrD0Ficf2hPcdxtOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=keT6svS6XfjfQxpudx4x1l4RsA65P0vkFkrdq9rgT9jonbV5N8uH4S5qs_eHEQAQj1d9nHv_ItTZEO4f0e6skJp5jXzBwC-Pj1cQKNNT4crnJsvAOySbeoUBlaq3jHKk59ur0xXu0b_U_0nLUbzPHIjk1KCfrWWEhvY27GejqNhV6ook-5F6e9ITU8h5THu7ZDSpsqPfCGna_VfekNSwSOtPCX38_P4SMHGCF3WjAIR2S6Una5geN5kmPV9dGOG-q5AzFN-SBoufeqHXt51NU5l7BW0q50O0zap4rYLsBgFlkIUZpVEQzqvL6_OIul4moaOKAqLS2bOya-Di3XmAhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=keT6svS6XfjfQxpudx4x1l4RsA65P0vkFkrdq9rgT9jonbV5N8uH4S5qs_eHEQAQj1d9nHv_ItTZEO4f0e6skJp5jXzBwC-Pj1cQKNNT4crnJsvAOySbeoUBlaq3jHKk59ur0xXu0b_U_0nLUbzPHIjk1KCfrWWEhvY27GejqNhV6ook-5F6e9ITU8h5THu7ZDSpsqPfCGna_VfekNSwSOtPCX38_P4SMHGCF3WjAIR2S6Una5geN5kmPV9dGOG-q5AzFN-SBoufeqHXt51NU5l7BW0q50O0zap4rYLsBgFlkIUZpVEQzqvL6_OIul4moaOKAqLS2bOya-Di3XmAhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlJbJghvrHHbXeZdKcebnWf1DapxugjB1zFHsO0uCjZD839UQ1aLfYZ4B5OMOJC48NaqX-3UV0dHNRuGb57459aTTBMvmCDWuiqv62pHfoK8rZ0Y6hNhYz1gRbvYYIvQLfTA2b6pIv9qFsNJ3CtPEX7NqI4JiFS2wjpdatplzGg7RzpH-q4QMlSAbP8D4vcDo1rR7W7NHj2l9xZzM1TRE22M38TIKXfQBCI3Lq3bAE-punGtM3Z4BW_MzESl60QxnGJpA4ZgYicZRNhkeXAkRRcK_460HDcLlmrGXa1yNV66w99kLAVPhCSexNpAJBKCBxM9m9gS-NI93h8AQ2s16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRGexGRZdnqSwBI06DFQ1H24NeIdf2MuknPDwX-S09vTVyBtYFN4o9MYD1VwXNQPe5-HLjRREtzcBXqOzl352uXjclJ4K7luojVhaYIe48eEQroon4BppkRgXU1tyWMvyq8gYMtRfTGxzzhRTzpt1QcsuQAZX5-vYRyRPO-EMzTIecdF-wtbpeLvSTfAIwQaRLUtmVayZbiZolGUapdHEOUc1qtFHyQp3d4KuUckx7tLJpKRbpSIrOu4pnShQHyPjwEOIK93AKM_stHSvM3mPwdK-gT0kF1-fJE3QKv3K0vSDdh9cbt8ePqqbVD6HpAQKyHNDW3g1D8JpkPJ7H0z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tT-u5Akz_MhVhqFacVd6OutLQIy4Y1k7yBXyw4QNdopWIzM4SxDPePBvuAMtOB4ihYixWsxwJOrgWbzGdmKtFmK2oqH4FDsm6P7NhQf3-dKaSpZn5KDqR9Q94z3vwzSAYhAK7rjJFa4jHSlE5drlYg28N8ZXBsO8-B50JAMTjD2fZHmlTVr78rjr_gb66inx2_J1SuYc5lJc-uOJxy3NlE0sr_BbGhxN7skHgwleWQ-1vVHe_Yzr-hGp0CoiteeVUqJ_Xr2zTA4l_9D9RGaXixXWoJVqTNto6zfs8xm76Yo5T5oYG3EANIT64PyyIBkIlqI7FUHgzEZ9gxL-Ic9RbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axDrRpFkZU0LVDEOko_b_MYqarhOJZhNeBLM2NFsyOopbkuvyEhRVwveY1Ck-ud5v7zTdTSSHyDaEErkBYb07RDptuW7nJF1O8biuYVwbqrjSa_pGS2RZMp5OmCybsNx8nky2KMraQvNqOPVDFztLFajdEdGGrOxLWkXB2llImhydBN8WT6ZOW71-5-U2_ic8586mvmm7Vfd50umzMApKc0YjXs7WChDUJ4bQPdJ2e46XLv8xO4zTktzjWtk8AADM3ToF5-nt0k3ar_iVktgv_3BNxvJktG2NXREWAW_RDHH9VeY4yODAqr8pd43hau1WSatUpWGN7bxAKPbWi3_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
