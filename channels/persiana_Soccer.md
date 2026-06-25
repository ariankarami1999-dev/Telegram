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
<img src="https://cdn4.telesco.pe/file/vJM0Blj1ZfLHKPSPvru6ho7JvClCvqDsL9rl70_CST0BTh_oGY_MYQDHaRV5zSg6Pi2EGW_soVY9I8NqyMV2PSRHe7IPmaKGoK_QX8wUbw_-5V-QVa-oIniKWX5Ka5_sNn8ABdi8lTgEQcBIYvXDx3BoMLS-6-vo8W5Wj2B4DdJCzHjUGgb09lMgsEyNqrahyZB9KyV5JHrE51G_kmlOlCYMrksorM0oDbcUVzS2mQPzuJcmLTCM5mOmTc385MsjMIvAwokZBi_NFKANFd8ob7rJGx4V_E6ZdTc8LkNG1oLbFpf2Twf3CHDwf6DrDGxxmtd4gPLQNhQsUbdsxiPG5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNw2gbBa6C-EPgtWczg6q8iPoRNiUDEBRouFUMkrufCF6TqDVOkFSu6QtqxBSP_M4Omf7wxYYZa-WyU-zqIdVpiH5_6jEFHDnAZ_JrfKXa01AI6a16RpYkfC-bA3p1elQarX4teLL5P9QACZ-9jUVH-iod14gMqVBlnIqSM7MprPlxPcaUChJWaHVRjXr4kf4jAJ3OIrjqcbERQqvZ_gVAnJurD6RMt042SMQf_0bty5bx5ZPXB52jIzTChll_nnSwure7aIKN-P9mEqhqMyeMTRwMGXFnSQdHwN86iFnCm4cydShwY01VzAu-JJyd4uHfo73C49vHarWbITPpXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Y9TEVFt7jj-gUU1VGn0uu2HigtjNhfmu6FeKU7BaOI9Q3lOm2yuoNwmQHwqyCgRjDTGwMcQOXXHOBJGaU1d80NBB3BMnEGjW3F_EetIQZHqeHj6Q8Z9fz8RGr1XZZh3qyTiU8E25Yh8zTf-llh7_9mYPXBA3x0RI6tcJsTSeUPq_6_3qpkmcEAwXO2_ja83sZg8oVqZhGb4XH1TiM9pscxcAiGt4KJJ6LU2b8iuIojYXAd8lBX4BS6ZkA2jwfsppB6qfRfjfUAZcQBlltV7OOKC53j5EAaIRD1fCJw2eQT9i2Gr3Tze-gBZ1DJ1MqsFZwP3DshgB3-KjBR3g5iEj4YSYnaNsZVtXm2Hf6UZCrHSRVZfTKuqyGKike6HBgGiBYTcfnz2_PYboJodZheApEsDAnIFLcJEhHDb63wJmNYZpxKctxER3AguhEmSwY8eVHURMZPUJ0iRsMSMHfAPrJEAbTHhuDzZdYldUK6QJkACHzhZI8nmOMTuDmihNVp5CEe7KluCCCCbQAZFMFjN7aqR7w8UqMBiBTHa3KXUHZkLcjOvEmD5Ka8Gne_giK59zwEWMDNW-Cy7mJ_iMZLgWEUpSr0R1h5VtPH-c9Vg-6lrIL2Q4aUutie_yzUA4j46wvSKu74UfYwIaAcUqZM6wdVj7ZU89q1Bf4iObIUUCyFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Y9TEVFt7jj-gUU1VGn0uu2HigtjNhfmu6FeKU7BaOI9Q3lOm2yuoNwmQHwqyCgRjDTGwMcQOXXHOBJGaU1d80NBB3BMnEGjW3F_EetIQZHqeHj6Q8Z9fz8RGr1XZZh3qyTiU8E25Yh8zTf-llh7_9mYPXBA3x0RI6tcJsTSeUPq_6_3qpkmcEAwXO2_ja83sZg8oVqZhGb4XH1TiM9pscxcAiGt4KJJ6LU2b8iuIojYXAd8lBX4BS6ZkA2jwfsppB6qfRfjfUAZcQBlltV7OOKC53j5EAaIRD1fCJw2eQT9i2Gr3Tze-gBZ1DJ1MqsFZwP3DshgB3-KjBR3g5iEj4YSYnaNsZVtXm2Hf6UZCrHSRVZfTKuqyGKike6HBgGiBYTcfnz2_PYboJodZheApEsDAnIFLcJEhHDb63wJmNYZpxKctxER3AguhEmSwY8eVHURMZPUJ0iRsMSMHfAPrJEAbTHhuDzZdYldUK6QJkACHzhZI8nmOMTuDmihNVp5CEe7KluCCCCbQAZFMFjN7aqR7w8UqMBiBTHa3KXUHZkLcjOvEmD5Ka8Gne_giK59zwEWMDNW-Cy7mJ_iMZLgWEUpSr0R1h5VtPH-c9Vg-6lrIL2Q4aUutie_yzUA4j46wvSKu74UfYwIaAcUqZM6wdVj7ZU89q1Bf4iObIUUCyFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NydwSm1lZnoCbhGDg3yJJVsWGWFfEIOc3BaIUJF6r2MtVyJxj33akODBrt0aNhxT3tVAxsEodEuottazk_4EyCogzcbygF7d8N1HqJR2yGW3mFUqwUR30lumXuCr00oD30OmKkdv2mj368uHZ800z2UqgydzZuoP6Vuhn5i_1ANuLohfa_JWuGtBLgk7VLwhl8ETrfuLJxqnKYBsgeV2BLxXLdD8UZpw1fSVWPMRtDLnPm2jryu7F01LVig31asMYTWEMSD7pvJ4ZddwgvhNVribuT6pqwmApsZD4tUwRUckYbpT3A8qkl5ao8FUNIHEqfx-fRI44aBf-xyOCvERwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24300">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E53bu3FewOeLDicpOcTByDelbj7quZCGqnqHjaNuIpdq6lwcaHxilwNfnlhI5fpjm1NEMZEeLmkyzErKe1IR76M9-1ZkFvs0RxRCH2e0Uw5pBNNE_E7gsfVmBzCimKXOV3CkkzGlUqZQQSp8xirV2xs-SqxCUuqaSi5d_4EyUHPIfQQG_E3hW_34ygj7uJeT_odKwTeKxGD8_51EoVD_yzY-ZqxOeFyjMvqwEDwUWFgGa-DbjhhdVIahTif9JUA6iRN_cizshPHeCMe60v72DnWpslSfecVeQQUMQpEfsXLp3t_t48ETX2gMUBaelO2r5Zj3TtaTrqqHjx4E7PPuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
📣
بونوسهای‌باورنکردنی‌لویالتی امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/persiana_Soccer/24300" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCnRBN80NdKFoeqUElnJWDig1T5MpvDAucp02BrpOyG-uDu-Lvp6_aSHYyPk4TwaETZekJn8W68EHK9xUsXM81B0WXwBw5K3s90CPvtPIP5PI8gyDAIjdFxtQQKhFEDvqMSSp-kXDtaU4d44x6Bj0Rc6hifc_sg9B5wFlM1LfFw3optASqNRU1WK0tPHiA9LPD7QGiePq_W3IPm_B4gpQ8S89vnIFvQmkbqJ6ZTvSjWkERvNHUR9fT_4Ih8Mg78Ium8vhzkxZ-qUcIf9sj_eFhlSBIBLIRE0aa5xCLWbyl4zmBpX-pZ33vxb09c-ebjvB20Dk8vZPcupnaAoCtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeofOteOtfv49iTbiKDtICYaQiJBC3hyj5b3fhWkYi4JCArfmK9DrCChGNheYmn0xoHORqPQeQ-F8oEPyGaUbpwWGvizrnu-3pQlc1IxJI2Vl5b9XAaRLcJfsgYOWHPubl45MAM0oJsnmGmF5131ggSW_dhzDPuXAf_DENpdoY4Wed1jlwdnAvvWauYvQ9l8CAtpHKiYxH9EKgVZA1Ouez5GXhjJMxA4c6k9tylie200a4XoMMHJTkT_-D5uIs3hjAsdzZhWBjxApm22coVqeAShNY7alkpk1ceLHbDk_el51sc4VFpy-1RK2j8xDWs8i_zTJqJ8lY4d7EOE_DgTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk8i4dZtDd6iJlaer3xQlAV6VrJId0JPG0eajbN7pXsOOsAHARA6oY7EebsY0WeNeNoIp88_OD8De8jxCy5JRd6188BDeSw1pvr9vNlP-gl_sA-BR7BlPk3bsPQcsiKKhw6abAVw_krNfBw2PcZEEaaGeUd8jn337EPUbKD_OU8nhMsS7yOA0MNkSfu_NdPXvo_aTpTGek-WC540_-El58pNAHP7_pHmy1fbyFDGGHVGm9Fp98UCUAUhldy2yP4xF3Gt1P6JWfOCzhOCv8r1AVTiI5iW-0ff808iPc6u5mzOGbTSq0Ui5BQGRXVkz08kLOBX_8ZrgJhA8S-FOkWBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GASIdFZS5MNdEioErClfyuaWKrtUPR6dM0V7sM_SadiQc19NW3d4vdHv-fzzGJRoNaSQ2oTLNP_oU_ubV0rh0sHVgZavOvVzYyFeSUKkYuYUrn9BB3b3LmIVCkRhJl_qWsl7jtSJ6kwv1uQ6NOJpizNCyABNsgCc1glWiLYZ3ISY7193kFEZzO-DeTTZSTdVmQzbsOVw2IieHsI0qtstWJTvdZmBbQLeWtZ7RbJWRY4EMOGbkDsLcISM5_NNilpT-eEYKwbWTWsoHfJlClunziUopeRhv9O79JSOmDeiZcrN3o4XBr1Iz1TbV2N5Ye-POdeZtdOWjjT6llxK1_CQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quSX8VY3KdIpyXhwCYRcz5KVqjb5bqR30toV8BI4kDzGMXhPlBWxVlsoxGZo4wLwjC5BgtunzqZKLjP7A2pYJlQdnSyNukQqG9CfS2OuJGh6bGDEi6HpkzWaQemWojL_Pajdvfk72A2yFrfVNLZIjKRiGu7l7Uy2SHuRYqpbeQ4DLG7Tbebg_bXTHBYkrr4osVQmb-pfqYLddZ7hBFynJuavMz5CnVuf_IS6hwoLOT19vl39VYrmHhT4geGHLThfzGT904yjL4tMD4hCwC80x1qJdbKaN4o9hFJUq9tgUXyhDfnVScEzGR2S9Osk8CCDX7fnG1VvnvQ1RdKsgVhj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ecgrc128vMhk2XajUKiOWM6GKiCZAuszgUyxTn7KsWrNjc42ZODFEYiIEON2BBt66q8vACP-brYtthmU8c42sr58GRoWTMfCyTTbl6bWXG1JXGIuRAhwwGE9VcA1t2qeAfl8ZqZE8oAJorV2H0IvPCm9rcRiKBFdvm_kGOpe9pC92dYtJTsHQi79Ee7vM_41AH5Dp0I4I2RIDfqPFq7ZRvTXiwEv1aE5lPGuJ8pU01YdwrryFSRGpBK1xO3bmSUVpPpGpokUaNkZh6amPDNW-9oapP3TtgBga9V7_skFMxobnAyUGc8loaU4vXt9phjoj_ETsdg_Ul2vZBcysvrnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMhPVaVm1RHDUra0gQHuGF-iEX0cV6EU86IJZ_AguijdSGxaw-IYADbKo-mV0WWdnGrfHOIzRcklWmaCr9hFpBowsbMGjmUfPN2wrRwB5prCOtaRvKXsdUE7YjT-C3a0yEFKWHFMZPkZaBnsjSERzx9Kx4uxeUYrX4MRjc1OiTLEgeor4I2PUM1WEdTHSTXESZBkeiTyHny4BTte03nqvBYLAaTgWDNIbOZa4dJrp3SF9l8VmCENDSCldxT0w6vztJi_3WXw66zCmqNl9qAglFCBArI0j-BKEQ3excx7bql3MppO-QA_gf611T2Qt6ZW_8Va9NZDYXo6KpjMk42wGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVO7dhhwWU3nnoYISterXERi9uIKP2mppgOvFaZDpTNUP8qo38t0JbAyvDzyHsdLTTqTMA0bhp0DBPHXAfZM_Vt1M9kqyKtWaeebG0c3wkvmuVwLIiTjgdS_C0Rsh9EkDxvtbHJztlk-jPOBG2mqh2_Lrr2bY_EQ_LsWzYEWWfszemhDA8FSWJvdoVg5gHtrB6kq_o8rQeNPozgUa3EQGGqvB7YeTH9wqxtthYPBa0b3-zZU5TM21vhsw2vSK7fERQxx_PWvMI3k9Xo0bbm5u0Z7urMyc0kgA3JCe9KpPH5de4ndmjfEEKi-XIT879-x40iIIkDqxVAOgcvt3SAhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkxJ3r8bfWlpl0Lq9NeSbbX6iMP9ZHDeMecFQXGo0oc5zHhyNGo1bA_6Fgj_x-akdX3CGV_-wGjh7-YIZekNw8rhUoYTgvTvTvD_jX6CINd-PlxoqJgYPl70bKFZsHmTB9lIl5ky-Q6MrF-tHWhnOy4yp2nWcWkRP4p8NeYnxJx3onZl0uIDXiEkMw9xntI5xbWsl268mD1tZ2fsV8MTF0tcPzB38YJyRKCbrcMHM2-QfskWFuyadEAoB4S0xvUBFduvgoRf2Y-pCQhNvy4Fhc9C5bc3N9F0pQWik-qL2161BPd2R0omz7WmYdnCLhTG2Hl4UUxWucSTlJq4cJ3Wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=aP2P-ULs8hX4dk1BdgD7hzEu1xWtSG8giMtJxcqrsQ5bj_u86kKGcToCw_qcJeQ_aBoRl4Ck6KIksvp3yMj0p9HO4RmATOwMbglwLP3c31e6ll_dNtRNSX0oGlIMRyAW7xTiIiwg4ZHB41q4ZG2RTDt27tdols8mAYDLMvZd7POG3j-3x_mzEVm087v_SJImMbYHYwFKqoZU8ACzcqKbAvVXobv60BePQoj1FfvYmqzSnK-mhPuU1XtU-IeisOG6MDo14WNIXwfrE4daFrN89D0FBl6z-OI-5QseNRa2kZ42UbdX4AAATFCTccVzGTcrwDUk6gOVPFD5N3B9D-F4928CdfVLFVYlaa7lUlwiLsV3-ctlnlNPhAXBdHp9fxTW_PaJn_GZ1tiOFDU4uze7G7VoGr6ODxWjfYl64VtEByrw-Dp5nyCiVS7vm_7b3-MWHx7N7RVRQASUp0OvZUhL2-7GUR5272PraEri7zwlo7G9sbcPUYK6g5PCVRJM780XFm4i8bOiJqQsG-UfEtDRseTbZnonrLQbTSC8WMprLWiggwIIV6V0buv32ZsU25Yykl9g7T2ixjwCgJIYHKyp96ZJCY_ubhZ_5kKuqQdx0LtN4gxdIv8Z_yiWUD_zbWcDiEUYoxpUVSdv6dBT5jkP_xH8hHYQLHR4IQC4GNsy0Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=aP2P-ULs8hX4dk1BdgD7hzEu1xWtSG8giMtJxcqrsQ5bj_u86kKGcToCw_qcJeQ_aBoRl4Ck6KIksvp3yMj0p9HO4RmATOwMbglwLP3c31e6ll_dNtRNSX0oGlIMRyAW7xTiIiwg4ZHB41q4ZG2RTDt27tdols8mAYDLMvZd7POG3j-3x_mzEVm087v_SJImMbYHYwFKqoZU8ACzcqKbAvVXobv60BePQoj1FfvYmqzSnK-mhPuU1XtU-IeisOG6MDo14WNIXwfrE4daFrN89D0FBl6z-OI-5QseNRa2kZ42UbdX4AAATFCTccVzGTcrwDUk6gOVPFD5N3B9D-F4928CdfVLFVYlaa7lUlwiLsV3-ctlnlNPhAXBdHp9fxTW_PaJn_GZ1tiOFDU4uze7G7VoGr6ODxWjfYl64VtEByrw-Dp5nyCiVS7vm_7b3-MWHx7N7RVRQASUp0OvZUhL2-7GUR5272PraEri7zwlo7G9sbcPUYK6g5PCVRJM780XFm4i8bOiJqQsG-UfEtDRseTbZnonrLQbTSC8WMprLWiggwIIV6V0buv32ZsU25Yykl9g7T2ixjwCgJIYHKyp96ZJCY_ubhZ_5kKuqQdx0LtN4gxdIv8Z_yiWUD_zbWcDiEUYoxpUVSdv6dBT5jkP_xH8hHYQLHR4IQC4GNsy0Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=BaHiL7gLpgYGEip-S2XKlQS-TFZ3nojfEabL_u5n5FJbCXvZQ190zG_8ruJbTOcIkznA3VvxwVOeHrmsLqg50bfHoVNvOogH1KIT73WfIrroEZPpen1FGM5QJ66P5b7gQvr-4m6nZPdpmy-P7jjgwJOYRm9bUps-5P9NWJgM11cv95YHVFWsTWeSBBYkdDKwiLKPSWdfFcGedbfJuSBUJUI6syv7OKk9MkqTmJxaPE9I5jv2cQVAP36lT9zDDbAZFPSZNcht3kjXQ0_EBDcb81JyZ7BtE-TrRI_SoI3tj1pKOJ7xXHe9AFru7uyCceaMQIZuGDrYWTqge4VMQhB5LD3zGkfbsOTSdKJs2UhxPdvsK3pDCptqJPiohVXgIvv5J2rEnJ890Fd3ZkKzPzjO1SeDi2Bk6QmjqY5dWGLpM_7AQi6dY3mVlrQPDle7H9aVznpkan7w4EIaECiUb_tQX18ATliLBObBgpvdQtaheot8yZld_0_LFdFb5lEoUBKwptLkLNj0gjgJq13_4FJjfVp1q8A7x5QZ0ti65jXHkDiXEHPWWC7krHJFabNeIuwytBkOsAn2pUiOlm-Kh0qFjD5udb9ku-n_8C1Gbw4VBLEFnn3-m_guIT_J2uz2vdAE08rH1E-n_rsKhNO7HNzq8ju5ckJJJsTAg_PuZw-xDS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=BaHiL7gLpgYGEip-S2XKlQS-TFZ3nojfEabL_u5n5FJbCXvZQ190zG_8ruJbTOcIkznA3VvxwVOeHrmsLqg50bfHoVNvOogH1KIT73WfIrroEZPpen1FGM5QJ66P5b7gQvr-4m6nZPdpmy-P7jjgwJOYRm9bUps-5P9NWJgM11cv95YHVFWsTWeSBBYkdDKwiLKPSWdfFcGedbfJuSBUJUI6syv7OKk9MkqTmJxaPE9I5jv2cQVAP36lT9zDDbAZFPSZNcht3kjXQ0_EBDcb81JyZ7BtE-TrRI_SoI3tj1pKOJ7xXHe9AFru7uyCceaMQIZuGDrYWTqge4VMQhB5LD3zGkfbsOTSdKJs2UhxPdvsK3pDCptqJPiohVXgIvv5J2rEnJ890Fd3ZkKzPzjO1SeDi2Bk6QmjqY5dWGLpM_7AQi6dY3mVlrQPDle7H9aVznpkan7w4EIaECiUb_tQX18ATliLBObBgpvdQtaheot8yZld_0_LFdFb5lEoUBKwptLkLNj0gjgJq13_4FJjfVp1q8A7x5QZ0ti65jXHkDiXEHPWWC7krHJFabNeIuwytBkOsAn2pUiOlm-Kh0qFjD5udb9ku-n_8C1Gbw4VBLEFnn3-m_guIT_J2uz2vdAE08rH1E-n_rsKhNO7HNzq8ju5ckJJJsTAg_PuZw-xDS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Ja3BXP2dMTGFHubzE0T6hY5vlwq-rJU0mxiLJIMb3jfTq8qmkeSEVDsDOb3GH8pNIx0i6Cnhitjp2-8HKeBsDM8I2lBVW2llYMQehjV199TLo2abzpqy7e9qgRiTKMTpouXJInUD8M6eWHwcsVabfgiaCTRZ7BNrO-lR2UDIlu_EWMLz12C62LpSJKGqZ25SxbutF95cH14SSWUcd2nuFD_fSQ0d2ujk4oBW9g4DagVxl9GXM07rP-lDJN4tNwBGyINX4oozlAAiHFd2oWqmD3KFwWzfeCM9dlGNHG4KtTRVDsP3MTwBWP5itq1NUiO__YpEd0nlR7Hiq3mPiqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzk3oqbCgyjWp5ZUqVaf66AdY9wMM6wbLccAVfhR9QNMRUBqJNSy6AhA4RT8H0O-MreuTjPNJmfWNT1yTfUDf0lCJm3tate3YZTmeP9n0_L-dSuZIx-6_5oXOoUXBrtz8KO45PMKby0A-zfapbe_SZtNlKQEj7PjMBNWkKRV47tZLkFQSfVSDt2hDRvuCqWsdxoJsVe7IKtC3pGu5HWCa8VZBtYvygI7WiJBbUIDpaPfvINoNVoscdZHwK8oRnEst2rIj_LCPtTsT0zmT4vCscfNwBTGI4h_DasXRJfhig9ktZBxHPQTqEMSubTPDRKp9MMlyk4zlwXw-7eYfGEbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXbkbKJLAlz2ESbu43Q7RwBbNXKDsmkFjvSikIYd2eL78PsmQjnhjpF4_pzYUU7UoJbl3aa-pg4Y6oEVGrEt19RPJT2gejG1DczTvHxAJ-535jOwyWypEeMtcGfu2nkhjYKwSlNNknVGZDK3hca4qJNTA-D1Iz7fo0k7VNbl0T8yVuQO5wBslwUl2RjNZYEhvE9L1dnYSAbu6-Tc4AuDe_2mzP0FPgshzUFFlDoGTBsy3tk7Tap1OKMJ2FWlFbuM8vf3rvbKBW2gQF_ASKZvV_99WHrA4qLpPuE1qWQ0bWucW2sGnuXFFS9FiM_q3N9v_RoRDfDdD911kAY7McsRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f30x5-UJv0u9R8-m0-y9HQd0rS89_bMHioFiXF0cX9Dz2Yu_4dStX7RLiS9DLKKtYnff7bUbJKVyHPFlROrGQgAmjpkB8YhBdvm2DJQoditd1LYD2CitUdw2iFAY-XVNDX8cpTPg_bb2iSq1LB0K5NsZhd1jvICxBupqknejmwWEsfFq5GCFPVsDYNe1Lh2jhXMVUh661xkLVA5jQaj2He7AGFpVasMhqgrlDEN2jB0wDErRBlMGAgbL750xYos8zWcMbqP2osXxOMySuAVvbnQbzM8UM3yzz_YJzqfg1ptdr4VsyOLb0FksbB7pV25ZehObb8ZTeLM_OvEstA-D_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrv4EUV9oGyBtbIzQhHoSXL1p9PMbC91G4V3idZN9ltlkvNJuStdweEAS1aQRDvOSpyVEru82XALmYqIgTDJHfELg_Ex86Pm4HslNvp3Z3J_Ut2LGrUvhLT4PzI5SZNMA0MWF5P-prk6N04afM8nRlvprncU81auqducIjVPu71bRGN1D_18WxKZ87RTZRuWTPJ7CCPqA-38QVDjFNlpKYDkw0q33xAgbNO8HJVaeqOZshhqobJoxJYst8dAZbXWZNXB0Syoo9QyE0TYacIcIrxkIwQGDaYEZOjgQDmnU2YvSAOU6S9KKMlEeJ8C0avBKJMxNseRoXrrpcieP88EwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=cIPYYtxQYzs2J5Bh_oXlvXX7sDsootI8eBXXL4PIuNNmkghJO6-2JLZUZ3V-nVZMUHdNa56HHWyC2uJnXet64lk1OzhI5W1Dfw-Vs8qmlnsLjvIP-s539UJaOqOR1saH3nzb0s1E9Ml8lhQ0LDm04fsqWTdWyXHORxf7joPf49BzZ4BUqKEt02P2FDlXJkzggN30PrZbK8zE5g3emghfGi_AujZG9Ohrse1bDiMnbmNSQmIb3nIF5TDMPYVjgoGehVwlQJq1h0AwrLsBZr3fVApsWQSDw-mbsst64f-9IFYa9h20MIpYMVlJ8sa6XVff19srOTVAD8SPdCkEb3fmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=cIPYYtxQYzs2J5Bh_oXlvXX7sDsootI8eBXXL4PIuNNmkghJO6-2JLZUZ3V-nVZMUHdNa56HHWyC2uJnXet64lk1OzhI5W1Dfw-Vs8qmlnsLjvIP-s539UJaOqOR1saH3nzb0s1E9Ml8lhQ0LDm04fsqWTdWyXHORxf7joPf49BzZ4BUqKEt02P2FDlXJkzggN30PrZbK8zE5g3emghfGi_AujZG9Ohrse1bDiMnbmNSQmIb3nIF5TDMPYVjgoGehVwlQJq1h0AwrLsBZr3fVApsWQSDw-mbsst64f-9IFYa9h20MIpYMVlJ8sa6XVff19srOTVAD8SPdCkEb3fmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKSNaJ-73b2y6NiGFerE99Lk-cEAeY1Jjh8BaEESSONWpnsNpFusFpEW-5PExjZD0srP8N2mvADhLv6U73rtEWahbj2II8nSbyeJ400PqOWjPkRxfNdopd4qDyb6iq75Nnlv62INACMOTXpgxmxtecJrMbW2RUJuXsD6d4mE-agEPmPpjgVi4-vRqBbJDHXKVKcGiCUsvmdIRjaUXVfEmv9P0aTx2--HDI-zg8-1kjPv05-Wy2YTX7I72RxWJpqrbLvh22H0jMQzilajPMt-7q5aM3b8SRz2mHScZsYdarad9z2Xx3edFtdtoVak_Mo5Ir8i0mN4eoNgB2Q1qSvLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-5rGw3pXCX_hyYuvBMRGzgicTsx-sTaLzMAWGh4vJOK28OX6yhWyNWG0C28OjQSQHw_Soi0qq5lXHKRgHVOf2KoorebdAtb3iYUtXoCnKmMcHUS2unOtNbd3D7cq3S2GCulz477lxkz22EaVFdqV6zt6pVjb6n6BmpsV9PjowMd29LcNR44DURQBTiYRTtfzJ5RlfZreQlCaQK61Jwi6MIhlYVdbH2om3WL_yoozaZSy_O9DeoR8_q7eWodJMUsCHWK4DTmM1q4C1VLlfkpORQulG2TJQmwE-2b4GSDDhsKwiINuiWZnB0WxsF4kQA1DfRAUB3hnbCUJWxcUlVQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyokP_Jsm6lahdKA6-i0p3Ca2ErjpMEoAQ5g0jLmGYN5E-__VSYHsKTekBZipvY0QUcAtYTmb-5vn9A7azwYTJe-JsAWJ5_jweNjFVK857bHAOarF7mzOv9BuZJMwPJPaA4VrEpKXGmBLlgsAcnUAbwiBeu_alkcbRKjjSMDvEHQbCAFFQxync1mYtXDajWuAF2Lj0jVZn2ccYFhynojzjZJduu3c2HkDGarZ4ASq37AKGynphD_mY0VphqevJIv_uLSxuVnXsaaxSDqpJ2jV-YEYJrTkjzd-wxPd7trkaLjm1et7nmXrvAy5ic7kxgGEI2UU6Q6SkIhtyKmWWD_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=ZPm3X78XbGpWLdmHShLGOXa-fLhgXqOJgYLljs8qxKZnpqNBaNJj39LoZNnu7IOu4ON27iOmYEy8GJ-J9RekQXLPIYfeSmH_X0QCVEGdScJwh8TdfgvVAVC4Y0am2hdFe2ve5Er9IJRM8X-ebQUr58R_vKSeXz4ZQ3gLSBO8fK6NAZsQWmSqL4uiY1jdhmJq25svJAZn0w1NS9epq4NoBq2LDO8_vShz63V5OWMSDluX-nXXKxXCTpLUxQpDmaLIJrS8_rnxXfVYwCO6bEuGQApEDePbtGm-zx0qCNub6I4wmKSPe4oDv6iByRPu2wsmjb062dG06s95SkSZOGNdBXFZCDhtD-8Fw8-Xmp4kfMtdlCMrQChF1KKLV7_72hkYYwx2ZsJ2sPPsdGAWbLz9kQ3P8T5z-mX8MQOjLa6aOY0KRhRa3aQ_xIwnS0Ad01MmYc6ZC5HYfCFb-cFv9rEm4VO-wClR6TrlPD84r7nqMu3eaeSVxIK-E6rf7fkEc2MnneB2KEdB5RzrTRGXtLzHYypUqHfpl1cFZnpJqXVFVv_FY_bsyMs-VA9nKyC2LBqd03TUuc6Eh_IJ7e1yGqBWTT1UR57KfQPHjsepdkvUONyS3blvJy6SxHu9TAg0rXZ5U8tux1XhcMcltR-x4f_c4MZ_77k5m4lTKT9WnHbNEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=ZPm3X78XbGpWLdmHShLGOXa-fLhgXqOJgYLljs8qxKZnpqNBaNJj39LoZNnu7IOu4ON27iOmYEy8GJ-J9RekQXLPIYfeSmH_X0QCVEGdScJwh8TdfgvVAVC4Y0am2hdFe2ve5Er9IJRM8X-ebQUr58R_vKSeXz4ZQ3gLSBO8fK6NAZsQWmSqL4uiY1jdhmJq25svJAZn0w1NS9epq4NoBq2LDO8_vShz63V5OWMSDluX-nXXKxXCTpLUxQpDmaLIJrS8_rnxXfVYwCO6bEuGQApEDePbtGm-zx0qCNub6I4wmKSPe4oDv6iByRPu2wsmjb062dG06s95SkSZOGNdBXFZCDhtD-8Fw8-Xmp4kfMtdlCMrQChF1KKLV7_72hkYYwx2ZsJ2sPPsdGAWbLz9kQ3P8T5z-mX8MQOjLa6aOY0KRhRa3aQ_xIwnS0Ad01MmYc6ZC5HYfCFb-cFv9rEm4VO-wClR6TrlPD84r7nqMu3eaeSVxIK-E6rf7fkEc2MnneB2KEdB5RzrTRGXtLzHYypUqHfpl1cFZnpJqXVFVv_FY_bsyMs-VA9nKyC2LBqd03TUuc6Eh_IJ7e1yGqBWTT1UR57KfQPHjsepdkvUONyS3blvJy6SxHu9TAg0rXZ5U8tux1XhcMcltR-x4f_c4MZ_77k5m4lTKT9WnHbNEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeXz2xXlZ8OliiJ-TzBPDq0CfLFWlGwx9zbo3nf9grWZoIcspHu8Bcj61PvfOUZ_CjRRtq_MuI-j5fXg9e6yjN-Yus8AJ2f6xoMXZ-cJyf3COYZJZ80rtwjKe2vEDUYIWCi-XSsf1KIeQ2S1r9dlMI5DwrOUkX4xrAw8N5RdW62vhw6XpI96-Iz6rxiJyYovO3olP0dYPtqOwQU4ZYIlRppPAo9rKPrh-TZ_5RZD8fba10KcMJkX550PjOh2T-DeRlVlAk6RHpRqjwhamo1LBNbuC775qyUrTUsU1PsRUWQElWFwDdC4qd4dZexc39mZ0-j-PpJdBsaxkVxqFoLOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkG-1s5oMA1wwwtoi3cZx5uvRHiHNwc2MbXTyJkkxeZSEgWnjSUwjXEDCf7NT-A8gYG5__GNlovh4rVVNZqoDYPBqlhZBlUmYYs4uAWu77CpGoiDRkVFMYJyj6VIBhAJFR-JZygXH3p3TEPAgEVTPeTytDMud2Tc0EaHkpYfhvF_Wc9cNRe61hXPf9ZBZCSP4ireWqvAjWF6Yapw1YzMLwRSSBFv7jomD56M724zT6SbkYSKVNbSVtZAQLgq31IzjnKyHP5DY4KmffGLFStpGqwlQxYLn-azmkTPbGq6p9PV8oC4jWbbUpN1htBRzMSLzC_9UcZ3LOfdw1ENHLRgxCHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkG-1s5oMA1wwwtoi3cZx5uvRHiHNwc2MbXTyJkkxeZSEgWnjSUwjXEDCf7NT-A8gYG5__GNlovh4rVVNZqoDYPBqlhZBlUmYYs4uAWu77CpGoiDRkVFMYJyj6VIBhAJFR-JZygXH3p3TEPAgEVTPeTytDMud2Tc0EaHkpYfhvF_Wc9cNRe61hXPf9ZBZCSP4ireWqvAjWF6Yapw1YzMLwRSSBFv7jomD56M724zT6SbkYSKVNbSVtZAQLgq31IzjnKyHP5DY4KmffGLFStpGqwlQxYLn-azmkTPbGq6p9PV8oC4jWbbUpN1htBRzMSLzC_9UcZ3LOfdw1ENHLRgxCHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=vNhzSUioqWxCN443Xm3Pcg4fr2T-vvs3zkEcKh4oABEMVFwJ6aJwd4LBl8wcJA-ylboZeDLbtR_spK4ubmNPsP0Oq5OGRUydGLFFN6WMtX7D9YQoQceqhcYyqPTKK_hpBXTtTZ7j_8vY1s7avhyCUcbxOiA4PFkYg7Q1qVOESaX-dtI8c1FGjvLTf5dcbVoZNtldHLnWON8pCI9hSwD852PqHm_vEBxQgfnrzx1UKYzBnnPHyuwEt0vEEAsvlRExQdbBdAGSM8dj0gxdquctO9KIV5zrqqz_tT7HCy8ebJyzPoKKNR3W76kHujOTx3gr3wXC5b4ugiVMZy2kgmv06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=vNhzSUioqWxCN443Xm3Pcg4fr2T-vvs3zkEcKh4oABEMVFwJ6aJwd4LBl8wcJA-ylboZeDLbtR_spK4ubmNPsP0Oq5OGRUydGLFFN6WMtX7D9YQoQceqhcYyqPTKK_hpBXTtTZ7j_8vY1s7avhyCUcbxOiA4PFkYg7Q1qVOESaX-dtI8c1FGjvLTf5dcbVoZNtldHLnWON8pCI9hSwD852PqHm_vEBxQgfnrzx1UKYzBnnPHyuwEt0vEEAsvlRExQdbBdAGSM8dj0gxdquctO9KIV5zrqqz_tT7HCy8ebJyzPoKKNR3W76kHujOTx3gr3wXC5b4ugiVMZy2kgmv06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojxMWyktTRTMeYTp41EzokoiQBUywE9APjOpJe8OU1UtoajtYssJ1zqsDjOy0rV4SJwYeE9iaCJMFUTa5GwX9xw6bfnimjFOlnWUk50pEuXO_SlAuPQ_8fW2AKFtwudQDg8y_xe3jtvbzQIY_BOt210cRuine3mejoiguiK_SRLtPXJA826RRjsQI3H6bf_cfVQ8FaxFyHCiDDSNqi-LzBjrBf_qCYbOsLOyjemv3HbpNBLDDeP3Q-eteSRNzn0nnXKrg_f3rB1NNFWT6S31YmDqKL__K3wcfXs_yXSRi-5yEPHRemff316FS6rJ5HZJ5FD38awROUKVnZAWIEYqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCEr29-SMLEnpPebMhVMH5UKOAsMIVXVhVrX4gX3qfvdRvhwSgmeFW4ux6LNEeBI7_DjAhCgkzYaMNuG_bssw47wEXydpruxrwAsuB3FAdfD1iCS7QiIDQchwf4AV0seZhi9pbUVMpE44nV-Ztx_yqU-ir6xqgG3bg515vz3gGW6HQPh3M4T6uTJ69PNavZBG5ku5OndTIWp7tmwh6uSGi7729-HZzMXi_xYGpVB1ClqdK6MfmUzQ2s0JWjBPWaFqpnQSfHJ4ge85IIqFVf3n4Fav2nr8_HgaDBV6ggMxyLMW8KPci1tmAokewyEOvOoAUheWMFCo72MUE2r0DmAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24270" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOB6Gm7NQ77liD3rtPM2qpV__MJbK5l-YUWPA1L4eVfK9jZE2PzQiWEz5qomPGfW-4eKjKi4oA05mR43GGW9X8Vf3Gzfvooqa0itxUEX-i0bTJXaFqNjDomK5xIbjQwFZMxAoEMm3A1MtItiibn5pEdIduYHY0qrwBIoutYHNl3snmO1zXeQ0z5LTcEsJF1yGGejCZWcKq4JiCUpdPHCSZSGecod3j756HwQGIA4emI-bJOWyx4OpncFz03dV6zMmNu4yoYgaNWiyP37opWU2eaypTWJOINElmpHvEHFC2QNSuFsguiXxHmljeJWO2sc6EXcFVgT3vQOeLBAG7XrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJ52yNSMzpRPHqL-22fWyRUYctAhqdWLuc_qzERPviUpNYo28ES1GixAn9o33sk4RpzMc5EYmmcvgvLR_9lPswwgCC4vjThqp-Y_6PPls3z34ueBT0_RX_F0NA-P6Nw8EWtwZ4xhqOTD_vQ8AFi1Dy_T9vt418yB_6jzKQtkxv4ji4NaEoNisM1jSyPaWHu80tMNXjvkFWr5cnp3dpbi4wXHFUa02I1UE5oK1AF10NkxHzxggV1_n1oSXw6kkoY34Z8NjMcNENM5iRNIiK_Lv753BAyTMBENXXL2CEOi4YYOMf3vGljqwsc7zuy-4d2VnYMIavXQHjrRPSVVrLHbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAh2-16uq16TShSPsx-4jv5Z8IFko67tMz1I9KdrDJtN5m-akwPrd70-lw1MyX55UphMyw7x99LYHKjdNYCNKn2lJjVdwpwj3KluSXKaf8vpBep9gYXssYEZk82FBxRyL0UcmL66b6kJsREli4tqWqrxw-Mqk7HJaeHXx3h-502T41S0rVt9WD-0l-Sd0nHKEHFdwl54s1eewGe8-sbojKgEObZmfUG9z_uaVm1QmBTYCJ4siIqEMQZ2Rkp2v01lopbCcJNLAfWfvUZ2lmJGy9DeGyXMPMU7oMgFMWsgv5NtIaD1F6GOCSbvQy2d8Ky2CwL7wHC95yEAcjTr4YKm1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhJ2qThiZDCpHWNU-lHsiZwlvByHiSFrFPu27EBA7Z_vECz1PDuXALCeicZvx7_9oM0pkJiky2Jh0q1bDWokI_2OYPqtp5JzHh3bMJqM6mPgCoTaI1LNC0P7KmpXzX2vdgpujWbRmi73omed5ZV09fV4VznHt19AK6sihfWxphRrUtYUMbgaVs988f8r12c9v-QnlJKkY3vV5Ij2lZiCiIRGRDBw-YMCmobkwWjC-W17G8HyYf4K043QJl6h0hqA61EBGztTlz_BQSKCvTjiifDSy9EzFHhTRgnX0Xc2brs0emCImwG9trbaR4IoXIxJNklDFcRzGsHo4xjlZQRfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=pV7aXBjte80WyIQLH3cmj7PgIUcZvqYZSzfsCXMfQVDT0CcJC_4Q4p3M-lFCtbx3jrXs4jDWg5WYv4V4WBwh6eaUHmEW_1ZWV8mODRfvIBWZlIyyTmHTtIh_CgZAvnILwVvFdjQsI_JRE32QZvpZL8hjxwY2HBGZsNDdGEUEWLMit05LMQWxuIo4H3s8W3xE1MPX3qRmOVEW3ZUpQuQle1IUTmlZ_ZFY26w_Zz91FmFBNSmeJ3QflBUbTo4OmRjVAQxC_zbyPyhr__93wGQt7QZDGhZGmH3qO3_Kgs60sMwHl-EbDOxsDVWv8gYma6kVEGbxkgYoQ9VXU_QNFtCT9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=pV7aXBjte80WyIQLH3cmj7PgIUcZvqYZSzfsCXMfQVDT0CcJC_4Q4p3M-lFCtbx3jrXs4jDWg5WYv4V4WBwh6eaUHmEW_1ZWV8mODRfvIBWZlIyyTmHTtIh_CgZAvnILwVvFdjQsI_JRE32QZvpZL8hjxwY2HBGZsNDdGEUEWLMit05LMQWxuIo4H3s8W3xE1MPX3qRmOVEW3ZUpQuQle1IUTmlZ_ZFY26w_Zz91FmFBNSmeJ3QflBUbTo4OmRjVAQxC_zbyPyhr__93wGQt7QZDGhZGmH3qO3_Kgs60sMwHl-EbDOxsDVWv8gYma6kVEGbxkgYoQ9VXU_QNFtCT9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQEFRg7hOWTg8uPVAEWKt1rH1lpx8d1nCtqfFp6ZsR5MrdvbcfUrB4Ksh7SUC-JRH1Tn6bUalrqk29s4fUAjibxKGgSBWLcm54SmLTenKxFH-VbEl8zrAFNzMPK2b9qAdXe2ZrJkYN0Ap-czvB7CeqTJfSzUCFBKBYDfq8ioMn7xZGm_tXE_mZiLW_AZJvu0RsO5EFdo-3bGirvQOsPfg2fYZbAVBS58KmrlqzQ7XZ6BRiPe5q3cyqniCyl3e3Ji06zsrJvLle_Dq-I7ISP5FJ1cTf8QZN3oVrHAKNlOecm-7H_UaNeTLt2F3_xeg9kCdm6gDNK0KRlRFH_5wLHYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyp_nL2gEB6DkcDWba_Y3sdJYhLA7Hx4oob964zwIcQCZfCdq6aARVW8HR8yVLUumgSg0O7lQiCdxU3ZIMMLoP0JrssDS6vL3gmXzbZfQmGdBBxh0-RBle3RthFzbi9r5bzEqweKeIpxfYakigxo950Ua68V7BdJHoESXmGUP-_QK63z3gbcF6WRSMZAva8sNaDwKKOJ02JLnf2Fccdc7hxHsZZ3Pj9p22vByFc4j8AC3Y2xrImx49anf6sLVLAV0S-DfYlN5gwP6sXgGKyp3jehTTSt83xBJSgid1ywwxywKt8J2eUVN4Oiim-CewfILrFTposZrIllcAnAgCDThw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=IMsu9x1ccLRKRH0hy40k5YTrLD1rI6uqYWDExL13ZsiM0MMtn6i7o0-s2Dl5U1otswmWFSL3TyHRfXK1WGdtdx47HmH29MFAifhgF0M6LWnJaOccmzJDJuOGxnLeRIbgRtHmZnfUkiNhBYtaXf3W5gSvPjHqBRdSepw0ZBR2blwDYlXjw5SRFU4lrn7bTp9wHIo_37SmFPrsBABR3yZqSTZSRjbETKwpQZld4E_-ZaI8d0U-hrJ2IhD1RA68OOzHxhpH_AaG0Q8CAwTjb_VwYR7xdlTFpeimr2bewjCAoecAWxWdK37HVFhOzm4g5hjR5ke_pIO5jvL9ZCt9zeaSToUiN9kk2BOPak0-qhEpefz5TrZx5pWblQSFof0N_h0C-vY2nZicuH9Y0LOCHF3kKtKti8YXv-rIvouJZ_aN3Ws_Zaibp7hi10aKVANhcbdIOw7NhaogVaP80CrBSSOQLuHBptRDcgo4L6WwKV7qabUzsl_suYGdTtKyPundzVL_UMQHmhUtPt00v3TVUFSa2D5RH0prLfbeVmktT5MiFLsj7Qlwct9vo53knCwEiDutD1AX7rnaDNTnIlduPAEPCnT67RyPE83KRlv7gW2vasgVUYwxgah6d6eAu7ktRrC6-kz8I2BGx0rC66_ebVEjY46Bt67LO7rf7eMAJj8DZco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=IMsu9x1ccLRKRH0hy40k5YTrLD1rI6uqYWDExL13ZsiM0MMtn6i7o0-s2Dl5U1otswmWFSL3TyHRfXK1WGdtdx47HmH29MFAifhgF0M6LWnJaOccmzJDJuOGxnLeRIbgRtHmZnfUkiNhBYtaXf3W5gSvPjHqBRdSepw0ZBR2blwDYlXjw5SRFU4lrn7bTp9wHIo_37SmFPrsBABR3yZqSTZSRjbETKwpQZld4E_-ZaI8d0U-hrJ2IhD1RA68OOzHxhpH_AaG0Q8CAwTjb_VwYR7xdlTFpeimr2bewjCAoecAWxWdK37HVFhOzm4g5hjR5ke_pIO5jvL9ZCt9zeaSToUiN9kk2BOPak0-qhEpefz5TrZx5pWblQSFof0N_h0C-vY2nZicuH9Y0LOCHF3kKtKti8YXv-rIvouJZ_aN3Ws_Zaibp7hi10aKVANhcbdIOw7NhaogVaP80CrBSSOQLuHBptRDcgo4L6WwKV7qabUzsl_suYGdTtKyPundzVL_UMQHmhUtPt00v3TVUFSa2D5RH0prLfbeVmktT5MiFLsj7Qlwct9vo53knCwEiDutD1AX7rnaDNTnIlduPAEPCnT67RyPE83KRlv7gW2vasgVUYwxgah6d6eAu7ktRrC6-kz8I2BGx0rC66_ebVEjY46Bt67LO7rf7eMAJj8DZco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=f-eFpGiNHUlRH_AKoJlyqIPowmtxrhoXPMHNVyB7BMQn88zCe5Lbxcvlz0pNLxUzSKrJ4ZFpQFqBIhXYAEGYdoXOjDDUvysygRRGqJa910VxUVpWOkBx9KTbItA_CIevjKvVY_OOz95E5XkEw2oZqayI8jFTjmF4RyRUwj6FKZSwOIJ3PyAAMKR0Hsn0ryM1lN1gr_gyufRYrC4VBx7TQ0JygNppB3P8AIU_dkHb_OJNtBnQ7O4aUvZ6xXOYGa-zeM4HzVrhXymfAMtYjXaCtLHsuvsi7C7nbVPYxxNBTLUNiPj2z3Iv8buuHQZLdhIO3PrCpOInnVVYv-TKfT_Big" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=f-eFpGiNHUlRH_AKoJlyqIPowmtxrhoXPMHNVyB7BMQn88zCe5Lbxcvlz0pNLxUzSKrJ4ZFpQFqBIhXYAEGYdoXOjDDUvysygRRGqJa910VxUVpWOkBx9KTbItA_CIevjKvVY_OOz95E5XkEw2oZqayI8jFTjmF4RyRUwj6FKZSwOIJ3PyAAMKR0Hsn0ryM1lN1gr_gyufRYrC4VBx7TQ0JygNppB3P8AIU_dkHb_OJNtBnQ7O4aUvZ6xXOYGa-zeM4HzVrhXymfAMtYjXaCtLHsuvsi7C7nbVPYxxNBTLUNiPj2z3Iv8buuHQZLdhIO3PrCpOInnVVYv-TKfT_Big" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa2XDinigAuRbifTiTKwJAjW3vpIQ0K_X7PAT2cAOqF2epkjZSRdmRnpbrJbUJ3sStiAwHDAnHp8f3b_bAJTRoweKia1xGgjcl3Mxn1GK-fF1CQTFhiEarK7Jd_GJR00FzrChyD245Vm72dLlrIhEOjXbvc48zeywQPC31o20oemHSTqMsQ802aOjE9LGmuwtMwuBGJOxWf2ACx16f_qJ9oCJVTOvH9rkSF37QYfLFpRCOkw5p3TmqlgtdyTG4SLu4BIojX9lyZI4xcKZWNbA3fGVTnaiGO5PdJFem6r55cd1O4mOrx7BnhCLPCpLdCykO0_ooarcnqOdtHD8GCzLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRtzEdFo1PHIoDFUEsQ4AIJgd4rBvKwzqebp9xCpyMqA1Z5ZZ0SInbDbpc2IDqUYk-oDVIAAvU8n95TxhsjANVBpSJBzUYFNkJd_bW1YXCvt0z8xP1WGRYXyY8sBLTztpQsfb7VvUluF_Wmy4WwsXkAUuxeb3jAIZ7V2wvKI5FviJWCjEJ7DRADz4XyAasR6BRWGP6HD-k37dioX8HmGKIIJm-qW7PsdGZpYmn0uKeDUVY4BD2M4ZzdTfudg7m2v6OdId-5XbHsZqNpZfwnGinLiuwQEcj-jqf9T0tHk9pHSFIISbK2wYVHmMArqrhqj0rP9v-qG4zXmKobLuxbkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSXlQrr6Hll6UyKagFt_GjuoG1S67LT3wtDvPxqjk3vmDYWVX0xcWf-C_J7k6nxDcLVYM9A6iK_aOJ5REsGs3ex6zEfapX5SXG8bhXT-z4Lwd09UPyh-X5_4em-Fb2bhOSn2-zuogo6H8tp03Sq6prS6y_ioYlS9cnqWzbrXkGclY1T7vfOHXinyjJHKJFKNWDqmsagMnHEozxeqN4LKEyCW4x5HTaSJ9S7GCq0uBv3zxZCFAa4KPkVp88q9u7m6j6KqLKDob7f_Gzj4ehHFJmjPH8dkWz5wlhkBni3raE2Mj5jS3d7kEAf3f5PEhqSyqidal93DYp2BK5pzsfjuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5JW7ukHTbWlSOx-mAutAZdFFa8JxykaxbP9Fc-nLIlUEIChxxF73R90MhOeBoTKO0pOD1iusQYoSsQo85uYUO3zdTJQjL-jwERrVT0KjD3Er6wO1somfbfZGJL4B50AYz13Xo0lV2PId7LAiAjHlRO9JbzEmMOVhyJ5Hb6ubz0KuMZm2mOIOExKzLer303ObvPg_J8ahl-3HHSdLm-3rPEtZrJ5h_0PAGuYU45b2BQArRCKjG7RvPhpqivs1VLUUek30HL9YO-BhCm32-WPkab-48Ok3kN7UqzQUicaXV9F4JDm9ySbm_zzHzdU6yvuECBSxArrsP0E2NiAoxDucA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmky3fhdTLqBbhkC7iHTTD-9FEAb__H5xo3X7pIziYDcdjLAl-Q2xQMDqSWljnnFBgMQ1uXZJGGJVRawjbHXHwz885dRJHYMLvkzjftBAba3qvZOKsFCwGJhCUsk3mwGhElG-xuW2soiHruyMFxdle5e7SyzmtRCcj3lUvfBXdfrXYJV78SbrAB89QQLTtOEL7QMtu0NoGXzgLlxgKlxAKPvTtID7mUb5e4kFeIH772K6tWVEmPqRnSR2JbbycFR0Svzxa_UYpN86hSsXHarEBKJm8EW3E2MVsryZ_nLSA-TxNYnqmBFrJfsLyVA_XVFLl48qGBLC3c3qrOKHLV8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fmc09eqYUVxhuO3bEbqNsNPvyqGlcazkjHXWsGO1oQveHK82EwvEheogBhj6G3bdGg91hvWzd3wKrbEji8RoFkjTGHW4OOlPmwjvRLQ2BcEo8_4Xy-TUciELN_LLZvVLgsoRHKQJJJzS3dbeA1PZN1quqcpc0IoYDzzxM_TH2mtqMxWZRWHE5hLxRMm4M0JDx1nPDs9D60WYJ8nkXpzTzE1hW1HhT0HF3XxuoTTc31h7T3KqmcZvvnFJUU5Z7GqTp0MSXlxSWik_6WQ9g2h_9jUAlNF22jPaNwwQbaV3IO6-SIgMlhjx77R7UOBJmFDN4qVTjwVxu8xw7ImSnwnCkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfYbEo-ITGmxo6Hdnv4ckaDliqWM8LV0hgevZbnCFUHo4T_DpPnRoVFwVi2Nv0URy7iaCPpPCVsTPDhx19_OqDf1f69wWERtvddX7Oz8L4_QX3gu5kismNSj6BgUyW0_6FN1iiCwUoDNfy5B-DHPUsmpaeN9rgq7p6gCXYcTf12KcXZdYFBeOxD4NS9gba0EnaBPNxY-_S0MSLaL02EDkmXxD_9IVWulkjHOcTC2SquMj8BZHDoskL_K1yNt-ycG2yr7_12iZ6FDEP8MZs25d6MZ1oTT4o243zLrawQzw2m15u8I8gS6g15H31DErdYUNxKTQXGl1J7ZjEQDEOmyww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qR-Y0oHkO43hkRQiAKjlB8L-KVE9_UH_o094arloJttXVaUvPxVEHQqgpQWyxmsSCw1hGmMY7rOWof4NCRhSO7RXDVE7uAUck2tYR1spuzpgnkhxZtJo4g2b-cl7cDvK1X1U2rsZHjGMCIMz_5z5SLlypN8p9ltOzZcl8qhsZYjPdWHhsOTL9Usou9JIHWaEu-Evspkxh1sVkiX4mTyf6zRaroLQor_avd5xB7ptsETYbYwPhIVxpzX_lH92UQikAReJJe87oW95O6kORVqhyouTMJpcWvfzlLCVIOMrwBNQEQ4Ea2NxLBcxMVvKj2pq4hzhCdEU5du-5LTTBm4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=hugXEZbqvF1hefqq7lKjxUsez-z39WzP-hx6aM6X2IXnWE6wSp6AyLhaJrKfgCjcI9LkPxnUJsu_qGMDqArHokb6y20r8Q1sGceJFAngC7p-G09FJC9NwXPU4oR7b0mfqESQCE6FR3IBXY5ZzMK57MVD_UlfBX5lr5aKZznQ6KtJzQGTQCgGEurkGBOXLMDZEJloisIZraz2qq4w3IAEfeMqWloSbfBmgI4WwfABKtQ50ZQ_GG8bzxGp18YF1YQnshTsosE3EoKO1tqoaf_hzFKh7UfCIm9GcaNDRjcpohVwXBB0yMcmhFe8NgBwpYcrYfLjgk3aW4C-7_XglDJ7pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=hugXEZbqvF1hefqq7lKjxUsez-z39WzP-hx6aM6X2IXnWE6wSp6AyLhaJrKfgCjcI9LkPxnUJsu_qGMDqArHokb6y20r8Q1sGceJFAngC7p-G09FJC9NwXPU4oR7b0mfqESQCE6FR3IBXY5ZzMK57MVD_UlfBX5lr5aKZznQ6KtJzQGTQCgGEurkGBOXLMDZEJloisIZraz2qq4w3IAEfeMqWloSbfBmgI4WwfABKtQ50ZQ_GG8bzxGp18YF1YQnshTsosE3EoKO1tqoaf_hzFKh7UfCIm9GcaNDRjcpohVwXBB0yMcmhFe8NgBwpYcrYfLjgk3aW4C-7_XglDJ7pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo7NTgp0Uxqm38L241LtTMGrwC_PZKiyKQxBCPTx89nc_c0SkBx1YVWvc-s0wcWUYsJOhHtotyORCi1J25_ZXVse27LNG18Tc018ClnGvVePQLQPOOBBFEzZs8A5yuQpxFIHTNK1i3ixpMVMv7mUr5DvZkV5z-FQnXkzVYMFI2Xs1AquLP4QQwB8kqCPp4y4k10rx9BG42b_H6K_UD1X9o6XbRiUaNzp_gwUpF0xUZFlVdisN-0O3zKfEZYI9rJipoUAATWITct1WZ82ejanwa4-u8ajLZz5HI61P4sNO6EHj6ZCyLDSyDb0A2qP4opj8i1ba2RJ-5Ne-3HGF5EBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNHzp_Iixl7wCpZmGYcwJcC4wvdn6eW9D8kPQGt51GssRtL3ub4EfhW28JpZ8KOkcTnGwCqUSbuCwFOf5ioVcE6f1zI8MpjazTIlvNkXI1gHcQWeedTvNhcXlhe6cGktEUVvRH1cQ4HL7ah-ONju2gt_kgRoP6xfqlr4vYG3VeC_E_8mg9THcEVRAKfl5xZsCOBU2uF9FL2BC6PWovtzUpxzPYhn75Y4_iEUkb8ST2fIoN4GEzXIDAyL0TlL-EKbtgO5axV_o6D9rKPzblUwukZWVu5RqqonJu0_r72BHHEa2HHWh_RfZNsVF0R2hU8S8cxf1m331gPMHxZ7XmnXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDmoDwXnG3AcAQkpu4AT0hHoqS_rDFPR4mveu468fiju0qvcP4iqXUILJuGSAHX1GnNqX4vPq7aZ5kXQKLAS2GzuOYLSF4eqMtHu6zVuCNrWc2iETgKvM3DPBu_yFaUkzQj3wWRhvg6zEjX9yMeRMWYb189xDl8I-8zOg9BdiddAUYSkzYczJ_6rkQ07d_0DtLfbreoBKcXw0_g0XtrhiGSm6nN6CcdZZd3OJGoXGl9peqsedt6RQMmWl17_tMoy9VvHUCBTzRGstNMjCWSQPFAGISrE3ccyobsMLIthuWjYegBaZPWEJbTe-IBtpUzA4nKhvBBP-LTfAEh6uqFV1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ7wg0yQPSex__Aq2MSGPjP0VfJiQpKwTixcpLf7Quk9cdap9Y_0lL8P_kQnDwGwh0nllDiwTsi7kbE234ZLxwNCafPKn3HTGHL8FF2iCCgE2tu9GRe6zFhnj19L_2ppgkxRyxqunREKoZfP_O5NzDQMSeD96Fom1jvIKRU-1Nt_lpUHwklCBH0e4AUCBMx5b9oCiKCKjlzWK81zzBmy8n2f5NH-JZSL4VhSInAwyiA48_WEE3JkB1kEDTLKS-Ptkd0aGTewr9HQNBFwdV5rViGJ-lhlGtqtsasHv5Qms_Q44InjSbjpU4uvr6ylQhwBacL3dfzXgstVfkpFOW5QQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6FlPUObAmVfQ3eyaLC5V0bHHtyhBlKkw0FZ8OqdNIAUP3ul4udle0cVGb5YcO6vJW8o257cQ455n4hQhTnViLBPxb3KthYUDuEQWezcJMBFd4YSg0wlXdaqbFk8RxFKoyeZAGTSTU_nByS1nP0u7RyMhRgjCEntSA1IDCCioueqxk6NE1E4gphdUV2unkU1UR0EHM36O7nUxRRv-f1eb7weY1Lgof-0mfQWW0hDqysLAgPrkcoQapFGn7tmTlU_67aHe2hGQsbzGgYsoxD5Lb-aaHUxb4znDeWLWMhvaw1m5rf5qWolQ3rjm9ZIG_RUyOovjiIk_g0wGFeTUm-FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-4hZpm5SoKO7wbWFiezn8kgw9NZo3GlT1aOWXCz6p4KpXVyXx8F9x-6JMuSD6ipFmdOLpHXI-4ZDQkeKDSwSHd9KkQWAjeO6uy0pIMhi6Nx_iAElsEBFe6nG7TI8HgjK0dfzmbXQ8QmQEKyaonhG6mcgZvrNrXJ-PL5_oBY2h94OxAm2JgQCeco3CIrp2Y-eGyUZCyY8CwpKuHnESrRJnXo2VZqRo0b9Bb__LCnjILXp2LtlwjKwUBrCETKrh_rtodSyiyfsFgEvA61JCcHyzScwUDafQb9TUVBTLkL_MHRbjPzqpNVh0r7FSug-fs0ceOcDyBmsSAsLyygrAX9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3Au1CBmFLEKtTxOe1owj1-ADZu-zaSFKMpFAVS2z7yF2-4nKqccRrxp1stgCZsLscLs5QkrLRsOsFEN0f0fLKnkUb5SMQwePS9U_imD3gzhu0KxRmVeZHv6JDyuCgGg-yN5GZFSQ0WSTtSDs46OlAKqW0rS9nsJkJE7s9aTnOVqZHGr0eoSXdCaUbScIHQTTvdhyu7c9ImTkEcS52_kXxibJ6YMZUHFy1mGypV4eW-uqvSOr7FlreEEq1ZPuwGopwCbTrZBoI3bUjcwlA7PIaqwFJPdoxCM4x-usELUTC1ntp-Rq82t4E6r7JPSVQnoMCzgw1TaDwFpwOlyS1j0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m55xza7tr48_OEtW9i-Q6jRTvHeeT8iJlUE_THyDvPXiRpvCCVcvx_krn9rrl-XmF38EzQTs0NmKmChvH39-GYy-FUJbpqfKs6jMzVR3VUgX7mhsobnZ5xSgKnLT_Jtc90Edn-XlnpAcOlvzCnPMzsPxBqCqkTzh2B4teoGDc6aT_3Sb9f4JbgOnItKPUG4T85I034YvKIsiiv3R4fawoDv_l8qC0SJOdTzdsDo8Hv8euTUaSNXGozswwja7KHbZC2se_KRg0aOTd3DdZ4f14hIk97pH17A_d5eS4YxwY9oDBew8LpJXsi9BMMO9pIlp3duVTMA4cDuX4mPlpxUMXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=LGB2ScXs0mZz9fyvl6bo8z2oDcvCZfkfzKeXa501v9t4E_VFgUNbnLTvw-mjlcnGch8cjpa80I9xXW0IZYltZs1kpT4gqSQHWq9ZVHONDlysbtJG07yywtDWjLyxdFYvet0Y9CyhE1Px-jAk-88RMng8ipklvpD2FFYz74Yqkc-ja0082rUARHIHvvoRRh8TgKtabKhPa_5OaJs3aHSelc2wOG3qtQuP-nzOm2GFcZAfHx7nGCzm3Rwqx8KI7udPkksW6G6ZiohNc-WAU-G2WnQgdQu0C6PkLiPzofov7d-bfGZjDwdGnWI1JXBXvMniyNZiPRj9k5NT00xTLus5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=LGB2ScXs0mZz9fyvl6bo8z2oDcvCZfkfzKeXa501v9t4E_VFgUNbnLTvw-mjlcnGch8cjpa80I9xXW0IZYltZs1kpT4gqSQHWq9ZVHONDlysbtJG07yywtDWjLyxdFYvet0Y9CyhE1Px-jAk-88RMng8ipklvpD2FFYz74Yqkc-ja0082rUARHIHvvoRRh8TgKtabKhPa_5OaJs3aHSelc2wOG3qtQuP-nzOm2GFcZAfHx7nGCzm3Rwqx8KI7udPkksW6G6ZiohNc-WAU-G2WnQgdQu0C6PkLiPzofov7d-bfGZjDwdGnWI1JXBXvMniyNZiPRj9k5NT00xTLus5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFQQaUr7eOehLQ2GXrU97FZt9vhmG6cuogRkla7_WDWHu9M-SY-fnhYyyPawNxlbFa7YlV1KoEkV6jhbDdMNdczT38lvWYrLe9g8YFx8fbc1-CFpFvmTGvTMazFUETSgxNvhNorIq_teD5Q6cpEXx-MsfC7j3tkeDa_tQ7KIqBKrzdcJTpxpLIr12_nPTjOz3wa_K8xjV8l-gHu7fAWnpdxDArJE9I7h2Cruj8dZnCbcIh4IcugVh7dK6YTG5V3ge8OHJhZF0h9f9BnmMnsLXnwSmji-VekRYCvWE-nbMDoOZhjrJMsH1ndjhZ-c1XhgosVN7tJ_OkzzxhDEC7wglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osZ_HgORWG9zYGsgWnKiRlc5Pcu5B-ACanbPKyFKErJNrexZqzYMZHj3LximlGg6o5y-v9U-VCMARZ1xtn-d0LlsL6--vIC8d2BpkmwfJKlW_X9qrGHwb758E0edGJa89EWMfbdw8VJpVja0F1P1gwQmqRIvSRHOp2LlX5buewQwhZA-q8nsbfcn4yEev8Z_NCNLkYp4Lq_XNTqBIL5maKKdgAA3JBWo67wOV4kY0imyYjDcSSBfnmuGmJzlbHlrIBNUOkRs8uWnc31nwxCqQQMwmtiQ4g4TQTDEZLcmj9aJBVPkGjFR30d8pOQp8UnvPd5j52l_DpreG966ZNdKsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQPOekYH1ibokDUmLCo5Qt76YG_Ozt5l4Zfv3Qyox0SCQTfgbvCSH7tApHlyC5L5VTDAXR7rZc8Lw3mjV3uzjQuuEC4yD_Rt_tdexKkgUfsVh7Kln_wb4epUkq_IXusY5NqXe0B8umpLwkBcGNquleUOK6QqL7fX4OmjebZAQiqv7h8adE5r4J4fQFqKWYxrJWr9QZ29ATXozdZKl2k9bTWN8YdrPoT8AqFaFQ61JKhsAwVZReDvrvbagXDZ_yIazAq4rKGFI_v8FavOveIe6W0Y-dmQWRtYBt8EwJBuPz1cXOlxaWRyXibjhSSFobkLe6XSWjdlPLWn_6SjrsFOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOm3fAr6qsoAFEJW9Vg_QdCA1HcUh5reoiGp-HcIwcW63m2lBU8WuaKhNSTHOwrDRCyj234OhezxawdOjEIFbChIJiGfylXbWMDKEumjxRt6mN80qMp1C6mMygdZvUrKbn2ebf8WGbe7I27-BZJzRVnPcnUu1Rc9no7sBzUrT_cQ6FCfwB-kj6ivnPjPqWH7Rqlrj5yHWjzY8t0-5hku6MXVOQ35svijKNphU-9ELNE0fIpQopiUwDVyFV190SOjP6vxNgjiqR-N0oos11uPx-dQDOe7AuQvpSPR-P2_GPvbPta6QQs1fB5stqVcA5n0CGusR0JncZrFLBfH4HOGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4p2L66uKRkO6YpZussSVCdQn8EYsrJXDWsvRrOwAJOtRz4lTtx95vKFJ75E049tbPgvCg3bDg0BkXXc25u2SHhoi98UH-JjFBn5js0Nc74ea7If47JmdGYU6uUNhYTpgiiRy9w1iH-iNob79P7mQfy017_KjMMUDDELzqBJIzhhaFB5qTORLxZx_8vrLd0q7NngAZ6tYzSq5jmZg9btv7RGsRECO6ixTG7xlyqoe771mqOmEa0MGkvUTXgW_bYehJ6lZUmBvrNCRYM3KkxQxCmx8TXFckzXTVtqsF7L70pIabN626Vgl0G2yVNsaTow6CUVbmW8KSkUAk-a6-_jnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-I88LsDztrwisMau_TaLVP9i3lbOGJ7oEq6_bKKjhjirUA9jyqEQWTB-oOSCdD4p5FtRBXdTE0Y3Vcg7htaYFuya5dU15NOOwLE0Jg2O_2yF85SZ-kJIbDlVAOSergXnnNlQcGq-aAd9gh0n4cx0c28M2uvEwBSmiN8is8YFl59q0MlC7G-qoMlrIu7Aqx8e6PoXvvl91efGuF5ItJkqCqf1VGPmiH6VJM9zSn39JP3GfN3kmsSp7FNowU9Fv_V9n85DAH-r9JxX_2r2CSfMb-i-E8wf2-heGbRzHfd9EMgQm3TXp4XhZjZmXJud2w_Ih7TQJj7u-kICfs6rrJVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYZumLFFb7Oe69PWwK99dWkVSI7o_dTUqUlL1jDudagk9Lb2q62QjtqGsvNCxqMgm0AMExkCRcm0dz6EL-cEuJ1XgWEPprD-UCF7Lihc8XrVkAyLFX-K8KfVjLCPrYSKgp0sgz0OV940Ulsq3IWTcf9LYFel-TWUHyU2EU3u95vuWtMWtpNNGWSyPEsD8Wrs4AX-N-QCZvjWYGCFAG8G7xYqd1FOPaiJl8qfPqmfLzI-RbfduKi6H0ytWQadZBBeS5fgoutmPcJHYYjVBui6FUViIjYtU7dcUq2DzDsian3AC3KVX23hhMdm8D-vj83Irt8tooUEMfHaYULVZRwyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSLMCdNCtMKoleFBfCkU93kkMIyBfi0JpDWitQcxwBXrSabdYzYkmKzFXwbKAong_Xhyufxv4iz8GCoUHEY5Yf9-LpW5wiiJtEHVG4Sl80oh4_oAwGXBGFyPSjPkP-CHq6BEV-gdG09kWOLTcoJ0A4CLzsxuNVwiJXtrp-5DN6dD158dgZ5sRqNhfJGnT7yDCtIYtB0EAyAy0t3QPUUN3VLMlpuE9nTz8wZiRHd4eyqfLArUoV0jpywPaL58JFgYzqtqb9HE_plJ77PxkZNz7UAxSx5SZzl9XGH2HWXdigxXUbCZ9CKgxykPeXtREHP0vonsFoyBo9wt571WmJHvLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuBOXd3bSmdvDcPxbsI-TMKm3H5rjOoZIMK1xV93wKWtfhybjJ1oinEoB_h_WB1wI80zwA15BNXYVYItirYOLnfVGJdl-iitlgV-wmSv3k5PX9u_V3vgSKcaGRoLnvv0EkRPGIWLFE0iH0WenaHINT3gjnpxrqmv4zsd-iEQ6YJCrsHs-pawjCAgShjuHGNSuiSIGN6u2HokRYT6EfNn_TQX3ygH7_JtFh59G40_lE3UlqJO0I88RpyNmS-aUY26IUg35VRhkjGC3YHC97CgVZzkRnoOG6Ndohw0gnr8qskmA29kYjfsDl9_ePxkxpAzu9_-vj2b4ju_VZAmeqWljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl-YS6MSOJ903gH0BOteABgUcW_bHHYL7FdSd9QYRDDrNtvFPGqbUsojTSwY9E1H5Q_T6HVuRRBSi90VbWUkuNdosSCzktE3AszT7uUGYfduh_zPievQG4sMDH6CqIuptPqbPI6thYiBTDlGgv0sWeXPnA0ayjDKxRZpa8pOury_RL1-dXa1hfU5XPp6JXx4FCy-gvehDQPF5NkvijMx1rzFyuc0F7KFwOaNY9XT1M-h2r7HRJrlyHKChDJzHbSDaOlDOA2FpSJ_JF0Uky1fW3k3yJl-8qNI7HholoipxfpYbgKDgb53r0B4WC5WPiOSn2k9HDn7gG6YCaO4OvqJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=tp6HchptQc_CTKV64S-Btv_eJGKc1R6YAT1RNnKai4C45Hf_gwOjbzAa_WtjhwdCBgxTU298NifT54v_OhMne7wc7mL4cH9z7pKLDDuhYFHw0oTDTKCCSa3uS-z61a8fRh_hQg8NxBfJ7QGe9ZeUuULzff_tjJtn139PeVNjQ7wYBpNz6c6v_OfmcQMwkAXG2tSOAn3jj9UjvoignRPeShpt-gHM7cmaFwraFJyZOZyhdKK9JX1-5OzYHBEkPuuPi594hi4DQyJnUanEkCkKh9y7SHsf81iyP4vfl3JYRs9TgXC6CnzHnmjZAVQ_UhG6kTm8OeGtKhD3WEpSI9sUtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=tp6HchptQc_CTKV64S-Btv_eJGKc1R6YAT1RNnKai4C45Hf_gwOjbzAa_WtjhwdCBgxTU298NifT54v_OhMne7wc7mL4cH9z7pKLDDuhYFHw0oTDTKCCSa3uS-z61a8fRh_hQg8NxBfJ7QGe9ZeUuULzff_tjJtn139PeVNjQ7wYBpNz6c6v_OfmcQMwkAXG2tSOAn3jj9UjvoignRPeShpt-gHM7cmaFwraFJyZOZyhdKK9JX1-5OzYHBEkPuuPi594hi4DQyJnUanEkCkKh9y7SHsf81iyP4vfl3JYRs9TgXC6CnzHnmjZAVQ_UhG6kTm8OeGtKhD3WEpSI9sUtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=GKNTtfMxsMOXvfeuGhIW2nebU1LnxRGO6WVAzXe6ELmlMKji4hX6X4Xqd1psUDEdyV4y1V08786fQaTLRXcolT3iqbjHdndtyR-7hxOxXW5LpFNGqAXHgz-LbRbHh3xoNYwpumz0P2EJEsmdVOfwcEB0UcqpC3LOd8eNlUSuF2pDJSqDWRqHtaZc0kE0yC_RD-IjzI4jiOFMpv83RSImY-dhg7RigM1TBGrbosl0ifwtbZSJNSPJBefw5e8Ylc4rGYrLNQSf-vlTtAlNGu9FRiCV7kFWUX0WxDd0W1fuH7iEg-r99Kb9vyXNSBY6GUuZj4-1IOHTb8OVT5tLv05cZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=GKNTtfMxsMOXvfeuGhIW2nebU1LnxRGO6WVAzXe6ELmlMKji4hX6X4Xqd1psUDEdyV4y1V08786fQaTLRXcolT3iqbjHdndtyR-7hxOxXW5LpFNGqAXHgz-LbRbHh3xoNYwpumz0P2EJEsmdVOfwcEB0UcqpC3LOd8eNlUSuF2pDJSqDWRqHtaZc0kE0yC_RD-IjzI4jiOFMpv83RSImY-dhg7RigM1TBGrbosl0ifwtbZSJNSPJBefw5e8Ylc4rGYrLNQSf-vlTtAlNGu9FRiCV7kFWUX0WxDd0W1fuH7iEg-r99Kb9vyXNSBY6GUuZj4-1IOHTb8OVT5tLv05cZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS9vt5GAHKDE3bmD7Ozcwq7mrVkr9AHC0wZNdQlTTyBg49vJYhtwFJSvgjTe0FTNtghSjGSnHbu4-Rnw6Ir4nw7LIH5VfWEJ16Vali69WH0PVVt7XdmlWrdFnvR7NMnWuMiLb3JI13QTTsIAQtkoNX3CpEhg1n4IyO-UFkDpvAfLt1jtrGKHbvYrVVayDqErk60jXy_k-vPMGvNV3SuhZDL4DPgAak--PwEYP9NPB_9agbb_jXP8FFaBK34ElwgDHrnSasW4XkcLIectzveS8l7VRo0ih0bNohHEvRWKanIvv7lYMVZjdUJi6vwocn2ADD8zyizU_i-SIzJFZ7-bmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAK_r1UUx76Vr3X2kjZddnld5VxWwNax94mvmtmDh43Ivyvhzp8ESJK55ON8fGJA64fsZnj2Q7qzGTHodtQsV9iIaAPeRS2o9IRsTYAyji2hhXgdVm637xBnKejoJbxmL66srsvlGKwdvp3hHAUeasH5CineJ6q21aCleI8UrlqsRgsmVH0rhOBsqEfMD1qlo7O2g62Tbmwe15RjNqtiXH2FL7-u84FRUPAwz0anlj-20197fJFb6P7CnnZUHXKgtaGOJ7K1sXLIa5D_7C554Owl0xS9ghmlvew7M2562HJIBZ_NaL4eyt0gRweD-faEEAr3_uh1CYuH4C8RwbdoDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWcRh0Y5A-N3nczPwGalkzHbU6NRGnPwGiiUT1fttpwPnqNZiKslao2MIqq8OD6nNs_p_9CCQvh-5dHVG4oqrBpvWTbS9kd5BCoArHdp7unX8UqRnKypyNLQejTiXD3uZjXJy8ZsDwbFrmXYoBc5m2zHTICuePjT9LQ7-klpM-LOkTz3tUzaRBSBjkNJoyyp4Q9JjHfnIatZ89txGcuJMa6kkB_2qP0Ih-cATfEWg8jSGAz47gcvNRl8mnN4te7dhjiUKIQZWv0pAibUQ8sxjfMAys2AEHoA0HDGfBZcZg_SIEGKO_TJdPkoc5j9JPcinIfiaakDpHWt35CCsGcBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIPj2bCTBpOQMqMdCaqOtNbySqJ_a60LcBCqHICaHzeBv02nDD1Hj4Jt-ANOP_TiZVqdj6ABkN74UOtmzvRnuUTl5XLze0hXbOr2-yv33AK377S2kdpb9sP_4ttOh206tVOKxniKrvhAyb5KjLX2xunS8BiSwA2TGU2ry4zCSUfQxK_M9TdiiNEZIq5cBIjZR2_ec7jAo_SURcik5jJC6B9-okTRWOCM6ntNq-NiuMVCjvalq4PdeZ78l8uQgAybd0qmjKq54veFTlgVx0RrjBNL9Zks3Y9IibmAF2aXimwOpg7YLzgdp7B0vY53th9FggWSZezRTGB8DREryvF3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upZ5631R_O9NuLIofs5sVY5m1wnnl_F9GvbK4vbJ4qn9WqMx8bvtepJlSwmyRK_2EEbLH31xmdfZnrW_37rihEOHbiINvW1sDA4fXkOzdNI3y56YgS-9FYMGT-avdYTYarRyAKkv5IPQpfHm0sq3QzU8GavnMInWxKUeg-7vBKKrt7bFJvMIr0BTJrB_4X5keetfTbr1A3vd-__2EamjWlYJp4nz9CQdhaUfdgMlqS8B1PCm_rqcOyWoA_BLoSPEG3aj_Nngg687Rt-eSLcg1EuRIKNNfnt1RXnKOp9iSthwOyo6eaaOvVM3ypxMI1brpMt5yvl5uII2CuBRontJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZRP6b2aD53svdYEe3jLkMX8If1dFzVA9Iu4Bv2k2ys3RARsHLJ_YQ3LS2Kk9vVaxi5TUGfA9w-ELQJAgxRVJTKt3qO441MY9mamQQ6JINZ0cw1ovyAyCNAnlVFa0Ng7Z-xiDKhb84YqzPgNwxnO5rQ5oFTP8L1hjty21N2jGfREQa827g4OEJsQDROqRs5_qGvr4kLyeDAf-Xc1wddYTxJbdUa3SSuNs7fqKPC5iBtRUarkqJe8QqZ2352Hx_FEbfHltYIY8O2nArLeCaFKy4KGQs3UBLdZQJiF1lhwoKAHW1SXRZTGbvZTfYOMf3t2DZwUIgaWL7dvIwmEmAgkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNug35QsKAh0k3Dmbou0oiDpIjAX6WJ7X1GXIYDhKCR7rFUiuFjJy9DMd1NS3rNeW5U2I2Gm8K9uP2GcHGhW0uAGWOi5YVTXUT_fm1MOWzh2WwKFFI-qfX4gKFT9Utf6PGRZcqNQ0ZO96Nt7-dcp8VC8puDx8XtyPW5z_VwAn_qE6awb8sdQtn5ZfM8CW2DEVo4JkVWwFi8bk43snIwIy3yaYf6mr_H17g9jV3I8QouIepWX4taB_qDENcxO-nJ51a4NCH0IlazslJW0fSDjxWq04FZAawdo7Zdl9l7ElRAJKj8qbLyNewkxx4iNE9qi61uMwugffr2gtjX80HK0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STRjkt-KIUlvrdilcp4HTI6RAUMgCLbNaadN3WtF0F0Gi6bHTarPu48ggX1oz7tGKYJ1pYSimTUrX1yCxwteA-bNamMiyGCUuk5B_4OJXvQuLSK8eTNgvKSE2nLKoKcJTyBUMKVTV76e-VnbuGvr4XXQQlG_v6j1eV9Dsqbu9YnsodOU4jYBJWzK82NKOwlF822NBb_zDirqcDkbexwpDgfrx2fXz8eElgPdq59PB3c7p-dvVMufUQWBsjqeGMVg_2_yYiqno0Q7e45QJRYVEvkmYRtY5fHE7iTcnX6AR847qshCHA9CQx3u2_gJSkAbFIr1RF1d1zWxnl2JULQDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MglzsFuPw_jMB98_QajFONAIuvNAz8q2UEr4vAYNYLtUhPly-WR1wzCQp9gjTRm2YEFq-ocycrOMxe0bte7qW-bS7wJBzCSXJVJB7QuT4gReE7MIPxRrRZ-7l47KbsTuNf40cPr4VZvvF2GDH5aMNBQ2XrvT_Cvghm6yC2chUwh_cNtDcQx8FMmSP0DqZm-KmnhUZbgwZvj7pD-AxHiVQb1s6kxdfnYT0AXMFJN6pCSDG4tEeFGSRvL10iRZgspqcKfShfA2EMxrRhssLm9e4ZRQxZei49C9eKEhNdvsFWu0tihwktcCe7m41OvC-jfaBNKeLC5Ng4oPaxYhMWG68g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=qbRAuenbGP3jrnv26R4BInO1QkYFWbzuz4zeRpetbgIgUx6GrCNFy0--IqC1H21x2i-pw4WcIQ4Jg0DUiRr9u2WAW0OrXuqEvqXhxdIE7Ymihw62ZiCNncXIW0De7EizE2bDkEUhkT20I5nhWGQ8tn5WXvji046rhUxAuj3zq3VQJaQyEFTamsf_WcTEnwuA5jXzZBU0AikQMSdGgb62WAJQ6dU87IU_SAtMcYkGH3mksl-6Ynz5rK5oD0R7Ae_GMXZLY7z5WdR0fLN8qbQUuWr9vOZpIj0NxQviLvY93puMm76ne03TCN41gj1fr4tYY5862Wew4mUwcxWZD5AxT4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=qbRAuenbGP3jrnv26R4BInO1QkYFWbzuz4zeRpetbgIgUx6GrCNFy0--IqC1H21x2i-pw4WcIQ4Jg0DUiRr9u2WAW0OrXuqEvqXhxdIE7Ymihw62ZiCNncXIW0De7EizE2bDkEUhkT20I5nhWGQ8tn5WXvji046rhUxAuj3zq3VQJaQyEFTamsf_WcTEnwuA5jXzZBU0AikQMSdGgb62WAJQ6dU87IU_SAtMcYkGH3mksl-6Ynz5rK5oD0R7Ae_GMXZLY7z5WdR0fLN8qbQUuWr9vOZpIj0NxQviLvY93puMm76ne03TCN41gj1fr4tYY5862Wew4mUwcxWZD5AxT4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4H9ER0hTqZux_HYTGxFUdy5mAxozGpqyKVDG4n5jYPXZBndeEQRViJgCubJmWkBQc8t0BQOIuiuhHbv4XI7kQtw1EB6WNyAhGhUGbQpYrBkKWKGbIleU41QbVkzb4aVRDNKjtNs5lffuYgWub9pmr9O3GCp3VjUqRjCpVqIIveuQ3w3VZBNJTamV5CEJ5kSWTqK0zL-ceUi1XR96o7KqNDbr9pPv-z3U4l31XA3cbHhAhYqilo4BOJ0ptijK0h48jzBrZBGCWM-RF1MpFueTczEegh0R6JxWGzaRz9yOwQJqTRx89V7shZnNPZFzH0c1dRGhufjoKk4_1-Kr2V1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_UEq-iP3taM9kgKK-_VUEcao_5QHElKG4hNjHu5oM91UU_KaBOoPz9XkpPqiTEA5Ie8vaQ-27-DQQytsG0i8tcNtbsbJC2yaXRWnaPKnY2GsnRSbSksAW8zhlAZZw1XDJiPgQe59iO4ghUW7HOb9NMOi1I68RqTuBak9vlYD-JubGbbH-uCAerfH-O2Y70EjO9Kd3jtj6xROVMS6QlgbfWMWobKupldqN3joPRkILEs33bOz8BMUULFWo2E0VdQuA3qJxe-g1c9Vjp6VNJVR60slNVej0j5bIkjZsOrxFSJjBBpVGR4LWFsCWjDe8yjIBCdQa7HJxJwtqoTFrtIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTapQ9BxfvfAz6dnEFq6bRdBiezHHgkyTEDF0jYL-pIXznJKilXOnq56NSbfnS1wxMRP4OjXs3urPLn1Hr_UYAUDdcglvpaCfZIIlmqU6spFGRg66qDJf1Jmbk6HY49R_1dBDfD9q7WIRdJvLe-kP9ZCkeG5BqXTMJzYoapwZLjrw-M9biiDyXSBDRcjIiHPbkiZqjCKdy-d0BFNJ3Vb42u0FBsTHSWweDnwAzWEO-EgFDwjTgfVqThiBxcTOT0Q46P7cd0iLFymOgpfszS5TJyJGaeg4UcR1exVK3MnVYkCiRXgbJ54GTMCXeNBh6tXWhiAL2C6o4gB9E_p5bnwXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJD3TtwGKOMLvM8SqXVdZit_jJpWjKJDoM_FwYy4KDYrcPJVdpvPZb7Spp-fozV6unf0VmdCUoq9ZEKiAGERNNWAIhPgJw7tR5MvOmLhiiigYVmu_2wbk6CoHukRwUvb6rgxWs8IOkY9o6BqYWdcvmMeE_v50evcMC4zwr-zpmgCIyVT0rgSTEGaZkWPR1z_8zJitmluvPbQHyh31hlpYzcq3vio7lrBWkCZzGBFHpv-2pW6WfCMDNXDExWYQRE_ldaeozKhjEDVfJ8Gy9cEZW0cPvbcv_iGb3tagJJIy1ysHfixrduIvdIlIPDM29n61Rc_ApBBswju3Jpmy84maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH0eXcxqIPgqCmxju5QFSeo6yUVrqQQ34nqWhZw3Hn5IEK0iYRV18FHKWJq0FNy_DD5F1aIRxM5f09QaIbAWzqpaTLq_R-g8YgzjoV4o0GoUwzIiQbPrzxe4AUr-Ag2mEQj_iaVZYi6i859iouKLCZYIaF9C5IwK9sjYFl_oCPSvAcIL5Eqno6yc_0L6Lzyp3WZcCGrLEaY9Dd_rQMh1jdYcYnIAMu6z_WhCDbDALVLgt51evo0T3JDONZz_QycoR7SPa7RNzzxHA5cmjj6MbIS1_a_PV9vtrVPNdqx9JoEflWi9V5aJtRnt0xnNhJ4VUYPR8syPJoer_F-NIB_BQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8x1QY8l5hkERpSrCkVa7D1R0BDts7xQrmks6vJ4ftrTsE5EEbk1sIPtMfkgOKT-4XI9-Py9FYNxs6yXks-9hwOPFFIM0Mo18IfQasW4wJc1WK4FZhj3w5h78XzB7i703JQdSpPnbzi6u6j7yg6nltGuO3JB5XsXsjn19R8zXOkckGrnJb2GQV56WcXw48GGmeHRCAfe6g5IT8RH5LkqPOdPjXm80CdxnYZQtGX_D5uA1JKi3ISPeKPXs4WRo6uEtSnUARUIPzF0wFQBcnQ7lVBIK7rnJXXWtSxsC7UJzuAGYcufYsirWt3SCGR1H4TuOmXjFuyRKw_2UCzJrB4law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=ssNU2orMo9XCHjkexkwnxYV4L1m0CyFxnOeytDiJgkU61GTXo6HCXsiF0CHTqD0IIEK1gBTShMwHPCn1WHSCkJQD1uQNVQS1K5KAWTSPdgTIJoTL8LEkLK3G4miRPns8pat67zWRQaX2xv79qUDgCLFssnjFnt6GD0ONqHiDhm3A5tJFTTakHziV1HvFxpEn0M3n_1kPu-4zv_lcN36wvN2zb6Z8sVqrdqvEaG4K3BULxTV9CBVOMR7s2mkrWmLToKeu2LJW1kiM_NoZFiDsKQzheworPt6cybPhmPAcPVV1t_SSzuiA7c3o8pygvqzJOynsBaBBmKEJ17ccYB-GYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=ssNU2orMo9XCHjkexkwnxYV4L1m0CyFxnOeytDiJgkU61GTXo6HCXsiF0CHTqD0IIEK1gBTShMwHPCn1WHSCkJQD1uQNVQS1K5KAWTSPdgTIJoTL8LEkLK3G4miRPns8pat67zWRQaX2xv79qUDgCLFssnjFnt6GD0ONqHiDhm3A5tJFTTakHziV1HvFxpEn0M3n_1kPu-4zv_lcN36wvN2zb6Z8sVqrdqvEaG4K3BULxTV9CBVOMR7s2mkrWmLToKeu2LJW1kiM_NoZFiDsKQzheworPt6cybPhmPAcPVV1t_SSzuiA7c3o8pygvqzJOynsBaBBmKEJ17ccYB-GYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=B_Ckjdg1D9BjQ9t8fXd0LkasP2A65g2-GiuitdX7KLdhWSdWe13unkD3T579bU1pRx8c7g1mlqAY6t-RV9jtDUbhg96NTbrAnIuKn-D5pyDej7vWzvTQBYLn3mQJAW52fL4W1C26tH_m3X0801LGWlSOJyE8htf_MEZbZUxBYGSpKU3JiGlp1JlJODLAc5wojiyccsRvf7Qs2di7-GN2ToaD4YCzIieMYbRBbcNcGZoRqfeGHVBK0myRv1Df8F6ZeKKlOj6JIiXUjZOPlHOk-Ci8dpl6RHxaz6bffgeXemYdE4BJLNWHRZcRSGzoMrjhBpaugAq7AVHSdDvFAktmPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=B_Ckjdg1D9BjQ9t8fXd0LkasP2A65g2-GiuitdX7KLdhWSdWe13unkD3T579bU1pRx8c7g1mlqAY6t-RV9jtDUbhg96NTbrAnIuKn-D5pyDej7vWzvTQBYLn3mQJAW52fL4W1C26tH_m3X0801LGWlSOJyE8htf_MEZbZUxBYGSpKU3JiGlp1JlJODLAc5wojiyccsRvf7Qs2di7-GN2ToaD4YCzIieMYbRBbcNcGZoRqfeGHVBK0myRv1Df8F6ZeKKlOj6JIiXUjZOPlHOk-Ci8dpl6RHxaz6bffgeXemYdE4BJLNWHRZcRSGzoMrjhBpaugAq7AVHSdDvFAktmPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gddBdW_RiMqkD2pDyFPmBUQWJwbIhDh3_IFQc2KE0MEwaMvEHlWStFKvpAnDMQdDSjILrfnhYwiYz3I-twoadpvHIZpJV7FbJUUkGmqpuuTcDnrW4qWGuxkFvMWUjJ888IgfEg2WvveQS8VaK2w6vBh39D976jAUMGdhV6QHzPOZpHDnUONGgknWkcdMFMnB0Q4x-Yp2uvFGSDDg81NfebUIeKdAbi8JbhTojNYEL7xLpB3vsn8hPxb1ppKCjvvZVunujd68SR31a9ioy586QIhMFSRXa7Dd35dOVVUsKivWw7nLYqdcVXSP4mTjNpm0Z4_5VnRo41WjfBLzCaarJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhZ3WXcp-CiLbSDB4_1piJUGPecykOZTTuPVyqQWEycrcacwOvV3f1UVrBgbHnHS5HRe_PkhfODVimN0pSGicCpttEyl-eGss6XEpyNruUUpj6aINmJgRaquRnmIk-ZtVhMceukll8U-Ug204iz1WsltS-4L62lHRbvgGRJtWLdYmGdq4GdUkEQy-De9IrDgxqQod9t_-74WR5bcoGnb4qI-BJbJSRm7TRFnXXS_6bTD22QGrcqa35Q4S5J3uXZ5fUpZ_dn1i_6DpjKPNvWtc8ek1RpElY5MSYVTiQ-3tsZGhzWB4ijZTje2oilWWW3zMKG2A8J8CtUNwFcPzPXgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdqIX5BcrEqOTAO5EbeXLTkLSPg4-7h0HOmDOlXWHsTzpwxso5bMajjkRuMwAmFsnl61ZlO3dvprv1vRm-mqIHvYivieE62KwpBWv3VtVwUsFCqeKJBv8BGTH9uJKcMKPOym_8EaodXlsr_Vgh_kK5fSuGSKVXhRsVxOlnpc3nI58zmJn9fWVExtBRQ6TKePnFhugqtC-eZXw9AUGzlIXhnRJ_eZaj7GR67DTuIRkm73ozQnBdYbLLp6rx7lC7ktoPsuHRjyHQs_nLtEA_O6ao7k4YPoMHN_LF6hHHuG4i1L6zyig8RRIf8JPVURjMNsMfqrL4MtiDq4QyBWRK2jfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJ1xRpN8E1W9zsyJsLKHYUTAXH7E2lwZMaXd0mfpMznOau_xE7sEv1sbQ4G1sHVLJxxrMiIReYV6UEARhs2z1vuevmE9TBnSlzaG6woUeEsyDZPW6rFykpZxuICf6nEjKBOppqtOlnAZ6-WDu1aJ1ZBxFEZUhmeJ41whrnz-oevKIv-ZzBVpHcldBDTA_oXratEFslap_mxeSPeFyP6wY3z0623pVxJGh4VU7m_UisIza7C_iBWa7QzXxxnhaNUmpSJxubJv5HmsIY_zaBg11e610auex6VMDMGvU1sX2a3ueBObM5r32tn8J2Q2njRx7m9TjcveAx55b3WQKNIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=kU85HsrECngCUzb12QEvbCJsdsEOltbjxvD4alp7aNZ9XN2MMtkiAIb0ZwsYhy5poWgowPfcj5YW9VSJqC4PSzecirwlkWix8sAgxXiJASepTr6lP_-AJn2gMp0bM5bE3TpdrD_0FaP0pBjpmYYQ797kWPIGhxzPf7RCqdFGJEYjkgDIKrwZuV2GQXZXKFlRiImlzkbdkaW7hjZUbjDKjQZ0YVnEwcpp5TIgF8H_XqLYxukl-g-tRY0i25J2o7-37Uz8qYK4-2rQ9HWbg3FNZbc-pYm7ZArGhjnh5LaVUUx5lFwaXbPOegbQ0ShqUZ1WWmISIchqYeNSySDLPYpC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=kU85HsrECngCUzb12QEvbCJsdsEOltbjxvD4alp7aNZ9XN2MMtkiAIb0ZwsYhy5poWgowPfcj5YW9VSJqC4PSzecirwlkWix8sAgxXiJASepTr6lP_-AJn2gMp0bM5bE3TpdrD_0FaP0pBjpmYYQ797kWPIGhxzPf7RCqdFGJEYjkgDIKrwZuV2GQXZXKFlRiImlzkbdkaW7hjZUbjDKjQZ0YVnEwcpp5TIgF8H_XqLYxukl-g-tRY0i25J2o7-37Uz8qYK4-2rQ9HWbg3FNZbc-pYm7ZArGhjnh5LaVUUx5lFwaXbPOegbQ0ShqUZ1WWmISIchqYeNSySDLPYpC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz_HN49obTYBvdQFqZyavQz3WBtJTlD2EO0oqBWzATPnpWb7OMPlG6jH6ZxbZnE0OjeqdnQdroShdQ3iYT17IC3cSj_HQRefzwO86ZGjHxdM6rKZyrM_NgRq8OPKHXbhFFEJ3GLvefSky7NRM3kOXxl6wgpUxahbD8iwQOmE2xdPlD-14fleSYXFCHRlD7vbQ-AW9Ms21sQ4A8r0cnhpi4QEIYXZFwNKDu_NLcHqz8fqkY0r_WJzbgubCX92YcxCaQZA-zXqKg3Mwc8PWfzRehSeoNjfSd72WQi47HvlXBkqyLeTUBlrPNs24elZvGkrTmEzr1d7AOKxI2HUlLAjHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=fUyROBfMbcscdoFbtXvt-XigVRaDIpLr5Q1MOM9rg58ZlvF7reGyIm_LYG0gLeqmmLHGbZ_bdnaAwxOY2lcjBvJnaJsmeuARIMhE7IdrWOG91UlTcf1ZLWJ-_3Hsl9LtQ9vOkV3FNoVLiyaRHmJytJukEfDg95NE5iadOVkJiJCd7YRC1kc7NuwXnIAI2IdW9SaxDhZB0HgPqWeyHmnhkLiDDbCEUIjbW6lAOgX5aSpmKqxPrJHQV1pQmmIYXbwWkTkY0_U4zfCKWIV675bZh6sP94cCiRkOwGrCMUiqiMm0YSPPyX7GIuE4rsnTuxPTGXlysxu2th84UuAHTE5GZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=fUyROBfMbcscdoFbtXvt-XigVRaDIpLr5Q1MOM9rg58ZlvF7reGyIm_LYG0gLeqmmLHGbZ_bdnaAwxOY2lcjBvJnaJsmeuARIMhE7IdrWOG91UlTcf1ZLWJ-_3Hsl9LtQ9vOkV3FNoVLiyaRHmJytJukEfDg95NE5iadOVkJiJCd7YRC1kc7NuwXnIAI2IdW9SaxDhZB0HgPqWeyHmnhkLiDDbCEUIjbW6lAOgX5aSpmKqxPrJHQV1pQmmIYXbwWkTkY0_U4zfCKWIV675bZh6sP94cCiRkOwGrCMUiqiMm0YSPPyX7GIuE4rsnTuxPTGXlysxu2th84UuAHTE5GZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFuPM9X_9k8wuMxt9CC7U9looQX16Dxx8HqEhFc6i5N8p_NAM8yCI_5YVSvZ7J1YN47DH9uCoRba_7yAsvNQ2Ck6W2bAa3RQqnWd9EOM9j1ozICaVN1p4bA1nt8OCGjLfcMARo_37AH_aEKsIPZNXbGeMz8mKvak52M9IoAPvK__Jlp5cdYufTo_Pbu2-N9zhRh4ULKLCcJjXnpaGeArHvwpOhI_fplkEulqxePJ-9N8LqqE1igGATwRmjMceLOwTLeIo2NhekARIj9hLT4oDfjCt8lwywcWi6ZX4F_wbZR-62cuw4Ma13hBm8_hrsXGQYW4Is5l_52Rf-S49yCCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=U36-zLgQ3PvzxJWzszReal-1RUIq_5jbXj0-e7QXvW_K3Bi0woDc6KreD4-7O11-LC8FbQpZpFrPtI4gqxdP6rBf3hMLXs0NJwkisu42ETfciCeeDoNw8J_1NAKAby7gCs5T-v-lA88NC-iRHY2R9bIbc5JYFTS4W13tKjOvM--FauRWeIpSlUeUZZ72jhiMItkTed2hUJpcsVKK8U3r6ysD9LdufKsgPuUfAF1hXLtfKlbg121E9zu05VO4fcQOfSVLoFYenl5v4sCt8wONemuwnMbOukMp1QDt7gtBZbtMoF-DqzoMiV2Gj35tWu9A9vg0eRUiXRzBGABcgXfE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=U36-zLgQ3PvzxJWzszReal-1RUIq_5jbXj0-e7QXvW_K3Bi0woDc6KreD4-7O11-LC8FbQpZpFrPtI4gqxdP6rBf3hMLXs0NJwkisu42ETfciCeeDoNw8J_1NAKAby7gCs5T-v-lA88NC-iRHY2R9bIbc5JYFTS4W13tKjOvM--FauRWeIpSlUeUZZ72jhiMItkTed2hUJpcsVKK8U3r6ysD9LdufKsgPuUfAF1hXLtfKlbg121E9zu05VO4fcQOfSVLoFYenl5v4sCt8wONemuwnMbOukMp1QDt7gtBZbtMoF-DqzoMiV2Gj35tWu9A9vg0eRUiXRzBGABcgXfE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbNXY2k2TqjSoeIebP6b2O3zGmqgNYxmAw0ik2dIhranCF3KErJxiNZdN_poBvjsxbblWotZ8YqNz4GY85QkJbVvgQxWf7AU_Jbp5WUQTZ43QVKswLzYB5Gqw_pgVEWU513Dusn8H7TD3p32iAtJe7zVVg9zwnudCglliOREkxPGCvZeKOUgl3yFOKeh7i2-dnZ2E9ZIVDNN48vTmpg4KiR84B6zMrma1dyU4sVMsp9qrbvSov99QotZuV-rpR9p07gOoMdg2VuOloLZX9hjTn2j8S6fFJEJZwLufi-T6DfIldktL0JmZONpyxzANrNeXxXWduv8WqCWthuBbT1UEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=qGN9snL0Js3OBVJx8j25IGksXdZRWCTOmzPgtizM3btzxVJi1mjvIXXI9SeY4SXzIsoMk3x6vb6FVFdLssPULG8Jh966UaQlWEVxJy90tZO3HX39nEFcHs_OF8QxXot7YmrgpfGoWUek_ir6pFw8GVe2V1K0w9iPsV8SKYnyE1Vn5d1eS36fkuAv-XomTKbp6Ej8GhNW_nCzLUMoPTZhp62GSxxHqIVXOmJfLt67pFMSVvIgNsLWU0C3McW3RTW0LR0jx-VncNMUfUDtsKEK47I_JSuUV0dv-vN0G-ITFH86qE2MbkN_aRVfEqQ09zlGi5Fycmy_199C9E7dJjQ0zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=qGN9snL0Js3OBVJx8j25IGksXdZRWCTOmzPgtizM3btzxVJi1mjvIXXI9SeY4SXzIsoMk3x6vb6FVFdLssPULG8Jh966UaQlWEVxJy90tZO3HX39nEFcHs_OF8QxXot7YmrgpfGoWUek_ir6pFw8GVe2V1K0w9iPsV8SKYnyE1Vn5d1eS36fkuAv-XomTKbp6Ej8GhNW_nCzLUMoPTZhp62GSxxHqIVXOmJfLt67pFMSVvIgNsLWU0C3McW3RTW0LR0jx-VncNMUfUDtsKEK47I_JSuUV0dv-vN0G-ITFH86qE2MbkN_aRVfEqQ09zlGi5Fycmy_199C9E7dJjQ0zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=VNY6UUtOHPHDQwilrVwU4KvrlQsEhTHVYwJ4Kr7lBY7MIUpz-UgieeWxa8FMsDAzTR2cjGw7egeCyVY2M9L8aJ0RHS88x99AjM5HosiHAI9Ys647uxjrqfyHLD1dbysOQ_qdbD1av65OAzB-qoZm2bg2QC0x2pZG7-ShtJONOPCH3gblM-6j0onKbWwUVmElfp-psR9s91w-yFaZ3q6QIUd2pX6P6-BThpYm-_iJ6rv8XMDhFsenPBlWXPWpO8zs6DxmjU1Btau5EjNyZalFqVuPHvLfUxAOUx-ACt9q0XHnaHUPx-Gd8jGFTF3J75ECE0D_OHWhx4cBI2ZFOV4EPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=VNY6UUtOHPHDQwilrVwU4KvrlQsEhTHVYwJ4Kr7lBY7MIUpz-UgieeWxa8FMsDAzTR2cjGw7egeCyVY2M9L8aJ0RHS88x99AjM5HosiHAI9Ys647uxjrqfyHLD1dbysOQ_qdbD1av65OAzB-qoZm2bg2QC0x2pZG7-ShtJONOPCH3gblM-6j0onKbWwUVmElfp-psR9s91w-yFaZ3q6QIUd2pX6P6-BThpYm-_iJ6rv8XMDhFsenPBlWXPWpO8zs6DxmjU1Btau5EjNyZalFqVuPHvLfUxAOUx-ACt9q0XHnaHUPx-Gd8jGFTF3J75ECE0D_OHWhx4cBI2ZFOV4EPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uia7ynyY89UIXbW_gg1_bKAK_72An7ExDG6jy5d9lwnKGo6MwqaqHtNZ49M2ttmTvDCXI1VFkP6CVo_7Poj4ITgw-A2ZKx8QEoorxeo3gnNGgx91XHV_ITwYi08YDFmbHDJ6wpwMo6uvkFQrSVDfUFhX7ZqvGPRNn07JkTjjP8E8QgmtJTJidJSzXljH6csb0btAN6Wtyvr6TbMFsiASPCMCcO3z53N5qCcuDw4LIySKGw8wPN50jdEJz8sQ-kuu2kGz5sB2MF7CWPJy8GpwJVZv26tjJsScYh8eXljTvEI3hc6A88kfhwQxWvRBdTF2z2Md9nlH-Hngc0jRmNYtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tx1C3P-uSYQk6n5zx-gz1sgcefxQ4EmgXmL81ey-VtP1Shc0zX0-jzW0_o1OX7it7lbWfOu-KQNGGXvZ1AuBOU6Cyv4OUpF-_Pm-p380Hq9Q89Aafkbd2HM2GTmGqg1EOJQFPLxJGVmf4ezswb7-tYEviOQm5mXh2i4zsX3hAba-9W1AN2Yhq6hTk4u1qf-Q85Mm6p1NW-dspJ74cySdUUUFKPsJ2PcN5xYl6CgEQbDSN4a7zS7PYHd41jQuxUB9gDasMGplvM7Y13Pz8Yo4RsXpJGAAo-C4fWcMaMnFpHgvV1U5LZ6h9emCbaAxPWkE9YH_o1xGiBzRAtovu3_afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkPbAkXzm-yCTR9-Z4wNlWcvnCRL2ICt07oO8JTNrGB--wdHv9euJYuZvO93D7FcFlyiZfURpl8RDC8Lv4Ye45rpW332yN3VW31Xu3ris6-mS_iFowRrbpNbiA2GHpyZhGPu_SOuVGER-VNADZFe5QwBDk_x_NMBDjpiVgpsDYmxM1YzQhVJVc-1u_m8itM4zVNDI75FdN72y1OUhwIaS6pgKKyPek4U10pQk4T6uVYkX-NI_z4D55X29G8WUin8cgGbubVKrvStWaUncJR7FBAa9-zNe88c686R9XOKfNIXDRljUgw9c-YL7uyxW5n9JHyCvU9uLHHJi0nH17IDeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=ofF20Lhu1M1RAzhW0FwWtIEFTMVGw0N0bX9rI5XusLI8vb-minhG9hOhmk5HtIdCyPtNiDPVFCchDY1apIqHY_2WjcWjb5mAfS0lApfkY1dJkz4rPe5TE109L5Zpq4D4BsDayyRPAQXwzXw7KhZzpp8dlyxjId14OnJdKGKyoFkAvaulQhgxzemFWdcAqDgdsLvz6zB3JlRfViGUBvp5trL1htAMLY7KYGL_ttbMBmUizAnHggD8si3-3ACMztYp83VQ6SSP3r_O-oCWyloNfTeojBh_baRjmWgfesGEhuO30if5r5yL4_5OOajrrtsgF9XMp8n9L-Wd2XyU-grYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=ofF20Lhu1M1RAzhW0FwWtIEFTMVGw0N0bX9rI5XusLI8vb-minhG9hOhmk5HtIdCyPtNiDPVFCchDY1apIqHY_2WjcWjb5mAfS0lApfkY1dJkz4rPe5TE109L5Zpq4D4BsDayyRPAQXwzXw7KhZzpp8dlyxjId14OnJdKGKyoFkAvaulQhgxzemFWdcAqDgdsLvz6zB3JlRfViGUBvp5trL1htAMLY7KYGL_ttbMBmUizAnHggD8si3-3ACMztYp83VQ6SSP3r_O-oCWyloNfTeojBh_baRjmWgfesGEhuO30if5r5yL4_5OOajrrtsgF9XMp8n9L-Wd2XyU-grYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7Nih31gukd8iHbxz7G8lBkJxTVfTyd0UXsLEpxvqLKYfZGVqlrM4ZFKHJ9FkKJ9hjDOikfxeexh7ff_KgqZ3Ae8IyRxP9Z_JJvrPzlrf5BKcwkeuLfco11Zux94ipPfIkT4LUe1fMHdVEFT-HyqC34BYFMYgM40rNnkCRXmv0qtS64A9nOl-uY0ZNTRK1b29b9jAlnooIBMOfdllxhl9zpMMOOLduq2QwRLnIT6N4UAGJL5t2pE9Pq8_PiVnoHEucy3ZWhOrSr3gHFBdXDhpy_lqeAft7-jRqEPq0aiviUfaCi6oUOlr0xRTPK1iOQbsAZW10VmihjzaR1mWUlEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
