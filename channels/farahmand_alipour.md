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
<img src="https://cdn4.telesco.pe/file/jWXPGVeNDJNu7KZoJPxhu9h7SB0oKcYWtXN6TM1cbmhYDyGV2qI0tjyCjcO73x0bx4xGJTS_EyPh-1nSQhJcRWG5ev_f1wCeo0Sh6gKtO9DCzR-FwAGre3XXC_NMJPsJQOsXoeVvD5svwWY3UW62fTTiwQlYWVw6LfjvmWBWVjUdJrbky4glOemIZ6FKJr3myCu1o0HH1uWp1pAndyUxUuNQNUUnX46OCwKhtlrJUIzJbq2qEA-kOHOiwWp0zJF4ftKLbmADDR1-dYPfxbBcfjNuDnMnb98dOEfKnYnfrQToKxVGq5hVBNQdEemU81UjDfkoxRjc5HhN_GK0CoGb7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8SSHnSVv0tkraq-S0j3cmxJ4wqOgXM9ODWKDy6DMAdLIfHglbVePiF3c5_Zh9Nlyh3alept5cMteNDUHUl8mUl8TejOPyTPU_ne6Df6ciCkx7kFgkbAmfDvTFP2YrGkxDK1NIhQhrQNGcexqhs1b2mwXIF2aMg_X5DnymnesdaF5kGMPy48vbYT54S270ZEF07Me636Y783dksaAhwRyC53Lqt97nicgPP85jCuC1oRl_FRCHoWtvJib89X7ZQFuAP_oqQ9KzLLodHsc4dQrVDeHNSXMy5Bd2ToOJdy58oCyIiY6FvIog0t_zwFz-TtIECH-kM-8SyzVUlIooPc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب با اینکه حملات متوجه شهرهای جنوبی بود، به یک پل راه‌آهن در شمال کشور حمله شد.
در ماه‌های اخیر، جمهوری اسلامی حساب ویژه‌ای روی این مسیر ارتباطی باز کرده بود، هم برای ارتباط با روسیه و هم برای ارتباط با چین.
حجم مبادلات هم ۶ برابر شده بود به ویژه پس
از اعمال محاصره دریایی توسط آمریکا.
فکر نکنم تعمیر این پل ، خیلی زمان ببره.
بیشتر یک اختلال چند روزه خواهد بود.
هدف آمریکا هم بیشتر ارسال یک پیام بود
که جنوب رو محاصره می‌کنیم و می‌تونیم مسیرهای دیگه رو هم از کار بندازیم،
اگه قرار باشه شما مسیر تنگه هرمز رو ناامن کنید.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5974" target="_blank">📅 12:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5973">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-efSmCELSIEbI1PRvIlWvGDBZJzOTGtA3m0Eb0MPLKTEYKxtvfkjCnJi0eV0uOAJGEobWTeI0vu9AAMpr-5-ot_7-UrUMWhgPDf3cEAOS8_vD4tCaZDhEPT3PkYJazOllt7CkmcjgYw0Y1tn1xOowcXfae9mLe0FystExkQv4yhkyQ3ZeK3hyN9eAe-uJUdjPn-vTkgEqhjB_-ip678nOUbKqkfiWqz5mqiO3qVhe0Hhdjj6_AiR77neLbDC6d0uOWrTz9pCtjxyj3V3pHW5jzU35FYH6ogxOLh01wcFhu5v4SErzicibNfxoh_zH5dLuq-5NMRNpMGvptT8kyo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظریم اول
خامنه‌ای پرچم رو تحویل امام زمان بده
و نماز جمعه رو توی بیت‌المقدس برگزار کنه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5973" target="_blank">📅 09:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بیانیه ارتش : به اهدافی در قطر و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5972" target="_blank">📅 09:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62b09d467f.mp4?token=R_MK3GLhsIUk_gatWET9iZr0h-FJgtQKDv-vnBBYmwjn4LGGgBngnnAWaW5Mk-jLdLLi5lU7OAnAQyvyVWeZNjveiCBKxZ8ZPRTmTblCNUFom2sdSbnmGV9iX2GG9n6cDo0bAm-GUPm6OfD3_YtPvlydMUdzzPTWTZi6KUuf_c3LTISK1uThAv2Ouw_ij0P7ab1aU2JRC1VIIF7okgIvlGeXQLKzCaNSp7cqor3017Fka3uBy_nRZFpFYtdLLrnu1Rtcx_tQyyYtOV6NymOOTroQ5WX0R7y_osSKIVSK_qWbEEMuKxrGphyxBHIZWdxPJAfOX1YyXvjC_xKfn_KP3oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانه‌روهاشون : «بهترین حالت برای ترامپ حفظ آتش‌بسه، اما ایران نباید این‌ کار رو بکنه، باید کار دیگه بکنه»</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5971" target="_blank">📅 09:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5970">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=NXtPonxBGuXY9jyfEGkXafR7rHkkBt8MgUUkYzWeNRbThahamPrTPoxps0N04ihfnEBtD-X3xL5pV6rULNnEWEY7BVzKnQW5I1z-GHvT2TWKEzJfMx87cikmbo7fRLTPhsX1JTs57NkHo6LPjdMvDwWQEHpPS64hTe8oZ4buOEjEcBwpe_gtwBLM_iHxDzS921B6y2k37CSGclrWCrWJKM8w0SroZOO_0WWf9Psx9f5quoFR6vry4aiQGJhRvz8D1deie6KjPYqDpHFlP598ofuSKILQEiBkS_TQVwYRGSDpf1G2lzv4y2Ul5b4HXJklicwiwU8P4rlZc0uYjTfcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9d1fd53c.mp4?token=NXtPonxBGuXY9jyfEGkXafR7rHkkBt8MgUUkYzWeNRbThahamPrTPoxps0N04ihfnEBtD-X3xL5pV6rULNnEWEY7BVzKnQW5I1z-GHvT2TWKEzJfMx87cikmbo7fRLTPhsX1JTs57NkHo6LPjdMvDwWQEHpPS64hTe8oZ4buOEjEcBwpe_gtwBLM_iHxDzS921B6y2k37CSGclrWCrWJKM8w0SroZOO_0WWf9Psx9f5quoFR6vry4aiQGJhRvz8D1deie6KjPYqDpHFlP598ofuSKILQEiBkS_TQVwYRGSDpf1G2lzv4y2Ul5b4HXJklicwiwU8P4rlZc0uYjTfcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت خامنه‌ای، پهپاد وار به پنکه کوبیده شد
و موجب آسیب زدن به اموال حرم شد.
یه تشییع جنازه برگزار کردن، هر ساعتش سوژه‌ای داشت.  گویی فیلم‌نامه‌اش
رو رضا عطاران نوشته.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5970" target="_blank">📅 08:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5969" target="_blank">📅 08:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5968">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736101eca8.mp4?token=VtMLdlL1oVUYAIz0JNf4sOCh1hLxilRbs_Dc-wG1jWaPbw3GjoU_27-oUpNcNtG4SHdRzQJvzwy5mtVBNnTRkQpJoLihXO2t7NL6JMWQcPvmzfAkSiOvHNnOVdyujIrOrnAWz154g6gvjNFDGF2YearaZR20ND1gE4ZVypDD2QN_n5RloDrcmRVvWSH5PBf6vWhrOakyszQPdGoXOkq0fSfqY5IV94hXpenXltkKR2d8_IUNk0g-WL4giW2IjL8-0NtXpkSvKoIwJUosfzGf66De2i2W0nZH-iIwsHFDvABXYJEmWFfa1xgzXzL6Gg_V1AeNOCt3ljO3CPJxW4yynA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون داغووون و پلشت دو عالم! برادرانشون در عراق و یمن و افغانستان پلشت‌تر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5968" target="_blank">📅 08:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏استانداری خوزستان: سه کشته و چند مجروح در حمله صبح امروز ارتش آمریکا به اطراف اهواز
مشخص نشده که این حمله به کجا صورت گرفته.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5967" target="_blank">📅 07:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5966" target="_blank">📅 07:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
سنتکام : به ۹۰ هدف حمله کردیم.
🚨
رسانه‌های اسرائیلی : با پایان آتش‌بس، جنگ در تنگه هرمز احتمالا چند روز تا چند هفته ادامه پیدا کند.
🚨
سپاه : به بحرین و کویت حمله کردیم.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5965" target="_blank">📅 06:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=pZS-nPHPbeKg0MEVQyQ4WJapS33I28raohJgajNUTycCTKeHcU8ZSy3x8oqQYC_veaWKQGNQJrajGuMJAGvtTOsgJ6QLh1FE9YgDl4-TEH0eIBCTRZyrkTdVnfoQFKWJDbsas8IfRaTkDYSs7Ye1kmP8S6ia47szsdQHOtSOl7DG0WOBPSbaA8xhDOuHxQ7mVQktLyHxOXrwrKBjlyk0xWhMgfldIObT_GZ_H-kf_CadL8t5m-vdnXDcgIygR-1NAsPIM36FsgdKAPEZVKQ4v3xaWTBtp9jq4r5OfaWzeZoVpG58dxrRaukH6JqyYaQfawyW4or8Dti5xFIKt7wLJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048e36ceb7.mp4?token=pZS-nPHPbeKg0MEVQyQ4WJapS33I28raohJgajNUTycCTKeHcU8ZSy3x8oqQYC_veaWKQGNQJrajGuMJAGvtTOsgJ6QLh1FE9YgDl4-TEH0eIBCTRZyrkTdVnfoQFKWJDbsas8IfRaTkDYSs7Ye1kmP8S6ia47szsdQHOtSOl7DG0WOBPSbaA8xhDOuHxQ7mVQktLyHxOXrwrKBjlyk0xWhMgfldIObT_GZ_H-kf_CadL8t5m-vdnXDcgIygR-1NAsPIM36FsgdKAPEZVKQ4v3xaWTBtp9jq4r5OfaWzeZoVpG58dxrRaukH6JqyYaQfawyW4or8Dti5xFIKt7wLJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏میرباقری در صداوسیما:
‏دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
‏مجری: بله دیگه، رهبر که خودش این حرفا رو میزد رو کشتن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5964" target="_blank">📅 06:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5962">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORSSurMMAI70VJWKO_s1REfizctv1GYft9tL0huNSzppDK2FszGK7HlDCVbNdlnBYGFPBr0XfjDzSfB6qfuHOMx7u3Yhtw1FgHmHH3rHErZDy5kiRRKDg-Lx_63RIxXI66pwvn8jLiUhoL9FYAo70HGjvE1bTLxehivPczEnExNHDa3OzAaZd3nBLCzTJk8AtOu42M-QjyAvWUrnsX1jast-AILDu_HcmU1Qrevub7XSGt8sctrBm8lp0zsX4e-HlYFczZjbBtyq0nh6uOPFk7co6f-YWerMB57bz5MJKn-hBLOk2jc3en9ztt-cYRMyxYO8Lv7wCD8rDM4RQmIaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f05e7ac7.mp4?token=p14IcqOr-WRkkTrHWZlkYq_hN3bHHoHaJzG31hEXwFucrk_UphCABumaEviXbSQ5LNIxD-fCaqegde7ZcfmUk3rBhfLZM99DA_ePmFmq-pyYpQKVIlJl1hX5HnIsc1rDhYXJizYD4me_U55eqUIgqimMfWqf7-OyH9K2U08WjEbRt1kiAx3skZH0hw1W1jv9azm9YWyAtlHvYqsYarRGhM-gqZp5ZvYAYBl3MhjcRL4T1CcocbpTYDRMLQumm2wqQadKmvuujBO9wZzhEasCZaXqaEHgdKsTTm6j5PZpVfHfjKUlN_x7jc_w3KBGxZi1-g1gq3EIS6zxc9bDe2Wz50b9jaIF7QJBMISlB6nPbMexHbsXGFJDVHIBQPHjSof9xuZKVaIhca4EBkJiRd6dqfkSxi5GqjCEF5SD7TYemSGPCwcBMUipPayGAKrMat4LQ4dNZ-bVa0UahtBNPMvD3WYubFLhWSDuIjvm3bKFhMniazaGvVnutpRESl71J2RfuQN7ZuI5Wy4NYbururQiELomt9yspSXdGaLo8oX55sztfR4ifSKxVy0WaQeg1mCnLcm44HXtlue5GVp2I-dIn1AiQaE5IxgF5UHCCMzzym-a8VPPVBp0OinyzASX7uobwMA6A8R07pj1a9nupeoMBIMTMjjR--LjMXCLB-WiKRc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به دو پل در استان گلستان - آق قلا - حمله کرد. یکی از این پل‌ها، پل راه آهن است.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5962" target="_blank">📅 06:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4d0713b6.mp4?token=uIzp1wt9Kfabk5a9_rntuJvkcXFgi3RTi6XakMwOZ085KupYctjxzrpOARdqBWVU7gNBs-LwNB0tEwdGXNw3Jkso2oPzUASWzChPxO-9Ve5qcZiNJeVzzskDZ5rl-aWWnYYvkbGQXi6RKwM8WzumUFkjWgY6SOmPJ5zReN-8LJK_B40WhcnkUyjb4P6ROh-k2S-bQs_D8l_qdBwSb5uFuqbY_Dt0mWYYF7L5bsFz_nJtptIn9B8zl3y12BacA98qDykzQVvmWjTa0CgFgFPVkGCgQWtRWrgNL9yprI_du9DiMerxw0bJmFN44BQ7tm36haoWvZ-0Xt_aE1Cs4r61ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : جمهوری اسلامی یکی بزند، ۲۰ تا می‌خورد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5961" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCpWKK1f6GSdx1XJYF6aT0hQmPwc12h1RS9u4c8-F-oCfckATc-AbLIo1g-1lSj1YbYnqLQn3NosFT-rtYTcQUqL6miPxg_TE-uxT6MEWOxB2wsgkMllbHGPHRduExqRsz-hkX63JKWvVHm_Jd2YeT_90fzVVIlGOftOKEkqBzj87KPPyBG2HeeEBE8xWv3nxIocGYAnzZQxHLbQkqL5bLxs8aZCHVczdFSCJW5-XiHv_6jABE7sNZiA2HA5ehl8xhy2MpR3a_S68Qt_4BNwkxdJnVOSsK7bGQZpavb6UFQaAOxWrFjo1rtVtjyuyN1bgQvhDGAAF9Rie3o6wx-5tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5960" target="_blank">📅 05:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=C0rYXg4AGESmbiarrpUjDZhCkUwUbhCjnwg6Jkxm-pFbASKNBBNND5s4X-6Ed9PdA4p5vuxUiW4TTGYpImVW33lHQfcP0m-7SFZNqzCW1lGCiN3_7_WjeCdnMi0uVYJ6rInyXa3D5-UG-yaXE5Ew2RVbtb96_6BgFgMDNwGQBe0EIYzcoZZeWha8rzl6jBhr48BoxR-_9JL9kjM8K-PMT6RX47sRTbOREpX-s4pjTikOYZHPJUhv-fbXlC3DwC5VcxvKQc6FWQ_AvrkIXfR1P5EeZiQu3xbtKwQP0C8SlCB8XVT2KaHNxAA39DHTenev0kiqX0LFezcES3o4MmdaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=C0rYXg4AGESmbiarrpUjDZhCkUwUbhCjnwg6Jkxm-pFbASKNBBNND5s4X-6Ed9PdA4p5vuxUiW4TTGYpImVW33lHQfcP0m-7SFZNqzCW1lGCiN3_7_WjeCdnMi0uVYJ6rInyXa3D5-UG-yaXE5Ew2RVbtb96_6BgFgMDNwGQBe0EIYzcoZZeWha8rzl6jBhr48BoxR-_9JL9kjM8K-PMT6RX47sRTbOREpX-s4pjTikOYZHPJUhv-fbXlC3DwC5VcxvKQc6FWQ_AvrkIXfR1P5EeZiQu3xbtKwQP0C8SlCB8XVT2KaHNxAA39DHTenev0kiqX0LFezcES3o4MmdaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQbr2QQISjVSia5hYpUZ8i9fYCdVLkSDje6yu5sne8rOE7svuV4afU3gQ-vIYkZ1LCPriPDcIPjLBQf6jP-rX1gvroTzLceNsmGaW9cyYvG7W3CNxGO6GHpL_zn1VMQ8xsLHtTeunRwcMvAW_B8ssGdpuMDRBhR8KFgNwT8pAdBRXJcXmTPNXMe6l_xg7OeyLg6M0FMNfGmiaZ5SrXzwAY0D783h2D0dfiUdar57sRIbVgVBvLFJ9_buGsu35IcbDRB6Cl0gJmVjduyLcB0XOoFL5xpZvpcAhXjNRAc7TW4AvzLZJ-k4x5y_5k1KX5ULDQUri7V1Ag1XInH93CvuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=a6YRUHq-rV24L6flWhgDAVm-Ct-xaM7v2RJhN4octByHVWWN7Xl1iQ8nKLTea0GsxBD2PKOKbKl651eSwuz4p_7FGybtQ2-NMlcGCvywjDqM6TUE8uhcPWHN9EER621LoPXyOVPcrJaqU1_ZJAMEKfn1bp-6hudLF6Ny61Y2vYEqICNJnPf3a9mzJ6cH81Gtms6fglafKY7fmmsE_YjQD5CDDO35R5Eenm23tiSAbjnvgM4X-r1jLWFVfJdDCYKSACi5SHq0r-4KgMYX5XhBdjlfCq7a6Z9gT1P-Bm84wioIXdDYw7EFUmJEveUzmBRilXnX0FedX73xIJyKWnfN5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=a6YRUHq-rV24L6flWhgDAVm-Ct-xaM7v2RJhN4octByHVWWN7Xl1iQ8nKLTea0GsxBD2PKOKbKl651eSwuz4p_7FGybtQ2-NMlcGCvywjDqM6TUE8uhcPWHN9EER621LoPXyOVPcrJaqU1_ZJAMEKfn1bp-6hudLF6Ny61Y2vYEqICNJnPf3a9mzJ6cH81Gtms6fglafKY7fmmsE_YjQD5CDDO35R5Eenm23tiSAbjnvgM4X-r1jLWFVfJdDCYKSACi5SHq0r-4KgMYX5XhBdjlfCq7a6Z9gT1P-Bm84wioIXdDYw7EFUmJEveUzmBRilXnX0FedX73xIJyKWnfN5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoKNV-SH1bSxxp-e9hUTncRC6t-PQiqbIvUFkyWRippYYNXNilQsxcaQW83DfC_ACLzq-HvOqx_Txb42chlkvwqnikxKMppDviuzqR9VdqxH5xDcO5BENLF5dt5YbyNNfZDeDG3XOMNqT48wtFaofwiU-fSUmwKkTp35jObwcA79RRU7QtqICUgHtvRpXe5X3eCeMh37nSaFz8rxEM5kda_7pl6gx7lzt6nf8Miqigz6GHIA5TIRGNgM4aSQlDI-SnHWFE73maLtRi8PaBBtg5HxehtoLwVG4S4rPvRu24BG0M8rEU163qX5NPb-uHzPXEEYSdXt3fmQcQ6u2mdSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=pMSkTdPHoYQbw00xk1pLXZeDHhR0CwFj31gxoos6JwMRUGZgw5HKqBurJFXbm6RrXTQwPnCz5SyXUFn7y0zgvHCBu4cpxP-CF2Vd49JFbqdi2Xd4sXMXTnFBeSO5ZChmUcBb_B-9F9jraEkI8c1Yx3avNtbSZyw5x6tCFO9X_HBjebRkX423LkjP6l5Fzx6-lge2M1pmKZ5780SKHKrGmIbh-bobLfBZb7E2Bu-CtvtlX2cxfL0mIYsxAE8jAsBUmY5TbBgAkN3KoZRzdZ3eBjgNiXozZSDf_eI2e5I6e3hshtvgZX9GV3-bEeWmAmmuqYZbEKorEtI52UWffw2h6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=pMSkTdPHoYQbw00xk1pLXZeDHhR0CwFj31gxoos6JwMRUGZgw5HKqBurJFXbm6RrXTQwPnCz5SyXUFn7y0zgvHCBu4cpxP-CF2Vd49JFbqdi2Xd4sXMXTnFBeSO5ZChmUcBb_B-9F9jraEkI8c1Yx3avNtbSZyw5x6tCFO9X_HBjebRkX423LkjP6l5Fzx6-lge2M1pmKZ5780SKHKrGmIbh-bobLfBZb7E2Bu-CtvtlX2cxfL0mIYsxAE8jAsBUmY5TbBgAkN3KoZRzdZ3eBjgNiXozZSDf_eI2e5I6e3hshtvgZX9GV3-bEeWmAmmuqYZbEKorEtI52UWffw2h6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdIeP9gpzdZz77w1auE91mVRFlWHDBUb7j8TS0O6U2EPp2IT6EPLljeo5hWNDwxDdPCwQsHQ9jeWxVGJFbXUDwfaOc4VcId88TMo8ENL93NYabk9An7GS_QKew6RpglTPxcEcKBpPkb5n3gjZcic4mxY6qkFH_Ys366wAGxaw0fxeZYjLpFOpWgmCH76RoraC08hHJeMsnuOH5oac9BBoiAKuf3gXreGeg3rk3kCUTa22NqFw-JuhNY1o4_nsfPx_4WMVvy2PICWJABoYy95CEpqa5wDBqnpYEDKNhzdwZ52CT3RQCvIytpBqZMfVa2rsrpQLet22ucPDNQZkb4lTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=LjNB-O_B9MqQgqTrVtAkJ41QU04GDCDhd2SPY_GWJBIKKNFi4Ra1N0Ou5DFFzr2SQ5E8MkTJ1twT1bnGE94QDnEIAp2Fu0SJ2VG2Z1oWFaAB4_Q457EQoJKq0QrWa2IAtxyFVZv-tbCQPYYp7cyLURwu-1mK5E4eFEdBBIXeLiSHpEneC8Dj55hmtXHm8mywRhwGm3R4W_1GBBVMtGaVlNltRcODXQgvrcwRhawaozTfbojKt18eMevK0K-bSouLO_2shlGDD9bVTBqLs6ww9Ivn8UrXJzQTbI85tLYQeh8AhN0UrgAbWCwgJRayBLERigLnGyKFpGzJ6odgMeCkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=LjNB-O_B9MqQgqTrVtAkJ41QU04GDCDhd2SPY_GWJBIKKNFi4Ra1N0Ou5DFFzr2SQ5E8MkTJ1twT1bnGE94QDnEIAp2Fu0SJ2VG2Z1oWFaAB4_Q457EQoJKq0QrWa2IAtxyFVZv-tbCQPYYp7cyLURwu-1mK5E4eFEdBBIXeLiSHpEneC8Dj55hmtXHm8mywRhwGm3R4W_1GBBVMtGaVlNltRcODXQgvrcwRhawaozTfbojKt18eMevK0K-bSouLO_2shlGDD9bVTBqLs6ww9Ivn8UrXJzQTbI85tLYQeh8AhN0UrgAbWCwgJRayBLERigLnGyKFpGzJ6odgMeCkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ6dPVSIehbZJFzU8M-L39JojQZGUuqptgZ4DXdg-IMvTjq5dUm6JL2xqxSRsTwB7g5w4GbrgInVWIDQZvEBHG3Q-YbTsb6uYQjQBRQHPF5lSV4Wib-c3h_s_KGsSac-mDxrQgOKWq-EU7zleA50qQ6OmbOfBzqyzVmb-aTKxjgpIQEYdfdMz4c2_GX03hH5OL2nYU6SA0eGililVHEAwCV-nxtweGac0sOz5_-MSKjLY-7EcWtcT4pgERBq-BQeVLlY9fmZnvqiDH6BC0UB6wc0uu-rkcG4YjJdYHTpnxXuSXuv-8kraGWGNXLkvPYmjvkBBcHgucUddnnYYUyNqymk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=KkkseBSes2NikL4SONuUUVQzS8T4vy3vBnjL1RD-JqmMnmyLB_1JHwpsCzWLkVUnWcFuzg4GVlA9wMb1e1NXsiS3Jnd2LpGRlWI_vVRAG1dDtL4mEtt-vYFOEhrf0ma27BD23VK-iRqb5S0n3ntdFJY5sr1XFJqIJCGsAJTt5gGLOANvsjAt4GQ8IfNR7q0sHOTWTPUnEiUWwKTk2JErKEBFO2OjAHMARO8SovUY7jaqiFloO43wc0_h5Nc8PYNWbp6vEWSWsUDz4DVLlVVLEccm5WZKl7n1LEe7KIJiIBntikf4jVqOy8-eweNcIMYbjVM6kyr9SXzLxXZOFzllJ6dPVSIehbZJFzU8M-L39JojQZGUuqptgZ4DXdg-IMvTjq5dUm6JL2xqxSRsTwB7g5w4GbrgInVWIDQZvEBHG3Q-YbTsb6uYQjQBRQHPF5lSV4Wib-c3h_s_KGsSac-mDxrQgOKWq-EU7zleA50qQ6OmbOfBzqyzVmb-aTKxjgpIQEYdfdMz4c2_GX03hH5OL2nYU6SA0eGililVHEAwCV-nxtweGac0sOz5_-MSKjLY-7EcWtcT4pgERBq-BQeVLlY9fmZnvqiDH6BC0UB6wc0uu-rkcG4YjJdYHTpnxXuSXuv-8kraGWGNXLkvPYmjvkBBcHgucUddnnYYUyNqymk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrdbDccmYiJMFR1jFKgxwveU2humWKCctQCPzQJfBbh-pIi1S5OXPmNdFZccVbqXlTCBTqqSLc3q2NiJqr5UvanLjROcTWJ998c1LKCpqOBhw_OKwHFp4utLmg_0uwfG887SUnk0PvN4ojL7knvtWPPOnzWjzeJkRDC8Z_plH2tBrmSSngjDAgKRJVDMBNS-ICwD_yDAO9LZ9WV0jederZd92JSNLaumzPDIlbfUrVyYmDbkXcK5GWf1qCiXgYR6v2tjDf6TmuVn5LGYRsSGoI9zlerPz7DRTVFSTPIsoY0zeWVgotJsBMCaze_y-CMMB9cqVrE6AZ715Cn6XEY39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=rbePIYaa2n8w5gyKc0u2FynX57bzvqSbWe5m24MSypcNXGrsTJ8CMaJEozgdH-b0x9_ZP1oixYPtPsyHaRxImCTsoL0sB2XosduFKNOMh2Q6mAi15b6UPTcxJCb0tdi7S5wIgcRohigXNpId8RfuteUk-hBA3EgwHg0AJ-8wnjhoD2JrFRyCKORiY2fCNMajbdBFr5DCy_4MAtHb81mVrog_d5nRmQAQVK5KcalV9wRtf4LvVAotYX68Zm1blAMxNVR8zThrY6Oli0xuIkbkmNUc9217oGNM3qRH43FDuvoAVBXifaboYFBmQgu5urgmfDNFvwg3eORr138f8Enu2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=rbePIYaa2n8w5gyKc0u2FynX57bzvqSbWe5m24MSypcNXGrsTJ8CMaJEozgdH-b0x9_ZP1oixYPtPsyHaRxImCTsoL0sB2XosduFKNOMh2Q6mAi15b6UPTcxJCb0tdi7S5wIgcRohigXNpId8RfuteUk-hBA3EgwHg0AJ-8wnjhoD2JrFRyCKORiY2fCNMajbdBFr5DCy_4MAtHb81mVrog_d5nRmQAQVK5KcalV9wRtf4LvVAotYX68Zm1blAMxNVR8zThrY6Oli0xuIkbkmNUc9217oGNM3qRH43FDuvoAVBXifaboYFBmQgu5urgmfDNFvwg3eORr138f8Enu2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=R92EOoAP1NDuXtdLId-nRLZjmh4DkMy8SOXyIROh2G8gYGWKIJhO_C7nxMeOGcrKT8GBPzIZS91Gd1cSJqyArjngeHqIpChDM21BGqlRWqnVnIsQDmK1Th2mLBvUqI2-XDtMgmymqVm_JfjeXwOxn0BIVIHX8jFf-Cu98WnvA-pN9_rGKjIcNrVlnckSASoARocn4kP6v2GiRRyiu6nimGdQ2hIuY1ky1SZj6TFQCP_01XALkBcBWIttMkhCQDdG4O30ezDz4Dg0au62SSpiSa8X9U9-Ksb0F_Ql50hd9BRIdhN6eOjHdMpEY4AUiBjoy9DqH5DJeoPna90ySUDGow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=R92EOoAP1NDuXtdLId-nRLZjmh4DkMy8SOXyIROh2G8gYGWKIJhO_C7nxMeOGcrKT8GBPzIZS91Gd1cSJqyArjngeHqIpChDM21BGqlRWqnVnIsQDmK1Th2mLBvUqI2-XDtMgmymqVm_JfjeXwOxn0BIVIHX8jFf-Cu98WnvA-pN9_rGKjIcNrVlnckSASoARocn4kP6v2GiRRyiu6nimGdQ2hIuY1ky1SZj6TFQCP_01XALkBcBWIttMkhCQDdG4O30ezDz4Dg0au62SSpiSa8X9U9-Ksb0F_Ql50hd9BRIdhN6eOjHdMpEY4AUiBjoy9DqH5DJeoPna90ySUDGow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcb5D5BSHyKRvQYK6raR79qckti50hZT5B27EszCKDLi2o1uZpwyt34pOD6DWTtqIJVzffDaJRo3GQDeRiOVwgq3crjh8ifQy0bbKexL2CoxrJR5xOL6LNOUhnsmuTWdYOD15I-GSFPYZRARTB0JcnulPG1rE7YeUPY8hiO1FVYK-U3goocltOHVm8TRAhh1E1JZRYvncdhaPgiXigmQ6gTaEuLCg4pWLEJmQmNimjJPxuzSt55cYEbmEjYOHvOXre4rYeJ04Uo69V2_MzguOKe9HmvdDk-KhjYxrYGaX3J39i55iqiHku_JEe8izAl4QnW-_ASiC3DfL5bIq791YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=OetgsBO2BI4pqgmD0C5lKgBSOX7xNMq0JhYIiWrNb-yAqDH6ugI8GwRH9DTcV2KmC6EVpVxalzA1-eMTBkoQoxnffgpBqVwxMnw1Dsp1tmPPlgu-6rgsHB0uRERs0jt-OxVyPxmZv-wH5syPd1WS4HAWDeFcb6lDT2x5Ney9NmC5aLOgChCWbZ5m1XsQIHrgNNSYqvBTqEVab-o9o0owtfqM-REoroabdxbosBnpWPyT7PaaKiuDnEsI-36QJvxS67xgy_NyJdAnFybDFQHrKjRiyhOZfQTS-ItYJ_6JwAugUbwZ8qtVY0odlWTSENSdVWTdlGJKWGXaMMwR6CBCFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=OetgsBO2BI4pqgmD0C5lKgBSOX7xNMq0JhYIiWrNb-yAqDH6ugI8GwRH9DTcV2KmC6EVpVxalzA1-eMTBkoQoxnffgpBqVwxMnw1Dsp1tmPPlgu-6rgsHB0uRERs0jt-OxVyPxmZv-wH5syPd1WS4HAWDeFcb6lDT2x5Ney9NmC5aLOgChCWbZ5m1XsQIHrgNNSYqvBTqEVab-o9o0owtfqM-REoroabdxbosBnpWPyT7PaaKiuDnEsI-36QJvxS67xgy_NyJdAnFybDFQHrKjRiyhOZfQTS-ItYJ_6JwAugUbwZ8qtVY0odlWTSENSdVWTdlGJKWGXaMMwR6CBCFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=E5JYXRQ--kXXelERk_calkf03nZWZWOOqj571m11qO47yANsIPwij3PH4Rn7vwD9pvUZkrcUuxSceD-7yPggKxC4TYqOQM3k2_b810q13fmk6IGeIgDZTDvUF1CbntiFccYs2KMvlsdD8gFdLB62UhzA6H8VKxY6RKfsF7HgrU3CKp0wr6JfSkHnT8oABd4tRhIgi3SzNTNY1JwCxDVxOsHFx3Z_cjSNeKFYCzWYLuvIykuJMUrqnCrs00nvYHTSDoDGA2A38qCe2MFLHUaFLaXbLDmuC8zYzKSHDDYbiIrUqlpKaULX_O0apQdqGjaKrqwsGGaBHYSXAWDnr8gPng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=E5JYXRQ--kXXelERk_calkf03nZWZWOOqj571m11qO47yANsIPwij3PH4Rn7vwD9pvUZkrcUuxSceD-7yPggKxC4TYqOQM3k2_b810q13fmk6IGeIgDZTDvUF1CbntiFccYs2KMvlsdD8gFdLB62UhzA6H8VKxY6RKfsF7HgrU3CKp0wr6JfSkHnT8oABd4tRhIgi3SzNTNY1JwCxDVxOsHFx3Z_cjSNeKFYCzWYLuvIykuJMUrqnCrs00nvYHTSDoDGA2A38qCe2MFLHUaFLaXbLDmuC8zYzKSHDDYbiIrUqlpKaULX_O0apQdqGjaKrqwsGGaBHYSXAWDnr8gPng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=rHFD8fy-XVM9U71knChGxBTKuP-Zb_aJb8IcP3z9Yn80VaqaWe-2QA1oaZQHx9A-3p4ApCYC2IUdmdnQmbf3u0Dso8wmzRHmBudNY0FQ2KsH7-pZt-SdqyMkwtxhKowmuTT5sPfk7LdS9dXKrCrksQu2xX4XGcxkaB6_xI0-LyeULnsWdRrmCWZxfoK76rz3xpQXLUIOwlOlPVskxAxPz_cQHAFbETkpJLgjpsVn27V_Dc-tG2nTZFz7uZRKaYQN-HJmKDI5JvX4o1JMsjcSM8FbpGEn0v0cAe_a4V_aK690xl1hxScARuIoFg8zWbNOHLveh_-LerBZ2VdfPbIcUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=rHFD8fy-XVM9U71knChGxBTKuP-Zb_aJb8IcP3z9Yn80VaqaWe-2QA1oaZQHx9A-3p4ApCYC2IUdmdnQmbf3u0Dso8wmzRHmBudNY0FQ2KsH7-pZt-SdqyMkwtxhKowmuTT5sPfk7LdS9dXKrCrksQu2xX4XGcxkaB6_xI0-LyeULnsWdRrmCWZxfoK76rz3xpQXLUIOwlOlPVskxAxPz_cQHAFbETkpJLgjpsVn27V_Dc-tG2nTZFz7uZRKaYQN-HJmKDI5JvX4o1JMsjcSM8FbpGEn0v0cAe_a4V_aK690xl1hxScARuIoFg8zWbNOHLveh_-LerBZ2VdfPbIcUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=CorPftxVQ6cEGHMgC1aGAfdI09mUXehiTB3V17XWHJhFJzwLS6X6iI98FkjbfFg-QpRuKIMmZgsMaPKGh7WydIP5M3seWj3mzaHVVxHYlLGqzPaV09Au-Ku_Y_4dgiOst7a56NV3VnD1KxVky_r_nzDYgFDXOT_wHLlRrlbnRLHKpWzMXD78okn5sZGzwRgUExt43OGJ_m7Fcl17IS8k1lM8VlqD_dMy8BN28-szskj4G9PX4W7PrJm3RqrexxHnZoCcITUDbLr7qZCvfmogKdpQLkurBLxYtgeqcrzlOBRVttBLFn1_kU7eokl18qhTawHSINRBy6KbmTzcLRKa-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=CorPftxVQ6cEGHMgC1aGAfdI09mUXehiTB3V17XWHJhFJzwLS6X6iI98FkjbfFg-QpRuKIMmZgsMaPKGh7WydIP5M3seWj3mzaHVVxHYlLGqzPaV09Au-Ku_Y_4dgiOst7a56NV3VnD1KxVky_r_nzDYgFDXOT_wHLlRrlbnRLHKpWzMXD78okn5sZGzwRgUExt43OGJ_m7Fcl17IS8k1lM8VlqD_dMy8BN28-szskj4G9PX4W7PrJm3RqrexxHnZoCcITUDbLr7qZCvfmogKdpQLkurBLxYtgeqcrzlOBRVttBLFn1_kU7eokl18qhTawHSINRBy6KbmTzcLRKa-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=SyIYSlsmZcW3yGuwVxuEyc47wdFXZmJLVo8Is1gd725hROjVFbN3CKiT3hOTxInWkDJtH5w4p8DA3MOE9YM_VSmYapE3VESwXdtndtdP0J2sPAPpf8kyo_EKjIwiSlbEgwwTBklE_VXDQR0mE-VlZf9I_wejIOjxvK849O_eqoJ5fSVPVrJupCp84m0VXqGQupfKv3-Y5KVBaSZZTHMz4_v0feZiWHwyMCymBH1tImaAGvQXbv8S070HhnOaHnJprSIphE_kdNM4CUc-NLxzngHRbfunC3Jb11Le0Bu_45zI5PK_gPgOJaqcD6LvZOEeVhTrM-wzCXaTDQ0nf-vphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=SyIYSlsmZcW3yGuwVxuEyc47wdFXZmJLVo8Is1gd725hROjVFbN3CKiT3hOTxInWkDJtH5w4p8DA3MOE9YM_VSmYapE3VESwXdtndtdP0J2sPAPpf8kyo_EKjIwiSlbEgwwTBklE_VXDQR0mE-VlZf9I_wejIOjxvK849O_eqoJ5fSVPVrJupCp84m0VXqGQupfKv3-Y5KVBaSZZTHMz4_v0feZiWHwyMCymBH1tImaAGvQXbv8S070HhnOaHnJprSIphE_kdNM4CUc-NLxzngHRbfunC3Jb11Le0Bu_45zI5PK_gPgOJaqcD6LvZOEeVhTrM-wzCXaTDQ0nf-vphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-S91SS5x1DCzVvx6VvdPSOVoP7CiAkK-rdCWP2hzB7jixuynPrRe4LhC_3uLJJN9bf5wVM5zvzrEu2SPHrEwpFRJw71ynXf6KDPIWv42DWgJjXoYkgyIqKp6mHyvFS7SJoCbqiRtrZAjg83gN2vkeJbABRrOUzLoYpwpFpyvoW35fH-s_G0Rq6j44FuiXJMqkmtJ80mYqVUjoIjl7Lck1Ht0ym-pCslS-TSNWpeyPAf7ei7jmVhNNoUTfVQutqrrwlcD3nMb01JTrWpnF1JPMyuIJjDbouHowyFx8zit8fBWRubfAAfqKn1gFftyMitF4wUEUw3Nrwd8iFT0iTsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3wTYM_3w3GDWFInbhHxBYIEmTm4HSuF7AlARKucvAaHCHQ6pZmKAbgxVQTGNePyh4VA-OKglOMxT6YR7SZAdpWIwR5m4dYKVNco_bHRojkDL5YVNwPBoZP_1uzVPrCmll0Y9GRdFulFYNERcRq-aeFC_iJNNtWqK_htvLhA6p2b5xZsEOtR6f9jaaD0627HNSQmpSKhZFFYPtHHd85OJ99QTRLgQmtwBwwVFQlqVrQ3pFPT2EeNsc3Qdfnb-ZydUfeMjAkYmFItKgnWJkZibfS84mjU4owQrlhbMfZDmsPpbd84xLoL8G_RXYaIhZt9nRjS5RLHDTK4CTxtEs3OnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2593zKkvcAUEXzIo7XrrrKGrJwcsTMMFh-0KbWFm-MpxdkbOJ83MFGBUe1T11b-6ttfAvN4bQk9yqu9cojRN7W2o5l5HJ-sjamggA44RBMu7u9NxIiW9j-CMI9qCByfFzAV4LcQsqjtENnDfF1v1DdM2jUjFZQl3hf5scxfMq0vX9VNfTZ9jaVboCgzXG6mGBscsfhzCIuzrPiW9JYNhoXkM9PoBQ89j_Znr7YuEUY9GT4KKAsCSlH_fBVZy8kdj2OPbuD5kIobfJ6xDCncq8vgNgZLOdh56Nknt2yUuSxeydiKFwbttu_bd3eNOGUuKr9vM5aE88pJ_RKYGDM7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=r8fK-VjLRDLjAJXD_-ZcJp2dhMsWtbSo7bHkJUHSr05DdOfzJyJTrme5JhoxN1AmaT7RvYW44CpURD1Zj40rPXUg1RekJk46zCDEXzqIT8-eY6jh4yBkgu-O1QdZLK8W-Oc5rjUoIDYQVHRo-byyj1cgVrVbYYVq67TXGf5zVEy-Keu9az66cs3Es_DAeXbmYsDJ4vQMLYYs2EmNzddX3wsIYAxcjxzv9jycDfFWYsiAX8Qcl-utH42WHBhtdXeqbYn6dHuB-SHvWGN6Qg7uDhLjwPVeLegcjs4zH5OJdev5v0HKEgUN5zO0huWXRrHGpGScFEAK0CBTq_GPSBw_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=r8fK-VjLRDLjAJXD_-ZcJp2dhMsWtbSo7bHkJUHSr05DdOfzJyJTrme5JhoxN1AmaT7RvYW44CpURD1Zj40rPXUg1RekJk46zCDEXzqIT8-eY6jh4yBkgu-O1QdZLK8W-Oc5rjUoIDYQVHRo-byyj1cgVrVbYYVq67TXGf5zVEy-Keu9az66cs3Es_DAeXbmYsDJ4vQMLYYs2EmNzddX3wsIYAxcjxzv9jycDfFWYsiAX8Qcl-utH42WHBhtdXeqbYn6dHuB-SHvWGN6Qg7uDhLjwPVeLegcjs4zH5OJdev5v0HKEgUN5zO0huWXRrHGpGScFEAK0CBTq_GPSBw_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob1n-6nC6FNurql3yKrcZ2BfMuOrP9FjeHbjLt-od2XbFuSzi5JUMD0GSvPnFI2gv8eTHwK8eLQWvN9MNvTq4GxZYfWe4XzB8YZQKbBYVxBYRdfLN3td6apri_981Iq-YZ2yp6utfhuVfvkbk6I9IPWPhD8Bm6J4Vzm9iB4jZxfogL9xahv4gF_MsJ_hZad9GO3DumMFb0iH5KFO0qQ3kOSMVT9smftEmiRchuZT1IpDUfxfJFj2E1hRVIjxBzWEWDGdXZAVfaT14EMcWWF2lWNJccG0Ggy8N30fmOQ_zeNH5iqFWNoDtFHuXpqBJII_DX5wX3MuOGz0PqZKDMvJzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=cledvbfOLXlVGvOnIXd728C7dee9A6WgqtJyum8l2ujAfE3C3Lt7FV70kRp8_loa8chcjL3scR682xsiesowVjci6WZrWsOcUNG44EBOUwuQoEOeQeJyTgE85-PHX9N_eH_5qpqu_tuauNXr-DcS0ZQ6sPeotiCuwn2TKPvE3T-_Rcf-ULcSf_3tu28wihpUvMK9RRdjqYOEA_iflnsgsRcrlRG6lEji3wRGqmDcUfpQCkbExFYCFnnjRhUihXg9HmQ_O3mFGDiIXAvuSbGd5yQMo_7TOmhRuLWlMf8PL6D9D99Bln9Ds5CewNzJ-kNjlrIY66-I97VmocaMKGjvEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=cledvbfOLXlVGvOnIXd728C7dee9A6WgqtJyum8l2ujAfE3C3Lt7FV70kRp8_loa8chcjL3scR682xsiesowVjci6WZrWsOcUNG44EBOUwuQoEOeQeJyTgE85-PHX9N_eH_5qpqu_tuauNXr-DcS0ZQ6sPeotiCuwn2TKPvE3T-_Rcf-ULcSf_3tu28wihpUvMK9RRdjqYOEA_iflnsgsRcrlRG6lEji3wRGqmDcUfpQCkbExFYCFnnjRhUihXg9HmQ_O3mFGDiIXAvuSbGd5yQMo_7TOmhRuLWlMf8PL6D9D99Bln9Ds5CewNzJ-kNjlrIY66-I97VmocaMKGjvEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilaHoUm4ut1awacUNlQ1yYISrhl99IyhuGk60zvjMW4-AOcIlE6w7vHo6Ts87EQGyPsG8I5I1BXLcANsk7vza4ITZYe54sCtW1ik-slQoSHgKaTjcgqx3d15ZMtmeEPr0sRXsvalpVIIKarNGIfhgnoaXsSES-xfY1j_qt91_EnD6RT99u23LYHLJYEECB9HCBXBBM5X_RMRoqS4D9josHOA-GpImVACAeWQfcHF-TE3SuE2vhEFCJZ3_ByLBO1uOpP7oc2cbOAu_e6OaRFhxZz9FGAYYpbYfX_j3M4NdRvDMlEBYzJ0CDiscUqMUQIKulD9UQ_zHo7thLF1qhKkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjVyqn2Nu7OOEnTYkJiY8YtCxDCB7IbGzwrcCCEJOEjBhKV2K-joOZoZBjLCee7iu56aZ5EcJ7UyjbCRFsNMYoLchmdcCeCgH5wXXCBgpZZlbj-rSmyvXiRyRFd8CLpeygHPzu8QhojhzC0AbkYWhFtFfQbbFKzRBJPeTnomSsbAF5gytWbTn3BTByyN8Y7tfoLptZhn5faOAAavqcNop3lC8p6I0ZGAy2AmkCX86A6qm47GCshQ5HOA1z9H93RnuwW63w-ZBAhI2O_JiR5LRWlRO7PLqXnHAcrQpJVzMFOXXKG2czpxl7G_7quszhIH893CbkaIBK8W52YPmX41gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=lGvjFGXRmAYRyNyJsWoVXqLfV-Qq1kQNZ_fl6JfllpBxebPG-hQrBplDA6HCd2esaH2ZPvsYL_mXk4-iaWRMFkoIDLy9UViZ_xVkJNqKlguRg2gMVc54IsGP8nM3W7GQjYER5L5xPtSy7Zbjap1IFncrPCTUvF1Ob_Ytth8fqputyqbVbPq6YNGau5TxmiocZv_hocI2rj3YTEx42-n5r3OphQMPvU2OLI8sOqfrgp1T8dewDJhuVWzzoRssdh0pDgMJrCAf41IOUkxNQNOiYmB_sfbga7Tq5tGJwrNc-2ynv6rUQJRN6xERCbKnYGpnvcvT7CZ_yCkze3-liglFLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=lGvjFGXRmAYRyNyJsWoVXqLfV-Qq1kQNZ_fl6JfllpBxebPG-hQrBplDA6HCd2esaH2ZPvsYL_mXk4-iaWRMFkoIDLy9UViZ_xVkJNqKlguRg2gMVc54IsGP8nM3W7GQjYER5L5xPtSy7Zbjap1IFncrPCTUvF1Ob_Ytth8fqputyqbVbPq6YNGau5TxmiocZv_hocI2rj3YTEx42-n5r3OphQMPvU2OLI8sOqfrgp1T8dewDJhuVWzzoRssdh0pDgMJrCAf41IOUkxNQNOiYmB_sfbga7Tq5tGJwrNc-2ynv6rUQJRN6xERCbKnYGpnvcvT7CZ_yCkze3-liglFLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU8wNFSAzccAonfAWwQsohYJ0TgGfO6RUGO7pPO4ASzyfM8rucpNFRhFeJhJRLDvRYMPX4s8QTk4T-Lesjzf0AUkTHZV-M98KNmdx4CZ0VBXbAXEwPYzKRLsSvd6vAzsGP3cVfEOYgipdO2A6lhrlYRkqVFtiTSGF0CLy_h_KmqC5Pt5OPnH8lUFOMCPniP7opgo_if4PaF-zcDzvbCpmi8TH23XZOsdwmSv1VfAYwtxX_CmqMUp5AOBvwycbrlZ7JNL1iswHv84QDBdS6ksqXSE1wE0Sg4Td9m1xlaelLrvlHwDn_bwvPBHZmi2XIhqv3AYYnMtoPSBfHHzHof1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTrCBnxoguW7TGgwEkUXgk-0hV8uPBOZtHBaGfUjM_Np3PZuDJnwmaeHKrr0sTKhnD_MSEzfLfkt3CUKa7iJsawZXI502GAO3Cqw1tYLYAp2UpXG4HpTF8CYtXoBgRP4YDTPlrttqPJWolAaC9QDpWE8-kxc8BwmbqeVFjM5BGmCsLOd9rDZVUIo6a6rdaoF-C6_qI63-W3vhoXDdM5Fa4-NV7LOhqlrCFdiVjUBOvPqzJnWmHlOucVNEB5MaabID9_Z3zUw0PyEs-syvwU466AaRUAfOPhajCktMmjPRuIYA2aCtDOH4PSlYUOeDCoduUMGD9kQ3bbDBSLhLyJv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR4a-_FTS3TKekzHxj3oUxLZO0GmQ5WnfQjoCK38nnDUL-sboyWvW1963Ev6ClX7s7PdVsLLeu_JHgG88Otdax3atNpqlfeDTquCCVSb0neljXZcO8S9-Cxm06zqraLMmUXLkGKtKMjc2toXQNg-fwSCZhSVDEQYNM6eQnWBpwg6TxH42FdLzRmaSTxYIbxKbLYAyFu1t3kiVYRL-_GW_q9jLSZEsOsVVUC7gOyZaAkxYV6YHm7WNHNmEdK5UM-C-luFl8PiMW64Zux1O0oDRuWDO290q6a9Sxn0RCwB8sKtcc_LggQcrC-PPs1i-ZLWtcqnJhjtgFgYMpiqmigW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G60ZvMyF6hkBHPZ3aK06yovHXswL1ukJdXBnT6xfrxngDe9fK29l0TMYZGWh2m21fbKtEGga7fFIbrQ55HyZS9WuQF-oX6FiD35u7L268cgUV8tLhXaWKXx6wnpV2aKviLQhqUEWAt_a9f1cyseuokTxvwAYL1R45-KL143VpoaqUvUKhNJNz4vxKBgyQuZhbEQ5qGip1gyQsLdu0k0HNNk6GJFulR-sVZB-RyMKcP4iMsnQTMOar0inmCN0iOeAHTHDIIdiocHW6ZqRY251d9oGSKpYsu-zICR7i3z9R8Mmf5EWIhzCq2s3PvjvUpIULh6fUP3cM7sHzylYbZAuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPtxC6crewv7nzB08wG6_zWzm-pikSUgtgFVHCumibIrq0Cq4tHfS42r0-2-DpPeTQxJjTkK9EYqs7F9ZXRqe0jkY7zSSaC2TYzAXMFgXFe6NJc7dptOAZXQZYV2K-v-5MLhFWoVJ0CMtcmDY_O_8IYeVUFGhECXTqky7k2d6ykGtsu4I3lYSNtsUQu7sEowhruv0Ycn_BF6ifdO_R3JBfS2pwF8BQnYz8zF7L6ctDoXvwhgJXF_nTuWShmoczZxAaoO3OhBgcvipwYg-zDNU__EDLeJvokKdyBwRcFnGTFTu3aJnOAKwhMIuf1ciaoUZBWUeWg0RG_IlrL40VTb5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfkvrGkCORs9OiG-mTM0CqSYE_yiuJr-ikT_jwknPAKcR4LeeuFuDZIwmMrAV4O_ITWDleqCAYW6BzTiltpYNQ7XkBst0BYkFgtvhEN_lZ4UDWOTTXAmyY9d7zgyjPaBsZA0JjEORPPEXc70gUhVtmjncd29t60mBRMb2WPJEAE7EA7Xsq1Kj69jnpRWahL3WIGgEukaQiqDLSTzVIe5xLqZrv8J88PeX1wHaovT1jbw83JgafYK4hI4epx_N7tOn-zjLBkbilPoL9YuSCwzJTrdT4dR8vWiHnRdctdF6xzWSkaPO16CszqOJ2uvh0wQ11TbPgkFopYrn6ihU4ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=VNLC37mroS1GXHVHYVhZog8bNssqGGhjlR4lfhjYPU3zBiIvw6Wiq5nTfY2bmQZyI5GzCeD3qO2j7Ib3oxe7qX9MiQcN5991hA3sGPUA_hv8cYAtMbf95Ag6wmVY4v0fuWON8AdtuV0QKWw4o6xEBeakkRPmGaQMr9WC0B09OGM6lTbCkvs6GSg3gPUDBY-Z3nF41E2UE4Mscya-QwWB2MxD_gexp1P2uvHyZcCh5PyrqW4zwkgks1prDhwi_3BM8Rp3UnKIrujjq78N2fbxaRx68Eq383saBk7Ei07QpiN3aff2hyqk9o26inv4uiOkNvv4ix2qWNXfGUFF33zR3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=VNLC37mroS1GXHVHYVhZog8bNssqGGhjlR4lfhjYPU3zBiIvw6Wiq5nTfY2bmQZyI5GzCeD3qO2j7Ib3oxe7qX9MiQcN5991hA3sGPUA_hv8cYAtMbf95Ag6wmVY4v0fuWON8AdtuV0QKWw4o6xEBeakkRPmGaQMr9WC0B09OGM6lTbCkvs6GSg3gPUDBY-Z3nF41E2UE4Mscya-QwWB2MxD_gexp1P2uvHyZcCh5PyrqW4zwkgks1prDhwi_3BM8Rp3UnKIrujjq78N2fbxaRx68Eq383saBk7Ei07QpiN3aff2hyqk9o26inv4uiOkNvv4ix2qWNXfGUFF33zR3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuEE226NQXT2g2u60LxMqa9QJJNaYSt56t0OfgNJR31nC9jcAl-8C-IEUnm6ULDa_IaLkNo-UmWBoNm3UKufLdr2QXWy3cV28J8MBxCFwc69i3dlC-QjmP7USFRxBhtj81NA45Qm_iOnDD98VGle-5_rAhrSBaVP9x_-JboblPC8EIFEG8-_BOY_vwG1LfFkJP4n6IXpIYh7WByXI2VH0ayD_obZIj9vANP9kTKJUhqojv1X_NdkTW8P0Wa1NExxLmaI00ymB74rVcJosyVcejRWPkBAOoUrLX5jtEIWolW0kAdvsjdhrqWQb_h18W58HD4MBOS6BjE5s76Tv_N2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=vud2ykINBqJe7vET9TZAqxzr880IUK3y1hYr_hs37XmcWealyYDmTaE5aXytwpM9EDjn_TLJTiNWN3urhHidoBaQ5mkrNQ2eix9y_oXEypT5SSeyBULVuDSID7UCeS5mQ_rWlq0Au3wSfALzmaMmQvXlmzJ_dMqLDgNc_NHgn_Q3PUb7Gh0vXU540VglXMQPg32JCA_F5ItVYDIvb2hRO5-fToo5RHGax25PHqjkSdGBdhdqebiAxxb47djZyyl9BBWpbzFExoNq8EAVPwyv60biE25Z8qVO_s8UwSbSiGySfJKI4lHIIgYaYKneklIeZ-C8ouC6eWImZR-faKCyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=vud2ykINBqJe7vET9TZAqxzr880IUK3y1hYr_hs37XmcWealyYDmTaE5aXytwpM9EDjn_TLJTiNWN3urhHidoBaQ5mkrNQ2eix9y_oXEypT5SSeyBULVuDSID7UCeS5mQ_rWlq0Au3wSfALzmaMmQvXlmzJ_dMqLDgNc_NHgn_Q3PUb7Gh0vXU540VglXMQPg32JCA_F5ItVYDIvb2hRO5-fToo5RHGax25PHqjkSdGBdhdqebiAxxb47djZyyl9BBWpbzFExoNq8EAVPwyv60biE25Z8qVO_s8UwSbSiGySfJKI4lHIIgYaYKneklIeZ-C8ouC6eWImZR-faKCyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=N7b49NuodZeOGw4hwj3e_9HamvGEXJ6cCoEo1RETToqJBRwUmyxlzd6JdMVDjWepLEN071ForyzJumNSJgmhvBpJVz-emN_AkH6DmWauNXNpWu3STcIZCaLQWL39YRAYxFhRSiTNb6uog1EjbqBDDHp2oq21IDoFvKydJng9uBGRHpr13vvuJT81A41-Lm1AxnzavVIcEeG71xxoHEWf70QZmM-6mGSsx3DRNcafjAxdCqGN5NY2bCdxzTdmLkE2qUhNk26aloqyLPj3TbG47t1uMjHvfUCrSj000YhBhy0CB4m9Sc9Ou_ZQvy0r1ZNlEsQpd1xi8sOYlym5VL1dBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=N7b49NuodZeOGw4hwj3e_9HamvGEXJ6cCoEo1RETToqJBRwUmyxlzd6JdMVDjWepLEN071ForyzJumNSJgmhvBpJVz-emN_AkH6DmWauNXNpWu3STcIZCaLQWL39YRAYxFhRSiTNb6uog1EjbqBDDHp2oq21IDoFvKydJng9uBGRHpr13vvuJT81A41-Lm1AxnzavVIcEeG71xxoHEWf70QZmM-6mGSsx3DRNcafjAxdCqGN5NY2bCdxzTdmLkE2qUhNk26aloqyLPj3TbG47t1uMjHvfUCrSj000YhBhy0CB4m9Sc9Ou_ZQvy0r1ZNlEsQpd1xi8sOYlym5VL1dBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuE1kvfJuxLYXGtG3W826DgMMy-1f26AB-UDIDadAxiKCn0d8ZzEKOwRd_5_5BO_PdoIBWSOeVnhKfTyIiGEzeVKNMV5eHe_QVYNX35RdomRbHhZhYINroXsBqdcTpyujC1UL32HXl2FFwZ7SLaelyWhmas0MSUhVVJDNKJmLEZr1OIYWBhaUY43oig0Q_d5uptfmkfeJbnjZvuLg3iQqRXSL-wFhcaBcKdxrivjz1qnX4wXbDDtjtaeKlmFSkMPAKrwhf-NhYXDNkXTF5pfbmL_LHUiuQYtbftxN8abrtViTGoVuRqzLSj1wekFAM-RI2TAY4r7gqsKZbBMvAcTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=uutH0IN-N4S4itTHkjxoqMQbaMfeq0vrzQVc2rOejYYgnQeKlyQtlg5D5WEWfsbLc5jgZAP45-Vg6TppZcBnWtRtwyZp49lOlN2U7uLdz_wBCemX484iUm7HJlN2wqrO99u2ZWC5NgwKD0iEYmy7QE_FKPKFFlaEa6YDh2KauixisiqRXmu5HWE07a002uEPSvGuJ74tUGOmLr72zwO2iagRutX7BfkY1Mo4lwsQH7Uk8Ocp1WtxmrC4uJnbiAVFI554NRAo0jyYZ1L9zwbGdPQ9WBCDmayKXDDyPZ5_DiZRAbABlJOIIFyXJgjYIbz61CwVFP93dijMGRAqhD0QpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=uutH0IN-N4S4itTHkjxoqMQbaMfeq0vrzQVc2rOejYYgnQeKlyQtlg5D5WEWfsbLc5jgZAP45-Vg6TppZcBnWtRtwyZp49lOlN2U7uLdz_wBCemX484iUm7HJlN2wqrO99u2ZWC5NgwKD0iEYmy7QE_FKPKFFlaEa6YDh2KauixisiqRXmu5HWE07a002uEPSvGuJ74tUGOmLr72zwO2iagRutX7BfkY1Mo4lwsQH7Uk8Ocp1WtxmrC4uJnbiAVFI554NRAo0jyYZ1L9zwbGdPQ9WBCDmayKXDDyPZ5_DiZRAbABlJOIIFyXJgjYIbz61CwVFP93dijMGRAqhD0QpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHsrG8Gxg7ySJ5RINnDy-hiVjg9RfiYe6XnaLxbV3vqIqK3Llo-mjuudWCH9wvQcbKo2mQ9Te1_djyYtTBxUCqsinwezqFbBSdwqdmDHbhlMBn_7FNpsPLZDxkZnoi9aQMHl2R1fMRU6Z4Vmu0Hr9ds5Xgzc51nhgWjzvL6APYDsS-PtE6y_pJ7PzuB1wQzYpt_ZHQ6qcIh2MQIhjtCKmxv5YnlQJtZ2ajJGF_MEtsqaoW7yQjYMsedYxrLt09x9VRo4R4_ix4EB31bRjJTLdtGilzKzRJYPwv-PhUg7YZTxpEzkQNEtP3Khf0NxIsvD4LsZ_7RI_RaUdLKPUUSJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK53WUx7ziHNxBdlSN1gdhYDaY8sdk3_pYv7HvgN-Kl6PZArqoFyhwmQKFbjcned_13T7E2NGhIDT-mGa93E0SU6A63X7ZmGfwTMsc64YdSonm7ecsnZdwk8IpiBwgzug43PLx5paCu-nrh5nEB8L9Yy_TLoNGBWUhye1GE1O_O6B2WDUqt_UxnN0tDy1n2220ZFXhpv9gCDlCQ23BAPj7MGzvUsk9snLKtLCM0HE6X4oavYiPWVPqIzwixk-1RLXk2rir8n7OYmDBfTUJBdwldRBwPvRhH7hxWxr4inIDTpQ3-9AieFYTmmgDbPYtFcWzPw1pjUxzWHOt_Lm6Rcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJY50gj8fbSAVHxaPg6DhFfVltApVbIh-OkTXXw1e4cv5rQHwmrB7ZEzIVV-ocdhEdMXplTWXdyW-TXUUYHrKMLWKuhj0sVauZRXK1K_-x3DnDkirGCULLkf-PBZqsqj2kOlSD_xPa0tJ9ABueGFjyLbgvtI7WGgc5FEFZwAK1tmKlKZcrGl5cEU8CLg5ymyjjO4-WEOd3MIkU4qztq8HRp3Rnafw0c-7FDW7yRqWjh-GiHCJYVb5zlKKewiPmQmhqIrINgLnLhWbgVrSWhCAPzkEemgjpROs7i0QucwxptYcqYO8e5mZimmAFD_2Fm38-t-hES0N7ONHBhkYVYE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwIbKni1VAqU4mQKSYC9V_-vm1YEWxLVlwRB_CiLulBNhnaejln9diCRXPAPHRWgx2RlB4MsJtT-m1XTZK4MqCn0ZkzxuRqc9A5znQDdu7qWw9rwoXU3Y3esy0XT3LFgkgv17diEZkRVt9dxZ_smd15AxQk0DB3SjEKQZX8KLv_U_9GKbyPmBUmWsBKHVeXzdIQgfgNjOKxcsdQE2ih_FsMMnQqN-Iitu5RUT55v9Vfey6SbF0cdvO1wOnR_ngsnXq-d6gke2bHgs758Hzt4RPq_azrWJ1fkJv7hlff4RrB_UobUMpUQZIzUARVn34DhhSPPDe7Jd0gtLpNAyrjNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tejdvwkF0RBYnx_e-I3qmPtu4sz_JieuKWZmJYjEoVLnre0RwKENXDkce3FuvD_WDZICTG_0ASRg-5FJtUZg0TS5LExZ_MOpK_tuf3L6rFSaPMN2wqWW98O5ElPxEZ7_BBLncX3VDsTs56jDINv1_IFMiXx11z1_RLmgPMmiN_cTzMHxDSMiBi1WASN7qXq3sOMO6X3lxUP_lFrvFZW3yQDDE_A7gL1SKrEektoL6ZUFVruVQzK8sNoUlemT8-nWdDq8bygklcmArSkP-P6whlQZLFLYWkbvmy3joRMJq85yLlSox3yQFcTXChTIBkChuwHZvda_dJlWNZ1zjj63HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zwd0fUEU2Z4oez9XwGjV-gMsN6zvkQiwVC43SNbxBs3jPB2-pnTJRF0abnej_Wc_NpyzAGAdcHhKQaH-ZhNP7xPO2X9S6ifsDJSEwTrBzxEzz9WgvXHF8I5Qpk9DMqZOQJ1SpLOggdicon2PXYr4eHhBSp2VUYVRJBzcSsdjEmXGFw0NNmZqdgWfA8-dwc-sHIehfYBocxOP1PjGsA2s_1mJ5nFdWOZtQK8L0Zx7FjdGLuzYiYHaKrO7xsWjUw70EXrOiMdlj9MjEc8ZbncQeIbc5AWP6m0n3dDtXYARqwEZt-h_8VzzyJ1rr3fuo7kZxw7UMITd6HGhTkpcCrRSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=HXpn09wlAEu2aplEAruIfLH-E_613f-1hK5-CoMUO-5SCUfWexjS15j6dxjValWHOXEKnQyv7uQVo6knuikW-Uac8fg5ak30kP9aKVGmgM7L9FDB1JtBC_eziOm3_R-tcyclrQ7OOB3tY8Z6MpZD4hwkzP_YW8bN09vvNShpfZjDtF1XmBD6M-R1u4rC1UFCbhFea6wbyEm7x1SUpjh2B7X0phkgbvwwML9dyV1aGBWPaop_nrMkoNMczGwQbT3thpyINUg6Xis_OYTanPMYuW_2HXvonTrA5Hnmh2fL79Lh2LVmIYaI5_O02bK-aJz37q9FYJY1wT5NTkxn1811Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=HXpn09wlAEu2aplEAruIfLH-E_613f-1hK5-CoMUO-5SCUfWexjS15j6dxjValWHOXEKnQyv7uQVo6knuikW-Uac8fg5ak30kP9aKVGmgM7L9FDB1JtBC_eziOm3_R-tcyclrQ7OOB3tY8Z6MpZD4hwkzP_YW8bN09vvNShpfZjDtF1XmBD6M-R1u4rC1UFCbhFea6wbyEm7x1SUpjh2B7X0phkgbvwwML9dyV1aGBWPaop_nrMkoNMczGwQbT3thpyINUg6Xis_OYTanPMYuW_2HXvonTrA5Hnmh2fL79Lh2LVmIYaI5_O02bK-aJz37q9FYJY1wT5NTkxn1811Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=lG2JyrUp-2ACnuqyxnTgHgOzZlSaRaDpNdxpQyDAYwxPv-iv1hYRjyJTfVmt99OcYPP5Tb7eHf0loYPqOHSvBoW7DhMmkQlwF1Zlv7BlEaH8xwBzFaVJUbpwWqn952cQ3c9HoC1WIWil21LntqVZ8Is-evC3ExYqMrERitHQjm5eR8Tczjbaz_8btD2qJIOzG_T4-xtZhYdCabhlrr0-EqkS2ejFvNhr8joWh2WoTbCB2cZtMBhW3s-5Q574zTDDcU1JNjCVtfakfLJX-jaB5VGfApmhYsPx_bL3gJmz1dl_M7X3yxCHQ35I2bEWK-ju6tGV76-GF3d1v2dHvfJLWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=lG2JyrUp-2ACnuqyxnTgHgOzZlSaRaDpNdxpQyDAYwxPv-iv1hYRjyJTfVmt99OcYPP5Tb7eHf0loYPqOHSvBoW7DhMmkQlwF1Zlv7BlEaH8xwBzFaVJUbpwWqn952cQ3c9HoC1WIWil21LntqVZ8Is-evC3ExYqMrERitHQjm5eR8Tczjbaz_8btD2qJIOzG_T4-xtZhYdCabhlrr0-EqkS2ejFvNhr8joWh2WoTbCB2cZtMBhW3s-5Q574zTDDcU1JNjCVtfakfLJX-jaB5VGfApmhYsPx_bL3gJmz1dl_M7X3yxCHQ35I2bEWK-ju6tGV76-GF3d1v2dHvfJLWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=G3n6LTvNNGjq5e4OyMhPChiQyKbv9O-uGI0HybdgwqVGI753kMhEGbRlxFgG5IrQ_I3-xcW2r3xq0Z5MplgD8xoWC-pEAm-VrE9BtL_hOxGNunYoRka9vlM8ginhNR9pJ5qnD1o9TH-yyCp7_vw_35qasyOqKKvDSTMd1Gi4n_OJODqY8GYgoKco1qqydkSFlSjBu9ZAjPUQJ2C_LX9rnWVFZNQnELsWBv6n1SzqTFpaObaLwiFbgOm4OddyjQOwiQe77mDweNT0cpdXEPpuPicr4Y5SpM87wjAA2LPEnsULyBbFJ7UEOeEi1pS9F-tGywxUo1bcKdKtm9wl_quKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=G3n6LTvNNGjq5e4OyMhPChiQyKbv9O-uGI0HybdgwqVGI753kMhEGbRlxFgG5IrQ_I3-xcW2r3xq0Z5MplgD8xoWC-pEAm-VrE9BtL_hOxGNunYoRka9vlM8ginhNR9pJ5qnD1o9TH-yyCp7_vw_35qasyOqKKvDSTMd1Gi4n_OJODqY8GYgoKco1qqydkSFlSjBu9ZAjPUQJ2C_LX9rnWVFZNQnELsWBv6n1SzqTFpaObaLwiFbgOm4OddyjQOwiQe77mDweNT0cpdXEPpuPicr4Y5SpM87wjAA2LPEnsULyBbFJ7UEOeEi1pS9F-tGywxUo1bcKdKtm9wl_quKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=srd9Si4aBCE1eaf5b6m1Z9mqAO1u_-rgNwcNEzxPyT7oFc1B42CzeSMziGcxLm8I0yhBjlo9INBzVX88vorZxP21qG82YuZlc5kFai0cebbc9dX9iWyF7Hr6kJgd5VR7qMZ8orqglgaWjBOgXc9J2CRxZEfhjC0pGHs9he2sCDi6YDAyDs6O3B4JQYHQ7nMZvXyJGnfK-FqsKxFWR9BHyi_ZsEixudEFsnaVFbwge5bE478rlXyLQqy5qsYHr0vpwaZimFY0P2ydX0i-JxDNhb-ZcIocy4v9rgo4ui9qkONlGHXXHDq_uAtk3a9f_E5y8SDrGeGM--l2EaWkmsKTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=srd9Si4aBCE1eaf5b6m1Z9mqAO1u_-rgNwcNEzxPyT7oFc1B42CzeSMziGcxLm8I0yhBjlo9INBzVX88vorZxP21qG82YuZlc5kFai0cebbc9dX9iWyF7Hr6kJgd5VR7qMZ8orqglgaWjBOgXc9J2CRxZEfhjC0pGHs9he2sCDi6YDAyDs6O3B4JQYHQ7nMZvXyJGnfK-FqsKxFWR9BHyi_ZsEixudEFsnaVFbwge5bE478rlXyLQqy5qsYHr0vpwaZimFY0P2ydX0i-JxDNhb-ZcIocy4v9rgo4ui9qkONlGHXXHDq_uAtk3a9f_E5y8SDrGeGM--l2EaWkmsKTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xksm6NoTfb0p3RMFCZziZNiaYqfJH7NmktJpDOFKG6JpXXG_SgcLx7fFpWp90rzBHelnPC2ygKaXdxTY4rJHgP0coKPwNJ6JZXUsGkQhxpvfEuW5PQrkkYawejvxD_gQvU5qqqTIwH4xM5NPDKsjMOLGd8rbE7ObdAvCxJqJDzh1EXZGV4Ge_rrxQMLys1CwjmpwNreptxVWVuTW0A0NMpalsqyltpCkPBMS_T4lkHYAAteCCyVmKy8v7UFM1tJJH3en6Fp6bDQnpWhi8fkQS4gCswqYB2y5IllYu_xRnRAlTLwk_uvb7th7nmtnshSkjhF-UVnJwfAu7MHj8v7CnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=PCPDlDTDytuz2PCTlESZKFfa83E6U9qABqR47kZhabXt2zUc62uFW_kN0l99-iRFjg03Pp-LlfI0gcoe6Q2Gibb-hO-6TALYUFloaunsuFxHjRva0qUZ3y1pGJSWGeqD2airgJLJ15-ILsek8QGVOGCoFW7UudiXyiBaZBxxCHaMNqS_DN0eGLmonrnasb0kLZGkZI5ten0TBBwviWjTMsqq1cS7ANyAgnOc03dcVB_QGMLZ6IGCEe4eT6w1Oa2QAtggknV5qMXLDS8QLTdWPL-1GXFKAZrD6d9mHdNo2JhzniI8k7bUf86AXfFwzXgJ2gH3S3dNvYOvq9G8X0knfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=PCPDlDTDytuz2PCTlESZKFfa83E6U9qABqR47kZhabXt2zUc62uFW_kN0l99-iRFjg03Pp-LlfI0gcoe6Q2Gibb-hO-6TALYUFloaunsuFxHjRva0qUZ3y1pGJSWGeqD2airgJLJ15-ILsek8QGVOGCoFW7UudiXyiBaZBxxCHaMNqS_DN0eGLmonrnasb0kLZGkZI5ten0TBBwviWjTMsqq1cS7ANyAgnOc03dcVB_QGMLZ6IGCEe4eT6w1Oa2QAtggknV5qMXLDS8QLTdWPL-1GXFKAZrD6d9mHdNo2JhzniI8k7bUf86AXfFwzXgJ2gH3S3dNvYOvq9G8X0knfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktsPZymnIar17oasfcfWp1ltLGHzqmGqTmZyMj9mt20jGuhJa3hW25ew8jHpmVdmLwVVtKVPCPf8OB_RvqtgLJdQ_IjoxpUkG2N0yclL8YQJIBmPM0_70AkgB31SxRFyho27tV5AP1hS_mA1DE_6_AY0XFRb8McDi9r5QXyqKNQVq68iWLjZ5F1Y_yc8I3IrRFKIWWQQUNxc_wYE7PRpH-AtqD5Z9ecbO5mIxr_9ae-gZCvPlWt77KhkrHOXTwaowXuX04Sbj7h4pQm99hLTs8mbDMP9MF0WzWz5Hn62tDSS7hWY_QfjPz5WXI-4HCPfa7kQ-WSd3p0lxW64f1HBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=WMHv2TfzUdTLa95EDHyWt2RyVyDCFHlkh7Ftcq99ZPA_iInpKAkUZeuPy1bI04XMma4MlhpWhez7usAzrOXpqA9m_J6CuWGf2qg3DBpBzQ70Pkzu2aR1L6jjkQq27c_t8-71wBvolMSsemoZgEPdqxN1wm8LpRjIUv6RiR30tIw8gHKRM9IW9jsIBCGCAyj1S6YGPxmYgncsXPYECbL4bkbgDBamO9-aAa6I5ry9uKUbpNJcDn-HRZ5H-agAyMLm8T35Vtt5adblwO49x96wI5PFMtRw2i6sr1NUdfpICgfwgzKaVlWDC7osX6A3Tc0ni1q5SaGDpIl_LF7rHRCmqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=WMHv2TfzUdTLa95EDHyWt2RyVyDCFHlkh7Ftcq99ZPA_iInpKAkUZeuPy1bI04XMma4MlhpWhez7usAzrOXpqA9m_J6CuWGf2qg3DBpBzQ70Pkzu2aR1L6jjkQq27c_t8-71wBvolMSsemoZgEPdqxN1wm8LpRjIUv6RiR30tIw8gHKRM9IW9jsIBCGCAyj1S6YGPxmYgncsXPYECbL4bkbgDBamO9-aAa6I5ry9uKUbpNJcDn-HRZ5H-agAyMLm8T35Vtt5adblwO49x96wI5PFMtRw2i6sr1NUdfpICgfwgzKaVlWDC7osX6A3Tc0ni1q5SaGDpIl_LF7rHRCmqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=mZaY8nP2Cw8BGUriSzMBsroVozEgOJBXtsNgTrnt7eCaBW-iXZS0bZAQMY2qq2nffWrcs2AQRrKOxs3S2k8aLymBSwyKEJcMS4kZvrXAYMN3EI2EbZg6JbRye79xP3xUMKDH6sY4wn-3SptTY8WMVEzyPkDowTv1Mrrfb_RqZHFSEjs2OwAOijA0_7O19bxL_osgKK-WRa6Hqv5kukWhJPjYqomYo3NNU7wQP_AjYOzaNVvkMM30sX0Lhn85nsW0fYL1mgSrvVOmQ4yAsNZRA0LhhH1Fr8mEg58sNhkxlg0HvXcaIKNKqt3G_H4I8ebsKpOdhKPrifmngsY1kHyJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=mZaY8nP2Cw8BGUriSzMBsroVozEgOJBXtsNgTrnt7eCaBW-iXZS0bZAQMY2qq2nffWrcs2AQRrKOxs3S2k8aLymBSwyKEJcMS4kZvrXAYMN3EI2EbZg6JbRye79xP3xUMKDH6sY4wn-3SptTY8WMVEzyPkDowTv1Mrrfb_RqZHFSEjs2OwAOijA0_7O19bxL_osgKK-WRa6Hqv5kukWhJPjYqomYo3NNU7wQP_AjYOzaNVvkMM30sX0Lhn85nsW0fYL1mgSrvVOmQ4yAsNZRA0LhhH1Fr8mEg58sNhkxlg0HvXcaIKNKqt3G_H4I8ebsKpOdhKPrifmngsY1kHyJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=N2jxoAmmefrTseWnEFlHnHtezjuQEhhuvnnw6VJW1WneTdODZXD852k_22gsG1CtWHVoJqEIi4Yk4QGZl1iCqPKlT9pnE2VVSMuvMPi25rPkSgECpiTbaG2wwnBfa_XQGcHF77Jb6Y17XVHXUOlUoHJEKSTO59J006NDvz347hJHRC667nGEy-_vpXQUU0anQMJvMUBCXkE-o9weJi2Mt1Hlx0g7NqSIPxP8ZuIXiXEwYNrdOMKVh1D-XfiD4VzwRilZWYYgaMUt-MVz80oFiiyrzAqU9jnE4Tb0XDdSlhGbH7fCMPp8uYyPLrf-j0YDpOK8KmoKMIsEsPGcQRNFlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=N2jxoAmmefrTseWnEFlHnHtezjuQEhhuvnnw6VJW1WneTdODZXD852k_22gsG1CtWHVoJqEIi4Yk4QGZl1iCqPKlT9pnE2VVSMuvMPi25rPkSgECpiTbaG2wwnBfa_XQGcHF77Jb6Y17XVHXUOlUoHJEKSTO59J006NDvz347hJHRC667nGEy-_vpXQUU0anQMJvMUBCXkE-o9weJi2Mt1Hlx0g7NqSIPxP8ZuIXiXEwYNrdOMKVh1D-XfiD4VzwRilZWYYgaMUt-MVz80oFiiyrzAqU9jnE4Tb0XDdSlhGbH7fCMPp8uYyPLrf-j0YDpOK8KmoKMIsEsPGcQRNFlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=E3M8fAxMS75YVzZYNVrMWJQmoh-AwkjaMk9x6CeXd2dCoSZEUVpepaBnYne5oiFDS5ZVheLID38wX7H5X7OXdE1undx3FhejRyabLm-rBMPKP4LoNc2I0vfoTbqaQ5yJzukSF-Vk-zFNpOi_TObARfNrt-9ISi52iHhy0LuCsjYf53mlgQyv--1irT8RxEW1BGw85gpqQMZzItOYjZxlGz4VtwYiD8qdZr0vUeAKGKkEn2BI861Ghzrx3cKo4_5eFbsvZcQqBVg9RF4lRcc0DDD_Fe9jx_nsLpV-OTGjRISiX_faKFGVM_oCoZal42ixP_ezLvu9CGzB40gChS5gCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=E3M8fAxMS75YVzZYNVrMWJQmoh-AwkjaMk9x6CeXd2dCoSZEUVpepaBnYne5oiFDS5ZVheLID38wX7H5X7OXdE1undx3FhejRyabLm-rBMPKP4LoNc2I0vfoTbqaQ5yJzukSF-Vk-zFNpOi_TObARfNrt-9ISi52iHhy0LuCsjYf53mlgQyv--1irT8RxEW1BGw85gpqQMZzItOYjZxlGz4VtwYiD8qdZr0vUeAKGKkEn2BI861Ghzrx3cKo4_5eFbsvZcQqBVg9RF4lRcc0DDD_Fe9jx_nsLpV-OTGjRISiX_faKFGVM_oCoZal42ixP_ezLvu9CGzB40gChS5gCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=duNsB3pY_mISnOJtJJYdK_CPDu_Vv1SAGSiEpTKbANoUJC_Z0gSGDsWRKDdtl6Sd6S6t0-vvSOrxWh2YiH_8oH2agAlmkkvr3mw1JzBtRGsvu3DkPwDAF0m4OaQPutwA3jEUlxUWUCdCP0oIcbW0X1B1byUVO-viFaeJJDCVLxLelPLuNIDNoOKyhT2MhDgfy1aJrCjobKJLquu9MmbN2I2jejnsmYBp6xjwhpxZ5_R8onOHVYybNrU1W8WVUHCiN9dBKvlF12CjfAMeScJxv1zeKwpzUizgrfUwIYjD9nPkQW5mdTyPzoQfPI5rPcgL3LI4gNuujrYfr40pFbFPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=duNsB3pY_mISnOJtJJYdK_CPDu_Vv1SAGSiEpTKbANoUJC_Z0gSGDsWRKDdtl6Sd6S6t0-vvSOrxWh2YiH_8oH2agAlmkkvr3mw1JzBtRGsvu3DkPwDAF0m4OaQPutwA3jEUlxUWUCdCP0oIcbW0X1B1byUVO-viFaeJJDCVLxLelPLuNIDNoOKyhT2MhDgfy1aJrCjobKJLquu9MmbN2I2jejnsmYBp6xjwhpxZ5_R8onOHVYybNrU1W8WVUHCiN9dBKvlF12CjfAMeScJxv1zeKwpzUizgrfUwIYjD9nPkQW5mdTyPzoQfPI5rPcgL3LI4gNuujrYfr40pFbFPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=cVz9vqXR2jl9nBPfyxIC61ET710dDTYn8iS8-aziPkAYkoB30yj7PpSAcx3jur2Jo-_BYJesvj9QScgAUFLt_16kcUBZyWcV8xRtXPlCtaWdEkukZLFUHjLOz1S5mTVr9JM-sSsyMLJa5wBUQFXR8tL7f5KLDWidtwQEKIUwf0GO9LfzXJU6E4apZGhXwHu_dDNh-2SwAGjl8TnGnFpyF_xruozsWgRbWiIv6K8t3I4cWHyAOCz0sLkXvaOSgG3jVDVZf8MLqnuaZ2QEqtoLWfNfOoeB9y1MLpcP38ViwoUNUWraaWD_-GMEqCYiTfROynW6wzCY5wqRIs8etz4VEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=cVz9vqXR2jl9nBPfyxIC61ET710dDTYn8iS8-aziPkAYkoB30yj7PpSAcx3jur2Jo-_BYJesvj9QScgAUFLt_16kcUBZyWcV8xRtXPlCtaWdEkukZLFUHjLOz1S5mTVr9JM-sSsyMLJa5wBUQFXR8tL7f5KLDWidtwQEKIUwf0GO9LfzXJU6E4apZGhXwHu_dDNh-2SwAGjl8TnGnFpyF_xruozsWgRbWiIv6K8t3I4cWHyAOCz0sLkXvaOSgG3jVDVZf8MLqnuaZ2QEqtoLWfNfOoeB9y1MLpcP38ViwoUNUWraaWD_-GMEqCYiTfROynW6wzCY5wqRIs8etz4VEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=OtXGSHn1rnIxbxEa5cdqvyz3MIFGEK4GlDyXTKE_yOHaH5vVk2nGu0IxtVLg_jVU-6PTyT0JjGhEjadoUasbjzsH5LSMTioDEV3rGe8ColykY6ULsn4NPyBILW9MrqTB3G3x1T4a1uNkgSpkjTK5qo0UxpHfVeexbu1IaoR0s0aBuhoOhxeWOLyHA4UtNTFPxbvFuzK1V47e53QOaywxftglWiz40z2p9RQs1Sl7uVYmwyWhTkFCGCgq8ZPm5X53OnArQu1WtKVAQxSUN_WkLjvfoEOSFLdskGYNvePtNVNjPkYlyP432KMbb1sdR4zHD65e6tUaXL3VLpqNig-hng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=OtXGSHn1rnIxbxEa5cdqvyz3MIFGEK4GlDyXTKE_yOHaH5vVk2nGu0IxtVLg_jVU-6PTyT0JjGhEjadoUasbjzsH5LSMTioDEV3rGe8ColykY6ULsn4NPyBILW9MrqTB3G3x1T4a1uNkgSpkjTK5qo0UxpHfVeexbu1IaoR0s0aBuhoOhxeWOLyHA4UtNTFPxbvFuzK1V47e53QOaywxftglWiz40z2p9RQs1Sl7uVYmwyWhTkFCGCgq8ZPm5X53OnArQu1WtKVAQxSUN_WkLjvfoEOSFLdskGYNvePtNVNjPkYlyP432KMbb1sdR4zHD65e6tUaXL3VLpqNig-hng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0xqcFAIs2noRnL3-mk8VEscd1kYYuUxT_aYol-ir_OZb7ClciL_tBTZY6Lb3h50wRKfJ1tMm-QWL8MSgPh4Sk5hAkKyVavfgC9NtX_bLS-p-2uWt0JKC5vnt0lp73jp7uH8iIx21EBOyxYXLknMrL6BjBP6hG_kmoOav8Wvy6LRaMrwiiGZm0vfZ7wcpotBGIurSkF5unstoCz9tkmZ8ye4JJXNbVzEwfBi7nwOjrjfiFcvMpuUyd8Zj8bRTxdYbn9U0SDoXB0kBUlO7oIVr4MiKqVSQQPzpVT-2-MMSqu2sPyhgqQw5HKVGGfU9mD8J4EIa3jOta29aTJFOIdu_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTn4-3mDYWOGsETPHFQIG2sVRjg74itJAlDTr9uHzai9XfmXPZdRDR1J90V8OruKXg4LmRVsmKMkYRwTto9wEOjuwjWeeS6sUrXkAd8gcFLalvc4F-RtnlVMaTijG17KVTgw64Irj9cz11QvscJqJeUhpdH-R7BZhVvg98_lUMK8sVuybpCno1Lc5YmC_uICj6DNjbBrjjqdoIcKDquPI2kemPM7BWHP-OjLueQ_ov50_csd7JgKncmMjCXXId2xwcPbAbnDdaZ_p3bsszxHI5IJ1kuYf5VyljkXiw1pXtKCTe9cRQqgen66mIatUvesgHMQCL0z5KoWZpqFuIjfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=sd_ltZMDe5vUmhGAjMrk23HoBDF4urr9FS32fv1d2fMPO8oOpdDuAJ8eA3DBoVdgDq-N7vE6E0zLtJsaV9sIUn7DqGv3_rHUwX551PZqh6kImSulgI-iGbSYjdr11ccei5WFdGHJfEXv-QZJRyPMsgROTFRwW2-L97Z9tmlOC9xmzZvkUGFGBpKk8xi9P8c1gqPCYfOGrx2k-OXpR1M26Tn3mlQvf5zBOdZoo00DOpaM1cgydpvN7DhpnEA2l4xdc8d81OodF9qylK46ddknL5oQFkDmtXs2FdR_wnaR6QfFnZY4tYrKaqaNGz9mQ2HmfFoXT40L1GnCCAFVkJAQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=sd_ltZMDe5vUmhGAjMrk23HoBDF4urr9FS32fv1d2fMPO8oOpdDuAJ8eA3DBoVdgDq-N7vE6E0zLtJsaV9sIUn7DqGv3_rHUwX551PZqh6kImSulgI-iGbSYjdr11ccei5WFdGHJfEXv-QZJRyPMsgROTFRwW2-L97Z9tmlOC9xmzZvkUGFGBpKk8xi9P8c1gqPCYfOGrx2k-OXpR1M26Tn3mlQvf5zBOdZoo00DOpaM1cgydpvN7DhpnEA2l4xdc8d81OodF9qylK46ddknL5oQFkDmtXs2FdR_wnaR6QfFnZY4tYrKaqaNGz9mQ2HmfFoXT40L1GnCCAFVkJAQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
