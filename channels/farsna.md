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
<img src="https://cdn4.telesco.pe/file/YkssjLsohcaiuxRnMx7DgNxDXE3FwmI9iaKr7ynqethkbPbFLRsocxJBbtBx0uldu_HPbCyiMZP45Id3C725ZHkvBSqHAi83yAxSzrirZfMI_gRJ8KVbyfUp25kp9ueTWKm13AxtQ6Yr8xVdKo-cymz_VF-lkn6wUnP9v9gfQTrCeR15CVhGiDF65LNvIlDI4IanPwEZfTF6lL1jZvF7EStjKzPuQU5nbExG6hxsj49mXNxuzGZjRDcTKexN5kpEo8J5oUv74a9uFpRRkW5h8iU6nOxnizOOLHL0lSj7G-X24j1YMhWRd-IA8YxuGKquURJ9SwVU7Jh2Wgy7hzQhbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 21:12:19</div>
<hr>

<div class="tg-post" id="msg-456279">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiRnUX1bBJQ6PZgttwH9A7Dv3KJBAuHzPjaFt415WlwyY0GKCnk1S5wNuXvX27kvsr_l1Q67bIPchpANIGzLLYejl8n3DDAR-UxJl8cCzQshGCViSFEZh5W75WO44XZyShuKXRMFqBUJMxsWtdcRGyi9QfnwOOv0_Bn4InCK5MYeusLsRz2vSgl1iX6ikY2rQpIFLdQBDgFyk2HbSAzEEBdrjyS4eaWcgmRpq4vVr7pIZQnrhl-EWW7_xk_tBlp6t4VkyCBepTdk7M4ffOSMWGCNRR1Bpg0QxhryqE7_5UiCZNteDkSzcQ4VCV4IdV3IhqZFFpQe4FOpCck0MfdMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌چی‌تی سناریوی قتل مادر و برادر یک نوجوان را به او داد
🔹
نشریۀ گاردین گزارش داده که که نوجوان ۱۷ ساله‌ای به نام آرچون در ایالت ماساچوست آمریکا متهم به قتل مادر و برادر کوچکترش شده است.
🔹
دادستان‌های این پرونده می‌گویند طبق تحقیقات او پیش‌از این حادثه از چت‌جی‌پی‌تی برای جست‌وجو دربارۀ داستان‌های تخیلی مرتبط با کشتن اعضای خانواده‌اش استفاده کرده بود.
🔹
آرچون در قالب داستان‌های فانتزی با حال‌وهوای رمان‌های گوتیک، شخصیت‌هایی می‌ساخته و با روش اینکه «اگر چنین اتفاقی برای فلان فرد بیفتد چه می‌شود» سؤال می‌پرسیده تا بتواند سناروی قتل دریافت کند.
🔹
گاردین برای دریافت توضیح دربارۀ این پرونده با اوپن‌ای‌آی، شرکت سازندۀ چت‌جی‌پی‌تی، تماس گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/456279" target="_blank">📅 21:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456278">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2c5c57d6.mp4?token=kWWCS_FQu2dP8luKd684rl8nJIVtLQ3gs9Qr-efMVzrN2dhQNMIPRQtZozzX2EIb-iW0XA5UJDMvm1GRzB-2UY4sHP9GrFiDKe-43dalCBez5FruZZb2KB8rhiTtSfTdgAm1wW6rpeY3pzSLXz_LuL3qz1Ucy_lTX9cbmxxIQ5jvcT2xVqql3p-eroSkP5Vw1t7rqmID9cCC6RH8WBK4Xw3b_AtPVJCTAhjPbPTvJDkdwopgkpOdkEuMY18glB_7i5quQM2_wQo07PmfgP4PBAk6Z9phW34JIjCSwPvNjXzk6v0FH6SVzO3uYTQMhRV-Y_F92DVjFSROIBL07s39jzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2c5c57d6.mp4?token=kWWCS_FQu2dP8luKd684rl8nJIVtLQ3gs9Qr-efMVzrN2dhQNMIPRQtZozzX2EIb-iW0XA5UJDMvm1GRzB-2UY4sHP9GrFiDKe-43dalCBez5FruZZb2KB8rhiTtSfTdgAm1wW6rpeY3pzSLXz_LuL3qz1Ucy_lTX9cbmxxIQ5jvcT2xVqql3p-eroSkP5Vw1t7rqmID9cCC6RH8WBK4Xw3b_AtPVJCTAhjPbPTvJDkdwopgkpOdkEuMY18glB_7i5quQM2_wQo07PmfgP4PBAk6Z9phW34JIjCSwPvNjXzk6v0FH6SVzO3uYTQMhRV-Y_F92DVjFSROIBL07s39jzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۱۶۸ به یاد شهدای مدرسۀ میناب به خیابان آمدند
@Farsna</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/farsna/456278" target="_blank">📅 20:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456273">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMogqAtmwgTjep7-MajQooKHV_zcKKhcbWQOwZ6HJCTLam9c0BJtsQFwqF6sIB8bvW2mrAmdNBOUv0WvGrNdWKDW-AcAx4fJi--SRq-ED_lHTpQCJ-Ke9-yKcF4p2bYyjfeWPYh2yVVElWXeK4ZpcZHfNA2C-P0YGISWwA-ipfULzqpffCtCr-_2675FVUebPCd9nbov2RE7_oXjcsV9bMgIVK-R4Tzuv8C8DIqsE-GhGELibb6ADkuo8TdocgzuR1QKf1Oh628R8Id02NwVBq4CkQlSrLwxe4V5CTo9K2aFkqbVRLIjrWWsdB24Vb9TziIPa04L3t3t816uENUcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYpX5c9IIdAqGpnRIRNS2bX1YCAui2UdCrw1e5mUj9AuZ_BQABeWHlwRvSPtb3Y5fAr-J7xVHTvIiwoJ-oYjprAixEYGlqKCvmKahoqHj1d_K7bmhgprQ_DLYdHqL5bXHzZAvellfWDqPAqhU00WNMMYRt2nkmpj2_TeIHfu23Bu-oeGUtxGa-WT7SPelqop2iv9kCux1eRsUzvzzDwZFBnhAKzWqudHYwWO9p7Y-uW63A2FuGqMKJHHzuEDZauwjveUnPZUxVBX5JTzWRofWX3PVhqa9pC8QGAlBU_GQvAAb44YOsFMU8Qu1vjw-SX3ryC38YEy7yNgL5XRKfECUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_SZBMNVfkeyQDjy9AHlHaedkVHGEJU2LaMQSwIM-4SP_oN6wpshWHVx7-v8a-8KhY0IMgdhN7006mMW7hXYRxKrc4PrQKE6vpKlW4movxQnoWJDBpQOHO4hhCk1a0aKPKksmnVM-nZ4kZgxYQ5k8lT7J_OJ-Uxc_AY8paPEu6_8QLWYdAA0BwnzxU_F7WxfWcd02ICaSvkf0WlOld-Bq4s1QwN1n4Ah4ohYORh-jU1ALlhAZarABrqlg8Grv7UKecgjBFV5EjqrbA3Yg7md1F_RYwP1FFk9k5KP3fz752vHPjv8j9RwRywdQm535DyRsfMAZOGgx6G5WLKIqTBQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INfJ46aie5_fz3HCTzFxODFbONwuI_1-DUURgONjNGEhtOSjR0Jn_4jWU2ARY-UWDG329Yq79f6ZIymMXnc7bmIxhX8vDtd3NzrZqT-4hhMALwZFCaWaKQCsDTdi3DpIMYj5YaPkr4dH64j5CdsqI_JWHdcEhJOJor2ytDH_ghRDkkggEKdu86qSo8Q44B2Rh03w9_8jY0WJykzfj4UPel4GIdztOD9V9arE3LsrvII_xdw1U0Al_FXSzlZyps7GeA9KH0cO3W0N1iIJhUlka7Fpj6aTMTFQ-4xQbObVA1_2c43lR6Rbkc2uoAxRRp74GCKPU6SH1t26-F15WD2O_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vfn5aNsl_5sbaL4b5blmGUp3-IbuPX0djSP9LDBM5uksWpBfXAsX86ljLWFdV3O3nhkxGd2Ro1m5xQgBPgeTLN0EFshq4pijKGOfSf_unj9Ceg9LtL-qnBpRJhhCmPhy5RPH8I2YE51UTK-9dcobtsivO8Q2tzD7DugiDGX1qA1Ok-Sm_ehJ4kogrLEzVdisRJbm3_W3W7uXikSmuWoPqe-T-rfM9ZtjGJThwLf--Ncxue_J9e6gyMeqSz9N1mdB4RKN-8t6dF-tz2pCJOi9--znkMciedXVwivIPpL4v_miJw_ozxNdGPrCNDgauUcaGhvxv93WQ5Mnblt4NelCFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
مخاطب رسانه‌ها در یک‌سال اخیر چه تغییری کرده است
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/456273" target="_blank">📅 20:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456272">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEgtVPiKgoYy4Z3q1aEGpEBM5Xrpd-H-Z_4lMr0CPqouiS0QpE99FhtlowaXJec1wrNezxXamuBcvbJDC-EXEJ3kG6pESYgUx7hrmb4iRoSbFPPnvQTfJFZu0x2oowldGtTE2Kd9B8Ub2gQWEmLVRU4ltSDtYISdklHNtm_CeellB4juDLbSkeEBZAubodNrkednrJ5N6yGm0h0fg_wQuMdarUTksabhM_SVc2EAM3ylCtDoCsViGuypDALAIWqa1gKVPKxBJY3nd7etU9Nb1_-bvr1iwyd8JGcqTaEGiDSC9ka7vo2ipFt0vQhEYgAYMZ-_NUT54Qc3eyOdvplelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توسعه شبکه ارتباطی ایرانسل در خراسان شمالی
🔸
با بهره‌برداری از پروژه‌های ارتباطی ایرانسل در خراسان شمالی توسط وزیر ارتباطات، شامل افتتاح یک سایت نسل پنجم در بجنورد و یک سایت نسل چهارم روستایی در شهرستان مانه و سملقان، دسترسی ساکنان این مناطق به خدمات ارتباطی پرسرعت ایرانسل توسعه یافت.
🔸
این مراسم، ۲۴ مردادماه ۱۴۰۵، با حضور وزیر ارتباطات، استاندار خراسان شمالی، نماینده ولی فقیه در استان، رگولاتور ارتباطات، رئیس سازمان فاوا، مدیرعامل زیرساخت، معاونان سیاست‌گذاری و حقوقی وزارت ارتباطات، جمعی از نمایندگان استان در مجلس، مدیران استانی و مدیران ایرانسل، در قالب جلسه شورای اداری استان خراسان شمالی، در محل استانداری برگزار شد.
🔸
در این مراسم، سایت نسل پنجم ایرانسل در شهر بجنورد، با اعتباری معادل ۲۸۳ میلیارد ریال به بهره‌برداری رسید.
🔸
همچنین سایت ارتباطی ایرانسل در روستای شاتوت واقع در دهستان شیرین‌سو شهرستان مانه و سملقان، با اعتبار ۱۳۰ میلیارد ریال از محل منابع USO به بهره‌برداری رسید و ۸۹ خانوار با جمعیت ۴۰۲ نفر را تحت پوشش شبکه ارتباطی قرار داد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/456272" target="_blank">📅 20:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456271">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA15_DHpWy_iwzefbxGe_1Ieu2bA5Vk-Ob5RK7VA1z_-dmqr9MB0QEK8AHwy3BS9CxGotYLqbQ4WGv4z_R2Y12Aa9h63Cf1qLd4WoIo4iDuPn2GKLiUhaACzMggfpULd1GQ7Z9t_EKaJvx17HInImZYP-Ta2P30dZhX4Sds9pBxdXSqs6Wzoby4k-4qlSUlO6fVrr3E9xzLhMT3oglBrH5d3tefDy50ctgNyWvZP-ilFzEel8llYqQJ8GJRdhXJxG7jNfxKnpPVsD9jd5XzXDFnhkK9i9UVBm4L3xIcV74FA3uWbdulcMLW2_S3bGR3paM4h1aOaufZWXHeX7Dz1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»/۸
🔹
ثبت رکورد ۷۲۶ همت تامین مالی در سه سال توسط بانک کشاورزی
🔻
حجم تسهیلات پرداختی بانک کشاورزی با شیبی صعودی از ۱۸۸ هزار میلیارد تومان در سال ۱۴۰۱  به ۲۷۷ هزار میلیارد تومان در سال ۱۴۰۴ افزایش یافته به طوری که از سال ۱۴۰۲ تا ۱۴۰۴ با رشد متوسط سالانه ۳۰۰ همت، جمعا ۷۲۶ همت تسهیلات پرداخت شده است.
🔻
رشد مبلغ تسهیلات پرداختی هم زمان با رشد تعداد تسهیلات، موجب شده تا متوسط مبلغ هر فقره تسهیلات نیز به طور میانگین سالانه ۳۵ درصد رشد کند.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/456271" target="_blank">📅 20:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456270">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/farsna/456270" target="_blank">📅 20:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456269">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
منابع عربی از هدف‌ قراردادن مجدد مقرهای نیروهای وابسته به سعودی در مأرب توسط نیروهای انصارالله خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/456269" target="_blank">📅 20:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456268">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oelKoekKluVD2HgjHLbPJd_EbAMI7CNgZbNPR35F-iKpYbGkewC4S_QCIVQXLVDAtv1HmT5sIZpM1oXjOMHWSxY-b8P27cxOCIqFRlMxT5Cd1xIR_BdpIFzt7r35Ls4AkEB1mVDM-W8m20z0W_dqHWwpTi2JApsbq7oYJ38uRnfBsb8edFbcLb_JGlrOQYqImOaRgiJlJWh4-UKZCSW82zsgzi6qaICwat5zo_orWUw8LOYgRKZTsPLtb9sK-YDiprtYENzz5A9LytxJG4zhQFGkQckm9k1neUaHvi-kHkx86RR2Tbyz6bZp4_sbc6VuRiEmbRPfaJLn8LOJsrdLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس دستگاه اطلاعات عربستان پیام پادشاه سعودی را به الزیدی تحویل داد
🔹
نخست‌وزیر عراق امروز با رئیس دستگاه اطلاعات عمومی عربستان سعودی که حامل پیام پادشاه این کشور بود دیدار کرد.
🔹
علی الزیدی مدعی شد بغداد اجازه نخواهد داد خاک عراق به نقطه آغاز هرگونه اقدام…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/456268" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456267">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انفجار بمب در مسیر تانک اسرائیلی در غزه
🔹
ارتش رژیم صهیونیستی: یک تانک اسرائیلی در جنوب نوار غزه و در منطقه خط زرد، روی مین ضدزره متعلق به حماس رفت.
🔹
در نتیجۀ این انفجار که صهیونیست‌ها مدعی هستند تلفاتی نداشته‌اند، ارتش اشغالگر شهر خان‌یونس را مورد حمله قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/456267" target="_blank">📅 20:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tctossU_Fm5JArksudrnf_IvI_bTQ80dw9H3Q9TxI1SFcYqBza6RqH2O9D6CH2xnvwW_R-kiC4y_g_tkW5U-gyRhM5tRvu4IFPpc7b8fAnR3TUZvyc5JxEDJNamQlF3TsY7JSsA-eA1CAbVyGic9gnuj6cyRXSd-WEJdaGATfT-9kHT3Y5sjPcxuheDbADbaZnJxflC7fDvup22d5U1Uq-lT6v00CGOzzX1SHhS9sOHLGimDqYkJKyiSTa36cP3oljlL3E-n9lh8kKHSnYMhwC0N7EKhIWMe-3chofIbTNa-k06a9TxccxTBU4CVxxlOV4sgkLAoHXzIl4PDrIKpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmffCAsaOFwUi4NAXF4Wxb7-OQrD8SKXxbdEZ7Aw4bI5VCa6E7gBNqrDRkMkhPYWGW3bsL3Qx7LoEiScHbeTrwLnWy--5puEYtfJwTnyWX9S8fc8fnUdFnHim1kK6zyrRrj6HuaYncAz4nPbkVDtvwhpeBJZPMWBCpKPcdgtbQqXy4xtCDGx8buQHIl1RWL4JrGy9l8Orl3UkFG1L2p7hgQcA3ohQSDWn4IrX0NJ2qQBHNLdH_3nPSfEbyCmtO2535RA67zP9UxDmkeROzoFemfsDz-NFdnd7jJYEX-Xzf7DBNUIVUePeGrICYo95-Ody57zGXpdvzvC6-dP0TgGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQZCRGJ3iDvklY0Olr9wpmmStLpkLcfuTsa355Qndm-3LITpyvPwn0aLRbMTBQY5oaCcp4dmDeJiVjF3FRoXXWsIp2MssTarZBkjnpljki9_gKj-uGob92jJmdPF_dIBCgETJoEXSkfjXMsu0bbLMXUeILydGpNxLt4JQu2JD_QZgMq3iq8vwqnbxTcdSTraCK4oeqpViLd4Xe4nbiKM7HX-zi3odzxEwTT71rfS1Lus8-Ag5t21NdroCLYbsAZMf6_OamEhw-YJlqIOb1IOv6DgtxGOODqQsm1RTbpf5sT2T8C7--GfzSs-UZLtXz8_bdZVNU57dxR_jnjGvR85gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFruh5MF0jd2iBsMkaOfRsQs0SkEzpsVBpzMhFyQr0J6yNj1Vi_Vx-emWR1q5rSuiftlnUqklQGnJAzx6mMPvQYwedYzDr7ssU3BhgOPZEV3CrXyZJJYR33tDErPHOU7SuCl11glScaUQrsm-w5oXOzHzd3GFGI9hbXvO177wEy8qgCK6Fr-CO-sRPckMshu9Vl5oQyUzYQ2L8yGSk8IEzmDFyO2mRe4b1ZennWRwJXYP4eNCXrYSaw2j8X4-rkL3eYM6WPOnJlkiVF7b6YsiNYH8N44MCGrxUIQFvdnrmevyWzE9EhlbvxLjoKe9kV7FV_xQEUS9O_xFLo3YKE8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UaEmErjgax_XtFgbzsi1rYWRHUCi3g08CIbEqCAZHxBaA-rvw3XzfjmuK4xi1G9TuG_yfUHdR7Dx56LTe5xwb_-SkEOnri-TtHWu1cPQ22l8UweYy4Kb02DWecZ57sa_KUPEusVmpglYGg2HJOfelPGdbFmMSEofKpJdu2XbPB12F8fF7EhsW6122EgWvXz5vt6paPCJpPvF4Q8TeOt9reLGf3FgS9EyU6DPQWrHhiXYnyOuKFcDZQmXAbOfidAfH6h02Ur7ERMkomVjUQtQ5ayijYpSL7K0ad7a6ITZso6ftTTPsT1-zC2ehQ8c5y8iMJ72qmLrF_t23_akdONKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaZ4b9iFxjhQVPypfHojpbIw_EDBX3xLPjC4__mOvedroqAfcZJGRrsP8IV2kMzb6lwsmWv9RKK1TxxaTyharIrHAaKEYIBXn8szAqjDOKgagy-2uUmHH1eLoOfqH2HHuUHTMPLalkLLHBbU6TrdxBXp3J13LJ1FHsHHyjyUGFPMSyYoB4-ZsYRaGj7PBz9V_6OSXYfFXBQsaWS0hkOkwzM563ROXAbnV2thYZyOh54-KopilcN50fyBlMEH074ZEIPPUDbGWWoMdV0PfM4KcgRZjqYE5iEOhgNW3VPnp93Ya2BC7a1WWwiM4pJKSJFKlUkMpH7hdW2pMN2AvBeXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JRikCJ8lGyP1QXSrUkRh0XzoXL3VfJ02cQTDzRrowI9NLozNs8fYnudl7sPUnJdyRGAD6fF712BZpv03vFtHCWEgfo-eJk3Rs0FBxBkffnF55E6YiKznmuYRBw5AZEPiaLXCy8U7W7TsBY3uvIM0zQ1EkNvmwOvf_jwItWNliIzZNghCyLkj2PRvrUe9QvjJQ851-MxHlWrfZSMmUnTTsRaAdO_IaH97zjOq6Pe9_YElBU-yD0mbSNDQSnSn0Y7j0xmRjyMQnwlnRDELMcMHnZCW1m9jMIYwAYmXYU8hGdX7TJzlBMOHxwWVD61v7jE-Tg-_M3bNSVePCPYvPzZD6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس دانشگاه تهران: کسانی که در سطح دانشگاه هنجارشکنی کردند، احضار شدند و شورای انضباطی به پروندهٔ آن‌ها رسیدگی کرد
🔹
به‌طور خاص ۲ نفر را داشتیم که متأسفانه در اقدامی بسیار زشت و هنجارشکن به پرچم مقدس جمهوری اسلامی اهانت کردند؛ با این افراد مدت‌ها پیش برخورد…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/456260" target="_blank">📅 20:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1130cd59.mp4?token=XIUBk2klwwS6sBBiHCYGRtb1JYyeXsJ0_dbIIcOkaKdilzL1InmGdicTCB7EOjn-U3IeKAzWF-FZfZDWE6FvCzPWinRfxbXVqQ8J3rsWsnBnuHtGlbFoMyIsLpir-Tc95p9ho7AldxKa10nTxCp-1cBC3jzuWqR61qAbQipiFOfxOk2PRO-X0-jG-I6fOwYEv4v4g3Q2ytj4hVAaZ6gDN73syQcV73a51leuC63cZ-OpC2kDMqAFpIGUELnDBvjroZBZT96-RRxkGOQpq-gPFUzE9vsQSQCJxLs0n-bQLgaO5FoRd5bpp2Im_HMfTh4s3oIRdXjD4gt5M_QnBeZ2gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1130cd59.mp4?token=XIUBk2klwwS6sBBiHCYGRtb1JYyeXsJ0_dbIIcOkaKdilzL1InmGdicTCB7EOjn-U3IeKAzWF-FZfZDWE6FvCzPWinRfxbXVqQ8J3rsWsnBnuHtGlbFoMyIsLpir-Tc95p9ho7AldxKa10nTxCp-1cBC3jzuWqR61qAbQipiFOfxOk2PRO-X0-jG-I6fOwYEv4v4g3Q2ytj4hVAaZ6gDN73syQcV73a51leuC63cZ-OpC2kDMqAFpIGUELnDBvjroZBZT96-RRxkGOQpq-gPFUzE9vsQSQCJxLs0n-bQLgaO5FoRd5bpp2Im_HMfTh4s3oIRdXjD4gt5M_QnBeZ2gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به شمس‌آذر توسط محبی
⚽️
شمس‌آذر ۰ - ۱ پرسپولیس @Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/456253" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va34oLogas1_sbVEJCtxL55OrCcSF7dbpffhvCftjMtoNI3dIayoiu3j_gvJ6sfPTKmvqKvR4wG-ZHWBULNV2ZCZg-3wrn-tD4AgMJCm9gykFKg6tBZBH00BMQu-5dAnL0nGw6ZIWliVyeNQu9IG_jLRL2-vG3tYIZ9uaIA-gzSi3QDlTEDRTtdGWGQCRdq11IvwAVwJRQEWcKngeTgcfjOEpDxpRm4Ii4lNbgtTFa8HKomn-578tOvvx0jZRQyvJYPzfdioaZrKQ5iWXzvaRQt96CGjDASIaonqWr2iQaY3GFmx9Lxqbcrt9tCEAm-04AXOtasLBOncbgZ31SsSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد عجیب انتقال چمن آزادی به اراک
🎙
رئیس هیئت فوتبال استان مرکزی در گفت‌وگو با فارس:
🗣️
مدتی قبل پیش از شروع مسابقات لیگ برتر یکی از مدیران پیشنهاد داد که می‌خواهند چمن ورزشگاه آزادی را به ورزشگاه امام خمینی (ره) اراک منتقل کنند و چمن ورزشگاه امام خمینی را هم به ورزشگاه ۵ مرداد اراک ببرند. وقتی این مسئله مطرح شد، من به‌شدت با آن مخالفت کردم. گفتم اگر چمن ورزشگاه آزادی خوب است چرا خودشان از آن استفاده نمی‌کنند؟ اگر این چمن اشکالی ندارد خب در همان ورزشگاه مورداستفاده قرار می‌گیرد.
🗣️
خوشبختانه مسئولان استان مرکزی هم به حرفم توجه کردند با انتقال چمن ورزشگاه آزادی به اراک مخالفت کردند. اگر ما هم به این پیشنهاد عجیب پاسخ مثبت می‌دادیم اکنون تیم آلومینیوم اراک هم مثل استقلال و پرسپولیس ورزشگاه خانگی اصلی‌اش را در اختیار نداشت و باید به دنبال ورزشگاه در شهرهای دیگر برای میزبانی می‌گشت. چون انتقال چمن آزادی به اراک و پهن کردنش به این راحتی‌ها نیست و کاری زمان بر است.
🗣️
شنیدم این انتقال چمن حدود ۵ میلیارد تومان هزینه داشت ولی مهم‌تر از هزینه این بود که اکنون تیم آلومینیوم اراک هم بدون زمین و ورزشگاه خانگی در لیگ می‌شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/456252" target="_blank">📅 19:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18bc020ef.mp4?token=fq_DPR49XSv24kfFdX1ozwAL4iEJjfyt9YtdSazZ5j0s7f57ltNGzwg-w4cFA0dKbzvl3UhSfRbQwlsh4GGcxnddzZ1kV7P7W3yE2LopsCv3iUcN0oydcYNJLyZK_8IBJyr5sgluueNY7bWuxUA2CTqRFyiLqk5K5zpvxaDfSLM8ivVvuWpS7ncemGWX6QjQOXQDarQYW1JHZPHhGZipZCz_jKBxVANc5dwDYSCfCofZrzV-FPUX-zb1481L3jomzI9SuPwNSOoidiJlzp7bZ22EweEz3SQFQs9fjXPeE9Aq0bVs_hkxpqPckfynqfz0BY9hU4LB70i48_zZDiWhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18bc020ef.mp4?token=fq_DPR49XSv24kfFdX1ozwAL4iEJjfyt9YtdSazZ5j0s7f57ltNGzwg-w4cFA0dKbzvl3UhSfRbQwlsh4GGcxnddzZ1kV7P7W3yE2LopsCv3iUcN0oydcYNJLyZK_8IBJyr5sgluueNY7bWuxUA2CTqRFyiLqk5K5zpvxaDfSLM8ivVvuWpS7ncemGWX6QjQOXQDarQYW1JHZPHhGZipZCz_jKBxVANc5dwDYSCfCofZrzV-FPUX-zb1481L3jomzI9SuPwNSOoidiJlzp7bZ22EweEz3SQFQs9fjXPeE9Aq0bVs_hkxpqPckfynqfz0BY9hU4LB70i48_zZDiWhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پرسپولیس به شمس‌آذر توسط محبی
⚽️
شمس‌آذر ۰ - ۱ پرسپولیس
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/456251" target="_blank">📅 19:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqgvE7Jwxjho6365hH2yDcw_9dC8wmTXeZ5KI9FHBnvAGGhlxInBcKHqQ92JiKjMJf_B_xs6qZxqt_Ua-IVd5iCETiAP5x4HuMlG_rFYX8w7CYTobq9YIWqB-avB3VcvMpn5ftqIx3D4HlbMBhHxlFUlFJ9T_4loRQoZJ8bIjUATQC7TIPR3UXHjaBHzrudygEnR3K3u7rF8UARf5w3xNRITiWDYVdqb5FH7IvSP4Hyt8cE3aRZ1PzRe33IJSfxek8bbIMEQ5KsKZqcCRPYii7_itWlCNwDehjAMTU7S8pI3pyvf2mO65WN_VWjYn2GWYSRtdvWkmxgLJhefggvgjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن پرسپولیس نیامده جدا شد
🔹
فرزین معامله‌گری که از تیم شمس‌آذر به پرسپولیس پیوسته بود، با توجه به مشمولیت، برای گذراندن خدمت سربازی راهی ملوان بندرانزلی شد.
🔹
پس از پایان دوران خدمت سربازی، وضعیت ادامه همکاری او با سرخپوشان مشخص خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/456250" target="_blank">📅 19:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456249">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54eb9c5b02.mp4?token=q2m1LhPLr78ieYU3ATV8cPdvrXMqyZl89tGn9dVl_B7LhqcfRIfGmzrqfw9eB1KgJh_V-FOdIdx6ixF8cSYOx1B2eLUZRqERsTeH9ZnZKhkt1tox_yySvSeH_ZdMvXZaLwrn9u2p9kJ5lciVJ91muEdBD4kv34_KiZj5oksIHDEfcnCtjHAA35kxzPNScpe2gT23JJi2x2dEpN3DpKJEL4qclgAt3kMMaIHbnO9xcY_UTZtAgdyHwT893fShk-pWyvuo9DVM40XrcCUiCqFeNIT8TrfA9Z0yIIEO3IF7j1wl3diNX_wYy5jtx8VgIqa3i-FZ5-2gH2DXquqlpExQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54eb9c5b02.mp4?token=q2m1LhPLr78ieYU3ATV8cPdvrXMqyZl89tGn9dVl_B7LhqcfRIfGmzrqfw9eB1KgJh_V-FOdIdx6ixF8cSYOx1B2eLUZRqERsTeH9ZnZKhkt1tox_yySvSeH_ZdMvXZaLwrn9u2p9kJ5lciVJ91muEdBD4kv34_KiZj5oksIHDEfcnCtjHAA35kxzPNScpe2gT23JJi2x2dEpN3DpKJEL4qclgAt3kMMaIHbnO9xcY_UTZtAgdyHwT893fShk-pWyvuo9DVM40XrcCUiCqFeNIT8TrfA9Z0yIIEO3IF7j1wl3diNX_wYy5jtx8VgIqa3i-FZ5-2gH2DXquqlpExQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماعات شبانه تا چه زمانی ادامه‌ خواهد داشت؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/456249" target="_blank">📅 19:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456248">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad5513ad.mp4?token=TDdnww7B-39InsmbKvl-BaKGd86y6cQbWhYeoaqUhxhluN1aVd6nfzmKMfA9y6YidhBs3URakX4LhH7Nuq1SLAzgciwp-lnZNN_wmHRSTnv8T2rNEPrY6MZNac9RXDR9wAaAAyhtDQm79qT796dklGOSiUw6gTAcBXyCGryO84zu5wFVIFtgf_rl-EjA0mPooMG7suMWkmDhL2WATEN_edHoc9KdDEprKMpyxR9ZzpGyZzJLRZD8WWMBwFCtFRydtqFhEp_zxw18mNcS7RUxAIUzLjcvZOyeCCOs5XMSoTJaLuQCt2ISmG4IEeccxGYS_vk_duPAQ86FwsBpxWHgSzdfrqKj_IoYLBanmgW1c0TY_EzE89c9LLroxY2dNaUum5JUksywTQswQt6dFTsEYNtM2UmaJ2VO_i1efN4ewLR3WXWEO_CNufupzpgLDiEQ_MJskRLhcyqnPdOOzLSwOZxh-UH-mctT-cKNCPjtaQsah7xh2HDJc3pflIjIP9c7NM_9bBYJ5AEKHuyPvR4sAMK6o2O2F_cuMTqzkb_dKilCcsPTI3esSZYgUiWT_Dm3ZmiKXcu_DrY_B_Nvz3h6d3550U7ggr8dLYECltU9cFdj5W7W0IFirgHWcB8nUcil7mKQBX4wkOLPI9XCMS3sOLfpXLZQqdbWWRmh8LspkHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad5513ad.mp4?token=TDdnww7B-39InsmbKvl-BaKGd86y6cQbWhYeoaqUhxhluN1aVd6nfzmKMfA9y6YidhBs3URakX4LhH7Nuq1SLAzgciwp-lnZNN_wmHRSTnv8T2rNEPrY6MZNac9RXDR9wAaAAyhtDQm79qT796dklGOSiUw6gTAcBXyCGryO84zu5wFVIFtgf_rl-EjA0mPooMG7suMWkmDhL2WATEN_edHoc9KdDEprKMpyxR9ZzpGyZzJLRZD8WWMBwFCtFRydtqFhEp_zxw18mNcS7RUxAIUzLjcvZOyeCCOs5XMSoTJaLuQCt2ISmG4IEeccxGYS_vk_duPAQ86FwsBpxWHgSzdfrqKj_IoYLBanmgW1c0TY_EzE89c9LLroxY2dNaUum5JUksywTQswQt6dFTsEYNtM2UmaJ2VO_i1efN4ewLR3WXWEO_CNufupzpgLDiEQ_MJskRLhcyqnPdOOzLSwOZxh-UH-mctT-cKNCPjtaQsah7xh2HDJc3pflIjIP9c7NM_9bBYJ5AEKHuyPvR4sAMK6o2O2F_cuMTqzkb_dKilCcsPTI3esSZYgUiWT_Dm3ZmiKXcu_DrY_B_Nvz3h6d3550U7ggr8dLYECltU9cFdj5W7W0IFirgHWcB8nUcil7mKQBX4wkOLPI9XCMS3sOLfpXLZQqdbWWRmh8LspkHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۲ حملهٔ هوایی شدید رژیم صهیونیستی به شهرک دیرالزهرانی در جنوب لبنان
🔹
رسانه‌های لبنانی از هدف‌قرارگرفتن یک خانهٔ مسکونی در محلهٔ «الراس» در شهرک دیرالزهرانی هوایی خبر دادند. این منابع گزارش کردند که همزمان یک موتورسیکلت هم هدف شلیک یک پهپاد قرار گرفته است.…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/456248" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw1sYa3Z0TRnYntJZqFzlVIovmJgsZ54TxTCvz0S8tcMGsfdVh_CgjCpeXrGN3PLj3GByXB1C8eN1J_4QGAnNkUluGC4MMx7KmbwW73cl3PCBH_bD0Kjb5P6iC3Z11QsRUF3hKexiCR4ud1nlBE2twkcJcxoqqD_-K7Tkxb66-ecr4zf9wozg7DqHFaent3jtJlTAobrXma6X3BTocc1kPgbxyKxUaefXsPMYea5B_o70bBDUtMQSKgRJ8h0J49g9NvRiECI9dWQGr0MqgqwfLRVYKEhZSYIeiOJxj8qhbFsJl_dnb1Z6C_47qhD5sjFCNK2lyJejGLjxivhWCnfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأکید مجلس اعلای شیعیان لبنان بر توقف فوری مذاکره با اسرائیل
🔹
نایب رئیس مجلس اعلای اسلامی شیعیان لبنان ضمن انتقاد از سکوت دولت لبنان در قبال جنایات رژیم صهیونیستی، تأکید کرد مسئولان این کشور باید به این سکوت پایان دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/456247" target="_blank">📅 19:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103ce0d5db.mp4?token=NMpK4Cv0ADtAfxvFkr1rH1_1biLZJ4av2Ib9DQZ5ccDXxsrH0QgxWaLq888G9JiT1E5_IqAEIJjPjUhOBVSC_ufDC8d2ejHBh_KAN667VBNCo806KqNvfSIZyvrBgODNORZsPCgMYggVOAHu2oPv24AHOrvUQ3axWvnE7pO9oFnXlNq7gQ9WDbdiC_gnhlIAFMzKqLjZhFGRZHm8RQYtIyVDYF6CqI0hFO8QAta2gVls88emEHlcDgz0P37G1g1hyWZmXmb9MtycmnOvh7jaTWLuYUZDmjzI5SstPoK29xoFQIrPlwKOjCfnGEE5qdOrCrejXfBtfnN_QJx7dIPD0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103ce0d5db.mp4?token=NMpK4Cv0ADtAfxvFkr1rH1_1biLZJ4av2Ib9DQZ5ccDXxsrH0QgxWaLq888G9JiT1E5_IqAEIJjPjUhOBVSC_ufDC8d2ejHBh_KAN667VBNCo806KqNvfSIZyvrBgODNORZsPCgMYggVOAHu2oPv24AHOrvUQ3axWvnE7pO9oFnXlNq7gQ9WDbdiC_gnhlIAFMzKqLjZhFGRZHm8RQYtIyVDYF6CqI0hFO8QAta2gVls88emEHlcDgz0P37G1g1hyWZmXmb9MtycmnOvh7jaTWLuYUZDmjzI5SstPoK29xoFQIrPlwKOjCfnGEE5qdOrCrejXfBtfnN_QJx7dIPD0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارتباطات: دولت پیگیر رفع مشکل ارتباط خراسان‌شمالی با ترکمنستان است
🔹
هم‌مرزی خراسان‌شمالی با ترکمنستان می‌تواند زمینه را برای همکاری‌های فناورانه و حضور فعالان فناوری این استان در کشور همسایه را فراهم کند.
🔸
خراسا‌ن‌شمالی باوجود ۳۰۰ کیلومتر مرز مشترک با ترکمنستان، هیچ گذر مرزی با آن ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/456246" target="_blank">📅 19:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH48WJSSQU0e6Esmna_kp9U3wspCAjE50I8j03Okr4eZJJkMNbOwxUqOTKYdBRGIS1u6TohYnuDeoljc2BPueY2wmGAk7LtBPlJGfYP8T3X8SsGN5kdIyvLOT9dAZZZetDe5GuBIfr-ttzDibBMm0crno5xJQD8j2_iWDWGNNKl4iSvN-sIPKE2g2nMOwXPle4za9EtdBssC5Ykmc7w2VHCJHgZ9osGV8YdA0EaAmo6FI3MfbDNxRtv9aApoDuqxbFP-GNMzgJqcBBXecw6FluOd0wAEzBnTdXRjeVXxt5V6ACearzFWiS9ozsIIaHX2GYCKHWYpb75oh7n3QGFUew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد پای شرکت‌های نفتی انگلیسی و آذربایجانی در سهم ایران در خزر
🔹
کارشناس سیاسی و روابط بین‌الملل، داریوش صفرنژاد می‌گوید پشت پردۀ تلاش‌ها برای تصویب کنوانسیون رژیم حقوقی دریای خزر که فاقد جامعیت لازم است، پروژه‌بگیران شرکت‌های نفتی انگلیسی و آمریکایی و آذربایجانی هستند.
🔹
ممنوعیت احداث خطوط انتقال نفت و گاز از آسیای میانه که از شرق دریای خزر به منطقه قفقاز جنوبی درغرب این دریا وصل می‌شد، از ابتدا در متن این کنوانسیون بود.
🔹
۸ سال پیش لحظۀ امضا این بند را از متن خارج کردند.
🔹
قرار شد این موضوع به صورت یک موافقت‌نامه جداگانه آماده شده و به امضای رؤسای جمهور برسد و به کنوانسیون محیط زیست خزر الحاق شود اما این کار انجام نشد و اکنون با گذشت ۸ سال هیچ اتفاقی نیفتاده است.
🔹
اگر این سند در مجلس تصویب شود، یعنی مجلس محترم سندی را تصویب کرده است که می‌تواند زمینه‌ساز جنگ آینده و اختلافات جدی با آذربایجان و ترکمنستان، به لحاظ قلمرو سرزمینی، حوزه منافع ملی و امنیت ملی ما باشد.
🔗
پیامدهای قانونی‌شدن کنوانسیون خزر برای منافع ایران در زمینۀ منابع نفت و گاز را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/456245" target="_blank">📅 19:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ba2d71c38.mp4?token=X5hHeysw5tdAJn4vmfimfMmNZGmiWyBreONbDS9Kh4yFX5NWS4dEqOJFjaLDJ8YsrTLSg_G3XxBpgABnut25oOmvnMvVWEYsmw-sBGTcOpD5xjHrODt-9fpiqbqSbsGnUFRZaSEKPvp92KAQkWKUQ63rHNJYF9kbWkSm7di37TAB6koFH82T-AV7D5UA6eu2U3gTx4IGWxp8oWhebBvtrt17AIpthfjjzquhvoisBMLSImetvOmpgaWBZYhUhAknrMKie9rNo8nZD9c2J6LuRmEyg9LYickd6QfqPUx2q8vuq_81w0bMT47VCvaqiqPpwJkA03cBru4r-gJGZy40-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ba2d71c38.mp4?token=X5hHeysw5tdAJn4vmfimfMmNZGmiWyBreONbDS9Kh4yFX5NWS4dEqOJFjaLDJ8YsrTLSg_G3XxBpgABnut25oOmvnMvVWEYsmw-sBGTcOpD5xjHrODt-9fpiqbqSbsGnUFRZaSEKPvp92KAQkWKUQ63rHNJYF9kbWkSm7di37TAB6koFH82T-AV7D5UA6eu2U3gTx4IGWxp8oWhebBvtrt17AIpthfjjzquhvoisBMLSImetvOmpgaWBZYhUhAknrMKie9rNo8nZD9c2J6LuRmEyg9LYickd6QfqPUx2q8vuq_81w0bMT47VCvaqiqPpwJkA03cBru4r-gJGZy40-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: طبق گزارش پنتاگون، ۲۴ پهپاد ۳۰ میلیون دلاری MQ-9 در جنگ هدف قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/456244" target="_blank">📅 18:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469a082088.mp4?token=T5dHRs4IvXz2JGctNBWANAOrc_JuDkdQs6QuiH5STTtJH5FKT5bbj5L5cBem9n1RyLAjTk7493H8SRErhkC7RMmFZg0ZE0-8Huo2N_wjjoP6Xynq2_cJdaKmLT2eF-BdnUrKpLziyv1QTjiszz_qpkax1uciRqrIuMzxC8fnnB9twK7RsyjC8mIg_EN9DAJn0nFp_BSPVrRIfbUeGouECGmT_mfG5ARXbQ9-f8iZa0fWzDgDgmrmpgBSwC13h1cf_GSNNbWQDByzBL5KbnUNcy_F_YfQcPk4nqJTqTI23fkz6_Iyycs2feIpg54FfWDneN2t5idYD_lVDYGsCe8guA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469a082088.mp4?token=T5dHRs4IvXz2JGctNBWANAOrc_JuDkdQs6QuiH5STTtJH5FKT5bbj5L5cBem9n1RyLAjTk7493H8SRErhkC7RMmFZg0ZE0-8Huo2N_wjjoP6Xynq2_cJdaKmLT2eF-BdnUrKpLziyv1QTjiszz_qpkax1uciRqrIuMzxC8fnnB9twK7RsyjC8mIg_EN9DAJn0nFp_BSPVrRIfbUeGouECGmT_mfG5ARXbQ9-f8iZa0fWzDgDgmrmpgBSwC13h1cf_GSNNbWQDByzBL5KbnUNcy_F_YfQcPk4nqJTqTI23fkz6_Iyycs2feIpg54FfWDneN2t5idYD_lVDYGsCe8guA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس پدافند هوایی سپاه: طبق گزارش پنتاگون، ۲۴ پهپاد ۳۰ میلیون دلاری MQ-9 در جنگ هدف قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/456243" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cun1R5W9DVQkP24E7NAPUfqitzgMuEryMr_5mAdwxmohBruWjfYeVOLN9tHSREJi47G7u6q-v1iP010-6TrLYXAjrkvkrZlUBgiqG4btQhck5psEZ3kBMlZyiXXHiO4Z5OqVN8Bv5eEHiqAQI6ZegTLAx60th_oi4vQz5YIfSrn5e6fiTHu6B8KWCkWScO9Lp8G47mcLHbSz9pJN1t5I4aILUEmODsFHLjfJezCXdYt7k45n0ZMRzJKJTTmwyyWRB_iOfwxudJly3fZHcQuvkklLDSQ_9xVzJARF-h9EG9VVhVVDm34WRr198_SUWikqN6csTfaI_XflALVrUzpnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال و معمای وام ۴ میلیون دلاری
🔹
‼️
خبرنگار فارس به سندی درباره یکی از پرداخت‌های هلدینگ خلیج فارس به باشگاه استقلال دست یافته که در آن هلدینگ خلیج فارس در مرداد سال گذشته یک تسهیلات ارزی ۴ میلیون دلاری به باشگاه استقلال پرداخت کرده است که با صورت‌های مالی ۶ ماهه اخیر این باشگاه همخوانی روشنی ندارد و ابهاماتی جدی در این زمینه به وجود آورده است.
⏺
مطابق این سند، هیأت‌مدیره صنایع پتروشیمی خلیج فارس در تاریخ ۱۴ مرداد ۱۴۰۴ مصوب کرده است که ۴ میلیون دلار تسهیلات ارزی با کارمزد سالانه ۸ درصد از طریق شرکت تجارت صنعت پتروشیمی خلیج فارس در اختیار باشگاه استقلال قرار گیرد. نامه مربوط به اجرای این مصوبه در تاریخ ۲۵ مرداد برای مدیرعامل تجارت صنعت ارسال شده و طبق اطلاعات رسیده به خبرنگار فارس، این مبلغ در همان مقطع در اختیار باشگاه استقلال قرار گرفته است.
⏺
در متن نامه نکات مهمی وجود دارد از جمله اینکه این ۴ میلیون دلار نه کمک بلاعوض بوده و نه بخشی از قرارداد اسپانسری استقلال بلکه هلدینگ صراحتاً از عبارت «تسهیلات ارزی» استفاده کرده و برای آن کارمزد سالانه در نظر گرفته و استقلال را مکلف کرده اصل تسهیلات به همراه کارمزد آن را تا پایان سال ۱۴۰۴ بازپرداخت کند.
🖥
ادامه مطلب
را در سایت فارس بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/456242" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42121d529.mp4?token=oOjmEAH9s9chb5mtDMk8gt5DmRMpwBPspW0v8-hgnYYLYOW3-DGhzj7ukWslX1IRvj6QVJs9R_h1t8aGodTJKqcHinZoymuK-qGqFNe9UgtrTOxSP4o1ZlBuXa0zd30C6M_Gy6S1Fb3jUkwGFFXqGEPFuxkKZSVb0QnOpneHnNs5m3NDpMV1VnWicDUQ9qMFR1RvDKznOHaatuuKvSEIcxcCitlIRwepnkHoz_0M8w3CVt-sa3Woz3OFvk7Bh_rn4yIUxOTrIPhNtX-WA2iJ6aok8LQoHFEiRbepdRD7FNGJ8VPnoAZZBb1tVYAdNUWh0MTzfdvPkW_4AqOP2d4YYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42121d529.mp4?token=oOjmEAH9s9chb5mtDMk8gt5DmRMpwBPspW0v8-hgnYYLYOW3-DGhzj7ukWslX1IRvj6QVJs9R_h1t8aGodTJKqcHinZoymuK-qGqFNe9UgtrTOxSP4o1ZlBuXa0zd30C6M_Gy6S1Fb3jUkwGFFXqGEPFuxkKZSVb0QnOpneHnNs5m3NDpMV1VnWicDUQ9qMFR1RvDKznOHaatuuKvSEIcxcCitlIRwepnkHoz_0M8w3CVt-sa3Woz3OFvk7Bh_rn4yIUxOTrIPhNtX-WA2iJ6aok8LQoHFEiRbepdRD7FNGJ8VPnoAZZBb1tVYAdNUWh0MTzfdvPkW_4AqOP2d4YYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خیل عاشقان رهبر شهید انقلاب در جوار مزار نورانی ایشان در رواق دارالذکر حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/456241" target="_blank">📅 18:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f63d681d6.mp4?token=tsJUM07CEqhzuDw6UXH4DP0xPa85QtLRfvImHwT-95A5cJAtsEwtNEMutNLCT8hWIxVROZd4zMZO0IZ7lb8r8CZViZ4g1x4Z6f5okD-1O-ABsZK8tLFKsvT3iw0rKzZWZbtnUAuw42vgnedA2F5AhEvDb9815FzMshHiZtzzIA_NFU23ijaICs5aGp6ZoJquUBqkVzdhitL_CMOV5-Rw9JaqPXsSppXqJomdu9IM05LE2Cef1WOMzO4Ddby6f-Nfj81mOqV4qiAq1EqdcXWUT1N7BN7URJykQpUoTSMQEhUtlUnPgKE4e-V9b9SJhgw-fxKCK10GvgZ3qByqZaO-IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f63d681d6.mp4?token=tsJUM07CEqhzuDw6UXH4DP0xPa85QtLRfvImHwT-95A5cJAtsEwtNEMutNLCT8hWIxVROZd4zMZO0IZ7lb8r8CZViZ4g1x4Z6f5okD-1O-ABsZK8tLFKsvT3iw0rKzZWZbtnUAuw42vgnedA2F5AhEvDb9815FzMshHiZtzzIA_NFU23ijaICs5aGp6ZoJquUBqkVzdhitL_CMOV5-Rw9JaqPXsSppXqJomdu9IM05LE2Cef1WOMzO4Ddby6f-Nfj81mOqV4qiAq1EqdcXWUT1N7BN7URJykQpUoTSMQEhUtlUnPgKE4e-V9b9SJhgw-fxKCK10GvgZ3qByqZaO-IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت ورزشگاه سردار آزادگان کمتر از ۹۰ دقیقه مانده به اولین بازی فصل پرسپولیس
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/456240" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNkgbwloqmrxxwMbL6IbI2gwc2j0_8HRL1_MFnZ6_abByLkAywkUU1oNHTqaBPiFOFBr9MpVjkvyEC3I_zEaO2tovjFn_Oqb2tI1wt_jb7bDtXADUftG99MzTWcX68DOKtSzKBoEqC-VTSLNw_gzNETEoXBP7jJFddZdTYJbUBG6VS5kBeSFN43n3wv1N8Jm0ZKG_hr0WiiTJMq2WWuw2sa-AnGvsMVTEahxiB8jLkHLDH2Ys_dGSq8joLP49WnqR23n4rMfswSaAKvtxzg7fOg_RMV1d9xfpbXhSs7Um6RR0PgzsEHhhpr0aoYyNN0AAtYCVj6I2JBVbpchofdh7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تدارک اردوغان برای نماز در مسجد اموی دمشق
🔹
سفیر ترکیه در سوریه از احتمال سفر اردوغان به دمشق تا پیش از پایان سال جاری میلادی خبر داد و گفت: امیدوارم اردوغان در کنار احمد الشرع در مسجد اموی حضور پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/456239" target="_blank">📅 18:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456236">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXD0kknHgJ0kZPfTkuqXPn55Bn3u4oNSYfxhvnSjVG0sl77qBddTZL5jA2giyKUYhzWwUqxfTYAugoGVoo6x6bS4TXk1DFOIyVF0qJezgNckNBcvq5zxmqCISu8Yxi6e6i5eiyeHosGuOQ-6cliA_D1MN8FF1c1fSrfTHWS4a-XLgpd2W1EqDUj50ZgyEh0dEX9IkJnj8jL-k-cmtjJOxt5iAGX_Dldwj5lFahaO8jT-qfavpZ7KJDMKrLdkjNnygcf3Z9Op-jGujaz21daHNmotWjq4paWdDc2GOhSXfJEtU8Uutw1oMMY6vwf6uRazdUUmvRfjTJYn7wORU-BM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwWhAIb0ksUSztkFg_8lmoVVq6YxxuXhZaSz1LzZVtLYgYWHurtjAAwEvzyyOUELWHxQVwgUQ0cvI91xdTp64-Dxkfc9d92v2Xw4CxNWwFo9Eawbi9Xj8xIrBLD_JGN4TTjIKaWzGKvQrgJCfLXb_SOyLnvIrUVsQFVsRFoZJa2bRUfOB3tJJUWpuVqqyJfXtPrfU-Lj_AYZCXfWo4i4ZP787z43jPJ8x0JOxQNs7CEXTdk_-eOEAw2k21lYjSZmBvfTnXDMm_4SHWB0SoqpVa_All9YsWduWpOoPEItamp9LY4e2KsHrIwwLJmm-QPqvfNHWye2jwk1vqLE0dJBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btGuAj8XOROfuEZev_Q8WwcnXxAzq7kAvQvdzvFqI8kjS6Yn1sZqi031Y_sQZ58PRCh_a_-iLna9ZA2ll9FjFpKm_1-rCHJDlXRklLe10-j1HoVZOUibOtUSZjrgdzVYMOjettLExTo4upfKweKjHtjMhm2ZMbOxcEpcWBbHcHM5cAzmNAXMjsFPpxSTEKt6ZlRRL3wyKgc_BIIbHKEztXjrr9GR059j2lPxxb_ZS5tIN2WGMb-CRpS89Ru0f1SNgI5c-GzdppIknpETUYRWpkdtynWdcNlb2-Sc9P1CSEYjTifKIPhZR8c6aLgWcNWBs96EXkMqLRZzBo_Tmx6POw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست مشترک سران قوا در نهاد ریاست‌جمهوری برگزار شد
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/456236" target="_blank">📅 18:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456235">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etZCOINGSfsHQaP37piguIxvSUU5wz1RjXK_VvIEbbjeowg91b169DmY20511Bx_2L_FSeU2QvUWHKD2fxPqpFSpzc-V8OKDqbZtHA-0IIvSZDvITV18bSPtLtAykEKzlxcJfTbbuzwmlRenUsF84LbDv8qsO6F8a1O_nRuUDH3P9_7XDKk4D8lfeP8v5mhhwnYFojzeetJCMNegUEoAfnj9uqBT0iAeH1XZxWNlc_NtNjT9VZtELSHOqFhXQfC2uqQWD9q82Xm0HQGmIbgd9trdOO6U11mE7Mh8jZBck-OEr--kBRzHucJD5XuBb3iov7vM9V7huZdh8Qv9akvl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورفی: جنگ با ایران از اول قابل پیروزی نبود، ترامپ فاجعه آفرید
🔹
سناتور آمریکایی که بارها درباره پیامدهای جنگ ایالات متحده علیه ایران هشدار داده، این جنگ را «بزرگ‌ترین فاجعه سیاست خارجی آمریکا از زمان جنگ عراق» توصیف کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/456235" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456234">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUdg3LoJBLNWcYfCX14QEHs6evnvf7fJiCMsDA4ZXGYOCmQnQQfIbBaxWpZUIh9bBz7ungWSXd--OqBqDQiP-hUw5bQxY2PDhoWA5S0mQaR7kivakCS4UR2p0JJa30EllafoBfsCm9yLE4URhSFz4s_WTWI09UCli2VIifxG3a_oBeVLhOSl7d7zA54F15-8ZpplX9rfB4qxuZKzDga5NQQAdXvspg9geMxINl6FmYATb_5I2u7ktz8RuCKnYu8xoKHZMNrMXhXmbBhjEb6ROwxg7lP42H-0kKvnJEeNofXCdpfiW6AIuIqEp4cip55J-IsBKSip5psyCBIIJhnx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تهدید صریح وزیر جنگ آمریکا: حملهٔ نظامی به کوبا روی میز است
🔹
پیت هگزث: اگر کوبا مطابق با ارادهٔ آمریکا پیش نرود، از گزینهٔ نظامی علیه این کشور استفاده خواهیم کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/456234" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456233">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BehJFwz-JROO-yF7X4Lktt_zUyJuqksCrcvZbQX4dORXid-4sXUQucGPQD4eUvu76dsRjhxjVQg8Awk_Hev3KSeX5Q9RN7mTYmnyRTx9gH631GYDIhKsxlZZ7hYpYvEDV2r6Uadu7Wmj-oov0XD54Ev77XxZNr5f0tn2zDLLnUO1eGW1ksK0SjocZjPDIDs0fWvxxc7VfLH8eJTsNYr1AO4qROE-UimNZD-V1r0UuZT8U2favRvVTDFMCCJdgMhPDTEIt8YMUyB4nxeZMfN3vfuISA5FxhLvvN_4KnSffvigem04-cT5bbVh_nFAACjmpwWppJxxhrHRQe93hrZPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام فارس TV مسدود شد
🔹
صفحه اینستاگرام فارس تی‌وی که به تازگی راه‌اندازی شده بود با ۳۸۰ هزار دنبال‌کننده توسط متا مسدود شد.
🔸
صفحه جدید
به نشانی
instagram.com/tv.farsna
را دنبال و به دوستان خود معرفی کنید.
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/456233" target="_blank">📅 18:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456232">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8175b9c63.mp4?token=Wd86GmYuALK-aQ21R7kEVUdKeAgjayhqoY1lWmVUqN096d22mWR_jqiemgMYGGpxbgl-GnF-Q_fTOiKtzaMKuKfaihkxI0rTozq8a05UFrdt8dGsxz2IXqNHmVhio2PByD6wZyhk8NSBLZGmCeYy8fgQSph80VYEjm6ebZdBEuOqgqG25tvbBQIy8TETtPuekU0CN_qGyCNU59qvPdZbVqcw471fdtJn0n3UT3M7ytmENuF9cm9uoqt-QIGcRGUkcqzDtCGNzsq0yiFIRU8pxY-706P_R_iHuoYBSEsdVE5DzLrRx3AMJEtlpGI4c_6s6_aHFiqYdKXGKurJ-U0TlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8175b9c63.mp4?token=Wd86GmYuALK-aQ21R7kEVUdKeAgjayhqoY1lWmVUqN096d22mWR_jqiemgMYGGpxbgl-GnF-Q_fTOiKtzaMKuKfaihkxI0rTozq8a05UFrdt8dGsxz2IXqNHmVhio2PByD6wZyhk8NSBLZGmCeYy8fgQSph80VYEjm6ebZdBEuOqgqG25tvbBQIy8TETtPuekU0CN_qGyCNU59qvPdZbVqcw471fdtJn0n3UT3M7ytmENuF9cm9uoqt-QIGcRGUkcqzDtCGNzsq0yiFIRU8pxY-706P_R_iHuoYBSEsdVE5DzLrRx3AMJEtlpGI4c_6s6_aHFiqYdKXGKurJ-U0TlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شبانۀ پلنگ نر در منطقۀ شکارممنوع کوه سفید دماوند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/456232" target="_blank">📅 17:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456231">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prmLQ43tENj6Y0vZMHp-O-FlHhqSYp5psk9AWtNdYTlL-pKiKrpuJdllPzt9-IB9T396TrM3jpmhn_SrwWRHQtabnlxuVzQjGaL9neJh4yOVfynR4e-iErzu-bsKB-3ohAc3pdnxpaN_klcKpiWl1CFBKytFS4BIfqVnBSFqffOZi9CQZdqlNrHNDnNXh8mKg6yzal6Q6Lb37ZHH3LCpFDy240C-l1vv3YnYLLsypmR-lAfazSJpffbWHtZsrzqAJmos86hPl9cVT8OMjfAu3l3Z3IryWVZmgtsYDHzAQAu4Fy5zmX3p3b7uW7TgLzuncIe8iMGR7cH8T9ldVcU5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت جانشین فرمانده سپاه اصفهان از یک پیشرفت در جنگ رمضان
🔹
سردار فتحیان: مرکزی که در جنگ ۱۲ روزه با ۴۰ شهید، بیشترین هدف حملات قرار گرفته بود، در جنگ رمضان با وجود ۱۲۰ بار اصابت، حتی یک شهید نداد.
🔹
استفاده از تجربۀ به‌دست‌آمده از روش‌های حملۀ دشمن در جنگ ۱۲ روزه باعث افزایش موفقیت و کاهش آسیب‌ها در جنگ رمضان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/456231" target="_blank">📅 17:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456230">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-gsMVfn2nt3GjYkd9VjNFcySrQay0w-RxN49Yg8UqJqsfRQIAZhv-Ol-d7BARcLnlkLhyqgNwA0g-x-BPKoKXugYqqtT9pt4Wcnq_9KXbpmdE-T0QnRyOsIlt7wLmD7sZOhiFGaMKGXrI0ruR-cYVmGsyuON4Tb33pUWccRdNQ9HCOFFTMUEPHK6B9THDnh1kVWhixjBWYSW3XK-tuhD2fuRXofP669Sju3zP-jCDjycRoQjJNKOvUYJFCNSwz-z7J5YUL_33yDU8LlyTN6ej60bgceGfeFrPlr_mIl9yG8ngVpV04DWlLxDwwAc2VfsaloL6fQKr4Nd7ubD7VSjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پزشک، ۱۵ هزار جنین را نجات داد
🔹
سازمان بسیج جامعه پزشکی طی ۳ سال گذشته، مجموعه‌ای از برنامه‌های درمانی، جهادی و امدادی را در مناطق کم‌برخوردار و همچنین در جریان بحران‌ها و حوادث اجرا کرده است؛ از ارائۀ حدود ۹ میلیون خدمت به بیش از ۴ میلیون و ۶۰۰ هزار نفر در مناطق محروم تا فعالیت تیم‌های واکنش سریع سلامت و خدمت‌رسانی به بیش از یک میلیون زائر اربعین.
🔹
یکی از طرح‌های این مجموعه با ارائۀ مشاوره و حمایت از خانواده‌ها، تاکنون ۲۷ هزار مادر را از تصمیم به سقط منصرف کرده و به تولد بیش از ۱۵ هزار فرزند منجر شده است.
🔗
ماجرای نجات ۱۵ هزار جنین را
اینجا
از زبان رئیس سازمان بسیج جامعه پزشکی بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/456230" target="_blank">📅 17:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456229">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57e086683.mp4?token=WjtfnsyukOmBw95O4JI4JXMJBU5zsBireXDl5xzMaL-m3-3tqJcZSY6s4CaFpaHPem4KWfhggKPszPiCpS4zk_jSsQkxOcvP_n5sjwJ_Q4QT5BhhBU70zJ6ar04Ce7MCxQS148rfooNCuHfmVg_7Z1QeNgiAXV-ZnaYvvJbqYKQh7En4fB5SR9r3nkphcKvs93im8CMua6nfiEkwU4WoRhOqW2kZ6sdxsxRGQsKZkIFoEMkHZzBlzoVDhbCOAO0btNbK0cFZwYAEI6xmnaVCmFOgtr4lT7uhkzJm3D5cSwnpyLurpOaZRvALbmJu3p9g38CwxHnhY-upgW2bhcAZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57e086683.mp4?token=WjtfnsyukOmBw95O4JI4JXMJBU5zsBireXDl5xzMaL-m3-3tqJcZSY6s4CaFpaHPem4KWfhggKPszPiCpS4zk_jSsQkxOcvP_n5sjwJ_Q4QT5BhhBU70zJ6ar04Ce7MCxQS148rfooNCuHfmVg_7Z1QeNgiAXV-ZnaYvvJbqYKQh7En4fB5SR9r3nkphcKvs93im8CMua6nfiEkwU4WoRhOqW2kZ6sdxsxRGQsKZkIFoEMkHZzBlzoVDhbCOAO0btNbK0cFZwYAEI6xmnaVCmFOgtr4lT7uhkzJm3D5cSwnpyLurpOaZRvALbmJu3p9g38CwxHnhY-upgW2bhcAZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ جان‌فدایان ایران به رؤیابافی ترامپ دربارۀ تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/456229" target="_blank">📅 17:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456228">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پیش‌فروش بلیت‌ قطارهای مسافری برای شهریورماه از روز دوشنبه آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/456228" target="_blank">📅 17:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456227">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLDMYMbI68bcH2jlno8wHp5G2W2C0wWlfrD7SMoKn_fUNIlxNIAp4_Pl0hnLaIjEz9GeY191T6_GAW5k4rsZshahnDB5GwxeKN7z83tCOehqN2Mo55mMtA5T4QobMvV5uj5kaOt3JNzmCtMZ4OczMg3GyvLYVn3kLLDKWyIOzHuzJ4dU05fqX_OrOfkkFyGYwjw70rD6WBFnhij1FCKzJu9qT9JcT9XYQx4lAUk6uaqm_YPCb_VF1ppZCEbPWeb30eWFrhe0YmKqA-xQcUHE2B57Z9WS8gFWQ3J-tCnYx_mDhhXsbLrnwfkdU6cJl0iipsRiJk9OURc6ivK4RcQ-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ الکترونیکی کتاب‌های درسی جدید منتشر شد
🔹
نسخۀ الکترونیکی کتاب‌های درسی سال تحصیلی ۱۴۰۵-۱۴۰۶ در پایگاه
chap.sch.ir
بارگذاری شد و دانش‌آموزان، معلمان و خانواده‌ها می‌توانند این کتاب‌ها را رایگان دریافت کنند.
🔹
درحال حاضر نسخۀ کتاب‌های دوره ابتدایی و متوسطۀ اول در دسترس است و کتاب‌های دورۀ متوسطۀ دوم نیز تا پایان مردادماه بارگذاری خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/456227" target="_blank">📅 17:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456226">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d602e8c27.mp4?token=bwREqstk3FxeY5FmiQaE9yrfehKxR6SY4tHesx-FQk0BOFM_tfFY-z6Wgr3SvxI4HsjwJ9D9bBMD3_md9VYtMamICAP3dSPujKCPzygmAnRP2mCB_sWwsuxmaBPLzDL_7__kO2RFgfSV7vmbYqzK3JiEXTYfZzmykyZX7KhyvvHJ0VS1PGms6mJl7agHYHlvYJARnJKAaAqxdbOZRnUmwpIdwGKc3Xp47PepwpHXq6gM8vTmHZL6HxdeiY-ZpzjqZOPpvTr0BOUT2QNBJsBqEKPVX66TcKGV9Z9QalDLD7Ge95VkjVJI8FwT2aDLu-fdu0aVvktBzOLDA_7pdAld6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d602e8c27.mp4?token=bwREqstk3FxeY5FmiQaE9yrfehKxR6SY4tHesx-FQk0BOFM_tfFY-z6Wgr3SvxI4HsjwJ9D9bBMD3_md9VYtMamICAP3dSPujKCPzygmAnRP2mCB_sWwsuxmaBPLzDL_7__kO2RFgfSV7vmbYqzK3JiEXTYfZzmykyZX7KhyvvHJ0VS1PGms6mJl7agHYHlvYJARnJKAaAqxdbOZRnUmwpIdwGKc3Xp47PepwpHXq6gM8vTmHZL6HxdeiY-ZpzjqZOPpvTr0BOUT2QNBJsBqEKPVX66TcKGV9Z9QalDLD7Ge95VkjVJI8FwT2aDLu-fdu0aVvktBzOLDA_7pdAld6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی، وزیر سابق کار: می‌شود هم جنگید، هم اقتصاد را مدیریت کرد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/456226" target="_blank">📅 17:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456225">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAMudHY8DhKdNE0vsCFaZ4n5oYR94GGBzWurNzzDioxZd-Gqy2izKSoy5ZDU9xZ-Bpl9Fp-Z5IoseHrIF1WpBA9nP10utrX5PoZ7acdQu3Yoa7SWBDHTlreuvfYHwULBj4x-pQ5qAu2tSe4wir7bkgDape3Gtg-c65_quRAd7rxuTBeMWUeuuuWZhOynahnpdHeXPlMjdtWNKadCuVosfmuPg7jLcDcDoe6RBZA1iVBYohiEhpVspProFTplqVFhqNhPwpyk-MB6e3TdSW-99F-x-65iXqERZjV5rT4IYTOn24lED8zrK81CvbRuiwxz6TmfbpXHXaEt0Epu7kLMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
✔️
غلامرضا محمدی سرمربی اسبق تیم ملی کشتی آزاد به‌عنوان سرمربی تیم کشتی آزاد استقلال انتخاب شد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/456225" target="_blank">📅 17:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456224">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b339ff2875.mp4?token=VBEcmY3hNhM3VmvETPoZNQBR6Frq6ufprxVHt-lGWAT8dBaMDisUt2D0IoTTJX3rUtEqBbf5UPzOvEEBuzQSFJ8MDL_Ca9ga2zOkBq0jYmGnFIwtmjbJZET5XdHrZ-I-sHaujHaq5V9y0D4nrSnPF6F7nQ_3YkYXchGobqSudGsOGQ5_bv-hwmDs-KN7kVKifvKwdM_1vOMZUF5Zt9VE-Q9gYaVXrWKsUgJOtviqmGo-zMF_V4rq8xW0XqCDYSh_5exWny9NSNQTqV_iXPXfwhipuHQQBnKbISRDLkRfO1FVtMP0uJWAMFY8O9a_RO5Jl6oMLbs2IKaEDWkteRdqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b339ff2875.mp4?token=VBEcmY3hNhM3VmvETPoZNQBR6Frq6ufprxVHt-lGWAT8dBaMDisUt2D0IoTTJX3rUtEqBbf5UPzOvEEBuzQSFJ8MDL_Ca9ga2zOkBq0jYmGnFIwtmjbJZET5XdHrZ-I-sHaujHaq5V9y0D4nrSnPF6F7nQ_3YkYXchGobqSudGsOGQ5_bv-hwmDs-KN7kVKifvKwdM_1vOMZUF5Zt9VE-Q9gYaVXrWKsUgJOtviqmGo-zMF_V4rq8xW0XqCDYSh_5exWny9NSNQTqV_iXPXfwhipuHQQBnKbISRDLkRfO1FVtMP0uJWAMFY8O9a_RO5Jl6oMLbs2IKaEDWkteRdqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست قاچاقچی بنزین رو شد
🔹
دادستان هرمزگان در جریان بررسی صف‌های بنزین، متوجه سوخت‌گیری‌های متعدد یک خودرو شد و تخلف را شناسایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/456224" target="_blank">📅 16:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456223">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
در حملهٔ بامداد امروز رژیم صهیونیستی به شهرک «انصار» در جنوب لبنان یک مادر و تمام فرزندانش به شهادت رسیدند.  @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/456223" target="_blank">📅 16:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
تیراندازی در دانشگاه ایالتی ویرجینیای آمریکا و اعلام وضعیت امنیتی
🔹
تیراندازی در دانشگاه ایالتی ویرجینیا که چند مظنون در آن دخیل بودند، به زخمی‌شدن چند نفر و اعمال محدودیت‌های امنیتی در محوطهٔ دانشگاه منجر شد.
🔹
این تیراندازی در نزدیکی ساختمان‌های Quad Annex دانشگاه رخ داد و پلیس دانشگاه و منطقه در حال تحقیق دربارهٔ آن هستند. هنوز جزئیاتی دربارهٔ انگیزه عاملان و بازداشت‌شدن یا نشدن آن‌ها منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/456222" target="_blank">📅 16:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456221">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d794581db4.mp4?token=dkkCbZWbVCMY6d-9Hw8oqbIl7vuKrJtowDBCoeOKsHNeUjXka8Wt3emaTp4oD6GmkpvNxtr1HUuGtdB-ZE-7UcFzz4XzECike7xRz1R903nu3p2R8uuuEK3uRpF66Ys8rOIsGCzfeXzJUXK1pTXE0XzaqZcXSsQ_X3AQuPyIc4AhyKXFcpFkeoyv6zU93xOsyEsh6XnfREGuh04wnyyZ5bZQBouxZJwMVgJllAoCozgHTauBAloZOqTmQ1tW1jS7OEN4W6dBGhH5IFpoEEDZHUo4aQCJrkpe6Ul8GAh-9bVAdRSnUcLe_xSqHR0pqmpwURf1xLTyUhObu0D-zskSOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d794581db4.mp4?token=dkkCbZWbVCMY6d-9Hw8oqbIl7vuKrJtowDBCoeOKsHNeUjXka8Wt3emaTp4oD6GmkpvNxtr1HUuGtdB-ZE-7UcFzz4XzECike7xRz1R903nu3p2R8uuuEK3uRpF66Ys8rOIsGCzfeXzJUXK1pTXE0XzaqZcXSsQ_X3AQuPyIc4AhyKXFcpFkeoyv6zU93xOsyEsh6XnfREGuh04wnyyZ5bZQBouxZJwMVgJllAoCozgHTauBAloZOqTmQ1tW1jS7OEN4W6dBGhH5IFpoEEDZHUo4aQCJrkpe6Ul8GAh-9bVAdRSnUcLe_xSqHR0pqmpwURf1xLTyUhObu0D-zskSOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت‌پردۀ افزایش قبض‌های آب
🔹
شرکت آب‌وفاضلاب هرگونه افزایش قیمت خارج از چارچوب تعرفه‌های مصوب را رد می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/456221" target="_blank">📅 16:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456220">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERGTTp2AyHqO3OIEfgi3c1bo79Q8edha9eWc3Bs3JLrBis8zCTHEm-eKwnZ1tMOEIX7RxR7leGLuIxLGX-kBOeyD7RglssVDrPwFvqs3jqx-Pn0eWp1lTZwX6ICfJNVmy-fVmSWEv-OHrC7Q0q08GgzyZ56GcDxvmiKMqI0T85qlSlDNrwghNfPJgWLdS55g074B1ewGQNS0rBjzNMZPU7K7HD9j9BAvcrFdV_vabmuIMlDEdedAubZ1VXM4b5wegm7Tn8L1UdUmuEVQDdlcKi0xvQ-JnZ5fW3vHFmC8mALa1-uojmKBBwjCAzKTtOYtj-yYa0q1AXnglCjjjX1ocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله لبنان: دشمن اسرائیلی بداند تلاش‌هایش برای تحمیل یک وضعیت جدید با پاسخی متناسب مواجه خواهد شد
🔹
حزب‌الله در بیانیه‌ای اعلام کرد: دشمن صهیونیستی غیرنظامیان بی‌گناه در جنوب لبنان را هدف قرار داد و با بمباران یک منزل در حومه شهر انصار و یک ساختمان در دیر الزهرانی، باعث شهادت ۱۱ نفر از جمله کودکان و زنان شد و ۱۲ نفر نیز مجروح شدند.
🔹
این تجاوز و نقض حاکمیت لبنان، مسئولیت آن بر عهده دولت اسرائیل و ایالات متحده است که از آن حمایت و پشتیبانی می‌کند.
🔹
در مقابل، دولت لبنان باید به دنبال راه‌هایی برای توقف این تجاوز باشد و نباید به ادامه مسیر مذاکرات مستقیم تحقیرآمیز و ارائه هدایای رایگان به دشمن ادامه دهد.
🔹
اکنون زمان آن است که دولت از ادامهٔ مذاکراتی که آمریکا تحمیل می‌کند دست بردارد و بداند که اتکا به تضمین‌ها و میانجی‌گری آمریکایی تلاشی بی‌نتیجه است، زیرا آمریکا شریک اسرائیل در جنایات و کشتارها علیه لبنان است.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/456220" target="_blank">📅 16:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456219">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c8fdcaf5.mp4?token=j2XoFK3v4qDEpZs4V_RpjUPiuyCwhX_lw1i3sm-mU55IGr5bdNF3BIGs68UuRg55TtvCtQxw-SIlYTmXQZR9Lp3Fh62rZZ53MofEMwziOx9iXIuMiS7QOAukAkMlJ-wjkjsCjFqQ-Ct8U7la6F639hX6MFNJ1V2RNOXyfnPC4BCZxIML4yoqOAC6LqxxfHvw3ouTuknaQSV9lIr1Rykay3Hs2XbhEKF54nQBDT5NEmhwCEPul_MzLYLUSjVYTK7eY7t3GoybZLoBD_ViHk-cLg1b4BRHWsKdok2zUOm3WL3L1dFalEQcWNITpLgRnjK13gEFFf3eU1O7hb1U1cTxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c8fdcaf5.mp4?token=j2XoFK3v4qDEpZs4V_RpjUPiuyCwhX_lw1i3sm-mU55IGr5bdNF3BIGs68UuRg55TtvCtQxw-SIlYTmXQZR9Lp3Fh62rZZ53MofEMwziOx9iXIuMiS7QOAukAkMlJ-wjkjsCjFqQ-Ct8U7la6F639hX6MFNJ1V2RNOXyfnPC4BCZxIML4yoqOAC6LqxxfHvw3ouTuknaQSV9lIr1Rykay3Hs2XbhEKF54nQBDT5NEmhwCEPul_MzLYLUSjVYTK7eY7t3GoybZLoBD_ViHk-cLg1b4BRHWsKdok2zUOm3WL3L1dFalEQcWNITpLgRnjK13gEFFf3eU1O7hb1U1cTxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوضاع قیمت‌ها در بازار کالاهای اساسی چطور است
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/456219" target="_blank">📅 16:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456217">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKDFiRzluWjuPDJ3s7X1K9-vypi1dcc8poFrFiBWUDZQGjchTMzqtg61RkU5gZXXln733ay_E6UiQF3jSs6Jkr6lmohFt9FicUNGhaRv_ZlvwE4VWZSHqzvhYCQc5g9l67g9dOwjR8ZxGeNDN4HuqT3IEX0lxAyq7xW1ZW1ks4dZ-PNWNud5yHFFm0HaDprsH3xW48rNioEggmEcBSqTbC__kQl70XElegeI-tZUq9iI__PZYoWf0H1nQt7vTeXJ1hmbrmYY98_jDVo9ikSpTYXb-YMa9C7a8MWCRd_Jwaj8oUjlIVXuYgy-PzY0LZ2RPZ1sEU-ZgPNsjq3-jweOsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما راوی محله‌تان باشید
🔹
خبرگزاری فارس در نظر دارد با راه‌اندازی یک صفحه اختصاصی برای هر محله پایتخت، پوشش اخبار و پیگیری مطالبات مردمی را به خود شما بسپارد.
🔹
اگر دغدغه محله‌تان را دارید و می‌خواهید صدای رسای هم‌محله‌ای‌های خود باشید، جای شما در تحریریه خبرگزاری فارس استان تهران خالی است.
🔹
علاقه‌مندان و افراد مستعد می‌توانند از طریق
این فرم
در طرح ثبت‌نام کنند.
@TehranFarsnews
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/456217" target="_blank">📅 15:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456216">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/679ed02728.mp4?token=q1iNXZ3ruy3cvrMv3Ha-8k3UX793JOqKn2Ecdqe20ECVsowGBwDJEp8XU8GZBe22uNxQujdB5KUtojls-RgcgVdgAen4ZuClTsPOG4sPITEKrgpgSZ-fBDnT4-GHpv4znt6pCNgXHNCJ7QfA2URK-qYfj-Yy3InQDORSyrZ-du1ZHD-P-xWl7Mxcbm1wfWAuAmvoMWIU2YwXMgUnWwKzrBstpH4eLPbc6YaX2WtFGl8y_f0PhYQC_VZx-pDZ2w5tz2tI0sQR__2LEgjRqgVeFrWafe78n__pxNWZwBHkBA-yFnst2UgaUPQeDMRNnBsrPCeOmLnwD3tyW3OR33aP-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/679ed02728.mp4?token=q1iNXZ3ruy3cvrMv3Ha-8k3UX793JOqKn2Ecdqe20ECVsowGBwDJEp8XU8GZBe22uNxQujdB5KUtojls-RgcgVdgAen4ZuClTsPOG4sPITEKrgpgSZ-fBDnT4-GHpv4znt6pCNgXHNCJ7QfA2URK-qYfj-Yy3InQDORSyrZ-du1ZHD-P-xWl7Mxcbm1wfWAuAmvoMWIU2YwXMgUnWwKzrBstpH4eLPbc6YaX2WtFGl8y_f0PhYQC_VZx-pDZ2w5tz2tI0sQR__2LEgjRqgVeFrWafe78n__pxNWZwBHkBA-yFnst2UgaUPQeDMRNnBsrPCeOmLnwD3tyW3OR33aP-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب اقتدار پدافندی
ایران
🔹
ارتش آمریکا در جریان جنگ با ایران، نزدیک به ۲۵ درصد از پهپادهای «ام کیو- ۹ ریپرِ» خود را از دست داده که هزینۀ هر فروند آنها بین ۳۰ تا ۵۰ میلیون دلار برآورد می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/456216" target="_blank">📅 15:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e954320d.mp4?token=gTNgViCw8xQoe4rLiagCwXUPZbFz2rD-AI9fIXtFrCbGJiHugZWijEBpjHX6s6WQVf2buBgg7EqZGCeG3OOxmRGYvLy6HnvbAx5JA0tsToMivHzyQbpEYdGAeutZU_VGeFX-qoxkn1vfXPRUC7Iq74cR3spD3gz13vpO-a_B2Mj6EUh5S36AHqFIT7i4Gy12U-2-G6RvreEuaCKLaRzI0rS9Mp3cXuZssGw2A2gQDxR700Hk80uHCra9fbZ6PRM-QL2jh6-t7DXolTMmaeyT8091XDtB6Bf-LaG4jVcj9Q-jkR1G8APLpPaWO61BGESPkUmhkjogT3F0pMyw-8GJLgbOWS29XVSzye2Q7vF-vKJtKXtcsFXNPXktuYlnMr0Q-jKItkWGbnVEj3an6nysHL-fvrfUhVoTug0ElIUiEBYGdvBN_4vCus-jwnUxoA0NW3aY9bIt-yAQqGLygjr3lJD_gi2k92ME7BCrx5SY6VTvyGXyOc9nEEXF5huNQHP4nFRw3gJSEVdFSl6joULM1KhVG9EWyrLLbOyaotoW6AlgP1AU21pW-FZHYWzTEiyJIMQ2UmTK3sKferiwVW4B_CoTovpxsMz5kflzZu45j9W0K92gdeDZQZOMuUHX2wH2Yy9-UK7fE_fFpABb86ynW1K7qSDgCr0D6522RQfs6sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e954320d.mp4?token=gTNgViCw8xQoe4rLiagCwXUPZbFz2rD-AI9fIXtFrCbGJiHugZWijEBpjHX6s6WQVf2buBgg7EqZGCeG3OOxmRGYvLy6HnvbAx5JA0tsToMivHzyQbpEYdGAeutZU_VGeFX-qoxkn1vfXPRUC7Iq74cR3spD3gz13vpO-a_B2Mj6EUh5S36AHqFIT7i4Gy12U-2-G6RvreEuaCKLaRzI0rS9Mp3cXuZssGw2A2gQDxR700Hk80uHCra9fbZ6PRM-QL2jh6-t7DXolTMmaeyT8091XDtB6Bf-LaG4jVcj9Q-jkR1G8APLpPaWO61BGESPkUmhkjogT3F0pMyw-8GJLgbOWS29XVSzye2Q7vF-vKJtKXtcsFXNPXktuYlnMr0Q-jKItkWGbnVEj3an6nysHL-fvrfUhVoTug0ElIUiEBYGdvBN_4vCus-jwnUxoA0NW3aY9bIt-yAQqGLygjr3lJD_gi2k92ME7BCrx5SY6VTvyGXyOc9nEEXF5huNQHP4nFRw3gJSEVdFSl6joULM1KhVG9EWyrLLbOyaotoW6AlgP1AU21pW-FZHYWzTEiyJIMQ2UmTK3sKferiwVW4B_CoTovpxsMz5kflzZu45j9W0K92gdeDZQZOMuUHX2wH2Yy9-UK7fE_fFpABb86ynW1K7qSDgCr0D6522RQfs6sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسکن واقعی باید چه ویژگی‌هایی داشته باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/456214" target="_blank">📅 15:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG5QCG9n1yGwg33Q0RmY-wDzmHEVNFJefe0676xHLI6TXM_y2Ye8a4Uudi79-y8NhL3mmqB3a2HnB2cDfDEs4emkCdO0VXW55IkpcCx4aQWzELuwiKARvfRLWTaNtfS62j9Q3HCShbHuUUnD71cKDdtkZEy9B1RyUvpNoAq4t8aHPaYgsEhgCeq1NDYdSZD3my2h0dtfbTveGN4ScIJAEkTdp8GHiKN21x5e18_Uus2R3K2IHo4vW1IXFeOkmKxAlXp1Cx_8NReMYlIjAhGVA5HsSLIVN471-bn-HvbY-omL17YHqaC4hcz7q7CwYACNrPRBLusNkDhGGoCnMN8ACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: متروی تهران تا پایان جنگ رایگان است
🔹
متروی تهران در حال حاضر رایگان است و شهردار تهران گفت که تا پایان جنگ هم مترو رایگان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/456213" target="_blank">📅 15:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حملهٔ توپخانه‌ای و راکتی ارتش سعودی به شمال یمن
🔹
منابع یمنی از حملات توپخانه‌ای ارتش سعودی به شهرستان «الظاهر» در استان صعده خبر دادند.
🔹
همزمان حملات راکتی از خاک عربستان به‌سمت منطقهٔ «بنی صیاح» در شهرستان مرزی «زارح» گزارش شده است. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456212" target="_blank">📅 15:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyDq1tEAdtgoutHWirq5Pijm7VjryTMclYgqyqHUx9Sgt6TMTgHiQPE-p-yN7jHoOTslueDWe7gHh7JnIb6a4rmL5yRAzvJKOoZHJw_kWOUqyWjp8RaGrzuKvJr9kvB8DaGCoGVBtzXB-TXkEmzSgIna0J1IJ1ZGCDH2x_TOnf4lO0nIVZS0OGBDTD-KmOCftMq_OiwvSW_d6O525y8QMmdePvj-YEOI49WMXi_rCPK127hb7hwiIlBNpNRnz-eqzI-08-e9CXoczAu06y2W1THLVOueWTQoxb3hr4g6ILwUHVnKcXHBHnIvL3Vcx_vL0t2I-kWDU_9j2lF5O7TDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سخنگوی ارتش: سرنوشت ۳ خلبان حاضر در عملیات ۱۱ اسفند ارتش هنوز مشخص نیست
🔹
پیگیری‌های ما ادامه دارد. طرف قطری اظهار بی‌اطلاعی کرده؛ از ارتش و دولت قطر می‌خواهیم که با مسئولیت‌پذیری بهتر برابر با کنوانسیون‌های بین‌المللی اقدام کنند. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/456210" target="_blank">📅 14:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoKCRFOPMslhp4-zqgcDni-KgfEcsn-tRbum9swLLWGANvFeUXghPGNRe9SKogGi6HOLDOpcDFeQ8WKsz3uGg9iATlJstNJhhNbVk7fHcC9Vd5pBG4lg6rZ86JFs1LSxJj6Cz3XJGhllRA8Zuaf779TJ4tNAqJwXMVTu2025Wq5UeOfZ8GVZgauMTqtubA-_7Ntrd8wtKfY_F-UpHGP0mOyC0tkavB5uu9Kq_Bd1bNHRPIZqop5gGOzE7_3PovrJ-71dVS0K4OPCiPk3NV9xpJh0_Wn3oWGYTp5nyOXxVMDM6sVuDWdCMD3thFsP4Hgk2s3T2GAqczpWrxMT4WO_Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته ویژه همراه اول برای قدردانی از مشترکان در ۳۲ سالگی
🔹
همراه اول به مناسبت سی‌ودومین سالروز ورود تلفن همراه به ایران، بسته ویژه ۳۲ گیگابایت اینترنت و ۳۲ ساعت مکالمه را با قیمت ۱۳۲ هزار تومان عرضه کرده است.
🔹
مشترکان تا ۳۰ مرداد ۱۴۰۵ می‌توانند این بسته را از طریق اپلیکیشن «همراه من» فعال کنند. باشگاه مشتریان همراه اول نیز برخی بسته‌های پرطرفدار را با یک‌پنجم امتیاز معمول ارائه می‌کند.
🔹
همراه اول اکنون ۵۴ درصد بازار مشترکان فعال، ۵۵ درصد بازار پهن‌باند سیار و ۶۷ درصد اشتراک‌های اینترنت اشیا کشور را در اختیار دارد و حدود ۴۵ هزار روستا به شبکه این اپراتور متصل هستند.
http://mci.ir/-48B5PW
@mcinews</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/456209" target="_blank">📅 14:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9w7ToIG5aXNt8SLPlfiQEAGmX-d4PGdP7jRA_WXwwMeyeo6msqwNn4ngze0kRHwyxoylaPIF2X1WPgIpYXwC1o3uRpfNBld8Gy6XhPl4Pr1gyTViZ7PP8nsbSemd4QnmfiAOXelYdx2K0JM2qFhJiAnkzzeHoqRkCq_qmcKakTOIxcg1e4gKzmq43FLxwmLqY0deO9HgM0zIduvC5HJR04d0ydRuOBwBSo555AOgU_Ge9f8NBtXp5dD4MBB8h5AKfdlah9VeAch8zphq28By8OglZhfwDiDOCGY5QXdRgLblRxPPaPEb9OxJrZVLsvCys5SD6wi46SDcBpDOS62Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬅️
برندگان طرح «سقای شهر» معرفی شدند
⬅️
برندگان طرح «سقای شهر» با برگزاری قرعه کشی انتخاب و معرفی شدند.
⬅️
به گزارش روابط عمومی بانک شهر، همزمان با آغاز ماه محرم، بانک شهر طرح «سقای شهر» را به اجرا درآورد. طرحی با محوریت مسئولیت اجتماعی که با هدف حمایت از زائران اربعین حسینی و تأمین آب آشامیدنی برای عزاداران در مسیر پیاده‌روی اربعین اجرا ‌شد.
⬅️
بر اساس این طرح که از ابتدای ماه محرم تا روز اربعین ادامه داشت، مشارکت‌کنندگان با افتتاح حساب ویژه «سقای شهر» و یا نگهداری موجودی در حساب خود، امتیاز دریافت می کردند. در نهایت این امتیازها به بطری‌های آب آشامیدنی تبدیل شد و توسط موکب بانک شهر در مسیر پیاده‌روی اربعین میان زائران توزیع شد.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/456208" target="_blank">📅 14:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/456207" target="_blank">📅 14:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">علت آلودگی نفتی سواحل قشم از زبان رئیس سازمان محیط‌زیست
🔹
آلودگی از ۳ روز پیش وارد سواحل قشم شده و مناطق سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام را درگیر کرده است. هم‌زمان عملیات مهار و پاک‌سازی با استفاده از شناور، تجهیزات تخصصی و بوم‌های حائل درحال…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/456206" target="_blank">📅 14:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGhkZC7GjD_QxJgp_GukSUG-wEt5wU3ycu3WeJ7gXdhGzcvD9l1--hRt2zIwcoO3_trbc_VHDHEft7_noe1GFhoA6xH-PCsp1sVC7Xs8HMuKuUEfO1tu_BHRPBHzPNdTqte1ESH5fnOD-gdfTJNZxBnVyNacqCyqnvkNG83ZppRnmo4TIxboKPgbseTYGhqWLLDm6Rgsus3idTLNwuKvZ-7583e8SQqydLm5_z-wcbRbGQu37EZeFLzxzDUEeHS4nwLGeqTi55ixopSm6z0Z_xWpJuHOroQlwB4U99SrxUntiDcaGSYzc3mmugugKmquNH0We9j1kiCCW6FAJJunEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان لیگ: استقلال باید میزبان دربی را اعلام کند
🔹
درباره اعلام مشهد، تبریز و یا اصفهان به عنوان گزینه‌های سازمان لیگ برای برگزاری دربی پایتخت که در هفته پنجم انجام می‌شود، باشگاه استقلال تصمیم‌گیرنده است و باید هرچه سریع‌تر گزینه خود را به ما معرفی کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/456205" target="_blank">📅 14:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2ab9f9ad.mp4?token=totrm2ueLDojRA56IvZOC9-zIa0mFqWPEUW2HLf6ObpTyy71sR9XWiOWyEUcPdNnPL5G7Cvre1dKDUQZk2Yt-ejvS9vVpsOKSkAoNAr2mnB-rdr02V-TVMM9_JHTPz3Rr2zjPeqgmbTiFhmO_g3Tq0X-TYXw4DQpztxC9yjb4tTL257aY8IuIs7UwuVnYmStdt2uwOOQ9WtMJw8O6rCZzzVI1pBCNlw66qGHbN8BLCWkUIQo1TKk-cQcyXVg9r9m6IEwOZWiGhM3tkGsnL_UW78NV6AsAPEtwWLO85HSMZZ8_eMx_uKWQf5mxOH2byCbzz0VTYPwuG598uO4CEdVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2ab9f9ad.mp4?token=totrm2ueLDojRA56IvZOC9-zIa0mFqWPEUW2HLf6ObpTyy71sR9XWiOWyEUcPdNnPL5G7Cvre1dKDUQZk2Yt-ejvS9vVpsOKSkAoNAr2mnB-rdr02V-TVMM9_JHTPz3Rr2zjPeqgmbTiFhmO_g3Tq0X-TYXw4DQpztxC9yjb4tTL257aY8IuIs7UwuVnYmStdt2uwOOQ9WtMJw8O6rCZzzVI1pBCNlw66qGHbN8BLCWkUIQo1TKk-cQcyXVg9r9m6IEwOZWiGhM3tkGsnL_UW78NV6AsAPEtwWLO85HSMZZ8_eMx_uKWQf5mxOH2byCbzz0VTYPwuG598uO4CEdVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: تلاش می‌کنیم رهنمودهای رهبر شهید را به نتیجه برسانیم؛ ایشان فرمودند باید قوی شویم و ان‌شاءالله این موضوع عملی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/456204" target="_blank">📅 14:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuBKe2KZwKCwHnrcFi2Fd52mHwCs_hDkuUc1jW0pArIZBjOeBfqNHE0X1yfX6UvPfzDufsi6Vg7tUxYtcXxdA-q2XxHVcPbtUrglDH5Xe1bkxvb-nOdKAh2fc6zusKxtbxA8ousNCZNT4ra0SbqNh6OXhM9J8_fKEeF4HA5fu-DlhMOMUUmrMakLkDK_6UM1GQUEJDP5V7_S1IR3Bh28sFNEsFCvtU4maPDesDttmjki0nl32OI2WTdhP1292WGZ8JxOfgyFuGO4Kg4XBWdym6rUa-AbVNLIiPmedOf6hVG1AfGONVS-dKuX_tl1UZoWVhFRadwgaToagcKIV0hqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در پیامی فرارسیدن هفتادونهمین
سالگرد استقلال جمهوری هند را به نخست‌وزیر، دولت و ملت این کشور
تبریک گفت
.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/456203" target="_blank">📅 14:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مسیر جنوب به شمال کندوان مسدود شد
🔹
پلیس‌راه مازندران: با توجه به افزایش حجم ترافیک در جاده‌های شمال، مسیر جنوب به شمال آزادراه تهران و البرز واقع در جادهٔ کندوان ساعت ۱۲ مسدود شد.
🔹
همچنین حدود ساعت ۱۵ از مرزن‌آباد به‌سمت جنوب محدودیت یک‌طرفه در کندوان اجرا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/456202" target="_blank">📅 14:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otx9qBbLkJ6s8RVXtp0emdcr9R_E5YkqHUqjjZsocwdh2AppnBuGMsko1nwAb5ksS-c4jMmKJxoyXzymjYMiLChA5j7FLtiR7xQwtny5BPYMOuYmpVWhDxv51n4er8YWopcA7UhIZrfcNwSt7kTU6_MbSP9OmDjH88Ggr99SQ3skpzOgdFsF_t3T9Gdqn20lWoeYWS1_WMD2c64oV2EwDfYiAgbSM5_9ldQvx6cyjhpZYvbqw4TlJCHNspMmi_0IVutny4Ubikkb9o7XO605048P1uMyW0Sq47YGpCtmwMzA2dzB83Brg4JjNl1WApKVkIu_Yye02c8arqnI2fcqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای فرودگاه بندرعباس ازسر گرفته شد
🔹
فرودگاه بین‌المللی بندرعباس از امروز بار دیگر فعالیت پروازی خود را آغاز کرد؛ براساس برنامهٔ اعلام‌شده، در روزهای آینده از این فرودگاه پروازهایی به‌مقصد تهران، مشهد و اصفهان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/456201" target="_blank">📅 14:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Fu3GFlkxwi5xydxjYGtvQi21NJzkUVcsWmPMP_SUBk_ukoy4qXHJDEC3rspu4ZZGatduoiESvXn0zSQHcvWDvG5vZoSptCQvNx5MVEbSVjuijcB57B9yoL4kGXU6EITrTrhiK671GVc_iOW_A5uN0_DITh5znyQHFXLRQ0qYNcFqv4nhqa8LYfT04Bo9UUMUqHxK_F8eRaXbMDt_eI0nNRO40P0I8k5Lm3JSb0ZRGBkHXLE69ftrhgDBSGD0b_cILk8WeKwTl1PCUAlfzZSu0R71Oc9eKCasANoqhmNzc0vE3gbo8gdakbCCtgHreASGrVZn9Tt9NxZq69sgacFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۲ ریشتر در عمق ۲۶ کیلومتری زمین، مرز استان‌های هرمزگان و کرمان در حوالی فاریاب را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/456200" target="_blank">📅 14:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX9iyaju-uyLwVmeJ2d1TB0mN9xnW2IAO_QilwUNOt-ddKCWzf7oxmUbkFqXD5RW-a12bjxW2zVic07KiaBoh1B0rkcm9V7rpdbl7pjBBrCaQ2r71eNBOd8uYFc6McCE4FOW3Cj0aVW-d4wieeu7fMGlCUlbtZTGBwXCxcsXlG104qBHwZWiOB5O0BthveJ25tN_33uZADMleG4fVEV3WgL-2VWVpzXa_m8zKjpl0_VqkUivczkI6JyMyLNJUOusMQF59fk6ybygFf67ihXmuJJ8mygiZsfdSiL6HWoLo_spVlkhglyQvzf4RpnHo09Gpb-xdDsHr71WK10ij-b6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران و تاجیکستان پای قرارداد نفتی بلندمدت
🔹
ایران و تاجیکستان در تازه‌ترین دور مذاکرات نفتی، بر سر یک همکاری بلندمدت در حوزهٔ انرژی به توافق رسیدند؛ توافقی که ۲ محور اصلی صادرات فرآورده‌های نفتی ایران به تاجیکستان و تأمین نفت خام مورد نیاز پالایشگاه‌های این کشور را شامل می‌شود.
🔹
براساس توافق انجام‌شده، ایران قرار است در قالب یک قرارداد بلندمدت بخشی‌از نیاز تاجیکستان به فرآورده‌های نفتی را تأمین کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/456199" target="_blank">📅 14:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/456198" target="_blank">📅 14:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d648076.mp4?token=sU6IssAd_s28g7EvUTuiGAgzq-ZnBZNER-Ufmb5aZRk9KIXMBXbH5vYv_f6tF5VMC_0xyUriP7NsXLhiCCHxbk50dBrslHtI9LMtihECH9pXOMO2iHUGz52uZv3B2xe9q6LU5RJrw_ZHRq_1-F435wv9702nrCuodBbUPM6S_jOzGm11PgFFTh6C-hZH9NORDP9ESJ3B8RVyLW4htkfnY7iWFj1E9Ys0RiSIo8sWXDSphcYZqOn52fmuFB7LZn5ETo4BMUUpIroGTsHJRIyt69TL5m-AI_iIlCvMPgBEOKYHgGDGc-vRSHVZf1yOrIbF4srRgQKovcRL7K5oufap6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d648076.mp4?token=sU6IssAd_s28g7EvUTuiGAgzq-ZnBZNER-Ufmb5aZRk9KIXMBXbH5vYv_f6tF5VMC_0xyUriP7NsXLhiCCHxbk50dBrslHtI9LMtihECH9pXOMO2iHUGz52uZv3B2xe9q6LU5RJrw_ZHRq_1-F435wv9702nrCuodBbUPM6S_jOzGm11PgFFTh6C-hZH9NORDP9ESJ3B8RVyLW4htkfnY7iWFj1E9Ys0RiSIo8sWXDSphcYZqOn52fmuFB7LZn5ETo4BMUUpIroGTsHJRIyt69TL5m-AI_iIlCvMPgBEOKYHgGDGc-vRSHVZf1yOrIbF4srRgQKovcRL7K5oufap6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت تحقیق کل قرآن با صدای شاکرنژاد رونمایی شد
🔹
حامد شاکرنژاد قاری بین‌المللی قرآن از اتمام ضبط تلاوت یک دوره کل قرآن کریم به روش تحقیق خبر داد.
🔹
این اثر طی دو سال استودیویی ضبط شده و به گفتۀ شاکرنژاد برای اولین‌بار در جهان اسلام کل قرآن به روش تحقیق و به‌صورت تصویری ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/456197" target="_blank">📅 13:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVhj3LJwC59GbPQ-OaB1QhAtZp2njEEZQZBZk0LwI_Cx9SCjf62zHtqqhNao1SG1yE50chNrY9l-pK-oInlZuXuOwlEB8_kZqtLlcBv7UyEP-nc2mfqk7QYQAtVciafKCoHMErmhEJm7g-kHfUULL_0b_ZjeiB2fek4oRU-sdbGgrdcbLyEa98bI2fhCuDwssdMXEpvNGgCE686rDy8DlNgsYQIZtUoUNbrb66QBS-1nYAGofM8EUkIJ3jJb820XsFwqAIWfK5vBC8kJeNY_8P5FJkSlFSLCu6fNyNuwSSJUHz7trswqRGgn2xszHrM6nhTTMgk54-XwWmwrIigGYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بازرسی: ۱.۶ میلیارد دلار توسط برخی تراستی‌ها مورد سوءاستفاده قرار گرفته
🔹
۵۹  پرونده برای متخلفان تشکیل شده که تعدادی بازداشت هستند و تعدادی هم خارج از کشور هستند.
🔹
بعضی از این متخلفان در کشورهای دیگر کارهایی می‌کنند تا از آن کشور ممنوع‌الخروج…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456196" target="_blank">📅 13:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFVQzFUm3_FRQyqPc5nQMb42lHYAhXZoV4i_9uynudhIlpXtitzczXZGpOp9AwVpHX9O-VLVf67tOyxOuS0TvmERynC_pR8cu-H15vVB_qg1YCrISNGdkbLvGOXNV-txe-qN3CPb9auOcH9Cu9ST4bJn-IxY4tbBr1dnJfGB_qS7-pnVCqlZj7ucwGPjO_RpLOQengMxvqqeeaJco_vLhzIwXOWV1Hk0CQMQd846cud56NQmI4fJ1cmyqmPL2ibx-076bWxepugpUwoaJ14VveFFIdMOprok3-D5Cp46IXILatFK5Zs-EanFAzxJjUmcZg31wpJbSTRvL0a8YlZf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
در حملهٔ بامداد امروز رژیم صهیونیستی به شهرک «انصار» در جنوب لبنان یک مادر و تمام فرزندانش به شهادت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456195" target="_blank">📅 13:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a34895eb.mp4?token=s-avHggZgCu34Dk_2GjyB6uM-JpdreSe9FYXJQDQhABRgSziWMmvJIucAYV02cZqbi3NWJyv8I2CQ8tlP8FarEVdK8xOgSGNiCcCGom_RORkAhle4tSnGQWad5h1lrxE3_c6DtGGyHy6O0m_b76FR7cz6u6mAa3SG11hDdo4KKn27SDQjOmECzfLKRZthB2rthzDCb_If_RqrUc4mOy13t-tJDO50P-J5ccDwYasNVt91oOG7VVPgJVba-GuNgSh1Q6nNO6xevUhhyLRJAo2DilIc4rRbKXivO3mWnA8sRen6u2W3V--cVrTV_porzNBVsUT2ac64fy_B_J5HQ8LGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a34895eb.mp4?token=s-avHggZgCu34Dk_2GjyB6uM-JpdreSe9FYXJQDQhABRgSziWMmvJIucAYV02cZqbi3NWJyv8I2CQ8tlP8FarEVdK8xOgSGNiCcCGom_RORkAhle4tSnGQWad5h1lrxE3_c6DtGGyHy6O0m_b76FR7cz6u6mAa3SG11hDdo4KKn27SDQjOmECzfLKRZthB2rthzDCb_If_RqrUc4mOy13t-tJDO50P-J5ccDwYasNVt91oOG7VVPgJVba-GuNgSh1Q6nNO6xevUhhyLRJAo2DilIc4rRbKXivO3mWnA8sRen6u2W3V--cVrTV_porzNBVsUT2ac64fy_B_J5HQ8LGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
۲ حملهٔ هوایی شدید رژیم صهیونیستی به شهرک دیرالزهرانی در جنوب لبنان
🔹
رسانه‌های لبنانی از هدف‌قرارگرفتن یک خانهٔ مسکونی در محلهٔ «الراس» در شهرک دیرالزهرانی هوایی خبر دادند. این منابع گزارش کردند که همزمان یک موتورسیکلت هم هدف شلیک یک پهپاد قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/456193" target="_blank">📅 13:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456186">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1-B9EOY37S0WhPLv4PU_BZpSrPzxhl35MPy_ynSXUuvBufvWurLW7PG_MrrxUCEkz9eEX5Na8Ktchyfb4_F8OO4VYM8zNYSdTEmOjNeVtgdj026rgwODs8eu5TZt45jZjxLiw7KOQBMDD5tGI49Sja-C5Xl9YmaQwhmtdZyr6etNEk5Wpr48AAmVNuvkbeyKvPgxDly2YtEAsOrY0-ivVocyrt9SeynIj0l6ns8gHgm7jV7NlmV-nTsB3fg88hlhAyhkT5lZ1tYKVUeKAu2GJbbiLO3Hhwk-5su50TIWchRxcCbrsB5saMW8ps3CGrlc6UkR5ZaqpOVxE6ONzCcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4pnbHoYnaBMq7P8lAGhTybIgvxQ4G5Q6rx8qM4p9kZvjPIhEFBDK_myaPLDNVg99X60O1Nf6z0wq1v36SqJ6piyYOowix5cewcc4Fo07lyZ1_1gXYD1_y4fopZFZA2eNJ_K9T1a1Thu3RghsTHaXLVNTG2v9msXNxS_tLp2YsnnW83zUh6kKBDcWZZXuyBIJcXdPzqHsVzPv8z0-B02GcOAjwFo6iOocxupZMqnvFx3QDr7EUbxqezRr6sFwM8HtwcP3fyVoc-3wr7lsEOJqXZqeYQ960_OPqxw2a-fbWjaVh73__BNaqDVg2cp9Y1k1aWEe2I676huaDBFDXvY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z62gVptTTS4oiOyRgU3RxKUD0dKMn8pywK8l1rUOUxM__68nR6QuN1-b4WAXOAv98ddjmowCkc2TuZ0zxNzFyAPtATh-xPRJxYXbArWGv-fMSt8L3E_XZcsAWv2cr4bAq4iJaYdU0ZgaS4tJp-ZmoDn5kJyUWaOT9I8Srgita6uZQR4osIcQWeyfQhqlfTjvU4KGM53AOwWdqjequ7BrO07OfJM6NhdQ8rlqEbGjlYMHElw6q7IJa-TwSanPs_l7rqxAKv6KnjXGTSdrN5wV1Irpo5gUoG6B1Dm1hFVz-GtKiWODIJoU17qpE7spc5buyjODHK7js8U45Irv_SCCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_Rockk4y4yp2RNPq8MRE6TN9QylclnkduzRmEWWE_1mO3uaWSAaZqiBkpOAqGSQ31coCU6rE3KJXpnCgALW8mny42eq-ZqPIib5EZqOgzsgf3UnBZT41AGg2lgvVwhVadCAf5uN8dqifg6u4L7YzYzcnb7UnGoIcr_FFAEM1iokC2oRw84AiokLRv3bTtXFO0VBN1_SJTXzCr1-M3Scbyl8ojZI2AO-We68vjp5P1N7LC45Ib2ahs_Ogojod7jCqSiYtfXkn-5hOsFrr1D1jr0mcbdiNzcJCwKTjpeqkMoQHMHw8lngYNlALBw05FoG_PLlRVrRKmxxiT0NFxQDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqNMdKESFN5eXNgx-PfYtXr_L6_8HGP_Cqz_IizMKzWFpaRcPpRediRVrHgNnoQJyDlPKl1yCr_pgbydcUrruwpjfPHpQB4U6oJ4KeoDbsTOFVbw42h7SeHFudMw1R9MLZChw6fVF3yI_8pFVeXAN6KNGzrkAdqiTDxUzooQ3272Vi-O9Vad0lbLL2fzHu3ZyjNBQxcQasoWKabl5ydm3y6zQMkLZPSs_an8Vnkr3hEAk09pZfmTu9UgMXW6RfzGJHgy5I6LbQEOFYiNnfB9Wf3zOpeigZic1gGJsxb6ISstFd-9iKPVgR1L2z_51vSHtEt4GUD-OknOR2t3KD0mhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1h4LPtp7eRHguz60lC8lKJrJcjbmjHAfah86ToRrkwvHaWEVC-wZsvC9WA44Ic0bZLUDNKubVpatQrzem9BE8JfQGr3NYT30M26P4q2AXa20qQ3j-TgQMpmnU2yc4uAUJfaQfNLSyItlJlCa-F416WYQLAJyB_dD1yzSYKClOv_AoL3o-LCjPdnZS0jd49gw4H3-Cl4enya2U9RYg1fObh_TmQ-m474zXZomTx8Zq4Op4H3Qv-lv9FUs7bwAGgDsItj8XwVs1TPae-8UZjJpzfY6bLjdk0HM3qVFfgbzpAJaeMB01UyS3j3hEHMLzV6MeOWVDQAI_MI0FIwHw1_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWnEAP-rVTfPmWcrPzeKs1hNYf2V2YLLxGmGeGdy6sfYxJTAQml9UC79tJUbf2nlTV6oBow2Y0gY7nXdlKzFBwz_zk0nZM8bvjWVo5IxsOtW0r1qWS1nAqLbyZScHqRARn51emRQHNPp2DTuVrAPKg-QyMtfgfMkKI32vfKWiDOZ1E3vNCw6rGVvPrGZHDMpA6jrsHMBJSAzcH_utQu5vKaPrKiB8vWOcFviWVnlGWsT3oVJNBTkmey9TFEDodJNXBDZ-68J004ob_uVOf9FX_dgDrXm88WZDEAgecq1pKr208X872cxEARQwTr64hLcLOeM170cSnlkYC4sVPGNCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات واترپلو زیر ۱۴ سال کشور
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456186" target="_blank">📅 12:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456185">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpRUCLvaGxO9ZIdA1OMHv4Q9hMWS073tfgk1LQMA5Rpyb3aZodB9VOBIrwC7Akmi6M2lJ3bTjUFdjvXeXp5zLIu6rLKxjnBNbeXFY-2K1mlMbfnhNGJ0tNXyBti8Jg0WYbqTKtJiFD9S0ycH8QAQ6VliIWF8j47-eep7OlCQ_P8Tascy0jEaP8qgYbDExn3317sOgmddcpz8L7h8rYoNXcwW73iKI_XHOMjepnn5_kCPuUGxZAeYE0Z7EmPFA8Xm_zuhmGMrvsbI3_J3a4BgzvIlJMrIyRFqUy5UGffRRrn2CbWMWKOz9CTIwLwHWQXEXbAwjanDIqwD9YJe0LeO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ دانشجوی دانشگاه تهران به علت آتش‌زدن پرچم ایران اخراج شدند
🔹
شورای انضباطی بدوی دانشگاه تهران، ۲ دانشجوی متخلف را به دلیل تخلفات انضباطی از جمله ایجاد آشوب و اخلال در روند آموزشی در اسفندماه ۱۴۰۴، به اخراج محکوم کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456185" target="_blank">📅 12:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456184">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS8auPNwTrk5LIIT0WmylnrGebjfEx1bpzFuB-bU-Z9pxTzNihzn-WbIPx15VqUyX03OyCWZOO_itSyP4BpWDs4FnDoTHDeJM_mODtbiRbsMASamGo5fhx9n7dXPFtBxgSWSly_1DIPL2TPrHQNifpT4wuZBuqEVV9TdIeQpiAvCMSdqEaiy89fgCVqGvZVj4sz-EzHVsLUf-nGI8LOErKObclLgc__-YxIcMaQ3Dd4oGNWJJnjwUOMyaSX5lPkd7PSzNkRxaEEQdJGJF6C_kjKzdhggB7I1JNNeAEPg2NNTah8EaLRsC-HYHaj8XxV0HGvOv6pjACGInWlKTyvYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضایی‌کوچی: کنوانسیون خزر دشمنان را به سواحل ایران نزدیک‌تر می‌کند
🔹
رئیس کمیسیون عمران مجلس:  در شرایط فعلی نباید دست به اقدامی عجولانه زد و به‌صورت شتاب‌زده یا حتی محرمانه، توافقی را به امضا رساند. برخی از این اقدامات شتاب‌زده نشان از ابهامات جدی در این…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/456184" target="_blank">📅 12:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456183">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab15b5cb9.mp4?token=lDdjUjDtQrQzoIY1M2lZnMZpKTU2DZKp8JgBn0Zg-zoFGsJPw2ic-5jwbW_PC89RouLmoIIFnGnoCwi_OaxWYXqEehHVrQfQR9CWSvAgY_hm-35ly-f_VR5W-ITtyXP2PCLJDnLhCH2fckSobUuTc1ftyxJ1JLqoS_SAjfVpmvygz0SwcJpMu4aGP-Jp08vaA4JmiemC_Ht23hoM_Kz9btLWL_Fmn2PMA8C29papre3xVkXCvkY5_YcL2POD6bW4iZ4fTcquNtXcNtwqAeFqKow31g-JWTRJfYitDpneOTCHeTR8K47-6UKZJH5Sc7YdZ5tpi4OiEy0xZxBbCYn8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab15b5cb9.mp4?token=lDdjUjDtQrQzoIY1M2lZnMZpKTU2DZKp8JgBn0Zg-zoFGsJPw2ic-5jwbW_PC89RouLmoIIFnGnoCwi_OaxWYXqEehHVrQfQR9CWSvAgY_hm-35ly-f_VR5W-ITtyXP2PCLJDnLhCH2fckSobUuTc1ftyxJ1JLqoS_SAjfVpmvygz0SwcJpMu4aGP-Jp08vaA4JmiemC_Ht23hoM_Kz9btLWL_Fmn2PMA8C29papre3xVkXCvkY5_YcL2POD6bW4iZ4fTcquNtXcNtwqAeFqKow31g-JWTRJfYitDpneOTCHeTR8K47-6UKZJH5Sc7YdZ5tpi4OiEy0xZxBbCYn8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور وزیر علوم در خبرگزاری فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/456183" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456182">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT3v16xv5JlBUpVYtdu6jFA7cpdDzTjFUNER6H_EQLZekUTl2uR3NIsXK4s_HZrYBia1Ku8tzfABeTUrFGoj6PJfuukE79VC-_Vo3vaTYGZ2ebua9rpgZQRRIMk7mZdthWjqYS20xsZ32ctCZJzRLQ5Si5bn6ugUbnB0AEBNMxYnWDCqi6AsdqFajsrwq3bjv3m0svJr1Vta2cFJCzNrHVMqg9Yc-iCDp4a0F_dnzsz6QybKjklnefokLeAzxsKog_2uq0g0--A0DsPoE8gKOeUzE4Gyl9IVeLn7wD-vdeP1G6gthEUzum74JCU7HHOxi0lwn6D3w5Fd_SvCZhFyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنبهٔ ثابت بورس
🔹
شاخص کل بورس که در آغاز معاملات امروز رکورد تاریخی جدید ۵ میلیون و ۷۷۲ هزار واحد را ثبت کرده بود، در پایان معاملات به ۵ میلیون و ۷۳۷ هزار واحد برگشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/456182" target="_blank">📅 12:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456181">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شهردار منطقهٔ ۲۰ تهران: ایستگاه مترو میدان حرم حضرت عبدالعظیم حسنی(ع) به‌زودی آمادهٔ بهره‌برداری می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/456181" target="_blank">📅 12:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456180">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0pCTNp2XL1LGAdsqbeRxGAgunMcVD2Gg8MzOFaSrSkyVy9Sz1yueG9sAeYnYOX_6UA82_amQyh8UGrU7UDOASf8kHDBThAAwjZ1gJcYVLxwi6048HmAhYJSXGwMztShiQ6eKEK31pW4BOTvwMoNYJFNte-Ln8EkhRZHp5UnEmPJRX2rem_VmBHx3McdiA7MfY-9B1TeRV5j0h77ijGaZX5dfcoWZkehz6pxGOvh4RMfBWzs9MojeX6RA-79QR2S1Z6sXqwvf4GN_LgyGwTNx05rYsNVXTlzh5CBnk07qPLyWRpPgBRDx5lBijdCA4_UKqKAUjPAAkE6ZCZbybYMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر انرژی آمریکا باز هم فاز کنترل بر تنگۀ هرمز برداشت
🔹
در حالی که روزنامۀ وال‌استریت‌ژورنال با ارائه آمارهای جدید ادعاهای دولت دونالد ترامپ در خصوص کنترل این کشور بر تنگۀ هرمز را به چالش کشید وزیر انرژی او بار دیگر ادعاها در این راستا را تکرار کرد.
🔹
او…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/456180" target="_blank">📅 12:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456179">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a913722b13.mp4?token=o7c7RC4DCe_9TLZmaNhv7QWW4BDF_zK0e4FzLvjdVKbKtEvD33tVfiLc3IB-P4SFEG1K4NDV2UMqi3VJcNS_bW4BqN_qFgunBlqhYjroQEF3jXx-QHm_i6Tq1ycbKezAPnk8NSl6yRe8_8piUMrU6-1Ea2k1qHVr1cUNSFa3iS8rQDrU12jYfqslmtaxDPWoQmzMl4v4BKa1oUyuXZnqFkt-hnF7ltRl-Fj0G-DZsmwL3WAMloM0WbTUBgGOmCKUPrm1_9Tp8HRqvdsKCqWl1Chmskgo18vt-dshMmfCb7xDlxQq8CCKzX60btiWUUgDRUB1vntrJX539V442Lu-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a913722b13.mp4?token=o7c7RC4DCe_9TLZmaNhv7QWW4BDF_zK0e4FzLvjdVKbKtEvD33tVfiLc3IB-P4SFEG1K4NDV2UMqi3VJcNS_bW4BqN_qFgunBlqhYjroQEF3jXx-QHm_i6Tq1ycbKezAPnk8NSl6yRe8_8piUMrU6-1Ea2k1qHVr1cUNSFa3iS8rQDrU12jYfqslmtaxDPWoQmzMl4v4BKa1oUyuXZnqFkt-hnF7ltRl-Fj0G-DZsmwL3WAMloM0WbTUBgGOmCKUPrm1_9Tp8HRqvdsKCqWl1Chmskgo18vt-dshMmfCb7xDlxQq8CCKzX60btiWUUgDRUB1vntrJX539V442Lu-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف خودروی متخلف پس‌از انجام حرکات خطرآفرین در اهواز
🔹
دادستان مرکز خوزستان: یک دستگاه خودروی پژو پارس به‌دلیل انجام حرکات نمایشی و خطرآفرین در کیانپارس اهواز توقیف و پروندهٔ قضایی برای راننده و سایر افراد متخلف تشکیل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/456179" target="_blank">📅 12:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456177">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca49c36c6c.mp4?token=XNmprV_sID3k80b4hIPPJn5FcNpQXl2AozgLLDhgRMP0he4QKxPgEeD4CC4YNq-VvmkmttlFOG_sxrzyH2OlnRZiWX_ehUVpo0wq-2BVL7eFYX3h8YfijPDiC6Mud85Kyfl95JOODiVGBjYFpGeB519XNJCTMkafFTcXntDrPK5QlFEDgkpFm30_iGK3g6DSBbDTdK9wpoDNgijJWqZVq6bue5-ml-9CiVx83SkjElgLJTj8eR9iILcwMMpomBhhhDE0Ya9SMHYHjdgG63SEi41IZiDT4NjX_qyoz9eTSn9AoAWhmqQiYByzdR_V-lE_VBgFd3DxZP7juqIHzqWwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca49c36c6c.mp4?token=XNmprV_sID3k80b4hIPPJn5FcNpQXl2AozgLLDhgRMP0he4QKxPgEeD4CC4YNq-VvmkmttlFOG_sxrzyH2OlnRZiWX_ehUVpo0wq-2BVL7eFYX3h8YfijPDiC6Mud85Kyfl95JOODiVGBjYFpGeB519XNJCTMkafFTcXntDrPK5QlFEDgkpFm30_iGK3g6DSBbDTdK9wpoDNgijJWqZVq6bue5-ml-9CiVx83SkjElgLJTj8eR9iILcwMMpomBhhhDE0Ya9SMHYHjdgG63SEi41IZiDT4NjX_qyoz9eTSn9AoAWhmqQiYByzdR_V-lE_VBgFd3DxZP7juqIHzqWwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاتک سنگین حزب‌الله در علی الطاهر؛ ده‌ها اسرائیلی زخمی شدند
🔹
رزمندگان حزب‌الله لبنان با تلاش نظامیان صهیونیست برای پیشروی در ارتفاعات استراتژیک علی الطاهر مقابله و ده‌ها اسرائیلی را زخمی کردند.
🔹
ارتش رژیم صهیونیستی در پی ناکامی‌های خود بمب‌هایی را بر روی منطقه علی الطاهر انداخت.
🔹
گزارش‌هایی از درگیری با سلاح‌های سنگین مخابره شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/456177" target="_blank">📅 12:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBDrRAykowbLg8IJgDT0uNxr-sCRnPMcKEu0HZfXQFD0kKUG0nYYV4NUThwywZcFmSVaEuWf6wqlrhQdTJamOOe45n5L14ziqzezOwd87EQliictH6P8v9pZVrZwaO8NCp0Zw6lsMgflmskM5sSKULlKuG-K8e1GEZF96Poy_t8G6gOiOWzSRpwFdcJzpAQDh6efDs18i9IP683Ey3-xWNAah1naXobVaMeQR-_qUXeM3hU8ZK1X0JYRdxGc5CMFPagarc8EuGPNMI2nilnDGR4iI1M98DBifmdUWls6L9R2oPvvjeZF6DkMC9QmnfU81EGVjQVdYVm4qW7cr9p5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابستان هم حریف قیمت تخم‌مرغ نشد
🔹
گزارش‌های میدانی نشان می‌دهد با وجود فصل گرما و کاهش تقاضا برای تخم‌مرغ، هر شانه تخم‌مرغ در مغازه‌های سطح شهر ۵۹۰ هزار تومان و در وانتی‌های کنار خیابان ۵۰۰ هزار تومان فروخته ‌می‌شود.
🔸
این درحالی‌ست که قیمت تخم‌مرغ ۲ هفتهٔ پیش تا ۴۵۰ هزار تومان در هر شانه پایین آمده بود.
🔹
رئیس هیئت‌مدیرهٔ اتحادیهٔ مرغداران میهن می‌گوید هزینهٔ تولید تخم‌مرغ بالاست و مرغدار ۴۰ هزار تومان کمتر از نرخ تمام‌شده می‌فروشد.
🔹
به‌گفتهٔ او نرخ واقعی تخم‌مرغ برای مصرف‌کننده ۵۸۰ هزار تومان در هر شانه است!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/456176" target="_blank">📅 12:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c9e1c5f.mp4?token=udDaB-_I9o0cAGkxBf7LQVap5VfsF-1EH-diUlN0k70ben198UXVQe5F1uasEpdUfoJnZVkiog1xVq703mWRZQ-wWpD1utcbeeAo9D4vTQ9bLyIC3zfajnvMIJ1l5eJ-odyAIYwy3bLJCs6RFqnSfI-NusJlyYavVk_YYpeU0bQ4lZFGqZaN4wHvv96n-Gwe2-zi6td0DeJwvC-LRyFGKELTeSUCFde7DnXp9T3-wbNe1aIVsCaOoV7C8Kv3WC1NDp_gprDsAIrR3tmahs7aXn7OL5sOK0D3kJME6Kqk8c6U4xVQbDYQW3gaz2OIq4N_nu_l_6gdu5gRb56aU9ztpgLJZ4VxMlCIjIpue_RiL4sfaq-gn5b_SVjE5Rw2x4FG9DsQv79Z-Ei27K_RDDUuYGYM6kV-sxyKq6ZqZzEPks4PHRkqBQbAPvlDArcPrn90zL-h3tZ45-RWxpAPo-Zvc5u_U0pUeQL6prmRHOSGc_WJ3EAOVj-yrTL16yJ3gD0VAoIARiCl3-MUyLE0Br697fl-3AN7dlfFMIiuJx7L1uJSqyBA9pQbt96FvxLBu0uSc69Sn51W7WFppVnPxAw66Odeu6pRK4UhjFNKe7Ls3UdLZYOnmhF4GWAhlPEww8r13RoJxWECuBZ56Q4GwVrA7dYVXlarI5jnwaK7ggBUFNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c9e1c5f.mp4?token=udDaB-_I9o0cAGkxBf7LQVap5VfsF-1EH-diUlN0k70ben198UXVQe5F1uasEpdUfoJnZVkiog1xVq703mWRZQ-wWpD1utcbeeAo9D4vTQ9bLyIC3zfajnvMIJ1l5eJ-odyAIYwy3bLJCs6RFqnSfI-NusJlyYavVk_YYpeU0bQ4lZFGqZaN4wHvv96n-Gwe2-zi6td0DeJwvC-LRyFGKELTeSUCFde7DnXp9T3-wbNe1aIVsCaOoV7C8Kv3WC1NDp_gprDsAIrR3tmahs7aXn7OL5sOK0D3kJME6Kqk8c6U4xVQbDYQW3gaz2OIq4N_nu_l_6gdu5gRb56aU9ztpgLJZ4VxMlCIjIpue_RiL4sfaq-gn5b_SVjE5Rw2x4FG9DsQv79Z-Ei27K_RDDUuYGYM6kV-sxyKq6ZqZzEPks4PHRkqBQbAPvlDArcPrn90zL-h3tZ45-RWxpAPo-Zvc5u_U0pUeQL6prmRHOSGc_WJ3EAOVj-yrTL16yJ3gD0VAoIARiCl3-MUyLE0Br697fl-3AN7dlfFMIiuJx7L1uJSqyBA9pQbt96FvxLBu0uSc69Sn51W7WFppVnPxAw66Odeu6pRK4UhjFNKe7Ls3UdLZYOnmhF4GWAhlPEww8r13RoJxWECuBZ56Q4GwVrA7dYVXlarI5jnwaK7ggBUFNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماعات شبانه تا چه زمانی ادامه‌ خواهد داشت؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/456175" target="_blank">📅 12:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزارت اطلاعات: دولت فرانسه باید پاسخ‌گوی مداخلات دیپلمات‌هایش باشد
🔹
وزارت اطلاعات در بیانیه‌ای به دولت فرانسه هشدار داد: سربازان گمنام امام زمان در فرآیند رسیدگی به یکی از پرونده‌های مهم نفوذ و مداخله خارجی و در حین اجرای دستور قضایی بازداشت دو تن از متهمین پرونده، از حضور غیرقانونی دو دیپلمات فرانسوی در محل قرار مخفی مطلع شدند.
🔹
از آن‌جا که دیپلمات‌های مذکور دارای سوابق گسترده تخلفات و رفتارهای مغایر قوانین داخلی کشور و تعهدات دیپلماتیک بودند، پس از احراز هویت آنان، مراتب به وزارت امور خارجه ایران اعلام گردید و سپس دیپلمات‌های متخلف با حضور پلیس دیپلماتیک، به سفیر ایران در فرانسه تحویل داده شدند.
🔹
درحالی که وزارت اطلاعات بدون علنی کردن موضوع تخلف، مشغول تحقیق از متهمین و بررسی مدارک و اسناد مکشوفه از محل قرار عناصر بیگانه با متهمین بود، فرانسوی‌ها به هیاهوی رسانه‌ای با هدف فرار به‌ جلو و پوشاندن تخلفات محرز صورت گرفته پرداختند.
🔹
تحقیقات اولیه از برنامه‌ریزی و طراحی پروژه‌ای گسترده با اهدافی همچون نفوذ، مداخله خارجی و بسترسازی برای اقدام فرانسه علیه استقلال کشور، از طریق شناسایی، برقراری ارتباط پنهان در داخل و خارج از کشور و شبکه‌سازی همراه با اصول پنهان‌کاری با برخی عناصر مورد نظر بیگانه حکایت دارد.
🔹
از آن‌جا که در قراردادهای مکشوفه از این پروژه شوم، امضای سفیر سابق فرانسه در ایران مشاهده می‌شود، دولت فرانسه باید نسبت به اقدامات غیرقانونی و مداخله گرایانه خویش پاسخگو باشد و درباره این طراحی خام اندیشانه توضیح دهد.
🔹
وزارت اطلاعات هشدار می‌دهد که اجازه رفتارهای غیرقانونی مداخله‌آمیز را به میهمانان دیپلماتیک خود نداده و در صورت تکرار، برخورد درخور متجاوزین را با مسببین صورت خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/456174" target="_blank">📅 11:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2RGxP3o2yx7-9eInlZE7AcFykA_KyMlsbi6Os29P8j3RrVwKto8h_6C2nG1laK9x69mzrZ0KhVhEX9SiEyH9i0XVWxtDCIBUIS_ZXUWKT_xrkRKHrhv0pI5oYq3PgtFcY8_W5M5wElAzk7d0v58sOMAWlkv_mopLK53O8TYxsjfWRURiZME0nDtzX2CGTDdIHyJRzko3RjBqC7K2pinQcjzePS3SrQRH9NTvmbRKmGIcwc4_qstylS_NYRlfBVceazK587rMNvrkOErLL-WGFa034rauZuonftvtIeseWHy8HTvWFscWVUVGLeEwc0ksPlQ3wMKzxeCDPv8_6bwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید: ترامپ دربارۀ «آمریکایی کردن» تنگۀ هرمز شوخی کرد!
🔹
وال‌استریت ژورنال به نقل از یک مقام ارشد کاخ سفید گزارش داد ترامپ تاکنون با مشاوران خود دربارۀ اعلام تنگۀ هرمز به‌عنوان «قلمرو آمریکا» گفت‌وگویی نداشته و اظهارات او در این‌باره بیشتر جنبۀ شوخی داشته…</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/456173" target="_blank">📅 11:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456172">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملهٔ توپخانه‌ای و راکتی ارتش سعودی به شمال یمن
🔹
منابع یمنی از حملات توپخانه‌ای ارتش سعودی به شهرستان «الظاهر» در استان صعده خبر دادند.
🔹
همزمان حملات راکتی از خاک عربستان به‌سمت منطقهٔ «بنی صیاح» در شهرستان مرزی «زارح» گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/456172" target="_blank">📅 11:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdvK0k_BZ2B59NbHDPLaM0h1-vCD77Pz8dOfGVR3HESlQeHfQR1H4_DKtPGYfq9jncFPbbBeH5kguN8jbbGdLDKyoEDEK3p4w1BFye68DDb_82OIZeWwmzh69tyzh10qIqCcFN3dJPw2zj6YseSHd-4VDN1Zrd9TSap-znl9l1uc7psQrTMU-mKKVRP2vWWh2ECzorRs3mwpRP9kEvB4t2pE6H1C8_MEqdpbLP9txD3_sXe8umiNVHZucWG9CO018B321gDznVNlGZAOe50l_FnErhINWn2U5s--vzwr7B2JW1JDX6P5kyxZjFeA1fTNVioFzx4Fxn01YWMUv6Jr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار منطقهٔ ۲۰ تهران: ایستگاه مترو میدان حرم حضرت عبدالعظیم حسنی(ع) به‌زودی آمادهٔ بهره‌برداری می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/456171" target="_blank">📅 11:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456164">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGy8BgEqT-cIwksF97A-Ys9lpvIou7j471QhvMHWWI6tCUdPlZdYvKrzI5FpAIcmQdcyfncYJZj39HLyyeIo17DZrHcXAMjgU4Jw_DW1yZQACt2dNWiTP1Xa9EMQqSlzYC1PykChXZQlYUsPF7zDiqAVWl1SvFOejFFoI2mxx7osjB88jKbpRHDFsb8FZxtXBNyyZl8yZY4axC0rv_UwkxVYTHtqSBNsFw0JqvVtybkb_01P8TR0RQJylDNG0SV2mP_z5pKvLBC1KUsgQEbfoY5ZTricdZC8LCcwmrb7GrQqYUKJWpq0jPZ27WAUXJfEQYt_RuHu1a_uhozbNH9bzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WE5faVvxPQGq8O13SciE1jFUf8crl7BsP_bhpWXw5yqt09C6OGDXBdWOcXyyLRozSX9VtQqDmdX-VQp2bYpK7v7nVPIGYfRmSX_-62HsljVNiTZ7qyu-of8wpKl1kbNGJxmsQmIzWnBWqy1Y5Lbrs-bORP9Xw-2XndHb0LqTm18dcYEWPNEyH4TFYzmu-IDsROqu4WZ1iK5N-1ofG2rutzNEgk0iQ60jHM8BM4EXS1zrOkpEin2IX7_SbfuIDu3IZdnfAKeS5jC9UE1DS14VlQnlLnlFn222q6m0kPqYBolK5Dx9jNYZPi6XySp7su0BDMd5AM-Abs4r8K5SC9RxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQoG5H8JACZsxmBkILCbs4J3ZCwiJ0oaK8H9nvWeeY0BzsYDGV6lIt5WCET0aixlfthaaG2LccV7oQ7xcwj3VQiZKswH6FzcjRaj44Hkh5RgVJpXH_xMMPJr67YiQJ6XVkeU2Tyd8W9cTVzY1QrQHOdPF8Qo7O0AMFU9_xh_mAIrT74y9fR75_sv4WeAEc3F-svtQzwsXPD2q_Gs5SbunMuhs4Cuv_M-uNSHJ5SzN6XnNlG_diQ3dFXFdYRpZWupOyJiX_UNhhSHatTB-yN4iZXPSGRzlKouKJgMJH3nqDIt9MnImEDD3EzJQZD6a0Agi63-nmZ8TnXQ4g_nT2bSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ol8SZO8RaN8wlSdiYnPbMAzTkfhfqWnMNBnbF_rt6cVABKG0pmCWuagnbVH0S1aZZj143YqU6QOZ9utvj4zdvdQYPl6E4pqOFvNABgfqmxtvtPyDXd2XA9rU7100e6Tv0OQVKwM5czYAeinlTvfUtlJJbIigwNe5D4R-CyyCDrZJXb8etgL6WKLEqChgXwP6xGZ7e7PA1cIVtA3wRyCAMm4kzm8l4vKX5zs3Ta7iSEmXxPqUfBN43CjwAVU6G3jjYvkbohdVany_4qe27vcVychJYEmD1rCpgQa2ukaTnZYDCEqxgoVrghuvnMrjGgbTM13CU6QCVj2-sS7azH0kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgMeaxk39uAhai7Rxw6Ht8vKRhdRkYDdIK6v3Vn8QB-HF1Kbi9rcCNNNDDl5_VU0ksA0CgIgGrR1XvZqJTDTd-mArgdv_n42cX9K4828-3xXUP52QKigiym2X9P0eKnwWE7Wb_QFPAYOgHYQDM9gp7J3mFnKU9t7w59935yW5D3UAtZVfJTrWgZj7fsaau2dvyGaXl0OARIRq6wVVzAHgBoOwqHhUiMS3BKt7UqghhZUHOgwhNWPSEmLBl8Mn0IWMIP85fHKT7h0z2kzN5l64JbDvBw_GdIXoGeOj2DM3W07LIJ9jp4CcbQhYYErGUIQAucejYZY-1JLi9apxInaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlGlGW7rOqmgx79-3eMgCWiEYNIEXljBxwBFvnXXHF88XCezPO4QmixhflqiKii_GRotp-I0dW8SdIt8QsA20FvyUeLO1SI-YNDT0tLLWnz81xvtU3wRNApDU0bL1L8eZ1mrOC5XpFaxbQlv2nLQVRJU59crFyx-ROho8EMD5AIF9RpwUL1durrKad-jsYA7ZR1DlVPe0Y552_dTdLae7WMgcG8QrVEGfH8kZGuBSZr3lfSdfqajnW4DrtZkRFZG-knf30epdBJdQCC5-t_p0qrz_44kHWT6rmppdp4FkJqvR2Ejzh82X0qfeLktK2HZiKi7r33w4dMsn_1HqE2ZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUcLEllWIla1uJWbf894HtcUX-Et06PBDlIZB_FC8Pc10FiuGawQFXteITgAD4dqFLu_GLSVT664VcCEGJ5syY08jaSLU60z04N_p035GcSTiSykvhP7aHdn5gB0SccPhvimvYybdOLT1KR1v73zeEk2CoaVPwiGmE-B-bnExk2xdI903p--ljHn8IJoWMtw9k2-JzU1210xHU2mt1RPxrDCuMtyCxu3MLEBu9OQqlj9UttwkYENnhtMlO0A5mi2DooFu528kEFaLItrHXj1quS5LHEiBcIGKm6koFZgE4gtwgD-ejbiWk80pr33kNRJUHWQUN21syvI2Jin0B1djg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم‌ ایران در دست هواداران تراکتور روی سکوهای ورزشگاه یادگار امام  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/456164" target="_blank">📅 10:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456163">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/necYsKpJ09UISmbrLnfGqsbyFy06JoLn5FVHMV8VNV3VwaIdiMX5wfcfz9n8CQiu3tdfqO_6PJY7g3G887OBRXoypCNeVH-M7M_H4wSARB62q6lMktYw0e2gypM3luGfeB0kNJpIJK-eAWyII64IVFyk2ostHvYKYpGv4jb4xFYHtba3Hm9r-RQ1BXYJwHSAoiRjs3G7nkrb2qZfCS4YL_PYHCPlTqpbjJ2jAXsNnxphHYU7eak_25uVXKuLFm-WvU7jSsSTnjtCSeMvTHV87YfOFfq2Dr_d6cZARFDGdXjLEVl0OwHumc1r3eL0BrETD0rlJIYqOSFuHf-8wzD2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
⚠️
مهلت ثبت‌نام: تا ۲۷ مردادماه
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/456163" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456162">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-text">💙
هر پیراهن، فقط یک پیراهن نیست؛
روایتِ یک سرزمین است، یادِ یک نسل و افتخارِ یک ملت.
⚽️
کیت جدید استقلال خوزستان با الهام از
خلیج همیشه فارس
و ادای احترام به
شهدای میناب
طراحی و رونمایی شد؛
تا نام و یاد کسانی که برای این خاک ایستادند، در میدان هم زنده بماند.
برای پیراهنی که فقط رنگ آبی ندارد، رنگِ ایران دارد.
🇮🇷
⭐️
بانک ملی ایران، هوادار استقلال خوزستان
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/456162" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456161">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/456161" target="_blank">📅 10:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456160">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsljmVXlyq9VsuBYSqw7VZoDKZUYRQ04dWmshmlU9t7mRckPkzz5o1cfgEtey6TMtWRNnvLaz6RFnSTSRM7yM9cgfiF1lE9YhmnAzr2l4yqcDajepjTJrxS96YyTON02Yc9tF9qTjR_ON3BKRGMnS8ECaGq7k8vhpG88V3IFpWdt9E85A8OGqnK_3WXtqYGI6najbhoteewmMLn56Ci8iOKvD20h0yG6pxwfQjQNAzt0iNZteExmOUqrUsiGwOyl-YbjrODMjJX5f2a1qEfp5aBzZUNjUzEauDSQzTSjSIDYtr6PYZNA7Ks0e_XqtjlopemFr4pQ5WNNrw3oaDoO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترقی: کنوانسیون خزر ایران را از مسیرهای اصلی ترانزیت انرژی و کالا کنار می‌گذارد
🔹
عضو شورای مرکزی حزب موتلفه اسلامی: موضوعی که مستقیماً با منافع ملی، تمامیت ارضی و امنیت ایران ارتباط دارد، نباید بدون رفع ابهامات و بررسی دقیق در دستور کار مجلس قرار گیرد.
🔹
پذیرش…</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456160" target="_blank">📅 10:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456159">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df2f723b6e.mp4?token=BUdiilLxgS8tgH0Hv0Y3RZ86X-RdYQ__PUdihkOEA1YXBCE4Hat5XooB1CU9MoDo41F97ABwZQBElMsh15kLtSHl-20RvUqoDBDJd-8bgq6FkGvO2xvs-gVp0Syvs01WWKC6lDHVz6icBkjs5kGTfugiuCJvroZBbWL5di4IRgA2j_Z4aU5MpZ-eQqWfoYotB8PVQjafy2cjaO24YqK-dtdbvy40du0Ew4JaO1yvPpVhDdMdPqvxrLI54LUefDFpHvoMjK3o5zbJQcY10vCdNkwoUExS_cJv1m8oOua-UivsDG0y69ViyayNW870A6QH8I7QDgRoX5O6dZaPMDZGxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df2f723b6e.mp4?token=BUdiilLxgS8tgH0Hv0Y3RZ86X-RdYQ__PUdihkOEA1YXBCE4Hat5XooB1CU9MoDo41F97ABwZQBElMsh15kLtSHl-20RvUqoDBDJd-8bgq6FkGvO2xvs-gVp0Syvs01WWKC6lDHVz6icBkjs5kGTfugiuCJvroZBbWL5di4IRgA2j_Z4aU5MpZ-eQqWfoYotB8PVQjafy2cjaO24YqK-dtdbvy40du0Ew4JaO1yvPpVhDdMdPqvxrLI54LUefDFpHvoMjK3o5zbJQcY10vCdNkwoUExS_cJv1m8oOua-UivsDG0y69ViyayNW870A6QH8I7QDgRoX5O6dZaPMDZGxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرگزاری فرانسه: تعداد کشته‌های زلزلهٔ ۷.۷ ریشتری اندونزی به ۲۰ نفر افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/456159" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456158">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/456158" target="_blank">📅 10:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7870aa7ef.mp4?token=HqMAAYJI48--vDuFuEQqHaSgAfr6bi-_VpPaJ5vHQCVCu28Y48bqYqfMSN9l89pYUdfJO0UrLpVHFg1UiLBsbtNHOzETnQGEVHATj03GuBrdq1LubSXQfGvxKjk0tUIcgkV6KkpqbXN1KQJ14hC5vZOoUhs40EFilxVm27QoIkk81dBSI3TbsQIAqjP902e3m8hjq6brWXZEZvUceHXpug9i6wJYh6XNoke_t9IB9gv6YcCDxmlvq3-qkFCrRQuQnd6Ps6kqfIvc4wZuW7NriyY9XC8F0xVDcgTMoHBdRmhkJbZwF7VJl38U1gZHviB3dpla6ZOFTVz0ip4eYRXVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7870aa7ef.mp4?token=HqMAAYJI48--vDuFuEQqHaSgAfr6bi-_VpPaJ5vHQCVCu28Y48bqYqfMSN9l89pYUdfJO0UrLpVHFg1UiLBsbtNHOzETnQGEVHATj03GuBrdq1LubSXQfGvxKjk0tUIcgkV6KkpqbXN1KQJ14hC5vZOoUhs40EFilxVm27QoIkk81dBSI3TbsQIAqjP902e3m8hjq6brWXZEZvUceHXpug9i6wJYh6XNoke_t9IB9gv6YcCDxmlvq3-qkFCrRQuQnd6Ps6kqfIvc4wZuW7NriyY9XC8F0xVDcgTMoHBdRmhkJbZwF7VJl38U1gZHviB3dpla6ZOFTVz0ip4eYRXVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای اصلاح پست ترامپ در توییتر از زبان قالیباف
🔹
در آخرین حمله‌ای که به ضاحیه شد، مذاکرات را متوقف کردم و اعلام کردم امشب رژیم را خواهیم زد و اگر رژیم پاسخ دهد، کل منطقه را می‌زنیم
🔹
نتیجه این شد که همان شب محاصره را برداشتند؛ در حالی که قرار بود طبق تفاهم، ۳۰ روزه باز شود.
🔹
وقتی ترامپ توییت زد که امشب محاصره و تنگۀ هرمز با هم باز می‌شود، اعلام کردم اگر ادعای غلط دربارۀ تنگه هرمز اصلاح نشود، حمله را انجام خواهیم داد و ترامپ مجبور شد پست خود را اصلاح کند. این نوع مذاکره یعنی مبارزه.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456157" target="_blank">📅 09:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHKBg9o-R1jnbGDx-Mx__wiLVc-4pPWrD9PUKFmEMZGS7VM7ELd3oWCXhChVHbf_pszRm08wwOrem5XF7zkLg9yxnCxVbx7LtRwcjMmkyU1VDnV00x3WiSye7wgSn1owozOiGPwfsDlCtfwbKWqorLLvF1of0SmfjuGaATppeGKPAYonaIfGRIjyNACPrsIBzMZSRbTxs6NyFcEIGKlt7QoiqEHxATBagBJvQX4jKajRPxL33SVqLhQOvR4Gcbh4W8G8gLLuy66seSLivdgX_PmmukXQUYoz68dPfawfbE2AdHRn7ulfpYs4YkfIPjXSueHm_5481nn7oJvMRQ0N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ‌ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار: ۱‍‍‍‍‍‍۵۵٬۱۶۳ تومان
🔹
یورو: ۱۷۹٬۶۸۹ تومان
🔹
درهم: ۴۲٬۲۵۰
🔹
یوآن: ۲۳٬۰۱۵
🔹
روبل: ۱٬۸۳۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/456156" target="_blank">📅 09:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhBsRrlM1Qf1MTSfWrfbMTusKqJMivGO1eaJPsHgbkO_Rq86qeZbuHBX2hdP2H_bVYFizqMkaul3c7FY9kgeuafAHsLigDVIFp8oBwdr3UXvQjIrLxp_DxgmkAyEyWMZRRttDThXV-5ecOt-BBZCxQKijNL-Z1fAQgxbaPUFEFk_Pls88th4np04oNas4_NizlfGPYL_RyzExfmz2qWf5Ayw00uHYyiKmtNymPnw81cN_zEFHIyZxDPH7K2AawH3Ckg9paF4nwF2nXsuM13nVxrHRlAPWHxtBzxeto1AnL3KqqR44u_3kDnD6VJwXc2dVp7CjZHVAHh-U8mZUSAnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مقابله با فشار خون
این‌کارها را انجام دهید
🔹
سزاوار، متخصص قلب و عروق: بخش عمدهٔ کنترل فشار خون به سبک زندگی بیمار وابسته است و با رعایت چند اصل ساده می‌توان این بیماری را تا حد زیادی مدیریت کرد.
موثرترین کارهای برای کنترل فشار خون:
🔹
انجام روزی ۳۰ تا ۴۵ دقیقه و هفته‌ای حداقل ۴ روز ورزش منظم
🔹
کاهش وزن
🔹
مصرف کمتر نمک
🔹
ترک سیگار
🔹
پرهیز از مشروبات الکلی
🔹
استفاده از غذاهای کم‌چرب و سبزیجات
🔹
بیماران هرگز دارو را خودسرانه قطع نکنند؛ زیرا فشار ۱۸۰ نیازمند مراجعه به پزشک و تنظیم درمان است و قطع دارو می‌تواند فشار خون را به سطوح بسیار خطرناک مانند ۲۲۰ برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/456155" target="_blank">📅 09:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrkLsYk7JcPxO51nIUpMxrB4-iWDhZ54MQ5i3pLZdu6nphoVb_CcB6V0Ag8DYsQv2cBVN5caPV_kQ5sx7Ol8aSfgCSHFo9JvYXBHCkD73KjyCoRdBbnR6S7qpG2ADPjflCzLhZiL0Sif4myNniPZoduZoUwjwKC4cdVDIie4VW1Zb3ykAgR7GXUSJwbyJt9BfqUcfKBWHkbxLerJ9Lgji7fCLefsKVud7W_bXZNVdxshDRJo2fglrZGVcT8eBYyct-PIVrjjabyaXmi0OS05RiOMGByZIT6Z0zh22F1uyUrwykgUXT7c4d0N-RCJiKMkZIlTmCicqKcvq_-8iq0ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی انگلیس: دیشب یک کشتی فله‌بر در تنگهٔ هرمز و نزدیکی سواحل عمان هدف حمله‌ای ناشناخته قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/456154" target="_blank">📅 09:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c890dc0fd6.mp4?token=VMj-Ml4ZagDunpMYink2TOoXP0YVr1yJXgHIpR0VIexNXE9w9fe2nbF4QI4sLFbsARbP8YO4e79pv1mI2m3Ee06UOZ5E77SFPms5N40wmcBVp2iiayCNXOlNHftOUpA_VrbRKSKPZO6KiXNDZ2N8aY6CD2BmubKgeIi0NPV7z76m77urCKmbdcuJUZjL4jC25DTTBeg4ZOa_KCpxbnV42rXPCpbY8AiwIqCL-H0x3jAV174H__JWWY58TIF2lCKcSK6B6DHWIw6N-QzUUClwRr7m84osYrG5zTlta-K27GeAz8_563QrhXNeAhBGC_dWQg95cDGhF0baT0ys8rKRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c890dc0fd6.mp4?token=VMj-Ml4ZagDunpMYink2TOoXP0YVr1yJXgHIpR0VIexNXE9w9fe2nbF4QI4sLFbsARbP8YO4e79pv1mI2m3Ee06UOZ5E77SFPms5N40wmcBVp2iiayCNXOlNHftOUpA_VrbRKSKPZO6KiXNDZ2N8aY6CD2BmubKgeIi0NPV7z76m77urCKmbdcuJUZjL4jC25DTTBeg4ZOa_KCpxbnV42rXPCpbY8AiwIqCL-H0x3jAV174H__JWWY58TIF2lCKcSK6B6DHWIw6N-QzUUClwRr7m84osYrG5zTlta-K27GeAz8_563QrhXNeAhBGC_dWQg95cDGhF0baT0ys8rKRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزایر دریاچهٔ ارومیه میزبان پرندگان شدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/456153" target="_blank">📅 09:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5oWoTWMLluIFoDanRc-OzFDUaCgrAU9gVYLDvGCVy3bWL6Tp8zr8Rr8TseffHLaJxIsbcB7TXnEmSRItMQy9pvYu8aSNYfFN_NcidWJSGZZSOiOgnDDHt94nKgYGxxkUBCz73uiXvk3pfJpwtzqKeCCigoxUblD6Ei6emeUIISizLA4Wt_0BZsLVIyBl8diU2jdr_eNfbTMtEanqxnFuSj8gHK_K0saQoodZ3lQ7dgavuLTZf_jxD3hNXk_k6ppWIMWkhRtb7rLnYB_B5L02C44k9Lmd5UEV-c4z6a7sWXFGo2zmiGxrxsna9tlTi9fxQSkwg64icWql3ns82XjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر وحیدی: رزمندگان اسلام مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردند
🔹
فرمانده‌کل سپاه به‌مناسبت فرارسیدن ماه ربیع‌الاول در دلنوشته‌ای خطاب به رزمندگان اسلام نوشت: شما با توکل به خدای متعال و رزم پیروزمندانه در شرایط بسیار سخت گرمای سوزان و شرجی سنگین جزایر و سواحل جنوب و سرمای ارتفاعات مرزی سربه‌فلک‌کشیدهٔ شمال و عملیات موفق آفندی و پدافندی زیر آتش سنگین، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید.
🔹
در این پیام آمده: رزمندگان شجاع و عزتمند ایران اسلامی! پاسداران غیور، ارتشیان دلیر، انتظامیان سخت‌کوش وبسیجیان و عشایر دریادل و سربازان گمنام امام زمان!
🔹
قلم و زبان از بیان منزلت و تقدیر مجاهدت‌های درخشان شما عاجز است که خدا خود رزمندگان اسلام را بر دیگران فضیلت بخشیده و اینگونه محبتش را در قرآن آشکار ساخته می‌فرماید: «ان الله یحب الذین یقاتلون فی سبیله صفا کأنهم بنیان مرصوص»
🔹
شکوه و عظمتی که با ۶ ماه جهاد بی‌نظیر خود در مقابل خون‌خوارترین دشمنان بشریت به‌نمایش گذاشتید چشم جهانیان را خیره و امید به غلبهٔ نهایی بر سلطه‌گران را در دل‌های مستضعان زنده کرده است. شما با توکل به خدای متعال و رزم پیروزمندانه در شرایط بسیار سخت گرمای سوزان و شرجی سنگین جزایر و سواحل جنوب و سرمای ارتفاعات مرزی سربه‌فلک‌کشیدهٔ شمال و عملیات موفق آفندی و پدافندی زیر آتش سنگین، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردید.
🔹
شما با توسل به اهل‌بیت (علیهم السلام) و آفرینش زیباترین جلوه‌های ایثار حماسه‌های درخشان ۸ سال دفاع مقدس را در صورت‌هایی نو، تکرار و خاطرهٔ نبردهای تاریخی بدر و خیبر در رکاب پیامبر اعظم را زنده کردید.
🔹
شما که با مدیریت مبتکرانهٔ صحنهٔ نبرد تحت‌فرماندهی حکیمانهٔ حضرت آیت‌الله سیدمجتبی خامنه‌ای (دام ظله) با عنایت پروردگار دروازه‌های قیام را بر روی مستضعفان جهان گشودید و با تحمیل ارادهٔ خود بر دشمن ثابت کردید که می‌توان اسلام را بر جهان حاکم کرد.
🔹
به‌یُمن تفضلات خداوند به ملت به‌پاخاسته که حتی یک روز صحنه را خالی نکردند و با دعای خیر حضرت ولی‌عصر (علیه السلام) ان‌شاءالله به‌زودی با پایان‌دادن به دردها و رنج‌های مردم مظلوم و مقاوم منطقه به‌ویژه فلسطین و لبنان عزیز، جهان برای طلوع خورشید عظمای ولایت از همیشه آماده تر خواهد شد.
🔹
فرصت را غنیمت شمرده، حلول ماه مبارک ربیع‌المولود را به شما و خانواده‌های فداکاری که چنین شیرمردانی را در دامان خود پروریده و به میدان فرستاده‌اند تبریک عرض می‌کنم و بالاترین پاداش الهی را برای شما طلب می‌کنم و از همهٔ شما که مقربان درگاه الهی و محبوب حضرت حق هستید التماس دعا دارم.
فرمانده کل سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/456152" target="_blank">📅 09:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456151">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌ زمان شارژ اعتبار کالابرگ تغییر کرد
🔹
معاون رفاه وزارت کار: از این پس اعتبار کالابرگ در روزهای ۱۵، ۲۵ و پنجم ماه بعد به حساب سرپرستان خانوار واریز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/456151" target="_blank">📅 09:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ورود ۴میلیون زائر به مشهدالرضا
🔹
معاون وزیر کشور: تاکنون بیش از ۴ میلیون نفر از زائران داخلی و سایر کشورها وارد مشهد شده‌اند و تمامی امکانات و نیازهای لازم برای خدمت رسانی به آنان فراهم است.
🔹
بیش از ۷۰۰ هزار نفر به‌ویژه از استانهای خراسان‌رضوی، جنوبی و شمالی…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456150" target="_blank">📅 08:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD3RBYPzp6fpONvJkhQlmfFyGx6PoEbDGlMZCUWQkSpIV-Ch8XXeyk25VrVpeetRuzKo5Gd6-XHVfTzJH9W8KQsrViOecpQrqcH_m8ZEoX8Qc5Px83Slr42e4xPW5UYhz-4Ri2hr0wSaS9sX_wJ5zcTdoihW77m6JxDBfjPTo0wd94MHDrm9XU0LBLeQ0_E7OqkAg6KQ-3_4KNaGS0K9LZA4Ugc2tMP1eajIcAfQae6FT_k_r2XaYdBgWFJm7fQ4SgsFVo2LRpH4MEvHZmdGAItiP7zuypVxmxt6z76UkZ0FE6v4FExJrjsEKcHEHmGbEPdZ-qe-FremrwvDjIimew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ بحران در ناو لینلکن را حاشا کرد!
🔹
خبرنگار: اعضای خانواده‌های نیروهای نظامی نگران شرایط موجود در ناو آبراهام لینکلن هستند.
🔸
ترامپ: خیر؛ این‌طور نیست. این ناو به‌زودی با یک ناو مشابه جایگزین خواهد شد.
🔹
خبرنگار: آیا این مأموریت بیش از حد طولانی نشده؟…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456149" target="_blank">📅 08:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnXLqOXm8D56TqQm9IN2o40OytxXCy3aY2kgzV83FfXs5riLl1LsAr4saPF_6jWUO3zPLQ-_2pqZ4F0sR2KAzy2tDBO8nDKPAnBvM5FqOYon9C67tvN9NLEGCPHIL9qXr42GdZBjNkWVuDIOv0SzpvxiwPf5e9bvMpCLuVMlmRmWUGSIWUbnXDiXFpkB1Ohw00X6XVgVIX9mGr0holB7r5MRawsK3mBr00Y3J4NdpZ-cWtGx2tNnghV9BdwX7eJzarK3yuJwB5_dOPJM0i2QfQ-In-g9LGPVq2GlFHw-w6VQEwLRoUPL8r-EcmNeKyT9U647qIEkAAAQXrXTAmeJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران در مرز آلودگی
🔹
شاخص امروز کیفیت هوای پایتخت با رسیدن به عدد ۱۰۰ همچنان در محدودۀ «قابل‌قبول»، اما در مرز وضعیت آلودگی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456148" target="_blank">📅 07:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دریای مازندران تا دوشنبه تعطیل شد
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، شنا و تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را از اواخر وقت امروز تا ظهر دوشنبه ۲۶ مرداد ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/456147" target="_blank">📅 07:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAD--X3v2Ff5qV1VhEDhBS9SH9yhXXaNQEJBS9Qf9iinoV5Ovr5DisfK3YjE8MoKC18BC55SSuqWbpAAN2IsdIm-HnKChgQ1KrplfpmhsC5Bb_Ti1HrxU50QCfqZOEBH_khntrnb_LgMCnEVPau6Jt3Jrfx4fGAlGYLJ_GAJeez4KjOVWuci3YaWKwev8fpAi5tOxwRdwdyTw0p8t7RkvErZ5bYA3BZgCwgy8rJtN_CbGt7tcKmEhKnJNzVSTFzycu80qkQaErJH4xomUP7obvFKeLLuMEluu4AQkDd9-KvOrqzD6hysaEzBz28yUmLkEJMbvf86UvpnSsWQPPbigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم
🔹
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
🔹
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ» را داشتیم که حالا وضعیت جدیدی پیدا کرده است.
🔹
مهلت ۶۰ روزه در واقع ۶۰ روز فرصت برای مذاکره به‌منظور دستیابی به توافق نهایی بود و اساساً چیزی به‌نام «تمدید آتش‌بس» وجود ندارد.
🔹
قطر و پاکستان به‌عنوان واسطه پیام‌هایی را ردوبدل می‌کنند و با ما در تماس هستند، ولی این به‌معنای مذاکره نیست و تصمیمی برای شروع مجدد مذاکرات با آمریکا نگرفته‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/456146" target="_blank">📅 07:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394c607be7.mp4?token=WEatZyFRRya7TRNdrIVOtpg7qUf9CzmxS0AWx-lXlM5FqVbgwrXSWBPDOc0QRxprvrIQlGDV0mxc24ovg-XR0Zhhsqw6-ChrsAZI2dh4WVf6LMLeCwapKBDPiNsKOdUhPpIVZc9nhE9i2P82cbMq03Zt_MGkdSQJTwJ_grNLasW_-8IB0vDB-mPp-jp5Bf6xTTv7A7XT46sXEO-8cbZcWy-f6OFyaPUNyfz_EM7f6xRFgxnc2dY9u7DHweD7qx2LynkVC33DYlu1uTLbqtYUv6npo47DaK1pseQMnU9qRyZQeYBqTzLYvluBTj0nNbOXl9FUw-mr32rpvrT5litBCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394c607be7.mp4?token=WEatZyFRRya7TRNdrIVOtpg7qUf9CzmxS0AWx-lXlM5FqVbgwrXSWBPDOc0QRxprvrIQlGDV0mxc24ovg-XR0Zhhsqw6-ChrsAZI2dh4WVf6LMLeCwapKBDPiNsKOdUhPpIVZc9nhE9i2P82cbMq03Zt_MGkdSQJTwJ_grNLasW_-8IB0vDB-mPp-jp5Bf6xTTv7A7XT46sXEO-8cbZcWy-f6OFyaPUNyfz_EM7f6xRFgxnc2dY9u7DHweD7qx2LynkVC33DYlu1uTLbqtYUv6npo47DaK1pseQMnU9qRyZQeYBqTzLYvluBTj0nNbOXl9FUw-mr32rpvrT5litBCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌دره‌سی کلیبر؛ روایت سبز جنگل‌های ارسباران
🔹
قلعه‌دره‌سی کلیبر، یکی از جلوه‌های تماشایی طبیعت ارسباران، با چشم‌اندازهای سرسبز و جنگل‌های انبوه، تصویری دیدنی از طبیعت آذربایجان شرقی را پیش‌روی گردشگران قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/456145" target="_blank">📅 05:57 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
