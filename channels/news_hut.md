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
<img src="https://cdn4.telesco.pe/file/v8PzzxOhu63Ov8gWZOYVU5XEFB8I1Z4hdBsEm4_1oC0ucECtjQETqvyHUnSn_yVwAa34DdiKiE5xLQDaQVkD0w_biQgmBK4-BGx0zxBSOTfYOCN8v2-J-LyuJkdzLEmZ1ZNWBsIIpDlRZTbJitdfg-U4-n_XcFUq4EzlKYb1SAfDf-D8QJNFyCGABOtPDItlJ0r9MQNnaeNAQqrdFA-1Ok7e0ygyyPOEXfceZPvzYVSy7n-VdrhWts68XkcF_vOiweg5IWyhhzQzV6WV5Ise40vNrOTYsbwKan6TX5RYHX0AYx-y4mvnU4TMjmVTM6IboyhP_Ieer1YDDk53r-_QXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuWa03tufeLY4c9mcM414FJCFRa0P-Kgn3BTe9xlOEYx_bt30NA_24JZOB3KbXw6UbMU4ekof065U39rhwUDvQwwiddNiz8uxL4h72rrCKt3yyqtDqE7AqhlxgQWHPfsav4qVzGEztnWhKI5UsNDaRG1963xABLdWEZVPZjgS6O8FlEpyLYwg6i-Uroc1VkXjpobFTZxZJkSMYHxfmFF8Ca9n9geQHuibSv_CBnGKTgh6bsyVW34KE7ZIGZaLvrHKyxHfheUZtKOVA_Ol6thNqxnQWcoRcXfh83Y1Augh6FrA3ksEq-H4lEiP2RfH7Y21DLKt7w5MS8LaEhulPBXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsAbBQ4B0aVXX27SRjTVZ2IacBEkz_DEFJcV5Q5MwMAN2BF7wBCJodnesaqCeuLcK8XlcBk5vS3NTahQPbLVO_cc90LJJaE0xmYo9hvWuVuHenS2qk61GNSuamGJP2RiM1gGeIwHGLNl8hI5R_1uKKDlnUYSOut8YIRF_UQSj1nhh_LzxLTsULpQQrRb3RbNf2VHGLOa4h9EuVks2iGTRWcAV1ljlyrwsC7XOz3W0U8jTZYyCU6zs_W0lvMsQBqI9BVwnT9GlDifCQA8bQD-CKSE5blbQlYiZ4yso3Y91zrcP7_i7fkNO5NSr5ezxv-IW9ecTRPJ4M8r-aGLCBTeEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=vgUZfrqujawumOMQSSwYWr75Oi3HkTm0l4Aia4-XV2siYUH4CCDt9itwI8t76eZPuauVg6_DWAm2cpZvsJC0RDGBATaUmfzSkj_95sIlqcwpFWjPTDzv_c9gO1eJDFkVtpmG1KSr-z9nsARmA4Jvw7q6Oj3lQQb-6uvHcU24umxsS6afIIx0qLOm9xxPQMp0OD5mBlfb-KcFbzH_EMTXQflnPlD4Hu4sNVUK1C4Ti96rX8ZNnP6xPZLt3R-6uVXYP4j9cOwNKaqm9RCxwo-Ie1XEGoBjrb3jDlCvbHtum_1bpdaI7Eb-6EtUiQ33C7RR8E68Bzx-DkiwnTe813PIWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=vgUZfrqujawumOMQSSwYWr75Oi3HkTm0l4Aia4-XV2siYUH4CCDt9itwI8t76eZPuauVg6_DWAm2cpZvsJC0RDGBATaUmfzSkj_95sIlqcwpFWjPTDzv_c9gO1eJDFkVtpmG1KSr-z9nsARmA4Jvw7q6Oj3lQQb-6uvHcU24umxsS6afIIx0qLOm9xxPQMp0OD5mBlfb-KcFbzH_EMTXQflnPlD4Hu4sNVUK1C4Ti96rX8ZNnP6xPZLt3R-6uVXYP4j9cOwNKaqm9RCxwo-Ie1XEGoBjrb3jDlCvbHtum_1bpdaI7Eb-6EtUiQ33C7RR8E68Bzx-DkiwnTe813PIWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=Z4H8rXu68M8gbTyIOru6_q1y3gwzDJ7RFtfitbNo9Rzaqp4g-1USJp0UOm7DsAJxTQ9TnSFCMTZdLzG6mHRm_K9Ulac2t1ZrYlGFfqTEPte9F4b_ugdjXCHA396IQkhZv_HZ0Y_9HgfcnEsA4_xRic7wjxPw4hCLiBiPFjpPtByOyryKEhHYkEpGwug-nKNZIt5nJVRbgKt8U86Oyp013XdcIi_94XUrDkdfSgXLlW9ZKwEpq7ot5HGk6nLW9cAMPofLQSKZPMQurXxQT8iRN4aAxoMs5AO9Z45xde0k82Nu1YbzMv1adKaNp0ECpcsr8GJ0zCWuZLjV1EZbA3A8ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=Z4H8rXu68M8gbTyIOru6_q1y3gwzDJ7RFtfitbNo9Rzaqp4g-1USJp0UOm7DsAJxTQ9TnSFCMTZdLzG6mHRm_K9Ulac2t1ZrYlGFfqTEPte9F4b_ugdjXCHA396IQkhZv_HZ0Y_9HgfcnEsA4_xRic7wjxPw4hCLiBiPFjpPtByOyryKEhHYkEpGwug-nKNZIt5nJVRbgKt8U86Oyp013XdcIi_94XUrDkdfSgXLlW9ZKwEpq7ot5HGk6nLW9cAMPofLQSKZPMQurXxQT8iRN4aAxoMs5AO9Z45xde0k82Nu1YbzMv1adKaNp0ECpcsr8GJ0zCWuZLjV1EZbA3A8ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHXak9rYBtajJSasGcvJ5iB0gaykyin-dUn1tno48YB4e26agYecv_BDoGVKOXbEzOk64aMGUOqEDYEW9KC53GCl71rxNEvwf3eNyC5TBn764aX1NfFA83KB9IaG_OplYFwioxSGhe8w3gIzCLEU8PP7XPdv_ddPi24Ndisc8WBwGaCJtnaR4GVoZ5zOwj4v8Qyl5v69EJVI_d0eDa4bJK7hlSkDvDmJNfpaMW40WWk9_M0l17wGiyBaE4TWRw212bqVogiYCIyzUqonbWSdcAD0wrYOVnwRFUAXeidcKL4DZ4Mg7Rvpe8lqRwNHgFL_db2ecgg3mBWHbXWziTJKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=CFOBUXRcGTlLvgucGwlfIk1Uu1s32iXgbdPan4LNrhtg2xNY4fd-pNR9PLnZZHC6cR9kWA_bYXdFOoP2_cm9NHUoAT4gdFug3pKil28hs3qTd9RVSmGGQ2JUz9yqeFg3Ou0HXKROBwUjAkxiqKjlarLsMR_vfAvQB4wDsWYm7UXsDZfVrCOIW4UF1vJs858jxl2Ewocu1dXVN8Fk1HUWsXEthgI8Ek2oTi7DR8L69RdoPkdLMYLbJ2RzKMvhV3wlOgbiRP1megkTeGohX1vqkrGTtMN26b80BtlJZwQoaianysJNGjsbvprJ3HwGGGt9_5EO78jb0G9Ca4-bPc9nZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=CFOBUXRcGTlLvgucGwlfIk1Uu1s32iXgbdPan4LNrhtg2xNY4fd-pNR9PLnZZHC6cR9kWA_bYXdFOoP2_cm9NHUoAT4gdFug3pKil28hs3qTd9RVSmGGQ2JUz9yqeFg3Ou0HXKROBwUjAkxiqKjlarLsMR_vfAvQB4wDsWYm7UXsDZfVrCOIW4UF1vJs858jxl2Ewocu1dXVN8Fk1HUWsXEthgI8Ek2oTi7DR8L69RdoPkdLMYLbJ2RzKMvhV3wlOgbiRP1megkTeGohX1vqkrGTtMN26b80BtlJZwQoaianysJNGjsbvprJ3HwGGGt9_5EO78jb0G9Ca4-bPc9nZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyih2pb5HXOREaTD8ppws1iqwzHPdZ1XKjxWI8hvlyhDgSiEk2Qutb56UKEQ3ppO3A62-7uYin4ckuN6TyyBrBs9XN7DWi_ZOngT50OJbnq1fgr435P4A4k9AJAFVBZHZLvZuRPNgWsWSR28bYrtldTCuZizhzuSfl3YQnoJ_Yhfxf0k3J-eO-J2fMXVmZoYlIx98KtlHF14p96pecsJnyloKQRwV9pHts0skrxOzXvX_jr1atMC8qj-pDl12GjARvu4ekIgHCjLiLHeviQ8oTNJAeJg_EbIc3kMtiukWNsNZO9G2erh7Y-xtcporgM2zWgSOXWf0J80Sz9c49Hjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9W5BJcyiMm7ew4-HP7Qjb2AiRKZrQrhBlQSV9UglTYXh9mQFp9URRUYiODNdOwTM1uqmFFLmKDf9uqFxoWZUYO1IM5lBhjbUKEFwazu96t2-ZeAh9jrGA9TJdOdwEyaAAd-W-9I_m31RLHxDS7HFldDRknjtemfSkPSBQj9i8P6QesjXd0Y2-W_jPDrQu0Pn-MYJAr0aHzdQbsc2k8LA1a2ZsNuVTh_7XDCwgAHGZKpy4dpP8TNIGGD6Pw1S3Lq8a8eaZjnlYnSGl9H4A18Q7AEcasCoaJLVSk686lbbu7_FudQGuwn5VSWi1_SJnFCgme-1QG5F_KVQe2u4GkiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=CFnnx4seYcbmN1gBcdQmuWEkzhxHbaal6TEBpi0kX4SmCA4bPIdyecCwMhDMXtlfaHLlbzbxvlxxPDTmyXgDpNc2eHsEjimP-arhqa0kjXJewhG5OIIucrnd1HYqhILaD5tyuSJu1ZTGrKNYBjKCDsZNmWeDddgMJqqwv0X9I9A4AvmsrFuI4kJkrVRCS8sCxg5Ex_ngzYuc1UO3ZQFnpJAb1SAwu5ZX9kcLVfnB7ioGhH5KCFowLHwWfuh3gIjS-2TdJ2aF75OBikKVsCsRhdFoKwDoSvKAs86xekQQpJ6PSPLKBBqfuiWYl1BNeWyfsrKktVUYStqIhZGZSUDOkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=CFnnx4seYcbmN1gBcdQmuWEkzhxHbaal6TEBpi0kX4SmCA4bPIdyecCwMhDMXtlfaHLlbzbxvlxxPDTmyXgDpNc2eHsEjimP-arhqa0kjXJewhG5OIIucrnd1HYqhILaD5tyuSJu1ZTGrKNYBjKCDsZNmWeDddgMJqqwv0X9I9A4AvmsrFuI4kJkrVRCS8sCxg5Ex_ngzYuc1UO3ZQFnpJAb1SAwu5ZX9kcLVfnB7ioGhH5KCFowLHwWfuh3gIjS-2TdJ2aF75OBikKVsCsRhdFoKwDoSvKAs86xekQQpJ6PSPLKBBqfuiWYl1BNeWyfsrKktVUYStqIhZGZSUDOkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfZSaK00HcDi6Sw8qCbfQF5zcVJbSFRLGBqW0xjrL3H3k1CZ03_6TMl3JZKApTnWuf2OTSMNYALgp9tfvKT1bIaVcRhhYPJkozVXErUDPzEbDDeS9TohZx6hQ73GkCf7m5akv-B2TyWpYpRvW1ww65XyBk2s8qUL04MBUXWbM_Ah4DpcAEv_ztLu6RkmmL3nYJ5nPoX9DG_xTPxy2rgiGREAxl8IHaIf-XcriDXwZaNlIKHRFTgl67C2n_tCllPiiTuA2fVoYX_c0jzVDpFQ-qj-FUzM61AEGivjoPfnNwJ6PD1c9TcVbSoBgVeyIUUJJyh8NpRrIp4Agv0b-xnQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEsdyeg1XnOYNtdV7ofQ82cY-tGJm-NaqwK3zOuzZkymiNc9lK8CCvxRkc46lBGd-0nv2X0aMQekQSmP87WIJc4FR452qMGPj-9xdZvJ7OMK4yZj7gVqKDo6Pa0NAKvt3ulDR5wGAL3QeOWUwd_uuOGR9bfqw1tkyNd5F1TpJsN72pALSkHddSPjTiNx8JQyJQaZDo09T1L5viFza0QP-MFcIwIaBWFxapvFik4IwKNleCKtRd8aVyU83TkhxmCtZMPf302578afDux7EQc5IGje-TX-Reeh1yCFpcRVJdOiqHZ6M0PpDgiweNRbNgjW6NUOOucW6tYCqKhMtEdIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGmNRpuCsFSi7AGSfZTytcknBCI-BJbe5Zr1v62AE0CQM1g-vHcZPApcHsxWNidbfOTU6OgmSdFUFGEhZ6NImoM9T695iO8i_tQkmWwQ8vhpmlgkYt48fRM2W3r16Wb5lFQxWkHeSzXjV6vPs0hqpP1ssrtTPnF1T_-48ynnUqcFGZq-TovohedG-Jso44L6bI7sTWU-JCyLU7XaYK_BkuiqSCHyvhO6kxYeUiXVr7UFvCS6fs91ykVwLnVmYIsQWFrt-Z43f76GqpWX4zoSdoFal-y-ynrPnLb21RrSFR8UrSIGYq2jDg4QIGqR1sxyT3GwC3g8cOzv4yHMjwknRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mpy5lw7UdiS3Ytv_erCydNIMwxbcc9wKVqnZnuWbyn6jtgkEKKrvETP0yz60MEa5NvkOabJNJ2Br61lvEqYg92ISUtN6xPFsRAACTgCKt0f9HwycnDC5Lmtb9BH92SqcY85iI0VogYsNFrRuZ85GcbRnQkfxU6-jRaCJOak8JezdeyUyAS8wPWjd_kOz2x0fXk_wIAjzqjK4GXCYK20AtaIZ_HCUifw33c4cVQ3TVEeI7xJOVnyVLPegVYeUtYPU0teT5qswB9Sr15O1fS06N3CZ6eMy1obOdAeZjg7KwumCntJaWgaL-kZ15dZlW04XlD7KbikMKZ8c7krxDxx-UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=NVBbkKC4xTo6btyNpJPS0PTCLP5M0F-D-JLHLrRYQ0embx9sh0y2qZCDeBKjSsP8q7bMi_CNgzygoQywXxA3L_adczDdrIL3vHRQx_9KxxMK8NffdRwCt83Tjq8I6VkDlNgbyXg_Pex2cvi7iHlAspKzlSVTZlznRyiZYx0vx1HTCI-mhYLg-w8B69K1sOmSdIwYZRd6CqB2Z8xptFD-K5UfsYdl_HO8ejp8LdQplEgY8YaN4VUZDsdZlTRVCcpR_raBSqD1JeMcG3UAa2CGv3DOauTeJfKK6plfuyhOlVYFQdBa6dXmvL8dwaDXCMSoN1u38GobHUJdFn6jRkFFXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=NVBbkKC4xTo6btyNpJPS0PTCLP5M0F-D-JLHLrRYQ0embx9sh0y2qZCDeBKjSsP8q7bMi_CNgzygoQywXxA3L_adczDdrIL3vHRQx_9KxxMK8NffdRwCt83Tjq8I6VkDlNgbyXg_Pex2cvi7iHlAspKzlSVTZlznRyiZYx0vx1HTCI-mhYLg-w8B69K1sOmSdIwYZRd6CqB2Z8xptFD-K5UfsYdl_HO8ejp8LdQplEgY8YaN4VUZDsdZlTRVCcpR_raBSqD1JeMcG3UAa2CGv3DOauTeJfKK6plfuyhOlVYFQdBa6dXmvL8dwaDXCMSoN1u38GobHUJdFn6jRkFFXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=RL6fttWafvWD0G-OeeJOKTBniBl9kAaNIQhejhvKH78WsJC5tWD_Zc3L1W-dP3W1LcfnVVg9-NA9ezi8TOlj7myu9q3lspmWUE4vtdSOnvFEeFBGSpq6NUQvho7hymIKxhaGynWjbX9_MxY-RZ2eS807dBgv06QNGNi5SG_duOzRJMEj_J2YNKxkx9HuSX3KMFptm4j5VkkhoHwPMUbM-NLksB0Kh05trC2615k8JxTeJfVUKZHyRbg7kKRKFKQG73u5EVpsljcXT_w8kHHiXkKuIStFyV6YtU1h1OfAuRgH7iD_Q24Xy525p9jWwHMLVnnS3CefiHlSLdEfOZIUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=RL6fttWafvWD0G-OeeJOKTBniBl9kAaNIQhejhvKH78WsJC5tWD_Zc3L1W-dP3W1LcfnVVg9-NA9ezi8TOlj7myu9q3lspmWUE4vtdSOnvFEeFBGSpq6NUQvho7hymIKxhaGynWjbX9_MxY-RZ2eS807dBgv06QNGNi5SG_duOzRJMEj_J2YNKxkx9HuSX3KMFptm4j5VkkhoHwPMUbM-NLksB0Kh05trC2615k8JxTeJfVUKZHyRbg7kKRKFKQG73u5EVpsljcXT_w8kHHiXkKuIStFyV6YtU1h1OfAuRgH7iD_Q24Xy525p9jWwHMLVnnS3CefiHlSLdEfOZIUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XItwumGMDwcydpWj8T0NxamqJfLOvtkYqIu_jYiYZVEaeeT5Mq8fjDqsxIokzCjdRwQLIFi8ggz7-oExapo9TLX-8I8jX8kk0Mit47Wov_xtGjcfDFEkiuMIvRXdw-0IdurmPDX0yyWhyNsH22H9ZtXFj85VBK8WHba1cy5gjdq0wdtxINTUgU3dlIvpCyyHJT0VGM6eUQlX1Mxc-Cd7R40c6Aj5wMfdac-INvR2tFoRAx-5aupfui-AihBTqSaJpP8lGsbZo6GLYecJiptQy7vNSK95ZcEQoEuW-4y2REteeaGm5S4pqh_99qTZhVa69v-gsnl-PQHDxSdQ5YvxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFEl8X_4L3vWxiHXcQ1g7XelgTj0ekjIqDgJKbAyPx6ylvlDxdIjNC5tYkNNoLJFSljU-lB5_qtBUFnJCgPpx1CkUZeqL2aJP6qPv_KJEtMzybF_qP613zp9BhKtLKo18Wfk63VJx3BaYHVcm3VU4P_Vr21W9BrP4734uGRtWuD9UrAgRPlDo5VGMVmJ3mh_Ts0XkVU1FNN-TjoYTdFOntBSlh24-0G7-eyhzUVi3vzyRRTC7vtvX3VycGNZmFvdpeDP85djZHWPslEMw0KQsEK0Qmsshwo6bfzHwsOcDWK4p6FtQVXDXHoBIMj_bX68gjHODzuSOeW-sB5LI217zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=gtWnFjzNDHDfIpzEotTKx_JBicrSnbLtRYepdU2Ihb5ykBqubzuvAmbO7nd6GSOZYf5-BvPtiGwZuEFGmhfoBuY5z8yIj6eomrQPPg28b6AK8kSB07Eq--MlgawE_J66-WD3di4Lw2dw9_WX8bofVmf4XRzC1ueKgiQsQcyxW8ykWha6EeZEuNmKNAUFgMTVUOKka2L8YJ92ejOnA42W7_Lw_ms0WVabrxUx0HNMJhnUv9u3jkrriR1W2vkNKTv9NFNLqq21Rk5UktoB70zPiXHlQqR1gWMhjNWSzEKH3frjVDd6XxPDIveDt2nxToZNhmSraXW9vUt5SUM-UshXLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=gtWnFjzNDHDfIpzEotTKx_JBicrSnbLtRYepdU2Ihb5ykBqubzuvAmbO7nd6GSOZYf5-BvPtiGwZuEFGmhfoBuY5z8yIj6eomrQPPg28b6AK8kSB07Eq--MlgawE_J66-WD3di4Lw2dw9_WX8bofVmf4XRzC1ueKgiQsQcyxW8ykWha6EeZEuNmKNAUFgMTVUOKka2L8YJ92ejOnA42W7_Lw_ms0WVabrxUx0HNMJhnUv9u3jkrriR1W2vkNKTv9NFNLqq21Rk5UktoB70zPiXHlQqR1gWMhjNWSzEKH3frjVDd6XxPDIveDt2nxToZNhmSraXW9vUt5SUM-UshXLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=plV2bf25e_WXFgL6s3sOwJjTlO37xaKk8ODBlJphUhCrupfnh80zEKjij7gGw_smJQr9Y8jbVc6iRbl_CdeDoHbUuTWCbwMxy9m6hQXnObHaioMwRqUjDKq_JelW3cX4tReZzYc-NUJA56-KPpohGZxaSRKz4422AHT2vrphEVFOYTOdRTvC4qdcsXbLMWZNJFHfvpXzFBTz2L44L8UqVCXQLlZknzuiNHyIlEcSVRb97o6CPR_HAA4nbnVCFzNKXd7etUttJX6KSpCuCr9Wf1pRCT0EaordpJbPYH_hpylbFOvI7yFk92YfkKn80OInSjX-0lJSL8h--NtxvbxUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=plV2bf25e_WXFgL6s3sOwJjTlO37xaKk8ODBlJphUhCrupfnh80zEKjij7gGw_smJQr9Y8jbVc6iRbl_CdeDoHbUuTWCbwMxy9m6hQXnObHaioMwRqUjDKq_JelW3cX4tReZzYc-NUJA56-KPpohGZxaSRKz4422AHT2vrphEVFOYTOdRTvC4qdcsXbLMWZNJFHfvpXzFBTz2L44L8UqVCXQLlZknzuiNHyIlEcSVRb97o6CPR_HAA4nbnVCFzNKXd7etUttJX6KSpCuCr9Wf1pRCT0EaordpJbPYH_hpylbFOvI7yFk92YfkKn80OInSjX-0lJSL8h--NtxvbxUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=MK8nQH1OIYmj_2DOSI4QGOEqTN-2izHtnEPY92uDptApHNV03XKQhdSdxsHdzPOrGWMzOtpapbYM_2osqa6GQFlqBcbGJbB7db9COQfHIkq1OBG429ZWfAl6utwZ3U1lyhgjBrM5j7qIGL2tf3yAGREr-DoaZqIvy2r4xwAkHkDFsUX5rYbvzLKk8yGr09FsMwYfzb-XiaDtLZZKy5Nb0wtoJSGK1e1GHyFaecNf1V7VTozeV4B05prVGsXmK-oHQ5Tqzv5qo7o5OYSZMpL2it2ThvYay5JoKm1JPbvtFgUogv-YU0DVfceKXcgvtti3i_JTeyB9b6O_hVGQy7kvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=MK8nQH1OIYmj_2DOSI4QGOEqTN-2izHtnEPY92uDptApHNV03XKQhdSdxsHdzPOrGWMzOtpapbYM_2osqa6GQFlqBcbGJbB7db9COQfHIkq1OBG429ZWfAl6utwZ3U1lyhgjBrM5j7qIGL2tf3yAGREr-DoaZqIvy2r4xwAkHkDFsUX5rYbvzLKk8yGr09FsMwYfzb-XiaDtLZZKy5Nb0wtoJSGK1e1GHyFaecNf1V7VTozeV4B05prVGsXmK-oHQ5Tqzv5qo7o5OYSZMpL2it2ThvYay5JoKm1JPbvtFgUogv-YU0DVfceKXcgvtti3i_JTeyB9b6O_hVGQy7kvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw872ibYpjMJoSRZEuRV5LmU_jErSt1HQn0mGTvFhYwF78SHm7x-rVvyrl3doHMNn2mXmEIVr_Escqys5s0LVeg3Mo-cVgfz50UcT4TSP5JUN-Z5I_h-xb4nAMrc2D2dVJjrd2zNnnZZnBONPLjJHVZjEhFNWF2mxLTEV69KXkzLIQ4dO5FyIl9teE_mVIaD-F-4tnoQqNCtefRYY2N3tgVHOJC1MFh6Kc_MRJTXZH2F2RyQREuFC9tVtCgf3WdesSzBHcMik6taKSTEpeYocmhpNM9OdaziP6e75MMNGDGREE-UWgtlwPHxKL7ov6wsARSehdKeLT8B2vgmXJzWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLgi1N-_1djW0HHzwd3kZ3WU4mIBG5kPplN35-CH9DTx6l_o1mJZpKa-MQyTj2h6jFnYr4PRk3vK-pxGJK1GPR8NTd7yFE0JpqtQGK5rqIDP65uNZUf2CAeJD38ogV6EXGglfwJESnr0_rsYLH5mBhH0Ym9d4Nd3b7JwlpNmK9nVRHTwxjaPC5E2AhNfBbaAnxFvM5fJ0_DfFMCnxUY1xPIuhXjdmRM0Id35DR0MeqtHJAWgrYNQ0KjrGfFo24jNvKpKQ_kKqrY_rbTQOLSOyIlrRaRtrKxqeDGmYNDe-kH6NDov-XaRhGIyFQ3O1PPMuIjoiZwteS7y-6oNt7R3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZUv8dTG9ngk2piIBTJbnZQ7taen2jP-TTHzhSdAvtLWUYhMbf0OKMhplwudhckKNs-45VRqCjr5WkP-GHHIBguCGZP6gPqjGk4xkAe_nh4evq3MrN7KhQmQmInuC_L1S6UtB1aBPR8wEUIfbIladax6bE2t9i9UPYxQeBvEKVpOvQW8N-wIod7YYKnJRS-7uosZiircEemgfmon9eIdNABcfVXjnS0iU4snoy_XyyybBhW1stvW2HZRlxVCJvAWfQoSpvLRAXhsFKQEqzg5phQvyq-f4F6Z_7foNUJAKx4vFhQsGuzVJDlEM5LVBd-IXlq-ntavyuB17XauwtUmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=Oox6I3GNtMkCy4biwbIjycAJFAmF-z5NwHs1aiDwAHw_L9Wp3qRU3DIhc4K3fA47ZEoRwfIgpkcPlEwOFzd50Qc6O453atqm9xvXIejaFaKLk_4qZh_xSDqLlc3wMJB7Wev_zV5ArTinj1rZp5yph2Q8gV0016eVps40QFOgc8ZZOTu9-WwvaqN-Q_70orMwyukJoCfSpbBP5NaLJCqSDdKpWAtz_2U_vBupkM2fHD3m6NLnCUdU5ARfGJybJxFsNscJHVeCX_h5V-z0ytjVlcnJTiwqXBjodI7rBnAafW7hFZnixCsL0HL4Lmcj2Hg2AdlSEJ8fYUKjG70ue8cq5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=Oox6I3GNtMkCy4biwbIjycAJFAmF-z5NwHs1aiDwAHw_L9Wp3qRU3DIhc4K3fA47ZEoRwfIgpkcPlEwOFzd50Qc6O453atqm9xvXIejaFaKLk_4qZh_xSDqLlc3wMJB7Wev_zV5ArTinj1rZp5yph2Q8gV0016eVps40QFOgc8ZZOTu9-WwvaqN-Q_70orMwyukJoCfSpbBP5NaLJCqSDdKpWAtz_2U_vBupkM2fHD3m6NLnCUdU5ARfGJybJxFsNscJHVeCX_h5V-z0ytjVlcnJTiwqXBjodI7rBnAafW7hFZnixCsL0HL4Lmcj2Hg2AdlSEJ8fYUKjG70ue8cq5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=smoRAa-ik6AL-anpBw0K-K7kGq4fh86ieKEPYPjbSL6B3vJtSU_jvzt04FWWf7tOhyBV1B-dYUvR6aRhQUNHUsDIpuDx_o4QT52f563nEWRETLRGouscImHAKldGGY_vrg7U-gmLVcUwUVCp8XqrQwX7Pxo076iuSDqhv2M-clJlWDRwLEkA57ZHmYY2o9TmsQISFvtk3gjk_yNjm34XgGFUsdDj-LwHDXx196_yr9S6Xm3O7Z9VIeLRBQcIfHRPIJfoiPdUI3bJzDQl6QQQd_H1iHP65u_LcysjINWb4ntpXFRZIehNwCQUlpOcJ5mOValx9rsjvgqSOE_0FHziMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=smoRAa-ik6AL-anpBw0K-K7kGq4fh86ieKEPYPjbSL6B3vJtSU_jvzt04FWWf7tOhyBV1B-dYUvR6aRhQUNHUsDIpuDx_o4QT52f563nEWRETLRGouscImHAKldGGY_vrg7U-gmLVcUwUVCp8XqrQwX7Pxo076iuSDqhv2M-clJlWDRwLEkA57ZHmYY2o9TmsQISFvtk3gjk_yNjm34XgGFUsdDj-LwHDXx196_yr9S6Xm3O7Z9VIeLRBQcIfHRPIJfoiPdUI3bJzDQl6QQQd_H1iHP65u_LcysjINWb4ntpXFRZIehNwCQUlpOcJ5mOValx9rsjvgqSOE_0FHziMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBxxDmcmE1kAlM77bgRzL612e7Ab5XIhpyjdGufT4Cf-UboxcFqwF3PR5-IO6bcHBb2Y_V_wKPdAZu0wi7HmLAtqxxcvZq3oBPvyqsitU2RumqvlGCPy-8D306JTC4sUDfo7iY-9ybJryVx_GT71f0lyjWWwwhdt7xYYRmaCIfU_wC40Hb0tMtvfdBvMZhkxqCDKssnwmV6ICFTJMFTAAdJEQazm6QfFemXaocaFnfpoK1xV0ZlkjNCZcO6y4-MJAT_d7kbvUAVL68NmLKMiD0ZWxMUYVg-nkYJaNX5D5I-9i7FBO9Ov2rug1ji9VSgOzmQax4bAn6CwvVrGUX1LWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=jZ8CcvikoFdyfOyNoBd3MLHpBhF8ss2Y-49axGaDzhMCtJhlCi_adgc0lVGGgPkXteWuMJepLfFAx506B5MrJS90FSGwixi9WnSjSJRVqc9YHTl_EYfLXcUP1I2wh1n4z04N2ujSANol_UXDyp8YdtoLk8Aj_Hj7re4NOmVVkrronuBJR_eXoRk3WgKL8yYYb8092l8NrKKLvhiUJJx_XH2nVDqc-KpV2LI4oZbvwcuH9oyE8AlfzgNfSj5qX-aXfYv0ceG_-m83n5PxSmqHe8bEAi114OywVNvkvF0Nf53aoZdJuuNJfj-orB4B-clswcE0DUlsrYDPrh11GAMdcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=jZ8CcvikoFdyfOyNoBd3MLHpBhF8ss2Y-49axGaDzhMCtJhlCi_adgc0lVGGgPkXteWuMJepLfFAx506B5MrJS90FSGwixi9WnSjSJRVqc9YHTl_EYfLXcUP1I2wh1n4z04N2ujSANol_UXDyp8YdtoLk8Aj_Hj7re4NOmVVkrronuBJR_eXoRk3WgKL8yYYb8092l8NrKKLvhiUJJx_XH2nVDqc-KpV2LI4oZbvwcuH9oyE8AlfzgNfSj5qX-aXfYv0ceG_-m83n5PxSmqHe8bEAi114OywVNvkvF0Nf53aoZdJuuNJfj-orB4B-clswcE0DUlsrYDPrh11GAMdcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=joR1uzloC7Lo0h7pYOySDEhNelCQfvoPTyFF3xWiXh6RQmPBq_gypfegU354kC0krhiKvesrEWeLDONV6nCdvO5mjd2d0iMdMm7ua99B_QXk_NcOTyjNU8nqXTUEtpEI3o7USKitJ9nk0wLQx0u2typdIh6JvL05ia5w6zuPrrD0bWi7SBTxrNOdUi4aJUOmHT_7DW6epmwOht4yZ-tezuAoeHTvgHCPNxarpz7ksemS0nUSqYhRvgmGilcyGxkOaWfd27qKjpLq-L4G2e39g0B0aHICZGk9IpE6-lNAtZysmyZkpNfI7VxzkfMTBWOcbF-KqT3rQOQKKj01eqYptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=joR1uzloC7Lo0h7pYOySDEhNelCQfvoPTyFF3xWiXh6RQmPBq_gypfegU354kC0krhiKvesrEWeLDONV6nCdvO5mjd2d0iMdMm7ua99B_QXk_NcOTyjNU8nqXTUEtpEI3o7USKitJ9nk0wLQx0u2typdIh6JvL05ia5w6zuPrrD0bWi7SBTxrNOdUi4aJUOmHT_7DW6epmwOht4yZ-tezuAoeHTvgHCPNxarpz7ksemS0nUSqYhRvgmGilcyGxkOaWfd27qKjpLq-L4G2e39g0B0aHICZGk9IpE6-lNAtZysmyZkpNfI7VxzkfMTBWOcbF-KqT3rQOQKKj01eqYptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=rox12fz5XNtL-k9h-VOK2VV7N6p2h2KYsnDqmIABM81VTbS5zRmP-ViDOcDtDejCA-ssh8y9zBQa2TzKaVZOROGEYUk1e6Cv1xrUPHXiq0spJjhgeNX1A5mHKVwR5vJc9gQ-YI6wsdUI07JgT-O93AmtoDQFeFz4MDzf_y5i-5UtoAmq9hwo8AwuQ5-_uj42HDnWywGNaEuIY_A9r0r3Epic7HPqj2_ObMLXyzxCFazMrRZlfxMc0LIKuSfePYd1uRHEpyrbHS48cD1gTk4J8_1jZhRUJHyBOqK-CVLFpYB5XCbAzi2HfFLGvs6gneOWT1iJwt9J7DlD0bhXmELA0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=rox12fz5XNtL-k9h-VOK2VV7N6p2h2KYsnDqmIABM81VTbS5zRmP-ViDOcDtDejCA-ssh8y9zBQa2TzKaVZOROGEYUk1e6Cv1xrUPHXiq0spJjhgeNX1A5mHKVwR5vJc9gQ-YI6wsdUI07JgT-O93AmtoDQFeFz4MDzf_y5i-5UtoAmq9hwo8AwuQ5-_uj42HDnWywGNaEuIY_A9r0r3Epic7HPqj2_ObMLXyzxCFazMrRZlfxMc0LIKuSfePYd1uRHEpyrbHS48cD1gTk4J8_1jZhRUJHyBOqK-CVLFpYB5XCbAzi2HfFLGvs6gneOWT1iJwt9J7DlD0bhXmELA0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=pyFOTlNIWfu0c-vdBsQbW2jcC0inBqGlr41gc4E0DOeEpefD0wyMuWoWqmRu0BObzvEwzOfXvD5V8J6KRSzlj_ktUUOYXNbEa93wmRxBUteX5nep9v10wl5JLi27n4UyxN_9poC89iMUgAbq-j1xueSLmtwjQv2wlo-VCzqUtv6xPjXbx3pXvsjy5WzVX9CeAHicI_WnAE-NLoGhkfd1_VOxNMontS8E5a8yITO2Tb8JNU-BLDd567CdLhmrPT79U6PArg4dqlftEFP3dTbW3QDkASyyMz9xP7A5kavkHPfmp1a9ErbAMzzgDZz2_l-GcqZnWqol1tvt5yjeUyA0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=pyFOTlNIWfu0c-vdBsQbW2jcC0inBqGlr41gc4E0DOeEpefD0wyMuWoWqmRu0BObzvEwzOfXvD5V8J6KRSzlj_ktUUOYXNbEa93wmRxBUteX5nep9v10wl5JLi27n4UyxN_9poC89iMUgAbq-j1xueSLmtwjQv2wlo-VCzqUtv6xPjXbx3pXvsjy5WzVX9CeAHicI_WnAE-NLoGhkfd1_VOxNMontS8E5a8yITO2Tb8JNU-BLDd567CdLhmrPT79U6PArg4dqlftEFP3dTbW3QDkASyyMz9xP7A5kavkHPfmp1a9ErbAMzzgDZz2_l-GcqZnWqol1tvt5yjeUyA0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=UMlx1if8hnNKjwBBbal7y7LOFfbB13JvlHCO7eMc8jajb-pqI06fAbhNraqgf0HkX-b5yaYBO63LfyG5NN0Pc7mbhSnVxFOWV8--hJpk_iUnkaRZunAILDp4VCpNR9a2ipHhkXb5NBvH6ZEWRLRSfmIWndV6ApdgnLJ1CLPuklUyoBLX7RV3sC61SElXGP_eTKZ5LN5Qz3i7LhHO0-giAjnZ6mE4eDm_tvC3oSOcvkU1SbE2DeHVtypvUHyktjLGHPVx0cnMxCe-fFv928_czrAzVyTJJ1Z1hjqsReJ5ya_EpfWyV7_0n8xKf_KlfAuI34SllWHirV_s6fpWsXc-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=UMlx1if8hnNKjwBBbal7y7LOFfbB13JvlHCO7eMc8jajb-pqI06fAbhNraqgf0HkX-b5yaYBO63LfyG5NN0Pc7mbhSnVxFOWV8--hJpk_iUnkaRZunAILDp4VCpNR9a2ipHhkXb5NBvH6ZEWRLRSfmIWndV6ApdgnLJ1CLPuklUyoBLX7RV3sC61SElXGP_eTKZ5LN5Qz3i7LhHO0-giAjnZ6mE4eDm_tvC3oSOcvkU1SbE2DeHVtypvUHyktjLGHPVx0cnMxCe-fFv928_czrAzVyTJJ1Z1hjqsReJ5ya_EpfWyV7_0n8xKf_KlfAuI34SllWHirV_s6fpWsXc-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=ko_UF_Blnh8Lua6u-1sluIf9L0vFmEJRBNWeYCqoeB2ZeJHpUMOwZj4KHTlQMRLP1ROJYMS7nz4YPqMYSaYyAV217MBVysJCYtfQmfpZSAUWrpMILyCWbVbSQNaeHr1Oe0_Qxb-plPCiZgBVKiE1ZJczLAugCfran1nGPobI8oMwd2mq1IkpGZUYhYw1OeNmaUvtSO86G7TEQaaRmjAJTw7zk8s28sieaXvJlxHcV9qQIPb2zJVtWz62hmlbu-vae9TS7bbUjlSu_HqbLym5CbmBdfbEZcUmRWbNNYbvpCDZoctOgfDYXDij83ce5yRNXqViFpOk2uQgMxPyamUsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=aY25ma_ec1fAxlAILYufLFjCQKDUfAi9ZfQORghAaChN-8kKAJZRa_-5cCGqaOYnylr8Sa7ePWSWWamej2JNgpbvdQDgvRwYGMPm2m_72ov-GwOtBvwC6vgms5bO-rbcZRzbHNnKW6S8KtJmdGKK7EqUNOKmidTL2dGGI7TuA9qgEQoi49WqGwgg7DMe6LFLi2r_lVlTuwUHrqrwS7nszoWfOYG7vMjDSRppTXhb1GF6to_T1fn1GhRIPvcgAQxSppBnDPBSpSFHNqh5CcM-Csx2yB_enhnG1jyZElZKxAfm-UsAaiIUzF6rQ3KsMkbM8BQUMZKTNs7ClrBgwn9eog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XclirMHnNPE9R583h4viXvbz7HW7Q38VvbEQbTGyYbC_BjT5jiXKfs3I6fmdKWZ6wBki7BB6T5CgISULXMk2kdzOqxCEGigC8IlFT_goZxGtVGVgvmHxnuTz2Hju-50FYu8OyZn1ZGjlTAXdSQXzp2ti0nxHspzgOMUApW5b1ParLuCdlFWOWxR1ht9MYsVwxrXsR8hgJ9SKu0tMZacPaoiAXUpLwRv9JNiF99fAL1Gsy9IsUCDGflvRJWm8w8JZjTGO_ric1M_zrTpmYLiQ0CMKSiF2WKKOrAc267yDNbtd0725NZffoDyPqqNF73SNErm8de8k0Sv0FUQ0ksFxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfaAMha3LNgAWOvRbH0l6L5ZbrhzCvsWJ8CerRop9Oo5PYkuiRk5zeSEzn52HqdZF8LJLUJ_ww-A-_1QATKtp0i-rERwK9e-BNkjCDlOBQRJ44UOOxDYiO-oprIsMn4QOZQGDrOaMslxULjhYnyPD0EUY4FzSyibDBPZsaN2V9p-gNGPH2kLxsBzKbYAegxj7ZqM5SiftQ0f-J2s9vI5lLcZRh_0UebQ05Y15sJoBrdh92ce7iofWNZUVWrrbTiaOE0qnXvVgmZ_vwbUQv0DtpYSvIfgqgXmUubmRPwbHbmv3Jr_E7aPJH8r9gcwGvWd5b39y1SqW7CbDFuwLJNuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvTZXEfATZJ1xbhDnKyP_fLSadLjStzEK4kiRrqZv5Lgco8lBlkMhpLXTaNdKLSD6KEcm02iH7nO5xZg9LxKJmJJgLR4KrnpD7aMw3nJHDMHfyO7e2ek5x_6guoHqJAKDQRcQcB5tK7z7DlpwLv64IdArOEXhJJCPHHN-DqQVmmPxhuiYcJOLGG9XNfqukRt5z0YqAg5Qzcay5jD8hZeye2jUw5W0fyixOI3IF1xXjbWWZhT3Ox6_bVzLlQ20kSkJABiBK9-479sRsqi_W_c1yJAh5nsj_mvtZu93pQeO4NhquwleobtY7j1b7esdwtgzgOThhYtj2ighl_ioUCpSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4qBHKK1Nts3NFWhk4pl9QPH8JMgXAxc0oQhcpiwXM05bEvFZvFagTRr2pwghYgdLHES8dKZi7rAHcW1xz9a8qtZMbPpnRIH9kJKRD7mhf9DnV7xlNtwnqsEDe4W_UW0Twp3DnBFvlSAhGHT4fkylRVRCKXtYiseEBmIjB1HWPl7RIOZOn2m2MRh8wn5tRXzpQaLidJOatYRhDCEylkz7T__dLOspD5hli1C9FNsUKPAfS5R8xLBMrL6eDjItpI7etlowgpjo3ksliU3EQKx-wMXzWcVOO4o6I3KODapGg64Y3At4wvGiF8rcCNloyANuvXGgKJPK_9pxCqAGilzRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=TPfK6xUxDjipVNcV1H1t7P474-dPy825epG8GTrewZyuPzrEJWnMht-_ATn9motq4Z_WEQRukPaJOU5LJrEwhaxtXW5G8CLB_-S6dIOjHZSyjvWxQs9EL41s_WueSG9E92ZB0-s9vRsdnOw6XqRh6ZtDsOFtC81P9MuczOC6i_QT8nMplgq2TE4NZOSTbZhCr-dUJQxoVP-F26gY0euP3aMgMCLg4RygesIuFzHZBQ2HhjlzHGV91vodAxkecUUrm3DMSvnymJxRa7IgKBw8dWI0LkBZVp2mRtZmEJWnvJlrojW5umuzyxLa-daKMksxe0M-gr-4BUFYaWF4ap1e2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=TPfK6xUxDjipVNcV1H1t7P474-dPy825epG8GTrewZyuPzrEJWnMht-_ATn9motq4Z_WEQRukPaJOU5LJrEwhaxtXW5G8CLB_-S6dIOjHZSyjvWxQs9EL41s_WueSG9E92ZB0-s9vRsdnOw6XqRh6ZtDsOFtC81P9MuczOC6i_QT8nMplgq2TE4NZOSTbZhCr-dUJQxoVP-F26gY0euP3aMgMCLg4RygesIuFzHZBQ2HhjlzHGV91vodAxkecUUrm3DMSvnymJxRa7IgKBw8dWI0LkBZVp2mRtZmEJWnvJlrojW5umuzyxLa-daKMksxe0M-gr-4BUFYaWF4ap1e2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/at5PBvaNG9v56ia-8h35OfSbXBfEEbTtS9-YWrByWgJYtLiHjKwvHH0xM1oyMYKupZG2jIhjC82T68f1je5CaMxhQ3kq2UXNATO7I_atXT1JAhFt1sDqKPsMCKYuKUjhs7cmgZzT9zthp2Haiz7JoOGgdyxF19AbcWCh-fnBND1zgXhqgTLbS2sTPWomdrw3TvjMUfH2thr7bg4I466lKRBNiGxnpON7d7zx6Wt6ZIt2jVwxUUW_5pE6WgwfpyIM_y-Zp1yVyztNxzKxmTYO9U37HlCHLXXpZU-5v1oWTN9p8WLRR2EdZipoDuGQinM4xS21qIFK3WJjsqf9SMryyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RuJJ2VZlpMPbnu5b-HuMZuuzZJmUZXW7Gmqi0oNOdD7qsrKeC8AZXLIGgNgHYD3ykAZQfJl4BrynFaw8_sJfkHg8zYsL5JdhBl77nIO4J27jOaCh3LXRi-ix9I4nRqevojFC4-DvSf-S7PEHy-LGkiLC5HTzGf3lwPxsWPfd22umiwW79QA7wcAwwi_frZ9xq2G9gO9shff4a_WduDb9RGdoiL3wWvND_hZKX8PbhTerzmQqiA7M1OjY0wlipXPnmYCk0ZcJdXMSlR0uGssEr8T8xyOayiRd-QG-txAhgQCfng9qhEuJslcPe8N2hPIrwY1q7McMf4wOmSuaqw6LvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=Ri_41_Ma2Ejsz9DmZW6xktC3Gjv7IY-xnKvhQLLtf3cI2JO7k37MSZBPHLVEJBV6lX5WNULZXD_bkzOYD5cCMVRpvdMXCHaYSrymaN3B6oi-cR-JxRRt2cphT6wyL_AzLnDhcVCZ-R5079Zbf-WKh_jzcIRLYIzaZwtmvqIFrxx5VBVfbU_qZpVpEKSr90zQI6wx_iFXCH4NUM1JdjM80Y9KMXiCiPpQEKHJG0V5GclQtfkPHb0GXIwGfPG2Bht3e72ft5y-REYNDLCXUFFHy0J4vvdlND4DxGdbAdUVXNvwYW-kIyKd3_Zg14wkiNnTuFBD6Y6VVJtg7pOsZMa-BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=Ri_41_Ma2Ejsz9DmZW6xktC3Gjv7IY-xnKvhQLLtf3cI2JO7k37MSZBPHLVEJBV6lX5WNULZXD_bkzOYD5cCMVRpvdMXCHaYSrymaN3B6oi-cR-JxRRt2cphT6wyL_AzLnDhcVCZ-R5079Zbf-WKh_jzcIRLYIzaZwtmvqIFrxx5VBVfbU_qZpVpEKSr90zQI6wx_iFXCH4NUM1JdjM80Y9KMXiCiPpQEKHJG0V5GclQtfkPHb0GXIwGfPG2Bht3e72ft5y-REYNDLCXUFFHy0J4vvdlND4DxGdbAdUVXNvwYW-kIyKd3_Zg14wkiNnTuFBD6Y6VVJtg7pOsZMa-BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=oWOq-3ZJRz7N8jduIkdAWxixMw3I-ji-MeC0uBLk2RVQEyU-odnkf9-uDn4vqhgysRgqWuMpMI7lj_wo8WEx11D5R873Mkysg67sOXGw7zebmniRIPk0fbFwuFMmLKoOK-fnsciKJC1ro9MlI4e4hH-RAvubPJavmU-QB2CzRaVkwg1O6YawWh69hbV81g0oLJF87aDRod3QnIY8-eNkvnTA3gOT3GNyUtgU9om_DuPCl4gGDu5-7p9ri5lYxXDv9Wek0Qcl1uBee2SnCkD2W2xjsOvsUwNpkbay9vTNM1h6L1CSN62-iTcXdOFONhLodKTLEaShq6dR4ovXd14UEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=oWOq-3ZJRz7N8jduIkdAWxixMw3I-ji-MeC0uBLk2RVQEyU-odnkf9-uDn4vqhgysRgqWuMpMI7lj_wo8WEx11D5R873Mkysg67sOXGw7zebmniRIPk0fbFwuFMmLKoOK-fnsciKJC1ro9MlI4e4hH-RAvubPJavmU-QB2CzRaVkwg1O6YawWh69hbV81g0oLJF87aDRod3QnIY8-eNkvnTA3gOT3GNyUtgU9om_DuPCl4gGDu5-7p9ri5lYxXDv9Wek0Qcl1uBee2SnCkD2W2xjsOvsUwNpkbay9vTNM1h6L1CSN62-iTcXdOFONhLodKTLEaShq6dR4ovXd14UEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=oYJHgl3m-2LX83zG8A3bDk7Qp95MbYNQWllwxaI8x3aQ3mNbiemham03zpjPr8TAmRG0fvhxRAZe_9bdPm9R9_GJGDZRx7Aft0niUmWzZqLyfbxGgCCZcAjpVCPjnYYvmlcDLvTCrzT55Yxdh2tdZStehqJ03gzgk9MqBs7C_mxMFAggOBmBymc49nReeZ3mbb8gXYjH3FUYny3wkQwolhwo6zjGrtGkB7dOQk_6qdgAIaDpo3HlyWO_NbHxZd_y0X6kUFD-BhfquqRljrx1o80UJaapa_nzIyQasisBgFBSMK3RNZZrCdTkMeAOohJTYGHU2omXF_oto5W3J9LnAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=oYJHgl3m-2LX83zG8A3bDk7Qp95MbYNQWllwxaI8x3aQ3mNbiemham03zpjPr8TAmRG0fvhxRAZe_9bdPm9R9_GJGDZRx7Aft0niUmWzZqLyfbxGgCCZcAjpVCPjnYYvmlcDLvTCrzT55Yxdh2tdZStehqJ03gzgk9MqBs7C_mxMFAggOBmBymc49nReeZ3mbb8gXYjH3FUYny3wkQwolhwo6zjGrtGkB7dOQk_6qdgAIaDpo3HlyWO_NbHxZd_y0X6kUFD-BhfquqRljrx1o80UJaapa_nzIyQasisBgFBSMK3RNZZrCdTkMeAOohJTYGHU2omXF_oto5W3J9LnAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=ZCiSmW4Wx9D56TsbURgI5221vAqntUmUvJb3saYEd1KvAheC_jTwm7WJ_Gc-ufNf9gl8NUPqTWLLpun2P13ild87xKqhmJzu37PyZJsSgNxQXCZuxQXgdVFRWM0LY72G84wzDKsVbHFF5IA7epwfY48L5UJ9BLOY8urfpRNq1jh4EjZCOie8RAbRQWINd6M8Q8L3iDRyABUSuZ-7ufriCbDVKViWezhSIKhir98RhoKoVt5wxjmX-kdLnlKs2DRWmOkFQy3MR_Tz2B8Yw51WCCWEFNMvtHscGwje57ulVJSEGuoJv1JQUPs3uil3IfVkxG8DzZa5K8RKRo9G2cV0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=ZCiSmW4Wx9D56TsbURgI5221vAqntUmUvJb3saYEd1KvAheC_jTwm7WJ_Gc-ufNf9gl8NUPqTWLLpun2P13ild87xKqhmJzu37PyZJsSgNxQXCZuxQXgdVFRWM0LY72G84wzDKsVbHFF5IA7epwfY48L5UJ9BLOY8urfpRNq1jh4EjZCOie8RAbRQWINd6M8Q8L3iDRyABUSuZ-7ufriCbDVKViWezhSIKhir98RhoKoVt5wxjmX-kdLnlKs2DRWmOkFQy3MR_Tz2B8Yw51WCCWEFNMvtHscGwje57ulVJSEGuoJv1JQUPs3uil3IfVkxG8DzZa5K8RKRo9G2cV0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=B_ljLKahIUit34n0_VlOyVYSELTvjfwpfsQK1_VlwF4sfZDTAGda6P7pfSteIp8bY1FZi3gd0Zc8Pu-zP8uDodyuYmyYXLmTExJyOQ7pLIL7sPt-FfPssIWvKANgwUbgaCNBXQgIbajcvU1W8f-s0MWZUQnDHlKSMcLZQyuXWAAr9RMIK_zXxuA23nKn13_L7CvsaM-EoS80oWH584SqSXCIdyxKJH-LEUbH4bKHDYY1HftLgz-vsn6JLtOuaoTsk6CW08pMPaAsLaBoML2gyprdl7T8lPo9k58XqgNVxGXSZytnKhCQc6KL3n116KlxhWFl-htzr-0AjeFG5GxB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=B_ljLKahIUit34n0_VlOyVYSELTvjfwpfsQK1_VlwF4sfZDTAGda6P7pfSteIp8bY1FZi3gd0Zc8Pu-zP8uDodyuYmyYXLmTExJyOQ7pLIL7sPt-FfPssIWvKANgwUbgaCNBXQgIbajcvU1W8f-s0MWZUQnDHlKSMcLZQyuXWAAr9RMIK_zXxuA23nKn13_L7CvsaM-EoS80oWH584SqSXCIdyxKJH-LEUbH4bKHDYY1HftLgz-vsn6JLtOuaoTsk6CW08pMPaAsLaBoML2gyprdl7T8lPo9k58XqgNVxGXSZytnKhCQc6KL3n116KlxhWFl-htzr-0AjeFG5GxB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=p4vQtH23Y7L4-rQLWqIfIKaHVd9oQSIbuRTOYgMGstO-g6prFAnwy4xYc2o9_0A3pHZtiIwsg_-_hoI5IAUROYSbngaP6C8kGPI2RSfZCn6oWb3tFgXzKWZmcbXgYb1kwBwEb-qLt7QVKRlcQ6WNmlO402r6NWgfLTwVIaTA4AstxYQafkGUtcP6e3SiJbBhe3CK676Yg2S95kW0NbrG4qQvEmyQCtIlbvklRbrp2wuHbOI_um4qonN7Z0RGP7KYdrvl6dqJdrnqAOCgPKC3TwKEvmPuBmMuZyFlznjkwbJhKTJGLpLfxiVT9DA3UPu2CFDot3bKCk3p8ReY6lrXUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=p4vQtH23Y7L4-rQLWqIfIKaHVd9oQSIbuRTOYgMGstO-g6prFAnwy4xYc2o9_0A3pHZtiIwsg_-_hoI5IAUROYSbngaP6C8kGPI2RSfZCn6oWb3tFgXzKWZmcbXgYb1kwBwEb-qLt7QVKRlcQ6WNmlO402r6NWgfLTwVIaTA4AstxYQafkGUtcP6e3SiJbBhe3CK676Yg2S95kW0NbrG4qQvEmyQCtIlbvklRbrp2wuHbOI_um4qonN7Z0RGP7KYdrvl6dqJdrnqAOCgPKC3TwKEvmPuBmMuZyFlznjkwbJhKTJGLpLfxiVT9DA3UPu2CFDot3bKCk3p8ReY6lrXUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7aRj6EsqBwRZ2yWpvO4kNOr6XeOTVnQb-9h0r_CkSo0Bopenb-vEByfWUAEmV5nPNXE5yO4q-XzUVSMq05IgI75DkTr7n-Y5F0P8khnKElmDFUixvnrNTv9VK5_T3H2xCYFn0UCyJTnR1bD0hW_EeYa3oAS0r2fPW3WXxOeOJmkJoYYBH5vSUOzaDdOriHuvTrbSNSFyihV8lccmD49U6BaD1Sg663Vto0QKktJ1sn9F1S9rwERdPo6b2dIKDIQjxN2RhE_dNluV2zYBiAnWTuAba2EaesNn3Y0CY0D8EjW3id--bQ-GFGuARxmRRCDpTSGPk9zk6lEQRWG0CT7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=iTkApy8FIib1eKBOgnvx-0WM7p_E5tm9fx-LVmqUGqCvnethakH_BtOQRtTPEbNNfG1h4uttY-e54PlFUSc2DD9CKqySb7uzEeLF51C15gFPm-mrQ6TvznBBTiNyOGqoWsYvY1uMYrPInWDDvx2pUO2Ez-bmvBnhCVpcPsG_YUETuAr2yFz-2I6zWSjzbTDfk_-4sSAxdkCzN-EQn6spk0cq4NWQJh-Amg7MGoJLU8OusEUe_um3LiuBNOdI_okVrypcgog2shg6I7pPKt8bkQKSDyMhonaqgtI02MYkrSU2VSDTvrPf1HdIbObFT7x8BT_UPSAXHGEgeAOCO_MAzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=iTkApy8FIib1eKBOgnvx-0WM7p_E5tm9fx-LVmqUGqCvnethakH_BtOQRtTPEbNNfG1h4uttY-e54PlFUSc2DD9CKqySb7uzEeLF51C15gFPm-mrQ6TvznBBTiNyOGqoWsYvY1uMYrPInWDDvx2pUO2Ez-bmvBnhCVpcPsG_YUETuAr2yFz-2I6zWSjzbTDfk_-4sSAxdkCzN-EQn6spk0cq4NWQJh-Amg7MGoJLU8OusEUe_um3LiuBNOdI_okVrypcgog2shg6I7pPKt8bkQKSDyMhonaqgtI02MYkrSU2VSDTvrPf1HdIbObFT7x8BT_UPSAXHGEgeAOCO_MAzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2ipt0hToHEohQpnZKqZAKkLJz3Hc9hL11XiovI3w82lV8LOe0rhpr17WuWTqCqdUU-6nQmDTOekkK3OVADWsjfhoOhH41Xvq6KJ9ry95mwPMGEDp1gRZBGqlS-jRpTTQrk8NL5yDMg2pQMUVMQRIyWr6WQlw5JYasduJw_wQ_4N-G68_1qomvBJxkC5KWaNnyn--4QhXOoqJyM18VBtJhIt43EpLlw3hnwgZCxCdH3qzmEhfJy6oQq1XBeF-8SK-YI2apAP65eS-Px-nooTxJDbfH2jMTdXbf2VNuabz7a10kSCuY8unu_N7HiNBv8TWXh_gSXtS_YMO0T__3F-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=hM8Y78g4YBGHcdAekbv1otyG1BO21R-gnsaLCieRsdQvYYm_UpOQCjs1rwHXUdk_nASacyV2ILxig8ZQBAL3eazJfgm2tzfM6QmTOMf5KYr6PI-QIJ2j-F_6SgLbR4C44_l1f-QN5e_gS5G75wGUy7Ib1QFpW2Oyq15t5toAZmW9THrdTekpnyi7lKQCJp-Wdtq3FgRpB4IlN_o-NQSTe6KG4nJdvgatCMueyj5tvXWun3B7ToRCvZMlS57hBmHXMKaHzNKztST3c_TcG1MOqFv80I9g2qlZCNHaSAnQGWNomBUfrjblaiVDeR3ptT4uXviicOJulRs-Ucbh-QWiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=hM8Y78g4YBGHcdAekbv1otyG1BO21R-gnsaLCieRsdQvYYm_UpOQCjs1rwHXUdk_nASacyV2ILxig8ZQBAL3eazJfgm2tzfM6QmTOMf5KYr6PI-QIJ2j-F_6SgLbR4C44_l1f-QN5e_gS5G75wGUy7Ib1QFpW2Oyq15t5toAZmW9THrdTekpnyi7lKQCJp-Wdtq3FgRpB4IlN_o-NQSTe6KG4nJdvgatCMueyj5tvXWun3B7ToRCvZMlS57hBmHXMKaHzNKztST3c_TcG1MOqFv80I9g2qlZCNHaSAnQGWNomBUfrjblaiVDeR3ptT4uXviicOJulRs-Ucbh-QWiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=W_YeFUcHT1EMmfwFEjaVNGBb4IOb0IeoJ67mqMiXOth80Lj1aZ_RIYieXwtNZadXkj_jtdImpB16WUEDGHHertPPCdMbKYTxiNSPwz8ij-sSxOgWbrfXE_ktH7gUars96RgiHuw67u0UGC40q-riiNRM4mVMurBAFuB_t-ywpDMq3U8YfD5gXKXixBfa81MwdmMDnpY-wsPIstSgBHYwfLif2dwn8azqEeBZSGdmd4XZOP-jYA_UMifz-r7RQYCfyHqYLs1XvLm0L7quOFx8lw_sOYNd45YDK-GD5gcYMMGTpkx9vw8uTb-vcKDxteqiHaFTwf6lkObFNN__GwgKvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=W_YeFUcHT1EMmfwFEjaVNGBb4IOb0IeoJ67mqMiXOth80Lj1aZ_RIYieXwtNZadXkj_jtdImpB16WUEDGHHertPPCdMbKYTxiNSPwz8ij-sSxOgWbrfXE_ktH7gUars96RgiHuw67u0UGC40q-riiNRM4mVMurBAFuB_t-ywpDMq3U8YfD5gXKXixBfa81MwdmMDnpY-wsPIstSgBHYwfLif2dwn8azqEeBZSGdmd4XZOP-jYA_UMifz-r7RQYCfyHqYLs1XvLm0L7quOFx8lw_sOYNd45YDK-GD5gcYMMGTpkx9vw8uTb-vcKDxteqiHaFTwf6lkObFNN__GwgKvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=NV0kmnwRYEsUYsbbTF3i7iwPsxHbZEC-ewUmpS8AMSxR24poNPaR44rVEbWYxiBpOzYz0VSqtLmBINhVB7ax58cGBNr0KWKRFTwhFYySglrT8ebQ5ocGskAvjZlge76-TQ8U5sAEcqWC3LgFHltWcWXouSkgWthwJ3O2k_GUCWhEXQzml5uMK1W4eZeoLiZgfXqougHrRjqCYXHuBRtAHcjiVranZTn9WQowQ8v9t070_3CO3SlZhKhD7JRfss4daPXkT5Kjkw2d4s9x-Y6rwG2wbTBMe5SZ6BGG_ZgFem5SzKdgQF2_EpZRiyOlf2aNY6_Ffmh_vcuCmEAzNcJE6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=NV0kmnwRYEsUYsbbTF3i7iwPsxHbZEC-ewUmpS8AMSxR24poNPaR44rVEbWYxiBpOzYz0VSqtLmBINhVB7ax58cGBNr0KWKRFTwhFYySglrT8ebQ5ocGskAvjZlge76-TQ8U5sAEcqWC3LgFHltWcWXouSkgWthwJ3O2k_GUCWhEXQzml5uMK1W4eZeoLiZgfXqougHrRjqCYXHuBRtAHcjiVranZTn9WQowQ8v9t070_3CO3SlZhKhD7JRfss4daPXkT5Kjkw2d4s9x-Y6rwG2wbTBMe5SZ6BGG_ZgFem5SzKdgQF2_EpZRiyOlf2aNY6_Ffmh_vcuCmEAzNcJE6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=aIscapCOh9jGdKB6gr9A1szqrDQHLaJW-xm2jXZ4FVh8TC65SlRUB0leVOWsjqqkeH22JtOJfb0Rw-3I5EQA9UFocYAUDMbx_1OndWC8k2-56jw7TKDopp2EmT5SUJyHmqSdpz-W23T-4ffFRmLzPVfjKRwFVycmJ6QUkzH0JUKfLQQ0jrdQ11BjurEOxV2Uv_Df77wTRaeHhuA_e2oKmk24mtPQFAPGDBwlSERFjvrv5X6Xi_R_xMY-nYZHqwdNp7R50yAZ0swqCqb-k0iQi8ltAr3dgsHVco3Wkau3ZDWD5NS7ucwaTlkkSfIWhLHhktlngM52JFeHPqWVtP19LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=aIscapCOh9jGdKB6gr9A1szqrDQHLaJW-xm2jXZ4FVh8TC65SlRUB0leVOWsjqqkeH22JtOJfb0Rw-3I5EQA9UFocYAUDMbx_1OndWC8k2-56jw7TKDopp2EmT5SUJyHmqSdpz-W23T-4ffFRmLzPVfjKRwFVycmJ6QUkzH0JUKfLQQ0jrdQ11BjurEOxV2Uv_Df77wTRaeHhuA_e2oKmk24mtPQFAPGDBwlSERFjvrv5X6Xi_R_xMY-nYZHqwdNp7R50yAZ0swqCqb-k0iQi8ltAr3dgsHVco3Wkau3ZDWD5NS7ucwaTlkkSfIWhLHhktlngM52JFeHPqWVtP19LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrqSzIW_JJhz_vmUxUgbebgZ515r9l8EnCntCT865wiC7Do0fRYDYWOBDP1Eg2CNf_DWoOlvhxlho3OexDAvhgH1ViFGEMcZ4XRkack7ZiTq0mwIGA7VpgmxEQb-0ucWRwEEItEYX152h5QT8BzpBTg6mKUHoCT-Ii2I--F_QFpySAS49iL9OQX8iZUeilVC6hdNfEMs_4RqsSoWnCTg9AMiRjrWPPyHWu2zpu9bD7XoPtpc0S9LBQFqREkXN4xBZEfsu8GZn1iXLjgeQhhhX8NWPqLXjRipQjF8LaISRjyzrC6pzpC31vO5vCaBUhY9a5nf8AdPHKURyzKTzeBTHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=Bpf40GK9JmkvSFz6fDedaMRJw64tX2jtJkrUtvyFAaeIxiw8P1zRP6-6sK1az0etraRREphb4nbcHidANvcchfpgu2cemLMoL1IRv5okdWnZMKkkIJ1o3mCY8BH5HERYOrvxidsrLa8AAIqzSH-FJG90Qq2H8CjyVMvb8IC9KS5u9pxzCQkXOTXkXOkE1JlXMLugFqCuYtpuRkHFCVv8DQ3CSphX6q7XRWXvXaMs-909pFwbAwOIyRf1CCz5Qlw9oU4ru_gT6N-PsKtiqfzL0oe70QgsaDThZxJGeYuVI2jNnZpyMlvkfnQehdWd6GjJCWd2WM6HNJu2NXd-6d3ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=Bpf40GK9JmkvSFz6fDedaMRJw64tX2jtJkrUtvyFAaeIxiw8P1zRP6-6sK1az0etraRREphb4nbcHidANvcchfpgu2cemLMoL1IRv5okdWnZMKkkIJ1o3mCY8BH5HERYOrvxidsrLa8AAIqzSH-FJG90Qq2H8CjyVMvb8IC9KS5u9pxzCQkXOTXkXOkE1JlXMLugFqCuYtpuRkHFCVv8DQ3CSphX6q7XRWXvXaMs-909pFwbAwOIyRf1CCz5Qlw9oU4ru_gT6N-PsKtiqfzL0oe70QgsaDThZxJGeYuVI2jNnZpyMlvkfnQehdWd6GjJCWd2WM6HNJu2NXd-6d3ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=EQwiXlM2J5XDXdWdszM3K9R37aJCKxKoCI_T6nM75t0GmVZgNLiAmrX5WBZg3t_EeJ-wu81rypXb0UK7Fq9cq4NaQYaDh3Mb7HgNSrz8sNHQbW40nPreHyyu9K48iCpzbeG4LymbJ4AXDjDZmaV0em1BU4BtRwoWUhH06r0gOSbcdEQ69lBZ_m1eyqXhnVdfx6YY20cgCSeqWzFB6MUL6_UEdRl3OIIvLDR1Y57VbTLep76E2HXaEL8rQduYK-gHhwBNN10qhkuOlEqyZCCFjlDNidli3liWHOInfOHxfILKhgdo1Lk588tiMjlE94lmRidRzJBsCelNF8Wy6zULCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=EQwiXlM2J5XDXdWdszM3K9R37aJCKxKoCI_T6nM75t0GmVZgNLiAmrX5WBZg3t_EeJ-wu81rypXb0UK7Fq9cq4NaQYaDh3Mb7HgNSrz8sNHQbW40nPreHyyu9K48iCpzbeG4LymbJ4AXDjDZmaV0em1BU4BtRwoWUhH06r0gOSbcdEQ69lBZ_m1eyqXhnVdfx6YY20cgCSeqWzFB6MUL6_UEdRl3OIIvLDR1Y57VbTLep76E2HXaEL8rQduYK-gHhwBNN10qhkuOlEqyZCCFjlDNidli3liWHOInfOHxfILKhgdo1Lk588tiMjlE94lmRidRzJBsCelNF8Wy6zULCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=kuVeht4b3MIHdAxVWB9y6Klb3GH6e8DUhmV-q_qIkVOUlOMe7VdbTI0uAGRO87kQbHyvby2xl_1J5ogHCSmpAgbiT65AgEl9WupKNllpdT3uIEoM5stGrAPqsvqh7SO7bTsnrmIp2qXr9f5o3BMywSW5XvxL6RNU5Ov7wfH37SJ1lcLh4Wa6sMHaxs6ISWDNaNWBpxm6804b5BRPg9frmYn17lGYYlzYmH5_lYCHjekL7EDPQKAvRbyY4wek0oFpghM_rHkdE-z4JeVpITxCqIdHGITpieZtek-ApMp4ATotQZznxeud1Nd25fXaQsb8qkakP_OsQkZs26nbYGs75g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=kuVeht4b3MIHdAxVWB9y6Klb3GH6e8DUhmV-q_qIkVOUlOMe7VdbTI0uAGRO87kQbHyvby2xl_1J5ogHCSmpAgbiT65AgEl9WupKNllpdT3uIEoM5stGrAPqsvqh7SO7bTsnrmIp2qXr9f5o3BMywSW5XvxL6RNU5Ov7wfH37SJ1lcLh4Wa6sMHaxs6ISWDNaNWBpxm6804b5BRPg9frmYn17lGYYlzYmH5_lYCHjekL7EDPQKAvRbyY4wek0oFpghM_rHkdE-z4JeVpITxCqIdHGITpieZtek-ApMp4ATotQZznxeud1Nd25fXaQsb8qkakP_OsQkZs26nbYGs75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=Ml2qxVmCH7HRx7AHmOY8NgIR6wLBd94ysDzBH0QsJYChUnWxPYIr4UnlQM8z9RWyxqraAC08brJEj2Qb_nzVrSIiazaF7mW5oM3RdchwqnuV5bBNm1_-WtW7gfomGdsi-8icJTtdQE9r-t0OwCn_njmc_n8ZTPQYVLJ2NGhzWit2JbN0ytNA6ojsSgnuS_ZtaaMJ4fIyyADfYiwcEKDKETyFhdGWc2gnKpGraqdvM6bFAL7tlrpYXjK0PXNwrakN7hx9HdaSrmTyOnEL9U_xbCvn-locgMl1_9PWF76aOEBgYtZA_fL6UIXgbOTzCQQ8FaQXv0G4rM1OEKjiBz-BNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=Ml2qxVmCH7HRx7AHmOY8NgIR6wLBd94ysDzBH0QsJYChUnWxPYIr4UnlQM8z9RWyxqraAC08brJEj2Qb_nzVrSIiazaF7mW5oM3RdchwqnuV5bBNm1_-WtW7gfomGdsi-8icJTtdQE9r-t0OwCn_njmc_n8ZTPQYVLJ2NGhzWit2JbN0ytNA6ojsSgnuS_ZtaaMJ4fIyyADfYiwcEKDKETyFhdGWc2gnKpGraqdvM6bFAL7tlrpYXjK0PXNwrakN7hx9HdaSrmTyOnEL9U_xbCvn-locgMl1_9PWF76aOEBgYtZA_fL6UIXgbOTzCQQ8FaQXv0G4rM1OEKjiBz-BNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=FyLGVQHgpIidrvXS6lWT0Nr8ixiG4-mSx1H2go8-e_vSFTYVxQz9zdNJXeOrWUG7FnOPyQir5tE8_ROldrUY_yG2cNf0OuN3vqx3fbGKmOaROvEeTH_jxx4GCVrUNkcxRxy50LMCbnPrHsk3pomoKzz2YVN-RGhwPh9lcGx60-zzD3C4lgpaB6Vf1CZhR4hJyQm85QDpbsAu7Cgz6kEgoH7JEGTW_xbGMnAp7I7WL2J26CT-fQYqzCwmX8T7C9aXB1bTVTmv4F6Zjw9PHV-ZknJPrU4K65K2GEcjmi1bYuydut3EyzicPrseKRS2k5x9WcYlpxAbWQuf13NJuYpurKPperZjrITgMjG_W2BR5b0m8xz0CKHfNAv01x8-eQe669nkalTZoQdIUEtoP8ODC-b5WbNAAnN9UwTCMfO2yDC896J3CIGPvW7Z7CCECRYXpIoTedypIPMtyoUdREZ4uBhGL69uAtjt1P_iHCMFpfbKLXoXicvFFatzGG7Bpw-a8yFLRnpIXitup6VwqubKX8-9SZ-o_J6__HiwkImRtADsrpiyYKt6qGtYA1P2yz0o65FEZS6i4fP-CxrLp4G4aBgPyRCLR0tgddAC1hQkkI-NpmANblnw-5tKHpTnWHV5_OyD3xm-IzkjxVSG359Ix8CKskpm3xgogwOF8xNJdQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=FyLGVQHgpIidrvXS6lWT0Nr8ixiG4-mSx1H2go8-e_vSFTYVxQz9zdNJXeOrWUG7FnOPyQir5tE8_ROldrUY_yG2cNf0OuN3vqx3fbGKmOaROvEeTH_jxx4GCVrUNkcxRxy50LMCbnPrHsk3pomoKzz2YVN-RGhwPh9lcGx60-zzD3C4lgpaB6Vf1CZhR4hJyQm85QDpbsAu7Cgz6kEgoH7JEGTW_xbGMnAp7I7WL2J26CT-fQYqzCwmX8T7C9aXB1bTVTmv4F6Zjw9PHV-ZknJPrU4K65K2GEcjmi1bYuydut3EyzicPrseKRS2k5x9WcYlpxAbWQuf13NJuYpurKPperZjrITgMjG_W2BR5b0m8xz0CKHfNAv01x8-eQe669nkalTZoQdIUEtoP8ODC-b5WbNAAnN9UwTCMfO2yDC896J3CIGPvW7Z7CCECRYXpIoTedypIPMtyoUdREZ4uBhGL69uAtjt1P_iHCMFpfbKLXoXicvFFatzGG7Bpw-a8yFLRnpIXitup6VwqubKX8-9SZ-o_J6__HiwkImRtADsrpiyYKt6qGtYA1P2yz0o65FEZS6i4fP-CxrLp4G4aBgPyRCLR0tgddAC1hQkkI-NpmANblnw-5tKHpTnWHV5_OyD3xm-IzkjxVSG359Ix8CKskpm3xgogwOF8xNJdQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=pgjTxK2BMm0hBMSce1_J-4ftwQQMpEW37r27iRf3zaDQt_ZRSySsNwjcMkrrZUDuMMVwdFw_3EpeDsjWdOhqqHwcfFcCW8UFj9x6hgqVGeqFRKG7uE2Dv3oolZmPSgoiVckIM1TFS1o6_DnJmNxi1Hm8sq2mdqp2uEnjjYm06EPidSgD-wPRa6BfkkFX7oIbWCKGO7dpJkuoYhbyn6kibtTNCwdtqFwfsMqCu3lujqiSIfWgZRO1oaV1vuFKdwxQx-3uvX7kpTnAq2fwUcqCuPamN0MJRllDCgtkwYcNELKqx4GsNL1tzFxXhp9tN33nFbNY7uFJcXe0CP6epPlxkRdbGqfJ9b5oJG9s0gCP0tcWRdp7ml98CZ966_TGYVO7U_Is5u6b7uJjQPRYLHcrJ7r7TwlmG_1mxpKIfsDaWXKyR6FXvLI6QdYnUMCpXhLK0Ap5L7jLT2Nhd-ydhTePdrxKVuvn79zFYIAicNpmEEbXVHKyZzjoWu4gywLnGpQ3py_Wv36l6deRSzdec6lf4f7MVkyKQJL53Ssvjm0OqBc7HEwKnjOwrQXPNoccI-fL5j__E-orpWj8OYS6lfklvxvTLQ2IltgS9kHn7J7mM0oS3hs5IKe85qN2dIpuQf_MWTa1mF1Zdv6ymostbTL2JefkESV4nhvqXrPFZOC6nxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=pgjTxK2BMm0hBMSce1_J-4ftwQQMpEW37r27iRf3zaDQt_ZRSySsNwjcMkrrZUDuMMVwdFw_3EpeDsjWdOhqqHwcfFcCW8UFj9x6hgqVGeqFRKG7uE2Dv3oolZmPSgoiVckIM1TFS1o6_DnJmNxi1Hm8sq2mdqp2uEnjjYm06EPidSgD-wPRa6BfkkFX7oIbWCKGO7dpJkuoYhbyn6kibtTNCwdtqFwfsMqCu3lujqiSIfWgZRO1oaV1vuFKdwxQx-3uvX7kpTnAq2fwUcqCuPamN0MJRllDCgtkwYcNELKqx4GsNL1tzFxXhp9tN33nFbNY7uFJcXe0CP6epPlxkRdbGqfJ9b5oJG9s0gCP0tcWRdp7ml98CZ966_TGYVO7U_Is5u6b7uJjQPRYLHcrJ7r7TwlmG_1mxpKIfsDaWXKyR6FXvLI6QdYnUMCpXhLK0Ap5L7jLT2Nhd-ydhTePdrxKVuvn79zFYIAicNpmEEbXVHKyZzjoWu4gywLnGpQ3py_Wv36l6deRSzdec6lf4f7MVkyKQJL53Ssvjm0OqBc7HEwKnjOwrQXPNoccI-fL5j__E-orpWj8OYS6lfklvxvTLQ2IltgS9kHn7J7mM0oS3hs5IKe85qN2dIpuQf_MWTa1mF1Zdv6ymostbTL2JefkESV4nhvqXrPFZOC6nxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRa0ta3MSKnDe87-brq8oUOv7NPXHGzvvjUvpZOyxi2lU9wc3N03KQkFizPexPt7NtLlGxRJv9dWjnuz0QAiKPuMy2hsSsdw2Uu3t6y5CqZj-Lo4FZSyDdLk7euZYtJinKLWs-2LNjRslW3A4CD4NlbCilcJYfMsk801p7ac0XerGlgVv-4G0hQvkG0k41d6qU_Z-WtSE_TLYl9uv1d4LqHRBHoRnsb_Ck6jga9JQyWYahoqiNLXrGPXHjii53OJGCrVjO6iDFFT8sOD-sSuLSDLEF186qdT1hKtR-Ho4ZHMUmGtAb2GAJVT5qJRlc3oQl2fJWwtHCosBbzXIHKmkB-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRa0ta3MSKnDe87-brq8oUOv7NPXHGzvvjUvpZOyxi2lU9wc3N03KQkFizPexPt7NtLlGxRJv9dWjnuz0QAiKPuMy2hsSsdw2Uu3t6y5CqZj-Lo4FZSyDdLk7euZYtJinKLWs-2LNjRslW3A4CD4NlbCilcJYfMsk801p7ac0XerGlgVv-4G0hQvkG0k41d6qU_Z-WtSE_TLYl9uv1d4LqHRBHoRnsb_Ck6jga9JQyWYahoqiNLXrGPXHjii53OJGCrVjO6iDFFT8sOD-sSuLSDLEF186qdT1hKtR-Ho4ZHMUmGtAb2GAJVT5qJRlc3oQl2fJWwtHCosBbzXIHKmkB-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDTLIvU5A1NEGxFyDIzKhlUjpIj3m2HB07wnkCiK2KDGuExGh87XrnTeRaByCWU6O_nyUO0k9p4srmg7fEuyVUYyoI9ae7SQSfkS9-TynH6XDHqTn8XEB85XM-tjQQ5J8P8bIOlMwP5fNHGNktn3jk5K0kWRAeqYIeFzCORucLy0VSjfajR3mHdTbJzU4XCKeqjfxyP5bZa1-rl1GobGnBWMGD7pTAWr-0Mgiz8G-O7wOiwUcwqZPyvZvf0l8VSNH_YKFT3ai1-O76ouT6YUKA_8sOHIwftBZx8p7UrgBfgC4SwW8cjDEdZH51BKzxuKkuQUW2d1tDGm_EBmzbbS3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ4Xa0g2qfcNutlET5sujuVX4NPY9tWPVa4YyO9FfIHfefsxbLoth5gi9jxbDSkaLoWbTeKwbwRI9P3m4rYOwHp4pD1ofjCB_o2x0164PomAhSFm7dP8vh1nDnPU1IhTOaPzxjSOl23mYs7kCd60PdK2M1ktB4wuk-JR9R_rK1LChjtemAEB3wneiD3y5dDJdmxFRv6eA-Nb41UtZu0PgpJRETo-xWI-kB_nSi4tXiH7rcNizoLNS8yvsaY6wPZBqbasshMSaK5u8qdJk4323i-2W1gG6CPbddkrw_DjFg6SXOinn2IZlFHPQk2naqxk95i7vsWXSkhHPu65xsCv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=GhPyMvW9eWM3alBlhzz9f3kcivuoUzs9Os72D56mmABPeYwrtvVGjYBuCwkDzQxBOVTRUoTVlPtQ3zBv71qv1ny0m7tVAUkLCzW1_q7PaAEHvib-aU8EvsvpuDrd_Y5QBrOCMBvRKGJJDstmIraK-PzYSZ_E0nrCxSiFDX_pbmsjaziwqw0ExyjZr2NcR0z46j7BUnJDiW9GjgEeVUKHPnk65POBZr670nUiTXBf2Z0y7l1zhShkiuxHDOQLq7GQwmPvnnr0nKDzFzaJyZhoMqmOVTEI5cvuFB_g-Vv5YKASgx6Jyonm-t-MjpIIzcWlvSNPvSuTgVUDPm99cA2GrRtdO6Vk3B1v3ISBixuJm8t6Q9lA5HHuGS6rPuL3zDlbGN4bdibftLHsv8v89Hxxp36Xje43avPweRmcfdGxhilOSI8RPewyLRlbpPc2KBy0-qpY-dEU8gTM96f1hm8GEBZyUhnePewQwTCNEVLCPJp_ET_ZfjNJ7I9FDFTvGi1ydiwvilmBjOaUjlkklKpItN4d1wZsXcdXDpj66a2Lq0MKrFQmJ4FpXl0gCWReuagMigopUjb8wDzTcehTn8QqQSOV8071bEt6LfROi7jansbFFOKrHaYmdCwFlShDOvI8nKYBobtr7XS0rHTQaaez1YBg_YVjHpSowkvlp29c7Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=GhPyMvW9eWM3alBlhzz9f3kcivuoUzs9Os72D56mmABPeYwrtvVGjYBuCwkDzQxBOVTRUoTVlPtQ3zBv71qv1ny0m7tVAUkLCzW1_q7PaAEHvib-aU8EvsvpuDrd_Y5QBrOCMBvRKGJJDstmIraK-PzYSZ_E0nrCxSiFDX_pbmsjaziwqw0ExyjZr2NcR0z46j7BUnJDiW9GjgEeVUKHPnk65POBZr670nUiTXBf2Z0y7l1zhShkiuxHDOQLq7GQwmPvnnr0nKDzFzaJyZhoMqmOVTEI5cvuFB_g-Vv5YKASgx6Jyonm-t-MjpIIzcWlvSNPvSuTgVUDPm99cA2GrRtdO6Vk3B1v3ISBixuJm8t6Q9lA5HHuGS6rPuL3zDlbGN4bdibftLHsv8v89Hxxp36Xje43avPweRmcfdGxhilOSI8RPewyLRlbpPc2KBy0-qpY-dEU8gTM96f1hm8GEBZyUhnePewQwTCNEVLCPJp_ET_ZfjNJ7I9FDFTvGi1ydiwvilmBjOaUjlkklKpItN4d1wZsXcdXDpj66a2Lq0MKrFQmJ4FpXl0gCWReuagMigopUjb8wDzTcehTn8QqQSOV8071bEt6LfROi7jansbFFOKrHaYmdCwFlShDOvI8nKYBobtr7XS0rHTQaaez1YBg_YVjHpSowkvlp29c7Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=pgwHgBZsd8h11W1yNPwGGPznNis-PCBoTTJnJNJO88BWx0TVU1mW9_gRSPXkVCq8MeFQXz_uSi5M3GXEOArx-8AkU0fcb_zc0h63uNsG5__Zeuffna-GO4QzfuMF_ebjP2wojTgsTxg76IbdHiUOsLv7LZWzIh6VjcsuYBOiQuscr_Zs1T4wCzDIXjObVT8KFOGWxzfXAmNFfp0m5LFGJm2wKnOTqcRM4MNToDWnKFXAEbC65yeGy5KLQGw5j8NYATwm0Ea145M7GK4f2VjY1ZUXtoRQyoNqAy6m8s-wJ23hrjVgBeJrrqfbbrGUtdNDyxwJeOy9SJpMY-HFLte3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=pgwHgBZsd8h11W1yNPwGGPznNis-PCBoTTJnJNJO88BWx0TVU1mW9_gRSPXkVCq8MeFQXz_uSi5M3GXEOArx-8AkU0fcb_zc0h63uNsG5__Zeuffna-GO4QzfuMF_ebjP2wojTgsTxg76IbdHiUOsLv7LZWzIh6VjcsuYBOiQuscr_Zs1T4wCzDIXjObVT8KFOGWxzfXAmNFfp0m5LFGJm2wKnOTqcRM4MNToDWnKFXAEbC65yeGy5KLQGw5j8NYATwm0Ea145M7GK4f2VjY1ZUXtoRQyoNqAy6m8s-wJ23hrjVgBeJrrqfbbrGUtdNDyxwJeOy9SJpMY-HFLte3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=X4iyhMGX_3FhF6X3ql13QlIXsIMvA0M-UtrLhD5oCmijI6TJ-Hdw0GTDBbYsiVYypjbqjCY3w_IzOrM9fjWgcj3tzmU5etXiwFFg7AlrMTZ15PZn1Mwgn088-0vGrD2v486wOw8Y2kciKhreD3WA0N3RlIC6CsNuleSpu6RsCLY79P8k_t2XjPq1eMeHQDJCwCZGiLb2S8MiggpxKZYD5aLQR2gARU0ZIcf1mPbSqAm_4KRuLunfi1mh0CilaDEwECx-5M9vyfLLvk8hnd_ZGoL-uiHgJhoQlOLsW4M7zZKEFisESOmCsPt8Dx0C0mjMGmgQfc-57p9aaN5J3fD5KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=X4iyhMGX_3FhF6X3ql13QlIXsIMvA0M-UtrLhD5oCmijI6TJ-Hdw0GTDBbYsiVYypjbqjCY3w_IzOrM9fjWgcj3tzmU5etXiwFFg7AlrMTZ15PZn1Mwgn088-0vGrD2v486wOw8Y2kciKhreD3WA0N3RlIC6CsNuleSpu6RsCLY79P8k_t2XjPq1eMeHQDJCwCZGiLb2S8MiggpxKZYD5aLQR2gARU0ZIcf1mPbSqAm_4KRuLunfi1mh0CilaDEwECx-5M9vyfLLvk8hnd_ZGoL-uiHgJhoQlOLsW4M7zZKEFisESOmCsPt8Dx0C0mjMGmgQfc-57p9aaN5J3fD5KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYVANrqYQziBvgdpQliBXhOxXlVlkKCOCYyW-W6cG_tyz12320fiNTf1BxjAE0AigffaqzGZaYBviblZaOd2mgROygmzMhyPsGhmOxKik6mrvsRjQhjXmvYSYly_g8E1n-cEd4OHp8popw339w8uAN5gqIaMfhmOpjISBRNoCcUEIOY-QYqRlZSm-5YgfCQBQ9mtF4Y3AhxJFm0ujiZ-uqRrCLIhPlkfmfcAqXarw7Vr91JcN5RFo-8rLnx2WTJAYGnYPRmH9KBlNpVOZROtvGeAfNNJzL3JikU2sQF_lYHAK3b6yKMiBQifVRR3ohcH54WxS2uixysjg_T48GjNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBc90T4Tp0GS-GIALrVDiw3X-SQXRNly7umHLOfkmlg_zp0vSx6uQLfJyQpaRCIsTXZQQ5iktLHhqJFN8eh8jtFdy565EhnVcnESX_lV2jOdEMDehnnM2vQvEtNFE8EfaAwiFhTSL4B3CCVt-lWSQ6Ev3Zzt_3MYQEIHyWc1P0zJHDfsPHWA_mXB7_b23Ca5FIh0veM_rNltc7L66AhsrllwSVCoixjkdKToNa2rccGxotwuN0qjb14pj2IBMGVSbNQItIDOIpAbJUTCDU-zj0Ymo4xUaB4COXFDhh-I3g-ELDIvP-81x4kBs1BOjoopF8f4Lkr32I9XXM9Uf_330Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6f64_GRtd6_10xa27yOfnuaSMDPRCN7g4Qbux0Ejsio5vzyLqkPdR1OF8g6eps425OmSGpaJ2BeLy6F5OKTR4MfzTPQxJnd3NppUqLqdPnU12KNT1hAwftmrYY0a3CbV9m5ehvE4AYocc9QaGAdMBUANSvruQ2O503sB9kvJuJj50LVjH6t6d47bn6ZYDATzAkqzJTIdFRLxrADYI2lAtD5xxMg_-cyQvSbTD8a4Xr6qaNZtjgIutihSs_8C1o2A2NCKQgr4DFaJgL_VvIm0CHBLKgOI0WywzxDPlY04MB_lSIDK095Qs9vG4A8sQpv9fCcIjSJk8MOeV-hWrhNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=rrrAE7Aan-FKbFVc9rtETVlbeMBNOqrZGOq84iXt6bt1zQlpnLS36Un18QKRetOU-AsqfpEfwL217gOc9cc4iAS2ZIjHaPphZ8AOtL0CHsf2BztV8DVAFdDaroUzVSHK13fK4-N77rmaFGHmr7Ee7MszdDFzNbnUplg61e4l1sHVSm-iv-51tbCQtVZNaF9la8ckKoKymSatM4XOMkkd5-FuhvVCvicn_u4DhrBumNz-e0hplocetD0tEDfm0ubnVoRhrJSZJ8EKJXboUh7pCtMLA8NjvsjQz9EBL9CakWi8LA1Dpt1SBbBvzP7qzopHNrKvACyN1JR3S6TfGLO4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=rrrAE7Aan-FKbFVc9rtETVlbeMBNOqrZGOq84iXt6bt1zQlpnLS36Un18QKRetOU-AsqfpEfwL217gOc9cc4iAS2ZIjHaPphZ8AOtL0CHsf2BztV8DVAFdDaroUzVSHK13fK4-N77rmaFGHmr7Ee7MszdDFzNbnUplg61e4l1sHVSm-iv-51tbCQtVZNaF9la8ckKoKymSatM4XOMkkd5-FuhvVCvicn_u4DhrBumNz-e0hplocetD0tEDfm0ubnVoRhrJSZJ8EKJXboUh7pCtMLA8NjvsjQz9EBL9CakWi8LA1Dpt1SBbBvzP7qzopHNrKvACyN1JR3S6TfGLO4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=WtWRAUyZT7Q1neH74O3bCx6TV_xf8oCtjLNMMVAHNlTmsxhlN_VP_WviNMkT06OqISfm-KYU6-9YQmk40M5ViPcZzPcXpu7jio2JWUx1vsk2m-tYXVJCxKCTrt9pMQkfcNtxSTUY4bs8IQVMTrmErovrWtmDQCskuR86jqNVtXr8xiZdf31TOd4g_2rDxoAN3knjtscub6DiDOAA41-l2Zk9jW1WVHceqC1JRt_W3Uz4LXNR8YgYFawKo-meX7BWH7qDLG3wG8n8Y8GCwGF-AbKnOEKHxJLh6q5BM7UxUwNPePeThiL-Y23ADoYI5xTVftPp-LSpFr35M_zKhD9aTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=WtWRAUyZT7Q1neH74O3bCx6TV_xf8oCtjLNMMVAHNlTmsxhlN_VP_WviNMkT06OqISfm-KYU6-9YQmk40M5ViPcZzPcXpu7jio2JWUx1vsk2m-tYXVJCxKCTrt9pMQkfcNtxSTUY4bs8IQVMTrmErovrWtmDQCskuR86jqNVtXr8xiZdf31TOd4g_2rDxoAN3knjtscub6DiDOAA41-l2Zk9jW1WVHceqC1JRt_W3Uz4LXNR8YgYFawKo-meX7BWH7qDLG3wG8n8Y8GCwGF-AbKnOEKHxJLh6q5BM7UxUwNPePeThiL-Y23ADoYI5xTVftPp-LSpFr35M_zKhD9aTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=sKLa1kKEDxonK8DMqcSVT5XAuNrFr2dc7iWCAhin6RkT0cl_35oHrvYamZtMYlHBrvXvLN3Ndxo2JmFTKL1m1Kz_6GRaB3BYp4AMKm9B6aaXxKq8TyZ7wNXGiUa2vfYK2Jc1wE5Kxz-Qe3o4jYK2aMb0LzgrEyc2ske7L7U9qF9gNCDXNPivW7h-E_8ql4HLDGqBQ5qQIMtb-dBcz8YzbnJRaBj_ZHvQxsMCzD4uA_k4jrqXje-L-KM4kKmajHx6bLKpXDxVFm5BEKUx5qO1TdcAUSm8cJANLoAiBGkPytBfC1tX-YZVNklnuBUWoaOsXjlqu3ZypLWq6_07bNNyMF03vcpcgrZ0xSPGWZjmuTMZ_DJE3WVL428nm-3OAxLk_jZmNq2cjW2JzLpLJ5pt1AbmS-yEu33G606Z_4_cSRCaXI5lEDLo1vqLdY0LKLxoJLCBpdW7C4pqjtf9qd_B2uz57cP-N5P3OVmGO11jzQhZhi6xD4T7Mc2M_4a_yEQSkpXKE1Wx76q9Wv6GtyxcpVCt6O4eypIKvWfULMxfq359wE7AGyZXQgBJ1zQw5695diYhQJspIWKycCniJ7slMKiym6PSxPRgHxv3ZTN15qsj7esSPttl03-91NuQVP2MmjLRsjv_D8jIQ_9mS0AA29zurSqgeTRLutufxmV7Iqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=sKLa1kKEDxonK8DMqcSVT5XAuNrFr2dc7iWCAhin6RkT0cl_35oHrvYamZtMYlHBrvXvLN3Ndxo2JmFTKL1m1Kz_6GRaB3BYp4AMKm9B6aaXxKq8TyZ7wNXGiUa2vfYK2Jc1wE5Kxz-Qe3o4jYK2aMb0LzgrEyc2ske7L7U9qF9gNCDXNPivW7h-E_8ql4HLDGqBQ5qQIMtb-dBcz8YzbnJRaBj_ZHvQxsMCzD4uA_k4jrqXje-L-KM4kKmajHx6bLKpXDxVFm5BEKUx5qO1TdcAUSm8cJANLoAiBGkPytBfC1tX-YZVNklnuBUWoaOsXjlqu3ZypLWq6_07bNNyMF03vcpcgrZ0xSPGWZjmuTMZ_DJE3WVL428nm-3OAxLk_jZmNq2cjW2JzLpLJ5pt1AbmS-yEu33G606Z_4_cSRCaXI5lEDLo1vqLdY0LKLxoJLCBpdW7C4pqjtf9qd_B2uz57cP-N5P3OVmGO11jzQhZhi6xD4T7Mc2M_4a_yEQSkpXKE1Wx76q9Wv6GtyxcpVCt6O4eypIKvWfULMxfq359wE7AGyZXQgBJ1zQw5695diYhQJspIWKycCniJ7slMKiym6PSxPRgHxv3ZTN15qsj7esSPttl03-91NuQVP2MmjLRsjv_D8jIQ_9mS0AA29zurSqgeTRLutufxmV7Iqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxESa6BMJa1rMdIz1ch55IaEXE5gT7UV6QrYAi1AZrLFVwPiOk7mlVPAK1-mrqBqoX2Rsko82nXc36m2rx4cB1Yy1svPcaFm29c6dPzhv7ACVKydRBtI5fCKOPwDkxkuPQcYzzuGzADQDB2K38js3WOgTylo3du8imHM21YU3Jbc3AU2xtS-Bx_gBS-1go6T5W1afFAcsspB1QOHf-Nm-EHpk6JspDMwqU2NkunOUVGkz_YbYHlh9p__j9HFRNMbv2e6iZ4Zz2Kr4B5bfsCMaf4lfwiHA0ges8pRruA70bm8yhNPlNHdgiVT4v08HILXH8yrAAYPgGO1mx_YbO8tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=GRXjJdFp0BDquW4T47IUehx6K_z_meIbvGNolx-CkyJMHvUVMfAxrjjHcs9U1Iqn-VAyccnU-2dPwH6nknIWP-c9nqMOraRjP24_ZNFGuPtb8aJOGMHaCsmgz5h_GUqhkq82fKBbTIsub4aLnmFMGLFKRea3tLRcNzk6ilsn8NGyYOUM1P7hWjciY_JZau6RQ1UnPnOaD6ugRQ4koSMPZ5omnzOdTwthiUSHdsYr1j_jb-2JSEYOMvSLYkT7yuybixQbEJg6m4VtBQlW0xoQfXxV2vRwCLr7QoEe8Sk3LAv6f0aBmXUnFo9LeV0yA8S-mEwK_un3nno7pk-wbsHOfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=GRXjJdFp0BDquW4T47IUehx6K_z_meIbvGNolx-CkyJMHvUVMfAxrjjHcs9U1Iqn-VAyccnU-2dPwH6nknIWP-c9nqMOraRjP24_ZNFGuPtb8aJOGMHaCsmgz5h_GUqhkq82fKBbTIsub4aLnmFMGLFKRea3tLRcNzk6ilsn8NGyYOUM1P7hWjciY_JZau6RQ1UnPnOaD6ugRQ4koSMPZ5omnzOdTwthiUSHdsYr1j_jb-2JSEYOMvSLYkT7yuybixQbEJg6m4VtBQlW0xoQfXxV2vRwCLr7QoEe8Sk3LAv6f0aBmXUnFo9LeV0yA8S-mEwK_un3nno7pk-wbsHOfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=QlwtizE6-jPxGFKn6a5uD-S7PxISMoJWu0AJ0hfVhc0Zz3C6Pu1a8uZLXzrJv1QOp2GwZoxfIM1sDEvj_u9PCUh12gaT_ZSjrAJ5b3CRyJ4CfXkYyDNgEcdrEMNqbnGByPT3WnG0yvPKfaPB_MQfNb7XbuklfFP1wkTlc4yQR_pNoNoqVpDgq-v3GKb8Vz39Y9btuQdrFCRpBOnFsUnT0iP9GutBYY_vvUDZHJ1NYW1bi5hmfX_J9GnGqH4dISm4gaBEQQ93kDElLK9J9pGG5Hq_gpA0FHe62V5VNpO0XXVMdzX629oilkaA_8ctjAvKJN1tkhOnOHqCaVdC7nEovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=QlwtizE6-jPxGFKn6a5uD-S7PxISMoJWu0AJ0hfVhc0Zz3C6Pu1a8uZLXzrJv1QOp2GwZoxfIM1sDEvj_u9PCUh12gaT_ZSjrAJ5b3CRyJ4CfXkYyDNgEcdrEMNqbnGByPT3WnG0yvPKfaPB_MQfNb7XbuklfFP1wkTlc4yQR_pNoNoqVpDgq-v3GKb8Vz39Y9btuQdrFCRpBOnFsUnT0iP9GutBYY_vvUDZHJ1NYW1bi5hmfX_J9GnGqH4dISm4gaBEQQ93kDElLK9J9pGG5Hq_gpA0FHe62V5VNpO0XXVMdzX629oilkaA_8ctjAvKJN1tkhOnOHqCaVdC7nEovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=dWzwsh30pnCqBZp-CIFUL_UpdInuH9k5YnmvnVAEEu_PwibNsN9sXkH6xGdC2JRrABpzfFA1bHYDyx3MkbXSiGN8B2jCEeWMJKXouN5dFPNL_VwEQBeqgeRCxqrM6EMDAzy6G82RypDZGTH_YxIKyLoiGKVo_lVm2xh6z03FMsIqnQiuAz8YnNaDcbEG-dgzr4W23ss2gdkUWffxiYygfnSLN8H3pIKfvqFw24XqSt1eyxFMLuBjfD0wv1HkpbwEs2NhM6XLjrQ3JMJWSwfg5_nD-lbMgLOYX5SoZGSOPisLGBL8DN_ginM5I-00BanDPYWuNo_3JEz8GldGtxgdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=dWzwsh30pnCqBZp-CIFUL_UpdInuH9k5YnmvnVAEEu_PwibNsN9sXkH6xGdC2JRrABpzfFA1bHYDyx3MkbXSiGN8B2jCEeWMJKXouN5dFPNL_VwEQBeqgeRCxqrM6EMDAzy6G82RypDZGTH_YxIKyLoiGKVo_lVm2xh6z03FMsIqnQiuAz8YnNaDcbEG-dgzr4W23ss2gdkUWffxiYygfnSLN8H3pIKfvqFw24XqSt1eyxFMLuBjfD0wv1HkpbwEs2NhM6XLjrQ3JMJWSwfg5_nD-lbMgLOYX5SoZGSOPisLGBL8DN_ginM5I-00BanDPYWuNo_3JEz8GldGtxgdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=dV6mqffX1btGWIBU2N0wzVi-sBL-7HrXSzk8TdgEnnQZOzqA7mcqrU9bVpbWFQ3cU3rA-6dvypTxcdkijipO_hjxAZiK93xYKWtlMP_K8lqHFOnx48PyaSFQSSjFvZHTUfoMim2wHaqiGVQK5uEb8Q9UB_lN789QulB7Pguao8a03l3axMyOnV7WY_HQdKB_HQAuq6w-yg3RaOo6n3-AFsdn8uRhiVTIs9MPwhHVnai2-K0g-DHqrQOiZYQmY9cmvFTROlnWTtmrs4qo4m1MatJKFVrhhf6lBTLlhIl0QhfBNu1PuK73eaxXYV9QlJEBikhpRd4IenDd3pAnzbtGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=dV6mqffX1btGWIBU2N0wzVi-sBL-7HrXSzk8TdgEnnQZOzqA7mcqrU9bVpbWFQ3cU3rA-6dvypTxcdkijipO_hjxAZiK93xYKWtlMP_K8lqHFOnx48PyaSFQSSjFvZHTUfoMim2wHaqiGVQK5uEb8Q9UB_lN789QulB7Pguao8a03l3axMyOnV7WY_HQdKB_HQAuq6w-yg3RaOo6n3-AFsdn8uRhiVTIs9MPwhHVnai2-K0g-DHqrQOiZYQmY9cmvFTROlnWTtmrs4qo4m1MatJKFVrhhf6lBTLlhIl0QhfBNu1PuK73eaxXYV9QlJEBikhpRd4IenDd3pAnzbtGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=nS6AOgt4XrHV2kMXJrl-2642EZjAv0AMBxUK-DHCWL2OUKORgyV4Hse_SXGVASksVCt8FvplrXoixrlE1zcZmIZjaLyeU5mrfSR4LdhSNfP1Bt84m5KAvQTBAUGtHOcB0Hm0tYap4CiDctZ6ccJ00WoFgLBXhMM5DbONMt7k4F9gznv6xXyu8Sl7hrJoZn58n5cEcIrd8QfdyyMakqLrHbRCaiSvz4Ai9ZzDCvmZKuTjnnRF4R_DKb8MCg_3mDkB4SLIIbzWdO-DaI4KAkAuQS-tz-tiCehvfKqiC8NDWouC0EGk_-SBfpq5LF9asW87dLnB_D6Q0qey-OGaRQdoGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=nS6AOgt4XrHV2kMXJrl-2642EZjAv0AMBxUK-DHCWL2OUKORgyV4Hse_SXGVASksVCt8FvplrXoixrlE1zcZmIZjaLyeU5mrfSR4LdhSNfP1Bt84m5KAvQTBAUGtHOcB0Hm0tYap4CiDctZ6ccJ00WoFgLBXhMM5DbONMt7k4F9gznv6xXyu8Sl7hrJoZn58n5cEcIrd8QfdyyMakqLrHbRCaiSvz4Ai9ZzDCvmZKuTjnnRF4R_DKb8MCg_3mDkB4SLIIbzWdO-DaI4KAkAuQS-tz-tiCehvfKqiC8NDWouC0EGk_-SBfpq5LF9asW87dLnB_D6Q0qey-OGaRQdoGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=FQFzE-_VpI5zTqlP671zGeIf-de8BqrTJUoAltd1n3zvEI_Cf1KPyxuVkC8Xl1OyQ9hL79z_EioRjQQqLb4AQoClZxdI5-WD3Cv7q6vsuBgE2-R7yVGl5q5-UUIdVw76onpotSgHKrfMFKH3CfYwWlURLhpbTon8pbC0EBlXKv3hLCP3RN2QIucswPWaJ2NegjAWrwHXjj3DXCJ_QWzggkfO0qaMP4WmcX0EEnY9k93LssZoA44fYe4-8jqWHjJ5LQ69FSd3dFFrU43HY5tnXycKvJDS_GG3tzEHUFD_6hetHQv2BiKasYdohFog6ituKbuW5TNkKgT3V7036WTU8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=FQFzE-_VpI5zTqlP671zGeIf-de8BqrTJUoAltd1n3zvEI_Cf1KPyxuVkC8Xl1OyQ9hL79z_EioRjQQqLb4AQoClZxdI5-WD3Cv7q6vsuBgE2-R7yVGl5q5-UUIdVw76onpotSgHKrfMFKH3CfYwWlURLhpbTon8pbC0EBlXKv3hLCP3RN2QIucswPWaJ2NegjAWrwHXjj3DXCJ_QWzggkfO0qaMP4WmcX0EEnY9k93LssZoA44fYe4-8jqWHjJ5LQ69FSd3dFFrU43HY5tnXycKvJDS_GG3tzEHUFD_6hetHQv2BiKasYdohFog6ituKbuW5TNkKgT3V7036WTU8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=nkJMJu5tlltJNfFW_hCH1OLG_4AWkabOf8MQ1PpbqpNSydYxkqf0U096oY7mWbPCX2K7-DwU_61bNJIuaEeAMKNAGFunIvTtixU2_9wUxNZeSzquzVvgaxVuTbh0SVuaDyBsRlwzd_Tpv22iyTFR0EsBW5fOPf7-pC2f5x7eSg2_cV9KVhzdIzZntgHcCUCo44VR0P35VHiScCi8yV5GKkDvvTz7C3gv8Z1h6pYY-czrZx1rB-EQ6Z_VLS76MngvrvhTN4RGw06ml7Alsq7NfPcPLf2gdGZOC0vP4VNwuGujYFaKyRtKGiRFwq7olrc06zUx6bWBIEPCOKd3KDH6mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=nkJMJu5tlltJNfFW_hCH1OLG_4AWkabOf8MQ1PpbqpNSydYxkqf0U096oY7mWbPCX2K7-DwU_61bNJIuaEeAMKNAGFunIvTtixU2_9wUxNZeSzquzVvgaxVuTbh0SVuaDyBsRlwzd_Tpv22iyTFR0EsBW5fOPf7-pC2f5x7eSg2_cV9KVhzdIzZntgHcCUCo44VR0P35VHiScCi8yV5GKkDvvTz7C3gv8Z1h6pYY-czrZx1rB-EQ6Z_VLS76MngvrvhTN4RGw06ml7Alsq7NfPcPLf2gdGZOC0vP4VNwuGujYFaKyRtKGiRFwq7olrc06zUx6bWBIEPCOKd3KDH6mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=KPFJ2TYG4P3oWoCbD__artGMvqAHV8JUVIKmYAN1pIf7mCEC289F8CqBdfgJXaDEZWZUjuTnidTmWc6ofv2R7V7rgaRVALFYbgrh7UgBK5kOQSXohIVCSi8_c8bA03jBGNvV1n4_U4YlP49Mp5MIxa9DtcnWDHGSQHtAhxnS-lORyZWgrWYYy6H0_t270YKtUbbvdwR8SLoQmLV8XJtc9zBS1O-4PTzbLq8cGMZvpKVtw-B6UbVMw3PZdCm1iK2w2Oma_oDF5vn_yCCcMTmvWhwV2UZEPT0oOMDmH0BxT8LbiM4HzvwQ78JALCpMray0h6gbIjQOda2nKqq1JGeJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=KPFJ2TYG4P3oWoCbD__artGMvqAHV8JUVIKmYAN1pIf7mCEC289F8CqBdfgJXaDEZWZUjuTnidTmWc6ofv2R7V7rgaRVALFYbgrh7UgBK5kOQSXohIVCSi8_c8bA03jBGNvV1n4_U4YlP49Mp5MIxa9DtcnWDHGSQHtAhxnS-lORyZWgrWYYy6H0_t270YKtUbbvdwR8SLoQmLV8XJtc9zBS1O-4PTzbLq8cGMZvpKVtw-B6UbVMw3PZdCm1iK2w2Oma_oDF5vn_yCCcMTmvWhwV2UZEPT0oOMDmH0BxT8LbiM4HzvwQ78JALCpMray0h6gbIjQOda2nKqq1JGeJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=Yhxihl6F0xoeZVMcvgOuuECz_cGHFXm5Qknj6VHzn7QeE7GHWbxHcHWgAcItAA5V79QGOvcdne4EZpKhrcM0HiGiHcHq15uxiMmEtEPSletLtWhRFUx-trocdg1vWAvseO_YLj5agGaKdcfDgm7IuB9JzP7jhA_yAmIg0SxRbvMVL1eo-ORXINmxiwrXjUOE2YhTADv6woi4xBR84qJNVDbDny6XOlAaaS6OcqQcLSTYw6ZoVM6b2BfENCaRrBZLXL6Cx5nH45hxjZpluDAKCSxeS-CV0lYDPwYSjd6gMNqnQtFBY8uhdAlem3N4AmR7jQ8Lr52DusSgW4v_ED8YBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=Yhxihl6F0xoeZVMcvgOuuECz_cGHFXm5Qknj6VHzn7QeE7GHWbxHcHWgAcItAA5V79QGOvcdne4EZpKhrcM0HiGiHcHq15uxiMmEtEPSletLtWhRFUx-trocdg1vWAvseO_YLj5agGaKdcfDgm7IuB9JzP7jhA_yAmIg0SxRbvMVL1eo-ORXINmxiwrXjUOE2YhTADv6woi4xBR84qJNVDbDny6XOlAaaS6OcqQcLSTYw6ZoVM6b2BfENCaRrBZLXL6Cx5nH45hxjZpluDAKCSxeS-CV0lYDPwYSjd6gMNqnQtFBY8uhdAlem3N4AmR7jQ8Lr52DusSgW4v_ED8YBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=VrvLb_NOPG8Ei1z5K6zQc2214jmHFXSw_IS3qD5XR20zecFUx-sMDqkn9D8RKdLk1ERLYA5ClGgFk27p7-rQAiEGwJeyPZs__Lf_4ukxy6mCnWD5xxu1HCttMmcZVKeCn8bvDij32TAJxvUYE_Rhhm9AEzMexouaGv-c6xSe9RtztTlChPXZUsi9Oz2PM1alxtBSvZrhnThF8Wy7ES_zWAXcHJ-cAjqEO5I7aVI-MjUue_LRygrIyYiqzqH-W42CSDHiWf-uA42lJ3mUJd0PaiGO6k1xCsH8X1O_kf8ZQ1Sn-qz68A0CMJLbqDbjKAQ3_FV-lC11VWWZELszuCJFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=VrvLb_NOPG8Ei1z5K6zQc2214jmHFXSw_IS3qD5XR20zecFUx-sMDqkn9D8RKdLk1ERLYA5ClGgFk27p7-rQAiEGwJeyPZs__Lf_4ukxy6mCnWD5xxu1HCttMmcZVKeCn8bvDij32TAJxvUYE_Rhhm9AEzMexouaGv-c6xSe9RtztTlChPXZUsi9Oz2PM1alxtBSvZrhnThF8Wy7ES_zWAXcHJ-cAjqEO5I7aVI-MjUue_LRygrIyYiqzqH-W42CSDHiWf-uA42lJ3mUJd0PaiGO6k1xCsH8X1O_kf8ZQ1Sn-qz68A0CMJLbqDbjKAQ3_FV-lC11VWWZELszuCJFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=lKv1lUHHxSX1vjOKOZFvZRk5QDlwM0gp5jXs6VbMuwx5JICHTdLNxE7n3jAN9AAqFCezPKeQ1vaISP0Ek1oeQpLkQqlHFsrDl0nb8epx19pORVtant_3HW7NElTAIIe9gRo-hXpdT4__yPXFAClY7H7vxk6zOUCpTkTcmF4AUsnFAoCLmfFzJ8Z3foRH4kRnRP9IVaxX0JnPmemOjHKiHKIBdoO4og-LDj8rE_XXRxO5alE3wew6Com6SQdIrCPs9QqwI-bx5lQFx9vVAEKmuRJ8PbQypiCP2Dp8H26P4ci_kIhRD2NvvOoNMXhBYIOClQJAdqcvmts5gAJEEyUlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=lKv1lUHHxSX1vjOKOZFvZRk5QDlwM0gp5jXs6VbMuwx5JICHTdLNxE7n3jAN9AAqFCezPKeQ1vaISP0Ek1oeQpLkQqlHFsrDl0nb8epx19pORVtant_3HW7NElTAIIe9gRo-hXpdT4__yPXFAClY7H7vxk6zOUCpTkTcmF4AUsnFAoCLmfFzJ8Z3foRH4kRnRP9IVaxX0JnPmemOjHKiHKIBdoO4og-LDj8rE_XXRxO5alE3wew6Com6SQdIrCPs9QqwI-bx5lQFx9vVAEKmuRJ8PbQypiCP2Dp8H26P4ci_kIhRD2NvvOoNMXhBYIOClQJAdqcvmts5gAJEEyUlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=C3bzUXeDNgTBs0S-AERDwDjgKuzxOzQvaAa2bu2_AK1VoBaLbQ7Fd6VowmZthtD7-oGb2UemwKjXEOOtqYtHW22SL0f2sg73D75por6bpU_9VXeKbkvtEi89taedmk9WlrJo1fyjv3pF8f0UI55CZaSV8T-KC_MppFLzUd9ybQarpBeteui80XzpYmUIYUYAiFwPZvwYBq699BHCIy-VNbJq6Ht1a9sdNp3APykT76GjV3SqVZB1y2i71SzbfYH9YeYfFCElmNTTJVJrjxFoMw_n-ixmOGN3j7Dny70YdUwCKVA8gez6QA3AQxbSXqygaL-Gpi3zbtZ24kYqlAZMXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=C3bzUXeDNgTBs0S-AERDwDjgKuzxOzQvaAa2bu2_AK1VoBaLbQ7Fd6VowmZthtD7-oGb2UemwKjXEOOtqYtHW22SL0f2sg73D75por6bpU_9VXeKbkvtEi89taedmk9WlrJo1fyjv3pF8f0UI55CZaSV8T-KC_MppFLzUd9ybQarpBeteui80XzpYmUIYUYAiFwPZvwYBq699BHCIy-VNbJq6Ht1a9sdNp3APykT76GjV3SqVZB1y2i71SzbfYH9YeYfFCElmNTTJVJrjxFoMw_n-ixmOGN3j7Dny70YdUwCKVA8gez6QA3AQxbSXqygaL-Gpi3zbtZ24kYqlAZMXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8nrh9j_x2tk5RAIlk7_IcnXGLSMCbIcxoGfTtcsClP8BnVjJL09tvFYrfkRFjSqvT6glyUsab8qPIJuxkcydsHWNjSymfytP4m8R9NOMfqDuZVwvWeMkGUz7JBiyz8ogfu6kx_MYVkNR4DbWr5mUH7nAqsJUqGhiCwzPDv_1AJnYG2U2E1oSTm5H5zvOlvLGkOCwl_U3nO4Yr-m6P_gL3yD_Qc1LnV9r8yO3HY4jEgc6Abb4Hj-Ef6ZI6w2UfSZwy6awKCBou0axTJHbIzOvOFXv3LlNquSRatGwOqTVC81Z4rw6waZVVDYn-g63xvMlctdShuOzxDeiyLJlr0XNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqFhT73RUuOkT5bjmrC43-NVChMmDFI4SC-DGaTjnN01-8fUROKsjZldbvuDdxe8MidaD37iI7JYu4h3dA0K7nuPKx37bpBwEOa60u9vcSKevwg0fswf3Pf78nsxqR5qOnaEVVF-YIzhgqKmg7-PravyPUvQycEBZ1Y0bDCUyQICCePAXJGQ-BbCVH87Tvfse3ux4gvgvYkeSrbnjcGHHtRyb2kbq2G9aLxHGTbkdz0qSFnJvblv-pZS2jNzP_zR27Sl2A-PZsLzhkFscZC2If95Kc-pYYGHtpxj9oyRleklhDtrAnjyI_RcPSKpnoqDeyv2gTZWEOVWTOYo5-sFzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGaotN43tk9Do_ElHCV0TqhGWXAjmCnVAHtH3PzzTK0lqdZfqwLNp04Z5rw4OIbcJy4OpOOOxeEbZrifkl43qutNTPYI1v7Sz824WoZ03NGL46RuEVjiBvzuwabU7pD0-v_gZFnYvcax1sWo4alstN88LA3A0wt16Ia9_LalTCtiFOCkCUCh4tPtvP0H7qZy2YHOlGyt29poPtvTQlHIXFekU9QiI2xPEdUTMjY4ITgGZJ6vLNRywJGaw9LAUcBp4453nVDh72Ne0jxWQw0qipii0RiUjsr5O0F4MXcdQ7vymdfgqNftHW4Ud416kqJ-K-8tuT9y0ila9bSusCs2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6l0HdEoOJJl8Lhc4UgcHSflowm8EHkohTZShERuOK8cZKBWlEjCXIxWDuu7bT02BA0uZ7CWnQCDTt5gZWdYPGYL9gTxHbgfob0BU6bkZKjCDKUBAHeWYjz1o8NfiERx7AWgvPwyyz2F5CL1C1XkGO61iqvEOYKWMKQ4pERwxa8pqj0ol5ZtfhBRSMD8GGBWus-ZeUjiDDoKBwQXJ9ZW6wufJ-la3Ukkl2HbXTHuQ7enhD-jxl6CLltuvP3oMo47prSpeIU12fMvVJ0FliLKY0RrInHy7xMySX36R8o-8GefDXfSPAU30Ibaq6POv76QD7sVaSnwjVB16zsv5p9sNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=SoMdZoQ2MOW8CzZHMxTHgKrf-KGjYSju3iU-ITnPqYso1pkbgUaGzrnCk9uitBi2bE7WKfnI0d7QzOCWxNba8NbVQDhGTpn-ClzIZeKojYDkNFIS9DBP7pdXidKOcEyciZDlm6_ElNWuO0V6A1IHupwtlViAGA8CjCAJmMYQBhGHDppm_6sUI6ntS5IcVBL-3JyovBIRNbcPdV2T_HuXRT6mg8xkri6tTghC4bHdyyYS80lPlDaD3P5WU3iQeB9KIsLzxZgvXqdtwJyd-HZqt9ijUx55xh3htDtUDp7hnAXVgeGcaYHnaUCcFm2raepj5wjXKeu5QBf15YeHIU_6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=SoMdZoQ2MOW8CzZHMxTHgKrf-KGjYSju3iU-ITnPqYso1pkbgUaGzrnCk9uitBi2bE7WKfnI0d7QzOCWxNba8NbVQDhGTpn-ClzIZeKojYDkNFIS9DBP7pdXidKOcEyciZDlm6_ElNWuO0V6A1IHupwtlViAGA8CjCAJmMYQBhGHDppm_6sUI6ntS5IcVBL-3JyovBIRNbcPdV2T_HuXRT6mg8xkri6tTghC4bHdyyYS80lPlDaD3P5WU3iQeB9KIsLzxZgvXqdtwJyd-HZqt9ijUx55xh3htDtUDp7hnAXVgeGcaYHnaUCcFm2raepj5wjXKeu5QBf15YeHIU_6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=DF7WuqSMNXbFdAo4r_HFEmeCsbvvFa63kA29ietOibpcr7GV8x_lyFBseSvYGfhT5afNwmx4KaZ5z-TI6WGm-IOk4HjKfkBd87tPYSpJBhi6dIyUuPO_U7x0erWPPSLxLd5UhU_OJWVmdULANWJkNn2xvIAGzeIKN_JIk3cEsr954XtvrY8w8R7NR3kWVfCk5_D0NBNNq1Ly1UqmmmFogvlLYkSbnwzUZ4BU0BN5KP00hP5rr1H1kPKfsA1InwZt4qkVBSu1UVT5w8KP2YzIpsjBhn64zA-4hUbIaeZIJT0VBTP_2lpTNAahLoblr6HqxWNUEfE3jSJI3ilfO8m7TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=DF7WuqSMNXbFdAo4r_HFEmeCsbvvFa63kA29ietOibpcr7GV8x_lyFBseSvYGfhT5afNwmx4KaZ5z-TI6WGm-IOk4HjKfkBd87tPYSpJBhi6dIyUuPO_U7x0erWPPSLxLd5UhU_OJWVmdULANWJkNn2xvIAGzeIKN_JIk3cEsr954XtvrY8w8R7NR3kWVfCk5_D0NBNNq1Ly1UqmmmFogvlLYkSbnwzUZ4BU0BN5KP00hP5rr1H1kPKfsA1InwZt4qkVBSu1UVT5w8KP2YzIpsjBhn64zA-4hUbIaeZIJT0VBTP_2lpTNAahLoblr6HqxWNUEfE3jSJI3ilfO8m7TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=u9cROBj6yc9kvLk2y5fPeJAubNsQAj4b4W1p7l-mbpeTvjU_ehHh635czqv6COD1w9UHZ35rNlOoHt3QQAe6qV7Xu_QDnD9c6a5Jnf9jD3RaDFEChEjffBXMxEEFtpef-BLL2j3pNE_ycqr7ywW5MHZyF3-TeIRC_u9-AbFD1TyFAFlEwDSkLgEiQivMonklwhlq9C9lBvEoCS87VKR3PwvUOB-EH9qs7AapyTGZCXH0al5rXcHFZHRIUDgskoQKIRGLtlHb441AG4d7AuQ9N6FMgxyR9xEyTZ0sDUnULBRDd20ER6x8XWFv4XEy6sXwBxYrtsYR-98yN7op4Q_vqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=u9cROBj6yc9kvLk2y5fPeJAubNsQAj4b4W1p7l-mbpeTvjU_ehHh635czqv6COD1w9UHZ35rNlOoHt3QQAe6qV7Xu_QDnD9c6a5Jnf9jD3RaDFEChEjffBXMxEEFtpef-BLL2j3pNE_ycqr7ywW5MHZyF3-TeIRC_u9-AbFD1TyFAFlEwDSkLgEiQivMonklwhlq9C9lBvEoCS87VKR3PwvUOB-EH9qs7AapyTGZCXH0al5rXcHFZHRIUDgskoQKIRGLtlHb441AG4d7AuQ9N6FMgxyR9xEyTZ0sDUnULBRDd20ER6x8XWFv4XEy6sXwBxYrtsYR-98yN7op4Q_vqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEYbvoklICVBtlihNZ7XGtAFT_uL2swSyYKKP6UuFp6TUc9QAkDMZdJAQ1CypmpU_UqRVWorNXQ7Wed814dbDyfKdpGKzikm_UaOt4hnz9xALD9XHLZZxfbjoXT2x8-FFtgSJBTChgeuoBGgxJOxFsuwVrNu-FE2zcqNx3Ay3nvGexLqGZ3oRxvy6ZcyZVSEQb8heYmgx09nbxcYHApIi-VrRQthLkEMtabzrTinhrJbRTQJKJy_uTA0zkYZiuYKpAuB7jeqUTLpyqFs-nxnUMvwYk1O5dqvfX9daW6stjkusQcK3cTioo38_IvSB9WsR4_99ASXaOzIZUUNFhSN6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=HjW4ErBrVj0Om-pznKg_eZVaj6tRwXsUN94UYPFIzboydJpzrBoiE-YYdzQoGTj289aw_ToffxND0bqyxmfCqGqd_ujfPuQesKyBgEPhafB1TkfWiq8uL55UVtdGOTzx4Xn2fXHICpaF-6xm2yqPaaSn-12MvlQnHv20FMbxw6oZ68RWKEMKm8pdGMiqpUqRZxRfo3aCDOg94e5o11t4YGgjvz-f-iZ1INiuNbu5J1I19Wr-2BBOEnyxr6FRerXyzOWIu2rkKRZJBM0GA2ioecKVgpAKBCTji2jhvUe0d6GLuo2o3ayqMq3WWioMfwPZGnEfgDzW9HSSe9_ZP0m34w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=HjW4ErBrVj0Om-pznKg_eZVaj6tRwXsUN94UYPFIzboydJpzrBoiE-YYdzQoGTj289aw_ToffxND0bqyxmfCqGqd_ujfPuQesKyBgEPhafB1TkfWiq8uL55UVtdGOTzx4Xn2fXHICpaF-6xm2yqPaaSn-12MvlQnHv20FMbxw6oZ68RWKEMKm8pdGMiqpUqRZxRfo3aCDOg94e5o11t4YGgjvz-f-iZ1INiuNbu5J1I19Wr-2BBOEnyxr6FRerXyzOWIu2rkKRZJBM0GA2ioecKVgpAKBCTji2jhvUe0d6GLuo2o3ayqMq3WWioMfwPZGnEfgDzW9HSSe9_ZP0m34w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
