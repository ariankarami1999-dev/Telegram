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
<img src="https://cdn4.telesco.pe/file/iTlvKHoaHmCU_0YdDnUHUscsOCcq1E1HBRv7UKT9sQvuk1qwy8EkI4gp70CZgvm6q4U9wE2F57MLDYSOAQ4ewhct-C2FbFUdZeNO1l9cmZNh2rMiH83L3AiP-w3U8stC7K6rV5lgeNeLPmB5QHUS83r0ghJRN1MnnBhe-HjCJ9alMA8AsE0dC0iG-0LPVUT0rJo6qGmhx43UkQo_Y8PhdL8i7-QYYREni1esZy510zG9ppNuOZpMhHdEW4A8Jm1F2SFwOHxgUMa1hEyqr9o3OYuxRbBODJ1J-o04Ze58J7xI0XsGyd6_29W4essNzn2-8lt8njDTAYaUOWx-D6-bEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 590K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 21:56:54</div>
<hr>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uv94aotyjbQ6hsDuasZx8r4Yb2vH0kA04ioO__cjngrZ1tpTdEg4BlRC3hSGZmLLm5h0ixDvAlIlmFPEKu-ieE4AABORk-YYj30XzHtd7EzaCRd2x3LDguzTJAegwJhq2LL46DyixAZEJYYTqq-AGhE4nT2GrrCbaXY-tNz58TpfgJcqXWGvVBs7m3fyWRreWi8ih9K4Tc5bRTcqgUsPhM3RmeIZg3n7tm2xwqHH-eVpovqVBlSqtjHVOa99E9g38vcTwwrmpR3N_vIVC4bedrL9DSvjyQ0CNqcGZmeRlY9wrNdCTwUJmwhBgmY3-xn3PNgDy_qrco_oerQAgM11xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=qM6frFOb-iQDEDJ8LTOgwAXHzvEQcSBGf8SD3GUy6mOAu3JwBXZp5ZAL5UHqBTu4DoLHoO6HJ4L0tlPGxNesWfALRTp5I_fsVo0IjwA7B9KqIqVda2gYPAZRDJHxa_hRtxJBZCSYodUnuWo1q1R1raEPWlRkCAaVx-7zx9cdHy7dBUO2m5IBuqmXa-NNTzN2RvhJR68A7gHXaNsH2JPfDDDNOSmXGtUbIFUaX85Ik1vOPyUXVnzgYkJ65kINz_NeBEkx0IA60hZ69nJmbsEgABkFuV0paPeRg4Te0469lpwRJkO8qH73X1qEa0tXXJD-4Wrasc4PvjvnqQjFwLM4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=qM6frFOb-iQDEDJ8LTOgwAXHzvEQcSBGf8SD3GUy6mOAu3JwBXZp5ZAL5UHqBTu4DoLHoO6HJ4L0tlPGxNesWfALRTp5I_fsVo0IjwA7B9KqIqVda2gYPAZRDJHxa_hRtxJBZCSYodUnuWo1q1R1raEPWlRkCAaVx-7zx9cdHy7dBUO2m5IBuqmXa-NNTzN2RvhJR68A7gHXaNsH2JPfDDDNOSmXGtUbIFUaX85Ik1vOPyUXVnzgYkJ65kINz_NeBEkx0IA60hZ69nJmbsEgABkFuV0paPeRg4Te0469lpwRJkO8qH73X1qEa0tXXJD-4Wrasc4PvjvnqQjFwLM4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg8W9CAwiag-JY6xpaDztF8fKgXJp-i6CQkrUDL46X_EY3MR4Y28OIPhlWRr4QCFujEtuyQeb-SDYNDSU3ekdYeFNrbT77pWcWFOWr9o4-ulzaUv-Y0oslc0UX8qnXETkBYn5loQrvq5nXowWyuZvec1w4LhbtpquPePO6yRbUoC0PZlFNa6ADlzuuyG7vD9IGdiXrqTnrSGMRxrODSmM8twarDH2cN_K_bIlXz6CmmBMzR0M-5jKCYogFRQ0xjH6qRgTjry9kgrcujBgI8deyyxAaPodM1GKK7iAo8fjrbFJF1hBtzEfY11Y9kjEGSa5xBu2juh7LBwNuQshkDWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd5ZPDIL0J0LD1J1G1fCAqpCsLy2PHlWZphWn_Gb0Kj9_EQI0WzZsv6GhBvD8VvfujZNHDs-n-Q-uzkxO3VXdYY6NE6oS_sk0vqF57OVe53jolPwrhELUxp0oTgS-iQ2zAYvWEgl8jxizyQCf04wMRSbMuSmpPJyrwYqKtRjJwCCTSSMpE7WXD1FDgUS926JCRNZQgEURGSz3GJZQQmRec50-gr-J8R3uT5i3E1187I2oyNUgsHk84FZH3r83lrOh3rQPiagCG3WUnBgydK4-E1KNbl6xIWEY965Gpcluvfzex2LhY-hvQt8T-wuSLPu6RU5vr8l3XfP43xJXVLV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrJlRoJ86dCP54nps2XQs2252A2UIAP6E9UEZfHN2wt6yxR5K_8OO7WvluSphqfxRkXSVlZUUv3jIYg-BCoZhmkwZXHG2n2vujLdM9o1q4RGamO9oBWs3N0P93q8i4QSnKskwQ9srcqXaYYS3Bez4HoCcURh2D_GMphYKETzomZ6m5N27p8PbO5ywspYaexvQ7u4SvjkNwHXSAfm7nSxkmuStn0Iey_yQq9SBCfdtLlWKSRzZLpXjqDx_5VfiQ8GiSOCvNxSRzP-qXhBQ9uTsgx4QnsT3P8wPKanKyWkzHahFdBCFAL1ViPW3UwSTB1DwaGBy3ZU_Tu5TA_OgmxKgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEtYXs28TL8KX8XBbozD2CizNpWrRzdHU-3hzKkGgmz-of1g1Vnpxe2ytr4sE0K8LpsM0b6r5DOhMEj3ghp0NK79NgtJ3125TR_t5HD5tLqRriIAFAYJ8TfvFaS1q1SwcU5V4gJ1kBqMEe-qSNWDrDF5x5DBWaik5FFIN8z4Q9TVmBQX0GAXpZ0u8AWTf5Ly-w82mYaA4VG0zrOSU3GIGe4GQWhVzHQImWv2kIcfYbATUN9HBNbV3Ek8L0Sj-WSA36g5O04F1KDnr4v1CLmwkP-6kjHR91GzJvU4ajQ1J1NJNbQ2BbCU5YoyueSTyif16QYAXpVFfwvjRQqafLv7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/banVahDOnWQElsi9p4pViX_nh7efNeHLtnjbUuCpmrBRu6jOtQlyECxtG7Pbo-blHn2tMaVzpzkY47d0KASF4Ki1zUYmb2EEKSyB3n01dTaUZ2C3omcufhGF4rbVf6XkwTxm4q6n6YjcdgwB7Lx98FGXkQ5agUOSs-793AdMosMBClHdh7oukx4CYATXoYNsRUTnfOJLCyzrhc5VC3zN5yX48U55hG-TwCltI2-N9bra5zb9eWweow6qJJRVHlTo6srxCpQHTE374D9cirFDDHFybkH9V9RZk18Qih4380G8Zq_JY2ppS-RVj5UgabTzCP0N0Vz-SCf8rF6IACmgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29202">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvhW3OmnSxWMZk-Ew6h_Lr6SYTc2gRbEYGugX_0At6UgXIF0Gt9z4eMj8EiGYKYgaCN58nl82gQXy3yUC5EoqM7xhGsPfcVna21ENoQlg1Nn5cUqyjUt9fY_UmZCnrnZxLMKm9zTcI5gaAI9RirX2xGQh048GgaZcPG9vYnPmG5TWOo_PHlq5x5SldaggFikbgBAuBQ74HVclYHJA1lMJR496J89cFXBV3m-9F0tRGQGJDAGVtJBUUV9K22TUXZAXN7SJ9HvJ4dPhjMYX13jxYksZbVPS2Nfl19hEpZHd6j2nrb0SZTRa1bKuTWxubxCxmvamUNqlIWZ9NqXAEOl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/29202" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pluBGrDzRZLrKORHFVWeuaHgzqsC9A-cOFp14Rcz_kG-qygDftuBhL5PQOcSPy0HeGrvpLTBpn79QzUFJR9gfT4t2QS2m9UUirC0_9qJeMbKBL_bLfERvhJTUg0PyHK_KlX7km5mARrwxFk6cjA7TvyntDAZuYphTUnu0Yoxc8rqG8isBC2EuJ4hNRWy2xKDvBtyZyJ8sgbFD2AbQWxOccCke5gDWlVqn0u08BKwO7qh1EBga3VQM3m9XpOBsnFqrtISJSBHGgJ-76noTcJ1pYkQP6h56QoxlHTlY7SJ-u1prkCpsI7tJfXcn-I2aZuS-Y1bqyBBKY4zgXR3SIUrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
یوونتوس
🆚
میلان
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/29201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=ugtJMeX94BOvZML36Qble1J0W7WL6Lz2bvPuC3_C72xL1QJydOB3ALVB24DrfiglGkUGs3lE_TGBlGJo-QEmy2obIPCT-c-kJRCjI3NNJ4MOLd_VS3eVO2MlCBsbwirCuOIyH0vI3JWoJNby-w7mrqZ_0urnoWvtgyVQfbUoxAwHVcaMZ2P4OTVY7hkOXot5rLUXscBnoGMYtzqMkLlYq97N7q5LMpxAEhJidW21SV1lo-jSt4dxFwMvaz2ix1XHaeNX3NX0EmezGPMvoU9csWpjbSdpPD5_yYcjDTixEDGraTQX2ND5xpw87rdmvBGp9i7I79TnJrFbYA_-xLMs-rg4afBL8jwGZmNBVAMOHYchyaqcHAKwUlEEFsO4_c2PK9nG8LhkwV5pawFTJikCxhLibQXsjV8MAOXda1q0ReQA3sYIDig2ehG053hLlUMEnp3isDW-7j0ZXhHu8cD4yUlHpqRUZd3wCb2kJS-7LwVHYEc2i09a7DzdTGiKyhsbCPcxCRoEEL-0ne-m3cWRXeTfLXLQNQrkv_Abdd7iStaUv3IpCVtuVZWNnB0nF3Kx0WBngXHfQnyIKh743GZzednOStJREHjA7o8K_5x-WUsevR999FqaJR5UtBLahbUmCE8W459gYXGdKm2KNwDRX6HR5JlFMhusEh_iFaQr7-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=ugtJMeX94BOvZML36Qble1J0W7WL6Lz2bvPuC3_C72xL1QJydOB3ALVB24DrfiglGkUGs3lE_TGBlGJo-QEmy2obIPCT-c-kJRCjI3NNJ4MOLd_VS3eVO2MlCBsbwirCuOIyH0vI3JWoJNby-w7mrqZ_0urnoWvtgyVQfbUoxAwHVcaMZ2P4OTVY7hkOXot5rLUXscBnoGMYtzqMkLlYq97N7q5LMpxAEhJidW21SV1lo-jSt4dxFwMvaz2ix1XHaeNX3NX0EmezGPMvoU9csWpjbSdpPD5_yYcjDTixEDGraTQX2ND5xpw87rdmvBGp9i7I79TnJrFbYA_-xLMs-rg4afBL8jwGZmNBVAMOHYchyaqcHAKwUlEEFsO4_c2PK9nG8LhkwV5pawFTJikCxhLibQXsjV8MAOXda1q0ReQA3sYIDig2ehG053hLlUMEnp3isDW-7j0ZXhHu8cD4yUlHpqRUZd3wCb2kJS-7LwVHYEc2i09a7DzdTGiKyhsbCPcxCRoEEL-0ne-m3cWRXeTfLXLQNQrkv_Abdd7iStaUv3IpCVtuVZWNnB0nF3Kx0WBngXHfQnyIKh743GZzednOStJREHjA7o8K_5x-WUsevR999FqaJR5UtBLahbUmCE8W459gYXGdKm2KNwDRX6HR5JlFMhusEh_iFaQr7-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
درهفته چهارم لالیگا؛ شاگردان هانسی فلیک در در دیداری خارج‌از خانه آتش بازی به پا کردند و با نتیجه پرگل پنج بر صفر والنسیا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/29200" target="_blank">📅 20:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e23364253.mp4?token=CYFRr0VGoG27ZqcqwdyzP5jWl6Bw6MvggLWOATrqxOjDQ0VahgPcWU9IlNX2h95-fLugpDFQDt-9WMQMt11TPtCL_onTxr73awEpVif7CK3TGcsJO4q3jzSLtxYSsnTm8E1YqRqKF4VyHVwPfbRTMdDR954XnNkCDW_byQDC9nzmi7l39VntqvAtm71Qe80So4oEi50R77anSEp51QDwKNGgUiGUQeLLGGjzvORpr_V8vOifksk9S5fExyQRKsweVkF2rENGZ7rzWa9YlEmSTrgUw56-1Gb4k-FGZFfjP1m0_Vrg15pQ0rIb5A4b580hq9ejg55ShC7avOYk3wT2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e23364253.mp4?token=CYFRr0VGoG27ZqcqwdyzP5jWl6Bw6MvggLWOATrqxOjDQ0VahgPcWU9IlNX2h95-fLugpDFQDt-9WMQMt11TPtCL_onTxr73awEpVif7CK3TGcsJO4q3jzSLtxYSsnTm8E1YqRqKF4VyHVwPfbRTMdDR954XnNkCDW_byQDC9nzmi7l39VntqvAtm71Qe80So4oEi50R77anSEp51QDwKNGgUiGUQeLLGGjzvORpr_V8vOifksk9S5fExyQRKsweVkF2rENGZ7rzWa9YlEmSTrgUw56-1Gb4k-FGZFfjP1m0_Vrg15pQ0rIb5A4b580hq9ejg55ShC7avOYk3wT2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ کسری فیکس شد؛ ترکیب سپاهان برای دیدار مقابل استقلال خوزستان؛ ساعت 19 از شبکه استانی اصفهان پخش زنده خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/29199" target="_blank">📅 20:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29198">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIgC4xoKKvWTkaKD-YLrh6H3gp1Z9nFHPTyoRXv1ZIVDBUFa_Nwm4ZB8XEdIgUdNJbFz7UWoSbE1HcNiyxkLdT7eFZLYSmXM_TiCyi9p7xuSSeW1hHnQ9Purg7IqSNUa2wgGKkb2WXZRkVpuHEWGyTTj_qj24XwimsXvadZJKNN7bUdthaVvOursWJqawJarB7gWtravEstChCsqAjb4bWviSlZpacmQVUTrQ1E4ZoG9Dh3OvRIHfXcmGvilcJ6Q08MsJiuyYB6SCpzH6wWstviFKS2YOTD3bSMC-N5lNUTwttT0IXpWiW4BPXWKtJp9RNED_iut1CxGP3pAeo0ARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی پرشیانا از سیرجان؛
مدیریت باشگاه گل‌گهر به سید مهدی رحمتی اولتیماتوم نهایی خودراداده‌اند و درصورت شکست دربازی هفته آینده با شمس‌آذر از هدایت سیرجانی‌ها برکنار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/29198" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKPIkCqtH_u03FdnqzqcXqZUA7EcBtc_ORZMUVzYI736r159lZlINOphbTvMYQs2DAMd-vVFYmM9_wBQ9sntqduDPB7ZCRJwTvaJhSknfhK9Jzzc861gjXIHKTvqncCW2s2xq1wgKEYpr3LkU-AZ7b4g7gASw-YZ58sPaXTROK55jbQAjm4EQom8rPQJ0lVNPw2GFN_IR4tXVyNyspUj7Nnh66nwr1odDWjqCDiVj68QL4k7QPAMMbJrAS2PLriwz123QAeRVVhTrIHe2T9qIOhPqiofbSX_IUW3rr2FwBhKNCfdyu14coxnLBsqs8LMG5I61Xrt3U_xznsEi0HFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امروزمقابل والنسیا؛ ساعت 17:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/29197" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=OWZNnmuRdQ_qffINMrF6ICfYI3uUjL6-HXQocc7ap7bx5uvy-Vc3MJ8t0Anr6Rrz5EiWNnTahhSRysCDlmboYSjL58zh4tMMVWlF38vAS-qcfsJTuYYF4EhylvYHY-j-mCnXHeXfbtroFIYvfFvG9SCNpCP9iHHWQTPc4XqzUNA51o9szSlY-aDwpP0bt3GaycpLbejzEVd6bp8JkOwt_UIRkSesJwhRRF4J9Bl3fqP8qW9GdtUw1lcxdajFun7sYhhLaSPUut-BlpZSxZMu9kv8-26J3oX4qKqQ3TsoltYo951_8Gx2bnda9Uqz6A3U_HS8yOi784u0_cjVeXF1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=OWZNnmuRdQ_qffINMrF6ICfYI3uUjL6-HXQocc7ap7bx5uvy-Vc3MJ8t0Anr6Rrz5EiWNnTahhSRysCDlmboYSjL58zh4tMMVWlF38vAS-qcfsJTuYYF4EhylvYHY-j-mCnXHeXfbtroFIYvfFvG9SCNpCP9iHHWQTPc4XqzUNA51o9szSlY-aDwpP0bt3GaycpLbejzEVd6bp8JkOwt_UIRkSesJwhRRF4J9Bl3fqP8qW9GdtUw1lcxdajFun7sYhhLaSPUut-BlpZSxZMu9kv8-26J3oX4qKqQ3TsoltYo951_8Gx2bnda9Uqz6A3U_HS8yOi784u0_cjVeXF1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت تیم آلومینیوم به پیروز قربانی سرمربی آلومینیوم اراک اعلام کرده دربازی فردا با استقلال از محمد خلیفه و بهرام‌گودرزی استفاده نکند که قربانی اعلام‌ کرده که محمد خلیفه و گودرزی از بهترین‌های این فصل تیمش بوده و نمیتونه اونارو کنار بزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/29196" target="_blank">📅 19:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAQAawG_FO231zm8vDhsdY7ujlvPOr6s-_13roaQGWlBNXOIOXhymfMJGjoONvQlAzPffO4NHFP63iTjmR8c4Of8kS4LNJ3MTI28K4rmGlqiXlrU_cPoXRKUe9leOSYnJwRJ8bw8FtLWi0VTYw2r70HTZ9PaGdmP6bmobu5H9k_avEjSrArtjLxe4NLCyt_n0KGDrM2F23QEmlDZcxpCLIlKFD6Nk65xGKytY9r9P6qoTZN2OLDnHTdLlIzsOwIm4jvyw4p1ShHf-baI-tS-pcwVNY1RmOq6CTNkL2QF-lhAjq4RbfaE8XaQka-2DDOrsBW6EIfGVLHWJZd4JwSWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKD5NVIppBIN59y8490ZD-1tug5TIeIDIaSaaDvx9ZFBo72ncVjo_aY1QYEpORI6TsbBlbtb4arjoE4ct8A1FME857TpjVzypnziR6Wd8fJAEp6e5_66A3NcQ8V0YU-bx_fBO9hfM1btd7I9Lslm46EpOt9kYq2Jhi-lhUJ-9_RO6FOpfwEzxOWM-T6t3jE-jj8Y0god61RGbqBMce40qO5LaQZ6OlqYvRE8HcAqSEKE7DvLjFjL8KzepcZMBHpdjf0oopJH1NNdIyODzjZdh4Addg2RihRZooEjOg3JRi4GjSA9miIDmeH-YikuNlUbkqa12ke2GqLM91uEl4sg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLVa2M5VUBFUk7y0KTArMu0Bkw37ApEGBEOHjJZkEFFIlPEfpXvwhPy_aejNS4TT5LvBZlt2XTNPmK8SQG2rPWIEhK_e_8ZsxKYBvW45HHvvLIkOvKBmMpOMrWcKIFMUAX6FrRRQjQZVpaBCFBJmJesWZ8woPdOnGUsVT5qgA8xOpkRLzwmPAUjetXvsVhT472vLkqxuA1xn64dEKWjPL7vn1ZNNfrVL3hWSMtPq2YCgqQj_ajV89gkEKt2zuLzGbj0OkAJa14WCLs3-a_WBgdJ13fbPLPU84vhqdUJzKR1wCrIZjAeYW2_cvq1EhAW0Q-W69F82TJjt6E_DRe1ePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ataQeQ07tUag8VlT6eKWMz6PFlFcnWAR8vSwxsbEYmMRFYygZqT3Azu642an_cAJiKI1DenX-00jB0u_aNmiKbfQ9ExH2RQDeOwe0Ai73FKpwzUBrCxFAH8cmqCniYWDTmBwbz6S1qzliEv6SxsTkD-NfD4RrgjM7-s7zUyzT0Ai33fr-Qa_cJnOnvuNbvPEZyUZ9lgExTGCWIuIh-ewC2HulhGHVuWh0GXJeJHKiWnZS1PZDLoUr3A67dnCR883l3dhACMhus6ghU3PbwDWomW-qV-NfC38OEPtSsFziq_dZ4EFHz4izajIiVi14Y7XZAE1IDQsocgv0Q1AwWdSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9R4lXO4q1W1qqy7R85EOSflJrf8VjnC6h2EpsvaG4Cpdg4mqsKAlyD3PXAGlSL158cbGY4SB5TbYtNrjNpAER-obLhTAv8ubuaQovXjLJeCuWS3YxLLM8bGJ5d3UnACoAUkd_joPL4-mC4sdr9D6U1e7Qb0F2DJMUlQ15ZkVNfAN2uKvgoOIMSXKWdAnGsfEb2lhq1r01XP5LiukfNkhCI9wkWYt1_pBVTZKz24siWywB6tIlHMBd2GtDVvbwK6n1h1isvux9r5baHxFPRXiGRC-Zx3V_Qed0dj4U5SFkPTdlBLUu1FIEl6D4muXr2d4_RzbiSePjxzOwuJJ2prUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29189">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txTE-ce9KWfrhcsBtVSaMIzJV9MH3umNQjizlsv3RgHqImS3ZsfURI1OVnZAJzYRAkjnCqIN9hU_7mDfgCmUSrfGvku8VEH4gOYK5B4e0UM-7JP-QGtj4yXFv5PTbfx9ir-qpFC0vIAjsHbMRyhYeCMCz8fB7uG80tVIu4cqEwWCedhHRsIIvGSEs2UbmZ4eeTwACXu2D7FRzZa9YQlxIAqq_XExwuqlboFXum8pQ4VYJdDB3xWEAsAaS-pHZc9yIHSodcLlEFNKPApC8Orrnndlw_UjnSOh8wHWcNrL9Uoa0DhZyjYCLsWFPlUEEhQx1DrrZAyiXJOomMXgQqf0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇦🇷
رئیس‌باشگاه‌اتحادعربستان:
سال2023 قبل از پیوستن لیونل‌مسی‌به اینترمیامی ما پیشنهادی دو ساله به‌ارزش 1.4 بیلیون دلار به‌اوپیشنهاد دادیم که اعلام‌کردبخاطر آرامش خانواده‌اش قصد داره ادامه فوتبالش رو در آمریکا پیش ببره و پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/29189" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29188">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgWPE3gmQhOqvEPOS_EteFPp79Ro-LB_ongMvrxCKvsPNWvyZXOtMJTjsJpb6SbygD95EUtY9hf2Ri6LEvTcQP4_oR3AKV2ECYr_izm1Yy4s8t_J4UCGXouDV_SHZirwZLQ0Spwk4hD6ZoarQarabC9qBbzimtqZRgPc0nf7CtESxlw4yKlMnbopdOp1OCJiQ8puB528urGBRYLIoSeqxBg4Z_jHWiPVQYAWE591YeyTYizEgmz-E6PnyFtwDBo93JQO7gmzbRVadDGYTd9WHa0yX4QWLea9nXYHIHHQKkq1EUK9NurGf4X-S2VojRxb75yI3Jr1sLoBnkHdJqvXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی هم ۴قسطه شدن!
بااسنپ‌پی می‌تونی از بین بیشتر از ۴هزار فروشگاه در شبکه‌های اجتماعی‌مثل‌اینستاگرام، بله‌وتلگرام در ۴قسط و بدون‌کارمزدخریدکنی تا دیگه با درگاه امن پرداخت اسنپ‌پی، خیالت از خریدت راحت باشه.
لیست فروشگاه‌ طرف قرارداد رو از لینک زیر ببین:
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/29188" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29187">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6gg6avdNPmBynAEAJLSO4aNsyWBqW2dA7ZNpjVeQdiCo5hRW_P3i_aOtjwn43tIUYhBE9NEjD0XG54rnAVdnxZk-lAzbgDDZLV56-EbiVmhlJgMkkuUeuyh6POlGI-ddzcr80j0fuGmXZR7DrlaTU3gfndKxCkeZvj7g4r-OrYwc1Ipmj59lkkSx-cmjdmbPMM_f5aHJLZDM5fjZBd_Z_pnMiRSm6w9xqEPcHOio_scs4UFe9YO1UmMlvvuXhU0Jf5V8KtLwR56j-RCrwEFcLxQBUnQdKIrbL16-T_xX9lieXnK2A6SYsW5ECsszC6BiGXVNqAtNb0FvQAlRHE_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/29187" target="_blank">📅 17:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2nZ-UeVdp2pDreRS5evJ63mwJu9CTkb7F94C1W01qQWs-SnfJYs3ZpX_gK4_ka9nbvkCI-zHIOBslRW33Rasa9dqjg66L5F8VG1xTOFOd-GSE-isAYEFJQ2l4dD-k5GrchGmDj97bCv1xEMLzau3qP1O6m-XihjP2Gqoci77TaIUI4kZAIjYOTp_4vAmCCjmLPsSmM1vYITCC89FPslMGqX8y_QgunuoZ3Tq0gKpiNbtwEt98NOqgVa8oMbsUzWVFTHXobEN2qgYHH_-QQSSrxFjZ9mhdSmQBR5Zwocf-T4Yx3lAPBhRxJKcabwgCtjg_zaCKvR5tmqbqDRPX2r8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV4QGQbUSq0slNCydaJ4Wvh5DLeFwpuVBngdRJbxhFCDoBB2eyqwyH0dErGXc91lvKqgi9ta2yLcT-xQ8m3f30JK9nqXOAVrojLRlZc8RpqmGfsXGvaq3FN4OMtKnDbHMMsRMtoXtDsP7koOKh_IYqas-F6LzQkXuGXhiWkiC2qbVBlXF2BI3JuCZVw1T6iuDjzLKbLPx_90stDPLgdhBsgxxov5lI0al6c2ukH-QWX1VfYCmRRWKqJIOWUN9jz6a48CFoiU9TFxmxG-95-Uj8bBS_rN2VrSjbT__BULQo1Zc9v9C6g6NT0eFAxIoTq8EORXW7gbpsQhYIhp099yPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛
ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/29185" target="_blank">📅 17:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwI2Wa_YKgBRTzFsU3-7pN8DkQ42YISkeblwIWGCA-KWCUM5reRsRs8-jk-YkAAdUJOhieoVtjG5JC3Pzc05oBR9kQ00xcv7aWk_7lMvle7tIhWDgWBSP3lZ3ZYhwUShZinoU-fI3Lv4vPTkyhaO-GvUcZg3DVQ83slL-proKhbrpuoXW_kIkuZ_cBw5ba5SqwR2wlh_hFOyh4rWzMU9sSeemc5nmekNgG8R0PR3Efrd8Nm5cCP5BRuWeJ_pKPSKChonKKCS_-FxLKx4A1ROHpKEuGfKOMvuBKwLG68PQ4m2h7yGgdip_zlKMLcewAXmwp0wceQzHEnX5e7xIiZHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته‌ولی توسال ۲۰۰۲ تیم پیکان یه اردوی ۱۰ روزه توی انگلیس برگزار می‌کنه و اونجا یه بازی با من‌ سیتی انجام میده. بازیم یک یک مساوی می‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/29184" target="_blank">📅 17:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=c2BBFhIqgLC9z93o3aVZmkNBddVxoYz3L_bIq4ma6B6131iC9CoEjvlZYckjix8SzlZQYCj-bDdMSmAQHk9MmGDQ4VycWZdAS5i68NgmHOTF27uWa9tmxMmsIbIBjkOeYBjV90FSiga5XBpPRID5IS50AOXRQGdleMewQzQrVwlpEXUzt127yMpWzsaA9Em8NZKPKZ3E9FoKk0NLi5lrPZvMlRiE36PrfK5kaHkXXqoN2yJ7bXT9pJMoSwksO95g3URVRA1KYnAAXmn-Ok4WGrLvjmKZOotmbE3aUk9wYpovH2OUxUZBCnWtrQRNaXI5Gthg8QZRNzlKZRulaV3uvKjmay8GSbtOnCNxhpvbibDac6dOymN6YcKAJwtkXgcRb7kSBf8BNmwd2K-73oA25V_8nTznmuujwaBm-5lGf9NSH7UFiJc5A9MmauHCK5PGGLNN3zs-lSIQ8m3ZIiVpjNgCbtPPbn_l63BvAXPzoxLVpc3oTiKzIc25k533e14zI4g4prgIj4sEsUHiKpU37X9JGvNd_SrnlddK74G6GFW9BdEgzN1UuRkQmhtA_L8epz4uHNxDdIstziHuPuwtim-2XNm1_QR5PAgs2XKiFFa9-Siwjwskaw99s_CJH6QQUepBByEFHp_-SR39KJ2rRiz20yiD2gqsPqvuyMX_KcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=c2BBFhIqgLC9z93o3aVZmkNBddVxoYz3L_bIq4ma6B6131iC9CoEjvlZYckjix8SzlZQYCj-bDdMSmAQHk9MmGDQ4VycWZdAS5i68NgmHOTF27uWa9tmxMmsIbIBjkOeYBjV90FSiga5XBpPRID5IS50AOXRQGdleMewQzQrVwlpEXUzt127yMpWzsaA9Em8NZKPKZ3E9FoKk0NLi5lrPZvMlRiE36PrfK5kaHkXXqoN2yJ7bXT9pJMoSwksO95g3URVRA1KYnAAXmn-Ok4WGrLvjmKZOotmbE3aUk9wYpovH2OUxUZBCnWtrQRNaXI5Gthg8QZRNzlKZRulaV3uvKjmay8GSbtOnCNxhpvbibDac6dOymN6YcKAJwtkXgcRb7kSBf8BNmwd2K-73oA25V_8nTznmuujwaBm-5lGf9NSH7UFiJc5A9MmauHCK5PGGLNN3zs-lSIQ8m3ZIiVpjNgCbtPPbn_l63BvAXPzoxLVpc3oTiKzIc25k533e14zI4g4prgIj4sEsUHiKpU37X9JGvNd_SrnlddK74G6GFW9BdEgzN1UuRkQmhtA_L8epz4uHNxDdIstziHuPuwtim-2XNm1_QR5PAgs2XKiFFa9-Siwjwskaw99s_CJH6QQUepBByEFHp_-SR39KJ2rRiz20yiD2gqsPqvuyMX_KcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛
به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29183" target="_blank">📅 17:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29182">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=oIDCQqEgQSg85MDGifyRgoMXlhUa0IIWu7QqIkw6sqBoJfD138Lds_zpCPHrwDP3oDSyy2_mJefJLPUO6zQ6llVXhkj28m9u6sx1qaKJsLJw_C-s4T9wjuAYQyaUTKa17YkWHtFLxFM87T6vfkGYFcsSTvpZWToaDYRx9sH6y06yv8jSgb5FWEP7pARisZ_4bOOBM2o3AqISzIxD9Z6YB-FxMBtgZbBa4qH64nfvkRCxZHXXSklJ1f-fLfjrYvllfMl93fcRc0-TUqusXlI8Bj0V8XtMLiyniwf3bOrayU5_GVaK5QEPEGpbMk-Mst96I2UJwltTkALwtVE_dNkTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=oIDCQqEgQSg85MDGifyRgoMXlhUa0IIWu7QqIkw6sqBoJfD138Lds_zpCPHrwDP3oDSyy2_mJefJLPUO6zQ6llVXhkj28m9u6sx1qaKJsLJw_C-s4T9wjuAYQyaUTKa17YkWHtFLxFM87T6vfkGYFcsSTvpZWToaDYRx9sH6y06yv8jSgb5FWEP7pARisZ_4bOOBM2o3AqISzIxD9Z6YB-FxMBtgZbBa4qH64nfvkRCxZHXXSklJ1f-fLfjrYvllfMl93fcRc0-TUqusXlI8Bj0V8XtMLiyniwf3bOrayU5_GVaK5QEPEGpbMk-Mst96I2UJwltTkALwtVE_dNkTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عمرمفیدقطعات‌مهم خودرو؛ این پست رو ذخیره کنید و برای دوستانتون هم بفرستید بکارشون میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/29182" target="_blank">📅 16:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29181">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIxuUe6alT2HewDWgjIGtKXurcmBqg1ndTf7LySTQU4KxUNT0IHBnxqp0aBMCCI8jaiIdldTABFwjRFLpY0NQ5x70xdzH1nObjUH-ruCb1185Yb_S22mKMTKZUhKgXkwPtVSxVH5GzMkBJVD1I0aRyIRLP46-sSS1Jk0kIAyunQMd1ACexB_BF-IhjAlUn2oNrqy7gRmE3irJWoUHCiLrl-jCrk2gVOuUuoSHUvO_zr9YvVhijVPA84wP0P8zX1RMkYv1HB6VS96htkImiMOAXs8-Kf-0q9vS8Ef7f2hQ_P-wrdOFNTM8__OsyqriVta15ow8JpfDKqLO5g2CGRMNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/29181" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnYw9couK6ZUmAFnvWPPXs2bXjbG0SwtxqTxjQNMeGLZl5UnGVCX6Cz4XdDY47CvYqheMS3ZdbdDZBcKJsG-MsXTekMFCRj7ndyHAj5AiQMSmKC8Iy7zQKoJpkw5Wijql04VpOsfKNW6jzGg76V2N1QqApCl0XzLrKMOl1ONDRdeqosckK2DiQ81sCb9Fy6zUIpsKuyrSdhJ18RbvCfDza5slhZN4qe9nFWQKpLBW_lwl1vsTh8VEYh9WLyNtE8SyxNYeuyS_U6wquj7HSCBnN_JQyr1bEKbtOAaAtF4uLLNPp3d41Pnu28c05So4YcJ0Ghp5pRlskJMQwYlDBKF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InXIDMMVkdIVv4CJt55UvfsgxsXt_KPaNH7QVYLTjkU9UtpyPDFLloS5ahvysWMZQg-0R8_XFkYg82z-FeZvjMHdEwT75BfhpmwdYWCmrDobSRTLkSuvgH6Pnr0s4wbTmaW2fDE6MSxWqOVWQaJjZPDKuXu2mfkJF2t1Z0PcmomhWyXBTIrivfxmg8mFyWr62zxCKvS-fcEj5usrcaYi2Wv9nhItXtsCxP5Z_crSprCHHz97bHkw2Du0RClFSCE1PU5poSetLt4br69bgpuKQORk2OTXnEVK5uCAlW-AWlMWWC0O2WGlz9ROCI_cN8MNLGnfHhtyV7xb2wYZkyQIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29178">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=h8K7dZi6dgVTpFpLFcMnfLDnuwhlifaEjFXQ_DWmY4JzuIX1DjnXjzd2QPfQvT3FR4eSN1sbZIaUXk1L5e_PXjWKZjIlHR375LAHg6D_INsY2_niwQVEw8u61lFhMypC9lQ9KLzzgzG9ayBsWjlsI5EzLqkvx5Ry1czwGd-XkGjLlJ1XuE07mULLzRIB7YPMOWsBh-7c337SjXi8vB3B5fD94yncCIJZx4GbLAH3rgN6HD170b7kMyQ7ZRvh_LTtVFGJfWMBV0ZsGtBlzdgrki1d3KFkNTXGhwStPbiIfeOGsJa3UCahXWxIqwpwOYy8pmbzUbLP0PNKv9re92LP-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=h8K7dZi6dgVTpFpLFcMnfLDnuwhlifaEjFXQ_DWmY4JzuIX1DjnXjzd2QPfQvT3FR4eSN1sbZIaUXk1L5e_PXjWKZjIlHR375LAHg6D_INsY2_niwQVEw8u61lFhMypC9lQ9KLzzgzG9ayBsWjlsI5EzLqkvx5Ry1czwGd-XkGjLlJ1XuE07mULLzRIB7YPMOWsBh-7c337SjXi8vB3B5fD94yncCIJZx4GbLAH3rgN6HD170b7kMyQ7ZRvh_LTtVFGJfWMBV0ZsGtBlzdgrki1d3KFkNTXGhwStPbiIfeOGsJa3UCahXWxIqwpwOYy8pmbzUbLP0PNKv9re92LP-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29178" target="_blank">📅 15:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29177">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=vlZ5fKv0aa_e-aP6r6reYIFEia-teRuRasxxNkSc2ZtYbnFr_BJpv5DQnEXqAdHrch6xXqE7lUTZdPepOJIV4h0QbOg8M6J2y2fefeksPPaPhrZhHYNf0-WFgFgxtBCOu4ZBksINN2Kx83AUt4Q7dvw2qyEQ5khM8vcSSLMDojNK13gtowjAANQQT3hmdtvw7JssKhjS8zRZQQ8SnSV-LT0C1wng436KdcoNSMo2tmqaGcbvZHpa8aOX-zRVnSpuVyjYdnVKVsfUR3IkUvbRY6wc2Ah10jQCaRYJCR0_hsHxIRzwFyzujKu9i0OroNitCYl34nVGcRThISFC2-wjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=vlZ5fKv0aa_e-aP6r6reYIFEia-teRuRasxxNkSc2ZtYbnFr_BJpv5DQnEXqAdHrch6xXqE7lUTZdPepOJIV4h0QbOg8M6J2y2fefeksPPaPhrZhHYNf0-WFgFgxtBCOu4ZBksINN2Kx83AUt4Q7dvw2qyEQ5khM8vcSSLMDojNK13gtowjAANQQT3hmdtvw7JssKhjS8zRZQQ8SnSV-LT0C1wng436KdcoNSMo2tmqaGcbvZHpa8aOX-zRVnSpuVyjYdnVKVsfUR3IkUvbRY6wc2Ah10jQCaRYJCR0_hsHxIRzwFyzujKu9i0OroNitCYl34nVGcRThISFC2-wjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزی‌روزگاری‌ادن‌هازارد فوق‌ستاره‌تیم‌ملی بلژیک و باشگاه چلسی درمستطیل‌سبز؛ کاش هیچوقت اون انتقال انجام نمیشد. هم رئالی‌ها پولشون رو به چوخ دادند هم ادن هازارد اون بازیکن سابق دیگه نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29177" target="_blank">📅 15:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29176">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfWhakMKuCqDtwecvfm3CgVyBdxP61pRLui4ZohQv3IBD7OJflzutil8_HycSGQiG8Ia3YCbMnKVyoJlijx2cRdBpB7L2basIGek_uZVtivZne_6FwZp0iBal9K54OqeAWCa7XhCjcaCwsw4xL-FiJd8CYFKE9KPOiMeUsBx1-OXVA5txvb-PKGK8Ul4MTjoSKf0fxiKbiIxRuAtitJaa4lxF5OCb1hq5_mKWvKmOcsJhTfvBLr8XZyHU955o5CHKj2qaH35GFlElnl_IhBPufX3LJ81OtqVUuatoxD5-Rzjjz-sIHqXYJ1LDOhsutPEMMQ1hb-RGw9OID9ly3Rw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛
ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29176" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29175">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=qS9bm8SArmfCGoIWF8Enous7-lpt9JWfwZOWaSK6jW6zazk7wmo2cwAFGI-zUoUdHZ9__Y8ADCLcWrif1GmVCdNBu6oTVW0fj3CS3hsWu03Z7qzVU-Hq8jBiUn4WHr-FP7d1T_mWQANlp08u6o4olrAvnJsqxeKSGSVTiE3hIk9GHl_qctli6mLIFPHdIUWTEuPG66p15vWVa-TH6Au_Q38FxhuNhi7Pf0CvBoZmn4ClXA6X4Rjnf8R14XeLPxKHsaGO1nPyLooPcf-vQjicFNj03JyyvGXOZLlhleL62ERF4Ffl4-4C7-5mGbhPgv_fqqE0Wm910aYOuz3wAVP18A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=qS9bm8SArmfCGoIWF8Enous7-lpt9JWfwZOWaSK6jW6zazk7wmo2cwAFGI-zUoUdHZ9__Y8ADCLcWrif1GmVCdNBu6oTVW0fj3CS3hsWu03Z7qzVU-Hq8jBiUn4WHr-FP7d1T_mWQANlp08u6o4olrAvnJsqxeKSGSVTiE3hIk9GHl_qctli6mLIFPHdIUWTEuPG66p15vWVa-TH6Au_Q38FxhuNhi7Pf0CvBoZmn4ClXA6X4Rjnf8R14XeLPxKHsaGO1nPyLooPcf-vQjicFNj03JyyvGXOZLlhleL62ERF4Ffl4-4C7-5mGbhPgv_fqqE0Wm910aYOuz3wAVP18A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
صحبت‌های‌جالب ارلینگ هالند درپایان دیدار روزگذشته‌مقابل‌کاونتری درباره کوتاه کردن موهاش‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29175" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29174">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDsphwxQgjIyrVnvS_r77PjBmZfRZxKcg3BRwEc9jQL6b0qz6d0yfgpFwN6hUr5cjs6haP6NZVqwm6G30idWAIM2-QF7Loj1Q5qxlX1zSxP_jAPNUwZlLaVCDMC2IZtBY03d13htuUCC5Q83nJV0wh8bHelUwvRLC1KcrEmZO79WyO_jhGDhFCqnXWxaB9uYAJT5qSVDrJ5Ue83PZAAWGta-PLJIafjq9SRr3Tpnc9cdZgmnduqWc0JIN4Bc1vdp1XRJQLzXkbuSLOZ4ujhyFazNOmwl4_PEd-PuNQio2vRLPr_FP2P_vLQrscv6fP38Q449cwMKRq0Kw5E8yXaUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🟢
آلومینیوم
🆚
استقلال
🔵
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/29174" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29172">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=BWFuCAdJr9YpPgJmqt37Lgszl-LEf0aSmgregjtu892uv3KxibQboEq0GjbtyaH7DZbGgqPpw2oRawt3L-DkMpCPbJt54FkFs31ncaV6eTnzURuo7X0T9TRGEthGUZqsNov0k5aVkE3nev4-wt6hBMM6T72Lr1Y9Bcfc-a_s67cDzM8Mf2DpMWxd8rx3u1nt92raKAo_9FMAxdJiQuLCrMO-T1c19uam2FS-WXBGZIMncPq8HTRQ_7Dyx2FsYk-7w1BScGFGAIddbOzBjfXYnOlAwokTE3s6tm3eIVA718OK6wuSFrhR0k189BqFtGwFU0ybdSnVMXwuXbvmsieJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=BWFuCAdJr9YpPgJmqt37Lgszl-LEf0aSmgregjtu892uv3KxibQboEq0GjbtyaH7DZbGgqPpw2oRawt3L-DkMpCPbJt54FkFs31ncaV6eTnzURuo7X0T9TRGEthGUZqsNov0k5aVkE3nev4-wt6hBMM6T72Lr1Y9Bcfc-a_s67cDzM8Mf2DpMWxd8rx3u1nt92raKAo_9FMAxdJiQuLCrMO-T1c19uam2FS-WXBGZIMncPq8HTRQ_7Dyx2FsYk-7w1BScGFGAIddbOzBjfXYnOlAwokTE3s6tm3eIVA718OK6wuSFrhR0k189BqFtGwFU0ybdSnVMXwuXbvmsieJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
گل‌های‌دیدار جذاب و دیدنی امشب دو تیم اینتر میلان
🆚
ناپولی درهفته‌سوم سری‌آ؛ برد جنون آمیز افعی‌ها در جوزپه‌مه آتزا در دقیقه نود مسابقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29172" target="_blank">📅 14:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29171">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpLOoUmW4qzeMEm37E5RH_unTzqT_sUY1Fb0bCEDhaU776U0QXa2L_NyoSf9Jnhyjk5L129rzo1ojtJ4b2K1EcieMPOr5zp0KpZdJ-Ap9TyhRHcCuNwjBidAh67gKetoWk6FpQin1-5Wzx1TnaHgbGmEEAQpgW7nVsiglOFg1XZ8Wp9hmi9_M0VW5PEU2893LCsULWJ1I6wMyuvCDygdJj1iCEuVw-BVFhGVxlgkMlEg_Ju7wz8KhPyP17qcwbsJ1p76BeBXkRJAXwsOo34hS2uA-FDTHFiuQG_t6IWXao-uJzekVZ_eNoxlF5tgN3EiAXBs4IwcSuJKPMFD938E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29171" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29170">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHcHqIDuF0Pxrl_k6JEhnliFI6O7rK2Js5jbJizqaFKTyICDlKuLDejOiB-OJ0UnqSagwFk2KjPtjIi_Te-Znr_kYIlGC4ZlJaRhEkOFPqVxzdGigOlSItxii-G_DPvy3Db3GWa4XmRXhw4q9U3B3sMV_uCyCwQySDdTUszXXjS4Cr2FHyY1mbTqH_q9Up919z-11a4dvThu3qERmuH5tvwJn3xEHd-x2ZFWA7aVgp-nbgCrD4bfmifGOHdxkjNbTin7Fm5yaZW-RB3g_GZZEb5iaOcl5gAHnJdYjUlQXJoNA2iS4FFQGqmD-eaBDlSpdZos61FBCZZ3ub92XeHMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29170" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29169">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9i6tv3xNpqU69tSlY5WJEvmZujXudh3wG_5_rL7yTORCDBphcPrhrjaXBHeTfz5lOXnKa6-IJv3wjyAz0sn9SvE4IT0nxpk9VVlvbvFP_jS8toS-ca-MkKsyLp79kUQoP1J1wqX-OT3EmPctk9FXzaNs7r5NcvK6e0rsDpF__CJr8zy-e4D9VIrr0oRmfaH1MfTrueF7G-FJqgLFz0H_SWlFLxncA_j0nX98NGGAJfMyYjwP3kHbGxFWOukNonSiHd45VLdG8MqqIlaxVJneUfJdEeNoJZTj4WKe1la7JBwMRmuYRN49uwU3BffLMnbniFJhUeEClVRrfO_tDVEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29169" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29168">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBpTj1of4Y7PapR7NOrkYvjmJMQ0YFIIcXeLxlO5d44yhwW3ZudQHIzzDKDvjGm7D60VWMw7BQloAl18KTsXRmW9jCEgz71QOA3a2yF5rVNpiRgmUgygB-kr9joTEucVNZzv_WHcEZfjApNIdXa8xtUkHiSTxxXahWb6DgYIBr9WT4GwJfDf9S_s4OmkPWbvoMb2UK0KrMKlMH09hMNQUkP2J0bUOPd7T8Kf-NW-41YZKZXOS6su_egbEApaHBgHlxJHzdpn6qpO4WI6VRPNe1rDCDMGmfX6E9WpJhDKSBKj3hGdnCkAEXaDAXENuL61bjugt539xqg2e-AT3Jm5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29168" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29166">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSLnpefxGuiq_mo5Lz0ypZ1r1XtbYL_6QBJBz_0qZDZsytZIeNg0zl-4J49u3fPQfNDnwGNi8sNcXzp2HTSmFLHBTkNbzsPIAXfqCDXO_2xIhnAFLz1tl2NTgtE--ajIBdAJRuSnTdZsUXQM9sLFfEW7gRxMk4kF9EqgBlaRQVYAo1EE7I9y8ibTI88sTc-k1jF7JMVXLHaRolFt4cmmfn8Th5Ayo4t2dviX2auHSCzhqmnnBQa3_trhbx96xazgB3p6ve0qmxZsSRS8EuOsQ9G4W3v9t13gM8N3yQxFl5qHfqORo8ze_kBbVuzyUL9mOTdbEU7aUpsKZ4z50Sp3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29166" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQGSh6JyEpXqnB05IDpW6jaIAkg-19IvHwMJ51XUNgqxcnpWKRX3Y4G2yqSDBaHSC7ce9NpAK3Y01s76hqwQQBBXP35UQG1Uy84fftZ6SNLz_NrLokDOGyC06ctSVMyxRpzuMJKdBazTDUPEfqER6VFvEsMp6--UIiTLVHbDv8tFobofAG_kLaoVDtJFdPevwMVNFvz18S0XYfIdaj9hUMhiLOVSVdJ_Rjwlxy1FpGfP--yAqQ7X6a5J9uOvAXbr7A4xIXQbVYon69R9lv-QWyNfggRPvIA5B2sf4P5I7zvAQqRPhACBOJYkEZhbnANNKHq0JKQ6lYkNKvWJ1jCNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYTS-trzNgmpJGZduooqZI0l0JNZa0_Q3MkYdqZRUZBi9cflu7RfCguzwF6B4a4b8U4DB3fKfcpfheb-Jk5TC_3GweVMsTwrEe6CSdoXtu6pbMaDiYi5VPbI-8kjGTLJbVEFhVSWxx2x8R2bs_nLsTfJSy8aquxoii8fcVJZBq4ivSaaoqtFUboJHzxB0WPh6YX2JuLpKAhLmlfEDBc_G3Z2PgKHb87OgkKdY8gxfWnnpdvTBLxBvBN4Ae4XDZcIl4D05AFshqfTvYw2fA2fKIccPf7wQE493fDpvKGSquyUcRzGqUO2DRxh7IhRjRVc_ZwDu_Y6TkjHgijcqZ5Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBJr2PKSzj4T2iY7bscNFHw7DqlTYzi8fD783Gho7PAIg5MHotohmr_HrFPmxCBsAmvLFBhNqKQX9_lo6MVrQx5VzOqHtlhQn0ePCkcSk1uQhXqLu-YMFczx94Rqxyo61G7FzwodE8Fg1IfocZUJKAvM3RyeydxK__4FbjjqzEHwHL429xEv2NLBPENrnZEIbPcub_pjadVtw4Fm1Z-OY1XrnIF9nAr1Q3AF3CPKt_mA9A6kjKpGmQ01dx6UxP-12x9YHvIhc9bk0Qww29MnVjFou66A2zqyLdIDP_g2VS7yUrQVV-nXPuYQV6QRN1E9T4cCTQhlZZzDmPF_6dIYvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBLtNctKhUyaE-NiIfNq0pkCc_Xo5YUHzzQ3h9lUhQ-2Y0VvR9XhGWMGaLHh1orBhSKYLZmFexFeUPRjgG1Dh93oHpwQLt3JCau-WBndi3oqxndl_GMG_CnzlrrG_xdf2xLxLCM2bUrwPx4kOvlTSlwo__cDYPEDmcOr67aG5KWdbsPYbNJL2cOPel2_VKqDkSk1b-o4HnfcdDfOMVoabmsOoSAkPbLZAY3A8GMsIQfUtQFwyMtlTbpz0S68grzkvdnilIFdimvQyT6ek277IhJxxARxT-JFxiS95Ccv_IeRZk5-CRE2D3aez3d0fOB6anNYNmHZHcG7-RB7RkYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29160">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhWYV3_hm1FC2kkbAoCcMoc3O6cEnN11gBeFUocwbWykzWAm819aA71XLcSmQ8FR9r6254p6uVFU9IbMhBRTpEJ3p0i22Cu_9O-HqT_UIzCDQPMHwbgk2Cz1XgAD3IuuzSci9ODF8bat5lo5ewNZ5RYe_fieEeE5r9ezDh0c5gf3HMQNImhSo7qFA029ogfpYHfsR33Mu9F5OGtfkyWo_8ZXxVaQ3etJ4JAJaq8DIn1tvmqcee-KZci-J8xxQHKz034VyUnJPXjd3iIZAeEgomycduAZAcgpXXlhodTRxZXURCLicT_ZwXc-aUFTz8yaE_rBuDtE4g8Gontn6D1XOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29160" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=REW8z8KJXO18H-eB9jRfyQ9jrPMj0IFCVQZjxMApK0R0YJ6GdKC3TT_75dl4-jojiA8K6Vizqge1GtDs2N8IjJ-lfujBtYrvBzwf1Ox0l6d48OOUdWZZiVvYRvmMrKAPXIsVhTHgyvPoXsp0QhJoDP_uFd6j9g07EVmL5w-XWpL5LtoM7mrJ5_CjX27KLsVo10usw4f3Uu246SMute0U2sRaKWR4lwdHsqADPAG9FfH9CZP_ELgGjni3am5Bavy3c3yDy0sp0Kgc8YY9ec2go-7I24vdwUjnLGYYAeTheRtQHsjDiMcA-umfWpKjSHi_HStDulWf1tU4zniAhv86bZqeuqGLC7bTiOJcr8lUVc64bm5eIh0qnMXd9GQNKoC0njbDOiRUUVCj1o3dEFrg9PaYfba_bffkDIDgJNIp2BWgFPtbD142AbkzOKgmjAiYjfJReOtQ9_fI1Kf5AfSWMJKNQF7hi5x5oyOx7_SZ4Z5XazG0pJUE1qVyKSuHxxf-MmOlmxUFP3GxMeIGD2pp4eq_A9J0MhO7zlBhYDr63157ppka6zRDHJR81MfMs63ekArjMzmO5Jhjjv881BoUJl4IqkoAVC8Qdw0v_00BcaXnISUJG7x5L1umuQ1iduYmQh6RD4-SGRlssPs6Ej3GfmE9tefPFQu0RCJkVXW3gwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=REW8z8KJXO18H-eB9jRfyQ9jrPMj0IFCVQZjxMApK0R0YJ6GdKC3TT_75dl4-jojiA8K6Vizqge1GtDs2N8IjJ-lfujBtYrvBzwf1Ox0l6d48OOUdWZZiVvYRvmMrKAPXIsVhTHgyvPoXsp0QhJoDP_uFd6j9g07EVmL5w-XWpL5LtoM7mrJ5_CjX27KLsVo10usw4f3Uu246SMute0U2sRaKWR4lwdHsqADPAG9FfH9CZP_ELgGjni3am5Bavy3c3yDy0sp0Kgc8YY9ec2go-7I24vdwUjnLGYYAeTheRtQHsjDiMcA-umfWpKjSHi_HStDulWf1tU4zniAhv86bZqeuqGLC7bTiOJcr8lUVc64bm5eIh0qnMXd9GQNKoC0njbDOiRUUVCj1o3dEFrg9PaYfba_bffkDIDgJNIp2BWgFPtbD142AbkzOKgmjAiYjfJReOtQ9_fI1Kf5AfSWMJKNQF7hi5x5oyOx7_SZ4Z5XazG0pJUE1qVyKSuHxxf-MmOlmxUFP3GxMeIGD2pp4eq_A9J0MhO7zlBhYDr63157ppka6zRDHJR81MfMs63ekArjMzmO5Jhjjv881BoUJl4IqkoAVC8Qdw0v_00BcaXnISUJG7x5L1umuQ1iduYmQh6RD4-SGRlssPs6Ej3GfmE9tefPFQu0RCJkVXW3gwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrH-hF9DpQdGVXJbtObnSJxj7gE2HHjKO7JuZnl6DB3paI1bduUvUMzD7RqmqKZn6eH_bmm69rP8ihRY7T50BRUZDRBGfLHduFDfvWIfpk5jbC9TRC1y_ZLlujq_2sTSQeB9DnTD0EhScwJIiUZGTkd3Yz6LKvIQ8AZt1TrM1NSViEgMSDjBNQpukIGUFTu9yK6PlheXsVAOiKcuCwlzIWdbSAandPx127djoR5DvkTrnKP5BwPOn2udLDENIHyVxlb5ueVfG8i25HVGckyMy3c6j9iNZDwQ5f3F_ED4YUFz_1FC69bZutVZYXc8qfcO2tzGFO4dw2lPPXvezhajcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiagZxNO8OEvVxIcfPsN7u1P4Qe2IKCy_zzp0swYQsG6NaL9pCC60hFb3vhM6J2h4MRBT-hgo8vBz-0X4APeLaSR7wof5ga-JiiAr4ug5dmNzMncdRMxU3MuPcQYwPfzR4DqwU-vTOylvZI6h8VIOVE6JUPjbJb9z3MLc6Fc950nZiKJOyH4XbNJza35UzbvgyryUDdcTrYO0OTgLPnOKzxEEBlo52VGV-0RIrDufh4LyjWyEGeqsjQrEkUTfbQvNQT3ypsq7aMdGwbUCn8TleeN4lC7jlDQOI8gI0mBhYKZkVtCcQpxUd4VggPSRQfjcQm4ppzDLcG7KeYShS4sdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2LHAXqVkC2ZgCJyDi-oFG19nbY_hGJIo3GRQuNhMJm7rBjTbtaOVaiHknEndJMaZsZvn68mfFDnqbTj-u7p_J5z9VB9c-v_TiCbmfHfGidSiLMF-JJkQx8m0Gd65LZuXkGmkMvp1R8h6hRBD7_GyajapBnJjitFdrze5Bd3Vavk_D5B83xGUxpzPpIoUFW0bUpTWa1jwPrUw1LC-zKshsBzvezkHe_Dz-6wayRWgImotyqoCZ5zY7e-W-EMHy82NX5PVxLgHqpvm_KCXc2apEy8Fz-ZGFVkiF0wZD-CU0minMPoL4-cOJue37fcmgKYaM7vQsf29pPOBCDhYGyNXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=rrQ5fjs_v1Csc657MI7FaKolcbD9pEIvzpd_JFqq0nOX1z7lV_ctKGOwIoU1uNHKH2q-aapH_J0OunA-jSqOekXfT1mYmDU3r2Y0NH-9XEziuPhYlkWaQGUTY9jmrA46LEH-0_-O7369P96eQ8_3kh2Yaz9BA1AnwM8VjB81KecXWrF6yXN0SutEqONNPnKUEIaSUCiX9PNH8cFYrLxkIoCAtjjln1FpolawdQNS1jefWnvm9q62cZ4vVXa4bYY_IsAB6cGNCt96DKyhqvur0HgXMH8QW_D3dj-4ycQUC63u3qdZ-DrBUUsky9gM9hG5IfCsNctr3GB_CXtT619BSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=rrQ5fjs_v1Csc657MI7FaKolcbD9pEIvzpd_JFqq0nOX1z7lV_ctKGOwIoU1uNHKH2q-aapH_J0OunA-jSqOekXfT1mYmDU3r2Y0NH-9XEziuPhYlkWaQGUTY9jmrA46LEH-0_-O7369P96eQ8_3kh2Yaz9BA1AnwM8VjB81KecXWrF6yXN0SutEqONNPnKUEIaSUCiX9PNH8cFYrLxkIoCAtjjln1FpolawdQNS1jefWnvm9q62cZ4vVXa4bYY_IsAB6cGNCt96DKyhqvur0HgXMH8QW_D3dj-4ycQUC63u3qdZ-DrBUUsky9gM9hG5IfCsNctr3GB_CXtT619BSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHxYDhrY7FrFo4EfMTfyS2hj44fZmJsDwDhTOzrlh3jeagBsrTChBMCpCd74gmSEuceG7ciLWvOTcYRZrAvvradKVUeQ5k6HyQ_FhboeOwJkD11X8aE6rU7C4I9dJ3nwgMlGyDLa3Ve6_d1e8lMMYQudsgDqCPigYeZywE_Xi9e2_ZqQTx3gJ-Z9ZqMxX-mxwmduyNG-q7vc80AVR5cZJCvsxXd1ZpsWQboivzsEIiba_ki0tRKfa6GfmhJ3V4d9QoO03XsNYuQaIO-w89f1-FXOdSyfCNmcddMM8Gb6sfixSiKAreAEKPvowMgTu-SZODHtcRDRyNDsn2bgz9DV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw417ufcElzJXXhozYVg5qFVnFLA668ZjozFSO7ctqHsstbm8UlPyj7oa15Ud7Jw95PQ1AjifqIQZnyqa3x0w-IXNdWXCvsdYqcsbwY11C3s5UqM3Fhx5sFtD5Gizhn7jWBU7S38Lip5rLHoka03YnF0aNwW2DqDbHLw78xDSf1ltrXJT5UFRHPOyz7_XMjdKmd8NPnTA-qlTznZT37qC1y4lKQ_rD-feH47DfWeNPESCmxvgz1YTixhipLFDtzf7elAOpAXFydBtTskkTg9v7eZhQ0UyAI8STKchbFx_Szv_OcpOMVaQNqe0Aj_DiVcuey3QAo-UX2nnvoucYyXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHc3p_sNQ-D3uQpGfL2nzHv4JsAsy2tZN5rW_zrglyvwZ6w79u5P71e3AnrSTvgB8DutwWLT27Q5N3lWfNGznlS1hmIGUIe6t31plGrzKRIoLsBsnyHCqLsgcm2Z9KZg0G3_kmdbOaeTDUAmcv5QgibjbTJeA7FI2-iNtKVajMnzPYsCrcTxXaeUmSozDQeFPGcsJ-HiqfQ5zcniMHwrUWDFnCfve2pxi1nC8oIRjaIEIHdIBjmrZbh_4RPa6QrTBXTuhfIq7Xs7LmxLou1gYBiakEBThT-GznXWAlzNp_BZ2t714k3m7a8FPBzp4BwBJHMLPg3LHRtI7Zr6Ef8fVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pB4irU_jGL0rLUYvx-L9psF2U-3cRYrSCj-Bgssc7SH2_olPQnefy9A_R7by9FtS7SQVffS8iWWzaxiOMvHsr_OO5d1PqFmvHj_FBi-k4uG_61KUd9q05WaN3zRa0fdMGr6FXHFOrbryD7Lo_W2D8Z92XaZSGu8JfyWwQaTJXHqP8d99eGBQxz3o6DFNvWaYgpN-AH0LIUQBZFDlpL7JZ2SFv1MF597H5unNDBn7cSMBTt-8WE42JDIoFWxCspeFYK5iiN_6XgdPATW3LxuTj5k45jf2DzVl0c9F5s0i-D8umopVeH9q6-mDdXQXoT4ddnePTXRWfejYlbJPFRcAyr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pB4irU_jGL0rLUYvx-L9psF2U-3cRYrSCj-Bgssc7SH2_olPQnefy9A_R7by9FtS7SQVffS8iWWzaxiOMvHsr_OO5d1PqFmvHj_FBi-k4uG_61KUd9q05WaN3zRa0fdMGr6FXHFOrbryD7Lo_W2D8Z92XaZSGu8JfyWwQaTJXHqP8d99eGBQxz3o6DFNvWaYgpN-AH0LIUQBZFDlpL7JZ2SFv1MF597H5unNDBn7cSMBTt-8WE42JDIoFWxCspeFYK5iiN_6XgdPATW3LxuTj5k45jf2DzVl0c9F5s0i-D8umopVeH9q6-mDdXQXoT4ddnePTXRWfejYlbJPFRcAyr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsKfE9Cm9G_mCYAL0W8rVAY8ZFGzM0F1lgMP7vEq1tfJ2oZcbEx_2eGD0u4GOzEuVHIF10GI1vt8_FXnFfL4D687VVJsZMDRI3QCX9g8tT4RxqgkEHxqujr2Auf6FTd-yCLH4f4Z7XvMZUjGpp1hJduJ088XMI9QPGvKXvp0_rq5X8xz5whbiMPK9h5hcAXysnPfzSonZnoA1yx2gG0cqvCt680WZr51pYuAilJqa-JbP_vXSbk77vLAckfAUeFGGqfwNlTpnkJqamvlgEMjA_7-VqdfaBlPHre9RTF_gd7-m-sdFlERbC4GXnR2Tbrh2Hw6fwQS-9SwjhhzqUohFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfQnf91wuH1GXB9wqXTIp5kH_ulQTIzw_rqb1hyEptiGhLMuyUZDf9veKSIydtIobuUeTBhDVpUNTUF-UTFJvlTB5C9Zn02J4wJfOgSkQLBYxCPfH7YGqHjr1YqAN2YId6FELgVjWlmCb78qLo4oFxcxdsiq0ywK8KpUzhQA1liG-TGnu0ZTY5ptAhbHBqoK1Ez8l1PfM5nlU0LbHxGSTzwfWjubEELIp8jNuKu8zdW0b5taXGhA9LdiUUR2tVLQvpOzQxPEhuZHk1e1iqglzdgYkN2hsZWEiVhNUmlx6a5cXm21eUhe43doir6nLZ3NuMwRHUclQzVo7R9RTLZ1cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=c6S5b0BUXyCW_7po6UOoU9ZrqKrjR7xF1PpRo9Yptzc-eesJ-MUtj6mC6ZxyS2epl63rqb_NsyyjFopW1xi2jWoLrGElNlkS_9sDQ_4fmunDi7nj8OaALQqu1HprzfP5MajzJg6kbDz6wqMSy8mFnpQKSOCwhvH13Bi7uWiwRzGXj6QYkFlT5EeA1tjZPBZnDAnAdjOuTOhrfS4cZ5lhGF_AIcSySD30gHYnCkupnfVkFJBAhYa_G6R_DKE6TnN4Fqn1tmc8CZwYVydrP1dKLSOPbYo-4DyYPlLyBzDCpsEY5CcrYaMhCfcdtY-v2_y9irgg9tK-4sIh9NpOsy2jYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=c6S5b0BUXyCW_7po6UOoU9ZrqKrjR7xF1PpRo9Yptzc-eesJ-MUtj6mC6ZxyS2epl63rqb_NsyyjFopW1xi2jWoLrGElNlkS_9sDQ_4fmunDi7nj8OaALQqu1HprzfP5MajzJg6kbDz6wqMSy8mFnpQKSOCwhvH13Bi7uWiwRzGXj6QYkFlT5EeA1tjZPBZnDAnAdjOuTOhrfS4cZ5lhGF_AIcSySD30gHYnCkupnfVkFJBAhYa_G6R_DKE6TnN4Fqn1tmc8CZwYVydrP1dKLSOPbYo-4DyYPlLyBzDCpsEY5CcrYaMhCfcdtY-v2_y9irgg9tK-4sIh9NpOsy2jYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLfQtF7nly2eTfiGqJUr4yTCDJxlVDR3-3lBl1v9F9uql8LC_Y77azYF2jLj_OodLn3294v7J-uxvmhjRP1DO2w-ZrRsX4hYptGTK6ILoLW3h5Eal44vqFZMa3r7EfFsHBKRekjBX_k87ycPEJvzb0rUoT62-0PGlwnGPdHqGtIQWz3CXjvKuCCN7xu9mKmmDi8oDuU7VVGVkRDGHZqgdx52H7PdOF6EfOD4uQ5xQ3YAINT1ioKujVCCtPP0Nj-iNyC135i_JUkIicMlKfoEypFw6N03WWjfqy2i4DOcY4mj-vnWpffXgT1Yj3RfjLSIj48blweJUqROloFDky287Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcSd7S41tggTC1n1nnFWZW7rXN7CPyps1PO-cS6T8VZW1NigjTLW8aY_7-9jrxT_Nn5lwB95n3WMLhsrwy-lLB7i72FSW9BUjCpfsqetR09bxZeP86Tf3KMsnv6PINtKR2b3I4BCdr9a01Vz3f4c3BS-4SDx6v16d1O-wPI09U3FhV735I7HB9L8QkKEVEc21y-xHHdBSluQA_nl2dSayE7562lb4QI88RVRdBJ26M3F7kz7PGZcZLtvmCcJQF_KiFFSPrsBuLwBi7TKHpl-54wrJpRpL7l7_ReWt3MmBB64uWEOuRrb37UKxHnUpj25oPbNd7IsQKjeVZ7nglDZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMjZb-ziaT_s0nvBqKAmR-9_TANAqvhX4V1KWk9Fo-riGj4poXWM6Nc0ug89thz_YVSt1pWV2CTCDceU5sOf1UjgLFoQbcNdPd0v_FP5lmUX_xUASw2DgQ_6ZFY1lrh0cT3LT9zoOi_iweEeRAUWF4gT_mRVzofxDVm7zVIqPVG6BbimPwY1xQlce6VQMsVC_4936TYOhhC5HkQLrgQhBZimsgBIg6CSIdtrOn8Z0Wr7fanCl5CY1oKbgbHIgDDlts4cboSaOracDEcDvXBZtx-BwuMk075vhoXBIvzozRGHLPRjWXetJSleQ9MTQlwB6MLxGnE8bxhG3bCgdADKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtqueINA2OZg0so3zmY1bcURykChiGaaR7PvarSPvhvMZafAaMT30H7Ivmi8zPIOoqZyYwksdzQlAgbnIbZxhF_nLyxEWiuRXZQMCzHK0qJpuBa9N382OSIlfsnkhJvyVNi-Ii-iYbo9OjxgdKAJc9yA8ze5nKMqmseDz_Vb8Vhd5w0YMhiJy2TEjcNRzwnLizE1HIoRdmZyGqGzyZJqSjlUmroEwoDzICJY4uEXlavabnEAF9KOHFaYTWGN9vXM_lhV-JSZpimt0EJObrlLvTJft-n3iP6GTVDq4OnS9BWwUhERbXCbLOGs4_iXXwU0fZBXyOxhnb2omSFmGQh12GZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtqueINA2OZg0so3zmY1bcURykChiGaaR7PvarSPvhvMZafAaMT30H7Ivmi8zPIOoqZyYwksdzQlAgbnIbZxhF_nLyxEWiuRXZQMCzHK0qJpuBa9N382OSIlfsnkhJvyVNi-Ii-iYbo9OjxgdKAJc9yA8ze5nKMqmseDz_Vb8Vhd5w0YMhiJy2TEjcNRzwnLizE1HIoRdmZyGqGzyZJqSjlUmroEwoDzICJY4uEXlavabnEAF9KOHFaYTWGN9vXM_lhV-JSZpimt0EJObrlLvTJft-n3iP6GTVDq4OnS9BWwUhERbXCbLOGs4_iXXwU0fZBXyOxhnb2omSFmGQh12GZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkpF6f19EjyUU2_AkzOhcTXCqRBJTgeHGfGa2srXyqmKwDRvXiNWxVEE-7bkCFuJ2QN946IucXWmxyuWiWhV5z-Zmd5xTNIbn58BY4lYk0UiMgzzpTNPmfcR1P_UE9UfCVUK7nLmtk2WX-pE64ix854en9qDckAKUro2bnkqYQ96rKaS_7NbHVNvsNKVratgl1JV7RsQl48TMpJuPJoegDug_ATgO1rrgH3Dm1JkSa920svRXQ_Db83hwUGMLKzczyGqbfsDHrd291AS_NXnaZH-3HHgVo7tK91RK2vEuErcWEbGdW0mcOn0bq7rMgz3YR5MPORC-Q7mH0jta3GnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFg7vcYkIGGL12r6-nrCNzNBG_N4BTkQ2CIlCcecnCX6hugvI9c5GZhDMwzo8fy69jQD_EL4qqR1EMjFLWF9iRAio5NNA-blQODSIVXHHIZIRVT1Z0anYUkj85W2Ui-acNNdkwJhHXhMOZ7GtnidV5Phkrq8fvC5n1NbsJE0S_WVZGpXDJPdF6CEl747o7m5Kdoh95EHx8moqJqqvwePr1FpGxfatT7vvxREmHajq-w-hmKGqlfesWQgakQ_wFrNA5VYkQa2ENNm55i8FLn_buJxpKEYfGPwalxzjIXKs7Y76sNoMZvIGV-8Z60vLr9SvGfmi6ZHxTdF5K7ykgxrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7T4l4vVXhKHtM76guNl5uR1wiayvUZLUsPlmxMNEoep1Z5EksMT3HHCm6L0f2CQUl3wEyimBVYnV_gRp0oRt7aLL7F6osgo4pijjAcMwaiABdbrQHuGw3_m70sK7tekGAQY0T6Mv8rQq-vh_h1XPS5oM_JqBxr5PoDvr7nAlDmdM6Gk8ocOJzDE8kqE33R1ujzY_Cwis_AHcDPaPGJPnCQoKequJ1-nGK1Z1ZSno8-DW2m1HlyE0if5zr_VQ6-tyb2oWUtCddd9UCGpOoLKJaUOozn4g8nvRjSe8qgvVmMC-20y6UZVmB747lMj2uvHgakYi423hkqXwJwuUdgMEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ts2II_5GR7SSqm8I7g8ShHh3o7EWwtuYNBfal0cZPTMFidZ5_4UIn8WALmFHOH_4FI0Hv6QaHatBjALo-WmOBUJytoTeWWDXYbNeamF65oNPa-jZA9zY5BZ5R4DL8811yKxdg2hGGdgkIcqNg57tcXLklZyWN2_d0yEnEyghNpKuP1KqXhXQ_zPEpAUeeRBKwozilNGXdmXDNm5ALKg8_Xuab67SSvbxmyMX-H27dzBYEqje7uu2HO-LlTk_i7H_xKfqAbh3YecSODJkfS2S-WqqwFaHPKin3oDQ5HwbyjtVlJUCRHZtB0DMg0LyUVyyQPUiiO3bL2nc6DFQ6NOn8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKN-K9eWOi9FP8_9U4lbay_xjdbVTsk2VqFk-dVBNFIwv9W_HG3EIpOYWwLighwZK8YMQ5RPft1KsT_MJCUAofRV0XRAs58WH45uhkO5rOS-dJhndloof2Gs7bu-s9a8S675-fVZZu29XOBQSWAilIZpWRTOxwKPIbIejwRvEGcg--sjzLiPUKWvgDC7Cass61uWFHrVuR2SlK1Kdtcz12im53PEH41ZdKEq_IPMKQpLV67k8m2tGEO2unuxukSitHRLM6Rlvij17wFFxfLAdxJQPM4GLB0BgRnJfqtIPstcAxEQfqoW2_lIjWNVaSzGrqVAONSWeg8j8rEXHEhbyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=rpk7feQoo2DgMcanMyY2oTIT4DOrMKfGn2SmhwczicndVL7_j2PWyj5U-NEWcycIc99rq4neK8ZqxBedc0uafNMe6sw55YAJTNiJkV4BYtpCR_hAKqWYa4e6tauuBoeGyxzfRT9gQf2gsMDAWBtt0_8OWsJv6a-BXfxBKWa-R5-oQLJcDlnLGvThGkvlzmQaCK5CM5btdslpv41HyMKRuQlXDlxGniIS1Mnprwm80mZXN0yn3MJedXizmCx9Lnb-VTziQfxPP7iNGIQAtzPfuh0iNVT_waod46fekwFGKKVSb369sQ9nztpKBeXkrRyhXcPa6voN99b2JTWiIhFtPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=rpk7feQoo2DgMcanMyY2oTIT4DOrMKfGn2SmhwczicndVL7_j2PWyj5U-NEWcycIc99rq4neK8ZqxBedc0uafNMe6sw55YAJTNiJkV4BYtpCR_hAKqWYa4e6tauuBoeGyxzfRT9gQf2gsMDAWBtt0_8OWsJv6a-BXfxBKWa-R5-oQLJcDlnLGvThGkvlzmQaCK5CM5btdslpv41HyMKRuQlXDlxGniIS1Mnprwm80mZXN0yn3MJedXizmCx9Lnb-VTziQfxPP7iNGIQAtzPfuh0iNVT_waod46fekwFGKKVSb369sQ9nztpKBeXkrRyhXcPa6voN99b2JTWiIhFtPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pv9cLW7Qe0lqL7bo4WOigOvtftJAAs41vOMx4VZyNjA5OSyKC7v1w5BpnmH5aZM_DrYlF7SN-mtzIbZAEJXw1FAyvm-RjoIaKwAFDDG5rfhDEX58BQ2hwkicuWVuYL1qkjKS0ZU3Xs1FZQGEVPR_aXPY5W7xjAqpA78iH1D2LPvifJsvZq8HIjkd6mvBKROx9BhBUpXZpUkEYnNjOh-waWZi1neQ7v3LlddaoaJ1ErucUz5lvhNwqGtl6Gquhs3DFQM8Kj96DSlQXIxe8_qMWKYU3ddKPwkB7mvfjSEGCDp3EEzCTBCLxG0QZl3aXctbFuwWKR3VIyhW194t1ZoK5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j49_69zdpZytq0rp7OLf5azqiE7OyHvfyJGqrwQnETyBI4iHtCCcuTHOLpPSn9vPEjxmhwZaXc7MeV2re2xRQwaIfvA_S4hlE8Uk0Ljijtmnwol14gsAvW08m8hrk7LnQUFwdiE67VNl7G7QegQ2ss0aLJfO8gIbHZIzK9kPNZkHB-eq1KTvPR0KTiFaBsHZNmjn0rUUXJfZrv1fkDZv7D05EeE5BzVuZTQazDA6p8jsrd2i6AcQzXDQh1hEnm8zvRDD-l_RghHGFeek_oTwe9OCtnXKkkKq9mNY707kRPTxHiSo6cgFThqpEDVCKRITZ4wbsFUPPcGox0Fn5qdUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=lL75T_1Bk4TWccrGIJBsDMa3hLrK8CiD4sKvqGYlYU5UBAWHdav72F4zF-Z9-Yu76DBJYgg2Z_BfjoT5O1Rb4-rX0rk_GbITV4jl9B1TeDuIuPUNRszqOJgkjAc7WzDHp5v0m-ZO-S2TJMGHeIxbFMg8-7iJEVSHnQZZBasXjhkj129SBZUGz-7cgI9qKVTonsmlDsRU7_f96FVJJLXiUo6ZC0DL2kn5A3RvGHRVHqZCvVDgAs9xvquwm4f6utvmVdIBZnQq58nTNVCaBv6V_-KexHihPchWBDnjihUSBrBXA_bOvlT2PVI-MmzXzteazj1fSgaNWE6GorQtAHCIvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=lL75T_1Bk4TWccrGIJBsDMa3hLrK8CiD4sKvqGYlYU5UBAWHdav72F4zF-Z9-Yu76DBJYgg2Z_BfjoT5O1Rb4-rX0rk_GbITV4jl9B1TeDuIuPUNRszqOJgkjAc7WzDHp5v0m-ZO-S2TJMGHeIxbFMg8-7iJEVSHnQZZBasXjhkj129SBZUGz-7cgI9qKVTonsmlDsRU7_f96FVJJLXiUo6ZC0DL2kn5A3RvGHRVHqZCvVDgAs9xvquwm4f6utvmVdIBZnQq58nTNVCaBv6V_-KexHihPchWBDnjihUSBrBXA_bOvlT2PVI-MmzXzteazj1fSgaNWE6GorQtAHCIvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpOmNMOk89AI7rG38IeQX1SpF7Y70Q8YT5cY5XlURnyCD7RQLCivWC752sXXo5Op-esHQi2cQ1wavsqAN-EHgNEZv8efBvVZUHTmwV-ncwT9g3_i_vD86-7ifso28WF_eGjkxtocNTMuCerZjzNAuSetrM7vnFT0sUvjuLBxrV_jVMW-dUDxxe1sxpX5bLqp6aXFjU_7NZjLmvVPz_k-S7kTx5FrdRqHnKWh492x63c2GkR17wRisPVpZK8CwjeNN2xTbnO3_L28GCujXqE2b2jh7H4_GMnjYa15EhzaBZkYA5AE1wU0p5cdrFYUR3SHvDUO3EeMNEL8JGQ4mAFcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZgRaIZtbw9yXU2u7IeN64LhlZq1FSSA4r7AjlifXMElTHxXrPZhMgplcoSQ81fc9gc2yU9xcGKrlWXyjjxE1URiQrhepl190OTsNJ3M6anv6gcJ__vI0zjJj54jybaxPYEV2bPHf_Nhm_86QyP1OTJBEnEKFGDIKkxqxItfDAxL68ZvJk5Dx7CB_3O-6m2VmO96EFo9PW5e7_Dc8as2qXEmTozUm8w5mrZkWs-Z_sJXefeVDl_eB_9Bf7cnSYDx81WIB_J3azHJBD8zqfz8WfJF0Kd0Om88wKc6SUo6k0Mml-c62yE64Q2QKwq7StHd7BrrLEzDvUjrUJueLYYOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGSAP7GhmiA47gSxz9VY7wxDiM1eFc6G_SVCNnZ5TuidZJTGr4uXUknYW0wR-oN1zVwgeCdQ9nhLSeYiHWLdoZvgJfA3f25mTioJNytqoH_C78pz5Y1QLYLZlKKbzkvkR8KzzK68L4ddyoM79IyAli3jhbuGyVbQw3nUva38bC3LfJn-UJ_7pM80AU7JHdVfQ4F4mM_RhZpT0W9h_EyXtWmHY9JFIHmz05iKoP1dHH3DGLBakgjetxeeS7tBFic4mexNxNP2JT1aVs4Mj9B7diEaqLepD2ff3GD85tEoQe5v9BHUpQOYGjJsgm-a0QPZEJ-y3ZhYe5B94hTFoPT8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=gEHm6PsIEJWP-gdxWPUT80ebnIFnqlWd05qw-K8K0ltO9Vj9JVq6zFZzS-BFAMNnBxpK-bP1HU5Un3Op7nAISWsQbQDL-g9oBVxlIwmEH8BgxtGIH6-U0aK8J9HxTXilulCiGEl3NeKwywyRRxBYo5eDN3jgBpNyyAavdNt9-BxTjxB4VRhhxgjPa-YwbMZeVxQuFJsdeWMPPko0N0sLYrgAdwN_8akrzicvUuvOn__7e2X0lTw2nBmGxiLL5id5UVd3ZRe0M6CwDWKibGRxhrVZsNFs84KZO4iwED1BjrSxdDKd_FlaE31Dy9NDTcr2tbXk3hzZiqKKUBfgtHAGOSeiyNnpqSWvjSfYhOgulwp8LOqju1NsIh6XotjQwKnErfvI751SGqTQ2lvvdq8qqH1rQqXI8lBAvUHWx55VR4iGlm82CFpS6u5G6xHLHVGq5-3Z0QY-zzPcTOZjHIy8o6qpAct6ZE8TQhsrKFEFtzrfYw_WccQuQyqQMO5MD60rTaNf3R94g57QMW8uTV0EMAh5-KY3DPgeUWy7pCZn9sW1UdZUwt9Zx2V2a9ya1MQ8Ouu0A1HqWnCUsjtSbMnvW_zAbFlBS55eAI0SOVSpNVLJuxiFJhJ6fqGhpcUVnkBA-0B5TnLOmGEffZ0Ek3em2QhEKZO0OiF6sdBeZn-5PjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=gEHm6PsIEJWP-gdxWPUT80ebnIFnqlWd05qw-K8K0ltO9Vj9JVq6zFZzS-BFAMNnBxpK-bP1HU5Un3Op7nAISWsQbQDL-g9oBVxlIwmEH8BgxtGIH6-U0aK8J9HxTXilulCiGEl3NeKwywyRRxBYo5eDN3jgBpNyyAavdNt9-BxTjxB4VRhhxgjPa-YwbMZeVxQuFJsdeWMPPko0N0sLYrgAdwN_8akrzicvUuvOn__7e2X0lTw2nBmGxiLL5id5UVd3ZRe0M6CwDWKibGRxhrVZsNFs84KZO4iwED1BjrSxdDKd_FlaE31Dy9NDTcr2tbXk3hzZiqKKUBfgtHAGOSeiyNnpqSWvjSfYhOgulwp8LOqju1NsIh6XotjQwKnErfvI751SGqTQ2lvvdq8qqH1rQqXI8lBAvUHWx55VR4iGlm82CFpS6u5G6xHLHVGq5-3Z0QY-zzPcTOZjHIy8o6qpAct6ZE8TQhsrKFEFtzrfYw_WccQuQyqQMO5MD60rTaNf3R94g57QMW8uTV0EMAh5-KY3DPgeUWy7pCZn9sW1UdZUwt9Zx2V2a9ya1MQ8Ouu0A1HqWnCUsjtSbMnvW_zAbFlBS55eAI0SOVSpNVLJuxiFJhJ6fqGhpcUVnkBA-0B5TnLOmGEffZ0Ek3em2QhEKZO0OiF6sdBeZn-5PjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSbFWEJ8iTwx8MUl3jHQsmNbxJZlxt9LTwOO54drE8feU45v7Tq9JKgR0Rpr3_x0TS6aq7gTTFDkeTtpioK2XzR4hiB6sXbordErtUc61BKeFr0OSaqMeOjAWMUI2IJjFZm6oxyQkP3xx3wko2MOZ0dXd4QKHPv-FL086eJzNnrgiOUR6OGkw7yr7T7pn8RQWtYSKFlaFBa74W_pP2UB4QvrgW_9AX2Ml-WMTiGza7c-j4ptJttfC_8vU15ktm1gEV0tUTyUxUgCw1rhMUSQ0z07VR45wCfMWKXSjSw5FpLv-eU9IqKrmwMi6RIhaDgV-RZ8p8UWBnq19E4FCZXX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkm49QI7ypxhi0nwT4_bcZhQrt8ZxJ49nD7CMhFuE37dokpjUjuARg2T2Rxiuskxow0d7UjlXUoEp7zelpEByXvuNSJgK1iUnozDdZW1d22w36D1cIlk3x40x0R3-z8XYnGQCXpGN7aolHZ6D3rcQR_yVC2fEzUFMIAJx7BHz4nF-w8JRVjjFG5W4pic0Bgg6wAz7Rwx507KmUlaYgYwdFzmzpg2nUAxgAbbaUiuZQUIdwDnvDYvm2HbMXB-mns0kEcU1_xKI7r-705URtgmehId6tQE6Jamn7_3qLtMAU0zhNhP022UDuKAOgewvddypXANeivY6D7Pn0CV1Z8kTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVt9aITPbg6_fv4ob3-hmCuTEwuk5eF2sCx_9MezWtH-lvn_pUSne_c_ijSbyq0M-ELjZqzZDqIEIVBd2eilGRBLn-F9MBNllbAHv3kiyFbBJRQo9PrynLKb-ozaZCaomNANxn8WeWODQjPDz1Ou8wtuu9Xw2EneMKmTFXaQKVz6r77DDuofTGzTFmf-_FkPJ1oQJpQy7C7Kw06usexyQmPmKdC_yZf1NlOETs6tjmu9PjvDRp2xRzUZT4Bsfv0ibTzOP0t1Ykjb85wZbKX4UJ3iUhmP07O24IL_1yQAwS9NG4TCPiNGl4VPI4dqMNjo9q_HEgWlj1D9EVSy7BD4tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lc3srfxZDGQU7_A1KsnptUYWEAU1xKmC0ZJeAZHt3JPqyRTtmNHq0UvyQiWpeAWTbT0FPfvQgGyavNYot9W8MfjxB1SM5spqBKnP6-xjplxUHG8rOdDyDSr95pkG38I_fwDoWhRn2VDvpJDiPEk4ptFgwa1lvE4fzQFeF2uKTJMcIXi2n9NMFh4Zm_gzR6D_Qr0QqPNNX-0D4i-nl91DY2BQWpThOE_JYBnyvDDvbOmQnAVQOwpJ513hGro5FzoBwzbyge_oAlHtKAaZgAf40Q-HWmanGepulUJBPlXcYEgqyxVdyigrO3UqbOZtGmKZ8hPI68bR-3DDZuJ-2CNz5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSdVCXdsj6RkIiJSrNbfWN6WWNXpcMFa96x3qCx8BuiV3HF1zJiudJJDN0lt6FE4-DS6z30fleWPJIvm19rjzdFCy1QXcw_PBGHBFwBCu3kfu1_27NsAL00p4h6lm5ydOiB9uCsyc3GU39h2wPGvT4VP3DD4EI9uBYycrUaSQ4tR8_d2JpmVflAhPi-dRAjz60GrREYIMwSd8pmUd_CRYLWp8ZhIXUMo6kqxGAyhqvkRVul6FNhwI6ffKBZv90HzHxASaiiDDky3qnlitHBVc9D2-_sc-_vplbns9c72pAJeOgUMF_mCUOtNNdof2UIl5dX6bWHBXrZegEQzVfGRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=cfQCzrZDtwV53Ht26WnR9rnuWfKbCmyWUbJhdxEFigMQo7rPG06kg7cSmxF-Kg4SwLK27nYHhEbiTu76UYoWMBhP1JsL07mbxjxvasRob8NLAiTF0wpYx_zlIYKIKrpIsIAdClaLiMsynT_wr06aeO8-YY4wByLpc9grlIUXyYUjo0gI4ty5dh4vxinBInFgnC1OWjtjTUP6p2vC9jh2lVO0LTYMBuJIgIAYNMKpxfs6n_aqJ5E8Y71M5HbOKcaHJXyTcXiD6wAuSftGfuS5n92Su3NPaWcOpD3dqIOSLOu0OBLFQiGHLzY2M-Q0P6ELzw-joaAb4CeWv3Hdw4frqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=cfQCzrZDtwV53Ht26WnR9rnuWfKbCmyWUbJhdxEFigMQo7rPG06kg7cSmxF-Kg4SwLK27nYHhEbiTu76UYoWMBhP1JsL07mbxjxvasRob8NLAiTF0wpYx_zlIYKIKrpIsIAdClaLiMsynT_wr06aeO8-YY4wByLpc9grlIUXyYUjo0gI4ty5dh4vxinBInFgnC1OWjtjTUP6p2vC9jh2lVO0LTYMBuJIgIAYNMKpxfs6n_aqJ5E8Y71M5HbOKcaHJXyTcXiD6wAuSftGfuS5n92Su3NPaWcOpD3dqIOSLOu0OBLFQiGHLzY2M-Q0P6ELzw-joaAb4CeWv3Hdw4frqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL41UKfdmHC5VJjXYhTI0lnDE2HX-tLB_Vbj-ca3BqyY-cQjK4YPVCzH6aNsXB8nbJMEoKn3YDmPgCe-GsyGfSrhGk3bt1Y9zw23HKkzGv3hlg873ybmxzAPWaBic2Ft_iac1G0wuV8RL12B0E-RbH-UD7iTnWqk05w1lzTN3PXW8mQE3QPXPe2U9rKGxcnBYyesyfGbKyUHmMm5jNEPxNP1VSCeg-Uu8HCNtQY6lNs0K055FfV-9Vn1dN49G-L-mgi6Ov_dY9gvB-KAY-YIwQx63VcrRm1Fr2n6GgtnlOdceQuF65i2lNno1agMN6l9s0UrTFqeavSf-ckEc-N5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyxI8zv2R9VhRHHccSy8j4vQNqaiOzHAft9FHUQ1ewtfH8eC7ob2oC_rDQG12b7pMf5tnL073iG8k72eA7U2G-sesDdX9gjBzJgekLIqHdsnOEUBwu7pI9f2g4yBej4TnkDFaJPXy6GmXUc5twMZMEpmDomqBQ_3cVGYuZiL8LTeNqgjmEW5UccVYE6TpeM8oge7Zly_LQMr33tyW-wuIQZf0c839X-yUaWWMgTKvDN1HtBzQEOXKmVLuJQimNZyt8RJuNgHirbCsc_fKwpJZOYplyYI3mJoavUwKxZKJx6CQ7GQMUM5GijS0Zstsv9BMbi3u2vwweLbWhJcypm_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=eu6zNCkIzABPKa5LcsKwedBRmjfPj92Tz44P-YXK31TUaA--3SbtpArKzfYU3vRYBBXLUfmfnLjkgnjdbA4TZLYiAKH5CbXQdEsGO-Qaeob3oyfFdTDBftOt6wawbd1W-MeIVpbdYEJMsO1UNwokFkr7oHzh-tJQSENFVaH3FeV0uYxESQZsI5VGbh2UnkSdugFu0GW_GAz3mtSqzwqCGbZwYPT8cVozSEXZmuN8rsn15rv_5SXTLo57UUApNR9DgtnM38mjBBWZ9EBtt7g_aqDWUzQXSC1I_8zo09KQi1O9jaIwdiSK-FTt864uznAcgIvK3zHnq-6kJqoisUG2JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=eu6zNCkIzABPKa5LcsKwedBRmjfPj92Tz44P-YXK31TUaA--3SbtpArKzfYU3vRYBBXLUfmfnLjkgnjdbA4TZLYiAKH5CbXQdEsGO-Qaeob3oyfFdTDBftOt6wawbd1W-MeIVpbdYEJMsO1UNwokFkr7oHzh-tJQSENFVaH3FeV0uYxESQZsI5VGbh2UnkSdugFu0GW_GAz3mtSqzwqCGbZwYPT8cVozSEXZmuN8rsn15rv_5SXTLo57UUApNR9DgtnM38mjBBWZ9EBtt7g_aqDWUzQXSC1I_8zo09KQi1O9jaIwdiSK-FTt864uznAcgIvK3zHnq-6kJqoisUG2JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXDVpFVpfs51AmjYgVtiErPClKYq2jJ9Q9hmN1HTNDPh2e8d0QBljPwqLXnzhs3ejhMvtHR5YdPAMjaVnjvx7kmZfItZgGgKl9A5TiztYd9wFLSGxc4Wm2yF_SmE8bUWGjZ6V7_b5XUY3jaQx4EhWSpXJ1qsfvh0b2qZ2kMDHGyXYxPUkbgpdJ019fzj2t26T8BuiFJ5hqRLEhfzBBU5bZmSJtrDMOASjNavxntGLo7Dy8HYbHo4Mlk9E_qjX7CeAK49yj3rjH-Zr6afSlOW4sll72F-h8BpJf4X43JJIfEswfNTISOwfe6yJRaIKBZ0o6nbVMNrOs88RqCq786tjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=AsQiCfaDPdWXQbR1QsgwG-_rGDnzABHKbLlq3A4Td1UBxLkdl99pc7Nh8DGkuh1khkNysMfH1JrSUINFw63YCHMJXszPeM-wJDvfNKjsx4WHv-sfO39AGiNzt1vBV1A-RbCatoh-HlzAeYuFKo3pZ9EnBk6LSbbzACxCvi4tjfeovsgON8JyMeLmEHCLv5J-NHid718Kem_ajPgN8FKrZYReCUIQkKK2LlHPq34c-zUoOUwNxqKdLlCNy88ySN-VGLyYROs5M7ds-wlkLOm9a69GclVfZB7Np8LelUwb1u5r88_dFaxw7dm0L5gRlByRx-v9T1w0rcLNi1NqhQvIrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=AsQiCfaDPdWXQbR1QsgwG-_rGDnzABHKbLlq3A4Td1UBxLkdl99pc7Nh8DGkuh1khkNysMfH1JrSUINFw63YCHMJXszPeM-wJDvfNKjsx4WHv-sfO39AGiNzt1vBV1A-RbCatoh-HlzAeYuFKo3pZ9EnBk6LSbbzACxCvi4tjfeovsgON8JyMeLmEHCLv5J-NHid718Kem_ajPgN8FKrZYReCUIQkKK2LlHPq34c-zUoOUwNxqKdLlCNy88ySN-VGLyYROs5M7ds-wlkLOm9a69GclVfZB7Np8LelUwb1u5r88_dFaxw7dm0L5gRlByRx-v9T1w0rcLNi1NqhQvIrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm_L_29PahpoSqscbnEZLWs9zPV1BtVWT58fRix2NwFA3vuwh25Ls-idobdU9RYL-XyXMKUR_RU-u__mkJDBsJOWPh0X0mOVapfN9kVmMWE2NF3uyRlV_QRdkCQv9YISCw5Y7RdRR_UagpmTQ1vfqvPEXysVuY3UTCsx3ipdTOtHa3-1WOHDp9D52084IVRrF2F7DKLKqMmUcYp0fixCt_KM1MGvgcAPfgJzsbcujFK4Lpu4aUvYTyGlJ_JI2wCZfXfL8hhbaKd5P1mGTCgoPs1o7lIePceHHCdKAng6AFJFzgaqm8aOkELfKGu2peB36aNlOg_ff1PpMoXFhA1FlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQYxF1Y_5S88Ph5XM9CL_vmyhrEiW_B9XNhxYU-Vs4tJy-oJJilZZxzfmneNF788mEK4qQzsA7-0rH2FMUzJVuT_anPuF9Dl7tFwWylH67Bmxi02S16oeCfelJS8dLQ14pKDZrlfn94xgMZsFN2cNV7AXZddVDnB2XJ7D9Rd-1QnPhYij0U7ona5BLA22fITn9wqFzNEQLqLAUG9ZWlA01LCZS789iZrAX9skUVGUSAG5DMHot54QbxCZDPIkodKrNe1vU8O-SvqNUNXnYLXGR0wo3B5bnuCT0GGBwYN3lasy5CLTMu_m7oVoGByR0sFitHyVSJKty12-TaqE4xoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Li0SgkJiVErBibzwZt7ycva631jYN1agsyQTsiQodvSm9Lra69wAqSLzFppP73RS9iUUsTt_VKZ8Nhg92fPJWq34-OmzCxj5fGU4IMzW5OADD8ZTrKNCfqmHLhnNMpOxHbPTCIkyOxT93x1RCiZJcbw-xOQvJKG3mZhmfMvqeHg6MW-rA176gj8cmg_kIjsaWhgC7n0IhThIrWnUamg52IczkZJxHe-u8-YzUznhv-8qdBr7kJom9kLMCSUL01yWgciX6q8-eUixiD8cb2pjuOro2LDSpRQSYq7BEV-dwnUJdF4VKSMPtZ5JW3lnXvVB9r0oltrJV55XiMUgtvJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhpv7PhjV_KdMMa5Ta3ewWOu4fid2whN5qcyKhxXTrNNu7-hhWmroDtYV9kQxgEAjfiTbQPWEs6yVzI3n_9JM2uWootbRevAS1ElWh9IxJxX9P-SgJV6Ecjsx0ZTRnVbJJjvEkgauUMykt3yU_DXYeb_CC8JzJmw7fRvRiUjlNqqym-hdLiMy03r_2Ac7vZlUXS14OCcNI-kvebgmao1ShMF1PrZosFGopCYjVBK__Z0R16a9hOdnuhE_OiDeMIVAFg5NluzZXgHKwQDCV8E7qMzufA37EYR29a1sF5G9CMYNBZpXsHudvx5hvQ1kl-cYMiKEgZBHreGyw1WGWBEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=qooNGSaYsJXqfwCVLVYsOMlIKp_Ozy5woU7OIjpaIeBemHjXP2L1heN12kCtDmGlDm5sHBWPnlu8KdpYZuDr80TkpBTU9QQE142C4bfeo6UKCMoQZHSGWrPbStdX2yujmrrSJTtc-65FMa5O2FjWBH3XnnBcsyGv60lVXG2eTiM7j5ypZHqJtQYGC2BmzofP1GLz5GLXXKEUSJ7-1WFkAMJUEPRyinJlokO4q436zpqXv2yIEoLDgOzNOPGWQeCFqq_YZTaOiz1vl9gg3mlWh69fuIxHCVUi37-vVnOZMhRriOrrJl-KeOoht5-tOG9TaMK26EleXCYiJyjJvC1LnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=qooNGSaYsJXqfwCVLVYsOMlIKp_Ozy5woU7OIjpaIeBemHjXP2L1heN12kCtDmGlDm5sHBWPnlu8KdpYZuDr80TkpBTU9QQE142C4bfeo6UKCMoQZHSGWrPbStdX2yujmrrSJTtc-65FMa5O2FjWBH3XnnBcsyGv60lVXG2eTiM7j5ypZHqJtQYGC2BmzofP1GLz5GLXXKEUSJ7-1WFkAMJUEPRyinJlokO4q436zpqXv2yIEoLDgOzNOPGWQeCFqq_YZTaOiz1vl9gg3mlWh69fuIxHCVUi37-vVnOZMhRriOrrJl-KeOoht5-tOG9TaMK26EleXCYiJyjJvC1LnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo93lxUwSFBG-8A4Qf1mavDIgYW14_tl5dNcVkshAOru4nyOPQvhE1vSgG5TjSSOcyR6UjElJUGKL8uQEWkhSOCL42EarIBvtTikwue-kqIbTd6cUfeaD235amNeLHVCJvLQTqJJ3gr5TJY4bN0SYMZYJl17MNqs505AdBmS8FrlqmklaJ_gRu1Q2Y3s9RdZK7udEGgZDAwr17hWb8onCVu8FjAoMldh2D9c46gtrpBLpUD_HgSzE5xSzkrmcQqP3yhOIXqMmbU5JBbgrblnbiYjOQDYQhc8vtclzy2P_mJhoXZ4H6D-ucU2XPpD0Vv1l6W4LRkw9iShmysYq1p1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNPB-r1Bjk04KvONNMLDDCCqxvXKVnd3_pmS2PuVRud7ca7Y45ZjVxTWfgNyo4-qb4gQAdekFlMKBAhaNwbqCD6MfLsFUcNmqVIAPRrFplY26TZ5kvSD6xezGmKrfB6mvKq1XT8Et_MCy2X29bH_TwsmosKcW3iIT-mYfePfNJpeeLT1Ls5fvxt0or11nOEHOxcpQP0NqPP3MV3wV6rSBLxmZuW7TGqVpPKrjuC229eeP4lV4RVauP0AEZwtbKYrtLmxo13hOT1C_mJRXzlfdUjLr9Y6gtyNSaWGbrYTT_S1n4M10NT2LUtoWfzb2hCfbenTMPLa9wlLuuClOfU6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaYCrVueygDhPuEy3y3Rq3b_Ef5D-WmSRjoDVLYrnPt8LZfu8tefh91z0GSfd0BKe9RfA13wx3NfSj03ftd-P3l0-9Z4WXBBm1bGQbpJvum4dpsIINE_pFXdDqlJySavLsHZia4DQFBMm3_utvHNte3aFEn4QZjlACbZSuQKWwnW3jqZHBAsA0czQdZpl-7cZcKIkO14q32oJ7eVIC3-0zK01e31yue28xTObof3xKRTySBoMyxLqcK7Uc9emRxfZ5lMuofII5_S9wlmOhUMEl6cURkCF0EtWJwN8UF_5EH7JaxYsxCkT5DWrD9ZNfoH6FiAQ70_LB2bG_drWl9yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuxEL8y0Ah4LwLk8NEJrXwAxQ0BngC01MXOxBBYZxGbgJ-nw8SYnrd8fwtAkTjDARbWabgRQIrDXeAI9Bb_8paceFZYvnLQgZlg8gXCS1H3U63iU30HWt6RnkjotM-aT6uqIu9uAbZ7VZIqcsUOmSrUCetPwhOYN-Ds6uKZHT96j-HkrdRBqjUV1L6BD9CGhgzUvqrk87Nc0SUPh8lEtJZutLYjqCBUX2-dBUTGhtfCKduFdLdlWqyENj0Hrf2tldMZxt4BmQQdhdKG-8kX3ln96juXybOFCiI4Zg9-Rdf9q5m9g13ugFxsbn9fIYZS8I3pONDd0WJbYc-LIxdHy8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
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
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNDK9D7HHQAh-8IT84FHefiHS6h-DNAXqZm3c5B_Nz7zEmn35Jo13UUx_CTfgM5tQnV7wPnt1O0ShdTV7UH90KRh3uXO0qbxhC-cg24Ta3BrwD2KPniQ8v7dcXnqBAPAmO4iAqB-xyNFXTlImPEub6ceolYTEX98V-PywluqUweHbkYok9Il0LFJVBSfHuC_hnLJ6SWxMFpMPIKOKM0QVi4XIRuKYjf4n8rOoRhYq3As8kZCUrzfv--AB6XXRX9NWfQ06mpOtZzBVLlRYDeLwSZwnKrsAtOB6rAAv8c3edvauHgj81nEhWkb0iOodi-qS47JHfhn-Z0q6OSzzRT0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiRZxOxdM9Yc3Mck87G0gnWSCuj_y2W_7ATHxVZfXVu3jaUIMUu4_MUPbUGVYdjd_ndTgTUwDfTdxyFulOm9uyvB2HXtWuKuYvtRyrW1XeBACHf27Sjirz24E-xjMDE1NdJu3IrdSvgcRcjhDbIkcFygMeT-A63i_sNPeogpfc16VOoC96d5Dbt8TVRMSIlcUyg-huj4w_4NdpsQjFNB03MVOZM1td8E0w1JT6q1v_Hx3EBqHFRUH6e-BKNVKJT9DsY9L7ig_fS0kdhd-LnL-wrzrSSGIwbXTDmMSMZuKH3FHFzAmFf0zsG_vuzOQYrwzuUFiTHGS7GHJLLTJimJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYx2ki97bDpFigFruk0D1ONTlDhc0wk03gMZ970Mu7zNWLXeD2VjxfWuq1xNu8Hsrt7b-KQbK63x3koz9iAaZnKVgc1XJc2Li8Ehbz4BjvNayRaCRi-R6mGodel1YikEdnTx1JwixAdfZMVt_827jmilAxNA9on7fKkaNGZ_JADlxR0V6B0jpYqzUeIKrocSO12zYzDh4cgpJef2FlCAToJJobx0YMmwArs6sSFrt5zGqkY7DGteaA-KRb94AGIzAUZV2kPorzIIdwtQ7oSi8eBjLnpkdKEoM2MlukGPX8nBYSUMokQV1BdaepY9mUdRqswqDQ8n1SsV10UByYXl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
