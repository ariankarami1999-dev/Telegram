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
<img src="https://cdn4.telesco.pe/file/Jiw9pe1vta3Gog8mIMz1nQVW0XegOH7KG_VvJzsP-GEQmcdKN-PyCwF1eZlxVBLUQkNwPNkKv-XGIuBKCdRd4L3fGyz1lvZTBYMEhmknE00td56WVSuMAxIG9MRWUEOmGkosGtQ7voKUqQDD269zyo3x6rIdpaWfO2InDF1vWIjrarr4tAvLVt5fHSLkdsab0g5Ia37psYObv3tBlm4xCBAp2tWs8CaQa_xqyfK0H7gbBymgPiOj6c3RjCwy1U_ddrVGfLyxyF7KH28VEYyk2vtXRQXbRNJA6NVcCBQS9egSbL1jcvDrUm61CUzHbg_F_ib40binEsXso8SwYUYwuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 570K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCJPOi_nb9pUO-N4wIy54s4cJWqC1_NgAlaKjWpjk_F60ovf5pZO2Ln8LOppYLSM2UhJFg5YY7FqkbXwsmfDKDn-OZOyuKxTxiJWQf5WL9SED_gPwn3dNjTmVIaFKVinG4ZbT4hu2P4SBg_sPTp7V64f2h24ZNxKzZkd4u4x87M64nvxu5w6OsvL69b7_RkY5Zm_3foh4kt7Kk0tDdkFxdBXWf9S7hScT8ilWqz-krAnOxGFkB-i-zil7UvmCdP5-kyBAqkMK_eCB2rzSWP0EL-JSyPja5JTg-qi0qG2ze_GuLGdwS2_sTkgBn1y0I1ZkXbF6UuXDmffu1up2G2enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npvB-ORMNXp7tKr3vk5V8Y9L6fiw8UmIqPSDy2ecDr-qvNzDl51TJ2ltzpQVYTNHZHnyKuA2IjWL-Jhb70_Tyrk4dsBEhn--h8mJqNE_weDFeQX9RVosea9H2WvrBWidWgatm7H1CDCpqfokBe2BzuhzlN5kztCO5ANFVnI1_3V-eTuJIM9FfholoTOJlQjErd9-qro9Vs5-zcgSbDMFHsjA0icm8vKweVayIXgjbC-CRUKSsQlJcsBqPJzeGZh-sAM3qOmhpkzE7AYZbGRYlEm_owTEwyY_fJ_7EGsQ6jD50S-5HhR5Vq7N0PPR3tTQWVf63LZscA1qRm8XnWmhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kxb77cA-9qYkRi7j2ysfvBr4_VxC-P1IZM5gEjGyxRm592M8L3HDrRHG0lI8y8sy9ydWEpixk8TJ-z5eNlRQWuzvZWXosZr6j2V6zd2P0g4sKnbcNM3oT5hjsrPbzk3z_mogpc50uEHRhlDGajwtZH9aDA-JZtHO8EuPgAjx39hNZznDvOR47XiA7_3QNrIwnIf1kmeLhLUGKG3EL9UUwVCi8pJJE7wmcMQRmgd_t-4Ad-TncViAQZC__bKfRSgiriezG4GLwecHiy76ITdQidnxVQ6o6IE9UXRTGAEZPwULpfZOvGOjj2QIrR2d3ASpSrwNJ8baJVexPowtAO6-OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyyIE0oV7ATWAmqnYtGsiNRLz0HREuRvN2MsIhCEqGLFZYaQYzcXL0AbtLc7RpMYvV1FkFc570NKXplD_1KwuFrXzaPDZOJmL8bNso_ffHBEA0ch1dl1GOXGgsj8XguIhz4phmBMH_uBNUyDogtH5Ieo90AhQB325_qTcOWZDJajvztcrmDl6titcddvl-L09yecgqsiPIOtn3IfHicOMIGySrqUKdtJZnbW4j-Payr4TLBlyxGenmaf4L4zdbEi5yzfm8DLi0kAww3ISbA16C3ee_LZ8RrU9G68cOTVtsV_VAYtXkD8K9MZPq2cvpSX8MpY9hI4hqIUnL_bFTMwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omwyTy3ZgxH4ydfG0rSWK8cy8uwBQl1vAojVqsAJi0dqEY8zv0ouxAwSfFYQff6_5UfZ43XBNr5soQakNS-ndFqrdfIPHtssa-utJODwJzclDJG3-NKhEFRYvsgx8DxV-YWR5SboqeB4TI9-bfCgPVGgVVX5VXi3nBri7hK9Qgnq3RwvOHvrkgY6yiFOHbs_SwQVvg2VN2VN8OwV-fWTNMRqrWjv0ij41Ja4KVZagG2OTx8XIzrBsa0x08ufkDwZ2Cs8xMpgnfHmUOgaDCL4b2N0SSQ8eA6OASxORaBY9b0ybqcDKbgowH84CgpU9y2m5-vHOL5y1xs4MIqFQPeHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
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
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJEtlYP9YUI1NBvHOpXtsr56o2GKQwxW5BDn7ip_CZ-tKuiQn3Cxrzbhrws4JOZNCtMEv89LegQJbHPY8bijT6_2vhamACVZHGiOwJBUDrgN4G7QlWUTtLPBcX2zhl9cuYEANzQlcExZDkBEhm-sMvmSp-B_cO0ESOX6aLXUp22h1Helf_XayHMUPyyxnJj7IhrssgGPkLXox1_Zy3p-Sjk-SnnePXqU3G8XIH-OIc_tIqM6d_urFlHw4u89fmNkKIMWrZu03yleGO-BQHIRj7r5bSP_4TlwdAFfp3SLXbtGUa5AY33uu8wat0w5Y59c7sabZaMYcaNAR6JMFs-qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgak10HrOXVM0zjntYbkECMphbo3bS2BzLgrbgN47Q2bhw-PBlDIo80bS5YwBQUeT8enT2kF8mikRdQUj5UCqyXCIOP9GBBUiaHyJVZ2eML4FKQBkr0SXvmf9bVS7-eidJDDnrD2ucEk-WkJG7Sn5jna4xdP2zSWaansYdLrxQ7Zgjx9dV5HFfhSPJ8LjjmEWRqO0q09gWQGFwGZ4xZFOtt_NN71oR4PalaZ3256j17M8MuQgBoAPFhfFZhpCzmBE7AUSSHlx_s7xVZzcs49uzjkkfVwTfU37kK2ADoGWKV_iPChglQykywWe-KUiWGGvhtuS-DlDemq1u0YzWJydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOaaiU9deyrH2ZfigMmxYJTqMVrULYegZpzsP_IlM6iQeL7ATrND9esb-pyAqnUuDgvXhhd1qJa-bI3d-du12jQvtz4W4P_FYt0iS3R77J7Q46twhSNGoDfQEYHX0s9RhoT99jlvDs6J1X4z0Z7xS9EqwRS5TZTD2HU1Hh3pag7wIjGMr1Ac_yUznrf4lxxG-Lncfgri-u3XlcfG9XwFEmLM-gVQn7Y_dqo9sVITojkL7Vu1tvzusu5tcbAtwcR4JJiQ-e_E9qnyWE3If9xu9OWe_eq228BLkmlf7GEaQBPqKrN9CZcpNCu6WzQ3Af2bEntQUiC2sVEWWem4gHSEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jInb9oV8PzyrlRUQ_yTak5xMQobfrEA1qIPJHZvnR80qg6Fzp5NYU0Yah9LLhoj0bTMyRUHHxIUa-jdiPsZTNX33YcaBBkMuWe3otcDwz9ibtVxFqtDuLC-ItopfxDIIndjJxqVjtkuJq9GJ42kuHSVwN3Rk47mkteYXR9NQpL75TskHvOtZ4Z2-XkMRnNtNySz9mZ2tqkxxnwMgnwOVkGTAG-WOoq90qZ-Dj6A-SeHtSehX03JEdOc-ZU5zkXn4xMIO3LaFJSa0qtNb_jfkpH4mOjZhziXBAiND2-zIEX85b_o-dfJhux-UKBcEqls7oNvbNcMNuHWH0TiTPyszpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPGHge9v6PpQDyL2LFZoNJTGpphZVoH4OaYRJI_WdhZy27VhdtAfoN4E8C204Qhk3IAb3X09L23VqwhQYBpdLW2PD8IphdY183gnOAMxCN_eKUqyexvIvBTPfYRvORuNliIhGQOiIuXkZXQ915RBy2wgviULRh1y_Bsuxs8Z2knpSOta5-pZMm9xrBDfBBa6Y29gXUW0q7-UBTq4w9a961AvoAJAJ599NKvHW9mvI-5ElTFiMD4FVnpYJIMQkC0Bb7aS49_1okcjMPN7smceDog2h7CBLqvcYLXlrHqapmBNNliu5-T7JXOygP1OZO6pXD2LGxxxKN62ewCXslo65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO9aBA4No5IEOFgHswleRFpQpoile52AKmtyMYsqm5gXdbFIrwJWQUuAG0SlQ63l_atyaOC_fAlk-ypu2fV7CcoCufCCmJqkaQyTUwQrpOJNFA3MIxVWcFUYocYZhQybHRhQohhO6flR7zwzyuyuXFX6FNHbpjAY7G7sm8bO22nJy2_UApSz44k8Kb_cfHgyogMVzACAi5xDadNYTqkuqYUtMs17s_0Em8SmFS_0tz3NsavATPJZtMU33UoXlZqFsdWv3ch9F5Ofl-WsMMN2SC4lcrXJR4HQOycCknzywM1DPjv88LTY6lbhqjZICkqGSmgtHiCtKUZddzb0dZZ4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig7dbAWluVnBqrmsd2BhSn78L1df2-M4Xqm_jbo02rWdiFRtxfva83_GDl9pXc5mFWKETG-ozGs7I_bq9e2cTTfKk53kHXJsixFpuGlqJ5CZhECC-YTziVf6EcpUEzm9EjT22LpIseWERQAvMnOOzz1l2F4aBFqUhYWNBHr7dixQL37xFJ08KRuwiyw1xqz6k4RsUC3EYvcHngB1MCaeBWMiUuqEQUCytykZ8bu739AsELcfjAq8RmLh-kr_eVNz4VIC6sWrCaEjptWZxvtmpAztTRE9nXaZWd_Rl80lWIuGUtq36uV2XbqkX-FgqpbOHSfG8VL96LcvU_rSRIpSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prRISydCrGW-yIRv8sqRsQjNKvSS-80LA-oygw9zpXVqU2emTYEp40AlqcpDF83T3eGRv8J9SFIAeI7Ea9C9Z2e_E2-ParLD_fx718AIgAjN1J38vfmwgNWmGo5_ejZKjRLtCuQymqsnMk2FcqEZqTs1OID2A4x1gHCwEv7bKjnHXIkuB3OFnVObMdVMv9cz7nDyCk_gLR5yYC_TICS1BCHyapQrGc8IeafYplrwdN8_BtaOu2fC8FPsWCqFTEwbNZ2hL86KUr6XDBu3_niykSY4mhmS7cz_vgZuWQJ0a3UItW4qj0V4WM5p8Gf23DGyUJxgOEEuPP-wKFzGSrfM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-Mtrjab160LLJT04DkgcJKn4vHRRBE2ai_nd-zzMOg8Ql-UaALpgSVM-TXZ1a6dxhz_6fetH9tY9ffiqIlZn5LQDqca3OSwGufUjzfUngKs1xM7JJDRLRYkBRUdM0Sy5bSF2CmFylmO-P0Q-v070bQm2IxgrTkYgUjomuCgcxH8HUSd-7mFYF9HAJvSPx7WR85QgaGmFnqD6lEynkrQM8CNsZnodLJLLbgtcTlZl6eBQFNO7fP72wsluvWg2wYsDknvTYSiMnL1UQRwrFcHrCwyBGy8RnddWVx9_1R4HOTEcXiqu2fhIgCJEoZECYENUyYQREAq8eRuKRMsgmHibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQCQul8tfod6MqiDN_vYbGdQI6Pw0X6b8ZXMctyZ24DXFNULlSuDmS2aaArsH1eAJJ7es-FsCT1HBaCXlfeV4SCow8nux7CXT-wAXHlEFOF85Z2x5IXIHOa5Di_GVmqimI1pCZgxXg4vagIenLYm14KkqRxNf2CASD1C-Fe_DtK07RgPa-lP2FwN6EFw2qqXSmkSz-aGmuFpxzlCn2FN57xyeGFzQF3iz-iXcUqxZnhnsDTDS8cifD2n5sUneYbnXLf4V2Mm_eRzCpu8-pJMABujnU8I0zs20aCmvSzVm4Uz24N8-sA5AL2rnjjMda9D2gcRWwlLcpvKjB64qDUMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=BC6qG-D58NKl_4-dj7Amp8lQkSGZOdBXBFkURalj_0JzGgEFpmvWDfVX8G5A1jNugWKXCEFWXfXrr38AVddYLKf_Pq4JwQq6jpFbhACFjGmJHhbJ4NxQuR2vJ_DK3BRX8F6IDGxUQdoyXhRzaBhsngrow6XMpa4FuvZsF-fkHjvAj-iUdmzcq8svszzUMxQT4uhtcCzFgpN9eZOWtXM6IOB6Ogy4XxHtAn3O5oPzad6xXp-5tbnTKEOoRrqYC7HcfvOMRgzsL3aTqNHvZsOSLZARDEaEExXRoDgUNGN35s2baPCEUfOPCzJX_z0g-lQmh8ecZZVs_dOvWVYWWR9bwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=BC6qG-D58NKl_4-dj7Amp8lQkSGZOdBXBFkURalj_0JzGgEFpmvWDfVX8G5A1jNugWKXCEFWXfXrr38AVddYLKf_Pq4JwQq6jpFbhACFjGmJHhbJ4NxQuR2vJ_DK3BRX8F6IDGxUQdoyXhRzaBhsngrow6XMpa4FuvZsF-fkHjvAj-iUdmzcq8svszzUMxQT4uhtcCzFgpN9eZOWtXM6IOB6Ogy4XxHtAn3O5oPzad6xXp-5tbnTKEOoRrqYC7HcfvOMRgzsL3aTqNHvZsOSLZARDEaEExXRoDgUNGN35s2baPCEUfOPCzJX_z0g-lQmh8ecZZVs_dOvWVYWWR9bwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=pPCsFgbKDQKqcrE-9aLTEdUK2Oq34a4ODPjVsiuUDWx8hiwPFbscUoh2NIm0JqVeauQm4oukVQK8Ct6ho25HA6m_Vs55jZ5Df0KCK6y5bjr-G9OU-Eg_Hlpfhs955oSriF5Q1QWRzDNEDbsh4ajPh9ija07jSjNGTJMj9FzZvMIHQST7wj-NTNpvg78bQ5MtI_XZ1yfw7eWTDfwZwi94OmDKJQa0_AwgieyA1sOgAe8IhevkBKGDXbp2iKZ_HNhVJSObEUDqyn-fxIAHxIxstiyEEpr91MFfJOQKn039gWVDfRT9Rt83PkPbN4rZsZKcAX6oU1l286YJ3J-Ziehsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=pPCsFgbKDQKqcrE-9aLTEdUK2Oq34a4ODPjVsiuUDWx8hiwPFbscUoh2NIm0JqVeauQm4oukVQK8Ct6ho25HA6m_Vs55jZ5Df0KCK6y5bjr-G9OU-Eg_Hlpfhs955oSriF5Q1QWRzDNEDbsh4ajPh9ija07jSjNGTJMj9FzZvMIHQST7wj-NTNpvg78bQ5MtI_XZ1yfw7eWTDfwZwi94OmDKJQa0_AwgieyA1sOgAe8IhevkBKGDXbp2iKZ_HNhVJSObEUDqyn-fxIAHxIxstiyEEpr91MFfJOQKn039gWVDfRT9Rt83PkPbN4rZsZKcAX6oU1l286YJ3J-Ziehsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=mGhWRW-jQCKSr81aZ13rLeGqNSP0QVHkq65650ahSH-fhAj_zoKTRyjTqMw3cUGdNPJsufAU9QaZBXTSDHBF3uw_sGZ9icfe-bWYAFdnOnRnTlbEofzM7tpM5l7mbvdaH7IU3HM8STzFgUzK0mlbXekOzsVWp_FJDBi8vxccbvYfCMM8P3ucw9PrCmtL_RL8T3TcZwKS924_0jpuEop962jmOwiRnGLhgxoon7dAqNpLgBJELgNEjWrPBVcIAxjCRwF4c0VUK_-m9c2cRzt1awu69Tj5ERugBYjLAybRV131BIwYE5HgeCMvYmGTEe_D6rJQLk2VKksQCTv8hmBFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=mGhWRW-jQCKSr81aZ13rLeGqNSP0QVHkq65650ahSH-fhAj_zoKTRyjTqMw3cUGdNPJsufAU9QaZBXTSDHBF3uw_sGZ9icfe-bWYAFdnOnRnTlbEofzM7tpM5l7mbvdaH7IU3HM8STzFgUzK0mlbXekOzsVWp_FJDBi8vxccbvYfCMM8P3ucw9PrCmtL_RL8T3TcZwKS924_0jpuEop962jmOwiRnGLhgxoon7dAqNpLgBJELgNEjWrPBVcIAxjCRwF4c0VUK_-m9c2cRzt1awu69Tj5ERugBYjLAybRV131BIwYE5HgeCMvYmGTEe_D6rJQLk2VKksQCTv8hmBFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQkjXTB364Xx2QDRLraocKFY3jDpOhvabPdoLhNJ-0pqv3l5t0QJai89Vy0ezgBWNQEUzdDhHmzkzaxk7PR3_NirN_j7Zkx4gzX3K1rk91qzvGTY9wbCQ5tB3nI5Ni0gi3QX1f-WQICimX8oSaEc84xJjvCCora04WT911Mwgfa3YtXDcbkMT_jexF4aV_C3wum6eVO7bbBdq_qLU0g1Sn-A0CPONhOwkSKzsnQ2oPgv0MIBulw2TjAks9SWjGtOFDV18OxaJe21Kvv0zgOAwfsm5gqOj2p0rCmFp26u2Q2J-cRcR5JLAAZcbAQFWCVapOv2pdtt1rJKzX0hpNpvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHMoMtx1yij-mJb-O750eGXGyF6ZEUyKunIV7xMAQ3lR28bGXLciYJU88cbTybpBJ_cGmDGl2q2mcGrSG4ascDC7AMJUln2ubjd8PESzovmw02-ITdupNhKstzsYm7IKaudXT_t7We62pbMg_2_ADQvoVPuIAz9_h_fiy_VHGGZGRPxTLjHwkddVulqSuiFDQZUZNWLSF4DVLdPgaW678Z2EyqU1jwaD30ke6rqg3qv1B_Cmfq5P6j2iaCSjjssROEFJqlB3RoPfIdg8R5KTASXMLKuQ7nKNCCiRH8krerLSnziI1xZjKm5NCSvNA49w-G-boU5XakIlLT5O711_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1WKL7hhYwrCafDEGoC3HjonwuJhhmaD9J_C5Rz-r9iceBslPVxWKCjjHwlA6CFWJqO5UXsjcGzNchiObtzLVu350OtSHJHeumwaFY7oYzfL5EzJjAnQAJ8XJ-L63O7noto5aikSDC3sQtyGLFBLKfjC6HsPZMlPjoU1NUMY1mSvXOaaRU-NDbzK-nRaa-17ZGRod6EulpMip-VFkLMYA5vspowtQ96XQ5ON0tRxxfhCyoeBEq5e4OGlA3AlqDqgyhrrMrGFwPG-yiqtWnhFFEZmt5WAfyzuD2Rtui6tpZbE0OUxWIjUs4zNJqydXMXwZEX7PJ08BdGIPQ-gSiK2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=ED8UtDrbDDt5erE1MJz550eJ_cLmkp94SFlZfnCMrsxLHeOFwrEiAQB05waobPHo-Npp6osDfScm7ffCyL0VdUxj3C1hKr5AZKMc-lZ8a_W2LDVon7lOTirCQtJi-788e2XVa6ZmFr9PK3dDrRpx5BOLAmfq76_nl-4LN822CwzZVVHtvUP2NqVILPJ7KsF09Plv6VyAdSmQPM3RW6zw4ha2NhPiETgNMovvkZ8oU08A70VpYmviXkzT8xB2c6jIKnoc5HIfRieA-BH2Z6e81CE934ZVv9F44wV4MftjLQn1w2SjYShp0Sl-bbqdvJ8MlLgz1ef3qlVrDu8lF1zfyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=ED8UtDrbDDt5erE1MJz550eJ_cLmkp94SFlZfnCMrsxLHeOFwrEiAQB05waobPHo-Npp6osDfScm7ffCyL0VdUxj3C1hKr5AZKMc-lZ8a_W2LDVon7lOTirCQtJi-788e2XVa6ZmFr9PK3dDrRpx5BOLAmfq76_nl-4LN822CwzZVVHtvUP2NqVILPJ7KsF09Plv6VyAdSmQPM3RW6zw4ha2NhPiETgNMovvkZ8oU08A70VpYmviXkzT8xB2c6jIKnoc5HIfRieA-BH2Z6e81CE934ZVv9F44wV4MftjLQn1w2SjYShp0Sl-bbqdvJ8MlLgz1ef3qlVrDu8lF1zfyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=EiPaP7trcOQCZt1c2MmavA6DZzOzWHI4_uI_Sz9vYN2KrGTDz17_D8PXgmyHH28TcjZ8bD3l_GmocF7FcuzUug2wVsUjsMslzS-5eYkKCfJ-wSEhgvakDWkhQbbKMCq1G_rbvc93_KXAJAts78BezGHIRxeTQtnBi01329_FZ3IciOw-VPwvCwlBvqU0ryWjxqalJEreZtA_bWPqQXgQ5w3YsYAy6ZA255P0bZ-K0prvbUamcJVE173X8rn6wVy-nGtJ-4ios1AvX1ZQ0bOD_ybHsdP0ykyo61sGTMG0YQgxvC3RTpR0jWii6ZaUFwXujnp0Qx-J8ylQfbG0J2ON2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=EiPaP7trcOQCZt1c2MmavA6DZzOzWHI4_uI_Sz9vYN2KrGTDz17_D8PXgmyHH28TcjZ8bD3l_GmocF7FcuzUug2wVsUjsMslzS-5eYkKCfJ-wSEhgvakDWkhQbbKMCq1G_rbvc93_KXAJAts78BezGHIRxeTQtnBi01329_FZ3IciOw-VPwvCwlBvqU0ryWjxqalJEreZtA_bWPqQXgQ5w3YsYAy6ZA255P0bZ-K0prvbUamcJVE173X8rn6wVy-nGtJ-4ios1AvX1ZQ0bOD_ybHsdP0ykyo61sGTMG0YQgxvC3RTpR0jWii6ZaUFwXujnp0Qx-J8ylQfbG0J2ON2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBgkVgHf2XvgSfoYnc8CWBy_5GLaHZG0pijsZTHoF07ZHhWJxbWz5i7dmNfTCx8UTw2zaxonhmRuqrBRabna5jLRewd0ja9Bda-_Ww7fqYeFxSJadBgnNXn9_Uyz0eyReVGskVg8SNLJJ3v9Lwemso4J_n5kKWL-jSVAiHpD0Yqrgisfcn2UrB9-Havs1uciG6Hbs36DYTh4mLJUWTn_FW2Z7v2Fojq1Xm168gBtfeYdQ7-Xv0crHlQjl3x0N5ZBmVfv15sTnMF4NGqiy1ERwko8UzqmZ7xAGugUM7Lnz5e4h5mpaGcIQS7VQcYD8axT30KBvfBjbXjeJm58csTpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuodZ54gXhxJEq3fX6Y1laKsUHJg_ufhQYKUsHOvmSivTxF8vd2-GEGD6hwgw8ay6cC9-bBNjY6a58JsbW696bn3AfVRX-yiZlN54iiHOcu61f8HbbhHXLTKpfNw4mokurmIExxRRXMcqJFqih-RoI3hAGyQ81-PDTYlsH1EXfAmeBO-BAH9M7FZ_aTzSwbuKnN5QgZNmFMRFew6sC93JEA3SQz5BB_ZihTmL8dxbHsTUtv_oTcuEXZ3GRbiag8cEiXL0BrPKVwcpkF_iSklw4IjywH9d_WAtT2bUHatVEMObmV0kbvldJ7P3ksU8QRaMgul5360xhgzXL-1rQXviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjPFfdiVus_robR9KlK95LSvbn5hRunptDKp4b8TGrrouctz-onedL7ne4rNv0S_S5o3kjBOahRs10cMOvwiKDzaeO_it870tVlFBQfaB4jGTnIaLq_lTc-6U70tVZY_khS4nyeSpdsP_94srz6x2f-UyWvXawPtSCNGjNwx1-K2itEyj9fJUdYCk46mvUspI-YdPgmxplOp535YdQt1mvqsuYAklf6Y19jZClWJ9RvdnRSgS--Tl97sQsfv4nVzF4XbQyfh36Gqzf_T4N3gtou0-9RGaEujqSEea4DPfhv1glFyrhZYFoXr6oUQy3NzblKtzX8atwd6kofKlOXm5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7eU02SDgtbckqd6G5n8hi8Tsf6FtKXHk-051RbvDV9d-I-y0y7RVYN7Ptf4IpZCB1bjOqby5xBeX5bOKOB8qJP8GYQCJ0IjJC1pXPmW_tEhP4Qccf8S8ZxZoRH6hamgESabo3wZOUW9_TfsjeHxFXAfixGXUJ_Sb3sAAFdW7TJK50THuOjwQTQJZ6C6QxQdM8qcQBGYFgewwIx1RnfBw9vRTFwsCI3SFMdtUjDn8PoRU3UfaKWkKSMelzSJqZ2tteWoL9J1TBm5kFGqf45f4JdZTzUbDOy-U8OLUVv_JVyHo35zuT8PBa8RsyO4xT3DOpiQ9O4SarmetKf4MGaKFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzN6GASkOoxPsUfuT0MleUyB1Q0PlrZdSOZajEg8u83YYQH4QtbF2lnZxRHN5CMezfuviXQgJymhPQAZ2M8WQ_pilOcaYsnDVVtZCZNAdRgBIAb0cEPeQh76in4JZgS3WG1HHGQtz-YoiKtDJ-7d-YCsR_yeO8JYVUmmypok97aRlLYGijBSu-1ZCxXBS2Ge31qmaTEiUYPSbUa3zLcvRhsb24AfpHHq0EgW2GeWCFE-HPo7iXXYFAMQfj105Prv3ZsYWD1CwadrDKG_QLTM_qXdDLZBrq0lGgX_gXYwvCrNJea_m3a_VN2ZqniD1LH9Z5TDaDDAQ2XOikCmi7kg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fM7-8zrNX3QRtYqbV9nPh0o4xCxW3RSli2GKIg63AllWs_ExirIstq0gfJl8jjT1wJODqOOy_pxKsjHh0f88BwzYubbLMwz04_jVRUylyaAd5IMoYuYdze3uuMl_OgMPh48U1j_iSLryZvgRFPCxy9abLUjgtsaLQrdJDHXvX-Qy4XbY8trkEFb5u9EZTp86J5SgqdNCxPOUDLkrMHR97eO1Hv-HbaG5ayfqSFaAgL2kax5Y39pUT0j9YUbP3h3B2WkVi_GLvvSYj1eRpvkM3Gd-rUMZkizWJiA0BhW0PmcZnKLes_i5bHEjoQM9MRUJOCcaXPQ8Tfm2hN6pAPWwGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=bo-VZYMwYYWDMS5SKyY6HVm5njM1PvRHNyK2Xu3pploKwM_3ZMisrTJ9fj2mfdQBo1jojjUh1JJu55j8r3PpmuKrjLNsNg-x3oDw0sa770siRITeOPc14lo4s9ez4EC09-mGX1EGMLVN68J7b2SHL2x0NarNqCmiS_nTU8vHVTiINTcWxfuPiRURyVRT89ZVcMlM4cilUZaS6SvwxKZuYWZzm56P4FOKuJnN7wuxztzaWZWTZ7zk9Vt-Ly_CCD-ReVEAAPU3rhekoHjelt1ItqnSUoahAvGwzH18qpGbhbRDh2Sq1BpNq70u7TskCsm7eGYRDK-qhbh4SJkFjaj67wSbNv3aYFpEobJ23aU5Z2bMQjSjIJv9aVebLyu_ajzzNtkfng73_ZTT1QgBZRHJWfgTEYEzcPrW1iray8qsV6UIGobWkYSO38kAVFvqUct1OCYJfjN1yxJp1WveyxfUhaY8cf21juKYtjThb2xM1fiKt4UM4YjH5b322dwpOLuXynoSM4SEJs1Cwr38S4pqJcmKw_HEkftoq_QaZKBRGon_1JkMyzXtL6mpEcXUxKLIaFc2jbM0DGzjR7eBzFm0aJYd_nzwGeVLfHe_BrXNjJnJFwoxWP0prN9FPym_q1C219_mLYCsQNS2q9WzwExYNOWL_vVHYIKEImvBBa0sdU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=bo-VZYMwYYWDMS5SKyY6HVm5njM1PvRHNyK2Xu3pploKwM_3ZMisrTJ9fj2mfdQBo1jojjUh1JJu55j8r3PpmuKrjLNsNg-x3oDw0sa770siRITeOPc14lo4s9ez4EC09-mGX1EGMLVN68J7b2SHL2x0NarNqCmiS_nTU8vHVTiINTcWxfuPiRURyVRT89ZVcMlM4cilUZaS6SvwxKZuYWZzm56P4FOKuJnN7wuxztzaWZWTZ7zk9Vt-Ly_CCD-ReVEAAPU3rhekoHjelt1ItqnSUoahAvGwzH18qpGbhbRDh2Sq1BpNq70u7TskCsm7eGYRDK-qhbh4SJkFjaj67wSbNv3aYFpEobJ23aU5Z2bMQjSjIJv9aVebLyu_ajzzNtkfng73_ZTT1QgBZRHJWfgTEYEzcPrW1iray8qsV6UIGobWkYSO38kAVFvqUct1OCYJfjN1yxJp1WveyxfUhaY8cf21juKYtjThb2xM1fiKt4UM4YjH5b322dwpOLuXynoSM4SEJs1Cwr38S4pqJcmKw_HEkftoq_QaZKBRGon_1JkMyzXtL6mpEcXUxKLIaFc2jbM0DGzjR7eBzFm0aJYd_nzwGeVLfHe_BrXNjJnJFwoxWP0prN9FPym_q1C219_mLYCsQNS2q9WzwExYNOWL_vVHYIKEImvBBa0sdU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlbJMxlor0VYGRh_ChBqhmEbOH4uOy8HRGCHXoypK9fAFsC8W2dDI8VI82etVBf46TueVsrWg7BROCNdlKDP99p5zBxVLaSfCqzg45zkTUK_ww2nnIMdFQ-nkM1U8EaVkczGt-BIA5OTcgdwJWTthdaJWi_SdW2x_49VUpVchiDREtAw1zYof2fvmnUYffnWLvlFrffL0OjeCp12y5pEm_-GQvX-fyUBruKcYCWEIeMkfZnHzsN4kB9yIjnAi0Z5mULjiC-x8he4yDQZ3W9CNlzMABm0GZgt9__cQBpX6IPtAhJl9FOjLeV9qYlWc7DZIplWLFcv6jqj3OJO6P1LnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcFeBaf6PRyRKwAeJd6nj1p_D2SUqJuDYdbBQ3pphHs9D3LfcIPtbc5znAfxKuzT-xE4rCPO9DFB96aiqRB4EJVv4ie_Py3M7aLGYpNRRWMYS1OD6BMItHS4I1qG_kx-UIhAqQ3rC7RIe_ZwDTL5DLd4wupqMT6CfLXTCY-9RJwiTQRJQwVLTue_d85TZMHLsIaIH5jpCciYltCLpGo0gHV8ZHms85Cfc_2kfiRRNo-ywfk2KTq6LmLZAROg991GZkuADL-Xv0Coi3dDAFHLYA2XP6U331DSdzOGviS7soZTaYGhB7QJhDun35cHwPMdoI26X4wcWfSues8XpSa6IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=gQElSuWCTm7pJBhSXn8mwhhONsUeavficUW8AN1xWXZlTByNuo-d_X7dqGHczku5_zFvyyiyC14MoN__HCtPc2if--6SvXPAYEVHUEACmk8BhQAgY7npTGXtTkqc76S9UDFj-Bhz3ZAdYrmNg9tiMT5UkZv7xIgH5d_piUb1UALx-LwHVX1KRVVtj1ZA12Y-aQbWM2V97ZyFV9X2C7twC5EPfOyxDt7sVEG0_5U_2oKVSAvIiP8C4j4NtFTL2QdbtJ_cl9d6pgrbXfGqwreO0baExJ82thacRK93qrg4mUHIJrX4DVNBC9UsmhNObVBw_RKZyx9Iz1Ty6Nkndw3LSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=gQElSuWCTm7pJBhSXn8mwhhONsUeavficUW8AN1xWXZlTByNuo-d_X7dqGHczku5_zFvyyiyC14MoN__HCtPc2if--6SvXPAYEVHUEACmk8BhQAgY7npTGXtTkqc76S9UDFj-Bhz3ZAdYrmNg9tiMT5UkZv7xIgH5d_piUb1UALx-LwHVX1KRVVtj1ZA12Y-aQbWM2V97ZyFV9X2C7twC5EPfOyxDt7sVEG0_5U_2oKVSAvIiP8C4j4NtFTL2QdbtJ_cl9d6pgrbXfGqwreO0baExJ82thacRK93qrg4mUHIJrX4DVNBC9UsmhNObVBw_RKZyx9Iz1Ty6Nkndw3LSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qohXO_p7WW1irmjSQ_4n4TubYOyqcYl6FhaBZVu8B0XgvSWbWaoQB9vwR2Z8mBtHaVPrub-cGy8FBpIF1q2qMhSIl9hf7ZMRPkRqWZ4fdvw3L90s_uIkm3siVto9DcDAu_oHHFD8_JMG7IkqkISNT1iJgzsjOw7L2hhGu1Nfs2pYwRSFTd7QVtnsPn8QWH2zd13HjRvbaARzu6qeFhyREdL22yb12fW179JeGH3A6q6LNzysJix521XOiWObxpnKmio9L3v9qLV_YHv_3mII7sTchUSfPOjlBk1Y-qOs_aiYqIADELdS3wLJyzGKVlRNsbt3Er40mpDuw64BZ5b2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBRdvb1fEmKbgaZvaPVsDe-PIkoGfkph0__2lLDT4wK7sxiTsF7PGkzveG5Bxtd3Z_2fNrKgCKSVhiF6oUoaR_ysdS0RpyQu1zQE4P3cgLorXfdXFDWUgoNTPU-TtLnYy8kwf_bRoG-rYeLz4tS7zHTGF3CYztp-mSh2r7bJSgF1hIFQDxenjSHz0OYfQu0wehiylxzT-BDuSf0oMUC4X9ESGu_cnO_lPZi2fJTFkpDp1hVX0V0pLN4de8iWp4SaXCvVvDitFWXEavfBMftzxQ8zQNOtcJKdImJ8czXnOOyL4ba9ZkusXiMu6ijwU0P5rUyYAHA148tMKl3PHkat7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=PRYi5vJV85-Sm94TbmpiVsF2mNjuUdwDQHBXbwk2AeNpwTLUevB5j6toxEx6_QgLMyELg9KsjYOFgtpg-KD2mecAFDqnuDg-pIjHqONNcqL7uVsDcnQPHfFfpJGXRC-OgF_cVhSKCFemauriV243w0D7NDApoa7_oXpEveXXmX_MvSl6UWNzP_lFtXeig1tpPYbkEVfrEvpHua3a7Xw0bGYc6H505-TVQ_fYq9WlIMYuK57X1kZFRn4wEV39RsMF-Le73ivPeyUH98XUODRUNurxgPk-1nXA4wxmmlcOrzB22QP_MuZjpSyOoo-W0iux313zUmczSKbQGeK4K066pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=PRYi5vJV85-Sm94TbmpiVsF2mNjuUdwDQHBXbwk2AeNpwTLUevB5j6toxEx6_QgLMyELg9KsjYOFgtpg-KD2mecAFDqnuDg-pIjHqONNcqL7uVsDcnQPHfFfpJGXRC-OgF_cVhSKCFemauriV243w0D7NDApoa7_oXpEveXXmX_MvSl6UWNzP_lFtXeig1tpPYbkEVfrEvpHua3a7Xw0bGYc6H505-TVQ_fYq9WlIMYuK57X1kZFRn4wEV39RsMF-Le73ivPeyUH98XUODRUNurxgPk-1nXA4wxmmlcOrzB22QP_MuZjpSyOoo-W0iux313zUmczSKbQGeK4K066pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSVP_i9B0W_HlHJ129TsBwrqRyQxtdzYfE6Buf5k1_uBV3O1GrkCsNIlw00IGKRfIut5n-rcy-FSrBjaPr6pMnEwp0gXXNzR3842AP1kiPkzkAQqaWLDtvddV7Vgf2XpThMOxvHdZkSoaCbpbhmYEgGUSY68WDowMyaZ_WGrQBFFYasJ-y7PdPSgQdhZNDhm-mLVnIkw2DlndbNcKZg_lIIqTojmdykvs2j1ijxNEfrf1epUSLrHHASY-qPA3crWVb7UdSrjmauaZcqt9F78LZ3zFV6BgwWhY56MUndiq7zzETWyAX0jDlFT-O6mFbT4CpaD_TkaAITdYaIKjnP2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=PZVxO2YQZ1_aex_aQa_NRMo7Sq_e8Kd6XwfbtpFt9q--Nc7KL1R15hK3613Mamu0XYMuzF-GMnIuHMlm_Sb9JhjTHcjdZqFzrGadrnJVmvNoU0Qc_e3Mx-c5oJQmCgfpPd6O-j5xThcC24yST0hjkjvL6HFqruuk0PKo2Ve9-F0UMxxuo-xh-Uht06QbXzR3YRQeYWLbvq6R4LV4eGwPv0YGd7bvlvdy296rhhJSK6Vuf61CPbV71iU0ocVS5YGxi0FSW_Lf_izwmeSkoNiv_cLOi3264hXZSuTgcDze79EqHeLc6VNhb9McuHzKMGx8Rgh_N96zcR75hUv6asWmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=PZVxO2YQZ1_aex_aQa_NRMo7Sq_e8Kd6XwfbtpFt9q--Nc7KL1R15hK3613Mamu0XYMuzF-GMnIuHMlm_Sb9JhjTHcjdZqFzrGadrnJVmvNoU0Qc_e3Mx-c5oJQmCgfpPd6O-j5xThcC24yST0hjkjvL6HFqruuk0PKo2Ve9-F0UMxxuo-xh-Uht06QbXzR3YRQeYWLbvq6R4LV4eGwPv0YGd7bvlvdy296rhhJSK6Vuf61CPbV71iU0ocVS5YGxi0FSW_Lf_izwmeSkoNiv_cLOi3264hXZSuTgcDze79EqHeLc6VNhb9McuHzKMGx8Rgh_N96zcR75hUv6asWmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29258">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=XY2Bgpwh6q-VRCyR4gZdR3RPfnVc8iyugfJss10pdqPJb0gnKsZk_GBeVgdeppD6R2wIJ14Sygp1ZU2WxN5Qpd-2h6pNzp1heqFjX1F1YAya7kHhpqdHPamJDaI-qdQEys0YoSHbeo9bhNI_7VYYsmBg6tA5ubc6bH-awqiK0QK5Tdgct7qZfffr8auBwJ86rowdljVxu8ixPU4HT1cGod3iLIEXj9-GsrIPkAZPzUg28Mi1iQ6ZqgWM6MOM7dahDGk3kiwUZ4S3ZYRBrUiRFDAMSqeDvk-AUVAcUO-xsf36MjTHOQjQHnMnkT1SL81XuRDltNL2gCoSkuXttGHtyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=XY2Bgpwh6q-VRCyR4gZdR3RPfnVc8iyugfJss10pdqPJb0gnKsZk_GBeVgdeppD6R2wIJ14Sygp1ZU2WxN5Qpd-2h6pNzp1heqFjX1F1YAya7kHhpqdHPamJDaI-qdQEys0YoSHbeo9bhNI_7VYYsmBg6tA5ubc6bH-awqiK0QK5Tdgct7qZfffr8auBwJ86rowdljVxu8ixPU4HT1cGod3iLIEXj9-GsrIPkAZPzUg28Mi1iQ6ZqgWM6MOM7dahDGk3kiwUZ4S3ZYRBrUiRFDAMSqeDvk-AUVAcUO-xsf36MjTHOQjQHnMnkT1SL81XuRDltNL2gCoSkuXttGHtyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ لیست‌بازیکنان پرسپولیس و ذوب آهن برای مسابقه‌امشب؛ بازگشت محمدحسین صادقی به لیست هیجده نفره و غیب ادامه دار دنیل گرا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29258" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=kR9rZ_fgAHYgKHtEt_e2g1PYe6MxZV3Bg2yanTVouMzAs4xvNBgZAmSANUUut6FjfrsmY4DnjiJufH-u3Wmfse-ZtgN5FdOpBS7t9P2AHhLZN9HbwkO0QKQHvgVkYxf8WifVkbis5tyC1ylVNq4mrrt8ZcRiQDwUehs9U53UaelWk_xULg6jIUT8G1DmWYlt9ZeH0n0iwIOlEgPJ7TnSdem9-UiLya3SXjGq7MUjZ9St0dCqwMOrQfs8XQN4BOwJaC7h-x8lukEu8pzlP47qXJiDRGTj-LijP8HZSdood8Q2puQI5CBhvGkwHeqWPxzv63aLEkcDdkHLvQ12tAXHPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=kR9rZ_fgAHYgKHtEt_e2g1PYe6MxZV3Bg2yanTVouMzAs4xvNBgZAmSANUUut6FjfrsmY4DnjiJufH-u3Wmfse-ZtgN5FdOpBS7t9P2AHhLZN9HbwkO0QKQHvgVkYxf8WifVkbis5tyC1ylVNq4mrrt8ZcRiQDwUehs9U53UaelWk_xULg6jIUT8G1DmWYlt9ZeH0n0iwIOlEgPJ7TnSdem9-UiLya3SXjGq7MUjZ9St0dCqwMOrQfs8XQN4BOwJaC7h-x8lukEu8pzlP47qXJiDRGTj-LijP8HZSdood8Q2puQI5CBhvGkwHeqWPxzv63aLEkcDdkHLvQ12tAXHPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3fc5egLOKfKri6qvz0dmlP41oM8eNaE3cW9rU3olDl3XSbUob8rh1Jfy4runRFHdqqowdqHEiAWvAUf5pSiRnZinTbll0bhdycmx5-2EX3q5ui9CpQB9Kwfk1E0nSkP26sFn20EQ8xpm3neai7Xu3DgFTqYacqbP6DMKI3JjvwxKVNIDmlikckDY_cLPRPuZcKlc-kw4x265F6ooH3CH2YZxTQZ_l9CThS1X0barv3UAXc5DM1l5hk6XGw-WDtpxFj_sH8ok_2FQyddWJiJcI2z34t4Z4yD6HYUCMVZaTcxaAy8MtDGgqgxnSWqjyB_2i0kqMENs06_GfWQMUJkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=vp-7cCvI704ETp933MbNIEVe9M5QfTfym8q0O5Bypk2QENtIvPuAgopma-R-rEAvMUX-6W3n-v_-g-oxUEpegWYlKyQ1y-tiUmZFxvUVmWR71oUljhe6n02pvq2m4jzT4zBb5Zr8wu2SUOvwVl_sQG82xkIdLa7kMMFlbzNNEuFSzc6ZCRLhdffqTZrOsEKS_MB4cdzuCxVcK6ORC5B-bCkIl-wejyJ-_JjZYALHBXWxtpTUc8nMK7rSvPmzPbQ2VDw94GzRn6WEeU5-hr3MRB1g8AZgT5QjKc4z-6M3g-PNcvQYQ5kUBTnyMhLrmZ0XnGqgAwnFSkrcycp1RKJFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=Ana-AAM4-xw3KJcJLzxCHebmMD1BpDcuyV9nRtoqXi07lDpbx5GNm_jnR7FfJv1-bOwhSu3iTXypl-V_hAo-t72VOPkRiaP6Wwz8yIlz_ImwyN66WVZrdRfW-LFCUD5_HgtMxQd0oxj5HU87uSMcimyx7Na5Yum2I_co92JXe-RESc1NRIMAsbd7880aTmH1pT0dLEOuDhTkpcj83qFTrHOCD1ubG6z4EVEx7j5F9Ikp_f840GlmcQVqHO84C-TYl6uZEMQ4IIVcjpzs7JhrFfZQvqSBlDQUt5qRwzU0J0zeI-vS7SPB_p-tUvhKtZJoMd9CW8BTNKN2NQx8SflHqEZesSopHVQSPrPOorg1f45PoqVKXbfaeoQefDaUg9JoBDQhtQePf9us17madQP4U5mIe83LZo_5EzvzbcDvha9AQDnbvPkxH4YKgU2nF0sW1ouIbs3ncaBiQhp-_9qYeP9upiUPIT2zZrh9_IwtGFKOmZE_gCY_HEGRSOvqCg8r4RCmET5slrLdyrqJ6CaqsZCc_9QzRDkePewI7Aupcg0KAXFSlGaJ-qpp09_y6_GB6K4PiysqEdrTQ6ptiw4h3m0N0bs4m_Y_7V8Cq1uc11AD_7V4Eisp8RTlXMSxY7lTvTziuWXN--el8jgy5yLq6uDdV8WBDCNS2XJtApbgu3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=Ana-AAM4-xw3KJcJLzxCHebmMD1BpDcuyV9nRtoqXi07lDpbx5GNm_jnR7FfJv1-bOwhSu3iTXypl-V_hAo-t72VOPkRiaP6Wwz8yIlz_ImwyN66WVZrdRfW-LFCUD5_HgtMxQd0oxj5HU87uSMcimyx7Na5Yum2I_co92JXe-RESc1NRIMAsbd7880aTmH1pT0dLEOuDhTkpcj83qFTrHOCD1ubG6z4EVEx7j5F9Ikp_f840GlmcQVqHO84C-TYl6uZEMQ4IIVcjpzs7JhrFfZQvqSBlDQUt5qRwzU0J0zeI-vS7SPB_p-tUvhKtZJoMd9CW8BTNKN2NQx8SflHqEZesSopHVQSPrPOorg1f45PoqVKXbfaeoQefDaUg9JoBDQhtQePf9us17madQP4U5mIe83LZo_5EzvzbcDvha9AQDnbvPkxH4YKgU2nF0sW1ouIbs3ncaBiQhp-_9qYeP9upiUPIT2zZrh9_IwtGFKOmZE_gCY_HEGRSOvqCg8r4RCmET5slrLdyrqJ6CaqsZCc_9QzRDkePewI7Aupcg0KAXFSlGaJ-qpp09_y6_GB6K4PiysqEdrTQ6ptiw4h3m0N0bs4m_Y_7V8Cq1uc11AD_7V4Eisp8RTlXMSxY7lTvTziuWXN--el8jgy5yLq6uDdV8WBDCNS2XJtApbgu3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8S88B8frreMUYoU-qg0avxDkxITMjySPnisK8nIkG7WjYF4JsN4C_I4zomA7kfFJyZyZoQHJ3Ik8qO9n_ZKTtLmRNy-mv8TVAXKUM6xoD6rhGuIZy5ETm3qQ5Ei_pjv6adNlzjgmrMg8QiPtB81_qsBbmvZLjFVjYSIXZBfNKgOigPHpC2TRRJLzF9MlFTMLci7SXuxd2g-e_-Sf6nTaJckNoXs9MvSlv8HcD3ZZ8PvE_JbpcPi6CMg3nWgYnAiJeiGKR5BMJah2Fv0i7fXuB8pppUDOIwzwH-pSDrF8G_B4c_X0qfhX5D1pFbioFe-cSwalqc2FigbHjMHdXiUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
اودینزه
🆚
لاتزیو
🇮🇹
⏰
ساعت ۲۲:۱۵
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
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29252" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2v9BT1Gakdbg9XKq_6rdz00C4urCH1bVbmRlwzDdW7NkGj7RyJFudwEzJ0GOkJQpUQ7TuRUOYlixWOj5FlibdFdU49i-fXGsiyb93lw7b5TsKDSVJ_Le_rZV36ci1zPfwIfnX35mGOe-iB0sPoVcO5gddDrURHnCP8rvRXgrhCFtTs-eedaUx5BYo9O5XzDBs6PoiZlLRpBd4Xoa7yJx6bT5maR7psJrTYO-haAA4fugojsqZb_yoLN8--MyKoQBI5nf6EZ48VaSpLLum92ht-tzXnr2vAKfXF_RdjB7KvRU9pJpl4SrjvOqEhj8erAR6mixZm-tRaAxhxqmyvzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2t-v0NaqIf3SKTyCPQtvqeuMoK9opEhPu3czwfLotdjk970GJ-M-EcL-RKk8dtrPnO_S2qkIwtaLT80coIC9V7GiEDlYUbBqRiy5pmdX7lG_GcEVGlHq2-wXsnE5as_CgzOTkiILvXDaRwjit7d0n7uyheShPjCAr0mx46B5B6SiKc_2IH2MI4mvFiXMMdvxnNWCp1lvPco_3tqk02XtC4QoQMgnQr1ULbKxP2giIjJih6VwI1L76etvbWH7ISiNvQjPWSyoLeejBIaMdYO7mbAEkgO0d_tyy_q6m8ryYTdOqk8iH7Scoalf1J3GUKGRsvT08H43_QcHzP3IfjRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AouSs_yRPFP9cZOBHf1fc1wU2rnGX1FCLiqfl6OX3R8yq3VE2pHGDOSmh1Q5b15pRJXm-91ekXNofaaBJQ-OCVXGwJySJhv3iidFi7wXmsGGncjq-YBkHgnMLANsyoGm8obWB__5micht3FCztOuHlF5qynF440gcuG8ImKcVl939e3sFt3J5bs-AAQOEk6otqHu15UYAHuN1tmO6exu78EmfkiCeMhRap_ND9k4DMOdUysnbL8d9rpOev82LFVH9YyKu4acsqYi-Tynoh1qZ9FSTvz28QlI6D047B6jl-ot5i8AnP7vl4LDMipFQe42eGskUaIo6W4nPPdevscewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuGkYHl8dJh_-oM3xOvIuvIvvjnb6NOfV24cbk7fBkOz_gRWYC4KQp3JEHnph3Bh2aGVtjtc8kP_i_owAzqKZFJJBoPk-ENaMPW_qLku8T3UZDCJsVUUj21BlWuXVsc3ON3IkYh6mCgbAl_9DhFjBMU-G8VpCKIvETjrzkH-xGbytFrdED0KAPB_bNblpQWpS6wYSamMNhjVfthcR-j1VQZbodP_Ruvkbtlam8rhvKvpSgYgVJVzzS9A8kCNOm7HdKiHQ_YQLTmI_BiLMrOr7_TBVaonZgoTgvn0sRv4TUVzRLnbIvidncHsu18mJzxRJIwt1Ia3m33doKPw0u-Zuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=SAGRZhoYdm2jA3vDcHcXveRDEakPwl3hbylIbCrcknJ7z8LKEWEKqBImtz_1HH1mtSNvU653LZ9yZGgjTFjnDWVPjQZEB07iPrLMdN1XmJkyRBYtHoTUUjAf5gBHpKsGwfVNA6Wzu0pgCoaZ7x81Tj1OqSRP2qpydmq7kB4YTIqnhqIILC1v_X6IKNi8C9NoKrLWXAlqdTZSEmC9oQYsh2q3SPwdZlyq5adwFaM9QxqZKfXTh3Fgt29MLkgc2EbXrVkvI0YkMJlQRnedPiJ5NnEkxVVQAzAohE5xcqxmql2jadvsJdE4dMgnLOpHuHeWNiK0_JsbaDq-jAS-_W43SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=SAGRZhoYdm2jA3vDcHcXveRDEakPwl3hbylIbCrcknJ7z8LKEWEKqBImtz_1HH1mtSNvU653LZ9yZGgjTFjnDWVPjQZEB07iPrLMdN1XmJkyRBYtHoTUUjAf5gBHpKsGwfVNA6Wzu0pgCoaZ7x81Tj1OqSRP2qpydmq7kB4YTIqnhqIILC1v_X6IKNi8C9NoKrLWXAlqdTZSEmC9oQYsh2q3SPwdZlyq5adwFaM9QxqZKfXTh3Fgt29MLkgc2EbXrVkvI0YkMJlQRnedPiJ5NnEkxVVQAzAohE5xcqxmql2jadvsJdE4dMgnLOpHuHeWNiK0_JsbaDq-jAS-_W43SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFRGl1kwvy8kspW149UpwFGpJDEnerF6nT-eKgDrL2BgCwE8ltgKlEliOMCEZrA9uExDuxSpANVJia6APf7wDfizgwZEEdwZagqU9H6n__G30V3zchDJz3LyMib3XRozdms4ASHEAwiePBiaWJyKiX-RkF9KHqFbKZU1BCc-SN0LCY_sHnmz5uR5hLcyzPMxL_7sEBG-bvPWgv3GNiHFuZn1Ma28Jojk9E5yrgCmL9SRyoW0PfIKFcoZwEBclG8BKPccpZsKNhjSaIx_29r4teYgwYpXvXJCtqLyL2ZupFm4p-2hSOigf8l3oZEMLu2yQZA6F-XEM_NpCCJ-LMjrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=InzmYvz36QuGfdJBm746z76hULChSd48b2DmEL532O6m0oybl_ZdG45cX4nEi2oX9WtvJW-J5EWLkVBKDL6w3d43lNk8wAkuu2DqDOE-877nxSgAQVZ6fQYGi5fBumpm-FSjQTXQxCh76Fv_mLsezQkfut8nuqwQNV9lvf8EBLbzIRWedbePnSfQ-8A-IVyty09yKqfNOO0UW8PfBAu_Q2r2FINlzP3D3nUCIDaKw7wpMIvVBcO6mktfWfSzFw7J_KpvDq6U-gvXYkqWwBGEmRgVQ6PInTQHY9ko83Ywaw7C5kVjBxd8Hp9SANrey5wGXiwZOvQyMkGBpsCm-eLy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=InzmYvz36QuGfdJBm746z76hULChSd48b2DmEL532O6m0oybl_ZdG45cX4nEi2oX9WtvJW-J5EWLkVBKDL6w3d43lNk8wAkuu2DqDOE-877nxSgAQVZ6fQYGi5fBumpm-FSjQTXQxCh76Fv_mLsezQkfut8nuqwQNV9lvf8EBLbzIRWedbePnSfQ-8A-IVyty09yKqfNOO0UW8PfBAu_Q2r2FINlzP3D3nUCIDaKw7wpMIvVBcO6mktfWfSzFw7J_KpvDq6U-gvXYkqWwBGEmRgVQ6PInTQHY9ko83Ywaw7C5kVjBxd8Hp9SANrey5wGXiwZOvQyMkGBpsCm-eLy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqcSUNvtObRTnT1oxXVO4JUvlufU27l4bGoRWpdQ19wQ1Y04n_Un14F6Vuv8Zbj2LXI-4INDZABKbuEPt3V6IsL5TW5CVxLOOOURfOSATN-obkn00gGfq_ttnTPttBEdGDNYRGmti9ooOrd38YgoDHR2GG-P1Q-rQLlnsgts9NRncir8_OUNpD2ivIFGQkMTuEQiQs_NLRUruTwO4asIWSlsfm6WhXDvKiNv90VN9g766p1WG67vj6dABlldhdLb6-kUXXJCb52936fiQL0rQS-XKeKPWrNRPp4SrshkhL0V6mobdLeaatXV9UwA_MiFdDeE5hsTaSouxk8wCx3uTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ7Ev_rpKs7Ai6e9cy2mcz12pKA-vmFpsS1AnvMZe2OJyBcxUcqSzvVWrR47CvcWSeZkq48Ln1orej8LY6Gf_5jNMwgfhgNn06vfk96__S_Oht3GtGpFD-rIe--DjytoUx2urx8v98-SjMW8dQVJCAd6c6Co3TL88ceo01jiAlGl67sf92aVeKLeU8TxpnRvZ6zmo_ZSWKKJjieGPEeYoRbVyAI4opc2Fpbec57KnaESU4xS25iCOVA78syexCQ9yT_tyNOnNBj4MeIEsX7g6gQfvaw7dA0DexpJATG77mqDfHfR4VVE6hRi7uX06aIN6YwdSqG-Iv0Mqtr0pQniZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMwLTk8le80D1mXLDHkW_LQw_CPVIRAM3ckmC4PdJ8Avaxx6fkBP2tCQ4gSGa_VJB_I-d1Z4dEYLBUmOTPb30EGDVkGURcVv2gGALbsgTXBthgLxYcrzkbbssgbWk3EbjiMbc9CrZIUw_TExMa7oBlcDJQNQzxeFk2SR8ZaScXIg23NHWMj5ndr_ciuinm5B8CsNnR0MbeDSmiFgQ7-k_7S4II-gc1fuCWLdSuPkJ0ezkhkzfIoha4eyMkCAYV4BAx9cD9DFviJpEK5p6aZiLWo2CS_XrsET2kk2OBGHMRgdTlkTd3gMw1NeFMbSHvBBwEscnf4EPNgQxui57SCyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=psCkIW7zgUn3FAfTi143eef1yijUnRHlvmcIMW6zuHOZGCyHJCP7UmXXyGpzvMxNEtYT3gFQiktc3n5nLuPBAZeG-vKurx1tpOFXLofdVmvTKJd5jsg-h7-Fwy8WesIwFAY6pSvnSNbGQbt-u-5dBWUBgMHDZ8ryNZfKNuUjU29ElHZjGqqTXYRJpcgqr-D5IJpffptFW_UnQ4wJhsAcsZ_rCD51ujfLV0gMvD7ldNE2Dk1erz-wGNUtIWeZIOquQOeXUAZY2qsj9gMAZvpVEzoQaKERFmlG254vEnCKYy6WgktlARVuqUDb4AfOFe_74c4KTnMZWCIzSHSn86p2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=psCkIW7zgUn3FAfTi143eef1yijUnRHlvmcIMW6zuHOZGCyHJCP7UmXXyGpzvMxNEtYT3gFQiktc3n5nLuPBAZeG-vKurx1tpOFXLofdVmvTKJd5jsg-h7-Fwy8WesIwFAY6pSvnSNbGQbt-u-5dBWUBgMHDZ8ryNZfKNuUjU29ElHZjGqqTXYRJpcgqr-D5IJpffptFW_UnQ4wJhsAcsZ_rCD51ujfLV0gMvD7ldNE2Dk1erz-wGNUtIWeZIOquQOeXUAZY2qsj9gMAZvpVEzoQaKERFmlG254vEnCKYy6WgktlARVuqUDb4AfOFe_74c4KTnMZWCIzSHSn86p2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNA0hKm98XOjkEPmL2yezeWD7KfEwjPsSKMDyITYACfzdVmUGJNrReIfTW38j31wuYCQO-WnnhwqtwbEWKO6pauebQwEQGL3DY-8Mb8xpeIV9-jvqNFUKeWuIEI2unVBeGg1ZbV9AbGE2beL41mi8ntvsrJJsrKF0BenUlarQBqg89f-lmExvl6ZhhjIBa3IZIo8C4cB0CaNi_4ecK9DSWwCPVetdrmawc1SRfzH0MWer41qAnHszOVIxSM0YMq6xdq2zvHH-J3vZxvJmx_FmuEf9Uis7d5PiH5LEUhZwGnnzNPwyWa-RLnS8jGUKOhYRUvsOgzTQljJTCcBSvQBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbZ9Vc0R2sDwoMZMTpbYrlR6jtDF9vwbQm8n6H2xepZf2kM68Ju-fnPm8twBR3CGrpF8bKs_Lspg9rvuhfFxJQoDn0cdvXhvLIPl9YCH5c92Goo8o6KjaiKVVZTG5hZyuNktVk1dCuwaHmZ3yUHXn6NdY21j4g51-bgXhDZMYh_qQ7wSUlpVQhx81L1PUi3PndjUMViBoAnx1B-_827cyyCn2GOCNN3wr1ggF98cLSG7ltouDyX6tc13yEGi7VIs8N89RQoHoikyOkjAIEDzXLLqfp5WrGwywikZ-yRWPcwIoIKaWNUTnAu5-8KYPiNBNECqBr5fL26d5MT-h3-FAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEpL_iXzGbSbghExOkKK80cQ279raCF_bVuqzE2tmUqF-HjDf05eZh727vYiZ6nNbidk8KmXGFderbDC8oBpMDfqDJzOFLbhbJG9bTfR_lLZ59sGh5GOcwRm1NTEuE8S0q-dK76FTapmKo1Pkl1aAEngi4F8_2EcM9X5nz0BnOWQ5xapcXM7LT7rEdBZMdTQiHFhmEIEsIiSot3qFx_7w-Iene45DVrmgxGmKcsgo2mWHh0mA1lJsKt4DKMxx93dPH5DwnUqc4ocktrOqrnn7eli8qaewuMFxy2Yn3lgpcHsSQJTH0tOguiFJ4IuT9b18GCwypjiEPqh9J1bNSBaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریهTYC اسپورت خبرگزاری معتبر آرژانتین: لیونل مسی و رونالدو به‌مسابقه خداحافظی کارلوس توز دعوت‌شدند و ممکنه باهم‌همتیمی بشن! فکر کنم این‌آرزوی تمام هوادارای فوتبال جهانه که یک بار هم شده دوتا گوت تاریخ فوتبال رو تو یه تیم ببینیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29238" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPXJ6FJ_Pwc1lKvw5RU2RyRcXwWNdsmiVeGppgYINP_EkfsKwkiO8mXMj6e613PyXWUTSBUDGFHF9GqTUFvhGqugT3sp9RFW9ARsGtrccPdM7ALHyZLBXYRa8eql9jU82lJ6bDI5XJE-Zf_L7QaxAEFR_mFWsUFaVd5Vh5IB7epzWQVwNseStSldyD-gRH3f6J2kmxtldHIS5ov2mxY195KXg8eBV23JgO_W8cKkZwNO5RVcZNDKG2tY3Eu0Wsj1Qi9HQscCf8A-knbRnOJrSy9Iq6lpAnKP9S6cVuyRs7i6ZYf-hEYUpe7BMEKxPB2D8Uqqzd5npEnQ1ptHhVYIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29237" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOZiKJnovxWfeqhV8WMUPUW3y6hvF4ov5_fpX-vBsoqkcJe1d95w9AbLTmJLCg5c3sLoByAIvBXzYW7z7RO6VGXk3_-Rc8DiPcmdmTVfri-cV4k1CdRLkwtbJkM1wRU-WEkTDrn6CqqpE5OfHZnT_ikbS6igwIwdlohmD4H1awm28HgFHpw7DiHpwBuZB5P9OZebB-3oywxH2fCHhdWCBzOFmfVrQsPXWNUQE7NmXojblxvYBaOOBubXV-nPn9ekJ8J8ZtDdzgpOcA87KVn3JTtw_RwTS3NxICdr45GxKOUVGP0ihLuRGi0kta0FH5qqhT2elZBG1ENrp6pk76NNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9pyghAAua51L6kNYpyYbrdwjr9YrZP2PobaaIqfy9gkMeNg5MhU2TDdrrEGUtkthn89CcBUcMxEveSSFaClC2v_z5T8700gTqEt1fDZUGAmVML1EVYXvd0ETZ-6tIY94FhmJuo_XJ-DFqYQi4JJZppMh7yrL0ismjaAkPrrF32ggaPR_QV_KW3S3O9CkPqzDxMUlRid_eRJ1_bbs20MwmOiz9wih6hxRigi24B6leCZTFpUPLO7ka--05QzPKP4FJVLdmzsQ5ou3xttch6HtG3AfJi2LUc5bIYEJFMJ007ijsifFpOBDnnH8eBqAidiaw2Wpl8TP-yIEFycyy_wZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baLFNVWXVEClCty2zMLH3JBH6W11ONFHI4Cf1MlPB2sk9-gHx-ACv0RarvoAntW559lesOERFB041MKuG06fVu_HsQMDyBWzI9YI2oOKI6qVVqxcRExPi27izq7y5vQ0dqV0xP0V6Rg7Noe-yy6g4nJr4O9Un9SPq2mJaJWjsBFbgsgNDRXzN6I5MUcXo8uv2sfDc_bGPpjWLrxNSuAP1KWo_08ZHYmGZ4gPd0jYExhZ4YXbpvUI0eLon8NTZBp1gjAl_PQj0Bu1mMA7v9cGKqcHIuYzwo5zkRJjmEUlKV_ERAtk0B4K8G5iys3lKdsIaki8Jx7KN-0VmLN3kgAC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTIrAFZbTe92QM2j3wqTpzY7DUUzjnDqa8z3EDweyYxrxKF9wy91qHZb-QukLlnZa7983zBUstzA_x0B0D_SY_G-_YjlxBE1-PQTxpi5jw6X98FkpqDZvJ-dFlIYH-r0hUyEOAeMBnHYlwgIc2a6aftj4S4pt_aVLFbymnAW2iY0DfBqX7zbavo1Sy89q96SH41UDyNxaLUAilO3VItEz05xhp34uI3phsqHNGVC9-megW0cWY6BS_GTDsuIS7yo2ZLCbU-Q_Di26J2YkihUgPYxkIGdpVSmGRpueEKBnOsPC8aT4IIz1PkG51_Q3B1Dky0rM4fYT9fwq2p5Jdji43b8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTIrAFZbTe92QM2j3wqTpzY7DUUzjnDqa8z3EDweyYxrxKF9wy91qHZb-QukLlnZa7983zBUstzA_x0B0D_SY_G-_YjlxBE1-PQTxpi5jw6X98FkpqDZvJ-dFlIYH-r0hUyEOAeMBnHYlwgIc2a6aftj4S4pt_aVLFbymnAW2iY0DfBqX7zbavo1Sy89q96SH41UDyNxaLUAilO3VItEz05xhp34uI3phsqHNGVC9-megW0cWY6BS_GTDsuIS7yo2ZLCbU-Q_Di26J2YkihUgPYxkIGdpVSmGRpueEKBnOsPC8aT4IIz1PkG51_Q3B1Dky0rM4fYT9fwq2p5Jdji43b8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuVL2kRK4GHQtRQOVoT7xkT7FhmdOY4ML9E4s8e9AkAyJ9nYq531fuQAVdbFoUMMBNRNznzrvuLkFbAhLYwi2MRCXbGci5WtO3TrWpxjqBxq7rF3Q58PF2FOxYJjgeyC16O7lIBVsuFiDyCmLOnRTVhOb2YrgT1LeZbj9gIuJ2yhN2M-1xa1SLr8im0m51Il5uCEWxqnkY-TPEkgQuL4E_s7DsKZn18-JFcXWAirtdvUulUMPqxbnH7s0vz0jm93hOpalFkRyK4mATygbH38qCJ3mf4Gjf5vg5GpmR64QBT1VKdcpNHyn12WpoSQBm0KOXZq1ilvGPviu-0Vb3w1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
پرسپولیس
🆚
ذوب آهن
🟢
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
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29232" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lz237cZ71VlmxpnDVN8l6DPKAbBcABI1pusI6ME0_hVxPwGMzyw8jlq9l_qqW0C8BACnnuPCgOpsrDarvJJB3bhoKkIFJZ4k2crRXHOO-0kB9kTvQEQDgie4rpM0U19uPZSxZqFJZn8LPG6rQWvp7YYGCBJwseFaY-TOpdn24CKhUXapo8DtKxM5_UH9hOm6o62pJ_AU3BDukNQ4Dh6dWZJ9iTM7xCBtIq72Hd2XuTB2sk2hv1Pb9276lJ3Lon_XnFVqc9thi7RdWPa6u6yz-5whZDGFzUqIxC46ImZZHT7aYoF-S-ycCjMk0Nt1ddNP0Z-OXYZlY9GCsqWQXzZqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlXV0PU9Ln9h3QlIUrm2KN3EdBURIUuNoiZ1NnphNIJsOIYQ4fFez2ZoM7_GdgGyVwgKsQntqtQpSKcs5z0v79GTSRvbhSAebNFvSifUBGIDxf5eC1Zy_GEJipDbup9P41Jn6ITR4r8PF0Zkz-RGtNei11xs4CPIaF7kHGSAfYs5TyOknDSPdBaCsVG1R7tU3fLGkDzUtsByv_UPXm-yUCMK2F9hIloEwPP3kSaaOKbvEReIDSSbDRds55RDNHI63FzWdc_O7Lym95pE0VDLG9OM4_H9w8hH7nYYi60IUqcxBMGvRp39UzB6iIXN3rGri9Y0tbHXSkN4rl78Hv6y4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpi2E_4-eZD70qTo-zGpslLA6oV1TM2c4n7wlJDlfGM4Op5OOkea1ngHvutt-erQZG57ECKAzlE1iWRyWmsrZgq4jriQZRgh1j3yS8wjWgUcwrmpPcw5K0Pxd_Oo1nyDOXFopHMR-rJMJlBBpWeuinSjSwF4lwD4S_vfgNrobrDLTTSCr0DwO7vuTuJtBQSU8uzMVj8GuyhAbcFdaXS5G4e776B9IeHAKZuE2EenbB7mXXGnHzluqVQLH_C2HMs3fvG_hkp00WJE9xfz5exkKqZgRBFyjhw4fU9x19K-3U0NLpqFg2O-0tFzzoRCrjaUgI5a_UzC2mb-W8Y9GN1Luw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29229" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLD2c8hKvYA15XwaD1n1vzfbQ8YdD-meoQ_D4f-PleRap1t7Hb5Riac52bH2AvJ_pvlibGDAUt_IvYOCxqbonj4Fuh8SX2zQt2mGIGj7mMboYQPw7T47k7eNzeOX-DgiJDKxq97raL1_QNU8Gq4ML6BZF6_9YnJV9BTTaqc9uJbYZG1RoF87rHf19jSvUs18WxTFFwBmR_izwD_2bl6vvElX8BXNROUsPrclF5MrakA-ahNMUCR16nHd70jvTwav9mI8S05W7ndU1o0tF-S1ef4yU8SVTAruHnh18Mj4nyIx51kquX7JhyyL9OfzTo8oce3R9wz3W1Ge6bVzFcX9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
آخرین برد ذوب‌آهن‌مقابل‌پرسپولیس به هفته ۲۸ لیگ ۱۹ برمی‌گردد و این تیم در ۱۹ بازی قبلی خود با سرخپوشان تنها ۲ بار پیروز شده. از آخرین پیروزی عبدالله ویسی برابر پرسپولیس هم ۱۱ سال می‌گذرد و این سرمربی با ۱۱شکست‌مقابل‌پرسپولیس در لیگ برتر از هیچ تیمی به این…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29228" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29226" target="_blank">📅 11:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eti8DWGnLu_18H1_ef2h8o4O_efMuD2YvoUs766cniHoejiX5_lq0aZde9JD0f-Or--a_xh8tsg01jh4FrIACOJ-oMjVK4sd4YRZsYoEaFYGYDFDUnJ8_QStKYjtLsP4JqnF3-yQBhLrnW5cI_2QfSkmYV10ZuLgmsmDkIUlH5CaAY8-qlypDPHLWxlwutgUZ7q6m6_dl0j-HK4lf-9jbHv17OGpo6-AjOnLHIuDsmZMgKqBmz0gBA3A1WCkqrPM8joWosQUV0pZA0OtNuh_0NSFm9TZbeO7qG963nGEoPihrmv3xiGi6VVgF0lVWQlYG-VYl3ymclgidBP00QK3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خب‌رسمی‌شد؛ ازساعت 12 فرداشب به بعد بنزین لیتری 10 هزار تومان به مردم فروخته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29225" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owlgYzlEHDgUeQRNVIqT4_hSwxOsIKMfNzIPoDLLcBUGayTpI42gGoQqcyLvxiM-jyCOIfUzlcvgvS7n-fMfQ9wubAVQTT71OIDEGDRFmYF0PEwBDeH1nv6j6m8K7RDKwcjHJL5Xh1pMd34CMXyJalhCg44MLQZ-E5_rSvHkyNocNNfVgmNr9kEAsbeaZrDdLXLyRIhva5DeYUayOooTTNa7X90fxi_f6nYx-iXolN7kc6t-LRn685oX_XXeftyUbiWHxMRw_clJ8qr97IL0YZztbPcwelfFMSW3IKROCPNGrtw3r4khfnhHGN0xGmlcJIifvoidiLVBLbNefrUzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌بازیکنان‌حال‌حاضر فوتبال جهان بر اساس جدیدترین‌آپدیت سایت ترانسفر مارکت. لامین یامال و ارلینگ هالند همچنان با ارزشمندترینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29224" target="_blank">📅 11:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzD-pVwn03v7-z22W76y2c_4YsFwnRzHHEbpcyZ32oL6IdtcZKryJ57ndL0cOUjh7mufgZ5bOOUibjmVipUthPeOheu-xL3G-rQwGjF4OE5fbtlVfrbEHaHYPN1ldK0PTM-f9DyajRg23T9mCwxnVhtERHn3JXpBJ5I76DjTqqfpKUC0Ea7lsUisRlQ-0Vo-1D-gMi3XrNSQ8GqoFCvc44hiVgyeGqPugP4KgcRbVo9IDuAvogNwCcE-3G3E73ydYjilNoYrlvuEWnzHVrPnKiH0Vims9VczmXNMAWcg496j8FyvtgySq5KxHcvuMzeq7VLbtNylulpgX3GGMb9RwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اردوی تیم‌ملی امید به دلیل کمبود بازیکن لغو شد و شهرآبادی، لطیفی‌فر و ایری سه بازیکن پرسپولیس، محبی بازیکن خیبر و صحرایی بازیکن گل گهر که تنها نفرات حاضر در اردو بودند به تیم‌های خود بازگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29223" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWN05OQIE4j5OlSDOgW-BsBmWPv4rcBrQeQ16HoFf2ZnXRchrzrTZUWurRkqpk2z_YbJ2atTJArbXYGSlxhhLx9wPNwrNHw8DuLbAEJw2awMe7zjfBTz4A6Mq9YTkvhraOhAutrwfyIBicW9D-19gtwpN9CY3NVjmV8Yq9vacbiIojzNnC5n119oClVKZo1hQOZyNga-3VCrJodKImFJf8-hhLHAD-pmfQBSPSJgomM4NnthmdXL_0g3L3WEOuKOTHkPbGVJ7-Ox8rRy12cH2xDRw6Adz97ufMfGJsa661qUo1DTS2EIZTTaObcDkdL9fOWxClsLr9d1Qsie8XzohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29222" target="_blank">📅 10:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNLFsIlBotq0_vHLdT1Km0A9NZiRAac8tdsHqYmii8G-K-KpIUcWAk6AyENPm-hF7sxp5Hw8h7ZVDe-AbXw7YoHJW5AZcqkxNrZATQGL5Wahh_JTNUYGO45TSJtYx1QbALJpgN0-90oJCzWAmPlAI2SbkHCoHREdhzdpdIEFbCTNPKaxK57VGgMUzRF-nFDAJpbIlTpubfw5CE5oRaGJsgoP_2HjHG8L6TiNwYakgkP2sjebQ-1Q1uqCfjQmbfMRiXqETNwiuYgWprAMfMgpYN7PpnMXwcDmPIeJzHaJ01pMPU-xhx4W7riuxngdihycyIHybPKlbaDxkBZRF2laCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRDwgjb7P6d-vAjKefTjs5ebin5E8pWEvABLyjLkRU-t53jrYGMFCsac_hI77NGjK23WnSuOM6xLxvwxADIdZ_VfL2vGzMV7P26qUFgNGYXX74KbxQb4opM35v_b8BIg6OAMFDsoBrwhYy3kQovnIrVOFGEsm_PO0-Vdprn8b2UsNvTrGao9B81cTOglu1m0TabiixcbTRDb-CNiwmVoKdiLtDA9jmvS45uHrLby9iJBJOp1iJb-ctQ3PXtswyp9NFx7V7Bg2e60Xfm3UySvG_-PfUixQxapnUac0lLryqDuhH9hXydu6pDJX6DfkhJWwV0_dbhxoRlVQEQpEKw04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGTAoizM9MAPxLAxrDL_XcDMop4q0jQveeeVxgzSnoiZ_ssc3JzNQJHy2a0hbuSNVj6bKm-0VN6fwe5L7Cg0jWeI8fcTgkezycSounCbAPrw4DUUQR2CgH9wCA4NFge5RqJ-occnDAn1NvNtdrBNIvgFgsfKVkkKwVm6r_H67ZA-zDefuLd5IKdmfUaziJO8LtrysdPiBSSVZ1UTcPP-Q-Gc9NJQYULbDmO1ZH4ZodKfK54h7CzDAQK4tKNfA31Gnf1764jElQZrmx03Lw4RQsBNZ8FqS4bHFOvn13SQx7FRl39CUz_n8M6GGc_IpT24RGtWjBtqIiYj5Z85Ya4l_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29218">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzjqxHiHKa6TrAGzRKEcWoM4i6kwDYOvc5Mq4SqKi7GYHL_bg2jZxl7zNijwrEp5iN_Ita_RYsvwnepKDJ49B8Zy8ZHuElxk-twYP6YTGpOf4hyVS61uDSJLiA0TMZ-GgKWFjCCEaJ60pk6uN7W9Ymi0PMJ0YgjCP2ByOJiPXsA9oX1terW84XY6muPpD0osoAmFdIlXDVN8tAp6vdFc4DxA3IDplbt5Y3p9LSS8oy9sDULfHhaB3Copnee8csFeGQa8SkiET1KJH9dkx6q5T1BasM8BTAU_4fNGl-IlPIzLGHHPZuypfckVrxbmu51WOFmobYnlTHNljLcD-lMCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
بعداز نمایش نچندان دلچسب در بازی اول؛ محمد صلاح ستاره‌مصری‌ترابزون‌اسپور شب گذشته دوگل‌خوشکل‌برای‌این تیم زد و سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29218" target="_blank">📅 00:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sO1_kPK-ew1vcI-Vm9sDUE7nEdDEl0Bgp2MIqCZZxxBjMm_zwY9jvUGgIHA9kaD_3waS4cpCOq5Z_Ua0EyeudyxL78y1uYxWoFzp7I-8tTwRZ82lF4aLKQP3YnpfxJtf2UpGesZ348mi91Q4ij0G6HFHllKibw8rZNvaTFIqSQzmbPn87NRPMYAHKi3xn6qlSyuf7uesEJ63D1NWvY9M_kgv5YBOpD96h4urwa5h3WVamafSryZ0oUTpIEdzQq3wcPss_zj-UfU_JKNZDVnXlNyPwyllEQ4wbBfF-U1DbVhDrDKDCQ0lHIx1QR-iNbef8EPvJqu70plE_8E0kb87ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌‌سوم سری‌آ
؛ شاگردان آموریم در واپسین دقایق بازی گل‌مساوی رو از بیانکونری خوردند و سه امتیاز شیرین بازی رو با یک امتیاز عوض کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29217" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgbF43lvs3faeoOVaZo7sspLbwzQESIPxICf8bFd_f40EmAIfZZJs6ykrLZlNVW-xOXwQuN7wc0Hz3D11KMdV2U9_QaKsFCscEzVNH5wFzk0atsJrkKjJwFU4hW_KyrbSwxlCExuGkaOla2qC33OyPwNe36nr05oladpkcg_-FfkxdfOb1kI2_yc5-lR38zVq7zwUCQeCB07CPTTft7f-_hcKGbMDkUC448Bxbq1IgWJDFJjb_jN3mE4T5VUXtsZDLbfEOf8i5kwbSI99CeA4HDWnuvywajhYV9YXYqB6zsYOA1dyo-ZG1hCQVcQhjB4T74CyOXmU4mWvlbOnw4y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات لالیگا برای بارسلونا به یه جلسه تمرینی شده! ۱۷ گلزده در ۴ بازی‌واقعیه پلی استیشن نیست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29216" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=pHVCey9fL67scY3yTI-U6mbhe0zlZfg-SoUDyQg8x2Ckas9xvMJ0M3XMqLiMuyptN5jmmbRnmOuuzKlKBqZsFPI-LgvMHeHQBfjy00BF4yrMUmxj7kbSmqnpCxfJUViUN0zw_vMARKla7s5FYaGAGPgWdeNiEA2emleG-EuqXFu93uw6YkxZ3l2Rxt3qQ9JG3i6_wp2vmtyqisBOpzdiU_ZBum6IsLyKsjI2QWqDXU1YJLHH8Yec9Atlv3kElAY9aVdYCzYBY-2z55RB7qeGSWxkcaB3yfv2P_MQFk_nOrIrr86noUrap7H6vb82vGe_Ndrut9rYyBmmiF69IS22aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=pHVCey9fL67scY3yTI-U6mbhe0zlZfg-SoUDyQg8x2Ckas9xvMJ0M3XMqLiMuyptN5jmmbRnmOuuzKlKBqZsFPI-LgvMHeHQBfjy00BF4yrMUmxj7kbSmqnpCxfJUViUN0zw_vMARKla7s5FYaGAGPgWdeNiEA2emleG-EuqXFu93uw6YkxZ3l2Rxt3qQ9JG3i6_wp2vmtyqisBOpzdiU_ZBum6IsLyKsjI2QWqDXU1YJLHH8Yec9Atlv3kElAY9aVdYCzYBY-2z55RB7qeGSWxkcaB3yfv2P_MQFk_nOrIrr86noUrap7H6vb82vGe_Ndrut9rYyBmmiF69IS22aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی آقا دایی هم عصبی کردین؛ واکنش اسطوره فوتبال ایران درباره درگیری خداداد و امید عالیشاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29215" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unkTRlTrUo7RbgR3nP80nJ6sqf5C3fUdj7tpm8j0W2ARXWMpCoL8mrNCvREQ7ZpRb6N7WME1TPhOrQFtYAWdrEc5nFsxWnR0YEfelCCgS54PrEB9L39wA9opxo8gv349Jds0ifrP_1GK-KhZlrTlDkqk3vNvNxC8ijhSIXU26ZiIYvHmMljxBtedW1XmYkY8B6nE68FXvmFXK-4FLh44o-eXN0nfeIxiFe-960rYsphW1U_L_iWFr6_sNEORp3HoX8BQq1FHYKW28UOIOMkJZQTQEAHf1dwWrNA-UENL-5zfiWcg0mhgL38jVR5ktmsdI1fcWOlwxqIzg5lQ7tEwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیروزقربانی‌سرمربی‌آلومینیوم: کاری به توافقات بین دو باشگاه ندارم و اجازه نمیدم خلیفه و گودرزی دوتا از بهترین‌های لیگ نیم‌فصل از تیم ما جدا بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29214" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiVvme-1szP7g20TEw1zXmT1N3Anw0i6RwmN7Z93o5_eb6Q96Od058-m5Qz0qTLzUpKU2sxsDzoihaU8wYmdVa55BfeT4JH1ZMobmX-FhjM9LnAbS1km9YBdNmt6XAStJcOnzG6XeDa3bgxNG6i0hK3I4xJdoXLsRYWNaUEm0HLKzD6mjtprTwQSgEDctOfrz1qbeRUlyxQ7sl4OD5JqJ9LkpKmzpVGKSa5Nt16EVQH8UMeJyHKyfMx2oH9pW5rZPs2G1OZaKO2-wm0yYenyYxPfFcPpIhCfgWr0KDRJiGis1YtMu4gxymgqkl-Y2jCtV1xp46SEMh5JKStD6zk0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29213" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=LgWR3E4Qfh-XaTm4jjC-bUbr6e_dR9ftJ0RnXsWWTgjqqqvopvZxzB78ctCsLtA7u_fUzqW1LWw4xLI2bebzrt5L9cZS3z3pxkArRzbTZwUl_kXMU7XTDIMEPT34EJREJA0JzhgWhBSd_WHQD24E-PCmDrH5J6FgfTywOYC_BKUoBHZeskadq7DK0Z1xlCeCcScOIvJqwNBT-rp0Aey0UtkHtFtAwUsurV53eKBjHX_dYrzJAVIebESekZH3Kiu50apyBSERLqGMY6tgHXT3VBTCvJNRBd3f8Ro7mAgjFeAkZU8-xqs3_uRhQH_2DabVfXX8CA42pnUiR-FnHgPukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=LgWR3E4Qfh-XaTm4jjC-bUbr6e_dR9ftJ0RnXsWWTgjqqqvopvZxzB78ctCsLtA7u_fUzqW1LWw4xLI2bebzrt5L9cZS3z3pxkArRzbTZwUl_kXMU7XTDIMEPT34EJREJA0JzhgWhBSd_WHQD24E-PCmDrH5J6FgfTywOYC_BKUoBHZeskadq7DK0Z1xlCeCcScOIvJqwNBT-rp0Aey0UtkHtFtAwUsurV53eKBjHX_dYrzJAVIebESekZH3Kiu50apyBSERLqGMY6tgHXT3VBTCvJNRBd3f8Ro7mAgjFeAkZU8-xqs3_uRhQH_2DabVfXX8CA42pnUiR-FnHgPukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی‌لیگ‌برتر درپایان دیدارهای امروز؛ سپاهان با همون تک گل لیموچی سه امتیاز خانگی تقابل با آبی‌های خوزستانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29212" target="_blank">📅 22:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCFYy0yvKGizFM6hDb-4SrUk2P1P1QjQFmcOlE8-gscKrxNRmWhSTUqAbLnRN_Ebn1HH55_n0rtTcoucpZCKBh7a7XF1vCUAL4hfDmNF0t3_xTbkw1fXgpvsgUSngfBlPDX3o2fEh-91DXOhg112dT2-AKER8aUoPN0mDgiajca6XCfz5SDLGwsoZYGL6KJwFV42xyzr7BHoq_idrB9T8CTDj2D-Ntd75xNDb0NsjJdOBNOxanpOBidPRBnVuB3JQGypjTtKrqulxpJ_7U9Pl7CTj_ZJMgPJSjV1NK95N92S_kZ8sQQjJScO8Muj_wGjoaqlmzmY3edqxcOa9pvGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29211" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGbJyERaqnqNnrsw_dkiug2M1jE5LI9QlQYOQfjh_glewmfOxzcHwgGAareFaIoT01PBy2GmDXMCZnOCJqMC2lH5sf1CVXnfk0XZEqmTtrjCl9pM6CIee1mL_2kcGJgR2W43yo5mpLCxy9q9sx0yfWPtI84T4iACrlpTkX0qhHnv4bGzC0MJOM7XsPCpTEDimLUDTQRAN59adcRjOVXxialLIcHtTEaAdoKAbYFiEgQSSC-3_vUuzYjNVL52IzytMKFJZsctjBpf4Sox9IGDSJz9tJYHz_Hv7rluUPjGRvDkcAJyP_N0DXP5fYP56v1_dR-PvFXPwQQEFiR6SDE4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=ciw31AK6-W4u-_X_1aGh2k1grLcYNYdZJccXxjbzN7QM0bE3SZ4Snm4LNxWRruacsg1hi5pQAYnl9VN41yGon3BNSw-nEpgE7YfDAX1ql0YytxFqBrZapQEcEKiP622DxXY6a1QoBl_2I9vnApxZroG4YdcBHZIgS5BTpXYcBJjT0Q0I0c99-yt2oatdjKP5c3x3IAMOXjgFU1Z-33wqmgMoexiZuay4Cncyu88eRvmG2PEqofEgID70NYA3rbPj_C7_YWyl6OYu7q35sNQw2GYCRSPT7M3V0yF14p9CjzWgBhfjcz7LT542T-lOiCQf25brrkTBUe_mY9Pg3WJbITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=ciw31AK6-W4u-_X_1aGh2k1grLcYNYdZJccXxjbzN7QM0bE3SZ4Snm4LNxWRruacsg1hi5pQAYnl9VN41yGon3BNSw-nEpgE7YfDAX1ql0YytxFqBrZapQEcEKiP622DxXY6a1QoBl_2I9vnApxZroG4YdcBHZIgS5BTpXYcBJjT0Q0I0c99-yt2oatdjKP5c3x3IAMOXjgFU1Z-33wqmgMoexiZuay4Cncyu88eRvmG2PEqofEgID70NYA3rbPj_C7_YWyl6OYu7q35sNQw2GYCRSPT7M3V0yF14p9CjzWgBhfjcz7LT542T-lOiCQf25brrkTBUe_mY9Pg3WJbITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdfG6VVj8x3rs_bVBf_aCfIUiy5v4okR-8vCG0hE78dMDhNEWMLgP6dE0hCdBG0Wpy8sUTYG0YJpuOa_cFbuRW1D0tmucetZleeniLvkJfkTg6q_PjEg-VRC5k8zK0EDSIMOLRqDcuJF6fhPOF2eLHeOX3ulSwkB_JheEdH4TAeyjSL14XFNO-FvSdYauq9yKgt2Zu7AhxGkxpkJFryPKrXL9vLg-akS6qpO2sTrnC6H8m2SfysNqTAxO_cJHfs3lsUhu0nMaNo8qNj5o4oARaEGTbVgOvV63OUjwt9BbNaOQZrgcTgsiJjTWKInb1OE8F8DoylBAFtg_R3aT17bgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo8SV1RoV5uLPQzrIzrJQFY8nwEsD1Ms9i547S9utOu5EdJbidWYRkqyj6Fg2OrrEFWup4nOYSkUnZGUIVXaR1ibPOubWD-RhkuvJSs4kyBkg4cRcC66Fnme04m3HtftM4N_FMno1VaAJzki2Nfdud6ap7F0PW8vY_A4baq22Y5EU0hcubnqvic5-SOWlhezWP2_2JR8Crz7UjN9OPHtL2YeDY9YJ6_mEHmlt7d4x07ef2nnupEhyRjX9XNOZTUSNkeHbDTzP65aqxjKqmFZhecvNvNyAYNgrgvVNvHJE6qQYctlb2OiKJm9xk5djUs5jxrXzQ5lsCRnXaW80SZEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4rkUui3I20B3zbnxHCeklS7JnzO8nKx1xO5HHTVZBHACVL3R3oLHe7OyGJQT6xJVsItC8Wie_EyYP-lBiOl2Mu3Z_GPKOooQtJT7CzGGeUCS40klg5bhQ40nkyQHEnadElhjJKHV38Yym-KfjELyFgRFvpuDqzfwvpy0iXjGteoe4pN2Ck6BRv9L1xL9T0ARP1wrJ8Wqv_k-E8ikiC93tMDdxcl11QjzJYqk3wnd_x9QPyTHXtunrH5z8Ao8s1kt6sn84RY7M3eTgJv9_vPicF2fcUL9rOh_0XYBQLuMEwiiDkr7ldt1RGnn-PqPWYgHAwWGjUWNaEgrP8Sp1Vu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ توقف شاگردان سهراب بختیاری‌زاده دراراک مقابل یاران پیروز قربانی در روز درخشان محمد خلیفه دروازه‌بان جوان ایرالکویی‌ها.
🟢
آلومینیوم اراک
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMBTdl2DWer3hgqZVx8jJgA1zt9XXQkQtS3cF7HJYuIc3vbl_DKMrb-3sQbcx15CPChEUvTvVIB0RANG5i5vaNxz3Nd8MVyA8fdCCpjnxMBUHTnmXiJBL0mfgo8rplq_EpAAqyjt3PC8PFVHSvWNnAQCb1hhvVQANPGTQBx60uPpEXzFANSlISLzEBs6A4Na2ouLGYuEv8Mbw9KZ6AghUWEiMl0OCR8S6N4IF4NpstcFgI1PDqyL3SS6v6nMPx69bEW0e8wQRL_0qfFSQEfsH0TEu1F0ao1LZhJ8uqwlz7BsB9CYdiMZNLoMGniQeYf7SOFy1r3EKdTBXDluZ0eiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD4LiLk1akgBwXVhMQNMZYNLUQ11Gz3-G2Ba9tpQQxcCO9DXMDI_1Sc6pPmFr17ln0SpUTejgCaDhO2DF89LbZBQXdeYnp_mtEDBOzFjyPtYQftzL4TeoF7QXEgx5hPkKk2ezI_8PlFubuAr4qybXmvbv5UC2g_uSaOVICSLc6Y531L6WNiUrApjt8Qme2_PEJ0Wq_SE0WVMxXiRhRJdK8mvq49KP1v1-Ca8rEcGEtMUB9dtUH-1i1nhxLYykDdnMEe-IYa3m7gCmIn5JwJeX2ftzcTOprbvzVASPIGeXyyT7wQm6A9Srp7xIy0_BE8hZAwnqZSyp5_BYgYs7ssc_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmsc-82nOs491vnpR_2D6anoZddUPh3pyaAh_YVPxOSIiDmO9LIIHgNivAmxAIpQyIvIPd3lx7N_isZ6HhVvfpyYGVg7mbbnjLSJUWLUW5JwaSDshstEFe_FgD9FdzsQ9dUpsfPlbkLTXdvQv7PCgPxAqfm6ZabynyplMKtB5YhNrkfgJae_uZV36Z4G913_S7AQBkARDq2UKVu05jwlNW3T85wIgpzg06rBzZrGyT_vn9hWd7LpZRzn-8kdnErcuEwUry-nKQU1FFc1fTl5aEZEET7qE33gRZ0cdxfyhTcw4hXBEuUBgy2vYgOhiiWJigT76v4jwkiJLenMXXO-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29202" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29200">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=hggtz-rPmZdGY6mF8UmeeK-x05dnhSSvPkGKDTleZH31op0hIvKCal2jfVB-6YRwF0CfFM9HuQtKWf_YRDIAT85gPlCYPhB7LlAtj0UuM1OaQw2wNS1ZBNs3-oyEl2pRS7BTsVA-C9BgX8BjxY6yQZeTAwy5MnJUZG0sQU-JB9oNyIAjoAL18gtwwM0r94uIdYU8JzgACOgpWTM0rbavhV9_zHsTfTjNWrH78WLr-mvxWrbw-vx7qP1ZPEv2VMZjwP3bWAnIIP93m0Fcl-C8_To_pyGzTR7o-A0rtFj-G1KyrwUrl-4PQehcFa5PgrArci-nWVVWzJ2aKAC7lBS_0l31xdaAeM0sZZaDTLUQucvmyNDNHIHSkUVS11fTP9iJO96WFhCU4Y62Krr_FVHX8K62hfkcBzI2RwWI22BHzr-s4wc6wZRGgC9eh4FH2dNiJ1lCSz38We5GqWrRT3ffOhuixCD4LLzrCTaBRoejdcUgUAgKmMrAAsUkkE1Id5W7CqP3tiqIJ_ZGMeHQENnp0g0LrV21CfUY5dbTNhfakDDg9NAHTHVOI0bJ29fDUrTGSn-YWJhwcGBB-bpMG9ZN9xwBhGjOu2WDsbwMpbywvQnhE9zib1ooaE3cExRUVWZ5Iv-4xxf5k5uvzvuLYJBjXR0meWGQa8aNyAt4WSh614Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=hggtz-rPmZdGY6mF8UmeeK-x05dnhSSvPkGKDTleZH31op0hIvKCal2jfVB-6YRwF0CfFM9HuQtKWf_YRDIAT85gPlCYPhB7LlAtj0UuM1OaQw2wNS1ZBNs3-oyEl2pRS7BTsVA-C9BgX8BjxY6yQZeTAwy5MnJUZG0sQU-JB9oNyIAjoAL18gtwwM0r94uIdYU8JzgACOgpWTM0rbavhV9_zHsTfTjNWrH78WLr-mvxWrbw-vx7qP1ZPEv2VMZjwP3bWAnIIP93m0Fcl-C8_To_pyGzTR7o-A0rtFj-G1KyrwUrl-4PQehcFa5PgrArci-nWVVWzJ2aKAC7lBS_0l31xdaAeM0sZZaDTLUQucvmyNDNHIHSkUVS11fTP9iJO96WFhCU4Y62Krr_FVHX8K62hfkcBzI2RwWI22BHzr-s4wc6wZRGgC9eh4FH2dNiJ1lCSz38We5GqWrRT3ffOhuixCD4LLzrCTaBRoejdcUgUAgKmMrAAsUkkE1Id5W7CqP3tiqIJ_ZGMeHQENnp0g0LrV21CfUY5dbTNhfakDDg9NAHTHVOI0bJ29fDUrTGSn-YWJhwcGBB-bpMG9ZN9xwBhGjOu2WDsbwMpbywvQnhE9zib1ooaE3cExRUVWZ5Iv-4xxf5k5uvzvuLYJBjXR0meWGQa8aNyAt4WSh614Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
درهفته چهارم لالیگا؛ شاگردان هانسی فلیک در در دیداری خارج‌از خانه آتش بازی به پا کردند و با نتیجه پرگل پنج بر صفر والنسیا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29200" target="_blank">📅 20:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29199">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e23364253.mp4?token=oPqmm7K9Vmy2cjWBJS-s0X9n0MvVqIZ_5cbIZn4twwGroiuKgDQghHb9MP4JYP5ILw13EgGy5LExYj1UC3cn9DQSsWto5dkYUQhpSE8tlL0tL5AELemG-e5I3bNsw_4B_y2fgt_d9NzKNKOdwwXbheExa9YPko9ITo1dLptFMc7RVRRCqnpHr-4Q5Ymo0urBCucxm2P2r7Qn7DkW8XuiSDvw8xB9w3B4B6rORhaq6t6w67etTczOt986TLfp50UNjYp1p_DQJOIaUAtz4OS5ZaRrJyFJMyJ8NWS8iogjb50pPMH1qJDfI8A1cPRVCNSANDjstXgIKcgbolm8so-c7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e23364253.mp4?token=oPqmm7K9Vmy2cjWBJS-s0X9n0MvVqIZ_5cbIZn4twwGroiuKgDQghHb9MP4JYP5ILw13EgGy5LExYj1UC3cn9DQSsWto5dkYUQhpSE8tlL0tL5AELemG-e5I3bNsw_4B_y2fgt_d9NzKNKOdwwXbheExa9YPko9ITo1dLptFMc7RVRRCqnpHr-4Q5Ymo0urBCucxm2P2r7Qn7DkW8XuiSDvw8xB9w3B4B6rORhaq6t6w67etTczOt986TLfp50UNjYp1p_DQJOIaUAtz4OS5ZaRrJyFJMyJ8NWS8iogjb50pPMH1qJDfI8A1cPRVCNSANDjstXgIKcgbolm8so-c7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ کسری فیکس شد؛ ترکیب سپاهان برای دیدار مقابل استقلال خوزستان؛ ساعت 19 از شبکه استانی اصفهان پخش زنده خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29199" target="_blank">📅 20:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29198">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUgOA1Towfx_iRxbEJ-JkWQjOW2Clqqku6FlvOrQn0kH69PwkCXqJA4mwu4nW0PyBl1_PJ62M0u0iwFJJGyLY7n_PVrn2LCjxc29tqoEcHUCSRpT4D-p1F3FxJd7NF5Fvv8eMxMr0UlwDf6XiS_CRE_Y38NpSlBsCGtlZh7yWVVcywH86scniERMtjMA_kqyIEYRtlnQ4FxSisI7RxNCMTqEy6N7Wc1uPFgSEOiZXkMRGxIt6Osux6rWE2Q1nZvmUydrWe7bG343sVwIUqqPn2cUlD5XTlsNV7XY8ONxf406ZujDpknCohxSRGEmksL0MjaYRLSoYXzDXys3_ywefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی پرشیانا از سیرجان؛
مدیریت باشگاه گل‌گهر به سید مهدی رحمتی اولتیماتوم نهایی خودراداده‌اند و درصورت شکست دربازی هفته آینده با شمس‌آذر از هدایت سیرجانی‌ها برکنار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29198" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29197">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBzfr-XlIORag4ij0R-ykLw8p8KsXSDeWyjHhTldgjluSfxj49sfKP1ISyN0L9UF_62gA7Yejotz4ozjxdgpxGAySRAcxRcVWb543TxRuT4hCOQJgq-q6cnCiuEXQ5ZD0IPC-VC5SD4WVhQ6LxbbrAzhL4I7UHZh7WM8DoOLx49yOx62sqrj2tS5ZhP8LIJcgOrd8Iia2c7CbNiI2CqaI8fALnXWMVmQhADsyn5nPw7mXD1N1lhuuxTRzS80JnnL57r0_q_OjDs_eyStHAzip-7o0MNomZHkmkwzpMjRawfuotEAW1qlywu34JX6rWrERlxv_8RIR8CWmPUKHyFVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امروزمقابل والنسیا؛ ساعت 17:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29197" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29196">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=ZWyn8TXJ-I0hlipL3L8LIoy7AmYvukEveyQuZFQUNCoAeZ0-ZDfjbv9ISpelqfjIgFeCDz4io1t3OfMjmMU-lNA1SllQg54Cay1HGRFuGComFxk4ni2eYkcEYlWgrvTH8n3v_8XNPtVDT4UZx6syHwkKzxESfaiVweFvIZbwv42uiY-t0xU4yAuaP-Qs4phEJHDGW9AYDfZKGW5MJX8mAUKIg1ZHGyCgeFJAJlbsFFJGazxhmTylQckFimrXwzs6EYlIyZCe9bMA-oCtcWnvYLXlogHoOPbj44xkbZeZ-dCxQe0qPi1skwKZ6qNsB0Tg5-zd8xkyK9Gxsh9sITaI3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=ZWyn8TXJ-I0hlipL3L8LIoy7AmYvukEveyQuZFQUNCoAeZ0-ZDfjbv9ISpelqfjIgFeCDz4io1t3OfMjmMU-lNA1SllQg54Cay1HGRFuGComFxk4ni2eYkcEYlWgrvTH8n3v_8XNPtVDT4UZx6syHwkKzxESfaiVweFvIZbwv42uiY-t0xU4yAuaP-Qs4phEJHDGW9AYDfZKGW5MJX8mAUKIg1ZHGyCgeFJAJlbsFFJGazxhmTylQckFimrXwzs6EYlIyZCe9bMA-oCtcWnvYLXlogHoOPbj44xkbZeZ-dCxQe0qPi1skwKZ6qNsB0Tg5-zd8xkyK9Gxsh9sITaI3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت تیم آلومینیوم به پیروز قربانی سرمربی آلومینیوم اراک اعلام کرده دربازی فردا با استقلال از محمد خلیفه و بهرام‌گودرزی استفاده نکند که قربانی اعلام‌ کرده که محمد خلیفه و گودرزی از بهترین‌های این فصل تیمش بوده و نمیتونه اونارو کنار بزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29196" target="_blank">📅 19:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxG1otMFQHyhtxcsypeNopMtyiiwrSN4sLl4pVM7bj1VfKRaayF4DNdOwIFNYJ30W4L53kVh4R0eXDSfAHivyyN8r-L6RzxNFnE3IkHodTt3AN9973DvM0wCoYqWHpvOT_XrYDR1JDiC6-cTYcGyHnfyfESCYyg3Hg9X6labECvZDnnpw_ZC1QirC_v1cmIBzr0QDORs5xKLWPLconb45dGoTtLFY0Kjzpk8yWFZxUdnJy2inBBvWqrtWvJJbRmyNEWi31vqqADeWb-KmbrpWHTJxuhkGhP8kWMXx-xa0IbbJFg2l7J7j9uUrED8O8aOiV0KDA2_IhB2Y56n6Er3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIAJKo6lAzKnwbrK4_JXXc1ewMRPv4gz6KeqY92NIWHlopQa8Pc_f7ze_zOxX8lji4dSQIbTSAN6yrX5alJWUPaeQR745D-oIkQrYaJjKPdICA82KWK1L5LCTSzdOwIKT7RrVOdxAmuC0rUTEW-HgenuOa0ihOzcu0FiU_-K_K4sPBEHpLoKwi9B5brUDPZFYEgaVg6jLlCEsXhC7JfCQVTSqbg8tXKX6LvDquaTI0wpWgjp9xF3LhPDNtcuwMOXSZmDOXfv62agMXNxbiUYBq4Ff9y1DvhWbkn8l_uem9ROJbMzlGwJy9aVNBJIyZFiOLQFTmz2pBclTldzXdMY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA-R4hP5-ICgg21PgkUs2EGXP-KZYizuhmscoL30S9VRxDIpzeTEAx3ujrG4jo6-1U8jmTuOHCt4TQyBiYF8OIo2Pmwq2kficE7iEUzo480_F0GPSrKtSIPVjJ2fozjAJCWPx9GxCYw60KKCSTsycsHYOAZtymipLiGFEAbxT5jz6uMl_uJXbA2QOVJe6jglz8MSbhi3j1zJXpF92W1OHPdeKEXgTTp_ItYfxt9CcI8b8UZ-S1Yy-27s_DpII5PNHbpuvjk8Ok-ajE9ScPgEjQ62P7esovwswt1BS7Gqs60_jSHH9Vrmmkr2ADiUhaJvvwH9f11AB45f2-pYnn9PyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syiuqJLbvbDsg834ZEFPtLTtHuIwRnYI68GDAIVzrtkxDEOmTSAiGvmhPXbv1cek9GM5ktIk5rVrgdk-WDLcGiQGrbMA9qHgm6GUex27cl2xWY7lVzEj4nPzQWgxfdotJ7n4mt_zdvmqGWYyQAZ8XrIIycJBR40UCX_cQZXA94q6PyK1hLr9_o0SFBrFeyo7-fcpCtIs2BVLSdsfsoVpb-78mOlVNoCqzN1V6bATBSJigGtD89vcqOY69UqS_To4lrqoySwkRA5I3DwHXnox-iUJ0lDj5mdtFW1g77hbdTFXUb0ipGamywVGBcaTiixEF3supwwyLVGFz4fw5kusog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FesoouY3OURtTH03_i_J_EDqEkitWQ7S-SOIIxackmhHiPEodhsrUog4R3gqHn9GTcsuBo-eheJFowcGayigHxQK-0phC_CboQYI-9xsfNan7J1k2djADrvHH4g4WXMxOofqb2y-hgOkxkRZZG_KmLVaC0Y1yZxxOzCZDMZv6keULTZqahSJw5cB0IWKmZPuTwlZTYNTuTlFpYBU-0gQtn7Xx7c2Zsws7Xtr_rAuvWFuEOu8PNgy9LMBB0gK29G8pbg9c7-LPv7QhhAzkchbphhV6to7PhXF04-qCNs6S7exXvBjC7VvAgv5r5mzmslogndKY4snQGyi4O0BKkOYaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
