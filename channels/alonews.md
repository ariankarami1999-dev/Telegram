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
<img src="https://cdn4.telesco.pe/file/oTF_naOUns1QMXRzE2BIOHta7yf28o7ulF5EO_D-BOdrex52rFOqMkHqEdohTTJBj82UcrfMsq6khu0qPlXUHkebJWLX0GZf8k1zIfmdjXFsJTvRt5-wU_d4ZNn2V5mBiTaQEY4hL9ZfdSqQCL3VBgfgCggL1_tIVoy5hZ5X5ZxOIg99AYGWHWF6K91fGSgjbLXoXxEysZarV4mYY1xbHiqbefNRSW6vG7h3vu_eaQidqoYZHkEhT6vJCgOV0N13Uy7TKU1wHba_5NXRQEllpjJ6DjRPtMOivGY5XzOL5ADjob4U5a__tZ7aoUlNqx5wvdp5LF-FrLcpi6Vz_Wjg8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-144387">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پزشکیان: اگر لازم شد برق دولت را قطع کنید؛ برق صنایع نباید قطع شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/144387" target="_blank">📅 14:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144386">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN6qnRR8Q8836Zwjr6AWjxrHFxh4KQ-1VYAm6LEjkrf92tln2IAjLGF3nkjMko68pANNkSQK2irWP4bFMvu0p0SScT3YcD4NHUNNZodWAR-b-b2R4ddw57dObfs7uvAixT3vjCQW8l676086Qfc1VWYDJBLy4UkK0WX_fmhcNyCMi5rhBsS1HvL17RatXszj8WzpJNXIOkz1V1fVWD8T4We6eM7p2DwiniQk6QpkS-j56uToeTaLrpjay9REdWkpmZjehcJM0PRXKq5L6drcEYt8oKRM4YD1eh3O80FdBcX1oTwNbAZdzolEUSnXpWXl21Hfr0wRor8VkJ1n3ILDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شورای شهر اوتاوا روند بررسی تغییر نام خیابانی را آغاز کرده که حدود ۲۵ سال است به نام دونالد ترامپ نام‌گذاری شده است.
🔴
به گفته برخی اعضای شورا، با تشدید اختلافات تجاری میان کانادا و آمریکا و اظهارات تند ترامپ علیه کانادا، ادامه استفاده از نام او برای یک خیابان در پایتخت این کشور «مایه شرمساری» است و باید تغییر کند.
🔴
این پیشنهاد هنوز نهایی نشده و پس از طی مراحل قانونی، درباره تغییر نام خیابان تصمیم‌گیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/144386" target="_blank">📅 14:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144385">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca27e916.mp4?token=WPpF1CtEqEa2Ks_Ne0loKnCtzoXL0ptPg7G_svMsEq2nlx5PeFjv_RPzUnSl2bWu-TZWT8jw08X8Cpa3gDkjug6vHk1Q8Sx6r4x6G_hjA4hu93E6StaNSFkyg9P9eR0u6az1rr3wSKQ0m4f5tICV_bFTZQb_thhm_ItddJdjT1Cj5hxwQUKpp-_354cxb18CEJhyfhxMwDMpS97V0_qyB1Xz61IeT6e8BJ2tgn9YoPU_OzzWwSnDxglhwQkbzrhdMFdiKilv6CL_CjAH0-HhD0j4BThbXXu4Awl3HNByUIwDWqNpESSTdlc9pT0rMoo8u_yNgkxoIOejc2UkQrSNtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca27e916.mp4?token=WPpF1CtEqEa2Ks_Ne0loKnCtzoXL0ptPg7G_svMsEq2nlx5PeFjv_RPzUnSl2bWu-TZWT8jw08X8Cpa3gDkjug6vHk1Q8Sx6r4x6G_hjA4hu93E6StaNSFkyg9P9eR0u6az1rr3wSKQ0m4f5tICV_bFTZQb_thhm_ItddJdjT1Cj5hxwQUKpp-_354cxb18CEJhyfhxMwDMpS97V0_qyB1Xz61IeT6e8BJ2tgn9YoPU_OzzWwSnDxglhwQkbzrhdMFdiKilv6CL_CjAH0-HhD0j4BThbXXu4Awl3HNByUIwDWqNpESSTdlc9pT0rMoo8u_yNgkxoIOejc2UkQrSNtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صدا و سیما: تو رو به خدا، به ۱۲۴ هزار پیغمبر، به همه اهل بیت باور کنیم ما در جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/144385" target="_blank">📅 14:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144384">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سیلاب و رانش زمین در شیلی، پرو و بولیوی
🔴
سیلاب‌های ویرانگر، بارش برف و رانش زمین بخش‌هایی از منطقه آند در شیلی، پرو و بولیوی را تحت تأثیر قرار داده و خسارات گسترده‌ای برجای گذاشته است.
🔴
رئیس‌جمهور پرو در پی تشدید این شرایط، وضعیت فوق‌العاده اعلام کرده است.
🔴
کارشناسان هشدار داده‌اند که در صورت ادامه بحران، تا ۱.۲ میلیون نفر ممکن است تحت تأثیر این حوادث قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/144384" target="_blank">📅 14:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144383">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=om-sDPAYFcXrEsyLb2rjNquqX3f6LTVWIZS1sbRTb-c4mz9w-1p6S9vAqV1Ym1zB19VFpC4KOWYvEP8y6yXXzO6u3v7q24Lq-db9-UcgvllqCUNPcQ0gZDgGvcUcEMptIKcWGC_lJiNuPO2ANSGvSPN9HFX3DFghA4DjpI_E9EFB9SvUOTkTPNbnP3uMLDoclu5ogHw0wDg4XjqohJZP2JqVgFKRfVwlouF9xSIekVLKPFcYwknf8F2cq7HGIiS65fEV3j3ZRBYM_FjQelFu8_XOC8JuW4h8SR_kKgR1D7kB4LEZ2Ir2okYYxEJnBWIXIslEtvIwAP3vPGEYdH4AbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb1e6c44c2.mp4?token=om-sDPAYFcXrEsyLb2rjNquqX3f6LTVWIZS1sbRTb-c4mz9w-1p6S9vAqV1Ym1zB19VFpC4KOWYvEP8y6yXXzO6u3v7q24Lq-db9-UcgvllqCUNPcQ0gZDgGvcUcEMptIKcWGC_lJiNuPO2ANSGvSPN9HFX3DFghA4DjpI_E9EFB9SvUOTkTPNbnP3uMLDoclu5ogHw0wDg4XjqohJZP2JqVgFKRfVwlouF9xSIekVLKPFcYwknf8F2cq7HGIiS65fEV3j3ZRBYM_FjQelFu8_XOC8JuW4h8SR_kKgR1D7kB4LEZ2Ir2okYYxEJnBWIXIslEtvIwAP3vPGEYdH4AbTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری ازدرگیری محیط‌بانان با شکارچیان مسلح در تنگ‌صیاد چهارمحال‌وبختیاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/144383" target="_blank">📅 14:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144382">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMwLlKIgHarfVg5NHvcX2ulEiQS98awAXcsBIZT4CGzwZCne45bFFpbSKaLneWoxd2GzvKoLaUzEXEkTB-hrX_1FkfAOepiB5nsgJiCULg48A3MaSdH7VuD_imLPVf7dxJw7me75AWhsM2bMmbKIAsfnWQa-tCgrsTUXxibacEtepIPwfAtzTKc0dNsW8wIafTIgn_PEkRXKrutfErln71yHS1wIAngDpUYLe0UN4QAswbaiwyI_nkVmNik1EaOIZ-bec0qwo9SiAqoGTIYMVnCefm6qlccfggZ_aRCAUUpcICjMkjRFht_Ymt3tXzvIEf_YmkSzMcE53Kg1YrXE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این مرد ایتالیایی بعد از اینکه مادرش فوت میکنه چیزی به کسی نمیگه و اونو توی خونه مومیایی میکنه و بعد خودشو به شکل مادرش در میاره تا مستمری سالیانه ۶۰ هزار دلاری مادرش رو بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/144382" target="_blank">📅 14:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144381">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5KwNe_nFEg6_gGf_ifHOhjU2OMPjwEmldsLchwXBRkWDrPubAmowxlm8b7kLI2y54Ir7we1hE2uQmIU87Ecv7U9VRDqHC5tgehIs7HsFSevirdQ3aaLB_3PTRwkJUdV0s16I27c3DtqzXx-tSCjKMjqLjCo6L4d3gNHuo-OkBXiaWN2VSB1YVsZYuAndOjd7Q5BPYlvpD5tB2vx6oZUedpz89_dOW3MszJd-5A-D7ecZ0qEGbUix_nFhocIon0wnjmAHXvU25DdWW1vaJ9yRJb7EIhEH9YJi_zbWST7lFVh_8g93WkcfZrzV_8pGyWaMYyxiERJYeyHJ0a4ifuUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع برکنارشده اوکراین به تیم دفاعی ایتالیا پیوست
‏
🔴
میخائیلو فدوروف وزیر دفاع پیشین اوکراین پیشنهاد وزیر دفاع ایتالیا برای همکاری به عنوان مشاور در زمینه نوآوری‌های دفاعی را پذیرفت؛ سمتی که قرار است در کنار فعالیت اصلی او برای راه‌اندازی صندوق سرمایه‌گذاری دفاعی در اوکراین دنبال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/144381" target="_blank">📅 13:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144380">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
العربیه: گروه‌های عراقی در ساعات آینده قصد هدف قرار دادن عربستان سعودی را دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/144380" target="_blank">📅 13:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144379">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_aur90-31DhknWDB-rnsOnubYK37rAZqlQeg-wy-HA6u9jDD5l9sBbBeiQHn4GuI1Oyg16kHjcl-hETKtbZ-CfugLGkFFS1_aNx1lQofRu2IsfcKvzzfX80eXtgQ0qq8cMgBpO40zTIQNlzeQItsRAiO2xS7Yd7Fvz4SuLOMb0SEQkJ0FgCQm-oK8v0wTRV7nALFCB4i7uBKKgpC4ZuiiG80iU1BAKLrZDTJK4be6QDNdkaXEKCYy3OgbbhM2d5IvHvE3dRWFunr36QkZBgP0r86gbzUX9yS_SHZBMYnwH64dA0RgNse8MHM24J5wa0jaewtngUqqF_RZC7Mg5bKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه رسمی توافق عظیم نفتی ونزوئلا و آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144379" target="_blank">📅 13:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144378">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756a7c2134.mp4?token=Y4yqRe6V_2bFFSfZdZ1soSORbGdWjs-GrY7Qn42eiGIUh6oU6GdSCMK0REktRJWVvo30WCfI9Eh3zURMMFSpkIKC8OTl4ayZJRxcHOZ_th9pm_5G1BHuO7CkO4Mansk66Svij-YrmondndMeVnd8U31zXuRvVxkw1bSvdRjC4f1NOiRSh5hAUUgfTaPpps5MoVXVX-0ev3SmPnVSHzL--gDLJX8JO6hFTdGdIAMhugpW8pIQEBICOni6yJ5C_62rl9L_nuDLglXajlqpGKaK2nhUJrpAx_tkxH09RkI-tAicbEcEWzna5_hLcX8apfgDAJ-lT9tWX69N45_zeke8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756a7c2134.mp4?token=Y4yqRe6V_2bFFSfZdZ1soSORbGdWjs-GrY7Qn42eiGIUh6oU6GdSCMK0REktRJWVvo30WCfI9Eh3zURMMFSpkIKC8OTl4ayZJRxcHOZ_th9pm_5G1BHuO7CkO4Mansk66Svij-YrmondndMeVnd8U31zXuRvVxkw1bSvdRjC4f1NOiRSh5hAUUgfTaPpps5MoVXVX-0ev3SmPnVSHzL--gDLJX8JO6hFTdGdIAMhugpW8pIQEBICOni6yJ5C_62rl9L_nuDLglXajlqpGKaK2nhUJrpAx_tkxH09RkI-tAicbEcEWzna5_hLcX8apfgDAJ-lT9tWX69N45_zeke8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر مسعود پزشکیان: برای کسانی که می‌گویند تحریم‌ها هیچ تاثیری ندارند، واقعاً نمی‌دانم چه بگویم.
🔴
منظورم این است که عقل سلیم یک چیز خوب است. این تمام چیزی است که می‌خواهم بگویم.
🔴
عقل سلیم واقعاً یک چیز خوب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/144378" target="_blank">📅 13:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144377">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsbEOKLp9mv8Sikk09ZJAL7IYBRQZ-k8DsQ7JVT9kl1HW2QHjBF9GPnl2z8FORmhUbJhTCMMlxFGFRRYVIUvwPTvR3ImeB94TKwU3lpJVI3KQoEdZ7NnwMG5drBv0v1NRbTSHuCpf66UUugLHR06QOYUjHFxF_c527MpP2se5z1oZtXmAEn8QCdreKV8aJLHXdOu3irfs0qrF2fKnZETmvBgxtjSVo-As35nR4vOIFZVe7o_shZ23TU19s4ka8LSvjMpo0_wkzWyHSk8DhYq_C_3g14DmZ6MdnmL9pi_bEVLG681kO8I7x_yQaVWKwCiwHvRGvwZbxByocLOPcaQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: شنیدن خبر درگذشت پادشاه هارالد نروژ بسیار غم‌انگیز است. او مردی قوی، با افتخار و بسیار مورد احترام بود. او به کشورش عشق می‌ورزید و واقعاً مورد عشق و احترام مردمش بود.
🔴
قلب ما با خانواده سلطنتی و تمام مردم نروژ در این دوران سخت است.
🔴
این یک فقدان بزرگ است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/144377" target="_blank">📅 13:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
العربیه: گروه‌های عراقی در ساعات آینده قصد هدف قرار دادن عربستان سعودی را دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/144376" target="_blank">📅 13:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144375">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNIU7KJg5pJ9MvG43zKZTn8-E_C2Y6zM0_xm0HfqMxRf6_QImx9J3iS3-5t7cu60we4rYIuKZX6FotUbri__Ob4xe3mOs_K9FJiCk-T4jVqlzI4nru0vtvghl0-ACfVMsGwgq8lafXGbTE5WTWk_IioNnGklmch-utA0OdzQioFFTrIT0gWuPYED7_xGcFpfRJXkyIa5Tk26wnLHzcVcJraS2GWh7LlTAKOg9Ndzfn3ySt8mLzq79bmCL-odyKAwAAyjlOnrmZY1fvD4t-nOx21lhDqRaPLc34Jw3TUlZy65eGyaBjezSZaKNpRuKdmTat8wCmsKXFzF1n3t_287Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت دلار از ۲۰۵ هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/144375" target="_blank">📅 13:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144374">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz4KEztPUxhGFHywa4apoH5xPkZs-Ji2mXJzxrzuPssybL3Sbw4ysy3a_GUrJpZgHGk27_PTiNeVDzJYJcX8C03CLzA_wAdod5syfyhLiLz3QYls-IHXSk_VEOfAj0EP7gvSpvc5oFz_fpCnEzfvekt4uZ8jZoTz_-yjeWSx7PiwuAGbEmRbX2why5MTTEzSiDEPI8GTWBrsIRbsSSI6Dq0nmsOCoraa1d1UqbxOeA-fn_Al9g546CLQNUk5xu5xC0QeJt-j4GBCrapP9_jk-fF9bl595a6etz56k0vBsm35vAfLuXezWRpnf5zMqdDu_aklbHGIHIvMDthm_Gy6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: میانگین عبور کشتی‌ها از تنگه هرمز، از ۱۰۰ فروند قبل از جنگ به ۷ فروند در روز رسیده/ ۵۹ درصد ذخایر استراتژیک آمریکا خالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/144374" target="_blank">📅 12:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144373">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دادستان تهران: پرونده نتانیاهو و ترامپ رفت دادگاه تا رای صادر شه ایشالله
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/144373" target="_blank">📅 12:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144372">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۸ ریشتر حوالی قصرشیرین در استان کرمانشاه را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/144372" target="_blank">📅 12:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xyp5MRT3G2nG9U_E88jg_YIhzkLeuQz_cz5gXxt_FtxVfmayK_fD_KpxiL5azUg2FfwIr9igNgARUTGKrruj-n94EAFNbHKSKjnmhRF5f8mjaambMfUpDGUNoFW84FpToO7TsH_6Len-xMSIJmScXe8I9xexpY5-kmILR2t6AM1by1wsTXwDomhfFaTzDKtePieDfpknXYxkjzB-_XA3Mmno2zuC5y7i_uJZD2Id9G2Y9iIpGHHrAqQROBEhVAyC7saKKFS5ZWg9Q3MovcxrORllTW4hOKRhIHnjWVZ0TzTBCRXsHwlHK0maYxk_Bl9tyAHMjnuwEYijR_8kyN51BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیهان مشاور قالیباف را بی‌غیرت خطاب کرد
🔴
امیر ابراهیم رسولی یکی از مشاوران قالیباف پیش از این گفته بود: خونخواه رهبرم ولی پوشک بچه شده ۸۶۰ هزارتومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/144371" target="_blank">📅 12:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlv-TJPZZN-kal5LirOTV2LJJXAZdDWKZFGOCF1X4x0fwhF2ZPz1bPeNA66qVI7fCYJDjE7YaqpaTcTAhB_lYrd264ekZOvJBQ-N9xOvq1zGBiVLA7Kq1VrB3oILoRbLilXN5rci2TAzS8YTY1h-JTq_a9-DJzkMdXHL-Gcsv-jyzU93t_hIxngYfqh-Bk86aji4Ac8AxrNqwk7DTGhardMGyoZVwvcX8ru8BG2swXfv9TvrabNa7cZ-BZqbkkNz7l04gnSvWql3cE-qxVaRx3gL4l4c70EoM4P0zlkANo9ekM90a9zGKTUbzrwY_SeFikddkPntwwK1g84_Em28iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گلدمن ساکس: بازگشت میزان صادرات نفت به دو سوم سطح قبل از جنگ
🔴
به گزارش گلدمن ساکس، صادرات نفت خلیج فارس به ۱۵ تا ۱۶ میلیون بشکه در روز بهبود یافته است - که حدود دو سوم سطح قبل از جنگ است.
🔴
نفتکش‌ها به‌طور فزاینده‌ای «تاریک می‌شوند» (ارسال سیگنال موقعیت خود را متوقف می‌کنند) و از انتقال‌های کشتی‌به‌کشتی برای دور زدن اختلالات استفاده می‌کنند، که به کاهش قیمت نفت به حدود ۸۹ دلار از ۱۲۰+ دلار در آوریل کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/144370" target="_blank">📅 12:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گاردین: دانشگاه اکستر بریتانیا با عربستان سعودی برای آموزش افسران و مقام‌های نظامی توافق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/144369" target="_blank">📅 12:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی اعلام کرد ستاد مشترک ارتش کره‌جنوبی روز جمعه به وقت محلی از برگزاری رزمایش نظامی مشترک این کشور با ژاپن و آمریکا از ۹ تا ۱۱ سپتامبر (۱۸ تا ۲۰ شهریور ۱۴۰۵) خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/144368" target="_blank">📅 12:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ونزوئلا در فکر خروج از اوپک؛ خطری برای انسجام و اعتبار این کارتل نفتی
🔴
بررسی احتمال خروج ونزوئلا از اوپک، هم‌زمان با چرخش این کشور به سمت واشنگتن، جایگاه و اعتبار این کارتل نفتی را با چالشی جدی مواجه کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/144367" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d3d466698.mp4?token=jEHZ4mq99sGmQnq78Q-_7LMNWu9RTWlW0eLSqPwCnBuahUT3_5I76FVDHXRxNjeHGhc-0tCiaM-iWZYH150mcohW0UXyVRF8moqamgBkjQohK_Y7BRMzAFAzweCFq6oXfc73QRfel82djwQY7BbrN_6RAOttKvx3cYm7JNcG0r71coBbDVYtEmDfEEKL55N4eX-magf0ntQSjPPRrnyFOaQTfZgcTyNxnCjHqPeCnRalz8kfBCYGOER9Afzji9ccC9wpVQXc0g2gEc5Z17AcrHyruXYDthCog6oZUqArduiZe5W1qAF6WM-HaRnvUStfXAH9zj23xMhPutc8i_Bodg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d3d466698.mp4?token=jEHZ4mq99sGmQnq78Q-_7LMNWu9RTWlW0eLSqPwCnBuahUT3_5I76FVDHXRxNjeHGhc-0tCiaM-iWZYH150mcohW0UXyVRF8moqamgBkjQohK_Y7BRMzAFAzweCFq6oXfc73QRfel82djwQY7BbrN_6RAOttKvx3cYm7JNcG0r71coBbDVYtEmDfEEKL55N4eX-magf0ntQSjPPRrnyFOaQTfZgcTyNxnCjHqPeCnRalz8kfBCYGOER9Afzji9ccC9wpVQXc0g2gEc5Z17AcrHyruXYDthCog6oZUqArduiZe5W1qAF6WM-HaRnvUStfXAH9zj23xMhPutc8i_Bodg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از
آخرین وضعیت تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144366" target="_blank">📅 12:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رسانه نزدیک به ماگا: آمریکا مخفیانه مسیر جدیدی در تنگه هرمز باز کرده است
🔴
«مورس ریپورت» مدعی شده تصاویر ماهواره‌ای از لایروبی یک مسیر کشتیرانی جدید در بخش عمانی تنگه هرمز حکایت دارد؛ مسیری با حدود ۴۸۸ متر عرض و ۲۸ متر عمق که به ادعای این رسانه، کشتی‌های عبوری از آن از خط دید مستقیم نیروهای ایران خارج خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/144365" target="_blank">📅 11:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144364">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی: ایالات متحده برای مقابله با ایران، حجم بسیار زیادی از مهمات و تسلیحات را با سرعت به خاورمیانه منتقل کرده؛ به گونه‌ای که در مورد تضعیف توان این کشور برای دفاع در برابر تهدید‌های احتمالی از سوی چین و روسیه، نگرانی‌هایی ایجاد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144364" target="_blank">📅 11:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtWmr3KZ7AUAQQotBM3sEaQAh7wZff7cZEHm7ckf_kIt0r2q9FAYcTH6wTSVn8aAw9tfySLBQPXaRNTuto_arOL6CqtiDwNi8N46NV0uSnw65Ub1WuPby6iQwl-gieTp7P16crSPfRn-KqNZBhaAw5kucY7v1xC1StltgKkPWJREFzdBIfLf1BYKpI3iQN2HmmK3OKcGrjSl_di9wiwfz4vQWM5D5CbM01CAXrug0zEIUDBtJmQGlAlZazOQEuj7BkTfF5KmUX3LPQezM6MZye0NpaUKHWswWdJw8HcBCbG2RN177KVqIytt06zKLHMhFxwNmaFARuTYPn7dq5UttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای از باقیمانده ناوچه‌های جماران، نقدی ،بایندر و چند شناور دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144363" target="_blank">📅 11:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شمال کشور از دوشنبه پاییزی می‌شود
🔴
هواشناسی: انتظار می‌رود از دوشنبه و سه‌شنبه، هوای خنک بر بخش‌های گسترده‌ای از کشور حاکم شود. این افت دما به‌گونه‌ای است که بسیاری از نقاط کشور دمایی کمتر از حد نرمال را تجربه خواهند کرد.
🔴
همچنین پیش‌بینی می‌شود شرایط جوی و دمایی در نواحی سردسیر شمال‌ غرب و شمال کشور، حال‌وهوایی شبه‌پاییزی به خود بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144362" target="_blank">📅 11:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
حمله اوکراین به بلگورود؛ ۳ کشته و ۹ زخمی
🔴
مقام‌های روسیه اعلام کرده‌اند در حمله اوکراین به منطقه بلگورود، دست‌کم ۳ نفر کشته و ۹ نفر زخمی شده‌اند.
🔴
هنوز جزئیات بیشتری درباره نوع حمله، محل دقیق اصابت و میزان خسارت منتشر نشده است.
🔴
بلگورود در ماه‌های اخیر بارها به یکی از اصلی‌ترین مناطق مرزی درگیر با حملات اوکراین تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144361" target="_blank">📅 11:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz-zQwiLz_eGlv6jYPS2wVLhLMuUKXsBPOmGKrRfK-BGueP3sRZZ2wn-UtmQewTBynJiy-fCO5F5_MU_hdC6MTTSDH0HUxsrrdM4sOIevPvFuJqkHjwFg4o63oYjUvchkEWIpLBSX2mkdb7hNNaPwWhmv7kKee1XjBg-scuqqhW0qoz8LwHZTX0EiTCexigPigVc2R-xM44ZYgvwOxMQPEFocMhzWJwoP5UJwUsYDJxTRDjb-iaP9b3cU-Qw_EfrykOsrg6Q-Ry4ZLvwiuhvy2ktzgcWFS8wRg3K-jqic16n8dU-OJkqpN_75wq5U3xCtjFLC2J6F7pn6ccbuKGTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فضای هوایی نزدیک تنگه هرمز شب گذشته شاهد فعالیت گسترده هواپیماهای آمریکایی تانکربود بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144360" target="_blank">📅 11:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نیویورک‌تایمز: جنگ ترامپ علیه ایران پس از گذشت شش ماه، به نسخه‌ای از «جنگ‌های بی‌پایان» بوش تبدیل شده
🔴
ترامپ در برزخی آزار دهنده میان «نبرد تمام عیار» و «صلح واقعی» گرفتار شده
🔴
شاید نقطه مطلوب راهبردی پیدا شده باشد؛ یعنی «فشار قهری مستمر، بدون جنگی بزرگ یا توافقی غیر قابل‌ قبول»
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144359" target="_blank">📅 11:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiVfjhJ9LmQxv-dPkMAx6lWjn8WxyyZJ6_d26EplZGS39HAuN5LTXsk4uJmeSSZIveEKOdPAGuenAwZncHUdSWFfu76Uo7iLEs6XfrhyJOtkuJ4-alvs9tGDXbBrvj9aHGnWyabshwRVgt4Jw5o8VSquTmJ9DwR-JvGVfjXoQ51VMcCgKAJFqTlx_ZqF_40mJ8sbpE3n4u66ndlCOrXb6AfLy-4FHLr-enw-cpnvuFwwa65J8FwEDJqknkpT-MiMQIdtdbnQyGReCj87f_fYGbinGm6U-DEuXbpjzCzTxBqRftzUMoRZcmwVc5EYegReCYC0HTqRhfHEUtTQS9s2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو
:
توافق نفتی جدید با ونزوئلا، ۱۰۰ میلیارد دلار سرمایه‌گذاری برای این کشور به همراه داره!
🔴
این توافق پیروزی بزرگ برای مردم آمریکا و ونزوئلاس!
🔴
با سرمایه‌گذاری ۱۰۰ میلیارد دلاری در ونزوئلا؛ از هزاران شغل پردرآمد حمایت خواهد شد و به بازسازی اقتصاد ونزوئلا کمک میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144358" target="_blank">📅 11:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نیویورک‌تایمز:
جنگ ترامپ با ایران به «جنگ بی‌پایان» شبیه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144357" target="_blank">📅 10:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/طرفداران پهلوی به خونه علی کریمی حمله کردن و کتکش زدن
🔴
اولین فیلم از دوربین مداربسته منتشر شد
🚨
🚨
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144356" target="_blank">📅 10:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
استیون میلر، مشاور کاخ سفید مدعی شد: آنچه ترامپ در ایران به دست آورد، بزرگترین دستاورد نظامی در تاریخ جنگ‌های مدرن است
🔴
مین‌های ایرانی در خطوط کشتیرانی بین‌المللی در تنگه هرمز خنثی شده‌اند.
🔴
تقریباً ۱۵۰۰ کشتی حامل ۷۵۰ میلیون بشکه نفت تحت حفاظت ایالات متحده از تنگه هرمز عبور کرده‌اند.
🔴
ایران از زمان از سرگیری تحریم در ماه گذشته، هیچ نفتی از سواحل خود صادر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144355" target="_blank">📅 10:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866482ed98.mp4?token=IgtW92tX7mjcHcjPL1aSalpQRqXEjFL8NxskPFVV9pIzilEX_7C_fPQWcJX8JzUUlRPgpxflDjQmCPiUVtnLPRefJHASy58XhhRnONCjwp_u27yjjqhgoLEeeov3Iw2a31pqsdPDTN2EokCNyKmV7IVNYlWOa0AaVYhSFz9D129hBsqPvHue5JU6aAo9NxvD0w5xkeNSNFexr5nuZczQf7ZXCKkZLttNQvmwz_sd_H7IDZTjf7cChHCE1iGu3oIX3zvQwSfc2p4SNkoD8PAKW059ay0_cUTx15HkvzkuEN-4OCIjjfjaCY4Ss71MD1xLWhnY5cMUsAB77TkXe8vqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866482ed98.mp4?token=IgtW92tX7mjcHcjPL1aSalpQRqXEjFL8NxskPFVV9pIzilEX_7C_fPQWcJX8JzUUlRPgpxflDjQmCPiUVtnLPRefJHASy58XhhRnONCjwp_u27yjjqhgoLEeeov3Iw2a31pqsdPDTN2EokCNyKmV7IVNYlWOa0AaVYhSFz9D129hBsqPvHue5JU6aAo9NxvD0w5xkeNSNFexr5nuZczQf7ZXCKkZLttNQvmwz_sd_H7IDZTjf7cChHCE1iGu3oIX3zvQwSfc2p4SNkoD8PAKW059ay0_cUTx15HkvzkuEN-4OCIjjfjaCY4Ss71MD1xLWhnY5cMUsAB77TkXe8vqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: در صدا و سیما می‌گویند تورم آمریکا ۲ درصد بالا رفته، تورم ایران که ۱۰۰% رفته بالا
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144354" target="_blank">📅 10:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در جنوب اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/144353" target="_blank">📅 10:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNu1hJQjV2mZrueH-8vOOsx8wwwl_dHwaieiSGM7Gacue90CvmN_52aS8GqMufvAP5yxy-eGHqDpGPdeUy02CSqkQn_PmzvaJLQhdwAfa8UhOBv3yKsUErKM92fEY5C7jDpE6cL2BJYKYON9RfegaXBjd0O87UmXKqyPYaAKxsa4617QAQLIKxZNIV7szhXpc1o0ipNuoQYAOBtVU4Bbv4XkxuxQYkmO-xN_InPohBblZchaPvj_gKH9TORNTCPs4gpI6nIvQ8XeD6TU7hGBYDq9zVShYyMKd7_cheq3i48X8rtcP3RHU5D01UUY866iLP261E54_L9vvzMgXdbMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف ۵۰ تن تخم مرغ احتکار شده در قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144352" target="_blank">📅 10:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFJvbs8cYSgmxrUvxR8T7KSwsSYsiNeS_RsA_ofSVCguuj9m2co9AUEb9x7HrrClDV8_JbKWjpq3YjRJikEpjNrNMQzX6YLf42ibZqwaLEB_-jJ_GEI3RrE_rVzeccdUwiq26CInqqdcjMBnb3aCEFbJdKS1lDH-IN-ms-95g4wHlpDUxQsbwlvMJGMel4qA8_5cXKPnuKyeDVJEYbQ8QV_Ozl2ry74H-kUUOdzRmcCiOYvQhKvh1iP5bs0spLFHwGmZxHI_bg2jAauxjm8FOvHMJ1inQ1u77pXWTMI3OP_6CyPOdjB-4JGc5jXznmX3QPVi1F7MdflrppWYAfdZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گلوله‌باران توپخانه‌ای اسرائیل شهرک
حاریس
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144351" target="_blank">📅 10:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
روزنامه معاریو به نقل از منبع سیاسی:
نتانیاهو در قبال لبنان با احتیاط رفتار می‌کند تا ترامپ را خشمگین نکند
🔴
یک منبع سیاسی گفت: بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در قبال لبنان با احتیاط رفتار می‌کند تا دونالد ترامپ، رئیس‌جمهور آمریکا، را خشمگین نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144350" target="_blank">📅 09:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به میانجی‌ها گفت هیچ علاقه‌ای به بازگشت به تفاهم‌نامه اسلام‌آباد ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144349" target="_blank">📅 09:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdUF3kgN6uw9o2wjO5qhQDJsCroe8nhTmJ4UIWmDdijXDkNlVxgJyfCzQGygsu1kTlmcqQf2TfKAaS1y6gg4nlLAFQdebtBV2oZg01RHcfsn_bfPgjnMcih6ZAHr5bR9HxD_vdoGxGTdYnSyZOOzKJKhlJA2clIEN6OUnJeXxJEfccQTTutAIwSUfOn2QHshhucwY64uCZOHm6xybbpEOtqCytUcM1rlXmsCFhSnrNuvdZY7PEDYfvqJZi0J7teUpogDCvYeI8LFLcqkVr7MNC-l0iyTDqe1JsI--HnwiSFvBYU5vBhZYwyK6RAypAtqAZsX5rv_CvvUK9rQdiRGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به کاخ ریاست‌جمهوری و فرودگاه پایتخت نیجر
🔴
منابع امنیتی از شنیده شدن صدای تیراندازی و انفجارهای پی‌درپی در نقاط مختلف نیامی، پایتخت نیجر، خبر دادند و اعلام کردند افراد مسلح به فرودگاه بین‌المللی دیوری هامانی حمله کرده و تلاش کرده‌اند حلقه امنیتی اطراف کاخ ریاست‌جمهوری را بشکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144348" target="_blank">📅 09:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144347">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bcdfad7d.mp4?token=hZuX1aa0Ii6MpSo0cEiE2d8oOp53_BiWbT1jTf78G7n77blnPIJKLmOmwMLPqQZ7_hC4k7ZRMO7GeC-KjvZmdHRgLkDdcYPBNkhzmz0Gc1Bev-6C8dVKC_SMllLvaUeFFV8upfjsgj5JHxQfNiYsjBhT64TNnh2nRt9Q_TAFwyIhvkUZoFxrwliQ4qyHA9S7AeIwa4qTrCmE07-GIwBBhOMoSF3imRZfL4CLXt6_Jxem2atnbMn15OuLxFHJ8q5rxVklA3wSqdlEV1TLgE99tcZa6kA1IKIZWKtvDw5EBfvRbcYUv740bV-fPAoxjxJzVqF9tf2GZQi038TQluu73Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bcdfad7d.mp4?token=hZuX1aa0Ii6MpSo0cEiE2d8oOp53_BiWbT1jTf78G7n77blnPIJKLmOmwMLPqQZ7_hC4k7ZRMO7GeC-KjvZmdHRgLkDdcYPBNkhzmz0Gc1Bev-6C8dVKC_SMllLvaUeFFV8upfjsgj5JHxQfNiYsjBhT64TNnh2nRt9Q_TAFwyIhvkUZoFxrwliQ4qyHA9S7AeIwa4qTrCmE07-GIwBBhOMoSF3imRZfL4CLXt6_Jxem2atnbMn15OuLxFHJ8q5rxVklA3wSqdlEV1TLgE99tcZa6kA1IKIZWKtvDw5EBfvRbcYUv740bV-fPAoxjxJzVqF9tf2GZQi038TQluu73Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط بالگرد بلک‌هاوک در مکزیک
🔴
یک فروند بالگرد نظامی بلک‌هاوک در مکزیک سقوط کرد و هر ۷ خدمه آن زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144347" target="_blank">📅 09:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144346">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رسانه‌های لبنانی از حمله توپخانه ای اسرائیل به شهرک «حاریص» در جنوب لبنان خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144346" target="_blank">📅 09:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144345">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfsgtUFCR7efaS2pAMKPmS5TI0eHYGMe_szuqZ8Q0Y6BQQTSMGvViouTGYqB32u-X9htaIV1KItc1oPTYWhr7Nc3a8Dgs46c0rDa216BkL9saaV5gWhAz9lyD_LRiBu4mdgxKl_zVT5GNAVXv81yFueac8D_-8cqVIMuA4D878ZwnTyusDVln2gQvKq-yEAQKqE0sJWQ_mIC1_yrf1Ett0sm7orU9S7TWpYj4E2WzBzoas3H4bBcFZXiokyMGoM2pMFgLJyfo0NGhcdZ33p7azW9mI0Xs7olkRD51a1WaqvYysNh5N5KefoLWZlKs7gXk8ptteOrDpL9WT5wAZ3fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز فرماندهی مرکزی آمریکا (CENTCOM) تا روز جمعه ۲۸ اوت، ۸۲ کشتی را مطابق با محاصره آمریکا تغییر مسیر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144345" target="_blank">📅 09:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فارس: ایران خارج از محاصره دریایی، نفت کافی برای تأمین بودجه سال جاری در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144344" target="_blank">📅 09:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144343">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رویترز: بحران سوخت در روسیه؛ تولید بنزین فقط ۷۰ درصد مصرف را جواب می‌دهد
🔴
دلیل کاهش تولید بنزین در روسیه، حملات پهپادی اوکراین به چند پالایشگاه بزرگ این کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144343" target="_blank">📅 09:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144342">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
بر اساس گزارش رویترز به نقل از مقامات پلیس نپال، آمار قربانیان سیل و رانش زمین اخیر در این کشور به ۶۲۶ کشته رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144342" target="_blank">📅 09:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
روزنامه دنیای اقتصاد نوشت: بر اساس سه سناریو، تورم نقطه به نقطه پایان سال در صورت تداوم تنش به ۹۹.۲ درصد، در سناریوی میانی به ۸۰.۳ درصد و در صورت تفاهم و تنش زدایی به ۶۱.۷ درصد میرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144341" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آموزش و پرورش: همه مدارس دولتی هیئت امنایی و دریافت شهریه ممنوع می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144340" target="_blank">📅 08:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSl_-bDbfAd3hzuaUpvG6nur5XDyjf5iIFnL_tEDp_2PIqwccZoeGfdXiSzy5a1dXNTItfvvptO_rUfTsoAiPrveaPvwWrfv5y-Cbtg6Bx31FQZnD5zFs-GVKP1S5LDs7GcIxN5pbIoZ_DbgWBmy34MoPo9Nk2NLTvqLYHcUSvPxiZL_3UNPwsz4V7OEOG4xm28wr9SN-sQtFJBhgqtRYk4MEs9FFabi-UMYHfV9rPpkHvACPHGAmjRXP_q-dsuYl30LNVhJPVv58Wc5MfkP-GwVgLlllsk6OeXZjSn7V8uUa6_YboVwav7w2ocyerPfc_Z-PYFwxsJy9e4RNF6ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری NBC
:
منابع می‌گویند پیت هگست، وزیر جنگ آمریکا، با دوستان و افراد نزدیک خود درباره احتمال نامزدی در انتخابات ریاست‌جمهوری آمریکا در سال ۲۰۲۸ صحبت کرده است.
🔴
دولت ترامپ تاکنون درباره این گزارش اظهارنظری نکرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144339" target="_blank">📅 08:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آدام شف، سناتور دموکرات از ایالت کالیفرنیا در پیامی با انتقاد از سیاست‌های جنگ‌طلبانه دونالد ترامپ رئیس جمهوری آمریکا خواستار پایان دادن به جنگ تجاوزکارانه ایالات متحده علیه ایران شد و تاکید کرد که باید به این جنگ پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/144338" target="_blank">📅 08:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس گزارش داد که پس از تخلیه در مراحل اولیه جنگ علیه ایران، روند بازگشت پرسنل دیپلماتیک ایالات متحده به خاورمیانه آغاز شده است.
🔴
دیپلمات‌ها و برخی از اعضای خانواده‌های آن‌ها در حال بازگشت به سفارتخانه‌های آمریکا در کشورهای منطقه هستند.
🔴
وزارت امور خارجه آمریکا محدودیت‌های مربوط به حضور پرسنل را در برخی بخش‌ها کاهش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/144337" target="_blank">📅 08:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روزنامه وال‌استریت‌ژورنال به نقل از مقامات آمریکایی مدعی شد  واشنگتن با سرعت اقدام به انتقال مقادیر عظیمی از مهمات و ذخایر نظامی به منطقه خاورمیانه کرده است.
🔴
طبق گزارش این روزنامه، هدف اصلی از این انتقال گسترده ذخایر نظامی، آمادگی برای مقابله با تهدیدات احتمالی ناشی از ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/144336" target="_blank">📅 08:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jismIL6g1grKOwdqXhRCTs06ci_hMURLMVmV8ulswPnAL6Q7Ox9QgmexDe9p7wFc3v-EiVvQSP5zxgJSwhmMEuPFC99CeEhxmMWCXIYrID7zzPY3-payDp8EtWlQx2ufd06Y1s9adv5lpawB_hpHVNW9uUTOKy-Mms6rFtlw4Zpvm0y4coc3xdOTP7TxE394yN8Q-ccoKURhRILviuyg8rCJ-MBwto6f8jpkhn6kg_WZZP0_iYf6-6MeMQ48U8y1Vh0jIvjhlUh8RyHvSdX1MrJG9jleoiOAVJ9_dH5fgsB1Kj2J8Mu0b1OwEpI__O2blh4LjcNNMx5Yyg4eupXUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: همین الان توافق‌نامه‌ای با ونزوئلا امضا کردیم که بزرگ‌ترین قرارداد نفتی در تاریخ جهان است
🔴
وزیران خارجه و جنگ در تأمین دسترسی ما به بیش از ۶۵ میلیارد بشکه از ذخایر نفتی ونزوئلا موفق شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/144335" target="_blank">📅 08:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
العربیه گزارش می دهد که گروه های عراقی در حال برنامه ریزی برای هدف قرار دادن عربستان سعودی در ساعات آینده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/144334" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144333">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAoF2oWiNgyCWjfa2ZrySVpzr8T7noDi6H0X536CJhsG3HFPMNLxq3QumxLTqgKIiOetoNK6sSqq9ELE7DdgnSu__FKtWZ9F6ZWECje8I169kGZ_P5KiARguX8DJw98Qqq91Eo5BZW-5Zehq-B5Sk3Dr-Xm6ib0aDt0u2W453ET1qJBuaupC-1k2-qRjcLDwtuUsS0nkAXCPB_0h7FJC5zDe84N5uAqo0Zq6NLeMmE6el_ux-0J2ZiFA_hcVGZxQKKiMAbc0NuWcju7sJKQvaQSyFPW0HgR2QhOdPRxAUatEDdujef2DO5oy7Ta93Pfcwadfi0EdUltqgSELz82u1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/144333" target="_blank">📅 01:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144332">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، محله "دواها" در شهر "کفر رومان" واقع در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/144332" target="_blank">📅 01:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144331">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iawpROs6zYIYVRJKbAgqyd9MOovCsOCJMfcAhKM2sy-ruoOagqHGTBY_zvFDvsiDSnQfV2mcuJiHgSvmFG2TSM6Rls8AjzajSFV2Gd_kXzcLlATmfVJcHT8VRAc3mw28MI7PM83tXt1_HZ0YG7ducz2o-9arCFDL2l9gnJqGqzeY6iB6o5Sqsjfx1_r4Pj3nfl6_8xoofZiHvxc6LFi_3iRk8J59IKvg2RC0S2xUOfow0MapFyukkf_iy9vHwvJGO0YRAoptrscOmXo2xt2-tA6QPU6RYYYgtU72Ni3kfaVzPU_7YrssXTMREkBZWdxkK0Yu8OII-teRO1HWFGfiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: گرونی چیه بابا فقط انتقام رهبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/144331" target="_blank">📅 01:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_sKby5Nx617oe76IJBwZ8JTva-tXNdVG8AlR8v3N0U_AAFBQ0UGyhDrVJIo1SDThhR7I5X3FkN7Xq1k6ejIB-Jz_e2lYxlz5aDHuOFsqcZN6t21uZA_imKlELUTixMGg6fp0f4hsjnjz8HxGMl-EZDj2vIjYTCgYzZhV5yddeqESry-vnYOfZoo7QqS_iDwkOGagwkVZgoPBMSTJfmgZwS8HbHVRseiCBvVzN1mNsdAahch4D7D2Vnry21jjKNLuwsZCGy1KTdGGtlKq-BEyMC3Pb2ti5toJmLVZJJX0Nj2A12aRGuPGszOGWN28GWTAPX7LeNgsLG3F-o-K9MLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/طرفداران پهلوی به خونه علی کریمی حمله کردن و کتکش زدن
🔴
اولین فیلم از دوربین مداربسته منتشر شد
🚨
🚨
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/144330" target="_blank">📅 01:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZjNV5cxqv7JYqcTSMFuEGRk0DkvIapjn3u9ipIkeNFVdqHJZDXBtAwRjhKCogSpGdoitTHynqQdr8LTjtaB_bab_SmHVumxwHYIi_EveG6MiyGLcJcXu2vfWx0OF0JECpQn-CJRncDr6UW1VbAv9x8KRKB8cVgaaoKX9D05HyAqmyVLFbUB1W7u0zvq6esjEPasHNNbpIr9UpKbN8WKK_DVr6t_k9k7UC-ASrKMjKif6oo9TnRCbmGuWtG7Td9ZMakDwPdxMCivJ_dz6_5Olpro7OaiYnJ0eimg4R2h7VWWJwMbcTjyq-SSzC3yYWLzku2f-2MHR8YKZ6N2ohInng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: پول نداریم، بدبختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/144329" target="_blank">📅 01:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/144328" target="_blank">📅 01:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بی‌بی‌سی: آمریکا در حال برنامه‌ریزی برای قطع کمک‌های نظامی به نیروهای پیشمرگه، که متحد اصلی آن در خاورمیانه است، است. وزارت دفاع آمریکا به رهبران اقلیم کردستان عراق اطلاع داده است که برنامه‌ای برای تمدید توافقنامه ارائه کمک‌های امنیتی به نیروهای پیشمرگه کرد ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/144327" target="_blank">📅 00:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
باراک راوید: بیش از ۲۰۰ شیء شبیه مین از مسیر اصلی تنگه هرمز جمع‌آوری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/144326" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=STK_oBYvh1C4A-iciMXT4JUhMMZrAGSOf25hlV4fFLFiiFaEnk_9_LBPVwWlT2hEyL1aaz0y5OmCoDb1mvcQm7wfxQE5mBCXK27079AGDRspgek9m6A_9VkhZVQqNcSNF7CYHzZIbles8w2Dr221oid6CpcB2bvtnqAwCEMGP-jOt6YsVuiDpgh9ERxqo_dsIIXFJFYB-zqIqqh3rHyQNKTqWY5JD51BvfhQ4Lrc2yMcg6Gl_MsidQynxVBmGhcTjvzQMt1TXGQ-Vb9cbl3dJrPF-rSajMma5HQlt2sWJevdRsIL-9Er3UJ_AjVXmotT5cci7I678tPdLdNTS9xUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=STK_oBYvh1C4A-iciMXT4JUhMMZrAGSOf25hlV4fFLFiiFaEnk_9_LBPVwWlT2hEyL1aaz0y5OmCoDb1mvcQm7wfxQE5mBCXK27079AGDRspgek9m6A_9VkhZVQqNcSNF7CYHzZIbles8w2Dr221oid6CpcB2bvtnqAwCEMGP-jOt6YsVuiDpgh9ERxqo_dsIIXFJFYB-zqIqqh3rHyQNKTqWY5JD51BvfhQ4Lrc2yMcg6Gl_MsidQynxVBmGhcTjvzQMt1TXGQ-Vb9cbl3dJrPF-rSajMma5HQlt2sWJevdRsIL-9Er3UJ_AjVXmotT5cci7I678tPdLdNTS9xUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: به دنبال این هستیم که برخی از ادارات را دورکار کنیم
🔴
حقوق پرسنل را کم نمی‌کنیم اما مصرف سوخت و انرژی ما کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/144325" target="_blank">📅 00:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کی‌یف بیش از دو روز است که تحت بمباران مداوم قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/144324" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144323">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/144323" target="_blank">📅 00:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
پزشکیان: با آمدن محسن رضایی، در حال نزدیک شدن به یک زبان مشترک در دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/144322" target="_blank">📅 23:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144318">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-JbjFCFchBjABKZPVzp3c_eQQGhXf0IkEOTwyUFSfVliT5Q5QUIF9TKXRwW-H4ESWKba9w3EWq5pRyfc0ax5BA7cqd7tTy4jrQzSO1aaWJBGLB-CQ11vl5_tBq_g-77dR_EszBgOifElxIgLrrcP-iU6QyxhhDV3Y2jUtWCzgzLW768dSCPfRYU9JmHaMZh0SloUG-S4yLsDU3ZJvJOAu4jdLYnGQJFRxeaNQ5hXcydSq4nP5xjbDz3Ja00o2wf1LlO5bVHV7fPYuODleyvGRqCU4fMLjgIPihUhJhkMmbKgr4Z5QZkx9FVDfGu7NLRFf752HBMzmCd12Ur-hCOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f256f6aba.mp4?token=aZQOLmVJYmrKEtUBlMjyrevVM6tZcdVL_-1KU8XjHmTdQhkRMCPRbqFJEpCjgeFaxjbVCD3qdKREfa2y_wLmo-b9rG8CJzsLkkxd02tP1Vn1pc60D0Ae1_J8q8ip-t8vKm70igxTM1Pr1PB4nV99gaP_F_Dtk0yTI0E3N8TqBVVDzZn-00lsBeRMDS9cmEdYVlTWKUByNfEZrJi6IqXGn3WBDeQYeK1DXNaQEP-gKrPwaMU6vE6s2WOWSnN0N9ZK1IHOkZDURe0VIkeUWc5qdWLREMzKJNt9CMUpY2qJO2oBcSJg1ZeiNIyREpLtnSLxicnhNJLf6IKu__QOEA4XZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f256f6aba.mp4?token=aZQOLmVJYmrKEtUBlMjyrevVM6tZcdVL_-1KU8XjHmTdQhkRMCPRbqFJEpCjgeFaxjbVCD3qdKREfa2y_wLmo-b9rG8CJzsLkkxd02tP1Vn1pc60D0Ae1_J8q8ip-t8vKm70igxTM1Pr1PB4nV99gaP_F_Dtk0yTI0E3N8TqBVVDzZn-00lsBeRMDS9cmEdYVlTWKUByNfEZrJi6IqXGn3WBDeQYeK1DXNaQEP-gKrPwaMU6vE6s2WOWSnN0N9ZK1IHOkZDURe0VIkeUWc5qdWLREMzKJNt9CMUpY2qJO2oBcSJg1ZeiNIyREpLtnSLxicnhNJLf6IKu__QOEA4XZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انفجار بزرگ در کی‌یف، در نزدیکی بزرگراه ژیتومیر، پس از حمله روسیه به یک انبار مهمات اوکراینی رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/144318" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144317">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان: بنابرقولی که داده بودیم، باید مبلغ کالابرگ را متناسب با افزایش نرخ ارز افزایش می‌دادیم، اما نتوانستیم این کار را انجام دهیم. در این زمینه از مردم عزیزمان شرمنده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144317" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144316">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a29fb5c7c.mp4?token=MM-iSo6sB0XEh9UMqtIo6ZNkr9iniv5QbCu-D3cfr4ruv0Chf-mSouwirqZQBdx6ZubfKO4qvziS_LO6gRdfigkneObJdojyXwMKM_1ft3fqUF1krTQOZFgAza5S45ttTuIcD5HMr_PtZfZJAp9rQyJpDecwxEqH-WWl3kt6mSHhz316HSP1nB1r2aiTSsBDDDSuCOX8pWPGqg3iM9N3CdQbHN61ywIbSOnqQ8pskPCTjG5zUl7KoRsyoOYRuX5YxeEuw4h9WY9ETME4ZfA3-Kq3wkmZN-OxZXXnD9WE6FFeq8yUNc66lqps25_wt7GXoViXNtDEM7PEifIrm1Pleg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a29fb5c7c.mp4?token=MM-iSo6sB0XEh9UMqtIo6ZNkr9iniv5QbCu-D3cfr4ruv0Chf-mSouwirqZQBdx6ZubfKO4qvziS_LO6gRdfigkneObJdojyXwMKM_1ft3fqUF1krTQOZFgAza5S45ttTuIcD5HMr_PtZfZJAp9rQyJpDecwxEqH-WWl3kt6mSHhz316HSP1nB1r2aiTSsBDDDSuCOX8pWPGqg3iM9N3CdQbHN61ywIbSOnqQ8pskPCTjG5zUl7KoRsyoOYRuX5YxeEuw4h9WY9ETME4ZfA3-Kq3wkmZN-OxZXXnD9WE6FFeq8yUNc66lqps25_wt7GXoViXNtDEM7PEifIrm1Pleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: واقعیت اینه که ما پول نداریم، درآمدمون هم که مشخصه، کمتر شده بیشتر نشده، مشکلاتمون هم بیشتر شده، در ضمن باید جواب هم پس بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/144316" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پزشکیان: افرادی که دستی بر آتش ندارند، تحلیل‌هایشان در جیبشان بگذارند
‏
🔴
طرح نمی‌خواهم؛ اگر کسی می‌تواند مشکلات را با شرایط موجود حل کند، به او اختیار می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/144315" target="_blank">📅 23:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
عراقچی: به جهان نشان دادیم که آمریکا و اسرائیل قادر به مقابله با موشک‌های ما نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/144314" target="_blank">📅 23:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رئیس‌جمهور: اگر به تعهدات عمل نکنند، به مذاکرات ادامه نخواهیم داد اما نباید نگاه صفر و صدی داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/144313" target="_blank">📅 23:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان: در زمان اجرای تفاهم‌نامه اسلام‌آباد توانستیم به میزان کافی نفت صادر کنیم
🔴
نزدیک به ۹۰ میلیون بشکه را در همان مدت کوتاه صادر کردیم
🔴
من معتقدم اگر در داخل افرادی که دستی در آتش ندارند، تحلیل‌هایشان را در جیب خودشان بگذارند می‌توانیم به صلح نزدیک‌تر شویم
🔴
می‌گویند تحریم‌ها اصلاً تأثیری ندارد و مشکل فقط از مدیریت ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/144312" target="_blank">📅 23:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144310">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پزشکیان درباره قیمت ۱۰۰ هزار تومانی بزنین در کرمان که متوقف شد: باید طرح‌های مختلفی داشته باشیم اما اگر طرحی شکست خورد باید این توانایی را داشته باشیم که نسخه خودمان را تغییر بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/144310" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144309">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
پزشکیان: مسیرها بسته است؛ کالا وارد نمی‌شود و یکی از این کالاها بنزین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/144309" target="_blank">📅 22:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144308">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=lKkF4fEXSalv3J7-hV4VtVzOGv4FmTfm9hIZJMw9WTDlhtuesUIxOcSC088G3lJRi7fAco-fB0H_JdDNuRcXFzBjp9bB6HYug7VDsKHDwvVd8lF16ccewOPQdU9Wt5SH8D2XqiALsUl7YEGbpcLsRjZKbSDiBuer7-FMbYDrxpufNEs1mgvkzAg9HlpAcHuWdPPF26TTLwmhNlnulHeq5w4Oqn052lClrB5iVqQ_AiMtQlvz1DqMjJrQqiJiL4gxiCLNrJxRSqrDTXEYbhptMYBI4nJE0tIhYR5PkI1Rgb_3JiLsLHqihkA6tKtdDlHg5Oy150UIXxrrlbQNbx5SQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=lKkF4fEXSalv3J7-hV4VtVzOGv4FmTfm9hIZJMw9WTDlhtuesUIxOcSC088G3lJRi7fAco-fB0H_JdDNuRcXFzBjp9bB6HYug7VDsKHDwvVd8lF16ccewOPQdU9Wt5SH8D2XqiALsUl7YEGbpcLsRjZKbSDiBuer7-FMbYDrxpufNEs1mgvkzAg9HlpAcHuWdPPF26TTLwmhNlnulHeq5w4Oqn052lClrB5iVqQ_AiMtQlvz1DqMjJrQqiJiL4gxiCLNrJxRSqrDTXEYbhptMYBI4nJE0tIhYR5PkI1Rgb_3JiLsLHqihkA6tKtdDlHg5Oy150UIXxrrlbQNbx5SQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید. نرخ سوم قیمت بنزین بیش از ۱۰ هزار تومان نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/144308" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144307">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان: در روند گفت وگوهای فعلی، نقشه‌راهی برای عبور از تنگه هرمز تدوین شده که توسط برادران ما در سپاه پاسداران، نیروهای نظامی و تیم مذاکره‌کننده به استحضار آیت الله خامنه و مورد توافق قرار گرفته است.
🔴
عمانی‌ها در ابتدا همراهی کردند، سپس ملاحظاتی داشتند، اما در دیدار پریروز، مجدداً به تفاهم رسیدیم و پذیرفتند که مسیر بر اساس نقشه هماهنگ‌شده بازگشایی شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/144307" target="_blank">📅 22:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144306">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پزشکیان: ما داریم تلاش می‌کنیم از حرف‌های تفرقه انگیز پرهیز کنیم. شما خیلی راحت می‌توانید بدی‌های من را ببینید و نقد کنید. چرا خوبی‌های هم را نبینیم.
🔴
چرا باید هر روز شما عیب من را ببینید و من هم همین‌کار را بکنم و روز به روز این شکاف بیشتر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/144306" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144305">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پزشکیان: اگر آمریکا تعهدات خود در زمینه رفع تحریم و محاصره و آزادسازی دارایی‌ها را انجام دهد، سرمایه‌گذاری را شروع کند و جنگ در لبنان را تمام کند ماهم تنگه هرمز را باز می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144305" target="_blank">📅 22:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144304">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
طبق گزارش گلدمن ساکس، جریان نفت خام از طریق تنگه هرمز تقریباً به دو سوم سطح قبل از جنگ بازگشته است و تأثیر جنگ ایران بر قیمت جهانی نفت را به حداقل رسانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/144304" target="_blank">📅 22:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144303">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8f9c4ae0.mp4?token=q_CtCyivoAfM2uYeJM61JBbBur2gYKdFUCajxjwmqdDciAMmQRwAT5I6jb_4PE7RiTtsu0vOwBBQZ5VfRWsSuHJ9K1wb_tACcGORDj6NbYnphAs7QQIKFtJCiwpZQKKA9Wo9EtA3yOAIgw_SZkJm315Oa6G3NpHwMNZRV2ph7sd9iIgfiMz0bKAKBoGxwjF6wWt4EMxyIfQtJqcMiloxa506b8cCI3_DiN_fONuaCQuOf0mA49mR7G_CBR4HjNbc9Txlb6XB2SeQzSHenM32L3jXx3dQYZaDd2p82_IDFmRPs41YpupubykMailU62vFgMcsQQ7Lw3MIcOcig5M-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8f9c4ae0.mp4?token=q_CtCyivoAfM2uYeJM61JBbBur2gYKdFUCajxjwmqdDciAMmQRwAT5I6jb_4PE7RiTtsu0vOwBBQZ5VfRWsSuHJ9K1wb_tACcGORDj6NbYnphAs7QQIKFtJCiwpZQKKA9Wo9EtA3yOAIgw_SZkJm315Oa6G3NpHwMNZRV2ph7sd9iIgfiMz0bKAKBoGxwjF6wWt4EMxyIfQtJqcMiloxa506b8cCI3_DiN_fONuaCQuOf0mA49mR7G_CBR4HjNbc9Txlb6XB2SeQzSHenM32L3jXx3dQYZaDd2p82_IDFmRPs41YpupubykMailU62vFgMcsQQ7Lw3MIcOcig5M-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
عراقچی: تلاش کردند که آتش موشک‌های ما را خاموش کنند، اما نتوانستند، نهایتاً چاره‌ای پیدا نکردند جز اینکه تقاضای مذاکره بکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/144303" target="_blank">📅 22:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144302">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیوزویک: جنگ‌های ایران و اوکراین، افسانه بازدارندگی هسته‌ای را به چالش کشیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/144302" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144301">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
به دلیل تحریم های جدید آمریکا علیه ایران، بانک مرکزی عراق تعاملات 14 فرد و 19 شرکت فعال در زمینه‌های نفت، تجارت و حمل‌ونقل را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/144301" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8YDAWkBb0aHhWSKmOnqpLYb7kNccjICSxDYtK9vqBmelDCgoXfjplQu6KwiPNAnNK0CsjB7KFhvggr_UT1uL57tuugxGyXAmnfAsGT3u3Mh4-6syagxHenTJJHRgIqHsaNlILo7qoj05Bb3eJq4htLXcFRypfLTR3MmIGW4iffsAJh6FuhOw_M8znLGe7uPU2e9sRIsKt1YeQY5r1OjA1_lAVaEPBBOkUzjVRnMpMiz14a661kFCn35qfcEatnbgm6NKmhTEyM6pPRdWE1EVDPuQAeJg_yaEj7ismrV_wNPVs9pRnsq9CuP3PWxYBkgk34mt9rssHYl_uNDo6IYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش وال‌استریت ژورنال، پیتر هگ‌ست، وزیر جنگ، در حال بررسی امکان بازگرداندن صدها مقام ارشد نظامی ایالات متحده به پایگاه کوانتیکو برای یک سخنرانی دیگر است.
🔴
به احتمال زیاد، این جلسه بر اولویت‌های او، از جمله استانداردهای سخت‌گیرانه‌تر آمادگی جسمانی و آراستگی، آمادگی بیشتر برای نبرد و تغییرات بیشتر در سیاست‌های پنتاگون، تأکید خواهد کرد. این در حالی است که سال گذشته، یک گردهمایی غیرمنتظره از ژنرال‌ها و دریاسالادها برگزار شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/144300" target="_blank">📅 21:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: افراد و نهادهایی را که از طرف ایران به فعالیت‌های مالی غیرقانونی مبادرت می‌کنند، هدف قرار خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/144299" target="_blank">📅 21:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
شنیده شدن صدای انفجاری مهیب در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/144298" target="_blank">📅 21:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMoXHNKFvXUGAAO4V3i8l8ghkF1Tz4Ha6FHSbUwbil5CAY62D9NV7rr6RHuC4pwHUrbdCA6x3D0bP7-CmkFalJzVY2kFBwvd6C-m3U--7xPqICHSWPe943bPz1f9TO4KfqMTJTUgHW3ee6mryE-BCXJbUNv3YYeUDib_RvnHVjv3XpuY05-tx8Co38_vS_4yVP6iKvK95nNPgNX8S4zrKpZhImVOeTLzSNhDkeQ3hOizxpJUMMYlIolYquTZ35xrim_VEIHKw7-FapOb2FuJRxkFALaHcoIJmkuKXbVSm-HQB3FVMyZPMUEam8_rtW00Zehui-cqyJkLTGHrAbCFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۸۸ دلار
✅
@AloNewd</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/144297" target="_blank">📅 21:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
توانیر: کاهش ۵۳ درصدی قطعی برق در تابستان امسال
🔴
هدف نهایی این است که در تابستان آینده، پرونده قطعی برق به‌طور کامل بسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/144296" target="_blank">📅 21:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: عملیات موفقیت‌آمیز ترور رهبر حماس در اردوگاه جنین
🔴
ارتش مانند بقیه اردوگاه‌های کرانه باختری، به طور دائم در این اردوگاه حضور دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/144295" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144294">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بیانیه ایت الله مجتبی خامنه ای: از رئیس جمهور و دولتش بخاطر زحماتش تشکر میکنم، بیان دلسوزانه ی مشکلات کشور باعث میشه دشمن روحیه بگیره پس باید حواسمون باشه هم چنین مردم جانانه ایستادن و باید در شأن و منزلتشون مسولین بهشون خدمت کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/144294" target="_blank">📅 21:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: رویای آمریکایی بازگشت. فکر می‌کنم این بار قوی‌تر از همیشه بازگشته است.
🔴
ما در حال حاضر عالی عمل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/144293" target="_blank">📅 21:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144292">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: می‌بینید که چقدر خوب می‌جنگیم. ما بسیار خوب می‌جنگیم.
🔴
به ونزوئلا نگاه کنید. ۴۸ دقیقه.
🔴
راستش را بخواهید، با آن افرادی که پشت سرم هستند صحبت کردن را دوست ندارم.
🔴
ظاهر آنها خیلی خوب به نظر می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/144292" target="_blank">📅 20:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144291">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b86a38e6.mp4?token=HaAc1zTvWsOLnhbYtqR5NcGwxcJSOU2zfXbT7RSVpN9zj1MWons5hHrQsNCLZJiU_-t24npqU4P0n_GTFSqKxccs49gn2ZMwlDOgpW0A-RW96CY7SDN4RnlYIY6tyzbHTvFe1UYYuTsd8ZtVRAzZrc3s8IzXVCB0xiLYQILKkWLMSWHUIX4HoN6uRv69upGSk67XQt1FP5F6VKDXHq4f0ABigmQcIrcj-OfubHXZ0PCW8k9MDXG33uQNKtYsUi_uHqZyUj_1KGGqw1MYj5arahBUMVilA80eGBxJhc79GzLQQmEIGNh-1jb2gZ8joKtKB0z6SmdQsWVTWZoJlAy9AjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b86a38e6.mp4?token=HaAc1zTvWsOLnhbYtqR5NcGwxcJSOU2zfXbT7RSVpN9zj1MWons5hHrQsNCLZJiU_-t24npqU4P0n_GTFSqKxccs49gn2ZMwlDOgpW0A-RW96CY7SDN4RnlYIY6tyzbHTvFe1UYYuTsd8ZtVRAzZrc3s8IzXVCB0xiLYQILKkWLMSWHUIX4HoN6uRv69upGSk67XQt1FP5F6VKDXHq4f0ABigmQcIrcj-OfubHXZ0PCW8k9MDXG33uQNKtYsUi_uHqZyUj_1KGGqw1MYj5arahBUMVilA80eGBxJhc79GzLQQmEIGNh-1jb2gZ8joKtKB0z6SmdQsWVTWZoJlAy9AjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره فضا: از نظر ژنتیکی، من به آن چیزها باور دارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/144291" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61032aae6.mp4?token=A_yXvrSixEAuZRH0-b8O_3O4zpeohdGx77lB4YafZBWTa9O_w9yLgREI_Y8jsvXun30Q20hILX0qYQoSKSm4YwXdGXQx58qeCqIt0G2AsZMSZZ_hhcrfzPdh9YMNIRMRPqel6SscFAT6FlsRPLHuO2hGvMLRfUAL14l_RdwpmKVcJnPfKI7_3sH_c7rLLF6A6I2weDu59md-8_r9Bx50QHg0cY4Rn6kXXGukTS_4zMd0snHgM4KEk_yvBHld_ZLOANFkYKzNH0HjW8pTxZYrFC7dMiAA8BH9ZrJna7k39I9Ku_Qsc1GauYpUi3pa0I3jAWecZgf-YgD-qoPqRw3j6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61032aae6.mp4?token=A_yXvrSixEAuZRH0-b8O_3O4zpeohdGx77lB4YafZBWTa9O_w9yLgREI_Y8jsvXun30Q20hILX0qYQoSKSm4YwXdGXQx58qeCqIt0G2AsZMSZZ_hhcrfzPdh9YMNIRMRPqel6SscFAT6FlsRPLHuO2hGvMLRfUAL14l_RdwpmKVcJnPfKI7_3sH_c7rLLF6A6I2weDu59md-8_r9Bx50QHg0cY4Rn6kXXGukTS_4zMd0snHgM4KEk_yvBHld_ZLOANFkYKzNH0HjW8pTxZYrFC7dMiAA8BH9ZrJna7k39I9Ku_Qsc1GauYpUi3pa0I3jAWecZgf-YgD-qoPqRw3j6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
در دوران اوباما، توانایی ارسال فضانوردان به مدار را از دست دادیم.
🔴
ما هیچ توانایی‌ای در فضا نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/144290" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
دستیار رئیس‌جمهور روسیه: پوتین دوشنبه ۱۰ شهریور ۱۴۰۵ با مسعود پزشکیان دیدار و گفت‌وگو خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/144289" target="_blank">📅 20:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e59767ff6.mp4?token=MC3sYcKkCOAIWtZ8RZmQ51jNnzfjckCPddOXbkF5nnx7DQCp1RmXozxcazZ73ado9Yoko1O5RhSf0E5Cuvs_TlPKQIBGv2Zy_qXyfFSzLImD2Co1nIXeogRYmKJBSJEFkx-FUY0HR2YOpS4W4cx6xJCJobiNEjO6C0vOKUlwWLtUE3k0oUmKQjEhC430ror0e7ILdacZQ4YICdJfMVhK635cLdPxXFR4oYR6ifNifkppJVI_NAVLxZBLsFxU7LrsCtLJmdXyofqWYAgdy4shL3DC51VeUG4omu8CwmSAdCu5tDLwwdmtXX-yqrRAb6rG1J_tbXS8J9f9wAWqF73wEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e59767ff6.mp4?token=MC3sYcKkCOAIWtZ8RZmQ51jNnzfjckCPddOXbkF5nnx7DQCp1RmXozxcazZ73ado9Yoko1O5RhSf0E5Cuvs_TlPKQIBGv2Zy_qXyfFSzLImD2Co1nIXeogRYmKJBSJEFkx-FUY0HR2YOpS4W4cx6xJCJobiNEjO6C0vOKUlwWLtUE3k0oUmKQjEhC430ror0e7ILdacZQ4YICdJfMVhK635cLdPxXFR4oYR6ifNifkppJVI_NAVLxZBLsFxU7LrsCtLJmdXyofqWYAgdy4shL3DC51VeUG4omu8CwmSAdCu5tDLwwdmtXX-yqrRAb6rG1J_tbXS8J9f9wAWqF73wEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دستیابی ایران به بمب اتم یعنی پایان اسرائیل
‏
🔴
نخست‌وزیر اسرائیل: واقعیت به‌سرعت در حال تغییر است. یک قدرت افول می‌کند و قدرت دیگری ظهور می‌کند؛ مهم‌ترین قدرتی که باید ظهور کند، قدرت ماست.
‏
🔴
بمب‌های هسته‌ای در دست ایران، یعنی پایان دولت اسرائیل؛ پایان ملت یهود. ما باید این کار را انجام دهیم، چون در غیر این صورت نابود خواهیم شد. دیگر اینجا نخواهیم بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/144288" target="_blank">📅 20:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAToVNyRHk4jpcHf23FkYOBGi3n5o6FwrULdD4GTQOMS4dVT8uWYUBXFXf8L20RQMOeDqbg-elnXKK88PBw-8KsY323Yc1uCgtmLzJDI5YFu_qGBaAre1HJtf_kXiq3zse8Lr6NDCHUX1h1uzdV-CHABjh4CNMVCVqBi-pYdOJzQSffSmqWuMgI_4Q_YwdBjRWsQjErdnaSebs2UHJeozxzxGrxhydAJxmm2WvrM899QQoDC1f-j_SKE-RqeS9jGhok7MBtZldvD_3leF7WzQeNX1g22D40kuslPX5u9QIilLdRtVVPMBMuEoTy2MzNh_1H1tAm6LAccA3r9QWz0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت: وزارت خزانه‌داری قول داده است که تمام راه‌های اقتصادی را که تهران در اختیار دارد، قطع کند و در نهایت، تهدید ناشی از رژیم ایران را پایان دهد.
🔴
همچنین هشدار دادیم که کسانی که از ایران حمایت می‌کنند، نمی‌توانند به استفاده از دلار آمریکا و سیستم مالی جهانی ادامه دهند.
🔴
بانک "میصر" در امارات متحده عربی، به سختی این موضوع را درک کرد و امروز، ما اولین قدم را برای پاسخگو کردن این بانک به دلیل حمایت مداوم و فاحش آن از رژیم ایران، برمی‌داریم
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/144287" target="_blank">📅 20:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شرکت انرژی قطر تعلیق تحویل محموله‌های گاز طبیعی مایع (LNG) به شرکت ایتالیایی «ادیسون» را تا اواسط پاییز تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/144286" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
جاده چالوس از شمال به جنوب یک‌طرفه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/144285" target="_blank">📅 20:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144283">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nba11jayC_c9e4fEaOKaw31U2c4ynN4r1vBi5v8ccxwWY4iyaI3i1L71J_w9RJZxDcisM9Q7Etu0DX7GWCeN_GV33tTeo_wLnKFGr9QWelbQexfUV03FjdabJz4Vkh0zQp2YJflX574ydJlXvB1CE-RkB-Q71Wy-wzr5vMBPnP6SdNVuGBYwooK91KnHpXw-t2VTaKEn9B9f1GXhNZsCw-ARCJ3ihUKsZyl0XgnGIBoyB6V_kiBngYaQssBEsgERRvAyPsccIeZVJhai705ylISg9WMgOF1zZj6bfyXCyY3Tqctoyn0x82O84nCAQmzw7yKTuuGLwOnfIwXe41a3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNRDwuVRPRyWkYn6TgQO17Ufc2ON9pXLMEX5vl8xMPAhpSOL_b9d3XTMxnd7U7wutNWY798tUL-6o5u8rlSyYQJ17w9q5V8_73pvu9tEPHYACi_iCj-a2qPeBgexK5I5Lx-l4HZcHmD2CapxnY0Jlu1syV1Eab8qBimJMLRk9GNvDkh-hvNi68gE3JvPrT2uF8wVgK4UurJSbBlpgDV796VPtAPwmYWk3v3xf9cs-gypckxH5rNgJ6j-Hc5hALEzSGNm3RgBSmX8CDh9Qz0-xGDa71ruUa4JIhA72b1lqXS6gKd7vLpSsijhZHcngfc3xOAUznWw3tGrIU_gCjFJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به جنوب لبنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/144283" target="_blank">📅 20:00 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
